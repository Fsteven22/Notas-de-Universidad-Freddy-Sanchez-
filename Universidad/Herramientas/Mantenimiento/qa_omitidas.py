#!/usr/bin/env python3
"""qa_omitidas.py — lista las notas de Universidad/ que el sitio NO publica.

El gate de publicacion es silencioso: una nota sin `dg-publish: true` en su
frontmatter queda fuera del sitio sin ningun aviso (hoy son ~9-28 segun la
tanda). Este script hace visible esa lista, agrupada por semestre/materia,
para poder decidir nota por nota si la omision es deliberada o un olvido.

Reglas que replica (mismas que site/scripts/sync-vault.mjs):
  - Solo se publican las notas bajo Preuniversitario/, 1er/2do/3er Semestre/
    y las de la raiz de Universidad/. El resto (Herramientas/, etc.) no entra.
  - Se lee el frontmatter con utf-8-sig: un BOM UTF-8 al inicio del archivo
    rompe el parseo y deja la nota fuera del sitio sin razon aparente.

Convenciones del vault (Mantenimiento/):
  - Corre DRY por defecto (solo reporte): es de solo lectura, no modifica nada.
  - --vault <ruta>  raiz del vault (default: deducida desde la ubicacion del script)
  - -o <reporte>    escribe reporte en archivo (default: solo consola)
  - --estricto      exit code != 0 si hay notas omitidas (para CI)
  - Excluye: .obsidian, .trash, .git, node_modules y la nota espejo
             _Test Callout Fences.md (sus ejemplos son intencionales)

Uso:
  py qa_omitidas.py
  py qa_omitidas.py --vault "C:\\...\\OneSyncFiles" -o omitidas.txt
  py qa_omitidas.py --estricto
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Ruta del vault deducida desde la ubicacion de este script:
# Universidad/Herramientas/Mantenimiento/qa_omitidas.py -> 3 niveles arriba
def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules")
SKIP_FILES = ("_Test Callout Fences.md",)
SEMESTER_IDS = ("Preuniversitario", "1er Semestre", "2do Semestre", "3er Semestre")
MD_EXT = (".md", ".markdown")
FRONT_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---", re.DOTALL)
PUBLISH_RE = re.compile(r"^\s*dg-publish\s*:\s*(true|false)\s*$", re.IGNORECASE | re.MULTILINE)
BOM = "\ufeff"


def estado_nota(path: Path):
    """Devuelve ('publica'|'omitida'|'revisar', detalle)."""
    try:
        raw = path.read_text(encoding="utf-8-sig")  # utf-8-sig se come el BOM
    except Exception as e:
        return "revisar", f"no se pudo leer: {e}"
    if raw.startswith(BOM):
        return "revisar", "BOM UTF-8 al inicio (rompe el parseo del frontmatter)"
    m = FRONT_RE.match(raw)
    if not m:
        return "revisar", "sin frontmatter"
    fm = m.group(1)
    p = PUBLISH_RE.search(fm)
    if not p:
        return "revisar", "frontmatter sin linea dg-publish valida"
    return ("publica" if p.group(1).lower() == "true" else "omitida"), ""


def grupo_de(rel: Path):
    """(semestre, materia) a los que pertenece la nota, o None si no es publicable."""
    partes = rel.parts
    if len(partes) == 1:
        return ("raiz (Universidad/", rel.stem) if False else ("Universidad (raiz)", "-")
    top = partes[0]
    if top in SEMESTER_IDS:
        materia = partes[1] if len(partes) > 2 else "(sin materia)"
        return (top, materia)
    return None  # Herramientas/ y afines: el sitio no los recorre


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--vault", default=raiz_por_defecto(), help="raiz del vault")
    ap.add_argument("-o", "--output", default=None, help="archivo de reporte")
    ap.add_argument("--estricto", action="store_true",
                    help="exit code != 0 si hay notas omitidas")
    args = ap.parse_args()

    vault = Path(args.vault)
    uni = vault / "Universidad"
    if not uni.is_dir():
        print(f"ERROR: no existe {uni}", file=sys.stderr)
        return 2

    publicadas, omitidas, revisar, fuera = [], [], [], []
    for md in sorted(uni.rglob("*")):
        if not md.is_file() or md.suffix.lower() not in MD_EXT:
            continue
        if any(p in SKIP_DIRS for p in md.parts) or md.name in SKIP_FILES:
            continue
        rel = md.relative_to(uni)
        g = grupo_de(rel)
        if g is None:
            fuera.append(rel.as_posix())
            continue
        estado, detalle = estado_nota(md)
        fila = (g[0], g[1], rel.as_posix(), detalle)
        (publicadas if estado == "publica" else omitidas if estado == "omitida" else revisar).append(fila)

    # ── resumen ─────────────────────────────────────────────────────────
    total = len(publicadas) + len(omitidas) + len(revisar)
    lineas = []
    lineas.append(f"qa_omitidas — vault: {vault}")
    lineas.append(f"notas publicables revisadas: {total} "
                  f"(publica: {len(publicadas)} · omitida: {len(omitidas)} · revisar: {len(revisar)})")
    lineas.append("")

    grupos = {}
    for filas in (omitidas, revisar):
        for sem, mat, rel, det in filas:
            grupos.setdefault((sem, mat), []).append((rel, det))

    lineas.append("=== Omitidas / a revisar por materia ===")
    for (sem, mat) in sorted(grupos):
        por_mat = [f for f in grupos[(sem, mat)]]
        pub = sum(1 for s, m, _, _ in publicadas if (s, m) == (sem, mat))
        lineas.append(f"\n## {sem} / {mat}  (publican {pub}, no publican {len(por_mat)})")
        for rel, det in por_mat:
            lineas.append(f"  · {rel}" + (f"  [{det}]" if det else ""))
    if not grupos:
        lineas.append("  (ninguna: todas las notas publicables tienen dg-publish)")
    lineas.append("")
    lineas.append(f"=== Resumen por materia (solo no publicadas) ===")
    for (sem, mat) in sorted(grupos):
        lineas.append(f"  {sem:18s} {mat:55s} {len(grupos[(sem, mat)]):4d}")
    lineas.append(f"\nFuera del alcance del sitio (no se recorren): {len(fuera)} archivos "
                  f"(Herramientas/, etc.)")

    texto = "\n".join(lineas)
    print(texto)
    if args.output:
        Path(args.output).write_text(texto, encoding="utf-8")
        print(f"\nreporte escrito en {args.output}")

    if args.estricto and (omitidas or revisar):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""qa_assets_huerfanos.py — detecta assets del vault que ninguna nota publica referencia.

Escanea toda la carpeta Universidad/ en busca de archivos de imagen/diagrama/PDF
que existan en el vault pero que ninguna nota referencie mediante ![[...]] o [[...]].
Sirve para identificar material huérfano que ocupa cuota y nunca se publica.

Convenciones del vault (Mantenimiento/):
  - Corre DRY por defecto (solo reporte). --apply no aplica aqui: es solo lectura.
  - --vault <ruta>  raiz del vault (default: deducida desde la ubicacion del script)
  - -o <reporte>    escribe reporte en archivo (default: solo consola)
  - Exit code != 0 si hay hallazgos (para CI)
  - Excluye: .obsidian, .trash, .git, node_modules, y la nota espejo
            _Test Callout Fences.md (sus ejemplos son intencionales)

Uso:
  py qa_assets_huerfanos.py --vault "C:\\...\\OneSyncFiles" -o reporte.txt
  py qa_assets_huerfanos.py --vault "C:\\...\\OneSyncFiles" --apply
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Ruta del vault deducida desde la ubicacion de este script:
# Universidad/Herramientas/Mantenimiento/qa_assets_huerfanos.py -> 3 niveles arriba
def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules")
SKIP_FILES = ("_Test Callout Fences.md",)
ASSET_EXTS = {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".pptx"}
WIKI_RE = re.compile(r"!?\[\[([^\]]+)\]\]")


def norm_name(s: str) -> str:
    """Nombre base sin extension, minusculas, para comparar robusto."""
    return os.path.splitext(s)[0].lower()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--vault", default=None, help="raiz del vault (default: deducida)")
    ap.add_argument("--apply", action="store_true", help="(no-op: este script es solo lectura)")
    ap.add_argument("-o", "--salida", default=None, help="ruta del reporte de salida")
    args = ap.parse_args()

    vault = os.path.abspath(args.vault) if args.vault else raiz_por_defecto()
    uni = os.path.join(vault, "Universidad")
    if not os.path.isdir(uni):
        print(f"Universidad/ no existe en: {vault}")
        return 2

    # 1. Indexar todos los assets existentes en el vault
    assets_existentes = {}  # nombre_lower -> ruta completa
    for dp, ds, fs in os.walk(uni):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            ext = os.path.splitext(f)[1].lower()
            if ext in ASSET_EXTS:
                assets_existentes[norm_name(f)] = os.path.join(dp, f)

    # 2. Recopilar todos los nombres de asset referenciados por notas .md
    referidos = set()
    for dp, ds, fs in os.walk(uni):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            if not f.endswith(".md"):
                continue
            if f in SKIP_FILES:
                continue
            ruta = os.path.join(dp, f)
            try:
                raw = Path(ruta).read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for m in WIKI_RE.finditer(raw):
                target = m.group(1).strip()
                # quitar alias y ancla
                target = target.split("|")[0].split("#")[0]
                referidos.add(norm_name(target))

    # 3. Assets que existen pero nadie referencia
    huerfanos = []
    for nombre_lower, ruta in sorted(assets_existentes.items()):
        if nombre_lower not in referidos:
            huerfanos.append(ruta)

    # 4. Reporte
    total_assets = len(assets_existentes)
    total_referidos = len(referidos & set(assets_existentes.keys()))
    lineas = [
        f"assets en el vault: {total_assets}",
        f"assets referenciados por notas: {total_referidos}",
        f"assets HUERFANOS (sin referencia): {len(huerfanos)}",
        "",
    ]
    for ruta in huerfanos:
        rel = os.path.relpath(ruta, vault)
        lineas.append(f"  HUERFANO: {rel}")

    reporte = "\n".join(lineas) + "\n"

    if args.salida:
        with open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(reporte)
        print(f"reporte escrito en: {args.salida}")
    else:
        print(reporte, end="")

    return 1 if huerfanos else 0


if __name__ == "__main__":
    raise SystemExit(main())

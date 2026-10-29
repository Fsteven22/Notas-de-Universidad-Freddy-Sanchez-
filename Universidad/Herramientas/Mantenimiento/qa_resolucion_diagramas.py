#!/usr/bin/env python3
"""qa_resolucion_diagramas.py — verifica que cada embed de diagrama resuelva a un archivo real.

Recorre todas las notas .md del vault y, para cada wikilink/embed que apunte a un
archivo dentro de una carpeta "Diagramas" (o que termine en .svg/.png/.mmd),
verifica que el archivo objetivo exista. Resuelve relativo a la nota, a cualquier
carpeta ancestro, y por sufijo de ruta en cualquier parte del vault (como lo hace
Obsidian).

Convenciones del vault (Mantenimiento/):
  - Corre DRY por defecto (solo reporte). --apply no aplica aqui: es solo lectura.
  - --vault <ruta>  raiz del vault (default: deducida desde la ubicacion del script)
  - -o <reporte>    escribe reporte en archivo (default: solo consola)
  - Exit code != 0 si hay hallazgos (para CI)
  - Excluye: .obsidian, .trash, .git, node_modules, y _Test Callout Fences.md

Uso:
  py qa_resolucion_diagramas.py --vault "C:\\...\\OneSyncFiles" -o reporte.txt
"""

import argparse
import os
import re
import sys
from pathlib import Path

def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules")
SKIP_FILES = ("_Test Callout Fences.md",)
ASSET_EXTS = (".svg", ".png", ".jpg", ".jpeg", ".pdf", ".mmd", ".pptx")
WIKI_RE = re.compile(r"!?\[\[([^\]]+)\]\]")


def norm_name(s: str) -> str:
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

    # Indexar todos los archivos del vault por nombre (para resolucion por sufijo)
    indice = {}  # nombre_lower -> set de rutas relativas
    for dp, ds, fs in os.walk(uni):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            ruta = os.path.join(dp, f)
            rel = os.path.relpath(ruta, uni)
            indice.setdefault(norm_name(f), set()).add(rel)

    bad = []
    total = 0

    for dp, ds, fs in os.walk(uni):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            if not f.endswith(".md"):
                continue
            if f in SKIP_FILES:
                continue
            ruta_nota = os.path.join(dp, f)
            try:
                raw = Path(ruta_nota).read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            nota_dir = os.path.dirname(ruta_nota)

            for m in WIKI_RE.finditer(raw):
                target = m.group(1).strip()
                # quitar alias y ancla
                target = target.split("|")[0].split("#")[0]
                if not target:
                    continue
                total += 1

                # Solo chequear targets que parezcan archivos (tienen extension o apuntan a Diagramas/)
                if not (target.lower().endswith(ASSET_EXTS) or "Diagramas" in target or "/" in target):
                    continue

                resuelto = False

                # 1. Relativo a la nota
                if os.path.exists(os.path.join(nota_dir, target)):
                    resuelto = True
                else:
                    # 2. Ancestor folders
                    d = nota_dir
                    while True:
                        if os.path.exists(os.path.join(d, target)):
                            resuelto = True
                            break
                        if d == uni or os.path.dirname(d) == d:
                            break
                        d = os.path.dirname(d)
                if not resuelto:
                    # 3. Desde la raiz del vault
                    if os.path.exists(os.path.join(uni, target)):
                        resuelto = True
                if not resuelto:
                    # 4. Por sufijo de ruta en cualquier parte del vault (Obsidian)
                    clave = target.replace("\\", "/").lower().lstrip("/")
                    for rel in indice.get(norm_name(target), set()):
                        if rel == clave or rel.endswith("/" + clave):
                            resuelto = True
                            break

                if not resuelto:
                    rel_nota = os.path.relpath(ruta_nota, vault)
                    bad.append(f"  BAD: {target}  [en {rel_nota}]")

    lineas = [
        f"embeds de diagrama/asset revisados: {total}",
        f"embeds NO resueltos: {len(bad)}",
        "",
    ] + bad + [""]

    reporte = "\n".join(lineas) + "\n"

    if args.salida:
        with open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(reporte)
        print(f"reporte escrito en: {args.salida}")
    else:
        print(reporte, end="")

    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

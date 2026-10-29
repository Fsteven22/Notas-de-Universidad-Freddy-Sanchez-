#!/usr/bin/env python3
"""qa_svg_titulo.py — detecta SVGs con titulos placeholder que quedaron sin sustituir.

Escanea todos los archivos .svg del vault y extrae el elemento <text> con clase
"flowchartTitleText" (generado por mmdc / Mermaid). Si el titulo es un placeholder
generico (ej. "Concepto clave", "Titulo del diagrama", "Diagrama", "Grafico")
reporta el archivo para que se le asigne un titulo real.

Convenciones del vault (Mantenimiento/):
  - Corre DRY por defecto (solo reporte). --apply no aplica aqui: es solo lectura.
  - --vault <ruta>  raiz del vault (default: deducida desde la ubicacion del script)
  - -o <reporte>    escribe reporte en archivo (default: solo consola)
  - Exit code != 0 si hay hallazgos (para CI)
  - Excluye: .obsidian, .trash, .git, node_modules, y _Test Callout Fences.md

Uso:
  py qa_svg_titulo.py --vault "C:\\...\\OneSyncFiles" -o reporte.txt
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

# Titulos placeholder genericos que indican que el SVG nunca se le puso uno real
TITULOS_PLACEHOLDER = {
    "concepto clave",
    "titulo del diagrama",
    "diagrama",
    "grafico",
    "titulo",
    "placeholder",
    "sin titulo",
    "mermaid diagram",
}

TITLE_RE = re.compile(r'class="flowchartTitleText">(.*?)</text>', re.DOTALL)


def limpiar_titulo(raw: str) -> str:
    """Elimina etiquetas HTML internas y espacios de sobra del texto del title."""
    t = re.sub(r"<[^>]+>", "", raw)
    return " ".join(t.split()).strip()


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

    sospechosos = []
    total_svg = 0

    for dp, ds, fs in os.walk(uni):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            if not f.lower().endswith(".svg"):
                continue
            if f in SKIP_FILES:
                continue
            total_svg += 1
            ruta = os.path.join(dp, f)
            try:
                raw = Path(ruta).read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            m = TITLE_RE.search(raw)
            if not m:
                continue
            titulo = limpiar_titulo(m.group(1))
            if not titulo:
                continue
            if titulo.lower() in TITULOS_PLACEHOLDER:
                rel = os.path.relpath(ruta, vault)
                sospechosos.append(f"  {rel}  (titulo: {titulo})")

    lineas = [
        f"SVG escaneados: {total_svg}",
        f"SVG con titulo placeholder: {len(sospechosos)}",
        "",
    ] + sospechosos + [""]

    reporte = "\n".join(lineas) + "\n"

    if args.salida:
        with open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(reporte)
        print(f"reporte escrito en: {args.salida}")
    else:
        print(reporte, end="")

    return 1 if sospechosos else 0


if __name__ == "__main__":
    raise SystemExit(main())

# -*- coding: utf-8 -*-
"""verifica_fuentes_mmd.py - busca SVG sin fuente .mmd al lado (y viceversa).

Recorre una carpeta (por defecto todo Universidad/) y reporta:
  1. cada .svg que NO tiene su .mmd homónimo al lado (problema principal);
  2. cada .mmd que NO tiene su .svg homónimo al lado (huérfano, solo aviso).

El contrato de la casa exige que cada diagrama SVG publicado lleve su fuente
Mermaid (.mmd) en la misma carpeta, para que siga siendo re-editable.

Uso:
    py -X utf8 verifica_fuentes_mmd.py [carpeta] [-o reporte.txt] [--solo nombre]

Ejemplos:
    py -X utf8 verifica_fuentes_mmd.py "Universidad/2do Semestre/Programación orientada a objetos"
    py -X utf8 verifica_fuentes_mmd.py "Universidad" --solo Diagramas
    py -X utf8 verifica_fuentes_mmd.py -o reporte_faltantes.txt
"""
import argparse
import io
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKIP = {".git", "__pycache__", ".obsidian", "site", "node_modules", "SVG-Pipeline"}


def escanear(raiz, solo=None):
    """Devuelve (sin_mmd, mmd_huerfano, total_svg, total_mmd)."""
    raiz = Path(raiz)
    sin_mmd = []
    mmd_huerfano = []
    total_svg = 0
    total_mmd = 0

    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in SKIP]
        # si se pidió --solo, saltar carpetas que no coincidan
        rel = os.path.relpath(dp, raiz)
        if solo and solo.lower() not in rel.lower():
            continue

        for f in fs:
            nombre = f.lower()
            if nombre.endswith(".svg"):
                total_svg += 1
                svg = Path(dp) / f
                mmd = svg.with_suffix(".mmd")
                if not mmd.exists():
                    sin_mmd.append(svg)
            elif nombre.endswith(".mmd"):
                total_mmd += 1
                mmd = Path(dp) / f
                svg = mmd.with_suffix(".svg")
                if not svg.exists():
                    mmd_huerfano.append(mmd)

    return sin_mmd, mmd_huerfano, total_svg, total_mmd


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("carpeta", nargs="?", default=".",
                    help="raíz a escanear (default: .)")
    ap.add_argument("-o", "--reporte", help="guarda el reporte en este archivo")
    ap.add_argument("--solo", help="solo carpetas cuyo camino contenga este texto")
    args = ap.parse_args(argv)

    sin_mmd, mmd_huerfano, total_svg, total_mmd = escanear(
        args.carpeta, args.solo)

    lineas = []
    lineas.append("=== Verificación de fuentes .mmd ===")
    lineas.append(f"Raíz escaneada: {os.path.abspath(args.carpeta)}")
    if args.solo:
        lineas.append(f"Filtro: carpetas que contengan '{args.solo}'")
    lineas.append("")
    lineas.append(f"SVG encontrados:      {total_svg}")
    lineas.append(f".mmd encontrados:     {total_mmd}")
    lineas.append(f"SVG sin .mmd al lado: {len(sin_mmd)}")
    lineas.append(f".mmd huérfanos:       {len(mmd_huerfano)}")
    lineas.append("")

    if sin_mmd:
        lineas.append("SVG sin fuente .mmd (problema principal):")
        for s in sorted(sin_mmd):
            lineas.append(f"  SIN-MMD  {s}")
        lineas.append("")

    if mmd_huerfano:
        lineas.append(".mmd sin .svg al lado (huérfano):")
        for m in sorted(mmd_huerfano):
            lineas.append(f"  HUÉRFANO  {m}")
        lineas.append("")

    if not sin_mmd and not mmd_huerfano:
        lineas.append("Todo OK: cada .svg tiene su .mmd al lado.")

    reporte = "\n".join(lineas) + "\n"
    print(reporte)

    if args.reporte:
        io.open(args.reporte, "w", encoding="utf-8", newline="\n").write(reporte)
        print(f"Reporte guardado en: {args.reporte}")

    return 1 if (sin_mmd or mmd_huerfano) else 0


if __name__ == "__main__":
    raise SystemExit(main())

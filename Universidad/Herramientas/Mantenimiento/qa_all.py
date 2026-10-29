#!/usr/bin/env python3
"""qa_all.py — punto de entrada unico para los 4 scripts de auditoria de Mantenimiento/.

Ejecuta en orden:
  1. qa_assets_huerfanos.py      assets del vault sin referencia de ninguna nota
  2. qa_resolucion_diagramas.py  embeds de diagrama/asset que no resuelven
  3. qa_fugas_copyright.py       archivos excluidos que se siguen publicando
  4. qa_svg_titulo.py            SVGs con titulos placeholder sin sustituir

Cada script corre DRY por defecto (solo reporte). Pasa --apply si un script lo
soporta y toca archivos. Usa -o para escribir reportes individuales.

Convenciones:
  - --vault <ruta>  raiz del vault (default: deducida desde la ubicacion de este script)
  - Exit code != 0 si cualquier script encuentra hallazgos (para CI)
  - Los scripts viven en la misma carpeta que este archivo

Uso:
  py qa_all.py --vault "C:\\...\\OneSyncFiles"
  py qa_all.py --vault "C:\\...\\OneSyncFiles" -o reporte_qa.txt
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "qa_assets_huerfanos.py",
    "qa_resolucion_diagramas.py",
    "qa_fugas_copyright.py",
    "qa_svg_titulo.py",
]


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--vault", default=None, help="raiz del vault (default: deducida)")
    ap.add_argument("--apply", action="store_true", help="pasa --apply a cada script")
    ap.add_argument("-o", "--salida", default=None,
                    help="prefijo para archivos de reporte (se le anexa el nombre del script)")
    args = ap.parse_args()

    vault = os.path.abspath(args.vault) if args.vault else raiz_por_defecto()
    aqui = os.path.dirname(os.path.abspath(__file__))

    print(f"Vault: {vault}")
    print(f"Scripts: {len(SCRIPTS)}")
    print("=" * 70)

    codigo_global = 0
    for nombre in SCRIPTS:
        ruta_script = os.path.join(aqui, nombre)
        if not os.path.isfile(ruta_script):
            print(f"\n[SALTADO] {nombre}: no existe")
            continue

        cmd = [sys.executable, "-X", "utf8", ruta_script, "--vault", vault]
        if args.apply:
            cmd.append("--apply")
        if args.salida:
            base = os.path.splitext(nombre)[0]
            cmd.extend(["-o", f"{args.salida}_{base}.txt"])

        print(f"\n--- {nombre} ---")
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        # Imprimir solo la parte de reporte (sin el "reporte escrito en" de consola)
        salida = r.stdout
        if args.salida:
            # Quitar la linea de "reporte escrito en" de la salida de consola
            lineas = [l for l in salida.splitlines()
                      if not l.startswith("reporte escrito en:")]
            salida = "\n".join(lineas)
        print(salida, end="")
        if r.returncode != 0:
            codigo_global = 1
        if r.stderr:
            print(f"[stderr] {r.stderr}", file=sys.stderr)

    print("\n" + "=" * 70)
    print(f"QA completo. Exit code: {codigo_global}")
    return codigo_global


if __name__ == "__main__":
    raise SystemExit(main())

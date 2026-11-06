# -*- coding: utf-8 -*-
"""mmdc con la fuente recortada: reemplazo directo de `mmdc` en los scripts del pipeline.

Mermaid CLI incrusta la tipografia "Recursive Variable" completa (4 subconjuntos, ~160 KB de
base64) dentro de cada SVG. Este wrapper hace lo mismo que `mmdc` y ademas deja la fuente
recortada a los glifos que usa ese diagrama: el SVG se ve igual y pesa una quinta parte.

Uso (igual que mmdc, pero con el wrapper):
    py -3.12 mmdc_ligero.py -i diagrama.mmd -o diagrama.svg -b white
    py -3.12 mmdc_ligero.py -i diagrama.mmd -o diagrama.svg -b white -s 2

Todos los argumentos se pasan tal cual a mmdc.
"""
import os
import shutil
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import subconjuntar_fuente  # noqa: E402


def mmdc_path():
    cand = os.path.join(os.environ.get("APPDATA", ""), "npm", "mmdc.cmd")
    if cand and os.path.isfile(cand):
        return cand
    return shutil.which("mmdc") or shutil.which("mmdc.cmd") or "mmdc"


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        raise SystemExit(1)

    salida = None
    for i, a in enumerate(args):
        if a == "-o" and i + 1 < len(args):
            salida = args[i + 1]

    exe = mmdc_path()
    r = subprocess.run([exe] + args, capture_output=True, text=True)
    if r.stdout:
        sys.stdout.write(r.stdout)
    if r.stderr:
        sys.stderr.write(r.stderr)
    if r.returncode != 0:
        raise SystemExit(r.returncode)

    if salida and salida.lower().endswith(".svg") and os.path.isfile(salida):
        try:
            info = subconjuntar_fuente.aplicar(salida)
            print("[fuente recortada] %s: %d B -> %d B (%s)" % (
                os.path.basename(salida), info["antes"], info["despues"], info["estado"]))
        except Exception as exc:                      # pragma: no cover
            print("[AVISO] no se pudo recortar la fuente de %s: %s" % (salida, exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import argparse, re
from mdlib import walk_notes, load, report

# Error 7: contenido que la convencion del vault manda dentro de callouts
# y esta suelto fuera: tablas, formulas $$...$$ y listas de datos.
# Detecta los bloques de riesgo y los lista (no toca nada: crear un callout
# requiere elegir titulo/tipo, decision humana; el script da la fila/linea).
# Uso: python detect_fuera_callouts.py "<carpeta>" -o reporte.txt

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("-o", default=None)
args = ap.parse_args()

FUEGO = ["tablas", "formulas", "datos"]

filas = []
for p, rel in walk_notes(args.root):
    lines = load(p).split("\n")
    fence = False
    bloque = []
    inicio = None
    def vaciar():
        global bloque, inicio
        if bloque and inicio is not None:
            filas.append("%s:%d-%d :: %d linea(s) fuera de callout [%s]" % (
                rel, inicio + 1, inicio + len(bloque), len(bloque), " ".join(set(b[0] for b in bloque))))
        bloque, inicio = [], None
    for i, ln in enumerate(lines):
        if ln.strip().startswith("```"):
            fence = not fence
            vaciar()
            continue
        if fence or ln.startswith("---") or (i == 0 and ln.strip() == "---"):
            continue
        es = ln.lstrip().startswith(">")
        tipo = None
        if not es:
            if ln.strip().startswith("|"):
                tipo = "tablas"
            elif ln.strip().startswith("$$"):
                tipo = "formulas"
            elif re.match(r"^\s*(\d+[\.\)]\s|\- \*\*)", ln) and any(sym in ln for sym in ("=", "^", "\\frac", "$")):
                tipo = "datos"
        if tipo:
            bloque.append((tipo, ln))
            if inicio is None:
                inicio = i
        else:
            vaciar()
    vaciar()

print("bloques-fuera-callout=%d" % len(filas))
if args.o:
    report(args.o, ["bloques=%d" % len(filas)] + filas)

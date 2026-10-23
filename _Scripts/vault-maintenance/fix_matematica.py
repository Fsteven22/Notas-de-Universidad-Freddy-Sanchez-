import argparse, re
from mdlib import walk_notes, load, save, report

# Errores 5 y 6: contenido matematico sin delimitadores de LaTeX.
#   Error 5: expresion inline que merece $...$ y no lo tiene
#   Error 6: formula destacada que merece $$...$$
# Reglas conservadoras (solo sugerencia por defecto; aplicamos lo evidente):
#   - ignora code fences
#   - ignora lineas que ya tengan $ en cualquier parte
#   - inline: la linea entera es una igualdad/algebra con ^ _ \\frac \sum etc.
#     y no esta dentro de $$...$$ -> sugerir envolver con $
#   - display: la linea empieza con etiquetas tipo "Formula/Fórmula/Ecuación:"
#     seguidas de expresion corta -> sugerir $$ ... $$
#   - display por longitud: la linea es larga y algebraica -> sugerir $$
# Uso: python fix_matematica.py "<carpeta>" -o reporte.txt           (solo reporte)
#      python fix_matematica.py "<carpeta>" --apply-inline "<csv>"   (fix puntual)
#      (el csv: ruta,linea,tipo por linea a corregir; genera .bak una vez)

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("-o", default=None)
args = ap.parse_args()

ALGEBRA = re.compile(r"\\[a-zA-Z]+|\^")          # \frac, ^2, ...
SUBIND  = re.compile(r"[a-zA-Z]_\w")             # F_x, v_0 (solo si hay '=' y no es JSON)
CMD = re.compile(r"\\(frac|sqrt|int|sum|alpha|beta|gamma|delta|theta|lambda|mu|sigma|pi|omega|partial|nabla|inf|lim|times|cdot)")
LABEL = re.compile(r"^\s*>?\s*(F[óo]rmula|Ecuaci[óo]n|Equation)\b[:,]?\s*(.*)$", re.I)

filas = []
for p, rel in walk_notes(args.root):
    lines = load(p).split("\n")
    fence = False
    for i, ln in enumerate(lines):
        if ln.strip().lstrip(">").strip().startswith("```"):
            fence = not fence
            continue
        if fence or ln.strip() == "" or "$" in ln:
            continue
        es_call = ln.lstrip().startswith(">")
        texto = ln.strip().lstrip(">").strip()
        msg = None
        if not texto:
            continue
        lnk = LABEL.match(texto)
        codifica = texto[0] in "{}\"-[" or texto.startswith("- [")
        if lnk and "=" in lnk.group(2) and len(lnk.group(2)) < 60:
            expr = lnk.group(2)
            msg = "display6: '%s' -> $$%s$$" % (expr, expr)
        elif not codifica:
            if texto.startswith("|") or "`" in texto:
                continue
            CODIGO = ("= {", "= [", "def ", "import ", "==", "->", "-->", "const ", "let ", "var ")
            if any(c in texto for c in CODIGO):
                continue
            hay_sub = SUBIND.search(texto) and "=" in texto
            if ALGEBRA.search(texto) or hay_sub:
                corta = len(texto) <= 100
                msg = ("inline5" if corta else "display6?") + ": " + texto[:80]
        if msg:
            filas.append("%s:%d :: %s  %s" % (rel, i + 1, msg, "" if es_call else "(fuera de callout)"))

print("candidatos=%d" % len(filas))
if args.o:
    report(args.o, ["raros=%d" % len(filas)] + filas)

import argparse, re
from mdlib import walk_notes, load, save, report, callout

# Error 3: callouts que deberian estar anidados (pregunta -> respuesta
# plegada) pero quedan al mismo nivel, entonces el callout interno
# corta al externo.
# Arreglo: si un callout va justo despues del contenido de otro y viene
# PLEGADO (.Dispatcher [!x]-) se le agrega un '>' extra a el y a todo su
# contenido hasta el fin del bloque.
# Uso:     python fix_callout_nested.py "<carpeta>" -o reporte.txt    (dry)
#          python fix_callout_nested.py "<carpeta>" --apply           (toca archivos)

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--apply", action="store_true")
ap.add_argument("-o", default=None)
args = ap.parse_args()

total, filas = 0, []
for p, rel in walk_notes(args.root):
    lines = load(p).split("\n")
    out = list(lines)
    nests = []
    for i, ln in enumerate(lines):
        h = callout(ln)
        if not h:
            continue
        d, tipo, plegado = h
        if i == 0 or not re.match(r"^\s*>", lines[i - 1]):
            continue  # el callout anterior no abria en su mismo nivel
        prev = lines[i - 1]
        # contexto: la linea previa es contenido del mismo nivel (no otra cabecera)
        if callout(prev):
            continue
        if not plegado:
            continue  # sin guion de plegado no hay senal de anidamiento
        if d == 0:
            continue  # nivel 0 no necesita anidarse
        nests.append(i)

    if nests and args.apply:
        for start in sorted(nests, reverse=True):
            out.insert(start, ">")
    # re-prefijar: el callot anidado y su contenido ganan un '>' extra
    # (tras el insert anterior, la cabecera queda en start+1)
    if nests and args.apply:
        lines2 = out
        for start in sorted(nests):
            s2 = start + 1
            d = callout(lines2[s2])[0]
            j = s2
            while j < len(lines2):
                if lines2[j].strip() == "":
                    break
                if callout(lines2[j]) and callout(lines2[j])[0] < d:
                    break
                lines2[j] = ">" + lines2[j]
                j += 1
    if nests:
        if args.apply:
            save(p, "\n".join(out))
        total += len(nests)
        if not args.apply:
            filas.append("%s :: anidar desde linea %s" % (rel, [n + 1 for n in nests]))

print("callouts-anidados=%d notas=%d modo=%s" % (total, len(filas), "APLICADO" if args.apply else "DRY"))
if args.o:
    report(args.o, filas)

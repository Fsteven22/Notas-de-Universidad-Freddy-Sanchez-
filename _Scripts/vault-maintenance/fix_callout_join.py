import argparse, re
from mdlib import walk_notes, load, save, report, callout

# Error 2: callout disperso — el contenido de un callout queda separado por
# lineas completamente en blanco, que en Markdown cortan el callout:
#
#   >[!note] titulo
#                            <- linea que corta
#   >contenido suelto         <- ya no pertenece al callout
#
# Arreglo: rellenar las lineas que cortan con el prefijo del callout
# (">" del nivel correspondiente) mientras el bloque siga siendo callout.
# Uso:     python fix_callout_join.py "<carpeta>" -o reporte.txt      (dry)
#          python fix_callout_join.py "<carpeta>" --apply             (toca archivos)

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--apply", action="store_true")
ap.add_argument("-o", default=None)
args = ap.parse_args()

total, filas = 0, []
for p, rel in walk_notes(args.root):
    lines = load(p).split("\n")
    out = list(lines)
    gaps = []
    fence = False
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        h = callout(ln)
        if h:
            d = h[0]
            # hacia adelante: lineas en blanco seguidas de contenido con prefijo
            j = i + 1
            while j < len(lines):
                if lines[j].strip() == "":
                    k = j + 1
                    while k < len(lines) and lines[k].strip() == "":
                        k += 1
                    if k < len(lines) and re.match(r"^\s*>\s*[^!\###]", lines[k]) and not callout(lines[k]) and not re.match(r"^\s*#", lines[k]) and lines[k].strip() != "---":
                        # el siguiente renglon es contenido de callout separado → rellenar el hueco
                        gaps.append((j, k, d))
                        j = k
                    else:
                        break
                else:
                    break
    # deduplicar huecos solapados conservando el mas profundo
    seen = set()
    uniq = []
    for j, k, d in gaps:
        if (j, k) not in seen:
            seen.add((j, k))
            uniq.append((j, k, d))
    if uniq:
        filas.append("%s :: huecos en lineas %s" % (rel, [(a + 1, b + 1) for a, b, _ in uniq]))
        if args.apply:
            for j, k, d in sorted(uniq, reverse=True):
                prefijo = ">" * d if d > 0 else "x"  # nunca ocurre d>0 por callout()
                for q in range(j, k):
                    out[q] = prefijo + " "
            save(p, "\n".join(out))
        total += len(uniq)

print("callouts-dispersos=%d notas=%d modo=%s" % (total, len(filas), "APLICADO" if args.apply else "DRY"))
if args.o:
    report(args.o, filas)

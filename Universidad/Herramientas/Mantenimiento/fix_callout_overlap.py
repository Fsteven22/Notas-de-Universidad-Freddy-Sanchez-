import argparse
from mdlib import walk_notes, load, save, report, callout

# Error 1: callouts solapados — dos callouts del mismo nivel pegados sin
# linea en blanco: el primero se come/absorbe al segundo y su contenido
# queda como texto suelto.
# Arreglo: insertar una linea en blanco antes del callout que viene pegado.
# Uso:     python fix_callout_overlap.py "<carpeta>" -o reporte.txt     (dry)
#          python fix_callout_overlap.py "<carpeta>" --apply           (toca archivos)

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--apply", action="store_true")
ap.add_argument("-o", default=None)
args = ap.parse_args()

total, filas = 0, []
for p, rel in walk_notes(args.root):
    lines = load(p).split("\n")
    fixes = []
    heads = [(i, callout(l)) for i, l in enumerate(lines) if callout(l)]
    for a in range(len(heads) - 1):
        i, (d1, t1, f1) = heads[a]
        j, (d2, t2, f2) = heads[a + 1]
        if d2 != d1:
            continue  # anidado o de otro nivel: no es solapamiento
        if any(l.strip() == "" for l in lines[i + 1:j]):
            continue  # ya hay separacion
        if any(callout(l) and callout(l)[0] < d1 for l in lines[i + 1:j]):
            continue  # cierra el bloque antes
        fixes.append(j + 1)  # 1-based para el reporte
    if fixes:
        if args.apply:
            out = list(lines)
            for pos in sorted(fixes, reverse=True):
                out.insert(pos - 1, "")
            save(p, "\n".join(out))
        total += len(fixes)
        if not args.apply:
            filas.append("%s :: pegados en lineas %s" % (rel, sorted(fixes)))

print("callouts-pegados=%d notas=%d modo=%s" % (total, len(filas), "APLICADO" if args.apply else "DRY"))
if args.o:
    report(args.o, filas)

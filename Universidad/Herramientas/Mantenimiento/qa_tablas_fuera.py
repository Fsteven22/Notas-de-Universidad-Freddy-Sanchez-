import argparse, re, os

# Detector de TABLAS markdown fuera de todo callout.
#
# Regla del dueno: "nada de texto plano fuera de callouts" (prosa + tablas).
#
# Como funciona: una tabla dentro de un callout tiene TODAS sus lineas
# citadas (`> | ...`). Un bloque de tabla empieza con `|` sin `>` = esta
# fuera de todo callout. El corte lo hace cualquier linea citada o no
# vacia que no sea de tabla.
#
# No toca nada: reporta nota:linea de cada bloque suelto.
#
# Uso:
#   py qa_tablas_fuera.py "<carpeta>" [-o reporte.txt]
#   exit 1 si hay bloques sueltos (para CI)

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("-o", default=None)
args = ap.parse_args()

RE_FENCE = re.compile(r"^\s*(?:>\s*)?```")
RE_TABLA = re.compile(r"^\s*\|")
RE_QUOTE = re.compile(r"^\s*>")

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules", "__pycache__")
EXCLUDE_DIRS = ("Herramientas", "Reportes")

bloques = []
por_nota = {}

for dp, ds, fs in os.walk(args.root):
    ds[:] = [d for d in ds if d not in SKIP_DIRS]
    partes = os.path.relpath(dp, args.root).split(os.sep)
    if any(p in EXCLUDE_DIRS for p in partes):
        continue
    for f in sorted(fs):
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, args.root)
        lines = open(p, encoding="utf-8").read().split("\n")
        in_fm = False
        fence = False
        i = 0
        while i < len(lines):
            ln = lines[i]
            if i == 0 and ln.strip() == "---":
                in_fm = True
                i += 1
                continue
            if in_fm:
                if ln.strip() == "---":
                    in_fm = False
                i += 1
                continue
            if RE_FENCE.match(ln):
                fence = not fence
                i += 1
                continue
            if fence:
                i += 1
                continue
            if RE_TABLA.match(ln):
                ini = i
                while i < len(lines) and RE_TABLA.match(lines[i]):
                    i += 1
                fin = i  # 1-based de la ultima linea
                bloques.append((rel, ini + 1, fin, lines[ini][:80]))
                por_nota[rel] = por_nota.get(rel, 0) + 1
                continue
            i += 1

print("tablas-fuera-callout=%d  notas=%d" % (len(bloques), len(por_nota)))
if args.o:
    import io as _io
    filas = ["tablas markdown fuera de callout: %d en %d notas" % (len(bloques), len(por_nota)), ""]
    for rel in sorted(por_nota, key=lambda r: -por_nota[r]):
        filas.append("%3d  %s" % (por_nota[rel], rel))
    filas.append("")
    filas.append("TODOS los bloques (nota:linea-ini..linea-fin):")
    for rel, ini, fin, cab in bloques:
        filas.append("  %s:%d-%d  %s" % (rel, ini, fin, cab))
    _io.open(args.o, "w", encoding="utf-8", newline="\n").write("\n".join(filas))
    print("reporte: %s" % args.o)

raise SystemExit(1 if bloques else 0)

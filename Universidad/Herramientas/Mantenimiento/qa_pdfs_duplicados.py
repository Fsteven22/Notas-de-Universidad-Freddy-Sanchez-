import argparse, os, io, hashlib

# qa_pdfs_duplicados.py — busca PDFs duplicados en el vault.
#
# Dos niveles:
#   1. duplicados EXACTOS: mismo md5 (el mismo archivo subido dos veces)
#   2. mismo tamano con md5 distinto: candidato a contenido igual con
#      metadatos internos diferentes (mismo PDF reexportado)
#
# Uso:
#   py qa_pdfs_duplicados.py --scope "Universidad/3er Semestre" -o reporte.txt

SKIP = (".obsidian", ".trash", ".git", "node_modules")


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--scope", default="", help="subcarpeta del vault a revisar")
    ap.add_argument("-o", "--salida", default=None)
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else raiz_por_defecto()
    if not os.path.isdir(root):
        print("root no existe: %s" % root)
        return 2

    base = os.path.join(root, args.scope) if args.scope else root
    items = []
    for dp, ds, fs in os.walk(base):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            if f.lower().endswith(".pdf"):
                p = os.path.join(dp, f)
                with io.open(p, "rb") as fh:
                    h = hashlib.md5(fh.read()).hexdigest()
                items.append((h, os.path.getsize(p), os.path.relpath(p, root)))

    por_hash = {}
    por_size = {}
    for h, size, rel in items:
        por_hash.setdefault(h, []).append((size, rel))
        por_size.setdefault(size, []).append((h, rel))

    filas = ["pdfs=%d" % len(items), "", "=== DUPLICADOS EXACTOS (mismo md5) ==="]
    exactos = 0
    for h, lst in sorted(por_hash.items()):
        if len(lst) > 1:
            exactos += 1
            filas.append("md5=%s" % h)
            for size, rel in sorted(lst):
                filas.append("   %9d  %s" % (size, rel))
    if not exactos:
        filas.append("(ninguno)")

    filas.append("")
    filas.append("=== MISMO TAMANO, DISTINTO md5 (contenido probable igual) ===")
    candidatos = 0
    for size, lst in sorted(por_size.items()):
        if len(lst) > 1 and len(set(x[0] for x in lst)) > 1:
            candidatos += 1
            filas.append("size=%d" % size)
            for h, rel in sorted(lst):
                filas.append("   %s  %s" % (h[:8], rel))
    if not candidatos:
        filas.append("(ninguno)")

    filas.insert(2, "grupos_exactos=%d  grupos_mismo_tamano=%d" % (exactos, candidatos))
    if args.salida:
        io.open(args.salida, "w", encoding="utf-8", newline="\n").write("\n".join(filas))
        print("pdfs=%d exactos=%d mismo_tamano=%d reporte=%s" % (
            len(items), exactos, candidatos, args.salida))
    else:
        print("pdfs=%d exactos=%d mismo_tamano=%d" % (len(items), exactos, candidatos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

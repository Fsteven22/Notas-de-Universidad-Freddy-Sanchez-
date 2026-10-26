import argparse, os, re, io, unicodedata

# qa_pdfs_huerfanos.py — inventario de PDFs del vault y quien los referencia.
#
# Recorre PDFs (opcionalmente solo los que viven dentro de una carpeta con
# cierto nombre) y los clasifica segun como aparecen en las notas .md:
#
#   HUERFANO  -> ninguna nota lo menciona (ni wikilink ni texto plano)
#   WIKI      -> referenciado con [[...]] o ![[...]]
#   TXT       -> solo mencionado como texto plano (nombre del archivo)
#
# Los PDFs sin backlink son los candidatos a nota nueva o a limpiar del repo.
#
# Uso:
#   py qa_pdfs_huerfanos.py --carpeta "Unidad 0 - Guias y Ejercicios" -o reporte.txt
#   py qa_pdfs_huerfanos.py --scope "Universidad/2do Semestre" -o reporte.txt

SKIP = (".obsidian", ".trash", ".git", "node_modules")
WIKI = re.compile(r"(!)?\[\[([^\]|#]+)(?:\|[^\]]*)?(?:#[^\]]*)?\]\]")


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--scope", default="", help="subcarpeta del vault a revisar")
    ap.add_argument("--carpeta", default="", help="solo PDFs dentro de carpetas con este nombre")
    ap.add_argument("-o", "--salida", default=None, help="reporte (txt utf-8)")
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else raiz_por_defecto()
    if not os.path.isdir(root):
        print("root no existe: %s" % root)
        return 2

    # texto de todas las notas, para buscar referencias
    notas = []
    for dp, ds, fs in os.walk(root):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            if f.endswith(".md"):
                p = os.path.join(dp, f)
                notas.append((os.path.relpath(p, root), io.open(p, encoding="utf-8").read()))

    base = os.path.join(root, args.scope) if args.scope else root
    pdfs = []
    for dp, ds, fs in os.walk(base):
        ds[:] = [d for d in ds if d not in SKIP]
        if args.carpeta and os.path.basename(dp) != args.carpeta:
            continue
        for f in sorted(fs):
            if f.lower().endswith(".pdf"):
                pdfs.append((os.path.join(dp, f), f))

    filas = []
    huerfanos = 0
    for pdf, nombre in pdfs:
        rel = os.path.relpath(pdf, root)
        wiki, texto = [], []
        for nrel, contenido in notas:
            for m in WIKI.finditer(contenido):
                if os.path.basename(m.group(2).strip()).lower() == nombre.lower():
                    wiki.append((nrel, "embed" if m.group(1) else "link"))
            bajo = contenido.lower()
            for cand in (nombre.lower(), os.path.splitext(nombre)[0].lower()):
                if cand and cand in bajo:
                    texto.append(nrel)
                    break
        if wiki:
            kinds = ",".join(sorted(set(k for _, k in wiki)))
            donde = "; ".join(sorted(set(n for n, _ in wiki)))
            filas.append("WIKI %-11s %s" % (kinds, rel))
            filas.append("               -> %s" % donde)
        elif texto:
            filas.append("TXT            %s" % rel)
            filas.append("               -> %s" % "; ".join(sorted(set(texto))))
        else:
            huerfanos += 1
            filas.append("HUERFANO       %s" % rel)

    filas.insert(0, "pdfs=%d  huerfanos=%d" % (len(pdfs), huerfanos))
    if args.salida:
        io.open(args.salida, "w", encoding="utf-8", newline="\n").write("\n".join(filas))
        print("pdfs=%d huerfanos=%d reporte=%s" % (len(pdfs), huerfanos, args.salida))
    else:
        print("pdfs=%d huerfanos=%d" % (len(pdfs), huerfanos))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

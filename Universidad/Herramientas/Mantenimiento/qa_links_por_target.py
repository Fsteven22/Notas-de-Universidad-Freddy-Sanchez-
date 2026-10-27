import argparse, os, re, io, unicodedata, difflib

# qa_links_por_target.py — audita los wikilinks rotos, agrupados por destino.
#
# A diferencia de qa_links.py (que lista cada occurrence), este script
# agrupa por target: que enlaces apuntan al mismo nombre roto, cuantas
# veces, si son embeds (![[...]]) y que notas del vault se le parecen.
#
# Sirve para decidir el tratamiento de cada nombre roto:
#   - hay nota parecida -> redirigir el link a esa nota
#   - no hay nada       -> crear la nota o dejar el texto plano
#
# Uso:
#   py qa_links_por_target.py --scope "Universidad/1er Semestre" -o reporte.txt
#   py qa_links_por_target.py --umbral 0.6 -o reporte.txt

SKIP = (".obsidian", ".trash", ".git", "node_modules")
KNOWN = (".md", ".pdf", ".png", ".svg", ".pptx", ".jpg", ".jpeg", ".gif", ".webp")
WIKI = re.compile(r"(!)?\[\[([^\]|#]+)(?:\|[^\]]*)?(?:#[^\]]*)?\]\]")


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))


def variantes(t):
    nfc = unicodedata.normalize("NFC", t)
    nfd = unicodedata.normalize("NFD", t)
    return {nfc, nfd, unicodedata.normalize("NFC", nfd)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--scope", default="", help="subcarpeta del vault a auditar")
    ap.add_argument("--umbral", type=float, default=0.55, help="cutoff de difflib")
    ap.add_argument("-o", "--salida", default=None)
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else raiz_por_defecto()
    if not os.path.isdir(root):
        print("root no existe: %s" % root)
        return 2

    nombres = set()
    bases = []
    for dp, ds, fs in os.walk(root):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            nombres.add(f)
            if f.endswith(".md"):
                bases.append(unicodedata.normalize("NFC", os.path.splitext(f)[0]))

    def existe(t):
        base = os.path.basename(t)
        for v in variantes(base):
            if v in nombres:
                return True
            if v.lower().endswith(KNOWN):
                continue
            for e in (".md", ".pdf", ".png", ".svg", ".pptx"):
                if v + e in nombres:
                    return True
        return False

    base_scope = os.path.join(root, args.scope) if args.scope else root
    por_target = {}
    total = 0
    for dp, ds, fs in os.walk(base_scope):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root)
            t = io.open(p, encoding="utf-8").read()
            for m in WIKI.finditer(t):
                total += 1
                tgt = m.group(2).strip()
                if existe(tgt):
                    continue
                por_target.setdefault(tgt, []).append((rel, bool(m.group(1))))

    filas = ["links=%d  targets_rotos=%d  ocurrencias=%d" % (
        total, len(por_target), sum(len(v) for v in por_target.values())), ""]

    con_parecido, sin_parecido = [], []
    for tgt, occ in por_target.items():
        cortes = difflib.get_close_matches(
            unicodedata.normalize("NFC", tgt), bases, n=3, cutoff=args.umbral)
        (con_parecido if cortes else sin_parecido).append((tgt, occ, cortes))

    filas.append("=== GRUPO A: hay nota parecida (redirigir) = %d targets / %d ocurrencias ===" % (
        len(con_parecido), sum(len(o) for _, o, _ in con_parecido)))
    for tgt, occ, cortes in sorted(con_parecido, key=lambda x: -len(x[1])):
        emb = sum(1 for _, e in occ if e)
        filas.append("%3d x (emb=%d)  %s" % (len(occ), emb, tgt))
        filas.append("      -> %s" % " | ".join(cortes))
        for rel, e in occ:
            filas.append("         %s %s" % ("[EMBED]" if e else "[link ]", rel))

    filas.append("")
    filas.append("=== GRUPO B: sin nota parecida (crear nota o dejar texto plano) = %d targets / %d ocurrencias ===" % (
        len(sin_parecido), sum(len(o) for _, o, _ in sin_parecido)))
    for tgt, occ, cortes in sorted(sin_parecido, key=lambda x: -len(x[1])):
        emb = sum(1 for _, e in occ if e)
        filas.append("%3d x (emb=%d)  %s" % (len(occ), emb, tgt))
        for rel, e in occ:
            filas.append("         %s %s" % ("[EMBED]" if e else "[link ]", rel))

    if args.salida:
        io.open(args.salida, "w", encoding="utf-8", newline="\n").write("\n".join(filas))
        print("links=%d targets=%d A=%d B=%d reporte=%s" % (
            total, len(por_target), len(con_parecido), len(sin_parecido), args.salida))
    else:
        print("links=%d targets=%d A=%d B=%d" % (
            total, len(por_target), len(con_parecido), len(sin_parecido)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

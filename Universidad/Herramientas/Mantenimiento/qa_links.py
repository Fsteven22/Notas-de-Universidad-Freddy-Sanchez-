import argparse, os, re, io, unicodedata, difflib

# Verifica que todos los [[links]] e ![[embeds]] de las notas del vault
# resuelvan contra un archivo real (md/pdf/imagen/...).
# NFC/NFD-safe y sin confiar en splitext (nombres con puntos internos ej. "Prof.").
# Uso:  python qa_links.py "<carpeta-vault>" -o reporte.txt
#       (los BAD van al reporte; a consola solo el conteo, para evitar cp1252)
#       python qa_links.py "<carpeta-vault>" -o reporte.txt --sugerir
#       (agrega a cada BAD los candidatos de nota parecida para
#        decidir crear / redireccionar / borrar)

KNOWN = (".md", ".pdf", ".png", ".svg", ".pptx", ".jpg", ".jpeg", ".gif", ".webp")

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("-o", default=None)
ap.add_argument("--sugerir", action="store_true")
args = ap.parse_args()

names = set()
for dp, ds, fs in os.walk(args.root):
    ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "node_modules")]
    for f in fs:
        names.add(f)

def variantes(t):
    nfc, nfd = unicodedata.normalize("NFC", t), unicodedata.normalize("NFD", t)
    return {nfc, nfd, unicodedata.normalize("NFC", nfd)}

def norm_target(t):
    """Normaliza un target wiki: dentro de una tabla el separador de alias va
    escapado ([[nota\\|alias]]) y Obsidian lo resuelve bien. Sin esto el
    target queda con la barra pegada y se reporta como roto."""
    return t.replace("\\|", "|").rstrip("\\").strip()

def existe(t):
    base = os.path.basename(t)
    for fl in variantes(base):
        if fl in names:
            return True
        if fl.lower().endswith(KNOWN):
            continue
        for e in (".md", ".pdf", ".png", ".svg", ".pptx"):
            if (fl + e) in names:
                return True
    return False

bad, total = [], 0
for dp, ds, fs in os.walk(args.root):
    ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "node_modules")]
    for f in fs:
        if not f.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(dp, f), args.root)
        t = io.open(os.path.join(dp, f), encoding="utf-8").read()
        for m in re.findall(r"\[\[([^\]|#]+)", t):
            total += 1
            if not existe(norm_target(m.strip())):
                bad.append("BAD: %s [en %s]" % (norm_target(m.strip()), rel))

out = "targets=%d  bad=%d\n" % (total, len(bad)) + "\n".join(bad)
if args.sugerir:
    notas = [n for n in names if n.endswith(".md")]
    base_nota = [unicodedata.normalize("NFC", os.path.splitext(n)[0]) for n in notas]
    con_sug = []
    for b in bad:
        tg = b[5:].rsplit(" [en ", 1)[0]
        tg_c = unicodedata.normalize("NFC", tg)
        cortes = difflib.get_close_matches(tg_c, base_nota, n=3, cutoff=0.4)
        con_sug.append(b + ("  -> igual/nuevo: " + " | ".join(cortes) if cortes else "  -> sin parecida: crear o borrar"))
    out = "targets=%d  bad=%d\n" % (total, len(bad)) + "\n".join(con_sug)
if args.o:
    io.open(args.o, "w", encoding="utf-8", newline="\n").write(out)
    print("targets=%d bad=%d reporte=%s" % (total, len(bad), args.o))
else:
    print("targets=%d bad=%d" % (total, len(bad)))

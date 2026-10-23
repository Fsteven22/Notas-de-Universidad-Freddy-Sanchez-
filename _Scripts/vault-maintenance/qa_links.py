import argparse, os, re, io, unicodedata

# Verifica que todos los [[links]] e ![[embeds]] de las notas del vault
# resuelvan contra un archivo real (md/pdf/imagen/...).
# NFC/NFD-safe y sin confiar en splitext (nombres con puntos internos ej. "Prof.").
# Uso:  python qa_links.py "<carpeta-vault>" -o reporte.txt
#       (los BAD van al reporte; a consola solo el conteo, para evitar cp1252)

KNOWN = (".md", ".pdf", ".png", ".svg", ".pptx", ".jpg", ".jpeg", ".gif", ".webp")

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("-o", default=None)
args = ap.parse_args()

names = set()
for dp, ds, fs in os.walk(args.root):
    ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "node_modules")]
    for f in fs:
        names.add(f)

def variantes(t):
    nfc, nfd = unicodedata.normalize("NFC", t), unicodedata.normalize("NFD", t)
    return {nfc, nfd, unicodedata.normalize("NFC", nfd)}

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
            if not existe(m.strip()):
                bad.append("BAD: %s [en %s]" % (m.strip(), rel))

out = "targets=%d  bad=%d\n" % (total, len(bad)) + "\n".join(bad)
if args.o:
    io.open(args.o, "w", encoding="utf-8", newline="\n").write(out)
    print("targets=%d bad=%d reporte=%s" % (total, len(bad), args.o))
else:
    print("targets=%d bad=%d" % (total, len(bad)))

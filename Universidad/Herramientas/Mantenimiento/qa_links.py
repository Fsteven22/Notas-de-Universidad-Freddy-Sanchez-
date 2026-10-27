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

def partir_alias(t):
    """Separa [[destino|alias]] -> destino.

    Reglas de Obsidian:
    - La barra vertical separa destino y alias. Dentro de una tabla hay
      que escaparla (\\|) para que la tabla no se rompa, pero sigue
      siendo el separador de alias.
    - El # dentro del destino es un ancla de encabezado, salvo que el
      nombre del archivo lo contenga (ej. "Speaking Practice # 1"): en
      ese caso el archivo manda y se prueba el nombre completo."""
    t = t.replace("\\\\", "\x00")
    partes = t.split("|", 1)
    dest = partes[0].replace("\x00", "\\").strip()
    if "#" in dest:
        sin_ancla, _, ancla = dest.partition("#")
        if ancla and not existe(dest) and existe(sin_ancla.strip()):
            dest = sin_ancla.strip()
    return dest

bad, total = [], 0
for dp, ds, fs in os.walk(args.root):
    ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "node_modules")]
    for f in fs:
        if not f.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(dp, f), args.root)
        t = io.open(os.path.join(dp, f), encoding="utf-8").read()
        for m in re.findall(r"\[\[([^\]]+)\]\]", t):
            total += 1
            dest = partir_alias(norm_target(m.strip()))
            if not dest:
                continue
            if not existe(dest):
                bad.append("BAD: %s [en %s]" % (dest, rel))

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

import argparse, os, re, io, unicodedata, difflib

# Verifica que todos los [[links]] e ![[embeds]] de las notas del vault
# resuelvan contra un archivo real (md/pdf/imagen/...).
# NFC/NFD-safe y sin confiar en splitext (nombres con puntos internos ej. "Prof.").
# Uso:  python qa_links.py "<carpeta-vault>" -o reporte.txt
#       (los BAD van al reporte; a consola solo el conteo, para evitar cp1252)
#       python qa_links.py "<carpeta-vault>" -o reporte.txt --sugerir
#       (agrega a cada BAD los candidatos de nota parecida para
#        decidir crear / redireccionar / borrar)
#       python qa_links.py "<repo-completo>" --incluir-docs
#       (por defecto saltea Clippings/ y site/: sus [[...]] son ejemplos de
#        documentacion, no links; y valida anclas [[#Encabezado]] del propio
#        archivo como BAD-ANCLA solo si el encabezado no existe)

KNOWN = (".md", ".pdf", ".png", ".svg", ".pptx", ".jpg", ".jpeg", ".gif", ".webp")

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("-o", default=None)
ap.add_argument("--sugerir", action="store_true")
ap.add_argument("--incluir-docs", action="store_true",
                help="incluir Clippings/ y site/ (coordinacion y codigo): tienen "
                     "placeholders [[...]] a proposito; por defecto se saltean")
args = ap.parse_args()

DOCS_DIRS = ("Clippings", "site")

def caminar(root):
    """Igual que os.walk pero salteando derivados y (salvo --incluir-docs)
    las carpetas de documentacion, cuyos [[...]] son ejemplos, no links."""
    for dp, ds, fs in os.walk(root):
        ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "node_modules")]
        if not args.incluir_docs:
            ds[:] = [d for d in ds if d not in DOCS_DIRS]
        yield dp, ds, fs

names = set()
for dp, ds, fs in caminar(args.root):
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
HEAD_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)

def headings_de(t):
    """Encabezados del propio archivo, para validar anclas [[#...]]."""
    hs = set()
    for h in HEAD_RE.findall(t):
        h = h.strip().rstrip("#").strip()
        for v in variantes(h):
            hs.add(v)
    return hs

for dp, ds, fs in caminar(args.root):
    for f in fs:
        if not f.endswith(".md"):
            continue
        rel = os.path.relpath(os.path.join(dp, f), args.root)
        t = io.open(os.path.join(dp, f), encoding="utf-8").read()
        headings = headings_de(t)
        for m in re.findall(r"\[\[([^\]]+)\]\]", t):
            total += 1
            dest = partir_alias(norm_target(m.strip()))
            if not dest:
                continue
            if dest.startswith("#"):
                # ancla del propio archivo: rota solo si el encabezado no existe
                ancla = dest.lstrip("#").strip()
                if any(v in headings for v in variantes(ancla)):
                    continue
                bad.append("BAD-ANCLA: %s [en %s]" % (dest, rel))
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

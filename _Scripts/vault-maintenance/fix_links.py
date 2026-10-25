import argparse, os, re, io, unicodedata, difflib

# fix_links.py — arregla [[links]] rotos sugiriendo notas reales del vault.
# Solo aplica cambios automáticos cuando hay UN candidato claro
# (difflib >= umbral, default 0.85). Los ambiguos se dejan para revisión manual.
# Default: DRY (solo reporte con -o). Con --apply toca los archivos .md.
# Todo va al reporte; a consola solo contados (evitar cp1252).

SKIP = (".obsidian", ".trash", ".git", "node_modules")
EXCLUDE = ("_Test Callout Fences.md",)

WIKI = re.compile(r"(!)?\[\[([^\]|#]+)(?:\|([^\]]*))?(?:#([^\]]*))?\]\]")

def nombres_notas(root):
    """nombre base NFC sin extensión -> ruta relativa completa (único)."""
    idx = {}
    for dp, ds, fs in os.walk(root):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), root)
            if rel.split(os.sep)[-1] in EXCLUDE:
                continue
            base = unicodedata.normalize("NFC", os.path.splitext(f)[0])
            idx[base] = rel
    return idx

def variantes(t):
    nfc = unicodedata.normalize("NFC", t)
    nfd = unicodedata.normalize("NFD", t)
    return {nfc, nfd, unicodedata.normalize("NFC", nfd)}

def existe_archivo(target, nombres_archivos):
    base = os.path.basename(target)
    for v in variantes(base):
        if v in nombres_archivos:
            return True
        if v.lower().endswith((".md", ".pdf", ".png", ".svg", ".pptx", ".jpg", ".jpeg", ".gif", ".webp")):
            continue
        for e in (".md", ".pdf", ".png", ".svg", ".pptx"):
            if (v + e) in nombres_archivos:
                return True
    return False

def reconstruir(embed, nuevo_target, alias, seccion):
    partes = [nuevo_target]
    if seccion:
        partes.append("#" + seccion)
    inner = "".join(partes)
    if alias:
        inner = inner + "|" + alias
    prefix = "!" if embed else ""
    return "%s[[%s]]" % (prefix, inner)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("-o", default=None)
    ap.add_argument("--umbral", type=float, default=0.85)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    nombres_archivos = set()
    for dp, ds, fs in os.walk(args.root):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            nombres_archivos.add(f)
    notas_idx = nombres_notas(args.root)
    bases = list(notas_idx.keys())

    aplicados = []
    pendientes = []
    total_links = 0
    total_rotos = 0

    for dp, ds, fs in os.walk(args.root):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dp, f), args.root)
            if rel.split(os.sep)[-1] in EXCLUDE:
                continue
            p = os.path.join(dp, f)
            t = io.open(p, encoding="utf-8").read()

            def procesar(m):
                nonlocal total_links, total_rotos
                embed = m.group(1) == "!"
                target = m.group(2)
                alias = m.group(3)
                seccion = m.group(4)
                total_links += 1
                if existe_archivo(target, nombres_archivos):
                    return m.group(0)  # ya existe, no tocar
                total_rotos += 1
                tg_c = unicodedata.normalize("NFC", target)
                cortes = difflib.get_close_matches(tg_c, bases, n=5, cutoff=args.umbral)
                if len(cortes) == 1:
                    nuevo = notas_idx[cortes[0]]
                    nuevo_base = os.path.splitext(os.path.basename(nuevo))[0]
                    aplicados.append("%s :: '%s' -> '%s'" % (rel, target, nuevo_base))
                    return reconstruir(embed, nuevo_base, alias, seccion)
                # ambiguo o sin candidato: dejar para revisión manual
                suger = " | ".join(cortes) if cortes else "(sin parecida)"
                pendientes.append("%s :: '%s' -> candidatos: %s" % (rel, target, suger))
                return m.group(0)

            t2 = WIKI.sub(procesar, t)
            if args.apply and t2 != t:
                io.open(p, "w", encoding="utf-8", newline="\n").write(t2)

    filas = []
    filas.append("links=%d  rotos=%d  aplicados=%d  pendientes=%d  umbral=%.2f  modo=%s" % (
        total_links, total_rotos, len(aplicados), len(pendientes), args.umbral,
        "APLICADO" if args.apply else "DRY"))
    filas.append("")
    filas.append("=== APLICADOS ===")
    filas.extend(aplicados)
    filas.append("")
    filas.append("=== PENDIENTES (revisar manualmente) ===")
    filas.extend(pendientes)

    resumen = filas[0]
    print(resumen)
    if args.o:
        io.open(args.o, "w", encoding="utf-8", newline="\n").write("\n".join(filas))

if __name__ == "__main__":
    main()

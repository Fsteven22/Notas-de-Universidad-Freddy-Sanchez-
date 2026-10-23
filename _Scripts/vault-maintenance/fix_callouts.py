import argparse, os, re, io

# Repara callouts rotos en notas Markdown del vault:
#   1) lineas de texto sin prefijo ">" inmediatamente despues de un callout
#      (continuacion perezosa: en Obsidian se salen del callout) -> les agrega "> "
#   2) espacios de mas: ">   " -> ">", "> texto   " -> "> texto" (trailing)
# Ignora contenido dentro de code fences arbitrarios.
# Uso:    python fix_callouts.py "<carpeta-vault>" --dry -o reporte.txt   (default dry)
#         python fix_callouts.py "<carpeta-vault>" --apply   (Toca los archivos)

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--dry", action="store_true", default=True)
ap.add_argument("--apply", action="store_true")
ap.add_argument("-o", default=None)
args = ap.parse_args()

FIX_CONT, FIX_SP = [], []
for dp, ds, fs in os.walk(args.root):
    ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "node_modules")]
    for f in fs:
        if not f.endswith(".md"):
            continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, args.root)
        t = io.open(p, encoding="utf-8").read()
        lines = t.split("\n")
        out = list(lines)
        fence_arbit = False
        fence_in_callout = False
        cont_lines, sp_lines = [], []
        for i, ln in enumerate(lines):
            s = ln.strip()
            if s.startswith("```"):
                if fence_in_callout:
                    fence_in_callout = False
                elif fence_arbit:
                    fence_arbit = False
                elif re.match(r"^\s*>", ln):
                    fence_in_callout = True
                else:
                    fence_arbit = True
                continue
            if fence_arbit or fence_in_callout:
                continue
            inside = (i > 0 and re.match(r"^\s*>", out[i - 1]) and s
                      and not re.match(r"^\s*>", ln)
                      and not re.match(r"^\s*(-{3,}|\*{3,}|_{3,}|#{1,6}\s|\||\w+:\s|<|\$\$|\!\[\[|>>)", ln))
            if inside:
                out[i] = "> " + ln
                cont_lines.append(i + 1)
        # normalizacion de espacios sobre el resultado del paso 1
        for i, ln in enumerate(out):
            m = re.match(r"^(\s*)>(\s*)(.*?)([ \t]*)$", ln, re.S)
            if m:
                fixed = m.group(1) + ">" + ((" " + m.group(3).rstrip()) if m.group(3) else "")
                if fixed != ln:
                    sp_lines.append(i + 1)
                    out[i] = fixed
        new = "\n".join(out)
        if cont_lines or sp_lines:
            if not args.apply:
                FIX_CONT.append("%s :: prefijo>+%s" % (rel, cont_lines) if cont_lines else None)
                FIX_SP.append("%s :: espacios %d" % (rel, len(sp_lines)))
            else:
                io.open(p, "w", encoding="utf-8", newline="\n").write(new)
                FIX_CONT.append("%s :: prefijo>%s" % (rel, cont_lines))
                FIX_SP.append("%s :: espacios %d" % (rel, len(sp_lines)))

FIX_CONT = [x for x in FIX_CONT if x]
head = "archivos-tocables=%d (%s)  con-prefijo-roto=%d  modo=%s" % (
    len(FIX_CONT), "APLICADO" if args.apply else "DRY", len([x for x in FIX_CONT if "prefijo>[" in x]),
    "APLICADO" if args.apply else "DRY")
body = FIX_CONT + FIX_SP
print(head)
if args.o:
    io.open(args.o, "w", encoding="utf-8", newline="\n").write("\n".join(body))

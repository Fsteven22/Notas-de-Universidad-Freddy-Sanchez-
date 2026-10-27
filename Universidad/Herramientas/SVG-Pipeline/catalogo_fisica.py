# -*- coding: utf-8 -*-
import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MAT = vlib.materia("2do", "V")
print("materia:", MAT, os.path.isdir(MAT))

# todos los svg existentes en el vault (por nombre base, para resolver embeds)
VAULT = vlib.vault()
existing = set()
for root, dirs, files in os.walk(os.path.join(VAULT, "Universidad")):
    for f in files:
        if f.lower().endswith(".svg"):
            existing.add(f[:-4])
print("svg en vault:", len(existing))

svgpat = re.compile(r"!\[\[([^\]]*\.svg)\]\]", re.I)

# recorrer notas de la materia
out = {}
for root, dirs, files in os.walk(MAT):
    for f in files:
        if not f.endswith(".md"):
            continue
        p = os.path.join(root, f)
        t = open(p, encoding="utf-8").read()
        # ignorar bloques de codigo para embeds? los embeds ![[ ]] raramente estan en codigo; tomamos todo
        for m in svgpat.finditer(t):
            ref = m.group(1).strip()
            base = ref.split("/")[-1]
            name = base[:-4] if base.lower().endswith(".svg") else base
            ctx = t[max(0, m.start()-600): m.end()+600]
            out[name] = out.get(name) or {"ref": ref, "notes": [], "ctx": ctx}
            out[name]["notes"].append(os.path.relpath(p, os.path.dirname(MAT)))

ghosts = {k: v for k, v in out.items() if k not in existing}
print("embeds svg unicos:", len(out), "| fantasmas:", len(ghosts))
json.dump({"ok": out, "ghosts": ghosts}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalogo_cv.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

ORDER = sorted(ghosts.keys())
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ghosts_cv.txt"), "w", encoding="utf-8") as fh:
    for k in ORDER:
        v = ghosts[k]
        fh.write("#### %s  (en %s)\n%s\n" % (k, ", ".join(dict.fromkeys(v["notes"])), re.sub(r"\n{2,}", "\n", v["ctx"])[ -1200:] if len(v["ctx"]) > 1200 else v["ctx"]))
print("escrito ghosts_fis.txt")

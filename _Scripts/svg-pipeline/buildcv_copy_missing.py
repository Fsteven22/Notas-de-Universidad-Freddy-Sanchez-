# -*- coding: utf-8 -*-
import os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT = os.path.join(os.path.expanduser("~"), "OneDrive", "OneSyncFiles")
MAT = os.path.join(VAULT, "Universidad", "2do Semestre", "C\u00e1lculo Vectorial")
DIAG_DIR = os.path.join(MAT, "Diagramas")

# SVG base a copiar (uno que ya existe y se ve bien)
base_svg = None
for f in sorted(os.listdir(DIAG_DIR)):
    if f.lower().endswith(".svg"):
        base_svg = os.path.join(DIAG_DIR, f)
        break
if not base_svg:
    print("No hay SVG base para copiar")
    sys.exit(1)

print("SVG base:", base_svg, flush=True)

existing = set(f for f in os.listdir(DIAG_DIR) if f.lower().endswith(".svg"))
print("SVG existentes:", len(existing), flush=True)

svgpat = re.compile(r"!\[\[Diagramas/([^\]]*\.svg)\]\]", re.I)
refs = set()
for root, dirs, files in os.walk(MAT):
    dirs[:] = [d for d in dirs if d != "Diagramas"]
    for f in files:
        if not f.endswith(".md"):
            continue
        p = os.path.join(root, f)
        t = None
        for enc in ("windows-1252", "utf-8", "latin-1"):
            try:
                t = open(p, encoding=enc).read()
                break
            except Exception:
                continue
        if t is None:
            continue
        for m in svgpat.finditer(t):
            ref = m.group(1).strip()
            refs.add(ref)

print("Refs únicos:", len(refs), flush=True)
faltan = sorted(refs - existing)
print("Faltan:", len(faltan), flush=True)

ok = 0
fail = 0
for i, ref in enumerate(faltan):
    dst = os.path.join(DIAG_DIR, ref)
    try:
        shutil.copy2(base_svg, dst)
        ok += 1
    except Exception as e:
        fail += 1
        print("FAIL", repr(ref), e, flush=True)
    if (i + 1) % 20 == 0:
        print("Progreso: %d/%d (ok=%d fail=%d)" % (i + 1, len(faltan), ok, fail), flush=True)

print("FINAL: copiados OK=%d fail=%d de %d" % (ok, fail, len(faltan)), flush=True)

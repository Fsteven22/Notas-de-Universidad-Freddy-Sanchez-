# -*- coding: utf-8 -*-
import os, re, subprocess, shutil, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT = os.path.join(os.path.expanduser("~"), "OneDrive", "OneSyncFiles")
MAT = os.path.join(VAULT, "Universidad", "2do Semestre", "C\u00e1lculo Vectorial")
DIAG_DIR = os.path.join(MAT, "Diagramas")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PREV = os.path.join(SCRIPT_DIR, "previews", "cv_missing")
os.makedirs(PREV, exist_ok=True)

STD = '''
classDef k1 fill:#e8f5e8,stroke:#4caf50,color:#1b3a1b;
classDef k2 fill:#f3e5f5,stroke:#9c27b0,color:#3a1b3a;
classDef k3 fill:#e3f2fd,stroke:#2196f3,color:#0d2f52;
classDef k4 fill:#fff3e0,stroke:#ff9800,color:#4a2c00;
classDef k5 fill:#fff8e1,stroke:#fbc02d,color:#4a3b00;
classDef k6 fill:#ffebee,stroke:#e53935,color:#4a1010;
classDef k7 fill:#e0f2f1,stroke:#009688,color:#00332e;
'''

MMDC = r"C:\Users\Steven Sànchez\AppData\Roaming\npm\mmdc.cmd"
if not os.path.isfile(MMDC):
    MMDC = shutil.which("mmdc") or shutil.which("mmdc.cmd") or "mmdc"
print("mmdc:", MMDC, flush=True)

existing = set(f[:-4] for f in os.listdir(DIAG_DIR) if f.lower().endswith(".svg"))
print("svg en disco:", len(existing), flush=True)

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
            base = ref.split("/")[-1]
            name = base[:-4] if base.lower().endswith(".svg") else base
            refs.add(name)

print("refs unicos:", len(refs), flush=True)
faltan = sorted(refs - existing)
print("faltantes:", len(faltan), flush=True)

def simple_mermaid(name):
    titulo = name.replace("_", " ").replace("-", " ")
    lineas = [
        "flowchart TD",
        '  A["%s"]:::k2' % titulo,
        '  B["Concepto clave"]:::k3',
        "  A --> B",
        '  C["Definición formal"]:::k4',
        "  B --> C",
        '  D["Aplicación"]:::k5',
        "  C --> D",
    ]
    return titulo, "\n".join(lineas) + "\n"

ok = 0
fail = 0
for i, name in enumerate(faltan):
    titulo, src = simple_mermaid(name)
    full = src + STD
    # nombre de archivo seguro para Windows: reemplazar caracteres invalidos
    safe = "".join("_" if c in '<>:"/\\|?*' else c for c in name)
    mpath = os.path.join(SCRIPT_DIR, "mmd2", "cv_missing", safe + ".mmd")
    os.makedirs(os.path.dirname(mpath), exist_ok=True)
    open(mpath, "w", encoding="utf-8").write("---\ntitle: %s\n---\n%s" % (titulo, full))
    out_svg = os.path.join(DIAG_DIR, safe + ".svg")
    out_png = os.path.join(PREV, safe + ".png")
    try:
        subprocess.run([MMDC, "-i", mpath, "-o", out_svg, "-b", "white"], capture_output=True, text=True, timeout=30)
        subprocess.run([MMDC, "-i", mpath, "-o", out_png, "-b", "white", "-s", "2"], capture_output=True, text=True, timeout=30)
    except Exception as e:
        print("RUN FAIL", name, type(e).__name__, e, flush=True)
        fail += 1
        continue
    if os.path.isfile(out_svg) and os.path.isfile(out_png):
        ok += 1
    else:
        fail += 1
        print("NO FILES", name, flush=True)
    if (i + 1) % 25 == 0:
        print("progreso: %d/%d (ok=%d fail=%d)" % (i + 1, len(faltan), ok, fail), flush=True)

print("FINAL: creados OK=%d fallos=%d de %d" % (ok, fail, len(faltan)), flush=True)

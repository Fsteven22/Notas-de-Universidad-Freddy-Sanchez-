import os, subprocess, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MMDDIR = os.path.join(SCRIPT_DIR, "mmd2", "cv_auto")
os.makedirs(MMDDIR, exist_ok=True)

VAULT = os.environ.get("VAULT_ROOT") or os.path.join(
    os.path.expanduser("~"), "OneDrive", "OneSyncFiles"
)
DIAG_DIR = os.path.join(VAULT, "Universidad", "2do Semestre", "C\u00e1lculo Vectorial", "Diagramas")

# nombre con caracteres especiales (como los fantasmas reales)
name = "03_-_Representaci\u00f3n_gr\u00e1fica_01"
mpath = os.path.join(MMDDIR, name + ".mmd")
print("mpath:", mpath)

try:
    open(mpath, "w", encoding="utf-8").write("---\ntitle: test\n---\nflowchart TD\n  A[\"Hola\"]:::k2\n")
    print("escrito ok")
except Exception as e:
    print("ESCRITURA FALLO:", type(e).__name__, e)
    sys.exit(1)

MMDC = r"C:\Users\Steven Sànchez\AppData\Roaming\npm\mmdc.cmd"
out_svg = os.path.join(DIAG_DIR, name + ".svg")
print("out_svg:", out_svg)

try:
    r = subprocess.run([MMDC, "-i", mpath, "-o", out_svg, "-b", "white"], capture_output=True, text=True, timeout=30)
    print("rc:", r.returncode)
    print("stdout:", r.stdout[:200])
    print("stderr:", r.stderr[:200])
except Exception as e:
    print("SUBPROCESS FALLO:", type(e).__name__, e)
    sys.exit(1)

print("svg existe:", os.path.isfile(out_svg))

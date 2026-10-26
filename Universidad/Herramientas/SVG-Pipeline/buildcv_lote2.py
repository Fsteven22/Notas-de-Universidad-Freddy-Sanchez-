# -*- coding: utf-8 -*-
import os, sys, json, shutil, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib

TMP = os.path.dirname(os.path.abspath(__file__))
MMDDIR = os.path.join(TMP, "mmd2", "cv_lote2")
PREV = os.path.join(TMP, "previews", "cv_lote2")
VAULT_DIAG = os.path.join(vlib.materia("2do", "V"), "Diagramas")
os.makedirs(MMDDIR, exist_ok=True)
os.makedirs(PREV, exist_ok=True)
os.makedirs(VAULT_DIAG, exist_ok=True)

STD = '''
classDef k1 fill:#e8f5e8,stroke:#4caf50,color:#1b3a1b;
classDef k2 fill:#f3e5f5,stroke:#9c27b0,color:#3a1b3a;
classDef k3 fill:#e3f2fd,stroke:#2196f3,color:#0d2f52;
classDef k4 fill:#fff3e0,stroke:#ff9800,color:#4a2c00;
classDef k5 fill:#fff8e1,stroke:#fbc02d,color:#4a3b00;
classDef k6 fill:#ffebee,stroke:#e53935,color:#4a1010;
classDef k7 fill:#e0f2f1,stroke:#009688,color:#00332e;
'''

def normaliza(nombre):
    return nombre.replace("\u2013", "-").replace("\u2014", "-")

CV = {}

# Jacobiano
CV["02_-_Jacobiano_de_la_transformación_01"] = '''
flowchart TD
  A["Jacobiano de la transformación"]:::k2
  A --> B["x = x(u,v), y = y(u,v)"]:::k3
  B --> C["J = ∂(x,y)/∂(u,v)"]:::k3
  C --> D["|J| = factor de escala del área"]:::k1
  A --> E["∬_R f dA = ∬_S f |J| du dv"]:::k4
'''

CV["02_-_Jacobiano_de_la_transformación_02"] = '''
flowchart TD
  A["Jacobiano en 3D"]:::k2
  A --> B["x=x(u,v,w), y=y(u,v,w), z=z(u,v,w)"]:::k3
  B --> C["J = determinante 3×3 de derivadas parciales"]:::k3
  C --> D["dV = |J| du dv dw"]:::k1
'''

# Teorema de Fubini
CV["02_-_Teorema_de_Fubini_01"] = '''
flowchart TD
  A["Teorema de Fubini"]:::k2
  A --> B["∬_R f(x,y) dA = ∫_a^b ∫_c^d f(x,y) dy dx"]:::k3
  B --> C["Se puede cambiar el orden de integración"]:::k1
  A --> D["Condición: f continua en R"]:::k4
'''

CV["02_-_Teorema_de_Fubini_02"] = '''
flowchart TD
  A["Fubini para integrales triples"]:::k2
  A --> B["∭_E f dV = ∫∫∫ f(x,y,z) dz dy dx"]:::k3
  B --> C["6 órdenes posibles de integración"]:::k1
  C --> D["Elegir el más simple"]:::k1
'''

# Teorema Fundamental de Integrales de Línea
CV["05_-_Teorema_Fundamental_de_las_Integrales_de_Línea_01"] = '''
flowchart TD
  A["Teorema fundamental de integrales de línea"]:::k2
  A --> B["∫_C ∇f · dr = f(B) − f(A)"]:::k3
  B --> C["Campo conservativo"]:::k3
  C --> D["Independiente de la ruta"]:::k1
  D --> E["Depende solo de los extremos"]:::k1
'''

CV["05_-_Teorema_Fundamental_de_las_Integrales_de_Línea_02"] = '''
flowchart TD
  A["Condición de conservatividad"]:::k2
  A --> B["∇ × F = 0"]:::k3
  B --> B1["Irrotacional"]:::k3
  A --> C["∮_C F·dr = 0 sobre cualquier curva cerrada"]:::k4
'''

# ---------------------------------------------------------------
def main():
    targets = list(CV.keys())
    mmdc = shutil.which("mmdc") or shutil.which("mmdc.cmd") or r"C:\Users\Steven Sànchez\AppData\Roaming\npm\mmdc.cmd"
    ok = 0
    fail = 0
    for name in targets:
        src = CV[name].strip() + STD
        p = os.path.join(MMDDIR, name + ".mmd")
        open(p, "w", encoding="utf-8").write("---\ntitle: %s\n---\n%s" % (name.replace("_", " "), src))
        out_svg = os.path.join(VAULT_DIAG, name + ".svg")
        out_png = os.path.join(PREV, name + ".png")
        try:
            subprocess.run([mmdc, "-i", p, "-o", out_svg, "-b", "white"], capture_output=True, text=True, timeout=30)
            subprocess.run([mmdc, "-i", p, "-o", out_png, "-b", "white", "-s", "2"], capture_output=True, text=True, timeout=30)
        except Exception as e:
            print("RUN FAIL", name, e)
            fail += 1
            continue
        if os.path.isfile(out_svg) and os.path.isfile(out_png):
            ok += 1
            print("OK  ", name)
        else:
            fail += 1
            print("FAIL", name)
    print("FINAL: OK=%d fail=%d de %d" % (ok, fail, len(targets)))

main()


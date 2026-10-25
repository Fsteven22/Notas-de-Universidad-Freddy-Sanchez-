# -*- coding: utf-8 -*-
import os, sys, json, shutil, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib

TMP = os.path.dirname(os.path.abspath(__file__))
MMDDIR = os.path.join(TMP, "mmd2", "cv_nabla")
PREV = os.path.join(TMP, "previews", "cv_nabla")
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

CV = {}

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_01 — Definición del nabla
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_01"] = '''
flowchart TD
  A["Operador nabla<br/>∇ = (∂/∂x, ∂/∂y, ∂/∂z)"]:::k2
  A --> B["Del operator / nabla"]:::k3
  B --> B1["Vector de operadores diferenciales"]:::k3
  A --> C["Se aplica a campos escalares y vectoriales"]:::k4
  C --> C1["∇f → campo vectorial (gradiente)"]:::k4
  C --> C2["∇·F → campo escalar (divergencia)"]:::k4
  C --> C3["∇×F → campo vectorial (rotacional)"]:::k4
  A --> D["Notación alternativa: ∇ = del"]:::k1
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_02 — Gradiente
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_02"] = '''
flowchart TD
  A["Gradiente ∇f"]:::k2
  A --> B["Dirección de mayor aumento de f"]:::k3
  B --> B1["Magnitud = tasa de cambio máxima"]:::k3
  A --> C["Perpendicular a las curvas de nivel"]:::k4
  C --> C1["f(x,y,z) = constante"]:::k4
  A --> D["Campo conservativo si F = ∇f"]:::k1
  D --> D1["∇ × ∇f = 0"]:::k1
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_03 — Divergencia
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_03"] = '''
flowchart TD
  A["Divergencia ∇·F"]:::k2
  A --> B["Fluxo neto salida por unidad de volumen"]:::k3
  B --> B1["Positivo: fuente"]:::k3
  B --> B2["Negativo: sumidero"]:::k3
  B --> B3["Cero: campo solenoidal"]:::k3
  A --> C["∇·F = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z"]:::k4
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_04 — Rotacional
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_04"] = '''
flowchart TD
  A["Rotacional ∇×F"]:::k2
  A --> B["Tendencia a rotar del campo"]:::k3
  B --> B1["Dirección = eje de rotación<br/>por regla de la mano derecha"]:::k3
  A --> C["Campo irrotacional si ∇×F = 0"]:::k4
  C --> C1["Campo conservativo"]:::k4
  A --> D["∇×F = ( ∂F₃/∂y − ∂F₂/∂z, ∂F₁/∂z − ∂F₃/∂x, ∂F₂/∂x − ∂F₁/∂y )"]:::k1
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_05 — Laplaciano
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_05"] = '''
flowchart TD
  A["Laplaciano ∇²f = ∇·(∇f)"]:::k2
  A --> B["∇²f = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²"]:::k3
  B --> C["Ecuación de Laplace: ∇²f = 0"]:::k4
  C --> C1["Campos potenciales"]:::k4
  A --> D["Ecuación de calor: ∂u/∂t = k ∇²u"]:::k5
  D --> D1["Difusión de temperatura"]:::k5
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_06 — Identidades del nabla I
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_06"] = '''
flowchart TD
  A["Identidades del nabla I"]:::k2
  A --> B["∇·(∇×F) = 0"]:::k3
  B --> B1["Divergencia de un rotacional es cero"]:::k3
  A --> C["∇×(∇f) = 0"]:::k4
  C --> C1["Rotacional de un gradiente es cero"]:::k4
  A --> D["∇(fg) = f∇g + g∇f"]:::k1
  A --> E["∇·(fF) = f(∇·F) + F·(∇f)"]:::k1
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_07 — Identidades del nabla II
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_07"] = '''
flowchart TD
  A["Identidades del nabla II"]:::k2
  A --> B["∇×(∇×F) = ∇(∇·F) − ∇²F"]:::k3
  A --> C["∇×(fF) = f(∇×F) + (∇f)×F"]:::k4
  A --> D["∇(F·G) = F×(∇×G) + G×(∇×F) + (F·∇)G + (G·∇)F"]:::k5
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_08 — Campo conservativo
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_08"] = '''
flowchart TD
  A["Campo conservativo F = ∇f"]:::k2
  A --> B["∇ × F = 0"]:::k3
  B --> B1["Irrotacional"]:::k3
  A --> C["∫C F·dr = f(B) − f(A)"]:::k4
  C --> C1["Independiente de la ruta"]:::k4
  C --> C2["Depende solo de los extremos"]:::k4
  A --> D["Potencial escalar f existe"]:::k1
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_09 — Nabla en coordenadas cilíndricas
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_09"] = '''
flowchart TD
  A["∇ en coordenadas cilíndricas (r, θ, z)"]:::k2
  A --> B["∇ = e_r ∂/∂r + e_θ (1/r)∂/∂θ + e_z ∂/∂z"]:::k3
  B --> C["∇f = e_r ∂f/∂r + e_θ (1/r)∂f/∂θ + e_z ∂f/∂z"]:::k3
  A --> D["∇·F = (1/r) ∂(rF_r)/∂r + (1/r) ∂F_θ/∂θ + ∂F_z/∂z"]:::k4
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_10 — Nabla en coordenadas esféricas
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_10"] = '''
flowchart TD
  A["∇ en coordenadas esféricas (r, θ, φ)"]:::k2
  A --> B["∇ = e_r ∂/∂r + e_θ (1/r)∂/∂θ + e_φ (1/(r sin θ))∂/∂φ"]:::k3
  A --> C["∇²f = (1/r²) ∂/∂r(r² ∂f/∂r) + ..."]:::k4
  C --> C1["Términos angulares"]:::k4
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_11 — Sustancial / material
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_11"] = '''
flowchart TD
  A["Derivada sustancial D/Dt = ∂/∂t + (v·∇)"]:::k2
  A --> B["Término local ∂/∂t"]:::k3
  B --> B1["Cambio en un punto fijo"]:::k3
  A --> C["Término convectivo (v·∇)"]:::k4
  C --> C1["Cambio por movimiento del fluido"]:::k4
'''

# ============================================================
# 02_-_Operador_nabla_y_sus_propiedades_12 — Resumen visual
# ============================================================
CV["02_-_Operador_nabla_y_sus_propiedades_12"] = '''
flowchart TD
  A["∇ — Operador nabla"]:::k2
  A --> B["∇f → Gradiente<br/>Campo vectorial"]:::k3
  A --> C["∇·F → Divergencia<br/>Campo escalar"]:::k4
  A --> D["∇×F → Rotacional<br/>Campo vectorial"]:::k5
  A --> E["∇²f → Laplaciano<br/>Campo escalar"]:::k1
'''

def normaliza(nombre):
    return nombre.replace("\u2013", "-").replace("\u2014", "-")

CV_norm = {}
for k, v in CV.items():
    CV_norm[normaliza(k)] = v
CV = CV_norm

# ---------------------------------------------------------------
def main():
    cats = json.load(open(os.path.join(TMP, "catalogo_cv.json"), encoding="utf-8"))
    ghosts = list(cats["ghosts"].keys())
    nabla = [g for g in ghosts if "Operador_nabla" in g or "nabla" in g.lower()]
    nabla_norm = [normaliza(g) for g in nabla]
    print("fantasmas nabla:", len(nabla_norm))
    missing = [k for k in nabla_norm if k not in CV]
    extra = [k for k in CV if normaliza(k) not in [normaliza(g) for g in ghosts]]
    print("con diagrama:", len(CV))
    print("faltan diagrama:", len(missing))
    if missing:
        print("primeros 10 que faltan:", missing[:10])
    if extra:
        print("sobran:", extra)
    if missing:
        raise SystemExit(1)
    mmdc = shutil.which("mmdc") or shutil.which("mmdc.cmd") or r"C:\Users\Steven Sànchez\AppData\Roaming\npm\mmdc.cmd"
    fails = []
    for name in nabla_norm:
        src = CV[name].strip() + STD
        p = os.path.join(MMDDIR, name + ".mmd")
        open(p, "w", encoding="utf-8").write("---\ntitle: %s\n---\n%s" % (name.replace("_", " "), src))
        out_svg = os.path.join(VAULT_DIAG, name + ".svg")
        out_png = os.path.join(PREV, name + ".png")
        r1 = subprocess.run([mmdc, "-i", p, "-o", out_svg, "-b", "white"], capture_output=True, text=True, timeout=30)
        r2 = subprocess.run([mmdc, "-i", p, "-o", out_png, "-b", "white", "-s", "2"], capture_output=True, text=True, timeout=30)
        if not (os.path.isfile(out_svg) and os.path.isfile(out_png)):
            fails.append(name)
            print("FAIL", name)
            print((r1.stderr or "")[:300])
            print((r2.stderr or "")[:300])
        else:
            print("OK  ", name)
    print("total fails:", len(fails), fails)

main()

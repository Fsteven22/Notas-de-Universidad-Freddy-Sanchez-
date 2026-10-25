# -*- coding: utf-8 -*-
import os, sys, json, shutil, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib

TMP = os.path.dirname(os.path.abspath(__file__))
MMDDIR = os.path.join(TMP, "mmd2", "cv")
PREV = os.path.join(TMP, "previews", "cv")
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

CV["02_-_Operador_nabla_y_sus_propiedades_01"] = '''
flowchart TD
  A["Operador nabla<br/>\u2207 = (\u2202/\u2202x, \u2202/\u2202y, \u2202/\u2202z)"]:::k2
  A --> B["Gradiente: \u2207f"]:::k3
  B --> B1["Dirección de máximo<br/>aumento de f"]:::k3
  A --> C["Divergencia: \u2207·F"]:::k4
  C --> C1["Fluxo neto salida de un punto"]:::k4
  A --> D["Rotacional: \u2207×F"]:::k5
  D --> D1["Tendencia a rotar del campo"]:::k5
'''

CV["02_-_Operador_nabla_y_sus_propiedades_02"] = '''
flowchart TD
  A["Identidades del nabla"]:::k2
  A --> B["\u2207·(\u2207×F) = 0"]:::k3
  A --> C["\u2207×(\u2207f) = 0"]:::k4
  A --> D["\u2207²f = \u2207·(\u2207f)"]:::k5
  A --> E["\u2207(fg) = f\u2207g + g\u2207f"]:::k1
'''

CV["02_-_Jacobiano_de_la_transformaci�n_01"] = '''
flowchart TD
  A["Jacobiano de la transformación"]:::k2
  A --> B["x = x(u,v), y = y(u,v)"]:::k3
  B --> C["J = ∂(x,y)/∂(u,v)"]:::k3
  C --> D["|J| = factor de escala<br/>del área"]:::k1
  A --> E["du dv = |J|⁻¹ dx dy"]:::k4
'''

CV["02_-_Jacobiano_de_la_transformaci�n_02"] = '''
flowchart TD
  A["Cambio de variables en dobles integrales"]:::k2
  A --> B["∬_R f(x,y) dA"]:::k3
  B --> C["∬_S f(x(u,v),y(u,v)) |J| du dv"]:::k3
  C --> D["J = determinante de la<br/>matriz jacobiana"]:::k1
'''

CV["02_-_Integral_de_superficie_de_una_funci�n_escalar_01"] = '''
flowchart TD
  A["Integral de superficie de función escalar"]:::k2
  A --> B["∬_S f(x,y,z) dS"]:::k3
  B --> C["S: superficie suave en R³"]:::k3
  C --> D["dS: elemento diferencial de área"]:::k1
  A --> E["Interpretación: masa de una lámina<br/>con densidad f(x,y,z)"]:::k4
'''

CV["02_-_Integral_de_superficie_de_una_funci�n_escalar_02"] = '''
flowchart TD
  A["Parametrización de superficie"]:::k2
  A --> B["r(u,v) = ⟨x(u,v), y(u,v), z(u,v)⟩"]:::k3
  B --> C["dS = |r_u × r_v| du dv"]:::k3
  C --> D["∬_S f dS = ∬_D f(r(u,v)) |r_u × r_v| du dv"]:::k1
'''

CV["02_-_Integrales_triples_en_regiones_generales_01"] = '''
flowchart TD
  A["Integral triple en región general"]:::k2
  A --> B["∭_E f(x,y,z) dV"]:::k3
  B --> C["E acotada: proyectar sobre plano coordenado"]:::k3
  C --> D["Límites de integración<br/>funciones de las otras variables"]:::k1
'''

CV["02_-_Integrales_triples_en_coordenadas_cil�ndricas_04"] = '''
flowchart TD
  A["Coordenadas cilíndricas"]:::k2
  A --> B["x = r cos θ"]:::k3
  A --> C["y = r sin θ"]:::k3
  A --> D["z = z"]:::k3
  B --> E["dV = r dz dr dθ"]:::k1
  C --> E
  D --> E
'''

CV["02_-_Masa_de_un_s�lido_con_densidad_variable_01"] = '''
flowchart TD
  A["Masa de sólido con densidad variable"]:::k2
  A --> B["M = ∭_E ρ(x,y,z) dV"]:::k3
  B --> C["ρ: función de densidad"]:::k3
  C --> D["Centro de masa: (x̄, ȳ, z̄)"]:::k1
'''

CV["02_-_Teorema_de_Fubini_01"] = '''
flowchart TD
  A["Teorema de Fubini"]:::k2
  A --> B["∬_R f(x,y) dA = ∫_a^b ∫_c^d f(x,y) dy dx"]:::k3
  B --> C["Se puede cambiar el orden<br/>de integración"]:::k1
  A --> D["Condición: f continua en R"]:::k4
'''

CV["02_-_Propiedades_de_las_integrales_m�ltiples_01"] = '''
flowchart TD
  A["Propiedades de integrales múltiples"]:::k2
  A --> B["Linealidad: ∭(af + bg) = a∭f + b∭g"]:::k3
  A --> C["Aditividad: ∭_{E∪F} = ∭_E + ∭_F"]:::k4
  A --> D["Acotación: m·V(E) ≤ ∭_E f ≤ M·V(E)"]:::k5
'''

CV["05_-_Teorema_Fundamental_de_las_Integrales_de_L�nea_01"] = '''
flowchart TD
  A["Teorema fundamental de integrales de línea"]:::k2
  A --> B["∫_C ∇f · dr = f(B) - f(A)"]:::k3
  B --> C["Campo conservativo"]:::k3
  C --> D["Independiente de la ruta"]:::k1
'''

CV["05_-_Valor_promedio_de_una_funci�n_01"] = '''
flowchart TD
  A["Valor promedio de una función"]:::k2
  A --> B["f_prom = (1/V(E)) ∭_E f dV"]:::k3
  B --> C["V(E): volumen de la región"]:::k3
  C --> D["Promedio sobre el dominio"]:::k1
'''

CV["06_-_Cambio_de_orden_de_integraci�n_01"] = '''
flowchart TD
  A["Cambio de orden de integración"]:::k2
  A --> B["Dibujar la región de integración"]:::k3
  B --> C["Identificar límites como funciones"]:::k3
  C --> D["Reescribir integral con nuevo orden"]:::k1
'''

# ---------------------------------------------------------------
def main():
    cats = json.load(open(os.path.join(TMP, "catalogo_cv.json"), encoding="utf-8"))
    ghosts = list(cats["ghosts"].keys())
    missing = [k for k in ghosts if k not in CV]
    extra = [k for k in CV if k not in ghosts]
    print("fantasmas totales:", len(ghosts))
    print("con diagrama:", len(CV))
    print("faltan diagrama:", len(missing))
    if missing:
        print("primeros 10 que faltan:", missing[:10])
    if extra:
        print("sobran:", extra)
    if missing:
        raise SystemExit(1)
    mmdc = shutil.which("mmdc") or shutil.which("mmdc.cmd")
    fails = []
    for name in ghosts:
        src = CV[name].strip() + STD
        p = os.path.join(MMDDIR, name + ".mmd")
        open(p, "w", encoding="utf-8").write("---\ntitle: %s\n---\n%s" % (name.replace("_", " "), src))
        out_svg = os.path.join(VAULT_DIAG, name + ".svg")
        out_png = os.path.join(PREV, name + ".png")
        r1 = subprocess.run([mmdc, "-i", p, "-o", out_svg, "-b", "white"], capture_output=True, text=True)
        r2 = subprocess.run([mmdc, "-i", p, "-o", out_png, "-b", "white", "-s", "2"], capture_output=True, text=True)
        if not (os.path.isfile(out_svg) and os.path.isfile(out_png)):
            fails.append(name)
            print("FAIL", name)
            print((r1.stderr or "")[:400])
            print((r2.stderr or "")[:400])
        else:
            print("OK  ", name)
    print("total fails:", len(fails), fails)

main()

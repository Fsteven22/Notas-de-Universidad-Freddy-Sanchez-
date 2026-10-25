# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib

TMP = os.path.dirname(os.path.abspath(__file__))
MMDDIR = os.path.join(TMP, "mmd2", "cv_lote3")
PREV = os.path.join(TMP, "previews", "cv_lote3")
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

# ============================================================
# 01 - Producto punto y ángulo entre vectores
# ============================================================
CV["01_-_Producto_punto_y_angulo_entre_vectores_01"] = '''
flowchart TD
  A["Producto punto: A·B = |A||B|cos(θ)"]:::k2
  A --> B["θ = ángulo entre vectores"]:::k3
  B --> C["θ = 0°: mismos direcciones"]:::k3
  B --> D["θ = 90°: ortogonales (A·B=0)"]:::k3
  B --> E["θ = 180°: direcciones opuestas"]:::k3
  A --> F["Proyección de A sobre B:<br/>(A·B/|B|²)·B"]:::k4
  F --> G["Componente de A en dirección B"]:::k4
'''

# ============================================================
# 02 - Producto cruz y área
# ============================================================
CV["02_-_Producto_cruz_y_area_01"] = '''
flowchart TD
  A["Producto cruz: A × B"]:::k2
  A --> B["|A × B| = |A||B|sin(θ)"]:::k3
  B --> C["Área del paralelogramo<br/>generado por A y B"]:::k3
  A --> D["Dirección: regla de la mano derecha"]:::k4
  D --> D1["Perpendicular a ambos vectores"]:::k4
  A --> E["A × B = -(B × A)"]:::k1
  E --> E1["Anticonmutativo"]:::k1
'''

# ============================================================
# 03 - Ecuación de recta en R3
# ============================================================
CV["03_-_Ecuacion_de_recta_en_R3_01"] = '''
flowchart TD
  A["Recta en R³"]:::k2
  A --> B["Ecuación vectorial: r(t) = P₀ + t·v"]:::k3
  B --> C["P₀: punto sobre la recta"]:::k3
  B --> D["v: vector dirección"]:::k3
  A --> E["Ecuación paramétrica:<br/>x = x₀ + at, y = y₀ + bt, z = z₀ + ct"]:::k4
  A --> F["Ecuación simétrica:<br/>(x-x₀)/a = (y-y₀)/b = (z-z₀)/c"]:::k5
'''

# ============================================================
# 04 - Ecuación de plano en R3
# ============================================================
CV["04_-_Ecuacion_de_plano_en_R3_01"] = '''
flowchart TD
  A["Plano en R³"]:::k2
  A --> B["Ecuación punto-normal:<br/>n·(r - r₀) = 0"]:::k3
  B --> C["n: vector normal al plano"]:::k3
  B --> D["r₀: punto sobre el plano"]:::k3
  A --> E["Forma general: ax + by + cz + d = 0"]:::k4
  E --> E1["n = ⟨a, b, c⟩"]:::k4
  A --> F["Distancia punto-plano:<br/>d = |n·(P - P₀)|/|n|"]:::k5
'''

# ============================================================
# 05 - Gradiente y campo de pendiente máxima
# ============================================================
CV["05_-_Gradiente_y_campo_de_pendiente_01"] = '''
flowchart TD
  A["Gradiente ∇f(x,y,z)"]:::k2
  A --> B["∇f = ⟨∂f/∂x, ∂f/∂y, ∂f/∂z⟩"]:::k3
  B --> C["Apunta en dirección de<br/>máximo aumento de f"]:::k3
  A --> D["|∇f| = tasa de cambio máxima"]:::k4
  A --> E["Perpendicular a las superficies de nivel"]:::k5
  E --> E1["f(x,y,z) = constante"]:::k5
  A --> G["Campo de pendiente máxima"]:::k1
'''

# ============================================================
# 06 - Derivada direccional
# ============================================================
CV["06_-_Derivada_direccional_01"] = '''
flowchart TD
  A["Derivada direccional"]:::k2
  A --> B["D_u f = ∇f · u"]:::k3
  B --> C["u: vector unitario (dirección)"]:::k3
  C --> D["Tasa de cambio de f en dirección u"]:::k4
  A --> E["Máximo: ∇f (u = ∇f/|∇f|)"]:::k5
  A --> F["Mínimo: -∇f (u = -∇f/|∇f|)"]:::k6
  A --> G["Cero: u ⟂ ∇f (nivel)"]:::k1
'''

# ============================================================
# 07 - Regla de la cadena multivariable
# ============================================================
CV["07_-_Regla_de_la_cadena_multivariable_01"] = '''
flowchart TD
  A["Regla de la cadena"]:::k2
  A --> B["z = f(x,y), x=x(t), y=y(t)"]:::k3
  B --> C["dz/dt = ∂f/∂x·dx/dt + ∂f/∂y·dy/dt"]:::k3
  A --> D["z = f(x,y,z), x=x(t),y=y(t),z=z(t)"]:::k4
  D --> E["dz/dt = Σ ∂f/∂xi · dxi/dt"]:::k4
  A --> F["Forma vectorial: dz/dt = ∇f · dr/dt"]:::k5
'''

# ============================================================
# 08 - Extremo local y segunda derivada
# ============================================================
CV["08_-_Extremo_local_segunda_derivada_01"] = '''
flowchart TD
  A["Extremo local de f(x,y)"]:::k2
  A --> B["Punto crítico: ∇f = 0"]:::k3
  B --> C["D = f_xx·f_yy - (f_xy)²"]:::k4
  C --> D["D > 0, f_xx > 0: mínimo local"]:::k4
  C --> E["D > 0, f_xx < 0: máximo local"]:::k4
  C --> F["D < 0: punto de silla"]:::k4
  C --> G["D = 0: prueba inconclusa"]:::k1
'''

# ============================================================
# 09 - Multiplicadores de Lagrange
# ============================================================
CV["09_-_Multiplicadores_de_Lagrange_01"] = '''
flowchart TD
  A["Optimización restringida"]:::k2
  A --> B["Extremar f(x,y,z) sujeto a g(x,y,z) = c"]:::k3
  B --> C["∇f = λ∇g"]:::k4
  C --> D["λ: multiplicador de Lagrange"]:::k4
  D --> E["∇f paralelo a ∇g"]:::k5
  E --> E1["Curva de nivel tangente a la restricción"]:::k5
  A --> F["Resolver sistema: ∇f=λ∇g, g=c"]:::k1
'''

# ============================================================
# 10 - Integral doble región rectangular
# ============================================================
CV["10_-_Integral_doble_region_rectangular_01"] = '''
flowchart TD
  A["Integral doble rectangular"]:::k2
  A --> B["R = [a,b] × [c,d]"]:::k3
  B --> C["∬_R f(x,y) dA"]:::k3
  C --> D["= ∫_a^b ∫_c^d f(x,y) dy dx"]:::k4
  D --> E["= ∫_c^d ∫_a^b f(x,y) dx dy"]:::k4
  A --> F["Interpretación: volumen bajo la superficie"]:::k5
'''

# ============================================================
# 11 - Integral doble región general
# ============================================================
CV["11_-_Integral_doble_region_general_01"] = '''
flowchart TD
  A["Integral doble región general"]:::k2
  A --> B["Región tipo I: a≤x≤b, g₁(x)≤y≤g₂(x)"]:::k3
  B --> C["∬_D f dA = ∫_a^b ∫_{g₁(x)}^{g₂(x)} f dy dx"]:::k3
  A --> D["Región tipo II: c≤y≤d, h₁(y)≤x≤h₂(y)"]:::k4
  D --> E["∬_D f dA = ∫_c^d ∫_{h₁(y)}^{h₂(y)} f dx dy"]:::k4
  A --> F["Dibujar la región antes de integrar"]:::k1
'''

# ============================================================
# 12 - Integral triple coordenadas esféricas
# ============================================================
CV["12_-_Integral_triple_esfericas_01"] = '''
flowchart TD
  A["Coordenadas esféricas (ρ, θ, φ)"]:::k2
  A --> B["x = ρ sinφ cosθ"]:::k3
  A --> C["y = ρ sinφ sinθ"]:::k3
  A --> D["z = ρ cosφ"]:::k3
  A --> E["dV = ρ² sinφ dρ dφ dθ"]:::k4
  E --> F["∬∭_E f dV = ∫∫∫ f ρ² sinφ dρ dφ dθ"]:::k4
  A --> G["ρ: distancia al origen"]:::k1
  G --> G1["θ: azimutal (xy-plano)"]:::k1
  G --> G2["φ: polar (desde eje z)"]:::k1
'''

# ============================================================
# 13 - Campo conservativo y potencial
# ============================================================
CV["13_-_Campo_conservativo_potencial_01"] = '''
flowchart TD
  A["Campo conservativo F"]:::k2
  A --> B["F = ∇f (f = función potencial)"]:::k3
  B --> C["∇ × F = 0"]:::k3
  A --> D["∫C F·dr = f(B) - f(A)"]:::k4
  D --> E["Independiente de la ruta"]:::k4
  D --> F["∮C F·dr = 0 (curva cerrada)"]:::k4
  A --> G["Condición: dominio simplemente conexo"]:::k1
'''

# ============================================================
# 14 - Flujo de campo vectorial
# ============================================================
CV["14_-_Flujo_de_campo_vectorial_01"] = '''
flowchart TD
  A["Flujo de campo vectorial"]:::k2
  A --> B["∬_S F·n dS"]:::k3
  B --> C["F: campo vectorial"]:::k3
  B --> D["n: vector normal unitario a S"]:::k3
  A --> E["Interpretación: cantidad que cruza S"]:::k4
  E --> E1["Flujo neto de entrada/salida"]:::k4
  A --> F["Superficie cerrada: teorema de la divergencia"]:::k5
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

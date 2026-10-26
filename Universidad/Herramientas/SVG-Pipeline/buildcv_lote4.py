# -*- coding: utf-8 -*-
import os, sys, subprocess, shutil
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib

TMP = os.path.dirname(os.path.abspath(__file__))
MMDDIR = os.path.join(TMP, "mmd2", "cv_lote4")
PREV = os.path.join(TMP, "previews", "cv_lote4")
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

# ============================================================
# Diagramas Mermaid específicos para conceptos de Cálculo Vectorial
# ============================================================
CV = {}

# --- Unidad 1: Geometría Analítica en R3 ---

CV["01_-_Distancias_en_R3"] = '''
flowchart TD
  A["Distancia en R³"]:::k2
  A --> B["Entre dos puntos: d = |P₁P₂|"]:::k3
  A --> C["Punto a recta: d = |(P-P₀)×v|/|v|"]:::k4
  A --> D["Punto a plano: d = |n·(P-P₀)|/|n|"]:::k5
  A --> E["Entre rectas paralelas: d = |(P₂-P₁)×v|/|v|"]:::k1
'''

CV["01_-_Rectas_en_R3"] = '''
flowchart TD
  A["Recta en R³"]:::k2
  A --> B["Vectorial: r(t) = P₀ + t·v"]:::k3
  A --> C["Paramétrica: x=x₀+at, y=y₀+bt, z=z₀+ct"]:::k4
  A --> D["Simétrica: (x-x₀)/a = (y-y₀)/b = (z-z₀)/c"]:::k5
  B --> E["P₀: punto, v: dirección"]:::k3
'''

CV["01_-_Sistema_de_referencia_espacial_en_R3"] = '''
flowchart TD
  A["Sistema de referencia en R³"]:::k2
  A --> B["Origen O y ejes x, y, z"]:::k3
  A --> C["Vectores unitarios: i, j, k"]:::k4
  A --> D["Punto P = (x, y, z)"]:::k5
  A --> E["Sistema derecho: i × j = k"]:::k1
'''

CV["01_-_Superficies_cuadraticas"] = '''
flowchart TD
  A["Superficies cuadráticas"]:::k2
  A --> B["Elipsoide: x²/a² + y²/b² + z²/c² = 1"]:::k3
  A --> C["Hiperboloide de una hoja: x²/a² + y²/b² - z²/c² = 1"]:::k4
  A --> D["Hiperboloide de dos hojas: -x²/a² - y²/b² + z²/c² = 1"]:::k5
  A --> E["Paraboloide elíptico: z = x²/a² + y²/b²"]:::k1
  A --> F["Paraboloide hiperbólico: z = x²/a² - y²/b²"]:::k1
'''

CV["01_-_Nociones_topologicas_en_Rn"] = '''
flowchart TD
  A["Nociones topológicas en Rⁿ"]:::k2
  A --> B["Bola abierta: B(P, r) = {Q : |PQ| < r}"]:::k3
  A --> C["Punto interior, exterior, frontera"]:::k4
  A --> D["Conjunto abierto, cerrado"]:::k5
  A --> E["Conjunto acotado y cerrado = compacto"]:::k1
'''

CV["01_-_Polinomios_de_Taylor"] = '''
flowchart TD
  A["Polinomio de Taylor multivariable"]:::k2
  A --> B["T₂(x) = f(P) + ∇f(P)·(x-P) + ½(x-P)·H(P)·(x-P)"]:::k3
  A --> C["H: matriz hessiana de segundas derivadas"]:::k4
  A --> D["Aproximación local de la función"]:::k5
'''

CV["01_–_Caminos_suaves_simples_y_cerrados"] = '''
flowchart TD
  A["Caminos en R³"]:::k2
  A --> B["Suave: derivable, tangente continua"]:::k3
  A --> C["Simple: no se autointerseca"]:::k4
  A --> D["Cerrado: punto inicial = punto final"]:::k5
  A --> E["Conturo: simple y cerrado"]:::k1
'''

CV["01_–_Campos_vectoriales_-_divergencia_y_rotacional"] = '''
flowchart TD
  A["Campo vectorial F(x,y,z)"]:::k2
  A --> B["Div: ∇·F = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z"]:::k3
  B --> B1["Positivo: fuente, Negativo: sumidero"]:::k3
  A --> C["Rot: ∇×F"]:::k4
  C --> C1["Tendencia a rotar del campo"]:::k4
'''

CV["01_–_Funciones_vectoriales_de_variable_escalar"] = '''
flowchart TD
  A["Función vectorial r(t) = ⟨x(t), y(t), z(t)⟩"]:::k2
  A --> B["r'(t) = ⟨x'(t), y'(t), z'(t)⟩: velocidad"]:::k3
  A --> C["|r'(t)|: velocidad módulo"]:::k4
  A --> D["Longitud de arco: s = ∫|r'(t)| dt"]:::k5
'''

CV["01_–_Integral_doble"] = '''
flowchart TD
  A["Integral doble ∬_R f(x,y) dA"]:::k2
  A --> B["Volumen bajo la superficie z = f(x,y)"]:::k3
  A --> C["Región R en el plano xy"]:::k4
  A --> D["Integral iterada: ∫∫ f dy dx"]:::k5
'''

CV["01_–_Integral_triple"] = '''
flowchart TD
  A["Integral triple ∭_E f(x,y,z) dV"]:::k2
  A --> B["Volumen o masa del sólido E"]:::k3
  A --> C["Región E en R³"]:::k4
  A --> D["Integral iterada: ∫∫∫ f dz dy dx"]:::k5
'''

CV["01_–_Integrales_múltiples"] = '''
flowchart TD
  A["Integrales múltiples"]:::k2
  A --> B["Doble: ∬_R f dA (área/volumen)"]:::k3
  A --> C["Triple: ∭_E f dV (volumen/masa)"]:::k4
  A --> D["Fubini: cambiar orden de integración"]:::k5
'''

CV["01_–_Producto_punto_y_ángulos"] = '''
flowchart TD
  A["Producto punto A·B = |A||B|cos(θ)"]:::k2
  A --> B["θ = ángulo entre vectores"]:::k3
  A --> C["A·B = 0: ortogonales"]:::k4
  A --> D["Proyección: comp_B A = (A·B)/|B|"]:::k5
'''

CV["01_–_Teorema_de_cambio_de_variable_en_R3"] = '''
flowchart TD
  A["Cambio de variable en R³"]:::k2
  A --> B["x = x(u,v,w), y = y(u,v,w), z = z(u,v,w)"]:::k3
  B --> C["J = matriz jacobiana 3×3"]:::k4
  C --> D["|J| = factor de escala del volumen"]:::k5
  D --> E["dV = |J| du dv dw"]:::k1
'''

CV["01_–_Teoremas_de_la_teoría_vectorial"] = '''
flowchart TD
  A["Teoremas del cálculo vectorial"]:::k2
  A --> B["Gradiente: ∇f"]:::k3
  A --> C["Divergencia: ∇·F"]:::k4
  A --> D["Rotacional: ∇×F"]:::k5
  A --> E["Teoremas: Gradiente, Divergencia, Stokes"]:::k1
'''

CV["01_–_Transformaciones_entre_sistemas_de_coordenadas"] = '''
flowchart TD
  A["Transformaciones de coordenadas"]:::k2
  A --> B["Cartesianas → Cilíndricas"]:::k3
  A --> C["Cartesianas → Esféricas"]:::k4
  A --> D["Jacobiano = factor de escala"]:::k5
'''

CV["01_–_Volumen_de_sólidos_en_R3"] = '''
flowchart TD
  A["Volumen de sólidos en R³"]:::k2
  A --> B["V = ∭_E dV"]:::k3
  A --> C["Coordenadas rectangulares, cilíndricas, esféricas"]:::k4
  A --> D["Jacobiano ajusta el elemento de volumen"]:::k5
'''

CV["01_–_Área_de_una_región_en_R2"] = '''
flowchart TD
  A["Área de región en R²"]:::k2
  A --> B["A = ∬_R dA"]:::k3
  A --> C["Integral doble sobre la región"]:::k4
'''

CV["01_–_Área_de_una_superficie"] = '''
flowchart TD
  A["Área de superficie"]:::k2
  A --> B["A = ∬_D |r_u × r_v| du dv"]:::k3
  A --> C["r(u,v): parametrización de la superficie"]:::k4
'''

# --- Unidad 2: Superficies y Coordenadas ---

CV["02_-_Planos_en_R3"] = '''
flowchart TD
  A["Plano en R³"]:::k2
  A --> B["Punto-normal: n·(r - r₀) = 0"]:::k3
  A --> C["General: ax + by + cz + d = 0"]:::k4
  A --> D["n = ⟨a, b, c⟩ es normal al plano"]:::k5
'''

CV["02_-_Relación_recta–plano"] = '''
flowchart TD
  A["Relación recta-plano"]:::k2
  A --> B["Recta sobre plano: v·n = 0"]:::k3
  A --> C["Recta paralela: v·n = 0, punto no en plano"]:::k4
  A --> D["Recta intersectante: v·n ≠ 0"]:::k5
'''

CV["02_-_Superficies_cilindricas"] = '''
flowchart TD
  A["Superficies cilíndricas"]:::k2
  A --> B["Generatriz paralela a un eje fijo"]:::k3
  A --> C["Directriz: curva en plano perpendicular"]:::k4
  A --> D["Ejemplo: x² + y² = r² (cilindro circular)"]:::k5
'''

CV["02_-_Transformaciones_entre_Coordenadas"] = '''
flowchart TD
  A["Transformaciones entre coordenadas"]:::k2
  A --> B["Cartesianas ↔ Cilíndricas"]:::k3
  A --> C["Cartesianas ↔ Esféricas"]:::k4
  A --> D["Jacobiano para cambio de variable en integrales"]:::k5
'''

CV["02_-_Vectores_en_R3"] = '''
flowchart TD
  A["Vectores en R³"]:::k2
  A --> B["Suma: A + B (regla del paralelogramo)"]:::k3
  A --> C["Producto escalar: k·A"]:::k4
  A --> D["Producto punto y cruz"]:::k5
'''

CV["02_–_Integral_de_superficie_de_una_función_escalar"] = '''
flowchart TD
  A["∬_S f(x,y,z) dS"]:::k2
  A --> B["S: superficie suave en R³"]:::k3
  A --> C["dS: elemento de área de superficie"]:::k4
  A --> D["Interpretación: masa de lámina con densidad f"]:::k5
'''

CV["02_–_Integrales_de_línea_escalares"] = '''
flowchart TD
  A["∫_C f(x,y,z) ds"]:::k2
  A --> B["C: curva suave parametrizada"]:::k3
  A --> C["ds: elemento de arco"]:::k4
  A --> D["Interpretación: área de cortina sobre C"]:::k5
'''

CV["02_–_Integrales_triples_en_coordenadas_cilíndricas"] = '''
flowchart TD
  A["Coordenadas cilíndricas (r, θ, z)"]:::k2
  A --> B["x = r cos θ, y = r sin θ, z = z"]:::k3
  A --> C["dV = r dz dr dθ"]:::k4
  A --> D["∭_E f dV = ∫∫∫ f r dz dr dθ"]:::k5
'''

CV["02_–_Integrales_triples_en_regiones_generales"] = '''
flowchart TD
  A["Región general E en R³"]:::k2
  A --> B["Proyectar sobre plano coordenado"]:::k3
  B --> C["Límites como funciones de las otras variables"]:::k4
  C --> D["∭_E f dV con límites variables"]:::k5
'''

CV["02_–_Jacobiano_de_la_transformación"] = '''
flowchart TD
  A["Jacobiano J = ∂(x,y,z)/∂(u,v,w)"]:::k2
  A --> B["Determinante de matriz 3×3 de derivadas parciales"]:::k3
  A --> C["|J| = factor de escala del volumen"]:::k4
  A --> D["dV_xyz = |J| dV_uvw"]:::k5
'''

CV["02_–_Masa_de_un_sólido_con_densidad_variable"] = '''
flowchart TD
  A["Masa M = ∭_E ρ(x,y,z) dV"]:::k2
  A --> B["ρ: función de densidad"]:::k3
  A --> C["Centro de masa: (x̄, ȳ, z̄)"]:::k4
  A --> D["x̄ = (1/M)∭ x ρ dV"]:::k5
'''

CV["02_–_Propiedades_de_las_integrales_múltiples"] = '''
flowchart TD
  A["Propiedades integrales múltiples"]:::k2
  A --> B["Linealidad: ∬(af+bg) = a∬f + b∬g"]:::k3
  A --> C["Aditividad: ∬_{R∪S} = ∬_R + ∬_S"]:::k4
  A --> D["Acotación: m·A(R) ≤ ∬_R f ≤ M·A(R)"]:::k5
'''

CV["02_–_Teorema_de_Fubini"] = '''
flowchart TD
  A["Teorema de Fubini"]:::k2
  A --> B["∬_R f dA = ∫_a^b ∫_c^d f dy dx"]:::k3
  A --> C["Cambiar orden de integración"]:::k4
  A --> D["f continua en R"]:::k5
'''

CV["02_–_Teoremas_de_Existencia_y_Clasificación"] = '''
flowchart TD
  A["Teoremas de existencia y clasificación"]:::k2
  A --> B["Extremo local: ∇f = 0, prueba de D"]:::k3
  A --> C["D > 0: máximo o mínimo"]:::k4
  A --> D["D < 0: punto de silla"]:::k5
'''

CV["02_–_Volumen_bajo_una_superficie"] = '''
flowchart TD
  A["Volumen bajo superficie z = f(x,y)"]:::k2
  A --> B["V = ∬_R f(x,y) dA"]:::k3
  A --> C["R: región en el plano xy"]:::k4
  A --> D["f(x,y) ≥ 0 sobre R"]:::k5
'''

# --- Unidad 3: Funciones de Varias Variables ---

CV["03_-_Representación_gráfica"] = '''
flowchart TD
  A["Gráfico de z = f(x,y)"]:::k2
  A --> B["Superficie en R³"]:::k3
  A --> C["Curvas de nivel: f(x,y) = c"]:::k4
  A --> D["Proyección en el plano xy"]:::k5
'''

CV["03_–_Aplicaciones_geométricas_básicas"] = '''
flowchart TD
  A["Aplicaciones geométricas"]:::k2
  A --> B["Área, volumen, masa"]:::k3
  A --> C["Centro de masa, momentos"]:::k4
  A --> D["Inercia, radiación de giro"]:::k5
'''

CV["03_–_Campos_conservativos_e_independencia_del_camino"] = '''
flowchart TD
  A["Campo conservativo F = ∇f"]:::k2
  A --> B["∫C F·dr = f(B) - f(A)"]:::k3
  B --> B1["Independiente de la ruta"]:::k3
  A --> C["∮C F·dr = 0 (curva cerrada)"]:::k4
'''

CV["03_–_Centro_de_masa_y_momentos"] = '''
flowchart TD
  A["Centro de masa y momentos"]:::k2
  A --> B["x̄ = M_yz / M, ȳ = M_xz / M"]:::k3
  A --> C["M_xz = ∭ x ρ dV, M_yz = ∭ y ρ dV"]:::k4
  A --> D["Momento de inercia: I_z = ∭ (x²+y²) ρ dV"]:::k5
'''

CV["03_–_Curvas_como_intersección_de_superficies"] = '''
flowchart TD
  A["Curva como intersección de superficies"]:::k2
  A --> B["S₁: F(x,y,z) = 0"]:::k3
  A --> C["S₂: G(x,y,z) = 0"]:::k4
  A --> D["C: S₁ ∩ S₂"]:::k5
'''

CV["03_–_Funciones_vectoriales"] = '''
flowchart TD
  A["Función vectorial r(t)"]:::k2
  A --> B["r'(t): velocidad"]:::k3
  A --> C["r''(t): aceleración"]:::k4
  A --> D["|r'(t)|: rapidez"]:::k5
'''

CV["03_–_Integral_de_superficie_vectorial_(Flujo)"] = '''
flowchart TD
  A["Flujo ∬_S F·n dS"]:::k2
  A --> B["F: campo vectorial"]:::k3
  A --> C["n: normal unitaria a S"]:::k4
  A --> D["Cantidad que cruza la superficie"]:::k5
'''

CV["03_–_Integrales_de_línea_vectoriales"] = '''
flowchart TD
  A["∫_C F·dr"]:::k2
  A --> B["F: campo vectorial"]:::k3
  A --> C["dr: diferencial de posición"]:::k4
  A --> D["Trabajo del campo sobre la curva"]:::k5
'''

CV["03_–_Integrales_triples_en_coordenadas_esféricas"] = '''
flowchart TD
  A["Coordenadas esféricas (ρ, θ, φ)"]:::k2
  A --> B["dV = ρ² sinφ dρ dφ dθ"]:::k3
  A --> C["ρ: radio, θ: azimut, φ: polar"]:::k4
  A --> D["∭_E f ρ² sinφ dρ dφ dθ"]:::k5
'''

CV["03_–_Interpretación_geométrica_de_la_integral_doble"] = '''
flowchart TD
  A["∬_R f(x,y) dA"]:::k2
  A --> B["Volumen bajo z = f(x,y)"]:::k3
  A --> C["f ≥ 0: volumen positivo"]:::k4
  A --> D["f cambia signo: volumen neto"]:::k5
'''

CV["03_–_Interpretación_geométrica_del_plano_tangente_y_la_aproximación_lineal"] = '''
flowchart TD
  A["Plano tangente y aproximación lineal"]:::k2
  A --> B["z = f(P₀) + ∇f(P₀)·(x-P₀)"]:::k3
  A --> C["Aproximación local de f cerca de P₀"]:::k4
  A --> D["Error de primer orden"]:::k5
'''

CV["03_–_Masa_de_una_lámina_con_densidad_variable"] = '''
flowchart TD
  A["Masa M = ∬_D ρ(x,y) dA"]:::k2
  A --> B["ρ: densidad superficial"]:::k3
  A --> C["Centro de masa en el plano"]:::k4
'''

CV["03_–_Teorema_de_Fubini_para_integrales_múltiples"] = '''
flowchart TD
  A["Fubini para integrales múltiples"]:::k2
  A --> B["Cambiar orden de integración"]:::k3
  A --> C["∭_E f dV en 6 órdenes posibles"]:::k4
'''

CV["03_–_Teorema_de_cambio_de_variables"] = '''
flowchart TD
  A["Cambio de variables"]:::k2
  A --> B["T: (u,v) → (x,y)"]:::k3
  B --> C["J = ∂(x,y)/∂(u,v)"]:::k4
  C --> D["∬_R f(x,y) dA = ∬_S f(x(u,v),y(u,v)) |J| du dv"]:::k5
'''

CV["03_–_Teorema_del_valor_medio_para_integrales_triples"] = '''
flowchart TD
  A["Valor medio para integrales triples"]:::k2
  A --> B["f_prom = (1/V(E)) ∭_E f dV"]:::k3
  A --> C["V(E): volumen de la región"]:::k4
'''

# --- Unidad 4: Optimización ---

CV["04_-_Teorema_de_la_Función_Implícita"] = '''
flowchart TD
  A["Teorema de la función implícita"]:::k2
  A --> B["F(x,y,z) = 0 define z = z(x,y)"]:::k3
  B --> C["∂z/∂x = -F_x/F_z, ∂z/∂y = -F_y/F_z"]:::k4
  A --> D["F_z ≠ 0 en el punto"]:::k5
'''

CV["04_–_Clasificación_de_superficies_por_secciones"] = '''
flowchart TD
  A["Clasificación por secciones planas"]:::k2
  A --> B["Sección con planos coordenados"]:::k3
  A --> C["Identificar tipo de superficie cuadrática"]:::k4
'''

CV["04_–_Criterios_de_conservatividad_en_R2_y_R3"] = '''
flowchart TD
  A["Criterios de conservatividad"]:::k2
  A --> B["∇×F = 0 (irrotacional)"]:::k3
  A --> C["Dominio simplemente conexo"]:::k4
  A --> D["F = ∇f existe"]:::k5
'''

CV["04_–_Funciones_vectoriales_de_variable_vectorial"] = '''
flowchart TD
  A["F: Rⁿ → Rᵐ"]:::k2
  A --> B["Jacobiano m×n"]:::k3
  A --> C["Derivada = mejor aproximación lineal"]:::k4
'''

CV["04_–_Propiedades_e_Interpretaciones_de_las_integrales_de_línea"] = '''
flowchart TD
  A["Propiedades integrales de línea"]:::k2
  A --> B["∫C (F+G)·dr = ∫C F·dr + ∫C G·dr"]:::k3
  A --> C["∫_{-C} F·dr = -∫C F·dr"]:::k4
  A --> D["Cambio de parametrización no afecta"]:::k5
'''

CV["04_–_Regiones_en_integrales_dobles"] = '''
flowchart TD
  A["Regiones en integrales dobles"]:::k2
  A --> B["Tipo I: a≤x≤b, g₁(x)≤y≤g₂(x)"]:::k3
  A --> C["Tipo II: c≤y≤d, h₁(y)≤x≤h₂(y)"]:::k4
'''

CV["04_–_Teorema_del_valor_medio_para_integrales_dobles"] = '''
flowchart TD
  A["Valor medio para integrales dobles"]:::k2
  A --> B["f_prom = (1/A(R)) ∬_R f dA"]:::k3
  A --> C["A(R): área de la región"]:::k4
'''

# --- Unidad 5: Línea e Integrales Dobles ---

CV["05_-_Funciones_compuestas"] = '''
flowchart TD
  A["Funciones compuestas z = f(g(t))"]:::k2
  A --> B["dz/dt = f'(g(t)) · g'(t)"]:::k3
  A --> C["Regla de la cadena multivariable"]:::k4
'''

CV["05_–_Integrales_iteradas"] = '''
flowchart TD
  A["Integrales iteradas"]:::k2
  A --> B["∫_a^b (∫_{g₁(x)}^{g₂(x)} f dy) dx"]:::k3
  A --> C["Integrar por la variable interior primero"]:::k4
'''

CV["05_–_Teorema_Fundamental_de_las_Integrales_de_Línea"] = '''
flowchart TD
  A["∫_C ∇f · dr = f(B) - f(A)"]:::k2
  A --> B["Campo conservativo"]:::k3
  A --> C["Independiente de la ruta"]:::k4
'''

CV["05_–_Valor_promedio_de_una_función"] = '''
flowchart TD
  A["Valor promedio f_prom"]:::k2
  A --> B["f_prom = (1/A(R)) ∬_R f dA"]:::k3
  A --> C["o (1/V(E)) ∭_E f dV"]:::k4
'''

# --- Unidad 6: Integrales Triples y Teoremas ---

CV["06_–_Cambio_de_orden_de_integración"] = '''
flowchart TD
  A["Cambio de orden de integración"]:::k2
  A --> B["Dibujar la región E"]:::k3
  A --> C["Identificar límites como funciones"]:::k4
  A --> D["Reescribir integral con nuevo orden"]:::k5
'''

CV["07_–_Propiedades_de_las_integrales_dobles"] = '''
flowchart TD
  A["Propiedades integrales dobles"]:::k2
  A --> B["Linealidad y aditividad"]:::k3
  A --> C["Acotación y comparación"]:::k4
  A --> D["Cambio de orden (Fubini)"]:::k5
'''

CV["Bienvenida_y_Syllabus_Calculo_Vectorial"] = '''
flowchart TD
  A["Cálculo Vectorial"]:::k2
  A --> B["Unidad 1: Geometría en R³"]:::k3
  A --> C["Unidad 2: Superficies y coordenadas"]:::k4
  A --> D["Unidad 3: Funciones de varias variables"]:::k5
  A --> E["Unidad 4: Optimización"]:::k1
  A --> F["Unidad 5: Integrales dobles"]:::k1
  A --> G["Unidad 6: Integrales triples y teoremas"]:::k1
'''

# ---------------------------------------------------------------
def main():
    targets = list(CV.keys())
    mmdc = shutil.which("mmdc") or shutil.which("mmdc.cmd") or r"C:\Users\Steven Sànchez\AppData\Roaming\npm\mmdc.cmd"
    print("mmdc:", mmdc, flush=True)
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
            print("RUN FAIL", name, e, flush=True)
            fail += 1
            continue
        if os.path.isfile(out_svg) and os.path.isfile(out_png):
            ok += 1
            print("OK  ", name, flush=True)
        else:
            fail += 1
            print("FAIL", name, flush=True)
    print("FINAL: OK=%d fail=%d de %d" % (ok, fail, len(targets)), flush=True)

main()

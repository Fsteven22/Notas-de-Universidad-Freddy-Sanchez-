# -*- coding: utf-8 -*-
import os, sys, json, shutil
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib

TMP = os.path.dirname(os.path.abspath(__file__))
MMDDIR = os.path.join(TMP, "mmd2", "fis")
PREV = os.path.join(TMP, "previews", "fis")
VAULT_DIAG = os.path.join(vlib.materia("1er", "F"), "Diagramas")
os.makedirs(MMDDIR, exist_ok=True)
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

F = {}

F["Problemas_de_Cuerpos_Rígidos_en_Sistemas_con_Poleas_01"] = '''
flowchart TD
  A["Polea con masa colgante<br/>y masa en plano inclinado"]:::k2
  A --> B["Traslacional · ΣF = ma"]:::k3
  B --> B1["Masa colgante: mg − T = ma"]:::k3
  B --> B2["Plano inclinado: mg sinθ − T − f = ma"]:::k3
  A --> C["Rotacional · Στ = I α"]:::k4
  C --> C1["T₁ R − T₂ R = I α"]:::k4
  B2 --> C1
  C1 --> C2["Restricción: a = α R<br/>la cuerda no se estira"]:::k1
  A --> D["Tipo de cuerda"]:::k6
  D --> D1["Ideal: masa nula → T₁ = T₂"]:::k1
  D --> D2["Masiva: participa del sistema<br/>→ T₁ ≠ T₂"]:::k6
  C2 --> E["Alternativa: conservación<br/>mgh + ½mv² + ½Iω² = constante"]:::k5
'''

F["Problemas_de_Cálculo_de_Momento_de_Inercia_01"] = '''
flowchart TD
  A["Momento de inercia<br/>I = Σ mᵢ rᵢ² = ∫ r² dm"]:::k2
  A --> B["Tipos de problemas"]:::k3
  B --> B1["Eje fijo: la distancia<br/>al eje no cambia"]:::k3
  B --> B2["Múltiples componentes:<br/>sumar I de cada pieza"]:::k3
  B --> B3["Geometría compleja:<br/>partir en formas básicas"]:::k3
  B --> B4["Ejes inclinados:<br/>descomposición tensorial"]:::k3
  A --> C["Ejemplo: placa en L"]:::k4
  C --> C1["Horizontal 0.6 × 0.2 m, 2 kg<br/>CM en (0.3, 0)"]:::k4
  C --> C2["Vertical 0.2 × 0.4 m, 1 kg<br/>CM en (0.1, 0.2)"]:::k4
  C1 --> C3["I = Σ (I_CM + M d²)"]:::k1
  C2 --> C3
  C3 --> C4["Sumar aportes y comparar<br/>con el eje de la esquina"]:::k1
'''

F["Problemas_de_Deformación_por_Cortante_(Esfuerzo_Cortante)_01"] = '''
flowchart TD
  A["Esfuerzo cortante<br/>τ = V / A"]:::k2
  A --> B["Orígenes del cortante"]:::k3
  B --> B1["Empernado y soldaduras:<br/>τ = V/A en planos de corte"]:::k3
  B --> B2["Torsión: τ = T r / J<br/>máximo en el perímetro"]:::k4
  B --> B3["Flexión: τ = V Q / (I b)<br/>distribución parabólica"]:::k4
  A --> C["Estados de cortante"]:::k1
  C --> C1["Puro: solo τ"]:::k1
  C --> C2["Combinado: τ + σ normales"]:::k1
  C --> C3["Máximo: τ = (σ1 − σ3)/2"]:::k6
  A --> D["Rigidez G típica"]:::k5
  D --> D1["Acero 80–85 GPa · Aluminio 26–28<br/>Concreto 8–15 · Caucho ~0.003"]:::k5
'''

F["Problemas_de_Deformación_por_Tensión_y_Compresión_(Ley_de_Hooke)_01"] = '''
flowchart TD
  A["σ = E · ε<br/>Ley de Hooke"]:::k2
  A --> B["Regiones de comportamiento"]:::k3
  B --> B1["Elástica: recupera la forma<br/>σ ≤ σe"]:::k1
  B --> B2["Plástica: cambio permanente<br/>σ mayor que σe"]:::k6
  A --> C["Tipos de carga"]:::k4
  C --> C1["Tracción: σ + las secciones se alejan"]:::k4
  C --> C2["Compresión: σ − las secciones se acercan"]:::k4
  C --> C3["Flexión: tracción + compresión juntas"]:::k4
  C --> C4["Torsión: necesita módulo G"]:::k4
  A --> D["Datos típicos"]:::k5
  D --> D1["Acero E ≈ 200 GPa · Aluminio 70<br/>Concreto 20–40 · Madera 10–15"]:::k5
  B1 --> E["Método DEMAT:<br/>datos → σ = F/A → ε = σ/E → ΔL = ε L₀"]:::k3
'''

F["Problemas_de_Ecuación_de_Bernoulli_01"] = '''
flowchart TD
  A["Bernoulli<br/>P + ½ρv² + ρgh = constante"]:::k2
  A --> B["Cuándo NO aplicar"]:::k6
  B --> B1["Viscosidad significativa"]:::k6
  B --> B2["Compresible M grande que 0.3"]:::k6
  B --> B3["Flujo no estacionario"]:::k6
  B --> B4["Bombas, turbinas o<br/>fricción grande"]:::k6
  A --> C["Correcciones"]:::k4
  C --> C1["+ H pérdidas por fricción"]:::k4
  C --> C2["+ / − H bomba o turbina"]:::k4
  C --> C3["Cd en orificios · α corrige<br/>la energía cinética"]:::k4
  A --> D["Método PEACE"]:::k1
  D --> D1["Puntos · Energía · Asumir ·<br/>Calcular · Evaluar"]:::k1
  D --> E["Instrumentos: Torricelli v = √(2gh) ·<br/>Venturímetro · Tubo de Pitot"]:::k5
'''

F["Problemas_de_Ecuación_de_Bernoulli_02"] = '''
flowchart TD
  A["Torricelli<br/>v = √(2gh)"]:::k2
  A --> B["Variaciones"]:::k3
  B --> B1["Presión extra: v = √(2gh + 2ΔP/ρ)<br/>tanque presurizado"]:::k3
  B --> B2["Orificio sumergido:<br/>v = √(2g(h₁ − h₂))"]:::k3
  B --> B3["Pared inclinada:<br/>v = √(2g h cos²α)"]:::k3
  A --> C["Derivadas útiles"]:::k5
  C --> C1["Tiempo de vaciado:<br/>t = (2 A_t / A_o) √(h₀ / 2g)"]:::k5
  C --> C2["Alcance horizontal:<br/>x = 2 √(h_orificio · h_líquido)"]:::k5
  C --> C3["Caudal instantáneo:<br/>Q(t) = Cd · A · √(2g h(t))"]:::k5
  C1 --> D["Verificar unidades y<br/>altura de referencia"]:::k6
  C2 --> D
  C3 --> D
'''

F["Problemas_de_Ecuación_de_Continuidad_01"] = '''
flowchart TD
  A["Continuidad<br/>Q = A₁ v₁ = A₂ v₂"]:::k2
  A --> B["Circulares: Q = π/4 · D² v"]:::k3
  A --> C["Relación de velocidades:<br/>v₂/v₁ = A₁/A₂ = (D₁/D₂)²"]:::k3
  A --> D["Caudal másico:<br/>ṁ = ρ A v · kg/s"]:::k1
  A --> E["Aplicaciones típicas"]:::k4
  E --> E1["Boquillas aceleran · difusores frenan<br/>venturímetros miden · ramas reparten"]:::k4
  E --> E2["Cavitación: presión baja en secciones estrechas<br/>turbulencia en cambios bruscos"]:::k6
  E --> F["Método CAVE"]:::k5
  F --> F1["Caudal - Área - Velocidad -<br/>Evaluar con los datos del punto"]:::k5
'''

F["Problemas_de_Ecuación_de_Continuidad_02"] = '''
flowchart TD
  A["Tubo de Venturi"]:::k2
  A --> B["Sección 1: ancha · v₁ lenta · P₁ alta"]:::k1
  A --> C["Garganta: estrecha · v₂ = 1/β² · P₂ baja"]:::k1
  C --> C1["β = A₂/A₁"]:::k1
  A --> D["Sobremedida · bocal · placa orificio"]:::k3
  D --> D1["Venturi: baja pérdida · alta precisión"]:::k1
  D --> D2["Tobera: solo converge · más pérdida"]:::k3
  D --> D3["Placa: restricción abrupta · económica"]:::k3
  A --> E["ΔP = P₁ − P₂ = (ρ v₁²/2)(β⁻⁴ − 1)"]:::k4
  E --> F["Pérdida permanente:<br/>(1 − Cd²)(P₁ − P₂)"]:::k4
  A --> G["Límites: β 0.2 a 0.75 ·<br/>Re mayor que 2×10⁴ · P₂ encima de P vapor"]:::k5
'''

F["Problemas_de_Encuentro_01"] = '''
flowchart TD
  A["Encuentro frontal<br/>dos móviles se acercan"]:::k2
  B["Móvil 1: x₁(t) = x₀₁ + v₁ t"]:::k3
  B --> A
  C["Móvil 2: x₂(t) = d₀ − v₂ t"]:::k4
  C --> A
  A --> D["Condición x₁ = x₂"]:::k1
  D --> E["t = d₀ / (v₁ + v₂)"]:::k4
  E --> F["Posición: x_enc = v₁ · t desde origen 1"]:::k1
  A --> G["Velocidad relativa de cierre:<br/>v₁ + v₂"]:::k5
  G --> H["Ejemplos: autos en sentidos opuestos ·<br/>trenes de estaciones distintas"]:::k5
'''

F["Problemas_de_Encuentro_02"] = '''
flowchart TD
  A["Alcance · persecución<br/>mismo sentido"]:::k2
  B["Objetivo con ventaja:<br/>x_obj = d₀ + v_obj t"]:::k3
  B --> A
  C["Perseguidor más rápido: v_per mayor que v_obj"]:::k4
  C --> A
  A --> D["Velocidad relativa de cierre:<br/>v_per − v_obj"]:::k1
  D --> E["Exige v_per mayor que v_obj<br/>si no, nunca alcanza"]:::k6
  E --> F["Condición: x_per(t) = x_obj(t)"]:::k1
  F --> G["Ejemplos: policía y ladrón ·<br/>depredador y presa · auto y auto lento"]:::k5
'''

F["Problemas_de_Encuentro_03"] = '''
flowchart TD
  A["Gráfica x - t del encuentro"]:::k2
  A --> B["Recta del móvil 1:<br/>pendiente = v₁"]:::k1
  A --> C["Recta del móvil 2:<br/>pendiente = v₂ (negativa si viene al encuentro)"]:::k4
  B --> D["Intersección:<br/>momento y lugar del encuentro"]:::k3
  C --> D
  D --> E["Ordenada del cruce:<br/>posición común x_enc"]:::k3
  D --> F["Pendiente más inclinada:<br/>el móvil más rápido"]:::k5
  D --> G["Área bajo la curva v-t:<br/>desplazamiento de cada móvil"]:::k5
'''

F["Problemas_de_Energía_Elástica_01"] = '''
flowchart TD
  A["Energía potencial elástica<br/>U = ½ k x²"]:::k2
  A --> B["Elementos estructurales"]:::k3
  B --> B1["Barra en tracción:<br/>U = F² L / (2 E A)"]:::k1
  B --> B2["Viga en flexión:<br/>U = M² L / (2 E I)"]:::k4
  B --> B3["Eje en torsión:<br/>U = T² L / (2 G J)"]:::k4
  A --> C["Resortes"]:::k4
  C --> C1["Lineal: U = ½ k x²"]:::k4
  C --> C2["Torsional: U = ½ k θ²"]:::k4
  A --> D["Densidad de energía<br/>u = U/V"]:::k5
  D --> D1["u = σ²/(2E) = ½ σ ε"]:::k5
  D --> D2["Unidades J/m³<br/>máximo en el límite elástico"]:::k5
  B --> E["Método: derivar el campo de<br/>esfuerzos U = ∫ u dV"]:::k6
'''

F["Problemas_de_Engranajes,_Poleas_y_Transmisión_de_Movimiento_01"] = '''
flowchart TD
  A["Transmisión de movimiento"]:::k2
  A --> B["Piñón motor → cadena → piñón conducido"]:::k3
  B --> C["Sin deslizamiento: v₁ = v₂<br/>en el contacto"]:::k1
  C --> D["Relación de transmisión:<br/>i = ω₁/ω₂ = N₂/N₁ = D₂/D₁"]:::k4
  D --> E["Torques: T₂/T₁ = N₂/N₁ = i<br/>conserva potencia P₁ = P₂"]:::k4
  A --> F["Poleas con correa"]:::k3
  F --> F1["D₁ ω₁ = D₂ ω₂"]:::k1
  F --> F2["Ventaja mecánica: VM = F_carga / F_esfuerzo"]:::k5
  F --> F3["Eficiencia: η = útil / suministrada"]:::k5
  D --> G["Aplicaciones: bicicletas ·<br/>maquinaria · motores"]:::k5
'''

F["Problemas_de_Equilibrio_Traslacional_y_Rotacional_01"] = '''
flowchart TD
  A["Equilibrio simultáneo"]:::k2
  A --> B["ΣF = 0 traslacional"]:::k1
  A --> C["Στ = 0 rotacional"]:::k1
  B --> D["Tipos de equilibrio"]:::k3
  D --> D1["Estable: regresa al punto<br/>CG bajo"]:::k1
  D --> D2["Inestable: se aleja<br/>CG sobre el borde"]:::k6
  D --> D3["Neutro: U no cambia<br/>rodillo o esfera"]:::k3
  C --> E["Elegir eje en fuerza<br/>desconocida: su τ = 0"]:::k4
  A --> F["Apoyos"]:::k7
  F --> F1["Rodillo: 1 reacción perpendicular"]:::k7
  F --> F2["Pasador: 2 reacciones H y V"]:::k7
  F --> F3["Empotramiento: 2 fuerzas + momento"]:::k7
'''

F["Problemas_de_Estabilidad_01"] = '''
flowchart TD
  A["Estabilidad de equilibrio"]:::k2
  A --> B["Claves del CG"]:::k3
  B --> B1["Proyección del CG dentro<br/>de la base → estable"]:::k1
  B --> B2["Proyección sale del borde<br/>→ vuelco"]:::k6
  B --> B3["CG constante en altura<br/>→ neutro (rodillo)"]:::k3
  A --> C["Vuelco inminente"]:::k4
  C --> C1["Línea de acción del peso<br/>pasa por el borde de la base"]:::k4
  C --> C2["M vuelco = M estabilizador"]:::k4
  C --> C3["Método del punto de vuelco:<br/>igualar momentos respecto del borde"]:::k4
  A --> D["También afecta<br/>deslizamiento"]:::k6
  D --> D1["Fricción insuficiente<br/>la masa desliza antes de volcar"]:::k6
  A --> E["Factores: base más ancha ·<br/>CG más bajo · carga segura"]:::k1
'''

F["Problemas_de_Flotabilidad_y_Empuje_en_Fluidos_en_Movimiento_01"] = '''
flowchart TD
  A["Cuerpo en fluido<br/>en movimiento"]:::k2
  A --> B["Empuje: b = ρ_fluido · V_sumergido · g"]:::k1
  A --> C["Resistencia: F_d = ½ ρ v² C_d A<br/>opuesta a v relativa"]:::k4
  C --> C1["Esfera C_d ≈ 0.47 · cilindro 1.2<br/>placa 1.3 · hidrodinámica 0.04 a 0.1"]:::k4
  C --> C2["Re menor que 1: Ley de Stokes<br/>C_d = 24 / Re"]:::k5
  A --> D["Equilibrio de fuerzas"]:::k3
  D --> D1["Vertical: empuje + corriente − W"]:::k3
  D --> D2["Horizontal: propulsión − resistencia"]:::k3
  D1 --> E["Velocidad terminal:<br/>v_t = √(2 m g / (ρ A C_d))"]:::k1
  D2 --> E
  E --> F["Método MAREA:<br/>masas · Arquímedes · resistencia ·<br/>equilibrio · análisis"]:::k5
'''

F["Problemas_de_Flujo_con_Viscosidad_(Poiseuille)_01"] = '''
flowchart TD
  A["Poiseuille<br/>Q = π R⁴ ΔP / (8 μ L)"]:::k2
  A --> B["Número de Reynolds<br/>Re = ρ v D / μ"]:::k3
  B --> B1["Re menor que 2100: laminar<br/>válido Poiseuille"]:::k1
  B --> B2["2100 a 4000: transición"]:::k5
  B --> B3["Re mayor que 4000: turbulento<br/>NO vale Poiseuille"]:::k6
  A --> C["Resistencia hidráulica:<br/>R_h = 8 μ L / (π R⁴)"]:::k4
  C --> C1["Ley de Ohm fluida:<br/>ΔP = R_h · Q"]:::k4
  C --> C2["Serie: R total = Σ Rᵢ<br/>Paralelo: 1/R total = Σ 1/Rᵢ"]:::k4
  C1 --> D["Método VAPOR:<br/>viscosidad · área · presión ·<br/>Ohm · Reynolds"]:::k5
  B1 --> E["Pérdidas: ∝ v en laminar<br/>∝ v² en turbulento"]:::k3
  B3 --> E
'''

F["Problemas_de_Gráficos_(x-t,_v-t,_a-t)_01"] = '''
flowchart TD
  A["Relación entre gráficos<br/>x-t · v-t · a-t"]:::k2
  A --> B["Hacia abajo: derivadas"]:::k3
  B --> B1["v = dx/dt<br/>pendiente del gráfico x-t"]:::k1
  B --> B2["a = dv/dt<br/>pendiente del gráfico v-t"]:::k1
  A --> C["Hacia arriba: integrales"]:::k4
  C --> C1["Δx = ∫ v dt<br/>área del gráfico v-t"]:::k3
  C --> C2["Δv = ∫ a dt<br/>área del gráfico a-t"]:::k3
  A --> D["Lectura rápida"]:::k5
  D --> D1["x-t con curva cuadrática:<br/>a constante"]:::k5
  D --> D2["v-t horizontal: MRU"]:::k5
  D --> D3["a-t con tramos:<br/>cambia la aceleración"]:::k5
'''

F["Problemas_de_Leyes_de_Newton_con_fuerzas_no_constantes_01"] = '''
flowchart TD
  A["m a = F puede tener<br/>F no constante"]:::k2
  A --> B["Resistencia lineal<br/>F = − b v"]:::k3
  B --> B1["Fluidos viscosos · Stokes<br/>v terminal = m g / b"]:::k3
  A --> C["Resistencia cuadrática<br/>F = − c v²"]:::k4
  C --> C1["Altas velocidades · turbulencia<br/>v terminal = √(m g / c)"]:::k4
  A --> D["Método según dependencia"]:::k7
  D --> D1["F(t): integrar dos veces<br/>x(t) con x₀ y v₀"]:::k7
  D --> D2["F(x): m v dv/dx = F(x)<br/>∫ m v dv = ∫ F dx"]:::k7
  D --> D3["F(v): dv/F(v) = dt/m<br/>separar variables"]:::k7
  D --> E["Terminal: cuando a = 0<br/>peso equilibra resistencia"]:::k6
'''

F["Problemas_de_Límite_Elástico_y_Resistencia_01"] = '''
flowchart TD
  A["Curva esfuerzo - deformación<br/>σ vs ε"]:::k2
  A --> B["Zonas"]:::k3
  B --> B1["Elástica: σ = E ε<br/>lineal y recuperable"]:::k1
  B --> B2["Fluencia: σe · crece sin<br/>mucha deformación extra"]:::k5
  B --> B3["Endurecimiento: hasta σu<br/>máxima resistencia"]:::k4
  B --> B4["Ruptura: falla del material"]:::k6
  A --> C["Factor de seguridad<br/>FS = σ material / σ trabajo"]:::k4
  C --> C1["Estructuras críticas: FS 3 a 5"]:::k1
  C --> C2["Normales: FS 2 a 3"]:::k1
  C --> C3["Temporales: FS 1.5 a 2"]:::k1
  C --> D["FS menor que 1 → falla inmediata"]:::k6
  C --> E["Método SERF: seguridad ·<br/>esfuerzo · resistencia · factor"]:::k5
'''

F["Problemas_de_Persecución_01"] = '''
flowchart TD
  A["Persecución clásica<br/>velocidades constantes"]:::k2
  B["Objetivo: ventaja d₀<br/>x_obj = d₀ + v_obj t"]:::k3
  B --> A
  C["Perseguidor: x_per = v_per t<br/>v_per mayor que v_obj"]:::k4
  C --> A
  A --> D["Alcance: x_per = x_obj"]:::k1
  D --> E["(v_per − v_obj) t = d₀"]:::k1
  E --> F["t = d₀ / (v_per − v_obj)"]:::k4
  F --> G["Posición del alcance:<br/>x = v_per · t"]:::k1
  A --> H["Comparar velocidades relativas<br/>y revisar si t es positivo"]:::k5
'''

F["Problemas_de_Persecución_02"] = '''
flowchart TD
  A["Persecución con aceleración<br/>partir del reposo"]:::k2
  B["Objetivo: velocidad constante<br/>x_obj = d₀ + v t"]:::k3
  B --> A
  C["Perseguidor: acelera desde reposo<br/>x_per = ½ a t²"]:::k4
  C --> A
  A --> D["Alcanzar: ½ a t² = d₀ + v t"]:::k1
  D --> E["½ a t² − v t − d₀ = 0"]:::k1
  E --> F["Solución cuadrática:<br/>t = (v + √(v² + 2 a d₀)) / a"]:::k4
  F --> G["Descartar la raíz negativa<br/>elegimos el tiempo positivo"]:::k6
  G --> H["Posición de alcance<br/>x = d₀ + v t"]:::k1
'''

F["Problemas_de_Persecución_03"] = '''
flowchart TD
  A["Alcance con retardo<br/>mismo punto de partida"]:::k2
  B["Bus lento: sale a t = 0<br/>x_bus = v₁ t"]:::k3
  B --> A
  C["Auto rápido: sale τ después<br/>x_auto = v₂ (t − τ)"]:::k4
  C --> A
  A --> D["Ventaja temporal τ del lento"]:::k5
  D --> E["v₂ (t − τ) = v₁ t"]:::k1
  E --> F["t = v₂ τ / (v₂ − v₁)"]:::k4
  F --> G["Posición: x = v₁ · t"]:::k1
  F --> H["Ejemplo: bus 60 auto 90 τ = 1/6 h<br/>t = 0.5 h · x = 30 km desde la estación"]:::k5
'''

F["Problemas_de_Persecución_04"] = '''
flowchart TD
  A["Gráfica x - t de alcance"]:::k2
  A --> B["Recta del bus:<br/>pendiente 60 km/h"]:::k1
  A --> C["Recta del auto:<br/>sale τ después<br/>pendiente 90 km/h"]:::k4
  B --> D["Cruce en t = 0.5 h<br/>x = 30 km"]:::k3
  C --> D
  D --> E["Pendiente mayor →<br/>velocidad mayor"]:::k5
  D --> F["Parábola en x-t:<br/>aceleración constante"]:::k5
  D --> G["Punto de intersección:<br/>momento y lugar del alcance"]:::k3
'''

F["Problemas_de_Planos_Inclinados_01"] = '''
flowchart TD
  A["Objeto en plano inclinado<br/>ángulo θ"]:::k2
  A --> B["Descomposición del peso"]:::k3
  B --> B1["W sinθ a lo largo del plano<br/>fuerza que desliza"]:::k1
  B --> B2["W cosθ perpendicular ·<br/>la normal N = W cosθ"]:::k1
  B --> A
  A --> C["Fricción"]:::k4
  C --> C1["f = μ N = μ W cosθ"]:::k4
  C --> C2["Subida a g (sinθ + μ cosθ)<br/>baja a g (sinθ − μ cosθ)"]:::k4
  A --> D["Ángulo crítico:<br/>θc = arctan(μs)"]:::k6
  D --> D1["θ menor que θc: reposo<br/>θ mayor que θc: desliza"]:::k6
  A --> E["Geometría: h = L sinθ<br/>d = L cosθ"]:::k3
  E --> F["Sistemas conectados:<br/>DCL por objeto · tensión común ·<br/>misma aceleración"]:::k5
'''

F["Problemas_de_Presión_en_un_Fluido_01"] = '''
flowchart TD
  A["Presión hidrostática<br/>P = P₀ + ρ g h"]:::k2
  A --> B["Gradiente dP/dh = ρ g"]:::k3
  B --> B1["Cada 100 m de agua<br/>+1 MPa aprox"]:::k3
  A --> C["Fluido estratificado:<br/>P = P₀ + ∫ ρ(z) g dz"]:::k4
  A --> D["Equivalencias"]:::k5
  D --> D1["Altura columna: h = P / (ρ g)"]:::k5
  D --> D2["Atmósfera: 101325 Pa<br/>= 10.33 m de agua"]:::k5
  A --> E["Densidades de referencia"]:::k7
  E --> E1["Agua 1000 · mar 1025<br/>mercurio 13600 · aceite 900 kg/m³"]:::k7
  E --> E2["Mercurio 13.6 veces más denso<br/>que el agua"]:::k7
'''

F["Problemas_de_Presión_y_Fuerza_sobre_Superficies_01"] = '''
flowchart TD
  A["Fuerza sobre superficie"]:::k2
  A --> B["Horizontal"]:::k3
  B --> B1["Presión uniforme<br/>F = ρ g h · A"]:::k1
  B --> B2["Punto de aplicación:<br/>centro geométrico"]:::k1
  A --> C["Vertical"]:::k3
  C --> C1["Presión variable P(y) = ρ g (h₀ + y)<br/>F = ρ g h̄ · A"]:::k4
  C --> C2["Al integrar: F = ρ g h_c · A<br/>h_c = profundidad del centroide"]:::k4
  C --> C3["Centro de presión:<br/>h_cp = h_c + I_c / (h_c A)"]:::k4
  C3 --> D["h cp siempre debajo del centroide"]:::k6
  A --> E["Inclinada"]:::k3
  E --> E1["Componente normal<br/>F_n = ρ g h̄ A"]:::k5
  E --> E2["Mismo h_cp con I_c inclinada"]:::k5
'''

F["Problemas_de_Revoluciones,_Ángulos_y_Tiempo_01"] = '''
flowchart TD
  A["Cinemática angular"]:::k2
  A --> B["Ecuaciones con α constante"]:::k3
  B --> B1["ω = ω₀ + α t"]:::k1
  B --> B2["θ = θ₀ + ω₀ t + ½ α t²"]:::k1
  B --> B3["ω² = ω₀² + 2 α Δθ"]:::k1
  A --> C["Conversión revoluciones<br/>1 rev = 2π rad"]:::k4
  C --> C1["Revoluciones por minuto:<br/>rad/s = RPM · 2π/60"]:::k4
  A --> D["Relaciones con el arco"]:::k5
  D --> D1["s = r θ · v = r ω"]:::k5
  D --> D2["a tangencial = r α"]:::k5
  D --> D3["a centrípeta = r ω²"]:::k5
  A --> E["Periódicas: T = 2π/ω = 1/f<br/>f = ω / 2π"]:::k7
'''

F["Problemas_de_Rodadura_sin_deslizamiento_01"] = '''
flowchart TD
  A["Rodadura pura"]:::k2
  A --> B["Condición de contacto<br/>v_CM = ω R · a_CM = α R"]:::k1
  A --> C["Factor β = I / M R²"]:::k3
  C --> C1["Cilindro sólido β = 1/2"]:::k1
  C --> C2["Esfera sólida β = 2/5"]:::k1
  C --> C3["Cilindro hueco β = 1"]:::k3
  C --> C4["Esfera hueca β = 2/3"]:::k3
  C --> D["Energía total<br/>E_k = ½ M v² (1 + β)"]:::k4
  D --> E["Plano inclinado:<br/>a_CM = g sinθ / (1 + β)"]:::k4
  D --> F["Separar traslacional de rotacional"]:::k6
  A --> G["Incluir torque de la fricción<br/>en Στ = I α respecto al CM"]:::k5
'''

F["Problemas_de_Tiempo-Distancia_01"] = '''
flowchart TD
  A["Viaje por tramos<br/>datos completos"]:::k2
  A --> B["Tabular por tramo"]:::k3
  B --> B1["Columnas: dᵢ · vᵢ · tᵢ"]:::k3
  B --> B2["Faltante: aplicar d = v t"]:::k3
  B1 --> C["Sumas"]:::k4
  C --> C1["d total = Σ dᵢ"]:::k4
  C --> C2["t total = Σ tᵢ"]:::k4
  C1 --> D["Velocidad media:<br/>v̄ = d total / t total"]:::k1
  C2 --> D
  D --> E["No promediar velocidades<br/>a mano: depende de tiempos"]:::k6
  D --> F["Casos: viaje con límites distintos ·<br/>tramos urbanos y rurales"]:::k5
'''

F["Problemas_de_Tiempo-Distancia_02"] = '''
flowchart TD
  A["Gráfico v - t por tramos"]:::k2
  A --> B["Cada barra: velocidad del tramo<br/>ancho = tiempo del tramo"]:::k3
  B --> C["Área de cada barra<br/>= distancia dᵢ = vᵢ tᵢ"]:::k1
  C --> D["Área total<br/>= distancia del viaje"]:::k1
  D --> E["Ejemplo 90 y 60 km/h<br/>mismas distancias"]:::k4
  E --> F["Media armónica:<br/>v̄ = 2 v₁ v₂ / (v₁ + v₂) = 72 km/h"]:::k4
  F --> G["NO es el promedio simple<br/>(90 + 60)/2 = 75: tiempos distintos"]:::k6
  E --> H["Barra ancha con v bajo<br/>puede pesar más en el total"]:::k5
'''

F["Problemas_de_Torque_01"] = '''
flowchart TD
  A["Cálculo del torque<br/>τ = F r sinθ"]:::k2
  A --> B["Método 1: componente útil<br/>F⊥ = F sinθ · τ = F⊥ r"]:::k3
  A --> C["Método 2: brazo efectivo<br/>d = r sinθ · τ = F d"]:::k3
  B --> D["F tangencial contribuye<br/>F radial no aporta torque"]:::k4
  B --> E["Casos límite"]:::k5
  E --> E1["θ = 90°: τ máximo = F r"]:::k1
  E --> E2["θ = 0° o 180°: τ = 0"]:::k6
  D --> F["Error típico: multiplicar<br/>la fuerza completa en vez<br/>del componente útil"]:::k6
'''

F["Problemas_de_Trabajo_01"] = '''
flowchart TD
  A["Trabajo y ángulo<br/>W = F d cosθ"]:::k2
  A --> B["θ = 0°: W = + F d<br/>mismo sentido del movimiento"]:::k1
  A --> C["0° menor que θ menor que 90°: W positivo · motor"]:::k1
  A --> D["θ = 90°: W = 0<br/>perpendicular no trabaja"]:::k3
  A --> E["90° menor que θ menor que 180°: W negativo · resistivo"]:::k6
  A --> F["θ = 180°: W = − F d"]:::k6
  A --> G["Teorema trabajo - energía<br/>W total = ΔE cinética"]:::k4
  G --> G1["W sumado menor que 0: frena<br/>0: velocidad constante"]:::k4
  G --> G2["W neto = Σ trabajos de<br/>cada fuerza"]:::k4
'''

F["Problemas_de_Variación_de_Momentum_en_Sistemas_Aislados_01"] = '''
flowchart TD
  A["Momentum en sistema aislado<br/>p = conservado"]:::k2
  A --> B["p antes = p después"]:::k1
  A --> C["Explosión"]:::k4
  C --> C1["Una parte se separa<br/>con fuerzas internas"]:::k4
  C --> C2["p total igual<br/>pero energía cinética ↑"]:::k4
  A --> D["Coalescencia"]:::k4
  D --> D1["Objetos se pegan<br/>p total igual"]:::k4
  D --> D2["Energía cinética ↓ se pierde"]:::k4
  B --> E["Restitución:<br/>e = −(v₂f − v₁f)/(v₂i − v₁i)"]:::k5
  E --> E1["e = 1 elástica · e = 0 pegada<br/>0 menor que e menor que 1 inelástica"]:::k5
  A --> F["Método SICE:<br/>sistema · inicial · conservación · ecuaciones"]:::k3
'''

F["Problemas_de_Velocidad_Final_usando_Impulso_01"] = '''
flowchart TD
  A["Impulso - momentum<br/>J = ∫ F dt = Δp"]:::k2
  A --> B["Calcular J"]:::k3
  B --> B1["F constante: J = F Δt"]:::k3
  B --> B2["F(t) conocida: integrar"]:::k3
  B --> B3["Datos de gráfica o tabla:<br/>área o suma de bloques"]:::k3
  A --> C["Relación con velocidad:<br/>v final = v inicial + J/m"]:::k1
  A --> D["Sistemas interactivos:<br/>Σ p inicial = Σ p final"]:::k4
  D --> D1["Bordes de colisión<br/>propulsión · explosiones"]:::k4
  D --> D2["El impulso externo debe<br/>ser pequeño en el intervalo"]:::k6
  C --> E["Verificar unidades<br/>N·s = kg·m/s"]:::k5
'''

F["Práctica_de_Giroscopio_01"] = '''
flowchart TD
  A["Giroscopio en precesión"]:::k2
  A --> B["Torque del peso:<br/>τ = w r = m g r"]:::k3
  A --> C["Momentum angular<br/>L = I_G ω_G del disco"]:::k3
  B --> D["τ = dL/dt"]:::k1
  C --> D
  D --> E["Velocidad de precesión:<br/>Ω = τ / L = w r / (I_G ω_G)"]:::k4
  E --> F["El eje traza un semicírculo<br/>rotando uniforme"]:::k5
  A --> G["Materiales"]:::k7
  G --> G1["Giroscopio de 3 ejes<br/>contrapeso · masa 10 g"]:::k7
  G --> G2["Barrera de luz ±0.001 s<br/>cronómetro ±0.01 s"]:::k7
'''

F["Práctica_de_Giroscopio_02"] = '''
flowchart TD
  A["Fórmulas del reporte"]:::k2
  A --> B["ω G = 2π / T giro<br/>(media vuelta del disco)"]:::k3
  A --> C["Ω = π / T precesión<br/>(media vuelta del eje)"]:::k3
  A --> D["I G esp = m g r / (Ω ω_G)"]:::k4
  A --> E["ω G promedio =<br/>(ω final + ω inicial)/2"]:::k4
  A --> F["Incertidumbres"]:::k6
  F --> F1["Barrera de luz ±0.001 s<br/>cronómetro ±0.01 s"]:::k6
  F --> F2["Distancia ±0.05 cm<br/>masa ±0.01 g"]:::k6
  E --> G["Fricción del disco:<br/>T gira más al final"]:::k5
'''

F["Rodadura_01"] = '''
flowchart TD
  A["Método dinámico"]:::k2
  A --> B["1. Newton lineal<br/>ΣF = M a_CM"]:::k3
  A --> C["2. Newton rotacional<br/>τ total = I α"]:::k3
  A --> D["3. Rodar sin deslizar<br/>a_CM = α R"]:::k3
  B --> E["Ejemplo disco:<br/>F − f_s = M a · f_s R = ½ M R² α"]:::k4
  C --> E
  D --> E
  E --> F["a_CM = 2 F / 3M"]:::k1
  E --> G["f_s = F / 3"]:::k1
  A --> H["Buena cuando necesitas<br/>fuerzas o aceleraciones"]:::k5
'''

F["Rodadura_02"] = '''
flowchart TD
  A["Método energético"]:::k2
  A --> B["Energía inicial: M g h<br/>partiendo del reposo"]:::k3
  B --> C["Energía final:<br/>½ M v² + ½ I ω²"]:::k3
  B --> D["Rodar sin deslizar:<br/>ω = v / R"]:::k1
  C --> E["M g h = ½ M v² (1 + β)"]:::k1
  D --> E
  E --> F["v = √(2 g h / (1 + β))"]:::k4
  F --> G["Ejemplo cilindro β = 1/2:<br/>v = 2/3 · √(g h)"]:::k4
  A --> H["Útil cuando no hay<br/>fuerzas no conservativas<br/>y solo quieres velocidad"]:::k5
'''

F["Rodadura_03"] = '''
flowchart TD
  A["Carrera rodando<br/>misma masa y radio"]:::k2
  B["Disco: I = ½ M R²<br/>β = 1/2"]:::k3
  B --> C["v disco = √(4 g h / 3)"]:::k1
  D["Aro: I = M R² · β = 1"]:::k4
  D --> E["v aro = √(g h)"]:::k1
  A --> F["El disco llega primero<br/>más fracción en traslación"]:::k5
  A --> G["Orden de llegadas<br/>esfera · cilindro · aro"]:::k6
  A --> H["Energía en cada pieza:<br/>traslación + rotación"]:::k3
  E --> H
'''

F["Rodadura_04"] = '''
flowchart TD
  A["Dinámico vs energético"]:::k2
  A --> B["Dinámico"]:::k3
  B --> B1["Objetivo: fuerzas y aceleraciones"]:::k3
  B --> B2["3 ecuaciones simultáneas"]:::k3
  B --> B3["Análisis completo del movimiento"]:::k3
  A --> C["Energético"]:::k4
  C --> C1["Objetivo: velocidades y alturas"]:::k4
  C --> C2["1 ecuación de conservación"]:::k4
  C --> C3["Resultado final rápido"]:::k4
  D["Elegir: fuerzas → dinámico ·<br/>solo velocidades → energético"]:::k6
  B --> D
  C --> D
'''

F["Segunda_ley_de_Newton_para_Rotación_01"] = '''
flowchart TD
  A["τ neto = I α"]:::k2
  A --> B["Causa: torque neto"]:::k3
  A --> C["Efecto: aceleración angular"]:::k3
  A --> D["Resistencia: I momento de inercia"]:::k3
  B --> E["Mayor τ → mayor α<br/>proporcionalidad directa"]:::k1
  D --> F["Mayor I → menor α<br/para mismo τ"]:::k1
  D --> G["I es la masa rotacional:<br/>dificulta cambiar la rotación"]:::k4
  A --> H["Analogía con F = m a:<br/>τ · I · α juegan F · m · a"]:::k5
'''

F["Segunda_ley_de_Newton_para_Rotación_02"] = '''
flowchart TD
  A["Procedimiento rotacional"]:::k2
  A --> S1["1. Elegir eje de rotación"]:::k3
  S1 --> S2["2. DCL con todas<br/>las fuerzas"]:::k3
  S2 --> S3["3. Torques de cada fuerza:<br/>τ = r F sinθ"]:::k3
  S3 --> S4["4. Sumar torques<br/>con signo y aplicar τ = I α"]:::k4
  S4 --> R["Resolver para α<br/>o para la fuerza desconocida"]:::k1
  A --> U["Casos clásicos"]:::k5
  U --> U1["Volante: I grande frena cambios de ω"]:::k5
  U --> U2["Yo-yo: el peso da torque<br/>por la cuerda"]:::k5
  U --> U3["Rueda acelerando: torque motor<br/>menos fricción"]:::k5
'''

F["Tensión_Superficial_01"] = '''
flowchart TD
  A["Tensión superficial<br/>γ en N/m"]:::k2
  A --> B["Origen molecular"]:::k3
  B --> B1["Interior: fuerzas simétricas<br/>se equilibran"]:::k1
  B --> B2["Superficie: menos vecinos<br/>asimetría hacia adentro"]:::k4
  B --> A
  A --> C["Comportamiento como piel: fuerza<br/>por longitud = energía por área"]:::k4
  A --> D["Unidades: N/m = J/m²"]:::k5
  D --> D1["γ de agua ≈ 0.072 N/m ·<br/>con jabón baja"]:::k5
  A --> E["Efectos"]:::k1
  E --> E1["Insectos sobre el agua"]:::k1
  E --> E2["Gotas casi esféricas"]:::k1
  E --> E3["Capilaridad en tubos finos"]:::k1
'''

F["Teorema_de_los_Vasos_Comunicantes_01"] = '''
flowchart TD
  A["Vasos comunicantes"]:::k2
  A --> B["El líquido sube<br/>al mismo nivel en todos"]:::k1
  A --> C["Fundamento"]:::k3
  C --> C1["P es la misma en el mismo nivel"]:::k3
  C --> C2["P = P_atm + ρ g h<br/>igual de presiones en la base"]:::k3
  C1 --> D["Forma no importa: nivel<br/>depende solo de la altura"]:::k4
  A --> E["Líquidos inmiscibles"]:::k6
  E --> E1["ρ₁ h₁ = ρ₂ h₂ en la separación"]:::k6
  E --> E2["Denser abajo: alturas<br/>inversas a las densidades"]:::k6
'''

F["Teorema_de_los_Vasos_Comunicantes_02"] = '''
flowchart TD
  A["Vasos comunicantes<br/>aplicaciones"]:::k2
  A --> B["Cotidianas"]:::k3
  B --> B1["Riego uniforme · tanques nivelados<br/>cafetera · acueductos romanos"]:::k3
  A --> C["Ingeniería"]:::k4
  C --> C1["Nivelaciones de construcción"]:::k4
  C --> C2["Cerraje hidráulico"]:::k4
  A --> D["Experimento"]:::k5
  D --> D1["Tubos distintos diámetros<br/>unidos con manguera"]:::k5
  D --> D2["Verter agua: mismo nivel<br/>en todos los tubos"]:::k1
  A --> E["Condición: comunicación<br/>libre sin atrancos"]:::k6
'''

F["Torque_y_Equilibrio_Rotacional_01"] = '''
flowchart TD
  A["Factores del torque<br/>τ = r F sinθ"]:::k2
  A --> B["Fuerza F: mayor F<br/>mayor τ"]:::k1
  A --> C["Brazo r: mayor distancia<br/>del eje mayor τ"]:::k1
  A --> D["Ángulo θ"]:::k3
  D --> D1["θ = 90° torque máximo"]:::k1
  D --> D2["θ = 0 o 180 clásico torque nulo"]:::k6
  D --> D3["Componente radial<br/>no contribuye"]:::k4
  A --> E["Real"]:::k5
  E --> E1["Llave larga da más torque"]:::k5
  E --> E2["Puerta: empuja lejos<br/>de las bisagras"]:::k5
  E --> E3["Balanza: τ₁ = τ₂<br/>r₁ F₁ = r₂ F₂"]:::k5
'''

F["Torque_y_Equilibrio_Rotacional_02"] = '''
flowchart TD
  A["Flujo de resolución<br/>estática rotacional"]:::k2
  A --> S1["1. Elegir eje en fuerza<br/>desconocida: su τ = 0"]:::k3
  S1 --> S2["2. DCL con puntos de aplicación"]:::k3
  S2 --> S3["3. Torques por fuerza<br/>τ = r F sinθ + signo"]:::k4
  S3 --> S4["4. Σ τ = 0"]:::k4
  S4 --> S5["5. Cerrado con Σ F = 0"]:::k4
  S5 --> R["Resolver el sistema<br/>de reacciones"]:::k1
  A --> T["Signos: antihorario +<br/>horario − siendo consistente"]:::k5
'''

F["Torque_y_Equilibrio_Rotacional_03"] = '''
flowchart TD
  A["Ejemplo resuelto: llave"]:::k2
  A --> B["F = 50 N · r = 0.5 m · θ = 90°"]:::k3
  B --> C["τ = 0.5 · 50 · 1 = 25 N·m"]:::k1
  A --> D["Ejemplo puerta"]:::k4
  D --> D1["F = 10 N · r = 0.8 m"]:::k4
  D --> D2["Máximo: τ = 10 · 0.8 · sin90° = 8 N·m"]:::k1
  D --> D3["Si θ = 30°: τ = 10 · 0.8 · 0.5<br/>= 4 N·m · se pierde la mitad"]:::k6
  C --> E["Elección del eje simplifica<br/>el cálculo"]:::k5
'''

F["Torque_y_Equilibrio_Rotacional_04"] = '''
flowchart TD
  A["Viga apoyada en 2 soportes"]:::k2
  A --> B["Viga 20 kg de 4 m<br/>objeto 50 kg a 1 m del izquierdo"]:::k3
  B --> E["Eje en soporte izquierdo"]:::k3
  E --> E1["F₁ no aporta τ r = 0"]:::k5
  E --> E2["Objeto: +50·9.8·1 = +490 N·m"]:::k4
  E --> E3["Viga: +20·9.8·2(2) = +490 N·m"]:::k4
  E --> E4["Soporte derecho: −F₂(4)"]:::k4
  E2 --> R1["Σ τ = 0: 490 + 490 − 4 F₂ = 0<br/>F₂ = 245 N"]:::k1
  E3 --> R1
  E4 --> R1
  R1 --> R2["Σ F = 0: F₁ = 490 + 196 − 245<br/>= 441 N"]:::k1
  A --> T["Verificar ambas condiciones<br/>rotacional y traslacional"]:::k5
'''

F["Trabajo_y_Energía_01"] = '''
flowchart TD
  A["Signos del trabajo<br/>W = F d cosθ"]:::k2
  A --> B["θ menor que 90°: W mayor que 0<br/>energía entra al objeto"]:::k1
  A --> C["θ = 90°: W = 0<br/>la fuerza no aporta energía"]:::k3
  A --> D["θ mayor que 90°: W menor que 0<br/>la fuerza quita energía"]:::k6
  D --> D1["Fricción típica: θ = 180°"]:::k6
  A --> E["Ejemplos"]:::k5
  E --> E1["Peso bajando: +m g h<br/>subiendo: −m g h"]:::k5
  E --> E2["Normal en constante horizontal: 0"]:::k3
  A --> F["Interpretación: W positivo acelera<br/>negativo frena"]:::k4
'''

F["Trabajo_y_Energía_02"] = '''
flowchart TD
  A["Trabajo neto y equivalencias"]:::k2
  A --> B["W neto = Σ trabajos<br/>de cada fuerza"]:::k3
  A --> C["W del F neta:<br/>(ΣF) · d"]:::k3
  B --> D["Se pueden sumar<br/>en cualquier orden"]:::k1
  A --> E["Energía potencial del resorte<br/>U = ½ k (x₁² − x₂²)"]:::k4
  E --> F["Al conservar energía el trabajo<br/>de fuerzas conservativas guarda<br/>como U"]:::k5
  D --> G["Verificación: Σ F debe dar<br/>resultante física real"]:::k6
'''

F["Trabajo_y_Energía_03"] = '''
flowchart TD
  A["Casos concretos de trabajo"]:::k2
  A --> B["Fuerza constante diagonal:<br/>W = F d cosθ"]:::k1
  A --> C["Peso W = ± m g h"]:::k1
  A --> D["Normal: cero en horizontal<br/>no va en otro sentido"]:::k3
  A --> E["Fricción cinética:<br/>W = −μ N d"]:::k4
  E --> F["Distancia que se arrastra sobre la<br/>superficie mientras dura el contacto"]:::k4
  A --> G["Resorte: integral<br/>W = −½ k Δ(x²)"]:::k4
  A --> H["Método: redactar el DCL<br/>antes de asignar signos"]:::k5
'''

F["Trabajo_y_Energía_04"] = '''
flowchart TD
  A["Trabajo en modelo teórico"]:::k2
  A --> B["Teorema trabajo - energía<br/>W total = ΔE cinética"]:::k3
  A --> C["Energía externa:<br/>potencia P = dW / dt = F v"]:::k3
  A --> D["Conservativas: guardan<br/>U = m g h · ½ k x²"]:::k4
  D --> E["No conservativas quitan<br/>o agregan energía"]:::k4
  A --> F["Cuerda y tensión"]:::k3
  F --> F1["Polea ideal: Σ τ = 0 ·<br/>la misma tensión"]:::k3
  A --> G["Verificar unidades: N·m = J"]:::k6
'''

F["Trabajo_y_Energía_05"] = '''
flowchart TD
  A["Gráfica F vs desplazamiento"]:::k2
  A --> B["Área bajo la curva<br/>= trabajo"]:::k1
  B --> C["Fuerza constante:<br/>rectángulo F·d"]:::k1
  B --> D["Resorte: triángulo<br/>½ k x²"]:::k4
  B --> E["Fuerza variable:<br/>∫ F(x) dx"]:::k4
  E --> F["Área de la curva eje arriba<br/>abajo: si F va contra el movimiento"]:::k5
  A --> G["Aplicación: frenado visto<br/>en la gráfica F - x"]:::k5
'''

F["Trabajo_y_Energía_06"] = '''
flowchart TD
  A["Ejercicio pato y trineo"]:::k2
  A --> B["Datos: F = 40 N<br/>θ = 20° · d = 50 m"]:::k3
  B --> C["W = F d cos20°"]:::k1
  C --> D["W = 40 · 50 · 0.9397"]:::k1
  D --> E["W ≈ 1879 J"]:::k4
  E --> F["θ menor que 90°: trabajo positivo<br/>la fuerza ayuda al movimiento"]:::k1
  A --> G["Ojo: usar cos θ y no sin θ<br/>el ángulo va vs. el desplazamiento"]:::k6
'''

F["Trabajo_y_Energía_07"] = '''
flowchart TD
  A["Bloque empujado 10 kg<br/>F = 10 N a 30° · d = 2 m"]:::k2
  A --> B["1. Trabajo del empuje:<br/>W_F = 10 · 2 · cos30° = 17.32 J"]:::k3
  A --> C["2. Normal y peso:<br/>W = 0 · perpendiculares"]:::k3
  A --> D["3. Falta fricción:<br/>N = mg − F sin30°"]:::k4
  D --> D1["N = 98.1 − 5 = 93.1 N"]:::k4
  D1 --> E["f_k = μ N = 0.3 · 93.1<br/>= 27.93 N"]:::k4
  E --> F["W fricción = −55.86 J"]:::k6
  B --> G["Sigue en la siguiente figura:<br/>sumar neto y interpretar"]:::k5
'''

F["Trabajo_y_Energía_08"] = '''
flowchart TD
  A["Cerrar el bloque empujado"]:::k2
  A --> B["W_F = 17.32 J"]:::k3
  A --> C["W_N = W_peso = 0"]:::k3
  A --> D["W_fricción = −55.86 J"]:::k6
  B --> E["W neto = 17.32 − 55.86<br/>= −38.54 J"]:::k1
  C --> E
  D --> E
  E --> F["W menor que 0: el bloque<br/>se desacelera"]:::k6
  F --> G["Coherente con teorema<br/>trabajo - energía"]:::k5
'''

F["Trabajo_y_Energía_09"] = '''
flowchart TD
  A["Errores y trucos del trabajo"]:::k2
  A --> B["Errores comunes"]:::k6
  B --> B1["Usar F completa en lugar<br/>de F cosθ"]:::k6
  B --> B2["Confundir desplazamiento<br/>con distancia sobre la curva"]:::k6
  B --> B3["Olvidar el signo del trabajo"]:::k6
  A --> C["Trucos"]:::k1
  C --> C1["Dibujar DCL con ángulos reales"]:::k1
  C --> C2["Sistema de coordenadas claro"]:::k1
  C --> C3["Chequear que el signo<br/>tenga sentido físico"]:::k1
  A --> D["Regla: solo la componente<br/>paralela a d trabaja"]:::k5
'''

F["Unidades_y_Magnitudes_Físicas_01"] = '''
flowchart TD
  A["Magnitudes físicas"]:::k2
  A --> B["Fundamentales SI<br/>7 clases"]:::k3
  B --> B1["Longitud m · masa kg<br/>tiempo s"]:::k1
  B --> B2["Corriente A · temperatura K<br/>cantidad de sustancia mol · luminosa cd"]:::k1
  B --> A
  A --> C["Derivadas"]:::k4
  C --> C1["Velocidad m/s · aceleración m/s²"]:::k3
  C --> C2["Fuerza N = kg m/s²"]:::k3
  C --> C3["Trabajo J = N m"]:::k3
  C --> C4["Potencia W = J/s"]:::k3
  A --> D["SI desde 1960:<br/>base métrica decimal"]:::k5
  D --> E["Sin estándar no hay<br/>medición comparable"]:::k6
'''

F["Uso_del_Calibrador_de_Vernier_(Pie_de_Rey)_01"] = '''
flowchart TD
  A["Lectura del calibrador"]:::k2
  A --> B["1. Escala principal:<br/>leer el mm completo<br/>pasado el cero del vernier"]:::k3
  A --> C["2. Vernier: buscar la línea<br/>que coincide"]:::k3
  B --> D["3. Sumar:<br/>lectura + n × precisión"]:::k4
  D --> E["Precisiones típicas"]:::k5
  E --> E1["10 divisiones: 0.1 mm"]:::k1
  E --> E2["20 divisiones: 0.05 mm<br/>19 mm = 20 divisiones"]:::k1
  E --> E3["50 divisiones: 0.02 mm<br/>49 mm = 50 divisiones"]:::k1
  D --> F["Ejemplo: cero entre 34 y 35 ·<br/>coincide la 7 con 0.1 mm<br/>→ 34.7 mm"]:::k4
'''

F["Vectores_01"] = '''
flowchart TD
  A["Vectores aplicados a la física"]:::k2
  A --> B["Cinemática: posición vel y<br/>relativos"]:::k3
  A --> C["Dinámica: ΣF = m a<br/>por componentes"]:::k3
  C --> C1["ΣF_x = m a_x · ΣF_y = m a_y<br/>ΣF_z = m a_z"]:::k3
  A --> D["Operaciones"]:::k4
  D --> D1["Suma cabeza - cola"]:::k1
  D --> D2["Producto punto cos:<br/>proyecciones"]:::k1
  D --> D3["Producto cruz sin:<br/>perpendiculares + mano derecha"]:::k1
  A --> E["Ejemplo: A + B<br/>A = 3i + 4j · B = −2i + 5j"]:::k5
  E --> F["(3−2)i + (4+5)j = i + 9j<br/>magnitud √82"]:::k4
'''

F["Velocidad_Relativa_para_Barcos_y_Aviones_01"] = '''
flowchart TD
  A["Velocidad relativa<br/>avión con viento"]:::k2
  A --> B["v_AB = v_A − v_B<br/>A visto desde B"]:::k3
  A --> C["Viento: medio en movimiento"]:::k4
  C --> C1["misma dirección: v tierra = v_a ± v_w<br/>cola suma · frente resta"]:::k1
  C --> C2["viento cruzado:<br/>v_tierra = √(v_a² + v_w²)"]:::k1
  C --> C3["ángulo: arctan(v_w / v_a)"]:::k3
  A --> D["Casos: vuelo comercial<br/>helicópteros · paracaidistas"]:::k5
  C1 --> E["Ver el medio también se mueve:<br/>sumar como vectores"]:::k5
'''

F["Velocidad_Relativa_para_Barcos_y_Aviones_02"] = '''
flowchart TD
  A["Barcos en corriente"]:::k2
  A --> B["v tierra = v barco + v corriente<br/>suma vectorial"]:::k3
  B --> C["a favor del río:<br/>el río arrastra al barco"]:::k1
  B --> D["cruce perpendicular:<br/>derivación"]:::k4
  D --> D1["La corriente mueve al barco<br/>aguas abajo mientras cruza"]:::k4
  D --> D2["magnitud por Pitágoras<br/>v_tierra = √(v_ba² + v_c²)"]:::k3
  A --> E["Canales y mares:<br/>anchuras y travesías"]:::k5
  A --> F["Regla VIMAR:<br/>vectorizar · identificar referencias<br/>marcar ecuación · aplicar componentes ·<br/>resolver"]:::k6
'''

F["Velocidad_Relativa_para_Barcos_y_Aviones_03"] = '''
flowchart TD
  A["Rumbo de compensación"]:::k2
  A --> B["Meta en costa en frente<br/>corriente lateral"]:::k3
  A --> C["Apuntar levemente<br/>aguas arriba"]:::k4
  C --> C1["deriva natural: cancela<br/>el arrastre de la corriente"]:::k1
  C --> C2["v deseada = v vehículo/medio<br/>+ v compensación"]:::k4
  C2 --> D["Componente perpendicular<br/>al destino: debe ser 0"]:::k1
  D --> E["Tiempo t = d / v completo<br/>solo cuenta la componente útil"]:::k3
  A --> F["Avión: cruce con viento de cola<br/>lateral · compensar hacia lados"]:::k5
'''

F["Velocidad_Relativa_para_Barcos_y_Aviones_04"] = '''
flowchart TD
  A["Diagrama de vectores<br/>de velocidad"]:::k2
  A --> B["Río: 200 m · corriente 3 m/s<br/>barco 5 m/s respecto al agua"]:::k3
  B --> C["v barco agua: [−3 I +4 J] m/s"]:::k3
  C --> C1["Componente X compensará la<br/>corriente de 3 m/s aguas abajo"]:::k4
  C --> C2["Componente Y = 4 m/s<br/>para cruzar"]:::k4
  C2 --> D["Rumbo: θ = arctan(3/4)<br/>= 36.87° contra la corriente"]:::k1
  D --> E["Tiempo de cruce:<br/>t = 200 / 4 = 50 s"]:::k1
  A --> F["Vectores ∥ suma directa ·<br/>⊥ Pitágoras · ángulo → componentes"]:::k5
'''

F["Viscosidad_y_Número_de_Reynolds_01"] = '''
flowchart TD
  A["Viscosidad dinámica μ<br/>resistencia al corte"]:::k2
  A --> B["η = μ / ρ cinemática<br/>m²/s"]:::k3
  A --> C["Tipos de fluidos"]:::k4
  C --> C1["Newtoniano: τ ∝ gradiente<br/>agua · aire"]:::k1
  C --> C2["No newtoniano: cambia con el corte"]:::k4
  C --> C3["Plástico ideal: necesita<br/>esfuerzo mínimo"]:::k4
  A --> D["Re = ρ v D / μ"]:::k5
  D --> D1["Bajo Re: dominan viscosidad<br/>laminar"]:::k5
  D --> D2["Alto Re: dominan inercia<br/>turbulencia"]:::k5
  A --> E["Valores 20 °C: agua 0.001 Pa·s<br/>aceite 0.1 a 0.2 · glicerina 1.5"]:::k7
'''

# ---------------------------------------------------------------
def main():
    cats = json.load(open(os.path.join(TMP, "catalogo_fis.json"), encoding="utf-8"))
    ghosts = list(cats["ghosts"].keys())
    missing = [k for k in ghosts if k not in F]
    extra = [k for k in F if k not in ghosts]
    print("faltan:", missing)
    print("sobran:", extra)
    if missing or extra:
        raise SystemExit(1)
    mmdc = shutil.which("mmdc") or shutil.which("mmdc.cmd")
    fails = []
    for name in ghosts:
        src = F[name].strip() + STD
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

# missing import subprocess at top? add below
import subprocess
main()

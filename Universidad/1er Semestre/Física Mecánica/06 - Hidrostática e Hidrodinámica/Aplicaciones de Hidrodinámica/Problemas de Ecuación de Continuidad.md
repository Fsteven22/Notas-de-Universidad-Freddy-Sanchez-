---
dg-publish: true
---

# Problemas de Ecuación de Continuidad

> [!quote] "Lo que entra debe salir: la ecuación de continuidad es el reflejo matemático de que la masa no se crea ni se destruye en el flujo." 💧
>
> [!info] La ecuación de continuidad expresa la conservación de masa en fluidos en movimiento. Es fundamental para analizar el comportamiento de fluidos en tuberías, canales, boquillas y cualquier sistema donde el área transversal cambie a lo largo del flujo.

## 🔧 Conceptos Fundamentales

> [!info] **Principio de Conservación de Masa** ⚖️
> 
> ### Ecuación General:
> 
> **ρ₁A₁v₁ = ρ₂A₂v₂** (flujo compresible)
> 
> ### Para Flujo Incompresible (ρ = constante):
> 
> **A₁v₁ = A₂v₂ = Q** (caudal constante)
> 
> ### Variables Fundamentales:
> 
> - **Caudal (Q)**: Volumen que pasa por unidad de tiempo [m³/s, L/min]
> - **Velocidad (v)**: Velocidad media del fluido [m/s]
> - **Área (A)**: Área transversal perpendicular al flujo [m²]
> - **Densidad (ρ)**: Masa por unidad de volumen [kg/m³]
> 
> ### Relaciones Derivadas:
> 
> |Magnitud|Fórmula|Unidades SI|
> |---|---|---|
> |Caudal|Q = A × v|m³/s|
> |Velocidad media|v = Q/A|m/s|
> |Caudal másico|ṁ = ρ × Q|kg/s|
> |Área|A = Q/v|m²|
>
> [!tip] **Tipos de Secciones Transversales** 🔄
> 
> ### Geometrías Comunes:
> 
> **Circular**: A = πr² = π(D/2)² = πD²/4
> 
> **Rectangular**: A = b × h (base × altura)
> 
> **Anular**: A = π(R² - r²) (corona circular)
> 
> **Triangular**: A = (b × h)/2
> 
> ### Relaciones de Cambio:
> 
> - **Estrechamiento**: A₂ < A₁ → v₂ > v₁
> - **Ensanchamiento**: A₂ > A₁ → v₂ < v₁
> - **Factor de contracción**: v₂/v₁ = A₁/A₂
>
> [!warning] **Aplicaciones Típicas** 🚿
> 
> ### Sistemas con Cambio de Sección:
> 
> - **Boquillas y toberas**: Aceleración de flujo
> - **Difusores**: Desaceleración de flujo
> - **Venturímetros**: Medición de caudal
> - **Tuberías ramificadas**: Distribución de flujo
> 
> ### Efectos Físicos:
> 
> - **Cavitación**: Baja presión en secciones estrechas
> - **Turbulencia**: Cambios bruscos de sección
> - **Pérdidas de energía**: Fricción y separación
>
> [!success] 🔗 Metodología de Resolución
> 
> ```mermaid
> graph TD
>     A[Identificar Puntos de Interés] --> B[Definir Áreas Transversales]
>     B --> C[Aplicar Ecuación de Continuidad]
>     C --> D[Verificar Unidades]
>     D --> E[Interpretar Resultados]
>     E --> F[Validar Coherencia Física]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
> ```
>
> [!note] **Fórmulas Clave** 📐
> 
> ### Ecuación Básica:
> 
> **Q = A₁v₁ = A₂v₂** (flujo incompresible)
> 
> ### Caudal en función del diámetro:
> 
> **Q = (π/4)D₁²v₁ = (π/4)D₂²v₂**
> 
> ### Relación de velocidades:
> 
> **v₂/v₁ = A₁/A₂ = (D₁/D₂)²** (para secciones circulares)
> 
> ### Caudal másico:
> 
> **ṁ = ρQ = ρAv** [kg/s]

## 🎯 Estrategias de Resolución

> [!tip] **Método CAVE (Caudal-Área-Velocidad-Evaluación)** 🧠
> 
> ### **C**audal - Identifica la conservación
> 
> 1. Reconoce que Q₁ = Q₂ para flujo incompresible
> 2. Identifica los puntos donde conoces/necesitas datos
> 3. Establece la ecuación de continuidad
> 
> ### **A**rea - Calcula las secciones transversales
> 
> 4. Determina la geometría en cada punto
> 5. Calcula las áreas usando fórmulas geométricas
> 6. Considera cambios graduales vs abruptos
> 
> ### **V**elocidad - Encuentra las velocidades
> 
> 7. Usa v = Q/A en cada sección
> 8. Aplica relaciones de proporcionalidad
> 9. Verifica coherencia con datos conocidos
> 
> ### **E**valuación - Verifica y concluye
> 
> 10. Revisa unidades y órdenes de magnitud
> 11. Comprueba la conservación de masa
> 12. Interpreta el resultado físicamente

## 📚 Problemas Tipo

> [!example] **Problema 1: Tubería con Estrechamiento** 🔧
> 
> ### Enunciado:
> 
> Una tubería horizontal transporta agua. En la sección 1 tiene diámetro D₁ = 20 cm y velocidad v₁ = 2 m/s. En la sección 2 se estrecha a D₂ = 10 cm. Calcula: a) El caudal b) La velocidad en la sección 2
> 
> ### Datos:
> 
> - D₁ = 20 cm = 0.20 m
> - D₂ = 10 cm = 0.10 m
> - v₁ = 2 m/s
> - Fluido: agua (incompresible)
> 
> ### Solución:
> 
> **a) Caudal:**
> 
> - A₁ = π(D₁/2)² = π(0.10)² = 0.0314 m²
> - Q = A₁v₁ = 0.0314 × 2 = **0.0628 m³/s = 62.8 L/s**
> 
> **b) Velocidad en sección 2:**
> 
> - A₂ = π(D₂/2)² = π(0.05)² = 0.00785 m²
> - Por continuidad: Q = A₂v₂
> - v₂ = Q/A₂ = 0.0628/0.00785 = **8 m/s**
> 
> **Verificación**: v₂/v₁ = (D₁/D₂)² = (20/10)² = 4 ✓
>
> [!example] **Problema 2: Sistema de Tuberías Ramificadas** 🌿
> 
> ### Enunciado:
> 
> Una tubería principal de diámetro 30 cm con caudal de 0.15 m³/s se divide en tres ramas: Rama A (D = 15 cm), Rama B (D = 12 cm), Rama C (D = 10 cm). Si las velocidades en las ramas A y B son 6 m/s y 8 m/s respectivamente, calcula la velocidad en la rama C y en la tubería principal.
> 
> ### Datos:
> 
> - Tubería principal: D₀ = 30 cm, Q₀ = 0.15 m³/s
> - Rama A: D_A = 15 cm, v_A = 6 m/s
> - Rama B: D_B = 12 cm, v_B = 8 m/s
> - Rama C: D_C = 10 cm, v_C = ?
> 
> ### Solución:
> 
> **Caudales en cada rama:**
> 
> - A_A = π(0.075)² = 0.0177 m²
>     
> - Q_A = A_A × v_A = 0.0177 × 6 = 0.106 m³/s
>     
> - A_B = π(0.06)² = 0.0113 m²
>     
> - Q_B = A_B × v_B = 0.0113 × 8 = 0.090 m³/s
>     
> 
> **Por conservación de masa:**
> 
> - Q₀ = Q_A + Q_B + Q_C
> - Q_C = Q₀ - Q_A - Q_B = 0.15 - 0.106 - 0.090 = **-0.046 m³/s**
> 
> **Error en el planteamiento**: Los datos son inconsistentes. **Recalculando con Q₀ = 0.25 m³/s:**
> 
> - Q_C = 0.25 - 0.106 - 0.090 = 0.054 m³/s
> - A_C = π(0.05)² = 0.00785 m²
> - **v_C = Q_C/A_C = 0.054/0.00785 = 6.88 m/s**
> 
> **Velocidad en tubería principal:**
> 
> - A₀ = π(0.15)² = 0.0707 m²
> - **v₀ = Q₀/A₀ = 0.25/0.0707 = 3.54 m/s**
>
> [!example] **Problema 3: Boquilla Variable** 💨
> 
> ### Enunciado:
> 
> Una boquilla cónica reduce el diámetro linealmente desde 8 cm hasta 2 cm en una longitud de 20 cm. Si el caudal es 12 L/s, calcula la velocidad a distancias de 0, 5, 10, 15 y 20 cm desde la entrada.
> 
> ### Datos:
> 
> - D₁ = 8 cm (entrada), D₂ = 2 cm (salida)
> - Longitud: L = 20 cm
> - Q = 12 L/s = 0.012 m³/s
> - Variación lineal de diámetro
> 
> ### Solución:
> 
> **Ecuación del diámetro:**
> 
> - D(x) = D₁ - (D₁ - D₂) × (x/L)
> - D(x) = 8 - (8-2) × (x/20) = 8 - 0.3x [cm]
> 
> **Cálculo de velocidades:**
> 
> |x (cm)|D (cm)|A (m²)|v (m/s)|
> |---|---|---|---|
> |0|8.0|0.00503|2.39|
> |5|6.5|0.00332|3.61|
> |10|5.0|0.00196|6.11|
> |15|3.5|0.00096|12.5|
> |20|2.0|0.00031|**38.2**|
> 
> **Observación**: La velocidad aumenta dramáticamente hacia la salida debido a la reducción cuadrática del área.

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "AVAN"** 🌊
> 
> **A**rea pequeña → **V**elocidad alta **A**rea grande → velocidad **N**ormal (baja)
> 
> **Regla del Producto Constante**: A₁v₁ = A₂v₂ = constante
>
> [!tip] **Analogía del Río** 🏞️
> 
> - **Río ancho** (A grande) → agua **lenta** (v pequeña)
> - **Río estrecho** (A pequeña) → agua **rápida** (v grande)
> - **Caudal constante**: La misma cantidad de agua pasa por cualquier sección

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir área con diámetro**: Recordar que A ∝ D² para círculos
> 2. **Olvidar la incompresibilidad**: Solo válida para líquidos y gases a baja velocidad
> 3. **Unidades inconsistentes**: Mezclar cm, m, L/s, m³/s sin conversión
> 4. **Velocidad media vs puntual**: La ecuación usa velocidad media
> 5. **Ignorar ramificaciones**: En bifurcaciones, Q_entrada = Σ Q_salidas
> 6. **Área mal calculada**: Usar radio en lugar de diámetro o viceversa

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Ingeniería Hidráulica:
> 
> - Diseño de sistemas de riego por aspersión
> - Dimensionamiento de tuberías de distribución
> - Análisis de pérdidas en redes de agua potable
> 
> ### Industria:
> 
> - Toberas de inyección en motores
> - Sistemas de ventilación industrial
> - Procesos de atomización y pulverización
> 
> ### Medicina:
> 
> - Flujo sanguíneo en arterias y capilares
> - Sistemas de infusión intravenosa
> - Equipos de hemodiálisis
> 
> ### Aeronáutica:
> 
> - Diseño de toberas de motores a reacción
> - Túneles de viento para pruebas
> - Sistemas de combustible en aeronaves

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Ecuación de Continuidad y Bernoulli]] - Teoría completa
> - [[Flujo Laminar y Ecuación de Poiseuille]] - Flujo con viscosidad
> - [[Presión y Densidad]] - Propiedades de fluidos
> - [[Hidrodinámica]] - Conceptos generales
> - **Próximo tema**: [[Problemas de Ecuación de Bernoulli]]

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Vectores]] - Para análisis vectorial de velocidades
> - [[Unidades y Magnitudes Físicas]] - Conversiones y dimensional
> - **Matemáticas**: Geometría básica, áreas de figuras planas
> 
> ### **Conocimientos Previos**:
> 
> - Concepto de densidad y fluidos incompresibles
> - Caudal y velocidad media
> - Principio de conservación de masa
>
> [!note] **Temas Relacionados**
> 
> - [[Viscosidad y Número de Reynolds]] - Caracterización del flujo
> - **Medición de caudal**: Venturímetros, rotámetros, ultrasonido
> - **CFD**: Dinámica de fluidos computacional

---

**Tags:** #hidrodinamica #continuidad #caudal #velocidad #flujo #incompresible #tuberias #conservacion-masa #fisica-mecanica #problemas #boquillas #venturi

# Problemas del Tubo de Venturi

>[!quote] "El tubo de Venturi es la sinfonía perfecta entre continuidad y energía: donde el fluido acelera, la presión disminuye, creando una danza hidrodinámica que podemos medir y controlar." 🎼
>
> [!info] El tubo de Venturi, inventado por Giovanni Battista Venturi en 1797, es un dispositivo fundamental para medir el caudal de fluidos basado en la aplicación simultánea del principio de Bernoulli y la ecuación de continuidad. Su diseño ingenioso convierte las variaciones de presión en información precisa sobre el flujo, siendo esencial en aplicaciones industriales y de laboratorio.

## 🌀 Fundamentos Teóricos

> [!info] **Principio del Tubo de Venturi** 🔄
> 
> ### Diseño Característico:
> 
> - **Sección 1**: Entrada (diámetro grande D₁)
> - **Sección 2**: Garganta (diámetro pequeño D₂)  
> - **Sección 3**: Salida (recuperación a D₁)
> - **Ángulo de convergencia**: 7-15° (típico)
> - **Ángulo de divergencia**: 5-7° (evita separación)
> 
> ### Ecuaciones Fundamentales:
> 
> **Ecuación de Continuidad**: A₁v₁ = A₂v₂ = Q
> 
> **Ecuación de Bernoulli**: P₁ + ½ρv₁² = P₂ + ½ρv₂²
> 
> ### Resultado Final:
> 
> **Q = A₂√[2(P₁ - P₂)/(ρ(1 - β⁴))]**
> 
> - **β = D₂/D₁**: Relación de diámetros
> - **P₁ - P₂**: Diferencia de presión
> - **ρ**: Densidad del fluido
> 
> ### Interpretación Física:
> |Parámetro|Comportamiento|Causa|
> |---|---|---|
> |Velocidad|v₂ > v₁|Reducción de área (continuidad)|
> |Presión|P₂ < P₁|Aumento de velocidad (Bernoulli)|
> |Caudal|Q = constante|Conservación de masa|
> |Energía|Conversión P↔K|Intercambio presión-velocidad|
>
> [!tip] **Coeficientes de Corrección** 🔧
> 
> ### Coeficiente de Descarga (Cd):
> 
> **Q_real = Cd × Q_teórico**
> 
> **Q = Cd × A₂√[2(P₁ - P₂)/(ρ(1 - β⁴))]**
> 
> - **Cd**: Coeficiente de descarga (0.95-0.99)
> - Considera pérdidas por fricción y efectos viscosos
> - Depende de Re y β
> 
> ### Factores que Afectan Cd:
> 
> **1. Número de Reynolds**:
> - **Re < 10⁴**: Cd variable con Re
> - **Re > 2×10⁴**: Cd aproximadamente constante
> - **Re = ρvD/μ**: Calculado en garganta
> 
> **2. Relación β = D₂/D₁**:
> - **β = 0.2-0.4**: Cd ≈ 0.99
> - **β = 0.5-0.7**: Cd ≈ 0.97-0.98
> - **β > 0.8**: Precisión reducida
> 
> **3. Acabado Superficial**:
> - Superficie lisa: Mayor Cd
> - Rugosidad: Reduce Cd
> - Transiciones suaves: Mejor desempeño
>
> [!warning] **Tipos de Venturi y Variaciones** ⚡
> 
> ### Clasificación por Construcción:
> 
> **1. Venturi Clásico**:
> - Convergencia y divergencia suaves
> - Máxima recuperación de presión
> - Menor pérdida de carga permanente
> 
> **2. Tobera (Nozzle)**:
> - Solo sección convergente
> - Menor costo de fabricación
> - Mayor pérdida de carga
> 
> **3. Placa Orificio**:
> - Restricción abrupta
> - Más económica
> - Mayor pérdida, menor precisión
> 
> ### Configuraciones Especiales:
> 
> - **Venturi insertable**: Para tuberías existentes
> - **Venturi de bajo β**: Alta sensibilidad
> - **Venturi de flujo reverso**: Bidireccional
> - **Micro-venturi**: Aplicaciones de laboratorio
>
>[!success] 🔗 Funcionamiento del Tubo de Venturi
> 
> ```mermaid
> graph LR
>     A[Entrada D₁] -->|Convergencia| B[Garganta D₂]
>     B -->|Divergencia| C[Salida D₁]
>     D[Alta Presión P₁] --> E[Baja Presión P₂]
>     E --> F[Recuperación P₃]
>     G[Baja Velocidad v₁] --> H[Alta Velocidad v₂]
>     H --> I[Velocidad v₁]
>     J[Medición ΔP] --> K[Cálculo de Q]
>     K --> L[Caudal Conocido]
>     style A fill:#e1f5fe
>     style B fill:#ffcdd2
>     style C fill:#e1f5fe
>     style J fill:#f3e5f5
> ```
>
> [!note] **Relaciones Fundamentales** 📊
> 
> ### Ecuación de Velocidades:
> 
> **v₂/v₁ = (A₁/A₂) = (D₁/D₂)² = 1/β²**
> 
> ### Diferencia de Presión:
> 
> **ΔP = P₁ - P₂ = (ρv₁²/2)(β⁻⁴ - 1)**
> 
> ### Pérdida de Carga Permanente:
> 
> **ΔP_pérdida = (1 - Cd²)(P₁ - P₂)**
> 
> ### Sensibilidad del Medidor:
> 
> **dQ/dΔP ∝ 1/√ΔP**: Mayor sensibilidad a bajo caudal
> 
> ### Límites de Operación:
> |Parámetro|Rango Recomendado|Observaciones|
> |---|---|---|
> |Relación β|0.2 - 0.75|Compromiso precisión-pérdida|
> |Número Re|> 2×10⁴|Para Cd constante|
> |Cavitación|P₂ > P_vapor|Evitar formación de burbujas|
> |Velocidad|< 0.3 Mach|Flujo incompresible|

## 🎯 Estrategias de Resolución

> [!tip] **Método VENTU (Velocidades-Ecuaciones-Newton-Transición-Unidades)** 🧠
> 
> ### **V**elocidades - Relación de flujos
> 
> 1. Aplica ecuación de continuidad: A₁v₁ = A₂v₂
> 2. Calcula relación de velocidades: v₂ = v₁/β²
> 3. Determina velocidades en función del caudal
> 4. Verifica régimen de flujo (Re)
> 
> ### **E**cuaciones - Principios fundamentales
> 
> 5. Aplica Bernoulli entre secciones 1 y 2
> 6. Substituye velocidades de continuidad
> 7. Despeja diferencia de presión o caudal
> 8. Incluye coeficientes de corrección
> 
> ### **N**ewton - Análisis de fuerzas
> 
> 9. Considera fuerzas de presión en el fluido
> 10. Analiza cambio de momentum
> 11. Evalúa pérdidas por fricción
> 12. Verifica equilibrio de fuerzas
> 
> ### **T**ransición - Geometría del dispositivo
> 
> 13. Define relación β = D₂/D₁
> 14. Calcula áreas A₁ y A₂
> 15. Considera ángulos de transición
> 16. Evalúa efectos de entrada y salida
> 
> ### **U**nidades - Verificación dimensional
> 
> 17. Verifica consistencia de unidades
> 18. Convierte a unidades de ingeniería
> 19. Interpreta resultados físicamente
> 20. Compara con especificaciones de diseño

## 📚 Problemas Tipo

> [!example] **Problema 1: Medición de Caudal de Agua** 💧
> 
> ### Enunciado:
> 
> Un tubo de Venturi horizontal se usa para medir el flujo de agua en una tubería de 200 mm de diámetro. La garganta tiene 100 mm de diámetro. Un manómetro diferencial de mercurio indica una diferencia de 250 mm Hg. Si Cd = 0.98, determina: a) El caudal de agua b) Las velocidades en ambas secciones c) La pérdida de carga permanente
> 
> ### Solución:
> 
> **Datos dados**:
> - D₁ = 200 mm = 0.2 m, D₂ = 100 mm = 0.1 m
> - Δh_Hg = 250 mm = 0.25 m
> - Cd = 0.98, ρ_agua = 1000 kg/m³, ρ_Hg = 13,600 kg/m³
> 
> **Cálculos preliminares**:
> - β = D₂/D₁ = 0.1/0.2 = 0.5
> - A₁ = π(0.1)² = 0.0314 m², A₂ = π(0.05)² = 0.00785 m²
> - ΔP = (ρ_Hg - ρ_agua) × g × Δh = (13,600 - 1000) × 9.81 × 0.25 = 30,870 Pa
> 
> **a) Caudal de agua**:
> - Q = Cd × A₂ × √[2ΔP/(ρ(1 - β⁴))]
> - Q = 0.98 × 0.00785 × √[2×30,870/(1000×(1 - 0.5⁴))]
> - Q = 0.98 × 0.00785 × √[61,740/(1000×0.9375)] = 0.0621 m³/s = 62.1 L/s
> 
> **b) Velocidades**:
> - v₁ = Q/A₁ = 0.0621/0.0314 = 1.98 m/s
> - v₂ = Q/A₂ = 0.0621/0.00785 = 7.91 m/s
> - Verificación: v₂ = v₁/β² = 1.98/0.25 = 7.92 m/s ✓
> 
> **c) Pérdida de carga permanente**:
> - ΔP_pérdida = (1 - Cd²) × ΔP = (1 - 0.98²) × 30,870 = 1,242 Pa
> - h_pérdida = ΔP_pérdida/(ρg) = 1,242/(1000×9.81) = 0.127 m
>
> [!example] **Problema 2: Venturi para Gas Natural** ⛽
> 
> ### Enunciado:
> 
> Un tubo de Venturi mide el flujo de gas natural (ρ = 0.8 kg/m³, μ = 1.1×10⁻⁵ Pa·s) en una tubería de 300 mm. La garganta tiene 180 mm de diámetro. La diferencia de presión medida es 1500 Pa. Si Cd = 0.96, determina: a) El caudal másico b) El número de Reynolds c) La validez de usar Cd constante
> 
> ### Solución:
> 
> **Datos**:
> - D₁ = 300 mm = 0.3 m, D₂ = 180 mm = 0.18 m
> - ρ = 0.8 kg/m³, μ = 1.1×10⁻⁵ Pa·s
> - ΔP = 1500 Pa, Cd = 0.96
> 
> **Cálculos preliminares**:
> - β = 0.18/0.3 = 0.6
> - A₁ = π(0.15)² = 0.0707 m², A₂ = π(0.09)² = 0.0254 m²
> 
> **a) Caudal másico**:
> - Q = Cd × A₂ × √[2ΔP/(ρ(1 - β⁴))]
> - Q = 0.96 × 0.0254 × √[2×1500/(0.8×(1 - 0.6⁴))]
> - Q = 0.96 × 0.0254 × √[3000/(0.8×0.8704)] = 1.83 m³/s
> - **Caudal másico**: ṁ = ρQ = 0.8 × 1.83 = 1.46 kg/s
> 
> **b) Número de Reynolds (en garganta)**:
> - v₂ = Q/A₂ = 1.83/0.0254 = 72.0 m/s
> - Re₂ = ρv₂D₂/μ = (0.8 × 72.0 × 0.18)/(1.1×10⁻⁵) = 942,545
> 
> **c) Validez de Cd constante**:
> - Re₂ = 942,545 > 2×10⁴ ✓
> - Es válido usar Cd = 0.96 constante
> - El flujo está en régimen turbulento desarrollado
>
> [!example] **Problema 3: Diseño de Venturi para Aplicación Específica** 🎯
> 
> ### Enunciado:
> 
> Se requiere diseñar un tubo de Venturi para medir caudales de agua de 50-500 L/s en una tubería de 400 mm. El manómetro diferencial disponible mide hasta 2 m de columna de agua. Determina: a) El diámetro óptimo de garganta b) La diferencia de presión para Q = 300 L/s c) El error porcentual si se desprecia Cd
> 
> ### Solución:
> 
> **Especificaciones de diseño**:
> - D₁ = 400 mm = 0.4 m
> - Q_rango = 0.05 - 0.5 m³/s
> - ΔP_max = ρg × 2 = 1000 × 9.81 × 2 = 19,620 Pa
> - Cd = 0.98 (asumido)
> 
> **a) Diámetro óptimo (para Q_max = 0.5 m³/s)**:
> - Despejando D₂ de la ecuación de Venturi:
> - 0.5 = 0.98 × (π D₂²/4) × √[2×19,620/(1000×(1 - β⁴))]
> - Probando β = 0.6: D₂ = 0.24 m
> - A₂ = π(0.12)² = 0.0452 m²
> - Verificación: Q = 0.98 × 0.0452 × √[39,240/(1000×0.8704)] = 0.498 m³/s ≈ 0.5 ✓
> 
> **b) Diferencia de presión para Q = 300 L/s**:
> - Despejando ΔP: ΔP = [Q/(Cd × A₂)]² × ρ(1 - β⁴)/2
> - ΔP = [0.3/(0.98 × 0.0452)]² × 1000 × 0.8704/2
> - ΔP = (6.78)² × 435.2 = 20,008 Pa = 2.04 m de agua
> - **¡Excede el rango del manómetro!** Requiere β menor
> 
> **c) Error sin considerar Cd**:
> - Q_teórico = 0.3/0.98 = 0.306 m³/s
> - Error = (0.306 - 0.3)/0.3 × 100% = 2.0%

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "VENTU"** 🌪️
> 
> **V**elocidad aumenta en garganta (**V**elocity increases)
> **E**cuación de continuidad siempre (**E**quation A₁v₁ = A₂v₂)
> **N**iveles de presión diferentes (**N**ozzle pressure drop)
> **T**ubo mide caudal por ΔP (**T**ube measures flow)
> **U**sa Bernoulli y continuidad (**U**ses both principles)
>
> [!info] **Reglas Nemotécnicas Adicionales** 🎯
> 
> ### "BETA-CHICA": **BETA** **CHICA** da mayor diferencia
> - **B**eta pequeña (D₂/D₁ pequeño)
> - **E**xcelente sensibilidad
> - **T**ubo más efectivo
> - **A**umento de velocidad mayor
> - **CH**orro más rápido
> - **I**ncremento de ΔP
> - **C**audal más fácil de medir
> - **A**plicable para rangos amplios
> 
> ### "P-BAJA-V-ALTA": **P** **BAJA** cuando **V** **ALTA**
> - **Presión** disminuye en garganta
> - **Velocidad** aumenta por continuidad
> - Principio fundamental de Bernoulli
> 
> ### "CD-CERCA-UNO": **CD** siempre **CERCA** de **UNO**
> - **C**oeficiente **D**escarga típico: 0.95-0.99
> - **C**orrección pequeña pero importante
> - **D**iseño bien hecho → Cd alto

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir diámetros**: D₁ (entrada) vs D₂ (garganta)
> 2. **Usar áreas en lugar de diámetros**: β = D₂/D₁, no A₂/A₁
> 3. **Olvidar el término (1 - β⁴)**: En denominador de la ecuación
> 4. **Aplicar en flujo compresible**: Solo válido para líquidos y gases a baja velocidad
> 5. **Ignorar efectos de Reynolds**: Cd variable a Re bajo
> 6. **Mala medición de presión**: Tomas mal ubicadas
> 7. **Despreciar pérdidas permanentes**: En cálculos de eficiencia energética
> 8. **Usar en flujo pulsante**: Requiere amortiguadores de pulsación

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Industria Petroquímica:
> 
> - Medición de hidrocarburos líquidos
> - Control de flujo en refinerías
> - Sistemas de transferencia custodia
> - Monitoreo de procesos químicos
> 
> ### Sistemas de Agua:
> 
> - Plantas de tratamiento
> - Redes de distribución municipal
> - Sistemas de riego industrial
> - Control de caudales en centrales hidroeléctricas
> 
> ### Industria Alimentaria:
> 
> - Dosificación de líquidos en bebidas
> - Control de flujo en lácteos
> - Sistemas CIP (Clean in Place)
> - Medición en cervecerías
> 
> ### Aplicaciones Especializadas:
> 
> - Túneles de viento (medición de velocidad de aire)
> - Sistemas HVAC (calefacción, ventilación)
> - Laboratorios de calibración
> - Investigación en mecánica de fluidos
> 
> ### Ventajas del Venturi:
> - **Alta precisión**: ±0.5-1% del caudal
> - **Amplio rango**: 10:1 típico
> - **Baja pérdida permanente**: 5-15% del ΔP
> - **Sin partes móviles**: Mantenimiento mínimo

## 📈 Casos Especiales

> [!note] **Situaciones Complejas** 🔬
> 
> ### Flujo Compresible (Gases):
> 
> **Factor de Expansión (Y)**:
> - **Y = 1 - (0.41 + 0.35β⁴)(ΔP/P₁)/γ**
> - **γ**: Relación de calores específicos
> - **Aplicable cuando**: ΔP/P₁ < 0.2
> 
> **Ecuación modificada**:
> **ṁ = Cd × Y × A₂ × √[2ρ₁ΔP/(1 - β⁴)]**
> 
> ### Efectos de Temperatura:
> - **Expansión del Venturi**: Cambio de β
> - **Propiedades del fluido**: ρ = ρ(T), μ = μ(T)
> - **Compensación**: Corrección automática o manual
> 
> ### Instalación no Ideal:
> - **Perturbaciones aguas arriba**: Requiere tramos rectos
> - **Efectos de codos**: Distorsión del perfil de velocidad
> - **Vibración de tubería**: Afecta medición de presión
> - **Depósitos en paredes**: Cambio gradual de β
> 
> ### Aplicaciones Especiales:
> - **Flujo bifásico**: Líquido + gas
> - **Fluidos no newtonianos**: Correcciones reológicas
> - **Flujo pulsante**: Amortiguamiento requerido
> - **Condiciones criogénicas**: Materiales especiales

## 🔬 Comparación con Otros Medidores

> [!tip] **Dispositivos de Medición de Flujo** ⚖️
> 
> ### Comparativa de Desempeño:
> 
> |Dispositivo|Precisión|Pérdida de Carga|Rango|Costo|
> |---|---|---|---|---|
> |Venturi clásico|±0.5%|5-15% ΔP|10:1|Alto|
> |Tobera de flujo|±1%|30-60% ΔP|4:1|Medio|
> |Placa orificio|±1-2%|60-90% ΔP|4:1|Bajo|
> |Tubo Pitot|±2-5%|Despreciable|3:1|Bajo|
> |Medidor magnético|±0.2%|Nula|100:1|Alto|
> 
> ### Criterios de Selección:
> - **Precisión requerida**: Venturi para alta precisión
> - **Pérdida de carga aceptable**: Venturi minimiza pérdidas
> - **Costo inicial vs operativo**: Balance económico
> - **Mantenimiento**: Venturi sin partes móviles
> - **Tipo de fluido**: Compatibilidad material-fluido

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Ecuación de Continuidad y Bernoulli]] - Principios fundamentales
> - [[Problemas del Teorema de Torricelli]] - Aplicaciones relacionadas
> - [[Flujo Laminar y Ecuación de Poiseuille]] - Comportamiento viscoso
> - [[Presión y Densidad]] - Conceptos de base
> - [[Aplicaciones de Hidrodinámica]] - Contexto general

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Fundamentos de Hidrostática e Hidrodinámica]] - Base teórica
> - [[Unidades y Magnitudes Físicas]] - Consistencia dimensional
> - [[Vectores]] - Para análisis de velocidades
> - [[Conocimientos Previos a las Prácticas]] - Fundamentos matemáticos

---

**Tags:** #hidrodinamica #tubo-venturi #medicion-flujo #bernoulli #ecuacion-continuidad #caudal #diferencia-presion #coeficiente-descarga #ingenieria-hidraulica #instrumentacion-fluidos

# Gráficas No Lineales

> [!quote] "La naturaleza rara vez es lineal: las gráficas no lineales revelan la verdadera complejidad y belleza de los fenómenos físicos." 📈

> [!info]- Las gráficas no lineales son fundamentales para analizar la mayoría de los fenómenos físicos reales. Mientras que las relaciones lineales proporcionan una base sólida, la naturaleza exhibe comportamientos exponenciales, parabólicos, hiperbólicos y de otros tipos no lineales. Dominar el reconocimiento de patrones y las técnicas de análisis para estas gráficas es esencial para la física experimental moderna.

## 🔍 Identificación de Patrones

> [!info]- **Reconocimiento Visual de Curvas** 👁️
> 
> ### Patrones Fundamentales:
> 
> **1. Comportamiento Exponencial**:
> 
> ```
> Características visuales:
> - Crecimiento/decrecimiento muy rápido
> - Curvatura consistente (cóncava hacia arriba/abajo)
> - Cambio de pendiente dramático
> - Asíntotas horizontales en decrecimiento
> ```
> 
> **2. Comportamiento Parabólico**:
> 
> ```
> Características visuales:
> - Forma de "U" o "∩"
> - Curvatura simétrica alrededor del vértice
> - Una sola dirección de curvatura
> - Puede tener máximo o mínimo definido
> ```
> 
> **3. Comportamiento Hiperbólico**:
> 
> ```
> Características visuales:
> - Curva pronunciada cerca del origen
> - Aplananamiento gradual hacia asíntotas
> - Comportamiento 1/x típico
> - Puede tener discontinuidades
> ```
> 
> **4. Comportamiento Logarítmico**:
> 
> ```
> Características visuales:
> - Crecimiento rápido inicial, luego gradual
> - Curvatura cóncava hacia abajo
> - Tendencia a "saturación"
> - Comportamiento opuesto al exponencial
> ```
> 
> ### Tabla de Reconocimiento Rápido:
> 
> |Tipo de Curva|Forma General|Curvatura|Comportamiento Extremos|
> |---|---|---|---|
> |**Exponencial creciente**|J-shape|Cóncava arriba|Crece sin límite|
> |**Exponencial decreciente**|L-shape invertida|Cóncava arriba|Tiende a cero|
> |**Parabólica (arriba)**|U-shape|Cóncava arriba|Mínimo en el vértice|
> |**Parabólica (abajo)**|∩-shape|Cóncava abajo|Máximo en el vértice|
> |**Hiperbólica**|Curva asintótica|Variable|Tiende a asíntotas|
> |**Logarítmica**|Crecimiento saturado|Cóncava abajo|Crecimiento lento|

> [!tip]- **Estrategias de Identificación** 🎯
> 
> ### Método Sistemático:
> 
> **Paso 1: Observación General**
> 
> ```
> ¿La curva es suave o tiene discontinuidades?
> ¿Crece, decrece o tiene ambos comportamientos?
> ¿Hay simetría evidente?
> ¿Se observan asíntotas?
> ```
> 
> **Paso 2: Análisis de Curvatura**
> 
> ```
> Cóncava hacia arriba (∪): d²y/dx² > 0
> Cóncava hacia abajo (∩): d²y/dx² < 0
> Puntos de inflexión: cambio de curvatura
> ```
> 
> **Paso 3: Comportamiento en los Extremos**
> 
> ```
> x → 0: ¿Qué pasa con y?
> x → ∞: ¿Hay límite finito o crece/decrece indefinidamente?
> ¿Hay valores donde la función no está definida?
> ```
> 
> **Paso 4: Análisis Cuantitativo**
> 
> ```
> Calcular razones entre puntos consecutivos
> Si y(i+1)/y(i) ≈ constante → exponencial
> Si Δy ∝ Δx → lineal
> Si Δy ∝ (Δx)² → parabólica
> ```
> 
> ### Test de Linealización:
> 
> **Para identificar el tipo correcto de función:**
> 
> |Sospecha|Transformación|Gráfica Linealizada|Si es lineal...|
> |---|---|---|---|
> |**Exponencial**|ln(y) vs x|Semi-logarítmica|y = ae^(bx)|
> |**Potencial**|ln(y) vs ln(x)|Log-log|y = ax^n|
> |**Parabólica**|y vs x²|y vs x²|y = ax² + bx + c|
> |**Hiperbólica**|1/y vs x o y vs 1/x|Transformada|y = a/(x+b)|
> 
> ### Contexto Físico:
> 
> **Pistas del fenómeno estudiado:**
> 
> - **Crecimiento/decaimiento radiactivo** → Exponencial
> - **Movimiento bajo gravedad** → Parabólico
> - **Fuerza eléctrica/gravitatoria** → Hiperbólico (1/r²)
> - **Carga/descarga de capacitores** → Exponencial
> - **Oscilaciones amortiguadas** → Exponencial modulada
> - **Resonancia** → Lorentziana (híbrido)

## 📈 Gráficas Exponenciales

> [!info]- **Funciones Exponenciales Fundamentales** ⚡
> 
> ### Forma General:
> 
> ```
> y = a·e^(bx) + c
> ```
> 
> **Parámetros y significado físico:**
> 
> - **a**: Amplitud o factor de escala
> - **b**: Constante de crecimiento/decaimiento
>     - b > 0: Crecimiento exponencial
>     - b < 0: Decaimiento exponencial
> - **c**: Desplazamiento vertical (asíntota horizontal)
> 
> ### Tipos Principales:
> 
> **1. Crecimiento Exponencial Simple**:
> 
> ```
> y = a·e^(bx)    (b > 0)
> 
> Características:
> - Crecimiento acelerado
> - Duplicación en intervalos constantes
> - No hay límite superior
> - Pendiente proporcional al valor actual
> ```
> 
> **2. Decaimiento Exponencial**:
> 
> ```
> y = a·e^(-bx)   (b > 0)
> 
> Características:
> - Decrecimiento hacia cero
> - Vida media constante
> - Asíntota horizontal en y = 0
> - Disminución porcentual constante
> ```
> 
> **3. Exponencial con Offset**:
> 
> ```
> y = a·e^(-bx) + c
> 
> Características:
> - Decaimiento hacia valor constante c
> - Asíntota horizontal en y = c
> - Útil para procesos de relajación
> ```
> 
> ### Conceptos Característicos:
> 
> **Tiempo de Duplicación (τ₂)**:
> 
> ```
> Para y = a·e^(bx): τ₂ = ln(2)/b ≈ 0.693/b
> Tiempo para que y se duplique
> ```
> 
> **Vida Media (τ₁/₂)**:
> 
> ```
> Para y = a·e^(-bx): τ₁/₂ = ln(2)/b ≈ 0.693/b
> Tiempo para que y se reduzca a la mitad
> ```
> 
> **Constante de Tiempo (τ)**:
> 
> ```
> τ = 1/b
> Tiempo para que y cambie por un factor e
> ```

> [!success] 🔬 Aplicaciones Físicas Exponenciales
> 
> ```mermaid
> graph TD
>     A[Fenómenos Exponenciales] --> B[Decaimiento Radiactivo]
>     A --> C[Descarga de Capacitor]
>     A --> D[Enfriamiento de Newton]
>     A --> E[Absorción de Luz]
>     A --> F[Crecimiento Poblacional]
>     A --> G[Circuitos RC]
>     
>     B --> B1["N(t) = N₀e^(-λt)"]
>     C --> C1["V(t) = V₀e^(-t/RC)"]
>     D --> D1["T(t) = T∞ + (T₀-T∞)e^(-kt)"]
>     E --> E1["I = I₀e^(-μx)"]
>     F --> F1["P(t) = P₀e^(rt)"]
>     G --> G1["q(t) = q₀e^(-t/τ)"]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#e0f2f1
> ```

> [!example]- **Análisis de Gráficas Exponenciales** 📊
> 
> ### Ejemplo: Descarga de un Capacitor
> 
> **Situación**: Un capacitor se descarga a través de una resistencia **Ecuación teórica**: V(t) = V₀e^(-t/RC)
> 
> **Datos experimentales**:
> 
> ```
> t (s):  0,    1,    2,    3,    4,    5
> V (V):  12.0, 4.4,  1.6,  0.6,  0.2,  0.1
> ```
> 
> ### Construcción de la Gráfica:
> 
> **Gráfica Original (V vs t)**:
> 
> - Forma: Curva decreciente típica exponencial
> - Comportamiento: Decaimiento rápido inicial, luego gradual
> - Asíntota: V → 0 cuando t → ∞
> 
> **Identificación del patrón**:
> 
> ```
> Razón consecutiva: V(i+1)/V(i)
> 4.4/12.0 = 0.37
> 1.6/4.4  = 0.36
> 0.6/1.6  = 0.38
> → Razón aproximadamente constante ≈ 0.37
> ```
> 
> **Conclusión**: Comportamiento exponencial confirmado
> 
> ### Linealización:
> 
> **Transformación logarítmica**:
> 
> ```
> ln(V) = ln(V₀) - t/RC
> ```
> 
> **Datos linealizados**:
> 
> ```
> t (s):    0,    1,     2,     3,     4,     5
> ln(V):   2.48, 1.48,  0.47, -0.51, -1.61, -2.30
> ```
> 
> **Gráfica ln(V) vs t**:
> 
> - Debe mostrar comportamiento lineal
> - Pendiente = -1/RC
> - Intercepto = ln(V₀)
> 
> ### Ajuste y Parámetros:
> 
> **Regresión lineal de ln(V) vs t**:
> 
> ```
> Pendiente: m = -0.96 s⁻¹
> Intercepto: b = 2.48
> Correlación: r = -0.999
> ```
> 
> **Cálculo de parámetros físicos**:
> 
> ```
> RC = -1/m = 1/0.96 = 1.04 s
> V₀ = e^b = e^2.48 = 12.0 V
> ```
> 
> **Ecuación experimental**: V(t) = 12.0·e^(-t/1.04)
> 
> ### Interpretación Física:
> 
> **Constante de tiempo**: τ = RC = 1.04 s **Vida media**: t₁/₂ = ln(2)·τ = 0.72 s **Significado**: El voltaje se reduce a 1/e ≈ 37% cada 1.04 s

> [!warning]- **Precauciones en Análisis Exponencial** ⚠️
> 
> ### Errores Comunes:
> 
> **1. Confundir tipos exponenciales**:
> 
> - No todos los crecimientos rápidos son exponenciales
> - Verificar siempre con linealización logarítmica
> - Distinguir entre y = a^x y y = e^(ax)
> 
> **2. Problemas con datos cercanos a cero**:
> 
> - ln(y) no está definido para y ≤ 0
> - Ruido experimental puede dominar valores pequeños
> - Considerar offset: y = ae^(-bx) + c
> 
> **3. Rango de validez**:
> 
> - Comportamiento exponencial puede ser solo aproximado
> - Verificar límites físicos del modelo
> - Cuidado con extrapolaciones
> 
> **4. Interpretación de parámetros**:
> 
> - Unidades de las constantes exponenciales
> - Significado físico vs matemático
> - Constantes de tiempo vs frecuencias
> 
> ### Mejores Prácticas:
> 
> **Para análisis robusto**:
> 
> - Usar múltiples décadas de datos si es posible
> - Verificar linealidad en gráfica semi-log
> - Considerar modelos híbridos si es necesario
> - Validar parámetros con teoría física

## 📊 Gráficas Parabólicas

> [!info]- **Funciones Parabólicas y Cuadráticas** 🏗️
> 
> ### Forma General:
> 
> ```
> y = ax² + bx + c
> ```
> 
> **Parámetros fundamentales:**
> 
> - **a**: Coeficiente cuadrático
>     - a > 0: Parábola abre hacia arriba (mínimo)
>     - a < 0: Parábola abre hacia abajo (máximo)
>     - |a| determina la "apertura" de la parábola
> - **b**: Coeficiente lineal
>     - Determina la posición horizontal del vértice
>     - Afecta la asimetría de la curva
> - **c**: Término independiente
>     - Intercepto en y (valor cuando x = 0)
>     - Desplazamiento vertical
> 
> ### Formas Alternativas:
> 
> **1. Forma de vértice**:
> 
> ```
> y = a(x - h)² + k
> 
> Donde:
> - (h, k) es el vértice
> - h = -b/(2a)
> - k = c - b²/(4a)
> ```
> 
> **2. Forma factorizada**:
> 
> ```
> y = a(x - r₁)(x - r₂)
> 
> Donde r₁, r₂ son las raíces (interceptos en x)
> ```
> 
> ### Características Geométricas:
> 
> **Vértice**:
> 
> ```
> Coordenadas: (h, k) = (-b/2a, c - b²/4a)
> - Punto de máximo (a < 0) o mínimo (a > 0)
> - Eje de simetría: x = h
> ```
> 
> **Interceptos**:
> 
> ```
> Intercepto y: (0, c)
> Interceptos x: Resolver ax² + bx + c = 0
> Discriminante: Δ = b² - 4ac
> - Δ > 0: Dos interceptos reales
> - Δ = 0: Un intercepto (tangente)
> - Δ < 0: Sin interceptos reales
> ```
> 
> **Directriz y foco**:
> 
> ```
> Para y = ax²:
> Foco: (0, 1/4a)
> Directriz: y = -1/4a
> ```

> [!tip]- **Aplicaciones Físicas Parabólicas** 🌍
> 
> ### Fenómenos Físicos Comunes:
> 
> **1. Movimiento de Proyectiles**:
> 
> ```
> y = y₀ + v₀t - ½gt²
> 
> Interpretación:
> - a = -½g (coeficiente cuadrático)
> - b = v₀ (velocidad inicial)
> - c = y₀ (altura inicial)
> - Vértice: altura máxima
> ```
> 
> **2. Energía Cinética**:
> 
> ```
> E_k = ½mv²
> 
> Gráfica E_k vs v:
> - Parábola que abre hacia arriba
> - Pasa por el origen
> - Pendiente inicial cero
> ```
> 
> **3. Ley de Hooke (Energía Potencial)**:
> 
> ```
> U = ½kx²
> 
> Gráfica U vs x:
> - Parábola simétrica
> - Mínimo en el equilibrio (x = 0)
> - Curvatura proporcional a k
> ```
> 
> **4. Resistencia del Aire**:
> 
> ```
> F_drag = ½ρv²A·C_d
> 
> Gráfica F vs v:
> - Dependencia cuadrática
> - Solo valores positivos
> ```
> 
> **5. Lentes y Espejos**:
> 
> ```
> 1/f = 1/d₀ + 1/d_i
> 
> Rearreglando puede dar relaciones parabólicas
> entre distancias y magnificaciones
> ```
> 
> ### Identificación en el Laboratorio:
> 
> **Señales de comportamiento parabólico:**
> 
> - Curva suave con un solo extremo (máximo o mínimo)
> - Simetría aproximada alrededor de un eje vertical
> - Cambio de curvatura constante
> - Aceleración/desaceleración constante en sistemas mecánicos

> [!success] 🔧 Análisis de Gráficas Parabólicas
> 
> ```mermaid
> graph TD
>     A[Análisis Parabólico] --> B[Identificación Visual]
>     A --> C[Linealización]
>     A --> D[Ajuste Directo]
>     
>     B --> B1[Forma de U o ∩]
>     B --> B2[Un solo extremo]
>     B --> B3[Simetría aparente]
>     
>     C --> C1["y vs x²"]
>     C --> C2["√y vs x (si y ≥ 0)"]
>     
>     D --> D1[Regresión polinomial]
>     D --> D2[Método de mínimos cuadrados]
>     D --> D3[Forma de vértice]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
> ```

> [!example]- **Ejemplo: Análisis de Movimiento Parabólico** 🎯
> 
> ### Experimento: Lanzamiento de Proyectil
> 
> **Situación**: Una pelota se lanza horizontalmente desde una altura **Ecuación teórica**: y = h₀ - ½gt²
> 
> **Datos experimentales**:
> 
> ```
> t (s):  0,    0.1,  0.2,  0.3,  0.4,  0.5
> y (m):  1.80, 1.75, 1.60, 1.35, 1.00, 0.55
> ```
> 
> ### Análisis Visual:
> 
> **Características observadas**:
> 
> - Curva descendente suave
> - Curvatura constante (cóncava hacia abajo)
> - Intercepto en y = 1.80 m (altura inicial)
> - Aceleración descendente evidente
> 
> **Confirmación del patrón**:
> 
> ```
> Diferencias sucesivas (Δy):
> Δy₁ = 1.75 - 1.80 = -0.05 m
> Δy₂ = 1.60 - 1.75 = -0.15 m  
> Δy₃ = 1.35 - 1.60 = -0.25 m
> Δy₄ = 1.00 - 1.35 = -0.35 m
> Δy₅ = 0.55 - 1.00 = -0.45 m
> 
> Segundas diferencias (ΔΔy):
> ΔΔy₁ = -0.15 - (-0.05) = -0.10 m
> ΔΔy₂ = -0.25 - (-0.15) = -0.10 m
> ΔΔy₃ = -0.35 - (-0.25) = -0.10 m
> ΔΔy₄ = -0.45 - (-0.35) = -0.10 m
> 
> → Segundas diferencias constantes → Parabólico ✓
> ```
> 
> ### Método 1: Linealización
> 
> **Transformación**: y vs t² **Predicción**: Debe ser lineal con pendiente -½g
> 
> **Datos transformados**:
> 
> ```
> t² (s²): 0,    0.01, 0.04, 0.09, 0.16, 0.25
> y (m):   1.80, 1.75, 1.60, 1.35, 1.00, 0.55
> ```
> 
> **Regresión lineal de y vs t²**:
> 
> ```
> Pendiente: m = -5.1 m/s²
> Intercepto: b = 1.79 m
> Correlación: r = -0.9995
> ```
> 
> **Interpretación**:
> 
> ```
> Pendiente = -½g → g = -2m = 10.2 m/s²
> Error respecto a g = 9.81 m/s²: 4.0%
> Altura inicial: h₀ = 1.79 m
> ```
> 
> ### Método 2: Ajuste Parabólico Directo
> 
> **Ajuste**: y = at² + bt + c **Resultado usando mínimos cuadrados**:
> 
> ```
> a = -5.08 m/s²  (coeficiente de t²)
> b = 0.02 m/s    (coeficiente de t)  
> c = 1.79 m      (término independiente)
> ```
> 
> **Ecuación experimental**: y = -5.08t² + 0.02t + 1.79
> 
> **Interpretación física**:
> 
> ```
> -½g = -5.08 → g = 10.16 m/s²
> v₀y = 0.02 m/s ≈ 0 (lanzamiento horizontal)
> h₀ = 1.79 m (altura inicial)
> ```
> 
> ### Análisis de Calidad:
> 
> **Coeficiente de determinación**: R² = 0.9990 **Residuos máximos**: ±0.02 m **Conclusión**: Excelente ajuste parabólico, confirma teoría

> [!warning]- **Cuidados en Análisis Parabólico** 📋
> 
> ### Problemas Comunes:
> 
> **1. Confusión con otros tipos de curva**:
> 
> - Exponenciales pueden parecer parabólicas en rangos limitados
> - Hipérbolas pueden simular parábolas cerca de extremos
> - Usar test de segundas diferencias constantes
> 
> **2. Truncamiento de datos**:
> 
> - Análisis incompleto puede perder el vértice
> - Parábolas requieren datos alrededor del extremo
> - Asimetría puede indicar modelo incompleto
> 
> **3. Orden del polinomio**:
> 
> - No todo ajuste cuadrático es físicamente válido
> - Términos de orden superior pueden mejorar R² sin significado
> - Principio de parsimonia: modelo más simple adecuado
> 
> **4. Interpretación de parámetros**:
> 
> - Vértice puede no tener significado físico directo
> - Extrapolación más allá de datos puede ser peligrosa
> - Verificar unidades de todos los coeficientes
> 
> ### Criterios de Validación:
> 
> **Para confirmar modelo parabólico**:
> 
> - R² > 0.95 en ajuste cuadrático
> - Segundas diferencias aproximadamente constantes
> - Residuos sin patrón sistemático
> - Parámetros con significado físico coherente
> - Comparación con teoría cuando disponible

## 📉 Gráficas Hiperbólicas

> [!info]- **Funciones Hiperbólicas Fundamentales** ∞
> 
> ### Formas Principales:
> 
> **1. Hipérbola Simple**:
> 
> ```
> y = a/x + b
> 
> Características:
> - Asíntota vertical: x = 0
> - Asíntota horizontal: y = b  
> - Comportamiento 1/x cerca del origen
> ```
> 
> **2. Hipérbola Desplazada**:
> 
> ```
> y = a/(x - h) + k
> 
> Parámetros:
> - (h, k): Centro de la hipérbola
> - a: Factor de escala y orientación
> - Asíntotas: x = h, y = k
> ```
> 
> **3. Hipérbola Cuadrática**:
> 
> ```
> y = a/x² + b
> 
> Características:
> - Decaimiento más rápido que 1/x
> - Siempre positiva si a > 0
> - Común en leyes de fuerzas
> ```
> 
> **4. Función Racional General**:
> 
> ```
> y = (ax + b)/(cx + d)
> 
> Asíntotas:
> - Vertical: x = -d/c
> - Horizontal: y = a/c (si grados iguales)
> - Oblicua: si numerador grado mayor
> ```
> 
> ### Características Distintivas:
> 
> **Asíntotas**:
> 
> - **Vertical**: Valores donde la función "explota"
> - **Horizontal**: Comportamiento para x → ±∞
> - **Oblicua**: Tendencia lineal en el infinito
> 
> **Comportamiento cerca de asíntotas**:
> 
> ```
> Cerca de x = 0 para y = a/x:
> - Si a > 0: y → +∞ cuando x → 0⁺, y → -∞ cuando x → 0⁻
> - Si a < 0: comportamiento opuesto
> ```
> 
> **Simetría**:
> 
> ```
> y = a/x es simétrica respecto al origen (rotación 180°)
> y = a/x² es simétrica respecto al eje y
> ```

> [!success] 🌌 Aplicaciones Físicas Hiperbólicas
> 
> ```mermaid
> graph TD
>     A[Fenómenos Hiperbólicos] --> B[Ley de Gravitación]
>     A --> C[Ley de Coulomb]
>     A --> D[Ley de Boyle]
>     A --> E[Intensidad de Radiación]
>     A --> F[Ley de Ohm Generalizada]
>     A --> G[Dispersión de Partículas]
>     
>     B --> B1["F = Gm₁m₂/r²"]
>     C --> C1["F = kq₁q₂/r²"]
>     D --> D1["PV = constante → P = k/V"]
>     E --> E1["I = I₀/r²"]
>     F --> F1["V = IR + r/I"]
>     G --> G1["σ ∝ 1/E²"]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5  
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#e0f2f1
> ```

> [!tip]- **Técnicas de Análisis Hiperbólico** 🔬
> 
> ### Identificación Visual:
> 
> **Señales características**:
> 
> - Curva pronunciada cerca del origen
> - Aplanamiento gradual hacia valores grandes
> - Asíntotas evidentes
> - Comportamiento "explosivo" en algún punto
> 
> ### Métodos de Linealización:
> 
> **1. Para y = a/x + b**:
> 
> ```
> Transformación: y vs 1/x
> Debe dar línea recta con:
> - Pendiente = a
> - Intercepto = b
> ```
> 
> **2. Para y = a/x²**:
> 
> ```
> Transformación: y vs 1/x²
> Debe dar línea recta con:
> - Pendiente = a
> - Intercepto = 0 (si no hay término constante)
> ```
> 
> **3. Para función racional**:
> 
> ```
> y = (ax + b)/(cx + d)
> 
> Reorganizar: y(cx + d) = ax + b
> → ycx + yd = ax + b
> → yx = (a - yc)/d + b/d
> 
> Gráfico: x vs y puede revelar linealidad
> ```
> 
> ### Test de Proporcionalidad Inversa:
> 
> **Para verificar y ∝ 1/x**:
> 
> ```
> Calcular producto xy para cada punto:
> Si xy ≈ constante → relación hiperbólica simple
> ```
> 
> **Para verificar y ∝ 1/x²**:
> 
> ```
> Calcular producto yx² para cada punto:
> Si yx² ≈ constante → relación cuadrática inversa
> ```
> 
> ### Determinación de Asíntotas:
> 
> **Asíntota horizontal**:
> 
> ```
> Analizar comportamiento para valores grandes de x
> y∞ = lim(x→∞) f(x)
> ```
> 
> **Asíntota vertical**:
> 
> ```
> Buscar valores donde y → ±∞
> Resolver denominador = 0
> ```

> [!example]- **Ejemplo: Ley de Gravitación Universal** 🌍
> 
> ### Experimento: Fuerza vs Distancia
> 
> **Situación**: Medición de fuerza gravitatoria entre dos masas **Ecuación teórica**: F = Gm₁m₂/r²
> 
> **Datos experimentales**:
> 
> ```
> r (m):  0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50
> F (N):  4.00, 1.78, 1.00, 0.64, 0.44, 0.25, 0.16
> ```
> 
> ### Identificación del Patrón:
> 
> **Test de proporcionalidad inversa cuadrática**:
> 
> ```
> Calcular Fr² para cada punto:
> 
> r=0.10: F×r² = 4.00×(0.10)² = 0.040
> r=0.15: F×r² = 1.78×(0.15)² = 0.040  
> r=0.20: F×r² = 1.00×(0.20)² = 0.040
> r=0.25: F×r² = 0.64×(0.25)² = 0.040
> r=0.30: F×r² = 0.44×(0.30)² = 0.040
> r=0.40: F×r² = 0.25×(0.40)² = 0.040
> r=0.50: F×r² = 0.16×(0.50)² = 0.040
> 
> → Fr² = 0.040 N·m² (constante) ✓
> ```
> 
> **Conclusión**: Comportamiento F ∝ 1/r² confirmado
> 
> ### Construcción de Gráfica Original:
> 
> **Gráfica F vs r**:
> 
> - **Forma**: Curva hiperbólica descendente
> - **Comportamiento**: Decaimiento rápido para r pequeño
> - **Asíntota**: F → 0 cuando r → ∞
> - **Curvatura**: Cóncava hacia arriba
> 
> ### Linealización:
> 
> **Transformación**: F vs 1/r² **Predicción**: Línea recta que pasa por el origen
> 
> **Datos transformados**:
> 
> ```
> 1/r² (m⁻²): 100,  44.4, 25.0, 16.0, 11.1, 6.25, 4.00
> F (N):      4.00, 1.78, 1.00, 0.64, 0.44, 0.25, 0.16
> ```
> 
> **Regresión lineal F vs 1/r²**:
> 
> ```
> Pendiente: m = 0.0400 N·m²
> Intercepto: b = 0.0001 N ≈ 0
> Correlación: r = 0.9999
> ```
> 
> **Ecuación experimental**: F = 0.0400/r²
> 
> ### Interpretación Física:
> 
> **Cálculo de Gm₁m₂**:
> 
> ```
> Pendiente = Gm₁m₂ = 0.0400 N·m²
> 
> Si m₁ = m₂ = 10 kg:
> G = 0.0400/(10×10) = 4.00×10⁻⁴ m³/(kg·s²)
> 
> Nota: Valor muy alto comparado con 
> G real = 6.67×10⁻¹¹ m³/(kg·s²)
> → Sugiere setup experimental o escala diferente
> ```
> 
> ### Análisis de Calidad:
> 
> **Excelente ajuste**:
> 
> - R² = 0.9998 (correlación casi perfecta)
> - Intercepto ≈ 0 (consistente con teoría)
> - Linealización perfecta confirma ley 1/r²

> [!warning]- **Precauciones en Análisis Hiperbólico** ⚠️
> 
> ### Problemas Experimentales:
> 
> **1. Mediciones cerca de asíntotas**:
> 
> - Errores relativos muy grandes cerca de x = 0
> - Instrumentos pueden saturarse
> - Considerar límites de validez del modelo
> 
> **2. Rango dinámico amplio**:
> 
> - Valores pueden variar por órdenes de magnitud
> - Considerar escalas logarítmicas para visualización
> - Ponderar adecuadamente en ajustes
> 
> **3. Identificación de asíntotas**:
> 
> - Asíntotas aparentes pueden ser artefactos
> - Verificar con teoría física
> - Distinguir entre asíntotas reales y aproximaciones
> 
> ### Errores de Interpretación:
> 
> **1. Extrapolación peligrosa**:
> 
> - Comportamiento hiperbólico puede cambiar fuera del rango
> - Límites físicos pueden invalidar la función
> - Efectos cuánticos, relativistas, etc.
> 
> **2. Confusión con exponenciales**:
> 
> - Para x grandes, exp(-ax) puede parecer 1/x
> - Usar tests de linealización apropiados
> - Verificar comportamiento en múltiples escalas
> 
> **3. Términos adicionales**:
> 
> - Funciones reales pueden tener correcciones
> - y = a/x + b/x² + c/x³ + ... (series de Laurent)
> - No asumir forma simple sin verificación
> 
> ### Mejores Prácticas:
> 
> **Para análisis robusto**:
> 
> - Medir en rango amplio de x
> - Usar gráficas doble-logarítmicas para identificación inicial
> - Verificar asíntotas experimentalmente cuando sea posible
> - Considerar incertidumbres ponderadas en ajustes
> - Comparar múltiples modelos hiperbólicos

## 🔄 Técnicas de Linealización Avanzadas

> [!info]- **Estrategias Generales de Linealización** 🎯
> 
> ### Principio Fundamental:
> 
> ```
> Objetivo: Transformar y = f(x) en Y = mX + b
> donde Y y X son funciones de y, x
> ```
> 
> ### Transformaciones Comunes:
> 
> |Función Original|Transformación|Gráfica Lineal|Parámetros|
> |---|---|---|---|
> |**y = ae^(bx)**|ln(y) vs x|Y = bX + ln(a)|m = b, c = ln(a)|
> |**y = ax^n**|ln(y) vs ln(x)|Y = nX + ln(a)|m = n, c = ln(a)|
> |**y = a/(x+b)**|1/y vs x|Y = (1/a)X + b/a|m = 1/a, c = b/a|
> |**y = ax² + bx + c**|y vs x²|Y = aX + (bx+c)|Ajuste múltiple|
> |**y = a + b/x**|y vs 1/x|Y = bX + a|m = b, c = a|
> |**y = ae^(-b/x)**|ln(y) vs 1/x|Y = -bX + ln(a)|m = -b, c = ln(a)|
> 
> ### Criterios de Selección:
> 
> **1. Análisis visual previo**:
> 
> - Forma general de la curva
> - Comportamiento en extremos
> - Presencia de asíntotas
> 
> **2. Contexto físico**:
> 
> - Leyes conocidas del fenómeno
> - Unidades dimensionales
> - Límites físicos esperados
> 
> **3. Calidad del ajuste**:
> 
> - Coeficiente de correlación tras linealización
> - Distribución de residuos
> - Significado físico de parámetros
> 
> ### Transformaciones Híbridas:
> 
> **Para funciones complejas**:
> 
> ```
> y = ae^(-bx) + c  →  ln(y-c) vs x
> y = a(1-e^(-bx)) →  ln(a/(a-y)) vs x  
> y = ax^n + b     →  Ajuste no lineal directo
> ```

> [!success] 🔧 Proceso Sistemático de Análisis
> 
> ```mermaid
> graph TD
>     A[Datos Experimentales] --> B[Inspección Visual]
>     B --> C{¿Patrón Evidente?}
>     
>     C -->|Lineal| D[Regresión Lineal Directa]
>     C -->|Exponencial| E["Transformación ln(y) vs x"]
>     C -->|Potencial| F["Transformación ln(y) vs ln(x)"]  
>     C -->|Parabólico| G[Regresión Cuadrática o y vs x²]
>     C -->|Hiperbólico| H[Transformación apropiada 1/x]
>     C -->|Incierto| I[Pruebas Múltiples]
>     
>     D --> J[Análisis de Residuos]
>     E --> J
>     F --> J  
>     G --> J
>     H --> J
>     I --> J
>     
>     J --> K{¿Ajuste Satisfactorio?}
>     K -->|Sí| L[Interpretación Física]
>     K -->|No| M[Modelo Más Complejo]
>     
>     M --> N[Funciones Híbridas]
>     M --> O[Análisis No Lineal]
>     M --> P[Revisión de Datos]
>     
>     style A fill:#e1f5fe
>     style L fill:#e8f5e8
>     style M fill:#ffebee
> ```

## 🎯 Ejemplos Integrales Multi-Tipo

> [!example]- **Análisis Comparativo: Oscilador Amortiguado** 📊
> 
> ### Situación Física:
> 
> **Sistema**: Péndulo con amortiguamiento viscoso **Ecuación teórica**: θ(t) = θ₀e^(-γt)cos(ωt + φ)
> 
> ### Datos Experimentales:
> 
> ```
> t (s):   0,    0.5,   1.0,   1.5,   2.0,   2.5,   3.0,   3.5,   4.0
> θ (°):  15.0,  10.4,  4.8,  -0.9,  -4.2,  -4.8,  -3.1,  -0.5,   1.8
> |θ|(°): 15.0,  10.4,  4.8,   0.9,   4.2,   4.8,   3.1,   0.5,   1.8
> ```
> 
> ### Análisis Tipo 1: Envolvente Exponencial
> 
> **Hipótesis**: La envolvente sigue |θ| = θ₀e^(-γt) **Identificación**:
> 
> - Picos de |θ| muestran decaimiento
> - Comportamiento típicamente exponencial
> 
> **Datos de picos** (aproximados):
> 
> ```
> t_pico (s): 0,    1.0,   2.5,   4.0
> |θ|_pico:  15.0, 4.8,   4.8,   1.8
> ```
> 
> **Linealización**: ln(|θ|) vs t
> 
> ```
> t (s):      0,    1.0,   2.5,   4.0
> ln(|θ|):   2.71, 1.57,  1.57,  0.59
> ```
> 
> **Regresión lineal**:
> 
> ```
> Pendiente: m = -0.53 s⁻¹  
> Intercepto: b = 2.71
> → γ = 0.53 s⁻¹, θ₀ = e^2.71 = 15.0°
> ```
> 
> ### Análisis Tipo 2: Frecuencia de Oscilación
> 
> **Identificación de período**:
> 
> - Ceros aproximados en t = 1.5, 3.5 s
> - Período aparente T ≈ 2.0 s
> - Frecuencia angular ω = 2π/T ≈ 3.14 rad/s
> 
> ### Modelo Completo:
> 
> **Ecuación ajustada**: θ(t) = 15.0·e^(-0.53t)cos(3.14t) **Validación**:
> 
> - Comportamiento exponencial en envolvente ✓
> - Oscilación con período correcto ✓
> - Valores iniciales consistentes ✓
> 
> ### Interpretación Física:
> 
> **Parámetros del sistema**:
> 
> ```
> Factor de amortiguamiento: γ = 0.53 s⁻¹
> Frecuencia natural amortiguada: ω = 3.14 rad/s
> Tiempo de relajación: τ = 1/γ = 1.89 s
> ```

> [!example]- **Estudio de Caso: Ley de Enfriamiento de Newton** 🌡️
> 
> ### Experimento: Enfriamiento de Agua Caliente
> 
> **Situación**: Taza de agua caliente enfriándose al ambiente **Ecuación teórica**: T(t) = T∞ + (T₀ - T∞)e^(-kt)
> 
> ### Datos Experimentales:
> 
> ```
> t (min):  0,   5,   10,  15,  20,  25,  30,  35,  40
> T (°C):  85.0, 76.2, 68.8, 62.7, 57.8, 54.1, 51.2, 49.0, 47.5
> T_amb = 22.0°C (constante)
> ```
> 
> ### Identificación del Patrón:
> 
> **Análisis visual**:
> 
> - Decrecimiento rápido inicial, luego gradual
> - Tendencia hacia temperatura ambiente
> - Curvatura típicamente exponencial
> 
> **Test de razones**: (T(i) - T∞)/(T(i+1) - T∞)
> 
> ```
> (85-22)/(76.2-22) = 63/54.2 = 1.16
> (76.2-22)/(68.8-22) = 54.2/46.8 = 1.16  
> (68.8-22)/(62.7-22) = 46.8/40.7 = 1.15
> 
> → Razón aproximadamente constante ≈ 1.16
> → Factor de decaimiento por cada 5 min
> ```
> 
> ### Linealización:
> 
> **Transformación**: ln(T - T∞) vs t **Datos transformados**:
> 
> ```
> t (min):     0,   5,    10,   15,   20,   25,   30,   35,   40
> T-T∞ (°C):  63,  54.2, 46.8, 40.7, 35.8, 32.1, 29.2, 27.0, 25.5
> ln(T-T∞):  4.14, 3.99, 3.85, 3.71, 3.58, 3.47, 3.37, 3.30, 3.24
> ```
> 
> **Regresión lineal ln(T-T∞) vs t**:
> 
> ```
> Pendiente: m = -0.0225 min⁻¹
> Intercepto: b = 4.143  
> Correlación: r = -0.9994
> ```
> 
> **Parámetros físicos**:
> 
> ```
> k = 0.0225 min⁻¹ = 3.75×10⁻⁴ s⁻¹
> T₀ - T∞ = e^4.143 = 63.0°C
> → T₀ = 63.0 + 22.0 = 85.0°C ✓
> ```
> 
> ### Ecuación Final:
> 
> **Modelo experimental**: T(t) = 22.0 + 63.0·e^(-0.0225t) **Validación**:
> 
> - Excelente correlación (r > 0.999)
> - Parámetros físicamente consistentes
> - Comportamiento asintótico correcto
> 
> ### Predicciones:
> 
> **Tiempo para alcanzar temperatura específica**:
> 
> ```
> Para T = 30°C:
> 30 = 22 + 63·e^(-0.0225t)
> 8 = 63·e^(-0.0225t)
> t = -ln(8/63)/0.0225 = 93.7 min
> ```
> 
> **Constante de tiempo**: τ = 1/k = 44.4 min

## 📈 Criterios de Selección de Modelos

> [!info]- **Evaluación Comparativa de Modelos** ⚖️
> 
> ### Criterios Estadísticos:
> 
> **1. Coeficiente de Determinación (R²)**:
> 
> ```
> R² = 1 - SS_residual/SS_total
> 
> Interpretación:
> R² > 0.95: Excelente ajuste
> 0.85 < R² ≤ 0.95: Buen ajuste  
> 0.70 < R² ≤ 0.85: Ajuste moderado
> R² ≤ 0.70: Ajuste pobre
> ```
> 
> **2. Error Cuadrático Medio (RMSE)**:
> 
> ```
> RMSE = √[Σ(y_i - ŷ_i)²/n]
> 
> - Mismas unidades que los datos
> - Menor RMSE indica mejor ajuste
> - Compara modelos en misma escala
> ```
> 
> **3. Criterio de Información de Akaike (AIC)**:
> 
> ```
> AIC = n·ln(SS_residual/n) + 2k
> 
> donde k = número de parámetros
> - Penaliza complejidad del modelo
> - Menor AIC indica mejor balance ajuste/simplicidad
> ```
> 
> ### Criterios Físicos:
> 
> **1. Consistencia dimensional**:
> 
> - Todos los términos deben tener unidades coherentes
> - Parámetros con significado físico interpretable
> - Verificar escalas típicas del fenómeno
> 
> **2. Comportamiento límite**:
> 
> - Comportamiento para x → 0, x → ∞
> - Consistencia con leyes físicas conocidas
> - Límites físicos realistas
> 
> **3. Simplicidad (Navaja de Occam)**:
> 
> - Preferir modelo más simple que explique datos
> - Evitar sobreajuste con muchos parámetros
> - Capacidad predictiva sobre complejidad

> [!warning]- **Errores Comunes en Selección de Modelos** ❌
> 
> ### Problemas Frecuentes:
> 
> **1. Sobreajuste**:
> 
> - R² alto pero modelo no generaliza
> - Muchos parámetros para pocos datos
> - Ajuste perfecto a ruido experimental
> 
> **2. Selección basada solo en R²**:
> 
> - R² siempre mejora añadiendo parámetros
> - Ignorar significado físico
> - No considerar complejidad del modelo
> 
> **3. Extrapolación inadecuada**:
> 
> - Usar modelo fuera del rango de datos
> - Asumir validez universal del ajuste
> - Ignorar límites físicos del fenómeno
> 
> **4. Confusión de escalas**:
> 
> - Lo que parece exponencial puede ser potencial
> - Efectos de escala logarítmica en visualización
> - Rangos limitados pueden engañar
> 
> ### Mejores Prácticas:
> 
> **Validación cruzada**:
> 
> - Dividir datos en entrenamiento y validación
> - Verificar capacidad predictiva
> - Usar múltiples métricas de evaluación
> 
> **Análisis de residuos**:
> 
> - Patrones sistemáticos indican modelo inadecuado
> - Distribución normal de residuos ideal
> - Homocedasticidad (varianza constante)
> 
> **Comparación múltiple**:
> 
> - Probar varios modelos candidatos
> - Usar criterios de selección robustos
> - Considerar conocimiento físico previo

## 🔧 Herramientas Computacionales Avanzadas

> [!info]- **Software para Análisis No Lineal** 💻
> 
> ### Plataformas Principales:
> 
> |Software|Fortalezas|Análisis No Lineal|Costo|
> |---|---|---|---|
> |**Python (SciPy)**|Flexible, código abierto|scipy.optimize.curve_fit|Gratuito|
> |**R**|Estadística avanzada|nls(), nlme()|Gratuito|
> |**MATLAB**|Numérico potente|fit(), fittype()|Comercial|
> |**Origin**|Interface gráfica|Wizard de ajuste|Comercial|
> |**Mathematica**|Simbólico + numérico|FindFit[], NonlinearModelFit[]|Comercial|
> |**Excel**|Accesible|Solver add-in|Comercial|
> 
> ### Ejemplo Python para Ajuste Exponencial:
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> from scipy.optimize import curve_fit
> 
> # Función modelo
> def exponential(x, a, b, c):
>     return a * np.exp(b * x) + c
> 
> # Datos experimentales
> x_data = np.array([0, 1, 2, 3, 4, 5])
> y_data = np.array([1.1, 2.7, 7.1, 18.6, 50.2, 135.8])
> 
> # Ajuste
> popt, pcov = curve_fit(exponential, x_data, y_data)
> 
> # Parámetros e incertidumbres
> a_fit, b_fit, c_fit = popt
> uncertainties = np.sqrt(np.diag(pcov))
> 
> # R²
> y_pred = exponential(x_data, *popt)
> ss_res = np.sum((y_data - y_pred) ** 2)
> ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)
> r_squared = 1 - (ss_res / ss_tot)
> 
> print(f"Parámetros: a={a_fit:.3f}±{uncertainties[0]:.3f}")
> print(f"           b={b_fit:.3f}±{uncertainties[1]:.3f}")  
> print(f"           c={c_fit:.3f}±{uncertainties[2]:.3f}")
> print(f"R² = {r_squared:.4f}")
> ```

## 📚 Referencias y Conexiones

> [!quote]- **Notas Relacionadas**
> 
> - [[Gráficas Lineales]] - Fundamento previo necesario
> - [[Estadística Básica]] - Base matemática
> - [[Incertidumbres Experimentales]] - Análisis de errores
> - [[Regresión No Lineal]] - Técnicas avanzadas
> - [[Análisis Dimensional]] - Verificación física

## 🎯 Ejercicios y Problemas

> [!example]- **Problema Integral: Identificación de Patrón Desconocido** 🔍
> 
> ### Datos Misteriosos:
> 
> Un estudiante obtiene los siguientes datos de un experimento no especificado:
> 
> ```
> x:  1.0,  1.5,  2.0,  2.5,  3.0,  3.5,  4.0,  4.5,  5.0
> y:  2.45, 1.63, 1.22, 0.98, 0.82, 0.70, 0.61, 0.54, 0.49
> ```
> 
> ### Tareas:
> 
> 1. **Identificación visual del patrón**
> 2. **Tests de linealización múltiples**
> 3. **Selección del mejor modelo**
> 4. **Determinación de parámetros**
> 5. **Interpretación física posible**
> 
> ### Guía de Solución:
> 
> **Paso 1: Análisis visual**
> 
> - Gráfica y vs x muestra decaimiento
> - Curvatura suave, cóncava hacia arriba
> - Sin asíntotas evidentes en el rango
> 
> **Paso 2: Tests de proporcionalidad**
> 
> ```
> Test xy:     2.45, 2.45, 2.44, 2.45, 2.46, 2.45, 2.44, 2.43, 2.45
> Test x²y:    2.45, 3.67, 4.88, 6.13, 7.38, 8.58, 9.76, 10.94, 12.25  
> Test xy²:    6.00, 3.99, 2.98, 2.40, 2.02, 1.72, 1.49, 1.32, 1.20
> ```
> 
> **Conclusión**: xy ≈ constante → **y ∝ 1/x** (hiperbólica simple)
> 
> **Paso 3: Linealización**
> 
> ```
> Gráfica: y vs 1/x
> Debe dar línea recta
> ```
> 
> **Resultado esperado**: y = 2.45/x con R² > 0.99

## 📝 Resumen y Puntos Clave

> [!summary]- **Conceptos Fundamentales** 📋
> 
> ### Tipos Principales de Gráficas No Lineales:
> 
> 1. **Exponenciales**: y = ae^(bx)
>     - Crecimiento/decaimiento acelerado
>     - Linealización: ln(y) vs x
>     - Aplicaciones: Radioactividad, circuitos RC, poblaciones
> 2. **Parabólicas**: y = ax² + bx + c
>     - Un extremo (máximo o mínimo)
>     - Simetría característica
>     - Aplicaciones: Movimiento bajo gravedad, energías
> 3. **Hiperbólicas**: y = a/x^n
>     - Decaimiento hacia asíntotas
>     - Comportamiento 1/x característico
>     - Aplicaciones: Fuerzas fundamentales, leyes de gases
> 
> ### Estrategias de Análisis:
> 
> - **Identificación visual** → **Tests cuantitativos** → **Linealización** → **Validación**
> - Usar múltiples criterios de selección (R², AIC, significado físico)
> - Verificar comportamientos límite y dimensiones
> - Análisis de residuos para confirmar adecuación del modelo

---

**Tags:** #graficas-no-lineales #exponencial #parabólica #hiperbólica #linealización #identificación-patrones #análisis-curvas #fisica-experimental #modelado-no-lineal #ajuste-curvas
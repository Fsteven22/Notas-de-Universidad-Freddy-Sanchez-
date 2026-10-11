---
dg-publish: true
---

# Derivadas Parciales

> [!quote] "En el mundo de las magnitudes físicas, cada variable cuenta su propia historia de cambio." 📐

> [!info] Las derivadas parciales son herramientas matemáticas fundamentales para entender cómo cambian las magnitudes físicas cuando varía una sola variable, manteniendo todas las demás constantes. En física experimental, son esenciales para la propagación de incertidumbres y el análisis de sensibilidad en mediciones.

## 🔧 Conceptos Fundamentales

> [!info] **Definición Matemática** 📊
> 
> ### Concepto Central:
> 
> Para una función z = f(x, y), la **derivada parcial** con respecto a x es:
> 
> 
> $∂z/∂x = lim[h→0] [f(x+h, y) - f(x, y)]/h$
> 
> 
> **Interpretación física**: Tasa de cambio de z cuando x varía, manteniendo y constante.
> 
> ### Notación Estándar:
> 
> |Notación|Significado|Contexto|
> |---|---|---|
> |∂f/∂x|Derivada parcial de f respecto a x|General|
> |f_x|Notación subíndice|Matemáticas|
> |∂z/∂x|Cambio de z por cambio en x|Física|
> |df/dx\|_{y=cte}|Derivada manteniendo y constante|Termodinámica|
> 
> ### Diferencias con Derivadas Ordinarias:
> 
> |Aspecto|Derivada Ordinaria|Derivada Parcial|
> |---|---|---|
> |**Variables**|Una sola: f(x)|Múltiples: f(x,y,z,...)|
> |**Símbolo**|d/dx|∂/∂x|
> |**Interpretación**|Tasa de cambio total|Tasa de cambio con otras variables fijas|
> |**Resultado**|Función de x|Función de todas las variables|

> [!tip] **Reglas de Derivación Parcial** ⚡
> 
> ### Reglas Básicas:
> 
> **Regla de la constante**:
> 
> ```
> Si z = c (constante), entonces ∂z/∂x = 0
> ```
> 
> **Regla de la potencia**:
> 
> ```
> Si z = x^n, entonces ∂z/∂x = nx^(n-1)
> ```
> 
> **Regla del producto**:
> 
> ```
> Si z = f(x,y)·g(x,y), entonces:
> ∂z/∂x = (∂f/∂x)·g + f·(∂g/∂x)
> ```
> 
> **Regla de la cadena**:
> 
> ```
> Si z = f(u,v) donde u=u(x,y) y v=v(x,y), entonces:
> ∂z/∂x = (∂f/∂u)·(∂u/∂x) + (∂f/∂v)·(∂v/∂x)
> ```
> 
> ### Casos Especiales en Física:
> 
> |Función|Derivada Parcial ∂f/∂x|Aplicación Física|
> |---|---|---|
> |f = x + y|∂f/∂x = 1|Suma de longitudes|
> |f = xy|∂f/∂x = y|Área rectangular|
> |f = x/y|∂f/∂x = 1/y|Velocidad v = d/t|
> |f = x²|∂f/∂x = 2x|Energía cuadrática|
> |f = √x|∂f/∂x = 1/(2√x)|Período de péndulo|
> |f = e^x|∂f/∂x = e^x|Decaimiento exponencial|
> |f = sin(x)|∂f/∂x = cos(x)|Movimiento oscilatorio|
> |f = ln(x)|∂f/∂x = 1/x|Escalas logarítmicas|

> [!warning] **Interpretación Geométrica** 📐
> 
> ### Visualización 3D:
> 
> Para z = f(x, y), la superficie en el espacio 3D:
> 
> - **∂z/∂x**: Pendiente de la curva al cortar la superficie con un plano y = constante
> - **∂z/∂y**: Pendiente de la curva al cortar la superficie con un plano x = constante
> 
> ### Analogía Física:
> 
> **Montaña topográfica**:
> 
> - **z**: Altitud en cada punto
> - **∂z/∂x**: Pendiente hacia el este/oeste
> - **∂z/∂y**: Pendiente hacia el norte/sur
> - **∇z**: Vector gradiente (dirección de máxima pendiente)
> 
> ### Curvas de Nivel:
> 
> Las curvas donde f(x,y) = constante son perpendiculares al gradiente:
> 
> ```
> ∇f = (∂f/∂x, ∂f/∂y)
> ```

> [!success] 🔗 Algoritmo de Cálculo
> 
> ```mermaid
> graph TD
>     A["Identificar la función f(x,y,z,...)"] --> B[Seleccionar variable de derivación]
>     B --> C[Tratar otras variables como constantes]
>     C --> D[Aplicar reglas de derivación ordinaria]
>     D --> E[Simplificar expresión resultante]
>     E --> F[Verificar dimensiones físicas]
>     F --> G[Evaluar en punto específico si es necesario]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#e0f2f1
> ```

## 🎯 Derivadas Parciales en Física

> [!note] **Aplicaciones en Mecánica** 🏗️
> 
> ### Cinemática:
> 
> **Posición en 2D**: r(t) = (x(t), y(t))
> 
> ```
> Velocidad: v_x = ∂x/∂t, v_y = ∂y/∂t
> Aceleración: a_x = ∂²x/∂t², a_y = ∂²y/∂t²
> ```
> 
> **Movimiento projectil**: x = v₀ₓt, y = v₀ᵧt - ½gt²
> 
> ```
> ∂x/∂t = v₀ₓ (velocidad horizontal constante)
> ∂y/∂t = v₀ᵧ - gt (velocidad vertical variable)
> ```
> 
> ### Dinámica:
> 
> **Energía cinética**: K = ½m(vₓ² + vᵧ²)
> 
> ```
> ∂K/∂vₓ = mvₓ (momento en x)
> ∂K/∂vᵧ = mvᵧ (momento en y)
> ```
> 
> **Fuerza conservativa**: F = -∇U
> 
> ```
> Fₓ = -∂U/∂x, Fᵧ = -∂U/∂y, F_z = -∂U/∂z
> ```
> 
> ### Trabajo y Energía:
> 
> **Potencia**: P = \vec{F} · \vec{v}
> 
> ```
> ∂P/∂v = F (fuerza en dirección del movimiento)
> ```
> 
> **Energía potencial gravitacional**: U = mgh(x,y)
> 
> ```
> Fₓ = -mg(∂h/∂x), Fᵧ = -mg(∂h/∂y)
> ```

> [!tip] **Propagación de Incertidumbres** 📊
> 
> ### Fórmula General:
> 
> Para z = f(x, y, ...), la incertidumbre se propaga como:
> 
> 
> $u_z = √[(∂f/∂x)² · u_x² + (∂f/∂y)² · u_y² + ...]$
> 
> 
> ### Coeficientes de Sensibilidad:
> 
> Los términos (∂f/∂x) se llaman **coeficientes de sensibilidad**:
> 
> - **Magnitud**: Indica cuánto afecta un cambio en x al resultado
> - **Signo**: Indica si la relación es directa (+) o inversa (-)
> 
> ### Análisis de Dominancia:
> 
> La contribución de cada variable a la incertidumbre total:
> 
> ```
> Contribución de x: C_x = (∂f/∂x)² · u_x²
> Porcentaje: %C_x = (C_x / u_z²) × 100%
> ```
> 
> **Estrategia experimental**: Concentrar esfuerzos en reducir las incertidumbres que más contribuyen.

## 📚 Ejemplos Detallados

> [!example] **Ejemplo 1: Área de un Rectángulo** 📐
> 
> ### Función:
> 
> A = xy (área = largo × ancho)
> 
> ### Derivadas Parciales:
> 
> ```
> ∂A/∂x = y (cambio de área por cambio en largo)
> ∂A/∂y = x (cambio de área por cambio en ancho)
> ```
> 
> ### Interpretación Física:
> 
> - **∂A/∂x = y**: Si el largo aumenta 1 unidad, el área aumenta en y unidades
> - **∂A/∂y = x**: Si el ancho aumenta 1 unidad, el área aumenta en x unidades
> 
> ### Aplicación Numérica:
> 
> Para x = 5 m, y = 3 m:
> 
> - A = 15 m²
> - ∂A/∂x = 3 m (sensibilidad al largo)
> - ∂A/∂y = 5 m (sensibilidad al ancho)
> 
> **Conclusión**: El área es más sensible a cambios en el ancho que en el largo.
> 
> ### Propagación de Incertidumbres:
> 
> Si u_x = 0.1 m y u_y = 0.05 m:
> 
> ```
> u_A = √[(∂A/∂x)² · u_x² + (∂A/∂y)² · u_y²]
> u_A = √[(3)² · (0.1)² + (5)² · (0.05)²]
> u_A = √[0.09 + 0.0625] = 0.39 m²
> ```

> [!example] **Ejemplo 2: Velocidad (División)** 🚗
> 
> ### Función:
> 
> v = d/t (velocidad = distancia / tiempo)
> 
> ### Derivadas Parciales:
> 
> ```
> ∂v/∂d = 1/t (sensibilidad a la distancia)
> ∂v/∂t = -d/t² (sensibilidad al tiempo)
> ```
> 
> ### Interpretación Física:
> 
> - **∂v/∂d = 1/t > 0**: La velocidad aumenta con la distancia
> - **∂v/∂t = -d/t² < 0**: La velocidad disminuye con el tiempo
> 
> ### Análisis de Sensibilidad:
> 
> Para d = 100 m, t = 10 s (v = 10 m/s):
> 
> - ∂v/∂d = 0.1 s⁻¹
> - ∂v/∂t = -1.0 m/s²
> 
> **Observación**: |∂v/∂t| >> |∂v/∂d|, la velocidad es más sensible al tiempo.
> 
> ### Propagación de Incertidumbres:
> 
> Si u_d = 1 m y u_t = 0.1 s:
> 
> ```
> u_v = √[(0.1)² · (1)² + (-1.0)² · (0.1)²]
> u_v = √[0.01 + 0.01] = 0.14 m/s
> ```
> 
> **Contribuciones**:
> 
> - Distancia: 50%
> - Tiempo: 50%

> [!example] **Ejemplo 3: Densidad de un Cilindro** ⚖️
> 
> ### Función:
> 
> ρ = m/(πr²h) (densidad = masa / volumen)
> 
> ### Derivadas Parciales:
> 
> ```
> ∂ρ/∂m = 1/(πr²h)
> ∂ρ/∂r = -2m/(πr³h)
> ∂ρ/∂h = -m/(πr²h²)
> ```
> 
> ### Interpretación Física:
> 
> - **∂ρ/∂m > 0**: La densidad aumenta con la masa
> - **∂ρ/∂r < 0**: La densidad disminuye con el radio (volumen crece como r²)
> - **∂ρ/∂h < 0**: La densidad disminuye con la altura
> 
> ### Cálculo Numérico:
> 
> Para m = 100 g, r = 2 cm, h = 5 cm:
> 
> - ρ = 100/(π × 4 × 5) = 1.59 g/cm³
> - ∂ρ/∂m = 1/(20π) = 0.0159 cm³/g
> - ∂ρ/∂r = -200/(40π) = -1.59 g/cm⁴
> - ∂ρ/∂h = -100/(20π) = -0.318 g/cm⁵
> 
> ### Análisis de Sensibilidad:
> 
> Con incertidumbres u_m = 1 g, u_r = 0.1 cm, u_h = 0.1 cm:
> 
> ```
> C_m = (0.0159)² × (1)² = 2.53 × 10⁻⁴
> C_r = (-1.59)² × (0.1)² = 0.0253
> C_h = (-0.318)² × (0.1)² = 0.00101
> ```
> 
> **Dominancia**: Radio >> Altura >> Masa
> 
> **Recomendación**: Concentrar esfuerzos en medir el radio con mayor precisión.

## 🧮 Técnicas de Cálculo

> [!tip] **Estrategias de Memorización** 🎯
> 
> ### Mnemotecnia: "DERIVAR"
> 
> **D**eterminar la función f(x,y,...) **E**legir la variable de derivación **R**econocer constantes (otras variables) **I**dentificar reglas aplicables **V**erificar dimensiones físicas **A**plicar en punto específico si es necesario **R**evisar el resultado físicamente
> 
> ### Patrones Comunes:
> 
> |Tipo de función|Patrón|Ejemplo|
> |---|---|---|
> |**Lineal**|∂(ax + by)/∂x = a|Suma de medidas|
> |**Producto**|∂(xy)/∂x = y|Áreas, volúmenes|
> |**Cociente**|∂(x/y)/∂x = 1/y|Velocidades, densidades|
> |**Potencia**|∂(x^n)/∂x = nx^(n-1)|Energías cuadráticas|
> |**Exponencial**|∂(e^x)/∂x = e^x|Decaimientos|
> |**Logarítmica**|∂(ln x)/∂x = 1/x|Escalas log|

> [!note] **Verificaciones Útiles** ✅
> 
> ### Análisis Dimensional:
> 
> La derivada parcial ∂f/∂x debe tener unidades [f]/[x]:
> 
> ```
> Si f está en [m²] y x en [m], entonces ∂f/∂x está en [m²]/[m] = [m]
> ```
> 
> ### Comportamiento Límite:
> 
> - **x → 0**: ¿Qué ocurre con ∂f/∂x?
> - **x → ∞**: ¿Se vuelve despreciable?
> - **Signos**: ¿Son consistentes con la física?
> 
> ### Simetría:
> 
> Si f(x,y) = f(y,x), entonces ∂f/∂x|_{x=y} = ∂f/∂y|_{x=y}
> 
> ### Casos Especiales:
> 
> - **Variables independientes**: Solo una derivada no nula
> - **Funciones separables**: f(x,y) = g(x)h(y)
> - **Homogeneidad**: Verificar usando teorema de Euler

## ⚡ Derivadas de Orden Superior

> [!info] **Derivadas Mixtas y Segundas** 📈
> 
> ### Derivadas Segundas:
> 
> **Notación**:
> 
> ```
> ∂²f/∂x² = f_xx (derivada segunda respecto a x)
> ∂²f/∂y² = f_yy (derivada segunda respecto a y)
> ```
> 
> **Interpretación física**: Curvatura o aceleración en cada dirección.
> 
> ### Derivadas Mixtas:
> 
> **Definición**:
> 
> ```
> ∂²f/∂x∂y = ∂/∂x(∂f/∂y) = ∂/∂y(∂f/∂x)
> ```
> 
> **Teorema de Schwarz**: Si f es suave, entonces:
> 
> ```
> ∂²f/∂x∂y = ∂²f/∂y∂x
> ```
> 
> ### Aplicaciones Físicas:
> 
> **Aceleración**: a = ∂v/∂t = ∂²x/∂t² **Curvatura espacial**: Describes cómo cambia la pendiente **Interacciones cruzadas**: Cómo una variable afecta la sensibilidad a otra

## 🌊 Aplicaciones Avanzadas

> [!info] **Gradiente y Campos Vectoriales** 🧭
> 
> ### Vector Gradiente:
> 
> ```
> ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)
> ```
> 
> **Propiedades**:
> 
> - Apunta en la dirección de máximo crecimiento
> - Magnitud indica la tasa máxima de cambio
> - Perpendicular a las curvas de nivel
> 
> ### Campos Conservativos:
> 
> Una fuerza \vec{F} es conservativa si:
> 
> ```
> \vec{F} = -∇U (derivado de un potencial U)
> ```
> 
> ### Aplicaciones:
> 
> - **Campo gravitacional**: \vec{g} = -∇Φ
> - **Campo eléctrico**: \vec{E} = -∇V
> - **Fuerza elástica**: \vec{F} = -∇U_elástica

> [!info] **Optimización y Puntos Críticos** 🎯
> 
> ### Condiciones para Extremos:
> 
> Un punto (x₀, y₀) es crítico si:
> 
> ```
> ∂f/∂x|_(x₀,y₀) = 0  y  ∂f/∂y|_(x₀,y₀) = 0
> ```
> 
> ### Clasificación (usando Hessiano):
> 
> ```
> H = |∂²f/∂x²    ∂²f/∂x∂y|
>     |∂²f/∂y∂x   ∂²f/∂y² |
> ```
> 
> - **det(H) > 0 y ∂²f/∂x² > 0**: Mínimo local
> - **det(H) > 0 y ∂²f/∂x² < 0**: Máximo local
> - **det(H) < 0**: Punto de silla
> 
> ### Aplicaciones Físicas:
> 
> - **Equilibrio estable**: Mínimo de energía potencial
> - **Equilibrio inestable**: Máximo de energía potencial
> - **Puntos de silla**: Equilibrios neutrales

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir ∂ con d**:
>     - ❌ ∂f/∂x para funciones de una variable
>     - ✅ df/dx para f(x), ∂f/∂x para f(x,y,...)
> 2. **No mantener variables constantes**:
>     - ❌ Derivar tratando y como función de x
>     - ✅ Tratar y como constante al derivar respecto a x
> 3. **Errores de signo**:
>     - ❌ ∂(x/y)/∂y = x/y²
>     - ✅ ∂(x/y)/∂y = -x/y²
> 4. **Unidades inconsistentes**:
>     - Verificar siempre [∂f/∂x] = [f]/[x]
> 5. **Aplicar reglas incorrectas**:
>     - Usar regla del producto cuando no aplica
>     - Olvidar la regla de la cadena
> 6. **Interpretación física errónea**:
>     - No relacionar el resultado con el fenómeno físico
>     - Ignorar el significado del signo

## 🎯 Aplicaciones Específicas en Laboratorio

> [!info] **Experimentos Típicos** 🔬
> 
> ### Péndulo Simple:
> 
> **Período**: T = 2π√(L/g)
> 
> ```
> ∂T/∂L = π/√(Lg) (sensibilidad a la longitud)
> ∂T/∂g = -π√(L)/g^(3/2) (sensibilidad a g)
> ```
> 
> **Análisis**: T es más sensible a cambios en g que en L.
> 
> ### Caída Libre:
> 
> **Posición**: y = y₀ + v₀t - ½gt²
> 
> ```
> ∂y/∂y₀ = 1 (posición inicial)
> ∂y/∂v₀ = t (velocidad inicial)
> ∂y/∂t = v₀ - gt (velocidad instantánea)
> ∂y/∂g = -½t² (efecto gravitacional)
> ```
> 
> ### Ley de Hooke:
> 
> **Fuerza**: F = kx
> 
> ```
> ∂F/∂k = x (cambio por rigidez)
> ∂F/∂x = k (cambio por desplazamiento)
> ```
> 
> ### Resistencia de Materiales:
> 
> **Esfuerzo**: σ = F/A
> 
> ```
> ∂σ/∂F = 1/A (sensibilidad a la fuerza)
> ∂σ/∂A = -F/A² (sensibilidad al área)
> ```

## 📖 Referencias y Conexiones

> [!quote] **Notas Relacionadas**
> 
> - [[Incertidumbres Experimentales]] - Aplicación principal
> - [[Análisis de Errores]] - Contexto experimental
> - [[Cálculo Vectorial]] - Extensiones matemáticas
> - [[Optimización]] - Aplicaciones avanzadas

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Funciones de Varias Variables]] - Concepto base
> - **Cálculo diferencial**: Derivadas ordinarias
> - **Álgebra**: Operaciones básicas

> [!note] **Temas Siguientes**
> 
> - [[Incertidumbres Experimentales]] - Aplicación directa
> - [[Análisis Gráfico]] - Representación visual
> - [[Optimización en Física]] - Aplicaciones avanzadas

---

**Tags:** #derivadas-parciales #calculo-multivariable #propagacion-incertidumbres #analisis-matematico #fisica-matematica #sensibilidad #gradiente #optimizacion #laboratorio
# Integrales en Coordenadas Polares

>[!quote] *"Cuando las curvas danzan en círculos y espirales, el lenguaje cartesiano se vuelve torpe. Las coordenadas polares nos ofrecen la gracia natural para describir el mundo circular, transformando integrales complejas en elegantes expresiones radiales."*

> [!info]+ Fundamentos de Coordenadas Polares 🌀
> ### Sistema de Coordenadas Polares
> Un punto en el plano se describe mediante:
> - **Radio** $r \geq 0$: distancia al origen
> - **Ángulo** $\theta$: medido desde el eje x positivo
> 
> ### Transformación entre Sistemas
> **Polares → Cartesianas:**
> $$\begin{cases}
> x = r\cos\theta \\
> y = r\sin\theta
> \end{cases}$$
> 
> **Cartesianas → Polares:**
> $$\begin{cases}
> r = \sqrt{x^2 + y^2} \\
> \theta = \arctan\left(\frac{y}{x}\right)
> \end{cases}$$
> 
> ### Jacobiano de la Transformación
> **$$J = \left|\frac{\partial(x,y)}{\partial(r,\theta)}\right| = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r$$**

> [!note]- Elemento Diferencial de Área 📐
> ### Deducción del Elemento de Área
> ```mermaid
> graph TB
>     A[Sector Circular Infinitesimal] --> B[Dimensiones del Sector]
>     B --> C["Δr × rΔθ"]
>     C --> D[Elemento de Área: dA = r dr dθ]
>     
>     E[Visualización] --> F["┌─────┐ <- r + dr"]
>     F --> G["│ ░░░ │"]
>     G --> H["│░░░ │ <- altura ≈ r"]  
>     H --> I["└─────┘ <- r"]
>     I --> J["↖─ dθ ─↗"]
>     
>     style A fill:#e8f5e8
>     style D fill:#c8e6c9
>     style E fill:#e1f5fe
> ```
> 
> ### Construcción del Sector Circular
> **Consideremos un sector circular infinitesimal:**
> - **Radio interior**: $r$
> - **Radio exterior**: $r + dr$  
> - **Ángulo**: $d\theta$
> 
> **Dimensiones aproximadas:**
> - **Anchura radial**: $dr$
> - **Altura tangencial**: $r \cdot d\theta$ (longitud del arco)
> 
> **Por tanto:**
> $$dA = \text{anchura} \times \text{altura} = dr \times (r \cdot d\theta) = r \, dr \, d\theta$$

> [!tip]- Integral Doble en Coordenadas Polares 🔄
> ### Fórmula General
> **Para una función $f(x,y) = f(r\cos\theta, r\sin\theta) = g(r,\theta)$:**
> 
> **$$\iint_R f(x,y) \, dA = \iint_R g(r,\theta) \cdot r \, dr \, d\theta$$**
> 
> ### Regiones Típicas en Coordenadas Polares
> 
> **1. Región Polar Simple:**
> $$R = \{(r,\theta) : \alpha \leq \theta \leq \beta, \, 0 \leq r \leq h(\theta)\}$$
> 
> **$$\iint_R f(x,y) \, dA = \int_{\alpha}^{\beta} \int_0^{h(\theta)} g(r,\theta) \cdot r \, dr \, d\theta$$**
> 
> **2. Corona Circular:**
> $$R = \{(r,\theta) : 0 \leq \theta \leq 2\pi, \, r_1 \leq r \leq r_2\}$$
> 
> **$$\iint_R f(x,y) \, dA = \int_0^{2\pi} \int_{r_1}^{r_2} g(r,\theta) \cdot r \, dr \, d\theta$$**
> 
> **3. Sector Circular:**
> $$R = \{(r,\theta) : \alpha \leq \theta \leq \beta, \, 0 \leq r \leq R\}$$
> 
> **$$\iint_R f(x,y) \, dA = \int_{\alpha}^{\beta} \int_0^R g(r,\theta) \cdot r \, dr \, d\theta$$**

> [!example]- Cálculo de Áreas con Sectores Circulares 📊
> ### Ejemplo 1: Área de un Círculo
> **Región:** $x^2 + y^2 \leq a^2$
> **En polares:** $0 \leq r \leq a, \, 0 \leq \theta \leq 2\pi$
> 
> ```
> Área = ∬_R 1 dA = ∫₀^{2π} ∫₀^a r dr dθ
> 
> = ∫₀^{2π} [r²/2]₀^a dθ = ∫₀^{2π} (a²/2) dθ
> 
> = (a²/2) × 2π = πa²
> ```
> 
> ### Ejemplo 2: Área de una Cardioide
> **Curva:** $r = a(1 + \cos\theta)$ donde $0 \leq \theta \leq 2\pi$
> 
> ```
> Área = ∫₀^{2π} ∫₀^{a(1+cosθ)} r dr dθ
> 
> = ∫₀^{2π} [r²/2]₀^{a(1+cosθ)} dθ
> 
> = (1/2) ∫₀^{2π} a²(1+cosθ)² dθ
> 
> = (a²/2) ∫₀^{2π} (1 + 2cosθ + cos²θ) dθ
> 
> = (a²/2) [θ + 2sinθ + (θ/2 + sin(2θ)/4)]₀^{2π}
> 
> = (a²/2) × (3π/2) = 3πa²/2
> ```
> 
> ### Ejemplo 3: Área entre Dos Círculos Concéntricos
> **Región:** $r_1^2 \leq x^2 + y^2 \leq r_2^2$
> **En polares:** $r_1 \leq r \leq r_2, \, 0 \leq \theta \leq 2\pi$
> 
> ```
> Área = ∫₀^{2π} ∫_{r₁}^{r₂} r dr dθ
> 
> = ∫₀^{2π} [r²/2]_{r₁}^{r₂} dθ
> 
> = ∫₀^{2π} (r₂² - r₁²)/2 dθ
> 
> = π(r₂² - r₁²)
> ```

> [!abstract]- Ejemplos de Integrales con Funciones 🧮
> ### Ejemplo 4: Integral de $f(x,y) = x^2 + y^2$ sobre un Círculo
> **Región:** $x^2 + y^2 \leq R^2$
> **Función en polares:** $f(r,\theta) = r^2$
> 
> ```
> I = ∬_R (x² + y²) dA = ∫₀^{2π} ∫₀^R r² × r dr dθ
> 
> = ∫₀^{2π} ∫₀^R r³ dr dθ = ∫₀^{2π} [r⁴/4]₀^R dθ
> 
> = ∫₀^{2π} R⁴/4 dθ = (R⁴/4) × 2π = πR⁴/2
> ```
> 
> ### Ejemplo 5: Integral de $f(x,y) = e^{-(x^2+y^2)}$ sobre $\mathbb{R}^2$
> **Región:** Todo el plano
> **Función en polares:** $f(r,\theta) = e^{-r^2}$
> 
> ```
> I = ∫₀^{2π} ∫₀^∞ e^{-r²} × r dr dθ
> 
> Sustitución: u = r², du = 2r dr → r dr = (1/2)du
> 
> = ∫₀^{2π} ∫₀^∞ e^{-u} × (1/2) du dθ
> 
> = (1/2) ∫₀^{2π} [-e^{-u}]₀^∞ dθ = (1/2) ∫₀^{2π} 1 dθ = π
> ```
> 
> ### Ejemplo 6: Volume bajo una Superficie
> **Superficie:** $z = \sqrt{x^2 + y^2}$ sobre $x^2 + y^2 \leq 4$
> **En polares:** $z = r$, región $0 \leq r \leq 2$
> 
> ```
> V = ∬_R √(x² + y²) dA = ∫₀^{2π} ∫₀^2 r × r dr dθ
> 
> = ∫₀^{2π} ∫₀^2 r² dr dθ = ∫₀^{2π} [r³/3]₀^2 dθ
> 
> = ∫₀^{2π} 8/3 dθ = (8/3) × 2π = 16π/3
> ```

> [!success]- Casos Especiales y Técnicas Avanzadas 🎯
> ### Regiones con Simetría Radial
> **Para funciones que dependen solo de $r$:**
> $$\iint_R f(\sqrt{x^2+y^2}) \, dA = 2\pi \int_0^R f(r) \cdot r \, dr$$
> 
> ### Integrales sobre Pétalos de Rosa
> **Para $r = a\cos(n\theta)$ o $r = a\sin(n\theta)$:**
> - Si $n$ es impar: $n$ pétalos, integrar $\theta \in [0, \pi]$
> - Si $n$ es par: $2n$ pétalos, integrar $\theta \in [0, 2\pi]$
> 
> ### Curvas en Coordenadas Polares Comunes
> | Curva | Ecuación Polar | Rango de θ |
> |-------|----------------|------------|
> | Círculo | $r = a$ | $[0, 2\pi]$ |
> | Cardioide | $r = a(1 + \cos\theta)$ | $[0, 2\pi]$ |
> | Rosa 3 pétalos | $r = a\cos(3\theta)$ | $[0, \pi]$ |
> | Rosa 4 pétalos | $r = a\cos(2\theta)$ | $[0, 2\pi]$ |
> | Espiral | $r = a\theta$ | $[0, n\pi]$ |
> | Lemniscata | $r^2 = a^2\cos(2\theta)$ | $[-\pi/4, \pi/4] \cup [3\pi/4, 5\pi/4]$ |

> [!warning]- Errores Comunes y Precauciones ⚠️
> ### Errores Frecuentes
> 
> **1. 🔄 Olvidar el factor $r$ en $dA$**
> ```
> ❌ Incorrecto: ∬_R f(r,θ) dr dθ
> ✅ Correcto:   ∬_R f(r,θ) × r dr dθ
> ```
> 
> **2. 📊 Límites de integración incorrectos**
> ```
> Para r = f(θ), los límites de r son: 0 ≤ r ≤ f(θ)
> NO: constante ≤ r ≤ constante
> ```
> 
> **3. ⚠️ Transformación incompleta de la función**
> ```
> Si f(x,y) = x² + y², entonces f(r,θ) = r²
> NO solo cambiar variables sin transformar la expresión
> ```
> 
> **4. 🔍 Rangos de θ mal determinados**
> ```
> Para curvas simétricas, verificar si se necesita θ ∈ [0,π] o [0,2π]
> ```
> 
> ### Lista de Verificación
> - ✅ ¿Incluí el factor $r$ en el elemento de área?
> - ✅ ¿Transformé correctamente la función $f(x,y)$?
> - ✅ ¿Los límites de $r$ dependen correctamente de $\theta$?
> - ✅ ¿El rango de $\theta$ cubre toda la región una vez?
> - ✅ ¿Verifiqué la simetría de la región?

> [!brain]+ Estrategia de Resolución: POLAR 🧠
> **P** - **Problema**: Identificar si coordenadas polares simplifican
> **O** - **Origen**: Colocar el origen estratégicamente  
> **L** - **Límites**: Determinar rangos de $r$ y $\theta$
> **A** - **Área**: Recordar $dA = r \, dr \, d\theta$
> **R** - **Resolver**: Integrar primero en $r$, luego en $\theta$
> 
> ### ¿Cuándo usar Coordenadas Polares?
> 1. **🎯 Regiones circulares** o con simetría radial
> 2. **📐 Funciones** que involucran $x^2 + y^2$
> 3. **🌀 Curvas** definidas naturalmente en polares
> 4. **⚡ Integrales** que se simplifican con la transformación

> [!summary]+ Fórmulas Clave y Resultados Importantes 📋
> ### Fórmulas Fundamentales
> 
> **Transformación:**
> $$x = r\cos\theta, \quad y = r\sin\theta, \quad dA = r \, dr \, d\theta$$
> 
> **Integral Doble:**
> $$\iint_R f(x,y) \, dA = \int_{\alpha}^{\beta} \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta) \cdot r \, dr \, d\theta$$
> 
> **Área de Región Polar:**
> $$A = \int_{\alpha}^{\beta} \int_0^{r(\theta)} r \, dr \, d\theta = \frac{1}{2}\int_{\alpha}^{\beta} [r(\theta)]^2 \, d\theta$$
> 
> ### Casos Especiales Útiles
> ```
> Área círculo de radio R:           A = πR²
> Área cardioide r = a(1+cosθ):     A = 3πa²/2  
> Área pétalo r = a cos(nθ):        A = πa²/(4n)
>
> ∬ (x²+y²) dA sobre círculo R:     I = πR⁴/2
> ∬ e^{-(x²+y²)} dA sobre ℝ²:      I = π
> ```

> [!success]- Conexiones y Aplicaciones 🔗
> ### Aplicaciones Físicas
> - **🌡️ Distribuciones de temperatura** con simetría radial
> - **⚡ Campos eléctricos** alrededor de cargas puntuales  
> - **🌊 Ondas circulares** y patrones de interferencia
> - **🔄 Momento de inercia** de objetos circulares
> - **📡 Antenas** y patrones de radiación
> 
> ### Conexiones Matemáticas
> - **Transformación de Jacobiano** general
> - **Coordenadas cilíndricas** en 3D
> - **Funciones de Bessel** y ecuaciones diferenciales
> - **Series de Fourier** en coordenadas polares
> - **Análisis complejo** y funciones holomorfahs

---

## Referencias

> [!quote] Notas Relacionadas
> - [[Integrales Dobles]]
> - [[Transformaciones de Coordenadas]]
> - [[Jacobiano de Transformaciones]]
> - [[Coordenadas Cilíndricas y Esféricas]]

## Notas Recomendadas

> [!info] Prerrequisitos
> - [[Integrales Dobles]]
> - [[Funciones Trigonométricas]]
> - [[Límites y Continuidad]]
> - [[Criterios de Convergencia y Divergencia]]

> [!tip] Continuación del Tema
> - [[Coordenadas Cilíndricas y Esféricas]]
> - [[Integrales de Línea]]
> - [[Teoremas de Green y Stokes]]
> - [[Análisis Vectorial]]

---

**Tags:** #matemáticas #integrales #coordenadas-polares #integrales-dobles #área #jacobiano #transformaciones #sectores-circulares #cálculo-multivariable #geometría
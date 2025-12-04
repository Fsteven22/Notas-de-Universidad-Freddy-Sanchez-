# 📊 Extremos Relativos de Funciones Multivariables

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva
> **Los extremos relativos (o locales) de una función multivariable son puntos donde la función alcanza valores máximos o mínimos en comparación con los puntos cercanos. Representan "picos", "valles" o "puntos de silla" en la superficie que describe la función. Este concepto es fundamental para optimización, análisis de estabilidad y modelado de fenómenos naturales.**
> 
> **Características clave:**
> - **Localidad:** Comparación con puntos vecinos (no globales)
> - **Puntos críticos:** Donde el gradiente se anula o no existe
> - **Clasificación:** Máximos, mínimos y puntos de silla
> - **Criterio:** Prueba de las segundas derivadas (Hessiano)
> - **Aplicación:** Optimización en múltiples variables

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto
> **Orígenes (1600-1800):**
> - **Fermat (1638):** Método para encontrar máximos y mínimos
>   - Tangente horizontal en extremos
>   - Precursor del cálculo diferencial
> - **Leibniz & Newton (1670s):** Cálculo diferencial
>   - Derivadas y puntos críticos
>   - Optimización en una variable
> - **Euler (1755):** Cálculo de variaciones
>   - Ecuaciones de Euler-Lagrange
>   - Extremos de funcionales
> 
> **Desarrollo multivariable (1800-1900):**
> - **Lagrange (1788):** Multiplicadores de Lagrange
>   - Optimización con restricciones
>   - Método sistemático
> - **Hesse (1844):** Matriz Hessiana
>   - Segunda derivada parcial
>   - Criterio de clasificación
> - **Weierstrass (1860):** Teoría rigurosa
>   - Existencia de extremos
>   - Compacidad y continuidad
> 
> **Era moderna (1900-presente):**
> - **Análisis convexo:**
>   - Programación no lineal
>   - Optimización global
> - **Aplicaciones computacionales:**
>   - Algoritmos de optimización
>   - Machine learning
>   - Redes neuronales (minimización de pérdida)

## 📊 Definición Formal

> [!important]- Extremos Relativos
> **Definición:**
> 
> Sea $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ una función y $(a_1, a_2, \ldots, a_n) \in D$ un punto en el dominio.
> 
> **MÁXIMO RELATIVO:**
> 
> $f$ tiene un **máximo relativo** en $(a_1, \ldots, a_n)$ si existe $\delta > 0$ tal que:
> 
> $$f(x_1, \ldots, x_n) \leq f(a_1, \ldots, a_n)$$
> 
> para todo $(x_1, \ldots, x_n)$ en el disco abierto:
> 
> $$D_\delta = \{(x_1, \ldots, x_n) : \sqrt{(x_1-a_1)^2 + \cdots + (x_n-a_n)^2} < \delta\}$$
> 
> **MÍNIMO RELATIVO:**
> 
> $f$ tiene un **mínimo relativo** en $(a_1, \ldots, a_n)$ si existe $\delta > 0$ tal que:
> 
> $$f(x_1, \ldots, x_n) \geq f(a_1, \ldots, a_n)$$
> 
> para todo $(x_1, \ldots, x_n) \in D_\delta$
> 
> **EXTREMO RELATIVO:**
> 
> Un punto es un **extremo relativo** si es máximo o mínimo relativo.
> 
> **PUNTO DE SILLA:**
> 
> Un punto crítico que NO es extremo relativo. La función aumenta en algunas direcciones y disminuye en otras.
> 
> **Notación especial para $f: \mathbb{R}^2 \to \mathbb{R}$:**
> - Punto: $(a, b)$
> - Máximo relativo: $f(x, y) \leq f(a, b)$ cerca de $(a, b)$
> - Mínimo relativo: $f(x, y) \geq f(a, b)$ cerca de $(a, b)$

## 🎯 Puntos Críticos

> [!success]- Definición y Caracterización
> **Teorema de Fermat (versión multivariable):**
> 
> Si $f$ tiene un extremo relativo en $(a, b)$ y las derivadas parciales existen en ese punto, entonces:
> 
> $$\frac{\partial f}{\partial x}(a, b) = 0 \quad \text{y} \quad \frac{\partial f}{\partial y}(a, b) = 0$$
> 
> Equivalentemente: $$\nabla f(a, b) = \vec{0}$$
> 
> **DEMOSTRACIÓN (caso $\mathbb{R}^2$):**
> 
> Supongamos que $f$ tiene máximo relativo en $(a, b)$.
> 
> Considere la función de una variable:
> $$g(x) = f(x, b)$$
> 
> Como $f$ tiene máximo en $(a, b)$, entonces $g$ tiene máximo en $x = a$.
> 
> Por teorema de Fermat en una variable:
> $$g'(a) = 0$$
> 
> Pero: $$g'(a) = \frac{\partial f}{\partial x}(a, b)$$
> 
> Por tanto: $$\frac{\partial f}{\partial x}(a, b) = 0$$
> 
> Análogamente, considerando $h(y) = f(a, y)$:
> $$\frac{\partial f}{\partial y}(a, b) = 0 \quad \checkmark$$
> 
> **PUNTO CRÍTICO:**
> 
> Un punto $(a, b)$ es **crítico** si:
> 
> 1. $\nabla f(a, b) = \vec{0}$ (punto estacionario), o
> 2. $\nabla f(a, b)$ no existe
> 
> **TIPOS DE PUNTOS CRÍTICOS:**
> 
> ```mermaid
> graph TD
>     A[Punto Crítico] --> B{∇f existe?}
>     B -->|Sí: ∇f = 0⃗| C[Punto Estacionario]
>     B -->|No| D[Punto Singular]
>     
>     C --> E{Clasificación}
>     E -->|D > 0, fₓₓ > 0| F[Mínimo Relativo]
>     E -->|D > 0, fₓₓ < 0| G[Máximo Relativo]
>     E -->|D < 0| H[Punto de Silla]
>     E -->|D = 0| I[Prueba Inconclusiva]
>     
>     style F fill:#c8e6c9
>     style G fill:#c8e6c9
>     style H fill:#ffccbc
>     style I fill:#fff9c4
> ```
> 
> **⚠️ IMPORTANTE:**
> 
> - Todo extremo relativo (con derivadas) es punto crítico
> - NO todo punto crítico es extremo relativo
> - Los puntos de silla son puntos críticos sin ser extremos

## 🔍 Prueba de las Segundas Derivadas

> [!tip]- Criterio del Hessiano
> **Para funciones $f: \mathbb{R}^2 \to \mathbb{R}$:**
> 
> Sea $(a, b)$ un punto crítico donde $\nabla f(a, b) = \vec{0}$.
> 
> **MATRIZ HESSIANA:**
> 
> $$H(x, y) = \begin{bmatrix} f_{xx}(x,y) & f_{xy}(x,y) \\ f_{yx}(x,y) & f_{yy}(x,y) \end{bmatrix}$$
> 
> **DISCRIMINANTE (Determinante del Hessiano):**
> 
> $$D(a, b) = \det(H(a,b)) = f_{xx}(a,b) \cdot f_{yy}(a,b) - [f_{xy}(a,b)]^2$$
> 
> Notación común:
> $$D = f_{xx}f_{yy} - (f_{xy})^2$$
> 
> **CRITERIO DE CLASIFICACIÓN:**
> 
> **CASO 1:** $D(a, b) > 0$ (Hessiano definido)
> 
> - Si $f_{xx}(a, b) > 0$: **MÍNIMO RELATIVO** ✓
> - Si $f_{xx}(a, b) < 0$: **MÁXIMO RELATIVO** ✓
> 
> (Alternativamente: usar $f_{yy}$ en lugar de $f_{xx}$)
> 
> **CASO 2:** $D(a, b) < 0$ (Hessiano indefinido)
> 
> - **PUNTO DE SILLA** ✗
> 
> **CASO 3:** $D(a, b) = 0$
> 
> - **PRUEBA INCONCLUSIVA** ?
> - Se requiere análisis adicional
> 
> **RESUMEN VISUAL:**
> 
> | Condición | $D > 0$ y $f_{xx} > 0$ | $D > 0$ y $f_{xx} < 0$ | $D < 0$ | $D = 0$ |
> |-----------|------------------------|------------------------|---------|---------|
> | **Resultado** | Mínimo relativo 📉 | Máximo relativo 📈 | Punto de silla 🏔️ | Inconclusivo ❓ |
> | **Hessiano** | Definido positivo | Definido negativo | Indefinido | Semi-definido |
> | **Superficie** | Paraboloide hacia arriba | Paraboloide hacia abajo | Silla de montar | Requiere análisis |
> 
> **DEMOSTRACIÓN (idea):**
> 
> Usar desarrollo de Taylor de segundo orden alrededor de $(a, b)$:
> 
> $$f(a+h, b+k) \approx f(a,b) + \nabla f(a,b) \cdot \begin{bmatrix} h \\ k \end{bmatrix} + \frac{1}{2}\begin{bmatrix} h & k \end{bmatrix} H(a,b) \begin{bmatrix} h \\ k \end{bmatrix}$$
> 
> Como $(a, b)$ es crítico: $\nabla f(a, b) = \vec{0}$
> 
> $$f(a+h, b+k) - f(a,b) \approx \frac{1}{2}\begin{bmatrix} h & k \end{bmatrix} H(a,b) \begin{bmatrix} h \\ k \end{bmatrix}$$
> 
> El signo depende de la forma cuadrática asociada a $H(a,b)$:
> - Si $H$ es definida positiva ($D > 0$, $f_{xx} > 0$): forma cuadrática $> 0$ → mínimo
> - Si $H$ es definida negativa ($D > 0$, $f_{xx} < 0$): forma cuadrática $< 0$ → máximo
> - Si $H$ es indefinida ($D < 0$): forma cuadrática cambia de signo → silla

## 📐 Procedimiento Completo

> [!important]- Algoritmo para Encontrar Extremos
> **MÉTODO SISTEMÁTICO:**
> 
> **PASO 1: Encontrar puntos críticos**
> 
> Resolver el sistema:
> $$\begin{cases}
> \frac{\partial f}{\partial x} = 0 \\
> \frac{\partial f}{\partial y} = 0
> \end{cases}$$
> 
> Los puntos $(a, b)$ que satisfacen ambas ecuaciones son los puntos críticos.
> 
> **PASO 2: Calcular segundas derivadas**
> 
> Calcular:
> $$f_{xx} = \frac{\partial^2 f}{\partial x^2}, \quad f_{yy} = \frac{\partial^2 f}{\partial y^2}, \quad f_{xy} = \frac{\partial^2 f}{\partial x \partial y}$$
> 
> **PASO 3: Evaluar el discriminante**
> 
> Para cada punto crítico $(a, b)$:
> $$D(a, b) = f_{xx}(a,b) \cdot f_{yy}(a,b) - [f_{xy}(a,b)]^2$$
> 
> **PASO 4: Clasificar puntos**
> 
> Aplicar el criterio:
> - $D > 0$ y $f_{xx} > 0$: **mínimo relativo**
> - $D > 0$ y $f_{xx} < 0$: **máximo relativo**
> - $D < 0$: **punto de silla**
> - $D = 0$: **inconclusivo** (análisis adicional)
> 
> **PASO 5: Evaluar la función (opcional)**
> 
> Calcular $f(a, b)$ para cada extremo relativo para conocer los valores óptimos.
> 
> **DIAGRAMA DE FLUJO:**
> 
> ```mermaid
> flowchart TD
>     A[Función f x,y] --> B[Calcular ∇f]
>     B --> C[Resolver ∇f = 0⃗]
>     C --> D[Puntos críticos: a,b]
>     
>     D --> E[Calcular fₓₓ, f_yy, fₓᵧ]
>     E --> F[D = fₓₓ·f_yy - fₓᵧ²]
>     
>     F --> G{D > 0?}
>     G -->|Sí| H{fₓₓ > 0?}
>     G -->|No| I{D < 0?}
>     
>     H -->|Sí| J[✓ Mínimo Relativo]
>     H -->|No| K[✓ Máximo Relativo]
>     I -->|Sí| L[✗ Punto de Silla]
>     I -->|No| M[? Inconclusivo]
>     
>     style J fill:#c8e6c9
>     style K fill:#c8e6c9
>     style L fill:#ffccbc
>     style M fill:#fff9c4
> ```

## 💡 Ejemplos Resueltos

> [!example]- Problemas Detallados
> **Problema 1: Paraboloide elíptico**
> 
> Encontrar y clasificar los extremos de:
> $$f(x, y) = x^2 + 2y^2 - 4x + 4y + 7$$
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Derivadas parciales**
> 
> $$f_x = 2x - 4$$
> $$f_y = 4y + 4$$
> 
> **Puntos críticos:**
> $$\begin{cases}
> 2x - 4 = 0 \implies x = 2 \\
> 4y + 4 = 0 \implies y = -1
> \end{cases}$$
> 
> Único punto crítico: $(2, -1)$
> 
> **PASO 2: Segundas derivadas**
> 
> $$f_{xx} = 2$$
> $$f_{yy} = 4$$
> $$f_{xy} = 0$$
> 
> **PASO 3: Discriminante**
> 
> $$D(2, -1) = (2)(4) - (0)^2 = 8 > 0$$
> 
> Como $D > 0$ y $f_{xx} = 2 > 0$:
> 
> $$\boxed{\text{MÍNIMO RELATIVO en } (2, -1)}$$
> 
> **PASO 4: Valor del mínimo**
> 
> $$f(2, -1) = (2)^2 + 2(-1)^2 - 4(2) + 4(-1) + 7$$
> $$= 4 + 2 - 8 - 4 + 7 = 1$$
> 
> **RESPUESTA FINAL:**
> - Mínimo relativo en $(2, -1)$
> - Valor mínimo: $f(2, -1) = 1$
> 
> **VERIFICACIÓN GEOMÉTRICA:**
> 
> Completando cuadrados:
> $$f(x, y) = (x-2)^2 + 2(y+1)^2 + 1$$
> 
> Esta es la ecuación de un paraboloide elíptico con vértice en $(2, -1, 1)$ que abre hacia arriba, confirmando el mínimo. ✓
> 
> ---
> 
> **Problema 2: Punto de silla**
> 
> Clasificar los extremos de:
> $$f(x, y) = x^2 - y^2$$
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Puntos críticos**
> 
> $$f_x = 2x = 0 \implies x = 0$$
> $$f_y = -2y = 0 \implies y = 0$$
> 
> Punto crítico: $(0, 0)$
> 
> **PASO 2: Segundas derivadas**
> 
> $$f_{xx} = 2, \quad f_{yy} = -2, \quad f_{xy} = 0$$
> 
> **PASO 3: Discriminante**
> 
> $$D(0, 0) = (2)(-2) - (0)^2 = -4 < 0$$
> 
> $$\boxed{\text{PUNTO DE SILLA en } (0, 0)}$$
> 
> **INTERPRETACIÓN:**
> 
> Esta función se llama "paraboloide hiperbólico" o "silla de montar".
> 
> - A lo largo del eje $x$ ($y = 0$): $f(x, 0) = x^2$ → parábola hacia arriba
> - A lo largo del eje $y$ ($x = 0$): $f(0, y) = -y^2$ → parábola hacia abajo
> 
> En $(0, 0)$ la función tiene mínimo en una dirección y máximo en otra perpendicular. ✓
> 
> ---
> 
> **Problema 3: Múltiples puntos críticos**
> 
> Encontrar extremos de:
> $$f(x, y) = x^3 - 3x + y^2$$
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Derivadas y puntos críticos**
> 
> $$f_x = 3x^2 - 3 = 0 \implies x^2 = 1 \implies x = \pm 1$$
> $$f_y = 2y = 0 \implies y = 0$$
> 
> Puntos críticos: $(1, 0)$ y $(-1, 0)$
> 
> **PASO 2: Segundas derivadas**
> 
> $$f_{xx} = 6x, \quad f_{yy} = 2, \quad f_{xy} = 0$$
> 
> **PASO 3: Análisis de $(1, 0)$**
> 
> $$f_{xx}(1, 0) = 6(1) = 6$$
> $$f_{yy}(1, 0) = 2$$
> $$f_{xy}(1, 0) = 0$$
> 
> $$D(1, 0) = (6)(2) - (0)^2 = 12 > 0$$
> 
> Como $D > 0$ y $f_{xx} = 6 > 0$:
> 
> $$\boxed{\text{MÍNIMO RELATIVO en } (1, 0)}$$
> 
> Valor: $f(1, 0) = 1 - 3 + 0 = -2$
> 
> **PASO 4: Análisis de $(-1, 0)$**
> 
> $$f_{xx}(-1, 0) = 6(-1) = -6$$
> $$f_{yy}(-1, 0) = 2$$
> $$f_{xy}(-1, 0) = 0$$
> 
> $$D(-1, 0) = (-6)(2) - (0)^2 = -12 < 0$$
> 
> $$\boxed{\text{PUNTO DE SILLA en } (-1, 0)}$$
> 
> Valor: $f(-1, 0) = -1 + 3 + 0 = 2$
> 
> **RESUMEN:**
> - Mínimo relativo en $(1, 0)$ con valor $-2$
> - Punto de silla en $(-1, 0)$
> 
> ---
> 
> **Problema 4: Caso inconclusivo**
> 
> Analizar:
> $$f(x, y) = x^4 + y^4$$
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Punto crítico**
> 
> $$f_x = 4x^3 = 0 \implies x = 0$$
> $$f_y = 4y^3 = 0 \implies y = 0$$
> 
> Punto crítico: $(0, 0)$
> 
> **PASO 2: Discriminante**
> 
> $$f_{xx} = 12x^2 \implies f_{xx}(0,0) = 0$$
> $$f_{yy} = 12y^2 \implies f_{yy}(0,0) = 0$$
> $$f_{xy} = 0$$
> 
> $$D(0, 0) = (0)(0) - (0)^2 = 0$$
> 
> **Prueba inconclusiva** ⚠️
> 
> **PASO 3: Análisis directo**
> 
> Observemos que:
> $$f(x, y) = x^4 + y^4 \geq 0 \text{ para todo } (x, y)$$
> 
> Y $f(0, 0) = 0$
> 
> Por tanto: $$f(x, y) \geq f(0, 0) = 0$$
> 
> $$\boxed{\text{MÍNIMO ABSOLUTO en } (0, 0)}$$
> 
> **LECCIÓN:** Cuando $D = 0$, el criterio falla pero el análisis directo puede resolver el caso.

## 🎨 Interpretación Geométrica

> [!note]- Visualización de Superficies
> **Tipos de superficies en puntos críticos:**
> 
> **1. PARABOLOIDE ELÍPTICO (Mínimo):**
> 
> Ejemplo: $f(x, y) = x^2 + y^2$
> 
> ```
>         z
>         ↑
>         |    ╱╲
>         |   ╱  ╲
>         |  ╱    ╲
>         | ╱______╲
>         |╱________╲
>         └──────────→ xy
>         
>     Cuenco hacia arriba
>     D > 0, fₓₓ > 0
> ```
> 
> Características:
> - Todas las secciones son parábolas hacia arriba
> - Punto mínimo en el centro
> - $D > 0$, $f_{xx} > 0$
> 
> **2. PARABOLOIDE ELÍPTICO INVERTIDO (Máximo):**
> 
> Ejemplo: $f(x, y) = -x^2 - y^2$
> 
> ```
>       ╲________╱
>        ╲______╱
>         ╲____╱
>          ╲__╱
>           ╲╱
>         
>     Cuenco hacia abajo
>     D > 0, fₓₓ < 0
> ```
> 
> Características:
> - Todas las secciones son parábolas hacia abajo
> - Punto máximo en el centro
> - $D > 0$, $f_{xx} < 0$
> 
> **3. PARABOLOIDE HIPERBÓLICO (Silla):**
> 
> Ejemplo: $f(x, y) = x^2 - y^2$
> 
> ```
>         ╲     ╱
>          ╲   ╱
>           ╲ ╱
>            X  ← Punto de silla
>           ╱ ╲
>          ╱   ╲
>         ╱     ╲
>         
>     Silla de montar
>     D < 0
> ```
> 
> Características:
> - Curva hacia arriba en una dirección
> - Curva hacia abajo en dirección perpendicular
> - $D < 0$
> 
> **CURVAS DE NIVEL:**
> 
> Para $f(x, y) = x^2 + y^2$ (mínimo en origen):
> 
> ```
>         y
>         ↑
>         |    ⊙  ← círculos concéntricos
>         |   ⊙⊙
>         |  ⊙ ⊙
>         | ⊙   ⊙
>         |⊙_____⊙→ x
>         
>     Centro = mínimo
> ```
> 
> Para $f(x, y) = x^2 - y^2$ (silla en origen):
> 
> ```
>         y
>         ↑  ╲ | ╱
>         |   ╲|╱
>         |────X──── x
>         |   ╱|╲
>         |  ╱ | ╲
>         
>     Hipérbolas
> ```

## 🔗 Relación con Optimización

> [!success]- Extremos en Regiones Cerradas
> **Teorema de Weierstrass:**
> 
> Si $f$ es continua en una región cerrada y acotada $D \subseteq \mathbb{R}^2$, entonces $f$ alcanza su valor máximo absoluto y su valor mínimo absoluto en $D$.
> 
> **MÉTODO DE OPTIMIZACIÓN EN REGIONES CERRADAS:**
> 
> Para encontrar el máximo y mínimo absoluto de $f$ en región $D$:
> 
> **PASO 1:** Encontrar puntos críticos en el **interior** de $D$
> 
> Resolver $\nabla f = \vec{0}$
> 
> **PASO 2:** Encontrar valores en la **frontera** de $D$
> 
> Esto puede requerir:
> - Parametrización de la frontera
> - Multiplicadores de Lagrange
> - Análisis por segmentos
> 
> **PASO 3:** Evaluar $f$ en todos los candidatos
> 
> - Puntos críticos del interior
> - Puntos críticos de la frontera
> - Esquinas o puntos especiales
> 
> **PASO 4:** Comparar valores
> 
> - El mayor valor → **máximo absoluto**
> - El menor valor → **mínimo absoluto**
> 
> **EJEMPLO:**
> 
> Encontrar extremos absolutos de $f(x, y) = x^2 + y^2 - 2x$ en el disco $x^2 + y^2 \leq 4$
> 
> **Interior:**
> 
> $$f_x = 2x - 2 = 0 \implies x = 1$$
> $$f_y = 2y = 0 \implies y = 0$$
> 
> Punto crítico: $(1, 0)$ (está en el interior: $1^2 + 0^2 = 1 < 4$ ✓)
> 
> $f(1, 0) = 1 + 0 - 2 = -1$
> 
> **Frontera:** $x^2 + y^2 = 4$
> 
> Parametrización: $x = 2\cos\theta$, $y = 2\sin\theta$
> 
> $$g(\theta) = (2\cos\theta)^2 + (2\sin\theta)^2 - 2(2\cos\theta)$$
> $$= 4 - 4\cos\theta$$
> 
> $$g'(\theta) = 4\sin\theta = 0 \implies \theta = 0, \pi$$
> 
> - $\theta = 0$: $(2, 0)$, $f(2, 0) = 4 + 0 - 4 = 0$
> - $\theta = \pi$: $(-2, 0)$, $f(-2, 0) = 4 + 0 + 4 = 8$
> 
> **COMPARACIÓN:**
> 
> | Punto | Tipo | Valor |
> |-------|------|-------|
> | $(1, 0)$ | Interior | $-1$ |
> | $(2, 0)$ | Frontera | $0$ |
> | $(-2, 0)$ | Frontera | $8$ |
> 
> **RESPUESTA:**
> - **Mínimo absoluto:** $f(1, 0) = -1$
> - **Máximo absoluto:** $f(-2, 0) = 8$

## ⚡ Casos Especiales

> [!important]- Situaciones Particulares
> **1. FUNCIONES DEFINIDAS POR PARTES:**
> 
> Verificar continuidad y derivabilidad en las fronteras.
> 
> Ejemplo: 
> $$f(x, y) = \begin{cases}
> x^2 + y^2 & \text{si } x^2 + y^2 \leq 1 \\
> 2 - x^2 - y^2 & \text{si } x^2 + y^2 > 1
> \end{cases}$$
> 
> Analizar puntos críticos en cada región y en la frontera común.
> 
> **2. FUNCIONES NO DIFERENCIABLES:**
> 
> Ejemplo: $f(x, y) = |x| + |y|$
> 
> - No es diferenciable en los ejes
> - Mínimo en $(0, 0)$ pero $\nabla f(0, 0)$ no existe
> - Requiere análisis directo
> 
> **3. PUNTOS CRÍTICOS EN EL INFINITO:**
> 
> Algunas funciones tienen comportamiento asintótico relevante.
> 
> Ejemplo: $f(x, y) = \frac{1}{1 + x^2 + y^2}$
> 
> - Máximo en $(0, 0)$: $f(0, 0) = 1$
> - $\lim_{|(x,y)| \to \infty} f(x, y) = 0$ (ínfimo pero no mínimo)
> 
> **4. SIMETRÍAS:**
> 
> Aprovechar simetrías para simplificar.
> 
> Si $f(x, y) = f(-x, y) = f(x, -y)$, solo analizar primer cuadrante.
> 
> **5. FUNCIONES HOMOGÉNEAS:**
> 
> Para $f(tx, ty) = t^n f(x, y)$:
> 
> - Si $n > 0$: extremos solo en el origen o frontera
> - Si $n < 0$: sin extremos en el origen
> 
> **6. MÉTODO DE DESCENSO:**
> 
> Para verificar que un punto crítico NO es extremo:
> 
> Encontrar curvas pasando por el punto donde $f$ aumenta y disminuye.
> 
> Ejemplo en silla $(0, 0)$ de $f = x^2 - y^2$:
> - A lo largo de $y = 0$: $f(t, 0) = t^2 \geq 0$ (crece)
> - A lo largo de $x = 0$: $f(0, t) = -t^2 \leq 0$ (decrece)

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes
> **1. "Todo punto crítico es extremo"**
> 
> ✗ **FALSO**
> 
> Los puntos de silla son críticos pero NO extremos.
> 
> Ejemplo: $f(x, y) = x^2 - y^2$ tiene punto crítico en $(0, 0)$ pero es silla, no extremo.
> 
> ---
> 
> **2. "Si $D = 0$ no hay extremo"**
> 
> ✗ **FALSO**
> 
> Cuando $D = 0$ la prueba es **inconclusiva**, no negativa.
> 
> Ejemplo: $f(x, y) = x^4 + y^4$ tiene $D(0, 0) = 0$ pero $(0, 0)$ SÍ es mínimo absoluto.
> 
> ---
> 
> **3. "Máximo relativo = máximo absoluto"**
> 
> ✗ **FALSO**
> 
> Un máximo relativo es local; puede haber valores mayores lejos del punto.
> 
> Ejemplo: $f(x, y) = -(x-1)^2 - (y-1)^2 + (x-5)^2 + (y-5)^2$
> 
> Puede tener dos máximos relativos con diferentes valores.
> 
> ---
> 
> **4. "Si $f_x(a, b) = 0$ entonces $(a, b)$ es crítico en esa dirección"**
> 
> ✗ **INCOMPLETO**
> 
> Se necesita $f_x = 0$ **Y** $f_y = 0$ simultáneamente.
> 
> Ejemplo: $f(x, y) = x^2 + y$
> 
> $f_x = 2x = 0 \implies x = 0$ pero $f_y = 1 \neq 0$ para todo $y$. No hay puntos críticos.
> 
> ---
> 
> **5. "Usar $f_{yy}$ en lugar de $f_{xx}$ da diferente resultado"**
> 
> ✗ **FALSO** (cuando $D > 0$)
> 
> Si $D > 0$, entonces $f_{xx}$ y $f_{yy}$ tienen el mismo signo.
> 
> Puedes usar cualquiera de los dos para clasificar.
> 
> **DEMOSTRACIÓN:**
> 
> Si $D = f_{xx}f_{yy} - (f_{xy})^2 > 0$, entonces:
> $$f_{xx}f_{yy} > (f_{xy})^2 \geq 0$$
> 
> Por tanto $f_{xx}$ y $f_{yy}$ tienen el mismo signo. ✓
> 
> ---
> 
> **6. "Olvidar verificar que el punto está en el dominio"**
> 
> ⚠️ **IMPORTANTE**
> 
> Siempre verificar que puntos críticos estén en $\text{Dom}(f)$.
> 
> Ejemplo: $f(x, y) = \ln(x^2 + y^2)$ con dominio $x^2 + y^2 > 0$
> 
> Aunque $f_x = \frac{2x}{x^2+y^2} = 0 \implies x = 0$ y $f_y = \frac{2y}{x^2+y^2} = 0 \implies y = 0$
> 
> El punto $(0, 0)$ NO está en el dominio. Sin puntos críticos.
> 
> ---
> 
> **7. "Confundir segunda derivada mixta"**
> 
> ⚠️ **CUIDADO**
> 
> Por teorema de Schwarz (si son continuas):
> $$f_{xy} = f_{yx}$$
> 
> Pero en el discriminante se usa $(f_{xy})^2$, no $f_{xy} \cdot f_{yx}$.
> 
> $$D = f_{xx}f_{yy} - (f_{xy})^2 \quad \checkmark$$
> $$D = f_{xx}f_{yy} - f_{xy}f_{yx} \quad \checkmark \text{ (equivalente)}$$

## 🔗 Extensión a $n$ Variables

> [!quote]- Generalización
> **Para $f: \mathbb{R}^n \to \mathbb{R}$:**
> 
> **PUNTO CRÍTICO:**
> 
> $\mathbf{a} = (a_1, \ldots, a_n)$ es crítico si:
> $$\nabla f(\mathbf{a}) = \vec{0}$$
> 
> Es decir:
> $$\frac{\partial f}{\partial x_1}(\mathbf{a}) = \cdots = \frac{\partial f}{\partial x_n}(\mathbf{a}) = 0$$
> 
> **MATRIZ HESSIANA:**
> 
> $$H(\mathbf{x}) = \begin{bmatrix}
> \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
> \frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
> \vdots & \vdots & \ddots & \vdots \\
> \frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
> \end{bmatrix}$$
> 
> **CRITERIO DE CLASIFICACIÓN:**
> 
> Calcular los **valores propios** de $H(\mathbf{a})$:
> 
> - **Todos $\lambda_i > 0$:** mínimo relativo (Hessiano definido positivo)
> - **Todos $\lambda_i < 0$:** máximo relativo (Hessiano definido negativo)
> - **Signos mixtos:** punto de silla (Hessiano indefinido)
> - **Algún $\lambda_i = 0$:** inconclusivo (Hessiano semi-definido)
> 
> **CRITERIO ALTERNATIVO (Menores principales):**
> 
> Sean $D_1, D_2, \ldots, D_n$ los menores principales de $H(\mathbf{a})$.
> 
> - **Mínimo:** $D_1 > 0, D_2 > 0, \ldots, D_n > 0$
> - **Máximo:** $D_1 < 0, D_2 > 0, D_3 < 0, D_4 > 0, \ldots$ (signos alternados)
> 
> **EJEMPLO ($\mathbb{R}^3$):**
> 
> $f(x, y, z) = x^2 + 2y^2 + 3z^2$
> 
> $$H = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 6 \end{bmatrix}$$
> 
> Valores propios: $\lambda_1 = 2, \lambda_2 = 4, \lambda_3 = 6$ (todos positivos)
> 
> $(0, 0, 0)$ es **mínimo relativo** (de hecho, absoluto).

## 📚 Recursos Adicionales

> [!note]- Herramientas y Visualización
> **Software de cálculo:**
> 
> - **GeoGebra 3D**
>   - Graficar superficies
>   - Visualizar puntos críticos
>   - Curvas de nivel
> - **MATLAB/Octave**
>   ```matlab
>   [X, Y] = meshgrid(-2:0.1:2, -2:0.1:2);
>   Z = X.^2 + Y.^2;
>   surf(X, Y, Z);
>   ```
> - **Python (matplotlib)**
>   ```python
>   import numpy as np
>   import matplotlib.pyplot as plt
>   from mpl_toolkits.mplot3d import Axes3D
>   
>   x = np.linspace(-2, 2, 100)
>   y = np.linspace(-2, 2, 100)
>   X, Y = np.meshgrid(x, y)
>   Z = X**2 + Y**2
>   
>   fig = plt.figure()
>   ax = fig.add_subplot(111, projection='3d')
>   ax.plot_surface(X, Y, Z, cmap='viridis')
>   plt.show()
>   ```
> - **Wolfram Alpha**
>   - "critical points x^2 + y^2"
>   - "classify critical point (0,0) of x^2 - y^2"
> 
> **Calculadoras simbólicas:**
> - **SymPy (Python)**
>   ```python
>   from sympy import symbols, diff, solve
>   x, y = symbols('x y')
>   f = x**2 + y**2 - 2*x
>   fx = diff(f, x)
>   fy = diff(f, y)
>   critical = solve([fx, fy], [x, y])
>   ```

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas
> **Nivel introductorio:**
> - **Stewart, J.** (2021). _Cálculo de Varias Variables_ (9ª ed.). Cengage.
>   - Cap. 14: Derivadas parciales
>   - Sección 14.7: Máximos y mínimos
> - **Thomas, G. B.** (2019). _Cálculo Varias Variables_ (14ª ed.). Pearson.
>   - Cap. 14: Derivadas parciales
>   - Sección 14.7: Valores extremos
> 
> **Nivel intermedio:**
> - **Marsden, J. E., & Tromba, A. J.** (2012). _Vector Calculus_ (6th ed.). Freeman.
>   - Cap. 3: Funciones de varias variables
>   - Tratamiento geométrico excelente
> - **Edwards, C. H., & Penney, D. E.** (2008). _Cálculo con Geometría Analítica_.
>   - Cap. 13: Derivadas parciales
>   - Muchos ejemplos aplicados
> 
> **Nivel avanzado:**
> - **Apostol, T. M.** (1969). _Calculus, Vol. II_ (2nd ed.). Wiley.
>   - Cap. 12: Optimización multivariable
>   - Tratamiento riguroso
> - **Rudin, W.** (1976). _Principles of Mathematical Analysis_ (3rd ed.). McGraw-Hill.
>   - Cap. 9: Funciones de varias variables
>   - Teoría avanzada

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales
> 
> **DEFINICIONES ESENCIALES:**
> 
> - **Punto crítico:** $\nabla f(\mathbf{a}) = \vec{0}$ o no existe
> - **Extremo relativo:** Máximo o mínimo local
> - **Punto de silla:** Crítico pero no extremo
> 
> **CRITERIO DEL HESSIANO ($\mathbb{R}^2$):**
> 
> $$D(a, b) = f_{xx}(a,b) \cdot f_{yy}(a,b) - [f_{xy}(a,b)]^2$$
> 
> | $D$ | $f_{xx}$ | Clasificación |
> |-----|----------|---------------|
> | $> 0$ | $> 0$ | Mínimo relativo |
> | $> 0$ | $< 0$ | Máximo relativo |
> | $< 0$ | - | Punto de silla |
> | $= 0$ | - | Inconclusivo |
> 
> **PROCEDIMIENTO:**
> 
> 1. Encontrar críticos: $\nabla f = \vec{0}$
> 2. Calcular $f_{xx}, f_{yy}, f_{xy}$
> 3. Evaluar discriminante $D$
> 4. Clasificar según criterio
> 
> **TEOREMA CLAVE:**
> 
> Todo extremo relativo (con derivadas) es punto crítico, pero no viceversa.

---

**Tags:** #calculo-multivariable #extremos-relativos #optimizacion #puntos-criticos #hessiano #segunda-derivada #maximos #minimos #punto-silla #gradiente #derivadas-parciales
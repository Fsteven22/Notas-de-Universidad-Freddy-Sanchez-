# 📐 Producto Interno

## 🎯 Introducción al Producto Interno

> [!info]- 💡 ¿Qué es un Producto Interno?
> 
> El **producto interno** es una operación que toma dos vectores y produce un número (escalar). Generaliza el concepto del "producto punto" que conocemos de $\mathbb{R}^n$ a espacios vectoriales más abstractos.
> 
> **Analogía intuitiva:**
> 
> Imagina que tienes dos flechas (vectores) en el espacio. El producto interno te dice:
> 
> - **¿Qué tan alineadas están?** (si apuntan en la misma dirección o no)
> - **¿Cuánta "energía compartida" tienen?** (en términos físicos)
> - **¿Cuál es la "proyección" de una sobre otra?**
> 
> **Desde lo conocido a lo abstracto:**
> 
> ```mermaid
> graph LR
>     A[Producto Punto en ℝⁿ<br/>u·v = u₁v₁ + ... + uₙvₙ] --> B[Generalización]
>     B --> C[Producto Interno ⟨u,v⟩<br/>Espacio abstracto V]
>     C --> D[Mantiene propiedades<br/>esenciales]
>     
>     style A fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
> ```

---

## 📋 Definición Formal

> [!note]- 🔷 Axiomas del Producto Interno
> 
> Sea $V$ un espacio vectorial sobre $\mathbb{R}$ (o $\mathbb{C}$). Un **producto interno** en $V$ es una función:
> 
> $$\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R} \text{ (o } \mathbb{C}\text{)}$$
> 
> que satisface los siguientes **cuatro axiomas** para todo $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ y todo escalar $\alpha$:
> 
> ### Axiomas para Espacios Reales
> 
> |#|Nombre|Expresión Matemática|Significado Intuitivo|
> |---|---|---|---|
> |**PI1**|**Linealidad en el primer argumento**|$\langle \alpha\mathbf{u} + \mathbf{v}, \mathbf{w} \rangle = \alpha\langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$|Distributiva respecto a combinaciones lineales|
> |**PI2**|**Simetría (Conmutatividad)**|$\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$|El orden no importa|
> |**PI3**|**Positividad**|$\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$|El "producto consigo mismo" es no negativo|
> |**PI4**|**Definición positiva**|$\langle \mathbf{v}, \mathbf{v} \rangle = 0 \iff \mathbf{v} = \mathbf{0}$|Solo el vector cero tiene producto cero consigo mismo|
> 
> **Visualización de los axiomas:**
> 
> ```mermaid
> graph TD
>     A[Producto Interno ⟨·,·⟩] --> B[PI1: Linealidad]
>     A --> C[PI2: Simetría]
>     A --> D[PI3: Positividad]
>     A --> E[PI4: Definición Positiva]
>     
>     B --> F[⟨αu+v,w⟩ = α⟨u,w⟩ + ⟨v,w⟩]
>     C --> G[⟨u,v⟩ = ⟨v,u⟩]
>     D --> H[⟨v,v⟩ ≥ 0]
>     E --> I[⟨v,v⟩ = 0 ⟺ v = 0]
>     
>     style A fill:#e1ffe1
>     style B fill:#fff4e1
>     style C fill:#e1f5ff
>     style D fill:#ffe1e1
>     style E fill:#f0e1ff
> ```
> 
> ### Axiomas para Espacios Complejos
> 
> En espacios sobre $\mathbb{C}$, el axioma **PI2** se modifica:
> 
> |#|Nombre|Expresión|
> |---|---|---|
> |**PI2'**|**Simetría conjugada (Hermítica)**|$\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$|
> 
> donde $\overline{z}$ denota el conjugado complejo de $z$.

---

## 🌟 Ejemplos Fundamentales

### 📊 Ejemplo 1: Producto Punto Euclidiano en $\mathbb{R}^n$

> [!example]- 🎯 El Ejemplo Clásico
> 
> **Definición:**
> 
> Para $\mathbf{u} = (u_1, u_2, \ldots, u_n)$ y $\mathbf{v} = (v_1, v_2, \ldots, v_n)$ en $\mathbb{R}^n$:
> 
> $$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + \cdots + u_nv_n = \sum_{i=1}^n u_i v_i$$
> 
> **Ejemplo numérico en $\mathbb{R}^3$:**
> 
> ```
> u = (1, 2, 3)
> v = (4, 5, 6)
> 
> ⟨u, v⟩ = 1·4 + 2·5 + 3·6
>        = 4 + 10 + 18
>        = 32
> ```
> 
> **Verificación de axiomas:**
> 
> |Axioma|Verificación|
> |---|---|
> |**PI1**|$\langle \alpha\mathbf{u} + \mathbf{v}, \mathbf{w} \rangle = \sum_i (\alpha u_i + v_i)w_i = \alpha\sum_i u_iw_i + \sum_i v_iw_i$ ✅|
> |**PI2**|$\sum_i u_iv_i = \sum_i v_iu_i$ (conmutatividad de $\mathbb{R}$) ✅|
> |**PI3**|$\langle \mathbf{v}, \mathbf{v} \rangle = \sum_i v_i^2 \geq 0$ (suma de cuadrados) ✅|
> |**PI4**|$\sum_i v_i^2 = 0 \iff v_i = 0$ para todo $i$ ✅|
> 
> **Casos especiales:**
> 
> ```
> En ℝ²:
> u = (3, 4),  v = (1, 0)
> ⟨u, v⟩ = 3·1 + 4·0 = 3
> 
> u = (1, 1),  v = (1, -1)
> ⟨u, v⟩ = 1·1 + 1·(-1) = 0  (ortogonales!)
> 
> u = (3, 4)
> ⟨u, u⟩ = 3² + 4² = 25
> ```

### 📊 Ejemplo 2: Producto Interno Ponderado en $\mathbb{R}^n$

> [!example]- ⚖️ Asignando Importancia Diferente
> 
> **Definición:**
> 
> Dados pesos positivos $w_1, w_2, \ldots, w_n > 0$:
> 
> $$\langle \mathbf{u}, \mathbf{v} \rangle_w = w_1u_1v_1 + w_2u_2v_2 + \cdots + w_nu_nv_n$$
> 
> **Interpretación:**
> 
> Los pesos $w_i$ indican la "importancia" o "peso" de cada componente.
> 
> |Peso|Interpretación|Aplicación|
> |---|---|---|
> |$w_i > 1$|Componente $i$ es MÁS importante|Variables críticas en modelos|
> |$w_i = 1$|Todas las componentes iguales|Producto estándar|
> |$0 < w_i < 1$|Componente $i$ es MENOS relevante|Variables secundarias|
> 
> **Ejemplo numérico:**
> 
> ```
> En ℝ³ con pesos w = (2, 3, 1):
> u = (1, 2, 3)
> v = (4, 5, 6)
> 
> ⟨u, v⟩_w = 2·(1·4) + 3·(2·5) + 1·(3·6)
>          = 2·4 + 3·10 + 1·18
>          = 8 + 30 + 18
>          = 56
> 
> Comparar con producto estándar:
> ⟨u, v⟩ = 32
> 
> El producto ponderado da más importancia a las
> componentes con pesos mayores.
> ```
> 
> **Aplicación práctica:**
> 
> ```mermaid
> graph LR
>     A[Datos: temperatura, humedad, presión] --> B[Pesos: 1, 3, 2]
>     B --> C[Producto ponderado]
>     C --> D[Humedad tiene más<br/>impacto en el resultado]
>     
>     style B fill:#fff4e1
>     style D fill:#e1ffe1
> ```

### 📊 Ejemplo 3: Producto Interno en $C[a,b]$

> [!example]- 📈 Funciones Continuas
> 
> **Definición:**
> 
> Sea $C[a,b]$ el espacio de funciones continuas en el intervalo $[a,b]$:
> 
> $$\langle f, g \rangle = \int_a^b f(x)g(x) , dx$$
> 
> **Interpretación geométrica:**
> 
> - Si $f$ y $g$ son ambas positivas: el producto interno mide el "área de solapamiento"
> - Si $f$ y $g$ tienen signos opuestos en algunos lugares: el producto puede ser pequeño o cero
> 
> ```mermaid
> graph TD
>     A[Funciones f y g] --> B[Multiplicar punto a punto<br/>f·x·g·x]
>     B --> C["Integrar sobre [a,b]"]
>     C --> D[⟨f,g⟩ = ∫ f·x·g·x dx]
>     
>     style A fill:#e1f5ff
>     style D fill:#e1ffe1
> ```
> 
> **Ejemplo 1: Funciones polinomiales**
> 
> ```
> f(x) = x,  g(x) = x²  en [0,1]
> 
> ⟨f, g⟩ = ∫₀¹ x · x² dx
>        = ∫₀¹ x³ dx
>        = [x⁴/4]₀¹
>        = 1/4 - 0
>        = 1/4
> ```
> 
> **Ejemplo 2: Funciones trigonométricas**
> 
> ```
> f(x) = sin(x),  g(x) = cos(x)  en [0,2π]
> 
> ⟨f, g⟩ = ∫₀²π sin(x)cos(x) dx
>        = ∫₀²π (1/2)sin(2x) dx
>        = [-cos(2x)/4]₀²π
>        = 0
> 
> ¡Son ortogonales!
> ```
> 
> **Ejemplo 3: Funciones idénticas**
> 
> ```
> f(x) = x  en [0,1]
> 
> ⟨f, f⟩ = ∫₀¹ x² dx
>        = [x³/3]₀¹
>        = 1/3
> ```
> 
> **Verificación de axiomas:**
> 
> |Axioma|Verificación|
> |---|---|
> |**PI1**|$\int_a^b (\alpha f + g)h , dx = \alpha\int_a^b fh , dx + \int_a^b gh , dx$ (linealidad de la integral) ✅|
> |**PI2**|$\int_a^b fg , dx = \int_a^b gf , dx$ (conmutatividad del producto) ✅|
> |**PI3**|$\int_a^b f^2 , dx \geq 0$ (integrando no negativo) ✅|
> |**PI4**|Si $\int_a^b f^2 , dx = 0$ y $f$ continua $\Rightarrow f = 0$ ✅|

### 📊 Ejemplo 4: Producto Interno con Función Peso

> [!example]- 🎚️ Pesos Variables
> 
> **Definición:**
> 
> Con una función peso $w(x) > 0$ continua en $[a,b]$:
> 
> $$\langle f, g \rangle_w = \int_a^b w(x)f(x)g(x) , dx$$
> 
> **Interpretación:**
> 
> La función peso $w(x)$ da más o menos importancia a diferentes regiones del intervalo.
> 
> **Ejemplos de funciones peso comunes:**
> 
> |Función Peso|Nombre|Uso|
> |---|---|---|
> |$w(x) = 1$|Uniforme|Producto estándar|
> |$w(x) = x$|Lineal|Más peso cerca de $b$|
> |$w(x) = e^{-x}$|Exponencial|Decae con $x$|
> |$w(x) = \frac{1}{\sqrt{1-x^2}}$|Chebyshev|Polinomios de Chebyshev|
> 
> **Ejemplo numérico:**
> 
> ```
> f(x) = x,  g(x) = 1,  w(x) = x  en [0,1]
> 
> ⟨f, g⟩_w = ∫₀¹ x · x · 1 dx
>          = ∫₀¹ x² dx
>          = 1/3
> 
> Sin peso:
> ⟨f, g⟩ = ∫₀¹ x · 1 dx = 1/2
> 
> La función peso cambia el resultado!
> ```
> 
> **Aplicación en polinomios ortogonales:**
> 
> ```mermaid
> graph TD
>     A[Intervalo y función peso] --> B[Definen familia de<br/>polinomios ortogonales]
>     B --> C{Ejemplos}
>     C --> D["w·x = 1 en [-1,1]<br/>→ Polinomios de Legendre"]
>     C --> E["w·x = 1/√·1-x² en [-1,1]<br/>→ Polinomios de Chebyshev"]
>     C --> F["w·x = e⁻ˣ en [0,∞]<br/>→ Polinomios de Laguerre"]
>     
>     style B fill:#e1ffe1
> ```

### 📊 Ejemplo 5: Producto de Frobenius en Matrices

> [!example]- 📐 Matrices como Vectores
> 
> **Definición:**
> 
> Para matrices $A, B \in \mathbb{R}^{m \times n}$:
> 
> $$\langle A, B \rangle = \text{tr}(A^T B) = \sum_{i=1}^m \sum_{j=1}^n a_{ij}b_{ij}$$
> 
> donde $\text{tr}$ denota la traza (suma de elementos diagonales).
> 
> **Interpretación:**
> 
> Tratamos a las matrices como vectores "aplanados" y tomamos el producto punto.
> 
> **Ejemplo numérico:**
> 
> ```
> A = [1  2]    B = [5  6]
>     [3  4]        [7  8]
> 
> ⟨A, B⟩ = 1·5 + 2·6 + 3·7 + 4·8
>        = 5 + 12 + 21 + 32
>        = 70
> 
> Alternativamente:
> A^T B = [1  3] [5  6] = [26  30]
>         [2  4] [7  8]   [38  44]
> 
> tr(A^T B) = 26 + 44 = 70 ✅
> ```
> 
> **Casos especiales:**
> 
> ```
> Matrices idénticas:
> A = [1  2]
>     [3  4]
> 
> ⟨A, A⟩ = 1² + 2² + 3² + 4² = 30
> 
> Esta es la norma de Frobenius al cuadrado:
> ‖A‖²_F = 30
> ```
> 
> **Propiedades:**
> 
> |Propiedad|Expresión|
> |---|---|
> |**Relación con traza**|$\langle A, B \rangle = \text{tr}(A^T B) = \text{tr}(B^T A)$|
> |**Vectorización**|Si $\text{vec}(A)$ aplana $A$ en un vector, $\langle A, B \rangle = \text{vec}(A)^T \text{vec}(B)$|
> |**Norma inducida**|$\|A\|_F = \sqrt{\langle A, A \rangle}$ (norma de Frobenius)|

---

## 🔍 Propiedades Derivadas

> [!success]- ⚡ Consecuencias de los Axiomas
> 
> De los cuatro axiomas fundamentales, podemos derivar propiedades adicionales importantes:
> 
> ### Propiedad 1: Linealidad en el Segundo Argumento (Espacios Reales)
> 
> **Teorema:** En espacios reales, por simetría:
> 
> $$\langle \mathbf{u}, \alpha\mathbf{v} + \mathbf{w} \rangle = \alpha\langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{u}, \mathbf{w} \rangle$$
> 
> **Demostración:**
> 
> ```
> ⟨u, αv + w⟩ = ⟨αv + w, u⟩           (por simetría, PI2)
>             = α⟨v, u⟩ + ⟨w, u⟩      (por linealidad, PI1)
>             = α⟨u, v⟩ + ⟨u, w⟩      (por simetría nuevamente)
> ```
> 
> **Conclusión:** En espacios reales, el producto interno es **bilineal** (lineal en ambos argumentos).
> 
> ### Propiedad 2: Producto con el Vector Cero
> 
> $$\langle \mathbf{0}, \mathbf{v} \rangle = 0 \quad \text{y} \quad \langle \mathbf{v}, \mathbf{0} \rangle = 0$$
> 
> **Demostración:**
> 
> ```
> ⟨0, v⟩ = ⟨0·v, v⟩
>        = 0·⟨v, v⟩
>        = 0
> ```
> 
> ### Propiedad 3: Identidad de Polarización
> 
> **En espacios reales:**
> 
> $$\langle \mathbf{u}, \mathbf{v} \rangle = \frac{1}{4}\left(|\mathbf{u}+\mathbf{v}|^2 - |\mathbf{u}-\mathbf{v}|^2\right)$$
> 
> **Interpretación:** Podemos recuperar el producto interno si solo conocemos la norma.
> 
> **Demostración:**
> 
> ```
> ‖u+v‖² = ⟨u+v, u+v⟩
>        = ⟨u,u⟩ + 2⟨u,v⟩ + ⟨v,v⟩
>        = ‖u‖² + 2⟨u,v⟩ + ‖v‖²
> 
> ‖u-v‖² = ‖u‖² - 2⟨u,v⟩ + ‖v‖²
> 
> Restando:
> ‖u+v‖² - ‖u-v‖² = 4⟨u,v⟩
> 
> ⟨u,v⟩ = (‖u+v‖² - ‖u-v‖²)/4
> ```
> 
> ### Propiedad 4: Identidad del Paralelogramo
> 
> $$|\mathbf{u}+\mathbf{v}|^2 + |\mathbf{u}-\mathbf{v}|^2 = 2\left(|\mathbf{u}|^2 + |\mathbf{v}|^2\right)$$
> 
> **Interpretación geométrica:**
> 
> ```mermaid
> graph TD
>     A[Paralelogramo con<br/>lados u y v] --> B[Suma de cuadrados<br/>de diagonales]
>     B --> C[= 2 × suma de cuadrados<br/>de los lados]
>     
>     style A fill:#e1f5ff
>     style C fill:#e1ffe1
> ```
> 
> **Ejemplo numérico:**
> 
> ```
> u = (3, 0),  v = (0, 4)
> 
> u + v = (3, 4)    →  ‖u+v‖² = 25
> u - v = (3, -4)   →  ‖u-v‖² = 25
> 
> Lado izquierdo: 25 + 25 = 50
> 
> ‖u‖² = 9,  ‖v‖² = 16
> Lado derecho: 2(9 + 16) = 50 ✅
> ```
> 
> ### Tabla Resumen de Propiedades
> 
> |Propiedad|Fórmula|Uso Principal|
> |---|---|---|
> |**Bilinealidad**|Lineal en ambos argumentos|Cálculos algebraicos|
> |**Producto con cero**|$\langle \mathbf{0}, \mathbf{v} \rangle = 0$|Simplificación|
> |**Polarización**|Recuperar $\langle \mathbf{u}, \mathbf{v} \rangle$ de normas|Teoría, verificación|
> |**Paralelogramo**|Relación entre diagonales y lados|Verificar si una norma proviene de un producto interno|

---

## 🎨 Visualización Geométrica

> [!tip]- 🗺️ Interpretación Geométrica del Producto Interno
> 
> ### Ángulo entre Vectores
> 
> Una vez definido el producto interno, podemos definir el **ángulo** $\theta$ entre dos vectores no nulos:
> 
> $$\cos \theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{|\mathbf{u}| \cdot |\mathbf{v}|}$$
> 
> donde $|\mathbf{v}| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$ es la norma inducida.
> 
> ```mermaid
> graph TD
>     A[⟨u,v⟩] --> B{Signo del<br/>producto}
>     B -->|> 0| C[Ángulo agudo<br/>0° < θ < 90°]
>     B -->|= 0| D[Ortogonales<br/>θ = 90°]
>     B -->|< 0| E[Ángulo obtuso<br/>90° < θ < 180°]
>     
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
>     style E fill:#ffe1e1
> ```
> 
> **Casos especiales:**
> 
> |Valor de $\cos\theta$|Ángulo $\theta$|Relación|Interpretación|
> |---|---|---|---|
> |$1$|$0°$|$\mathbf{v} = c\mathbf{u}$, $c > 0$|Misma dirección|
> |$> 0$|$0° < \theta < 90°$|Componentes alineadas|Agudo|
> |$0$|$90°$|$\langle \mathbf{u}, \mathbf{v} \rangle = 0$|Perpendiculares|
> |$< 0$|$90° < \theta < 180°$|Componentes opuestas|Obtuso|
> |$-1$|$180°$|$\mathbf{v} = c\mathbf{u}$, $c < 0$|Dirección opuesta|
> 
> **Ejemplo visual en $\mathbb{R}^2$:**
> 
> ```
> u = (1, 0)
> 
> v₁ = (1, 1)   →  cos θ = 1/√2  →  θ = 45°
> v₂ = (0, 1)   →  cos θ = 0     →  θ = 90°
> v₃ = (-1, 1)  →  cos θ = -1/√2 →  θ = 135°
> v₄ = (-1, 0)  →  cos θ = -1    →  θ = 180°
> ```

---

## 🔬 Verificación de Productos Internos

> [!warning]- ✅ ¿Cómo Verificar si una Función es un Producto Interno?
> 
> Para verificar que una función $\langle \cdot, \cdot \rangle$ es un producto interno válido, debemos verificar los **cuatro axiomas**.
> 
> ### Ejemplo: Verificar un Candidato
> 
> **Pregunta:** ¿Es $\langle \mathbf{u}, \mathbf{v} \rangle = u_1v_1 - u_2v_2$ un producto interno en $\mathbb{R}^2$?
> 
> **Solución:**
> 
> ```
> Verificar PI3 (Positividad):
> Para v = (1, 1):
> ⟨v, v⟩ = 1·1 - 1·1 = 0
> 
> Pero v ≠ 0, lo que viola PI4! ❌
> 
> Además, para v = (0, 1):
> ⟨v, v⟩ = 0·0 - 1·1 = -1 < 0
> 
> Esto viola PI3! ❌
> 
> Conclusión: NO es un producto interno.
> ```
> 
> ### Checklist de Verificación
> 
> ```mermaid
> graph TD
>     A[Candidato a<br/>producto interno] --> B{PI1: Linealidad?}
>     B -->|No| Z1[❌ NO es producto interno]
>     B -->|Sí| C{PI2: Simetría?}
>     C -->|No| Z2[❌ NO es producto interno]
>     C -->|Sí| D{PI3: Positividad?}
>     D -->|No| Z3[❌ NO es producto interno]
>     D -->|Sí| E{PI4: Definición positiva?}
>     E -->|No| Z4[❌ NO es producto interno]
>     E -->|Sí| F[✅ SÍ es producto interno]
>     
>     style F fill:#e1ffe1
>     style Z1 fill:#ffe1e1
>     style Z2 fill:#ffe1e1
>     style Z3 fill:#ffe1e1
>     style Z4 fill:#ffe1e1
> ```

---

## 📚 Ejemplos Adicionales

> [!example]- 🔢 Más Ejemplos Trabajados
> 
> ### Ejemplo 6: Producto Interno en $\mathbb{C}^n$
> 
> **Definición (Hermítico):**
> 
> $$\langle \mathbf{z}, \mathbf{w} \rangle = \sum_{i=1}^nz_i \overline{w_i}$$
> donde $\overline{w_i}$ es el conjugado complejo de $w_i$.
> 
> **Ejemplo:**
> 
> ```
> z = (1+i, 2)
> w = (1-i, 3i)
> 
> ⟨z, w⟩ = (1+i)·(1+i) + 2·(-3i)
>        = (1+i)·(1+i) - 6i
>        = 1 + 2i + i² - 6i
>        = 1 + 2i - 1 - 6i
>        = -4i
> 
> Verificar simetría hermítica:
> ⟨w, z⟩ = (1-i)·(1-i) + 3i·(-2i)
>        = (1-i)·(1-i) + 6
>        = 1 - 2i - 1 + 6
>        = 4i
> 
> ⟨w, z⟩ = 4i = conjugado de (-4i) = ⟨z, w⟩̄ ✅
> ```
> 
> ### Ejemplo 7: Producto en Polinomios
> 
> **Espacio:** $P_n$ (polinomios de grado ≤ n)
> 
> **Producto interno:**
> 
> $$\langle p, q \rangle = \int_{-1}^1 p(x)q(x) , dx$$
> 
> **Ejemplo:**
> 
> ```
> p(x) = 1
> q(x) = x
> 
> ⟨p, q⟩ = ∫₋₁¹ 1·x dx
>        = [x²/2]₋₁¹
>        = 1/2 - 1/2
>        = 0
> 
> ¡Los polinomios constantes y lineales son ortogonales!
> ```
> 
> ### Ejemplo 8: Producto en Secuencias
> 
> **Espacio:** $\ell^2$ (secuencias de cuadrado sumable)
> 
> $$\langle (a_n), (b_n) \rangle = \sum_{n=1}^\infty a_n b_n$$
> 
> (cuando la serie converge)
> 
> **Ejemplo:**
> 
> ```
> a_n = 1/2ⁿ
> b_n = 1/3ⁿ
> 
> ⟨(a_n), (b_n)⟩ = ∑_{n=1}^∞ (1/2ⁿ)·(1/3ⁿ)
>                = ∑_{n=1}^∞ 1/6ⁿ
>                = (1/6)/(1-1/6)
>                = (1/6)/(5/6)
>                = 1/5
> ```

---

## 🎯 Aplicaciones del Producto Interno

> [!quote]- 🌍 Usos en el Mundo Real
> 
> ### 1. Geometría y Visualización
> 
> - **Cálculo de ángulos** entre vectores
> - **Determinación de ortogonalidad**
> - **Proyecciones** de vectores
> 
> ### 2. Física
> 
> - **Trabajo mecánico:** $W = \mathbf{F} \cdot \mathbf{d}$
> - **Flujo eléctrico/magnético**
> - **Mecánica cuántica:** estados cuánticos y productos internos
> 
> ### 3. Procesamiento de Señales
> 
> - **Correlación** entre señales
> - **Análisis de Fourier**
> - **Filtrado** de señales
> 
> ### 4. Machine Learning
> 
> - **Similitud entre vectores de características**
> - **Kernels** en SVM
> - **Análisis de componentes principales (PCA)**
> 
> ### 5. Estadística
> 
> - **Correlación** entre variables
> - **Regresión** por mínimos cuadrados
> - **Análisis multivariado**
> 
> ```mermaid
> mindmap
>   root((Producto<br/>Interno))
>     Geometría
>       Ángulos
>       Distancias
>       Proyecciones
>     Física
>       Trabajo
>       Campos
>       Cuántica
>     Señales
>       Correlación
>       Fourier
>       Filtros
>     ML/AI
>       Similitud
>       Kernels
>       PCA
>     Estadística
>       Correlación
>       Regresión
>       Multivariado
> ```

---

## 🧩 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> ### Nivel Básico
> 
> **1.** Calcula $\langle \mathbf{u}, \mathbf{v} \rangle$ con el producto punto estándar:
> 
> - $\mathbf{u} = (2, -1, 3)$, $\mathbf{v} = (1, 4, -2)$
> 
> **2.** Verifica que $\langle \mathbf{u}, \mathbf{v} \rangle = 2u_1v_1 + 3u_2v_2$ satisface los axiomas del producto interno en $\mathbb{R}^2$.
> 
> **3.** Calcula $\langle f, g \rangle$ donde:
> 
> - $f(x) = 1$, $g(x) = x^2$ en $[0,1]$
> - Producto: $\langle f, g \rangle = \int_0^1 f(x)g(x) , dx$
> 
> ### Nivel Intermedio
> 
> **4.** Demuestra que $\langle \mathbf{u}, \mathbf{v} \rangle = u_1v_1 + 2u_2v_2 + u_1v_2 + u_2v_1$ **NO** es un producto interno en $\mathbb{R}^2$.
> 
> **5.** Encuentra el ángulo entre $\mathbf{u} = (1, 2, 2)$ y $\mathbf{v} = (2, 1, 2)$ usando el producto punto estándar.
> 
> **6.** Calcula $\langle p, q \rangle$ donde:
> 
> - $p(x) = x$, $q(x) = x^2 - 1/3$ en $[-1,1]$
> - Producto: $\langle p, q \rangle = \int_{-1}^1 p(x)q(x) , dx$
> 
> ### Nivel Avanzado
> 
> **7.** Demuestra la identidad de polarización para cualquier producto interno en un espacio real.
> 
> **8.** Sea $\langle \cdot, \cdot \rangle$ un producto interno. Demuestra que si $\langle \mathbf{u}, \mathbf{v} \rangle = 0$ para todo $\mathbf{v} \in V$, entonces $\mathbf{u} = \mathbf{0}$.
> 
> **9.** Encuentra una función peso $w(x)$ tal que los polinomios $p(x) = 1$ y $q(x) = x$ sean ortogonales en $[0,1]$ con el producto: $$\langle p, q \rangle_w = \int_0^1 w(x)p(x)q(x) , dx$$

---

## 📖 Resumen del Capítulo

> [!abstract]- 📝 Puntos Clave
> 
> ### Conceptos Fundamentales
> 
> |Concepto|Descripción|Notación|
> |---|---|---|
> |**Producto interno**|Función bilineal, simétrica, positiva definida|$\langle \mathbf{u}, \mathbf{v} \rangle$|
> |**Cuatro axiomas**|PI1-PI4: linealidad, simetría, positividad, def. positiva|-|
> |**Ejemplos clásicos**|Producto punto, integral de funciones, Frobenius|Varios|
> 
> ### Fórmulas Esenciales \
> 
> $$\begin{align} \text{Producto punto:} & \quad \langle \mathbf{u}, \mathbf{v} \rangle = \sum_{i=1}^n u_i v_i \\[8pt] \text{Integral:} & \quad \langle f, g \rangle = \int_a^b f(x)g(x) , dx \\[8pt] \text{Ángulo:} & \quad \cos\theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{|\mathbf{u}| \cdot |\mathbf{v}|} \end{align}$$
> 
> ### Propiedades Importantes
> 
> - Bilinealidad (espacios reales)
> - Identidad de polarización
> - Identidad del paralelogramo
> - Induce norma y distancia
> 
> ### Próximo Tema
> 
> En el siguiente capítulo estudiaremos la **norma inducida** y la **distancia** que surgen naturalmente del producto interno.

---

**Tags:** #algebra-lineal #producto-interno #espacios-vectoriales #bilineal #norma #geometria
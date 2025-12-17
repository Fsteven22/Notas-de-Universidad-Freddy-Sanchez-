# 📏 Norma Inducida y Distancia

## 🎯 Introducción

> [!info]- 💡 De Producto Interno a Geometría
> 
> Una vez que tenemos un producto interno en un espacio vectorial, automáticamente obtenemos dos conceptos geométricos fundamentales:
> 
> 1. **Norma** (longitud de vectores)
> 2. **Distancia** (separación entre vectores)
> 
> **Analogía intuitiva:**
> 
> - El **producto interno** es como tener una "regla flexible" que nos permite medir
> - La **norma** es usar esa regla para medir la longitud de una flecha
> - La **distancia** es usar esa regla para medir cuán separados están dos puntos
> 
> ```mermaid
> graph LR
>     A[Producto Interno<br/>⟨·,·⟩] --> B[Norma<br/>‖·‖]
>     B --> C[Distancia<br/>d·,·]
>     A -.->|También define| D[Ángulo<br/>θ]
>     
>     style A fill:#e1ffe1
>     style B fill:#fff4e1
>     style C fill:#e1f5ff
>     style D fill:#f0e1ff
> ```
> 
> **Jerarquía de estructuras:**
> 
> |Estructura|Requiere|Proporciona|Ejemplo|
> |---|---|---|---|
> |**Espacio Vectorial**|Suma, producto por escalar|Estructura algebraica|$\mathbb{R}^n$|
> |**+ Producto Interno**|$\langle \cdot, \cdot \rangle$|Geometría (ángulos)|$(\mathbb{R}^n, \cdot)$|
> |**+ Norma**|$\|\cdot\|$|Longitudes|Espacio normado|
> |**+ Distancia**|$d(\cdot, \cdot)$|Topología (cercanía)|Espacio métrico|

---

## 📐 Norma Inducida por el Producto Interno

### 🔍 Definición

> [!note]- 📏 ¿Qué es la Norma?
> 
> Sea $V$ un espacio vectorial con producto interno $\langle \cdot, \cdot \rangle$. La **norma inducida** de un vector $\mathbf{v} \in V$ es:
> 
> $$|\mathbf{v}| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$$
> 
> **Interpretación geométrica:**
> 
> La norma $|\mathbf{v}|$ representa la **longitud** o **magnitud** del vector $\mathbf{v}$.
> 
> ```mermaid
> graph TD
>     A[Vector v] --> B[Producto interno<br/>consigo mismo]
>     B --> C[⟨v, v⟩]
>     C --> D[Raíz cuadrada]
>     D --> E[‖v‖ = √⟨v,v⟩<br/>Longitud]
>     
>     style A fill:#e1f5ff
>     style C fill:#fff4e1
>     style E fill:#e1ffe1
> ```
> 
> **Notación:**
> 
> - $|\mathbf{v}|$ se lee "norma de ve" o "longitud de ve"
> - También se denota $|\mathbf{v}|_2$ en algunos contextos (norma euclidiana)

### ⚖️ Axiomas de la Norma

> [!success]- ✅ Propiedades que debe Satisfacer
> 
> Toda norma inducida por un producto interno satisface las siguientes propiedades para todo $\mathbf{u}, \mathbf{v} \in V$ y todo escalar $\alpha$:
> 
> |#|Nombre|Expresión|Significado|
> |---|---|---|---|
> |**N1**|**No negatividad**|$\|\mathbf{v}\| \geq 0$|Las longitudes son positivas|
> |**N2**|**Definición positiva**|$\|\mathbf{v}\| = 0 \iff \mathbf{v} = \mathbf{0}$|Solo el cero tiene longitud cero|
> |**N3**|**Homogeneidad**|$\|\alpha\mathbf{v}\| = \|\alpha\| \cdot \|\mathbf{v}\|$|Escalar multiplica la longitud|
> |**N4**|**Desigualdad triangular**|$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$|Camino directo más corto|
> 
> **Verificación de axiomas:**
> 
> ```mermaid
> graph TD
>     A[Norma ‖·‖ inducida] --> B[N1: ‖v‖ ≥ 0]
>     A --> C[N2: ‖v‖ = 0 ⟺ v = 0]
>     A --> D[N3: ‖αv‖ = |α|‖v‖]
>     A --> E[N4: ‖u+v‖ ≤ ‖u‖ + ‖v‖]
>     
>     B --> F[✅ De PI3]
>     C --> G[✅ De PI4]
>     D --> H[✅ De PI1]
>     E --> I[✅ De Cauchy-Schwarz]
>     
>     style A fill:#e1ffe1
>     style F fill:#e1ffe1
>     style G fill:#e1ffe1
>     style H fill:#e1ffe1
>     style I fill:#e1ffe1
> ```

### 📊 Demostración de Propiedades

> [!example]- 🔍 Pruebas de los Axiomas
> 
> **Demostración N1 (No negatividad):**
> 
> $$|\mathbf{v}| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle} \geq 0$$
> 
> porque:
> 
> - $\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$ por el axioma PI3 del producto interno
> - La raíz cuadrada de un número no negativo es no negativa
> 
> ∎
> 
> **Demostración N2 (Definición positiva):**
> 
> $$|\mathbf{v}| = 0 \iff \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle} = 0 \iff \langle \mathbf{v}, \mathbf{v} \rangle = 0 \iff \mathbf{v} = \mathbf{0}$$
> 
> La última equivalencia es el axioma PI4 del producto interno.
> 
> ∎
> 
> **Demostración N3 (Homogeneidad):**
> 
> $$\begin{align} |\alpha\mathbf{v}| &= \sqrt{\langle \alpha\mathbf{v}, \alpha\mathbf{v} \rangle} \ &= \sqrt{\alpha\langle \mathbf{v}, \alpha\mathbf{v} \rangle} \quad \text{(linealidad, PI1)} \ &= \sqrt{\alpha \cdot \alpha \langle \mathbf{v}, \mathbf{v} \rangle} \ &= \sqrt{\alpha^2 \langle \mathbf{v}, \mathbf{v} \rangle} \ &= |\alpha| \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle} \ &= |\alpha| \cdot |\mathbf{v}| \end{align}$$
> 
> ∎
> 
> **Demostración N4 (Desigualdad triangular):**
> 
> Esta es más compleja y la demostraremos en el capítulo 07. Requiere la desigualdad de Cauchy-Schwarz.

---

## 🌟 Ejemplos de Normas Inducidas

### 📊 Ejemplo 1: Norma Euclidiana en $\mathbb{R}^n$

> [!example]- 📐 La Norma Más Común
> 
> **Producto interno:** $\langle \mathbf{u}, \mathbf{v} \rangle = \sum_{i=1}^n u_i v_i$
> 
> **Norma inducida:**
> 
> $$|\mathbf{v}| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle} = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} = \sqrt{\sum_{i=1}^n v_i^2}$$
> 
> **Ejemplos numéricos:**
> 
> ```
> En ℝ²:
> v = (3, 4)
> ‖v‖ = √(3² + 4²) = √(9 + 16) = √25 = 5
> 
> En ℝ³:
> v = (1, 2, 2)
> ‖v‖ = √(1² + 2² + 2²) = √(1 + 4 + 4) = √9 = 3
> 
> En ℝ⁴:
> v = (1, 1, 1, 1)
> ‖v‖ = √(1 + 1 + 1 + 1) = √4 = 2
> ```
> 
> **Interpretación geométrica en $\mathbb{R}^2$ y $\mathbb{R}^3$:**
> 
> - En $\mathbb{R}^2$: Es la longitud de la hipotenusa (Teorema de Pitágoras)
> - En $\mathbb{R}^3$: Es la diagonal del paralelepípedo
> 
> ```mermaid
> graph TD
>     A[Vector v = ·3, 4] --> B[Componente x: 3]
>     A --> C[Componente y: 4]
>     B --> D[Triángulo rectángulo]
>     C --> D
>     D --> E[Hipotenusa = ‖v‖ = 5]
>     
>     style A fill:#e1f5ff
>     style E fill:#e1ffe1
> ```
> 
> **Casos especiales:**
> 
> |Vector|Norma|Observación|
> |---|---|---|
> |$(1, 0, 0, \ldots, 0)$|$1$|Vector canónico unitario|
> |$(a, a, \ldots, a)$ ($n$ componentes)|$|a|
> |$\mathbf{0}$|$0$|Único vector con norma cero|

### 📊 Ejemplo 2: Norma Ponderada en $\mathbb{R}^n$

> [!example]- ⚖️ Con Pesos Diferentes
> 
> **Producto interno ponderado:** $\langle \mathbf{u}, \mathbf{v} \rangle_w = \sum_{i=1}^n w_i u_i v_i$ con $w_i > 0$
> 
> **Norma inducida:**
> 
> $$|\mathbf{v}|_w = \sqrt{\sum_{i=1}^n w_i v_i^2}$$
> 
> **Ejemplo numérico:**
> 
> ```
> En ℝ³ con pesos w = (2, 3, 1):
> v = (1, 2, 3)
> 
> ‖v‖_w = √(2·1² + 3·2² + 1·3²)
>       = √(2·1 + 3·4 + 1·9)
>       = √(2 + 12 + 9)
>       = √23
>       ≈ 4.80
> 
> Comparar con norma estándar:
> ‖v‖ = √(1 + 4 + 9) = √14 ≈ 3.74
> 
> La norma ponderada da más importancia a la
> segunda componente (peso = 3).
> ```
> 
> **Interpretación:**
> 
> |Peso $w_i$|Efecto en la norma|
> |---|---|
> |$w_i > 1$|Aumenta la contribución de la componente $i$|
> |$w_i = 1$|Norma estándar|
> |$0 < w_i < 1$|Disminuye la contribución de la componente $i$|
> 
> **Aplicación práctica:**
> 
> En procesamiento de datos, los pesos pueden representar la importancia relativa de diferentes características.

### 📊 Ejemplo 3: Norma $L^2$ en $C[a,b]$

> [!example]- 📈 Norma de Funciones
> 
> **Producto interno:** $\langle f, g \rangle = \int_a^b f(x)g(x) , dx$
> 
> **Norma inducida ($L^2$-norma):**
> 
> $$|f| = \sqrt{\langle f, f \rangle} = \sqrt{\int_a^b f(x)^2 , dx}$$
> 
> **Ejemplos numéricos:**
> 
> ```
> Ejemplo 1: f(x) = x en [0,1]
> 
> ‖f‖ = √∫₀¹ x² dx
>     = √[x³/3]₀¹
>     = √(1/3)
>     = 1/√3
>     ≈ 0.577
> 
> Ejemplo 2: f(x) = sin(x) en [0,π]
> 
> ‖f‖ = √∫₀^π sin²(x) dx
>     = √∫₀^π (1-cos(2x))/2 dx
>     = √[x/2 - sin(2x)/4]₀^π
>     = √(π/2)
>     ≈ 1.253
> 
> Ejemplo 3: f(x) = 1 (función constante) en [a,b]
> 
> ‖f‖ = √∫_a^b 1² dx
>     = √(b - a)
> ```
> 
> **Interpretación:**
> 
> La norma $L^2$ mide la "energía" o "tamaño" de una función en el intervalo.
> 
> **Propiedades:**
> 
> |Función|Norma en $[a,b]$|Observación|
> |---|---|---|
> |$f(x) = c$ (constante)|$|c|
> |$f(x) = 0$|$0$|Única función con norma cero|
> |$\|f\|$ grande|-|Función "oscila mucho" o tiene valores grandes|

### 📊 Ejemplo 4: Norma de Frobenius

> [!example]- 🔲 Norma de Matrices
> 
> **Producto interno de Frobenius:** $\langle A, B \rangle = \text{tr}(A^T B) = \sum_{i,j} a_{ij}b_{ij}$
> 
> **Norma inducida (norma de Frobenius):**
> 
> $$|A|_F = \sqrt{\langle A, A \rangle} = \sqrt{\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2}$$
> 
> **Ejemplo numérico:**
> 
> ```
> A = [1  2]
>     [3  4]
> 
> ‖A‖_F = √(1² + 2² + 3² + 4²)
>       = √(1 + 4 + 9 + 16)
>       = √30
>       ≈ 5.48
> 
> B = [2  0]
>     [0  3]
> 
> ‖B‖_F = √(4 + 0 + 0 + 9)
>       = √13
>       ≈ 3.61
> ```
> 
> **Propiedades especiales:**
> 
> |Propiedad|Expresión|Uso|
> |---|---|---|
> |**Invariancia ortogonal**|$\|UAV\|_F = \|A\|_F$ si $U, V$ ortogonales|Cambios de base|
> |**Relación con traza**|$\|A\|_F^2 = \text{tr}(A^T A)$|Cálculo eficiente|
> |**Suma de valores singulares**|$\|A\|_F^2 = \sum \sigma_i^2$|Análisis espectral|

---

## 📐 Distancia Inducida

### 🔍 Definición

> [!note]- 🗺️ Midiendo Separación entre Vectores
> 
> Sea $V$ un espacio con producto interno y norma inducida $|\cdot|$. La **distancia** entre dos vectores $\mathbf{u}, \mathbf{v} \in V$ es:
> 
> $$d(\mathbf{u}, \mathbf{v}) = |\mathbf{u} - \mathbf{v}|$$
> 
> **Interpretación geométrica:**
> 
> La distancia $d(\mathbf{u}, \mathbf{v})$ es la longitud del vector diferencia $\mathbf{u} - \mathbf{v}$.
> 
> ```mermaid
> graph TD
>     A[Vectores u y v] --> B[Diferencia u - v]
>     B --> C[Norma de la diferencia]
>     C --> D[d·u,v = ‖u - v‖]
>     
>     style A fill:#e1f5ff
>     style D fill:#e1ffe1
> ```
> 
> **Expandiendo la definición:**
> 
> $$d(\mathbf{u}, \mathbf{v}) = |\mathbf{u} - \mathbf{v}| = \sqrt{\langle \mathbf{u} - \mathbf{v}, \mathbf{u} - \mathbf{v} \rangle}$$

### ⚖️ Axiomas de la Métrica

> [!success]- ✅ Propiedades de la Distancia
> 
> La distancia inducida satisface los axiomas de una **métrica**:
> 
> |#|Nombre|Expresión|Significado|
> |---|---|---|---|
> |**M1**|**No negatividad**|$d(\mathbf{u}, \mathbf{v}) \geq 0$|Distancias son positivas|
> |**M2**|**Identidad de indiscernibles**|$d(\mathbf{u}, \mathbf{v}) = 0 \iff \mathbf{u} = \mathbf{v}$|Solo puntos idénticos tienen distancia cero|
> |**M3**|**Simetría**|$d(\mathbf{u}, \mathbf{v}) = d(\mathbf{v}, \mathbf{u})$|No importa el orden|
> |**M4**|**Desigualdad triangular**|$d(\mathbf{u}, \mathbf{w}) \leq d(\mathbf{u}, \mathbf{v}) + d(\mathbf{v}, \mathbf{w})$|El rodeo no es más corto|
> 
> **Verificación de axiomas:**
> 
> ```mermaid
> graph TD
>     A[Distancia d·,·] --> B[M1: d·u,v ≥ 0]
>     A --> C[M2: d·u,v = 0 ⟺ u = v]
>     A --> D[M3: d·u,v = d·v,u]
>     A --> E[M4: Desigualdad triangular]
>     
>     B --> F[✅ De N1]
>     C --> G[✅ De N2]
>     D --> H[✅ De simetría de ‖·‖]
>     E --> I[✅ De N4]
>     
>     style A fill:#e1ffe1
> ```

### 📊 Demostración de Propiedades

> [!example]- 🔍 Pruebas de los Axiomas
> 
> **Demostración M1 (No negatividad):**
> 
> $$d(\mathbf{u}, \mathbf{v}) = |\mathbf{u} - \mathbf{v}| \geq 0$$
> 
> porque toda norma es no negativa (axioma N1).
> 
> ∎
> 
> **Demostración M2 (Identidad de indiscernibles):**
> 
> $$\begin{align} d(\mathbf{u}, \mathbf{v}) = 0 &\iff |\mathbf{u} - \mathbf{v}| = 0 \ &\iff \mathbf{u} - \mathbf{v} = \mathbf{0} \quad \text{(por N2)} \ &\iff \mathbf{u} = \mathbf{v} \end{align}$$
> 
> ∎
> 
> **Demostración M3 (Simetría):**
> 
> $$\begin{align} d(\mathbf{u}, \mathbf{v}) &= |\mathbf{u} - \mathbf{v}| \ &= |(-1)(\mathbf{v} - \mathbf{u})| \ &= |-1| \cdot |\mathbf{v} - \mathbf{u}| \quad \text{(por N3)} \ &= |\mathbf{v} - \mathbf{u}| \ &= d(\mathbf{v}, \mathbf{u}) \end{align}$$
> 
> ∎
> 
> **Demostración M4 (Desigualdad triangular):**
> 
> $$\begin{align} d(\mathbf{u}, \mathbf{w}) &= |\mathbf{u} - \mathbf{w}| \ &= |(\mathbf{u} - \mathbf{v}) + (\mathbf{v} - \mathbf{w})| \ &\leq |\mathbf{u} - \mathbf{v}| + |\mathbf{v} - \mathbf{w}| \quad \text{(por N4)} \ &= d(\mathbf{u}, \mathbf{v}) + d(\mathbf{v}, \mathbf{w}) \end{align}$$
> 
> ∎

---

## 🌟 Ejemplos de Distancias

### 📊 Ejemplo 1: Distancia Euclidiana en $\mathbb{R}^n$

> [!example]- 📐 La Distancia Estándar
> 
> **Fórmula:**
> 
> $$d(\mathbf{u}, \mathbf{v}) = |\mathbf{u} - \mathbf{v}| = \sqrt{\sum_{i=1}^n (u_i - v_i)^2}$$
> 
> **Ejemplos numéricos:**
> 
> ```
> En ℝ²:
> u = (1, 2),  v = (4, 6)
> 
> d(u, v) = √((1-4)² + (2-6)²)
>         = √((-3)² + (-4)²)
>         = √(9 + 16)
>         = √25
>         = 5
> 
> En ℝ³:
> u = (0, 0, 0),  v = (1, 2, 2)
> 
> d(u, v) = √(1² + 2² + 2²)
>         = √9
>         = 3
> 
> En ℝ⁴:
> u = (1, 2, 3, 4),  v = (2, 3, 4, 5)
> 
> d(u, v) = √(1² + 1² + 1² + 1²)
>         = √4
>         = 2
> ```
> 
> **Interpretación geométrica:**
> 
> - En $\mathbb{R}^2$: Distancia en línea recta entre dos puntos
> - En $\mathbb{R}^3$: Distancia "como vuela el pájaro"
> 
> **Casos especiales:**
> 
> |Vectores|Distancia|Observación|
> |---|---|---|
> |$\mathbf{u}, \mathbf{u}$|$0$|Distancia a sí mismo|
> |$\mathbf{u}, -\mathbf{u}$|$2\|\mathbf{u}\|$|Vectores opuestos|
> |Ortogonales con $\|\mathbf{u}\|=\|\mathbf{v}\|=1$|$\sqrt{2}$|Diagonal de cuadrado unitario|

### 📊 Ejemplo 2: Distancia entre Funciones

> [!example]- 📈 Distancia $L^2$
> 
> **Fórmula:**
> 
> $$d(f, g) = |f - g| = \sqrt{\int_a^b (f(x) - g(x))^2 , dx}$$
> 
> **Ejemplos numéricos:**
> 
> ```
> Ejemplo 1: f(x) = x, g(x) = x² en [0,1]
> 
> d(f, g) = √∫₀¹ (x - x²)² dx
>         = √∫₀¹ (x² - 2x³ + x⁴) dx
>         = √[x³/3 - x⁴/2 + x⁵/5]₀¹
>         = √(1/3 - 1/2 + 1/5)
>         = √(10/30 - 15/30 + 6/30)
>         = √(1/30)
>         ≈ 0.183
> 
> Ejemplo 2: f(x) = 1, g(x) = x en [0,1]
> 
> d(f, g) = √∫₀¹ (1 - x)² dx
>         = √∫₀¹ (1 - 2x + x²) dx
>         = √[x - x² + x³/3]₀¹
>         = √(1 - 1 + 1/3)
>         = √(1/3)
>         ≈ 0.577
> ```
> 
> **Interpretación:**
> 
> La distancia $L^2$ mide qué tan "diferentes" son dos funciones en promedio sobre el intervalo.

### 📊 Ejemplo 3: Distancia de Frobenius entre Matrices

> [!example]- 🔲 Distancia entre Matrices
> 
> **Fórmula:**
> 
> $$d(A, B) = |A - B|_F = \sqrt{\sum_{i,j} (a_{ij} - b_{ij})^2}$$
> 
> **Ejemplo numérico:**
> 
> ```
> A = [1  2]    B = [2  3]
>     [3  4]        [4  5]
> 
> A - B = [-1  -1]
>         [-1  -1]
> 
> d(A, B) = √(1 + 1 + 1 + 1)
>         = √4
>         = 2
> ```
> 
> **Aplicación:**
> 
> Útil para medir el "error" entre matrices en aproximaciones numéricas.

---

## 🔗 Relaciones entre Norma y Distancia

> [!tip]- 🎨 Conexiones Importantes
> 
> ### Relación Fundamental
> 
> $$d(\mathbf{u}, \mathbf{v}) = |\mathbf{u} - \mathbf{v}|$$
> 
> **Consecuencias:**
> 
> |Propiedad de Norma|Propiedad de Distancia Correspondiente|
> |---|---|
> |$\|\mathbf{v}\| \geq 0$|$d(\mathbf{u}, \mathbf{v}) \geq 0$|
> |$\|\mathbf{v}\| = 0 \iff \mathbf{v} = \mathbf{0}$|$d(\mathbf{u}, \mathbf{v}) = 0 \iff \mathbf{u} = \mathbf{v}$|
> |$\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$|$d(\mathbf{u}, \mathbf{w}) \leq d(\mathbf{u}, \mathbf{v}) + d(\mathbf{v}, \mathbf{w})$|
> 
> ### Desigualdad Triangular Inversa
> 
> $$\big| |\mathbf{u}| - |\mathbf{v}| \big| \leq d(\mathbf{u}, \mathbf{v})$$
> > **Demostración:**
> 
> ```
> Por desigualdad triangular:
> ‖u‖ = ‖u - v + v‖ ≤ ‖u - v‖ + ‖v‖
> 
> Por lo tanto:
> ‖u‖ - ‖v‖ ≤ ‖u - v‖
> 
> Similarmente:
> ‖v‖ - ‖u‖ ≤ ‖v - u‖ = ‖u - v‖
> 
> Combinando:
> |‖u‖ - ‖v‖| ≤ ‖u - v‖ = d(u, v)
> ```
> 
> **Interpretación:**
> 
> La diferencia de longitudes nunca excede la distancia entre los vectores.

---

## 📊 Propiedades Adicionales

> [!note]- 🔍 Más Relaciones Útiles
> 
> ### Norma de la Suma y Diferencia
> 
> **Identidad del paralelogramo:**
> 
> $$|\mathbf{u} + \mathbf{v}|^2 + |\mathbf{u} - \mathbf{v}|^2 = 2(|\mathbf{u}|^2 + |\mathbf{v}|^2)$$
> 
> **En términos de distancia:**
> 
> $$d(\mathbf{u}, \mathbf{v})^2 + |\mathbf{u} + \mathbf{v}|^2 = 2(|\mathbf{u}|^2 + |\mathbf{v}|^2)$$
> 
> **Ejemplo numérico:**
> 
> ```
> u = (3, 0),  v = (0, 4)
> 
> u + v = (3, 4)  →  ‖u+v‖² = 25
> u - v = (3,-4)  →  ‖u-v‖² = 25
> 
> ‖u‖² = 9,  ‖v‖² = 16
> 
> Verificar:
> 25 + 25 = 2(9 + 16)
> 50 = 50 ✅
> ```
> 
> ### Identidad de Polarización (recordatorio)
> 
> $$\langle \mathbf{u}, \mathbf{v} \rangle = \frac{1}{4}(|\mathbf{u}+\mathbf{v}|^2 - |\mathbf{u}-\mathbf{v}|^2)$$
> 
> **En términos de distancia:**
> 
> $$\langle \mathbf{u}, \mathbf{v} \rangle = \frac{1}{4}(|\mathbf{u}+\mathbf{v}|^2 - d(\mathbf{u}, \mathbf{v})^2)$$
> 
> **Interpretación:**
> 
> Podemos recuperar el producto interno conociendo solo las normas (o distancias).

---

## 🎯 Visualización Geométrica

> [!quote]- 🗺️ Interpretación Gráfica
> 
> ### En $\mathbb{R}^2$
> 
> ```mermaid
> graph TD
>     A[Punto u = ·3,2] --> B[Norma ‖u‖]
>     B --> C[Radio desde origen<br/>‖u‖ = √13]
>     
>     D[Punto v = ·1,4] --> E[Norma ‖v‖]
>     E --> F[Radio desde origen<br/>‖v‖ = √17]
>     
>     A --> G[Distancia d·u,v]
>     D --> G
>     G --> H[Línea recta u→v<br/>d·u,v = √8]
>     
>     style C fill:#e1ffe1
>     style F fill:#fff4e1
>     style H fill:#e1f5ff
> ```
> 
> ### Bolas y Esferas
> 
> **Bola abierta:**
> 
> $$B(\mathbf{c}, r) = {\mathbf{v} \in V : d(\mathbf{v}, \mathbf{c}) < r}$$
> 
> Todos los vectores a distancia menor que $r$ del centro $\mathbf{c}$.
> 
> **Esfera:**
> 
> $$S(\mathbf{c}, r) = {\mathbf{v} \in V : d(\mathbf{v}, \mathbf{c}) = r}$$
> 
> Todos los vectores a distancia exactamente $r$ del centro $\mathbf{c}$.
> 
> **Ejemplos:**
> 
> |Espacio|Centro|Radio|Forma|
> |---|---|---|---|
> |$\mathbb{R}^2$|$(0,0)$|$1$|Círculo unitario|
> |$\mathbb{R}^3$|$(0,0,0)$|$1$|Esfera unitaria|
> |$\mathbb{R}^n$|$\mathbf{0}$|$1$|Hiperesfera unitaria|

---

## 🧩 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> ### Nivel Básico
> 
> **1.** Calcula la norma de los siguientes vectores con el producto punto estándar:
> 
> - $\mathbf{v} = (3, 4)$ en $\mathbb{R}^2$
> - $\mathbf{w} = (1, 2, 2)$ en $\mathbb{R}^3$
> - $\mathbf{u} = (1, -1, 1, -1)$ en $\mathbb{R}^4$
> 
> **2.** Calcula la distancia entre:
> 
> - $\mathbf{u} = (1, 2)$ y $\mathbf{v} = (4, 6)$
> - $\mathbf{p} = (0, 0, 0)$ y $\mathbf{q} = (1, 1, 1)$
> 
> **3.** Verifica la homogeneidad de la norma: $|\alpha\mathbf{v}| = |\alpha| \cdot |\mathbf{v}|$ para:
> 
> - $\alpha = 3$, $\mathbf{v} = (1, 2)$
> - $\alpha = -2$, $\mathbf{v} = (3, 4, 5)$
> 
> ### Nivel Intermedio
> 
> **4.** Calcula $|f|$ para las siguientes funciones en $[0,1]$:
> 
> - $f(x) = 2x$
> - $f(x) = x^2$
> - $f(x) = \cos(\pi x)$
> 
> **5.** Verifica la identidad del paralelogramo para:
> 
> - $\mathbf{u} = (1, 0)$, $\mathbf{v} = (0, 1)$
> - $\mathbf{u} = (1, 2, 3)$, $\mathbf{v} = (2, 1, 0)$
> 
> **6.** Encuentra todos los vectores en $\mathbb{R}^2$ que tienen norma $1$ y están a distancia $\sqrt{2}$ de $\mathbf{v} = (1, 0)$.
> 
> ### Nivel Avanzado
> 
> **7.** Demuestra la desigualdad triangular inversa: $$\big| |\mathbf{u}| - |\mathbf{v}| \big| \leq |\mathbf{u} - \mathbf{v}|$$
> 
> **8.** Sea $|\cdot|_w$ la norma inducida por el producto ponderado con pesos $w_1, w_2, \ldots, w_n > 0$. Demuestra que satisface los cuatro axiomas de norma.
> 
> **9.** Calcula la norma de Frobenius de la matriz: $$A = \begin{pmatrix} 1 & 2 & 3 \ 4 & 5 & 6 \ 7 & 8 & 9 \end{pmatrix}$$

---

## 📖 Resumen del Capítulo

> [!abstract]- 📝 Puntos Clave
> 
> ### Conceptos Fundamentales
> 
> |Concepto|Definición|Notación|
> |---|---|---|
> |**Norma inducida**|$\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$|$\|\cdot\|$|
> |**Distancia**|$d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\|$|$d(\cdot, \cdot)$|
> |**Axiomas de norma**|N1-N4|-|
> |**Axiomas de métrica**|M1-M4|-|
> 
> ### Fórmulas Esenciales
> 
> $$\begin{align} \text{Norma euclidiana:} & \quad |\mathbf{v}| = \sqrt{\sum_{i=1}^n v_i^2} \\[8pt] \text{Norma }L^2: & \quad |f| = \sqrt{\int_a^b f(x)^2 , dx} \\[8pt] \text{Distancia euclidiana:} & \quad d(\mathbf{u}, \mathbf{v}) = \sqrt{\sum_{i=1}^n (u_i - v_i)^2} \end{align}$$
> 
> ### Propiedades Importantes
> 
> - Toda norma inducida satisface los cuatro axiomas
> - La distancia hereda propiedades de la norma
> - Identidad del paralelogramo caracteriza normas de producto interno
> - Desigualdad triangular y su versión inversa
> 
> ### Jerarquía de Estructuras
> 
> ```mermaid
> graph TD
>     A[Producto Interno] --> B[Norma]
>     B --> C[Distancia]
>     C --> D[Topología]
>     
>     A -.->|Define| E[Ángulos]
>     B -.->|Define| F[Longitudes]
>     C -.->|Define| G[Cercanía]
>     
>     style A fill:#e1ffe1
>     style B fill:#fff4e1
>     style C fill:#e1f5ff
> ```
> 
> ### Próximo Tema
> 
> En el siguiente capítulo estudiaremos la **ortogonalidad y ortonormalidad**, conceptos fundamentales que dependen crucialmente del producto interno.

---

**Tags:** #algebra-lineal #norma #distancia #metrica #espacio-normado #espacio-metrico #geometria
# 📐 Espacio Vectorial

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva **Un espacio vectorial es una estructura algebraica formada por un conjunto de objetos llamados vectores, junto con dos operaciones (suma de vectores y multiplicación por escalares) que satisfacen ciertas propiedades naturales. Es el marco matemático fundamental para estudiar objetos que pueden sumarse y escalarse, generalizando las nociones geométricas de vectores en el plano y el espacio.**
> 
> **Características clave:**
> 
> - **Vectores:** Elementos del espacio (pueden ser flechas, funciones, matrices, polinomios, etc.)
> - **Escalares:** Números que multiplican vectores (usualmente ℝ o ℂ)
> - **Suma vectorial:** Operación que combina dos vectores
> - **Multiplicación escalar:** Operación que escala un vector
> - **Axiomas:** Conjunto de propiedades que deben satisfacerse
> - **Generalidad:** Incluye geometría, funciones, matrices y más

### 📖 Contexto Histórico

> [!note]- Desarrollo Histórico **Orígenes Geométricos (1600-1800):**
> 
> - **Descartes (1637):** Geometría analítica
>     - Coordenadas para representar puntos
>     - Base para álgebra geométrica
> - **Newton & Leibniz (1670s):** Cálculo diferencial
>     - Tangentes como "vectores velocidad"
> - **Euler (1748):** Análisis vectorial implícito
>     - Componentes de fuerzas
> 
> **Nacimiento del Concepto Vectorial (1800-1850):**
> 
> - **Wessel (1797):** Representación geométrica de números complejos
>     - Puntos en el plano como pares ordenados
> - **Argand (1806):** Diagrama de Argand
>     - Números complejos como vectores
> - **Gauss (1831):** Teoría de números complejos
> - **Hamilton (1843):** Cuaterniones
>     - Primer álgebra no conmutativa
>     - Generalización de números complejos a 4D
>     - Operaciones vectoriales en 3D
> - **Grassmann (1844):** "Ausdehnungslehre" (Teoría de la Extensión)
>     - Primera axiomatización abstracta
>     - Espacios de n dimensiones
>     - Producto exterior
>     - Trabajo adelantado a su época, poco reconocido inicialmente
> 
> **Consolidación del Análisis Vectorial (1850-1900):**
> 
> - **Maxwell (1873):** "Treatise on Electricity and Magnetism"
>     - Usa cuaterniones de Hamilton
>     - Ecuaciones de Maxwell
> - **Gibbs (1881):** Análisis vectorial moderno
>     - Notación de punto y cruz
>     - Separa parte vectorial de cuaterniones
>     - "Vector Analysis" (1901)
> - **Heaviside (1880s):** Análisis operacional
>     - Aplicaciones en ingeniería
> - **Peano (1888):** Axiomatización de espacios vectoriales
>     - Define espacio vectorial abstracto
>     - Lista de axiomas formales
>     - "Calcolo Geometrico"
> 
> **Álgebra Lineal Abstracta (1900-1930):**
> 
> - **Hilbert (1906):** Espacios de Hilbert
>     - Espacios de dimensión infinita
>     - Base para mecánica cuántica
> - **Banach (1920s):** Espacios de Banach
>     - Espacios normados completos
>     - Análisis funcional
> - **Steinitz (1910):** Teoría abstracta de espacios vectoriales
> - **Weyl (1918):** "Raum, Zeit, Materie"
>     - Espacios vectoriales en relatividad
> 
> **Era Moderna (1930-presente):**
> 
> - **Von Neumann (1930s):** Teoría de operadores
>     - Álgebras de operadores en espacios de Hilbert
> - **Bourbaki (1939-presente):** Estructuras matemáticas
>     - Formalización rigurosa y abstracta
>     - "Éléments de mathématique"
> - **Grothendieck (1950s):** Álgebra homológica
>     - Categorías de espacios vectoriales
> - **Computación (1950s-presente):**
>     - Álgebra lineal numérica
>     - Gráficos por computadora
>     - Machine Learning (2010s)
>     - Deep Learning basado en espacios vectoriales

## 📐 Definición Formal

> [!success]- Definición Axiomática **Definición:** Un **espacio vectorial** sobre un campo 𝔽 (usualmente ℝ o ℂ) es un conjunto V junto con dos operaciones:
> 
> ```
> 1. SUMA VECTORIAL: + : V × V → V
>    (u, v) ↦ u + v
> 
> 2. MULTIPLICACIÓN ESCALAR: · : 𝔽 × V → V
>    (c, v) ↦ c·v
> ```
> 
> que satisfacen los siguientes **axiomas** para todo u, v, w ∈ V y todo c, d ∈ 𝔽:
> 
> **AXIOMAS DE LA SUMA:**
> 
> ```
> (A1) CLAUSURA: u + v ∈ V
>      (la suma de vectores está en V)
> 
> (A2) CONMUTATIVA: u + v = v + u
> 
> (A3) ASOCIATIVA: (u + v) + w = u + (v + w)
> 
> (A4) ELEMENTO NEUTRO: Existe 0 ∈ V tal que v + 0 = v para todo v
>      (vector cero o nulo)
> 
> (A5) ELEMENTO OPUESTO: Para cada v ∈ V existe -v ∈ V tal que
>      v + (-v) = 0
>      (vector opuesto o inverso aditivo)
> ```
> 
> **AXIOMAS DE LA MULTIPLICACIÓN ESCALAR:**
> 
> ```
> (M1) CLAUSURA: c·v ∈ V
>      (el múltiplo escalar está en V)
> 
> (M2) DISTRIBUTIVA RESPECTO A SUMA DE VECTORES:
>      c·(u + v) = c·u + c·v
> 
> (M3) DISTRIBUTIVA RESPECTO A SUMA DE ESCALARES:
>      (c + d)·v = c·v + d·v
> 
> (M4) ASOCIATIVA MIXTA: c·(d·v) = (cd)·v
> 
> (M5) ELEMENTO NEUTRO: 1·v = v para todo v
>      (donde 1 es la unidad del campo 𝔽)
> ```
> 
> **Notación:**
> 
> ```
> (V, +, ·) es un espacio vectorial sobre 𝔽
> 
> o simplemente: V es un espacio vectorial
> 
> Elementos de V: vectores
> Elementos de 𝔽: escalares
> ```
> 
> **Terminología:**
> 
> ```
> - Si 𝔽 = ℝ: espacio vectorial REAL
> - Si 𝔽 = ℂ: espacio vectorial COMPLEJO
> - Si 𝔽 = ℚ: espacio vectorial RACIONAL
> - Si 𝔽 = ℤ_p: espacio vectorial sobre campo finito
> ```

## 🎯 Ejemplos Fundamentales

### 1️⃣ Espacios Euclidianos ℝⁿ

> [!example]- El Ejemplo Más Importante **Definición:**
> 
> ```
> ℝⁿ = {(x₁, x₂, ..., xₙ) : xᵢ ∈ ℝ}
> 
> Conjunto de n-tuplas de números reales
> ```
> 
> **Operaciones:**
> 
> ```
> SUMA:
> (x₁, x₂, ..., xₙ) + (y₁, y₂, ..., yₙ) = (x₁+y₁, x₂+y₂, ..., xₙ+yₙ)
> 
> Componente por componente
> 
> MULTIPLICACIÓN ESCALAR:
> c·(x₁, x₂, ..., xₙ) = (cx₁, cx₂, ..., cxₙ)
> 
> Escalar multiplica cada componente
> ```
> 
> **Casos particulares:**
> 
> ```
> ℝ¹ = ℝ: la recta real
>        (números reales como vectores)
> 
> ℝ²: el plano
>     Vectores: (x, y)
>     Interpretación: puntos o flechas en el plano
> 
> ℝ³: el espacio tridimensional
>     Vectores: (x, y, z)
>     Interpretación: puntos o flechas en el espacio
> 
> ℝⁿ: espacio n-dimensional
>     n > 3: "hiperEspacio" (no visualizable geométricamente)
> ```
> 
> **Vector cero y opuestos:**
> 
> ```
> Vector cero: 0 = (0, 0, ..., 0)
> 
> Opuesto de v = (x₁, ..., xₙ):
> -v = (-x₁, ..., -xₙ)
> ```
> 
> **Verificación de axiomas (ejemplo en ℝ²):**
> 
> ```
> u = (u₁, u₂), v = (v₁, v₂), c ∈ ℝ
> 
> (A2) Conmutativa:
> u + v = (u₁+v₁, u₂+v₂) = (v₁+u₁, v₂+u₂) = v + u ✓
> 
> (A3) Asociativa:
> (u + v) + w = ((u₁+v₁)+w₁, (u₂+v₂)+w₂)
>             = (u₁+(v₁+w₁), u₂+(v₂+w₂)) = u + (v + w) ✓
> 
> (M2) Distributiva:
> c(u + v) = c(u₁+v₁, u₂+v₂) = (c(u₁+v₁), c(u₂+v₂))
>          = (cu₁+cv₁, cu₂+cv₂) = cu + cv ✓
> 
> [Similar para los demás axiomas]
> ```

### 2️⃣ Espacio de Matrices M_{m×n}(ℝ)

> [!example]- Matrices como Vectores **Definición:**
> 
> ```
> M_{m×n}(ℝ) = {matrices m×n con entradas reales}
> 
> Conjunto de todas las matrices de orden m×n
> ```
> 
> **Operaciones:**
> 
> ```
> SUMA: Suma de matrices (componente por componente)
> A + B = [aᵢⱼ] + [bᵢⱼ] = [aᵢⱼ + bᵢⱼ]
> 
> MULTIPLICACIÓN ESCALAR:
> c·A = c·[aᵢⱼ] = [c·aᵢⱼ]
> ```
> 
> **Vector cero:**
> 
> ```
> Matriz nula: O = [0]_{m×n}
> 
> Todos los elementos son cero
> ```
> 
> **Dimensión:**
> 
> ```
> dim(M_{m×n}(ℝ)) = m·n
> 
> Isomorfo a ℝ^{mn}
> ```
> 
> **Casos especiales:**
> 
> ```
> M_{n×n}(ℝ): matrices cuadradas de orden n
> dim = n²
> 
> M_{n×1}(ℝ): matrices columna (vectores de ℝⁿ)
> dim = n
> 
> M_{1×n}(ℝ): matrices fila
> dim = n
> ```

### 3️⃣ Espacio de Polinomios P_n(ℝ)

> [!example]- Polinomios como Vectores **Definición:**
> 
> ```
> P_n(ℝ) = {p(x) = a₀ + a₁x + a₂x² + ... + aₙxⁿ : aᵢ ∈ ℝ}
> 
> Polinomios de grado ≤ n con coeficientes reales
> ```
> 
> **Operaciones:**
> 
> ```
> SUMA:
> p(x) + q(x) = (a₀ + b₀) + (a₁ + b₁)x + ... + (aₙ + bₙ)xⁿ
> 
> Sumar coeficientes correspondientes
> 
> MULTIPLICACIÓN ESCALAR:
> c·p(x) = ca₀ + ca₁x + ... + caₙxⁿ
> 
> Multiplicar cada coeficiente por c
> ```
> 
> **Vector cero:**
> 
> ```
> Polinomio cero: 0(x) = 0
> 
> Todos los coeficientes son cero
> ```
> 
> **Dimensión:**
> 
> ```
> dim(P_n(ℝ)) = n + 1
> 
> Base estándar: {1, x, x², x³, ..., xⁿ}
> ```
> 
> **Isomorfismo con ℝⁿ⁺¹:**
> 
> ```
> p(x) = a₀ + a₁x + ... + aₙxⁿ  ↔  (a₀, a₁, ..., aₙ)
> 
> Cada polinomio corresponde a su vector de coeficientes
> ```
> 
> **Espacio de todos los polinomios:**
> 
> ```
> P(ℝ) = ⋃_{n=0}^∞ P_n(ℝ)
> 
> Todos los polinomios (cualquier grado)
> dim(P(ℝ)) = ∞  (dimensión infinita)
> ```

### 4️⃣ Espacio de Funciones C([a,b])

> [!example]- Funciones Continuas **Definición:**
> 
> ```
> C([a,b]) = {f : [a,b] → ℝ : f es continua}
> 
> Funciones continuas en el intervalo [a,b]
> ```
> 
> **Operaciones:**
> 
> ```
> SUMA:
> (f + g)(x) = f(x) + g(x)
> 
> Suma puntual de funciones
> 
> MULTIPLICACIÓN ESCALAR:
> (c·f)(x) = c·f(x)
> 
> Multiplicar valor de la función por c
> ```
> 
> **Vector cero:**
> 
> ```
> Función cero: 0(x) = 0 para todo x ∈ [a,b]
> 
> Función constantemente cero
> ```
> 
> **Dimensión:**
> 
> ```
> dim(C([a,b])) = ∞
> 
> Espacio de dimensión infinita
> (no tiene base finita)
> ```
> 
> **Ejemplos de elementos:**
> 
> ```
> - f(x) = x²
> - g(x) = sin(x)
> - h(x) = e^x
> - k(x) = 1/(1 + x²)
> 
> Todas son funciones continuas, luego vectores en C([a,b])
> ```

### 5️⃣ Espacio de Sucesiones ℓ²

> [!example]- Sucesiones de Cuadrado Sumable **Definición:**
> 
> ```
> ℓ² = {(x₁, x₂, x₃, ...) : xᵢ ∈ ℝ y Σ_{i=1}^∞ xᵢ² < ∞}
> 
> Sucesiones infinitas cuya suma de cuadrados converge
> ```
> 
> **Operaciones:**
> 
> ```
> SUMA:
> (x₁, x₂, ...) + (y₁, y₂, ...) = (x₁+y₁, x₂+y₂, ...)
> 
> MULTIPLICACIÓN ESCALAR:
> c·(x₁, x₂, ...) = (cx₁, cx₂, ...)
> ```
> 
> **Vector cero:**
> 
> ```
> 0 = (0, 0, 0, ...)
> ```
> 
> **Dimensión:**
> 
> ```
> dim(ℓ²) = ∞
> 
> Base: {eᵢ : i ∈ ℕ} donde eᵢ tiene 1 en posición i y 0 en el resto
> e₁ = (1, 0, 0, ...)
> e₂ = (0, 1, 0, ...)
> e₃ = (0, 0, 1, ...)
> ...
> ```
> 
> **Importancia:**
> 
> ```
> - Base de espacios de Hilbert
> - Análisis de Fourier
> - Mecánica cuántica
> - Procesamiento de señales
> ```

### 6️⃣ Otros Ejemplos

> [!example]- Espacios Menos Convencionales **Soluciones de ecuaciones diferenciales:**
> 
> ```
> V = {y : y'' + y = 0}
> 
> Espacio de soluciones de la ecuación diferencial
> 
> Vectores: y = c₁cos(x) + c₂sin(x)
> dim(V) = 2
> Base: {cos(x), sin(x)}
> ```
> 
> **Matrices simétricas:**
> 
> ```
> S_n = {A ∈ M_{n×n}(ℝ) : A^T = A}
> 
> Matrices simétricas de orden n
> dim(S_n) = n(n+1)/2
> ```
> 
> **Polinomios pares:**
> 
> ```
> P_par = {p(x) : p(-x) = p(x)}
> 
> Polinomios de grado par: a₀ + a₂x² + a₄x⁴ + ...
> Subespacio de P(ℝ)
> ```
> 
> **Números complejos:**
> 
> ```
> ℂ es espacio vectorial sobre ℝ
> dim_ℝ(ℂ) = 2
> Base: {1, i}
> 
> z = a + bi ↔ (a, b) ∈ ℝ²
> 
> Pero ℂ también es espacio vectorial sobre ℂ
> dim_ℂ(ℂ) = 1
> ```

## 🔧 Propiedades Derivadas

> [!important]- Consecuencias de los Axiomas **Teorema:** En todo espacio vectorial V:
> 
> **1. Unicidad del vector cero:**
> 
> ```
> Existe un único vector 0 ∈ V tal que v + 0 = v para todo v
> 
> Demostración:
> Supongamos dos vectores cero: 0 y 0'
> Entonces: 0 = 0 + 0' = 0'  (por axioma A4 aplicado a ambos)
> Luego 0 = 0' (unicidad)
> ```
> 
> **2. Unicidad del opuesto:**
> 
> ```
> Para cada v ∈ V, existe un único -v tal que v + (-v) = 0
> 
> Demostración:
> Supongamos dos opuestos: w y w'
> v + w = 0 y v + w' = 0
> Entonces: w = w + 0 = w + (v + w') = (w + v) + w' = 0 + w' = w'
> ```
> 
> **3. Producto por cero:**
> 
> ```
> 0·v = 0  (escalar cero por cualquier vector da vector cero)
> 
> Demostración:
> 0·v = (0 + 0)·v = 0·v + 0·v  (por M3)
> Sumando -(0·v) a ambos lados:
> 0 = 0·v
> ```
> 
> **4. Producto de escalar por vector cero:**
> 
> ```
> c·0 = 0  (cualquier escalar por vector cero da vector cero)
> 
> Demostración:
> c·0 = c·(0 + 0) = c·0 + c·0  (por M2)
> Sumando -(c·0):
> 0 = c·0
> ```
> 
> **5. Producto por -1:**
> 
> ```
> (-1)·v = -v
> 
> El producto por -1 da el opuesto del vector
> 
> Demostración:
> v + (-1)·v = 1·v + (-1)·v = (1 + (-1))·v = 0·v = 0
> Por unicidad del opuesto: (-1)·v = -v
> ```
> 
> **6. Si c·v = 0:**
> 
> ```
> c·v = 0 ⟹ c = 0 o v = 0
> 
> Propiedad del producto nulo
> 
> Demostración (contrarecíproca):
> Si c ≠ 0 y c·v = 0, entonces:
> v = 1·v = (c⁻¹c)·v = c⁻¹·(c·v) = c⁻¹·0 = 0
> ```
> 
> **7. Cancelación:**
> 
> ```
> u + w = v + w ⟹ u = v
> 
> Sumar -w a ambos lados:
> u + w + (-w) = v + w + (-w)
> u + 0 = v + 0
> u = v
> ```

## 🎯 Subespacios Vectoriales

> [!important]- Espacios dentro de Espacios **Definición:** Un subconjunto W ⊆ V es un **subespacio vectorial** de V si:
> 
> ```
> 1. 0 ∈ W  (contiene el vector cero)
> 
> 2. W es cerrado bajo suma:
>    u, v ∈ W ⟹ u + v ∈ W
> 
> 3. W es cerrado bajo multiplicación escalar:
>    v ∈ W, c ∈ 𝔽 ⟹ c·v ∈ W
> ```
> 
> **Equivalentemente:**
> 
> ```
> W es subespacio ⟺ W es cerrado bajo combinaciones lineales
> 
> u, v ∈ W y c, d ∈ 𝔽 ⟹ c·u + d·v ∈ W
> ```
> 
> **Teorema:** Todo subespacio W es en sí mismo un espacio vectorial con las operaciones heredadas de V.
> 
> **Subespacios triviales:**
> 
> ```
> {0}: subespacio trivial (solo el vector cero)
> V: el espacio completo (subespacio impropio)
> 
> Ambos siempre son subespacios de V
> ```

> [!example]- Ejemplos de Subespacios **Ejemplo 1: Rectas por el origen en ℝ²**
> 
> ```
> W = {(x, y) ∈ ℝ² : y = mx}  (recta con pendiente m)
> 
> Equivalentemente: W = {t(1, m) : t ∈ ℝ}
> 
> Verificación:
> 4. (0, 0) ∈ W ✓
> 5. Si (x₁, mx₁), (x₂, mx₂) ∈ W:
>    (x₁, mx₁) + (x₂, mx₂) = (x₁+x₂, m(x₁+x₂)) ∈ W ✓
> 6. c(x, mx) = (cx, cmx) ∈ W ✓
> 
> W es subespacio de ℝ²
> dim(W) = 1
> ```
> 
> **Ejemplo 2: Planos por el origen en ℝ³**
> 
> ```
> W = {(x, y, z) ∈ ℝ³ : ax + by + cz = 0}
> 
> Plano que pasa por el origen con vector normal (a,b,c)
> 
> Es subespacio de ℝ³
> dim(W) = 2
> ```
> 
> **Ejemplo 3: Matrices diagonales**
> 
> ```
> D_n = {matrices diagonales n×n}
> 
> D_n ⊂ M_{n×n}(ℝ)
> 
> Verificación:
> 7. Matriz nula es diagonal ✓
> 8. Suma de diagonales es diagonal ✓
> 9. Múltiplo de diagonal es diagonal ✓
> 
> dim(D_n) = n
> ```
> 
> **Ejemplo 4: Polinomios de grado ≤ 2**
> 
> ```
> P₂(ℝ) = {a₀ + a₁x + a₂x² : aᵢ ∈ ℝ}
> 
> P₂(ℝ) ⊂ P(ℝ)  (subespacio de todos los polinomios)
> 
> dim(P₂(ℝ)) = 3
> Base: {1, x, x²}
> ```
> 
> **Ejemplo 5: Espacio nulo de una matriz**
> 
> ```
> Nul(A) = {x ∈ ℝⁿ : Ax = 0}
> 
> Conjunto de soluciones de sistema homogéneo
> 
> Siempre es subespacio de ℝⁿ:
> 10. A·0 = 0 ✓
> 11. Si Ax₁ = 0 y Ax₂ = 0: A(x₁+x₂) = Ax₁ + Ax₂ = 0 ✓
> 12. Si Ax = 0: A(cx) = c(Ax) = c·0 = 0 ✓
> ```
> 
> **NO ejemplos (no son subespacios):**
> 
> ```
> 13. W = {(x, y) ∈ ℝ² : y = mx + b, b ≠ 0}
>    Recta que NO pasa por el origen
>    (0, 0) ∉ W ✗
> 
> 14. W = {(x, y) ∈ ℝ² : x ≥ 0, y ≥ 0}
>    Primer cuadrante
>    No cerrado bajo múltiplos: (-1)·(1,1) = (-1,-1) ∉ W ✗
> 
> 15. W = {(x, y) ∈ ℝ² : x² + y² = 1}
>    Círculo unitario
>    No cerrado bajo suma: (1,0) + (0,1) = (1,1) ∉ W ✗
> ```

## 🔄 Combinaciones Lineales

> [!important]- Concepto Central **Definición:** Dados vectores v₁, v₂, ..., vₖ ∈ V y escalares c₁, c₂, ..., cₖ ∈ 𝔽, una **combinación lineal** es:
> 
> ```
> c₁v₁ + c₂v₂ + ... + cₖvₖ
> 
> o  Σ_{i=1}^k cᵢvᵢ
> ```
> 
> **Espacio generado (Span):**
> 
> ```
> Span{v₁, v₂, ..., vₖ} = {c₁v₁ + c₂v₂ + ... + cₖvₖ : cᵢ ∈ 𝔽}
> 
> Conjunto de todas las combinaciones lineales de los vectores
> ```
> 
> **Teorema:** Span{v₁, ..., vₖ} es un subespacio de V
> 
> ```
> Es el MENOR subespacio que contiene a v₁, ..., vₖ
> ```
> 
> **Generadores:**
> 
> ```
> Se dice que {v₁, ..., vₖ} GENERA o SPAN V si:
> 
> Span{v₁, ..., vₖ} = V
> 
> Es decir, todo vector de V es combinación lineal de v₁, ..., vₖ
> ```

> [!example]- Ejemplos de Combinaciones Lineales **Ejemplo 1: En ℝ²**
> 
> ```
> v₁ = (1, 0), v₂ = (0, 1)
> 
> Combinación lineal:
> c₁(1,0) + c₂(0,1) = (c₁, c₂)
> 
> Span{v₁, v₂} = ℝ²
> 
> Estos vectores generan todo ℝ²
> ```
> 
> **Ejemplo 2: Recta en ℝ³**
> 
> ```
> v = (1, 2, -1)
> 
> Span{v} = {t(1, 2, -1) : t ∈ ℝ}
> 
> Es una recta que pasa por el origen
> dim(Span{v}) = 1
> ```
> 
> **Ejemplo 3: Plano en ℝ³**
> 
> ```
> v₁ = (1, 0, 0), v₂ = (0, 1, 0)
> Span{v₁, v₂} = {c₁(1,0,0) + c₂(0,1,0) : c₁, c₂ ∈ ℝ} = {(c₁, c₂, 0) : c₁, c₂ ∈ ℝ}
> 
> Es el plano xy (z = 0) dim(Span{v₁, v₂}) = 2
> 
> ```
> 
> **Ejemplo 4: Polinomios**
> ```
> 
> p₁(x) = 1, p₂(x) = x, p₃(x) = x²
> 
> Span{p₁, p₂, p₃} = {a₀ + a₁x + a₂x² : aᵢ ∈ ℝ} = P₂(ℝ)
> 
> Generan todos los polinomios de grado ≤ 2
> 
> ```
> 
> **Ejemplo 5: Matrices**
> ```
> 
> E₁₁ = ⎡1 0⎤, E₁₂ = ⎡0 1⎤, E₂₁ = ⎡0 0⎤, E₂₂ = ⎡0 0⎤ ⎣0 0⎦ ⎣0 0⎦ ⎣1 0⎦ ⎣0 1⎦
> 
> Span{E₁₁, E₁₂, E₂₁, E₂₂} = M₂ₓ₂(ℝ)
> 
> Cualquier matriz 2×2 es combinación lineal de estas
> 
> ⎡a b⎤ = aE₁₁ + bE₁₂ + cE₂₁ + dE₂₂ ⎣c d⎦
> ```

## 📐 Dependencia e Independencia Lineal

> [!important]- Concepto Fundamental **Definición:** Un conjunto de vectores {v₁, v₂, ..., vₖ} es:
> 
> **LINEALMENTE INDEPENDIENTE** si:
> 
> ```
> c₁v₁ + c₂v₂ + ... + cₖvₖ = 0  ⟹  c₁ = c₂ = ... = cₖ = 0
> 
> La única combinación lineal que da cero es la trivial
> (todos los coeficientes cero)
> ```
> 
> **LINEALMENTE DEPENDIENTE** si:
> 
> ```
> Existen c₁, ..., cₖ NO TODOS CEROS tal que:
> c₁v₁ + c₂v₂ + ... + cₖvₖ = 0
> 
> Al menos un coeficiente no es cero
> ```
> 
> **Interpretación:**
> 
> ```
> INDEPENDIENTES: Ningún vector es combinación de los otros
>                Aportan direcciones genuinamente distintas
> 
> DEPENDIENTES: Al menos un vector es combinación de los otros
>              Hay redundancia en el conjunto
> ```
> 
> **Equivalencias (para dependencia):**
> 
> ```
> {v₁, ..., vₖ} es linealmente dependiente ⟺
> 
> 1. Existe vᵢ que es combinación lineal de los demás
> 
> 2. Al menos un vector puede eliminarse sin cambiar el Span
> 
> 3. El sistema homogéneo [v₁ ... vₖ]c = 0 tiene 
>    soluciones no triviales
> ```

> [!example]- Ejemplos de (In)dependencia Lineal **Ejemplo 1: Vectores estándar en ℝ³**
> 
> ```
> e₁ = (1,0,0), e₂ = (0,1,0), e₃ = (0,0,1)
> 
> Verificar independencia:
> c₁(1,0,0) + c₂(0,1,0) + c₃(0,0,1) = (0,0,0)
> (c₁, c₂, c₃) = (0, 0, 0)
> 
> Solo solución: c₁ = c₂ = c₃ = 0
> 
> SON LINEALMENTE INDEPENDIENTES ✓
> ```
> 
> **Ejemplo 2: Vectores en el plano**
> 
> ```
> v₁ = (1, 2), v₂ = (2, 4)
> 
> Verificar:
> c₁(1,2) + c₂(2,4) = (0,0)
> (c₁ + 2c₂, 2c₁ + 4c₂) = (0,0)
> 
> c₁ + 2c₂ = 0
> 2c₁ + 4c₂ = 0  (segunda es múltiplo de primera)
> 
> Infinitas soluciones: c₁ = -2c₂, c₂ libre
> Por ejemplo: c₁ = 2, c₂ = -1
> 
> 2(1,2) - 1(2,4) = (0,0)
> 
> SON LINEALMENTE DEPENDIENTES ✗
> 
> Nota: v₂ = 2v₁ (uno es múltiplo del otro)
> ```
> 
> **Ejemplo 3: Tres vectores en ℝ²**
> 
> ```
> v₁ = (1,0), v₂ = (0,1), v₃ = (1,1)
> 
> Como hay 3 vectores en espacio de dimensión 2:
> DEBEN ser linealmente dependientes
> 
> Verificación:
> v₃ = v₁ + v₂
> 1·v₁ + 1·v₂ - 1·v₃ = 0
> 
> Coeficientes no todos ceros → dependientes
> ```
> 
> **Ejemplo 4: Polinomios**
> 
> ```
> p₁(x) = 1, p₂(x) = x, p₃(x) = x²
> 
> ¿Son independientes?
> c₁·1 + c₂·x + c₃·x² = 0  (polinomio cero)
> 
> Para que un polinomio sea idénticamente cero,
> todos sus coeficientes deben ser cero:
> c₁ = c₂ = c₃ = 0
> 
> SON LINEALMENTE INDEPENDIENTES ✓
> ```
> 
> **Ejemplo 5: Funciones**
> 
> ```
> f₁(x) = sin(x), f₂(x) = cos(x)
> 
> ¿Son independientes en C([0, 2π])?
> 
> c₁sin(x) + c₂cos(x) = 0  para todo x ∈ [0, 2π]
> 
> Evaluar en x = 0: c₂ = 0
> Evaluar en x = π/2: c₁ = 0
> 
> SON LINEALMENTE INDEPENDIENTES ✓
> ```
> 
> **Ejemplo 6: Matrices**
> 
> ```
> A₁ = ⎡1 0⎤,  A₂ = ⎡0 1⎤,  A₃ = ⎡1 1⎤
>      ⎣0 1⎦       ⎣1 0⎦       ⎣1 1⎦
> 
> c₁A₁ + c₂A₂ + c₃A₃ = O
> 
> ⎡c₁+c₃  c₂+c₃⎤ = ⎡0 0⎤
> ⎣c₂+c₃  c₁+c₃⎦   ⎣0 0⎦
> 
> Sistema:
> c₁ + c₃ = 0
> c₂ + c₃ = 0
> c₂ + c₃ = 0  (repetida)
> c₁ + c₃ = 0  (repetida)
> 
> Soluciones: c₁ = -c₃, c₂ = -c₃, c₃ libre
> Ejemplo: c₁ = 1, c₂ = 1, c₃ = -1
> 
> A₁ + A₂ - A₃ = O
> 
> SON LINEALMENTE DEPENDIENTES ✗
> ```

## 🎯 Base y Dimensión

> [!important]- Conceptos Centrales **Definición de BASE:**
> 
> ```
> Un conjunto B = {v₁, v₂, ..., vₙ} es una BASE de V si:
> 
> 1. B es LINEALMENTE INDEPENDIENTE
> 2. B GENERA V (Span(B) = V)
> ```
> 
> **Propiedades de una base:**
> 
> ```
> - Todo vector v ∈ V se expresa ÚNICAMENTE como
>   combinación lineal de vectores de la base
> 
> - Es un conjunto "mínimo" que genera V
>   (quitar un vector → ya no genera V)
> 
> - Es un conjunto "máximo" independiente
>   (agregar un vector → se vuelve dependiente)
> ```
> 
> **Definición de DIMENSIÓN:**
> 
> ```
> La DIMENSIÓN de V, denotada dim(V), es el número
> de vectores en una base de V
> 
> Si V tiene base finita: dim(V) = n
> Si V no tiene base finita: dim(V) = ∞
> ```
> 
> **Teorema fundamental:**
> 
> ```
> Todas las bases de un espacio vectorial V
> tienen el MISMO número de elementos
> 
> Por eso la dimensión está bien definida
> ```
> 
> **Convención:**
> 
> ```
> dim({0}) = 0  (espacio trivial)
> 
> El único vector es 0, que no puede estar en ninguna base
> (pues {0} es linealmente dependiente)
> ```

> [!example]- Bases Estándar y Dimensiones **Base estándar de ℝⁿ:**
> 
> ```
> B = {e₁, e₂, ..., eₙ}
> 
> e₁ = (1, 0, 0, ..., 0)
> e₂ = (0, 1, 0, ..., 0)
> e₃ = (0, 0, 1, ..., 0)
> ...
> eₙ = (0, 0, 0, ..., 1)
> 
> dim(ℝⁿ) = n
> ```
> 
> **Base estándar de Pₙ(ℝ):**
> 
> ```
> B = {1, x, x², x³, ..., xⁿ}
> 
> dim(Pₙ(ℝ)) = n + 1
> ```
> 
> **Base estándar de M_{m×n}(ℝ):**
> 
> ```
> B = {Eᵢⱼ : 1 ≤ i ≤ m, 1 ≤ j ≤ n}
> 
> donde Eᵢⱼ tiene 1 en posición (i,j) y 0 en el resto
> 
> dim(M_{m×n}(ℝ)) = m·n
> ```
> 
> **Ejemplos de dimensiones:**
> 
> ```
> ℝ¹ = ℝ:          dim = 1
> ℝ²:              dim = 2
> ℝ³:              dim = 3
> ℝⁿ:              dim = n
> 
> P₂(ℝ):           dim = 3
> P₁₀(ℝ):          dim = 11
> Pₙ(ℝ):           dim = n + 1
> P(ℝ):            dim = ∞
> 
> M₂ₓ₂(ℝ):         dim = 4
> M₃ₓ₃(ℝ):         dim = 9
> M_{m×n}(ℝ):      dim = mn
> 
> C([a,b]):        dim = ∞
> ℓ²:              dim = ∞
> ```

> [!example]- Encontrar Bases y Dimensiones **Ejemplo 1: Subespacio de ℝ³**
> 
> ```
> W = {(x, y, z) ∈ ℝ³ : x + 2y - z = 0}
> 
> Parametrizar:
> z = x + 2y
> (x, y, z) = (x, y, x+2y) = x(1,0,1) + y(0,1,2)
> 
> W = Span{(1,0,1), (0,1,2)}
> 
> Verificar independencia:
> c₁(1,0,1) + c₂(0,1,2) = (0,0,0)
> c₁ = 0, c₂ = 0  (única solución)
> 
> Base: B = {(1,0,1), (0,1,2)}
> dim(W) = 2
> ```
> 
> **Ejemplo 2: Espacio nulo**
> 
> ```
> A = ⎡1  2  -1   0⎤
>     ⎣2  4   0   2⎦
> 
> Nul(A) = {x ∈ ℝ⁴ : Ax = 0}
> 
> Resolver sistema homogéneo:
> x₁ + 2x₂ - x₃ = 0
> 2x₁ + 4x₂ + 2x₄ = 0
> 
> Forma escalonada → variables libres: x₂, x₃
> 
> Solución general:
> x₁ = -2x₂ + x₃
> x₂ = x₂  (libre)
> x₃ = x₃  (libre)
> x₄ = 2x₂ - x₃
> 
> x = x₂(-2, 1, 0, 2) + x₃(1, 0, 1, -1)
> 
> Base: B = {(-2,1,0,2), (1,0,1,-1)}
> dim(Nul(A)) = 2
> ```
> 
> **Ejemplo 3: Matrices simétricas 2×2**
> 
> ```
> S₂ = {⎡a b⎤ : matriz simétrica}
>      ⎣b c⎦
> 
> Parametrización:
> ⎡a b⎤ = a⎡1 0⎤ + b⎡0 1⎤ + c⎡0 0⎤
> ⎣b c⎦     ⎣0 0⎦     ⎣1 0⎦     ⎣0 1⎦
> 
> Base: B = {⎡1 0⎤, ⎡0 1⎤, ⎡0 0⎤}
>           ⎣0 0⎦  ⎣1 0⎦  ⎣0 1⎦
> 
> dim(S₂) = 3
> ```

## 🔄 Teoremas Fundamentales

> [!important]- Resultados Clave **Teorema 1: Caracterización de bases**
> 
> ```
> Si V tiene dimensión n, entonces:
> 
> Un conjunto B = {v₁, ..., vₙ} es base de V ⟺
> 
> 1. B tiene n vectores Y es linealmente independiente
> 
> O
> 
> 2. B tiene n vectores Y genera V
> 
> (Basta verificar UNA de las dos condiciones)
> ```
> 
> **Teorema 2: Más de n vectores**
> 
> ```
> Si dim(V) = n, entonces:
> 
> Cualquier conjunto con más de n vectores
> es LINEALMENTE DEPENDIENTE
> 
> No puede haber conjuntos independientes con > n elementos
> ```
> 
> **Teorema 3: Menos de n vectores**
> 
> ```
> Si dim(V) = n, entonces:
> 
> Cualquier conjunto con menos de n vectores
> NO PUEDE GENERAR V
> 
> Se necesitan al menos n vectores para generar V
> ```
> 
> **Teorema 4: Extensión a base**
> 
> ```
> Todo conjunto linealmente independiente
> puede EXTENDERSE a una base
> 
> Si {v₁, ..., vₖ} es independiente en V con dim(V) = n,
> entonces existen vₖ₊₁, ..., vₙ tales que
> {v₁, ..., vₖ, vₖ₊₁, ..., vₙ} es base de V
> ```
> 
> **Teorema 5: Reducción a base**
> 
> ```
> Todo conjunto generador contiene una base
> 
> Si {v₁, ..., vₖ} genera V, entonces algún subconjunto
> de estos vectores forma una base de V
> ```
> 
> **Teorema 6: Dimensión de subespacios**
> 
> ```
> Si W es subespacio de V, entonces:
> 
> dim(W) ≤ dim(V)
> 
> Además: dim(W) = dim(V) ⟺ W = V
> ```

## 🎨 Coordenadas respecto a una Base

> [!important]- Representación Única **Teorema de coordenadas:**
> 
> ```
> Si B = {v₁, v₂, ..., vₙ} es base de V, entonces
> todo vector v ∈ V se expresa ÚNICAMENTE como:
> 
> v = c₁v₁ + c₂v₂ + ... + cₙvₙ
> 
> Los escalares c₁, c₂, ..., cₙ se llaman
> COORDENADAS de v respecto a la base B
> ```
> 
> **Notación:**
> 
> ```
> [v]_B = ⎡c₁⎤
>         ⎢c₂⎥
>         ⎢⋮ ⎥
>         ⎣cₙ⎦
> 
> Vector de coordenadas de v en la base B
> ```
> 
> **Isomorfismo de coordenadas:**
> 
> ```
> La función φ: V → ℝⁿ definida por φ(v) = [v]_B
> es un isomorfismo de espacios vectoriales
> 
> Todo espacio de dimensión n es "esencialmente" ℝⁿ
> ```

> [!example]- Ejemplos de Coordenadas **Ejemplo 1: Base estándar de ℝ³**
> 
> ```
> B = {(1,0,0), (0,1,0), (0,0,1)}
> 
> v = (2, -3, 5)
> 
> v = 2(1,0,0) - 3(0,1,0) + 5(0,0,1)
> 
> [v]_B = ⎡ 2⎤
>         ⎢-3⎥
>         ⎣ 5⎦
> 
> (Las coordenadas son las mismas componentes)
> ```
> 
> **Ejemplo 2: Base no estándar**
> 
> ```
> B = {(1,1), (1,-1)} base de ℝ²
> 
> v = (3, 1)
> 
> Encontrar c₁, c₂ tal que:
> c₁(1,1) + c₂(1,-1) = (3,1)
> 
> Sistema:
> c₁ + c₂ = 3
> c₁ - c₂ = 1
> 
> Solución: c₁ = 2, c₂ = 1
> 
> [v]_B = ⎡2⎤
>         ⎣1⎦
> 
> Verificación: 2(1,1) + 1(1,-1) = (2,2) + (1,-1) = (3,1) ✓
> ```
> 
> **Ejemplo 3: Polinomios**
> 
> ```
> B = {1, x, x²} base de P₂(ℝ)
> 
> p(x) = 3 - 2x + 5x²
> 
> [p]_B = ⎡ 3⎤
>         ⎢-2⎥
>         ⎣ 5⎦
> 
> Las coordenadas son los coeficientes
> ```

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "Todos los conjuntos son espacios vectoriales"**
> 
> ```
> ✗ INCORRECTO
> 
> ℕ = {0, 1, 2, 3, ...} NO es espacio vectorial sobre ℝ
> No cerrado bajo multiplicación escalar: 0.5 · 1 = 0.5 ∉ ℕ
> 
> ℤ = {..., -2, -1, 0, 1, 2, ...} NO es espacio vectorial sobre ℝ
> No cerrado bajo multiplicación escalar: 0.5 · 2 = 1 ∉ ℤ
> 
> ✓ Debe satisfacer todos los axiomas
> ```
> 
> **2. "Independencia = vectores distintos"**
> 
> ```
> ✗ INCORRECTO
> 
> v₁ = (1, 2), v₂ = (2, 4)  son distintos pero DEPENDIENTES
> (v₂ = 2v₁)
> 
> ✓ Independencia significa que ninguno es combinación
>   lineal de los otros
> ```
> 
> **3. "Más vectores = mejor base"**
> 
> ```
> ✗ INCORRECTO
> 
> En ℝ², no puede haber base con 3 vectores
> Cualquier conjunto de 3 vectores en ℝ² es dependiente
> 
> ✓ Una base tiene exactamente dim(V) vectores
> ```
> 
> **4. "El vector cero puede estar en una base"**
> 
> ```
> ✗ INCORRECTO
> 
> Cualquier conjunto que contenga 0 es DEPENDIENTE
> Pues: 1·0 = 0 (coeficiente no nulo)
> 
> ✓ Bases son conjuntos independientes
>   Nunca incluyen el vector cero
> ```
> 
> **5. "Subespacio = subconjunto"**
> 
> ```
> ✗ No todo subconjunto es subespacio
> 
> {(x,y) : x > 0, y > 0} ⊂ ℝ²  NO es subespacio
> No contiene 0, no cerrado bajo múltiplos negativos
> 
> ✓ Subespacio debe ser cerrado bajo operaciones
>   y contener el vector cero
> ```
> 
> **6. "dim(U + W) = dim(U) + dim(W)"**
> 
> ```
> ✗ INCORRECTO en general
> 
> U = Span{(1,0)}, W = Span{(0,1)} en ℝ²
> dim(U) = 1, dim(W) = 1
> U + W = ℝ², dim(U + W) = 2 ≠ 1 + 1
> 
> ✓ CORRECTO: dim(U + W) = dim(U) + dim(W) - dim(U ∩ W)
> ```
> 
> **7. "Confundir coordenadas"**
> 
> ```
> v = (3, 5) en base estándar de ℝ²
> 
> ✗ [v]_B = (3, 5) para cualquier base B
> 
> ✓ Las coordenadas DEPENDEN de la base elegida
>   Solo coinciden con componentes en base estándar
> ```

## 📊 Suma e Intersección de Subespacios

> [!note]- Operaciones con Subespacios **Suma de subespacios:**
> 
> ```
> U + W = {u + w : u ∈ U, w ∈ W}
> 
> Conjunto de todas las sumas de vectores de U y W
> ```
> 
> **Intersección:**
> 
> ```
> U ∩ W = {v : v ∈ U Y v ∈ W}
> 
> Vectores que están en ambos subespacios
> ```
> 
> **Teorema:**
> 
> ```
> Si U y W son subespacios de V, entonces:
> - U ∩ W es subespacio de V
> - U + W es subespacio de V
> ```
> 
> **Fórmula de dimensión:**
> 
> ```
> dim(U + W) = dim(U) + dim(W) - dim(U ∩ W)
> 
> (Análoga a |A ∪ B| = |A| + |B| - |A ∩ B| en teoría de conjuntos)
> ```
> 
> **Suma directa:**
> 
> ```
> U ⊕ W  (se lee "U suma directa W")
> 
> Cuando U ∩ W = {0}
> 
> En este caso: dim(U ⊕ W) = dim(U) + dim(W)
> ```

## 🎯 Ejercicios Propuestos

> [!example]- Problemas de Práctica **Nivel básico:**
> 
> 1. Verificar que son espacios vectoriales: a) ℝ³ con operaciones usuales b) P₃(ℝ) con suma y múltiplo escalar usuales c) M₂ₓ₃(ℝ) con operaciones matriciales
>     
> 2. Determinar si son subespacios de ℝ³: a) W = {(x, y, z) : x + y + z = 0} b) W = {(x, y, z) : x = 2y} c) W = {(x, y, z) : xyz = 0} d) W = {(x, y, z) : x² + y² = z²}
>     
> 3. Determinar si son l.i. o l.d.: a) {(1,0), (0,1)} en ℝ² b) {(1,2), (2,4)} en ℝ² c) {(1,0,0), (0,1,0), (1,1,0)} en ℝ³
>     
> 
> **Nivel intermedio:** 4. Encontrar base y dimensión: a) W = {(x, y, z) ∈ ℝ³ : 2x - y + 3z = 0} b) U = {A ∈ M₂ₓ₂(ℝ) : A es simétrica} c) P_par = {p ∈ P(ℝ) : p(-x) = p(x)}
> 
> 4. Expresar v como combinación lineal de B: a) v = (5, 7), B = {(1,2), (2,3)} en ℝ² b) v = (1, 0, 3), B = {(1,1,1), (1,1,0), (1,0,0)} en ℝ³
>     
> 5. Extender a base de ℝ³: {(1, 0, 1), (0, 1, 1)}
>     
> 
> **Nivel avanzado:** 7. Demostrar que si {v₁, v₂, v₃} es l.i., entonces {v₁ + v₂, v₂ + v₃, v₃ + v₁} es l.i.
> 
> 6. Si dim(V) = n y W es subespacio con dim(W) = n-1, demostrar que existe v ∈ V \ W tal que V = W ⊕ Span{v}
>     
> 7. Demostrar la fórmula de dimensión: dim(U + W) = dim(U) + dim(W) - dim(U ∩ W)
>     
> 8. Encontrar todas las bases de ℝ² que contengan (1,1)
>     

## 💡 Aplicaciones de Espacios Vectoriales

> [!example]- Contextos Reales **Física:**
> 
> ```
> - Estados cuánticos: vectores en espacio de Hilbert
> - Fuerzas y velocidades: vectores en ℝ³
> - Campos eléctricos/magnéticos: campos vectoriales
> - Relatividad: espacio-tiempo de Minkowski
> ```
> 
> **Ingeniería:**
> 
> ```
> - Señales: funciones en L²[0,T]
> - Sistemas de control: espacios de estado
> - Procesamiento de imágenes: matrices como vectores
> - Redes neuronales: vectores de pesos
> ```
> 
> **Computación:**
> 
> ```
> - Gráficos 3D: transformaciones lineales en ℝ³
> - Machine Learning: vectores de características
> - Compresión: proyección en subespacios
> - Criptografía: espacios sobre campos finitos
> ```
> 
> **Economía:**
> 
> ```
> - Modelos input-output: vectores de producción
> - Optimización: espacios de estrategias
> - Series temporales: vectores de datos
> ```
> 
> **Matemáticas:**
> 
> ```
> - Ecuaciones diferenciales: soluciones forman espacio
> - Análisis funcional: funciones como vectores
> - Topología: espacios topológicos vectoriales
> - Geometría: variedades diferenciables
> ```

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[02.1 Conjuntos]] - Definición de conjunto
> - [[02.3 Funciones]] - Operaciones como funciones
> - [[03.1 Conjuntos Numéricos]] - Campo de escalares ℝ, ℂ
> - [[06.1 Matrices]] - M_{m×n} como espacio vectorial
> - [[06.2 Operaciones con Matrices]] - Suma y multiplicación
> 
> **Temas relacionados:**
> 
> - [[Álgebra Lineal]] - Teoría completa
> - [[Transformaciones Lineales]] - Funciones entre espacios
> - [[Producto Interno]] - Estructura adicional
> - [[Normas]] - Medida de longitud
> - [[Ortogonalidad]] - Perpendicularidad generalizada
> 
> **Aplicaciones posteriores:**
> 
> - [[Eigenvalores y Eigenvectores]] - Diagonalización
> - [[Espacios con Producto Interno]] - Geometría
> - [[Análisis Funcional]] - Dimensión infinita
> - [[Ecuaciones Diferenciales]] - Espacio de soluciones
> - [[Optimización]] - Espacios de restricciones

## 📚 Recursos Adicionales

> [!tip]- Herramientas y Referencias **Software:**
> 
> - [MATLAB/Octave](https://octave.org/) - Cálculos con vectores
> - [Python NumPy](https://numpy.org/) - Álgebra lineal
> - [Wolfram Alpha](https://www.wolframalpha.com/) - "is {(1,2), (3,4)} linearly independent"
> - [GeoGebra](https://www.geogebra.org/) - Visualización 2D/3D
> 
> **Calculadoras online:**
> 
> - Verificadores de independencia lineal
> - Calculadoras de bases
> - Verificadores de subespacios
> 
> **Videos educativos:**
> 
> - 3Blue1Brown - "Essence of Linear Algebra"
> - MIT OpenCourseWare - Gilbert Strang
> - Khan Academy - Linear Algebra
> - Professor Leonard - Vector Spaces
> 
> **Tutoriales interactivos:**
> 
> - [Immersive Linear Algebra](http://immersivemath.com/)
> - [Linear Algebra Done Right (Axler)](http://linear.axler.net/)

## 📖 Bibliografía Esencial

> [!note]- Lecturas Recomendadas **Introductorios:**
> 
> - Lay, D. C. (2015). _Linear Algebra and Its Applications_ (5th ed.)
>     - Cap. 4: Espacios vectoriales
>     - Enfoque geométrico e intuitivo
> - Anton, H. & Rorres, C. (2013). _Elementary Linear Algebra_ (11th ed.)
>     - Cap. 4-5: Espacios vectoriales generales
> - Poole, D. (2014). _Linear Algebra: A Modern Introduction_ (4th ed.)
>     - Aplicaciones contemporáneas
> 
> **Nivel intermedio:**
> 
> - Strang, G. (2016). _Introduction to Linear Algebra_ (5th ed.)
>     - Cap. 3: Espacios vectoriales y subespacios
>     - Video lectures disponibles (MIT OCW)
> - Friedberg, S., Insel, A. & Spence, L. (2018). _Linear Algebra_ (5th ed.)
>     - Tratamiento riguroso y abstracto
> 
> **Avanzado:**
> 
> - Axler, S. (2015). _Linear Algebra Done Right_ (3rd ed.)
>     - Énfasis en espacios vectoriales abstractos
>     - Sin determinantes hasta el final
> - Hoffman, K. & Kunze, R. (1971). _Linear Algebra_ (2nd ed.)
>     - Clásico matemático riguroso
> - Roman, S. (2007). _Advanced Linear Algebra_ (3rd ed.)
>     - Temas avanzados y generalizaciones
> 
> **Análisis Funcional:**
> 
> - Kreyszig, E. (1989). _Introductory Functional Analysis_
>     - Espacios de dimensión infinita
> - Rudin, W. (1991). _Functional Analysis_ (2nd ed.)
>     - Tratamiento profundo
> 
> **Aplicaciones:**
> 
> - Strang, G. (2019). _Linear Algebra and Learning from Data_
>     - Machine Learning y Data Science
> - Meyer, C. D. (2000). _Matrix Analysis and Applied Linear Algebra_
>     - Énfasis computacional

## 🎓 Resumen Ejecutivo

> [!important]- Conceptos Clave para Recordar **Definición de espacio vectorial:**
> 
> ```
> Conjunto V con:
> - Suma de vectores: +
> - Multiplicación por escalar: ·
> 
> Satisfaciendo 10 axiomas:
> 5 para suma (conmutativa, asociativa, neutro, opuesto, clausura)
> 5 para multiplicación (distributivas, asociativa, neutro, clausura)
> ```
> 
> **Ejemplos principales:**
> 
> ```
> ℝⁿ: n-tuplas de reales (dim = n)
> M_{m×n}(ℝ): matrices m×n (dim = mn)
> Pₙ(ℝ): polinomios grado ≤ n (dim = n+1)
> C([a,b]): funciones continuas (dim = ∞)
> ```
> 
> **Subespacio:**
> 
> ```
> W ⊆ V es subespacio si:
> 1. 0 ∈ W
> 2. Cerrado bajo suma
> 3. Cerrado bajo múltiplos escalares
> 
> Equivalente: cerrado bajo combinaciones lineales
> ```
> 
> **Independencia lineal:**
> 
> ```
> {v₁, ..., vₖ} es l.i. si:
> c₁v₁ + ... + cₖvₖ = 0 ⟹ c₁ = ... = cₖ = 0
> 
> Ningún vector es combinación de los otros
> ```
> 
> **Base:**
> 
> ```
> Conjunto que es:
> - Linealmente independiente
> - Genera todo el espacio
> 
> Todo vector se expresa ÚNICAMENTE como
> combinación lineal de vectores de la base
> ```
> 
> **Dimensión:**
> 
> ```
> dim(V) = número de vectores en cualquier base
> 
> Todas las bases tienen el mismo número de elementos
> 
> Medida del "tamaño" del espacio
> ```
> 
> **Teoremas clave:**
> 
> ```
> - n vectores en ℝⁿ son base ⟺ son l.i.
> - Más de n vectores en espacio dim n → dependientes
> - Menos de n vectores → no generan
> - dim(U + W) = dim(U) + dim(W) - dim(U ∩ W)
> ```

## 🧩 Problemas Resueltos Detallados

> [!example]- Soluciones Paso a Paso **Problema 1: Verificar que es espacio vectorial**
> 
> ```
> V = {(x, 2x) : x ∈ ℝ} con operaciones usuales de ℝ²
> 
> SOLUCIÓN:
> 
> Verificar axiomas:
> 
> (A1) Clausura suma:
> u = (x₁, 2x₁), v = (x₂, 2x₂)
> u + v = (x₁ + x₂, 2x₁ + 2x₂) = (x₁ + x₂, 2(x₁ + x₂)) ∈ V ✓
> 
> (A2) Conmutativa:
> Heredada de ℝ² ✓
> 
> (A3) Asociativa:
> Heredada de ℝ² ✓
> 
> (A4) Vector cero:
> 0 = (0, 0) ∈ V (pues 0 = 2·0) ✓
> 
> (A5) Opuestos:
> -(x, 2x) = (-x, -2x) = (-x, 2(-x)) ∈ V ✓
> 
> (M1) Clausura multiplicación:
> c(x, 2x) = (cx, 2cx) = (cx, 2(cx)) ∈ V ✓
> 
> (M2)-(M5): Heredadas de ℝ² ✓
> 
> RESPUESTA: V es espacio vectorial
> 
> Nota: V es subespacio de ℝ², isomorfo a ℝ
> dim(V) = 1, base: {(1, 2)}
> ```
> 
> **Problema 2: Determinar si es subespacio**
> 
> ```
> W = {(x, y, z) ∈ ℝ³ : x - 2y + 3z = 0}
> 
> SOLUCIÓN:
> 
> Método 1: Verificar las tres condiciones
> 
> 1. ¿0 ∈ W?
>    (0,0,0): 0 - 2(0) + 3(0) = 0 ✓
> 
> 2. ¿Cerrado bajo suma?
>    u = (x₁, y₁, z₁), v = (x₂, y₂, z₂) ∈ W
>    Entonces: x₁ - 2y₁ + 3z₁ = 0 y x₂ - 2y₂ + 3z₂ = 0
>    
>    u + v = (x₁+x₂, y₁+y₂, z₁+z₂)
>    (x₁+x₂) - 2(y₁+y₂) + 3(z₁+z₂)
>    = (x₁ - 2y₁ + 3z₁) + (x₂ - 2y₂ + 3z₂)
>    = 0 + 0 = 0 ✓
>    
>    u + v ∈ W ✓
> 
> 3. ¿Cerrado bajo múltiplos?
>    v = (x, y, z) ∈ W, c ∈ ℝ
>    x - 2y + 3z = 0
>    
>    cv = (cx, cy, cz)
>    cx - 2(cy) + 3(cz) = c(x - 2y + 3z) = c·0 = 0 ✓
>    
>    cv ∈ W ✓
> 
> RESPUESTA: W es subespacio de ℝ³
> 
> Es un plano que pasa por el origen
> dim(W) = 2
> ```
> 
> **Problema 3: Independencia lineal**
> 
> ```
> ¿Son l.i. los vectores v₁ = (1, 2, 1), v₂ = (2, 1, 0), v₃ = (1, -1, -1)?
> 
> SOLUCIÓN:
> 
> Plantear: c₁v₁ + c₂v₂ + c₃v₃ = 0
> 
> c₁(1,2,1) + c₂(2,1,0) + c₃(1,-1,-1) = (0,0,0)
> 
> Sistema de ecuaciones:
> c₁ + 2c₂ + c₃ = 0    ... (1)
> 2c₁ + c₂ - c₃ = 0    ... (2)
> c₁ - c₃ = 0          ... (3)
> 
> De (3): c₃ = c₁
> 
> Sustituir en (1):
> c₁ + 2c₂ + c₁ = 0
> 2c₁ + 2c₂ = 0
> c₁ + c₂ = 0
> c₂ = -c₁                ... (4)
> 
> Sustituir (3) y (4) en (2):
> 2c₁ + (-c₁) - c₁ = 0
> 0 = 0 ✓
> 
> Sistema tiene infinitas soluciones:
> c₁ libre, c₂ = -c₁, c₃ = c₁
> 
> Ejemplo con c₁ = 1:
> 1·v₁ - 1·v₂ + 1·v₃ = (1,2,1) - (2,1,0) + (1,-1,-1)
>                    = (0,0,0) ✓
> 
> RESPUESTA: Son LINEALMENTE DEPENDIENTES
> 
> Relación: v₁ - v₂ + v₃ = 0
> o: v₃ = v₂ - v₁
> ```
> 
> **Problema 4: Encontrar base y dimensión**
> 
> ```
> W = {p(x) ∈ P₃(ℝ) : p(0) = 0 y p(1) = 0}
> 
> SOLUCIÓN:
> 
> Paso 1: Caracterizar W
> p(x) = a₀ + a₁x + a₂x² + a₃x³
> 
> p(0) = a₀ = 0
> p(1) = a₀ + a₁ + a₂ + a₃ = 0
> 
> Como a₀ = 0:
> a₁ + a₂ + a₃ = 0
> a₁ = -a₂ - a₃
> 
> Paso 2: Parametrizar
> p(x) = 0 + (-a₂ - a₃)x + a₂x² + a₃x³
>      = a₂(-x + x²) + a₃(-x + x³)
>      = a₂·p₁(x) + a₃·p₂(x)
> 
> donde:
> p₁(x) = -x + x² = x² - x
> p₂(x) = -x + x³ = x³ - x
> 
> Paso 3: Verificar independencia
> c₁p₁(x) + c₂p₂(x) = 0
> c₁(x² - x) + c₂(x³ - x) = 0
> -c₁x - c₂x + c₁x² + c₂x³ = 0
> c₂x³ + c₁x² - (c₁ + c₂)x = 0
> 
> Coeficientes iguales a cero:
> c₂ = 0  (coef. de x³)
> c₁ = 0  (coef. de x²)
> 
> Son l.i. ✓
> 
> Paso 4: Verificar que generan W
> Todo p ∈ W se escribió como c₁p₁ + c₂p₂ ✓
> 
> RESPUESTA:
> Base: B = {x² - x, x³ - x}
> dim(W) = 2
> 
> Interpretación: Polinomios cúbicos que se anulan en 0 y 1
> ```
> 
> **Problema 5: Coordenadas en base no estándar**
> 
> ```
> B = {v₁ = (1,1,0), v₂ = (1,0,1), v₃ = (0,1,1)} base de ℝ³
> 
> Encontrar [v]_B donde v = (2, 3, 4)
> 
> SOLUCIÓN:
> 
> Necesitamos c₁, c₂, c₃ tales que:
> c₁v₁ + c₂v₂ + c₃v₃ = v
> 
> c₁(1,1,0) + c₂(1,0,1) + c₃(0,1,1) = (2,3,4)
> 
> Sistema:
> c₁ + c₂ = 2           ... (1)
> c₁ + c₃ = 3           ... (2)
> c₂ + c₃ = 4           ... (3)
> 
> De (1): c₂ = 2 - c₁
> De (2): c₃ = 3 - c₁
> 
> Sustituir en (3):
> (2 - c₁) + (3 - c₁) = 4
> 5 - 2c₁ = 4
> c₁ = 1/2
> 
> Entonces:
> c₂ = 2 - 1/2 = 3/2
> c₃ = 3 - 1/2 = 5/2
> 
> Verificación:
> (1/2)(1,1,0) + (3/2)(1,0,1) + (5/2)(0,1,1)
> = (1/2, 1/2, 0) + (3/2, 0, 3/2) + (0, 5/2, 5/2)
> = (2, 3, 4) ✓
> 
> RESPUESTA:
> [v]_B = ⎡1/2⎤
>         ⎢3/2⎥
>         ⎣5/2⎦
> 
> O en fracciones: [v]_B = (1/2)⎡1⎤ = 1/2⎡1⎤
>                              ⎢3⎥      ⎢3⎥
>                              ⎣5⎦      ⎣5⎦
> ```

## 🌐 Extensiones y Generalizaciones

> [!note]- Conceptos Relacionados **Espacios normados:**
> 
> ```
> Espacio vectorial V con norma ||·||
> 
> ||v|| mide "longitud" o "tamaño" de v
> 
> Propiedades:
> 1. ||v|| ≥ 0, ||v|| = 0 ⟺ v = 0
> 2. ||cv|| = |c|·||v||
> 3. ||u + v|| ≤ ||u|| + ||v||  (desigualdad triangular)
> ```
> 
> **Espacios con producto interno:**
> 
> ```
> Espacio vectorial con producto ⟨·,·⟩
> 
> ⟨u, v⟩ generaliza producto punto
> 
> Induce norma: ||v|| = √⟨v,v⟩
> ```
> 
> **Espacios de Banach:**
> 
> ```
> Espacio normado completo
> (toda sucesión de Cauchy converge)
> 
> Ejemplos: ℝⁿ, C([a,b]), ℓᵖ
> ```
> 
> **Espacios de Hilbert:**
> 
> ```
> Espacio con producto interno completo
> 
> Generalización de ℝⁿ con producto punto
> Base de mecánica cuántica
> 
> Ejemplo: L²([a,b]), ℓ²
> ```
> 
> **Módulos:**
> 
> ```
> Generalización de espacios vectoriales
> donde escalares vienen de un anillo (no campo)
> 
> Ejemplo: ℤ-módulos = grupos abelianos
> ```
> 
> **Álgebras:**
> 
> ```
> Espacio vectorial con multiplicación adicional
> 
> Ejemplos:
> - ℂ como álgebra sobre ℝ
> - Matrices M_n(ℝ)
> - Álgebras de Lie
> ```

## 🎯 Resumen Visual

> [!important]- Mapa Conceptual
> 
> ```
> ESPACIO VECTORIAL V
> │
> ├── OPERACIONES
> │   ├── Suma: u + v
> │   └── Múltiplo escalar: c·v
> │
> ├── AXIOMAS (10)
> │   ├── Suma (5): conmutativa, asociativa, neutro, opuesto, clausura
> │   └── Multiplicación (5): distributivas, asociativa, neutro, clausura
> │
> ├── SUBESPACIOS W ⊆ V
> │   ├── Contiene 0
> │   ├── Cerrado bajo suma
> │   └── Cerrado bajo múltiplos
> │
> ├── COMBINACIONES LINEALES
> │   ├── c₁v₁ + c₂v₂ + ... + cₖvₖ
> │   └── Span{v₁, ..., vₖ}
> │
> ├── INDEPENDENCIA LINEAL
> │   ├── L.I.: solo combinación trivial da 0
> │   └── L.D.: existe combinación no trivial que da 0
> │
> ├── BASE
> │   ├── Linealmente independiente
> │   ├── Genera todo V
> │   └── Representación única
> │
> └── DIMENSIÓN
>     ├── dim(V) = |base|
>     ├── Todas las bases tienen mismo tamaño
>     └── Medida del "tamaño" del espacio
> ```

---

**Tags:** #espacio-vectorial #álgebra-lineal #vectores #base #dimensión #independencia-lineal #subespacio #combinación-lineal #axiomas #coordenadas #generadores
 
# 📐 Vectores en Espacios Vectoriales

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva **Un espacio vectorial es una estructura algebraica que generaliza las propiedades fundamentales de los vectores geométricos (flechas en el espacio). Consiste en un conjunto de objetos llamados vectores, junto con operaciones de suma y multiplicación por escalares que satisfacen ciertas propiedades axiomáticas. Esta abstracción permite aplicar conceptos geométricos a contextos muy diversos: funciones, matrices, polinomios, soluciones de ecuaciones diferenciales, y más.**
> 
> **Características clave:**
> 
> - **Abstracción:** Generaliza vectores geométricos
> - **Operaciones:** Suma de vectores y multiplicación por escalares
> - **Axiomas:** 10 propiedades fundamentales
> - **Universalidad:** Aplica a múltiples contextos matemáticos
> - **Estructura:** Base algebraica para análisis lineal

### 📖 Contexto Histórico

> [!note]- Desarrollo Histórico **Precursores (1600-1800):**
> 
> - **Descartes (1637):** Coordenadas cartesianas
>     - Base para representación algebraica
>     - Geometría analítica
> - **Leibniz (1679):** Análisis situs
>     - Primeras ideas de álgebra geométrica
> - **Wessel, Argand (1797-1806):** Números complejos
>     - Representación geométrica
>     - Operaciones vectoriales implícitas
> 
> **Nacimiento de vectores (1800-1850):**
> 
> - **Bolzano (1804):** Primeras ideas abstractas
>     - Independencia lineal (implícita)
> - **Möbius (1827):** Coordenadas baricéntricas
>     - Combinaciones lineales
> - **Grassmann (1844):** _Ausdehnungslehre_
>     - Teoría de extensión
>     - Álgebra de vectores abstractos
>     - Producto exterior
>     - Poco reconocido en su época
> - **Hamilton (1843):** Cuaterniones
>     - Extensión de números complejos
>     - Operaciones vectoriales en ℝ³
>     - Producto cruz
> - **Cauchy (1840s):** Análisis matricial
>     - Sistemas lineales
>     - Determinantes
> 
> **Consolidación (1850-1900):**
> 
> - **Cayley (1858):** Teoría de matrices
>     - Álgebra matricial formal
>     - _Memoir on the Theory of Matrices_
> - **Gibbs, Heaviside (1880s):** Análisis vectorial moderno
>     - Notación actual (i, j, k)
>     - Producto punto y cruz
>     - Aplicaciones en física
> - **Peano (1888):** Axiomas de espacios vectoriales
>     - Definición formal abstracta
>     - 10 axiomas fundamentales
>     - _Calcolo geometrico_
> 
> **Era moderna (1900-presente):**
> 
> - **Hilbert (1900s):** Espacios de dimensión infinita
>     - Espacios de Hilbert
>     - Análisis funcional
>     - Mecánica cuántica
> - **Banach (1920s):** Espacios normados
>     - Análisis funcional
>     - Topología lineal
> - **Von Neumann (1930s):** Axiomatización
>     - Espacios vectoriales en mecánica cuántica
>     - Álgebras de operadores
> - **Bourbaki (1940s-1960s):** Estructuras algebraicas
>     - Sistematización moderna
>     - Álgebra lineal abstracta
> - **Computación moderna (1950-presente):**
>     - Algoritmos numéricos
>     - Computación científica
>     - Machine learning (espacios de características)
>     - Gráficos por computadora

## 📊 Definición Formal de Espacio Vectorial

> [!important]- Axiomas Fundamentales **Definición:**
> 
> ```
> Un espacio vectorial V sobre un campo F es un conjunto
> no vacío junto con dos operaciones:
> 
> 1. Suma de vectores: + : V × V → V
>    (u⃗, v⃗) ↦ u⃗ + v⃗
> 
> 2. Multiplicación por escalar: · : F × V → V
>    (α, v⃗) ↦ αv⃗
> 
> que satisfacen los siguientes 10 axiomas:
> 
> AXIOMAS DE LA SUMA:
> 
> (A1) Cerradura: ∀u⃗, v⃗ ∈ V, u⃗ + v⃗ ∈ V
> 
> (A2) Asociatividad: ∀u⃗, v⃗, w⃗ ∈ V,
>      (u⃗ + v⃗) + w⃗ = u⃗ + (v⃗ + w⃗)
> 
> (A3) Elemento neutro: ∃0⃗ ∈ V tal que ∀v⃗ ∈ V,
>      v⃗ + 0⃗ = 0⃗ + v⃗ = v⃗
> 
> (A4) Elemento inverso: ∀v⃗ ∈ V, ∃(-v⃗) ∈ V tal que
>      v⃗ + (-v⃗) = (-v⃗) + v⃗ = 0⃗
> 
> (A5) Conmutatividad: ∀u⃗, v⃗ ∈ V,
>      u⃗ + v⃗ = v⃗ + u⃗
> 
> AXIOMAS DE LA MULTIPLICACIÓN POR ESCALAR:
> 
> (M1) Cerradura: ∀α ∈ F, ∀v⃗ ∈ V, αv⃗ ∈ V
> 
> (M2) Distributividad respecto a suma vectorial:
>      ∀α ∈ F, ∀u⃗, v⃗ ∈ V,
>      α(u⃗ + v⃗) = αu⃗ + αv⃗
> 
> (M3) Distributividad respecto a suma de escalares:
>      ∀α, β ∈ F, ∀v⃗ ∈ V,
>      (α + β)v⃗ = αv⃗ + βv⃗
> 
> (M4) Asociatividad mixta: ∀α, β ∈ F, ∀v⃗ ∈ V,
>      α(βv⃗) = (αβ)v⃗
> 
> (M5) Elemento neutro: ∀v⃗ ∈ V,
>      1·v⃗ = v⃗
>      (donde 1 es la identidad del campo F)
> ```
> 
> **Notación:**
> 
> ```
> • V: espacio vectorial
> • F: campo de escalares (usualmente ℝ o ℂ)
> • v⃗, u⃗, w⃗: vectores (elementos de V)
> • α, β, γ: escalares (elementos de F)
> • 0⃗: vector cero (elemento neutro de V)
> • 0: escalar cero (elemento del campo)
> 
> Convenciones:
> • Vectores: negrita v o flecha v⃗
> • Escalares: letra normal α, β
> • Conjunto: mayúscula V, W
> ```

## 🎯 Propiedades Derivadas

> [!success]- Consecuencias de los Axiomas **Propiedades fundamentales:**
> 
> ```
> De los 10 axiomas se derivan muchas propiedades:
> 
> P1) Unicidad del vector cero:
>     El vector neutro 0⃗ es único
>     
>     Demostración:
>     Supongamos dos neutros: 0⃗ y 0⃗'
>     Por (A3): 0⃗' = 0⃗ + 0⃗' = 0⃗
> 
> P2) Unicidad del inverso:
>     Para cada v⃗, su inverso -v⃗ es único
>     
>     Demostración:
>     Si v⃗ + u⃗ = 0⃗ y v⃗ + w⃗ = 0⃗
>     u⃗ = u⃗ + 0⃗ = u⃗ + (v⃗ + w⃗) = (u⃗ + v⃗) + w⃗ = 0⃗ + w⃗ = w⃗
> 
> P3) Producto por cero escalar:
>     0·v⃗ = 0⃗ para todo v⃗ ∈ V
>     
>     Demostración:
>     0·v⃗ = (0 + 0)·v⃗ = 0·v⃗ + 0·v⃗
>     Por cancelación: 0⃗ = 0·v⃗
> 
> P4) Producto de escalar por vector cero:
>     α·0⃗ = 0⃗ para todo α ∈ F
>     
>     Demostración:
>     α·0⃗ = α·(0⃗ + 0⃗) = α·0⃗ + α·0⃗
>     Por cancelación: 0⃗ = α·0⃗
> 
> P5) Producto por -1:
>     (-1)·v⃗ = -v⃗
>     
>     Demostración:
>     v⃗ + (-1)·v⃗ = 1·v⃗ + (-1)·v⃗ = (1 + (-1))·v⃗ = 0·v⃗ = 0⃗
>     Por definición de inverso: (-1)·v⃗ = -v⃗
> 
> P6) Si αv⃗ = 0⃗, entonces α = 0 o v⃗ = 0⃗
>     
>     Demostración:
>     Si α ≠ 0, entonces existe α⁻¹
>     v⃗ = 1·v⃗ = (α⁻¹α)·v⃗ = α⁻¹(αv⃗) = α⁻¹·0⃗ = 0⃗
> 
> P7) Cancelación:
>     Si u⃗ + v⃗ = u⃗ + w⃗, entonces v⃗ = w⃗
>     
>     Demostración:
>     -u⃗ + (u⃗ + v⃗) = -u⃗ + (u⃗ + w⃗)
>     (-u⃗ + u⃗) + v⃗ = (-u⃗ + u⃗) + w⃗
>     0⃗ + v⃗ = 0⃗ + w⃗
>     v⃗ = w⃗
> 
> P8) Opuesto de una suma:
>     -(u⃗ + v⃗) = -u⃗ + (-v⃗)
>     
>     Demostración por verificación
> 
> P9) Opuesto del opuesto:
>     -(-v⃗) = v⃗
>     
>     Por unicidad del inverso
> 
> P10) Resta definida como:
>      u⃗ - v⃗ := u⃗ + (-v⃗)
> ```

## 📐 Ejemplos de Espacios Vectoriales

> [!note]- Casos Fundamentales **1. Espacio euclidiano ℝⁿ:**
> 
> ```
> Conjunto: ℝⁿ = {(x₁, x₂, ..., xₙ) : xᵢ ∈ ℝ}
> Campo: ℝ (números reales)
> 
> Suma: (x₁, ..., xₙ) + (y₁, ..., yₙ) = (x₁+y₁, ..., xₙ+yₙ)
> Producto: α(x₁, ..., xₙ) = (αx₁, ..., αxₙ)
> 
> Vector cero: 0⃗ = (0, 0, ..., 0)
> Inverso: -(x₁, ..., xₙ) = (-x₁, ..., -xₙ)
> 
> Casos especiales:
> • ℝ¹ = ℝ: recta real
> • ℝ²: plano
> • ℝ³: espacio tridimensional
> • ℝⁿ: espacio n-dimensional
> 
> Dimensión: n (finita)
> 
> Verificación de axiomas: directa (componente a componente)
> ```
> 
> **2. Espacio complejo ℂⁿ:**
> 
> ```
> Conjunto: ℂⁿ = {(z₁, z₂, ..., zₙ) : zᵢ ∈ ℂ}
> Campo: ℂ (números complejos)
> 
> Operaciones: análogas a ℝⁿ
> 
> Aplicaciones:
> • Mecánica cuántica
> • Procesamiento de señales
> • Análisis de Fourier
> 
> Dimensión: n (como espacio vectorial sobre ℂ)
>           2n (como espacio vectorial sobre ℝ)
> ```
> 
> **3. Espacio de matrices Mₘₓₙ(F):**
> 
> ```
> Conjunto: Matrices m×n con entradas en campo F
> 
> Suma: [A]ᵢⱼ + [B]ᵢⱼ = [Aᵢⱼ + Bᵢⱼ]
> Producto: α[A]ᵢⱼ = [αAᵢⱼ]
> 
> Vector cero: Matriz cero (todas entradas 0)
> 
> Dimensión: mn
> 
> Casos especiales:
> • M₂ₓ₂(ℝ): matrices 2×2 reales (dim = 4)
> • Mₙₓₙ(ℝ): matrices cuadradas n×n (dim = n²)
> • Mₙₓ₁(ℝ) ≅ ℝⁿ: matrices columna
> ```
> 
> **4. Espacio de polinomios Pₙ(F):**
> 
> ```
> Conjunto: Polinomios de grado ≤ n con coeficientes en F
> 
> Pₙ(F) = {a₀ + a₁x + a₂x² + ... + aₙxⁿ : aᵢ ∈ F}
> 
> Suma: (a₀ + a₁x + ...) + (b₀ + b₁x + ...) 
>     = (a₀+b₀) + (a₁+b₁)x + ...
> 
> Producto: α(a₀ + a₁x + ...) = (αa₀) + (αa₁)x + ...
> 
> Vector cero: Polinomio cero: 0 (todos coeficientes 0)
> 
> Dimensión: n + 1
> 
> Base estándar: {1, x, x², ..., xⁿ}
> 
> Casos:
> • P₀(ℝ): constantes (dim = 1)
> • P₁(ℝ): lineales ax + b (dim = 2)
> • P₂(ℝ): cuadráticas (dim = 3)
> • P(ℝ): todos los polinomios (dim = ∞)
> ```
> 
> **5. Espacio de funciones continuas C[a,b]:**
> 
> ```
> Conjunto: Funciones continuas f: [a,b] → ℝ
> 
> Suma: (f + g)(x) = f(x) + g(x)
> Producto: (αf)(x) = αf(x)
> 
> Vector cero: Función cero: f(x) = 0 ∀x ∈ [a,b]
> Inverso: (-f)(x) = -f(x)
> 
> Dimensión: infinita
> 
> Subespacios importantes:
> • C^∞[a,b]: funciones infinitamente diferenciables
> • C^k[a,b]: funciones k veces diferenciables
> 
> Aplicaciones:
> • Análisis funcional
> • Ecuaciones diferenciales
> • Series de Fourier
> ```
> 
> **6. Espacio de sucesiones ℓ²:**
> 
> ```
> Conjunto: Sucesiones de cuadrado sumable
> 
> ℓ² = {(x₁, x₂, x₃, ...) : Σ|xₙ|² < ∞}
> 
> Operaciones componente a componente
> 
> Vector cero: (0, 0, 0, ...)
> 
> Dimensión: infinita
> 
> Espacio de Hilbert fundamental en análisis
> ```
> 
> **7. Espacio de soluciones de EDO:**
> 
> ```
> Conjunto: Soluciones de ecuación diferencial lineal homogénea
> 
> Ejemplo: y'' + y = 0
> Soluciones: {A cos(x) + B sen(x) : A, B ∈ ℝ}
> 
> Forma espacio vectorial de dimensión 2
> Base: {cos(x), sen(x)}
> 
> Generalización:
> Soluciones de EDO lineal homogénea de orden n
> forman espacio vectorial de dimensión n
> ```

## 🔍 Subespacios Vectoriales

> [!important]- Espacios Dentro de Espacios **Definición:**
> 
> ```
> Un subespacio W de un espacio vectorial V es un
> subconjunto W ⊆ V que es en sí mismo un espacio
> vectorial con las mismas operaciones.
> 
> CRITERIO DE SUBESPACIO (Teorema):
> W es subespacio de V si y solo si:
> 
> (S1) W ≠ ∅ (no vacío)
>      Equivalente: 0⃗ ∈ W
> 
> (S2) Cerradura bajo suma:
>      ∀u⃗, v⃗ ∈ W, u⃗ + v⃗ ∈ W
> 
> (S3) Cerradura bajo multiplicación por escalar:
>      ∀α ∈ F, ∀v⃗ ∈ W, αv⃗ ∈ W
> 
> Forma compacta:
> W es subespacio ⟺ ∀α, β ∈ F, ∀u⃗, v⃗ ∈ W,
>                    αu⃗ + βv⃗ ∈ W
> 
> Nota: No es necesario verificar los 10 axiomas,
> solo estas 3 condiciones (heredan las demás de V)
> ```
> 
> **Ejemplos en ℝ³:**
> 
> ```
> 1. {0⃗}: subespacio trivial (dimensión 0)
> 
> 2. Rectas por el origen:
>    W = {t(a, b, c) : t ∈ ℝ}, (a,b,c) ≠ (0,0,0)
>    Dimensión: 1
>    
>    Ejemplo: W = {(t, 2t, -t) : t ∈ ℝ}
>    Generado por v⃗ = (1, 2, -1)
> 
> 3. Planos por el origen:
>    W = {s(a₁,b₁,c₁) + t(a₂,b₂,c₂) : s,t ∈ ℝ}
>    donde v⃗₁ y v⃗₂ no son paralelos
>    Dimensión: 2
>    
>    Ejemplo: plano xy
>    W = {(x, y, 0) : x, y ∈ ℝ}
> 
> 4. Todo ℝ³ (dimensión 3)
> 
> Contraejemplos (NO son subespacios):
> • Recta que no pasa por origen: (1,1,1) + t(1,0,0)
>   (no contiene 0⃗)
> • Plano que no pasa por origen: x + y + z = 1
>   (no contiene 0⃗)
> • Primer octante: {(x,y,z) : x,y,z ≥ 0}
>   (no cerrado bajo multiplicación: -1·(1,1,1) ∉ W)
> ```
> 
> **Ejemplos en otros espacios:**
> 
> ```
> En Mₙₓₙ(ℝ):
> • Matrices simétricas: Aᵀ = A
> • Matrices antisimétricas: Aᵀ = -A
> • Matrices triangulares superiores
> • Matrices diagonales
> • Matrices de traza cero: tr(A) = 0
> 
> En Pₙ(ℝ):
> • Polinomios de grado ≤ k (k < n)
> • Polinomios pares: p(-x) = p(x)
> • Polinomios impares: p(-x) = -p(x)
> • Polinomios con p(a) = 0 (raíz fija)
> 
> En C[a,b]:
> • Funciones que se anulan en un punto
> • Funciones pares
> • Funciones impares
> • Soluciones de EDO lineal homogénea
> ```
> 
> **Operaciones con subespacios:**
> 
> ```
> Sean U, W subespacios de V
> 
> 1. Intersección:
>    U ∩ W = {v⃗ ∈ V : v⃗ ∈ U y v⃗ ∈ W}
>    
>    Teorema: U ∩ W es subespacio
>    
>    Ejemplo en ℝ³:
>    U = plano xy: {(x,y,0)}
>    W = plano xz: {(x,0,z)}
>    U ∩ W = eje x: {(x,0,0)} (subespacio)
> 
> 2. Suma:
>    U + W = {u⃗ + w⃗ : u⃗ ∈ U, w⃗ ∈ W}
>    
>    Teorema: U + W es subespacio
>    
>    Es el subespacio más pequeño que contiene U y W
> 
> 3. Unión:
>    U ∪ W generalmente NO es subespacio
>    
>    Contraejemplo en ℝ²:
>    U = eje x, W = eje y
>    (1,0) ∈ U ⊂ U∪W
>    (0,1) ∈ W ⊂ U∪W
>    Pero (1,0) + (0,1) = (1,1) ∉ U∪W
> ```

## 🧮 Combinaciones Lineales

> [!tip]- Construcción de Vectores **Definición:**
> 
> ```
> Sean v⃗₁, v⃗₂, ..., v⃗ₖ vectores en V y α₁, α₂, ..., αₖ escalares
> 
> Una combinación lineal es:
> 
> w⃗ = α₁v⃗₁ + α₂v⃗₂ + ... + αₖv⃗ₖ = Σᵢ₌₁ᵏ αᵢv⃗ᵢ
> 
> Notación:
> • Coeficientes: α₁, α₂, ..., αₖ ∈ F
> • Vectores: v⃗₁, v⃗₂, ..., v⃗ₖ ∈ V
> • Resultado: w⃗ ∈ V (por cerradura)
> 
> Interpretación geométrica en ℝ²:
> w⃗ = α₁v⃗₁ + α₂v⃗₂
> "Caminar α₁ pasos en dirección v⃗₁,
>  luego α₂ pasos en dirección v⃗₂"
> ```
> 
> **Conjunto generado (span):**
> 
> ```
> El conjunto generado por v⃗₁, ..., v⃗ₖ es:
> 
> span{v⃗₁, ..., v⃗ₖ} = gen{v⃗₁, ..., v⃗ₖ}
>                     = {α₁v⃗₁ + ... + αₖv⃗ₖ : αᵢ ∈ F}
> 
> Todas las combinaciones lineales posibles
> 
> TEOREMA: span{v⃗₁, ..., v⃗ₖ} es un subespacio de V
> 
> Es el subespacio más pequeño que contiene
> a v⃗₁, ..., v⃗ₖ
> 
> Demostración de que es subespacio:
> (S1) 0⃗ = 0v⃗₁ + ... + 0v⃗ₖ ∈ span{...} ✓
> 
> (S2) Sean w⃗₁ = Σαᵢv⃗ᵢ, w⃗₂ = Σβᵢv⃗ᵢ
>      w⃗₁ + w⃗₂ = Σ(αᵢ + βᵢ)v⃗ᵢ ∈ span{...} ✓
> 
> (S3) γw⃗₁ = Σ(γαᵢ)v⃗ᵢ ∈ span{...} ✓
> ```
> 
> **Ejemplos:**
> 
> ```
> En ℝ³:
> 
> 1. span{(1,0,0)} = eje x
>    = {(t,0,0) : t ∈ ℝ}
>    Recta por origen (dimensión 1)
> 
> 2. span{(1,0,0), (0,1,0)} = plano xy
>    = {(s,t,0) : s,t ∈ ℝ}
>    Plano por origen (dimensión 2)
> 
> 3. span{(1,0,0), (0,1,0), (0,0,1)} = ℝ³
>    Todo el espacio (dimensión 3)
> 
> 4. span{(1,2,3), (2,4,6)} = recta
>    Segundo vector es múltiplo del primero
>    No agregan dimensión (colineales)
> 
> En P₂(ℝ):
> 
> span{1, x, x²} = P₂(ℝ)
> Todos los polinomios de grado ≤ 2
> 
> span{1, x} = P₁(ℝ) ⊂ P₂(ℝ)
> Polinomios lineales
> ```
> 
> **Sistema generador:**
> 
> ```
> Decimos que {v⃗₁, ..., v⃗ₖ} genera V si:
> 
> span{v⃗₁, ..., v⃗ₖ} = V
> 
> Es decir, todo vector de V es combinación lineal
> de v⃗₁, ..., v⃗ₖ
> 
> Equivalente: ∀v⃗ ∈ V, ∃α₁, ..., αₖ ∈ F :
>              v⃗ = α₁v⃗₁ + ... + αₖv⃗ₖ
> 
> Ejemplo:
> {(1,0,0), (0,1,0), (0,0,1)} genera ℝ³
> 
> Cualquier (x,y,z) = x(1,0,0) + y(0,1,0) + z(0,0,1)
> ```

## 🎯 Independencia Lineal

> [!success]- Vectores Esenciales **Definición:**
> 
> ```
> Los vectores v⃗₁, v⃗₂, ..., v⃗ₖ son linealmente independientes (LI)
> si la única combinación lineal que produce 0⃗ es la trivial:
> 
> α₁v⃗₁ + α₂v⃗₂ + ... + αₖv⃗ₖ = 0⃗
> ⟹ α₁ = α₂ = ... = αₖ = 0
> 
> Son linealmente dependientes (LD) si:
> ∃α₁, ..., αₖ ∈ F (no todos cero) tales que
> α₁v⃗₁ + ... + αₖv⃗ₖ = 0⃗
> Interpretación: • LI: Ningún vector es combinación de los otros "Cada vector aporta nueva dirección" • LD: Al menos un vector es combinación de los otros "Hay redundancia"
> 
> ```
> 
> **Caracterizaciones equivalentes:**
> ```
> 
> Para vectores v⃗₁, ..., v⃗ₖ, las siguientes son equivalentes:
> 
> 1. Son linealmente dependientes (LD)
>     
> 2. Al menos uno es combinación lineal de los otros ∃i : v⃗ᵢ ∈ span{v⃗₁, ..., v⃗ᵢ₋₁, v⃗ᵢ₊₁, ..., v⃗ₖ}
>     
> 3. Se puede eliminar al menos uno sin cambiar el span span{v⃗₁, ..., v⃗ₖ} = span{v⃗₁, ..., v⃗ᵢ₋₁, v⃗ᵢ₊₁, ..., v⃗ₖ} para algún i
>     
> 4. La ecuación α₁v⃗₁ + ... + αₖv⃗ₖ = 0⃗ tiene solución no trivial
>     
> 
> Negando: Son LI ⟺ ninguna de las anteriores
> 
> ```
> 
> **Ejemplos en ℝ³:**
> ```
> 
> Linealmente independientes:
> 
> 1. {(1,0,0), (0,1,0), (0,0,1)} Vectores canónicos (base estándar)
>     
>     α(1,0,0) + β(0,1,0) + γ(0,0,1) = (0,0,0) (α, β, γ) = (0,0,0) ⟹ α = β = γ = 0 ✓
>     
> 2. {(1,2,3), (0,1,2), (0,0,1)} Forma triangular
>     
> 3. {(1,0,0), (1,1,0), (1,1,1)} No ortogonales pero LI
>     
> 
> Linealmente dependientes:
> 
> 4. {(1,2,3), (2,4,6)} Segundo = 2 × primero 2(1,2,3) - 1(2,4,6) = 0⃗
>     
> 5. {(1,0,0), (0,1,0), (1,1,0)} Tercero = primero + segundo 1(1,0,0) + 1(0,1,0) - 1(1,1,0) = 0⃗
>     
> 6. Cualquier conjunto de 4 o más vectores en ℝ³ (exceden la dimensión)
>     
> 
> ```
> 
> **Criterios prácticos:**
> ```
> 
> En ℝⁿ con vectores columna:
> 
> v⃗₁, ..., v⃗ₖ son LI ⟺ det([v⃗₁ | ... | v⃗ₖ]) ≠ 0 (si k = n, matriz cuadrada)
> 
> O equivalentemente: rank([v⃗₁ | ... | v⃗ₖ]) = k
> 
> Proceso de verificación:
> 
> 7. Formar matriz con vectores como columnas
> 8. Reducir a forma escalonada
> 9. Contar pivotes
> 10. Si # pivotes = # vectores ⟹ LI
> 
> Ejemplo: v⃗₁ = (1,2,3), v⃗₂ = (0,1,2), v⃗₃ = (0,0,1)
> 
> [1 0 0] [2 1 0] ya escalonada, 3 pivotes ⟹ LI [3 2 1]
> 
> ```
> 
> **Propiedades:**
> ```
> 
> P1) Conjunto con vector cero es siempre LD α·0⃗ = 0⃗ con α ≠ 0
> 
> P2) Conjunto con vector repetido es LD 1·v⃗ - 1·v⃗ = 0⃗
> 
> P3) Subconjunto de conjunto LI es LI (eliminar vectores preserva independencia)
> 
> P4) Superconjunto de conjunto LD es LD (agregar vectores preserva dependencia)
> 
> P5) Si {v⃗₁, ..., v⃗ₖ} es LI y {v⃗₁, ..., v⃗ₖ, v⃗} es LD, entonces v⃗ ∈ span{v⃗₁, ..., v⃗ₖ}
> 
> P6) En espacio de dimensión n: • Más de n vectores son siempre LD • n vectores LI generan todo el espacio
> ```

## 📏 Base y Dimensión

> [!important]- Estructura Fundamental **Definición de base:**
> 
> ```
> Un conjunto B = {v⃗₁, v⃗₂, ..., v⃗ₙ} es una base de V si:
> 
> (B1) Los vectores son linealmente independientes
> (B2) Los vectores generan V: span(B) = V
> 
> Equivalentemente:
> Todo vector v⃗ ∈ V se escribe de manera ÚNICA como
> combinación lineal de los vectores de la base
> 
> v⃗ = α₁v⃗₁ + α₂v⃗₂ + ... + αₙv⃗ₙ
> 
> Los escalares α₁, ..., αₙ se llaman coordenadas
> de v⃗ respecto a la base B
> 
> Notación: [v⃗]_B = (α₁, α₂, ..., αₙ)ᵀ
> ```
> 
> **Bases estándar:**
> 
> ```
> En ℝⁿ:
> e⃗₁ = (1,0,0,...,0)
> e⃗₂ = (0,1,0,...,0)
> ⋮
> e⃗ₙ = (0,0,0,...,1)
> 
> Base canónica: {e⃗₁, e⃗₂, ..., e⃗ₙ}
> 
> Ejemplo en ℝ³:
> {(1,0,0), (0,1,0), (0,0,1)}
> 
> Cualquier (x,y,z) = x(1,0,0) + y(0,1,0) + z(0,0,1)
> Coordenadas = coeficientes
> 
> En Pₙ(F):
> Base estándar: {1, x, x², ..., xⁿ}
> 
> Ejemplo: p(x) = 3 + 2x - 5x²
> Coordenadas: [p]_B = (3, 2, -5)ᵀ en P₂
> 
> En Mₘₓₙ(F):
> Base estándar: matrices Eᵢⱼ con 1 en posición (i,j)
> y 0 en las demás
> 
> Ejemplo en M₂ₓ₂:
> E₁₁ = [1 0]  E₁₂ = [0 1]
>       [0 0]        [0 0]
> 
> E₂₁ = [0 0]  E₂₂ = [0 0]
>       [1 0]        [0 1]
> 
> Base: {E₁₁, E₁₂, E₂₁, E₂₂}
> ```
> 
> **Dimensión:**
> 
> ```
> TEOREMA FUNDAMENTAL:
> Si V tiene una base finita, entonces todas las bases
> de V tienen el mismo número de elementos.
> 
> Este número se llama dimensión de V:
> dim(V) = número de vectores en cualquier base
> 
> Ejemplos:
> • dim(ℝⁿ) = n
> • dim(ℂⁿ) = n (sobre ℂ), 2n (sobre ℝ)
> • dim(Pₙ(F)) = n + 1
> • dim(Mₘₓₙ(F)) = mn
> • dim({0⃗}) = 0 (espacio trivial)
> 
> Espacios de dimensión infinita:
> • P(F): todos los polinomios
> • C[a,b]: funciones continuas
> • ℓ²: sucesiones de cuadrado sumable
> • Espacios de Hilbert
> ```
> 
> **Teoremas sobre dimensión:**
> 
> ```
> T1) Si dim(V) = n y S = {v⃗₁, ..., v⃗ₖ} ⊂ V:
>     
>     a) Si k > n, entonces S es LD
>     b) Si k < n, entonces S no genera V
>     c) Si k = n y S es LI, entonces S es base
>     d) Si k = n y S genera V, entonces S es base
> 
> T2) Si W es subespacio de V con dim(V) = n:
>     
>     dim(W) ≤ dim(V)
>     
>     Igualdad ⟺ W = V
> 
> T3) Teorema de la dimensión para suma:
>     
>     dim(U + W) = dim(U) + dim(W) - dim(U ∩ W)
>     
>     Análogo a |A∪B| = |A| + |B| - |A∩B|
> 
> T4) Si {v⃗₁, ..., v⃗ₖ} es LI en V con dim(V) = n
>     y k < n, se puede extender a una base
>     agregando n-k vectores
>     
>     Teorema de extensión de base
> 
> T5) Si {v⃗₁, ..., v⃗ₖ} genera V con dim(V) = n
>     y k > n, se puede reducir a una base
>     eliminando k-n vectores
>     
>     Teorema de reducción
> ```
> 
> **Cambio de base:**
> 
> ```
> Sean B = {v⃗₁, ..., v⃗ₙ} y B' = {w⃗₁, ..., w⃗ₙ} bases de V
> 
> Coordenadas de v⃗:
> [v⃗]_B respecto a B
> [v⃗]_B' respecto a B'
> 
> Matriz de cambio de base: P = [w⃗₁|...|w⃗ₙ]_B
> (columnas son coordenadas de w⃗ᵢ en base B)
> 
> Relación:
> [v⃗]_B = P[v⃗]_B'
> [v⃗]_B' = P⁻¹[v⃗]_B
> 
> P es invertible (columnas son LI)
> ```

## 🔍 Propiedades Adicionales

> [!note]- Resultados Importantes **Teorema de Steinitz (reemplazo):**
> 
> ```
> Si {v⃗₁, ..., v⃗ₙ} genera V y {w⃗₁, ..., w⃗ₘ} es LI,
> entonces:
> 
> 1. m ≤ n
> 2. Se pueden reemplazar m vectores de {v⃗ᵢ}
>    por {w⃗ⱼ} manteniendo la propiedad de generar
> 
> Consecuencia: dim(V) está bien definida
> ```
> 
> **Suma directa:**
> 
> ```
> Sean U, W subespacios de V
> 
> V = U ⊕ W (suma directa) si:
> 
> 1. V = U + W (todo vector se escribe como suma)
> 2. U ∩ W = {0⃗} (escritura es única)
> 
> Equivalente: Todo v⃗ ∈ V se escribe únicamente como
> v⃗ = u⃗ + w⃗ con u⃗ ∈ U, w⃗ ∈ W
> 
> Propiedad dimensional:
> V = U ⊕ W ⟹ dim(V) = dim(U) + dim(W)
> 
> Ejemplo en ℝ³:
> U = plano xy = {(x,y,0)}
> W = eje z = {(0,0,z)}
> ℝ³ = U ⊕ W
> 
> dim(ℝ³) = dim(U) + dim(W) = 2 + 1 = 3 ✓
> ```
> 
> **Complemento:**
> 
> ```
> Si W es subespacio de V, un complemento de W
> es un subespacio W' tal que:
> 
> V = W ⊕ W'
> 
> Teorema: Todo subespacio tiene complemento
> (no único en general)
> 
> Ejemplo en ℝ³:
> W = eje x
> Complementos posibles:
> • Plano yz
> • Cualquier plano que contenga y,z pero no x
> ```

## 🧩 Problemas Resueltos

> [!example]- Ejemplos Detallados **Problema 1: Verificar espacio vectorial**
> 
> ```
> Verificar si V = {(x, y) ∈ ℝ² : x + y = 0}
> es un espacio vectorial con las operaciones usuales.
> 
> SOLUCIÓN:
> 
> V = {(x, -x) : x ∈ ℝ} = {x(1, -1) : x ∈ ℝ}
> 
> Es una recta por el origen en ℝ²
> 
> Como V ⊂ ℝ², usamos criterio de subespacio:
> 
> (S1) 0⃗ ∈ V: (0, 0) satisface 0 + 0 = 0 ✓
> 
> (S2) Cerradura suma:
>      (x₁, -x₁), (x₂, -x₂) ∈ V
>      Suma: (x₁+x₂, -x₁-x₂) = (x₁+x₂, -(x₁+x₂)) ∈ V ✓
> 
> (S3) Cerradura multiplicación:
>      α(x, -x) = (αx, -αx) ∈ V ✓
> 
> Por tanto, V es subespacio de ℝ² (y por ende,
> espacio vectorial con operaciones heredadas)
> 
> Dimensión: dim(V) = 1
> Base: {(1, -1)}
> ```
> 
> **Problema 2: Independencia lineal**
> 
> ```
> Determinar si los vectores son LI en ℝ³:
> v⃗₁ = (1, 2, 3)
> v⃗₂ = (0, 1, 2)
> v⃗₃ = (1, 0, 1)
> 
> SOLUCIÓN:
> 
> Método 1: Resolver α₁v⃗₁ + α₂v⃗₂ + α₃v⃗₃ = 0⃗
> 
> α₁(1,2,3) + α₂(0,1,2) + α₃(1,0,1) = (0,0,0)
> 
> Sistema:
> α₁ + α₃ = 0         ... (1)
> 2α₁ + α₂ = 0        ... (2)
> 3α₁ + 2α₂ + α₃ = 0  ... (3)
> 
> De (1): α₃ = -α₁
> De (2): α₂ = -2α₁
> Sustituir en (3):
> 3α₁ + 2(-2α₁) + (-α₁) = 0
> 3α₁ - 4α₁ - α₁ = 0
> -2α₁ = 0
> α₁ = 0
> 
> Por tanto: α₁ = α₂ = α₃ = 0
> 
> ⟹ Los vectores son LINEALMENTE INDEPENDIENTES
> 
> Método 2: Determinante
> [1  0  1]
> [2  1  0] = 1(1-0) - 0 + 1(2-1) = 1 + 1 = 2 ≠ 0
> [3  2  1]
> 
> det ≠ 0 ⟹ LI
> 
> Como son 3 vectores LI en ℝ³:
> Forman una BASE de ℝ³
> ```
> 
> **Problema 3: Encontrar base y dimensión**
> 
> ```
> Sea W = {(x, y, z) ∈ ℝ³ : 2x - y + z = 0}
> Encontrar base y dimensión de W.
> 
> SOLUCIÓN:
> 
> W es un plano por el origen (subespacio)
> 
> Expresar condición:
> z = -2x + y
> 
> Vector general en W:
> (x, y, z) = (x, y, -2x+y)
>           = (x, y, -2x) + (0, 0, y)
>           = x(1, 0, -2) + y(0, 1, 1)
> 
> Por tanto:
> W = span{(1,0,-2), (0,1,1)}
> 
> Verificar que son LI:
> α(1,0,-2) + β(0,1,1) = (0,0,0)
> (α, β, -2α+β) = (0,0,0)
> 
> α = 0, β = 0, -2α + β = 0 ✓
> 
> Solo solución trivial ⟹ LI
> 
> Base de W: {(1,0,-2), (0,1,1)}
> Dimensión: dim(W) = 2
> 
> Cualquier vector en W se escribe:
> (x,y,z) = x(1,0,-2) + y(0,1,1)
> ```
> 
> **Problema 4: Coordenadas respecto a base**
> 
> ```
> En ℝ², sean:
> Base estándar: E = {e⃗₁, e⃗₂} = {(1,0), (0,1)}
> Base alternativa: B = {v⃗₁, v⃗₂} = {(1,1), (1,-1)}
> 
> Encontrar coordenadas de w⃗ = (3, 1) en ambas bases.
> 
> SOLUCIÓN:
> 
> Coordenadas en base estándar:
> w⃗ = 3(1,0) + 1(0,1)
> [w⃗]_E = (3, 1)ᵀ
> 
> Coordenadas en base B:
> w⃗ = α(1,1) + β(1,-1)
> (3,1) = (α+β, α-β)
> 
> Sistema:
> α + β = 3
> α - β = 1
> 
> Sumar: 2α = 4 ⟹ α = 2
> Restar: 2β = 2 ⟹ β = 1
> 
> [w⃗]_B = (2, 1)ᵀ
> 
> Verificación:
> 2(1,1) + 1(1,-1) = (2,2) + (1,-1) = (3,1) ✓
> ```
> 
> **Problema 5: Extender a base**
> 
> ```
> En ℝ⁴, dado conjunto LI:
> S = {(1,0,0,0), (0,1,1,0)}
> 
> Extender a base de ℝ⁴.
> 
> SOLUCIÓN:
> 
> Necesitamos agregar 4 - 2 = 2 vectores más
> 
> Probar vectores canónicos restantes:
> e⃗₃ = (0,0,1,0)
> e⃗₄ = (0,0,0,1)
> 
> Verificar que {v⃗₁, v⃗₂, e⃗₃, e⃗₄} es LI:
> 
> Matriz:
> [1  0  0  0]
> [0  1  0  0]
> [0  1  1  0]
> [0  0  0  1]
> 
> Reducir:
> [1  0  0  0]
> [0  1  0  0]
> [0  0  1  0]  (restar fila 2 de fila 3)
> [0  0  0  1]
> 
> 4 pivotes ⟹ LI
> 
> Base de ℝ⁴:
> {(1,0,0,0), (0,1,1,0), (0,0,1,0), (0,0,0,1)}
> 
> Nota: La extensión no es única
> Otras opciones válidas existen
> ```
> 
> **Problema 6: Suma e intersección**
> 
> ```
> En ℝ³, sean:
> U = span{(1,0,0), (0,1,0)} (plano xy)
> W = span{(0,1,0), (0,0,1)} (plano yz)
> 
> Encontrar U + W y U ∩ W.
> 
> SOLUCIÓN:
> 
> U + W:
> Vector general:
> u⃗ + w⃗ = α(1,0,0) + β(0,1,0) + γ(0,1,0) + δ(0,0,1)
>        = α(1,0,0) + (β+γ)(0,1,0) + δ(0,0,1)
> 
> Con α, β+γ, δ arbitrarios:
> U + W = span{(1,0,0), (0,1,0), (0,0,1)} = ℝ³
> 
> dim(U + W) = 3
> 
> U ∩ W:
> Vector en ambos subespacios:
> En U: (x, y, 0)
> En W: (0, y, z)
> 
> Intersección: x = 0, z = 0
> U ∩ W = {(0, y, 0) : y ∈ ℝ}
>       = span{(0,1,0)} (eje y)
> 
> dim(U ∩ W) = 1
> 
> Verificar fórmula dimensional:
> dim(U + W) = dim(U) + dim(W) - dim(U ∩ W)
> 3 = 2 + 2 - 1 ✓
> ```
> 
> **Problema 7: Polinomios**
> 
> ```
> En P₃(ℝ), sea W = {p ∈ P₃ : p(1) = 0 y p'(0) = 0}
> Encontrar base y dimensión de W.
> 
> SOLUCIÓN:
> 
> Polinomio general en P₃:
> p(x) = a₀ + a₁x + a₂x² + a₃x³
> 
> Condición 1: p(1) = 0
> a₀ + a₁ + a₂ + a₃ = 0
> a₀ = -a₁ - a₂ - a₃
> 
> Condición 2: p'(x) = a₁ + 2a₂x + 3a₃x²
> p'(0) = a₁ = 0
> 
> Sustituyendo:
> a₁ = 0
> a₀ = -a₂ - a₃
> 
> p(x) = (-a₂-a₃) + 0·x + a₂x² + a₃x³
>      = a₂(-1 + x²) + a₃(-1 + x³)
> 
> W = span{-1+x², -1+x³}
> 
> Verificar LI:
> α(-1+x²) + β(-1+x³) = 0
> (-α-β) + αx² + βx³ = 0
> 
> Coeficientes:
> -α - β = 0
> α = 0
> β = 0
> 
> De segunda y tercera: α = β = 0
> Primera se satisface: -0-0 = 0 ✓
> 
> Son LI
> 
> Base: {-1+x², -1+x³}
> Dimensión: dim(W) = 2
> ```

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "Todo conjunto de vectores es un espacio vectorial"**
> 
> ```
> ✗ FALSO
> 
> Contraejemplo: {(x,y) ∈ ℝ² : x,y > 0} (primer cuadrante)
> 
> No es espacio vectorial:
> • No contiene 0⃗ = (0,0)
> • No cerrado bajo multiplicación: -1·(1,1) = (-1,-1) ∉ conjunto
> 
> Debe satisfacer los 10 axiomas
> ```
> 
> **2. "Si genera, es base"**
> 
> ```
> ✗ FALSO
> 
> Contraejemplo en ℝ²:
> {(1,0), (0,1), (1,1)} genera ℝ² pero NO es base
> 
> Razón: No son LI (tercero es suma de primeros dos)
> 
> Para ser base: generar Y ser LI
> ```
> 
> **3. "Si son LI, es base"**
> 
> ```
> ✗ FALSO
> 
> Contraejemplo en ℝ³:
> {(1,0,0), (0,1,0)} son LI pero NO base de ℝ³
> 
> Razón: No generan todo ℝ³ (solo plano xy)
> 
> Para ser base: LI Y generar
> ```
> 
> **4. "Dos vectores paralelos son LI"**
> 
> ```
> ✗ FALSO
> 
> Vectores paralelos siempre son LD
> 
> Si v⃗₂ = αv⃗₁:
> 1·v⃗₂ - α·v⃗₁ = 0⃗ (combinación no trivial)
> ```
> 
> **5. "dim(U + W) = dim(U) + dim(W)"**
> 
> ```
> ✗ FALSO en general
> 
> Fórmula correcta:
> dim(U + W) = dim(U) + dim(W) - dim(U ∩ W)
> 
> Solo vale sin corrección si U ∩ W = {0⃗} (suma directa)
> ```
> 
> **6. "El vector cero es LI"**
> 
> ```
> ✗ FALSO
> 
> El conjunto {0⃗} es siempre LD
> 
> Razón: α·0⃗ = 0⃗ para cualquier α ≠ 0
> 
> Conjunto vacío ∅ se considera LI (vacuamente)
> ```
> 
> **7. "Coordenadas son únicas sin especificar base"**
> 
> ```
> ✗ FALSO
> 
> Las coordenadas dependen de la base elegida
> 
> Mismo vector, diferentes coordenadas en bases distintas
> 
> Ejemplo: (3,1) en ℝ²
> Base estándar: [3,1]ᵀ
> Base {(1,1),(1,-1)}: [2,1]ᵀ
> ```

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[05.1 - Vectores en Rⁿ]] - Caso concreto ℝⁿ
> - [[05.2 - Operaciones con vectores]] - Suma y producto
> - [[Álgebra abstracta]] - Estructuras algebraicas
> 
> **Temas relacionados:**
> 
> - [[09.2 - Transformaciones lineales]] - Funciones entre espacios
> - [[09.3 - Matrices y transformaciones]] - Representación
> - [[09.4 - Valores y vectores propios]] - Diagonalización
> - [[Producto interno]] - Espacios con geometría
> 
> **Aplicaciones posteriores:**
> 
> - [[Ecuaciones diferenciales]] - Espacios de soluciones
> - [[Análisis funcional]] - Espacios infinito-dimensionales
> - [[Análisis numérico]] - Métodos computacionales
> - [[Machine Learning]] - Espacios de características
> - [[Mecánica cuántica]] - Estados cuánticos
> - [[Gráficos por computadora]] - Transformaciones

## 📚Recursos Adicionales

> [!note]- Herramientas y Referencias **Software de álgebra lineal:**
> 
> - **MATLAB** - [mathworks.com](https://www.mathworks.com/)
>     - Funciones: null(), orth(), rank()
>     - Visualización de espacios vectoriales
> - **Python (NumPy/SciPy)** - [numpy.org](https://numpy.org/)
>     - numpy.linalg para álgebra lineal
>     - Jupyter notebooks para aprendizaje interactivo
> - **Octave** - [octave.org](https://www.gnu.org/software/octave/)
>     - Alternativa libre a MATLAB
> - **SageMath** - [sagemath.org](https://www.sagemath.org/)
>     - Sistema de álgebra computacional
>     - Incluye teoría de espacios vectoriales
> - **Wolfram Alpha** - [wolframalpha.com](https://www.wolframalpha.com/)
>     - "span of vectors {(1,2,3), (0,1,2)}"
>     - "linear independence {(1,0,0), (0,1,0)}"
> 
> **Visualizadores:**
> 
> - **3Blue1Brown - Essence of Linear Algebra**
>     - Videos animados explicando conceptos
>     - Visualización de transformaciones
> - **GeoGebra 3D** - Visualizar subespacios en ℝ³
> - **Linear Algebra Toolkit** - [linear.ups.edu](http://linear.ups.edu/)
>     - Herramientas interactivas
> 
> **Calculadoras online:**
> 
> - [Matrix Calculator](https://matrixcalc.org/)
> - [Symbolab](https://www.symbolab.com/solver/matrix-calculator)
> - [WolframAlpha](https://www.wolframalpha.com/)
> 
> **Tutoriales interactivos:**
> 
> - [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
> - [MIT OCW - Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)
> - [Brilliant - Linear Algebra](https://brilliant.org/courses/linear-algebra/)

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas **Nivel introductorio:**
> 
> - **Kolman, B., & Hill, D.** (2006). _Álgebra Lineal_ (8ª ed.). Pearson.
>     - Cap. 4: Espacios vectoriales reales
>     - Enfoque computacional y teórico equilibrado
> - **Lay, D. C.** (2016). _Álgebra Lineal y sus Aplicaciones_ (5ª ed.). Pearson.
>     - Cap. 4: Espacios vectoriales
>     - Énfasis en aplicaciones
>     - Muy didáctico
> - **Grossman, S. I.** (2012). _Álgebra Lineal_ (7ª ed.). McGraw-Hill.
>     - Cap. 4: Espacios vectoriales
>     - Numerosos ejemplos
> 
> **Nivel intermedio:**
> 
> - **Anton, H., & Rorres, C.** (2014). _Álgebra Lineal Elemental_ (11ª ed.). Wiley.
>     - Cap. 5: Espacios vectoriales generales
>     - Aplicaciones variadas
> - **Strang, G.** (2016). _Introduction to Linear Algebra_ (5th ed.). Wellesley-Cambridge.
>     - Enfoque geométrico e intuitivo
>     - Curso MIT disponible online
> - **Poole, D.** (2014). _Álgebra Lineal: Una Introducción Moderna_ (4ª ed.). Cengage.
>     - Aplicaciones modernas
>     - Geometría y álgebra integradas
> 
> **Nivel avanzado:**
> 
> - **Axler, S.** (2015). _Linear Algebra Done Right_ (3rd ed.). Springer.
>     - Sin determinantes hasta el final
>     - Enfoque abstracto y elegante
>     - Teoría profunda
> - **Hoffman, K., & Kunze, R.** (1971). _Linear Algebra_ (2nd ed.). Pearson.
>     - Tratado clásico
>     - Muy riguroso
>     - Nivel de posgrado
> - **Roman, S.** (2008). _Advanced Linear Algebra_ (3rd ed.). Springer.
>     - Álgebra multilineal
>     - Formas canónicas
>     - Teoría de módulos
> 
> **Aplicaciones:**
> 
> - **Meyer, C. D.** (2000). _Matrix Analysis and Applied Linear Algebra_. SIAM.
>     - Énfasis computacional
>     - Análisis numérico
> - **Trefethen, L. N., & Bau, D.** (1997). _Numerical Linear Algebra_. SIAM.
>     - Algoritmos numéricos
>     - Estabilidad y precisión
> 
> **En español:**
> 
> - **De Burgos, J.** (2006). _Álgebra Lineal y Geometría Cartesiana_ (3ª ed.). McGraw-Hill.
>     - Autor español
>     - Muy completo
> - **Rojo, J.** (2001). _Álgebra Lineal_. McGraw-Hill.
>     - Enfoque latinoamericano
> - **Nakos, G., & Joyner, D.** (1999). _Álgebra Lineal con Aplicaciones_. Thomson.
>     - Traducción de calidad
> 
> **Histórico:**
> 
> - **Grassmann, H.** (1844). _Ausdehnungslehre_.
>     - Obra fundacional (alemán)
> - **Peano, G.** (1888). _Calcolo geometrico_.
>     - Axiomas formales
> - **Van der Waerden, B. L.** (1930). _Moderne Algebra_.
>     - Sistematización moderna

## 🎓 Conceptos Clave - Mapa Mental

> [!important]- Estructura Conceptual
> 
> ```
> VECTORES EN ESPACIOS VECTORIALES
> │
> ├── DEFINICIÓN FORMAL
> │   ├── Conjunto V (vectores)
> │   ├── Campo F (escalares)
> │   ├── Operación suma: V × V → V
> │   ├── Operación producto: F × V → V
> │   └── 10 Axiomas
> │       ├── (A1-A5) Suma
> │       │   ├── Cerradura
> │       │   ├── Asociatividad
> │       │   ├── Neutro (0⃗)
> │       │   ├── Inverso (-v⃗)
> │       │   └── Conmutatividad
> │       └── (M1-M5) Multiplicación
> │           ├── Cerradura
> │           ├── Distributividad (2 tipos)
> │           ├── Asociatividad mixta
> │           └── Neutro (1·v⃗ = v⃗)
> │
> ├── EJEMPLOS FUNDAMENTALES
> │   ├── ℝⁿ, ℂⁿ (euclidianos)
> │   ├── Mₘₓₙ(F) (matrices)
> │   ├── Pₙ(F) (polinomios)
> │   ├── C[a,b] (funciones continuas)
> │   ├── ℓ² (sucesiones)
> │   └── Soluciones de EDO
> │
> ├── SUBESPACIOS
> │   ├── Definición: W ⊆ V
> │   ├── Criterio (3 condiciones)
> │   │   ├── 0⃗ ∈ W
> │   │   ├── Cerradura suma
> │   │   └── Cerradura producto
> │   └── Operaciones
> │       ├── Intersección U ∩ W
> │       ├── Suma U + W
> │       └── Suma directa U ⊕ W
> │
> ├── COMBINACIONES LINEALES
> │   ├── Definición: α₁v⃗₁ + ... + αₖv⃗ₖ
> │   ├── Conjunto generado (span)
> │   ├── Sistema generador
> │   └── Propiedades
> │       └── span{...} es subespacio
> │
> ├── INDEPENDENCIA LINEAL
> │   ├── LI: solo combinación trivial da 0⃗
> │   ├── LD: existe combinación no trivial = 0⃗
> │   ├── Caracterizaciones
> │   │   ├── Por definición
> │   │   ├── Uno es combinación de otros
> │   │   └── Se puede eliminar sin cambiar span
> │   └── Criterios prácticos
> │       ├── Determinante (matrices)
> │       ├── Rango
> │       └── Reducción escalonada
> │
> ├── BASE Y DIMENSIÓN
> │   ├── Base: LI y genera
> │   ├── Coordenadas únicas
> │   ├── Dimensión: # vectores en base
> │   ├── Bases estándar
> │   │   ├── ℝⁿ: vectores canónicos
> │   │   ├── Pₙ: {1, x, x², ..., xⁿ}
> │   │   └── Mₘₓₙ: matrices Eᵢⱼ
> │   └── Teoremas
> │       ├── Todas las bases tienen mismo #
> │       ├── Extensión de base
> │       ├── Reducción de generador
> │       └── Fórmula dimensional
> │
> ├── PROPIEDADES DERIVADAS
> │   ├── Unicidad de 0⃗ y -v⃗
> │   ├── 0·v⃗ = 0⃗ y α·0⃗ = 0⃗
> │   ├── (-1)·v⃗ = -v⃗
> │   ├── Cancelación
> │   └── Si αv⃗ = 0⃗: α = 0 o v⃗ = 0⃗
> │
> └── APLICACIONES
>     ├── Sistemas lineales
>     ├── Ecuaciones diferenciales
>     ├── Análisis funcional
>     ├── Mecánica cuántica
>     ├── Machine Learning
>     └── Gráficos por computadora
> ```

## 🌟 Conceptos Avanzados

> [!success]- Extensiones y Generalizaciones **Espacios normados:**
> 
> ```
> Espacio vectorial V con función norma ||·|| : V → ℝ⁺
> 
> Propiedades:
> 1. ||v⃗|| ≥ 0, ||v⃗|| = 0 ⟺ v⃗ = 0⃗
> 2. ||αv⃗|| = |α| ||v⃗||
> 3. ||u⃗ + v⃗|| ≤ ||u⃗|| + ||v⃗|| (desigualdad triangular)
> 
> Ejemplos:
> • ℝⁿ con norma euclidiana: ||v⃗|| = √(Σvᵢ²)
> • ℝⁿ con norma p: ||v⃗||_p = (Σ|vᵢ|ᵖ)^(1/p)
> • C[a,b] con norma sup: ||f|| = max|f(x)|
> 
> Permite definir convergencia, continuidad
> ```
> 
> **Espacios con producto interno:**
> 
> ```
> Espacio vectorial V con producto interno ⟨·,·⟩ : V×V → F
> 
> Propiedades (caso real):
> 4. ⟨u⃗, v⃗⟩ = ⟨v⃗, u⃗⟩ (simetría)
> 5. ⟨αu⃗ + βv⃗, w⃗⟩ = α⟨u⃗, w⃗⟩ + β⟨v⃗, w⃗⟩ (linealidad)
> 6. ⟨v⃗, v⃗⟩ ≥ 0, ⟨v⃗, v⃗⟩ = 0 ⟺ v⃗ = 0⃗ (positividad)
> 
> Induce norma: ||v⃗|| = √⟨v⃗, v⃗⟩
> 
> Ejemplos:
> • ℝⁿ: ⟨u⃗, v⃗⟩ = Σuᵢvᵢ (producto punto)
> • C[a,b]: ⟨f, g⟩ = ∫ₐᵇ f(x)g(x)dx
> 
> Permite definir ortogonalidad, proyecciones
> ```
> 
> **Espacios de Hilbert:**
> 
> ```
> Espacio con producto interno, completo
> (toda sucesión de Cauchy converge)
> 
> Generalización infinito-dimensional de ℝⁿ
> 
> Ejemplos:
> • ℓ²: sucesiones de cuadrado sumable
> • L²[a,b]: funciones de cuadrado integrable
> 
> Fundamentales en:
> • Análisis funcional
> • Mecánica cuántica (estados cuánticos)
> • Procesamiento de señales
> ```
> 
> **Espacios cociente:**
> 
> ```
> Dado subespacio W de V:
> 
> Espacio cociente: V/W
> Elementos: clases de equivalencia [v⃗] = v⃗ + W
> 
> v⃗ ~ u⃗ ⟺ v⃗ - u⃗ ∈ W
> 
> Operaciones:
> [v⃗] + [u⃗] = [v⃗ + u⃗]
> α[v⃗] = [αv⃗]
> 
> Dimensión: dim(V/W) = dim(V) - dim(W)
> 
> Aplicaciones en álgebra abstracta
> ```
> 
> **Duales y funcionales:**
> 
> ```
> Espacio dual V*: funcionales lineales sobre V
> 
> V* = {φ : V → F : φ es lineal}
> 
> Operaciones:
> (φ + ψ)(v⃗) = φ(v⃗) + ψ(v⃗)
> (αφ)(v⃗) = αφ(v⃗)
> 
> V* es espacio vectorial
> 
> Si dim(V) = n finita: dim(V*) = n
> V ≅ V** (bidual)
> 
> Base dual: si B = {v⃗₁, ..., v⃗ₙ} base de V
> Base dual B* = {φ₁, ..., φₙ} donde φᵢ(v⃗ⱼ) = δᵢⱼ
> ```

## 🎯 Aplicaciones Específicas

> [!note]- Contextos Prácticos **Machine Learning:**
> 
> ```
> Espacio de características:
> • Datos como vectores en ℝⁿ
> • Dimensión = número de características
> • Transformaciones lineales (PCA, LDA)
> • Proyecciones para reducción dimensional
> • Kernel trick (espacios de Hilbert)
> 
> Ejemplo: Clasificación de imágenes
> Imagen 28×28 pixels → vector en ℝ⁷⁸⁴
> ```
> 
> **Mecánica Cuántica:**
> 
> ```
> Estados cuánticos como vectores:
> • Espacio de Hilbert complejo
> • Superposición = combinación lineal
> • Observables = operadores lineales
> • Medición = proyección
> 
> |ψ⟩ = α|0⟩ + β|1⟩ (qubit)
> Base computacional: {|0⟩, |1⟩}
> ```
> 
> **Procesamiento de Señales:**
> 
> ```
> Señales como funciones en L²:
> • Series de Fourier = combinaciones lineales
> • Base: {e^(inx)}
> • Transformadas lineales
> • Filtros = proyecciones en subespacios
> ```
> 
> **Gráficos por Computadora:**
> 
> ```
> Transformaciones geométricas:
> • Puntos como vectores en ℝ³ o ℝ⁴
> • Rotaciones, escalas, traslaciones
> • Matrices de transformación
> • Espacios de colores (RGB, HSV)
> ```
> 
> **Redes Neuronales:**
> 
> ```
> Arquitectura como composición de transformaciones:
> • Capas = transformaciones lineales + no linealidad
> • Pesos = matrices
> • Backpropagation = cálculo en espacio tangente
> • Embeddings = representación en espacio vectorial
> ```
> 
> **Optimización:**
> 
> ```
> Espacios de soluciones:
> • Factibilidad = subespacio o cono
> • Gradientes en espacio dual
> • Direcciones de descenso
> • Restricciones lineales definen subespacios
> ```

## 💡 Intuición Geométrica

> [!tip]- Visualización de Conceptos **Dimensión como grados de libertad:**
> 
> ```
> • dim = 0: punto (sin movimiento)
> • dim = 1: recta (un parámetro)
> • dim = 2: plano (dos parámetros)
> • dim = 3: espacio (tres parámetros)
> • dim = n: hiperplano n-dimensional
> 
> Cada dimensión agrega un "eje" independiente
> ```
> 
> **Base como sistema de coordenadas:**
> 
> ```
> Elegir base = elegir "reglas" para medir
> 
> Diferentes bases = diferentes perspectivas
> del mismo espacio
> 
> Cambio de base = cambio de perspectiva
> (como rotar sistema coordenado)
> ```
> 
> **Independencia lineal:**
> 
> ```
> Geométricamente:
> 
> 2 vectores LI en ℝ³ → generan plano
> No están en misma recta
> 
> 3 vectores LI en ℝ³ → generan todo ℝ³
> No están en mismo plano
> 
> Cada vector añade nueva "dirección"
> ```
> 
> **Subespacios como restricciones:**
> 
> ```
> Ecuación lineal = restricción = quita 1 dimensión
> 
> En ℝ³:
> • 0 ecuaciones: ℝ³ (dim 3)
> • 1 ecuación: plano (dim 2)
> • 2 ecuaciones: recta (dim 1)
> • 3 ecuaciones: punto (dim 0)
> 
> Cada restricción independiente reduce dimensión en 1
> ```

---

**Tags:** #espacios-vectoriales #algebra-lineal #vectores #base #dimension #independencia-lineal #subespacios #combinaciones-lineales #axiomas #estructuras-algebraicas #generador #coordenadas

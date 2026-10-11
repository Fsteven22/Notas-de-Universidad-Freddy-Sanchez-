---
dg-publish: true
---

# ⚡ Producto Cruz y Áreas

## 🎯 Fundamentos del Producto Cruz

> [!info] 💡 Introducción al Producto Vectorial El **producto cruz** (también llamado **producto vectorial**) es una operación entre dos vectores en ℝ³ que resulta en un **nuevo vector perpendicular** a ambos vectores originales. Es fundamental en física, ingeniería y geometría espacial.
> 
> **Analogías útiles:**
> 
> - **Física:** Momento de una fuerza (torque) τ⃗ = \vec{r} × \vec{F}
> - **Geometría:** Área del paralelogramo formado por dos vectores
> - **Rotación:** Eje de rotación perpendicular al plano de giro
> - **Magnetismo:** Fuerza magnética \vec{F} = q\vec{v} × \vec{B}
> 
> **Diferencia fundamental:**
> 
> - **Producto punto:** u · v = escalar
> - **Producto cruz:** u × v = vector perpendicular
> 
> **Importancia histórica:**
> 
> - **William Rowan Hamilton (1843):** Cuaterniones (precursores)
> - **Hermann Grassmann (1844):** Producto exterior
> - **Josiah Willard Gibbs (1881):** Notación moderna del producto cruz
> - **Oliver Heaviside (1892):** Aplicaciones en electromagnetismo
> 
> **Característica única:**
> 
> - Solo está definido en ℝ³ (y ℝ⁷ con propiedades especiales)
> - No existe en ℝ² ni en ℝ⁴

### 📝 Definición Formal

> [!note] 🌟 Concepto Matemático del Producto Cruz **Definición algebraica:**
> 
> Dados dos vectores **u** = (u₁, u₂, u₃) y **v** = (v₁, v₂, v₃) en ℝ³, su producto cruz es:
> 
> **u × v = (u₂v₃ - u₃v₂, u₃v₁ - u₁v₃, u₁v₂ - u₂v₁)**
> 
> **Fórmula con determinante:**
> 
> ```
> u × v = |i    j    k  |
>         |u₁   u₂   u₃ |
>         |v₁   v₂   v₃ |
> ```
> 
> Expandiendo por la primera fila:
> 
> **u × v = i(u₂v₃ - u₃v₂) - j(u₁v₃ - u₃v₁) + k(u₁v₂ - u₂v₁)**
> 
> **Propiedades geométricas:**
> 
> 1. **Dirección:** Perpendicular a u y a v
> 2. **Sentido:** Regla de la mano derecha
> 3. **Magnitud:** ||u × v|| = ||u|| · ||v|| · sen(θ)
> 4. **Área:** ||u × v|| = área del paralelogramo formado por u y v
> 
> **Notaciones equivalentes:**
> 
> - u × v (más común)
> - u ∧ v (notación alternativa)
> - [u, v] (menos común)

### 🔢 Cálculo del Producto Cruz

> [!example] 📊 Método del Determinante **Método práctico:**
> 
> **Paso 1:** Formar el determinante 3×3
> 
> ```
> |i    j    k  |
> |u₁   u₂   u₃ |
> |v₁   v₂   v₃ |
> ```
> 
> **Paso 2:** Expandir por cofactores de la primera fila
> 
> **Componente i:**
> 
> ```
> i · |u₂  u₃|  = i(u₂v₃ - u₃v₂)
>     |v₂  v₃|
> ```
> 
> **Componente j:** (¡Con signo negativo!)
> 
> ```
> -j · |u₁  u₃|  = -j(u₁v₃ - u₃v₁) = j(u₃v₁ - u₁v₃)
>      |v₁  v₃|
> ```
> 
> **Componente k:**
> 
> ```
> k · |u₁  u₂|  = k(u₁v₂ - u₂v₁)
>     |v₁  v₂|
> ```
> 
> **Ejemplos básicos:**
> 
> **Ejemplo 1:**
> 
> ```
> u = (1, 0, 0)
> v = (0, 1, 0)
> 
> u × v = |i  j  k|
>         |1  0  0|
>         |0  1  0|
> 
>       = i(0·0 - 0·1) - j(1·0 - 0·0) + k(1·1 - 0·0)
>       = i(0) - j(0) + k(1)
>       = (0, 0, 1) = k
> ```
> 
> **Ejemplo 2:**
> 
> ```
> u = (2, 3, 1)
> v = (1, -2, 3)
> 
> u × v = |i   j   k |
>         |2   3   1 |
>         |1  -2   3 |
> 
>       = i(3·3 - 1·(-2)) - j(2·3 - 1·1) + k(2·(-2) - 3·1)
>       = i(9 + 2) - j(6 - 1) + k(-4 - 3)
>       = i(11) - j(5) + k(-7)
>       = (11, -5, -7)
> ```
> 
> **Ejemplo 3:**
> 
> ```
> u = (1, 2, 3)
> v = (2, 4, 6) = 2u
> 
> u × v = |i  j  k|
>         |1  2  3|
>         |2  4  6|
> 
>       = i(2·6 - 3·4) - j(1·6 - 3·2) + k(1·4 - 2·2)
>       = i(12 - 12) - j(6 - 6) + k(4 - 4)
>       = (0, 0, 0)
> 
> ¡Vectores paralelos dan producto cruz cero!
> ```

## 🧭 Regla de la Mano Derecha

### ✋ Determinación del Sentido

> [!tip] 👉 Método Visual **La regla de la mano derecha determina el sentido de u × v:**
> 
> **Método 1 - Dedos curvados:**
> 
> 1. Apunta los dedos de tu mano derecha en dirección de **u**
> 2. Curva los dedos hacia **v** (por el ángulo más pequeño)
> 3. Tu pulgar extendido apunta en dirección de **u × v**
> 
> **Método 2 - Sistema de coordenadas:**
> 
> - **i × j = k** ✓
> - **j × k = i** ✓
> - **k × i = j** ✓
> 
> Ciclo: i → j → k → i (sentido antihorario visto desde arriba)
> 
> **Método 3 - Tornillo:**
> 
> - Gira un tornillo (rosca derecha) de u hacia v
> - El tornillo avanza en dirección de u × v
> 
> **Verificación:**
> 
> ```
> Si u × v = w, entonces:
> - w ⊥ u (w · u = 0)
> - w ⊥ v (w · v = 0)
> - w sigue la regla de la mano derecha
> ```
> 
> **Ejemplo práctico:**
> 
> ```
> i × j = ?
> 
> Dedos apuntan en +X (i)
> Curvas hacia +Y (j)
> Pulgar apunta en +Z
> 
> Por lo tanto: i × j = k ✓
> ```

### 🔄 Productos de Vectores Base

> [!success] 📐 Tabla de Productos Cruz Básicos
> 
> **Vectores base:** i = (1,0,0), j = (0,1,0), k = (0,0,1)
> 
> |×|**i**|**j**|**k**|
> |---|---|---|---|
> |**i**|**0**|**k**|**-j**|
> |**j**|**-k**|**0**|**i**|
> |**k**|**j**|**-i**|**0**|
> 
> **Propiedades observables:**
> 
> 1. Diagonal principal: todos ceros (i × i = 0)
> 2. Antisimetría: j × i = -(i × j) = -k
> 3. Ciclo positivo: i → j → k → i
> 4. Ciclo negativo: i → k → j → i
> 
> **Regla mnemotécnica:**
> 
> ```
> Ciclo directo (↻):  i × j = k,  j × k = i,  k × i = j
> Ciclo inverso (↺):  j × i = -k, k × j = -i, i × k = -j
> ```
> 
> **Dibujo conceptual:**
> 
> ```
>        k (arriba)
>        |
>        |
>        o----→ i (derecha)
>       /
>      /
>     j (frente)
> ```

## 📐 Propiedades del Producto Cruz

### ⚖️ Propiedades Algebraicas

> [!note] 🔢 Propiedades Fundamentales **1. Anticonmutativa:**
> 
> ```
> u × v = -(v × u)
> ```
> 
> ¡El orden importa! Cambiar el orden invierte el resultado.
> 
> **2. Distributiva respecto a la suma:**
> 
> ```
> u × (v + w) = u × v + u × w
> (u + v) × w = u × w + v × w
> ```
> 
> **3. Asociativa con escalares:**
> 
> ```
> (ku) × v = k(u × v) = u × (kv)
> ```
> 
> Donde k es un escalar.
> 
> **4. NO es asociativa:**
> 
> ```
> u × (v × w) ≠ (u × v) × w  (en general)
> ```
> 
> **5. Producto con sí mismo:**
> 
> ```
> u × u = 0  (para todo vector u)
> ```
> 
> **6. Producto con vector cero:**
> 
> ```
> u × 0 = 0
> 0 × u = 0
> ```
> 
> **7. Vectores paralelos:**
> 
> ```
> u × v = 0  ⟺  u y v son paralelos
> ```
> 
> **8. Identidad de Jacobi:**
> 
> ```
> u × (v × w) + v × (w × u) + w × (u × v) = 0
> ```

### 🎯 Propiedades Geométricas

> [!warning] 📏 Interpretación Geométrica **1. Perpendicularidad:**
> 
> ```
> (u × v) ⊥ u
> (u × v) ⊥ v
> 
> Verificación:
> (u × v) · u = 0
> (u × v) · v = 0
> ```
> 
> **2. Magnitud (Área del paralelogramo):**
> 
> ```
> ||u × v|| = ||u|| · ||v|| · sen(θ)
> ```
> 
> Donde θ es el ángulo entre u y v (0 ≤ θ ≤ π)
> 
> **Interpretación:**
> 
> - ||u × v|| = área del paralelogramo con lados u y v
> - ½||u × v|| = área del triángulo con lados u y v
> 
> **3. Magnitud máxima:**
> 
> ```
> ||u × v|| es máxima cuando u ⊥ v
> ||u × v||ₘₐₓ = ||u|| · ||v|| (cuando θ = 90°)
> ```
> 
> **4. Magnitud mínima:**
> 
> ```
> ||u × v|| = 0 cuando u ∥ v
> (vectores paralelos o uno es cero)
> ```
> 
> **5. Relación con producto punto:**
> 
> ```
> ||u × v||² + (u · v)² = ||u||² · ||v||²
> ```
> 
> (Identidad de Lagrange)

## 📊 Cálculo de Áreas

### 🔺 Área de Triángulos

> [!success] 📐 Fórmula del Área **Dados tres puntos A, B, C en ℝ³:**
> 
> **Método 1 - Usando vectores:**
> 
> ```
> A\vec{B} = B - A
> A\vec{C} = C - A
> 
> Área = ½||A\vec{B} × A\vec{C}||
> ```
> 
> **Método 2 - Fórmula directa:**
> 
> ```
> Área = ½√[(A\vec{B} × A\vec{C}) · (A\vec{B} × A\vec{C})]
> ```
> 
> **Interpretación:**
> 
> - A\vec{B} × A\vec{C} es perpendicular al plano del triángulo
> - ||A\vec{B} × A\vec{C}|| es el área del paralelogramo
> - El triángulo es la mitad del paralelogramo
> 
> **Ejemplo:**
> 
> ```
> A = (1, 0, 0)
> B = (0, 1, 0)
> C = (0, 0, 1)
> 
> A\vec{B} = (0, 1, 0) - (1, 0, 0) = (-1, 1, 0)
> A\vec{C} = (0, 0, 1) - (1, 0, 0) = (-1, 0, 1)
> 
> A\vec{B} × A\vec{C} = |i   j   k |
>            |-1  1   0 |
>            |-1  0   1 |
> 
>          = i(1·1 - 0·0) - j((-1)·1 - 0·(-1)) + k((-1)·0 - 1·(-1))
>          = i(1) - j(-1) + k(1)
>          = (1, 1, 1)
> 
> ||A\vec{B} × A\vec{C}|| = √(1² + 1² + 1²) = √3
> 
> Área = ½√3 ≈ 0.866 unidades²
> ```

### ▱ Área de Paralelogramos

> [!info] 📐 Paralelogramo Formado por Vectores **Dados dos vectores u y v:**
> 
> **Área del paralelogramo:**
> 
> ```
> A = ||u × v||
> ```
> 
> **Interpretación:**
> 
> - Los vectores u y v forman dos lados adyacentes
> - El área es la magnitud del producto cruz
> 
> **Fórmula alternativa:**
> 
> ```
> A = ||u|| · ||v|| · sen(θ)
> ```
> 
> Donde θ es el ángulo entre u y v.
> 
> **Ejemplo:**
> 
> ```
> u = (3, 0, 0)
> v = (0, 4, 0)
> 
> u × v = |i  j  k|
>         |3  0  0|
>         |0  4  0|
> 
>       = i(0·0 - 0·4) - j(3·0 - 0·0) + k(3·4 - 0·0)
>       = (0, 0, 12)
> 
> Área = ||u × v|| = 12 unidades²
> 
> Verificación:
> A = ||u|| · ||v|| · sen(90°) = 3 · 4 · 1 = 12 ✓
> ```
> 
> **Caso con cuatro puntos:**
> 
> Si tenemos un paralelogramo ABCD:
> 
> ```
> A\vec{B} = B - A
> A\vec{D} = D - A
> 
> Área = ||A\vec{B} × A\vec{D}||
> ```

### 🔷 Área de Polígonos Generales

> [!tip] 🔢 Polígonos en el Espacio **Para un polígono con vértices P₁, P₂, ..., Pₙ:**
> 
> **Método de triangulación:**
> 
> 1. Dividir el polígono en triángulos desde P₁
> 2. Calcular área de cada triángulo
> 3. Sumar todas las áreas
> 
> ```
> Triángulos: P₁P₂P₃, P₁P₃P₄, ..., P₁Pₙ₋₁Pₙ
> 
> Área total = Σ (½||P₁Pᵢ⃗ × P₁Pᵢ₊₁⃗||)
> ```
> 
> **Ejemplo - Cuadrilátero:**
> 
> ```
> Puntos: A = (0,0,0), B = (1,0,0), C = (1,1,0), D = (0,1,0)
> 
> Triángulo 1: ABC
> A\vec{B} = (1, 0, 0)
> A\vec{C} = (1, 1, 0)
> A\vec{B} × A\vec{C} = (0, 0, 1)
> Á₁ = ½||(0, 0, 1)|| = ½
> 
> Triángulo 2: ACD
> A\vec{C} = (1, 1, 0)
> A\vec{D} = (0, 1, 0)
> A\vec{C} × A\vec{D} = (0, 0, 1)
> Á₂ = ½||(0, 0, 1)|| = ½
> 
> Área total = ½ + ½ = 1 unidad²
> ```

## ⚡ Aplicaciones Físicas

### 🔄 Momento de una Fuerza (Torque)

> [!warning] 🔧 Torque Vectorial **Definición:**
> 
> El momento τ⃗ (torque) de una fuerza \vec{F} aplicada en un punto, respecto a un punto de referencia O, es:
> 
> **τ⃗ = \vec{r} × \vec{F}**
> 
> Donde:
> 
> - **\vec{r}** = vector posición desde O hasta el punto de aplicación de \vec{F}
> - **\vec{F}** = vector fuerza
> - **τ⃗** = vector momento (perpendicular al plano \vec{r}-\vec{F})
> 
> **Magnitud:**
> 
> ```
> ||τ⃗|| = ||\vec{r}|| · ||\vec{F}|| · sen(θ)
>       = d · ||\vec{F}||
> ```
> 
> Donde d es la distancia perpendicular de O a la línea de acción de \vec{F}.
> 
> **Unidades:** N·m (newton-metro)
> 
> **Interpretación:**
> 
> - Magnitud: capacidad de rotación
> - Dirección: eje de rotación
> - Sentido: regla de la mano derecha
> 
> **Ejemplo:**
> 
> ```
> Una llave de 0.3 m se usa para apretar un tornillo.
> Se aplica una fuerza \vec{F} = (0, 50, 0) N al extremo.
> El tornillo está en el origen.
> 
> \vec{r} = (0.3, 0, 0) m
> \vec{F} = (0, 50, 0) N
> 
> τ⃗ = \vec{r} × \vec{F} = |i    j    k  |
>                |0.3  0    0  |
>                |0    50   0  |
> 
>             = i(0·0 - 0·50) - j(0.3·0 - 0·0) + k(0.3·50 - 0·0)
>             = (0, 0, 15) N·m
> 
> ||τ⃗|| = 15 N·m (torque en dirección +Z)
> El tornillo gira en sentido antihorario visto desde arriba
> ```

### 🧲 Fuerza Magnética

> [!info] ⚡ Fuerza de Lorentz **La fuerza sobre una carga en movimiento en un campo magnético:**
> **\vec{F} = q(\vec{v} × \vec{B})**
> 
> Donde:
> 
> - **q** = carga eléctrica (coulombs)
> - **\vec{v}** = velocidad de la partícula (m/s)
> - **\vec{B}** = campo magnético (teslas, T)
> - **\vec{F}** = fuerza magnética (newtons, N)
> 
> **Propiedades:**
> 
> 1. \vec{F} ⊥ \vec{v} (perpendicular a la velocidad)
> 2. \vec{F} ⊥ \vec{B} (perpendicular al campo)
> 3. \vec{F} no realiza trabajo (W = \vec{F} · \vec{d} = 0)
> 4. Cambia dirección pero no rapidez
> 
> **Magnitud:**
> 
> ```
> ||\vec{F}|| = |q| · ||\vec{v}|| · ||\vec{B}|| · sen(θ)
> ```
> 
> **Ejemplo:**
> 
> ```
> Un electrón (q = -1.6 × 10⁻¹⁹ C) se mueve con:
> \vec{v} = (2×10⁶, 0, 0) m/s
> 
> En un campo magnético:
> \vec{B} = (0, 0, 0.5) T
> 
> \vec{F} = q(\vec{v} × \vec{B})
> 
> \vec{v} × \vec{B} = |i         j    k  |
>          |2×10⁶     0    0  |
>          |0         0    0.5|
> 
>        = i(0·0.5 - 0·0) - j(2×10⁶·0.5 - 0·0) + k(2×10⁶·0 - 0·0)
>        = (0, -10⁶, 0) T·m/s
> 
> \vec{F} = (-1.6×10⁻¹⁹)(0, -10⁶, 0)
>   = (0, 1.6×10⁻¹³, 0) N
> 
> La fuerza apunta en dirección +Y
> ```

### 🌊 Momento Angular

> [!success] 🔄 Cantidad de Movimiento Angular **Definición:**
> 
> El momento angular \vec{L} de una partícula respecto a un punto O es:
> 
> **\vec{L} = \vec{r} × \vec{p} = \vec{r} × (m\vec{v})**
> 
> Donde:
> 
> - **\vec{r}** = vector posición desde O
> - **\vec{p}** = momento lineal = m\vec{v}
> - **m** = masa
> - **\vec{v}** = velocidad
> 
> **Conservación:**
> 
> Si τ⃗ₑₓₜ = 0 (no hay torques externos):
> 
> ```
> \vec{L} = constante
> ```
> 
> **Relación con torque:**
> 
> ```
> τ⃗ = d\vec{L}/dt
> ```
> 
> **Ejemplo:**
> 
> ```
> Una partícula de masa m = 2 kg en:
> \vec{r} = (3, 0, 0) m
> \vec{v} = (0, 4, 0) m/s
> 
> \vec{L} = \vec{r} × (m\vec{v})
>   = (3, 0, 0) × (2·(0, 4, 0))
>   = (3, 0, 0) × (0, 8, 0)
> 
>   = |i  j  k|
>     |3  0  0|
>     |0  8  0|
> 
>   = (0, 0, 24) kg·m²/s
> 
> El momento angular apunta en dirección +Z
> ```

## 🔺 Producto Triple Escalar

### 📦 Volumen de Paralelepípedos

> [!note] 🎲 Triple Producto Escalar **Definición:**
> 
> El producto triple escalar de tres vectores u, v, w es:
> 
> **u · (v × w)**
> 
> También se nota como: [u, v, w]
> 
> **Cálculo con determinante:**
> 
> ```
> u · (v × w) = |u₁  u₂  u₃|
>               |v₁  v₂  v₃|
>               |w₁  w₂  w₃|
> ```
> 
> **Interpretación geométrica:**
> 
> **|u · (v × w)| = volumen del paralelepípedo formado por u, v, w**
> 
> **Propiedades:**
> 
> 1. **Permutación cíclica:**
> 
> ```
> u · (v × w) = v · (w × u) = w · (u × v)
> ```
> 
> 2. **Cambio de orden:**
> 
> ```
> u · (v × w) = -(u · (w × v))
> ```
> 
> 3. **Vectores coplanares:**
> 
> ```
> u · (v × w) = 0  ⟺  u, v, w son coplanares
> ```
> 
> 4. **Distributiva:**
> 
> ```
> u · (v × (w + t)) = u · (v × w) + u · (v × t)
> ```
> 
> **Ejemplo:**
> 
> ```
> u = (1, 0, 0)
> v = (0, 2, 0)
> w = (0, 0, 3)
> 
> u · (v × w) = |1  0  0|
>               |0  2  0|
>               |0  0  3|
> 
>             = 1·|2  0| - 0 + 0
>                 |0  3|
> 
>             = 1·(2·3 - 0·0) = 6
> 
> Volumen = |6| = 6 unidades³
> 
> (Es un paralelepípedo rectangular de 1×2×3)
> ```

### 🔺 Volumen de Tetraedros

> [!example] 📐 Pirámide Triangular **Dado un tetraedro con vértices A, B, C, D:**
> 
> **Volumen = (1/6)|A\vec{B} · (A\vec{C} × A\vec{D})|**
> 
> **Proceso:**
> 
> 1. Calcular vectores desde A: A\vec{B}, A\vec{C}, A\vec{D}
> 2. Calcular A\vec{C} × A\vec{D}
> 3. Calcular A\vec{B} · (A\vec{C} × A\vec{D})
> 4. Tomar valor absoluto y dividir entre 6
> 
> **Ejemplo:**
> 
> ```
> A = (0, 0, 0)
> B = (1, 0, 0)
> C = (0, 1, 0)
> D = (0, 0, 1)
> 
> A\vec{B} = (1, 0, 0)
> A\vec{C} = (0, 1, 0)
> A\vec{D} = (0, 0, 1)
> 
> A\vec{C} × A\vec{D} = |i  j  k|
>            |0  1  0|
>            |0  0  1|
> 
>          = (1, 0, 0)
> 
> A\vec{B} · (A\vec{C} × A\vec{D}) = (1, 0, 0) · (1, 0, 0) = 1
> 
> Volumen = (1/6)|1| = 1/6 unidades³
> ```

## 🎨 Aplicaciones Geométricas

### 📐 Vector Normal a un Plano

> [!tip] ⊥ Perpendicular al Plano **Dados dos vectores u y v en un plano:**
> 
> **Un vector perpendicular al plano es:** **\vec{n} = u × v**
> 
> **Propiedades:**
> 
> - \vec{n} ⊥ u
> - \vec{n} ⊥ v
> - \vec{n} ⊥ (cualquier combinación lineal de u y v)
> 
> **Vector unitario normal:**
> 
> ```
> \hat{n} = (u × v) / ||u × v||
> ```
> 
> **Aplicación - Ecuación del plano:**
> 
> Si el plano pasa por punto P₀ y tiene vectores directores u y v:
> 
> ```
> \vec{n} = u × v
> 
> Ecuación: \vec{n} · (P - P₀) = 0
> ```
> 
> **Ejemplo:**
> 
> ```
> Plano que contiene los puntos:
> A = (1, 0, 0)
> B = (0, 1, 0)
> C = (0, 0, 1)
> 
> Vectores en el plano:
> A\vec{B} = (-1, 1, 0)
> A\vec{C} = (-1, 0, 1)
> 
> Normal:
> \vec{n} = A\vec{B} × A\vec{C} = |i   j   k |
>                 |-1  1   0 |
>                 |-1  0   1 |
> 
>              = i(1·1 - 0·0) - j((-1)·1 - 0·(-1)) + k((-1)·0 - 1·(-1))
>              = (1, 1, 1)
> 
> Ecuación del plano usando punto A:
> (1, 1, 1) · [(x, y, z) - (1, 0, 0)] = 0
> (1, 1, 1) · (x-1, y, z) = 0
> (x-1) + y + z = 0
> x + y + z = 1
> ```

### 📏 Distancia de Punto a Recta

> [!success] 📐 Distancia Perpendicular **Dados:**
> 
> - Punto P
> - Recta que pasa por Q con dirección \vec{v}
> 
> **Distancia de P a la recta:**
> 
> **d = ||Q\vec{P} × \vec{v}|| / ||\vec{v}||**
> 
> **Justificación:**
> 
> - Q\vec{P} × \vec{v} tiene magnitud igual al área del paralelogramo
> - Área = base × altura = ||\vec{v}|| × d
> - Entonces: ||Q\vec{P} × \vec{v}|| = ||\vec{v}|| × d
> 
> **Ejemplo:**
> 
> ```
> Punto P = (2, 1, 3)
> Recta por Q = (0, 0, 0) con dirección \vec{v} = (1, 0, 0)
> 
> Q\vec{P} = (2, 1, 3)
> 
> Q\vec{P} × \vec{v} = |i  j  k|
>           |2  1  3|
>           |1  0  0|
> 
>         = i(1·0 - 3·0) - j(2·0 - 3·1) + k(2·0 - 1·1)
>         = (0, 3, -1)
> 
> ||Q\vec{P} × \vec{v}|| = √(0² + 3² + (-1)²) = √10
> ||\vec{v}|| = 1
> 
> d = √10 / 1 = √10 ≈ 3.16 unidades
> ```

## 🔄 Identidades Vectoriales

> [!note] 🧮 Fórmulas Importantes **1. Producto vectorial triple (BAC-CAB):**
> 
> ```
> u × (v × w) = v(u · w) - w(u · v)
> ```
> 
> Mnemotecnia: "Back Cab"
> 
> **2. Identidad de Lagrange:**
> 
> ```
> ||u × v||² = ||u||² ||v||² - (u · v)²
> ```
> 
> **3. Relación con producto punto:**
> 
> ```
> (u × v) · (w × t) = (u · w)(v · t) - (u · t)(v · w)
> ```
> 
> **4. Doble producto vectorial:**
> 
> ```
> (u × v) × w = v(u · w) - u(v · w)
> ```
> 
> **5. Producto de cuatro vectores:**
> 
> ```
> (u × v) · (w × t) = |u·w  u·t|
>                      |v·w  v·t|
> ```

## 🧪 Ejercicios Integrales

> [!example] 💪 Práctica Completa **Nivel 1 - Básico:** 🟢
> 
> 1. Calcular el producto cruz: a) u = (1, 2, 3) × v = (4, 5, 6) b) i × j c) k × i
> 
> **Solución:**
> 
> ```
> a) u × v = |i  j  k|
>            |1  2  3|
>            |4  5  6|
> 
>          = i(2·6 - 3·5) - j(1·6 - 3·4) + k(1·5 - 2·4)
>          = i(12 - 15) - j(6 - 12) + k(5 - 8)
>          = (-3, 6, -3)
> 
> b) i × j = (1,0,0) × (0,1,0)
>          = |i  j  k|
>            |1  0  0|
>            |0  1  0|
>          = k = (0, 0, 1)
> 
> c) k × i = (0,0,1) × (1,0,0)
>          = |i  j  k|
>            |0  0  1|
>            |1  0  0|
>          = j = (0, 1, 0)
> ```
> 
> 2. Verificar que u × v es perpendicular tanto a u como a v: u = (2, 1, -1), v = (1, 3, 2)
> 
> **Solución:**
> 
> ```
> u × v = |i   j   k |
>         |2   1  -1 |
>         |1   3   2 |
> 
>       = i(1·2 - (-1)·3) - j(2·2 - (-1)·1) + k(2·3 - 1·1)
>       = i(2 + 3) - j(4 + 1) + k(6 - 1)
>       = (5, -5, 5)
> 
> Verificación:
> (u × v) · u = (5, -5, 5) · (2, 1, -1)
>             = 10 - 5 - 5 = 0 ✓
> 
> (u × v) · v = (5, -5, 5) · (1, 3, 2)
>             = 5 - 15 + 10 = 0 ✓
> ```
> 
> ---
> 
> **Nivel 2 - Intermedio:** 🟡
> 
> 3. Calcular el área del triángulo con vértices: A = (1, 0, 0), B = (0, 2, 0), C = (0, 0, 3)
> 
> **Solución:**
> 
> ```
> A\vec{B} = (-1, 2, 0)
> A\vec{C} = (-1, 0, 3)
> 
> A\vec{B} × A\vec{C} = |i   j   k |
>            |-1  2   0 |
>            |-1  0   3 |
> 
>          = i(2·3 - 0·0) - j((-1)·3 - 0·(-1)) + k((-1)·0 - 2·(-1))
>          = i(6) - j(-3) + k(2)
>          = (6, 3, 2)
> 
> ||A\vec{B} × A\vec{C}|| = √(36 + 9 + 4) = √49 = 7
> 
> Área = ½·7 = 3.5 unidades²
> ```
> 
> 4. Encontrar un vector unitario perpendicular al plano que contiene: u = (1, 1, 0) y v = (0, 1, 1)
> 
> **Solución:**
> 
> ```
> \vec{n} = u × v = |i  j  k|
>             |1  1  0|
>             |0  1  1|
> 
>           = i(1·1 - 0·1) - j(1·1 - 0·0) + k(1·1 - 1·0)
>           = (1, -1, 1)
> 
> ||\vec{n}|| = √(1 + 1 + 1) = √3
> 
> \hat{n} = \vec{n}/||\vec{n}|| = (1/√3, -1/√3, 1/√3)
>              ≈ (0.577, -0.577, 0.577)
> ```
> 
> ---
> 
> **Nivel 3 - Avanzado:** 🔴
> 
> 5. Calcular el volumen del tetraedro con vértices: A = (0, 0, 0), B = (2, 0, 0), C = (0, 3, 0), D = (0, 0, 4)
> 
> **Solución:**
> 
> ```
> A\vec{B} = (2, 0, 0)
> A\vec{C} = (0, 3, 0)
> A\vec{D} = (0, 0, 4)
> 
> A\vec{C} × A\vec{D} = |i  j  k|
>            |0  3  0|
>            |0  0  4|
> 
>          = (12, 0, 0)
> 
> A\vec{B} · (A\vec{C} × A\vec{D}) = (2, 0, 0) · (12, 0, 0) = 24
> 
> Volumen = (1/6)|24| = 4 unidades³
> ```
> 
> 6. Problema aplicado: Una llave de 40 cm se usa en un tornillo. Se aplica una fuerza F = (0, 100, 50) N al extremo de la llave que está en posición r = (0.4, 0, 0) m desde el centro del tornillo.
>     
>     a) Calcular el torque b) ¿En qué dirección gira el tornillo? c) Magnitud del torque
>     
> 
> **Solución:**
> 
> ```
> a) τ⃗ = \vec{r} × \vec{F}
> 
>    τ⃗ = |i    j    k  |
>        |0.4  0    0  |
>        |0    100  50 |
> 
>      = i(0·50 - 0·100) - j(0.4·50 - 0·0) + k(0.4·100 - 0·0)
>      = i(0) - j(20) + k(40)
>      = (0, -20, 40) N·m
> 
> b) La componente principal es +Z (40 N·m)
>    El tornillo gira en sentido antihorario visto desde arriba
>    (regla de la mano derecha)
> 
> c) ||τ⃗|| = √(0² + 20² + 40²)
>          = √(400 + 1600)
>          = √2000
>          ≈ 44.7 N·m
> ```

## 💡 Consejos y Errores Comunes

> [!tip] 🧠 Estrategias de Aprendizaje **Para dominar el producto cruz:**
> 
> **1. Memorizar la fórmula del determinante:**
> 
> - Primera fila: i, j, k
> - Segunda fila: componentes de u
> - Tercera fila: componentes de v
> - ¡El signo de j es negativo!
> 
> **2. Regla de la mano derecha:**
> 
> - Practica con los vectores base
> - Visualiza la rotación
> - Verifica el sentido del resultado
> 
> **3. Verificación:**
> 
> - El resultado debe ser perpendicular a ambos vectores
> - Comprobar con producto punto: (u × v) · u = 0
> 
> **Errores comunes a evitar:**
> 
> ❌ **Error 1:** Olvidar el signo negativo en la componente j
> 
> ```
> u × v = i(...) - j(...) + k(...)  ✓
> u × v = i(...) + j(...) + k(...)  ✗
> ```
> 
> ❌ **Error 2:** Confundir el orden (no es conmutativo)
> 
> ```
> u × v ≠ v × u
> u × v = -(v × u)  ✓
> ```
> 
> ❌ **Error 3:** Creer que da un escalar
> 
> ```
> u × v = vector  ✓
> u · v = escalar  (eso es producto punto)
> ```
> 
> ❌ **Error 4:** Pensar que es asociativo
> 
> ```
> u × (v × w) ≠ (u × v) × w  (en general)
> ```
> 
> ❌ **Error 5:** Olvidar tomar valor absoluto en áreas/volúmenes
> 
> ```
> Área = ||u × v||  ✓ (siempre positiva)
> Área = u × v  ✗ (es un vector)
> ```
> 
> ❌ **Error 6:** Confundir producto triple escalar con vectorial
> 
> ```
> u · (v × w) = escalar  (volumen)
> u × (v × w) = vector  (triple producto vectorial)
> ```

## 📊 Tabla Resumen

> [!example] 📋 Compendio Completo
> 
> |Concepto|Fórmula|Resultado|Aplicación|
> |---|---|---|---|
> |**Producto cruz**|u × v|Vector ⊥ a u y v|Perpendicular|
> |**Determinante**|\|i j k; u₁ u₂ u₃; v₁ v₂ v₃\||(u₂v₃-u₃v₂, u₃v₁-u₁v₃, u₁v₂-u₂v₁)|Cálculo|
> |**Magnitud**|\|u × v\| = \|u\|v\|sen(θ)|Escalar ≥ 0|Área paralelogramo|
> |**Área triángulo**|½\|A\vec{B} × A\vec{C}\||Escalar|Geometría|
> |**Torque**|τ⃗ = \vec{r} × \vec{F}|Vector|Mecánica|
> |**Fuerza magnética**|\vec{F} = q(\vec{v} × \vec{B})|Vector|Electromagnetismo|
> |**Triple escalar**|u · (v × w)|Escalar|Volumen paralelepípedo|
> |**Volumen tetraedro**|(1/6)\|A\vec{B} · (A\vec{C} × A\vec{D})\||Escalar|Geometría 3D|
> |**Vectores paralelos**|u × v = 0|Vector cero|Colinealidad|
> |**Anticonmutativa**|u × v = -(v × u)|Propiedad|Álgebra|

## 🔗 Conexiones con el Sistema de Notas

> [!quote] 🌟 Enlaces Conceptuales **Prerequisites:**
> 
> - [[02 - Vectores en R3]] - Base fundamental
> - [[01 – Producto punto y ángulos]] - Operación complementaria
> - [[04 - Determinantes]] - Método de cálculo
> 
> **Temas siguientes:**
> 
> - [[03 – Aplicaciones geométricas básicas]] - Uso combinado
> - [[Rectas y Planos en R3]] - Ecuaciones vectoriales
> - [[Superficies en R3]] - Vectores normales
> 
> **Aplicaciones avanzadas:**
> 
> - [[Teorema de Stokes]] - Circulación y flujo
> - [[Teorema de la Divergencia]] - Flujo a través de superficies
> - [[Ecuaciones de Maxwell]] - Electromagnetismo
> 
> **Temas relacionados:**
> 
> - [[Momentum Angular]] - Mecánica rotacional
> - [[Campos Vectoriales]] - Rotacional
> - [[Geometría Diferencial]] - Formas diferenciales

---

**Tags:** #producto-cruz #producto-vectorial #área #torque #momento-angular #fuerza-magnética #producto-triple #volumen #vectores #R3 #geometría-vectorial #física-vectorial #determinante #regla-mano-derecha #university #matemáticas


# 🔍 Teorema de Rouché-Frobenius

## 🎯 Fundamentos del Teorema

> [!info]- 💡 Introducción al Teorema de Rouché-Frobenius El **Teorema de Rouché-Frobenius** es uno de los resultados fundamentales del álgebra lineal que establece las condiciones necesarias y suficientes para que un sistema de ecuaciones lineales tenga solución. Es la herramienta definitiva para determinar la **compatibilidad** de sistemas lineales.
> 
> **Analogías útiles:**
> 
> - **Detective de sistemas:** Determina si un caso (sistema) tiene solución o no
> - **Árbitro matemático:** Decide si las ecuaciones "juegan bien juntas"
> - **Diagnóstico médico:** Examina la salud de un sistema de ecuaciones
> - **Control de calidad:** Verifica si las restricciones son consistentes
> 
> **Importancia histórica:**
> 
> - **Eugène Rouché (1832-1910):** Matemático francés, trabajos en geometría y análisis
> - **Ferdinand Georg Frobenius (1849-1917):** Matemático alemán, contribuciones al álgebra
> - **Contexto:** Formalización del álgebra lineal en el siglo XIX
> - **Impacto:** Base para resolver sistemas en ingeniería, física, economía, computación
> 
> **¿Por qué es importante?**
> 
> - Determina existencia de soluciones sin resolverlas
> - Clasifica sistemas según su tipo de solución
> - Fundamental en teoría y aplicaciones del álgebra lineal
> - Base para métodos numéricos y algoritmos computacionales

### 📊 Conceptos Previos Esenciales

> [!note]- 🔑 Prerequisitos Necesarios
> 
> **1. Matriz de Coeficientes (A):**
> 
> Para el sistema Ax = b con m ecuaciones y n incógnitas:
> 
> $$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \ a_{21} & a_{22} & \cdots & a_{2n} \ \vdots & \vdots & \ddots & \vdots \ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$
> 
> **2. Matriz Ampliada o Aumentada (A|b):**
> 
> $$[A|b] = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} & | & b_1 \ a_{21} & a_{22} & \cdots & a_{2n} & | & b_2 \ \vdots & \vdots & \ddots & \vdots & | & \vdots \ a_{m1} & a_{m2} & \cdots & a_{mn} & | & b_m \end{pmatrix}$$
> 
> **3. Rango de una Matriz:**
> 
> El **rango** de una matriz A, denotado rg(A) o rk(A), es:
> 
> - El número máximo de filas linealmente independientes
> - El número máximo de columnas linealmente independientes
> - La dimensión del espacio generado por sus filas (o columnas)
> - El número de filas no nulas en su forma escalonada reducida
> 
> **Propiedades del rango:**
> 
> - 0 ≤ rg(A) ≤ min(m, n)
> - rg(A) = rg(Aᵀ)
> - rg(A) ≤ min(número de filas, número de columnas)
> - Si A es de m×n: rg(A) = m → filas LI (rango fila completo)
> - Si A es de m×n: rg(A) = n → columnas LI (rango columna completo)
> 
> **4. Formas de calcular el rango:**
> 
> a) **Reducción por filas (Gauss-Jordan):** Contar filas no nulas en forma escalonada
> 
> b) **Determinantes:** Orden del mayor menor no nulo
> 
> c) **Dimensión del espacio columna:** dim(Col(A))
> 
> **5. Sistema de ecuaciones lineales:**
> 
> Forma general: $$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \ \vdots \ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$
> 
> Forma matricial: **Ax = b**
> 
> **6. Tipos de sistemas según soluciones:**
> 
> - **Compatible Determinado (CD):** Una única solución
> - **Compatible Indeterminado (CI):** Infinitas soluciones
> - **Incompatible (I):** Sin solución
> 
> **7. Sistema homogéneo vs no homogéneo:**
> 
> - **Homogéneo:** Ax = 0 (siempre compatible, x = 0 es solución trivial)
> - **No homogéneo:** Ax = b (b ≠ 0)

## 📜 Enunciado del Teorema

### 🎓 Teorema de Rouché-Frobenius

> [!important]- ⭐ Enunciado Formal
> 
> Sea un sistema de ecuaciones lineales **Ax = b** con:
> 
> - A: matriz de coeficientes (m × n)
> - x: vector de incógnitas (n × 1)
> - b: vector de términos independientes (m × 1)
> - [A|b]: matriz ampliada (m × (n+1))
> 
> Entonces:
> 
> **1. COMPATIBILIDAD:**
> 
> El sistema es **compatible** (tiene solución) si y solo si:
> 
> $$\boxed{rg(A) = rg(A|b)}$$
> 
> **2. INCOMPATIBILIDAD:**
> 
> El sistema es **incompatible** (no tiene solución) si y solo si:
> 
> $$\boxed{rg(A) < rg(A|b)}$$
> 
> **3. TIPO DE SOLUCIÓN (para sistemas compatibles):**
> 
> Si rg(A) = rg(A|b) = r, entonces:
> 
> a) **Compatible Determinado:** Una única solución $$\boxed{r = n} \quad \text{(rango = número de incógnitas)}$$
> 
> b) **Compatible Indeterminado:** Infinitas soluciones $$\boxed{r < n} \quad \text{(rango < número de incógnitas)}$$
> 
> Con **n - r** grados de libertad (parámetros libres)
> 
> **RESUMEN EN TABLA:**
> 
> |Condición|Tipo de Sistema|Soluciones|Grados de Libertad|
> |---|---|---|---|
> |rg(A) < rg(A\|b)|Incompatible|0|-|
> |rg(A) = rg(A\|b) = n|Compatible Determinado|1|0|
> |rg(A) = rg(A\|b) = r < n|Compatible Indeterminado|∞|n - r|

### 🔍 Interpretación Geométrica

> [!tip]- 🌐 Visualización del Teorema
> 
> **Para sistemas 2×2 (dos ecuaciones, dos incógnitas):**
> 
> Cada ecuación representa una recta en el plano:
> 
> **1. Compatible Determinado (rg(A) = rg(A|b) = 2):**
> 
> ```
>      y
>      ↑
>      |     L₁: a₁x + b₁y = c₁
>      |    /
>      |   /
>      |  / ← Punto de intersección (solución única)
>      | /\
>      |/  \
>   ───┼────\──→ x
>      |     \ L₂: a₂x + b₂y = c₂
> ```
> 
> - Las rectas se cortan en un punto
> - Rectas no paralelas
> 
> **2. Compatible Indeterminado (rg(A) = rg(A|b) = 1 < 2):**
> 
> ```
>      y
>      ↑
>      |   L₁ y L₂ coinciden (misma recta)
>      |  /
>      | /
>      |/ ← Infinitos puntos de intersección
>   ───┼────────→ x
>      |
> ```
> 
> - Las rectas son la misma
> - Ecuaciones proporcionales
> - Infinitas soluciones sobre la recta
> 
> **3. Incompatible (rg(A) = 1 < rg(A|b) = 2):**
> 
> ```
>      y
>      ↑
>      |   L₁: ───────────
>      |
>      |   L₂: ───────────
>      |   ← Rectas paralelas, no se cortan
>   ───┼────────→ x
>      |
> ```
> 
> - Las rectas son paralelas
> - No hay punto de intersección
> - Sin solución
> 
> **Para sistemas 3×3 (tres ecuaciones, tres incógnitas):**
> 
> Cada ecuación representa un plano en el espacio:
> 
> **Compatible Determinado:**
> 
> - Los tres planos se cortan en un único punto
> 
> **Compatible Indeterminado:**
> 
> - Los planos se cortan en una recta (1 grado de libertad)
> - Los tres planos coinciden (2 grados de libertad)
> 
> **Incompatible:**
> 
> - No hay punto común a los tres planos
> - Ejemplos: tres planos paralelos, dos planos paralelos y el tercero los corta

## ✅ Ejemplos Resueltos Paso a Paso

### 📝 Nivel 1 - Sistemas Básicos

> [!example]- 🟢 Ejemplo 1: Compatible Determinado (Caso Más Simple)
> 
> **Sistema:** $$\begin{cases} x + y = 3 \ 2x - y = 0 \end{cases}$$
> 
> **Solución:**
> 
> **Paso 1:** Escribir en forma matricial Ax = b
> 
> $$A = \begin{pmatrix} 1 & 1 \ 2 & -1 \end{pmatrix}, \quad x = \begin{pmatrix} x \ y \end{pmatrix}, \quad b = \begin{pmatrix} 3 \ 0 \end{pmatrix}$$
> 
> **Paso 2:** Formar matriz ampliada [A|b]
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & | & 3 \ 2 & -1 & | & 0 \end{pmatrix}$$
> 
> **Paso 3:** Calcular rg(A)
> 
> Reducción por filas:
> 
> ```
> F₂ → F₂ - 2F₁
> 
> [1   1  ]     [1   1 ]
> [2  -1  ]  →  [0  -3 ]
> 
> Dos filas no nulas → rg(A) = 2
> ```
> 
> **Paso 4:** Calcular rg(A|b)
> 
> ```
> [1   1  | 3]     [1   1  | 3]
> [2  -1  | 0]  →  [0  -3  |-6]
> 
> Dos filas no nulas → rg(A|b) = 2
> ```
> 
> **Paso 5:** Aplicar Rouché-Frobenius
> 
> - rg(A) = 2
> - rg(A|b) = 2
> - n = 2 (dos incógnitas)
> 
> Como rg(A) = rg(A|b) = 2 = n:
> 
> ✅ **Sistema Compatible Determinado (solución única)**
> 
> **Paso 6:** Resolver el sistema
> 
> De la forma escalonada:
> 
> ```
> x + y = 3
> -3y = -6  →  y = 2
> 
> Sustituyendo: x + 2 = 3  →  x = 1
> ```
> 
> **Solución: (x, y) = (1, 2)**
> 
> Verificación:
> 
> - x + y = 1 + 2 = 3 ✓
> - 2x - y = 2(1) - 2 = 0 ✓

> [!example]- 🟢 Ejemplo 2: Sistema Incompatible
> 
> **Sistema:** $$\begin{cases} x + y = 1 \ x + y = 2 \end{cases}$$
> 
> **Solución:**
> 
> **Paso 1:** Matrices
> 
> $$A = \begin{pmatrix} 1 & 1 \ 1 & 1 \end{pmatrix}, \quad b = \begin{pmatrix} 1 \ 2 \end{pmatrix}$$
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & | & 1 \ 1 & 1 & | & 2 \end{pmatrix}$$
> 
> **Paso 2:** Calcular rg(A)
> 
> ```
> F₂ → F₂ - F₁
> 
> [1  1]     [1  1]
> [1  1]  →  [0  0]
> 
> Una fila no nula → rg(A) = 1
> ```
> 
> **Paso 3:** Calcular rg(A|b)
> 
> ```
> [1  1 | 1]     [1  1 | 1]
> [1  1 | 2]  →  [0  0 | 1]
>                    ↑
>                0 = 1 (contradicción!)
> 
> Dos filas no nulas → rg(A|b) = 2
> ```
> 
> **Paso 4:** Aplicar Rouché-Frobenius
> 
> - rg(A) = 1
> - rg(A|b) = 2
> 
> Como rg(A) < rg(A|b):
> 
> ❌ **Sistema Incompatible (sin solución)**
> 
> **Interpretación geométrica:**
> 
> - Ambas ecuaciones representan rectas paralelas (misma pendiente)
> - x + y = 1 es una recta
> - x + y = 2 es otra recta paralela desplazada
> - Nunca se cortan → sin solución

> [!example]- 🟢 Ejemplo 3: Compatible Indeterminado
> 
> **Sistema:** $$\begin{cases} x + 2y = 4 \ 2x + 4y = 8 \end{cases}$$
> 
> **Solución:**
> 
> **Paso 1:** Matrices
> 
> $$A = \begin{pmatrix} 1 & 2 \ 2 & 4 \end{pmatrix}, \quad b = \begin{pmatrix} 4 \ 8 \end{pmatrix}$$
> 
> $$[A|b] = \begin{pmatrix} 1 & 2 & | & 4 \ 2 & 4 & | & 8 \end{pmatrix}$$
> 
> **Paso 2:** Calcular rg(A)
> 
> ```
> F₂ → F₂ - 2F₁
> 
> [1  2]     [1  2]
> [2  4]  →  [0  0]
> 
> Una fila no nula → rg(A) = 1
> ```
> 
> **Paso 3:** Calcular rg(A|b)
> 
> ```
> [1  2 | 4]     [1  2 | 4]
> [2  4 | 8]  →  [0  0 | 0]
>                    ↑
>                 0 = 0 (identidad!)
> 
> Una fila no nula → rg(A|b) = 1
> ```
> 
> **Paso 4:** Aplicar Rouché-Frobenius
> 
> - rg(A) = 1
> - rg(A|b) = 1
> - n = 2 (dos incógnitas)
> 
> Como rg(A) = rg(A|b) = 1 < 2 = n:
> 
> ✅ **Sistema Compatible Indeterminado (infinitas soluciones)**
> 
> **Grados de libertad:** n - r = 2 - 1 = 1 parámetro
> 
> **Paso 5:** Expresar soluciones
> 
> De x + 2y = 4:
> 
> $$x = 4 - 2y$$
> 
> Haciendo y = λ (parámetro libre):
> 
> $$\boxed{\begin{cases} x = 4 - 2\lambda \ y = \lambda \end{cases}, \quad \lambda \in \mathbb{R}}$$
> 
> O en forma vectorial:
> 
> $$\begin{pmatrix} x \ y \end{pmatrix} = \begin{pmatrix} 4 \ 0 \end{pmatrix} + \lambda \begin{pmatrix} -2 \ 1 \end{pmatrix}$$
> 
> **Interpretación:** La solución es una recta en el plano
> 
> **Verificación con algunos valores:**
> 
> - λ = 0: (x,y) = (4, 0) → 4 + 2(0) = 4 ✓
> - λ = 1: (x,y) = (2, 1) → 2 + 2(1) = 4 ✓
> - λ = 2: (x,y) = (0, 2) → 0 + 2(2) = 4 ✓

### 📝 Nivel 2 - Sistemas 3×3

> [!example]- 🟡 Ejemplo 4: Sistema 3×3 Compatible Determinado
> 
> **Sistema:** $$\begin{cases} x + y + z = 6 \ 2x - y + z = 3 \ x + 2y - z = 1 \end{cases}$$
> 
> **Solución:**
> 
> **Paso 1:** Matriz ampliada
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 6 \ 2 & -1 & 1 & | & 3 \ 1 & 2 & -1 & | & 1 \end{pmatrix}$$
> 
> **Paso 2:** Reducción por filas (Gauss-Jordan)
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - F₁
> 
> [1   1   1 | 6]     [1   1   1 | 6]
> [2  -1   1 | 3]  →  [0  -3  -1 |-9]
> [1   2  -1 | 1]     [0   1  -2 |-5]
> ```
> 
> ```
> F₃ → F₃ + (1/3)F₂
> 
> [1   1   1 | 6]
> [0  -3  -1 |-9]
> [0   0  -7/3|-8]
> ```
> 
> **Paso 3:** Calcular rangos
> 
> Para A:
> 
> ```
> [1   1   1]
> [0  -3  -1]
> [0   0 -7/3]
> 
> Tres filas no nulas → rg(A) = 3
> ```
> 
> Para [A|b]: Tres filas no nulas → rg(A|b) = 3
> 
> **Paso 4:** Aplicar teorema
> 
> - rg(A) = 3
> - rg(A|b) = 3
> - n = 3
> 
> Como rg(A) = rg(A|b) = n = 3:
> 
> ✅ **Sistema Compatible Determinado**
> 
> **Paso 5:** Resolver por sustitución regresiva
> 
> ```
> -7z/3 = -8  →  z = 24/7
> 
> -3y - (24/7) = -9
> -3y = -9 + 24/7 = -39/7
> y = 13/7
> 
> x + 13/7 + 24/7 = 6
> x = 6 - 37/7 = 5/7
> ```
> 
> **Solución: (x, y, z) = (5/7, 13/7, 24/7)**

> [!example]- 🟡 Ejemplo 5: Sistema 3×3 Compatible Indeterminado
> 
> **Sistema:** $$\begin{cases} x + y + z = 1 \ 2x + 2y + 2z = 2 \ 3x + 3y + 3z = 3 \end{cases}$$
> 
> **Solución:**
> 
> **Paso 1:** Matriz ampliada
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 1 \ 2 & 2 & 2 & | & 2 \ 3 & 3 & 3 & | & 3 \end{pmatrix}$$
> 
> **Paso 2:** Reducción
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - 3F₁
> 
> [1  1  1 | 1]     [1  1  1 | 1]
> [2  2  2 | 2]  →  [0  0  0 | 0]
> [3  3  3 | 3]     [0  0  0 | 0]
> ```
> 
> **Paso 3:** Rangos
> 
> - rg(A) = 1 (una fila no nula)
> - rg(A|b) = 1 (una fila no nula)
> - n = 3
> 
> **Paso 4:** Clasificación
> 
> Como rg(A) = rg(A|b) = 1 < 3 = n:
> 
> ✅ **Compatible Indeterminado**
> 
> **Grados de libertad:** 3 - 1 = 2 parámetros
> 
> **Paso 5:** Solución general
> 
> De x + y + z = 1:
> 
> $$x = 1 - y - z$$
> 
> Haciendo y = λ, z = μ:
> 
> $$\boxed{\begin{cases} x = 1 - \lambda - \mu \ y = \lambda \ z = \mu \end{cases}, \quad \lambda, \mu \in \mathbb{R}}$$
> 
> Forma vectorial:
> 
> $$\begin{pmatrix} x \ y \ z \end{pmatrix} = \begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix} + \lambda \begin{pmatrix} -1 \ 1 \ 0 \end{pmatrix} + \mu \begin{pmatrix} -1 \ 0 \ 1 \end{pmatrix}$$
> 
> **Interpretación:** La solución es un plano en ℝ³

> [!example]- 🟡 Ejemplo 6: Sistema 3×3 Incompatible
> 
> **Sistema:** $$\begin{cases} x + y + z = 1 \ 2x + 2y + 2z = 2 \ 3x + 3y + 3z = 5 \end{cases}$$
> 
> **Solución:**
> 
> **Paso 1:** Matriz ampliada
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 1 \ 2 & 2 & 2 & | & 2 \ 3 & 3 & 3 & | & 5 \end{pmatrix}$$
> 
> **Paso 2:** Reducción
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - 3F₁
> 
> [1  1  1 | 1]     [1  1  1 | 1]
> [2  2  2 | 2]  →  [0  0  0 | 0]
> [3  3  3 | 5]     [0  0  0 | 2]
>                              ↑
>                          0 = 2 (contradicción!)
> ```
> 
> **Paso 3:** Rangos
> 
> Para A:
> 
> ```
> [1  1  1]
> [0  0  0]
> [0  0  0]
> 
> rg(A) = 1
> ```
> 
> Para [A|b]:
> 
> ```
> [1  1  1 | 1]
> [0  0  0 | 0]
> [0  0  0 | 2]
> 
> rg(A|b) = 2 (dos filas no nulas)
> ```
> 
> **Paso 4:** Clasificación
> 
> Como rg(A) = 1 < rg(A|b) = 2:
> 
> ❌ **Sistema Incompatible (sin solución)**
> 
> **Interpretación:**
> 
> - Las primeras dos ecuaciones definen el mismo plano
> - La tercera ecuación define un plano paralelo
> - Los planos nunca se intersectan

### 📝 Nivel 3 - Sistemas con Parámetros

> [!example]- 🔴 Ejemplo 7: Sistema con Parámetro
> 
> **Sistema (con parámetro a):** $$\begin{cases} x + y + z = 1 \ x + 2y + 3z = 2 \ x + 3y + az = 3 \end{cases}$$
> 
> **Objetivo:** Discutir según valores de a
> 
> **Solución:**
> 
> **Paso 1:** Matriz ampliada
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 1 \ 1 & 2 & 3 & | & 2 \ 1 & 3 & a & | & 3 \end{pmatrix}$$
> 
> **Paso 2:** Reducción (con a como parámetro)
> 
> ```
> F₂ → F₂ - F₁
> F₃ → F₃ - F₁
> 
> [1  1  1  | 1]     [1  1   1  | 1]
> [1  2  3  | 2]  →  [0  1   2  | 1]
> [1  3  a  | 3]     [0  2  a-1 | 2]
> ```
> 
> ```
> F₃ → F₃ - 2F₂
> 
> [1  1   1  | 1]
> [0  1   2  | 1]
> [0  0  a-5 | 0]
> ```
> 
> **Paso 3:** Análisis por casos
> 
> **CASO 1: a ≠ 5**
> 
> La tercera fila es no nula: (a-5)z = 0
> 
> - rg(A) = 3
> - rg(A|b) = 3
> - n = 3
> 
> Como rg(A) = rg(A|b) = n:
> 
> ✅ **Sistema Compatible Determinado**
> 
> Solución:
> 
> ```
> (a-5)z = 0  →  z = 0
> y + 2(0) = 1  →  y = 1
> x + 1 + 0 = 1  →  x = 0
> ```
> 
> **Solución única: (x, y, z) = (0, 1, 0)** para todo a ≠ 5
> 
> **CASO 2: a = 5**
> 
> Sustituyendo a = 5:
> 
> ```
> [1  1  1 | 1]
> [0  1  2 | 1]
> [0  0  0 | 0]
> ```
> 
> - rg(A) = 2
> - rg(A|b) = 2
> - n = 3
> 
> Como rg(A) = rg(A|b) = 2 < 3 = n:
> ✅ **Sistema Compatible Indeterminado**
> 
> **Grados de libertad:** 3 - 2 = 1 parámetro
> 
> Solución:
> 
> ```
> De la segunda ecuación: y + 2z = 1  →  y = 1 - 2z
> De la primera: x + (1-2z) + z = 1  →  x = z
> ```
> 
> Haciendo z = λ:
> 
> $$\boxed{\begin{cases} x = \lambda \ y = 1 - 2\lambda \ z = \lambda \end{cases}, \quad \lambda \in \mathbb{R}}$$
> 
> **RESUMEN:**
> 
> |Valor de a|Tipo de Sistema|Solución|
> |---|---|---|
> |a ≠ 5|Compatible Determinado|(0, 1, 0)|
> |a = 5|Compatible Indeterminado|(λ, 1-2λ, λ)|

> [!example]- 🔴 Ejemplo 8: Sistema con Dos Parámetros
> 
> **Sistema:** $$\begin{cases} x + y + z = a \ x + 2y + 4z = b \ 2x + 3y + 5z = 3 \end{cases}$$
> 
> **Objetivo:** Determinar valores de a y b para que el sistema sea compatible
> 
> **Solución:**
> 
> **Paso 1:** Matriz ampliada
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & a \ 1 & 2 & 4 & | & b \ 2 & 3 & 5 & | & 3 \end{pmatrix}$$
> 
> **Paso 2:** Reducción
> 
> ```
> F₂ → F₂ - F₁
> F₃ → F₃ - 2F₁
> 
> [1  1  1 | a  ]     [1  1  1  | a    ]
> [1  2  4 | b  ]  →  [0  1  3  | b-a  ]
> [2  3  5 | 3  ]     [0  1  3  | 3-2a ]
> ```
> 
> ```
> F₃ → F₃ - F₂
> 
> [1  1  1 | a      ]
> [0  1  3 | b-a    ]
> [0  0  0 | 3-2a-b+a]
> 
> [1  1  1 | a    ]
> [0  1  3 | b-a  ]
> [0  0  0 | 3-a-b]
> ```
> 
> **Paso 3:** Análisis
> 
> Matriz de coeficientes A reducida:
> 
> ```
> [1  1  1]
> [0  1  3]
> [0  0  0]
> 
> rg(A) = 2 (siempre, independiente de a y b)
> ```
> 
> Para rg(A|b):
> 
> - Si la tercera fila es toda ceros: rg(A|b) = 2
> - Si la tercera fila tiene elemento no nulo: rg(A|b) = 3
> 
> **Condición de compatibilidad:**
> 
> El sistema es compatible ⟺ rg(A) = rg(A|b)
> 
> Esto ocurre cuando: 3 - a - b = 0
> 
> $$\boxed{a + b = 3}$$
> 
> **CONCLUSIÓN:**
> 
> - **Si a + b = 3:** Sistema Compatible Indeterminado
>     - rg(A) = rg(A|b) = 2 < 3
>     - Infinitas soluciones con 1 parámetro libre
> - **Si a + b ≠ 3:** Sistema Incompatible
>     - rg(A) = 2 < rg(A|b) = 3
>     - Sin solución
> 
> **Ejemplo numérico:**
> 
> Si a = 1, b = 2 (cumple a + b = 3):
> 
> ```
> [1  1  1 | 1]
> [0  1  3 | 1]
> [0  0  0 | 0]
> 
> De la segunda: y + 3z = 1  →  y = 1 - 3z
> De la primera: x + (1-3z) + z = 1  →  x = 2z
> 
> Solución: (x,y,z) = (2λ, 1-3λ, λ), λ ∈ ℝ
> ```

> [!example]- 🔴 Ejemplo 9: Discusión Completa con Parámetro
> 
> **Sistema:** $$\begin{cases} x + y + z = 1 \ 2x + ay + 2z = 3 \ x + y + az = 2 \end{cases}$$
> 
> **Objetivo:** Discusión completa según valores de a
> 
> **Solución:**
> 
> **Paso 1:** Matriz ampliada
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 1 \ 2 & a & 2 & | & 3 \ 1 & 1 & a & | & 2 \end{pmatrix}$$
> 
> **Paso 2:** Reducción
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - F₁
> 
> [1  1   1  | 1]     [1  1   1   | 1]
> [2  a   2  | 3]  →  [0  a-2  0  | 1]
> [1  1   a  | 2]     [0  0   a-1 | 1]
> ```
> 
> **Paso 3:** Análisis por casos
> 
> **CASO 1: a ≠ 1 y a ≠ 2**
> 
> Todas las filas son no nulas:
> 
> - rg(A) = 3
> - rg(A|b) = 3
> - n = 3
> 
> ✅ **Sistema Compatible Determinado (solución única)**
> 
> Resolución:
> 
> ```
> (a-1)z = 1  →  z = 1/(a-1)
> (a-2)y = 1  →  y = 1/(a-2)
> x + 1/(a-2) + 1/(a-1) = 1
> ```
> 
> $$\boxed{x = 1 - \frac{1}{a-2} - \frac{1}{a-1}}$$
> 
> **CASO 2: a = 1**
> 
> Sustituyendo:
> 
> ```
> [1  1  1 | 1]
> [0 -1  0 | 1]
> [0  0  0 | 1]
>           ↑
>        0 = 1 (contradicción!)
> ```
> 
> - rg(A) = 2
> - rg(A|b) = 3
> 
> ❌ **Sistema Incompatible (sin solución)**
> 
> **CASO 3: a = 2**
> 
> Sustituyendo:
> 
> ```
> [1  1  1 | 1]
> [0  0  0 | 1]
>           ↑
>        0 = 1 (contradicción!)
> [0  0  1 | 1]
> ```
> 
> También se puede ver que la segunda fila da contradicción directamente.
> 
> - rg(A) < rg(A|b)
> 
> ❌ **Sistema Incompatible (sin solución)**
> 
> **TABLA RESUMEN:**
> 
> |Valor de a|Tipo|Soluciones|Observaciones|
> |---|---|---|---|
> |a ≠ 1, a ≠ 2|Compatible Det.|1|Solución explícita|
> |a = 1|Incompatible|0|Contradicción en F₃|
> |a = 2|Incompatible|0|Contradicción en F₂|

## 🔧 Métodos de Cálculo del Rango

### 📐 Método 1: Reducción por Filas (Gauss-Jordan)

> [!note]- 🔨 Método de Eliminación Gaussiana
> 
> **Procedimiento:**
> 
> 1. **Aplicar operaciones elementales** hasta obtener forma escalonada
> 2. **Contar filas no nulas** en la forma escalonada
> 3. Ese número es el rango
> 
> **Operaciones elementales permitidas:**
> 
> - **F_i ↔ F_j:** Intercambiar filas i y j
> - **F_i → k·F_i:** Multiplicar fila i por k ≠ 0
> - **F_i → F_i + k·F_j:** Sumar a la fila i un múltiplo de la fila j
> 
> **Ejemplo detallado:**
> 
> $$A = \begin{pmatrix} 1 & 2 & 3 & 4 \ 2 & 4 & 6 & 8 \ 1 & 1 & 1 & 2 \end{pmatrix}$$
> 
> **Paso a paso:**
> 
> ```
> Matriz original:
> [1  2  3  4]
> [2  4  6  8]
> [1  1  1  2]
> 
> F₂ → F₂ - 2F₁:
> [1  2  3  4]
> [0  0  0  0]  ← Fila de ceros
> [1  1  1  2]
> 
> F₃ → F₃ - F₁:
> [1  2  3  4]
> [0  0  0  0]
> [0 -1 -2 -2]
> 
> F₂ ↔ F₃ (opcional, para mejor visualización):
> [1  2  3  4]
> [0 -1 -2 -2]
> [0  0  0  0]
> 
> Forma escalonada final.
> Filas no nulas: 2
> ```
> 
> **Conclusión:** rg(A) = 2
> 
> **Ventajas:**
> 
> - Método sistemático y algorítmico
> - Funciona para cualquier matriz
> - El mismo proceso sirve para resolver el sistema
> 
> **Desventajas:**
> 
> - Puede ser laborioso para matrices grandes
> - Requiere cuidado con los cálculos

### 📐 Método 2: Determinantes (Menores)

> [!note]- 🔢 Método de los Menores
> 
> **Definición:** El rango de A es el orden del mayor menor no nulo
> 
> **Menor de orden k:** Determinante de una submatriz k×k
> 
> **Procedimiento:**
> 
> 1. Calcular determinantes de submatrices de orden máximo posible
> 2. Si alguno es ≠ 0, ese es el rango
> 3. Si todos son cero, probar con orden menor
> 4. Continuar hasta encontrar un menor no nulo
> 
> **Ejemplo:**
> 
> $$A = \begin{pmatrix} 1 & 2 & 3 \ 2 & 4 & 6 \ 1 & 3 & 5 \end{pmatrix}$$
> 
> **Paso 1:** Probar determinante de orden 3
> 
> $$\det(A) = \begin{vmatrix} 1 & 2 & 3 \ 2 & 4 & 6 \ 1 & 3 & 5 \end{vmatrix}$$
> 
> Por Sarrus o cofactores:
> 
> ```
> "= 1(4(5) - 6(3)) - 2(2(5) - 6(1)) + 3(2(3) - 4(1))"
> "= 1(20 - 18) - 2(10 - 6) + 3(6 - 4)"
> "= 2 - 8 + 6"
> "= 0"
> ```
> 
> Como det(A) = 0, rg(A) < 3
> 
> **Paso 2:** Probar menores de orden 2
> 
> $$\begin{vmatrix} 1 & 2 \ 2 & 4 \end{vmatrix} = 4 - 4 = 0$$
> 
> $$\begin{vmatrix} 1 & 3 \ 2 & 6 \end{vmatrix} = 6 - 6 = 0$$
> 
> $$\begin{vmatrix} 1 & 2 \ 1 & 3 \end{vmatrix} = 3 - 2 = 1 \neq 0$$ ✓
> 
> **Conclusión:** rg(A) = 2
> 
> **Ventajas:**
> 
> - Definición teórica precisa
> - Útil para matrices pequeñas
> 
> **Desventajas:**
> 
> - Muy laborioso para matrices grandes
> - Muchos determinantes para calcular

### 📐 Método 3: Usando Propiedades

> [!tip]- ⚡ Atajos y Propiedades Útiles
> 
> **Propiedades del rango:**
> 
> **1. Filas/columnas proporcionales:**
> 
> Si una fila es múltiplo de otra, no aumenta el rango
> 
> $$A = \begin{pmatrix} 1 & 2 & 3 \ 2 & 4 & 6 \end{pmatrix}$$
> 
> F₂ = 2F₁ → rg(A) = 1
> 
> **2. Filas/columnas de ceros:**
> 
> No contribuyen al rango
> 
> $$A = \begin{pmatrix} 1 & 2 \ 0 & 0 \ 3 & 4 \end{pmatrix}$$
> 
> rg(A) = 2 (ignorar fila de ceros)
> 
> **3. Matriz escalonada:**
> 
> El rango = número de pivotes (filas con primer elemento no nulo)
> 
> $$A = \begin{pmatrix} 2 & 1 & 3 \ 0 & 4 & 2 \ 0 & 0 & 5 \end{pmatrix}$$
> 
> Tres pivotes → rg(A) = 3
> 
> **4. Submatrices:**
> 
> - rg(A) ≥ rg(submatriz de A)
> - Si una submatriz k×k tiene determinante ≠ 0, entonces rg(A) ≥ k
> 
> **5. Operaciones elementales:**
> 
> No cambian el rango de la matriz
> 
> **6. Transpuesta:**
> 
> rg(A) = rg(Aᵀ)
> 
> **7. Producto:**
> 
> rg(AB) ≤ min{rg(A), rg(B)}
> 
> **8. Suma:**
> 
> rg(A + B) ≤ rg(A) + rg(B)

## 🧪 Ejercicios Progresivos

### 📝 Nivel 1 - Ejercicios Básicos

> [!example]- 🟢 Práctica Inicial
> 
> **Ejercicio 1:** Clasifique el siguiente sistema usando Rouché-Frobenius: $$\begin{cases} x + 2y = 5 \ 2x + 4y = 10 \end{cases}$$
> 
> ---
> 
> **Ejercicio 2:** Determine el rango de la matriz: $$A = \begin{pmatrix} 1 & 2 & 3 \ 2 & 4 & 6 \ 1 & 1 & 1 \end{pmatrix}$$
> 
> ---
> 
> **Ejercicio 3:** Demuestre que el siguiente sistema es incompatible: $$\begin{cases} x - y = 1 \ 2x - 2y = 5 \end{cases}$$
> 
> ---
> 
> **Ejercicio 4:** Clasifique el sistema: $$\begin{cases} x + y + z = 6 \ 2x + 2y + 2z = 12 \ x + y + z = 6 \end{cases}$$
> 
> ---
> 
> **Ejercicio 5:** Calcule rg(A) y rg(A|b) para: $$\begin{cases} x + y = 1 \ 2x + 2y = 3 \end{cases}$$
> 
> ---
> 
> **Ejercicio 6:** Si det(A) = 0 para una matriz cuadrada 3×3, ¿puede el sistema Ax = b ser Compatible Determinado? Justifique.
> 
> ---
> 
> **Ejercicio 7:** Clasifique según el número de soluciones: $$\begin{cases} 3x + 6y = 9 \ x + 2y = 3 \end{cases}$$
> 
> ---
> 
> **Ejercicio 8:** Determine el rango de: $$B = \begin{pmatrix} 1 & 0 & 0 \ 0 & 2 & 0 \ 0 & 0 & 3 \end{pmatrix}$$
> 
> ---
> 
> **Ejercicio 9:** ¿Es posible que un sistema homogéneo Ax = 0 sea incompatible? Justifique.
> 
> ---
> 
> **Ejercicio 10:** Clasifique: $$\begin{cases} x + y + z = 0 \ 2x + 2y + 2z = 0 \end{cases}$$

### 📝 Nivel 2 - Ejercicios Intermedios

> [!example]- 🟡 Práctica Intermedia
> 
> **Ejercicio 11:** Clasifique y resuelva si es posible: $$\begin{cases} x + 2y - z = 4 \ 2x + 5y + z = 13 \ 3x + 7y = 17 \end{cases}$$
> 
> ---
> 
> **Ejercicio 12:** Determine k para que el sistema tenga infinitas soluciones: $$\begin{cases} x + y = 2 \ 2x + 2y = k \end{cases}$$
> 
> ---
> 
> **Ejercicio 13:** Clasifique según el valor de a: $$\begin{cases} x + y = 1 \ 2x + 2y = a \end{cases}$$
> 
> ---
> 
> **Ejercicio 14:** Resuelva el sistema usando Rouché-Frobenius: $$\begin{cases} 2x + y - z = 3 \ x - 2y + z = -3 \ 3x - y = 0 \end{cases}$$
> 
> ---
> 
> **Ejercicio 15:** Clasifique el sistema rectangular (más ecuaciones que incógnitas): $$\begin{cases} x + y = 3 \ 2x - y = 0 \ x + 3y = 7 \end{cases}$$
> 
> ---
> 
> **Ejercicio 16:** Determine todos los valores de a y b para que el sistema sea compatible: $$\begin{cases} x + y = 1 \ 2x + 2y = a \ 3x + 3y = b \end{cases}$$
> 
> ---
> 
> **Ejercicio 17:** Calcule el rango usando determinantes: $$C = \begin{pmatrix} 1 & 2 & 3 \ 2 & 4 & 7 \ 3 & 6 & 10 \end{pmatrix}$$
> 
> ---
> 
> **Ejercicio 18:** Para qué valores de m el sistema tiene solución única: $$\begin{cases} x + 2y + z = 1 \ 2x + 3y + mz = 2 \ x + y + 3z = m \end{cases}$$
> 
> ---
> 
> **Ejercicio 19:** Clasifique el sistema: $$\begin{cases} x + y + z = 1 \ 2x + 3y + 4z = 3 \ 3x + 4y + 5z = 4 \end{cases}$$
> 
> ---
> 
> **Ejercicio 20:** Si rg(A) = 2, rg(A|b) = 2 y n = 4, ¿cuántos grados de libertad tiene el sistema?

### 📝 Nivel 3 - Ejercicios Avanzados

> [!example]- 🔴 Práctica Avanzada
> 
> **Ejercicio 21:** Discusión completa según a y b: $$\begin{cases} x + y + az = 1 \ x + ay + z = 1 \ ax + y + z = b \end{cases}$$
> 
> ---
> 
> **Ejercicio 22:** Discuta según el valor de λ: $$\begin{cases} x + y + z = 1 \ x + 2y + 3z = 2 \ x + 3y + \lambda z = 3 \end{cases}$$
> 
> ---
> 
> **Ejercicio 23:** Determine a, b, c para que el sistema sea compatible: $$\begin{cases} x + y + z = 1 \ 2x + 2y + 2z = a \ 3x + 3y + 3z = b \ 4x + 4y + 4z = c \end{cases}$$
> 
> ---
> 
> **Ejercicio 24:** Clasifique el sistema según α y β: $$\begin{cases} x + y + z = α \ 2x + 3y + 4z = 3 \ 3x + 4y + 5z = β \end{cases}$$
> 
> ---
> 
> **Ejercicio 25:** Demuestre: Si A es invertible (n×n), entonces Ax = b siempre tiene solución única.
> 
> ---
> 
> **Ejercicio 26:** Determine k y m para que el sistema tenga exactamente 2 grados de libertad: $$\begin{cases} x + y + z + w = 1 \ 2x + 2y + 2z + 2w = k \ 3x + 3y + 3z + 3w = m \end{cases}$$
> 
> ---
> 
> **Ejercicio 27:** Discuta completamente según p: $$\begin{cases} x + py + z = 1 \ px + y + z = p \ x + y + pz = p^2 \end{cases}$$
> 
> ---
> 
> **Ejercicio 28:** Sea A una matriz m×n con rg(A) = r. Si Ax = b tiene solución, ¿cuál es el mínimo número de parámetros libres?
> 
> ---
> 
> **Ejercicio 29:** Encuentre condiciones sobre a, b, c para que el sistema: $$\begin{cases} x + 2y + 3z = a \ 2x + 4y + 6z = b \ x + 2y + 3z = c \end{cases}$$ sea compatible.
> 
> ---
> 
> **Ejercicio 30:** Problema aplicado: En un circuito eléctrico con tres mallas, las corrientes i₁, i₂, i₃ satisfacen: $$\begin{cases} 2i_1 - i_2 = 4 \ -i_1 + 3i_2 - i_3 = 0 \ -i_2 + 2i_3 = -2 \end{cases}$$ a) Clasifique el sistema b) Determine las corrientes

## 💡 Soluciones de Ejercicios Seleccionados

### 🔍 Soluciones Nivel 1

> [!success]- ✅ Soluciones Ejercicios Básicos
> 
> **Solución Ejercicio 1:**
> 
> $$[A|b] = \begin{pmatrix} 1 & 2 & | & 5 \ 2 & 4 & | & 10 \end{pmatrix}$$
> 
> F₂ → F₂ - 2F₁: $$\begin{pmatrix} 1 & 2 & | & 5 \ 0 & 0 & | & 0 \end{pmatrix}$$
> 
> - rg(A) = 1
> - rg(A|b) = 1
> - n = 2
> 
> Como rg(A) = rg(A|b) = 1 < 2: **Compatible Indeterminado** con 1 grado de libertad
> 
> Solución: x = 5 - 2λ, y = λ
> 
> ---
> 
> **Solución Ejercicio 2:**
> 
> Reducción por filas:
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - F₁
> 
> [1  2  3]     [1  2  3]
> [2  4  6]  →  [0  0  0]
> [1  1  1]     [0 -1 -2]
> ```
> 
> Dos filas no nulas → **rg(A) = 2**
> 
> ---
> 
> **Solución Ejercicio 3:**
> 
> $$[A|b] = \begin{pmatrix} 1 & -1 & | & 1 \ 2 & -2 & | & 5 \end{pmatrix}$$
> 
> F₂ → F₂ - 2F₁: $$\begin{pmatrix} 1 & -1 & | & 1 \ 0 & 0 & | & 3 \end{pmatrix}$$
> 
> La última fila representa: 0 = 3 (contradicción)
> 
> - rg(A) = 1
> - rg(A|b) = 2
> 
> Como rg(A) < rg(A|b): **Sistema Incompatible**
> 
> ---
> 
> **Solución Ejercicio 5:**
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & | & 1 \ 2 & 2 & | & 3 \end{pmatrix}$$
> 
> F₂ → F₂ - 2F₁: $$\begin{pmatrix} 1 & 1 & | & 1 \ 0 & 0 & | & 1 \end{pmatrix}$$
> 
> - **rg(A) = 1**
> - **rg(A|b) = 2**
> 
> Sistema Incompatible
> 
> ---
> 
> **Solución Ejercicio 6:**
> 
> **No**, no puede ser Compatible Determinado.
> 
> **Justificación:**
> 
> - Si det(A) = 0 → rg(A) < 3
> - Para Compatible Determinado necesitamos: rg(A) = n = 3
> - Por tanto, es imposible
> 
> Si det(A) = 0, el sistema solo puede ser:
> 
> - Incompatible, o
> - Compatible Indeterminado
> 
> ---
> 
> **Solución Ejercicio 8:**
> 
> A es una matriz diagonal con elementos no nulos en la diagonal.
> 
> Una matriz diagonal con todos los elementos diagonales ≠ 0 tiene rango completo.
> 
> **rg(B) = 3**
> 
> ---
> 
> **Solución Ejercicio 9:**
> 
> **No**, un sistema homogéneo NUNCA es incompatible.
> 
> **Demostración:** Para Ax = 0, el vector x = 0 siempre es solución (solución trivial).
> 
> Por tanto, el sistema siempre tiene al menos una solución.
> 
> Por Rouché-Frobenius: rg(A) = rg(A|0) siempre, ya que agregar una columna de ceros no aumenta el rango.
> 
> **Conclusión:** Los sistemas homogéneos siempre son compatibles.
> 
> ---
> 
> **Solución Ejercicio 10:**
> 
> Las dos ecuaciones son proporcionales (la segunda es el doble de la primera).
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 0 \ 2 & 2 & 2 & | & 0 \end{pmatrix}$$
> 
> Reduciendo: $$\begin{pmatrix} 1 & 1 & 1 & | & 0 \ 0 & 0 & 0 & | & 0 \end{pmatrix}$$
> 
> - rg(A) = 1
> - rg(A|b) = 1
> - n = 3
> 
> **Compatible Indeterminado** con n - r = 3 - 1 = 2 grados de libertad

### 🔍 Soluciones Nivel 2

> [!success]- ✅ Soluciones Ejercicios Intermedios
> 
> **Solución Ejercicio 11:**
> 
> $$[A|b] = \begin{pmatrix} 1 & 2 & -1 & | & 4 \ 2 & 5 & 1 & | & 13 \ 3 & 7 & 0 & | & 17 \end{pmatrix}$$
> 
> Reducción:
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - 3F₁
> 
> [1  2 -1 |  4]
> [0  1  3 |  5]
> [0  1  3 |  5]
> 
> F₃ → F₃ - F₂
> 
> [1  2 -1 |  4]
> [0  1  3 |  5]
> [0  0  0 |  0]
> ```
> 
> - rg(A) = 2, rg(A|b) = 2, n = 3
> 
> **Compatible Indeterminado** (1 grado de libertad)
> 
> Solución:
> 
> ```
> y + 3z = 5  →  y = 5 - 3z
> x + 2(5-3z) - z = 4  →  x = -6 + 7z
> ```
> 
> Con z = λ: $$\boxed{(x,y,z) = (-6+7\lambda, 5-3\lambda, \lambda)}$$
> 
> ---
> 
> **Solución Ejercicio 12:**
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & | & 2 \ 2 & 2 & | & k \end{pmatrix}$$
> 
> F₂ → F₂ - 2F₁: $$\begin{pmatrix} 1 & 1 & | & 2 \ 0 & 0 & | & k-4 \end{pmatrix}$$
> 
> Para infinitas soluciones: rg(A) = rg(A|b) < n
> 
> Necesitamos k - 4 = 0
> 
> **k = 4**
> 
> ---
> 
> **Solución Ejercicio 13:**
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & | & 1 \ 2 & 2 & | & a \end{pmatrix}$$
> 
> F₂ → F₂ - 2F₁: $$\begin{pmatrix} 1 & 1 & | & 1 \ 0 & 0 & | & a-2 \end{pmatrix}$$
> 
> **Clasificación:**
> 
> - **Si a = 2:** rg(A) = rg(A|b) = 1 < 2 → **Compatible Indeterminado**
> - **Si a ≠ 2:** rg(A) = 1 < rg(A|b) = 2 → **Incompatible**
> 
> ---
> 
> **Solución Ejercicio 16:**
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & | & 1 \ 2 & 2 & | & a \ 3 & 3 & | & b \end{pmatrix}$$
> 
> Reducción:
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - 3F₁
> 
> [1  1 | 1  ]
> [0  0 | a-2]
> [0  0 | b-3]
> ```
> 
> Para que sea compatible: rg(A) = rg(A|b)
> 
> rg(A) = 1 siempre
> 
> Para que rg(A|b) = 1, necesitamos que F₂ y F₃ sean ceros:
> 
> **Condiciones:**
> 
> - a - 2 = 0 → a = 2
> - b - 3 = 0 → b = 3
> 
> **Respuesta: a = 2 y b = 3**
> 
> ---
> 
> **Solución Ejercicio 20:**
> 
> Datos:
> 
> - rg(A) = 2
> - rg(A|b) = 2
> - n = 4
> 
> Como rg(A) = rg(A|b): Sistema compatible
> 
> Grados de libertad = n - rg(A) = 4 - 2 = **2 parámetros libres**

### 🔍 Soluciones Nivel 3

> [!success]- ✅ Soluciones Ejercicios Avanzados
> 
> **Solución Ejercicio 22:**
> 
> $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 1 \ 1 & 2 & 3 & | & 2 \ 1 & 3 & \lambda & | & 3 \end{pmatrix}$$
> 
> Reducción:
> 
> ```
> F₂ → F₂ - F₁
> F₃ → F₃ - F₁
> 
> [1  1    1     | 1]
> [0  1    2     | 1]
> [0  2  λ-1     | 2]
> 
> F₃ → F₃ - 2F₂
> 
> [1  1    1     | 1]
> [0  1    2     | 1]
> [0  0  λ-5     | 0]
> ```
> 
> **Análisis:**
> 
> **Caso 1: λ ≠ 5**
> 
> (λ-5)z = 0 → z = 0
> 
> - rg(A) = 3, rg(A|b) = 3, n = 3
> - **Compatible Determinado**
> 
> Solución:
> 
> ```
> z = 0
> y + 2(0) = 1  →  y = 1
> x + 1 + 0 = 1  →  x = 0
> ```
> 
> Solución única: **(0, 1, 0)**
> 
> **Caso 2: λ = 5**
> 
> Tercera fila: 0 = 0 (identidad)
> 
> - rg(A) = 2, rg(A|b) = 2, n = 3
> - **Compatible Indeterminado** (1 grado de libertad)
> 
> Solución:
> 
> ```
> y + 2z = 1  →  y = 1 - 2z
> x + (1-2z) + z = 1  →  x = z
> ```
> 
> Con z = μ: **(μ, 1-2μ, μ)**
> 
> ---
> 
> **Solución Ejercicio 25:**
> 
> **Demostración:**
> 
> **Hipótesis:** A es invertible (n×n)
> 
> **Consecuencias:**
> 
> - det(A) ≠ 0
> - rg(A) = n (rango completo)
> - A tiene inversa A⁻¹
> 
> **Para el sistema Ax = b:**
> 
> Como rg(A) = n y agregar la columna b no puede hacer que el rango exceda n:
> 
> rg(A|b) ≤ n
> 
> Pero también rg(A|b) ≥ rg(A) = n
> 
> Por tanto: rg(A|b) = n
> 
> **Aplicando Rouché-Frobenius:**
> 
> rg(A) = rg(A|b) = n
> 
> **Conclusión:** Sistema Compatible Determinado (solución única)
> 
> **Además**, la solución es: x = A⁻¹b ∎
> 
> ---
> 
> **Solución Ejercicio 26:**
> 
> Para 2 grados de libertad necesitamos:
> 
> - Sistema compatible: rg(A) = rg(A|b)
> - Grados de libertad = n - rg(A) = 2
> - Por tanto: rg(A) = 4 - 2 = 2
> 
> Sistema: $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & 1 & | & 1 \ 2 & 2 & 2 & 2 & | & k \ 3 & 3 & 3 & 3 & | & m \end{pmatrix}$$
> 
> Observamos que todas las filas tienen coeficientes proporcionales.
> 
> Reducción:
> 
> ```
> F₂ → F₂ - 2F₁
> F₃ → F₃ - 3F₁
> 
> [1  1  1  1 | 1  ]
> [0  0  0  0 | k-2]
> [0  0  0  0 | m-3]
> ```
> 
> Para rg(A) = 1 y rg(A|b) = 1:
> 
> **k - 2 = 0 → k = 2** **m - 3 = 0 → m = 3**
> 
> Verificación: Con k = 2 y m = 3, tenemos rg(A) = rg(A|b) = 1
> 
> Grados de libertad = 4 - 1 = 3 ≠ 2 ❌
> 
> **Corrección:** Para tener exactamente 2 grados de libertad con 4 incógnitas, necesitamos rg(A) = 2.
> 
> Esto requeriría agregar otra ecuación linealmente independiente. Con solo 3 ecuaciones proporcionales es imposible lograr rg = 2.
> 
> **Respuesta:** No es posible con este sistema. Se necesitarían ecuaciones adicionales o diferentes.
> 
> ---
> 
> **Solución Ejercicio 28:**
> 
> **Dato:** A es m×n con rg(A) = r, y Ax = b tiene solución
> 
> **Análisis:**
> 
> Si tiene solución → rg(A) = rg(A|b) = r
> 
> Número de parámetros libres = n - r
> 
> **Mínimo número de parámetros:**
> 
> El mínimo ocurre cuando r es máximo posible.
> 
> Como rg(A) = r (dato), ese es el rango que tenemos.
> 
> **Respuesta:** El número de parámetros libres es **n - r**
> 
> - Si r = n: 0 parámetros (Compatible Determinado)
> - Si r < n: n - r parámetros (Compatible Indeterminado)

## 📊 Casos Especiales y Situaciones Particulares

### 🔍 Sistemas Homogéneos

> [!note]- 🟦 Propiedades de Sistemas Homogéneos (Ax = 0)
> 
> **Definición:** Un sistema es homogéneo si b = 0, es decir, Ax = 0
> 
> **Propiedades fundamentales:**
> 
> **1. Siempre son compatibles:**
> 
> - x = 0 (solución trivial) siempre es solución
> - rg(A) = rg(A|0) siempre (columna de ceros no aumenta rango)
> 
> **2. Clasificación:**
> 
> **Caso A: rg(A) = n**
> 
> - Compatible Determinado
> - **Solo solución trivial:** x = 0
> - Las columnas de A son linealmente independientes
> 
> **Caso B: rg(A) < n**
> 
> - Compatible Indeterminado
> - **Infinitas soluciones** (incluyendo la trivial)
> - Soluciones no triviales existen
> - Grados de libertad: n - rg(A)
> 
> **3. Espacio nulo (Núcleo):**
> 
> El conjunto de todas las soluciones de Ax = 0 forma un **subespacio vectorial** llamado:
> 
> - **Nul(A)** o **Ker(A)** (núcleo de A)
> - Dimensión: dim(Nul(A)) = n - rg(A)
> 
> **4. Teorema de rango-nulidad:**
> 
> $$\boxed{\text{rg}(A) + \dim(\text{Nul}(A)) = n}$$
> 
> **Ejemplo:**
> 
> $$\begin{cases} x + 2y - z = 0 \ 2x + 4y - 2z = 0 \end{cases}$$
> 
> Matriz: $$A = \begin{pmatrix} 1 & 2 & -1 \ 2 & 4 & -2 \end{pmatrix}$$
> 
> F₂ = 2F₁ → rg(A) = 1
> 
> Grados de libertad: 3 - 1 = 2
> 
> Solución general:
> 
> ```
> x + 2y - z = 0  →  x = -2y + z
> ```
> 
> Con y = λ, z = μ: $$\begin{pmatrix} x \ y \ z \end{pmatrix} = \lambda \begin{pmatrix} -2 \ 1 \ 0 \end{pmatrix} + \mu \begin{pmatrix} 1 \ 0 \ 1 \end{pmatrix}$$
> 
> El núcleo es un **plano** en ℝ³ que pasa por el origen.

### 🔍 Sistemas Cuadrados (m = n)

> [!tip]- 🟨 Sistemas con Igual Número de Ecuaciones e Incógnitas
> 
> **Caso especial:** A es matriz cuadrada n×n
> 
> **Criterio del determinante:**
> 
> Para sistemas cuadrados:
> 
> $$\boxed{\det(A) \neq 0 \iff \text{rg}(A) = n \iff \text{Sistema Compatible Determinado}}$$
> 
> **Tabla de equivalencias:**
> 
> |det(A)|rg(A)|Tipo de Sistema|Soluciones|
> |---|---|---|---|
> |≠ 0|n|Compatible Det.|Única: x = A| ⁻¹b |
> | = 0 | < n | Compatible Ind. o Incompatible | Depende de b |
> 
> **Casos cuando det(A) = 0:**
> 
> **1. Sistema Homogéneo (Ax = 0):**
> 
> - Siempre Compatible Indeterminado
> - Infinitas soluciones (incluyendo x = 0)
> 
> **2. Sistema No Homogéneo (Ax = b, b ≠ 0):**
> 
> - Puede ser Compatible Indeterminado (infinitas soluciones)
> - Puede ser Incompatible (sin solución)
> - Depende de si b ∈ Col(A)
> 
> **Ejemplo - Compatible Determinado:**
> 
> $$\begin{cases} x + y = 3 \ 2x - y = 0 \end{cases}$$
> 
> $$\det(A) = \begin{vmatrix} 1 & 1 \ 2 & -1 \end{vmatrix} = -1 - 2 = -3 \neq 0$$
> 
> Por tanto: **Compatible Determinado**
> 
> Solución: x = A⁻¹b = (1, 2)
> 
> **Ejemplo - det(A) = 0, Compatible Indeterminado:**
> 
> $$\begin{cases} x + y = 2 \ 2x + 2y = 4 \end{cases}$$
> 
> $$\det(A) = \begin{vmatrix} 1 & 1 \ 2 & 2 \end{vmatrix} = 2 - 2 = 0$$
> 
> Análisis: Segunda ecuación es el doble de la primera
> 
> - rg(A) = 1, rg(A|b) = 1
> - **Compatible Indeterminado**
> 
> **Ejemplo - det(A) = 0, Incompatible:**
> 
> $$\begin{cases} x + y = 2 \ 2x + 2y = 5 \end{cases}$$
> 
> $$\det(A) = 0$$
> 
> Análisis: rg(A) = 1 < rg(A|b) = 2
> 
> - **Incompatible**

### 🔍 Sistemas Rectangulares

> [!warning]- 🟧 Sistemas con m ≠ n
> 
> **Tipo 1: Sistemas Subdeterminados (m < n)**
> 
> Menos ecuaciones que incógnitas
> 
> **Características:**
> 
> - rg(A) ≤ min(m, n) = m < n
> - Si es compatible: siempre tiene infinitas soluciones
> - Grados de libertad ≥ n - m
> 
> **Ejemplo:** $$\begin{cases} x + y + z = 1 \ 2x - y + z = 0 \end{cases}$$
> 
> m = 2, n = 3 (subdeterminado)
> 
> Si rg(A) = rg(A|b) = 2 < 3:
> 
> - Compatible Indeterminado
> - Al menos 3 - 2 = 1 grado de libertad
> 
> **Tipo 2: Sistemas Sobredeterminados (m > n)**
> 
> Más ecuaciones que incógnitas
> 
> **Características:**
> 
> - rg(A) ≤ min(m, n) = n
> - Puede ser incompatible (común)
> - Puede ser compatible determinado
> - Puede ser compatible indeterminado (raro)
> 
> **Ejemplo Compatible:** $$\begin{cases} x + y = 3 \ 2x - y = 0 \ x + 3y = 7 \end{cases}$$
> 
> m = 3, n = 2 (sobredeterminado)
> 
> Verificación: Si las tres ecuaciones son consistentes
> 
> - rg(A) = rg(A|b) = 2 = n
> - **Compatible Determinado**
> 
> **Ejemplo Incompatible:** $$\begin{cases} x + y = 1 \ x + y = 2 \ x + y = 3 \end{cases}$$
> 
> Las tres ecuaciones son contradictorias
> 
> - rg(A) = 1 < rg(A|b) = 3
> - **Incompatible**
> 
> **Aplicaciones:**
> 
> - **Ajuste de curvas:** Mínimos cuadrados
> - **Sistemas inconsistentes:** Aproximaciones
> - **Redundancia:** Verificación de datos

### 🔍 Sistemas con Parámetros

> [!example]- 🟪 Análisis Paramétrico Sistemático
> 
> **Metodología general:**
> 
> **Paso 1:** Escribir la matriz ampliada con parámetros
> 
> **Paso 2:** Reducir por filas (manteniendo parámetros simbólicos)
> 
> **Paso 3:** Identificar valores críticos donde el rango cambia
> 
> - Valores que hacen que pivotes sean cero
> - Valores que crean/eliminan contradicciones
> 
> **Paso 4:** Analizar cada caso por separado
> 
> **Paso 5:** Resumir en tabla de discusión
> 
> **Ejemplo completo:**
> 
> $$\begin{cases} x + y + z = 1 \ x + 2y + 4z = 2 \ x + 3y + az = b \end{cases}$$
> 
> **Matriz ampliada:** $$[A|b] = \begin{pmatrix} 1 & 1 & 1 & | & 1 \ 1 & 2 & 4 & | & 2 \ 1 & 3 & a & | & b \end{pmatrix}$$
> 
> **Reducción:**
> 
> ```
> F₂ → F₂ - F₁
> F₃ → F₃ - F₁
> 
> [1  1   1  | 1  ]
> [0  1   3  | 1  ]
> [0  2  a-1 | b-1]
> 
> F₃ → F₃ - 2F₂
> 
> [1  1   1    | 1    ]
> [0  1   3    | 1    ]
> [0  0  a-7   | b-3  ]
> ```
> 
> **Análisis:**
> 
> La tercera fila es: (a-7)z = b-3
> 
> **Caso 1: a ≠ 7**
> 
> Elemento a-7 ≠ 0 es pivote
> 
> - rg(A) = 3
> - rg(A|b) = 3
> - **Compatible Determinado** para cualquier b
> 
> **Caso 2: a = 7**
> 
> Tercera fila: 0·z = b-3
> 
> **Subcaso 2a: a = 7 y b = 3**
> 
> - 0 = 0 (identidad)
> - rg(A) = 2, rg(A|b) = 2
> - **Compatible Indeterminado** (1 parámetro)
> 
> **Subcaso 2b: a = 7 y b ≠ 3**
> 
> - 0 = b-3 ≠ 0 (contradicción)
> - rg(A) = 2 < rg(A|b) = 3
> - **Incompatible**
> 
> **Tabla resumen:**
> 
> |a|b|Tipo|Soluciones|
> |---|---|---|---|
> |a ≠ 7|cualquier b|CD|1|
> |a = 7|b = 3|CI|∞ (1 param)|
> |a = 7|b ≠ 3|I|0|

## 🎓 Teoremas y Propiedades Importantes

### 📐 Teoremas Relacionados

> [!note]- 📚 Teoremas Fundamentales del Álgebra Lineal
> 
> **Teorema 1: Existencia de Soluciones**
> 
> Un sistema Ax = b tiene solución si y solo si b ∈ Col(A)
> 
> Equivalentemente: b es combinación lineal de las columnas de A
> 
> **Teorema 2: Unicidad de Soluciones**
> 
> Si Ax = b tiene solución, esta es única ⟺ Nul(A) = {0}
> 
> Equivalentemente: Las columnas de A son linealmente independientes
> 
> **Teorema 3: Rango-Nulidad**
> 
> Para matriz A (m×n): $$\boxed{\text{rg}(A) + \dim(\text{Nul}(A)) = n}$$
> 
> Consecuencia: Grados de libertad = n - rg(A)
> 
> **Teorema 4: Para Matrices Cuadradas (Equivalencias)**
> 
> Para A (n×n), las siguientes afirmaciones son equivalentes:
> 
> 1. A es invertible
> 2. det(A) ≠ 0
> 3. rg(A) = n
> 4. Las columnas de A son linealmente independientes
> 5. Las filas de A son linealmente independientes
> 6. Ax = b tiene solución única para todo b
> 7. Ax = 0 tiene solo la solución trivial
> 8. Col(A) = ℝⁿ
> 9. Nul(A) = {0}
> 
> **Teorema 5: Superposición (Sistemas Homogéneos)**
> 
> Si x₁ y x₂ son soluciones de Ax = 0, entonces:
> 
> - c₁x₁ + c₂x₂ también es solución (∀c₁, c₂ ∈ ℝ)
> - Las soluciones forman un subespacio vectorial
> 
> **Teorema 6: Solución General de Sistema No Homogéneo**
> 
> Si xₚ es una solución particular de Ax = b, y xₕ es la solución general de Ax = 0, entonces:
> 
> $$\boxed{x_{\text{general}} = x_p + x_h}$$
> 
> **Ejemplo:**
> 
> Para Ax = b con solución particular xₚ = (1, 0, 2) y núcleo generado por v = (1, -1, 0):
> 
> Solución general: x = (1, 0, 2) + λ(1, -1, 0)
> 
> **Teorema 7: Propiedades del Rango**
> 
> 1. rg(A) = rg(Aᵀ)
> 2. rg(AB) ≤ min{rg(A), rg(B)}
> 3. rg(A + B) ≤ rg(A) + rg(B)
> 4. Si A es invertible: rg(AB) = rg(B)
> 5. rg(A) = número de pivotes en forma escalonada
> 
> **Teorema 8: Alternativa de Fredholm**
> 
> Para sistema Ax = b, exactamente una de las siguientes es verdadera:
> 
> 6. Ax = b tiene solución para todo b
> 7. Aᵀy = 0 tiene solución no trivial
> 
> **Teorema 9: Compatibilidad y Ortogonalidad**
> 
> Ax = b tiene solución ⟺ b es ortogonal a todas las soluciones de Aᵀy = 0

### 🔧 Propiedades Operacionales

> [!tip]- ⚙️ Operaciones que Preservan/Cambian el Rango
> 
> **Operaciones que NO cambian el rango:**
> 
> 1. **Intercambiar filas:** F_i ↔ F_j
> 2. **Multiplicar fila por escalar no nulo:** F_i → kF_i (k ≠ 0)
> 3. **Sumar múltiplo de una fila a otra:** F_i → F_i + kF_j
> 4. **Transpuesta:** rg(A) = rg(Aᵀ)
> 5. **Operaciones elementales de columnas**
> 
> **Operaciones que pueden cambiar el rango:**
> 
> 6. **Multiplicar fila por cero:** Disminuye el rango
> 7. **Eliminar fila no nula:** Disminuye el rango
> 8. **Agregar fila LI:** Puede aumentar el rango
> 9. **Suma de matrices:** rg(A + B) puede ser mayor, igual o menor
> 10. **Producto de matrices:** rg(AB) ≤ min{rg(A), rg(B)}
> 
> **Ejemplos:**
> 
> **Preservación por operaciones elementales:**
> 
> ```
> A = [1  2]    F₂ → F₂ - 2F₁    [1  2]
>     [2  4]    ───────────→      [0  0]
> 
> rg(A) = 1 antes y después
> ```
> 
> **Cambio por producto:**
> 
> ```
> A = [1  0]  rg(A) = 2
>     [0  1]
> 
> B = [1  1]  rg(B) = 1
>     [1  1]
> 
> AB = [1  1]  rg(AB) = 1 < min{2,1} ✓
>      [1  1]
> ```
> 
> **Cambio por suma:**
> 
> ```
> A = [1   0]  rg(A) = 1
>     [-1  0]
> 
> B = [0  1]  rg(B) = 1
>     [0  1]
> 
> A+B = [1  1]  rg(A+B) = 2 > rg(A) + rg(B) - 1
>       [-1 1]
> ```

## 🌐 Aplicaciones Prácticas

### 💼 Aplicaciones en Ingeniería

> [!example]- ⚡ Circuitos Eléctricos
> 
> **Leyes de Kirchhoff:**
> 
> Las corrientes en un circuito eléctrico con n nodos y m mallas satisfacen un sistema de ecuaciones lineales.
> 
> **Ejemplo - Circuito con 3 mallas:**
> 
> ```
>     R₁=2Ω        R₂=3Ω
>   ───/\/\/\───●───/\/\/\───
>   |           |            |
>   |           |            |
>  V₁=12V      R₃=4Ω       V₂=6V
>   |           |            |
>   |           |            |
>   ─────────────●───────────
> ```
> 
> **Sistema de ecuaciones (Ley de Mallas):** $$\begin{cases} 2i_1 + 4i_3 = 12 \ 3i_2 - 4i_3 = 6 \ i_1 + i_2 = i_3 \end{cases}$$
> 
> Reescribiendo: $$\begin{cases} 2i_1 + 0i_2 + 4i_3 = 12 \ 0i_1 + 3i_2 - 4i_3 = 6 \ i_1 + i_2 - i_3 = 0 \end{cases}$$
> 
> **Análisis con Rouché-Frobenius:**
> 
> $$[A|b] = \begin{pmatrix} 2 & 0 & 4 & | & 12 \ 0 & 3 & -4 & | & 6 \ 1 & 1 & -1 & | & 0 \end{pmatrix}$$
> 
> Reducción muestra que rg(A) = rg(A|b) = 3
> 
> **Conclusión:** Sistema Compatible Determinado
> 
> Las corrientes tienen valores únicos determinados.

> [!example]- 🏗️ Estructuras y Estática
> 
> **Análisis de armaduras (Método de los Nudos):**
> 
> En una estructura, las fuerzas en equilibrio satisfacen:
> 
> - ΣFₓ = 0 (suma de fuerzas horizontales)
> - ΣFᵧ = 0 (suma de fuerzas verticales)
> 
> **Ejemplo - Armadura con 3 barras:**
> 
> ```
>         B
>        /|\
>       / | \
>      /  |  \
>    T₁  T₂  T₃
>    /   |   \
>   /    |    \
>  A     |     C
>        ↓
>       100N
> ```
> 
> **Equilibrio en nudo B:** $$\begin{cases} T_1\cos(45°) - T_3\cos(45°) = 0 \ T_1\sin(45°) + T_2 + T_3\sin(45°) = 100 \end{cases}$$
> 
> Simplificando (con cos(45°) = sin(45°) = √2/2): $$\begin{cases} T_1 - T_3 = 0 \ 0.707T_1 + T_2 + 0.707T_3 = 100 \end{cases}$$
> 
> Con condición adicional (simetría): T₁ = T₃
> 
> Sistema se reduce: $$\begin{cases} T_1 - T_3 = 0 \ 1.414T_1 + T_2 = 100 \end{cases}$$
> 
> **Análisis:** Sistema subdeterminado (2 ecuaciones, 3 incógnitas)
> 
> Si agregamos condición de apoyo o material, se vuelve determinado.

> [!example]- 🔬 Balances de Materia (Ingeniería Química)
> 
> **Balance de masa en proceso continuo:**
> 
> Entrada = Salida + Acumulación
> 
> **Ejemplo - Mezclador con 3 corrientes:**
> 
> ```
> F₁ (x₁=0.8) ─→ \
>                 \
>                  ●─→ F₃ (x₃=?)
>                 /
> F₂ (x₂=0.3) ─→ /
> ```
> 
> F = caudal (kg/h), x = fracción de componente A
> 
> **Balance total:** $$F_1 + F_2 = F_3$$
> 
> **Balance de componente A:** $$0.8F_1 + 0.3F_2 = x_3F_3$$
> 
> Si conocemos F₁ = 100 kg/h y queremos F₃ = 150 kg/h:
> 
> $$\begin{cases} 100 + F_2 = 150 \ 0.8(100) + 0.3F_2 = x_3(150) \end{cases}$$
> 
> Primera ecuación: F₂ = 50 kg/h
> 
> Segunda ecuación: 80 + 15 = 150x₃ → x₃ = 0.633
> 
> **Sistema Compatible Determinado:** Solución única posible.

### 💰 Aplicaciones en Economía

> [!example]- 📊 Modelo de Leontief (Input-Output)
> 
> **Análisis de sectores económicos interdependientes:**
> 
> Economía con n sectores donde cada sector:
> 
> - Produce output
> - Requiere inputs de otros sectores
> 
> **Ejemplo - 3 sectores (Agricultura, Industria, Servicios):**
> 
> Matriz de coeficientes técnicos A y demanda final d:
> 
> $$A = \begin{pmatrix} 0.2 & 0.3 & 0.1 \ 0.4 & 0.2 & 0.2 \ 0.1 & 0.3 & 0.4 \end{pmatrix}, \quad d = \begin{pmatrix} 100 \ 150 \ 200 \end{pmatrix}$$
> 
> **Sistema:** (I - A)x = d
> 
> donde x = vector de producción total
> 
> $$(I - A) = \begin{pmatrix} 0.8 & -0.3 & -0.1 \ -0.4 & 0.8 & -0.2 \ -0.1 & -0.3 & 0.6 \end{pmatrix}$$
> 
> **Pregunta:** ¿Cuánto debe producir cada sector para satisfacer la demanda?
> 
> **Análisis Rouché-Frobenius:**
> 
> Calcular det(I - A):
> 
> Si det(I - A) ≠ 0 → Sistema Compatible Determinado
> 
> Solución única: x = (I - A)⁻¹d

> [!example]- 💹 Optimización de Portafolios
> 
> **Asignación de inversiones con restricciones:**
> 
> Inversionista con $100,000 quiere distribuir en 3 activos:
> 
> - Acciones (A)
> - Bonos (B)
> - Efectivo (C)
> 
> **Restricciones:**
> 
> 1. Total invertido: A + B + C = 100,000
> 2. Al menos 30% en bonos: B ≥ 30,000
> 3. Acciones no más del doble de bonos: A ≤ 2B
> 
> **Sistema (considerando igualdades):** $$\begin{cases} A + B + C = 100,000 \ B = 30,000 \ A = 2B \end{cases}$$
> 
> Sustituyendo: $$\begin{cases} A + 30,000 + C = 100,000 \ A = 60,000 \end{cases}$$
> 
> Entonces: C = 10,000
> 
> **Solución:** (A, B, C) = (60,000, 30,000, 10,000)
> 
> Sistema Compatible Determinado bajo restricciones de igualdad.

### 🔬 Aplicaciones en Ciencias

> [!example]- 🧪 Balanceo de Ecuaciones Químicas
> 
> **Balancear:** C₃H₈ + O₂ → CO₂ + H₂O
> 
> Con coeficientes a, b, c, d: aC₃H₈ + bO₂ → cCO₂ + dH₂O
> 
> **Balance de átomos:**
> 
> - Carbono (C): 3a = c
> - Hidrógeno (H): 8a = 2d
> - Oxígeno (O): 2b = 2c + d
> 
> **Sistema:** $$\begin{cases} 3a - c = 0 \ 8a - 2d = 0 \ 2b - 2c - d = 0 \end{cases}$$
> 
> Matriz: $$[A|0] = \begin{pmatrix} 3 & 0 & -1 & 0 & | & 0 \ 8 & 0 & 0 & -2 & | & 0 \ 0 & 2 & -2 & -1 & | & 0 \end{pmatrix}$$
> 
> Sistema homogéneo → Compatible (infinitas soluciones)
> 
> Solución con menor entero: a = 1, b = 5, c = 3, d = 4
> 
> **Ecuación balanceada:** C₃H₈ + 5O₂ → 3CO₂ + 4H₂O

## 📝 Estrategias de Resolución

### 🎯 Metodología Paso a Paso

> [!tip]- 🗺️ Algoritmo General para Clasificar Sistemas
> 
> **PASO 1: Identificar el sistema**
> 
> - Número de ecuaciones (m)
> - Número de incógnitas (n)
> - Escribir en forma matricial Ax = b
> 
> **PASO 2: Formar matriz ampliada [A|b]**
> 
> ```
> [A|b] = [a₁₁ a₁₂ ... a₁ₙ | b₁]
>         [a₂₁ a₂₂ ... a₂ₙ | b₂]
>         [ ⋮   ⋮   ⋱  ⋮   | ⋮ ]
>         [aₘ₁ aₘ₂ ... aₘₙ | bₘ]
> ```
> 
> **PASO 3: Reducir a forma escalonada**
> 
> - Usar eliminación gaussiana
> - Aplicar operaciones elementales
> - Mantener registro de pasos (si hay parámetros)
> 
> **PASO 4: Calcular rangos**
> 
> - rg(A) = número de filas no nulas en A reducida
> - rg(A|b) = número de filas no nulas en [A|b] reducida
> 
> **PASO 5: Aplicar Rouché-Frobenius**
> 
> ```
> SI rg(A) < rg(A|b) ENTONCES
>     Sistema INCOMPATIBLE
>     
> SI NO (rg(A) = rg(A|b))
>     SI rg(A) = n ENTONCES
>         Sistema COMPATIBLE DETERMINADO
>         Resolver por sustitución regresiva
>     SI NO
>         Sistema COMPATIBLE INDETERMINADO
>         Grados de libertad = n - rg(A)
>         Expresar solución con parámetros
> ```
> 
> **PASO 6: Interpretar resultado**
> 
> - 0 soluciones: Incompatible
> - 1 solución: Compatible Determinado
> - ∞ soluciones: Compatible Indeterminado
> 
> **PASO 7: (Opcional) Verificar solución**
> 
> - Sustituir en ecuaciones originales
> - Confirmar que satisface todas las ecuaciones

### 🔍 Trucos y Atajos

> [!tip]- ⚡ Métodos Rápidos de Identificación
> 
> **Atajo 1: Observación Visual**
> 
> Antes de reducir, busca:
> 
> - **Filas/ecuaciones idénticas** → rango menor
> - **Filas proporcionales** → dependencia lineal
> - **Ecuaciones contradictorias evidentes** → incompatible
> 
> Ejemplo:
> 
> ```
> x + y = 1
> x + y = 2  ← Contradicción obvia, incompatible
> ```
> 
> **Atajo 2: Sistemas 2×2**
> 
> Para sistema: $$\begin{cases} a_1x + b_1y = c_1 \ a_2x + b_2y = c_2 \end{cases}$$
> 
> Calcular: Δ = a₁b₂ - a₂b₁
> 
> - **Si Δ ≠ 0:** Compatible Determinado
> - **Si Δ = 0:** Verificar si ecuaciones son proporcionales
>     - Proporcionales y consistentes → Compatible Indeterminado
>     - Proporcionales pero inconsistentes → Incompatible
> 
> **Atajo 3: Sistemas Homogéneos**
> 
> Para Ax = 0:
> 
> - **Siempre compatible** (x = 0 es solución)
> - Solo verificar si det(A) = 0 para infinitas soluciones
> 
> **Atajo 4: Sistemas Triangulares**
> 
> Si la matriz ya es triangular:
> 
> ```
> [*  *  *]
> [0  *  *]
> [0  0  *]
> ```
> 
> Rango = número de elementos * en diagonal ≠ 0
> 
> **Atajo 5: Matrices con Bloques de Ceros**
> 
> ```
> [A₁₁  0  ]
> [ 0  A₂₂]
> ```
> 
> rg(A) = rg(A₁₁) + rg(A₂₂)
> 
> **Atajo 6: Identificación Rápida de Incompatibilidad**
> 
> Después de reducir, busca filas tipo:
> 
> ```
> [0  0  0 ... 0 | k]  donde k ≠ 0
> ```
> 
> Esta fila representa 0 = k → **Incompatible inmediatamente**

## 📖 Resumen y Puntos Clave

> [!abstract]- 🎓 Conceptos Esenciales para Recordar
> 
> ### Teorema de Rouché-Frobenius
> 
> **Enunciado central:**
> 
> Para sistema Ax = b:
> 
> |Condición|Tipo de Sistema|N° Soluciones|Grados de Libertad|
> |---|---|---|---|
> |rg(A) < rg(A\|b)|Incompatible|0|-|
> |rg(A) = rg(A\|b) = n|Compatible Determinado|1|0|
> |rg(A) = rg(A\|b) = r < n|Compatible Indeterminado|∞|n - r|
> 
> ### Puntos Clave
> 
> **1. Compatibilidad:**
> 
> - Sistema tiene solución ⟺ rg(A) = rg(A|b)
> - Sistema NO tiene solución ⟺ rg(A) < rg(A|b)
> 
> **2. Tipo de solución (si es compatible):**
> 
> - Única solución ⟺ rango = n (número de incógnitas)
> - Infinitas soluciones ⟺ rango < n
> 
> **3. Rango:**
> 
> - Es el número máximo de filas/columnas linealmente independientes
> - Se calcula por reducción gaussiana (filas no nulas)
> - No cambia con operaciones elementales
> 
> **4. Sistemas homogéneos (Ax = 0):**
> 
> - SIEMPRE son compatibles (x = 0 es solución)
> - Tienen solo solución trivial ⟺ rg(A) = n
> - Tienen infinitas soluciones ⟺ rg(A) < n
> 
> **5. Grados de libertad:**
> 
> - Número de parámetros libres = n - rg(A)
> - Representa la dimensión del espacio de soluciones
> 
> **6. Matrices cuadradas (n×n):**
> 
> - det(A) ≠ 0 ⟺ rg(A) = n ⟺ Solución única
> - det(A) = 0 ⟺ rg(A) < n ⟺ Múltiples soluciones o incompatible
> 
> **7. Interpretación geométrica:**
> 
> - 2×2: Rectas que se cortan (CD), coinciden (CI), o son paralelas (I)
> - 3×3: Planos que se cortan en punto (CD), recta (CI), o no se cortan (I)

> [!summary]- 📋 Tabla de Decisión Rápida
> 
> ### Algoritmo de Clasificación
> 
> ```
> 1. Calcular rg(A) y rg(A|b)
> 
> 2. Comparar rangos:
>    
>    ┌─ rg(A) < rg(A|b) ──→ INCOMPATIBLE (0 soluciones)
>    │
>    └─ rg(A) = rg(A|b) = r
>       │
>       ├─ r = n ──→ COMPATIBLE DETERMINADO (1 solución)
>       │
>       └─ r < n ──→ COMPATIBLE INDETERMINADO (∞ soluciones)
>                    con (n-r) grados de libertad
> ```
> 
> ### Casos Especiales
> 
> |Tipo de Sistema|Características|Rango|
> |---|---|---|
> |Homogéneo|Siempre compatible|rg(A) = rg(A\|0)|
> |Cuadrado + det≠0|Única solución|rg(A) = n|
> |Subdeterminado (m<n)|Si compatible → infinitas|rg ≤ m < n|
> |Sobredeterminado (m>n)|A menudo incompatible|rg ≤ n|

---

## 🎯 Errores Comunes y Cómo Evitarlos

> [!warning]- ⚠️ Trampas Frecuentes
> 
> ### Error 1: Confundir rg(A) con rg(A|b)
> 
> **❌ Incorrecto:**
> 
> - "Como det(A) = 0, el sistema es incompatible"
> 
> **✅ Correcto:**
> 
> - det(A) = 0 solo indica que rg(A) < n
> - Necesitamos comparar rg(A) con rg(A|b)
> - Puede ser compatible indeterminado O incompatible
> 
> **Ejemplo:**
> 
> ```
> Sistema 1: x + y = 1      Sistema 2: x + y = 1
>           2x + 2y = 2              2x + 2y = 3
> 
> Ambos tienen det(A) = 0, pero:
> Sistema 1: Compatible Indeterminado
> Sistema 2: Incompatible
> ```
> 
> ### Error 2: No verificar todas las filas en la reducción
> 
> **❌ Incorrecto:**
> 
> - Dejar de reducir antes de llegar a forma escalonada completa
> - Puede llevar a calcular mal el rango
> 
> **✅ Correcto:**
> 
> - Reducir completamente hasta que todos los ceros posibles estén debajo de pivotes
> - Contar TODAS las filas no nulas
> 
> ### Error 3: Olvidar contar grados de libertad
> 
> **❌ Incorrecto:**
> 
> - "El sistema tiene infinitas soluciones" (sin especificar cuántos parámetros)
> 
> **✅ Correcto:**
> 
> - "El sistema tiene infinitas soluciones con n - r grados de libertad"
> - Expresar solución general con parámetros λ, μ, etc.
> 
> ### Error 4: Confusión con sistemas homogéneos
> 
> **❌ Incorrecto:**
> 
> - "Un sistema homogéneo puede ser incompatible"
> 
> **✅ Correcto:**
> 
> - Los sistemas homogéneos SIEMPRE son compatibles
> - x = 0 siempre es solución
> - Solo pueden ser CD (si rg=n) o CI (si rg<n)
> 
> ### Error 5: Operaciones que cambian el rango
> 
> **❌ Incorrecto:**
> 
> - Multiplicar una fila por cero
> - Eliminar filas "que parecen innecesarias"
> 
> **✅ Correcto:**
> 
> - Solo usar operaciones elementales válidas:
>     - Intercambiar filas
>     - Multiplicar por k ≠ 0
>     - Sumar múltiplo de una fila a otra
> 
> ### Error 6: No verificar contradicciones
> 
> **❌ Incorrecto:**
> 
> - Ignorar filas tipo [0 0 0 | k] con k ≠ 0
> 
> **✅ Correcto:**
> 
> - Una sola fila [0 ... 0 | k≠0] hace el sistema incompatible
> - Representa la ecuación imposible: 0 = k
> 
> ### Error 7: Mala interpretación con parámetros
> 
> **❌ Incorrecto:**
> 
> - "Para a = 2, el sistema es compatible" (sin analizar completamente)
> 
> **✅ Correcto:**
> 
> - Analizar TODOS los casos posibles del parámetro
> - Identificar valores críticos donde cambia el rango
> - Crear tabla completa de discusión

---

## 🧠 Técnicas de Memorización

> [!tip]- 🎨 Reglas Nemotécnicas
> 
> ### Mnemónico 1: "RR = Solución"
> 
> **Rangos Iguales = Compatible**
> 
> - **R**g(A) = **R**g(A|b) → Sistema **R**esoluble
> 
> ### Mnemónico 2: "Si suma, resta soluciones"
> 
> - **Menor que** (rg(A) **<** rg(A|b)) → **resta** soluciones → **0** soluciones
> - **Igual a** (rg(A) **=** rg(A|b)) → **suma** posibilidades → soluciones **existen**
> 
> ### Mnemónico 3: "R = N: Única; R < N: Infinitas"
> 
> - **R**ango = **N**úmero de incógnitas → **Ú**nica solución
> - **R**ango **<** **N** → I**N**finitas soluciones
> 
> ### Visualización: Semáforo
> 
> ```
> 🔴 ROJO (Incompatible): rg(A) < rg(A|b)
>     → DETENTE, no hay solución
> 
> 🟡 AMARILLO (CI): rg(A) = rg(A|b) < n
>     → PRECAUCIÓN, infinitas opciones
> 
> 🟢 VERDE (CD): rg(A) = rg(A|b) = n
>     → ADELANTE, una solución única
> ```
> 
> ### Analogía: Rompecabezas
> 
> - **Incompatible**: Piezas que no encajan (contradicción)
> - **Compatible Determinado**: Una única forma de armar (solución única)
> - **Compatible Indeterminado**: Múltiples formas válidas (infinitas soluciones)

---

## 📚 Recursos Adicionales

> [!info]- 🔗 Material Complementario
> 
> ### Conceptos Relacionados
> 
> 1. **Espacios vectoriales**
>     - Espacio columna: Col(A)
>     - Espacio nulo: Nul(A)
>     - Dimensión y bases
> 2. **Determinantes**
>     - Cálculo y propiedades
>     - Relación con invertibilidad
>     - Regla de Cramer
> 3. **Sistemas de ecuaciones**
>     - Método de Gauss-Jordan
>     - Eliminación gaussiana
>     - Factorización LU
> 4. **Independencia lineal**
>     - Combinaciones lineales
>     - Bases y dimensión
>     - Wronskiano
> 
> ### Temas Avanzados
> 
> 1. **Teorema de rango-nulidad**
>     - dim(Im(A)) + dim(Ker(A)) = n
> 2. **Descomposición SVD**
>     - A = UΣVᵀ
>     - Rango y valores singulares
> 3. **Pseudo-inversa de Moore-Penrose**
>     - Solución de mínimos cuadrados
>     - Sistemas inconsistentes
> 4. **Espacios afines**
>     - Variedades lineales
>     - Geometría de soluciones

---

## ✅ Checklist de Dominio del Tema

> [!check]- ☑️ Autoevaluación
> 
> ### Conceptos Básicos
> 
> - [ ] Puedo explicar qué es el rango de una matriz
> - [ ] Entiendo la diferencia entre rg(A) y rg(A|b)
> - [ ] Sé calcular rangos por reducción gaussiana
> - [ ] Identifico sistemas compatibles e incompatibles
> - [ ] Distingo entre compatible determinado e indeterminado
> 
> ### Aplicación del Teorema
> 
> - [ ] Clasifico correctamente cualquier sistema 2×2
> - [ ] Clasifico correctamente cualquier sistema 3×3
> - [ ] Manejo sistemas con parámetros
> - [ ] Determino grados de libertad correctamente
> - [ ] Expreso soluciones generales con parámetros
> 
> ### Casos Especiales
> 
> - [ ] Reconozco propiedades de sistemas homogéneos
> - [ ] Aplico el teorema a matrices cuadradas
> - [ ] Analizo sistemas subdeterminados
> - [ ] Analizo sistemas sobredeterminados
> - [ ] Interpreto geométricamente las soluciones
> 
> ### Habilidades Avanzadas
> 
> - [ ] Discuto completamente sistemas paramétricos
> - [ ] Resuelvo problemas aplicados (circuitos, economía, etc.)
> - [ ] Relaciono con otros teoremas de álgebra lineal
> - [ ] Evito todos los errores comunes
> - [ ] Puedo enseñar el tema a otros
> 
> ### Puntuación
> 
> - **20/20**: ¡Dominio completo! 🌟
> - **15-19**: Excelente comprensión 👍
> - **10-14**: Buen nivel, seguir practicando 📚
> - **< 10**: Revisar conceptos fundamentales 📖

---

## 🎓 Ejercicios de Consolidación Final

> [!example]- 🏆 Desafíos Integradores
> 
> ### Desafío 1: Problema Completo Paso a Paso
> 
> Dado el sistema dependiente de parámetros a y b:
> 
> $$\begin{cases} x + y + z = 1 \ 2x + ay + 2z = b \ x + 4y + z = 5 \end{cases}$$
> 
> **Tareas:**
> 
> 1. Realizar discusión completa según a y b
> 2. Para cada caso, determinar tipo de sistema
> 3. Si es compatible, expresar la solución general
> 4. Dar interpretación geométrica
> 
> ---
> 
> ### Desafío 2: Análisis Teórico
> 
> **Demuestre:**
> 
> a) Si A es m×n con m > n y rg(A) = n, entonces Ax = b puede no tener solución.
> 
> b) Si Ax = b tiene solución única, entonces Ax = 0 solo tiene la solución trivial.
> 
> c) Para sistema homogéneo: rg(A) = n ⟺ det(A) ≠ 0 (si A es cuadrada)
> 
> ---
> 
> ### Desafío 3: Problema Aplicado
> 
> En una red eléctrica con 4 nodos, las corrientes i₁, i₂, i₃, i₄ satisfacen:
> 
> $$\begin{cases} i_1 + i_2 = 10 \ i_2 + i_3 = 8 \ i_3 + i_4 = 6 \ i_1 - i_4 = 4 \end{cases}$$
> 
> a) Clasifique el sistema b) Determine las corrientes c) Si hay una medición errónea y la última ecuación es i₁ - i₄ = 5, ¿qué ocurre?
> 
> ---
> 
> ### Desafío 4: Caso Extremo
> 
> Considere el sistema con parámetro λ:
> 
> $$\begin{cases} x + y + z + w = 1 \ x + λy + z + w = λ \ x + y + λz + w = λ \ x + y + z + λw = λ \end{cases}$$
> 
> Determine para qué valores de λ el sistema:
> 
> - Es compatible determinado
> - Es compatible indeterminado
> - Es incompatible
> 
> ---
> 
> ### Desafío 5: Conexión con Otros Conceptos
> 
> Sea A una matriz 3×3 con rg(A) = 2.
> 
> a) ¿Cuál es dim(Nul(A))? b) ¿Puede Ax = b tener solución única? c) Si Ax = b tiene solución, ¿cuántos grados de libertad tiene? d) Dé un ejemplo concreto de tal sistema

---

## 🌟 Reflexiones Finales

> [!note]- 💭 Importancia y Perspectiva
> 
> ### ¿Por qué es fundamental este teorema?
> 
> El Teorema de Rouché-Frobenius es una de las joyas del álgebra lineal porque:
> 
> 1. **Universalidad**: Aplica a CUALQUIER sistema lineal
> 2. **Eficiencia**: Determina existencia sin resolver
> 3. **Elegancia**: Conecta álgebra (rangos) con geometría (soluciones)
> 4. **Aplicabilidad**: Base de innumerables aplicaciones prácticas
> 
> ### Conexiones profundas
> 
> Este teorema está conectado con:
> 
> - **Geometría**: Intersección de variedades lineales
> - **Optimización**: Restricciones factibles
> - **Computación**: Algoritmos numéricos
> - **Física**: Leyes de conservación
> - **Economía**: Equilibrio de mercados
> 
> ### Próximos pasos
> 
> Después de dominar este teorema, explorar:
> 
> 1. Métodos numéricos para sistemas grandes
> 2. Sistemas de ecuaciones no lineales
> 3. Ecuaciones diferenciales lineales
> 4. Álgebra lineal computacional
> 5. Optimización lineal y programación
> 
> ### Mensaje final
> 
> > _"El Teorema de Rouché-Frobenius no solo nos dice si un sistema tiene solución, sino que nos revela la estructura profunda de las relaciones lineales. Es la puerta de entrada al pensamiento matemático moderno."_
> 
> ¡Sigue practicando y explorando las maravillas del álgebra lineal! 🚀

---
## 🔗 Enlaces con Notas del Sistema

> [!quote]- 🌐 Relaciones Conceptuales
> 
> **Depende directamente de:**
> 
> - [[04 - Rango de una matriz]] - Concepto fundamental del teorema
> - [[05 - Formas Escalonadas y Matriz Escalonada]] - Método para calcular rangos
> - [[03 - Algoritmo de Gauss]] - Herramienta de cálculo
> - [[02 - Sistemas de ecuaciones lineales]] - Objeto de estudio
> - [[Matrices]] - Estructura algebraica base
> 
> **Es prerequisito para:**
> 
> - [[07 - Clasificación de soluciones de un S.E.L.]] - Aplicación directa
> - [[08 - Dimensión y descripción del conjunto solución]] - Análisis de infinitas soluciones
> - [[09 - Resolución de sistemas lineales]] - Estrategias de solución
> - [[10 - Sistemas homogéneos]] - Caso especial
> 
> **Conceptos relacionados:**
> 
> - [[Espacios Vectoriales]] - Espacio solución como subespacio
> - [[Dependencia e Independencia Lineal]] - Relación con el rango
> - [[Subespacios vectoriales]] - Conjunto solución de sistemas compatibles
> - [[Dimensión de un espacio vectorial]] - Grados de libertad
> 
> **Aplicaciones prácticas:**
> 
> - [[Circuitos Eléctricos - Leyes de Kirchhoff]] - Análisis de redes
> - [[Sistemas de Balance de Materia]] - Ingeniería Química
> - [[Modelo de Leontief]] - Economía Input-Output
> - [[Análisis Estructural]] - Estática y armaduras
> - [[Balanceo de Ecuaciones Químicas]] - Estequiometría
> 
> **Extensiones y generalizaciones:**
> 
> - [[Sistemas con parámetros]] - Discusión de sistemas
> - [[Mínimos Cuadrados]] - Sistemas incompatibles aproximados
> - [[Pseudoinversa de Moore-Penrose]] - Soluciones generalizadas
> - [[Programación Lineal]] - Factibilidad de restricciones
> - [[Teoremas de Existencia y Unicidad]] - Ecuaciones diferenciales

> [!info]- 📚 Temas Avanzados Relacionados
> 
> **Para profundizar después de dominar este tema:**
> 
> **Álgebra Lineal Computacional:**
> 
> - Métodos iterativos para sistemas grandes
> - Factorización LU, QR, SVD
> - Estabilidad numérica y condicionamiento
> - Matrices dispersas y técnicas especializadas
> 
> **Espacios Vectoriales:**
> 
> - Teorema de la dimensión
> - Espacios fundamentales (Col, Nul, Row, Null(Aᵀ))
> - Complemento ortogonal
> - Proyecciones y descomposiciones
> 
> **Sistemas No Lineales:**
> 
> - Método de Newton para sistemas
> - Linealización
> - Análisis de estabilidad
> - Sistemas dinámicos
> 
> **Optimización:**
> 
> - Programación lineal (método simplex)
> - Condiciones KKT
> - Dualidad
> - Optimización restringida
> 
> **Aplicaciones Avanzadas:**
> 
> - Análisis de circuitos AC
> - Sistemas de control
> - Procesamiento de señales
> - Machine Learning (regresión, clasificación)
> - Análisis de redes sociales (PageRank)

---

## 🎓 Recursos Adicionales para Estudio

> [!tip]- 📖 Material Complementario Recomendado
> 
> **Libros de referencia:**
> 
> 1. **Álgebra Lineal Básica:**
>     - Grossman, S. "Álgebra Lineal" (Cap. 3-4)
>     - Lay, D. "Álgebra Lineal y sus Aplicaciones" (Cap. 1-2)
>     - Strang, G. "Introduction to Linear Algebra" (Cap. 2)
> 2. **Álgebra Lineal Avanzada:**
>     - Anton, H. "Elementary Linear Algebra" (Cap. 4-5)
>     - Poole, D. "Linear Algebra: A Modern Introduction" (Cap. 2-3)
> 3. **Aplicaciones:**
>     - Strang, G. "Linear Algebra and Learning from Data"
>     - Meyer, C. "Matrix Analysis and Applied Linear Algebra"
> 
> **Recursos en línea:**
> 
> - MIT OpenCourseWare - Linear Algebra (18.06)
> - Khan Academy - Linear Algebra
> - 3Blue1Brown - "Essence of Linear Algebra" (YouTube)
> - Paul's Online Math Notes - Linear Algebra
> 
> **Software recomendado:**
> 
> - MATLAB/Octave - Cálculos numéricos
> - Python (NumPy, SciPy) - Análisis computacional
> - Mathematica/WolframAlpha - Cálculos simbólicos
> - GeoGebra - Visualización geométrica


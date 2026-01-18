# 🔢 Matriz Asociada a un S.E.L. y Sistema Aumentado

## 🎯 Introducción

> [!info]- 💡 ¿Qué es un Sistema de Ecuaciones Lineales?
> 
> Un **Sistema de Ecuaciones Lineales (S.E.L.)** es un conjunto de ecuaciones algebraicas de primer grado con varias incógnitas. La representación matricial permite usar las herramientas del álgebra lineal para resolver estos sistemas de forma eficiente.
> 
> **Forma general:**
> 
> ```
> a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ = b₁
> a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ = b₂
>      ⋮         ⋮              ⋮
> aₘ₁x₁ + aₘ₂x₂ + ... + aₘₙxₙ = bₘ
> ```
> 
> **Analogía práctica:** Imagina que tienes varias restricciones (ecuaciones) sobre cantidades desconocidas (variables). La representación matricial organiza toda esta información de manera compacta y permite aplicar operaciones sistemáticas para encontrar las soluciones.
> 
> **¿Por qué es importante?**
> 
> |Aspecto|Descripción|Aplicación|
> |---|---|---|
> |**Compacidad**|Notación concisa|Sistemas grandes|
> |**Algoritmos**|Métodos sistemáticos|Cómputo eficiente|
> |**Teoría**|Propiedades algebraicas|Análisis de soluciones|
> |**Generalización**|Estructura uniforme|Múltiples contextos|
> |**Visualización**|Interpretación geométrica|Comprensión intuitiva|

```mermaid
graph TB
    A[Sistema de Ecuaciones Lineales] --> B[Forma Escalar]
    A --> C[Forma Matricial]
    A --> D[Forma Vectorial]
    
    B --> E[Ecuaciones individuales]
    C --> F[Matriz de coeficientes A]
    C --> G[Matriz aumentada A|b]
    D --> H[Combinación lineal]
    
    F --> I[Ax = b]
    G --> I
    H --> I
    
    style A fill:#e1f5ff
    style I fill:#e1ffe1
```

---

## 📐 Representaciones de un S.E.L.

### 📝 Forma Escalar (Ecuaciones)

> [!example]- 📋 Representación Tradicional
> 
> **Definición:**
> 
> La forma más natural de escribir un sistema es mediante ecuaciones individuales:
> 
> ```
> a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ = b₁
> a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ = b₂
>      ⋮         ⋮              ⋮
> aₘ₁x₁ + aₘ₂x₂ + ... + aₘₙxₙ = bₘ
> ```
> 
> Donde:
> 
> - **aᵢⱼ**: coeficientes conocidos
> - **xⱼ**: incógnitas (variables)
> - **bᵢ**: términos independientes (constantes)
> - **m**: número de ecuaciones
> - **n**: número de incógnitas
> 
> **Ejemplo 1: Sistema 2×2**
> 
> ```
> 2x + 3y = 8
> 4x - y = 2
> 
> Coeficientes:
> a₁₁ = 2,  a₁₂ = 3,  b₁ = 8
> a₂₁ = 4,  a₂₂ = -1, b₂ = 2
> 
> Incógnitas: x, y
> ```
> 
> **Ejemplo 2: Sistema 3×3**
> 
> ```
>  x + 2y - z = 4
> 3x - y + 2z = 1
> 2x + y + z = 3
> 
> Coeficientes:
> Primera ecuación:  1,  2, -1 | 4
> Segunda ecuación:  3, -1,  2 | 1
> Tercera ecuación:  2,  1,  1 | 3
> ```
> 
> **Ejemplo 3: Sistema rectangular (m ≠ n)**
> 
> ```
> x + y + z = 6
> 2x - y = 1
> 
> 2 ecuaciones, 3 incógnitas (subdeterminado)
> ```
> 
> **Ventajas:**
> 
> - ✅ Fácil de leer y escribir
> - ✅ Interpretación directa
> - ✅ Familiar para principiantes
> 
> **Desventajas:**
> 
> - ❌ Tedioso para sistemas grandes
> - ❌ Dificulta ver patrones
> - ❌ No aprovecha estructura matricial

### 🔢 Forma Matricial

> [!note]- 🎯 Representación Compacta
> 
> **Matriz de coeficientes A:**
> 
> ```
> A = [ a₁₁  a₁₂  ...  a₁ₙ ]
>     [ a₂₁  a₂₂  ...  a₂ₙ ]
>     [  ⋮    ⋮    ⋱   ⋮  ]
>     [ aₘ₁  aₘ₂  ...  aₘₙ ]
> 
> Dimensión: m × n
> - m filas (ecuaciones)
> - n columnas (variables)
> ```
> 
> **Vector de incógnitas x:**
> 
> ```
> x = [ x₁ ]
>     [ x₂ ]
>     [ ⋮  ]
>     [ xₙ ]
> 
> Dimensión: n × 1
> ```
> 
> **Vector de términos independientes b:**
> 
> ```
> b = [ b₁ ]
>     [ b₂ ]
>     [ ⋮  ]
>     [ bₘ ]
> 
> Dimensión: m × 1
> ```
> 
> **Ecuación matricial:**
> 
> **Ax = b**
> 
> Esta simple ecuación encapsula todo el sistema.
> 
> **Ejemplo del sistema 2×2:**
> 
> ```
> 2x + 3y = 8
> 4x - y = 2
> 
> Forma matricial:
> 
> [ 2   3 ] [ x ]   [ 8 ]
> [ 4  -1 ] [ y ] = [ 2 ]
> 
> A         x    =  b
> ```
> 
> **Verificación del producto:**
> 
> ```
> Ax = [ 2   3 ] [ x ]   [ 2x + 3y ]
>      [ 4  -1 ] [ y ] = [ 4x - y  ]
> 
> Igualando con b:
> [ 2x + 3y ]   [ 8 ]
> [ 4x - y  ] = [ 2 ]
> 
> Recuperamos las ecuaciones originales ✅
> ```
> 
> **Ejemplo del sistema 3×3:**
> 
> ```
> [ 1   2  -1 ] [ x ]   [ 4 ]
> [ 3  -1   2 ] [ y ] = [ 1 ]
> [ 2   1   1 ] [ z ]   [ 3 ]
> ```
> 
> **Propiedades de la representación:**
> 
> |Componente|Símbolo|Dimensión|Significado|
> |---|---|---|---|
> |Matriz coeficientes|A|m × n|Transforma variables|
> |Vector incógnitas|x|n × 1|Variables a encontrar|
> |Vector términos|b|m × 1|Resultados deseados|
> |Sistema completo|Ax = b|-|Ecuación matricial|

### 📊 Matriz Aumentada

> [!success]- 🔗 Sistema Completo
> 
> **Definición:**
> 
> La **matriz aumentada** combina A y b en una sola estructura:
> 
> **[A|b]**
> 
> ```
> [A|b] = [ a₁₁  a₁₂  ...  a₁ₙ | b₁ ]
>         [ a₂₁  a₂₂  ...  a₂ₙ | b₂ ]
>         [  ⋮    ⋮    ⋱   ⋮   | ⋮  ]
>         [ aₘ₁  aₘ₂  ...  aₘₙ | bₘ ]
> 
> Dimensión: m × (n+1)
> ```
> 
> La línea vertical | separa coeficientes de términos independientes.
> 
> **Ejemplo 1: Sistema 2×2**
> 
> ```
> 2x + 3y = 8
> 4x - y = 2
> 
> Matriz aumentada:
> 
> [ 2   3 | 8 ]
> [ 4  -1 | 2 ]
> 
> Fila 1: coeficientes de ecuación 1 + término independiente
> Fila 2: coeficientes de ecuación 2 + término independiente
> ```
> 
> **Ejemplo 2: Sistema 3×4 (subdeterminado)**
> 
> ```
> x + 2y - z + w = 5
> 2x - y + z = 3
> x + y + w = 4
> 
> [ 1   2  -1   1 | 5 ]
> [ 2  -1   1   0 | 3 ]
> [ 1   1   0   1 | 4 ]
> 
> 3 ecuaciones, 4 incógnitas
> ```
> 
> **¿Por qué usar matriz aumentada?**
> 
> ```mermaid
> graph LR
>     A[Matriz Aumentada<br/>A|b] --> B[Operaciones elementales]
>     B --> C[Eliminación Gaussiana]
>     B --> D[Gauss-Jordan]
>     
>     C --> E[Forma escalonada]
>     D --> F[Forma escalonada reducida]
>     
>     E --> G[Resolver sistema]
>     F --> G
>     
>     style A fill:#e1f5ff
>     style G fill:#e1ffe1
> ```
> 
> **Ventajas:**
> 
> - ✅ Mantiene coeficientes y términos juntos
> - ✅ Facilita operaciones fila
> - ✅ Evita errores de sincronización
> - ✅ Formato estándar para algoritmos
> 
> **Notación alternativa:**
> 
> Algunos textos usan:
> 
> ```
> (A|b)  o  [A : b]  o  A̅
> ```

### 🎨 Forma Vectorial

> [!tip]- 🔄 Combinación Lineal
> 
> **Interpretación alternativa:**
> 
> El sistema Ax = b puede verse como una combinación lineal de las columnas de A:
> 
> ```
> x₁ [ a₁₁ ]   x₂ [ a₁₂ ]       xₙ [ a₁ₙ ]   [ b₁ ]
>    [ a₂₁ ] +    [ a₂₂ ] + ... +   [ a₂ₙ ] = [ b₂ ]
>    [  ⋮  ]      [  ⋮  ]           [  ⋮  ]   [ ⋮  ]
>    [ aₘ₁ ]      [ aₘ₂ ]           [ aₘₙ ]   [ bₘ ]
> 
> x₁a₁ + x₂a₂ + ... + xₙaₙ = b
> ```
> 
> Donde aⱼ es la j-ésima columna de A.
> 
> **Ejemplo:**
> 
> ```
> Sistema:
> 2x + 3y = 8
> 4x - y = 2
> 
> Forma vectorial:
> 
> x [ 2 ]  +  y [  3 ] = [ 8 ]
>   [ 4 ]       [ -1 ]   [ 2 ]
> 
> ¿Qué combinación de los vectores (2,4) y (3,-1)
> produce el vector (8,2)?
> ```
> 
> **Interpretación geométrica en ℝ²:**
> 
> ```
> Vector objetivo: b = (8, 2)
> 
> Columnas de A:
> a₁ = (2, 4)  ← primera columna
> a₂ = (3, -1) ← segunda columna
> 
> Pregunta: ¿Existe combinación xa₁ + ya₂ = b?
> 
> Si sí → sistema compatible
> Si no → sistema incompatible
> ```
> 
> **Ventajas de esta vista:**
> 
> - ✅ Interpretación geométrica clara
> - ✅ Conecta con espacios vectoriales
> - ✅ Revela estructura del espacio columna
> - ✅ Útil para teoría (existencia de soluciones)

---

## 🔧 Construcción de Matrices

### 📥 De Ecuaciones a Matrices

> [!example]- 🔨 Proceso de Conversión
> 
> **Algoritmo de construcción:**
> 
> ```
> Entrada: Sistema de ecuaciones
> Salida: Matriz aumentada [A|b]
> 
> Paso 1: Identificar incógnitas (ordenar: x₁, x₂, ..., xₙ)
> Paso 2: Para cada ecuación i:
>   a. Escribir coeficiente de cada variable (usar 0 si falta)
>   b. Escribir término independiente al final
> Paso 3: Formar matriz fila por fila
> ```
> 
> **Ejemplo 1: Sistema ordenado**
> 
> ```
> 3x - 2y + z = 7
> x + 4y - 3z = -2
> 2x + y + 5z = 11
> 
> Variables en orden: x, y, z
> 
> Ecuación 1: coefs = [3, -2, 1], término = 7
> Ecuación 2: coefs = [1, 4, -3], término = -2
> Ecuación 3: coefs = [2, 1, 5], término = 11
> 
> Matriz aumentada:
> [ 3  -2   1 |  7 ]
> [ 1   4  -3 | -2 ]
> [ 2   1   5 | 11 ]
> ```
> 
> **Ejemplo 2: Variables desordenadas**
> 
> ```
> 2y - 3x = 5
> x + 4y = 1
> 
> ¡Cuidado! Reordenar primero:
> 
> -3x + 2y = 5
>   x + 4y = 1
> 
> Ahora en orden (x, y):
> [ -3   2 | 5 ]
> [  1   4 | 1 ]
> ```
> 
> **Ejemplo 3: Variables faltantes**
> 
> ```
> x + z = 3
> 2y - z = 1
> x + y = 2
> 
> Falta y en ec.1, falta x en ec.2, falta z en ec.3
> Usar coeficiente 0:
> 
> x + 0y + z = 3
> 0x + 2y - z = 1
> x + y + 0z = 2
> 
> [ 1   0   1 | 3 ]
> [ 0   2  -1 | 1 ]
> [ 1   1   0 | 2 ]
> ```
> 
> **Ejemplo 4: Sistema homogéneo**
> 
> ```
> 2x - y + 3z = 0
> x + 2y - z = 0
> 3x + y + 2z = 0
> 
> Todos los términos independientes son 0:
> 
> [ 2  -1   3 | 0 ]
> [ 1   2  -1 | 0 ]
> [ 3   1   2 | 0 ]
> 
> Vector b = 0 (vector cero)
> ```
> 
> **Errores comunes:**
> 
> ```
> ❌ INCORRECTO:
> 2x + 3 = y  →  [ 2  1 | 3 ]  NO!
> 
> ✅ CORRECTO:
> Primero reordenar: 2x - y = -3
> Luego: [ 2  -1 | -3 ]
> 
> ❌ INCORRECTO:
> x = 5  →  [ 1 | 5 ]  Falta dimensión
> 
> ✅ CORRECTO (sistema 2D):
> x + 0y = 5  →  [ 1  0 | 5 ]
> ```

### 📤 De Matrices a Ecuaciones

> [!note]- 🔄 Proceso Inverso
> 
> **Algoritmo de reconstrucción:**
> 
> ```
> Entrada: Matriz aumentada [A|b] de m×(n+1)
> Salida: Sistema de ecuaciones
> 
> Para cada fila i (i = 1 hasta m):
>   Ecuación i: Σ(j=1 hasta n) aᵢⱼxⱼ = bᵢ
> ```
> 
> **Ejemplo 1: Sistema básico**
> 
> ```
> Matriz aumentada:
> [ 1   2  -3 | 4 ]
> [ 2  -1   1 | 3 ]
> [ 0   3   2 | 5 ]
> 
> Variables: x, y, z
> 
> Fila 1:  1x + 2y - 3z = 4  →  x + 2y - 3z = 4
> Fila 2:  2x - 1y + 1z = 3  →  2x - y + z = 3
> Fila 3:  0x + 3y + 2z = 5  →  3y + 2z = 5
> 
> Sistema:
>   x + 2y - 3z = 4
>  2x - y + z = 3
>      3y + 2z = 5
> ```
> 
> **Ejemplo 2: Coeficientes especiales**
> 
> ```
> [ 0   1   0 | 3 ]
> [ 1   0   0 | 2 ]
> [ 0   0   1 | 5 ]
> 
> Fila 1:  0x + 1y + 0z = 3  →  y = 3
> Fila 2:  1x + 0y + 0z = 2  →  x = 2
> Fila 3:  0x + 0y + 1z = 5  →  z = 5
> 
> ¡Sistema diagonal! Solución directa.
> ```
> 
> **Ejemplo 3: Forma escalonada**
> 
> ```
> [ 1   2   3 | 6 ]
> [ 0   1   2 | 4 ]
> [ 0   0   1 | 1 ]
> 
> Fila 1:  x + 2y + 3z = 6
> Fila 2:      y + 2z = 4
> Fila 3:          z = 1
> 
> Forma triangular → sustitución hacia atrás
> ```
> 
> **Verificación:**
> 
> ```
> Después de convertir, verificar:
> 1. ✅ Número de ecuaciones = número de filas
> 2. ✅ Número de variables = número de columnas - 1
> 3. ✅ Términos independientes en columna final
> 4. ✅ Coeficientes 0 para variables ausentes
> ```

---

## 🎯 Tipos de Sistemas según Dimensiones

### 📏 Clasificación Dimensional

> [!info]- 📐 Según m y n
> 
> **Tabla de clasificación:**
> 
> |m|n|Relación|Nombre|Características|
> |---|---|---|---|---|
> |m = n|n|Cuadrado|Determinado|Generalmente solución única|
> |m < n|n|Rectangular ancho|Subdeterminado|Infinitas soluciones o ninguna|
> |m > n|n|Rectangular alto|Sobredeterminado|Sin solución exacta o única|
> 
> **Sistema cuadrado (m = n):**
> 
> ```
> Matriz A es cuadrada n×n
> 
> Ejemplo 3×3:
> [ 1   2  -1 ] [ x ]   [ 4 ]
> [ 3  -1   2 ] [ y ] = [ 1 ]
> [ 2   1   1 ] [ z ]   [ 3 ]
> 
> Casos:
> - Si det(A) ≠ 0: solución única x = A⁻¹b
> - Si det(A) = 0: infinitas soluciones o ninguna
> ```
> 
> **Sistema subdeterminado (m < n):**
> 
> ```
> Más incógnitas que ecuaciones
> 
> Ejemplo 2×3:
> [ 1   2   1 | 5 ]
> [ 2  -1   3 | 4 ]
> 
> 2 ecuaciones, 3 incógnitas
> 
> Si compatible: infinitas soluciones (n - m grados de libertad)
> Si incompatible: sin solución
> ```
> 
> **Sistema sobredeterminado (m > n):**
> 
> ```
> Más ecuaciones que incógnitas
> 
> Ejemplo 4×2:
> [ 1   2 | 3 ]
> [ 2  -1 | 1 ]
> [ 1   1 | 2 ]
> [ 3   1 | 4 ]
> 
> 4 ecuaciones, 2 incógnitas
> 
> Generalmente sin solución exacta
> → Usar mínimos cuadrados para solución aproximada
> ```
> 
> **Diagrama de decisión:**
> 
> ```mermaid
> graph TD
>     A[Sistema Ax = b] --> B{Comparar m y n}
>     
>     B -->|m = n| C[Sistema Cuadrado]
>     B -->|m < n| D[Subdeterminado]
>     B -->|m > n| E[Sobredeterminado]
>     
>     C --> F{det A ≠ 0?}
>     F -->|Sí| G[Solución única<br/>x = A⁻¹b]
>     F -->|No| H[Infinitas o ninguna]
>     
>     D --> I[Infinitas soluciones<br/>o ninguna]
>     E --> J[Generalmente<br/>sin solución exacta]
>     
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
>     style E fill:#ffe1e1
> ```

### 🔍 Sistemas Homogéneos vs No Homogéneos

> [!tip]- ⚖️ Según el Vector b
> 
> **Sistema homogéneo:**
> 
> ```
> Ax = 0  (b = 0, vector cero)
> 
> Ejemplo:
>  x + 2y - z = 0
> 2x - y + 3z = 0
>  x + y + z = 0
> 
> Matriz aumentada:
> [ 1   2  -1 | 0 ]
> [ 2  -1   3 | 0 ]
> [ 1   1   1 | 0 ]
> 
> Propiedades:
> ✅ SIEMPRE tiene solución: x = 0 (solución trivial)
> ✅ Si det(A) ≠ 0: solo x = 0
> ✅ Si det(A) = 0: infinitas soluciones
> ✅ Soluciones forman subespacio vectorial
> ```
> 
> **Sistema no homogéneo:**
> 
> ```
> Ax = b  (b ≠ 0, al menos un bᵢ ≠ 0)
> 
> Ejemplo:
>  x + 2y - z = 4
> 2x - y + 3z = 1
>  x + y + z = 3
> 
> Matriz aumentada:
> [ 1   2  -1 | 4 ]
> [ 2  -1   3 | 1 ]
> [ 1   1   1 | 3 ]
> 
> Propiedades:
> ❓ Puede tener solución o no
> ❓ Si tiene, puede ser única o infinitas
> ❌ Soluciones NO forman subespacio
> ```
> 
> **Relación entre ambos:**
> 
> ```
> Sistema no homogéneo: Ax = b
> Sistema homogéneo asociado: Ax = 0
> 
> Teorema:
> Si xₚ es solución particular de Ax = b
> y xₕ es solución de Ax = 0
> 
> Entonces x = xₚ + xₕ también es solución de Ax = b
> 
> Solución general: x = xₚ + ker(A)
> ```
> 
> **Comparación:**
> 
> |Aspecto|Homogéneo (Ax = 0)|No Homogéneo (Ax = b)|
> |---|---|---|
> |**Solución trivial**|Siempre x = 0|No existe|
> |**Existencia**|Siempre|Depende de rg(A) y rg(A\|b)|
> |**Estructura**|Subespacio vectorial|Variedad afín|
> |**Superposición**|✅ Suma de soluciones es solución|❌ No aplica|
> |**Multiplicación**|✅ αx solución si x lo es|❌ No aplica|

---

## 🔬 Operaciones Elementales por Filas

### 🎲 Tipos de Operaciones

> [!example]- 🛠️ Transformaciones Permitidas
> 
> **Las tres operaciones elementales:**
> 
> **Tipo 1: Intercambio de filas**
> 
> ```
> Fᵢ ↔ Fⱼ
> 
> Intercambiar las filas i y j
> 
> Ejemplo:
> [ 1   2 | 3 ]      [ 4   5 | 6 ]
> [ 4   5 | 6 ]  →   [ 1   2 | 3 ]
> 
> F₁ ↔ F₂
> 
> Efecto en ecuaciones: cambiar orden
> ```
> 
> **Tipo 2: Multiplicar fila por escalar no nulo**
> 
> ```
> Fᵢ → kFᵢ  (k ≠ 0)
> 
> Multiplicar todos los elementos de fila i por k
> 
> Ejemplo:
> [ 2   4  -6 | 8 ]      [ 1   2  -3 | 4 ]
> [ 1   3   2 | 5 ]  →   [ 1   3   2 | 5 ]
> 
> F₁ → (1/2)F₁
> 
> Efecto en ecuaciones: multiplicar ecuación por constante
> ```
> 
> **Tipo 3: Sumar múltiplo de una fila a otra**
> 
> ```
> Fᵢ → Fᵢ + kFⱼ  (i ≠ j)
> 
> Reemplazar fila i por fila i más k veces fila j
> 
> Ejemplo:
> [ 1   2 | 3 ]      [ 1   2 | 3 ]
> [ 3   4 | 5 ]  →   [ 0  -2 |-4 ]
> 
> F₂ → F₂ - 3F₁
> 
> Efecto en ecuaciones: restar ecuaciones
> ```
> 
> **Notación:**
> 
> ```
> Operación     Notación común
> ---------------------------------
> Intercambio   Rᵢ ↔ Rⱼ  o  Fᵢ ↔ Fⱼ
> Escalamiento  Rᵢ → kRᵢ  o  kFᵢ
> Combinación   Rᵢ → Rᵢ + kRⱼ  o  Fᵢ + kFⱼ
> ```
> 
> **Propiedad fundamental:**
> 
> ```
> Las operaciones elementales NO cambian el conjunto solución
> 
> Si [A|b] → [A'|b'] mediante operaciones elementales
> Entonces:
> Soluciones de Ax = b = Soluciones de A'x = b'
> 
> ✅ Sistemas equivalentes
> ```

### 📋 Ejemplos de Aplicación

> [!success]- 💫 Transformaciones Paso a Paso
> 
> **Ejemplo 1: Crear cero debajo del pivote**
> 
> ```
> Matriz inicial:
> [ 2 1 3| 5 ] [ 4 3 7 | 11] [ 6 2 8 | 14]
> 
> Objetivo: Hacer ceros en columna 1, debajo del 2
> 
> Paso 1: F₂ → F₂ - 2F₁ [ 2 1 3 | 5 ] [ 0 1 1 | 1 ] ← 4-2(2)=0, 3-2(1)=1, etc. [ 6 2 8 | 14]
> 
> Paso 2: F₃ → F₃ - 3F₁ [ 2 1 3 | 5 ] [ 0 1 1 | 1 ] [ 0 -1 -1 | -1] ← 6-3(2)=0, 2-3(1)=-1, etc.
> 
> ```
> 
> **Ejemplo 2: Obtener 1 como pivote**
> 
> ```
> 
> [ 3 6 9 | 12] [ 1 2 1 | 4 ] [ 2 4 3 | 7 ]
> 
> Opción A: Dividir F₁ F₁ → (1/3)F₁
> 
> [ 1 2 3 | 4 ] [ 1 2 1 | 4 ] [ 2 4 3 | 7 ]
> 
> Opción B: Intercambiar filas F₁ ↔ F₂
> 
> [ 1 2 1 | 4 ] [ 3 6 9 | 12] [ 2 4 3 | 7 ]
> 
> ✅ Opción B evita fracciones
> 
> ```
> 
> **Ejemplo 3: Eliminación completa**
> 
> ```
> 
> Sistema inicial: [ 1 2 -1 | 4 ] [ 2 1 3 | 9 ] [ 3 1 2 | 10]
> 
> Paso 1: Eliminar columna 1 debajo de pivote F₂ → F₂ - 2F₁ F₃ → F₃ - 3F₁
> 
> [ 1 2 -1 | 4 ] [ 0 -3 5 | 1 ] ← 2-2(1)=0, 1-2(2)=-3, etc. [ 0 -5 5 | -2] ← 3-3(1)=0, 1-3(2)=-5, etc.
> 
> Paso 2: Eliminar columna 2 debajo de segundo pivote F₃ → F₃ - (5/3)F₂
> 
> [ 1 2 -1 | 4 ] [ 0 -3 5 | 1 ] [ 0 0 -10/3 | -11/3] ← cálculos detallados
> 
> ✅ Forma escalonada alcanzada
> 
> ```
> 
> **Ejemplo 4: Estrategia con fracciones**
> 
> ```
> 
> [ 1 1/2 1/3 | 1 ] [ 2 1 2/3 | 3 ] [ 3 3/2 1 | 4 ]
> 
> Estrategia: Eliminar fracciones primero Multiplicar cada fila por mcm de denominadores
> 
> F₁ → 6F₁ F₂ → 3F₂ F₃ → 2F₃
> 
> [ 6 3 2 | 6 ] [ 6 3 2 | 9 ] ← ¡Filas proporcionales! [ 6 3 2 | 8 ]
> 
> Sistema inconsistente detectado
> ```

---

## 🎨 Formas Especiales de Matrices

### 🔺 Forma Escalonada (Row Echelon Form)

> [!note]- 📐 Estructura Triangular
> 
> **Definición:**
> 
> Una matriz está en **forma escalonada** si cumple:
> 
> 1. Todas las filas de ceros están al final
> 2. El primer elemento no nulo de cada fila (pivote) está a la derecha del pivote de la fila anterior
> 3. Todos los elementos debajo de un pivote son cero
> 
> **Visualización:**
> 
> ```
> Forma escalonada típica:
> 
> [ ★  *  *  *  * | * ]
> [ 0  ★  *  *  * | * ]
> [ 0  0  0  ★  * | * ]
> [ 0  0  0  0  ★ | * ]
> [ 0  0  0  0  0 | 0 ]
> 
> Donde:
> ★ = pivote (primer elemento no nulo de fila)
> * = cualquier valor
> 0 = cero
> ```
> 
> **Ejemplos válidos:**
> 
> ```
> Ejemplo 1:
> [ 1   2   3 | 4 ]
> [ 0   1   5 | 6 ]
> [ 0   0   1 | 2 ]
> ✅ Forma escalonada
> 
> Ejemplo 2:
> [ 2   4  -1   3 | 5 ]
> [ 0   3   2  -1 | 4 ]
> [ 0   0   0   4 | 6 ]
> [ 0   0   0   0 | 0 ]
> ✅ Forma escalonada (columna 3 sin pivote)
> 
> Ejemplo 3:
> [ 1   0   2 | 3 ]
> [ 0   0   1 | 4 ]
> ✅ Forma escalonada (fila sin segunda columna pivote)
> ```
> 
> **Ejemplos NO válidos:**
> 
> ```
> Ejemplo 1:
> [ 1   2   3 | 4 ]
> [ 0   1   5 | 6 ]
> [ 0   0   0 | 0 ]
> [ 0   0   1 | 2 ]
> ❌ Fila de ceros no está al final
> 
> Ejemplo 2:
> [ 1   2   3 | 4 ]
> [ 0   1   5 | 6 ]
> [ 0   2   1 | 3 ]
> ❌ Hay elemento no nulo debajo de pivote
> 
> Ejemplo 3:
> [ 0   1   3 | 4 ]
> [ 1   2   5 | 6 ]
> ❌ Pivote de F₂ no está a la derecha del de F₁
> ```
> 
> **Propiedades:**
> 
> - Número de pivotes = rango de la matriz
> - Columnas con pivotes → variables básicas
> - Columnas sin pivotes → variables libres
> - Fácil resolver por sustitución hacia atrás
> 
> **Obtención:**
> 
> ```
> Algoritmo de Eliminación Gaussiana:
> 1. Encontrar pivote en columna actual
> 2. Si es cero, intercambiar con fila inferior
> 3. Eliminar elementos debajo del pivote
> 4. Avanzar a siguiente columna/fila
> 5. Repetir hasta procesar todas
> ```

### 💎 Forma Escalonada Reducida (RREF)

> [!tip]- ✨ Forma Canónica
> 
> **Definición:**
> 
> Una matriz está en **forma escalonada reducida** (Reduced Row Echelon Form) si:
> 
> 1. Está en forma escalonada
> 2. Todos los pivotes son 1
> 3. Cada pivote es el ÚNICO elemento no nulo en su columna
> 
> **Visualización:**
> 
> ```
> Forma escalonada reducida:
> 
> [ 1  0  *  0  * | * ]
> [ 0  1  *  0  * | * ]
> [ 0  0  0  1  * | * ]
> [ 0  0  0  0  0 | 0 ]
> 
> Donde:
> 1 = pivote (único elemento no nulo en columna)
> * = cualquier valor
> 0 = cero
> ```
> 
> **Ejemplos:**
> 
> ```
> Ejemplo 1: Sistema con solución única
> [ 1   0   0 | 2 ]
> [ 0   1   0 | 3 ]
> [ 0   0   1 | 5 ]
> 
> Lectura directa: x=2, y=3, z=5
> 
> Ejemplo 2: Sistema con variable libre
> [ 1   2   0 | 3 ]
> [ 0   0   1 | 4 ]
> 
> x + 2y = 3  →  x = 3 - 2y
> z = 4
> y es libre (parámetro)
> 
> Ejemplo 3: Sistema inconsistente
> [ 1   0   2 | 3 ]
> [ 0   1  -1 | 4 ]
> [ 0   0   0 | 1 ]
>                ↑
> ❌ 0 = 1 (contradicción)
> ```
> 
> **Ventajas de RREF:**
> 
> - ✅ Solución se lee directamente
> - ✅ Variables libres claramente identificadas
> - ✅ Inconsistencias evidentes
> - ✅ Forma única para cada matriz
> 
> **Obtención:**
> 
> ```
> Método de Gauss-Jordan:
> 1. Llevar a forma escalonada (Gauss)
> 2. Hacer todos los pivotes = 1
> 3. Eliminar elementos ARRIBA de pivotes
> 4. Procesar de abajo hacia arriba
> ```
> 
> **Ejemplo completo:**
> 
> ```
> Matriz inicial:
> [ 2   4  -2 | 6 ]
> [ 1   3   1 | 8 ]
> [ 3   5  -1 | 11]
> 
> Paso 1: Forma escalonada
> [ 2   4  -2 | 6 ]
> [ 0   1   2 | 5 ]
> [ 0   0   1 | 2 ]
> 
> Paso 2: Pivotes = 1
> F₁ → (1/2)F₁
> [ 1   2  -1 | 3 ]
> [ 0   1   2 | 5 ]
> [ 0   0   1 | 2 ]
> 
> Paso 3: Eliminar arriba de pivotes
> F₂ → F₂ - 2F₃
> F₁ → F₁ + F₃
> [ 1   2   0 | 5 ]
> [ 0   1   0 | 1 ]
> [ 0   0   1 | 2 ]
> 
> F₁ → F₁ - 2F₂
> [ 1   0   0 | 3 ]
> [ 0   1   0 | 1 ]
> [ 0   0   1 | 2 ]
> 
> ✅ RREF alcanzado
> Solución: x=3, y=1, z=2
> ```

---

## 💡 Interpretación Geométrica

### 📊 Sistemas en ℝ²

> [!example]- 🎨 Visualización en el Plano
> 
> **Cada ecuación es una recta:**
> 
> ```
> Ecuación: ax + by = c
> Representa una recta en el plano xy
> 
> Sistema 2×2:
> a₁x + b₁y = c₁  (Recta L₁)
> a₂x + b₂y = c₂  (Recta L₂)
> 
> Solución = Intersección de L₁ y L₂
> ```
> 
> **Caso 1: Solución única**
> 
> ```
> Sistema:
> x + y = 3
> x - y = 1
> 
> Matriz:
> [ 1   1 | 3 ]
> [ 1  -1 | 1 ]
> 
> Geometría:
>       y
>       |
>     3 •---L₁ (x+y=3)
>       |  /|
>     2 | / |
>       |/  |
>     1 •---+---L₂ (x-y=1)
>       |   |
>       +---+---+--- x
>           1   2
> 
> Rectas se cruzan en (2, 1)
> ✅ Solución única
> ```
> 
> **Caso 2: Infinitas soluciones**
> 
> ```
> Sistema:
> 2x + 4y = 6
> x + 2y = 3
> 
> Matriz:
> [ 2   4 | 6 ]
> [ 1   2 | 3 ]
> 
> F₁ → (1/2)F₁
> [ 1   2 | 3 ]
> [ 1   2 | 3 ]
> 
> ¡Ecuaciones idénticas!
> 
> Geometría:
>       y
>       |
>       |  L₁ y L₂ coinciden
>       | /
>       |/
>       +--------- x
> 
> Rectas son la misma
> ✅ Infinitas soluciones (toda la recta)
> ```
> 
> **Caso 3: Sin solución**
> 
> ```
> Sistema:
> x + y = 2
> x + y = 4
> 
> Matriz:
> [ 1   1 | 2 ]
> [ 1   1 | 4 ]
> 
> F₂ → F₂ - F₁
> [ 1   1 | 2 ]
> [ 0   0 | 2 ]
>           ↑
> ❌ 0 = 2 (imposible)
> 
> Geometría:
>       y
>       |
>     4 •----L₂ (x+y=4)
>       |
>     2 •----L₁ (x+y=2)
>       |
>       +--------- x
> 
> Rectas paralelas
> ❌ Sin intersección
> ```

### 🌐 Sistemas en ℝ³

> [!success]- 📐 Visualización en el Espacio
> 
> **Cada ecuación es un plano:**
> 
> ```
> Ecuación: ax + by + cz = d
> Representa un plano en el espacio xyz
> 
> Sistema 3×3:
> Tres planos P₁, P₂, P₃
> 
> Solución = Intersección de los tres planos
> ```
> 
> **Configuraciones posibles:**
> 
> **1. Solución única (tres planos se intersectan en un punto)**
> 
> ```
> Sistema:
> x + y + z = 6
> 2x - y + z = 3
> x + 2y - z = 2
> 
> Los tres planos se cruzan en un único punto
> ✅ Solución: (1, 2, 3)
> ```
> 
> **2. Infinitas soluciones en una recta**
> 
> ```
> Tres planos se intersectan a lo largo de una recta
> 
> Ejemplo:
> x + y + z = 1
> 2x + 2y + 2z = 2  (mismo plano que el primero)
> x - y + z = 0
> 
> Solución: recta paramétrica
> ```
> 
> **3. Infinitas soluciones en un plano**
> 
> ```
> Los tres planos coinciden
> 
> Solución: todo un plano
> ```
> 
> **4. Sin solución - Planos paralelos**
> 
> ```
> Al menos dos planos paralelos sin intersección
> 
> x + y + z = 1
> x + y + z = 2  (paralelo al primero)
> x - y + z = 0
> 
> ❌ Inconsistente
> ```
> 
> **5. Sin solución - Intersección vacía**
> 
> ```
> Tres planos forman un "prisma triangular"
> Cada par se intersecta, pero no hay punto común
> 
> ❌ Inconsistente
> ```
> 
> **Diagrama de casos:**
> 
> ```mermaid
> graph TB
>     A[Sistema 3×3] --> B{¿Los planos<br/>se intersectan?}
>     
>     B -->|Sí| C{¿En cuántos puntos?}
>     B -->|No| D[Sin solución<br/>planos paralelos]
>     
>     C -->|Uno| E[Solución única<br/>punto]
>     C -->|Infinitos| F{¿Forma?}
>     
>     F -->|Recta| G[Infinitas en recta]
>     F -->|Plano| H[Infinitas en plano]
>     
>     style E fill:#e1ffe1
>     style D fill:#ffe1e1
>     style G fill:#fff4e1
>     style H fill:#fff4e1
> ```

---

## 📚 Resumen y Conclusiones

> [!success]- 🎯 Puntos Clave
> 
> **Representaciones equivalentes:**
> 
> |Forma|Notación|Ventaja|Uso|
> |---|---|---|---|
> |**Escalar**|Ecuaciones individuales|Intuitiva|Presentación inicial|
> |**Matricial**|Ax = b|Compacta|Teoría y cómputo|
> |**Aumentada**|[A\|b]|Completa|Algoritmos de resolución|
> |**Vectorial**|Combinación lineal|Geométrica|Interpretación espacial|
> 
> **Operaciones elementales:**
> 
> ```
> 1. Fᵢ ↔ Fⱼ         (intercambio)
> 2. Fᵢ → kFᵢ        (escalamiento, k ≠ 0)
> 3. Fᵢ → Fᵢ + kFⱼ   (combinación)
> 
> ✅ Preservan soluciones
> ✅ Base de eliminación Gaussiana
> ```
> 
> **Formas canónicas:**
> 
> ```
> Forma Escalonada (REF):
> - Estructura triangular
> - Fácil sustitución hacia atrás
> - No única
> 
> Forma Escalonada Reducida (RREF):
> - Pivotes = 1
> - Columnas pivote "limpias"
> - Solución directa
> - Única para cada matriz
> ```
> 
> **Clasificación de sistemas:**
> 
> ```mermaid
> mindmap
>   root((Sistema<br/>Ax = b))
>     Por dimensión
>       Cuadrado m=n
>       Subdeterminado m<n
>       Sobredeterminado m>n
>     Por término
>       Homogéneo b=0
>       No homogéneo b≠0
>     Por soluciones
>       Compatible
>         Determinado única
>         Indeterminado infinitas
>       Incompatible ninguna
> ```
> 
> **Interpretación geométrica:**
> 
> - **ℝ²**: Intersección de rectas
> - **ℝ³**: Intersección de planos
> - **ℝⁿ**: Intersección de hiperplanos
> 
> **Próximos pasos:**
> 
> Con esta base de representación matricial, podemos estudiar:
> 
> - Métodos de resolución (Gauss, Gauss-Jordan, Cramer)
> - Teoría de rango y compatibilidad
> - Espacios vectoriales asociados
> - Aplicaciones prácticas

---

**Tags:** #álgebra-lineal #sistemas-ecuaciones #matrices #matriz-aumentada #eliminación-gaussiana #gauss-jordan #forma-escalonada #RREF #operaciones-elementales #geometría #mermaid #matemáticas

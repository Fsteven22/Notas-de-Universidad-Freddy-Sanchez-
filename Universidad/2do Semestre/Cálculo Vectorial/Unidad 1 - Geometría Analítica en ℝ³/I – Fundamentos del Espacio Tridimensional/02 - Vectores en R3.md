---
dg-publish: true
tags: [MATG1046, unidad1, vectores, R3, magnitud-vector, componentes, vectores-unitarios]
---

# ➡️ Vectores en ℝ³

## 🎯 Introducción

> [!info] 💡 Introducción a los Vectores Tridimensionales
>
> Los **vectores en ℝ³** son magnitudes que poseen tanto **magnitud** (tamaño o longitud) como **dirección** y **sentido** en el espacio tridimensional. Son fundamentales para describir desplazamientos, fuerzas, velocidades y muchas otras cantidades físicas.
>
> **Analogías útiles:**
>
> - **Física:** Una fuerza aplicada a un objeto (intensidad + dirección)
> - **Navegación:** Instrucciones "camina 5 metros al norte y 3 metros hacia arriba"
> - **Videojuegos:** Velocidad de un personaje (velocidad + dirección de movimiento)
>
> **Diferencia fundamental:**
>
> - **Escalar:** Solo magnitud (temperatura: 25°C, masa: 5 kg)
> - **Vector:** Magnitud + dirección + sentido (velocidad: 50 km/h al norte)
>
> **Importancia histórica:**
>
> - **William Hamilton (1843):** Descubrimiento de los cuaterniones
> - **Hermann Grassmann (1844):** Álgebra vectorial general
> - **Josiah Gibbs (1881):** Notación vectorial moderna
> - **Oliver Heaviside (1892):** Análisis vectorial aplicado

---

## 📋 Definiciones Formales

### 1️⃣ Vector

> [!note] 📋 Definición — Vector
>
> **Definición:**
>
> Un **vector en ℝ³** es un elemento del espacio vectorial tridimensional que puede representarse de múltiples formas:
>
> **1. Como terna ordenada:** **v** = (v₁, v₂, v₃) donde v₁, v₂, v₃ ∈ ℝ
>
> **2. Como vector columna:**
>
> ```
> v = [v₁]
>     [v₂]
>     [v₃]
> ```
>
> **3. En términos de vectores base:** **v** = v₁**i** + v₂**j** + v₃**k**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Vector_definicion_01.svg]]
> **Se lee así:** un cuadro raíz «Vector en ℝ³» se ramifica en tres representaciones: la **terna** (v₁, v₂, v₃), la **columna** ordenada y la **combinación** v₁**i** + v₂**j** + v₃**k** — las tres denotan exactamente el mismo objeto.
> **Por qué importa:** marear cada vector en una sola convención obliga a reescribir fórmulas; reconocer las tres formas hace las equivalencias instantáneas.
> **Ejemplo:** el vector de velocidades \vec{V} = (3, 2, 5) en un FPS o en una partícula es el mismo como columna y como \vec{V} = 3i + 2j + 5k.
>
> **Componentes del vector:**
>
> - **v₁:** componente en X (primera componente)
> - **v₂:** componente en Y (segunda componente)
> - **v₃:** componente en Z (tercera componente)
>
> **Propiedades geométricas:**
>
> - **Magnitud (norma):** ||**v**|| = √(v₁² + v₂² + v₃²)
> - **Dirección:** Determinada por las razones v₁:v₂:v₃
> - **Sentido:** Dado por los signos de las componentes

### 2️⃣ Base estándar (i, j, k)

> [!note] 📋 Definición — Base estándar (i, j, k)
>
> **La base estándar de ℝ³** la forman **i** = (1, 0, 0), **j** = (0, 1, 0), **k** = (0, 0, 1), los tres **vectores unitarios canónicos**, perpendiculares entre sí.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Base_estandar_01.svg]]
> **Se lee así:** tres ramas con **i**, **j**, **k**: cada una con su dirección canónica (X, Y, Z positivos), magnitud 1 y la propiedad de que cualquier vector se escribe como **v** = v₁**i** + v₂**j** + v₃**k**.
> **Por qué importa:** sin base hay que recordar las componentes "de memoria"; con base, toda componente es un coeficiente de su vector canónico.
> **Ejemplo:** en mecánica, **g** = −9.81**k** es la aceleración de la gravedad — una pura componente sobre **k**.
>
> **Vector i (dirección X):**
>
> - **i** = (1, 0, 0) = 1**i** + 0**j** + 0**k**
> - Magnitud: ||**i**|| = 1
> - Dirección: eje X positivo
>
> **Vector j (dirección Y):**
>
> - **j** = (0, 1, 0) = 0**i** + 1**j** + 0**k**
> - Magnitud: ||**j**|| = 1
> - Dirección: eje Y positivo
>
> **Vector k (dirección Z):**
>
> - **k** = (0, 0, 1) = 0**i** + 0**j** + 1**k**
> - Magnitud: ||**k**|| = 1
> - Dirección: eje Z positivo
>
> **Propiedades:**
>
> 1. Son **ortogonales** entre sí (perpendiculares)
> 2. Tienen **magnitud unitaria** (longitud = 1)
> 3. Forman una **base ortonormal** de ℝ³
> 4. Cualquier vector se puede expresar como combinación lineal de ellos
>
> **Ejemplo de descomposición:**
>
> **v** = (3, -2, 5) = 3**i** - 2**j** + 5**k**
>
> Esto significa:
>
> - 3 unidades en dirección de **i** (hacia X+)
> - 2 unidades en dirección opuesta a **j** (hacia Y-)
> - 5 unidades en dirección de **k** (hacia Z+)

### 3️⃣ Vector nulo

> [!note] 📋 Definición — Vector nulo
>
> **Definición:**
>
> **0** = (0, 0, 0) = 0**i** + 0**j** + 0**k**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Vector_nulo_01.svg]]
> **Se lee así:** un cuadro con el cero como raíz y cuatro hojas: **magnitud 0**, **sin dirección definida**, **neutro de la suma** (**v** + **0** = **v**) y **resultado** de **v** − **v**.
> **Por qué importa:** es el requisito de un espacio vectorial bien portado: sin neutro, las operaciones pierden cierre y el módulo de distancia ||\vec{u} − \vec{v}|| deja de ser simétrico respecto de 0.
> **Ejemplo:** el desplazamiento de una partícula que no se movió es **Δr** = **r₁** − **r₂** = **0**.
>
> **Características:**
>
> - **Única magnitud:** ||**0**|| = 0
> - **Sin dirección definida**
> - **Elemento neutro** de la suma: **v** + **0** = **v**
> - **Resultado** de: **v** - **v** = **0**
>
> **Propiedades:**
>
> - 0·**v** = **0** para todo vector **v**
> - **0** + **0** = **0**
> - Es el único vector con norma cero

### 4️⃣ Vector unitario

> [!note] 📋 Definición — Vector unitario
>
> **Definición:**
>
> Un vector **u** es **unitario** si ||**u**|| = 1
>
> **Cómo obtener un vector unitario:**
>
> Dado cualquier vector **v** ≠ **0**, su **vector unitario** en la misma dirección es:
>
> **û = v/||v|| = (1/||v||)·v**
>
> Este proceso se llama **normalización**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Vector_unitario_01.svg]]
> **Se lee así:** la cadena «v = (3, 4, 0) → ||v|| = √(9+16) = 5 → û = v/||v|| = (3/5, 4/5, 0) → verificación ||û|| = 1» — normalizar es dividir cada componente por la norma.
> **Por qué importa:** la dirección de una fuerza, de un rayo de luz o de la normal a un plano solo se codifica con un vector unitario — escalar la medida alteraría los cálculos de norma.
> **Ejemplo:** el vector normal a un plano n̂ = (0, −4, 3)/5 = (0, −0.8, 0.6), siempre unitario.
>
> **Ejemplo:**
>
> ```
> v = (3, 4, 0)
>
> ||v|| = √(9 + 16 + 0) = 5
>
> û = v/||v|| = (3/5, 4/5, 0)
>
> Verificación: ||û|| = √((3/5)² + (4/5)² + 0²)
>                     = √(9/25 + 16/25)
>                     = √(25/25) = 1 ✓
> ```
>
> **Aplicaciones:**
>
> - Representar direcciones puras (sin magnitud específica)
> - Normalizar vectores en computación gráfica
> - Definir bases ortonormales

### 5️⃣ Vector opuesto

> [!note] 📋 Definición — Vector opuesto
>
> **Definición:**
>
> El **vector opuesto** de **v** = (v₁, v₂, v₃) es:
>
> **-v = (-v₁, -v₂, -v₃)**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Vector_opuesto_01.svg]]
> **Se lee así:** la flecha **v** apuntando a un extremo, la misma flecha negada **−v** vuelven al origen: **misma magnitud y dirección, sentido contrario**, y \v avecesume con \v = 0.
> **Por qué importa:** el opuesto es el inverso aditivo de la suma; usarlo es la única vía rápida para "dirección opuesta" sin imposibles ideas sobre negatives, y es la clave del vector equilibrio.
> **Ejemplo:** el desplazamiento desde B hasta A siendo A\vec{B} el desplazamiento de A a B: B\vec{A} = −A\vec{B}.
>
> **Propiedades:**
>
> - Misma magnitud: ||**-v**|| = ||**v**||
> - Misma dirección
> - Sentido contrario
> - **v** + (-**v**) = **0**
>
> **Ejemplo:**
>
> ```
> v = (2, -3, 5)
> -v = (-2, 3, -5)
>
> v + (-v) = (2-2, -3+3, 5-5) = (0, 0, 0) = 0
> ```

### 6️⃣ Paralelismo

> [!note] 📋 Definición — Paralelismo
>
> **Definición:**
>
> Dos vectores **u** y **v** son **paralelos** si uno es múltiplo escalar del otro.
>
> **Condición matemática:**
>
> **u** ∥ **v** ⟺ ∃k ∈ ℝ tal que **u** = k**v**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Vectores_paralelos_01.svg]]
> **Se lee así:** con el signo de $k$ o con las razones $u_1/v_1 = u_2/v_2 = u_3/v_3$: si k > 0, **mismo sentido**; si k < 0, **sentidos opuestos**; y la verificación equivalente con componentes.
> **Por qué importa:** paralelismo es la prueba universal para detectar colinealidad y dependencia lineal sin resolver un sistema: dividir componentes basta.
> **Ejemplo:** (2, 4, 6) = 2·(1, 2, 3) → paralelos; (3, 6, 9) no con v = (1, 2, 4) porque 9/4 ≠ 3 — prueba en un segundo.
>
> **Método de verificación (componentes):**
>
> Si **u** = (u₁, u₂, u₃) y **v** = (v₁, v₂, v₃), entonces son paralelos si:
>
> **u₁/v₁ = u₂/v₂ = u₃/v₃ = k**
>
> (Siempre que los denominadores sean no nulos)
>
> **Ejemplos:**
>
> ```
> u = (2, 4, 6)
> v = (1, 2, 3)
>
> Verificación: 2/1 = 4/2 = 6/3 = 2
> Por lo tanto: u = 2v → Son paralelos ✓
>
> w = (3, -6, 9)
> Verificación: 3/1 = -6/2 = 9/3 = 3 (¡No!)
> -6/2 = -3 ≠ 3
> Por lo tanto: NO son paralelos con v
> ```

### 7️⃣ Colinealidad

> [!note] 📋 Definición — Colinealidad
>
> **Definición:**
>
> Tres puntos A, B, C son **colineales** si están sobre la misma recta.
>
> **Condición equivalente:**
>
> A, B, C son colineales ⟺ A\vec{B} ∥ A\vec{C}
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Colineales_01.svg]]
> **Se lee así:** tres puntos en una recta admite al más sencillo de los gráficos: A, B y C con A\vec{B} y A\vec{C} dibujados como flechas desde A — la condición es que una sea múltiplo de la otra.
> **Por qué importa:** detectar colinealidad es decidir si un ray tracing da con un objeto, si un GPS reporta un punto falso o si tres puntos no forman plano trivialmente.
> **Ejemplo:** A = (1, 2, 3), B = (2, 4, 5), C = (3, 6, 7): A\vec{B} = (1, 2, 2) y A\vec{C} = (2, 4, 4) = 2·A\vec{B} → colineales ✓.
>
> **Método de verificación:**
>
> Calcular A\vec{B} y A\vec{C}, luego verificar si uno es múltiplo del otro.
>
> **Ejemplo:**
>
> ```
> A = (1, 2, 3)
> B = (2, 4, 5)
> C = (3, 6, 7)
>
> A\vec{B} = (1, 2, 2)
> A\vec{C} = (2, 4, 4)
>
> A\vec{C} = 2·A\vec{B}  → Son colineales ✓
> ```

---

## 📍 Notación y Representación

### ✍️ Formas de Notación

> [!example] 📝 Convenciones de Escritura
>
> **Notaciones equivalentes para el mismo vector:**
>
> **1. Notación de flecha (más común):**
>
> - **v**, **u**, **w** (negrita)
> - \vec{v}, \vec{u}, \vec{w} (con flecha)
>
> **2. Notación con puntos (vector posición):**
>
> - **Desde el origen:** O\vec{P} donde P = (x, y, z)
> - **Entre dos puntos:** A\vec{B} desde A hasta B
>
> **3. Notación de componentes:**
>
> - **v** = ⟨v₁, v₂, v₃⟩ (paréntesis angulares)
> - **v** = (v₁, v₂, v₃) (paréntesis normales)
> - **v** = v₁**i** + v₂**j** + v₃**k** (combinación lineal)
>
> **Ejemplos concretos:**
>
> - **v** = (3, -2, 5)
> - **v** = 3**i** - 2**j** + 5**k**
> - **v** = ⟨3, -2, 5⟩
>
> **Todas representan el mismo vector**

### 🎨 Interpretación Geométrica

> [!tip] 👁️ Visualización de Vectores
>
> **Representación gráfica:**
>
> Un vector se dibuja como una **flecha** (segmento dirigido) donde:
>
> - **Punto inicial:** Origen del vector (cola)
> - **Punto final:** Extremo del vector (punta)
> - **Longitud de la flecha:** Magnitud del vector
> - **Dirección de la flecha:** Dirección y sentido del vector
>
> **Características importantes:**
>
> **1. Vectores libres:**
>
> - Un vector puede trasladarse paralelamente sin cambiar su identidad
> - **v** = (2, 3, 1) es el mismo desde (0,0,0) a (2,3,1) o desde (1,1,1) a (3,4,2)
>
> **2. Vector posición:**
>
> - Vector que va desde el origen O hasta un punto P
> - Si P = (x, y, z), entonces O\vec{P} = (x, y, z)
>
> **3. Equipolencia:**
>
> - Dos vectores son equipolentes si tienen la misma magnitud, dirección y sentido
> - Pueden tener diferentes puntos de aplicación

---

## ➕ Vector entre Dos Puntos

### 📏 Fórmula Fundamental

> [!warning] 🔷 Cálculo del Vector A\vec{B}
>
> **Dados dos puntos A y B en ℝ³:**
>
> - A = (x₁, y₁, z₁)
> - B = (x₂, y₂, z₂)
>
> **El vector que va de A hasta B es:**
>
> **A\vec{B} = B - A = (x₂ - x₁, y₂ - y₁, z₂ - z₁)**
>
> **Interpretación:**
>
> - Se **restan las coordenadas**: (coordenada final) - (coordenada inicial)
> - El vector "apunta" de A hacia B
> - La magnitud es la distancia entre A y B
>
> **Regla mnemotécnica:** **"Punto final MENOS punto inicial"**
>
> **Propiedades:**
>
> 1. **B\vec{A} = -A\vec{B}** (vector opuesto)
> 2. **A\vec{A} = (0, 0, 0) = 0⃗** (vector cero)
> 3. Si C es punto medio de AB, entonces A\vec{C} = ½A\vec{B}

### 📊 Ejemplos Detallados

> [!example] 🎯 Casos Prácticos
>
> **Ejemplo 1: Vector básico**
>
> Dados A = (1, 2, 3) y B = (4, 6, 8)
>
> Calcular A\vec{B}:
>
> ```
> A\vec{B} = B - A
>    = (4, 6, 8) - (1, 2, 3)
>    = (4-1, 6-2, 8-3)
>    = (3, 4, 5)
> ```
>
> **Interpretación:** Desde A, moverse 3 unidades en X, 4 en Y y 5 en Z para llegar a B
>
> ---
>
> **Ejemplo 2: Vector con componentes negativas**
>
> Dados C = (5, -2, 7) y D = (1, 3, 4)
>
> Calcular C\vec{D}:
>
> ```
> C\vec{D} = D - C
>    = (1, 3, 4) - (5, -2, 7)
>    = (1-5, 3-(-2), 4-7)
>    = (-4, 5, -3)
> ```
>
> **Interpretación:** Desde C, moverse -4 en X (hacia la izquierda), +5 en Y, -3 en Z (hacia abajo)
>
> ---
>
> **Ejemplo 3: Vector opuesto**
>
> Usando los puntos anteriores, calcular D\vec{C}:
>
> ```
> D\vec{C} = C - D
>    = (5, -2, 7) - (1, 3, 4)
>    = (4, -5, 3)
> ```
>
> **Verificación:** D\vec{C} = -C\vec{D} ✓
>
> ---
>
> **Ejemplo 4: Aplicación práctica**
>
> Un dron está en posición A = (10, 5, 20) metros y debe ir a B = (15, 12, 35) metros. ¿Qué vector de desplazamiento necesita?
>
> ```
> A\vec{B} = (15, 12, 35) - (10, 5, 20)
>    = (5, 7, 15) metros
> ```
>
> **Respuesta:** El dron debe desplazarse 5m al este, 7m al norte, y 15m hacia arriba

---

## 🔢 Componentes de un Vector

### 📦 Descomposición en Componentes

> [!success] 🟢 Análisis de Componentes
>
> **Dado un vector v = (v₁, v₂, v₃):**
>
> **1. Componente en X (v₁):**
>
> - Proyección del vector sobre el eje X
> - Distancia horizontal en dirección X
> - Se obtiene multiplicando: v₁ = ||v|| · cos(α) donde α es el ángulo con el eje X
>
> **2. Componente en Y (v₂):**
>
> - Proyección del vector sobre el eje Y
> - Distancia horizontal en dirección Y
> - Se obtiene multiplicando: v₂ = ||v|| · cos(β) donde β es el ángulo con el eje Y
>
> **3. Componente en Z (v₃):**
>
> - Proyección del vector sobre el eje Z
> - Altura vertical
> - Se obtiene multiplicando: v₃ = ||v|| · cos(γ) donde γ es el ángulo con el eje Z
>
> **Expresión con vectores unitarios:**
>
> **v** = v₁**i** + v₂**j** + v₃**k**
>
> Donde cada término representa la contribución en cada dirección

### 🔍 Propiedades de las Componentes

> [!tip] ⚡ Características Importantes
>
> **1. Independencia:**
>
> - Las componentes son independientes entre sí
> - Modificar una componente no afecta las otras
>
> **2. Aditividad:**
>
> - Si **u** = (u₁, u₂, u₃) y **v** = (v₁, v₂, v₃)
> - Entonces **u** + **v** = (u₁+v₁, u₂+v₂, u₃+v₃)
>
> **3. Escalamiento:**
>
> - Si k es un escalar: k**v** = (kv₁, kv₂, kv₃)
> - Multiplica cada componente por el escalar
>
> **4. Relación con la magnitud:**
>
> - ||**v**||² = v₁² + v₂² + v₃²
> - Es la suma de los cuadrados de las componentes
>
> **5. Componentes nulas:**
>
> - Si v₁ = 0: vector paralelo al plano YZ
> - Si v₂ = 0: vector paralelo al plano XZ
> - Si v₃ = 0: vector paralelo al plano XY

---

## 📐 Magnitud (Norma) de un Vector

### 📏 Definición y Cálculo

> [!warning] 🔶 Longitud del Vector
>
> **Dado un vector v = (v₁, v₂, v₃):**
>
> **La magnitud o norma del vector es:**
>
> **||v|| = √(v₁² + v₂² + v₃²)**
>
> También se denota como |**v**| o simplemente ||**v**||
>
> **Interpretación geométrica:**
>
> - Es la **longitud** del vector
> - Distancia desde el origen hasta el punto (v₁, v₂, v₃)
> - Siempre es un número **no negativo**: ||**v**|| ≥ 0
> - ||**v**|| = 0 si y solo si **v** = **0** (vector cero)
>
> **Propiedades fundamentales:**
>
> 1. **Positividad:** ||**v**|| > 0 si **v** ≠ **0**
> 2. **Homogeneidad:** ||k**v**|| = |k| · ||**v**||
> 3. **Desigualdad triangular:** ||**u** + **v**|| ≤ ||**u**|| + ||**v**||
>
> **Origen de la fórmula:** Se deriva del teorema de Pitágoras aplicado en tres dimensiones

### 📊 Ejemplos de Cálculo de Magnitud

> [!example] 🎯 Ejercicios Resueltos
>
> **Ejemplo 1: Vector básico**
>
> **v** = (3, 4, 0)
>
> ```
>
> ||v|| = √(3² + 4² + 0²)
>      = √(9 + 16 + 0)
>      = √25
>      = 5
> ```
>
> ---
>
> **Ejemplo 2: Vector con todas las componentes**
>
> **w** = (2, -3, 6)
>
> ```
>
> ||w|| = √(2² + (-3)² + 6²)
>      = √(4 + 9 + 36)
>      = √49
>      = 7
> ```
>
> ---
>
> **Ejemplo 3: Vector unitario**
>
> **u** = (1/√3, 1/√3, 1/√3)
>
> ```
>
> ||u|| = √((1/√3)² + (1/√3)² + (1/√3)²)
>      = √(1/3 + 1/3 + 1/3)
>      = √1
>      = 1
> ```
>
> Este es un **vector unitario** (magnitud = 1)
>
> ---
>
> **Ejemplo 4: Aplicación práctica**
>
> Un avión se desplaza desde A = (0, 0, 0) hasta B = (300, 400, 100) kilómetros. ¿Qué distancia recorrió?
>
> ```
> A\vec{B} = (300, 400, 100)
> Distancia = ||A\vec{B}|| = √(300² + 400² + 100²)
>                     = √(90000 + 160000 + 10000)
>                     = √260000
>                     ≈ 509.9 km
> ```

---

## 🧮 Operaciones con Vectores

### ➕ Suma de Vectores

> [!success] ➕ Operación Fundamental
>
> **Dados u = (u₁, u₂, u₃) y v = (v₁, v₂, v₃):**
>
> **u + v = (u₁ + v₁, u₂ + v₂, u₃ + v₃)**
>
> Se suman **componente a componente**
>
> **Interpretación geométrica:**
>
> - **Regla del paralelogramo:** Los vectores forman los lados de un paralelogramo
> - **Regla del triángulo:** Colocar el segundo vector al final del primero
>
> **Propiedades algebraicas:**
>
> 1. **Conmutativa:** **u** + **v** = **v** + **u**
> 2. **Asociativa:** (**u** + **v**) + **w** = **u** + (**v** + **w**)
> 3. **Elemento neutro:** **v** + **0** = **v**
> 4. **Elemento opuesto:** **v** + (-**v**) = **0**
>
> **Ejemplo:**
>
> ```
> u = (2, 3, -1)
> v = (1, -2, 4)
> u + v = (2+1, 3+(-2), -1+4)
>       = (3, 1, 3)
> ```

### ➖ Resta de Vectores

> [!note] ➖ Diferencia de Vectores
>
> **Dados u = (u₁, u₂, u₃) y v = (v₁, v₂, v₃):**
>
> **u - v = (u₁ - v₁, u₂ - v₂, u₃ - v₃)**
>
> **Equivalencia:** **u** - **v** = **u** + (-**v**)
>
> **Interpretación geométrica:**
>
> - Vector que va desde la punta de **v** hasta la punta de **u**
> - Si ambos parten del origen
>
> **Ejemplo:**
>
> ```
> u = (5, 2, 7)
> v = (3, 1, 4)
> u - v = (5-3, 2-1, 7-4)
>       = (2, 1, 3)
> ```

### ✖️ Multiplicación por Escalar

> [!info] ✖️ Escalamiento de Vectores
>
> **Dado un vector v = (v₁, v₂, v₃) y un escalar k ∈ ℝ:**
>
> **k·v = (k·v₁, k·v₂, k·v₃)**
>
> **Efecto geométrico:**
>
> - Si k > 0: **Estira** el vector (si k > 1) o **contrae** (si 0 < k < 1)
> - Si k < 0: **Invierte el sentido** y escala por |k|
> - Si k = 0: Resulta en el vector cero
>
> **Propiedades:**
>
> 1. **Asociativa:** k(m**v**) = (km)**v**
> 2. **Distributiva 1:** (k + m)**v** = k**v** + m**v**
> 3. **Distributiva 2:** k(**u** + **v**) = k**u** + k**v**
> 4. **Identidad:** 1·**v** = **v**
>
> **Ejemplo:**
>
> ```
> v = (2, -3, 4)
> 3v = (3·2, 3·(-3), 3·4)
>    = (6, -9, 12)
>
> -2v = (-2·2, -2·(-3), -2·4)
>     = (-4, 6, -8)
> ```

---

## 🎯 Vectores Especiales

> [!tip] 🔹 Vectores especiales y qué tienen en común
>
> El **vector nulo**, los **unitarios**, los **opuestos** y los **paralelos** son herramientas del mismo juego: son atajos para medir, comparar y componer vectores. Todo el resto del capítulo se apoya en ellos.

---

## 🎨 Diagrama de Conceptos Vectoriales

> [!note] 🗺️ Mapa de la nota
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Vectores_en_R3_01.svg]]
> **Se lee así:** «Vector en ℝ³» se ramifica en tres: **Componentes** (v = (x, y, z), proyecciones sobre los ejes, base canónica), **Magnitud** (|v| = √(x²+y²+z²), vector unitario v/|v|, ángulo con cada eje) y **Vector opuesto** (−v invierte las componentes, misma magnitud y dirección, v + (−v) = 0).
> **Por qué importa:** es la estructura completa de la nota en un solo vistazo — agrupa lo que necesitas saber sobre vectores y cómo cada rama conecta: norma ↔ unitario ↔ opuesto.
> **Ejemplo:** calcula a mano llévate \|(1, 2, 2)\|, el \^u de cada eje y el opuesto de cada vector — obtendrás las tres ramas.

---

## 🧪 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> **Nivel 1 - Básico** 🟢
>
> Dados A = (2, 1, 3) y B = (5, 4, 7), calcular:
> a) A\vec{B} · b) B\vec{A} · c) ||A\vec{B}||
>
> > [!success]- ✅ Solución
> >
> > a) A\vec{B} = (5−2, 4−1, 7−3) = (3, 3, 4)
> > b) B\vec{A} = (2−5, 1−4, 3−7) = (−3, −3, −4) = −A\vec{B}
> > c) ||A\vec{B}|| = √(9 + 9 + 16) = √34 ≈ 5.83
> >
> > **Lección:** A\vec{B} = −B\vec{A} siempre — el sentido cambia, la distancia no.

> [!example] 📋 Planteamiento
>
> Expresa **v** = (4, −2, 6) en términos de **i**, **j**, **k**.
>
> > [!success]- ✅ Solución
> >
> > **v** = 4**i** − 2**j** + 6**k**
> >
> > **Lección:** la combinación lineal con la base canónica es el mismo objeto que la terna — no hay "versión simplificada", solo distintas formas de escribirlo.

> [!example] 📋 Planteamiento
>
> **Nivel 2 - Intermedio** 🟡
>
> Dados **u** = (1, 2, −1) y **v** = (3, −1, 2), calcular:
> a) **u** + **v** · b) 2**u** − 3**v** · c) ||**u** + **v**||
>
> > [!success]- ✅ Solución
> >
> > a) **u** + **v** = (1+3, 2−1, −1+2) = (4, 1, 1)
> > b) 2**u** − 3**v** = (2, 4, −2) − (9, −3, 6) = (−7, 7, −8)
> > c) ||**u** + **v**|| = ||(4, 1, 1)|| = √(16+1+1) = √18 = 3√2
> >
> > **Lección:** componente a componente primero, raíz y cancela después — nunca memorices los resultados intermedios.

> [!example] 📋 Planteamiento
>
> Encuentra un vector unitario en la dirección de **w** = (2, −2, 1).
>
> > [!success]- ✅ Solución
> >
> > ||w|| = √(4 + 4 + 1) = √9 = 3
> > ŵ = w/||w|| = (2/3, −2/3, 1/3)
> > Verificación: ||(2/3, −2/3, 1/3)|| = √(4/9 + 4/9 + 1/9) = √(9/9) = 1 ✓
> >
> > **Lección:** siempre verifica ||û|| = 1 — si no cuadra, la división entre la norma está mal.

> [!example] 📋 Planteamiento
>
> **Nivel 3 - Avanzado** 🔴
>
> Dados A = (1, 0, 2), B = (3, 4, 1) y C = (−1, 2, 3):
> a) Calcular A\vec{B} + A\vec{C}
> b) Encontrar el punto D tal que ABCD es un paralelogramo
>
> > [!success]- ✅ Solución
> >
> > a) A\vec{B} = (3−1, 4−0, 1−2) = (2, 4, −1)
> >    A\vec{C} = (−1−1, 2−0, 3−2) = (−2, 2, 1)
> >    A\vec{B} + A\vec{C} = (2−2, 4+2, −1+1) = (0, 6, 0)
> >
> > b) En un paralelogramo ABCD: \vec{AB} = \vec{DC}, es decir D = A + C − B
> >    D = (1, 0, 2) + (−1, 2, 3) − (3, 4, 1) = (−3, −2, 4)
> >
> > **Lección:** en un paralelogramo, \vec{AB} \vec{DC} apunta de D hacia C — por eso est D: D = A + C − B.

> [!example] 📋 Planteamiento
>
> Un drone parte de (0, 0, 50) m debe recoger un paquete en (100, 80, 30) y entregarlo en (150, 120, 40):
> a) Vector desplazamiento total
> b) Distancia total recorrida
>
> > [!success]- ✅ Solución
> >
> > Origen O = (0, 0, 50) · Recogida P = (100, 80, 30) · Entrega E = (150, 120, 40)
> >
> > a) Vector total: O\vec{E} = (150, 120, 40) − (0, 0, 50) = **(150, 120, −10) metros**
> >
> > b) Trayectoria: O → P → E
> >
> >    O\vec{P} = (100, 80, −20)
> >    ||O\vec{P}|| = √(10000 + 6400 + 400) = √16800 ≈ 129.6 m
> >
> >    P\vec{E} = (50, 40, 10)
> >    ||P\vec{E}|| = √(2500 + 1600 + 100) = √4200 ≈ 64.8 m
> >
> >    Distancia total = 129.6 + 64.8 ≈ **194.4 metros**
> >
> > **Lección:** el desplazamiento total no depende de la ruta — la trayectoria sí: aquí se recorre O→P→E, no O→E directamente.

---

## 🔗 Propiedades Algebraicas Completas

> [!note] 🔢 Axiomas del Espacio Vectorial ℝ³
>
> **ℝ³ con las operaciones de suma (+) y multiplicación escalar (·) forma un espacio vectorial:**
>
> **A. Propiedades de la suma:**
>
> 1. **Cerradura:** ∀**u**, **v** ∈ ℝ³ ⟹ **u** + **v** ∈ ℝ³
> 2. **Conmutativa:** **u** + **v** = **v** + **u**
> 3. **Asociativa:** (**u** + **v**) + **w** = **u** + (**v** + **w**)
> 4. **Elemento neutro:** ∃**0** tal que **v** + **0** = **v**
> 5. **Elemento inverso:** ∀**v** ∃(-**v**) tal que **v** + (-**v**) = **0**
>
> **B. Propiedades de la multiplicación escalar:**
>
> 6. **Cerradura:** ∀k ∈ ℝ, **v** ∈ ℝ³ ⟹ k**v** ∈ ℝ³
> 7. **Distributiva 1:** k(**u** + **v**) = k**u** + k**v**
> 8. **Distributiva 2:** (k + m)**v** = k**v** + m**v**
> 9. **Asociativa mixta:** k(m**v**) = (km)**v**
> 10. **Elemento identidad:** 1·**v** = **v**
>
> Estas propiedades hacen de ℝ³ un **espacio vectorial real de dimensión 3**

---

## 💡 Consejos de Estudio y Errores Comunes

> [!tip] 🧠 Estrategias de Aprendizaje
>
> **Para dominar vectores:**
>
> **1. Visualización:**
>
> - Dibujar constantemente vectores en 3D
> - Usar software: GeoGebra 3D, Desmos
> - Construir modelos físicos con flechas
>
> **2. Práctica de cálculos:**
>
> - Hacer muchos ejercicios de componentes
> - Verificar respuestas calculando magnitudes
> - Comprobar paralelismo en ejemplos
>
> **3. Conexión con aplicaciones:**
>
> - Pensar en términos de desplazamiento
> - Relacionar con fuerzas y velocidades
> - Implementar en código
>
> **Errores comunes a evitar:**
>
> ❌ **Error 1:** Confundir punto con vector
>
> - (2, 3, 4) puede ser punto P o vector **v**
> - Contexto determina la interpretación
>
> ❌ **Error 2:** Orden en resta de puntos
>
> - A\vec{B} = B - A (NO A - B)
> - Mnemotecnia: "final menos inicial"
>
> ❌ **Error 3:** Olvidar raíz cuadrada en magnitud
>
> - ||**v**|| = √(v₁² + v₂² + v₃²) ✓
> - ||**v**|| = v₁² + v₂² + v₃² ❌
>
> ❌ **Error 4:** Sumar vector con escalar
>
> - k + **v** NO tiene sentido
> - Solo se puede: k·**v** o **u** + **v**
>
> ❌ **Error 5:** Dividir entre vector
>
> - **u**/**v** NO está definido
> - Solo: k/**v** si pensamos en (1/k)**v**

---

## 📊 Tabla Resumen de Vectores

> [!example] 📋 Compendio Completo
>
> | Concepto | Notación | Fórmula | Ejemplo |
> |---|---|---|---|
> | **Vector** | **v**, \vec{v} | (v₁, v₂, v₃) | (3, -2, 5) |
> | **Magnitud** | \|**v**\| | √(v₁² + v₂² + v₃²) | √(9+4+25) = √38 |
> | **Vector entre puntos** | A\vec{B} | B - A | (5,2,7)-(1,3,4)=(4,-1,3) |
> | **Suma** | **u** + **v** | (u₁+v₁, u₂+v₂, u₃+v₃) | (1,2,3)+(4,5,6)=(5,7,9) |
> | **Resta** | **u** - **v** | (u₁-v₁, u₂-v₂, u₃-v₃) | (5,7,9)-(1,2,3)=(4,5,6) |
> | **Mult. escalar** | k**v** | (kv₁, kv₂, kv₃) | 3(1,2,3)=(3,6,9) |
> | **Vector unitario** | û | **v**/\|**v**\| | (3,4,0)/5=(3/5,4/5,0) |
> | **Vectores base** | **i**, **j**, **k** | (1,0,0), (0,1,0), (0,0,1) | **v**=3**i**-2**j**+5**k** |
> | **Vector cero** | **0** | (0, 0, 0) | Elemento neutro |
> | **Vector opuesto** | -**v** | (-v₁, -v₂, -v₃) | -(2,3,1)=(-2,-3,-1) |
> | **Paralelismo** | **u** ∥ **v** | **u** = k**v** | (2,4,6) = 2(1,2,3) |

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo el mismo vector en las tres formas (terna, columna, combinación i j k).
> - [ ] Calculo la magnitud con \|**v**\| = √(v₁² + v₂² + v₃²).
>
> [!note] 📋 Nivel Intermedio
>
> - [ ] Normalizo un vector no nulo dividiendo entre su norma y verifico que el resultado queda unitario.
> - [ ] Decido paralelismo por las razones u₁/v₁ = u₂/v₂ = u₃/v₃.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas con desplazamiento, velocidad y posición en ℝ³ vinculando vector y física.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Calculus*, cap. 12 «Vectors and the Geometry of Space»: vectores, norma, operaciones en ℝ³.
> - Syllabus oficial MATG1046 «Cálculo Vectorial», ESPOL — Unidad 1 (Geometría Analítica en ℝ³).
> - Apuntes del curso MATG1046 y las figuras de la propia materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR

#flashcards/calcvec-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es un vector unitario?::Un vector con norma 1: \hat{v} = v/||v|| (para v ≠ 0).
> - ¿Cómo decidir paralelismo con componentes?::Si u₁/v₁ = u₂/v₂ = u₃/v₃ = k, son paralelos.
> - ¿Tres puntos A, B, C son colineales?::A\vec{B} ∥ A\vec{C} — uno es múltiplo escalar del otro.
> - ¿La magnitud del vector opuesto?::Igual que la de v: ||−v|| = ||v||.

---

## 🔗 Conexiones

> [!quote] 🌟 Enlaces Conceptuales
>
> **Prerequisites (Prerrequisitos):**
>
> - [[01 - Sistema de referencia espacial en R3]] — Base del espacio ℝ³
> - [[02 - Vectores en R3]] — Componentes de vectores
> - Álgebra Básica — Operaciones fundamentales
>
> **Temas siguientes:**
>
> - [[01 - Distancias en ℝ³]] — Usa magnitud de vectores
> - [[01 - Rectas en R3]] — Ecuaciones vectoriales de rectas
> - [[02 - Planos en R3]] — Vectores normales a planos
>
> **Operaciones avanzadas:**
>
> - [[01 – Producto punto y ángulos]] — Proyecciones y ángulos
> - [[02 – Producto cruz y áreas]] — Vector perpendicular
> - Producto Triple — Volumen de paralelepípedos
>
> **Aplicaciones:**
>
> - Cinemática Vectorial — Movimiento en el espacio
> - Fuerzas y Equilibrio — Estática vectorial
> - [[01 – Transformaciones lineales]] — Matrices y vectores
>
> **Temas relacionados:**
>
> - [[01 - Subespacios Vectoriales]] — Generalización abstracta
> - [[02 – Base y dimensión]] — Vectores linealmente independientes
> - [[Álgebra Lineal]] — Teoría completa

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - El vector unitario como "tarjeta de dirección": si solo te importa hacia dónde apunta, descarta la magnitud y conserva dirección con \hat{v}.
> - Siguiente nota: [[01 – Producto punto y ángulos]] — la métrica angular entre vectores (coseno del ángulo).
> - Repasa los tres vectores canónicos y su propiedad de base ortonormal antes de continuar.

---

**Tags:** #MATG1046 #unidad1 #vectores #R3 #magnitud-vector #componentes #vectores-unitarios

# ➡️ Vectores en ℝ³

## 🎯 Fundamentos de Vectores en el Espacio

> [!info]- 💡 Introducción a los Vectores Tridimensionales Los **vectores en ℝ³** son magnitudes que poseen tanto **magnitud** (tamaño o longitud) como **dirección** y **sentido** en el espacio tridimensional. Son fundamentales para describir desplazamientos, fuerzas, velocidades y muchas otras cantidades físicas.
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

### 📐 Definición Formal de Vector

> [!note]- 🌟 Concepto Matemático de Vector **Definición:**
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
> Donde:
> 
> - **i** = (1, 0, 0) — vector unitario en dirección del eje X
> - **j** = (0, 1, 0) — vector unitario en dirección del eje Y
> - **k** = (0, 0, 1) — vector unitario en dirección del eje Z
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

## 📍 Notación y Representación

### ✍️ Formas de Notación

> [!example]- 📝 Convenciones de Escritura **Notaciones equivalentes para el mismo vector:**
> 
> **1. Notación de flecha (más común):**
> 
> - **v**, **u**, **w** (negrita)
> - v⃗, u⃗, w⃗ (con flecha)
> 
> **2. Notación con puntos (vector posición):**
> 
> - **Desde el origen:** OP⃗ donde P = (x, y, z)
> - **Entre dos puntos:** AB⃗ desde A hasta B
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

> [!tip]- 👁️ Visualización de Vectores **Representación gráfica:**
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
> - Si P = (x, y, z), entonces OP⃗ = (x, y, z)
> 
> **3. Equipolencia:**
> 
> - Dos vectores son equipolentes si tienen la misma magnitud, dirección y sentido
> - Pueden tener diferentes puntos de aplicación

## ➕ Vector entre Dos Puntos

### 📏 Fórmula Fundamental

> [!warning]- 🔷 Cálculo del Vector AB⃗ **Dados dos puntos A y B en ℝ³:**
> 
> - A = (x₁, y₁, z₁)
> - B = (x₂, y₂, z₂)
> 
> **El vector que va de A hasta B es:**
> 
> **AB⃗ = B - A = (x₂ - x₁, y₂ - y₁, z₂ - z₁)**
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
> 1. **BA⃗ = -AB⃗** (vector opuesto)
> 2. **AA⃗ = (0, 0, 0) = 0⃗** (vector cero)
> 3. Si C es punto medio de AB, entonces AC⃗ = ½AB⃗

### 📊 Ejemplos Detallados

> [!example]- 🎯 Casos Prácticos **Ejemplo 1: Vector básico**
> 
> Dados A = (1, 2, 3) y B = (4, 6, 8)
> 
> Calcular AB⃗:
> 
> ```
> AB⃗ = B - A
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
> Calcular CD⃗:
> 
> ```
> CD⃗ = D - C
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
> Usando los puntos anteriores, calcular DC⃗:
> 
> ```
> DC⃗ = C - D
>    = (5, -2, 7) - (1, 3, 4)
>    = (4, -5, 3)
> ```
> 
> **Verificación:** DC⃗ = -CD⃗ ✓
> 
> ---
> 
> **Ejemplo 4: Aplicación práctica**
> 
> Un dron está en posición A = (10, 5, 20) metros y debe ir a B = (15, 12, 35) metros. ¿Qué vector de desplazamiento necesita?
> 
> ```
> AB⃗ = (15, 12, 35) - (10, 5, 20)
>    = (5, 7, 15) metros
> ```
> 
> **Respuesta:** El dron debe desplazarse 5m al este, 7m al norte, y 15m hacia arriba

## 🔢 Componentes de un Vector

### 📦 Descomposición en Componentes

> [!success]- 🟢 Análisis de Componentes **Dado un vector v = (v₁, v₂, v₃):**
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

### 🎯 Vectores Unitarios Canónicos

> [!note]- 📏 Base Estándar de ℝ³ **Los tres vectores fundamentales:**
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

### 🔍 Propiedades de las Componentes

> [!tip]- ⚡ Características Importantes **1. Independencia:**
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

## 📐 Magnitud (Norma) de un Vector

### 📏 Definición y Cálculo

> [!warning]- 🔶 Longitud del Vector **Dado un vector v = (v₁, v₂, v₃):**
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

> [!example]- 🎯 Ejercicios Resueltos **Ejemplo 1: Vector básico**
> 
> **v** = (3, 4, 0)
> 
> ```
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
> AB⃗ = (300, 400, 100)
> Distancia = ||AB⃗|| = √(300² + 400² + 100²)
>                     = √(90000 + 160000 + 10000)
>                     = √260000
>                     ≈ 509.9 km
> ```

## 🧮 Operaciones con Vectores

### ➕ Suma de Vectores

> [!success]- ➕ Operación Fundamental **Dados u = (u₁, u₂, u₃) y v = (v₁, v₂, v₃):**
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

> [!note]- ➖ Diferencia de Vectores **Dados u = (u₁, u₂, u₃) y v = (v₁, v₂, v₃):**
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

> [!info]- ✖️ Escalamiento de Vectores **Dado un vector v = (v₁, v₂, v₃) y un escalar k ∈ ℝ:**
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

## 🎯 Vectores Especiales

### 🔵 Vector Cero

> [!warning]- ⭕ El Vector Nulo **Definición:**
> 
> **0** = (0, 0, 0) = 0**i** + 0**j** + 0**k**
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

### 🎯 Vectores Unitarios

> [!success]- 📏 Vectores de Magnitud 1 **Definición:**
> 
> Un vector **u** es **unitario** si ||**u**|| = 1
> 
> **Cómo obtener un vector unitario:**
> 
> Dado cualquier vector **v** ≠ **0**, su **vector unitario** en la misma dirección es:
> 
> **û = v/||v|| = (1/||v||)·v**
> 
> Este proceso se llama **normalización**
> 
> **Ejemplo:**
> 
> ```
> v = (3, 4, 0)
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

### ↔️ Vectores Opuestos

> [!note]- 🔄 Inversión de Sentido **Definición:**
> 
> El **vector opuesto** de **v** = (v₁, v₂, v₃) es:
> 
> **-v = (-v₁, -v₂, -v₃)**
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

## 🎨 Diagrama de Conceptos Vectoriales

```mermaid
graph TD
    A[Vectores en ℝ³] --> B[Representación]
    A --> C[Operaciones]
    A --> D[Propiedades]
    
    B --> B1[Componentes<br/>v₁, v₂, v₃]
    B --> B2[Notación<br/>v, v⃗, ⟨v₁,v₂,v₃⟩]
    B --> B3[Base canónica<br/>i, j, k]
    
    C --> C1[Suma/Resta<br/>u ± v]
    C --> C2[Mult. escalar<br/>k·v]
    C --> C3[Magnitud<br/>||v||]
    
    D --> D1[Vector entre puntos<br/>AB⃗ = B - A]
    D --> D2[Vector unitario<br/>û = v/||v||]
    D --> D3[Vector cero<br/>0 = 0,0,0]
    
    style A fill:#e3f2fd
    style B fill:#e8f5e9
    style C fill:#fff3e0
    style D fill:#f3e5f5
    style B1 fill:#c8e6c9
    style C1 fill:#ffe082
    style D1 fill:#ce93d8
```

## 🧪 Ejercicios Integrales

> [!example]- 💪 Práctica Completa **Nivel 1 - Básico:** 🟢
> 
> 1. Dados A = (2, 1, 3) y B = (5, 4, 7), calcular:
>     - a) AB⃗
>     - b) BA⃗
>     - c) ||AB⃗||
> 
> **Solución:**
> 
> ```
> a) AB⃗ = (5-2, 4-1, 7-3) = (3, 3, 4)
> b) BA⃗ = (2-5, 1-4, 3-7) = (-3, -3, -4) = -AB⃗
> c) ||AB⃗|| = √(9 + 9 + 16) = √34 ≈ 5.83
> ```
> 
> 2. Expresar **v** = (4, -2, 6) en términos de **i**, **j**, **k**:
> 
> **Solución:** **v** = 4**i** - 2**j** + 6**k**
> 
> ---
> 
> **Nivel 2 - Intermedio:** 🟡
> 
> 3. Dados **u** = (1, 2, -1) y **v** = (3, -1, 2), calcular:
>     - a) **u** + **v**
>     - b) 2**u** - 3**v**
>     - c) ||**u** + **v**||
> 
> **Solución:**
> 
> ```
> a) u + v = (1+3, 2-1, -1+2) = (4, 1, 1)
> 
> b) 2u - 3v = 2(1,2,-1) - 3(3,-1,2)
>            = (2,4,-2) - (9,-3,6)
>            = (2-9, 4-(-3), -2-6)
>            = (-7, 7, -8)
> 
> c) ||u+v|| = ||(4,1,1)|| = √(16+1+1) = √18 = 3√2
> ```
> 
> 4. Encontrar un vector unitario en la dirección de **w** = (2, -2, 1):
> 
> **Solución:**
> 
> ```
> ||w|| = √(4 + 4 + 1) = √9 = 3
> ŵ = w/||w|| = (2/3, -2/3, 1/3)
> 
> Verificación: ||(2/3, -2/3, 1/3)|| = √(4/9 + 4/9 + 1/9)
>                                     = √(9/9) = 1 ✓
> ```
> 
> ---
> 
> **Nivel 3 - Avanzado:** 🔴
> 
> 5. Dados A = (1, 0, 2), B = (3, 4, 1) y C = (-1, 2, 3):
>     - a) Calcular AB⃗ + AC⃗
>     - b) Encontrar el punto D tal que ABCD es un paralelogramo
> 
> **Solución:**
> 
> ```
> a) AB⃗ = (3-1, 4-0, 1-2) = (2, 4, -1)
>    AC⃗ = (-1-1, 2-0, 3-2) = (-2, 2, 1)
>    AB⃗ + AC⃗ = (2-2, 4+2, -1+1) = (0, 6, 0)
> 
> b) En un paralelogramo: AB⃗ = DC⃗
>    Entonces: D + AB⃗ = C
>    D = C - AB⃗ = (-1, 2, 3) - (2, 4, -1)
>    D = (-3, -2, 4)
> ```
> 
> 6. Problema aplicado: Un drone parte de la posición (0, 0, 50) metros y debe recoger un paquete en (100, 80, 30) y entregarlo en (150, 120, 40). Calcular:
>     - a) Vector desplazamiento total
>     - b) Distancia total recorrida
> 
> **Solución:**
> 
> ```
> Origen O = (0, 0, 50)
> Punto de recogida P = (100, 80, 30)
> Punto de entrega E = (150, 120, 40)
> 
> a) Vector total: OE⃗ = (150, 120, 40) - (0, 0, 50)
>                     = (150, 120, -10) metros
> 
> b) Trayectoria: O → P → E
>    
>    OP⃗ = (100, 80, -20)
>    ||OP⃗|| = √(10000 + 6400 + 400) = √16800 ≈ 129.6 m
>    
>    PE⃗ = (50, 40, 10)
>    ||PE⃗|| = √(2500 + 1600 + 100) = √4200 ≈ 64.8 m
>    
>    Distancia total = 129.6 + 64.8 = 194.4 metros
> ```

## 🔍 Vectores Paralelos y Colineales

### ↕️ Definición de Paralelismo

> [!warning]- 📏 Vectores con la Misma Dirección **Definición:**
> 
> Dos vectores **u** y **v** son **paralelos** si uno es múltiplo escalar del otro.
> 
> **Condición matemática:**
> 
> **u** ∥ **v** ⟺ ∃k ∈ ℝ tal que **u** = k**v**
> 
> **Casos especiales:**
> 
> - Si k > 0: **mismo sentido**
> - Si k < 0: **sentidos opuestos**
> - Si k = 0: uno es el vector cero
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

### 🔗 Puntos Colineales

> [!tip]- 📍 Tres Puntos en Línea Recta **Definición:**
> 
> Tres puntos A, B, C son **colineales** si están sobre la misma recta.
> 
> **Condición equivalente:**
> 
> A, B, C son colineales ⟺ AB⃗ ∥ AC⃗
> 
> **Método de verificación:**
> 
> Calcular AB⃗ y AC⃗, luego verificar si uno es múltiplo del otro.
> 
> **Ejemplo:**
> 
> ```
> A = (1, 2, 3)
> B = (2, 4, 5)
> C = (3, 6, 7)
> 
> AB⃗ = (1, 2, 2)
> AC⃗ = (2, 4, 4)
> 
> AC⃗ = 2·AB⃗  → Son colineales ✓
> ```

## 🌐 Aplicaciones de Vectores

### 🎮 En Computación Gráfica

> [!success]- 💻 Modelado y Animación 3D **Usos fundamentales:**
> 
> **1. Representación de posiciones:**
> 
> - Cada vértice de un modelo 3D: vector posición
> - Cámaras y objetos: vectores de ubicación
> 
> **2. Direcciones de movimiento:**
> 
> - Velocidad de personajes: vector velocidad
> - Trayectorias: secuencias de vectores
> 
> **3. Iluminación:**
> 
> - Vectores normales a superficies
> - Dirección de rayos de luz
> 
> **Ejemplo en código:**
> 
> ```python
> class Vector3D:
>     def __init__(self, x, y, z):
>         self.x = x
>         self.y = y
>         self.z = z
>     
>     def __add__(self, otro):
>         return Vector3D(
>             self.x + otro.x,
>             self.y + otro.y,
>             self.z + otro.z
>         )
>     
>     def magnitud(self):
>         return (self.x**2 + self.y**2 + self.z**2)**0.5
>     
>     def normalizar(self):
>         mag = self.magnitud()
>         if mag > 0:
>             return Vector3D(
>                 self.x/mag,
>                 self.y/mag,
>                 self.z/mag
>             )
>         return Vector3D(0, 0, 0)
> 
> # Uso
> posicion = Vector3D(10, 5, 20)
> velocidad = Vector3D(2, 0, -1)
> nueva_posicion = posicion + velocidad
> 
> print(f"Nueva posición: ({nueva_posicion.x}, "
>       f"{nueva_posicion.y}, {nueva_posicion.z})")
> # Salida: Nueva posición: (12, 5, 19)
> ```

### ⚡ En Física

> [!note]- 🔬 Magnitudes Vectoriales **Aplicaciones principales:**
> 
> **1. Cinemática:**
> 
> - **Posición:** r⃗(t) = (x(t), y(t), z(t))
> - **Velocidad:** v⃗ = dr⃗/dt
> - **Aceleración:** a⃗ = dv⃗/dt
> 
> **2. Dinámica:**
> 
> - **Fuerza:** F⃗ = m·a⃗ (Segunda Ley de Newton)
> - **Momento:** p⃗ = m·v⃗
> - **Impulso:** J⃗ = Δp⃗
> 
> **3. Campo vectorial:**
> 
> - **Campo eléctrico:** E⃗
> - **Campo magnético:** B⃗
> - **Campo gravitatorio:** g⃗
> 
> **Ejemplo práctico:**
> 
> ```
> Un objeto se mueve con:
> - Posición inicial: r⃗₀ = (0, 0, 100) m
> - Velocidad: v⃗ = (50, 30, -10) m/s
> 
> Después de t = 2 segundos:
> r⃗(2) = r⃗₀ + v⃗·t
>       = (0, 0, 100) + 2(50, 30, -10)
>       = (0, 0, 100) + (100, 60, -20)
>       = (100, 60, 80) m
> ```

### 🛩️ En Ingeniería y Navegación

> [!info]- 🧭 Aplicaciones Prácticas **1. Navegación aérea:**
> 
> - Rumbo de avión: vector dirección
> - Velocidad del viento: vector que se suma/resta
> - Velocidad resultante: suma vectorial
> 
> **Ejemplo:**
> 
> ```
> Velocidad del avión: v⃗ₐ = (400, 0, 0) km/h (hacia el este)
> Velocidad del viento: v⃗ᵥ = (0, 50, 0) km/h (hacia el norte)
> Velocidad resultante: v⃗ᵣ = (400, 50, 0) km/h
> 
> Magnitud: ||v⃗ᵣ|| = √(400² + 50²) ≈ 403.1 km/h
> ```
> 
> **2. Estructuras:**
> 
> - Fuerzas en vigas y columnas
> - Tensiones en cables
> - Momentos y torques
> 
> **3. Robótica:**
> 
> - Posición del efector final
> - Trayectorias de movimiento
> - Control de velocidad

## 📚 Propiedades Algebraicas Completas

> [!note]- 🔢 Axiomas del Espacio Vectorial ℝ³ **ℝ³ con las operaciones de suma (+) y multiplicación escalar (·) forma un espacio vectorial:**
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

## 🔗 Conexiones con el Sistema de Notas

> [!quote]- 🌟 Enlaces Conceptuales
> 
> **Prerequisites (Prerrequisitos):**
> 
> - [[01.1 Sistema de Referencia Espacial]] - Base del espacio ℝ³
> - [[Números Reales]] - Componentes de vectores
> - [[Álgebra Básica]] - Operaciones fundamentales
> 
> **Temas siguientes:**
> 
> - [[01.3 Distancia en el Espacio]] - Usa magnitud de vectores
> - [[01.4 Rectas en ℝ³]] - Ecuaciones vectoriales de rectas
> - [[01.5 Planos en ℝ³]] - Vectores normales a planos
> 
> **Operaciones avanzadas:**
> 
> - [[Producto Punto]] - Proyecciones y ángulos
> - [[Producto Cruz]] - Vector perpendicular
> - [[Producto Triple]] - Volumen de paralelepípedos
> 
> **Aplicaciones:**
> 
> - [[Cinemática Vectorial]] - Movimiento en el espacio
> - [[Fuerzas y Equilibrio]] - Estática vectorial
> - [[Transformaciones Lineales]] - Matrices y vectores
> 
> **Temas relacionados:**
> 
> - [[Espacios Vectoriales]] - Generalización abstracta
> - [[Bases y Dimensión]] - Vectores linealmente independientes
> - [[Álgebra Lineal]] - Teoría completa

## 💡 Consejos de Estudio y Errores Comunes

> [!tip]- 🧠 Estrategias de Aprendizaje **Para dominar vectores:**
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
> - AB⃗ = B - A (NO A - B)
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

## 📊 Tabla Resumen de Vectores

> [!example]- 📋 Compendio Completo
> 
> |Concepto|Notación|Fórmula|Ejemplo|
> |---|---|---|---|
> |**Vector**|**v**, v⃗|(v₁, v₂, v₃)|(3, -2, 5)|
> |**Magnitud**|\|**v**\||√(v₁² + v₂² + v₃²)|√(9+4+25) = √38|
> |**Vector entre puntos**|AB⃗|B - A|(5,2,7)-(1,3,4)=(4,-1,3)|
> |**Suma**|**u** + **v**|(u₁+v₁, u₂+v₂, u₃+v₃)|(1,2,3)+(4,5,6)=(5,7,9)|
> |**Resta**|**u** - **v**|(u₁-v₁, u₂-v₂, u₃-v₃)|(5,7,9)-(1,2,3)=(4,5,6)|
> |**Mult. escalar**|k**v**|(kv₁, kv₂, kv₃)|3(1,2,3)=(3,6,9)|
> |**Vector unitario**|û|**v**/\|**v**\||(3,4,0)/5=(3/5,4/5,0)|
> |**Vectores base**|**i**, **j**, **k**|(1,0,0), (0,1,0), (0,0,1)|**v**=3**i**-2**j**+5**k**|
> |**Vector cero**|**0**|(0, 0, 0)|Elemento neutro|
> |**Vector opuesto**|-**v**|(-v₁, -v₂, -v₃)|-(2,3,1)=(-2,-3,-1)|
> |**Paralelismo**|**u** ∥ **v**|**u** = k**v**|(2,4,6) = 2(1,2,3)|

---

**Tags:** #vectores #R3 #geometría-vectorial #magnitud-vector #componentes #vectores-unitarios #operaciones-vectoriales #suma-vectores #producto-escalar #vector-entre-puntos #paralelismo #espacios-vectoriales #álgebra-lineal #física-vectorial #university #matemáticas
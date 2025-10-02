# 📏 Distancia en el Espacio

## 🎯 Fundamentos de la Métrica Euclidiana

> [!info]- 💡 Introducción a la Distancia en ℝ³ La **distancia euclidiana** es la medida de separación entre dos puntos en el espacio tridimensional. Es la extensión natural del teorema de Pitágoras a tres dimensiones y constituye la métrica estándar en geometría analítica.
> 
> **Analogías útiles:**
> 
> - **Navegación:** Distancia "en línea recta" entre dos ciudades
> - **Física:** Camino más corto que recorre la luz
> - **Arquitectura:** Distancia directa entre dos esquinas de un edificio
> 
> **Concepto clave:** La distancia siempre es el **camino más corto** entre dos puntos, que en espacio euclidiano es una **línea recta**.
> 
> **Importancia histórica:**
> 
> - **Euclides (300 a.C.):** Axiomas de geometría
> - **Descartes (1637):** Geometría analítica
> - **Pitágoras (500 a.C.):** Teorema fundamental
> - **Minkowski (1908):** Generalización de espacios métricos

### 📐 Propiedades de una Métrica

> [!note]- 🌟 Axiomas de Distancia Una función d(P, Q) es una **métrica** si cumple:
> 
> **1. No negatividad:**
> 
> - d(P, Q) ≥ 0 para todos los puntos P, Q
> - La distancia nunca es negativa
> 
> **2. Identidad:**
> 
> - d(P, Q) = 0 ⟺ P = Q
> - La distancia es cero si y solo si los puntos son iguales
> 
> **3. Simetría:**
> 
> - d(P, Q) = d(Q, P)
> - La distancia de P a Q es igual que de Q a P
> 
> **4. Desigualdad triangular:**
> 
> - d(P, R) ≤ d(P, Q) + d(Q, R)
> - El camino directo es el más corto
> 
> La distancia euclidiana cumple todas estas propiedades.

## 📊 Fórmula de la Distancia entre Dos Puntos

### 🔢 Deducción y Fórmula

> [!warning]- 🔷 Fórmula Fundamental **Dados dos puntos en ℝ³:**
> 
> - P₁ = (x₁, y₁, z₁)
> - P₂ = (x₂, y₂, z₂)
> 
> **La distancia entre P₁ y P₂ es:**
> 
> **d(P₁, P₂) = √[(x₂ - x₁)² + (y₂ - y₁)² + (z₂ - z₁)²]**
> 
> **Forma alternativa usando vectores:**
> 
> Si **v** = P₁P₂⃗ = (x₂ - x₁, y₂ - y₁, z₂ - z₁)
> 
> Entonces: **d(P₁, P₂) = ||v|| = ||P₁P₂⃗||**
> 
> **Interpretación:**
> 
> - Es la **magnitud del vector** que une los dos puntos
> - Es la longitud de la **línea recta** que los conecta
> - Es el camino **más corto** entre ellos
> 
> **Relación con dimensiones inferiores:**
> 
> - En ℝ¹: d = |x₂ - x₁|
> - En ℝ²: d = √[(x₂-x₁)² + (y₂-y₁)²]
> - En ℝ³: d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]

### 🔍 Demostración Visual

> [!tip]- 📐 Deducción Geométrica **Aplicación del Teorema de Pitágoras en 3D:**
> 
> ```
> Paso 1: Considerar el triángulo rectángulo en el plano XY
> - Cateto horizontal: Δx = x₂ - x₁
> - Cateto vertical (en XY): Δy = y₂ - y₁
> - Hipotenusa en XY: d_xy = √(Δx² + Δy²)
> 
> Paso 2: Considerar el triángulo rectángulo formado por d_xy y Δz
> - Cateto horizontal: d_xy = √[(x₂-x₁)² + (y₂-y₁)²]
> - Cateto vertical: Δz = z₂ - z₁
> - Hipotenusa final: d = √(d_xy² + Δz²)
> 
> Paso 3: Sustituir d_xy
> d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]
> ```
> 
> **Visualización:**
> 
> - Imagina un paralelepípedo rectangular
> - Los puntos están en vértices opuestos
> - La distancia es la **diagonal espacial**

## 📝 Ejemplos Resueltos

### ✅ Ejemplo 1: Distancia Básica

> [!example]- 🎯 Caso Fundamental **Problema:** Calcular la distancia entre A = (1, 2, 3) y B = (4, 6, 7)
> 
> **Solución paso a paso:**
> 
> ```
> Datos:
> A = (1, 2, 3) → x₁=1, y₁=2, z₁=3
> B = (4, 6, 7) → x₂=4, y₂=6, z₂=7
> 
> Paso 1: Calcular diferencias
> Δx = x₂ - x₁ = 4 - 1 = 3
> Δy = y₂ - y₁ = 6 - 2 = 4
> Δz = z₂ - z₁ = 7 - 3 = 4
> 
> Paso 2: Elevar al cuadrado
> (Δx)² = 3² = 9
> (Δy)² = 4² = 16
> (Δz)² = 4² = 16
> 
> Paso 3: Sumar
> (Δx)² + (Δy)² + (Δz)² = 9 + 16 + 16 = 41
> 
> Paso 4: Raíz cuadrada
> d(A, B) = √41 ≈ 6.403 unidades
> ```
> 
> **Verificación con vectores:**
> 
> ```
> AB⃗ = (3, 4, 4)
> ||AB⃗|| = √(9 + 16 + 16) = √41 ✓
> ```

### ✅ Ejemplo 2: Distancia con Coordenadas Negativas

> [!example]- 🎯 Caso con Signos **Problema:** Calcular la distancia entre C = (-2, 3, -1) y D = (4, -1, 5)
> 
> **Solución:**
> 
> ```
> Datos:
> C = (-2, 3, -1)
> D = (4, -1, 5)
> 
> Diferencias:
> Δx = 4 - (-2) = 4 + 2 = 6
> Δy = -1 - 3 = -4
> Δz = 5 - (-1) = 5 + 1 = 6
> 
> Cálculo:
> d(C, D) = √(6² + (-4)² + 6²)
>         = √(36 + 16 + 36)
>         = √88
>         = √(4 × 22)
>         = 2√22 ≈ 9.381 unidades
> ```
> 
> **Nota importante:** Los signos negativos desaparecen al elevar al cuadrado.

### ✅ Ejemplo 3: Distancia desde el Origen

> [!example]- 🎯 Caso Especial **Problema:** Calcular la distancia desde el origen O = (0, 0, 0) hasta P = (3, 4, 12)
> 
> **Solución:**
> 
> ```
> Cuando uno de los puntos es el origen, la fórmula se simplifica:
> 
> d(O, P) = √(3² + 4² + 12²)
>         = √(9 + 16 + 144)
>         = √169
>         = 13 unidades
> ```
> 
> **Interpretación:** La distancia desde el origen es simplemente la **magnitud del vector posición** del punto.
> 
> **Fórmula simplificada:** d(O, P) = √(x² + y² + z²) = ||OP⃗||

### ✅ Ejemplo 4: Puntos en Planos Coordenados

> [!example]- 🎯 Casos en Planos **a) Distancia en el plano XY:**
> 
> P = (5, 12, 0) y Q = (1, 9, 0)
> 
> ```
> Como z₁ = z₂ = 0, la fórmula se reduce a 2D:
> d(P, Q) = √[(1-5)² + (9-12)² + 0²]
>         = √[(-4)² + (-3)²]
>         = √(16 + 9)
>         = √25 = 5 unidades
> ```
> 
> **b) Distancia en el eje X:**
> 
> A = (3, 0, 0) y B = (7, 0, 0)
> 
> ```
> Como y₁ = y₂ = z₁ = z₂ = 0:
> d(A, B) = √[(7-3)²]
>         = √16 = 4 unidades
> ```
> 
> **Nota:** Es simplemente |x₂ - x₁|

## 🧮 Aplicaciones de la Distancia

### 🔵 Ecuación de la Esfera

> [!success]- ⭕ Lugar Geométrico **Definición:**
> 
> Una **esfera** es el conjunto de todos los puntos que están a una distancia constante (radio) de un punto fijo (centro).
> 
> **Ecuación de la esfera:**
> 
> Centro C = (h, k, l), radio r
> 
> **Forma estándar:** **(x - h)² + (y - k)² + (z - l)² = r²**
> 
> **Deducción:** Si P = (x, y, z) está en la esfera, entonces d(P, C) = r
> 
> ```
> √[(x-h)² + (y-k)² + (z-l)²] = r
> 
> Elevando al cuadrado ambos lados:
> (x-h)² + (y-k)² + (z-l)² = r²
> ```
> 
> **Casos especiales:**
> 
> **Esfera centrada en el origen:** x² + y² + z² = r²
> 
> **Ejemplo:** Esfera con centro C = (1, -2, 3) y radio r = 5:
> 
> ```
> (x - 1)² + (y + 2)² + (z - 3)² = 25
> ```

### 📍 Punto Medio entre Dos Puntos

> [!note]- 🎯 Fórmula del Punto Medio **Dados P₁ = (x₁, y₁, z₁) y P₂ = (x₂, y₂, z₂):**
> 
> **El punto medio M es:**
> 
> **M = ((x₁ + x₂)/2, (y₁ + y₂)/2, (z₁ + z₂)/2)**
> 
> **Interpretación:**
> 
> - Es el promedio de las coordenadas correspondientes
> - Divide el segmento P₁P₂ en dos partes iguales
> - Equidista de ambos puntos: d(P₁, M) = d(M, P₂)
> 
> **Propiedades:**
> 
> 1. d(P₁, M) = d(M, P₂) = ½d(P₁, P₂)
> 2. P₁M⃗ = ½P₁P₂⃗
> 3. M es único para cada par de puntos
> 
> **Ejemplo:**
> 
> ```
> P₁ = (2, 4, 6)
> P₂ = (8, 2, 10)
> 
> M = ((2+8)/2, (4+2)/2, (6+10)/2)
>   = (10/2, 6/2, 16/2)
>   = (5, 3, 8)
> 
> Verificación:
> d(P₁, M) = √[(5-2)² + (3-4)² + (8-6)²]
>          = √(9 + 1 + 4) = √14
> 
> d(M, P₂) = √[(8-5)² + (2-3)² + (10-8)²]
>          = √(9 + 1 + 4) = √14 ✓
> ```

### 🎯 División de un Segmento

> [!tip]- 📐 Razón de División **Punto que divide P₁P₂ en razón r:s**
> 
> Si queremos encontrar un punto Q que divide P₁P₂ tal que: d(P₁, Q) : d(Q, P₂) = r : s
> 
> **Fórmula:**
> 
> **Q = ((sx₁ + rx₂)/(r+s), (sy₁ + ry₂)/(r+s), (sz₁ + rz₂)/(r+s))**
> 
> **Casos especiales:**
> 
> - Si r = s = 1: Q es el punto medio
> - Si r = 2, s = 1: Q divide en 2:1 (más cerca de P₂)
> 
> **Ejemplo:** Dividir el segmento de A = (0, 0, 0) a B = (6, 9, 12) en razón 1:2
> 
> ```
> r = 1, s = 2
> 
> Q = ((2·0 + 1·6)/3, (2·0 + 1·9)/3, (2·0 + 1·12)/3)
>   = (6/3, 9/3, 12/3)
>   = (2, 3, 4)
> 
> Verificación:
> d(A, Q) = √(4 + 9 + 16) = √29
> d(Q, B) = √[(6-2)² + (9-3)² + (12-4)²]
>         = √(16 + 36 + 64) = √116 = 2√29
> 
> Razón: √29 : 2√29 = 1 : 2 ✓
> ```

## 🔬 Problemas Aplicados

### 🛩️ Ejemplo: Navegación Aérea

> [!example]- ✈️ Problema Realista **Situación:** Un avión está en la posición A = (100, 200, 8000) metros (coordenadas relativas a un aeropuerto) y debe aterrizar en B = (0, 0, 0). Una torre de control está en T = (50, 100, 150) metros.
> 
> **Preguntas:** a) ¿Qué distancia debe recorrer el avión para aterrizar? b) ¿A qué distancia está la torre del punto de aterrizaje? c) ¿Cuál es el punto medio de la trayectoria del avión?
> 
> **Soluciones:**
> 
> **a) Distancia de vuelo:**
> 
> ```
> d(A, B) = √[(0-100)² + (0-200)² + (0-8000)²]
>         = √[10000 + 40000 + 64000000]
>         = √64050000
>         ≈ 8003.1 metros
> ```
> 
> **b) Distancia de la torre al aterrizaje:**
> 
> ```
> d(T, B) = √(50² + 100² + 150²)
>         = √(2500 + 10000 + 22500)
>         = √35000
>         ≈ 187.1 metros
> ```
> 
> **c) Punto medio de la trayectoria:**
> 
> ```
> M = ((100+0)/2, (200+0)/2, (8000+0)/2)
>   = (50, 100, 4000) metros
> ```

### 🏗️ Ejemplo: Ingeniería Estructural

> [!example]- 🏢 Problema de Construcción **Situación:** En un edificio, tres columnas están ubicadas en:
> 
> - Columna A: (0, 0, 0) metros
> - Columna B: (10, 0, 0) metros
> - Columna C: (5, 8, 0) metros
> 
> Se instalará un tanque de agua en el punto T = (5, 4, 20) metros.
> 
> **Preguntas:** a) ¿Cuál columna está más cerca del tanque? b) ¿Qué longitud de tubería se necesita desde cada columna?
> 
> **Soluciones:**
> 
> **a) Distancias:**
> 
> ```
> d(A, T) = √[(5-0)² + (4-0)² + (20-0)²]
>         = √(25 + 16 + 400)
>         = √441 = 21 metros
> 
> d(B, T) = √[(5-10)² + (4-0)² + (20-0)²]
>         = √(25 + 16 + 400)
>         = √441 = 21 metros
> 
> d(C, T) = √[(5-5)² + (4-8)² + (20-0)²]
>         = √(0 + 16 + 400)
>         = √416 ≈ 20.4 metros
> ```
> 
> **Respuesta:** La columna C está más cerca (20.4 m)
> 
> **b) Longitudes de tubería:**
> 
> - Desde A: 21 metros
> - Desde B: 21 metros
> - Desde C: 20.4 metros (más eficiente)

### 🎮 Ejemplo: Videojuegos

> [!example]- 🕹️ Detección de Colisiones **Situación:** En un videojuego 3D:
> 
> - Jugador en posición P = (10, 5, 2)
> - Enemigo en posición E = (13, 8, 5)
> - Radio de detección: 5 unidades
> 
> **Pregunta:** ¿El enemigo está en rango de detección?
> 
> **Solución:**
> 
> ```
> d(P, E) = √[(13-10)² + (8-5)² + (5-2)²]
>         = √(9 + 9 + 9)
>         = √27
>         = 3√3 ≈ 5.196 unidades
> ```
> 
> **Respuesta:** NO está en rango (5.196 > 5)
> 
> **Código de implementación:**
> 
> ```python
> def distancia_3d(p1, p2):
>     dx = p2[0] - p1[0]
>     dy = p2[1] - p1[1]
>     dz = p2[2] - p1[2]
>     return (dx**2 + dy**2 + dz**2)**0.5
> 
> def en_rango(jugador, enemigo, rango):
>     return distancia_3d(jugador, enemigo) <= rango
> 
> # Uso
> P = (10, 5, 2)
> E = (13, 8, 5)
> detectado = en_rango(P, E, 5)
> print(f"Enemigo detectado: {detectado}")
> # Salida: Enemigo detectado: False
> ```

## 🧮 Distancias Especiales

### 📏 Distancia Máxima y Mínima

> [!warning]- 🔶 Problemas de Optimización **Problema tipo:** Encontrar el punto sobre una superficie que minimiza/maximiza la distancia a otro punto dado.
> 
> **Ejemplo: Punto más cercano en un plano**
> 
> Dado el plano XY (z = 0) y el punto P = (3, 4, 5), encontrar el punto Q en el plano más cercano a P.
> 
> **Solución:** El punto más cercano es la proyección perpendicular:
> 
> ```
> Q = (3, 4, 0)
> 
> d(P, Q) = √[(3-3)² + (4-4)² + (5-0)²]
>         = √25 = 5 unidades
> ```
> 
> **Generalización:** Para proyectar P = (x, y, z) sobre:
> 
> - Plano XY: Q = (x, y, 0)
> - Plano XZ: Q = (x, 0, z)
> - Plano YZ: Q = (0, y, z)

### 🎯 Distancia entre Puntos Simétricos

> [!note]- 🔄 Simetría en el Espacio **Simetría respecto al origen:**
> 
> Si P = (x, y, z), su simétrico respecto al origen es P' = (-x, -y, -z)
> 
> ```
> d(P, P') = √[(−x−x)² + (−y−y)² + (−z−z)²]
>          = √[(2x)² + (2y)² + (2z)²]
>          = 2√(x² + y² + z²)
>          = 2·d(O, P)
> ```
> 
> **Simetría respecto a un plano:**
> 
> **Plano XY (z = 0):** P = (x, y, z) → P' = (x, y, -z) d(P, P') = 2|z|
> 
> **Plano XZ (y = 0):** P = (x, y, z) → P' = (x, -y, z) d(P, P') = 2|y|
> 
> **Plano YZ (x = 0):** P = (x, y, z) → P' = (-x, y, z) d(P, P') = 2|x|

## 🎨 Diagrama de Conceptos

```mermaid
graph TD
    A[Distancia en ℝ³] --> B[Fórmula Básica]
    A --> C[Aplicaciones]
    A --> D[Casos Especiales]
    
    B --> B1[d = √Δx² + Δy² + Δz²<br/>Distancia euclidiana]
    B --> B2[Propiedades<br/>Simetría, No negatividad]
    B --> B3[Relación con vectores<br/>d = ||v||]
    
    C --> C1[Ecuación esfera<br/>x-h² + y-k² + z-l² = r²]
    C --> C2[Punto medio<br/>M = P₁+P₂/2]
    C --> C3[División de segmentos<br/>Razón r:s]
    
    D --> D1[Desde el origen<br/>d = √x² + y² + z²]
    D --> D2[En planos coordenados<br/>Una coordenada = 0]
    D --> D3[En ejes<br/>Dos coordenadas = 0]
    
    style A fill:#e3f2fd
    style B fill:#e8f5e9
    style C fill:#fff3e0
    style D fill:#f3e5f5
```

## 🧪 Ejercicios Progresivos

> [!example]- 💪 Práctica Completa **Nivel 1 - Básico:** 🟢
> 
> 1. Calcular las siguientes distancias:
>     - a) d((1,2,3), (4,6,15))
>     - b) d((0,0,0), (5,12,0))
>     - c) d((-1,2,3), (2,-2,7))
> 
> **Soluciones:**
> 
> ```
> a) d = √[(4-1)² + (6-2)² + (15-3)²]
>      = √(9 + 16 + 144) = √169 = 13
> 
> b) d = √(25 + 144 + 0) = √169 = 13
> 
> c) d = √[(2-(-1))² + (-2-2)² + (7-3)²]
>      = √(9 + 16 + 16) = √41
> ```
> 
> 2. Encontrar el punto medio de:
>     - A = (2, 4, 6) y B = (8, 2, 10)
> 
> **Solución:** M = ((2+8)/2, (4+2)/2, (6+10)/2) = (5, 3, 8)
> 
> ---
> 
> **Nivel 2 - Intermedio:** 🟡
> 
> 3. Determinar si los puntos A = (1,2,3), B = (4,6,7) y C = (7,10,11) son colineales usando distancias.
> 
> **Solución:**
> 
> ```
> Si son colineales: d(A,C) = d(A,B) + d(B,C)
> 
> d(A,B) = √(9 + 16 + 16) = √41
> d(B,C) = √(9 + 16 + 16) = √41
> d(A,C) = √(36 + 64 + 64) = √164 = 2√41
> 
> d(A,C) = 2√41 = √41 + √41 = d(A,B) + d(B,C) ✓
> Son colineales
> ```
> 
> 4. Escribir la ecuación de una esfera con centro C = (2, -1, 3) que pasa por el punto P = (5, 3, 7).
> 
> **Solución:**
> 
> ```
> Radio: r = d(C, P) = √[(5-2)² + (3-(-1))² + (7-3)²]
>                    = √(9 + 16 + 16) = √41
> 
> Ecuación: (x-2)² + (y+1)² + (z-3)² = 41
> ```
> 
> ---
> 
> **Nivel 3 - Avanzado:** 🔴
> 
> 5. Un punto P se mueve en el espacio de tal forma que siempre está a igual distancia de A = (1, 0, 0) y B = (0, 1, 0). Encontrar la ecuación del lugar geométrico.
> 
> **Solución:**
> 
> ```
> Sea P = (x, y, z)
> d(P, A) = d(P, B)
> 
> √[(x-1)² + y² + z²] = √[x² + (y-1)² + z²]
> 
> Elevando al cuadrado:
> (x-1)² + y² + z² = x² + (y-1)² + z²
> x² - 2x + 1 + y² = x² + y² - 2y + 1
> -2x = -2y
> x = y
> 
> Respuesta: El plano x = y
> ```
> 
> 6. Problema de optimización: Encontrar el punto en el eje Z más cercano a P = (3, 4, 7).
> 
> **Solución:**
> 
> ```
> Un punto en el eje Z tiene forma Q = (0, 0, z)
> 
> d(P, Q) = √[(3-0)² + (4-0)² + (7-z)²]
>         = √[25 + (7-z)²]
> 
> Para minimizar, minimizamos (7-z)²
> Esto ocurre cuando z = 7
> 
> Punto más cercano: Q = (0, 0, 7)
> Distancia mínima: d = √25 = 5
> ```

## 💻 Implementación Computacional

### 🐍 Python

> [!success]- 💻 Código Optimizado
> 
> ```python
> import math
> from typing import Tuple
> 
> def distancia_euclidiana(p1: Tuple[float, float, float], 
>                          p2: Tuple[float, float, float]) -> float:
>     """
>     Calcula la distancia euclidiana entre dos puntos en ℝ³
>     
>     Args:
>         p1: Primer punto (x1, y1, z1)
>         p2: Segundo punto (x2, y2, z2)
>     
>     Returns:
>         Distancia entre los puntos
>     """
>     dx = p2[0] - p1[0]
>     dy = p2[1] - p1[1]
>     dz = p2[2] - p1[2]
>     return math.sqrt(dx**2 + dy**2 + dz**2)
> 
> def punto_medio(p1: Tuple[float, float, float],
>                 p2: Tuple[float, float, float]) -> Tuple[float, float, float]:
>     """Calcula el punto medio entre dos puntos"""
>     return (
>         (p1[0] + p2[0]) / 2,
>         (p1[1] + p2[1]) / 2,
>         (p1[2] + p2[2]) / 2
>     )
> 
> def punto_en_esfera(punto: Tuple[float, float, float],
>                     centro: Tuple[float, float, float],
>                     radio: float,
>                     tolerancia: float = 1e-6) -> bool:
>     """Verifica si un punto está en una esfera"""
>     dist = distancia_euclidiana(punto, centro)
>     return abs(dist - radio) < tolerancia
> 
> # Ejemplos de uso
> if __name__ == "__main__":
>     A = (1, 2, 3)
>     B = (4, 6, 7)
>     
>     print(f"Distancia entre {A} y {B}: {distancia_euclidiana(A, B):.2f}")
>     print(f"Punto medio: {punto_medio(A, B)}")
>     
>     # Verificar si (5, 3, 7) está en esfera centrada en (2, -1, 3) con radio √41
>     P = (5, 3, 7)
>     C = (2, -1, 3)
>     r = math.sqrt(41)
>     print(f"¿P está en la esfera? {punto_en_esfera(P, C, r)}")
> ```

### 🎯 JavaScript

> [!note]- 🌐 Para Aplicaciones Web
> 
> ```javascript
> class Punto3D {
>     constructor(x, y, z) {
>         this.x = x;
>         this.y = y;
>         this.z = z;
>     }
>     
>     distanciaA(otro) {
>         const dx = otro.x - this.x;
>         const dy = otro.y - this.y;
>         const dz = otro.z - this.z;
>         return Math.sqrt(dx*dx + dy*dy + dz*dz);
>     }
>     
>     puntoMedioCon(otro) {
>         return new Punto3D(
>             (this.x + otro.x) / 2,
>             (this.y + otro.y) / 2,
>             (this.z + otro.z) / 2
>         );
>     }
>     
>     toString() {
>         return `(${this.x}, ${this.y}, ${this.z})`;
>     }
> }
> 
> // Uso
> const A = new Punto3D(1, 2, 3);
> const B = new Punto3D(4, 6, 7);
> 
> console.log(`Distancia: ${A.distanciaA(B).toFixed(2)}`);
> console.log(`Punto medio: ${A.puntoMedioCon(B)}`);
> ```

## 🔗 Conexiones con el Sistema de Notas

> [!quote]- 🌟 Enlaces Conceptuales **Prerequisites (Prerrequisitos):**
> 
> - [[01.1 Sistema de Referencia Espacial]] - Puntos en ℝ³
> - [[01.2 Vectores en ℝ³]] - Magnitud de vectores
> - [[Teorema de Pitágoras]] - Fundamento geométrico
> 
> **Temas siguientes:**
> 
> - [[01.4 Rectas en ℝ³]] - Distancia punto-recta
> - [[01.5 Planos en ℝ³]] - Distancia punto-plano
> - [[01.7 Distancias en ℝ³]] - Casos especiales
> 
> **Conceptos relacionados:**
> 
> - [[Producto Punto]] - Proyecciones y distancias
> - [[Ecuaciones Cuadráticas]] - Esfera y superficies
> - [[Optimización]] - Problemas de mínima distancia
> 
> **Aplicaciones:**
> 
> - [[Colisiones en 3D]] - Detección en videojuegos
> - [[Geometría Computacional]] - Algoritmos espaciales
> - [[Física del Movimiento]] - Trayectorias y desplazamientos

## 💡 Consejos y Errores Comunes

> [!tip]- 🧠 Estrategias de Éxito **Para dominar distancias:**
> 
> **1. Visualización:**
> 
> - Dibujar los puntos en un sistema 3D
> - Imaginar el segmento que los une
> - Proyectar mentalmente sobre los planos
> 
> **2. Orden en los cálculos:**
> 
> - Siempre restar coordenadas correspondientes
> - Elevar al cuadrado cada diferencia
> - Sumar todos los términos
> - Aplicar raíz cuadrada AL FINAL
> 
> **3. Simplificación:**
> 
> - Buscar patrones (puntos en planos o ejes)
> - Factorizar cuando sea posible
> - Dejar resultados en forma radical si es exacto
> 
> **Errores comunes a evitar:**
> 
> ❌ **Error 1:** Olvidar la raíz cuadrada
> 
> ```
> ✗ d = (3)² + (4)² + (0)² = 25
> ✓ d = √[(3)² + (4)² + (0)²] = √25 = 5
> ```
> 
> ❌ **Error 2:** Signos en las restas
> 
> ```
> Para A = (2, -3, 5) y B = (-1, 4, 2):
> ✗ Δx = 2 - 1 = 1
> ✓ Δx = -1 - 2 = -3
> ```
> 
> ❌ **Error 3:** Orden incorrecto en punto medio
> 
> ```
> ✗ M = (x₁ - x₂)/2  (resta)
> ✓ M = (x₁ + x₂)/2  (suma)
> ```
> 
> ❌ **Error 4:** Confundir distancia con vector
> 
> - Distancia: es un número (escalar) ≥ 0
> - Vector: tiene componentes y dirección
> 
> ❌ **Error 5:** No verificar el contexto
> 
> - ¿Pedían distancia exacta o aproximada?
> - ¿En qué unidades están las coordenadas?

## 📊 Tabla Resumen

> [!example]- 📋 Fórmulas Esenciales
> 
> |Concepto|Fórmula|Ejemplo|
> |---|---|---|
> |**Distancia 3D**|d = √(Δx² + Δy² + Δz²)|d((1,2,3), (4,6,7)) = √41|
> |**Desde origen**|d = √(x² + y² + z²)|d(O, (3,4,12)) = 13|
> |**Punto medio**|M = ((x₁+x₂)/2, ...)|M((0,0,0), (6,4,2)) = (3,2,1)|
> |**Esfera**|(x-h)² + (y-k)² + (z-l)² = r²|Centro (1,2,3), r=5|
> |**División r:s**|Q = (sx₁+rx₂)/(r+s), ...|Razón 1:2 en segmento|
> |**En plano XY**|d = √(Δx² + Δy²)|z₁ = z₂ = 0|
> |**En eje X**|d = \|x₂ - x₁\||y₁ = y₂ = z₁ = z₂ = 0|

---

**Tags:** #distancia-euclidiana #geometría-analítica #R3 #fórmula-distancia #punto-medio #esfera #métrica #teorema-pitágoras #coordenadas-3d #división-segmento #optimización-distancia #university #matemáticas #cálculo-vectorial
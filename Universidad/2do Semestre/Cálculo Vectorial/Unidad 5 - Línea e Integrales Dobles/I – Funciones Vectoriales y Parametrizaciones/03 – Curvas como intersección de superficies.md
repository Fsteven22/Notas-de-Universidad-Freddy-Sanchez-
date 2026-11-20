---
dg-publish: true
---

# 📐 Curvas como Intersección de Superficies

## 🎯 Introducción

> [!info] 💡 ¿Qué es la Intersección de Superficies?
> 
> En el espacio tridimensional **ℝ³**, cuando dos superficies se encuentran, su intersección generalmente forma una **curva espacial**. Este concepto es fundamental en cálculo vectorial y tiene aplicaciones en geometría, física y diseño computacional.
> 
> **Analogía práctica:** Imagina dos hojas de papel que se cruzan en el espacio:
> 
> - **Primera hoja** podría ser horizontal (un plano)
> - **Segunda hoja** podría estar inclinada
> - La **línea donde se tocan** es la curva de intersección
> 
> **¿Por qué es importante?**
> 
> |Aspecto|Descripción|Ejemplo de Uso|
> |---|---|---|
> |**Visualización 3D**|Entender formas complejas|Modelado CAD, gráficos|
> |**Física**|Trayectorias de partículas|Movimiento con restricciones|
> |**Ingeniería**|Intersección de estructuras|Diseño de piezas mecánicas|
> |**Geografía**|Curvas de nivel|Mapas topográficos|
> |**Optimización**|Restricciones múltiples|Programación no lineal|

![[Diagramas/03_–_Curvas_como_intersección_de_superficies_01.svg]]

---

## 📊 Conceptos Fundamentales

### 🌍 Superficies en ℝ³

> [!example] 📐 Representación de Superficies
> 
> Una **superficie** en ℝ³ puede representarse de varias formas:
> 
> **1. Forma Implícita:** F(x, y, z) = 0
> 
> ```
> Ejemplos:
> • Plano:        x + 2y - z = 5
> • Esfera:       x² + y² + z² = r²
> • Cilindro:     x² + y² = r²
> • Paraboloide:  z = x² + y²
> ```
> 
> **2. Forma Paramétrica:** **r**(u, v) = (x(u,v), y(u,v), z(u,v))
> 
> ```
> Ejemplo - Esfera:
> x = R·cos(u)·sin(v)
> y = R·sin(u)·sin(v)
> z = R·cos(v)
> donde u ∈ [0, 2π], v ∈ [0, π]
> ```
> 
> **3. Forma Explícita:** z = f(x, y)
> 
> ```
> Ejemplos:
> • Plano inclinado:    z = 2x + 3y + 1
> • Paraboloide:        z = x² + y²
> • Silla de montar:    z = x² - y²
> ```
> 
> **Comparación de representaciones:**
> 
> |Forma|Ventajas|Desventajas|Uso Típico|
> |---|---|---|---|
> |**Implícita**|Simple, directa|Difícil parametrizar|Intersecciones|
> |**Paramétrica**|Fácil recorrer|Más variables|Visualización|
> |**Explícita**|Intuitiva|Solo funciones|Gráficas simples|
> 
> **Visualización de tipos de superficies:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_02.svg]]

### 🔄 Curvas Espaciales

> [!note] 📈 Definición y Propiedades
> 
> Una **curva espacial** es una función vectorial:
> 
> **r**(t) = (x(t), y(t), z(t))
> 
> donde t es el parámetro (típicamente el tiempo o longitud de arco).
> 
> **Propiedades fundamentales:**
> 
> |Propiedad|Fórmula|Interpretación|
> |---|---|---|
> |**Vector Tangente**|**T**(t) = **r**'(t) / \|**r**'(t)\||Dirección de movimiento|
> |**Velocidad**|**v**(t) = **r**'(t)|Tasa de cambio de posición|
> |**Rapidez**|v(t) = \|**r**'(t)\||Magnitud de velocidad|
> |**Aceleración**|**a**(t) = **r**''(t)|Cambio en velocidad|
> 
> **Ejemplo de curva espacial:**
> 
> ```
> Hélice circular:
> r(t) = (R·cos(t), R·sin(t), ct)
> 
> donde:
> • R = radio de la hélice
> • c = paso vertical
> • t ∈ [0, 2πn] para n vueltas
> ```
> 
> **Elementos de una curva:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_03.svg]]

---

## 🔗 Intersección de Dos Superficies

### 📋 Planteamiento del Problema

> [!success] 🎯 Sistema de Ecuaciones
> 
> Para encontrar la curva de intersección de dos superficies:
> 
> **Sistema:**
> 
> ```
> S₁: F₁(x, y, z) = 0
> S₂: F₂(x, y, z) = 0
> ```
> 
> **Solución:** Los puntos (x, y, z) que satisfacen **ambas** ecuaciones simultáneamente forman la curva de intersección.
> 
> **Proceso de solución:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_04.svg]]
> 
> **Estrategias generales:**
> 
> |Método|Cuándo Usar|Complejidad|Ventaja|
> |---|---|---|---|
> |**Sustitución**|Una superficie es simple (plano)|⭐⭐ Baja|Directo, algebraico|
> |**Eliminación**|Ambas son polinomiales|⭐⭐⭐ Media|Sistemático|
> |**Paramétrico**|Superficies con simetría|⭐⭐⭐⭐ Alta|Elegante, geométrico|
> |**Numérico**|Casos complicados|⭐⭐⭐⭐⭐ Muy Alta|Universal|

### 🔧 Método 1: Plano Intersecando Superficie

> [!example] ✂️ Ejemplo: Plano y Esfera
> 
> **Problema:** Encontrar la intersección de:
> 
> ```
> S₁ (Plano):   z = 1
> S₂ (Esfera):  x² + y² + z² = 4
> ```
> 
> **Paso 1: Sustituir**
> 
> Reemplazamos z = 1 en la ecuación de la esfera:
> 
> ```
> x² + y² + (1)² = 4
> x² + y² + 1 = 4
> x² + y² = 3
> ```
> 
> **Paso 2: Interpretar**
> 
> Esta es un **círculo** en el plano z = 1 con radio √3.
> 
> **Paso 3: Parametrizar**
> 
> ```
> x(t) = √3 · cos(t)
> y(t) = √3 · sin(t)
> z(t) = 1
> 
> donde t ∈ [0, 2π]
> ```
> 
> **Vector posición de la curva:**
> 
> ```
> r(t) = (√3·cos(t), √3·sin(t), 1)
> ```
> 
> **Visualización:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_05.svg]]
> 
> **Propiedades de la curva:**
> 
> |Propiedad|Cálculo|Valor|
> |---|---|---|
> |**Vector tangente**|r'(t)|(-√3·sin(t), √3·cos(t), 0)|
> |**Rapidez**|\|r'(t)\||√3 (constante)|
> |**Longitud**|∫₀²π \|r'(t)\| dt|2π√3|
> 
> **Ejemplo 2: Plano inclinado y cilindro**
> 
> ```
> S₁ (Cilindro):  x² + y² = 1
> S₂ (Plano):     z = x
> ```
> 
> **Solución:**
> 
> De S₁: x² + y² = 1 → Parametrizar: x = cos(t), y = sin(t)
> 
> De S₂: z = x = cos(t)
> 
> **Curva de intersección:**
> 
> ```
> r(t) = (cos(t), sin(t), cos(t))
> t ∈ [0, 2π]
> ```
> 
> Esta es una **elipse alabeada** (elipse que no está en un plano).

### ⚙️ Método 2: Dos Superficies Cuadráticas

> [!tip] 🔄 Ejemplo: Dos Cilindros
> 
> **Problema:** Intersección de dos cilindros:
> 
> ```
> S₁: x² + y² = 1  (cilindro eje z)
> S₂: x² + z² = 1  (cilindro eje y)
> ```
> 
> **Análisis:**
> 
> De S₁: x² = 1 - y²
> 
> Sustituir en S₂:
> 
> ```
> (1 - y²) + z² = 1
> z² = y²
> z = ±y
> ```
> 
> **Sistema resultante:**
> 
> ```
> x² + y² = 1
> z = ±y
> ```
> 
> **Dos curvas de intersección:**
> 
> **Curva C₁ (z = y):**
> 
> ```
> x = cos(t)
> y = sin(t)
> z = sin(t)
> 
> r₁(t) = (cos(t), sin(t), sin(t))
> ```
> 
> **Curva C₂ (z = -y):**
> 
> ```
> r₂(t) = (cos(t), sin(t), -sin(t))
> ```
> 
> **Visualización de las curvas:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_06.svg]]
> 
> **Propiedades:**
> 
> |Aspecto|Curva C₁|Curva C₂|
> |---|---|---|
> |**Simetría**|Respecto a plano y=z|Respecto a plano y=-z|
> |**Tangente en t=0**|(0, 1, 1)|(0, 1, -1)|
> |**Puntos extremos**|z_max = 1, z_min = -1|z_max = 1, z_min = -1|

### 🎨 Método 3: Casos Especiales

> [!note] 🌟 Intersección de Esfera y Cono
> 
> **Problema:**
> 
> ```
> S₁ (Esfera):  x² + y² + z² = 4
> S₂ (Cono):    z² = x² + y²
> ```
> 
> **Paso 1: Sustitución**
> 
> De S₂: z² = x² + y²
> 
> Sustituir en S₁:
> 
> ```
> x² + y² + (x² + y²) = 4
> 2(x² + y²) = 4
> x² + y² = 2
> ```
> 
> **Paso 2: Encontrar z**
> 
> De S₂: z² = x² + y² = 2
> 
> ```
> z = ±√2
> ```
> 
> **Resultado:** Dos círculos
> 
> **Círculo C₁ (z = √2):**
> 
> ```
> x² + y² = 2, z = √2
> 
> Parametrización:
> r₁(t) = (√2·cos(t), √2·sin(t), √2)
> ```
> 
> **Círculo C₂ (z = -√2):**
> 
> ```
> r₂(t) = (√2·cos(t), √2·sin(t), -√2)
> ```
> 
> **Interpretación geométrica:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_07.svg]]

---

## 📐 Vector Tangente y Propiedades

### 🧭 Cálculo del Vector Tangente

> [!success] ➡️ Derivada de la Curva
> 
> Si la curva está parametrizada como **r**(t) = (x(t), y(t), z(t)), el **vector tangente** es:
> 
> **r**'(t) = (x'(t), y'(t), z'(t))
> 
> **Vector tangente unitario:**
> 
> ```
> T(t) = r'(t) / |r'(t)|
> ```
> 
> **Ejemplo con hélice:**
> 
> ```
> r(t) = (2cos(t), 2sin(t), t)
> 
> r'(t) = (-2sin(t), 2cos(t), 1)
> 
> |r'(t)| = √(4sin²(t) + 4cos²(t) + 1)
>        = √(4 + 1)
>        = √5
> 
> T(t) = 1/√5 · (-2sin(t), 2cos(t), 1)
> ```
> 
> **Tabla de vectores fundamentales:**
> 
> |Vector|Símbolo|Fórmula|Significado|
> |---|---|---|---|
> |**Posición**|**r**(t)|(x(t), y(t), z(t))|Punto en la curva|
> |**Velocidad**|**v**(t)|**r**'(t)|Tasa de cambio|
> |**Tangente unitario**|**T**(t)|**r**'(t)/\|**r**'(t)\||Dirección|
> |**Normal principal**|**N**(t)|**T**'(t)/\|**T**'(t)\||Curvatura|
> |**Binormal**|**B**(t)|**T** × **N**|Perpendicular al plano osculador|
> 
> **Interpretación física:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_08.svg]]

### 📏 Longitud de Arco

> [!example] 📊 Cálculo de Distancia Recorrida
> 
> La **longitud de arco** desde t = a hasta t = b es:
> 
> ```
> L = ∫ₐᵇ |r'(t)| dt
> ```
> 
> **Ejemplo: Longitud de un círculo**
> 
> ```
> r(t) = (R·cos(t), R·sin(t), h)  [círculo en z = h]
> 
> r'(t) = (-R·sin(t), R·cos(t), 0)
> 
> |r'(t)| = √(R²sin²(t) + R²cos²(t))
>        = R
> 
> L = ∫₀²π R dt = R·t |₀²π = 2πR  ✓
> ```
> 
> **Ejemplo: Longitud de una hélice**
> 
> ```
> r(t) = (cos(t), sin(t), t),  t ∈ [0, 2π]
> 
> r'(t) = (-sin(t), cos(t), 1)
> 
> |r'(t)| = √(sin²(t) + cos²(t) + 1) = √2
> 
> L = ∫₀²π √2 dt = 2π√2
> ```
> 
> **Tabla de longitudes comunes:**
> 
> | Curva | Parametrización | |r'(t)| | Longitud (0 a 2π) | |-------|----------------|---------|-------------------| | **Círculo** | (R·cos t, R·sin t, 0) | R | 2πR | | **Hélice** | (R·cos t, R·sin t, ct) | √(R²+c²) | 2π√(R²+c²) | | **Elipse** | (a·cos t, b·sin t, 0) | Complicado | Integral elíptica |

---
## 📊 Problemas Resueltos Paso a Paso

### 📝 Problema 1: Plano y Paraboloide

> [!example] 🎯 Enunciado y Solución Completa
> 
> **Enunciado:** Encuentre la curva de intersección entre:
> 
> ```
> S₁ (Paraboloide): z = x² + y²
> S₂ (Plano):       z = 4
> ```
> 
> **Paso 1: Plantear el sistema**
> 
> ```
> z = x² + y²  ... (1)
> z = 4        ... (2)
> ```
> 
> **Paso 2: Igualar**
> 
> ```
> x² + y² = 4
> ```
> 
> Esta es un círculo de radio 2 en el plano z = 4.
> 
> **Paso 3: Parametrizar**
> 
> ```
> x(t) = 2·cos(t)
> y(t) = 2·sin(t)
> z(t) = 4
> 
> t ∈ [0, 2π]
> ```
> 
> **Paso 4: Vector posición**
> 
> ```
> r(t) = (2cos(t), 2sin(t), 4)
> ```
> 
> **Paso 5: Propiedades**
> 
> Vector tangente:
> 
> ```
> r'(t) = (-2sin(t), 2cos(t), 0)
> ```
> 
> Rapidez:
> 
> ```
> |r'(t)| = √(4sin²(t) + 4cos²(t)) = 2
> ```
> 
> Longitud total:
> 
> ```
> L = ∫₀²π 2 dt = 4π
> ```
> 
> **Visualización:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_09.svg]]

### 📝 Problema 2: Esfera y Cilindro

> [!example] 🎯 Problema Más Complejo
> 
> **Enunciado:** Encuentre las curvas de intersección entre:
> 
> ```
> S₁ (Esfera):   x² + y² + z² = 9
> S₂ (Cilindro): x² + y² = 4
> ```
> 
> **Paso 1: Sustituir**
> 
> De S₂: x² + y² = 4
> 
> Sustituir en S₁:
> 
> ```
> 4 + z² = 9
> z² = 5
> z = ±√5
> ```
> 
> **Paso 2: Identificar las curvas**
> 
> Dos círculos:
> 
> - C₁: x² + y² = 4, z = √5
> - C₂: x² + y² = 4, z = -√5
> 
> **Paso 3: Parametrizar**
> 
> **Curva C₁:**
> 
> ```
> r₁(t) = (2cos(t), 2sin(t), √5)
> t ∈ [0, 2π]
> ```
> 
> **Curva C₂:**
> 
> ```
> r₂(t) = (2cos(t), 2sin(t), -√5)
> t ∈ [0, 2π]
> ```
> 
> **Paso 4: Análisis geométrico**
> 
> |Propiedad|Valor|
> |---|---|
> |**Radio de círculos**|2|
> |**Separación vertical**|2√5|
> |**Longitud cada curva**|4π|
> |**Simetría**|Respecto a plano xy|
> 
> **Interpretación:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_10.svg]]
> 
> **Verificación:**
> 
> Para t = 0:
> 
> ```
> r₁(0) = (2, 0, √5)
> 
> Verificar en esfera:
> 2² + 0² + (√5)² = 4 + 5 = 9 ✓
> 
> Verificar en cilindro:
> 2² + 0² = 4 ✓
> ```

### 📝 Problema 3: Dos Paraboloides

> [!example] 🎯 Caso Avanzado
> 
> **Enunciado:**
> 
> ```
> S₁: z = x² + y²      (paraboloide hacia arriba)
> S₂: z = 8 - x² - y²  (paraboloide hacia abajo)
> ```
> 
> **Paso 1: Igualar**
> 
> ```
> x² + y² = 8 - x² - y²
> 2(x² + y²) = 8
> x² + y² = 4
> ```
> 
> **Paso 2: Encontrar z**
> 
> ```
> z = x² + y² = 4
> ```
> 
> **Paso 3: Curva de intersección**
> 
> Círculo en el plano z = 4:
> 
> ```
> x² + y² = 4
> z = 4
> ```
> 
> **Parametrización:**
> 
> ```
> r(t) = (2cos(t), 2sin(t), 4)
> t ∈ [0, 2π]
> ```
> 
> **Interpretación geométrica:**
> 
> Los dos paraboloides se tocan en un círculo que es:
> 
> - El "borde superior" del paraboloide inferior
> - El "borde inferior" del paraboloide superior
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_11.svg]]

---

## 🎓 Ejercicios Propuestos

> [!note] 💪 Problemas para Practicar
> 
> ### Nivel Básico
> 
> **1. Plano y Esfera**
> 
> ```
> Encuentre la intersección de:
> • Esfera: x² + y² + z² = 16
> • Plano: z = 2
> 
> Respuesta esperada: Círculo de radio...?
> ```
> 
> **2. Dos Planos**
> 
> ```
> Intersección de:
> • Plano 1: x + y + z = 1
> • Plano 2: x - y + 2z = 3
> 
> Respuesta: Recta (parametrizarla)
> ```
> 
> ### Nivel Intermedio
> 
> **3. Cilindro y Esfera**
> 
> ```
> • Cilindro: x² + z² = 1
> • Esfera: x² + y² + z² = 4
> 
> Encuentre las dos curvas de intersección
> ```
> 
> **4. Cono y Plano**
> 
> ```
> • Cono: z² = x² + y²
> • Plano: z = 2
> 
> ¿Qué tipo de curva resulta?
> ```
> 
> ### Nivel Avanzado
> 
> **5. Dos Cilindros Oblicuos**
> 
> ```
> • x² + y² = 1
> • y² + z² = 1
> 
> Encuentre todas las curvas de intersección
> ```
> 
> **6. Hiperboloide y Esfera**
> 
> ```
> • Hiperboloide: x² + y² - z² = 1
> • Esfera: x² + y² + z² = 9
> 
> Analice el número de componentes de la intersección
> ```
> 
> ### Problemas de Aplicación
> 
> **7. Topografía**
> 
> ```
> Una montaña tiene perfil z = 100e^(-(x²+y²)/50)
> Encuentre la curva de nivel a altura z = 50
> ```
> 
> **8. Trayectoria Restringida**
> 
> ```
> Una partícula se mueve sobre:
> • Esfera: x² + y² + z² = 25
> • Plano: x + 2y + 2z = 5
> 
> Encuentre su trayectoria y velocidad si |dr/dt| = 2
> ```

---

## 🔗 Conexión con Otros Temas

> [!quote] 🌟 Temas Relacionados
> 
> **Diagrama de conceptos:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_12.svg]]
> 
> **Progresión del aprendizaje:**
> 
> |Tema Previo|Tema Actual|Tema Siguiente|
> |---|---|---|
> |Superficies cuadráticas|**Intersección de superficies**|Integral de línea|
> |Curvas planas|**Curvas espaciales**|Integral de superficie|
> |Derivadas parciales|**Vector tangente**|Curvatura y torsión|
> |Producto vectorial|**Cálculo de normales**|Teorema de Stokes|
> 
> **Conexiones profundas:**
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_13.svg]]

---

## 📚 Resumen y Puntos Clave

> [!success] ✅ Conceptos Fundamentales
> 
> ### Ideas Centrales
> 
> |Concepto|Descripción|Fórmula Clave|
> |---|---|---|
> |**Intersección**|Puntos que satisfacen ambas superficies|F₁ = 0 ∧ F₂ = 0|
> |**Parametrización**|Expresar curva con un parámetro|**r**(t) = (x(t), y(t), z(t))|
> |**Vector tangente**|Dirección de la curva|**T** = **r**'/\|**r**'\||
> |**Longitud de arco**|Distancia recorrida|L = ∫\|**r**'(t)\| dt|
> 
> ### Métodos de Solución
> 
> ![[Diagramas/03_–_Curvas_como_intersección_de_superficies_14.svg]]
> 
> ### Checklist de Resolución
> 
> - [ ] Identificar las dos superficies (F₁ = 0, F₂ = 0)
> - [ ] Elegir método apropiado (sustitución, eliminación, numérico)
> - [ ] Resolver sistema para encontrar relación entre x, y, z
> - [ ] Parametrizar la curva resultante
> - [ ] Calcular vector tangente r'(t)
> - [ ] Verificar solución sustituyendo en ambas ecuaciones
> - [ ] Analizar propiedades geométricas (si se requiere)
> 
> ### Errores Comunes
> 
> |Error|Corrección|
> |---|---|
> |Olvidar dominio del parámetro|Especificar t ∈ [a, b]|
> |No verificar en ambas superficies|Sustituir en F₁ y F₂|
> |Confundir curva con superficie|Una curva tiene 1 parámetro|
> |Ignorar casos múltiples|Pueden haber varias curvas|

---

**Tags:** #cálculo-vectorial #superficies #intersección #curvas-espaciales #parametrización #vector-tangente #geometría-3d #aplicaciones #mermaid #diagramas
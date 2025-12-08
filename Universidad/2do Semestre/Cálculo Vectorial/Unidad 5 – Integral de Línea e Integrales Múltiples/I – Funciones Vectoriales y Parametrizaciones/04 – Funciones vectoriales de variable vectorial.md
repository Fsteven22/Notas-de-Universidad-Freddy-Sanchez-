# 🎯 Funciones Vectoriales de Variable Vectorial

## 🌐 Fundamentos de Funciones Vectoriales

> [!info]- 💡 Introducción a las Funciones Vectoriales Multivariables Las **funciones vectoriales de variable vectorial** son transformaciones que toman vectores como entrada y producen vectores como salida. Generalizan las funciones escalares f(x, y, z) y las funciones vectoriales r(t) al permitir múltiples variables de entrada.
> 
> **Analogías útiles:**
> 
> - **Transformaciones geométricas:** Rotar, escalar o deformar objetos en el espacio
> - **Campos de velocidad:** En cada punto del espacio hay un vector velocidad
> - **Campos electromagnéticos:** Campo eléctrico **E**(x, y, z) asigna un vector a cada punto
> - **Flujo de fluidos:** El vector velocidad del fluido en cada posición
> 
> **Diferencias fundamentales:**
> 
> - **Función escalar:** f: ℝⁿ → ℝ (entrada vector, salida número)
> - **Función vectorial paramétrica:** r: ℝ → ℝⁿ (entrada número, salida vector)
> - **Función vectorial de variable vectorial:** **F**: ℝⁿ → ℝᵐ (entrada vector, salida vector)
> 
> **Importancia histórica:**
> 
> - **Leonhard Euler (1755):** Ecuaciones de movimiento de fluidos
> - **Carl Friedrich Gauss (1813):** Teoría del potencial y campos
> - **James Clerk Maxwell (1865):** Ecuaciones del electromagnetismo
> - **Josiah Willard Gibbs (1881):** Análisis vectorial moderno
> - **Oliver Heaviside (1884):** Operadores diferenciales vectoriales

### 📝 Definición Formal

> [!note]- 🌟 Concepto Matemático **Definición:**
> 
> Una **función vectorial de variable vectorial** es una función:
> 
> **F**: D ⊆ ℝⁿ → ℝᵐ
> 
> que asigna a cada vector **x** = (x₁, x₂, ..., xₙ) en el dominio D un vector **F(x)** = (F₁(**x**), F₂(**x**), ..., Fₘ(**x**)) en ℝᵐ.
> 
> **Notaciones equivalentes:**
> 
> - **F**(**x**) = (F₁(**x**), F₂(**x**), ..., Fₘ(**x**))
> - **F**(x₁, x₂, ..., xₙ) = ⟨F₁, F₂, ..., Fₘ⟩
> - **F** = F₁**e**₁ + F₂**e**₂ + ... + Fₘ**e**ₘ (base canónica)
> 
> **Casos particulares importantes:**
> 
> **1. Campo vectorial en ℝ²:**
> 
> ```
> F: ℝ² → ℝ²
> F(x, y) = (P(x, y), Q(x, y))
> ```
> 
> **2. Campo vectorial en ℝ³:**
> 
> ```
> F: ℝ³ → ℝ³
> F(x, y, z) = (P(x, y, z), Q(x, y, z), R(x, y, z))
> ```
> 
> O en notación con vectores base:
> 
> ```
> F(x, y, z) = P(x, y, z)**i** + Q(x, y, z)**j** + R(x, y, z)**k**
> ```
> 
> **3. Transformación del plano al espacio:**
> 
> ```
> F: ℝ² → ℝ³
> F(u, v) = (x(u, v), y(u, v), z(u, v))
> ```
> 
> Usada para parametrizar superficies.
> 
> **Componentes:**
> 
> - **F₁, F₂, ..., Fₘ:** son las **funciones componentes** (escalares)
> - Cada Fᵢ es una función escalar: Fᵢ: ℝⁿ → ℝ

### 🎨 Interpretación Geométrica

> [!tip]- 👁️ Visualización de Campos Vectoriales **Representación gráfica:**
> 
> Un campo vectorial **F**: ℝⁿ → ℝᵐ se visualiza dibujando:
> 
> **1. Para campos en ℝ² → ℝ²:**
> 
> - En cada punto (x, y) del plano, dibujar el vector **F**(x, y)
> - El vector puede partir del punto o estar centrado en él
> - La longitud representa la magnitud ||**F**(x, y)||
> - La dirección muestra hacia dónde "apunta" el campo
> 
> **2. Para campos en ℝ³ → ℝ³:**
> 
> - En cada punto (x, y, z) del espacio, dibujar el vector **F**(x, y, z)
> - Visualización más compleja, a menudo se usan cortes o muestreo
> 
> **3. Líneas de flujo (streamlines):**
> 
> - Curvas tangentes al campo vectorial en cada punto
> - Soluciones de la EDO: d**r**/dt = **F**(**r**)
> - Muestran cómo "fluiría" una partícula en el campo
> 
> **Características visuales importantes:**
> 
> **Campos uniformes:**
> 
> - Todos los vectores tienen la misma magnitud y dirección
> - Ejemplo: **F**(x, y) = (1, 2) — campo constante
> 
> **Campos radiales:**
> 
> - Vectores apuntan hacia/desde un punto central
> - Ejemplo: **F**(x, y) = (x, y) — expansión desde origen
> 
> **Campos rotacionales:**
> 
> - Vectores circulan alrededor de un eje
> - Ejemplo: **F**(x, y) = (-y, x) — rotación antihoraria
> 
> **Campos gradientes:**
> 
> - Apuntan en dirección de máximo crecimiento de una función escalar
> - Perpendiculares a curvas de nivel

## 🔵 Campos Vectoriales en ℝ²

### 📐 Definición y Ejemplos

> [!example]- 🎯 Campos en el Plano **Campo vectorial en ℝ²:**
> 
> **F**: ℝ² → ℝ² **F**(x, y) = (P(x, y), Q(x, y)) = P(x, y)**i** + Q(x, y)**j**
> 
> donde P y Q son funciones escalares de dos variables.
> 
> **Ejemplo 1: Campo constante**
> 
> ```
> F(x, y) = (3, -2)
> 
> En todo punto del plano, el vector es el mismo.
> Aplicación: Viento uniforme, campo gravitacional cerca de la Tierra.
> ```
> 
> **Ejemplo 2: Campo radial (expansión)**
> 
> ```
> F(x, y) = (x, y)
> 
> En cada punto, el vector apunta radialmente hacia afuera.
> Magnitud: ||F(x, y)|| = √(x² + y²) = r
> 
> Puntos específicos:
> (1, 0)  → F = (1, 0)
> (0, 2)  → F = (0, 2)
> (-1, 1) → F = (-1, 1)
> ```
> 
> **Ejemplo 3: Campo radial (contracción)**
> 
> ```
> F(x, y) = (-x, -y)
> 
> Vectores apuntan hacia el origen.
> Aplicación: Fuerza gravitacional, atracción hacia un punto.
> ```
> 
> **Ejemplo 4: Campo rotacional**
> 
> ```
> F(x, y) = (-y, x)
> 
> Vectores perpendiculares al radio.
> Magnitud: ||F(x, y)|| = √(x² + y²) = r
> 
> Puntos específicos:
> (1, 0)  → F = (0, 1)   — apunta "arriba"
> (0, 1)  → F = (-1, 0)  — apunta "izquierda"
> (-1, 0) → F = (0, -1)  — apunta "abajo"
> (0, -1) → F = (1, 0)   — apunta "derecha"
> 
> Rotación antihoraria alrededor del origen.
> ```
> 
> **Ejemplo 5: Campo gravitacional**
> 
> ```
> F(x, y) = -k(x, y)/(x² + y²)^(3/2)
> 
> Fuerza inversamente proporcional al cuadrado de la distancia.
> Magnitud: ||F|| = k/r²
> ```
> 
> **Ejemplo 6: Campo gradiente**
> 
> ```
> Si f(x, y) = x² + y², entonces:
> F(x, y) = ∇f = (∂f/∂x, ∂f/∂y) = (2x, 2y)
> 
> Apunta en dirección de máximo crecimiento de f.
> Perpendicular a las curvas de nivel f(x, y) = c.
> ```

### 🌀 Propiedades de Campos en ℝ²

> [!success]- 📊 Análisis de Campos Planos **Dado F(x, y) = (P(x, y), Q(x, y)):**
> 
> **1. Magnitud del campo:**
> 
> ```
> ||F(x, y)|| = √[P(x, y)² + Q(x, y)²]
> ```
> 
> Mide la "intensidad" del campo en cada punto.
> 
> **2. Campo vectorial unitario:**
> 
> ```
> F̂(x, y) = F(x, y)/||F(x, y)||  (donde F ≠ 0)
> ```
> 
> Indica solo la dirección, normalizado a longitud 1.
> 
> **3. Divergencia (2D):**
> 
> ```
> div F = ∇ · F = ∂P/∂x + ∂Q/∂y
> ```
> 
> Mide la "expansión" o "compresión" del campo:
> 
> - div F > 0: fuente (expansión)
> - div F < 0: sumidero (contracción)
> - div F = 0: campo incompresible
> 
> **4. Rotacional escalar (2D):**
> 
> ```
> rot F = ∂Q/∂x - ∂P/∂y
> ```
> 
> Mide la "rotación" del campo:
> 
> - rot F > 0: rotación antihoraria
> - rot F < 0: rotación horaria
> - rot F = 0: campo irrotacional
> 
> **Ejemplos de cálculo:**
> 
> **Campo F(x, y) = (x, y):**
> 
> ```
> P = x, Q = y
> 
> div F = ∂x/∂x + ∂y/∂y = 1 + 1 = 2
> (fuente uniforme)
> 
> rot F = ∂y/∂x - ∂x/∂y = 0 - 0 = 0
> (sin rotación)
> ```
> 
> **Campo F(x, y) = (-y, x):**
> 
> ```
> P = -y, Q = x
> 
> div F = ∂(-y)/∂x + ∂x/∂y = 0 + 0 = 0
> (incompresible)
> 
> rot F = ∂x/∂x - ∂(-y)/∂y = 1 - (-1) = 2
> (rotación uniforme antihoraria)
> ```

### 🔄 Líneas de Flujo en ℝ²

> [!warning]- 🌊 Trayectorias del Campo **Definición:**
> 
> Una **línea de flujo** (o línea de corriente) de un campo vectorial **F**(x, y) = (P, Q) es una curva **r**(t) = (x(t), y(t)) tal que en cada punto, el vector tangente es paralelo al campo:
> 
> **d**r**/dt = **F**(**r**(t))**
> 
> **Sistema de EDOs:**
> 
> ```
> dx/dt = P(x, y)
> dy/dt = Q(x, y)
> ```
> 
> **Forma diferencial:**
> 
> ```
> dy/dx = Q(x, y)/P(x, y)  (cuando P ≠ 0)
> ```
> 
> **Ejemplos:**
> 
> **1. Campo F(x, y) = (1, 2):**
> 
> ```
> dx/dt = 1  →  x(t) = t + C₁
> dy/dt = 2  →  y(t) = 2t + C₂
> 
> Eliminando t: y = 2x + (C₂ - 2C₁)
> 
> Líneas de flujo: rectas con pendiente 2
> ```
> 
> **2. Campo F(x, y) = (x, y):**
> 
> ```
> dx/dt = x  →  x(t) = Ae^t
> dy/dt = y  →  y(t) = Be^t
> 
> Eliminando t: y/x = B/A = constante
> 
> Líneas de flujo: rectas que pasan por el origen
> ```
> 
> **3. Campo F(x, y) = (-y, x):**
> 
> ```
> dx/dt = -y
> dy/dt = x
> 
> Multiplicando primera por x, segunda por y:
> x dx/dt = -xy
> y dy/dt = xy
> 
> Sumando: x dx/dt + y dy/dt = 0
> d(x² + y²)/dt = 0
> 
> x² + y² = R² (constante)
> 
> Líneas de flujo: circunferencias concéntricas
> ```

## 🌐 Campos Vectoriales en ℝ³

### 📐 Definición y Ejemplos

> [!example]- 🎯 Campos en el Espacio **Campo vectorial en ℝ³:**
> 
> **F**: ℝ³ → ℝ³ **F**(x, y, z) = (P(x, y, z), Q(x, y, z), R(x, y, z))
> 
> O en notación con vectores base: **F** = P**i** + Q**j** + R**k**
> 
> **Ejemplo 1: Campo constante**
> 
> ```
> F(x, y, z) = (1, 0, 2)
> 
> Mismo vector en todo el espacio.
> Aplicación: Campo magnético uniforme.
> ```
> 
> **Ejemplo 2: Campo radial (expansión desde origen)**
> 
> ```
> F(x, y, z) = (x, y, z)
> 
> Vectores apuntan radialmente hacia afuera.
> Magnitud: ||F|| = √(x² + y² + z²) = r
> 
> Puntos específicos:
> (1, 0, 0) → F = (1, 0, 0)
> (1, 1, 0) → F = (1, 1, 0)
> (1, 1, 1) → F = (1, 1, 1)
> ```
> 
> **Ejemplo 3: Campo gravitacional**
> 
> ```
> F(x, y, z) = -GM(x, y, z)/(x² + y² + z²)^(3/2)
> 
> Ley de gravitación de Newton.
> Magnitud: ||F|| = GM/r²
> ```
> 
> **Ejemplo 4: Campo rotacional alrededor del eje Z**
> 
> ```
> F(x, y, z) = (-y, x, 0)
> 
> Rotación en planos z = constante.
> Similar al campo 2D pero extendido a 3D.
> ```
> 
> **Ejemplo 5: Campo helicoidal**
> 
> ```
> F(x, y, z) = (-y, x, 1)
> 
> Combina rotación (en XY) con componente vertical constante.
> Líneas de flujo: hélices.
> ```
> 
> **Ejemplo 6: Campo eléctrico de una carga puntual**
> 
> ```
> F(x, y, z) = kQ(x, y, z)/(x² + y² + z²)^(3/2)
> 
> Ley de Coulomb.
> Si Q > 0: campo apunta hacia afuera (repulsión)
> Si Q < 0: campo apunta hacia adentro (atracción)
> ```
> 
> **Ejemplo 7: Campo velocidad de un fluido**
> 
> ```
> F(x, y, z) = (y, -x, z²)
> 
> Componentes xy: rotación
> Componente z: dependiente de altura
> ```

### 🧮 Operadores Diferenciales

> [!note]- 🔢 Divergencia y Rotacional **Dado F(x, y, z) = (P, Q, R) = P**i** + Q**j** + R**k****
> 
> **1. Operador nabla (∇):**
> 
> ```
> ∇ = (∂/∂x, ∂/∂y, ∂/∂z) = ∂/∂x **i** + ∂/∂y **j** + ∂/∂z **k**
> ```
> 
> **2. Gradiente de una función escalar f:**
> 
> ```
> ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)
> ```
> 
> El gradiente es un campo vectorial que apunta en dirección de máximo crecimiento.
> 
> **3. Divergencia (∇ · F):**
> 
> ```
> div F = ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z
> ```
> 
> **Interpretación:**
> 
> - Mide la "expansión" o "fuente" del campo
> - div F > 0: fuente (flujo saliente neto)
> - div F < 0: sumidero (flujo entrante neto)
> - div F = 0: campo solenoidal (incompresible)
> 
> **4. Rotacional (∇ × F):**
> 
> ```
> rot F = ∇ × F = | **i**    **j**    **k**  |
>                  | ∂/∂x  ∂/∂y  ∂/∂z |
>                  |  P     Q     R   |
> 
> = (∂R/∂y - ∂Q/∂z)**i** + (∂P/∂z - ∂R/∂x)**j** + (∂Q/∂x - ∂P/∂y)**k**
> ```
> 
> **Interpretación:**
> 
> - Mide la "rotación" o "circulación" del campo
> - ||rot F|| indica la velocidad angular local
> - Dirección de rot F: eje de rotación (regla mano derecha)
> - rot F = **0**: campo irrotacional (conservativo)
> 
> **5. Laplaciano de una función escalar:**
> 
> ```
> ∇²f = ∇ · (∇f) = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²
> ```
> 
> **6. Laplaciano vectorial:**
> 
> ```
> ∇²F = (∇²P, ∇²Q, ∇²R)
> ```

### 📊 Ejemplos de Cálculo

> [!example]- 🧮 Aplicación de Operadores **Ejemplo 1: Campo radial F(x, y, z) = (x, y, z)**
> 
> ```
> P = x, Q = y, R = z
> 
> Divergencia:
> div F = ∂x/∂x + ∂y/∂y + ∂z/∂z = 1 + 1 + 1 = 3
> 
> Interpretación: Fuente uniforme en todo el espacio.
> 
> Rotacional:
> rot F = | **i**   **j**   **k** |
>         | ∂/∂x  ∂/∂y  ∂/∂z|
>         |  x     y     z  |
> 
> = (∂z/∂y - ∂y/∂z)**i** + (∂x/∂z - ∂z/∂x)**j** + (∂y/∂x - ∂x/∂y)**k**
> = (0 - 0)**i** + (0 - 0)**j** + (0 - 0)**k**
> = **0**
> 
> Interpretación: Campo irrotacional (no hay circulación).
> ```
> 
> **Ejemplo 2: Campo rotacional F(x, y, z) = (-y, x, 0)**
> 
> ```
> P = -y, Q = x, R = 0
> 
> Divergencia:
> div F = ∂(-y)/∂x + ∂x/∂y + ∂(0)/∂z = 0 + 0 + 0 = 0
> 
> Interpretación: Campo incompresible.
> 
> Rotacional:
> rot F = (∂0/∂y - ∂x/∂z)**i** + (∂(-y)/∂z - ∂0/∂x)**j** + (∂x/∂x - ∂(-y)/∂y)**k**
>       = (0 - 0)**i** + (0 - 0)**j** + (1 - 0)**k**
>       = (0, 0, 2)
> 
> Interpretación: Rotación alrededor del eje Z con velocidad angular 1.
> ```
> 
> **Ejemplo 3: Campo F(x, y, z) = (yz, xz, xy)**
> 
> ```
> P = yz, Q = xz, R = xy
> 
> Divergencia:
> div F = ∂(yz)/∂x + ∂(xz)/∂y + ∂(xy)/∂z
>       = 0 + 0 + 0 = 0
> 
> Rotacional:
> rot F = (∂(xy)/∂y - ∂(xz)/∂z)**i** + (∂(yz)/∂z - ∂(xy)/∂x)**j** + (∂(xz)/∂x - ∂(yz)/∂y)**k**
>       = (x - x)**i** + (y - y)**j** + (z - z)**k**
>       = **0**
> 
> Campo solenoidal (div = 0) e irrotacional (rot = 0).
> ```
> 
> **Ejemplo 4: Campo gravitacional F = -GM**r**/r³**
> 
> ```
> F(x, y, z) = -GM(x, y, z)/(x² + y² + z²)^(3/2)
> 
> Sea r = √(x² + y² + z²)
> 
> Divergencia (para r ≠ 0):
> div F = 0  (cálculo largo, usar identidad)
> 
> Pero: ∫∫ F · dS sobre esfera = -4πGM ≠ 0
> (hay "fuente" en el origen)
> 
> Rotacional:
> rot F = 0  (campo conservativo)
> ```

## 🔄 Campos Conservativos

### 🎯 Definición y Propiedades

> [!warning]- ⚡ Campos con Función Potencial **Definición:**
> 
> Un campo vectorial **F** es **conservativo** si existe una función escalar φ (llamada **función potencial**) tal que:
> 
> **F** = ∇φ
> 
> Es decir:
> 
> ```
> P = ∂φ/∂x
> Q = ∂φ/∂y
> R = ∂φ/∂z  (en 3D)
> ```
> 
> **Condición necesaria y suficiente (en dominios simplemente conexos):**
> 
> **F** es conservativo ⟺ **rot F** = **0**
> 
> **Propiedades fundamentales:**
> 
> **1. Independencia del camino:**
> 
> ```
> ∫C F · dr  solo depende de puntos inicial y final, no del camino C
> ```
> 
> **2. Teorema Fundamental:**
> 
> ```
> ∫C ∇φ · dr = φ(B) - φ(A)
> ```
> 
> donde A y B son los extremos de la curva C.
> 
> **3. Integral en curva cerrada:**
> 
> ```
> ∮C F · dr = 0  para toda curva cerrada C
> ```
> 
> **4. Trabajo:**
> 
> El trabajo realizado por un campo conservativo es independiente del camino y solo depende del cambio en el potencial.

### 🔍 Verificación y Cálculo del Potencial

> [!tip]- 🛠️ Método para Encontrar φ **Pasos para verificar si F es conservativo y encontrar φ:**
> 
> **Paso 1: Verificar rot F = 0**
> 
> En ℝ²: ∂Q/∂x = ∂P/∂y En ℝ³: Calcular rot F y verificar que sea **0**
> 
> **Paso 2: Integrar la primera componente:**
> 
> ```
> φ(x, y, z) = ∫ P(x, y, z) dx + g(y, z)
> ```
> 
> donde g(y, z) es una "constante" de integración (función de y, z).
> 
> **Paso 3: Derivar respecto a y y comparar con Q:**
> 
> ```
> ∂φ/∂y = Q(x, y, z)
> ```
> 
> Resolver para g'_y(y, z).
> 
> **Paso 4: Integrar respecto a y:**
> 
> ```
> g(y, z) = ∫ g'_y(y, z) dy + h(z)
> ```
> 
> **Paso 5: Derivar respecto a z y comparar con R:**
> 
> ```
> ∂φ/∂z = R(x, y, z)
> ```
> 
> Resolver para h'(z).
> 
> **Paso 6: Integrar y obtener φ completo.**
> 
> **Ejemplo detallado:**
> 
> **F**(x, y, z) = (yz, xz, xy)
> 
> ```
> Paso 1: Verificar
> rot F = (x - x, y - y, z - z) = (0, 0, 0) ✓
> 
> Paso 2: Integrar P = yz
> φ = ∫ yz dx = xyz + g(y, z)
> 
> Paso 3: Derivar respecto a y
> ∂φ/∂y = xz + ∂g/∂y = Q = xz
> ∴ ∂g/∂y = 0  →  g(y, z) = h(z)
> 
> Paso 4: Ahora φ = xyz + h(z)
> 
> Paso 5: Derivar respecto a z
> ∂φ/∂z = xy + h'(z) = R = xy
> ∴ h'(z) = 0  →  h(z) = C (constante)
> 
> Solución:
> φ(x, y, z) = xyz + C
> 
> Verificación:
> ∇φ = (yz, xz, xy) = F ✓
> ```

## 🎨 Superficies Paramétricas

### 📐 Definición

> [!success]- 🌊 Parametrización de Superficies **Definición:**
> 
> Una **superficie paramétrica** es una función:
> 
> **r**: D ⊆ ℝ² → ℝ³ **r**(u, v) = (x(u, v), y(u, v), z(u, v))
> 
> donde D es una región del plano uv (dominio de parametrización).
> 
> **Interpretación:**
> 
> - Cada par (u, v) genera un punto en la superficie
> - **r**(u, v) "mapea" el dominio D sobre la superficie S
> - Las curvas u = constante y v = constante son las **curvas coordenadas**
> 
> **Notación alternativa:**
> 
> ```
> r(u, v) = x(u, v)**i** + y(u, v)**j** + z(u, v)**k**
> ```
> 
> **Ejemplo básico: Plano**
> 
> ```
> r(u, v) = (u, v, 2u + 3v)
> 
> Describe el plano z = 2x + 3y
> ```

### 📊 Ejemplos Clásicos

> [!example]- 🎪 Superficies Importantes **Ejemplo 1: Plano general**
> 
> ```
> r(u, v) = P₀ + u**a** + v**b**
> 
> donde:
> - P₀: punto base
> - **a**, **b**: vectores directores (no paralelos)
> 
> Específico:
> r(u, v) = (1, 2, 3) + u(1, 0, 1) + v(0, 1, 2)
>         = (1 + u, 2- v, 3 + u + 2v)
> ```
> 
> **Ejemplo 2: Esfera de radio R**
> ```
> 
> r(θ, φ) = (R sin φ cos θ, R sin φ sin θ, R cos φ)
> 
> donde:
> 
> - θ ∈ [0, 2π]: ángulo azimutal
> - φ ∈ [0, π]: ángulo polar
> 
> Para R = 1: r(θ, φ) = (sin φ cos θ, sin φ sin θ, cos φ)
> 
> Puntos específicos: φ = 0: (0, 0, 1) — polo norte φ = π: (0, 0, -1) — polo sur φ = π/2, θ=0: (1, 0, 0) — ecuador
> 
> ```
> 
> **Ejemplo 3: Cilindro circular**
> ```
> 
> r(θ, z) = (R cos θ, R sin θ, z)
> 
> θ ∈ [0, 2π], z ∈ ℝ
> 
> Para R = 2: r(θ, z) = (2 cos θ, 2 sin θ, z)
> 
> Curvas coordenadas:
> 
> - θ = const: líneas verticales
> - z = const: circunferencias horizontales
> 
> ```
> 
> **Ejemplo 4: Cono**
> ```
> 
> r(θ, z) = (z cos θ, z sin θ, z)
> 
> θ ∈ [0, 2π], z ≥ 0
> 
> Radio aumenta linealmente con la altura. Pendiente del cono: 45° (ángulo con horizontal)
> 
> ```
> 
> **Ejemplo 5: Toro (rosquilla)**
> ```
> 
> r(u, v) = ((R + r cos v) cos u, (R + r cos v) sin u, r sin v)
> 
> donde:
> 
> - R: radio mayor (del centro al centro del tubo)
> - r: radio menor (radio del tubo)
> - u, v ∈ [0, 2π]
> 
> Para R = 3, r = 1: r(u, v) = ((3 + cos v) cos u, (3 + cos v) sin u, sin v)
> 
> ```
> 
> **Ejemplo 6: Paraboloide**
> ```
> 
> r(u, v) = (u, v, u² + v²)
> 
> Superficie z = x² + y²
> 
> Curvas coordenadas:
> 
> - u = const: parábolas en planos verticales
> - v = const: parábolas en planos verticales
> 
> ```
> 
> **Ejemplo 7: Superficie de revolución**
> 
> Rotar la curva z = f(x) alrededor del eje Z:
> ```
> 
> r(θ, t) = (t cos θ, t sin θ, f(t))
> 
> Ejemplo (rotar z = x²): r(θ, t) = (t cos θ, t sin θ, t²)
> ```

### 🧮 Vectores Tangentes y Normal

> [!note]- 📐 Geometría de Superficies **Dada r(u, v) = (x(u, v), y(u, v), z(u, v)):**
> 
> **1. Vectores tangentes parciales:**
> 
> ```
> rᵤ = ∂r/∂u = (∂x/∂u, ∂y/∂u, ∂z/∂u)
> rᵥ = ∂r/∂v = (∂x/∂v, ∂y/∂v, ∂z/∂v)
> ```
> 
> - **rᵤ**: tangente a curvas v = constante
> - **rᵥ**: tangente a curvas u = constante
> - Generan el plano tangente en cada punto
> 
> **2. Vector normal:**
> 
> ```
> **N** = rᵤ × rᵥ
> ```
> 
> - Perpendicular a la superficie
> - Magnitud: ||**N**|| = área del paralelogramo formado por rᵤ y rᵥ
> 
> **3. Vector normal unitario:**
> 
> ```
> **n** = **N**/||**N**|| = (rᵤ × rᵥ)/||rᵤ × rᵥ||
> ```
> 
> **4. Área de elemento de superficie:**
> 
> ```
> dS = ||rᵤ × rᵥ|| du dv
> ```
> 
> **Ejemplo (esfera unitaria):**
> 
> ```
> r(θ, φ) = (sin φ cos θ, sin φ sin θ, cos φ)
> 
> rθ = (-sin φ sin θ, sin φ cos θ, 0)
> rφ = (cos φ cos θ, cos φ sin θ, -sin φ)
> 
> N = rθ × rφ = | **i**              **j**             **k**        |
>               | -sin φ sin θ   sin φ cos θ      0         |
>               | cos φ cos θ    cos φ sin θ    -sin φ     |
> 
>   = (sin² φ cos θ, sin² φ sin θ, sin φ cos φ)
> 
> ||N|| = sin φ
> 
> n = (sin φ cos θ, sin φ sin θ, cos φ) = r(θ, φ)
> 
> El vector normal apunta radialmente hacia afuera ✓
> ```

## 💪 Ejercicios Integrales

> [!example]- 🎯 Práctica Completa **Nivel 1 - Básico:** 🟢
> 
> **1.** Dado el campo **F**(x, y) = (2x, 3y), calcular: a) **F**(1, 2) b) ||**F**(1, 2)|| c) Dibujar el campo en algunos puntos
> 
> **Solución:**
> 
> ```
> a) F(1, 2) = (2·1, 3·2) = (2, 6)
> 
> b) ||F(1, 2)|| = ||(2, 6)|| = √(4 + 36) = √40 = 2√10 ≈ 6.32
> 
> c) Puntos:
> (0, 0) → (0, 0)
> (1, 0) → (2, 0)
> (0, 1) → (0, 3)
> (1, 1) → (2, 3)
> (2, 1) → (4, 3)
> 
> Campo de expansión, más fuerte en y que en x.
> ```
> 
> **2.** Calcular la divergencia y rotacional de **F**(x, y, z) = (x², y², z²).
> 
> **Solución:**
> 
> ```
> P = x², Q = y², R = z²
> 
> div F = ∂(x²)/∂x + ∂(y²)/∂y + ∂(z²)/∂z
>       = 2x + 2y + 2z
> 
> rot F = (∂(z²)/∂y - ∂(y²)/∂z, ∂(x²)/∂z - ∂(z²)/∂x, ∂(y²)/∂x - ∂(x²)/∂y)
>       = (0 - 0, 0 - 0, 0 - 0)
>       = (0, 0, 0)
> 
> Campo irrotacional pero no solenoidal.
> ```
> 
> ---
> 
> **Nivel 2 - Intermedio:** 🟡
> 
> **3.** Verificar si **F**(x, y, z) = (2xy, x² + 2yz, y²) es conservativo. Si lo es, encontrar la función potencial φ.
> 
> **Solución:**
> 
> ```
> P = 2xy, Q = x² + 2yz, R = y²
> 
> Verificar rot F = 0:
> ∂R/∂y - ∂Q/∂z = ∂(y²)/∂y - ∂(x² + 2yz)/∂z = 2y - 2y = 0 ✓
> ∂P/∂z - ∂R/∂x = ∂(2xy)/∂z - ∂(y²)/∂x = 0 - 0 = 0 ✓
> ∂Q/∂x - ∂P/∂y = ∂(x² + 2yz)/∂x - ∂(2xy)/∂y = 2x - 2x = 0 ✓
> 
> Es conservativo.
> 
> Encontrar φ:
> ∂φ/∂x = 2xy  →  φ = ∫ 2xy dx = x²y + g(y, z)
> 
> ∂φ/∂y = x² + ∂g/∂y = x² + 2yz
> ∴ ∂g/∂y = 2yz  →  g = y²z + h(z)
> 
> φ = x²y + y²z + h(z)
> 
> ∂φ/∂z = y² + h'(z) = y²
> ∴ h'(z) = 0  →  h(z) = C
> 
> φ(x, y, z) = x²y + y²z + C
> 
> Verificación:
> ∇φ = (2xy, x² + 2yz, y²) = F ✓
> ```
> 
> **4.** Parametrizar el cilindro x² + y² = 9 entre z = 0 y z = 5.
> 
> **Solución:**
> 
> ```
> r(θ, z) = (3 cos θ, 3 sin θ, z)
> 
> donde θ ∈ [0, 2π], z ∈ [0, 5]
> 
> Vectores tangentes:
> rθ = (-3 sin θ, 3 cos θ, 0)
> rz = (0, 0, 1)
> 
> Normal:
> N = rθ × rz = (3 cos θ, 3 sin θ, 0)
> 
> Vector normal unitario:
> n = (cos θ, sin θ, 0) (apunta hacia afuera)
> ```
> 
> ---
> 
> **Nivel 3 - Avanzado:** 🔴
> 
> **5.** Encontrar las líneas de flujo del campo **F**(x, y) = (y, -x).
> 
> **Solución:**
> 
> ```
> Sistema de EDOs:
> dx/dt = y
> dy/dt = -x
> 
> Derivando la primera:
> d²x/dt² = dy/dt = -x
> 
> Ecuación diferencial: d²x/dt² + x = 0
> 
> Solución general:
> x(t) = A cos t + B sin t
> 
> Entonces:
> y(t) = dx/dt = -A sin t + B cos t
> 
> Eliminando t (usando x² + y² = A² + B²):
> x² + y² = R² (constante)
> 
> Líneas de flujo: circunferencias concéntricas.
> Orientación: horaria (porque F apunta perpendicular hacia "dentro")
> ```
> 
> **6.** Calcular el área de la superficie parametrizada por: **r**(u, v) = (u cos v, u sin v, u), 0 ≤ u ≤ 2, 0 ≤ v ≤ 2π
> 
> **Solución:**
> 
> ```
> rᵤ = (cos v, sin v, 1)
> rᵥ = (-u sin v, u cos v, 0)
> 
> N = rᵤ × rᵥ = | **i**      **j**      **k**  |
>               | cos v    sin v      1    |
>               | -u sin v  u cos v   0    |
> 
>   = (-u cos v, -u sin v, u)
> 
> ||N|| = √(u² cos² v + u² sin² v + u²)
>       = √(u² + u²)
>       = u√2
> 
> Área:
> A = ∫∫ ||N|| du dv
>   = ∫₀²π ∫₀² u√2 du dv
>   = ∫₀²π [u²√2/2]₀² dv
>   = ∫₀²π 2√2 dv
>   = 2√2 · 2π
>   = 4π√2
> ```
> 
> **7.** Dado el campo **F**(x, y, z) = (y² + z², 2xy, 2xz), determinar si es conservativo y calcular el trabajo a lo largo de cualquier curva de (0, 0, 0) a (1, 2, 3).
> 
> **Solución:**
> 
> ```
> P = y² + z², Q = 2xy, R = 2xz
> 
> Verificar rot F:
> ∂R/∂y - ∂Q/∂z = 0 - 0 = 0 ✓
> ∂P/∂z - ∂R/∂x = 2z - 2z = 0 ✓
> ∂Q/∂x - ∂P/∂y = 2y - 2y = 0 ✓
> 
> Es conservativo.
> 
> Encontrar φ:
> ∂φ/∂x = y² + z²  →  φ = x(y² + z²) + g(y, z)
> 
> ∂φ/∂y = 2xy + ∂g/∂y = 2xy
> ∴ ∂g/∂y = 0  →  g(y, z) = h(z)
> 
> φ = x(y² + z²) + h(z)
> 
> ∂φ/∂z = 2xz + h'(z) = 2xz
> ∴ h'(z) = 0  →  h = C
> 
> φ(x, y, z) = x(y² + z²) + C
> 
> Trabajo:
> W = φ(1, 2, 3) - φ(0, 0, 0)
>   = 1(4 + 9) - 0
>   = 13
> 
> El trabajo es 13 unidades, independiente del camino.
> ```

## 🎓 Consejos de Estudio

> [!tip]- 🧠 Estrategias de Dominio **Para dominar funciones vectoriales de variable vectorial:**
> 
> **1. Visualización:**
> 
> - Dibujar campos vectoriales a mano en cuadrículas
> - Usar software: MATLAB, Python (Matplotlib), GeoGebra
> - Identificar patrones: radiales, rotacionales, mixtos
> - Observar líneas de flujo y equipotenciales
> 
> **2. Cálculo de operadores:**
> 
> - Memorizar fórmulas de div, rot, ∇
> - Practicar productos cruz sistemáticamente
> - Verificar resultados con propiedades (div(rot F) = 0, etc.)
> 
> **3. Campos conservativos:**
> 
> - Siempre verificar rot F = 0 primero
> - Método sistemático para encontrar φ
> - Practicar con varios ejemplos
> 
> **4. Superficies paramétricas:**
> 
> - Identificar el tipo de superficie (esfera, cilindro, etc.)
> - Calcular vectores tangentes y normales
> - Visualizar curvas coordenadas
> 
> **Errores comunes a evitar:**
> 
> ❌ **Error 1:** Confundir div y rot
> 
> - div F es un escalar (en 3D)
> - rot F es un vector (en 3D)
> 
> ❌ **Error 2:** Orden incorrecto en producto cruz
> 
> - **a** × **b** ≠ **b** × **a**
> - **a** × **b** = -(**b** × **a**)
> 
> ❌ **Error 3:** Olvidar verificar rot F = 0
> 
> - No todos los campos son conservativos
> - Verificar antes de buscar φ
> 
> ❌ **Error 4:** Signos en el rotacional
> 
> - Usar determinante 3×3 cuidadosamente
> - Verificar cada componente
> 
> ❌ **Error 5:** Confundir rᵤ × rᵥ con rᵥ × rᵤ
> 
> - El orden determina la orientación del normal
> - Afecta el signo en integrales de superficie

## 🔗 Referencias a Otras Notas

> [!quote]- 🌟 Conexiones Conceptuales
> 
> **Fundamentos previos (Prerequisites):**
> 
> - [[02 - Vectores en R3]] - Operaciones vectoriales y producto cruz
> - [[02 - Parametrizaciones en R2]] - Curvas planas como introducción
> - [[03 - Parametrizaciones en R3]] - Curvas espaciales
> - [[Derivadas Parciales]] - ∂f/∂x, ∂f/∂y para funciones multivariables
> - [[Cálculo Diferencial Multivariable]] - Gradiente y derivadas direccionales
> - [[Funciones de Varias Variables]] - Dominio, rango, gráficas
> 
> **Operadores diferenciales:**
> 
> - [[Gradiente]] - ∇f, dirección de máximo crecimiento
> - [[Divergencia]] - ∇ · F, medida de "fuente"
> - [[Rotacional]] - ∇ × F, medida de "circulación"
> - [[Laplaciano]] - ∇²f, divergencia del gradiente
> - [[Identidades Vectoriales]] - div(rot F) = 0, rot(∇f) = 0
> 
> **Campos vectoriales especiales:**
> 
> - [[Campos Conservativos]] - F = ∇φ, trabajo independiente del camino
> - [[Campos Solenoidales]] - div F = 0, sin fuentes ni sumideros
> - [[Campos Irrotacionales]] - rot F = 0, sin circulación
> - [[Campos Armónicos]] - ∇²φ = 0, ecuación de Laplace
> - [[Campo Gravitacional]] - Ley de Newton, F ∝ 1/r²
> - [[Campo Eléctrico]] - Ley de Coulomb
> - [[Campo Magnético]] - Ley de Biot-Savart
> 
> **Integrales vectoriales:**
> 
> - [[Integrales de Línea Escalares]] - ∫C f ds
> - [[Integrales de Línea Vectoriales]] - ∫C F · dr (trabajo)
> - [[Integrales de Superficie]] - ∫∫S F · dS (flujo)
> - [[Integrales de Volumen]] - ∫∫∫V f dV
> 
> **Teoremas fundamentales:**
> 
> - [[Teorema Fundamental para Integrales de Línea]] - Para campos conservativos
> - [[Teorema de Green]] - Relaciona integral de línea con doble integral
> - [[Teorema de la Divergencia (Gauss)]] - ∫∫S F · dS = ∫∫∫V div F dV
> - [[Teorema de Stokes]] - ∫C F · dr = ∫∫S (rot F) · dS
> - [[Teorema de la Divergencia 2D]] - Caso plano del teorema de Gauss
> 
> **Superficies paramétricas:**
> 
> - [[Parametrización de Superficies]] - r(u, v)
> - [[Plano Tangente]] - Generado por rᵤ y rᵥ
> - [[Vector Normal a Superficie]] - N = rᵤ × rᵥ
> - [[Primera Forma Fundamental]] - Métrica en superficies
> - [[Segunda Forma Fundamental]] - Curvatura de superficies
> - [[Área de Superficies]] - ∫∫ ||rᵤ × rᵥ|| du dv
> 
> **Superficies clásicas:**
> 
> - [[Esfera]] - Parametrización esférica
> - [[Cilindro]] - Parametrización cilíndrica
> - [[Cono]] - Superficie de revolución
> - [[Toro]] - Superficie toroidal
> - [[Paraboloide]] - Elíptico e hiperbólico
> - [[Hiperboloide]] - De una y dos hojas
> - [[Superficie de Revolución]] - Rotar curva alrededor de eje
> 
> **Aplicaciones en física:**
> 
> - [[Ecuaciones de Maxwell]] - Electromagnetismo
> - [[Ley de Gauss]] - Flujo eléctrico
> - [[Ley de Ampère]] - Circulación magnética
> - [[Ley de Faraday]] - Inducción electromagnética
> - [[Ecuación de Continuidad]] - Conservación de masa/carga
> - [[Mecánica de Fluidos]] - Ecuaciones de Euler y Navier-Stokes
> - [[Termodinámica]] - Flujo de calor, ecuación de difusión
> 
> **Ecuaciones diferenciales:**
> 
> - [[Ecuación de Laplace]] - ∇²φ = 0
> - [[Ecuación de Poisson]] - ∇²φ = ρ
> - [[Ecuación de Onda]] - ∂²u/∂t² = c²∇²u
> - [[Ecuación de Calor]] - ∂u/∂t = α∇²u
> - [[Ecuación de Difusión]] - ∂c/∂t = D∇²c
> 
> **Geometría diferencial:**
> 
> - [[Curvas en Superficies]] - Geodésicas
> - [[Curvatura Gaussiana]] - K = κ₁κ₂
> - [[Curvatura Media]] - H = (κ₁ + κ₂)/2
> - [[Coordenadas Curvilíneas]] - Esféricas, cilíndricas
> - [[Formas Diferenciales]] - Generalización moderna
> - [[Variedades Diferenciables]] - Espacios curvos abstractos
> 
> **Análisis vectorial avanzado:**
> 
> - [[Teorema de Helmholtz]] - Descomposición de campos
> - [[Potencial Vector]] - A tal que B = rot A
> - [[Función de Green]] - Soluciones fundamentales
> - [[Campos Armónicos Esféricos]] - Expansión en esféricos
> - [[Transformada de Fourier Vectorial]] - Análisis frecuencial
> 
> **Herramientas computacionales:**
> 
> - [[MATLAB - Quiver]] - Visualización de campos vectoriales
> - [[Python - Matplotlib Quiver3D]] - Campos en 3D
> - [[Mathematica - VectorPlot3D]] - Campos vectoriales
> - [[GeoGebra 3D - Campos]] - Visualización interactiva
> - [[ParaView]] - Visualización científica avanzada
> 
> **Tópicos relacionados:**
> 
> - [[Coordenadas Generalizadas]] - Mecánica Lagrangiana
> - [[Tensor Métrico]] - Geometría Riemanniana
> - [[Cálculo Tensorial]] - Generalización de vectores
> - [[Análisis Complejo]] - Campos en el plano complejo
> - [[Teoría de Potencial]] - Física matemática
> - [[Homología y Cohomología]] - Topología algebraica

---

**Tags:** #funciones-vectoriales #campos-vectoriales #divergencia #rotacional #gradiente #superficies-paramétricas #campos-conservativos #operadores-diferenciales #flujo #circulación #teoremas-fundamentales #análisis-vectorial #R2 #R3 #university #matemáticas #física-matemática #referencias #enlaces-conceptuales

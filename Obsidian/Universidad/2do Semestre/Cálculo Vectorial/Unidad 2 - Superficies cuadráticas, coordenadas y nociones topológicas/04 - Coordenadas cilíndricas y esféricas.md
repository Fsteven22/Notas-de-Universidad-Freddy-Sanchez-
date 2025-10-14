# 🌐 Coordenadas Cilíndricas y Esféricas

## 🎯 Fundamentos de los Sistemas de Coordenadas

> [!info]- 💡 Introducción a los Sistemas de Coordenadas Curvilíneos Los **sistemas de coordenadas cilíndricas y esféricas** son extensiones naturales del sistema cartesiano que aprovechan las simetrías geométricas de ciertos problemas. Mientras que las coordenadas cartesianas (x, y, z) son ideales para geometría rectangular, las coordenadas curvilíneas simplifican enormemente problemas con simetría circular o esférica.
> 
> **Analogías útiles:**
> 
> - **Coordenadas cilíndricas:** Sistema de direcciones polares con altura (edificio circular con pisos)
> - **Coordenadas esféricas:** Sistema GPS invertido (latitud, longitud, altitud desde el centro)
> - **Mapas geográficos:** Proyecciones de la esfera terrestre
> - **Radar:** Ángulo, distancia y elevación
> 
> **Importancia histórica:**
> 
> - **Euler (1748):** Formalización de coordenadas polares
> - **Lagrange (1788):** Mecánica analítica en coordenadas generalizadas
> - **Hamilton (1833):** Sistemas canónicos de coordenadas
> - **Maxwell (1873):** Ecuaciones electromagnéticas en esféricas
> 
> **¿Por qué usar coordenadas curvilíneas?**
> 
> - Simplifican ecuaciones con simetrías específicas
> - Facilitan integrales múltiples
> - Naturales para describir movimientos circulares o radiales
> - Esenciales en física (mecánica, electromagnetismo, mecánica cuántica)

### 📊 Comparación de Sistemas

> [!note]- 🌟 Tres Sistemas Principales
> 
> |Sistema|Coordenadas|Mejor para|Simetría|
> |---|---|---|---|
> |**Cartesiano**|(x, y, z)|Geometría rectangular|Traslacional|
> |**Cilíndrico**|(r, θ, z)|Cilindros, rotación alrededor de eje|Rotacional (eje z)|
> |**Esférico**|(ρ, φ, θ)|Esferas, problemas radiales|Rotacional (punto central)|
> 
> **Criterios de selección:**
> 
> 1. **Usar cilíndricas cuando:**
>     - Hay simetría alrededor de un eje (z)
>     - Objetos cilíndricos o tubulares
>     - Rotación en plano horizontal
>     - Ejemplos: cables, tuberías, campos magnéticos de cables
> 2. **Usar esféricas cuando:**
>     - Hay simetría radial desde un punto
>     - Objetos esféricos
>     - Problemas gravitacionales o electrostáticos puntuales
>     - Ejemplos: planetas, átomos, antenas omnidireccionales
> 3. **Usar cartesianas cuando:**
>     - No hay simetrías especiales
>     - Geometría rectangular o cúbica
>     - Simplifica los cálculos más que curvilíneas

## 🔵 Coordenadas Cilíndricas

### 📐 Definición y Conversión

> [!example]- 🟢 Sistema de Coordenadas Cilíndricas (r, θ, z)
> 
> **Definición:** El sistema de coordenadas cilíndricas extiende las coordenadas polares 2D al espacio 3D añadiendo una coordenada de altura z.
> 
> **Las tres coordenadas:**
> 
> 1. **r (radio):** Distancia del punto al eje z (en el plano xy)
>     - Rango: r ≥ 0
>     - r = 0 corresponde al eje z
> 2. **θ (ángulo azimutal):** Ángulo medido desde el eje x positivo
>     - Rango: 0 ≤ θ < 2π (o -π < θ ≤ π)
>     - Medido en sentido antihorario (vista desde arriba)
> 3. **z (altura):** Coordenada vertical (igual que en cartesianas)
>     - Rango: -∞ < z < ∞
>     - Mide elevación sobre el plano xy
> 
> **Conversión: Cilíndricas → Cartesianas**
> 
> $$\begin{cases} x = r\cos\theta \ y = r\sin\theta \ z = z \end{cases}$$
> 
> **Conversión: Cartesianas → Cilíndricas**
> 
> $$\begin{cases} r = \sqrt{x^2 + y^2} \ \theta = \arctan\left(\frac{y}{x}\right) \text{ (con ajuste de cuadrante)} \ z = z \end{cases}$$
> 
> **Ajuste de cuadrante para θ:**
> 
> ```python
> import numpy as np
> 
> def cartesianas_a_cilindricas(x, y, z):
>     """
>     Conversión con manejo correcto de cuadrantes
>     """
>     r = np.sqrt(x**2 + y**2)
>     theta = np.arctan2(y, x)  # arctan2 maneja cuadrantes automáticamente
>     return r, theta, z
> 
> # Alternativa manual:
> def theta_manual(x, y):
>     if x > 0:
>         return np.arctan(y/x)
>     elif x < 0 and y >= 0:
>         return np.arctan(y/x) + np.pi
>     elif x < 0 and y < 0:
>         return np.arctan(y/x) - np.pi
>     elif x == 0 and y > 0:
>         return np.pi/2
>     elif x == 0 and y < 0:
>         return -np.pi/2
>     else:  # x == 0 and y == 0
>         return 0  # Indefinido, por convención
> ```

### 🎨 Superficies de Coordenadas Constantes

> [!tip]- 📏 Familias de Superficies
> 
> **1. r = constante (r = r₀)**
> 
> - **Superficie:** Cilindro circular de radio r₀ con eje en z
> - **Ecuación cartesiana:** x² + y² = r₀²
> - **Descripción:** Todos los puntos a distancia fija del eje z
> - **Ejemplo:** r = 3 es un cilindro de radio 3
> 
> **2. θ = constante (θ = θ₀)**
> 
> - **Superficie:** Semiplano vertical que contiene el eje z
> - **Ecuación cartesiana:** y = x tan(θ₀)
> - **Descripción:** Plano que forma ángulo θ₀ con el eje x
> - **Ejemplo:** θ = π/4 es el plano y = x (para x ≥ 0)
> 
> **3. z = constante (z = z₀)**
> 
> - **Superficie:** Plano horizontal a altura z₀
> - **Ecuación cartesiana:** z = z₀
> - **Descripción:** Paralelo al plano xy
> - **Ejemplo:** z = 5 es un plano horizontal a 5 unidades sobre xy
> 
> **Visualización:**
> 
> ```
>        z↑
>         |
>         |_____ Plano z = z₀
>         |
>         |    /| Semiplano θ = θ₀
>         |   / |
>         |  /  |
>         | /   | Cilindro r = r₀
>         |/____|________→ y
>        /
>       /
>      x
> ```
> 
> **Coordenadas curvilíneas ortogonales:** Las tres familias son **mutuamente perpendiculares** en cada punto:
> 
> - Las líneas r = constante son perpendiculares a θ = constante
> - Las líneas z = constante son perpendiculares a ambas

### ✅ Ejemplos de Conversión

> [!example]- 💪 Casos Prácticos
> 
> **Ejemplo 1 - Conversión básica (Cartesianas → Cilíndricas):**
> 
> Punto P(3, 3, 4) en cartesianas:
> 
> ```
> r = √(3² + 3²) = √18 = 3√2 ≈ 4.24
> θ = arctan(3/3) = arctan(1) = π/4 = 45°
> z = 4
> 
> Respuesta: (3√2, π/4, 4) o (4.24, 0.785, 4)
> ```
> 
> **Ejemplo 2 - Conversión con cuadrante (Cartesianas → Cilíndricas):**
> 
> Punto Q(-2, 2√3, -1):
> 
> ```
> r = √((-2)² + (2√3)²) = √(4 + 12) = 4
> θ = arctan(2√3/-2) = arctan(-√3)
>   Cuadrante II: θ = π - π/3 = 2π/3 ≈ 120°
> z = -1
> 
> Respuesta: (4, 2π/3, -1)
> ```
> 
> **Ejemplo 3 - Conversión (Cilíndricas → Cartesianas):**
> 
> Punto R(5, π/6, 2):
> 
> ```
> x = 5 cos(π/6) = 5 · √3/2 = 5√3/2 ≈ 4.33
> y = 5 sin(π/6) = 5 · 1/2 = 5/2 = 2.5
> z = 2
> 
> Respuesta: (5√3/2, 5/2, 2) o (4.33, 2.5, 2)
> ```
> 
> **Ejemplo 4 - Ecuación de superficie:**
> 
> Convertir x² + y² = 9 a cilíndricas:
> 
> ```
> Sustituir: x² + y² = r²
> r² = 9
> r = 3
> 
> Respuesta: r = 3 (cilindro de radio 3)
> ```
> 
> **Ejemplo 5 - Ecuación más compleja:**
> 
> Convertir x² + y² + z² = 16 a cilíndricas:
> 
> ```
> Sustituir: x² + y² = r²
> r² + z² = 16
> 
> Respuesta: r² + z² = 16 (esfera de radio 4)
> ```
> 
> **Ejemplo 6 - Ecuación con ángulo:**
> 
> Convertir y = x a cilíndricas:
> 
> ```
> y = x
> r sin θ = r cos θ
> sin θ = cos θ
> tan θ = 1
> θ = π/4 (para r > 0)
> 
> Respuesta: θ = π/4 (semiplano)
> ```

### 🧮 Vectores Unitarios y Diferenciales

> [!note]- 📐 Base Vectorial Cilíndrica
> 
> **Vectores unitarios:**
> 
> 1. **êᵣ (radial):** Apunta desde el eje z hacia el punto $$\hat{\mathbf{e}}_r = \cos\theta,\hat{\mathbf{i}} + \sin\theta,\hat{\mathbf{j}}$$
>     
> 2. **êθ (tangencial):** Perpendicular a êᵣ, en dirección de θ creciente $$\hat{\mathbf{e}}_\theta = -\sin\theta,\hat{\mathbf{i}} + \cos\theta,\hat{\mathbf{j}}$$
>     
> 3. **êz (axial):** Paralelo al eje z $$\hat{\mathbf{e}}_z = \hat{\mathbf{k}}$$
>     
> 
> **Propiedades:**
> 
> - Son ortogonales: êᵣ · êθ = êᵣ · êz = êθ · êz = 0
> - Son unitarios: |êᵣ| = |êθ| = |êz| = 1
> - **IMPORTANTE:** êᵣ y êθ varían con la posición (dependen de θ)
> 
> **Derivadas de vectores unitarios:**
> 
> $$\frac{\partial\hat{\mathbf{e}}_r}{\partial\theta} = \hat{\mathbf{e}}_\theta$$
> 
> $$\frac{\partial\hat{\mathbf{e}}_\theta}{\partial\theta} = -\hat{\mathbf{e}}_r$$
> 
> $$\frac{\partial\hat{\mathbf{e}}_z}{\partial\theta} = \mathbf{0}$$
> 
> **Elemento de longitud (diferencial):**
> 
> $$d\mathbf{s} = dr,\hat{\mathbf{e}}_r + r,d\theta,\hat{\mathbf{e}}_\theta + dz,\hat{\mathbf{e}}_z$$
> 
> **Longitud de arco:**
> 
> $$ds^2 = dr^2 + r^2d\theta^2 + dz^2$$
> 
> **Elemento de volumen:**
> 
> $$dV = r,dr,d\theta,dz$$
> 
> **NOTA CRUCIAL:** El factor r aparece en dV (no es simplemente dr dθ dz)

### 📊 Integrales en Coordenadas Cilíndricas

> [!success]- 🟢 Integración Triple
> 
> **Forma general:**
> 
> $$\iiint_V f(x,y,z),dV = \int_{\alpha}^{\beta}\int_{h_1(\theta)}^{h_2(\theta)}\int_{g_1(r,\theta)}^{g_2(r,\theta)} f(r\cos\theta, r\sin\theta, z) \cdot r,dz,dr,d\theta$$
> 
> **Región típica:**
> 
> - α ≤ θ ≤ β (ángulo)
> - h₁(θ) ≤ r ≤ h₂(θ) (radio)
> - g₁(r,θ) ≤ z ≤ g₂(r,θ) (altura)
> 
> **Orden de integración:** Puede variar: dz dr dθ, dr dθ dz, etc., según la región
> 
> **Ejemplo 1 - Volumen de cilindro:**
> 
> Cilindro: 0 ≤ r ≤ R, 0 ≤ θ ≤ 2π, 0 ≤ z ≤ h
> 
> $$V = \int_0^{2\pi}\int_0^R\int_0^h r,dz,dr,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^R rh,dr,d\theta$$
> 
> $$= \int_0^{2\pi} \frac{R^2h}{2},d\theta = \pi R^2h$$
> 
> **Ejemplo 2 - Masa de sólido con densidad variable:**
> 
> Densidad: ρ(r, θ, z) = r² + z Región: 0 ≤ r ≤ 2, 0 ≤ θ ≤ π, 0 ≤ z ≤ 3
> 
> $$M = \int_0^\pi\int_0^2\int_0^3 (r^2 + z) \cdot r,dz,dr,d\theta$$
> 
> $$= \int_0^\pi\int_0^2 r\left[r^2z + \frac{z^2}{2}\right]_0^3 dr,d\theta$$
> 
> $$= \int_0^\pi\int_0^2 r(3r^2 + 4.5),dr,d\theta$$
> 
> $$= \int_0^\pi \left[\frac{3r^4}{4} + \frac{4.5r^2}{2}\right]_0^2 d\theta$$
> 
> $$= \int_0^\pi (12 + 9),d\theta = 21\pi$$
> 
> **Ejemplo 3 - Volumen bajo superficie:**
> 
> Volumen bajo z = 4 - r² y sobre el plano xy, dentro del cilindro r = 2:
> 
> $$V = \int_0^{2\pi}\int_0^2\int_0^{4-r^2} r,dz,dr,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^2 r(4-r^2),dr,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^2 (4r - r^3),dr,d\theta$$
> 
> $$= \int_0^{2\pi} \left[2r^2 - \frac{r^4}{4}\right]_0^2 d\theta$$
> 
> $$= \int_0^{2\pi} (8 - 4),d\theta = 8\pi$$

### 🎯 Aplicaciones Físicas en Cilíndricas

> [!example]- ⚡ Casos de Uso
> 
> **1. Campo eléctrico de cable infinito:**
> 
> Cable cargado a lo largo del eje z con densidad lineal λ:
> 
> $$\mathbf{E} = \frac{\lambda}{2\pi\epsilon_0 r},\hat{\mathbf{e}}_r$$
> 
> - Campo solo radial (simetría cilíndrica)
> - No depende de θ ni z
> - Inversamente proporcional a r
> 
> **2. Campo magnético de corriente:**
> 
> Corriente I por cable en eje z (Ley de Ampère):
> 
> $$\mathbf{B} = \frac{\mu_0 I}{2\pi r},\hat{\mathbf{e}}_\theta$$
> 
> - Campo tangencial (círculos concéntricos)
> - Regla de la mano derecha
> 
> **3. Movimiento circular:**
> 
> Partícula en movimiento circular uniforme:
> 
> $$\mathbf{r}(t) = R,\hat{\mathbf{e}}_r$$
> 
> $$\mathbf{v}(t) = R\omega,\hat{\mathbf{e}}_\theta$$
> 
> $$\mathbf{a}(t) = -R\omega^2,\hat{\mathbf{e}}_r$$
> 
> (aceleración centrípeta)
> 
> **4. Flujo en tuberías:**
> 
> Velocidad de fluido en tubería cilíndrica (flujo de Poiseuille):
> 
> $$v(r) = v_{\max}\left(1 - \frac{r^2}{R^2}\right),\hat{\mathbf{e}}_z$$
> 
> - Perfil parabólico
> - Máximo en el centro (r = 0)
> - Cero en las paredes (r = R)

## 🌍 Coordenadas Esféricas

### 📐 Definición y Conversión

> [!example]- 🔴 Sistema de Coordenadas Esféricas (ρ, φ, θ)
> 
> **Definición:** El sistema de coordenadas esféricas describe la posición de un punto mediante su distancia al origen y dos ángulos.
> 
> **Las tres coordenadas:**
> 
> 1. **ρ (rho - radio radial):** Distancia del punto al origen
>     - Rango: ρ ≥ 0
>     - ρ = 0 es el origen
>     - También llamado "r" en física
> 2. **φ (phi - ángulo polar/cenital):** Ángulo desde el eje z positivo
>     - Rango: 0 ≤ φ ≤ π
>     - φ = 0: eje z positivo
>     - φ = π/2: plano xy
>     - φ = π: eje z negativo
>     - También llamado "colatitud" o "θ" en física
> 3. **θ (theta - ángulo azimutal):** Ángulo desde el eje x positivo en el plano xy
>     - Rango: 0 ≤ θ < 2π
>     - Mismo que θ en cilíndricas
>     - Equivalente a la longitud geográfica
> 
> **NOTA:** Existen diferentes convenciones. En matemáticas usamos (ρ, φ, θ), en física a menudo (r, θ, φ). **¡Siempre verificar la convención!**
> 
> **Conversión: Esféricas → Cartesianas**
> 
> $$\begin{cases} x = \rho\sin\phi\cos\theta \ y = \rho\sin\phi\sin\theta \ z = \rho\cos\phi \end{cases}$$
> 
> **Conversión: Cartesianas → Esféricas**
> 
> $$\begin{cases} \rho = \sqrt{x^2 + y^2 + z^2} \ \phi = \arccos\left(\frac{z}{\sqrt{x^2+y^2+z^2}}\right) \ \theta = \arctan\left(\frac{y}{x}\right) \text{ (con ajuste de cuadrante)} \end{cases}$$
> 
> **Conversión: Cilíndricas ↔ Esféricas**
> 
> Cilíndricas → Esféricas: $$\begin{cases} \rho = \sqrt{r^2 + z^2} \ \phi = \arctan\left(\frac{r}{z}\right) \text{ o } \arccos\left(\frac{z}{\sqrt{r^2+z^2}}\right) \ \theta = \theta \end{cases}$$
> 
> Esféricas → Cilíndricas: $$\begin{cases} r = \rho\sin\phi \ \theta = \theta \ z = \rho\cos\phi \end{cases}$$

### 🎨 Superficies de Coordenadas Constantes

> [!tip]- 📏 Familias de Superficies Esféricas
> 
> **1. ρ = constante (ρ = ρ₀)**
> 
> - **Superficie:** Esfera de radio ρ₀ centrada en el origen
> - **Ecuación cartesiana:** x² + y² + z² = ρ₀²
> - **Descripción:** Todos los puntos equidistantes del origen
> - **Ejemplo:** ρ = 5 es una esfera de radio 5
> 
> **2. φ = constante (φ = φ₀)**
> 
> - **Superficie:** Cono circular con vértice en el origen y eje en z
> - **Ecuación cartesiana:** z² = (x² + y²) cot²(φ₀)
> - **Casos especiales:**
>     - φ = 0: eje z positivo (línea)
>     - φ = π/2: plano xy
>     - φ = π: eje z negativo (línea)
> - **Ejemplo:** φ = π/4 es un cono de 45°
> 
> **3. θ = constante (θ = θ₀)**
> 
> - **Superficie:** Semiplano vertical que contiene el eje z
> - **Ecuación cartesiana:** y = x tan(θ₀)
> - **Descripción:** Igual que en cilíndricas
> - **Ejemplo:** θ = π/3 es un semiplano a 60° del eje x
> 
> **Visualización geográfica:**
> 
> ```
> - ρ constante: Superficie de la Tierra (esfera)
> - φ constante: Líneas de latitud constante (paralelos)
> - θ constante: Líneas de longitud constante (meridianos)
> ```
> 
> **Analogía con globo terráqueo:**
> 
> - ρ: altitud sobre/bajo el centro de la Tierra
> - φ: colatitud (0° en Polo Norte, 90° en Ecuador, 180° en Polo Sur)
> - θ: longitud (medida desde meridiano de Greenwich)

### ✅ Ejemplos de Conversión

> [!example]- 💪 Casos Prácticos Esféricos
> 
> **Ejemplo 1 - Conversión básica (Cartesianas → Esféricas):**
> 
> Punto P(1, 1, √2):
> 
> ```
> ρ = √(1² + 1² + (√2)²) = √(1 + 1 + 2) = 2
> 
> φ = arccos(√2/2) = π/4 = 45°
> 
> θ = arctan(1/1) = π/4 = 45°
> 
> Respuesta: (2, π/4, π/4)
> ```
> 
> **Ejemplo 2 - Punto en eje z:**
> 
> Punto Q(0, 0, 5):
> 
> ```
> ρ = 5
> φ = arccos(5/5) = 0
> θ = indefinido (pero por convención θ = 0)
> 
> Respuesta: (5, 0, 0) - sobre eje z positivo
> ```
> 
> **Ejemplo 3 - Conversión (Esféricas → Cartesianas):**
> 
> Punto R(6, π/3, π/4):
> 
> ```
> x = 6 sin(π/3) cos(π/4) 
>   = 6 · (√3/2) · (√2/2) = 3√6/2 ≈ 3.67
> 
> y = 6 sin(π/3) sin(π/4)
>   = 6 · (√3/2) · (√2/2) = 3√6/2 ≈ 3.67
> 
> z = 6 cos(π/3) = 6 · (1/2) = 3
> 
> Respuesta: (3√6/2, 3√6/2, 3)
> ```
> 
> **Ejemplo 4 - Ecuación de superficie:**
> 
> Convertir x² + y² + z² = 25 a esféricas:
> 
> ```
> ρ² = 25
> ρ = 5
> 
> Respuesta: ρ = 5 (esfera de radio 5)
> ¡La más simple posible en esféricas!
> ```
> 
> **Ejemplo 5 - Cono en esféricas:**
> 
> Convertir z = √(x² + y²) a esféricas:
> 
> ```
> ρ cos φ = ρ sin φ
> cos φ = sin φ
> tan φ = 1
> φ = π/4
> 
> Respuesta: φ = π/4 (cono de 45°)
> ```
> 
> **Ejemplo 6 - Cilindro en esféricas:**
> 
> Convertir x² + y² = 4 a esféricas:
> 
> ```
> (ρ sin φ cos θ)² + (ρ sin φ sin θ)² = 4
> ρ² sin² φ (cos² θ + sin² θ) = 4
> ρ² sin² φ = 4
> ρ sin φ = 2
> 
> Respuesta: ρ sin φ = 2 (cilindro de radio 2)
> ¡Más complicado en esféricas!
> ```

### 🧮 Vectores Unitarios y Diferenciales

> [!note]- 📐 Base Vectorial Esférica
> 
> **Vectores unitarios:**
> 
> 1. **êρ (radial):** Apunta desde el origen hacia el punto $$\hat{\mathbf{e}}_\rho = \sin\phi\cos\theta,\hat{\mathbf{i}} + \sin\phi\sin\theta,\hat{\mathbf{j}} + \cos\phi,\hat{\mathbf{k}}$$
>     
> 2. **êφ (polar):** Perpendicular a êρ, en dirección de φ creciente $$\hat{\mathbf{e}}_\phi = \cos\phi\cos\theta,\hat{\mathbf{i}} + \cos\phi\sin\theta,\hat{\mathbf{j}} - \sin\phi,\hat{\mathbf{k}}$$
>     
> 3. **êθ (azimutal):** Perpendicular a ambos, en dirección de θ creciente $$\hat{\mathbf{e}}_\theta = -\sin\theta,\hat{\mathbf{i}} + \cos\theta,\hat{\mathbf{j}}$$
>     
> 
> **Propiedades:**
> > **Propiedades:**
> 
> - Son ortogonales: êρ · êφ = êρ · êθ = êφ · êθ = 0
> - Son unitarios: |êρ| = |êφ| = |êθ| = 1
> - **IMPORTANTE:** Los tres varían con la posición (dependen de φ y θ)
> - Forman un sistema dextrógiro: êρ × êφ = êθ
> 
> **Elemento de longitud (diferencial):**
> 
> $$d\mathbf{s} = d\rho,\hat{\mathbf{e}}_\rho + \rho,d\phi,\hat{\mathbf{e}}_\phi + \rho\sin\phi,d\theta,\hat{\mathbf{e}}_\theta$$
> 
> **Longitud de arco:**
> 
> $$ds^2 = d\rho^2 + \rho^2d\phi^2 + \rho^2\sin^2\phi,d\theta^2$$
> 
> **Elemento de área (sobre esfera ρ = R):**
> 
> $$dA = R^2\sin\phi,d\phi,d\theta$$
> 
> **Elemento de volumen:**
> 
> $$dV = \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> **NOTA CRUCIAL:** El jacobiano ρ² sin φ aparece en dV
> 
> **Factores de escala:**
> 
> - h_ρ = 1
> - h_φ = ρ
> - h_θ = ρ sin φ

### 📊 Integrales en Coordenadas Esféricas

> [!success]- 🟢 Integración Triple en Esféricas
> 
> **Forma general:**
> 
> $$\iiint_V f(x,y,z),dV = \int_{\alpha}^{\beta}\int_{\phi_1}^{\phi_2}\int_{\rho_1(\phi,\theta)}^{\rho_2(\phi,\theta)} f(\rho,\phi,\theta) \cdot \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> **Región típica:**
> 
> - α ≤ θ ≤ β (azimutal: 0 a 2π para revolución completa)
> - φ₁ ≤ φ ≤ φ₂ (polar: 0 a π para esfera completa)
> - ρ₁(φ,θ) ≤ ρ ≤ ρ₂(φ,θ) (radial)
> 
> **Orden estándar:** dρ dφ dθ (pero puede variar)
> 
> **Ejemplo 1 - Volumen de esfera:**
> 
> Esfera de radio R:
> 
> $$V = \int_0^{2\pi}\int_0^\pi\int_0^R \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^\pi \sin\phi\left[\frac{\rho^3}{3}\right]_0^R d\phi,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^\pi \frac{R^3}{3}\sin\phi,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi} \frac{R^3}{3}[-\cos\phi]_0^\pi d\theta$$
> 
> $$= \int_0^{2\pi} \frac{R^3}{3}(-(-1) - (-1)),d\theta = \int_0^{2\pi} \frac{2R^3}{3},d\theta$$
> 
> $$= \frac{2R^3}{3} \cdot 2\pi = \frac{4\pi R^3}{3}$$
> 
> ✓ Fórmula conocida verificada!
> 
> **Ejemplo 2 - Volumen de cono esférico:**
> 
> Región: 0 ≤ ρ ≤ a, 0 ≤ φ ≤ φ₀, 0 ≤ θ ≤ 2π
> 
> $$V = \int_0^{2\pi}\int_0^{\phi_0}\int_0^a \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^{\phi_0} \frac{a^3}{3}\sin\phi,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi} \frac{a^3}{3}[-\cos\phi]_0^{\phi_0} d\theta$$
> 
> $$= \int_0^{2\pi} \frac{a^3}{3}(1 - \cos\phi_0),d\theta$$
> 
> $$= \frac{2\pi a^3}{3}(1 - \cos\phi_0)$$
> 
> **Ejemplo 3 - Masa con densidad variable:**
> 
> Densidad: ρ_masa = ρ (aumenta con la distancia) Región: esfera de radio R
> 
> $$M = \int_0^{2\pi}\int_0^\pi\int_0^R \rho \cdot \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^\pi\int_0^R \rho^3\sin\phi,d\rho,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^\pi \frac{R^4}{4}\sin\phi,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi} \frac{R^4}{4} \cdot 2,d\theta = \pi R^4$$
> 
> **Ejemplo 4 - Volumen entre dos esferas:**
> 
> Cascarón esférico: a ≤ ρ ≤ b
> 
> $$V = \int_0^{2\pi}\int_0^\pi\int_a^b \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> $$= \int_0^{2\pi}\int_0^\pi \frac{b^3 - a^3}{3}\sin\phi,d\phi,d\theta$$
> 
> $$= \frac{4\pi}{3}(b^3 - a^3)$$

### 🎯 Aplicaciones Físicas en Esféricas

> [!example]- ⚡ Casos de Uso Físicos
> 
> **1. Campo gravitacional de masa puntual:**
> 
> Masa M en el origen:
> 
> $$\mathbf{g} = -\frac{GM}{\rho^2},\hat{\mathbf{e}}_\rho$$
> 
> - Campo puramente radial (simetría esférica)
> - No depende de φ ni θ
> - Ley del inverso del cuadrado
> 
> **2. Campo eléctrico de carga puntual:**
> 
> Carga q en el origen:
> 
> $$\mathbf{E} = \frac{kq}{\rho^2},\hat{\mathbf{e}}_\rho$$
> 
> donde k = 1/(4πε₀)
> 
> **3. Funciones de onda del átomo de hidrógeno:**
> 
> Función de onda en mecánica cuántica:
> 
> $$\psi_{nlm}(\rho, \phi, \theta) = R_{nl}(\rho) \cdot Y_l^m(\phi, \theta)$$
> 
> - R_{nl}: parte radial
> - Y_l^m: armónicos esféricos (parte angular)
> - Las coordenadas esféricas son naturales por simetría del átomo
> 
> **4. Momento angular orbital:**
> 
> $$\mathbf{L} = \mathbf{r} \times \mathbf{p}$$
> 
> En esféricas:
> 
> - L_z = -iℏ ∂/∂θ
> - Operadores de momento angular naturalmente expresados
> 
> **5. Potencial gravitacional de esfera:**
> 
> Para esfera uniforme de radio R y masa M:
> 
> $$\Phi(\rho) = \begin{cases} -\frac{3GM}{2R} + \frac{GM\rho^2}{2R^3} & \text{si } \rho < R \ -\frac{GM}{\rho} & \text{si } \rho \geq R \end{cases}$$
> 
> **6. Radiación de antena:**
> 
> Patrón de radiación de dipolo:
> 
> $$I(\phi, \theta) = I_0 \sin^2\phi$$
> 
> - Máxima radiación perpendicular al eje (φ = π/2)
> - Nula en dirección del eje (φ = 0, π)

## 🔄 Tabla Comparativa de Sistemas

> [!note]- 📋 Resumen Completo de Conversiones
> 
> ### Conversiones Cartesianas ↔ Cilíndricas ↔ Esféricas
> 
> |Desde → Hacia|Cartesianas (x, y, z)|Cilíndricas (r, θ, z)|Esféricas (ρ, φ, θ)|
> |---|---|---|---|
> |**Cartesianas**|—|r = √(x²+y²)<br>θ = arctan(y/x)<br>z = z|ρ = √(x²+y²+z²)<br>φ = arccos(z/ρ)<br>θ = arctan(y/x)|
> |**Cilíndricas**|x = r cos θ<br>y = r sin θ<br>z = z|—|ρ = √(r²+z²)<br>φ = arctan(r/z)<br>θ = θ|
> |**Esféricas**|x = ρ sin φ cos θ<br>y = ρ sin φ sin θ<br>z = ρ cos φ|r = ρ sin φ<br>θ = θ<br>z = ρ cos φ|—|
> 
> ### Elementos Diferenciales
> 
> |Sistema|Elemento de Volumen|Elemento de Longitud|
> |---|---|---|
> |**Cartesiano**|dV = dx dy dz|ds² = dx² + dy² + dz²|
> |**Cilíndrico**|dV = r dr dθ dz|ds² = dr² + r²dθ² + dz²|
> |**Esférico**|dV = ρ² sin φ dρ dφ dθ|ds² = dρ² + ρ²dφ² + ρ²sin²φ dθ²|
> 
> ### Superficies de Coordenada Constante
> 
> |Coordenada = cte|Cartesianas|Cilíndricas|Esféricas|
> |---|---|---|---|
> |**Primera**|x = x₀ (plano)|r = r₀ (cilindro)|ρ = ρ₀ (esfera)|
> |**Segunda**|y = y₀ (plano)|θ = θ₀ (semiplano)|φ = φ₀ (cono)|
> |**Tercera**|z = z₀ (plano)|z = z₀ (plano)|θ = θ₀ (semiplano)|

## 💻 Implementación Computacional

### 🐍 Código Python Completo

> [!success]- 🔧 Biblioteca de Conversiones
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> from mpl_toolkits.mplot3d import Axes3D
> 
> class CoordenadasCurvilineas:
>     """
>     Clase para conversión entre sistemas de coordenadas
>     """
>     
>     # ========== CARTESIANAS ↔ CILÍNDRICAS ==========
>     
>     @staticmethod
>     def cart_a_cil(x, y, z):
>         """
>         Convierte cartesianas a cilíndricas
>         
>         Retorna: (r, theta, z)
>         """
>         r = np.sqrt(x**2 + y**2)
>         theta = np.arctan2(y, x)  # Maneja cuadrantes automáticamente
>         return r, theta, z
>     
>     @staticmethod
>     def cil_a_cart(r, theta, z):
>         """
>         Convierte cilíndricas a cartesianas
>         
>         Retorna: (x, y, z)
>         """
>         x = r * np.cos(theta)
>         y = r * np.sin(theta)
>         return x, y, z
>     
>     # ========== CARTESIANAS ↔ ESFÉRICAS ==========
>     
>     @staticmethod
>     def cart_a_esf(x, y, z):
>         """
>         Convierte cartesianas a esféricas
>         
>         Retorna: (rho, phi, theta)
>         """
>         rho = np.sqrt(x**2 + y**2 + z**2)
>         
>         # Evitar división por cero
>         if rho == 0:
>             return 0, 0, 0
>         
>         phi = np.arccos(z / rho)
>         theta = np.arctan2(y, x)
>         
>         return rho, phi, theta
>     
>     @staticmethod
>     def esf_a_cart(rho, phi, theta):
>         """
>         Convierte esféricas a cartesianas
>         
>         Retorna: (x, y, z)
>         """
>         x = rho * np.sin(phi) * np.cos(theta)
>         y = rho * np.sin(phi) * np.sin(theta)
>         z = rho * np.cos(phi)
>         return x, y, z
>     
>     # ========== CILÍNDRICAS ↔ ESFÉRICAS ==========
>     
>     @staticmethod
>     def cil_a_esf(r, theta, z):
>         """
>         Convierte cilíndricas a esféricas
>         
>         Retorna: (rho, phi, theta)
>         """
>         rho = np.sqrt(r**2 + z**2)
>         
>         if rho == 0:
>             return 0, 0, theta
>         
>         phi = np.arctan2(r, z)  # o arccos(z/rho)
>         return rho, phi, theta
>     
>     @staticmethod
>     def esf_a_cil(rho, phi, theta):
>         """
>         Convierte esféricas a cilíndricas
>         
>         Retorna: (r, theta, z)
>         """
>         r = rho * np.sin(phi)
>         z = rho * np.cos(phi)
>         return r, theta, z
>     
>     # ========== VECTORES UNITARIOS ==========
>     
>     @staticmethod
>     def vectores_unitarios_cil(theta):
>         """
>         Calcula vectores unitarios cilíndricos
>         
>         Retorna: e_r, e_theta, e_z (en componentes cartesianas)
>         """
>         e_r = np.array([np.cos(theta), np.sin(theta), 0])
>         e_theta = np.array([-np.sin(theta), np.cos(theta), 0])
>         e_z = np.array([0, 0, 1])
>         return e_r, e_theta, e_z
>     
>     @staticmethod
>     def vectores_unitarios_esf(phi, theta):
>         """
>         Calcula vectores unitarios esféricos
>         
>         Retorna: e_rho, e_phi, e_theta (en componentes cartesianas)
>         """
>         e_rho = np.array([
>             np.sin(phi)*np.cos(theta),
>             np.sin(phi)*np.sin(theta),
>             np.cos(phi)
>         ])
>         
>         e_phi = np.array([
>             np.cos(phi)*np.cos(theta),
>             np.cos(phi)*np.sin(theta),
>             -np.sin(phi)
>         ])
>         
>         e_theta = np.array([
>             -np.sin(theta),
>             np.cos(theta),
>             0
>         ])
>         
>         return e_rho, e_phi, e_theta
> 
> # ========== FUNCIONES DE INTEGRACIÓN ==========
> 
> def integral_triple_cilindrica(f, r_lims, theta_lims, z_lims, n=50):
>     """
>     Calcula integral triple en coordenadas cilíndricas
>     
>     Parámetros:
>     -----------
>     f : function
>         Función f(r, theta, z) a integrar
>     r_lims, theta_lims, z_lims : tuple
>         Límites de integración (min, max)
>     n : int
>         Número de puntos por dimensión
>     
>     Retorna:
>     --------
>     valor : float
>         Aproximación de la integral
>     """
>     r = np.linspace(r_lims[0], r_lims[1], n)
>     theta = np.linspace(theta_lims[0], theta_lims[1], n)
>     z = np.linspace(z_lims[0], z_lims[1], n)
>     
>     dr = r[1] - r[0]
>     dtheta = theta[1] - theta[0]
>     dz = z[1] - z[0]
>     
>     integral = 0
>     for ri in r:
>         for ti in theta:
>             for zi in z:
>                 # Incluir jacobiano r
>                 integral += f(ri, ti, zi) * ri * dr * dtheta * dz
>     
>     return integral
> 
> def integral_triple_esferica(f, rho_lims, phi_lims, theta_lims, n=50):
>     """
>     Calcula integral triple en coordenadas esféricas
>     
>     Parámetros:
>     -----------
>     f : function
>         Función f(rho, phi, theta) a integrar
>     rho_lims, phi_lims, theta_lims : tuple
>         Límites de integración
>     n : int
>         Número de puntos por dimensión
>     
>     Retorna:
>     --------
>     valor : float
>         Aproximación de la integral
>     """
>     rho = np.linspace(rho_lims[0], rho_lims[1], n)
>     phi = np.linspace(phi_lims[0], phi_lims[1], n)
>     theta = np.linspace(theta_lims[0], theta_lims[1], n)
>     
>     drho = rho[1] - rho[0]
>     dphi = phi[1] - phi[0]
>     dtheta = theta[1] - theta[0]
>     
>     integral = 0
>     for ri in rho:
>         for pi in phi:
>             for ti in theta:
>                 # Incluir jacobiano rho^2 * sin(phi)
>                 integral += f(ri, pi, ti) * ri**2 * np.sin(pi) * drho * dphi * dtheta
>     
>     return integral
> 
> # ========== VISUALIZACIÓN ==========
> 
> def graficar_superficie_cilindrica(r_func, theta_range, z_range, n=50):
>     """
>     Grafica superficie en coordenadas cilíndricas
>     
>     Parámetros:
>     -----------
>     r_func : function
>         r = r_func(theta, z)
>     theta_range, z_range : tuple
>         Rangos de parámetros
>     """
>     theta = np.linspace(theta_range[0], theta_range[1], n)
>     z = np.linspace(z_range[0], z_range[1], n)
>     Theta, Z = np.meshgrid(theta, z)
>     
>     R = r_func(Theta, Z)
>     
>     # Convertir a cartesianas
>     X = R * np.cos(Theta)
>     Y = R * np.sin(Theta)
>     
>     # Graficar
>     fig = plt.figure(figsize=(10, 8))
>     ax = fig.add_subplot(111, projection='3d')
>     surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
>     
>     ax.set_xlabel('X')
>     ax.set_ylabel('Y')
>     ax.set_zlabel('Z')
>     ax.set_title('Superficie en Coordenadas Cilíndricas')
>     fig.colorbar(surf, shrink=0.5)
>     
>     return fig, ax
> 
> def graficar_superficie_esferica(rho_func, phi_range, theta_range, n=50):
>     """
>     Grafica superficie en coordenadas esféricas
>     
>     Parámetros:
>     -----------
>     rho_func : function
>         rho = rho_func(phi, theta)
>     phi_range, theta_range : tuple
>         Rangos de parámetros
>     """
>     phi = np.linspace(phi_range[0], phi_range[1], n)
>     theta = np.linspace(theta_range[0], theta_range[1], n)
>     Phi, Theta = np.meshgrid(phi, theta)
>     
>     Rho = rho_func(Phi, Theta)
>     
>     # Convertir a cartesianas
>     X = Rho * np.sin(Phi) * np.cos(Theta)
>     Y = Rho * np.sin(Phi) * np.sin(Theta)
>     Z = Rho * np.cos(Phi)
>     
>     # Graficar
>     fig = plt.figure(figsize=(10, 8))
>     ax = fig.add_subplot(111, projection='3d')
>     surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
>     
>     ax.set_xlabel('X')
>     ax.set_ylabel('Y')
>     ax.set_zlabel('Z')
>     ax.set_title('Superficie en Coordenadas Esféricas')
>     fig.colorbar(surf, shrink=0.5)
>     
>     return fig, ax
> 
> # ========== EJEMPLOS DE USO ==========
> 
> if __name__ == "__main__":
>     
>     print("="*50)
>     print("EJEMPLOS DE CONVERSIÓN")
>     print("="*50)
>     
>     # Ejemplo 1: Cartesianas → Cilíndricas
>     x, y, z = 3, 4, 5
>     r, theta, z_cil = CoordenadasCurvilineas.cart_a_cil(x, y, z)
>     print(f"\nCartesianas ({x}, {y}, {z})")
>     print(f"→ Cilíndricas ({r:.3f}, {theta:.3f} rad = {np.degrees(theta):.1f}°, {z_cil})")
>     
>     # Ejemplo 2: Cartesianas → Esféricas
>     rho, phi, theta_esf = CoordenadasCurvilineas.cart_a_esf(x, y, z)
>     print(f"\nCartesianas ({x}, {y}, {z})")
>     print(f"→ Esféricas ({rho:.3f}, {phi:.3f} rad = {np.degrees(phi):.1f}°, {theta_esf:.3f} rad)")
>     
>     # Ejemplo 3: Volumen de esfera con integral esférica
>     print("\n" + "="*50)
>     print("CÁLCULO DE VOLUMEN DE ESFERA (R=2)")
>     print("="*50)
>     
>     R = 2
>     V_esfera = integral_triple_esferica(
>         lambda rho, phi, theta: 1,  # f = 1 para volumen
>         (0, R), (0, np.pi), (0, 2*np.pi),
>         n=30
>     )
>     V_teorico = (4/3) * np.pi * R**3
>     
>     print(f"Volumen calculado: {V_esfera:.4f}")
>     print(f"Volumen teórico: {V_teorico:.4f}")
>     print(f"Error relativo: {abs(V_esfera - V_teorico)/V_teorico * 100:.2f}%")
>     
>     # Ejemplo 4: Graficar cilindro helicoidal
>     print("\n" + "="*50)
>     print("GENERANDO GRÁFICAS...")
>     print("="*50)
>     
>     # Cilindro con ondulación
>     graficar_superficie_cilindrica(
>         lambda theta, z: 2 + 0.5*np.sin(3*theta),
>         (0, 2*np.pi), (0, 10)
>     )
>     
>     # Esfera con deformación
>     graficar_superficie_esferica(
>         lambda phi, theta: 3 + 0.5*np.cos(3*phi)*np.sin(2*theta),
>         (0, np.pi), (0, 2*np.pi)
>     )
>     
>     plt.show()
> ```

### 🎮 Visualización Interactiva Avanzada

> [!example]- 🌐 Sistema de Coordenadas Interactivo
> 
> ```python
> import plotly.graph_objects as go
> import numpy as np
> 
> def visualizar_sistemas_coordenadas():
>     """
>     Crea visualización interactiva de los tres sistemas
>     """
>     
>     # Punto ejemplo
>     x0, y0, z0 = 3, 4, 5
>     
>     # Conversiones
>     r, theta, z_c = CoordenadasCurvilineas.cart_a_cil(x0, y0, z0)
>     rho, phi, theta_e = CoordenadasCurvilineas.cart_a_esf(x0, y0, z0)
>     
>     fig = go.Figure()
>     
>     # Punto original
>     fig.add_trace(go.Scatter3d(
>         x=[x0], y=[y0], z=[z0],
>         mode='markers',
>         marker=dict(size=10, color='red'),
>         name=f'Punto P({x0},{y0},{z0})'
>     ))
>     
>     # Ejes cartesianos
>     for axis, color in zip(['x', 'y', 'z'], ['red', 'green', 'blue']):
>         line_data = np.zeros((2, 3))
>         if axis == 'x':
>             line_data[:, 0] = [0, 6]
>         elif axis == 'y':
>             line_data[:, 1] = [0, 6]
>         else:
>             line_data[:, 2] = [0, 6]
>         
>         fig.add_trace(go.Scatter3d(
>             x=line_data[:, 0],
>             y=line_data[:, 1],
>             z=line_data[:, 2],
>             mode='lines',
>             line=dict(color=color, width=3),
>             name=f'Eje {axis.upper()}'
>         ))
>     
>     # Cilindro r = cte
>     theta_vals = np.linspace(0, 2*np.pi, 50)
>     z_vals = np.linspace(0, z0, 30)
>     Theta_cil, Z_cil = np.meshgrid(theta_vals, z_vals)
>     X_cil = r * np.cos(Theta_cil)
>     Y_cil = r * np.sin(Theta_cil)
>     
>     fig.add_trace(go.Surface(
>         x=X_cil, y=Y_cil, z=Z_cil,
>         opacity=0.3,
>         colorscale='Blues',
>         showscale=False,
>         name='Cilindro r=cte'
>     ))
>     
>     # Esfera rho = cte
>     phi_vals = np.linspace(0, np.pi, 30)
>     theta_vals2 = np.linspace(0, 2*np.pi, 50)
>     Phi_esf, Theta_esf = np.meshgrid(phi_vals, theta_vals2)
>     X_esf = rho * np.sin(Phi_esf) * np.cos(Theta_esf)
>     Y_esf = rho * np.sin(Phi_esf) * np.sin(Theta_esf)
>     Z_esf = rho * np.cos(Phi_esf)
>     
>     fig.add_trace(go.Surface(
>     ```python
>         x=X_esf, y=Y_esf, z=Z_esf,
>         opacity=0.2,
>         colorscale='Reds',
>         showscale=False,
>         name='Esfera ρ=cte'
>     ))
>     
>     # Configuración
>     fig.update_layout(
>         title=f'Sistemas de Coordenadas<br>Cartesianas: ({x0},{y0},{z0})<br>Cilíndricas: ({r:.2f},{np.degrees(theta):.1f}°,{z_c})<br>Esféricas: ({rho:.2f},{np.degrees(phi):.1f}°,{np.degrees(theta_e):.1f}°)',
>         scene=dict(
>             xaxis_title='X',
>             yaxis_title='Y',
>             zaxis_title='Z',
>             aspectmode='data'
>         ),
>         width=900,
>         height=700
>     )
>     
>     return fig
> 
> # Crear y mostrar visualización
> fig = visualizar_sistemas_coordenadas()
> fig.show()
> 
> # ========== ANIMACIÓN DE ROTACIÓN ==========
> 
> def animar_coordenadas_cilindricas():
>     """
>     Anima un punto moviéndose en coordenadas cilíndricas
>     """
>     from matplotlib.animation import FuncAnimation
>     
>     fig = plt.figure(figsize=(12, 5))
>     
>     # Subplot 1: Vista 3D
>     ax1 = fig.add_subplot(121, projection='3d')
>     
>     # Subplot 2: Proyección XY
>     ax2 = fig.add_subplot(122)
>     
>     # Parámetros
>     r = 3
>     z_final = 10
>     n_frames = 100
>     
>     # Trayectoria completa (hélice)
>     theta_full = np.linspace(0, 4*np.pi, 200)
>     z_full = np.linspace(0, z_final, 200)
>     x_full = r * np.cos(theta_full)
>     y_full = r * np.sin(theta_full)
>     
>     def update(frame):
>         ax1.clear()
>         ax2.clear()
>         
>         # Posición actual
>         idx = int(frame * len(theta_full) / n_frames)
>         theta_now = theta_full[idx]
>         z_now = z_full[idx]
>         x_now = x_full[idx]
>         y_now = y_full[idx]
>         
>         # Vista 3D
>         ax1.plot(x_full[:idx], y_full[:idx], z_full[:idx], 'b-', alpha=0.5, linewidth=1)
>         ax1.scatter([x_now], [y_now], [z_now], c='red', s=100, marker='o')
>         
>         # Cilindro guía
>         theta_cil = np.linspace(0, 2*np.pi, 50)
>         z_cil = np.linspace(0, z_final, 20)
>         Theta_cil, Z_cil = np.meshgrid(theta_cil, z_cil)
>         X_cil = r * np.cos(Theta_cil)
>         Y_cil = r * np.sin(Theta_cil)
>         ax1.plot_surface(X_cil, Y_cil, Z_cil, alpha=0.1, color='cyan')
>         
>         ax1.set_xlabel('X')
>         ax1.set_ylabel('Y')
>         ax1.set_zlabel('Z')
>         ax1.set_title('Trayectoria Helicoidal')
>         ax1.set_xlim([-4, 4])
>         ax1.set_ylim([-4, 4])
>         ax1.set_zlim([0, z_final])
>         
>         # Proyección XY
>         circle = plt.Circle((0, 0), r, fill=False, color='cyan', linestyle='--')
>         ax2.add_patch(circle)
>         ax2.plot(x_full[:idx], y_full[:idx], 'b-', alpha=0.5, linewidth=1)
>         ax2.scatter([x_now], [y_now], c='red', s=100, marker='o', zorder=5)
>         ax2.plot([0, x_now], [0, y_now], 'r--', linewidth=1)
>         
>         ax2.set_xlabel('X')
>         ax2.set_ylabel('Y')
>         ax2.set_title(f'Proyección XY\nr={r:.1f}, θ={np.degrees(theta_now):.0f}°, z={z_now:.2f}')
>         ax2.set_xlim([-4, 4])
>         ax2.set_ylim([-4, 4])
>         ax2.set_aspect('equal')
>         ax2.grid(True, alpha=0.3)
>         
>         return ax1, ax2
>     
>     anim = FuncAnimation(fig, update, frames=n_frames, interval=50, repeat=True)
>     plt.tight_layout()
>     
>     return anim
> 
> # Ejecutar animación
> anim = animar_coordenadas_cilindricas()
> plt.show()
> 

## 🧪 Ejercicios Progresivos

> [!example]- 💪 Práctica Graduada
> 
> **Nivel 1 - Conversiones Básicas:** 🟢
> 
> 1. **Cartesianas → Cilíndricas:**
>    - Convertir P(1, √3, 2) a cilíndricas
>    - Respuesta: r = 2, θ = π/3, z = 2
> 
> 2. **Cilíndricas → Cartesianas:**
>    - Convertir Q(4, π/6, -3) a cartesianas
>    - Respuesta: x = 2√3, y = 2, z = -3
> 
> 3. **Cartesianas → Esféricas:**
>    - Convertir R(0, 0, 5) a esféricas
>    - Respuesta: ρ = 5, φ = 0, θ = 0 (sobre eje z)
> 
> 4. **Esféricas → Cartesianas:**
>    - Convertir S(6, π/2, π/4) a cartesianas
>    - Respuesta: x = 3√2, y = 3√2, z = 0
> 
> 5. **Identificación de superficie:**
>    - ¿Qué superficie representa r = 5 en cilíndricas?
>    - Respuesta: Cilindro de radio 5
> 
> 6. **Identificación de superficie:**
>    - ¿Qué superficie representa ρ = 3 en esféricas?
>    - Respuesta: Esfera de radio 3
> 
> **Nivel 2 - Ecuaciones y Conversiones:** 🟡
> 
> 7. **Ecuación cartesiana → cilíndrica:**
>    - Convertir x² + y² = 16 a cilíndricas
>    - Respuesta: r = 4
> 
> 8. **Ecuación cilíndrica → cartesiana:**
>    - Convertir r = 2z a cartesianas
>    - Respuesta: x² + y² = 4z²
> 
> 9. **Ecuación esférica → cartesiana:**
>    - Convertir ρ = 4 cos φ a cartesianas
>    - Solución: ρ² = 4ρ cos φ
>      x² + y² + z² = 4z
>      x² + y² + (z-2)² = 4
>    - Respuesta: Esfera de radio 2 centrada en (0,0,2)
> 
> 10. **Ecuación compleja:**
>     - Convertir z = x² + y² a cilíndricas
>     - Respuesta: z = r²
> 
> 11. **Intersección:**
>     - Encontrar intersección de r = 2 y z = 3 en cilíndricas
>     - Respuesta: Círculo de radio 2 en el plano z = 3
> 
> 12. **Cono en diferentes sistemas:**
>     - Expresar z = √(x² + y²) en cilíndricas y esféricas
>     - Respuestas: z = r (cil.), φ = π/4 (esf.)
> 
> **Nivel 3 - Integrales:** 🔴
> 
> 13. **Volumen de cilindro:**
>     - Calcular volumen de r ≤ 2, 0 ≤ θ ≤ 2π, 0 ≤ z ≤ 5
>     - Respuesta: V = 20π
> 
> 14. **Volumen de hemisferio:**
>     - Calcular volumen de 0 ≤ ρ ≤ R, 0 ≤ φ ≤ π/2, 0 ≤ θ ≤ 2π
>     - Respuesta: V = (2/3)πR³
> 
> 15. **Masa con densidad variable:**
>     - ρ_masa = r, región: 0 ≤ r ≤ 3, 0 ≤ θ ≤ π, 0 ≤ z ≤ 2
>     - Calcular masa total
>     - Respuesta: M = 18π
> 
> 16. **Integral esférica:**
>     - ∫∫∫ ρ² dV sobre esfera de radio 2
>     - Respuesta: 128π/3
> 
> **Nivel 4 - Problemas Aplicados:** 🟣
> 
> 17. **Campo eléctrico:**
>     - Carga Q en origen. Calcular flujo de E a través de esfera de radio R
>     - Respuesta: Φ = Q/ε₀ (Ley de Gauss)
> 
> 18. **Centro de masa:**
>     - Cono sólido: 0 ≤ r ≤ h-z, 0 ≤ z ≤ h, densidad uniforme
>     - Encontrar altura del centro de masa
>     - Respuesta: z_cm = h/4
> 
> 19. **Momento de inercia:**
>     - Cilindro sólido de radio R, altura h, masa M
>     - Calcular I_z (momento alrededor del eje z)
>     - Respuesta: I_z = MR²/2
> 
> 20. **Problema de optimización:**
>     - Cilindro inscrito en esfera de radio R
>     - Encontrar dimensiones para volumen máximo
>     - Respuesta: r = R√(2/3), h = 2R/√3

## 🔬 Operadores Diferenciales

> [!note]- 📐 Gradiente, Divergencia, Rotacional y Laplaciano
> 
> ### En Coordenadas Cilíndricas
> 
> **Gradiente:**
> 
> $$\nabla f = \frac{\partial f}{\partial r}\,\hat{\mathbf{e}}_r + \frac{1}{r}\frac{\partial f}{\partial\theta}\,\hat{\mathbf{e}}_\theta + \frac{\partial f}{\partial z}\,\hat{\mathbf{e}}_z$$
> 
> **Divergencia:**
> 
> Para **F** = F_r **ê**_r + F_θ **ê**_θ + F_z **ê**_z:
> 
> $$\nabla \cdot \mathbf{F} = \frac{1}{r}\frac{\partial(rF_r)}{\partial r} + \frac{1}{r}\frac{\partial F_\theta}{\partial\theta} + \frac{\partial F_z}{\partial z}$$
> 
> **Rotacional:**
> 
> $$\nabla \times \mathbf{F} = \left(\frac{1}{r}\frac{\partial F_z}{\partial\theta} - \frac{\partial F_\theta}{\partial z}\right)\hat{\mathbf{e}}_r$$
> $$+ \left(\frac{\partial F_r}{\partial z} - \frac{\partial F_z}{\partial r}\right)\hat{\mathbf{e}}_\theta$$
> $$+ \frac{1}{r}\left(\frac{\partial(rF_\theta)}{\partial r} - \frac{\partial F_r}{\partial\theta}\right)\hat{\mathbf{e}}_z$$
> 
> **Laplaciano:**
> 
> $$\nabla^2 f = \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial f}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 f}{\partial\theta^2} + \frac{\partial^2 f}{\partial z^2}$$
> 
> ### En Coordenadas Esféricas
> 
> **Gradiente:**
> 
> $$\nabla f = \frac{\partial f}{\partial\rho}\,\hat{\mathbf{e}}_\rho + \frac{1}{\rho}\frac{\partial f}{\partial\phi}\,\hat{\mathbf{e}}_\phi + \frac{1}{\rho\sin\phi}\frac{\partial f}{\partial\theta}\,\hat{\mathbf{e}}_\theta$$
> 
> **Divergencia:**
> 
> $$\nabla \cdot \mathbf{F} = \frac{1}{\rho^2}\frac{\partial(\rho^2 F_\rho)}{\partial\rho} + \frac{1}{\rho\sin\phi}\frac{\partial(\sin\phi \cdot F_\phi)}{\partial\phi} + \frac{1}{\rho\sin\phi}\frac{\partial F_\theta}{\partial\theta}$$
> 
> **Laplaciano:**
> 
> $$\nabla^2 f = \frac{1}{\rho^2}\frac{\partial}{\partial\rho}\left(\rho^2\frac{\partial f}{\partial\rho}\right) + \frac{1}{\rho^2\sin\phi}\frac{\partial}{\partial\phi}\left(\sin\phi\frac{\partial f}{\partial\phi}\right) + \frac{1}{\rho^2\sin^2\phi}\frac{\partial^2 f}{\partial\theta^2}$$
> 
> **Aplicación - Ecuación de Laplace:**
> 
> En esféricas con simetría radial (solo depende de ρ):
> 
> $$\nabla^2 f = \frac{1}{\rho^2}\frac{d}{d\rho}\left(\rho^2\frac{df}{d\rho}\right) = 0$$
> 
> Solución: f(ρ) = A/ρ + B
> 
> (Potencial de carga puntual en electrostática)

## 🎯 Aplicaciones Avanzadas

### 🌌 Física y Electromagnetismo

> [!example]- ⚡ Problemas Físicos Clásicos
> 
> **1. Ecuación de Laplace en cilíndricas:**
> 
> Potencial electrostático en región cilíndrica:
> 
> $$\nabla^2 V = \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial V}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 V}{\partial\theta^2} + \frac{\partial^2 V}{\partial z^2} = 0$$
> 
> Para simetría azimutal (independiente de θ y z):
> 
> $$\frac{1}{r}\frac{d}{dr}\left(r\frac{dV}{dr}\right) = 0$$
> 
> Solución: V(r) = A ln(r) + B
> 
> **2. Ecuación de onda en esféricas:**
> 
> $$\frac{\partial^2 u}{\partial t^2} = c^2\nabla^2 u$$
> 
> Con simetría esférica:
> 
> $$\frac{\partial^2 u}{\partial t^2} = \frac{c^2}{\rho^2}\frac{\partial}{\partial\rho}\left(\rho^2\frac{\partial u}{\partial\rho}\right)$$
> 
> Solución: u(ρ,t) = f(ρ-ct)/ρ + g(ρ+ct)/ρ
> 
> (Ondas esféricas radiando desde origen)
> 
> **3. Ecuación de Schrödinger para átomo de hidrógeno:**
> 
> $$-\frac{\hbar^2}{2m}\nabla^2\psi - \frac{ke^2}{\rho}\psi = E\psi$$
> 
> En esféricas, con separación de variables:
> 
> $$\psi_{nlm}(\rho,\phi,\theta) = R_{nl}(\rho)Y_l^m(\phi,\theta)$$
> 
> Niveles de energía: E_n = -13.6 eV / n²
> 
> **4. Flujo de calor en cilindro:**
> 
> Ecuación de calor: ∂T/∂t = α∇²T
> 
> Para cilindro infinito con simetría radial:
> 
> $$\frac{\partial T}{\partial t} = \frac{\alpha}{r}\frac{\partial}{\partial r}\left(r\frac{\partial T}{\partial r}\right)$$
> 
> Estado estacionario: T(r) = A ln(r) + B
> 
> **5. Campo magnético de solenoide:**
> 
> Solenoide largo con n vueltas/metro, corriente I:
> 
> $$\mathbf{B} = \begin{cases}
> \mu_0 nI\,\hat{\mathbf{e}}_z & r < R \\
> 0 & r > R
> \end{cases}$$
> 
> Campo uniforme dentro, nulo fuera

### 🛰️ Mecánica Orbital

> [!tip]- 🌍 Movimiento de Satélites
> 
> **Ecuación de órbita en coordenadas esféricas:**
> 
> Para movimiento en plano (φ = π/2 constante):
> 
> $$\rho(\theta) = \frac{p}{1 + e\cos\theta}$$
> 
> donde:
> - p = parámetro de la órbita
> - e = excentricidad
> 
> **Tipos de órbitas:**
> - e = 0: circular
> - 0 < e < 1: elíptica
> - e = 1: parabólica
> - e > 1: hiperbólica
> 
> **Energía orbital:**
> 
> $$E = \frac{1}{2}m\dot{\rho}^2 + \frac{L^2}{2m\rho^2} - \frac{GMm}{\rho}$$
> 
> donde L = momento angular (constante)
> 
> **Velocidad en órbita circular:**
> 
> $$v = \sqrt{\frac{GM}{\rho}}$$
> 
> **Período orbital (Tercera Ley de Kepler):**
> 
> $$T^2 = \frac{4\pi^2}{GM}a^3$$
> 
> donde a = semieje mayor

### 🌊 Mecánica de Fluidos

> [!warning]- 💧 Flujo en Coordenadas Curvilíneas
> 
> **1. Flujo de Poiseuille (tubería cilíndrica):**
> 
> Perfil de velocidad en tubería de radio R:
> 
> $$v_z(r) = \frac{\Delta P}{4\mu L}(R^2 - r^2)$$
> 
> donde:
> - ΔP = diferencia de presión
> - μ = viscosidad
> - L = longitud del tubo
> 
> **2. Flujo vorticial (cilíndricas):**
> 
> Vórtice libre:
> 
> $$v_\theta(r) = \frac{\Gamma}{2\pi r}$$
> 
> donde Γ = circulación
> 
> **3. Flujo radial esférico:**
> 
> Fuente/sumidero puntual:
> 
> $$v_\rho(\rho) = \frac{Q}{4\pi\rho^2}$$
> 
> donde Q = caudal volumétrico
> 
> **4. Ecuación de Navier-Stokes en cilíndricas:**
> 
> Componente radial:
> 
> $$\frac{\partial v_r}{\partial t} + v_r\frac{\partial v_r}{\partial r} + \frac{v_\theta}{r}\frac{\partial v_r}{\partial\theta} + v_z\frac{\partial v_r}{\partial z} - \frac{v_\theta^2}{r}$$
> $$= -\frac{1}{\rho}\frac{\partial p}{\partial r} + \nu\left[\nabla^2v_r - \frac{v_r}{r^2} - \frac{2}{r^2}\frac{\partial v_\theta}{\partial\theta}\right]$$

## 📚 Problemas Desafiantes

> [!example]- 🏆 Desafíos Avanzados
> 
> **Desafío 1 - Transformación de integrales:**
> 
> Evaluar ∫∫∫_V e^(-(x²+y²+z²)) dV sobre todo el espacio.
> 
> **Solución:**
> ```
> Usar esféricas es ideal:
> 
> I = ∫₀^∞ ∫₀^π ∫₀^{2π} e^(-ρ²) · ρ²sin φ dθ dφ dρ
> 
> = 2π ∫₀^π sin φ dφ · ∫₀^∞ ρ²e^(-ρ²) dρ
> 
> = 2π · 2 · (√π/4) = π^(3/2)
> ```
> 
> **Desafío 2 - Momento de inercia de cono:**
> 
> Cono sólido: 0 ≤ r ≤ (h-z)tan α, 0 ≤ z ≤ h, densidad ρ₀
> 
> Calcular I_z (momento alrededor del eje z)
> 
> **Pista:** I_z = ∫∫∫ r² ρ₀ · r dr dθ dz
> 
> **Desafío 3 - Campo gravitacional de cáscara esférica:**
> 
> Demostrar que una cáscara esférica uniforme no ejerce fuerza neta sobre una masa en su interior.
> 
> **Enfoque:** Usar simetría esférica y calcular integral del campo gravitacional.
> 
> **Desafío 4 - Coordenadas generalizadas:**
> 
> Para sistema con coordenadas (u, v, w), los factores de escala son:
> 
> $$h_u = \left|\frac{\partial\mathbf{r}}{\partial u}\right|$$
> 
> Verificar que para cilíndricas: h_r = 1, h_θ = r, h_z = 1
> 
> **Desafío 5 - Integral de superficie:**
> 
> Calcular ∫∫_S **F** · d**S** donde **F** = ρ² **ê**_ρ y S es la esfera ρ = R.
> 
> **Respuesta:** 4πR⁴

## 🌐 Conexiones Conceptuales

> [!quote]- 🔗 Enlaces con Otros Temas
> 
> **Prerequisitos:**
> - [[Coordenadas Polares 2D]] - Base para cilíndricas
> - [[Vectores en ℝ³]] - Vectores unitarios y bases
> - [[Trigonometría]] - Funciones circulares
> - [[Cálculo Integral]] - Integrales múltiples
> - [[Cambio de Variable]] - Jacobiano
> 
> **Temas relacionados:**
> - [[Superficies de Revolución]] - Naturales en cilíndricas/esféricas
> - [[Distancias en ℝ³]] - Métricas en diferentes sistemas
> - [[Producto Vectorial]] - Rotacional en curvilíneas
> - [[Integrales Múltiples]] - Aplicaciones de coordenadas
> 
> **Aplicaciones directas:**
> - [[Ecuaciones Diferenciales Parciales]] - Separación de variables
> - [[Mecánica Clásica]] - Lagrangiano en coordenadas generalizadas
> - [[Electromagnetismo]] - Simetrías de campos
> - [[Mecánica Cuántica]] - Átomo de hidrógeno
> - [[Análisis Vectorial]] - Operadores diferenciales
> 
> **Temas avanzados:**
> - [[Geometría Diferencial]] - Variedades y métricas
> - [[Relatividad General]] - Coordenadas curvilíneas en espacio-tiempo
> - [[Teoría de Campos]] - Lagrangianos en diferentes coordenadas
> - [[Elementos Finitos]] - Mallados en coordenadas naturales
> 
> **Aplicaciones interdisciplinarias:**
> - [[Física]] - Problemas con simetría
> - [[Ingeniería]] - Diseño de componentes axisimétricos
> - [[Astronomía]] - Coordenadas celestes
> - [[Geofísica]] - Coordenadas geográficas
> - [[Gráficos por Computadora]] - Mapeo de texturas

## 💡 Consejos de Estudio

> [!tip]- 🧠 Estrategias de Aprendizaje
> 
> **Para elegir el sistema correcto:**
> 
> **Diagrama de decisión:**
> ```
> ¿Hay simetría?
>    ↓
>    ├─ Simetría alrededor de eje → CILÍNDRICAS
>    │   Ejemplos: cables, tuberías, cilindros
>    │
>    ├─ Simetría desde punto central → ESFÉRICAS
>    │   Ejemplos: planetas, átomos, esferas
>    │
>    └─ No hay simetría especial → CARTESIANAS
>        Ejemplos: cajas, cubos, geometría rectangular
> ```
> 
> **Nemotecnia para conversiones:**
> 
> **Cilíndricas (r, θ, z):**
> - "**R**adio en el plano"
> - "**θ** ángulo como en polares"
> - "**z** se queda igual"
> - Fórmula clave: x² + y² = r²
> 
> **Esféricas (ρ, φ, θ):**
> - "**ρ** (rho) = **R**adio total desde origen"
> - "**φ** (phi) = ángulo **F**rom arriba (desde eje z)"
> - "**θ** (theta) = mismo que cilíndricas"
> - Fórmula clave: x² + y² + z² = ρ²
> 
> **Para recordar Jacobianos:**
> - Cilíndricas: dV = **r** dr dθ dz (un "r")
> - Esféricas: dV = **ρ² sin φ** dρ dφ dθ (dos "ρ" y un "sin")
> 
> **Errores comunes a evitar:**
> 
> 1. ❌ Olvidar el jacobiano en integrales
>    - ✓ Cilíndricas: SIEMPRE incluir factor r
>    - ✓ Esféricas: SIEMPRE incluir ρ² sin φ
> 
> 2. ❌ Confundir convenciones (φ y θ intercambiados)
>    - ✓ Verificar qué convención usa el libro/problema
> 
> 3. ❌ Límites de integración incorrectos
>    - ✓ θ: 0 a 2π (vuelta completa)
>    - ✓ φ: 0 a π (de polo a polo)
> 
> 4. ❌ No ajustar cuadrante en arctan
>    - ✓ Usar arctan2(y, x) en programación
>    - ✓ Verificar signos de x e y manualmente
> 
> 5. ❌ Olvidar que vectores unitarios varían con posición
>    - ✓ ∂**ê**_r/∂θ ≠ 0 (en cilíndricas y esféricas)
> 
> **Práctica recomendada:**
> 
> 6. **Visualizar primero:** Dibujar el problema en 3D
> 7. **Identificar simetría:** ¿Qué coordenadas simplifican?
> 8. **Convertir ecuaciones:** Llevar todo al sistema elegido
> 9. **Plantear límites:** Cuidado con el orden de integración
> 10. **Verificar dimensiones:** El resultado debe tener unidades correctas
> 11. **Casos límite:** Verificar resultados conocidos (esfera, cilindro, etc.)

## 📊 Tabla de Referencia Rápida

> [!abstract]- 📋 Fórmulas Esenciales
> 
> ### Conversiones Directas
> 
> |De/A|Cilíndricas (r, θ, z)|Esféricas (ρ, φ, θ)|
> |---|---|---|
> |**Cartesianas (x, y, z)**|x = r cos θ<br>y = r sin θ<br>z = z|x = ρ sin φ cos θ<br>y = ρ sin φ sin θ<br>z = ρ cos φ|
> |**Inversas**|r = √(x²+y²)<br>θ = arctan2(y, x)<br>z = z|ρ = √(x²+y²+z²)<br>φ = arccos(z/ρ)<br>θ = arctan2(y, x)|
> 
> ### Elementos Diferenciales
> 
> |Sistema|Longitud|Área|Volumen|
> |---|---|---|---|
> |**Cartesiano**|ds² = dx² + dy² + dz²|dA = dx dy|dV = dx dy dz|
> |**Cilíndrico**|ds² = dr² + r²dθ² + dz²|dA = r dr dθ|dV = r dr dθ dz|
> |**Esférico**|ds² = dρ² + ρ²dφ² + ρ²sin²φ dθ²|dA = ρ² sin φ dφ dθ|dV = ρ² sin φ dρ dφ dθ|
> 
> ### Rangos Típicos
> 
> |Coordenada|Rango Estándar|Notas|
> |---|---|---|
> |r|[0, ∞)|Radio cilíndrico|
> |θ (cil/esf)|[0, 2π) o [-π, π]|Ángulo azimutal|
> |z|(-∞, ∞)|Altura|
> |ρ|[0, ∞)|Radio esférico|
> |φ|[0, π]|Ángulo polar/colatitud|
> 
> ### Operadores (Cilíndricas)
> 
> |Operador|Fórmula|
> |---|---|
> |**Gradiente**|∇f = (∂f/∂r)**ê**_r + (1/r)(∂f/∂θ)**ê**_θ + (∂f/∂z)**ê**_z|
> |**Divergencia**|∇·**F** = (1/r)∂(rF_r)/∂r + (1/r)∂F_θ/∂θ + ∂F_z/∂z|
> |**Laplaciano**|∇²f = (1/r)∂/∂r(r∂f/∂r) + (1/r²)∂²f/∂θ² + ∂²f/∂z²|
> 
> ### Operadores (Esféricas)
> 
> |Operador|Fórmula|
> |---|---|
> |**Gradiente**|∇f = (∂f/∂ρ)**ê**_ρ + (1/ρ)(∂f/∂φ)**ê**_φ + (1/ρsinφ)(∂f/∂θ)**ê**_θ|
> |**Divergencia**|∇·**F** = (1/ρ²)∂(ρ²F_ρ)/∂ρ + (1/ρsinφ)∂(sinφF_φ)/∂φ + (1/ρsinφ)∂F_θ/∂θ|
> |**Laplaciano**|∇²f = (1/ρ²)∂/∂ρ(ρ²∂f/∂ρ) + (1/ρ²sinφ)∂/∂φ(sinφ∂f/∂φ) + (1/ρ²sin²φ)∂²f/∂θ²|

## 🎓 Aplicaciones en Ingeniería

> [!example]- 🔧 Casos de Ingeniería Práctica
> 
> **1. Diseño de Antenas**
> 
> ```python
> def patron_radiacion_dipolo(phi, theta, I0=1.0):
>     """
>     Patrón de radiación de antena dipolo
>     
>     Intensidad: I(φ,θ) = I₀ sin²φ
>     """
>     return I0 * np.sin(phi)**2
> 
> # Calcular potencia total radiada
> def potencia_radiada(I0, a=1.0):
>     """
>     P_total = ∫∫ I(φ,θ) · ρ² sin φ dφ dθ
>     sobre esfera de radio a
>     """
>     def integrando(phi, theta):
>         return patron_radiacion_dipolo(phi, theta, I0) * np.sin(phi)
>     
>     P = integral_triple_esferica(
>         lambda rho, phi, theta: integrando(phi, theta) if rho == a else 0,
>         (a, a), (0, np.pi), (0, 2*np.pi),
>         n=50
>     )
>     
>     return P * a**2  # Factor de área
> 
> # Visualizar patrón 3D
> phi_vals = np.linspace(0, np.pi, 50)
> theta_vals = np.linspace(0, 2*np.pi, 50)
> Phi, Theta = np.meshgrid(phi_vals, theta_vals)
> 
> # Intensidad normalizada como radio
> Rho = patron_radiacion_dipolo(Phi, Theta)
> 
> # Convertir a cartesianas
> X = Rho * np.sin(Phi) * np.cos(Theta)
> Y = Rho * np.sin(Phi) * np.sin(Theta)
> Z = Rho * np.cos(Phi)
> 
> fig = plt.figure(figsize=(10, 8))
> ax = fig.add_subplot(111, projection='3d')
> surf = ax.plot_surface(X, Y, Z, cmap='hot', alpha=0.8)
> ax.set_title('Patrón de Radiación de Dipolo')
> plt.show()
> ```
> 
> **2. Análisis de Tensiones en Cilindro Presurizado**
> 
> Cilindro de pared delgada bajo presión interna p:
> 
> ```python
> def tensiones_cilindro(r, p_int, R_int, espesor, E, nu):
>     """
>     Tensiones en cilindro presurizado
>     
>     Parámetros:
>     -----------
>     r : float
>         Radio donde calcular (R_int ≤ r ≤ R_int + espesor)
>     p_int : float
>         Presión interna
>     R_int : float
>         Radio interno
>     espesor : float
>         Espesor de pared
>     E : float
>         Módulo de Young
>     nu : float
>         Coeficiente de Poisson
>     
>     Retorna:
>     --------
>     sigma_r, sigma_theta, sigma_z : float
>         Tensiones radial, tangencial y axial
>     """
>     R_ext = R_int + espesor
>     
>     # Fórmulas de Lamé
>     A = p_int * R_int**2 / (R_ext**2 - R_int**2)
>     B = -p_int * R_int**2 * R_ext**2 / (R_ext**2 - R_int**2)
>     
>     sigma_r = A - B/r**2
>     sigma_theta = A + B/r**2
>     
>     # Tensión axial (extremos cerrados)
>     sigma_z = p_int * R_int**2 / (R_ext**2 - R_int**2)
>     
>     return sigma_r, sigma_theta, sigma_z
> 
> # Ejemplo: cilindro con presión de 10 MPa
> R_int = 0.1  # m
> espesor = 0.01  # m
> p = 10e6  # Pa
> 
> # Graficar distribución de tensiones
> r_vals = np.linspace(R_int, R_int + espesor, 100)
> sigma_r_vals = []
> sigma_theta_vals = []
> 
> for r in r_vals:
>     sr, st, sz = tensiones_cilindro(r, p, R_int, espesor, 200e9, 0.3)
>     sigma_r_vals.append(sr/1e6)  # Convertir a MPa
>     sigma_theta_vals.append(st/1e6)
> 
> plt.figure(figsize=(10, 6))
> plt.plot(r_vals*1000, sigma_r_vals, label='σᵣ (Radial)')
> plt.plot(r_vals*1000, sigma_theta_vals, label='σ_θ (Tangencial)')
> plt.xlabel('Radio (mm)')
> plt.ylabel('Tensión (MPa)')
> plt.title('Distribución de Tensiones en Cilindro Presurizado')
> plt.legend()
> plt.grid(True, alpha=0.3)
> plt.show()
> ```
> 
> **3. Transferencia de Calor en Esfera**
> 
> ```python
> def conduccion_calor_esfera(r, R_int, R_ext, T_int, T_ext, k):
>     """
>     Temperatura en cáscara esférica con conducción radial
>     
>     Solución de estado estacionario: ∇²T = 0
>     Con simetría esférica: d/dr(r² dT/dr) = 0
>     
>     Solución: T(r) = A/r + B
>     """
>     # Condiciones de frontera
>     A = (T_int - T_ext) * R_int * R_ext / (R_ext - R_int)
>     B = (T_ext * R_ext - T_int * R_int) / (R_ext - R_int)
>     
>     T = A/r + B
>     
>     return T
> 
> def flujo_calor_esfera(r, R_int, R_ext, T_int, T_ext, k):
>     """
>     Flujo de calor: q = -k dT/dr
>     """
>     A = (T_int - T_ext) * R_int * R_ext / (R_ext - R_int)
>     dT_dr = -A / r**2
>     q = -k * dT_dr
>     
>     return q
> 
> # Ejemplo: aislamiento esférico
> R_int = 0.05  # m (radio interno)
> R_ext = 0.10  # m (radio externo)
> T_int = 100   # °C (temperatura interna)
> T_ext = 20    # °C (temperatura externa)
> k = 0.05      # W/(m·K) (conductividad térmica)
> 
> r_vals = np.linspace(R_int, R_ext, 100)
> T_vals = [conduccion_calor_esfera(r, R_int, R_ext, T_int, T_ext, k) 
>           for r in r_vals]
> q_vals = [flujo_calor_esfera(r, R_int, R_ext, T_int, T_ext, k)
>           for r in r_vals]
> 
> fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
> 
> ax1.plot(r_vals*100, T_vals)
> ax1.set_xlabel('Radio (cm)')
> ax1.set_ylabel('Temperatura (°C)')
> ax1.set_title('Distribución de Temperatura')
> ax1.grid(True, alpha=0.3)
> 
> ax2.plot(r_vals*100, q_vals)
> ax2.set_xlabel('Radio (cm)')
> ax2.set_ylabel('Flujo de Calor (W/m²)')
> ax2.set_title('Flujo de Calor Radial')
> ax2.grid(True, alpha=0.3)
> 
> plt.tight_layout()
> plt.show()
> 
> # Resistencia térmica total
> R_thermal = (R_ext - R_int) / (4 * np.pi * k * R_int * R_ext)
> print(f"Resistencia térmica: {R_thermal:.4f} K/W")
> ```
> 
> **4. Análisis de Vibraciones en Membrana Circular**
> 
> ```python
> def modos_membrana_circular(r, theta, n, m, R, c):
>     """
>     Modos normales de vibración de membrana circular
>     
>     Solución de ecuación de onda:
>     u(r,θ,t) = J_n(k_nm·r) [A·cos(nθ) + B·sin(nθ)] cos(ω_nm·t)
>     
>     Parámetros:
>     -----------
>     n : int
>         Número de nodos angulares
>     m : int
>         Número de nodos radiales
>     R : float
>         Radio de la membrana
>     c : float
>         Velocidad de onda
>     """
>     from scipy.special import jn, jn_zeros
>     
>     # Ceros de función de Bessel
>     k_nm = jn_zeros(n, m)[-1] / R
>     omega_nm = c * k_nm
>     
>     # Forma del modo
>     u = jn(n, k_nm * r) * np.cos(n * theta)
>     
>     return u, omega_nm
> 
> # Visualizar primeros modos
> R = 1.0
> c = 1.0
> r = np.linspace(0, R, 100)
> theta = np.linspace(0, 2*np.pi, 100)
> R_grid, Theta_grid = np.meshgrid(r, theta)
> 
> fig, axes = plt.subplots(2, 3, figsize=(15, 10), subplot_kw={'projection': '3d'})
> axes = axes.flatten()
> 
> modos = [(0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]
> 
> for idx, (n, m) in enumerate(modos):
>     U, omega = modos_membrana_circular(R_grid, Theta_grid, n, m, R, c)
>     
>     # Convertir a cartesianas para graficar
>     X = R_grid * np.cos(Theta_grid)
>     Y = R_grid * np.sin(Theta_grid)
>     
>     ax = axes[idx]
>     surf = ax.plot_surface(X, Y, U, cmap='seismic', alpha=0.8)
>     ax.set_title(f'Modo ({n},{m})\nω = {omega:.2f} rad/s')
>     ax.set_zlim([-1.5, 1.5])
> 
> plt.tight_layout()
> plt.show()
> ```

## 🌟 Sistemas de Coordenadas Generalizados

> [!info]- 🔵 Extensión a Coordenadas Arbitrarias
> 
> **Coordenadas curvilíneas generales (u₁, u₂, u₃):**
> 
> Para transformación **r** = **r**(u₁, u₂, u₃):
> 
> **Vectores base covariantes:**
> 
> $$\mathbf{g}_i = \frac{\partial\mathbf{r}}{\partial u_i}$$
> 
> **Factores de escala:**
> 
> $$h_i = |\mathbf{g}_i| = \left|\frac{\partial\mathbf{r}}{\partial u_i}\right|$$
> 
> **Vectores unitarios:**
> 
> $$\hat{\mathbf{e}}_i = \frac{\mathbf{g}_i}{h_i}$$
> 
> **Tensor métrico:**
> 
> $$g_{ij} = \mathbf{g}_i \cdot \mathbf{g}_j$$
> 
> **Jacobiano:**
> 
> $$J = \det\left(\frac{\partial(x,y,z)}{\partial(u_1,u_2,u_3)}\right) = h_1 h_2 h_3$$
> 
> (para sistemas ortogonales)
> 
> **Elemento de volumen:**
> 
> $$dV = J,du_1,du_2,du_3 = h_1 h_2 h_3,du_1,du_2,du_3$$
> 
> **Ejemplos:**
> 
> |Sistema|h₁|h₂|h₃|J|
> |---|---|---|---|---|
> |Cartesiano|1|1|1|1|
> |Cilíndrico|1|r|1|r|
> |Esférico|1|ρ|ρ sin φ|ρ² sin φ|
> |Elíptico|√(a²sinh²μ + b²sin²ν)|...|...|...|

## 🎬 Animaciones y Visualizaciones Dinámicas

> [!tip]- 🎥 Crear Visualizaciones Interactivas
> 
> ```python
> def animar_transformacion_coordenadas():
>     """
>     Anima la transformación entre sistemas de coordenadas
>     """
>     from matplotlib.animation import FuncAnimation
>     
>     fig = plt.figure(figsize=(15, 5))
>     
>     # Tres subplots: Cartesianas, Cilíndricas, Esféricas
>     ax1 = fig.add_subplot(131, projection='3d')
>     ax2 = fig.add_subplot(132, projection='3d')
>     ax3 = fig.add_subplot(133, projection='3d')
>     
>     # Punto que se mueve en hélice
>     t_vals = np.linspace(0, 4*np.pi, 200)
>     
>     def trayectoria_cart(t):
>         x = 2 * np.cos(t)
>         y = 2 * np.sin(t)
>         z = t
>         return x, y, z
>     
>     def update(frame):
>         for ax in [ax1, ax2, ax3]:
>             ax.clear()
>         
>         # Calcular posición actual
>         t = t_vals[frame]
>         x, y, z = trayectoria_cart(t)
>         
>         # Convertir a otros sistemas
>         r, theta, z_cil = CoordenadasCurvilineas.cart_a_cil(x, y, z)
>         rho, phi, theta_esf = CoordenadasCurvilineas.cart_a_esf(x, y, z)
>         
>         # Trayectoria hasta ahora
>         x_traj, y_traj, z_traj = trayectoria_cart(t_vals[:frame])
>         
>         # Plot 1: Cartesianas
>         ax1.plot(x_traj, y_traj, z_traj, 'b-', alpha=0.5, linewidth=1)
>         ax1.scatter([x], [y], [z], c='red', s=100, marker='o')
>         ax1.set_xlabel('X')
>         ax1.set_ylabel('Y')
>         ax1.set_zlabel('Z')
>         ax1.set_title(f'Cartesianas\n({x:.2f}, {y:.2f}, {z:.2f})')
>         ax1.set_xlim([-3, 3])
>         ax1.set_ylim([-3, 3])
>         ax1.set_zlim([0, 13])
>         
>         # Plot 2: Cilíndricas (visualización)
>         ax2.plot(x_traj, y_traj, z_traj, 'g-', alpha=0.5, linewidth=1)
>         ax2.scatter([x], [y], [z], c='red', s=100, marker='o')
>         
>         # Dibujar línea radial
>         ax2.plot([0, x], [0, y], [z, z], 'r--', linewidth=1)
>         
>         # Círculo en plano xy
>         theta_circle = np.linspace(0, theta, 50)
>         x_circle = r * np.cos(theta_circle)
>         y_circle = r * np.sin(theta_circle)
>         z_circle = np.full_like(x_circle, z)
>         ax2.plot(x_circle, y_circle, z_circle, 'orange', linewidth=2)
>         
>         ax2.set_xlabel('X')
>         ax2.set_ylabel('Y')
>         ax2.set_zlabel('Z')
>         ax2.set_title(f'Cilíndricas\n(r={r:.2f}, θ={np.degrees(theta):.0f}°, z={z:.2f})')
>         ax2.set_xlim([-3, 3])
>         ax2.set_ylim([-3, 3])
>         ax2.set_zlim([0, 13])
>         
>         # Plot 3: Esféricas (visualización)
>         ax3.plot(x_traj, y_traj, z_traj, 'm-', alpha=0.5, linewidth=1)
>         ax3.scatter([x], [y], [z], c='red', s=100, marker='o')
>         
>         # Línea radial desde origen
>         ax3.plot([0, x], [0, y], [0, z], 'r--', linewidth=2)
>         
>         # Arco para ángulo phi
>         phi_arc = np.linspace(0, phi, 30)
>         x_arc = rho * np.sin(phi_arc) * np.cos(theta_esf)
>         y_arc = rho * np.sin(phi_arc) * np.sin(theta_esf)
>         z_arc = rho * np.cos(phi_arc)
>         ax3.plot(x_arc, y_arc, z_arc, 'cyan', linewidth=2)
>         
>         ax3.set_xlabel('X')
>         ax3.set_ylabel('Y')
>         ax3.set_zlabel('Z')
>         ax3.set_title(f'Esféricas\n(ρ={rho:.2f}, φ={np.degrees(phi):.0f}°, θ={np.degrees(theta_esf):.0f}°)')
>         ax3.set_xlim([-3, 3])
>         ax3.set_ylim([-3, 3])
>         ax3.set_zlim([0, 13])
>         
>         return ax1, ax2, ax3
>     
>     anim = FuncAnimation(fig, update, frames=len(t_vals), 
>                         interval=50, repeat=True, blit=False)
>     
>     plt.tight_layout()
>     return anim
> 
> # Ejecutar
> anim = animar_transformacion_coordenadas()
> plt.show()
> ```

## 📝 Resumen Final

> [!abstract]- 🎓 Puntos Clave para Recordar
> 
> ### Conceptos Fundamentales
> 
> **1. Sistemas de Coordenadas:**
> 
> - **Cartesianas (x, y, z):** Rectangular, sin simetría especial
> - **Cilíndricas (r, θ, z):** Simetría alrededor de eje z
> - **Esféricas (ρ, φ, θ):** Simetría radial desde origen
> 
> **2. Cuándo Usar Cada Sistema:**
> 
> - Cilíndricas: cables, tuberías, cilindros, rotación alrededor de eje
> - Esféricas: planetas, átomos, esferas, problemas radiales
> - Cartesianas: cuando no hay simetría especial
> 
> **3. Conversiones Clave:**
> 
> ```
> Cilíndricas:
>   x = r cos θ,  y = r sin θ,  z = z
>   r = √(x²+y²),  θ = arctan2(y,x)
> 
> Esféricas:
>   x = ρ sin φ cos θ,  y = ρ sin φ sin θ,  z = ρ cos φ
>   ρ = √(x²+y²+z²),  φ = arccos(z/ρ),  θ = arctan2(y,x)
> ```
> 
> **4. Jacobianos (CRÍTICO para integrales):**
> 
> - Cilíndricas: dV = **r** dr dθ dz
> - Esféricas: dV = **ρ² sin φ** dρ dφ dθ
> 
> **5. Rangos de Coordenadas:**
> 
> - r ≥ 0, ρ ≥ 0
> - 0 ≤ θ < 2π (o -π < θ ≤ π)
> - 0 ≤ φ ≤ π
> - -∞ < z < ∞
> 
> **6. Aplicaciones Principales:**
> 
> - **Física:** Electromagnetismo, mecánica cuántica, gravitación
> - **Ingeniería:** Transferencia de calor, mecánica de fluidos, tensiones
> - **Matemáticas:** Integrales múltiples, EDPs con simetría
> 
> ### Errores Comunes a Evitar
> 
> ❌ **NO** olvides el jacobiano ❌ **NO** confundas φ y θ entre convenciones ❌ **NO** uses arctan, usa arctan2 ❌ **NO** olvides que vectores unitarios varían con posición ❌ **NO** uses límites de integración incorrectos
> 
> ### Estrategia de Resolución
> 
> 1. Identificar simetría del problema
> 2. Elegir sistema de coordenadas apropiado
> 3. Convertir todas las ecuaciones al nuevo sistema
> 4. Establecer límites de integración correctos
> 5. **Incluir jacobiano** en integrales
> 6. Verificar resultado con casos conocidos

---

**Tags:** #coordenadas-curvilíneas #cilíndricas #esféricas #transformaciones #jacobiano #integrales-múltiples #simetría #análisis-vectorial #física #ingeniería #operadores-diferenciales #university #mathematics #R3

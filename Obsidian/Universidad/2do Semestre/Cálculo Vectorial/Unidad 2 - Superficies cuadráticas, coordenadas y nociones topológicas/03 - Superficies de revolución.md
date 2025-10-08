# 🌀 Superficies de Revolución

## 🎯 Fundamentos de las Superficies de Revolución

> [!info]- 💡 Introducción a las Superficies Generadas por Rotación Las **superficies de revolución** son superficies tridimensionales generadas al rotar una curva plana (llamada **generatriz**) alrededor de un eje fijo (llamado **eje de revolución**). Estas superficies poseen simetría rotacional y son fundamentales en geometría, física, ingeniería y diseño industrial.
> 
> **Analogías útiles:**
> 
> - **Alfarería:** Un jarrón creado en un torno giratorio
> - **Ingeniería:** Diseño de tubos, tanques cilíndricos, cúpulas
> - **Astronomía:** Forma de planetas y estrellas en rotación
> - **Arquitectura:** Domos, torres, columnas
> 
> **Importancia histórica:**
> 
> - **Arquímedes (287-212 a.C.):** Estudió el paraboloide de revolución
> - **Apolonio (262-190 a.C.):** Análisis de cónicas y sus revoluciones
> - **Galileo (1638):** Catenaria y formas de resistencia óptima
> - **Euler (1744):** Cálculo variacional y superficies mínimas

### 📊 Características Fundamentales

> [!note]- 🌟 Propiedades Esenciales
> 
> **Elementos de una superficie de revolución:**
> 
> |Elemento|Definición|Notación|
> |---|---|---|
> |**Generatriz**|Curva que se rota|C(t) o y = f(x)|
> |**Eje de revolución**|Línea fija de rotación|Usualmente eje z o x|
> |**Meridianos**|Curvas obtenidas por cortes con planos que contienen el eje|Copias de la generatriz|
> |**Paralelos**|Círculos perpendiculares al eje|Circunferencias horizontales|
> |**Perfil**|Forma de la generatriz|Determina la superficie|
> 
> **Propiedades geométricas:**
> 
> - **Simetría rotacional:** Invariante bajo rotaciones alrededor del eje
> - **Simetría de reflexión:** Simétrica respecto a planos que contienen el eje
> - **Meridianos idénticos:** Todos los cortes meridionales son congruentes
> - **Paralelos circulares:** Cualquier corte perpendicular al eje es un círculo

## 🔄 Generación por Rotación

### 📐 Método de Generación

> [!success]- 🟢 Proceso de Construcción
> 
> **Definición formal:** Una superficie de revolución S se obtiene rotando una curva C alrededor de un eje L. Si un punto P(x₀, y₀) de la curva está a distancia r del eje, al rotar describe un círculo de radio r.
> 
> **Pasos para generar una superficie:**
> 
> 1. **Definir la generatriz:** Curva C en un plano (usualmente xz o yz)
> 2. **Seleccionar el eje:** Línea fija L (comúnmente eje z)
> 3. **Calcular distancia al eje:** Para cada punto de C, r = distancia a L
> 4. **Rotar:** Cada punto describe un círculo de radio r
> 5. **Parametrizar:** Usar coordenadas cilíndricas o esféricas
> 
> **Visualización del proceso:**
> 
> ```
> Curva inicial → Eje de rotación → Rotación completa → Superficie
>      |                |                  |                |
>   y=f(x)           eje z            θ: 0→2π         S(x,θ)
> ```

### 🧮 Ecuaciones Paramétricas

> [!example]- 📘 Formulación Matemática
> 
> **Caso 1: Rotación alrededor del eje z**
> 
> Si la generatriz es C: x = f(t), z = g(t) en el plano xz, la superficie de revolución es:
> 
> $$\begin{cases} x(t, \theta) = f(t)\cos\theta \ y(t, \theta) = f(t)\sin\theta \ z(t, \theta) = g(t) \end{cases}$$
> 
> donde:
> 
> - t: parámetro de la curva generatriz
> - θ: ángulo de rotación (0 ≤ θ ≤ 2π)
> - f(t): distancia del punto al eje z
> - g(t): altura del punto
> 
> **Caso 2: Rotación alrededor del eje x**
> 
> Si la generatriz es C: y = f(x), la superficie es:
> 
> $$\begin{cases} x(u, \theta) = u \ y(u, \theta) = f(u)\cos\theta \ z(u, \theta) = f(u)\sin\theta \end{cases}$$
> 
> **Caso 3: Forma implícita**
> 
> Para rotación alrededor del eje z, si la generatriz satisface F(x, z) = 0:
> 
> $$F(\sqrt{x^2 + y^2}, z) = 0$$
> 
> Esta ecuación representa la superficie completa.

### 🔧 Coordenadas Cilíndricas

> [!tip]- 🎯 Sistema Natural para Superficies de Revolución
> 
> **Coordenadas cilíndricas (r, θ, z):**
> 
> $$\begin{cases} x = r\cos\theta \ y = r\sin\theta \ z = z \end{cases}$$
> 
> **Para superficie de revolución:**
> 
> - r = f(z): radio en función de la altura
> - θ: ángulo libre (0 ≤ θ ≤ 2π)
> - z: coordenada vertical
> 
> **Ventajas:**
> 
> - Ecuaciones más simples
> - Simetría explícita
> - Fácil visualización
> 
> **Ejemplo - Cono:**
> 
> - Generatriz: r = az (línea recta)
> - Superficie: x² + y² = a²z²
> - Parametrización: (az cos θ, az sin θ, z)

## 🎨 Ejemplos Clásicos

### 🔵 Esfera

> [!example]- ⚪ La Superficie Más Simétrica
> 
> **Generatriz:** Semicírculo en el plano xz
> 
> $$x = R\cos t, \quad z = R\sin t \quad (0 \leq t \leq \pi)$$
> 
> **Ecuación paramétrica (rotación alrededor de z):**
> 
> $$\begin{cases} x(\phi, \theta) = R\sin\phi\cos\theta \ y(\phi, \theta) = R\sin\phi\sin\theta \ z(\phi, \theta) = R\cos\phi \end{cases}$$
> 
> donde:
> 
> - φ: ángulo polar (0 ≤ φ ≤ π)
> - θ: ángulo azimutal (0 ≤ θ ≤ 2π)
> - R: radio de la esfera
> 
> **Ecuación implícita:**
> 
> $$x^2 + y^2 + z^2 = R^2$$
> 
> **Propiedades:**
> 
> - Curvatura gaussiana constante: K = 1/R²
> - Área superficial: A = 4πR²
> - Volumen encerrado: V = (4/3)πR³
> - Máxima simetría posible
> 
> **Aplicaciones:**
> 
> - Balones deportivos
> - Planetas y estrellas
> - Burbujas de jabón
> - Tanques esféricos a presión

### 🔴 Cilindro Circular

> [!example]- 📏 Superficie de Revolución Más Simple
> 
> **Generatriz:** Línea recta paralela al eje z
> 
> $$x = R, \quad z = t \quad (-h \leq t \leq h)$$
> 
> **Ecuación paramétrica:**
> 
> $$\begin{cases} x(t, \theta) = R\cos\theta \ y(t, \theta) = R\sin\theta \ z(t, \theta) = t \end{cases}$$
> 
> **Ecuación implícita:**
> 
> $$x^2 + y^2 = R^2$$
> 
> **Propiedades:**
> 
> - Curvatura gaussiana: K = 0 (superficie desarrollable)
> - Área lateral: A = 2πRh
> - Volumen: V = πR²h
> - Se puede "desenrollar" en un rectángulo
> 
> **Variantes:**
> 
> - **Cilindro elíptico:** x²/a² + y²/b² = 1
> - **Cilindro parabólico:** y = x²
> 
> **Aplicaciones:**
> 
> - Tuberías
> - Columnas arquitectónicas
> - Latas y envases
> - Pozos y chimeneas

### 🟠 Cono Circular

> [!example]- 🔺 Superficie Cónica Clásica
> 
> **Generatriz:** Línea recta que pasa por el origen
> 
> $$x = at, \quad z = t \quad (0 \leq t \leq h)$$
> 
> **Ecuación paramétrica:**
> 
> $$\begin{cases} x(t, \theta) = at\cos\theta \ y(t, \theta) = at\sin\theta \ z(t, \theta) = t \end{cases}$$
> 
> donde a = R/h (relación radio/altura)
> 
> **Ecuación implícita:**
> 
> $$x^2 + y^2 = a^2z^2$$
> 
> o en forma estándar:
> 
> $$z^2 = \frac{x^2 + y^2}{a^2}$$
> 
> **Propiedades:**
> 
> - Curvatura gaussiana: K = 0 (desarrollable)
> - Área lateral: A = πR√(R² + h²) = πRℓ (ℓ = generatriz)
> - Volumen: V = (1/3)πR²h
> - Ángulo del vértice: α = 2 arctan(R/h)
> 
> **Tipos especiales:**
> 
> - **Cono recto:** Vértice sobre el centro de la base
> - **Cono oblicuo:** Vértice descentrado
> - **Cono doble:** Extensión hacia z negativo
> 
> **Aplicaciones:**
> 
> - Embudos y conos de tráfico
> - Altavoces y megáfonos
> - Volcanes (aproximación geológica)
> - Punta de cohetes

### 🟡 Paraboloide de Revolución

> [!example]- 📡 Superficie Parabólica
> 
> **Generatriz:** Parábola en el plano xz
> 
> $$x = \sqrt{2pz}, \quad z = t \quad (z \geq 0)$$
> 
> o equivalentemente: z = x²/(2p)
> 
> **Ecuación paramétrica:**
> 
> $$\begin{cases} x(z, \theta) = \sqrt{2pz}\cos\theta \ y(z, \theta) = \sqrt{2pz}\sin\theta \ z(z, \theta) = z \end{cases}$$
> 
> **Ecuación implícita:**
> 
> $$z = \frac{x^2 + y^2}{2p}$$
> 
> donde p es el parámetro focal de la parábola.
> 
> **Propiedades especiales:**
> 
> - **Propiedad focal:** Rayos paralelos al eje reflejan hacia el foco
> - Foco: F(0, 0, p/2)
> - Curvatura gaussiana: K = 1/(p²(1 + r²/p²)²)
> - Curvatura media: H = (2 + 3r²/p²)/(2p(1 + r²/p²)^(3/2))
> 
> **Aplicaciones:**
> 
> - Antenas parabólicas (reflexión de señales)
> - Telescopios reflectores
> - Faros de automóviles
> - Hornos solares
> - Puentes colgantes (forma de cables)
> 
> **Ejemplo numérico:** Para p = 2:
> 
> - z = (x² + y²)/4
> - En z = 4: círculo de radio 4
> - Foco: F(0, 0, 1)

### 🟢 Elipsoide de Revolución

> [!example]- 🏈 Superficies Elípticas
> 
> **Tipo A: Elipsoide prolado (alargado)**
> 
> **Generatriz:** Elipse con eje mayor vertical
> 
> $$x = b\cos t, \quad z = a\sin t \quad (a > b)$$
> 
> **Ecuación implícita:**
> 
> $$\frac{x^2 + y^2}{b^2} + \frac{z^2}{a^2} = 1$$
> 
> **Tipo B: Elipsoide oblato (achatado)**
> 
> **Generatriz:** Elipse con eje mayor horizontal
> 
> $$x = a\cos t, \quad z = b\sin t \quad (a > b)$$
> 
> **Ecuación implícita:**
> 
> $$\frac{x^2 + y^2}{a^2} + \frac{z^2}{b^2} = 1$$
> 
> **Propiedades:**
> 
> - Excentricidad: e = √(1 - b²/a²) (prolado) o e = √(1 - a²/b²) (oblato)
> - Área superficial: Fórmula compleja con integrales elípticas
> - Volumen: V = (4/3)πa²b (prolado) o V = (4/3)πab² (oblato)
> 
> **Aplicaciones:**
> 
> - **Prolado:** Balones de rugby, huevos
> - **Oblato:** Tierra (achatada en los polos), Saturno
> - **Astronomía:** Forma de planetas en rotación
> - **Biología:** Forma de células

### 🔵 Hiperboloide de Revolución

> [!example]- ⌛ Superficies Hiperbólicas
> 
> **Tipo A: Hiperboloide de una hoja**
> 
> **Generatriz:** Hipérbola que NO cruza el eje
> 
> $$x = a\cosh t, \quad z = b\sinh t$$
> 
> o en forma más simple: x = a√(1 + z²/b²)
> 
> **Ecuación implícita:**
> 
> $$\frac{x^2 + y^2}{a^2} - \frac{z^2}{b^2} = 1$$
> 
> **Propiedades:**
> 
> - Radio mínimo: r = a (en z = 0)
> - Asíntotas: x² + y² = (a/b)²z²
> - Superficie reglada (contiene líneas rectas)
> - Curvatura gaussiana negativa: K < 0
> 
> **Tipo B: Hiperboloide de dos hojas**
> 
> **Generatriz:** Hipérbola que SÍ cruza el eje
> 
> **Ecuación implícita:**
> 
> $$\frac{z^2}{c^2} - \frac{x^2 + y^2}{a^2} = 1$$
> 
> (para |z| ≥ c)
> 
> **Propiedades:**
> 
> - Dos componentes separadas: z ≥ c y z ≤ -c
> - Radio mínimo: r = 0 (en z = ±c)
> - No es reglada
> 
> **Aplicaciones:**
> 
> - **Una hoja:** Torres de enfriamiento de plantas nucleares
> - **Una hoja:** Estructuras arquitectónicas (Torre Kobe Port)
> - **Dos hojas:** Trayectorias de partículas en física
> - **Ingeniería:** Piezas mecánicas con resistencia optimizada

### 🟣 Toroide (Toro)

> [!example]- 🍩 La Rosquilla Matemática
> 
> **Generatriz:** Círculo que NO pasa por el eje de revolución
> 
> Círculo de radio r con centro a distancia R del eje z:
> 
> $$\begin{cases} x = R + r\cos t \ z = r\sin t \end{cases}$$
> 
> **Ecuación paramétrica completa:**
> 
> $$\begin{cases} x(t, \theta) = (R + r\cos t)\cos\theta \ y(t, \theta) = (R + r\cos t)\sin\theta \ z(t, \theta) = r\sin t \end{cases}$$
> 
> donde:
> 
> - R: radio mayor (del centro del toro al centro del tubo)
> - r: radio menor (del tubo)
> - Condición: R > r (toro estándar)
> 
> **Ecuación implícita:**
> 
> $$(\sqrt{x^2 + y^2} - R)^2 + z^2 = r^2$$
> 
> o en forma expandida:
> 
> $$(x^2 + y^2 + z^2 + R^2 - r^2)^2 = 4R^2(x^2 + y^2)$$
> 
> **Propiedades:**
> 
> - Área superficial: A = 4π²Rr
> - Volumen encerrado: V = 2π²Rr²
> - Género topológico: g = 1 (tiene un "agujero")
> - Curvatura gaussiana variable: positiva en exterior, negativa en interior
> 
> **Variantes:**
> 
> - **R = r:** Toro con cuello (degenerado)
> - **R < r:** Toro auto-intersectante (spindle torus)
> - **R >> r:** Toro delgado (tubular)
> 
> **Aplicaciones:**
> 
> - Cámaras de neumáticos
> - Tokamak (reactor de fusión nuclear)
> - Salvavidas inflables
> - Topología y geometría diferencial

### 🟤 Catenoide

> [!example]- ⛓️ La Superficie Mínima
> 
> **Generatriz:** Catenaria (curva de una cadena colgante)
> 
> $$x = a\cosh\left(\frac{z}{a}\right)$$
> 
> **Ecuación paramétrica:**
> 
> $$\begin{cases} x(z, \theta) = a\cosh(z/a)\cos\theta \ y(z, \theta) = a\cosh(z/a)\sin\theta \ z(z, \theta) = z \end{cases}$$
> 
> **Ecuación implícita:**
> 
> $$\sqrt{x^2 + y^2} = a\cosh\left(\frac{z}{a}\right)$$
> 
> **Propiedades extraordinarias:**
> 
> - **Superficie mínima:** Minimiza área para contorno dado
> - Curvatura media: H = 0
> - Curvatura gaussiana: K = -1/(a²cosh⁴(z/a)) < 0
> - Radio mínimo: r = a (en z = 0)
> 
> **Relación con otras superficies:**
> 
> - Es la única superficie mínima de revolución
> - Se puede transformar en helicoide mediante isometría
> 
> **Aplicaciones:**
> 
> - Películas de jabón entre anillos circulares
> - Arquitectura tensada (membranas)
> - Física: superficies de energía mínima
> - Estudio de tensión superficial

## 📏 Propiedades Geométricas

### 🧮 Cálculo de Áreas y Volúmenes

> [!tip]- 📐 Fórmulas Integrales
> 
> **Área de superficie de revolución (alrededor del eje x):**
> 
> Para y = f(x), a ≤ x ≤ b:
> 
> $$A = 2\pi\int_a^b f(x)\sqrt{1 + [f'(x)]^2},dx$$
> 
> **Área de superficie de revolución (alrededor del eje z):**
> 
> Para x = f(z), c ≤ z ≤ d:
> 
> $$A = 2\pi\int_c^d f(z)\sqrt{1 + [f'(z)]^2},dz$$
> 
> **Volumen por método de discos:**
> 
> $$V = \pi\int_a^b [f(x)]^2,dx$$
> 
> **Volumen por método de cascarones:**
> 
> $$V = 2\pi\int_a^b xf(x),dx$$
> 
> **Teoremas de Pappus:**
> 
> 1. **Volumen:** V = 2πȳA
>     - ȳ: distancia del centroide de la región al eje
>     - A: área de la región plana
> 2. **Área:** S = 2πȳL
>     - ȳ: distancia del centroide de la curva al eje
>     - L: longitud de la curva

### 📊 Curvaturas

> [!note]- 📈 Análisis de Curvatura
> 
> **Curvatura gaussiana K:**
> 
> Para superficie en coordenadas cilíndricas r = f(z):
> 
> $$K = -\frac{f''(z)}{f(z)[1 + (f'(z))^2]^2}$$
> 
> **Curvatura media H:**
> 
> $$H = \frac{f''(z)[1 + (f'(z))^2] - f'(z)^2}{2f(z)[1 + (f'(z))^2]^{3/2}}$$
> 
> **Clasificación por curvatura:**
> 
> |K > 0|K = 0|K < 0|
> |---|---|---|
> |Elipsoide|Cilindro, Cono|Hiperboloide, Catenoide|
> |Forma convexa|Desarrollable|Forma silla|
> |Esfera|Superficie reglada|Superficie mínima|
> 
> **Propiedades:**
> 
> - K = 0: Superficie desarrollable (puede aplanarse sin distorsión)
> - H = 0: Superficie mínima (área mínima local)
> - K constante: Superficies de curvatura constante

## 💻 Implementación Computacional

### 🐍 Código Python para Visualización

> [!success]- 🔧 Generación de Superficies de Revolución
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> from mpl_toolkits.mplot3d import Axes3D
> 
> def superficie_revolucion(f, z_range, n_theta=50, n_z=50):
>     """
>     Genera una superficie de revolución alrededor del eje z.
>     
>     Parámetros:
>     -----------
>     f : function
>         Función que define el radio r = f(z)
>     z_range : tuple
>         (z_min, z_max) rango de z
>     n_theta : int
>         Número de puntos angulares
>     n_z : int
>         Número de puntos en z
>     
>     Retorna:
>     --------
>     X, Y, Z : arrays
>         Mallas de coordenadas para graficar
>     """
>     # Crear mallas paramétricas
>     theta = np.linspace(0, 2*np.pi, n_theta)
>     z = np.linspace(z_range[0], z_range[1], n_z)
>     Theta, Z = np.meshgrid(theta, z)
>     
>     # Calcular radio para cada z
>     R = f(Z)
>     
>     # Convertir a coordenadas cartesianas
>     X = R * np.cos(Theta)
>     Y = R * np.sin(Theta)
>     
>     return X, Y, Z
> 
> # Ejemplo 1: Esfera
> def esfera(z, R=1):
>     return np.sqrt(R**2 - z**2)
> 
> # Ejemplo 2: Paraboloide
> def paraboloide(z, p=2):
>     return np.sqrt(2*p*z)
> 
> # Ejemplo 3: Cono
> def cono(z, a=1):
>     return a * z
> 
> # Ejemplo 4: Hiperboloide de una hoja
> def hiperboloide(z, a=1, b=1):
>     return a * np.sqrt(1 + (z/b)**2)
> 
> # Ejemplo 5: Catenoide
> def catenoide(z, a=1):
>     return a * np.cosh(z/a)
> 
> # Ejemplo 6: Toro
> def toro_generatriz(theta, R=3, r=1):
>     """
>     Genera toro completo (parametrización diferente)
>     """
>     u = np.linspace(0, 2*np.pi, 50)
>     v = np.linspace(0, 2*np.pi, 50)
>     U, V = np.meshgrid(u, v)
>     
>     X = (R + r*np.cos(U)) * np.cos(V)
>     Y = (R + r*np.cos(U)) * np.sin(V)
>     Z = r * np.sin(U)
>     
>     return X, Y, Z
> 
> # Función de graficación
> def graficar_superficie(X, Y, Z, titulo, color='viridis'):
>     """
>     Grafica una superficie 3D
>     """
>     fig = plt.figure(figsize=(10, 8))
>     ax = fig.add_subplot(111, projection='3d')
>     
>     # Graficar superficie
>     surf = ax.plot_surface(X, Y, Z, cmap=color, alpha=0.8,
>                           linewidth=0, antialiased=True)
>     
>     # Configuración
>     ax.set_xlabel('X')
>     ax.set_ylabel('Y')
>     ax.set_zlabel('Z')
>     ax.set_title(titulo, fontsize=14, fontweight='bold')
>     
>     # Barra de color
>     fig.colorbar(surf, shrink=0.5, aspect=5)
>     
>     # Aspecto igual
>     ax.set_box_aspect([1,1,1])
>     
>     plt.tight_layout()
>     return fig, ax
> 
> # Generar y graficar superficies
> if __name__ == "__main__":
>     
>     # 1. Esfera
>     X1, Y1, Z1 = superficie_revolucion(lambda z: esfera(z, R=1), 
>                                        (-1, 1), n_theta=60, n_z=60)
>     graficar_superficie(X1, Y1, Z1, "Esfera (R=1)", 'Blues')
>     
>     # 2. Paraboloide
>     X2, Y2, Z2 = superficie_revolucion(lambda z: paraboloide(z, p=2), 
>                                        (0, 4), n_theta=60, n_z=60)
>     graficar_superficie(X2, Y2, Z2, "Paraboloide (p=2)", 'Reds')
>     
>     # 3. Cono
>     X3, Y3, Z3 = superficie_revolucion(lambda z: cono(z, a=0.5), 
>                                        (0, 5), n_theta=60, n_z=60)
>     graficar_superficie(X3, Y3, Z3, "Cono (a=0.5)", 'Greens')
>     
>     # 4. Hiperboloide
>     X4, Y4, Z4 = superficie_revolucion(lambda z: hiperboloide(z, a=1, b=1), 
>                                        (-3, 3), n_theta=60, n_z=60)
>     graficar_superficie(X4, Y4, Z4, "Hiperboloide de una hoja", 'Purples')
>     
>     # 5. Catenoide
>     X5, Y5, Z5 = superficie_revolucion(lambda z: catenoide(z, a=1), 
>                                        (-2, 2), n_theta=60, n_z=60)
>     graficar_superficie(X5, Y5, Z5, "Catenoide (a=1)", 'Oranges')
>     
>     # 6. Toro
>     X6, Y6, Z6 = toro_generatriz(None, R=3, r=1)
>     graficar_superficie(X6, Y6, Z6, "Toro (R=3, r=1)", 'plasma')
>     
>     plt.show()
> 
> # Función adicional: Calcular área de superficie
> def area_superficie_revolucion(f, df, z_range, n_points=1000):
>     """
>     Calcula el área de una superficie de revolución usando integración numérica.
>     
>     Parámetros:
>     -----------
>     f : function
>         Función radio r = f(z)
>     df : function
>         Derivada de f
>     z_range : tuple
>         (z_min, z_max)
>     n_points : int
>         Número de puntos para integración
>     
>     Retorna:
>     --------
>     area : float
>         Área de la superficie
>     """
>     z = np.linspace(z_range[0], z_range[1], n_points)
>     dz = z[1] - z[0]
>     
>     # Fórmula: A = 2π ∫ r√(1 + (dr/dz)²) dz
>     integrando = f(z) * np.sqrt(1 + df(z)**2)
>     area = 2 * np.pi * np.trapz(integrando, dx=dz)
>     
>     return area
> 
> # Función adicional: Calcular volumen
> def volumen_revolucion(f, z_range, n_points=1000):
>     """
>     Calcula el volumen encerrado por una superficie de revolución.
>     
>     Fórmula: V = π ∫ r² dz
>     """
>     z = np.linspace(z_range[0], z_range[1], n_points)
>     dz = z[1] - z[0]
>     
>     integrando = f(z)**2
>     volumen = np.pi * np.trapz(integrando, dx=dz)
>     
>     return volumen
> 
> # Ejemplo de cálculos
> print("=== CÁLCULOS DE ÁREAS Y VOLÚMENES ===\n")
> 
> # Esfera de radio 1
> print("Esfera (R=1):")
> area_esfera = 4 * np.pi * 1**2  # Fórmula exacta
> vol_esfera = (4/3) * np.pi * 1**3
> print(f"  Área (exacta): {area_esfera:.4f}")
> print(f"  Volumen (exacto): {vol_esfera:.4f}\n")
> 
> # Cono de altura 5, radio base 2.5
> print("Cono (a=0.5, h=5):")
> R_base = 2.5
> h = 5
> generatriz = np.sqrt(R_base**2 + h**2)
> area_cono = np.pi * R_base * generatriz
> vol_cono = (1/3) * np.pi * R_base**2 * h
> print(f"  Área lateral (exacta): {area_cono:.4f}")
> print(f"  Volumen (exacto): {vol_cono:.4f}\n")
> 
> # Cilindro de radio 2, altura 4
> print("Cilindro (R=2, h=4):")
> R_cil = 2
> h_cil = 4
> area_cil = 2 * np.pi * R_cil * h_cil
> vol_cil = np.pi * R_cil**2 * h_cil
> print(f"  Área lateral (exacta): {area_cil:.4f}")
> print(f"  Volumen (exacto): {vol_cil:.4f}\n")
> ```
> 
> **Características del código:**
> - Genera superficies paramétricas completas
> - Visualización 3D interactiva
> - Cálculo numérico de áreas y volúmenes
> - Fácil extensión a nuevas superficies
> - Colormaps personalizables
>  

### 🎮 Visualización Interactiva Avanzada

> [!example]- 🌐 Código con Plotly para Interactividad
> 
> ```python
> import plotly.graph_objects as go
> import numpy as np
> 
> def superficie_interactiva(f, z_range, titulo, n_theta=50, n_z=50):
>     """
>     Crea una visualización interactiva de superficie de revolución
>     usando Plotly
>     """
>     # Generar datos
>     theta = np.linspace(0, 2*np.pi, n_theta)
>     z = np.linspace(z_range[0], z_range[1], n_z)
>     Theta, Z = np.meshgrid(theta, z)
>     R = f(Z)
>     X = R * np.cos(Theta)
>     Y = R * np.sin(Theta)
>     
>     # Crear figura
>     fig = go.Figure(data=[go.Surface(
>         x=X, y=Y, z=Z,
>         colorscale='Viridis',
>         showscale=True,
>         opacity=0.9
>     )])
>     
>     # Configuración del layout
>     fig.update_layout(
>         title=titulo,
>         scene=dict(
>             xaxis_title='X',
>             yaxis_title='Y',
>             zaxis_title='Z',
>             aspectmode='data'
>         ),
>         width=800,
>         height=700
>     )
>     
>     return fig
> 
> # Crear galería de superficies
> superficies = {
>     'Esfera': (lambda z: np.sqrt(1 - z**2), (-1, 1)),
>     'Paraboloide': (lambda z: np.sqrt(2*z), (0.1, 4)),
>     'Cono': (lambda z: 0.5*z, (0, 5)),
>     'Hiperboloide': (lambda z: np.sqrt(1 + z**2), (-3, 3)),
>     'Catenoide': (lambda z: np.cosh(z), (-2, 2))
> }
> 
> # Generar todas las superficies
> for nombre, (func, rango) in superficies.items():
>     fig = superficie_interactiva(func, rango, f"Superficie: {nombre}")
>     fig.show()
> ```

## 🎯 Aplicaciones Prácticas

### 🏗️ Ingeniería y Arquitectura

> [!example]- 🏢 Casos de Uso Real
> 
> **1. Torres de enfriamiento (Hiperboloide):**
> 
> ```python
> def torre_enfriamiento(z, a=20, b=30, h=100):
>     """
>     Diseño de torre de enfriamiento hiperbólica
>     
>     Parámetros:
>     -----------
>     a : float
>         Radio mínimo (cuello) en metros
>     b : float
>         Parámetro de forma
>     h : float
>         Altura total
>     """
>     # Hiperboloide: r = a√(1 + (z/b)²)
>     # Centrado en z = h/2
>     z_centrado = z - h/2
>     return a * np.sqrt(1 + (z_centrado/b)**2)
> 
> # Generar torre
> X_torre, Y_torre, Z_torre = superficie_revolucion(
>     lambda z: torre_enfriamiento(z, a=20, b=30, h=100),
>     (0, 100), n_theta=80, n_z=80
> )
> 
> # Calcular área para determinar materiales
> area = area_superficie_revolucion(
>     lambda z: torre_enfriamiento(z),
>     lambda z: (20 * z) / (30**2 * np.sqrt(1 + (z/30)**2)),  # Derivada
>     (0, 100)
> )
> print(f"Área de superficie: {area:.2f} m²")
> ```
> 
> **2. Cúpulas geodésicas (Esfera truncada):**
> 
> ```python
> def cupula(z, R=10, z_max=8):
>     """
>     Cúpula esférica truncada para edificios
>     """
>     if z > z_max:
>         return 0
>     return np.sqrt(R**2 - z**2)
> 
> # Calcular volumen interior
> V_cupula = volumen_revolucion(
>     lambda z: cupula(z, R=10, z_max=8),
>     (0, 8)
> )
> print(f"Volumen de la cúpula: {V_cupula:.2f} m³")
> ```
> 
> **3. Tanques de almacenamiento:**
> 
> ```python
> def tanque_toroidal(R_mayor=5, r_menor=1):
>     """
>     Tanque en forma de toro para líquidos
>     Ventaja: mayor capacidad, menor espacio
>     """
>     # Volumen del toro
>     V = 2 * np.pi**2 * R_mayor * r_menor**2
>     
>     # Área superficial
>     A = 4 * np.pi**2 * R_mayor * r_menor
>     
>     return V, A
> 
> V_tanque, A_tanque = tanque_toroidal(R_mayor=5, r_menor=1)
> print(f"Capacidad del tanque: {V_tanque:.2f} m³")
> print(f"Área de material: {A_tanque:.2f} m²")
> ```

### 🔭 Astronomía y Física

> [!note]- 🌌 Aplicaciones Científicas
> 
> **1. Forma de planetas (Elipsoide oblato):**
> 
> ```python
> def planeta_rotante(z, R_ecuatorial, R_polar):
>     """
>     Modelo de planeta achatado por rotación
>     
>     Ejemplo: Tierra
>     R_ecuatorial ≈ 6378 km
>     R_polar ≈ 6357 km
>     """
>     # Elipsoide oblato
>     a = R_ecuatorial
>     b = R_polar
>     
>     if abs(z) > b:
>         return 0
>     return a * np.sqrt(1 - z**2/b**2)
> 
> # Tierra
> X_tierra, Y_tierra, Z_tierra = superficie_revolucion(
>     lambda z: planeta_rotante(z, R_ecuatorial=6378, R_polar=6357),
>     (-6357, 6357), n_theta=100, n_z=100
> )
> 
> # Calcular achatamiento
> f = (6378 - 6357) / 6378
> print(f"Achatamiento de la Tierra: {f:.6f}")
> ```
> 
> **2. Espejos parabólicos de telescopios:**
> 
> ```python
> def espejo_parabolico(z, D=1.0, f=2.0):
>     """
>     Espejo parabólico para telescopio
>     
>     Parámetros:
>     -----------
>     D : float
>         Diámetro del espejo (metros)
>     f : float
>         Distancia focal (metros)
>     
>     Relación: z = r²/(4f)
>     Invertido: r = √(4fz)
>     """
>     # Parámetro focal p = 2f
>     p = 2 * f
>     return np.sqrt(2 * p * z)
> 
> # Ejemplo: Espejo de 1m de diámetro, focal 2m
> z_max = (0.5)**2 / (4 * 2.0)  # Profundidad máxima
> 
> X_espejo, Y_espejo, Z_espejo = superficie_revolucion(
>     lambda z: espejo_parabolico(z, D=1.0, f=2.0),
>     (0, z_max), n_theta=60, n_z=60
> )
> 
> print(f"Profundidad del espejo: {z_max*1000:.2f} mm")
> ```
> 
> **3. Antenas parabólicas:**
> 
> ```python
> def antena_parabolica(D=3.0, f=1.2):
>     """
>     Diseño de antena parabólica satelital
>     
>     Parámetros típicos:
>     D = 0.6m (uso doméstico) a 30m (radio astronomía)
>     f/D = 0.3-0.5 (relación focal típica)
>     """
>     # Profundidad del plato
>     h = D**2 / (16 * f)
>     
>     # Ganancia aproximada (dB)
>     lamb = 0.03  # Longitud de onda típica (10 GHz)
>     G_dB = 10 * np.log10((np.pi * D / lamb)**2 * 0.6)
>     
>     return h, G_dB
> 
> h_antena, ganancia = antena_parabolica(D=3.0, f=1.2)
> print(f"Profundidad de la antena: {h_antena:.3f} m")
> print(f"Ganancia estimada: {ganancia:.1f} dB")
> ```

### 🎨 Diseño Industrial y CAD

> [!tip]- 🔧 Modelado de Productos
> 
> **1. Botellas y envases:**
> 
> ```python
> def botella_perfil(z, tipo='vino'):
>     """
>     Perfiles de botellas comerciales
>     """
>     if tipo == 'vino':
>         # Base cilíndrica + cuello cónico
>         if z < 20:
>             return 4.0  # Base cilíndrica
>         elif z < 25:
>             return 4.0 - (z - 20) * 0.6  # Transición
>         else:
>             return 1.0  # Cuello
>     
>     elif tipo == 'refresco':
>         # Forma más compleja (spline simplificado)
>         if z < 5:
>             return 3.0  # Base
>         elif z < 15:
>             return 3.0 + 0.5 * np.sin(np.pi * (z - 5) / 10)
>         else:
>             return 2.5 - (z - 15) * 0.1
>     
>     return 2.0
> 
> # Generar botella de vino
> X_botella, Y_botella, Z_botella = superficie_revolucion(
>     lambda z: botella_perfil(z, tipo='vino'),
>     (0, 30), n_theta=60, n_z=100
> )
> 
> # Calcular volumen (capacidad)
> V_botella = volumen_revolucion(
>     lambda z: botella_perfil(z, tipo='vino'),
>     (0, 30)
> )
> print(f"Capacidad de la botella: {V_botella/1000:.2f} litros")
> ```
> 
> **2. Componentes mecánicos (ejes, poleas):**
> 
> ```python
> def eje_escalonado(z, diametros, alturas):
>     """
>     Eje mecánico con múltiples diámetros
>     
>     Ejemplo: eje de transmisión
>     """
>     z_acum = 0
>     for i, (d, h) in enumerate(zip(diametros, alturas)):
>         if z < z_acum + h:
>             return d / 2
>         z_acum += h
>     return diametros[-1] / 2
> 
> # Ejemplo: eje con 3 secciones
> diams = [40, 30, 20]  # mm
> alts = [50, 30, 40]   # mm
> 
> X_eje, Y_eje, Z_eje = superficie_revolucion(
>     lambda z: eje_escalonado(z, diams, alts),
>     (0, sum(alts)), n_theta=40, n_z=60
> )
> ```
> 
> **3. Lentes ópticas:**
> 
> ```python
> def lente_convergente(z, R1=50, R2=50, espesor_central=10):
>     """
>     Lente biconvexa (convergente)
>     
>     Parámetros:
>     -----------
>     R1, R2 : float
>         Radios de curvatura (mm)
>     espesor_central : float
>         Grosor en el centro (mm)
>     """
>     # Perfil basado en esferas
>     # Superficie frontal (0 < z < espesor/2)
>     # Superficie posterior (espesor/2 < z < espesor)
>     
>     if z < espesor_central / 2:
>         # Primera superficie esférica
>         z_rel = espesor_central / 2 - z
>         if z_rel < R1:
>             return np.sqrt(R1**2 - z_rel**2) - R1 + espesor_central/2
>     else:
>         # Segunda superficie esférica
>         z_rel = z - espesor_central / 2
>         if z_rel < R2:
>             return np.sqrt(R2**2 - z_rel**2) - R2 + espesor_central/2
>     
>     return espesor_central / 2
> 
> # Calcular distancia focal (lente delgada)
> def distancia_focal_lente(R1, R2, n=1.5):
>     """
>     Ecuación del fabricante de lentes
>     n: índice de refracción del vidrio
>     """
>     f = 1 / ((n - 1) * (1/R1 + 1/R2))
>     return f
> 
> f_lente = distancia_focal_lente(R1=50, R2=50, n=1.5)
> print(f"Distancia focal: {f_lente:.2f} mm")
> ```

### 🎢 Entretenimiento y Arte

> [!example]- 🎨 Aplicaciones Creativas
> 
> **1. Diseño de montañas rusas (loops):**
> 
> ```python
> def loop_montaña_rusa(theta, R=10, forma='circular'):
>     """
>     Perfil de loop vertical
>     
>     Formas:
>     - 'circular': círculo perfecto (no óptimo)
>     - 'clothoid': espiral de Cornu (óptimo)
>     """
>     if forma == 'circular':
>         x = R * (1 - np.cos(theta))
>         z = R * np.sin(theta)
>     elif forma == 'clothoid':
>         # Simplificación: radio variable
>         # Radio aumenta en la parte superior
>         R_var = R * (1 + 0.3 * np.sin(theta))
>         x = R_var * (1 - np.cos(theta))
>         z = R_var * np.sin(theta)
>     
>     return x, z
> 
> # Generar loop
> theta_loop = np.linspace(0, 2*np.pi, 100)
> x_loop, z_loop = loop_montaña_rusa(theta_loop, R=10, forma='clothoid')
> 
> # Si se rota este perfil, se obtiene un "tornado" 3D
> ```
> 
> **2. Esculturas matemáticas:**
> 
> ```python
> def escultura_artistica(z, periodo=5):
>     """
>     Superficie artística con modulación sinusoidal
>     """
>     # Base + ondulación
>     r_base = 2 + 0.5 * np.sin(2 * np.pi * z / periodo)
>     return r_base * (1 + 0.2 * np.cos(4 * np.pi * z / periodo))
> 
> X_art, Y_art, Z_art = superficie_revolucion(
>     lambda z: escultura_artistica(z, periodo=5),
>     (0, 20), n_theta=100, n_z=100
> )
> ```
> 
> **3. Instrumentos musicales (campanas, trompetas):**
> 
> ```python
> def campana_perfil(z, h=30, R_base=15, R_boca=20):
>     """
>     Perfil de campana musical
>     Forma aproximada: combinación de curvas
>     """
>     t = z / h  # Normalizar 0 a 1
>     
>     if t < 0.3:
>         # Corona (parte superior)
>         return R_base * (1 - 0.3 * t)
>     elif t < 0.7:
>         # Cuerpo (expansión gradual)
>         return R_base + (R_boca - R_base) * ((t - 0.3) / 0.4)**1.5
>     else:
>         # Boca (abertura final)
>         return R_boca + (R_boca * 0.1) * np.sin(np.pi * (t - 0.7) / 0.3)
> 
> X_campana, Y_campana, Z_campana = superficie_revolucion(
>     lambda z: campana_perfil(z, h=30, R_base=15, R_boca=20),
>     (0, 30), n_theta=80, n_z=100
> )
> ```

## 🧪 Ejercicios Progresivos

> [!example]- 💪 Práctica Graduada
> 
> **Nivel 1 - Identificación:** 🟢
> 
> 1. **Reconocimiento:**
>    - Identificar la superficie generada por y = x rotada alrededor del eje x
>    - Respuesta: Cono circular recto
> 
> 2. **Ecuación simple:**
>    - Escribir la ecuación de la esfera de radio 5 centrada en el origen
>    - Respuesta: x² + y² + z² = 25
> 
> 3. **Generatriz:**
>    - ¿Qué curva genera un cilindro de radio 3 al rotar alrededor del eje z?
>    - Respuesta: Línea recta x = 3 paralela al eje z
> 
> 4. **Clasificación:**
>    - ¿La superficie x² + y² = 4z² es un cono, cilindro o paraboloide?
>    - Respuesta: Cono (z² aparece con mismo coeficiente que x² + y²)
> 
> **Nivel 2 - Parametrización:** 🟡
> 
> 5. **Paraboloide:**
>    - Parametrizar el paraboloide z = x² + y² usando coordenadas cilíndricas
>    - Respuesta: x = r cos θ, y = r sin θ, z = r²
> 
> 6. **Hiperboloide:**
>    - Escribir las ecuaciones paramétricas del hiperboloide x² + y² - z² = 1
>    - Respuesta: x = cosh(u) cos(v), y = cosh(u) sin(v), z = sinh(u)
> 
> 7. **Toro:**
>    - Parametrizar un toro con R = 4, r = 1
>    - Respuesta: 
>      - x = (4 + cos u) cos v
>      - y = (4 + cos u) sin v
>      - z = sin u
> 
> 8. **Catenoide:**
>    - Encontrar la ecuación del catenoide con a = 2
>    - Respuesta: r = 2 cosh(z/2) o √(x² + y²) = 2 cosh(z/2)
> 
> **Nivel 3 - Cálculos:** 🔴
> 
> 9. **Área de superficie:**
>    - Calcular el área de la esfera de radio R
>    - Respuesta: A = 4πR²
> 
> 10. **Volumen:**
>     - Calcular el volumen del cono de altura h y radio base R
>     - Respuesta: V = (1/3)πR²h
> 
> 11. **Problema aplicado:**
>     - Una antena parabólica tiene diámetro 2m y profundidad 0.25m. 
>       Encontrar la distancia focal.
>     - Solución: z = x²/(4f), entonces 0.25 = 1²/(4f), f = 1m
> 
> 12. **Intersección:**
>     - Encontrar la curva de intersección entre el cilindro x² + y² = 4 
>       y el plano z = x
>     - Respuesta: Elipse en el plano inclinado
> 
> **Nivel 4 - Desafíos:** 🟣
> 
> 13. **Optimización:**
>     - Encontrar el cilindro de volumen máximo inscrito en una esfera de radio R
>     - Respuesta: h = 2R/√3, r = R√(2/3), V_max = (4πR³)/(3√3)
> 
> 14. **Curvatura:**
>     - Calcular la curvatura gaussiana del paraboloide z = x² + y² en el origen
>     - Respuesta: K = 4
> 
> 15. **Problema físico:**
>     - Un líquido en rotación adopta forma de paraboloide. Si gira a ω rad/s,
>       encontrar la ecuación de la superficie.
>     - Respuesta: z = (ω²/2g)(x² + y²)
> 
> 16. **Superficie mínima:**
>     - Demostrar que el catenoide r = a cosh(z/a) es una superficie mínima
>       (curvatura media H = 0)
>     - Pista: Calcular H usando la fórmula de curvatura en coordenadas cilíndricas

## 📊 Tabla Comparativa de Superficies

> [!note]- 📋 Resumen Completo
> 
> | Superficie | Ecuación Implícita | Generatriz | K (Curvatura) | Aplicaciones |
> |------------|-------------------|------------|---------------|--------------|
> | **Esfera** | x² + y² + z² = R² | Semicírculo | 1/R² > 0 | Balones, planetas |
> | **Cilindro** | x² + y² = R² | Línea recta | 0 | Tuberías, columnas |
> | **Cono** | x² + y² = a²z² | Línea inclinada | 0 | Embudos, volcanes |
> | **Paraboloide** | z = (x²+y²)/(2p) | Parábola | > 0 | Antenas, telescopios |
> | **Elipsoide** | x²/a² + y²/a² + z²/b² = 1 | Elipse | > 0 | Planetas, huevos |
> | **Hiperboloide 1** | x²/a² + y²/a² - z²/b² = 1 | Hipérbola | < 0 | Torres de enfriamiento |
> | **Hiperboloide 2** | z²/c² - x²/a² - y²/a² = 1 | Hipérbola | < 0 | Física de partículas |
> | **Toro** | (√(x²+y²)-R)² + z² = r² | Círculo | Variable | Neumáticos, tokamak |
> | **Catenoide** | √(x²+y²) = a cosh(z/a) | Catenaria | < 0 | Películas de jabón |
> 
> **Leyenda de curvatura:**
> - K > 0: Forma convexa (tipo esfera)
> - K = 0: Desarrollable (puede aplanarse)
> - K < 0: Forma de silla (hiperbólica)

## 🌐 Conexiones Conceptuales

> [!quote]- 🔗 Enlaces con Otros Temas
> 
> **Prerequisitos:**
> - [[Coordenadas Cilíndricas]] - Sistema natural para superficies de revolución
> - [[Coordenadas Esféricas]] - Para esfera y elipsoides
> - [[Curvas Paramétricas]] - Generatrices
> - [[Vectores en ℝ³]] - Normal y tangentes a superficies
> - [[Cálculo Integral]] - Áreas y volúmenes
> 
> **Temas relacionados:**
> - [[Superficies Cuádricas]] - Clasificación algebraica
> - [[Sólidos de Revolución]] - Volúmenes
> - [[Curvaturas]] - Análisis geométrico diferencial
> - [[Ecuaciones Paramétricas en 3D]] - Representación
> 
> **Aplicaciones directas:**
> - [[Cálculo de Áreas de Superficie]] - Integrales de superficie
> - [[Centros de Masa]] - Teoremas de Pappus
> - [[Momento de Inercia]] - Física rotacional
> - [[Optimización en 3D]] - Problemas isoperimétricos
> 
> **Temas avanzados:**
> - [[Geometría Diferencial]] - Curvaturas y geodésicas
> - [[Superficies Mínimas]] - Catenoide, helicoide
> - [[CAD/CAM]] - Modelado industrial
> - [[Gráficos por Computadora]] - Rendering de superficies
> 
> **Aplicaciones interdisciplinarias:**
> 
> - [[Física]] - Formas en equilibrio, rotación de fluidos
> - [[Arquitectura]] - Estructuras de revolución optimizadas
> - [[Astronomía]] - Forma de cuerpos celestes
> - [[Ingeniería Mecánica]] - Diseño de componentes axisimétricos
> - [[Óptica]] - Lentes, espejos y sistemas de reflexión

## 💡 Consejos de Estudio

> [!tip]- 🧠 Estrategias de Aprendizaje
> 
> **Para identificar superficies:**
> 
> 1. **Buscar simetría rotacional:**
>     - Si x e y aparecen solo como x² + y² → Revolución alrededor de z
>     - Si y y z aparecen solo como y² + z² → Revolución alrededor de x
> 2. **Analizar la ecuación:**
>     - **Suma de cuadrados = constante** → Esfera o elipsoide
>     - **Suma de cuadrados = función lineal de z** → Cono
>     - **Suma de cuadrados = función cuadrática de z** → Paraboloide
>     - **Diferencia de cuadrados** → Hiperboloide
> 3. **Método del corte:**
>     - Cortar con planos z = k (paralelos perpendiculares al eje)
>     - Si son círculos → superficie de revolución
>     - El radio r(z) define la generatriz
> 
> **Nemotecnia para clasificación:**
> 
> **ESCP-HT:**
> 
> - **E**sfera: x² + y² + z² = R²
> - **C**ilindro: x² + y² = R²
> - **C**ono: x² + y² = a²z²
> - **P**araboloide: z = a(x² + y²)
> - **H**iperboloide: x² + y² - z² = ±1
> - **T**oro: (√(x²+y²) - R)² + z² = r²
> 
> **Visualización mental:**
> 
> ```
> Generatriz → Rotación → Superficie
> 
> Línea recta:
>   Vertical     → Cilindro
>   Inclinada    → Cono
>   
> Curva:
>   Círculo      → Esfera (si pasa por eje) o Toro (si no pasa)
>   Parábola     → Paraboloide
>   Hipérbola    → Hiperboloide
>   Catenaria    → Catenoide
> ```
> 
> **Errores comunes a evitar:**
> 
> - ❌ Confundir hiperboloide de una y dos hojas (signos)
> - ❌ Olvidar el dominio de las funciones (especialmente raíces cuadradas)
> - ❌ No verificar que la generatriz sea válida para todo el rango
> - ❌ Parametrizar incorrectamente el ángulo θ (debe ir de 0 a 2π)
> - ❌ Confundir radio con diámetro en problemas aplicados
> 
> **Verificación de resultados:**
> 
> 1. **Simetría:** Rotar la ecuación paramétrica θ → θ + π debe dar el mismo punto
> 2. **Límites:** Verificar comportamiento en extremos del dominio
> 3. **Casos conocidos:** Comparar con fórmulas de área/volumen estándar
> 4. **Visualización:** Graficar siempre que sea posible

## 🔬 Propiedades Avanzadas

### 📐 Análisis Diferencial

> [!warning]- 🟡 Geometría Diferencial de Superficies
> 
> **Vector normal unitario:**
> 
> Para superficie parametrizada como **r**(u, v):
> 
> $$\mathbf{n} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{|\mathbf{r}_u \times \mathbf{r}_v|}$$
> 
> **Primera forma fundamental (métrica):**
> 
> $$ds^2 = E,du^2 + 2F,du,dv + G,dv^2$$
> 
> donde:
> 
> - E = **r**_u · **r**_u
> - F = **r**_u · **r**_v
> - G = **r**_v · **r**_v
> 
> **Segunda forma fundamental (curvatura):**
> 
> $$II = L,du^2 + 2M,du,dv + N,dv^2$$
> 
> donde:
> 
> - L = **r**_uu · **n**
> - M = **r**_uv · **n**
> - N = **r**_vv · **n**
> 
> **Curvaturas principales:**
> 
> $$\kappa_1, \kappa_2 = \frac{H \pm \sqrt{H^2 - K}}{1}$$
> 
> donde:
> 
> - H = (κ₁ + κ₂)/2 (curvatura media)
> - K = κ₁κ₂ (curvatura gaussiana)
> 
> **Ejemplo: Esfera de radio R**
> 
> ```python
> # Parametrización esférica
> def esfera_parametrica(phi, theta, R=1):
>     x = R * np.sin(phi) * np.cos(theta)
>     y = R * np.sin(phi) * np.sin(theta)
>     z = R * np.cos(phi)
>     return x, y, z
> 
> # Curvaturas
> K_esfera = 1 / R**2  # Gaussiana
> H_esfera = 1 / R      # Media
> kappa_1 = kappa_2 = 1 / R  # Principales (iguales)
> 
> print(f"La esfera tiene curvatura constante en todas direcciones")
> ```

### 🎲 Clasificación Topológica

> [!info]- 🔵 Invariantes Topológicos
> 
> **Característica de Euler (χ):**
> 
> Para superficie triangulada:
> 
> $$\chi = V - E + F$$
> 
> donde V = vértices, E = aristas, F = caras
> 
> **Valores para superficies comunes:**
> 
> |Superficie|χ|Género (g)|Comentario|
> |---|---|---|---|
> |Esfera|2|0|Sin agujeros|
> |Toro|0|1|Un agujero|
> |Bitoro|-2|2|Dos agujeros|
> |Superficie cerrada|2-2g|g|Fórmula general|
> 
> **Relación:** χ = 2 - 2g
> 
> **Propiedades:**
> 
> - Invariante bajo deformaciones continuas (homeomorfismos)
> - Las superficies de revolución cerradas tienen g = 0 o g = 1
> - Esfera, elipsoide, paraboloide cerrado: g = 0
> - Toro: g = 1
> 
> **Clasificación por curvatura total:**
> 
> $$\int_S K , dA = 2\pi\chi$$
> 
> (Teorema de Gauss-Bonnet)

### 🌊 Superficies Mínimas

> [!success]- 🟢 Minimización de Área
> 
> **Definición:** Una superficie es **mínima** si tiene curvatura media H = 0 en todos los puntos.
> 
> **Propiedad física:**
> 
> - Superficie de área mínima para un contorno dado
> - Película de jabón adopta forma de superficie mínima
> 
> **Superficies mínimas de revolución:**
> 
> 1. **Catenoide** (única no trivial):
>     - r = a cosh(z/a)
>     - H = 0 en todas partes
>     - K < 0 (curvatura gaussiana negativa)
> 2. **Plano** (trivial):
>     - z = 0
>     - H = K = 0
> 
> **Ecuación diferencial:**
> 
> Para superficie de revolución r = f(z), la condición H = 0 implica:
> 
> $$\frac{d}{dz}\left(\frac{rf'(z)}{\sqrt{1 + [f'(z)]^2}}\right) = \sqrt{1 + [f'(z)]^2}$$
> 
> Solución: r = a cosh(z/a) + c (catenoide desplazado)
> 
> **Experimento con pompas de jabón:**
> 
> ```python
> def experimento_jabon(R1, R2, d):
>     """
>     Dos aros circulares paralelos de radios R1 y R2
>     separados por distancia d.
>     
>     La película de jabón forma un catenoide si:
>     d < d_crítico = a * arcosh(R2/R1)
>     
>     donde a es el parámetro del catenoide.
>     """
>     # Calcular parámetro 'a' del catenoide
>     # Resolver: R1 = a*cosh(0), R2 = a*cosh(d/a)
>     
>     # Simplificación: si R1 = R2, entonces a = R1 y superficie es cilindro
>     if abs(R1 - R2) < 0.01:
>         return "Cilindro (caso degenerado)"
>     
>     # Distancia crítica para existencia de catenoide
>     if R1 > R2:
>         R1, R2 = R2, R1  # Asegurar R1 ≤ R2
>     
>     # Estimación: d_crit ≈ 1.32 * R1 (para R2/R1 pequeño)
>     d_crit = 1.32 * R1
>     
>     if d < d_crit:
>         return f"Catenoide estable (d = {d:.2f} < {d_crit:.2f})"
>     else:
>         return f"Dos discos separados (d = {d:.2f} > {d_crit:.2f})"
> 
> # Ejemplo
> resultado = experimento_jabon(R1=5, R2=7, d=6)
> print(resultado)
> ```

## 🎯 Problemas Especiales

### 🏆 Problemas de Olimpiada

> [!example]- 🥇 Desafíos Avanzados
> 
> **Problema 1: Intersección óptima**
> 
> Dado un cono x² + y² = z² y una esfera x² + y² + z² = 4, encontrar: a) La curva de intersección b) El área de la superficie esférica dentro del cono
> 
> **Solución:**
> 
> ```
> a) Sustituyendo x² + y² = z² en la esfera:
>    z² + z² = 4
>    2z² = 4
>    z = ±√2
>    
>    Curva de intersección: círculos z = √2 con radio √2
>    
> b) Usando coordenadas esféricas:
>    Superficie limitada por θ = π/4
>    
>    A = ∫∫ R² sin φ dφ dθ
>    A = 2πR²(1 - cos(π/4))
>    A = 2π·4·(1 - 1/√2)
>    A ≈ 7.39 unidades²
> ```
> 
> **Problema 2: Volumen máximo**
> 
> Inscribir un cilindro de volumen máximo en un cono de altura h y radio base R.
> 
> **Solución:**
> 
> ```
> Sea el cilindro de radio r y altura y.
> Por semejanza: r = R(h-y)/h
> 
> Volumen: V(y) = πr²y = π[R(h-y)/h]²y
> V(y) = πR²(h-y)²y/h²
> 
> Maximizar:
> dV/dy = πR²/h² [(h-y)² - 2(h-y)y] = 0
> (h-y)² = 2(h-y)y
> h-y = 2y
> y = h/3
> 
> r = R(h-h/3)/h = 2R/3
> 
> V_max = π(2R/3)²(h/3) = 4πR²h/27
> ```
> 
> **Problema 3: Geodésicas**
> 
> Encontrar la geodésica (camino más corto) sobre un cilindro entre dos puntos.
> 
> **Solución:**
> 
> ```
> En cilindro x² + y² = R²:
> - Desarrollar el cilindro en plano
> - La geodésica es una línea recta en el plano desarrollado
> - Al enrollar de vuelta: hélice
> 
> Ecuación paramétrica:
> x(t) = R cos(t)
> y(t) = R sin(t)
> z(t) = at
> 
> donde a depende de los puntos inicial y final
> ```

### 🔧 Problemas de Ingeniería

> [!tip]- ⚙️ Casos Aplicados
> 
> **Problema 4: Diseño de tanque**
> 
> Diseñar un tanque de almacenamiento de 1000 m³ con forma de revolución que minimice el área superficial (y por tanto el costo de material).
> 
> **Análisis:**
> 
> ```python
> def optimizar_tanque(volumen_deseado):
>     """
>     Para volumen fijo, la esfera minimiza área superficial.
>     
>     V = (4/3)πR³ = 1000
>     R = (3V/(4π))^(1/3)
>     
>     A = 4πR²
>     """
>     R = (3 * volumen_deseado / (4 * np.pi))**(1/3)
>     A = 4 * np.pi * R**2
>     
>     return R, A
> 
> R_optimo, A_minima = optimizar_tanque(1000)
> print(f"Radio óptimo: {R_optimo:.2f} m")
> print(f"Área mínima: {A_minima:.2f} m²")
> 
> # Comparar con cilindro de igual volumen (h = 2R)
> R_cil = (1000 / (2*np.pi))**(1/3)
> A_cil = 2*np.pi*R_cil**2 + 2*np.pi*R_cil*(2*R_cil)  # 2 tapas + lateral
> A_cil = 6*np.pi*R_cil**2
> 
> print(f"\nCilindro (h=2R):")
> print(f"Radio: {R_cil:.2f} m")
> print(f"Área: {A_cil:.2f} m²")
> print(f"Incremento vs esfera: {(A_cil/A_minima - 1)*100:.1f}%")
> ```
> 
> **Problema 5: Torre de enfriamiento**
> 
> Una torre de enfriamiento hiperbólica debe tener:
> 
> - Altura: 100 m
> - Radio base: 40 m
> - Radio superior: 30 m
> - Radio mínimo (cuello): 25 m a 60 m de altura
> 
> Encontrar la ecuación del perfil.
> 
> **Solución:**
> 
> ```python
> def perfil_torre_enfriamiento(z, h=100, R_base=40, R_top=30, 
>                               R_min=25, z_min=60):
>     """
>     Hiperboloide con parámetros ajustados
>     
>     Forma general: r² = a² + b²(z - z₀)²
>     
>     Condiciones:
>     - r(0) = R_base
>     - r(z_min) = R_min
>     - r(h) = R_top
>     """
>     # Centrar en el cuello
>     z_rel = z - z_min
>     
>     # Determinar a y b por condiciones
>     # En cuello: r = R_min, z_rel = 0 → a = R_min
>     a = R_min
>     
>     # En base: r = R_base, z_rel = -z_min
>     # R_base² = a² + b²z_min²
>     b_squared = (R_base**2 - a**2) / z_min**2
>     b = np.sqrt(b_squared)
>     
>     # Calcular radio
>     r = np.sqrt(a**2 + b**2 * z_rel**2)
>     
>     return r
> 
> # Verificación
> z_test = [0, 60, 100]
> for z in z_test:
>     r = perfil_torre_enfriamiento(z)
>     print(f"z = {z} m: r = {r:.2f} m")
> 
> # Calcular volumen de concreto (espesor 30 cm)
> def volumen_concreto(espesor=0.3):
>     z = np.linspace(0, 100, 1000)
>     r_ext = perfil_torre_enfriamiento(z)
>     r_int = r_ext - espesor
>     
>     # Volumen = π∫(r_ext² - r_int²)dz
>     dz = z[1] - z[0]
>     V = np.pi * np.trapz(r_ext**2 - r_int**2, dx=dz)
>     return V
> 
> V_concreto = volumen_concreto()
> print(f"\nVolumen de concreto: {V_concreto:.2f} m³")
> ```
> 
> **Problema 6: Lente asférica**
> 
> Diseñar una lente con perfil no esférico que corrija aberración esférica.
> 
> **Enfoque:**
> 
> ```python
> def lente_asferica(r, R0, k, A4=0, A6=0):
>     """
>     Perfil asférico generalizado
>     
>     z(r) = (r²/R₀)/(1 + √(1 - (1+k)(r/R₀)²)) + A₄r⁴ + A₆r⁶
>     
>     Parámetros:
>     -----------
>     r : float
>         Distancia radial
>     R0 : float
>         Radio de curvatura base
>     k : float
>         Constante cónica (k=-1: parábola, k=0: esfera)
>     A4, A6 : float
>         Coeficientes asféricos de orden superior
>     """
>     # Término cónico
>     r_norm = r / R0
>     discriminante = 1 - (1 + k) * r_norm**2
>     
>     if discriminante < 0:
>         return np.nan  # Fuera del dominio válido
>     
>     z_conico = (r**2 / R0) / (1 + np.sqrt(discriminante))
>     
>     # Términos asféricos
>     z_asferico = A4 * r**4 + A6 * r**6
>     
>     return z_conico + z_asferico
> 
> # Ejemplo: lente parabólica (k=-1) sin aberración esférica
> r_values = np.linspace(0, 10, 100)
> z_values = [lente_asferica(r, R0=50, k=-1) for r in r_values]
> 
> # Rotar para obtener superficie 3D
> # (código de generación de superficie similar a ejemplos anteriores)
> ```

## 📚 Recursos Adicionales

### 📖 Material de Referencia

> [!note]- 📚 Lecturas Recomendadas
> 
> **Textos clásicos:**
> 
> 1. **Do Carmo, M. - "Differential Geometry of Curves and Surfaces"**
>     - Capítulo 3: Superficies de revolución
>     - Tratamiento riguroso de curvaturas
> 2. **Stewart, J. - "Calculus: Early Transcendentals"**
>     - Sección 12.6: Superficies cuádricas
>     - Sección 15.7: Áreas de superficies
> 3. **Thomas, Weir, Hass - "Thomas' Calculus"**
>     - Capítulo 16: Integrales de superficie
>     - Aplicaciones físicas
> 
> **Recursos online:**
> 
> - **Paul's Online Math Notes** - Superficies de revolución
> - **Wolfram MathWorld** - Surfaces of Revolution
> - **GeoGebra** - Visualizaciones interactivas 3D
> - **Desmos 3D** - Graficador en línea
> 
> **Software recomendado:**
> 
> - **Mathematica/Wolfram Alpha** - Cálculo simbólico
> - **MATLAB** - Análisis numérico
> - **Python (matplotlib, plotly)** - Visualización
> - **Blender** - Modelado 3D
> - **AutoCAD/SolidWorks** - CAD profesional

### 🎬 Visualizaciones Dinámicas

> [!tip]- 🎥 Crear Animaciones
> 
> ```python
> import matplotlib.pyplot as plt
> from matplotlib.animation import FuncAnimation
> from mpl_toolkits.mplot3d import Axes3D
> 
> def animar_revolucion(f, z_range, n_frames=60):
>     """
>     Anima el proceso de generación de una superficie de revolución
>     """
>     fig = plt.figure(figsize=(12, 5))
>     
>     # Subplot 1: Generatriz 2D
>     ax1 = fig.add_subplot(121)
>     
>     # Subplot 2: Superficie 3D
>     ax2 = fig.add_subplot(122, projection='3d')
>     
>     # Generatriz
>     z = np.linspace(z_range[0], z_range[1], 100)
>     r = f(z)
>     
>     def update(frame):
>         ax1.clear()
>         ax2.clear()
>         
>         # Ángulo actual
>         theta_max = 2 * np.pi * frame / n_frames
>         
>         # Graficar generatriz
>         ax1.plot(r, z, 'b-', linewidth=2, label='Generatriz')
>         ax1.axvline(0, color='k', linestyle='--', alpha=0.3)
>         ax1.set_xlabel('Radio')
>         ax1.set_ylabel('Z')
>         ax1.set_title('Curva Generatriz')
>         ax1.grid(True, alpha=0.3)
>         ax1.legend()
>         ax1.set_aspect('equal')
>         
>         # Graficar superficie parcial
>         theta = np.linspace(0, theta_max, 50)
>         Theta, Z = np.meshgrid(theta, z)
>         R = f(Z)
>         X = R * np.cos(Theta)
>         Y = R * np.sin(Theta)
>         
>         ax2.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')
>         ax2.set_xlabel('X')
>         ax2.set_ylabel('Y')
>         ax2.set_zlabel('Z')
>         ax2.set_title(f'Revolución: {theta_max*180/np.pi:.0f}°')
>         ax2.set_box_aspect([1,1,1])
>         
>         return ax1, ax2
>     
>     anim = FuncAnimation(fig, update, frames=n_frames, 
>                         interval=50, repeat=True)
>     
>     return anim
> 
> # Ejemplo: Animar creación de paraboloide
> anim = animar_revolucion(lambda z: np.sqrt(2*z), (0, 4))
> plt.show()
> 
> # Guardar animación
> # anim.save('paraboloide_revolucion.gif', writer='pillow', fps=20)
> ```

---

## 🎓 Resumen Final

> [!abstract]- 📝 Puntos Clave
> 
> **Conceptos fundamentales:**
> 
> 1. **Definición:** Superficie generada al rotar una curva (generatriz) alrededor de un eje
>     
> 2. **Elementos:**
>     
>     - Generatriz: curva que se rota
>     - Eje de revolución: línea fija
>     - Meridianos: cortes con planos que contienen el eje
>     - Paralelos: círculos perpendiculares al eje
> 3. **Ecuaciones:**
>     
>     - **Paramétrica:** x = f(t)cos θ, y = f(t)sin θ, z = g(t)
>     - **Implícita:** F(√(x²+y²), z) = 0
>     - **Cilíndricas:** r = f(z), θ libre
> 4. **Superficies clásicas:**
>     
>     - Esfera: x² + y² + z² = R²
>     - Cilindro: x² + y² = R²
>     - Cono: x² + y² = a²z²
>     - Paraboloide: z = (x²+y²)/(2p)
>     - Hiperboloide: x²/a² + y²/a² ∓ z²/b² = ±1
>     - Toro: (√(x²+y²) - R)² + z² = r²
>     - Catenoide: √(x²+y²) = a cosh(z/a)
> 5. **Propiedades geométricas:**
>     
>     - Simetría rotacional completa
>     - Curvatura varía según la generatriz
>     - Área y volumen calculables por integrales
> 6. **Aplicaciones:**
>     
>     - Ingeniería: torres, tanques, componentes mecánicos
>     - Física: óptica, astronomía, mecánica de fluidos
>     - Arquitectura: cúpulas, estructuras optimizadas
>     - Diseño industrial: envases, lentes, instrumentos

**Tags:** #geometría-analítica #superficies #revolución #sólidos-3d #coordenadas-cilíndricas #parametrización #curvatura #cálculo-integral #aplicaciones #university #mathematics #CAD #ingeniería #física #visualización-3d
`

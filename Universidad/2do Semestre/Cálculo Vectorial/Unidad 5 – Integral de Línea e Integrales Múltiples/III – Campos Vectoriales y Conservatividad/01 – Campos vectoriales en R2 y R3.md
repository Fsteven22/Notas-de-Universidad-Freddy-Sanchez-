# 🌊 Campos Vectoriales en ℝ² y ℝ³

## 🎯 Fundamentos de Campos Vectoriales

> [!info]- 💡 Introducción a los Campos Vectoriales Un **campo vectorial** es una función que asigna un vector a cada punto del espacio. Imagina que en cada ubicación del espacio hay una "flecha" que indica dirección y magnitud de alguna cantidad física.
> 
> **Analogías útiles:**
> 
> - **🌬️ Viento:** En cada punto del espacio hay un vector velocidad
> - **🧲 Magnetismo:** Limaduras de hierro se alinean con el campo magnético
> - **🌊 Corriente de agua:** El flujo tiene dirección y velocidad en cada punto
> - **⚡ Campo eléctrico:** Cargas experimentan fuerzas en diferentes direcciones
> - **🌡️ Flujo de calor:** El calor fluye en dirección del gradiente de temperatura
> 
> **Diferencia con funciones escalares:**
> 
> ```
> Función escalar: f: ℝⁿ → ℝ
> Ejemplo: T(x,y,z) = temperatura en cada punto
> 
> Campo vectorial: F: ℝⁿ → ℝⁿ
> Ejemplo: v(x,y,z) = (vₓ, vᵧ, vᵤ) velocidad en cada punto
> ```
> 
> **Importancia histórica:**
> 
> - **James Clerk Maxwell (1860s):** Teoría electromagnética usando campos
> - **Hermann von Helmholtz (1858):** Descomposición de campos vectoriales
> - **George Gabriel Stokes (1850s):** Teoremas fundamentales
> - **Leonhard Euler (1750s):** Ecuaciones de fluidos
> - **Carl Friedrich Gauss (1830s):** Teoría del potencial
> 
> **Aplicaciones modernas:**
> 
> - Simulación de fluidos (CFD)
> - Predicción meteorológica
> - Diseño electromagnético
> - Computación gráfica (physics engines)
> - Robótica y navegación

### 📐 Definición Formal

> [!note]- 🌟 Concepto Matemático **Definición:**
> 
> Un **campo vectorial** en ℝⁿ es una función vectorial que asigna a cada punto un vector:
> 
> **En ℝ²:** $$\mathbf{F}(x, y) = \langle P(x,y), Q(x,y) \rangle = P(x,y)\mathbf{i} + Q(x,y)\mathbf{j}$$
> 
> **En ℝ³:** $$\mathbf{F}(x, y, z) = \langle P(x,y,z), Q(x,y,z), R(x,y,z) \rangle$$ $$= P(x,y,z)\mathbf{i} + Q(x,y,z)\mathbf{j} + R(x,y,z)\mathbf{k}$$
> 
> **Componentes:**
> 
> - **P, Q, R:** Funciones escalares (componentes del campo)
> - Cada componente es una función de posición
> - Los vectores base **i**, **j**, **k** son constantes
> 
> **Notaciones equivalentes:**
> 
> ```
> F(x,y,z) = ⟨P, Q, R⟩
> F(x,y,z) = (P, Q, R)
> F = P i + Q j + R k
> F = [P, Q, R]ᵀ
> ```
> 
> **Dominio del campo:**
> 
> - **D ⊆ ℝⁿ:** Región donde el campo está definido
> - Puede ser todo el espacio o una región específica
> - Puntos donde alguna componente no está definida se excluyen
> 
> **Continuidad y diferenciabilidad:**
> 
> - **F es continuo** si P, Q, R son continuas
> - **F es diferenciable** si P, Q, R tienen derivadas parciales continuas
> - **Campo suave (smooth):** F es infinitamente diferenciable (C∞)

## 🎨 Representación Gráfica

### 📊 Visualización de Campos

> [!tip]- 👁️ Cómo "Ver" un Campo Vectorial **Métodos de visualización:**
> 
> **1. Flechas (vectores):** ➡️
> 
> - Dibujar vectores en una malla de puntos
> - Longitud = magnitud del campo
> - Dirección = dirección del campo
> - Limitación: muchos vectores crean confusión visual
> 
> **2. Líneas de flujo (streamlines):** 〰️
> 
> - Curvas tangentes al campo en cada punto
> - Siguen la dirección del campo
> - Densidad indica magnitud
> - Nunca se cruzan (excepto en puntos singulares)
> 
> **3. Código de colores:** 🎨
> 
> - Color indica magnitud
> - Flechas o campos graduados
> - Útil para campos 3D proyectados
> 
> **4. Animación de partículas:** 🌟
> 
> - Partículas siguen el campo
> - Muestra comportamiento dinámico
> - Ideal para fluidos
> 
> **Interpretación de gráficas:**
> 
> ```
> Flechas largas → campo fuerte
> Flechas cortas → campo débil
> Líneas cercanas → alta intensidad
> Líneas alejadas → baja intensidad
> Convergencia → sumidero (sink)
> Divergencia → fuente (source)
> Circulación → vórtice (vortex)
> ```
> 
> **Software recomendado:**
> 
> - **GeoGebra 3D:** Visualización interactiva
> - **Mathematica:** VectorPlot, VectorPlot3D
> - **Python:** matplotlib.quiver, plotly
> - **MATLAB:** quiver, quiver3, streamline

### 🖼️ Ejemplos Visuales de Campos

> [!example]- 🎯 Campos Básicos Representativos **Ejemplo 1: Campo radial (ℝ²)**
> 
> $$\mathbf{F}(x,y) = \langle x, y \rangle$$
> 
> ```
> Características:
> - Apunta hacia afuera desde el origen
> - Magnitud aumenta con la distancia: ||F|| = √(x² + y²)
> - Líneas de flujo: rayos desde el origen
> - Interpretación física: explosión, campo eléctrico de carga positiva
> 
> Puntos específicos:
> F(1, 0) = ⟨1, 0⟩ → hacia la derecha
> F(0, 1) = ⟨0, 1⟩ → hacia arriba
> F(1, 1) = ⟨1, 1⟩ → diagonal, ||F|| = √2
> F(-1, -1) = ⟨-1, -1⟩ → hacia tercer cuadrante
> ```
> 
> ---
> 
> **Ejemplo 2: Campo rotacional (ℝ²)**
> 
> $$\mathbf{F}(x,y) = \langle -y, x \rangle$$
> 
> ```
> Características:
> - Gira alrededor del origen (antihorario)
> - Magnitud constante en círculos: ||F|| = √(x² + y²)
> - Líneas de flujo: círculos concéntricos
> - Interpretación física: remolino, campo magnético
> 
> Puntos específicos:
> F(1, 0) = ⟨0, 1⟩ → hacia arriba
> F(0, 1) = ⟨-1, 0⟩ → hacia la izquierda
> F(1, 1) = ⟨-1, 1⟩ → perpendicular al radio
> 
> Propiedad: F ⊥ r (siempre perpendicular a la posición)
> ```
> 
> ---
> 
> **Ejemplo 3: Campo gravitacional (ℝ³)**
> 
> $$\mathbf{F}(x,y,z) = -\frac{GMm}{r^3}\langle x, y, z \rangle = -\frac{GMm}{(x^2+y^2+z^2)^{3/2}}\langle x, y, z \rangle$$
> 
> ```
> Características:
> - Apunta hacia el origen (atracción)
> - Magnitud decae con r²: ||F|| = GMm/r²
> - Líneas de flujo: rayos hacia el origen
> - Simetría esférica
> 
> Propiedades:
> - Conservativo: F = -∇φ donde φ = -GMm/r
> - Ley del inverso del cuadrado
> - Campo central (depende solo de r)
> ```
> 
> ---
> 
> **Ejemplo 4: Campo uniforme (ℝ³)**
> 
> $$\mathbf{F}(x,y,z) = \langle 1, 0, 0 \rangle$$
> 
> ```
> Características:
> - Constante en todo el espacio
> - Magnitud ||F|| = 1 en todos lados
> - Líneas de flujo: rectas paralelas al eje x
> - Interpretación: gravedad uniforme, campo eléctrico entre placas
> 
> Propiedades:
> - Conservativo
> - Divergencia cero: ∇·F = 0
> - Rotacional cero: ∇×F = 0
> ```
> 
> ---
> 
> **Ejemplo 5: Campo dipolar (ℝ²)**
> 
> $$\mathbf{F}(x,y) = \left\langle \frac{2xy}{(x^2+y^2)^2}, \frac{y^2-x^2}{(x^2+y^2)^2} \right\rangle$$
> 
> ```
> Características:
> - Fuente en un punto, sumidero en otro
> - Patrón de imán o dipolo eléctrico
> - Decae como 1/r³
> - Líneas de flujo curvas características
> ```

## 🔍 Tipos de Campos Vectoriales

### 🌀 Campos según su Comportamiento

> [!success]- 📋 Clasificación por Propiedades **1. Campos conservativos:** ⚡
> 
> $$\mathbf{F} = \nabla \phi$$
> 
> Existe función potencial φ tal que **F** es su gradiente.
> 
> **Características:**
> 
> - Rotacional nulo: ∇ × **F** = **0**
> - Trabajo independiente del camino
> - ∮ **F**·d**r** = 0 en curvas cerradas
> 
> **Ejemplos físicos:**
> 
> - Campo gravitacional
> - Campo eléctrico (electrostática)
> - Fuerza elástica
> 
> ---
> 
> **2. Campos solenoidales (incompresibles):** 💨
> 
> $$\nabla \cdot \mathbf{F} = 0$$
> 
> Divergencia nula, el campo no tiene fuentes ni sumideros.
> 
> **Características:**
> 
> - Flujo total nulo a través de superficies cerradas
> - "Lo que entra = lo que sale"
> - Existe potencial vectorial: **F** = ∇ × **A**
> 
> **Ejemplos físicos:**
> 
> - Fluidos incompresibles
> - Campo magnético (∇·**B** = 0 siempre)
> - Flujo estacionario
> 
> ---
> 
> **3. Campos irrotacionales:** 🔄
> 
> $$\nabla \times \mathbf{F} = \mathbf{0}$$
> 
> Rotacional nulo, sin circulación local.
> 
> **Características:**
> 
> - No hay "remolinos" microscópicos
> - Equivale a ser conservativo (en dominio simplemente conexo)
> - Circulación nula en curvas pequeñas
> 
> **Ejemplos físicos:**
> 
> - Flujo potencial (aerodinámica)
> - Campos conservativos
> 
> ---
> 
> **4. Campos radiales:** 📡
> 
> $$\mathbf{F}(x,y,z) = f(r)\mathbf{r}$$
> 
> donde r = ||(x,y,z)|| y **r** = (x,y,z).
> 
> **Características:**
> 
> - Dirección radial desde un punto (usualmente origen)
> - Magnitud depende solo de la distancia
> - Simetría esférica o cilíndrica
> 
> **Ejemplos físicos:**
> 
> - Campo gravitacional de masa puntual
> - Campo eléctrico de carga puntual
> - Flujo radial desde fuente
> 
> ---
> 
> **5. Campos uniformes:** ➡️
> 
> $$\mathbf{F}(x,y,z) = \mathbf{c}$$
> 
> donde **c** es un vector constante.
> 
> **Características:**
> 
> - Mismo vector en todo punto
> - ∇·**F** = 0 y ∇×**F** = **0**
> - Líneas de flujo paralelas
> 
> **Ejemplos físicos:**
> 
> - Gravedad cerca de la superficie terrestre
> - Campo eléctrico entre placas paralelas
> - Viento constante

### 🎭 Puntos Singulares y Críticos

> [!warning]- ⚠️ Comportamiento Especial **Definición:**
> 
> Un **punto singular** o **crítico** de **F** es un punto donde **F** = **0** o donde **F** no está definido.
> 
> **Tipos de puntos críticos en ℝ²:**
> 
> **1. Fuente (source):** 🌟
> 
> ```
> Los vectores apuntan hacia afuera
> Divergencia positiva: ∇·F > 0
> Ejemplo: F = ⟨x, y⟩ en el origen
> Interpretación: emanación de fluido
> ```
> 
> **2. Sumidero (sink):** 🕳️
> 
> ```
> Los vectores apuntan hacia adentro
> Divergencia negativa: ∇·F < 0
> Ejemplo: F = ⟨-x, -y⟩ en el origen
> Interpretación: absorción de fluido
> ```
> 
> **3. Punto silla (saddle):** 🐴
> 
> ```
> Vectores salen en unas direcciones, entran en otras
> Ni fuente ni sumidero
> Ejemplo: F = ⟨x, -y⟩ en el origen
> Interpretación: punto de equilibrio inestable
> ```
> 
> **4. Centro o vórtice:** 🌀
> 
> ```
> Vectores giran alrededor del punto
> Líneas de flujo son curvas cerradas
> Ejemplo: F = ⟨-y, x⟩ en el origen
> Interpretación: remolino, rotación pura
> ```
> 
> **5. Espiral:** 🌊
> 
> ```
> Combinación de rotación y atracción/repulsión
> Espiral hacia adentro (atractor) o afuera (repulsor)
> Ejemplo: F = ⟨-y-x, x-y⟩ en el origen
> ```
> 
> **Clasificación mediante autovalores:**
> 
> Para campo lineal **F** = A**x**, matriz A = [a b; c d]:
> 
> ```
> Traza: τ = a + d
> Determinante: Δ = ad - bc
> 
> Δ > 0, τ² < 4Δ → Centro/espiral
> Δ > 0, τ² > 4Δ, τ ≠ 0 → Nodo (fuente/sumidero)
> Δ < 0 → Punto silla
> Δ = 0 → Degenerado
> ```

## 🧮 Operadores Diferenciales

### ∇ Gradiente

> [!note]- 📈 Del Escalar al Vector **Definición:**
> 
> El **gradiente** de una función escalar f es un campo vectorial:
> 
> **En ℝ²:** $$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right\rangle$$
> 
> **En ℝ³:** $$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right\rangle$$
> 
> **Símbolo nabla:** ∇ = ⟨∂/∂x, ∂/∂y, ∂/∂z⟩
> 
> **Interpretaciones:**
> 
> **1. Dirección de máximo crecimiento:** ⬆️
> 
> - ∇f apunta en la dirección donde f crece más rápidamente
> - ||∇f|| es la tasa máxima de cambio
> 
> **2. Perpendicular a curvas de nivel:** ⊥
> 
> - ∇f es perpendicular a las curvas f(x,y) = c
> - En montañas: apunta en la dirección de máxima pendiente
> 
> **3. Negativo: descenso más rápido:** ⬇️
> 
> - -∇f apunta hacia donde f decrece más rápido
> - Usado en optimización (gradient descent)
> 
> **Propiedades:**
> 
> ```
> 1. Linealidad: ∇(af + bg) = a∇f + b∇g
> 2. Regla del producto: ∇(fg) = f∇g + g∇f
> 3. Regla de la cadena: ∇(f(g)) = f'(g)∇g
> 4. Si f = constante, entonces ∇f = 0
> ```
> 
> **Ejemplo detallado:**
> 
> $$f(x,y) = x^2 + y^2$$
> 
> ```
> ∂f/∂x = 2x
> ∂f/∂y = 2y
> 
> ∇f = ⟨2x, 2y⟩ = 2⟨x, y⟩
> 
> Interpretación:
> - Apunta radialmente hacia afuera
> - Perpendicular a círculos x² + y² = c
> - Magnitud ||∇f|| = 2√(x² + y²) aumenta con la distancia
> ```

### 🌊 Divergencia

> [!success]- 📤 Flujo Saliente **Definición:**
> 
> La **divergencia** de un campo vectorial **F** = ⟨P, Q, R⟩ es un campo escalar:
> 
> $$\nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$
> 
> **Notaciones:** div **F**, ∇·**F**
> 
> **Interpretaciones físicas:**
> 
> **1. Densidad de flujo saliente:** 💨
> 
> ```
> ∇·F > 0 → fuente neta (divergencia positiva)
> ∇·F < 0 → sumidero neto (convergencia)
> ∇·F = 0 → incompresible (solenoidal)
> ```
> 
> **2. Tasa de expansión:** 📈
> 
> - Mide cuánto "se expande" el campo en un punto
> - Cambio de volumen por unidad de volumen
> 
> **3. Balance de masa/energía:** ⚖️
> 
> - ∇·**F** = tasa de creación - tasa de destrucción
> - Ecuación de continuidad: ∂ρ/∂t + ∇·(ρ**v**) = 0
> 
> **Propiedades:**
> 
> ```
> 1. Linealidad: ∇·(aF + bG) = a(∇·F) + b(∇·G)
> 2. Regla del producto: ∇·(fF) = f(∇·F) + F·∇f
> 3. Divergencia de gradiente: ∇·(∇f) = ∇²f (Laplaciano)
> 4. Divergencia de rotacional: ∇·(∇×F) = 0 siempre
> ```
> 
> **Ejemplos:**
> 
> **Ejemplo 1: Campo radial**
> 
> ```
> F = ⟨x, y, z⟩
> 
> ∇·F = ∂x/∂x + ∂y/∂y + ∂z/∂z = 1 + 1 + 1 = 3
> 
> Divergencia constante positiva → expansión uniforme
> ```
> 
> **Ejemplo 2: Campo rotacional**
> 
> ```
> F = ⟨-y, x, 0⟩
> 
> ∇·F = ∂(-y)/∂x + ∂x/∂y + ∂0/∂z = 0 + 0 + 0 = 0
> 
> Divergencia nula → flujo incompresible
> ```
> 
> **Ejemplo 3: Campo inverso del cuadrado**
> 
> ```
> F = r/r³ = ⟨x, y, z⟩/(x²+y²+z²)^(3/2)
> 
> ∇·F = 0 (excepto en el origen)
> 
> Cumple ley de Gauss para campo central
> ```

### 🔄 Rotacional

> [!info]- 🌀 Circulación Local **Definición:**
> 
> El **rotacional** de un campo vectorial **F** = ⟨P, Q, R⟩ es un campo vectorial:
> 
> $$\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \ P & Q & R \end{vmatrix}$$
> 
> $$= \left\langle \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right\rangle$$
> 
> **Notaciones:** curl **F**, rot **F**, ∇×**F**
> 
> **En ℝ² (caso especial):**
> 
> Para **F** = ⟨P, Q, 0⟩: $$\nabla \times \mathbf{F} = \left\langle 0, 0, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right\rangle$$
> 
> Solo la componente k es no nula.
> 
> **Interpretaciones físicas:**
> 
> **1. Densidad de circulación:** 🌀
> 
> - Mide tendencia a rotar alrededor de un punto
> - ||∇×**F**|| es el doble de la velocidad angular local
> - Dirección: eje de rotación (regla de la mano derecha)
> 
> **2. Vorticidad en fluidos:** 💨
> 
> - **ω** = ∇×**v** es el vector vorticidad
> - ||**ω**|| mide intensidad del remolino
> - Flujo irrotacional: ∇×**v** = **0**
> 
> **3. Campo magnético inducido:** ⚡
> 
> - Ley de Ampère: ∇×**B** = μ₀**J** + μ₀ε₀∂**E**/∂t
> - Corriente crea campo magnético rotacional
> 
> **Propiedades:**
> 
> ```
> 1. Linealidad: ∇×(aF + bG) = a(∇×F) + b(∇×G)
> 2. Regla del producto: ∇×(fF) = f(∇×F) + (∇f)×F
> 3. Rotacional de gradiente: ∇×(∇f) = 0 siempre
> 4. Divergencia de rotacional: ∇·(∇×F) = 0 siempre
> 5. Rotacional del rotacional: ∇×(∇×F) = ∇(∇·F) - ∇²F
> ```
> 
> **Ejemplos:**
> 
> **Ejemplo 1: Campo rotacional puro**
> 
> ```
> F = ⟨-y, x, 0⟩
> 
> ∇×F = | i    j    k   |
>       | ∂/∂x ∂/∂y ∂/∂z |
>       | -y    x    0   |
> 
> = ⟨0, 0, ∂x/∂x - ∂(-y)/∂y⟩ = ⟨0, 0, 1 + 1⟩ = ⟨0, 0, 2⟩
> 
> Rotación constante antihoraria con velocidad angular 1
> ```
> 
> **Ejemplo 2: Campo conservativo**
> 
> ```
> F = ⟨2xy, x², 0⟩
> 
> ∇×F = ⟨0, 0, ∂(x²)/∂x - ∂(2xy)/∂y⟩
>     = ⟨0, 0, 2x - 2x⟩
>     = ⟨0, 0, 0⟩
> 
> Rotacional nulo → campo conservativo
> Existe φ tal que F = ∇φ, con φ = x²y
> ```
> 
> **Ejemplo 3: Campo magnético de alambre**
> 
> ```
> Corriente I en alambre infinito a lo largo del eje z
> 
> B = (μ₀I/2πr)⟨-y, x, 0⟩/r
> 
> donde r = √(x² + y²)
> 
> ∇×B = μ₀I δ(x,y) k̂  (distribución delta en el alambre)
> ```

### 📐 Laplaciano

> [!tip]- ∆ Operador de Segundo Orden **Definición:**
> 
> El **Laplaciano** es la divergencia del gradiente:
> 
> $$\nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$
> 
> **Notaciones:** ∆f, ∇²f, div(grad f)
> 
> **Interpretaciones:**
> 
> **1. Curvatura promedio:** 📊
> 
> - Mide cuánto difiere f de su promedio local
> - ∇²f > 0: f es menor que su promedio (curva hacia arriba)
> - ∇²f < 0: f es mayor que su promedio (curva hacia abajo)
> - ∇²f = 0: f es igual a su promedio (función armónica)
> 
> **2. Difusión:** 🌡️
> 
> - Ecuación del calor: ∂T/∂t = α∇²T
> - ∇²T mide el balance térmico local
> 
> **3. Ondas:** 🌊
> 
> - Ecuación de onda: ∂²ψ/∂t² = c²∇²ψ
> - Relaciona aceleración temporal con curvatura espacial
> 
> **Ecuaciones importantes:**
> 
> **Ecuación de Laplace:** ∇²φ = 0
> 
> ```
> Soluciones: funciones armónicas
> Aplicaciones: potencial electrostático, flujo estacionario
> Propiedad del valor medio
> ```
> 
> **Ecuación de Poisson:** ∇²φ = -ρ/ε₀
> 
> ```
> Relaciona potencial con densidad de carga
> Generalización de Laplace con término fuente
> ```
> 
> **Ejemplo:**
> 
> ```
> f(x,y,z) = x² + y² - 2z²
> 
> ∂²f/∂x² = 2
> ∂²f/∂y² = 2
> ∂²f/∂z² = -4
> 
> ∇²f = 2 + 2 - 4 = 0
> 
> f es función armónica (solución de ∇²f = 0)
> ```

## 🔗 Identidades Vectoriales

> [!note]- 🧮 Relaciones Fundamentales **Identidades básicas:**
> 
> 1. **Gradiente de producto:** $\nabla(fg) = f\nabla g + g\nabla f$
>     
> 2. **Divergencia de producto escalar-vector:** $\nabla \cdot (f\mathbf{F}) = f(\nabla \cdot \mathbf{F}) + \mathbf{F} \cdot \nabla f$
>     
> 3. **Rotacional de producto escalar-vector:** $\nabla \times (f\mathbf{F}) = f(\nabla \times \mathbf{F}) + (\nabla f) \times \mathbf{F}$
>     
> 4. **Divergencia de producto cruz:** $\nabla \cdot (\mathbf{F} \times \mathbf{G}) = \mathbf{G} \cdot (\nabla \times \mathbf{F}) - \mathbf{F} \cdot (\nabla \times \mathbf{G})$
>     
> 5. **Rotacional de gradiente (siempre cero):** $\nabla \times (\nabla f) = \mathbf{0}$
>     
> 6. **Divergencia de rotacional (siempre cero):** $\nabla \cdot (\nabla \times \mathbf{F}) = 0$
>     
> 7. **Rotacional del rotacional:** $\nabla \times (\nabla \times \mathbf{F}) = \nabla(\nabla \cdot \mathbf{F}) - \nabla^2\mathbf{F}$
>     
> 8. **Laplaciano de producto:** $\nabla^2(fg) = f\nabla^2 g + 2(\nabla f) \cdot (\nabla g) + g\nabla^2 f$
>     
> 
> **Identidades de composición:**
> 
> ```
> Campo F es conservativo ⟺ ∇×F = 0 (en dominio simplemente conexo)
> Campo F es solenoidal ⟺ ∇·F = 0
> 
> Si F = ∇φ (conservativo), entonces ∇×F = ∇×(∇φ) = 0 ✓
> Si F = ∇×A (solenoidal), entonces ∇·F = ∇·(∇×A) = 0 ✓
> ```
> 
> **Descomposición de Helmholtz:**
> 
> Todo campo vectorial suficientemente suave puede descomponerse:
> 
> $\mathbf{F} = -\nabla \phi + \nabla \times \mathbf{A}$
> 
> donde:
> 
> - φ: potencial escalar (parte conservativa)
> - **A**: potencial vectorial (parte solenoidal)

## 🌊 Líneas de Flujo y Trayectorias

### 〰️ Líneas de Campo

> [!success]- 🛤️ Curvas Tangentes al Campo **Definición:**
> 
> Una **línea de flujo** (streamline) de un campo **F** es una curva cuyo vector tangente en cada punto es paralelo a **F**.
> 
> **Ecuación diferencial:**
> 
> $\frac{d\mathbf{r}}{dt} = \mathbf{F}(\mathbf{r})$
> 
> **En componentes (ℝ²):** $\frac{dx}{dt} = P(x,y), \quad \frac{dy}{dt} = Q(x,y)$
> 
> **Forma implícita (ℝ²):** $\frac{dy}{dx} = \frac{Q(x,y)}{P(x,y)}$
> 
> **Propiedades:**
> 
> 1. **No se cruzan:** Dos líneas de flujo distintas nunca se intersectan (excepto en puntos singulares)
> 2. **Tangencia:** El campo es tangente a las líneas en cada punto
> 3. **Unicidad:** Por cada punto pasa una única línea de flujo
> 4. **Curvas cerradas:** Posibles solo si hay circulación
> 
> **Diferencia con trayectorias:**
> 
> ```
> Línea de flujo (streamline):
> - Fotografía instantánea del campo
> - Dirección del campo en cada punto
> - No depende del tiempo (campo estacionario)
> 
> Trayectoria (pathline):
> - Historia de una partícula específica
> - Camino real seguido en el tiempo
> - En campos estacionarios: coincide con línea de flujo
> - En campos no estacionarios: puede diferir
> ```
> 
> **Método de solución:**
> 
> **Paso 1:** Plantear ecuaciones diferenciales **Paso 2:** Resolver el sistema (separación de variables, integración) **Paso 3:** Obtener familia de curvas (con constante de integración)

### 📊 Ejemplos de Líneas de Flujo

> [!example]- 🎯 Cálculos Detallados **Ejemplo 1: Campo radial**
> 
> $\mathbf{F}(x,y) = \langle x, y \rangle$
> 
> ```
> Ecuación diferencial:
> dy/dx = y/x
> 
> Separar variables:
> dy/y = dx/x
> 
> Integrar:
> ln|y| = ln|x| + C
> ln|y/x| = C
> y/x = K  (donde K = e^C)
> 
> Solución: y = Kx
> 
> Líneas de flujo: rectas radiales desde el origen
> Familia de rectas con pendiente variable
> ```
> 
> ---
> 
> **Ejemplo 2: Campo rotacional**
> 
> $\mathbf{F}(x,y) = \langle -y, x \rangle$
> 
> ```
> Ecuación diferencial:
> dy/dx = x/(-y) = -x/y
> 
> Separar variables:
> y dy = -x dx
> 
> Integrar:
> y²/2 = -x²/2 + C
> x² + y² = K
> 
> Solución: círculos concéntricos
> Radio √K depende de la condición inicial
> ```
> 
> ---
> 
> **Ejemplo 3: Campo de punto silla**
> 
> $\mathbf{F}(x,y) = \langle x, -y \rangle$
> 
> ```
> Ecuación diferencial:
> dy/dx = -y/x
> 
> Separar variables:
> dy/y = -dx/x
> 
> Integrar:
> ln|y| = -ln|x| + C
> ln|xy| = C
> xy = K
> 
> Solución: hipérbolas xy = K
> Familia de hipérbolas con asíntotas en los ejes
> ```
> 
> ---
> 
> **Ejemplo 4: Campo lineal general**
> 
> $\mathbf{F}(x,y) = \langle ax + by, cx + dy \rangle$
> 
> ```
> Ecuación diferencial:
> dy/dx = (cx + dy)/(ax + by)
> 
> Solución general: depende de autovalores de matriz [a b; c d]
> 
> Casos:
> - Autovalores reales distintos → líneas rectas y curvas
> - Autovalores complejos → espirales
> - Autovalores repetidos → líneas rectas o curvas parabólicas
> ```
> 
> ---
> 
> **Ejemplo 5: Campo en ℝ³ - hélice**
> 
> $\mathbf{F}(x,y,z) = \langle -y, x, 1 \rangle$
> 
> ```
> Ecuaciones paramétricas:
> dx/dt = -y
> dy/dt = x
> dz/dt = 1
> 
> De las dos primeras: x² + y² = R² (constante)
> De la tercera: z = t + z₀
> 
> Solución: hélices cilíndricas
> x(t) = R cos(t + φ)
> y(t) = R sin(t + φ)
> z(t) = t + z₀
> ```

## 🎨 Diagramas de Fase

### 📈 Análisis Cualitativo

> [!tip]- 🔍 Retrato de Fase **Concepto:**
> 
> Un **diagrama de fase** es una representación gráfica del comportamiento de un sistema dinámico en el plano (o espacio) de estados.
> 
> **Elementos del diagrama:**
> 
> 1. **Puntos críticos:** Donde **F** = **0**
> 2. **Líneas de flujo:** Trayectorias del sistema
> 3. **Flechas de dirección:** Sentido del flujo
> 4. **Regiones:** Areas con comportamiento similar
> 
> **Análisis de estabilidad:**
> 
> **Punto crítico estable (atractor):** 🎯
> 
> ```
> Las trayectorias cercanas convergen al punto
> Pequeñas perturbaciones → regreso al equilibrio
> Ejemplo: sumidero, espiral atractora
> ```
> 
> **Punto crítico inestable (repulsor):** 💥
> 
> ```
> Las trayectorias cercanas divergen del punto
> Pequeñas perturbaciones → alejamiento del equilibrio
> Ejemplo: fuente, espiral repulsora, punto silla
> ```
> 
> **Punto crítico semi-estable:** ⚖️
> 
> ```
> Estable en algunas direcciones, inestable en otras
> Ejemplo: punto silla (estable en una dirección)
> ```
> 
> **Linearización cerca de puntos críticos:**
> 
> Para **F**(x₀) = **0**, expandir en serie de Taylor:
> 
> $\mathbf{F}(\mathbf{x}) \approx J(\mathbf{x}_0)(\mathbf{x} - \mathbf{x}_0)$
> 
> donde J es la matriz Jacobiana:
> 
> $J = \begin{bmatrix} \frac{\partial P}{\partial x} & \frac{\partial P}{\partial y} \ \frac{\partial Q}{\partial x} & \frac{\partial Q}{\partial y} \end{bmatrix}$
> 
> El comportamiento local depende de los autovalores de J.

## 💪 Ejercicios Integrales

> [!example]- 🎯 Problemas Resueltos Completos **Nivel 1 - Básico:** 🟢
> 
> **Ejercicio 1:** Dado **F**(x,y) = ⟨3x²y, x³ + y²⟩, calcular ∇·**F** y ∇×**F**.
> 
> ```
> Solución:
> 
> P = 3x²y,  Q = x³ + y²
> 
> Divergencia:
> ∇·F = ∂P/∂x + ∂Q/∂y
>     = ∂(3x²y)/∂x + ∂(x³ + y²)/∂y
>     = 6xy + 2y
>     = 2y(3x + 1)
> 
> Rotacional (componente z):
> (∇×F)_z = ∂Q/∂x - ∂P/∂y
>         = ∂(x³ + y²)/∂x - ∂(3x²y)/∂y
>         = 3x² - 3x²
>         = 0
> 
> Como (∇×F)_z = 0, el campo es conservativo en ℝ².
> ```
> 
> ---
> 
> **Ejercicio 2:** Verificar si **F**(x,y,z) = ⟨2x, 2y, 2z⟩ es solenoidal.
> 
> ```
> Solución:
> 
> ∇·F = ∂(2x)/∂x + ∂(2y)/∂y + ∂(2z)/∂z
>     = 2 + 2 + 2
>     = 6
> 
> Como ∇·F ≠ 0, el campo NO es solenoidal.
> 
> Interpretación física:
> Campo radial con expansión uniforme (fuente).
> ```
> 
> ---
> 
> **Nivel 2 - Intermedio:** 🟡
> 
> **Ejercicio 3:** Encontrar las líneas de flujo de **F**(x,y) = ⟨x + y, x - y⟩.
> 
> ```
> Solución:
> 
> Ecuación diferencial:
> dy/dx = (x - y)/(x + y)
> 
> Esta es una ecuación homogénea. Sustitución: y = vx
> 
> dy/dx = v + x(dv/dx)
> 
> v + x(dv/dx) = (x - vx)/(x + vx) = (1 - v)/(1 + v)
> 
> x(dv/dx) = (1 - v)/(1 + v) - v
>          = (1 - v - v - v²)/(1 + v)
>          = (1 - 2v - v²)/(1 + v)
> 
> Separar variables:
> (1 + v)dv/(1 - 2v - v²) = dx/x
> 
> Integrar (completando cuadrado en denominador):
> -(1/2)ln|v² + 2v - 1| + (1/√2)arctan((v+1)/√2) = ln|x| + C
> 
> Solución implícita complicada.
> 
> Método alternativo - autovalores:
> Matriz del sistema: A = [1  1]
>                         [1 -1]
> 
> Autovalores: λ = ±√2
> Autovectores correspondientes dan direcciones principales.
> ```
> 
> ---
> 
> **Ejercicio 4:** Para **F**(x,y,z) = ⟨yz, xz, xy⟩, verificar que ∇·(∇×**F**) = 0.
> 
> ```
> Solución:
> 
> Paso 1: Calcular ∇×F
> 
> ∇×F = | i    j    k   |
>       | ∂/∂x ∂/∂y ∂/∂z |
>       | yz   xz   xy  |
> 
> = i(∂(xy)/∂y - ∂(xz)/∂z) - j(∂(xy)/∂x - ∂(yz)/∂z) + k(∂(xz)/∂x - ∂(yz)/∂y)
> = i(x - x) - j(y - y) + k(z - z)
> = ⟨0, 0, 0⟩
> 
> Paso 2: Calcular ∇·(∇×F)
> 
> ∇·(∇×F) = ∇·⟨0, 0, 0⟩ = 0 ✓
> 
> Esto verifica la identidad general: ∇·(∇×F) = 0 siempre.
> ```
> 
> ---
> 
> **Nivel 3 - Avanzado:** 🔴
> 
> **Ejercicio 5:** Encontrar el potencial escalar φ para **F** = ⟨2xy + z², x² - 3z, 2xz - 3y⟩ y verificar que es conservativo.
> 
> ```
> Solución:
> 
> Paso 1: Verificar que ∇×F = 0
> 
> ∇×F = | i    j    k   |
>       | ∂/∂x ∂/∂y ∂/∂z |
>       | 2xy+z² x²-3z 2xz-3y |
> 
> Componente i: ∂(2xz-3y)/∂y - ∂(x²-3z)/∂z = -3 - (-3) = 0 ✓
> Componente j: ∂(2xy+z²)/∂z - ∂(2xz-3y)/∂x = 2z - 2z = 0 ✓
> Componente k: ∂(x²-3z)/∂x - ∂(2xy+z²)/∂y = 2x - 2x = 0 ✓
> 
> Campo es conservativo ✓
> 
> Paso 2: Encontrar φ tal que ∇φ = F
> 
> ∂φ/∂x = 2xy + z²
> Integrar respecto a x:
> φ = x²y + xz² + g(y,z)
> 
> ∂φ/∂y = x² + ∂g/∂y = x² - 3z
> ∂g/∂y = -3z
> g(y,z) = -3yz + h(z)
> 
> φ = x²y + xz² - 3yz + h(z)
> 
> ∂φ/∂z = 2xz - 3y + h'(z) = 2xz - 3y
> h'(z) = 0  →  h(z) = C
> 
> Solución:
> φ(x,y,z) = x²y + xz² - 3yz + C
> 
> Verificación:
> ∇φ = ⟨2xy + z², x² - 3z, 2xz - 3y⟩ = F ✓
> ```
> 
> ---
> 
> **Ejercicio 6 - Aplicación:** Un campo de velocidad de fluido incompresible en 2D es **v** = ⟨-y/(x²+y²), x/(x²+y²)⟩. Verificar que es solenoidal, calcular su rotacional, y encontrar las líneas de flujo.
> 
> ```
> Solución:
> 
> Parte 1: Verificar incompresibilidad (∇·v = 0)
> 
> P = -y/(x²+y²),  Q = x/(x²+y²)
> 
> ∂P/∂x = -y·(-2x)/(x²+y²)² = 2xy/(x²+y²)²
> ∂Q/∂y = x·(-2y)/(x²+y²)² = -2xy/(x²+y²)²
> 
> ∇·v = ∂P/∂x + ∂Q/∂y
>     = 2xy/(x²+y²)² - 2xy/(x²+y²)²
>     = 0 ✓
> 
> El fluido es incompresible.
> 
> Parte 2: Calcular rotacional
> 
> (∇×v)_z = ∂Q/∂x - ∂P/∂y
> 
> ∂Q/∂x = [(x²+y²) - x·2x]/(x²+y²)² = (y² - x²)/(x²+y²)²
> ∂P/∂y = [-(x²+y²) - (-y)·2y]/(x²+y²)² = -(x² - y²)/(x²+y²)² = (y² - x²)/(x²+y²)²
> 
> (∇×v)_z = (y² - x²)/(x²+y²)² - (y² - x²)/(x²+y²)² = 0
> 
> ¡Cuidado! Este cálculo sugiere rotacional cero, pero...
> 
> Usando coordenadas polares: v = (1/r)⟨-sin θ, cos θ⟩ = (1/r)θ̂
> 
> Circulación alrededor del origen:
> Γ = ∮ v·dr = ∫₀²π (1/r)r dθ = 2π ≠ 0
> 
> Paradoja: El campo es irrotacional excepto en el origen.
> Rotacional = 2πδ(x,y) (distribución delta en origen)
> 
> Parte 3: Líneas de flujo
> 
> dy/dx = Q/P = x/(x²+y²) / [-y/(x²+y²)] = -x/y
> 
> y dy = -x dx
> 
> Integrar:
> y²/2 = -x²/2 + C
> x² + y² = K
> 
> Líneas de flujo: círculos concéntricos alrededor del origen
> 
> Interpretación física:
> Vórtice puntual en el origen (como remolino de agua yéndose por desagüe)
> ```

## 📖 Referencias Conceptuales

> [!quote]- 🌟 Enlaces con Otras Notas
> 
> **Fundamentos previos:**
> 
> - [[01 - Sistema de Referencia Espacial]] - Coordenadas en ℝ² y ℝ³
> - [[02 - Vectores en R3]] - Operaciones vectoriales básicas
> - [[Derivadas Parciales]] - Base del cálculo vectorial
> - [[Funciones de Varias Variables]] - Dominio y continuidad
> 
> **Operadores relacionados:**
> 
> - [[Gradiente]] - Del campo escalar al vectorial
> - [[Divergencia]] - Medida de flujo saliente
> - [[Rotacional]] - Medida de circulación
> - [[Laplaciano]] - Operador de difusión
> 
> **Teoremas fundamentales:**
> 
> - [[Teorema Fundamental para Integrales de Línea]] - Campos conservativos
> - [[Teorema de Green]] - Relación circulación-divergencia (2D)
> - [[Teorema de Stokes]] - Circulación y rotacional (3D)
> - [[Teorema de la Divergencia (Gauss)]] - Flujo a través de superficies
> - [[Descomposición de Helmholtz]] - Parte conservativa y solenoidal
> 
> **Temas relacionados:**
> 
> - [[03 - Parametrización de Curvas]] - Líneas de flujo
> - [[04 - Interpretaciones Geométricas y Físicas]] - Trabajo y flujo
> - [[Integrales de Línea]] - Circulación y trabajo
> - [[Integrales de Superficie]] - Flujo a través de superficies
> 
> **Aplicaciones físicas:**
> 
> - [[Ecuaciones de Maxwell]] - Electromagnetismo
> - [[Ecuaciones de Navier-Stokes]] - Mecánica de fluidos
> - [[Ecuación del Calor]] - Difusión térmica
> - [[Ecuación de Onda]] - Propagación
> - [[Mecánica Clásica]] - Campos de fuerza
> 
> **Análisis cualitativo:**
> 
> - [[Sistemas Dinámicos]] - Diagramas de fase
> - [[Teoría de Estabilidad]] - Puntos críticos
> - [[Ecuaciones Diferenciales]] - Líneas de flujo
> - [[Análisis Numérico]] - Métodos computacionales
> 
> **Temas avanzados:**
> 
> - [[Formas Diferenciales]] - Formalismo abstracto
> - [[Geometría Diferencial]] - Variedades y tensores
> - [[Topología]] - Propiedades globales
> - [[Teoría de Campos]] - Física teórica
> - [[Análisis Funcional]] - Espacios de campos

---

**Tags:** #campos-vectoriales #cálculo-vectorial #gradiente #divergencia #rotacional #laplaciano #campos-conservativos #campos-solenoidales #líneas-de-flujo #operadores-diferenciales #electromagnetismo #mecánica-de-fluidos #ecuaciones-de-maxwell #navier-stokes #sistemas-dinámicos #puntos-críticos #diagramas-de-fase #identidades-vectoriales #university #matemáticas #física
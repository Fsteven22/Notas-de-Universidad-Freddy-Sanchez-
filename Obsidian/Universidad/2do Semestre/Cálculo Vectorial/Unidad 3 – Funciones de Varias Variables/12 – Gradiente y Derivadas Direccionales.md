# 📘 Gradiente y Derivadas Direccionales

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes el Gradiente y las Derivadas Direccionales?
> 
> El gradiente y las derivadas direccionales extienden el concepto de derivada para medir **tasas de cambio en cualquier dirección**, no solo en las direcciones de los ejes coordenados.
> 
> **Motivación:**
> 
> - Derivadas parciales: miden cambio solo en direcciones $x$ e $y$
> - En la realidad: necesitamos conocer el cambio en **cualquier dirección**
> - Solución: **derivadas direccionales** y el **vector gradiente**
> 
> **Pregunta fundamental:**
> 
> Si estás en una montaña en el punto $(x_0, y_0)$, ¿en qué dirección deberías caminar para:
> 
> - ¿Subir más rápido? → Dirección del gradiente
> - ¿Bajar más rápido? → Dirección opuesta al gradiente
> - ¿Mantener la altura? → Perpendicular al gradiente
> 
> **Aplicaciones prácticas:**
> 
> - **Física:** Campos vectoriales, flujo de calor, campo eléctrico
> - **Optimización:** Gradiente descendente, algoritmos de búsqueda
> - **Machine Learning:** Backpropagation, entrenamiento de redes neuronales
> - **Meteorología:** Dirección de máximo cambio de temperatura/presión
> - **Visión por computadora:** Detección de bordes, análisis de imágenes
> - **Economía:** Dirección de máxima ganancia/pérdida

---

## 🧭 Derivadas Direccionales

### 📋 Definición Formal

> [!example]- 🟢 Definición: Derivada Direccional
> 
> **Definición:** Sea $f: \mathbb{R}^2 \to \mathbb{R}$ y $\mathbf{u} = (u_1, u_2)$ un **vector unitario** ($|\mathbf{u}| = 1$). La **derivada direccional** de $f$ en el punto $(x_0, y_0)$ en la dirección $\mathbf{u}$ es:
> 
> $$D_{\mathbf{u}}f(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + hu_1, y_0 + hu_2) - f(x_0, y_0)}{h}$$
> 
> **siempre que este límite exista.**
> 
> ---
> 
> **Interpretación:**
> 
> - Mide la **tasa de cambio instantánea** de $f$ al moverse desde $(x_0, y_0)$ en la dirección $\mathbf{u}$
> - Es la pendiente de la curva obtenida al cortar la superficie $z = f(x,y)$ con un plano vertical en dirección $\mathbf{u}$
> - Generaliza las derivadas parciales:
>     - $D_{(1,0)}f = f_x$ (dirección del eje $x$)
>     - $D_{(0,1)}f = f_y$ (dirección del eje $y$)
> 
> ---
> 
> **Notaciones equivalentes:**
> 
> $$D_{\mathbf{u}}f = \frac{\partial f}{\partial \mathbf{u}} = \nabla_{\mathbf{u}}f$$
> 
> ---
> 
> **IMPORTANTE:** $\mathbf{u}$ debe ser un **vector unitario**. Si tienes un vector $\mathbf{v}$ no unitario, primero normalízalo:
> 
> $$\mathbf{u} = \frac{\mathbf{v}}{|\mathbf{v}|}$$

### 🎨 Visualización Geométrica

> [!note]- 🖼️ Interpretación Gráfica
> 
> ### Superficie y Dirección
> 
> Para $z = f(x,y)$, la derivada direccional en dirección $\mathbf{u}$:
> 
> ```
>           z
>           |
>           |      /|\  Superficie
>           |     / | \
>           |    /  |  \
>           |   /   •P  \
>           |  /   /|    \
>           | /   / |     \
>           |/___/  |      \
>           +---→---+------- y
>          /    u⃗   |
>         x         |
>                (x₀,y₀)
> ```
> 
> ---
> 
> ### Corte Vertical
> 
> Imagina cortar la superficie con un plano vertical que:
> 
> - Pasa por el punto $(x_0, y_0, f(x_0, y_0))$
> - Es perpendicular al plano $xy$
> - Apunta en dirección $\mathbf{u}$
> 
> ```
>         z
>         |
>         |    /
>         |   /  ← Pendiente = D_u f
>         |  /
>         | •
>         |/
>         +-------- dirección u⃗
> ```
> 
> La derivada direccional es la **pendiente** de esta curva de intersección.
> 
> ---
> 
> ### Comparación con Derivadas Parciales
> 
> ```
> Vista superior (plano xy):
> 
>         y
>         ↑
>         |
>     •---|---  Direcciones especiales:
>    /    |      • Eje x: f_x
>   u⃗    |      • Eje y: f_y
>  /     |      • Cualquier u⃗: D_u f
> +------→------ x
> ```

---

## ∇ El Vector Gradiente

### 📐 Definición del Gradiente

> [!example]- 🟡 Definición: Gradiente
> 
> **Definición:** El **gradiente** de $f$ en el punto $(x, y)$ es el vector:
> 
> $$\nabla f(x, y) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right) = (f_x, f_y)$$
> 
> ---
> 
> **Notaciones equivalentes:**
> 
> $$\nabla f = \text{grad } f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$
> 
> El símbolo $\nabla$ se llama **"nabla"** o **"del"**.
> 
> ---
> 
> **En tres variables:**
> 
> $$\nabla f(x, y, z) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right) = (f_x, f_y, f_z)$$
> 
> ---
> 
> **En $n$ variables:**
> 
> $$\nabla f(\mathbf{x}) = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n}\right)$$
> 
> ---
> 
> **Propiedades del operador $\nabla$:**
> 
> El gradiente es un **operador vectorial** que transforma:
> 
> - Una función escalar $f: \mathbb{R}^n \to \mathbb{R}$
> - En un campo vectorial $\nabla f: \mathbb{R}^n \to \mathbb{R}^n$

### 🔗 Teorema Fundamental: Gradiente y Derivada Direccional

> [!note]- 🎯 Teorema: Fórmula de la Derivada Direccional
> 
> **Teorema:** Si $f$ es **diferenciable** en $(x_0, y_0)$, entonces la derivada direccional en cualquier dirección $\mathbf{u}$ (con $|\mathbf{u}| = 1$) existe y está dada por:
> 
> $$D_{\mathbf{u}}f(x_0, y_0) = \nabla f(x_0, y_0) \cdot \mathbf{u}$$
> 
> donde $\cdot$ denota el **producto punto** (producto escalar).
> 
> ---
> 
> **En componentes:**
> 
> Si $\mathbf{u} = (u_1, u_2)$ y $\nabla f = (f_x, f_y)$:
> 
> $$D_{\mathbf{u}}f = f_x u_1 + f_y u_2$$
> 
> ---
> 
> **Interpretación:**
> 
> - El gradiente **contiene toda la información** sobre las derivadas direccionales
> - Para calcular $D_{\mathbf{u}}f$, basta calcular el producto punto $\nabla f \cdot \mathbf{u}$
> - Las derivadas parciales son casos especiales del producto punto
> 
> ---
> 
> **Verificación para derivadas parciales:**
> 
> - En dirección $x$: $\mathbf{u} = (1, 0)$ $$D_{(1,0)}f = (f_x, f_y) \cdot (1, 0) = f_x$$ ✓
>     
> - En dirección $y$: $\mathbf{u} = (0, 1)$ $$D_{(0,1)}f = (f_x, f_y) \cdot (0, 1) = f_y$$ ✓
>     

---

## 📊 Propiedades del Gradiente

### 🌟 Propiedad 1: Dirección de Máximo Crecimiento

> [!note]- 🔺 El Gradiente Apunta Hacia Arriba
> 
> **Teorema:** El gradiente $\nabla f(x_0, y_0)$ apunta en la dirección de **máximo crecimiento** de $f$ en el punto $(x_0, y_0)$.
> 
> ---
> 
> ### Demostración
> 
> Sabemos que:
> 
> $$D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u} = |\nabla f| |\mathbf{u}| \cos\theta$$
> 
> donde $\theta$ es el ángulo entre $\nabla f$ y $\mathbf{u}$.
> 
> Como $|\mathbf{u}| = 1$:
> 
> $$D_{\mathbf{u}}f = |\nabla f| \cos\theta$$
> 
> **Máximo:** cuando $\cos\theta = 1$ → $\theta = 0$ → $\mathbf{u}$ paralelo a $\nabla f$
> 
> $$\max_{\mathbf{u}} D_{\mathbf{u}}f = |\nabla f|$$
> 
> **Alcanzado cuando:** $\mathbf{u} = \frac{\nabla f}{|\nabla f|}$
> 
> ---
> 
> ### Consecuencias importantes
> 
> ✅ **Máximo crecimiento:** En dirección de $\nabla f$, con tasa $|\nabla f|$
> 
> ✅ **Máximo decrecimiento:** En dirección de $-\nabla f$, con tasa $-|\nabla f|$
> 
> ✅ **Sin cambio:** Perpendicular a $\nabla f$ (cuando $\theta = 90°$, $\cos\theta = 0$)

### 🌟 Propiedad 2: Perpendicular a Curvas de Nivel

> [!note]- 🗺️ Gradiente y Curvas de Nivel
> 
> **Teorema:** El gradiente $\nabla f(x_0, y_0)$ es **perpendicular** a la curva de nivel de $f$ que pasa por $(x_0, y_0)$.
> 
> ---
> 
> ### Curvas de nivel
> 
> Una **curva de nivel** es el conjunto de puntos donde $f$ tiene un valor constante:
> 
> $$C_c = {(x, y) : f(x, y) = c}$$
> 
> ---
> 
> ### Visualización
> 
> ```
> Vista superior (mapa topográfico):
> 
>         y
>         |
>         |  f = 30
>         | /
>         |/  f = 20
>    ∇f → •  
>        /|\ f = 10
>       / | \
>      /  |  \
>     +---+---+--- x
> ```
> 
> El gradiente es perpendicular a las curvas de nivel.
> 
> ---
> 
> ### Demostración (intuición)
> 
> Si te mueves **a lo largo** de una curva de nivel:
> 
> - $f$ no cambia (permanece constante)
> - Por lo tanto, $D_{\mathbf{u}}f = 0$ en esa dirección
> - Como $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u} = 0$
> - Entonces $\nabla f \perp \mathbf{u}$
> 
> El gradiente es perpendicular a la dirección tangente de la curva de nivel.
> 
> ---
> 
> ### Aplicación práctica
> 
> **Mapas topográficos:**
> 
> - Líneas de contorno = curvas de nivel (altura constante)
> - El gradiente apunta "cuesta arriba", perpendicular a las curvas
> - Donde las curvas están más juntas, $|\nabla f|$ es mayor (pendiente pronunciada)

### 🌟 Propiedad 3: Magnitud del Gradiente

> [!note]- 📏 La Norma del Gradiente
> 
> **Interpretación:** La magnitud $|\nabla f|$ mide:
> 
> 1. La **tasa máxima de cambio** de $f$ en el punto
> 2. La "**pendiente**" más pronunciada de la superficie
> 3. Qué tan "empinada" está la función
> 
> ---
> 
> ### Fórmula
> 
> $$|\nabla f| = \sqrt{f_x^2 + f_y^2}$$
> 
> ---
> 
> ### Casos especiales
> 
> ✅ **$|\nabla f| = 0$:**
> 
> - El punto es **crítico** (posible máximo, mínimo o punto silla)
> - La superficie es "plana" localmente
> - No hay dirección de máximo crecimiento
> 
> ✅ **$|\nabla f|$ grande:**
> 
> - Cambio rápido de $f$
> - Superficie muy inclinada
> - Curvas de nivel muy juntas
> 
> ✅ **$|\nabla f|$ pequeño:**
> 
> - Cambio lento de $f$
> - Superficie casi plana
> - Curvas de nivel separadas

---

## 📝 Ejemplos Básicos

### Ejemplo 1: Cálculo del Gradiente

> [!example]- 📐 Ejemplo 1: Función Polinomial
> 
> **Función:** $$f(x,y) = x^2 + 2xy + y^2$$
> 
> ---
> 
> **Paso 1: Calcular derivadas parciales**
> 
> $$f_x = 2x + 2y$$ $$f_y = 2x + 2y$$
> 
> ---
> 
> **Paso 2: Formar el gradiente**
> 
> $$\boxed{\nabla f(x,y) = (2x + 2y, 2x + 2y) = 2(x+y)(1, 1)}$$
> 
> ---
> 
> **Paso 3: Evaluar en un punto**
> 
> En $(1, 2)$:
> 
> $$\nabla f(1, 2) = (2(1) + 2(2), 2(1) + 2(2)) = (6, 6)$$
> 
> ---
> 
> **Interpretación:**
> 
> - En $(1, 2)$, la dirección de máximo crecimiento es $(6, 6)$ o normalizando: $\frac{1}{\sqrt{2}}(1, 1)$
> - La tasa máxima de cambio es $|\nabla f| = \sqrt{36 + 36} = 6\sqrt{2} \approx 8.49$

### Ejemplo 2: Derivada Direccional

> [!example]- 📐 Ejemplo 2: Calcular Derivada Direccional
> 
> **Función:** $f(x,y) = x^2 + y^2$
> 
> **Punto:** $(3, 4)$
> 
> **Dirección:** $\mathbf{v} = (1, 2)$ (no unitario)
> 
> ---
> 
> **Paso 1: Calcular gradiente**
> 
> $$\nabla f = (2x, 2y)$$
> 
> En $(3, 4)$:
> 
> $$\nabla f(3, 4) = (6, 8)$$
> 
> ---
> 
> **Paso 2: Normalizar el vector dirección**
> 
> $$|\mathbf{v}| = \sqrt{1^2 + 2^2} = \sqrt{5}$$
> 
> $$\mathbf{u} = \frac{\mathbf{v}}{|\mathbf{v}|} = \frac{(1, 2)}{\sqrt{5}} = \left(\frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}}\right)$$
> 
> ---
> 
> **Paso 3: Calcular derivada direccional**
> 
> $$D_{\mathbf{u}}f(3, 4) = \nabla f(3, 4) \cdot \mathbf{u}$$
> 
> $$= (6, 8) \cdot \left(\frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}}\right)$$
> 
> $$= 6 \cdot \frac{1}{\sqrt{5}} + 8 \cdot \frac{2}{\sqrt{5}}$$
> 
> $$= \frac{6 + 16}{\sqrt{5}} = \frac{22}{\sqrt{5}} = \frac{22\sqrt{5}}{5} \approx 9.85$$
> 
> $$\boxed{D_{\mathbf{u}}f(3, 4) = \frac{22}{\sqrt{5}}}$$
> 
> ---
> 
> **Interpretación:**
> 
> - Al moverse desde $(3, 4)$ en dirección $(1, 2)$, $f$ aumenta a razón de $\approx 9.85$ unidades por unidad de distancia

### Ejemplo 3: Dirección de Máximo Crecimiento

> [!example]- 📐 Ejemplo 3: Máximo Ascenso
> 
> **Función (temperatura):** $T(x,y) = 100 - x^2 - 2y^2$
> 
> **Punto:** $(1, 1)$
> 
> **Preguntas:** a) ¿En qué dirección aumenta más rápido la temperatura? b) ¿Cuál es la tasa máxima de aumento? c) ¿En qué dirección no cambia la temperatura?
> 
> ---
> 
> **Solución:**
> 
> **Gradiente:**
> 
> $$\nabla T = (-2x, -4y)$$
> 
> En $(1, 1)$:
> 
> $$\nabla T(1, 1) = (-2, -4)$$
> 
> ---
> 
> **a) Dirección de máximo crecimiento:**
> 
> Es la dirección del gradiente: $(-2, -4)$
> 
> Normalizado:
> 
> $$\mathbf{u}_{\max} = \frac{(-2, -4)}{\sqrt{4 + 16}} = \frac{(-2, -4)}{\sqrt{20}} = \frac{1}{\sqrt{5}}(-1, -2)$$
> 
> $$\boxed{\text{Dirección: } (-1, -2) \text{ (o hacia el suroeste)}}$$
> 
> ---
> 
> **b) Tasa máxima de aumento:**
> 
> $$|\nabla T(1, 1)| = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5} \approx 4.47 \text{ °C/unidad}$$
> 
> $$\boxed{\text{Tasa máxima: } 2\sqrt{5} \approx 4.47 \text{ °C/unidad}}$$
> 
> ---
> 
> **c) Dirección sin cambio:**
> 
> Perpendicular al gradiente $(-2, -4)$.
> 
> Un vector perpendicular es $(4, -2)$ o $(-4, 2)$ (intercambiar componentes y cambiar signo de una).
> 
> Normalizado: $\mathbf{u}_{\perp} = \frac{1}{\sqrt{20}}(2, -1)$
> 
> $$\boxed{\text{Direcciones: } (2, -1) \text{ o } (-2, 1)}$$
> 
> Estas son las direcciones **tangentes a las curvas de nivel**.

### Ejemplo 4: Función Exponencial

> [!example]- 📐 Ejemplo 4: Gradiente de Exponencial
> 
> **Función:** $f(x,y) = e^{x^2+y^2}$
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$f_x = e^{x^2+y^2} \cdot 2x = 2xe^{x^2+y^2}$$
> 
> $$f_y = e^{x^2+y^2} \cdot 2y = 2ye^{x^2+y^2}$$
> 
> ---
> 
> **Gradiente:**
> 
> $$\boxed{\nabla f(x,y) = 2e^{x^2+y^2}(x, y)}$$
> 
> ---
> 
> **En el origen $(0, 0)$:**
> 
> $$\nabla f(0, 0) = 2e^0(0, 0) = (0, 0)$$
> 
> **Interpretación:** El origen es un **punto crítico** (de hecho, es un mínimo).
> 
> ---
> 
> **En $(1, 0)$:**
> 
> $$\nabla f(1, 0) = 2e^1(1, 0) = (2e, 0)$$
> 
> La función crece más rápido en la dirección positiva del eje $x$.

### Ejemplo 5: Función Logarítmica

> [!example]- 📐 Ejemplo 5: Gradiente de Logaritmo
> 
> **Función:** $f(x,y) = \ln(x^2 + y^2)$ para $(x,y) \neq (0, 0)$
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$f_x = \frac{1}{x^2 + y^2} \cdot 2x = \frac{2x}{x^2 + y^2}$$
> 
> $$f_y = \frac{1}{x^2 + y^2} \cdot 2y = \frac{2y}{x^2 + y^2}$$
> 
> ---
> 
> **Gradiente:**
> 
> $$\nabla f(x,y) = \frac{2}{x^2 + y^2}(x, y) = \frac{2\mathbf{r}}{r^2}$$
> 
> donde $\mathbf{r} = (x, y)$ y $r = |\mathbf{r}| = \sqrt{x^2 + y^2}$
> 
> $$\boxed{\nabla f(x,y) = \frac{2}{r}\hat{\mathbf{r}}}$$
> 
> donde $\hat{\mathbf{r}} = \frac{\mathbf{r}}{r}$ es el vector unitario radial.
> 
> ---
> 
> **Interpretación:**
> 
> - El gradiente apunta radialmente hacia afuera desde el origen
> - Su magnitud decrece como $1/r$
> - Es perpendicular a los círculos $x^2 + y^2 = c$ (curvas de nivel)

---

## 🔬 Ejemplos Avanzados

### Ejemplo 6: Optimización - Ascenso más Rápido

> [!example]- 📐 Ejemplo 6: Escalador en Montaña
> 
> **Situación:** Un escalador está en el punto $(1, 2)$ de una montaña con elevación:
> 
> $$h(x,y) = 10 - x^2 - y^2$$
> 
> **Preguntas:** a) ¿En qué dirección debe caminar para subir más rápido? b) Si camina 0.1 km en esa dirección, ¿cuánto sube aproximadamente? c) ¿En qué dirección debe caminar para mantener la altitud?
> 
> ---
> 
> **Solución:**
> 
> **Gradiente:**
> 
> $$\nabla h = (-2x, -2y)$$
> 
> En $(1, 2)$:
> 
> $$\nabla h(1, 2) = (-2, -4)$$
> 
> ---
> 
> **a) Dirección de máximo ascenso:**
> 
> $$\mathbf{d} = \nabla h(1, 2) = (-2, -4)$$
> 
> Normalizado:
> 
> $$\mathbf{u} = \frac{(-2, -4)}{\sqrt{20}} = \frac{(-1, -2)}{\sqrt{5}}$$
> 
> $$\boxed{\text{Dirección: hacia } (-1, -2) \text{ (suroeste)}}$$
> 
> ---
> 
> **b) Cambio en altitud:**
> 
> Tasa de cambio: $|\nabla h(1, 2)| = \sqrt{20} = 2\sqrt{5}$
> 
> Cambio aproximado:
> 
> $$\Delta h \approx |\nabla h| \cdot \Delta s = 2\sqrt{5} \cdot 0.1 \approx 0.447 \text{ km} = 447 \text{ m}$$
> 
> $$\boxed{\text{Sube aproximadamente 447 metros}}$$
> 
> ---
> 
> **c) Dirección para mantener altitud:**
> 
> Perpendicular al gradiente $(-2, -4)$:
> 
> $$\mathbf{v} = (4, -2) \text{ o } (-4, 2)$$
> 
> Normalizado: $\mathbf{u}_{\perp} = \frac{1}{\sqrt{20}}(2, -1)$
> 
> $$\boxed{\text{Direcciones: } (2, -1) \text{ o } (-2, 1)}$$

### Ejemplo 7: Física - Campo Eléctrico

> [!example]- ⚡ Ejemplo 7: Potencial Eléctrico
> 
> **Potencial eléctrico:**
> 
> $$V(x,y) = \frac{k}{\ sqrt{x^2 + y^2}}$$
> 
> donde $k$ es una constante.
> 
> El **campo eléctrico** es $\mathbf{E} = -\nabla V$.
> 
> ---
> 
> **Calcular el campo eléctrico:**
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial V}{\partial x} = k \cdot \left(-\frac{1}{2}\right)(x^2+y^2)^{-3/2} \cdot 2x = -\frac{kx}{(x^2+y^2)^{3/2}}$$
> 
> $$\frac{\partial V}{\partial y} = -\frac{ky}{(x^2+y^2)^{3/2}}$$
> 
> ---
> 
> **Gradiente:**
> 
> $$\nabla V = -\frac{k}{(x^2+y^2)^{3/2}}(x, y) = -\frac{k}{r^3}\mathbf{r}$$
> 
> ---
> 
> **Campo eléctrico:**
> 
> $$\mathbf{E} = -\nabla V = \frac{k}{r^3}\mathbf{r} = \frac{k}{r^2}\hat{\mathbf{r}}$$
> 
> $$\boxed{\mathbf{E}(x,y) = \frac{k}{(x^2+y^2)^{3/2}}(x, y)}$$
> 
> ---
> 
> **Interpretación:**
> 
> - El campo eléctrico apunta radialmente **hacia afuera** (si $k > 0$)
> - Su magnitud es $|\mathbf{E}| = k/r^2$ (ley del inverso del cuadrado)
> - Es perpendicular a las superficies equipotenciales (círculos concéntricos)

### Ejemplo 8: Machine Learning - Gradiente Descendente

> [!example]- 🤖 Ejemplo 8: Optimización con Gradiente

> **Función de costo (error cuadrático):**
> 
> $$C(w_1, w_2) = (w_1 - 3)^2 + (w_2 + 1)^2$$
> 
> Queremos minimizar $C$ usando **gradiente descendente**.
> 
> ---
> 
> **Algoritmo:**
> 
> $$\mathbf{w}^{(k+1)} = \mathbf{w}^{(k)} - \alpha \nabla C(\mathbf{w}^{(k)})$$
> 
> donde $\alpha$ es la tasa de aprendizaje.
> 
> ---
> 
> **Paso 1: Calcular gradiente**
> 
> $$\frac{\partial C}{\partial w_1} = 2(w_1 - 3)$$
> 
> $$\frac{\partial C}{\partial w_2} = 2(w_2 + 1)$$
> 
> $$\nabla C(w_1, w_2) = (2(w_1 - 3), 2(w_2 + 1))$$
> 
> ---
> 
> **Paso 2: Iteraciones con $\alpha = 0.1$**
> 
> **Punto inicial:** $(w_1, w_2)^{(0)} = (0, 0)$
> 
> **Iteración 1:**
> 
> $$\nabla C(0, 0) = (2(-3), 2(1)) = (-6, 2)$$
> 
> $$(w_1, w_2)^{(1)} = (0, 0) - 0.1(-6, 2) = (0.6, -0.2)$$
> 
> **Iteración 2:**
> 
> $$\nabla C(0.6, -0.2) = (2(-2.4), 2(0.8)) = (-4.8, 1.6)$$
> 
> $$(w_1, w_2)^{(2)} = (0.6, -0.2) - 0.1(-4.8, 1.6) = (1.08, -0.36)$$
> 
> **Iteración 3:**
> 
> $$\nabla C(1.08, -0.36) = (-3.84, 1.28)$$
> 
> $$(w_1, w_2)^{(3)} = (1.08, -0.36) - 0.1(-3.84, 1.28) = (1.464, -0.488)$$
> 
> ---
> 
> **Convergencia:**
> 
> El algoritmo converge a $(3, -1)$, el **mínimo global** donde $\nabla C = (0, 0)$.
> 
> |Iteración|$(w_1, w_2)$|$C$|$\|\nabla C\|$|
> |---|---|---|---|
> |0|$(0, 0)$|$10$|$6.32$|
> |1|$(0.6, -0.2)$|$6.40$|$5.06$|
> |2|$(1.08, -0.36)$|$4.10$|$4.04$|
> |3|$(1.464, -0.488)$|$2.62$|$3.24$|
> |...|...|...|...|
> |∞|$(3, -1)$|$0$|$0$|

### Ejemplo 9: Curvas de Nivel y Gradiente

> [!example]- 🗺️ Ejemplo 9: Análisis de Curvas de Nivel
> 
> **Función:** $f(x,y) = x^2 - y^2$ (paraboloide hiperbólico o "silla de montar")
> 
> ---
> 
> **Gradiente:**
> 
> $$\nabla f(x,y) = (2x, -2y)$$
> 
> ---
> 
> **Curvas de nivel:** $f(x,y) = c$
> 
> $$x^2 - y^2 = c$$
> 
> Estas son **hipérbolas** (excepto $c = 0$ que son las rectas $y = \pm x$).
> 
> ---
> 
> **Verificar perpendicularidad:**
> 
> Para la curva de nivel $x^2 - y^2 = c$, derivando implícitamente:
> 
> $$2x - 2y\frac{dy}{dx} = 0$$
> 
> $$\frac{dy}{dx} = \frac{x}{y}$$
> 
> Vector tangente a la curva: $(1, \frac{dy}{dx}) = (1, \frac{x}{y})$ o proporcional a $(y, x)$
> 
> Gradiente en ese punto: $(2x, -2y)$
> 
> **Producto punto:**
> 
> $$(2x, -2y) \cdot (y, x) = 2xy - 2xy = 0$$ ✓
> 
> El gradiente es perpendicular a la curva de nivel.
> 
> ---
> 
> **Visualización en puntos específicos:**
> 
> |Punto|$f(x,y)$|$\nabla f$|Dirección|
> |---|---|---|---|
> |$(1, 0)$|$1$|$(2, 0)$|→ Este|
> |$(0, 1)$|$-1$|$(0, -2)$|↓ Sur|
> |$(1, 1)$|$0$|$(2, -2)$|↘ Sureste|
> |$(2, 1)$|$3$|$(4, -2)$|→ Este-sur|

### Ejemplo 10: Tres Variables

> [!example]- 📐 Ejemplo 10: Gradiente en 3D
> 
> **Función (temperatura en el espacio):**
> 
> $$T(x,y,z) = 100e^{-(x^2+y^2+z^2)}$$
> 
> ---
> 
> **Gradiente:**
> 
> $$\frac{\partial T}{\partial x} = 100e^{-(x^2+y^2+z^2)} \cdot (-2x) = -200xe^{-(x^2+y^2+z^2)}$$
> 
> Por simetría:
> 
> $$\nabla T(x,y,z) = -200e^{-(x^2+y^2+z^2)}(x, y, z)$$
> 
> $$\boxed{\nabla T = -200e^{-r^2}\mathbf{r}}$$
> 
> donde $\mathbf{r} = (x, y, z)$ y $r = |\mathbf{r}|$.
> 
> ---
> 
> **En el punto $(1, 0, 0)$:**
> 
> $$\nabla T(1, 0, 0) = -200e^{-1}(1, 0, 0) \approx (-73.6, 0, 0)$$
> 
> ---
> 
> **Interpretación:**
> 
> - En el origen: $\nabla T(0,0,0) = (0, 0, 0)$ (punto crítico, máximo)
> - El gradiente apunta radialmente **hacia dentro** (hacia el origen)
> - La temperatura es máxima en el origen y decrece en todas direcciones
> - Las superficies de nivel son esferas concéntricas

---

## 🧮 Propiedades Algebraicas del Gradiente

### 📊 Operaciones con Gradientes

> [!note]- 🔧 Propiedades del Operador Gradiente
> 
> Sean $f$ y $g$ funciones diferenciables, y $c$ una constante.
> 
> ### 1. Linealidad
> 
> $$\nabla(cf) = c\nabla f$$
> 
> $$\nabla(f + g) = \nabla f + \nabla g$$
> 
> ---
> 
> ### 2. Regla del Producto
> 
> $$\nabla(fg) = f\nabla g + g\nabla f$$
> 
> ---
> 
> ### 3. Regla del Cociente
> 
> $$\nabla\left(\frac{f}{g}\right) = \frac{g\nabla f - f\nabla g}{g^2}$$
> 
> ---
> 
> ### 4. Regla de la Cadena
> 
> Si $h = f \circ g$ (composición), entonces:
> 
> $$\nabla h(\mathbf{x}) = f'(g(\mathbf{x}))\nabla g(\mathbf{x})$$
> 
> Para $f: \mathbb{R} \to \mathbb{R}$ y $g: \mathbb{R}^n \to \mathbb{R}$.
> 
> ---
> 
> ### 5. Gradiente de Potencias
> 
> $$\nabla(f^n) = nf^{n-1}\nabla f$$
> 
> ---
> 
> ### Ejemplos de aplicación:
> 
> **a) $\nabla(x^2y^2) = ?$**
> 
> Usando regla del producto con $f = x^2$, $g = y^2$:
> 
> $$\nabla(x^2y^2) = x^2\nabla(y^2) + y^2\nabla(x^2)$$
> 
> $$= x^2(0, 2y) + y^2(2x, 0) = (2xy^2, 2x^2y)$$
> 
> ---
> 
> **b) $\nabla\left(\frac{x}{x^2+y^2}\right) = ?$**
> 
> Usando regla del cociente:
> 
> $$\nabla\left(\frac{x}{x^2+y^2}\right) = \frac{(x^2+y^2)(1,0) - x(2x,2y)}{(x^2+y^2)^2}$$
> 
> $$= \frac{(x^2+y^2-2x^2, -2xy)}{(x^2+y^2)^2} = \frac{(y^2-x^2, -2xy)}{(x^2+y^2)^2}$$

---

## 🎯 Aplicaciones Importantes

### 🏔️ Aplicación 1: Mapas Topográficos

> [!example]- 🗺️ Ejemplo 11: Análisis de Terreno
> 
> **Mapa topográfico** con curvas de nivel:
> 
> ```
>         y
>         |
>      6  |     1000m
>         |    /
>      4  |   /  900m
>         |  /  /
>      2  | /  /  800m
>         |/  /  /
>      0  +--+--+---- x
>         0  2  4
> ```
> 
> **Función de elevación:** $h(x,y) = 1000 - 10x^2 - 10y^2$
> 
> ---
> 
> **Gradiente:**
> 
> $$\nabla h = (-20x, -20y)$$
> 
> ---
> 
> **Interpretación del mapa:**
> 
> ✅ **Gradiente grande** (curvas juntas) = pendiente pronunciada
> 
> ✅ **Gradiente pequeño** (curvas separadas) = pendiente suave
> 
> ✅ **Gradiente cero** (centro) = cima de la montaña
> 
> ✅ **Dirección del gradiente** = dirección "cuesta arriba"
> 
> ---
> 
> **Ejemplo numérico:**
> 
> En $(2, 1)$:
> 
> - Elevación: $h(2,1) = 1000 - 40 - 10 = 950$ m
> - Gradiente: $\nabla h(2,1) = (-40, -20)$
> - Dirección de máximo ascenso: $(-40, -20)$ o $(-2, -1)$ normalizado
> - Pendiente máxima: $|\nabla h| = \sqrt{1600 + 400} = 20\sqrt{5} \approx 44.7$ m/unidad

### 🌡️ Aplicación 2: Flujo de Calor

> [!example]- 🔥 Ejemplo 12: Conducción Térmica
> 
> **Ley de Fourier:** El flujo de calor es proporcional al negativo del gradiente de temperatura:
> 
> $$\mathbf{q} = -k\nabla T$$
> 
> donde:
> 
> - $\mathbf{q}$ = vector de flujo de calor
> - $k$ = conductividad térmica
> - $T$ = temperatura
> 
> ---
> 
> **Situación:** Placa metálica con temperatura:
> 
> $$T(x,y) = 100 - x^2 - y^2$$
> 
> ---
> 
> **Gradiente de temperatura:**
> 
> $$\nabla T = (-2x, -2y)$$
> 
> En $(3, 4)$:
> 
> $$\nabla T(3,4) = (-6, -8)$$
> 
> ---
> 
> **Flujo de calor (con $k = 1$):**
> 
> $$\mathbf{q}(3,4) = -\nabla T(3,4) = (6, 8)$$
> 
> ---
> 
> **Interpretación:**
> 
> - El calor fluye en dirección $(6, 8)$
> - El calor va de regiones **calientes** (centro) a **frías** (exterior)
> - La dirección es **opuesta** al gradiente de temperatura
> - Magnitud del flujo: $|\mathbf{q}| = 10$ unidades

### 💧 Aplicación 3: Optimización de Funciones

> [!example]- 📈 Ejemplo 13: Encontrar Extremos
> 
> **Función:** $f(x,y) = x^2 + y^2 - 4x - 6y + 13$
> 
> ---
> 
> **Condición necesaria para extremos:**
> 
> En un extremo local (máximo o mínimo), el gradiente debe ser cero:
> 
> $$\nabla f = \mathbf{0}$$
> 
> ---
> 
> **Calcular gradiente:**
> 
> $$\nabla f = (2x - 4, 2y - 6)$$
> 
> ---
> 
> **Resolver $\nabla f = \mathbf{0}$:**
> 
> $$2x - 4 = 0 \implies x = 2$$ $$2y - 6 = 0 \implies y = 3$$
> 
> **Punto crítico:** $(2, 3)$
> 
> ---
> 
> **Clasificar el punto:**
> 
> Completando cuadrados:
> 
> $$f(x,y) = (x-2)^2 + (y-3)^2 + 0$$
> 
> Como $(x-2)^2 + (y-3)^2 \geq 0$ con igualdad solo en $(2,3)$:
> 
> $$\boxed{(2, 3) \text{ es un MÍNIMO GLOBAL con } f(2,3) = 0}$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> La superficie es un paraboloide con vértice en $(2, 3, 0)$. El gradiente:
> 
> - Apunta "cuesta arriba" desde cualquier punto
> - Es cero en el mínimo
> - Su magnitud aumenta con la distancia al mínimo

### 🎯 Aplicación 4: Descenso por Gradiente

> [!example]- 🤖 Ejemplo 14: Minimización Iterativa
> 
> **Problema:** Minimizar $f(x,y) = x^2 + 4y^2 - 2x - 4y + 5$
> 
> **Algoritmo de descenso por gradiente:**
> 
> $$\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - \alpha \nabla f(\mathbf{x}^{(k)})$$
> 
> ---
> 
> **Gradiente:**
> 
> $$\nabla f(x,y) = (2x - 2, 8y - 4)$$
> 
> ---
> 
> **Configuración:**
> 
> - Punto inicial: $(x_0, y_0) = (0, 0)$
> - Tasa de aprendizaje: $\alpha = 0.1$
> 
> ---
> 
> **Iteraciones:**
> 
> |$k$|$(x_k, y_k)$|$f(x_k, y_k)$|$\nabla f$|$\|\nabla f\|$|
> |---|---|---|---|---|
> |0|$(0, 0)$|$5.00$|$(-2, -4)$|$4.47$|
> |1|$(0.2, 0.4)$|$3.64$|$(-1.6, -0.8)$|$1.79$|
> |2|$(0.36, 0.48)$|$3.27$|$(-1.28, -0.16)$|$1.29$|
> |3|$(0.488, 0.496)$|$3.13$|$(-1.024, -0.032)$|$1.03$|
> |...|...|...|...|...|
> |∞|$(1, 0.5)$|$3.00$|$(0, 0)$|$0$|
> 
> ---
> 
> **Solución exacta:**
> 
> $$\nabla f = \mathbf{0} \implies x = 1, , y = 0.5$$
> 
> $$f(1, 0.5) = 1 + 1 - 2 - 2 + 5 = 3$$
> 
> El algoritmo converge al **mínimo global** $(1, 0.5)$.

---

## 🔬 Conceptos Avanzados

### 🌀 Campos Conservativos

> [!note]- 🔄 Campos Vectoriales y Potenciales
> 
> **Definición:** Un campo vectorial $\mathbf{F}: \mathbb{R}^n \to \mathbb{R}^n$ es **conservativo** si existe una función escalar $f: \mathbb{R}^n \to \mathbb{R}$ tal que:
> 
> $$\mathbf{F} = \nabla f$$
> 
> La función $f$ se llama **función potencial**.
> 
> ---
> 
> ### Propiedades
> 
> ✅ Si $\mathbf{F} = \nabla f$, entonces el trabajo realizado por $\mathbf{F}$ a lo largo de cualquier camino solo depende de los puntos inicial y final (independiente del camino).
> 
> ✅ La integral de línea cerrada es cero: $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$
> 
> ---
> 
> ### Criterio en $\mathbb{R}^2$
> 
> Si $\mathbf{F} = (P, Q)$, entonces $\mathbf{F}$ es conservativo si y solo si:
> 
> $$\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$
> 
> ---
> 
> ### Ejemplo
> 
> **Campo:** $\mathbf{F}(x,y) = (2xy, x^2 + 2y)$
> 
> **Verificar si es conservativo:**
> 
> $$\frac{\partial P}{\partial y} = \frac{\partial}{\partial y}(2xy) = 2x$$
> 
> $$\frac{\partial Q}{\partial x} = \frac{\partial}{\partial x}(x^2 + 2y) = 2x$$
> 
> Como son iguales, $\mathbf{F}$ **es conservativo**. ✓
> 
> ---
> 
> **Encontrar el potencial $f$:**
> 
> Necesitamos $\nabla f = (2xy, x^2 + 2y)$
> 
> De $f_x = 2xy$:
> 
> $$f(x,y) = \int 2xy , dx = x^2y + g(y)$$
> 
> De $f_y = x^2 + 2y$:
> 
> $$\frac{\partial}{\partial y}(x^2y + g(y)) = x^2 + g'(y) = x^2 + 2y$$
> 
> $$g'(y) = 2y \implies g(y) = y^2 + C$$
> 
> $$\boxed{f(x,y) = x^2y + y^2 + C}$$
> 
> **Verificación:** $\nabla f = (2xy, x^2 + 2y)$ ✓

### 📊 Matriz Hessiana

> [!note]- 🔢 Derivadas Segundas y Hessiana
> 
> **Definición:** La **matriz Hessiana** de $f: \mathbb{R}^n \to \mathbb{R}$ es la matriz de derivadas parciales de segundo orden:
> 
> $$H_f = \begin{pmatrix} f_{xx} & f_{xy} & \cdots & f_{xn} \ f_{yx} & f_{yy} & \cdots & f_{yn} \ \vdots & \vdots & \ddots & \vdots \ f_{nx} & f_{ny} & \cdots & f_{nn} \end{pmatrix}$$
> 
> ---
> 
> ### En dos variables
> 
> $$H_f = \begin{pmatrix} f_{xx} & f_{xy} \ f_{yx} & f_{yy} \end{pmatrix}$$
> 
> ---
> 
> ### Relación con optimización
> 
> En un punto crítico $(x_0, y_0)$ donde $\nabla f = \mathbf{0}$:
> 
> - Si $H_f$ es **definida positiva** → **mínimo local**
> - Si $H_f$ es **definida negativa** → **máximo local**
> - Si $H_f$ es **indefinida** → **punto silla**
> 
> ---
> 
> ### Criterio del discriminante (2D)
> 
> Sea $D = f_{xx}f_{yy} - (f_{xy})^2$ el determinante de la Hessiana.
> 
> - $D > 0$ y $f_{xx} > 0$ → **mínimo local**
> - $D > 0$ y $f_{xx} < 0$ → **máximo local**
> - $D < 0$ → **punto silla**
> - $D = 0$ → **test inconclu
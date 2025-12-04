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
> - $D = 0$ → **test inconclubegin{bmatrix} 2x & -2y \ 2y & 2x \end{bmatrix}$$
> $$\det(J_{\vec{F}}) = 4x^2 + 4y^2 = 4(x^2 + y^2)$$
> 
> **Puntos singulares:** $\det(J_{\vec{F}}) = 0$
> 
> $$x^2 + y^2 = 0 \implies x = y = 0$$
> 
> $$\boxed{\text{Único punto singular: } (0,0)}$$
> 
> **b)** En todo punto $(x,y) \neq (0,0)$:
> 
> $$\det(J_{\vec{F}}) > 0$$ ✅
> 
> Por el teorema de la función inversa, **sí existe inversa local**.
> 
> **c)** Cerca del origen:
> 
> Esta es la función $f(z) = z^2$ en el plano complejo. El origen es un **punto de ramificación**: dos hojas se encuentran allí. No es inyectiva en ningún entorno del origen.
> 
> ---
> 
> **10.** $F(x,y,z) = x^3 + y^3 + z^3 - 3xyz - 1 = 0$
> 
> **a)** Podemos despejar $z$ cuando:
> 
> $$F_z = 3z^2 - 3xy \neq 0$$
> 
> $$z^2 \neq xy$$
> 
> $$\boxed{\text{Excepto en puntos donde } z^2 = xy}$$
> 
> **b)** En $(1, 0, 0)$:
> 
> Verificar: $1 + 0 + 0 - 0 - 1 = 0$ ✅
> 
> $$\nabla F(1,0,0) = (3x^2 - 3yz, 3y^2 - 3xz, 3z^2 - 3xy)\Big|_{(1,0,0)}$$
> 
> $$= (3, 0, 0)$$
> 
> **Plano tangente:**
> 
> $$3(x - 1) + 0(y - 0) + 0(z - 0) = 0$$
> 
> $$\boxed{x = 1}$$
> 
> (plano vertical)
> 
> **c)** $F_z(1,0,0) = 0$ ❌
> 
> No podemos despejar $z$ en este punto (el gradiente apunta en dirección $x$, no $z$).
> 
> Pero podemos despejar $x$ en función de $(y,z)$:
> 
> $$\frac{\partial x}{\partial y} = -\frac{F_y}{F_x}, \quad \frac{\partial x}{\partial z} = -\frac{F_z}{F_x}$$
> $$
> 

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Diferenciabilidad
> 
> ✅ **Condición suficiente (C¹):**
> 
> - Si todas las derivadas parciales son **continuas** → función diferenciable
> - Es la condición más práctica de verificar
> - Garantiza que todas las fórmulas funcionan
> 
> ✅ **No confundir:**
> 
> - Existencia de derivadas parciales ≠ diferenciabilidad
> - Diferenciabilidad ≠ C¹ (aunque C¹ ⇒ diferenciable)
> 
> ---
> 
> ### Teorema de la Función Inversa
> 
> ✅ **Condición clave:**
> 
> - $\det(J_{\vec{F}}(\vec{a})) \neq 0$ → existe inversa local
> - El Jacobiano mide "no degeneración"
> 
> ✅ **Consecuencias:**
> 
> - Inversa es C¹
> - $J_{\vec{G}} = (J_{\vec{F}})^{-1}$
> - Válido solo localmente
> 
> ✅ **Aplicaciones:**
> 
> - Cambios de coordenadas
> - Sistemas de ecuaciones
> - Análisis de estabilidad
> 
> ---
> 
> ### Teorema de la Función Implícita
> 
> ✅ **Condición clave:**
> 
> - $\det\left(\frac{\partial F}{\partial \vec{y}}\right) \neq 0$ → podemos despejar $\vec{y}$
> - Las variables a despejar deben tener derivadas invertibles
> 
> ✅ **Fórmula de derivadas:**
> 
> - $\frac{dy}{dx} = -\frac{F_x}{F_y}$ (caso simple)
> - $J_{\vec{g}} = -\left[\frac{\partial F}{\partial \vec{y}}\right]^{-1} \cdot \frac{\partial F}{\partial \vec{x}}$ (caso general)
> 
> ✅ **Aplicaciones:**
> 
> - Ecuaciones implícitas
> - Superficies de nivel
> - Multiplicadores de Lagrange
> - Geometría diferencial
> 
> ---
> 
> ### Estrategia General
> 
> **Para verificar si un teorema aplica:**
> 
> 1. ✅ Verificar C¹ (derivadas continuas)
> 2. ✅ Calcular Jacobiana/gradiente
> 3. ✅ Verificar determinante ≠ 0
> 4. ✅ Concluir sobre existencia local

---

## 🔗 Relaciones Importantes

> [!quote]- 🌐 Conexiones con Otros Temas
> 
> ### Prerequisitos:
> 
> - **[[08 - Derivadas Parciales]]** - Base para todo
> - **[[09 - Derivada Direccional]]** - Caso especial
> - **[[10 - Diferenciabilidad]]** - Concepto fundamental
> - **[[11 - Funciones de Clase C¹]]** - Hipótesis central
> - **[[12 - Matriz Jacobiana]]** - Herramienta principal
> - **Álgebra Lineal: Determinantes** - Criterio de invertibilidad
> - **Álgebra Lineal: Sistemas lineales** - Resolución local
> 
> ### Este tema es prerequisito para:
> 
> - **[[14 - Multiplicadores de Lagrange]]** - Usa función implícita
> - **[[15 - Optimización con Restricciones]]** - Aplicación directa
> - **[[16 - Integrales Múltiples]]** - Cambio de variables válido
> - **[[17 - Teoremas Integrales]]** - Condiciones de regularidad
> - **Geometría Diferencial** - Superficies y variedades
> - **Ecuaciones Diferenciales** - Existencia y unicidad
> - **Análisis Complejo** - Funciones holomorfas
> 
> ### Conceptos relacionados:
> 
> - **Aproximación Lineal** - Consecuencia de diferenciabilidad
> - **Plano Tangente** - Existe si es diferenciable
> - **Regla de la Cadena** - Válida para C¹
> - **Cambio de Variables** - Usa función inversa
> - **Curvas/Superficies de Nivel** - Usa función implícita
> - **Difeomorfismos** - Invertibilidad global
> 
> ### Diagrama de Flujo:
> 
> ```
> C¹ (derivadas continuas)
>          ↓
>   Diferenciabilidad
>          ↓
>     ┌────┴────┐
>     ↓         ↓
> Función    Función
> Inversa    Implícita
>     ↓         ↓
> Cambios   Ecuaciones
> Coords    Implícitas
> ```
> 
> ### Siguiente tema recomendado:
> 
> **[[14 - Multiplicadores de Lagrange]]** - Aplicación importante de estos teoremas

---

## 📊 Mapa Conceptual Completo

> [!note]- 🌳 Árbol de Conceptos
> 
> ```
> TEOREMAS SOBRE DIFERENCIABILIDAD
> │
> ├─ TEOREMA 1: DIFERENCIABILIDAD
> │  ├─ Enunciado: C¹ ⇒ Diferenciable
> │  ├─ Hipótesis: Derivadas parciales continuas
> │  ├─ Conclusión: Aproximación lineal válida
> │  └─ Consecuencias
> │     ├─ D_u f = ∇f · u funciona
> │     ├─ Plano tangente existe
> │     └─ Regla de la cadena válida
> │
> ├─ TEOREMA 2: FUNCIÓN INVERSA
> │  ├─ Enunciado: det(J_F) ≠ 0 ⇒ existe F⁻¹ local
> │  ├─ Hipótesis
> │  │  ├─ F ∈ C¹
> │  │  └─ Jacobiano no nulo
> │  ├─ Conclusión
> │  │  ├─ Existe inversa local G
> │  │  ├─ G ∈ C¹
> │  │  └─ J_G = (J_F)⁻¹
> │  └─ Aplicaciones
> │     ├─ Cambios de coordenadas
> │     ├─ Sistemas no lineales
> │     └─ Análisis de singularidades
> │
> ├─ TEOREMA 3: FUNCIÓN IMPLÍCITA
> │  ├─ Enunciado: det(∂F/∂y) ≠ 0 ⇒ podemos despejar y
> │  ├─ Hipótesis
> │  │  ├─ F ∈ C¹
> │  │  ├─ F(a,b) = 0
> │  │  └─ ∂F/∂y invertible
> │  ├─ Conclusión
> │  │  ├─ Existe y = g(x) local
> │  │  ├─ g ∈ C¹
> │  │  └─ Fórmula para derivadas
> │  └─ Aplicaciones
> │     ├─ Ecuaciones implícitas
> │     ├─ Superficies de nivel
> │     ├─ Multiplicadores de Lagrange
> │     └─ Geometría diferencial
> │
> ├─ RELACIONES ENTRE TEOREMAS
> │  ├─ Función implícita generaliza función inversa
> │  ├─ Todos requieren C¹
> │  └─ Todos son resultados locales
> │
> ├─ CONTRAEJEMPLOS IMPORTANTES
> │  ├─ Derivadas existen pero no continuas
> │  ├─ No diferenciable pero derivadas existen
> │  └─ Jacobiano cero: no invertible
> │
> └─ APLICACIONES AVANZADAS
>    ├─ Optimización con restricciones
>    ├─ Ecuaciones diferenciales
>    ├─ Análisis numérico (Newton)
>    ├─ Geometría diferencial
>    └─ Física matemática
> ```

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **Los tres teoremas son pilares del cálculo multivariable**
>     - Diferenciabilidad: cuándo las fórmulas funcionan
>     - Función Inversa: cuándo podemos "revertir" transformaciones
>     - Función Implícita: cuándo podemos "despejar" variables
> 2. **La condición C¹ es central**
>     - Aparece en los tres teoremas
>     - Es verificable en la práctica
>     - Garantiza "buen comportamiento"
> 3. **El Jacobiano es la clave**
>     - Su determinante mide "no degeneración"
>     - Determina invertibilidad local
>     - Aparece en todos los criterios
> 4. **Todo es local**
>     - Los teoremas garantizan existencia en entornos
>     - No dicen nada sobre comportamiento global
>     - Singularidades pueden aparecer fuera del entorno
> 5. **Aplicaciones ubicuas**
>     - Estos teoremas fundamentan casi toda la matemática aplicada
>     - Desde optimización hasta ecuaciones diferenciales
>     - Son herramientas indispensables
> 
> ---
> 
> ### Jerarquía de Conceptos
> 
> ```
> Derivadas parciales existen
>          ↓
> Derivadas parciales continuas (C¹)
>          ↓
>    Diferenciabilidad
>          ↓
>     ┌────┴────┐
>     ↓         ↓
> Invertibilidad  Despeje
>   local        implícito
> ```
> 
> ---
> 
> ### Estrategia para Aplicar los Teoremas
> 
> **Checklist:**
> 
> 6. ✅ **Identificar el problema:**
>     - ¿Quiero invertir una función? → Función Inversa
>     - ¿Quiero despejar variables? → Función Implícita
>     - ¿Quiero usar fórmulas? → Diferenciabilidad
> 7. ✅ **Verificar hipótesis:**
>     - Calcular derivadas parciales
>     - Verificar continuidad
>     - Calcular Jacobiana/determinante
> 8. ✅ **Aplicar conclusión:**
>     - Usar fórmulas del teorema
>     - Calcular derivadas de funciones implícitas
>     - Analizar comportamiento local
> 9. ✅ **Interpretar resultado:**
>     - ¿Qué dice geométricamente?
>     - ¿Hay singularidades?
>     - ¿Es válido globalmente?
> 
> ---
> 
> ### Errores Comunes
> 
> ❌ **Confundir:**
> 
> - "Derivadas existen" con "función diferenciable"
> - "Localmente invertible" con "globalmente invertible"
> - "Podemos despejar" con "hay fórmula cerrada"
> 
> ❌ **Olvidar:**
> 
> - Verificar continuidad de derivadas
> - Calcular el determinante Jacobiano
> - Que los resultados son locales
> 
> ❌ **Asumir:**
> 
> - Que el teorema aplica sin verificar hipótesis
> - Que si falla en un punto, falla en todos
> - Que existe fórmula explícita para la inversa/implícita
> 
> ---
> 
> ### Reflexión Final
> 
> Estos tres teoremas responden preguntas fundamentales:
> 
> 1. **¿Cuándo puedo confiar en las fórmulas?** → Teorema de Diferenciabilidad
> 2. **¿Cuándo puedo "deshacer" una transformación?** → Teorema de la Función Inversa
> 3. **¿Cuándo puedo resolver para una variable?** → Teorema de la Función Implícita
> 
> Son herramientas que:
> 
> - **Unifican** el cálculo multivariable
> - **Garantizan** validez de métodos
> - **Fundamentan** aplicaciones prácticas
> 
> **Mensaje clave:**
> 
> La continuidad de las derivadas (C¹) es la "regularidad mínima" que garantiza que el cálculo multivariable funciona como esperamos. El Jacobiano no nulo es la condición que permite "invertir" o "despejar" localmente.
> 
> Estos teoremas son el puente entre:
> 
> - El cálculo de derivadas (mecánico)
> - La existencia de soluciones (teórico)
> - Las aplicaciones prácticas (útil)
> 
> Dominarlos es dominar el corazón del cálculo multivariable.

---

## 📖 Tabla de Referencia Rápida

> [!note]- 📋 Resumen de Teoremas
> 
> |Teorema|Hipótesis|Conclusión|Aplicación Principal|
> |---|---|---|---|
> |**Diferenciabilidad**|$f \in C^1$|$f$ diferenciable|Usar fórmulas con confianza|
> |**Función Inversa**|$F \in C^1$, $\det(J_F) \neq 0$|Existe $F^{-1}$ local, C¹|Cambios de coordenadas|
> |**Función Implícita**|$F \in C^1$, $\det(\frac{\partial F}{\partial y}) \neq 0$|Existe $y = g(x)$ local, C¹|Despejar variables|
> 
> ### Fórmulas Clave
> 
> **Derivada implícita (caso simple):** $$\frac{dy}{dx} = -\frac{F_x}{F_y}$$
> 
> **Derivada implícita (general):** $$J_g = -\left[\frac{\partial F}{\partial y}\right]^{-1} \cdot \frac{\partial F}{\partial x}$$
> 
> **Jacobiana de la inversa:** $$J_{F^{-1}} = (J_F)^{-1}$$
> 
> ### Condiciones a Verificar
> 
> ✅ C¹: Todas las derivadas parciales continuas
> 
> ✅ Jacobiano: $\det(J_F) \neq 0$
> 
> ✅ Punto satisface ecuación: $F(\vec{a}) = 0$

---

**Tags:** #calculo-multivariable #teoremas-diferenciabilidad #funcion-inversa #funcion-implicita #clase-C1 #jacobiana #jacobiano #diferenciabilidad #multiplicadores-lagrange #cambio-variables #ecuaciones-implicitas #optimizacion #analisis-real

# 📘  Derivada Direccional

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Derivadas Direccionales?
> 
> Las derivadas parciales nos dan información sobre cómo cambia una función en las direcciones de los **ejes coordenados**. Pero, ¿qué pasa si queremos saber cómo cambia en **cualquier dirección**?
> 
> **Motivación:**
> 
> - Derivadas parciales: solo direcciones $x$ e $y$ (ejes coordenados)
> - Derivadas direccionales: **cualquier dirección** en el plano o espacio
> - Generalización natural de las derivadas parciales
> 
> **Aplicaciones prácticas:**
> 
> - **Geografía:** Pendiente de una montaña en cualquier dirección
> - **Física:** Tasa de cambio de temperatura en una dirección específica
> - **Optimización:** Dirección de máximo crecimiento (gradiente)
> - **Navegación:** Determinar la ruta de mayor/menor ascenso
> 
> **Diferencia clave:**
> 
> - Derivada parcial $\frac{\partial f}{\partial x}$: dirección fija (eje $x$)
> - Derivada direccional $D_{\vec{u}}f$: dirección **arbitraria** $\vec{u}$

---

## 📐 Definición de Derivada Direccional

### 🔍 Definición Formal

> [!example]- 🟢 Definición: Derivada Direccional
> 
> **Definición:** Sea $f: \mathbb{R}^n \to \mathbb{R}$ una función y $\vec{u}$ un **vector unitario** (es decir, $|\vec{u}| = 1$). La **derivada direccional** de $f$ en el punto $\vec{a}$ en la dirección de $\vec{u}$ es:
> 
> $$D_{\vec{u}}f(\vec{a}) = \lim_{h \to 0} \frac{f(\vec{a} + h\vec{u}) - f(\vec{a})}{h}$$
> 
> **siempre que este límite exista.**
> 
> ---
> 
> **En dos variables:** Si $\vec{a} = (x_0, y_0)$ y $\vec{u} = (u_1, u_2)$ con $u_1^2 + u_2^2 = 1$:
> 
> $$D_{\vec{u}}f(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + hu_1, y_0 + hu_2) - f(x_0, y_0)}{h}$$
> 
> ---
> 
> **Interpretación:**
> 
> - Mide la **tasa de cambio instantánea** de $f$ cuando nos movemos desde $(x_0, y_0)$ en la dirección del vector $\vec{u}$
> - Es la pendiente de la superficie en esa dirección específica
> 
> ---
> 
> **Notaciones:**
> 
> - $D_{\vec{u}}f$
> - $\nabla_{\vec{u}}f$
> - $\frac{\partial f}{\partial \vec{u}}$

### 🎯 Interpretación Geométrica

> [!note]- 📊 Visualización
> 
> Para una superficie $z = f(x,y)$ y un punto $(x_0, y_0)$:
> 
> ```
>         z
>         |
>         |    Superficie z = f(x,y)
>         |      /|\
>         |     / | \
>         |    /  |  \
>         |   /   •(x₀,y₀)
>         |  /   ↗ \    ← Dirección û
>         | /  /    \
>         |/__/______\__ y
>        /
>       x
> ```
> 
> **$D_{\vec{u}}f(x_0, y_0)$ es:**
> 
> - La pendiente de la curva que resulta de cortar la superficie con un plano vertical que pasa por $(x_0, y_0)$ en la dirección de $\vec{u}$
> - Qué tan rápido cambia $f$ si nos movemos desde $(x_0, y_0)$ en dirección $\vec{u}$
> 
> ---
> 
> **Analogía de la montaña:**
> 
> Imagina que estás en un punto de una montaña:
> 
> - Las derivadas parciales $f_x$ y $f_y$ te dicen qué tan empinado es hacia el Este y Norte
> - La derivada direccional $D_{\vec{u}}f$ te dice qué tan empinado es en **cualquier dirección** que elijas

---

## 🧮 Relación con Derivadas Parciales

> [!note]- 🔄 Casos Especiales
> 
> Las **derivadas parciales** son casos especiales de derivadas direccionales:
> 
> ### Dirección del eje $x$
> 
> Si $\vec{u} = \vec{i} = (1, 0)$:
> 
> $$D_{\vec{i}}f = \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h} = \frac{\partial f}{\partial x}$$
> 
> ---
> 
> ### Dirección del eje $y$
> 
> Si $\vec{u} = \vec{j} = (0, 1)$:
> 
> $$D_{\vec{j}}f = \lim_{h \to 0} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h} = \frac{\partial f}{\partial y}$$
> 
> ---
> 
> **Conclusión:** $$\boxed{\frac{\partial f}{\partial x} = D_{\vec{i}}f \quad \text{y} \quad \frac{\partial f}{\partial y} = D_{\vec{j}}f}$$
> 
> Las derivadas parciales son simplemente derivadas direccionales en las direcciones de los ejes coordenados.

---

## 🌟 El Gradiente

### 📐 Definición del Gradiente

> [!example]- 🟡 Definición: Vector Gradiente
> 
> **Definición:** El **gradiente** de una función $f(x,y)$ es el vector formado por todas sus derivadas parciales:
> 
> $$\nabla f = \text{grad } f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$
> 
> ---
> 
> **En tres variables:** $$\nabla f(x,y,z) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$$
> 
> ---
> 
> **Notación:**
> 
> - $\nabla f$ (nabla de $f$)
> - $\text{grad } f$
> - El símbolo $\nabla$ se lee "nabla" o "del"
> 
> ---
> 
> **Propiedades del vector:**
> 
> - El gradiente es un **vector** (no un escalar)
> - Tiene la misma dimensión que el dominio de $f$
> - Sus componentes son las derivadas parciales
> 
> ---
> 
> **Ejemplo:** Si $f(x,y) = x^2 + 3xy + y^2$:
> 
> $$\frac{\partial f}{\partial x} = 2x + 3y$$ $$\frac{\partial f}{\partial y} = 3x + 2y$$
> 
> $$\nabla f = (2x + 3y, 3x + 2y)$$
> 
> En el punto $(1, 2)$: $$\nabla f(1,2) = (2(1) + 3(2), 3(1) + 2(2)) = (8, 7)$$

### 🎯 Propiedades del Gradiente

> [!note]- ⭐ Propiedades Importantes
> 
> ### 1. Álgebra del Gradiente
> 
> **Linealidad:** $$\nabla(af + bg) = a\nabla f + b\nabla g$$
> 
> **Regla del producto:** $$\nabla(fg) = f\nabla g + g\nabla f$$
> 
> **Regla del cociente:** $$\nabla\left(\frac{f}{g}\right) = \frac{g\nabla f - f\nabla g}{g^2}$$
> 
> **Regla de la cadena:** Si $h = g \circ f$, entonces: $$\nabla h = g'(f) \nabla f$$
> 
> ---
> 
> ### 2. Interpretación Geométrica
> 
> El gradiente $\nabla f$ en un punto:
> 
> - Apunta en la dirección de **máximo crecimiento** de $f$
> - Su magnitud $|\nabla f|$ es la **tasa máxima de cambio**
> - Es **perpendicular** a las curvas de nivel de $f$
> 
> ---
> 
> ### 3. Propiedades Direccionales
> 
> - La dirección de $\nabla f$ es donde $f$ crece más rápidamente
> - La dirección de $-\nabla f$ es donde $f$ decrece más rápidamente
> - Las direcciones perpendiculares a $\nabla f$ no cambian el valor de $f$ (tangentes a curvas de nivel)

---

## 🔑 Fórmula Fundamental: Derivada Direccional y Gradiente

> [!example]- 🟢 Teorema Principal
> 
> **Teorema:** Si $f$ es **diferenciable** en $(x_0, y_0)$ y $\vec{u}$ es un vector unitario, entonces:
> 
> $$\boxed{D_{\vec{u}}f = \nabla f \cdot \vec{u}}$$
> 
> Es decir, la derivada direccional es el **producto punto** del gradiente con el vector dirección.
> 
> ---
> 
> **En componentes:** Si $\vec{u} = (u_1, u_2)$ y $\nabla f = (f_x, f_y)$:
> 
> $$D_{\vec{u}}f = f_x u_1 + f_y u_2$$
> 
> ---
> 
> **En tres variables:** Si $\vec{u} = (u_1, u_2, u_3)$ y $\nabla f = (f_x, f_y, f_z)$:
> 
> $$D_{\vec{u}}f = f_x u_1 + f_y u_2 + f_z u_3$$
> 
> ---
> 
> **Importancia:** Esta fórmula convierte un problema de límites en un simple producto punto. ¡Es mucho más fácil de calcular!
> 
> ---
> 
> **Condición necesaria:**
> 
> - $\vec{u}$ debe ser **unitario**: $|\vec{u}| = 1$
> - Si no lo es, primero normalizar: $\hat{u} = \frac{\vec{u}}{|\vec{u}|}$

---

## 📚 Ejemplos Básicos

### Ejemplo 1: Derivada Direccional Simple

> [!example]- 📝 Ejemplo 1: Cálculo Directo
> 
> **Función:** $$f(x,y) = x^2 + y^2$$
> 
> **Punto:** $(3, 4)$
> 
> **Dirección:** $\vec{v} = (1, 1)$
> 
> ---
> 
> **Paso 1: Calcular el gradiente**
> 
> $$\frac{\partial f}{\partial x} = 2x, \quad \frac{\partial f}{\partial y} = 2y$$
> 
> $$\nabla f = (2x, 2y)$$
> 
> En $(3, 4)$: $$\nabla f(3,4) = (6, 8)$$
> 
> ---
> 
> **Paso 2: Normalizar el vector dirección**
> 
> $$|\vec{v}| = \sqrt{1^2 + 1^2} = \sqrt{2}$$
> 
> $$\vec{u} = \frac{\vec{v}}{|\vec{v}|} = \frac{(1,1)}{\sqrt{2}} = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$$
> 
> ---
> 
> **Paso 3: Calcular la derivada direccional**
> 
> $$D_{\vec{u}}f(3,4) = \nabla f(3,4) \cdot \vec{u}$$
> 
> $$= (6, 8) \cdot \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$$
> 
> $$= 6 \cdot \frac{1}{\sqrt{2}} + 8 \cdot \frac{1}{\sqrt{2}}$$
> 
> $$= \frac{6 + 8}{\sqrt{2}} = \frac{14}{\sqrt{2}} = 7\sqrt{2}$$
> 
> $$\boxed{D_{\vec{u}}f(3,4) = 7\sqrt{2} \approx 9.899}$$
> 
> ---
> 
> **Interpretación:** Si nos movemos desde $(3,4)$ en la dirección de $45°$ (hacia arriba-derecha), la función aumenta a una tasa de $7\sqrt{2}$ unidades por unidad de distancia.

### Ejemplo 2: Diferentes Direcciones

> [!example]- 📝 Ejemplo 2: Comparar Direcciones
> 
> **Función:** $$f(x,y) = x^2 - y^2$$
> 
> **Punto:** $(1, 1)$
> 
> Calcular la derivada direccional en varias direcciones.
> 
> ---
> 
> **Gradiente:** $$\nabla f = (2x, -2y)$$
> 
> En $(1,1)$: $$\nabla f(1,1) = (2, -2)$$
> 
> ---
> 
> **a) Dirección del eje $x$:** $\vec{u}_1 = (1, 0)$
> 
> $$D_{\vec{u}_1}f = (2, -2) \cdot (1, 0) = 2$$
> 
> ---
> 
> **b) Dirección del eje $y$:** $\vec{u}_2 = (0, 1)$
> 
> $$D_{\vec{u}_2}f = (2, -2) \cdot (0, 1) = -2$$
> 
> ---
> 
> **c) Dirección diagonal:** $\vec{v}_3 = (1, 1)$
> 
> Normalizar: $\vec{u}_3 = \frac{1}{\sqrt{2}}(1, 1)$
> 
> $$D_{\vec{u}_3}f = (2, -2) \cdot \frac{1}{\sqrt{2}}(1, 1) = \frac{1}{\sqrt{2}}(2 - 2) = 0$$
> 
> ---
> 
> **d) Dirección del gradiente:** $\vec{u}_4 = \frac{(2,-2)}{|(2,-2)|} = \frac{1}{\sqrt{8}}(2, -2) = \frac{1}{2\sqrt{2}}(2, -2)$
> 
> $$D_{\vec{u}_4}f = (2, -2) \cdot \frac{1}{2\sqrt{2}}(2, -2) = \frac{1}{2\sqrt{2}}(4 + 4) = \frac{8}{2\sqrt{2}} = 2\sqrt{2}$$
> 
> ---
> 
> **Observaciones:**
> 
> - En dirección $x$: aumenta ($+2$)
> - En dirección $y$: disminuye ($-2$)
> - En dirección diagonal $(1,1)$: no cambia ($0$)
> - En dirección del gradiente: máximo cambio ($2\sqrt{2}$)

### Ejemplo 3: Función Exponencial

> [!example]- 📝 Ejemplo 3: Con Exponencial
> 
> **Función:** $$f(x,y) = e^{xy}$$
> 
> **Punto:** $(0, 1)$
> 
> **Dirección:** hacia el punto $(1, 3)$ desde $(0, 1)$
> 
> ---
> 
> **Paso 1: Gradiente**
> 
> $$\frac{\partial f}{\partial x} = ye^{xy}, \quad \frac{\partial f}{\partial y} = xe^{xy}$$
> 
> En $(0, 1)$: $$\nabla f(0,1) = (1 \cdot e^0, 0 \cdot e^0) = (1, 0)$$
> 
> ---
> 
> **Paso 2: Vector dirección**
> 
> Desde $(0,1)$ hacia $(1,3)$: $$\vec{v} = (1,3) - (0,1) = (1, 2)$$
> 
> Normalizar: $$|\vec{v}| = \sqrt{1^2 + 2^2} = \sqrt{5}$$
> 
> $$\vec{u} = \frac{1}{\sqrt{5}}(1, 2)$$
> 
> ---
> 
> **Paso 3: Derivada direccional**
> 
> $$D_{\vec{u}}f(0,1) = (1, 0) \cdot \frac{1}{\sqrt{5}}(1, 2) = \frac{1}{\sqrt{5}}$$
> 
> $$\boxed{D_{\vec{u}}f(0,1) = \frac{1}{\sqrt{5}} = \frac{\sqrt{5}}{5}}$$

### Ejemplo 4: Función Trigonométrica

> [!example]- 📝 Ejemplo 4: Seno y Coseno
> 
> **Función:** $$f(x,y) = \sin(x)\cos(y)$$
> 
> **Punto:** $\left(\frac{\pi}{4}, \frac{\pi}{3}\right)$
> 
> **Dirección:** $\vec{u} = \frac{1}{\sqrt{2}}(1, -1)$ (ya normalizado)
> 
> ---
> 
> **Gradiente:** $$\frac{\partial f}{\partial x} = \cos(x)\cos(y)$$ $$\frac{\partial f}{\partial y} = -\sin(x)\sin(y)$$
> 
> En $\left(\frac{\pi}{4}, \frac{\pi}{3}\right)$:
> 
> $$f_x = \cos\left(\frac{\pi}{4}\right)\cos\left(\frac{\pi}{3}\right) = \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{2}}{4}$$
> 
> $$f_y = -\sin\left(\frac{\pi}{4}\right)\sin\left(\frac{\pi}{3}\right) = -\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} = -\frac{\sqrt{6}}{4}$$
> 
> $$\nabla f = \left(\frac{\sqrt{2}}{4}, -\frac{\sqrt{6}}{4}\right)$$
> 
> ---
> 
> **Derivada direccional:**
> 
> $$D_{\vec{u}}f = \left(\frac{\sqrt{2}}{4}, -\frac{\sqrt{6}}{4}\right) \cdot \frac{1}{\sqrt{2}}(1, -1)$$
> 
> $$= \frac{1}{\sqrt{2}}\left(\frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4}\right) = \frac{\sqrt{2} + \sqrt{6}}{4\sqrt{2}}$$
> 
> $$= \frac{\sqrt{2} + \sqrt{6}}{4\sqrt{2}} \cdot \frac{\sqrt{2}}{\sqrt{2}} = \frac{2 + \sqrt{12}}{8} = \frac{2 + 2\sqrt{3}}{8} = \frac{1 + \sqrt{3}}{4}$$
> 
> $$\boxed{D_{\vec{u}}f = \frac{1 + \sqrt{3}}{4}}$$

---

## 🎯 Dirección de Máximo Crecimiento

> [!note]- 🌟 Teorema: Máximo y Mínimo Crecimiento
> 
> **Teorema:** Sea $f$ diferenciable en $(x_0, y_0)$ y sea $\nabla f(x_0, y_0) \neq \vec{0}$. Entonces:
> 
> ### 1. Máximo Crecimiento
> 
> La dirección de **máximo crecimiento** de $f$ es: $$\vec{u}_{\text{máx}} = \frac{\nabla f}{|\nabla f|}$$
> 
> Y la **tasa máxima de crecimiento** es: $$D_{\text{máx}} = |\nabla f|$$
> 
> ---
> 
> ### 2. Mínimo Crecimiento (Máximo Decrecimiento)
> 
> La dirección de **máximo decrecimiento** de $f$ es: $$\vec{u}_{\text{mín}} = -\frac{\nabla f}{|\nabla f|}$$
> 
> Y la **tasa mínima de cambio** es: $$D_{\text{mín}} = -|\nabla f|$$
> 
> ---
> 
> ### 3. Sin Cambio
> 
> Las direcciones donde $f$ **no cambia** son perpendiculares a $\nabla f$: $$\vec{u} \perp \nabla f \implies D_{\vec{u}}f = 0$$
> 
> Estas direcciones son **tangentes a las curvas de nivel** de $f$.
> 
> ---
> 
> **Demostración del máximo:**
> 
> $$D_{\vec{u}}f = \nabla f \cdot \vec{u} = |\nabla f| |\vec{u}| \cos\theta$$
> 
> Como $|\vec{u}| = 1$: $$D_{\vec{u}}f = |\nabla f| \cos\theta$$
> 
> Esto es máximo cuando $\cos\theta = 1$, es decir, cuando $\theta = 0$, lo que significa que $\vec{u}$ apunta en la misma dirección que $\nabla f$.

### Ejemplo 5: Encontrar Direcciones Extremas

> [!example]- 📝 Ejemplo 5: Máximo y Mínimo Cambio
> 
> **Función:** $$f(x,y) = x^2 + 2y^2$$
> 
> **Punto:** $(1, 1)$
> 
> Encontrar: a) Dirección de máximo crecimiento y su tasa b) Dirección de máximo decrecimiento y su tasa c) Una dirección donde $f$ no cambia
> 
> ---
> 
> **Gradiente:** $$\nabla f = (2x, 4y)$$
> 
> En $(1,1)$: $$\nabla f(1,1) = (2, 4)$$
> 
> **Magnitud:** $$|\nabla f(1,1)| = \sqrt{2^2 + 4^2} = \sqrt{20} = 2\sqrt{5}$$
> 
> ---
> 
> **a) Máximo crecimiento:**
> 
> Dirección: $$\vec{u}_{\text{máx}} = \frac{(2,4)}{2\sqrt{5}} = \frac{1}{\sqrt{5}}(1, 2)$$
> 
> Tasa máxima: $$D_{\text{máx}} = 2\sqrt{5} \approx 4.472$$
> 
> $$\boxed{\text{Dirección: } \frac{1}{\sqrt{5}}(1,2), \quad \text{Tasa: } 2\sqrt{5}}$$
> 
> ---
> 
> **b) Máximo decrecimiento:**
> 
> Dirección: $$\vec{u}_{\text{mín}} = -\frac{1}{\sqrt{5}}(1, 2)$$
> 
> Tasa: $$D_{\text{mín}} = -2\sqrt{5}$$
> 
> $$\boxed{\text{Dirección: } -\frac{1}{\sqrt{5}}(1,2), \quad \text{Tasa: } -2\sqrt{5}}$$
> 
> ---
> 
> **c) Sin cambio:**
> 
> Necesitamos $\vec{u} \perp (2,4)$
> 
> Un vector perpendicular a $(2,4)$ es $(4, -2)$ o $(-4, 2)$
> 
> Normalizar: $\vec{u} = \frac{1}{\sqrt{20}}(4, -2) = \frac{1}{\sqrt{5}}(2, -1)$
> 
> Verificar: $$D_{\vec{u}}f = (2,4) \cdot \frac{1}{\sqrt{5}}(2,-1) = \frac{1}{\sqrt{5}}(4 - 4) = 0$$ ✓
> 
> $$\boxed{\text{Dirección sin cambio: } \frac{1}{\sqrt{5}}(2,-1)}$$

---

## 🏔️ Aplicaciones Prácticas

### Aplicación 1: Ascenso en una Montaña

> [!example]- ⛰️ Ejemplo: Topografía
> 
> **Situación:** La elevación de una montaña está dada por (en metros): $$h(x,y) = 1000 - 0.01x^2 - 0.02y^2$$
> 
> donde $x, y$ están en metros.
> 
> Un excursionista está en el punto $(50, 30)$.
> 
> ---
> 
> **a) ¿En qué dirección debe caminar para subir más rápido?**
> 
> **Gradiente:** $$\nabla h = (-0.02x, -0.04y)$$
> 
> En $(50, 30)$: $$\nabla h(50,30) = (-1, -1.2)$$
> 
> **Dirección de máximo ascenso:** (opuesto al gradiente porque el gradiente apunta hacia abajo) $$\vec{u}_{\text{ascenso}} = -\frac{(-1,-1.2)}{|(-1,-1.2)|} = \frac{(1,1.2)}{\sqrt{1 + 1.44}} = \frac{(1,1.2)}{\sqrt{2.44}}$$
> 
> $$= \frac{(1,1.2)}{1.562} \approx (0.640, 0.768)$$
> 
> **Respuesta:** Debe caminar aproximadamente en dirección $(0.640, 0.768)$, es decir, un ángulo de unos $50.2°$ respecto al eje $x$ positivo.
> 
> ---
> 
> **b) ¿Cuál es la pendiente máxima en ese punto?**
> 
> $$|\nabla h(50,30)| = \sqrt{1 + 1.44} = \sqrt{2.44} \approx 1.562$$
> 
> **Respuesta:** La pendiente máxima es aproximadamente 1.562, o un ángulo de $\arctan(1.562) \approx 57.4°$.
> 
> ---
> 
> **c) Si camina hacia el Norte, ¿cuál es su tasa de ascenso?**
> 
> Norte = dirección $\vec{u} = (0, 1)$
> 
> $$D_{\vec{u}}h = (-1, -1.2) \cdot (0, 1) = -1.2$$
> 
> **Respuesta:** Desciende a razón de 1.2 metros por metro de distancia horizontal.

### Aplicación 2: Temperatura

> [!example]- 🌡️ Ejemplo: Distribución de Temperatura
> 
> **Situación:** La temperatura en una placa metálica es: $$T(x,y) = 100 - x^2 - 2y^2$$
> 
> (temperatura en °C, coordenadas en cm)
> 
> Un sensor está en $(3, 2)$.
> 
> ---
> 
> **a) ¿En qué dirección aumenta la temperatura más rápido?**
> 
> $$\nabla T = (-2x, -4y)$$
> 
> En $(3,2)$: $$\nabla T(3,2) = (-6, -8)$$
> 
> **Dirección de máximo aumento:** $$\vec{u} = \frac{(-6,-8)}{\sqrt{36+64}} = \frac{(-6,-8)}{10} = (-0.6, -0.8)$$
> 
> **Respuesta:** Hacia el origen (dirección aproximada $(-0.6, -0.8)$).
>
> ---
> 
> **b) ¿Cuál es la tasa máxima de cambio de temperatura?**
> 
> $$|\nabla T(3,2)| = 10 \text{ °C/cm}$$
> 
> **Respuesta:** La temperatura aumenta a razón máxima de 10°C por centímetro en la dirección hacia el origen.
> 
> ---
> 
> **c) Si el sensor se mueve en dirección $\vec{v} = (4, 3)$, ¿cómo cambia la temperatura?**
> 
> Normalizar: $\vec{u} = \frac{(4,3)}{5}$
> 
> $$D_{\vec{u}}T = (-6, -8) \cdot \frac{(4,3)}{5} = \frac{-24-24}{5} = \frac{-48}{5} = -9.6$$
> 
> **Respuesta:** La temperatura disminuye a razón de 9.6°C/cm.

### Aplicación 3: Optimización

> [!example]- 📊 Ejemplo: Función de Producción
> 
> **Situación:** Una empresa tiene función de producción: $$P(K,L) = 100K^{0.4}L^{0.6}$$
> 
> donde $K$ = capital, $L$ = trabajo.
> 
> Actualmente $K = 81$, $L = 16$.
> 
> ---
> 
> **a) Si se aumenta capital y trabajo proporcionalmente, ¿cómo cambia la producción?**
> 
> Dirección: $\vec{v} = (1, 1)$ (proporcional)
> 
> Normalizar: $\vec{u} = \frac{1}{\sqrt{2}}(1, 1)$
> 
> **Gradiente:** $$\frac{\partial P}{\partial K} = 40K^{-0.6}L^{0.6}$$ $$\frac{\partial P}{\partial L} = 60K^{0.4}L^{-0.4}$$
> 
> En $(81, 16)$: $$P_K = 40 \cdot 81^{-0.6} \cdot 16^{0.6} = 40 \cdot \frac{16^{0.6}}{81^{0.6}}$$
> 
> Calculando:
> 
> - $81^{0.6} = (3^4)^{0.6} = 3^{2.4} \approx 13.97$
> - $16^{0.6} = (2^4)^{0.6} = 2^{2.4} \approx 5.28$
> 
> $$P_K \approx 40 \cdot \frac{5.28}{13.97} \approx 15.1$$
> 
> Similarmente: $$P_L \approx 60 \cdot \frac{81^{0.4}}{16^{0.4}} \approx 113.1$$
> 
> $$\nabla P(81,16) \approx (15.1, 113.1)$$
> 
> **Derivada direccional:** $$D_{\vec{u}}P \approx (15.1, 113.1) \cdot \frac{1}{\sqrt{2}}(1,1) \approx \frac{128.2}{\sqrt{2}} \approx 90.7$$
> 
> **Respuesta:** La producción aumenta aproximadamente 90.7 unidades por unidad de aumento proporcional.
> 
> ---
> 
> **b) ¿Qué recurso tiene mayor productividad marginal?**
> 
> Comparar componentes del gradiente:
> 
> - Capital: $P_K \approx 15.1$
> - Trabajo: $P_L \approx 113.1$
> 
> **Respuesta:** El trabajo tiene mucho mayor productividad marginal.

---

## 🔄 Derivadas Direccionales en Tres Variables

> [!note]- 🎲 Extensión a $\mathbb{R}^3$
> 
> ### Definición
> 
> Para $f(x,y,z)$ y vector unitario $\vec{u} = (u_1, u_2, u_3)$:
> 
> $$D_{\vec{u}}f = \nabla f \cdot \vec{u} = f_x u_1 + f_y u_2 + f_z u_3$$
> 
> donde: $$\nabla f = (f_x, f_y, f_z) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$$
> 
> ---
> 
> ### Interpretación
> 
> - El gradiente $\nabla f$ apunta en la dirección de máximo crecimiento en el espacio 3D
> - $|\nabla f|$ es la tasa máxima de cambio
> - $\nabla f$ es perpendicular a las **superficies de nivel** $f(x,y,z) = c$

### Ejemplo 6: Función de Tres Variables

> [!example]- 📝 Ejemplo 6: En 3D
> 
> **Función:** $$f(x,y,z) = x^2 + y^2 + z^2$$
> 
> **Punto:** $(1, 2, 2)$
> 
> **Dirección:** hacia el punto $(2, 3, 4)$
> 
> ---
> 
> **Gradiente:** $$\nabla f = (2x, 2y, 2z)$$
> 
> En $(1,2,2)$: $$\nabla f(1,2,2) = (2, 4, 4)$$
> 
> ---
> 
> **Vector dirección:** Desde $(1,2,2)$ hacia $(2,3,4)$: $$\vec{v} = (2,3,4) - (1,2,2) = (1, 1, 2)$$
> 
> Normalizar: $$|\vec{v}| = \sqrt{1 + 1 + 4} = \sqrt{6}$$
> 
> $$\vec{u} = \frac{1}{\sqrt{6}}(1, 1, 2)$$
> 
> ---
> 
> **Derivada direccional:** $$D_{\vec{u}}f = (2, 4, 4) \cdot \frac{1}{\sqrt{6}}(1, 1, 2)$$
> 
> $$= \frac{1}{\sqrt{6}}(2 + 4 + 8) = \frac{14}{\sqrt{6}} = \frac{14\sqrt{6}}{6} = \frac{7\sqrt{6}}{3}$$
> 
> $$\boxed{D_{\vec{u}}f(1,2,2) = \frac{7\sqrt{6}}{3} \approx 5.715}$$

### Ejemplo 7: Campo Escalar en Física

> [!example]- 📝 Ejemplo 7: Potencial Eléctrico
> 
> **Situación:** El potencial eléctrico debido a una carga puntual es: $$V(x,y,z) = \frac{k}{\sqrt{x^2 + y^2 + z^2}}$$
> 
> donde $k$ es una constante.
> 
> **Encontrar:** La dirección del campo eléctrico en el punto $(1, 1, 1)$.
> 
> ---
> 
> **Nota:** El campo eléctrico es $\vec{E} = -\nabla V$
> 
> **Calcular el gradiente:**
> 
> Sea $r = \sqrt{x^2 + y^2 + z^2}$, entonces $V = \frac{k}{r}$
> 
> $$\frac{\partial V}{\partial x} = -\frac{k}{r^2} \cdot \frac{\partial r}{\partial x} = -\frac{k}{r^2} \cdot \frac{x}{r} = -\frac{kx}{r^3}$$
> 
> Similarmente: $$\nabla V = -\frac{k}{r^3}(x, y, z)$$
> 
> En $(1,1,1)$: $$r = \sqrt{3}, \quad r^3 = 3\sqrt{3}$$
> 
> $$\nabla V(1,1,1) = -\frac{k}{3\sqrt{3}}(1,1,1)$$
> 
> ---
> 
> **Campo eléctrico:** $$\vec{E}(1,1,1) = -\nabla V = \frac{k}{3\sqrt{3}}(1,1,1)$$
> 
> **Dirección:** $(1,1,1)$ normalizado = $\frac{1}{\sqrt{3}}(1,1,1)$
> 
> **Interpretación:** El campo apunta radialmente hacia afuera desde el origen.

---

## 📐 Relación con Curvas y Superficies de Nivel

> [!note]- 🎯 Gradiente y Curvas de Nivel
> 
> ### Teorema: Gradiente Perpendicular a Curvas de Nivel
> 
> **Enunciado:** Si $f$ es diferenciable, entonces $\nabla f$ en un punto es **perpendicular** a la curva de nivel de $f$ que pasa por ese punto.
> 
> ---
> 
> **En 2D:**
> 
> - Curva de nivel: $f(x,y) = c$
> - $\nabla f$ es perpendicular a esta curva
> 
> **En 3D:**
> 
> - Superficie de nivel: $f(x,y,z) = c$
> - $\nabla f$ es perpendicular a esta superficie (es el vector normal)
> 
> ---
> 
> **Consecuencia:** Para moverse **sin cambiar** el valor de $f$, debemos movernos en dirección perpendicular a $\nabla f$.
> 
> ---
> 
> **Visualización en 2D:**
> 
> ```
>       y
>       |
>       |    ∇f ↑
>       |      |
>       |  ----•----  ← Curva de nivel f(x,y) = c
>       |            (tangente a la curva)
>       +------------ x
> ```
> 
> El gradiente apunta "cuesta arriba", perpendicular a las curvas de nivel.

### Ejemplo 8: Curvas de Nivel

> [!example]- 📝 Ejemplo 8: Visualizar Gradiente y Nivel
> 
> **Función:** $$f(x,y) = x^2 + y^2$$
> 
> **Curvas de nivel:** círculos $x^2 + y^2 = c$
> 
> ---
> 
> **Gradiente:** $$\nabla f = (2x, 2y)$$
> 
> En un punto $(x_0, y_0)$: $$\nabla f(x_0, y_0) = (2x_0, 2y_0) = 2(x_0, y_0)$$
> 
> ---
> 
> **Observación:**
> 
> - El gradiente apunta radialmente hacia afuera desde el origen
> - Las curvas de nivel son círculos concéntricos
> - El gradiente es perpendicular a los círculos (radios son perpendiculares a círculos)
> 
> **Verificación de perpendicularidad:**
> 
> Vector tangente a la curva $x^2 + y^2 = c$ en $(x_0, y_0)$ es perpendicular al radio, por ejemplo $(-y_0, x_0)$.
> 
> Producto punto: $$(2x_0, 2y_0) \cdot (-y_0, x_0) = -2x_0y_0 + 2y_0x_0 = 0$$ ✓
> 
> El gradiente es perpendicular al vector tangente, confirmando el teorema.

### Ejemplo 9: Superficie de Nivel

> [!example]- 📝 Ejemplo 9: Normal a Superficie
> 
> **Superficie:** $$x^2 + y^2 + z^2 = 9$$ (esfera de radio 3)
> 
> **Encontrar:** Vector normal en el punto $(1, 2, 2)$
> 
> ---
> 
> **Solución:**
> 
> Definimos $f(x,y,z) = x^2 + y^2 + z^2$
> 
> La esfera es la superficie de nivel $f(x,y,z) = 9$
> 
> El vector normal es $\nabla f$:
> 
> $$\nabla f = (2x, 2y, 2z)$$
> 
> En $(1,2,2)$: $$\nabla f(1,2,2) = (2, 4, 4)$$
> 
> O normalizando: $$\vec{n} = \frac{(2,4,4)}{|(2,4,4)|} = \frac{(2,4,4)}{6} = \frac{1}{3}(1, 2, 2)$$
> 
> $$\boxed{\text{Vector normal unitario: } \frac{1}{3}(1,2,2)}$$
> 
> ---
> 
> **Observación geométrica:** Para una esfera centrada en el origen, el vector normal en cualquier punto apunta radialmente (es paralelo al vector posición), lo cual tiene sentido geométricamente.

---

## 🎯 Propiedades de las Derivadas Direccionales

> [!note]- 📋 Propiedades Importantes
> 
> ### 1. Linealidad
> 
> $$D_{\vec{u}}(af + bg) = aD_{\vec{u}}f + bD_{\vec{u}}g$$
> 
> ---
> 
> ### 2. Regla del Producto
> 
> $$D_{\vec{u}}(fg) = f \cdot D_{\vec{u}}g + g \cdot D_{\vec{u}}f$$
> 
> ---
> 
> ### 3. Regla de la Cadena
> 
> Si $h = g \circ f$: $$D_{\vec{u}}h = g'(f) \cdot D_{\vec{u}}f$$
> 
> ---
> 
> ### 4. Desigualdad de Cauchy-Schwarz
> 
> $$|D_{\vec{u}}f| = |\nabla f \cdot \vec{u}| \leq |\nabla f| |\vec{u}| = |\nabla f|$$
> 
> (porque $|\vec{u}| = 1$)
> 
> La igualdad se alcanza cuando $\vec{u}$ es paralelo a $\nabla f$.
> 
> ---
> 
> ### 5. Direcciones Opuestas
> 
> $$D_{-\vec{u}}f = -D_{\vec{u}}f$$
> 
> ---
> 
> ### 6. Independencia del Ángulo con Nivel
> 
> Si $\vec{u}$ es tangente a una curva de nivel ($\vec{u} \perp \nabla f$): $$D_{\vec{u}}f = 0$$

---

## 🧮 Tabla de Fórmulas de Referencia

> [!note]- 📋 Resumen de Fórmulas
> 
> |Concepto|Fórmula|
> |---|---|
> |**Derivada direccional**|$D_{\vec{u}}f = \nabla f \cdot \vec{u}$|
> |**Gradiente (2D)**|$\nabla f = (f_x, f_y)$|
> |**Gradiente (3D)**|$\nabla f = (f_x, f_y, f_z)$|
> |**Magnitud del gradiente**|$\|\nabla f\| = \sqrt{f_x^2 + f_y^2}$|
> |**Vector unitario**|$\vec{u} = \frac{\vec{v}}{\|\vec{v}\|}$|
> |**Dirección máximo crecimiento**|$\vec{u}_{\max} = \frac{\nabla f}{\|\nabla f\|}$|
> |**Tasa máxima de cambio**|$D_{\max} = \|\nabla f\|$|
> |**Dirección mínimo**|$\vec{u}_{\min} = -\frac{\nabla f}{\|\nabla f\|}$|
> |**Sin cambio**|$\vec{u} \perp \nabla f$|
> |**Producto punto**|$\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2$|
> |**Ángulo entre vectores**|$\cos\theta = \frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\|\vec{b}\|}$|

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular el gradiente:**
> 
> a) $f(x,y) = 3x^2 + 2xy + y^2$
> 
> b) $f(x,y) = e^{xy}$
> 
> c) $f(x,y) = \ln(x^2 + y^2)$
> 
> d) $f(x,y) = x\sin(y)$
> 
> ---
> 
> **2. Calcular derivada direccional:**
> 
> Para $f(x,y) = x^2 + y^2$ en el punto $(1,1)$:
> 
> a) En dirección $\vec{v} = (1, 0)$
> 
> b) En dirección $\vec{v} = (0, 1)$
> 
> c) En dirección $\vec{v} = (3, 4)$
> 
> d) En dirección $\vec{v} = (-1, -1)$
> 
> ---
> 
> **3. Normalizar vectores:**
> 
> a) $\vec{v} = (3, 4)$
> 
> b) $\vec{v} = (1, 1, 1)$
> 
> c) $\vec{v} = (5, -12)$
> 
> d) $\vec{v} = (2, 2, 1)$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Dirección de máximo cambio:**
> 
> Para cada función en el punto dado, encontrar:
> 
> - Dirección de máximo crecimiento
> - Tasa máxima de cambio
> - Una dirección donde no cambia
> 
> a) $f(x,y) = x^2 - y^2$ en $(2, 1)$
> 
> b) $f(x,y) = xe^y$ en $(1, 0)$
> 
> c) $f(x,y,z) = xyz$ en $(1, 2, 3)$
> 
> ---
> 
> **5. Aplicaciones:**
> 
> a) La temperatura en una placa es $T(x,y) = 100 - x^2 - 2y^2$. En el punto $(3,2)$, ¿en qué dirección aumenta más rápido la temperatura?
> 
> b) La elevación de una colina es $h(x,y) = 50 - x^2 - y^2$. Si estás en $(3,4)$ y caminas hacia $(5,6)$, ¿subes o bajas? ¿A qué tasa?
> 
> ---
> 
> **6. Curvas de nivel:**
> 
> Para $f(x,y) = xy$:
> 
> a) Dibujar algunas curvas de nivel
> 
> b) Calcular $\nabla f$ en el punto $(2, 3)$
> 
> c) Verificar que $\nabla f$ es perpendicular a la curva de nivel que pasa por $(2,3)$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Problemas teóricos:**
> 
> a) Demostrar que si $f(x,y) = g(x) + h(y)$, entonces $\nabla f = (g'(x), h'(y))$
> 
> b) Demostrar que $\nabla(fg) = f\nabla g + g\nabla f$
> 
> c) Si $\nabla f = \vec{0}$ en todos los puntos, ¿qué podemos concluir sobre $f$?
> 
> ---
> 
> **8. Optimización:**
> 
> a) Encuentra el punto más cercano a $(1,2)$ sobre la curva $x^2 + y^2 = 1$ usando el hecho de que en el punto más cercano, el gradiente debe ser perpendicular a la curva.
> 
> b) Para $f(x,y) = x^2 + 2y^2$, encontrar todos los puntos donde $\nabla f = \vec{0}$
> 
> ---
> 
> **9. Tres variables:**
> 
> a) Para $f(x,y,z) = x^2 + y^2 + z^2$, encontrar la derivada direccional en $(1,1,1)$ hacia el punto $(2,3,2)$
> 
> b) Para $V(x,y,z) = xyz$, encontrar el vector normal a la superficie de nivel que pasa por $(1,2,3)$
> 
> ---
> 
> **10. Aplicación física:**
> 
> El potencial gravitatorio cerca de la superficie terrestre es $V(x,y,z) = -gz$ donde $g = 9.8$ m/s².
> 
> a) Calcular $\nabla V$
> 
> b) ¿Qué representa físicamente $-\nabla V$?
> 
> c) Si una partícula en $(1,2,3)$ se mueve en dirección $(1,1,1)$ normalizada, ¿cómo cambia su energía potencial?

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = 3x^2 + 2xy + y^2$
> 
> $$\nabla f = (6x + 2y, 2x + 2y)$$
> 
> ---
> 
> **1b)** $f(x,y) = e^{xy}$
> 
> $$\nabla f = (ye^{xy}, xe^{xy})$$
> 
> ---
> 
> **2a)** $f(x,y) = x^2 + y^2$ en $(1,1)$, dirección $(1,0)$
> 
> $$\nabla f(1,1) = (2, 2)$$ $$D_{\vec{u}}f = (2,2) \cdot (1,0) = 2$$
> 
> ---
> 
> **2c)** Dirección $\vec{v} = (3,4)$
> 
> Normalizar: $\vec{u} = \frac{1}{5}(3,4)$
> 
> $$D_{\vec{u}}f = (2,2) \cdot \frac{1}{5}(3,4) = \frac{6+8}{5} = \frac{14}{5}$$
> 
> ---
> 
> **3a)** $\vec{v} = (3,4)$
> 
> $$|\vec{v}| = \sqrt{9+16} = 5$$ $$\vec{u} = \frac{1}{5}(3,4)$$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $f(x,y) = x^2 - y^2$ en $(2,1)$
> 
> $$\nabla f = (2x, -2y)$$ $$\nabla f(2,1) = (4, -2)$$
> 
> **Dirección máximo crecimiento:** $$\vec{u}_{\max} = \frac{(4,-2)}{\sqrt{16+4}} = \frac{(4,-2)}{\sqrt{20}} = \frac{1}{\sqrt{5}}(2,-1)$$
> 
> **Tasa máxima:** $$|\nabla f| = \sqrt{20} = 2\sqrt{5}$$
> 
> **Sin cambio:** perpendicular a $(4,-2)$ → $(2,4)$ o $(-2,-4)$
> 
> Normalizado: $\vec{u} = \frac{1}{\sqrt{20}}(2,4) = \frac{1}{\sqrt{5}}(1,2)$
> 
> ---
> 
> **5a)** $T(x,y) = 100 - x^2 - 2y^2$ en $(3,2)$
> 
> $$\nabla T = (-2x, -4y)$$ $$\nabla T(3,2) = (-6, -8)$$
> 
> **Dirección de máximo aumento:** $$\vec{u} = \frac{(-6,-8)}{10} = (-0.6, -0.8)$$
> 
> **Respuesta:** Hacia el origen (sudoeste).
> 
> ---
> 
> **5b)** $h(x,y) = 50 - x^2 - y^2$ en $(3,4)$ hacia $(5,6)$
> 
> $$\nabla h(3,4) = (-6, -8)$$
> 
> Dirección: $\vec{v} = (2,2)$, normalizar: $\vec{u} = \frac{1}{\sqrt{2}}(1,1)$
> 
> $$D_{\vec{u}}h = (-6,-8) \cdot \frac{1}{\sqrt{2}}(1,1) = \frac{-14}{\sqrt{2}} = -7\sqrt{2}$$
> 
> **Respuesta:** Bajas a razón de $7\sqrt{2} \approx 9.9$ m por unidad de distancia.

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **7c)** Si $\nabla f = \vec{0}$ en todos los puntos
> 
> $$\frac{\partial f}{\partial x} = 0 \text{ y } \frac{\partial f}{\partial y} = 0$$
> 
> **Conclusión:** $f$ es una función **constante**.
> 
> ---
> 
> **8b)** $f(x,y) = x^2 + 2y^2$
> 
> $$\nabla f = (2x, 4y) = (0,0)$$
> 
> $$x = 0 \text{ y } y = 0$$
> 
> **Respuesta:** Solo en el punto $(0,0)$.
> 
> ---
> 
> **10a)** $V(x,y,z) = -gz$
> 
> $$\nabla V = (0, 0, -g)$$
> 
> ---
> 
> **10b)** $-\nabla V = (0,0,g)$
> 
> **Respuesta:** La fuerza gravitatoria (apunta hacia abajo).

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Derivadas Direccionales
> 
> ✅ **Definición:**
> 
> - $D_{\vec{u}}f$ mide la tasa de cambio de $f$ en dirección $\vec{u}$
> - $\vec{u}$ debe ser **unitario**: $|\vec{u}| = 1$
> 
> ✅ **Fórmula fundamental:**
> 
> - $D_{\vec{u}}f = \nabla f \cdot \vec{u}$
> - Producto punto del gradiente con la dirección
> 
> ✅ **Casos especiales:**
> 
> - Derivadas parciales son derivadas direccionales en ejes coordenados
> - $\frac{\partial f}{\partial x} = D_{\vec{i}}f$, $\frac{\partial f}{\partial y} = D_{\vec{j}}f$
> 
> ---
> 
> ### Sobre el Gradiente
> 
> ✅ **Vector gradiente:**
> 
> - $\nabla f$ = vector de derivadas parciales
> - En 2D: $\nabla f = (f_x, f_y)$
> - En 3D: $\nabla f = (f_x, f_y, f_z)$
> 
> ✅ **Dirección del gradiente:**
> 
> - Apunta hacia el **máximo crecimiento** de $f$
> - Es **perpendicular** a curvas/superficies de nivel
> 
> ✅ **Magnitud del gradiente:**
> 
> - $|\nabla f|$ = tasa **máxima** de cambio de $f$
> 
> ---
> 
> ### Aplicaciones
> 
> 📍 **Optimización:** Gradiente indica dirección de ascenso 📍 **Física:** Campos vectoriales (eléctrico, gravitatorio) 📍 **Geometría:** Vector normal a superficies 📍 **Análisis:** Curvas y superficies de nivel

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes 
> **Este tema es prerequisito para:**
> 
> - [[10 - Diferenciabilidad y Plano Tangente]] - El gradiente define el plano tangente
> - [[11 - Regla de la Cadena]] - Composición con derivadas direccionales
> - [[12 - Optimización sin Restricciones]] - Condiciones de primer orden
> - [[13 - Multiplicadores de Lagrange]] - Optimización con restricciones
> - [[14 - Teorema de Taylor]] - Aproximaciones de orden superior
> - [[15 - Campos Vectoriales]] - Gradiente como campo vectorial
> 
> **Conceptos relacionados:**
> 
> - **Derivadas Parciales** - Casos especiales de derivadas direccionales
> - **Continuidad** - Diferenciabilidad implica continuidad
> - **Curvas de Nivel** - Perpendiculares al gradiente
> - **Vector Normal** - El gradiente es normal a superficies de nivel
> - **Descenso de Gradiente** - Algoritmo de optimización
> 
> **Siguiente tema recomendado:** [[10 - Diferenciabilidad y Aproximación Lineal]]

---

## 💡 Estrategias y Trucos

> [!tip]- 🎯 Técnicas para Problemas de Derivadas Direccionales
> 
> ### Estrategia 1: Siempre Normalizar
> 
> **Antes de calcular** $D_{\vec{u}}f$, verificar: $$|\vec{u}| = 1$$
> 
> Si no: $\vec{u} = \frac{\vec{v}}{|\vec{v}|}$
> 
> **Error común:** Olvidar normalizar y obtener resultados incorrectos.
> 
> ---
> 
> ### Estrategia 2: Gradiente Primero
> 
> **Orden recomendado:**
> 
> 1. Calcular $\nabla f$
> 2. Evaluar en el punto
> 3. Normalizar el vector dirección
> 4. Producto punto
> 
> ---
> 
> ### Estrategia 3: Interpretación Geométrica
> 
> **Usar el ángulo:** $$D_{\vec{u}}f = |\nabla f| \cos\theta$$
> 
> donde $\theta$ es el ángulo entre $\nabla f$ y $\vec{u}$.
> 
> - $\theta = 0°$: máximo crecimiento
> - $\theta = 90°$: sin cambio
> - $\theta = 180°$: máximo decrecimiento
> 
> ---
> 
> ### Estrategia 4: Verificar con Casos Conocidos
> 
> **Sanity check:**
> 
> - $D_{\vec{i}}f$ debe dar $f_x$
> - $D_{\vec{j}}f$ debe dar $f_y$
> - Si $\vec{u} \perp \nabla f$, debe dar 0
> 
> ---
> 
> ### Estrategia 5: Usar Simetría
> 
> Si la función tiene simetría, el gradiente también:
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2$ (simétrica radial)
> 
> - $\nabla f = 2(x,y)$ apunta radialmente
> - En círculos concéntricos, perpendicular a los círculos

---

## 🔬 Casos Especiales

> [!warning]- ⚠️ Situaciones Especiales
> 
> ### Caso 1: Gradiente Cero
> 
> Si $\nabla f(x_0, y_0) = \vec{0}$:
> 
> - $D_{\vec{u}}f = \vec{0} \cdot \vec{u} = 0$ para **toda** dirección $\vec{u}$
> - El punto $(x_0, y_0)$ es un **punto crítico**
> - Puede ser máximo, mínimo o punto silla
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2$ en $(0,0)$
> 
> - $\nabla f(0,0) = (0,0)$
> - Es un mínimo
> 
> ---
> 
> ### Caso 2: Función No Diferenciable
> 
> La fórmula $D_{\vec{u}}f = \nabla f \cdot \vec{u}$ requiere que $f$ sea **diferenciable**.
> 
> **Contraejemplo:** $f(x,y) = |x| + |y|$ en $(0,0)$
> 
> - Las derivadas parciales existen: $f_x(0,0) = 0$, $f_y(0,0) = 0$
> - Pero $f$ no es diferenciable en $(0,0)$
> - La fórmula del gradiente NO funciona correctamente
> 
> ---
> 
> ### Caso 3: Dirección No Unitaria
> 
> Si usamos un vector $\vec{v}$ que no es unitario:
> 
> $$\frac{df}{d\vec{v}} = \nabla f \cdot \vec{v} = |\vec{v}| \cdot D_{\vec{u}}f$$
> 
> donde $\vec{u} = \frac{\vec{v}}{|\vec{v}|}$
> 
> Esto da la tasa de cambio **total** (no normalizada).
> 
> ---
> 
> ### Caso 4: Curvas Paramétricas
> 
> Si nos movemos a lo largo de una curva $\vec{r}(t) = (x(t), y(t))$:
> 
> $$\frac{df}{dt} = \nabla f \cdot \frac{d\vec{r}}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$
> 
> Esto es la **derivada total** (tema de la regla de la cadena).

---

## 📊 Visualización Avanzada

> [!note]- 🎨 Interpretación Visual Completa
> 
> ### Mapa de Contorno con Gradientes
> 
> Para $f(x,y) = x^2 + y^2$:
> 
> ```
>       y
>       |
>     4 |        ○  ← f = 16
>       |      ○   ○
>     3 |    ○   •   ○
>       |      ↗ ↑ ↖   ← Gradientes
>     2 |   ○   ○   ○ ○
>       |     ○ • ○     ← f = 4
>     1 | ○ ○ ↗ ↑ ↖ ○ ○
>       |   ○ • ○      ← f = 1
>     0 +---•------------ x
>       0   1   2   3   4
> 
>     • = Curva de nivel
>     ↑ = Vector gradiente (perpendicular)
> ```
> 
> **Observaciones:**
> 
> - Curvas de nivel: círculos concéntricos
> - Gradientes: apuntan hacia afuera (máximo crecimiento)
> - Perpendiculares a las curvas de nivel
> - Más largos donde la función crece más rápido
> 
> ---
> 
> ### Campo de Gradientes 3D
> 
> Para $f(x,y,z) = x^2 + y^2 + z^2$:
> 
> ```
>         z
>         |
>         |    ↑
>         |  ↗ | ↖
>         | ←  •  →  ← Gradientes apuntan
>         |  ↙ | ↘     radialmente
>         +--------- y
>        /
>       /
>      x
> ```
> 
> Las superficies de nivel son esferas, y los gradientes apuntan radialmente hacia afuera.

---

## 🎯 Algoritmo: Descenso de Gradiente

> [!note]- 🔄 Aplicación en Optimización
> 
> ### Método del Descenso de Gradiente
> 
> **Objetivo:** Encontrar el mínimo de $f(x,y)$
> 
> **Idea:** Moverse en la dirección de **mayor descenso** (opuesta al gradiente)
> 
> **Algoritmo:**
> 
> 1. Empezar en un punto inicial $(x_0, y_0)$
> 2. Calcular $\nabla f(x_k, y_k)$
> 3. Actualizar: $(x_{k+1}, y_{k+1}) = (x_k, y_k) - \alpha \nabla f(x_k, y_k)$
> 4. Repetir hasta convergencia
> 
> donde $\alpha$ es el **tamaño de paso** (learning rate)
> 
> ---
> 
> ### Ejemplo Numérico
> 
> **Minimizar:** $f(x,y) = x^2 + 4y^2$
> 
> **Gradiente:** $\nabla f = (2x, 8y)$
> 
> **Punto inicial:** $(4, 2)$ **Tamaño de paso:** $\alpha = 0.1$
> 
> **Iteración 1:**
> 
> - $\nabla f(4,2) = (8, 16)$
> - $(x_1, y_1) = (4,2) - 0.1(8,16) = (3.2, 0.4)$
> 
> **Iteración 2:**
> 
> - $\nabla f(3.2, 0.4) = (6.4, 3.2)$
> - $(x_2, y_2) = (3.2, 0.4) - 0.1(6.4, 3.2) = (2.56, 0.08)$
> 
> **Continuar...**
> 
> El método converge hacia el mínimo $(0,0)$.
> 
> ---
> 
> **Aplicaciones:**
> 
> - Machine Learning (entrenamiento de redes neuronales)
> - Optimización numérica
> - Ajuste de parámetros

---

## 📐 Fórmulas en Diferentes Sistemas de Coordenadas

> [!note]- 🔢 Coordenadas Alternativas
> 
> ### Coordenadas Polares (2D)
> 
> Si $x = r\cos\theta$, $y = r\sin\theta$:
> 
> $$\nabla f = \frac{\partial f}{\partial r}\hat{r} + \frac{1}{r}\frac{\partial f}{\partial \theta}\hat{\theta}$$
> 
> donde:
> 
> - $\hat{r} = (\cos\theta, \sin\theta)$ (dirección radial)
> - $\hat{\theta} = (-\sin\theta, \cos\theta)$ (dirección tangencial)
> 
> ---
> 
> ### Coordenadas Cilíndricas (3D)
> 
> Si $x = r\cos\theta$, $y = r\sin\theta$, $z = z$:
> 
> $$\nabla f = \frac{\partial f}{\partial r}\hat{r} + \frac{1}{r}\frac{\partial f}{\partial \theta}\hat{\theta} + \frac{\partial f}{\partial z}\hat{z}$$
> 
> ---
> 
> ### Coordenadas Esféricas (3D)
> 
> Si $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$:
> 
> $$\nabla f = \frac{\partial f}{\partial \rho}\hat{\rho} + \frac{1}{\rho}\frac{\partial f}{\partial \phi}\hat{\phi} + \frac{1}{\rho\sin\phi}\frac{\partial f}{\partial \theta}\hat{\theta}$$
> 
> ---
> 
> **Importancia:** En problemas con simetría, estas coordenadas simplifican enormemente los cálculos.

---

## 🌟 Teoremas Importantes Relacionados

> [!note]- 🎓 Resultados Teóricos
> 
> ### Teorema 1: Existencia del Máximo
> 
> **Enunciado:** Si $f$ es diferenciable y $\nabla f \neq \vec{0}$, entonces existe una dirección de máximo crecimiento.
> 
> **Dirección:** $\vec{u}_{\max} = \frac{\nabla f}{|\nabla f|}$
> 
> **Valor máximo:** $|\nabla f|$
> 
> ---
> 
> ### Teorema 2: Caracterización de Puntos Críticos
> 
> **Enunciado:** Si $\nabla f(x_0, y_0) = \vec{0}$, entonces $D_{\vec{u}}f(x_0, y_0) = 0$ para toda dirección $\vec{u}$.
> 
> **Consecuencia:** Los puntos críticos no tienen dirección de crecimiento preferida (primera derivada = 0).
> 
> ---
> 
> ### Teorema 3: Regla de la Cadena (adelanto)
> 
> **Enunciado:** Si $\vec{r}(t) = (x(t), y(t))$ es una curva diferenciable, entonces:
> 
> $$\frac{d}{dt}f(\vec{r}(t)) = \nabla f \cdot \vec{r}'(t)$$
> 
> **Interpretación:** La derivada de $f$ a lo largo de una curva es la derivada direccional en la dirección tangente a la curva.
> 
> ---
> 
> ### Teorema 4: Valor Medio
> 
> **Enunciado:** Si $f$ es diferenciable en un segmento de recta de $\vec{a}$ a $\vec{b}$, entonces existe un punto $\vec{c}$ en ese segmento tal que:
> 
> $$f(\vec{b}) - f(\vec{a}) = \nabla f(\vec{c}) \cdot (\vec{b} - \vec{a})$$
> 
> **Interpretación:** Generalización del teorema del valor medio a varias variables.

---

## 💻 Ejemplos Computacionales

> [!example]- 🖥️ Ejemplo: Cálculo Numérico
> 
> ### Pseudocódigo para Derivada Direccional
> 
> ```python
> def derivada_direccional(f, punto, direccion):
>     """
>     Calcula la derivada direccional de f en punto
>     en la dirección dada
>     """
>     # Calcular gradiente (numéricamente)
>     h = 1e-8
>     grad_x = (f(punto[0]+h, punto[1]) - f(punto[0]-h, punto[1])) / (2*h)
>     grad_y = (f(punto[0], punto[1]+h) - f(punto[0], punto[1]-h)) / (2*h)
>     
>     gradiente = [grad_x, grad_y]
>     
>     # Normalizar dirección
>     norma = sqrt(direccion[0]**2 + direccion[1]**2)
>     direccion_unit = [direccion[0]/norma, direccion[1]/norma]
>     
>     # Producto punto
>     resultado = gradiente[0]*direccion_unit[0] + gradiente[1]*direccion_unit[1]
>     
>     return resultado
> ```
> 
> ---
> 
> ### Ejemplo de Uso
> 
> ```python
> # Función: f(x,y) = x^2 + y^2
> def f(x, y):
>     return x**2 + y**2
> 
> punto = (1, 1)
> direccion = (3, 4)
> 
> resultado = derivada_direccional(f, punto, direccion)
> # Resultado: 2.8 (que es 14/5)
> ```

---

## 🎯 Resumen Visual: Mapa Conceptual

> [!note]- 🌳 Árbol de Conceptos
> 
> ```
> DERIVADA DIRECCIONAL
> │
> ├─ DEFINICIÓN
> │  ├─ Límite: lim[h→0] (f(a+hu) - f(a))/h
> │  ├─ Dirección: vector unitario û
> │  └─ Interpretación: tasa de cambio en dirección û
> │
> ├─ GRADIENTE
> │  ├─ Definición: ∇f = (fx, fy) o (fx, fy, fz)
> │  ├─ Propiedades algebraicas
> │  ├─ Dirección: máximo crecimiento
> │  ├─ Magnitud: tasa máxima de cambio
> │  └─ Perpendicularidad: a curvas/superficies de nivel
> │
> ├─ FÓRMULA FUNDAMENTAL
> │  ├─ Dᵤf = ∇f · û
> │  ├─ Requiere: f diferenciable, û unitario
> │  └─ Casos especiales: fx = Dᵢf, fy = Dⱼf
> │
> ├─ DIRECCIONES ESPECIALES
> │  ├─ Máximo crecimiento: û = ∇f/||∇f||
> │  ├─ Máximo decrecimiento: û = -∇f/||∇f||
> │  └─ Sin cambio: û ⊥ ∇f
> │
> └─ APLICACIONES
>    ├─ Optimización (descenso de gradiente)
>    ├─ Física (campos, fuerzas)
>    ├─ Geometría (vectores normales)
>    └─ Análisis (curvas de nivel)
> ```

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **La derivada direccional generaliza las derivadas parciales** a cualquier dirección
>     
> 2. **El gradiente es el vector clave:**
>     
>     - Sus componentes son las derivadas parciales
>     - Apunta hacia el máximo crecimiento
>     - Es perpendicular a curvas/superficies de nivel
> 3. **Fórmula fundamental:** $D_{\vec{u}}f = \nabla f \cdot \vec{u}$
>     
>     - Simple producto punto
>     - Requiere $\vec{u}$ unitario
>     - Requiere $f$ diferenciable
> 4. **Interpretación geométrica es crucial:**
>     
>     - Visualizar el gradiente
>     - Entender curvas de nivel
>     - Relacionar con pendientes
> 5. **Aplicaciones prácticas abundan:**
>     
>     - Optimización (machine learning)
>     - Física (campos vectoriales)
>     - Ingeniería (análisis de sensibilidad)
> 
> ---
> 
> ### Próximos Pasos
> 
> Con derivadas direccionales y gradiente dominados, estás listo para:
> 
> - **Diferenciabilidad completa:** Aproximación lineal total
> - **Plano tangente:** Mejor aproximación a superficies
> - **Regla de la cadena:** Composición de funciones
> - **Optimización:** Encontrar extremos usando gradiente
> - **Campos vectoriales:** Gradiente como campo vectorial
> 
> ---
> 
> ### Práctica Recomendada
> 
> - Calcular gradientes de muchas funciones
> - Visualizar curvas de nivel y gradientes simultáneamente
> - Practicar normalización de vectores
> - Resolver problemas aplicados (física, economía)
> - Implementar descenso de gradiente numéricamente
> - Relacionar derivadas direccionales con geometría

---

## 📖 Lecturas Complementarias

> [!note]- 📚 Para Profundizar
> 
> ### Conceptos Relacionados
> 
> **1. Diferenciabilidad:**
> 
> - Relación entre gradiente y diferenciabilidad
> - Aproximación lineal completa
> - Plano tangente
> 
> **2. Optimización:**
> 
> - Condiciones de primer orden: $\nabla f = \vec{0}$
> - Descenso de gradiente y variantes
> - Métodos de Newton
> 
> **3. Geometría Diferencial:**
> 
> - Curvaturas
> - Vectores normales y tangentes
> - Superficies de nivel
> 
> **4. Análisis Vectorial:**
> 
> - Divergencia y rotacional
> - Teoremas integrales (Green, Stokes, Gauss)
> - Campos conservativos
> 
> **5. Ecuaciones Diferenciales:**
> 
> - EDPs de primer orden
> - Método de las características
> - Ecuaciones de transporte
> 
> ---
> 
> ### Aplicaciones Avanzadas
> 
> - **Machine Learning:** Backpropagation, optimización convexa
> - **Física:** Mecánica lagrangiana, teoría de campos
> - **Procesamiento de señales:** Filtros adaptativos
> - **Computer Vision:** Detección de bordes (gradiente de imagen)
> - **Finanzas:** Análisis de sensibilidad (las "griegas")

---

**Tags:** #calculo-multivariable #derivada-direccional #gradiente #optimizacion #curvas-nivel #vectores #descenso-gradiente #fisica-matematica #campos-vectoriales #geometria-diferencial
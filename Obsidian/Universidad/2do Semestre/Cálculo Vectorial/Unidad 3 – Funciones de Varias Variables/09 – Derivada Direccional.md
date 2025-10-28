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
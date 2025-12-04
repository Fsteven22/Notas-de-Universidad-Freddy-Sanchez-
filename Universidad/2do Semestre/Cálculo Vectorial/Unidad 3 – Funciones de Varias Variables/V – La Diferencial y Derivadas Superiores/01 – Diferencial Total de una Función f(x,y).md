# 📘 Diferencial Total de una Función f(x,y)

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante el Diferencial Total?
> 
> El diferencial total es un concepto fundamental que nos permite **aproximar el cambio** en una función cuando sus variables cambian simultáneamente.
> 
> **Importancia práctica:**
> 
> - **Física:** Propagación de errores en mediciones
> - **Ingeniería:** Análisis de sensibilidad de sistemas
> - **Economía:** Cambios marginales en funciones de producción
> - **Computación:** Algoritmos de optimización (gradiente descendente)
> 
> **Diferencia con una variable:**
> 
> - En $f(x)$: $df = f'(x)dx$ (un solo término)
> - En $f(x,y)$: $df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$ (suma de contribuciones)
> 
> **Nueva perspectiva:** El diferencial total captura cómo **cada variable contribuye independientemente** al cambio total de la función.

---

## 📐 Definición del Diferencial Total

### 📋 Definición Formal

> [!example]- 🟢 Definición: Diferencial Total
> 
> **Definición formal:** Sea $f: D \subseteq \mathbb{R}^2 \to \mathbb{R}$ una función diferenciable en un punto $(x_0, y_0)$.
> 
> El **diferencial total** de $f$ en $(x_0, y_0)$ es:
> 
> $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$
> 
> donde:
> 
> - $\frac{\partial f}{\partial x}$ es la derivada parcial respecto a $x$ evaluada en $(x_0, y_0)$
> - $\frac{\partial f}{\partial y}$ es la derivada parcial respecto a $y$ evaluada en $(x_0, y_0)$
> - $dx$ y $dy$ son los **diferenciales** (cambios infinitesimales) en $x$ e $y$
> 
> ---
> 
> **Notación alternativa:**
> 
> $$df = f_x(x_0, y_0)dx + f_y(x_0, y_0)dy$$
> 
> donde $f_x$ y $f_y$ denotan las derivadas parciales.
> 
> ---
> 
> **Interpretación geométrica:**
> 
> El diferencial total representa el **cambio aproximado** en $f$ cuando nos movemos desde $(x_0, y_0)$ hasta $(x_0 + dx, y_0 + dy)$:
> 
> $$\Delta f \approx df$$
> 
> donde $\Delta f = f(x_0 + dx, y_0 + dy) - f(x_0, y_0)$ es el cambio **real**.

### 🎯 Interpretación Intuitiva

> [!note]- 💭 Interpretación Práctica
> 
> **El diferencial total nos dice:**
> 
> ✅ "Cuánto cambia $f$ cuando $x$ cambia en $dx$ Y $y$ cambia en $dy$"
> 
> ✅ "La contribución de cada variable al cambio total"
> 
> ✅ "Una aproximación lineal al cambio verdadero en $f$"
> 
> ---
> 
> **Analogía física:**
> 
> Imagina que $f(x,y)$ representa la **temperatura** en un punto $(x,y)$ de una placa:
> 
> - Si te mueves $dx$ en dirección $x$: la temperatura cambia aproximadamente $\frac{\partial f}{\partial x}dx$
> - Si te mueves $dy$ en dirección $y$: la temperatura cambia aproximadamente $\frac{\partial f}{\partial y}dy$
> - **Movimiento simultáneo:** el cambio total es la **suma** de ambas contribuciones
> 
> ---
> 
> **Ejemplo numérico:**
> 
> Si $f(x,y) = x^2 + 3xy$, entonces:
> 
> $$df = (2x + 3y)dx + 3xdy$$
> 
> En el punto $(2, 1)$:
> 
> $$df = (2(2) + 3(1))dx + 3(2)dy = 7dx + 6dy$$
> 
> **Interpretación:** Si $x$ aumenta en $0.1$ (dx = 0.1) y $y$ aumenta en $0.05$ (dy = 0.05):
> 
> $$df \approx 7(0.1) + 6(0.05) = 0.7 + 0.3 = 1.0$$
> 
> La función aumentará aproximadamente en $1.0$ unidad.

---

## 🧮 Fórmula General y Propiedades

### 📊 Fórmula para Funciones de Varias Variables

> [!example]- 🔢 Generalización a n Variables
> 
> Para una función $f(x_1, x_2, \ldots, x_n)$ diferenciable:
> 
> $$df = \frac{\partial f}{\partial x_1}dx_1 + \frac{\partial f}{\partial x_2}dx_2 + \cdots + \frac{\partial f}{\partial x_n}dx_n$$
> 
> **Notación compacta:**
> 
> $$df = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i}dx_i$$
> 
> ---
> 
> **Casos particulares:**
> 
> **Una variable:** $f(x)$ $$df = f'(x)dx$$
> 
> **Dos variables:** $f(x,y)$ $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$
> 
> **Tres variables:** $f(x,y,z)$ $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz$$
> 
> ---
> 
> **Interpretación vectorial:**
> 
> El diferencial total puede escribirse como producto punto:
> 
> $$df = \nabla f \cdot d\vec{r}$$
> 
> donde:
> 
> - $\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$ es el **gradiente**
> - $d\vec{r} = (dx, dy)$ es el **vector desplazamiento infinitesimal**

### 🔧 Propiedades Algebraicas

> [!note]- 🟢 Propiedades del Diferencial Total
> 
> Si $f$ y $g$ son funciones diferenciables y $c$ es una constante:
> 
> ### 1. Linealidad
> 
> $$d(f + g) = df + dg$$ $$d(cf) = c \cdot df$$
> 
> **Demostración:** $$d(f + g) = \frac{\partial(f+g)}{\partial x}dx + \frac{\partial(f+g)}{\partial y}dy$$ $$= \left(\frac{\partial f}{\partial x} + \frac{\partial g}{\partial x}\right)dx + \left(\frac{\partial f}{\partial y} + \frac{\partial g}{\partial y}\right)dy$$ $$= \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial g}{\partial x}dx + \frac{\partial g}{\partial y}dy = df + dg$$
> 
> ---
> 
> ### 2. Regla del Producto
> 
> $$d(fg) = f \cdot dg + g \cdot df$$
> 
> **Ejemplo:** Si $h(x,y) = f(x,y) \cdot g(x,y)$: $$dh = f \cdot dg + g \cdot df$$
> 
> ---
> 
> ### 3. Regla del Cociente
> 
> $$d\left(\frac{f}{g}\right) = \frac{g \cdot df - f \cdot dg}{g^2}$$
> 
> (válida donde $g \neq 0$)
> 
> ---
> 
> ### 4. Regla de la Cadena
> 
> Si $z = f(x,y)$ donde $x = x(t)$ y $y = y(t)$:
> 
> $$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$
> 
> ---
> 
> ### 5. Diferencial de una Constante
> 
> $$d(c) = 0$$
> 
> Si $f(x,y) = k$ (constante), entonces $df = 0$.
> 
> ---
> 
> ### 6. Diferencial de la Variable Independiente
> 
> $$d(x) = dx$$ $$d(y) = dy$$

---

## 📚 Ejemplos Detallados

### Ejemplo 1: Función Polinomial Simple

> [!example]- 📝 Ejemplo 1: Calcular el Diferencial Total
> 
> **Función:** $$f(x,y) = x^2 + 3xy + y^2$$
> 
> **Paso 1:** Calcular derivadas parciales
> 
> $$\frac{\partial f}{\partial x} = 2x + 3y$$ $$\frac{\partial f}{\partial y} = 3x + 2y$$
> 
> **Paso 2:** Escribir el diferencial total
> 
> $$df = (2x + 3y)dx + (3x + 2y)dy$$
> 
> ---
> 
> **Evaluación en un punto específico:** En $(x_0, y_0) = (1, 2)$:
> 
> $$\frac{\partial f}{\partial x}\bigg|_{(1,2)} = 2(1) + 3(2) = 8$$ $$\frac{\partial f}{\partial y}\bigg|_{(1,2)} = 3(1) + 2(2) = 7$$
> 
> $$df|_{(1,2)} = 8dx + 7dy$$
> 
> ---
> 
> **Aplicación numérica:** Si $dx = 0.1$ y $dy = -0.05$:
> 
> $$df \approx 8(0.1) + 7(-0.05) = 0.8 - 0.35 = 0.45$$
> 
> **Verificación del cambio real:**
> 
> $$f(1, 2) = 1 + 6 + 4 = 11$$ $$f(1.1, 1.95) = (1.1)^2 + 3(1.1)(1.95) + (1.95)^2 = 1.21 + 6.435 + 3.8025 = 11.4475$$ $$\Delta f = 11.4475 - 11 = 0.4475$$
> 
> El diferencial $df = 0.45$ es una **excelente aproximación** del cambio real $\Delta f = 0.4475$ ✓

### Ejemplo 2: Función con Exponencial

> [!example]- 📝 Ejemplo 2: Función Exponencial
> 
> **Función:** $$f(x,y) = e^{x+y}$$
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial f}{\partial x} = e^{x+y}$$ $$\frac{\partial f}{\partial y} = e^{x+y}$$
> 
> **Diferencial total:**
> 
> $$df = e^{x+y}dx + e^{x+y}dy = e^{x+y}(dx + dy)$$
> 
> ---
> 
> **Observación importante:** Podemos factorizar:
> 
> $$df = f(x,y)(dx + dy)$$
> 
> **En el punto $(0, 0)$:**
> 
> $$f(0,0) = e^0 = 1$$ $$df|_{(0,0)} = 1 \cdot (dx + dy) = dx + dy$$
> 
> ---
> 
> **Interpretación:** En el origen, el cambio en $f$ es simplemente la suma de los cambios en $x$ e $y$.

### Ejemplo 3: Función Trigonométrica

> [!example]- 📝 Ejemplo 3: Funciones Trigonométricas
> 
> **Función:** $$f(x,y) = \sin(x)\cos(y)$$
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial f}{\partial x} = \cos(x)\cos(y)$$ $$\frac{\partial f}{\partial y} = -\sin(x)\sin(y)$$
> 
> **Diferencial total:**
> 
> $$df = \cos(x)\cos(y)dx - \sin(x)\sin(y)dy$$
> 
> ---
> 
> **En el punto $(\pi/4, \pi/3)$:**
> 
> $$\frac{\partial f}{\partial x}\bigg|_{(\pi/4,\pi/3)} = \cos(\pi/4)\cos(\pi/3) = \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{2}}{4}$$
> 
> $$\frac{\partial f}{\partial y}\bigg|_{(\pi/4,\pi/3)} = -\sin(\pi/4)\sin(\pi/3) = -\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} = -\frac{\sqrt{6}}{4}$$
> 
> $$df\bigg|_{(\pi/4,\pi/3)} = \frac{\sqrt{2}}{4}dx - \frac{\sqrt{6}}{4}dy$$

### Ejemplo 4: Función Racional

> [!example]- 📝 Ejemplo 4: Cociente de Funciones
> 
> **Función:** $$f(x,y) = \frac{x}{y}$$
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial f}{\partial x} = \frac{1}{y}$$ $$\frac{\partial f}{\partial y} = -\frac{x}{y^2}$$
> 
> **Diferencial total:**
> 
> $$df = \frac{1}{y}dx - \frac{x}{y^2}dy$$
> 
> Factorizando:
> 
> $$df = \frac{1}{y}\left(dx - \frac{x}{y}dy\right) = \frac{ydx - xdy}{y^2}$$
> 
> ---
> 
> **Verificación usando regla del cociente:**
> 
> Si escribimos $f = \frac{u}{v}$ donde $u = x$ y $v = y$:
> 
> $$du = dx, \quad dv = dy$$
> 
> $$df = \frac{v \cdot du - u \cdot dv}{v^2} = \frac{y \cdot dx - x \cdot dy}{y^2}$$ ✓

### Ejemplo 5: Función Implícita

> [!example]- 📝 Ejemplo 5: Relación Implícita
> 
> **Ecuación implícita:** $$x^2 + y^2 = 25$$
> 
> Podemos escribir esto como $f(x,y) = x^2 + y^2 - 25 = 0$
> 
> **Diferencial total:**
> 
> $$df = 2xdx + 2ydy = 0$$
> 
> (El diferencial es cero porque $f$ es constante)
> 
> ---
> 
> **Despejando $dy/dx$:**
> 
> $$2xdx + 2ydy = 0$$ $$2ydy = -2xdx$$ $$\frac{dy}{dx} = -\frac{x}{y}$$
> 
> Esta es la **derivada implícita** de la circunferencia.
> 
> ---
> 
> **Interpretación geométrica:** En cualquier punto $(x_0, y_0)$ de la circunferencia, si nos movemos de tal forma que permanecemos en la circunferencia, entonces:
> 
> $$2x_0dx + 2y_0dy = 0$$
> 
> Esto define la **dirección tangente** a la circunferencia.

### Ejemplo 6: Función Compuesta

> [!example]- 📝 Ejemplo 6: Composición de Funciones
> 
> **Función:** $$f(x,y) = \ln(x^2 + y^2)$$
> 
> **Usando regla de la cadena:**
> 
> Sea $u = x^2 + y^2$, entonces $f = \ln(u)$
> 
> $$\frac{\partial f}{\partial x} = \frac{1}{u}\frac{\partial u}{\partial x} = \frac{1}{x^2+y^2} \cdot 2x = \frac{2x}{x^2+y^2}$$
> 
> $$\frac{\partial f}{\partial y} = \frac{1}{u}\frac{\partial u}{\partial y} = \frac{1}{x^2+y^2} \cdot 2y = \frac{2y}{x^2+y^2}$$
> 
> **Diferencial total:**
> 
> $$df = \frac{2x}{x^2+y^2}dx + \frac{2y}{x^2+y^2}dy$$
> 
> Factorizando:
> 
> $$df = \frac{2(xdx + ydy)}{x^2+y^2}$$
> 
> ---
> 
> **Nota importante:** Observe que $xdx + ydy = \frac{1}{2}d(x^2 + y^2)$, por lo que:
> 
> $$df = \frac{d(x^2 + y^2)}{x^2 + y^2} = d(\ln(x^2 + y^2))$$ ✓

### Ejemplo 7: Función de Tres Variables

> [!example]- 📝 Ejemplo 7: Extensión a Tres Dimensiones
> 
> **Función:** $$f(x,y,z) = xyz$$
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial f}{\partial x} = yz$$ $$\frac{\partial f}{\partial y} = xz$$ $$\frac{\partial f}{\partial z} = xy$$
> 
> **Diferencial total:**
> 
> $$df = yzdx + xzdy + xydz$$
> 
> ---
> 
> **En el punto $(2, 3, 1)$:**
> 
> $$df|_{(2,3,1)} = 3(1)dx + 2(1)dy + 2(3)dz = 3dx + 2dy + 6dz$$
> 
> ---
> 
> **Aplicación:** Si $dx = 0.1$, $dy = -0.05$, $dz = 0.02$:
> 
> $$df \approx 3(0.1) + 2(-0.05) + 6(0.02) = 0.3 - 0.1 + 0.12 = 0.32$$

---

## 🔬 Aplicación: Propagación de Errores

### 📏 Análisis de Errores en Mediciones

> [!tip]- ⚠️ Propagación de Errores
> 
> Cuando medimos variables experimentales con cierto error, el diferencial total nos permite estimar el **error en el resultado**.
> 
> **Fórmula general:**
> 
> Si $z = f(x,y)$ y tenemos errores $\Delta x$ y $\Delta y$ en las mediciones:
> 
> $$\Delta z \approx df = \frac{\partial f}{\partial x}\Delta x + \frac{\partial f}{\partial y}\Delta y$$
> 
> **Error máximo absoluto:**
> 
> $$|\Delta z|_{\text{max}} \approx \left|\frac{\partial f}{\partial x}\right||\Delta x| + \left|\frac{\partial f}{\partial y}\right||\Delta y|$$
> 
> (tomamos valor absoluto de cada término)
> 
> ---
> 
> **Error relativo:**
> 
> $$\frac{|\Delta z|}{|z|} \approx \frac{1}{|f|}\left(\left|\frac{\partial f}{\partial x}\right||\Delta x| + \left|\frac{\partial f}{\partial y}\right||\Delta y|\right)$$

### Ejemplo 8: Error en el Área de un Rectángulo

> [!example]- 📝 Ejemplo 8: Propagación de Errores
> 
> **Problema:** Se mide un rectángulo con lados $x = 10$ cm y $y = 15$ cm, cada uno con un error de $\pm 0.1$ cm. ¿Cuál es el error aproximado en el área?
> 
> **Solución:**
> 
> **Función:** $A(x,y) = xy$
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial A}{\partial x} = y = 15$$ $$\frac{\partial A}{\partial y} = x = 10$$
> 
> **Diferencial total:**
> 
> $$dA = 15dx + 10dy$$
> 
> ---
> 
> **Error máximo:**
> 
> Con $|\Delta x| = |\Delta y| = 0.1$ cm:
> 
> $$|\Delta A|_{\text{max}} \approx 15(0.1) + 10(0.1) = 1.5 + 1.0 = 2.5 \text{ cm}^2$$
> 
> ---
> 
> **Área medida:**
> 
> $$A = 10 \times 15 = 150 \text{ cm}^2$$
> 
> **Error relativo:**
> 
> $\frac{|\Delta A|}{A} \approx \frac{2.5}{150} = 0.0167 \approx 1.67%$$
> 
> **Conclusión:** El área es $150 \pm 2.5$ cm² (error del 1.67%)
> 

### Ejemplo 9: Error en el Volumen de un Cilindro

> [!example]- 📝 Ejemplo 9: Cilindro con Errores
> 
> **Problema:** Un cilindro tiene radio $r = 5$ cm (error $\pm 0.05$ cm) y altura $h = 20$ cm (error $\pm 0.1$ cm). Estimar el error en el volumen.
> 
> **Función:** $$V(r,h) = \pi r^2 h$$
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial V}{\partial r} = 2\pi rh$$ $$\frac{\partial V}{\partial h} = \pi r^2$$
> 
> ---
> 
> **En $r = 5$, $h = 20$:**
> 
> $$\frac{\partial V}{\partial r}\bigg|_{(5,20)} = 2\pi(5)(20) = 200\pi$$ $$\frac{\partial V}{\partial h}\bigg|_{(5,20)} = \pi(5)^2 = 25\pi$$
> 
> **Diferencial:**
> 
> $$dV = 200\pi \cdot dr + 25\pi \cdot dh$$
> 
> ---
> 
> **Error máximo:**
> 
> $$|\Delta V|_{\text{max}} \approx 200\pi(0.05) + 25\pi(0.1)$$ $$= 10\pi + 2.5\pi = 12.5\pi \approx 39.27 \text{ cm}^3$$
> 
> ---
> 
> **Volumen medido:**
> 
> $V = \pi(5)^2(20) = 500\pi \approx 1570.8 \text{ cm}^3$
> 
> **Error relativo:**
> 
> $\frac{|\Delta V|}{V} = \frac{12.5\pi}{500\pi} = 0.025 = 2.5%$
> $
> 

---

## 🎨 Interpretación Geométrica

### 📊 Visualización del Diferencial Total

> [!note]- 🖼️ Interpretación Geométrica
> 
> ### Plano Tangente
> 
> Para una función $z = f(x,y)$, el diferencial total en un punto $(x_0, y_0)$ representa la **ecuación del plano tangente** a la superficie en ese punto.
> 
> **Ecuación del plano tangente:**
> 
> $$z - z_0 = \frac{\partial f}{\partial x}\bigg|_{(x_0,y_0)}(x - x_0) + \frac{\partial f}{\partial y}\bigg|_{(x_0,y_0)}(y - y_0)$$
> 
> Usando diferenciales: $dz = z - z_0$, $dx = x - x_0$, $dy = y - y_0$:
> 
> $$dz = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$
> 
> ---
> 
> ### Aproximación Lineal
> 
> ```
>         z
>         |     /|  ← Superficie real z = f(x,y)
>         |    / |
>         |   /  |  ← Plano tangente (aproximación lineal)
>         |  /   o (x₀,y₀,z₀)
>         | /___/
>         +-------- y
>        /
>       x
> ```
> 
> El diferencial $dz$ representa el **cambio vertical en el plano tangente**, mientras que $\Delta z$ es el cambio en la superficie real.
> 
> ---
> 
> ### Vector Gradiente
> 
> El diferencial total está relacionado con el **gradiente**:
> 
> $$df = \nabla f \cdot d\vec{r}$$
> 
> donde:
> 
> - $\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$ apunta en la dirección de máximo crecimiento
> - $d\vec{r} = (dx, dy)$ es el desplazamiento
> 
> **Interpretación:** El cambio en $f$ es la **proyección** del gradiente sobre la dirección del desplazamiento.

---

## 🔄 Diferencial Total en Coordenadas Polares

### 🌀 Transformación de Coordenadas

> [!example]- 🔄 Diferenciales en Polares
> 
> **Transformación:**
> 
> $$\begin{cases} x = r\cos\theta \ y = r\sin\theta \end{cases}$$
> 
> **Diferenciales de las coordenadas cartesianas:**
> 
> $$dx = \cos\theta , dr - r\sin\theta , d\theta$$ $$dy = \sin\theta , dr + r\cos\theta , d\theta$$
> 
> ---
> 
> **Para una función $f(x,y)$:**
> 
> En coordenadas cartesianas: $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$
> 
> En coordenadas polares (sustituyendo): $$df = \frac{\partial f}{\partial x}(\cos\theta , dr - r\sin\theta , d\theta) + \frac{\partial f}{\partial y}(\sin\theta , dr + r\cos\theta , d\theta)$$
> 
> Reagrupando: $$df = \left(\frac{\partial f}{\partial x}\cos\theta + \frac{\partial f}{\partial y}\sin\theta\right)dr + \left(-\frac{\partial f}{\partial x}r\sin\theta + \frac{\partial f}{\partial y}r\cos\theta\right)d\theta$$
> 
> ---
> 
> **Alternativamente:** Si expresamos $f$ directamente en polares como $f(r,\theta)$:
> 
> $$df = \frac{\partial f}{\partial r}dr + \frac{\partial f}{\partial \theta}d\theta$
> 
> **Calculando derivadas parciales:**
> 
> $\frac{\partial f}{\partial r} = 2r$ $\frac{\partial f}{\partial \theta} = 0$
> 
> **Diferencial total:**
> 
> $df = 2r , dr$
> 
> ---
> 
> **Interpretación:** La función $r^2$ **no depende** de $\theta$ (es radialmente simétrica), por lo que el diferencial solo tiene componente radial.
> 
> **En el punto $(r, \theta) = (3, \pi/4)$:**
> 
> $df = 2(3)dr = 6dr$
> 
> Si $dr = 0.1$: $df \approx 0.6$
> $$

---

## 🧩 Aplicaciones Adicionales

### 💼 Aplicación en Economía

> [!tip]- 💰 Funciones de Producción
> 
> **Función de producción Cobb-Douglas:**
> 
> $P(K, L) = AK^{\alpha}L^{\beta}$
> 
> donde:
> 
> - $P$ = producción
> - $K$ = capital
> - $L$ = trabajo
> - $A, \alpha, \beta$ = constantes
> 
> **Diferencial total:**
> 
> $dP = \frac{\partial P}{\partial K}dK + \frac{\partial P}{\partial L}dL$
> 
> $dP = A\alpha K^{\alpha-1}L^{\beta}dK + A\beta K^{\alpha}L^{\beta-1}dL$
> 
> ---
> 
> **Interpretación económica:**
> 
> - $\frac{\partial P}{\partial K}$ = **productividad marginal del capital**
> - $\frac{\partial P}{\partial L}$ = **productividad marginal del trabajo**
> - $dP$ = cambio en producción por cambios $dK$ y $dL$
> 
> ---
> 
> **Ejemplo numérico:**
> 
> Si $P(K,L) = 10K^{0.3}L^{0.7}$ con $K = 100$, $L = 50$:
> 
> $\frac{\partial P}{\partial K} = 3K^{-0.7}L^{0.7} = 3(100)^{-0.7}(50)^{0.7} \approx 0.75$ $\frac{\partial P}{\partial L} = 7K^{0.3}L^{-0.3} = 7(100)^{0.3}(50)^{-0.3} \approx 3.5$
> 
> Si aumentamos capital en $\Delta K = 5$ y trabajo en $\Delta L = 2$:
> 
> $\Delta P \approx 0.75(5) + 3.5(2) = 3.75 + 7 = 10.75 \text{ unidades}$

### 🌡️ Aplicación en Termodinámica

> [!tip]- 🔥 Primera Ley de la Termodinámica
> 
> **Energía interna de un gas ideal:**
> 
> $U = U(T, V)$
> 
> donde $T$ = temperatura, $V$ = volumen
> 
> **Primera ley:**
> 
> $dU = dQ - dW$
> 
> donde:
> 
> - $dQ$ = calor añadido al sistema
> - $dW$ = trabajo realizado por el sistema
> 
> ---
> 
> **Usando diferencial total:**
> 
> $dU = \frac{\partial U}{\partial T}dT + \frac{\partial U}{\partial V}dV$
> 
> $dU = C_V dT + \left[\left(\frac{\partial U}{\partial V}\right)_T\right]dV$
> 
> donde $C_V$ es la **capacidad calorífica a volumen constante**.
> 
> ---
> 
> **Para un gas ideal:** $U$ depende solo de $T$, no de $V$:
> 
> $dU = C_V dT$

### 🔬 Aplicación en Física: Ley de los Gases Ideales

> [!example]- 📝 Ejemplo 11: Gases Ideales
> 
> **Ecuación de estado:** $PV = nRT$
> 
> donde $P$ = presión, $V$ = volumen, $T$ = temperatura, $n$ = moles, $R$ = constante
> 
> **Diferencial total (con $n$ constante):**
> 
> $d(PV) = d(nRT)$ $PdV + VdP = nRdT$
> 
> ---
> 
> **Procesos especiales:**
> 
> **1. Proceso isotérmico** ($dT = 0$): $PdV + VdP = 0$ $\frac{dP}{P} = -\frac{dV}{V}$
> 
> **2. Proceso isobárico** ($dP = 0$): $PdV = nRdT$
> 
> **3. Proceso isocórico** ($dV = 0$): $VdP = nRdT$

---

## 🎯 Aproximaciones y Cálculos Numéricos

### 📐 Aproximación Lineal

> [!tip]- ✅ Fórmula de Aproximación
> 
> **Fórmula general:**
> 
> Para calcular $f(x_0 + \Delta x, y_0 + \Delta y)$ conociendo $f(x_0, y_0)$:
> 
> $f(x_0 + \Delta x, y_0 + \Delta y) \approx f(x_0, y_0) + df$
> 
> $f(x_0 + \Delta x, y_0 + \Delta y) \approx f(x_0, y_0) + \frac{\partial f}{\partial x}\bigg|_{(x_0,y_0)}\Delta x + \frac{\partial f}{\partial y}\bigg|_{(x_0,y_0)}\Delta y$
> 
> ---
> 
> **Condición de validez:**
> 
> Esta aproximación es **buena** cuando $\Delta x$ y $\Delta y$ son **pequeños**.
> 
> **Error de aproximación:**
> 
> $\text{Error} = f(x_0 + \Delta x, y_0 + \Delta y) - [f(x_0, y_0) + df]$
> 
> El error es del orden $O(\Delta x^2, \Delta y^2, \Delta x \Delta y)$ (términos cuadráticos).

### Ejemplo 12: Aproximación de una Raíz

> [!example]- 📝 Ejemplo 12: Calcular $\sqrt{(4.02)^2 + (2.97)^2}$
> 
> **Función:** $f(x,y) = \sqrt{x^2 + y^2}$
> 
> **Punto base:** $(x_0, y_0) = (4, 3)$
> 
> **Valor exacto en el punto base:** $f(4, 3) = \sqrt{16 + 9} = \sqrt{25} = 5$
> 
> ---
> 
> **Derivadas parciales:**
> 
> $\frac{\partial f}{\partial x} = \frac{x}{\sqrt{x^2 + y^2}}$ $\frac{\partial f}{\partial y} = \frac{y}{\sqrt{x^2 + y^2}}$
> 
> **En $(4, 3)$:**
> 
> $\frac{\partial f}{\partial x}\bigg|_{(4,3)} = \frac{4}{5} = 0.8$ $\frac{\partial f}{\partial y}\bigg|_{(4,3)} = \frac{3}{5} = 0.6$
> 
> ---
> 
> **Cambios:** $\Delta x = 4.02 - 4 = 0.02$ $\Delta y = 2.97 - 3 = -0.03$
> 
> **Aproximación:**
> 
> $f(4.02, 2.97) \approx 5 + 0.8(0.02) + 0.6(-0.03)$ $\approx 5 + 0.016 - 0.018 = 4.998$
> 
> ---
> 
> **Valor real:** $\sqrt{(4.02)^2 + (2.97)^2} = \sqrt{16.1604 + 8.8209} = \sqrt{24.9813} \approx 4.9981$
> 
> **Error:** $|4.998 - 4.9981| = 0.0001$ (¡excelente aproximación!)

### Ejemplo 13: Aproximación de Función Exponencial

> [!example]- 📝 Ejemplo 13: Calcular $e^{0.02}\cos(0.03)$
> 
> **Función:** $f(x,y) = e^x\cos(y)$
> 
> **Punto base:** $(x_0, y_0) = (0, 0)$
> 
> $f(0, 0) = e^0\cos(0) = 1 \cdot 1 = 1$
> 
> ---
> 
> **Derivadas parciales:**
> 
> $\frac{\partial f}{\partial x} = e^x\cos(y)$ $\frac{\partial f}{\partial y} = -e^x\sin(y)$
> 
> **En $(0, 0)$:**
> 
> $\frac{\partial f}{\partial x}\bigg|_{(0,0)} = 1 \cdot 1 = 1$ $\frac{\partial f}{\partial y}\bigg|_{(0,0)} = -1 \cdot 0 = 0$
> 
> ---
> 
> **Aproximación:**
> 
> $f(0.02, 0.03) \approx 1 + 1(0.02) + 0(0.03) = 1.02$
> 
> **Valor real:** $e^{0.02}\cos(0.03) \approx 1.0202 \cdot 0.9996 \approx 1.0198$
> 
> **Error relativo:** $\frac{|1.02 - 1.0198|}{1.0198} \approx 0.02%$
> $

---

## 🔍 Diferenciabilidad y Diferencial Total

### 📋 Relación con Diferenciabilidad

> [!note]- 🟢 Condición de Diferenciabilidad
> 
> **Definición:** Una función $f(x,y)$ es **diferenciable** en $(x_0, y_0)$ si existe el diferencial total y satisface:
> 
> $\Delta f = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0) = df + \varepsilon_1\Delta x + \varepsilon_2\Delta y$
> 
> donde $\varepsilon_1, \varepsilon_2 \to 0$ cuando $(\Delta x, \Delta y) \to (0, 0)$.
> 
> **En otras palabras:**
> 
> $\lim_{(\Delta x, \Delta y) \to (0,0)} \frac{|\Delta f - df|}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} = 0$
> 
> ---
> 
> **Teorema:** Si las derivadas parciales $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$ existen y son **continuas** en una vecindad de $(x_0, y_0)$, entonces $f$ es diferenciable en $(x_0, y_0)$.
> 
> ---
> 
> **Implicaciones:**
> 
> $\text{Diferenciable} \implies \text{Continua}$ $\text{Diferenciable} \implies \text{Existen derivadas parciales}$
> 
> Pero:
> 
> $\text{Existen derivadas parciales} \not!!!\implies \text{Diferenciable}$

### Ejemplo 14: Función No Diferenciable

> [!example]- 📝 Ejemplo 14: Derivadas Parciales Existen pero No Diferenciable
> 
> **Función:**
> 
> $f(x,y) = \begin{cases} \frac{xy}{\sqrt{x^2 + y^2}} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$
> 
> **Derivadas parciales en el origen:**
> 
> $\frac{\partial f}{\partial x}\bigg|_{(0,0)} = \lim_{h \to 0} \frac{f(h, 0) - f(0, 0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$
> 
> $\frac{\partial f}{\partial y}\bigg|_{(0,0)} = \lim_{h \to 0} \frac{f(0, h) - f(0, 0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$
> 
> Ambas derivadas parciales **existen** y son 0.
> 
> ---
> 
> **¿Es diferenciable?**
> 
> Si fuera diferenciable, el diferencial sería $df = 0 \cdot dx + 0 \cdot dy = 0$.
> 
> Verificamos la condición:
> 
> Por el camino $y = x$:
> 
> $f(h, h) = \frac{h \cdot h}{\sqrt{h^2 + h^2}} = \frac{h^2}{\sqrt{2h^2}} = \frac{h^2}{|h|\sqrt{2}} = \frac{|h|}{\sqrt{2}}$
> 
> $\frac{|f(h,h) - 0|}{\sqrt{h^2 + h^2}} = \frac{|h|/\sqrt{2}}{\sqrt{2}|h|} = \frac{1}{2} \not\to 0$
> 
> **Conclusión:** La función **NO es diferenciable** en el origen, aunque las derivadas parciales existen.

---

## 📊 Tabla Resumen: Diferencial de Funciones Comunes

> [!note]- 📋 Catálogo de Diferenciales
> 
> |Función $f(x,y)$|Diferencial $df$|
> |---|---|
> |$c$ (constante)|$0$|
> |$x$|$dx$|
> |$y$|$dy$|
> |$ax + by$|$a , dx + b , dy$|
> |$x^2 + y^2$|$2x , dx + 2y , dy$|
> |$xy$|$y , dx + x , dy$|
> |$x^2y$|$2xy , dx + x^2 , dy$|
> |$\frac{x}{y}$|$\frac{1}{y}dx - \frac{x}{y^2}dy$|
> |$x^n$|$nx^{n-1}dx$|
> |$e^{x+y}$|$e^{x+y}(dx + dy)$|
> |$e^{xy}$|$ye^{xy}dx + xe^{xy}dy$|
> |$\ln(x)$|$\frac{1}{x}dx$|
> |$\ln(xy)$|$\frac{1}{x}dx + \frac{1}{y}dy$|
> |$\ln(x^2 + y^2)$|$\frac{2x , dx + 2y , dy}{x^2 + y^2}$|
> |$\sin(x + y)$|$\cos(x+y)(dx + dy)$|
> |$\sin(x)\cos(y)$|$\cos(x)\cos(y)dx - \sin(x)\sin(y)dy$|
> |$\sqrt{x^2 + y^2}$|$\frac{x , dx + y , dy}{\sqrt{x^2 + y^2}}$|
> |$x^y$|$yx^{y-1}dx + x^y\ln(x)dy$|

---

## 🎓 Ejercicios Propuestos

### Nivel Básico

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular el diferencial total de las siguientes funciones:**
> 
> a) $f(x,y) = 3x^2 + 4y^2$
> 
> b) $f(x,y) = 2xy + x - 3y$
> 
> c) $f(x,y) = x^3y^2$
> 
> d) $f(x,y) = e^{2x+y}$
> 
> e) $f(x,y) = \ln(x + 2y)$
> 
> ---
> 
> **2. Evaluar el diferencial en el punto indicado:**
> 
> a) $f(x,y) = x^2 + xy + y^2$ en $(1, 2)$
> 
> b) $f(x,y) = \sin(x)\cos(y)$ en $(\pi/2, 0)$
> 
> c) $f(x,y) = \frac{x}{y}$ en $(4, 2)$
> 
> ---
> 
> **3. Aproximar usando el diferencial total:**
> 
> a) $f(2.01, 2.98)$ si $f(x,y) = x^2 + y^2$
> 
> b) $(1.98)^3(3.02)$ usando $f(x,y) = x^3y$
> 
> c) $\sqrt{(3.97)^2 + (5.03)^2}$

### Nivel Intermedio

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Propagación de errores:**
> 
> a) La base de un triángulo es $b = 10 \pm 0.1$ cm y la altura es $h = 8 \pm 0.05$ cm. Estimar el error en el área.
> 
> b) Se mide la resistencia de dos resistores: $R_1 = 100 \pm 2$ Ω y $R_2 = 150 \pm 3$ Ω. Si están en paralelo ($\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}$), estimar el error en $R$.
> 
> c) El radio de un cono es $r = 5 \pm 0.1$ cm y la altura $h = 12 \pm 0.2$ cm. Estimar el error en el volumen $V = \frac{1}{3}\pi r^2 h$.
> 
> ---
> 
> **5. Funciones implícitas:**
> 
> a) Para $x^2 + xy + y^2 = 7$, usar el diferencial total para encontrar $\frac{dy}{dx}$
> 
> b) En la elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, encontrar $dy/dx$ usando diferenciales
> 
> ---
> 
> **6. Tres variables:**
> 
> a) Calcular $df$ para $f(x,y,z) = x^2yz + xy^2z^2$
> 
> b) Para $f(x,y,z) = e^{xyz}$, evaluar $df$ en $(1, 0, 2)$

### Nivel Avanzado

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Coordenadas polares:**
> 
> a) Expresar $df$ en coordenadas polares para $f(x,y) = \ln(x^2 + y^2)$
> 
> b) Si $f(r,\theta) = r^2\sin(2\theta)$, calcular $df$ y luego expresarlo en coordenadas cartesianas
> 
> ---
> 
> **8. Aplicaciones físicas:**
> 
> a) La ley de gases ideales es $PV = nRT$. Con $n$ constante, expresar $dP$ en términos de $dV$ y $dT$.
> 
> b) La energía cinética de un objeto es $E = \frac{1}{2}mv^2$. Si $m = 10 \pm 0.1$ kg y $v = 20 \pm 0.5$ m/s, estimar el error en $E$.
> 
> ---
> 
> **9. Diferenciabilidad:**
> 
> a) Verificar si $f(x,y) = \begin{cases} \frac{x^2y}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$ es diferenciable en el origen.
> 
> b) Demostrar que si $f$ es diferenciable en $(x_0, y_0)$, entonces es continua en ese punto.
> 
> ---
> 
> **10. Problemas de optimización:**
> 
> a) Una caja rectangular tiene dimensiones $x$, $y$, $z$ con volumen $V = xyz = 1000$ cm³. Si queremos minimizar el área superficial $S = 2(xy + xz + yz)$, usar $dS = 0$ con la restricción $dV = 0$ para encontrar las dimensiones óptimas.

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = 3x^2 + 4y^2$
> 
> $df = 6x , dx + 8y , dy$
> 
> ---
> 
> **1b)** $f(x,y) = 2xy + x - 3y$
> 
> $df = (2y + 1)dx + (2x - 3)dy$
> 
> ---
> 
> **1d)** $f(x,y) = e^{2x+y}$
> 
> $df = 2e^{2x+y}dx + e^{2x+y}dy = e^{2x+y}(2dx + dy)$
> 
> ---
> 
> **2a)** $f(x,y) = x^2 + xy + y^2$ en $(1, 2)$
> 
> $\frac{\partial f}{\partial x} = 2x + y \bigg|_{(1,2)} = 4$ $\frac{\partial f}{\partial y} = x + 2y \bigg|_{(1,2)} = 5$
> 
> $df|_{(1,2)} = 4dx + 5dy$
> 
> ---
> 
> **3a)** $f(2.01, 2.98)$ donde $f(x,y) = x^2 + y^2$
> 
> Punto base: $(2, 3)$, $f(2,3) = 4 + 9 = 13$
> 
> $df = 2x , dx + 2y , dy = 2(2)(0.01) + 2(3)(-0.02)$ $= 0.04 - 0.12 = -0.08$
> 
> $f(2.01, 2.98) \approx 13 - 0.08 = 12.92$
> 
> Valor real: $(2.01)^2 + (2.98)^2 = 4.0401 + 8.8804 = 12.9205$ ✓

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** Área del triángulo: $A = \frac{1}{2}bh$
> 
> $dA = \frac{1}{2}h , db + \frac{1}{2}b , dh = \frac{1}{2}(8)(0.1) + \frac{1}{2}(10)(0.05)$ $= 0.4 + 0.25 = 0.65 \text{ cm}^2$
> 
> Área: $A = \frac{1}{2}(10)(8) = 40$ cm²
> 
> Error relativo: $\frac{0.65}{40} = 1.625%$
> 
> ---
> 
> **5a)** $x^2 + xy + y^2 = 7$
> 
> $d(x^2 + xy + y^2) = d(7) = 0$ $2x , dx + (y , dx + x , dy) + 2y , dy = 0$ $(2x + y)dx + (x + 2y)dy = 0$
> 
> $\frac{dy}{dx} = -\frac{2x + y}{x + 2y}$
> 
> ---
> 
> **6a)** $f(x,y,z) = x^2yz + xy^2z^2$
> 
> $\frac{\partial f}{\partial x} = 2xyz + y^2z^2$ $\frac{\partial f}{\partial y} = x^2z + 2xyz^2$ $\frac{\partial f}{\partial z} = x^2y + 2xy^2z$
> 
> $df = (2xyz + y^2z^2)dx + (x^2z + 2xyz^2)dy + (x^2y + 2xy^2z)dz$

---

## 🌟 Teoremas y Propiedades Importantes

> [!note]- 📜 Teoremas Fundamentales
> 
> ### Teorema 1: Existencia del Diferencial
> 
> Si $f$ es diferenciable en $(x_0, y_0)$, entonces:
> 
> 1. $f$ es **continua** en $(x_0, y_0)$
> 2. Las derivadas parciales $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$ **existen** en $(x_0, y_0)$
> 3. El diferencial total existe y es único
> 
> ---
> 
> ### Teorema 2: Condición Suficiente de Diferenciabilidad
> 
> Si las derivadas parciales $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$ existen y son **continuas** en una vecindad de $(x_0, y_0)$, entonces $f$ es diferenciable en $(x_0, y_0)$.
> 
> **Consecuencia práctica:** La mayoría de funciones "normales" (polinomios, exponenciales, trigonométricas y sus combinaciones) son diferenciables donde están definidas.
> 
> ---
> 
> ### Teorema 3: Unicidad del Plano Tangente
> 
> Si $f$ es diferenciable en $(x_0, y_0)$, entonces existe un **único** plano tangente a la superficie $z = f(x,y)$ en el punto $(x_0, y_0, f(x_0, y_0))$.
> 
> ---
> 
> ### Teorema 4: Aproximación Lineal
> 
> Si $f$ es diferenciable, entonces:
> 
> $\lim_{(\Delta x, \Delta y) \to (0,0)} \frac{|\Delta f - df|}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} = 0$
> 
> Es decir, el diferencial es la **mejor aproximación lineal** al cambio real.

---

## 💡 Consejos y Errores Comunes

> [!tip]- ⚠️ Errores Frecuentes
> 
> ### Error 1: Confundir $df$ con $\Delta f$
> 
> ❌ **Incorrecto:** "$df$ es el cambio exacto en $f$"
> 
> ✅ **Correcto:** "$df$ es una **aproximación lineal** al cambio $\Delta f$"
> 
> **Diferencia:**
> 
> - $\Delta f = f(x + \Delta x, y + \Delta y) - f(x,y)$ (cambio real, exacto)
> - $df = \frac{\partial f}{\partial x}\Delta x + \frac{\partial f}{\partial y}\Delta y$ (aproximación lineal)
> 
> ---
> 
> ### Error 2: Olvidar evaluar las derivadas parciales
> 
> ❌ **Incorrecto:** "El diferencial de $f(x,y) = x^2y$ es $df = 2xy , dx + x^2 , dy$"
> 
> ✅ **Correcto:** "El diferencial **general** es $df = 2xy , dx + x^2 , dy$, pero en el punto $(1,2)$ es $df = 4dx + dy$"
> 
> ---
> 
> ### Error 3: Usar notación incorrecta
> 
> ❌ **Incorrecto:** $df = f_x + f_y$ (faltan los diferenciales)
> 
> ✅ **Correcto:** $df = f_x , dx + f_y , dy$
> 
> **Recordar:** Las derivadas parciales se **multiplican** por los diferenciales correspondientes.
> 
> ---
> 
> ### Error 4: Ignorar signos en errores
> 
> ❌ **Incorrecto:** En propagación de errores, $|\Delta f| = |f_x|\Delta x + |f_y|\Delta y$
> 
> ✅ **Correcto:** $|\Delta f|_{\text{max}} = |f_x||\Delta x| + |f_y||\Delta y|$
> 
> **Razón:** Debemos considerar el **peor caso** donde ambos errores se suman.
> 
> ---
> 
> ### Error 5: Aplicar diferencial a funciones no diferenciables
> 
> ❌ **Incorrecto:** Usar $df$ en puntos donde $f$ no es diferenciable
> 
> ✅ **Correcto:** Verificar primero que las derivadas parciales existen y son continuas
> 
> **Ejemplo:** $f(x,y) = |x| + |y|$ **no es diferenciable** en $(0,0)$

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema es fundamental para:**
> 
> - **[[08 - Derivadas Parciales]]** - El diferencial total usa derivadas parciales
> - **[[09 - Diferenciabilidad]]** - Concepto central de diferenciabilidad
> - **[[10 - Regla de la Cadena]]** - Se expresa elegantemente con diferenciales
> - **[[11 - Gradiente]]** - $df = \nabla f \cdot d\vec{r}$
> - **[[15 - Optimización]]** - Condición $df = 0$ para extremos
> - **[[20 - Integrales de Línea]]** - Diferenciales exactos e inexactos
> 
> **Conceptos relacionados:**
> 
> - **Aproximación lineal** - El diferencial es la mejor aproximación lineal
> - **Plano tangente** - Representación geométrica del diferencial
> - **Propagación de errores** - Aplicación práctica directa
> - **Formas diferenciales** - Generalización en geometría diferencial
> 
> **Temas previos necesarios:**
> 
> - [[01 - Funciones de Varias Variables]]
> - [[02 - Continuidad]]
> - [[07 - Límites en Varias Variables]]

---

## 📝 Resumen de Conceptos Clave

> [!tip]- 💡 Puntos Esenciales para Recordar
> 
> ### Definición del Diferencial Total
> 
> ✅ **Fórmula fundamental:**
> 
> $df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$
> 
> ---
> 
> ### Interpretaciones
> 
> ✅ **Geométrica:** Cambio vertical en el plano tangente
> 
> ✅ **Física:** Cambio aproximado cuando variables cambian simultáneamente
> 
> ✅ **Algebraica:** Aproximación lineal de primer orden
> 
> ---
> 
> ### Propiedades Clave
> 
> ✅ **Linealidad:** $d(af + bg) = a , df + b , dg$
> 
> ✅ **Producto:** $d(fg) = f , dg + g , df$
> 
> ✅ **Composición:** Regla de la cadena
> 
> ---
> 
> ### Aplicaciones Principales
> 
> 📊 **Aproximación de valores:** $f(x + \Delta x, y + \Delta y) \approx f(x,y) + df$
> 
> 📊 **Propagación de errores:** $|\Delta f|_{\text{max}} = |f_x||\Delta x| + |f_y||\Delta y|$
> 
> 📊 **Derivadas implícitas:** $df = 0$ si $f$ es constante
> 
> 📊 **Plano tangente:** $z - z_0 = f_x(x - x_0) + f_y(y - y_0)$
> 
> ---
> 
> ### Condiciones Importantes
> 
> ⚠️ **Diferenciable** $\implies$ derivadas parciales existen
> 
> ⚠️ **Derivadas parciales continuas** $\implies$ diferenciable
> 
> ⚠️ **Diferenciable** $\implies$ continua
> 
> ⚠️ **Aproximación válida** cuando $\Delta x, \Delta y$ son pequeños

---

## 🎨 Visualización del Diferencial Total

> [!note]- 🖼️ Interpretación Gráfica Detallada
> 
> ### Superficie y Plano Tangente
> 
> ```
>         z
>         |           Superficie z = f(x,y)
>         |          /|
>         |         / |
>         |    Δf  /  | df ← Plano tangente
>         |       /   |
>         |   P₀ •----• (x₀+Δx, y₀+Δy, z₀+df)
>         |      |   /
>         |      |  / 
>         |      | /
>         +------•------------- y
>        /    (x₀,y₀)
>       x
> ```
> 
> **Elementos:**
> 
> - $P_0 = (x_0, y_0, z_0)$ - Punto de tangencia
> - $df$ - Cambio en el plano tangente (aproximación)
> - $\Delta f$ - Cambio real en la superficie
> - **Error** = $|\Delta f - df|$ (diferencia entre curvas)
> 
> ---
> 
> ### Vista Superior: Contornos y Gradiente
> 
> ```
>         y
>         |
>         |    
>         |   ↗ ∇f (gradiente)
>         |  ↗
>         | ↗  • (x₀,y₀)
>         |   /
>         |  / ← dr (desplazamiento)
>         | /
>         +------------- x
>         
>     df = ∇f · dr
> ```
> 
> **Interpretación:**
> 
> - El diferencial es la **proyección** del gradiente sobre el desplazamiento
> - Máximo $df$ cuando nos movemos en dirección del gradiente
> - $df = 0$ cuando nos movemos perpendicular al gradiente (a lo largo de curvas de nivel)
> 
> ---
> 
> ### Componentes del Diferencial
> 
> ```
>         y
>         |
>         |
>         | (x₀,y₀+dy)
>         |    •-------• (x₀+dx,y₀+dy)
>         |    |       |
>         |    | f_y·dy| Total: df = f_x·dx + f_y·dy
>         |    |       |
>         |    •-------•
>         | (x₀,y₀)  f_x·dx
>         |
>         +----------------------- x
> ```
> 
> **Descomposición:**
> 
> - Primero movemos $dx$ en $x$: contribución $f_x \cdot dx$
> - Luego movemos $dy$ en $y$: contribución $f_y \cdot dy$
> - **Total:** suma de ambas contribuciones

---

## 🧪 Experimento Numérico: Verificación del Diferencial

> [!example]- 🔬 Comparación Diferencial vs Cambio Real
> 
> **Función:** $f(x,y) = x^2 + xy + y^2$
> 
> **Punto base:** $(2, 3)$, $f(2,3) = 4 + 6 + 9 = 19$
> 
> **Derivadas parciales:**
> 
> $f_x = 2x + y = 7 \quad \text{en } (2,3)$ $f_y = x + 2y = 8 \quad \text{en } (2,3)$
> 
> **Diferencial:** $df = 7dx + 8dy$
> 
> ---
> 
> ### Tabla de Comparación
> 
> |$\Delta x$|$\Delta y$|$df$ (aprox)|$\Delta f$ (real)|Error|Error %|
> |---|---|---|---|---|---|
> |0.1|0.1|1.5|1.51|0.01|0.66%|
> |0.2|0.1|2.2|2.24|0.04|1.79%|
> |0.1|0.2|2.3|2.33|0.03|1.29%|
> |0.5|0.5|7.5|8.25|0.75|9.09%|
> |1.0|1.0|15.0|18.0|3.0|16.7%|
> 
> **Observaciones:**
> 
> ✅ Para cambios pequeños ($|\Delta x|, |\Delta y| < 0.2$), el error es menor al 2%
> 
> ✅ El error **crece** con el tamaño de los cambios
> 
> ✅ El error es aproximadamente **cuadrático** en $\Delta x$ y $\Delta y$
> 
> **Conclusión:** El diferencial es una **excelente aproximación** para cambios pequeños, pero pierde precisión con cambios grandes.

---

## 🔄 Diferencial Total en Diferentes Sistemas de Coordenadas

### 🌐 Coordenadas Cilíndricas

> [!note]- 🔵 Cilíndricas $(r, \theta, z)$
> 
> **Transformación:**
> 
> $\begin{cases} x = r\cos\theta \ y = r\sin\theta \ z = z \end{cases}$
> 
> **Diferenciales:**
> 
> $dx = \cos\theta , dr - r\sin\theta , d\theta$ $dy = \sin\theta , dr + r\cos\theta , d\theta$ $dz = dz$
> 
> ---
> 
> **Para una función $f(x,y,z)$:**
> 
> Si expresamos $f$ en cilíndricas como $f(r,\theta,z)$:
> 
> $df = \frac{\partial f}{\partial r}dr + \frac{\partial f}{\partial \theta}d\theta + \frac{\partial f}{\partial z}dz$
> 
> **Ejemplo:** $f = x^2 + y^2 = r^2$
> 
> $df = 2r , dr$

### 🌍 Coordenadas Esféricas

> [!note]- 🔴 Esféricas $(\rho, \theta, \phi)$
> 
> **Transformación:**
> 
> $\begin{cases} x = \rho\sin\phi\cos\theta \ y = \rho\sin\phi\sin\theta \ z = \rho\cos\phi \end{cases}$
> 
> donde $\rho \geq 0$, $0 \leq \phi \leq \pi$, $0 \leq \theta < 2\pi$
> 
> **Diferenciales:**
> 
> $dx = \sin\phi\cos\theta , d\rho + \rho\cos\phi\cos\theta , d\phi - \rho\sin\phi\sin\theta , d\theta$ $dy = \sin\phi\sin\theta , d\rho + \rho\cos\phi\sin\theta , d\phi + \rho\sin\phi\cos\theta , d\theta$ $dz = \cos\phi , d\rho - \rho\sin\phi , d\phi$
> 
> ---
> 
> **Para una función $f(\rho,\theta,\phi)$:**
> 
> $df = \frac{\partial f}{\partial \rho}d\rho + \frac{\partial f}{\partial \theta}d\theta + \frac{\partial f}{\partial \phi}d\phi$
> 
> **Ejemplo:** $f = x^2 + y^2 + z^2 = \rho^2$
> 
> $df = 2\rho , d\rho$

---

## 📐 Relación con el Gradiente y la Derivada Direccional

### 🎯 Forma Vectorial del Diferencial

> [!note]- ➡️ Notación Vectorial
> 
> **El diferencial como producto punto:**
> 
> $df = \nabla f \cdot d\vec{r}$
> 
> donde:
> 
> $\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right) = (f_x, f_y)$
> 
> $d\vec{r} = (dx, dy)$
> 
> ---
> 
> **Desarrollo:**
> 
> $df = \nabla f \cdot d\vec{r} = (f_x, f_y) \cdot (dx, dy) = f_x , dx + f_y , dy$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - Si $d\vec{r}$ tiene magnitud $|d\vec{r}| = ds$ y dirección $\vec{u}$:
> 
> $df = \nabla f \cdot \vec{u} , ds = D_{\vec{u}}f , ds$
> 
> donde $D_{\vec{u}}f$ es la **derivada direccional** en la dirección $\vec{u}$.
> 
> ---
> 
> **Consecuencias importantes:**
> 
> 1. **Máximo cambio:** $df$ es máximo cuando $d\vec{r}$ está en la dirección de $\nabla f$
>     
> 2. **Sin cambio:** $df = 0$ cuando $d\vec{r} \perp \nabla f$ (movimiento a lo largo de curvas de nivel)
>     
> 3. **Magnitud:** $|df| \leq |\nabla f| \cdot |d\vec{r}|$ (desigualdad de Cauchy-Schwarz)
>     

### Ejemplo 15: Gradiente y Diferencial

> [!example]- 📝 Ejemplo 15: Cálculo con Gradiente
> 
> **Función:** $f(x,y) = x^2 - y^2$
> 
> **Gradiente:**
> 
> $\nabla f = (2x, -2y)$
> 
> **En el punto $(3, 4)$:**
> 
> $\nabla f|_{(3,4)} = (6, -8)$
> 
> ---
> 
> **Desplazamiento:** $d\vec{r} = (0.1, 0.2)$
> 
> **Diferencial:**
> 
> $df = \nabla f \cdot d\vec{r} = (6, -8) \cdot (0.1, 0.2)$ $= 6(0.1) + (-8)(0.2) = 0.6 - 1.6 = -1.0$
> 
> ---
> 
> **Verificación:**
> 
> $f(3,4) = 9 - 16 = -7$ $f(3.1, 4.2) = (3.1)^2 - (4.2)^2 = 9.61 - 17.64 = -8.03$ $\Delta f = -8.03 - (-7) = -1.03$
> 
> El diferencial $df = -1.0$ es muy cercano al cambio real $\Delta f = -1.03$ ✓

---

## 🌟 Aplicación Avanzada: Ecuaciones Diferenciales

### 📚 Diferenciales Exactos

> [!note]- 🔬 Formas Diferenciales Exactas
> 
> **Definición:** Una expresión de la forma:
> 
> $M(x,y)dx + N(x,y)dy$
> 
> es un **diferencial exacto** si existe una función $f(x,y)$ tal que:
> 
> $df = M(x,y)dx + N(x,y)dy$
> 
> Es decir:
> 
> $M = \frac{\partial f}{\partial x}, \quad N = \frac{\partial f}{\partial y}$
> 
> ---
> 
> **Criterio de exactitud (Teorema de Schwarz):**
> 
> La forma $M , dx + N , dy$ es exacta si y solo si:
> 
> $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
> 
> (condición de igualdad de derivadas parciales mixtas)
> 
> ---
> 
> **Aplicación en EDO:**
> 
> La ecuación diferencial $M(x,y)dx + N(x,y)dy = 0$ es **exacta** si:
> 
> $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
> 
> En ese caso, la solución es $f(x,y) = C$ donde $df = M , dx + N , dy$.

### Ejemplo 16: Ecuación Diferencial Exacta

> [!example]- 📝 Ejemplo 16: Resolver EDO Exacta
> 
> **Ecuación:** $(2xy + 3)dx + (x^2 + 4y)dy = 0$
> 
> **Verificar exactitud:**
> 
> $M = 2xy + 3, \quad N = x^2 + 4y$
> 
> $\frac{\partial M}{\partial y} = 2x, \quad \frac{\partial N}{\partial x} = 2x$
> 
> Como son iguales, la ecuación **es exacta** ✓
> 
> ---
> 
> **Encontrar $f(x,y)$:**
> 
> De $\frac{\partial f}{\partial x} = M = 2xy + 3$:
> 
> $f(x,y) = \int (2xy + 3)dx = x^2y + 3x + g(y)$
> 
> donde $g(y)$ es una función solo de $y$.
> 
> ---
> 
> De $\frac{\partial f}{\partial y} = N = x^2 + 4y$:
> 
> $\frac{\partial f}{\partial y} = x^2 + g'(y) = x^2 + 4y$
> 
> $g'(y) = 4y \implies g(y) = 2y^2 + C_1$
> 
> ---
> 
> **Solución general:**
> 
> $f(x,y) = x^2y + 3x + 2y^2 = C$
> 
> donde $C$ es una constante arbitraria.

---

## 🎓 Ejercicios Adicionales de Aplicación

> [!example]- 💪 Problemas Integradores
> 
> **11. Optimización con restricciones:**
> 
> Maximizar $f(x,y) = xy$ sujeto a $x + y = 10$.
> 
> a) Usar el método de sustitución b) Usar diferenciales: $df = 0$ con $d(x+y) = 0$ c) Comparar ambos métodos
> 
> ---
> 
> **12. Análisis de sensibilidad:**
> 
> Una empresa produce $Q = 50L^{0.4}K^{0.6}$ unidades, donde $L$ = trabajo y $K$ = capital.
> 
> a) Si $L = 100$ y $K = 200$, calcular $dQ$ b) Si el trabajo aumenta 2% y el capital disminuye 1%, ¿cómo cambia la producción? c) ¿Qué es más efectivo: aumentar $L$ o $K$?
> 
> ---
> 
> **13. Física: Ley de Snell:**
> 
> El tiempo de viaje de luz es $T = \frac{\sqrt{x^2 + h_1^2}}{v_1} + \frac{\sqrt{(a-x)^2 + h_2^2}}{v_2}$
> 
> a) Calcular $dT$ b) Para $dT = 0$, derivar la ley de Snell: $\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$
> 
> ---
> 
> **14. Geometría: Área de triángulo:**
> 
> El área de un triángulo con lados $a$, $b$ y ángulo $C$ es $A = \frac{1}{2}ab\sin C$.
> 
> a) Calcular $dA$ b) Si $a = 5 \pm 0.1$ m, $b = 7 \pm 0.15$ m, $C = 60° \pm 1°$, estimar el error en $A$
> 
> ---
> 
> **15. Ecuación de onda:**
> 
> Una onda tiene forma $z = A\sin(kx - \omega t)$.
> 
> a) Calcular $dz$ b) Mostrar que $\frac{\partial^2 z}{\partial t^2} = v^2\frac{\partial^2 z}{\partial x^2}$ donde $v = \omega/k$

---

## 📊 Tabla Comparativa: Diferencial vs Otros Conceptos

> [!note]- 📋 Diferencial en Contexto
> 
> |Concepto|Definición|Relación con Diferencial|Uso Principal|
> |---|---|---|---|
> |**Diferencial Total**|$df = f_x dx + f_y dy$|-|Aproximación lineal|
> |**Cambio Real**|$\Delta f = f(x+\Delta x, y+\Delta y) - f(x,y)$|$\Delta f \approx df$|Valor exacto|
> |**Derivada Parcial**|$f_x = \lim_{\Delta x \to 0} \frac{\Delta f}{\Delta x}$|$df = f_x dx + f_y dy$|Tasa de cambio en una dirección|
> |**Gradiente**|$\nabla f = (f_x, f_y)$|$df = \nabla f \cdot d\vec{r}$|Dirección de máximo crecimiento|
> |**Derivada Direccional**|$D_{\vec{u}}f = \nabla f \cdot \vec{u}$|$df = D_{\vec{u}}f , ds$|Tasa de cambio en dirección $\vec{u}$|
> |**Plano Tangente**|$z - z_0 = f_x(x-x_0) + f_y(y-y_0)$|$dz = df$|Aproximación geométrica|

---

## 🎯 Estrategias para Resolver Problemas

> [!tip]- 🛠️ Metodología Paso a Paso
> 
> ### Para Calcular el Diferencial:
> 
> **Paso 1:** Identificar la función $f(x,y)$
> 
> **Paso 2:** Calcular derivadas parciales
> 
> - $\frac{\partial f}{\partial x}$
> - $\frac{\partial f}{\partial y}$
> 
> **Paso 3:** Escribir el diferencial general
> 
> - $df = f_x , dx + f_y , dy$
> 
> **Paso 4:** Si es necesario, evaluar en un punto específico
> 
> ---
> 
> ### Para Aproximar Valores:
> 
> **Paso 1:** Identificar punto base $(x_0, y_0)$ cercano donde conocemos $f$
> 
> **Paso 2:** Calcular $f(x_0, y_0)$
> 
> **Paso 3:** Calcular derivadas parciales en $(x_0, y_0)$
> 
> **Paso 4:** Determinar $\Delta x = x - x_0$ y $\Delta y = y - y_0$
> 
> **Paso 5:** Calcular $df = f_x(x_0,y_0)\Delta x + f_y(x_0,y_0)\Delta y$
> 
> **Paso 6:** Aproximar: $f(x,y) \approx f(x_0,y_0) + df$
> 
> ---
> 
> ### Para Propagación de Errores:
> 
> **Paso 1:** Identificar la función $f$ y las variables medidas
> 
> **Paso 2:** Calcular $|f_x|$ y $|f_y|$ en los valores medidos
> 
> **Paso 3:** Identificar errores $|\Delta x|$ y $|\Delta y|$
> 
> **Paso 4:** Error máximo: $|\Delta f|_{\max} = |f_x||\Delta x| + |f_y||\Delta y|$
> 
> **Paso 5:** Error relativo: $\frac{|\Delta f|}{|f|}$

---

## 🌈 Visualización Interactiva Conceptual

> [!note]- 🎨 Comprensión Visual
> 
> ### Analogía del "Camino en una Montaña"
> 
> Imagina que $z = f(x,y)$ representa la **altura de una montaña**:
> 
> **Situación:**
> 
> - Estás en el punto $(x_0, y_0)$ a altura $z_0 = f(x_0, y_0)$
> - Quieres saber tu nueva altura si caminas $dx$ hacia el este y $dy$ hacia el norte
> 
> **El Diferencial Total te dice:**
> 
> $\text{Cambio de altura} \approx \underbrace{(\text{pendiente este})}_{\partial f/\partial x} \times dx + \underbrace{(\text{pendiente norte})}_{\partial f/\partial y} \times dy$
> 
> ---
> 
> ### Componentes:
> 
> 1. **$\frac{\partial f}{\partial x}dx$** - Cambio si solo caminaras hacia el este
> 2. **$\frac{\partial f}{\partial y}dy$** - Cambio si solo caminaras hacia el norte
> 3. **$df$** - Suma de ambos efectos (aproximación lineal)
> 
> ---
> 
> ### ¿Por qué es una aproximación?
> 
> - El diferencial asume que la pendiente es **constante**
> - En realidad, la pendiente cambia (términos de segundo orden)
> - Funciona bien para **desplazamientos pequeños**

---

## 📚 Referencias y Lecturas Adicionales

> [!note]- 📖 Para Profundizar
> 
> ### Temas Relacionados para Estudiar:
> 
> **Nivel Intermedio:**
> 
> - Derivadas direccionales y gradiente
> - Plano tangente y recta normal
> - Regla de la cadena multivariable
> - Teorema de Taylor en varias variables
> 
> **Nivel Avanzado:**
> 
> - Formas diferenciales en geometría diferencial
> - Teorema de Stokes
> - Cálculo variacional
> - Diferencial exterior (cálculo en variedades)
> 
> ### Aplicaciones Especializadas:
> 
> - Mecánica analítica (Lagrangiana, Hamiltoniana)
> - Termodinámica (potenciales termodinámicos)
> - Geometría diferencial (formas, cohomología)
> - Teoría de control (linealización de sistemas)

---

## ✨ Conclusión

> [!quote]- 🎓 Reflexión Final
> 
> El **diferencial total** es uno de los conceptos más poderosos del cálculo multivariable:
> 
> ### Importancia Conceptual:
> 
> ✨ **Unifica** múltiples conceptos:
> 
> - Derivadas parciales
> - Aproximación lineal
> - Gradiente
> - Plano tangente
> 
> ✨ **Conecta** teoría y práctica:
> 
> - Base teórica rigurosa
> - Aplicaciones numéricas directas
> - Herramienta de análisis de errores
> 
> ✨ **Extiende** ideas de cálculo de una variable:
> 
> - $df = f'(x)dx$ → $df

**Tags:** #calculo-multivariable #diferencial-total #derivadas-parciales #aproximacion-lineal #propagacion-errores #diferenciabilidad #plano-tangente #gradiente #aplicaciones
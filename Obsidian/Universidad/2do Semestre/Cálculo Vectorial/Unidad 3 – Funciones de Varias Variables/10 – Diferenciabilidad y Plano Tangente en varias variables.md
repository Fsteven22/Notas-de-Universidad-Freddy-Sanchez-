# 📘 Diferenciabilidad y Plano Tangente

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante la Diferenciabilidad en varias variables?
> 
> La diferenciabilidad extiende el concepto de aproximación lineal a funciones de varias variables, permitiéndonos **aproximar localmente** una función compleja mediante una función lineal simple.
> 
> **Motivación:**
> 
> - En $f(x)$: $f(x) \approx f(a) + f'(a)(x-a)$ cerca de $x = a$
> - En $f(x,y)$: necesitamos una **aproximación lineal en 2D**
> - Solución: **Plano tangente** que depende de ambas derivadas parciales
> 
> **Diferencia crucial:**
> 
> - **Derivadas parciales existentes** ≠ **Diferenciabilidad**
> - Diferenciabilidad es un concepto **más fuerte** que requiere:
>     - Existencia de derivadas parciales
>     - Continuidad de las derivadas parciales
>     - Aproximación lineal "buena" en todas direcciones
> 
> **Aplicaciones prácticas:**
> 
> - **Física:** Aproximaciones lineales de sistemas no lineales
> - **Ingeniería:** Análisis de sensibilidad, propagación de errores
> - **Optimización:** Condiciones necesarias para extremos
> - **Machine Learning:** Descenso de gradiente, backpropagation
> - **Geometría:** Planos tangentes a superficies

---

## 📐 Diferenciabilidad en Una Variable (Repaso)

### 🔄 Recordatorio: Caso Unidimensional

> [!note]- 📊 Diferenciabilidad en $\mathbb{R}$
> 
> ### Definición
> 
> Una función $f: \mathbb{R} \to \mathbb{R}$ es **diferenciable** en $x = a$ si existe $f'(a)$ tal que:
> 
> $$f(x) = f(a) + f'(a)(x-a) + o(|x-a|)$$
> 
> donde $\lim_{x \to a} \frac{o(|x-a|)}{|x-a|} = 0$
> 
> ---
> 
> ### Interpretación Geométrica
> 
> La función puede aproximarse por su **recta tangente**:
> 
> ```
>     y
>     |
>     |    /  f(x)
>     |   / â— 
>     |  /  /
>     | â—----- Recta tangente: y = f(a) + f'(a)(x-a)
>     |/
>     +-------- x
>         a
> ```
> 
> ---
> 
> ### Propiedades clave
> 
> ✅ **Diferenciable** ⟹ **Continua**
> 
> ✅ **Diferenciable** ⟹ **Derivada existe**
> 
> ❌ **Derivada existe** ⟹ **Diferenciable** (falso en varias variables!)
> 
> ---
> 
> ### Error de aproximación
> 
> El error $E(x) = f(x) - [f(a) + f'(a)(x-a)]$ satisface:
> 
> $$\lim_{x \to a} \frac{E(x)}{|x-a|} = 0$$
> 
> Esto significa que el error es **mucho más pequeño** que la distancia $|x-a|$.

---

## 🎯 Diferenciabilidad en Varias Variables

### 📋 Definición Formal

> [!example]- 🟢 Definición: Diferenciabilidad en $\mathbb{R}^2$
> 
> **Definición:** Una función $f: \mathbb{R}^2 \to \mathbb{R}$ es **diferenciable** en el punto $(x_0, y_0)$ si existen las derivadas parciales $f_x(x_0, y_0)$ y $f_y(x_0, y_0)$, y además:
> 
> $$f(x,y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) + E(x,y)$$
> 
> donde el **error** $E(x,y)$ satisface:
> 
> $$\lim_{(x,y) \to (x_0, y_0)} \frac{E(x,y)}{\sqrt{(x-x_0)^2 + (y-y_0)^2}} = 0$$
> 
> ---
> 
> **Notación compacta:** Si denotamos $\Delta x = x - x_0$, $\Delta y = y - y_0$, y $\Delta z = f(x,y) - f(x_0, y_0)$:
> 
> $$\Delta z = f_x(x_0, y_0)\Delta x + f_y(x_0, y_0)\Delta y + E(\Delta x, \Delta y)$$
> 
> con:
> 
> $$\lim_{(\Delta x, \Delta y) \to (0,0)} \frac{E(\Delta x, \Delta y)}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} = 0$$
> 
> ---
> 
> **Interpretación:**
> 
> - La parte lineal $f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$ es la **mejor aproximación lineal**
> - El error $E(x,y)$ es **"pequeño de orden superior"**
> - El error va a cero **más rápido** que la distancia al punto
> 
> ---
> 
> **Notación alternativa:** Usando $h = (h_1, h_2) = (x - x_0, y - y_0)$ y $|h| = \sqrt{h_1^2 + h_2^2}$:
> 
> $$f(x_0 + h_1, y_0 + h_2) = f(x_0, y_0) + f_x(x_0, y_0)h_1 + f_y(x_0, y_0)h_2 + o(|h|)$$

> [!example]- 🔵 Definición: Diferenciabilidad en $\mathbb{R}^n$
> 
> **Generalización:** Una función $f: \mathbb{R}^n \to \mathbb{R}$ es diferenciable en $\mathbf{x}_0 = (x_1^0, x_2^0, \ldots, x_n^0)$ si:
> 
> $$f(\mathbf{x}) = f(\mathbf{x}_0) + \sum_{i=1}^{n} \frac{\partial f}{\partial x_i}(\mathbf{x}_0)(x_i - x_i^0) + E(\mathbf{x})$$
> 
> donde:
> 
> $$\lim_{\mathbf{x} \to \mathbf{x}_0} \frac{E(\mathbf{x})}{|\mathbf{x} - \mathbf{x}_0|} = 0$$
> 
> ---
> 
> **En notación vectorial:**
> 
> $$f(\mathbf{x}_0 + \mathbf{h}) = f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0) \cdot \mathbf{h} + o(|\mathbf{h}|)$$
> 
> donde $\nabla f = \left(\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right)$ es el **gradiente**.

### 🔍 Diferencia con Derivadas Parciales

> [!warning]- ⚠️ Diferenciabilidad vs Derivadas Parciales
> 
> ### ¡CUIDADO! No son lo mismo
> 
> **Derivadas parciales existen** ≠ **Función diferenciable**
> 
> ---
> 
> ### Contraejemplo clásico
> 
> Considere:
> 
> $$f(x,y) = \begin{cases} \frac{xy}{\sqrt{x^2 + y^2}} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **En el origen $(0,0)$:**
> 
> $$f_x(0,0) = \lim_{h \to 0} \frac{f(h,0) - f(0,0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$$
> 
> $$f_y(0,0) = \lim_{h \to 0} \frac{f(0,h) - f(0,0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$$
> 
> ✅ **Las derivadas parciales existen** en $(0,0)$
> 
> ---
> 
> **Pero:** Si nos acercamos al origen por la recta $y = x$:
> 
> $$\lim_{t \to 0} f(t,t) = \lim_{t \to 0} \frac{t \cdot t}{\sqrt{t^2 + t^2}} = \lim_{t \to 0} \frac{t^2}{t\sqrt{2}} = \lim_{t \to 0} \frac{t}{\sqrt{2}} = 0$$
> 
> Pero por $y = 2x$:
> 
> $$\lim_{t \to 0} f(t,2t) = \lim_{t \to 0} \frac{t \cdot 2t}{\sqrt{t^2 + 4t^2}} = \lim_{t \to 0} \frac{2t^2}{t\sqrt{5}} = \lim_{t \to 0} \frac{2t}{\sqrt{5}}$$
> 
> La aproximación lineal $L(x,y) = 0 + 0 \cdot x + 0 \cdot y = 0$ no es una buena aproximación en todas direcciones.
> 
> ❌ **La función NO es diferenciable** en $(0,0)$
> 
> ---
> 
> ### Resumen visual
> 
> ```
> Derivadas parciales existen en (x₀,y₀)
>                 ↓
>            ¿Son continuas?
>           /              \
>         SÍ                NO
>         ↓                 ↓
>   DIFERENCIABLE    POSIBLEMENTE NO
>         ↓               DIFERENCIABLE
>     CONTINUA              ↓
>                      Verificar
>                      definición
> ```

---

## 📊 Teorema Fundamental de Diferenciabilidad

> [!note]- 🎯 Condición Suficiente para Diferenciabilidad
> 
> **Teorema:** Si $f: \mathbb{R}^2 \to \mathbb{R}$ tiene derivadas parciales $f_x$ y $f_y$ que son **continuas** en un entorno abierto de $(x_0, y_0)$, entonces $f$ es **diferenciable** en $(x_0, y_0)$.
> 
> ---
> 
> ### En símbolos
> 
> $$\text{Si } f_x, f_y \text{ son continuas en } (x_0, y_0) \implies f \text{ es diferenciable en } (x_0, y_0)$$
> 
> ---
> 
> ### Consecuencias importantes
> 
> ✅ **Diferenciable** ⟹ **Continua**
> 
> ✅ **Diferenciable** ⟹ **Derivadas parciales existen**
> 
> ✅ **Derivadas parciales continuas** ⟹ **Diferenciable**
> 
> ❌ **Derivadas parciales existen** ⟹ **Diferenciable** (FALSO)
> 
> ---
> 
> ### Clase $C^1$
> 
> Decimos que $f$ es de **clase $C^1$** si todas sus derivadas parciales de primer orden existen y son continuas.
> 
> **Resultado clave:** $$f \in C^1 \implies f \text{ es diferenciable}$$
> 
> ---
> 
> ### Ejemplos de funciones $C^1$
> 
> - Polinomios: $f(x,y) = x^2 + y^2 + xy$
> - Exponenciales: $f(x,y) = e^{x+y}$
> - Trigonométricas: $f(x,y) = \sin(xy)$
> - Composiciones de funciones $C^1$
> 
> **Prácticamente todas las funciones "usuales" son $C^1$** donde están definidas.

---

## ✈️ Plano Tangente

### 📐 Definición Geométrica

> [!example]- 🟡 Definición: Plano Tangente
> 
> **Definición:** El **plano tangente** a la superficie $z = f(x,y)$ en el punto $(x_0, y_0, z_0)$ donde $z_0 = f(x_0, y_0)$ es el plano dado por:
> 
> $$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
> 
> o equivalentemente:
> 
> $$z = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
> 
> ---
> 
> **Interpretación:**
> 
> - Es el **único plano** que mejor aproxima la superficie cerca del punto
> - Contiene las dos rectas tangentes en las direcciones $x$ e $y$
> - Es la gráfica de la **aproximación lineal** de $f$
> 
> ---
> 
> **Forma alternativa (implícita):**
> 
> $$f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) - (z - z_0) = 0$$
> 
> ---
> 
> **Notación compacta:**
> 
> Si $L(x,y)$ denota la función lineal que define el plano tangente:
> 
> $$L(x,y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
> 
> Entonces el plano tangente es: $z = L(x,y)$

### 🎨 Visualización del Plano Tangente

> [!note]- 🖼️ Interpretación Gráfica
> 
> ### Superficie y Plano Tangente
> 
> ```
>           z
>           |
>           |     /|\  Superficie z = f(x,y)
>           |    / | \
>           |   /  |  \
>           |  /   â— P(x₀,y₀,z₀)
>           | /___/|\___\  â† Plano tangente
>           |/   / | \   \
>           +---+--+--+--- y
>          /   /   |   \
>         x   /    y₀   \
>            x₀
> ```
> 
> ---
> 
> ### Componentes del Plano Tangente
> 
> El plano tangente está determinado por:
> 
> 1. **Punto de tangencia:** $(x_0, y_0, f(x_0, y_0))$
> 2. **Pendiente en dirección $x$:** $f_x(x_0, y_0)$
> 3. **Pendiente en dirección $y$:** $f_y(x_0, y_0)$
> 
> ---
> 
> ### Aproximación Local
> 
> Cerca del punto $(x_0, y_0)$:
> 
> $$f(x,y) \approx L(x,y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
> 
> Esta es la **mejor aproximación lineal** de $f$ cerca de $(x_0, y_0)$.

---

## 📝 Ejemplos Detallados

### Ejemplo 1: Plano Tangente a un Paraboloide

> [!example]- 📐 Ejemplo 1: Paraboloide
> 
> **Función:** $$f(x,y) = x^2 + y^2$$
> 
> **Punto:** $(1, 2)$
> 
> ---
> 
> **Paso 1: Calcular $f(x_0, y_0)$**
> 
> $$f(1, 2) = 1^2 + 2^2 = 1 + 4 = 5$$
> 
> El punto en la superficie es $(1, 2, 5)$.
> 
> ---
> 
> **Paso 2: Calcular derivadas parciales**
> 
> $$f_x(x,y) = 2x \implies f_x(1,2) = 2(1) = 2$$
> 
> $$f_y(x,y) = 2y \implies f_y(1,2) = 2(2) = 4$$
> 
> ---
> 
> **Paso 3: Ecuación del plano tangente**
> 
> $$z - 5 = 2(x - 1) + 4(y - 2)$$
> 
> $$z - 5 = 2x - 2 + 4y - 8$$
> 
> $$z = 2x + 4y - 5$$
> 
> $$\boxed{z = 2x + 4y - 5}$$
> 
> ---
> 
> **Verificación:** El plano pasa por $(1, 2, 5)$:
> 
> $$z = 2(1) + 4(2) - 5 = 2 + 8 - 5 = 5$$ ✓
> 
> ---
> 
> **Interpretación:**
> 
> - Cerca de $(1, 2)$, el paraboloide se comporta como el plano $z = 2x + 4y - 5$
> - La pendiente en dirección $x$ es 2
> - La pendiente en dirección $y$ es 4

### Ejemplo 2: Función Exponencial

> [!example]- 📐 Ejemplo 2: Exponencial
> 
> **Función:** $$f(x,y) = e^{xy}$$
> 
> **Punto:** $(0, 1)$
> 
> ---
> 
> **Paso 1: Valor en el punto**
> 
> $$f(0, 1) = e^{0 \cdot 1} = e^0 = 1$$
> 
> ---
> 
> **Paso 2: Derivadas parciales**
> 
> $$f_x(x,y) = ye^{xy} \implies f_x(0,1) = 1 \cdot e^0 = 1$$
> 
> $$f_y(x,y) = xe^{xy} \implies f_y(0,1) = 0 \cdot e^0 = 0$$
> 
> ---
> 
> **Paso 3: Plano tangente**
> 
> $$z - 1 = 1(x - 0) + 0(y - 1)$$
> 
> $$z - 1 = x$$
> 
> $$\boxed{z = x + 1}$$
> 
> ---
> 
> **Interpretación:**
> 
> - El plano tangente es $z = x + 1$
> - En el punto $(0, 1)$, la superficie tiene pendiente 1 en dirección $x$ y 0 en dirección $y$
> - Aproximación: $e^{xy} \approx x + 1$ cerca de $(0, 1)$

### Ejemplo 3: Función Trigonométrica

> [!example]- 📐 Ejemplo 3: Seno y Coseno
> 
> **Función:** $$f(x,y) = \sin(x)\cos(y)$$
> 
> **Punto:** $(0, 0)$
> 
> ---
> 
> **Paso 1: Valor**
> 
> $$f(0, 0) = \sin(0)\cos(0) = 0 \cdot 1 = 0$$
> 
> ---
> 
> **Paso 2: Derivadas**
> 
> $$f_x(x,y) = \cos(x)\cos(y) \implies f_x(0,0) = \cos(0)\cos(0) = 1$$
> 
> $$f_y(x,y) = -\sin(x)\sin(y) \implies f_y(0,0) = -\sin(0)\sin(0) = 0$$
> 
> ---
> 
> **Paso 3: Plano tangente**
> 
> $$z - 0 = 1(x - 0) + 0(y - 0)$$
> 
> $$\boxed{z = x}$$
> 
> ---
> 
> **Aproximación:** Cerca del origen:
> 
> $$\sin(x)\cos(y) \approx x$$

### Ejemplo 4: Función Compuesta

> [!example]- 📐 Ejemplo 4: Logaritmo
> 
> **Función:** $$f(x,y) = \ln(x^2 + y^2 + 1)$$
> 
> **Punto:** $(1, 1)$
> 
> ---
> 
> **Paso 1: Valor**
> 
> $$f(1, 1) = \ln(1^2 + 1^2 + 1) = \ln(3)$$
> 
> ---
> 
> **Paso 2: Derivadas**
> 
> $$f_x(x,y) = \frac{2x}{x^2 + y^2 + 1} \implies f_x(1,1) = \frac{2(1)}{3} = \frac{2}{3}$$
> 
> $$f_y(x,y) = \frac{2y}{x^2 + y^2 + 1} \implies f_y(1,1) = \frac{2(1)}{3} = \frac{2}{3}$$
> 
> ---
> 
> **Paso 3: Plano tangente**
> 
> $$z - \ln(3) = \frac{2}{3}(x - 1) + \frac{2}{3}(y - 1)$$
> 
> $$z = \ln(3) + \frac{2}{3}(x - 1) + \frac{2}{3}(y - 1)$$
> 
> $$\boxed{z = \frac{2}{3}x + \frac{2}{3}y + \ln(3) - \frac{4}{3}}$$

### Ejemplo 5: Verificar Diferenciabilidad

> [!example]- 📐 Ejemplo 5: Verificación Directa
> 
> **Función:** $$f(x,y) = x^2 + 2xy + y^2$$
> 
> **Verificar diferenciabilidad en $(0, 0)$**
> 
> ---
> 
> **Método 1: Derivadas continuas**
> 
> $$f_x(x,y) = 2x + 2y$$ $$f_y(x,y) = 2x + 2y$$
> 
> Ambas son polinomios, por lo tanto **continuas en todo $\mathbb{R}^2$**.
> 
> ✅ **Conclusión:** $f$ es diferenciable en $(0, 0)$ (y en todo punto).
> 
> ---
> 
> **Método 2: Verificación directa de la definición**
> 
> En $(0, 0)$: $f(0, 0) = 0$, $f_x(0, 0) = 0$, $f_y(0, 0) = 0$
> 
> Aproximación lineal: $L(x,y) = 0 + 0 \cdot x + 0 \cdot y = 0$
> 
> Error: $$E(x,y) = f(x,y) - L(x,y) = x^2 + 2xy + y^2$$
> 
> Debemos verificar: $$\lim_{(x,y) \to (0,0)} \frac{x^2 + 2xy + y^2}{\sqrt{x^2 + y^2}} = 0$$
> 
> Acotando: $$|x^2 + 2xy + y^2| \leq x^2 + 2|x||y| + y^2 \leq x^2 + 2|x||y| + y^2$$
> 
> Por Cauchy-Schwarz: $|xy| \leq \frac{1}{2}(x^2 + y^2)$
> 
> $$|x^2 + 2xy + y^2| \leq x^2 + (x^2 + y^2) + y^2 = 2(x^2 + y^2)$$
> 
> Por lo tanto: $$\frac{|E(x,y)|}{\sqrt{x^2 + y^2}} \leq \frac{2(x^2 + y^2)}{\sqrt{x^2 + y^2}} = 2\sqrt{x^2 + y^2} \to 0$$
> 
> ✅ **La función es diferenciable en $(0, 0)$**

---

## 🧮 Vector Normal y Ecuación Implícita

### 📐 Vector Normal al Plano Tangente

> [!note]- 🎯 Vector Normal
> 
> ### Definición
> 
> Si el plano tangente a $z = f(x,y)$ en $(x_0, y_0)$ es:
> 
> $$z = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
> 
> Reescribiendo en forma implícita:
> 
> $$f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) - (z - f(x_0, y_0)) = 0$$
> 
> Un **vector normal** al plano tangente es:
> 
> $$\mathbf{n} = \left(f_x(x_0, y_0), f_y(x_0, y_0), -1\right)$$
> 
> o alternativamente:
> 
> $$\mathbf{n} = \left(-f_x(x_0, y_0), -f_y(x_0, y_0), 1\right)$$
> 
> ---
> 
> ### Forma general
> 
> Si la superficie está dada implícitamente por $F(x, y, z) = c$, entonces un vector normal en $(x_0, y_0, z_0)$ es:
> 
> $$\mathbf{n} = \nabla F(x_0, y_0, z_0) = \left(\frac{\partial F}{\partial x}, \frac{\partial F}{\partial y}, \frac{\partial F}{\partial z}\right)\bigg|_{(x_0, y_0, z_0)}$$
> 
> ---
> 
> ### Ecuación del plano con vector normal
> 
> Si $\mathbf{n} = (A, B, C)$ y el plano pasa por $(x_0, y_0, z_0)$:
> 
> $$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$$

### Ejemplo 6: Vector Normal

> [!example]- 📐 Ejemplo 6: Calcular Vector Normal
> 
> **Superficie:** $z = x^2 + y^2$ en el punto $(1, 2, 5)$
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$f_x(1,2) = 2(1) = 2$$ $$f_y(1,2) = 2(2) = 4$$
> 
> ---
> 
> **Vector normal:**
> 
> $$\mathbf{n} = (2, 4, -1)$$
> 
> o normalizando (vector unitario):
> 
> $$\hat{\mathbf{n}} = \frac{1}{\sqrt{2^2 + 4^2 + (-1)^2}}(2, 4, -1) = \frac{1}{\sqrt{21}}(2, 4, -1)$$
> 
> ---
> 
> **Ecuación del plano (forma vectorial):**
> 
> $$2(x - 1) + 4(y - 2) - 1(z - 5) = 0$$
> 
> $$2x + 4y - z - 5 = 0$$
> 
> o despejando $z$:
> 
> $$z = 2x + 4y - 5$$

---

## 🔬 Aplicaciones de la Diferenciabilidad

### 📏 Aplicación 1: Aproximación Lineal y Estimación

> [!example]- 📊 Ejemplo 7: Estimación de Valores
> 
> **Problema:** Estimar $f(1.02, 1.97)$ donde $f(x,y) = x^2 + y^2$
> 
> ---
> 
> **Solución usando plano tangente:**
> 
> Tomamos el punto cercano $(1, 2)$ donde es fácil calcular.
> 
> **Paso 1: Valor exacto en $(1, 2)$**
> 
> $$f(1, 2) = 1^2 + 2^2 = 5$$
> 
> ---
> 
> **Paso 2: Derivadas parciales**
> 
> $$f_x(1,2) = 2(1) = 2$$ $$f_y(1,2) = 2(2) = 4$$
> 
> ---
> 
> **Paso 3: Aproximación lineal**
> 
> $$L(x,y) = f(1,2) + f_x(1,2)(x-1) + f_y(1,2)(y-2)$$
> 
> $$L(x,y) = 5 + 2(x-1) + 4(y-2)$$
> 
> ---
> 
> **Paso 4: Estimar**
> 
> $$f(1.02, 1.97) \approx L(1.02, 1.97)$$
> 
> $$= 5 + 2(1.02 - 1) + 4(1.97 - 2)$$
> 
> $$= 5 + 2(0.02) + 4(-0.03)$$
> 
> $$= 5 + 0.04 - 0.12$$
> 
> $$= 4.92$$
> 
> ---
> 
> **Verificación:** Valor exacto:
> 
> $$f(1.02, 1.97) = (1.02)^2 + (1.97)^2 = 1.0404 + 3.8809 = 4.9213$$
> 
> **Error:** $|4.92 - 4.9213| = 0.0013$ (muy pequeño!)

### 💰 Aplicación 2: Análisis de Sensibilidad en Economía

> [!example]- 📈 Ejemplo 8: Función de Producción
> 
> **Situación:** Una empresa tiene función de producción Cobb-Douglas:
> 
> $$P(K,L) = 100K^{0.3}L^{0.7}$$
> 
> donde $K$ = capital (miles de $), $L$ = trabajo (horas)
> 
> Actualmente: $K = 1000$, $L = 500$
> 
> **Pregunta:** ¿Cómo cambia la producción si $K$ aumenta a 1010 y $L$ disminuye a 498?
> 
> ---
> 
> **Solución:**
> 
> **Paso 1: Producción actual**
> 
> $$P(1000, 500) = 100 \cdot 1000^{0.3} \cdot 500^{0.7}$$
> 
> $$= 100 \cdot 15.8489 \cdot 87.0551 \approx 137,972.6$$
> 
> ---
> 
> **Paso 2: Derivadas parciales (productividades marginales)**
> 
> $$\frac{\partial P}{\partial K} = 100 \cdot 0.3 \cdot K^{-0.7}L^{0.7} = 30K^{-0.7}L^{0.7}$$
> 
> $$\frac{\partial P}{\partial L} = 100 \cdot 0.7 \cdot K^{0.3}L^{-0.3} = 70K^{0.3}L^{-0.3}$$
> 
> En $(1000, 500)$:
> 
> $$\frac{\partial P}{\partial K}(1000, 500) = 30 \cdot 1000^{-0.7} \cdot 500^{0.7} \approx 41.39$$
> 
> $$\frac{\partial P}{\partial L}(1000, 500) = 70 \cdot 1000^{0.3} \cdot 500^{-0.3} \approx 193.16$$
> 
> ---
> 
> **Paso 3: Cambio aproximado**
> 
> $$\Delta P \approx \frac{\partial P}{\partial K}\Delta K + \frac{\partial P}{\partial L}\Delta L$$
> 
> $$\Delta P \approx 41.39(10) + 193.16(-2)$$
> 
> $$\Delta P \approx 413.9 - 386.32 = 27.58$$
> 
> ---
> 
> **Interpretación:**
> 
> - La producción aumentará aproximadamente **27.58 unidades**
> - Aumentar capital en 10 (miles) aporta +413.9
> - Reducir trabajo en 2 horas resta -386.32
> - Efecto neto: +27.58

### 🌡️ Aplicación 3: Propagación de Errores

> [!example]- 🔬 Ejemplo 9: Medición de Área
> 
> **Problema:** Se mide un rectángulo y se obtiene:
> 
> - Largo: $x = 10.0 \pm 0.1$ cm
> - Ancho: $y = 5.0 \pm 0.05$ cm
> 
> ¿Cuál es el error máximo en el área?
> 
> ---
> 
> **Solución:**
> 
> **Función:** $A(x,y) = xy$
> 
> **Derivadas:**
> 
> $$\frac{\partial A}{\partial x} = y, \quad \frac{\partial A}{\partial y} = x$$
> 
> En $(10, 5)$:
> 
> $$\frac{\partial A}{\partial x}(10,5) = 5, \quad \frac{\partial A}{\partial y}(10,5) = 10$$
> 
> ---
> 
> **Diferencial total:**
> 
> $$dA = \frac{\partial A}{\partial x}dx + \frac{\partial A}{\partial y}dy$$
> 
> $$dA = 5dx + 10dy$$
> 
> ---
> 
> **Error máximo:**
> 
> $$|\Delta A| \approx |dA| = |5dx + 10dy|$$
> 
> Con $|dx| \leq 0.1$ y $|dy| \leq 0.05$:
> 
> $$|\Delta A| \leq 5(0.1) + 10(0.05) = 0.5 + 0.5 = 1.0 \text{ cm}^2$$
> 
> ---
> 
> **Resultado:**
> 
> $$A = 10 \times 5 = 50 \text{ cm}^2$$
> 
> $$A = 50 \pm 1 \text{ cm}^2$$
> 
> **Error relativo:** $\frac{1}{50} = 2%$

### 🏗️ Aplicación 4: Optimización Local

> [!example]- 📐 Ejemplo 10: Condición Necesaria para Extremos
> 
> **Teorema:** Si $f$ es diferenciable en $(x_0, y_0)$ y tiene un **extremo local** (máximo o mínimo) en ese punto, entonces:
> 
> $$f_x(x_0, y_0) = 0 \quad \text{y} \quad f_y(x_0, y_0) = 0$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - El plano tangente debe ser **horizontal**: $z = f(x_0, y_0)$
> - Las derivadas parciales son las pendientes → deben ser cero
> - Los puntos donde esto ocurre se llaman **puntos críticos**
> 
> ---
> 
> **Ejemplo:** Encontrar puntos críticos de $f(x,y) = x^2 + y^2 - 4x - 6y + 13$
> 
> **Derivadas:**
> 
> $$f_x = 2x - 4 = 0 \implies x = 2$$ $$f_y = 2y - 6 = 0 \implies y = 3$$
> 
> **Punto crítico:** $(2, 3)$
> 
> **Valor:** $f(2,3) = 4 + 9 - 8 - 18 + 13 = 0$
> 
> **Plano tangente en $(2, 3, 0)$:**
> 
> $$z = 0 + 0(x-2) + 0(y-3) = 0$$
> 
> (Plano horizontal, como se esperaba)
> 
> ---
> 
> **Nota:** La condición es **necesaria** pero no **suficiente**. Para determinar si es máximo, mínimo o punto silla, necesitamos el **criterio de la segunda derivada** (tema futuro).

---

## 🧮 Diferencial Total

### 📐 Definición del Diferencial

> [!note]- 📋 Diferencial de una Función
> 
> ### Definición
> 
> Si $f$ es diferenciable en $(x, y)$, el **diferencial total** de $f$ es:
> 
> $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$
> 
> donde $dx$ y $dy$ son **incrementos independientes** (diferenciales) de $x$ e $y$.
> 
> ---
> 
> ### Interpretación
> 
> - $df$ representa el **cambio aproximado** en $f$ cuando $x$ cambia en $dx$ e $y$ cambia en $dy$
> - Es la **parte lineal** del cambio total $\Delta f$
> - Equivale a usar el plano tangente para aproximar el cambio
> 
> ---
> 
> ### Relación con el cambio real
> 
> $$\Delta f = f(x + \Delta x, y + \Delta y) - f(x, y)$$
> 
> $$df = f_x(x,y)\Delta x + f_y(x,y)\Delta y$$
> 
> Para cambios pequeños:
> 
> $$\Delta f \approx df$$
> 
> El error $|\Delta f - df|$ es de orden superior: $O(|(\Delta x, \Delta y)|^2)$
> 
> ---
> 
> ### Notación alternativa
> 
> $$df = \nabla f \cdot d\mathbf{r}$$
> 
> donde $\nabla f = (f_x, f_y)$ y $d\mathbf{r} = (dx, dy)$

### Ejemplo 11: Diferencial Total

> [!example]- 📐 Ejemplo 11: Calcular Diferencial
> 
> **Función:** $f(x,y) = x^2y + e^{xy}$
> 
> ---
> 
> **Paso 1: Derivadas parciales**
> 
> $$f_x = 2xy + ye^{xy}$$ $$f_y = x^2 + xe^{xy}$$
> 
> ---
> 
> **Paso 2: Diferencial total**
> 
> $$df = (2xy + ye^{xy})dx + (x^2 + xe^{xy})dy$$
> 
> ---
> 
> **Evaluación en $(1, 0)$:**
> 
> $$f_x(1,0) = 2(1)(0) + 0 \cdot e^0 = 0$$ $$f_y(1,0) = 1^2 + 1 \cdot e^0 = 1 + 1 = 2$$
> 
> $$df|_{(1,0)} = 0 \cdot dx + 2 \cdot dy = 2dy$$
> 
> ---
> 
> **Interpretación:** En $(1, 0)$:
> 
> - Cambios en $x$ no afectan $f$ (en primera aproximación)
> - Un cambio $dy$ en $y$ produce un cambio aproximado $2dy$ en $f$

### Ejemplo 12: Uso del Diferencial

> [!example]- 📐 Ejemplo 12: Estimación con Diferencial
> 
> **Problema:** Una lata cilíndrica tiene radio $r = 5$ cm y altura $h = 10$ cm.
> 
> Volumen: $V = \pi r^2 h$
> 
> Si el radio aumenta 0.1 cm y la altura disminuye 0.2 cm, ¿cuál es el cambio aproximado en el volumen?
> 
> ---
> 
> **Solución:**
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial V}{\partial r} = 2\pi rh$$ $$\frac{\partial V}{\partial h} = \pi r^2$$
> 
> En $(5, 10)$:
> 
> $$\frac{\partial V}{\partial r}(5,10) = 2\pi(5)(10) = 100\pi$$ $$\frac{\partial V}{\partial h}(5,10) = \pi(5)^2 = 25\pi$$
> 
> ---
> 
> **Diferencial:**
> 
> $$dV = 100\pi \cdot dr + 25\pi \cdot dh$$
> 
> Con $dr = 0.1$ y $dh = -0.2$:
> 
> $$dV = 100\pi(0.1) + 25\pi(-0.2)$$ $$= 10\pi - 5\pi$$ $$= 5\pi \approx 15.71 \text{ cm}^3$$
> 
> ---
> 
> **Interpretación:**
> 
> El volumen aumenta aproximadamente **15.71 cm³**
> 
> - Aumento por radio: $+10\pi$ cm³
> - Disminución por altura: $-5\pi$ cm³
> - Efecto neto: $+5\pi$ cm³

---

## 🎨 Visualización: Superficie vs Plano Tangente

> [!note]- 🖼️ Comparación Gráfica Detallada
> 
> ### Para $f(x,y) = x^2 + y^2$ en $(1, 1)$
> 
> **Valores importantes:**
> 
> - $f(1,1) = 2$
> - $f_x(1,1) = 2$
> - $f_y(1,1) = 2$
> - Plano tangente: $z = 2 + 2(x-1) + 2(y-1) = 2x + 2y - 2$
> 
> ---
> 
> ### Tabla de Comparación
> 
> |Punto $(x,y)$|$f(x,y)$ (exacto)|$L(x,y)$ (plano)|Error|
> |---|---|---|---|
> |$(1.0, 1.0)$|$2.000$|$2.000$|$0.000$|
> |$(1.1, 1.0)$|$2.210$|$2.200$|$0.010$|
> |$(1.0, 1.1)$|$2.210$|$2.200$|$0.010$|
> |$(1.1, 1.1)$|$2.420$|$2.400$|$0.020$|
> |$(1.2, 1.2)$|$2.880$|$2.800$|$0.080$|
> |$(1.5, 1.5)$|$4.500$|$4.000$|$0.500$|
> 
> **Observación:** El error crece con la distancia al punto de tangencia.
> 
> ---
> 
> ### Visualización 3D (ASCII Art)
> 
> ```
>         z
>         |
>       4 |      /•\  Paraboloide
>         |     / | \
>       3 |    /  |  \
>         |   /   |   \
>       2 |  •----•----• Plano tangente (z = 2x+2y-2)
>         | /     |(1,1,2)
>       1 |/______|______
>         +-------+------- y
>        /        1
>       x
> ```
> 
> **Cerca del punto de tangencia:** superficie ≈ plano
> 
> **Lejos del punto:** el paraboloide se curva alejándose del plano

---

## ⚠️ Casos Especiales y Contraejemplos

### 🚫 Contraejemplo 1: Derivadas Existen pero No Diferenciable

> [!warning]- ⚠️ Ejemplo Patológico
> 
> **Función:**
> 
> $$f(x,y) = \begin{cases} \frac{x^2y}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> ---
> 
> **En el origen:**
> 
> **Derivadas parciales:**
> 
> $$f_x(0,0) = \lim_{h \to 0} \frac{f(h,0) - 0}{h} = \lim_{h \to 0} \frac{0}{h} = 0$$
> 
> $$f_y(0,0) = \lim_{h \to 0} \frac{f(0,h) - 0}{h} = \lim_{h \to 0} \frac{0}{h} = 0$$
> 
> ✅ **Las derivadas parciales existen**
> 
> ---
> 
> **Verificar diferenciabilidad:**
> 
> Aproximación lineal: $L(x,y) = 0$
> 
> Error: $E(x,y) = f(x,y) - 0 = \frac{x^2y}{x^2 + y^2}$
> 
> Debemos verificar si:
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^2y/(x^2+y^2)}{\sqrt{x^2+y^2}} = 0$$
> 
> Por la recta $y = x$:
> 
> $$\lim_{t \to 0} \frac{t^2 \cdot t/(2t^2)}{\sqrt{2}t} = \lim_{t \to 0} \frac{t/2}{\sqrt{2}t} = \frac{1}{2\sqrt{2}} \neq 0$$
> 
> ❌ **La función NO es diferenciable en $(0,0)$**
> 
> ---
> 
> **Conclusión:** Las derivadas parciales existen pero la función **no es diferenciable**.

### 🚫 Contraejemplo 2: Derivadas Parciales Discontinuas

> [!warning]- ⚠️ Derivadas No Continuas
> 
> **Función:**
> 
> $$f(x,y) = \begin{cases} xy\frac{x^2 - y^2}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> ---
> 
> **Propiedades:**
> 
> 1. Las derivadas parciales **existen** en todo punto
> 2. En $(0,0)$: $f_x(0,0) = 0$ y $f_y(0,0) = 0$
> 3. Pero las derivadas parciales **no son continuas** en $(0,0)$
> 
> ---
> 
> **Consecuencia:**
> 
> - No podemos usar el teorema de derivadas continuas
> - Debemos verificar diferenciabilidad directamente
> - En este caso particular, resulta que **SÍ es diferenciable** (pero es difícil de probar)

### ✅ Ejemplo: Diferenciable pero No $C^1$

> [!note]- 🔍 Caso Interesante
> 
> **Función:**
> 
> $$f(x,y) = \begin{cases} (x^2 + y^2)\sin\left(\frac{1}{\sqrt{x^2+y^2}}\right) & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **Propiedades:**
> 
> - $f$ es diferenciable en $(0,0)$
> - $f_x$ y $f_y$ existen en todo punto
> - Pero $f_x$ y $f_y$ **NO son continuas** en $(0,0)$
> 
> **Conclusión:** La diferenciabilidad no implica que las derivadas sean continuas (aunque el recíproco sí es cierto).

---

## 🔧 Técnicas de Cálculo

### 📝 Algoritmo para Encontrar el Plano Tangente

> [!tip]- ✅ Método Paso a Paso
> 
> **Dado:** Superficie $z = f(x,y)$ y punto $(x_0, y_0)$
> 
> **Objetivo:** Encontrar el plano tangente
> 
> ---
> 
> ### Paso 1: Calcular $f(x_0, y_0)$
> 
> Evaluar la función en el punto dado.
> 
> ---
> 
> ### Paso 2: Calcular derivadas parciales
> 
> $$f_x(x,y) = \frac{\partial f}{\partial x}$$ $$f_y(x,y) = \frac{\partial f}{\partial y}$$
> 
> ---
> 
> ### Paso 3: Evaluar derivadas en el punto
> 
> $$f_x(x_0, y_0), \quad f_y(x_0, y_0)$$
> 
> ---
> 
> ### Paso 4: Escribir ecuación del plano
> 
> **Forma punto-pendiente:**
> 
> $$z - f(x_0, y_0) = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$
> 
> **O simplificar a la forma:**
> 
> $$z = Ax + By + C$$
> 
> ---
> 
> ### Paso 5: Verificación (opcional)
> 
> Comprobar que el punto $(x_0, y_0, f(x_0, y_0))$ satisface la ecuación.

### 📊 Algoritmo para Verificar Diferenciabilidad

> [!tip]- ✅ Método de Verificación
> 
> **Dado:** Función $f(x,y)$ y punto $(x_0, y_0)$
> 
> **Objetivo:** Determinar si $f$ es diferenciable en el punto
> 
> ---
> 
> ### Método 1: Derivadas Continuas (Más fácil)
> 
> 1. Calcular $f_x(x,y)$ y $f_y(x,y)$
> 2. Verificar si son **continuas** en $(x_0, y_0)$
> 3. Si SÍ → $f$ es diferenciable ✓
> 4. Si NO → usar Método 2
> 
> ---
> 
> ### Método 2: Verificación Directa (Más complejo)
> 
> 1. Calcular $f_x(x_0, y_0)$ y $f_y(x_0, y_0)$
> 2. Formar aproximación lineal: $$L(x,y) = f(x_0,y_0) + f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)$$
> 3. Calcular error: $$E(x,y) = f(x,y) - L(x,y)$$
> 4. Verificar si: $$\lim_{(x,y) \to (x_0,y_0)} \frac{E(x,y)}{\sqrt{(x-x_0)^2 + (y-y_0)^2}} = 0$$
> 5. Si el límite es 0 → diferenciable ✓
> 6. Si el límite no existe o ≠ 0 → no diferenciable ✗

---

## 📚 Ejemplos Avanzados

### Ejemplo 13: Superficie Implícita

> [!example]- 📐 Ejemplo 13: Plano Tangente a Superficie Implícita
> 
> **Superficie:** $x^2 + y^2 + z^2 = 14$
> 
> **Punto:** $(1, 2, 3)$
> 
> ---
> 
> **Método: Gradiente**
> 
> Definimos $F(x,y,z) = x^2 + y^2 + z^2$, entonces la superficie es $F = 14$.
> 
> **Gradiente:**
> 
> $$\nabla F = (2x, 2y, 2z)$$
> 
> En $(1, 2, 3)$:
> 
> $$\nabla F(1,2,3) = (2, 4, 6)$$
> 
> Este es el **vector normal** al plano tangente.
> 
> ---
> 
> **Ecuación del plano tangente:**
> 
> $$2(x - 1) + 4(y - 2) + 6(z - 3) = 0$$
> 
> $$2x + 4y + 6z = 2 + 8 + 18 = 28$$
> 
> $$\boxed{x + 2y + 3z = 14}$$
> 
> (dividiendo por 2)
> 
> ---
> 
> **Verificación:** El punto $(1, 2, 3)$ satisface:
> 
> $$1 + 2(2) + 3(3) = 1 + 4 + 9 = 14$$ ✓

### Ejemplo 14: Optimización con Diferenciabilidad

> [!example]- 📐 Ejemplo 14: Encontrar Extremos
> 
> **Función:** $f(x,y) = x^2 + y^2 - 2x - 4y + 5$
> 
> **Encontrar puntos críticos y clasificarlos**
> 
> ---
> 
> **Paso 1: Derivadas parciales**
> 
> $$f_x = 2x - 2$$ $$f_y = 2y - 4$$
> 
> ---
> 
> **Paso 2: Puntos críticos**
> 
> Resolver $f_x = 0$ y $f_y = 0$:
> 
> $$2x - 2 = 0 \implies x = 1$$ $$2y - 4 = 0 \implies y = 2$$
> 
> **Punto crítico:** $(1, 2)$
> 
> ---
> 
> **Paso 3: Valor en el punto crítico**
> 
> $$f(1, 2) = 1 + 4 - 2 - 8 + 5 = 0$$
> 
> ---
> 
> **Paso 4: Completar cuadrados (para clasificar)**
> 
> $$f(x,y) = (x^2 - 2x + 1) + (y^2 - 4y + 4) + 5 - 1 - 4$$
> 
> $$= (x-1)^2 + (y-2)^2$$
> 
> Como $(x-1)^2 + (y-2)^2 \geq 0$ con igualdad solo en $(1, 2)$:
> 
> $$\boxed{f(1, 2) = 0 \text{ es un MÍNIMO ABSOLUTO}}$$
> 
> ---
> 
> **Plano tangente en el mínimo:**
> 
> $$z = 0 + 0(x-1) + 0(y-2) = 0$$
> 
> (Plano horizontal, como esperábamos)

### Ejemplo 15: Aproximación de Funciones Complicadas

> [!example]- 📐 Ejemplo 15: Función Compleja
> 
> **Función:** $f(x,y) = e^{x} \sin(y) + \ln(1 + x + y)$
> 
> **Aproximar cerca de $(0, 0)$**
> 
> ---
> 
> **Paso 1: Valor en $(0, 0)$**
> 
> $$f(0, 0) = e^0 \sin(0) + \ln(1) = 0 + 0 = 0$$
> 
> ---
> 
> **Paso 2: Derivadas parciales**
> 
> $$f_x = e^x \sin(y) + \frac{1}{1+x+y}$$
> 
> $$f_y = e^x \cos(y) + \frac{1}{1+x+y}$$
>
> ---
> 
> **Paso 3: Evaluar en $(0, 0)$**
> 
> $$f_x(0,0) = e^0 \sin(0) + \frac{1}{1+0+0} = 0 + 1 = 1$$
> 
> $$f_y(0,0) = e^0 \cos(0) + \frac{1}{1+0+0} = 1 + 1 = 2$$
> 
> ---
> 
> **Paso 4: Aproximación lineal**
> 
> $$L(x,y) = 0 + 1 \cdot x + 2 \cdot y$$
> 
> $$\boxed{f(x,y) \approx x + 2y \text{ cerca de } (0,0)}$$
> 
> ---
> 
> **Verificación numérica:**
> 
> |Punto|$f(x,y)$ (exacto)|$L(x,y)$ (aprox)|Error|
> |---|---|---|---|
> |$(0.1, 0.1)$|$0.2953$|$0.3000$|$0.0047$|
> |$(0.2, 0.1)$|$0.3921$|$0.4000$|$0.0079$|
> |$(-0.1, 0.1)$|$0.0953$|$0.1000$|$0.0047$|
> 
> La aproximación es muy buena para valores pequeños.

---

## 🌍 Diferenciabilidad en Tres Variables

### 📋 Extensión a $\mathbb{R}^3$

> [!note]- 🎲 Diferenciabilidad en Tres Variables
> 
> ### Definición
> 
> Una función $f: \mathbb{R}^3 \to \mathbb{R}$ es **diferenciable** en $(x_0, y_0, z_0)$ si:
> 
> $$f(x,y,z) = f(x_0,y_0,z_0) + f_x(x_0,y_0,z_0)(x-x_0)$$ $$+ f_y(x_0,y_0,z_0)(y-y_0) + f_z(x_0,y_0,z_0)(z-z_0) + E(x,y,z)$$
> 
> donde:
> 
> $$\lim_{(x,y,z) \to (x_0,y_0,z_0)} \frac{E(x,y,z)}{\sqrt{(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2}} = 0$$
> 
> ---
> 
> ### Interpretación
> 
> - En 2D: plano tangente
> - En 3D: **hiperplano tangente** (en $\mathbb{R}^4$)
> - La función se aproxima por una función **lineal afín**
> 
> ---
> 
> ### Diferencial total
> 
> $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz$$
> 
> $$df = \nabla f \cdot d\mathbf{r}$$
> 
> donde $\nabla f = (f_x, f_y, f_z)$ y $d\mathbf{r} = (dx, dy, dz)$

### Ejemplo 16: Función de Tres Variables

> [!example]- 📐 Ejemplo 16: Temperatura en 3D
> 
> **Función:** $T(x,y,z) = 100e^{-(x^2+y^2+z^2)}$
> 
> Representa temperatura en un punto del espacio.
> 
> **Punto:** $(0, 0, 0)$
> 
> ---
> 
> **Paso 1: Valor**
> 
> $$T(0,0,0) = 100e^0 = 100$$
> 
> ---
> 
> **Paso 2: Derivadas parciales**
> 
> $$\frac{\partial T}{\partial x} = 100e^{-(x^2+y^2+z^2)} \cdot (-2x) = -200xe^{-(x^2+y^2+z^2)}$$
> 
> Por simetría:
> 
> $$\frac{\partial T}{\partial y} = -200ye^{-(x^2+y^2+z^2)}$$
> 
> $$\frac{\partial T}{\partial z} = -200ze^{-(x^2+y^2+z^2)}$$
> 
> ---
> 
> **Paso 3: Evaluar en el origen**
> 
> $$T_x(0,0,0) = -200(0)e^0 = 0$$ $$T_y(0,0,0) = 0$$ $$T_z(0,0,0) = 0$$
> 
> ---
> 
> **Paso 4: Aproximación lineal**
> 
> $$T(x,y,z) \approx 100 + 0 \cdot x + 0 \cdot y + 0 \cdot z = 100$$
> 
> ---
> 
> **Interpretación:**
> 
> - En el origen, la temperatura es máxima (100°)
> - Las derivadas son cero → es un **punto crítico**
> - La aproximación lineal es constante (hiperplano horizontal)

---

## 🔗 Relación con Otros Conceptos

### 📊 Jerarquía de Propiedades

> [!note]- 🌳 Diagrama de Implicaciones
> 
> ```
> Clase C² (derivadas segundas continuas)
>                 ↓
> Clase C¹ (derivadas primeras continuas)
>                 ↓
>         DIFERENCIABLE
>            ↙    ↘
> Derivadas         Continua
> parciales           ↓
> existen          Límite
>                  existe
> ```
> 
> ---
> 
> ### Resumen de implicaciones
> 
> ✅ $f \in C^1$ ⟹ $f$ diferenciable
> 
> ✅ $f$ diferenciable ⟹ $f$ continua
> 
> ✅ $f$ diferenciable ⟹ $f_x, f_y$ existen
> 
> ❌ $f_x, f_y$ existen ⟹ $f$ diferenciable (FALSO)
> 
> ❌ $f$ continua ⟹ $f_x, f_y$ existen (FALSO)
> 
> ❌ $f$ diferenciable ⟹ $f \in C^1$ (FALSO, pero casi)

### 🔄 Conexión con Derivada Direccional

> [!note]- 🎯 Relación con Derivadas Direccionales
> 
> ### Teorema
> 
> Si $f$ es **diferenciable** en $(x_0, y_0)$, entonces $f$ tiene **derivada direccional** en cualquier dirección $\mathbf{u} = (u_1, u_2)$ con $|\mathbf{u}| = 1$:
> 
> $$D_{\mathbf{u}}f(x_0, y_0) = \nabla f(x_0, y_0) \cdot \mathbf{u}$$
> 
> $$= f_x(x_0, y_0)u_1 + f_y(x_0, y_0)u_2$$
> 
> ---
> 
> ### Interpretación
> 
> - Las derivadas parciales son casos especiales:
>     - $f_x = D_{(1,0)}f$ (dirección del eje $x$)
>     - $f_y = D_{(0,1)}f$ (dirección del eje $y$)
> - La diferenciabilidad garantiza que **todas las derivadas direccionales existan**
> 
> ---
> 
> ### Recíproco (FALSO)
> 
> La existencia de todas las derivadas direccionales **NO** implica diferenciabilidad.
> 
> **Contraejemplo:** La función del cono
> 
> $$f(x,y) = \sqrt{x^2 + y^2}$$
> 
> tiene todas las derivadas direccionales en $(0,0)$, pero **no es diferenciable** allí.

---

## 🎓 Teoremas Importantes

### 📐 Teorema del Valor Medio (Multivariable)

> [!note]- 🎯 Teorema del Valor Medio
> 
> **Teorema:** Si $f$ es diferenciable en todos los puntos del segmento que une $(x_0, y_0)$ con $(x_0 + h, y_0 + k)$, entonces existe un punto $(x_0 + \theta h, y_0 + \theta k)$ con $0 < \theta < 1$ tal que:
> 
> $$f(x_0 + h, y_0 + k) - f(x_0, y_0) = f_x(x_0 + \theta h, y_0 + \theta k) \cdot h$$ $$+ f_y(x_0 + \theta h, y_0 + \theta k) \cdot k$$
> 
> ---
> 
> ### Consecuencia
> 
> Si $|f_x| \leq M$ y $|f_y| \leq M$ en una región, entonces:
> 
> $$|f(x_1, y_1) - f(x_2, y_2)| \leq M\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2} \cdot \sqrt{2}$$
> 
> Esto da una **cota para el cambio** de la función.

### 📊 Teorema de la Función Implícita

> [!note]- 🔍 Función Implícita (Adelanto)
> 
> **Teorema:** Si $F(x, y, z) = 0$ define implícitamente $z = f(x, y)$ cerca de un punto $(x_0, y_0, z_0)$ donde:
> 
> - $F$ es diferenciable
> - $F(x_0, y_0, z_0) = 0$
> - $\frac{\partial F}{\partial z}(x_0, y_0, z_0) \neq 0$
> 
> Entonces las derivadas parciales de $z$ con respecto a $x$ e $y$ son:
> 
> $$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$$
> 
> ---
> 
> ### Ejemplo aplicado
> 
> Para la esfera $x^2 + y^2 + z^2 = 1$:
> 
> $F(x,y,z) = x^2 + y^2 + z^2 - 1$
> 
> $$F_x = 2x, \quad F_y = 2y, \quad F_z = 2z$$
> 
> $$\frac{\partial z}{\partial x} = -\frac{2x}{2z} = -\frac{x}{z}$$
> 
> $$\frac{\partial z}{\partial y} = -\frac{2y}{2z} = -\frac{y}{z}$$
> 
> Estas son exactamente las pendientes del plano tangente a la esfera.

---

## 💡 Aplicaciones Avanzadas

### 🤖 Aplicación 5: Machine Learning - Gradiente Descendente

> [!example]- 🧠 Ejemplo 17: Optimización en ML
> 
> **Contexto:** En machine learning, queremos minimizar una función de costo $C(\mathbf{w})$ donde $\mathbf{w} = (w_1, w_2, \ldots, w_n)$ son los pesos del modelo.
> 
> ---
> 
> ### Algoritmo de Gradiente Descendente
> 
> **Idea:** Moverse en la dirección opuesta al gradiente (máximo descenso).
> 
> **Iteración:**
> 
> $$\mathbf{w}^{(k+1)} = \mathbf{w}^{(k)} - \alpha \nabla C(\mathbf{w}^{(k)})$$
> 
> donde $\alpha > 0$ es la **tasa de aprendizaje** (learning rate).
> 
> ---
> 
> ### Ejemplo en 2D
> 
> **Función de costo:** $C(w_1, w_2) = w_1^2 + 4w_2^2$
> 
> **Gradiente:**
> 
> $$\nabla C = (2w_1, 8w_2)$$
> 
> **Punto inicial:** $(w_1, w_2) = (4, 2)$
> 
> **Tasa de aprendizaje:** $\alpha = 0.1$
> 
> ---
> 
> **Iteración 1:**
> 
> $$\nabla C(4, 2) = (8, 16)$$
> 
> $$(w_1, w_2)^{(1)} = (4, 2) - 0.1(8, 16) = (3.2, 0.4)$$
> 
> **Iteración 2:**
> 
> $$\nabla C(3.2, 0.4) = (6.4, 3.2)$$
> 
> $$(w_1, w_2)^{(2)} = (3.2, 0.4) - 0.1(6.4, 3.2) = (2.56, 0.08)$$
> 
> **Iteración 3:**
> 
> $$\nabla C(2.56, 0.08) = (5.12, 0.64)$$
> 
> $$(w_1, w_2)^{(3)} = (2.56, 0.08) - 0.1(5.12, 0.64) = (2.048, 0.016)$$
> 
> ---
> 
> **Convergencia:** El algoritmo converge a $(0, 0)$, el mínimo global de $C$.
> 
> **Papel de la diferenciabilidad:** Garantiza que el gradiente existe y apunta en la dirección de máximo crecimiento.

### 🌊 Aplicación 6: Física - Potencial y Campo

> [!example]- ⚡ Ejemplo 18: Potencial Eléctrico
> 
> **Potencial eléctrico** en el espacio:
> 
> $$V(x,y,z) = \frac{kQ}{\sqrt{x^2 + y^2 + z^2}}$$
> 
> donde $k$ es la constante de Coulomb y $Q$ la carga.
> 
> ---
> 
> ### Campo eléctrico
> 
> El **campo eléctrico** es el negativo del gradiente del potencial:
> 
> $$\mathbf{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}, \frac{\partial V}{\partial y}, \frac{\partial V}{\partial z}\right)$$
> 
> ---
> 
> **Cálculo:**
> 
> $$\frac{\partial V}{\partial x} = kQ \cdot \frac{\partial}{\partial x}(x^2+y^2+z^2)^{-1/2}$$
> 
> $$= kQ \cdot \left(-\frac{1}{2}\right)(x^2+y^2+z^2)^{-3/2} \cdot 2x$$
> 
> $$= -\frac{kQx}{(x^2+y^2+z^2)^{3/2}}$$
> 
> Por simetría:
> 
> $$\mathbf{E} = \frac{kQ}{(x^2+y^2+z^2)^{3/2}}(x, y, z) = \frac{kQ}{r^3}\mathbf{r}$$
> 
> donde $\mathbf{r} = (x, y, z)$ y $r = |\mathbf{r}|$.
> 
> ---
> 
> **Interpretación:** El campo eléctrico apunta radialmente hacia afuera (si $Q > 0$) y su magnitud decrece con $1/r^2$.

### 🏔️ Aplicación 7: Topografía - Curvas de Nivel

> [!example]- 🗺️ Ejemplo 19: Mapa Topográfico
> 
> **Función de elevación:** $h(x,y) = 1000 - x^2 - 2y^2$
> 
> Representa la altura de una montaña.
> 
> ---
> 
> ### Gradiente
> 
> $$\nabla h = (-2x, -4y)$$
> 
> ---
> 
> ### Interpretación
> 
> - El gradiente $\nabla h$ apunta en la dirección de **máximo ascenso**
> - Es **perpendicular** a las curvas de nivel $h(x,y) = c$
> - Su magnitud $|\nabla h| = \sqrt{4x^2 + 16y^2}$ indica la "pendiente"
> 
> ---
> 
> ### En el punto $(5, 3)$:
> 
> $$h(5, 3) = 1000 - 25 - 18 = 957 \text{ metros}$$
> 
> $$\nabla h(5, 3) = (-10, -12)$$
> 
> **Dirección de máximo ascenso:** $(10, 12)$ (opuesta al gradiente negativo)
> 
> **Pendiente máxima:** $|\nabla h| = \sqrt{100 + 144} = \sqrt{244} \approx 15.62$
> 
> ---
> 
> ### Plano tangente
> 
> Representa el **suelo local** en ese punto:
> 
> $$z = 957 - 10(x - 5) - 12(y - 3)$$
> 
> $$z = 957 - 10x + 50 - 12y + 36$$
> 
> $$z = -10x - 12y + 1043$$

---

## 🔢 Fórmulas de Referencia Rápida

> [!note]- 📋 Tabla de Fórmulas Esenciales
> 
> ### Diferenciabilidad
> 
> $$f(x,y) = f(x_0,y_0) + f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0) + o(|\mathbf{h}|)$$
> 
> ---
> 
> ### Plano Tangente
> 
> $$z = f(x_0,y_0) + f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)$$
> 
> ---
> 
> ### Vector Normal
> 
> $$\mathbf{n} = (f_x(x_0,y_0), f_y(x_0,y_0), -1)$$
> 
> ---
> 
> ### Diferencial Total
> 
> $$df = f_x , dx + f_y , dy$$
> 
> $$df = \nabla f \cdot d\mathbf{r}$$
> 
> ---
> 
> ### Aproximación Lineal
> 
> $$\Delta f \approx f_x(x_0,y_0)\Delta x + f_y(x_0,y_0)\Delta y$$
> 
> ---
> 
> ### Condición Suficiente
> 
> $$f_x, f_y \text{ continuas} \implies f \text{ diferenciable}$$
> 
> ---
> 
> ### Superficie Implícita
> 
> Para $F(x,y,z) = c$:
> 
> $$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$$

---

## 🎯 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular el plano tangente:**
> 
> a) $f(x,y) = x^2 + y^2$ en $(1, 1)$
> 
> b) $f(x,y) = xy$ en $(2, 3)$
> 
> c) $f(x,y) = e^{x+y}$ en $(0, 0)$
> 
> d) $f(x,y) = \sin(x)\cos(y)$ en $(\pi/2, 0)$
> 
> e) $f(x,y) = \ln(x^2 + y^2)$ en $(1, 0)$
> 
> f) $f(x,y) = \sqrt{x^2 + y^2}$ en $(3, 4)$
> 
> ---
> 
> **2. Aproximación lineal:**
> 
> a) Estimar $f(1.1, 0.9)$ donde $f(x,y) = x^2y$ usando $(1, 1)$
> 
> b) Estimar $f(2.05, 2.98)$ donde $f(x,y) = \frac{x}{y}$ usando $(2, 3)$
> 
> c) Estimar $\sqrt{(3.02)^2 + (3.97)^2}$ usando $f(x,y) = \sqrt{x^2+y^2}$ en $(3, 4)$
> 
> ---
> 
> **3. Vector normal:**
> 
> Encontrar un vector normal al plano tangente:
> 
> a) $z = x^2 + y^2$ en $(1, 2)$
> 
> b) $z = xy^2$ en $(1, 1)$
> 
> c) $z = e^{xy}$ en $(0, 1)$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Verificar diferenciabilidad:**
> 
> a) $f(x,y) = \begin{cases} \frac{xy^2}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$
> 
> b) $f(x,y) = |xy|$ en $(0, 0)$
> 
> c) $f(x,y) = \sqrt[3]{xy}$ en $(0, 0)$
> 
> ---
> 
> **5. Superficies implícitas:**
> 
> Encontrar el plano tangente:
> 
> a) $x^2 + y^2 + z^2 = 9$ en $(2, 2, 1)$
> 
> b) $xyz = 8$ en $(1, 2, 4)$
> 
> c) $z = x^2 - y^2$ en $(1, 1, 0)$ (superficie de silla)
> 
> ---
> 
> **6. Propagación de errores:**
> 
> a) El volumen de un cono es $V = \frac{1}{3}\pi r^2 h$. Si $r = 5 \pm 0.1$ cm y $h = 12 \pm 0.2$ cm, estimar el error en $V$.
> 
> b) La ley de gases ideales: $PV = nRT$. Si $V = 10 \pm 0.1$ L y $T = 300 \pm 2$ K, estimar el error en $P$ (con $n, R$ constantes).
> 
> ---
> 
> **7. Diferencial total:**
> 
> Calcular $df$:
> 
> a) $f(x,y) = x^3y^2 + xy$
> 
> b) $f(x,y) = e^{xy}\ln(x+y)$
> 
> c) $f(x,y,z) = xyz + x^2 + y^2 + z^2$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **8. Problemas teóricos:**
> 
> a) Demostrar que si $f$ es diferenciable en $(x_0, y_0)$, entonces $f$ es continua en ese punto.
> 
> b) Dar un ejemplo de función con derivadas parciales en $(0,0)$ pero que no sea diferenciable allí.
> 
> c) Si $f$ y $g$ son diferenciables, demostrar que $fg$ es diferenciable y encontrar su plano tangente.
> 
> ---
> 
> **9. Optimización:**
> 
> a) Encontrar puntos críticos de $f(x,y) = x^3 + y^3 - 3xy$ y calcular el plano tangente en cada uno.
> 
> b) La temperatura en una placa es $T(x,y) = 100 - x^2 - y^2$. ¿Dónde es el plano tangente horizontal?
> 
> ---
> 
> **10. Aplicaciones:**
> 
> a) Una caja rectangular tiene dimensiones $x = 10$, $y = 8$, $z = 6$ cm (todas con error de $\pm 0.1$ cm). Estimar el error máximo en el volumen.
> 
> b) La función de producción es $P(K,L) = 50K^{0.4}L^{0.6}$. Si $K$ aumenta 2% y $L$ disminuye 1%, ¿cuál es el cambio porcentual aproximado en $P$?
> 
> ---
> 
> **11. Tres variables:**
> 
> a) Encontrar el "hiperplano tangente" a $w = xyz$ en $(1, 2, 3)$
> 
> b) Para $f(x,y,z) = x^2 + y^2 + z^2$, calcular $df$ y evaluar en $(1,1,1)$ con $(dx, dy, dz) = (0.1, -0.1, 0.2)$

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = x^2 + y^2$ en $(1, 1)$
> 
> $f(1,1) = 2$
> 
> $f_x(1,1) = 2$, $f_y(1,1) = 2$
> 
> $$\boxed{z = 2 + 2(x-1) + 2(y-1) = 2x + 2y - 2}$$
> 
> ---
> 
> **1b)** $f(x,y) = xy$ en $(2, 3)$
> 
> $f(2,3) = 6$
> 
> $f_x(2,3) = 3$, $f_y(2,3) = 2$
> 
> $$\boxed{z = 6 + 3(x-2) + 2(y-3) = 3x + 2y - 6}$$
> 
> ---
> 
> **2a)** $f(x,y) = x^2y$ usando $(1, 1)$
> 
> $f(1,1) = 1$
> 
> $f_x(1,1) = 2(1)(1) = 2$, $f_y(1,1) = (1)^2 = 1$
> 
> $$L(x,y) = 1 + 2(x-1) + 1(y-1)$$
> 
> $$f(1.1, 0.9) \approx 1 + 2(0.1) + 1(-0.1) = 1 + 0.2 - 0.1 = 1.1$$
> 
> (Valor exacto: $1.089$, error: $0.011$)
> 
> ---
> 
> **3a)** $z = x^2 + y^2$ en $(1, 2)$
> 
> $f_x(1,2) = 2$, $f_y(1,2) = 4$
> 
> $$\boxed{\mathbf{n} = (2, 4, -1)}$$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $f(x,y) = \frac{xy^2}{x^2+y^2}$ en $(0,0)$
> 
> $f_x(0,0) = 0$, $f_y(0,0) = 0$ (calcular por definición)
> 
> Aproximación lineal: $L(x,y) = 0$
> 
> Error: $E(x,y) = \frac{xy^2}{x^2+y^2}$
> 
> Por $y = x$: $\frac{x \cdot x^2}{2x^2} = \frac{x}{2}$
> 
> $$\lim_{x \to 0} \frac{x/2}{\sqrt{2}|x|} = \frac{1}{2\sqrt{2}} \neq 0$$
> 
> $$\boxed{\text{NO es diferenciable}}$$
> 
> ---
> 
> **5a)** $x^2 + y^2 + z^2 = 9$ en $(2, 2, 1)$
> 
> $F = x^2 - y^2 + z^2 - 9$
> $\nabla F = (2x, 2y, 2z)$ en $(2, 2, 1)$ es $(4, 4, 2)$
> 
> Plano tangente:
> 
> $$4(x-2) + 4(y-2) + 2(z-1) = 0$$
> 
> $$4x + 4y + 2z = 8 + 8 + 2 = 18$$
> 
> $$\boxed{2x + 2y + z = 9}$$
> 
> ---
> 
> **6a)** $V = \frac{1}{3}\pi r^2 h$, $r = 5 \pm 0.1$, $h = 12 \pm 0.2$
> 
> $$\frac{\partial V}{\partial r} = \frac{2\pi rh}{3}, \quad \frac{\partial V}{\partial h} = \frac{\pi r^2}{3}$$
> 
> En $(5, 12)$:
> 
> $$\frac{\partial V}{\partial r} = \frac{2\pi(5)(12)}{3} = 40\pi$$
> 
> $$\frac{\partial V}{\partial h} = \frac{\pi(25)}{3} = \frac{25\pi}{3}$$
> 
> $$|dV| \leq 40\pi(0.1) + \frac{25\pi}{3}(0.2) = 4\pi + \frac{5\pi}{3} = \frac{17\pi}{3} \approx 17.8 \text{ cm}^3$$
> 
> $$V = \frac{\pi(25)(12)}{3} = 100\pi \approx 314.2 \text{ cm}^3$$
> 
> $$\boxed{V = 100\pi \pm \frac{17\pi}{3} \text{ cm}^3}$$
> 
> ---
> 
> **7a)** $f(x,y) = x^3y^2 + xy$
> 
> $$f_x = 3x^2y^2 + y$$ $$f_y = 2x^3y + x$$
> 
> $$\boxed{df = (3x^2y^2 + y)dx + (2x^3y + x)dy}$$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **8a)** Demostración de continuidad
> 
> **Tesis:** Si $f$ es diferenciable en $(x_0, y_0)$, entonces es continua.
> 
> **Demostración:**
> 
> Por diferenciabilidad:
> 
> $$f(x,y) = f(x_0,y_0) + f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0) + E(x,y)$$
> 
> donde:
> 
> $$\lim_{(x,y) \to (x_0,y_0)} \frac{E(x,y)}{\sqrt{(x-x_0)^2 + (y-y_0)^2}} = 0$$
> 
> Esto implica $\lim_{(x,y) \to (x_0,y_0)} E(x,y) = 0$.
> 
> Tomando límites:
> 
> $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = f(x_0,y_0) + 0 + 0 + 0 = f(x_0,y_0)$$
> 
> Por lo tanto $f$ es continua. ∎
> 
> ---
> 
> **9a)** $f(x,y) = x^3 + y^3 - 3xy$
> 
> $$f_x = 3x^2 - 3y = 0 \implies x^2 = y$$ $$f_y = 3y^2 - 3x = 0 \implies y^2 = x$$
> 
> De la segunda: $x = y^2$. Sustituyendo en la primera:
> 
> $$(y^2)^2 = y \implies y^4 = y \implies y(y^3 - 1) = 0$$
> 
> $$y = 0 \text{ o } y = 1$$
> 
> **Puntos críticos:**
> 
> - $y = 0 \implies x = 0$: punto $(0, 0)$
> - $y = 1 \implies x = 1$: punto $(1, 1)$
> 
> **En $(0, 0)$:**
> 
> $f(0,0) = 0$, plano tangente: $z = 0$
> 
> **En $(1, 1)$:**
> 
> $f(1,1) = 1 + 1 - 3 = -1$, plano tangente: $z = -1$
> 
> ---
> 
> **10b)** $P(K,L) = 50K^{0.4}L^{0.6}$
> 
> $$\frac{\partial P}{\partial K} = 50(0.4)K^{-0.6}L^{0.6} = 20K^{-0.6}L^{0.6}$$
> 
> $$\frac{\partial P}{\partial L} = 50(0.6)K^{0.4}L^{-0.4} = 30K^{0.4}L^{-0.4}$$
> 
> Cambio relativo:
> 
> $$\frac{dP}{P} = \frac{1}{P}\left(\frac{\partial P}{\partial K}dK + \frac{\partial P}{\partial L}dL\right)$$
> 
> $$= \frac{20K^{-0.6}L^{0.6}}{50K^{0.4}L^{0.6}}dK + \frac{30K^{0.4}L^{-0.4}}{50K^{0.4}L^{0.6}}dL$$
> 
> $$= \frac{0.4}{K}dK + \frac{0.6}{L}dL$$
> 
> Con $\frac{dK}{K} = 0.02$ y $\frac{dL}{L} = -0.01$:
> 
> $$\frac{dP}{P} = 0.4(0.02) + 0.6(-0.01) = 0.008 - 0.006 = 0.002$$
> 

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Diferenciabilidad
> 
> ✅ **Definición:**
> 
> - $f$ diferenciable ⟺ puede aproximarse por una función lineal.
>     
> - El error de aproximación es de **orden superior**.
>     
> 
> ✅ **Condición suficiente (más usada):**
> 
> - Si $f_x$ y $f_y$ son **continuas** → $f$ es diferenciable.
>     
> - Prácticamente todas las funciones “usuales” cumplen esto.
>     
> 
> ✅ **No confundir:**
> 
> - Derivadas parciales existen ≠ Diferenciabilidad.
>     
> - La diferenciabilidad es una condición más fuerte.
>     
> 
> ---
> 
> ### Sobre Plano Tangente
> 
> ✅ **Ecuación estándar:**  
> $$z = f(x_0,y_0) + f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)$$
> 
> ✅ **Interpretación:**
> 
> - Mejor aproximación lineal de la superficie.
>     
> - Contiene las rectas tangentes en direcciones $x$ e $y$.
>     
> - Es horizontal en puntos críticos.
>     
> 
> ✅ **Vector normal:**  
> $$\mathbf{n} = (f_x, f_y, -1)$$
> 
> ---
> 
> ### Sobre Aplicaciones
> 
> ✅ **Aproximación:** Estimar valores cercanos.  
> ✅ **Propagación de errores:** Calcular incertidumbres.  
> ✅ **Optimización:** Condición necesaria: $\nabla f = \mathbf{0}$.  
> ✅ **Machine Learning:** Base del gradiente descendente.
> 

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema es continuación de:**
> 
> - [[08 - Derivadas Parciales]]
>     
> - [[07 - Límites y Continuidad]]
>     
> 
> **Este tema es prerequisito para:**
> 
> - [[11 - Gradiente y Derivadas Direccionales]]
>     
> - [[12 - Regla de la Cadena Multivariable]]
>     
> - [[13 - Plano Tangente y Aproximación]]
>     
> - [[14 - Extremos y Optimización]]
>     
> - [[15 - Multiplicadores de Lagrange]]
>     
> 
> **Conceptos relacionados:**
> 
> - **Diferencial total**: Aproximación lineal infinitesimal.
>     
> - **Gradiente**: Vector de derivadas parciales.
>     
> - **Matriz Jacobiana**: Funciones vectoriales.
>     
> - **Matriz Hessiana**: Derivadas de segundo orden, útil en optimización.
>     
> 
> **Siguiente tema recomendado:** [[11 - Gradiente y Derivadas Direccionales]]
> 

---

## 📊 Comparación: Una vs Varias Variables

> [!note]- 📈 Tabla Comparativa

|Concepto|Una Variable ($f: \mathbb{R} \to \mathbb{R}$)|Dos Variables ($f: \mathbb{R}^2 \to \mathbb{R}$)|
|---|---|---|
|**Derivada**|$f'(x)$|$f_x(x,y)$ y $f_y(x,y)$|
|**Aproximación**|Recta tangente|Plano tangente|
|**Ecuación**|$y = f(a) + f'(a)(x-a)$|$z = f(x_0,y_0) + f_x(x-x_0) + f_y(y-y_0)$|
|**Diferencial**|$df = f'(x)dx$|$df = f_x dx + f_y dy$|
|**Condición suficiente**|$f'$ existe|$f_x, f_y$ continuas|
|**Geométrico**|Pendiente de la recta|Vector normal $(f_x, f_y, -1)$|
|**Punto crítico**|$f'(x) = 0$|$f_x = 0$ y $f_y = 0$|
|**Continuidad**|Diferenciable ⟹ Continua|Diferenciable ⟹ Continua|
|**Recíproco**|Continua ⟹ Diferenciable (FALSO)|Derivadas existen ⟹ Diferenciable (FALSO)|

---

## 💭 Intuición Geométrica Profunda

> [!note]- 🎨 Visualización Conceptual
> 
> ### Analogía: Superficie como "Colina"
> 
> **Derivadas parciales:**
> 
> - $f_x$ = pendiente si caminas hacia el Este.
>     
> - $f_y$ = pendiente si caminas hacia el Norte.
>     
> 
> **Plano tangente:**
> 
> - Representa el “suelo local” en tu posición.
>     
> 
> **Diferenciabilidad:**
> 
> - La colina es “suave” (sin picos ni esquinas).
>     
> - Localmente se comporta como un plano inclinado.
>     
> 
> ### ¿Por qué derivadas parciales no bastan?
> 
> Superficie con cresta afilada:
> 
> ```
>         z
>         |
>         |      /\
>         |     /  \
>         |    /    \
>         |   /      \
>         |  /        \
>         | /          \
>         +-------------- y
>        /
>       x
> ```
> 
> - Derivadas parciales pueden existir en $x$ e $y$.
>     
> - Pero en diagonal no hay pendiente definida → No diferenciable.
>     
> 
> ### El plano tangente como "mejor ajuste"
> 
> El plano tangente es el único plano que:
> 
> 1. Pasa por $(x_0, y_0, f(x_0,y_0))$.
>     
> 2. Tiene pendiente $f_x$ en dirección $x$.
>     
> 3. Tiene pendiente $f_y$ en dirección $y$.
>     
> 4. Minimiza el error cerca del punto.
>     
> 

---

## 🧮 Técnicas Avanzadas

### 🔬 Método de Taylor (Adelanto)

> [!note]- 📐 Aproximación de Orden Superior
> 
> - Aproximación lineal = **Taylor de orden 1**.
>     
> 
> **Taylor de orden 2:**  
> $$f(x,y) \approx f(x_0,y_0) + f_x \Delta x + f_y \Delta y + \frac{1}{2}[f_{xx}(\Delta x)^2 + 2 f_{xy} \Delta x \Delta y + f_{yy}(\Delta y)^2]$$
> 
> **Ejemplo:** $f(x,y) = e^{xy}$ cerca de $(0,0)$
> 
> - Orden 1: $f \approx 1$
>     
> - Orden 2: $f \approx 1 + xy$
>     
> 

### 🎯 Criterio Práctico de Diferenciabilidad

> [!tip]- ✅ Algoritmo Rápido
> 
> 1. **Verificar $C^1$**: ¿$f_x$, $f_y$ continuas? → Sí → Diferenciable.
>     
> 2. **Verificar existencia de derivadas parciales**: No → No diferenciable.
>     
> 3. **Verificar límite del error:**  
>     $$\lim_{(x,y) \to (x_0,y_0)} \frac{f(x,y) - L(x,y)}{\sqrt{(x-x_0)^2 + (y-y_0)^2}} = 0$$
>     
> 
> - =0 → Diferenciable, ≠0 → No diferenciable.
>     
> 
> **Nota:** En la práctica, Paso 1 suele ser suficiente.
> 

---

## 🎪 Casos Especiales Importantes

### 🌀 Funciones Homogéneas

> [!note]- 🔢 Teorema de Euler
> 
> - Homogénea de grado $k$ si $f(tx,ty) = t^k f(x,y)$.
>     
> - Teorema de Euler: $xf_x + yf_y = k f$.
>     
> 
> **Ejemplo:** $f(x,y) = x^2 + xy + y^2$ → grado 2  
> $$xf_x + yf_y = 2f$$ 
> 

### 🌊 Funciones Armónicas

> [!note]- 🎵 Laplaciano Cero
> 
> - $f$ armónica si $\nabla^2 f = f_{xx} + f_{yy} = 0$.
>     
> - Representan estados estacionarios (temperatura, potencial).
>     
> - Valor en un punto = promedio de los alrededores.
>     
> 
> **Ejemplo:** $f(x,y) = e^x\cos y$  
> $$f_{xx} + f_{yy} = 0 \implies f \text{ armónica}$$ 
> 

---

## 📚 Resumen Final

> [!note]- 🎯 Lo Más Importante
> 
> 1. **Diferenciabilidad:**
>     
>     - Aproximable por línea, más fuerte que derivadas parciales, garantiza continuidad.
>         
> 2. **Plano Tangente:**
>     
>     - Mejor aproximación lineal, ecuación $z = f(x_0,y_0) + f_x(x-x_0) + f_y(y-y_0)$
>         
>     - Horizontal en puntos críticos
>         
> 3. **Diferencial Total:**
>     
>     - $df = f_x dx + f_y dy$, útil para aproximación y regla de la cadena
>         
> 
> **Jerarquía de conceptos:**
> 
> ```
> C¹ (derivadas continuas)
>         ↓
>   Diferenciable
>    ↙         ↘
>  Continua  Derivadas parciales
> ```
> 
> **Práctica:**
> 
> - La mayoría de funciones son $C^1$ → diferenciables.
>     
> - Para plano tangente: calcular $f$, $f_x$, $f_y$ en el punto.
>     
> - Aproximación: $\Delta f \approx f_x \Delta x + f_y \Delta y$.
>     
> - Errores: $|df| \le |f_x||dx| + |f_y||dy|$.
>     
> 

---

## 🎓 Reflexiones Finales

> [!note]- 💭 Filosofía del Cálculo Multivariable
> 
> - **Linealización:** “Localmente, todo lo suave es lineal”.
>     
> - Funciones complicadas → aproximación lineal, superficies curvas → planos, sistemas no lineales → linearización.
>     
> 
> **Importancia de diferenciabilidad:**
> 
> 1. Matemática: continuidad, aproximación.
>     
> 2. Geometría: superficie suave.
>     
> 3. Computación: métodos numéricos.
>     
> 4. Aplicaciones: optimización, ML, física.
>     
> 
> **Plano tangente = “lente local”**
> 
> - Transforma lo curvo en plano, lo no lineal en lineal, lo complicado en simple.
>     

---
**Tags:** #calculo-multivariable #diferenciabilidad #plano-tangente #aproximacion-lineal #diferencial-total #gradiente #continuidad #optimizacion #machine-learning #propagacion-errores



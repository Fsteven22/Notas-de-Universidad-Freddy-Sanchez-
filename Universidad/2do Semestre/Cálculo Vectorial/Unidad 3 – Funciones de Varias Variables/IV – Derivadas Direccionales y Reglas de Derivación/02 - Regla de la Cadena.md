# 📘 Regla de la Cadena

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante la Regla de la Cadena?
> 
> La regla de la cadena es una de las herramientas más poderosas del cálculo multivariable, extendiendo el concepto de derivación de funciones compuestas a dimensiones superiores.
> 
> **Motivación:**
> 
> - En una variable: $(f \circ g)' = f'(g(x)) \cdot g'(x)$
> - En varias variables: ¿Cómo derivar composiciones más complejas?
> - Solución: **Regla de la cadena multivariable** usando matrices jacobianas
> 
> **Pregunta fundamental:**
> 
> Si $z = f(x,y)$ y ambas $x$ e $y$ dependen de otras variables $s$ y $t$, ¿cómo calculamos $\frac{\partial z}{\partial s}$ y $\frac{\partial z}{\partial t}$?
> 
> **Aplicaciones prácticas:**
> 
> - **Física:** Cambios de coordenadas (polares, cilíndricas, esféricas)
> - **Termodinámica:** Derivadas de variables de estado
> - **Machine Learning:** Backpropagation en redes neuronales
> - **Optimización:** Gradientes en coordenadas transformadas
> - **Geometría:** Parametrizaciones de curvas y superficies
> - **Ecuaciones diferenciales:** Cambio de variables para simplificar

---

## 🔗 Regla de la Cadena - Caso General

### 📋 Definición Formal

> [!example]- 🟢 Teorema: Regla de la Cadena Multivariable
> 
> **Teorema:** Sean $\vec{g}: \mathbb{R}^m \to \mathbb{R}^n$ y $f: \mathbb{R}^n \to \mathbb{R}^p$ funciones diferenciables. Entonces la composición $h = f \circ \vec{g}$ es diferenciable y:
> 
> $$J_h(\vec{x}) = J_f(\vec{g}(\vec{x})) \cdot J_{\vec{g}}(\vec{x})$$
> 
> donde $J$ denota la matriz jacobiana.
> 
> ---
> 
> **En componentes:**
> 
> Si $\vec{g}(\vec{x}) = (g_1(\vec{x}), \ldots, g_n(\vec{x}))$ y $f(\vec{y}) = (f_1(\vec{y}), \ldots, f_p(\vec{y}))$, entonces:
> 
> $$\frac{\partial h_i}{\partial x_j} = \sum_{k=1}^{n} \frac{\partial f_i}{\partial y_k} \cdot \frac{\partial g_k}{\partial x_j}$$
> 
> ---
> 
> **Notación matricial:**
> 
> $$\begin{pmatrix} \frac{\partial h_1}{\partial x_1} & \cdots & \frac{\partial h_1}{\partial x_m} \ \vdots & \ddots & \vdots \ \frac{\partial h_p}{\partial x_1} & \cdots & \frac{\partial h_p}{\partial x_m} \end{pmatrix} = \begin{pmatrix} \frac{\partial f_1}{\partial y_1} & \cdots & \frac{\partial f_1}{\partial y_n} \ \vdots & \ddots & \vdots \ \frac{\partial f_p}{\partial y_1} & \cdots & \frac{\partial f_p}{\partial y_n} \end{pmatrix} \cdot \begin{pmatrix} \frac{\partial g_1}{\partial x_1} & \cdots & \frac{\partial g_1}{\partial x_m} \ \vdots & \ddots & \vdots \ \frac{\partial g_n}{\partial x_1} & \cdots & \frac{\partial g_n}{\partial x_m} \end{pmatrix}$$
> 
> ---
> 
> **Dimensiones:**
> 
> - $J_f$: matriz $p \times n$
> - $J_{\vec{g}}$: matriz $n \times m$
> - $J_h = J_f \cdot J_{\vec{g}}$: matriz $p \times m$
> 
> ---
> 
> **Interpretación:**
> 
> La derivada de una composición es el **producto** de las derivadas, donde las "derivadas" son ahora matrices jacobianas.

### 🎨 Visualización Geométrica

> [!note]- 🖼️ Interpretación Gráfica
> 
> ### Diagrama de Composición
> 
> ```
> ℝᵐ ──g→ ℝⁿ ──f→ ℝᵖ
>  x⃗       y⃗       z⃗
> 
> Composición: h = f ∘ g
> 
> ℝᵐ ──────h─────→ ℝᵖ
>  x⃗               z⃗
> ```
> 
> ---
> 
> ### Aproximación Lineal
> 
> La regla de la cadena dice que la aproximación lineal de $h$ es:
> 
> ```
> Δz⃗ ≈ Jf(g(x⃗)) · Jg(x⃗) · Δx⃗
> 
>       ↑           ↑       ↑
>    cambio     transf.  cambio
>    de z       interm.   de x
> ```
> 
> ---
> 
> ### Intuición
> 
> 1. Un cambio pequeño $\Delta\vec{x}$ en la entrada
> 2. Causa un cambio $\Delta\vec{y} \approx J_{\vec{g}} \Delta\vec{x}$ en las variables intermedias
> 3. Que causa un cambio $\Delta\vec{z} \approx J_f \Delta\vec{y}$ en la salida
> 4. Combinando: $\Delta\vec{z} \approx J_f \cdot J_{\vec{g}} \Delta\vec{x}$

---

## 📊 Casos Especiales Importantes

### 🌟 Caso 1: Función Real de Variables Intermedias

> [!example]- 🔵 Caso: $z = f(x, y)$ con $x = x(t)$, $y = y(t)$
> 
> **Situación:** Función $z = f(x,y)$ donde $x$ e $y$ dependen de una variable $t$.
> 
> $$z = f(x(t), y(t))$$
> 
> ---
> 
> **Regla de la cadena:**
> 
> $$\frac{dz}{dt} = \frac{\partial f}{\partial x} \cdot \frac{dx}{dt} + \frac{\partial f}{\partial y} \cdot \frac{dy}{dt}$$
> 
> ---
> 
> **En notación vectorial:**
> 
> $$\frac{dz}{dt} = \nabla f \cdot \frac{d\vec{r}}{dt}$$
> 
> donde $\vec{r}(t) = (x(t), y(t))$.
> 
> ---
> 
> **Ejemplo:**
> 
> $z = x^2 + y^2$ con $x = \cos t$, $y = \sin t$
> 
> **Método 1: Regla de la cadena**
> 
> $$\frac{dz}{dt} = 2x \cdot (-\sin t) + 2y \cdot \cos t$$ $$= 2\cos t \cdot (-\sin t) + 2\sin t \cdot \cos t$$ $$= -2\cos t \sin t + 2\sin t \cos t = 0$$
> 
> **Método 2: Sustitución directa**
> 
> $$z = \cos^2 t + \sin^2 t = 1$$ $$\frac{dz}{dt} = 0$$ ✓
> 
> ---
> 
> **Interpretación:**
> 
> Movemos un punto sobre el círculo unitario ($x^2 + y^2 = 1$), por lo que $z$ permanece constante.

### 🌟 Caso 2: Función de Dos Variables Independientes

> [!example]- 🔵 Caso: $z = f(x, y)$ con $x = x(s,t)$, $y = y(s,t)$
> 
> **Situación:** $z$ depende de $x$ e $y$, que a su vez dependen de $s$ y $t$.
> 
> $$z = f(x(s,t), y(s,t))$$
> 
> ---
> 
> **Regla de la cadena:**
> 
> $$\frac{\partial z}{\partial s} = \frac{\partial f}{\partial x} \cdot \frac{\partial x}{\partial s} + \frac{\partial f}{\partial y} \cdot \frac{\partial y}{\partial s}$$
> 
> $$\frac{\partial z}{\partial t} = \frac{\partial f}{\partial x} \cdot \frac{\partial x}{\partial t} + \frac{\partial f}{\partial y} \cdot \frac{\partial y}{\partial t}$$
> 
> ---
> 
> **Matriz jacobiana:**
> 
> $$J_h = \begin{pmatrix} \frac{\partial z}{\partial s} & \frac{\partial z}{\partial t} \end{pmatrix} = \begin{pmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} \end{pmatrix} \cdot \begin{pmatrix} \frac{\partial x}{\partial s} & \frac{\partial x}{\partial t} \ \frac{\partial y}{\partial s} & \frac{\partial y}{\partial t} \end{pmatrix}$$
> 
> ---
> 
> **Ejemplo:**
> 
> $z = x^2 - y^2$ con $x = s + t$, $y = s - t$
> 
> **Derivadas parciales de $f$:** $$f_x = 2x, \quad f_y = -2y$$
> 
> **Derivadas de las variables intermedias:** $$\frac{\partial x}{\partial s} = 1, \quad \frac{\partial x}{\partial t} = 1$$ $$\frac{\partial y}{\partial s} = 1, \quad \frac{\partial y}{\partial t} = -1$$
> 
> **Aplicando la regla:** $$\frac{\partial z}{\partial s} = 2x \cdot 1 + (-2y) \cdot 1 = 2x - 2y$$ $$= 2(s+t) - 2(s-t) = 4t$$
> 
> $$\frac{\partial z}{\partial t} = 2x \cdot 1 + (-2y) \cdot (-1) = 2x + 2y$$ $$= 2(s+t) + 2(s-t) = 4s$$
> 
> **Verificación por sustitución:** $$z = (s+t)^2 - (s-t)^2 = 4st$$ $$\frac{\partial z}{\partial s} = 4t$$ ✓ $$\frac{\partial z}{\partial t} = 4s$$ ✓

### 🌟 Caso 3: Cambio de Coordenadas Polares

> [!example]- 🔵 Caso: Coordenadas Polares
> 
> **Transformación:** $$x = r\cos\theta, \quad y = r\sin\theta$$
> 
> **Pregunta:** Si $z = f(x,y)$, ¿cómo son $\frac{\partial z}{\partial r}$ y $\frac{\partial z}{\partial \theta}$?
> 
> ---
> 
> **Solución usando regla de la cadena:**
> 
> $$\frac{\partial z}{\partial r} = \frac{\partial f}{\partial x} \cdot \frac{\partial x}{\partial r} + \frac{\partial f}{\partial y} \cdot \frac{\partial y}{\partial r}$$
> 
> $$= f_x \cdot \cos\theta + f_y \cdot \sin\theta$$
> 
> $$\boxed{\frac{\partial z}{\partial r} = \cos\theta , f_x + \sin\theta , f_y}$$
> 
> ---
> 
> $$\frac{\partial z}{\partial \theta} = \frac{\partial f}{\partial x} \cdot \frac{\partial x}{\partial \theta} + \frac{\partial f}{\partial y} \cdot \frac{\partial y}{\partial \theta}$$
> 
> $$= f_x \cdot (-r\sin\theta) + f_y \cdot (r\cos\theta)$$
> 
> $$\boxed{\frac{\partial z}{\partial \theta} = -r\sin\theta , f_x + r\cos\theta , f_y}$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - $\frac{\partial z}{\partial r}$: tasa de cambio en dirección radial
> - $\frac{\partial z}{\partial \theta}$: tasa de cambio en dirección angular (tangencial)
> 
> ---
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2$
> 
> $$f_x = 2x, \quad f_y = 2y$$
> 
> $$\frac{\partial z}{\partial r} = 2x \cos\theta + 2y \sin\theta$$ $$= 2r\cos^2\theta + 2r\sin^2\theta = 2r$$
> 
> $$\frac{\partial z}{\partial \theta} = -2xr\sin\theta + 2yr\cos\theta$$ $$= -2r^2\cos\theta\sin\theta + 2r^2\sin\theta\cos\theta = 0$$
> 
> **Verificación:** $z = r^2$ en coordenadas polares $$\frac{\partial z}{\partial r} = 2r$$ ✓ $$\frac{\partial z}{\partial \theta} = 0$$ ✓

### 🌟 Caso 4: Gradiente en Coordenadas Curvilíneas

> [!example]- 🔵 Caso: Gradiente en Diferentes Coordenadas
> 
> **Relación fundamental:**
> 
> $$\nabla f = \frac{\partial f}{\partial r}\hat{r} + \frac{1}{r}\frac{\partial f}{\partial \theta}\hat{\theta}$$
> 
> (en coordenadas polares)
> 
> ---
> 
> **Derivación:**
> 
> En cartesianas: $\nabla f = f_x \hat{x} + f_y \hat{y}$
> 
> Usando: $$\hat{r} = \cos\theta , \hat{x} + \sin\theta , \hat{y}$$ $$\hat{\theta} = -\sin\theta , \hat{x} + \cos\theta , \hat{y}$$
> 
> Y las fórmulas anteriores para $\frac{\partial z}{\partial r}$ y $\frac{\partial z}{\partial \theta}$.
> 
> ---
> 
> **Coordenadas cilíndricas:**
> 
> $$\nabla f = \frac{\partial f}{\partial r}\hat{r} + \frac{1}{r}\frac{\partial f}{\partial \theta}\hat{\theta} + \frac{\partial f}{\partial z}\hat{z}$$
> 
> ---
> 
> **Coordenadas esféricas:**
> 
> $$\nabla f = \frac{\partial f}{\partial \rho}\hat{\rho} + \frac{1}{\rho}\frac{\partial f}{\partial \phi}\hat{\phi} + \frac{1}{\rho\sin\phi}\frac{\partial f}{\partial \theta}\hat{\theta}$$

---

## 📝 Ejemplos Básicos

### Ejemplo 1: Composición Simple

> [!example]- 📝 Ejemplo 1: Cadena con Una Variable
> 
> **Función:** $z = e^{x^2 + y^2}$ con $x = t$, $y = 2t$
> 
> **Calcular:** $\frac{dz}{dt}$
> 
> ---
> 
> **Método 1: Regla de la cadena**
> 
> $$\frac{dz}{dt} = \frac{\partial z}{\partial x} \cdot \frac{dx}{dt} + \frac{\partial z}{\partial y} \cdot \frac{dy}{dt}$$
> 
> $$\frac{\partial z}{\partial x} = e^{x^2+y^2} \cdot 2x$$ $$\frac{\partial z}{\partial y} = e^{x^2+y^2} \cdot 2y$$
> 
> $$\frac{dx}{dt} = 1, \quad \frac{dy}{dt} = 2$$
> 
> $$\frac{dz}{dt} = 2xe^{x^2+y^2} \cdot 1 + 2ye^{x^2+y^2} \cdot 2$$ $$= 2e^{x^2+y^2}(x + 2y)$$
> 
> Sustituyendo $x = t$, $y = 2t$: $$= 2e^{t^2+4t^2}(t + 4t) = 10te^{5t^2}$$
> 
> $$\boxed{\frac{dz}{dt} = 10te^{5t^2}}$$
> 
> ---
> 
> **Método 2: Sustitución primero**
> 
> $$z = e^{t^2 + (2t)^2} = e^{5t^2}$$ $$\frac{dz}{dt} = e^{5t^2} \cdot 10t = 10te^{5t^2}$$ ✓

### Ejemplo 2: Dos Variables Independientes

> [!example]- 📝 Ejemplo 2: Derivadas Parciales
> 
> **Función:** $w = xy + yz + zx$ con $x = s + t$, $y = st$, $z = s - t$
> 
> **Calcular:** $\frac{\partial w}{\partial s}$ y $\frac{\partial w}{\partial t}$
> 
> ---
> 
> **Derivadas parciales de $w$:**
> 
> $$\frac{\partial w}{\partial x} = y + z$$ $$\frac{\partial w}{\partial y} = x + z$$ $$\frac{\partial w}{\partial z} = y + x$$
> 
> ---
> 
> **Derivadas de variables intermedias:**
> 
> $$\frac{\partial x}{\partial s} = 1, \quad \frac{\partial y}{\partial s} = t, \quad \frac{\partial z}{\partial s} = 1$$ $$\frac{\partial x}{\partial t} = 1, \quad \frac{\partial y}{\partial t} = s, \quad \frac{\partial z}{\partial t} = -1$$
> 
> ---
> 
> **Aplicando regla de la cadena:**
> 
> $$\frac{\partial w}{\partial s} = (y+z) \cdot 1 + (x+z) \cdot t + (y+x) \cdot 1$$ $$= y + z + tx + tz + y + x$$ $$= x + 2y + z + t(x + z)$$
> 
> Sustituyendo: $$= (s+t) + 2st + (s-t) + t(s+t + s-t)$$ $$= 2s + 2st + 2st = 2s + 4st$$
> 
> $$\boxed{\frac{\partial w}{\partial s} = 2s + 4st}$$
> 
> ---
> 
> $$\frac{\partial w}{\partial t} = (y+z) \cdot 1 + (x+z) \cdot s + (y+x) \cdot (-1)$$ $$= y + z + sx + sz - y - x$$ $$= z - x + s(x + z)$$
> 
> Sustituyendo: $$= (s-t) - (s+t) + s(s+t + s-t)$$ $$= -2t + 2s^2$$
> 
> $$\boxed{\frac{\partial w}{\partial t} = 2s^2 - 2t}$$

### Ejemplo 3: Verificación con Laplaciano

> [!example]- 📝 Ejemplo 3: Laplaciano en Polares
> 
> **Objetivo:** Expresar $\nabla^2 f = f_{xx} + f_{yy}$ en coordenadas polares.
> 
> ---
> 
> **Paso 1: Primera derivada**
> 
> Ya sabemos: $$\frac{\partial f}{\partial r} = \cos\theta , f_x + \sin\theta , f_y$$
> 
> ---
> 
> **Paso 2: Segunda derivada respecto a $r$**
> 
> $$\frac{\partial^2 f}{\partial r^2} = \frac{\partial}{\partial r}\left(\cos\theta , f_x + \sin\theta , f_y\right)$$
> 
> Aplicando regla de la cadena nuevamente: $$= \cos\theta \frac{\partial f_x}{\partial r} + \sin\theta \frac{\partial f_y}{\partial r}$$
> 
> $$= \cos\theta(\cos\theta , f_{xx} + \sin\theta , f_{xy}) + \sin\theta(\cos\theta , f_{yx} + \sin\theta , f_{yy})$$
> 
> $$= \cos^2\theta , f_{xx} + 2\cos\theta\sin\theta , f_{xy} + \sin^2\theta , f_{yy}$$
> 
> ---
> 
> **Paso 3: Derivada respecto a $\theta$**
> 
> Similarmente (proceso más largo): $$\frac{\partial^2 f}{\partial \theta^2} = r^2\sin^2\theta , f_{xx} - 2r^2\cos\theta\sin\theta , f_{xy} + r^2\cos^2\theta , f_{yy} - r\cos\theta , f_x - r\sin\theta , f_y$$
> 
> ---
> 
> **Resultado final:**
> 
> $$\boxed{\nabla^2 f = \frac{\partial^2 f}{\partial r^2} + \frac{1}{r}\frac{\partial f}{\partial r} + \frac{1}{r^2}\frac{\partial^2 f}{\partial \theta^2}}$$
> 
> Esta es la fórmula del laplaciano en coordenadas polares.

---

## 🔬 Ejemplos Avanzados

### Ejemplo 4: Termodinámica

> [!example]- 🔥 Ejemplo 4: Relaciones Termodinámicas
> 
> **Contexto:** En termodinámica, las variables de estado están relacionadas. Para un gas ideal:
> 
> $$PV = nRT$$
> 
> Donde $P$ (presión), $V$ (volumen), $T$ (temperatura) están relacionadas.
> 
> ---
> 
> **Pregunta:** Si consideramos $T = T(P, V)$, ¿cómo se relacionan las derivadas parciales?
> 
> ---
> 
> **Solución:**
> 
> De la ecuación del gas ideal: $$T = \frac{PV}{nR}$$
> 
> Derivadas parciales directas: $$\frac{\partial T}{\partial P}\Bigg|_V = \frac{V}{nR}$$ $$\frac{\partial T}{\partial V}\Bigg|_P = \frac{P}{nR}$$
> 
> ---
> 
> **Relación de reciprocidad:**
> 
> Si $F(P, V, T) = PV - nRT = 0$, entonces:
> 
> $$\frac{\partial P}{\partial V}\Bigg|_T \cdot \frac{\partial V}{\partial T}\Bigg|_P \cdot \frac{\partial T}{\partial P}\Bigg|_V = -1$$
> 
> Esta es una **relación termodinámica fundamental** que se deriva de la regla de la cadena para funciones implícitas.
> 
> ---
> 
> **Verificación:**
> 
> $$\frac{\partial P}{\partial V}\Bigg|_T = -\frac{P}{V}$$ $$\frac{\partial V}{\partial T}\Bigg|_P = \frac{V}{T}$$ $$\frac{\partial T}{\partial P}\Bigg|_V = \frac{T}{P}$$
> 
> Producto: $$-\frac{P}{V} \cdot \frac{V}{T} \cdot \frac{T}{P} = -1$$ ✓

### Ejemplo 5: Machine Learning - Backpropagation

> [!example]- 🤖 Ejemplo 5: Red Neuronal Simple
> 
> **Arquitectura:** Red con una capa oculta
> 
> ```
> Entrada: x
>    ↓
> z₁ = w₁x + b₁
>    ↓
> a₁ = σ(z₁)  [función de activación]
>    ↓
> z₂ = w₂a₁ + b₂
>    ↓
> ŷ = σ(z₂)
>    ↓
> L = (ŷ - y)²  [función de pérdida]
> ```
> 
> ---
> 
> **Objetivo:** Calcular $\frac{\partial L}{\partial w_1}$ (gradiente para actualizar peso)
> 
> ---
> 
> **Aplicando regla de la cadena:**
> 
> $$\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_2} \cdot \frac{\partial z_2}{\partial a_1} \cdot \frac{\partial a_1}{\partial z_1} \cdot \frac{\partial z_1}{\partial w_1}$$
> 
> ---
> 
> **Calculando cada término:**
> 
> 1. $\frac{\partial L}{\partial \hat{y}} = 2(\hat{y} - y)$
>     
> 2. $\frac{\partial \hat{y}}{\partial z_2} = \sigma'(z_2)$
>     
> 3. $\frac{\partial z_2}{\partial a_1} = w_2$
>     
> 4. $\frac{\partial a_1}{\partial z_1} = \sigma'(z_1)$
>     
> 5. $\frac{\partial z_1}{\partial w_1} = x$
>     
> 
> ---
> 
> **Resultado:**
> 
> $$\boxed{\frac{\partial L}{\partial w_1} = 2(\hat{y} - y) \cdot \sigma'(z_2) \cdot w_2 \cdot \sigma'(z_1) \cdot x}$$
> 
> Este es el **algoritmo de backpropagation**: aplicación sistemática de la regla de la cadena para calcular gradientes en redes neuronales.

### Ejemplo 6: Geometría - Curva Parametrizada

> [!example]- 📐 Ejemplo 6: Derivada Direccional a lo Largo de una Curva
> 
> **Función:** $f(x,y) = x^2 + xy + y^2$
> 
> **Curva:** $\vec{r}(t) = (\cos t, \sin t)$ (círculo unitario)
> 
> **Pregunta:** ¿Cómo cambia $f$ a lo largo de la curva?
> 
> ---
> 
> **Solución:**
> 
> $$\frac{df}{dt} = \nabla f \cdot \frac{d\vec{r}}{dt}$$
> 
> **Gradiente:** $$\nabla f = (2x + y, x + 2y)$$
> 
> En $(\cos t, \sin t)$: $$\nabla f = (2\cos t + \sin t, \cos t + 2\sin t)$$
> 
> **Velocidad:** $\frac{d\vec{r}}{dt} = (-\sin t, \cos t)$
> 
> **Producto punto:** $\frac{df}{dt} = (2\cos t + \sin t)(-\sin t) + (\cos t + 2\sin t)(\cos t)$ $= -2\cos t \sin t - \sin^2 t + \cos^2 t + 2\sin t \cos t$ $= \cos^2 t - \sin^2 t = \cos(2t)$
> 
> $\boxed{\frac{df}{dt} = \cos(2t)}$
> 
> ---
> 
> **Interpretación:**
> 
> - $f$ oscila a lo largo del círculo
> - Máximo cuando $t = 0, \pi$ (puntos $(\pm 1, 0)$)
> - Mínimo cuando $t = \pi/2, 3\pi/2$ (puntos $(0, \pm 1)$)

### Ejemplo 7: Física - Conservación de Energía

> [!example]- ⚡ Ejemplo 7: Energía en Sistema Mecánico
> 
> **Sistema:** Partícula en campo potencial $V(x, y)$ con trayectoria $\vec{r}(t) = (x(t), y(t))$
> 
> **Energía potencial:** $V(x, y) = \frac{1}{2}k(x^2 + y^2)$ (oscilador armónico 2D)
> 
> ---
> 
> **Pregunta:** ¿Cómo cambia $V$ con el tiempo?
> 
> ---
> 
> **Solución:**
> 
> $\frac{dV}{dt} = \frac{\partial V}{\partial x}\frac{dx}{dt} + \frac{\partial V}{\partial y}\frac{dy}{dt}$
> 
> $= kx \cdot v_x + ky \cdot v_y$
> 
> $= k\vec{r} \cdot \vec{v}$
> 
> ---
> 
> **Relación con la fuerza:**
> 
> La fuerza es $\vec{F} = -\nabla V = -k\vec{r}$
> 
> Por segunda ley de Newton: $m\vec{a} = \vec{F}$
> 
> $\frac{dV}{dt} = -\vec{F} \cdot \vec{v} = -m\vec{a} \cdot \vec{v}$
> 
> ---
> 
> **Energía total:**
> 
> $E = \frac{1}{2}m|\vec{v}|^2 + V$
> 
> $\frac{dE}{dt} = m\vec{v} \cdot \vec{a} + \frac{dV}{dt} = m\vec{v} \cdot \vec{a} - m\vec{a} \cdot \vec{v} = 0$
> 
> $\boxed{\frac{dE}{dt} = 0}$ (conservación de energía) ✓

### Ejemplo 8: Coordenadas Esféricas

> [!example]- 🌍 Ejemplo 8: Laplaciano en Coordenadas Esféricas
> 
> **Transformación:** $x = \rho\sin\phi\cos\theta$ $y = \rho\sin\phi\sin\theta$ $z = \rho\cos\phi$
> 
> ---
> 
> **Laplaciano en cartesianas:** $\nabla^2 f = f_{xx} + f_{yy} + f_{zz}$
> 
> ---
> 
> **Usando regla de la cadena (proceso extenso):**
> 
> Se puede demostrar que:
> 
> $\boxed{\nabla^2 f = \frac{1}{\rho^2}\frac{\partial}{\partial \rho}\left(\rho^2\frac{\partial f}{\partial \rho}\right) + \frac{1}{\rho^2\sin\phi}\frac{\partial}{\partial \phi}\left(\sin\phi\frac{\partial f}{\partial \phi}\right) + \frac{1}{\rho^2\sin^2\phi}\frac{\partial^2 f}{\partial \theta^2}}$
> 
> ---
> 
> **Ejemplo de aplicación:** $f = \frac{1}{\rho}$ (potencial de Coulomb)
> 
> En esféricas: $f$ solo depende de $\rho$
> 
> $\nabla^2 f = \frac{1}{\rho^2}\frac{d}{d\rho}\left(\rho^2 \cdot \frac{-1}{\rho^2}\right) = \frac{1}{\rho^2}\frac{d}{d\rho}(-1) = 0$
> 
> (para $\rho \neq 0$)
> 
> Esto verifica que $f = 1/\rho$ es armónica excepto en el origen.

---

## 🧮 Regla de la Cadena - Formas Alternativas

### 📊 Notación Diferencial

> [!note]- 📝 Notación de Leibniz Extendida
> 
> **Forma diferencial:**
> 
> Si $z = f(x, y)$ con $x = x(t)$, $y = y(t)$:
> 
> $dz = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$
> 
> Y como $dx = \frac{dx}{dt}dt$ y $dy = \frac{dy}{dt}dt$:
> 
> $dz = \left(\frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}\right)dt$
> 
> Por lo tanto:
> 
> $\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$
> 
> ---
> 
> **Ventajas:**
> 
> - Notación compacta y elegante
> - Facilita manipulaciones algebraicas
> - Natural para física e ingeniería
> 
> ---
> 
> **Precaución:**
> 
> Esta notación es intuitiva pero requiere cuidado:
> 
> - Los diferenciales no son "números" que se cancelan arbitrariamente
> - Debe respetarse qué variables son independientes

### 🔄 Diagramas de Árbol

> [!note]- 🌲 Método del Árbol de Dependencias
> 
> **Técnica:** Dibujar un árbol que muestre las dependencias.
> 
> ---
> 
> **Ejemplo:** $w = f(x, y, z)$ con $x = x(s, t)$, $y = y(s, t)$, $z = z(s, t)$
> 
> ```
>         w
>       / | \
>      x  y  z
>     /|  |\ /|\
>    s t  s t s t
> ```
> 
> **Regla:** Para calcular $\frac{\partial w}{\partial s}$, suma todos los caminos de $w$ a $s$:
> 
> $\frac{\partial w}{\partial s} = \frac{\partial w}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial w}{\partial y}\frac{\partial y}{\partial s} + \frac{\partial w}{\partial z}\frac{\partial z}{\partial s}$
> 
> ---
> 
> **Ejemplo más complejo:** $z = f(u, v)$ con $u = g(x, y)$, $v = h(x, y)$
> 
> ```
>         z
>        / \
>       u   v
>      /|   |\
>     x y   x y
> ```
> 
> $\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$
> 
> $\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial y}$

---

## 🎯 Aplicaciones Especiales

### 🔍 Aplicación 1: Cambios de Variables en EDPs

> [!example]- 🔬 Ejemplo 9: Ecuación del Calor
> 
> **Ecuación del calor:** $u_t = k u_{xx}$
> 
> **Transformación:** Variables de similitud $\xi = \frac{x}{\sqrt{t}}$
> 
> Buscamos $u(x, t) = U(\xi)$ (solución auto-similar)
> 
> ---
> 
> **Regla de la cadena:**
> 
> $\frac{\partial u}{\partial t} = \frac{dU}{d\xi} \cdot \frac{\partial \xi}{\partial t} = U'(\xi) \cdot \left(-\frac{x}{2t^{3/2}}\right) = -\frac{\xi}{2t}U'(\xi)$
> 
> $\frac{\partial u}{\partial x} = U'(\xi) \cdot \frac{\partial \xi}{\partial x} = \frac{U'(\xi)}{\sqrt{t}}$
> 
> $\frac{\partial^2 u}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{U'}{\sqrt{t}}\right) = \frac{U''(\xi)}{\sqrt{t}} \cdot \frac{1}{\sqrt{t}} = \frac{U''(\xi)}{t}$
> 
> ---
> 
> **Sustituyendo en la EDP:**
> 
> $-\frac{\xi}{2t}U' = k \cdot \frac{U''}{t}$
> 
> $\boxed{U'' + \frac{\xi}{2k}U' = 0}$
> 
> Una EDO ordinaria más simple.

### 🎲 Aplicación 2: Cambio de Variables en Probabilidad

> [!example]- 📊 Ejemplo 10: Transformación de Variables Aleatorias
> 
> **Problema:** Si $X$ e $Y$ son variables aleatorias con densidad conjunta $f_{XY}(x, y)$, y definimos:
> 
> $U = g(X, Y), \quad V = h(X, Y)$
> 
> ¿Cuál es la densidad de $(U, V)$?
> 
> ---
> 
> **Fórmula del cambio de variables:**
> 
> $f_{UV}(u, v) = f_{XY}(x(u,v), y(u,v)) \cdot |J|$
> 
> donde $J$ es el Jacobiano de la transformación inversa:
> 
> $J = \det\begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{pmatrix}$
> 
> ---
> 
> **Ejemplo concreto:** $X$, $Y$ independientes, normales estándar
> 
> Transformación a polares: $R = \sqrt{X^2 + Y^2}$, $\Theta = \arctan(Y/X)$
> 
> Inversa: $X = R\cos\Theta$, $Y = R\sin\Theta$
> 
> $J = \det\begin{pmatrix} \cos\theta & -r\sin\theta \ \sin\theta & r\cos\theta \end{pmatrix} = r$
> 
> $f_{R\Theta}(r, \theta) = \frac{1}{2\pi}e^{-r^2/2} \cdot r$
> 
> Esto muestra que $R$ y $\Theta$ son independientes (distribución de Rayleigh para $R$, uniforme para $\Theta$).

### 🌊 Aplicación 3: Mecánica de Fluidos

> [!example]- 💧 Ejemplo 11: Derivada Material
> 
> **Contexto:** En mecánica de fluidos, seguimos una partícula de fluido que se mueve.
> 
> **Derivada material (sustancial):**
> 
> $\frac{D\phi}{Dt} = \frac{\partial \phi}{\partial t} + \vec{v} \cdot \nabla\phi$
> 
> donde $\vec{v}$ es el campo de velocidad del fluido.
> 
> ---
> 
> **Interpretación:**
> 
> - $\frac{\partial \phi}{\partial t}$: cambio local en el tiempo (observador fijo)
> - $\vec{v} \cdot \nabla\phi$: cambio por el movimiento (convección)
> 
> ---
> 
> **Derivación usando regla de la cadena:**
> 
> Una partícula sigue la trayectoria $\vec{r}(t)$ con $\frac{d\vec{r}}{dt} = \vec{v}$
> 
> $\frac{D\phi}{Dt} = \frac{d}{dt}\phi(\vec{r}(t), t)$
> 
> Por regla de la cadena:
> 
> $= \frac{\partial \phi}{\partial t} + \frac{\partial \phi}{\partial x}\frac{dx}{dt} + \frac{\partial \phi}{\partial y}\frac{dy}{dt} + \frac{\partial \phi}{\partial z}\frac{dz}{dt}$
> 
> $= \frac{\partial \phi}{\partial t} + \nabla\phi \cdot \vec{v}$
> 
> ---
> 
> **Ejemplo:** Temperatura de una partícula de agua en el océano
> 
> Si $T = T(x, y, z, t)$ es el campo de temperatura:
> 
> $\frac{DT}{Dt} = \frac{\partial T}{\partial t} + u\frac{\partial T}{\partial x} + v\frac{\partial T}{\partial y} + w\frac{\partial T}{\partial z}$
> 
> donde $\vec{v} = (u, v, w)$ es la velocidad del agua.

---

## 🧩 Propiedades y Teoremas

### 📐 Propiedad 1: Composición de Funciones Lineales

> [!note]- 🔢 Caso Especial: Transformaciones Lineales
> 
> **Teorema:** Si $\vec{g}$ y $f$ son lineales, entonces:
> 
> $J_{f \circ \vec{g}} = J_f \cdot J_{\vec{g}}$
> 
> se reduce a multiplicación de matrices constantes.
> 
> ---
> 
> **Ejemplo:**
> 
> $\vec{g}(x, y) = \begin{pmatrix} 2x + y \ x - y \end{pmatrix}, \quad f(u, v) = 3u + 4v$
> 
> $J_{\vec{g}} = \begin{pmatrix} 2 & 1 \ 1 & -1 \end{pmatrix}, \quad J_f = \begin{pmatrix} 3 & 4 \end{pmatrix}$
> 
> $J_{f \circ \vec{g}} = \begin{pmatrix} 3 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \ 1 & -1 \end{pmatrix} = \begin{pmatrix} 10 & -1 \end{pmatrix}$
> 
> **Verificación directa:**
> 
> $h(x, y) = f(\vec{g}(x, y)) = 3(2x + y) + 4(x - y) = 10x - y$
> 
> $J_h = \begin{pmatrix} 10 & -1 \end{pmatrix}$ ✓

### 📐 Propiedad 2: Regla de la Cadena Iterada

> [!note]- 🔄 Composiciones Múltiples
> 
> **Teorema:** Para composiciones $h = f \circ g \circ k$:
> 
> $J_h = J_f \cdot J_g \cdot J_k$
> 
> evaluadas en los puntos apropiados.
> 
> ---
> 
> **Generalización:** Para $h = f_n \circ f_{n-1} \circ \cdots \circ f_1$:
> 
> $J_h = J_{f_n} \cdot J_{f_{n-1}} \cdots J_{f_1}$
> 
> ---
> 
> **Aplicación en Deep Learning:**
> 
> Red neuronal con $n$ capas:
> 
> $\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial z_n} \cdot \frac{\partial z_n}{\partial z_{n-1}} \cdots \frac{\partial z_2}{\partial z_1} \cdot \frac{\partial z_1}{\partial w_1}$
> 
> **Problema del gradiente que desaparece:** Si cada $|\frac{\partial z_i}{\partial z_{i-1}}| < 1$, el producto decae exponencialmente.

### 📐 Propiedad 3: Invariancia del Gradiente

> [!note]- 🌐 Gradiente es Independiente de Coordenadas
> 
> **Teorema:** El gradiente $\nabla f$ es un objeto geométrico invariante bajo cambios de coordenadas.
> 
> **Significado:** Aunque las componentes cambien, la dirección y magnitud del gradiente son las mismas.
> 
> ---
> 
> **Ejemplo:**
> 
> $f(x, y) = x^2 + y^2$ en cartesianas: $\nabla f = (2x, 2y)$
> 
> En polares: $f(r, \theta) = r^2$
> 
> $\nabla f = \frac{\partial f}{\partial r}\hat{r} = 2r\hat{r}$
> 
> En el punto $(x, y) = (1, 0) \leftrightarrow (r, \theta) = (1, 0)$:
> 
> - Cartesianas: $\nabla f = (2, 0)$ → apunta en dirección $\hat{x}$
> - Polares: $\nabla f = 2\hat{r}$ → apunta radialmente hacia afuera
> 
> Ambos representan el mismo vector geométrico. ✓

---

## 💡 Casos Especiales y Trampas

### ⚠️ Cuidado 1: Variables Mezcladas

> [!warning]- 🚨 Dependencia Parcial
> 
> **Situación problemática:**
> 
> $z = f(x, y)$ con $y = g(x)$ (solo $y$ depende de $x$)
> 
> ---
> 
> **Error común:**
> 
> $\frac{dz}{dx} \stackrel{?}{=} \frac{\partial z}{\partial x}$ ❌
> 
> ---
> 
> **Correcto:**
> 
> $\frac{dz}{dx} = \frac{\partial z}{\partial x} + \frac{\partial z}{\partial y}\frac{dy}{dx}$
> 
> Porque $x$ aparece tanto directamente como a través de $y$.
> 
> ---
> 
> **Ejemplo:**
> 
> $z = x^2 + xy$ con $y = 2x$
> 
> **Incorrecto:** $\frac{\partial z}{\partial x} = 2x + y$ ❌
> 
> **Correcto:** $\frac{dz}{dx} = (2x + y) + x \cdot 2 = 2x + y + 2x = 4x + y = 6x$
> 
> **Verificación:** $z = x^2 + x(2x) = 3x^2$, entonces $\frac{dz}{dx} = 6x$ ✓

### ⚠️ Cuidado 2: Notación Ambigua

> [!warning]- 📝 Claridad en las Derivadas Parciales
> 
> **Problema:** El símbolo $\frac{\partial z}{\partial x}$ puede ser ambiguo si no especificamos qué se mantiene constante.
> 
> ---
> 
> **Notación clara:**
> 
> $\frac{\partial z}{\partial x}\Bigg|_y \quad \text{vs} \quad \frac{\partial z}{\partial x}\Bigg|_w$
> 
> indican qué variable se mantiene constante.
> 
> ---
> 
> **Ejemplo termodinámico:**
> 
> Para $U = U(T, V)$ (energía interna):
> 
> $\frac{\partial U}{\partial T}\Bigg|_V \neq \frac{\partial U}{\partial T}\Bigg|_P$
> 
> - Primera: calor específico a volumen constante $C_V$
> - Segunda: relacionada con $C_P$ (calor específico a presión constante)
> 
> ---
> 
> **Regla práctica:**
> 
> En contextos complejos (termodinámica, química), siempre especificar qué se mantiene constante.

### ⚠️ Cuidado 3: Orden de Composición

> [!warning]- 🔄 Orden de las Matrices
> 
> **Error común:** Multiplicar jacobianas en orden incorrecto
> 
> $J_{f \circ g} = J_g \cdot J_f$ ❌
> 
> **Correcto:**
> 
> $J_{f \circ g} = J_f \cdot J_g$ ✓
> 
> (evaluadas en puntos apropiados)
> 
> ---
> 
> **Mnemotécnica:**
> 
> Si $h(x) = f(g(x))$, pensamos: "primero aplicamos $g$, luego $f$"
> 
> Pero en la multiplicación matricial: $J_f$ va primero (izquierda)
> 
> $\frac{\partial h}{\partial x} = \frac{\partial f}{\partial g} \cdot \frac{\partial g}{\partial x}$
> 
> Lee de derecha a izquierda: "cambio de $x$ a $g$, luego de $g$ a $f$"

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre la Regla de la Cadena
> 
> ✅ **Idea central:**
> 
> - La derivada de una composición es el producto de las derivadas
> - En múltiples variables: producto de matrices jacobianas
> 
> ✅ **Fórmula fundamental:** $J_{f \circ g} = J_f(g(\vec{x})) \cdot J_g(\vec{x})$
> 
> ✅ **Casos importantes:**
> 
> 1. Una variable independiente: $\frac{dz}{dt} = \nabla f \cdot \frac{d\vec{r}}{dt}$
> 2. Varias independientes: suma de productos parciales
> 3. Cambio de coordenadas: transforma derivadas entre sistemas
> 
> ✅ **Aplicaciones ubicuas:**
> 
> - Física: cambios de referencia, coordenadas curvilíneas
> - Machine Learning: backpropagation
> - Optimización: gradientes en espacios transformados
> - Ecuaciones diferenciales: simplificación por cambio de variables
> 
> ---
> 
> ### Estrategia para Aplicar
> 
> **Pasos sistemáticos:**
> 
> 1. ✅ **Identificar dependencias:** Dibujar diagrama de árbol
> 2. ✅ **Calcular derivadas parciales:** De cada función en la cadena
> 3. ✅ **Aplicar fórmula:** Sumar todos los caminos
> 4. ✅ **Simplificar:** Sustituir si es necesario
> 5. ✅ **Verificar:** Por sustitución directa cuando sea posible
> 
> ---
> 
> ### Errores Frecuentes
> 
> ❌ **Olvidar términos:** En derivadas parciales con múltiples caminos ❌ **Confundir notación:** $\frac{\partial}{\partial x}$ vs $\frac{d}{dx}$ ❌ **Orden incorrecto:** En productos de matrices ❌ **Evaluar mal:** Olvidar evaluar en el punto correcto
> 
> ---
> 
> ### Conexiones Importantes
> 
> La regla de la cadena conecta:
> 
> - Derivadas parciales con derivadas totales
> - Coordenadas diferentes del mismo espacio
> - Capas de una red neuronal
> - Variables termodinámicas
> - Parametrizaciones geométricas
> 
> Es el puente entre el cálculo local (derivadas) y estructuras globales (transformaciones).

---

## 📚 Tabla de Referencia Rápida

> [!note]- 📋 Fórmulas Clave
> 
> |Situación|Fórmula|
> |---|---|
> |**General**|$J_{f \circ g} = J_f \cdot J_g$|
> |**Una variable**|$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$|
> |**Dos variables**|$\frac{\partial z}{\partial s} = f_x \frac{\partial x}{\partial s} + f_y \frac{\partial y}{\partial s}$|
> |**Vectorial**|$\frac{dz}{dt} = \nabla f \cdot \vec{v}$|
> |**Polares**|$\frac{\partial f}{\partial r} = \cos\theta f_x + \sin\theta f_y$|
> ||$\frac{\partial f}{\partial \theta} = -r\sin\theta f_x + r\cos\theta f_y$|
> |**Tres variables**|$\frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} + \frac{\partial w}{\partial z}\frac{dz}{dt}$|
> 
> ### Notación
> 
> - $\frac{\partial}{\partial x}$: derivada parcial (otras variables constantes)
> - $\frac{d}{dt}$: derivada total (todas las dependencias)
> - $J_f$: matriz jacobiana de $f$
> - $\nabla f$: gradiente de $f$

---

## 🔗 Relaciones con Otros Temas

> [!quote]- 🌐 Conexiones Matemáticas
> 
> ### Prerequisitos:
> 
> - **Derivadas parciales** - Base fundamental
> - **Matriz Jacobiana** - Herramienta principal
> - **Gradiente** - Caso especial importante
> - **Diferenciabilidad** - Hipótesis necesaria
> - **Álgebra lineal: multiplicación de matrices**
> 
> ### Este tema es prerequisito para:
> 
> - **Derivadas implícitas** - Aplicación directa
> - **Multiplicadores de Lagrange** - Usa cadena implícita
> - **Cambio de variables en integrales** - Transformaciones
> - **Ecuaciones diferenciales** - Cambios de coordenadas
> - **Geometría diferencial** - Mapas entre variedades
> - **Optimización** - Gradientes en coordenadas transformadas
> 
> ### Temas relacionados:
> 
> - **Backpropagation** - Aplicación en ML
> - **Derivada material** - Mecánica de fluidos
> - **Coordenadas generalizadas** - Mecánica clásica
> - **Teoría de la información** - Divergencia KL
> 
> ### Siguiente tema:
> 
> **[[15 - Derivadas Implícitas]]** - Extensión natural usando la regla de la cadena

---

**Tags:** #calculo-multivariable #regla-cadena #jacobiana #composicion-funciones #backpropagation #cambio-coordenadas #derivada-direccional #gradiente #machine-learning #fisica #optimizacion
# 📘 Aplicaciones de la Diferencial y la Hessiana

## 🎯 Introducción

> [!info]- 💡 ¿Por qué estudiar la Diferencial y la Hessiana?
> 
> La **diferencial** y la **matriz Hessiana** son herramientas fundamentales que extienden conceptos del cálculo de una variable al mundo multivariable, permitiéndonos:
> 
> **Motivación:**
> 
> - En 1D: $f'(x)$ nos da la pendiente y $f''(x)$ nos dice si es cóncava o convexa
> - En múltiples variables: la **diferencial** generaliza $f'(x)$ y la **Hessiana** generaliza $f''(x)$
> - Estas herramientas son esenciales para **optimización** y **aproximación**
> 
> **¿Qué nos permiten hacer?**
> 
> - **Diferencial**: Aproximar funciones linealmente (mejor aproximación local)
> - **Hessiana**: Clasificar puntos críticos (máximos, mínimos, puntos silla)
> - Analizar la **curvatura** de superficies en múltiples direcciones
> - Resolver problemas de **optimización** sin restricciones
> 
> **Aplicaciones prácticas:**
> 
> - 📊 **Optimización**: Encontrar máximos y mínimos de funciones multivariables
> - 🎯 **Machine Learning**: Descenso de gradiente, entrenamiento de redes neuronales
> - 📈 **Economía**: Análisis de utilidad, maximización de beneficios
> - 🔬 **Física**: Energía potencial, estabilidad de sistemas
> - 🏗️ **Ingeniería**: Diseño óptimo, análisis de estructuras
> 
> **Conexión conceptual:**
> 
> - Diferencial → Aproximación de primer orden → Vector gradiente
> - Hessiana → Aproximación de segundo orden → Curvatura y clasificación

---

## 📐 La Diferencial

### 🔍 Definición y Concepto

> [!example]- 🟢 Definición: La Diferencial
> 
> **Definición:** Para una función diferenciable $f: \mathbb{R}^n \to \mathbb{R}$, la **diferencial** de $f$ en el punto $\mathbf{a}$ es la transformación lineal:
> 
> $$df_{\mathbf{a}}(\mathbf{h}) = \nabla f(\mathbf{a}) \cdot \mathbf{h}$$
> 
> donde $\mathbf{h} = (h_1, h_2, \ldots, h_n)$ es un vector de incrementos.
> 
> ---
> 
> **Para dos variables** $f(x,y)$: $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy = f_x,dx + f_y,dy$$
> 
> **Para tres variables** $f(x,y,z)$: $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz$$
> 
> ---
> 
> **Interpretación:**
> 
> - $dx, dy, dz$ representan **cambios infinitesimales** en las variables
> - $df$ representa el **cambio infinitesimal** resultante en $f$
> - La diferencial es la **mejor aproximación lineal** al cambio real en $f$
> 
> **Notación alternativa:**
> 
> - $df = \nabla f \cdot d\mathbf{r}$ donde $d\mathbf{r} = (dx, dy, dz)$
> - $df = \sum_{i=1}^n \frac{\partial f}{\partial x_i}dx_i$

> [!note]- 🎯 Interpretación Geométrica de la Diferencial
> 
> ### En dos variables
> 
> Para $z = f(x,y)$, la diferencial $df$ representa:
> 
> ```
>         z
>         │
>         │    Superficie z = f(x,y)
>         │      /│\
>         │     / │ \
>         │    /  │  \    ← Plano tangente
>         │   /   │   \     (aproximación lineal)
>         │  /    •────\── dz = df
>         │ /    (x₀,y₀)  
>         │/             
>         +───────────── y
>        /         
>       /
>      x
> ```
> 
> **El plano tangente en $(x_0, y_0)$:** $$z = f(x_0, y_0) + f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)$$
> 
> La diferencial $df$ es la parte lineal de esta ecuación.
> 
> ---
> 
> **Relación con la aproximación:** $$\Delta f = f(x_0+\Delta x, y_0+\Delta y) - f(x_0,y_0) \approx df = f_x\Delta x + f_y\Delta y$$
> 
> El símbolo $\approx$ significa "aproximadamente igual para $\Delta x, \Delta y$ pequeños"

### 📊 Propiedades de la Diferencial

> [!tip]- ✅ Propiedades Algebraicas
> 
> La diferencial es **lineal** y satisface:
> 
> ### 1. Linealidad
> 
> $$d(af + bg) = a,df + b,dg$$ donde $a, b$ son constantes.
> 
> ---
> 
> ### 2. Regla del Producto
> 
> $$d(fg) = f,dg + g,df$$
> 
> **Ejemplo:** Si $h(x,y) = x^2y$: $$dh = d(x^2 \cdot y) = x^2,dy + y,d(x^2) = x^2,dy + 2xy,dx$$
> 
> ---
> 
> ### 3. Regla del Cociente
> 
> $$d\left(\frac{f}{g}\right) = \frac{g,df - f,dg}{g^2}$$
> 
> ---
> 
> ### 4. Regla de la Cadena
> 
> Si $z = f(u,v)$ donde $u = u(x,y)$ y $v = v(x,y)$: $$dz = \frac{\partial f}{\partial u}du + \frac{\partial f}{\partial v}dv$$
> 
> ---
> 
> ### 5. Diferencial de Funciones Elementales
> 
> |Función|Diferencial|
> |---|---|
> |$f = x^n$|$df = nx^{n-1}dx$|
> |$f = e^x$|$df = e^x dx$|
> |$f = \ln x$|$df = \frac{dx}{x}$|
> |$f = \sin x$|$df = \cos x,dx$|
> |$f = \cos x$|$df = -\sin x,dx$|

---

## 📚 Ejemplos: Cálculo de Diferenciales

### Ejemplo 1: Diferencial de Polinomio

> [!example]- 📝 Ejemplo 1: Función Polinomial
> 
> **Función:** $$f(x,y) = x^3 + 2x^2y + 3y^2$$
> 
> ---
> 
> **Paso 1: Calcular derivadas parciales** $$\frac{\partial f}{\partial x} = 3x^2 + 4xy$$ $$\frac{\partial f}{\partial y} = 2x^2 + 6y$$
> 
> ---
> 
> **Paso 2: Escribir la diferencial** $$\boxed{df = (3x^2 + 4xy)dx + (2x^2 + 6y)dy}$$
> 
> ---
> 
> **Evaluada en $(1, 2)$:** $$df\big|_{(1,2)} = (3(1)^2 + 4(1)(2))dx + (2(1)^2 + 6(2))dy$$ $$= (3 + 8)dx + (2 + 12)dy$$ $$= 11dx + 14dy$$
> 
> **Interpretación:** Si desde el punto $(1,2)$ nos movemos una distancia pequeña $dx$ en dirección $x$ y $dy$ en dirección $y$, el cambio en $f$ es aproximadamente $11dx + 14dy$.

### Ejemplo 2: Función Exponencial

> [!example]- 📝 Ejemplo 2: Con Exponencial
> 
> **Función:** $$f(x,y) = e^{xy}$$
> 
> ---
> 
> **Derivadas parciales:** $$\frac{\partial f}{\partial x} = ye^{xy}$$ $$\frac{\partial f}{\partial y} = xe^{xy}$$
> 
> ---
> 
> **Diferencial:** $$\boxed{df = ye^{xy}dx + xe^{xy}dy = e^{xy}(y,dx + x,dy)}$$
> 
> ---
> 
> **En $(1, 0)$:** $$df\big|_{(1,0)} = e^{0}(0,dx + 1,dy) = dy$$
> 
> **Interpretación:** En el punto $(1,0)$, cambios en $x$ no afectan a $f$ en primer orden (porque $y=0$), solo cambios en $y$ importan.

### Ejemplo 3: Función con Logaritmo

> [!example]- 📝 Ejemplo 3: Función Logarítmica
> 
> **Función:** $$f(x,y) = \ln(x^2 + y^2)$$
> 
> ---
> 
> **Derivadas parciales:** $$\frac{\partial f}{\partial x} = \frac{2x}{x^2 + y^2}$$ $$\frac{\partial f}{\partial y} = \frac{2y}{x^2 + y^2}$$
> 
> ---
> 
> **Diferencial:** $$\boxed{df = \frac{2x,dx + 2y,dy}{x^2 + y^2} = \frac{2(x,dx + y,dy)}{x^2 + y^2}}$$
> 
> ---
> 
> **Forma vectorial:** $$df = \frac{2}{x^2 + y^2}(x, y) \cdot (dx, dy) = \frac{2\mathbf{r} \cdot d\mathbf{r}}{|\mathbf{r}|^2}$$
> 
> donde $\mathbf{r} = (x, y)$.

### Ejemplo 4: Tres Variables

> [!example]- 📝 Ejemplo 4: Función de Tres Variables
> 
> **Función:** $$f(x,y,z) = x^2yz + \sin(xyz)$$
> 
> ---
> 
> **Derivadas parciales:** $$\frac{\partial f}{\partial x} = 2xyz + yz\cos(xyz)$$ $$\frac{\partial f}{\partial y} = x^2z + xz\cos(xyz)$$ $$\frac{\partial f}{\partial z} = x^2y + xy\cos(xyz)$$
> 
> ---
> 
> **Diferencial:** $$df = [2xyz + yz\cos(xyz)]dx$$ $$\quad + [x^2z + xz\cos(xyz)]dy$$ $$\quad + [x^2y + xy\cos(xyz)]dz$$
> 
> ---
> 
> **En $(1, 1, 0)$:** $$f_x(1,1,0) = 0 + 0 \cdot 1 = 0$$ $$f_y(1,1,0) = 0 + 0 \cdot 1 = 0$$ $$f_z(1,1,0) = 1 + 1 \cdot 1 = 2$$
> 
> $$\boxed{df\big|_{(1,1,0)} = 2dz}$$

---

## 🔬 Aplicaciones de la Diferencial

### 🌡️ Aplicación 1: Propagación de Errores

> [!example]- 📊 Ejemplo: Error en Mediciones
> 
> **Situación:** Medimos el radio $r = 5$ cm (con error $\pm 0.1$ cm) y altura $h = 10$ cm (con error $\pm 0.2$ cm) de un cilindro.
> 
> El volumen es: $$V(r, h) = \pi r^2 h$$
> 
> **¿Cuál es el error aproximado en el volumen?**
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Calcular la diferencial $$dV = \frac{\partial V}{\partial r}dr + \frac{\partial V}{\partial h}dh$$ $$= 2\pi rh,dr + \pi r^2,dh$$
> 
> **Paso 2:** Evaluar en $(r, h) = (5, 10)$ $$dV = 2\pi(5)(10)dr + \pi(5)^2dh$$ $$= 100\pi,dr + 25\pi,dh$$
> 
> **Paso 3:** Usar $dr = \pm 0.1$ y $dh = \pm 0.2$
> 
> Error máximo (en el peor caso, ambos errores se suman): $$|dV| \leq 100\pi(0.1) + 25\pi(0.2) = 10\pi + 5\pi = 15\pi \approx 47.1 \text{ cm}^3$$
> 
> ---
> 
> **Volumen nominal:** $$V(5, 10) = \pi(5)^2(10) = 250\pi \approx 785.4 \text{ cm}^3$$
> 
> **Error relativo:** $$\frac{|dV|}{V} \approx \frac{47.1}{785.4} \approx 0.06 = 6%$$
> 
> **Conclusión:** El error en el volumen es aproximadamente $\pm 47$ cm³ o $\pm 6%$.
> $$

### 💰 Aplicación 2: Economía - Productividad Marginal

> [!example]- 📈 Ejemplo: Función de Producción
> 
> **Situación:** Una empresa tiene función de producción Cobb-Douglas: $$P(K, L) = 10K^{0.4}L^{0.6}$$
> 
> donde $K$ es capital y $L$ es trabajo. Actualmente $K = 100$ y $L = 200$.
> 
> **¿Cómo cambia la producción si se aumenta el capital en 5 unidades y el trabajo en 10?**
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Productividades marginales $$\frac{\partial P}{\partial K} = 4K^{-0.6}L^{0.6}$$ $$\frac{\partial P}{\partial L} = 6K^{0.4}L^{-0.4}$$
> 
> **Paso 2:** Evaluar en $(100, 200)$ $$P_K(100, 200) = 4(100)^{-0.6}(200)^{0.6} \approx 4 \cdot 0.251 \cdot 28.84 \approx 29.0$$ $$P_L(100, 200) = 6(100)^{0.4}(200)^{-0.4} \approx 6 \cdot 6.31 \cdot 0.205 \approx 7.75$$
> 
> **Paso 3:** Calcular cambio aproximado $$dP = P_K,dK + P_L,dL = 29.0(5) + 7.75(10)$$ $$= 145 + 77.5 = 222.5$$
> 
> **Interpretación:** La producción aumentará aproximadamente 222.5 unidades.
> 
> **Verificación:** $$P(105, 210) - P(100, 200) \approx 224.3$$
> 
> ¡La aproximación es muy buena!

### 🌍 Aplicación 3: Física - Energía

> [!example]- ⚡ Ejemplo: Energía Cinética Relativista
> 
> **Situación:** La energía cinética relativista es: $$E(m, v) = \frac{mc^2}{\sqrt{1 - v^2/c^2}} - mc^2$$
> 
> donde $c$ es la velocidad de la luz.
> 
> Para $v \ll c$, aproximar el cambio en energía cuando cambian $m$ y $v$.
> 
> ---
> 
> **Solución simplificada:**
> 
> Para velocidades no relativistas, podemos aproximar: $$E \approx \frac{1}{2}mv^2$$
> 
> **Diferencial:** $$dE = \frac{\partial E}{\partial m}dm + \frac{\partial E}{\partial v}dv$$ $$= \frac{v^2}{2}dm + mv,dv$$
> 
> **Interpretación:**
> 
> - $\frac{v^2}{2}$ es la energía cinética por unidad de masa
> - $mv$ es el momento lineal
> 
> **Ejemplo numérico:** $m = 2$ kg, $v = 10$ m/s
> 
> Si $dm = 0.1$ kg y $dv = 1$ m/s: $$dE = \frac{(10)^2}{2}(0.1) + 2(10)(1) = 5 + 20 = 25 \text{ J}$$

---

## 🔲 La Matriz Hessiana

### 🔍 Definición

> [!example]- 🟡 Definición: Matriz Hessiana
> 
> **Definición:** Para una función $f: \mathbb{R}^n \to \mathbb{R}$ de clase $C^2$, la **matriz Hessiana** en el punto $\mathbf{a}$ es:
> 
> $$H_f(\mathbf{a}) = \begin{bmatrix} \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \ \frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \ \vdots & \vdots & \ddots & \vdots \ \frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2} \end{bmatrix}_{\mathbf{a}}$$
> 
> ---
> 
> **Para dos variables** $f(x,y)$: $$H_f = \begin{bmatrix} f_{xx} & f_{xy} \ f_{yx} & f_{yy} \end{bmatrix}$$
> 
> **Por el Teorema de Schwarz:** Si $f$ es $C^2$, entonces $f_{xy} = f_{yx}$, y la Hessiana es **simétrica**.
> 
> ---
> 
> **Para tres variables** $f(x,y,z)$: $$H_f = \begin{bmatrix} f_{xx} & f_{xy} & f_{xz} \ f_{yx} & f_{yy} & f_{yz} \ f_{zx} & f_{zy} & f_{zz} \end{bmatrix}$$
> 
> ---
> 
> **Interpretación:**
> 
> - La Hessiana captura toda la información sobre la **curvatura** de $f$
> - Generaliza la segunda derivada $f''(x)$ de una variable
> - Es fundamental para clasificar **puntos críticos**

> [!note]- 📊 Interpretación Geométrica
> 
> ### Analogía con una variable
> 
> **En 1D:**
> 
> - $f'(x_0) = 0$ → punto crítico
> - $f''(x_0) > 0$ → mínimo local
> - $f''(x_0) < 0$ → máximo local
> 
> **En múltiples variables:**
> 
> - $\nabla f(\mathbf{x}_0) = \mathbf{0}$ → punto crítico
> - $H_f(\mathbf{x}_0)$ **definida positiva** → mínimo local
> - $H_f(\mathbf{x}_0)$ **definida negativa** → máximo local
> - $H_f(\mathbf{x}_0)$ **indefinida** → punto silla
> 
> ---
> 
> ### Curvatura en diferentes direcciones
> 
> La Hessiana nos dice cómo "se curva" $f$ en cada dirección:
> 
> Para un vector unitario $\mathbf{v}$, la curvatura en esa dirección es: $$\mathbf{v}^T H_f \mathbf{v}$$
> 
> - Si esto es positivo para todo $\mathbf{v}$ → función cóncava hacia arriba
> - Si es negativo para todo $\mathbf{v}$ → función cóncava hacia abajo
> - Si cambia de signo → punto silla

---

## 📚 Ejemplos: Cálculo de Hessianas

### Ejemplo 5: Hessiana de Polinomio

> [!example]- 📝 Ejemplo 5: Función Cuadrática
> 
> **Función:** $$f(x,y) = x^2 + 2xy + 3y^2$$
> 
> ---
> 
> **Paso 1: Derivadas de primer orden** $$f_x = 2x + 2y$$ $$f_y = 2x + 6y$$
> 
> ---
> 
> **Paso 2: Derivadas de segundo orden** $$f_{xx} = 2$$ $$f_{xy} = 2 = f_{yx}$$ $$f_{yy} = 6$$
> 
> ---
> 
> **Paso 3: Matriz Hessiana** $$\boxed{H_f = \begin{bmatrix} 2 & 2 \ 2 & 6 \end{bmatrix}}$$
> 
> **Observación:** La Hessiana es **constante** para funciones cuadráticas.
> 
> ---
> 
> **Análisis:**
> 
> - Determinante: $\det(H) = 2(6) - 2(2) = 12 - 4 = 8 > 0$
> - $f_{xx} = 2 > 0$
> - **Conclusión:** $H$ es definida positiva → la función es convexa

### Ejemplo 6: Hessiana con Exponencial

> [!example]- 📝 Ejemplo 6: Función Exponencial
> 
> **Función:** $$f(x,y) = e^{x^2 + y^2}$$
> 
> ---
> 
> **Derivadas de primer orden:** $$f_x = 2xe^{x^2+y^2}$$ $$f_y = 2ye^{x^2+y^2}$$
> 
> ---
> 
> **Derivadas de segundo orden:**
> 
> $$f_{xx} = 2e^{x^2+y^2} + 2x \cdot 2xe^{x^2+y^2} = 2e^{x^2+y^2}(1 + 2x^2)$$
> 
> $$f_{yy} = 2e^{x^2+y^2} + 2y \cdot 2ye^{x^2+y^2} = 2e^{x^2+y^2}(1 + 2y^2)$$
> 
> $$f_{xy} = 2x \cdot 2ye^{x^2+y^2} = 4xye^{x^2+y^2}$$
> 
> ---
> 
> **Matriz Hessiana:** $$H_f = 2e^{x^2+y^2}\begin{bmatrix} 1 + 2x^2 & 2xy \ 2xy & 1 + 2y^2 \end{bmatrix}$$
> 
> ---
> 
> **En el origen** $(0,0)$: $$H_f(0,0) = 2e^0\begin{bmatrix} 1 & 0 \ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \ 0 & 2 \end{bmatrix} = 2I$$
> 
> **Interpretación:** En el origen, la función tiene curvatura uniforme en todas direcciones.

### Ejemplo 7: Hessiana de Función Trigonométrica

> [!example]- 📝 Ejemplo 7: Con Seno y Coseno
> 
> **Función:** $$f(x,y) = \sin(x)\cos(y)$$
> 
> ---
> 
> **Derivadas de primer orden:** $$f_x = \cos(x)\cos(y)$$ $$f_y = -\sin(x)\sin(y)$$
> 
> ---
> 
> **Derivadas de segundo orden:** $$f_{xx} = -\sin(x)\cos(y)$$ $$f_{yy} = -\sin(x)\cos(y)$$ $$f_{xy} = -\cos(x)\sin(y) = f_{yx}$$
> 
> ---
> 
> **Matriz Hessiana:** $$H_f = \begin{bmatrix} -\sin(x)\cos(y) & -\cos(x)\sin(y) \ -\cos(x)\sin(y) & -\sin(x)\cos(y) \end{bmatrix}$$
> 
> ---
> 
> **En** $(\pi/2, 0)$: $$H_f(\pi/2, 0) = \begin{bmatrix} -1 & 0 \ 0 & -1 \end{bmatrix} = -I$$
> 
> **Interpretación:** Definida negativa → máximo local en $(\pi/2, 0)$.

### Ejemplo 8: Tres Variables

> [!example]- 📝 Ejemplo 8: Función de Tres Variables
> 
> **Función:** $$f(x,y,z) = x^2 + y^2 + z^2 + 2xy - xz$$
> 
> ---
> 
> **Derivadas de primer orden:** $$f_x = 2x + 2y - z$$ $$f_y = 2y + 2x$$ $$f_z = 2z - x$$
> 
> ---
> 
> **Derivadas de segundo orden:** $$f_{xx} = 2, \quad f_{yy} = 2, \quad f_{zz} = 2$$ $$f_{xy} = 2, \quad f_{xz} = -1, \quad f_{yz} = 0$$
> 
> ---
> 
> **Matriz Hessiana:** $$\boxed{H_f = \begin{bmatrix} 2 & 2 & -1 \ 2 & 2 & 0 \ -1 & 0 & 2 \end{bmatrix}}$$
> 
> Esta matriz es constante en todo $\mathbb{R}^3$.

---

## 🎯 Clasificación de Puntos Críticos

### 📊 Criterio del Determinante (2 Variables)

> [!tip]- ✅ Criterio de la Segunda Derivada (Test de la Hessiana)
> 
> Sea $f(x,y)$ una función de clase $C^2$ y $(x_0, y_0)$ un **punto crítico** (es decir, $\nabla f(x_0, y_0) = \mathbf{0}$).
> 
> Sea la Hessiana en ese punto: $$H = \begin{bmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{bmatrix}\bigg|_{(x_0,y_0)}$$
> 
> Definimos:
> 
> - $D = \det(H) = f_{xx}f_{yy} - (f_{xy})^2$ (determinante de $H$)
> - $A = f_{xx}(x_0, y_0)$
> 
> ---
> 
> ### Clasificación:
> 
> |Condición|Clasificación|
> |---|---|
> |$D > 0$ y $A > 0$|**Mínimo local**|
> |$D > 0$ y $A < 0$|**Máximo local**|
> |$D < 0$ | **Punto silla** |
> | $D = 0$ | **Indeterminado** (requiere análisis adicional) |
> 
> ---
> 
> ### Interpretación visual:
> 
> **Mínimo local** ($D > 0$, $A > 0$):
> 
> ```
>         z
>         │
>         │    ╱╲
>         │   ╱  ╲
>         │  │  • │  ← Valle (paraboloide hacia arriba)
>         │   ╲  ╱
>         │    ╲╱
>         └────────── y
>        ╱
>       x
> ```
> 
> **Máximo local** ($D > 0$, $A < 0$):
> 
> ```
>         z
>         │    ╲╱
>         │   ╱  ╲
>         │  │  • │  ← Pico (paraboloide hacia abajo)
>         │   ╲  ╱
>         │    ╱╲
>         └────────── y
>        ╱
>       x
> ```
> 
> **Punto silla** ($D < 0$):
> 
> ```
>         z
>         │   ╱│╲
>         │  ╱ │ ╲
>         │ ╱  •  ╲  ← Silla de montar
>         │╱   │   ╲
>         └────────── y
>        ╱
>       x
> ```
> 
> ---
> 
> ### Mnemónica:
> 
> - **D**eterminante **D**escribe la naturaleza del punto
> - Si $D > 0$: el punto es extremo → mirar **A** para saber si es máx o mín
> - Si $D < 0$: punto **S**illa (ambas letras tienen curvas opuestas: **S** y **D**)

### 🔬 Criterio de Sylvester (n Variables)

> [!note]- 🟣 Criterio General: Menores Principales
> 
> Para funciones de $n$ variables, usamos los **menores principales** de la Hessiana.
> 
> ### Definición:
> 
> El $k$-ésimo **menor principal** $D_k$ es el determinante de la submatriz $k \times k$ superior izquierda de $H$.
> 
> Para $n = 3$: $$D_1 = f_{xx}$$ $$D_2 = \begin{vmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{vmatrix}$$ $$D_3 = \det(H) = \begin{vmatrix} f_{xx} & f_{xy} & f_{xz} \ f_{xy} & f_{yy} & f_{yz} \ f_{xz} & f_{yz} & f_{zz} \end{vmatrix}$$
> 
> ---
> 
> ### Clasificación en un punto crítico:
> 
> |Condición|Clasificación|
> |---|---|
> |Todos los $D_k > 0$|**Definida positiva** → Mínimo local|
> |$D_k$ alternan: $D_1 < 0$, $D_2 > 0$, $D_3 < 0$, ...|**Definida negativa** → Máximo local|
> |Ni definida positiva ni negativa|**Indefinida** → Punto silla|
> |Algún $D_k = 0$|**Indeterminado**|
> 
> ---
> 
> ### Criterio alternativo (valores propios):
> 
> Calcular los valores propios $\lambda_1, \lambda_2, \ldots, \lambda_n$ de $H$:
> 
> |Valores propios|Clasificación|
> |---|---|
> |Todos $\lambda_i > 0$|**Definida positiva** → Mínimo|
> |Todos $\lambda_i < 0$|**Definida negativa** → Máximo|
> |Algunos $> 0$, otros $< 0$|**Indefinida** → Punto silla|
> |Algún $\lambda_i = 0$|**Semidefinida** o indefinida|

---

## 📚 Ejemplos: Clasificación de Puntos Críticos

### Ejemplo 9: Función Cuadrática Simple

> [!example]- 📝 Ejemplo 9: Paraboloide
> 
> **Función:** $$f(x,y) = x^2 + y^2$$
> 
> ---
> 
> **Paso 1: Encontrar puntos críticos** $$\nabla f = (2x, 2y) = (0, 0)$$ $$\implies (x, y) = (0, 0)$$
> 
> ---
> 
> **Paso 2: Calcular la Hessiana** $$H = \begin{bmatrix} 2 & 0 \ 0 & 2 \end{bmatrix}$$
> 
> ---
> 
> **Paso 3: Aplicar criterio** $$D = \det(H) = 4 > 0$$ $$A = f_{xx} = 2 > 0$$
> 
> $$\boxed{\text{Mínimo local en } (0, 0)}$$
> 
> ---
> 
> **Verificación:** $$f(0,0) = 0 \leq f(x,y) = x^2 + y^2 \text{ para todo } (x,y)$$
> 
> De hecho, es un **mínimo global**.

### Ejemplo 10: Punto Silla Clásico

> [!example]- 📝 Ejemplo 10: Silla de Montar
> 
> **Función:** $$f(x,y) = x^2 - y^2$$
> 
> ---
> 
> **Paso 1: Punto crítico** $$\nabla f = (2x, -2y) = (0, 0)$$ $$\implies (0, 0)$$
> 
> ---
> 
> **Paso 2: Hessiana** $$H = \begin{bmatrix} 2 & 0 \ 0 & -2 \end{bmatrix}$$
> 
> ---
> 
> **Paso 3: Clasificación** $$D = \det(H) = 2(-2) - 0 = -4 < 0$$
> 
> $$\boxed{\text{Punto silla en } (0, 0)}$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - En la dirección $x$: $f(x, 0) = x^2$ → curva hacia arriba (mínimo)
> - En la dirección $y$: $f(0, y) = -y^2$ → curva hacia abajo (máximo)
> - Es un **punto silla**: mínimo en una dirección, máximo en otra
> 
> ```
>     z
>     │  ╱│╲
>     │ ╱ │ ╲
>     │╱  •  ╲  ← Silla
>     └────────── y
>    ╱
>   x
> ```

### Ejemplo 11: Función más Compleja

> [!example]- 📝 Ejemplo 11: Múltiples Puntos Críticos
> 
> **Función:** $$f(x,y) = x^3 + y^3 - 3xy$$
> 
> ---
> 
> **Paso 1: Encontrar puntos críticos** $$f_x = 3x^2 - 3y = 0 \implies y = x^2$$ $$f_y = 3y^2 - 3x = 0 \implies x = y^2$$
> 
> Sustituyendo $y = x^2$ en $x = y^2$: $$x = (x^2)^2 = x^4$$ $$x^4 - x = 0$$ $$x(x^3 - 1) = 0$$ $$x = 0 \text{ o } x = 1$$
> 
> **Puntos críticos:**
> 
> - $(0, 0)$: cuando $x = 0$, entonces $y = 0$
> - $(1, 1)$: cuando $x = 1$, entonces $y = 1$
> 
> ---
> 
> **Paso 2: Calcular la Hessiana** $$f_{xx} = 6x, \quad f_{yy} = 6y, \quad f_{xy} = -3$$
> 
> $$H = \begin{bmatrix} 6x & -3 \ -3 & 6y \end{bmatrix}$$
> 
> ---
> 
> **Paso 3: Clasificar $(0, 0)$** $$H(0,0) = \begin{bmatrix} 0 & -3 \ -3 & 0 \end{bmatrix}$$ $$D = 0 \cdot 0 - (-3)^2 = -9 < 0$$
> 
> $$\boxed{\text{Punto silla en } (0, 0)}$$
> 
> ---
> 
> **Paso 4: Clasificar $(1, 1)$** $$H(1,1) = \begin{bmatrix} 6 & -3 \ -3 & 6 \end{bmatrix}$$ $$D = 6 \cdot 6 - (-3)^2 = 36 - 9 = 27 > 0$$ $$A = f_{xx}(1,1) = 6 > 0$$
> 
> $$\boxed{\text{Mínimo local en } (1, 1)}$$
> 
> ---
> 
> **Valores de la función:** $$f(0,0) = 0$$ $$f(1,1) = 1 + 1 - 3 = -1$$

### Ejemplo 12: Tres Variables

> [!example]- 📝 Ejemplo 12: Función en $\mathbb{R}^3$
> 
> **Función:** $$f(x,y,z) = x^2 + 2y^2 + 3z^2 - 2xy$$
> 
> ---
> 
> **Paso 1: Punto crítico** $$\nabla f = (2x - 2y, 4y - 2x, 6z) = (0, 0, 0)$$
> 
> De la tercera ecuación: $z = 0$
> 
> De las primeras dos: $$2x - 2y = 0 \implies x = y$$ $$4y - 2x = 0 \implies 4y - 2y = 0 \implies y = 0$$
> 
> **Punto crítico:** $(0, 0, 0)$
> 
> ---
> 
> **Paso 2: Hessiana** $$H = \begin{bmatrix} 2 & -2 & 0 \ -2 & 4 & 0 \ 0 & 0 & 6 \end{bmatrix}$$
> 
> ---
> 
> **Paso 3: Menores principales** $$D_1 = 2 > 0$$ $$D_2 = \begin{vmatrix} 2 & -2 \ -2 & 4 \end{vmatrix} = 8 - 4 = 4 > 0$$ $$D_3 = \det(H) = 6 \cdot D_2 = 6 \cdot 4 = 24 > 0$$
> 
> Todos los menores son positivos.
> 
> $$\boxed{\text{Mínimo local en } (0, 0, 0)}$$
> 
> ---
> 
> **Verificación (valores propios):**
> 
> La matriz $2 \times 2$ superior izquierda tiene valores propios: $$\lambda = \frac{6 \pm \sqrt{36-16}}{2} = \frac{6 \pm \sqrt{20}}{2} = 3 \pm \sqrt{5}$$
> 
> Ambos son positivos (aproximadamente 5.236 y 0.764).
> 
> El tercer valor propio es $\lambda_3 = 6 > 0$.
> 
> Todos los valores propios son positivos → **definida positiva**.

---

## 🎨 Aproximación de Taylor de Segundo Orden

> [!note]- 📐 Fórmula de Taylor Multivariable
> 
> ### Aproximación de segundo orden
> 
> Para una función $f: \mathbb{R}^n \to \mathbb{R}$ de clase $C^2$, la **aproximación de Taylor de segundo orden** cerca del punto $\mathbf{a}$ es:
> 
> $$f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot (\mathbf{x} - \mathbf{a}) + \frac{1}{2}(\mathbf{x} - \mathbf{a})^T H_f(\mathbf{a}) (\mathbf{x} - \mathbf{a})$$
> 
> ---
> 
> ### Para dos variables:
> 
> $$f(x,y) \approx f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$ $$+ \frac{1}{2}[f_{xx}(a,b)(x-a)^2 + 2f_{xy}(a,b)(x-a)(y-b) + f_{yy}(a,b)(y-b)^2]$$
> 
> ---
> 
> ### Interpretación:
> 
> - **Término de orden 0:** $f(\mathbf{a})$ → valor en el punto
> - **Término de orden 1:** $\nabla f(\mathbf{a}) \cdot (\mathbf{x} - \mathbf{a})$ → aproximación lineal (diferencial)
> - **Término de orden 2:** $\frac{1}{2}(\mathbf{x} - \mathbf{a})^T H (\mathbf{x} - \mathbf{a})$ → corrección cuadrática (curvatura)
> 
> ---
> 
> ### En un punto crítico:
> 
> Si $\nabla f(\mathbf{a}) = \mathbf{0}$ (punto crítico), la aproximación se simplifica:
> 
> $$f(\mathbf{x}) \approx f(\mathbf{a}) + \frac{1}{2}(\mathbf{x} - \mathbf{a})^T H_f(\mathbf{a}) (\mathbf{x} - \mathbf{a})$$
> 
> La naturaleza del punto crítico depende completamente de la Hessiana.

### Ejemplo 13: Taylor de Segundo Orden

> [!example]- 📝 Ejemplo 13: Aproximación Cuadrática
> 
> **Función:** $$f(x,y) = e^x \cos(y)$$
> 
> **Aproximar cerca del punto** $(0, 0)$.
> 
> ---
> 
> **Paso 1: Valor en el punto** $$f(0, 0) = e^0 \cos(0) = 1$$
> 
> ---
> 
> **Paso 2: Gradiente** $$f_x = e^x \cos(y) \implies f_x(0,0) = 1$$ $$f_y = -e^x \sin(y) \implies f_y(0,0) = 0$$
> 
> $$\nabla f(0,0) = (1, 0)$$
> 
> ---
> 
> **Paso 3: Hessiana** $$f_{xx} = e^x \cos(y) \implies f_{xx}(0,0) = 1$$ $$f_{yy} = -e^x \cos(y) \implies f_{yy}(0,0) = -1$$ $$f_{xy} = -e^x \sin(y) \implies f_{xy}(0,0) = 0$$
> 
> $$H(0,0) = \begin{bmatrix} 1 & 0 \ 0 & -1 \end{bmatrix}$$
> 
> ---
> 
> **Paso 4: Aproximación de Taylor** $$f(x,y) \approx 1 + 1 \cdot x + 0 \cdot y + \frac{1}{2}[1 \cdot x^2 + 2(0)xy + (-1)y^2]$$
> 
> $$\boxed{f(x,y) \approx 1 + x + \frac{x^2}{2} - \frac{y^2}{2}}$$
> 
> ---
> 
> **Verificación:** Para $(0.1, 0.1)$:
> 
> **Valor exacto:** $$f(0.1, 0.1) = e^{0.1}\cos(0.1) \approx 1.1052 \times 0.9950 \approx 1.0997$$
> 
> **Aproximación:** $$1 + 0.1 + \frac{(0.1)^2}{2} - \frac{(0.1)^2}{2} = 1.1$$
> 
> Error: $|1.0997 - 1.1| = 0.0003$ (¡muy pequeño!)

---

## 🎯 Optimización sin Restricciones

### 📊 Estrategia General

> [!tip]- ✅ Pasos para Optimizar
> 
> Para encontrar **extremos** de $f(\mathbf{x})$:
> 
> ### Paso 1: Encontrar puntos críticos
> 
> Resolver $\nabla f = \mathbf{0}$ $$\frac{\partial f}{\partial x_1} = 0, \quad \frac{\partial f}{\partial x_2} = 0, \quad \ldots, \quad \frac{\partial f}{\partial x_n} = 0$$
> 
> ---
> 
> ### Paso 2: Calcular la Hessiana
> 
> $$H_f = \begin{bmatrix} f_{x_1 x_1} & f_{x_1 x_2} & \cdots \ f_{x_2 x_1} & f_{x_2 x_2} & \cdots \ \vdots & \vdots & \ddots \end{bmatrix}$$
> 
> ---
> 
> ### Paso 3: Clasificar cada punto crítico
> 
> - Calcular $\det(H)$ y menores principales
> - O calcular valores propios de $H$
> - Aplicar criterio de clasificación
> 
> ---
> 
> ### Paso 4: Verificar condiciones de frontera
> 
> Si el dominio tiene frontera, evaluar $f$ en:
> 
> - Los puntos críticos interiores
> - Los extremos en la frontera
> - Comparar valores para encontrar máximo/mínimo global
> 
> ---
> 
> ### Condiciones necesarias vs suficientes:
> 
> **Condición necesaria** (primer orden): $$\nabla f(\mathbf{x}^*) = \mathbf{0}$$
> 
> **Condición suficiente** (segundo orden):
> 
> - Para mínimo: $\nabla f = \mathbf{0}$ y $H$ definida positiva
> - Para máximo: $\nabla f = \mathbf{0}$ y $H$ definida negativa

### Ejemplo 14: Problema de Optimización

> [!example]- 📝 Ejemplo 14: Minimizar Distancia
> 
> **Problema:** Encontrar el punto en el plano $z = x + y + 1$ que está más cerca del origen.
> 
> ---
> 
> **Planteamiento:**
> 
> Minimizar la distancia al origen: $$d = \sqrt{x^2 + y^2 + z^2}$$
> 
> Equivalentemente, minimizar: $$f(x,y) = x^2 + y^2 + z^2 = x^2 + y^2 + (x+y+1)^2$$
> 
> $$f(x,y) = x^2 + y^2 + x^2 + y^2 + 2xy + 2x + 2y + 1$$ $$= 2x^2 + 2y^2 + 2xy + 2x + 2y + 1$$
> 
> ---
> 
> **Paso 1: Puntos críticos** $$f_x = 4x + 2y + 2 = 0$$ $$f_y = 4y + 2x + 2 = 0$$
> 
> De la primera ecuación: $2x + y = -1$ → $y = -1 - 2x$
> 
> Sustituyendo en la segunda: $$4(-1 - 2x) + 2x + 2 = 0$$ $$-4 - 8x + 2x + 2 = 0$$ $$-6x = 2$$ $$x = -\frac{1}{3}$$
> 
> $$y = -1 - 2\left(-\frac{1}{3}\right) = -1 + \frac{2}{3} = -\frac{1}{3}$$
> 
> $$z = -\frac{1}{3} - \frac{1}{3} + 1 = \frac{1}{3}$$
> 
> **Punto crítico:** $\left(-\frac{1}{3}, -\frac{1}{3}, \frac{1}{3}\right)$
> 
> ---
> 
> **Paso 2: Hessiana** $$f_{xx} = 4, \quad f_{yy} = 4, \quad f_{xy} = 2$$
> 
> $$H = \begin{bmatrix} 4 & 2 \ 2 & 4 \end{bmatrix}$$
> 
> ---
> 
> **Paso 3: Clasificación** $$D = 4 \cdot 4 - 2^2 = 16 - 4 = 12 > 0$$ $$A = 4 > 0$$
> 
> $$\boxed{\text{Mínimo local (y global) en } \left(-\frac{1}{3}, -\frac{1}{3}, \frac{1}{3}\right)}$$
> 
> ---
> 
> **Distancia mínima:** $$d = \sqrt{\left(-\frac{1}{3}\right)^2 + \left(-\frac{1}{3}\right)^2 + \left(\frac{1}{3}\right)^2} = \sqrt{\frac{3}{9}} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$$

### Ejemplo 15: Maximizar Producción

> [!example]- 📝 Ejemplo 15: Economía - Función de Producción
> 
> **Situación:** Una empresa tiene función de producción: $$P(x,y) = 100x + 80y - x^2 - y^2 - xy$$
> 
> donde $x$ e $y$ son cantidades de dos insumos. Los costos totales son: $$C(x,y) = 40x + 30y$$
> 
> **Maximizar el beneficio** $B(x,y) = P(x,y) - C(x,y)$.
> 
> ---
> 
> **Función objetivo:** $$B(x,y) = 100x + 80y - x^2 - y^2 - xy - 40x - 30y$$ $$= 60x + 50y - x^2 - y^2 - xy$$
> 
> ---
> 
> **Paso 1: Puntos críticos** $$B_x = 60 - 2x - y = 0$$ $$B_y = 50 - 2y - x = 0$$
> 
> De la primera: $y = 60 - 2x$
> 
> Sustituyendo: $$50 - 2(60 - 2x) - x = 0$$ $$50 - 120 + 4x - x = 0$$ $$3x = 70$$ $$x = \frac{70}{3} \approx 23.33$$
> 
> $$y = 60 - 2 \cdot \frac{70}{3} = 60 - \frac{140}{3} = \frac{40}{3} \approx 13.33$$
> 
> ---
> 
> **Paso 2: Hessiana** $$B_{xx} = -2, \quad B_{yy} = -2, \quad B_{xy} = -1$$
> 
> $$H = \begin{bmatrix} -2 & -1 \ -1 & -2 \end{bmatrix}$$
> 
> ---
> 
> **Paso 3: Clasificación** $$D = (-2)(-2) - (-1)^2 = 4 - 1 = 3 > 0$$ $$A = -2 < 0$$
> 
> $$\boxed{\text{Máximo en } \left(\frac{70}{3}, \frac{40}{3}\right)}$$
> 
> ---
> 
> **Beneficio máximo:** $$B\left(\frac{70}{3}, \frac{40}{3}\right) = 60 \cdot \frac{70}{3} + 50 \cdot \frac{40}{3} - \left(\frac{70}{3}\right)^2 - \left(\frac{40}{3}\right)^2 - \frac{70}{3} \cdot \frac{40}{3}$$
> 
> $$= \frac{4200 + 2000 - 4900 - 1600 - 2800}{9} = \frac{-3100}{9}$$
> 
> Espera, esto da negativo... Revisemos el cálculo.
> 
> Realmente: $$B = 60 \cdot \frac{70}{3} + 50 \cdot \frac{40}{3} - \frac{4900}{9} - \frac{1600}{9} - \frac{2800}{9}$$ $$= 1400 + \frac{2000}{3} - \frac{9300}{9}$$ $$= 1400 + 666.67 - 1033.33 = 1033.34$$
> 
> **Beneficio máximo ≈ 1033 unidades monetarias**

---

## 🌍 Aplicaciones Avanzadas

### 🤖 Machine Learning: Descenso de Gradiente

> [!example]- 🧠 Aplicación: Optimización en ML
> 
> **Contexto:** En machine learning, queremos minimizar una **función de pérdida** (loss function) $L(\mathbf{w})$ donde $\mathbf{w}$ son los parámetros del modelo.
> 
> ### Descenso de Gradiente (Gradient Descent)
> 
> **Algoritmo iterativo:** $$\mathbf{w}^{(k+1)} = \mathbf{w}^{(k)} - \alpha \nabla L(\mathbf{w}^{(k)})$$
> 
> donde:
> 
> - $\mathbf{w}^{(k)}$ son los parámetros en la iteración $k$
> - $\alpha > 0$ es la **tasa de aprendizaje** (learning rate)
> - $\nabla L$ es el gradiente de la función de pérdida
> 
> ---
> 
> ### Interpretación:
> 
> - Nos movemos en la dirección **opuesta** al gradiente (dirección de mayor descenso)
> - La Hessiana $H_L$ nos dice sobre la **curvatura** del espacio de pérdida
> - Si $H_L$ es definida positiva en el mínimo → convergencia garantizada (localmente)
> 
> ---
> 
> ### Método de Newton (usa la Hessiana)
> 
> Una mejora del descenso de gradiente: $$\mathbf{w}^{(k+1)} = \mathbf{w}^{(k)} - [H_L(\mathbf{w}^{(k)})]^{-1} \nabla L(\mathbf{w}^{(k)})$$
> 
> **Ventaja:** Convergencia más rápida (cuadrática vs lineal)
> 
> **Desventaja:** Requiere calcular e invertir la Hessiana (costoso computacionalmente)
> 
> ---
> 
> ### Ejemplo simple: Regresión lineal
> 
> **Función de pérdida:** $$L(w_0, w_1) = \sum_{i=1}^n (y_i - w_0 - w_1 x_i)^2$$
> 
> **Gradiente:** $$\frac{\partial L}{\partial w_0} = -2\sum(y_i - w_0 - w_1 x_i)$$ $$\frac{\partial L}{\partial w_1} = -2\sum x_i(y_i - w_0 - w_1 x_i)$$
> 
> **Hessiana:** $$H = 2\begin{bmatrix} n & \sum x_i \ \sum x_i & \sum x_i^2 \end{bmatrix}$$
> 
> Esta Hessiana es siempre definida positiva (cuando $x_i$ no son todos iguales), lo que garantiza que existe un único mínimo global.

### 🔬 Física: Estabilidad de Equilibrio

> [!example]- ⚛️ Aplicación: Energía Potencial
> 
> **Contexto:** En física, un sistema en equilibrio está en un punto donde la energía potencial $U(\mathbf{r})$ tiene derivada cero.
> 
> ### Análisis de Estabilidad
> 
> Para una partícula en posición $\mathbf{r} = (x, y, z)$ con energía potencial $U(\mathbf{r})$:
> 
> **Condición de equilibrio:** $$\nabla U(\mathbf{r}_0) = \mathbf{0}$$
> 
> La fuerza es $\mathbf{F} = -\nabla U$, así que en equilibrio $\mathbf{F} = \mathbf{0}$.
> 
> ---
> 
> ### Clasificación del equilibrio usando la Hessiana:
> 
> |Hessiana $H_U$ en $\mathbf{r}_0$|Tipo de equilibrio|
> |---|---|
> |Definida positiva|**Estable** (mínimo de energía)|
> |Definida negativa|**Inestable** (máximo de energía)|
> |Indefinida|**Inestable** (punto silla)|
> |Semidefinida|**Marginalmente estable** o inestable|
> 
> ---
> 
> ### Ejemplo: Péndulo doble (simplificado)
> 
> **Energía potencial:** $$U(\theta_1, \theta_2) = -mg\ell_1\cos\theta_1 - mg\ell_2\cos(\theta_1 + \theta_2)$$
> 
> **Puntos de equilibrio:**
> 
> 1. $(\theta_1, \theta_2) = (0, 0)$ → péndulo colgando hacia abajo
> 2. $(\theta_1, \theta_2) = (\pi, 0)$ → péndulo hacia arriba
> 
> **Hessiana en** $(0, 0)$: $$H_U(0,0) = mg\begin{bmatrix} \ell_1 + \ell_2 & \ell_2 \ \ell_2 & \ell_2 \end{bmatrix}$$
> 
> Valores propios positivos → **equilibrio estable**
> 
> **Hessiana en** $(\pi, 0)$: $$H_U(\pi, 0) = -mg\begin{bmatrix} \ell_1 + \ell_2 & \ell_2 \ \ell_2 & \ell_2 \end{bmatrix}$$
> 
> Valores propios negativos → **equilibrio inestable**
> 
> ---
> 
> ### Interpretación física:
> 
> - Bola en un valle (mínimo) → pequeñas perturbaciones hacen que oscile pero regrese
> - Bola en una colina (máximo) → pequeñas perturbaciones hacen que ruede lejos
> - Bola en una silla de montar → estable en una dirección, inestable en otra

### 📊 Economía: Análisis de Segundo Orden

> [!example]- 💼 Aplicación: Teoría del Consumidor
> 
> **Contexto:** Un consumidor tiene función de utilidad $U(x_1, x_2, \ldots, x_n)$ donde $x_i$ son cantidades de bienes.
> 
> ### Condiciones de Segundo Orden
> 
> **Problema:** Maximizar $U(\mathbf{x})$ sujeto a restricción presupuestaria.
> 
> En un óptimo interior, las **condiciones de segundo orden** requieren que la Hessiana de la función de Lagrange (veremos esto más adelante) sea definida negativa en el espacio tangente a la restricción.
> 
> ---
> 
> ### Ejemplo: Función de utilidad Cobb-Douglas
> 
> $$U(x, y) = x^\alpha y^\beta$$
> 
> donde $0 < \alpha, \beta < 1$ y $\alpha + \beta < 1$ (rendimientos decrecientes).
> 
> **Hessiana:** $$U_x = \alpha x^{\alpha-1}y^\beta, \quad U_y = \beta x^\alpha y^{\beta-1}$$
> 
> $$U_{xx} = \alpha(\alpha-1)x^{\alpha-2}y^\beta < 0$$ $$U_{yy} = \beta(\beta-1)x^\alpha y^{\beta-2} < 0$$ $$U_{xy} = \alpha\beta x^{\alpha-1}y^{\beta-1} > 0$$
> 
> $$H_U = \begin{bmatrix} \alpha(\alpha-1)x^{\alpha-2}y^\beta & \alpha\beta x^{\alpha-1}y^{\beta-1} \ \alpha\beta x^{\alpha-1}y^{\beta-1} & \beta(\beta-1)x^\alpha y^{\beta-2} \end{bmatrix}$$
> 
> **Determinante:** $$\det(H) = \alpha\beta(\alpha-1)(\beta-1)x^{2\alpha-2}y^{2\beta-2} - \alpha^2\beta^2 x^{2\alpha-2}y^{2\beta-2}$$ $$= \alpha\beta x^{2\alpha-2}y^{2\beta-2}[(\alpha-1)(\beta-1) - \alpha\beta]$$ $$= \alpha\beta x^{2\alpha-2}y^{2\beta-2}[\alpha\beta - \alpha - \beta + 1 - \alpha\beta]$$ $$= \alpha\beta x^{2\alpha-2}y^{2\beta-2}[1 - \alpha - \beta] > 0$$
> 
> (positivo si $\alpha + \beta < 1$)
> 
> Con $U_{xx} < 0$ y $\det(H) > 0$, la Hessiana es **definida negativa** → función **cóncava** → cualquier máximo local es global.

### 🏗️ Ingeniería: Diseño Óptimo

> [!example]- 🔧 Aplicación: Optimización Estructural
> 
> **Problema:** Diseñar una caja rectangular sin tapa con volumen fijo $V_0$ que minimice el área de material usado.
> 
> **Variables:** largo $x$, ancho $y$, altura $z$
> 
> ---
> 
> **Restricción:** $$xyz = V_0$$
> 
> **Función objetivo (área superficial):** $$A = xy + 2xz + 2yz$$
> 
> ---
> 
> **Método 1: Sustitución**
> 
> De la restricción: $z = \frac{V_0}{xy}$
> 
> $$A(x,y) = xy + 2x\frac{V_0}{xy} + 2y\frac{V_0}{xy} = xy + \frac{2V_0}{y} + \frac{2V_0}{x}$$
> 
> **Derivadas parciales:** $$A_x = y - \frac{2V_0}{x^2} = 0$$ $$A_y = x - \frac{2V_0}{y^2} = 0$$
> 
> De estas ecuaciones: $$y = \frac{2V_0}{x^2}, \quad x = \frac{2V_0}{y^2}$$
> 
> Sustituyendo: $$y = \frac{2V_0}{x^2} \implies x = \frac{2V_0}{(2V_0/x^2)^2} = \frac{2V_0 x^4}{4V_0^2} = \frac{x^4}{2V_0}$$
> 
> $$2V_0 = x^3 \implies x = (2V_0)^{1/3}$$
> 
> Por simetría del problema: $y = (2V_0)^{1/3}$
> 
> Y entonces: $z = \frac{V_0}{xy} = \frac{V_0}{(2V_0)^{2/3}} = \frac{V_0^{1/3}}{2^{2/3}} = \frac{(2V_0)^{1/3}}{2}$
> 
> **Resultado:** La caja óptima tiene base cuadrada con $x = y = (2V_0)^{1/3}$ y altura $z = x/2$.
> 
> ---
> 
> **Verificación con Hessiana:**
> 
> $$A_{xx} = \frac{4V_0}{x^3}, \quad A_{yy} = \frac{4V_0}{y^3}, \quad A_{xy} = 1$$
> 
> En el punto crítico $x = y = (2V_0)^{1/3}$:
> 
> $$A_{xx} = \frac{4V_0}{2V_0} = 2, \quad A_{yy} = 2$$
> 
> $$H = \begin{bmatrix} 2 & 1 \ 1 & 2 \end{bmatrix}$$
> 
> $$\det(H) = 4 - 1 = 3 > 0, \quad A_{xx} = 2 > 0$$
> 
> $$\boxed{\text{Mínimo confirmado}}$$

---

## 🎓 Teoremas Importantes

### 📐 Teorema del Valor Medio (Multivariable)

> [!note]- 🟣 Teorema: Valor Medio Multivariable
> 
> **Enunciado:** Sea $f: \mathbb{R}^n \to \mathbb{R}$ diferenciable en un conjunto convexo abierto $D$. Si $\mathbf{a}, \mathbf{b} \in D$, entonces existe $\mathbf{c}$ en el segmento que une $\mathbf{a}$ y $\mathbf{b}$ tal que:
> 
> $$f(\mathbf{b}) - f(\mathbf{a}) = \nabla f(\mathbf{c}) \cdot (\mathbf{b} - \mathbf{a})$$
> 
> ---
> 
> **Interpretación:**
> 
> - El cambio en $f$ es igual a la diferencial evaluada en algún punto intermedio
> - Generaliza el teorema del valor medio de una variable
> - Útil para estimación de errores y análisis de convergencia
> 
> ---
> 
> **Para dos variables:** $$f(x_1, y_1) - f(x_0, y_0) = f_x(c, d)(x_1 - x_0) + f_y(c, d)(y_1 - y_0)$$
> 
> para algún $(c, d)$ en el segmento de $(x_0, y_0)$ a $(x_1, y_1)$.

### 🎯 Teorema de Taylor Multivariable

> [!note]- 🟡 Teorema: Fórmula de Taylor con Resto
> 
> **Enunciado:** Sea $f: \mathbb{R}^n \to \mathbb{R}$ de clase $C^{k+1}$ en una bola alrededor de $\mathbf{a}$. Entonces para $\mathbf{x}$ en esa bola:
> 
> $$f(\mathbf{x}) = f(\mathbf{a}) + \sum_{|\alpha|=1}^k \frac{1}{\alpha!}D^\alpha f(\mathbf{a})(\mathbf{x}-\mathbf{a})^\alpha + R_k(\mathbf{x})$$
> 
> donde $R_k(\mathbf{x})$ es el resto.
> 
> ---
> 
> **Para $k=2$ (segundo orden):**
> 
> $$f(\mathbf{x}) = f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot (\mathbf{x}-\mathbf{a})$$ $$+ \frac{1}{2}(\mathbf{x}-\mathbf{a})^T H_f(\mathbf{a})(\mathbf{x}-\mathbf{a}) + R_2(\mathbf{x})$$
> 
> **Resto (forma de Lagrange):** $$R_2(\mathbf{x}) = \frac{1}{6}\sum_{i,j,k=1}^n \frac{\partial^3 f}{\partial x_i \partial x_j \partial x_k}(\mathbf{c})(x_i-a_i)(x_j-a_j)(x_k-a_k)$$
> 
> para algún $\mathbf{c}$ en el segmento de $\mathbf{a}$ a $\mathbf{x}$.
> 
> ---
> 
> **Orden del resto:** $$R_2(\mathbf{x}) = O(|\mathbf{x}-\mathbf{a}|^3)$$
> 
> Esto significa que el error es del orden del cubo de la distancia.

### 🔬 Condiciones de Optimalidad

> [!note]- 🟢 Teorema: Condiciones Necesarias y Suficientes
> 
> ### Condiciones Necesarias (Primer Orden)
> 
> **Teorema:** Si $f$ tiene un extremo local en $\mathbf{x}^*$ y es diferenciable en ese punto, entonces:
> 
> $$\nabla f(\mathbf{x}^*) = \mathbf{0}$$
> 
> ---
> 
> ### Condiciones Suficientes (Segundo Orden)
> 
> Sea $\mathbf{x}^_$ un punto crítico de $f$ (i.e., $\nabla f(\mathbf{x}^_) = \mathbf{0}$) y suponga que $f$ es $C^2$ cerca de $\mathbf{x}^*$.
> 
> **Para mínimo local:**
> 
> Si $H_f(\mathbf{x}^_)$ es **definida positiva**, entonces $\mathbf{x}^_$ es un **mínimo local estricto**.
> 
> **Para máximo local:**
> 
> Si $H_f(\mathbf{x}^_)$ es **definida negativa**, entonces $\mathbf{x}^_$ es un **máximo local estricto**.
> 
> **Para punto silla:**
> 
> Si $H_f(\mathbf{x}^_)$ es **indefinida** (tiene valores propios de signos diferentes), entonces $\mathbf{x}^_$ es un **punto silla**.
> 
> ---
> 
> ### Casos frontera:
> 
> Si $H_f(\mathbf{x}^*)$ es **semidefinida** (algunos valores propios cero), el test no es concluyente y se requiere análisis de orden superior.
> 
> ---
> 
> **Nota importante:** Estas son condiciones **locales**. Para extremos globales, se debe:
> 
> 1. Encontrar todos los puntos críticos
> 2. Evaluar $f$ en cada uno
> 3. Considerar el comportamiento en la frontera (si existe)
> 4. Comparar valores

---

## 📊 Tabla Resumen: Criterios de Clasificación

> [!note]- 📋 Referencia Rápida
> 
> ### Para dos variables $f(x,y)$
> 
> En un punto crítico $(x_0, y_0)$ donde $\nabla f = (0,0)$:
> 
> |$\det(H)$|$f_{xx}$|Clasificación|
> |---|---|---|
> |$> 0$|$> 0$|**Mínimo local**|
> |$> 0$|$< 0$|**Máximo local**|
> |$< 0$|cualquiera|**Punto silla**|
> |$= 0$|cualquiera|**Indeterminado**|
> 
> donde $\det(H) = f_{xx}f_{yy} - (f_{xy})^2$
> 
> ---
> 
> ### Para $n$ variables
> 
> **Menores principales** $D_k$ ($k$-ésimo menor principal):
> 
> |Condición|Clasificación|
> |---|---|
> |Todos $D_k > 0$|**Definida positiva** → Mínimo|
> |$D_k$ alterna signos: $(-1)^k D_k > 0$|**Definida negativa** → Máximo|
> |Otros casos|**Indefinida** → Punto silla|
> 
> **Alternativamente (valores propios $\lambda_i$):**
> 
> |Valores propios|Clasificación|
> |---|---|
> |Todos $\lambda_i > 0$|**Mínimo local**|
> |Todos $\lambda_i < 0$|**Máximo local**|
> |Mixtos (+ y -)|**Punto silla**|
> |Algún $\lambda_i = 0$|**Indeterminado**|

---

## 💡 Trucos y Técnicas Útiles

> [!tip]- 🎯 Estrategias para Simplificar Cálculos
> 
> ### Truco 1: Identificar simetrías
> 
> Si la función tiene simetría, úsala para simplificar:
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2$
> 
> - Claramente simétrica en $x$ e $y$
> - Si hay un extremo, probablemente esté en $x = y$ o en $x = 0, y = 0$
> 
> ---
> 
> ### Truco 2: Cambio de variables
> 
> A veces un cambio de variables simplifica la Hessiana:
> 
> **Ejemplo:** Para $f(x,y) = e^{x^2+y^2}$, usar coordenadas polares: $$u = x^2 + y^2 \implies f = e^u$$
> 
> ---
> 
> ### Truco 3: Usar la estructura de la Hessiana
> 
> Para matrices especiales:
> 
> **Matriz diagonal:** $$H = \begin{bmatrix} a & 0 \ 0 & b \end{bmatrix}$$
> 
> - Definida positiva si $a, b > 0$
> - Valores propios son simplemente $a$ y $b$
> 
> **Matriz con patrón:** $$H = \begin{bmatrix} a & c \ c & b \end{bmatrix}$$
> 
> - $\det(H) = ab - c^2$
> - Si $a = b$, entonces definida positiva si $a > |c|$
> 
> ---
> 
> ### Truco 4: Completar cuadrados
> 
> Para funciones cuadráticas, completar cuadrados identifica el extremo:
> 
> **Ejemplo:** $f(x,y) = x^2 + 4xy + 5y^2$
> 
> $$= x^2 + 4xy + 4y^2 + y^2 = (x + 2y)^2 + y^2 \geq 0$$
> 
> Mínimo en $x + 2y = 0$ y $y = 0$, es decir, $(0,0)$.
> 
> ---
> 
> ### Truco 5: Verificación numérica
> 
> Si no estás seguro de la clasificación:
> 
> 1. Evalúa $f$ en el punto crítico
> 2. Evalúa $f$ en puntos cercanos en diferentes direcciones
> 3. Compara valores para intuir la naturaleza del punto

---

## 🎨 Visualización de Conceptos

> [!note]- 🖼️ Interpretación Gráfica Avanzada
> 
> ### Curvas de nivel y Hessiana
> 
> Para $f(x,y)$, las **curvas de nivel** $f(x,y) = c$ nos dan información sobre la curvatura:
> 
> **Mínimo local:**
> 
> ```
>       y
>       │
>       │    ╱─╲
>       │   │   │  ← Curvas de nivel cerradas, elípticas
>       │   │ • │    concéntricas alrededor del mínimo
>       │    ╲─╱
>       └────────── x
> ```
> 
> **Máximo local:**
> 
> ```
>       y
>       │
>       │    ╱─╲
>       │   │   │  ← Curvas cerradas alrededor del máximo
>       │   │ • │    (misma forma pero función decrece hacia afuera)
>       │    ╲─╱
>       └────────── x
> ```
> 
> **Punto silla:**
> 
> ```
>       y
>       │   ╱ │ ╲
>       │  │  │  │  ← Curvas hiperbólicas
>       │ ─ ─•─ ─    que se cruzan en el punto silla
>       │  │  │  │
>       │   ╲ │ ╱
>       └────────── x
> ```
> 
> ---
> 
> ### Secciones de la superficie
> 
> **En un mínimo:**
> 
> - Cualquier sección vertical es una parábola hacia arriba
> - La Hessiana es definida positiva
> 
> **En un máximo:**
> 
> - Cualquier sección vertical es una parábola hacia abajo
> - La Hessiana es definida negativa
> 
> **En un punto silla:**
> 
> - Algunas secciones curvan hacia arriba, otras hacia abajo
> - La Hessiana tiene valores propios de signos opuestos

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular diferenciales:**
> 
> a) $f(x,y) = x^3y + xy^2$
> 
> b) $f(x,y) = e^{2x}\sin(3y)$
> 
> c) $f(x,y,z) = xyz + x^2 + y^2 + z^2$
> 
> ---
> 
> **2. Calcular Hessianas:**
> 
> a) $f(x,y) = 3x^2 + 2xy + y^2$
> 
> b) $f(x,y) = x^4 + y^4 - 4xy$
> 
> c) $f(x,y) = \ln(1 + x^2 + y^2)$
> 
> ---
> 
> **3. Usar la diferencial para aproximar:**
> 
> a) $f(x,y) = \sqrt{x^2 + y^2}$ cerca de $(3, 4)$ para estimar $f(3.1, 3.9)$
> 
> b) $f(x,y) = e^{xy}$ cerca de $(0, 0)$ para estimar $f(0.1, 0.1)$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Clasificar puntos críticos:**
> 
> a) $f(x,y) = x^2 + xy + y^2 - 3x - 6y$
> 
> b) $f(x,y) = x^3 - 3xy + y^3$
> 
> c) $f(x,y) = e^{-x^2-y^2}(x^2 + 2y^2)$
> 
> ---
> 
> **5. Propagación de errores:**
> 
> a) El volumen de un cono es $V = \frac{1}{3}\pi r^2 h$. Si $r = 5 \pm 0.1$ cm y $h = 10 \pm 0.2$ cm, estimar el error en $V$.
> 
> b) La ley de gases ideales es $PV = nRT$. Si $P$, $V$ y $T$ se miden con errores del 2%, 3% y 1% respectivamente, ¿cuál es el error aproximado en $n$?
> 
> ---
> 
> **6. Optimización:**
> 
> a) Encontrar las dimensiones de la caja rectangular de volumen máximo que se puede inscribir en una esfera de radio $R$.
> 
> b) Minimizar $f(x,y) = x^2 + 2y^2 + 2xy + 2x - 3y$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Tres variables:**
> 
> a) Clasificar los puntos críticos de $f(x,y,z) = x^2 + y^2 + z^2 + 2xy - 4z$
> 
> b) Encontrar el volumen máximo de un paralelepípedo inscrito en el elipsoide $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$
> 
> ---
> 
> **8. Teoría:**
> 
> a) Demostrar que si $f$ es una función cuadrática $f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T A \mathbf{x} + \mathbf{b}^T\mathbf{x} + c$, entonces $H_f = A$.
> 
> b) Si $f$ es convexa (Hessiana siempre definida positiva), demostrar que cualquier mínimo local es global.
> 
> ---
> 
> **9. Aplicaciones:**
> 
> a) **Economía:** Una empresa produce dos bienes con función de beneficio $B(x,y) = -x^2 - y^2 + 10x + 8y - xy - 20$. Encontrar la producción óptima.
> 
> b) **Física:** La energía potencial de una partícula es $U(x,y) = x^2y + y^3 - 3y$. Encontrar y clasificar los puntos de equilibrio.
> 
> ---
> 
> **10. Aproximación de Taylor:**
> 
> a) Encontrar la aproximación de Taylor de segundo orden de $f(x,y) = \cos(x)\cos(y)$ cerca de $(0, 0)$.
> 
> b) Usar la aproximación para estimar $f(0.1, 0.2)$ y comparar con el valor exacto.

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = x^3y + xy^2$
> 
> $$df = (3x^2y + y^2)dx + (x^3 + 2xy)dy$$
> 
> ---
> 
> **2a)** $f(x,y) = 3x^2 + 2xy + y^2$
> 
> $$H = \begin{bmatrix} 6 & 2 \ 2 & 2 \end{bmatrix}$$
> 
> ---
> 
> **3a)** $f(x,y) = \sqrt{x^2 + y^2}$ cerca de $(3, 4)$
> 
> $$f(3,4) = 5$$ $$f_x(3,4) = \frac{3}{5}, \quad f_y(3,4) = \frac{4}{5}$$
> 
> $$f(3.1, 3.9) \approx 5 + \frac{3}{5}(0.1) + \frac{4}{5}(-0.1) = 5 + 0.06 - 0.08 = 4.98$$
> 
> **Valor exacto:** $\sqrt{(3.1)^2 + (3.9)^2} = \sqrt{9.61 + 15.21} = \sqrt{24.82} \approx 4.982$
> 
> ¡Excelente aproximación!

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $f(x,y) = x^2 + xy + y^2 - 3x - 6y$
> 
> **Punto crítico:** $$f_x = 2x + y - 3 = 0$$ $$f_y = x + 2y - 6 = 0$$
> 
> Resolviendo: $(x, y) = (0, 3)$
> 
> **Hessiana:** $$H = \begin{bmatrix} 2 & 1 \ 1 & 2 \end{bmatrix}$$
> 
> $$\det(H) = 3 > 0, \quad f_{xx} = 2 > 0$$
> 
> $$\boxed{\text{Mínimo local en } (0, 3)}$$
> 
> ---
> 
> **5a)** $V = \frac{1}{3}\pi r^2 h$
> 
> $$dV = \frac{2\pi rh}{3}dr + \frac{\pi r^2}{3}dh$$
> 
> Con $r = 5$, $h = 10$, $dr = 0.1$, $dh = 0.2$:
> 
> $$dV = \frac{2\pi(5)(10)}{3}(0.1) + \frac{\pi(25)}{3}(0.2)$$ $$= \frac{100\pi}{3}(0.1) + \frac{25\pi}{3}(0.2)$$
> $$= \frac{10\pi}{3} + \frac{5\pi}{3} = \frac{15\pi}{3} = 5\pi \approx 15.7 \text{ cm}^3$$
> 
> **Volumen nominal:** $V = \frac{1}{3}\pi(25)(10) = \frac{250\pi}{3} \approx 261.8$ cm³
> 
> **Error relativo:** $\frac{5\pi}{250\pi/3} = \frac{15}{250} = 0.06 = 6%$
> 
> ---
> 
> **6b)** $f(x,y) = x^2 + 2y^2 + 2xy + 2x - 3y$
> 
> **Punto crítico:** $$f_x = 2x + 2y + 2 = 0 \implies x + y = -1$$ $$f_y = 4y + 2x - 3 = 0$$
> 
> Sustituyendo $x = -1 - y$: $$4y + 2(-1-y) - 3 = 0$$ $$4y - 2 - 2y - 3 = 0$$ $$2y = 5 \implies y = \frac{5}{2}$$ $$x = -1 - \frac{5}{2} = -\frac{7}{2}$$
> 
> **Hessiana:** $$H = \begin{bmatrix} 2 & 2 \ 2 & 4 \end{bmatrix}$$
> 
> $$\det(H) = 8 - 4 = 4 > 0, \quad f_{xx} = 2 > 0$$
> 
> $$\boxed{\text{Mínimo en } \left(-\frac{7}{2}, \frac{5}{2}\right)}$$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **7a)** $f(x,y,z) = x^2 + y^2 + z^2 + 2xy - 4z$
> 
> **Punto crítico:** $$f_x = 2x + 2y = 0 \implies y = -x$$ $$f_y = 2y + 2x = 0 \implies y = -x$$ (misma ecuación) $$f_z = 2z - 4 = 0 \implies z = 2$$
> 
> De las primeras dos: $x$ puede ser cualquier valor con $y = -x$.
> 
> Espera, esto indica un **problema**: hay infinitos puntos críticos en la línea $y = -x, z = 2$.
> 
> Revisemos: las dos primeras ecuaciones son redundantes, lo que sugiere que hay una línea completa de puntos críticos.
> 
> **Hessiana:** $$H = \begin{bmatrix} 2 & 2 & 0 \ 2 & 2 & 0 \ 0 & 0 & 2 \end{bmatrix}$$
> 
> **Valores propios:** Resolviendo $\det(H - \lambda I) = 0$:
> 
> La submatriz $2 \times 2$ superior tiene valores propios $0$ y $4$ (suma = 4, producto = 0). El tercer valor propio es $2$.
> 
> Valores propios: ${0, 2, 4}$
> 
> Como hay un valor propio cero, la Hessiana es **semidefinida positiva**, no concluyente.
> 
> Reescribiendo: $$f(x,y,z) = x^2 + y^2 + 2xy + z^2 - 4z$$ $$= (x+y)^2 + (z-2)^2 - 4$$
> 
> **Mínimo global:** en cualquier punto con $x + y = 0$ y $z = 2$, donde $f = -4$.
> 
> ---
> 
> **9a)** $B(x,y) = -x^2 - y^2 + 10x + 8y - xy - 20$
> 
> **Punto crítico:** $$B_x = -2x + 10 - y = 0 \implies y = 10 - 2x$$ $$B_y = -2y + 8 - x = 0$$
> 
> Sustituyendo: $$-2(10 - 2x) + 8 - x = 0$$ $$-20 + 4x + 8 - x = 0$$ $$3x = 12 \implies x = 4$$ $$y = 10 - 8 = 2$$
> 
> **Hessiana:** $$H = \begin{bmatrix} -2 & -1 \ -1 & -2 \end{bmatrix}$$
> 
> $$\det(H) = 4 - 1 = 3 > 0, \quad B_{xx} = -2 < 0$$
> 
> $$\boxed{\text{Máximo en } (4, 2)}$$
> 
> **Beneficio máximo:** $$B(4,2) = -16 - 4 + 40 + 16 - 8 - 20 = 8$$
> 
> ---
> 
> **10a)** $f(x,y) = \cos(x)\cos(y)$ cerca de $(0,0)$
> 
> $$f(0,0) = 1$$
> 
> $$f_x = -\sin(x)\cos(y) \implies f_x(0,0) = 0$$ $$f_y = -\cos(x)\sin(y) \implies f_y(0,0) = 0$$
> 
> $$f_{xx} = -\cos(x)\cos(y) \implies f_{xx}(0,0) = -1$$ $$f_{yy} = -\cos(x)\cos(y) \implies f_{yy}(0,0) = -1$$ $$f_{xy} = \sin(x)\sin(y) \implies f_{xy}(0,0) = 0$$
> 
> **Aproximación de Taylor:** $$f(x,y) \approx 1 + 0 \cdot x + 0 \cdot y + \frac{1}{2}[(-1)x^2 + 0 \cdot xy + (-1)y^2]$$
> 
> $$\boxed{f(x,y) \approx 1 - \frac{x^2}{2} - \frac{y^2}{2}}$$
> 
> **Para** $(0.1, 0.2)$: $$f(0.1, 0.2) \approx 1 - \frac{0.01}{2} - \frac{0.04}{2} = 1 - 0.005 - 0.02 = 0.975$$
> 
> **Valor exacto:** $$\cos(0.1)\cos(0.2) \approx 0.9950 \times 0.9801 \approx 0.9752$$
> 
> ¡Excelente aproximación! Error ≈ 0.0002

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre la Diferencial
> 
> ✅ **Definición:**
> 
> - $df = \nabla f \cdot d\mathbf{r}$ es la mejor aproximación lineal al cambio en $f$
> - Generaliza $dy = f'(x)dx$ de una variable
> 
> ✅ **Interpretación:**
> 
> - Representa el cambio infinitesimal en $f$
> - Es exacta para funciones lineales
> - Es aproximada para funciones no lineales
> 
> ✅ **Uso práctico:**
> 
> - Propagación de errores
> - Aproximaciones locales
> - Sensibilidad de sistemas
> 
> ---
> 
> ### Sobre la Hessiana
> 
> ✅ **Definición:**
> 
> - Matriz de segundas derivadas parciales
> - Simétrica (por Teorema de Schwarz)
> - Captura la curvatura de $f$
> 
> ✅ **Clasificación de puntos críticos:**
> 
> - **Definida positiva** → Mínimo local
> - **Definida negativa** → Máximo local
> - **Indefinida** → Punto silla
> - **Semidefinida** → Indeterminado
> 
> ✅ **Criterios prácticos:**
> 
> - **2 variables:** Usar $D = f_{xx}f_{yy} - (f_{xy})^2$
> - **n variables:** Calcular menores principales o valores propios
> 
> ---
> 
> ### Sobre Optimización
> 
> ✅ **Condición necesaria (1er orden):** $$\nabla f(\mathbf{x}^*) = \mathbf{0}$$
> 
> ✅ **Condición suficiente (2do orden):**
> 
> - Examinar la naturaleza de $H_f(\mathbf{x}^*)$
> 
> ✅ **Estrategia general:**
> 
> 1. Encontrar puntos críticos
> 2. Calcular Hessiana
> 3. Clasificar cada punto
> 4. Considerar frontera si existe
> 
> ---
> 
> ### Aplicaciones Importantes
> 
> 📊 **Propagación de errores:** Estimar incertidumbre en mediciones
> 
> 🎯 **Machine Learning:** Optimización de funciones de pérdida
> 
> 🔬 **Física:** Análisis de estabilidad de equilibrios
> 
> 💼 **Economía:** Maximización de utilidad y beneficios
> 
> 🏗️ **Ingeniería:** Diseño óptimo de sistemas

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema conecta con:**
> 
> - **Derivadas Parciales** → Base fundamental para diferencial y Hessiana
> - **Gradiente** → Primera parte de la diferencial: $df = \nabla f \cdot d\mathbf{r}$
> - **Aproximación de Taylor** → La diferencial es el término de primer orden
> - **Optimización** → La Hessiana clasifica puntos críticos
> - **Multiplicadores de Lagrange** → Extenderemos estas ideas con restricciones
> - **Ecuaciones Diferenciales** → La Hessiana aparece en estabilidad de sistemas
> - **Álgebra Lineal** → Valores propios, formas cuadrá ticas, matrices simétricas
> - **Análisis Numérico** → Métodos iterativos usan gradiente y Hessiana
> 
> **Prerrequisitos:**
> 
> - Derivadas parciales de primer y segundo orden
> - Gradiente y derivadas direccionales
> - Conocimientos básicos de álgebra lineal (determinantes, valores propios)
> 
> **Siguiente paso natural:**
> 
> - [[Multiplicadores de Lagrange]] → Optimización con restricciones
> - [[Campos Vectoriales]] → Generalización a funciones vectoriales

---

## 📝 Formulario de Referencia Rápida

> [!note]- 📋 Fórmulas Importantes
> 
> ### Diferencial
> 
> **Dos variables:** $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$
> 
> **Tres variables:** $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz$$
> 
> **Forma vectorial:** $$df = \nabla f \cdot d\mathbf{r}$$
> 
> ---
> 
> ### Matriz Hessiana
> 
> **Dos variables:** $$H_f = \begin{bmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{bmatrix}$$
> 
> **Determinante:** $$D = \det(H) = f_{xx}f_{yy} - (f_{xy})^2$$
> 
> ---
> 
> ### Criterio de Clasificación (2D)
> 
> En punto crítico $(x_0, y_0)$:
> 
> - $D > 0$ y $f_{xx} > 0$ → **Mínimo**
> - $D > 0$ y $f_{xx} < 0$ → **Máximo**
> - $D < 0$ → **Punto silla**
> - $D = 0$ → **Indeterminado**
> 
> ---
> 
> ### Aproximación de Taylor (2do orden)
> 
> $$f(\mathbf{x}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot (\mathbf{x}-\mathbf{a})$$ $$+ \frac{1}{2}(\mathbf{x}-\mathbf{a})^T H_f(\mathbf{a})(\mathbf{x}-\mathbf{a})$$
> 
> **Para dos variables:** $$f(x,y) \approx f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$ $$+ \frac{1}{2}[f_{xx}(x-a)^2 + 2f_{xy}(x-a)(y-b) + f_{yy}(y-b)^2]$$
> 
> ---
> 
> ### Propagación de Errores
> 
> Si $z = f(x,y)$ con errores $\Delta x$ y $\Delta y$: $$\Delta z \approx \left|\frac{\partial f}{\partial x}\right|\Delta x + \left|\frac{\partial f}{\partial y}\right|\Delta y$$
> 
> **Error relativo:** $$\frac{\Delta z}{z} \approx \frac{x}{z}\left|\frac{\partial f}{\partial x}\right|\frac{\Delta x}{x} + \frac{y}{z}\left|\frac{\partial f}{\partial y}\right|\frac{\Delta y}{y}$$

---

## 💭 Reflexiones Finales

> [!note]- 🎯 Para Profundizar
> 
> ### Importancia Conceptual
> 
> La diferencial y la Hessiana son **herramientas fundamentales** que permiten:
> 
> 1. **Linearizar** problemas no lineales localmente
> 2. **Analizar curvatura** en múltiples dimensiones
> 3. **Clasificar** comportamiento local de funciones
> 4. **Optimizar** sistemas complejos
> 
> ---
> 
> ### Conexión con la Intuición
> 
> **La diferencial** responde: "Si me muevo un poquito, ¿cuánto cambia la función?"
> 
> **La Hessiana** responde: "¿En qué direcciones la función se curva hacia arriba o hacia abajo?"
> 
> ---
> 
> ### Limitaciones
> 
> ⚠️ **La diferencial es solo una aproximación de primer orden:**
> 
> - Buena cerca del punto
> - Empeora al alejarse
> - No captura curvatura
> 
> ⚠️ **La Hessiana solo da información local:**
> 
> - Un mínimo local puede no ser global
> - Puntos críticos pueden no ser extremos
> - Se necesita análisis global del dominio
> 
> ---
> 
> ### Extensiones Avanzadas
> 
> **Temas relacionados para explorar:**
> 
> - **Optimización convexa:** Cuando $H$ es siempre definida positiva
> - **Análisis de sensibilidad:** Cómo cambios en parámetros afectan óptimos
> - **Métodos numéricos:** Algoritmos que usan gradiente y Hessiana
> - **Geometría diferencial:** Curvatura de variedades
> - **Cálculo variacional:** Optimización de funcionales
> - **Control óptimo:** Minimizar funciones en espacios funcionales
> 
> ---
> 
> ### Para Dominar el Tema
> 
> 1. **Practica cálculo manual** de diferenciales y Hessianas
> 2. **Visualiza** curvas de nivel y superficies
> 3. **Resuelve problemas aplicados** de optimización
> 4. **Verifica resultados** numéricamente cuando sea posible
> 5. **Conecta** con aplicaciones en tu área de interés

---

## 🎨 Ejemplo Integrador Completo

> [!example]- 🌟 Problema Completo: Análisis Exhaustivo
> 
> **Función:** $$f(x,y) = x^3 - 3x + y^2 - 2y$$
> 
> Realizar un **análisis completo**: diferencial, Hessiana, puntos críticos, clasificación y gráfico conceptual.
> 
> ---
> 
> ### Paso 1: Dominio y Continuidad
> 
> - Dominio: $\mathbb{R}^2$ (toda función polinomial)
> - Continua y suave ($C^\infty$)
> 
> ---
> 
> ### Paso 2: Diferencial
> 
> **Derivadas de primer orden:** $$f_x = 3x^2 - 3$$ $$f_y = 2y - 2$$
> 
> **Diferencial:** $$\boxed{df = (3x^2 - 3)dx + (2y - 2)dy}$$
> 
> **En** $(2, 3)$: $$df\big|_{(2,3)} = (12 - 3)dx + (6 - 2)dy = 9dx + 4dy$$
> 
> ---
> 
> ### Paso 3: Puntos Críticos
> 
> $$f_x = 3x^2 - 3 = 0 \implies x^2 = 1 \implies x = \pm 1$$ $$f_y = 2y - 2 = 0 \implies y = 1$$
> 
> **Puntos críticos:** $(1, 1)$ y $(-1, 1)$
> 
> ---
> 
> ### Paso 4: Hessiana
> 
> **Segundas derivadas:** $$f_{xx} = 6x, \quad f_{yy} = 2, \quad f_{xy} = 0$$
> 
> $$H = \begin{bmatrix} 6x & 0 \ 0 & 2 \end{bmatrix}$$
> 
> ---
> 
> ### Paso 5: Clasificación
> 
> **En** $(1, 1)$: $$H(1,1) = \begin{bmatrix} 6 & 0 \ 0 & 2 \end{bmatrix}$$ $$D = 12 > 0, \quad f_{xx} = 6 > 0$$
> 
> $$\boxed{\text{Mínimo local en } (1, 1)}$$
> 
> Valor: $f(1,1) = 1 - 3 + 1 - 2 = -3$
> 
> ---
> 
> **En** $(-1, 1)$: $$H(-1,1) = \begin{bmatrix} -6 & 0 \ 0 & 2 \end{bmatrix}$$ $$D = -12 < 0$$
> 
> $$\boxed{\text{Punto silla en } (-1, 1)}$$
> 
> Valor: $f(-1,1) = -1 + 3 + 1 - 2 = 1$
> 
> ---
> 
> ### Paso 6: Aproximación de Taylor en (1,1)
> 
> $$f(x,y) \approx f(1,1) + 0 \cdot (x-1) + 0 \cdot (y-1)$$ $$+ \frac{1}{2}[6(x-1)^2 + 0 + 2(y-1)^2]$$
> 
> $$\boxed{f(x,y) \approx -3 + 3(x-1)^2 + (y-1)^2}$$
> 
> Esta es la ecuación de un **paraboloide elíptico** con vértice en $(1, 1, -3)$.
> 
> ---
> 
> ### Paso 7: Comportamiento Global
> 
> **Cuando** $|x| \to \infty$ o $|y| \to \infty$:
> 
> - El término dominante es $x^3$ (para $x \to +\infty$) o $y^2$ (para $|y| \to \infty$)
> - $f \to +\infty$ cuando $x \to +\infty$
> - $f \to -\infty$ cuando $x \to -\infty$
> 
> **Conclusión:**
> 
> - El mínimo local en $(1, 1)$ es también un **mínimo global en dirección $y$**
> - No hay mínimo global absoluto (la función es ilimitada inferiormente)
> - No hay máximo global
> 
> ---
> 
> ### Paso 8: Visualización Conceptual
> 
> **Curvas de nivel cerca de los puntos críticos:**
> 
> ```
>       y
>       │
>     3 │
>       │
>     2 │
>       │
>     1 │    ●─────●     ● Punto silla (-1,1)
>       │  silla  mín     ● Mínimo (1,1)
>     0 │
>       │
>    -1 │
>       └────┴────┴────┴──── x
>          -2   -1    0    1    2
> ```
> 
> **Comportamiento:**
> 
> - En $(-1, 1)$: las curvas de nivel forman hipérbolas (silla)
> - En $(1, 1)$: las curvas de nivel son elipses cerradas (mínimo)

---

## 📚 Referencias y Lectura Adicional

> [!note]- 📖 Para Seguir Aprendiendo
> 
> ### Libros Recomendados
> 
> 1. **Stewart, James** - "Cálculo: Varias Variables"
>     - Excelente para fundamentos y visualización
>     - Muchos ejemplos aplicados
> 2. **Marsden & Tromba** - "Vector Calculus"
>     - Enfoque más riguroso
>     - Buena conexión con física
> 3. **Boyd & Vandenberghe** - "Convex Optimization"
>     - Aplicaciones en optimización
>     - Muy usado en machine learning
> 4. **Spivak, Michael** - "Calculus on Manifolds"
>     - Tratamiento riguroso y avanzado
>     - Para los matemáticamente inclinados
> 
> ---
> 
> ### Recursos en Línea
> 
> - **Khan Academy:** Videos introductorios
> - **MIT OpenCourseWare:** Curso completo de cálculo multivariable
> - **3Blue1Brown:** Visualizaciones excelentes
> - **Wolfram MathWorld:** Referencia técnica
> 
> ---
> 
> ### Software para Visualización
> 
> - **GeoGebra:** Gratuito, excelente para 3D
> - **MATLAB/Octave:** Para cálculos numéricos
> - **Python (matplotlib, numpy):** Programación científica
> - **Mathematica/Maple:** Cálculo simbólico

---

**Tags:** #calculo-multivariable #diferencial #hessiana #optimizacion #aproximacion-taylor #puntos-criticos #propagacion-errores #machine-learning #segunda-derivada #curvatura #analisis-multivariable
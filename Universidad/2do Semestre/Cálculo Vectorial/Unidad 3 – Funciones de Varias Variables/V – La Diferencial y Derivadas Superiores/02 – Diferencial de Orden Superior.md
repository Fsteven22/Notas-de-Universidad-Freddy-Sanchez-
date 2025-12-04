# 📘 Derivadas de Orden Superior y Diferenciales

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Derivadas de Orden Superior?
> 
> Las derivadas de orden superior nos permiten analizar cómo cambia la **tasa de cambio** de una función, proporcionando información sobre:
> 
> **Importancia práctica:**
> 
> - **Física:** Aceleración (segunda derivada de posición), jerk (tercera derivada)
> - **Economía:** Tasa de cambio de la tasa marginal
> - **Ingeniería:** Análisis de vibraciones, flexión de vigas
> - **Optimización:** Criterio de la segunda derivada para clasificar puntos críticos
> 
> **Diferencia con una variable:**
> 
> - En $f(x)$: solo una segunda derivada $f''(x)$
> - En $f(x,y)$: **tres** derivadas de segundo orden posibles
> - En $f(x,y,z)$: **seis** derivadas de segundo orden posibles
> 
> **Nueva complejidad:** En varias variables, podemos derivar con respecto a **diferentes variables en diferentes órdenes**, lo que introduce el concepto de **derivadas mixtas**.

---

## 📐 Notación y Definiciones

### 📝 Notación para Derivadas Parciales

> [!example]- 🟢 Sistemas de Notación
> 
> Para una función $f(x,y)$, existen varias notaciones equivalentes:
> 
> ### Primera Derivada
> 
> **Con respecto a $x$:** $$\frac{\partial f}{\partial x} = f_x = \partial_x f = D_x f = f_1$$
> 
> **Con respecto a $y$:** $$\frac{\partial f}{\partial y} = f_y = \partial_y f = D_y f = f_2$$
> 
> ---
> 
> ### Segunda Derivada (Puras)
> 
> **Derivar dos veces con respecto a $x$:** $$\frac{\partial^2 f}{\partial x^2} = f_{xx} = \partial_{xx} f = D_{xx} f = f_{11}$$
> 
> **Derivar dos veces con respecto a $y$:** $$\frac{\partial^2 f}{\partial y^2} = f_{yy} = \partial_{yy} f = D_{yy} f = f_{22}$$
> 
> ---
> 
> ### Segunda Derivada (Mixtas)
> 
> **Derivar primero con respecto a $x$, luego con respecto a $y$:** $$\frac{\partial^2 f}{\partial y \partial x} = f_{xy} = \partial_{xy} f = D_{xy} f = f_{12}$$
> 
> **Derivar primero con respecto a $y$, luego con respecto a $x$:** $$\frac{\partial^2 f}{\partial x \partial y} = f_{yx} = \partial_{yx} f = D_{yx} f = f_{21}$$
> 
> ---
> 
> ### ⚠️ Importante: Orden de Derivación
> 
> En la notación de Leibniz $\frac{\partial^2 f}{\partial y \partial x}$:
> 
> - Se lee de **derecha a izquierda**: primero $\partial x$, luego $\partial y$
> - Es equivalente a $(f_x)_y$
> 
> En la notación de subíndices $f_{xy}$:
> 
> - Se lee de **izquierda a derecha**: primero $x$, luego $y$
> 
> **Regla mnemotécnica:**
> 
> - Leibniz: derecha → izquierda
> - Subíndices: izquierda → derecha

---

## 🔢 Derivadas de Segundo Orden

### 📊 Las Cuatro Derivadas Segundas

> [!example]- 🟡 Clasificación Completa
> 
> Para $f(x,y)$, existen **cuatro** derivadas de segundo orden:
> 
> ### 1. Derivada Segunda Pura en $x$
> 
> $$f_{xx} = \frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right)$$
> 
> **Interpretación:** Mide cómo cambia la pendiente en dirección $x$ cuando nos movemos en dirección $x$.
> 
> **Analogía:** Si $f$ es altura, $f_x$ es inclinación hacia el este, $f_{xx}$ es "qué tan rápido aumenta esa inclinación".
> 
> ---
> 
> ### 2. Derivada Segunda Pura en $y$
> 
> $$f_{yy} = \frac{\partial^2 f}{\partial y^2} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$$
> 
> **Interpretación:** Mide cómo cambia la pendiente en dirección $y$ cuando nos movemos en dirección $y$.
> 
> ---
> 
> ### 3. Derivada Mixta $f_{xy}$
> 
> $$f_{xy} = \frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$$
> 
> **Interpretación:** Primero derivamos respecto a $x$, luego respecto a $y$.
> 
> Mide cómo cambia la pendiente en dirección $x$ cuando nos movemos en dirección $y$.
> 
> ---
> 
> ### 4. Derivada Mixta $f_{yx}$
> 
> $$f_{yx} = \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$$
> 
> **Interpretación:** Primero derivamos respecto a $y$, luego respecto a $x$.
> 
> Mide cómo cambia la pendiente en dirección $y$ cuando nos movemos en dirección $x$.
> 
> ---
> 
> ### 📋 Resumen Visual
> 
> ```
> f(x,y)
>    ↓
>    ├─→ ∂/∂x → f_x ─→ ∂/∂x → f_{xx}
>    │              └─→ ∂/∂y → f_{xy}
>    │
>    └─→ ∂/∂y → f_y ─→ ∂/∂x → f_{yx}
>                   └─→ ∂/∂y → f_{yy}
> ```

---

## 🌟 Teorema de Schwarz (Clairaut)

### 🎯 Teorema Fundamental

> [!note]- 🟢 Teorema de Igualdad de Derivadas Mixtas
> 
> **Enunciado:** Sea $f: D \subseteq \mathbb{R}^2 \to \mathbb{R}$ una función. Si las derivadas parciales mixtas $f_{xy}$ y $f_{yx}$ son **continuas** en un punto $(a,b)$, entonces:
> 
> $$f_{xy}(a,b) = f_{yx}(a,b)$$
> 
> **En otras palabras:** El orden de derivación **no importa** si las derivadas mixtas son continuas.
> 
> ---
> 
> ### Condiciones del Teorema
> 
> **Hipótesis necesarias:**
> 
> 1. ✅ Las derivadas parciales $f_x$ y $f_y$ existen en un entorno de $(a,b)$
> 2. ✅ Las derivadas segundas $f_{xy}$ y $f_{yx}$ existen en un entorno de $(a,b)$
> 3. ✅ Las derivadas $f_{xy}$ y $f_{yx}$ son **continuas** en $(a,b)$
> 
> **Nota importante:** La continuidad de las derivadas mixtas es **suficiente** pero no **necesaria**. Puede haber casos donde $f_{xy} = f_{yx}$ sin que sean continuas.
> 
> ---
> 
> ### Consecuencias Prácticas
> 
> **Para funciones "suaves" (polinomios, exponenciales, trigonométricas, etc.):**
> 
> $$f_{xy} = f_{yx} \quad \text{siempre}$$
> 
> Esto **simplifica enormemente** los cálculos, ya que:
> 
> - Podemos derivar en el orden que sea más conveniente
> - Solo necesitamos calcular 3 (no 4) derivadas segundas distintas
> 
> ---
> 
> ### Ejemplo Visual
> 
> ```
> Para f(x,y) = x²y³:
> 
> Camino 1: f → f_x → f_{xy}
>           f → 2xy³ → 6xy²
> 
> Camino 2: f → f_y → f_{yx}
>           f → 3x²y² → 6xy²
> 
> Resultado: f_{xy} = f_{yx} = 6xy² ✓
> ```

---

## 📚 Ejemplos Detallados de Derivadas Segundas

### Ejemplo 1: Polinomio Simple

> [!example]- 📝 Ejemplo 1: Función Polinomial
> 
> **Función:** $$f(x,y) = x^3 + 2x^2y + 3xy^2 + y^3$$
> 
> ### Derivadas Primeras
> 
> $$f_x = 3x^2 + 4xy + 3y^2$$ $$f_y = 2x^2 + 6xy + 3y^2$$
> 
> ---
> 
> ### Derivadas Segundas Puras
> 
> $$f_{xx} = \frac{\partial}{\partial x}(3x^2 + 4xy + 3y^2) = 6x + 4y$$
> 
> $$f_{yy} = \frac{\partial}{\partial y}(2x^2 + 6xy + 3y^2) = 6x + 6y$$
> 
> ---
> 
> ### Derivadas Mixtas
> 
> **Primera forma ($f_{xy}$):** $$f_{xy} = \frac{\partial}{\partial y}(3x^2 + 4xy + 3y^2) = 4x + 6y$$
> 
> **Segunda forma ($f_{yx}$):** $$f_{yx} = \frac{\partial}{\partial x}(2x^2 + 6xy + 3y^2) = 4x + 6y$$
> 
> ---
> 
> ### Verificación del Teorema de Schwarz
> 
> $$f_{xy} = 4x + 6y = f_{yx} \quad ✓$$
> 
> Las derivadas mixtas son iguales, como predice el teorema (son continuas).
> 
> ---
> 
> ### Evaluación en un Punto
> 
> En $(1, 2)$:
> 
> - $f_{xx}(1,2) = 6(1) + 4(2) = 14$
> - $f_{yy}(1,2) = 6(1) + 6(2) = 18$
> - $f_{xy}(1,2) = 4(1) + 6(2) = 16$

### Ejemplo 2: Función Exponencial

> [!example]- 📝 Ejemplo 2: Exponencial Compuesta
> 
> **Función:** $$f(x,y) = e^{x^2+y^2}$$
> 
> ### Derivadas Primeras
> 
> Por regla de la cadena:
> 
> $$f_x = e^{x^2+y^2} \cdot 2x = 2xe^{x^2+y^2}$$
> 
> $$f_y = e^{x^2+y^2} \cdot 2y = 2ye^{x^2+y^2}$$
> 
> ---
> 
> ### Derivadas Segundas Puras
> 
> **Para $f_{xx}$:** $$f_{xx} = \frac{\partial}{\partial x}(2xe^{x^2+y^2})$$
> 
> Usando regla del producto: $$f_{xx} = 2e^{x^2+y^2} + 2x \cdot 2xe^{x^2+y^2}$$ $$f_{xx} = 2e^{x^2+y^2}(1 + 2x^2)$$
> 
> **Para $f_{yy}$:** $$f_{yy} = 2e^{x^2+y^2}(1 + 2y^2)$$
> 
> ---
> 
> ### Derivada Mixta
> 
> $$f_{xy} = \frac{\partial}{\partial y}(2xe^{x^2+y^2})$$ $$f_{xy} = 2x \cdot 2ye^{x^2+y^2}$$ $$f_{xy} = 4xye^{x^2+y^2}$$
> 
> Por simetría: $f_{yx} = 4xye^{x^2+y^2}$ ✓
> 
> ---
> 
> ### En el origen $(0,0)$:
> 
> - $f_{xx}(0,0) = 2e^0(1 + 0) = 2$
> - $f_{yy}(0,0) = 2e^0(1 + 0) = 2$
> - $f_{xy}(0,0) = 4(0)(0)e^0 = 0$

### Ejemplo 3: Función Trigonométrica

> [!example]- 📝 Ejemplo 3: Función Seno-Coseno
> 
> **Función:** $$f(x,y) = \sin(x)\cos(y)$$
> 
> ### Derivadas Primeras
> 
> $$f_x = \cos(x)\cos(y)$$ $$f_y = -\sin(x)\sin(y)$$
> 
> ---
> 
> ### Derivadas Segundas Puras
> 
> $$f_{xx} = -\sin(x)\cos(y)$$ $$f_{yy} = -\sin(x)\cos(y)$$
> 
> **Observación:** $f_{xx} = f_{yy}$ para esta función particular.
> 
> ---
> 
> ### Derivada Mixta
> 
> $$f_{xy} = \frac{\partial}{\partial y}(\cos(x)\cos(y)) = -\cos(x)\sin(y)$$
> 
> $$f_{yx} = \frac{\partial}{\partial x}(-\sin(x)\sin(y)) = -\cos(x)\sin(y)$$
> 
> $$f_{xy} = f_{yx} \quad ✓$$
> 
> ---
> 
> ### En $(\pi/4, \pi/4)$:
> 
> - $f_{xx}(\pi/4, \pi/4) = -\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2}}{2} = -\frac{1}{2}$
> - $f_{yy}(\pi/4, \pi/4) = -\frac{1}{2}$
> - $f_{xy}(\pi/4, \pi/4) = -\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{2}}{2} = -\frac{1}{2}$

### Ejemplo 4: Función Racional

> [!example]- 📝 Ejemplo 4: Cociente de Polinomios
> 
> **Función:** $$f(x,y) = \frac{xy}{x^2 + y^2}$$
> 
> **Dominio:** $(x,y) \neq (0,0)$
> 
> ### Derivadas Primeras
> 
> Usando regla del cociente:
> 
> $$f_x = \frac{y(x^2+y^2) - xy(2x)}{(x^2+y^2)^2} = \frac{y^3 - x^2y}{(x^2+y^2)^2}$$
> 
> $$f_y = \frac{x(x^2+y^2) - xy(2y)}{(x^2+y^2)^2} = \frac{x^3 - xy^2}{(x^2+y^2)^2}$$
> 
> ---
> 
> ### Simplificación
> 
> $$f_x = \frac{y(y^2-x^2)}{(x^2+y^2)^2}$$
> 
> $$f_y = \frac{x(x^2-y^2)}{(x^2+y^2)^2}$$
> 
> ---
> 
> ### Derivada Segunda $f_{xx}$
> 
> (Proceso largo usando regla del cociente...)
> 
> $$f_{xx} = \frac{2xy(3x^2-y^2)}{(x^2+y^2)^3}$$
> 
> ---
> 
> ### Derivada Mixta $f_{xy}$
> 
> $$f_{xy} = \frac{(y^2-x^2)(y^2-x^2) - 2y \cdot y \cdot 2(x^2+y^2)}{(x^2+y^2)^3}$$
> 
> Simplificando:
> 
> $$f_{xy} = \frac{x^4 - 6x^2y^2 + y^4}{(x^2+y^2)^3}$$
> 
> Por simetría de la función original, $f_{yx} = f_{xy}$ ✓

### Ejemplo 5: Logaritmo

> [!example]- 📝 Ejemplo 5: Función Logarítmica
> 
> **Función:** $$f(x,y) = \ln(x^2 + y^2)$$
> 
> **Dominio:** $x^2 + y^2 > 0$ (excluyendo el origen)
> 
> ### Derivadas Primeras
> 
> $$f_x = \frac{2x}{x^2+y^2}$$
> 
> $$f_y = \frac{2y}{x^2+y^2}$$
> 
> ---
> 
> ### Derivadas Segundas Puras
> 
> **Para $f_{xx}$:** $$f_{xx} = \frac{2(x^2+y^2) - 2x(2x)}{(x^2+y^2)^2}$$ $$f_{xx} = \frac{2y^2 - 2x^2}{(x^2+y^2)^2}$$
> 
> **Para $f_{yy}$:** $$f_{yy} = \frac{2x^2 - 2y^2}{(x^2+y^2)^2}$$
> 
> ---
> 
> ### Derivada Mixta
> 
> $$f_{xy} = \frac{\partial}{\partial y}\left(\frac{2x}{x^2+y^2}\right)$$ $$f_{xy} = \frac{0 - 2x(2y)}{(x^2+y^2)^2}$$ $$f_{xy} = \frac{-4xy}{(x^2+y^2)^2}$$
> 
> Por simetría: $f_{yx} = f_{xy}$ ✓
> 
> ---
> 
> ### Propiedad Notable: Ecuación de Laplace
> 
> $$f_{xx} + f_{yy} = \frac{2y^2-2x^2}{(x^2+y^2)^2} + \frac{2x^2-2y^2}{(x^2+y^2)^2} = 0$$
> 
> Esta función satisface la **ecuación de Laplace**: $\nabla^2 f = 0$ (función armónica).

---

## 🔍 Contraejemplo: Derivadas Mixtas NO Iguales

### ⚠️ Cuando Falla el Teorema de Schwarz

> [!warning]- 🔴 Ejemplo Patológico
> 
> **Función:** $$f(x,y) = \begin{cases} \frac{xy(x^2-y^2)}{x^2+y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> ### Análisis en el Origen
> 
> **Derivada $f_x(0,0)$:** $$f_x(0,0) = \lim_{h \to 0} \frac{f(h,0) - f(0,0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$$
> 
> **Derivada $f_y(0,0)$:** $$f_y(0,0) = \lim_{k \to 0} \frac{f(0,k) - f(0,0)}{k} = \lim_{k \to 0} \frac{0 - 0}{k} = 0$$
> 
> ---
> 
> ### Derivadas Mixtas en el Origen
> 
> **Calculando $f_{xy}(0,0)$:** $$f_{xy}(0,0) = \lim_{k \to 0} \frac{f_x(0,k) - f_x(0,0)}{k}$$
> 
> Primero necesitamos $f_x(0,k)$ para $k \neq 0$: $$f_x(x,y) = \frac{y(x^4+4x^2y^2-y^4)}{(x^2+y^2)^2}$$
> 
> En $(0,k)$: $$f_x(0,k) = \frac{k(-k^4)}{k^4} = -k$$
> 
> Por lo tanto: $$f_{xy}(0,0) = \lim_{k \to 0} \frac{-k - 0}{k} = -1$$
> 
> ---
> 
> **Calculando $f_{yx}(0,0)$:**
> 
> Por simetría del análisis: $$f_{yx}(0,0) = 1$$
> 
> ---
> 
> ### Conclusión
> 
> $$f_{xy}(0,0) = -1 \neq 1 = f_{yx}(0,0)$$
> 
> **¿Por qué falla el teorema?**
> 
> Aunque las derivadas mixtas **existen** en el origen, **NO son continuas** allí. Por lo tanto, no se cumplen las hipótesis del Teorema de Schwarz.
> 
> **Lección:** La continuidad de las derivadas mixtas es **esencial** para garantizar su igualdad.

---

## 🎨 Interpretación Geométrica

### 🗺️ Significado de las Derivadas Segundas

> [!note]- 🎯 Visualización Geométrica
> 
> ### Derivada Segunda Pura: Curvatura
> 
> **$f_{xx}(a,b)$** mide la **curvatura** de la superficie en el punto $(a,b)$ en la dirección del eje $x$.
> 
> ```
> Vista desde arriba (dirección y constante):
> 
> f_{xx} > 0:  Cóncava hacia arriba
>       z
>       |
>       |   ∪      ← Parábola hacia arriba
>       |
>       +-------- x
> 
> f_{xx} < 0:  Cóncava hacia abajo
>       z
>       |   ∩      ← Parábola hacia abajo
>       |
>       +-------- x
> 
> f_{xx} = 0:  Sin curvatura (plano o punto de inflexión)
>       z
>       |   ___    ← Línea recta
>       |
>       +-------- x
> ```
> 
> ---
> 
> ### Derivada Mixta: Torsión
> 
> **$f_{xy}(a,b)$** mide la **torsión** de la superficie: cómo cambia la pendiente en dirección $x$ cuando nos movemos en dirección $y$.
> 
> ```
> f_{xy} > 0:  Superficie tipo "silla de montar" con torsión positiva
> 
> Vista 3D:
>       z
>       |    ╱╲
>       |   ╱  ╲
>       |  ╱    ╲   ← Los gradientes se tuercen
>       | ╱______╲
>       +----------y
>      ╱
>     x
> 
> f_{xy} < 0:  Torsión opuesta
> 
> f_{xy} = 0:  Sin torsión (ejes principales alineados)
> ```
> 
> ---
> 
> ### Ejemplo: Paraboloide Elíptico
> 
> $$f(x,y) = x^2 + 2y^2$$
> 
> - $f_{xx} = 2 > 0$ → curvatura positiva en $x$
> - $f_{yy} = 4 > 0$ → curvatura positiva en $y$ (más pronunciada)
> - $f_{xy} = 0$ → sin torsión
> 
> ```
> Superficie:
>       z
>       |    ╱╲
>       |   ╱  ╲
>       |  │    │   ← Cuenco sin torsión
>       | ╱      ╲
>       +----------y
>      ╱
>     x
> ```
> 
> ---
> 
> ### Ejemplo: Silla de Montar
> 
> $$f(x,y) = x^2 - y^2$$
> 
> - $f_{xx} = 2 > 0$ → curvatura positiva en $x$
> - $f_{yy} = -2 < 0$ → curvatura negativa en $y$
> - $f_{xy} = 0$ → sin torsión adicional
> 
> ```
> Superficie:
>       z
>       |  ╲  ╱
>       |   ╲╱     ← Silla: cóncava en una dirección,
>       |   ╱╲        convexa en la otra
>       |  ╱  ╲
>       +----------y
>      ╱
>     x
> ```

---

## 🔢 Derivadas de Orden Superior (n ≥ 3)

### 📊 Derivadas Terceras

> [!example]- 🟡 Terceras Derivadas
> 
> Para $f(x,y)$, existen **8 derivadas terceras** posibles:
> 
> ### Puras (2 derivadas)
> 
> 1. $f_{xxx} = \frac{\partial^3 f}{\partial x^3}$ - tres veces respecto a $x$
> 2. $f_{yyy} = \frac{\partial^3 f}{\partial y^3}$ - tres veces respecto a $y$
> 
> ---
> 
> ### Mixtas (6 derivadas)
> 
> 3. $f_{xxy} = \frac{\partial^3 f}{\partial y \partial x^2}$ - dos veces $x$, una vez $y$
> 4. $f_{xyx} = \frac{\partial^3 f}{\partial x \partial y \partial x}$
> 5. $f_{yxx} = \frac{\partial^3 f}{\partial x^2 \partial y}$
> 6. $f_{xyy} = \frac{\partial^3 f}{\partial y^2 \partial x}$ - una vez $x$, dos veces $y$
> 7. $f_{yxy} = \frac{\partial^3 f}{\partial y \partial x \partial y}$
> 8. $f_{yyx} = \frac{\partial^3 f}{\partial x \partial y^2}$
> 
> ---
> 
> ### Teorema de Schwarz Generalizado
> 
> Si todas las derivadas parciales hasta orden $n$ son **continuas**, entonces el orden de derivación **no importa**.
> 
> Por ejemplo: $$f_{xxy} = f_{xyx} = f_{yxx}$$
> 
> Esto reduce las 8 terceras derivadas a solo **4 distintas**:
> 
> - $f_{xxx}$
> - $f_{yyy}$
> - $f_{xxy}$ (que también es $f_{xyx}$ y $f_{yxx}$)
> - $f_{xyy}$ (que también es $f_{yxy}$ y $f_{yyx}$)
> 
> ---
> 
> ### Ejemplo: $f(x,y) = x^4y^3$
> 
> **Derivadas primeras:**
> 
> - $f_x = 4x^3y^3$
> - $f_y = 3x^4y^2$
> 
> **Derivadas segundas:**
> 
> - $f_{xx} = 12x^2y^3$
> - $f_{xy} = 12x^3y^2$
> - $f_{yy} = 6x^4y$
> 
> **Derivadas terceras:**
> 
> - $f_{xxx} = 24xy^3$
> - $f_{xxy} = 36x^2y^2$
> - $f_{xyy} = 24x^3y$
> - $f_{yyy} = 6x^4$
> 
> **Verificación de Schwarz:** $$f_{xxy} = \frac{\partial}{\partial y}(12x^2y^3) = 36x^2y^2$$ $$f_{xyx} = \frac{\partial}{\partial x}(12x^3y^2) = 36x^2y^2$$ $$f_{yxx} = \frac{\partial}{\partial x}(12x^2y^3) = 36x^2y^2$$
> 
> Todas iguales ✓

---

## 📐 Matriz Hessiana

### 🎯 Definición y Propiedades

> [!note]- 🟢 La Matriz Hessiana
> 
> **Definición:** Para una función $f: \mathbb{R}^2 \to \mathbb{R}$, la **matriz Hessiana** (o Hessiano) en un punto $(a,b)$ es la matriz de derivadas segundas:
> 
> $$H_f(a,b) = \begin{bmatrix} f_{xx}(a,b) & f_{xy}(a,b) \ f_{yx}(a,b) & f_{yy}(a,b) \end{bmatrix}$$
> 
> Si se cumple el Teorema de Schwarz ($f_{xy} = f_{yx}$), la matriz es **simétrica**:
> 
> $$H_f(a,b) = \begin{bmatrix} f_{xx}(a,b) & f_{xy}(a,b) \ f_{xy}(a,b) & f_{yy}(a,b) \end{bmatrix}$$
> 
> ---
> 
> ### Determinante de la Hessiana
> 
> $$\det(H_f) = f_{xx}f_{yy} - (f_{xy})^2$$
> 
> Este determinante es **fundamental** para:
> 
> - Clasificar puntos críticos
> - Criterio de la segunda derivada
> - Análisis de curvatura
> 
> ---
> 
> ### Traza de la Hessiana
> 
> $$\text{tr}(H_f) = f_{xx} + f_{yy}$$
> 
> La traza aparece en:
> 
> - Ecuación de Laplace: $\nabla^2 f = \text{tr}(H_f)$
> - Análisis de funciones armónicas
> 
> ---
> 
> ### Para Funciones de Tres Variables
> 
> Para $f(x,y,z)$, la Hessiana es $3 \times 3$:
> 
> $$H_f = \begin{bmatrix} f_{xx} & f_{xy} & f_{xz} \ f_{yx} & f_{yy} & f_{yz} \ f_{zx} & f_{zy} & f_{zz} \end{bmatrix}$$
> 
> ---
> 
> ### Notación Alternativa
> 
> $$H_f = \nabla^2 f = D^2f$$

---

## 📚 Ejemplos con Matriz Hessiana

### Ejemplo 6: Calcular Hessiana de un Polinomio

> [!example]- 📝 Ejemplo 6: Hessiana Explícita
> 
> **Función:** $$f(x,y) = x^3 + y^3 - 3xy$$
> 
> ### Derivadas Primeras
> 
> $$f_x = 3x^2 - 3y$$ $$f_y = 3y^2 - 3x$$
> 
> ---
> 
> ### Derivadas Segundas
> 
> $$f_{xx} = 6x$$ $$f_{yy} = 6y$$ $$f_{xy} = -3$$
> 
> ---
> 
> ### Matriz Hessiana
> 
> $$H_f(x,y) = \begin{bmatrix} 6x & -3 \ -3 & 6y \end{bmatrix}$$
> 
> ---
> 
> ### Evaluación en Puntos Específicos
> 
> **En el origen $(0,0)$:** $$H_f(0,0) = \begin{bmatrix} 0 & -3 \ -3 & 0 \end{bmatrix}$$
> 
> $$\det(H_f(0,0)) = 0 \cdot 0 - (-3)^2 = -9 < 0$$
> 
> ---
> 
> **En el punto $(1,1)$:** $$H_f(1,1) = \begin{bmatrix} 6 & -3 \ -3 & 6 \end{bmatrix}$$
> 
> $$\det(H_f(1,1)) = 6 \cdot 6 - (-3)^2 = 36 - 9 = 27 > 0$$ $$\text{tr}(H_f(1,1)) = 6 + 6 = 12 > 0$$
> 
> Como $\det > 0$ y $\text{tr} > 0$, el punto $(1,1)$ es un **mínimo local** (lo veremos en optimización).

### Ejemplo 7: Hessiana de Función Exponencial

> [!example]- 📝 Ejemplo 7: Función con Exponencial
> 
> **Función:** $$f(x,y) = e^{-(x^2+y^2)}$$
> 
> ### Derivadas Primeras
> 
> $$f_x = -2xe^{-(x^2+y^2)}$$ $$f_y = -2ye^{-(x^2+y^2)}$$
> 
> ---
> 
> ### Derivadas Segundas
> 
> $$f_{xx} = -2e^{-(x^2+y^2)} + 4x^2e^{-(x^2+y^2)} = 2e^{-(x^2+y^2)}(2x^2 - 1)$$
> 
> $$f_{yy} = 2e^{-(x^2+y^2)}(2y^2 - 1)$$
> 
> $$f_{xy} = 4xye^{-(x^2+y^2)}$$
> 
> ---
> 
> ### Matriz Hessiana
> 
> $$H_f(x,y) = 2e^{-(x^2+y^2)} \begin{bmatrix} 2x^2-1 & 2xy \ 2xy & 2y^2-1 \end{bmatrix}$$
> 
> ---
> 
> ### En el Origen $(0,0)$
> 
> $$H_f(0,0) = 2e^0 \begin{bmatrix} -1 & 0 \ 0 & -1 \end{bmatrix} = \begin{bmatrix} -2 & 0 \ 0 & -2 \end{bmatrix}$$
> 
> $$\det(H_f(0,0)) = 4 > 0$$ $$\text{tr}(H_f(0,0)) = -4 < 0$$
> 
> El origen es un **máximo local** de esta función "campana" gaussiana.

### Ejemplo 8: Hessiana de una Silla de Montar

> [!example]- 📝 Ejemplo 8: Punto de Silla
> 
> **Función:** $$f(x,y) = x^2 - y^2$$
> 
> ### Derivadas
> 
> $$f_x = 2x, \quad f_y = -2y$$ $$f_{xx} = 2, \quad f_{yy} = -2, \quad f_{xy} = 0$$
> 
> ---
> 
> ### Matriz Hessiana
> 
> $$H_f = \begin{bmatrix} 2 & 0 \ 0 & -2 \end{bmatrix}$$
> 
> Esta matriz es **constante** en todo punto.
> 
> ---
> 
> ### Análisis
> 
> $$\det(H_f) = 2 \cdot (-2) - 0^2 = -4 < 0$$
> 
> Como el determinante es negativo, **cualquier punto** (en particular el origen) es un **punto de silla** o **punto silla**.
> 
> **Interpretación geométrica:**
> 
> - En dirección $x$: curvatura positiva (cóncava arriba)
> - En dirección $y$: curvatura negativa (cóncava abajo)
> - Superficie con forma de silla de montar

---

## 🎯 Aplicación: Criterio de la Segunda Derivada

### 🔍 Clasificación de Puntos Críticos

> [!tip]- ⭐ Criterio de la Segunda Derivada para Extremos
> 
> Sea $f(x,y)$ una función con derivadas segundas continuas, y sea $(a,b)$ un **punto crítico** (donde $f_x = f_y = 0$).
> 
> Sea $D = \det(H_f(a,b)) = f_{xx}(a,b) \cdot f_{yy}(a,b) - [f_{xy}(a,b)]^2$
> 
> ---
> 
> ### Casos de Clasificación
> 
> **Caso 1: $D > 0$ y $f_{xx}(a,b) > 0$**
> 
> - ✅ $(a,b)$ es un **mínimo local**
> - Ambas curvaturas principales son positivas (cuenco hacia arriba)
> 
> **Caso 2: $D > 0$ y $f_{xx}(a,b) < 0$**
> 
> - ✅ $(a,b)$ es un **máximo local**
> - Ambas curvaturas principales son negativas (cuenco hacia abajo)
> 
> **Caso 3: $D < 0$**
> 
> - ✅ $(a,b)$ es un **punto de silla** (punto silla)
> - Curvaturas de signos opuestos
> 
> **Caso 4: $D = 0$**
> 
> - ❓ El criterio **no decide**
> - Se necesita análisis adicional
> 
> ---
> 
> ### Interpretación del Determinante
> 
> $$D = f_{xx} f_{yy} - (f_{xy})^2$$
> 
> - Si $D > 0$: $f_{xx}$ y $f_{yy}$ tienen el **mismo signo** (después de considerar el término mixto)
> - Si $D < 0$: curvaturas de signos **opuestos**
> 
> ---
> 
> ### Algoritmo de Clasificación
> 
> ```
> 1. Encontrar puntos críticos: resolver f_x = 0, f_y = 0
> 2. Para cada punto crítico (a,b):
>    a) Calcular f_{xx}(a,b), f_{yy}(a,b), f_{xy}(a,b)
>    b) Calcular D = f_{xx}·f_{yy} - (f_{xy})²
>    c) Clasificar según D y f_{xx}:
>       - D > 0, f_{xx} > 0 → MÍNIMO
>       - D > 0, f_{xx} < 0 → MÁXIMO
>       - D < 0 → PUNTO DE SILLA
>       - D = 0 → INDETERMINADO
> ```

---

## 📚 Ejemplos de Clasificación de Puntos Críticos

### Ejemplo 9: Optimización de Polinomio

> [!example]- 📝 Ejemplo 9: Clasificación Completa
> 
> **Función:** $$f(x,y) = x^3 + y^3 - 3xy$$
> 
> ### Paso 1: Encontrar Puntos Críticos
> 
> $$f_x = 3x^2 - 3y = 0 \implies y = x^2$$ $$f_y = 3y^2 - 3x = 0 \implies x = y^2$$
> 
> Sustituyendo $y = x^2$ en $x = y^2$: $$x = (x^2)^2 = x^4$$ $$x^4 - x = 0$$ $$x(x^3 - 1) = 0$$
> 
> Soluciones: $x = 0$ o $x = 1$
> 
> - Si $x = 0$: $y = 0^2 = 0$ → Punto $(0,0)$
> - Si $x = 1$: $y = 1^2 = 1$ → Punto $(1,1)$
> 
> **Puntos críticos:** $(0,0)$ y $(1,1)$
> 
> ---
> 
> ### Paso 2: Calcular la Hessiana
> 
> Del Ejemplo 6, sabemos: $$H_f(x,y) = \begin{bmatrix} 6x & -3 \ -3 & 6y \end{bmatrix}$$
> 
> ---
> 
> ### Paso 3: Clasificar $(0,0)$
> 
> $$H_f(0,0) = \begin{bmatrix} 0 & -3 \ -3 & 0 \end{bmatrix}$$
> 
> $$D = 0 \cdot 0 - (-3)^2 = -9 < 0$$
> 
> **Conclusión:** $(0,0)$ es un **punto de silla** ⚠️
> 
> ---
> 
> ### Paso 4: Clasificar $(1,1)$
> 
> $$H_f(1,1) = \begin{bmatrix} 6 & -3 \ -3 & 6 \end{bmatrix}$$
> 
> $$D = 6 \cdot 6 - (-3)^2 = 36 - 9 = 27 > 0$$ $$f_{xx}(1,1) = 6 > 0$$
> 
> **Conclusión:** $(1,1)$ es un **mínimo local** ✅
> 
> Valor: $f(1,1) = 1 + 1 - 3 = -1$

### Ejemplo 10: Función con Tres Puntos Críticos

> [!example]- 📝 Ejemplo 10: Análisis Completo
> 
> **Función:** $$f(x,y) = x^4 + y^4 - 4xy$$
> 
> ### Encontrar Puntos Críticos
> 
> $$f_x = 4x^3 - 4y = 0 \implies y = x^3$$ $$f_y = 4y^3 - 4x = 0 \implies x = y^3$$
> 
> Sustituyendo: $$x = (x^3)^3 = x^9$$ $$x^9 - x = 0$$ $$x(x^8 - 1) = 0$$
> 
> Soluciones reales: $x = 0, 1, -1$
> 
> **Puntos críticos:**
> 
> - $(0, 0)$
> - $(1, 1)$
> - $(-1, -1)$
> 
> ---
> 
> ### Calcular Hessiana
> 
> $$f_{xx} = 12x^2$$ $$f_{yy} = 12y^2$$ $$f_{xy} = -4$$
> 
> $$H_f(x,y) = \begin{bmatrix} 12x^2 & -4 \ -4 & 12y^2 \end{bmatrix}$$
> 
> ---
> 
> ### Clasificar cada punto
> 
> **En $(0,0)$:** $$H_f(0,0) = \begin{bmatrix} 0 & -4 \ -4 & 0 \end{bmatrix}$$ $$D = 0 \cdot 0 - 16 = -16 < 0$$
> 
> → **Punto de silla** ⚠️
> 
> ---
> 
> **En $(1,1)$:** $$H_f(1,1) = \begin{bmatrix} 12 & -4 \ -4 & 12 \end{bmatrix}$$ $$D = 12 \cdot 12 - 16 = 144 - 16 = 128 > 0$$ $$f_{xx}(1,1) = 12 > 0$$
> 
> → **Mínimo local** ✅
> 
> Valor: $f(1,1) = 1 + 1 - 4 = -2$
> 
> ---
> 
> **En $(-1,-1)$:** $$H_f(-1,-1) = \begin{bmatrix} 12 & -4 \ -4 & 12 \end{bmatrix}$$
> 
> Igual que $(1,1)$: **Mínimo local** ✅
> 
> Valor: $f(-1,-1) = 1 + 1 + 4 = 2$
> 
> ---
> 
> ### Resumen
> 
> |Punto|Tipo|Valor de $f$|
> |---|---|---|
> |$(0,0)$|Punto de silla|$0$|
> |$(1,1)$|Mínimo local|$-2$|
> |$(-1,-1)$|Mínimo local|$2$|
> 
> El **mínimo global** en los tres puntos es $f(1,1) = -2$.

### Ejemplo 11: Caso Indeterminado

> [!example]- 📝 Ejemplo 11: Cuando $D = 0$
> 
> **Función:** $$f(x,y) = x^4 + y^4$$
> 
> ### Punto Crítico
> 
> $$f_x = 4x^3 = 0 \implies x = 0$$ $$f_y = 4y^3 = 0 \implies y = 0$$
> 
> Único punto crítico: $(0,0)$
> 
> ---
> 
> ### Hessiana en el Origen
> 
> $$f_{xx} = 12x^2 \implies f_{xx}(0,0) = 0$$ $$f_{yy} = 12y^2 \implies f_{yy}(0,0) = 0$$ $$f_{xy} = 0$$
> 
> $$H_f(0,0) = \begin{bmatrix} 0 & 0 \ 0 & 0 \end{bmatrix}$$
> 
> $$D = 0 \cdot 0 - 0^2 = 0$$
> 
> ---
> 
> ### Análisis Adicional
> 
> El criterio de la segunda derivada **no decide**.
> 
> Sin embargo, podemos observar: $$f(x,y) = x^4 + y^4 \geq 0$$
> 
> con igualdad solo en $(0,0)$.
> 
> **Conclusión:** $(0,0)$ es un **mínimo global** (no solo local), pero el criterio estándar no lo detecta porque las derivadas segundas se anulan.
> 
> **Lección:** Cuando $D = 0$, se requiere análisis de orden superior o métodos alternativos.

---

## 🔄 Diferenciales de Orden Superior

### 📐 Definición del Diferencial de Segundo Orden

> [!note]- 🟢 Diferencial de Segundo Orden
> 
> **Para funciones de una variable:**
> 
> Si $y = f(x)$, el segundo diferencial es: $$d^2y = f''(x)(dx)^2$$
> 
> ---
> 
> **Para funciones de dos variables:**
> 
> Si $z = f(x,y)$, el **segundo diferencial** es:
> 
> $$d^2f = f_{xx}(dx)^2 + 2f_{xy}(dx)(dy) + f_{yy}(dy)^2$$
> 
> Esta expresión puede escribirse en forma matricial:
> 
> $$d^2f = \begin{bmatrix} dx & dy \end{bmatrix} \begin{bmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{bmatrix} \begin{bmatrix} dx \ dy \end{bmatrix}$$
> 
> $$d^2f = \begin{bmatrix} dx & dy \end{bmatrix} H_f \begin{bmatrix} dx \ dy \end{bmatrix}$$
> 
> ---
> 
> ### Notación de Operador
> 
> Podemos usar la notación de operador diferencial:
> 
> $$d^2f = \left(\frac{\partial}{\partial x}dx + \frac{\partial}{\partial y}dy\right)^2 f$$
> 
> Expandiendo: $$d^2f = \frac{\partial^2 f}{\partial x^2}(dx)^2 + 2\frac{\partial^2 f}{\partial x \partial y}(dx)(dy) + \frac{\partial^2 f}{\partial y^2}(dy)^2$$
> 
> ---
> 
> ### Interpretación
> 
> El segundo diferencial mide la **curvatura** de la función en una dirección arbitraria $(dx, dy)$.
> 
> - Si $d^2f > 0$ para todo $(dx, dy) \neq (0,0)$: función localmente convexa
> - Si $d^2f < 0$ para todo $(dx, dy) \neq (0,0)$: función localmente cóncava

### Ejemplo 12: Calcular Segundo Diferencial

> [!example]- 📝 Ejemplo 12: Diferencial Explícito
> 
> **Función:** $$f(x,y) = x^2y + xy^2$$
> 
> ### Derivadas Segundas
> 
> $$f_{xx} = 2y$$ $$f_{yy} = 2x$$ $$f_{xy} = 2x + 2y$$
> 
> ---
> 
> ### Segundo Diferencial
> 
> $$d^2f = f_{xx}(dx)^2 + 2f_{xy}(dx)(dy) + f_{yy}(dy)^2$$
> 
> $$d^2f = 2y(dx)^2 + 2(2x+2y)(dx)(dy) + 2x(dy)^2$$
> 
> $$d^2f = 2y(dx)^2 + (4x+4y)(dx)(dy) + 2x(dy)^2$$
> 
> ---
> 
> ### En el Punto $(1,1)$
> 
> $$d^2f\big|_{(1,1)} = 2(dx)^2 + 8(dx)(dy) + 2(dy)^2$$
> 
> ---
> 
> ### Análisis de Convexidad
> 
> Para determinar si la función es convexa en $(1,1)$, verificamos si $d^2f > 0$ para todo $(dx, dy) \neq (0,0)$.
> 
> La Hessiana en $(1,1)$: $$H_f(1,1) = \begin{bmatrix} 2 & 4 \ 4 & 2 \end{bmatrix}$$
> 
> Autovalores: $$\det(H - \lambda I) = (2-\lambda)^2 - 16 = 0$$ $$\lambda^2 - 4\lambda - 12 = 0$$ $$\lambda = 6 \text{ o } \lambda = -2$$
> 
> Como hay un autovalor negativo, la función **no es convexa** en $(1,1)$ (el punto es una silla).

---

## 🎨 Formas Cuadráticas y Hessianas

### 🔍 Conexión con Álgebra Lineal

> [!note]- 🎯 Formas Cuadráticas
> 
> **Definición:** Una **forma cuadrática** en $\mathbb{R}^2$ es una expresión de la forma:
> 
> $$Q(h, k) = ah^2 + 2bhk + ck^2$$
> 
> donde $a, b, c$ son constantes.
> 
> ---
> 
> ### Relación con la Hessiana
> 
> El segundo diferencial $d^2f$ en un punto es una forma cuadrática:
> 
> $$d^2f = f_{xx}(dx)^2 + 2f_{xy}(dx)(dy) + f_{yy}(dy)^2$$
> 
> Con matriz asociada: $$A = \begin{bmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{bmatrix} = H_f$$
> 
> ---
> 
> ### Clasificación de Formas Cuadráticas
> 
> Una forma cuadrática (y su matriz asociada) puede ser:
> 
> **1. Definida Positiva:** $Q(h,k) > 0$ para todo $(h,k) \neq (0,0)$
> 
> - Todos los autovalores $> 0$
> - $\det(A) > 0$ y $a > 0$
> - Corresponde a **mínimo local**
> 
> **2. Definida Negativa:** $Q(h,k) < 0$ para todo $(h,k) \neq (0,0)$
> 
> - Todos los autovalores $< 0$
> - $\det(A) > 0$ y $a < 0$
> - Corresponde a **máximo local**
> 
> **3. Indefinida:** $Q$ toma valores positivos y negativos
> 
> - Autovalores de signos opuestos
> - $\det(A) < 0$
> - Corresponde a **punto de silla**
> 
> **4. Semidefinida:** $Q(h,k) \geq 0$ (o $\leq 0$) pero puede ser $0$
> 
> - Al menos un autovalor es $0$
> - $\det(A) = 0$
> - Caso **indeterminado**
> 
> ---
> 
> ### Criterio de Sylvester
> 
> Para determinar el tipo de forma cuadrática usando **menores principales**:
> 
> Para matriz $2 \times 2$: $$A = \begin{bmatrix} a & b \ b & c \end{bmatrix}$$
> 
> - **Definida positiva:** $a > 0$ y $\det(A) > 0$
> - **Definida negativa:** $a < 0$ y $\det(A) > 0$
> - **Indefinida:** $\det(A) < 0$
> - **Semidefinida:** $\det(A) = 0$

---

## 📊 Fórmula de Taylor de Segundo Orden

### 🎯 Aproximación Cuadrática

> [!note]- 🟢 Polinomio de Taylor de Segundo Orden
> 
> **Para funciones de una variable:** $$f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2$$
> 
> ---
> 
> **Para funciones de dos variables:**
> 
> Si $f$ tiene derivadas segundas continuas en un punto $(a,b)$, entonces:
> 
> $$f(x,y) \approx f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$ $$+ \frac{1}{2}[f_{xx}(a,b)(x-a)^2 + 2f_{xy}(a,b)(x-a)(y-b) + f_{yy}(a,b)(y-b)^2]$$
> 
> ---
> 
> ### Notación Compacta
> 
> Sea $\mathbf{x} = (x,y)$, $\mathbf{a} = (a,b)$, $\mathbf{h} = \mathbf{x} - \mathbf{a} = (x-a, y-b)$.
> 
> Entonces: $$f(\mathbf{a} + \mathbf{h}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot \mathbf{h} + \frac{1}{2}\mathbf{h}^T H_f(\mathbf{a}) \mathbf{h}$$
> 
> Donde:
> 
> - $\nabla f(\mathbf{a}) = (f_x(a,b), f_y(a,b))$ es el **gradiente**
> - $H_f(\mathbf{a})$ es la **matriz Hessiana**
> - $\mathbf{h}^T H_f \mathbf{h}$ es el **segundo diferencial**
> 
> ---
> 
> ### Términos de la Aproximación
> 
> **Término de orden cero:** $f(a,b)$ - valor en el punto
> 
> **Término de primer orden:** $f_x(a,b)(x-a) + f_y(a,b)(y-b)$ - aproximación lineal (plano tangente)
> 
> **Término de segundo orden:** $\frac{1}{2}[f_{xx}(x-a)^2 + 2f_{xy}(x-a)(y-b) + f_{yy}(y-b)^2]$ - corrección cuadrática 
> ### Error de la Aproximación
> 
> El **error** (resto de Taylor) es:
> 
> $$R_2(\mathbf{h}) = f(\mathbf{a} + \mathbf{h}) - P_2(\mathbf{h})$$
> 
> donde $P_2$ es el polinomio de Taylor de grado 2.
> 
> Si las derivadas terceras existen y están acotadas, entonces: $$|R_2(\mathbf{h})| \leq M |\mathbf{h}|^3$$
> 
> para alguna constante $M$ y $|\mathbf{h}|$ suficientemente pequeño.

### Ejemplo 13: Aproximación de Taylor

> [!example]- 📝 Ejemplo 13: Aproximación Cuadrática
> 
> **Función:** $$f(x,y) = e^x \cos(y)$$
> 
> **Aproximar cerca del origen** $(0,0)$.
> 
> ---
> 
> ### Paso 1: Valor en el Origen
> 
> $$f(0,0) = e^0 \cos(0) = 1$$
> 
> ---
> 
> ### Paso 2: Derivadas Primeras
> 
> $$f_x = e^x \cos(y) \implies f_x(0,0) = 1$$ $$f_y = -e^x \sin(y) \implies f_y(0,0) = 0$$
> 
> ---
> 
> ### Paso 3: Derivadas Segundas
> 
> $$f_{xx} = e^x \cos(y) \implies f_{xx}(0,0) = 1$$ $$f_{yy} = -e^x \cos(y) \implies f_{yy}(0,0) = -1$$ $$f_{xy} = -e^x \sin(y) \implies f_{xy}(0,0) = 0$$
> 
> ---
> 
> ### Paso 4: Polinomio de Taylor
> 
> $$P_2(x,y) = 1 + 1 \cdot x + 0 \cdot y + \frac{1}{2}[1 \cdot x^2 + 2 \cdot 0 \cdot xy + (-1) \cdot y^2]$$
> 
> $$P_2(x,y) = 1 + x + \frac{1}{2}(x^2 - y^2)$$
> 
> ---
> 
> ### Paso 5: Verificación
> 
> Comparemos valores:
> 
> **En $(0.1, 0.1)$:**
> 
> - Valor exacto: $f(0.1, 0.1) = e^{0.1}\cos(0.1) \approx 1.0998$
> - Aproximación: $P_2(0.1, 0.1) = 1 + 0.1 + \frac{1}{2}(0.01 - 0.01) = 1.1$
> - Error: $\approx 0.0002$
> 
> **En $(0.5, 0)$:**
> 
> - Valor exacto: $f(0.5, 0) = e^{0.5} \approx 1.6487$
> - Aproximación: $P_2(0.5, 0) = 1 + 0.5 + \frac{1}{2}(0.25) = 1.625$
> - Error: $\approx 0.024$

### Ejemplo 14: Aproximación en Punto No Trivial

> [!example]- 📝 Ejemplo 14: Taylor alrededor de $(1,2)$
> 
> **Función:** $$f(x,y) = x^2y + y^2$$
> 
> **Aproximar cerca de** $(1,2)$.
> 
> ---
> 
> ### Cálculos en $(1,2)$
> 
> **Valor:** $$f(1,2) = 1^2 \cdot 2 + 2^2 = 2 + 4 = 6$$
> 
> **Derivadas primeras:** $$f_x = 2xy \implies f_x(1,2) = 4$$ $$f_y = x^2 + 2y \implies f_y(1,2) = 1 + 4 = 5$$
> 
> **Derivadas segundas:** $$f_{xx} = 2y \implies f_{xx}(1,2) = 4$$ $$f_{yy} = 2 \implies f_{yy}(1,2) = 2$$ $$f_{xy} = 2x \implies f_{xy}(1,2) = 2$$
> 
> ---
> 
> ### Polinomio de Taylor
> 
> Sea $h = x - 1$ y $k = y - 2$:
> 
> $$P_2(x,y) = 6 + 4h + 5k + \frac{1}{2}[4h^2 + 2 \cdot 2 \cdot hk + 2k^2]$$
> 
> $$P_2(x,y) = 6 + 4(x-1) + 5(y-2) + 2(x-1)^2 + 2(x-1)(y-2) + (y-2)^2$$
> 
> ---
> 
> ### Simplificación
> 
> Expandiendo: $$P_2(x,y) = 6 + 4x - 4 + 5y - 10 + 2(x^2-2x+1) + 2(xy-2x-y+2) + (y^2-4y+4)$$
> 
> Después de simplificar (esto es tedioso pero directo): $$P_2(x,y) = 2x^2 + 2xy + y^2 - 4x - 4y + 4$$
> 
> **Verificación:** En $(1,2)$: $$P_2(1,2) = 2 + 4 + 4 - 4 - 8 + 4 = 6 = f(1,2)$$ ✓

---

## 🧮 Derivadas de Orden Superior en Tres Variables

### 📐 Extensión a $\mathbb{R}^3$

> [!note]- 🟡 Derivadas Segundas en Tres Variables
> 
> Para $f(x,y,z)$, existen **6 derivadas segundas** (si son continuas):
> 
> ### Derivadas Puras (3)
> 
> 1. $f_{xx} = \frac{\partial^2 f}{\partial x^2}$
> 2. $f_{yy} = \frac{\partial^2 f}{\partial y^2}$
> 3. $f_{zz} = \frac{\partial^2 f}{\partial z^2}$
> 
> ---
> 
> ### Derivadas Mixtas (3, por Schwarz)
> 
> 4. $f_{xy} = f_{yx} = \frac{\partial^2 f}{\partial x \partial y}$
> 5. $f_{xz} = f_{zx} = \frac{\partial^2 f}{\partial x \partial z}$
> 6. $f_{yz} = f_{zy} = \frac{\partial^2 f}{\partial y \partial z}$
> 
> ---
> 
> ### Matriz Hessiana en $\mathbb{R}^3$
> 
> $$H_f = \begin{bmatrix} f_{xx} & f_{xy} & f_{xz} \ f_{xy} & f_{yy} & f_{yz} \ f_{xz} & f_{yz} & f_{zz} \end{bmatrix}$$
> 
> Es una matriz **simétrica** $3 \times 3$.
> 
> ---
> 
> ### Segundo Diferencial
> 
> $$d^2f = f_{xx}(dx)^2 + f_{yy}(dy)^2 + f_{zz}(dz)^2$$ $$+ 2f_{xy}(dx)(dy) + 2f_{xz}(dx)(dz) + 2f_{yz}(dy)(dz)$$
> 
> En forma matricial: $$d^2f = \begin{bmatrix} dx & dy & dz \end{bmatrix} H_f \begin{bmatrix} dx \ dy \ dz \end{bmatrix}$$
> 
> ---
> 
> ### Operador de Laplace (Laplaciano)
> 
> El **Laplaciano** de $f$ es la traza de la Hessiana:
> 
> $$\nabla^2 f = \Delta f = f_{xx} + f_{yy} + f_{zz}$$
> 
> **Funciones armónicas:** Si $\nabla^2 f = 0$, la función es **armónica**.
> 
> ---
> 
> ### Ejemplo: Campo Gravitacional
> 
> El potencial gravitacional en $\mathbb{R}^3$: $$\phi(x,y,z) = -\frac{GM}{\sqrt{x^2+y^2+z^2}}$$
> 
> Es armónico excepto en el origen (satisface $\nabla^2\phi = 0$).

### Ejemplo 15: Función en Tres Variables

> [!example]- 📝 Ejemplo 15: Cálculo en $\mathbb{R}^3$
> 
> **Función:** $$f(x,y,z) = x^2y + y^2z + z^2x$$
> 
> ### Derivadas Primeras
> 
> $$f_x = 2xy + z^2$$ $$f_y = x^2 + 2yz$$ $$f_z = y^2 + 2zx$$
> 
> ---
> 
> ### Derivadas Segundas Puras
> 
> $$f_{xx} = 2y$$ $$f_{yy} = 2z$$ $$f_{zz} = 2x$$
> 
> ---
> 
> ### Derivadas Mixtas
> 
> $$f_{xy} = 2x$$ $$f_{xz} = 2z$$ $$f_{yz} = 2y$$
> 
> ---
> 
> ### Matriz Hessiana
> 
> $$H_f(x,y,z) = \begin{bmatrix} 2y & 2x & 2z \ 2x & 2z & 2y \ 2z & 2y & 2x \end{bmatrix}$$
> 
> ---
> 
> ### En el Punto $(1,1,1)$
> 
> $$H_f(1,1,1) = \begin{bmatrix} 2 & 2 & 2 \ 2 & 2 & 2 \ 2 & 2 & 2 \end{bmatrix}$$
> 
> **Determinante:** $$\det(H_f(1,1,1)) = 0$$
> 
> La matriz es **singular** (no invertible), lo que indica un caso degenerado.
> 
> ---
> 
> ### Laplaciano
> 
> $$\nabla^2 f = f_{xx} + f_{yy} + f_{zz} = 2y + 2z + 2x = 2(x+y+z)$$
> 
> En $(1,1,1)$: $\nabla^2 f = 6 \neq 0$
> 
> Por lo tanto, $f$ **no es armónica**.

---

## 🎯 Aplicaciones Prácticas

### 🔬 Física: Ecuación de Onda

> [!note]- 🌊 Aplicación: Propagación de Ondas
> 
> La **ecuación de onda** en una dimensión espacial:
> 
> $$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$
> 
> donde:
> 
> - $u(x,t)$ es el desplazamiento
> - $c$ es la velocidad de propagación
> 
> ---
> 
> ### En Dos Dimensiones
> 
> Para una membrana vibrante (como un tambor):
> 
> $$\frac{\partial^2 u}{\partial t^2} = c^2\left(\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}\right)$$
> 
> $$\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u$$
> 
> ---
> 
> ### Solución Simple
> 
> Una solución de onda plana: $$u(x,y,t) = A\sin(k_x x + k_y y - \omega t)$$
> 
> Verificación: $$u_{tt} = -\omega^2 A\sin(k_x x + k_y y - \omega t)$$ $$\nabla^2 u = -(k_x^2 + k_y^2)A\sin(k_x x + k_y y - \omega t)$$
> 
> Para que satisfaga la ecuación de onda: $$\omega^2 = c^2(k_x^2 + k_y^2)$$

### 🏗️ Ingeniería: Flexión de Vigas

> [!note]- 🔧 Aplicación: Ecuación de la Viga
> 
> La **deflexión** de una viga está gobernada por:
> 
> $$EI\frac{d^4 w}{dx^4} = q(x)$$
> 
> donde:
> 
> - $w(x)$ es la deflexión
> - $E$ es el módulo de Young
> - $I$ es el momento de inercia
> - $q(x)$ es la carga distribuida
> 
> ---
> 
> ### Para Placas en 2D
> 
> La ecuación biarmónica (de placas):
> 
> $$D\nabla^4 w = q(x,y)$$
> 
> donde: $$\nabla^4 = \nabla^2(\nabla^2) = \frac{\partial^4}{\partial x^4} + 2\frac{\partial^4}{\partial x^2 \partial y^2} + \frac{\partial^4}{\partial y^4}$$
> 
> Esto requiere **derivadas de cuarto orden**.
> 
> ---
> 
> ### Ejemplo: Placa Circular
> 
> Para una placa circular uniforme con carga $q_0$: $$w(r) = \frac{q_0}{64D}(a^2-r^2)^2$$
> 
> donde $a$ es el radio y $r = \sqrt{x^2+y^2}$.

### 📊 Economía: Utilidad y Elasticidad

> [!note]- 💰 Aplicación: Función de Utilidad
> 
> **Función de utilidad:** $U(x,y)$ representa la satisfacción del consumidor al consumir $x$ unidades del bien 1 e $y$ unidades del bien 2.
> 
> ---
> 
> ### Utilidades Marginales
> 
> $$U_x = \frac{\partial U}{\partial x}, \quad U_y = \frac{\partial U}{\partial y}$$
> 
> Miden el beneficio adicional de consumir una unidad más.
> 
> ---
> 
> ### Ley de Utilidad Marginal Decreciente
> 
> $$U_{xx} < 0, \quad U_{yy} < 0$$
> 
> Cada unidad adicional proporciona **menos** satisfacción que la anterior.
> 
> ---
> 
> ### Bienes Complementarios vs. Sustitutos
> 
> **Complementarios:** $U_{xy} > 0$
> 
> - Consumir más de $x$ aumenta la utilidad marginal de $y$
> - Ejemplo: café y azúcar
> 
> **Sustitutos:** $U_{xy} < 0$
> 
> - Consumir más de $x$ disminuye la utilidad marginal de $y$
> - Ejemplo: té y café
> 
> ---
> 
> ### Ejemplo: Función Cobb-Douglas
> 
> $$U(x,y) = x^\alpha y^\beta, \quad \alpha, \beta > 0$$
> 
> **Derivadas:**
> 
> - $U_x = \alpha x^{\alpha-1}y^\beta$
> - $U_{xx} = \alpha(\alpha-1)x^{\alpha-2}y^\beta < 0$ (si $\alpha < 1$)
> - $U_{xy} = \alpha\beta x^{\alpha-1}y^{\beta-1} > 0$
> 
> Los bienes son **complementarios**.

---

## 📚 Ejercicios Propuestos

### Nivel Básico

> [!example]- 💪 Práctica Básica
> 
> **1. Calcular todas las derivadas segundas:**
> 
> a) $f(x,y) = x^3y^2 + x^2y^3$
> 
> b) $f(x,y) = e^{xy}$
> 
> c) $f(x,y) = \ln(x^2 + y^2)$
> 
> d) $f(x,y) = \sin(x+y)$
> 
> e) $f(x,y) = \frac{x}{y}$
> 
> ---
> 
> **2. Verificar el Teorema de Schwarz:**
> 
> Para cada función del ejercicio 1, verificar que $f_{xy} = f_{yx}$.
> 
> ---
> 
> **3. Calcular la matriz Hessiana:**
> 
> a) $f(x,y) = x^2 + 2xy + 3y^2$ en $(1,1)$
> 
> b) $f(x,y) = e^x\sin(y)$ en $(0, \pi/2)$
> 
> c) $f(x,y) = xy^2 - x^2y$ en $(2,-1)$
> 
> ---
> 
> **4. Evaluar el determinante de la Hessiana:**
> 
> Para las funciones del ejercicio 3, calcular $D = \det(H_f)$ en los puntos dados.

### Nivel Intermedio

> [!example]- 💪 Práctica Intermedia
> 
> **5. Encontrar y clasificar puntos críticos:**
> 
> a) $f(x,y) = x^2 + y^2 - 2x - 4y + 5$
> 
> b) $f(x,y) = x^3 - 3xy + y^3$
> 
> c) $f(x,y) = x^4 + y^4 - 2x^2 + 4xy - 2y^2$
> 
> d) $f(x,y) = e^{-(x^2+y^2)}(x^2-y^2)$
> 
> ---
> 
> **6. Aproximación de Taylor:**
> 
> a) Encontrar el polinomio de Taylor de segundo orden para $f(x,y) = \sin(x)\sin(y)$ alrededor del origen.
> 
> b) Aproximar $\cos(0.1)\cos(0.2)$ usando la aproximación del inciso (a).
> 
> c) Estimar el error de la aproximación.
> 
> ---
> 
> **7. Segundo diferencial:**
> 
> a) Calcular $d^2f$ para $f(x,y) = x^2y - xy^2$ en el punto $(1,2)$.
> 
> b) Determinar si la función es localmente convexa o cóncava en ese punto.
> 
> ---
> 
> **8. Funciones en tres variables:**
> 
> Para $f(x,y,z) = xyz$:
> 
> a) Calcular todas las derivadas segundas
> 
> b) Escribir la matriz Hessiana
> 
> c) Calcular el Laplaciano $\nabla^2 f$

### Nivel Avanzado

> [!example]- 💪 Práctica Avanzada
> 
> **9. Teoría:**
> 
> a) Demostrar que si $f_{xy}$ y $f_{yx}$ existen y son continuas, entonces son iguales.
> 
> b) Dar un ejemplo explícito donde $f_{xy} \neq f_{yx}$ en un punto.
> 
> c) Demostrar que si $f$ es un polinomio, entonces todas sus derivadas mixtas conmutan.
> 
> ---
> 
> **10. Funciones armónicas:**
> 
> a) Verificar que $f(x,y) = e^x\cos(y)$ satisface la ecuación de Laplace: $f_{xx} + f_{yy} = 0$
> 
> b) Encontrar todas las funciones de la forma $f(x,y) = ax^2 + bxy + cy^2$ que son armónicas.
> 
> c) Demostrar que $f(x,y,z) = \frac{1}{\sqrt{x^2+y^2+z^2}}$ es armónica en $\mathbb{R}^3 \setminus {(0,0,0)}$.
> 
> ---
> 
> **11. Optimización con restricciones:**
> 
> Encontrar los extremos de $f(x,y) = x^2 + 2y^2$ sujeto a la restricción $x + y = 1$:
> 
> a) Usando sustitución directa
> 
> b) Verificar la clasificación usando la Hessiana restringida
> 
> ---
> 
> **12. Aplicación física:**
> 
> La temperatura en una placa está dada por: $$T(x,y) = 100 - x^2 - 2y^2$$
> 
> a) Encontrar los puntos donde la temperatura es estacionaria
> 
> b) Calcular el Laplaciano $\nabla^2 T$
> 
> c) Interpretar físicamente el signo de $\nabla^2 T$

---

## ✅ Soluciones Selectas

### Soluciones Básicas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = x^3y^2 + x^2y^3$
> 
> $$f_x = 3x^2y^2 + 2xy^3$$ $$f_y = 2x^3y + 3x^2y^2$$
> 
> $$f_{xx} = 6xy^2 + 2y^3$$ $$f_{yy} = 2x^3 + 6x^2y$$ $$f_{xy} = 6x^2y + 6xy^2$$ $$f_{yx} = 6x^2y + 6xy^2$$ ✓
> 
> ---
> 
> **1b)** $f(x,y) = e^{xy}$
> 
> $$f_x = ye^{xy}$$ $$f_y = xe^{xy}$$
> 
> $$f_{xx} = y^2e^{xy}$$ $$f_{yy} = x^2e^{xy}$$ $$f_{xy} = e^{xy} + xye^{xy} = e^{xy}(1 + xy)$$ $$f_{yx} = e^{xy}(1 + xy)$$ ✓
> 
> ---
> 
> **3a)** $f(x,y) = x^2 + 2xy + 3y^2$ en $(1,1)$
> 
> $$f_{xx} = 2, \quad f_{yy} = 6, \quad f_{xy} = 2$$
> 
> $$H_f(1,1) = \begin{bmatrix} 2 & 2 \ 2 & 6 \end{bmatrix}$$
> 
> $$D = 2 \cdot 6 - 2^2 = 12 - 4 = 8 > 0$$
> 
> Como $D > 0$ y $f_{xx} = 2 > 0$, el punto $(1,1)$ sería un **mínimo local** si fuera crítico.

### Soluciones Intermedias

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **5a)** $f(x,y) = x^2 + y^2 - 2x - 4y + 5$
> 
> **Puntos críticos:** $$f_x = 2x - 2 = 0 \implies x = 1$$ $$f_y = 2y - 4 = 0 \implies y = 2$$
> 
> Punto crítico: $(1, 2)$
> 
> **Hessiana:** $$f_{xx} = 2, \quad f_{yy} = 2, \quad f_{xy} = 0$$
> 
> $$H_f = \begin{bmatrix} 2 & 0 \ 0 & 2 \end{bmatrix}$$
> 
> $$D = 4 > 0, \quad f_{xx} = 2 > 0$$
> 
> **Conclusión:** $(1,2)$ es un **mínimo local** ✓
> 
> Valor: $f(1,2) = 1 + 4 - 2 - 8 + 5 = 0$
> 
> ---
> 
> **6a)** $f(x,y) = \sin(x)\sin(y)$ alrededor de $(0,0)$
> 
> $$f(0,0) = 0$$ $$f_x = \cos(x)\sin(y) \implies f_x(0,0) = 0$$ $$f_y = \sin(x)\cos(y) \implies f_y(0,0) = 0$$
> 
> $$f_{xx} = -\sin(x)\sin(y) \implies f_{xx}(0,0) = 0$$ $$f_{yy} = -\sin(x)\sin(y) \implies f_{yy}(0,0) = 0$$ $$f_{xy} = \cos(x)\cos(y) \implies f_{xy}(0,0) = 1$$
> 
> **Polinomio de Taylor:** $$P_2(x,y) = 0 + 0 + 0 + \frac{1}{2}[0 + 2 \cdot 1 \cdot xy + 0]$$ $$P_2(x,y) = xy$$
> 
> ---
> 
> **8c)** $f(x,y,z) = xyz$
> 
> $$f_{xx} = 0, \quad f_{yy} = 0, \quad f_{zz} = 0$$
> 
> $$\nabla^2 f = f_{xx} + f_{yy} + f_{zz} = 0 + 0 + 0 = 0$$
> 
> La función $xyz$ es **armónica** ✓

---

## 🎨 Visualización de Conceptos

### Curvatura y Hessiana

> [!note]- 🖼️ Interpretación Visual
> 
> ### Matriz Hessiana Definida Positiva
> 
> ```
> f(x,y) = x² + y²
> 
> Vista 3D:           Curvas de nivel:
>       z                    y
>       |                    |
>       |   ∪                |    ○○○
>       |  / \               |   ○   ○
>       | |   |              |  ○  •  ○
>       |  \ /               |   ○   ○
>       +------- y           |    ○○○
>      /                     +--------- x
>     x                      
> 
> Mínimo local           Círculos concéntricos
> D > 0, f_xx > 0        creciendo hacia afuera
> ```
> 
> ---
> 
> ### Matriz Hessiana Definida Negativa
> 
> ```
> f(x,y) = -(x² + y²)
> 
> Vista 3D:           Curvas de nivel:
>       z                    y
>       |                    |
>       |\  /|               |    ○○○
>       | \/ |               |   ○   ○
>       |  ▲ |               |  ○  •  ○
>       |    |               |   ○   ○
>       +------- y           |    ○○○
>      /                     +--------- x
>     x                      
> 
> Máximo local           Círculos concéntricos
> D > 0, f_xx < 0        decreciendo hacia afuera
> ```
> 
> ---
> 
> ### Matriz Hessiana Indefinida
> 
> ```
> f(x,y) = x² - y²
> 
> Vista 3D:           Curvas de nivel:
>       z                    y
>       |                    |
>       | \ /                |    —  \  /
>       |  X                 |   |    \/
>       | / \                |   |    /\
>       +------- y           |    —  /  \
>      /                     +--------- x
>     x                      
> 
> Punto de silla         Hipérbolas
> D < 0                  (silla de montar)
> ```

---

## 💡 Consejos y Errores Comunes

> [!tip]- ⚠️ Errores Comunes al Trabajar con Derivadas Superiores
> 
> ### Error 1: Confundir el Orden de Derivación
> 
> ❌ **Incorrecto:** Pensar que $\frac{\partial^2 f}{\partial y \partial x}$ significa derivar primero respecto a $y$
> 
> ✅ **Correcto:** En notación de Leibniz, se lee **de derecha a izquierda**: primero $\partial x$, luego $\partial y$
> 
> **Ejemplo:** $$\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = (f_x)_y = f_{xy}$$
> 
> **Regla mnemotécnica:**
> 
> - Leibniz: **derecha → izquierda**
> - Subíndices: **izquierda → derecha**
> 
> ---
> 
> ### Error 2: Asumir que las Derivadas Mixtas Siempre son Iguales
> 
> ❌ **Incorrecto:** "$f_{xy} = f_{yx}$ siempre"
> 
> ✅ **Correcto:** Solo cuando las derivadas mixtas son **continuas** (Teorema de Schwarz)
> 
> **Contraejemplo:** $$f(x,y) = \begin{cases} \frac{xy(x^2-y^2)}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$$
> 
> En el origen: $f_{xy}(0,0) = -1 \neq 1 = f_{yx}(0,0)$
> 
> ---
> 
> ### Error 3: Malinterpretar el Criterio de la Segunda Derivada
> 
> ❌ **Incorrecto:** "Si $f_{xx} > 0$ y $f_{yy} > 0$, entonces es un mínimo"
> 
> ✅ **Correcto:** Se necesita que **$D = f_{xx}f_{yy} - (f_{xy})^2 > 0$**
> 
> **Contraejemplo:** $$f(x,y) = x^2 - y^2 + 10xy$$
> 
> En el origen:
> 
> - $f_{xx} = 2 > 0$ ✓
> - $f_{yy} = -2$ (¡negativo!)
> - $D = 2(-2) - 10^2 = -104 < 0$ → **Punto de silla**
> 
> ---
> 
> ### Error 4: Olvidar el Factor $\frac{1}{2}$ en Taylor
> 
> ❌ **Incorrecto:** $$P_2(x,y) = f(a,b) + f_x h + f_y k + f_{xx}h^2 + 2f_{xy}hk + f_{yy}k^2$$
> 
> ✅ **Correcto:** $$P_2(x,y) = f(a,b) + f_x h + f_y k + \frac{1}{2}[f_{xx}h^2 + 2f_{xy}hk + f_{yy}k^2]$$
> 
> El factor $\frac{1}{2}$ viene de la fórmula general de Taylor.
> 
> ---
> 
> ### Error 5: Confundir Determinante con Traza
> 
> ❌ **Incorrecto:** Usar $f_{xx} + f_{yy}$ para clasificar puntos críticos
> 
> ✅ **Correcto:** Usar $D = f_{xx}f_{yy} - (f_{xy})^2$
> 
> **Nota:** La traza $f_{xx} + f_{yy}$ es el Laplaciano, usado para funciones armónicas, no para clasificación de extremos.
> 
> ---
> 
> ### Error 6: Derivar Incorrectamente el Término Mixto
> 
> ❌ **Incorrecto:** Para $f(x,y) = x^2y$, pensar que $f_{xy} = 2x$
> 
> ✅ **Correcto:** $$f_x = 2xy \implies f_{xy} = \frac{\partial}{\partial y}(2xy) = 2x$$
> 
> Aunque el resultado es correcto aquí, el proceso importa:
> 
> **Proceso correcto:**
> 
> 1. Derivar respecto a $x$: $f_x = 2xy$
> 2. Derivar el resultado respecto a $y$: $f_{xy} = 2x$
> 
> ---
> 
> ### Error 7: No Verificar la Existencia de Derivadas
> 
> ❌ **Incorrecto:** Asumir que si $f$ es continua, entonces todas las derivadas existen
> 
> ✅ **Correcto:** La continuidad NO implica derivabilidad
> 
> **Ejemplo:** $f(x,y) = \sqrt{x^2+y^2}$ es continua en el origen pero no diferenciable allí.
> 
> ---
> 
> ### Error 8: Calcular Mal el Determinante de la Hessiana
> 
> ❌ **Incorrecto:** $D = f_{xx} + f_{yy}$
> 
> ✅ **Correcto:** $$D = f_{xx} \cdot f_{yy} - (f_{xy})^2$$
> 
> **Verificación dimensional:**
> 
> - Si $f$ tiene unidades $[U]$
> - $f_{xx}$ tiene unidades $[U]/[x]^2$
> - $f_{yy}$ tiene unidades $[U]/[y]^2$
> - $D$ tiene unidades $[U]^2/([x]^2[y]^2)$

---

## 🔧 Estrategias de Cálculo

### 📊 Técnicas Eficientes

> [!tip]- 🎯 Métodos para Calcular Derivadas Superiores
> 
> ### Técnica 1: Usar Simetría
> 
> Si $f(x,y) = f(y,x)$ (función simétrica), entonces:
> 
> - $f_x(x,y) = f_y(y,x)$
> - $f_{xx}(x,y) = f_{yy}(y,x)$
> - $f_{xy} = f_{yx}$ automáticamente
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2 + xy$
> 
> Por simetría:
> 
> - Calcular $f_x$ y usar simetría para $f_y$
> - $f_{xx}$ y $f_{yy}$ se relacionan por simetría
> 
> ---
> 
> ### Técnica 2: Factorización Previa
> 
> Antes de derivar, factorizar puede simplificar:
> 
> **Ejemplo:** $f(x,y) = (x+y)^3$
> 
> En lugar de expandir: $$f = x^3 + 3x^2y + 3xy^2 + y^3$$
> 
> Usar regla de la cadena: $$f_x = 3(x+y)^2$$ $$f_{xx} = 6(x+y)$$
> 
> ---
> 
> ### Técnica 3: Derivadas Logarítmicas
> 
> Para productos o cocientes complejos, usar $\ln$:
> 
> **Ejemplo:** $f(x,y) = x^y$
> 
> $$\ln f = y\ln x$$
> 
> Derivando respecto a $x$: $$\frac{f_x}{f} = \frac{y}{x} \implies f_x = \frac{y}{x} \cdot x^y = yx^{y-1}$$
> 
> ---
> 
> ### Técnica 4: Notación de Operadores
> 
> Usar operadores diferenciales: $$D_x = \frac{\partial}{\partial x}, \quad D_y = \frac{\partial}{\partial y}$$
> 
> Entonces: $$f_{xy} = D_y D_x f$$ $$f_{xxy} = D_y D_x^2 f$$
> 
> ---
> 
> ### Técnica 5: Verificación Cruzada
> 
> Para verificar cálculos, usar:
> 
> 1. Calcular $f_{xy}$ derivando primero en $x$
> 2. Calcular $f_{yx}$ derivando primero en $y$
> 3. Verificar que coincidan (si las derivadas son continuas)
> 
> Si no coinciden, hay un error de cálculo.
> 
> ---
> 
> ### Técnica 6: Software de Álgebra Computacional
> 
> Para funciones complicadas, usar software:
> 
> - Python (SymPy)
> - Mathematica
> - Maple
> - MATLAB
> 
> **Ejemplo en Python:**
> 
> ```python
> from sympy import symbols, diff
> x, y = symbols('x y')
> f = x**3 * y**2
> 
> f_xx = diff(f, x, 2)  # Segunda derivada en x
> f_xy = diff(f, x, y)  # Derivada mixta
> ```

---

## 📐 Propiedades Adicionales

### 🔍 Teoremas Importantes

> [!note]- 🟢 Propiedades de las Derivadas Superiores
> 
> ### Propiedad 1: Linealidad
> 
> Para funciones $f$ y $g$, y constantes $a, b$:
> 
> $$(af + bg)_{xx} = af_{xx} + bg_{xx}$$ $$(af + bg)_{xy} = af_{xy} + bg_{xy}$$
> 
> **Aplicación:** Las derivadas superiores respetan la estructura lineal.
> 
> ---
> 
> ### Propiedad 2: Regla del Producto
> 
> Para el producto $h = fg$:
> 
> $$h_{xx} = f_{xx}g + 2f_xg_x + fg_{xx}$$
> 
> $$h_{xy} = f_{xy}g + f_xg_y + f_yg_x + fg_{xy}$$
> 
> **Nota:** Similar a la regla de Leibniz para derivadas de productos.
> 
> ---
> 
> ### Propiedad 3: Regla de la Cadena para Derivadas Segundas
> 
> Si $z = f(u,v)$ donde $u = u(x,y)$ y $v = v(x,y)$:
> 
> $$z_{xx} = f_{uu}u_x^2 + 2f_{uv}u_xv_x + f_{vv}v_x^2 + f_uu_{xx} + f_vv_{xx}$$
> 
> **Fórmula compleja pero sistemática.**
> 
> ---
> 
> ### Propiedad 4: Invarianza Bajo Rotaciones (para funciones radiales)
> 
> Si $f(x,y) = g(r)$ donde $r = \sqrt{x^2+y^2}$:
> 
> $$\nabla^2 f = g''(r) + \frac{1}{r}g'(r)$$
> 
> **Aplicación:** Simplifica el cálculo del Laplaciano en coordenadas polares.
> 
> ---
> 
> ### Propiedad 5: Derivadas de Funciones Implícitas
> 
> Si $F(x,y,z) = 0$ define $z = f(x,y)$ implícitamente:
> 
> $$z_{xx} = -\frac{1}{F_z}\left[F_{xx} + 2F_{xz}z_x + F_{zz}z_x^2 + F_zz_{xx}\right]$$
> 
> (Después de simplificar y resolver para $z_{xx}$)

---

## 🌍 Extensión a Dimensiones Superiores

### 📊 Generalización a $\mathbb{R}^n$

> [!note]- 🔵 Derivadas en Dimensiones Arbitrarias
> 
> Para $f: \mathbb{R}^n \to \mathbb{R}$, la **matriz Hessiana** es $n \times n$:
> 
> $$H_f = \begin{bmatrix} \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \ \frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \ \vdots & \vdots & \ddots & \vdots \ \frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2} \end{bmatrix}$$
> 
> ---
> 
> ### Número de Derivadas Segundas
> 
> **Sin aplicar Schwarz:** $n^2$ derivadas segundas posibles
> 
> **Con Schwarz (derivadas continuas):** $\frac{n(n+1)}{2}$ derivadas distintas
> 
> |Dimensión|Sin Schwarz|Con Schwarz|
> |---|---|---|
> |$n=2$|4|3|
> |$n=3$|9|6|
> |$n=4$|16|10|
> |$n=5$|25|15|
> 
> ---
> 
> ### Criterio de la Segunda Derivada en $\mathbb{R}^n$
> 
> Un punto crítico es:
> 
> - **Mínimo local** si $H_f$ es **definida positiva** (todos los autovalores $> 0$)
> - **Máximo local** si $H_f$ es **definida negativa** (todos los autovalores $< 0$)
> - **Punto de silla** si $H_f$ es **indefinida** (autovalores de signos mixtos)
> 
> ---
> 
> ### Criterio de Sylvester Generalizado
> 
> Para matriz $n \times n$, calcular los **menores principales**:
> 
> $$\Delta_1 = H_{11}$$ $$\Delta_2 = \begin{vmatrix} H_{11} & H_{12} \ H_{21} & H_{22} \end{vmatrix}$$ $$\Delta_3 = \begin{vmatrix} H_{11} & H_{12} & H_{13} \ H_{21} & H_{22} & H_{23} \ H_{31} & H_{32} & H_{33} \end{vmatrix}$$ $$\vdots$$ $$\Delta_n = \det(H_f)$$
> 
> **Definida positiva:** Todos los $\Delta_i > 0$
> 
> **Definida negativa:** $\Delta_i$ alterna signos: $\Delta_1 < 0, \Delta_2 > 0, \Delta_3 < 0, \ldots$

---

## 🎓 Conceptos Avanzados

### 🔬 Tensor de Derivadas

> [!note]- 🟣 Formulación Tensorial
> 
> ### Derivadas como Tensores
> 
> Las derivadas parciales de orden $k$ forman un **tensor** de orden $k$:
> 
> **Orden 0:** $f$ (escalar)
> 
> **Orden 1:** $\nabla f = (f_{x_1}, f_{x_2}, \ldots, f_{x_n})$ (vector)
> 
> **Orden 2:** $H_f = [f_{x_ix_j}]$ (matriz/tensor 2)
> 
> **Orden 3:** $T_{ijk} = f_{x_ix_jx_k}$ (tensor 3)
> 
> ---
> 
> ### Notación de Índices
> 
> En notación de Einstein: $$f_{,i} = \frac{\partial f}{\partial x_i}$$ $$f_{,ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$$
> 
> El Teorema de Schwarz se escribe: $$f_{,ij} = f_{,ji}$$
> 
> ---
> 
> ### Aplicación en Física
> 
> El **tensor de deformación** en elasticidad: $$\varepsilon_{ij} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\right)$$
> 
> es simétrico por construcción (análogo a Schwarz).

---

## 📚 Aplicaciones Modernas

### 🤖 Machine Learning y Optimización

> [!note]- 💻 Aplicaciones Computacionales
> 
> ### Método de Newton en Optimización
> 
> Para minimizar $f(\mathbf{x})$, el método de Newton usa:
> 
> $$\mathbf{x}_{k+1} = \mathbf{x}_k - [H_f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$$
> 
> Requiere:
> 
> - Calcular el gradiente $\nabla f$
> - Calcular la Hessiana $H_f$
> - Invertir $H_f$ (o resolver sistema lineal)
> 
> ---
> 
> ### Quasi-Newton (BFGS)
> 
> Para evitar calcular $H_f$ explícitamente, métodos como **BFGS** aproximan la Hessiana usando solo gradientes.
> 
> Actualización: $$H_{k+1} \approx H_k + \text{(corrección usando gradientes)}$$
> 
> ---
> 
> ### Redes Neuronales: Backpropagation
> 
> El entrenamiento de redes neuronales requiere:
> 
> - **Primera derivada:** Gradiente para descenso (backprop)
> - **Segunda derivada:** Para métodos de segundo orden (Newton, Levenberg-Marquardt)
> 
> La Hessiana de una red neuronal puede ser **enorme** ($10^6 \times 10^6$ para redes grandes), por lo que se usan aproximaciones.
> 
> ---
> 
> ### Análisis de Sensibilidad
> 
> La Hessiana mide cómo cambia el gradiente: $$\frac{\partial}{\partial x_j}\left(\frac{\partial f}{\partial x_i}\right) = H_{ij}$$
> 
> **Aplicación:** Determinar qué parámetros son más sensibles en modelos complejos.

---

## 🎯 Resumen de Conceptos Clave

> [!tip]- 💡 Puntos Esenciales
> 
> ### Derivadas de Segundo Orden
> 
> ✅ **Para $f(x,y)$, hay 4 derivadas segundas:**
> 
> - Dos puras: $f_{xx}$, $f_{yy}$
> - Dos mixtas: $f_{xy}$, $f_{yx}$
> 
> ✅ **Teorema de Schwarz:** Si las derivadas mixtas son continuas, entonces $f_{xy} = f_{yx}$
> 
> ---
> 
> ### Matriz Hessiana
> 
> ✅ **Definición:** $$H_f = \begin{bmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{bmatrix}$$
> 
> ✅ **Determinante:** $$D = f_{xx}f_{yy} - (f_{xy})^2$$
> 
> ---
> 
> ### Criterio de la Segunda Derivada
> 
> ✅ **Clasificación de puntos críticos:**
> 
> - $D > 0$ y $f_{xx} > 0$ → **Mínimo local**
> - $D > 0$ y $f_{xx} < 0$ → **Máximo local**
> - $D < 0$ → **Punto de silla**
> - $D = 0$ → **Indeterminado**
> 
> ---
> 
> ### Segundo Diferencial
> 
> ✅ **Fórmula:** $$d^2f = f_{xx}(dx)^2 + 2f_{xy}(dx)(dy) + f_{yy}(dy)^2$$
> 
> ✅ **Forma matricial:** $$d^2f = \begin{bmatrix} dx & dy \end{bmatrix} H_f \begin{bmatrix} dx \ dy \end{bmatrix}$$
> 
> ---
> 
> ### Aproximación de Taylor
> 
> ✅ **Segundo orden:** $$f(\mathbf{a}+\mathbf{h}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot \mathbf{h} + \frac{1}{2}\mathbf{h}^T H_f(\mathbf{a}) \mathbf{h}$$
> 
> ---
> 
> ### Laplaciano
> 
> ✅ **Definición:** $$\nabla^2 f = f_{xx} + f_{yy} + f_{zz}$$
> 
> ✅ **Funciones armónicas:** $\nabla^2 f = 0$

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema es fundamental para:**
> 
> - [[03 - Optimización]] - Clasificación de extremos usando la Hessiana
> - [[04 - Multiplicadores de Lagrange]] - Optimización con restricciones
> - [[05 - Gradiente y Direccionales]] - La Hessiana es la derivada del gradiente
> - [[06 - Aproximación de Taylor]] - Expansiones de orden superior
> - [[07 - Formas Cuadráticas]] - Análisis de convexidad
> 
> **Conceptos relacionados:**
> 
> - **Diferenciabilidad** - Las derivadas segundas requieren diferenciabilidad
> - **Continuidad** - Necesaria para el Teorema de Schwarz
> - **Álgebra Lineal** - Autovalores y definitud de matrices
> - **Análisis Numérico** - Métodos de optimización
> 
> **Siguiente tema recomendado:** [[03 - Optimización y Puntos Críticos]]

---

## 📝 Notas Finales

> [!note]- 🎯 Reflexiones sobre Derivadas Superiores
> 
> ### Importancia Conceptual
> 
> Las derivadas de orden superior nos permiten:
> 
> 1. **Analizar curvatura** - Entender la geometría local de superficies
> 2. **Clasificar extremos** - Distinguir mínimos, máximos y puntos de silla
> 3. **Aproximar funciones** - Construir polinomios de Taylor precisos
> 4. **Modelar fenómenos** - Ecuaciones diferenciales parciales
> 
> ---
> 
> ### Conexión Intuición-Formalismo
> 
> **Intuición geométrica:**
> 
> - $f_{xx}$ mide "cuánto se curva" en dirección $x$
> - $f_{xy}$ mide "cómo se tuerce" la superficie
> - La Hessiana captura toda la información de curvatura local
> 
> **Formalismo matemático:**
> 
> - Teorema de Schwarz garantiza consistencia
> - Formas cuadráticas conectan con álgebra lineal
> - Aproximaciones de Taylor proporcionan herramienta analítica
> 
> ---
> 
> ### Para Profundizar
> 
> **Conceptos avanzados:**
> 
> - Formas diferenciales de orden superior
> - Análisis de Morse (topología diferencial)
> - Teoría de catástrofes
> - Cálculo variacional
> 
> **Aplicaciones especializadas:**
> 
> - Geometría Riemanniana (tensor de curvatura)
> - Teoría de elasticidad (tensor de deformación)
> - Mecánica cuántica (operadores diferenciales)
> - Procesamiento de imágenes (detección de bordes)
> 
> ---
> 
> ### Perspectiva Histórica
> 
> El desarrollo de derivadas superiores fue crucial para:
> 
> - **Newton y Leibniz** - Fundamentos del cálculo
> - **Euler y Lagrange** - Mecánica analítica
> - **Gauss** - Geometría diferencial
> - **Riemann** - Geometría no-euclidiana
> - **Schwarz y Clairaut** - Teorema de igualdad de derivadas mixtas

---

**Tags:** #calculo-multivariable #derivadas-superiores #matriz-hessiana #teorema-schwarz #segundo-diferencial #taylor #optimizacion #puntos-criticos #curvatura #laplaciano
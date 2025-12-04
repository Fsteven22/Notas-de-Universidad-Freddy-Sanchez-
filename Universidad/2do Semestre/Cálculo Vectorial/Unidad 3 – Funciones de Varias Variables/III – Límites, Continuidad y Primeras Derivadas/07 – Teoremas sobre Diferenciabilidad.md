# 📘 Teoremas sobre Diferenciabilidad

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes los Teoremas sobre Diferenciabilidad?
> 
> Hasta ahora hemos visto cómo calcular derivadas parciales y la matriz Jacobiana. Pero surge una pregunta fundamental: **¿cuándo podemos estar seguros de que una función es diferenciable y que todas nuestras fórmulas funcionan correctamente?**
> 
> **Motivación:**
> 
> - Calcular derivadas parciales es fácil... pero ¿garantizan diferenciabilidad?
> - ¿Cuándo podemos usar la regla de la cadena con confianza?
> - ¿Cuándo existe una función inversa localmente?
> - ¿Cuándo podemos despejar variables implícitamente?
> 
> **El problema central:**
> 
> Existen funciones donde:
> 
> - ✅ Las derivadas parciales existen
> - ✅ El gradiente está bien definido
> - ❌ Pero la función NO es diferenciable
> - ❌ Y las fórmulas fallan
> 
> **La solución: Teoremas fundamentales**
> 
> Este tema presenta los **tres teoremas pilares** del cálculo multivariable:
> 
> 1. **Teorema de Diferenciabilidad (C¹):** Condiciones suficientes
> 2. **Teorema de la Función Inversa:** Cuándo existe inversa local
> 3. **Teorema de la Función Implícita:** Cuándo podemos despejar variables
> 
> **Aplicaciones prácticas:**
> 
> - **Análisis:** Garantizar que aproximaciones lineales son válidas
> - **Optimización:** Condiciones para usar multiplicadores de Lagrange
> - **Ecuaciones:** Resolver sistemas implícitos
> - **Geometría:** Existencia de parametrizaciones
> - **Física:** Cambios de coordenadas válidos
> - **Ingeniería:** Análisis de sensibilidad confiable

---

## 📝 Teorema 1: Condición Suficiente para Diferenciabilidad

### 🔑 Teorema Principal (C¹ ⇒ Diferenciable)

> [!example]- 🟢 Teorema: Diferenciabilidad de Funciones C¹
> 
> **Enunciado:** Sea $f: U \subseteq \mathbb{R}^n \to \mathbb{R}$ donde $U$ es abierto. Si todas las derivadas parciales de $f$ existen y son **continuas** en $U$, entonces $f$ es **diferenciable** en $U$.
> 
> **En notación:** Si $f \in C^1(U)$, entonces $f$ es diferenciable en $U$.
> 
> ---
> 
> **Consecuencias:**
> 
> 1. **Aproximación lineal válida:** $$f(\vec{a} + \vec{h}) = f(\vec{a}) + \nabla f(\vec{a}) \cdot \vec{h} + o(|\vec{h}|)$$
>     
> 2. **Fórmula de derivada direccional funciona:** $$D_{\vec{u}}f = \nabla f \cdot \vec{u}$$
>     
> 3. **Plano tangente existe:** $$z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$
>     
> 4. **Regla de la cadena válida:** Si $f, g \in C^1$ entonces $(f \circ g)' = f'(g) \cdot g'$
>     
> 
> ---
> 
> **Interpretación:**
> 
> - La **continuidad** de las derivadas parciales es la clave
> - No basta que las derivadas existan
> - C¹ es la "regularidad mínima segura"
> 
> ---
> 
> **Notación recordatoria:**
> 
> $$f \in C^1(U) \iff \begin{cases} \text{Todas las } \frac{\partial f}{\partial x_i} \text{ existen en } U \ \text{Todas las } \frac{\partial f}{\partial x_i} \text{ son continuas en } U \end{cases}$$

### 🎯 Versión para Funciones Vectoriales

> [!example]- 🟡 Extensión a $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$
> 
> **Teorema:** Sea $\vec{F}: U \subseteq \mathbb{R}^n \to \mathbb{R}^m$ donde $U$ es abierto.
> 
> Si todas las derivadas parciales de todas las componentes de $\vec{F}$ existen y son continuas en $U$, entonces $\vec{F}$ es diferenciable en $U$.
> 
> **En términos de la Jacobiana:**
> 
> Si todos los elementos de $J_{\vec{F}}$ son funciones continuas, entonces $\vec{F}$ es diferenciable.
> 
> ---
> 
> **Consecuencias:**
> 
> 1. **Aproximación lineal:** $$\vec{F}(\vec{a} + \vec{h}) = \vec{F}(\vec{a}) + J_{\vec{F}}(\vec{a})\vec{h} + o(|\vec{h}|)$$
>     
> 2. **Regla de la cadena matricial:** $$J_{\vec{G} \circ \vec{F}} = J_{\vec{G}}(\vec{F}) \cdot J_{\vec{F}}$$
>     
> 
> ---
> 
> **Ejemplo verificable:**
> 
> $$\vec{F}(x,y) = \begin{bmatrix} x^2 + y^2 \ xy \end{bmatrix}$$
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & 2y \ y & x \end{bmatrix}$$
> 
> Todas las entradas son **polinomios** → continuas en $\mathbb{R}^2$
> 
> $$\boxed{\vec{F} \in C^1(\mathbb{R}^2) \implies \vec{F} \text{ es diferenciable}}$$

### 📊 Ejemplos y Contraejemplos

> [!example]- 📝 Ejemplo 1: Función C¹
> 
> **Función:** $$f(x,y) = e^{x^2+y^2}$$
> 
> **Derivadas parciales:**
> 
> $$f_x = 2xe^{x^2+y^2}, \quad f_y = 2ye^{x^2+y^2}$$
> 
> **Continuidad:**
> 
> Ambas derivadas son composiciones de funciones continuas (polinomios y exponencial).
> 
> $$\boxed{f \in C^1(\mathbb{R}^2) \implies f \text{ es diferenciable en todo } \mathbb{R}^2}$$
> 
> **Por tanto:**
> 
> - Podemos usar $D_{\vec{u}}f = \nabla f \cdot \vec{u}$ con confianza
> - El plano tangente existe en todo punto
> - La regla de la cadena funciona

> [!example]- 📝 Contraejemplo 1: Derivadas Existen pero NO es Diferenciable
> 
> **Función:**
> 
> $$f(x,y) = \begin{cases} \frac{xy}{\sqrt{x^2+y^2}} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **En el origen:**
> 
> **Derivadas parciales:**
> 
> $$f_x(0,0) = \lim_{h \to 0} \frac{f(h,0) - f(0,0)}{h} = \lim_{h \to 0} \frac{0}{h} = 0$$
> 
> $$f_y(0,0) = \lim_{k \to 0} \frac{f(0,k) - f(0,0)}{k} = \lim_{k \to 0} \frac{0}{k} = 0$$
> 
> ✅ Las derivadas parciales **existen**: $\nabla f(0,0) = (0,0)$
> 
> ---
> 
> **Verificar diferenciabilidad:**
> 
> Para ser diferenciable, necesitamos:
> 
> $$\lim_{(h,k) \to (0,0)} \frac{f(h,k) - f(0,0) - \nabla f(0,0) \cdot (h,k)}{\sqrt{h^2+k^2}} = 0$$
> 
> $$= \lim_{(h,k) \to (0,0)} \frac{hk/(h^2+k^2)^{1/2}}{\sqrt{h^2+k^2}} = \lim_{(h,k) \to (0,0)} \frac{hk}{h^2+k^2}$$
> 
> **Probar con $h = k = t$:**
> 
> $$\lim_{t \to 0} \frac{t^2}{2t^2} = \frac{1}{2} \neq 0$$
> 
> ❌ El límite **no es cero** → $f$ NO es diferenciable en $(0,0)$
> 
> ---
> 
> **Continuidad de las derivadas:**
> 
> Fuera del origen:
> 
> $$f_x(x,y) = \frac{y^3}{(x^2+y^2)^{3/2}}$$
> 
> $$\lim_{(x,y) \to (0,0)} f_x(x,y) \text{ depende de la dirección}$$
> 
> ❌ $f_x$ **no es continua** en $(0,0)$
> 
> ---
> 
> **Conclusión:**
> 
> - Derivadas parciales existen: ✅
> - Derivadas parciales continuas: ❌
> - Función diferenciable: ❌
> 
> **Moraleja:** Existencia de derivadas parciales NO implica diferenciabilidad.

> [!example]- 📝 Contraejemplo 2: Función NO C¹
> 
> **Función:**
> 
> $$f(x,y) = \begin{cases} (x^2+y^2)\sin\left(\frac{1}{\sqrt{x^2+y^2}}\right) & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **Resultado (se puede demostrar):**
> 
> - $f$ es diferenciable en $(0,0)$ ✅
> - Las derivadas parciales existen en todo punto ✅
> - Pero $f_x$ y $f_y$ **no son continuas** en $(0,0)$ ❌
> 
> Por tanto: $f \notin C^1$ pero es diferenciable.
> 
> **Moraleja:**
> 
> - Diferenciabilidad NO implica C¹
> - C¹ es condición **suficiente** pero no necesaria

---

## 🔄 Teorema 2: Teorema de la Función Inversa

### 🔑 Enunciado del Teorema

> [!example]- 🟢 Teorema de la Función Inversa
> 
> **Contexto:** Sea $\vec{F}: U \subseteq \mathbb{R}^n \to \mathbb{R}^n$ donde $U$ es abierto, y sea $\vec{a} \in U$.
> 
> **Hipótesis:**
> 
> 1. $\vec{F} \in C^1(U)$ (función continuamente diferenciable)
> 2. $\det(J_{\vec{F}}(\vec{a})) \neq 0$ (Jacobiano no nulo en $\vec{a}$)
> 
> **Conclusión:**
> 
> Existen entornos abiertos $V$ de $\vec{a}$ y $W$ de $\vec{F}(\vec{a})$ tales que:
> 
> 1. **$\vec{F}$ es inyectiva en $V$:** $$\vec{F}(\vec{x}_1) = \vec{F}(\vec{x}_2) \implies \vec{x}_1 = \vec{x}_2 \quad \forall \vec{x}_1, \vec{x}_2 \in V$$
>     
> 2. **$\vec{F}(V) = W$** (sobreyectiva sobre $W$)
>     
> 3. **Existe función inversa:** $\vec{G}: W \to V$ tal que: $$\vec{G}(\vec{F}(\vec{x})) = \vec{x} \quad \forall \vec{x} \in V$$ $$\vec{F}(\vec{G}(\vec{y})) = \vec{y} \quad \forall \vec{y} \in W$$
>     
> 4. **La inversa es C¹:** $\vec{G} \in C^1(W)$
>     
> 5. **Jacobiana de la inversa:** $$J_{\vec{G}}(\vec{y}) = [J_{\vec{F}}(\vec{G}(\vec{y}))]^{-1}$$
>     
>     O en el punto $\vec{a}$: $$J_{\vec{G}}(\vec{F}(\vec{a})) = [J_{\vec{F}}(\vec{a})]^{-1}$$
>     
> 
> ---
> 
> **Interpretación geométrica:**
> 
> ```
>     Dominio U               Imagen
>        V                      W
>     •───→ F                •───→
>     a                      F(a)
>     │                       │
>     │ localmente            │ localmente
>     │ invertible            │
>     ↓                       ↓
>     •←─── G                •←───
> ```
> 
> Si el Jacobiano es no nulo, $\vec{F}$ es **localmente invertible**.
> 
> ---
> 
> **Condición geométrica:**
> 
> $\det(J_{\vec{F}}(\vec{a})) \neq 0$ significa que $\vec{F}$ no "aplasta" el espacio cerca de $\vec{a}$.

### 🎯 Casos Especiales y Ejemplos

> [!example]- 📝 Ejemplo 1: Coordenadas Polares
> 
> **Transformación:**
> 
> $$\vec{F}(r, \theta) = \begin{bmatrix} r\cos\theta \ r\sin\theta \end{bmatrix} = \begin{bmatrix} x \ y \end{bmatrix}$$
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} \cos\theta & -r\sin\theta \ \sin\theta & r\cos\theta \end{bmatrix}$$
> 
> **Jacobiano:**
> 
> $$\det(J_{\vec{F}}) = r(\cos^2\theta + \sin^2\theta) = r$$
> 
> **Análisis:**
> 
> - Si $r > 0$: $\det(J_{\vec{F}}) = r \neq 0$ ✅
> - Por el teorema: $\vec{F}$ es **localmente invertible** para $r > 0$
> 
> **Función inversa:**
> 
> $$\vec{G}(x,y) = \begin{bmatrix} \sqrt{x^2+y^2} \ \arctan(y/x) \end{bmatrix} = \begin{bmatrix} r \ \theta \end{bmatrix}$$
> 
> (con ajustes apropiados para los cuadrantes)
> 
> **Jacobiana de la inversa:**
> 
> $$J_{\vec{G}} = [J_{\vec{F}}]^{-1} = \frac{1}{r}\begin{bmatrix} r\cos\theta & r\sin\theta \ -\sin\theta & \cos\theta \end{bmatrix}$$
> 
> $$= \begin{bmatrix} \cos\theta & \sin\theta \ -\frac{\sin\theta}{r} & \frac{\cos\theta}{r} \end{bmatrix}$$
> 
> ---
> 
> **Singularidad en el origen:**
> 
> - Cuando $r = 0$: $\det(J_{\vec{F}}) = 0$ ❌
> - El teorema **no aplica** en el origen
> - De hecho, múltiples valores de $\theta$ dan el mismo punto $(0,0)$
> - No hay inversa única en el origen

> [!example]- 📝 Ejemplo 2: Función Compleja
> 
> **Función:** $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$ (corresponde a $f(z) = z^2$ en el plano complejo)
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & -2y \ 2y & 2x \end{bmatrix}$$
> 
> **Jacobiano:**
> 
> $$\det(J_{\vec{F}}) = 4x^2 + 4y^2 = 4(x^2 + y^2)$$
> 
> **Análisis:**
> 
> - Si $(x,y) \neq (0,0)$: $\det(J_{\vec{F}}) > 0$ ✅
> - $\vec{F}$ es localmente invertible excepto en el origen
> 
> **Inversa local:**
> 
> Cerca de $(1,0)$: $\vec{F}(1,0) = (1,0)$
> 
> $$J_{\vec{F}}(1,0) = \begin{bmatrix} 2 & 0 \ 0 & 2 \end{bmatrix}$$
> 
> Inversa de la Jacobiana:
> 
> $$J_{\vec{G}}(1,0) = \begin{bmatrix} 1/2 & 0 \ 0 & 1/2 \end{bmatrix}$$
> 
> **Interpretación:** Localmente cerca de $(1,0)$, la inversa es aproximadamente $(x,y) \mapsto (x/2, y/2)$ más términos de orden superior.

> [!example]- 📝 Ejemplo 3: Transformación NO Invertible
> 
> **Función:**
> 
> $$\vec{F}(x,y) = \begin{bmatrix} x^2 \ y^2 \end{bmatrix}$$
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & 0 \ 0 & 2y \end{bmatrix}$$
> 
> **Jacobiano:**
> 
> $$\det(J_{\vec{F}}) = 4xy$$
> 
> **Análisis:**
> 
> - Si $x = 0$ o $y = 0$: $\det(J_{\vec{F}}) = 0$ ❌
> - En los ejes, el teorema **no garantiza** invertibilidad local
> 
> **Verificación:**
> 
> En el eje $x$ (donde $y=0$):
> 
> $$\vec{F}(2,0) = \begin{bmatrix} 4 \ 0 \end{bmatrix} = \vec{F}(-2,0)$$
> 
> ¡Dos puntos distintos tienen la misma imagen! No es inyectiva.
> 
> **Pero:** En el primer cuadrante ($x,y > 0$), $\det(J_{\vec{F}}) = 4xy > 0$ y $\vec{F}$ SÍ es localmente invertible.

### 🔧 Aplicaciones del Teorema

> [!note]- 🎯 Aplicaciones Prácticas
> 
> ### 1. Cambios de Coordenadas Válidos
> 
> **Problema:** ¿Cuándo un cambio de coordenadas es válido?
> 
> **Respuesta:** Cuando el Jacobiano es no nulo.
> 
> **Ejemplo:** Coordenadas esféricas
> 
> $$\vec{F}(\rho,\phi,\theta) = \begin{bmatrix} \rho\sin\phi\cos\theta \ \rho\sin\phi\sin\theta \ \rho\cos\phi \end{bmatrix}$$
> 
> $$\det(J_{\vec{F}}) = \rho^2\sin\phi$$
> 
> Válido cuando $\rho > 0$ y $\phi \in (0, \pi)$
> 
> ---
> 
> ### 2. Resolución de Sistemas No Lineales
> 
> **Sistema:** $\vec{F}(\vec{x}) = \vec{b}$
> 
> Si cerca de una solución $\vec{a}$ se tiene $\det(J_{\vec{F}}(\vec{a})) \neq 0$:
> 
> - La solución es **localmente única**
> - Podemos usar el método de Newton
> - Pequeños cambios en $\vec{b}$ producen pequeños cambios en la solución
> 
> ---
> 
> ### 3. Análisis de Estabilidad
> 
> En ecuaciones diferenciales, si $\det(J_{\vec{F}}(\vec{x}_0)) \neq 0$ en un punto de equilibrio:
> 
> - El equilibrio es **hiperbólico**
> - Podemos analizar estabilidad usando la Jacobiana
> 
> ---
> 
> ### 4. Optimización
> 
> En problemas de optimización con restricciones:
> 
> - La invertibilidad local garantiza que podemos parametrizar restricciones
> - Permite usar multiplicadores de Lagrange

---

## 🔗 Teorema 3: Teorema de la Función Implícita

### 🔑 Enunciado del Teorema

> [!example]- 🟢 Teorema de la Función Implícita
> 
> **Contexto:** Sea $F: U \subseteq \mathbb{R}^{n+m} \to \mathbb{R}^m$ donde $U$ es abierto.
> 
> Escribimos $\vec{x} \in \mathbb{R}^n$ y $\vec{y} \in \mathbb{R}^m$, así que:
> 
> $$F(\vec{x}, \vec{y}) = \vec{0}$$
> 
> Sea $(\vec{a}, \vec{b})$ un punto donde $F(\vec{a}, \vec{b}) = \vec{0}$.
> 
> **Hipótesis:**
> 
> 1. $F \in C^1(U)$
>     
> 2. La matriz Jacobiana parcial respecto a $\vec{y}$: $$\frac{\partial F}{\partial \vec{y}}(\vec{a}, \vec{b}) = \begin{bmatrix} \frac{\partial F_1}{\partial y_1} & \cdots & \frac{\partial F_1}{\partial y_m} \ \vdots & \ddots & \vdots \ \frac{\partial F_m}{\partial y_1} & \cdots & \frac{\partial F_m}{\partial y_m} \end{bmatrix}_{(\vec{a},\vec{b})}$$
>     
>     tiene determinante no nulo: $\det\left(\frac{\partial F}{\partial \vec{y}}(\vec{a}, \vec{b})\right) \neq 0$
>     
> 
> **Conclusión:**
> 
> Existen entornos $V$ de $\vec{a}$ (en $\mathbb{R}^n$) y $W$ de $\vec{b}$ (en $\mathbb{R}^m$), y una función única $\vec{g}: V \to W$ tal que:
> 
> 1. **$\vec{g}$ resuelve la ecuación implícita:** $$F(\vec{x}, \vec{g}(\vec{x})) = \vec{0} \quad \forall \vec{x} \in V$$
>     
> 2. **$\vec{g}$ pasa por $(\vec{a}, \vec{b})$:** $$\vec{g}(\vec{a}) = \vec{b}$$
>     
> 3. **$\vec{g}$ es C¹:** $\vec{g} \in C^1(V)$
>     
> 4. **Jacobiana de $\vec{g}$:** $$J_{\vec{g}}(\vec{x}) = -\left[\frac{\partial F}{\partial \vec{y}}(\vec{x}, \vec{g}(\vec{x}))\right]^{-1} \cdot \frac{\partial F}{\partial \vec{x}}(\vec{x}, \vec{g}(\vec{x}))$$
>     
> 
> ---
> 
> **Interpretación:**
> 
> Si la Jacobiana parcial respecto a las variables que queremos despejar es invertible, entonces **podemos despejar localmente** esas variables en función de las demás.
> 
> ---
> 
> **Diagrama conceptual:**
> 
> ```
> Ecuación: F(x, y) = 0
>           ↓
> Condición: det(∂F/∂y) ≠ 0
>           ↓
> Existe: y = g(x) localmente
> ```

### 🎯 Caso Simple: Una Ecuación, Dos Variables

> [!example]- 📝 Versión 2D (Más Común)
> 
> **Contexto:** $F(x, y) = 0$ (una ecuación escalar)
> 
> **Hipótesis:**
> 
> 1. $F \in C^1$
> 2. $F(a, b) = 0$
> 3. $\frac{\partial F}{\partial y}(a, b) \neq 0$
> 
> **Conclusión:**
> 
> Existe función $y = g(x)$ definida cerca de $x = a$ tal que:
> 
> 4. $F(x, g(x)) = 0$ para $x$ cerca de $a$
> 5. $g(a) = b$
> 6. $g$ es C¹
> 7. **Derivada de $g$:** $$g'(x) = -\frac{\frac{\partial F}{\partial x}(x, g(x))}{\frac{\partial F}{\partial y}(x, g(x))} = -\frac{F_x}{F_y}$$
> 
> ---
> 
> **Fórmula memorable:**
> 
> Si $F(x,y) = 0$ define $y$ implícitamente:
> 
> $$\boxed{\frac{dy}{dx} = -\frac{F_x}{F_y}}$$
> 
> (siempre que $F_y \neq 0$)

### 📊 Ejemplos Detallados

> [!example]- 📝 Ejemplo 1: Círculo
> 
> **Ecuación:** $$F(x,y) = x^2 + y^2 - 1 = 0$$
> 
> (círculo unitario)
> 
> **Pregunta:** ¿Podemos despejar $y$ en función de $x$ cerca del punto $(0, 1)$?
> 
> ---
> 
> **Verificar hipótesis:**
> 
> 1. $F \in C^1(\mathbb{R}^2)$ ✅ (polinomio)
>     
> 2. $F(0, 1) = 0 + 1 - 1 = 0$ ✅
>     
> 3. $\frac{\partial F}{\partial y} = 2y$
>     
>     En $(0,1)$: $F_y(0,1) = 2 \neq 0$ ✅
>     
> 
> **Conclusión:** Por el teorema, existe $y = g(x)$ cerca de $x=0$ tal que $F(x, g(x)) = 0$.
> 
> ---
> 
> **Encontrar la función explícitamente:**
> 
> De $x^2 + y^2 = 1$:
> 
> $$y = \pm\sqrt{1-x^2}$$
> 
> Como $g(0) = 1$ (positivo), tomamos:
> 
> $$g(x) = \sqrt{1-x^2}$$
> 
> válida para $x \in (-1, 1)$ cerca de $x=0$.
> 
> ---
> 
> **Derivada implícita:**
> 
> $$g'(x) = -\frac{F_x}{F_y} = -\frac{2x}{2y} = -\frac{x}{y}$$
> 
> En la curva: $y = \sqrt{1-x^2}$, así que:
> 
> $$g'(x) = -\frac{x}{\sqrt{1-x^2}}$$
> 
> **Verificación directa:**
> 
> $$\frac{d}{dx}\sqrt{1-x^2} = \frac{-2x}{2\sqrt{1-x^2}} = -\frac{x}{\sqrt{1-x^2}}$$ ✓
> ---
> 
> **¿Qué pasa en otros puntos?**
> 
> **En $(0, -1)$:**
> 
> - $F_y(0,-1) = -2 \neq 0$ ✅
> - Podemos despejar: $y = -\sqrt{1-x^2}$
> 
> **En $(1, 0)$:**
> 
> - $F_y(1,0) = 0$ ❌
> - El teorema **no aplica**
> - No podemos despejar $y$ como función de $x$ (tangente vertical)
> 
> **Pero:**
> 
> - $F_x(1,0) = 2 \neq 0$ ✅
> - ¡Podemos despejar $x$ como función de $y$!
> - $x = \sqrt{1-y^2}$ cerca de $y=0$

> [!example]- 📝 Ejemplo 2: Superficie en 3D
> 
> **Ecuación:** $$F(x,y,z) = x^2 + y^2 + z^2 - z = 0$$
> 
> **Pregunta:** ¿Podemos despejar $z$ en función de $(x,y)$ cerca del punto $(0, 0, 1)$?
> 
> ---
> 
> **Verificar hipótesis:**
> 
> 1. $F \in C^1(\mathbb{R}^3)$ ✅
>     
> 2. $F(0,0,1) = 0 + 0 + 1 - 1 = 0$ ✅
>     
> 3. $\frac{\partial F}{\partial z} = 2z - 1$
>     
>     En $(0,0,1)$: $F_z(0,0,1) = 2 - 1 = 1 \neq 0$ ✅
>     
> 
> **Conclusión:** Existe $z = g(x,y)$ cerca de $(0,0)$ con $g(0,0) = 1$.
> 
> ---
> 
> **Función explícita:**
> 
> De $x^2 + y^2 + z^2 - z = 0$:
> 
> $$z^2 - z + (x^2 + y^2) = 0$$
> 
> Fórmula cuadrática:
> 
> $$z = \frac{1 \pm \sqrt{1 - 4(x^2+y^2)}}{2}$$
> 
> Como $g(0,0) = 1$, tomamos el signo +:
> 
> $$g(x,y) = \frac{1 + \sqrt{1 - 4(x^2+y^2)}}{2}$$
> 
> válida para $x^2 + y^2 < 1/4$.
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z} = -\frac{2x}{2z-1}$$
> 
> $$\frac{\partial z}{\partial y} = -\frac{F_y}{F_z} = -\frac{2y}{2z-1}$$
> 
> En el punto $(0,0,1)$:
> 
> $$g_x(0,0) = -\frac{0}{1} = 0, \quad g_y(0,0) = -\frac{0}{1} = 0$$
> 
> El plano tangente en $(0,0,1)$ es horizontal: $z = 1$.

> [!example]- 📝 Ejemplo 3: Sistema de Ecuaciones
> 
> **Sistema:**
> 
> $$\begin{cases} F_1(x, y, z) = x^2 + y^2 + z^2 - 1 = 0 \ F_2(x, y, z) = x + y + z - 1 = 0 \end{cases}$$
> 
> **Pregunta:** ¿Podemos despejar $(y,z)$ en función de $x$ cerca del punto $(1, 0, 0)$?
> 
> ---
> 
> **Función vectorial:**
> 
> $$\vec{F}(x,y,z) = \begin{bmatrix} x^2 + y^2 + z^2 - 1 \ x + y + z - 1 \end{bmatrix}$$
> 
> **Verificar:**
> 
> 4. $\vec{F} \in C^1$ ✅
>     
> 5. $\vec{F}(1,0,0) = \begin{bmatrix} 0 \ 0 \end{bmatrix}$ ✅
>     
> 6. **Jacobiana parcial respecto a $(y,z)$:**
>     
> 
> $$\frac{\partial \vec{F}}{\partial (y,z)} = \begin{bmatrix} \frac{\partial F_1}{\partial y} & \frac{\partial F_1}{\partial z} \ \frac{\partial F_2}{\partial y} & \frac{\partial F_2}{\partial z} \end{bmatrix} = \begin{bmatrix} 2y & 2z \ 1 & 1 \end{bmatrix}$$
> 
> En $(1,0,0)$:
> 
> $$\frac{\partial \vec{F}}{\partial (y,z)}(1,0,0) = \begin{bmatrix} 0 & 0 \ 1 & 1 \end{bmatrix}$$
> 
> Determinante: $0 \cdot 1 - 0 \cdot 1 = 0$ ❌
> 
> **Conclusión:** El teorema **no garantiza** que podamos despejar $(y,z)$ en función de $x$ cerca de este punto.
> 
> ---
> 
> **Alternativa:** ¿Podemos despejar $(x,z)$ en función de $y$?
> 
> $$\frac{\partial \vec{F}}{\partial (x,z)} = \begin{bmatrix} 2x & 2z \ 1 & 1 \end{bmatrix}$$
> 
> En $(1,0,0)$:
> 
> $$\begin{bmatrix} 2 & 0 \ 1 & 1 \end{bmatrix}$$
> 
> Determinante: $2 \cdot 1 - 0 \cdot 1 = 2 \neq 0$ ✅
> 
> **¡Sí podemos!** Existen funciones $x = g_1(y)$, $z = g_2(y)$ cerca de $y=0$.

### 🔧 Fórmula para las Derivadas

> [!note]- 📐 Cálculo de Derivadas Implícitas
> 
> ### Caso: Una Ecuación $F(x,y) = 0$
> 
> Si $y = g(x)$ está definida implícitamente por $F(x,y) = 0$:
> 
> $$\boxed{\frac{dy}{dx} = -\frac{F_x}{F_y}}$$
> 
> (siempre que $F_y \neq 0$)
> 
> ---
> 
> ### Caso: Una Ecuación $F(x,y,z) = 0$
> 
> Si $z = g(x,y)$ está definida implícitamente:
> 
> $$\boxed{\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}}$$
> 
> (siempre que $F_z \neq 0$)
> 
> ---
> 
> ### Caso General: Sistema
> 
> Si $\vec{y} = \vec{g}(\vec{x})$ está definido implícitamente por $\vec{F}(\vec{x}, \vec{y}) = \vec{0}$:
> 
> $$\boxed{J_{\vec{g}}(\vec{x}) = -\left[\frac{\partial \vec{F}}{\partial \vec{y}}\right]^{-1} \cdot \frac{\partial \vec{F}}{\partial \vec{x}}}$$
> 
> ---
> 
> **Mnemónico:**
> 
> "Negativo de la inversa de las derivadas en $y$, multiplicado por las derivadas en $x$"

---

## 🔄 Relación entre los Teoremas

> [!note]- 🔗 Conexiones entre los Tres Teoremas
> 
> ### Teorema de la Función Implícita vs Inversa
> 
> El **Teorema de la Función Implícita** es una generalización del **Teorema de la Función Inversa**.
> 
> **Demostración conceptual:**
> 
> Consideremos $F(\vec{x}, \vec{y}) = \vec{y} - \vec{G}(\vec{x})$ donde $\vec{G}: \mathbb{R}^n \to \mathbb{R}^n$.
> 
> La ecuación $F(\vec{x}, \vec{y}) = \vec{0}$ se convierte en:
> 
> $$\vec{y} = \vec{G}(\vec{x})$$
> 
> La Jacobiana parcial respecto a $\vec{y}$ es:
> 
> $$\frac{\partial F}{\partial \vec{y}} = I_n$$
> 
> que siempre es invertible.
> 
> ---
> 
> ### Diagrama de Implicaciones
> 
> ```
> Función Implícita (general)
>          ↓
>          ├─→ Función Inversa (caso especial)
>          │
>          └─→ Diferenciabilidad (base)
> ```
> 
> Todos estos teoremas se basan en:
> 
> - C¹ (continuidad de derivadas)
> - Jacobiano no nulo (invertibilidad local)
> 
> ---
> 
> ### Tabla Comparativa
> 
> |Aspecto|Diferenciabilidad|Función Inversa|Función Implícita|
> |---|---|---|---|
> |**Condición**|$f \in C^1$|$\det(J_{\vec{F}}) \neq 0$|$\det\left(\frac{\partial F}{\partial \vec{y}}\right) \neq 0$|
> |**Garantiza**|Aprox. lineal|Inversa local|Despeje local|
> |**Aplicación**|Fórmulas básicas|Cambio de variables|Ecuaciones implícitas|
> |**Dimensiones**|Cualquiera|$n \to n$ (cuadrada)|$(n+m) \to m$|

---

## 🎯 Aplicaciones Avanzadas

### Aplicación 1: Multiplicadores de Lagrange

> [!example]- 🎯 Optimización con Restricciones
> 
> **Problema:** Optimizar $f(\vec{x})$ sujeto a $g(\vec{x}) = c$
> 
> **Método:** Buscar puntos donde:
> 
> $$\nabla f = \lambda \nabla g$$
> 
> para algún $\lambda \in \mathbb{R}$ (multiplicador de Lagrange).
> 
> ---
> 
> **Justificación usando Función Implícita:**
> 
> Si $\nabla g \neq \vec{0}$ en un punto, el teorema de la función implícita garantiza que podemos parametrizar la restricción $g(\vec{x}) = c$ localmente.
> 
> En esa parametrización, la condición de optimalidad lleva a $\nabla f = \lambda \nabla g$.
> 
> ---
> 
> **Ejemplo:**
> 
> **Maximizar:** $f(x,y) = xy$
> 
> **Sujeto a:** $g(x,y) = x^2 + y^2 = 1$
> 
> **Condición de Lagrange:**
> 
> $$\nabla f = \lambda \nabla g$$
> 
> $$(y, x) = \lambda(2x, 2y)$$
> 
> Esto da: $$y = 2\lambda x, \quad x = 2\lambda y$$
> 
> Multiplicando: $xy = 4\lambda^2 xy$
> 
> Si $xy \neq 0$: $\lambda = \pm \frac{1}{2}$
> 
> Para $\lambda = \frac{1}{2}$: $x = y$
> 
> Con restricción: $2x^2 = 1$ → $x = \frac{1}{\sqrt{2}}$
> 
> **Puntos críticos:** $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ y $\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$
> 
> **Valor máximo:** $f = \frac{1}{2}$

### Aplicación 2: Superficies de Nivel

> [!example]- 🏔️ Geometría Diferencial
> 
> **Teorema:** Si $F \in C^1$ y $\nabla F(\vec{a}) \neq \vec{0}$, entonces la superficie de nivel
> 
> $$S = {\vec{x} : F(\vec{x}) = c}$$
> 
> que pasa por $\vec{a}$ (donde $F(\vec{a}) = c$) es una superficie suave cerca de $\vec{a}$.
> 
> **Vector normal:** $\nabla F(\vec{a})$ es perpendicular a $S$ en $\vec{a}$.
> 
> ---
> 
> **Ejemplo:** Esfera
> 
> $$F(x,y,z) = x^2 + y^2 + z^2$$
> 
> Superficie de nivel: $x^2 + y^2 + z^2 = R^2$
> 
> $$\nabla F = (2x, 2y, 2z)$$
> 
> En cualquier punto $(x_0, y_0, z_0)$ de la esfera:
> 
> $$\nabla F(x_0,y_0,z_0) = 2(x_0, y_0, z_0)$$
> 
> Apunta radialmente hacia afuera (perpendicular a la esfera). ✓

### Aplicación 3: Ecuaciones Diferenciales

> [!example]- 📊 Existencia y Unicidad
> 
> **Teorema de Existencia (Picard-Lindelöf):**
> 
> Para el problema de valor inicial:
> 
> $$\frac{d\vec{x}}{dt} = \vec{F}(t, \vec{x}), \quad \vec{x}(t_0) = \vec{x}_0$$
> 
> Si $\vec{F} \in C^1$, entonces existe solución única local.
> 
> **Demostración:** Usa el teorema de la función implícita en forma integral (teorema del punto fijo).
> 
> ---
> 
> **Aplicación práctica:**
> 
> Sistema: $\begin{cases} \frac{dx}{dt} = y \ \frac{dy}{dt} = -x \end{cases}$
> 
> $$\vec{F}(x,y) = \begin{bmatrix} y \ -x \end{bmatrix}$$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix}$$
> 
> Como $\vec{F} \in C^1(\mathbb{R}^2)$, existe solución única para cualquier condición inicial.
> 
> Solución: $x(t) = A\cos(t) + B\sin(t)$, $y(t) = -A\sin(t) + B\cos(t)$

### Aplicación 4: Análisis Numérico

> [!example]- 💻 Método de Newton-Raphson
> 
> **Problema:** Resolver $\vec{F}(\vec{x}) = \vec{0}$
> 
> **Método iterativo:**
> 
> $$\vec{x}_{n+1} = \vec{x}_n - [J_{\vec{F}}(\vec{x}_n)]^{-1} \vec{F}(\vec{x}_n)$$
> 
> **Convergencia garantizada:**
> 
> Por el teorema de la función inversa, si:
> 
> - $\vec{F} \in C^1$
> - $\det(J_{\vec{F}}(\vec{x}^_)) \neq 0$ en la solución $\vec{x}^_$
> - $\vec{x}_0$ suficientemente cerca de $\vec{x}^*$
> 
> Entonces el método converge cuadráticamente.
> 
> ---
> 
> **Ejemplo:** Resolver
> 
> $$\begin{cases} x^2 + y^2 - 5 = 0 \ xy - 2 = 0 \end{cases}$$
> 
> $$\vec{F}(x,y) = \begin{bmatrix} x^2 + y^2 - 5 \ xy - 2 \end{bmatrix}$$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & 2y \ y & x \end{bmatrix}$$
> 
> En la solución $(2, 1)$:
> 
> $$J_{\vec{F}}(2,1) = \begin{bmatrix} 4 & 2 \ 1 & 2 \end{bmatrix}$$
> 
> $$\det(J_{\vec{F}}(2,1)) = 8 - 2 = 6 \neq 0$$ ✅
> 
> El método de Newton convergerá cerca de esta solución.

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Verificar diferenciabilidad:**
> 
> Determinar si las siguientes funciones son C¹ y por tanto diferenciables:
> 
> a) $f(x,y) = x^3 + y^3 - 3xy$
> 
> b) $f(x,y) = e^{x^2-y^2}$
> 
> c) $f(x,y) = \begin{cases} \frac{x^2y}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$
> 
> d) $f(x,y) = |x| + |y|$
> 
> ---
> 
> **2. Función implícita simple:**
> 
> Para cada ecuación, determinar si se puede despejar $y$ en función de $x$ cerca del punto dado:
> 
> a) $x^2 + y^2 = 4$ en $(1, \sqrt{3})$
> 
> b) $x^3 + y^3 = 6xy$ en $(0, 0)$
> 
> c) $e^{xy} - x - y = 1$ en $(0, 0)$
> 
> ---
> 
> **3. Derivadas implícitas:**
> 
> Calcular $\frac{dy}{dx}$ usando la fórmula implícita:
> 
> a) $x^2 + y^2 = 25$ en el punto $(3, 4)$
> 
> b) $x^3 + y^3 = 6xy$ en el punto $(1, 1)$ (si es posible)
> 
> c) $\sin(xy) + \cos(x+y) = 1$ en el punto $(0, 0)$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Teorema de la función inversa:**
> 
> Para cada transformación, determinar dónde es localmente invertible:
> 
> a) $\vec{F}(x,y) = \begin{bmatrix} x + y \ xy \end{bmatrix}$
> 
> b) $\vec{F}(x,y) = \begin{bmatrix} e^x\cos y \ e^x\sin y \end{bmatrix}$
> 
> c) $\vec{F}(r,\theta) = \begin{bmatrix} r^2\cos\theta \ r^2\sin\theta \end{bmatrix}$
> 
> ---
> 
> **5. Función implícita en 3D:**
> 
> Para $F(x,y,z) = x^2 + y^2 - z^2 = 0$ (cono):
> 
> a) ¿Podemos despejar $z$ cerca de $(1, 0, 1)$?
> 
> b) ¿Podemos despejar $z$ cerca de $(0, 0, 0)$?
> 
> c) Calcular $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$ en $(1, 0, 1)$
> 
> ---
> 
> **6. Sistema implícito:**
> 
> Para el sistema: $$\begin{cases} x^2 + y^2 + z^2 = 9 \ x + y + z = 3 \end{cases}$$
> 
> a) Verificar que $(1, 1, 1)$ es solución
> 
> b) ¿Podemos despejar $(y, z)$ en función de $x$ cerca de este punto?
> 
> c) Calcular la Jacobiana de la función implícita

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Demostración:**
> 
> Demostrar que si $f \in C^1$ y $\nabla f(\vec{a}) \neq \vec{0}$, entonces la superficie de nivel que pasa por $\vec{a}$ tiene vector normal $\nabla f(\vec{a})$.
> 
> ---
> 
> **8. Multiplicadores de Lagrange:**
> 
> Usar el teorema de la función implícita para justificar el método de multiplicadores de Lagrange en:
> 
> **Maximizar:** $f(x,y,z) = xyz$
> 
> **Sujeto a:** $x + y + z = 3$ y $x^2 + y^2 + z^2 = 5$
> 
> ---
> 
> **9. Análisis de singularidades:**
> 
> Para $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$:
> 
> a) Encontrar todos los puntos singulares (donde $\det(J_{\vec{F}}) = 0$)
> 
> b) En los puntos no singulares, ¿existe inversa local?
> 
> c) Analizar el comportamiento cerca de los puntos singulares
> 
> ---
> 
> **10. Aplicación:**
> 
> Una superficie está dada implícitamente por:
> 
> $$F(x,y,z) = x^3 + y^3 + z^3 - 3xyz - 1 = 0$$
> 
> a) ¿En qué puntos se puede despejar $z$ como función de $(x,y)$?
> 
> b) Encontrar la ecuación del plano tangente en el punto $(1, 0, 0)$
> 
> c) Calcular $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$ en ese punto

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = x^3 + y^3 - 3xy$
> 
> $$f_x = 3x^2 - 3y, \quad f_y = 3y^2 - 3x$$
> 
> Ambas son polinomios → continuas en $\mathbb{R}^2$
> 
> $$\boxed{f \in C^1(\mathbb{R}^2)}$$ → diferenciable
> 
> ---
> 
> **1c)** $f(x,y) = \begin{cases} \frac{x^2y}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$
> 
> En el origen:
> 
> $$f_x(0,0) = \lim_{h \to 0} \frac{0}{h} = 0$$
> 
> $$f_y(0,0) = \lim_{k \to 0} \frac{0}{k} = 0$$
> 
> Fuera del origen:
> 
> $$f_x(x,y) = \frac{2xy^3}{(x^2+y^2)^2}$$
> 
> $$\lim_{(x,y) \to (0,0)} f_x(x,y)$$ depende de la dirección
> 
> $$\boxed{f \notin C^1} \text{ cerca del origen}$$
> 
> ---
> 
> **2a)** $x^2 + y^2 = 4$ en $(1, \sqrt{3})$
> 
> $$F(x,y) = x^2 + y^2 - 4$$
> 
> $$F_y = 2y$$
> 
> En $(1, \sqrt{3})$: $F_y = 2\sqrt{3} \neq 0$ ✅
> 
> **Sí se puede despejar:** $y = \sqrt{4-x^2}$ cerca de $x=1$
> 
> ---
> 
> **3a)** $x^2 + y^2 = 25$ en $(3, 4)$
> 
> $$\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{2x}{2y} = -\frac{x}{y}$$
> 
> En $(3,4)$:
> 
> $$\boxed{\frac{dy}{dx} = -\frac{3}{4}}$$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $\vec{F}(x,y) = \begin{bmatrix} x + y \ xy \end{bmatrix}$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 1 & 1 \ y & x \end{bmatrix}$$
> 
> $$\det(J_{\vec{F}}) = x - y$$
> 
> Localmente invertible cuando $x \neq y$
> 
> $$\boxed{\text{Invertible en } {(x,y) : x \neq y}}$$
> 
> ---
> 
> **5.** $F(x,y,z) = x^2 + y^2 - z^2 = 0$
> 
> **a)** En $(1, 0, 1)$:
> 
> $$F_z = -2z = -2 \neq 0$$ ✅
> 
> Sí se puede despejar $z$
> 
> **b)** En $(0, 0, 0)$:
> 
> $$F_z = 0$$ ❌
> 
> No se puede despejar $z$ (el cono tiene singularidad)
> 
> **c)** En $(1, 0, 1)$:
> 
> $$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z} = -\frac{2x}{-2z} = \frac{x}{z} = \frac{1}{1} = 1$$
> 
> $$\frac{\partial z}{\partial y} = -\frac{F_y}{F_z} = \frac{2y}{-2z} = -\frac{y}{z} = 0$$
> 
> ---
> 
> **6.** Sistema en $(1, 1, 1)$:
> 
> $$\vec{F}(x,y,z) = \begin{bmatrix} x^2 + y^2 + z^2 - 9 \ x + y + z - 3 \end{bmatrix}$$
> 
> **a)** $\vec{F}(1,1,1) = \begin{bmatrix} 3 - 9 \ 3 - 3 \end{bmatrix} = \begin{bmatrix} -6 \ 0 \end{bmatrix}$
> 
> No es solución. Error en el enunciado. Probemos $(2, 1, 0)$:
> 
> $\vec{F}(2,1,0) = \begin{bmatrix} 5 - 9 \ 3 - 3 \end{bmatrix}$ tampoco.
> 
> Solución correcta: buscar puntos que satisfagan ambas ecuaciones.

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **9a)** $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & -2y \ 2y & 2x \end{bmatrix}$$
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
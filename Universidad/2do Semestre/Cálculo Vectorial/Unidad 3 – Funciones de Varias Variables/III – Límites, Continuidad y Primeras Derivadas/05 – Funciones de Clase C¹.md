# 📘 Funciones de Clase C¹

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Funciones de Clase C¹?
> 
> Hasta ahora hemos trabajado con derivadas parciales y el gradiente, pero surge una pregunta crucial: **¿cuándo podemos estar seguros de que la fórmula de la derivada direccional funciona?** La respuesta está en las funciones de clase C¹.
> 
> **Motivación:**
> 
> - Derivadas parciales pueden existir sin que la función sea diferenciable
> - Necesitamos condiciones que **garanticen** diferenciabilidad
> - Las funciones C¹ proporcionan esa garantía
> - Son la "regularidad mínima" para hacer cálculo multivariable con confianza
> 
> **El problema:**
> 
> Pueden existir funciones donde:
> 
> - ✅ Existen $f_x$ y $f_y$ en un punto
> - ✅ Existe el gradiente $\nabla f$
> - ❌ Pero la función NO es diferenciable
> - ❌ La fórmula $D_{\vec{u}}f = \nabla f \cdot \vec{u}$ FALLA
> 
> **La solución: Clase C¹**
> 
> Si las derivadas parciales son **continuas**, entonces:
> 
> - ✅ La función ES diferenciable
> - ✅ Todas las fórmulas funcionan
> - ✅ Podemos trabajar con confianza

---

## 📋 Definición de Función de Clase C¹

### 📝 Definición Formal

> [!example]- 🟢 Definición: Función de Clase C¹
> 
> **Definición:** Una función $f: \mathbb{R}^n \to \mathbb{R}$ es de **clase C¹** en un conjunto abierto $U$ si:
> 
> 1. Todas sus **derivadas parciales** $\frac{\partial f}{\partial x_i}$ **existen** en $U$
> 2. Todas sus derivadas parciales son **continuas** en $U$
> 
> **Notación:** $$f \in C^1(U)$$
> 
> ---
> 
> **En dos variables:** $f(x,y)$ es de clase C¹ en $U$ si:
> 
> $$\frac{\partial f}{\partial x} \text{ y } \frac{\partial f}{\partial y} \text{ existen y son continuas en } U$$
> 
> ---
> 
> **En tres variables:** $f(x,y,z)$ es de clase C¹ en $U$ si:
> 
> $$\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \text{ existen y son continuas en } U$$
> 
> ---
> 
> **Interpretación:**
> 
> - C¹ = "Continuamente diferenciable una vez"
> - Las derivadas no solo existen, sino que **no tienen saltos**
> - Es una condición de "suavidad" o "regularidad"
> 
> ---
> 
> **Observaciones importantes:**
> 
> - La continuidad de las derivadas parciales es lo que diferencia C¹ de simplemente "tener derivadas parciales"
> - C¹ es una propiedad **local**: puede cumplirse en un conjunto abierto pero no en todo $\mathbb{R}^n$
> - Si $f \in C^1$ en un punto, entonces $f$ es diferenciable en ese punto

### 🎯 ¿Por qué "C¹"?

> [!note]- 📖 Nomenclatura y Jerarquía
> 
> La notación "C" viene de **"continua"** (continuous):
> 
> ### Jerarquía de Regularidad
> 
> **C⁰:** Funciones **continuas**
> 
> - $f$ es continua
> - Sin derivadas requeridas
> 
> **C¹:** Funciones **continuamente diferenciables**
> 
> - $f$ es continua
> - Derivadas parciales existen y son continuas
> - **Este es nuestro tema**
> 
> **C²:** Funciones **dos veces continuamente diferenciables**
> 
> - $f$ es C¹
> - Derivadas parciales de segundo orden existen y son continuas
> - Ejemplo: $f_{xx}, f_{xy}, f_{yy}$ continuas
> 
> **C³, C⁴, ..., Cⁿ:** Generalización natural
> 
> **C∞:** Funciones **infinitamente diferenciables**
> 
> - Todas las derivadas de todos los órdenes existen y son continuas
> - También llamadas funciones "suaves" (smooth)
> 
> ---
> 
> **Inclusiones:**
> 
> $$C^\infty \subset \cdots \subset C^3 \subset C^2 \subset C^1 \subset C^0$$
> 
> Cada clase está contenida en la anterior (más regular ⊂ menos regular)

---

## 🔑 Teorema Fundamental: C¹ Implica Diferenciabilidad

> [!example]- 🟢 Teorema Principal
> 
> **Teorema:** Si $f$ es de clase C¹ en un abierto $U$ que contiene al punto $\vec{a}$, entonces $f$ es **diferenciable** en $\vec{a}$.
> 
> **En dos variables:** Si $f \in C^1$ en un entorno de $(a,b)$, entonces:
> 
> $$f(a+h, b+k) = f(a,b) + f_x(a,b) \cdot h + f_y(a,b) \cdot k + \epsilon(h,k)$$
> 
> donde $\lim_{(h,k) \to (0,0)} \frac{\epsilon(h,k)}{\sqrt{h^2+k^2}} = 0$
> 
> ---
> 
> **Consecuencias importantes:**
> 
> 1. **Fórmula del gradiente funciona:** $$D_{\vec{u}}f = \nabla f \cdot \vec{u}$$
>     
> 2. **Existe plano tangente:** $$z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$
>     
> 3. **Regla de la cadena funciona** (próximo tema)
>     
> 4. **La función es continua:** $$\lim_{(x,y) \to (a,b)} f(x,y) = f(a,b)$$
>     
> 
> ---
> 
> **Importancia práctica:**
> 
> ✅ Si verificamos que $f \in C^1$, podemos usar TODAS las fórmulas del cálculo multivariable con confianza.
> 
> ❌ Sin C¹, debemos verificar diferenciabilidad caso por caso (más difícil).

---

## 📊 Ejemplos: Identificando Funciones C¹

### Ejemplo 1: Polinomios

> [!example]- 📝 Ejemplo 1: Los Polinomios son C∞
> 
> **Función:** $$f(x,y) = x^3 + 2x^2y + xy^2 + y^3$$
> 
> **Pregunta:** ¿Es $f \in C^1(\mathbb{R}^2)$?
> 
> ---
> 
> **Solución:**
> 
> **Paso 1: Calcular derivadas parciales**
> 
> $$\frac{\partial f}{\partial x} = 3x^2 + 4xy + y^2$$
> 
> $$\frac{\partial f}{\partial y} = 2x^2 + 2xy + 3y^2$$
> 
> ---
> 
> **Paso 2: ¿Son continuas?**
> 
> Ambas derivadas parciales son **polinomios**, y los polinomios son continuos en todo $\mathbb{R}^2$.
> 
> $$\boxed{f \in C^1(\mathbb{R}^2)}$$
> 
> De hecho, como todas las derivadas de todos los órdenes son polinomios:
> 
> $$\boxed{f \in C^\infty(\mathbb{R}^2)}$$
> 
> ---
> 
> **Conclusión general:**
> 
> ✅ **Todo polinomio es C∞**

### Ejemplo 2: Funciones Exponenciales

> [!example]- 📝 Ejemplo 2: Exponenciales
> 
> **Función:** $$f(x,y) = e^{x+y} + e^{xy}$$
> 
> **Pregunta:** ¿Es $f \in C^1(\mathbb{R}^2)$?
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial f}{\partial x} = e^{x+y} + ye^{xy}$$
> 
> $$\frac{\partial f}{\partial y} = e^{x+y} + xe^{xy}$$
> 
> ---
> 
> **Continuidad:**
> 
> - La función exponencial $e^u$ es continua para todo $u$
> - Composiciones y sumas de funciones continuas son continuas
> - Por tanto, $f_x$ y $f_y$ son continuas en $\mathbb{R}^2$
> 
> $$\boxed{f \in C^1(\mathbb{R}^2)}$$
> 
> De hecho: $$\boxed{f \in C^\infty(\mathbb{R}^2)}$$
> 
> ---
> 
> **Regla general:**
> 
> ✅ **Funciones exponenciales, trigonométricas, y sus composiciones son típicamente C∞**

### Ejemplo 3: Funciones Racionales

> [!example]- 📝 Ejemplo 3: Con Singularidades
> 
> **Función:** $$f(x,y) = \frac{x^2 + y^2}{x^2 + y^2 + 1}$$
> 
> **Pregunta:** ¿Dónde es $f \in C^1$?
> 
> ---
> 
> **Derivadas parciales:**
> 
> Usando regla del cociente:
> 
> $$\frac{\partial f}{\partial x} = \frac{2x(x^2 + y^2 + 1) - (x^2 + y^2) \cdot 2x}{(x^2 + y^2 + 1)^2}$$
> 
> $$= \frac{2x(1)}{(x^2 + y^2 + 1)^2} = \frac{2x}{(x^2 + y^2 + 1)^2}$$
> 
> Similarmente:
> 
> $$\frac{\partial f}{\partial y} = \frac{2y}{(x^2 + y^2 + 1)^2}$$
> 
> ---
> 
> **Continuidad:**
> 
> - El denominador $x^2 + y^2 + 1 \geq 1 > 0$ para todo $(x,y)$
> - Nunca se anula
> - Por tanto, $f_x$ y $f_y$ son continuas en **todo** $\mathbb{R}^2$
> 
> $$\boxed{f \in C^1(\mathbb{R}^2)}$$
> 
> ---
> 
> **Regla general:**
> 
> Una función racional $\frac{P(x,y)}{Q(x,y)}$ es C¹ en todos los puntos donde $Q(x,y) \neq 0$

### Ejemplo 4: Valor Absoluto

> [!example]- 📝 Ejemplo 4: NO es C¹ (pero derivadas existen)
> 
> **Función:** $$f(x,y) = |x| + |y|$$
> 
> **Pregunta:** ¿Es $f \in C^1(\mathbb{R}^2)$?
> 
> ---
> 
> **Análisis en el origen $(0,0)$:**
> 
> **Derivada parcial respecto a $x$:**
> 
> $$\frac{\partial f}{\partial x}(0,0) = \lim_{h \to 0} \frac{f(h,0) - f(0,0)}{h} = \lim_{h \to 0} \frac{|h|}{h}$$
> 
> Este límite **no existe** (es $+1$ si $h>0$ y $-1$ si $h<0$).
> 
> ---
> 
> **Análisis fuera del origen:**
> 
> Para $(x,y) \neq (0,0)$ donde $x \neq 0$ y $y \neq 0$:
> 
> $$f_x(x,y) = \text{sgn}(x), \quad f_y(x,y) = \text{sgn}(y)$$
> 
> donde $\text{sgn}$ es la función signo ($+1$ si positivo, $-1$ si negativo).
> 
> ---
> 
> **Continuidad de las derivadas:**
> 
> La función $\text{sgn}(x)$ es **discontinua** en $x=0$.
> 
> Por ejemplo:
> 
> - $\lim_{x \to 0^+} f_x(x,y) = +1$
> - $\lim_{x \to 0^-} f_x(x,y) = -1$
> 
> Las derivadas parciales **no son continuas** en los ejes.
> 
> $$\boxed{f \notin C^1(\mathbb{R}^2)}$$
> 
> ---
> 
> **Conclusión:**
> 
> ❌ $f(x,y) = |x| + |y|$ NO es de clase C¹ en ningún entorno que contenga los ejes coordenados.
> 
> ✅ Es C¹ en cada uno de los cuatro cuadrantes abiertos (donde $x \neq 0$ y $y \neq 0$).

### Ejemplo 5: Caso Patológico Importante

> [!example]- 📝 Ejemplo 5: Derivadas Existen pero NO es Diferenciable
> 
> **Función:**
> 
> $$f(x,y) = \begin{cases} \frac{xy}{\sqrt{x^2+y^2}} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **Pregunta:** ¿Es $f$ diferenciable en $(0,0)$? ¿Es C¹?
> 
> ---
> 
> **Paso 1: Verificar que existen derivadas parciales en $(0,0)$**
> 
> $$f_x(0,0) = \lim_{h \to 0} \frac{f(h,0) - f(0,0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$$
> 
> $$f_y(0,0) = \lim_{k \to 0} \frac{f(0,k) - f(0,0)}{k} = \lim_{k \to 0} \frac{0 - 0}{k} = 0$$
> 
> ✅ Las derivadas parciales existen: $\nabla f(0,0) = (0,0)$
> 
> ---
> 
> **Paso 2: Verificar diferenciabilidad**
> 
> Si $f$ fuera diferenciable, la aproximación lineal sería:
> 
> $$f(h,k) \approx f(0,0) + f_x(0,0) \cdot h + f_y(0,0) \cdot k = 0$$
> 
> El error debería cumplir:
> 
> $$\lim_{(h,k) \to (0,0)} \frac{f(h,k) - 0}{\sqrt{h^2+k^2}} = \lim_{(h,k) \to (0,0)} \frac{hk/(h^2+k^2)^{1/2}}{\sqrt{h^2+k^2}} = \lim_{(h,k) \to (0,0)} \frac{hk}{h^2+k^2}$$
> 
> **Probar con $h=k=t$:**
> 
> $$\lim_{t \to 0} \frac{t \cdot t}{t^2 + t^2} = \lim_{t \to 0} \frac{t^2}{2t^2} = \frac{1}{2} \neq 0$$
> 
> ❌ El límite **no es cero**, por tanto $f$ NO es diferenciable en $(0,0)$.
> 
> ---
> 
> **Paso 3: ¿Es C¹?**
> 
> Para $(x,y) \neq (0,0)$, usando regla del cociente:
> 
> $$f_x(x,y) = \frac{y \cdot \sqrt{x^2+y^2} - xy \cdot \frac{x}{\sqrt{x^2+y^2}}}{x^2+y^2} = \frac{y^3}{(x^2+y^2)^{3/2}}$$
> 
> **Continuidad en el origen:**
> 
> $$\lim_{(x,y) \to (0,0)} f_x(x,y) = \lim_{(x,y) \to (0,0)} \frac{y^3}{(x^2+y^2)^{3/2}}$$
> 
> En coordenadas polares ($x = r\cos\theta, y = r\sin\theta$):
> 
> $$= \lim_{r \to 0} \frac{r^3\sin^3\theta}{r^3} = \sin^3\theta$$
> 
> Este límite **depende de la dirección** $\theta$, por tanto no existe.
> 
> $$\boxed{f_x \text{ es discontinua en } (0,0)}$$
> 
> ---
> 
> **Conclusión:**
> 
> ✅ Derivadas parciales existen en $(0,0)$
> 
> ❌ Derivadas parciales NO son continuas en $(0,0)$
> 
> ❌ $f \notin C^1$ en ningún entorno de $(0,0)$
> 
> ❌ $f$ NO es diferenciable en $(0,0)$
> 
> ---
> 
> **Moraleja:**
> 
> Este ejemplo muestra que:
> 
> - Existencia de $\nabla f$ **NO implica** diferenciabilidad
> - **C¹ SÍ implica** diferenciabilidad
> - La continuidad de las derivadas es crucial

---

## 🧮 Criterio Práctico: ¿Cómo Verificar C¹?

> [!note]- 🔍 Estrategia para Verificar C¹
> 
> ### Algoritmo Práctico
> 
> Para verificar si $f \in C^1(U)$:
> 
> **Paso 1:** Calcular todas las derivadas parciales
> 
> - $\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \ldots$
> 
> **Paso 2:** Identificar posibles puntos problemáticos
> 
> - Denominadores que se anulan
> - Discontinuidades
> - Puntos donde cambia la definición
> 
> **Paso 3:** Verificar continuidad de las derivadas
> 
> - En puntos "normales": usar composición de funciones continuas
> - En puntos problemáticos: calcular límites
> 
> **Paso 4:** Concluir
> 
> - Si todas las derivadas son continuas en $U$: $f \in C^1(U)$
> - Si alguna es discontinua en un punto de $U$: $f \notin C^1(U)$
> 
> ---
> 
> ### Atajos Útiles
> 
> **✅ Son automáticamente C∞:**
> 
> - Polinomios
> - Funciones exponenciales $e^{g(x,y)}$ donde $g$ es C∞
> - Funciones trigonométricas $\sin(g), \cos(g)$ donde $g$ es C∞
> - Logaritmos $\ln(g)$ donde $g > 0$ y $g$ es C∞
> 
> **✅ Composiciones y operaciones:**
> 
> - Si $f, g \in C^1$ entonces $f+g, f \cdot g, f/g$ (donde $g \neq 0$) están en C¹
> - Si $f \in C^1$ y $g \in C^1$ entonces $f \circ g \in C^1$ (con dominio apropiado)
> 
> **⚠️ Sospechosos comunes (verificar):**
> 
> - Valor absoluto $|x|, |y|$
> - Raíces $\sqrt{x}, \sqrt{x^2+y^2}$
> - Funciones definidas por casos
> - Cocientes donde el denominador puede anularse

---

## 📚 Ejemplos de Verificación Detallada

### Ejemplo 6: Raíz Cuadrada

> [!example]- 📝 Ejemplo 6: Función Raíz
> 
> **Función:** $$f(x,y) = \sqrt{x^2 + y^2}$$
> 
> **Pregunta:** ¿Dónde es $f \in C^1$?
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial f}{\partial x} = \frac{x}{\sqrt{x^2+y^2}}$$
> 
> $$\frac{\partial f}{\partial y} = \frac{y}{\sqrt{x^2+y^2}}$$
> 
> ---
> 
> **Análisis de continuidad:**
> 
> **Para $(x,y) \neq (0,0)$:**
> 
> - El denominador $\sqrt{x^2+y^2} > 0$
> - Ambas derivadas son continuas
> 
> **En $(0,0)$:**
> 
> - Las derivadas **no están definidas** (división por cero)
> 
> ---
> 
> **Verificación en el origen:**
> 
> Usando la definición:
> 
> $$f_x(0,0) = \lim_{h \to 0} \frac{\sqrt{h^2} - 0}{h} = \lim_{h \to 0} \frac{|h|}{h}$$
> 
> Este límite no existe.
> 
> ---
> 
> **Conclusión:**
> 
> $$\boxed{f \in C^1(\mathbb{R}^2 \setminus {(0,0)})}$$
> 
> - Es C¹ en todo $\mathbb{R}^2$ **excepto** el origen
> - En el origen, ni siquiera es diferenciable

### Ejemplo 7: Función por Casos

> [!example]- 📝 Ejemplo 7: Definición por Casos
> 
> **Función:**
> 
> $$f(x,y) = \begin{cases} x^2 + y^2 & \text{si } x^2 + y^2 \leq 1 \ 2\sqrt{x^2+y^2} - 1 & \text{si } x^2 + y^2 > 1 \end{cases}$$
> 
> **Pregunta:** ¿Es $f \in C^1(\mathbb{R}^2)$?
> 
> ---
> 
> **Paso 1: Derivadas en el interior de cada región**
> 
> **Región 1:** $x^2 + y^2 < 1$
> 
> $$f_x = 2x, \quad f_y = 2y$$
> 
> (continuas en el interior)
> 
> **Región 2:** $x^2 + y^2 > 1$
> 
> $$f_x = \frac{2x}{\sqrt{x^2+y^2}}, \quad f_y = \frac{2y}{\sqrt{x^2+y^2}}$$
> 
> (continuas en el interior)
> 
> ---
> 
> **Paso 2: Verificar en la frontera $x^2 + y^2 = 1$**
> 
> Tomemos un punto en el círculo unitario, digamos $(1, 0)$.
> 
> **Desde el interior ($r < 1$):**
> 
> $$\lim_{x \to 1^-} f_x(x,0) = 2 \cdot 1 = 2$$
> 
> **Desde el exterior ($r > 1$):**
> 
> $$\lim_{x \to 1^+} f_x(x,0) = \frac{2 \cdot 1}{\sqrt{1}} = 2$$
> 
> ✅ Los límites coinciden.
> 
> **Derivada en $(1,0)$ por definición:**
> 
> $$f_x(1,0) = \lim_{h \to 0} \frac{f(1+h,0) - f(1,0)}{h}$$
> 
> - $f(1,0) = 2\sqrt{1} - 1 = 1$
> - Para $h$ pequeño negativo: $f(1+h,0) = (1+h)^2$
> - Para $h$ pequeño positivo: $f(1+h,0) = 2\sqrt{(1+h)^2} - 1 = 2|1+h| - 1$
> 
> Calculando límites laterales ambos dan $2$.
> 
> $$f_x(1,0) = 2$$
> 
> ---
> 
> **Paso 3: Continuidad de $f_x$ en $(1,0)$**
> 
> Hemos mostrado:
> 
> - $f_x(1,0) = 2$
> - $\lim_{(x,y) \to (1,0)} f_x(x,y) = 2$ (desde ambos lados)
> 
> ✅ $f_x$ es continua en $(1,0)$
> 
> Por simetría, esto vale en todo el círculo unitario.
> 
> ---
> 
> **Conclusión:**
> 
> $$\boxed{f \in C^1(\mathbb{R}^2)}$$
> 
> Las derivadas parciales son continuas en **todo** $\mathbb{R}^2$, incluyendo la frontera.

### Ejemplo 8: Logaritmo

> [!example]- 📝 Ejemplo 8: Con Logaritmo
> 
> **Función:** $$f(x,y) = \ln(1 + x^2 + y^2)$$
> 
> **Pregunta:** ¿Es $f \in C^1(\mathbb{R}^2)$?
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial f}{\partial x} = \frac{2x}{1 + x^2 + y^2}$$
> 
> $$\frac{\partial f}{\partial y} = \frac{2y}{1 + x^2 + y^2}$$
> 
> ---
> 
> **Análisis:**
> 
> - El denominador $1 + x^2 + y^2 \geq 1 > 0$ para todo $(x,y)$
> - Nunca se anula
> - Las derivadas son cocientes de funciones continuas con denominador no nulo
> 
> $$\boxed{f \in C^1(\mathbb{R}^2)}$$
> 
> De hecho, $f \in C^\infty(\mathbb{R}^2)$.

---

## 🎯 Propiedades de las Funciones C¹

> [!note]- ⭐ Propiedades Algebraicas
> 
> ### 1. Linealidad
> 
> Si $f, g \in C^1(U)$ y $\alpha, \beta \in \mathbb{R}$, entonces:
> 
> $$\alpha f + \beta g \in C^1(U)$$
> 
> **Demostración:**
> 
> $$\frac{\partial}{\partial x}(\alpha f + \beta g) = \alpha \frac{\partial f}{\partial x} + \beta \frac{\partial g}{\partial x}$$
> 
> Suma de funciones continuas es continua. ✓
> 
> ---
> 
> ### 2. Producto
> 
> Si $f, g \in C^1(U)$, entonces:
> 
> $$f \cdot g \in C^1(U)$$
> 
> **Demostración:**
> 
> $$\frac{\partial}{\partial x}(fg) = f \frac{\partial g}{\partial x} + g \frac{\partial f}{\partial x}$$
> 
> Suma y producto de funciones continuas es continua. ✓
> 
> ---
> 
> ### 3. Cociente
> 
> Si $f, g \in C^1(U)$ y $g(x,y) \neq 0$ en $U$, entonces:
> 
> $$\frac{f}{g} \in C^1(U)$$
> 
> **Demostración:**
> 
> $$\frac{\partial}{\partial x}\left(\frac{f}{g}\right) = \frac{g \frac{\partial f}{\partial x} - f \frac{\partial g}{\partial x}}{g^2}$$
> Como $g \neq 0$ en $U$ y $f, g$ son C¹, esta expresión es continua. ✓
> 
> ---
> 
> ### 4. Composición (Regla de la Cadena)
> 
> Si $f \in C^1(V)$ y $g: U \to V$ con $g \in C^1(U)$, entonces:
> 
> $$h = f \circ g \in C^1(U)$$
> 
> **Ejemplo:** Si $f(u,v) = u^2 + v^2$ y $g(x,y) = (x+y, xy)$, entonces:
> 
> $$h(x,y) = f(g(x,y)) = (x+y)^2 + (xy)^2$$
> 
> es C¹ porque es composición de funciones C¹.
> 
> ---
> 
> ### 5. Continuidad
> 
> Si $f \in C^1(U)$, entonces:
> 
> $$f \in C^0(U)$$
> 
> Es decir, **C¹ implica continuidad**.
> 
> **Demostración:** La diferenciabilidad (que sigue de C¹) implica continuidad.
> 
> ---
> 
> ### 6. Vector Gradiente
> 
> Si $f \in C^1(U)$, entonces la función:
> 
> $$\nabla f: U \to \mathbb{R}^n$$
> 
> que asigna a cada punto su gradiente, es **continua**.
> 
> **Interpretación:** El campo vectorial gradiente no tiene "saltos".
> 

---

## 🔄 Relación con Diferenciabilidad

> [!note]- 🔗 Diferenciabilidad vs C¹
> 
> ### Diagrama de Implicaciones
> 
> ```
> f ∈ C¹
>   ↓ (SIEMPRE)
> f es diferenciable
>   ↓ (SIEMPRE)
> Derivadas parciales existen
>   ↓ (SIEMPRE)
> f es continua
> ```
> 
> **Implicaciones inversas:**
> 
> ```
> f continua ⇏ Derivadas parciales existen
> Derivadas parciales existen ⇏ f diferenciable
> f diferenciable ⇏ f ∈ C¹
> ```
> 
> ---
> 
> ### Contraejemplos
> 
> **1. Continua pero sin derivadas parciales:**
> 
> $$f(x,y) = \begin{cases} \sqrt[3]{x^2} & \text{si } y = 0 \ 0 & \text{si } y \neq 0 \end{cases}$$
> 
> Continua en todas partes, pero $f_x(0,0)$ no existe.
> 
> ---
> 
> **2. Derivadas parciales existen pero no diferenciable:**
> 
> Ya vimos el Ejemplo 5: $f(x,y) = \frac{xy}{\sqrt{x^2+y^2}}$ (extendida por $0$ en el origen).
> 
> ---
> 
> **3. Diferenciable pero no C¹:**
> 
> $$f(x,y) = \begin{cases} (x^2+y^2)\sin\left(\frac{1}{\sqrt{x^2+y^2}}\right) & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> Se puede demostrar que:
> 
> - $f$ es diferenciable en $(0,0)$
> - $f_x$ y $f_y$ existen en todas partes
> - Pero $f_x$ y $f_y$ **no son continuas** en $(0,0)$
> 
> Por tanto: diferenciable pero $\notin C^1$.

---

## 🛠️ Aplicaciones de las Funciones C¹

### Aplicación 1: Teorema de la Función Implícita

> [!example]- 📐 Función Implícita
> 
> **Teorema:** Si $F(x,y) \in C^1$ y satisface:
> 
> 1. $F(x_0, y_0) = 0$
> 2. $\frac{\partial F}{\partial y}(x_0, y_0) \neq 0$
> 
> Entonces cerca de $(x_0, y_0)$, la ecuación $F(x,y) = 0$ define implícitamente a $y$ como función de $x$:
> 
> $$y = g(x)$$
> 
> donde $g \in C^1$.
> 
> ---
> 
> **Ejemplo:**
> 
> **Ecuación:** $$F(x,y) = x^2 + y^2 - 1 = 0$$
> 
> (círculo unitario)
> 
> **Verificar C¹:**
> 
> $$F_x = 2x, \quad F_y = 2y$$
> 
> Ambas continuas, así que $F \in C^1(\mathbb{R}^2)$. ✓
> 
> **En el punto $(0,1)$:**
> 
> - $F(0,1) = 0$ ✓
> - $F_y(0,1) = 2 \neq 0$ ✓
> 
> Por el teorema, cerca de $(0,1)$, podemos despejar:
> 
> $$y = g(x) = \sqrt{1-x^2}$$
> 
> y esta función es C¹ cerca de $x=0$.
> 
> ---
> 
> **Derivada de $g$:**
> 
> $$g'(x) = -\frac{F_x}{F_y} = -\frac{2x}{2y} = -\frac{x}{y}$$
> 
> En $(0,1)$: $g'(0) = 0$ ✓
> 
> **Importancia:** El requisito $F \in C^1$ es esencial para este teorema.

### Aplicación 2: Optimización con Restricciones

> [!example]- 🎯 Multiplicadores de Lagrange
> 
> **Problema:** Optimizar $f(x,y)$ sujeto a $g(x,y) = c$
> 
> **Método:** Si $f, g \in C^1$ y $\nabla g \neq \vec{0}$, los extremos ocurren donde:
> 
> $$\nabla f = \lambda \nabla g$$
> 
> para algún $\lambda \in \mathbb{R}$ (multiplicador de Lagrange).
> 
> ---
> 
> **Ejemplo:**
> 
> **Maximizar:** $f(x,y) = xy$
> 
> **Sujeto a:** $g(x,y) = x^2 + y^2 = 1$
> 
> **Verificar C¹:**
> 
> - $f \in C^1$ (polinomio) ✓
> - $g \in C^1$ (polinomio) ✓
> 
> **Gradientes:**
> 
> $$\nabla f = (y, x)$$ $$\nabla g = (2x, 2y)$$
> 
> **Condición:**
> 
> $$(y, x) = \lambda(2x, 2y)$$
> 
> Esto da: $y = 2\lambda x$ y $x = 2\lambda y$
> 
> Sustituyendo: $y = 2\lambda(2\lambda y) = 4\lambda^2 y$
> 
> Si $y \neq 0$: $4\lambda^2 = 1$, así que $\lambda = \pm \frac{1}{2}$
> 
> ---
> 
> **Solución:**
> 
> Para $\lambda = \frac{1}{2}$: $(x,y) = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$
> 
> $f\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) = \frac{1}{2}$ (máximo)
> 
> Para $\lambda = -\frac{1}{2}$: $(x,y) = \left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$
> 
> $f\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right) = \frac{1}{2}$ (máximo)
> 
> Los otros dos puntos críticos dan el mínimo $-\frac{1}{2}$.

### Aplicación 3: Ecuaciones Diferenciales Parciales

> [!example]- 🌊 Ecuación de Laplace
> 
> **Ecuación:** $$\Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = 0$$
> 
> (Ecuación de Laplace en 2D)
> 
> **Requisito:** Para que esta ecuación tenga sentido, necesitamos que $f \in C^2$.
> 
> Pero primero debemos verificar $f \in C^1$.
> 
> ---
> 
> **Ejemplo de solución:**
> 
> $$f(x,y) = x^2 - y^2$$
> 
> **Verificar C²:**
> 
> $$f_x = 2x, \quad f_y = -2y$$ (continuas, así que $f \in C^1$)
> 
> $$f_{xx} = 2, \quad f_{yy} = -2$$ (continuas, así que $f \in C^2$)
> 
> **Verificar que satisface la ecuación:**
> 
> $$\Delta f = 2 + (-2) = 0$$ ✓
> 
> ---
> 
> **Importancia:** Muchos teoremas de EDPs requieren $C^1$ o $C^2$ como hipótesis.

---

## 📊 Tabla Resumen: Clases de Funciones

> [!note]- 📋 Comparación de Regularidad
> 
> |Clase|Definición|Propiedades|Ejemplo|
> |---|---|---|---|
> |**Continua**|$\lim_{(x,y) \to (a,b)} f(x,y) = f(a,b)$|No hay saltos|$\|x\| + \|y\|$|
> |**Derivadas parciales existen**|$f_x, f_y$ existen|Puede no ser diferenciable|$\frac{xy}{\sqrt{x^2+y^2}}$|
> |**Diferenciable**|Aproximación lineal existe|Es continua, $\nabla f$ existe|Todas las C¹|
> |**C¹**|Derivadas parciales continuas|Es diferenciable, fórmulas funcionan|$x^2 + y^2$|
> |**C²**|Segundas derivadas continuas|Teorema de Schwarz aplica|Polinomios|
> |**C∞**|Todas las derivadas continuas|"Suave", muy regular|$e^{x+y}$|
> 
> ---
> 
> ### Jerarquía de Inclusión
> 
> $$\text{C}^\infty \subset \text{C}^2 \subset \text{C}^1 \subset \text{Diferenciable} \subset \text{Derivadas existen} \subset \text{Continua}$$

---

## 🧮 Teorema de Schwarz (Adelanto a C²)

> [!note]- 🔄 Igualdad de Derivadas Mixtas
> 
> **Teorema de Schwarz (o Clairaut):** Si $f \in C^2$ en un abierto $U$, entonces:
> 
> $$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$$
> 
> en todo punto de $U$.
> 
> **En otras palabras:** El orden de derivación no importa.
> 
> ---
> 
> **Ejemplo:**
> 
> $$f(x,y) = x^3y + xy^3$$
> 
> **Calcular $f_{xy}$:**
> 
> $$f_x = 3x^2y + y^3$$ $$f_{xy} = 3x^2 + 3y^2$$
> 
> **Calcular $f_{yx}$:**
> 
> $$f_y = x^3 + 3xy^2$$ $$f_{yx} = 3x^2 + 3y^2$$
> 
> $$\boxed{f_{xy} = f_{yx}}$$ ✓
> 
> ---
> 
> **Importancia de C²:**
> 
> - Sin $C^2$, las derivadas mixtas pueden **no ser iguales**
> - C² es la condición mínima para que el Hessiano sea simétrico
> - Crucial en teoría de optimización
> 
> ---
> 
> **Contraejemplo (sin C²):**
> 
> $$f(x,y) = \begin{cases} \frac{xy(x^2-y^2)}{x^2+y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> Se puede demostrar que en el origen:
> 
> $$f_{xy}(0,0) = 1, \quad f_{yx}(0,0) = -1$$
> 
> $$f_{xy}(0,0) \neq f_{yx}(0,0)$$
> 
> Y efectivamente, las segundas derivadas **no son continuas** en $(0,0)$.

---

## 🎯 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Identificar la clase:**
> 
> Para cada función, determinar si es C¹ en $\mathbb{R}^2$:
> 
> a) $f(x,y) = 3x^2 + 2xy + 5y^2$
> 
> b) $f(x,y) = e^{x^2+y^2}$
> 
> c) $f(x,y) = |x| \cdot y$
> 
> d) $f(x,y) = \sin(xy)$
> 
> e) $f(x,y) = \sqrt{|x| + |y|}$
> 
> ---
> 
> **2. Derivadas parciales:**
> 
> Para $f(x,y) = x^3 + y^3 - 3xy$:
> 
> a) Calcular $f_x$ y $f_y$
> 
> b) ¿Son continuas en $\mathbb{R}^2$?
> 
> c) ¿Es $f \in C^1(\mathbb{R}^2)$?
> 
> d) Calcular $f_{xx}, f_{yy}, f_{xy}, f_{yx}$
> 
> e) Verificar que $f_{xy} = f_{yx}$
> 
> ---
> 
> **3. Dominios de C¹:**
> 
> Para cada función, determinar el mayor conjunto abierto donde es C¹:
> 
> a) $f(x,y) = \frac{1}{x^2 + y^2}$
> 
> b) $f(x,y) = \ln(x^2 + y^2)$
> 
> c) $f(x,y) = \sqrt{x^2 + y^2}$
> 
> d) $f(x,y) = \frac{x-y}{x+y}$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Funciones por casos:**
> 
> Determinar si las siguientes funciones son C¹ en $\mathbb{R}^2$:
> 
> a) $$f(x,y) = \begin{cases} xy & \text{si } x \geq 0 \ 0 & \text{si } x < 0 \end{cases}$$
> 
> b) $$f(x,y) = \begin{cases} x^2y & \text{si } y \geq x^2 \ xy^2 & \text{si } y < x^2 \end{cases}$$
> 
> c) $$f(x,y) = \begin{cases} \frac{x^3}{x^2+y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> ---
> 
> **5. Diferenciabilidad vs C¹:**
> 
> Para $f(x,y) = \begin{cases} \frac{x^2y}{x^2+y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$
> 
> a) Calcular $f_x(0,0)$ y $f_y(0,0)$ usando la definición
> 
> b) Calcular $f_x(x,y)$ y $f_y(x,y)$ para $(x,y) \neq (0,0)$
> 
> c) Determinar si $f_x$ y $f_y$ son continuas en $(0,0)$
> 
> d) ¿Es $f$ diferenciable en $(0,0)$?
> 
> e) ¿Es $f \in C^1$ en algún entorno de $(0,0)$?
> 
> ---
> 
> **6. Aplicación a optimización:**
> 
> Verificar que $f(x,y) = x^3 - 3xy^2$ es C¹ y encontrar todos los puntos críticos (donde $\nabla f = \vec{0}$).

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Teoría:**
> 
> a) Demostrar que si $f, g \in C^1(U)$, entonces $f \cdot g \in C^1(U)$
> 
> b) Dar un ejemplo de $f$ diferenciable en $(0,0)$ pero que $f \notin C^1$ en ningún entorno de $(0,0)$
> 
> c) Demostrar que si $f \in C^1(\mathbb{R}^2)$ y $\nabla f = \vec{0}$ en todo punto, entonces $f$ es constante
> 
> ---
> 
> **8. Composición:**
> 
> Si $f(u,v) = u^2 + v^2$ y $g(x,y) = (e^x\cos y, e^x\sin y)$:
> 
> a) Verificar que $f, g \in C^1$
> 
> b) Calcular $h(x,y) = f(g(x,y))$ explícitamente
> 
> c) Verificar que $h \in C^1$
> 
> d) Calcular $\nabla h$ usando la regla de la cadena
> 
> ---
> 
> **9. Función implícita:**
> 
> Para $F(x,y) = x^3 + y^3 - 3xy$:
> 
> a) Verificar que $F \in C^1(\mathbb{R}^2)$
> 
> b) Verificar que $F(1,1) = -1$
> 
> c) Calcular $F_y(1,1)$
> 
> d) ¿Puede la ecuación $F(x,y) = -1$ definir localmente $y$ como función de $x$ cerca de $(1,1)$?
> 
> ---
> 
> **10. Tres variables:**
> 
> Para $f(x,y,z) = \frac{xyz}{x^2+y^2+z^2}$ (extendida por $0$ en el origen):
> 
> a) Calcular las derivadas parciales en el origen
> 
> b) Calcular las derivadas parciales fuera del origen
> 
> c) Determinar si las derivadas son continuas en el origen
> 
> d) ¿Es $f \in C^1(\mathbb{R}^3)$?

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = 3x^2 + 2xy + 5y^2$
> 
> Polinomio ⇒ $f \in C^\infty(\mathbb{R}^2)$ ✓
> 
> ---
> 
> **1c)** $f(x,y) = |x| \cdot y$
> 
> $$f_x(x,y) = \text{sgn}(x) \cdot y$$
> 
> Discontinua en el eje $y$ (donde $x=0$) ⇒ $f \notin C^1(\mathbb{R}^2)$ ✗
> 
> Pero $f \in C^1$ en cada semiplano ${x > 0}$ o ${x < 0}$ ✓
> 
> ---
> 
> **1e)** $f(x,y) = \sqrt{|x| + |y|}$
> 
> $$f_x = \frac{\text{sgn}(x)}{2\sqrt{|x|+|y|}}$$
> 
> Discontinua en los ejes ⇒ $f \notin C^1(\mathbb{R}^2)$ ✗
> 
> ---
> 
> **3a)** $f(x,y) = \frac{1}{x^2+y^2}$
> 
> Indefinida en $(0,0)$
> 
> $$f \in C^1(\mathbb{R}^2 \setminus {(0,0)})$$
> 
> ---
> 
> **3c)** $f(x,y) = \sqrt{x^2+y^2}$
> 
> Derivadas no existen en $(0,0)$
> 
> $$f \in C^1(\mathbb{R}^2 \setminus {(0,0)})$$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $f(x,y) = \begin{cases} xy & x \geq 0 \ 0 & x < 0 \end{cases}$
> 
> **En $x > 0$:** $f_x = y, f_y = x$ (continuas)
> 
> **En $x < 0$:** $f_x = 0, f_y = 0$ (continuas)
> 
> **En $x = 0$ (eje $y$):**
> 
> Desde la derecha: $\lim_{x \to 0^+} f_x(x,y) = y$
> 
> Desde la izquierda: $\lim_{x \to 0^-} f_x(x,y) = 0$
> 
> Para $y \neq 0$: discontinuidad
> 
> $$f \notin C^1(\mathbb{R}^2)$$ pero $f \in C^1$ fuera del eje $y$ (excepto el origen)
> 
> ---
> 
> **5. Resumen:**
> 
> a) $f_x(0,0) = 0, f_y(0,0) = 0$
> 
> b) $f_x(x,y) = \frac{2xy^3}{(x^2+y^2)^2}$ para $(x,y) \neq (0,0)$
> 
> c) $\lim_{(x,y) \to (0,0)} f_x(x,y)$ depende de la dirección ⇒ discontinua
> 
> d) Sí, es diferenciable (se puede verificar con la definición)
> 
> e) No, $f \notin C^1$ en ningún entorno de $(0,0)$
> 
> **Conclusión:** Ejemplo de función diferenciable pero no C¹
> 
> ---
> 
> **6.** $f(x,y) = x^3 - 3xy^2$
> 
> $$\nabla f = (3x^2 - 3y^2, -6xy) = (0,0)$$
> 
> De $-6xy = 0$: $x = 0$ o $y = 0$
> 
> Si $x = 0$: $-3y^2 = 0$ ⇒ $y = 0$
> 
> Si $y = 0$: $3x^2 = 0$ ⇒ $x = 0$
> 
> **Único punto crítico:** $(0,0)$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **7c)** Si $\nabla f = \vec{0}$ en todo punto:
> 
> Para cualesquiera dos puntos $(x_1,y_1)$ y $(x_2,y_2)$, el segmento que los une está en el dominio.
> 
> Por el teorema del valor medio:
> 
> $$f(x_2,y_2) - f(x_1,y_1) = \nabla f(c_1,c_2) \cdot ((x_2,y_2) - (x_1,y_1)) = \vec{0} \cdot \vec{v} = 0$$
> 
> Por tanto $f(x_2,y_2) = f(x_1,y_1)$ para todo par de puntos.
> 
> $$f \text{ es constante}$$
> 
> ---
> 
> **8b)** $h(x,y) = f(g(x,y)) = (e^x\cos y)^2 + (e^x\sin y)^2 = e^{2x}$
> 
> $$\nabla h = (2e^{2x}, 0)$$
> 
> Es C¹ (de hecho C∞) ✓
> 
> ---
> 
> **9.**
> 
> a) Polinomio ⇒ $F \in C^\infty$ ✓
> 
> b) $F(1,1) = 1 + 1 - 3 = -1$ ✓
> 
> c) $F_y = 3y^2 - 3x$, entonces $F_y(1,1) = 3 - 3 = 0$ ✗
> 
> d) **No** puede, porque $F_y(1,1) = 0$ (falla la condición del teorema)
> 
> ---
> 
> **10d)** Las derivadas parciales NO son continuas en el origen.
> 
> Por ejemplo, en coordenadas esféricas se puede mostrar que el límite de $f_x$ depende de la dirección.
> 
> $$f \notin C^1(\mathbb{R}^3)$$

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre C¹
> 
> ✅ **Definición:**
> 
> - Derivadas parciales existen
> - Derivadas parciales son **continuas**
> - Es una condición de "suavidad"
> 
> ✅ **Teorema fundamental:**
> 
> - $f \in C^1$ ⇒ $f$ es diferenciable
> - Garantiza que todas las fórmulas funcionan
> 
> ✅ **Jerarquía:**
> 
> - $C^\infty \subset C^2 \subset C^1 \subset$ Diferenciable
> - Cada clase es más restrictiva
> 
> ---
> 
> ### Verificación Práctica
> 
> ✅ **Funciones automáticamente C∞:**
> 
> - Polinomios
> - Exponenciales
> - Trigonométricas
> - Sus composiciones (donde estén definidas)
> 
> ✅ **Sospechosos (verificar):**
> 
> - Valor absoluto
> - Raíces
> - Cocientes (donde denominador → 0)
> - Funciones definidas por casos
> 
> ✅ **Estrategia:**
> 
> 1. Calcular derivadas parciales
> 2. Identificar puntos problemáticos
> 3. Verificar continuidad
> 
> ---
> 
> ### Importancia
> 
> ✅ **C¹ es la "regularidad mínima" para:**
> 
> - Diferenciabilidad garantizada
> - Regla de la cadena
> - Función implícita
> - Multiplicadores de Lagrange
> - Muchos teoremas de EDPs
> 
> ✅ **En la práctica:**
> 
> - La mayoría de funciones "razonables" son C¹
> - Excepciones típicas: valor absoluto, raíces, casos

---

## 📊 Mapa Conceptual Completo

> [!note]- 🌳 Árbol de Conceptos
> 
> ```
> FUNCIONES DE CLASE C¹
> │
> ├─ DEFINICIÓN
> │  ├─ Derivadas parciales existen
> │  ├─ Derivadas parciales continuas
> │  └─ Notación: f ∈ C¹(U)
> │
> ├─ TEOREMA FUNDAMENTAL
> │  ├─ C¹ ⇒ Diferenciable
> │  ├─ Garantiza: D_u f = ∇f · u 
> │  ├─ Garantiza: plano tangente existe 
> │  └─ Garantiza: regla de la cadena funciona 
> │
> ├─ JERARQUÍA DE REGULARIDAD 
> │  ├─ C⁰: continua 
> │  ├─ C¹: continuamente diferenciable 
> │  ├─ C²: segundas derivadas continuas 
> │  ├─ C³, C⁴, ..., Cⁿ 
> │  └─ C∞: infinitamente diferenciable 
> 
> ├─ PROPIEDADES ALGEBRAICAS 
> │  ├─ Suma: f + g ∈ C¹ 
> │  ├─ Producto: f · g ∈ C¹ 
> │  ├─ Cociente: f/g ∈ C¹ (donde g ≠ 0) 
> │  └─ Composición: f ∘ g ∈ C¹ 
> │
> ├─ EJEMPLOS IMPORTANTES 
> │ ├─ C∞: polinomios, e^x, sin, cos 
> │ ├─ C¹ pero no C∞: casos especiales 
> │ ├─ NO C¹: |x|, funciones con esquinas 
> │ └─ Diferenciable pero NO C¹: casos patológicos 
> │
> │─ APLICACIONES 
> │ ├─ Teorema función implícita 
> │ ├─ Multiplicadores de Lagrange 
> │ ├─ Regla de la cadena 
> │ ├─ Ecuaciones diferenciales parciales 
> │ └─ Teoría de optimización
> ```

---

## 🔬 Análisis Profundo: ¿Por qué C¹ es Suficiente?

> [!note]- 🧠 Intuición Matemática
> 
> ### La Pregunta Fundamental
> 
> **¿Por qué la continuidad de las derivadas parciales implica diferenciabilidad?**
> 
> La respuesta está en el **Teorema del Valor Medio Multivariable**.
> 
> ---
> 
> ### Bosquejo de la Demostración
> 
> **Queremos probar:** Si $f \in C^1$, entonces para $(h,k)$ cerca de $(0,0)$:
> 
> $$f(a+h, b+k) - f(a,b) = f_x(a,b) \cdot h + f_y(a,b) \cdot k + \epsilon(h,k)$$
> 
> donde $\lim_{(h,k) \to (0,0)} \frac{\epsilon(h,k)}{\sqrt{h^2+k^2}} = 0$
> 
> ---
> 
> **Paso 1: Descomponer el cambio**
> 
> $$f(a+h, b+k) - f(a,b) = [f(a+h, b+k) - f(a, b+k)] + [f(a, b+k) - f(a,b)]$$
> 
> El primer término involucra cambio solo en $x$, el segundo solo en $y$.
> 
> ---
> 
> **Paso 2: Aplicar valor medio a cada término**
> 
> Por el teorema del valor medio en una variable:
> 
> $$f(a+h, b+k) - f(a, b+k) = f_x(\xi_1, b+k) \cdot h$$
> 
> para algún $\xi_1$ entre $a$ y $a+h$.
> 
> $$f(a, b+k) - f(a,b) = f_y(a, \eta_1) \cdot k$$
> 
> para algún $\eta_1$ entre $b$ y $b+k$.
> 
> ---
> 
> **Paso 3: Usar continuidad de las derivadas**
> 
> Como $f_x$ es **continua**:
> 
> $$f_x(\xi_1, b+k) = f_x(a,b) + \delta_1(h,k)$$
> 
> donde $\delta_1(h,k) \to 0$ cuando $(h,k) \to (0,0)$.
> 
> Similarmente para $f_y$.
> 
> ---
> 
> **Paso 4: Reescribir el error**
> 
> $$f(a+h, b+k) - f(a,b) = [f_x(a,b) + \delta_1(h,k)] \cdot h + [f_y(a,b) + \delta_2(h,k)] \cdot k$$
> 
> $$= f_x(a,b) \cdot h + f_y(a,b) \cdot k + \underbrace{\delta_1(h,k) \cdot h + \delta_2(h,k) \cdot k}_{\epsilon(h,k)}$$
> 
> ---
> 
> **Paso 5: Verificar que el error es pequeño**
> 
> $$\frac{|\epsilon(h,k)|}{\sqrt{h^2+k^2}} \leq \frac{|\delta_1| \cdot |h| + |\delta_2| \cdot |k|}{\sqrt{h^2+k^2}}$$
> 
> $$\leq |\delta_1| \cdot \frac{|h|}{\sqrt{h^2+k^2}} + |\delta_2| \cdot \frac{|k|}{\sqrt{h^2+k^2}}$$
> 
> $$\leq |\delta_1| + |\delta_2| \to 0$$
> 
> cuando $(h,k) \to (0,0)$. ✓
> 
> ---
> 
> **Conclusión:** La **continuidad** de las derivadas es lo que permite controlar el error y garantiza diferenciabilidad.

---

## 🎨 Visualización Geométrica

> [!note]- 📊 Interpretación Visual
> 
> ### Función C¹: Superficie Suave
> 
> ```
>         z
>         |
>         |    ___
>         |  /     \    ← Superficie "suave"
>         | /       \     sin esquinas
>         |/         \
>         +------------ y
>        /
>       x
> ```
> 
> **Características:**
> 
> - El plano tangente existe en cada punto
> - La superficie no tiene "picos" ni "esquinas"
> - El gradiente varía continuamente
> 
> ---
> 
> ### NO C¹: Superficie con Esquina
> 
> ```
>         z
>         |
>         |    /\      ← Esquina en el origen
>         |   /  \       (como |x|)
>         |  /    \
>         | /      \
>         +------------ y
>        /
>       x
> ```
> 
> **Características:**
> 
> - Plano tangente no está bien definido en la esquina
> - Las derivadas "saltan" en la esquina
> - Función continua pero no C¹
> 
> ---
> 
> ### Campo de Gradientes: C¹ vs NO C¹
> 
> **Función C¹:** $f(x,y) = x^2 + y^2$
> 
> ```
>       y
>       |
>     2 |   ↗  ↑  ↖
>       |   →  •  ←    ← Gradientes varían
>     1 |   ↘  ↓  ↙      suavemente
>       |
>     0 +------------- x
>       0   1   2
> ```
> 
> El campo vectorial $\nabla f$ es **continuo** (sin saltos).
> 
> ---
> 
> **Función NO C¹:** $f(x,y) = |x|$
> 
> ```
>       y
>       |
>     2 |   ←  ?  →    ← Discontinuidad
>       |   ←  ?  →      en x = 0
>     1 |   ←  ?  →
>       |
>     0 +------------- x
>       -1  0  1
> ```
> 
> El gradiente tiene un **salto** en $x=0$ (va de $-1$ a $+1$).

---

## 🔧 Herramientas Computacionales

> [!example]- 💻 Verificación Numérica de C¹
> 
> ### Pseudocódigo: Verificar Continuidad de Derivadas
> 
> ```python
> def es_C1_numerico(f, punto, epsilon=1e-8, delta=1e-6):
>     """
>     Verifica numéricamente si f parece ser C¹ cerca de punto
>     """
>     x0, y0 = punto
>     
>     # Calcular derivadas parciales en el punto
>     fx_centro = (f(x0+epsilon, y0) - f(x0-epsilon, y0)) / (2*epsilon)
>     fy_centro = (f(x0, y0+epsilon) - f(x0, y0-epsilon)) / (2*epsilon)
>     
>     # Verificar continuidad en un entorno
>     max_diff_x = 0
>     max_diff_y = 0
>     
>     # Muestrear puntos cercanos
>     for dx in [-delta, 0, delta]:
>         for dy in [-delta, 0, delta]:
>             if dx == 0 and dy == 0:
>                 continue
>             
>             x, y = x0 + dx, y0 + dy
>             
>             # Derivadas en el punto cercano
>             fx = (f(x+epsilon, y) - f(x-epsilon, y)) / (2*epsilon)
>             fy = (f(x, y+epsilon) - f(x, y-epsilon)) / (2*epsilon)
>             
>             # Calcular diferencias
>             max_diff_x = max(max_diff_x, abs(fx - fx_centro))
>             max_diff_y = max(max_diff_y, abs(fy - fy_centro))
>     
>     # Criterio: las derivadas varían poco en el entorno
>     umbral = 0.1  # ajustable según el problema
>     
>     if max_diff_x < umbral and max_diff_y < umbral:
>         return True, "Parece ser C¹"
>     else:
>         return False, f"Variación grande: fx={max_diff_x:.4f}, fy={max_diff_y:.4f}"
> ```
> 
> ---
> 
> ### Ejemplo de Uso
> 
> ```python
> # Función C¹
> def f1(x, y):
>     return x**2 + y**2
> 
> print(es_C1_numerico(f1, (0, 0)))
> # Salida: (True, "Parece ser C¹")
> 
> # Función NO C¹
> def f2(x, y):
>     return abs(x) + abs(y)
> 
> print(es_C1_numerico(f2, (0, 0)))
> # Salida: (False, "Variación grande: fx=2.0000, fy=2.0000")
> ```
> 
> ---
> 
> ### Visualización de Derivadas
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> 
> def visualizar_derivada(f, region=(-2, 2, -2, 2), n=50):
>     """
>     Visualiza la derivada parcial fx y su continuidad
>     """
>     x = np.linspace(region[0], region[1], n)
>     y = np.linspace(region[2], region[3], n)
>     X, Y = np.meshgrid(x, y)
>     
>     # Calcular fx numéricamente
>     h = 0.001
>     FX = (f(X+h, Y) - f(X-h, Y)) / (2*h)
>     
>     # Graficar
>     plt.figure(figsize=(10, 4))
>     
>     plt.subplot(1, 2, 1)
>     plt.contourf(X, Y, f(X, Y), levels=20)
>     plt.colorbar(label='f(x,y)')
>     plt.title('Función f')
>     plt.xlabel('x')
>     plt.ylabel('y')
>     
>     plt.subplot(1, 2, 2)
>     plt.contourf(X, Y, FX, levels=20)
>     plt.colorbar(label='fx(x,y)')
>     plt.title('Derivada parcial fx')
>     plt.xlabel('x')
>     plt.ylabel('y')
>     
>     plt.tight_layout()
>     plt.show()
> 
> # Ejemplo: función C¹
> visualizar_derivada(lambda x, y: x**2 + y**2)
> ```

---

## 🌐 Extensión a Funciones Vectoriales

> [!note]- 🎯 C¹ para Funciones $\mathbb{R}^n \to \mathbb{R}^m$
> 
> ### Definición para Funciones Vectoriales
> 
> **Función:** $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$
> 
> $$\vec{F}(x_1, \ldots, x_n) = (F_1(x_1, \ldots, x_n), \ldots, F_m(x_1, \ldots, x_n))$$
> 
> **Definición:** $\vec{F} \in C^1(U)$ si **cada componente** $F_i \in C^1(U)$ para $i = 1, \ldots, m$.
> 
> Es decir, todas las derivadas parciales:
> 
> $$\frac{\partial F_i}{\partial x_j}, \quad i = 1,\ldots,m, \quad j = 1,\ldots,n$$
> 
> existen y son continuas.
> 
> ---
> 
> ### Matriz Jacobiana
> 
> La **matriz jacobiana** de $\vec{F}$ es:
> 
> $$J_{\vec{F}} = \begin{pmatrix} \frac{\partial F_1}{\partial x_1} & \cdots & \frac{\partial F_1}{\partial x_n} \ \vdots & \ddots & \vdots \ \frac{\partial F_m}{\partial x_1} & \cdots & \frac{\partial F_m}{\partial x_n} \end{pmatrix}$$
> 
> Si $\vec{F} \in C^1$, entonces $J_{\vec{F}}$ es una **función continua** con valores matriciales.
> 
> ---
> 
> ### Ejemplo: Transformación Polar
> 
> $$\vec{F}(r, \theta) = (r\cos\theta, r\sin\theta)$$
> 
> **Componentes:**
> 
> - $F_1(r,\theta) = r\cos\theta$
> - $F_2(r,\theta) = r\sin\theta$
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial F_1}{\partial r} = \cos\theta, \quad \frac{\partial F_1}{\partial \theta} = -r\sin\theta$$
> 
> $$\frac{\partial F_2}{\partial r} = \sin\theta, \quad \frac{\partial F_2}{\partial \theta} = r\cos\theta$$
> 
> Todas son continuas en $\mathbb{R}^2$ (para $r > 0$).
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{pmatrix} \cos\theta & -r\sin\theta \ \sin\theta & r\cos\theta \end{pmatrix}$$
> 
> $$\boxed{\vec{F} \in C^1({(r,\theta) : r > 0})}$$
> 
> De hecho, $\vec{F} \in C^\infty$ para $r > 0$.

---

## 📐 Teorema del Valor Medio Multivariable

> [!note]- 📏 Versión Multivariable
> 
> **Teorema del Valor Medio:** Si $f \in C^1$ en un conjunto convexo $U$ que contiene el segmento de $\vec{a}$ a $\vec{b}$, entonces existe un punto $\vec{c}$ en ese segmento tal que:
> 
> $$f(\vec{b}) - f(\vec{a}) = \nabla f(\vec{c}) \cdot (\vec{b} - \vec{a})$$
> 
> ---
> 
> **En dos variables:** Si $(a,b)$ y $(x,y)$ están en $U$, existe $(c_1, c_2)$ en el segmento entre ellos tal que:
> 
> $$f(x,y) - f(a,b) = f_x(c_1, c_2) \cdot (x-a) + f_y(c_1, c_2) \cdot (y-b)$$
> 
> ---
> 
> **Importancia:**
> 
> - Generalización directa del teorema del valor medio de una variable
> - **Requiere C¹** para su validez
> - Fundamental para muchas demostraciones en cálculo multivariable
> 
> ---
> 
> ### Ejemplo de Aplicación
> 
> **Función:** $f(x,y) = x^2 + xy + y^2$
> 
> **Puntos:** $(0,0)$ a $(1,1)$
> 
> **Calcular:**
> 
> $$f(1,1) - f(0,0) = 3 - 0 = 3$$
> 
> **Gradiente:**
> 
> $$\nabla f = (2x + y, x + 2y)$$
> 
> **Por el teorema:** Existe $(c_1, c_2)$ en el segmento $[(0,0), (1,1)]$ tal que:
> 
> $$3 = (2c_1 + c_2) \cdot 1 + (c_1 + 2c_2) \cdot 1 = 3c_1 + 3c_2 = 3(c_1 + c_2)$$
> 
> $$c_1 + c_2 = 1$$
> 
> Por ejemplo, $(c_1, c_2) = (0.5, 0.5)$ funciona (el punto medio). ✓

---

## 🎓 Conexión con Análisis Real

> [!note]- 📚 Contexto Teórico Avanzado
> 
> ### Espacios de Funciones
> 
> Las funciones C¹ forman un **espacio vectorial**:
> 
> $$C^1(U) = {f: U \to \mathbb{R} : f \text{ es de clase } C^1}$$
> 
> **Propiedades:**
> 
> - Es un espacio lineal (suma y producto por escalar están bien definidos)
> - Tiene estructura de anillo (también hay producto)
> - Es un **espacio de Banach** con la norma adecuada
> 
> ---
> 
> ### Norma C¹
> 
> Para funciones en un dominio acotado $U$:
> 
> $$|f|_{C^1} = \sup_{(x,y) \in U} |f(x,y)| + \sup_{(x,y) \in U} |f_x(x,y)| + \sup_{(x,y) \in U} |f_y(x,y)|$$
> 
> Esta norma mide:
> 
> - El tamaño de la función
> - El tamaño de sus derivadas
> 
> ---
> 
> ### Densidad
> 
> **Teorema:** Las funciones C∞ con soporte compacto son **densas** en C¹.
> 
> Es decir, cualquier función C¹ puede aproximarse arbitrariamente bien por funciones C∞.
> 
> **Importancia:** En análisis funcional y EDPs, esto permite "suavizar" funciones.
> 
> ---
> 
> ### Teoremas de Inmersión (Embeddings)
> 
> **Teorema de Sobolev:** En dimensiones bajas, los espacios de Sobolev $W^{1,p}$ se "incrustan" en espacios C⁰ o C¹.
> 
> Esto conecta:
> 
> - Teoría de integración (espacios $L^p$)
> - Teoría de diferenciación (espacios C^k)
> 
> **Relevancia:** Fundamental en teoría moderna de EDPs.

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> Este tema es prerequisito para:
> 
> - [[10 - Diferenciabilidad]] - C¹ es condición suficiente para diferenciabilidad
> - [[12 - Regla de la Cadena Multivariable]] - Requiere C¹ para funcionar
> - [[13 - Teorema de la Función Implícita]] - Hipótesis esencial
> - [[14 - Teorema de la Función Inversa]] - Requiere C¹
> - [[15 - Multiplicadores de Lagrange]] - Necesita gradientes continuos
> - [[16 - Fórmula de Taylor Multivariable]] - Extensión a C²
> - [[17 - Teorema de Schwarz]] - Igualdad de derivadas mixtas
> 
> Conceptos relacionados:
> 
> - **Diferenciabilidad** - C¹ es condición suficiente (tema central de Nota 10)
> - **Gradiente** - Sus componentes deben ser continuas (ver Nota 11)
> - **Derivadas Parciales** - Deben existir y ser continuas (ver Nota 08)
> - **Continuidad** - C¹ implica continuidad de f y de sus derivadas
> - **Aproximación Lineal** - C¹ garantiza que el plano tangente existe
> - **Optimización** - Condiciones de primer orden requieren gradientes continuos
> 
> Siguiente tema recomendado: 
> [[12 - Regla de la Cadena Multivariable]]
> 

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **C¹ es la "regularidad mínima segura"**
>     - Garantiza diferenciabilidad
>     - Todas las fórmulas funcionan
>     - Es verificable en la práctica
> 2. **La continuidad de las derivadas es crucial**
>     - No basta que existan
>     - Deben ser funciones continuas
>     - Esto elimina "esquinas" y "saltos"
> 3. **Mayoría de funciones "normales" son C¹ (o C∞)**
>     - Polinomios
>     - Exponenciales
>     - Trigonométricas
>     - Sus composiciones
> 4. **Excepciones importantes**
>     - Valor absoluto: |x|, |y|
>     - Raíces en el origen: √(x²+y²)
>     - Funciones por casos (verificar frontera)
> 5. **Teorema fundamental**
>     - C¹ ⇒ Diferenciable
>     - Pero NO al revés (existen contraejemplos)
> 
> ---
> 
> ### Estrategia Práctica
> 
> **Para verificar si f ∈ C¹:**
> 
> 6. ✅ Calcular derivadas parciales explícitamente
> 7. ✅ Identificar puntos "sospechosos"
> 8. ✅ Verificar continuidad
>     - Automática para polinomios, exp, trig
>     - Calcular límites en puntos problemáticos
> 9. ✅ Concluir sobre el dominio de C¹
> 
> ---
> 
> ### Próximos Pasos
> 
> Con C¹ dominado, estás listo para:
> 
> - **Regla de la Cadena:** Composición de funciones
> - **Función Implícita:** Despejar variables
> - **Función Inversa:** Invertibilidad local
> - **Optimización:** Teoría completa con gradientes
> - **EDPs:** Ecuaciones diferenciales parciales
> 
> ---
> 
> ### Reflexión Final
> 
> C¹ es donde el cálculo multivariable se vuelve "manejable":
> 
> - Suficientemente restrictivo para que los teoremas funcionen
> - Suficientemente amplio para incluir casi todas las funciones útiles
> - El equilibrio perfecto entre teoría y práctica
> 
> **Mensaje clave:** Si puedes verificar C¹, puedes trabajar con confianza. Si no, procede con cuidado y verifica diferenciabilidad caso por caso.

---

## 📖 Resumen de Fórmulas y Definiciones

> [!note]- 📋 Referencia Rápida
> 
> ### Definiciones Fundamentales
> 
> |Concepto|Definición|
> |---|---|
> |**f ∈ C¹(U)**|Derivadas parciales existen y son continuas en U|
> |**f ∈ C²(U)**|Segundas derivadas existen y son continuas en U|
> |**f ∈ C∞(U)**|Todas las derivadas existen y son continuas en U|
> 
> ---
> 
> ### Teoremas Clave
> 
> |Teorema|Enunciado|
> |---|---|
> |**C¹ ⇒ Diferenciable**|Si f ∈ C¹, entonces f es diferenciable|
> |**Valor Medio**|f(b) - f(a) = ∇f(c) · (b - a) para algún c|
> |**Schwarz (C²)**|Si f ∈ C², entonces f_xy = f_yx|
> 
> ---
> 
> ### Funciones Comunes
> 
> |Tipo|Clase|Observaciones|
> |---|---|---|
> |Polinomios|C∞|Siempre suaves|
> |e^(expresión)|C∞|Donde esté definida|
> |sin, cos|C∞|Siempre suaves|
> |√(expresión)|Verificar|Cuidado en raíces|
> |\|x\|, \|y\||NO C¹|En el origen|
> |Cocientes|Verificar|Donde denominador ≠ 0|

---

**Tags:** #calculo-multivariable #clase-C1 #diferenciabilidad #continuidad #derivadas-parciales #gradiente #regularidad #funciones-suaves #analisis-real #teoremas-fundamentales

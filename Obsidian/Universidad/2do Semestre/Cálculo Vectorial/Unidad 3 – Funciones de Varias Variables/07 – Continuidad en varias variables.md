# 📘 07 – Continuidad en Varias Variables

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante la Continuidad?
> 
> La continuidad es un concepto fundamental que garantiza que las funciones se comportan "suavemente" sin saltos ni interrupciones.
> 
> **Importancia práctica:**
> 
> - **Física:** Variables continuas (temperatura, presión, densidad)
> - **Ingeniería:** Análisis de estructuras sin fracturas
> - **Economía:** Modelos de demanda y oferta
> - **Computación:** Interpolación y aproximación de datos
> 
> **Diferencia con una variable:**
> 
> - En $f(x)$: continuidad se verifica en **un punto** de una recta
> - En $f(x,y)$: continuidad se verifica en **un punto** del **plano**
> - En $f(x,y,z)$: continuidad se verifica en **un punto** del **espacio**
> 
> **Nueva complejidad:** En varias variables, podemos acercarnos a un punto desde **infinitas direcciones**, lo que hace la continuidad más restrictiva y más interesante.

---

## 📐 Definición de Continuidad

### 🔍 Definición Formal

> [!example]- 🟢 Definición: Continuidad en un Punto
> 
> **Definición formal:** Una función $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ es **continua** en un punto $(x_0, y_0)$ si se cumplen tres condiciones:
> 
> 1. **Existencia:** $f(x_0, y_0)$ está definida
> 2. **Límite existe:** $\lim_{(x,y) \to (x_0,y_0)} f(x,y)$ existe
> 3. **Coincidencia:** $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = f(x_0, y_0)$
> 
> **En símbolos:** $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = f(x_0, y_0)$$
> 
> ---
> 
> **Definición equivalente ($\varepsilon$-$\delta$):**
> 
> $f$ es continua en $(x_0, y_0)$ si para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
> 
> $$\text{Si } \sqrt{(x-x_0)^2 + (y-y_0)^2} < \delta \implies |f(x,y) - f(x_0,y_0)| < \varepsilon$$
> 
> **Interpretación intuitiva:**
> 
> - Puntos **cercanos** a $(x_0, y_0)$ tienen valores de función **cercanos** a $f(x_0, y_0)$
> - No hay "saltos" en el valor de la función
> - La superficie $z = f(x,y)$ no tiene "rupturas"

### 🎯 Definición Intuitiva

> [!note]- 💭 Interpretación Práctica
> 
> **Una función es continua en un punto si:**
> 
> ✅ "Podemos calcular el límite por sustitución directa"
> 
> ✅ "La gráfica no tiene saltos, agujeros ni interrupciones en ese punto"
> 
> ✅ "Pequeños cambios en la entrada producen pequeños cambios en la salida"
> 
> ---
> 
> **Analogía física:**
> 
> Imagina que $f(x,y)$ representa la **altura de una superficie**:
> 
> - **Continua:** Puedes caminar sobre la superficie sin caer en agujeros
> - **Discontinua:** Hay grietas, acantilados o agujeros donde "caes"
> 
> ---
> 
> **Ejemplo visual:**
> 
> ```
> Función CONTINUA:          Función DISCONTINUA:
> 
>     z                          z
>     |                          |
>     |    ___                   |    ___
>     |   /   \                  |   /   
>     |  /     \                 |  /     
>     |_/       \_               |_/       o  ← salto
>     +--------- y               +--------- y
>    /                          /
>   x                          x
> ```

---

## 📊 Continuidad en un Conjunto

> [!example]- 🟡 Continuidad en Regiones
> 
> **Definición:** Una función $f$ es **continua en un conjunto $D$** si es continua en **cada punto** de $D$.
> 
> $$f \text{ es continua en } D \iff f \text{ es continua en } (x,y) \text{ para todo } (x,y) \in D$$
> 
> ---
> 
> ### Tipos de Conjuntos
> 
> **1. Conjunto Abierto:**
> 
> - No incluye su frontera
> - Ejemplo: $D = {(x,y) : x^2 + y^2 < 1}$ (interior del círculo)
> 
> **2. Conjunto Cerrado:**
> 
> - Incluye su frontera
> - Ejemplo: $D = {(x,y) : x^2 + y^2 \leq 1}$ (disco cerrado)
> 
> **3. Conjunto Acotado:**
> 
> - Contenido en un círculo de radio finito
> - Ejemplo: $D = {(x,y) : |x| \leq 5, |y| \leq 5}$
> 
> **4. Conjunto Compacto:**
> 
> - Cerrado y acotado
> - Importante para el Teorema del Valor Extremo
> 
> ---
> 
> **Continuidad en la frontera:**
> 
> Si $f$ está definida solo en un conjunto $D$, entonces "$f$ es continua en la frontera de $D$" significa que el límite desde **dentro** del dominio coincide con el valor de la función.

---

## 🎨 Tipos de Discontinuidad

### ⚠️ Clasificación de Discontinuidades

> [!warning]- 🔴 Discontinuidades en Varias Variables
> 
> ### 1. Discontinuidad Removible (Evitable)
> 
> **Definición:** El límite existe pero no coincide con el valor de la función (o la función no está definida).
> 
> **Características:**
> 
> - $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$ existe
> - Pero $f(x_0,y_0) \neq L$ (o no está definida)
> - Se puede "arreglar" redefiniendo $f(x_0,y_0) = L$
> 
> ---
> 
> ### 2. Discontinuidad Esencial (No Removible)
> 
> **Definición:** El límite **no existe**.
> 
> **Características:**
> 
> - $\lim_{(x,y) \to (x_0,y_0)} f(x,y)$ no existe
> - Depende del camino de aproximación
> - **No** se puede arreglar redefiniendo
> 
> ---
> 
> ### 3. Discontinuidad de Salto
> 
> **Definición:** La función "salta" de un valor a otro.
> 
> **Características:**
> 
> - Común en funciones definidas por partes
> - El límite puede no existir o existir pero diferir del valor
> 
> ---
> 
> ### 4. Discontinuidad Infinita
> 
> **Definición:** La función tiende a $\pm\infty$ en el punto.
> 
> **Características:**
> 
> - $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = \pm\infty$
> - Común en denominadores que se anulan
> - Representa una "asíntota vertical" en 2D

---

## 📚 Ejemplos Detallados

### Ejemplo 1: Función Continua Polinomial

> [!example]- 📝 Ejemplo 1: Polinomio
> 
> **Función:** $$f(x,y) = x^2 + 3xy - 2y^2 + 5$$
> 
> **Análisis de continuidad:**
> 
> Los polinomios son **siempre continuos** en todo $\mathbb{R}^2$.
> 
> **Verificación en cualquier punto $(x_0, y_0)$:**
> 
> $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = x_0^2 + 3x_0y_0 - 2y_0^2 + 5 = f(x_0, y_0)$$
> 
> **Conclusión:**
> 
> - $f$ es continua en **todo** $\mathbb{R}^2$
> - No hay restricciones en el dominio
> - La superficie es "suave" sin interrupciones

### Ejemplo 2: Discontinuidad Removible

> [!example]- 📝 Ejemplo 2: Discontinuidad que se puede Arreglar
> 
> **Función:** $$f(x,y) = \begin{cases} \frac{x^2 - y^2}{x - y} & \text{si } x \neq y \ 0 & \text{si } x = y \end{cases}$$
> 
> **Análisis en la recta $x = y$:**
> 
> Para $x \neq y$, simplificamos: $$f(x,y) = \frac{(x-y)(x+y)}{x-y} = x + y$$
> 
> **Calculamos el límite en un punto $(a,a)$ de la recta:** $$\lim_{(x,y) \to (a,a)} f(x,y) = \lim_{(x,y) \to (a,a)} (x + y) = 2a$$
> 
> **Pero** $f(a,a) = 0$
> 
> **Problema:** $\lim_{(x,y) \to (a,a)} f(x,y) = 2a \neq 0 = f(a,a)$
> 
> **Tipo:** Discontinuidad **removible**
> 
> **Solución:** Redefinir $$f(x,y) = \begin{cases} \frac{x^2 - y^2}{x - y} & \text{si } x \neq y \ 2x & \text{si } x = y \end{cases}$$
> 
> Ahora $f$ es continua en todo $\mathbb{R}^2$.

### Ejemplo 3: Discontinuidad Esencial

> [!example]- 📝 Ejemplo 3: Límite que No Existe
> 
> **Función:** $$f(x,y) = \begin{cases} \frac{xy}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **Análisis en el origen:**
> 
> **Por el eje X** ($y = 0$): $$\lim_{x \to 0} \frac{x \cdot 0}{x^2 + 0} = 0$$
> 
> **Por la recta $y = x$:** $$\lim_{x \to 0} \frac{x \cdot x}{x^2 + x^2} = \lim_{x \to 0} \frac{x^2}{2x^2} = \frac{1}{2}$$
> 
> **Conclusión:**
> 
> - El límite **depende del camino** ($0 \neq \frac{1}{2}$)
> - Por lo tanto, el límite **NO existe**
> - La función es **discontinua** en $(0,0)$
> - Esta discontinuidad es **esencial** (no removible)
> 
> **No importa cómo redefinamos** $f(0,0)$, la función seguirá siendo discontinua porque el límite no existe.

### Ejemplo 4: Función Racional Continua

> [!example]- 📝 Ejemplo 4: Continuidad de una Función Racional
> 
> **Función:** $$f(x,y) = \frac{x^2 + y^2}{x^2 + y^2 + 1}$$
> 
> **Análisis:**
> 
> **Dominio:** $\mathbb{R}^2$ (el denominador nunca es cero)
> 
> **Continuidad:**
> 
> - Numerador: continuo (polinomio)
> - Denominador: continuo y $> 0$ siempre
> - Cociente: continuo donde el denominador $\neq 0$
> 
> **Verificación en cualquier punto $(x_0, y_0)$:**
> 
> $$\lim_{(x,y) \to (x_0,y_0)} \frac{x^2 + y^2}{x^2 + y^2 + 1} = \frac{x_0^2 + y_0^2}{x_0^2 + y_0^2 + 1} = f(x_0, y_0)$$
> 
> **Conclusión:** $f$ es continua en todo $\mathbb{R}^2$

### Ejemplo 5: Discontinuidad Infinita

> [!example]- 📝 Ejemplo 5: Asíntota Vertical
> 
> **Función:** $$f(x,y) = \frac{1}{x^2 + y^2}$$
> 
> **Dominio:** $\mathbb{R}^2 \setminus {(0,0)}$
> 
> **Análisis en el origen:**
> 
> Cuando $(x,y) \to (0,0)$: $$x^2 + y^2 \to 0^+ \implies \frac{1}{x^2 + y^2} \to +\infty$$
> 
> **Conclusión:**
> 
> - $f$ tiene una **discontinuidad infinita** en $(0,0)$
> - La función no está definida en el origen
> - La superficie tiene un "pico infinito" en el origen
> 
> **Visualización:**
> 
> ```
>         z
>         |
>       ∞ |     |
>         |     |
>         |    /|\
>         |   / | \
>         |__/  |  \__
>         +-----o----- y
>        /    (0,0)
>       x
> ```

### Ejemplo 6: Función Definida por Partes

> [!example]- 📝 Ejemplo 6: Continuidad en Función por Partes
> 
> **Función:** $$f(x,y) = \begin{cases} x^2 + y^2 & \text{si } x^2 + y^2 < 1 \ 2 - x^2 - y^2 & \text{si } x^2 + y^2 \geq 1 \end{cases}$$
> 
> **Análisis:**
> 
> **Interior de las regiones:**
> 
> - Dentro del círculo unitario: $f(x,y) = x^2 + y^2$ (continua)
> - Fuera del círculo: $f(x,y) = 2 - x^2 - y^2$ (continua)
> 
> **En la frontera** $x^2 + y^2 = 1$:
> 
> Debemos verificar si los límites desde ambos lados coinciden.
> 
> **Desde dentro** ($x^2 + y^2 < 1$): $$\lim_{(x,y) \to (x_0,y_0)} (x^2 + y^2) = x_0^2 + y_0^2 = 1$$
> 
> **Desde fuera** ($x^2 + y^2 > 1$): $$\lim_{(x,y) \to (x_0,y_0)} (2 - x^2 - y^2) = 2 - 1 = 1$$
> 
> **Valor en la frontera:** $$f(x_0,y_0) = 2 - x_0^2 - y_0^2 = 2 - 1 = 1$$
> 
> **Conclusión:** Todos coinciden, por lo tanto $f$ es **continua** en todo $\mathbb{R}^2$ ✓

### Ejemplo 7: Discontinuidad en la Frontera

> [!example]- 📝 Ejemplo 7: Salto en la Frontera
> 
> **Función:** $$f(x,y) = \begin{cases} 1 & \text{si } x^2 + y^2 < 1 \ 2 & \text{si } x^2 + y^2 \geq 1 \end{cases}$$
> 
> **Análisis en la circunferencia** $x^2 + y^2 = 1$:
> 
> Sea $(x_0, y_0)$ un punto con $x_0^2 + y_0^2 = 1$.
> 
> **Desde dentro:** $$\lim_{\substack{(x,y) \to (x_0,y_0) \ x^2+y^2 < 1}} f(x,y) = 1$$
> 
> **Valor en la frontera:** $$f(x_0,y_0) = 2$$
> 
> **Problema:** $1 \neq 2$
> 
> **Conclusión:**
> 
> - Discontinuidad de **salto** en toda la circunferencia $x^2 + y^2 = 1$
> - Continua dentro y fuera del círculo, pero no en la frontera

### Ejemplo 8: Función Trigonométrica

> [!example]- 📝 Ejemplo 8: Continuidad de Funciones Compuestas
> 
> **Función:** $$f(x,y) = \sin(x^2 + y^2)$$
> 
> **Análisis:**
> 
> Esta es una **composición** de funciones:
> 
> - $g(x,y) = x^2 + y^2$ (continua en $\mathbb{R}^2$)
> - $h(u) = \sin(u)$ (continua en $\mathbb{R}$)
> - $f(x,y) = h(g(x,y))$
> 
> **Teorema de composición:** Si $g$ es continua en $(x_0, y_0)$ y $h$ es continua en $g(x_0, y_0)$, entonces $h \circ g$ es continua en $(x_0, y_0)$.
> 
> **Conclusión:** $f(x,y) = \sin(x^2 + y^2)$ es continua en todo $\mathbb{R}^2$ ✓

---

## 🎯 Propiedades de Funciones Continuas

### 📜 Teoremas Fundamentales

> [!note]- 🟢 Propiedades Algebraicas
> 
> Si $f$ y $g$ son continuas en $(x_0, y_0)$, entonces:
> 
> ### 1. Suma
> 
> $$f + g \text{ es continua en } (x_0, y_0)$$ $$(f + g)(x,y) = f(x,y) + g(x,y)$$
> 
> ### 2. Diferencia
> 
> $$f - g \text{ es continua en } (x_0, y_0)$$
> 
> ### 3. Producto
> 
> $$f \cdot g \text{ es continua en } (x_0, y_0)$$ $$(f \cdot g)(x,y) = f(x,y) \cdot g(x,y)$$
> 
> ### 4. Producto por Escalar
> 
> $$c \cdot f \text{ es continua en } (x_0, y_0)$$ para cualquier constante $c$
> 
> ### 5. Cociente
> 
> $$\frac{f}{g} \text{ es continua en } (x_0, y_0)$$ **siempre que** $g(x_0, y_0) \neq 0$
> 
> ### 6. Composición
> 
> Si $g$ es continua en $(x_0, y_0)$ y $h$ es continua en $g(x_0, y_0)$: $$h \circ g \text{ es continua en } (x_0, y_0)$$
> 
> ### 7. Potencia
> 
> $$f^n \text{ es continua en } (x_0, y_0)$$ para cualquier $n \in \mathbb{N}$
> 
> ### 8. Raíz
> 
> $$\sqrt[n]{f} \text{ es continua en } (x_0, y_0)$$ si $f(x_0, y_0) > 0$ (para $n$ par) o $f(x_0, y_0) \in \mathbb{R}$ (para $n$ impar)

---

## 🌟 Funciones Continuas Importantes

> [!tip]- ✅ Catálogo de Funciones Continuas
> 
> ### Siempre Continuas en Todo su Dominio:
> 
> **1. Polinomios:** $$f(x,y) = a_0 + a_1x + a_2y + a_3x^2 + a_4xy + a_5y^2 + \ldots$$ Continua en $\mathbb{R}^2$
> 
> **2. Funciones Racionales:** $$f(x,y) = \frac{P(x,y)}{Q(x,y)}$$ Continua donde $Q(x,y) \neq 0$
> 
> **3. Funciones Trigonométricas:**
> 
> - $\sin(x + y)$, $\cos(xy)$, $\tan(x/y)$, etc.
> - Continuas en sus dominios naturales
> 
> **4. Funciones Exponenciales:**
> 
> - $e^{x+y}$, $e^{xy}$, $a^{x^2+y^2}$
> - Continuas en $\mathbb{R}^2$
> 
> **5. Funciones Logarítmicas:**
> 
> - $\ln(x^2 + y^2)$, $\log(x + y)$
> - Continuas donde el argumento $> 0$
> 
> **6. Raíces:**
> 
> - $\sqrt{x^2 + y^2}$, $\sqrt[3]{x + y}$
> - Continuas donde el radicando es válido
> 
> **7. Valor Absoluto:**
> 
> - $|x + y|$, $|xy|$
> - Continuas en $\mathbb{R}^2$
> 
> ---
> 
> ### Ejemplos Específicos:
> 
> |Función|Dominio|Continuidad|
> |---|---|---|
> |$x^2 + y^2$|$\mathbb{R}^2$|Todo $\mathbb{R}^2$|
> |$\frac{1}{x^2 + y^2}$|$\mathbb{R}^2 \setminus {(0,0)}$|Su dominio|
> |$\sqrt{1 - x^2 - y^2}$|$x^2 + y^2 \leq 1$|Su dominio|
> |$\ln(x + y)$|$x + y > 0$|Su dominio|
> |$e^{xy}$|$\mathbb{R}^2$|Todo $\mathbb{R}^2$|
> |$\arctan(y/x)$|$x \neq 0$|Su dominio|

---

## 🔬 Teoremas Importantes

### Teorema del Valor Intermedio

> [!note]- 🎯 Teorema del Valor Intermedio (TVI)
> 
> **Enunciado:** Sea $f$ continua en un conjunto **conexo por trayectorias** $D \subseteq \mathbb{R}^2$.
> 
> Si $(x_1, y_1), (x_2, y_2) \in D$ y $f(x_1, y_1) < c < f(x_2, y_2)$, entonces existe un punto $(x_0, y_0) \in D$ tal que:
> 
> $$f(x_0, y_0) = c$$
> 
> **Interpretación:**
> 
> - Si viajas continuamente de un punto a otro sobre la superficie
> - Y la altura inicial es menor que $c$ y la final es mayor que $c$
> - Entonces **pasas** por una altura exactamente igual a $c$
> 
> ---
> 
> **Conjunto conexo por trayectorias:** Un conjunto donde **cualquier par de puntos** puede conectarse por una curva continua completamente contenida en el conjunto.
> 
> **Ejemplos:**
> 
> - ✅ Disco: $x^2 + y^2 \leq 1$ (conexo)
> - ✅ Rectángulo: $[a,b] \times [c,d]$ (conexo)
> - ❌ Dos discos separados: NO conexo
> 
> ---
> 
> **Aplicación:** Garantiza la existencia de soluciones a ecuaciones $f(x,y) = c$ en regiones continuas.

### Teorema del Valor Extremo

> [!note]- 🎯 Teorema del Valor Extremo (TVE)
> 
> **Enunciado:** Sea $f$ continua en un conjunto **compacto** (cerrado y acotado) $D \subseteq \mathbb{R}^2$.
> 
> Entonces $f$ alcanza su **máximo** y su **mínimo** absolutos en $D$.
> 
> Es decir, existen puntos $(x_{\text{max}}, y_{\text{max}})$ y $(x_{\text{min}}, y_{\text{min}})$ en $D$ tales que:
> 
> $$f(x_{\text{min}}, y_{\text{min}}) \leq f(x,y) \leq f(x_{\text{max}}, y_{\text{max}})$$
> 
> para todo $(x,y) \in D$.
> 
> ---
> 
> **Requisitos esenciales:**
> 
> 1. ✅ $f$ debe ser **continua**
> 2. ✅ $D$ debe ser **cerrado** (incluye su frontera)
> 3. ✅ $D$ debe ser **acotado** (contenido en un círculo finito)
> 
> **Ejemplo:**
> 
> - Función: $f(x,y) = x^2 + y^2$
> - Dominio: $D = {(x,y) : x^2 + y^2 \leq 1}$ (disco cerrado)
> 
> **Entonces:**
> 
> - Mínimo: $f(0,0) = 0$ (en el centro)
> - Máximo: $f = 1$ (en la circunferencia $x^2 + y^2 = 1$)
> 
> ---
> 
> **Importancia:**
> 
> - Fundamental para **optimización**
> - Garantiza que problemas de máximos/mínimos tienen solución
> - Base para cálculo de extremos con restricciones

### Teorema de Weierstrass

> [!note]- 🎯 Teorema de Aproximación de Weierstrass
> 
> **Enunciado:** Toda función continua en un conjunto compacto puede aproximarse **uniformemente** por polinomios.
> 
> Si $f$ es continua en $D$ (compacto), entonces para todo $\varepsilon > 0$, existe un polinomio $P(x,y)$ tal que:
> 
> $$|f(x,y) - P(x,y)| < \varepsilon$$
> 
> para todo $(x,y) \in D$.
> 
> **Aplicación práctica:**
> 
> - Interpolación numérica
> - Aproximación de funciones complejas
> - Base teórica para métodos numéricos

---

## 💡 Estrategias para Verificar Continuidad

> [!tip]- ⭐ Guía Paso a Paso
> 
> ### Método General:
> 
> **Paso 1:** Identificar el **dominio** de la función
> 
> - ¿Dónde está definida?
> - ¿Hay divisiones por cero?
> - ¿Raíces con radicandos negativos?
> - ¿Logaritmos de argumentos $\leq 0$?
> 
> **Paso 2:** En el **interior del dominio**
> 
> - Si la función es combinación de funciones continuas conocidas
> - Entonces es continua ahí (usar propiedades algebraicas)
> 
> **Paso 3:** En **puntos problemáticos** o **frontera**
> 
> - Calcular $\lim_{(x,y) \to (x_0,y_0)} f(x,y)$
> - Comparar con $f(x_0, y_0)$
> - ¿Coinciden? → Continua
> - ¿No coinciden o límite no existe? → Discontinua
> 
> **Paso 4:** Para **funciones definidas por partes**
> 
> - Verificar continuidad en cada región
> - **Crucial:** Verificar en las fronteras entre regiones
> 
> ---
> 
> ### Checklist Rápido:
> 
> |Tipo de Función|¿Dónde verificar?|
> |---|---|
> |Polinomio |Automáticamente continua |
> | Racional | Puntos donde denominador = 0 | 
> | Con raíces | Puntos donde radicando = 0 o cambia de signo | 
> | Con logaritmo | Puntos donde argumento = 0 | 
> | Por partes | **Todas las fronteras entre regiones** | 
> | Con valor absoluto | Generalmente continua, verificar casos especiales | 
> | Trigonométrica | Puntos donde hay indeterminaciones |

---

## 📚 Ejemplos Adicionales

### Ejemplo 9: Continuidad de Función Compuesta

> [!example]- 📝 Ejemplo 9: Composición Compleja
> 
> **Función:** $$f(x,y) = e^{\sin(x^2 + y^2)}$$
> 
> **Análisis por composición:**
> 
> Esta función es la composición:
> 
> - $u(x,y) = x^2 + y^2$ → continua en $\mathbb{R}^2$ (polinomio)
> - $v(u) = \sin(u)$ → continua en $\mathbb{R}$ (trigonométrica)
> - $w(v) = e^v$ → continua en $\mathbb{R}$ (exponencial)
> - $f(x,y) = w(v(u(x,y)))$
> 
> **Por el teorema de composición:** Como cada función es continua en su dominio, la composición es continua.
> 
> **Conclusión:** $f(x,y) = e^{\sin(x^2 + y^2)}$ es continua en todo $\mathbb{R}^2$ ✓

### Ejemplo 10: Función con Raíz

> [!example]- 📝 Ejemplo 10: Verificar Continuidad en la Frontera
> 
> **Función:** $$f(x,y) = \sqrt{4 - x^2 - y^2}$$
> 
> **Dominio:** $D = {(x,y) : x^2 + y^2 \leq 4}$ (disco cerrado de radio 2)
> 
> **En el interior** ($x^2 + y^2 < 4$):
> 
> - El radicando es positivo
> - La raíz cuadrada es continua
> - Por lo tanto, $f$ es continua
> 
> **En la frontera** ($x^2 + y^2 = 4$):
> 
> Sea $(x_0, y_0)$ tal que $x_0^2 + y_0^2 = 4$.
> 
> $$\lim_{(x,y) \to (x_0,y_0)} \sqrt{4 - x^2 - y^2} = \sqrt{4 - x_0^2 - y_0^2} = \sqrt{0} = 0$$
> 
> $$f(x_0, y_0) = \sqrt{4 - 4} = 0$$
> 
> El límite coincide con el valor: **continua en la frontera** ✓
> 
> **Conclusión:** $f$ es continua en todo su dominio $D$

### Ejemplo 11: Discontinuidad No Removible

> [!example]- 📝 Ejemplo 11: Verificar que NO se puede Arreglar
> 
> **Función:** $$f(x,y) = \begin{cases} \frac{x^2y}{x^4 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **Verificación del límite en $(0,0)$:**
> 
> **Por el eje Y** ($x = 0$): $$\lim_{y \to 0} \frac{0 \cdot y}{0 + y^2} = 0$$
> 
> **Por la parábola $y = x^2$:** $$\lim_{x \to 0} \frac{x^2 \cdot x^2}{x^4 + x^4} = \lim_{x \to 0} \frac{x^4}{2x^4} = \frac{1}{2}$$
> 
> **Conclusión:**
> 
> - Los límites por diferentes caminos son diferentes: $0 \neq \frac{1}{2}$
> - El límite **NO existe**
> - La discontinuidad es **esencial** (no removible)
> - No importa cómo redefinamos $f(0,0)$, seguirá siendo discontinua

### Ejemplo 12: Función Absoluto

> [!example]- 📝 Ejemplo 12: Continuidad del Valor Absoluto
> 
> **Función:** $$f(x,y) = |x + y|$$
> 
> **Análisis:**
> 
> El valor absoluto de una función continua es continuo.
> 
> - $g(x,y) = x + y$ es continua (polinomio)
> - $h(u) = |u|$ es continua
> - $f(x,y) = h(g(x,y))$ es continua por composición
> 
> **Verificación en $(0,0)$:** $$\lim_{(x,y) \to (0,0)} |x + y| = |0 + 0| = 0 = f(0,0)$$ ✓
> 
> **Conclusión:** $f(x,y) = |x + y|$ es continua en todo $\mathbb{R}^2$

### Ejemplo 13: Función Definida por Partes (Compleja)

> [!example]- 📝 Ejemplo 13: Múltiples Regiones
> 
> **Función:** $$f(x,y) = \begin{cases} x^2 + y^2 & \text{si } x^2 + y^2 \leq 1 \ 1 & \text{si } 1 < x^2 + y^2 \leq 2 \ 4 - x^2 - y^2 & \text{si } x^2 + y^2 > 2 \end{cases}$$
> 
> **Verificación:**
> 
> **Interior de cada región:** Continua (funciones conocidas)
> 
> **Frontera 1:** $x^2 + y^2 = 1$
> 
> Desde dentro: $$\lim_{\substack{(x,y) \to (x_0,y_0) \ x^2+y^2 < 1}} (x^2 + y^2) = 1$$
> 
> Valor en la frontera (región 2): $$f(x_0, y_0) = 1$$
> 
> Coinciden ✓
> 
> **Frontera 2:** $x^2 + y^2 = 2$
> 
> Desde la región 2: $$\lim_{\substack{(x,y) \to (x_0,y_0) \ 1 < x^2+y^2 < 2}} 1 = 1$$
> 
> Desde la región 3: $$\lim_{\substack{(x,y) \to (x_0,y_0) \ x^2+y^2 > 2}} (4 - x^2 - y^2) = 4 - 2 = 2$$
> 
> **Problema:** $1 \neq 2$
> 
> **Conclusión:**
> 
> - Continua en las regiones 1 y 2
> - **Discontinua** en la circunferencia $x^2 + y^2 = 2$
> - Discontinuidad de **salto**

### Ejemplo 14: Función Trigonométrica con Singularidad

> [!example]- 📝 Ejemplo 14: Extender por Continuidad
> 
> **Función:** $$f(x,y) = \frac{\sin(x^2 + y^2)}{x^2 + y^2} \quad \text{para } (x,y) \neq (0,0)$$
> 
> **Pregunta:** ¿Cómo definir $f(0,0)$ para que sea continua?
> 
> **Cálculo del límite:**
> 
> Sea $u = x^2 + y^2$. Cuando $(x,y) \to (0,0)$, entonces $u \to 0^+$.
> 
> $$\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2} = \lim_{u \to 0^+} \frac{\sin(u)}{u} = 1$$
> 
> **Definición extendida:** $$f(x,y) = \begin{cases} \frac{\sin(x^2 + y^2)}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 1 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **Conclusión:** Con esta definición, $f$ es continua en todo $\mathbb{R}^2$ ✓

### Ejemplo 15: Aplicación del TVE

> [!example]- 📝 Ejemplo 15: Encontrar Extremos
> 
> **Función:** $$f(x,y) = x^2 + y^2 - 2x - 4y + 10$$
> 
> **Dominio:** $D = {(x,y) : x^2 + y^2 \leq 9}$ (disco cerrado)
> 
> **Análisis:**
> 
> 1. $f$ es continua (polinomio)
> 2. $D$ es compacto (cerrado y acotado)
> 3. Por el **TVE**, $f$ alcanza máximo y mínimo en $D$
> 
> **Completando cuadrados:** $$f(x,y) = (x-1)^2 + (y-2)^2 + 5$$
> 
> **Mínimo:**
> 
> - Ocurre en $(1, 2)$
> - ¿Está en $D$? → $1^2 + 2^2 = 5 < 9$ ✓
> - Valor mínimo: $f(1,2) = 0 + 0 + 5 = 5$
> 
> **Máximo:**
> 
> - Debe estar en la frontera $x^2 + y^2 = 9$
> - La función crece con la distancia de $(1,2)$
> - Punto más lejano de $(1,2)$ en la circunferencia
> 
> **Conclusión:** El TVE **garantiza** que estos extremos existen.

---

## 🔄 Continuidad Uniforme

> [!note]- 🎯 Concepto Avanzado: Continuidad Uniforme
> 
> ### Definición
> 
> Una función $f$ es **uniformemente continua** en $D$ si:
> 
> Para todo $\varepsilon > 0$, existe $\delta > 0$ tal que para **cualesquiera** puntos $(x_1, y_1), (x_2, y_2) \in D$:
> 
> $$\text{Si } \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2} < \delta \implies |f(x_1,y_1) - f(x_2,y_2)| < \varepsilon$$
> 
> **Diferencia con continuidad ordinaria:**
> 
> - **Continuidad:** El $\delta$ puede depender del punto
> - **Continuidad uniforme:** El mismo $\delta$ funciona para **todos** los puntos
> 
> ---
> 
> ### Teorema de Heine-Cantor
> 
> Si $f$ es continua en un conjunto **compacto** $D$, entonces $f$ es **uniformemente continua** en $D$.
> 
> **Implicación:** En conjuntos compactos, la continuidad es "más fuerte" y más manejable.
> 
> ---
> 
> ### Ejemplo:
> 
> **Función:** $f(x,y) = x^2 + y^2$
> 
> - En el disco $x^2 + y^2 \leq 1$ (compacto): **uniformemente continua**
> - En todo $\mathbb{R}^2$ (no compacto): continua pero **NO uniformemente continua**

---

## 🎨 Visualización de Discontinuidades

> [!note]- 🖼️ Interpretación Gráfica
> 
> ### Función Continua:
> 
> ```
>         z
>         |
>         |    ___
>         |   /   \
>         |  /     \    ← Superficie suave
>         | /       \
>         |/         \
>         +----------- y
>        /
>       x
> ```
> 
> "Puedes dibujarla sin levantar el lápiz"
> 
> ---
> 
> ### Discontinuidad Removible:
> 
> ```
>         z
>         |
>         |    ___
>         |   /   \
>         |  /  o  \    ← Agujero removible
>         | /   ↓   \
>         |/         \
>         +----------- y
>        /
>       x
> ```
> 
> "Un agujero que se puede 'rellenar'"
> 
> ---
> 
> ### Discontinuidad Esencial:
> 
> ```
>         z
>         |
>         |    ___      ___
>         |   /   \    /   \  ← Salto o torsión
>         |  /     ✗✗✗     \
>         | /               \
>         |/                 \
>         +------------------- y
>        /
>       x
> ```
> 
> "Imposible de reparar"
> 
> ---
> 
> ### Discontinuidad Infinita:
> 
> ```
>         z
>       ∞ |     |
>         |     |
>         |    /|\      ← Pico infinito
>         |   / | \
>         |__/  |  \__
>         +-----o----- y
>        /    punto
>       x   singular
> ```
> 
> "Una 'chimenea' infinita"

---

## 🧮 Continuidad en Coordenadas Polares

> [!tip]- 🔄 Análisis en Polares
> 
> ### Conversión
> 
> Para analizar continuidad en el origen usando coordenadas polares:
> 
> $$\begin{cases} x = r\cos\theta \ y = r\sin\theta \ r = \sqrt{x^2 + y^2} \end{cases}$$
> 
> **Continuidad en $(0,0)$:**
> 
> $f$ es continua en el origen si: $$\lim_{r \to 0^+} f(r\cos\theta, r\sin\theta) = f(0,0)$$ **independientemente** de $\theta$.
> 
> ---
> 
> ### Ejemplo:
> 
> **Función:** $$f(x,y) = \begin{cases} \frac{x^3 + y^3}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **En polares:** $$f(r\cos\theta, r\sin\theta) = \frac{r^3(\cos^3\theta + \sin^3\theta)}{r^2} = r(\cos^3\theta + \sin^3\theta)$$
> 
> **Límite cuando $r \to 0$:** $$\lim_{r \to 0^+} r(\cos^3\theta + \sin^3\theta) = 0$$
> 
> Como $|\cos^3\theta + \sin^3\theta| \leq 2$, el límite es 0 para todo $\theta$.
> 
> **Conclusión:** $$\lim_{(x,y) \to (0,0)} f(x,y) = 0 = f(0,0)$$
> 
> La función es **continua** en el origen ✓

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Determinar si las siguientes funciones son continuas en todo su dominio:**
> 
> a) $f(x,y) = x^3 + 2x^2y + y^3$
> 
> b) $f(x,y) = \frac{x + y}{x - y}$
> 
> c) $f(x,y) = \sqrt{9 - x^2 - y^2}$
> 
> d) $f(x,y) = e^{x-y}$
> 
> e) $f(x,y) = \ln(x^2 + y^2)$
> 
> ---
> 
> **2. Para cada función, identificar puntos de discontinuidad:**
> 
> a) $f(x,y) = \frac{1}{(x-1)^2 + y^2}$
> 
> b) $f(x,y) = \frac{xy}{x^2 - y^2}$
> 
> c) $f(x,y) = \tan\left(\frac{x}{y}\right)$
> 
> d) $f(x,y) = \frac{1}{\sqrt{x^2 + y^2 - 1}}$
> 
> ---
> 
> **3. Determinar el valor de $k$ para que la función sea continua:**
> 
> a) $f(x,y) = \begin{cases} \frac{x^2 - y^2}{x + y} & \text{si } x + y \neq 0 \ k & \text{si } x + y = 0 \end{cases}$
> 
> En el punto $(1, -1)$.
> 
> b) $f(x,y) = \begin{cases} \frac{\sin(x^2 + y^2)}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ k & \text{si } (x,y) = (0,0) \end{cases}$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Verificar continuidad en el origen:**
> 
> a) $f(x,y) = \begin{cases} \frac{xy^2}{x^2 + y^4} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$
> 
> b) $f(x,y) = \begin{cases} \frac{x^2y}{x^4 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$
> 
> c) $f(x,y) = \begin{cases} (x^2 + y^2)\sin\left(\frac{1}{x^2 + y^2}\right) & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$
> 
> ---
> 
> **5. Funciones definidas por partes - verificar continuidad:**
> 
> a) $f(x,y) = \begin{cases} x^2 + y^2 & \text{si } x^2 + y^2 \leq 1 \ 2\sqrt{x^2 + y^2} - 1 & \text{si } x^2 + y^2 > 1 \end{cases}$
> 
> b) $f(x,y) = \begin{cases} xy & \text{si } |x| + |y| \leq 1 \ 1 & \text{si } |x| + |y| > 1 \end{cases}$
> 
> ---
> 
> **6. Aplicar el Teorema del Valor Extremo:**
> 
> a) $f(x,y) = x^2 + 2y^2$ en el disco $x^2 + y^2 \leq 4$
> 
> b) $f(x,y) = xy$ en el rectángulo $[0,1] \times [0,2]$
> 
> c) $f(x,y) = e^{-(x^2+y^2)}$ en $\mathbb{R}^2$ (¿se aplica el TVE?)

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Problemas conceptuales:**
> 
> a) Demostrar que si $f$ y $g$ son continuas en $(x_0, y_0)$, entonces $f + g$ es continua en $(x_0, y_0)$.
> 
> b) Dar un ejemplo de una función discontinua en el origen pero continua en todo otro punto.
> 
> c) Construir una función que sea continua solo en un punto.
> 
> ---
> 
> **8. Extensiones por continuidad:**
> 
> a) $f(x,y) = \frac{e^{xy} - 1}{xy}$ para $(x,y) \neq (0,0)$
> 
> Definir $f(0,0)$ para que sea continua.
> 
> b) $f(x,y) = \frac{\ln(1 + x^2 + y^2)}{x^2 + y^2}$ para $(x,y) \neq (0,0)$
> 
> ---
> 
> **9. Continuidad uniforme:**
> 
> a) Demostrar que $f(x,y) = x^2 + y^2$ es uniformemente continua en el disco $x^2 + y^2 \leq 1$.
> 
> b) Demostrar que $f(x,y) = xy$ NO es uniformemente continua en $\mathbb{R}^2$.
> 
> ---
> 
> **10. Aplicaciones:**
> 
> a) La temperatura en una placa está dada por $T(x,y) = 100 - x^2 - y^2$ en el cuadrado $[-5,5] \times [-5,5]$. ¿Garantiza el TVE que hay una temperatura máxima? Encuéntrala.
> 
> b) La densidad de población es $\rho(x,y) = \frac{1000}{1 + x^2 + y^2}$. ¿Es continua en todo $\mathbb{R}^2$? ¿Dónde alcanza su máximo?

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = x^3 + 2x^2y + y^3$
> 
> Es un polinomio → **Continua en todo** $\mathbb{R}^2$ ✓
> 
> ---
> 
> **1b)** $f(x,y) = \frac{x + y}{x - y}$
> 
> Función racional → Continua donde $x - y \neq 0$
> 
> **Discontinua** en la recta $y = x$
> 
> ---
> 
> **1c)** $f(x,y) = \sqrt{9 - x^2 - y^2}$
> 
> Dominio: $x^2 + y^2 \leq 9$
> 
> Raíz cuadrada de función continua → **Continua en su dominio**
> 
> ---
> 
> **1d)** $f(x,y) = e^{x-y}$
> 
> Exponencial de función continua → **Continua en** $\mathbb{R}^2$ ✓
> 
> ---
> 
> **1e)** $f(x,y) = \ln(x^2 + y^2)$
> 
> Dominio: $x^2 + y^2 > 0$ → $(x,y) \neq (0,0)$
> 
> **Continua en** $\mathbb{R}^2 \setminus {(0,0)}$
> 
> **Discontinuidad infinita** en el origen
> 
> ---
> 
> **2a)** $f(x,y) = \frac{1}{(x-1)^2 + y^2}$
> 
> **Discontinua** en $(1, 0)$ (denominador = 0)
> 
> Discontinuidad **infinita**
> 
> ---
> 
> **3a)** $f(x,y) = \begin{cases} \frac{x^2 - y^2}{x + y} & \text{si } x + y \neq 0 \ k & \text{si } x + y = 0 \end{cases}$
> 
> En $(1, -1)$:
> 
> $$\lim_{(x,y) \to (1,-1)} \frac{(x-y)(x+y)}{x+y} = \lim_{(x,y) \to (1,-1)} (x - y) = 1 - (-1) = 2$$
> 
> Para continuidad: $k = 2$ ✓
> 
> ---
> 
> **3b)**
> 
> $$\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2} = 1$$
> 
> Para continuidad: $k = 1$ ✓

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $f(x,y) = \begin{cases} \frac{xy^2}{x^2 + y^4} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$
> 
> **Por $y = 0$:** Límite = 0
> 
> **Por $y = x$:** $$\lim_{x \to 0} \frac{x \cdot x^2}{x^2 + x^4} = \lim_{x \to 0} \frac{x^3}{x^2(1 + x^2)} = \lim_{x \to 0} \frac{x}{1 + x^2} = 0$$
> 
> **Por $x = y^2$:** $$\lim_{y \to 0} \frac{y^2 \cdot y^2}{y^4 + y^4} = \lim_{y \to 0} \frac{y^4}{2y^4} = \frac{1}{2}$$
> 
> Como $0 \neq \frac{1}{2}$: **Discontinua** en el origen ✗
> 
> ---
> 
> **4c)** $f(x,y) = \begin{cases} (x^2 + y^2)\sin\left(\frac{1}{x^2 + y^2}\right) & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$
> 
> Como $|\sin(u)| \leq 1$:
> 
> $$\left|(x^2 + y^2)\sin\left(\frac{1}{x^2 + y^2}\right)\right| \leq x^2 + y^2 \to 0$$
> 
> Por teorema del sandwich: $$\lim_{(x,y) \to (0,0)} f(x,y) = 0 = f(0,0)$$
> 
> **Continua** en el origen ✓
> 
> ---
> 
> **5a)** Verificar en la frontera $x^2 + y^2 = 1$:
> 
> Desde dentro: $\lim = 1$
> 
> Desde fuera: $\lim = 2\sqrt{1} - 1 = 1$
> 
> Valor en la frontera: $f = 1$
> 
> **Continua** en todo $\mathbb{R}^2$ ✓
> 
> ---
> 
> **6a)** $f(x,y) = x^2 + 2y^2$ en $D = {x^2 + y^2 \leq 4}$
> 
> - $f$ es continua (polinomio)
> - $D$ es compacto (cerrado y acotado)
> - Por TVE: existen máximo y mínimo
> 
> **Mínimo:** $f(0,0) = 0$
> 
> **Máximo:** En la frontera $x^2 + y^2 = 4$
> 
> - Máximo cuando $y = \pm 2$, $x = 0$: $f(0, \pm 2) = 8$

---

## 🌟 Aplicaciones Prácticas

> [!note]- 🔬 Aplicaciones de la Continuidad
> 
> ### 1. Física
> 
> **Distribución de temperatura:**
> 
> - La temperatura en una placa debe ser continua (no hay saltos instantáneos)
> - $T(x,y)$ continua garantiza transiciones su aves de temperatura

> - Importante para análisis térmico y conducción de calor
> 
> **Campos de fuerza:**
> 
> - Campos gravitatorios, eléctricos y magnéticos son continuos
> - $\vec{F}(x,y,z)$ continua → no hay fuerzas infinitas en puntos finitos
> 
> ---
> 
> ### 2. Ingeniería
> 
> **Análisis de estructuras:**
> 
> - La tensión en una viga: $\sigma(x,y)$ debe ser continua
> - Discontinuidades → puntos de fractura potenciales
> - TVE garantiza existencia de tensión máxima
> 
> **Diseño de superficies:**
> 
> - Carrocerías de autos, alas de aviones
> - Superficies continuas → mejor aerodinámica
> - Funciones spline para interpolación suave
> 
> ---
> 
> ### 3. Economía
> 
> **Funciones de utilidad:**
> 
> - $U(x,y)$ = utilidad del consumo de bienes $x$ e $y$
> - Continuidad → preferencias racionales
> - TVE en presupuesto compacto → existe elección óptima
> 
> **Isocuantas y curvas de indiferencia:**
> 
> - Deben ser continuas para representar sustitución gradual
> 
> ---
> 
> ### 4. Ciencias de la Computación
> 
> **Procesamiento de imágenes:**
> 
> - Una imagen $I(x,y)$ (intensidad de píxeles)
> - Filtros de suavizado → hacer la función más continua
> - Detección de bordes → buscar discontinuidades
> 
> **Interpolación de datos:**
> 
> - Dados puntos discretos, construir función continua
> - Métodos: interpolación lineal, bicúbica, splines
> 
> ---
> 
> ### 5. Biología
> 
> **Concentración de sustancias:**
> 
> - Difusión de nutrientes: $C(x,y,t)$ continua
> - Gradientes de concentración → dirección de difusión
> 
> **Modelos de población:**
> 
> - Densidad de población: $\rho(x,y)$ típicamente continua
> - Continuidad permite predecir migraciones

---

## 🔍 Temas Relacionados y Conexiones

> [!info]- 🌐 Profundización: Conceptos Topológicos
> 
> ### Conjuntos Abiertos y Cerrados
> 
> **Conjunto Abierto:** Un conjunto $A \subseteq \mathbb{R}^2$ es abierto si cada punto de $A$ está contenido en un disco completamente dentro de $A$.
> 
> **Ejemplos:**
> 
> - ${(x,y) : x^2 + y^2 < 1}$ (abierto)
> - ${(x,y) : x > 0}$ (abierto)
> 
> ---
> 
> **Conjunto Cerrado:** Un conjunto es cerrado si contiene todos sus puntos límite (su complemento es abierto).
> 
> **Ejemplos:**
> 
> - ${(x,y) : x^2 + y^2 \leq 1}$ (cerrado)
> - ${(x,y) : y \geq x^2}$ (cerrado)
> 
> ---
> 
> ### Caracterización de Continuidad
> 
> **Teorema (Topológico):** $f: D \to \mathbb{R}$ es continua si y solo si la **preimagen** de todo conjunto abierto es abierta.
> 
> **Preimagen:** $f^{-1}(U) = {(x,y) \in D : f(x,y) \in U}$
> 
> **Aplicación:** Esta caracterización es fundamental en topología y análisis avanzado.
> 
> ---
> 
> ### Puntos de Acumulación
> 
> **Definición:** $(x_0, y_0)$ es un punto de acumulación de $D$ si todo disco centrado en $(x_0, y_0)$ contiene puntos de $D$ distintos de $(x_0, y_0)$.
> 
> **Importancia:** Para que tenga sentido hablar del límite en un punto, ese punto debe ser de acumulación del dominio.

---

## 📊 Tabla Comparativa: Tipos de Continuidad

> [!note]- 📋 Resumen Comparativo
> 
> |Tipo|Definición|Ejemplo|¿Removible?|
> |---|---|---|---|
> |**Continua**|$\lim f = f(p)$|$f(x,y) = x^2 + y^2$|N/A|
> |**Removible**|$\lim f \neq f(p)$ pero límite existe|$\frac{x^2-y^2}{x-y}$ en $y=x$|✅ Sí|
> |**Esencial**|Límite no existe|$\frac{xy}{x^2+y^2}$ en $(0,0)$|❌ No|
> |**Infinita**|$\lim f = \pm\infty$|$\frac{1}{x^2+y^2}$ en $(0,0)$|❌ No|
> |**Salto**|Límites laterales diferentes|Función escalón 2D|❌ No|
> 
> ---
> 
> ### Consecuencias de la Continuidad
> 
> |Propiedad|Requiere|Garantiza|
> |---|---|---|
> |**TVI**|Continuidad + Conexidad|Valores intermedios|
> |**TVE**|Continuidad + Compacidad|Existencia de extremos|
> |**Diferenciabilidad**|Continuidad de derivadas|Aproximación lineal|
> |**Integrabilidad**|Continuidad (o casi)|Existencia de integral|

---

## 💡 Consejos y Errores Comunes

> [!tip]- ⚠️ Errores Frecuentes
> 
> ### Error 1: Confundir "definida" con "continua"
> 
> ❌ **Incorrecto:** "Si $f(x_0, y_0)$ está definida, entonces $f$ es continua ahí"
> 
> ✅ **Correcto:** Necesitamos tres condiciones: definida + límite existe + límite = valor
> 
> **Contraejemplo:** $$f(x,y) = \begin{cases} \frac{xy}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$$
> 
> Está definida en $(0,0)$ pero **NO es continua** ahí.
> 
> ---
> 
> ### Error 2: Verificar solo ejes coordenados
> 
> ❌ **Incorrecto:** "El límite es el mismo por ejes X e Y → función continua"
> 
> ✅ **Correcto:** Debemos verificar **todas las direcciones** (infinitas)
> 
> **Contraejemplo:** $$f(x,y) = \frac{xy}{x^2+y^2}$$
> 
> Por ejes da 0, pero por $y=x$ da $\frac{1}{2}$.
> 
> ---
> 
> ### Error 3: Olvidar verificar fronteras en funciones por partes
> 
> ❌ **Incorrecto:** "Cada parte es continua → toda la función es continua"
> 
> ✅ **Correcto:** Debemos verificar **explícitamente** las fronteras entre regiones
> 
> **Ejemplo:** $$f(x,y) = \begin{cases} 1 & x^2+y^2 < 1 \ 2 & x^2+y^2 \geq 1 \end{cases}$$
> 
> Cada región continua, pero **discontinua en la circunferencia**.
> 
> ---
> 
> ### Error 4: Aplicar TVE sin verificar compacidad
> 
> ❌ **Incorrecto:** "Función continua → tiene máximo y mínimo"
> 
> ✅ **Correcto:** TVE requiere dominio **compacto** (cerrado Y acotado)
> 
> **Contraejemplo:** $f(x,y) = x^2 + y^2$ en todo $\mathbb{R}^2$
> 
> Continua pero **no tiene máximo** (no acotado).
> 
> ---
> 
> ### Error 5: Confundir límites iterados con límite doble
> 
> ❌ **Incorrecto:** "Los límites iterados existen y coinciden → función continua"
> 
> ✅ **Correcto:** Límites iterados **NO garantizan** continuidad (ni límite doble)
> 
> **Contraejemplo:** $$f(x,y) = \frac{xy}{x^2+y^2}$$
> 
> Ambos límites iterados son 0, pero el límite doble no existe.

---

## 🎯 Estrategias de Demostración

> [!tip]- 🔧 Técnicas para Probar Continuidad
> 
> ### Técnica 1: Usar Funciones Conocidas
> 
> **Funciones elementales continuas:**
> 
> - Polinomios
> - Exponenciales
> - Trigonométricas
> - Logaritmos (en su dominio)
> 
> **Luego usar álgebra de funciones continuas:**
> 
> - Suma, resta, producto, cociente (si denominador $\neq 0$)
> - Composición
> 
> ---
> 
> ### Técnica 2: Definición $\varepsilon$-$\delta$
> 
> **Útil para demostraciones rigurosas:**
> 
> Para probar que $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$:
> 
> 1. Fijar $\varepsilon > 0$ arbitrario
> 2. Encontrar $\delta > 0$ en términos de $\varepsilon$
> 3. Demostrar: si $\sqrt{(x-x_0)^2 + (y-y_0)^2} < \delta$ entonces $|f(x,y) - L| < \varepsilon$
> 
> **Ejemplo:** Probar que $f(x,y) = 3x + 4y$ es continua en $(0,0)$.
> 
> Queremos: $|3x + 4y - 0| < \varepsilon$
> 
> $$|3x + 4y| \leq 3|x| + 4|y| \leq 3\sqrt{x^2+y^2} + 4\sqrt{x^2+y^2} = 7\sqrt{x^2+y^2}$$
> 
> Tomamos $\delta = \frac{\varepsilon}{7}$:
> 
> Si $\sqrt{x^2+y^2} < \delta = \frac{\varepsilon}{7}$, entonces: $$|3x + 4y| \leq 7\sqrt{x^2+y^2} < 7 \cdot \frac{\varepsilon}{7} = \varepsilon$$ ✓
> 
> ---
> 
> ### Técnica 3: Coordenadas Polares
> 
> **Para continuidad en el origen:**
> 
> Mostrar que $\lim_{r \to 0} f(r\cos\theta, r\sin\theta)$ existe y es independiente de $\theta$.
> 
> ---
> 
> ### Técnica 4: Teorema del Sandwich
> 
> **Para probar que límite = 0:**
> 
> Encontrar cotas: $$0 \leq |f(x,y) - L| \leq g(x,y)$$
> 
> donde $\lim_{(x,y) \to (x_0,y_0)} g(x,y) = 0$.

---

## 🔄 Extensión a Tres Variables

> [!note]- 🎲 Continuidad en $\mathbb{R}^3$
> 
> ### Definición
> 
> $f: D \subseteq \mathbb{R}^3 \to \mathbb{R}$ es continua en $(x_0, y_0, z_0)$ si:
> 
> $$\lim_{(x,y,z) \to (x_0,y_0,z_0)} f(x,y,z) = f(x_0, y_0, z_0)$$
> 
> **Equivalentemente ($\varepsilon$-$\delta$):**
> 
> Para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
> 
> $$\sqrt{(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2} < \delta \implies |f(x,y,z) - f(x_0,y_0,z_0)| < \varepsilon$$
> 
> ---
> 
> ### Ejemplos
> 
> **1. Continua:** $$f(x,y,z) = x^2 + y^2 + z^2$$ Polinomio → continua en todo $\mathbb{R}^3$
> 
> **2. Discontinua:** $$f(x,y,z) = \frac{xyz}{x^2 + y^2 + z^2}$$ Discontinua en el origen (límite depende del camino)
> 
> **3. Con restricción:** $$f(x,y,z) = \sqrt{1 - x^2 - y^2 - z^2}$$ Continua en la bola $x^2 + y^2 + z^2 \leq 1$
> 
> ---
> 
> ### Coordenadas Esféricas
> 
> Para analizar continuidad en el origen: $$\begin{cases} x = \rho\sin\phi\cos\theta \ y = \rho\sin\phi\sin\theta \ z = \rho\cos\phi \end{cases}$$
> 
> La función es continua en el origen si: $$\lim_{\rho \to 0} f(\rho\sin\phi\cos\theta, \rho\sin\phi\sin\theta, \rho\cos\phi)$$
> 
> existe e es independiente de $\phi$ y $\theta$.

---

## 📈 Gráficas y Visualización

> [!note]- 🎨 Interpretación Visual de la Continuidad
> 
> ### Función Continua: Paraboloide
> 
> $$f(x,y) = x^2 + y^2$$
> 
> ```
> Superficie suave, sin interrupciones
> 
>         z
>         |    /\
>         |   /  \
>         |  |    |    ← Forma de cuenco
>         | /      \
>         |/        \
>         +---------- y
>        /
>       x
> ```
> 
> ---
> 
> ### Discontinuidad Removible
> 
> $$f(x,y) = \frac{x^2-y^2}{x-y}, \quad x \neq y$$
> 
> ```
> Superficie con una "línea de agujeros"
> 
>         z
>         |    
>         |   ╱╲
>         |  ╱  ╲
>         | ╱ ⊙⊙ ╲   ← Agujeros en y=x
>         |╱      ╲
>         +---------- y
>        /
>       x
> ```
> 
> ---
> 
> ### Discontinuidad Esencial
> 
> $$f(x,y) = \frac{xy}{x^2+y^2}$$
> 
> ```
> Superficie que "gira" al acercarse al origen
> 
>         z
>       ½ |   ╱
>         |  ╱
>         | ╱  ⟲    ← Diferentes valores
>         |╱   ⟳      según dirección
>         +---------- y
>      -½ ╲
>         ╲
>       x
> ```
> 
> ---
> 
> ### Discontinuidad Infinita
> 
> $$f(x,y) = \frac{1}{x^2+y^2}$$
> 
> ```
> "Chimenea" infinita en el origen
> 
>         z
>       ∞ |  │
>         |  │
>         | ╱│╲      ← Tiende a infinito
>         |╱ │ ╲
>         +--o-- y
>        /  origen
>       x
> ```

---

## 🎓 Resumen de Conceptos Clave

> [!tip]- 💡 Puntos Esenciales para Recordar
> 
> ### Definición de Continuidad
> 
> ✅ **Tres condiciones necesarias:**
> 
> 1. $f(x_0, y_0)$ definida
> 2. $\lim_{(x,y) \to (x_0,y_0)} f(x,y)$ existe
> 3. Límite = valor de la función
> 
> ---
> 
> ### Propiedades Importantes
> 
> ✅ **Álgebra de funciones continuas:**
> 
> - Suma, resta, producto de continuas → continua
> - Cociente continuo si denominador $\neq 0$
> - Composición de continuas → continua
> 
> ✅ **Funciones elementales:**
> 
> - Polinomios: siempre continuos
> - Racionales: continuas donde denominador $\neq 0$
> - Exponenciales y trigonométricas: continuas en su dominio
> 
> ---
> 
> ### Teoremas Fundamentales
> 
> ✅ **Teorema del Valor Intermedio:**
> 
> - Requiere: continuidad + conexidad
> - Garantiza: valores intermedios
> 
> ✅ **Teorema del Valor Extremo:**
> 
> - Requiere: continuidad + compacidad
> - Garantiza: existencia de máximo y mínimo
> 
> ---
> 
> ### Tipos de Discontinuidad
> 
> 🔴 **Removible:** límite existe pero $\neq$ valor 🔴 **Esencial:** límite no existe 🔴 **Infinita:** límite = $\pm\infty$ 🔴 **Salto:** en funciones por partes
> 
> ---
> 
> ### Estrategias de Verificación
> 
> 📍 **Funciones por partes:** verificar **fronteras** 📍 **En el origen:** usar polares o sandwich 📍 **Extensión continua:** calcular límite y definir ahí 📍 **Dominio:** primero identificar dónde está definida

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema es prerequisito para:**
> 
> - [[08 - Derivadas Parciales]] - Las derivadas requieren continuidad
> - [[09 - Diferenciabilidad]] - Diferenciable → continua (pero no viceversa)
> - [[10 - Regla de la Cadena]] - Se basa en composición de funciones continuas
> - [[15 - Optimización]] - TVE garantiza existencia de extremos
> - [[20 - Integrales Dobles]] - Funciones continuas son integrables
> 
> **Conceptos relacionados:**
> 
> - **Límites** - Base fundamental de continuidad
> - **Topología** - Conjuntos abiertos, cerrados, compactos
> - **Diferenciabilidad** - Condición más fuerte que continuidad
> - **Integrabilidad** - Funciones continuas (o casi) son integrables
> 
> **Siguiente tema recomendado:** [[08 - Derivadas Parciales de Funciones de Varias Variables]]

---

## 📝 Notas Finales

> [!note]- 🎯 Reflexiones sobre Continuidad
> 
> ### Importancia Conceptual
> 
> La continuidad en varias variables es **más restrictiva** que en una variable:
> 
> - En 1D: solo 2 direcciones de aproximación
> - En 2D: infinitas direcciones de aproximación
> - En 3D: aún más complejo
> 
> Esto hace que:
> 
> - Sea **más difícil** probar que una función es continua
> - Sea **más fácil** probar que NO es continua (basta un camino)
> - Los teoremas sean **más potentes** cuando se aplican
> 
> ---
> 
> ### Conexión con la Intuición
> 
> **Interpretación física:**
> 
> - Una superficie continua es aquella que puedes "moldear con arcilla"
> - Sin rasgaduras, agujeros o picos infinitos
> - Pequeños cambios en posición → pequeños cambios en altura
> 
> **Relevancia práctica:**
> 
> - Modelado de fenómenos naturales
> - Interpolación y aproximación numérica
> - Base para cálculo diferencial e integral
> - Optimización y búsqueda de extremos
> 
> ---
> 
> ### Para Estudiar Más
> 
> **Conceptos avanzados:**
> 
> - Continuidad uniforme
> - Espacios métricos y topológicos
> - Teoremas de punto fijo
> - Continuidad de Hölder y Lipschitz
> 
> **Aplicaciones:**
> 
> - Ecuaciones diferenciales parciales
> - Análisis funcional
> - Teoría de la medida
> - Topología algebraica

---

**Tags:** #calculo-multivariable #continuidad #funciones-varias-variables #limites #teorema-valor-extremo #teorema-valor-intermedio #discontinuidad #topologia #compacidad
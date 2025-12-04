# 📘 Límite de Funciones de Varias Variables

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes los Límites en Varias Variables?
> 
> Los límites son fundamentales para entender el comportamiento de funciones cerca de un punto, incluso cuando la función no está definida ahí.
> 
> **Diferencia clave con funciones de una variable:**
> 
> - En $f(x)$: solo podemos acercarnos desde **2 direcciones** (izquierda o derecha)
> - En $f(x,y)$: podemos acercarnos desde **infinitas direcciones** en el plano
> - En $f(x,y,z)$: podemos acercarnos desde **infinitas direcciones** en el espacio
> 
> **Aplicaciones:**
> 
> - Determinar continuidad de funciones
> - Calcular derivadas parciales
> - Analizar comportamiento en fronteras del dominio
> - Optimización y análisis de superficies

---

## 📐 Definición de Límite

### 🔍 Definición Formal (Epsilon-Delta)

> [!example]- 🟢 Definición: Límite de una Función de Dos Variables
> 
> **Definición formal:** Sea $f$ una función definida en un conjunto $D \subseteq \mathbb{R}^2$ (excepto posiblemente en el punto $(x_0, y_0)$). Decimos que:
> 
> $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$$
> 
> si para todo $\varepsilon > 0$, existe un $\delta > 0$ tal que:
> 
> $$\text{Si } 0 < \sqrt{(x-x_0)^2 + (y-y_0)^2} < \delta \text{ entonces } |f(x,y) - L| < \varepsilon$$
> 
> **Interpretación geométrica:**
> 
> - $\sqrt{(x-x_0)^2 + (y-y_0)^2}$ es la **distancia** de $(x,y)$ a $(x_0,y_0)$
> - El límite existe si podemos hacer que $f(x,y)$ esté tan cerca de $L$ como queramos
> - Esto debe cumplirse **sin importar la dirección** desde la cual nos acerquemos

### 🎯 Definición Intuitiva

> [!note]- 💭 Interpretación Práctica
> 
> El límite $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$ significa:
> 
> **"Cuando $(x,y)$ se acerca a $(x_0,y_0)$ desde cualquier dirección, $f(x,y)$ se acerca a $L$"**
> 
> **Condiciones necesarias:**
> 
> 1. El límite debe ser el **mismo** desde todas las direcciones
> 2. El punto $(x_0,y_0)$ debe ser un **punto de acumulación** del dominio
> 3. No importa si $f$ está o no definida en $(x_0,y_0)$
> 
> **Notación alternativa:** $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L \quad \text{o} \quad f(x,y) \to L \text{ cuando } (x,y) \to (x_0,y_0)$$

---

## ⚠️ Diferencia con Límites en Una Variable

> [!warning]- 🔄 Conceptos Clave
> 
> ### En una variable: $\lim_{x \to a} f(x)$
> 
> - Solo **2 direcciones** de aproximación: izquierda ($x \to a^-$) y derecha ($x \to a^+$)
> - El límite existe si: $\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)$
> - Es relativamente "fácil" verificar
> 
> ```
>      f(x)
>       |
>       |    /
>       |   /
>     L |--o
>       |   \
>       |    \
>       +------→ x
>           a
> ```
> 
> ---
> 
> ### En dos variables: $\lim_{(x,y) \to (a,b)} f(x,y)$
> 
> - **Infinitas direcciones** de aproximación
> - Podemos acercarnos por:
>     - Líneas rectas: $y = mx + c$
>     - Parábolas: $y = x^2$
>     - Espirales, curvas, cualquier trayectoria...
> - El límite existe si es el **mismo** desde **todas** las direcciones
> 
> ```
>       y
>       |  ↖  ↑  ↗
>       |    \ | /
>       |  ←--o--→
>       |    / | \
>       |  ↙  ↓  ↘
>       +---------- x
>          (a,b)
> ```
> 
> **CONSECUENCIA IMPORTANTE:**
> 
> - Para probar que un límite **NO existe**: basta encontrar **dos caminos** con límites diferentes
> - Para probar que un límite **SÍ existe**: debemos verificar **todos** los caminos posibles (infinitos)

---

## 🛠️ Métodos para Calcular Límites

### 📍 Método 1: Sustitución Directa

> [!tip]- ✅ Cuando la Función es Continua en el Punto
> 
> **Aplicable cuando:**
> 
> - La función está definida en $(x_0, y_0)$
> - No hay indeterminaciones ($\frac{0}{0}$, $\frac{\infty}{\infty}$, etc.)
> 
> **Procedimiento:** Simplemente sustituir: $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = f(x_0,y_0)$
> 
> ---
> 
> **Ejemplo 1:** Límite directo
> 
> $$\lim_{(x,y) \to (2,3)} (x^2 + y^2 - xy)$$
> 
> **Solución:**
> 
> - No hay división por cero ni raíces problemáticas
> - Sustituimos directamente:
> 
> $$= 2^2 + 3^2 - (2)(3) = 4 + 9 - 6 = 7$$
> 
> **Respuesta:** $\boxed{7}$
> 
> ---
> 
> **Ejemplo 2:** Con funciones trigonométricas
> 
> $$\lim_{(x,y) \to (0,\pi/4)} \sin(x) + \cos(y)$$
> 
> **Solución:** $$= \sin(0) + \cos(\pi/4) = 0 + \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{2}$$
> 
> **Respuesta:** $\boxed{\frac{\sqrt{2}}{2}}$

### 📍 Método 2: Trayectorias Específicas

> [!tip]- 🛤️ Probar que un Límite NO Existe
> 
> **Estrategia:** Si encontramos **dos caminos diferentes** que dan límites diferentes, entonces el límite **NO existe**.
> 
> **Caminos comunes a probar:**
> 
> 1. **Eje X:** $y = 0$ (hacer $y = 0$ y calcular límite en $x$)
> 2. **Eje Y:** $x = 0$ (hacer $x = 0$ y calcular límite en $y$)
> 3. **Recta $y = x$:** (hacer $y = x$)
> 4. **Recta $y = mx$:** (hacer $y = mx$ para $m$ arbitrario)
> 5. **Parábola $y = x^2$:** (hacer $y = x^2$)
> 6. **Parábola $x = y^2$:** (hacer $x = y^2$)
> 
> ---
> 
> **Ejemplo 3:** Límite que NO existe
> 
> $$\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2}$$
> 
> **Camino 1: Por el eje X** ($y = 0$)
> 
> $$\lim_{x \to 0} \frac{x \cdot 0}{x^2 + 0^2} = \lim_{x \to 0} \frac{0}{x^2} = 0$$
> 
> **Camino 2: Por la recta $y = x$**
> 
> $$\lim_{x \to 0} \frac{x \cdot x}{x^2 + x^2} = \lim_{x \to 0} \frac{x^2}{2x^2} = \lim_{x \to 0} \frac{1}{2} = \frac{1}{2}$$
> 
> **Conclusión:** Como $0 \neq \frac{1}{2}$, los límites por diferentes caminos son distintos.
> 
> $$\boxed{\text{El límite NO existe}}$$
> 
> ---
> 
> **Ejemplo 4:** Otro límite que NO existe
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^2 - y^2}{x^2 + y^2}$$
> 
> **Por el eje X** ($y = 0$): $$\lim_{x \to 0} \frac{x^2 - 0}{x^2 + 0} = 1$$
> 
> **Por el eje Y** ($x = 0$): $$\lim_{y \to 0} \frac{0 - y^2}{0 + y^2} = -1$$
> 
> **Conclusión:** $1 \neq -1$, por lo tanto:
> 
> $$\boxed{\text{El límite NO existe}}$$

### 📍 Método 3: Coordenadas Polares

> [!tip]- 🔄 Transformación a Coordenadas Polares
> 
> **Sustitución:** $$\begin{cases} x = r\cos\theta \ y = r\sin\theta \ r = \sqrt{x^2 + y^2} \end{cases}$$
> 
> **Cuando $(x,y) \to (0,0)$:** entonces $r \to 0$ (independientemente de $\theta$)
> 
> **El límite existe si:** $$\lim_{r \to 0} f(r\cos\theta, r\sin\theta) = L$$
> 
> es **independiente** de $\theta$.
> 
> ---
> 
> **Ejemplo 5:** Usando polares (límite existe)
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^2y}{x^2 + y^2}$$
> 
> **Sustitución:** $$x = r\cos\theta, \quad y = r\sin\theta$$
> 
> $$f = \frac{(r\cos\theta)^2 \cdot r\sin\theta}{r^2} = \frac{r^3\cos^2\theta\sin\theta}{r^2} = r\cos^2\theta\sin\theta$$
> 
> **Tomando límite:** $$\lim_{r \to 0} r\cos^2\theta\sin\theta = 0$$
> 
> Como $|\cos^2\theta\sin\theta| \leq 1$, tenemos: $$|r\cos^2\theta\sin\theta| \leq |r| \to 0$$
> 
> **Conclusión:** El límite existe y es:
> 
> $$\boxed{0}$$
> 
> ---
> 
> **Ejemplo 6:** Usando polares (límite NO existe)
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^3}{x^2 + y^2}$$
> 
> **Sustitución:** $$f = \frac{(r\cos\theta)^3}{r^2} = \frac{r^3\cos^3\theta}{r^2} = r\cos^3\theta$$
> 
> **Análisis:**
> 
> - El límite depende de $\theta$ a través de $\cos^3\theta$
> - Para $\theta = 0$: límite = $r \cdot 1 = r \to 0$
> - Para $\theta = \pi/2$: límite = $r \cdot 0 = 0$
> 
> **Pero** la expresión $r\cos^3\theta$ depende de $\theta$...
> 
> Probemos caminos específicos:
> 
> - **Por $y = 0$:** $\lim_{x \to 0} \frac{x^3}{x^2} = \lim_{x \to 0} x = 0$
> - **Por $y = x$:** $\lim_{x \to 0} \frac{x^3}{x^2 + x^2} = \lim_{x \to 0} \frac{x^3}{2x^2} = \lim_{x \to 0} \frac{x}{2} = 0$
> 
> **Parece que el límite es 0...**
> 
> Pero el término $r\cos^3\theta$ **no** tiende a 0 uniformemente en $\theta$. Necesitamos más análisis.

### 📍 Método 4: Teorema del Sandwich (Squeeze)

> [!tip]- 🥪 Acotar la Función
> 
> **Teorema del Sandwich:** Si $g(x,y) \leq f(x,y) \leq h(x,y)$ cerca de $(x_0, y_0)$ y
> 
> $$\lim_{(x,y) \to (x_0,y_0)} g(x,y) = \lim_{(x,y) \to (x_0,y_0)} h(x,y) = L$$
> 
> entonces:
> 
> $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$$
> 
> **Estrategia común:**
> 
> - Usar $|x| \leq \sqrt{x^2 + y^2}$ y $|y| \leq \sqrt{x^2 + y^2}$
> - Usar $|\sin\theta| \leq 1$ y $|\cos\theta| \leq 1$
> - Factorizar potencias de $r = \sqrt{x^2 + y^2}$
> 
> ---
> 
> **Ejemplo 7:** Usando squeeze theorem
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^2y^2}{x^2 + y^2}$$
> 
> **Análisis:**
> 
> Sabemos que $y^2 \leq x^2 + y^2$, entonces:
> 
> $$\frac{x^2y^2}{x^2 + y^2} \leq \frac{x^2(x^2 + y^2)}{x^2 + y^2} = x^2$$
> 
> Por otro lado, la función es no negativa:
> 
> $$0 \leq \frac{x^2y^2}{x^2 + y^2} \leq x^2$$
> 
> Tomando límites:
> 
> $$\lim_{(x,y) \to (0,0)} 0 = 0 \quad \text{y} \quad \lim_{(x,y) \to (0,0)} x^2 = 0$$
> 
> **Por el teorema del sandwich:**
> 
> $$\boxed{\lim_{(x,y) \to (0,0)} \frac{x^2y^2}{x^2 + y^2} = 0}$$
> 
> ---
> 
> **Ejemplo 8:** Otro ejemplo con acotación
> 
> $$\lim_{(x,y) \to (0,0)} x^2\sin\left(\frac{1}{xy}\right)$$
> 
> **Análisis:**
> 
> Sabemos que $|\sin(u)| \leq 1$ para todo $u$, entonces:
> 
> $$\left|x^2\sin\left(\frac{1}{xy}\right)\right| \leq |x^2| \cdot 1 = x^2$$
> 
> Por lo tanto:
> 
> $$-x^2 \leq x^2\sin\left(\frac{1}{xy}\right) \leq x^2$$
> 
> Como $\lim_{(x,y) \to (0,0)} (\pm x^2) = 0$:
> 
> $$\boxed{\lim_{(x,y) \to (0,0)} x^2\sin\left(\frac{1}{xy}\right) = 0}$$

### 📍 Método 5: Factorización y Simplificación

> [!tip]- ✂️ Simplificar Antes de Evaluar
> 
> **Estrategias:**
> 
> 1. Factorizar numerador y denominador
> 2. Multiplicar por el conjugado
> 3. Cancelar factores comunes
> 4. Usar identidades algebraicas o trigonométricas
> 
> ---
> 
> **Ejemplo 9:** Simplificación algebraica
> 
> $$\lim_{(x,y) \to (1,2)} \frac{x^2 - 2xy + y^2}{x - y}$$
> 
> **Solución:**
> 
> Factorizamos el numerador:
> 
> $$x^2 - 2xy + y^2 = (x - y)^2$$
> 
> Entonces:
> 
> $$\frac{(x-y)^2}{x-y} = x - y$$
> 
> **Ahora sustituimos:**
> 
> $$\lim_{(x,y) \to (1,2)} (x - y) = 1 - 2 = -1$$
> 
> **Respuesta:** $\boxed{-1}$
> 
> ---
> 
> **Ejemplo 10:** Multiplicar por el conjugado
> 
> $$\lim_{(x,y) \to (0,0)} \frac{\sqrt{x^2 + y^2 + 1} - 1}{x^2 + y^2}$$
> 
> **Solución:**
> 
> Multiplicamos por el conjugado:
> 
> $$\frac{\sqrt{x^2 + y^2 + 1} - 1}{x^2 + y^2} \cdot \frac{\sqrt{x^2 + y^2 + 1} + 1}{\sqrt{x^2 + y^2 + 1} + 1}$$
> 
> $$= \frac{(x^2 + y^2 + 1) - 1}{(x^2 + y^2)(\sqrt{x^2 + y^2 + 1} + 1)}$$
> 
> $$= \frac{x^2 + y^2}{(x^2 + y^2)(\sqrt{x^2 + y^2 + 1} + 1)}$$
> 
> $$= \frac{1}{\sqrt{x^2 + y^2 + 1} + 1}$$
> 
> **Ahora sustituimos:**
> 
> $$\lim_{(x,y) \to (0,0)} \frac{1}{\sqrt{0 + 0 + 1} + 1} = \frac{1}{1 + 1} = \frac{1}{2}$$
> 
> **Respuesta:** $\boxed{\frac{1}{2}}$$

---

## 🎨 Propiedades de los Límites

> [!note]- 📜 Leyes de los Límites
> 
> Si $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$ y $\lim_{(x,y) \to (x_0,y_0)} g(x,y) = M$, entonces:
> 
> ### 1. Suma y Resta
> 
> $$\lim_{(x,y) \to (x_0,y_0)} [f(x,y) \pm g(x,y)] = L \pm M$$
> 
> ### 2. Producto
> 
> $$\lim_{(x,y) \to (x_0,y_0)} [f(x,y) \cdot g(x,y)] = L \cdot M$$
> 
> ### 3. Producto por Constante
> 
> $$\lim_{(x,y) \to (x_0,y_0)} [c \cdot f(x,y)] = c \cdot L$$
> 
> ### 4. Cociente
> 
> $$\lim_{(x,y) \to (x_0,y_0)} \frac{f(x,y)}{g(x,y)} = \frac{L}{M} \quad \text{si } M \neq 0$$
> 
> ### 5. Potencia
> 
> $$\lim_{(x,y) \to (x_0,y_0)} [f(x,y)]^n = L^n$$
> 
> ### 6. Raíz
> 
> $$\lim_{(x,y) \to (x_0,y_0)} \sqrt[n]{f(x,y)} = \sqrt[n]{L} \quad \text{(si está definida)}$$
> 
> ### 7. Composición
> 
> Si $g$ es continua en $L$: $$\lim_{(x,y) \to (x_0,y_0)} g(f(x,y)) = g(L)$$
> 
> **Ejemplos:**
> 
> - $\lim e^{f(x,y)} = e^L$
> - $\lim \sin(f(x,y)) = \sin(L)$
> - $\lim \ln(f(x,y)) = \ln(L)$ (si $L > 0$)

---

## 📚 Ejemplos Detallados

> [!example]- 📝 Ejemplo 11: Límite con Indeterminación $\frac{0}{0}$
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^3 + y^3}{x^2 + y^2}$$
> 
> **Intento 1: Sustitución directa** $$\frac{0^3 + 0^3}{0^2 + 0^2} = \frac{0}{0} \quad \text{(indeterminado)}$$
> 
> **Intento 2: Coordenadas polares** $$x = r\cos\theta, \quad y = r\sin\theta$$
> 
> $$\frac{r^3\cos^3\theta + r^3\sin^3\theta}{r^2} = r(\cos^3\theta + \sin^3\theta)$$
> 
> Como $|\cos^3\theta + \sin^3\theta| \leq 2$:
> 
> $$|r(\cos^3\theta + \sin^3\theta)| \leq 2r \to 0 \text{ cuando } r \to 0$$
> 
> **Conclusión:** $$\boxed{\lim_{(x,y) \to (0,0)} \frac{x^3 + y^3}{x^2 + y^2} = 0}$$

> [!example]- 📝 Ejemplo 12: Límite que Depende del Camino
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^2y}{x^4 + y^2}$$
> 
> **Camino 1: Eje X** ($y = 0$) $$\lim_{x \to 0} \frac{x^2 \cdot 0}{x^4 + 0} = 0$$
> 
> **Camino 2: Eje Y** ($x = 0$) $$\lim_{y \to 0} \frac{0 \cdot y}{0 + y^2} = 0$$
> 
> **Camino 3: Parábola $y = x^2$** $$\lim_{x \to 0} \frac{x^2 \cdot x^2}{x^4 + (x^2)^2} = \lim_{x \to 0} \frac{x^4}{x^4 + x^4} = \frac{1}{2}$$
> 
> **Conclusión:** Por el eje X y Y obtenemos 0, pero por la parábola obtenemos $\frac{1}{2}$.
> 
> $$\boxed{\text{El límite NO existe}}$$

> [!example]- 📝 Ejemplo 13: Límite Trigonométrico
> 
> $$\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2}$$
> 
> **Solución:**
> 
> Hacemos la sustitución $u = x^2 + y^2$
> 
> Cuando $(x,y) \to (0,0)$, entonces $u \to 0$
> 
> Conocemos el límite fundamental: $$\lim_{u \to 0} \frac{\sin(u)}{u} = 1$$
> 
> Por lo tanto: $$\boxed{\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2} = 1}$$

> [!example]- 📝 Ejemplo 14: Límite Exponencial
> 
> $$\lim_{(x,y) \to (0,0)} \frac{e^{x+y} - 1}{x + y}$$
> 
> **Solución:**
> 
> Hacemos $u = x + y$
> 
> Cuando $(x,y) \to (0,0)$ por cualquier camino donde $x + y \to 0$, tenemos $u \to 0$
> 
> Usamos el límite fundamental: $$\lim_{u \to 0} \frac{e^u - 1}{u} = 1$$
> 
> **Respuesta:** $\boxed{1}$

> [!example]- 📝 Ejemplo 15: Límite con Valor Absoluto
> 
> $$\lim_{(x,y) \to (0,0)} \frac{|xy|}{\sqrt{x^2 + y^2}}$$
> 
> **Solución usando desigualdades:**
> 
> Sabemos que $|xy| \leq \frac{x^2 + y^2}{2}$ (desigualdad AM-GM)
> 
> Por lo tanto: $$\frac{|xy|}{\sqrt{x^2 + y^2}} \leq \frac{x^2 + y^2}{2\sqrt{x^2 + y^2}} = \frac{\sqrt{x^2 + y^2}}{2}$$
> 
> Como: $$0 \leq \frac{|xy|}{\sqrt{x^2 + y^2}} \leq \frac{\sqrt{x^2 + y^2}}{2}$$
> 
> Y $\lim_{(x,y) \to (0,0)} \frac{\sqrt{x^2 + y^2}}{2} = 0$
> 
> **Por el teorema del sandwich:** $$\boxed{\lim_{(x,y) \to (0,0)} \frac{|xy|}{\sqrt{x^2 + y^2}} = 0}$$

---

## 🔄 Límites Iterados vs Límite Doble

> [!warning]- ⚠️ Diferencia Importante
> 
> ### Límite Doble
> 
> $$\lim_{(x,y) \to (x_0,y_0)} f(x,y)$$
> 
> - Nos acercamos al punto desde **todas las direcciones simultáneamente**
> - El más restrictivo y el más fuerte
> 
> ### Límites Iterados
> 
> **Primera forma:** $$\lim_{x \to x_0} \left[\lim_{y \to y_0} f(x,y)\right]$$
> 
> - Primero fijamos $x$ y calculamos el límite en $y$
> - Luego calculamos el límite en $x$
> 
> **Segunda forma:** $$\lim_{y \to y_0} \left[\lim_{x \to x_0} f(x,y)\right]$$
> 
> - Primero fijamos $y$ y calculamos el límite en $x$
> - Luego calculamos el límite en $y$
> 
> ---
> 
> ### ⚡ Teorema Importante
> 
> **Si el límite doble existe:** $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$$
> 
> **Y los límites iterados existen, entonces:** $$\lim_{x \to x_0} \left[\lim_{y \to y_0} f(x,y)\right] = \lim_{y \to y_0} \left[\lim_{x \to x_0} f(x,y)\right] = L$$
> 
> **PERO:**
> 
> - Los límites iterados pueden existir **sin que exista el límite doble**
> - Los límites iterados pueden ser **diferentes entre sí**
> 
> ---


### Ejemplo: Límites Iterados Diferentes

> [!example]- 📝 Ejemplo 16: Límites Iterados Diferentes del Límite Doble
> 
> $$f(x,y) = \frac{xy}{x^2 + y^2}$$
> 
> **Límite iterado 1:** Primero $y \to 0$, luego $x \to 0$
> 
> $$\lim_{x \to 0} \left[\lim_{y \to 0} \frac{xy}{x^2 + y^2}\right]$$
> 
> Fijamos $x$ y calculamos: $$\lim_{y \to 0} \frac{xy}{x^2 + y^2} = \lim_{y \to 0} \frac{xy}{x^2 + y^2} = \frac{x \cdot 0}{x^2 + 0} = 0$$
> 
> Ahora: $$\lim_{x \to 0} 0 = 0$$
> 
> **Límite iterado 2:** Primero $x \to 0$, luego $y \to 0$
> 
> $$\lim_{y \to 0} \left[\lim_{x \to 0} \frac{xy}{x^2 + y^2}\right]$$
> 
> Fijamos $y$ y calculamos: $$\lim_{x \to 0} \frac{xy}{x^2 + y^2} = \frac{0 \cdot y}{0 + y^2} = 0$$
> 
> Ahora: $$\lim_{y \to 0} 0 = 0$$
> 
> **Límite doble:** Por camino $y = x$
> 
> $$\lim_{x \to 0} \frac{x \cdot x}{x^2 + x^2} = \lim_{x \to 0} \frac{x^2}{2x^2} = \frac{1}{2}$$
> 
> **Conclusión:**
> 
> - Ambos límites iterados existen y son iguales: $0$
> - Pero el límite doble **NO existe** (depende del camino)
> - Los límites iterados **NO garantizan** la existencia del límite doble

---

## 🌟 Límites en Tres Variables

> [!note]- 🎲 Extensión a $\mathbb{R}^3$
> 
> ### Definición
> 
> $$\lim_{(x,y,z) \to (x_0,y_0,z_0)} f(x,y,z) = L$$
> 
> si para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:
> 
> $$0 < \sqrt{(x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2} < \delta \implies |f(x,y,z) - L| < \varepsilon$$
> 
> ### Coordenadas Esféricas
> 
> Para límites en el origen: $$\begin{cases} x = \rho\sin\phi\cos\theta \ y = \rho\sin\phi\sin\theta \ z = \rho\cos\phi \ \rho = \sqrt{x^2 + y^2 + z^2} \end{cases}$$
> 
> Cuando $(x,y,z) \to (0,0,0)$: $\rho \to 0$

> [!example]- 📝 Ejemplo 17: Límite en Tres Variables
> 
> $$\lim_{(x,y,z) \to (0,0,0)} \frac{xyz}{x^2 + y^2 + z^2}$$
> 
> **Por el eje X** ($y = z = 0$): $$\lim_{x \to 0} \frac{x \cdot 0 \cdot 0}{x^2 + 0 + 0} = 0$$
> 
> **Por la recta $x = y = z$:** $$\lim_{x \to 0} \frac{x \cdot x \cdot x}{x^2 + x^2 + x^2} = \lim_{x \to 0} \frac{x^3}{3x^2} = \lim_{x \to 0} \frac{x}{3} = 0$$
> 
> **Usando coordenadas esféricas:** $$f = \frac{\rho^3\sin\phi\cos\theta \cdot \sin\phi\sin\theta \cdot \cos\phi}{\rho^2}$$
> 
> $$= \rho \sin^2\phi\cos\phi\cos\theta\sin\theta$$
> 
> Como $|\sin^2\phi\cos\phi\cos\theta\sin\theta| \leq 1$:
> 
> $$|f| \leq \rho \to 0$$
> 
> **Conclusión:** $$\boxed{\lim_{(x,y,z) \to (0,0,0)} \frac{xyz}{x^2 + y^2 + z^2} = 0}$$

> [!example]- 📝 Ejemplo 18: Límite en 3D que NO Existe
> 
> $$\lim_{(x,y,z) \to (0,0,0)} \frac{x^2 + y^2}{x^2 + y^2 + z^2}$$
> 
> **Por el eje Z** ($x = y = 0$): $$\lim_{z \to 0} \frac{0 + 0}{0 + 0 + z^2} = 0$$
> 
> **Por el plano $z = 0$** (cualquier camino con $z = 0$, $x$ o $y \neq 0$): $$\lim_{(x,y) \to (0,0)} \frac{x^2 + y^2}{x^2 + y^2 + 0} = 1$$
> 
> **Conclusión:** Los límites son diferentes ($0 \neq 1$), por lo tanto:
> 
> $$\boxed{\text{El límite NO existe}}$$

---

## 💡 Estrategias y Consejos Prácticos

> [!tip]- ⭐ Guía Paso a Paso para Calcular Límites
> 
> ### Paso 1: Intentar Sustitución Directa
> 
> - Si no hay indeterminación → **ese es el límite**
> - Si hay indeterminación → continuar
> 
> ### Paso 2: Buscar Límites que NO Existen
> 
> Probar caminos específicos:
> 
> - Ejes coordenados: $x = 0$, $y = 0$
> - Rectas: $y = x$, $y = -x$, $y = mx$
> - Parábolas: $y = x^2$, $x = y^2$
> 
> Si encuentras **dos caminos con límites diferentes** → **el límite NO existe**
> 
> ### Paso 3: Si parece que el límite existe
> 
> Intentar probarlo usando:
> 
> - **Coordenadas polares** (para origen)
> - **Teorema del sandwich** (acotar la función)
> - **Simplificación algebraica**
> 
> ### Paso 4: Verificación Final
> 
> - ¿La expresión depende del ángulo $\theta$ en polares?
> - ¿Todos los términos tienden a cero suficientemente rápido?
> - ¿Las cotas son correctas?

> [!tip]- 🎯 Errores Comunes a Evitar
> 
> ❌ **Error 1:** Confiar solo en los ejes coordenados
> 
> - Una función puede dar el mismo límite por los ejes pero diferente por otras trayectorias
> 
> ❌ **Error 2:** Asumir que límites iterados implican límite doble
> 
> - Los límites iterados pueden existir sin que exista el límite doble
> 
> ❌ **Error 3:** Simplificar incorrectamente antes de tomar límites
> 
> - Asegúrate de que las simplificaciones sean válidas cerca del punto
> 
> ❌ **Error 4:** Olvidar verificar el dominio
> 
> - La función debe estar definida cerca del punto (excepto posiblemente en el punto mismo)
> 
> ❌ **Error 5:** No considerar suficientes caminos
> 
> - Probar solo 2-3 caminos no prueba que el límite existe
> 
> ❌ **Error 6:** Confundir $\to$ con $=$
> 
> - $\lim_{(x,y) \to (0,0)} f(x,y)$ no requiere que $f(0,0)$ esté definida

> [!tip]- 🔍 Caminos Útiles para Probar
> 
> |Tipo de Camino|Ecuación|Cuándo Usar|
> |---|---|---|
> |**Eje X**|$y = 0$|Siempre primero|
> |**Eje Y**|$x = 0$|Siempre primero|
> |**Diagonal**|$y = x$|Cuando aparece $x^2 + y^2$ o $xy$|
> |**Diagonal negativa**|$y = -x$|Para funciones con signos|
> |**Recta general**|$y = mx$|Si los anteriores dan lo mismo|
> |**Parábola**|$y = x^2$|Cuando hay potencias distintas|
> |**Parábola inversa**|$x = y^2$|Alternativa a $y = x^2$|
> |**Cúbica**|$y = x^3$|Para exponentes altos|
> |**Curva parametrizada**|$x = t^n, y = t^m$|Casos complejos|

---

## 📊 Tabla Resumen: Métodos

> [!note]- 📋 Comparación de Métodos
> 
> |Método|Cuándo Usar|Ventajas|Limitaciones|
> |---|---|---|---|
> |**Sustitución Directa**|Función continua|Rápido y simple|No funciona con indeterminaciones|
> |**Caminos Específicos**|Probar que NO existe|Definitivo si encuentras diferencia|No prueba existencia|
> |**Coordenadas Polares**|Límites en origen|Sistemático, reduce variables|Solo para origen; requiere independencia de θ|
> |**Teorema Sandwich**|Función acotable|Riguroso, prueba existencia|Requiere encontrar cotas|
> |**Simplificación**|Indeterminaciones algebraicas|Puede eliminar la indeterminación|No siempre es posible|
> |**Límites Iterados**|Complementario|Fácil de calcular|NO garantiza límite doble|

---

## 📚 Ejemplos Adicionales Desafiantes

> [!example]- 📝 Ejemplo 19: Función Complicada
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^2 + y^2}{\sqrt{x^2 + y^2 + 1} - 1}$$
> 
> **Solución:**
> 
> Multiplicamos por el conjugado:
> 
> $$\frac{x^2 + y^2}{\sqrt{x^2 + y^2 + 1} - 1} \cdot \frac{\sqrt{x^2 + y^2 + 1} + 1}{\sqrt{x^2 + y^2 + 1} + 1}$$
> 
> $$= \frac{(x^2 + y^2)(\sqrt{x^2 + y^2 + 1} + 1)}{(x^2 + y^2 + 1) - 1}$$
> 
> $$= \frac{(x^2 + y^2)(\sqrt{x^2 + y^2 + 1} + 1)}{x^2 + y^2}$$
> 
> $$= \sqrt{x^2 + y^2 + 1} + 1$$
> 
> Ahora sustituimos:
> 
> $$\lim_{(x,y) \to (0,0)} (\sqrt{x^2 + y^2 + 1} + 1) = \sqrt{0 + 0 + 1} + 1 = 2$$
> 
> **Respuesta:** $\boxed{2}$

> [!example]- 📝 Ejemplo 20: Límite Logarítmico
> 
> $$\lim_{(x,y) \to (0,0)} \frac{\ln(1 + x^2 + y^2)}{x^2 + y^2}$$
> 
> **Solución:**
> 
> Hacemos $u = x^2 + y^2$
> 
> Cuando $(x,y) \to (0,0)$, entonces $u \to 0^+$
> 
> Usamos el límite fundamental: $$\lim_{u \to 0} \frac{\ln(1 + u)}{u} = 1$$
> 
> Por lo tanto: $$\boxed{\lim_{(x,y) \to (0,0)} \frac{\ln(1 + x^2 + y^2)}{x^2 + y^2} = 1}$$

> [!example]- 📝 Ejemplo 21: Límite con Sen y Cos
> 
> $$\lim_{(x,y) \to (0,0)} \frac{1 - \cos(x^2 + y^2)}{x^2 + y^2}$$
> 
> **Solución:**
> 
> Usamos la identidad: $1 - \cos(u) = 2\sin^2\left(\frac{u}{2}\right)$
> 
> $$\frac{1 - \cos(x^2 + y^2)}{x^2 + y^2} = \frac{2\sin^2\left(\frac{x^2 + y^2}{2}\right)}{x^2 + y^2}$$
> 
> Sea $u = \frac{x^2 + y^2}{2}$, entonces $x^2 + y^2 = 2u$:
> 
> $$= \frac{2\sin^2(u)}{2u} = \frac{\sin^2(u)}{u}$$
> 
> $$= \frac{\sin(u)}{u} \cdot \sin(u)$$
> 
> Cuando $u \to 0$: $$\lim_{u \to 0} \frac{\sin(u)}{u} = 1 \quad \text{y} \quad \lim_{u \to 0} \sin(u) = 0$$
> 
> Pero necesitamos ser más cuidadosos:
> 
> $$\frac{\sin^2(u)}{u} = \sin(u) \cdot \frac{\sin(u)}{u} \to 0 \cdot 1 = 0$$
> 
> **Respuesta:** $\boxed{0}$

> [!example]- 📝 Ejemplo 22: Límite Exponencial Complejo
> 
> $$\lim_{(x,y) \to (0,0)} \frac{e^{xy} - 1 - xy}{x^2y^2}$$
> 
> **Solución:**
> 
> Usamos la expansión de Taylor: $e^u = 1 + u + \frac{u^2}{2} + O(u^3)$
> 
> Con $u = xy$:
> 
> $$e^{xy} = 1 + xy + \frac{(xy)^2}{2} + O((xy)^3)$$
> 
> Entonces: $$e^{xy} - 1 - xy = \frac{(xy)^2}{2} + O((xy)^3)$$
> 
> Por lo tanto: $$\frac{e^{xy} - 1 - xy}{x^2y^2} = \frac{\frac{x^2y^2}{2} + O((xy)^3)}{x^2y^2} = \frac{1}{2} + O(xy)$$
> 
> Cuando $(x,y) \to (0,0)$:
> 
> $$\boxed{\lim_{(x,y) \to (0,0)} \frac{e^{xy} - 1 - xy}{x^2y^2} = \frac{1}{2}}$$

> [!example]- 📝 Ejemplo 23: Límite que Requiere Análisis Cuidadoso
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^3 - y^3}{x^2 + y^2}$$
> 
> **Intento por caminos:**
> 
> **Por $y = 0$:** $$\lim_{x \to 0} \frac{x^3}{x^2} = \lim_{x \to 0} x = 0$$
> 
> **Por $x = 0$:** $$\lim_{y \to 0} \frac{-y^3}{y^2} = \lim_{y \to 0} (-y) = 0$$
> 
> **Por $y = x$:** $$\lim_{x \to 0} \frac{x^3 - x^3}{x^2 + x^2} = \lim_{x \to 0} \frac{0}{2x^2} = 0$$
> 
> **Usando coordenadas polares:**
> 
> $$f = \frac{r^3\cos^3\theta - r^3\sin^3\theta}{r^2} = r(\cos^3\theta - \sin^3\theta)$$
> 
> Como $|\cos^3\theta - \sin^3\theta| \leq 2$:
> 
> $$|f| \leq 2r \to 0$$
> 
> **Conclusión:** $$\boxed{\lim_{(x,y) \to (0,0)} \frac{x^3 - y^3}{x^2 + y^2} = 0}$$

> [!example]- 📝 Ejemplo 24: Límite con Raíces
> 
> $$\lim_{(x,y) \to (0,0)} \frac{xy}{\sqrt{x^2 + y^2}}$$
> 
> **Solución:**
> 
> Usando la desigualdad $|xy| \leq \frac{x^2 + y^2}{2}$:
> 
> $$\left|\frac{xy}{\sqrt{x^2 + y^2}}\right| \leq \frac{x^2 + y^2}{2\sqrt{x^2 + y^2}} = \frac{\sqrt{x^2 + y^2}}{2}$$
> 
> Por el teorema del sandwich:
> 
> $$-\frac{\sqrt{x^2 + y^2}}{2} \leq \frac{xy}{\sqrt{x^2 + y^2}} \leq \frac{\sqrt{x^2 + y^2}}{2}$$
> 
> Como ambos lados tienden a 0:
> 
> $$\boxed{\lim_{(x,y) \to (0,0)} \frac{xy}{\sqrt{x^2 + y^2}} = 0}$$

> [!example]- 📝 Ejemplo 25: Un Límite Tramposo
> 
> $$\lim_{(x,y) \to (0,0)} \frac{x^2y}{x^4 + 3y^2}$$
> 
> **Por $y = 0$:** $$\lim_{x \to 0} \frac{0}{x^4} = 0$$
> 
> **Por $x = 0$:** $$\lim_{y \to 0} \frac{0}{3y^2} = 0$$
> 
> **Por $y = x^2$:** $$\lim_{x \to 0} \frac{x^2 \cdot x^2}{x^4 + 3x^4} = \lim_{x \to 0} \frac{x^4}{4x^4} = \frac{1}{4}$$
> 
> **Conclusión:** El límite por la parábola $y = x^2$ es diferente.
> 
> $$\boxed{\text{El límite NO existe}}$$

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular por sustitución directa:**
> 
> a) $\lim_{(x,y) \to (1,2)} (3x^2 + 2y^2 - xy)$
> 
> b) $\lim_{(x,y) \to (0,0)} (x^2 + y^2 + 5)$
> 
> c) $\lim_{(x,y) \to (\pi, \pi/2)} \sin(x)\cos(y)$
> 
> d) $\lim_{(x,y) \to (1,1)} e^{x+y}$
> 
> ---
> 
> **2. Usar caminos para mostrar que NO existe:**
> 
> a) $\lim_{(x,y) \to (0,0)} \frac{x - y}{x + y}$
> 
> b) $\lim_{(x,y) \to (0,0)} \frac{x^2 - y^2}{x^2 + y^2}$
> 
> c) $\lim_{(x,y) \to (0,0)} \frac{xy^2}{x^2 + y^4}$
> 
> d) $\lim_{(x,y) \to (0,0)} \frac{x^3 + y^3}{x - y}$
> 
> ---
> 
> **3. Usar coordenadas polares:**
> 
> a) $\lim_{(x,y) \to (0,0)} \frac{x^2 + y^2}{\sqrt{x^2 + y^2}}$
> 
> b) $\lim_{(x,y) \to (0,0)} (x^2 + y^2)\ln(x^2 + y^2)$
> 
> c) $\lim_{(x,y) \to (0,0)} \frac{x^4 + y^4}{x^2 + y^2}$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Límites con indeterminaciones:**
> 
> a) $\lim_{(x,y) \to (0,0)} \frac{x^2y}{x^4 + y^2}$
> 
> b) $\lim_{(x,y) \to (0,0)} \frac{\sin(xy)}{xy}$
> 
> c) $\lim_{(x,y) \to (0,0)} \frac{e^{x^2+y^2} - 1}{x^2 + y^2}$
> 
> d) $\lim_{(x,y) \to (0,0)} \frac{xy^2}{x^2 + y^2}$
> 
> ---
> 
> **5. Usar teorema del sandwich:**
> 
> a) $\lim_{(x,y) \to (0,0)} x^2y^2\sin\left(\frac{1}{xy}\right)$
> 
> b) $\lim_{(x,y) \to (0,0)} \frac{x^3y^3}{(x^2 + y^2)^2}$
> 
> c) $\lim_{(x,y) \to (0,0)} \sqrt{x^2 + y^2} \cdot \sin\left(\frac{1}{x}\right)\cos\left(\frac{1}{y}\right)$
> 
> ---
> 
> **6. Límites iterados:**
> 
> Para cada función, calcular ambos límites iterados y determinar si el límite doble existe:
> 
> a) $f(x,y) = \frac{x^2 - y^2}{x^2 + y^2}$
> 
> b) $f(x,y) = \frac{x^2y}{x^4 + y^2}$
> 
> c) $f(x,y) = \frac{xy}{x + y}$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Límites desafiantes:**
> 
> a) $\lim_{(x,y) \to (0,0)} \frac{x^3 + y^3}{x^2 + xy + y^2}$
> 
> b) $\lim_{(x,y) \to (0,0)} (x^2 + y^2)^{xy}$
> 
> c) $\lim_{(x,y) \to (0,0)} \frac{\tan(x^2 + y^2)}{x^2 + y^2}$
> 
> d) $\lim_{(x,y) \to (0,0)} \frac{\sin(x^2 + y^2) - (x^2 + y^2)}{(x^2 + y^2)^2}$
> 
> ---
> 
> **8. Límites en tres variables:**
> 
> a) $\lim_{(x,y,z) \to (0,0,0)} \frac{x^2 + y^2}{x^2 + y^2 + z^2}$
> 
> b) $\lim_{(x,y,z) \to (0,0,0)} \frac{xyz^2}{x^2 + y^2 + z^2}$
> 
> c) $\lim_{(x,y,z) \to (0,0,0)} \frac{x^2 + y^2 + z^2}{\sqrt{x^2 + y^2 + z^2 + 1} - 1}$
> 
> ---
> 
> **9. Problemas conceptuales:**
> 
> a) Dar un ejemplo de una función donde ambos límites iterados existan pero sean diferentes.
> 
> b) Dar un ejemplo donde ambos límites iterados sean iguales pero el límite doble no exista.
> 
> c) Construir una función $f(x,y)$ tal que $\lim_{(x,y) \to (0,0)} f(x,y)$ no existe, pero $f$ es continua en cualquier recta que pasa por el origen.

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $\lim_{(x,y) \to (1,2)} (3x^2 + 2y^2 - xy)$
> 
> $$= 3(1)^2 + 2(2)^2 - (1)(2) = 3 + 8 - 2 = 9$$
> 
> **Respuesta:** $\boxed{9}$
> 
> ---
> 
> **1b)** $\lim_{(x,y) \to (0,0)} (x^2 + y^2 + 5)$
> 
> $$= 0 + 0 + 5 = 5$$
> 
> **Respuesta:** $\boxed{5}$
> 
> ---
> 
> **1c)** $\lim_{(x,y) \to (\pi, \pi/2)} \sin(x)\cos(y)$
> 
> $$= \sin(\pi)\cos(\pi/2) = 0 \cdot 0 = 0$$
> 
> **Respuesta:** $\boxed{0}$
> 
> ---
> 
> **1d)** $\lim_{(x,y) \to (1,1)} e^{x+y}$
> 
> $$= e^{1+1} = e^2$$
> 
> **Respuesta:** $\boxed{e^2}$
> 
> ---
> 
> **2a)** $\lim_{(x,y) \to (0,0)} \frac{x - y}{x + y}$
> 
> **Por $y = 0$:** $\lim_{x \to 0} \frac{x}{x} = 1$
> 
> **Por $x = 0$:** $\lim_{y \to 0} \frac{-y}{y} = -1$
> 
> Como $1 \neq -1$: **El límite NO existe** ✓
> 
> ---
> 
> **2b)** $\lim_{(x,y) \to (0,0)} \frac{x^2 - y^2}{x^2 + y^2}$
> 
> **Por $y = 0$:** $\lim_{x \to 0} \frac{x^2}{x^2} = 1$
> 
> **Por $x = 0$:** $\lim_{y \to 0} \frac{-y^2}{y^2} = -1$
> 
> **El límite NO existe** ✓
> 
> ---
> 
> **3a)** $\lim_{(x,y) \to (0,0)} \frac{x^2 + y^2}{\sqrt{x^2 + y^2}}$
> 
> En polares: $r = \sqrt{x^2 + y^2}$
> 
> $$\frac{r^2}{r} = r \to 0$$
> 
> **Respuesta:** $\boxed{0}$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $\lim_{(x,y) \to (0,0)} \frac{x^2y}{x^4 + y^2}$
> **Por $y = 0$:** $\lim_{x \to 0} \frac{0}{x^4} = 0$
> 
> **Por $y = x^2$:** $\lim_{x \to 0} \frac{x^2 \cdot x^2}{x^4 + x^4} = \frac{x^4}{2x^4} = \frac{1}{2}$
> 
> Como $0 \neq \frac{1}{2}$: **El límite NO existe** ✓
> 
> ---
> 
> **4b)** $\lim_{(x,y) \to (0,0)} \frac{\sin(xy)}{xy}$
> 
> Sea $u = xy$. Cuando $(x,y) \to (0,0)$ por caminos donde $xy \to 0$:
> 
> $$\lim_{u \to 0} \frac{\sin(u)}{u} = 1$$
> 
> **Respuesta:** $\boxed{1}$
> 
> ---
> 
> **4c)** $\lim_{(x,y) \to (0,0)} \frac{e^{x^2+y^2} - 1}{x^2 + y^2}$
> 
> Sea $u = x^2 + y^2$:
> 
> $$\lim_{u \to 0^+} \frac{e^u - 1}{u} = 1$$
> 
> **Respuesta:** $\boxed{1}$
> 
> ---
> 
> **4d)** $\lim_{(x,y) \to (0,0)} \frac{xy^2}{x^2 + y^2}$
> 
> Usamos $|xy^2| \leq |x| \cdot y^2 \leq \sqrt{x^2 + y^2} \cdot y^2$
> 
> Como $y^2 \leq x^2 + y^2$:
> 
> $$\left|\frac{xy^2}{x^2 + y^2}\right| \leq \left|\frac{x(x^2 + y^2)}{x^2 + y^2}\right| = |x| \to 0$$
> 
> **Respuesta:** $\boxed{0}$
> 
> ---
> 
> **5a)** $\lim_{(x,y) \to (0,0)} x^2y^2\sin\left(\frac{1}{xy}\right)$
> 
> Como $|\sin(u)| \leq 1$:
> 
> $$\left|x^2y^2\sin\left(\frac{1}{xy}\right)\right| \leq x^2y^2$$
> 
> Y $x^2y^2 \leq (x^2 + y^2)^2$, que tiende a 0.
> 
> Más simple: $|x^2y^2| \to 0$
> 
> **Respuesta:** $\boxed{0}$
> 
> ---
> 
> **6a)** $f(x,y) = \frac{x^2 - y^2}{x^2 + y^2}$
> 
> **Límite iterado 1:** $$\lim_{x \to 0} \left[\lim_{y \to 0} \frac{x^2 - y^2}{x^2 + y^2}\right] = \lim_{x \to 0} \frac{x^2}{x^2} = 1$$
> 
> **Límite iterado 2:** $$\lim_{y \to 0} \left[\lim_{x \to 0} \frac{x^2 - y^2}{x^2 + y^2}\right] = \lim_{y \to 0} \frac{-y^2}{y^2} = -1$$
> 
> Los límites iterados son **diferentes**, y ya sabemos que el límite doble **NO existe**.

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **7a)** $\lim_{(x,y) \to (0,0)} \frac{x^3 + y^3}{x^2 + xy + y^2}$
> 
> Factorizamos: $x^3 + y^3 = (x + y)(x^2 - xy + y^2)$
> 
> Pero $x^2 + xy + y^2$ no es lo mismo que $x^2 - xy + y^2$...
> 
> **Por $y = x$:** $$\lim_{x \to 0} \frac{x^3 + x^3}{x^2 + x^2 + x^2} = \lim_{x \to 0} \frac{2x^3}{3x^2} = \lim_{x \to 0} \frac{2x}{3} = 0$$
> 
> **Usando polares:** $$\frac{r^3(\cos^3\theta + \sin^3\theta)}{r^2(\cos^2\theta + \cos\theta\sin\theta + \sin^2\theta)} = \frac{r(\cos^3\theta + \sin^3\theta)}{1 + \cos\theta\sin\theta}$$
> 
> Como el numerador es $O(r)$ y el denominador está acotado lejos de 0:
> 
> **Respuesta:** $\boxed{0}$
> 
> ---
> 
> **7c)** $\lim_{(x,y) \to (0,0)} \frac{\tan(x^2 + y^2)}{x^2 + y^2}$
> 
> Sea $u = x^2 + y^2$:
> 
> $$\lim_{u \to 0^+} \frac{\tan(u)}{u} = \lim_{u \to 0^+} \frac{\sin(u)}{u\cos(u)} = \frac{1}{1} = 1$$
> 
> **Respuesta:** $\boxed{1}$
> 
> ---
> 
> **8a)** $\lim_{(x,y,z) \to (0,0,0)} \frac{x^2 + y^2}{x^2 + y^2 + z^2}$
> 
> **Por el eje Z** ($x = y = 0$): $$\lim_{z \to 0} \frac{0}{z^2} = 0$$
> 
> **Por el plano $z = 0$** (cualquier punto con $z = 0$, pero $(x,y) \neq (0,0)$): $$\frac{x^2 + y^2}{x^2 + y^2 + 0} = 1$$
> 
> **El límite NO existe** (depende del camino) ✓
> 
> ---
> 
> **8b)** $\lim_{(x,y,z) \to (0,0,0)} \frac{xyz^2}{x^2 + y^2 + z^2}$
> 
> En coordenadas esféricas:
> 
> - $x = \rho\sin\phi\cos\theta$
> - $y = \rho\sin\phi\sin\theta$
> - $z = \rho\cos\phi$
> 
> $$f = \frac{\rho^4\sin\phi\cos\theta \cdot \sin\phi\sin\theta \cdot \cos^2\phi}{\rho^2}$$
> 
> $$= \rho^2 \sin^2\phi\cos^2\phi\cos\theta\sin\theta$$
> 
> Como todos los términos trigonométricos están acotados: $$|f| \leq C\rho^2 \to 0$$
> 
> **Respuesta:** $\boxed{0}$

---

## 🔗 Conexión con Continuidad

> [!info]- 🌉 Relación Límite-Continuidad
> 
> ### Definición de Continuidad
> 
> Una función $f(x,y)$ es **continua** en $(x_0, y_0)$ si:
> 
> 1. $f(x_0, y_0)$ está definida
> 2. $\lim_{(x,y) \to (x_0,y_0)} f(x,y)$ existe
> 3. $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = f(x_0, y_0)$
> 
> **En otras palabras:** Una función es continua si podemos calcular el límite por sustitución directa.
> 
> ---
> 
> ### Tipos de Discontinuidad
> 
> **1. Discontinuidad Removible:**
> 
> - El límite existe pero $f(x_0,y_0) \neq L$ (o no está definida)
> - Se puede "arreglar" redefiniendo $f(x_0,y_0) = L$
> 
> **Ejemplo:** $$f(x,y) = \begin{cases} \frac{x^2 + y^2}{x + y} & \text{si } x + y \neq 0 \ 5 & \text{si } x + y = 0 \end{cases}$$
> 
> En puntos donde $x + y = 0$ (excepto origen), hay discontinuidad removible.
> 
> ---
> 
> **2. Discontinuidad Esencial:**
> 
> - El límite no existe
> - No se puede "arreglar"
> 
> **Ejemplo:** $$f(x,y) = \frac{xy}{x^2 + y^2}$$
> 
> En $(0,0)$ el límite no existe (depende del camino).
> 
> ---
> 
> ### Funciones Continuas Comunes
> 
> **Siempre continuas en su dominio:**
> 
> - Polinomios
> - Funciones racionales (donde el denominador $\neq 0$)
> - $\sin(x,y)$, $\cos(x,y)$
> - $e^{f(x,y)}$ si $f$ es continua
> - $\ln(f(x,y))$ si $f$ es continua y positiva
> - Composiciones de funciones continuas

---

## 🎯 Teoremas Importantes

> [!note]- 📐 Teoremas Útiles sobre Límites
> 
> ### Teorema 1: Unicidad del Límite
> 
> Si $\lim_{(x,y) \to (x_0,y_0)} f(x,y)$ existe, entonces es **único**.
> 
> ---
> 
> ### Teorema 2: Límite de Composición
> 
> Si $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$ y $g$ es continua en $L$, entonces:
> 
> $$\lim_{(x,y) \to (x_0,y_0)} g(f(x,y)) = g(L)$$
> 
> **Aplicación práctica:**
> 
> - $\lim e^{f(x,y)} = e^{\lim f(x,y)}$
> - $\lim \sin(f(x,y)) = \sin(\lim f(x,y))$
> 
> ---
> 
> ### Teorema 3: Teorema del Sandwich
> 
> Si $g(x,y) \leq f(x,y) \leq h(x,y)$ cerca de $(x_0,y_0)$ y
> 
> $$\lim_{(x,y) \to (x_0,y_0)} g(x,y) = \lim_{(x,y) \to (x_0,y_0)} h(x,y) = L$$
> 
> entonces:
> 
> $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$$
> 
> ---
> 
> ### Teorema 4: Cambio a Coordenadas Polares
> 
> Si al convertir a polares obtenemos: $$\lim_{r \to 0} f(r\cos\theta, r\sin\theta) = L$$
> 
> **independiente de** $\theta$, entonces:
> 
> $$\lim_{(x,y) \to (0,0)} f(x,y) = L$$
> 
> ---
> 
> ### Teorema 5: Límites Laterales (No Aplica Directamente)
> 
> A diferencia de una variable, en varias variables **no** podemos hablar de límites "laterales" de forma simple porque hay infinitas direcciones.
> 
> Sin embargo, podemos hablar de:
> 
> - Límite por una trayectoria específica
> - Límite direccional (tema de derivadas direccionales)

---

## 📊 Visualización Geométrica

> [!note]- 🎨 Interpretación Gráfica del Límite
> 
> ### Para $z = f(x,y)$
> 
> El límite $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$ significa:
> 
> ```
>         z
>         |
>       L +---[···]---  ← La superficie se acerca a este nivel
>         |    \|/
>         |     o (x₀,y₀,L)
>         |    /|\
>         |   [···]
>         +-------------- y
>        /|
>       / |
>      x  |
> ```
> 
> **Interpretación:**
> 
> - Cuando nos acercamos a $(x_0,y_0)$ desde **cualquier dirección** en el plano $xy$
> - La altura de la superficie $z = f(x,y)$ se acerca a $L$
> 
> ---
> 
> ### Si el límite NO existe
> 
> ```
>         z
>         |
>      L₂ +---    ---    ← Por algunos caminos
>         |   \  /
>         |    \/
>         |    /\ 
>      L₁ +---    ---    ← Por otros caminos
>         +-------------- y
>        /|
>       / |
>      x  |
> ```
> 
> La superficie tiene diferentes "alturas límite" dependiendo de la dirección de aproximación.

---

## 🔬 Casos Especiales

> [!warning]- ⚠️ Situaciones Especiales a Considerar
> 
> ### Caso 1: Funciones Definidas por Partes
> 
> **Ejemplo:** $$f(x,y) = \begin{cases} \frac{xy}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> Para verificar continuidad en el origen, necesitamos: $$\lim_{(x,y) \to (0,0)} \frac{xy}{x^2 + y^2} = 0$$
> 
> Pero ya vimos que este límite **NO existe**, por lo que $f$ **NO es continua** en el origen.
> 
> ---
> 
> ### Caso 2: Límites Infinitos
> 
> $$\lim_{(x,y) \to (0,0)} \frac{1}{x^2 + y^2} = +\infty$$
> 
> **Interpretación:** La función crece sin límite cuando nos acercamos al origen.
> 
> **Notación formal:** Para todo $M > 0$, existe $\delta > 0$ tal que si $0 < \sqrt{x^2 + y^2} < \delta$, entonces $f(x,y) > M$.
> 
> ---
> 
> ### Caso 3: Límites en el Infinito
> 
> $$\lim_{(x,y) \to \infty} f(x,y) = L$$
> 
> Significa: cuando $\sqrt{x^2 + y^2} \to \infty$ (nos alejamos del origen en cualquier dirección), $f(x,y) \to L$.
> 
> **Ejemplo:** $$\lim_{(x,y) \to \infty} \frac{x^2 + y^2}{x^2 + y^2 + 1} = 1$$
> 
> ---
> 
> ### Caso 4: Límites en Fronteras del Dominio
> 
> Para $f(x,y) = \sqrt{1 - x^2 - y^2}$ (dominio: disco $x^2 + y^2 \leq 1$)
> 
> En puntos de la frontera $(x_0, y_0)$ con $x_0^2 + y_0^2 = 1$:
> 
> $$\lim_{(x,y) \to (x_0,y_0)} f(x,y) = 0$$
> 
> (solo considerando puntos dentro del dominio)

---

## 💡 Estrategias Avanzadas

> [!tip]- 🎓 Técnicas Adicionales
> 
> ### Técnica 1: Parametrización de Curvas
> 
> Para probar que un límite no existe, usar curvas parametrizadas:
> 
> **Ejemplo:** $f(x,y) = \frac{x^2y}{x^4 + y^2}$
> 
> Usar $x = t$, $y = t^2$: $$\lim_{t \to 0} \frac{t^2 \cdot t^2}{t^4 + t^4} = \lim_{t \to 0} \frac{t^4}{2t^4} = \frac{1}{2}$$
> 
> Usar $x = t$, $y = t$: $$\lim_{t \to 0} \frac{t^2 \cdot t}{t^4 + t^2} = \lim_{t \to 0} \frac{t^3}{t^2(t^2 + 1)} = \lim_{t \to 0} \frac{t}{t^2 + 1} = 0$$
> 
> Como $\frac{1}{2} \neq 0$, el límite **NO existe**.
> 
> ---
> 
> ### Técnica 2: Desigualdades Útiles
> 
> **AM-GM:** $$|xy| \leq \frac{x^2 + y^2}{2}$$
> 
> **Cauchy-Schwarz:** $$|ax + by| \leq \sqrt{a^2 + b^2}\sqrt{x^2 + y^2}$$
> 
> **Acotaciones básicas:**
> 
> - $|x| \leq \sqrt{x^2 + y^2}$
> - $|y| \leq \sqrt{x^2 + y^2}$
> - $x^2 \leq x^2 + y^2$
> - $y^2 \leq x^2 + y^2$
> 
> ---
> 
> ### Técnica 3: Series de Taylor
> 
> Para límites complicados cerca del origen, usar expansiones:
> 
> - $e^u = 1 + u + \frac{u^2}{2} + O(u^3)$
> - $\sin(u) = u - \frac{u^3}{6} + O(u^5)$
> - $\cos(u) = 1 - \frac{u^2}{2} + O(u^4)$
> - $\ln(1+u) = u - \frac{u^2}{2} + O(u^3)$
> 
> **Ejemplo:** $$\lim_{(x,y) \to (0,0)} \frac{e^{xy} - 1 - xy}{x^2y^2} = \lim_{(x,y) \to (0,0)} \frac{\frac{(xy)^2}{2} + O((xy)^3)}{x^2y^2} = \frac{1}{2}$$

---

## 📈 Resumen Visual

> [!note]- 🗺️ Mapa Conceptual: Estrategias para Límites
> 
> ```
> ¿Límite de f(x,y) cuando (x,y) → (x₀,y₀)?
>                    |
>         ┌──────────┴──────────┐
>         ↓                     ↓
>   ¿Sustitución         ¿Hay indicios de que
>    directa?              NO existe?
>         |                     |
>    ┌────┴────┐           ┌────┴────┐
>    ↓         ↓           ↓         ↓
>   Sí        No      Probar    Parece que
>    |         |      caminos    existe
>    ↓         ↓          |         |
> [LISTO]  Indeter-      ↓         ↓
>          minación  ¿Diferen-  Usar:
>              |      tes?      • Polares
>              ↓        |       • Sandwich
>         ┌────┴────┐  ↓       • Cotas
>         ↓         ↓  Sí
>    Simplifi-  Polar/ |
>     car      Sandwich ↓
>         |         | [NO EXISTE]
>         ↓         ↓
>      [RESULTADO]
> ```

---

## 🎯 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> **Sobre la existencia de límites:**
> 
> 1. ✅ El límite debe ser **el mismo** desde **todas** las direcciones
> 2. ✅ Para probar que NO existe: encontrar **dos caminos** con límites diferentes
> 3. ✅ Para probar que SÍ existe: usar métodos rigurosos (polares, sandwich, cotas)
> 4. ✅ Los límites iterados **NO garantizan** la existencia del límite doble
> 
> **Métodos principales:**
> 
> 1. 🔵 **Sustitución directa** → funciones continuas
> 2. 🔴 **Caminos específicos** → probar que NO existe
> 3. 🟢 **Coordenadas polares** → probar que SÍ existe (en el origen)
> 4. 🟡 **Teorema sandwich** → acotar y concluir
> 5. 🟣 **Simplificación** → eliminar indeterminaciones
> 
> **Errores a evitar:**
> 
> - ❌ Confiar solo en ejes coordenados
> - ❌ Asumir que límites iterados implican límite doble
> - ❌ No verificar suficientes caminos
> - ❌ Simplificar sin justificación
> - ❌ Olvidar que hay infinitas direcciones

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones
> 
> **Este tema es prerequisito para:**
> 
> - [[07 - Continuidad]] - Los límites definen la continuidad
> - [[08 - Derivadas Parciales]] - Las derivadas son límites especiales
> - [[09 - Diferenciabilidad]] - Requiere existencia de ciertos límites
> - [[10 - Regla de la Cadena]] - Se basa en continuidad y límites
> 
> **Conceptos relacionados:**
> 
> - **Topología** - Vecindades, puntos de acumulación
> - **Continuidad** - Relación directa con límites
> - **Diferenciabilidad** - Generaliza el concepto de límite
> - **Integrales múltiples** - Límites de sumas de Riemann
> 
> **Siguiente tema recomendado:** [[07 - Continuidad de Funciones de Varias Variables]]

---

## 📝 Ejercicios Adicionales de Desafío

> [!example]- 🏆 Problemas de Competencia
> 
> **10. Límites extremadamente desafiantes:**
> 
> a) $\lim_{(x,y) \to (0,0)} \left(\frac{x^2 + y^2}{x^2 + y^2 + (x-y)^2}\right)^{1/(x^2+y^2)}$
> 
> b) $\lim_{(x,y) \to (0,0)} \frac{\sin(x^2y) + \sin(xy^2)}{x^3 + y^3}$
> 
> c) $\lim_{(x,y) \to (0,0)} \frac{x^4 - y^4}{x^2 + y^2} \cdot \sin\left(\frac{1}{x^2+y^2}\right)$
> 
> d) $\lim_{(x,y) \to (0,0)} (x^2 + y^2)^{x^2y^2}$
> 
> ---
> 
> **11. Problemas conceptuales avanzados:**
> 
> a) Demostrar que si $\lim_{(x,y) \to (x_0,y_0)} f(x,y) = L$ y $\lim_{(x,y) \to (x_0,y_0)} g(x,y) = M$, entonces: $$\lim_{(x,y) \to (x_0,y_0)} [f(x,y) + g(x,y)] = L + M$$
> 
> b) Construir una función $f(x,y)$ tal que:
> 
> - $\lim_{(x,y) \to (0,0)} f(x,y)$ no existe
> - Pero para toda recta $y = mx$, el límite existe
> 
> c) Demostrar usando la definición $\varepsilon$-$\delta$ que: $$\lim_{(x,y) \to (0,0)} (3x^2 + 2y^2) = 0$$
> 
> ---
> 
> **12. Aplicaciones:**
> 
> a) La temperatura en una placa está dada por $T(x,y) = \frac{100xy}{x^2 + y^2 + 1}$. ¿Qué ocurre con la temperatura cuando nos acercamos al origen?
> 
> b) El potencial eléctrico es $V(x,y) = \frac{k}{\ sqrt{x^2 + y^2}}$ (donde $k$ es constante). Analizar el límite cuando $(x,y) \to (0,0)$ y su interpretación física.
> 
> c) La densidad de probabilidad conjunta es proporcional a $f(x,y) = e^{-(x^2+y^2)}$. Verificar que $\lim_{(x,y) \to \infty} f(x,y) = 0$.

---

## ✨ Comentarios Finales

> [!note]- 🎓 Reflexiones sobre Límites en Varias Variables
> 
> Los límites en varias variables son **fundamentalmente más complejos** que en una variable debido a:
> 
> 1. **Infinitas direcciones de aproximación** - No basta verificar dos caminos
> 2. **Complejidad geométrica** - Las regiones en $\mathbb{R}^2$ o $\mathbb{R}^3$ son más difíciles de visualizar
> 3. **Mayor riqueza de comportamientos** - Más formas en que un límite puede no existir
> 
> **Pero también son más interesantes:**
> 
> - Conectan álgebra con geometría
> - Desarrollan intuición espacial
> - Preparan para conceptos más avanzados (diferenciabilidad, optimización)
> 
> **Práctica recomendada:**
> 
> - Resolver muchos problemas variados
> - Visualizar siempre que sea posible
> - Entender el "por qué" detrás de cada método
> - No memorizar, sino comprender la estructura

---

**Tags:** #calculo-multivariable #limites #funciones-varias-variables #continuidad #coordenadas-polares #teorema-sandwich #convergencia #topologia
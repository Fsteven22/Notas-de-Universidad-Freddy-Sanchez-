---
dg-publish: true
tags: [MATG1045, unidad6, teoremas-especiales-integrales-definidas, simetria-par-impar, periodicidad, valor-medio-integrales, tvmi, fourier, rms]
---

# 🪞 Teoremas Especiales para Integrales Definidas

## 🎯 Introducción

> [!info] 💡 Qué aportan estos tres teoremas
>
> Esta nota reúne las tres herramientas que **ahorran cálculo** antes de integrar: el teorema de **simetría** (pares e impares), el teorema de **periodicidad** y el **teorema del valor medio para integrales**. Las dos primeras reducen o anulan la integral; la tercera garantiza que existe un punto donde la función toma su promedio.
>
> **Por qué importa:** en examen el tiempo se acaba, y estos teoremas convierten un ejercicio de cinco minutos en una línea. Además son la base del análisis de Fourier y del cálculo de potencia en señales periódicas.
>
> **Ejemplo:** $\int_{-2}^{2} x^3\,dx$ no requiere antiderivada: $x^3$ es impar sobre un intervalo simétrico, así que la respuesta es $0$.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Simetría par e impar en una integral definida
>
> Una función $f$ es **par** si $f(-x) = f(x)$ para todo $x$, y **impar** si $f(-x) = -f(x)$. Continuas sobre $[-a,a]$, cumplen:
>
> $$\text{par: } \int_{-a}^{a} f(x)\,dx = 2\int_{0}^{a} f(x)\,dx \qquad \text{impar: } \int_{-a}^{a} f(x)\,dx = 0$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Teoremas_Especiales_para_Integrales_Definidas_01.svg]]
>
> **Se lee así:** una caja inicial, "Simetría en $[-a,a]$", que se bifurca en dos ramas. La rama superior trata a la **función par** ($f(-x) = f(x)$) y encadena la igualdad de la integral con el doble de la integral de $0$ a $a$ con la lectura geométrica "áreas iguales se duplican". La rama inferior trata a la **impar** ($f(-x) = -f(x)$), conduce a la integral igual a cero y explica que la simetría respecto al origen hace que el área positiva y la negativa se cancelen.
>
> **Por qué importa:** el teorema entrega el resultado **sin calcular**, y el recuadro geométrico explica por qué. Te evita integrar media vuelta de la función a mano cuando el intervalo es simétrico.
>
> **Ejemplo:** con $\int_{-2}^{2} x^2\,dx$, la paridad de $x^2$ da $2\int_0^2 x^2\,dx = \frac{16}{3}$ sin escribir la antiderivada completa.

> [!note] 📋 Definición — Valor medio de una integral
>
> Si $f$ es continua en $[a,b]$ con $a \neq b$, su **valor medio** (o promedio) es
>
> $$\frac{1}{b-a}\int_a^b f(x)\,dx$$
>
> y el teorema del valor medio garantiza que existe al menos un $c \in (a,b)$ tal que
>
> $$\int_a^b f(x)\,dx = f(c)\,(b-a)$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Teoremas_Especiales_para_Integrales_Definidas_03.svg]]
>
> **Se lee así:** una cadena que arranca en el enunciado del teorema, baja a la hipótesis ($f$ continua en $[a,b]$ con $a \neq b$), sigue con la existencia de un $c$ en $(a,b)$ que cumple $f(c) = \frac{1}{b-a}\int_a^b f$, y desde ahí se abre en dos ramas: una describe el **rectángulo** con base $b-a$, que se bifurca en su altura $f(c)$ y en la igualdad de áreas, y la otra cierra en la lectura de $f(c)$ como el **valor promedio** de $f$ en el intervalo.
>
> **Por qué importa:** el esquema separa la parte lógica (hipótesis y existencia de $c$) de la parte geométrica (el rectángulo), y eso explica **por qué** el teorema exige continuidad y cómo leer el resultado como un área.
>
> **Ejemplo:** con $f(x) = x^2$ en $[0,3]$, el rectángulo del esquema dice que $\int_0^3 x^2\,dx = 9$ es el área de un rectángulo de base 3 y altura 3, y el punto donde se alcanza esa altura es $c = \sqrt{3}$.

---

## 🪞 Simetría: funciones pares e impares

> [!tip] 🏆 Teorema para funciones pares
>
> Si $f$ es **par** ($f(-x) = f(x)$) y continua en $[-a,a]$, entonces
>
> $$\int_{-a}^{a} f(x)\,dx = 2\int_{0}^{a} f(x)\,dx$$
>
> **Interpretación geométrica:** la gráfica es simétrica respecto al **eje $y$**, así que el área de $-a$ a $0$ es igual al área de $0$ a $a$ y se duplica.
>
> **Por qué importa:** reduces el intervalo a la mitad positiva, donde casi siempre la función es más cómoda de integrar.

> [!tip] 🏆 Teorema para funciones impares
>
> Si $f$ es **impar** ($f(-x) = -f(x)$) y continua en $[-a,a]$, entonces
>
> $$\int_{-a}^{a} f(x)\,dx = 0$$
>
> **Interpretación geométrica:** la gráfica tiene simetría **puntual respecto al origen**, así que el área positiva y la negativa se cancelan exactamente.
>
> **Por qué importa:** es la integral que se resuelve escribiendo cero. El único trabajo real es **verificar** la imparidad, no integrar.

> [!warning] 🔬 Demostración del teorema para funciones pares
>
> **Paso 1:** partir la integral: $\int_{-a}^{a} f(x)\,dx = \int_{-a}^{0} f(x)\,dx + \int_{0}^{a} f(x)\,dx$.
>
> **Paso 2:** en la primera, sustituir $u = -x$ (entonces $dx = -du$): cuando $x = -a$, $u = a$; cuando $x = 0$, $u = 0$.
>
> $$\int_{-a}^{0} f(x)\,dx = \int_{a}^{0} f(-u)(-du) = \int_{0}^{a} f(-u)\,du$$
>
> **Paso 3:** como $f$ es par, $f(-u) = f(u)$, así que $\int_{-a}^{0} f(x)\,dx = \int_{0}^{a} f(u)\,du = \int_{0}^{a} f(x)\,dx$.
>
> **Paso 4:** sustituir de vuelta: $\int_{-a}^{a} f(x)\,dx = \int_{0}^{a} f(x)\,dx + \int_{0}^{a} f(x)\,dx = 2\int_{0}^{a} f(x)\,dx$ ✓
>
> **Por qué importa:** la demostración es un solo cambio de variable; si te la piden en examen, el paso 2 (con el cambio de signo de los límites) es donde se puntúa.

> [!warning] 🔬 Demostración del teorema para funciones impares
>
> Se repiten los mismos pasos, pero en el paso 3 se usa que $f$ es impar, o sea $f(-u) = -f(u)$:
>
> $$\int_{-a}^{0} f(x)\,dx = \int_{0}^{a} (-f(u))\,du = -\int_{0}^{a} f(x)\,dx$$
>
> Por lo tanto $\int_{-a}^{a} f(x)\,dx = -\int_{0}^{a} f(x)\,dx + \int_{0}^{a} f(x)\,dx = 0$ ✓
>
> **Por qué importa:** las dos demostraciones son la misma; cambia un solo signo. Recordar eso te permite reconstruirlas sin memorizar.

> [!tip] 📈 Los cuatro ejemplos de simetría
>
> **Ejemplo 1 · Par:** $\int_{-2}^{2} x^2\,dx$. Se verifica $f(-x) = (-x)^2 = x^2 = f(x)$ ✓, y $2\int_0^2 x^2\,dx = 2\left[\frac{x^3}{3}\right]_0^2 = 2\cdot\frac{8}{3} = \frac{16}{3}$. Comprobación directa: $\left[\frac{x^3}{3}\right]_{-2}^{2} = \frac{8}{3} - \left(-\frac{8}{3}\right) = \frac{16}{3}$ ✓
>
> **Ejemplo 2 · Impar:** $\int_{-3}^{3} x^3\,dx$. $f(-x) = -x^3 = -f(x)$ ✓, así que la integral vale $0$. Comprobación: $\left[\frac{x^4}{4}\right]_{-3}^{3} = \frac{81}{4} - \frac{81}{4} = 0$ ✓
>
> **Ejemplo 3 · Trigonométrica:** $\int_{-\pi}^{\pi} \operatorname{sen}(x)\cos(x)\,dx$. Como $f(-x) = \operatorname{sen}(-x)\cos(-x) = (-\operatorname{sen} x)(\cos x) = -f(x)$, es impar y la integral vale $0$.
>
> **Ejemplo 4 · Mixta:** $\int_{-2}^{2} (x^2 + x^3)\,dx$. Se separa por linealidad: $\underbrace{x^2}_{\text{par}} + \underbrace{x^3}_{\text{impar}}$, así que $\int_{-2}^{2} x^2\,dx + \int_{-2}^{2} x^3\,dx = \frac{16}{3} + 0 = \frac{16}{3}$.
>
> **Por qué importa:** el ejemplo 4 es el patrón más útil: **toda función se parte en parte par más parte impar**, y en un intervalo simétrico solo sobrevive la par.

---

## 🔄 Periodicidad

> [!note] 📋 Función periódica y su teorema
>
> Una función $f$ es **periódica** con período $T > 0$ si $f(x + T) = f(x)$ para todo $x$ de su dominio. Si $f$ es continua y periódica con período $T$, entonces para cualquier real $a$:
>
> $$\int_a^{a+T} f(x)\,dx = \int_0^T f(x)\,dx$$
>
> **Corolario:** $\int_0^{nT} f(x)\,dx = n\int_0^T f(x)\,dx$ para cualquier entero positivo $n$.
>
> **Por qué importa:** la integral de una periódica **no depende de dónde empiece** el intervalo, solo de su longitud. Si mides $n$ periodos completos, multiplicas la de un período por $n$.

> [!warning] 🔬 Demostración del teorema de periodicidad
>
> **Paso 1:** partir el intervalo en tres tramos:
>
> $$\int_a^{a+T} f(x)\,dx = \int_a^{0} f(x)\,dx + \int_0^{T} f(x)\,dx + \int_T^{a+T} f(x)\,dx$$
>
> **Paso 2:** en el último tramo hacer $u = x - T$ (con lo que $x = u + T$ y los límites van de $0$ a $a$):
>
> $$\int_T^{a+T} f(x)\,dx = \int_0^{a} f(u + T)\,du$$
>
> **Paso 3:** aplicar la periodicidad $f(u+T) = f(u)$:
>
> $$\int_0^{a} f(u + T)\,du = \int_0^{a} f(u)\,du$$
>
> **Paso 4:** el primer y el último tramo se cancelan, $\int_a^{0} f + \int_0^{a} f = 0$, y queda $\int_a^{a+T} f(x)\,dx = \int_0^T f(x)\,dx$ ✓
>
> **Por qué importa:** no se usa ningún cálculo, solo el desplazamiento del argumento. El caso $a < 0$ es análogo con el mismo cambio de variable.

> [!tip] 📈 Los tres ejemplos de periodicidad
>
> **Ejemplo 1 · Seno ($T = 2\pi$):** la integral base es $\int_0^{2\pi} \operatorname{sen}(x)\,dx = [-\cos x]_0^{2\pi} = -1 + 1 = 0$. Entonces:
> - $\int_{\pi}^{3\pi} \operatorname{sen}(x)\,dx = \int_0^{2\pi} \operatorname{sen}(x)\,dx = 0$ (mismo largo, distinto inicio).
> - $\int_{-\pi}^{\pi} \operatorname{sen}(x)\,dx = 0$ **por imparidad**, ya que el intervalo es simétrico.
> - $\int_0^{4\pi} \operatorname{sen}(x)\,dx = 2\int_0^{2\pi} \operatorname{sen}(x)\,dx = 2 \cdot 0 = 0$ (dos periodos).
>
> **Ejemplo 2 · Coseno ($T = 2\pi$):** $\int_0^{2\pi} \cos(x)\,dx = [\operatorname{sen} x]_0^{2\pi} = 0 - 0 = 0$, y por lo tanto $\int_{5\pi}^{7\pi} \cos(x)\,dx = \int_0^{2\pi} \cos(x)\,dx = 0$.
>
> **Ejemplo 3 · Función cuadrada ($T = 2$):** con $f(x) = 1$ en $[0,1)$ y $f(x) = -1$ en $[1,2)$,
>
> $$\int_0^2 f(x)\,dx = \int_0^1 1\,dx + \int_1^2 (-1)\,dx = 1 - 1 = 0$$
>
> y por periodicidad $\int_{10}^{12} f(x)\,dx = \int_0^2 f(x)\,dx = 0$.
>
> **Por qué importa:** fíjate en que el ejemplo 1 distingue los dos caminos: $\int_{\pi}^{3\pi}$ se resuelve con periodicidad y $\int_{-\pi}^{\pi}$ con imparidad. Elegir el teorema equivocado a veces da el mismo resultado, pero no siempre.

---

## 🎨 Combinaciones de simetría y periodicidad

> [!tip] 🎯 Los casos que se repiten en examen
>
> **Par y periódica:** $\cos(x)$ cumple las dos. En un intervalo simétrico, $\int_{-\pi}^{\pi} \cos(x)\,dx = 2\int_0^{\pi} \cos(x)\,dx = 2[\operatorname{sen} x]_0^{\pi} = 0$.
>
> **Impar y periódica:** $\operatorname{sen}(x)$ cumple las dos, y en $[-\pi,\pi]$ manda la imparidad: $\int_{-\pi}^{\pi} \operatorname{sen}(x)\,dx = 0$.
>
> **Por qué importa:** cuando las dos propiedades apuntan al mismo resultado, se aplica la que sea más corta; cuando apuntan a cosas distintas (como en el seno con intervalo simétrico), **manda la imparidad**.

> [!info] 🧮 Funciones con múltiples propiedades: $f(x) = x\operatorname{sen}(x^2)$
>
> **En $[-a,a]$:** $f(-x) = (-x)\operatorname{sen}((-x)^2) = -x\operatorname{sen}(x^2) = -f(x)$, o sea que es **impar**, y por lo tanto $\int_{-a}^{a} x\operatorname{sen}(x^2)\,dx = 0$.
>
> **Por qué importa:** no basta con mirar que $\operatorname{sen}(x^2)$ es par: el producto de $x$ (impar) por una par es impar. Verificar la composición y el producto **siempre**, nunca suponerlo.

> [!info] 🖼️ Ejemplos pares, impares y compuestos
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Teoremas_Especiales_para_Integrales_Definidas_02.svg]]
>
> **Se lee así:** una caja de entrada, "Ejemplos pares e impares", con tres ramas. Dos son casos directos: $\cos(x)$, par y periódica, con su integral sobre $[-\pi,\pi]$ resuelta como $2\int_0^{\pi}$ igual a $0$; y $\operatorname{sen}(x)$, impar y periódica, con esa misma integral igual a $0$ por imparidad. La tercera rama baja a la función compuesta $f(x) = x\operatorname{sen}(x^2)$, encadena su verificación de imparidad con el cero resultante y cierra en una caja final de consejo: chequear la paridad antes de calcular.
>
> **Por qué importa:** una función puede tener **varias propiedades a la vez** y cada una acorta el cálculo. El diagrama también te obliga a verificar $f(-x)$ en vez de suponer la simetría.
>
> **Ejemplo:** con $f(x) = x\operatorname{sen}(x^2)$ verificas que es impar y concluyes de inmediato que $\int_{-a}^{a} x\operatorname{sen}(x^2)\,dx = 0$.

---

## 🧮 Teorema del valor medio para integrales

> [!tip] 🏆 Enunciado y condiciones
>
> Si $f$ es continua en el intervalo cerrado $[a,b]$ con $a \neq b$, existe al menos un $c \in (a,b)$ tal que
>
> $$\int_a^b f(x)\,dx = f(c)\,(b-a) \qquad \text{equivalentemente} \qquad f(c) = \frac{1}{b-a}\int_a^b f(x)\,dx$$
>
> **Condiciones necesarias:**
>
> - $f$ debe ser **continua** en $[a,b]$.
> - $a \neq b$ (el intervalo tiene longitud positiva).
> - $c$ pertenece al interior $(a,b)$.
>
> **Por qué importa:** la continuidad no es decorativa: sin ella puede no existir ningún $c$ que alcance el promedio. Es la hipótesis que más se olvida al citar el teorema.

> [!info] 🎨 Significado geométrico
>
> El teorema garantiza la existencia de un **rectángulo** con base $b - a$, altura $f(c)$ y área igual al área bajo la curva $y = f(x)$ desde $a$ hasta $b$. El número $\frac{1}{b-a}\int_a^b f(x)\,dx$ se llama **valor medio** (o promedio) de $f$ en $[a,b]$, y el teorema dice que ese valor se alcanza **de verdad** en algún punto del intervalo.
>
> **Por qué importa:** leer el resultado como un área (rectángulo equivalente) y no solo como un cociente es lo que permite trasladarlo a física: promedio de temperatura, de voltaje o de velocidad.

> [!warning] 🔬 Esquema de la demostración
>
> **Paso 1:** como $f$ es continua en $[a,b]$, alcanza su máximo $M$ y su mínimo $m$ en el intervalo.
>
> **Paso 2:** por la propiedad de comparación de integrales: $m(b-a) \leq \int_a^b f(x)\,dx \leq M(b-a)$.
>
> **Paso 3:** dividiendo por $(b - a) > 0$: $m \leq \frac{1}{b-a}\int_a^b f(x)\,dx \leq M$.
>
> **Paso 4:** por el **teorema del valor intermedio**, existe $c \in [a,b]$ con $f(c) = \frac{1}{b-a}\int_a^b f(x)\,dx$ ✓
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Teoremas_Especiales_para_Integrales_Definidas_04.svg]]
>
> **Se lee así:** una cadena vertical de cinco bloques: la caja inicial anuncia la demostración del teorema y de ella cuelgan los cuatro pasos numerados, encadenados por flechas rectas —continuidad y extremos, comparación de integrales, división por $(b-a)$ e invocación del teorema del valor intermedio— hasta un recuadro final verde que marca "TVMI probado".
>
> **Por qué importa:** la demostración se apoya en dos herramientas que ya dominas, la comparación de integrales y el valor intermedio. Te sirve para justificar el teorema por escrito y para no saltarte la hipótesis de continuidad, que es donde más se falla.
>
> **Ejemplo:** con $f(x) = x^2$ en $[0,3]$ la cadena te lleva a calcular $\int_0^3 x^2\,dx = 9$, dividir entre 3 para obtener el promedio $3$ y buscar $c$ con $c^2 = 3$, o sea $c = \sqrt{3}$.

> [!tip] 📈 Los tres ejemplos de valor medio
>
> **Ejemplo 1 · Cuadrática:** valor medio de $f(x) = x^2$ en $[0,3]$.
> 1. $\int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = 9$.
> 2. Valor medio $= \frac{9}{3-0} = 3$.
> 3. $c^2 = 3 \Rightarrow c = \sqrt{3} \approx 1{,}732$.
>
> Verificación: $c = \sqrt{3} \in (0,3)$ ✓ y $f(\sqrt{3}) = 3$ ✓
>
> **Ejemplo 2 · Trigonométrica:** valor medio de $f(x) = \operatorname{sen}(x)$ en $[0,\pi]$.
> 1. $\int_0^{\pi} \operatorname{sen}(x)\,dx = [-\cos x]_0^{\pi} = 1 + 1 = 2$.
> 2. Valor medio $= \frac{2}{\pi} \approx 0{,}637$.
> 3. $\operatorname{sen}(c) = \frac{2}{\pi} \Rightarrow c = \arcsin\left(\frac{2}{\pi}\right) \approx 0{,}69$ radianes.
>
> Verificación: $c \approx 0{,}69 \in (0,\pi)$ ✓
>
> **Ejemplo 3 · Lineal:** valor medio de $f(x) = 2x + 1$ en $[1,4]$.
> 1. $\int_1^4 (2x+1)\,dx = \left[x^2 + x\right]_1^4 = (16 + 4) - (1 + 1) = 18$.
> 2. Valor medio $= \frac{18}{4-1} = 6$.
> 3. $2c + 1 = 6 \Rightarrow c = 2{,}5$.
>
> **Observación:** $c = 2{,}5$ es exactamente el **punto medio** de $[1,4]$ ✓
>
> **Por qué importa:** el ejemplo 3 no es casualidad: en las lineales el promedio siempre se alcanza en el centro del intervalo, lo que da una comprobación rápida en examen.

> [!info] ⚡ Casos especiales del valor medio
>
> **Lineales:** para $f(x) = mx + b$ el punto $c$ siempre es el **punto medio** del intervalo: $c = \frac{a+b}{2}$.
>
> **Pares e impares:** una par en $[-a,a]$ tiene valor medio $\frac{1}{a}\int_0^a f(x)\,dx$ (se aprovecha la simetría); para $f(x) = x^2$ en $[-1,1]$ el valor medio es $\frac{1}{3}$, que se alcanza en $c = \pm\frac{1}{\sqrt{3}}$. Una impar en $[-a,a]$ tiene valor medio $0$, alcanzado en cualquier punto donde $f(c) = 0$.
>
> **Periódicas:** para $f$ con período $T$, el valor medio en cualquier intervalo de longitud $T$ es el mismo: $\frac{1}{T}\int_a^{a+T} f(x)\,dx = \frac{1}{T}\int_0^T f(x)\,dx$.
>
> **Por qué importa:** los tres casos permiten responder de memoria una pregunta de valor medio sin volver a integrar.

---

## 🔗 Valor medio y el teorema del valor medio para derivadas

> [!info] 🖼️ La misma idea en velocidad y posición
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Teoremas_Especiales_para_Integrales_Definidas_05.svg]]
>
> **Se lee así:** un árbol que arranca en la velocidad promedio de un viaje $s(t)$ y se bifurca en dos ramas. Una calcula directamente $v_{\text{prom}} = \frac{s(b) - s(a)}{b-a}$; la otra invoca el TVMI para afirmar que existe $c$ con $v(c) = v_{\text{prom}}$, y baja en cadena hasta la caja que distingue "calcular el promedio" de "garantizar que se alcanza", cerrando con la imagen del velocímetro que marca ese valor.
>
> **Por qué importa:** el dibujo separa dos cosas que se confunden todo el tiempo: el promedio se obtiene **dividiendo**, y el teorema solo añade que ese número **aparece** en algún instante concreto.
>
> **Ejemplo:** en un viaje de $a$ a $b$, el esquema te lleva a calcular $v_{\text{prom}} = \frac{s(b)-s(a)}{b-a}$ y a afirmar que hubo un momento en que el velocímetro marcó exactamente ese valor.

> [!info] 🔄 Conexión profunda con el teorema fundamental
>
> Aplicando el segundo teorema fundamental a $F(x) = \int_a^x f(t)\,dt$:
>
> $$F(b) - F(a) = \int_a^b f(x)\,dx$$
>
> Por el TVM **para derivadas** existe $c \in (a,b)$ con $F'(c) = \frac{F(b)-F(a)}{b-a}$, y como $F'(c) = f(c)$:
>
> $$f(c) = \frac{\int_a^b f(x)\,dx}{b-a} \quad \checkmark$$
>
> **Por qué importa:** el TVMI para integrales **no es un teorema nuevo**: es el TVM para derivadas aplicado a la primitiva. Entenderlo así te deja reconstruirlo sin memorizar.

> [!tip] 🎓 Mnemotecnia VMAP
>
> **V**erificar continuidad de la función · **M**edir la integral definida · **A**plicar la fórmula del valor medio · **P**oner igualación y resolver para $c$.
>
> **Ejemplo rápido:** con $f(x) = x^2$ en $[0,2]$:
> 1. **V:** ¿es continua en $[0,2]$? ✓
> 2. **M:** $\int_0^2 x^2\,dx = \frac{8}{3}$.
> 3. **A:** valor medio $= \frac{8/3}{2} = \frac{4}{3}$.
> 4. **P:** $c^2 = \frac{4}{3} \Rightarrow c = \frac{2}{\sqrt{3}}$.
>
> **Por qué importa:** la V es la que se salta la gente, y es la única que hace que el teorema aplique.

---

## 🛠️ Estrategias de aplicación

> [!tip] 🎓 Mnemotecnia SIPEM para elegir teorema
>
> **S**imetría: ¿es par, impar o ninguna? · **I**ntervalo: ¿es simétrico respecto al origen? · **P**eriodicidad: ¿tiene período conocido? · **E**strategia: ¿qué teorema aplicar? · **M**odificación: ¿se puede simplificar aún más la integral?
>
> **Por qué importa:** SIPEM se aplica **antes** de integrar. El orden importa: primero miras la función, después el intervalo, y solo entonces decides.

> [!info] ✅ Lista de verificación
>
> 1. **Identificar el tipo de función:** verificar $f(-x)$ contra $f(x)$ y buscar patrones periódicos.
> 2. **Analizar el intervalo:** ¿es simétrico respecto al origen? ¿abarca períodos completos?
> 3. **Aplicar el teorema correspondiente:** pares duplican la integral de $0$ a $a$; impares dan cero; periódicas desplazan el intervalo.
> 4. **Verificar el resultado:** comprobar signos y magnitud contra un caso simple.
>
> **Por qué importa:** el paso 2 es el que se olvida: la simetría de la función **no sirve de nada** si el intervalo no es simétrico.

---

## 🌐 Aplicaciones prácticas

> [!tip] 🌊 Series de Fourier
>
> En el análisis de Fourier, la simetría decide qué términos sobreviven:
>
> **Funciones pares** (solo cosenos): $a_n = \dfrac{2}{L}\displaystyle\int_0^L f(x)\cos\left(\frac{n\pi x}{L}\right)dx$.
>
> **Funciones impares** (solo senos): $b_n = \dfrac{2}{L}\displaystyle\int_0^L f(x)\operatorname{sen}\left(\frac{n\pi x}{L}\right)dx$.
>
> **Por qué importa:** la mitad de los coeficientes se anulan por simetría antes de integrar. Es la razón por la que en electricidad se descompone una señal en senos y cosenos según su paridad.

> [!info] ⚡ Ingeniería eléctrica: potencia y valor RMS
>
> Para una señal periódica $v(t)$ con período $T$, la potencia promedio es $P = \frac{1}{T}\int_0^T [v(t)]^2\,dt$, y la periodicidad permite calcularla sobre **cualquier** intervalo de longitud $T$. El **valor cuadrático medio** (RMS) de una función es $\text{RMS} = \sqrt{\dfrac{1}{b-a}\displaystyle\int_a^b [f(t)]^2\,dt}$, y el teorema garantiza que existe un $c$ donde $[f(c)]^2$ alcanza ese promedio.
>
> **Por qué importa:** el 120 V de tu casa es un valor **RMS**, no un valor instantáneo: es el promedio integral del cuadrado de la tensión, y su equivalente continuo disipa la misma potencia.

> [!note] 🌡️ Temperatura y ondas
>
> Si $T(t)$ es la temperatura durante un día, $T_{\text{prom}} = \frac{1}{24}\int_0^{24} T(t)\,dt$ y existe un momento $c$ en que $T(c) = T_{\text{prom}}$. Para una onda $f(t) = A\operatorname{sen}(\omega t + \phi)$, la energía por período es $E = \int_0^{2\pi/\omega} [f(t)]^2\,dt$, calculable en cualquier período completo por la periodicidad.
>
> **Por qué importa:** el teorema convierte un promedio que no puedes medir en todo instante (porque existe) en algo que sí puedes razonar.

> [!warning] 🚗 Velocidad promedio vs. velocidad instantánea
>
> **Velocidad promedio:** $v_{\text{prom}} = \dfrac{\text{desplazamiento}}{\text{tiempo}} = \dfrac{s(b) - s(a)}{b-a}$.
>
> **Teorema del valor medio para integrales:** existe $c$ tal que $v(c) = v_{\text{prom}}$.
>
> **Diferencia:** el promedio se calcula dividiendo, pero el teorema garantiza que **ese valor se alcanza** en algún instante del trayecto.
>
> **Por qué importa:** es la respuesta clásica a "¿alguna vez tuve exactamente la velocidad promedio?": la respuesta es sí, y el teorema es la justificación.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco fallos de simetría y periodicidad
>
> 1. **Asumir la paridad sin verificar:** siempre comprobar algebraicamente que $f(-x) = f(x)$ o $f(-x) = -f(x)$.
> 2. **Aplicar simetría en intervalos no simétricos:** los teoremas valen en $[-a,a]$, no en $[0,a]$.
> 3. **Confundir el período:** el de $\operatorname{sen}(x)$ y $\cos(x)$ es $2\pi$, no $\pi$. Usa siempre el período **mínimo**.
> 4. **Ignorar las discontinuidades:** en funciones por tramos hay que verificar simetría y periodicidad en todo el dominio.
> 5. **Suponer la composición:** $f(g(x))$ **no** hereda automáticamente las propiedades de $f$ y de $g$.
>
> **Por qué importa:** los cinco son errores de **verificación**, no de cálculo; por eso la calculadora no los detecta. Se previenen con el paso 1 de la lista de verificación.

> [!info] ⚠️ Situaciones que requieren cuidado especial
>
> - **Casi periódicas:** $f(x) = \operatorname{sen}(x) + \operatorname{sen}(\sqrt{2}\,x)$ **no** es periódica, porque la razón de sus períodos no es racional.
> - **Simetría local vs. global:** una función puede ser par en un intervalo sin serlo en todo su dominio.
> - **Periodicidad que no lo es:** $f(x) = x\operatorname{sen}(x)$ no es periódica aunque $\operatorname{sen}(x)$ sí lo sea: el factor $x$ rompe la repetición.
>
> **Por qué importa:** son las trampas que separan "aplicar la regla" de "entender la regla"; en examen suelen salir como opción falsa.

> [!warning] 🚨 Los cinco fallos del valor medio
>
> 1. **Olvidar la continuidad:** el teorema **no** aplica a funciones discontinuas.
> 2. **Confundirlo con el promedio de los extremos:** no es $\frac{f(a)+f(b)}{2}$, es $\frac{1}{b-a}\int_a^b f(x)\,dx$.
> 3. **Asumir unicidad de $c$:** pueden existir varios valores de $c$ que cumplan la igualdad.
> 4. **Intervalos degenerados:** si $a = b$ el teorema no aplica.
> 5. **Confundirlo con el TVM para derivadas:** son teoremas distintos con conclusiones distintas.
>
> **Por qué importa:** el error 2 es el más común: en lineales coinciden, y por eso la sorpresa llega cuando la función deja de serlo.

> [!info] ✅ Cómo verificar un resultado
>
> - Comprobar que $f$ sea continua en $[a,b]$.
> - Verificar que $c \in (a,b)$, es decir, en el interior.
> - Comprobar la ecuación: $f(c) \stackrel{?}{=} \frac{1}{b-a}\int_a^b f(x)\,dx$.
> - Revisar la lectura geométrica: el rectángulo debe tener la misma área que la región bajo la curva.
>
> **Por qué importa:** con estas cuatro comprobaciones el ejercicio se cierra sin depender del corrector: si las cuatro pasan, la respuesta es correcta.

---

## 🌟 Extensiones avanzadas

> [!tip] 🔬 Simetría generalizada y cuasi-periodicidad
>
> **Simetría respecto de un punto:** si $f(c+x) = f(c-x)$, entonces $\int_{c-a}^{c+a} f(x)\,dx = 2\int_c^{c+a} f(x)\,dx$. Es el teorema par trasladado al eje $x = c$.
>
> **Cuasi-periodicidad:** si $f(x+T) = k\,f(x)$ con $k \neq 1$, entonces $\int_0^{nT} f(x)\,dx = \dfrac{1 - k^n}{1 - k}\int_0^T f(x)\,dx$, por suma de progresión geométrica.
>
> **Por qué importa:** las dos generalizaciones muestran que la idea de fondo es la misma: **desplazar el argumento solo multiplica la integral por un factor**.

> [!info] 🌐 Extensión a dos variables y con función peso
>
> **Simetría en 2D:** si $f(x,y) = f(-x,y)$ (par en $x$), entonces $\iint_R f(x,y)\,dA = 2\iint_{R^+} f(x,y)\,dA$, donde $R^+$ es la parte de $R$ con $x \geq 0$.
>
> **Valor medio con función peso:** si $f$ y $g$ son continuas en $[a,b]$ y $g(x) \geq 0$, existe $c \in (a,b)$ tal que $\int_a^b f(x)g(x)\,dx = f(c)\int_a^b g(x)\,dx$.
>
> **Por qué importa:** la versión con peso es el teorema que usarás en probabilidad para el valor esperado de una variable continua; la versión en 2D es la que reaparece en Cálculo Vectorial.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{-1}^{1} \left(x^4 - 2x^2 + x^5\right)dx$ aprovechando la simetría.
>
> > [!success]- ✅ Solución
> >
> > **Paridad por términos:** $x^4$ es par, $-2x^2$ es par y $x^5$ es impar; el intervalo $[-1,1]$ es simétrico.
> >
> > **Descarte:** la integral de la parte impar vale $0$, así que solo sobrevive $\int_{-1}^{1} (x^4 - 2x^2)\,dx = 2\int_0^1 (x^4 - 2x^2)\,dx$.
> >
> > **Cálculo:** $2\left[\frac{x^5}{5} - \frac{2x^3}{3}\right]_0^1 = 2\left(\frac{1}{5} - \frac{2}{3}\right) = 2\left(\frac{3 - 10}{15}\right) = -\frac{14}{15}$.
> >
> > **Respuesta:** $-\dfrac{14}{15}$.
> >
> > **Control de signo:** el integrando vale $-2$ en $x = 1$ y $1$ en $x = 0$, así que un resultado negativo es razonable ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{-\pi}^{\pi} x\cos(x)\,dx$ sin calcular la antiderivada.
>
> > [!success]- ✅ Solución
> >
> > **Paridad:** $f(-x) = (-x)\cos(-x) = -x\cos(x) = -f(x)$, o sea que es **impar**.
> >
> > **Intervalo:** $[-\pi,\pi]$ es simétrico respecto al origen.
> >
> > **Teorema:** la integral de una impar sobre un intervalo simétrico vale $0$.
> >
> > **Respuesta:** $0$.
> >
> > **Cuidado:** $\cos(x)$ es par y $x$ es impar; el producto de una par por una impar **es impar**. Si hubieras supuesto que el producto es par, habrías integrado una hora para un resultado que es cero ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{0}^{4\pi} \cos^2(x)\,dx$ usando la periodicidad.
>
> > [!success]- ✅ Solución
> >
> > **Período:** $\cos^2(x) = \frac{1 + \cos(2x)}{2}$ tiene período $T = \pi$ (el de $\cos(2x)$).
> >
> > **Cantidad de periodos:** $4\pi = 4 \cdot \pi$, o sea cuatro periodos completos.
> >
> > **Integral en un período:** $\int_0^{\pi} \cos^2 x\,dx = \int_0^{\pi} \frac{1 + \cos 2x}{2}\,dx = \left[\frac{x}{2} + \frac{\operatorname{sen} 2x}{4}\right]_0^{\pi} = \frac{\pi}{2}$.
> >
> > **Corolario:** $4 \cdot \frac{\pi}{2} = 2\pi$.
> >
> > **Respuesta:** $2\pi$.
> >
> > **Control geométrico:** el promedio de $\cos^2$ sobre un período es $\frac{1}{2}$, así que en longitud $4\pi$ da $4\pi \cdot \frac{1}{2} = 2\pi$ ✓

> [!example] 📋 Planteamiento
>
> Encuentra el valor medio de $f(x) = \sqrt{x}$ en $[0,4]$ y el punto $c$ donde se alcanza.
>
> > [!success]- ✅ Solución
> >
> > **Continuidad:** $\sqrt{x}$ es continua en $[0,4]$ ✓ (el teorema aplica).
> >
> > **Integral:** $\int_0^4 \sqrt{x}\,dx = \left[\frac{2}{3}x^{3/2}\right]_0^4 = \frac{2}{3}\cdot 8 = \frac{16}{3}$.
> >
> > **Valor medio:** $\frac{1}{4-0}\cdot\frac{16}{3} = \frac{4}{3}$.
> >
> > **Punto $c$:** $\sqrt{c} = \frac{4}{3} \Rightarrow c = \frac{16}{9} \approx 1{,}78$.
> >
> > **Respuesta:** valor medio $\dfrac{4}{3}$ en $c = \dfrac{16}{9} \in (0,4)$ ✓

> [!example] 📋 Planteamiento
>
> Encuentra el valor medio de $f(x) = x^3$ en $[0,2]$ y verifica el teorema.
>
> > [!success]- ✅ Solución
> >
> > **Integral:** $\int_0^2 x^3\,dx = \left[\frac{x^4}{4}\right]_0^2 = 4$.
> >
> > **Valor medio:** $\frac{4}{2-0} = 2$.
> >
> > **Punto $c$:** $c^3 = 2 \Rightarrow c = \sqrt[3]{2} \approx 1{,}26$.
> >
> > **Respuesta:** valor medio $2$ en $c = \sqrt[3]{2}$.
> >
> > **Verificación:** $c \approx 1{,}26 \in (0,2)$ ✓, $f(c) = 2$ ✓, y $f(c)(b-a) = 2 \cdot 2 = 4 = \int_0^2 x^3\,dx$ ✓

> [!example] 📋 Planteamiento
>
> Aplica el teorema del valor medio para integrales a $f(x) = x^2$ en $[1,4]$ y compara con el promedio aritmético de los extremos.
>
> > [!success]- ✅ Solución
> >
> > **Integral:** $\int_1^4 x^2\,dx = \left[\frac{x^3}{3}\right]_1^4 = \frac{64 - 1}{3} = 21$.
> >
> > **Valor medio integral:** $\frac{21}{4-1} = 7$.
> >
> > **Punto $c$:** $c^2 = 7 \Rightarrow c = \sqrt{7} \approx 2{,}65 \in (1,4)$ ✓
> >
> > **Promedio aritmético de extremos:** $\frac{f(1) + f(4)}{2} = \frac{1 + 16}{2} = 8{,}5$.
> >
> > **Respuesta:** el valor medio integral es $7$ y se alcanza en $c = \sqrt{7}$; **no** coincide con $8{,}5$, que es el promedio de los extremos (error típico 2 de la nota) ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico la paridad de una función calculando $f(-x)$ antes de integrar en un intervalo simétrico.
> - [ ] Aplico el teorema para impares escribiendo $0$ y el de pares duplicando la integral de $0$ a $a$.
> - [ ] Calculo el valor medio de una función con $\frac{1}{b-a}\int_a^b f(x)\,dx$ y encuentro su punto $c$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Demuestro los teoremas de simetría y de periodicidad con un cambio de variable.
> - [ ] Uso el corolario $\int_0^{nT} = n\int_0^T$ para integrales sobre varios periodos completos.
> - [ ] Distingo el valor medio integral del promedio aritmético de los extremos y sé cuál aplica.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Separo cualquier función en parte par más parte impar y descarto la impar en intervalos simétricos.
> - [ ] Conecto el TVMI con el teorema del valor medio para derivadas a través de la primitiva $F(x) = \int_a^x f$.
> - [ ] Aplico el valor medio con función peso y reconozco su papel en el valor esperado de probabilidad.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 5.2 y 5.5: propiedades y valor medio.
> - R. Larson, *Cálculo* (Cengage), cap. 5.2: teorema del valor medio para integrales.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 5: symmetric and periodic functions.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la base para reconstruir el TVMI.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — linealidad, aditividad y comparación, usadas en todas las demostraciones.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — el teorema del valor intermedio que cierra la demostración.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — las identidades trigonométricas de las funciones periódicas.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice el teorema de simetría para funciones pares?::En $[-a,a]$, $\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx$, porque el área de la izquierda es igual a la de la derecha.
> - ¿Qué pasa con la integral de una función impar en $[-a,a]$?::Vale $0$: el área positiva y la negativa se cancelan por la simetría respecto al origen.
> - ¿Cuál es el teorema de periodicidad y su corolario?::$\int_a^{a+T} f = \int_0^T f$ para cualquier $a$, y por lo tanto $\int_0^{nT} f = n\int_0^T f$.
> - ¿Qué garantiza el teorema del valor medio para integrales?::Que si $f$ es continua en $[a,b]$ existe $c \in (a,b)$ con $\int_a^b f(x)\,dx = f(c)(b-a)$.
> - ¿Cuál es la diferencia entre valor medio integral y promedio aritmético?::El integral es $\frac{1}{b-a}\int_a^b f$; el de extremos es $\frac{f(a)+f(b)}{2}$. Coinciden solo en funciones lineales.
> - ¿Qué significa que una función sea cuasi-periódica con factor $k$?::Que $f(x+T) = k f(x)$, y entonces $\int_0^{nT} f = \frac{1-k^n}{1-k}\int_0^T f$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — las técnicas que estos teoremas ahorran.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/02 - Integral de Funciones por Tramos|02 - Integral de Funciones por Tramos]] — paridad y periodicidad aplicadas a funciones a trozos.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — las propiedades con las que se demuestran todos los teoremas de esta nota.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — la primitiva $F(x) = \int_a^x f$ que conecta el TVMI con el TVM de derivadas.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — dónde se rompe la hipótesis de continuidad del valor medio.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — el TVM para derivadas con el que se demuestra el TVMI.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: son simetría pura, el atajo más rentable de la nota.
> - Después pasa al 3, donde la periodicidad se combina con una identidad trigonométrica.
> - Cierra con el 4, 5 y 6, que cubren el valor medio y la diferencia con el promedio de extremos.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|Criterios de Convergencia y Divergencia]] para ver qué pasa cuando la hipótesis de continuidad falla, y en Cálculo Vectorial con [[05 – Valor promedio de una función|05 – Valor promedio de una función]] la versión en dos variables.

---

**Tags:** #MATG1045 #unidad6 #teoremas-especiales-integrales-definidas #simetria-par-impar #periodicidad #valor-medio-integrales #tvmi #fourier #rms

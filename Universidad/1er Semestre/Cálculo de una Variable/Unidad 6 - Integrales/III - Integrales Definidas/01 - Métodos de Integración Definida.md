---
dg-publish: true
tags: [MATG1045, unidad6, metodos-integracion-definida, integracion-definida, cambio-variable, integracion-partes, fracciones-parciales, integracion-trigonometrica, tecnicas-especiales]
---

# 🧮 Métodos de Integración Definida

## 🎯 Introducción

> [!info] 💡 Qué trae esta nota
>
> El [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] dice que una integral definida se evalúa con una antiderivada: $\int_a^b f(x)\,dx = F(b) - F(a)$. El problema es que casi ningún integrando llega en forma directa. Esta nota recopila los **métodos** que preparan el integrando para que el teorema aplique: cambio de variable, integración por partes, fracciones parciales, sustituciones trigonométricas y técnicas de simetría.
>
> **Por qué importa:** en un examen casi nunca se pregunta una fórmula, se pregunta **qué método conviene**. Elegirlo mal cuesta el ejercicio entero, no un paso suelto.
>
> **Ejemplo:** $\int_1^4 \frac{x}{\sqrt{x-1}}\,dx$ no sale de la tabla de integrales notables, pero un cambio de variable la convierte en una potencia simple que sí sale.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Cambio de variable en una integral definida
>
> Sea $g$ diferenciable en $[\alpha, \beta]$ con $g(\alpha) = a$ y $g(\beta) = b$, y sea $f$ continua en $[a, b]$. Entonces
>
> $$\int_a^b f(x)\,dx = \int_{\alpha}^{\beta} f(g(u))\,g'(u)\,du$$
>
> Equivalentemente: si $x = g(u)$, entonces $dx = g'(u)\,du$ **y los límites también se cambian**, uno a uno, resolviendo $g(u_1) = a$ y $g(u_2) = b$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métodos_de_Integración_Definida_01.svg]]
>
> **Se lee así:** una cadena de cajas que arranca en la integral definida original, pide identificar la sustitución $x = g(u)$, calcular el diferencial $dx = g'(u)\,du$ y encontrar los nuevos límites; ese último paso se bifurca en dos cajas, una por extremo ($u_1$ con $g(u_1) = a$ y $u_2$ con $g(u_2) = b$), que se reúnen en la integral transformada y cierran con la evaluación en los nuevos límites.
>
> **Por qué importa:** los límites forman parte del cambio de variable, no son un detalle final. Es el error más común de la técnica: integrar en la variable nueva y dejar los límites viejos, que da un resultado con buena pinta y mal valor.
>
> **Ejemplo:** en $\int_1^4 \frac{x}{\sqrt{x-1}}\,dx$, con $u = x - 1$ los extremos $x = 1$ y $x = 4$ se convierten en $u = 0$ y $u = 3$.

> [!note] 📋 Definición — Integración por partes en una integral definida
>
> Si $u$ y $v$ son diferenciables en $[a, b]$,
>
> $$\int_a^b u\,dv = [uv]_a^b - \int_a^b v\,du$$
>
> O en su forma con derivadas: $\int_a^b u(x)\,v'(x)\,dx = [u(x)\,v(x)]_a^b - \int_a^b u'(x)\,v(x)\,dx$.
>
> La elección de $u$ sigue el orden **LIATE**: **l**ogarítmicas, **i**nversas trigonométricas, **a**lgebraicas, **t**rigonométricas, **e**xponenciales. La función que se deriva más fácil va en $u$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métodos_de_Integración_Definida_02.svg]]
>
> **Se lee así:** un rombo de decisión donde se aplica LIATE sobre las dos funciones identificadas; del rombo salen dos ramas, una elige como $u$ la función prioritaria y la otra toma el resto como $dv$ junto con $dx$. La rama de $u$ pide calcular $du$ y la de $dv$ pide $v = \int dv$; las dos se juntan en la caja de aplicar la fórmula y terminan en la evaluación de los límites.
>
> **Por qué importa:** el rombo obliga a **decidir antes de integrar**. Un $u$ mal elegido deja la integral exactamente igual de difícil y el ejercicio se queda girando en un bucle que no avanza.
>
> **Ejemplo:** en $\int_1^e x\ln(x)\,dx$, LIATE pone $\ln(x)$ (logarítmica) en $u$ y $x\,dx$ (algebraica) en $dv$.

---

## ⚡ Cambio de variable paso a paso

> [!tip] 🔧 Los cuatro pasos, siempre en este orden
>
> 1. **Elegir la sustitución** $x = g(u)$ mirando la composición o el radical que estorba.
> 2. **Cambiar el diferencial**: $dx = g'(u)\,du$.
> 3. **Cambiar los límites**: resolver $g(u_1) = a$ y $g(u_2) = b$.
> 4. **Integrar en la nueva variable** y evaluar en $u_1$ y $u_2$.
>
> **Por qué importa:** el paso 3 es el que se salta. Sin él, la integral nueva se evalúa en los límites viejos y el resultado sale mal aunque toda la técnica haya sido correcta.
>
> **Ejemplo:** $\int_0^1 \frac{1}{\sqrt{1-x^2}}\,dx$ con $x = \operatorname{sen} u$ se convierte en $\int_0^{\pi/2} du = \frac{\pi}{2}$.

> [!tip] 📈 Ejemplo 1 · Sustitución trigonométrica inversa
>
> **Evalúa** $\int_0^1 \frac{1}{\sqrt{1-x^2}}\,dx$.
>
> **Paso 1:** $x = \operatorname{sen} u$, $dx = \cos u\,du$.
>
> **Paso 2:** límites: $x = 0 \Rightarrow \operatorname{sen} u = 0 \Rightarrow u = 0$; $x = 1 \Rightarrow \operatorname{sen} u = 1 \Rightarrow u = \frac{\pi}{2}$.
>
> **Paso 3:** $\int_0^{\pi/2} \frac{\cos u}{\sqrt{1 - \operatorname{sen}^2 u}}\,du = \int_0^{\pi/2} \frac{\cos u}{\cos u}\,du = \int_0^{\pi/2} 1\,du$.
>
> **Paso 4:** $[u]_0^{\pi/2} = \frac{\pi}{2}$.
>
> **Por qué importa:** es la integral que **define** al arcseno; reconocerla de vista ahorra los cuatro pasos enteros.

> [!tip] 📈 Ejemplo 2 · Sustitución algebraica
>
> **Evalúa** $\int_1^4 \frac{x}{\sqrt{x-1}}\,dx$.
>
> **Paso 1:** $u = x - 1$, entonces $x = u + 1$ y $dx = du$.
>
> **Paso 2:** límites: $x = 1 \Rightarrow u = 0$; $x = 4 \Rightarrow u = 3$.
>
> **Paso 3:** $\int_0^3 \frac{u+1}{\sqrt{u}}\,du = \int_0^3 \left(\sqrt{u} + \frac{1}{\sqrt{u}}\right)du$.
>
> **Paso 4:** $\left[\frac{2u^{3/2}}{3} + 2\sqrt{u}\right]_0^3 = \frac{2 \cdot 3\sqrt{3}}{3} + 2\sqrt{3} = 2\sqrt{3} + 2\sqrt{3} = 4\sqrt{3}$.
>
> **Por qué importa:** el truco es **sumar y restar 1** en el numerador para separar el cociente en dos potencias. Es el recurso que convierte una fracción con raíz en algo integrable de inmediato.

---

## ✂️ Integración por partes

> [!tip] 🔧 Los cuatro pasos con LIATE
>
> 1. **Separar** el integrando en $u$ y $dv$ siguiendo LIATE.
> 2. **Calcular** $du$ y $v = \int dv$.
> 3. **Aplicar** $\int_a^b u\,dv = [uv]_a^b - \int_a^b v\,du$.
> 4. **Evaluar** la parte $[uv]_a^b$ y resolver la integral nueva $\int_a^b v\,du$.
>
> **Por qué importa:** el paso 4 es donde el método a veces no simplifica nada. Si la integral nueva es más difícil que la original, la elección de $u$ estaba mal y hay que volver al paso 1.
>
> **Ejemplo:** $\int_1^e x\ln(x)\,dx$ con $u = \ln(x)$ reduce a una potencia pura.

> [!tip] 📈 Ejemplo 1 · Logaritmo por polinomio
>
> **Evalúa** $\int_1^e x\ln(x)\,dx$.
>
> **Aplicando LIATE:** $u = \ln(x)$ (logarítmica), $dv = x\,dx$ (algebraica).
>
> **Paso 1:** $du = \frac{1}{x}\,dx$, $v = \frac{x^2}{2}$.
>
> **Paso 2:** $\int_1^e x\ln(x)\,dx = \left[\frac{x^2}{2}\ln(x)\right]_1^e - \int_1^e \frac{x^2}{2} \cdot \frac{1}{x}\,dx = \left[\frac{x^2}{2}\ln(x)\right]_1^e - \int_1^e \frac{x}{2}\,dx$.
>
> **Paso 3:** $\left[\frac{x^2}{2}\ln(x)\right]_1^e - \left[\frac{x^2}{4}\right]_1^e = \left(\frac{e^2}{2} \cdot 1 - \frac{1}{2} \cdot 0\right) - \left(\frac{e^2}{4} - \frac{1}{4}\right)$.
>
> **Paso 4:** $\frac{e^2}{2} - \frac{e^2}{4} + \frac{1}{4} = \frac{e^2}{4} + \frac{1}{4} = \frac{e^2 + 1}{4}$.
>
> **Por qué importa:** fíjate en que $\ln(e) = 1$ y $\ln(1) = 0$, así que el término $[uv]$ solo aporta uno de los dos extremos.

> [!tip] 🌊 Ejemplo 2 · Exponencial por trigonométrica (partes dos veces)
>
> **Evalúa** $\int_0^{\pi} e^x \operatorname{sen}(x)\,dx$.
>
> **Primera aplicación:** $u = \operatorname{sen}(x)$, $dv = e^x\,dx$, con $du = \cos(x)\,dx$ y $v = e^x$.
>
> $$\int_0^{\pi} e^x \operatorname{sen}(x)\,dx = [e^x \operatorname{sen}(x)]_0^{\pi} - \int_0^{\pi} e^x \cos(x)\,dx = 0 - \int_0^{\pi} e^x \cos(x)\,dx$$
>
> **Segunda aplicación:** $u = \cos(x)$, $dv = e^x\,dx$, con $du = -\operatorname{sen}(x)\,dx$ y $v = e^x$.
>
> $$-\int_0^{\pi} e^x \cos(x)\,dx = -[e^x \cos(x)]_0^{\pi} - \int_0^{\pi} e^x \operatorname{sen}(x)\,dx = e^{\pi} + 1 - \int_0^{\pi} e^x \operatorname{sen}(x)\,dx$$
>
> **Resolución:** la integral original $I$ aparece a los dos lados, así que $I = e^{\pi} + 1 - I$ y por lo tanto $2I = e^{\pi} + 1$.
>
> **Respuesta:** $\int_0^{\pi} e^x \operatorname{sen}(x)\,dx = \dfrac{e^{\pi} + 1}{2}$.
>
> **Por qué importa:** es el caso en el que el método **no simplifica, se devuelve**. Ahí no se falla la técnica: hay que plantear la ecuación en la integral original y despejarla.

---

## 🧩 Fracciones parciales

> [!tip] 🔧 Proceso para integrales definidas
>
> 1. Descomponer la fracción en fracciones parciales.
> 2. Integrar cada fracción por separado.
> 3. Aplicar el teorema fundamental con los límites.
> 4. Evaluar en los extremos de integración.
>
> **Por qué importa:** el paso 1 es el único que requiere criterio; los tres siguientes son mecánicos. Si la descomposición es correcta, el resto cae solo.

> [!tip] 📋 Los tres casos de descomposición
>
> | Tipo de factor | Forma de fracción parcial |
> |---|---|
> | $(ax + b)$ | $\frac{A}{ax + b}$ |
> | $(ax + b)^n$ | $\frac{A_1}{ax + b} + \frac{A_2}{(ax + b)^2} + \cdots + \frac{A_n}{(ax + b)^n}$ |
> | $(ax^2 + bx + c)$ irreducible | $\frac{Ax + B}{ax^2 + bx + c}$ |
>
> **Por qué importa:** el segundo caso es el que se olvida: un factor repetido genera **una fracción por cada repetición**, no una sola. El tercero exige numerador de grado menor que el denominador.
>
> **Ejemplo:** $\frac{2x+1}{x^2(x+1)}$ requiere $\frac{A}{x} + \frac{B}{x^2} + \frac{C}{x+1}$, no solo dos términos.

> [!tip] 📈 Ejemplo · Fracciones parciales con límites limpios
>
> **Evalúa** $\int_1^3 \frac{2x + 1}{x^2 + x}\,dx$.
>
> **Paso 1:** factorizar el denominador: $x^2 + x = x(x+1)$.
>
> **Paso 2:** descomponer $\dfrac{2x + 1}{x(x+1)} = \dfrac{A}{x} + \dfrac{B}{x+1}$.
>
> **Paso 3:** $2x + 1 = A(x+1) + Bx$. Con valores convenientes: $x = 0 \Rightarrow 1 = A$ y $x = -1 \Rightarrow -1 = -B \Rightarrow B = 1$.
>
> **Paso 4:** $\int_1^3 \left(\frac{1}{x} + \frac{1}{x+1}\right)dx = \Big[\ln|x| + \ln|x+1|\Big]_1^3 = (\ln 3 + \ln 4) - (\ln 1 + \ln 2) = \ln 12 - \ln 2 = \ln 6$.
>
> **Respuesta:** $\ln 6$.
>
> **Por qué importa:** el denominador se anula en $x = 0$ y en $x = -1$, y **ninguno de los dos está en $[1,3]$**, así que la integral es propia y se integra directo. Si el intervalo pasara por $x = 0$ sería impropia y habría que tomar límite.

---

## 📐 Sustituciones trigonométricas

> [!tip] 📐 Los tres casos estándar
>
> | Expresión | Sustitución | Identidad que se usa |
> |---|---|---|
> | $\sqrt{a^2 - x^2}$ | $x = a\operatorname{sen}(\theta)$ | $\sqrt{a^2 - a^2\operatorname{sen}^2(\theta)} = a\cos(\theta)$ |
> | $\sqrt{a^2 + x^2}$ | $x = a\tan(\theta)$ | $\sqrt{a^2 + a^2\tan^2(\theta)} = a\sec(\theta)$ |
> | $\sqrt{x^2 - a^2}$ | $x = a\sec(\theta)$ | $\sqrt{a^2\sec^2(\theta) - a^2} = a\tan(\theta)$ |
>
> **Por qué importa:** la regla de oro es **el número primero, la variable después**: $a$ siempre va al frente. Elegir mal la identidad deja un radical que no se simplifica y el ejercicio se estanca.
>
> **Ejemplo:** $\sqrt{9 - x^2}$ es el caso 1 con $a = 3$, así que $x = 3\operatorname{sen}(\theta)$.

> [!tip] 📈 Ejemplo · Área de un semicírculo
>
> **Evalúa** $\int_0^{a} \sqrt{a^2 - x^2}\,dx$.
>
> **Paso 1:** $x = a\operatorname{sen}(\theta)$, $dx = a\cos(\theta)\,d\theta$.
>
> **Paso 2:** límites: $x = 0 \Rightarrow \theta = 0$; $x = a \Rightarrow \operatorname{sen}(\theta) = 1 \Rightarrow \theta = \frac{\pi}{2}$.
>
> **Paso 3:** $\int_0^{\pi/2} \sqrt{a^2 - a^2\operatorname{sen}^2(\theta)} \cdot a\cos(\theta)\,d\theta = \int_0^{\pi/2} a\cos(\theta) \cdot a\cos(\theta)\,d\theta = a^2 \int_0^{\pi/2} \cos^2(\theta)\,d\theta$.
>
> **Paso 4:** con $\cos^2(\theta) = \dfrac{1 + \cos(2\theta)}{2}$: $a^2 \int_0^{\pi/2} \dfrac{1 + \cos(2\theta)}{2}\,d\theta = \dfrac{a^2}{2}\left[\theta + \dfrac{\sin(2\theta)}{2}\right]_0^{\pi/2} = \dfrac{a^2}{2} \cdot \dfrac{\pi}{2} = \dfrac{\pi a^2}{4}$.
>
> **Respuesta:** $\dfrac{\pi a^2}{4}$.
>
> **Por qué importa:** el resultado **era geometría antes del cálculo**: $\frac{\pi a^2}{4}$ es exactamente el área de un cuarto de circunferencia de radio $a$. Verificarlo así detecta errores de sustitución al instante.

---

## 🎯 Técnicas especiales

> [!tip] 🎯 Aprovechando simetría (pares e impares)
>
> **Función par**, $f(-x) = f(x)$, sobre un intervalo simétrico:
>
> $$\int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$$
>
> **Función impar**, $f(-x) = -f(x)$, sobre un intervalo simétrico:
>
> $$\int_{-a}^a f(x)\,dx = 0$$
>
> **Por qué importa:** cuando el intervalo es simétrico, el **primer paso** es comprobar la paridad antes de integrar. Una impar sobre $[-a,a]$ se resuelve escribiendo cero, sin calcular nada.
>
> **Ejemplo:** $\int_{-2}^{2} x^3\,dx = 0$ porque $x^3$ es impar, mientras que $\int_{-2}^{2} x^4\,dx = 2\int_0^2 x^4\,dx$ porque $x^4$ es par.

> [!info] 🏆 La regla de Wallis
>
> Para $n$ entero no negativo:
>
> $$\int_0^{\pi/2} \operatorname{sen}^n(x)\,dx = \int_0^{\pi/2} \cos^n(x)\,dx = \begin{cases} \dfrac{(n-1)!!}{n!!} \cdot \dfrac{\pi}{2} & \text{si } n \text{ es par} \\[6pt] \dfrac{(n-1)!!}{n!!} & \text{si } n \text{ es impar} \end{cases}$$
>
> El doble factorial $n!!$ baja de dos en dos hasta 1 (o 2): $7!! = 7 \cdot 5 \cdot 3 \cdot 1$, $6!! = 6 \cdot 4 \cdot 2$.
>
> **Por qué importa:** el factor $\dfrac{\pi}{2}$ aparece **solo cuando $n$ es par**. Es la confusión clásica con la fórmula de Wallis para $\int_0^{\pi/2} \tan^n x\,dx$, donde la paridad se invierte: ahí converge solo los $n$ pares con la otra forma.
>
> **Ejemplo:** $\int_0^{\pi/2} \operatorname{sen}^4(x)\,dx = \dfrac{3!!}{4!!} \cdot \dfrac{\pi}{2} = \dfrac{3}{8} \cdot \dfrac{\pi}{2} = \dfrac{3\pi}{16}$.

> [!tip] 🔬 Ejemplo · Simetría aplicada
>
> **Evalúa** $\int_{-2}^{2} (x^4 - 3x^2 + 1)\,dx$.
>
> **Análisis de paridad:** $x^4$ es par, $-3x^2$ es par y $1$ es par; la suma de pares es par, y el intervalo $[-2,2]$ es simétrico.
>
> **Aplicando simetría:** $\int_{-2}^{2} (x^4 - 3x^2 + 1)\,dx = 2\int_0^{2} (x^4 - 3x^2 + 1)\,dx$.
>
> **Evaluando:** $2\left[\dfrac{x^5}{5} - x^3 + x\right]_0^2 = 2\left(\dfrac{32}{5} - 8 + 2\right) = 2\left(\dfrac{32}{5} - \dfrac{30}{5}\right) = 2 \cdot \dfrac{2}{5} = \dfrac{4}{5}$.
>
> **Respuesta:** $\dfrac{4}{5}$.
>
> **Por qué importa:** la paridad te ahorra **la mitad** del intervalo. Y conviene comprobar el signo: $\frac{32}{5} - 6$ es positivo, así que el resultado tiene que serlo; un valor negativo habría delatado un error aritmético.

---

## 🧭 Cómo elegir el método

> [!info] 🖼️ El algoritmo de decisión
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métodos_de_Integración_Definida_03.svg]]
>
> **Se lee así:** un árbol de decisiones con rombos encadenados. El primero pregunta si la integral está en forma estándar: si es sí, se aplica el teorema fundamental directo; si es no, el siguiente rombo pregunta si hay producto de funciones. De ahí se deriva a sustitución o a integración por partes según si una función deriva la otra, y el resto de ramas pasan por el rombo de fracción racional (fracciones parciales) y el de radical con cuadrática (sustitución trigonométrica), con un último camino a las técnicas especiales.
>
> **Por qué importa:** el diagrama te da un **criterio de decisión antes de calcular**, no una lista de técnicas sueltas. Evita forzar una sustitución donde no aplica y perder tiempo cuando el teorema fundamental ya bastaba.
>
> **Ejemplo:** $\int_0^1 \frac{1}{\sqrt{1-x^2}}\,dx$ cae en la rama de radical con cuadrática y se resuelve con la sustitución $x = \operatorname{sen}(u)$ y límites $u = 0$ y $u = \frac{\pi}{2}$.

> [!info] ✅ Lista de verificación antes de integrar
>
> 1. ¿La función es **continua** en el intervalo de integración?
> 2. ¿Hay discontinuidades que hagan la integral **impropia**?
> 3. ¿Se puede simplificar antes con **propiedades** (simetría, linealidad)?
> 4. ¿Cuál método es el **más corto**: sustitución, partes, fracciones parciales o trigonométrica?
> 5. ¿Los límites de integración están **dentro del dominio** del integrando?
>
> **Por qué importa:** casi todos los errores de examen salen del paso 2 o del paso 5. Comprobar la continuidad antes de integrar cuesta diez segundos y evita responder una integral que no existe.

---

## 🗺️ Mapa de los métodos

> [!info] 🖼️ El arsenal completo en un vistazo
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métodos_de_Integración_Definida_04.svg]]
>
> **Se lee así:** un cuadro raíz "Métodos Integración" despliega cinco subgrafos de rectángulos: la sustitución (con cambio de variable, límites nuevos y verificación), las partes (con LIATE, recursión y evaluación de límites), las fracciones parciales (descomposición, factorización e integración término a término), las trigonométricas (identidades, sustituciones estándar y geometría) y las aplicaciones (áreas, volúmenes y física).
>
> **Por qué importa:** el mapa es el **índice de la unidad** de un vistazo: para cada tipo de problema ves qué técnica existe y qué pasos tiene. Te sirve para repasar sin releer la nota entera.
>
> **Ejemplo:** al calcular el área de un semicírculo con $\int_0^a \sqrt{a^2 - x^2}\,dx$ recorres la rama de trigonométricas, con su sustitución estándar y la geometría del resultado.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cuatro fallos que más se repiten
>
> 1. **Límites sin cambiar en la sustitución.** Se integra en la variable nueva y se evalúa en los límites viejos. *Solución:* siempre convertir los extremos con $g(u_1) = a$ y $g(u_2) = b$ antes de integrar.
> 2. **Signos en integración por partes.** Se olvida el menos de $\int u\,dv = uv - \int v\,du$. *Solución:* escribir la fórmula completa cada vez; el signo no se deduce de memoria.
> 3. **Fracciones parciales mal descompuestas.** Se omite un término o se usa numerador de grado mayor. *Solución:* multiplicar la descomposición para recuperar la fracción original antes de integrar.
> 4. **Dominio de las sustituciones trigonométricas.** Se aplica sin verificar que la raíz sea real. *Solución:* $\sqrt{a^2 - x^2}$ exige $|x| \leq a$ y la sustitución debe ser invertible en el intervalo.
>
> **Por qué importa:** los cuatro son errores de **planteamiento**, no de cálculo, y por eso no los detecta la verificación automática de la calculadora. Se previenen en el paso 1 de cada técnica.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^2 \frac{x}{1+x^2}\,dx$ con un cambio de variable.
>
> > [!success]- ✅ Solución
> >
> > **Método:** cambio de variable con $u = 1 + x^2$, entonces $du = 2x\,dx$ y $\frac{1}{2}du = x\,dx$.
> >
> > **Límites:** $x = 0 \Rightarrow u = 1$ y $x = 2 \Rightarrow u = 5$.
> >
> > $$\int_1^5 \frac{1}{2}\frac{du}{u} = \frac{1}{2}\Big[\ln|u|\Big]_1^5 = \frac{1}{2}(\ln 5 - \ln 1) = \frac{\ln 5}{2}.$$
> >
> > **Respuesta:** $\dfrac{\ln 5}{2} \approx 0{,}8047$.

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^1 x\,e^{x^2}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Método:** cambio de variable con $u = x^2$, entonces $du = 2x\,dx$ y $\frac{1}{2}du = x\,dx$.
> >
> > **Límites:** $x = 0 \Rightarrow u = 0$ y $x = 1 \Rightarrow u = 1$.
> >
> > $$\frac{1}{2}\int_0^1 e^u\,du = \frac{1}{2}\Big[e^u\Big]_0^1 = \frac{e - 1}{2}.$$
> >
> > **Respuesta:** $\dfrac{e - 1}{2} \approx 0{,}8592$.

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^1 x\,e^{x}\,dx$ por partes.
>
> > [!success]- ✅ Solución
> >
> > **Método:** LIATE pone $u = x$ (algebraica) y $dv = e^x\,dx$ (exponencial), con $du = dx$ y $v = e^x$.
> >
> > $$\int_0^1 x e^x\,dx = \Big[x e^x\Big]_0^1 - \int_0^1 e^x\,dx = (1 \cdot e - 0) - \Big[e^x\Big]_0^1 = e - (e - 1) = 1.$$
> >
> > **Respuesta:** $1$.
> >
> > **Verificación:** $\frac{d}{dx}(x e^x - e^x) = e^x + x e^x - e^x = x e^x$ ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^{\pi} e^{x} \cos(x)\,dx$ aplicando partes dos veces.
>
> > [!success]- ✅ Solución
> >
> > **Método:** $u = \cos x$, $dv = e^x dx$, con $du = -\operatorname{sen} x\,dx$ y $v = e^x$.
> >
> > $$I = \Big[e^x \cos x\Big]_0^{\pi} + \int_0^{\pi} e^x \operatorname{sen} x\,dx = (-e^{\pi} - 1) + J.$$
> >
> > Para $J = \int_0^{\pi} e^x \operatorname{sen} x\,dx$: $u = \operatorname{sen} x$, $dv = e^x dx$, con $du = \cos x\,dx$ y $v = e^x$, así que $J = \Big[e^x \operatorname{sen} x\Big]_0^{\pi} - I = 0 - I$.
> >
> > Sustituyendo: $I = -e^{\pi} - 1 - I$, luego $2I = -(e^{\pi} + 1)$.
> >
> > **Respuesta:** $\displaystyle\int_0^{\pi} e^x \cos x\,dx = -\dfrac{e^{\pi} + 1}{2}$.

> [!example] 📋 Planteamiento
>
> Evalúa $\int_1^3 \frac{2x + 1}{x^2 + x}\,dx$ por fracciones parciales.
>
> > [!success]- ✅ Solución
> >
> > **Descomposición:** $x^2 + x = x(x+1)$, y $\dfrac{2x+1}{x(x+1)} = \dfrac{A}{x} + \dfrac{B}{x+1}$ da $A = 1$ y $B = 1$.
> >
> > **Integración:** $\int_1^3 \left(\dfrac{1}{x} + \dfrac{1}{x+1}\right)dx = \Big[\ln|x| + \ln|x+1|\Big]_1^3$.
> >
> > **Evaluación:** $(\ln 3 + \ln 4) - (\ln 1 + \ln 2) = \ln 12 - \ln 2 = \ln 6$.
> >
> > **Respuesta:** $\ln 6 \approx 1{,}7918$.
> >
> > **Nota:** el denominador se anula en $x = 0$ y $x = -1$, fuera de $[1,3]$, así que la integral es propia.

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^2 \sqrt{4 - x^2}\,dx$ justificando el resultado con geometría.
>
> > [!success]- ✅ Solución
> >
> > **Método:** sustitución trigonométrica con $x = 2\operatorname{sen}(\theta)$, $dx = 2\cos(\theta)\,d\theta$; límites $\theta = 0$ y $\theta = \frac{\pi}{2}$.
> >
> > $$\int_0^{\pi/2} \sqrt{4 - 4\operatorname{sen}^2\theta} \cdot 2\cos\theta\,d\theta = 4\int_0^{\pi/2} \cos^2\theta\,d\theta = 4 \cdot \frac{\pi}{4} = \pi.$$
> >
> > **Respuesta:** $\pi$.
> >
> > **Comprobación geométrica:** la integral es el área bajo $y = \sqrt{4-x^2}$ entre 0 y 2, es decir un **cuarto** de circunferencia de radio 2: $\frac{1}{4}\pi (2)^2 = \pi$ ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{-2}^{2} (x^4 - 3x^2 + 1)\,dx$ usando simetría.
>
> > [!success]- ✅ Solución
> >
> > **Paridad:** los tres términos son pares y el intervalo es simétrico, así que $\int_{-2}^{2} = 2\int_{0}^{2}$.
> >
> > $$2\left[\frac{x^5}{5} - x^3 + x\right]_0^2 = 2\left(\frac{32}{5} - 8 + 2\right) = 2\left(\frac{32}{5} - \frac{30}{5}\right) = \frac{4}{5}.$$
> >
> > **Respuesta:** $\dfrac{4}{5}$.
> >
> > **Control de signo:** $\frac{32}{5} - 6 = \frac{2}{5} > 0$, coherente con una función que vale 1 en $x = 0$ y crece.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo de memoria la fórmula de cambio de variable con sus dos límites nuevos.
> - [ ] Aplico LIATE para elegir $u$ y $dv$ sin probar y error.
> - [ ] Reconozco los tres casos estándar de sustitución trigonométrica y su $a$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo una integral por partes que se devuelve sobre sí misma, planteando la ecuación en la integral original.
> - [ ] Descompongo una fracción racional con factor repetido y con cuadrática irreducible.
> - [ ] Compruebo la paridad antes de integrar en un intervalo simétrico y ahorro la mitad del trabajo.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Elijo el método más corto leyendo solo el integrando, siguiendo el árbol de decisión de la nota.
> - [ ] Verifico el resultado con geometría o con un valor numérico aproximado cuando la integral lo permite.
> - [ ] Detecto cuándo una integral es impropia y aplico el límite en lugar de sustituir los extremos a ciegas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 7.1–7.6: técnicas de integración.
> - R. Larson, *Cálculo* (Cengage), cap. 7.2–7.6: sustitución, partes y fracciones parciales.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 6: métodos de integración.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la Parte II que convierte cada antiderivada en un número.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — linealidad, aditividad y simetría, que se usan antes de integrar.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — la sustitución con todos sus casos, nota completa.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — LIATE y el caso que se devuelve, en detalle.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice el teorema de cambio de variable en una integral definida?::$\int_a^b f(x)\,dx = \int_{\alpha}^{\beta} f(g(u))\,g'(u)\,du$, donde $g(\alpha)=a$, $g(\beta)=b$ y $f$ es continua en $[a,b]$.
> - ¿Por qué falla una sustitución bien hecha si no se cambian los límites?::Porque la integral nueva queda en la variable $u$ pero se evalúa en valores de $x$; los extremos se convierten resolviendo $g(u_1)=a$ y $g(u_2)=b$.
> - ¿En qué orden aplica LIATE y para qué sirve?::Logarítmicas, inversas trigonométricas, algebraicas, trigonométricas y exponenciales; decide cuál va en $u$ (la que se deriva más fácil) y cuál en $dv$.
> - ¿Qué hago cuando por partes devuelve la integral original?::La planteo como ecuación: si $I = \text{algo} - I$, entonces $2I = \text{algo}$ y se despeja $I$, como en $\int e^x \operatorname{sen} x\,dx$.
> - ¿Cuándo converge la regla de Wallis con el factor $\pi/2$?::Cuando $n$ es **par**: $\int_0^{\pi/2}\operatorname{sen}^n x\,dx = \frac{(n-1)!!}{n!!}\cdot\frac{\pi}{2}$; si $n$ es impar no lleva ese factor.
> - ¿Qué verifico antes de integrar en $[-a,a]$?::La paridad: si $f$ es impar la integral vale 0, y si es par vale $2\int_0^a f(x)\,dx$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — de donde salen las $F$ que estas técnicas buscan.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — el catálogo que hay que agotar antes de llamar a un método.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — la nota técnica del primer método de esta página.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/05 - Integrales por Fracciones Parciales|05 - Integrales por Fracciones Parciales]] — descomposición completa, incluidas raíces complejas.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — qué pasa cuando los límites salen del dominio o son infinitos.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la primera aplicación directa de estas integrales definidas.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: son cambio de variable puro, el paso que sostiene todo lo demás.
> - Después pasa al 3 y al 4, donde entra LIATE y el caso en que la integral se devuelve sobre sí misma.
> - Cierra con el 5 y el 6, que combinan descomposición y sustitución trigonométrica con comprobación geométrica.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|Cambio de Variable en Integrales]] para ver cada técnica con todos sus casos especiales.

---

**Tags:** #MATG1045 #unidad6 #metodos-integracion-definida #integracion-definida #cambio-variable #integracion-partes #fracciones-parciales #integracion-trigonometrica #tecnicas-especiales

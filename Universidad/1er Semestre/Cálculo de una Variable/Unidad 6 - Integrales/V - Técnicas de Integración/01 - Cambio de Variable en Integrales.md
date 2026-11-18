---
dg-publish: true
tags: [MATG1045, unidad6, cambio-de-variable-en-integrales, integrales, sustitucion, cambio-variable, tecnicas-integracion, trigonometricas, integrales-definidas]
---

# 🔄 Cambio de Variable en Integrales

## 🎯 Introducción

> [!info] 💡 Qué es el cambio de variable
>
> El **cambio de variable** (o sustitución) es la técnica que transforma una integral compleja en una más simple: eliges una expresión $u = g(x)$, reescribes la integral en $u$ y, si la derivada $g'(x)$ está presente (o es múltiplo constante), la integral resultante es inmediata. Es la primera técnica que se aprende después de las tablas y la que más se usa en todo el cálculo.
>
> **Por qué importa:** casi cualquier integral se puede plantear como composición $f(g(x)) \cdot g'(x)$; reconocer esa estructura es el 90 % del trabajo. Además, la misma idea sostiene las **sustituciones trigonométricas** para raíces de la forma $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$ y $\sqrt{x^2-a^2}$, que también cubre esta nota.
>
> **Ejemplo:** en $\int 2x(x^2+1)^3\,dx$ tomas $u = x^2+1$ y la integral se convierte en $\int u^3\,du$, que es una potencia pura.

> [!tip] 🎯 Las dos caras de la técnica en esta nota
>
> - **Sustitución clásica:** $u = g(x)$ con $g'(x)$ presente; resuelve potencias, exponenciales y logarítmicas.
> - **Sustituciones trigonométricas:** $x = a\sin t$, $x = a\tan t$ o $x = a\sec t$ según el signo bajo la raíz; resuelve integrales con radicales y con $a^2 \pm x^2$ en el denominador.
>
> **Por qué importa:** las dos comparten el mismo esqueleto (elegir la variable, transformar, integrar, volver), así que lo que practiques con una te sirve con la otra.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Cambio de variable (método general)
>
> Para resolver $\int f(g(x)) \cdot g'(x)\,dx$ se hace:
>
> 1. **Identificar:** $u = g(x)$.
> 2. **Derivar:** $du = g'(x)\,dx$.
> 3. **Sustituir:** $\int f(u)\,du$.
> 4. **Resolver:** integrar respecto a $u$.
> 5. **Regresar:** sustituir $u$ por $g(x)$ de nuevo.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Cambio_de_Variable_en_Integrales_01.svg]]
>
> **Se lee así:** un diagrama de flujo con un rectángulo de objetivo y una columna de cinco pasos numerados que descienden en línea recta, cada uno unido al siguiente por una flecha. Los pasos son tipo de tarea, no ecuaciones sueltas: identificar, derivar, sustituir, resolver y regresar. La columna desemboca en un recuadro de resultado y de ahí sale una caja aparte de consejo sobre la derivada.
>
> **Por qué importa:** el **orden** de los pasos es lo que evita los errores más comunes: olvidar el $dx$, no volver a la variable original o no verificar que la derivada esté presente. Es una lista de control mental para cada integral por sustitución.
>
> **Ejemplo:** en $\int 2x(x^2+1)^3\,dx$ recorres la columna con $u = x^2+1$, obtienes $\int u^3\,du$ y vuelves a la variable original para llegar a $\frac{(x^2+1)^4}{4} + C$.

---

## 🧮 Método general y casos comunes

> [!example] 📊 Los tres patrones que casi siempre funcionan
>
> **1 · Potencias con derivada presente:**
> $$\int (ax+b)^n\,dx = \frac{(ax+b)^{n+1}}{a(n+1)} + C$$
>
> **2 · Exponenciales:**
> $$\int e^{ax+b}\,dx = \frac{e^{ax+b}}{a} + C$$
>
> **3 · Logarítmicas:**
> $$\int \frac{f'(x)}{f(x)}\,dx = \ln|f(x)| + C$$
>
> **Por qué importa:** los tres son el mismo patrón $u = g(x)$ con $du$ presente; reconocerlos de memoria te ahorra plantear la sustitución explícita en cada ejercicio.

> [!warning] 🚨 Errores comunes
>
> - **Olvidar el factor diferencial $dx$:** al sustituir, $dx = du/g'(x)$ viaja con la integral.
> - **No verificar la derivada:** si $g'(x)$ no aparece (ni como múltiplo constante), la sustitución no simplifica nada.
> - **Confundir los límites** en integrales definidas: si cambias de variable, cambia también el intervalo.
> - **No volver a la variable original:** la respuesta en $u$ está incompleta.
>
> **Por qué importa:** los cuatro son de **planteamiento** y ninguno avisa con error; se previenen repasando los cinco pasos antes de integrar.

> [!tip] 💡 Estrategias de reconocimiento
>
> - Buscar **funciones compuestas** $f(g(x))$ con su derivada cerquita.
> - Comprobar si $g'(x)$ aparece como factor; si no, ver si es **múltiplo constante** (se ajusta el factor).
> - Practicar el reconocimiento de patrones: a más integrales vistas, más rápido se ve el $u$.
>
> **Por qué importa:** la sustitución no se inventa en el ejercicio: se reconoce. La práctica de patrones es lo que convierte los 5 pasos en un reflejo.

---

## 📐 Integrales definidas con cambio de variable

> [!info] 📋 Las dos vías para $\int_a^b f(g(x))\,g'(x)\,dx$
>
> **Opción 1 · Cambiar límites:** con $u = g(x)$, tomar $u_1 = g(a)$ y $u_2 = g(b)$ y escribir $\int_{u_1}^{u_2} f(u)\,du$.
>
> **Opción 2 · Evaluar al final:** integrar en $u$, volver a $x$ y sustituir los límites originales.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Cambio_de_Variable_en_Integrales_02.svg]]
>
> **Se lee así:** de una caja inicial con la integral definida salen dos ramas paralelas, una por cada vía. La primera se abre en dos cajas hermanas con los valores de la variable auxiliar en los extremos y desemboca en una caja con la integral ya escrita en la variable nueva; la segunda baja en línea recta hasta una caja con el resultado antiderivativo en la variable original. Las dos convergen en una caja final que pide elegir la vía con menos álgebra.
>
> **Por qué importa:** las dos ramas llegan al mismo número por caminos distintos; el esquema te hace **comparar antes de calcular** y evita arrastrar la variable auxiliar hasta el final.
>
> **Ejemplo:** con $\int_0^1 2x e^{x^2}\,dx$, la rama de cambiar límites lleva a $u = x^2$ con extremos $0$ y $1$ y a $\int_0^1 e^u\,du$, mientras la otra integra primero y evalúa al final.

> [!example] 📈 Ejemplo resuelto — los dos métodos
>
> **Resolver** $\int_0^1 2x e^{x^2}\,dx$.
>
> **Método 1 (cambio de límites):** $u = x^2$, $du = 2x\,dx$; cuando $x = 0$ → $u = 0$; cuando $x = 1$ → $u = 1$; luego $\int_0^1 e^u\,du = \big[e^u\big]_0^1 = e - 1$.
>
> **Método 2 (evaluar al final):** $\int 2x e^{x^2}\,dx = e^{x^2} + C$, y $\big[e^{x^2}\big]_0^1 = e^1 - e^0 = e - 1$.
>
> **Por qué importa:** los dos caminos dan $e-1$; con límites simples cualquiera sirve, pero si los límites en $x$ fueran incómodos, cambiarlos te ahorra trabajo.

---

## 🔺 Sustituciones trigonométricas

> [!info] 💡 Qué son y cuándo usarlas
>
> Las **sustituciones trigonométricas** son cambios de variable especiales que usan identidades trigonométricas para simplificar integrales con expresiones de la forma $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$ y $\sqrt{x^2 - a^2}$.
>
> **Por qué importa:** son la única vía para sacar la raíz del integrando; una vez dentro del ángulo, la identidad $\sin^2 + \cos^2 = 1$ (o sus primas) elimina el radical de golpe.

> [!note] 📋 Definición — Los tres casos de sustitución trigonométrica
>
> **Caso 1 · $\sqrt{a^2 - x^2}$** — usar $x = a\sin(t)$:
>
> - $dx = a\cos(t)\,dt$
> - $\sqrt{a^2 - x^2} = a\cos(t)$
> - **Triángulo:** hipotenusa $= a$, opuesto $= x$, adyacente $= \sqrt{a^2 - x^2}$
>
> **Caso 2 · $\sqrt{a^2 + x^2}$** — usar $x = a\tan(t)$:
>
> - $dx = a\sec^2(t)\,dt$
> - $\sqrt{a^2 + x^2} = a\sec(t)$
> - **Triángulo:** hipotenusa $= \sqrt{a^2 + x^2}$, opuesto $= x$, adyacente $= a$
>
> **Caso 3 · $\sqrt{x^2 - a^2}$** — usar $x = a\sec(t)$:
>
> - $dx = a\sec(t)\tan(t)\,dt$
> - $\sqrt{x^2 - a^2} = a\tan(t)$
> - **Triángulo:** hipotenusa $= x$, opuesto $= \sqrt{x^2 - a^2}$, adyacente $= a$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Cambio_de_Variable_en_Integrales_03.svg]]
>
> **Se lee así:** desde una caja raíz salen tres ramas paralelas, una por cada forma de raíz cuadrada, y cada rama corresponde a una sustitución trigonométrica distinta. De cada una cuelgan tres cajas hermanas: el diferencial que se deriva de la sustitución, la igualdad que permite simplificar la raíz y el triángulo de referencia con sus lados.
>
> **Por qué importa:** la simetría del esquema muestra que **el método es el mismo en los tres casos** y solo cambian los lados del triángulo: mira el signo bajo la raíz y ya sabes qué sustitución elegir.
>
> **Ejemplo:** para $\int \frac{dx}{x^2 + 9}$ tomas la rama de "suma", usas $x = 3\tan(t)$ y llegas a $\frac{1}{3}\arctan\left(\frac{x}{3}\right) + C$.

> [!warning] 🔍 Cuándo usar cada sustitución
>
> - **$a^2 - x^2$** → círculo, usar $\sin$.
> - **$a^2 + x^2$** → hipérbola, usar $\tan$.
> - **$x^2 - a^2$** → hipérbola, usar $\sec$.
>
> **Completar cuadrados si hace falta:**
> $$x^2 + bx + c = \left(x + \frac{b}{2}\right)^2 + \left(c - \frac{b^2}{4}\right)$$
>
> **Por qué importa:** la regla de los signos se resuelve en una línea; completar cuadrados te saca del apuro cuando la forma no es exactamente $a^2 \pm x^2$.

---

## 🧭 Triángulos y fórmulas de referencia

> [!info] 🖼️ Triángulos de referencia para volver a $x$
>
> Para regresar a la variable original se construye un triángulo rectángulo según cada caso:
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Cambio_de_Variable_en_Integrales_04.svg]]
>
> **Se lee así:** el diagrama parte de una caja que anuncia la construcción de los triángulos para volver a la variable original, y de ella salen tres ramas, cada una rotulada con una raíz distinta. Cada rama tiene dos cajas encadenadas: la primera asigna hipotenusa y catetos, y la segunda da la relación entre la sustitución y el ángulo inverso. Las tres ramas avanzan con la misma lógica.
>
> **Por qué importa:** el paso que más se olvida es justamente **volver a $x$**; con el triángulo a la vista tienes $\sin t$, $\cos t$ o $\tan t$ en función de $x$ y evitas dejar la respuesta en la variable auxiliar.
>
> **Ejemplo:** en $\int \frac{dx}{\sqrt{4 - x^2}}$ el triángulo del primer caso da $t = \arcsin\left(\frac{x}{2}\right)$, y la integral queda $\arcsin\left(\frac{x}{2}\right) + C$.

> [!note] 🚀 Integrales inmediatas con sustituciones trigonométricas
>
> **Tipo $\sqrt{a^2 - x^2}$:**
>
> - $\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\left(\frac{x}{a}\right) + C$
> - $\int \sqrt{a^2 - x^2}\,dx = \frac{x}{2}\sqrt{a^2 - x^2} + \frac{a^2}{2}\arcsin\left(\frac{x}{a}\right) + C$
>
> **Tipo $\sqrt{a^2 + x^2}$:**
>
> - $\int \frac{dx}{a^2 + x^2} = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C$
> - $\int \frac{dx}{\sqrt{a^2 + x^2}} = \ln\left|x + \sqrt{a^2 + x^2}\right| + C$
>
> **Tipo $\sqrt{x^2 - a^2}$:**
>
> - $\int \frac{dx}{\sqrt{x^2 - a^2}} = \ln\left|x + \sqrt{x^2 - a^2}\right| + C$
> - $\int \frac{dx}{x^2 - a^2} = \frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right| + C$
>
> **Por qué importa:** son las siete salidas limpias hacia las que tienden estas integrales; si tu resultado no se parece a ninguna, revisa la sustitución antes de seguir.

---

## ⚠️ Errores comunes

> [!warning] 🚨 La lista de comprobación antes de entregar
>
> 1. **¿Aparece la derivada?** Verificar que $g'(x)$ esté presente o sea múltiplo constante.
> 2. **¿Viajó el $dx$?** Cada $dx$ se reescribe en $du$ con su factor.
> 3. **¿Se cambió el intervalo?** En definidas, si cambias la variable, cambia $[a,b]$ por $[g(a),g(b)]$.
> 4. **¿Se volvió a $x$?** La respuesta final siempre en la variable original.
> 5. **¿Se usó el signo correcto bajo la raíz?** $\sin$ para diferencia, $\tan$ para suma, $\sec$ para diferencia con $x$ adelante.
>
> **Por qué importa:** las cinco preguntas cubren los fallos típicos de esta técnica; hacerlas antes de tachar el ejercicio te ahorra la corrección después.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Resuelve $\int 2x(x^2 + 1)^3\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $u = x^2 + 1$, $du = 2x\,dx$ (la derivada aparece completa).
> >
> > $$\int 2x(x^2+1)^3\,dx = \int u^3\,du = \frac{u^4}{4} + C$$
> >
> > **Vuelta a $x$:** $\frac{(x^2 + 1)^4}{4} + C$.
> >
> > **Control:** derivando, $\frac{d}{dx}\frac{(x^2+1)^4}{4} = (x^2+1)^3 \cdot 2x$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int 3x^2 e^{x^3}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $u = x^3$, $du = 3x^2\,dx$.
> >
> > $$\int 3x^2 e^{x^3}\,dx = \int e^u\,du = e^u + C$$
> >
> > **Vuelta a $x$:** $e^{x^3} + C$.
> >
> > **Patrón:** exponencial con el exponente igual a la derivada del exponente ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{6x}{x^2 + 1}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $u = x^2 + 1$, $du = 2x\,dx$, luego $6x\,dx = 3\,du$.
> >
> > $$\int \frac{6x}{x^2+1}\,dx = 3\int \frac{1}{u}\,du = 3\ln|u| + C$$
> >
> > **Vuelta a $x$:** $3\ln(x^2 + 1) + C$ (sin valor absoluto porque $x^2+1 > 0$).
> >
> > **Patrón:** derivada sobre función = logaritmo ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int_0^1 2x e^{x^2}\,dx$ con las dos vías.
>
> > [!success]- ✅ Solución
> >
> > **Vía 1 (cambiar límites):** $u = x^2$, $du = 2x\,dx$; extremos: $x = 0 \Rightarrow u = 0$ y $x = 1 \Rightarrow u = 1$.
> > $$\int_0^1 e^u\,du = \big[e^u\big]_0^1 = e - 1$$
> >
> > **Vía 2 (evaluar al final):** $\int 2xe^{x^2}\,dx = e^{x^2} + C$, y $\big[e^{x^2}\big]_0^1 = e^1 - e^0 = e - 1$.
> >
> > **Respuesta:** $e - 1$ por las dos vías ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{dx}{\sqrt{4 - x^2}}$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $a = 2$, usar $x = 2\sin(t)$, $dx = 2\cos(t)\,dt$.
> >
> > **Raíz:** $\sqrt{4 - x^2} = \sqrt{4 - 4\sin^2 t} = 2\cos t$.
> >
> > $$\int \frac{2\cos t\,dt}{2\cos t} = \int dt = t + C$$
> >
> > **Vuelta a $x$:** del triángulo, $t = \arcsin\left(\frac{x}{2}\right)$.
> >
> > **Respuesta:** $\arcsin\left(\frac{x}{2}\right) + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{dx}{x^2 + 9}$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $a = 3$, usar $x = 3\tan(t)$, $dx = 3\sec^2(t)\,dt$.
> >
> > **Denominador:** $x^2 + 9 = 9\tan^2 t + 9 = 9\sec^2 t$.
> >
> > $$\int \frac{3\sec^2 t\,dt}{9\sec^2 t} = \frac{1}{3}\int dt = \frac{t}{3} + C$$
> >
> > **Vuelta a $x$:** $t = \arctan\left(\frac{x}{3}\right)$.
> >
> > **Respuesta:** $\frac{1}{3}\arctan\left(\frac{x}{3}\right) + C$ — coincide con la fórmula de referencia ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{\sqrt{x^2 - 1}}{x}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $a = 1$, usar $x = \sec(t)$, $dx = \sec(t)\tan(t)\,dt$, $\sqrt{x^2 - 1} = \tan t$.
> >
> > $$\int \frac{\tan t \cdot \sec t \tan t\,dt}{\sec t} = \int \tan^2 t\,dt = \int (\sec^2 t - 1)\,dt = \tan t - t + C$$
> >
> > **Vuelta a $x$:** $\tan t = \sqrt{x^2 - 1}$ y $t = \arccos\left(\frac{1}{x}\right)$ (o $\arctan\sqrt{x^2-1}$).
> >
> > **Respuesta:** $\sqrt{x^2 - 1} - \arccos\left(\frac{1}{x}\right) + C$.
> >
> > **Truco:** $\tan^2 = \sec^2 - 1$ convierte la potencia en una fórmula tabulada ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico $u = g(x)$ y escribo $du$ correctamente, incluido el factor $dx$.
> - [ ] Aplico los tres patrones clásicos (potencia, exponencial, logarítmica) sin plantear la sustitución completa.
> - [ ] Vuelvo siempre a la variable original antes de dar la respuesta.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo integrales definidas con cambio de variable usando las dos vías y elijo la más corta.
> - [ ] Elijo la sustitución trigonométrica correcta según el signo bajo la raíz.
> - [ ] Construyo el triángulo de referencia para recuperar $t$ en función de $x$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Completo cuadrados para llevar una forma no estándar a uno de los tres casos.
> - [ ] Resuelvo integrales con radicales compuestos combinando completar cuadrados y sustitución trigonométrica.
> - [ ] Verifico cada resultado derivando la respuesta y comparando con el integrando original.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 5.5: integración por sustitución.
> - G. Strang, *Calculus* (Wellesley-Cambridge): sustitución y cambios de variable.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — el concepto de antiderivada que toda sustitución usa.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la base teórica de las integrales definidas con cambio de límites.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — la siguiente técnica, para productos sin derivada limpia.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/05 - Integrales por Fracciones Parciales|05 - Integrales por Fracciones Parciales]] — técnica complementaria para racionales.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿En qué consiste el cambio de variable?::$u = g(x)$ con $du = g'(x)\,dx$: convierte $\int f(g(x))g'(x)\,dx$ en $\int f(u)\,du$; se integra en $u$ y se vuelve a $x$.
> - ¿Cuáles son los cinco pasos del método?::Identificar $u$, derivar $du$, sustituir, resolver y regresar a la variable original.
> - ¿Qué cuidado hay con el $dx$?::Viaja con la sustitución: si $u = g(x)$, entonces $dx = du/g'(x)$; olvidarlo desbalancea la integral.
> - ¿Qué hago con una integral definida?::Vía 1: cambiar límites a $u_1 = g(a)$ y $u_2 = g(b)$. Vía 2: integrar y evaluar en $x$ al final; ambas dan lo mismo.
> - ¿Qué sustitución para $\sqrt{a^2 - x^2}$?::$x = a\sin t$ con $dx = a\cos t\,dt$; la raíz queda $a\cos t$ (triángulo: hipotenusa $a$, opuesto $x$).
> - ¿Y para $\sqrt{a^2 + x^2}$ y $\sqrt{x^2 - a^2}$?::$x = a\tan t$ (raíz $= a\sec t$) y $x = a\sec t$ (raíz $= a\tan t$), respectivamente.
> - ¿Cómo vuelvo a la variable $x$?::Con el triángulo de referencia: expreso $\sin t$, $\cos t$ o $\tan t$ en función de $x$; nunca dejes la respuesta en $t$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/02 - Identidades Trigonométricas para Integrales|02 - Identidades Trigonométricas para Integrales]] — las identidades que hacen posible la vuelta a la variable original.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — potencias de senos y cosenos, donde la sustitución trabaja con ángulos.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — la otra técnica básica: productos, no composiciones.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/04 - Integrales de Funciones Inversas|04 - Integrales de Funciones Inversas]] — integrales donde la variable se vuelve la función inversa.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — la misma sustitución evaluada con límites.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — aplicaciones donde el cambio de variable simplifica el radical.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1, 2 y 3: los tres patrones clásicos, el esqueleto de todo lo demás.
> - Después pasa al 4, donde entran las dos vías de las integrales definidas.
> - Cierra con el 5, 6 y 7: los tres casos de sustitución trigonométrica, uno por cada signo bajo la raíz.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|Integración por Partes]] para los productos sin derivada limpia.

---

**Tags:** #MATG1045 #unidad6 #cambio-de-variable-en-integrales #integrales #sustitucion #cambio-variable #tecnicas-integracion #trigonometricas #integrales-definidas

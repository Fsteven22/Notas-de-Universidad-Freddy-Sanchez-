---
dg-publish: true
tags: [MATG1045, unidad2, formas-indeterminadas, matemáticas, cálculo, límites, factorización, racionalización, cancelación, algebra, técnicas-estudio, teorema-emparedado, lhopital, derivadas, university]
---

# ❓ Formas Indeterminadas, Teorema del Emparedado y Regla de L'Hôpital

## 🎯 Introducción

> [!tip] 💡 Qué son las formas indeterminadas
>
> Una **forma indeterminada** aparece cuando la sustitución directa en un límite produce una expresión sin sentido por sí sola: $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \cdot \infty$, $\infty - \infty$, $0^0$, $1^\infty$ o $\infty^0$. El símbolo no está mal escrito: lo que falta es información sobre **qué tan rápido** tienden a cero (o a infinito) numerador y denominador, y esa velocidad es la que decide el valor real del límite.

> [!warning] ⚠️ Por qué $\frac{0}{0}$ no tiene un valor fijo
>
> - $\lim_{x \to 0} \frac{x}{x} = 1$, aunque numerador y denominador tienden a $0$.
> - $\lim_{x \to 0} \frac{2x}{x} = 2$, con exactamente la misma forma.
> - $\lim_{x \to 0} \frac{x^2}{x} = 0$, otra vez $\frac{0}{0}$.
>
> **Por qué importa:** la misma forma admite cualquier resultado, por eso se llama *indeterminada*. No puedes "cancelar el cero" a ciegas: primero hay que transformar la expresión y solo después sustituir.

> [!tip] 💡 Las tres vías de salida que estudiamos aquí
>
> 1. **Técnicas algebraicas** (factorización, racionalización y cancelación): reescriben la expresión hasta que la sustitución directa vuelve a funcionar.
> 2. **Teorema del emparedado**: acota la función entre otras dos cuyo límite sí se conoce.
> 3. **Regla de L'Hôpital**: sustituye numerador y denominador por sus derivadas, siempre que se cumplan sus condiciones.
>
> **Orden de ataque:** primero las técnicas algebraicas, que son las que más se usan en el parcial; después el emparedado si la función está acotada; y en última instancia L'Hôpital, que exige derivar y verificar condiciones.

---

## 📋 Definiciones Formales

> [!info] 📚 Definición de forma indeterminada $\frac{0}{0}$
>
> Decimos que $\lim_{x \to a} \frac{f(x)}{g(x)}$ tiene la **forma indeterminada** $\frac{0}{0}$ cuando $$\lim_{x \to a} f(x) = 0 \quad \text{y} \quad \lim_{x \to a} g(x) = 0$$
>
> En ese caso el teorema del cociente no se puede aplicar porque daría $\frac{0}{0}$, que no está definido. El límite puede valer cualquier cosa (o no existir), así que hay que transformar la expresión antes de sustituir.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Formas_Indeterminadas_01.svg]]
>
> **Se lee así:** El diagrama sigue la ruta de un límite de cociente: primero se intenta la **sustitución directa** y un primer rombo decide si el resultado sigue siendo un cociente bien definido, en cuyo caso se aplica el teorema del cociente. Si en cambio aparece 0 sobre 0, un rombo lo declara **forma indeterminada** y abre tres ramas paralelas: factorización, racionalización y cancelación.
>
> **Por qué importa:** Fíjate en que el orden importa: primero se sustituye y solo si sale 0/0 se cambian de herramienta. Saltarte esa verificación es la causa más común de errores en exámenes.
>
> **Ejemplo:** En $\lim_{x \to 2} \frac{x^2-4}{x-2}$ la sustitución da $\frac{0}{0}$, así que tomas la rama de factorización, cancelas $x-2$, evalúas $x+2$ y el límite es $4$.

> [!warning] 🥪 Definición del teorema del emparedado
>
> Sean $f(x)$, $g(x)$ y $h(x)$ tres funciones tales que:
>
> 1. $f(x) \leq g(x) \leq h(x)$ para todo $x$ en una vecindad de $a$ (excepto posiblemente en $a$),
> 2. $\lim_{x \to a} f(x) = \lim_{x \to a} h(x) = L$,
>
> **entonces** $\lim_{x \to a} g(x) = L$.
>
> **Intuición:** si una función está "emparedada" entre otras dos que tienden al mismo límite, ella también debe tender a ese límite, porque no tiene dónde esconderse.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Formas_Indeterminadas_04.svg]]
>
> **Se lee así:** El diagrama muestra tres rectángulos apilados en orden vertical: la **función superior**, la función emparedada en el medio y la **función inferior**, con flechas que bajan de una a otra para mostrar el orden de la desigualdad. A un lado, un rectángulo aparte con el **límite común L** se conecta con otro rectángulo que afirma que todas convergen a ese valor, de modo que la banda queda atrapada entre dos extremos que comparten destino.
>
> **Por qué importa:** Te da la intuición del teorema: si aprieto una función entre dos que van al mismo sitio, ella también va. Entender esto evita usar el teorema con cotas que no coinciden.
>
> **Ejemplo:** Para $\lim_{x \to 0} x^2 \sin(1/x)$ acotas la función entre $-x^2$ y $x^2$, que comparten el límite $0$, y concluyes que el límite buscado es $0$.

> [!tip] 🧭 Cómo ejecutar el emparedado paso a paso
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Formas_Indeterminadas_05.svg]]
>
> **Se lee así:** una caja inicial con el límite difícil pasa a un rombo que pregunta si la función está acotada: si la respuesta es no, toca buscar otra técnica; si es sí, se buscan cotas $f(x) \le g(x) \le h(x)$ y un segundo rombo pregunta si las cotas comparten límite; si no, se buscan mejores cotas y se vuelve atrás; si sí, se aplica el teorema y el límite de $g$ vale $L$.
>
> **Por qué importa:** el bucle "cotas que no coinciden → mejores cotas" es el corazón del método: sin cotas con límite común el emparedado no dice nada. Y cuando el acotado falla, ahí termina tu camino.
>
> **Ejemplo:** para $\lim_{x\to0} x^2 \sin(1/x)$ la función acotada es $\sin(1/x)$ con $-1 \le \sin(1/x) \le 1$; las cotas $\pm x^2$ comparten límite $0$ y el bucle no hace falta darlo.

> [!info] 📚 Definición de la regla de L'Hôpital
>
> Si $\lim_{x \to a} \frac{f(x)}{g(x)}$ es una forma indeterminada $\frac{0}{0}$ o $\frac{\infty}{\infty}$, y se cumplen las condiciones de la regla, entonces $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
>
> siempre que el límite de la derecha exista (finito o infinito). Es decir: podemos reemplazar las funciones por sus derivadas y el límite se mantiene.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Formas_Indeterminadas_06.svg]]
>
> **Se lee así:** El diagrama arranca con un límite en forma indeterminada y pasa por un rombo de **verificación de condiciones**. Si no se cumplen, la salida es usar otras técnicas; si se cumplen, se deriva numerador y denominador y se evalúa el límite de las derivadas, con un rombo que pregunta si el resultado ya quedó determinado. Si sí, se llega al resultado final; si no, sale un rectángulo de aplicar L'Hôpital otra vez.
>
> **Por qué importa:** El error típico es derivar sin verificar la forma, así que el rombo de condiciones es lo que te protege. Además te muestra que se puede repetir la regla mientras siga saliendo una indeterminación.
>
> **Ejemplo:** En $\lim_{x \to 0} \frac{1 - \cos x - x^2/2}{x^4}$ aplicas L'Hôpital cuatro veces seguidas, porque en cada paso sigue apareciendo $\frac{0}{0}$, y llegas a $-\frac{1}{24}$.

> [!tip] 🗺️ El árbol de ataque a cualquier forma indeterminada
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Formas_Indeterminadas_07.svg]]
>
> **Se lee así:** un rombo con "Forma indeterminada" pregunta el tipo y abre cuatro ramas: $0/0$ o $\infty/\infty$ mandan a aplicar L'Hôpital directamente; $0 \cdot \infty$ manda a transformar la expresión a cociente; $\infty - \infty$ manda a buscar denominador común; $0^0$, $1^\infty$ e $\infty^0$ mandan a usar logaritmos. Las ramas confluyen: denominador común y logaritmos llevan a un cociente $0/0$ o $\infty/\infty$, desde el que se aplica L'Hôpital y se evalúa el límite.
>
> **Por qué importa:** te dice que ninguna forma es terminal: todas se reducen a un cociente, y de ahí al teorema o a una técnica algebraica. Tener el árbol en la cabeza evita memorizar recetas sueltas.
>
> **Ejemplo:** $\lim_{x \to 0^+} x \ln x$ es del tipo $0 \cdot \infty$: lo pasas a $\frac{\ln x}{1/x}$ ($\infty/\infty$) y aplicas L'Hôpital, llegando a $0$.

---

## 🔢 Técnicas Algebraicas para el $\frac{0}{0}$

> [!success] 🎯 Estrategia de factorización
>
> **Objetivo:** factorizar numerador y denominador para **cancelar los factores comunes** que causan la indeterminación.
>
> **Proceso:**
>
> 1. Factorizar completamente el numerador.
> 2. Factorizar completamente el denominador.
> 3. Cancelar los factores comunes.
> 4. Evaluar el límite resultante por sustitución directa.

> [!tip] 🔧 Métodos de factorización
>
> **Patrones que conviene tener a mano:**
>
> - Diferencia de cuadrados: $a^2 - b^2 = (a+b)(a-b)$
> - Trinomio cuadrado perfecto: $a^2 + 2ab + b^2 = (a+b)^2$ y $a^2 - 2ab + b^2 = (a-b)^2$
> - Factor común: $ax + bx = x(a + b)$
> - Trinomio de segundo grado: $ax^2 + bx + c = (px + q)(rx + s)$
>
> |Tipo de factorización|Patrón|Ejemplo|Factorizado|
> |---|---|---|---|
> |Diferencia de cuadrados|$a^2 - b^2$|$x^2 - 4$|$(x+2)(x-2)$|
> |Cuadrado perfecto|$(a \pm b)^2$|$x^2 + 6x + 9$|$(x+3)^2$|
> |Factor común|$x(a + b)$|$3x^2 + 6x$|$3x(x+2)$|
> |Trinomio general|$ax^2 + bx + c$|$2x^2 + 7x + 3$|$(2x+1)(x+3)$|
> |Diferencia de cubos|$a^3 - b^3$|$x^3 - 8$|$(x-2)(x^2+2x+4)$|

> [!example] 📝 Ejemplos de factorización
>
> **Ejemplo 1: diferencia de cuadrados** $$\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$$
>
> - Verificar: $\frac{2^2 - 4}{2 - 2} = \frac{0}{0}$, así que sí es indeterminada.
> - Factorizar: $x^2 - 4 = (x+2)(x-2)$.
> - Simplificar: $\frac{(x+2)(x-2)}{x-2} = x+2$ para $x \neq 2$.
> - Evaluar: $\lim_{x \to 2} (x+2) = 4$.
>
> **Ejemplo 2: trinomio cuadrático** $$\lim_{x \to -1} \frac{x^2 + 3x + 2}{x^2 - 1}$$
>
> - Verificar: $\frac{1 - 3 + 2}{1 - 1} = \frac{0}{0}$.
> - Numerador: $x^2 + 3x + 2 = (x+1)(x+2)$.
> - Denominador: $x^2 - 1 = (x+1)(x-1)$.
> - Simplificar: $\frac{(x+1)(x+2)}{(x+1)(x-1)} = \frac{x+2}{x-1}$ para $x \neq -1$.
> - Evaluar: $\lim_{x \to -1} \frac{x+2}{x-1} = \frac{1}{-2} = -\frac{1}{2}$.

> [!tip] ⚡ Factorizaciones avanzadas
>
> **Suma y diferencia de cubos:**
>
> - $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$
> - $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$
>
> **Factorización por agrupación:**
>
> - $ax + ay + bx + by = a(x+y) + b(x+y) = (a+b)(x+y)$
>
> **Sustitución trigonométrica:** cuando aparezcan identidades como $\sin^2 x + \cos^2 x = 1$, úsalas para reescribir la expresión antes de buscar factores comunes.

> [!example] 🎯 Ejemplo avanzado con diferencia de cubos $$\lim_{x \to 2} \frac{x^3 - 8}{x^2 - 4}$$
>
> - Verificar: $\frac{8 - 8}{4 - 4} = \frac{0}{0}$.
> - Numerador: $x^3 - 8 = (x-2)(x^2 + 2x + 4)$.
> - Denominador: $x^2 - 4 = (x-2)(x+2)$.
> - Simplificar: $\frac{(x-2)(x^2 + 2x + 4)}{(x-2)(x+2)} = \frac{x^2 + 2x + 4}{x+2}$ para $x \neq 2$.
> - Evaluar: $\lim_{x \to 2} \frac{4 + 4 + 4}{4} = \frac{12}{4} = 3$.

> [!success] 🔄 Estrategias de racionalización
>
> **Objetivo:** eliminar los **radicales** multiplicando por el **conjugado**. Si tenemos $\sqrt{a} + \sqrt{b}$, su conjugado es $\sqrt{a} - \sqrt{b}$, y la propiedad clave es $(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = a - b$.
>
> **1. Racionalización simple:** $$\frac{1}{\sqrt{a}} \cdot \frac{\sqrt{a}}{\sqrt{a}} = \frac{\sqrt{a}}{a}$$
>
> **2. Racionalización con conjugado:** $$\frac{1}{\sqrt{a} + \sqrt{b}} \cdot \frac{\sqrt{a} - \sqrt{b}}{\sqrt{a} - \sqrt{b}} = \frac{\sqrt{a} - \sqrt{b}}{a - b}$$
>
> **3. Racionalización del numerador:** $$\frac{\sqrt{a} - \sqrt{b}}{c} \cdot \frac{\sqrt{a} + \sqrt{b}}{\sqrt{a} + \sqrt{b}} = \frac{a - b}{c(\sqrt{a} + \sqrt{b})}$$
>
> |Situación|Multiplicar por|Resultado|Uso típico|
> |---|---|---|---|
> |$\frac{A}{\sqrt{x}}$|$\frac{\sqrt{x}}{\sqrt{x}}$|$\frac{A\sqrt{x}}{x}$|Denominador con una raíz|
> |$\frac{A}{\sqrt{x} + \sqrt{y}}$|$\frac{\sqrt{x} - \sqrt{y}}{\sqrt{x} - \sqrt{y}}$|$\frac{A(\sqrt{x} - \sqrt{y})}{x - y}$|Suma de raíces en denominador|
> |$\frac{\sqrt{x} - \sqrt{y}}{A}$|$\frac{\sqrt{x} + \sqrt{y}}{\sqrt{x} + \sqrt{y}}$|$\frac{x - y}{A(\sqrt{x} + \sqrt{y})}$|Resta de raíces en numerador|

> [!example] 📊 Ejemplos de racionalización
>
> **Ejemplo 1: racionalización básica** $$\lim_{x \to 0} \frac{\sqrt{x + 1} - 1}{x}$$
>
> - Verificar: $\frac{\sqrt{1} - 1}{0} = \frac{0}{0}$.
> - Multiplicar por el conjugado: $\frac{\sqrt{x + 1} - 1}{x} \cdot \frac{\sqrt{x + 1} + 1}{\sqrt{x + 1} + 1}$.
> - Diferencia de cuadrados: $\frac{(x + 1) - 1}{x(\sqrt{x + 1} + 1)} = \frac{x}{x(\sqrt{x + 1} + 1)}$.
> - Simplificar: $\frac{1}{\sqrt{x + 1} + 1}$ para $x \neq 0$.
> - Evaluar: $\lim_{x \to 0} \frac{1}{\sqrt{1} + 1} = \frac{1}{2}$.
>
> **Ejemplo 2: racionalización compleja** $$\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$$
>
> - Verificar: $\frac{2 - 2}{4 - 4} = \frac{0}{0}$.
> - Multiplicar por el conjugado: $\frac{\sqrt{x} - 2}{x - 4} \cdot \frac{\sqrt{x} + 2}{\sqrt{x} + 2}$.
> - Simplificar numerador: $\frac{x - 4}{(x - 4)(\sqrt{x} + 2)}$.
> - Cancelar: $\frac{1}{\sqrt{x} + 2}$ para $x \neq 4$.
> - Evaluar: $\lim_{x \to 4} \frac{1}{\sqrt{4} + 2} = \frac{1}{4}$.

> [!info] 🖼️ Patrones comunes en racionalización
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Formas_Indeterminadas_02.svg]]
>
> **Se lee así:** Parte de una forma 0/0 en la que hay radicales y llega a un rombo que pregunta **dónde está la raíz**. Si el radical está arriba, la rama pide multiplicar por el conjugado del numerador; si está abajo, por el conjugado del denominador. Las dos rutas se vuelven a juntar en un rectángulo de **diferencia de cuadrados** y de ahí a un último rectángulo donde se simplifica y se evalúa el límite.
>
> **Por qué importa:** Decide rápido cuál conjugado multiplicar, que es el paso donde más se equivoca la gente. Te evita cancelar el factor equivocado y perder el término que da el resultado.
>
> **Ejemplo:** En $\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$ el radical está en el numerador, así que multiplicas por $(\sqrt{x} + 2)$ y el límite queda $\frac{1}{4}$.

> [!tip] 🎯 Identificación rápida de cuándo racionalizar
>
> **¿Cuándo racionalizar?**
>
> - Hay raíces cuadradas en numerador o denominador.
> - La sustitución directa da $\frac{0}{0}$.
> - Se pueden formar conjugados útiles.
>
> **¿Qué conjugado usar?**
>
> - Para $\sqrt{a} + b$ usar $\sqrt{a} - b$.
> - Para $\sqrt{a} - \sqrt{b}$ usar $\sqrt{a} + \sqrt{b}$.
> - Para $a + \sqrt{b}$ usar $a - \sqrt{b}$.

> [!success] ✂️ Proceso de cancelación
>
> **Objetivo:** eliminar los **factores que causan la indeterminación** mediante cancelación algebraica.
>
> **Pasos fundamentales:**
>
> 1. **Identificar** el factor problemático.
> 2. **Factorizar** tanto numerador como denominador.
> 3. **Cancelar** los factores comunes.
> 4. **Evaluar** el límite simplificado.

> [!tip] ⚡ Métodos de cancelación
>
> **1. Cancelación directa:** $$\frac{(x-a) \cdot P(x)}{(x-a) \cdot Q(x)} = \frac{P(x)}{Q(x)} \quad (x \neq a)$$
>
> **2. Cancelación múltiple:** $$\frac{(x-a)^2 \cdot P(x)}{(x-a) \cdot Q(x)} = \frac{(x-a) \cdot P(x)}{Q(x)} \quad (x \neq a)$$
>
> **3. Cancelación con factorización previa:** $$\frac{f(x)}{g(x)} \to \frac{A(x)(x-a)}{B(x)(x-a)} = \frac{A(x)}{B(x)}$$
>
> |Situación|Antes de cancelar|Después de cancelar|Factor cancelado|
> |---|---|---|---|
> |Factor lineal|$\frac{(x-2)(x+1)}{(x-2)(x+3)}$|$\frac{x+1}{x+3}$|$(x-2)$|
> |Factor cuadrático|$\frac{(x^2-1)(x+2)}{(x^2-1)(x-3)}$|$\frac{x+2}{x-3}$|$(x^2-1)$|
> |Múltiples factores|$\frac{(x-1)^2(x+2)}{(x-1)(x+5)}$|$\frac{(x-1)(x+2)}{x+5}$|$(x-1)$|
> |Con constantes|$\frac{2(x-3)(x+1)}{4(x-3)}$|$\frac{x+1}{2}$|$2(x-3)$|

> [!example] 🎨 Ejemplos de cancelación
>
> **Ejemplo 1: cancelación simple** $$\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$$
>
> - Verificar: $\frac{9 - 9}{3 - 3} = \frac{0}{0}$.
> - Factorizar: $\frac{(x+3)(x-3)}{x-3}$.
> - Cancelar: queda $x+3$ para $x \neq 3$.
> - Evaluar: $\lim_{x \to 3} (x+3) = 6$.
>
> **Ejemplo 2: cancelación múltiple** $$\lim_{x \to -2} \frac{x^3 + 8}{x^2 + 4x + 4}$$
>
> - Verificar: $\frac{-8 + 8}{4 - 8 + 4} = \frac{0}{0}$.
> - Numerador: $x^3 + 8 = (x+2)(x^2 - 2x + 4)$.
> - Denominador: $x^2 + 4x + 4 = (x+2)^2$.
> - Cancelar: $\frac{x^2 - 2x + 4}{x+2}$ para $x \neq -2$.
> - Evaluar: el numerador tiende a $12$ y el denominador a $0$, así que el límite no existe (la función se va a infinito).

> [!warning] ⚠️ Cuidados en la cancelación
>
> **1. Verificar la indeterminación:** confirma siempre que la sustitución da $\frac{0}{0}$ antes de cancelar.
>
> **2. Restricción de dominio:** recuerda que $x \neq a$ después de la cancelación; el límite estudia el comportamiento *cerca* de $a$, no en $a$.
>
> **3. Cancelación completa:** si queda un factor $(x-a)$ en el denominador, el límite será infinito.
>
> **4. Factorización correcta:** revisa cada factorización antes de cancelar; un factor mal factorizado arrastra todo el problema.

> [!example] 🔍 Ejemplo con múltiples técnicas $$\lim_{x \to 1} \frac{\sqrt{x+3} - 2}{x^2 - 1}$$
>
> - Verificar: $\frac{\sqrt{4} - 2}{1 - 1} = \frac{0}{0}$.
> - **Racionalizar el numerador:** multiplicar por $\frac{\sqrt{x+3} + 2}{\sqrt{x+3} + 2}$; el numerador da $(\sqrt{x+3})^2 - 4 = x - 1$.
> - **Factorizar el denominador:** $x^2 - 1 = (x-1)(x+1)$.
> - **Cancelar:** $\frac{x-1}{(x-1)(x+1)(\sqrt{x+3} + 2)} = \frac{1}{(x+1)(\sqrt{x+3} + 2)}$.
> - **Evaluar:** $\lim_{x \to 1} \frac{1}{(2)(\sqrt{4} + 2)} = \frac{1}{2 \cdot 4} = \frac{1}{8}$.
>
> **Por qué importa:** aquí conviven racionalización, factorización y cancelación; el orden (primero quitar la raíz, después factorizar) es lo que hace que los pasos encajen.

> [!info] 🖼️ Diagrama de flujo completo del $\frac{0}{0}$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Formas_Indeterminadas_03.svg]]
>
> **Se lee así:** Es el diagrama de flujo completo de la unidad: empieza con un límite que puede dar 0/0, se sustituye y un rombo separa el caso normal de la forma indeterminada. Desde ahí el flujo se bifurca: primero pregunta si hay radicales y manda a racionalizar, luego pregunta si se puede factorizar y lleva a factorizar, cancelar factores comunes y evaluar el límite. Si no se puede factorizar, la salida es L'Hôpital o sustitución.
>
> **Por qué importa:** Es tu mapa de decisión para resolver cualquier 0/0 sin saltarte pasos ni probar técnicas al azar. Recórrelo de izquierda a derecha y siempre sabrás qué hacer y en qué orden.
>
> **Ejemplo:** En $\lim_{x \to 1} \frac{\sqrt{x+3} - 2}{x^2-1}$ el diagrama te lleva a racionalizar, luego factorizar el denominador, cancelar $x-1$ y llegar a $\frac{1}{8}$.

> [!tip] 🧠 Técnica de estudio "FRC"
>
> - **F**actorizar: buscar factores comunes.
> - **R**acionalizar: si hay radicales, multiplicar por el conjugado.
> - **C**ancelar: eliminar los factores problemáticos.
>
> **Algoritmo de decisión:**
>
> 1. Verificar si es la forma $\frac{0}{0}$.
> 2. ¿Hay radicales? → racionalizar primero.
> 3. ¿Se puede factorizar? → factorizar.
> 4. ¿Hay factores comunes? → cancelar.
> 5. Evaluar el límite simplificado.
>
> **Frase nemotécnica:** *"Factoriza, Racionaliza, Cancela"*.

> [!tip] 💪 Banco de prácticas: técnicas algebraicas
>
> **Nivel 1 - Factorización básica:**
>
> - $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$
> - $\lim_{x \to -2} \frac{x^2 + 4x + 4}{x + 2}$
> - $\lim_{x \to 1} \frac{x^3 - 1}{x^2 - 1}$
>
> **Nivel 2 - Racionalización simple:**
>
> - $\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$
> - $\lim_{x \to 9} \frac{\sqrt{x} - 3}{x - 9}$
> - $\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1}$
>
> **Nivel 3 - Técnicas combinadas:**
>
> - $\lim_{x \to 4} \frac{x^2 - 16}{\sqrt{x + 5} - 3}$
> - $\lim_{x \to 2} \frac{\sqrt{x + 7} - 3}{x^2 - 4}$
> - $\lim_{x \to 0} \frac{(1 + x)^2 - 1}{x}$
>
> **Nivel 4 - Casos complejos:**
>
> - $\lim_{x \to 1} \frac{x^4 - 1}{x^3 - 1}$
> - $\lim_{x \to 8} \frac{\sqrt[3]{x} - 2}{x - 8}$
> - $\lim_{x \to 0} \frac{\sqrt{1 + 2x} - \sqrt{1 - 2x}}{x}$

> [!tip] 📊 Patrones que conviene reconocer de un vistazo
>
> **1. Diferencia de cuadrados en el numerador:** $$\frac{x^2 - a^2}{x - a} = x + a$$
>
> **2. Radical menos constante:** $$\frac{\sqrt{x + c} - \sqrt{c}}{x} = \frac{1}{\sqrt{x + c} + \sqrt{c}}$$
>
> **3. Diferencia de cubos:** $$\frac{x^3 - a^3}{x - a} = x^2 + ax + a^2$$
>
> **4. Tras cancelar $(x-a)$, si en el denominador queda $(x-a)^2$:** el límite es infinito, no un valor finito.

> [!warning] 🚨 Errores comunes en las técnicas algebraicas
>
> **1. No verificar la forma indeterminada:** sustituye siempre primero para confirmar $\frac{0}{0}$.
>
> **2. Factorización incorrecta:** revisa cada paso de factorización antes de cancelar.
>
> **3. Cancelación prematura:** no canceles antes de factorizar completamente.
>
> **4. Olvidar las restricciones de dominio:** en la expresión simplificada sigue valiendo $x \neq a$.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$.
>
> > [!success]- ✅ Solución
> >
> > Sustitución directa: $\frac{9-9}{3-3} = \frac{0}{0}$, forma indeterminada.
> >
> > Factorizar: $x^2 - 9 = (x+3)(x-3)$, así que $\frac{(x+3)(x-3)}{x-3} = x+2$ para $x \neq 3$.
> >
> > Evaluar: $\lim_{x \to 3} (x+3) = 6$.
> >
> > **Respuesta:** el límite vale $6$.

> [!example] 📋 Planteamiento
>
> Resuelve $\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$.
>
> > [!success]- ✅ Solución
> >
> > Sustitución: $\frac{\sqrt{4}-2}{0} = \frac{0}{0}$.
> >
> > Multiplicar por el conjugado del numerador:
> >
> > $$\frac{\sqrt{x+4}-2}{x} \cdot \frac{\sqrt{x+4}+2}{\sqrt{x+4}+2} = \frac{(x+4)-4}{x(\sqrt{x+4}+2)} = \frac{x}{x(\sqrt{x+4}+2)}.$$
> >
> > Cancelar y evaluar: $\lim_{x \to 0} \frac{1}{\sqrt{x+4}+2} = \frac{1}{4}$.
> >
> > **Respuesta:** el límite vale $\frac{1}{4}$.

> [!example] 📋 Planteamiento
>
> Encuentra $\lim_{x \to -1} \frac{x^2 + 3x + 2}{x^2 - 1}$.
>
> > [!success]- ✅ Solución
> >
> > Sustitución: $\frac{1-3+2}{1-1} = \frac{0}{0}$.
> >
> > Factorizar: numerador $= (x+1)(x+2)$ y denominador $= (x+1)(x-1)$.
> >
> > Cancelar $(x+1)$: queda $\frac{x+2}{x-1}$ para $x \neq -1$.
> >
> > Evaluar: $\frac{-1+2}{-1-1} = -\frac{1}{2}$.
> >
> > **Respuesta:** el límite vale $-\frac{1}{2}$.

> [!example] 📋 Planteamiento
>
> Usa el teorema del emparedado para hallar $\lim_{x \to 0} x^2 \sin\!\left(\frac{1}{x}\right)$.
>
> > [!success]- ✅ Solución
> >
> > Como $-1 \leq \sin(1/x) \leq 1$ para todo $x \neq 0$, multiplicando por $x^2 \geq 0$:
> >
> > $$-x^2 \leq x^2 \sin(1/x) \leq x^2.$$
> >
> > Los extremos cumplen $\lim_{x \to 0} (-x^2) = \lim_{x \to 0} x^2 = 0$, así que por el teorema del emparedado el límite central también es $0$.
> >
> > **Respuesta:** el límite vale $0$, aunque $\sin(1/x)$ oscila sin límite cerca del origen.

> [!example] 📋 Planteamiento
>
> Aplica la regla de L'Hôpital para calcular $\lim_{x \to 0} \frac{1 - \cos x - x^2/2}{x^4}$.
>
> > [!success]- ✅ Solución
> >
> > Sustitución: $\frac{1-1-0}{0} = \frac{0}{0}$, así que se aplica L'Hôpital:
> >
> > 1. $\frac{\sin x - x}{4x^3}$ (sigue $\frac{0}{0}$).
> > 2. $\frac{\cos x - 1}{12x^2}$ (sigue $\frac{0}{0}$).
> > 3. $\frac{-\sin x}{24x}$ (sigue $\frac{0}{0}$).
> > 4. $\frac{-\cos x}{24} \to -\frac{1}{24}$.
> >
> > **Respuesta:** el límite vale $-\frac{1}{24}$: se necesitaron cuatro aplicaciones seguidas porque la indeterminación se heredaba en cada paso.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 0} \frac{\sin 3x}{\tan 5x}$ con la regla de L'Hôpital.
>
> > [!success]- ✅ Solución
> >
> > Sustitución: $\frac{0}{0}$, así que se deriva numerador y denominador:
> >
> > $$\lim_{x \to 0} \frac{\sin 3x}{\tan 5x} = \lim_{x \to 0} \frac{3\cos 3x}{5\sec^2 5x} = \frac{3 \cdot 1}{5 \cdot 1} = \frac{3}{5}.$$
> >
> > Comprobación con límites notables: $\frac{\sin 3x}{\tan 5x} = \frac{\sin 3x}{3x} \cdot \frac{5x}{\tan 5x} \cdot \frac{3}{5} \to 1 \cdot 1 \cdot \frac{3}{5}$.
> >
> > **Respuesta:** el límite vale $\frac{3}{5}$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Reconozco las siete formas indeterminadas y sé que $\frac{0}{0}$ no tiene valor fijo.
> - [ ] Aplico factorización, racionalización y cancelación para eliminar una indeterminación $\frac{0}{0}$.
> - [ ] Verifico siempre la forma antes de usar una técnica.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Enuncio y aplico el teorema del emparedado con cotas que comparten el mismo límite.
> - [ ] Aplico la regla de L'Hôpital a $\frac{0}{0}$ y $\frac{\infty}{\infty}$ verificando sus condiciones.
> - [ ] Repito L'Hôpital cuantas veces haga falta mientras persista la indeterminación.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Eligo entre técnica algebraica, emparedado y L'Hôpital según el tipo de función.
> - [ ] Resuelvo indeterminaciones $0 \cdot \infty$, $\infty - \infty$ y $0^0$ reescribiéndolas a una forma $\frac{0}{0}$ o $\frac{\infty}{\infty}$.
> - [ ] Detecto cuándo L'Hôpital no aplica y cambio de estrategia sin perder tiempo.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4 y 6: formas indeterminadas y regla de L'Hôpital.
> - R. Larson, *Cálculo* (Cengage), cap. 8: teorema del emparedado y límites notables.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 5: límites y la regla de L'Hôpital.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la definición de límite que aquí se aplica.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — las propiedades que sostienen cada manipulación.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — las derivadas que usa L'Hôpital.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es una forma indeterminada?::Una expresión como $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0\cdot\infty$, $\infty-\infty$, $0^0$, $1^\infty$ o $\infty^0$ que no tiene valor fijo: el resultado depende de cómo tienden numerador y denominador.
> - ¿Cuál es el enunciado del teorema del emparedado?::Si $f(x) \leq g(x) \leq h(x)$ cerca de $a$ y $\lim f = \lim h = L$, entonces $\lim g = L$ también.
> - ¿Cuándo se puede aplicar la regla de L'Hôpital?::Cuando la sustitución da $\frac{0}{0}$ o $\frac{\infty}{\infty}$ (tras reescribir si hace falta) y el límite de las derivadas existe.
> - ¿Cuál es el orden de ataque ante un $\frac{0}{0}$?::Primero técnicas algebraicas (factorizar, racionalizar, cancelar); después emparedado si la función está acotada; al final L'Hôpital.
> - ¿Por qué $\lim_{x \to 0} x^2\sin(1/x) = 0$?::Por emparedado: $-x^2 \leq x^2\sin(1/x) \leq x^2$ y ambos extremos tienden a $0$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la definición de límite que se usa en cada técnica.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — comprobar el límite por lados cuando la expresión no es continua.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — las formas $\frac{\infty}{\infty}$ y $\infty-\infty$ del infinito.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — las reglas que ejecuta L'Hôpital en cada paso.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — dónde se usan estos límites para hallar asíntotas.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/03 - Límites en Gráficas|03 - Límites en Gráficas]] — leer un límite directamente de su gráfica.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero el banco de técnicas algebraicas de la nota hasta que factorizar y racionalizar salgan sin pensarlo.
> - Después salta al emparedado: domina $x^2\sin(1/x)$ y $\frac{\sin x}{x}$ antes de seguir.
> - Cuando las tres vías estén claras, resuelve los seis ejercicios propuestos en orden: los tres primeros son algebraicos, el cuarto es emparedado y los dos últimos son L'Hôpital.
> - En cada ejercicio, escribe **qué forma indeterminada salió** y **por qué técnica elegiste** antes de calcular.

---

**Tags:** #MATG1045 #unidad2 #formas-indeterminadas #teorema-emparedado #lhopital #factorizacion #racionalizacion #cancelacion #limites

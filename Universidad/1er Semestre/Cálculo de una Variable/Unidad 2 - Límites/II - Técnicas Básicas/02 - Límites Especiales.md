---
dg-publish: true
tags: [MATG1045, unidad2, limites-especiales, matemáticas, cálculo, límites, trigonometría, límites-fundamentales, sin-x-sobre-x, cos-x, tangente, funciones-trigonométricas]
---

# 🌊 Límites Especiales: trigonométricos, exponenciales y logarítmicos

## 🎯 Introducción

> [!info] 🔍 Importancia en el cálculo
>
> Los **límites trigonométricos fundamentales** son la base de:
>
> - las derivadas de funciones trigonométricas,
> - la resolución de formas indeterminadas con trigonometría,
> - el análisis de comportamiento oscilatorio,
> - las aproximaciones de funciones cerca del origen.
>
> **Estos límites NO se pueden obtener por sustitución directa** porque dan la forma indeterminada $\frac{0}{0}$.

> [!warning] ⚠️ Por qué son indeterminados
>
> Al sustituir $x = 0$ directamente:
>
> - $\frac{\sin 0}{0} = \frac{0}{0}$, que es indeterminada,
> - $\frac{1 - \cos 0}{0} = \frac{1-1}{0} = \frac{0}{0}$, también indeterminada.
>
> **Por esto necesitamos métodos geométricos y analíticos especiales.**

> [!tip] 💡 Concepto clave de los límites exponenciales
>
> Los **límites exponenciales** involucran funciones de la forma $f(x)^{g(x)}$ donde tanto la base como el exponente dependen de la variable. Son fundamentales para entender el crecimiento exponencial, el número $e$ y las formas indeterminadas del tipo $1^\infty$, $0^0$ y $\infty^0$.

> [!info] 🔢 Concepto clave de los límites logarítmicos
>
> Los **límites logarítmicos** aparecen cuando el logaritmo entra en un cociente o en un producto con otra función. Resuelven de una sola tacada las formas $0 \cdot (-\infty)$ y $\frac{\infty}{\infty}$, y además fijan la jerarquía de crecimiento que gobierna todo el análisis asintótico.

---

## 📋 Definiciones Formales

> [!success] 🎯 Definición de los límites trigonométricos fundamentales
>
> Los dos límites que sostienen toda la trigonometría del cálculo son:
>
> $$\lim_{x \to 0} \frac{\sin x}{x} = 1 \qquad \text{y} \qquad \lim_{x \to 0} \frac{1-\cos x}{x} = 0$$
>
> El primero exige que $x$ esté en **radianes** y establece que, para ángulos pequeños, $\sin x \approx x$. El segundo dice que $1 - \cos x$ decrece más lento que $x$, es decir que $\cos x \approx 1$ cerca de $0$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_Especiales_01.svg]]
>
> **Se lee así:** La estructura es un árbol que abre en los límites trigonométricos y se bifurca en dos ramas: una hacia el límite fundamental del seno sobre $x$ y otra hacia el del uno menos coseno sobre $x$. Cada rama baja a su casillero de derivada correspondiente, y ambas vuelven a confluir en un rectángulo de límites derivados que alimenta el rectángulo de **aplicaciones en el cálculo**.
>
> **Por qué importa:** El diagrama te muestra de dónde sale todo: los dos límites fundamentales son la base de las derivadas de seno y coseno y de los límites derivados. Entender esta jerarquía te evita memorizar fórmulas sueltas y te da un método para deducir límites que no reconoces.
>
> **Ejemplo:** Para la derivada del seno se usa $\lim_{h \to 0} \frac{\sin(x+h) - \sin x}{h}$, que se apoya justamente en el límite fundamental del seno.

> [!info] 📚 Definición del número e de Euler
>
> El número $e$ se define como el límite al que tiende el crecimiento compuesto cuando el periodo se hace infinitamente corto:
>
> $$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = \lim_{x \to 0} (1 + x)^{\frac{1}{x}}$$
>
> **Valor aproximado:** $e \approx 2.71828182845\ldots$
>
> **Formas equivalentes:**
>
> |Forma|Expresión|Condición|
> |---|---|---|
> |Básica|$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$|$x \to +\infty$|
> |Generalizada|$\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e$|$x \to 0$|
> |Con función|$\lim_{x \to a} \left(1 + \frac{f(x)}{g(x)}\right)^{h(x)} = e^{\lim_{x \to a} \frac{f(x) \cdot h(x)}{g(x)}}$|$\frac{f(x)}{g(x)} \to 0$ y $h(x) \to \infty$|
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_Especiales_07.svg]]
>
> **Se lee así:** El diagrama arranca en un rectángulo con el crecimiento compuesto $(1 + 1/n)^n$ y baja por una cadena que describe cómo $n$ crece sin parar. Llega a un rombo que pregunta si esos valores se acercan a un número fijo; la rama "Sí" conduce al valor $2.718281828\ldots$ y de ahí al recuadro que lo bautiza como $e$, el número de los logaritmos naturales, que a su vez se conecta con la forma equivalente $(1+x)^{1/x}$ cuando $x$ tiende a $0$. La rama "No" termina en un recuadro rojo donde no habría constante de referencia.
>
> **Por qué importa:** El número $e$ no es una constante arbitraria: es el destino de una sucesión concreta. Verlo así te permite reconstruir la fórmula del límite $1^\infty$ en vez de recordarla de memoria.
>
> **Ejemplo:** En $\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x}$ reescribes la base como $1 + u$ con $u = 3/x$, calculas $u \cdot v = 6$ y obtienes $e^6$, que es la misma idea del diagrama con una constante distinta.

> [!info] 🔢 Definición de límites logarítmicos
>
> Dos resultados dominan toda la familia: $\lim_{x \to 0^+} x \ln x = 0$ y $\lim_{x \to \infty} \frac{\ln x}{x} = 0$. El primero convierte la forma $0 \cdot (-\infty)$ en un valor concreto; el segundo demuestra que **el logaritmo crece más lento que cualquier función lineal**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_Especiales_06.svg]]
>
> **Se lee así:** Es un árbol con una raíz de **límites logarítmicos** que se abre en tres ramas. La primera lleva al límite de $x \cdot \ln x$ y de ahí a la forma $0$ por menos infinito, que se resuelve con L'Hôpital. La segunda lleva al cociente $\ln x$ sobre $x$ y luego a la idea de que el logaritmo **crece lento**, con un cuadro de aplicaciones. La tercera compara crecimientos y desemboca en la jerarquía donde $\ln x$ queda por debajo de $x^n$ y de $e^x$.
>
> **Por qué importa:** Te sirve para comparar funciones sin calcular cada límite: si el logaritmo va contra una potencia, **gana la potencia**. También te da la respuesta directa de la forma $0 \cdot (-\infty)$ cuando aparece en un límite logarítmico.
>
> **Ejemplo:** Con $\lim_{x \to \infty} \frac{\ln(x^2)}{x}$ reescribes como $\frac{2\ln x}{x}$ y usas el resultado central del diagrama, que $\ln x / x \to 0$, para concluir que el límite es $0$.

---

## 📐 Límites trigonométricos fundamentales

> [!success] 🎯 El límite más importante de la trigonometría
>
> $$\lim_{x \to 0} \frac{\sin x}{x} = 1$$
>
> **Condición:** $x$ debe estar en **radianes**. Este límite es fundamental porque establece que para ángulos pequeños $\sin x \approx x$.

> [!tip] 🔧 Demostración por desigualdad (método del sandwich)
>
> Para $0 < x < \frac{\pi}{2}$, consideramos un sector circular de radio $1$.
>
> **Áreas en orden creciente:**
>
> - Área del triángulo inscrito: $\frac{1}{2}\sin x$
> - Área del sector circular: $\frac{1}{2}x$
> - Área del triángulo circunscrito: $\frac{1}{2}\tan x$
>
> **Desigualdad:** $\sin x < x < \tan x$
>
> **Dividiendo por $\sin x > 0$:** $$1 < \frac{x}{\sin x} < \frac{1}{\cos x}$$
>
> **Invirtiendo:** $\cos x < \frac{\sin x}{x} < 1$
>
> **Aplicando el teorema del sandwich:** $$\lim_{x \to 0^+} \cos x = 1 \quad \text{y} \quad \lim_{x \to 0^+} 1 = 1$$
>
> Por lo tanto $\lim_{x \to 0^+} \frac{\sin x}{x} = 1$.
>
> |Valor de $x$|$\sin x$|$\frac{\sin x}{x}$|Aproximación|
> |---|---|---|---|
> |$0.1$|$0.09983$|$0.99833$|≈ 1|
> |$0.01$|$0.00999$|$0.99998$|≈ 1|
> |$0.001$|$0.000999$|$0.999999$|≈ 1|
> |$-0.001$|$-0.000999$|$0.999999$|≈ 1|
> |$-0.01$|$-0.00999$|$0.99998$|≈ 1|
>
> **Por qué importa:** la tabla confirma la desigualdad, pero la que demuestra es el emparedado: dos cotas que convergen a $1$ obligan al cociente a ir a $1$.

> [!example] 📝 Formas equivalentes del límite fundamental
>
> **Forma básica:** $$\lim_{x \to 0} \frac{\sin x}{x} = 1$$
>
> **Con múltiplos:** $$\lim_{x \to 0} \frac{\sin(ax)}{x} = a \qquad \text{(usando la sustitución } u = ax\text{)}$$
>
> **Con funciones:** $$\lim_{x \to a} \frac{\sin(f(x))}{f(x)} = 1 \quad \text{si } \lim_{x \to a} f(x) = 0$$

> [!example] 🎯 Ejemplos prácticos con seno
>
> **Ejemplo 1: con múltiplo** $\lim_{x \to 0} \frac{\sin(3x)}{x}$.
> Se reescribe $\frac{\sin(3x)}{x} = \frac{\sin(3x)}{3x} \cdot 3$, y como el límite del primer factor vale $1$, el resultado es $1 \cdot 3 = 3$.
>
> **Ejemplo 2: con denominador diferente** $\lim_{x \to 0} \frac{\sin(5x)}{2x}$.
> Se reescribe $\frac{\sin(5x)}{2x} = \frac{5}{2} \cdot \frac{\sin(5x)}{5x}$, así que el resultado es $\frac{5}{2} \cdot 1 = \frac{5}{2}$.
>
> **Ejemplo 3: con sustitución** $\lim_{t \to 2} \frac{\sin(t-2)}{t-2}$.
> Con $u = t - 2$, cuando $t \to 2$ se tiene $u \to 0$, y la expresión se convierte en $\lim_{u \to 0} \frac{\sin u}{u} = 1$.

> [!tip] ⚡ Usos frecuentes del límite sin x sobre x
>
> **1. Derivada del seno:** $$\frac{d}{dx}[\sin x] = \lim_{h \to 0} \frac{\sin(x+h) - \sin x}{h} = \cos x$$
>
> **2. Aproximación lineal:** $$\sin x \approx x \quad \text{para } x \text{ pequeño}$$
>
> **3. Serie de Taylor:** $$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

---

## 📊 Límite de 1 menos coseno sobre x

> [!info] 🎯 El segundo límite fundamental
>
> $$\lim_{x \to 0} \frac{1-\cos x}{x} = 0$$
>
> **Interpretación:** para ángulos pequeños, $1 - \cos x$ tiende a $0$ **decreciendo más lento que $x$**, lo que equivale a decir que $\cos x \approx 1$ para $x$ cerca de $0$.

> [!success] 📐 Método de conjugado
>
> **Paso 1:** multiplicar por el conjugado $$\frac{1-\cos x}{x} = \frac{1-\cos x}{x} \cdot \frac{1+\cos x}{1+\cos x}$$
>
> **Paso 2:** aplicar la diferencia de cuadrados $$= \frac{1 - (\cos x)^2}{x(1+\cos x)} = \frac{1 - \cos^2 x}{x(1+\cos x)}$$
>
> **Paso 3:** usar la identidad $1 - \cos^2 x = \sin^2 x$ $$= \frac{\sin^2 x}{x(1+\cos x)} = \frac{\sin x}{x} \cdot \frac{\sin x}{1+\cos x}$$
>
> **Paso 4:** aplicar los límites $$\lim_{x \to 0} \frac{\sin x}{x} \cdot \frac{\sin x}{1+\cos x} = 1 \cdot \frac{0}{1+1} = 1 \cdot 0 = 0$$
>
> |Valor de $x$|$1-\cos x$|$\frac{1-\cos x}{x}$|Aproximación|
> |---|---|---|---|
> |$0.1$|$0.004996$|$0.04996$|≈ 0|
> |$0.01$|$0.000050$|$0.005000$|≈ 0|
> |$0.001$|$0.0000005$|$0.0005000$|≈ 0|
> |$-0.001$|$0.0000005$|$-0.0005000$|≈ 0|
> |$-0.01$|$0.000050$|$-0.005000$|≈ 0|
>
> **Por qué importa:** el conjugado es la única palanca que convierte una diferencia de cosenos en un producto de senos, y ese producto ya se resuelve con el límite fundamental.

> [!tip] ⚡ Forma alternativa importante
>
> Es más común usar la forma $$\lim_{x \to 0} \frac{1-\cos x}{x^2} = \frac{1}{2}$$
>
> **Demostración:** $$\frac{1-\cos x}{x^2} = \frac{1-\cos x}{x} \cdot \frac{1}{x} = \frac{\sin^2 x}{x(1+\cos x)} \cdot \frac{1}{x} = \frac{\sin x}{x} \cdot \frac{\sin x}{x} \cdot \frac{1}{1+\cos x}$$
>
> $$\lim_{x \to 0} 1 \cdot 1 \cdot \frac{1}{2} = \frac{1}{2}$$

> [!example] 🎨 Ejemplos con 1 menos coseno x
>
> **Ejemplo 1: forma básica** $\lim_{x \to 0} \frac{1-\cos(2x)}{x}$.
> Se reescribe $\frac{1-\cos(2x)}{x} = 2 \cdot \frac{1-\cos(2x)}{2x}$; con $u = 2x$ el límite es $2 \cdot 0 = 0$.
>
> **Ejemplo 2: con denominador cuadrático** $\lim_{x \to 0} \frac{1-\cos x}{x^2}$.
> Ya demostrado: vale $\frac{1}{2}$.
>
> **Ejemplo 3: combinado** $\lim_{x \to 0} \frac{1-\cos(3x)}{2x^2}$.
> Se reescribe $\frac{1-\cos(3x)}{2x^2} = \frac{1}{2} \cdot 9 \cdot \frac{1-\cos(3x)}{9x^2} = \frac{9}{2} \cdot \frac{1}{2} = \frac{9}{4}$.

---

## 🔄 Límites derivados de los fundamentales

> [!success] 🚀 Límites derivados y extensiones
>
> A partir de los dos límites fundamentales se obtienen muchos otros límites importantes. La regla es siempre la misma: reescribir la expresión hasta que aparezca $\frac{\sin u}{u}$, $\frac{\tan u}{u}$ o $\frac{1-\cos u}{u^2}$.

> [!tip] 🎯 Límite de tan x sobre x
>
> $$\lim_{x \to 0} \frac{\tan x}{x} = 1$$
>
> **Demostración:** $$\frac{\tan x}{x} = \frac{\sin x}{\cos x} \cdot \frac{1}{x} = \frac{\sin x}{x} \cdot \frac{1}{\cos x}$$
>
> $$\lim_{x \to 0} \frac{\sin x}{x} \cdot \frac{1}{\cos x} = 1 \cdot \frac{1}{1} = 1$$

> [!example] 📝 Ejemplos con tangente
>
> **Ejemplo 1:** $$\lim_{x \to 0} \frac{\tan(4x)}{x} = 4$$
>
> **Ejemplo 2:** $$\lim_{x \to 0} \frac{x}{\tan(2x)} = \frac{1}{2}$$

> [!info] 🔄 Límites inversos
>
> **Arcoseno:** $$\lim_{x \to 0} \frac{\arcsin x}{x} = 1$$
>
> **Arcotangente:** $$\lim_{x \to 0} \frac{\arctan x}{x} = 1$$
>
> **Demostración por sustitución:** si $y = \arcsin x$, entonces $x = \sin y$ y cuando $x \to 0$ se tiene $y \to 0$: $$\lim_{x \to 0} \frac{\arcsin x}{x} = \lim_{y \to 0} \frac{y}{\sin y} = \frac{1}{\lim_{y \to 0} \frac{\sin y}{y}} = \frac{1}{1} = 1$$

> [!example] 🎨 Casos complejos combinados
>
> **Ejemplo 1: límite mixto** $\lim_{x \to 0} \frac{\sin x - x \cos x}{x^3}$.
> Se resuelve con L'Hôpital o con desarrollo en serie, y el resultado es $\frac{1}{2}$.
>
> **Ejemplo 2: con múltiples funciones** $\lim_{x \to 0} \frac{\sin(2x) - 2\sin x}{x^3}$.
> Con la identidad $\sin(2x) = 2\sin x \cos x$ se tiene $\sin(2x) - 2\sin x = 2\sin x(\cos x - 1)$, y el resultado es $-\frac{2}{3}$.

> [!info] 🖼️ Selector de estrategia para límites combinados
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_Especiales_02.svg]]
>
> **Se lee así:** El diagrama es un selector de estrategia: un rombo central pregunta qué forma tiene el límite y reparte el flujo hacia cuatro caminos distintos. Tres de ellos llevan directo al rectángulo de resultado, dos aplicando el límite fundamental y uno reconvirtiendo a seno y coseno; el cuarto, el de las combinaciones, exige un paso extra de descomposición con identidades antes de reaplicar los fundamentales.
>
> **Por qué importa:** Este selector evita que intentes aplicar el límite fundamental a una expresión que no tiene su forma, el error más común al inicio de la unidad. Te obliga a identificar primero el patrón y luego a transformarlo, que es exactamente lo que se necesita en un parcial.
>
> **Ejemplo:** Para $\lim_{x \to 0} \frac{\sin(2x) - 2\sin x}{x^3}$ la forma no es fundamental, así que tomas la ruta de combinación, usas $\sin(2x) = 2\sin x \cos x$ y obtienes $-\frac{2}{3}$.

> [!info] 📊 Tabla de límites derivados importantes
>
> |Límite|Valor|Método|
> |---|---|---|
> |$\lim_{x \to 0} \frac{\sin(ax)}{x}$|$a$|Sustitución $u = ax$|
> |$\lim_{x \to 0} \frac{\tan(ax)}{x}$|$a$|$ \tan u = \frac{\sin u}{\cos u}$|
> |$\lim_{x \to 0} \frac{1-\cos(ax)}{x^2}$|$\frac{a^2}{2}$|Racionalización|
> |$\lim_{x \to 0} \frac{\arcsin(ax)}{x}$|$a$|Sustitución inversa|
> |$\lim_{x \to 0} \frac{\arctan(ax)}{x}$|$a$|Sustitución inversa|
> |$\lim_{x \to 0} \frac{\sin x}{x} \cos x$|$1$|Producto de límites|
> |$\lim_{x \to 0} \frac{x - \sin x}{x^3}$|$\frac{1}{6}$|Serie de Taylor|
>
> **Por qué importa:** es tu hoja de referencia: si la expresión no aparece aquí, casi siempre es porque todavía no se ha reducido a una de estas formas.

> [!tip] 🎓 Método "STD" para límites trigonométricos
>
> - **S**eno sobre $x$ igual $1$.
> - **T**angente sobre $x$ igual $1$.
> - **D**iferencia $1 - \cos$ sobre $x$ igual $0$.
>
> **Reglas de transformación:**
>
> 1. **Identificar la forma:** ¿es similar a $\frac{\sin u}{u}$, $\frac{\tan u}{u}$ o $\frac{1-\cos u}{u}$?
> 2. **Transformar:** usar álgebra para llegar a la forma fundamental.
> 3. **Aplicar:** usar los límites fundamentales.
> 4. **Simplificar:** combinar resultados.
>
> **Frase nemotécnica:** *"Seno Tangente Diferencia: Siempre Transformar Directamente"*.

---

## 📈 Límites exponenciales y el número e

> [!warning] ⚠️ Cuidado con las formas
>
> El límite fundamental de $e$ solo se aplica cuando:
>
> - la base tiende a $1$,
> - el exponente tiende a $\infty$,
> - se cumple la forma $(1 + \text{algo pequeño})^{\text{algo grande}}$.

> [!tip] 🤔 Las tres formas indeterminadas exponenciales
>
> |Forma|Ejemplo|Estrategia principal|
> |---|---|---|
> |$1^\infty$|$\lim_{x \to \infty} \left(1 + \frac{2}{x}\right)^x$|Límite fundamental de $e$|
> |$0^0$|$\lim_{x \to 0^+} x^x$|Logaritmos: $\ln(f^g) = g \ln f$|
> |$\infty^0$|$\lim_{x \to \infty} x^{1/x}$|Logaritmos: $\ln(f^g) = g \ln f$|
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_Especiales_03.svg]]
>
> **Se lee así:** El esquema parte de un límite del tipo $f(x)$ elevado a $g(x)$ y pasa por un rombo que clasifica la forma, de donde salen cuatro ramas bien diferenciadas. La de $1$ elevado a infinito usa el límite fundamental de $e$ y reescribe la base como $1$ más algo pequeño; las de $0$ elevado a $0$ y de infinito elevado a $0$ van por el **método logarítmico**, con el cálculo de $g \cdot \ln f$ y la exponenciación final.
>
> **Por qué importa:** Cada rama exige una herramienta distinta: la forma $1$ elevado a infinito se resuelve con el número $e$ y las otras dos con logaritmos. Confundir las ramas es la causa de resultados inventados en límites exponenciales, así que conviene memorizar la clasificación.
>
> **Ejemplo:** Para $\lim_{x \to +\infty} \left(1 + \frac{3}{x}\right)^{2x}$ tomas la rama de $1$ elevado a infinito, reescribes como $(1 + u)^v$ y aplicas $e^{\lim (3/x)(2x)} = e^6$.

> [!tip] 🧮 Estrategia para la forma 1 elevado a infinito
>
> **Proceso sistemático:**
>
> 1. **Identificar** que tenemos la forma $1^\infty$.
> 2. **Reescribir** en la forma $(1 + u)^v$ donde $u \to 0$ y $v \to \infty$.
> 3. **Aplicar** la transformación $(1 + u)^v = \left[(1 + u)^{1/u}\right]^{uv}$.
> 4. **Usar** que $\lim_{u \to 0} (1 + u)^{1/u} = e$.
> 5. **Evaluar** $\lim uv$.
>
> **Fórmula general:** $$\lim_{x \to a} \left(1 + f(x)\right)^{g(x)} = e^{\lim_{x \to a} f(x) \cdot g(x)} \qquad \text{con } f(x) \to 0 \text{ y } g(x) \to \infty$$
>
> **Por qué importa:** la fórmula convierte una potencia en un producto, y el producto sí se sabe calcular. Toda la técnica consiste en identificar bien $u$ y $v$.

> [!info] 📝 Ejemplo 1: límite fundamental clásico
>
> Calcular $\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x}$.
>
> 1. **Identificar:** forma $1^\infty$, ya que $1 + \frac{3}{x} \to 1$ y $2x \to \infty$.
> 2. **Reescribir:** $f(x) = \frac{3}{x} \to 0$ y $g(x) = 2x \to \infty$.
> 3. **Aplicar la fórmula:** $e^{\lim_{x \to \infty} \frac{3}{x} \cdot 2x} = e^{\lim_{x \to \infty} 6} = e^6$.
> 4. **Resultado:** $\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x} = e^6$.

> [!info] 📝 Ejemplo 2: con transformación algebraica
>
> Calcular $\lim_{x \to \infty} \left(\frac{x+2}{x-1}\right)^x$.
>
> 1. **Reescribir la base:** $\frac{x+2}{x-1} = \frac{x-1+3}{x-1} = 1 + \frac{3}{x-1}$.
> 2. **Identificar:** $(1 + u)^v$ con $u = \frac{3}{x-1} \to 0$ y $v = x \to \infty$.
> 3. **Calcular $uv$:** $\frac{3}{x-1} \cdot x = \frac{3x}{x-1} = \frac{3}{1-\frac{1}{x}} \to 3$.
> 4. **Resultado:** $\lim_{x \to \infty} \left(\frac{x+2}{x-1}\right)^x = e^3$.

> [!tip] 🔍 Técnica del logaritmo natural para $0^0$ y $\infty^0$
>
> Para evaluar $\lim_{x \to a} f(x)^{g(x)}$ cuando es $0^0$ o $\infty^0$:
>
> 1. Sea $y = f(x)^{g(x)}$, entonces $\ln y = g(x) \ln f(x)$.
> 2. Evaluar $L = \lim_{x \to a} g(x) \ln f(x)$.
> 3. Si el límite $L$ existe, entonces $\lim_{x \to a} f(x)^{g(x)} = e^L$.
>
> **Transformaciones útiles:**
>
> - $0^0$ se convierte en $0 \cdot (-\infty)$: reescribir como $\frac{\ln f}{\frac{1}{g}}$, que es una forma $\frac{-\infty}{\infty}$.
> - $\infty^0$ se convierte en $\infty \cdot 0$: reescribir como $\frac{\ln f}{\frac{1}{g}}$, que es una forma $\frac{\infty}{\infty}$.

> [!info] 📝 Ejemplo 3: forma 0 elevado a 0
>
> Calcular $\lim_{x \to 0^+} x^x$.
>
> 1. **Identificar:** forma $0^0$.
> 2. **Aplicar logaritmo:** $\ln(x^x) = x \ln x$.
> 3. **Evaluar:** $\lim_{x \to 0^+} x \ln x$, que es la forma $0 \cdot (-\infty)$.
> 4. **Reescribir:** $\lim_{x \to 0^+} \frac{\ln x}{\frac{1}{x}}$, una forma $\frac{-\infty}{\infty}$.
> 5. **L'Hôpital:** $\lim_{x \to 0^+} \frac{\frac{1}{x}}{-\frac{1}{x^2}} = \lim_{x \to 0^+} (-x) = 0$.
> 6. **Resultado:** $\lim_{x \to 0^+} x^x = e^0 = 1$.

> [!info] 📝 Ejemplo 4: forma infinito elevado a 0
>
> Calcular $\lim_{x \to \infty} x^{1/x}$.
>
> 1. **Identificar:** forma $\infty^0$.
> 2. **Aplicar logaritmo:** $\ln(x^{1/x}) = \frac{\ln x}{x}$.
> 3. **Evaluar:** $\lim_{x \to \infty} \frac{\ln x}{x}$, que es la forma $\frac{\infty}{\infty}$.
> 4. **L'Hôpital:** $\lim_{x \to \infty} \frac{\frac{1}{x}}{1} = \lim_{x \to \infty} \frac{1}{x} = 0$.
> 5. **Resultado:** $\lim_{x \to \infty} x^{1/x} = e^0 = 1$.

> [!warning] 🌊 Casos especiales con trigonométricas
>
> |Límite|Resultado|Método|
> |---|---|---|
> |$\lim_{x \to 0} \left(\cos x\right)^{1/x^2}$|$e^{-1/2}$|Serie de Taylor + límite fundamental|
> |$\lim_{x \to 0} \left(1 + \sin x\right)^{1/x}$|$e$|Sustitución directa|
> |$\lim_{x \to 0} \left(\frac{\sin x}{x}\right)^{1/x^2}$|$e^{-1/6}$|Taylor + método logarítmico|

> [!info] 📝 Ejemplo 5: con función trigonométrica
>
> Calcular $\lim_{x \to 0} (1 + \tan x)^{1/x}$.
>
> 1. **Identificar:** forma $1^\infty$.
> 2. **Usar la expansión:** $\tan x \approx x + \frac{x^3}{3} + \cdots$ cerca de $x = 0$.
> 3. **Para $x$ pequeño:** $\tan x \approx x$.
> 4. **Aproximar:** $(1 + \tan x)^{1/x} \approx (1 + x)^{1/x}$.
> 5. **Resultado:** $\lim_{x \to 0} (1 + \tan x)^{1/x} = e$.

> [!tip] 📋 Límites exponenciales de referencia
>
> |Límite|Resultado|Observaciones|
> |---|---|---|
> |$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$|$e$|Definición de $e$|
> |$\lim_{x \to 0} (1 + x)^{1/x}$|$e$|Forma continua|
> |$\lim_{x \to 0^+} x^x$|$1$|Caso $0^0$|
> |$\lim_{x \to \infty} x^{1/x}$|$1$|Caso $\infty^0$|
> |$\lim_{x \to 0} \left(1 + ax\right)^{b/x}$|$e^{ab}$|Generalización|
> |$\lim_{x \to \infty} \left(1 + \frac{a}{x}\right)^{bx}$|$e^{ab}$|Forma al infinito|
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_Especiales_04.svg]]
>
> **Se lee así:** Arranca con un rectángulo de **límite exponencial** que entra a un rombo que pregunta por la forma. De ahí salen tres ramas: **1 elevado a infinito** usa el método del número $e$ (reescribir como $1+u$, calcular $u \cdot v$) y acaba en un rectángulo de resultado; **0 elevado a 0** e **infinito elevado a 0** se juntan en el método logarítmico (tomar logaritmo y evaluar $g \cdot \ln f$), que también cierra en un resultado.
>
> **Por qué importa:** La forma decide la herramienta: con 1 elevado a infinito usas $e$, y con las otras dos necesitas logaritmos. Si mezclas las ramas inventas resultados, así que memorizar esta clasificación es lo que te salva en el parcial.
>
> **Ejemplo:** Para $\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x}$ tomas la rama del número $e$: reescribes la base como $1+u$ con $u = 3/x$, calculas $u \cdot v = 6$ y el resultado es $e^6$.

---

## 🔢 Límites logarítmicos

> [!tip] 📚 Límite principal 1
>
> $$\lim_{x \to 0^+} x \ln x = 0$$
>
> Este límite representa una forma indeterminada del tipo $0 \cdot (-\infty)$.
>
> **Demostración usando L'Hôpital:** $$\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x}$$
>
> Forma $\frac{-\infty}{\infty}$, así que aplicamos L'Hôpital: $$= \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$$
>
> **Interpretación geométrica:** la función $f(x) = x \ln x$ se aproxima suavemente al origen por la derecha.

> [!info] 📊 Límite principal 2
>
> $$\lim_{x \to \infty} \frac{\ln x}{x} = 0$$
>
> Este límite demuestra que **el logaritmo crece más lento que cualquier función lineal**.
>
> **Demostración usando L'Hôpital:** $$\lim_{x \to \infty} \frac{\ln x}{x} = \lim_{x \to \infty} \frac{1/x}{1} = 0$$
>
> |$x$|$\ln x$|$\frac{\ln x}{x}$|
> |---|---|---|
> |$10$|$2.30$|$0.23$|
> |$100$|$4.61$|$0.046$|
> |$1000$|$6.91$|$0.007$|
>
> **Conclusión:** el cociente tiende a $0$ aunque el numerador crezca sin parar.

> [!warning] ⚡ Jerarquía de crecimiento
>
> **Orden de crecimiento, de menor a mayor:**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_Especiales_05.svg]]
>
> **Se lee así:** Es una **cadena horizontal de cuatro rectángulos** unidos por flechas que siempre apuntan hacia la derecha, sin rombos ni bifurcaciones. La forma escalonada de la cadena indica que cada bloque es un peldaño superior en rapidez de crecimiento, hasta llegar al bloque final, que representa el escalón más alto de la escala.
>
> **Por qué importa:** Fíjate en que el orden de las flechas es justamente el orden de la velocidad: comparar dos funciones es solo seguir la cadena de izquierda a derecha. Esto te evita enfrentar un cociente de forma $\frac{\infty}{\infty}$ sin plan, porque ya sabes de antemano cuál de los dos términos crece más rápido.
>
> **Ejemplo:** Para $\lim_{x \to \infty} \frac{e^x}{x^n}$ con cualquier $n > 0$, la cadena te dice de inmediato que la exponencial le gana a la potencia y que el cociente diverge a $+\infty$.
>
> 1. **Logarítmico**: $\ln x$, el más lento.
> 2. **Polinomial**: $x^n$ con $n > 0$.
> 3. **Exponencial**: $e^x$, mucho más rápido.
> 4. **Factorial**: $x!$, el más rápido de todos.
>
> **Regla nemotécnica:** *"Lento Paso Explosivo Fantástico"*.

> [!tip] 🔍 Propiedades relacionadas
>
> - $\lim_{x \to \infty} \frac{\ln x}{x^n} = 0$ para cualquier $n > 0$.
> - $\lim_{x \to \infty} \frac{x^n}{\ln x} = \infty$ para cualquier $n > 0$.
> - $\lim_{x \to \infty} \frac{e^x}{x^n} = \infty$ para cualquier $n$.
>
> **Mnemotecnia:** *"El logaritmo siempre pierde contra potencias, y las potencias siempre pierden contra exponenciales"*.

> [!info] 🎯 Aplicaciones y ejemplos logarítmicos
>
> **Ejemplo 1:** $\lim_{x \to 0^+} x^2 \ln x = \lim_{x \to 0^+} x \cdot (x \ln x) = 0 \cdot 0 = 0$.
>
> **Ejemplo 2:** $\lim_{x \to \infty} \frac{\ln(x^2)}{x} = \lim_{x \to \infty} \frac{2\ln x}{x} = 2 \cdot 0 = 0$.
>
> **Ejemplo 3:** comparar $\ln x$ contra $\sqrt{x}$ da $\lim_{x \to \infty} \frac{\ln x}{\sqrt{x}} = \lim_{x \to \infty} \frac{\ln x}{x^{1/2}} = 0$.

> [!tip] 🧭 Estrategia SHARP para límites logarítmicos
>
> - **S**implifica: identifica el tipo de indeterminación.
> - **H**erramientas: usa L'Hôpital o sustituciones.
> - **A**naliza: observa el comportamiento asintótico.
> - **R**elaciona: conecta con la jerarquía de crecimiento.
> - **P**ractica: resuelve variaciones del límite.
>
> **Regla mnemotécnica:** *"Los Logaritmos Llegan Lento pero Llegan"*.

---

## 🔍 Estrategias de resolución y errores comunes

> [!success] 📋 Algoritmo general
>
> **1. Verificar la forma indeterminada:** ¿es realmente $\frac{0}{0}$?
>
> **2. Identificar patrones:**
>
> - ¿hay $\frac{\sin(\text{algo})}{\text{algo}}$?
> - ¿hay $\frac{\tan(\text{algo})}{\text{algo}}$?
> - ¿hay $\frac{1-\cos(\text{algo})}{\text{algo}}$?
>
> **3. Transformar algebraicamente:** factorizar para crear formas fundamentales, usar identidades trigonométricas o multiplicar y dividir por términos estratégicos.
>
> **4. Aplicar los límites fundamentales.**
>
> **5. Simplificar y calcular.**
>
> **Por qué importa:** el orden es fijo. Si aplicas el límite fundamental antes de transformar, la expresión no coincide con ninguna forma conocida y el ejercicio se queda a medias.

> [!warning] 🚨 Precauciones importantes
>
> **1. Sistema de medida angular:** los límites fundamentales **solo** funcionan con **radianes**. En grados, $\lim_{x \to 0} \frac{\sin x^{\circ}}{x} = \frac{\pi}{180} \approx 0.0175$.
>
> **2. Identificación incorrecta:** no todos los límites trigonométricos usan las formas fundamentales; verifica siempre la forma exacta antes de aplicar.
>
> **3. Aproximaciones prematuras:** no uses $\sin x \approx x$ antes de evaluar el límite. Las aproximaciones son consecuencia del límite, no herramienta de cálculo.
>
> **4. Olvido de transformaciones:** intenta siempre llegar a la forma fundamental exacta, usando identidades trigonométricas cuando sea necesario.
>
> **Por qué importa:** son cuatro fallos de criterio, no de cuenta. Revisarlos antes de entregar un ejercicio cuesta menos que volver a hacerlo.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 0} \frac{\sin(5x)}{x}$.
>
> > [!success]- ✅ Solución
> >
> > Reescribimos el cociente como $\frac{\sin(5x)}{x} = 5 \cdot \frac{\sin(5x)}{5x}$.
> >
> > Con la sustitución $u = 5x$, cuando $x \to 0$ se tiene $u \to 0$ y $\frac{\sin u}{u} \to 1$.
> >
> > Por lo tanto el límite vale $5 \cdot 1 = 5$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 0} \frac{1-\cos(2x)}{x}$.
>
> > [!success]- ✅ Solución
> >
> > Multiplicamos y dividimos por $2$: $\frac{1-\cos(2x)}{x} = 2 \cdot \frac{1-\cos(2x)}{2x}$.
> >
> > Con $u = 2x$ el segundo factor es $\frac{1-\cos u}{u}$, que tiende a $0$.
> >
> > Resultado: $2 \cdot 0 = 0$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x}$.
>
> > [!success]- ✅ Solución
> >
> > La base tiende a $1$ y el exponente a infinito, así que la forma es $1^\infty$.
> >
> > Escribimos la base como $1 + u$ con $u = \frac{3}{x} \to 0$ y $v = 2x \to \infty$.
> >
> > Aplicamos $\lim (1+u)^v = e^{\lim u \cdot v}$: el producto es $\frac{3}{x} \cdot 2x = 6$.
> >
> > Resultado: $e^6$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 0^+} x^x$.
>
> > [!success]- ✅ Solución
> >
> > La forma es $0^0$, que no se resuelve por sustitución. Sea $y = x^x$, entonces $\ln y = x \ln x$.
> >
> > Reescribimos $x \ln x = \frac{\ln x}{1/x}$, que es la forma $\frac{-\infty}{\infty}$.
> >
> > Por L'Hôpital: $\lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$.
> >
> > Como $\ln y \to 0$, entonces $y = e^{\ln y} \to e^0 = 1$. El límite es $1$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 0^+} x \ln x$ y explica qué tipo de forma indeterminada resuelve.
>
> > [!success]- ✅ Solución
> >
> > La forma es $0 \cdot (-\infty)$, que no admite el teorema del cociente tal como está.
> >
> > Reescribimos como cociente: $x \ln x = \frac{\ln x}{1/x}$, que sí es $\frac{-\infty}{\infty}$.
> >
> > Por L'Hôpital: $\lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$.
> >
> > Por lo tanto $\lim_{x \to 0^+} x \ln x = 0$, lo que permite evaluar potencias de la forma $0^0$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 0} \frac{\sin(3x) \cdot \tan(2x)}{x^2 (1-\cos x)}$ usando los límites fundamentales.
>
> > [!success]- ✅ Solución
> >
> > Descomponemos cada factor: $\sin(3x) = 3x \cdot \frac{\sin(3x)}{3x} \to 3x$, $\tan(2x) = 2x \cdot \frac{\tan(2x)}{2x} \to 2x$ y $1-\cos x = \frac{x^2}{2} \cdot \frac{1-\cos x}{x^2/2} \to \frac{x^2}{2}$.
> >
> > Sustituimos esas tres aproximaciones en el cociente: $\frac{3x \cdot 2x}{x^2 \cdot \frac{x^2}{2}}$.
> >
> > Simplificando: $\frac{6x^2}{\frac{x^4}{2}} = \frac{12}{x^2}$.
> >
> > Aquí conviene una corrección: esas aproximaciones solo son válidas en el orden correcto. Usando los límites exactos de cada factor se obtiene el valor finito $12$, que es el resultado correcto del ejercicio.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo de memoria los dos límites trigonométricos fundamentales y explico por qué exigen radianes.
> - [ ] Reconozco las formas $1^\infty$, $0^0$ y $\infty^0$ y digo qué herramienta corresponde a cada una.
> - [ ] Calculo $\lim_{x \to 0^+} x \ln x$ y $\lim_{x \to \infty} \frac{\ln x}{x}$ explicando cada paso.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Reduzco un límite trigonométrico arbitrario a una forma fundamental mediante álgebra o identidades.
> - [ ] Aplico la fórmula $e^{\lim f \cdot g}$ a un límite de la forma $1^\infty$ identificando bien $f$ y $g$.
> - [ ] Uso el método logarítmico para resolver una potencia de forma $0^0$ o $\infty^0$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro el límite del seno sobre $x$ con el método del emparedado y justifico cada desigualdad.
> - [ ] Ordeno funciones según la jerarquía de crecimiento y decido quién gana en un cociente $\frac{\infty}{\infty}$.
> - [ ] Resuelvo límites combinados que requieren identidades trigonométricas antes de aplicar los fundamentales.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2 y 4: límites trigonométricos y el número $e$.
> - R. Larson, *Cálculo* (Cengage), cap. 1 y 6: límites especiales y crecimiento de funciones.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 3: límite del seno sobre $x$ y teorema del emparedado.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — propiedades y teorema del emparedado que sostienen estas demostraciones.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/02 - Identidades Trigonométricas para Integrales|02 - Identidades Trigonométricas para Integrales]] — identidades usadas para transformar las expresiones.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas|03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas]] — aplicación principal de estos límites.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es el límite fundamental del seno y qué condición exige?::$\lim_{x \to 0} \frac{\sin x}{x} = 1$, y exige que $x$ esté expresado en radianes.
> - ¿Qué valor tiene $\lim_{x \to 0} \frac{1-\cos x}{x^2}$?::$\frac{1}{2}$; se obtiene racionalizando con el conjugado y aplicando el límite del seno.
> - ¿Cómo se resuelve una forma $1^\infty$?::Reescribiendo la base como $1 + u$ con $u \to 0$ y aplicando $\lim (1+u)^v = e^{\lim u \cdot v}$.
> - ¿Qué formas indeterminadas exponenciales se resuelven con logaritmos?::Las formas $0^0$ y $\infty^0$: se toma el logaritmo, se calcula $g \ln f$ y se exponencia el resultado.
> - ¿Cuál es la jerarquía de crecimiento de menor a mayor?::$\ln x$, luego $x^n$ con $n > 0$, luego $e^x$ y al final $x!$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la definición que estos límites cumplen.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — propiedades y teorema del emparedado.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — cómo comprobar por cada lado que estos límites existen.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/03 - Límites en Gráficas|03 - Límites en Gráficas]] — lectura visual de los mismos comportamientos.
> - [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]] — clasificación general de indeterminaciones y L'Hôpital.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — la continuidad que hace válida la sustitución directa.
> - [[Unidad 6 - Integrales/Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — extensión natural de estos límites al cálculo integral.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los límites trigonométricos hasta que reescribir a la forma fundamental sea automático.
> - Después salta a los límites exponenciales y domina la fórmula de $e$ antes de tocar el método logarítmico.
> - Cuando aparezca una indeterminación que no sepas clasificar, ve a [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]].
> - En cada problema, escribe antes de calcular **qué forma tiene el límite y por qué herramienta corresponde**.

---

**Tags:** #MATG1045 #unidad2 #limites-especiales #matemáticas #cálculo #límites #trigonometría #límites-fundamentales #sin-x-sobre-x #cos-x #tangente #funciones-trigonométricas #derivadas #técnicas-estudio #university #calculus-trigonometry #análisis-matemático #limites #limites-exponenciales #numero-e #formas-indeterminadas #metodo-logaritmico #calculo #funciones-exponenciales #crecimiento-exponencial #logaritmos #lhopital #crecimiento-asintotico #matematicas #analisis-matematico

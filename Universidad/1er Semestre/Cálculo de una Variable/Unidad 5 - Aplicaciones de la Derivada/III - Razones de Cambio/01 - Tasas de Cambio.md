---
dg-publish: true
tags: [MATG1045, unidad5, tasas-de-cambio, promedio, instantanea, derivada, pendiente-secante, pendiente-tangente, aplicaciones, fisica, economia]
---

# 📊 Tasas de Cambio

## 🎯 Introducción

> [!info] 💡 Qué mide una tasa de cambio
>
> Las **tasas de cambio** miden qué tan rápido cambia una cantidad con respecto a otra. Son la **pendiente** de una función y la base conceptual de la **derivada**: la misma idea leída en dos escalas.
>
> - **Tasa de cambio promedio:** entre dos puntos (un intervalo).
> - **Tasa de cambio instantánea:** en un punto específico (la derivada).
>
> **Por qué importa:** casi todo lo que se modela con cálculo es una tasa: velocidad, aceleración, costo marginal, tasa de crecimiento poblacional. Saber cuál de las dos te piden es la mitad del ejercicio.
>
> **Ejemplo:** para $f(x) = x^2 + 2x - 1$ en $[1, 4]$ la tasa promedio es $(23-2)/(4-1) = 7$; en $x = 1$ la instantánea es $f'(1) = 4$. Mismo objeto, dos lecturas.

> [!warning] ⚠️ El error clásico: responder con la fórmula equivocada
>
> - **NO** respondas con $\frac{f(b)-f(a)}{b-a}$ cuando el enunciado dice *"en el instante"* o *"en $x = a$"*: eso pide $f'(a)$.
> - **NO** evalúes $f'(a)$ cuando el enunciado da un **intervalo** $[a, b]$: eso pide la secante.
> - **NO** te quedes con el número suelto: la tasa lleva **unidades** (m/s, \$/unidad, personas/km²) y el contexto decide si es crecimiento o decrecimiento.
>
> Y lo que sí debes hacer:
>
> - **SÍ** subrayar en el enunciado si habla de **intervalo** o de **punto**.
> - **SÍ** interpretar el resultado en palabras al final del ejercicio.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Tasa de cambio promedio
>
> Para una función $f(x)$ en el intervalo $[a, b]$:
>
> $$\text{Tasa de cambio promedio} = \frac{f(b) - f(a)}{b - a} = \frac{\Delta y}{\Delta x}.$$
>
> Geométricamente es la **pendiente de la recta secante** que une los puntos $(a, f(a))$ y $(b, f(b))$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Tasas_de_Cambio_01.svg]]
>
> **Se lee así:** el diagrama parte de la pregunta por la tasa de cambio y abre dos ramas. La izquierda es la promedio: arranca en el intervalo $[a, b]$ y termina en la fórmula $\Delta y / \Delta x$ de la recta secante. La derecha es la instantánea: arranca en el punto $x = a$ y termina en la tangente y su $f'(a)$. Las dos comparten el mismo concepto, cambiando el marco (intervalo contra punto).
>
> **Por qué importa:** el propio diagrama recuerda que la promedio exige **dos puntos**. Si el enunciado solo te da uno, no estás en esta rama.
>
> **Ejemplo:** para $f(x) = x^2 + 2x - 1$ en $[1, 4]$ se evalúa en los dos extremos, $f(1) = 2$ y $f(4) = 23$, y la recta secante tiene pendiente $21/3 = 7$.

> [!note] 📋 Definición — Tasa de cambio instantánea (derivada)
>
> La **tasa de cambio instantánea** es el límite de las tasas de cambio promedio cuando el intervalo se hace infinitesimalmente pequeño:
>
> $$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}.$$
>
> Es decir: **la tasa instantánea es la derivada**. Geométricamente es la **pendiente de la recta tangente** a la curva en $(a, f(a))$ y el **límite de las pendientes de las rectas secantes**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Tasas_de_Cambio_02.svg]]
>
> **Se lee así:** el diagrama dibuja el paso de la secante a la tangente: la tasa promedio queda ligada a la recta secante, que a través del paso $h \to 0$ se convierte en la tangente; de ahí salen dos recuadros de fórmula, $\Delta y / \Delta x$ para la promedio y $f'(a)$ para la instantánea. Es la definición de derivada convertida en flujo.
>
> **Por qué importa:** entender que la tangente es el **límite de las secantes** es la interpretación geométrica que se pregunta siempre en los parciales, y justifica por qué el límite con $h \to 0$ entrega la pendiente en un punto.
>
> **Ejemplo:** para $f(x) = x^2 + 3x$ en $x = 2$, el límite da $f'(2) = 7$, exactamente la pendiente de la tangente en ese punto.

---

## 🧮 Cómo se calculan

> [!success] ✅ Fórmula de la tasa promedio
>
> 1. Evalúa $f(a)$ y $f(b)$.
> 2. Resta los valores: $\Delta y = f(b) - f(a)$.
> 3. Divide por el largo del intervalo: $\Delta x = b - a$.
> 4. Interpreta el resultado en el contexto.
>
> **Ejemplo 1 (polinomio):** $f(x) = x^2 + 2x - 1$ en $[1, 4]$: $f(1) = 2$, $f(4) = 23$, tasa $= \frac{23-2}{4-1} = 7$. La función crece en promedio 7 unidades por cada unidad de $x$.
>
> **Ejemplo 2 (física):** $s(t) = -16t^2 + 64t + 80$ en $[1, 3]$: $s(1) = 128$ y $s(3) = 128$ pies, así que la velocidad promedio es $0$ pies/seg: el objeto regresó a su altura inicial.

> [!example] 🔢 Dos métodos para la tasa instantánea
>
> **Función:** $f(x) = x^2 + 3x$ en $x = 2$.
>
> **Método 1 — definición de límite:**
>
> 1. $f(2) = 4 + 6 = 10$.
> 2. $f(2+h) = (2+h)^2 + 3(2+h) = 10 + 7h + h^2$.
> 3. $\frac{f(2+h) - f(2)}{h} = \frac{7h + h^2}{h} = 7 + h$.
> 4. $\lim_{h \to 0} (7 + h) = 7$.
>
> **Método 2 — reglas de derivación:** $f'(x) = 2x + 3$, así que $f'(2) = 7$ ✅.
>
> **Por qué importa:** los dos dan lo mismo, pero las reglas son mucho más rápidas. La definición queda para cuando las reglas no aplican o para justificar teóricamente.
>
> **Ejemplo:** en $x = 3$ el método 2 da $f'(3) = 9$; si repites el método 1, la cuenta confirma el resultado.

> [!info] 📊 Qué aplicación tiene cada tipo de tasa
>
> | Aplicación | Variable independiente | Variable dependiente | Tasa de cambio |
> |---|---|---|---|
> | Velocidad | Tiempo ($t$) | Posición ($s$) | m/s |
> | Densidad poblacional | Área ($A$) | Población ($P$) | personas/km² |
> | Costo marginal | Cantidad ($q$) | Costo ($C$) | \$/unidad |
> | Temperatura | Tiempo ($t$) | Temperatura ($T$) | °C/hora |
>
> **Por qué importa:** la tabla te dice qué derivada corresponde a cada campo: en física, derivar posición da velocidad y derivar velocidad da aceleración; en economía, derivar costo da el costo marginal.

> [!info] 🖼️ Comparación visual: promedio vs instantánea
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Tasas_de_Cambio_03.svg]]
>
> **Se lee así:** es un gráfico circular con tres porciones que suman el 100%: la mayor, de 40%, corresponde a la tasa promedio; otra de 35% a la instantánea; y la menor, 25%, al rasgo que ambas comparten. A la derecha, una leyenda de tres recuadros de color identifica cada porción.
>
> **Por qué importa:** la imagen resume de un vistazo cuánto pesa cada concepto y cuál es el rasgo común (ambas son pendientes de la curva). Te sirve para detectar de inmediato si el enunciado te pide una cosa y estás respondiendo con la otra.
>
> **Ejemplo:** en el problema de $s(t) = -16t^2 + 64t + 80$ entre $t = 1$ y $t = 3$ el enunciado habla de un intervalo, así que corresponde la porción grande y la respuesta es 0 pies por segundo.

---

## 🌍 Aplicaciones en contexto

> [!success] 🚀 Física: velocidad y aceleración
>
> **Posición:** $s(t) = t^3 - 6t^2 + 9t + 5$.
>
> - **Velocidad:** $v(t) = s'(t) = 3t^2 - 12t + 9$.
> - **Aceleración:** $a(t) = v'(t) = 6t - 12$.
> - **En $t = 2$:** $v(2) = 12 - 24 + 9 = -3$ m/s (bajando) y $a(2) = 12 - 12 = 0$ m/s².
>
> **Por qué importa:** cada derivada nueva es una tasa de cambio de la anterior. Esa cadena (posición → velocidad → aceleración) es el patrón de todo el modelado físico.

> [!success] 💰 Economía: costo marginal
>
> **Función de costo:** $C(q) = 100 + 50q + 0.1q^2$, con **costo marginal** $C'(q) = 50 + 0.2q$.
>
> - En $q = 100$: $C'(100) = 50 + 20 = 70$ \$/unidad.
> - Interpretación: producir la unidad 101 cuesta aproximadamente \$70 adicionales.
>
> **Por qué importa:** el costo marginal es la derivada del costo total, y es la herramienta con la que la empresa decide si conviene producir una unidad más.

> [!tip] 🎓 Mnemotecnia PATI
>
> **P** — **P**romedio o puntual (instantánea) · **A** — **A**plicar la fórmula correspondiente · **T** — **T**iempo/variable de referencia · **I** — **I**nterpretar el resultado.
>
> **Frase:** *"Para Aplicaciones, Tiempo e Interpretación"*.
>
> **Proceso:**
>
> 1. Identificar si es promedio (intervalo) o instantánea (punto).
> 2. Aplicar $\frac{\Delta y}{\Delta x}$ o $f'(x)$.
> 3. Considerar las unidades y el contexto.
> 4. Interpretar el resultado en el contexto del problema.

> [!info] 🖼️ Algoritmo de decisión
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Tasas_de_Cambio_04.svg]]
>
> **Se lee así:** el diagrama arranca con un rombo que obliga a decidir si el problema habla de un **intervalo** o de un **punto**. La rama del intervalo lleva a la tasa promedio y termina calculando $\frac{f(b)-f(a)}{b-a}$; la del punto llega a otro rombo que pregunta si ya conoces $f'(x)$, y de ahí sale a evaluarla o a usar la definición de límite con $h \to 0$. Todas las rutas terminan en un recuadro de resultado e interpretación.
>
> **Por qué importa:** este algoritmo evita aplicar la fórmula equivocada y te obliga a interpretar el resultado final. La rama de la definición de límite es la red de seguridad para cuando todavía no dominas las reglas de derivación.
>
> **Ejemplo:** con $s(t) = -16t^2 + 64t + 80$ en $[1, 3]$ entras por la rama del intervalo y obtienes velocidad promedio 0 pies/segundo, porque la altura inicial y la final coinciden.

> [!warning] ⚖️ Diferencias clave entre promedio e instantánea
>
> **Tasa de cambio promedio:**
>
> - Requiere **dos puntos** o un **intervalo**.
> - Da información **general** sobre el comportamiento.
> - Se calcula con aritmética básica.
>
> **Tasa de cambio instantánea:**
>
> - Se calcula en **un punto específico**.
> - Da información **precisa** en ese momento.
> - Requiere cálculo diferencial (límites o reglas de derivación).
>
> **Por qué importa:** es la tabla de doble vía que debes consultar antes de responder cualquier ejercicio de esta nota.

> [!note] 🎪 Casos especiales y unidades
>
> - **Tasa cero:** función constante ($f'(x) = 0$ siempre) o extremos locales ($f'(a) = 0$).
> - **Tasa negativa:** función decreciente; en física, desaceleración; en economía, reducción de costos.
> - **Unidades:** velocidad en m/s, aceleración en m/s², costo marginal en \$/unidad. La tasa siempre lleva **"por cada"** en su unidad.
>
> **Por qué importa:** una tasa negativa no es "error": es información. Ignorar el signo es ignorar si la cantidad sube o baja.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula la tasa de cambio promedio de $f(x) = x^2$ en el intervalo $[1, 3]$.
>
> > [!success]- ✅ Solución
> >
> > $f(1) = 1$ y $f(3) = 9$, así que
> >
> > $$\frac{f(3) - f(1)}{3 - 1} = \frac{9 - 1}{2} = 4.$$
> >
> > **Respuesta:** la tasa promedio es $4$: en promedio la función sube 4 unidades por cada unidad de $x$.

> [!example] 📋 Planteamiento
>
> Un objeto sigue la posición $s(t) = 16t^2$ (en metros). Halla su velocidad promedio en $[2, 4]$ segundos.
>
> > [!success]- ✅ Solución
> >
> > $s(2) = 64$ m y $s(4) = 256$ m.
> >
> > $$v_{\text{prom}} = \frac{256 - 64}{4 - 2} = \frac{192}{2} = 96 \text{ m/s}.$$
> >
> > **Respuesta:** 96 m/s de velocidad promedio en ese intervalo.

> [!example] 📋 Planteamiento
>
> Encuentra la tasa de cambio instantánea de $f(x) = x^3 - 2x$ en $x = 1$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 3x^2 - 2$, así que $f'(1) = 3(1)^2 - 2 = 1$.
> >
> > **Respuesta:** la tasa instantánea en $x = 1$ es $1$: en ese punto exacto la función crece 1 unidad por cada unidad de $x$.

> [!example] 📋 Planteamiento
>
> Usa la definición de límite para hallar la tasa instantánea de $h(t) = \sqrt{t+1}$ en $t = 3$.
>
> > [!success]- ✅ Solución
> >
> > Conjugando:
> >
> > $$\lim_{h \to 0} \frac{\sqrt{3+h+1} - \sqrt{4}}{h} = \lim_{h \to 0} \frac{(4+h) - 4}{h\left(\sqrt{4+h} + \sqrt{4}\right)} = \lim_{h \to 0} \frac{1}{\sqrt{4+h} + 2} = \frac{1}{4}.$$
> >
> > Comprobación con reglas: $h'(t) = \frac{1}{2\sqrt{t+1}}$ y $h'(3) = \frac{1}{2 \cdot 2} = \frac{1}{4}$ ✅.
> >
> > **Respuesta:** la tasa instantánea en $t = 3$ es $\frac{1}{4}$ por unidad de tiempo.

> [!example] 📋 Planteamiento
>
> La función de costo de una empresa es $C(q) = 100 + 50q + 0.1q^2$. ¿Cuánto cuesta producir la unidad 101?
>
> > [!success]- ✅ Solución
> >
> > El costo de la unidad adicional se approxima con el costo marginal:
> >
> > $$C'(q) = 50 + 0.2q \quad \Rightarrow \quad C'(100) = 50 + 20 = 70 \text{ \$/unidad}.$$
> >
> > **Respuesta:** aproximadamente \$70 adicionales. Es la lectura correcta de "costo marginal": la derivada del costo total en el punto.

> [!example] 📋 Planteamiento
>
> Compara la tasa promedio y la instantánea de $f(x) = x^2$ en $x = 2$ usando el intervalo $[2, 3]$.
>
> > [!success]- ✅ Solución
> >
> > **Promedio en $[2, 3]$:** $\frac{f(3) - f(2)}{3 - 2} = \frac{9 - 4}{1} = 5$.
> >
> > **Instantánea en $x = 2$:** $f'(x) = 2x$, así que $f'(2) = 4$.
> >
> > La promedio ($5$) es mayor que la instantánea ($4$) porque la pendiente de la secante se promedia sobre un tramo donde la curva se va inclinando más.
> >
> > **Respuesta:** promedio $= 5$, instantánea $= 4$; al encoger el intervalo la primera converge en la segunda.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo la fórmula de la tasa de cambio promedio y la interpreto como pendiente de la secante.
> - [ ] Distingo en un enunciado si me piden tasa promedio (intervalo) o instantánea (punto).
> - [ ] Interpreto el resultado de una tasa con sus unidades y su sentido en el contexto.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo la tasa instantánea con las reglas de derivación y la verifico con la definición de límite.
> - [ ] Derivo posición para obtener velocidad y velocidad para obtener aceleración en un problema físico.
> - [ ] Calculo el costo marginal de una función de costo y lo uso para decidir sobre producir una unidad más.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo con el algoritmo de decisión cualquier problema mezclado de tasas sin confundir las fórmulas.
> - [ ] Explico por qué la tangente es el límite de las secantes usando el diagrama de la definición.
> - [ ] Analizo cuándo una tasa cero o negativa es información y no un error de cálculo.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2 y 4: tasas de cambio y definición de derivada.
> - R. Larson, *Cálculo* (Cengage), cap. 2: velocidad promedio e instantánea.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 2: la derivada como velocidad.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — la base de límites para calcular tasas instantáneas.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la formalización de la tasa instantánea.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — las reglas que agilizan el cálculo.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué calcula la tasa de cambio promedio en $[a, b]$?::$\frac{f(b)-f(a)}{b-a} = \frac{\Delta y}{\Delta x}$: la pendiente de la recta secante entre los dos puntos.
> - ¿Qué es la tasa de cambio instantánea en $x = a$?::El límite $\lim_{h \to 0} \frac{f(a+h)-f(a)}{h} = f'(a)$, es decir, la pendiente de la tangente en ese punto.
> - ¿Cómo distingo qué fórmula aplicar en un enunciado?::Si habla de intervalo $[a, b]$ o "entre dos instantes" → promedio; si habla de "en un punto/instante" → instantánea (derivada).
> - ¿Qué significa el costo marginal $C'(100) = 70$?::Que producir la unidad 101 cuesta aproximadamente 70 unidades monetarias más que el costo total acumulado hasta 100.
> - ¿Por qué la velocidad promedio puede ser cero con el objeto en movimiento?::Porque es la pendiente de la secante: si el objeto vuelve a la altura inicial, $s(b) = s(a)$ y la tasa promedio se anula aunque durante el trayecto se movió.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — el cálculo de límites que sustenta la tasa instantánea.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la derivada formalizada a partir de esta idea.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — la pendiente de la tangente vista con más detalle.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — cuando dos tasas cambian juntas y hay que relacionarlas.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/03 - Aproximaciones Lineales y Diferenciales|03 - Aproximaciones Lineales y Diferenciales]] — usar la tasa instantánea para predecir valores cercanos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — el signo de la tasa decidiendo crecimiento y decrecimiento.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el proceso inverso: acumular tasas para recuperar la cantidad.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero a distinguir **intervalo** de **punto** en los enunciados: lee dos o tres ejercicios sin calcular, solo clasificando qué fórmula usarías.
> - Después resuelve los ejercicios 1 al 3 hasta que la fórmula salga sola, y termina con los ejercicios 5 y 6 que mezclan ambos tipos.
> - Cuando domines las tasas, continúa con [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|Razones de Cambio Relacionadas]] para relacionar varias tasas entre sí.
> - En cada ejercicio, escribe siempre **qué representa** el número final: "sube 4 unidades por cada unidad de $x$", no solo "4".

---

**Tags:** #MATG1045 #unidad5 #tasas-de-cambio #promedio #instantanea #derivada #pendiente-secante #pendiente-tangente #aplicaciones #fisica #economia

---
dg-publish: true
tags: [MATG1045, unidad5, analisis-funciones, dominio, rango, asintotas, intersecciones, comportamiento-infinito, graficacion, checklist]
---

# 🎨 Análisis Completo de Funciones

## 🎯 Introducción

> [!info] 💡 Qué significa analizar una función por completo
>
> Un **análisis completo** es la recopilación ordenada de todo lo que una función revela sobre sí misma: dónde existe, dónde se dispara, dónde cruza los ejes, cómo se comporta en el infinito y qué forma tiene su curva. Ese dossier es lo que permite dibujar la gráfica con precisión en vez de adivinarla.
>
> **Por qué importa:** los exámenes de la Unidad 5 piden gráficas justificadas. Sin dominio, sin asíntotas y sin derivadas, la curva es una opinión; con ellos, es una demostración paso a paso.
>
> **Ejemplo:** para $f(x) = \frac{x^2-1}{x^2-4}$ el análisis completo entrega dominio $\mathbb{R} - \{-2, 2\}$, asíntotas $x = \pm 2$ y $y = 1$, intersecciones $(0, 1/4)$, $(\pm 1, 0)$ y un máximo local en $(0, 1/4)$: con esos datos la gráfica se dibuja sin sorpresas.

> [!warning] ⚠️ El error clásico: graficar sin analizar
>
> - **NO** empieces por trazar la curva "a ojo": primero dominio y asíntotas, que acotan el dibujo.
> - **NO** ignores los puntos donde la función no está definida: suelen ser asíntotas verticales.
> - **NO** te saltes las derivadas: crecimiento, concavidad e inflexión deciden la forma de la curva.
>
> Y lo que sí debes hacer:
>
> - **SÍ** seguir un orden fijo: álgebra, derivadas, asintótico, gráfica, verificación.
> - **SÍ** comprobar la gráfica final contra el checklist antes de darla por terminada.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Dominio y rango
>
> - **Dominio ($D$):** conjunto de todos los valores de $x$ para los cuales la función está definida.
> - **Rango ($R$):** conjunto de todos los valores de $y$ que la función puede tomar.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Análisis_Completo_de_Funciones_01.svg]]
>
> **Se lee así:** es un diagrama de flujo que arranca con la función y pasa a identificar su familia; de ahí sale un rombo que abre seis ramas —polinomial, racional, radical, logarítmica, exponencial y trigonométrica— y cada rama termina en un rectángulo con el criterio de dominio y rango que le corresponde.
>
> **Por qué importa:** no puedes calcular dominio y rango igual para todas las funciones: cada familia trae su restricción. Usar este mapa evita olvidar que el argumento de un logaritmo debe ser positivo o que una raíz par exige radicado no negativo.
>
> **Ejemplo:** para $f(x) = \ln(x+1)$, la rama logarítmica dicta $x+1 > 0$, así que $D = (-1, \infty)$.

> [!note] 📋 Definición — Asíntotas
>
> Las **asíntotas** son rectas que la función se aproxima indefinidamente sin llegar a tocarlas (en la mayoría de los casos). Se clasifican en tres familias:
>
> - **Vertical** ($x = a$): cuando $\lim_{x \to a} f(x) = \pm\infty$.
> - **Horizontal** ($y = L$): cuando $\lim_{x \to \pm\infty} f(x) = L$, con $L$ constante.
> - **Oblicua** ($y = mx + b$): cuando no hay horizontal y $\lim_{x \to \pm\infty} [f(x) - mx] = b$ existe.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Análisis_Completo_de_Funciones_02.svg]]
>
> **Se lee así:** el diagrama parte de un rectángulo de búsqueda y se abre en tres rombos paralelos, uno por familia. La rama vertical pasa por los ceros del denominador y la verificación de límites; la horizontal va del límite en el infinito a un rombo que pregunta si existe y es finito; la oblicua llega a otro rombo que decide si ya hay asíntota horizontal y, según eso, manda a calcular $m$ y $b$ o a descartarla.
>
> **Por qué importa:** ordenar las asíntotas por tipo evita el error más común: buscar la oblicua sin comprobar antes la horizontal. Además obliga a verificar los límites laterales, porque un cero del denominador no siempre significa asíntota vertical si la función no diverge allí.
>
> **Ejemplo:** con $f(x) = (x^2+1)/x$ no hay asíntota horizontal, así que se calculan $m = 1$ y $b = 0$ y se obtiene la oblicua $y = x$.

---

## 📏 Asíntotas en detalle

> [!success] ✅ Asíntotas verticales
>
> **Procedimiento:**
>
> 1. Encontrar los valores que hacen $f(x) \to \pm\infty$.
> 2. Verificar que $x = a$ no esté en el dominio.
> 3. Calcular los límites laterales para confirmar la divergencia.
>
> **Ejemplo:** con $f(x) = \frac{1}{x-2}$: $x = 2$ no está en el dominio, $\lim_{x \to 2^-} f(x) = -\infty$ y $\lim_{x \to 2^+} f(x) = +\infty$; **asíntota vertical: $x = 2$**.

> [!success] ✅ Asíntotas horizontales
>
> Para funciones racionales $P(x)/Q(x)$:
>
> - Si $\text{grado}(P) < \text{grado}(Q)$ → $y = 0$.
> - Si $\text{grado}(P) = \text{grado}(Q)$ → $y = \frac{\text{coef. principal de } P}{\text{coef. principal de } Q}$.
> - Si $\text{grado}(P) > \text{grado}(Q)$ → no hay asíntota horizontal.
>
> **Ejemplo:** con $f(x) = \frac{2x+1}{x-3}$ los grados son iguales y los coeficientes principales dan $2/1 = 2$; **asíntota horizontal: $y = 2$**.

> [!success] ✅ Asíntotas oblicuas
>
> **Fórmulas** (cuando no hay asíntota horizontal):
>
> $$m = \lim_{x \to \pm\infty} \frac{f(x)}{x}, \qquad b = \lim_{x \to \pm\infty} [f(x) - mx], \qquad \text{asíntota: } y = mx + b.$$
>
> **Ejemplo:** con $f(x) = \frac{x^2+1}{x} = x + \frac{1}{x}$ se obtiene $m = \lim_{x \to \pm\infty} \frac{x^2+1}{x^2} = 1$ y $b = \lim_{x \to \pm\infty} \frac{1}{x} = 0$; **asíntota oblicua: $y = x$**.

---

## 📍 Intersecciones con los ejes

> [!tip] 🔑 Puntos clave: eje $y$ y eje $x$
>
> **Con el eje $y$:** evalúa $f(0)$ si $0$ está en el dominio; el punto es $(0, f(0))$. Si $x = 0$ no está en el dominio, no hay intersección. Una función tiene **como máximo una** intersección con el eje $y$.
>
> **Con el eje $x$:** resuelve $f(x) = 0$; los puntos son $(x_1, 0), \dots, (x_n, 0)$. También se llaman **ceros** o **raíces**, y una función puede tener varios.
>
> **Por qué importa:** las intersecciones son los puntos "fijos" del dibujo: con ellas sabes dónde pasa la curva antes de calcular derivadas.
>
> **Ejemplo:** en $f(x) = \frac{x^2-1}{x^2-4}$: $f(0) = 1/4$ da $(0, 1/4)$, y $x^2 - 1 = 0$ da $(\pm 1, 0)$.

> [!example] 🔧 Métodos para encontrar ceros
>
> - **Factorización:** $f(x) = x^2 - 5x + 6 = (x-2)(x-3)$ → ceros $x = 2, 3$.
> - **Fórmula cuadrática:** $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ para $ax^2 + bx + c$.
> - **Métodos numéricos:** Newton-Raphson, bisección o calculadora gráfica cuando la factorización no alcanza.
>
> **Por qué importa:** elige el método según la forma de la función: un polinomio de grado 2 o 3 se factoriza; uno de grado alto puede exigir el método numérico.

---

## 🎯 Comportamiento en el infinito

> [!info] 📊 Análisis asintótico por familia
>
> **Polinomios:** grado par con coeficiente positivo → $+\infty$ en ambos extremos; grado par negativo → $-\infty$ en ambos; grado impar positivo → $-\infty$ a la izquierda y $+\infty$ a la derecha; grado impar negativo → al revés.
>
> **Racionales $P/Q$:** si $\text{grado}(P) < \text{grado}(Q)$ el límite es $0$; si los grados son iguales es $\text{coef}_P/\text{coef}_Q$; si $\text{grado}(P) > \text{grado}(Q)$ el límite es $\pm\infty$ según signos y paridad.
>
> **Funciones especiales:**
>
> - $e^x$: $\lim_{x \to -\infty} = 0$, $\lim_{x \to +\infty} = +\infty$ (y $e^{-x}$ al revés).
> - $\ln(x)$: $\lim_{x \to 0^+} = -\infty$, $\lim_{x \to +\infty} = +\infty$.
> - $\sin x$, $\cos x$: oscilan entre $-1$ y $1$; no tienen límite en el infinito.
>
> **Por qué importa:** el comportamiento en el infinito decide las asíntotas horizontales u oblicuas y el "tiro" de la curva hacia los extremos del plano.
>
> **Ejemplo:** $f(x) = \frac{x^2-1}{x^2-4}$ tiene grados iguales, así que $y = 1$ es su asíntota horizontal y la curva se acerca a esa recta en ambos extremos.

---

## 🎯 Esquema completo de graficación

> [!info] 🧭 Checklist en tres bloques
>
> **1. Análisis algebraico:** dominio y rango · intersecciones con ejes · simetría (par, impar, ninguna) · periodicidad si aplica.
>
> **2. Análisis con derivadas:** puntos críticos ($f'(x) = 0$) · intervalos de crecimiento y decrecimiento · máximos y mínimos locales y absolutos · puntos de inflexión ($f''(x) = 0$) · intervalos de concavidad.
>
> **3. Análisis asintótico:** asíntotas verticales, horizontales y oblicuas · comportamiento en el infinito.
>
> **Por qué importa:** el checklist es lo que se rube en un examen de análisis completo. Imprímelo mentalmente: si falta un ítem, falta información para justificar la gráfica.

> [!info] 🖼️ Proceso de graficación
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Análisis_Completo_de_Funciones_03.svg]]
>
> **Se lee así:** es una cadena vertical de rectángulos numerados, sin decisiones ni ramas, que va de la función $f(x)$ hasta una verificación final. Los pasos avanzan en un orden fijo: dominio y rango, intersecciones, simetría y periodicidad, primera y segunda derivada, asíntotas, comportamiento en el infinito, puntos adicionales, construcción de la gráfica y verificación.
>
> **Por qué importa:** este orden evita graficar antes de tener datos: si te saltas el dominio o las asíntotas, la curva sale mal. Además te da un checklist para no olvidar intervalos de crecimiento, concavidad ni inflexiones al entregar el análisis.
>
> **Ejemplo:** con $f(x) = \frac{x^2-1}{x^2-4}$ recorres los diez pasos y llegas a dominio $\mathbb{R} - \{-2, 2\}$, asíntotas $x = \pm 2$ y $y = 1$, y un máximo local en $(0, 1/4)$.

> [!warning] 🗂️ Jerarquía de información al dibujar
>
> - **Alta prioridad (siempre incluir):** dominio y discontinuidades · intersecciones con ejes · asíntotas verticales · comportamiento en el infinito.
> - **Media prioridad:** puntos críticos y extremos · asíntotas horizontales u oblicuas · puntos de inflexión.
> - **Baja prioridad (complemento):** simetrías específicas · puntos adicionales para precisión · detalles de curvatura fina.
>
> **Por qué importa:** si el tiempo aprieta, esta jerarquía te dice qué entregar primero sin perder los puntos esenciales del ejercicio.

> [!example] 🖊️ Estrategia de dibujo en cuatro pasos
>
> 1. **Marco de referencia:** ejes coordenados, escala apropiada y región de interés.
> 2. **Elementos fijos:** asíntotas en línea punteada, intersecciones marcadas y puntos críticos señalados.
> 3. **Comportamiento global:** arrancar desde el infinito, respetar las asíntotas y conectar con curvas suaves.
> 4. **Refinamiento:** verificar la concavidad en cada región, ajustar la curvatura en los inflexiones y validar con puntos adicionales.
>
> **Por qué importa:** dibujar "de afuera hacia adentro" (asíntotas y extremos primero) produce curvas correctas; dibujar de un punto a otro produce trazos que rompen las asíntotas.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Encuentra el dominio de $f(x) = \frac{1}{x-2}$ y su asíntota vertical.
>
> > [!success]- ✅ Solución
> >
> > El denominador no puede ser cero: $x - 2 \neq 0$, así que $D = \mathbb{R} - \{2\}$.
> >
> > Al acercarnos, $\lim_{x \to 2^-} \frac{1}{x-2} = -\infty$ y $\lim_{x \to 2^+} \frac{1}{x-2} = +\infty$; la función diverge, así que **$x = 2$ es asíntota vertical**.

> [!example] 📋 Planteamiento
>
> Determina la asíntota horizontal de $f(x) = \frac{2x+1}{x-3}$.
>
> > [!success]- ✅ Solución
> >
> > Los grados del numerador y del denominador son iguales ($1$), así que el límite en el infinito es el cociente de los coeficientes principales: $2/1 = 2$.
> >
> > **Asíntota horizontal: $y = 2$.** Comprobación: $\lim_{x \to \infty} \frac{2x+1}{x-3} = 2$.

> [!example] 📋 Planteamiento
>
> Calcula la asíntota oblicua de $f(x) = \frac{x^2+1}{x}$.
>
> > [!success]- ✅ Solución
> >
> > Como $\text{grado}(P) > \text{grado}(Q)$ no hay asíntota horizontal, así que se calcula la oblicua:
> >
> > $$m = \lim_{x \to \infty} \frac{x^2+1}{x^2} = 1, \qquad b = \lim_{x \to \infty} \left[\frac{x^2+1}{x} - x\right] = \lim_{x \to \infty} \frac{1}{x} = 0.$$
> >
> > **Asíntota oblicua: $y = x$** (la hipérbola se acerca a esa recta).

> [!example] 📋 Planteamiento
>
> Encuentra las intersecciones con ambos ejes de $f(x) = \frac{x^2-1}{x^2-4}$.
>
> > [!success]- ✅ Solución
> >
> > **Eje $y$:** $f(0) = \frac{-1}{-4} = \frac{1}{4}$ → punto $(0, 1/4)$.
> >
> > **Eje $x$:** resolver $x^2 - 1 = 0$ → $x = \pm 1$ → puntos $(-1, 0)$ y $(1, 0)$.
> >
> > Los tres puntos quedan marcados antes de trazar la curva.

> [!example] 📋 Planteamiento
>
> Describe el comportamiento en el infinito de $f(x) = e^{-x}$.
>
> > [!success]- ✅ Solución
> >
> > Cuando $x \to +\infty$, $e^{-x} = 1/e^x \to 0$: la función se acerca al eje $y = 0$ por arriba.
> >
> > Cuando $x \to -\infty$, $e^{-x} \to +\infty$: la curva se dispara hacia arriba a la izquierda.
> >
> > En conjunto tiene **asíntota horizontal $y = 0$ solo por la derecha**, y crece sin cota por la izquierda.

> [!example] 📋 Planteamiento
>
> Aplica el checklist completo a $f(x) = \frac{x^2-1}{x^2-4}$ y resume el resultado.
>
> > [!success]- ✅ Solución
> >
> > **Algebraico:** $D = \mathbb{R} - \{-2, 2\}$; intersecciones $(0, 1/4)$ y $(\pm 1, 0)$; la función es par (dominio y expresión simétricos).
> >
> > **Derivadas:** $f'(x) = \frac{-6x}{(x^2-4)^2}$, punto crítico en $x = 0$ con máximo local $f(0) = 1/4$; $f''(x) = \frac{6(3x^2+4)}{(x^2-4)^3}$ nunca se anula, así que la concavidad cambia solo en las asíntotas.
> >
> > **Asintótico:** verticales $x = \pm 2$; horizontal $y = 1$ (grados iguales).
> >
> > Con esos datos la gráfica queda completamente determinada.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Determino el dominio de una función racional, radical o logarítmica aplicando sus restricciones.
> - [ ] Encuentro las intersecciones con los ejes resolviendo $f(0)$ y $f(x) = 0$.
> - [ ] Clasifico una asíntota como vertical, horizontal u oblicua según el límite que corresponda.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo asíntotas horizontales por comparación de grados en una función racional.
> - [ ] Construyo la asíntota oblicua de una función con $m$ y $b$ cuando no hay horizontal.
> - [ ] Describo el comportamiento en el infinito de polinomios, racionales y funciones elementales.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Ejecuto el checklist de tres bloques de principio a fin en una función dada.
> - [ ] Dibujo una gráfica justificada respetando dominio, asíntotas, extremos y concavidad.
> - [ ] Verifico mi gráfica final contra el proceso de diez pasos y corrijo lo que falte.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: guía de graficación y asíntotas.
> - R. Larson, *Cálculo* (Cengage), cap. 3: análisis gráfico de funciones.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 4: el resumen de cómo se dibuja una función.
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — el cálculo de asíntotas visto desde los límites.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — el bloque de derivadas del checklist.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — concavidad e inflexiones.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué tres familias de asíntotas existen y qué límite las define?::Vertical ($x = a$) cuando $\lim_{x \to a} f(x) = \pm\infty$; horizontal ($y = L$) cuando $\lim_{x \to \pm\infty} f(x) = L$; oblicua ($y = mx + b$) cuando no hay horizontal y existen $m$ y $b$.
> - ¿Cómo se halla la asíntota horizontal de una racional?::Comparando grados: menor → $y = 0$; iguales → cociente de coeficientes principales; mayor → no hay.
> - ¿Cuál es la condición de las asíntotas verticales?::Que $x = a$ no esté en el dominio y que la función diverja allí ($\pm\infty$), verificando los límites laterales.
> - ¿Qué bloquees tiene el checklist de graficación?::Tres: algebraico (dominio, intersecciones, simetría), con derivadas (críticos, extremos, concavidad) y asintótico (asíntotas e infinito).
> - ¿Cuántas intersecciones con el eje $y$ puede tener una función?::Como máximo una, el punto $(0, f(0))$; con el eje $x$ puede tener varias, los ceros de la función.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — el cálculo de asíntotas con límites, antes de las derivadas.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — crecimiento, decrecimiento y extremos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — la segunda derivada y la forma de la curva.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — cuando del análisis se pasa a maximizar y minimizar.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — pendientes y tangentes leídas en la gráfica.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — una vez dibujada la función, el área debajo de la curva.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero el cálculo de dominio y asíntotas con las funciones de los ejercicios hasta que salga automático.
> - Después continúa con [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|Monotonía y Puntos Críticos]] para añadir el bloque de derivadas.
> - Cuando domines el análisis completo, integra todo en [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|Problemas de Optimización]].
> - En cada ejercicio, escribe antes de dibujar **qué ítem del checklist estás calculando y qué te aporta**.

---

**Tags:** #MATG1045 #unidad5 #analisis-funciones #dominio #rango #asintotas #intersecciones #comportamiento-infinito #graficacion #checklist

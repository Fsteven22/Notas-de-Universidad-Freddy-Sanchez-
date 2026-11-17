---
dg-publish: true
tags: [MATG1045, unidad6, asintotas-en-integrales-definidas, asíntotas, integrales-definidas, integrales-impropias, discontinuidades, límites, convergencia, análisis-funciones, cálculo-integral]
---

# 🎯 Asíntotas en Integrales Definidas

## 🎯 Introducción

> [!info] 💡 Qué es una asíntota y por qué le importa a la integral
>
> Una **asíntota** es una línea recta que una función se aproxima pero nunca toca. En integrales definidas, las asíntotas crean **situaciones especiales** que transforman integrales propias en **integrales impropias**: si el integrando se dispara en un extremo o dentro del intervalo porque ahí vive una asíntota vertical, el teorema fundamental del cálculo ya no se aplica directamente y hay que escribir **límites**.
>
> **Por qué importa:** una asíntota es la **señal de cambio de método**, no solo un dato de la gráfica. Reconocerla a tiempo evita que evalúes con sustitución una integral que en realidad es impropia y que la calculadora te devuelva un número sin sentido.
>
> **Ejemplo:** con $\int_0^{1} \frac{1}{\sqrt{1-x^2}}\,dx$, la asíntota vertical en $x = 1$ obliga a escribir $\lim_{t \to 1^-} \int_0^t \frac{1}{\sqrt{1-x^2}}\,dx$, que converge a $\frac{\pi}{2}$.

> [!tip] 🎯 Las tres asíntotas que aparecen en integrales
>
> - **Vertical** — $x = a$ donde $\lim_{x \to a} f(x) = \pm\infty$ (la que vuelve impropia a la integral).
> - **Horizontal** — $y = L$ donde $\lim_{x \to \pm\infty} f(x) = L$ (importa en integrales con límite infinito).
> - **Oblicua** — $y = mx + b$ donde $\lim_{x \to \pm\infty} [f(x) - (mx + b)] = 0$.
>
> **Por qué importa:** solo la vertical convierte a $\int_a^b f$ en impropia **sobre intervalo finito**; las otras dos gobiernan el comportamiento cuando el límite es infinito.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Asíntota y transformación en integral impropia
>
> Sea $f$ definida en $[a,b]$. Entonces:
>
> 1. **Asíntota vertical en un extremo:** si $f \to \pm\infty$ cuando $x \to b^-$,
> $$\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx$$
> (y análogamente en el extremo inferior con $t \to a^+$).
>
> 2. **Asíntota vertical en el interior:** si $f \to \pm\infty$ cuando $x \to c$ con $a < c < b$,
> $$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$$
> donde **ambas deben converger** para que converge la total.
>
> 3. **Transformación a impropia:** $\int_a^b f(x)\,dx$ se convierte en integral impropia en cuanto hay una asíntota de $f$ en $[a,b]$ o en el rango de integración.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Asíntotas_en_Integrales_Definidas_01.svg]]
>
> **Se lee así:** una caja central "asíntotas → integrales impropias" que abre tres ramas horizontales, una por cada tipo: vertical ($x = a$ con límite $\pm\infty$), horizontal ($y = L$ con límite $L$) y oblicua ($y = mx + b$ con $f - (mx+b) \to 0$). Solo la rama vertical continúa hacia un recuadro final de advertencia: si hay singularidad o asíntota en $[a,b]$, la integral es impropia y requiere límites.
>
> **Por qué importa:** el esquema te da el diagnóstico completo: mira el tipo de asíntota y de ahí sale la transformación que toca aplicar. Es el paso que decide si el ejercicio se resuelve sustituyendo o con límite.
>
> **Ejemplo:** $\int_0^{\pi/2} \tan x\,dx$ tiene asíntota vertical en $x = \pi/2$, así que se escribe $\lim_{t \to (\pi/2)^-} \int_0^t \tan x\,dx$.

---

## 🔬 Asíntotas verticales

> [!tip] 📊 Los tres casos de asíntota vertical
>
> **Caso 1 · Extremo:** si $f$ tiene asíntota vertical en $x = b$, $\int_a^b f = \lim_{t \to b^-} \int_a^t f$.
>
> **Caso 2 · Interior:** si la asíntota está en $x = c$ con $a < c < b$, $\int_a^b f = \int_a^c f + \int_c^b f$, y **ambas deben converger**.
>
> **Caso 3 · Múltiples asíntotas:** si hay varias, **cada segmento se analiza por separado**; la integral converge solo si todos los tramos convergen.
>
> **Por qué importa:** la dirección del límite ($t \to b^-$ vs. $t \to a^+$) la determina el **lado por el que la función existe**; elegir mal deja una integral que la calculadora evalúa sin quejarse y que no es la original.
>
> **Ejemplo (Caso 1):** $f(x) = \frac{1}{\sqrt{1-x^2}}$ tiene asíntota vertical en $x = 1$:
> $$\int_0^1 \frac{dx}{\sqrt{1-x^2}} = \lim_{t \to 1^-} \Big[\arcsin x\Big]_0^t = \lim_{t \to 1^-} \arcsin t = \frac{\pi}{2}$$
> — la integral **converge** a $\pi/2$ aunque el integrando se dispare.

> [!warning] ⚠️ Asíntota en el interior: el caso que más se falla
>
> Con la asíntota en $x = 0$ dentro de $[-1,1]$:
>
> $$\int_{-1}^{1} \frac{1}{x^2}\,dx = \int_{-1}^{0} \frac{1}{x^2}\,dx + \int_{0}^{1} \frac{1}{x^2}\,dx$$
>
> y la segunda pieza ya diverge:
> $$\int_{0}^{1} x^{-2}\,dx = \lim_{t \to 0^+} \Big[-\frac{1}{x}\Big]_t^1 = \lim_{t \to 0^+} \Big(-1 + \frac{1}{t}\Big) = +\infty$$
>
> **Respuesta:** la integral total **diverge**, aunque la primera pieza también lo haga por el mismo motivo.
>
> **Por qué importa:** sin partir en el punto problemático, la sustitución directa en $[-1,1]$ da un resultado falso (aparece $0$, por simetría). La discontinuidad interior **siempre** exige su propio corte.

---

## 🌊 Asíntotas horizontales y oblicuas

> [!tip] 📐 Asíntota horizontal $y = L$ con $L \neq 0$
>
> Si $\lim_{x \to \infty} f(x) = L \neq 0$, entonces $\int_a^{\infty} f(x)\,dx$ **diverge**: para $x$ grande, $f$ se queda entre $\frac{L}{2}$ y $\frac{3L}{2}$, así que crece sin cota.
>
> **Ejemplo:** $\int_1^{\infty} \frac{2x^2 + 1}{x^2 + 3}\,dx$:
> $$\lim_{x \to \infty} \frac{2x^2+1}{x^2+3} = \lim_{x \to \infty} \frac{2 + 1/x^2}{1 + 3/x^2} = 2 \neq 0$$
> — como $f \to 2$, la integral **diverge** hacia $+\infty$.
>
> **Por qué importa:** el test "$f \to 0$ es necesario" cierra la mitad de los ejercicios de una línea: si el límite no es cero, ni te molestes en integrar.

> [!info] 📐 Asíntota horizontal $y = 0$ y oblicua $y = mx + b$
>
> **Si $f \to 0$**, la integral **puede** converger o diverger: toca aplicar los criterios ($p$, comparación, razón). $\int_1^{\infty} \frac{1}{x^2}$ converge; $\int_1^{\infty} \frac{1}{x}$ diverge — mismo límite cero, distinto destino.
>
> **Si la asíntota es oblicua** ($y = mx + b$ con $m \neq 0$), se determina con:
>
> 1. $m = \lim_{x \to \infty} \frac{f(x)}{x}$
> 2. $b = \lim_{x \to \infty} [f(x) - mx]$
>
> y como $f(x) - (mx + b) \to 0$, el integrando se comporta como $mx + b$ para $x$ grande: si $(m,b) \neq (0,0)$, $\int_a^{\infty} f$ **diverge**. La diferencia $f - (mx+b)$ tiende a 0 y solo mide **qué tan rápido** se acerca a la asíntota (el residuo), no salva a la integral.
>
> **Ejemplo:** $f(x) = \sqrt{x^2 + x} - x$. Racionalizando:
> $$f(x) = \frac{x}{\sqrt{x^2+x} + x} = \frac{1}{\sqrt{1 + 1/x} + 1} \xrightarrow[x \to \infty]{} \frac{1}{2}$$
> — su asíntota es la **horizontal** $y = \frac{1}{2} \neq 0$, así que $\int_1^{\infty} (\sqrt{x^2+x} - x)\,dx$ **diverge** (el integrando se queda cerca de $\frac{1}{2}$).
>
> **Por qué importa:** el paso de racionalizar es el que revela el límite real; sin él, "raíz menos $x$" parece que se cancela y no es así.

---

## 🧭 Estrategia de análisis

> [!success] 🎯 Descomposición y veredicto
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Asíntotas_en_Integrales_Definidas_02.svg]]
>
> **Se lee así:** un árbol que arranca con el ejemplo $\int_1^{\infty} \frac{x + \sin x}{x^2}\,dx$, baja a la descomposición $\frac{1}{x} + \frac{\sin x}{x^2}$ y se bifurca: la rama de $\int_1^{\infty} \frac{1}{x}$ llega al recuadro "diverge" y la de $\int_1^{\infty} \frac{\sin x}{x^2}$ al recuadro "converge por comparación con $1/x^2$". Las dos flechas se reencuentran en la caja final: suma de una divergente con una convergente, la integral total **diverge**.
>
> **Por qué importa:** el esquema te obliga a separar el integrando en partes y a juzgar cada una por separado antes de sumar. Evita el error típico de declarar convergente la integral porque una de las partes lo es, y muestra **por qué** una pieza divergente arruina el total.
>
> **Ejemplo:** con la misma integral, la rama de $\frac{1}{x}$ diverge, la de $\frac{\sin x}{x^2}$ converge por comparación con $\frac{1}{x^2}$ y la caja final concluye divergencia total.

> [!tip] 📋 Técnicas de evaluación
>
> 1. **Identificar todas las asíntotas** en el intervalo de integración.
> 2. **Determinar el tipo** de asíntota (vertical, horizontal, oblicua).
> 3. **Transformar a integral impropia** según el tipo, con el límite correcto.
> 4. **Aplicar los criterios de convergencia** apropiados (comparación, $p$, Leibniz).
> 5. **Evaluar los límites** cuidadosamente (L'Hôpital cuando haga falta).
> 6. **Verificar el resultado** con análisis gráfico si es posible.
>
> **Por qué importa:** los pasos 1 y 3 son los que más se saltan; sin ellos el resto del ejercicio se construye sobre una integral mal planteada.

> [!warning] 🚨 Errores frecuentes y verificaciones
>
> **Errores:**
>
> - **No identificar asíntotas en el interior:** verificar **todo** el intervalo $[a,b]$.
> - **Confundir tipos de asíntotas:** vertical vs. horizontal vs. oblicua.
> - **No transformar correctamente:** seguir tratando una integral propia como si lo fuera.
> - **Evaluar mal los límites:** las direcciones laterales ($t \to c^-$, $t \to c^+$) son cruciales.
> - **No separar las discontinuidades:** múltiples asíntotas requieren múltiples cortes.
>
> **Verificaciones:**
>
> - **Análisis gráfico:** visualizar la función y sus asíntotas.
> - **Límites laterales:** comprobar el comportamiento desde ambos lados.
> - **Criterios de convergencia:** aplicar el test que corresponda a cada tramo.
> - **Cálculo paso a paso:** no saltar pasos en la evaluación de límites.
>
> **Por qué importa:** los tres primeros errores son de **planteamiento** y ninguno los detecta la calculadora; se previenen con la lista de técnicas, paso por paso.

---

## 📋 Tabla de referencia rápida

> [!tip] 📋 Tipos de asíntota y sus consecuencias
>
> | Tipo de asíntota | Ubicación | Transformación | Análisis requerido |
> |---|---|---|---|
> | Vertical | $x = a$ (extremo) | $\lim_{t \to a^-} \int f$ | Criterio $p$ para discontinuidades |
> | Vertical | $x = c$ (interior) | Separar en dos integrales | Ambas partes deben converger |
> | Horizontal | $y = L \neq 0$ | $\int_a^{\infty} f$ | Siempre diverge |
> | Horizontal | $y = 0$ | $\int_a^{\infty} f$ | Aplicar criterios de convergencia |
> | Oblicua | $y = mx + b$ | Residuo $f - (mx+b) \to 0$ | Diverge si $(m,b) \neq (0,0)$ |
>
> **Por qué importa:** con esta tabla decides la transformación y el criterio en un vistazo; es el resumen de toda la nota en cinco filas.

> [!info] 📚 Funciones de referencia con asíntotas
>
> - $\tan x$: asíntota vertical en $x = \frac{\pi}{2} + n\pi$.
> - $\frac{1}{x}$: vertical en $x = 0$, horizontal en $y = 0$.
> - $\frac{1}{x^2}$: vertical en $x = 0$.
> - $\ln x$: vertical en $x = 0$.
> - $e^x$: horizontal en $y = 0$ cuando $x \to -\infty$.
> - $\arctan x$: horizontales en $y = \pm\frac{\pi}{2}$.
> - $\frac{1}{\sqrt{1-x^2}}$: verticales en $x = \pm 1$.
>
> **Por qué importa:** son las funciones con las que se construyen los ejercicios tipo; reconocer su asíntota de memoria ahorra el paso de análisis.

> [!success] 🧠 Mnemotecnia: ASÍNTOTAS
>
> **A** — Analizar discontinuidades primero.
> **S** — Separar intervalos con asíntotas múltiples.
> **Í** — Identificar tipo: vertical, horizontal, oblicua.
> **N** — No olvidar los límites laterales.
> **T** — Transformar a integral impropia.
> **O** — Oblicuas requieren análisis del residuo.
> **T** — Testing con criterios de convergencia.
> **A** — Aproximación gráfica para visualizar.
> **S** — Siempre verificar el resultado final.
>
> **Por qué importa:** la letra **N** (límites laterales) es la que decide la dirección del cálculo; equivocarse ahí invierte el resultado sin avisar.

> [!tip] 🎯 Puntos clave para recordar
>
> 1. **Identificación completa:** buscar **todas** las asíntotas en $[a,b]$.
> 2. **Transformación automática:** asíntotas → integrales impropias con límite.
> 3. **Tipos distintos:** cada tipo de asíntota requiere un análisis diferente.
> 4. **Límites cuidadosos:** las direcciones laterales son cruciales.
> 5. **Separación obligatoria:** las múltiples discontinuidades se analizan por partes.
> 6. **Convergencia total:** **todas** las partes deben converger.
> 7. **Verificación gráfica:** visualizar ayuda a confirmar resultados.
>
> **Por qué importa:** los siete puntos son la lista de comprobación antes de entregar cualquier ejercicio con asíntotas.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^{1} \frac{1}{\sqrt{1-x^2}}\,dx$ o justifica su convergencia.
>
> > [!success]- ✅ Solución
> >
> > **Tipo:** asíntota vertical en el extremo superior $x = 1$.
> >
> > $$\int_0^1 \frac{dx}{\sqrt{1-x^2}} = \lim_{t \to 1^-} \int_0^t \frac{dx}{\sqrt{1-x^2}} = \lim_{t \to 1^-} \Big[\arcsin x\Big]_0^t = \lim_{t \to 1^-} \arcsin t$$
> >
> > **Límite:** $\arcsin 1 = \frac{\pi}{2}$.
> >
> > **Respuesta:** converge a $\frac{\pi}{2}$.
> >
> > **Cuidado:** el límite va $t \to 1^-$ porque es el extremo **superior** ✓

> [!example] 📋 Planteamiento
>
> Decide si converge $\int_0^{\pi/2} \tan x\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Tipo:** $\tan x$ tiene asíntota vertical en $x = \frac{\pi}{2}$ (extremo superior).
> >
> > $$\int_0^{\pi/2} \tan x\,dx = \lim_{t \to (\pi/2)^-} \Big[-\ln|\cos x|\Big]_0^t = \lim_{t \to (\pi/2)^-} \big(-\ln|\cos t| + \ln 1\big)$$
> >
> > **Límite:** $\cos t \to 0^+$, luego $-\ln|\cos t| \to +\infty$.
> >
> > **Respuesta:** la integral **diverge** por la asíntota vertical ✓

> [!example] 📋 Planteamiento
>
> ¿Converge $\int_{-1}^{1} \frac{1}{x^2}\,dx$?
>
> > [!success]- ✅ Solución
> >
> > **Tipo:** asíntota vertical en el **interior** $x = 0$; hay que partir:
> > $$\int_{-1}^{1} \frac{1}{x^2}\,dx = \int_{-1}^{0} \frac{1}{x^2}\,dx + \int_{0}^{1} \frac{1}{x^2}\,dx$$
> >
> > **Segunda pieza:** $\int_0^1 x^{-2}\,dx = \lim_{t \to 0^+} \big[-\frac{1}{x}\big]_t^1 = \lim_{t \to 0^+} \big(-1 + \frac{1}{t}\big) = +\infty$.
> >
> > **Respuesta:** diverge — una sola pieza divergente arrastra al total.
> >
> > **Trampa:** sin partir en $0$, la simetría da $0$ "de gratis", que es falso ✓

> [!example] 📋 Planteamiento
>
> ¿Converge $\int_1^{\infty} \frac{2x^2 + 1}{x^2 + 3}\,dx$?
>
> > [!success]- ✅ Solución
> >
> > **Límite del integrando:**
> > $$\lim_{x \to \infty} \frac{2x^2+1}{x^2+3} = \lim_{x \to \infty} \frac{2 + 1/x^2}{1 + 3/x^2} = 2$$
> >
> > **Test:** como $f \to 2 \neq 0$, para $x$ grande vale $f(x) \geq 1$, así que $\int_a^{\infty} f \geq \int_a^{\infty} 1\,dx = \infty$.
> >
> > **Respuesta:** la integral **diverge** hacia $+\infty$ — ni siquiera hace falta integrar ✓

> [!example] 📋 Planteamiento
>
> ¿Converge $\int_1^{\infty} \frac{x + \sin x}{x^2}\,dx$?
>
> > [!success]- ✅ Solución
> >
> > **Descomposición:** $\frac{x + \sin x}{x^2} = \frac{1}{x} + \frac{\sin x}{x^2}$.
> >
> > **Pieza 1:** $\int_1^{\infty} \frac{1}{x}\,dx = \lim_{t \to \infty} \big[\ln x\big]_1^t = \infty$ → **diverge**.
> >
> > **Pieza 2:** $0 \leq \left|\frac{\sin x}{x^2}\right| \leq \frac{1}{x^2}$ y $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ converge → por comparación **converge**.
> >
> > **Veredicto:** divergente + convergente = **diverge** el total.
> >
> > **Importancia:** es el caso del diagrama de descomposición: juzgar cada rama por separado antes de sumar ✓

> [!example] 📋 Planteamiento
>
> ¿Converge $\int_1^{\infty} \left(\sqrt{x^2 + x} - x\right)\,dx$?
>
> > [!success]- ✅ Solución
> >
> > **Racionalizar:** $\sqrt{x^2+x} - x = \frac{(\sqrt{x^2+x}-x)(\sqrt{x^2+x}+x)}{\sqrt{x^2+x}+x} = \frac{x}{\sqrt{x^2+x}+x} = \frac{1}{\sqrt{1+1/x}+1}$.
> >
> > **Límite:** $\lim_{x \to \infty} \frac{1}{\sqrt{1+1/x}+1} = \frac{1}{2} \neq 0$ — la asíntota es la horizontal $y = \frac{1}{2}$.
> >
> > **Test:** para $x$ grande, $\sqrt{x^2+x} - x \geq \frac{1}{4}$, así que la integral crece al menos como $\frac{1}{4}x$.
> >
> > **Respuesta:** la integral **diverge**.
> >
> > **Cuidado:** la diferencia de crecientes **no** se cancela: tiende a $\frac{1}{2}$, y con límite distinto de cero no hay convergencia ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Reconozco las tres asíntotas (vertical, horizontal, oblicua) y sé cuál vuelve impropia a la integral.
> - [ ] Escribo el límite correcto para una asíntota en cada extremo, con la dirección lateral adecuada.
> - [ ] Parto una integral con discontinuidad interior y juzgo cada tramo por separado.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Demuestro la divergencia de una integral con $f \to L \neq 0$ sin llegar a integrar.
> - [ ] Descompongo un integrando en partes y aplico el criterio adecuado a cada una antes de concluir.
> - [ ] Determino la asíntota oblicua o horizontal de $f$ calculando $m$ y $b$ con sus límites.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo integrales con múltiples asíntotas dividiendo el intervalo en todos los tramos necesarios.
> - [ ] Combino racionalización, comparación y criterios $p$ para decidir convergencia sin valor exacto.
> - [ ] Verifico cada resultado con el comportamiento gráfico y con las integrales de referencia.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 8.8: integrales impropias y discontinuidades.
> - G. Strang, *Calculus* (Wellesley-Cambridge): integrales impropias y límites.
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — las asíntotas vistas en límites, el prerrequisito directo.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — discontinuidades y límites laterales.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — los tipos de impropiedad en detalle.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — los criterios con los que se juzga cada tramo.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — la herramienta con la que se evalúan todos los límites de la nota.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué convierte a una integral propia en impropia?::Una asíntota vertical del integrando en el intervalo o en sus extremos: hay que escribir límites en lugar de sustituir.
> - ¿Cómo tratas una asíntota en el extremo superior $b$?::$\int_a^b f = \lim_{t \to b^-} \int_a^t f$; en el extremo inferior el límite es $t \to a^+$.
> - ¿Y una asíntota en el interior $c$?::Partir en $\int_a^c f + \int_c^b f$ y exigir que **ambas** converjan; si una diverge, diverge el total.
> - ¿Qué pasa si $f \to L \neq 0$ en el infinito?::$\int_a^{\infty} f$ diverge: para $x$ grande, $f$ se queda entre $L/2$ y $3L/2$.
> - ¿Puede converger una integral con $f \to 0$?::Puede converger ($\int_1^{\infty} 1/x^2$) o diverger ($\int_1^{\infty} 1/x$): el límite cero es necesario pero no suficiente; hay que aplicar criterios.
> - ¿Qué indica una asíntota oblicua $y = mx + b$ en $\int_a^{\infty} f$?::Que $f \approx mx + b$ para $x$ grande: si $(m,b) \neq (0,0)$ la integral diverge; el residuo $f - (mx+b) \to 0$ solo mide qué tan rápido se acerca.
> - ¿Converge $\int_0^1 \frac{dx}{\sqrt{1-x^2}}$?::Sí: asíntota vertical en $x = 1$ y $\lim_{t \to 1^-} \arcsin t = \frac{\pi}{2}$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — los tipos de impropiedad y el método LÍMITE.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — cómo se juzga cada tramo con comparación y criterio $p$.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/03 - Teoremas de Comparación y Desigualdades|03 - Teoremas de Comparación y Desigualdades]] — las desigualdades que acotan cada parte.
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — el análisis de asíntotas previo a la integral.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] — qué hacer cuando la integral no se puede evaluar a mano.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — el análisis completo que detecta las asíntotas antes de integrar.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: una asíntota en extremo que converge y otra que diverge, el esqueleto de todo lo demás.
> - Después pasa al 3 y al 4, donde entran la discontinuidad interior partida en dos y el test del límite distinto de cero.
> - Cierra con el 5 y el 6: descomposición de integrandos y racionalización para encontrar la asíntota real.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|Criterios de Convergencia y Divergencia]] para aplicar los criterios completos a cada tramo.

---

**Tags:** #MATG1045 #unidad6 #asintotas-en-integrales-definidas #asíntotas #integrales-definidas #integrales-impropias #discontinuidades #límites #convergencia #análisis-funciones #cálculo-integral

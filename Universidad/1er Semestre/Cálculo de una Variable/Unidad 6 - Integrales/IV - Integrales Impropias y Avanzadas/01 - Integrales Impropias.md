---
dg-publish: true
tags: [MATG1045, unidad6, integrales-impropias, tipo-i, tipo-ii, integrales-mixtas, convergencia, divergencia, comparacion, series, probabilidad, transformadas]
---

# 🚀 Integrales Impropias

## 🎯 Introducción

> [!info] 💡 Qué es una integral impropia
>
> Una **integral impropia** es una integral definida que no encaja en las hipótesis del teorema fundamental: o el **intervalo es infinito** (un límite o ambos valen $\pm\infty$), o el **integrando se dispara** en algún punto del intervalo (discontinuidad infinita), o ambas cosas a la vez. No se "calcula sustituyendo": se convierte en un **límite de integrales definidas** y la pregunta de fondo deja de ser "¿cuánto?" para ser "**¿existe?**" — la integral **converge** si ese límite es finito y **diverge** si no.
>
> **Por qué importa:** sin integrales impropias no existen las series infinitas, las transformadas de Laplace y de Fourier, ni la probabilidad continua: las tres se apoyan en que $\int_a^b f$ puede tener sentido aunque $a$, $b$ o $f$ se porten mal. En examen el formato siempre es el mismo: separar cada impropiedad, escribir el límite y decidir.
>
> **Ejemplo:** $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ converge, pero $\int_1^{\infty} \frac{1}{x}\,dx$ diverge: el integrando casi idéntico cambia de destino solo por el exponente.

> [!tip] 🎯 Dónde aparece en la carrera
>
> - **Análisis de series:** la integral test es la conexión directa entre integrales y series.
> - **Transformadas:** Laplace y Fourier son integrales impropias con parámetro.
> - **Probabilidad:** toda densidad de probabilidad debe integrar 1 en $(-\infty,\infty)$.
> - **Física:** campos, densidades de energía y distribuciones de velocidades.
> - **Ecuaciones diferenciales:** soluciones definidas en todo $[0,\infty)$.
>
> **Por qué importa:** el día de mañana el infinito lo pondrá el modelo (tiempo que no termina, soporte infinito) y la técnica la pones tú.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Integral impropia y sus tres tipos
>
> Sea $f$ integrable en todo subintervalo propio de su dominio. La integral $\int_a^b f(x)\,dx$ es **impropia** cuando:
>
> 1. **Tipo I** — uno o ambos límites son infinitos:
>
> $$\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx \qquad \int_{-\infty}^b f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx$$
>
> y con los dos infinitos, para **cualquier** $c \in \mathbb{R}$: $\int_{-\infty}^{\infty} f = \int_{-\infty}^{c} f + \int_{c}^{\infty} f$, donde **ambas deben converger**.
>
> 2. **Tipo II** — discontinuidad infinita en un extremo o dentro: si $f \to \infty$ en $x = a$, $\int_a^b f = \lim_{t \to a^+} \int_t^b f$; si se dispara en un interior $c$, $\int_a^b f = \int_a^c f + \int_c^b f$ con **ambas convergiendo**.
>
> 3. **Mixta** — conviven límites infinitos y discontinuidades en la misma integral.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integrales_Impropias_01.svg]]
>
> **Se lee así:** un cuadro raíz "Integrales Impropias" despliega tres subgrafos de rectángulos. El primero clasifica los **tipos** (I con límites infinitos, II con discontinuidades y mixto). El segundo describe la **evaluación**: límites, los dos desenlaces posibles (convergencia y divergencia) y los criterios de comparación. El tercero agrupa las **aplicaciones**: probabilidad, transformadas, física matemática y series infinitas.
>
> **Por qué importa:** el mapa te da el algoritmo completo en un vistazo: primero el **tipo** (qué rama), después la **evaluación** (límite o criterio) y al final la **aplicación**. Si un ejercicio se te resiste, casi siempre es porque estás evaluando por la rama equivocada.
>
> **Ejemplo:** $\int_0^{\infty} \frac{1}{\sqrt{x}}\,dx$ cae en la rama mixta: discontinuidad en 0 y límite superior infinito, así que se separa en dos integrales y cada una se juzga por su cuenta.

> [!warning] ⚠️ La regla de oro de las mixtas
>
> Cada impropiedad necesita **su propio límite**: un extremo infinito, un extremo que se dispara o un punto interior nunca se mezclan en la misma expresión. La integral se parte en tantas como problemas tenga, y **converge solo si todas convergen**.
>
> **Por qué importa:** una sola pieza divergente arrastra a toda la integral. Evaluarlas de golpe es el error que más se repite, porque sale "casi bien" en la calculadora.
>
> **Ejemplo:** $\int_0^{\infty} \frac{1}{\sqrt{x}}\,dx = \int_0^1 \frac{1}{\sqrt{x}}\,dx + \int_1^{\infty} \frac{1}{\sqrt{x}}\,dx$: la primera converge ($p = 1/2 < 1$) pero la segunda diverge ($p = 1/2 \leq 1$), así que la original **diverge**.

---

## 📐 Tipo I — Límites de integración infinitos

> [!tip] 📊 Los tres casos del Tipo I
>
> **Caso 1 · Límite superior infinito:** $\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx$
>
> **Caso 2 · Límite inferior infinito:** $\int_{-\infty}^b f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx$
>
> **Caso 3 · Ambos infinitos:** $\int_{-\infty}^{\infty} f(x)\,dx = \int_{-\infty}^{c} f(x)\,dx + \int_{c}^{\infty} f(x)\,dx$ con $c$ arbitrario y ambas convergiendo.
>
> **Por qué importa:** en el caso 3 el punto de corte $c$ es **libre** (0 es el más cómodo), pero la convergencia **no**: si una de las dos partes escapa, la integral no existe aunque la otra salga perfecta.
>
> **Ejemplo:** $\int_{-\infty}^{\infty} e^{-|x|}\,dx = \int_{-\infty}^{0} e^{x}\,dx + \int_{0}^{\infty} e^{-x}\,dx = 1 + 1 = 2$.

> [!tip] 📈 Ejemplo 1 · Convergente
>
> **Evalúa** $\int_1^{\infty} \frac{1}{x^2}\,dx$.
>
> **Paso 1:** escribir el límite: $\lim_{t \to \infty} \int_1^t x^{-2}\,dx$.
>
> **Paso 2:** antiderivada: $\lim_{t \to \infty} \left[-\frac{1}{x}\right]_1^t = \lim_{t \to \infty} \left(-\frac{1}{t} + 1\right)$.
>
> **Paso 3:** el límite: $0 + 1 = 1$.
>
> **Respuesta:** la integral **converge** a $1$.
>
> **Por qué importa:** $t \to \infty$ hace que $1/t \to 0$; ese paso es donde la integral "deja de crecer" y por eso converge.

> [!tip] 📈 Ejemplo 2 · Divergente
>
> **Evalúa** $\int_1^{\infty} \frac{1}{x}\,dx$.
>
> **Paso 1:** límite: $\lim_{t \to \infty} \int_1^t x^{-1}\,dx$.
>
> **Paso 2:** antiderivada: $\lim_{t \to \infty} \big[\ln x\big]_1^t = \lim_{t \to \infty} (\ln t - \ln 1)$.
>
> **Paso 3:** $\lim_{t \to \infty} \ln t = \infty$.
>
> **Respuesta:** la integral **diverge**.
>
> **Por qué importa:** el logaritmo tiende a infinito, aunque lo haga lentamente. Convergencia no es "crece despacio": es "**el límite existe y es finito**".

> [!tip] 📈 Ejemplo 3 · Integral Tipo I con parámetro
>
> **Evalúa** $\int_0^{\infty} x e^{-ax}\,dx$ con $a > 0$.
>
> **Paso 1:** límite y partes: con $u = x$, $dv = e^{-ax}dx$ (entonces $du = dx$, $v = -\frac{1}{a}e^{-ax}$),
> $$\int_0^{\infty} x e^{-ax}\,dx = \lim_{t \to \infty} \left[-\frac{x}{a}e^{-ax}\Big|_0^t + \frac{1}{a}\int_0^t e^{-ax}\,dx\right] = \lim_{t \to \infty} \left[-\frac{x}{a}e^{-ax} - \frac{1}{a^2}e^{-ax}\right]_0^t$$
>
> **Paso 2:** sustituir los extremos: $\lim_{t \to \infty} \left(-\frac{t}{a}e^{-at} - \frac{1}{a^2}e^{-at} + \frac{1}{a^2}\right)$.
>
> **Paso 3:** como $\lim_{t \to \infty} te^{-at} = 0$ y $\lim_{t \to \infty} e^{-at} = 0$ para $a > 0$ (L'Hôpital en el primero): $0 - 0 + \frac{1}{a^2}$.
>
> **Respuesta:** converge a $\dfrac{1}{a^2}$.
>
> **Por qué importa:** aquí el límite de $te^{-at}$ es el paso que decide; sin él la integral parece divergir. Es el ejemplo típico de "integrales que convergen a pesar de que el parámetro se escapa".

---

## 🕳️ Tipo II — Discontinuidades infinitas

> [!tip] 📊 Los tres casos del Tipo II
>
> **Caso 1 · Discontinuidad en el extremo inferior:** si $f$ se dispara en $x = a$,
> $$\int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx$$
>
> **Caso 2 · Discontinuidad en el extremo superior:** si $f$ se dispara en $x = b$,
> $$\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx$$
>
> **Caso 3 · Discontinuidad interior:** si $f$ se dispara en $c \in (a,b)$,
> $$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx \quad \text{(ambas deben converger)}$$
>
> **Por qué importa:** el límite se toma **hacia el punto problemático por el lado donde la función existe** ($a^+$, $b^-$). Elegir el lado equivocado deja una integral que la calculadora evalúa sin quejarse y que no es la original.
>
> **Ejemplo:** en $\int_0^1 \frac{1}{\sqrt{x}}\,dx$ la discontinuidad está en $x = 0$, así que el límite va $t \to 0^+$.

> [!tip] 📈 Ejemplo 1 · Convergente
>
> **Evalúa** $\int_0^1 \frac{1}{\sqrt{x}}\,dx$.
>
> **Análisis:** $f(x) = x^{-1/2}$ tiende a $\infty$ en $x = 0$ (Tipo II).
>
> **Paso 1:** $\lim_{t \to 0^+} \int_t^1 x^{-1/2}\,dx$.
>
> **Paso 2:** $\lim_{t \to 0^+} \big[2\sqrt{x}\big]_t^1 = \lim_{t \to 0^+} (2 - 2\sqrt{t})$.
>
> **Paso 3:** $2 - 0 = 2$.
>
> **Respuesta:** la integral **converge** a $2$.
>
> **Por qué importa:** aunque el integrando es infinito en el extremo, el **área** finita que queda debajo es finita: la discontinuidad no mata a la integral.

> [!tip] 📈 Ejemplo 2 · Divergente
>
> **Evalúa** $\int_0^1 \frac{1}{x}\,dx$.
>
> **Paso 1:** $\lim_{t \to 0^+} \int_t^1 x^{-1}\,dx$.
>
> **Paso 2:** $\lim_{t \to 0^+} \big[\ln x\big]_t^1 = \lim_{t \to 0^+} (0 - \ln t)$.
>
> **Paso 3:** $-\ln t \to \infty$ cuando $t \to 0^+$.
>
> **Respuesta:** la integral **diverge**.
>
> **Por qué importa:** es el mismo par $1/x^2$ vs. $1/x$ del Tipo I, pero ahora peleando en el otro extremo: cerca de 0 el logaritmo se escapa.

---

## ⚖️ Integrales mixtas

> [!tip] 🔀 El método de separación
>
> 1. **Listar** todos los problemas: extremos infinitos y puntos donde $f$ se dispara.
> 2. **Partir** la integral en cada uno de ellos (si un punto interior $c$ está en problemas, ese corte es obligatorio).
> 3. **Escribir un límite por problema**, sin mezclarlos.
> 4. **Convergencia conjunta:** la integral original converge **solo si** todas las piezas convergen.
>
> **Por qué importa:** el paso 2 es el que se olvida. Si dejas un $0$ problemático junto a un $\infty$ en la misma integral, el límite no está bien definido y todo lo demás cae.
>
> **Ejemplo:** $\int_0^{\infty} \frac{1}{\sqrt{x}(1+x)}\,dx = \int_0^1 \frac{1}{\sqrt{x}(1+x)}\,dx + \int_1^{\infty} \frac{1}{\sqrt{x}(1+x)}\,dx$ — la primera es Tipo II en 0 y la segunda es Tipo I en $\infty$.

> [!info] 🔍 Decidir convergencia sin calcular
>
> En la práctica no hace falta integrar: basta mirar el **comportamiento** del integrando en cada tramo.
>
> - Cerca de $x = 0$: $\frac{1}{\sqrt{x}(1+x)} \sim \frac{1}{\sqrt{x}}$, y $\int_0^1 \frac{1}{\sqrt{x}}$ converge ($p = 1/2 < 1$).
> - Para $x \to \infty$: $\frac{1}{\sqrt{x}(1+x)} \sim \frac{1}{x^{3/2}}$, y $\int_1^{\infty} \frac{1}{x^{3/2}}$ converge ($p = 3/2 > 1$).
>
> **Por qué importa:** esta es la vida real del examen: casi nunca te piden el valor exacto de una mixta, te piden **converge o diverge**, y la comparación con una $p$-serie se resuelve de un vistazo.

---

## 🔍 Criterios de convergencia

> [!info] 📋 Criterio de comparación directa
>
> Sean $0 \leq f(x) \leq g(x)$ para $x \geq a$:
>
> - Si $\int_a^{\infty} g(x)\,dx$ **converge**, entonces $\int_a^{\infty} f(x)\,dx$ **converge** (lo pequeño está cubierto).
> - Si $\int_a^{\infty} f(x)\,dx$ **diverge**, entonces $\int_a^{\infty} g(x)\,dx$ **diverge** (lo grande arrastra).
>
> **Por qué importa:** la comparación va **en un solo sentido** hacia cada conclusión. Invertirla es el fallo clásico: que $f \leq g$ y $g$ diverja **no** dice nada sobre $f$.
>
> **Ejemplo:** para $x \geq 1$ vale $x^2 + 1 \geq x^2$, luego $\frac{1}{x^2+1} \leq \frac{1}{x^2}$; como $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ converge, también converge $\int_1^{\infty} \frac{1}{x^2+1}\,dx$.

> [!info] 📋 Criterio de comparación límite
>
> Si $f$ y $g$ son positivas y
>
> $$\lim_{x \to \infty} \frac{f(x)}{g(x)} = L, \qquad 0 < L < \infty$$
>
> entonces $\int_a^{\infty} f$ y $\int_a^{\infty} g$ **convergen o divergen juntas**: para $x$ grande, $f$ y $g$ se comportan como múltiplos el uno del otro.
>
> **Por qué importa:** es el criterio que salva cuando la desigualdad no se ve: basta comparar los **grados dominantes** del numerador y el denominador.
>
> **Ejemplo:** $\int_1^{\infty} \frac{2x+1}{x^3 - x + 1}\,dx$: los grados dan $\frac{2x}{x^3} = \frac{2}{x^2}$, y $\int_1^{\infty} \frac{2}{x^2}\,dx$ converge, así que la original **converge**.

---

## 📊 Tablas de referencia (las $p$-series)

> [!tip] 📊 Integrales de referencia — Tipo I
>
> | Integral | Converge si | Valor (cuando converge) |
> |---|---|---|
> | $\int_1^{\infty} \frac{1}{x^p}\,dx$ | $p > 1$ | $\frac{1}{p-1}$ |
> | $\int_1^{\infty} \frac{1}{x(\ln x)^p}\,dx$ | $p > 1$ | $\frac{1}{p-1}$ |
> | $\int_1^{\infty} e^{-ax}\,dx$ | $a > 0$ | $\frac{1}{a}$ |
> | $\int_0^{\infty} e^{-ax^2}\,dx$ | $a > 0$ | $\frac{1}{2}\sqrt{\frac{\pi}{a}}$ |
> | $\int_0^{\infty} x e^{-ax}\,dx$ | $a > 0$ | $\frac{1}{a^2}$ |
>
> **Por qué importa:** la primera fila es la madre de todas: cualquier convergencia en el infinito se resuelve, al final, contra $1/x^p$ con $p > 1$.

> [!tip] 📊 Integrales de referencia — Tipo II
>
> | Integral | Converge si | Valor (cuando converge) |
> |---|---|---|
> | $\int_0^1 \frac{1}{x^p}\,dx$ | $p < 1$ | $\frac{1}{1-p}$ |
> | $\int_0^1 x^p\,dx$ | $p > -1$ | $\frac{1}{p+1}$ |
>
> **Por qué importa:** cerca de 0 manda la **izquierda** de la regla: con $p < 1$ el área cabe. El caso límite $p = 1$ da $\ln$, que diverge en los dos extremos.

> [!tip] 🧠 Mnemotecnia: la regla de los $p$
>
> - En el **infinito** ($\int_1^{\infty} \frac{1}{x^p}$): **$p$ grande converge** ($p > 1$), $p \leq 1$ diverge.
> - En el **cero** ($\int_0^1 \frac{1}{x^p}$): **$p$ pequeño converge** ($p < 1$), $p \geq 1$ diverge.
>
> Frase: "**en infinito $p$ grande converge; en cero $p$ pequeño converge**".
>
> **Por qué importa:** con esa frase decides cualquier $p$-serie en dos segundos, y es exactamente lo que la mayoría de los ejercicios de convergencia te piden.

> [!success] 🎭 Método "LÍMITE" para evaluar
>
> **L** — **Localiza** el problema: ¿infinito o discontinuidad?
> **Í** — **Identifica** el tipo: I, II o mixto.
> **M** — **Modifica** la integral escribiendo el límite correspondiente.
> **I** — **Integra**: encuentra la antiderivada.
> **T** — **Toma** el límite hacia el valor problemático.
> **E** — **Evalúa**: si el límite existe y es finito → converge; si no → diverge.
>
> **Por qué importa:** el orden importa: los dos primeros pasos son de análisis y los que evitan rehacer el ejercicio entero cuando te equivocas de tipo.

---

## 🌐 Aplicaciones

> [!note] 🎲 En probabilidad
>
> **Distribución exponencial:** $f(x) = \lambda e^{-\lambda x}$ para $x \geq 0$, con $$\int_0^{\infty} \lambda e^{-\lambda x}\,dx = 1.$$
>
> **Distribución normal:** $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$, con $$\int_{-\infty}^{\infty} f(x)\,dx = 1.$$
>
> **Por qué importa:** que una función sea densidad de probabilidad **es** una integral impropia que converge a 1. Si diverge, no hay probabilidad que repartir.

> [!note] ⚡ En física y transformadas
>
> **Transformada de Laplace:** $\mathcal{L}\{f(t)\} = \int_0^{\infty} f(t)\,e^{-st}\,dt$.
>
> **Energía de una partícula:** $E = \int_0^{\infty} \frac{1}{2}mv^2\,\rho(v)\,dv$, donde $\rho(v)$ es la distribución de velocidades.
>
> **Transformada de Fourier:** $\hat{f}(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt$, con la condición de convergencia $\int_{-\infty}^{\infty} |f(t)|\,dt < \infty$.
>
> **Por qué importa:** esas integrales existen **solo si** la integral impropia converge. La condición de integrabilidad absoluta es la que decide si una señal se puede transformar.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco fallos típicos
>
> 1. **No identificar todas las impropiedades.** *Mal:* ver solo el infinito y pasar por alto una discontinuidad. *Bien:* examinar **tanto** los extremos **como** el dominio del integrando.
> 2. **No separar las mixtas.** *Mal:* un solo límite para dos problemas. *Bien:* un límite por impropiedad; cada punto problemático tiene su propia integral.
> 3. **Evaluar mal los límites.** *Mal:* sustituir $\infty$ a ciegas. *Bien:* formas indeterminadas y L'Hôpital cuando haga falta.
> 4. **Confundir convergencia con valor.** *Mal:* "converge" no significa que el área sea grande o pequeña. *Bien:* convergencia = el límite **existe y es finito**.
> 5. **Mal usar los criterios de comparación.** *Mal:* invertir el sentido de la desigualdad. *Bien:* exigir $0 \leq f \leq g$ y recordar hacia qué lado va cada conclusión.
>
> **Por qué importa:** los tres primeros son de **planteamiento** y ninguno los detecta la calculadora; se previenen con el método LÍMITE, paso por paso.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Evalúa $\int_1^{\infty} \frac{1}{x^2}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Tipo:** I (límite superior infinito).
> >
> > $$\int_1^{\infty} \frac{1}{x^2}\,dx = \lim_{t \to \infty} \int_1^t x^{-2}\,dx = \lim_{t \to \infty} \Big[-\frac{1}{x}\Big]_1^t = \lim_{t \to \infty} \Big(-\frac{1}{t} + 1\Big) = 1$$
> >
> > **Respuesta:** converge a $1$.
> >
> > **Control:** coincide con la fila de la tabla ($p = 2 > 1$, valor $\frac{1}{p-1} = 1$) ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_1^{\infty} \frac{1}{x}\,dx$ y explica por qué la anterior sí converge y esta no.
>
> > [!success]- ✅ Solución
> >
> > $$\int_1^{\infty} \frac{1}{x}\,dx = \lim_{t \to \infty} \big[\ln x\big]_1^t = \lim_{t \to \infty} \ln t = \infty$$
> >
> > **Respuesta:** diverge.
> >
> > **Comparación:** el exponente $p = 1$ está justo en la frontera: $p = 2 > 1$ converge y $p = 1 \leq 1$ diverge. La regla de los $p$ resuelve las dos de un vistazo ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^1 \frac{1}{\sqrt{x}}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Tipo:** II, discontinuidad infinita en $x = 0$.
> >
> > $$\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{t \to 0^+} \int_t^1 x^{-1/2}\,dx = \lim_{t \to 0^+} \big[2\sqrt{x}\big]_t^1 = 2 - 0 = 2$$
> >
> > **Respuesta:** converge a $2$.
> >
> > **Control:** $p = 1/2 < 1$ en el extremo cero → converge, y la tabla da $\frac{1}{1-p} = \frac{1}{1/2} = 2$ ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^4 \frac{1}{\sqrt{4-x}}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Tipo:** II, discontinuidad en $x = 4$ (extremo superior).
> >
> > $$\int_0^4 (4-x)^{-1/2}\,dx = \lim_{t \to 4^-} \int_0^t (4-x)^{-1/2}\,dx$$
> >
> > Con $u = 4-x$ (es decir $du = -dx$, límites de $4$ a $4-t$):
> >
> > $$= \lim_{t \to 4^-} \int_{4-t}^{4} u^{-1/2}\,du = \lim_{t \to 4^-} \big[2\sqrt{u}\big]_{4-t}^{4} = 4 - 0 = 4$$
> >
> > **Respuesta:** converge a $4$.
> >
> > **Cuidado:** el límite va $t \to 4^-$ porque es el extremo **superior**; con $t \to 4^+$ la integral saldría al revés ✓

> [!example] 📋 Planteamiento
>
> Decide si converge $\int_1^{\infty} \frac{2x+1}{x^3 - x + 1}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Criterio:** comparación límite con $g(x) = \frac{2x}{x^3} = \frac{2}{x^2}$.
> >
> > $$\lim_{x \to \infty} \frac{(2x+1)/(x^3 - x + 1)}{2/x^2} = \lim_{x \to \infty} \frac{(2x+1)\,x^2}{2(x^3 - x + 1)} = 1$$
> >
> > Como $0 < 1 < \infty$, ambas integrales tienen el mismo comportamiento.
> >
> > $\int_1^{\infty} \frac{2}{x^2}\,dx = 2$ converge ($p = 2 > 1$).
> >
> > **Respuesta:** la integral **converge**.
> >
> > **Por qué no directa:** la antiderivada de $\frac{2x+1}{x^3-x+1}$ no es sencilla; el criterio decide sin integrar ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^{\infty} \frac{1}{\sqrt{x}(1+x)}\,dx$ (mixta).
>
> > [!success]- ✅ Solución
> >
> > **Separación:** $\int_0^1 \frac{1}{\sqrt{x}(1+x)}\,dx + \int_1^{\infty} \frac{1}{\sqrt{x}(1+x)}\,dx$ (problema en 0 y problema en $\infty$).
> >
> > **Parte 1 (Tipo II):** cerca de 0, $\frac{1}{\sqrt{x}(1+x)} \sim \frac{1}{\sqrt{x}}$, y $\int_0^1 \frac{1}{\sqrt{x}}$ converge ($p = 1/2 < 1$).
> >
> > **Parte 2 (Tipo I):** para $x$ grande, $\frac{1}{\sqrt{x}(1+x)} \sim \frac{1}{x^{3/2}}$, y $\int_1^{\infty} \frac{1}{x^{3/2}}$ converge ($p = 3/2 > 1$).
> >
> > **Valor exacto (opcional):** con $x = t^2$, $dx = 2t\,dt$:
> > $$\int_0^{\infty} \frac{2t\,dt}{t(1+t^2)} = \int_0^{\infty} \frac{2}{1+t^2}\,dt = \big[2\arctan t\big]_0^{\infty} = 2\cdot\frac{\pi}{2} = \pi$$
> >
> > **Respuesta:** converge a $\pi$.
> >
> > **Por qué importa:** las dos partes convergen **y** el valor sale limpio: es el ejercicio que combina los dos tipos en uno solo ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Reconozco si una integral es impropia por Tipo I, Tipo II o mixta, mirando límites y dominio.
> - [ ] Escribo el límite correcto para cada caso, incluido el corte arbitrario de $\int_{-\infty}^{\infty}$.
> - [ ] Aplico la regla de los $p$ para decidir convergencia de una $p$-serie en dos segundos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo integrales mixtas separando cada impropiedad y exigiendo que todas converjan.
> - [ ] Uso el criterio de comparación directa respetando el sentido de la desigualdad.
> - [ ] Aplico el criterio de comparación límite comparando los grados dominantes.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro la convergencia de $\int_0^{\infty} \frac{1}{\sqrt{x}(1+x)}\,dx$ sin tabla, y calculo su valor con una sustitución.
> - [ ] Relaciono la integral impropia con la prueba de integrales de series y con las transformadas.
> - [ ] Verifico que una función es densidad de probabilidad comprobando que integra 1 en todo su soporte.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 8.8: improper integrals y su convergencia.
> - G. Strang, *Calculus* (Wellesley-Cambridge): improper integrals y comparación con series.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — aditividad y comparación, la base de los criterios.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el marco que estas integrales se salen.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — los criterios llevados al extremo con series.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/03 - Teoremas de Comparación y Desigualdades|03 - Teoremas de Comparación y Desigualdades]] — la maquinaria de comparación en detalle.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — la herramienta con la que se evalúa cada límite.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué hace que una integral sea impropia?::Que el intervalo es infinito (Tipo I), que el integrando tiene discontinuidad infinita (Tipo II), o ambas (mixta).
> - ¿Cómo se evalúa una integral impropia?::Convirtiéndola en límite de integrales definidas, integrando primero y tomando el límite después; converge si el límite existe y es finito.
> - ¿Qué exige $\int_{-\infty}^{\infty} f$?::Partirla en $\int_{-\infty}^{c} f + \int_{c}^{\infty} f$ con $c$ arbitrario, y que **ambas** converjan.
> - ¿Cuándo converge $\int_1^{\infty} \frac{1}{x^p}\,dx$?::Cuando $p > 1$ (valor $\frac{1}{p-1}$); con $p \leq 1$ diverge.
> - ¿Cuándo converge $\int_0^1 \frac{1}{x^p}\,dx$?::Cuando $p < 1$ (valor $\frac{1}{1-p}$); con $p \geq 1$ diverge.
> - ¿Qué dice el criterio de comparación límite?::Si $f,g > 0$ y $\lim_{x\to\infty} f/g = L \in (0,\infty)$, las dos integrales convergen o divergen juntas.
> - ¿Cómo se demuestra la convergencia de una mixta?::Separando cada impropiedad en su propio límite y exigiendo que todas las piezas converjan.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/III - Integrales Definidas/02 - Integral de Funciones por Tramos|02 - Integral de Funciones por Tramos]] — la aditividad del intervalo con la que se separan las mixtas.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — los mismos criterios aplicados a series.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/03 - Teoremas de Comparación y Desigualdades|03 - Teoremas de Comparación y Desigualdades]] — la comparación y las desigualdades con demostración.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/04 - Asíntotas en Integrales Definidas|04 - Asíntotas en Integrales Definidas]] — dónde se esconden las discontinuidades dentro de una integral.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — las técnicas de integración que cada límite necesita.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la idea de área que sobrevive al infinito.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 3: son Tipo I y Tipo II puros, el esqueleto de todo lo demás.
> - Después pasa al 4 y al 5, donde entran el corte interior, la sustitución y los criterios de comparación.
> - Cierra con el 6, la mixta que combina los dos tipos y se resuelve hasta el valor exacto.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|Criterios de Convergencia y Divergencia]] para conectar estos criterios con las series infinitas.

---

**Tags:** #MATG1045 #unidad6 #integrales-impropias #tipo-i #tipo-ii #integrales-mixtas #convergencia #divergencia #comparacion #series #probabilidad #transformadas

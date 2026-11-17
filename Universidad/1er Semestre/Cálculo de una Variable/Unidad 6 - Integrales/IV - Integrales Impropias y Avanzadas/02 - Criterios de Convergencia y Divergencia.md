---
dg-publish: true
tags: [MATG1045, unidad6, criterios-de-convergencia, series, integrales-impropias, convergencia-absoluta, leibniz, criterio-integral, comparacion, dirichlet, abel]
---

# 📘 Criterios de Convergencia y Divergencia

## 🎯 Introducción

> [!info] 💡 La misma pregunta en dos escenarios
>
> "¿Esta suma infinita o esta área infinita tiene destino finito?" — esa es la pregunta de la nota. En **series** ($\sum_{n=1}^{\infty} a_n$) la respuesta la dan los criterios de comparación, razón, raíz, integral y Leibniz; en **integrales impropias** ($\int_a^{\infty} f$) los mismos criterios, adaptados al continuo. Los dos escenarios comparten la estructura: una condición necesaria, una familia de criterios positivos, un caso alternado/oscilatorio y unas integrales/series de referencia que hacen de contraste.
>
> **Por qué importa:** en examen casi nunca se pide integrar o sumar: se pide **decidir convergencia** con el criterio correcto. Elegir mal cuesta el ejercicio entero, y por eso esta nota está organizada como un algoritmo de decisión, no como una lista de fórmulas sueltas.
>
> **Ejemplo:** $\sum_{n=0}^{\infty} \left(\frac{2}{3}\right)^n$ converge a $3$ por razón ($L = 2/3 < 1$), mientras que $\int_1^{\infty} \frac{1}{x}\,dx$ diverge porque su límite es $\infty$.

> [!tip] 🎯 Por qué conviene tenerlos juntos
>
> - Los criterios de **series** y de **integrales** son el mismo método con otro objeto.
> - El **criterio integral** es el puente directo entre los dos mundos.
> - Las **series de referencia** (geométrica, $p$-serie, armónica) funcionan como las **integrales de referencia** ($1/x^p$, $e^{-ax}$).
> - El error más común es invertir las condiciones de $p$ entre el infinito y la discontinuidad.
>
> **Por qué importa:** estudiarlos en paralelo te ahorra la mitad del esfuerzo: lo que sepas de series lo llevas a integrales y al revés.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Serie infinita que converge o diverge
>
> Una **serie infinita** $\sum_{n=1}^{\infty} a_n$ tiene sumas parciales $S_n = \sum_{k=1}^{n} a_k$. La serie **converge** si $S_n$ tiene límite finito:
>
> $$\sum_{n=1}^{\infty} a_n = L \quad \text{si} \quad \lim_{n \to \infty} S_n = L < \infty$$
>
> **Diverge** si las sumas parciales tienden a $\pm\infty$, oscilan sin límite, o simplemente no tienen límite finito. Una **sucesión** $\{a_n\}$ converge a $L$ cuando $\lim_{n \to \infty} a_n = L$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Criterios_de_Convergencia_y_Divergencia_01.svg]]
>
> **Se lee así:** la raíz es una caja de "series infinitas" que se bifurca en dos ramas, convergentes y divergentes. La rama convergente se abre en dos hojas, **convergencia absoluta** y **convergencia condicional**; la divergente se abre en tres, hacia el infinito positivo, el infinito negativo y la oscilación sin límite. Aparte, más abajo, una caja de "casos típicos" apunta a la lista de series ya estudiadas.
>
> **Por qué importa:** el esquema te da el **mapa de desenlaces posibles** antes de aplicar cualquier criterio. No basta con responder "converge": conviene saber **de qué tipo**, porque la condicional cambia de valor al reordenar los términos.
>
> **Ejemplo:** con la geométrica $\sum_{n=0}^{\infty} r^n$, si $|r| < 1$ caes en la hoja de convergencia absoluta y si $|r| \geq 1$ en una de las tres hojas de divergencia.

> [!note] 📋 Definición — Integral impropia que converge o diverge
>
> Una **integral impropia** tiene al menos una de estas características:
>
> **Tipo I — límites infinitos:** $\int_a^{\infty} f = \lim_{t \to \infty} \int_a^t f$, $\int_{-\infty}^b f = \lim_{t \to -\infty} \int_t^b f$ y $\int_{-\infty}^{\infty} f = \int_{-\infty}^{c} f + \int_{c}^{\infty} f$ con ambas convergiendo.
>
> **Tipo II — discontinuidades:** $f$ se dispara en $a$, en $b$ o en un punto interior $c$; por ejemplo $\int_a^b \frac{1}{(x-c)^p}\,dx$ con $a < c < b$.
>
> Converge si el límite existe y es finito; diverge si no.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Criterios_de_Convergencia_y_Divergencia_03.svg]]
>
> **Se lee así:** una caja única de "integral impropia" que se divide en dos ramas, resultados **convergentes** y **divergentes**. La convergente se abre en convergencia absoluta y condicional; la divergente en tres hojas (infinito positivo, infinito negativo y oscilación sin límite). Debajo, aparte, una caja de "casos clásicos" apunta a la lista de tres integrales ya resueltas.
>
> **Por qué importa:** la estructura es **idéntica** a la de las series, así que reutilizas el mismo esquema mental en las dos unidades. Además te obliga a revisar el valor absoluto antes de concluir en una integral oscilatoria.
>
> **Ejemplo:** con $\int_1^{\infty} \frac{1}{x^2}\,dx$ el resultado $1$ te lleva a la hoja de convergencia absoluta, mientras que $\int_1^{\infty} \frac{1}{x}\,dx$ se va a una de las hojas de divergencia.

---

## 🔬 Criterios para series positivas

> [!tip] 📋 Criterios 1 a 3: comparación, límite y razón
>
> **1 · Comparación (directa).** Sean $\sum a_n$ y $\sum b_n$ con $a_n, b_n \geq 0$ y $a_n \leq b_n$ para $n$ suficientemente grande:
> - Si $\sum b_n$ converge $\Rightarrow$ $\sum a_n$ converge.
> - Si $\sum a_n$ diverge $\Rightarrow$ $\sum b_n$ diverge.
>
> **2 · Comparación por límite.** Si $\lim_{n \to \infty} \frac{a_n}{b_n} = L$ con $0 < L < \infty$, las dos series tienen **el mismo comportamiento**.
>
> **3 · Razón (D'Alembert).** Para $\sum a_n$ con $a_n > 0$, sea $L = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$:
> - $L < 1 \Rightarrow$ converge · $L > 1 \Rightarrow$ diverge · $L = 1 \Rightarrow$ **no decide**.
>
> **Por qué importa:** la comparación directa exige **ver** la desigualdad; la por límite solo pide comparar **grados dominantes**, y es la que más se usa en examen. $L = 1$ no es un empate: hay que probar otro criterio.
>
> **Ejemplo:** $\sum \frac{2n+1}{n^3 - 1}$ se compara con $\sum \frac{2}{n^2}$ (grado 1 sobre grado 3 = $1/n^2$), que converge.

> [!tip] 📋 Criterios 4 a 6: raíz, condensación e integral
>
> **4 · Raíz (Cauchy).** $L = \lim_{n \to \infty} \sqrt[n]{a_n}$: $L < 1$ converge, $L > 1$ diverge, $L = 1$ no decide. Es el criterio natural cuando hay **potencias de $n$**.
>
> **5 · Condensación de Cauchy.** Si $a_n \geq a_{n+1} \geq 0$, entonces $\sum_{n=1}^{\infty} a_n$ y $\sum_{k=0}^{\infty} 2^k a_{2^k}$ tienen el **mismo comportamiento**.
>
> **6 · Criterio integral.** Si $f$ es positiva, continua y decreciente en $[1,\infty)$, entonces $\sum_{n=1}^{\infty} f(n)$ y $\int_1^{\infty} f(x)\,dx$ **convergen o divergen juntas**.
>
> **Por qué importa:** el criterio integral es el **puente** entre series e integrales impropias: convierte una suma en un área que ya sabes evaluar. La condensación hace lo propio con sumas "demasiado lentas" como la armónica.
>
> **Ejemplo:** la armónica $\sum \frac{1}{n}$: con el integral, $\int_1^{\infty} \frac{1}{x}\,dx = \lim_{t \to \infty} \ln t = \infty$, así que **diverge**.

> [!success] 🔄 Criterio de Leibniz y convergencia condicional
>
> Para una serie **alternada** $\sum_{n=1}^{\infty} (-1)^{n+1} a_n$ con $a_n > 0$, **converge** si:
>
> 1. $a_n$ es decreciente: $a_{n+1} \leq a_n$;
> 2. $\lim_{n \to \infty} a_n = 0$.
>
> **Absoluta vs. condicional:** si $\sum |a_n|$ converge, la serie es **absolutamente convergente** (y por tanto convergente). Si $\sum |a_n|$ diverge pero $\sum a_n$ converge, es **condicionalmente convergente**.
>
> **Por qué importa:** la absoluta es estable (cualquier reordenamiento conserva el valor); la condicional **no**: un reordenamiento puede cambiarle el valor. Esa es la razón por la que el examen pregunta el tipo, no solo si converge.
>
> **Ejemplo:** la armónica alternada $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$: $1/n$ es decreciente y tiende a 0 → converge por Leibniz; como $\sum \frac{1}{n}$ diverge, converge **condicionalmente** (a $\ln 2$).

> [!info] 🖼️ El árbol de decisión absoluta vs. condicional
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Criterios_de_Convergencia_y_Divergencia_02.svg]]
>
> **Se lee así:** un organigrama con dos rombos de decisión encadenados. La serie parte de una caja rectangular y llega al primer rombo, donde se pregunta si converge la **suma de valores absolutos**: un "sí" lleva a la salida de convergencia absoluta y un "no" pasa al segundo rombo, que pregunta si converge la **serie original**, con dos salidas: convergencia condicional o divergencia.
>
> **Por qué importa:** ese es el **orden de preguntas** que te salva en examen: primero decides si es absoluta y solo después analizas el caso alternado. Te evita aplicar Leibniz a una serie que no cumple las hipótesis y confundir convergencia simple con condicional.
>
> **Ejemplo:** con la armónica alternada, el primer rombo da "no" ($\sum 1/n$ diverge) y el segundo "sí" por Leibniz: condicional a $\ln 2$.

> [!success] 🎯 Criterios avanzados: Dirichlet y Abel
>
> **7 · Dirichlet.** Para $\sum a_n b_n$: si $\{a_n\}$ es monótona con $\lim a_n = 0$ y las sumas parciales de $\sum b_n$ están **acotadas**, la serie converge.
>
> **8 · Abel.** Para $\sum a_n b_n$: si $\{a_n\}$ es monótona y **acotada** y $\sum b_n$ converge, la serie converge.
>
> **Por qué importa:** son los criterios para **productos**: uno de los factores "amortigua" (Dirichlet) o "hereda la convergencia" (Abel). Los verás otra vez en Fourier, donde aparecen productos de senos con coeficientes.
>
> **Ejemplo:** $\sum \frac{\operatorname{sen}(n)}{n}$ converge por Dirichlet: las sumas de $\operatorname{sen}(n)$ están acotadas y $1/n$ es monótona decreciente a 0.

---

## 🧮 Criterios para integrales impropias

> [!tip] 📋 Tipo I (infinito): comparación, límite y criterio $p$
>
> **Comparación directa.** Con $0 \leq f(x) \leq g(x)$ en $[a,\infty)$: si $\int_a^{\infty} g$ converge, $\int_a^{\infty} f$ converge; si $\int_a^{\infty} f$ diverge, $\int_a^{\infty} g$ diverge.
>
> **Comparación por límite.** Con $f, g > 0$ y $\lim_{x \to \infty} \frac{f(x)}{g(x)} = L$:
> - $0 < L < \infty$ → mismo comportamiento;
> - $L = 0$ y $\int g$ converge → $\int f$ converge;
> - $L = \infty$ y $\int g$ diverge → $\int f$ diverge.
>
> **Criterio $p$ (infinito).** $\int_1^{\infty} \frac{1}{x^p}\,dx$ **converge si $p > 1$** (valor $\frac{1}{p-1}$) y diverge si $p \leq 1$.
>
> **Por qué importa:** el criterio por límite con $L = 0$ y $L = \infty$ es el que casi nadie recuerda: son los dos casos donde el comportamiento **no** es el mismo, y hay que leerlo en el sentido correcto.
>
> **Ejemplo:** $\int_1^{\infty} \frac{\operatorname{sen}^2 x}{x^2}\,dx$: como $0 \leq \operatorname{sen}^2 x \leq 1$ vale $0 \leq \frac{\operatorname{sen}^2 x}{x^2} \leq \frac{1}{x^2}$, y $\int_1^{\infty} \frac{1}{x^2} = 1$ converge → la original converge.

> [!tip] 📋 Tipo II (discontinuidad): criterio $p$ y comparación asintótica
>
> **Criterio $p$ (discontinuidad).** Para la discontinuidad en $x = a$: $\int_a^{a+h} \frac{1}{(x-a)^p}\,dx$ **converge si $p < 1$** (valor $\frac{h^{1-p}}{1-p}$) y diverge si $p \geq 1$.
>
> **Comparación local.** Cerca de la discontinuidad $c$, comparar $f$ con $\frac{1}{(x-c)^p}$.
>
> **Comparación asintótica.** Si $f(x) \sim \frac{A}{(x-c)^p}$ cuando $x \to c$ (con $A \neq 0$): converge si $p < 1$, diverge si $p \geq 1$.
>
> **Por qué importa:** los dos criterios $p$ son **opuestos**: en el infinito converge $p > 1$ y en la discontinuidad $p < 1$. Memoria: cerca del problema, el exponente tiene que ser **pequeño** para que el área quepa.
>
> **Ejemplo:** $\int_0^1 \frac{1}{\sqrt{x}}\,dx$ tiene $p = 1/2 < 1$ en la discontinuidad $x = 0$ → converge a $2$.

> [!success] 🎯 Dirichlet, Abel y condensación para integrales
>
> **Dirichlet.** Para $\int_a^{\infty} f(x)g(x)\,dx$: si $F(x) = \int_a^x f$ está **acotada** y $g$ es monótona con $\lim_{x \to \infty} g(x) = 0$, la integral converge.
>
> **Abel.** Si $\int_a^{\infty} f$ converge y $g$ es monótona y acotada, $\int_a^{\infty} fg$ converge.
>
> **Condensación.** Para $f$ positiva y decreciente: $\int_1^{\infty} f(x)\,dx$ y $\sum_{n=0}^{\infty} 2^n f(2^n)$ tienen el mismo comportamiento.
>
> **Por qué importa:** Dirichlet es el criterio que salva las **integrales oscilatorias** como $\int_1^{\infty} \frac{\operatorname{sen} x}{x}\,dx$, cuya antiderivada no se escribe en elementos elementales pero cuya convergencia sí se demuestra de un renglón.
>
> **Ejemplo:** $\int_1^{\infty} \frac{\operatorname{sen} x}{x}\,dx$ converge por Dirichlet ($\int_1^{x} \operatorname{sen} = -\cos x + \cos 1$ acotada, $1/x \downarrow 0$); su valor es $\frac{\pi}{2}$.

> [!info] 🌳 Las cuatro integrales de referencia
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Criterios_de_Convergencia_y_Divergencia_04.svg]]
>
> **Se lee así:** un árbol con una caja raíz y cuatro ramas que se abren a la vez, cada una con su propia caja hija. Tres de esas hojas llevan después un recuadro con la **condición de convergencia** y, cuando corresponde, el **valor** de la integral; la cuarta rama termina directamente en la caja con su resultado. Todas siguen el mismo patrón: identificar la integral, fijar la condición, leer el valor.
>
> **Por qué importa:** esas cuatro son tus **funciones patrón** para comparar. Memorizar sus condiciones evita recalcularlas y permite resolver casi cualquier impropia con comparación directa o por límite.
>
> **Ejemplo:** para decidir si $\int_1^{\infty} \frac{1}{x^p}\,dx$ converge tomas la primera rama y usas $p > 1$; para $\int_0^1 \frac{1}{x^p}\,dx$ exige $p < 1$, justo al revés.

---

## 📊 Tablas resumen

> [!tip] 📋 Los seis criterios de series en una tabla
>
> | Criterio | Condición | Conclusión | Mejor uso |
> |---|---|---|---|
> | Divergencia (término) | $\lim a_n \neq 0$ | Diverge | Verificación inicial, siempre |
> | Comparación | $0 \leq a_n \leq b_n$ | Como $\sum b_n$ | Series similares conocidas |
> | Razón (D'Alembert) | $L = \lim \frac{a_{n+1}}{a_n}$ | $L<1$ conv · $L>1$ div | Factoriales, exponenciales |
> | Raíz (Cauchy) | $L = \lim \sqrt[n]{a_n}$ | $L<1$ conv · $L>1$ div | Potencias de $n$ |
> | Integral | $\int_1^{\infty} f$ | Como la integral | Funciones continuas decrecientes |
> | Leibniz | Alternada, $\downarrow 0$ | Converge | Series alternadas |
>
> **Series de referencia:**
>
> | Serie | Comportamiento |
> |---|---|
> | $\sum r^n$ (geométrica) | Converge si $\|r\| < 1$, suma $\frac{1}{1-r}$ |
> | $\sum \frac{1}{n^p}$ ($p$-serie) | Converge si $p > 1$ |
> | $\sum \frac{1}{n}$ (armónica) | **Diverge** |
> | $\sum \frac{1}{n!}$ | Converge (suma $e - 1$) |
> | $\sum \frac{1}{a^n}$ con $a > 1$ | Converge (geométrica con $r = 1/a$) |
>
> **Por qué importa:** la primera tabla te dice **qué criterio**; la segunda te da el **contraste** contra el que se mide todo. Las dos juntas resuelven el 90 % de los ejercicios de convergencia.

> [!tip] 📋 Los criterios de integrales en una tabla
>
> | Criterio | Tipo | Condición | Uso típico |
> |---|---|---|---|
> | Comparación directa | I y II | $0 \leq f \leq g$ | Funciones evidentemente mayores/menores |
> | Comparación por límite | I y II | $\lim \frac{f}{g} = L$ | Comportamiento asintótico similar |
> | Criterio $p$ (infinito) | I | $\int_1^{\infty} \frac{1}{x^p}$ | Referencia para $x \to \infty$: $p > 1$ |
> | Criterio $p$ (discontinuidad) | II | $\int_a^{a+h} \frac{1}{(x-a)^p}$ | Referencia cerca de la ruptura: $p < 1$ |
> | Dirichlet | I | Acotada × monótona a 0 | Integrales oscilatorias |
> | Abel | I | Convergente × acotada | Productos con una integral conocida |
>
> **Integrales de referencia:**
>
> | Integral | Convergencia | Valor |
> |---|---|---|
> | $\int_1^{\infty} \frac{1}{x^p}\,dx$ | $p > 1$ | $\frac{1}{p-1}$ |
> | $\int_0^1 \frac{1}{x^p}\,dx$ | $p < 1$ | $\frac{1}{1-p}$ |
> | $\int_0^{\infty} e^{-ax}\,dx$ | $a > 0$ | $\frac{1}{a}$ |
> | $\int_{-\infty}^{\infty} e^{-x^2}\,dx$ | Siempre | $\sqrt{\pi}$ |
> | $\int_0^{\infty} \frac{\operatorname{sen} x}{x}\,dx$ | Siempre (Dirichlet) | $\frac{\pi}{2}$ |
>
> **Por qué importa:** aquí está el error de $p$ resuelto de una vez: **en $\infty$ converge $p > 1$; en la discontinuidad, $p < 1$**. Imprimir mentalmente esta tabla evita el fallo que más se repite en el parcial.

---

## 🧠 Estrategia y mnemotecnia

> [!warning] ⚠️ Orden de aplicación para series
>
> 1. **Condición necesaria primero:** si $\lim_{n \to \infty} a_n \neq 0$, la serie **diverge** (término general). No pases a ningún otro criterio.
> 2. **Series con términos positivos:** comparación directa si se ve una mayorante/minorante; razón si hay factoriales o exponenciales; raíz si hay potencias de $n$; criterio integral si la función es conocida y decreciente.
> 3. **Series alternadas:** primero mirar si es absoluta; si no, Leibniz.
> 4. **Productos de sucesiones:** Dirichlet o Abel.
>
> **Errores comunes:** confundir la convergencia de $\{a_n\}$ con la de $\sum a_n$; aplicar el criterio equivocado a la estructura; no verificar las hipótesis; concluir algo cuando el criterio **no decide** ($L = 1$).
>
> **Por qué importa:** el paso 1 se salta en el 70 % de los exámenes y es gratis: un límite distinto de cero cierra el ejercicio en una línea.

> [!warning] ⚠️ Estrategia para integrales impropias
>
> 1. **Identificar el tipo:** ¿infinito (I), discontinuidad (II) o ambos (mixta)?
> 2. **Localizar los puntos problemáticos:** comportamiento asintótico en el infinito, comportamiento local en cada discontinuidad.
> 3. **Separar:** una integral por cada problema; en $\int_{-\infty}^{\infty}$ el punto de corte es obligatorio.
> 4. **Elegir el criterio:** comparación directa si la desigualdad se ve, por límite si solo se ven los grados, $p$ como referencia estándar.
> 5. **Verificar condiciones:** positividad, monotonía, continuidad.
>
> **Precauciones:** determinar **existencia antes que valor**; la convergencia condicional **cambia con reordenamientos**; para integrales simétricas divergentes existe el **valor principal de Cauchy**, que es otra cosa (no lo confundas con convergencia).
>
> **Por qué importa:** "calcular primero y preguntar después" es el error de procedimiento más caro: muchas integrales no tienen valor que calcular.

> [!success] 🧠 Mnemotecnia: CONVERDIV (series)
>
> **C** — Condición necesaria: $\lim a_n = 0$.
> **O** — Orden: divergencia → comparación → razón/raíz.
> **N** — Números de referencia: $p$-serie, geométrica, armónica.
> **V** — Verificar las hipótesis del criterio antes de aplicarlo.
> **E** — Evaluar los límites con cuidado (L'Hôpital cuando haga falta).
> **R** — Razón y raíz para factoriales y exponenciales.
> **D** — Dirichlet y Abel para productos.
> **I** — Integral para funciones continuas y decrecientes.
> **V** — Verificar la convergencia absoluta en las alternadas.
>
> **Por qué importa:** la primera V (verificar hipótesis) y la última V (absoluta) son las dos que separan un 8 de un 10 en la pregunta de criterios.

> [!success] 🧠 Mnemotecnia: IMPROPIA (integrales)
>
> **I** — Identificar el tipo: infinito o discontinuidad.
> **M** — Mayorante para la comparación directa.
> **P** — Criterios $p$: $>1$ en el infinito, $<1$ en la discontinuidad.
> **R** — Referencia: usar las integrales conocidas.
> **O** — Oscilatoria: Dirichlet y Abel.
> **P** — Positivas para comparar sin problema de signos.
> **I** — Intervalos: dividir en partes manejables.
> **A** — Asintótico: el comportamiento en los límites decide.
>
> **Por qué importa:** la letra **P** es la que más se olvida y es exactamente la condición opuesta entre los dos tipos: ahí se gana o se pierde el ejercicio.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> ¿Converge $\sum_{n=0}^{\infty} \left(\frac{3}{4}\right)^n$? Si converge, ¿cuánto vale?
>
> > [!success]- ✅ Solución
> >
> > **Término general:** $a_n = (3/4)^n$, serie geométrica con $r = 3/4$.
> >
> > **Criterio de la razón:** $L = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = \frac{3}{4} < 1$ → converge.
> >
> > **Valor:** $\frac{1}{1 - r} = \frac{1}{1 - 3/4} = 4$.
> >
> > **Respuesta:** converge a $4$.
> >
> > **Control:** es una suma de términos positivos decrecientes; el primer término ya vale 1, así que 4 es razonable ✓

> [!example] 📋 Planteamiento
>
> ¿Converge la serie armónica $\sum_{n=1}^{\infty} \frac{1}{n}$?
>
> > [!success]- ✅ Solución
> >
> > **Condición necesaria:** $\lim_{n \to \infty} \frac{1}{n} = 0$ → no decide; hay que seguir.
> >
> > **Criterio integral:** $f(x) = 1/x$ es positiva, continua y decreciente en $[1,\infty)$, así que la serie y $\int_1^{\infty} \frac{1}{x}\,dx$ tienen el mismo comportamiento.
> >
> > $$\int_1^{\infty} \frac{1}{x}\,dx = \lim_{t \to \infty} \big[\ln x\big]_1^t = \lim_{t \to \infty} \ln t = \infty$$
> >
> > **Respuesta:** la serie **diverge**.
> >
> > **Por qué no razón:** $L = \lim \frac{n}{n+1} = 1$, el criterio no decide. El integral sí ✓

> [!example] 📋 Planteamiento
>
> ¿Converge $\sum_{n=1}^{\infty} \frac{1}{n!}$? Usa el criterio de la razón.
>
> > [!success]- ✅ Solución
> >
> > $$L = \lim_{n \to \infty} \frac{n!}{(n+1)!} = \lim_{n \to \infty} \frac{1}{n+1} = 0 < 1$$
> >
> > **Respuesta:** converge (y su valor es $e - 1$).
> >
> > **Por qué razón:** el factorial no se integra ni se suma a mano; la razón cancela factoriales de un golpe. Es el criterio hecho para esa estructura ✓

> [!example] 📋 Planteamiento
>
> Clasifica la convergencia de $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$.
>
> > [!success]- ✅ Solución
> >
> > **Paso 1 · ¿absoluta?** $\sum |a_n| = \sum \frac{1}{n}$ es la armónica → **diverge** (ejercicio 2).
> >
> > **Paso 2 · ¿converge original?** Es alternada con $a_n = 1/n > 0$: decreciente ✓ y $\lim \frac{1}{n} = 0$ ✓ → converge por **Leibniz**.
> >
> > **Respuesta:** converge **condicionalmente** (a $\ln 2$).
> >
> > **Importancia del tipo:** al reordenar sus términos puede sumar cualquier número; por eso "converge" no basta como respuesta ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^{\infty} e^{-ax}\,dx$ con $a > 0$, o justifica su convergencia si prefieres no integrar.
>
> > [!success]- ✅ Solución
> >
> > **Directo:**
> > $$\int_0^{\infty} e^{-ax}\,dx = \lim_{t \to \infty} \Big[-\frac{1}{a}e^{-ax}\Big]_0^t = \lim_{t \to \infty} \left(-\frac{e^{-at}}{a} + \frac{1}{a}\right) = 0 + \frac{1}{a}$$
> >
> > **Respuesta:** converge a $\frac{1}{a}$ para todo $a > 0$.
> >
> > **Con criterio $p$:** para $x$ grande, $e^{-ax}$ decrece mucho más rápido que cualquier $\frac{1}{x^p}$, así que converge también por comparación con la $p$-serie de $p = 2$ ✓

> [!example] 📋 Planteamiento
>
> Decide la convergencia de $\int_1^{\infty} \frac{\operatorname{sen}^2 x}{x^2}\,dx$ sin calcular su valor.
>
> > [!success]- ✅ Solución
> >
> > **Acotación:** $0 \leq \operatorname{sen}^2 x \leq 1$ para todo $x$, así que $$0 \leq \frac{\operatorname{sen}^2 x}{x^2} \leq \frac{1}{x^2}$$
> >
> > **Integral de referencia:** $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ converge ($p = 2 > 1$).
> >
> > **Conclusión:** por comparación directa, $\int_1^{\infty} \frac{\operatorname{sen}^2 x}{x^2}\,dx$ **converge**.
> >
> > **Por qué no calcular:** la antiderivada de $\frac{\operatorname{sen}^2 x}{x^2}$ no es elemental; el criterio decide sin ella ✓

> [!example] 📋 Planteamiento
>
> ¿Converge $\int_{-2}^{2} \frac{1}{\sqrt[3]{x^2}}\,dx$? (discontinuidad interior en $x = 0$)
>
> > [!success]- ✅ Solución
> >
> > **Tipo:** II, discontinuidad en el interior $x = 0$; hay que partir: $$\int_{-2}^{0} x^{-2/3}\,dx + \int_{0}^{2} x^{-2/3}\,dx$$
> >
> > **Criterio $p$ local:** cerca de 0, $\frac{1}{\sqrt[3]{x^2}} = \frac{1}{|x|^{2/3}}$ con $p = 2/3 < 1$ → **cada parte converge**.
> >
> > **Valor:** $[3x^{1/3}]_{-2}^{0} + [3x^{1/3}]_{0}^{2} = (0 - 3\sqrt[3]{-2}) + (3\sqrt[3]{2} - 0) = 6\sqrt[3]{2}$.
> >
> > **Respuesta:** converge a $6\sqrt[3]{2} \approx 7{,}56$.
> >
> > **Cuidado con el dominio:** sin partir en 0, la calculadora devuelve error o un valor falso; la discontinuidad interior **siempre** exige su propio corte ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico la condición necesaria ($\lim a_n \neq 0$ ⇒ diverge) antes que cualquier otro criterio.
> - [ ] Distingo los criterios de razón, raíz, comparación e integral y sé para qué estructura sirve cada uno.
> - [ ] Recuerdo las condiciones opuestas del criterio $p$: $p > 1$ en el infinito y $p < 1$ en la discontinuidad.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Clasifico una serie como absolutamente, condicionalmente convergente o divergente siguiendo el árbol de decisión.
> - [ ] Uso Leibniz verificando las dos hipótesis (decreciente y límite cero) y no solo la segunda.
> - [ ] Decido la convergencia de una impropia con comparación directa o por límite eligiendo la mayorante correcta.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Aplico el criterio integral como puente entre una serie y su integral impropia asociada.
> - [ ] Reconozco cuándo un producto de series o una integral oscilatoria pide Dirichlet o Abel.
> - [ ] Explico por qué la convergencia condicional no sobrevive a un reordenamiento y qué implica eso en la práctica.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 11.1–11.4: series, prueba de la integral y comparación.
> - J. Stewart, *Cálculo* (Cengage), cap. 8.8: integrales impropias.
> - G. Strang, *Calculus* (Wellesley-Cambridge): series e integrales impropias con el criterio integral.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — los límites de sumas parciales y sucesiones con los que se decide todo.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/03 - Propiedades de la Sumatoria|03 - Propiedades de la Sumatoria]] — las reglas de la notación $\sum$.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — de dónde salen las sumas parciales.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — los tipos de impropiedad en detalle.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice la condición necesaria de convergencia?::Si $\lim_{n \to \infty} a_n \neq 0$ la serie diverge; si el límite es 0, la serie **puede** converger o diverger (no decide).
> - ¿Cuándo aplica el criterio de la razón y cuándo el de la raíz?::Razón cuando hay factoriales o exponenciales; raíz cuando hay potencias de $n$. Los dos: $L<1$ converge, $L>1$ diverge, $L=1$ no decide.
> - ¿Qué es la convergencia condicional?::Que la serie converge pero su versión con valores absolutos diverge (ej.: armónica alternada); al reordenar sus términos puede sumar cualquier número.
> - ¿Cuáles son las hipótesis de Leibniz?::Serie alternada $\sum(-1)^{n+1}a_n$ con $a_n>0$ decreciente y $\lim a_n = 0$.
> - ¿Qué dice el criterio integral?::Si $f$ es positiva, continua y decreciente, $\sum f(n)$ y $\int_1^{\infty} f(x)dx$ convergen o divergen juntas.
> - ¿Cuál es la regla del criterio $p$ en cada tipo?::En el infinito $\int_1^{\infty} 1/x^p$ converge si $p>1$; en la discontinuidad $\int_a^{a+h} 1/(x-a)^p$ converge si $p<1$.
> - ¿Cuándo uso Dirichlet para integrales?::En productos $\int f\cdot g$ donde $\int_a^x f$ está acotada y $g$ es monótona que tiende a 0 (típico: integrales oscilatorias).

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — los tipos de impropiedad y el método LÍMITE.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/03 - Teoremas de Comparación y Desigualdades|03 - Teoremas de Comparación y Desigualdades]] — la maquinaria de desigualdades con demostración.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — límites al infinito, la herramienta de todos los criterios.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/03 - Propiedades de la Sumatoria|03 - Propiedades de la Sumatoria]] — algebra de las sumas parciales.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — las técnicas con las que se integra antes de tomar el límite.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el área que sobrevive cuando el intervalo es infinito.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: uno converge por razón y el otro diverge por integral; son los dos patrones base.
> - Después pasa al 3 y al 4, donde entran la razón con factorial y el árbol absoluta/condicional.
> - Cierra con el 5, 6 y 7: integrales con comparación y una discontinuidad interior partida en dos.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/03 - Teoremas de Comparación y Desigualdades|Teoremas de Comparación y Desigualdades]] para ver las desigualdades con las que se demuestran estos criterios.

---

**Tags:** #MATG1045 #unidad6 #criterios-de-convergencia #series #integrales-impropias #convergencia-absoluta #leibniz #criterio-integral #comparacion #dirichlet #abel

---
dg-publish: true
tags: [MATG1045, unidad6, integral-de-riemann, particiones, sumas-riemann, norma, integrabilidad, geometria-areas]
---

# 🎯 Integral de Riemann

## 🎯 Introducción

> [!info] 💡 Qué es la integral de Riemann
>
> La **integral de Riemann** es la definición formal del área bajo una curva: se construye como el **límite de sumas de rectángulos** cuando el número de subdivisiones crece sin que ninguno sea demasiado ancho.
>
> **Por qué importa:** es la base teórica de toda la materia. A partir de aquí se definir la integral, se demuestra el teorema fundamental (que conecta integral y derivada) y se construyen las técnicas de cálculo.
>
> **Ejemplo:** para $f(x) = x^2$ en $[0, 2]$, la suma por la derecha con 4 subintervalos da $3.75$, con 8 da $3.21$, con 16 da $2.94$… y el límite es $\frac{8}{3} \approx 2.667$.

> [!warning] ⚠️ La confusión que hay que evitar desde el primer día
>
> - **NO** confundas $n \to \infty$ con $\|P\| \to 0$: tener muchos subintervalos no basta; lo que importa es que el **mayor** de ellos sea pequeño.
> - **NO** olvides el factor $\Delta x_i$: cada valor de la función se multiplica por el ancho de su subintervalo.
> - **NO** confundas los índices: en la suma por la izquierda se evalúa en $x_{i-1}$, en la derecha en $x_i$.
>
> **Por qué importa:** el primero es el error conceptual más caro de la unidad; los otros dos son errores de cuenta que se detectan comparando con el valor exacto.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Partición de un intervalo
>
> Una **partición** $P$ del intervalo $[a,b]$ es un conjunto finito de puntos
>
> $$P = \{x_0, x_1, x_2, \ldots, x_n\}$$
>
> con $a = x_0 < x_1 < x_2 < \cdots < x_n = b$.
>
> Los subintervalos $[x_{i-1}, x_i]$ tienen longitud $\Delta x_i = x_i - x_{i-1}$. Si todas las longitudes son iguales ($\Delta x = \frac{b-a}{n}$, con $x_i = a + i\Delta x$) la partición es **regular**; si no, es **irregular**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_01.svg]]
>
> **Se lee así:** como una cadena de cuatro rectángulos que avanza hacia la derecha. Una partición inicial da paso a la acción de agregar puntos de corte, y ese paso produce una partición refinada que, a su vez, desemboca en una mejor aproximación del área. No hay rombos ni ramas: es una secuencia lineal de pasos.
>
> **Por qué importa:** fija qué significa *refinamiento*: no se cambian los puntos antiguos, se añaden más. Te evita creer que al hacer una partición más fina se redefine la anterior, y prepara para entender por qué el límite se toma con $\|P\| \to 0$.
>
> **Ejemplo:** la partición regular $P = \{0, 0.5, 1, 1.5, 2\}$ de $f(x) = x^2$ en $[0,2]$ se refina con $n = 8$, donde $\|P\| = 0.25$ y la suma por la derecha mejora de $3.75$ a $3.21$.

> [!note] 📋 Definición — Norma de una partición
>
> La **norma** (o malla) de una partición $P$ es la longitud de su subintervalo más largo:
>
> $$\|P\| = \max_{1 \le i \le n} \Delta x_i = \max_{1 \le i \le n}(x_i - x_{i-1}).$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_02.svg]]
>
> **Se lee así:** como dos ramas paralelas que comparan una norma grande con una norma pequeña. La rama de la norma grande conduce a subintervalos anchos y termina en una aproximación burda, mientras la rama de la norma pequeña pasa por subintervalos finos, luego por una aproximación precisa, y continúa hasta el límite $\|P\| \to 0$ y la integral exacta.
>
> **Por qué importa:** el diagrama separa dos caminos que a primera vista parecen el mismo: *muchos subintervalos* no es lo mismo que *subintervalos finos*. La precisión la controla $\|P\| \to 0$, no $n \to \infty$.
>
> **Ejemplo:** un error típico es aproximar $\int_0^2 x^2 dx$ con $n = 1000$ subintervalos desiguales: la suma sigue lejos de $\frac{8}{3}$ si el subintervalo más largo no se encoge.

> [!note] 📋 Definición — Integral de Riemann
>
> Una función $f$ es **Riemann integrable** en $[a,b]$ si existe un número $I$ tal que para todo $\varepsilon > 0$ existe $\delta > 0$ con la propiedad:
>
> $$\text{Si } \|P\| < \delta, \quad \text{entonces} \quad \left|\sum_{i=1}^{n} f(x_i^*)\,\Delta x_i - I\right| < \varepsilon,$$
>
> para cualquier partición $P$ de $[a,b]$ y cualquier elección de puntos $x_i^* \in [x_{i-1}, x_i]$. En ese caso:
>
> $$\int_a^b f(x)\,dx = I = \lim_{\|P\| \to 0} \sum_{i=1}^{n} f(x_i^*)\,\Delta x_i.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_03.svg]]
>
> **Se lee así:** como un diagrama con un rombo de decisión en el centro. Una partición de norma pequeña alimenta el cálculo de la suma de Riemann, y el rombo pregunta si la norma ya tiende a cero: si la respuesta es sí, las sumas convergen al valor $I$ y ese número queda identificado como la integral de Riemann; si no, la flecha devuelve el proceso a refinar la partición y volver a empezar.
>
> **Por qué importa:** el rombo convierte la definición en un **ciclo de refinamiento**: la integral no se obtiene en un solo intento, sino en la familia de sumas que se estabiliza al hacer $\|P\| \to 0$. Evita tratar la suma de Riemann como un resultado único y definitivo.
>
> **Ejemplo:** con $f(x) = x^2$ en $[0,2]$ se pasa de $R_4 = 3.75$ a $R_8 = 3.21$, $R_{16} = 2.94$ y $R_{32} = 2.80$, acercándose siempre a $\frac{8}{3}$.

---

## 🧮 Suma de Riemann y sus variantes

> [!tip] 🔧 La suma de Riemann
>
> Dada una función $f$ en $[a,b]$ y una partición $P$, la **suma de Riemann** es
>
> $$S(f,P) = \sum_{i=1}^{n} f(x_i^*)\,\Delta x_i,$$
>
> donde $\sum_{i=1}^{n}$ indica sumar desde $i = 1$ hasta $i = n$, $f(x_i^*)$ es el valor de la función en un punto cualquiera $x_i^* \in [x_{i-1}, x_i]$ y $\Delta x_i = x_i - x_{i-1}$ es el ancho del subintervalo.
>
> **Por qué importa:** la multiplicación por $\Delta x_i$ es la que convierte alturas en **áreas**: cada $f(x_i^*)$ es la altura de un rectángulo y $\Delta x_i$ su base.

> [!note] 📝 Las tres sumas según el punto de muestra
>
> | Variante | Punto de muestra | Fórmula |
> |---|---|---|
> | Izquierda | $x_i^* = x_{i-1}$ | $L_n = \sum_{i=1}^{n} f(x_{i-1})\,\Delta x_i$ |
> | Derecha | $x_i^* = x_i$ | $R_n = \sum_{i=1}^{n} f(x_i)\,\Delta x_i$ |
> | Punto medio | $x_i^* = \frac{x_{i-1}+x_i}{2}$ | $M_n = \sum_{i=1}^{n} f\!\left(\frac{x_{i-1}+x_i}{2}\right)\Delta x_i$ |
>
> **Por qué importa:** en una función creciente, las sumas por izquierda acotan por debajo y las de derecha por encima; por eso $\int_a^b f \in [L_n, R_n]$ y el error está acotado por $R_n - L_n$.

> [!info] 🧮 Caso de la partición regular
>
> Con $\Delta x = \frac{b-a}{n}$ y $x_i = a + i\Delta x$:
>
> - **Izquierda:** $L_n = \frac{b-a}{n}\sum_{i=0}^{n-1} f\!\left(a + i\cdot\frac{b-a}{n}\right)$.
> - **Derecha:** $R_n = \frac{b-a}{n}\sum_{i=1}^{n} f\!\left(a + i\cdot\frac{b-a}{n}\right)$.
> - **Punto medio:** $M_n = \frac{b-a}{n}\sum_{i=1}^{n} f\!\left(a + \left(i-\frac{1}{2}\right)\frac{b-a}{n}\right)$.
>
> **Por qué importa:** factorizar $\Delta x$ fuera de la suma es lo que permite escribir la suma en notación sigma compacta, que es lo que se pide en los exámenes.

---

## 🔍 Ejemplo detallado: $f(x) = x^2$ en $[0, 2]$

> [!example] 🔬 Suma por la derecha con $n = 4$
>
> **Paso 1 — partición regular con $n = 4$:**
>
> $$\Delta x = \frac{2-0}{4} = 0.5, \qquad P = \{0, 0.5, 1, 1.5, 2\}, \qquad \|P\| = 0.5.$$
>
> **Paso 2 — suma por la derecha:**
>
> $$R_4 = \sum_{i=1}^{4} f(x_i)\,\Delta x_i = 0.5\big[f(0.5) + f(1) + f(1.5) + f(2)\big]$$
>
> $$= 0.5\big[0.25 + 1 + 2.25 + 4\big] = 0.5 \times 7.5 = 3.75.$$
>
> **Paso 3 — comparación con el valor exacto:**
>
> $$\int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} \approx 2.667, \qquad \text{error} = |3.75 - 2.667| = 1.083.$$
>
> **Mejorando la aproximación:**
>
> | $n$ | $\|P\|$ | $R_n$ | Error |
> |---|---|---|---|
> | 4 | 0.5 | 3.75 | 1.083 |
> | 8 | 0.25 | 3.21 | 0.543 |
> | 16 | 0.125 | 2.94 | 0.273 |
> | 32 | 0.0625 | 2.80 | 0.133 |
>
> **Por qué importa:** el error se reduce a la mitad cada vez que se duplica $n$, y la suma **siempre queda por encima** del valor exacto porque $x^2$ es creciente. Las dos señales —error que cae y cota que se respeta— son las que confirman que vamos bien.

---

## ⚡ Condiciones de integrabilidad

> [!success] ✅ Tres teoremas que garantizan la existencia
>
> 1. **Funciones continuas:** si $f$ es continua en $[a,b]$, entonces es Riemann integrable en $[a,b]$.
> 2. **Funciones monótonas:** si $f$ es monótona en $[a,b]$, entonces es Riemann integrable en $[a,b]$.
> 3. **Discontinuidades finitas:** si $f$ es acotada en $[a,b]$ y tiene un número finito de discontinuidades, entonces es Riemann integrable en $[a,b]$.
>
> **Por qué importa:** estos tres teoremas evitan perder tiempo: antes de construir sumas, se comprueba cuál se cumple.

> [!info] 🖼️ Estrategia de verificación
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_04.svg]]
>
> **Se lee así:** como una escalera de decisiones. Partiendo de una función definida en un intervalo cerrado, el primer rombo pregunta si es continua; si lo es, se llega al rectángulo de integrabilidad, y si no, la flecha baja a un segundo rombo sobre la monotonía. Desde ahí se pasa a un tercer rombo que combina acotación y número finito de discontinuidades, y la última salida advierte que la función puede no ser integrable.
>
> **Por qué importa:** el diagrama da una **estrategia de verificación** antes de calcular: primero continuidad, luego monotonía y por último acotación con discontinuidades finitas. Evita intentar integrar una función que no cumple ninguna condición y perder tiempo en sumas que no convergen.
>
> **Ejemplo:** la función $f(x) = x$ en $[0,1]$ es continua, así que el primer rombo ya responde sí y queda garantizada la integral $\int_0^1 x\,dx = \frac{1}{2}$.

---

## 🧮 Propiedades fundamentales

> [!info] 📋 Propiedades algebraicas
>
> - **Linealidad:** $\int_a^b \big[c_1 f(x) + c_2 g(x)\big]dx = c_1\int_a^b f(x)dx + c_2\int_a^b g(x)dx$.
> - **Aditividad en el dominio:** si $a < c < b$, entonces $\int_a^b f(x)dx = \int_a^c f(x)dx + \int_c^b f(x)dx$.
> - **Comparación:** si $f(x) \le g(x)$ en $[a,b]$, entonces $\int_a^b f(x)dx \le \int_a^b g(x)dx$.
>
> **Por qué importa:** son la versión "integral" de las propiedades de los límites, y son lo que permite calcular integrales de funciones complicadas descomponiéndolas en trozos manejables.

---

## 🌐 Interpretación geométrica

> [!tip] 🏔️ El significado visual
>
> - **Área positiva:** cuando $f(x) \ge 0$, la integral es el área bajo la curva.
> - **Área con signo:** cuando $f$ cambia de signo, se obtiene el **área neta** (lo que está sobre el eje menos lo que está debajo).
> - **Aproximación:** los rectángulos aproximan cada vez mejor la región curva.
>
> **Por qué importa:** la integral es la suma de áreas que se hace cada vez más fina; por eso el signo importa y por eso una función que cruza el eje puede dar cero.

> [!info] 🖼️ De los rectángulos al área
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_05.svg]]
>
> **Se lee así:** como un proceso de construcción con una bifurcación. Desde la función se divide el intervalo en subintervalos y se crean rectángulos; de cada rectángulo salen dos rutas, la altura y la base, que vuelven a juntarse en el área de un rectángulo. Después las áreas se suman, se toma el límite cuando la norma tiende a cero y se llega al área exacta.
>
> **Por qué importa:** el esquema muestra el **puente entre la fórmula y el dibujo**: la integral es una suma de áreas que se hace cada vez más fina. Explica por qué, si $f$ cambia de signo, obtienes un área neta y no un área positiva.
>
> **Ejemplo:** para $f(x) = x - 1$ en $[0,2]$, los rectángulos sobre $[0,1]$ restan y los de $[1,2]$ suman, y el área neta da $\int_0^2 (x-1)dx = 0$.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Errores frecuentes
>
> 1. **Confundir $n \to \infty$ con $\|P\| \to 0$:** no es lo mismo; con 1000 subintervalos desiguales la aproximación puede seguir lejos del valor exacto.
> 2. **Olvidar el $\Delta x_i$:** sin el ancho, la suma no es un área.
> 3. **Índices incorrectos:** en la suma izquierda se evalúa en $x_{i-1}$, en la derecha en $x_i$.
> 4. **Ignorar las discontinuidades:** hay que verificar la integrabilidad antes de calcular.
> 5. **Signos:** si $f(x) < 0$ en parte del intervalo, la integral es menor de lo que sugiere el "área".
>
> **Por qué importa:** los cinco son errores de procedimiento, y el primero es el que más se repite en las evaluaciones.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula las sumas por la izquierda y por la derecha de $f(x) = x^2$ en $[0,2]$ con $n = 4$, y acota la integral.
>
> > [!success]- ✅ Solución
> >
> > $\Delta x = \frac{2}{4} = 0.5$ y $P = \{0, 0.5, 1, 1.5, 2\}$.
> >
> > **Izquierda:** $L_4 = 0.5\,[f(0) + f(0.5) + f(1) + f(1.5)] = 0.5[0 + 0.25 + 1 + 2.25] = 1.75$.
> >
> > **Derecha:** $R_4 = 0.5\,[f(0.5) + f(1) + f(1.5) + f(2)] = 0.5[0.25 + 1 + 2.25 + 4] = 3.75$.
> >
> > Como $x^2$ es creciente en $[0,2]$: $1.75 \le \int_0^2 x^2 dx \le 3.75$.
> >
> > **Respuesta:** $L_4 = 1.75$ y $R_4 = 3.75$; la integral está entre ambos (el valor exacto es $\frac{8}{3} \approx 2.667$).

> [!example] 📋 Planteamiento
>
> Halla la suma por el punto medio de $f(x) = x^2$ en $[0,2]$ con $n = 4$.
>
> > [!success]- ✅ Solución
> >
> > Los puntos de muestra son los puntos medios: $0.25,\ 0.75,\ 1.25,\ 1.75$.
> >
> > $$M_4 = 0.5\,[f(0.25) + f(0.75) + f(1.25) + f(1.75)]$$
> >
> > $$= 0.5\,[0.0625 + 0.5625 + 1.5625 + 3.0625] = 0.5 \times 5.25 = 2.625.$$
> >
> > **Respuesta:** $M_4 = 2.625$, más cercano al valor exacto $\frac{8}{3} \approx 2.667$ que las sumas por los extremos.

> [!example] 📋 Planteamiento
>
> Calcula la norma de la partición $P = \{0, 0.3, 0.9, 1.4, 2\}$ de $[0,2]$.
>
> > [!success]- ✅ Solución
> >
> > Los subintervalos son $[0, 0.3]$, $[0.3, 0.9]$, $[0.9, 1.4]$ y $[1.4, 2]$, con longitudes $0.3$, $0.6$, $0.5$ y $0.6$.
> >
> > La norma es la mayor de ellas:
> >
> > $$\|P\| = \max\{0.3,\ 0.6,\ 0.5,\ 0.6\} = 0.6.$$
> >
> > **Respuesta:** $\|P\| = 0.6$, aunque la partición tiene 4 subintervalos: el subintervalo $[0.3, 0.9]$ es el que manda.

> [!example] 📋 Planteamiento
>
> Verifica si $f(x) = x$ en $[0,1]$ es Riemann integrable y, si lo es, calcula $\int_0^1 x\,dx$ con sumas por la derecha y $n = 4$.
>
> > [!success]- ✅ Solución
> >
> > $f(x) = x$ es continua en $[0,1]$, así que por el primer teorema es Riemann integrable.
> >
> > Con $\Delta x = \frac{1}{4} = 0.25$:
> >
> > $$R_4 = 0.25\,[f(0.25) + f(0.5) + f(0.75) + f(1)] = 0.25\,[0.25 + 0.5 + 0.75 + 1] = 0.25 \times 2.5 = 0.625.$$
> >
> > **Respuesta:** es integrable y $R_4 = 0.625$; el valor exacto es $\int_0^1 x\,dx = \frac{1}{2}$.

> [!example] 📋 Planteamiento
>
> Calcula la suma por el punto medio de $f(x) = x^2$ en $[1,3]$ con partición regular de $n = 4$.
>
> > [!success]- ✅ Solución
> >
> > $\Delta x = \frac{3-1}{4} = 0.5$; los puntos de muestra son $1.25,\ 1.75,\ 2.25,\ 2.75$.
> >
> > $$M_4 = 0.5\,\big[1.5625 + 3.0625 + 5.0625 + 7.5625\big] = 0.5 \times 17.25 = 8.625.$$
> >
> > El valor exacto es $\left[\frac{x^3}{3}\right]_1^3 = \frac{26}{3} \approx 8.667$.
> >
> > **Respuesta:** $M_4 = 8.625$, con un error de apenas $0.042$.

> [!example] 📋 Planteamiento
>
> Explica por qué $\int_0^2 (x-1)\,dx = 0$ aunque la función no sea positiva en todo el intervalo.
>
> > [!success]- ✅ Solución
> >
> > En $[0,1]$ la función es negativa y en $[1,2]$ positiva; por simetría, las dos áreas tienen la misma base (1) y la misma altura máxima (1).
> >
> > Por addividad:
> >
> > $$\int_0^2 (x-1)dx = \int_0^1 (x-1)dx + \int_1^2 (x-1)dx = -\frac{1}{2} + \frac{1}{2} = 0.$$
> >
> > **Respuesta:** la integral es el **área neta**: el rectángulo por debajo del eje del $[0,1]$ cancela exactamente al de encima del $[1,2]$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino partición, refinamiento y norma de una partición.
> - [ ] Escribo la suma de Riemann y las variantes izquierda, derecha y punto medio.
> - [ ] Explico por qué la condición del límite es $\|P\| \to 0$ y no $n \to \infty$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo sumas de Riemann con particiones regulares e irregulares.
> - [ ] Aplico los tres teoremas de integrabilidad antes de calcular una integral.
> - [ ] Uso la aditividad para acotar una integral entre $L_n$ y $R_n$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Interpreto la integral como área neta y detecto el cambio de signo en un intervalo.
> - [ ] Justifico por qué la suma por el punto medio es la mejor de las tres aproximaciones.
> - [ ] Enuncio la definición formal de Riemann integrable con $\varepsilon$ y $\delta$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 5: la integral como límite de sumas.
> - R. Larson, *Cálculo* (Cengage), cap. 5: sumas de Riemann y área bajo la curva.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 7: la definición formal de integral.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/03 - Propiedades de la Sumatoria|03 - Propiedades de la Sumatoria]] — la notación sigma que se usa aquí.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el puente entre esta definición y la derivada.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — las propiedades algebraicas de esta integral.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es la norma de una partición?::El máximo de las longitudes $\Delta x_i$ de sus subintervalos: $\|P\| = \max \Delta x_i$.
> - ¿Por qué el límite se toma con $\|P\| \to 0$ y no con $n \to \infty$?::Porque lo que controla la precisión es el tamaño del **mayor** subintervalo; con muchos subintervalos desiguales la aproximación puede seguir siendo mala.
> - ¿Cómo se define la suma de Riemann?::$S(f,P) = \sum_{i=1}^n f(x_i^*)\,\Delta x_i$, con $x_i^*$ cualquier punto del subintervalo y $\Delta x_i$ su ancho.
> - ¿Qué funciones son Riemann integrables?::Las continuas, las monótonas y las acotadas con un número finito de discontinuidades en $[a,b]$.
> - ¿Qué significa que $f$ cambie de signo en el intervalo?::Que la integral da el **área neta**: lo que hay sobre el eje menos lo que hay debajo, y puede ser cero aunque haya área.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/03 - Propiedades de la Sumatoria|03 - Propiedades de la Sumatoria]] — las sumas que aparecen en la definición.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — las propiedades algebraicas que se deducen de la definición.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la conexión integral-derivada que da sentido a todo esto.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — cómo se calculan las integrales en la práctica.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — la extensión del concepto a intervalos infinitos.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la interpretación geométrica completa.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 a 3: la cuenta de sumas debe salirte sin vacilar.
> - Después el 4, donde se ve por qué la continuidad garantiza la existencia de la integral.
> - Termina con el 6, que es el que fija la idea de área neta y evita confusiones de signo.
> - Cuando lo tengas claro, salta al [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|Teorema Fundamental del Cálculo]]: es donde esta definición se vuelve una herramienta de cálculo.

---

**Tags:** #MATG1045 #unidad6 #integral-de-riemann #particiones #sumas-riemann #norma #integrabilidad #geometria-areas

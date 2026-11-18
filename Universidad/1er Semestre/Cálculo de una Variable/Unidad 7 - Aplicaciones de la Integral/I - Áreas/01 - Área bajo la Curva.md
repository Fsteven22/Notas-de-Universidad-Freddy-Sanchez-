---
dg-publish: true
tags: [MATG1045, unidad7, area-bajo-la-curva, integrales, aplicaciones, areas, geometria-analitica, interpretacion-geometrica]
---

# 📐 Área bajo la Curva

## 🎯 Introducción

> [!info] 💡 Qué son y por qué importan
>
> El **área bajo una curva** es la aplicación geométrica original de la integral definida: si $f(x) \geq 0$ es continua en $[a,b]$, la región entre la gráfica de $f$, el eje $x$ y las rectas $x=a$, $x=b$ mide exactamente $\int_a^b f(x)\,dx$.
>
> **Por qué importa:** convierte una pregunta geométrica ("¿cuánto mide esta región?") en un cálculo mecánico. Volúmenes de revolución, trabajo, probabilidad y longitud de arco se construyen todos sobre esta misma idea de sumar infinitos rectángulos.
>
> **Ejemplo:** el área bajo $f(x) = x^2$ de $x = 0$ a $x = 2$ es $\int_0^2 x^2\,dx = \frac{8}{3}$, que coincide con el límite de las sumas de Riemann cuando $n \to \infty$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — el área como integral definida y el área total cuando la función cambia de signo.
> - **Procedimiento Paso a Paso** — método directo, división por raíces y simetría.
> - **Casos Fundamentales** — función positiva, negativa y mixta.
> - **Ejemplos Resueltos** — del caso base $x^2$ al físico $v(t) = 2t$.
> - **Ejercicios Propuestos** — seis plantillas, una por cada variante.
>
> **Por qué importa:** la única decisión real es "¿la función cambia de signo en el intervalo?": si no, integrar directo; si sí, partir en las raíces y sumar valores absolutos. Todo lo demás es ese criterio aplicado.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Área bajo la curva cuando $f \geq 0$
>
> Si $f(x) \geq 0$ es continua en $[a,b]$, el **área** de la región bajo la curva $y = f(x)$ entre $x = a$ y $x = b$ es:
> $$\text{Área} = \int_a^b f(x)\,dx$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Área_bajo_la_Curva_01.svg]]
>
> **Se lee así:** dos cadenas de rectángulos. La primera avanza en línea recta: función no negativa en $[a,b]$, región bajo la curva, aproximación con rectángulos, suma de Riemann, límite cuando $n \to \infty$ y, al final, la integral definida como área exacta. La segunda parte de la interpretación visual y se bifurca en dos cajas —la base $[a,b]$ y la altura variable $f(x)$— que desembocan juntas en el área.
>
> **Por qué importa:** el diagrama muestra que la integral definida no es un truco algebraico sino el límite de una suma de áreas. Con esa idea justificas el paso de rectángulos a área exacta y evitas el error más común: reportar un resultado negativo como si fuera un área.
>
> **Ejemplo:** el área bajo $f(x) = x^2$ de $x = 0$ a $x = 2$ se obtiene como $\int_0^2 x^2\,dx = \frac{8}{3}$, que coincide con la suma de Riemann al límite.

> [!warning] ⚠️ Condiciones y limitaciones
>
> - **Función no negativa:** $f(x) \geq 0$ en todo $[a,b]$ para que la integral sea el área.
> - **Continuidad:** $f$ debe ser continua (o al menos integrable) en el intervalo.
> - **Límites finitos:** $a$ y $b$ son números reales finitos.
>
> **Por qué importa:** si falla la positividad, la integral da **área con signo** (neta), no área geométrica; si falla la continuidad, hay que partir la integral donde se rompa la función.

> [!note] 📋 Definición — Área total cuando $f$ cambia de signo
>
> Si $f$ cambia de signo en $[a,b]$, con raíces $x_1 < x_2 < \dots < x_k$ que parten el intervalo en trozos de signo constante, el **área geométrica total** es la suma de los valores absolutos:
> $$\text{Área Total} = \sum_i \left|\int_{x_{i-1}}^{x_i} f(x)\,dx\right| \quad \text{con } x_0 = a,\ x_{k+1} = b$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Área_bajo_la_Curva_02.svg]]
>
> **Se lee así:** una caja lleva a un rombo que decide *si la función es no negativa en todo el intervalo*. Del **sí** sale directo a la integral del área; del **no** se encadena una serie de rectángulos: buscar raíces, dividir en subintervalos, tomar el valor absoluto en cada parte y sumar. Aparte, otro rombo sobre simetría se abre en dos cajas: función par, que duplica la integral de la mitad, y función impar, que pide cuidado.
>
> **Por qué importa:** la mayoría de los errores en área bajo la curva viene de ignorar el signo o de empezar la integral en el orden equivocado. Con este mapa de decisiones sabes de antemano qué revisar antes de integrar: positividad, raíces y simetría.
>
> **Ejemplo:** para $f(x) = x^3 - x$ en $[-2, 2]$ la nota divide en $[-2,-1]$, $[-1,0]$, $[0,1]$ y $[1,2]$, y suma los cuatro valores absolutos hasta obtener un área de $5$.

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🔎 Método directo — función simple y no negativa
>
> 1. Verificar que $f(x) \geq 0$ en $[a,b]$.
> 2. Encontrar la antiderivada $F(x)$ con $F'(x) = f(x)$.
> 3. Aplicar: $\text{Área} = F(b) - F(a)$.
>
> **Por qué importa:** es el camino más corto y solo exige comprobar el signo antes de evaluar; sin esa comprobación, el resultado puede salir negativo y ser el opuesto del área.

> [!tip] 🔎 Método por partes — función que cambia de signo
>
> 1. Encontrar las raíces de $f(x) = 0$ dentro de $[a,b]$.
> 2. Dividir $[a,b]$ en subintervalos donde $f$ mantiene signo.
> 3. Calcular $\left|\int\right|$ en cada subintervalo.
> 4. Sumar todos los resultados.
>
> **Por qué importa:** el valor absoluto está **fuera** de cada integral, no dentro del integrando: primero se integra en cada trozo y después se voltea el signo si el trozo salió negativo.

> [!tip] 🔎 Aprovechar la simetría — funciones pares e impares
>
> - **Función par** $f(-x) = f(x)$: si $f \geq 0$ en $[-a,a]$, entonces $\text{Área} = 2\int_0^a f(x)\,dx$.
> - **Función impar** $f(-x) = -f(x)$: la integral neta en $[-a,a]$ sale $0$ por cancelación; el área total es $2 \times$ (área del lado donde $f \geq 0$).
>
> **Por qué importa:** la paridad convierte un intervalo doble en uno solo. Reconocerla antes de integrar ahorra la mitad del cálculo y elimina un cambio de signo típico.

> [!tip] 🧠 Mnemotecnia GRAFO para área bajo la curva
>
> - **G** — Graficar la función y la región, marcando los límites $a$ y $b$ y sombreando el área.
> - **R** — Reconocer el tipo de área: positiva, negativa o mixta (y buscar las raíces si es mixta).
> - **A** — Aplicar el Teorema Fundamental del Cálculo; decidir área neta ($\int f$) o área total ($\int |f|$).
> - **F** — Formular la integral definida con los límites correctos, partiéndola si hay cambio de signo.
> - **O** — Obtener el resultado $F(b) - F(a)$ y verificar: el área geométrica debe ser positiva.
>
> **Por qué importa:** las cinco letras son el orden de trabajo completo: quien salta la **R** (reconocer el signo) es quien reporta $0$ como área en funciones impares.

---

## 📊 Casos Fundamentales

> [!info] 📈 Caso estándar: función siempre positiva
>
> Cuando $f(x) \geq 0$ en $[a,b]$, no hay truco: $\text{Área} = \int_a^b f(x)\,dx$. El ejemplo canónico es $f(x) = x^2$ en $[0,2]$: $\left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3}$.

> [!warning] 📉 Caso negativo: la integral sale negativa
>
> Cuando $f(x) \leq 0$ en $[a,b]$, la integral da el **negativo** del área. Para el área geométrica:
> $$\text{Área} = -\int_a^b f(x)\,dx = \int_a^b |f(x)|\,dx$$

> [!tip] 🔄 Caso mixto: la función cruza el eje
>
> 1. Encontrar las raíces: resolver $f(x) = 0$.
> 2. Dividir el intervalo en subintervalos donde $f$ mantiene signo.
> 3. Calcular por separado y sumar valores absolutos de cada integral.
>
> **Por qué importa:** es el caso de examen: quien olvida partir en las raíces reporta el área neta (a veces $0$) en lugar del área total.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Caso estándar: $f(x) = x^2$ en $[0, 2]$
>
> **Positividad:** $x^2 \geq 0$ para todo $x$ ✓
>
> **Cálculo:** $\text{Área} = \int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} - 0 = \frac{8}{3}$
>
> **Interpretación:** la región entre la parábola $y = x^2$, el eje $x$ y las rectas $x = 0$, $x = 2$ mide $\frac{8}{3}$ unidades cuadradas.
>
> **Por qué importa:** es el patrón base: positividad verificada, antiderivada y evaluar en los extremos.

> [!example] 🔢 Ejemplo 2 — Cambio de signo: $f(x) = x^3 - x$ en $[-2, 2]$
>
> **Paso 1 — Raíces:** $x^3 - x = 0 \Rightarrow x(x^2 - 1) = 0 \Rightarrow x = 0, \pm 1$.
>
> **Paso 2 — Signos en cada intervalo:**
>
> - $[-2, -1]$: $f(-1.5) = -1.875 < 0$
> - $[-1, 0]$: $f(-0.5) = 0.375 > 0$
> - $[0, 1]$: $f(0.5) = -0.375 < 0$
> - $[1, 2]$: $f(1.5) = 1.875 > 0$
>
> **Paso 3 — Integral por partes**, con $\int (x^3 - x)\,dx = \frac{x^4}{4} - \frac{x^2}{2}$:
>
> - $\int_{-2}^{-1} (x^3 - x)\,dx = \left[\frac{x^4}{4} - \frac{x^2}{2}\right]_{-2}^{-1} = \left(\frac{1}{4} - \frac{1}{2}\right) - (4 - 2) = -\frac{9}{4}$
> - $\int_{-1}^{0} (x^3 - x)\,dx = 0 - \left(-\frac{1}{4} + \frac{1}{2}\right) = \frac{1}{4}$
> - $\int_{0}^{1} (x^3 - x)\,dx = \frac{1}{4} - \frac{1}{2} - 0 = -\frac{1}{4}$
> - $\int_{1}^{2} (x^3 - x)\,dx = 4 - 2 - \left(\frac{1}{4} - \frac{1}{2}\right) = \frac{9}{4}$
>
> **Área total:** $\frac{9}{4} + \frac{1}{4} + \frac{1}{4} + \frac{9}{4} = 5$
>
> **Por qué importa:** los cuatro trozos se suman en valor absoluto: la integral neta habría dado $0$ (función impar en intervalo simétrico) y el área real es $5$.

> [!example] 🔢 Ejemplo 3 — Simetría par: $f(x) = 4 - x^2$ en $[-2, 2]$
>
> **Paridad:** $f(-x) = 4 - (-x)^2 = 4 - x^2 = f(x)$ (función par).
>
> **Positividad:** $4 - x^2 \geq 0 \Leftrightarrow x^2 \leq 4 \Leftrightarrow |x| \leq 2$, así que $f \geq 0$ en $[-2, 2]$ ✓.
>
> **Cálculo:** $\text{Área} = 2\int_0^2 (4 - x^2)\,dx = 2\left[4x - \frac{x^3}{3}\right]_0^2 = 2\left(8 - \frac{8}{3}\right) = 2 \cdot \frac{16}{3} = \frac{32}{3}$
>
> **Por qué importa:** la paridad corta el intervalo a la mitad; sin ella habría que partir en $[-2, 0]$ y $[0, 2]$ y sumar dos integrales iguales.

> [!example] 🔢 Ejemplo 4 — Polinomio con muchas raíces: $f(x) = x^4 - 5x^2 + 4$ en $[-3, 3]$
>
> **Factorización:** $x^4 - 5x^2 + 4 = (x^2 - 1)(x^2 - 4) = (x-1)(x+1)(x-2)(x+2)$; raíces $x = \pm 1, \pm 2$.
>
> **Análisis de signos:**
>
> - $(-3, -2)$: $f(-2.5) > 0$
> - $(-2, -1)$: $f(-1.5) < 0$
> - $(-1, 1)$: $f(0) = 4 > 0$
> - $(1, 2)$: $f(1.5) < 0$
> - $(2, 3)$: $f(2.5) > 0$
>
> **Cálculo por simetría** (función par), con $\int f = \frac{x^5}{5} - \frac{5x^3}{3} + 4x$:
>
> - $\int_0^1 f = \frac{1}{5} - \frac{5}{3} + 4 = \frac{38}{15}$
> - $\left|\int_1^2 f\right| = \left|\frac{32}{5} - \frac{40}{3} + 8 - \frac{38}{15}\right| = \frac{22}{15}$
> - $\int_2^3 f = \frac{243}{5} - 45 + 12 - \left(\frac{32}{5} - \frac{40}{3} + 8\right) = \frac{218}{15}$
>
> **Área total:** $2\left(\frac{38}{15} + \frac{22}{15} + \frac{218}{15}\right) = 2 \cdot \frac{278}{15} = \frac{556}{15}$
>
> **Por qué importa:** cuatro raíces y paridad: se integra la mitad y se duplica; sin factorizar antes, los cambios de signo se esconden y el resultado sale mal.

> [!example] 🔢 Ejemplo 5 — Trigonométrica: $f(x) = \sin x$ en $[0, 2\pi]$
>
> **Análisis:** $\sin x \geq 0$ en $[0, \pi]$ y $\sin x \leq 0$ en $[\pi, 2\pi]$.
>
> **Cálculo por partes:**
> $$\text{Área} = \int_0^{\pi} \sin x\,dx + \left|\int_{\pi}^{2\pi} \sin x\,dx\right| = [-\cos x]_0^{\pi} + \left|[-\cos x]_{\pi}^{2\pi}\right|$$
> $$= (-\cos \pi + \cos 0) + |(-\cos 2\pi + \cos \pi)| = (1 + 1) + |-1 - 1| = 2 + 2 = 4$$
>
> **Por qué importa:** el período partido por la mitad cambia de signo: el área total es $4$, mientras que la integral neta $\int_0^{2\pi} \sin x\,dx$ es $0$.

> [!example] 🔢 Ejemplo 6 — Sin forma cerrada: $f(x) = e^{-x^2}$ en $[-1, 1]$
>
> **Positividad:** $e^{-x^2} > 0$ para todo $x$ ✓.
>
> **Problema:** esta integral no tiene antiderivada elemental.
>
> **Solución:** se expresa con la función error $\text{erf}$: $\int_{-1}^{1} e^{-x^2}\,dx = \sqrt{\pi}\,\text{erf}(1) \approx 1.4936$, y se deja en valor numérico (para aproximarla, ver [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]]).
>
> **Por qué importa:** no toda área se cierra en fórmulas; reconocerlo a tiempo evita forzar sustituciones que no funcionan.

> [!example] 🚗 Ejemplo 7 — Aplicación física: desplazamiento
>
> **Problema:** un auto lleva velocidad $v(t) = 2t$ m/s durante los primeros $5$ segundos. ¿Qué distancia recorre?
>
> **Solución:** el desplazamiento es el área bajo la curva de velocidad:
> $$\text{Desplazamiento} = \int_0^5 2t\,dt = \left[t^2\right]_0^5 = 25 \text{ metros}$$
>
> **Por qué importa:** física y cálculo hablan el mismo idioma aquí: área bajo la curva de una tasa = acumulación de la cantidad.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Halla el área bajo $f(x) = x^2$ de $x = 0$ a $x = 3$.
>
> > [!success]- ✅ Solución
> >
> > $f \geq 0$ en $[0, 3]$ ✓, así que $\text{Área} = \int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = \frac{27}{3} = 9$.
> > **Lección:** positividad verificada, integral directa y ya.

> [!example] 📋 Planteamiento
>
> Halla el área total entre $f(x) = x^2 - 1$ y el eje $x$ en $[-1, 2]$.
>
> > [!success]- ✅ Solución
> > Raíz en $x = 1$ (dentro del intervalo): $f \leq 0$ en $[-1, 1]$ y $f \geq 0$ en $[1, 2]$.
> > $$\text{Área} = \int_{-1}^{1} (1 - x^2)\,dx + \int_{1}^{2} (x^2 - 1)\,dx = \left[x - \frac{x^3}{3}\right]_{-1}^{1} + \left[\frac{x^3}{3} - x\right]_{1}^{2} = \frac{4}{3} + \frac{4}{3} = \frac{8}{3}$$
> > **Lección:** partir en la raíz y sumar valores absolutos; la integral neta habría dado $0$ y el área real es $\frac{8}{3}$.

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^{\ln 3} e^x\,dx$ e interpútalo como área.
>
> > [!success]- ✅ Solución
> > $e^x > 0$ siempre, así que el valor de la integral es el área: $\int_0^{\ln 3} e^x\,dx = \left[e^x\right]_0^{\ln 3} = 3 - 1 = 2$.
> > **Lección:** la exponencial es su propia antiderivada; el área bajo $e^x$ entre $0$ y $\ln 3$ vale exactamente $2$.

> [!example] 📋 Planteamiento
>
> Usa simetría para calcular el área bajo $f(x) = x^2 + 1$ en $[-2, 2]$.
>
> > [!success]- ✅ Solución
> > $f(-x) = (-x)^2 + 1 = x^2 + 1 = f(x)$: función par y positiva.
> > $$\text{Área} = 2\int_0^2 (x^2 + 1)\,dx = 2\left[\frac{x^3}{3} + x\right]_0^2 = 2\left(\frac{8}{3} + 2\right) = \frac{28}{3}$$
> > **Lección:** la paridad duplica la mitad positiva; sin ella integrarías cuatro extremos en vez de dos.

> [!example] 📋 Planteamiento
>
> Calcula el área total bajo $f(x) = |\sin x|$ en $[0, 2\pi]$ sin operar con valores absolutos dentro de la integral.
>
> > [!success]- ✅ Solución
> > Se parte donde $\sin x$ cambia de signo ($x = \pi$):
> > $$\int_0^{\pi} \sin x\,dx + \left|\int_{\pi}^{2\pi} \sin x\,dx\right| = [-\cos x]_0^{\pi} + \left|[-\cos x]_{\pi}^{2\pi}\right| = 2 + |-2| = 4$$
> > **Lección:** $|\sin x|$ se quita partiendo el intervalo, no integrando el valor absoluto.

> [!example] 📋 Planteamiento
>
> Un móvil lleva velocidad $v(t) = 3t^2$ m/s durante $4$ s. ¿Qué distancia recorre?
>
> > [!success]- ✅ Solución
> > $v \geq 0$ en $[0, 4]$, así que la distancia es el área bajo la curva:
> > $$\int_0^4 3t^2\,dt = \left[t^3\right]_0^4 = 64 \text{ metros}$$
> > **Lección:** área bajo la tasa = acumulación; aquí, metros recorridos.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Planteo el área bajo $f \geq 0$ como $\int_a^b f(x)\,dx$ y verifico positividad antes de integrar.
> - [ ] Identifico las raíces de $f$ para partir el intervalo cuando la función cambia de signo.
> - [ ] Reconozco funciones pares para duplicar la integral de la mitad positiva del intervalo.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo el área total como suma de valores absolutos de las integrales por subintervalos.
> - [ ] Distingo área neta (con signo) de área geométrica (siempre positiva) y elijo la que pide el enunciado.
> - [ ] Aprovecho la simetría par/impar para reducir el intervalo de integración sin perder área.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo áreas de polinomios con cuatro raíces factorizando y tabulando signos antes de integrar.
> - [ ] Reconozco integrandos sin antiderivada elemental (como $e^{-x^2}$) y los dejo en forma de $\text{erf}$ o numérica.
> - [ ] Traduzco problemas de acumulación (velocidad → distancia, densidad → probabilidad) a un área bajo la curva.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage): aplicaciones del integral definido — área bajo una curva y área entre curvas.
> - G. Strang, *Calculus* (Wellesley-Cambridge): el área como límite de sumas de Riemann.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la definición formal que justifica el área como límite de sumas.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la herramienta principal de evaluación.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — linealidad y aditividad para partir intervalos.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas de evaluación con límites.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — áreas con límites infinitos.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] — aproximaciones cuando no hay forma cerrada.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — la misma área girada a tres dimensiones.
>
> **Conexiones interdisciplinarias:** en física, el área bajo la curva de velocidad es desplazamiento y bajo la de fuerza es trabajo; en probabilidad, el área bajo una función de densidad $f(x)$ es la probabilidad $P(a \leq X \leq b) = \int_a^b f(x)\,dx$; en diseño y arquitectura, esta misma idea mide superficies irregulares.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u7

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuándo es la integral definida exactamente el área bajo la curva?::Cuando $f \geq 0$ y es continua en $[a,b]$: $\text{Área} = \int_a^b f(x)\,dx$.
> - ¿Qué pasa si $f$ es negativa en todo el intervalo?::La integral sale negativa; el área geométrica es $-\int_a^b f(x)\,dx = \int_a^b |f(x)|\,dx$.
> - ¿Cómo se calcula el área total si $f$ cambia de signo?::Se hallan las raíces, se parte el intervalo, se integra por trozos y se suman los valores absolutos: $\sum_i \left|\int_{x_{i-1}}^{x_i} f\right|$.
> - ¿Qué ahorra reconocer una función par?::Integrar solo la mitad positiva y duplicar: $\text{Área} = 2\int_0^a f(x)\,dx$ en $[-a, a]$.
> - ¿Área neta o área total?::Neta = $\int_a^b f$ (puede ser $0$ o negativa); total = $\int_a^b |f|$ (siempre $\geq 0$). El enunciado decide cuál.
> - ¿Qué hacer si el integrando no tiene antiderivada elemental (ej. $e^{-x^2}$)?::Expresar con $\text{erf}$ o dejar valor numérico; la definición como límite de sumas sigue vigente.
> - ¿Cómo se traduce "distancia recorrida" a área?::Es el área bajo la curva de velocidad: $\int_{t_0}^{t_1} v(t)\,dt$ cuando $v \geq 0$.
> - ¿Cuál es el primer paso antes de cualquier integral de área?::Dibujar la región, verificar positividad y buscar raíces y simetrías.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la definición formal que justifica el área como límite de sumas.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la herramienta principal de evaluación.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — linealidad y aditividad para partir intervalos.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas de evaluación con límites.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — áreas con límites infinitos.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] — aproximaciones cuando no hay forma cerrada.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — la misma área girada a tres dimensiones.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — otra aplicación geométrica del integral definido.
>
> **Conexiones interdisciplinarias:** física (velocidad → distancia, fuerza → trabajo), probabilidad (densidad → $P(a \leq X \leq b) = \int_a^b f(x)\,dx$) y diseño (superficies irregulares).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 3: positividad directa, el caso más limpio.
> - Después el 2 y el 5: cambio de signo con raíces, el caso de examen.
> - Cierra con 4 y 6: simetría par y acumulación física.
> - Cuando lo tengas, continúa con [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas|02 - Área entre Curvas]] y luego los volúmenes de revolución de la misma unidad.

---

**Tags:** #MATG1045 #unidad7 #area-bajo-la-curva #integrales #aplicaciones #areas #geometria-analitica #interpretacion-geometrica

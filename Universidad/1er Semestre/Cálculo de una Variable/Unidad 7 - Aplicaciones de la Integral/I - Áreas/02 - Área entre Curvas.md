---
dg-publish: true
tags: [MATG1045, unidad7, area-entre-curvas, integrales, aplicaciones, areas, intersecciones, visualizacion-geometrica]
---

# 📏 Área entre Curvas

## 🎯 Introducción

> [!info] 💡 Qué es y por qué importa
>
> El **área entre curvas** es la extensión natural del área bajo una curva: la región queda limitada por **dos** funciones, y se calcula como la diferencia entre las integrales de la que está arriba y la que está abajo en cada intervalo.
>
> **Por qué importa:** casi toda región real está entre dos curvas (un terreno entre dos límites, una ganancia entre ingreso y costo, una probabilidad entre dos densidades). Saber plantear $\int (\text{superior} - \text{inferior})$ —y cuándo partir el intervalo— es la habilidad central de esta unidad.
>
> **Ejemplo:** entre $f(x) = 6 - x^2$ y $g(x) = x + 4$, las intersecciones $x = -2$ y $x = 1$ encierran una región de área $\frac{9}{2}$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — el área entre curvas respecto a $x$ y respecto a $y$.
> - **Procedimiento Paso a Paso** — el método PICAF y la elección del eje de integración.
> - **Casos Especiales** — signos distintos, simetría, intercambio de roles y regiones complejas.
> - **Ejemplos Resueltos** — cinco casos, de la parábola con recta al seno contra coseno.
> - **Ejercicios Propuestos** — seis plantillas, una por cada variante.
>
> **Por qué importa:** el orden de trabajo siempre es el mismo: intersecciones → quién arriba → integral por tramo → suma. El mapa de la nota sigue ese orden.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Área entre dos curvas respecto a $x$
>
> Si $f(x) \geq g(x)$ para todo $x \in [a,b]$, el **área** de la región limitada por $y = f(x)$ (superior) y $y = g(x)$ (inferior) entre $x = a$ y $x = b$ es:
> $$A = \int_a^b [f(x) - g(x)]\,dx$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Área_entre_Curvas_01.svg]]
>
> **Se lee así:** una cadena de rectángulos que empieza con dos funciones y termina en el **área total**. En medio, la decisión de qué función va arriba se resuelve con una caja que pregunta *si $f(x) \geq g(x)$*: el sí y el no abren dos caminos paralelos, cada uno con su integral, y ambos vuelven a unirse para sumar las áreas de todos los intervalos.
>
> **Por qué importa:** el diagrama obliga a buscar los cruces antes de integrar y a decidir el **orden de la resta** en cada tramo. Así se evita el error más caro: escribir $\int (g - f)$ cuando arriba está $f$, o integrar sobre un tramo donde las curvas ya se intercambiaron.
>
> **Ejemplo:** entre $f(x) = 6 - x^2$ y $g(x) = x + 4$ se resuelven las intersecciones $x = -2$ y $x = 1$, y el área resulta $\frac{9}{2}$.

> [!warning] ⚠️ Condición importante
>
> La fórmula $A = \int_a^b [f(x) - g(x)]\,dx$ solo es válida cuando $f(x) \geq g(x)$ en **todo** $[a,b]$. Si las funciones se cruzan dentro del intervalo, hay que dividir la región en subintervalos y sumar cada parte (con el orden de resta correcto en cada una).
>
> **Por qué importa:** una resta mal ordenada invierte el signo del tramo; el área total sale mal aunque la integral "se vea" bien calculada.

> [!note] 📋 Definición — Área entre curvas respecto a $y$
>
> Si las curvas vienen como $x = f(y)$ (derecha) y $x = g(y)$ (izquierda) con $f(y) \geq g(y)$ para $y \in [c,d]$, el área se mide con franjas horizontales:
> $$A = \int_c^d [f(y) - g(y)]\,dy$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Área_entre_Curvas_02.svg]]
>
> **Se lee así:** partes de la región entre curvas y llegas a un rombo que pregunta *cómo vienen dadas las funciones*. Se abre en tres ramas: si vienen como $y = f(x)$ tomas un candidato en $x$, si vienen como $x = g(y)$ tomas un candidato en $y$, y si están en ambas formas eliges la más simple. Cada candidato pasa a su propio rombo de cruces, que decide si conviene **cambiar a la otra variable**.
>
> **Por qué importa:** elegir bien la variable es la diferencia entre una integral de tres líneas y una de dos páginas. Este diagrama da un criterio objetivo para decidir entre $dx$ y $dy$ sin adivinar.
>
> **Ejemplo:** la región entre $x = y^2$ y $x = 2y$ en $[0, 2]$ se resuelve con $dy$ sin despejar nada: $\int_0^2 (2y - y^2)\,dy = \frac{4}{3}$.

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🎓 Mnemotecnia PICAF
>
> - **P** — Puntos de intersección: resolver $f(x) = g(x)$ para hallar los extremos reales de la región.
> - **I** — Intervalos: dividir el dominio según los cruces encontrados.
> - **C** — Comparar: determinar cuál función está arriba en cada intervalo (evaluar un punto).
> - **A** — Aplicar: integrar $\int (\text{superior} - \text{inferior})\,dx$ en cada tramo.
> - **F** — Finalizar: sumar las áreas de todos los intervalos.
>
> **Por qué importa:** las cinco letras son el algoritmo completo; saltarse la **C** (comparar) es la causa número uno de restas al revés.

> [!tip] 🔎 Elegir el eje de integración
>
> - **Respecto a $x$** cuando las funciones vienen como $y = f(x)$, las franjas verticales son simples y hay pocos cruces horizontales.
> - **Respecto a $y$** cuando es más fácil expresar $x$ en términos de $y$, la región se ve más simple con franjas horizontales o hay ramas múltiples que complicarían la integral en $x$.
>
> **Por qué importa:** una mala elección multiplica los tramos a integrar; la buena los reduce a uno solo.

---

## 📊 Casos Especiales

> [!info] ➕➖ Funciones con signos diferentes
>
> Si $f(x) \geq 0$ y $g(x) \leq 0$ en $[a,b]$, el área entre ellas suma ambas partes:
> $$A = \int_a^b f(x)\,dx + \int_a^b |g(x)|\,dx = \int_a^b f(x)\,dx - \int_a^b g(x)\,dx$$
>
> **Por qué importa:** la fórmula $\int (f - g)$ ya lo maneja: restar una función negativa es sumar su valor absoluto.

> [!tip] 🪞 Regiones simétricas
>
> Si la región es simétrica respecto al eje $y$ y ambas funciones son pares:
> $$A = 2\int_0^a [f(x) - g(x)]\,dx$$
>
> **Por qué importa:** la simetría corta el trabajo a la mitad; con funciones impares y región simétrica, en cambio, los tramos pueden cancelarse: conviene partir y sumar valores absolutos.

> [!warning] 🔄 Intercambio de roles
>
> Cuando las curvas se cruzan, en unos tramos $f \geq g$ y en otros $g \geq f$. El área total es:
> $$A = \sum_i \int_{x_i}^{x_{i+1}} |f(x) - g(x)|\,dx$$
>
> **Por qué importa:** el valor absoluto (o el orden de resta cambiado por tramo) es lo que evita restar el área al revés.

> [!warning] 🧩 Regiones complejas
>
> Para regiones que no se describen con una sola integral:
>
> 1. Identificar subregiones donde la relación entre funciones es constante.
> 2. Calcular el área de cada subregión por separado.
> 3. Sumar todas las áreas: $A_{\text{total}} = A_1 + A_2 + \cdots + A_n$.
>
> **Por qué importa:** dividir es siempre correcto; forzar una sola integral sobre una región partida casi nunca lo es.

> [!info] ⚠️ Casos problemáticos
>
> - **Tangencias:** las curvas se tocan pero no se cruzan: el tramo cuenta igual, sin cambio de orden.
> - **Asíntotas:** límites de integración que tienden a infinito → integral impropia.
> - **Discontinuidades:** partir la integral donde la función salte.
> - **Implícitas:** cuando cuesta despejar $y$ o $x$, conviene la otra variable o un parametrización.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Sin intersección: $f(x) = x^2 + 1$ y $g(x) = x^2 - 1$ en $[0, 2]$
>
> **Comparar:** para cualquier $x$, $f(x) = x^2 + 1 > x^2 - 1 = g(x)$ ✓ (las curvas son paralelas; no hay cruces en $[0,2]$).
>
> **Cálculo:**
> $$A = \int_0^2 [(x^2 + 1) - (x^2 - 1)]\,dx = \int_0^2 2\,dx = 2x\Big|_0^2 = 4$$
>
> **Por qué importa:** cuando la diferencia $f - g$ es constante, el área es un rectángulo: el integrando se simplifica antes de integrar.

> [!example] 🔢 Ejemplo 2 — Parábola y recta: $f(x) = 6 - x^2$ y $g(x) = x + 4$
>
> **P — Intersecciones:** $6 - x^2 = x + 4 \Rightarrow x^2 + x - 2 = 0 \Rightarrow (x+2)(x-1) = 0 \Rightarrow x = -2 \text{ o } x = 1$.
>
> **C — Quién arriba:** en $x = 0$: $f(0) = 6$, $g(0) = 4$ → $f \geq g$ en $[-2, 1]$.
>
> **A y F — Integral y suma:**
> $$A = \int_{-2}^1 [(6 - x^2) - (x + 4)]\,dx = \int_{-2}^1 (2 - x^2 - x)\,dx = \left[2x - \frac{x^3}{3} - \frac{x^2}{2}\right]_{-2}^1$$
> $$= \left(2 - \frac{1}{3} - \frac{1}{2}\right) - \left(-4 + \frac{8}{3} - 2\right) = \frac{7}{6} + \frac{10}{3} = \frac{9}{2}$$
>
> **Por qué importa:** es el caso canónico de examen: dos cruces reales, un solo tramo, y la resta en el orden correcto.

> [!example] 🔢 Ejemplo 3 — Se cruzan dos veces: $f(x) = \sin x$ y $g(x) = \cos x$ en $[0, 2\pi]$
>
> **P — Intersecciones:** $\sin x = \cos x \Rightarrow \tan x = 1 \Rightarrow x = \frac{\pi}{4}, \frac{5\pi}{4}$ en $[0, 2\pi]$.
>
> **C — Intervalos:**
>
> - En $[0, \frac{\pi}{4}]$: $\cos x \geq \sin x$
> - En $[\frac{\pi}{4}, \frac{5\pi}{4}]$: $\sin x \geq \cos x$
> - En $[\frac{5\pi}{4}, 2\pi]$: $\cos x \geq \sin x$
>
> **A y F — Sumar las tres partes:**
> $$A = \int_0^{\pi/4} (\cos x - \sin x)\,dx + \int_{\pi/4}^{5\pi/4} (\sin x - \cos x)\,dx + \int_{5\pi/4}^{2\pi} (\cos x - \sin x)\,dx$$
> $$= [\sin x + \cos x]_0^{\pi/4} + [-\cos x - \sin x]_{\pi/4}^{5\pi/4} + [\sin x + \cos x]_{5\pi/4}^{2\pi}$$
> $$= (\sqrt{2} - 1) + 2\sqrt{2} + (1 + \sqrt{2}) = 4\sqrt{2}$$
>
> **Por qué importa:** tres tramos con orden de resta distinto cada uno; sumar las tres partes da $4\sqrt{2}$, mientras que la integral neta $\int_0^{2\pi}(\sin x - \cos x)\,dx$ da $0$.

> [!example] 🔢 Ejemplo 4 — Respecto a $y$: $x = y^2$ y $x = 2y$ entre $y = 0$ y $y = 2$
>
> **C — Quién a la derecha:** en $y = 1$: $y^2 = 1$ y $2y = 2$ → $2y \geq y^2$ en $[0, 2]$.
>
> **A y F:**
> $$A = \int_0^2 (2y - y^2)\,dy = \left[y^2 - \frac{y^3}{3}\right]_0^2 = 4 - \frac{8}{3} = \frac{4}{3}$$
>
> **Por qué importa:** con franjas horizontales no hay que despejar $y$ de $x = y^2$ (que daría dos ramas): la región se describe en una sola integral.

> [!example] 🔢 Ejemplo 5 — Con PICAF: $f(x) = x^2$ y $g(x) = 2x - x^2$
>
> **P:** $x^2 = 2x - x^2 \Rightarrow 2x^2 - 2x = 0 \Rightarrow 2x(x - 1) = 0 \Rightarrow x = 0 \text{ o } x = 1$.
>
> **I:** región de interés $[0, 1]$.
>
> **C:** en $x = 0.5$: $f(0.5) = 0.25$, $g(0.5) = 0.75$ → $g \geq f$ en $[0, 1]$.
>
> **A:**
> $$A = \int_0^1 [(2x - x^2) - x^2]\,dx = \int_0^1 (2x - 2x^2)\,dx$$
>
> **F:**
> $$A = \left[x^2 - \frac{2x^3}{3}\right]_0^1 = 1 - \frac{2}{3} = \frac{1}{3}$$
>
> **Por qué importa:** la región está entre dos parábolas que se tocan en los extremos: el "abajo" y el "arriba" son cóncavas opuestas, y PICAF lo resuelve sin dudar.

---

## 🌀 Extensiones

> [!tip] 🌀 Coordenadas polares
>
> Para curvas $r = f(\theta)$ y $r = g(\theta)$ con $f(\theta) \geq g(\theta) \geq 0$ en $[\alpha, \beta]$:
> $$A = \frac{1}{2}\int_\alpha^\beta \left([f(\theta)]^2 - [g(\theta)]^2\right)d\theta$$
>
> **Por qué importa:** es la misma idea de "superior menos inferior", pero en radio: el factor $\frac{1}{2}$ y el cuadrado vienen del área del sector circular. Ver [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]].

> [!info] 📈 Curvas paramétricas
>
> Para curvas dadas paramétricamente, conviene la forma $dx = x'(t)\,dt$:
> $$A = \int y\,dx = \int_{t_1}^{t_2} y(t)\,x'(t)\,dt$$
>
> **Por qué importa:** evita despejar $y$ en función de $x$; la parametrización hace el trabajo (igual que en longitud de arco).

> [!warning] 🌊 Teorema de Green
>
> Para una curva cerrada simple $C$ recorrida en sentido positivo, el área encerrada también es:
> $$A = \oint_C x\,dy = -\oint_C y\,dx = \frac{1}{2}\oint_C (x\,dy - y\,dx)$$
>
> **Por qué importa:** es el puente entre integral de línea y área; aparece en flujo y circulación, y confirma que el área es un caso particular de una integral de línea.

---

## 🌍 Aplicaciones

> [!info] 🗛 Ingeniería civil — terrenos
>
> Para terrenos limitados por curvas de nivel o carreteras curvas:
> $$A = \int_a^b [f_{\text{superior}}(x) - f_{\text{inferior}}(x)]\,dx$$

> [!tip] 💊 Farmacología — biodisponibilidad
>
> La diferencia de concentración entre dos formulaciones se mide como área entre curvas de concentración:
> $$\text{Diferencia AUC} = \int_0^T [C_1(t) - C_2(t)]\,dt$$
> donde $C_1(t)$ y $C_2(t)$ son las concentraciones en sangre.

> [!warning] 🌊 Hidrología — volúmenes de agua
>
> Para embalses con perfiles variables, el volumen se obtiene integrando el área de la sección transversal $A(z)$ a la altura $z$:
> $$V = \int_0^h A(z)\,dz$$
>
> **Por qué importa:** misma estructura que el área entre curvas, pero con secciones en lugar de alturas: la idea se repite en toda la unidad.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Halla el área entre $f(x) = x + 2$ y $g(x) = x^2$.
>
> > [!success]- ✅ Solución
> > Cruces: $x^2 = x + 2 \Rightarrow (x+1)(x-2) = 0 \Rightarrow x = -1, 2$; en $x = 0$ vale $f(0) = 2 > g(0) = 0$, así que $f$ está arriba.
> > $$A = \int_{-1}^2 (x + 2 - x^2)\,dx = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^2 = \frac{10}{3} + \frac{7}{6} = \frac{9}{2}$$
> > **Lección:** cruces como límites y comparar un punto fija el orden de la resta ✓

> [!example] 📋 Planteamiento
>
> Halla el área entre $f(x) = e^x$ y $g(x) = x$ en $[0, 1]$.
>
> > [!success]- ✅ Solución
> > $e^x \geq x$ en todo $\mathbb{R}$ (no hay cruces): $A = \int_0^1 (e^x - x)\,dx = \left[e^x - \frac{x^2}{2}\right]_0^1 = \left(e - \frac{1}{2}\right) - 1 = e - \frac{3}{2} \approx 1.2183$.
> > **Lección:** cuando no hay intersección en el intervalo, un solo tramo y ya ✓

> [!example] 📋 Planteamiento
>
> Calcula el área entre $x = y + 2$ y $x = y^2$ respecto a $y$.
>
> > [!success]- ✅ Solución
> > Cruces: $y^2 = y + 2 \Rightarrow (y+1)(y-2) = 0 \Rightarrow y = -1, 2$; la recta está a la derecha en $[-1, 2]$.
> > $$A = \int_{-1}^2 (y + 2 - y^2)\,dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^2 = \frac{10}{3} + \frac{7}{6} = \frac{9}{2}$$
> > **Lección:** la misma región en la otra variable da el mismo área: $\frac{9}{2}$ ✓

> [!example] 📋 Planteamiento
>
> Halla el área entre $f(x) = \sin x$ y $g(x) = \cos x$ en $[0, \frac{\pi}{2}]$.
>
> > [!success]- ✅ Solución
> > Se cruzan en $x = \frac{\pi}{4}$:
> > $$A = \int_0^{\pi/4} (\cos x - \sin x)\,dx + \int_{\pi/4}^{\pi/2} (\sin x - \cos x)\,dx = (\sqrt{2} - 1) + (\sqrt{2} - 1) = 2\sqrt{2} - 2$$
> > **Lección:** un cruce, dos tramos, mismo patrón que el ejemplo 3 acortado ✓

> [!example] 📋 Planteamiento
>
> Halla el área entre $f(x) = 4 - x^2$ y $g(x) = x^2$.
>
> > [!success]- ✅ Solución
> > Cruces: $4 - x^2 = x^2 \Rightarrow x^2 = 2 \Rightarrow x = \pm\sqrt{2}$; $f$ está arriba.
> > $$A = \int_{-\sqrt{2}}^{\sqrt{2}} (4 - 2x^2)\,dx = \left[4x - \frac{2x^3}{3}\right]_{-\sqrt{2}}^{\sqrt{2}} = \frac{16\sqrt{2}}{3}$$
> > **Lección:** región simétrica con funciones pares: $2\int_0^{\sqrt2}(4-2x^2)\,dx$ da lo mismo ✓

> [!example] 📋 Planteamiento
>
> El ingreso marginal de una máquina es $R'(t) = 10e^{-0.1t}$ y el costo marginal es $C'(t) = 2$ (en miles por mes). ¿Cuál es la ganancia acumulada entre $t = 0$ y $t = 10$?
>
> > [!success]- ✅ Solución
> > La ganancia acumulada es el área entre las tasas:
> > $$A = \int_0^{10} (10e^{-0.1t} - 2)\,dt = \left[-100e^{-0.1t} - 2t\right]_0^{10} = (-100e^{-1} - 20) - (-100) = 80 - \frac{100}{e} \approx 43.21$$
> > **Lección:** área entre tasas = acumulación de la diferencia; aquí, miles en $10$ meses ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Planteo el área entre curvas como $\int_a^b [f(x) - g(x)]\,dx$ identificando quién está arriba.
> - [ ] Encuentro los puntos de intersección resolviendo $f(x) = g(x)$ antes de integrar.
> - [ ] Reconozco cuándo conviene integrar respecto a $y$ en lugar de respecto a $x$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Divido la región en tramos cuando las curvas se cruzan y sumo los valores absolutos.
> - [ ] Aprovecho simetrías y paridad para reducir el intervalo de integración.
> - [ ] Manejo los casos especiales: tangencias, asíntotas, discontinuidades y curvas implícitas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Aplico PICAF completo (Puntos, Intervalos, Comparar, Aplicar, Finalizar) sin saltar pasos.
> - [ ] Extiendo la fórmula a coordenadas polares $\frac{1}{2}\int ([f]^2 - [g]^2)\,d\theta$ y a curvas paramétricas $\int y(t)\,x'(t)\,dt$.
> - [ ] Verifico que el resultado sea positivo y geométricamente sensato, y lo contrasto con un bosquejo.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage): aplicaciones del integral definido — área entre dos curvas.
> - G. Strang, *Calculus* (Wellesley-Cambridge): áreas entre curvas y elección de variable.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el concepto fundamental base: una sola curva contra el eje.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la herramienta principal de evaluación.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas para resolver las integrales.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/04 - Asíntotas en Integrales Definidas|04 - Asíntotas en Integrales Definidas]] — cuando los límites de integración se escapan a infinito.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] — la extensión a otros sistemas de coordenadas.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas|03 - Derivadas Paramétricas]] — representaciones alternativas de curvas.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] — métodos computacionales cuando no hay forma cerrada.
>
> **Conexiones interdisciplinarias:** ingeniería civil (terrenos entre curvas de nivel), farmacología (diferencia de AUC entre formulaciones), hidrología (volumen por secciones), economía (costos e ingresos marginales) y física (centroides y momentos, que usan estas mismas áreas).

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u7

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la fórmula del área entre $f$ y $g$ con $f \geq g$ en $[a,b]$?::$A = \int_a^b [f(x) - g(x)]\,dx$, con $f$ la función superior y $g$ la inferior.
> - ¿Qué hago primero, antes de cualquier integral de área entre curvas?::Hallar los puntos de intersección resolviendo $f(x) = g(x)$: son los límites reales de la región.
> - ¿Qué pasa si las curvas se cruzan dentro del intervalo?::Se parte en tramos, en cada uno se decide quién está arriba y se suman los valores absolutos: $\sum_i \int_{x_i}^{x_{i+1}} |f - g|$.
> - ¿Cuándo integrar respecto a $y$?::Cuando las curvas vienen como $x = f(y)$, la región se ve mejor con franjas horizontales o hay ramas múltiples en $x$.
> - ¿Cómo es el área entre curvas en polares?::$A = \frac{1}{2}\int_\alpha^\beta ([f(\theta)]^2 - [g(\theta)]^2)\,d\theta$ con $f \geq g \geq 0$.
> - ¿Y para curvas paramétricas?::$A = \int y\,dx = \int_{t_1}^{t_2} y(t)\,x'(t)\,dt$, sin despejar $y$ en función de $x$.
> - ¿Qué error castiga el valor absoluto?::Restar al revés en un tramo donde ya se cruzaron las curvas: la integral neta miente, el área total no.
> - ¿Cómo se verifica rápido un área calculada?::El resultado debe ser positivo y concordar con un bosquejo de la región; si sale negativo, el orden de resta estuvo invertido.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el concepto fundamental base: una curva contra el eje.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la herramienta principal de evaluación.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas para resolver las integrales.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/04 - Asíntotas en Integrales Definidas|04 - Asíntotas en Integrales Definidas]] — contexto más amplio cuando los límites tienden a infinito.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/03 - Área entre Curvas respecto a Y|03 - Área entre Curvas respecto a Y]] — la misma idea con franjas horizontales.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — girar esta región da volumen.
>
> **Conexiones interdisciplinarias:** análisis de funciones (quién está arriba se decide con monotonía, ver [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]]), farmacología (AUC), economía (costos e ingresos marginales) y física (centroides y momentos).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 4: cruces limpios y un solo cambio de orden.
> - Después el 3: la misma región respecto a $y$, para sentir la elección de variable.
> - Cierra con 5 y 6: simetría y aplicación con tasas.
> - Cuando lo tengas, sigue con [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/03 - Área entre Curvas respecto a Y|03 - Área entre Curvas respecto a Y]] y luego la extensión polar en [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]].

---

**Tags:** #MATG1045 #unidad7 #area-entre-curvas #integrales #aplicaciones #areas #intersecciones #visualizacion-geometrica

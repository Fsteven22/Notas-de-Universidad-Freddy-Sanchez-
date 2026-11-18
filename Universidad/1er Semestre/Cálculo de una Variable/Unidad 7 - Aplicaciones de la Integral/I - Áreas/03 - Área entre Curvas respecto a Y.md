---
dg-publish: true
tags: [MATG1045, unidad7, area-entre-curvas-respecto-a-y, integrales, aplicaciones, areas, integracion-dy, franjas-horizontales, transformacion-ecuaciones]
---

# 📊 Área entre Curvas respecto a Y

## 🎯 Introducción

> [!info] 💡 Qué es y por qué importa
>
> La **integración respecto a $y$** es el método alternativo para calcular áreas entre curvas: en lugar de franjas verticales ($dx$), se toman **franjas horizontales** ($dy$). Ya no se resta "superior menos inferior", sino **derecha menos izquierda**.
>
> **Por qué importa:** muchas regiones vienen dadas como $x = f(y)$ (parábolas horizontales, curvas con bucle, círculos) o tienen límites horizontales naturales; forzarlas a $dx$ multiplica las integrales o exige invertir funciones. Con $dy$ la misma región sale en una sola línea.
>
> **Ejemplo:** la región entre $x = y^2$ y $x = 4$ con $-2 \leq y \leq 2$ se calcula directo como $A = \int_{-2}^{2} (4 - y^2)\,dy = \frac{32}{3}$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — la fórmula con franjas horizontales y el criterio para elegir $dy$ o $dx$.
> - **Procedimiento Paso a Paso** — el algoritmo de cinco pasos y la tabla de decisión.
> - **Casos Especiales** — conversiones útiles y ramas múltiples.
> - **Ejemplos Resueltos** — cinco casos, de la parábola al bucle.
> - **Ejercicios Propuestos** — seis plantillas, una por cada variante.
>
> **Por qué importa:** la elección de variable es una decisión, no un gusto: este mapa empieza por la fórmula y termina por el criterio que la hace obvia.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Área entre curvas respecto a $y$
>
> Si $x = f(y)$ está a la derecha de $x = g(y)$, con $f(y) \geq g(y)$ para todo $y \in [c,d]$, el **área** de la región entre ambas curvas es:
> $$A = \int_c^d [f(y) - g(y)]\,dy$$
>
> donde $f(y)$ es la función de la **derecha**, $g(y)$ la de la **izquierda**, y $[c,d]$ son los límites en $y$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Área_entre_Curvas_respecto_a_Y_01.svg]]
>
> **Se lee así:** una escalera de rectángulos numerados que empieza en la **región horizontal** y baja paso a paso: expresar las curvas en términos de $y$, tomar el menor y el mayor valor de $y$ como límites, verificar que la función de la derecha quede a la derecha, configurar la integral con la diferencia y evaluar. Una caja final advierte que, si el orden cambia dentro del intervalo, hay que separar en tramos o usar valor absoluto.
>
> **Por qué importa:** integrar respecto a $y$ invierte la regla de arriba y abajo: ahora se resta **derecha menos izquierda**. Tener el orden claro evita áreas negativas y explica por qué con $dy$ algunos ejercicios salen mucho más simples.
>
> **Ejemplo:** para la región entre $x = y^2$ y $x = 4$ con $-2 \leq y \leq 2$, la nota usa $A = \int_{-2}^{2} (4 - y^2)\,dy = \frac{32}{3}$.

> [!warning] ⚠️ Orientación de la franja
>
> En este método los rectángulos son **horizontales** y tienen:
>
> - **Ancho:** $f(y) - g(y)$ (derecha menos izquierda).
> - **Altura:** $dy$ (diferencial en $y$).
> - **Área del rectángulo:** $[f(y) - g(y)]\,dy$.
>
> **Por qué importa:** confundir el ancho con la altura (o restar izquierda menos derecha) invierte el signo del resultado; el área siempre sale positiva cuando el orden es el correcto.

> [!note] 📋 Definición — Criterio de elección entre $dx$ y $dy$
>
> La variable de integración se elige por cómo viene descrita la región:
>
> - **$dx$ (franjas verticales):** curvas como $y = f(x)$, límites verticales $x = a$, $x = b$, región "alta y delgada".
> - **$dy$ (franjas horizontales):** curvas como $x = f(y)$, límites horizontales $y = c$, $y = d$, región "ancha y baja", ramas múltiples en $x$ o inversas complejas.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Área_entre_Curvas_respecto_a_Y_02.svg]]
>
> **Se lee así:** una caja sobre el bucle abre una secuencia de rectángulos numerados: los cruces con el eje, el tramo donde vive el bucle, qué lado del bucle corresponde a cada subtramo, la integral partida en dos y el recordatorio de usar valor absoluto. Del mismo nodo sale una caja aparte que compara **franjas horizontales** contra verticales para decidir entre $dy$ y $dx$.
>
> **Por qué importa:** en un bucle el orden de las curvas se invierte a mitad del recorrido, así que un solo integrando da un resultado sin sentido. El diagrama entrena en detectar ese cambio de lado y **partir la integral en dos**, la trampa clásica de estos ejercicios.
>
> **Ejemplo:** para el bucle de $x = y^3 - 3y$ la nota integra de $-\sqrt{3}$ a $0$ con $y^3 - 3y$ y de $0$ a $\sqrt{3}$ con su negativo, evitando un área negativa.

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🔎 Algoritmo para integrar respecto a $y$
>
> 1. **Expresar las curvas en términos de $y$:** convertir $y = h(x)$ en $x = h^{-1}(y)$ cuando sea posible; identificar $x = f(y)$ (derecha) y $x = g(y)$ (izquierda).
> 2. **Encontrar los límites en $y$:** el menor y el mayor valor de $y$ de la región serán $c$ (inferior) y $d$ (superior).
> 3. **Verificar el orden:** para cada $y \in [c,d]$ comprobar que $f(y) \geq g(y)$; evaluar un punto si hay duda.
> 4. **Configurar la integral:** $A = \int_c^d [f(y) - g(y)]\,dy$.
> 5. **Evaluar:** y si el orden cambia dentro del intervalo, separar en tramos o usar valor absoluto.
>
> **Por qué importa:** los pasos 1 y 2 son donde se decide el ejercicio: escribir mal la rama (olvidadando el $\pm$) o usar límites de $x$ en una integral de $y$ arruina el resultado aunque la integral esté bien calculada.

> [!tip] 📋 Guía rápida de decisión
>
> | Situación | Mejor método | Razón |
> |---|---|---|
> | $y = x^2$, $y = x$ | $dx$ | funciones naturales en $x$ |
> | $x = y^2$, $x = 2y$ | $dy$ | funciones naturales en $y$ |
> | Límites $x = a$, $x = b$ | $dx$ | límites verticales |
> | Límites $y = c$, $y = d$ | $dy$ | límites horizontales |
> | Círculo $x^2 + y^2 = r^2$ | $dy$ | evita ramas múltiples |
> | $y = \sqrt{x}$ vs líneas verticales | $dy$ | convierte a $x = y^2$ |
> | Región "alta y delgada" | $dx$ | franjas verticales naturales |
> | Región "ancha y baja" | $dy$ | franjas horizontales naturales |
>
> **Por qué importa:** es la consulta de tres segundos antes de plantear la integral: identifica la fila y ya sabes qué variable y qué orden de resta usar.

---

## 🔄 Transformación de Ecuaciones

> [!info] 🔄 Conversiones útiles
>
> | Forma $y = f(x)$ | Forma $x = g(y)$ | Observaciones |
> |---|---|---|
> | $y = x^2$ | $x = \pm\sqrt{y}$ | dos ramas |
> | $y = \sqrt{x}$ | $x = y^2$ | simple |
> | $y = e^x$ | $x = \ln(y)$ | $y > 0$ |
> | $y = \sin(x)$ | $x = \arcsin(y)$ | $y \in [-1, 1]$ |
> | $x^2 + y^2 = r^2$ | $x = \pm\sqrt{r^2 - y^2}$ | círculo |
> | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ | $x = \pm\frac{a}{b}\sqrt{b^2 - y^2}$ | elipse |
>
> **Por qué importa:** la tabla es el diccionario del paso 1 del algoritmo: convertir mal (por ejemplo $y = x^2 \Rightarrow x = y^2$) cambia la curva completa.

> [!warning] 🌿 Manejo de ramas múltiples
>
> Cuando $x = f(y)$ tiene dos valores, hay que tomar **todas** las ramas relevantes. Para el círculo $x^2 + y^2 = 4$:
>
> - Rama derecha: $x = \sqrt{4 - y^2}$
> - Rama izquierda: $x = -\sqrt{4 - y^2}$
>
> $$A = \int_{-2}^{2} \left[\sqrt{4-y^2} - (-\sqrt{4-y^2})\right]dy = \int_{-2}^{2} 2\sqrt{4-y^2}\,dy = 4\pi$$
>
> **Por qué importa:** el resultado $4\pi$ es el área del disco de radio $2$: una buena verificación de que las dos ramas se usaron.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Parábola y recta vertical: $x = y^2$ y $x = 4$ en $[-2, 2]$
>
> **Paso 1 — Funciones:** $f(y) = 4$ (derecha), $g(y) = y^2$ (izquierda).
>
> **Paso 2 — Límites y orden:** $c = -2$, $d = 2$; para cualquier $y \in [-2, 2]$: $4 \geq y^2$ ✓.
>
> **Paso 3 — Cálculo:**
> $$A = \int_{-2}^2 (4 - y^2)\,dy = \left[4y - \frac{y^3}{3}\right]_{-2}^2 = \left(8 - \frac{8}{3}\right) - \left(-8 + \frac{8}{3}\right) = 16 - \frac{16}{3} = \frac{32}{3}$$
>
> **Por qué importa:** el caso más limpio de $dy$: la parábola horizontal y la recta vertical dan una sola integral simétrica.

> [!example] 🔢 Ejemplo 2 — Dos parábolas horizontales: $x = y^2 + 1$ y $x = 3 - y^2$
>
> **Paso 1 — Intersecciones:** $y^2 + 1 = 3 - y^2 \Rightarrow 2y^2 = 2 \Rightarrow y = \pm 1$.
>
> **Paso 2 — Quién a la derecha:** en $y = 0$: $3 - 0 = 3$ vs $0 + 1 = 1$ → $x = 3 - y^2$ está a la derecha.
>
> **Paso 3 — Cálculo:**
> $$A = \int_{-1}^1 [(3 - y^2) - (y^2 + 1)]\,dy = \int_{-1}^1 (2 - 2y^2)\,dy = 2\left[y - \frac{y^3}{3}\right]_{-1}^1 = 2\left(\frac{2}{3} + \frac{2}{3}\right) = \frac{8}{3}$$
>
> **Por qué importa:** la diferencia $f - g$ salió par, así que la simetría ya estaba haciendo el trabajo a medias.

> [!example] 🔢 Ejemplo 3 — Cuándo $dy$ conviene: $x = \sqrt{y}$, $x = 0$ y $y = 4$
>
> **Con $dy$ (directo):** la curva ya viene como $x = \sqrt{y}$ y los límites son horizontales:
> $$A = \int_0^4 \sqrt{y}\,dy = \left[\frac{2y^{3/2}}{3}\right]_0^4 = \frac{2}{3} \cdot 8 = \frac{16}{3}$$
>
> **Con $dx$ (posible, pero invirtiendo):** habría que escribir $y = x^2$ y usar $A = \int_0^2 (4 - x^2)\,dx = \frac{16}{3}$: mismo resultado, pero despejando.
>
> **Por qué importa:** cuando la frontera viene dada como $x = f(y)$ y los límites son $y = c$, $y = d$, la integral en $dy$ es la que no pide invertir nada.

> [!example] 🔢 Ejemplo 4 — Región compleja: $y = x^2 - 4$, $y = 0$, $x = 0$ (primer cuadrante)
>
> **Análisis:** $y = x^2 - 4$ corta al eje $x$ en $x = \pm 2$; en el primer cuadrante la región va de $y = -4$ a $y = 0$, con frontera derecha $x = \sqrt{y+4}$ (de $y = x^2 - 4$).
>
> **Con $dy$:**
> $$A = \int_{-4}^0 \sqrt{y + 4}\,dy \quad (u = y+4,\ du = dy,\ u \in [0, 4])$$
> $$= \int_0^4 \sqrt{u}\,du = \left[\frac{2u^{3/2}}{3}\right]_0^4 = \frac{2 \cdot 8}{3} = \frac{16}{3}$$
>
> **Por qué importa:** la región no se describe con una sola función $y = f(x)$ sobre un intervalo limpio; con $dy$ la frontera es una sola rama y la integral es directa.

> [!example] 🔢 Ejemplo 5 — Curva con bucle: $x = y^3 - 3y$
>
> **Paso 1 — Cruces con el eje $y$:** $y^3 - 3y = 0 \Rightarrow y(y^2 - 3) = 0 \Rightarrow y = 0, \pm\sqrt{3}$.
>
> **Paso 2 — El bucle vive entre** $y = -\sqrt{3}$ y $y = \sqrt{3}$.
>
> **Paso 3 — Lados del bucle:**
>
> - Para $y \in (-\sqrt{3}, 0)$: $x = y^3 - 3y > 0$ (derecha).
> - Para $y \in (0, \sqrt{3})$: $x = y^3 - 3y < 0$ (izquierda).
>
> **Paso 4 — Área del bucle** (valor absoluto por tramo):
> $$A = \int_{-\sqrt{3}}^0 (y^3 - 3y)\,dy + \int_0^{\sqrt{3}} -(y^3 - 3y)\,dy = \frac{9}{4} + \frac{9}{4} = \frac{9}{2}$$
>
> **Por qué importa:** el orden de los lados se invierte a mitad del bucle; sin partir la integral, las dos mitades se cancelarían y el área saldría $0$.

---

## 🌍 Aplicaciones

> [!info] 🏗️ Ingeniería — secciones transversales
>
> Para una viga con perfil definido por límites horizontales, derecha $x = f(y)$ e izquierda $x = g(y)$, el área de la sección transversal es:
> $$A = \int_c^d [f(y) - g(y)]\,dy$$

> [!tip] 💧 Hidráulica — área mojada en canales
>
> Para un canal con forma parabólica $y = ax^2$ (es decir, $x = \pm\sqrt{y/a}$):
>
> - Ancho de la superficie a altura $h$: $2\sqrt{\frac{h}{a}}$.
> - Área mojada: $A = \int_0^h 2\sqrt{\frac{y}{a}}\,dy = \frac{4}{3}\sqrt{\frac{h^3}{a}}$.
>
> **Por qué importa:** el área mojada manda en el diseño hidráulico (caudal, rozamiento); con $dy$ sale en una integral.

> [!warning] ⚖️ Centroides con $dy$
>
> Para una región entre $x = f(y)$ y $x = g(y)$:
> $$\bar{x} = \frac{1}{A}\int_c^d \frac{f(y) + g(y)}{2}\,[f(y) - g(y)]\,dy \qquad \bar{y} = \frac{1}{A}\int_c^d y\,[f(y) - g(y)]\,dy$$
>
> **Por qué importa:** la misma integral que da el área, con un factor más, da la coordenada del centroide; por eso el orden derecha-menos-izquierda importa también en física.

---

## ⚠️ Errores Comunes

> [!warning] 🚨 Errores frecuentes en integración $dy$
>
> 1. **Confundir derecha-izquierda con superior-inferior:**
>    - ❌ $\int [g(y) - f(y)]\,dy$ cuando $f(y) > g(y)$
>    - ✅ Siempre: derecha menos izquierda
> 2. **Límites incorrectos:**
>    - ❌ usar límites de $x$ cuando se integra en $y$
>    - ✅ los límites deben ser valores de $y$: $[c, d]$
> 3. **No verificar el orden de las funciones:**
>    - ❌ asumir que la primera función está a la derecha
>    - ✅ evaluar en un punto para verificar posiciones
> 4. **Olvidar ramas múltiples:**
>    - ❌ usar solo $x = \sqrt{y}$ cuando hay $x = \pm\sqrt{y}$
>    - ✅ considerar todas las ramas relevantes
> 5. **Conversión incorrecta de ecuaciones:**
>    - ❌ $y = x^2 \Rightarrow x = y^2$ (¡falso!)
>    - ✅ $y = x^2 \Rightarrow x = \pm\sqrt{y}$
>
> **Por qué importa:** los cinco errores son de planteamiento, no de cálculo: la integral puede salir perfecta y el área igualmente mal. La verificación con un bosquejo los detecta a todos.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Halla el área entre $x = y + 2$ y $x = y^2$.
>
> > [!success]- ✅ Solución
> > Cruces: $y^2 = y + 2 \Rightarrow (y+1)(y-2) = 0 \Rightarrow y = -1, 2$; en $y = 0$ vale $2 > 0$, así que la recta está a la derecha.
> > $$A = \int_{-1}^2 (y + 2 - y^2)\,dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^2 = \frac{10}{3} + \frac{7}{6} = \frac{9}{2}$$
> > **Lección:** misma estructura que el ejemplo 2 de la nota anterior, pero en horizontal ✓

> [!example] 📋 Planteamiento
>
> Halla el área entre $x = \sqrt{y}$ y $x = \frac{y}{2}$.
>
> > [!success]- ✅ Solución
> > Cruces: $\sqrt{y} = \frac{y}{2} \Rightarrow y = \frac{y^2}{4} \Rightarrow y(y - 4) = 0 \Rightarrow y = 0, 4$; en $y = 1$: $\sqrt{1} = 1 > \frac{1}{2}$ → $\sqrt{y}$ a la derecha.
> > $$A = \int_0^4 \left(\sqrt{y} - \frac{y}{2}\right)dy = \left[\frac{2y^{3/2}}{3} - \frac{y^2}{4}\right]_0^4 = \frac{16}{3} - 4 = \frac{4}{3}$$
> > **Lección:** comparar un punto interior fija el orden antes de integrar ✓

> [!example] 📋 Planteamiento
>
> Calcula el área entre $y = x^2$ y $y = 4$ primero con $dy$ y luego con $dx$, y compara.
>
> > [!success]- ✅ Solución
> > **Con $dy$:** $x = \pm\sqrt{y}$, así que $A = \int_0^4 2\sqrt{y}\,dy = \left[\frac{4y^{3/2}}{3}\right]_0^4 = \frac{32}{3}$.
> > **Con $dx$:** $A = 2\int_0^2 (4 - x^2)\,dx = 2\left[4x - \frac{x^3}{3}\right]_0^2 = 2 \cdot \frac{16}{3} = \frac{32}{3}$.
> > **Lección:** las dos variables dan lo mismo; la que ahorra ramas es la que conviene ✓

> [!example] 📋 Planteamiento
>
> Halla el área del bucle de $x = y^3 - 4y$.
>
> > [!success]- ✅ Solución
> > Cruces con el eje $y$: $y(y^2 - 4) = 0 \Rightarrow y = 0, \pm 2$. El bucle vive entre $-2$ y $2$, y cambia de lado en $y = 0$:
> > $$A = \int_{-2}^0 (y^3 - 4y)\,dy + \int_0^2 -(y^3 - 4y)\,dy = 2\int_0^2 (4y - y^3)\,dy = 2\left[2y^2 - \frac{y^4}{4}\right]_0^2 = 2(8 - 4) = 8$$
> > **Lección:** bucle simétrico: se calcula la mitad y se duplica ✓

> [!example] 📋 Planteamiento
>
> Halla el área entre $x = \ln y$ y $x = 0$ para $y \in [1, e]$.
>
> > [!success]- ✅ Solución
> > En $[1, e]$ se cumple $\ln y \geq 0$, así que la curva está a la derecha del eje $y$:
> > $$A = \int_1^e \ln y\,dy = \left[y\ln y - y\right]_1^e = (e - e) - (0 - 1) = 1$$
> > **Lección:** $\int \ln y\,dy = y\ln y - y$ (por partes); el área del "recuadro logarítmico" vale exactamente $1$ ✓

> [!example] 📋 Planteamiento
>
> Un canal tiene perfil $y = \frac{1}{4}x^2$ (con $x$ en metros). Halla el área mojada hasta una altura $h = 4$ m.
>
> > [!success]- ✅ Solución
> > El perfil equivale a $x = \pm 2\sqrt{y}$, así que el ancho a altura $y$ es $4\sqrt{y}$:
> > $$A = \int_0^4 4\sqrt{y}\,dy = 4\left[\frac{2y^{3/2}}{3}\right]_0^4 = \frac{8}{3} \cdot 8 = \frac{64}{3} \text{ m}^2$$
> > **Lección:** la fórmula general $A = \frac{4}{3}\sqrt{\frac{h^3}{a}}$ con $a = \frac{1}{4}$, $h = 4$ da lo mismo: $\frac{4}{3}\sqrt{\frac{64}{1/4}} = \frac{64}{3}$ ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Planteo el área respecto a $y$ como $\int_c^d [f(y) - g(y)]\,dy$ con $f$ a la derecha y $g$ a la izquierda.
> - [ ] Convierto ecuaciones entre $y = f(x)$ y $x = g(y)$ respetando las ramas ($\pm$).
> - [ ] Uso valores de $y$ (no de $x$) como límites de integración cuando integro en $dy$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Decido entre $dx$ y $dy$ con criterios: forma de las curvas, orientación de los límites y ramas.
> - [ ] Parto la integral en tramos cuando el orden derecha-izquierda cambia (bucles, cruces).
> - [ ] Verifico el resultado con una comprobación geométrica (ej. el círculo da $\pi r^2$).

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo regiones complejas que en $dx$ exigen dos integrales con una sola en $dy$.
> - [ ] Aplico el área respecto a $y$ a secciones transversales, canales hidráulicos y centroides.
> - [ ] Calculo áreas de bucles de curvas paramétricas implícitas usando valor absoluto por tramo.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage): aplicaciones del integral definido — áreas entre curvas y elección de variable.
> - G. Strang, *Calculus* (Wellesley-Cambridge): franjas horizontales y la simetría entre $dx$ y $dy$.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas|02 - Área entre Curvas]] — el mismo concepto con franjas verticales.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el caso base de una curva contra el eje.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas para evaluar las integrales resultantes.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/04 - Asíntotas en Integrales Definidas|04 - Asíntotas en Integrales Definidas]] — contexto más amplio de aplicaciones.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] — extensiones a otros sistemas.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — discos y arandelas con la misma lógica en $dy$.
>
> **Conexiones interdisciplinarias:** ingeniería (secciones transversales de vigas), hidráulica (área mojada de canales), física (centroides) y economía (aplicaciones con tasas horizontales).

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u7

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la fórmula del área respecto a $y$?::$A = \int_c^d [f(y) - g(y)]\,dy$ con $f$ la curva de la **derecha** y $g$ la de la **izquierda**.
> - ¿Qué forma tiene la franja en este método?::Horizontal: ancho $f(y) - g(y)$ y altura $dy$, así que el rectángulo vale $[f(y) - g(y)]\,dy$.
> - ¿Cuándo conviene $dy$ en lugar de $dx$::Cuando las curvas vienen como $x = f(y)$, los límites son horizontales, hay ramas múltiples en $x$ o la región es "ancha y baja".
> - ¿Qué pasa si el orden derecha-izquierda cambia dentro de $[c,d]$?::Hay que partir la integral en tramos (o usar valor absoluto); en un bucle, el lado se invierte a mitad de recorrido.
> - ¿Cómo se convierte $y = x^2$ a forma $x = g(y)$?::$x = \pm\sqrt{y}$ (dos ramas); escribir $x = y^2$ es el error clásico.
> - ¿Cuánto vale el área del disco $x^2 + y^2 \leq r^2$ vía $dy$?::$\int_{-r}^{r} 2\sqrt{r^2 - y^2}\,dy = \pi r^2$: sirve para verificar que se usaron las dos ramas.
> - ¿Qué significa que el resultado salga negativo?::Que se invirtió el orden de la resta en algún tramo: el área geométrica es siempre positiva.
> - ¿Cómo se verifica rápido un área en $dy$?::Con una comprobación geométrica conocida (disco, triángulo, parábola) o comparando con el cálculo en $dx$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas|02 - Área entre Curvas]] — el concepto base y el método con $dx$.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — una sola curva contra el eje.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas para evaluar las integrales resultantes.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/04 - Asíntotas en Integrales Definidas|04 - Asíntotas en Integrales Definidas]] — contexto más amplio de aplicaciones.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] — extensiones a otros sistemas de coordenadas.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — discos y arandelas con la misma lógica en $dy$.
>
> **Conexiones interdisciplinarias:** funciones inversas (para transformar entre $y = f(x)$ y $x = g(y)$), hidráulica (área mojada), física (centroides) y economía (aplicaciones con tasas).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: cruces limpios en $y$ y orden derecha-izquierda.
> - Después el 3: la misma región en las dos variables, para sentir la elección.
> - Cierra con 4, 5 y 6: bucle, logaritmo y canal hidráulico.
> - Cuando lo tengas, continúa con [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] y luego los volúmenes de la misma unidad.

---

**Tags:** #MATG1045 #unidad7 #area-entre-curvas-respecto-a-y #integrales #aplicaciones #areas #integracion-dy #franjas-horizontales #transformacion-ecuaciones

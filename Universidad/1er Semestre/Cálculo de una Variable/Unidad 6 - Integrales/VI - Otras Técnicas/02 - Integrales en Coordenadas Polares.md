---
dg-publish: true
tags: [MATG1045, unidad6, integrales-en-coordenadas-polares, integrales, coordenadas-polares, integrales-dobles, jacobiano, sectores-circulares]
---

# 🧮 Integrales en Coordenadas Polares

## 🎯 Introducción

> [!info] 💡 Qué son y por qué importa
>
> Las **coordenadas polares** describen un punto por su distancia al origen $r \geq 0$ y su ángulo $\theta$ medido desde el eje $x$ positivo. Transforman las integrales sobre regiones circulares, espirales y cardiodes en expresiones **radiales** mucho más simples, porque el elemento de área se vuelve $dA = r\,dr\,d\theta$.
>
> **Por qué importa:** la mitad de las integrales imposibles en cartesianas (esas con $x^2 + y^2$, o sobre un círculo completo) son triviales en polares; está detrás de las aplicaciones físicas de temperatura, campo eléctrico y ondas circulares.
>
> **Ejemplo:** $\iint_{x^2+y^2 \leq R^2} (x^2 + y^2)\,dA$ vale $\frac{\pi R^4}{2}$ — la integral cartesiana es un dolor de cabeza; en polares es $\int_0^{2\pi}\int_0^R r^3\,dr\,d\theta$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — sistema polar, transformación $(r, \theta) \leftrightarrow (x, y)$, jacobiano y elemento de área.
> - **Procedimiento Paso a Paso** — las tres regiones polares típicas y la estrategia POLAR.
> - **Ejemplos Resueltos** — áreas de regiones (círculo, cardioide, corona, cono) y de funciones.
> - **Curvas Comunes** — catálogo de curvas y sus rangos de $\theta$.
> - **Ejercicios Propuestos** — seis plantillas, de áreas completas al jacobiano.
>
> **Por qué importa:** el factor $r$ del jacobiano está en todos los pasos; el mapa empieza definiéndolo para que nunca falte.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Sistema polar y elemento de área
>
> Un punto en el plano puede describirse polares mediante:
>
> - **Radio** $r \geq 0$: distancia al origen.
> - **Ángulo** $\theta$: medido desde el eje $x$ positivo.
>
> **Transformación Polares → Cartesianas:**
> $$x = r\cos\theta, \qquad y = r\sin\theta$$
>
> **Transformación Cartesianas → Polares:**
> $$r = \sqrt{x^2 + y^2}, \qquad \theta = \arctan\left(\frac{y}{x}\right)$$
>
> **Jacobiano de la transformación:**
> $$J = \left|\frac{\partial(x,y)}{\partial(r,\theta)}\right| = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r\cos^2\theta + r\sin^2\theta = r$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Integrales_en_Coordenadas_Polares_01.svg]]
>
> **Se lee así:** el diagrama tiene dos caminos separados: a la izquierda, una cadena de cuatro rectángulos que va del sector circular infinitesimal a sus dimensiones y termina en el producto del incremento radial por el arco; a la derecha, una visualización hecha con caracteres, donde una franja sombreada entre dos radios muestra la altura aproximada y la apertura $d\theta$.
>
> **Por qué importa:** **el factor $r$ no sale de la nada**, aparece porque el arco crece con el radio, así que las zonas lejanas del origen aportan más área. Olvidarlo es el error número uno de la nota, y este diagrama te lo deja ver en vez de memorizarlo.
>
> **Ejemplo:** al calcular el área de la cardioide $r = a(1 + \cos\theta)$ de la nota, el integrando incluye $r$ porque $dA = r\,dr\,d\theta$.

> [!tip] 📐 Construcción del elemento de área
>
> Un sector circular infinitesimal tiene:
>
> - **Radio interior:** $r$; **radio exterior:** $r + dr$; **ángulo:** $d\theta$.
> - **Anchura radial:** $dr$; **altura tangencial:** $r \cdot d\theta$ (longitud del arco).
>
> **Por tanto:** $dA = \text{anchura} \times \text{altura} = dr \times (r\,d\theta) = r\,dr\,d\theta$.
>
> **Por qué importa:** la deducción gráfica muestra el porqué del factor antes de la fórmula abstracta del jacobiano.

> [!tip] 📐 Integral doble en coordenadas polares y regiones típicas
>
> Para una función $f(x,y) = g(r, \theta)$ sobre una región $R$:
> $$\iint_R f(x,y)\,dA = \int_{\alpha}^{\beta} \int_{r_1(\theta)}^{r_2(\theta)} g(r, \theta)\,r\,dr\,d\theta$$
>
> **Las tres regiones polares típicas:**
>
> 1. **Región polar simple:** $R = \{(r, \theta) : \alpha \leq \theta \leq \beta,\, 0 \leq r \leq h(\theta)\}$
> $$\iint_R f\,dA = \int_{\alpha}^{\beta} \int_0^{h(\theta)} g(r, \theta)\,r\,dr\,d\theta$$
> 2. **Corona circular:** $R = \{(r, \theta) : 0 \leq \theta \leq 2\pi,\, r_1 \leq r \leq r_2\}$
> $$\iint_R f\,dA = \int_0^{2\pi} \int_{r_1}^{r_2} g(r, \theta)\,r\,dr\,d\theta$$
> 3. **Sector circular:** $R = \{(r, \theta) : \alpha \leq \theta \leq \beta,\, 0 \leq r \leq R\}$
> $$\iint_R f\,dA = \int_{\alpha}^{\beta} \int_0^{R} g(r, \theta)\,r\,dr\,d\theta$$
>
> **Por qué importa:** la clasificación cubre el 90% de las regiones que se ven en el curso: círculo completo (simple), corona (anillo) y sector (quesito).

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🔎 Algoritmo POLAR
>
> - **P** — Problema: identificar si polares simplifica ($x^2 + y^2$, círculos, simetría radial).
> - **O** — Origen: colocar el origen estratégicamente cuando la región lo permita.
> - **L** — Límites: determinar $r_1(\theta)$ y $r_2(\theta)$, y el rango de $\theta$.
> - **A** — Área: recordar $dA = r\,dr\,d\theta$.
> - **R** — Resolver: integrar primero en $r$, luego en $\theta$.
>
> **Por qué importa:** las cinco letras son el procedimiento completo; saltarse la **L** (límites) y poner $0 \leq r \leq \pi$ o $0 \leq \theta \leq 2\pi$ "por costumbre" es el error más caro.

> [!tip] 📐 Fórmulas fundamentales
>
> **Transformación:** $x = r\cos\theta$, $y = r\sin\theta$, $dA = r\,dr\,d\theta$.
>
> **Integral doble:**
> $$\iint_R f(x,y)\,dA = \int_{\alpha}^{\beta} \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta$$
>
> **Área de región polar:**
> $$A = \int_{\alpha}^{\beta} \int_0^{r(\theta)} r\,dr\,d\theta = \frac{1}{2}\int_{\alpha}^{\beta} [r(\theta)]^2\,d\theta$$
>
> **Por qué importa:** la segunda fórmula convierte áreas de regiones polares en una integral simple de $r^2$; es la misma base de la nota de áreas polares de la unidad 7.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Área de un círculo $x^2 + y^2 \leq a^2$
>
> **En polares:** $0 \leq r \leq a$, $0 \leq \theta \leq 2\pi$:
> $$A = \int_0^{2\pi} \int_0^a r\,dr\,d\theta = \int_0^{2\pi} \left[\frac{r^2}{2}\right]_0^a d\theta = \frac{a^2}{2} \cdot 2\pi = \pi a^2$$
>
> **Por qué importa:** el caso base: confirma que la fórmula recupera el área conocida.

> [!example] 🔢 Ejemplo 2 — Área de la cardioide $r = a(1 + \cos\theta)$
>
> **En polares:** $0 \leq \theta \leq 2\pi$, $0 \leq r \leq a(1 + \cos\theta)$:
> $$A = \int_0^{2\pi} \int_0^{a(1 + \cos\theta)} r\,dr\,d\theta = \frac{1}{2}\int_0^{2\pi} a^2(1 + \cos\theta)^2\,d\theta$$
> $$= \frac{a^2}{2}\int_0^{2\pi} \left(1 + 2\cos\theta + \cos^2\theta\right)d\theta = \frac{a^2}{2} \cdot 3\pi = \frac{3\pi a^2}{2}$$
>
> **Por qué importa:** el ejemplo canónico de región polar simple con frontera dependiente de $\theta$; verifícalo con la fórmula del apartado anterior.

> [!example] 🔢 Ejemplo 3 — Corona circular $r_1^2 \leq x^2 + y^2 \leq r_2^2$
>
> **En polares:** $r_1 \leq r \leq r_2$, $0 \leq \theta \leq 2\pi$:
> $$A = \int_0^{2\pi} \int_{r_1}^{r_2} r\,dr\,d\theta = \int_0^{2\pi} \left[\frac{r^2}{2}\right]_{r_1}^{r_2} d\theta = \pi\left(r_2^2 - r_1^2\right)$$
>
> **Por qué importa:** confirma que el anillo es "círculo mayor menos círculo menor"; útil como verificación en cualquier región con $r_1 > 0$.

> [!example] 🔢 Ejemplo 4 — $f(x, y) = x^2 + y^2$ sobre el círculo $x^2 + y^2 \leq R^2$
>
> **En polares:** $f = r^2$:
> $$I = \int_0^{2\pi} \int_0^R r^2 \cdot r\,dr\,d\theta = \int_0^{2\pi} \frac{R^4}{4}\,d\theta = \frac{\pi R^4}{2}$$
>
> **Por qué importa:** el integrando $x^2 + y^2$ se vuelve $r^2$ y el elemento $r\,dr$ cierra el patrón $r^3$; es el ejercicio típico de examen.

> [!example] 🔢 Ejemplo 5 — Integral de Gauss $I = \iint_{\mathbb{R}^2} e^{-(x^2 + y^2)}\,dA$
>
> **En polares:** $I = \int_0^{2\pi} \int_0^{\infty} e^{-r^2}\,r\,dr\,d\theta$.
>
> Sustitución $u = r^2$, $du = 2r\,dr$:
> $$I = \frac{1}{2}\int_0^{2\pi} \left[-e^{-u}\Big|_0^{\infty}\right]d\theta = \frac{1}{2} \cdot 2\pi = \pi$$
>
> **Por qué importa:** la fórmula de Gauss se deriva de aquí; es la integral impropia doble más famosa del currículo.

> [!example] 🔢 Ejemplo 6 — Volumen bajo $z = \sqrt{x^2 + y^2}$ sobre $x^2 + y^2 \leq 4$
>
> **En polares:** $z = r$, región $0 \leq r \leq 2$:
> $$V = \int_0^{2\pi} \int_0^2 r \cdot r\,dr\,d\theta = \int_0^{2\pi} \frac{8}{3}\,d\theta = \frac{16\pi}{3}$$
>
> **Por qué importa:** el cono truncado en $r = 2$ tiene vía directa en polares: el integrando ya es $r$ y el elemento aporta otro $r$.

---

## 🌀 Curvas Comunes y Sus Rangos

> [!info] ⭐ Catálogo de curvas polares
>
> | Curva | Ecuación polar | Rango de $\theta$ |
> |---|---|---|
> | Círculo | $r = a$ | $[0, 2\pi]$ |
> | Cardioide | $r = a(1 + \cos\theta)$ | $[0, 2\pi]$ |
> | Rosa de 3 pétalos | $r = a\cos(3\theta)$ | $[0, \pi]$ |
> | Rosa de 4 pétalos | $r = a\cos(2\theta)$ | $[0, 2\pi]$ |
> | Espiral de Arquímedes | $r = a\theta$ | $[0, n\pi]$ |
> | Lemniscata | $r^2 = a^2\cos(2\theta)$ | $[-\pi/4, \pi/4] \cup [3\pi/4, 5\pi/4]$ |
>
> **Por qué importa:** es la tabla de referencia antes de plantear límites: $n$ impar → $n$ pétalos en $[0, \pi]$; $n$ par → $2n$ pétalos en $[0, 2\pi]$.
>
> **Áreas útiles:** círculo $\pi a^2$ · cardioide $\frac{3\pi a^2}{2}$ · pétalo $\frac{\pi a^2}{4n}$.

---

## ⚠️ Errores Comunes y Lista de Verificación

> [!warning] 🚨 Errores frecuentes
>
> 1. **Olvidar el factor $r$ en $dA$:**
>    - ❌ $\iint_R f(r, \theta)\,dr\,d\theta$
>    - ✅ $\iint_R f(r, \theta)\,r\,dr\,d\theta$
> 2. **Límites de integración incorrectos:**
>    - Para $r = f(\theta)$, los límites de $r$ son $0 \leq r \leq f(\theta)$.
>    - NO: constante $\leq r \leq$ constante.
> 3. **Transformación incompleta de la función:**
>    - Si $f(x, y) = x^2 + y^2$, entonces $f(r, \theta) = r^2$; no basta con cambiar los símbolos $x, y$ por $r, \theta$ sin transformar la expresión completa.
> 4. **Rangos de $\theta$ mal determinados:**
>    - Para curvas simétricas, verificar si se necesita $\theta \in [0, \pi]$ o $[0, 2\pi]$; integrar $[0, 2\pi]$ una rosa de 3 pétalos la recorre dos veces.
>
> **Por qué importa:** los cuatro son errores de planteamiento; la respuesta puede "salir del gusto" y aun así estar mal por un factor o un rango.

> [!tip] ✅ Lista de verificación
>
> - ¿Incluí el factor $r$ en el elemento de área?
> - ¿Transformé correctamente la función $f(x, y)$?
> - ¿Los límites de $r$ dependen correctamente de $\theta$?
> - ¿El rango de $\theta$ cubre toda la región una sola vez?
> - ¿Verificé la simetría de la región (ahorra integrar $2\pi$ completo)?
>
> **Por qué importa:** esta lista es el antídoto mecánico a los errores del bloque anterior; pasarla toma dos minutos.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Halla el área de la rosa $r = 2\cos(2\theta)$.
>
> > [!success]- ✅ Solución
> > $n = 2$ (par) → 4 pétalos; cada pétalo: $\frac{1}{2}\int_{-\pi/4}^{\pi/4} 4\cos^2(2\theta)\,d\theta = \pi/2$.
> > Total: $A = 4 \cdot \frac{\pi}{2} = 2\pi$.
> > **Lección:** n par → $2n$ pétalos en $[0, 2\pi]$; cada uno vale $\frac{\pi a^2}{4n}$ con $a = 2$: $\frac{\pi \cdot 4}{8} = \frac{\pi}{2}$ ✓

> [!example] 📋 Planteamiento
>
> Halla el área encerrada por la lemniscata $r^2 = 4\cos(2\theta)$.
>
> > [!success]- ✅ Solución
> > Un lazo existe donde $\cos 2\theta \geq 0$: $\theta \in [-\frac{\pi}{4}, \frac{\pi}{4}]$. La región completa son dos lazos iguales:
> > $$A = 2 \cdot \frac{1}{2}\int_{-\pi/4}^{\pi/4} 4\cos(2\theta)\,d\theta = 4\left[\frac{\sin 2\theta}{2}\right]_{-\pi/4}^{\pi/4} = 4\left(\frac{1}{2} + \frac{1}{2}\right) = 4$$
> > **Lección:** el área total de ambos lazos es $4$ ($2$ por lazo); la lemniscata se integra como $r^2$ directo, sin raíz ✓

> [!example] 📋 Planteamiento
>
> Halla $\iint_R (x^2 + y^2)\,dA$ sobre el disco de radio $3$.
>
> > [!success]- ✅ Solución
> > En polares: $f = r^2$, $0 \leq r \leq 3$, $0 \leq \theta \leq 2\pi$:
> > $$I = \int_0^{2\pi} \int_0^3 r^3\,dr\,d\theta = 2\pi \cdot \frac{81}{4} = \frac{81\pi}{2}$$
> > **Lección:** el mismo patrón $r^3$ del ejemplo 4 con $R = 3$ ✓

> [!example] 📋 Planteamiento
>
> Halla el volumen del sólido bajo $z = \sqrt{x^2 + y^2}$ sobre $x^2 + y^2 \leq 9$.
>
> > [!success]- ✅ Solución
> > En polares: $z = r$; $V = \int_0^{2\pi} \int_0^3 r^2\,dr\,d\theta = 2\pi \cdot 9 = 18\pi$.
> > Verificación: cilindro de radio $3$ y altura $3$ ($27\pi$) menos el cono de radio $3$ y altura $3$ ($\frac{1}{3}\pi \cdot 9 \cdot 3 = 9\pi$) $= 18\pi$ ✓
> > **Lección:** "volumen bajo $z = f$ sobre $D$" siempre es $\iint_D f\,dA$, aunque el resultado no sea un sólido clásico ✓

> [!example] 📋 Planteamiento
>
> Aproxima con un método adecuado el área encerrada por la espiral $r = \theta$ entre $\theta = 0$ y $\theta = 2\pi$.
>
> > [!success]- ✅ Solución
> > $A = \frac{1}{2}\int_0^{2\pi} \theta^2\,d\theta = \frac{1}{2} \cdot \frac{(2\pi)^3}{3} = \frac{4\pi^3}{3} \approx 41.34$.
> > **Lección:** la espiral de Arquímedes se integra exacto ($A = \frac{4\pi^3 a^2}{3}$ para $r = a\theta$ con $a = 1$) ✓

> [!example] 📋 Planteamiento
>
> ¿Cuál es el error en $\int_0^{2\pi} \int_0^2 f(r, \theta)\,dr\,d\theta$ para integrar sobre el disco de radio $2$?
>
> > [!success]- ✅ Solución
> > Falta el jacobiano: la integral correcta es $\int_0^{2\pi} \int_0^2 f(r, \theta)\,r\,dr\,d\theta$. Además, ningún $f$ puede integrarse sobre el disco con esa forma si $f$ depende de $x, y$ sin transformarlas: $f$ debe estar en función de $r$ y $\theta$.
> > **Lección:** $dA = r\,dr\,d\theta$, siempre, para cualquier región polar ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Convierto puntos y funciones entre cartesianas y polares con las fórmulas $x = r\cos\theta$, $y = r\sin\theta$.
> - [ ] Reconozco $dA = r\,dr\,d\theta$ como el elemento diferencial de área (con el factor $r$).
> - [ ] Identifico las tres regiones polares típicas: simple $0 \leq r \leq h(\theta)$, corona $r_1 \leq r \leq r_2$ y sector $0 \leq r \leq R$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Planteo integrales dobles en polares transformando $f(x, y)$ en $g(r, \theta)$ antes de integrar.
> - [ ] Calculo áreas y volúmenes en regiones con simetría radial con la estrategia POLAR completa.
> - [ ] Uso las fórmulas de referencia ($\pi a^2$, $\frac{3\pi a^2}{2}$, $\pi(r_2^2 - r_1^2)$) como verificación de resultados.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Derivo el jacobiano $r$ a partir de la geometría del sector y lo relaciono con $dA = r\,dr\,d\theta$.
> - [ ] Manejo rosas, cardiodes, espirales y lemniscatas con los rangos de $\theta$ correctos.
> - [ ] Exploro los límites $\theta \in [0, \pi]$ para $n$ impar y $[0, 2\pi]$ para $n$ par en rosas de $n$ pétalos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), caps. 15.4 / 15.5: integración en coordenadas polares y dobles integrales.
> - G. Strang, *Calculus* (Wellesley-Cambridge): transformaciones de coordenadas y jacobiano.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la suma que origina cualquier integral.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — cuando el límite superior se escapa (integral de Gauss).
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] — la misma fórmula en dimensión 1 y el área de pétalos.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — las mismas regiones generando sólidos.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] — el método numérico para cuando no hay forma cerrada.
>
> **Conexiones interdisciplinarias:** física (temperatura, campo eléctrico, ondas circulares), ingeniería (antenas, radiación), geometría diferencial (superficies de revolución) y análisis numérico (cubatura en dominios circulares).

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es el elemento diferencial de área en polares?::$dA = r\,dr\,d\theta$; el factor $r$ viene del jacobiano de $(x,y) \to (r,\theta)$.
> - ¿Cómo es la integral doble en polares?::$\iint_R f\,dA = \int_\alpha^\beta \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta$.
> - ¿Cuál es el jacobiano de la transformación?::$J = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r$.
> - ¿Cuál es el área de la región polar $0 \leq r \leq r(\theta)$?::$A = \frac{1}{2}\int_\alpha^\beta [r(\theta)]^2\,d\theta$.
> - ¿Cuál es el área de los 4 pétalos de $r = a\cos(2\theta)$?::$4 \cdot \frac{\pi a^2}{4 \cdot 2} = \frac{\pi a^2}{2}$; cada pétalo vale $\frac{\pi a^2}{4n}$ con $n = 2$.
> - ¿Cuál es el área de la cardioide $r = a(1 + \cos\theta)$?::$\frac{3\pi a^2}{2}$.
> - ¿Qué pasa con los rosas de $n$ impar?::Tienen $n$ pétalos y basta $\theta \in [0, \pi]$ porque al otro lado se repite la rosa.
> - ¿Qué es el error número uno de polares?::Olvidar el factor $r$ en el elemento de área.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la definición que subyace a cualquier integral.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] — cuando no hay forma cerrada o el rango es incómodo.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] — la misma fórmula en dimensión 1.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — dónde van los volúmenes calculados en polares.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — cuándo la integral de Gauss usa criterios.
>
> **Conexiones interdisciplinarias:** física (temperatura y campos con simetría radial), matemáticas (jacobianos y transformaciones generales), ingeniería (antenas, radiación) y geometría (curvas y superficies de revolución).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 3: área entre círculo y rosa, y $\int\!\!\int (x^2 + y^2)$ sobre disco.
> - Después el 2: lemniscata, con sus dos lazos y su rango real de $\theta$.
> - Cierra con 4 y 6: volumen bajo $z = r$ y el jacobiano ausente.
> - Cuando lo tengas, continúa con [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] y repasa [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]].

---

**Tags:** #MATG1045 #unidad6 #integrales-en-coordenadas-polares #integrales #coordenadas-polares #integrales-dobles #jacobiano #sectores-circulares

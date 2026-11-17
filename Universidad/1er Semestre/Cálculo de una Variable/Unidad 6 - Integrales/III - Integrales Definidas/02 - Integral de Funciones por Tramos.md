---
dg-publish: true
tags: [MATG1045, unidad6, integral-de-funciones-por-tramos, funciones-a-trozos, puntos-de-ruptura, aditividad-intervalo, funcion-escalón, funcion-signo, discontinuidades]
---

# 🧩 Integral de Funciones por Tramos

## 🎯 Introducción

> [!info] 💡 Concepto fundamental
>
> Una **función por tramos** (o función definida a trozos) es la que se define con expresiones distintas en intervalos distintos de su dominio. Integrarla no exige una técnica nueva: exige **partir el intervalo** en los puntos donde cambia la definición y sumar lo que salga en cada tramo.
>
> **Por qué importa:** la regla de aditividad respecto al intervalo, $\int_a^b = \int_a^c + \int_c^b$, es la que convierte un problema con varias definiciones en varios problemas con una sola. Sin esa división, la integral simplemente no está bien planteada.
>
> **Ejemplo:** $\int_{-2}^{3} |x|\,dx$ no tiene una fórmula única para $|x|$; se parte en $x = 0$ y se suman las dos mitades.

> [!tip] 🎯 Por qué aparecen en la carrera
>
> - Modelan **situaciones reales** con comportamientos diferentes en distintos rangos.
> - Aparecen en **física** (leyes que cambian según condiciones: fricción estática vs. cinética).
> - Son la base del **procesamiento de señales** (pulsos rectangulares, función escalón).
> - Estructuran la **economía** (funciones de costo, impuestos progresivos).
> - Generan las **funciones especiales** (escalón de Heaviside, signo, parte entera).
> - Sostienen la **probabilidad** (distribuciones mixtas y variables con soporte partido).
>
> **Por qué importa:** casi todos los modelos de ingeniería que verás en circuitos, control o señales son funciones por tramos; el día de mañana el tramo lo pondrá la ley física y la integral la pondrás tú.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Función definida por tramos
>
> Una función $f(x)$ está **definida por tramos** en $[a,b]$ si existen puntos
>
> $$a = x_0 < x_1 < x_2 < \cdots < x_n = b$$
>
> tales que en cada subintervalo $[x_{i-1}, x_i)$ la función tiene una expresión propia:
>
> $$f(x) = \begin{cases} f_1(x) & \text{si } x \in [x_0, x_1) \\ f_2(x) & \text{si } x \in [x_1, x_2) \\ \vdots & \vdots \\ f_n(x) & \text{si } x \in [x_{n-1}, x_n] \end{cases}$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Integral_de_Funciones_por_Tramos_01.svg]]
>
> **Se lee así:** un mapa mental con el nodo central "Funciones Por Tramos" y cuatro ramas. La primera es la **definición**, con sus hijos múltiples expresiones, intervalos diferentes, puntos de ruptura y continuidad. La segunda es la **integración**, con división del intervalo, integral por tramos, suma de resultados y evaluación de límites. La tercera agrupa los **tipos especiales** (escalón, valor absoluto, signo, trigonométricas modificadas) y la cuarta las **aplicaciones** (modelos físicos, economía, procesamiento de señales, probabilidad).
>
> **Por qué importa:** el mapa ordena el tema entero de un vistazo: qué es, cómo se integra y para qué sirve. Te evita integrar la expresión equivocada en un subintervalo, que es el error más caro de esta técnica.
>
> **Ejemplo:** la función escalón de Heaviside modela un interruptor; su integral $\int_{-a}^{b} H(x)\,dx = b$ es la energía que pasa cuando el interruptor se cierra en $x = 0$.

> [!warning] ⚠️ Los cinco elementos que hay que mirar siempre
>
> - **Puntos de ruptura:** $x_1, x_2, \ldots, x_{n-1}$, donde cambia la definición.
> - **Intervalos:** cada tramo tiene su propia expresión.
> - **Inclusión de extremos:** cuidado con los intervalos abiertos y cerrados.
> - **Continuidad:** puede ser continua o discontinua en los puntos de ruptura.
> - **Integrabilidad:** es integrable si cada tramo es integrable (en la práctica, continuo).
>
> **Por qué importa:** el cuarto y el quinto son los que deciden si la integral existe; los tres primeros deciden cómo se escribe. Los puntos de ruptura son **el corazón** del método.

---

## 🧮 Teorema de integración por tramos

> [!success] ✅ Teorema de integración por tramos
>
> Si $f(x)$ está definida por tramos en $[a,b]$ con puntos de ruptura $x_1, x_2, \ldots, x_{n-1}$ y cada tramo es integrable, entonces
>
> $$\int_a^b f(x)\,dx = \sum_{i=1}^{n} \int_{x_{i-1}}^{x_i} f_i(x)\,dx$$
>
> donde $f_i(x)$ es la expresión de $f$ en $[x_{i-1}, x_i]$.
>
> **Por qué importa:** la igualdad se sostiene en la aditividad de la integral: los puntos de ruptura tienen **medida cero**, así que agregar o quitar un punto de la frontera no cambia el valor.
>
> **Ejemplo:** en $\int_{-2}^{3}|x|\,dx$ el punto $x = 0$ parte la suma en $\int_{-2}^{0}(-x)\,dx + \int_{0}^{3}x\,dx$.

> [!info] 🔍 Condiciones de aplicabilidad
>
> 1. **Cada tramo** debe ser integrable (en la práctica, continuo en su intervalo).
> 2. Debe haber un **número finito** de puntos de ruptura en el intervalo cerrado.
> 3. Las **discontinuidades** en los puntos de ruptura no afectan el valor de la integral.
> 4. Los **valores** de $f$ exactamente en los puntos de ruptura pueden definirse arbitrariamente.
>
> **Por qué importa:** la 3 y la 4 explican por qué no importa si el tramo cierra por la izquierda o por la derecha: cambiar $f$ en un solo punto no mueve el área. Por eso un paso que parecía ambiguo no lo es.

---

## 🛠️ Proceso paso a paso

> [!tip] 📋 El método sistemático
>
> 1. **Identificar** los puntos de ruptura dentro de $[a,b]$.
> 2. **Dividir** el intervalo de integración en esos puntos.
> 3. **Escribir** la integral como suma de integrales en cada subintervalo.
> 4. **Integrar** cada tramo con la expresión que le corresponde.
> 5. **Sumar** todos los resultados parciales.
> 6. **Verificar** el resultado contra el comportamiento esperado (signos, continuidad, geometría).
>
> **Por qué importa:** el paso 2 es donde se cometen los errores: si un subintervalo queda sin cubrir o se solapa con otro, la suma final está mal aunque cada integral individual esté bien.
>
> **Ejemplo:** con tres tramos, la verificación del paso 6 puede ser comparar el resultado contra la suma de áreas de la gráfica.

---

## 💡 Ejemplos desarrollados

> [!tip] 📈 Ejemplo 1 · Función valor absoluto
>
> **Evalúa** $\int_{-2}^{3} |x|\,dx$.
>
> **Paso 1:** escribir la definición por tramos: $|x| = -x$ si $x < 0$ y $|x| = x$ si $x \geq 0$.
>
> **Paso 2:** punto de ruptura en $x = 0$; partir el intervalo:
>
> $$\int_{-2}^{3} |x|\,dx = \int_{-2}^{0} |x|\,dx + \int_{0}^{3} |x|\,dx$$
>
> **Paso 3:** aplicar la expresión de cada tramo: $\int_{-2}^{0} (-x)\,dx + \int_{0}^{3} x\,dx$.
>
> **Paso 4:** integrar: $\left[-\frac{x^2}{2}\right]_{-2}^{0} + \left[\frac{x^2}{2}\right]_{0}^{3}$.
>
> **Paso 5:** evaluar: $\left(0 - \left(-\frac{4}{2}\right)\right) + \left(\frac{9}{2} - 0\right) = 2 + \frac{9}{2} = \frac{13}{2}$.
>
> **Respuesta:** $\dfrac{13}{2}$.
>
> **Verificación geométrica:** es un triángulo de base 2 y altura 2 (área 2) más otro de base 3 y altura 3 (área $\frac{9}{2}$): $2 + \frac{9}{2} = \frac{13}{2}$ ✓

> [!tip] 📈 Ejemplo 2 · Función escalón modificada
>
> **Evalúa** $\int_{0}^{4} f(x)\,dx$ donde
>
> $$f(x) = \begin{cases} x^2 & \text{si } 0 \leq x < 1 \\ 2 & \text{si } 1 \leq x < 3 \\ 5 - x & \text{si } 3 \leq x \leq 4 \end{cases}$$
>
> **Paso 1:** puntos de ruptura en $x = 1$ y $x = 3$.
>
> **Paso 2:** partir la integral: $\int_{0}^{1} f + \int_{1}^{3} f + \int_{3}^{4} f$.
>
> **Paso 3:** aplicar cada definición: $\int_{0}^{1} x^2\,dx + \int_{1}^{3} 2\,dx + \int_{3}^{4} (5-x)\,dx$.
>
> **Paso 4:** integrar: $\left[\frac{x^3}{3}\right]_{0}^{1} + [2x]_{1}^{3} + \left[5x - \frac{x^2}{2}\right]_{3}^{4}$.
>
> **Paso 5:** evaluar: $\frac{1}{3} + (6 - 2) + \left((20 - 8) - \left(15 - \frac{9}{2}\right)\right) = \frac{1}{3} + 4 + \frac{3}{2} = \frac{35}{6}$.
>
> **Respuesta:** $\dfrac{35}{6}$.
>
> **Por qué importa:** el tramo del medio es constante, así que su integral es un rectángulo de altura 2 y ancho 2: $4$. Reconocer eso ahorra escribir la antiderivada.

> [!tip] 📈 Ejemplo 3 · Función trigonométrica por tramos
>
> **Evalúa** $\int_{0}^{2\pi} g(x)\,dx$ donde
>
> $$g(x) = \begin{cases} \operatorname{sen} x & \text{si } 0 \leq x \leq \pi \\ 0 & \text{si } \pi < x \leq 2\pi \end{cases}$$
>
> **Paso 1:** punto de ruptura en $x = \pi$.
>
> **Paso 2:** partir: $\int_{0}^{\pi} g(x)\,dx + \int_{\pi}^{2\pi} g(x)\,dx$.
>
> **Paso 3:** aplicar las definiciones: $\int_{0}^{\pi} \operatorname{sen} x\,dx + \int_{\pi}^{2\pi} 0\,dx$.
>
> **Paso 4:** evaluar: $\left[-\cos x\right]_{0}^{\pi} + 0 = (-\cos \pi) - (-\cos 0) = 1 + 1 = 2$.
>
> **Respuesta:** $2$.
>
> **Por qué importa:** el segundo tramo es cero, así que **no aporta nada**; la mitad de la nota de este ejercicio es reconocer cuándo un tramo se puede descartar de un vistazo.

> [!tip] 📈 Ejemplo 4 · Función cuadrática por tramos
>
> **Evalúa** $\int_{-1}^{2} h(x)\,dx$ donde
>
> $$h(x) = \begin{cases} x^2 + 1 & \text{si } -1 \leq x < 0 \\ 2x & \text{si } 0 \leq x < 1 \\ x^3 & \text{si } 1 \leq x \leq 2 \end{cases}$$
>
> **Paso 1:** puntos de ruptura en $x = 0$ y $x = 1$.
>
> **Paso 2:** partir: $\int_{-1}^{0} (x^2 + 1)\,dx + \int_{0}^{1} 2x\,dx + \int_{1}^{2} x^3\,dx$.
>
> **Paso 3:** integrar: $\left[\frac{x^3}{3} + x\right]_{-1}^{0} + [x^2]_{0}^{1} + \left[\frac{x^4}{4}\right]_{1}^{2}$.
>
> **Paso 4:** evaluar: $\left(0 - \left(-\frac{1}{3} - 1\right)\right) + (1 - 0) + \left(\frac{16}{4} - \frac{1}{4}\right) = \frac{4}{3} + 1 + \frac{15}{4} = \frac{73}{12}$.
>
> **Respuesta:** $\dfrac{73}{12}$.
>
> **Por qué importa:** aquí cada tramo tiene una expresión distinta y ninguna se simplifica con la anterior; es el caso típico de "tres integrales y una suma", donde el error suele estar en la suma final.

---

## 🎯 Casos especiales

> [!tip] 📊 Función signo
>
> $$\operatorname{sgn}(x) = \begin{cases} -1 & \text{si } x < 0 \\ 0 & \text{si } x = 0 \\ 1 & \text{si } x > 0 \end{cases}$$
>
> **Integral:** $\int_{-a}^{a} \operatorname{sgn}(x)\,dx = 0$ para cualquier $a > 0$.
>
> **Por qué importa:** es **impar** sobre un intervalo simétrico, así que la integral se anula sin calcular nada: la regla de simetría se aplica antes que la de tramos.

> [!tip] 📊 Función escalón unitario (Heaviside)
>
> $$H(x) = \begin{cases} 0 & \text{si } x < 0 \\ 1 & \text{si } x \geq 0 \end{cases}$$
>
> **Integral:** $\int_{-a}^{b} H(x)\,dx = b$ para $a > 0$ y $b > 0$.
>
> **Por qué importa:** el único tramo que aporta es el de la derecha, y es constante; el resultado depende solo de $b$. Es la forma en que las señales "encendidas" acumulan energía.

> [!tip] 📊 Función parte entera (piso)
>
> $$\lfloor x \rfloor = \max\{n \in \mathbb{Z} : n \leq x\}$$
>
> **En $[0,3]$:**
>
> $$\lfloor x \rfloor = \begin{cases} 0 & \text{si } 0 \leq x < 1 \\ 1 & \text{si } 1 \leq x < 2 \\ 2 & \text{si } 2 \leq x < 3 \\ 3 & \text{si } x = 3 \end{cases}$$
>
> **Por qué importa:** es la función por tramos por excelencia: **infinitos** tramos en cualquier intervalo largo, pero sobre $[0,3]$ basta con tres. El valor en $x = 3$ no cambia la integral, aunque la definición sí lo declare.

> [!tip] 📊 Función diente de sierra
>
> $$\operatorname{saw}(x) = x - \lfloor x \rfloor$$
>
> **Periódica** con período 1 y valores en $[0,1)$.
>
> **Por qué importa:** combina parte entera y línea recta, así que en cada período repite el mismo tramo. Su integral en $n$ periodos es $n$ veces la de uno solo.

---

## 🧠 Estrategias de resolución

> [!success] 🎯 Las cuatro estrategias generales
>
> **1. Análisis previo**
> - Identifica **todos** los puntos de ruptura en el intervalo.
> - Verifica la **continuidad** en cada punto.
> - Determina si hay **discontinuidades removibles**.
>
> **2. División sistemática**
> - Ordena los puntos de ruptura de menor a mayor.
> - Divide el intervalo en subintervalos apropiados.
> - Asegúrate de que **no se omita ni se solape** ningún subintervalo.
>
> **3. Integración cuidadosa**
> - Usa la expresión correcta en cada subintervalo.
> - Verifica los límites de integración de cada tramo.
> - Mantén el registro de los signos.
>
> **4. Verificación**
> - Comprueba que la unión de los subintervalos cubra todo $[a,b]$.
> - Verifica el comportamiento esperado (monotonía, signos).
> - Usa métodos alternativos cuando sea posible.
>
> **Por qué importa:** el punto 1 y el 2 son previos al cálculo y son donde se decide el éxito del ejercicio; el 3 y el 4 solo lo ejecutan.

> [!tip] 💡 Trucos para acortar el trabajo
>
> **Para funciones simétricas:** usa la paridad antes que la división: $\int_{-a}^{a} f(x)\,dx = 2\int_{0}^{a} f(x)\,dx$ si $f$ es par, y $0$ si es impar.
>
> **Para funciones periódicas:** calcula la integral en un período y multiplica: $\int_{0}^{nT} f(x)\,dx = n\int_{0}^{T} f(x)\,dx$.
>
> **Para optimizar cálculos:** busca patrones entre los resultados parciales y usa la linealidad para factorizar términos comunes antes de sumar.
>
> **Por qué importa:** estos tres atajos son los que separan un ejercicio de 10 minutos de uno de 3: aplican **antes** de partir el intervalo.

---

## 📊 Interpretación geométrica

> [!info] 📈 La integral como suma algebraica de áreas
>
> La integral de una función por tramos es la **suma algebraica de áreas** bajo cada tramo:
>
> - **Áreas positivas:** donde $f(x) > 0$.
> - **Áreas negativas:** donde $f(x) < 0$ se restan.
> - **Puntos de ruptura:** no afectan el valor de la integral.
> - **Discontinuidades de salto:** se manejan solas al partir el intervalo.
>
> **Por qué importa:** "suma algebraica" es la clave: no se suman valores absolutos. Si un tramo cae bajo el eje, su aporte es negativo y restar es correcto.

> [!info] 🖼️ De la función a la suma de áreas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Integral_de_Funciones_por_Tramos_02.svg]]
>
> **Se lee así:** un recorrido de cuatro cajas en cadena: función por tramos → división en intervalos → cálculo del área en cada tramo → suma algebraica de áreas. Por debajo, cinco cajas de datos (tramo 1 con área $A_1$, tramo 2 con $A_2$, tramo 3 con $A_3$, una elipsis y el tramo $n$ con $A_n$) alimentan una caja central de suma total, y esa suma desemboca en la igualdad final $\int f(x)\,dx = A_1 + A_2 + A_3 + \cdots + A_n$.
>
> **Por qué importa:** el diagrama separa el **camino conceptual** (dividir, calcular, sumar) del **camino de los datos** (cada tramo con su área). Así no se pierde ningún subintervalo y se mantienen los signos, porque las áreas negativas se restan.
>
> **Ejemplo:** con $\int_{-2}^{3} |x|\,dx$ de la nota, el punto de ruptura en $x = 0$ parte el intervalo en dos y las áreas $2$ y $\frac{9}{2}$ se suman para dar $\frac{13}{2}$.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco fallos típicos
>
> 1. **Omitir puntos de ruptura.** *Mal:* no identificar todos los cambios de definición. *Bien:* graficar la función o analizarla punto por punto.
> 2. **Límites de integración incorrectos.** *Mal:* usar intervalos que se solapan o dejan huecos. *Bien:* verificar que $\bigcup_{i=1}^{n} [x_{i-1}, x_i] = [a,b]$.
> 3. **Expresión equivocada en un intervalo.** *Mal:* aplicar el tramo de al lado. *Bien:* probar la expresión con un valor interior del subintervalo.
> 4. **Manejo incorrecto de extremos.** *Mal:* angustiarse con el abierto o cerrado del intervalo. *Bien:* recordar que el valor en el punto de ruptura no afecta la integral.
> 5. **Error aritmético en la suma final.** *Mal:* sumar mal los resultados parciales. *Bien:* comprobar cada parcial por separado antes de sumar.
>
> **Por qué importa:** los tres primeros son de **planteamiento** y arruinan el ejercicio entero; el cuarto no es un error real (solo ansiedad) y el quinto es el que más se comete en examen por prisa.

> [!tip] 💡 Mejores prácticas
>
> **Organización:** haz una tabla con el intervalo y su expresión correspondiente, calcula cada integral parcial por separado y suma al final.
>
> **Verificación:** grafica la función para ver los tramos y comprueba que el resultado tenga sentido geométricamente (signo y orden de magnitud).
>
> **Documentación:** escribe cada paso de la división e identifica explícitamente qué expresión usaste en cada tramo, para poder revisarlo después.
>
> **Por qué importa:** un ejercicio de tres tramos mal documentado no se puede revisar; el que está ordenado se corrige en una línea.

---

## 🌐 Aplicaciones

> [!note] 📡 En ingeniería
>
> **Procesamiento de señales:** señales digitales (escalón y pulsos rectangulares), filtros con respuesta en frecuencia por tramos y modulación, donde la señal cambia de comportamiento según el intervalo.
>
> **Control de sistemas:** controladores con estrategias distintas según el error, saturación de actuadores con límites operativos e histéresis, cuyo comportamiento depende de la historia del sistema.
>
> **Por qué importa:** en estas tres áreas la ley que rige el sistema **cambia de forma** al cruzar un umbral; integrar sin partir el intervalo significa aplicar la ley equivocada a media señal.

> [!note] 💰 En economía
>
> **Funciones de costo:** estructuras mixtas de costos fijos y variables, economías de escala con costos unitarios decrecientes por tramos e impuestos progresivos con tasas por tramo de ingreso.
>
> **Demanda y oferta:** precios con descuentos por cantidad y mercados segmentados con comportamiento distinto por segmento.
>
> **Por qué importa:** el impuesto progresivo es el ejemplo cotidiano de función por tramos: la tasa cambia al cruzar cada tramo y la carga total es la suma de lo pagado en cada uno.

> [!note] 🔬 En física
>
> **Mecánica:** fuerzas variables con leyes distintas según la posición, fricción con valores distintos para el reposo y el deslizamiento, y colisiones con fases antes, durante y después del impacto.
>
> **Termodinámica:** transiciones de fase con propiedades que cambian de forma abrupta y calor específico con valores distintos según la temperatura.
>
> **Por qué importa:** la física pone los puntos de ruptura: el instante en que un objeto empieza a deslizar o el calor en que el agua hierve. Saber leer esos puntos es la mitad del problema.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{-1}^{2} |2x - 1|\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Punto de ruptura:** $2x - 1 = 0 \Rightarrow x = \frac{1}{2}$, que cae dentro de $[-1,2]$.
> >
> > **División:** $\int_{-1}^{1/2} (1 - 2x)\,dx + \int_{1/2}^{2} (2x - 1)\,dx$.
> >
> > **Integración:** $\left[x - x^2\right]_{-1}^{1/2} + \left[x^2 - x\right]_{1/2}^{2}$.
> >
> > **Evaluación:** $\left(\frac{1}{2} - \frac{1}{4}\right) - (-1 - 1) = \frac{1}{4} + 2 = \frac{9}{4}$, y $(4 - 2) - \left(\frac{1}{4} - \frac{1}{2}\right) = 2 + \frac{1}{4} = \frac{9}{4}$.
> >
> > **Respuesta:** $\dfrac{9}{4} + \dfrac{9}{4} = \dfrac{9}{2}$.
> >
> > **Control:** $|2x-1| = 2\left|x - \frac{1}{2}\right|$ es simétrico respecto de $x = \frac{1}{2}$ y $[-1,2]$ tiene centro exactamente en $\frac{1}{2}$, así que las dos mitades deben dar lo mismo ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{0}^{3} f(x)\,dx$ donde $f(x) = \begin{cases} x + 1 & \text{si } 0 \leq x < 1 \\ 3 - x & \text{si } 1 \leq x \leq 3 \end{cases}$.
>
> > [!success]- ✅ Solución
> >
> > **Punto de ruptura:** $x = 1$.
> >
> > **División:** $\int_{0}^{1} (x + 1)\,dx + \int_{1}^{3} (3 - x)\,dx$.
> >
> > **Integración:** $\left[\frac{x^2}{2} + x\right]_{0}^{1} + \left[3x - \frac{x^2}{2}\right]_{1}^{3}$.
> >
> > **Evaluación:** $\left(\frac{1}{2} + 1\right) - 0 = \frac{3}{2}$, y $(9 - \frac{9}{2}) - (3 - \frac{1}{2}) = \frac{9}{2} - \frac{5}{2} = 2$.
> >
> > **Respuesta:** $\dfrac{3}{2} + 2 = \dfrac{7}{2}$.
> >
> > **Control geométrico:** el primer tramo es un trapecio de alturas 1 y 2 y ancho 1 (área $\frac{3}{2}$); el segundo es un triángulo de base 2 y altura 2 (área 2) ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{0}^{4} \left\lfloor \dfrac{x}{2} \right\rfloor dx$.
>
> > [!success]- ✅ Solución
> >
> > **Puntos de ruptura:** $\frac{x}{2}$ cruza enteros en $x = 2$ y $x = 4$.
> >
> > **Tramos:** $\left\lfloor \frac{x}{2} \right\rfloor = 0$ en $[0,2)$, $= 1$ en $[2,4)$ y $= 2$ solo en el punto $x = 4$.
> >
> > **División:** $\int_{0}^{2} 0\,dx + \int_{2}^{4} 1\,dx = 0 + [x]_{2}^{4} = 2$.
> >
> > **Respuesta:** $2$.
> >
> > **Por qué el punto final no cuenta:** el valor en un solo punto no cambia una integral, así que el tramo $\{4\}$ aporta $0$ ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{-3}^{3} \left(1 + \operatorname{sgn}(x)\right)dx$.
>
> > [!success]- ✅ Solución
> >
> > **Linealidad:** $\int_{-3}^{3} 1\,dx + \int_{-3}^{3} \operatorname{sgn}(x)\,dx$.
> >
> > **Primer término:** $\int_{-3}^{3} 1\,dx = 6$ (rectángulo de altura 1 y base 6).
> >
> > **Segundo término:** $\operatorname{sgn}$ es **impar** sobre el intervalo simétrico $[-3,3]$, así que vale $0$.
> >
> > **Respuesta:** $6 + 0 = 6$.
> >
> > **También por tramos:** $\int_{-3}^{0} 0\,dx$ (ya que $1 + (-1) = 0$) $+ \int_{0}^{3} 2\,dx = 0 + 6 = 6$ ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_{0}^{3} \left(x - \lfloor x \rfloor\right)dx$, la función diente de sierra.
>
> > [!success]- ✅ Solución
> >
> > **Tramos:** en $[0,1)$ vale $x - 0 = x$; en $[1,2)$ vale $x - 1$; en $[2,3)$ vale $x - 2$; en $x = 3$ vale $0$.
> >
> > **División:** $\int_{0}^{1} x\,dx + \int_{1}^{2} (x - 1)\,dx + \int_{2}^{3} (x - 2)\,dx$.
> >
> > **Integración:** $\left[\frac{x^2}{2}\right]_0^1 + \left[\frac{x^2}{2} - x\right]_1^2 + \left[\frac{x^2}{2} - 2x\right]_2^3$.
> >
> > **Evaluación:** $\frac{1}{2} + \left(2 - 2\right) - \left(\frac{1}{2} - 1\right) + \left(\frac{9}{2} - 6\right) - \left(2 - 4\right) = \frac{1}{2} + \frac{1}{2} + \frac{1}{2} = \frac{3}{2}$.
> >
> > **Respuesta:** $\dfrac{3}{2}$.
> >
> > **Atajo periódico:** la función tiene período 1 y su media en un período es $\int_0^1 x\,dx = \frac{1}{2}$, así que en 3 periodos da $3 \cdot \frac{1}{2} = \frac{3}{2}$ ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino una función por tramos y señalo sus puntos de ruptura en un intervalo dado.
> - [ ] Escribo la integral de una función por tramos como suma de integrales en cada subintervalo.
> - [ ] Aplico la regla de aditividad $\int_a^b = \int_a^c + \int_c^b$ sin solapar ni dejar huecos entre tramos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo integrales con valor absoluto, función signo y escalón de Heaviside identificando el punto de ruptura.
> - [ ] Integro funciones con tres o más tramos y verifico la suma parcial contra la geometría de la gráfica.
> - [ ] Explico por qué el valor de la función en un punto de ruptura no cambia el resultado de la integral.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Combino la división por tramos con la paridad y la periodicidad para acortar el cálculo.
> - [ ] Reconozco cuándo un tramo aporta cero y lo descarto sin integrar.
> - [ ] Modele una situación de la carrera (impuestos, saturación, fricción) como función por tramos y calculo su integral.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 5.1–5.2: propiedades de la integral y aditividad.
> - R. Larson, *Cálculo* (Cengage), cap. 5.1: funciones definidas a trozos.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 5: piecewise functions.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — la aditividad respecto al intervalo que sostiene todo el método.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — cómo se evalúa cada tramo.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — qué es un punto de ruptura y qué tipo de discontinuidad puede haber.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — el comportamiento de $f$ por izquierda y por derecha en cada ruptura.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es una función definida por tramos?::Una que tiene expresiones distintas en intervalos distintos de su dominio, separadas por puntos de ruptura $x_1 < x_2 < \cdots < x_{n-1}$.
> - ¿Cómo se integra una función por tramos?::Partiendo el intervalo en los puntos de ruptura: $\int_a^b f = \sum_{i=1}^n \int_{x_{i-1}}^{x_i} f_i(x)\,dx$, integrando cada tramo con su expresión.
> - ¿Por qué el valor de $f$ en un punto de ruptura no cambia la integral?::Porque un punto tiene medida cero: agregar o quitar un valor en un solo punto no altera el área acumulada.
> - ¿Qué integral da la función de Heaviside?::$\int_{-a}^{b} H(x)\,dx = b$ con $a>0$ y $b>0$: solo aporta el tramo donde $H = 1$.
> - ¿Cuándo vale cero la integral de la función signo?::En cualquier intervalo simétrico $[-a,a]$, porque $\operatorname{sgn}$ es impar; fuera de la simetría hay que partir el intervalo.
> - ¿Cuál es el error más caro al integrar por tramos?::Usar la expresión equivocada en un subintervalo o saltarse un tramo; se previene probando la expresión con un valor interior.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — las técnicas que cada tramo puede necesitar.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/03 - Teoremas Especiales para Integrales Definidas|03 - Teoremas Especiales para Integrales Definidas]] — simetría y periodicidad, los dos atajos que más ahorran aquí.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — qué hacer cuando la discontinuidad lleva el infinito dentro del intervalo.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la interpretación geométrica de estas sumas de áreas.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — donde las funciones por tramos aparecen primero, como leyes por tramos.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — la antiderivada que se aplica en cada tramo.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero el ejercicio 2: es el caso canónico, tres tramos con expresiones distintas.
> - Después pasa al 1 y al 4, donde entra el valor absoluto y el signo, que se resuelven con simetría antes que con división.
> - Cierra con el 3 y el 5, que combinan parte entera y periodicidad, los dos atajos más rápidos de la nota.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/III - Integrales Definidas/03 - Teoremas Especiales para Integrales Definidas|Teoremas Especiales para Integrales Definidas]] para aplicar paridad y periodicidad de forma sistemática.

---

**Tags:** #MATG1045 #unidad6 #integral-de-funciones-por-tramos #funciones-a-trozos #puntos-de-ruptura #aditividad-intervalo #funcion-escalón #funcion-signo #discontinuidades

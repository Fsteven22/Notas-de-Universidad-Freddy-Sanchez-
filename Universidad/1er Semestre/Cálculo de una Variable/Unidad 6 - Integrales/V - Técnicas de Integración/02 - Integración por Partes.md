---
dg-publish: true
tags: [MATG1045, unidad6, integracion-por-partes, integrales, por-partes, liate, tecnicas-integracion, udvivu, tabla, metodo-visual]
---

# 🔧 Integración por Partes

## 🎯 Introducción

> [!info] 💡 Qué es y cuándo se usa
>
> La **integración por partes** es la técnica que se apoya en la regla del producto para derivadas ($ (uv)' = u'v + uv' $) y sirve cuando la integral es un **producto de dos funciones** que no se resuelven bien por sustitución: se deriva una, se integra la otra y queda una integral más simple. Es la segunda técnica fundamental del cálculo integral, junto con el cambio de variable.
>
> **Por qué importa:** resuelve los casos clásicos $\int x e^x\,dx$, $\int x \ln x\,dx$ e $\int e^x \sin x\,dx$, y es puente hacia las integrales de funciones inversas y hacia la fórmula de Wallis. Además, cuando el polinomio es largo, existe un atajo visual —el **método de tabla— que esta nota cubre por completo.
>
> **Ejemplo:** $\int x e^x\,dx$ no admite sustitución limpia, pero tomando $u = x$ y $dv = e^x\,dx$ se convierte en $xe^x - \int e^x\,dx = e^x(x-1) + C$.

> [!tip] 🎯 Las dos caras de la técnica
>
> - **Método tradicional:** elegir $u$ y $dv$ (con LIATE), aplicar la fórmula una vez o varias.
> - **Método de tabla:** derivar a la izquierda hasta llegar a 0, integrar a la derecha y cruzar las diagonales con signos alternados; ideal para polinomios × (exponencial o trigonométrica).
>
> **Por qué importa:** los dos hacen lo mismo; la tabla es solo el atajo organizado del método tradicional repetido.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Fórmula de integración por partes y elección de $u$
>
> La fórmula es:
>
> $$\int u \, dv = uv - \int v \, du$$
>
> donde:
>
> - $u$ = función que se **deriva** fácilmente,
> - $dv$ = función que se **integra** fácilmente,
> - $du$ = derivada de $u$,
> - $v$ = antiderivada de $dv$.
>
> **Orden de prioridad para elegir $u$ (LIATE):**
>
> 1. **L** — Logarítmicas: $\ln(x)$, $\log(x)$
> 2. **I** — Inversas trigonométricas: $\arcsin(x)$, $\arctan(x)$, $\arccos(x)$
> 3. **A** — Algebraicas: $x^n$, polinomios
> 4. **T** — Trigonométricas: $\sin(x)$, $\cos(x)$, $\tan(x)$
> 5. **E** — Exponenciales: $e^x$, $a^x$
>
> La familia **más alta** de la lista se toma como $u$; el resto va en $dv$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integración_por_Partes_01.svg]]
>
> **Se lee así:** la caja de la fórmula abre el diagrama y da paso a una segunda caja con la estrategia de prioridad. De ella salen cinco ramas paralelas, una por cada familia de funciones, y además una sexta flecha directa hacia un recuadro final que fija la regla de qué tomar como $u$ y qué como $dv$. Las cinco familias quedan ordenadas de la prioridad más alta a la más baja.
>
> **Por qué importa:** LIATE te da un **criterio objetivo** para elegir $u$ en lugar de adivinar, y con eso se resuelve el error más común de la técnica. La fórmula y la estrategia quedan conectadas: no es un truco suelto, es el punto de partida del método.
>
> **Ejemplo:** en $\int x \ln(x)\,dx$ el logaritmo tiene la prioridad más alta, así que $u = \ln(x)$ y $dv = x\,dx$, y se llega a $\frac{x^2}{2}\ln(x) - \frac{x^2}{4} + C$.

> [!tip] 🐄 Mnemotecnia UDVIVU
>
> **U**n **D**ía **V**i **U**na **V**aca **V**estida de **U**niforme:
>
> $$\int \mathbf{U} \, d\mathbf{V} = \mathbf{U}\mathbf{V} - \int \mathbf{V} \, d\mathbf{U}$$
>
> - **U** = primera función ($u$)
> - **D** = derivada ($du$)
> - **V** = antiderivada ($v$)
> - **I** = igual
> - **V** = primera función por antiderivada ($uv$)
> - **V** = menos
> - **U** = integral de antiderivada por derivada ($\int v\,du$)
>
> **Por qué importa:** la frase recuerda tanto la fórmula como el orden de los factores; el riesgo de esta técnica no es recordar la fórmula, sino invertir un factor.

---

## 🔄 Método tradicional en acción

> [!success] 💡 Consejos de elección y comprobación
>
> - Si **LIATE no funciona** (la integral empeora), **intercambia** $u$ y $dv$ y vuelve a intentarlo.
> - **Verifica tu respuesta derivando:** la derivada del resultado debe devolver el integrando.
> - Algunos casos piden **combinación** con otras técnicas (sustitución antes, fracciones parciales después).
> - En **integrales cíclicas**, mantén la integral original como incógnita $I$ y despeja.
> - Practica el reconocimiento de patrones: polinomio × exponencial o polinomio × trigonométrica casi siempre van por partes (o por tabla).
>
> **Por qué importa:** intercambiar $u$ y $dv$ es la válvula de escape del método; saber cuándo hacerlo convierte un callejón sin salida en un ejercicio de tres líneas.

> [!note] 🚀 Integrales comunes por partes (tabla de referencia)
>
> | Integral | $u$ | $dv$ | Resultado |
> |---|---|---|---|
> | $\int x e^x\,dx$ | $x$ | $e^x\,dx$ | $e^x(x-1) + C$ |
> | $\int x \sin(x)\,dx$ | $x$ | $\sin(x)\,dx$ | $-x\cos(x) + \sin(x) + C$ |
> | $\int x \cos(x)\,dx$ | $x$ | $\cos(x)\,dx$ | $x\sin(x) + \cos(x) + C$ |
> | $\int \ln(x)\,dx$ | $\ln(x)$ | $dx$ | $x\ln(x) - x + C$ |
> | $\int x^n \ln(x)\,dx$ | $\ln(x)$ | $x^n\,dx$ | $\frac{x^{n+1}}{n+1}\ln(x) - \frac{x^{n+1}}{(n+1)^2} + C$ |
>
> **Por qué importa:** estas cinco cubren la mayoría de los ejercicios tipo; reconocer la estructura te ahorra montar la fórmula desde cero.

---

## 🔄 Integrales cíclicas

> [!warning] 🚨 El caso que vuelve al punto de partida
>
> Algunas integrales requieren aplicar la técnica **dos veces** y resolver un sistema. Ejemplo: $\int e^x \sin(x)\,dx$.
>
> **Primera aplicación** ($u = \sin x$, $dv = e^x dx$):
> $$\int e^x \sin x\,dx = e^x \sin x - \int e^x \cos x\,dx$$
>
> **Segunda aplicación** en $\int e^x \cos x\,dx$ ($u = \cos x$, $dv = e^x dx$):
> $$\int e^x \cos x\,dx = e^x \cos x + \int e^x \sin x\,dx$$
>
> **Sustituyendo** con $I = \int e^x \sin x\,dx$:
>
> $$I = e^x \sin x - \big[e^x \cos x + I\big] \;\Rightarrow\; 2I = e^x(\sin x - \cos x) \;\Rightarrow\; I = \frac{e^x(\sin x - \cos x)}{2} + C$$
>
> **Por qué importa:** la integral original reaparece con el mismo signo; en lugar de girar en círculo, la tratas como incógnita y despejas. Ese "dos pasadas + sistema" es el patrón completo del caso cíclico.

> [!info] 🖼️ El ciclo dibujado
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integración_por_Partes_02.svg]]
>
> **Se lee así:** una cadena de rectángulos que baja por el caso cíclico y se abre en dos pasadas sucesivas. La primera pasada registra la elección de $u$ y $dv$ y produce una integral nueva; esa integral entra como nueva partida en la segunda pasada, y al sustituirla aparece la integral original otra vez, lo que cierra el ciclo. El bloque final despeja la incógnita y la última caja advierte sobre la elección de $dv$.
>
> **Por qué importa:** el esquema muestra **por qué** esta integral no se resuelve a la primera y cómo se rompe el círculo al reunir las dos ecuaciones.
>
> **Ejemplo:** con $\int e^x \sin(x)\,dx$ el ciclo da $2I = e^x(\sin x - \cos x)$ y de ahí $I = \frac{e^x(\sin x - \cos x)}{2} + C$.

---

## 📐 Integrales definidas

> [!info] 📋 Fórmula con límites
>
> $$\int_a^b u \, dv = \Big[uv\Big]_a^b - \int_a^b v \, du$$
>
> **Por qué importa:** el término $[uv]_a^b$ se evalúa en los extremos **antes** de restar la integral; olvidarlo es el error típico de esta variante.

> [!example] 📈 Ejemplo resuelto — $\int_1^e x \ln(x)\,dx$
>
> **Elección:** $u = \ln(x)$, $dv = x\,dx$ (entonces $du = \frac{1}{x}\,dx$, $v = \frac{x^2}{2}$).
>
> $$\int_1^e x \ln x\,dx = \Big[\frac{x^2}{2}\ln x\Big]_1^e - \int_1^e \frac{x}{2}\,dx = \Big[\frac{x^2}{2}\ln x\Big]_1^e - \Big[\frac{x^2}{4}\Big]_1^e$$
>
> **Evaluación:** $\frac{e^2}{2}\ln e - \frac{1}{2}\ln 1 - \frac{e^2}{4} + \frac{1}{4} = \frac{e^2}{2} - 0 - \frac{e^2}{4} + \frac{1}{4}$.
>
> **Respuesta:** $\dfrac{e^2 + 1}{4}$.
>
> **Control:** $\ln 1 = 0$ anula el primer término del primer corchete y el segundo del segundo; el resto es aritmética limpia ✓

---

## 📊 El método de tabla

> [!info] 💡 Qué es y cuándo conviene
>
> El **método de tabla** organiza las derivadas e integrales en columnas conectadas por líneas diagonales: es la integración por partes repetida, resumida en una sola vista. Es especialmente útil cuando:
>
> - una función se puede **derivar hasta llegar a cero** (polinomios),
> - la otra se puede **integrar fácilmente varias veces**,
> - necesitarías aplicar por partes **múltiples veces**,
> - quieres **visualizar** el proceso completo.
>
> **Por qué importa:** en polinomios de grado alto la tabla ahorra tiempo y hace visible el error cuando los signos alternados no encajan.

> [!example] 📊 Estructura de la tabla
>
> | Signo | Derivadas ($u$) | Integrales ($v$) |
> |---|---|---|
> | $+$ | $f(x)$ | $\int g(x)\,dx$ |
> | $-$ | $f'(x)$ | $\iint g(x)\,dx\,dx$ |
> | $+$ | $f''(x)$ | $\iiint g(x)\,dx\,dx\,dx$ |
> | $-$ | $f'''(x)$ | $\dots$ |
> | $\dots$ | $\dots$ | $\dots$ |
> | $\pm$ | $0$ | $\dots$ |
>
> **Resultado:** $\sum (\text{signo} \times \text{derivada} \times \text{integral de la fila siguiente})$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integración_por_Partes_03.svg]]
>
> **Se lee así:** el diagrama arranca con una caja que presenta el método y otra que dice cuándo conviene, y de ahí pasa a una caja central que representa la tabla. De esa tabla cuelgan en vertical varias filas, cada una con su signo alternado, su derivada a la izquierda y su integral repetida a la derecha, hasta llegar a la fila donde la derivada se anula. Solo esa última fila enlaza con la caja del resultado, que se lee como una suma de productos con signo.
>
> **Por qué importa:** la tabla resume en una sola vista todas las aplicaciones de partes que harías una por una.
>
> **Ejemplo:** para $\int x^2 e^x\,dx$ la tabla da $x^2 e^x - 2x e^x + 2e^x + C$, que se factoriza como $e^x(x^2 - 2x + 2) + C$.

> [!info] 🖼️ Las diagonales, la clave visual
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integración_por_Partes_04.svg]]
>
> **Se lee así:** la misma idea de la tabla dibujada como una cadena: una caja describe el método, otra explica que cada nodo toca al vecino de la fila siguiente en la otra columna, y de ahí bajan una tras otra las filas con el signo alternado y la marca de la diagonal que une derivada e integral. La última fila, donde la derivada llega a cero, cierra el recorrido y dispara la caja del resultado.
>
> **Por qué importa:** la diagonal te dice **exactamente qué multiplicar con qué y con qué signo**; sin esa guía, las sumas largas se llenan de errores de emparejamiento entre columnas.
>
> **Ejemplo:** en $\int x^3 \sin(x)\,dx$ cada diagonal aporta un producto con signo y la suma es $-x^3\cos x + 3x^2\sin x + 6x\cos x - 6\sin x + C$.

> [!success] 🔧 Algoritmo de la tabla y sus límites
>
> **Pasos:**
>
> 1. **Identificar funciones:** una que se derive hasta 0, otra fácil de integrar.
> 2. **Crear columnas:** derivadas a la izquierda, integrales a la derecha.
> 3. **Llenar la tabla:** derivar hasta 0, integrar el mismo número de veces.
> 4. **Asignar signos:** alternar $+, -, +, -, \dots$
> 5. **Conectar diagonalmente:** cada derivada con la integral de la **fila siguiente**.
> 6. **Sumar productos:** multiplicar por el signo correspondiente.
>
> **Ventajas:** visualización clara, menos errores de organización, más rápido en polinomios de grado alto, verificación fácil por fila.
>
> **Cuándo NO usarla:**
>
> - funciones que **no se anulan** como $\ln(x)$ o $\arctan(x)$,
> - **integrales cíclicas** como $\int e^x \sin x\,dx$,
> - funciones difíciles de integrar repetidamente,
> - casos con **una sola aplicación**: el método tradicional es más directo.
>
> **Comparación ($\int x^2 e^x\,dx$):** el tradicional pide tres aplicaciones encadenadas ($u = x^2$, luego $2x$, luego $2$); la tabla las reúne en **un solo proceso** con conexiones diagonales.
>
> **Por qué importa:** la tabla es un atajo, no una técnica distinta; saber cuándo **no** usarla evita tablas interminables donde el método tradicional gana en dos pasos.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los seis fallos típicos
>
> 1. **Elegir mal $u$:** si la integral empeora, LIATE no se aplicó bien o toca intercambiar $u$ y $dv$.
> 2. **Derivar o integrar mal:** revisar $du$ y $v$ antes de sustituir.
> 3. **Olvidar la constante de integración** en el resultado indefinido.
> 4. **No reconocer el caso cíclico:** si la integral vuelve, plantear el sistema con $I$.
> 5. **En definidas, olvidar evaluar $[uv]_a^b$.**
> 6. **Emparejar mal las diagonales** de la tabla: cada derivada con la integral de la fila **siguiente**, no la misma.
>
> **Por qué importa:** los tres primeros son de ejecución y los tres últimos de método; la lista de comprobación antes de entregar cubre los dos frentes.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Resuelve $\int x e^x\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Elección (LIATE):** $u = x$ (algebraica), $dv = e^x\,dx$; $du = dx$, $v = e^x$.
> >
> > $$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C$$
> >
> > **Respuesta:** $e^x(x - 1) + C$.
> >
> > **Control:** $\frac{d}{dx}\big[e^x(x-1)\big] = e^x(x-1) + e^x = xe^x$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int x \ln(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Elección (LIATE):** $u = \ln x$ (logarítmica), $dv = x\,dx$; $du = \frac{1}{x}\,dx$, $v = \frac{x^2}{2}$.
> >
> > $$\int x \ln x\,dx = \frac{x^2}{2}\ln x - \int \frac{x^2}{2} \cdot \frac{1}{x}\,dx = \frac{x^2}{2}\ln x - \int \frac{x}{2}\,dx$$
> >
> > **Respuesta:** $\frac{x^2}{2}\ln x - \frac{x^2}{4} + C$.
> >
> > **Cuidado:** el logaritmo nunca se deriva antes que se integre: si lo pones en $dv$ no puedes integrarlo ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int x \arctan(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Elección (LIATE):** $u = \arctan x$ (inversa trigonométrica), $dv = x\,dx$; $du = \frac{1}{1+x^2}\,dx$, $v = \frac{x^2}{2}$.
> >
> > $$\int x \arctan x\,dx = \frac{x^2}{2}\arctan x - \frac{1}{2}\int \frac{x^2}{1+x^2}\,dx$$
> >
> > **Truco:** $\frac{x^2}{1+x^2} = 1 - \frac{1}{1+x^2}$, así que la integral es $x - \arctan x$.
> >
> > $$= \frac{x^2}{2}\arctan x - \frac{x}{2} + \frac{1}{2}\arctan x + C$$
> >
> > **Respuesta:** $\frac{x^2+1}{2}\arctan(x) - \frac{x}{2} + C$.
> >
> > **Lección:** a veces la segunda integral pide un reescrituramiento antes de integrar ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int e^x \sin(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Primera pasada** ($u = \sin x$, $dv = e^x dx$): $I = e^x \sin x - \int e^x \cos x\,dx$.
> >
> > **Segunda pasada** ($u = \cos x$, $dv = e^x dx$): $\int e^x \cos x\,dx = e^x \cos x + \int e^x \sin x\,dx = e^x \cos x + I$.
> >
> > **Sistema:** $I = e^x \sin x - e^x \cos x - I$, luego $2I = e^x(\sin x - \cos x)$.
> >
> > **Respuesta:** $I = \frac{e^x(\sin x - \cos x)}{2} + C$.
> >
> > **Control:** derivando, $\frac{d}{dx}\frac{e^x(\sin x - \cos x)}{2} = \frac{e^x(\sin x - \cos x) + e^x(\cos x + \sin x)}{2} = e^x \sin x$ ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_1^e x \ln(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > $u = \ln x$, $dv = x\,dx$ → $du = \frac{1}{x}dx$, $v = \frac{x^2}{2}$.
> >
> > $$\Big[\frac{x^2}{2}\ln x\Big]_1^e - \int_1^e \frac{x}{2}\,dx = \Big[\frac{x^2}{2}\ln x - \frac{x^2}{4}\Big]_1^e$$
> >
> > **Evaluación:** $\left(\frac{e^2}{2} - \frac{e^2}{4}\right) - \left(0 - \frac{1}{4}\right) = \frac{e^2}{4} + \frac{1}{4}$.
> >
> > **Respuesta:** $\frac{e^2 + 1}{4}$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int x^2 e^x\,dx$ con el método de tabla.
>
> > [!success]- ✅ Solución
> >
> > **Tabla:**
> >
> > | Signo | Derivadas de $x^2$ | Integrales de $e^x$ |
> > |---|---|---|
> > | $+$ | $x^2$ | $e^x$ |
> > | $-$ | $2x$ | $e^x$ |
> > | $+$ | $2$ | $e^x$ |
> > | $-$ | $0$ | $e^x$ |
> >
> > **Diagonales:** $+x^2 \cdot e^x$, $-(2x) \cdot e^x$, $+2 \cdot e^x$.
> >
> > **Respuesta:** $x^2 e^x - 2x e^x + 2e^x + C = e^x(x^2 - 2x + 2) + C$.
> >
> > **Atajo:** tres aplicaciones de partes en una sola vista ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int x^3 \sin(x)\,dx$ con el método de tabla.
>
> > [!success]- ✅ Solución
> >
> > **Tabla:** derivadas de $x^3$: $x^3 \to 3x^2 \to 6x \to 6 \to 0$; integrales de $\sin x$: $-\cos x \to -\sin x \to \cos x \to \sin x \to -\cos x$.
> >
> > **Diagonales con signos alternados:**
> >
> > - $+\, x^3 \cdot (-\cos x) = -x^3\cos x$
> > - $-\, 3x^2 \cdot (-\sin x) = +3x^2\sin x$
> > - $+\, 6x \cdot \cos x = +6x\cos x$
> > - $-\, 6 \cdot \sin x = -6\sin x$
> >
> > **Respuesta:** $-x^3\cos x + 3x^2\sin x + 6x\cos x - 6\sin x + C$.
> >
> > **Cuidado:** la derivada de la fila $k$ se empareja con la integral de la fila $k+1$ (diagonal), no con la propia ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int x^2 \ln(x)\,dx$ y explica por qué la tabla falla aquí.
>
> > [!success]- ✅ Solución
> >
> > **Por qué falla la tabla:** derivar $\ln x$ nunca llega a 0 ($\frac{1}{x} \to -\frac{1}{x^2} \to \dots$), así que la columna izquierda no termina.
> >
> > **Método tradicional:** $u = \ln x$, $dv = x^2\,dx$; $du = \frac{1}{x}dx$, $v = \frac{x^3}{3}$.
> >
> > $$\int x^2 \ln x\,dx = \frac{x^3}{3}\ln x - \int \frac{x^3}{3} \cdot \frac{1}{x}\,dx = \frac{x^3}{3}\ln x - \frac{1}{3}\int x^2\,dx$$
> >
> > **Respuesta:** $\frac{x^3}{3}\ln x - \frac{x^3}{9} + C$.
> >
> > **Lección:** la tabla exige una columna que se anule; con logaritmos o arctangentes, métodos tradicionales ✓

> [!note] 🏋️ Para practicar (sin solución: resuélvelas tú)
>
> **Nivel básico:**
>
> - $\int x e^x\,dx$ · $\int x^2 \cos(x)\,dx$ · $\int x^3 e^{2x}\,dx$
>
> **Nivel intermedio:**
>
> - $\int x^4 \sin(x)\,dx$ · $\int x^3 e^{-x}\,dx$ · $\int (x^2 + 1) \cos(2x)\,dx$
>
> **Nivel avanzado:**
>
> - $\int x^5 e^x\,dx$ · $\int (x^3 - 2x) \sin(3x)\,dx$
>
> **Por qué importa:** los de nivel intermedio y avanzado están hechos para el método de tabla; si te salen en menos de cinco renglones, domina la técnica.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico la fórmula $\int u\,dv = uv - \int v\,du$ eligiendo $u$ y $dv$ con LIATE.
> - [ ] Resuelvo los tres patrones clásicos ($xe^x$, $x\ln x$, $\ln x$) sin dudar en la elección.
> - [ ] Evalúo integrales definidas por partes sin olvidar el término $[uv]_a^b$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Reconozco el caso cíclico, planteo el sistema con $I$ y despejo la integral.
> - [ ] Construyo la tabla de derivadas e integrales con sus signos alternados.
> - [ ] Cruzo las diagonales correctamente (derivada con la integral de la fila siguiente).

> [!note] 📋 Nivel Avanzado
>
> - [ ] Decido en un vistazo entre método tradicional y tabla según la estructura de la integral.
> - [ ] Combino por partes con cambio de variable o fracciones parciales en una misma integral.
> - [ ] Verifico cada resultado derivando y comparando con el integrando original.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 7.1: integración por partes.
> - G. Strang, *Calculus* (Wellesley-Cambridge): integration by parts y su método visual.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — la técnica previa, para cuando el producto admite sustitución.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — el concepto de $v$ como antiderivada de $dv$.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/04 - Integrales de Funciones Inversas|04 - Integrales de Funciones Inversas]] — la aplicación directa de por partes a $\arctan$, $\arcsin$ y $\ln$.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/05 - Integrales por Fracciones Parciales|05 - Integrales por Fracciones Parciales]] — la técnica complementaria para racionales.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice la fórmula de integración por partes?::$\int u\,dv = uv - \int v\,du$, derivada de la regla del producto; $u$ se deriva y $dv$ se integra.
> - ¿Qué dice LIATE?::Orden para elegir $u$: **L**ogarítmicas, **I**nversas trigonométricas, **A**lgebraicas, **T**rigonométricas, **E**xponenciales; la familia más alta es $u$.
> - ¿Qué recuerda la mnemotecnia UDVIVU?::"Un Día Vi Una Vaca Vestida de Uniforme": $\int U\,dV = UV - \int V\,dU$, con el orden de los factores incluido.
> - ¿Cuándo conviene el método de tabla?::Cuando una función se deriva hasta 0 (polinomios) y la otra se integra fácil varias veces: reúne 3 o más aplicaciones en una sola vista.
> - ¿Cuándo NO usar la tabla?::Con $\ln$ o $\arctan$ (no se anulan), con cíclicas como $\int e^x\sin x$ y cuando una sola aplicación de partes basta.
> - ¿Cómo se resuelve una integral cíclica?::Aplicar por partes dos veces, llamar $I$ a la integral original, sustituirla y despejar: $2I = \dots$ → $I = \dots$
> - ¿Cómo se emparejan las filas de la tabla?::Cada derivada con la integral de la **fila siguiente** (diagonal), con signos alternados $+, -, +, -, \dots$

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — la otra técnica básica: composiciones en lugar de productos.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — potencias de senos y cosenos donde por partes se encuentra con la tabla.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/04 - Integrales de Funciones Inversas|04 - Integrales de Funciones Inversas]] — $\int \arctan x$, $\int \ln x$ y compañía resueltas con esta técnica.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/05 - Integrales por Fracciones Parciales|05 - Integrales por Fracciones Parciales]] — racionales que por partes no alcanza.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — $\int_0^{\infty} x e^{-x}\,dx$ y familia: por partes evaluada con límites.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — integrales donde a veces toca partir por partes.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1, 2 y 3: los tres patrones de LIATE, el esqueleto de la técnica.
> - Después pasa al 4 (cíclica con sistema) y al 5 (definida con $[uv]_a^b$).
> - Cierra con el 6, 7 y 8: el método de tabla, sus diagonales y su límite con los logaritmos.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/V - Técnicas de Integración/03 - Integrales Trigonométricas|Integrales Trigonométricas]]; como siguiente horizonte, la integración por partes **repetida** y la **combinación de técnicas** (por partes + sustitución en la misma integral).

---

**Tags:** #MATG1045 #unidad6 #integracion-por-partes #integrales #por-partes #liate #tecnicas-integracion #udvivu #tabla #metodo-visual

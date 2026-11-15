---
dg-publish: true
tags: [MATG1045, unidad4, regla-de-la-cadena, funciones-compuestas, derivadas, mnemotecnia, capas-de-funcion]
---

# ⛓️ Regla de la Cadena

## 🎯 Introducción

> [!info] 💡 Una función dentro de otra
>
> La **regla de la cadena** deriva funciones compuestas, es decir, funciones donde una está dentro de otra: $\sin(x^2)$, $e^{3x}$, $(x^2+1)^{5}$. En todas hay una **capa externa** que ves a simple vista y una **capa interna** escondida dentro del paréntesis o del exponente.
>
> **La idea en una frase:** se deriva de afuera hacia adentro, y cada capa aporta su propio factor derivado.
>
> **Por qué importa:** sin esta regla no podrías derivar ni la mitad de las funciones del curso, y tampoco entenderías la derivación implícita, la logarítmica ni las razones de cambio relacionadas, que son aplicaciones directas de ella.
>
> **Ejemplo:** $\frac{d}{dx}[\sin(x^2)] = \cos(x^2) \cdot 2x$: la externa $\sin$ se convierte en $\cos$ y la interna $x^2$ aporta su $2x$.

> [!warning] ⚠️ Lo que necesitas dominar antes
>
> - Las reglas básicas y la del producto/cociente: [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]].
> - Qué es una composición de funciones y por qué el orden importa: $f(g(x)) \neq g(f(x))$.
> - Las derivadas de las funciones elementales, que encontrarás en [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]].
>
> **Por qué importa:** la cadena solo multiplica lo que ya sabes derivar. Si no dominas la tabla de derivadas, la regla no te va a salvar.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Función compuesta
>
> Se llama **función compuesta** a la expresión $f(g(x))$, donde una función $g$ se aplica primero y su resultado alimenta a la función $f$. Se lee "$f$ de $g$ de $x$"; a $f$ se le llama **función externa** y a $g$ **función interna**.
>
> $$h(x) = f(g(x)) \qquad \text{con} \qquad u = g(x) \ \Rightarrow\ h(x) = f(u).$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Regla_de_la_Cadena_02.svg]]
>
> **Se lee así:** el diagrama parte de la composición $f(g(x))$ y la separa en dos cajas paralelas, la capa externa $f(u)$ y la capa interna $u = g(x)$. Cada capa baja a su derivada, $f'(u)$ y $g'(x)$, y las dos se juntan en una caja que dice "multiplica ambas"; después queda sustituir $u = g(x)$ y simplificar.
>
> **Por qué importa:** separar las capas **antes** de derivar es el paso donde más se falla. El diagrama obliga a nombrar la externa y la interna por separado, que es exactamente lo que evita el error de olvidar el factor interno.
>
> **Ejemplo:** en $\frac{d}{dx}[(3x+1)^5]$ la externa es $(\cdot)^5$ y la interna es $3x+1$.

> [!note] 📋 Definición — Regla de la cadena
>
> Si $h(x) = f(g(x))$ y ambas funciones son derivables, entonces
>
> $$h'(x) = f'(g(x)) \cdot g'(x), \qquad \text{o bien en notación de Leibniz} \qquad \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}.$$
>
> Se deriva la función **externa evaluada en la interna** y se **multiplica** por la derivada de la interna. Nunca se sustituye antes de derivar: primero $f'$, después $g'$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Regla_de_la_Cadena_01.svg]]
>
> **Se lee así:** es un flujo que arranca con un rombo que pregunta si hay función dentro de otra función. Si la respuesta es "no", la rama baja a usar las reglas básicas; si es "sí", la rama encadena cinco rectángulos: identificar la externa $f(u)$, identificar la interna $u = g(x)$, aplicar $f'(u)$ por $g'(x)$, sustituir $u = g(x)$ y simplificar el resultado.
>
> **Por qué importa:** el rombo inicial es el filtro que decide si la regla toca o no. Muchos errores consisten en aplicar la cadena donde no hay composición, y este diagrama te obliga a preguntarlo antes de escribir nada.
>
> **Ejemplo:** para $\frac{d}{dx}[\sin(x^2)]$ tomas la rama compuesta: externa $\sin(u)$, interna $u = x^2$, y el resultado es $\cos(x^2) \cdot 2x$.

---

## 🔍 Cómo reconocer la composición

> [!example] 📊 Los cuatro patrones que aparecen en los ejercicios
>
> 1. **Potencia de una función:** $[g(x)]^n$ — la interna está elevada a un número.
> 2. **Trigonométrica compuesta:** $\sin(g(x))$, $\cos(g(x))$, $\tan(g(x))$.
> 3. **Exponencial o logaritmo de una función:** $e^{g(x)}$, $\ln(g(x))$.
> 4. **Composición múltiple:** $f(g(h(x)))$, función dentro de función dentro de función.
>
> **Por qué importa:** reconocer el patrón te dice de entrada qué derivada externa va a salir, y con eso la mitad del ejercicio está escrita.
>
> **Ejemplo:** $\ln(x^2+1)$ es el patrón 3: la externa es $\ln(\cdot)$ y la interna $x^2+1$.

> [!tip] 🎓 Mnemotecnia "CADENA" y técnica "DENTRO-FUERA"
>
> **C**omposición → **A**fuera → **D**entro → **E**valúa → **N**otación → **A**decuada:
>
> 1. **C**omposición: identifica que hay una función dentro de otra.
> 2. **A**fuera: deriva primero la función externa.
> 3. **D**entro: multiplica por la derivada de la interna.
> 4. **E**valúa: sustituye la función interna en la derivada externa.
> 5. **N**otación: mantén la notación clara, con paréntesis.
> 6. **A**decuada: simplifica el resultado.
>
> **Técnica "DENTRO-FUERA":** ¿qué función está adentro del paréntesis? (DENTRO) · ¿qué operación se aplica a toda la expresión? (FUERA) · deriva exterior por interior derivado.
>
> **Por qué importa:** el orden "externa primero, interna después" es la regla; invertirlo produce respuestas con sentido pero equivocadas.
>
> **Ejemplo:** en $e^{x^3+2x}$, "dentro" es $x^3+2x$ y "fuera" es $e^{(\cdot)}$.

> [!note] 📝 La capa a capa: método del "pelado"
>
> 1. Identifica las capas de la función.
> 2. Pela una capa a la vez (deriva la externa).
> 3. Multiplica por lo que queda (deriva la interna).
> 4. Repite hasta llegar al centro si hay más de dos capas.
>
> **Por qué importa:** en composiciones de tres o más capas el error típico es saltarse la del medio; pelar capa por capa garantiza que ninguna quede fuera.
>
> **Ejemplo:** en $\sin(\cos(x^2))$ hay tres capas: $\sin$, $\cos$ y $x^2$.

---

## 🧮 Tabla de referencia rápida

> [!note] 🚀 Derivadas que salen de la cadena
>
> | Función | Derivada |
> |---------|----------|
> | $[g(x)]^n$ | $n[g(x)]^{n-1} \cdot g'(x)$ |
> | $\sin(g(x))$ | $\cos(g(x)) \cdot g'(x)$ |
> | $\cos(g(x))$ | $-\sin(g(x)) \cdot g'(x)$ |
> | $\tan(g(x))$ | $\sec^2(g(x)) \cdot g'(x)$ |
> | $e^{g(x)}$ | $e^{g(x)} \cdot g'(x)$ |
> | $\ln(g(x))$ | $\frac{g'(x)}{g(x)}$ |
> | $\sqrt{g(x)}$ | $\frac{g'(x)}{2\sqrt{g(x)}}$ |
>
> **Por qué importa:** cada fila es la derivada externa de la tabla de derivadas, evaluada en la interna, por la derivada de la interna. Si memorizas la fila 4, ya sabes la 5 y la 6.
>
> **Ejemplo:** $\frac{d}{dx}[\ln(x^2+1)] = \frac{2x}{x^2+1}$: externa $\ln$, interna $x^2+1$.

> [!info] 📐 Cadena generalizada y casos especiales
>
> - **Cadena de $n$ funciones:** $\frac{d}{dx}[f_1(f_2(\cdots f_n(x)\cdots))] = f_1'(\cdots) \cdot f_2'(\cdots) \cdots f_n'(x)$; se van encadenando factores desde la externa hasta la interna.
> - **Uso en derivación implícita:** si $y$ depende de $x$, entonces $\frac{d}{dx}[y^2] = 2y \frac{dy}{dx}$: la cadena aparece sin decir su nombre. En $x^2 + y^2 = 25$ se obtiene $2x + 2y\frac{dy}{dx} = 0$.
>
> **Por qué importa:** la segunda fila es el puente hacia [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]]: ahí la cadena se aplica a cada término con $y$.
>
> **Ejemplo:** en $\frac{d}{dx}[\sin(x^3+2x)]$ solo hay dos capas; en $\sin(\cos(x^2))$ hay tres y se aplica la cadena dos veces.

---

## 💡 Ejemplos resueltos

> [!example] 🔢 Ejemplo 1: potencia de una función
>
> **Resolver** $\frac{d}{dx}[(3x+1)^5]$.
>
> - Externa: $f(u) = u^5$ con $f'(u) = 5u^4$.
> - Interna: $u = 3x+1$ con $g'(x) = 3$.
>
> $$\frac{d}{dx}[(3x+1)^5] = 5(3x+1)^4 \cdot 3 = 15(3x+1)^4.$$
>
> **Por qué importa:** el $3$ del interno es el factor que la mayoría olvida; sin él la respuesta tiene la forma correcta pero un valor equivocado.

> [!example] 🔢 Ejemplo 2: trigonométrica compuesta
>
> **Resolver** $\frac{d}{dx}[\sin(x^2)]$.
>
> - Externa: $f(u) = \sin u$ con $f'(u) = \cos u$.
> - Interna: $u = x^2$ con $g'(x) = 2x$.
>
> $$\frac{d}{dx}[\sin(x^2)] = \cos(x^2) \cdot 2x = 2x\cos(x^2).$$
>
> **Por qué importa:** el argumento $x^2$ se conserva intacto dentro del coseno: se deriva la carcasa, no el contenido.

> [!example] 🔢 Ejemplo 3: exponencial compuesta
>
> **Resolver** $\frac{d}{dx}[e^{x^3+2x}]$.
>
> - Externa: $f(u) = e^u$ con $f'(u) = e^u$.
> - Interna: $u = x^3+2x$ con $g'(x) = 3x^2+2$.
>
> $$\frac{d}{dx}[e^{x^3+2x}] = e^{x^3+2x} \cdot (3x^2+2).$$
>
> **Por qué importa:** la exponencial se deriva igual a sí misma, así que el único trabajo real está en la interna.

> [!example] 🔢 Ejemplo 4: composición triple
>
> **Resolver** $\frac{d}{dx}[\sin(\cos(x^2))]$ por capas.
>
> - Capa 1 (interna): $h(x) = x^2$ con $h'(x) = 2x$.
> - Capa 2 (media): $g(x) = \cos(h(x))$ con $g'(x) = -\sin(x^2) \cdot 2x$.
> - Capa 3 (externa): $f(x) = \sin(g(x))$ con $f'(x) = \cos(\cos(x^2)) \cdot g'(x)$.
>
> $$\frac{d}{dx}[\sin(\cos(x^2))] = \cos(\cos(x^2)) \cdot \big(-\sin(x^2)\big) \cdot 2x = -2x\,\sin(x^2)\,\cos(\cos(x^2)).$$
>
> **Por qué importa:** aparecen **tres** factores, uno por capa. Contarlos es la mejor comprobación rápida de que no se saltó ninguna.

---

## ⚠️ Errores comunes y cómo evitarlos

> [!warning] 🚨 Los tres errores clásicos de la cadena
>
> 1. **Olvidar la derivada interna:** $\frac{d}{dx}[(2x+1)^3] = 3(2x+1)^2$ es incorrecto; lo correcto es $3(2x+1)^2 \cdot 2 = 6(2x+1)^2$.
> 2. **Invertir el orden:** se deriva primero la externa y después se multiplica por la interna; derivar primero la interna no tiene ninguna justificación.
> 3. **Aplicar la cadena donde no hay composición:** $\sin(x)$ no es compuesta, su derivada es $\cos x$ sin ningún factor extra.
>
> **Por qué importa:** el primer error es el más frecuente de todo el curso y se detecta con una pregunta: *¿hay algo adentro que yo no derive?*

> [!tip] 💡 Cinco estrategias anti-error
>
> 1. **Nombra** la función externa y la interna antes de escribir la derivada.
> 2. **Escribe** cada derivada por separado, en renglones distintos.
> 3. **Usa paréntesis** para no perder la estructura de la composición.
> 4. **Comprueba** que el número de factores coincide con el número de capas.
> 5. **Verifica** con un caso simple: la cadena en $(x+1)^2$ da $2(x+1)$, igual que expandiendo.
>
> **Ejemplo:** en $\sin(\cos(x^2))$ esperas tres factores; si tu respuesta trae dos, falta una capa.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Potencia compuesta

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = (3x+1)^5$ y comprueba el resultado expandiendo la potencia si lo deseas.
>
> > [!success]- ✅ Solución
> >
> > Externa $u^5$ con derivada $5u^4$; interna $u = 3x+1$ con derivada $3$.
> >
> > $$f'(x) = 5(3x+1)^4 \cdot 3 = 15(3x+1)^4.$$
> >
> > Verificación por expansión: $(3x+1)^5$ tiene término líder $243x^5$, cuya derivada es $1215x^4$, y $15(3x+1)^4$ empieza por $15 \cdot 81x^4 = 1215x^4$: coinciden.

### ✏️ Ejercicio 2 — Trigonométrica compuesta

> [!example] 📋 Planteamiento
>
> Deriva $g(x) = \sin(x^2)$ y calcula $g'(1)$.
>
> > [!success]- ✅ Solución
> >
> > Externa $\sin(u)$ con derivada $\cos(u)$; interna $u = x^2$ con derivada $2x$.
> >
> > $$g'(x) = \cos(x^2) \cdot 2x = 2x\cos(x^2).$$
> >
> > En $x = 1$: $g'(1) = 2\cos(1) \approx 2(0.5403) \approx 1.0806$.

### ✏️ Ejercicio 3 — Exponencial compuesta

> [!example] 📋 Planteamiento
>
> Deriva $h(x) = e^{x^3+2x}$ e interpreta el signo de la derivada en $x = 0$.
>
> > [!success]- ✅ Solución
> >
> > Externa $e^u$ con derivada $e^u$; interna $u = x^3+2x$ con derivada $3x^2+2$.
> >
> > $$h'(x) = (3x^2+2)\,e^{x^3+2x}.$$
> >
> > En $x = 0$: $h'(0) = 2 \cdot e^0 = 2 > 0$, así que la función crece en el origen. Además $3x^2+2$ y $e^{x^3+2x}$ son siempre positivas, por lo que $h$ es creciente en todo $\mathbb{R}$.

### ✏️ Ejercicio 4 — Composición triple

> [!example] 📋 Planteamiento
>
> Deriva $p(x) = \sin(\cos(x^2))$ contando los factores que deberían salir.
>
> > [!success]- ✅ Solución
> >
> > Hay tres capas, así que la respuesta debe tener tres factores:
> >
> > $$p'(x) = \cos(\cos(x^2)) \cdot \big(-\sin(x^2)\big) \cdot 2x = -2x\,\sin(x^2)\,\cos(\cos(x^2)).$$
> >
> > Factores: $\cos(\cos(x^2))$ (externa), $-\sin(x^2)$ (media) y $2x$ (interna). Si tu respuesta tiene dos, olvidaste una capa.

### ✏️ Ejercicio 5 — Raíz compuesta

> [!example] 📋 Planteamiento
>
> Deriva $q(x) = \sqrt{x^2+1}$ y determina en qué puntos la tangente es horizontal.
>
> > [!success]- ✅ Solución
> >
> > Reescribe $q(x) = (x^2+1)^{1/2}$: externa $u^{1/2}$ con derivada $\frac{1}{2}u^{-1/2}$; interna $u = x^2+1$ con derivada $2x$.
> >
> > $$q'(x) = \frac{1}{2}(x^2+1)^{-1/2} \cdot 2x = \frac{x}{\sqrt{x^2+1}}.$$
> >
> > La tangente es horizontal cuando $q'(x) = 0$, es decir cuando el numerador se anula: $x = 0$. El denominador nunca se anula, así que $x = 0$ es el único punto (el vértice de la curva).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico la función externa y la interna de una composición sin derivar.
> - [ ] Escribo la regla de la cadena en notación de Lagrange y en notación de Leibniz.
> - [ ] Derivo potencias, trigonométricas y exponenciales compuestas con un solo factor interno.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Derivo composiciones de tres o más capas contando los factores que deben salir.
> - [ ] Aplico la cadena dentro de la derivación implícita de una ecuación con $y$.
> - [ ] Verifico una derivada por cadena contra un caso que se pueda expandir.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Combino la cadena con la regla del producto o la del cociente en la misma función.
> - [ ] Reconozco cuándo **no** hay composición y evito factores de más.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 3: la regla de la cadena y sus aplicaciones.
> - R. Larson, *Cálculo* (Cengage), cap. 3: composición de funciones y derivadas compuestas.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la definición de derivada que la cadena generaliza.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — las reglas con las que se combina.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cómo se escribe la regla de la cadena?::$\big(f(g(x))\big)' = f'(g(x)) \cdot g'(x)$: derivada de la externa evaluada en la interna, multiplicada por la derivada de la interna.
> - ¿Cuál es la versión de Leibniz?::$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$, con $u$ la función interna.
> - ¿Cómo distingues si hay composición?::Preguntando si hay una función adentro de otra: si puedo escribir $f(g(x))$ con $g$ distinta de $f$, hay cadena.
> - ¿Cuántos factores debe tener la derivada de $\sin(\cos(x^2))$?::Tres, uno por capa: $\cos(\cos(x^2)) \cdot (-\sin(x^2)) \cdot 2x$.
> - ¿Qué error se comete con $\frac{d}{dx}[(2x+1)^3]$?::Olvidar el factor $2$ de la interna; lo correcto es $6(2x+1)^2$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — de dónde sale la noción de derivada de una composición.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — producto, cociente y potencia, con los que la cadena se combina.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — la cadena aplicada a cada término con $y$.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]] — la cadena dentro del $\ln$.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]] — la cadena aplicada dos veces seguidas.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero con potencias compuestas: son las que más rápido se automatizan.
> - Después salta a las composiciones de tres capas para acostumbrarte a contar factores.
> - Cuando la ecuación traiga $y$ mezclada con $x$, ve a [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]]: ahí la cadena aparece en cada término con $y$.
> - Para $f(x)^{g(x)}$ no alcanza la cadena: usa [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]].

---

**Tags:** #MATG1045 #unidad4 #regla-de-la-cadena #funciones-compuestas #derivadas #mnemotecnia #capas-de-funcion

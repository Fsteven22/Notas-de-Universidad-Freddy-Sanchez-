---
dg-publish: true
tags: [MATG1045, unidad4, tabla-de-derivadas-basicas, referencias-rapidas, formulas, funciones-elementales]
---

# 📋 Tabla de Derivadas Básicas

## 🎯 Introducción

> [!quote] 💬 Cita de la nota
>
> _"Las fórmulas de derivación son herramientas esenciales que todo estudiante de cálculo debe dominar. Esta tabla de referencia rápida complementa el estudio teórico profundo, proporcionando acceso inmediato a las fórmulas fundamentales necesarias para resolver problemas de derivación."_

> [!info] 💡 Qué es esta nota
>
> Esta es la **chuleta** de la unidad: las trece fórmulas directas que convierte cualquier función elemental en su derivada, más las reglas de combinación que las ponen a trabajar juntas. No sustituye a la teoría; la consulta cuando ya entiendes de dónde sale cada fórmula.
>
> **Notación utilizada:** operador $D_x f(x)$ o $f'(x)$ para la derivada; $\frac{dy}{dx}$ en notación de Leibniz; $\sin x$, $\cos x$, $\tan x$, $\cot x$, $\sec x$, $\csc x$ para las trigonométricas.
>
> **Por qué importa:** en un parcial no se deriva desde la definición: se reconoce la función, se busca la fila de la tabla y se aplica. Tener este mapa a la vista reduce los errores de memoria.
>
> **Ejemplo:** para $f(x) = e^x + \sin x$ consultas las filas de exponencial y seno, sumas las derivadas y obtienes $f'(x) = e^x + \cos x$.

> [!warning] ⚠️ Para qué sirve y para qué no
>
> - **Sirve** para derivar rápido funciones ya reconocidas y para verificar un resultado hecho a mano.
> - **Sirve** como puente a integrales: cada fila de la tabla tiene su fila espejo en [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]].
> - **No sirve** para derivar composiciones: ahí hace falta la [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]].
> - **No sustituye** la comprensión: si no sabes por qué $(\cos x)' = -\sin x$, el signo negativo se te va a olvidar justo cuando más lo necesites.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Tabla de derivadas básicas
>
> La **tabla de derivadas básicas** es el catálogo de igualdades $D_x(f) = f'$ que resuelve la derivada de cada función elemental sin volver al límite: constantes, potencias, exponenciales, logarítmicas, trigonométricas y sus inversas.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/cal1-derivadas-tabla-13-reglas-dx.png]]
>
> **Se lee así:** Se ve una tabla enmarcada de trece filas, agrupadas por familias de funciones: algebraicas, exponenciales, logarítmicas y trigonométricas. Cada fila enfrenta la función en una columna con su derivada en la otra, y todas las igualdades están escritas con la notación de operador $D_x(f) = f'$. Debajo hay un pie que la presenta como referencia de consulta rápida.
>
> **Por qué importa:** Es tu chuleta para no improvisar: con la tabla a la vista pasas de la función al resultado sin memorizar de memoria, y la notación de operador te prepara para las reglas de composición.
>
> **Ejemplo:** En un parcial te piden derivar $f(x) = e^x + \sin x$: consultas la tabla, sumas las derivadas de cada parte y obtienes $f'(x) = e^x + \cos(x)$.

> [!note] 📋 Definición — Operador de derivación $D_x$
>
> El **operador $D_x$** aplica la derivada a una expresión: $D_x[f(x)] = f'(x)$. Es una forma compacta de escribir "la derivada respecto a $x$ de lo que va entre corchetes", y admite composición: $D_x[f \circ g] = D_x[f(g(x))]$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/cal1-derivadas-tabla-15-formulas-dx.png]]
>
> **Se lee así:** Es una lámina en **dos columnas numeradas**: la izquierda lleva las primeras ocho igualdades y la derecha las siete restantes, con la numeración corrida para que no falte ninguna. Cada línea repite la misma forma, operador de derivación a la izquierda y resultado a la derecha, y las últimas filas incluyen ya las inversas trigonométricas con sus raíces cuadradas.
>
> **Por qué importa:** Fíjate en que las quince entradas usan la misma notación de operador y la misma disposición, así que puedes leerlas en diagonal para repasar rápido. Tenerla delante en un parcial te evita improvisar y te permite **verificar** un resultado derivando la expresión otra vez.
>
> **Ejemplo:** Para derivar $f(x) = e^x + \sin x$ consultas las filas de exponencial y seno, sumas las dos derivadas y obtienes $f'(x) = e^x + \cos x$, tal como aparece en los ejemplos rápidos de la nota.

---

## 📊 Las trece fórmulas fundamentales

> [!abstract] 📋 La tabla completa, fila por fila
>
> Estas son las trece igualdades que debes dominar de memoria. Se leen siempre igual: a la izquierda la función, a la derecha su derivada.
>
> | # | Función | Derivada |
> |---|---------|----------|
> | 1 | $D_x(k) = 0$ | toda constante $k \in \mathbb{R}$ |
> | 2 | $D_x(x) = 1$ | la identidad |
> | 3 | $D_x(x^n) = n x^{n-1}$ | potencia, para cualquier $n$ real |
> | 4 | $D_x(e^x) = e^x$ | la exponencial natural se copia |
> | 5 | $D_x(a^x) = a^x \ln a$ | base $a > 0$, $a \neq 1$ |
> | 6 | $D_x(\ln x) = \frac{1}{x}$ | $x > 0$ |
> | 7 | $D_x(\log_a x) = \frac{1}{x \ln a}$ | base $a > 0$, $a \neq 1$ |
> | 8 | $D_x(\sin x) = \cos x$ | |
> | 9 | $D_x(\cos x) = -\sin x$ | **signo negativo** |
> | 10 | $D_x(\tan x) = \sec^2 x$ | igual que $1/\cos^2 x$ |
> | 11 | $D_x(\cot x) = -\csc^2 x$ | **signo negativo** |
> | 12 | $D_x(\sec x) = \sec x \tan x$ | |
> | 13 | $D_x(\csc x) = -\csc x \cot x$ | **signo negativo** |
>
> **Por qué importa:** las filas 9, 11 y 13 son las que más se olvidan porque llevan signo negativo; las filas 5 y 7 son las que más se olvidan porque llevan el factor $\ln a$. Si tu respuesta trae un signo de más o un $\ln a$ de menos, revisa esas tres filas primero.
>
> **Ejemplo:** $D_x(\log_{10} x) = \frac{1}{x \ln 10}$: se toma la fila 7 con $a = 10$.

---

## ⚡ Reglas de combinación

> [!example] ⚡ Las cuatro reglas que combinan la tabla
>
> **Suma y diferencia:**
>
> $$D_x[f(x) \pm g(x)] = f'(x) \pm g'(x)$$
>
> **Producto:**
>
> $$D_x[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$
>
> **Cociente:**
>
> $$D_x\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}$$
>
> **Cadena:**
>
> $$D_x[f(g(x))] = f'(g(x)) \cdot g'(x)$$
>
> **Por qué importa:** la tabla te da la derivada de cada pieza; estas cuatro reglas te dicen cómo ensamblarlas. Juntas cubren el 99% de los ejercicios de la unidad.
>
> **Ejemplo:** para derivar $\frac{\sin x}{x}$ combinas la fila 8 con la regla del cociente: $\frac{x\cos x - \sin x}{x^2}$.

---

## 📝 Casos especiales y extensiones

> [!note] 🔢 Extensiones útiles de las fórmulas básicas
>
> **Potencias con exponente negativo:**
>
> - $D_x(x^{-n}) = -n x^{-n-1} = -\frac{n}{x^{n+1}}$
> - $D_x\left(\frac{1}{x}\right) = -\frac{1}{x^2}$
>
> **Raíces escritas como potencias:**
>
> - $D_x(\sqrt{x}) = D_x(x^{1/2}) = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$
> - $D_x(\sqrt[n]{x}) = \frac{1}{n} x^{(1/n)-1}$
>
> **Trigonométricas con coeficiente interno (cadena):**
>
> - $D_x(\sin(ax)) = a\cos(ax)$
> - $D_x(\cos(ax)) = -a\sin(ax)$
> - $D_x(\tan(ax)) = a\sec^2(ax)$
>
> **Por qué importa:** casi ningún ejercicio llega escrito tal cual a la tabla: hay que reescribir raíces como potencias y sacar el coeficiente interno antes de aplicar la fila correspondiente.
>
> **Ejemplo:** $\frac{d}{dx}[\sqrt[3]{x}] = \frac{1}{3}x^{-2/3} = \frac{1}{3\sqrt[3]{x^2}}$.

---

## 🚀 Ejemplos rápidos

> [!success] 🚀 Tres aplicaciones directas
>
> **1. Polinomio:** $f(x) = 3x^4 - 2x^3 + 5x - 7$
>
> $$f'(x) = 12x^3 - 6x^2 + 5$$
>
> **2. Suma exponencial-trigonométrica:** $f(x) = e^x + \sin x$
>
> $$f'(x) = e^x + \cos x$$
>
> **3. Producto con regla del producto:** $f(x) = x^2 \sin x$
>
> $$f'(x) = 2x\sin x + x^2\cos x$$
>
> **Por qué importa:** los tres casos son los que más salen en los ejercicios cortos: polinomio (filas 1-3), suma de elementales (filas 4 y 8) y producto (tabla + regla del producto).
>
> **Ejemplo:** en el caso 3, la tabla aporta $(x^2)' = 2x$ y $(\sin x)' = \cos x$, y el ensamblaje lo hace la regla del producto.

> [!tip] 🧠 Mnemotecnia "TABLA"
>
> - **T** — **Tipo:** identifica la familia de la función (algebraica, exponencial, logarítmica, trigonométrica).
> - **A** — **Aplica:** usa la fórmula directa correspondiente de la tabla.
> - **B** — **Busca:** ¿hay composición? Entonces aplica la cadena.
> - **L** — **Linealiza:** separa sumas y diferencias y deriva término a término.
> - **A** — **Ajusta:** simplifica el resultado final y revisa signos.
>
> **Por qué importa:** es el orden mental que evita el error de aplicar una fórmula directa a una función compuesta.

---

## 🔄 Relación con las integrales

> [!info] 🔄 La tabla tiene una versión en espejo
>
> Si $D_x F(x) = f(x)$, entonces $\int f(x)\,dx = F(x) + C$. Cada fila de la tabla es la mitad izquierda de una integral notable:
>
> - $D_x(x^2) = 2x$ ↔ $\int 2x\,dx = x^2 + C$
> - $D_x(\sin x) = \cos x$ ↔ $\int \cos x\,dx = \sin x + C$
> - $D_x(e^x) = e^x$ ↔ $\int e^x\,dx = e^x + C$
>
> **Por qué importa:** el mismo espejo aparece en el Teorema Fundamental del Cálculo: derivar e integrar son procesos inversos. Memorizar la tabla hoy te ahorra memorizar dos listas mañana.
>
> **Ejemplo:** si te piden $\int \frac{1}{x}\,dx$, buscas la fila 6 de la tabla al revés y obtienes $\ln|x| + C$.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Polinomio por la tabla

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = 3x^4 - 2x^3 + 5x - 7$ usando únicamente las filas 1 a 3 de la tabla.
>
> > [!success]- ✅ Solución
> >
> > Se deriva término a término: la fila 3 con $n = 4$, $n = 3$ y $n = 1$, la fila 2 para $5x$ y la fila 1 para la constante.
> >
> > $$f'(x) = 12x^3 - 6x^2 + 5.$$
> >
> > El $-7$ desaparece porque su derivada es $0$.

### ✏️ Ejercicio 2 — Suma de elementales

> [!example] 📋 Planteamiento
>
> Deriva $g(x) = e^x + \sin x$ y evalúa $g'(0)$.
>
> > [!success]- ✅ Solución
> >
> > Fila 4: $(e^x)' = e^x$; fila 8: $(\sin x)' = \cos x$.
> >
> > $$g'(x) = e^x + \cos x.$$
> >
> > En $x = 0$: $g'(0) = e^0 + \cos 0 = 1 + 1 = 2$.

### ✏️ Ejercicio 3 — Tabla más regla del producto

> [!example] 📋 Planteamiento
>
> Deriva $h(x) = x^2 \sin x$ y determina el signo de la pendiente en $x = \pi$.
>
> > [!success]- ✅ Solución
> >
> > Con la regla del producto y las filas 3 y 8:
> >
> > $$h'(x) = 2x\sin x + x^2\cos x.$$
> >
> > En $x = \pi$: $h'(\pi) = 2\pi \cdot 0 + \pi^2 \cdot (-1) = -\pi^2 < 0$, así que la función está decreciendo en ese punto.

### ✏️ Ejercicio 4 — Logaritmo y recíproco

> [!example] 📋 Planteamiento
>
> Deriva $p(x) = \ln x - \frac{1}{x}$ (dominio $x > 0$) y encuentra dónde la tangente es horizontal.
>
> > [!success]- ✅ Solución
> >
> > Fila 6: $(\ln x)' = \frac{1}{x}$; extensión de la fila 3 con $n = -1$: $(1/x)' = -\frac{1}{x^2}$, así que la derivada del segundo término es $+\frac{1}{x^2}$.
> >
> > $$p'(x) = \frac{1}{x} + \frac{1}{x^2} = \frac{x+1}{x^2}.$$
> >
> > Se anula cuando $x + 1 = 0$, es decir $x = -1$, que está fuera del dominio: **no hay tangente horizontal** para $x > 0$; la función siempre crece en su dominio.

### ✏️ Ejercicio 5 — Inversas trigonométricas

> [!example] 📋 Planteamiento
>
> Deriva $q(x) = \tan x - \arctan x$ y discute el signo de su derivada.
>
> > [!success]- ✅ Solución
> >
> > Fila 10: $(\tan x)' = \sec^2 x$; fila de las inversas: $(\arctan x)' = \frac{1}{1+x^2}$.
> >
> > $$q'(x) = \sec^2 x - \frac{1}{1+x^2}.$$
> >
> > Como $\sec^2 x \geq 1$ y $\frac{1}{1+x^2} < 1$ para todo $x$, la diferencia siempre es positiva: $q$ es creciente en todo su dominio.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo de memoria las trece fórmulas de la tabla con sus condiciones de dominio.
> - [ ] Distingo las tres derivadas con signo negativo entre las trigonométricas.
> - [ ] Derivo polinomios y sumas de funciones elementales usando la tabla.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Combino la tabla con las reglas de suma, producto y cociente en un mismo ejercicio.
> - [ ] Reescribo raíces y exponentes negativos como potencias antes de derivar.
> - [ ] Reconozco cuándo una función necesita la regla de la cadena en lugar de una fila directa.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Uso la tabla al revés para resolver integrales notables.
> - [ ] Verifico una derivada de la tabla con el cociente incremental.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), tablas de derivadas de las secciones iniciales de cap. 3.
> - R. Larson, *Cálculo* (Cengage), tabla resumen de derivadas.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — de dónde salen estas fórmulas.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — cuándo la derivada garantizadamente existe.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — la tabla espejo.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuáles son las tres derivadas trigonométricas con signo negativo?::$(\cos x)' = -\sin x$, $(\cot x)' = -\csc^2 x$ y $(\csc x)' = -\csc x \cot x$.
> - ¿Qué factor aparece en las derivadas con base distinta de $e$?::El $\ln a$: $(a^x)' = a^x \ln a$ y $(\log_a x)' = \frac{1}{x \ln a}$.
> - ¿Cómo se deriva $\sqrt{x}$ con la tabla?::Como potencia: $x^{1/2}$, y la fila 3 da $\frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$.
> - ¿Cuál es la fila espejo de $(\sin x)' = \cos x$?::$\int \cos x\,dx = \sin x + C$: derivar e integrar son procesos inversos.
> - ¿Cuándo la tabla no basta?::Cuando hay composición: entonces toca la regla de la cadena.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — las reglas que explican por qué cada fila de la tabla es así.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — lo que hace falta cuando la función no llega tal cual a la tabla.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas|03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas]] — las mismas familias, explicadas una por una.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — la tabla leída al revés.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Imprime o deja abierta esta tabla mientras practicas: la meta es que en dos semanas la escribas de memoria sin mirar.
> - Practica el reconocimiento: mira una función y di **en qué fila cae** antes de derivar.
> - Cuando aparezcan funciones compuestas, salta a [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]].
> - Cuando quieras el porqué de cada fórmula, lee [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]].

---

**Tags:** #MATG1045 #unidad4 #tabla-de-derivadas-basicas #referencias-rapidas #formulas #funciones-elementales

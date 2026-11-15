---
dg-publish: true
tags: [MATG1045, unidad4, derivadas-de-orden-superior, segunda-derivada, concavidad, regla-leibniz, series-taylor, puntos-inflexion, analisis-funciones]
---

# 📈 Derivadas de Orden Superior

## 🎯 Introducción

> [!info] 💡 Qué son las derivadas de orden superior
>
> Las **derivadas de orden superior** son derivadas de derivadas. La primera derivada da la tasa de cambio instantánea; las siguientes revelan la curvatura, los puntos de inflexión y el comportamiento local de la función.
>
> **Por qué importa:** cada orden responde una pregunta distinta sobre la misma curva. Con $f$ tienes el valor, con $f'$ la pendiente, con $f''$ la curvatura. Además, las derivadas superiores son los **coeficientes** de la serie de Taylor, que es la herramienta con la que se aproximan funciones difíciles.
>
> **Ejemplo:** en $f(x) = x^4 - 4x^3 + 6x^2$ la segunda derivada $f''(x) = 12(x-1)^2$ dice que la función es cóncava hacia arriba en todo el dominio, y la tercera $f'''(x) = 24(x-1)$ confirma que en $x = 1$ hay inflexión.

> [!warning] ⚠️ El error que más se repite
>
> - **NO** confundas $f^{(n)}(x)$ con $[f(x)]^n$: el paréntesis indica *derivada de orden $n$*, no potencia.
> - **NO** des por hecho un patrón: calcula las primeras tres o cuatro derivadas antes de generalizar.
> - **NO** concluyas inflexión solo porque $f''(x_0) = 0$: falta verificar el cambio de signo.
>
> **Por qué importa:** los tres son errores de procedimiento, y son los que el parcial penaliza con más frecuencia.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Derivada de orden superior
>
> Si $f$ es derivable $n$ veces, la **derivada de orden $n$** (o derivada $n$-ésima) se define por derivación sucesiva:
>
> $$f^{(n)}(x) = \frac{d^n}{dx^n}f(x) = \frac{d}{dx}\left(\frac{d^{n-1}}{dx^{n-1}}f(x)\right).$$
>
> La notación de Leibniz escribe $\frac{d^ny}{dx^n}$ para $y = f(x)$; la de Lagrange, $f^{(n)}(x)$; y en física se usan los puntos sobre la variable: $\dot{f}$, $\ddot{f}$, $\dddot{f}$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivadas_de_Orden_Superior_01.svg]]
>
> **Se lee así:** es una cadena de rectángulos, uno por cada orden de derivación, donde cada caja apunta a la siguiente para mostrar que derivar es derivar de nuevo. De cada una sale además una flecha lateral hacia un recuadro paralelo con lo que aporta ese orden concreto: el valor, el crecimiento, la concavidad, los puntos de inflexión y el comportamiento más complejo.
>
> **Por qué importa:** cada orden responde una pregunta distinta sobre la misma función: pendiente, velocidad, concavidad. Tener el mapa te evita confundir $f''(x) > 0$ con un máximo y te muestra **qué puedes concluir** de cada derivada.
>
> **Ejemplo:** en el análisis de $f(x) = x^4 - 4x^3 + 6x^2$, la tercera derivada da $f'''(x) = 24(x-1)$ y con ella confirmas el punto de inflexión en $x = 1$.

---

## 🧮 Cómo se calculan

> [!example] 🔢 Polinomio: todas sus derivadas
>
> **Función:** $f(x) = 2x^5 - 3x^4 + x^3 - 2x^2 + 5x - 1$.
>
> - $f'(x) = 10x^4 - 12x^3 + 3x^2 - 4x + 5$.
> - $f''(x) = 40x^3 - 36x^2 + 6x - 4$.
> - $f'''(x) = 120x^2 - 72x + 6$.
> - $f^{(4)}(x) = 240x - 72$.
> - $f^{(5)}(x) = 240$.
> - $f^{(6)}(x) = 0$, y $f^{(n)}(x) = 0$ para todo $n \ge 6$.
>
> **Por qué importa:** un polinomio de grado $n$ tiene derivada cero para órdenes mayores que $n$. Es el caso más simple para verificar que el método funciona.

> [!example] 🔢 Exponenciales: el patrón se mantiene
>
> - Para $f(x) = e^x$: $f'(x) = e^x$, $f''(x) = e^x$, $f'''(x) = e^x$… luego $\frac{d^n}{dx^n}[e^x] = e^x$ para todo $n \ge 0$.
> - Para $f(x) = e^{ax}$, con $a$ constante: $f'(x) = ae^{ax}$, $f''(x) = a^2e^{ax}$, $f'''(x) = a^3e^{ax}$… luego $\frac{d^n}{dx^n}[e^{ax}] = a^n e^{ax}$.
>
> **Por qué importa:** cada derivación solo multiplica por $a$, porque $\frac{d}{dx}e^{ax} = a e^{ax}$. Reconocer esto ahorra media hora de cuenta.

> [!info] 🖼️ El ciclo de cuatro del seno y el coseno
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivadas_de_Orden_Superior_02.svg]]
>
> **Se lee así:** aparecen dos ciclos cerrados de cuatro rectángulos, como dos ruedas que giran por separado. En cada rueda las casillas recorren el mismo ciclo de cuatro pasos —la función base, su derivada, la de la función opuesta y la de su opuesta— y la flecha de vuelta cierra el periodo. Los dos ciclos están desfasados: el coseno va un paso por delante del seno.
>
> **Por qué importa:** el periodo 4 es la clave: *¿cuántas derivadas hasta volver a la función original?* Con el ciclo a la vista no memorizas signos sueltos y puedes escribir la fórmula general con $n\pi/2$ sin equivocarte.
>
> **Ejemplo:** para $\cos(x)$, la cuarta derivada vuelve a $\cos(x)$, y por eso la fórmula general resulta $\frac{d^n}{dx^n}[\cos(x)] = \cos\left(x + \frac{n\pi}{2}\right)$.

> [!example] 🔢 Logaritmos y potencias
>
> **Logaritmo natural, $f(x) = \ln x$:**
>
> - $f'(x) = \frac{1}{x} = x^{-1}$.
> - $f''(x) = -\frac{1}{x^2}$.
> - $f'''(x) = \frac{2}{x^3}$.
> - $f^{(4)}(x) = -\frac{6}{x^4}$.
>
> Patrón: $\frac{d^n}{dx^n}[\ln x] = \frac{(-1)^{n+1}(n-1)!}{x^n}$ para $n \ge 1$.
>
> **Potencia, $f(x) = x^m$:** $f'(x) = mx^{m-1}$, $f''(x) = m(m-1)x^{m-2}$, $f'''(x) = m(m-1)(m-2)x^{m-3}$, y en general $\frac{d^n}{dx^n}[x^m] = \frac{m!}{(m-n)!}x^{m-n}$ para $n \le m$ (y $0$ si $n > m$).
>
> **Por qué importa:** el signo del logaritmo **alterna** porque cada derivación baja un exponente y lo hace negativo; el factorial aparece porque multiplicar por $-1$, luego por $-2$, luego por $-3$… reconstruye $(n-1)!$.

> [!info] 📋 Fórmulas generales que conviene tener a mano
>
> | Función | $n$-ésima derivada | Observaciones |
> |---|---|---|
> | $x^m$ | $\frac{m!}{(m-n)!}x^{m-n}$ si $n \le m$; $0$ si $n > m$ | $m$ entero positivo |
> | $e^{ax}$ | $a^n e^{ax}$ | Nunca se anula |
> | $\sin(ax)$ | $a^n \operatorname{sen}\left(ax + \frac{n\pi}{2}\right)$ | Periodo 4 en $n$ |
> | $\cos(ax)$ | $a^n \cos\left(ax + \frac{n\pi}{2}\right)$ | Periodo 4 en $n$ |
> | $\ln x$ | $\frac{(-1)^{n+1}(n-1)!}{x^n}$, $n \ge 1$ | Factorial en el numerador |
> | $(1+x)^m$ | $\frac{m!}{(m-n)!}(1+x)^{m-n}$ si $n \le m$ | Binomio generalizado |
> | $\frac{1}{1-x}$ | $\frac{n!}{(1-x)^{n+1}}$ | Patrón por derivación directa |
>
> **Por qué importa:** la tabla convierte el problema en una consulta: identifica la familia de tu función y aplica la fila.

---

## 🧮 Reglas para órdenes superiores

> [!success] ✅ Linealidad
>
> $$\frac{d^n}{dx^n}\big[a f(x) + b g(x)\big] = a\frac{d^n}{dx^n}f(x) + b\frac{d^n}{dx^n}g(x).$$
>
> Las derivadas de orden superior respetan la linealidad: derivar suma de funciones es sumar sus derivadas. Es lo que permite calcular la derivada de un polinomio término a término.

> [!success] ✅ Regla de Leibniz (producto)
>
> $$\frac{d^n}{dx^n}\big[f(x)g(x)\big] = \sum_{k=0}^{n} \binom{n}{k} f^{(k)}(x)\, g^{(n-k)}(x).$$
>
> Es la **generalización de la regla del producto** y tiene la misma estructura que el binomio de Newton $(a+b)^n = \sum_{k=0}^n \binom{n}{k}a^k b^{n-k}$, con derivadas en vez de potencias.
>
> - $n = 1$: $(fg)' = f'g + fg'$ (la regla del producto usual).
> - $n = 2$: $(fg)'' = f''g + 2f'g' + fg''$.
> - $n = 3$: $(fg)''' = f'''g + 3f''g' + 3f'g'' + fg'''$.
>
> **Por qué importa:** los coeficientes $\binom{n}{k}$ son los del binomio, y por eso los términos medios se repiten: no es un forget de dos derivadas, sino una suma ponderada.

> [!example] 🔢 Leibniz en acción: $\frac{d^3}{dx^3}[x^2 e^x]$
>
> - $f(x) = x^2$: $f'(x) = 2x$, $f''(x) = 2$, $f'''(x) = 0$.
> - $g(x) = e^x$: $g'(x) = g''(x) = g'''(x) = e^x$.
> - Aplicando Leibniz con $n = 3$:
>
> $$\binom{3}{0}(0)(e^x) + \binom{3}{1}(2)(e^x) + \binom{3}{2}(2x)(e^x) + \binom{3}{3}(x^2)(e^x)$$
>
> $$= 0 + 6e^x + 6xe^x + x^2e^x = e^x(x^2 + 6x + 6).$$
>
> **Por qué importa:** las derivadas de $e^x$ "secancelan" entre sí y quedan los factores $a^n$ del Leibniz, que es justo lo que hace manejable el cálculo.

> [!info] 🧮 Regla de la cadena para órdenes superiores
>
> Para $y = f(g(x))$, la **fórmula de Faà di Bruno** es
>
> $$\frac{d^n y}{dx^n} = \sum_{k=1}^{n} f^{(k)}(g(x))\cdot B_{n,k}\big(g'(x), g''(x), \ldots, g^{(n-k+1)}(x)\big),$$
>
> donde $B_{n,k}$ son los polinomios de Bell. En la práctica solo se usan los dos primeros casos:
>
> - $n = 1$: $\frac{dy}{dx} = f'(g(x))\,g'(x)$.
> - $n = 2$: $\frac{d^2y}{dx^2} = f''(g(x))[g'(x)]^2 + f'(g(x))\,g''(x)$.
>
> **Por qué importa:** fíjate en el $[g'(x)]^2$: la composición eleva al cuadrado el factor de la cadena. Ese cuadrado es lo que la distingue de la primera derivada.

> [!example] 🔢 Segunda derivada de una composición: $\frac{d^2}{dx^2}[\sin(x^2)]$
>
> - $f(u) = \operatorname{sen}u$, $g(x) = x^2$: $f'(u) = \cos u$, $f''(u) = -\operatorname{sen}u$, $g'(x) = 2x$, $g''(x) = 2$.
> - Aplicando la fórmula:
>
> $$\frac{d^2}{dx^2}[\operatorname{sen}(x^2)] = -\operatorname{sen}(x^2)(2x)^2 + \cos(x^2)\cdot 2 = -4x^2\operatorname{sen}(x^2) + 2\cos(x^2).$$
>
> **Por qué importa:** también sirve derivar dos veces directamente; la fórmula solo evita perder el factor $\frac{d}{dx}$ en algún paso.

---

## 🎪 Aplicaciones e interpretación

> [!info] 📈 Qué dice cada derivada
>
> **En la gráfica:**
>
> - $f''(x) > 0$: función cóncava hacia arriba (forma de U).
> - $f''(x) < 0$: función cóncava hacia abajo (forma de ∩).
> - $f''(x) = 0$: **posible** punto de inflexión (hay que verificar el cambio de signo).
>
> **En la física:**
>
> - Posición $s(t)$ → velocidad $v(t) = s'(t)$ → aceleración $a(t) = s''(t)$ → jerk $j(t) = s'''(t)$ (tasa de cambio de la aceleración).
>
> **Por qué importa:** el mismo formalismo sirve para las dos lecturas; por eso las derivadas superiores son el lenguaje común entre geometría y física.

> [!example] 🔢 Análisis completo de $f(x) = x^4 - 4x^3 + 6x^2$
>
> - $f'(x) = 4x^3 - 12x^2 + 12x = 4x(x^2 - 3x + 3)$.
> - $f''(x) = 12x^2 - 24x + 12 = 12(x-1)^2$.
> - $f'''(x) = 24x - 24 = 24(x-1)$.
>
> **Análisis:**
>
> - **Puntos críticos:** $f'(x) = 0 \Rightarrow x = 0$ (el discriminante de $x^2 - 3x + 3$ es negativo).
> - **Concavidad:** $f''(x) = 12(x-1)^2 \ge 0$ siempre, con $f''(1) = 0$.
> - **Inflexión:** en $x = 1$, porque $f'''(x) = 24(x-1)$ **cambia de signo** al pasar por 1 (y $f''(1) = 0$ por sí solo no bastaba).
> - **Interpretación:** función siempre cóncava hacia arriba, con inflexión en $(1, f(1)) = (1, 3)$.
>
> **Por qué importa:** este ejemplo muestra por qué la tercera derivada entra en juego: cuando la segunda no permite decidir (se anula sin cambio de signo), la tercera sí revela el cruce.

> [!info] 📈 Serie de Taylor: las derivadas como coeficientes
>
> $$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$
>
> Las derivadas de orden superior evaluated en $a$ son los **coeficientes** de la serie. Por eso son el puente entre derivar y aproximar.
>
> **Ejemplo (serie de Taylor de $e^x$ en 0):** como $f^{(n)}(0) = e^0 = 1$ para todo $n$, resulta $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{n=0}^{\infty}\frac{x^n}{n!}$.

> [!warning] 🚨 Errores frecuentes
>
> **De cálculo:**
>
> - Confundir $f^{(n)}(x)$ con $[f(x)]^n$.
> - Equivocar los coeficientes combinatorios al aplicar Leibniz.
> - Perder el signo en el ciclo trigonométrico.
> - Olvidar el factorial en las fórmulas de $\ln x$ y de $x^m$.
>
> **Conceptuales:**
>
> - Asumir un patrón sin verificarlo con casos conocidos.
> - Confundir el orden de derivación en derivadas parciales mixtas.
> - No revisar el dominio: cada derivada puede cambiarlo.
>
> **De aplicación:**
>
> - Leer $f''(x) > 0$ como "hay un mínimo" (solo da concavidad).
> - Declarar inflexión sin verificar el cambio de signo.
> - Ignorar las discontinuidades al derivar varias veces.
>
> **Estrategia de éxito:**
>
> 1. Calcula las primeras tres o cuatro derivadas a mano.
> 2. Busca el patrón solo después de tener esos casos.
> 3. Verifica con un caso conocido (polinomio o exponencial).
> 4. Expresa la fórmula general.

> [!tip] 🎓 Mnemotecnias y analogías
>
> - **"SCRC" para $\sin x$:** **S**in → **C**os → **-S**in → **-C**os → **S**in…
> - **Leibniz es el binomio:** $(fg)^{(n)}$ se expande como $(a+b)^n$, pero con derivadas.
> - **Analogía física:** 1ª derivada = velocidad, 2ª = aceleración, 3ª = jerk.
> - **Proceso de verificación:** derivar 3 o 4 veces → buscar patrón → comprobar con un caso particular → escribir la fórmula general.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Encuentra $f^{(4)}(x)$ para $f(x) = x^6 - 2x^4 + 3x^2$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 6x^5 - 8x^3 + 6x$.
> >
> > $f''(x) = 30x^4 - 24x^2 + 6$.
> >
> > $f'''(x) = 120x^3 - 48x$.
> >
> > $f^{(4)}(x) = 360x^2 - 48$.
> >
> > **Respuesta:** $f^{(4)}(x) = 360x^2 - 48$.

> [!example] 📋 Planteamiento
>
> Calcula $\frac{d^3}{dx^3}[e^{2x}]$.
>
> > [!success]- ✅ Solución
> >
> > Con la fórmula $\frac{d^n}{dx^n}[e^{ax}] = a^n e^{ax}$ y $a = 2$, $n = 3$:
> >
> > $$\frac{d^3}{dx^3}[e^{2x}] = 2^3 e^{2x} = 8e^{2x}.$$
> >
> > **Respuesta:** $8e^{2x}$.

> [!example] 📋 Planteamiento
>
> Determina $\frac{d^2}{dx^2}[\operatorname{sen}(3x)]$.
>
> > [!success]- ✅ Solución
> >
> > Con la fórmula $\frac{d^n}{dx^n}[\operatorname{sen}(ax)] = a^n\operatorname{sen}\left(ax + \frac{n\pi}{2}\right)$ y $a = 3$, $n = 2$:
> >
> > $$\frac{d^2}{dx^2}[\operatorname{sen}(3x)] = 9\operatorname{sen}\left(3x + \pi\right) = -9\operatorname{sen}(3x).$$
> >
> > **Respuesta:** $-9\operatorname{sen}(3x)$.

> [!example] 📋 Planteamiento
>
> Usa la regla de Leibniz para hallar $(x^2 \operatorname{sen} x)'''$.
>
> > [!success]- ✅ Solución
> >
> > Con $f = x^2$ ($f' = 2x$, $f'' = 2$, $f''' = 0$) y $g = \operatorname{sen}x$ ($g' = \cos x$, $g'' = -\operatorname{sen}x$, $g''' = -\cos x$):
> >
> > $$(x^2\operatorname{sen}x)''' = \binom{3}{0}x^2(-\cos x) + \binom{3}{1}(2x)(-\operatorname{sen}x) + \binom{3}{2}(2)(\cos x) + \binom{3}{3}(0)(\operatorname{sen}x)$$
> >
> > $$= -x^2\cos x - 6x\operatorname{sen}x + 6\cos x.$$
> >
> > **Respuesta:** $-x^2\cos x - 6x\operatorname{sen}x + 6\cos x$.

> [!example] 📋 Planteamiento
>
> Calcula $\frac{d^3}{dx^3}[\ln(1+x^2)]$.
>
> > [!success]- ✅ Solución
> >
> > $h'(x) = \frac{2x}{1+x^2}$.
> >
> > $h''(x) = \frac{2(1+x^2) - 2x(2x)}{(1+x^2)^2} = \frac{2 - 2x^2}{(1+x^2)^2}$.
> >
> > $h'''(x) = \frac{-4x(1+x^2) - (2-2x^2)(4x)}{(1+x^2)^3} = \frac{-4x - 4x^3 - 8x + 8x^3}{(1+x^2)^3} = \frac{4x^3 - 12x}{(1+x^2)^3}$.
> >
> > **Respuesta:** $\frac{4x^3 - 12x}{(1+x^2)^3}$.

> [!example] 📋 Planteamiento
>
> Encuentra la segunda derivada de $f(x) = \arctan(x^2)$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = \frac{2x}{1+x^4}$.
> >
> > $f''(x) = \frac{2(1+x^4) - 2x(4x^3)}{(1+x^4)^2} = \frac{2 + 2x^4 - 8x^4}{(1+x^4)^2} = \frac{2 - 6x^4}{(1+x^4)^2}$.
> >
> > **Respuesta:** $\frac{2 - 6x^4}{(1+x^4)^2}$.

> [!example] 📋 Planteamiento
>
> Determina $f^{(n)}(0)$ para $f(x) = \dfrac{x}{1-x^2}$.
>
> > [!success]- ✅ Solución
> >
> > Escribiendo la serie geométrica:
> >
> > $$\frac{x}{1-x^2} = x + x^3 + x^5 + \cdots$$
> >
> > El coeficiente de $x^n$ es $1$ cuando $n$ es impar, y $0$ cuando $n$ es par. Como $f^{(n)}(0) = n!\times(\text{coeficiente de } x^n)$:
> >
> > $$f^{(n)}(0) = \begin{cases} n! & \text{si } n \text{ es impar}, \\ 0 & \text{si } n \text{ es par}. \end{cases}$$
> >
> > **Respuesta:** por ejemplo $f'(0) = 1$, $f'''(0) = 6$ y $f^{(5)}(0) = 120$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo las notaciones de Leibniz, Lagrange y Newton para la derivada de orden $n$.
> - [ ] Calculo las derivadas sucesivas de polinomios, exponenciales y funciones trigonométricas.
> - [ ] Reconozco que un polinomio de grado $n$ tiene derivada cero para órdenes mayores que $n$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico la regla de Leibniz para calcular la derivada de orden $n$ de un producto.
> - [ ] Uso la linealidad para derivar sumas de funciones sin complicar el cálculo.
> - [ ] Calculo la segunda derivada de una composición con la fórmula de la cadena.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Interpreto $f''$ como curvatura, $f'''$ como cambio de curvatura y sé cuándo hace falta la tercera.
> - [ ] Uso las derivadas de orden superior como coeficientes de una serie de Taylor.
> - [ ] Verifico los patrones calculando varios casos antes de generalizar.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: derivadas de orden superior y series de Taylor.
> - R. Larson, *Cálculo* (Cengage), cap. 3: derivadas sucesivas y concavidad.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 3: la derivada $n$-ésima como operador.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] — las reglas que aquí se encadenan.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la base de la composición en órdenes superiores.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — la lectura geométrica de $f''$ y $f'''$.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es la derivada de orden $n$?::La que se obtiene derivando $n$ veces: $f^{(n)}(x) = \frac{d}{dx}\left(\frac{d^{n-1}}{dx^{n-1}}f(x)\right)$.
> - ¿Qué es la regla de Leibniz?::$\frac{d^n}{dx^n}(fg) = \sum_{k=0}^n \binom{n}{k} f^{(k)} g^{(n-k)}$: la generalización de la regla del producto con la estructura del binomio de Newton.
> - ¿Cuál es la n-ésima derivada de $e^{ax}$?::$a^n e^{ax}$, y de $\operatorname{sen}(ax)$: $a^n\operatorname{sen}\left(ax + \frac{n\pi}{2}\right)$, con periodo 4.
> - ¿Qué da $\frac{d^n}{dx^n}[\ln x]$?::$\frac{(-1)^{n+1}(n-1)!}{x^n}$ para $n \ge 1$: signo alternado y factorial en el numerador.
> - ¿Por qué $f''(x) = 0$ no basta para afirmar que hay inflexión?::Porque es solo condición necesaria: hay que comprobar que la segunda derivada **cambia de signo** al pasar por el punto (y ahí puede hacer falta $f'''$).

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] — las reglas que se encadenan para derivar varias veces.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — el origen del $[g'(x)]^2$ en la segunda derivada de una composición.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/02 - Derivadas de Funciones Inversas|02 - Derivadas de Funciones Inversas]] — derivar de forma implícita para despejar la inversa.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas|03 - Derivadas Paramétricas]] — la segunda derivada cuando la curva está parametrizada.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — la concavidad y los puntos de inflexión que mide $f''$.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/01 - Tasas de Cambio|01 - Tasas de Cambio]] — la lectura de $f'$ como velocidad y de $f''$ como aceleración.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 a 3: son derivación directa y debe salirte sin pensar.
> - Después salta al 4 (Leibniz) y al 5 (logaritmo compuesto), que son los dos que aparecen en parciales.
> - Cuando controles esos, usa el ejercicio 7 (serie de Taylor) como puente hacia [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|Antiderivadas]], donde las derivadas de orden superior se combinan al revés.
> - En cada ejercicio, escribe **qué información da cada orden** (pendiente, curvatura, cambio de curvatura): es lo que se pregunta en la parte conceptual.

---

**Tags:** #MATG1045 #unidad4 #derivadas-de-orden-superior #segunda-derivada #concavidad #regla-leibniz #series-taylor #puntos-inflexion #analisis-funciones

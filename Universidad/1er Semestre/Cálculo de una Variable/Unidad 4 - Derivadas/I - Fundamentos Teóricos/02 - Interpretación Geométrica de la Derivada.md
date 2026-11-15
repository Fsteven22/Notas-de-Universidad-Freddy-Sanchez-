---
dg-publish: true
tags: [MATG1045, unidad4, interpretacion-geometrica, tangente, secante, normal, pendiente, signos-derivada, mnemotecnia]
---

# 📐 Interpretación Geométrica de la Derivada

## 🎯 Introducción

> [!info] 💡 Concepto fundamental
>
> La **interpretación geométrica de la derivada** establece que la derivada de una función en un punto representa la **pendiente de la recta tangente** a la curva en ese punto. Esta conexión entre el álgebra y la geometría es uno de los conceptos más fundamentales del cálculo diferencial: convierte un límite abstracto en una pendiente que puedes dibujar.
>
> **Por qué importa:**
>
> - Conecta el **concepto abstracto** de límite con la **geometría visual**.
> - Permite **visualizar** las tasas de cambio instantáneas.
> - Es fundamental para **optimización** y **análisis gráfico**.
> - Proporciona **intuición geométrica** para resolver problemas.
> - Es la base para entender **máximos**, **mínimos** y **puntos de inflexión**.
>
> **Ejemplo:** saber que $f'(3) = 6$ en $f(x) = x^2$ no es solo un número: es la pendiente exacta con la que la curva sube en ese punto.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Secante, tangente y derivada
>
> **Pendiente de la recta secante** entre $(x, f(x))$ y $(x+h, f(x+h))$:
>
> $$m_{sec} = \frac{f(x+h) - f(x)}{h} \qquad \text{(tasa de cambio promedio)}.$$
>
> **Pendiente de la recta tangente** en $(x, f(x))$:
>
> $$m_{tan} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = f'(x) \qquad \text{(tasa de cambio instantánea)}.$$
>
> **Recta tangente** en el punto de tangencia $(a, f(a))$:
>
> $$y - f(a) = f'(a)(x - a) \qquad \text{(la mejor aproximación lineal en ese punto)}.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Interpretación_Geométrica_de_la_Derivada_01.svg]]
>
> **Se lee así:** el diagrama arranca con una función y dos puntos sobre la curva, de los que sale una recta secante con su pendiente promedio. En paralelo, otra rama muestra cómo se acercan los puntos hasta que el incremento se anula, y de ahí aparecen la recta tangente, su pendiente instantánea y finalmente la derivada.
>
> **Por qué importa:** fíjate en que la tangente toca en un solo punto y la secante une dos: ahí está la diferencia entre cambio promedio y cambio instantáneo. Te evita el error de interpretar $f'(x)$ como el promedio entre dos puntos cualesquiera.
>
> **Ejemplo:** con $f(x) = x^2$ en $x = 3$, la pendiente de la tangente es $f'(3) = 6$, mientras que la secante entre dos puntos alejados tiene otra pendiente.

> [!note] 📋 Definición — Recta normal
>
> La **recta normal** es la perpendicular a la recta tangente en el punto de tangencia. Su pendiente es el **recíproco negativo** de la derivada:
>
> $$m_n = -\frac{1}{f'(a)}, \qquad \text{válida cuando } f'(a) \neq 0.$$
>
> La condición de perpendicularidad es $m_1 \cdot m_2 = -1$: en efecto, $f'(a) \cdot \left(-\frac{1}{f'(a)}\right) = -1$. Si $f'(a) = 0$ (tangente horizontal), la normal es la vertical $x = a$.
>
> **Ecuación:** $y - f(a) = -\frac{1}{f'(a)}(x - a)$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Interpretación_Geométrica_de_la_Derivada_06.svg]]
>
> **Se lee así:** el esquema parte del punto de tangencia y de la pendiente $f'(a)$, y pasa por un rombo que pregunta si esa pendiente es cero. Si lo es, la tangente es horizontal y la normal queda vertical ($x = a$); si no, la normal toma el recíproco negativo $-1/f'(a)$ y se escribe en forma punto-pendiente. Las dos ramas terminan en la misma casilla: tangente y normal son perpendiculares.
>
> **Por qué importa:** el rombo recuerda el caso especial que se olvida: cuando la tangente es horizontal la fórmula del recíproco se indetermina, y ahí la normal es simplemente la vertical. Te evita dividir entre cero en un examen.
> **Por qué importa:** aparece en problemas de física (normal a una trayectoria, fuerzas) y en geometría analítica. El error típico es usar $+\frac{1}{f'(a)}$ y olvidar el signo menos.
>
> **Ejemplo:** para $f(x) = x^2$ en $x = 1$ vale $f'(1) = 2$, así que $m_n = -\tfrac{1}{2}$ y la normal es $y - 1 = -\tfrac{1}{2}(x-1)$, es decir $y = -\tfrac{1}{2}x + \tfrac{3}{2}$.

> [!warning] ⚠️ Elementos clave para recordar
>
> - **Secante:** une dos puntos de la curva (promedio).
> - **Tangente:** toca la curva en un solo punto (instantáneo).
> - **Derivada:** pendiente de la tangente = límite de pendientes de secantes.
> - **Punto de tangencia:** donde la recta tangente toca la curva.
>
> **Por qué importa:** estas cuatro palabras son las que distingue un examen de interpretación. "La tangente une dos puntos" es, por sí sola, una respuesta incorrecta.

---

## 📐 De la secante a la tangente

> [!info] 🔍 El proceso de aproximación
>
> 1. **Recta secante:** dados $P(x, f(x))$ y $Q(x+h, f(x+h))$, la pendiente es $m_{sec} = \frac{\Delta y}{\Delta x} = \frac{f(x+h)-f(x)}{h}$: cambio promedio en $[x, x+h]$.
> 2. **Reducir la distancia:** hacer $h$ cada vez más pequeño, $h \to 0$; el punto $Q$ se acerca a $P$ y la secante se aproxima a la tangente.
> 3. **Límite (tangente):** $m_{tan} = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h} = f'(x)$; la secante converge a la tangente y obtenemos la pendiente instantánea.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Interpretación_Geométrica_de_la_Derivada_02.svg]]
>
> **Se lee así:** muestra dos secuencias encadenadas que avanzan a la vez: por un lado, secantes con incremento grande, mediano y pequeño que terminan en la tangente cuando el incremento tiende a cero; por el otro, la pendiente pasa de aproximada a mejor y luego a excelente aproximación hasta volverse la pendiente exacta. Es la idea de *zoom infinito* sobre un punto.
>
> **Por qué importa:** te da la intuición de por qué la derivada es un límite y no un simple cociente evaluado en un $h$ cualquiera. También justifica el método numérico de diferencias finitas que usas para verificar tus resultados.
>
> **Ejemplo:** con $f(x) = x^2$ en $x = 2$, los valores $h = 1$, $0.1$, $0.01$ y $0.001$ dan pendientes $5$, $4.1$, $4.01$ y $4.001$, cada vez más cerca de $4$.
>
> **Tabla de aproximación:**
>
> | $h$ | $\frac{f(2+h)-f(2)}{h}$ | Interpretación |
> |---|---|---|
> | $1$ | $5$ | Aproximación gruesa |
> | $0.1$ | $4.1$ | Aproximación mejor |
> | $0.01$ | $4.01$ | Aproximación excelente |
> | $0.001$ | $4.001$ | Prácticamente la pendiente exacta: $4$ |

---

## 📏 Ecuación de la recta tangente

> [!tip] 📋 Formas punto-pendiente y casos especiales
>
> **Forma general:** $y - y_1 = m(x - x_1)$ con $(x_1, y_1) = (a, f(a))$ y $m = f'(a)$:
>
> $$y - f(a) = f'(a)(x - a), \qquad y = f'(a)(x - a) + f(a).$$
>
> **Casos especiales:**
>
> - **Tangente horizontal** ($f'(a) = 0$): $y = f(a)$; indica posible máximo o mínimo local.
> - **Tangente vertical** ($f'(a)$ no existe o es infinita): $x = a$; ocurre en cúspides o puntos angulosos.
>
> **Por qué importa:** el caso horizontal es el que conecta con la optimización de la Unidad 5: ahí es donde se buscan los puntos críticos.
>
> **Ejemplo:** la tangente a $y = \sin x$ en $x = \pi/4$ tiene pendiente $f'(\pi/4) = \frac{\sqrt{2}}{2}$ y pasa por $(\pi/4, \frac{\sqrt{2}}{2})$.

---

## 📊 Lectura de la gráfica: los signos de $f'(x)$

> [!info] 📈 Relación entre $f(x)$ y $f'(x)$
>
> - **$f'(x) > 0$:** la función es **creciente**, las tangentes tienen pendiente positiva, la gráfica sube de izquierda a derecha.
> - **$f'(x) < 0$:** la función es **decreciente**, las tangentes tienen pendiente negativa, la gráfica baja.
> - **$f'(x) = 0$:** tangentes **horizontales**; posibles máximos o mínimos locales: son los puntos críticos.
>
> **Tipos de tangente según la magnitud:**
>
> - **Horizontal:** pendiente $0$; función con máximo o mínimo local.
> - **Pendiente pronunciada:** $|f'(x)|$ grande; la función cambia rápido y la curva es empinada.
> - **Pendiente suave:** $|f'(x)|$ pequeño; la función cambia lento y la curva es plana.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Interpretación_Geométrica_de_la_Derivada_03.svg]]
>
> **Se lee así:** parte de la gráfica de la función y entra a un rombo que ordena las pendientes en tres casos: positivo, negativo o nulo. Cada caso lleva a una caja con la forma de la tangente correspondiente, y solo la rama de la tangente horizontal continúa hacia los máximos y mínimos locales.
>
> **Por qué importa:** es la traducción de los signos de la derivada a lo que ves en el dibujo. Evita el error de leer $f'(x) > 0$ como si la función fuera positiva: creciente y positiva son cosas distintas.
>
> **Ejemplo:** para $f(x) = x^3 - 2x + 1$ en $x = 1$ la derivada vale $1 > 0$, así que la función es creciente ahí y su tangente tiene pendiente positiva.

---

## 🔍 Rectas normales

> [!example] 🧪 Ejemplo resuelto: tangente y normal
>
> Para $f(x) = x^2$ en $x = 1$:
>
> - $f'(x) = 2x$, así que $f'(1) = 2$ (pendiente tangente).
> - Punto: $(1, 1)$.
> - **Tangente:** $y - 1 = 2(x - 1)$, es decir $y = 2x - 1$.
> - **Normal:** pendiente $m_n = -\frac{1}{2}$, así que $y - 1 = -\frac{1}{2}(x - 1)$, es decir $y = -\frac{1}{2}x + \frac{3}{2}$.
>
> **Por qué importa:** las dos rectas comparten el punto de tangencia y sus pendientes multiplican $-1$. Comprobar esa multiplicación es la verificación rápida de que la normal está bien.

---

## 🎭 Interpretación física

> [!info] ⚡ De posición a aceleración, y otras tasas
>
> **Cinemática:**
>
> - Si $s(t)$ es la posición, $v(t) = s'(t)$ es la velocidad instantánea: pendiente de la tangente a la curva posición-tiempo.
> - Si $v(t)$ es la velocidad, $a(t) = v'(t) = s''(t)$ es la aceleración: pendiente de la tangente a la curva velocidad-tiempo.
>
> **Ejemplo:** con $s(t) = 5t^2 + 2t$ se obtiene $v(t) = 10t + 2$, y en $t = 3$ el objeto se mueve a $32$ m/s.
>
> **Otras tasas de cambio:**
>
> - **Temperatura:** $T'(t)$ es la rapidez de calentamiento o enfriamiento; tangente empinada = cambio térmico rápido, tangente horizontal = temperatura estable.
> - **Población:** $P'(t)$ es la tasa de crecimiento; $P'(t) > 0$ crece, $P'(t) < 0$ disminuye, $P'(t) = 0$ estable.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Interpretación_Geométrica_de_la_Derivada_04.svg]]
>
> **Se lee así:** el esquema parte de una función física y pasa por un rombo que pregunta de qué fenómeno se trata. De ahí salen tres ramas paralelas, cada una con su variable propia (posición, temperatura o población), la derivada asociada y una interpretación final expresada como rapidez de cambio.
>
> **Por qué importa:** te muestra que la derivada siempre habla de rapidez de cambio y que solo cambia el nombre según la variable. Para leer un modelo físico o económico: primero identificas la variable, luego la tasa que te piden.
>
> **Ejemplo:** con la posición $s(t) = 5t^2 + 2t$, la derivada $v(t) = 10t + 2$ indica que en $t = 3$ el objeto se mueve a $32$ m/s.

---

## 🌍 Aplicaciones en física, economía e ingeniería

> [!note] 🌐 Dónde aparece la tangente fuera del aula
>
> - **Física (cinemática):** la tangente a la curva $s(t)$ indica qué tan rápido cambia la posición en cada instante.
> - **Economía:** el **costo marginal** $C'(x)$ es la pendiente de la curva de costo y representa el costo de producir una unidad adicional; el **beneficio máximo** ocurre donde $B'(x) = 0$ (tangente horizontal).
> - **Ingeniería:** carreteras con tangentes suaves para cambios graduales de dirección, análisis de pendientes en puentes para estabilidad y tangentes a perfiles alares para el flujo aerodinámico.
>
> **Por qué importa:** en los tres casos el procedimiento es el mismo: derivar, evaluar en el punto y leer la pendiente. Cambia el contexto, no el cálculo.
>
> **Ejemplo:** maximizar $B(x)$ es hallar donde su tangente es horizontal: $B'(x) = 0$.

---

## ⚠️ Errores comunes y cómo evitarlos

> [!warning] 🚨 Los cinco errores frecuentes
>
> 1. **Confundir secante con tangente:** incorrecto "la tangente une dos puntos"; correcto "la secante une dos, la tangente toca en uno".
> 2. **Ecuación mal escrita:** incorrecto $y = f'(a)\cdot x + f(a)$; correcto $y - f(a) = f'(a)(x - a)$.
> 3. **Olvidar evaluar la derivada en el punto:** se usa $f'(x)$ cuando hay que usar $f'(a)$, el valor en el punto pedido.
> 4. **Pendiente de la normal:** incorrecto $\frac{1}{f'(a)}$; correcto $-\frac{1}{f'(a)}$, recíproco negativo.
> 5. **Signo de la derivada:** incorrecto "$f'(x) > 0$ significa función positiva"; correcto "$f'(x) > 0$ significa función creciente".
>
> **Por qué importa:** los cinco son errores de lectura, no de cálculo; por eso no los detectas repasando la aritmética, sino releyendo el enunciado.

> [!tip] 💡 Regla de los tres pasos y verificación
>
> 1. **PUNTO:** encuentra $(a, f(a))$.
> 2. **PENDIENTE:** calcula $f'(a)$.
> 3. **ECUACIÓN:** escribe $y - f(a) = f'(a)(x - a)$.
> 4. **VERIFICA:** sustituye el punto en tu ecuación; si no cumple, hay un error.
>
> **Mnemotecnias:**
>
> - **"TOCA vs UNE":** la **T**angente **T**oca un punto, la **S**ecante **S**epara dos.
> - **"PUMA"** para la tangente: **P**unto de tangencia, **U**sa la derivada $f'(a)$, **M**étodo punto-pendiente, **A**plica $y - f(a) = f'(a)(x-a)$.
> - **"SUBE BAJA PLANO":** $f' > 0$ sube, $f' < 0$ baja, $f' = 0$ plano.
> - **"DALE LA VUELTA"** para la normal: derivada, recíproco negativo $-\frac{1}{f'(a)}$, perpendicular, ecuación punto-pendiente.
>
> **Método visual del "zoom geométrico":** dibuja la función con dos puntos distantes (secante), acerca gradualmente los puntos, observa cómo la secante se convierte en tangente y visualiza el límite como un zoom infinito.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Encuentra la ecuación de la recta tangente a $f(x) = x^2$ en $x = 3$.
>
> > [!success]- ✅ Solución
> >
> > 1. Derivada: $f'(x) = 2x$.
> > 2. Pendiente en el punto: $f'(3) = 6$.
> > 3. Punto de tangencia: $f(3) = 9$, es decir $(3, 9)$.
> > 4. Ecuación: $y - 9 = 6(x - 3)$, que simplifica a $y = 6x - 9$.
> >
> > **Verificación:** $(3, 9)$ cumple $9 = 6(3) - 9 = 9$. ✔

> [!example] 📋 Planteamiento
>
> Encuentra la recta tangente a $f(x) = \sin x$ en $x = \frac{\pi}{4}$.
>
> > [!success]- ✅ Solución
> >
> > Derivada: $f'(x) = \cos x$, y $f'(\pi/4) = \frac{\sqrt{2}}{2}$.
> >
> > Punto: $f(\pi/4) = \sin(\pi/4) = \frac{\sqrt{2}}{2}$, es decir $(\frac{\pi}{4}, \frac{\sqrt{2}}{2})$.
> >
> > Ecuación: $y - \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{2}\left(x - \frac{\pi}{4}\right)$, es decir $y = \frac{\sqrt{2}}{2}x - \frac{\sqrt{2}\pi}{8} + \frac{\sqrt{2}}{2}$.

> [!example] 📋 Planteamiento
>
> Encuentra la recta tangente a $f(x) = \frac{1}{x}$ en $x = 2$.
>
> > [!success]- ✅ Solución
> >
> > Derivada: $f'(x) = -\frac{1}{x^2}$, y $f'(2) = -\frac{1}{4}$.
> >
> > Punto: $f(2) = \frac{1}{2}$, es decir $(2, \frac{1}{2})$.
> >
> > Ecuación: $y - \frac{1}{2} = -\frac{1}{4}(x - 2)$, que simplifica a $y = -\frac{1}{4}x + 1$.
> >
> > **Lectura:** la pendiente negativa indica que la hipérbola baja en ese punto.

> [!example] 📋 Planteamiento
>
> Para $f(x) = x^2$ en $x = 1$, calcula la recta normal y comprueba la perpendicularidad.
>
> > [!success]- ✅ Solución
> >
> > $f'(1) = 2$ y el punto es $(1, 1)$.
> >
> > Tangente: $y - 1 = 2(x - 1)$, es decir $y = 2x - 1$.
> >
> > Normal: pendiente $m_n = -\frac{1}{f'(1)} = -\frac{1}{2}$, así que $y - 1 = -\frac{1}{2}(x - 1)$, es decir $y = -\frac{1}{2}x + \frac{3}{2}$.
> >
> > **Comprobación:** $2 \cdot \left(-\frac{1}{2}\right) = -1$: las rectas son perpendiculares. ✔

> [!example] 📋 Planteamiento
>
> Encuentra la recta tangente a $f(x) = x^3 - 3x$ en $x = 1$ e interpreta el resultado.
>
> > [!success]- ✅ Solución
> >
> > Derivada: $f'(x) = 3x^2 - 3$.
> >
> > En $x = 1$: $f'(1) = 3 - 3 = 0$.
> >
> > Punto: $f(1) = 1 - 3 = -2$, es decir $(1, -2)$.
> >
> > Ecuación: $y - (-2) = 0 \cdot (x - 1)$, es decir $y = -2$, una horizontal.
> >
> > **Interpretación:** tangente horizontal = punto crítico; en efecto, $x = 1$ es un mínimo local de la función (podría serlo; el análisis completo está en la nota de monotonía).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo la recta secante de la recta tangente y explico qué mide cada una.
> - [ ] Escribo la ecuación de la tangente con el método de tres pasos (punto, pendiente, ecuación).
> - [ ] Interpreto el signo de $f'(x)$ como crecimiento o decrecimiento de la gráfica.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Construyo la tangente a una función polinómica, trigonométrica o racional en un punto dado.
> - [ ] Calculo la recta normal y verifico la perpendicularidad de ambas rectas.
> - [ ] Reconozco las tangentes horizontales como puntos críticos candidatos a extremos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Explico la derivada como límite de pendientes de secantes usando el argumento del zoom infinito.
> - [ ] Traduzco un modelo físico o económico (posición, costo, población) en una lectura de pendiente.
> - [ ] Detecto y corrijo los cinco errores comunes de la sección antes de entregar un ejercicio.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2: la derivada y sus interpretaciones geométricas.
> - R. Larson, *Cálculo* (Cengage), cap. 2: tangentes y velocidad instantánea.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 2: la derivada como pendiente.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la definición de la que nace esta interpretación.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — cuándo la tangente existe.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/03 - Aproximaciones Lineales y Diferenciales|03 - Aproximaciones Lineales y Diferenciales]] — la tangente usada para aproximar.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué diferencia a la secante de la tangente?::La secante une dos puntos de la curva y mide cambio promedio; la tangente toca en un solo punto y mide cambio instantáneo, igual a $f'(a)$.
> - ¿Cómo se escribe la recta tangente en $(a, f(a))$?::$y - f(a) = f'(a)(x - a)$; si $f'(a) = 0$ la tangente es la horizontal $y = f(a)$.
> - ¿Cuál es la pendiente de la recta normal?::$-\frac{1}{f'(a)}$, el recíproco negativo; el producto con $f'(a)$ debe dar $-1$.
> - ¿Qué significa $f'(x) > 0$ en la gráfica?::Que la función es creciente y la tangente sube; no significa que la función sea positiva.
> - ¿Qué punto es candidato a extremo según la geometría?::Donde la tangente es horizontal, $f'(x) = 0$, más los puntos donde la derivada no existe.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — el límite que define la pendiente de la tangente.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la definición algebraica correspondiente.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — cuándo existe la tangente.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]] — concavidad y curvatura leídas en la gráfica.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — crecimiento y máximos a partir de los signos de $f'$.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — tangentes horizontales en problemas de máximo y mínimo.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — tasas relacionadas.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el proceso inverso: de la pendiente al área.
>
> **Mapa de la interpretación:**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Interpretación_Geométrica_de_la_Derivada_05.svg]]
>
> **Se lee así:** es un mapa mental cuyo nodo central abre cuatro ramas: los conceptos base de donde partes, los elementos clave con los que trabajas (tangente, secante, normal), las áreas donde se aplica y los temas de cálculo que se conectan con él. Cada rama tiene después sus propias hojas.
>
> **Por qué importa:** te sirve como mapa de la unidad: lo que aprendiste de geometría se reutiliza en optimización, integrales y ecuaciones diferenciales. Con esta vista sabes qué repasar cuando un tema se te resiste.
>
> **Ejemplo:** al pedir la normal a $f(x) = x^2$ en $x = 1$, tomas la hoja de elementos clave y usas el recíproco negativo $m_n = -\frac{1}{2}$.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica el método de tres pasos (punto, pendiente, ecuación) con las cinco funciones de los ejercicios.
> - Después conecta con [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|Análisis Completo de Funciones]] para estudiar la función completa a partir de los signos de $f'$.
> - Las tangentes horizontales que aparecen aquí son la puerta a [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|Problemas de Optimización]].
> - Si una tangente no existe, revisa [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|Derivabilidad y Continuidad]] antes de concluir.

---

**Tags:** #MATG1045 #unidad4 #interpretacion-geometrica #tangente #secante #normal #pendiente #signos-derivada #mnemotecnia

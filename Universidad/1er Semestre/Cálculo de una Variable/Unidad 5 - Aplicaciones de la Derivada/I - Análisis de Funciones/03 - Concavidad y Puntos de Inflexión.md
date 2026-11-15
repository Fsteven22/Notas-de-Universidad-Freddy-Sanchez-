---
dg-publish: true
tags: [MATG1045, unidad5, concavidad, puntos-inflexion, segunda-derivada, intervalos-concavidad, falsos-inflexiones, graficacion]
---

# 📈 Concavidad y Puntos de Inflexión

## 🎯 Introducción

> [!info] 💡 Qué añade la segunda derivada al análisis
>
> La **concavidad** describe la curvatura de una función en un intervalo: si la gráfica se "curva hacia arriba" (forma de U) o "hacia abajo" (forma de ∩). Los **puntos de inflexión** son los lugares donde esa curvatura cambia de dirección. Juntos completan el estudio que la primera derivada dejó a medias.
>
> **Por qué importa:** con $f'$ sabes si la curva sube o baja; con $f''$ sabes **cómo** lo hace. Un máximo y un mínimo pueden estar conectados por una curva cóncava o cóncava hacia abajo, y esa diferencia decide el bosquejo final.
>
> **Ejemplo:** en $f(x) = x^3 - 6x^2 + 9x + 1$ la segunda derivada $f''(x) = 6(x-2)$ revela una inflexión en $x = 2$: ahí la curva deja de mirar hacia abajo y empieza a mirar hacia arriba.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Intervalos de concavidad
>
> Los **intervalos de concavidad** son los rangos de valores de $x$ donde la función mantiene el mismo tipo de curvatura:
>
> - **Cóncava hacia arriba (forma de U):** $f''(x) > 0$; la recta secante queda por **encima** de la curva.
> - **Cóncava hacia abajo (forma de ∩):** $f''(x) < 0$; la recta secante queda por **debajo** de la curva.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Concavidad_y_Puntos_de_Inflexión_01.svg]]
>
> **Se lee así:** es una cadena de seis rectángulos, sin decisiones, que empieza en el dominio de la función y termina en la clasificación de la concavidad. En medio aparecen el paso de anular la segunda derivada, la lista de puntos críticos de curvatura, el corte del dominio en intervalos y la evaluación del signo en cada uno. Es la receta que produce la tabla de signos.
>
> **Por qué importa:** este orden evita el error típico de dar por hecho un punto de inflexión solo porque $f''(x) = 0$. Al evaluar el signo en cada intervalo, la concavidad queda **demostrada** y no supuesta.
>
> **Ejemplo:** para $f(x) = x^3 - 6x^2 + 9x + 1$, con $f''(x) = 6(x-2)$, el diagrama lleva a la tabla donde la función es cóncava hacia abajo para $x < 2$ y hacia arriba para $x > 2$.

> [!note] 📋 Definición — Punto de inflexión
>
> Un **punto de inflexión** es un punto de la curva donde la función **cambia su concavidad**: de cóncava hacia arriba a cóncava hacia abajo, o viceversa. En ese punto la tangente cruza la curva y la velocidad de cambio de la pendiente se anula.
>
> **Condiciones:**
>
> - **Necesaria:** $f''(x_0) = 0$ o $f''(x_0)$ no existe.
> - **Suficiente:** la segunda derivada **cambia de signo** al pasar por $x_0$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Concavidad_y_Puntos_de_Inflexión_02.svg]]
>
> **Se lee así:** el diagrama tiene un solo rombo de decisión y el resto son rectángulos encadenados. Partiendo de anular la segunda derivada, se listan los candidatos, se arma la tabla de signos y se llega al rombo: si hay cambio de signo se sigue hacia el punto de inflexión y se calculan el valor de la función y las coordenadas; si no, se sale por la rama que descarta el candidato.
>
> **Por qué importa:** la rama de descarte es lo que separa un punto de inflexión real de un falso inflexión como el $x = 0$ de $f(x) = x^4$. Sin verificar el cambio de signo, la gráfica sale con la curvatura mal dibujada.
>
> **Ejemplo:** en $f(x) = x^3$, $f''(x) = 6x$ cambia de signo en $0$, así que el diagrama confirma el punto de inflexión $(0, 0)$.

---

## 🧮 Criterio de la segunda derivada

> [!warning] ✅ La regla principal
>
> Para determinar la concavidad de $f(x)$ en un intervalo:
>
> - Si $f''(x) > 0$ → la función es **cóncava hacia arriba**.
> - Si $f''(x) < 0$ → la función es **cóncava hacia abajo**.
> - Si $f''(x) = 0$ → **posible** punto de inflexión (hay que verificar el cambio de signo).
>
> **Interpretación geométrica:** la segunda derivada mide la **tasa de cambio de la pendiente**: si $f'' > 0$ la pendiente está aumentando (la curva gira hacia arriba); si $f'' < 0$ está disminuyendo (gira hacia abajo); si $f'' = 0$ la pendiente se mantiene momentáneamente.
>
> **Por qué importa:** $f''$ no te dice si la función sube o baja, sino si la pendiente crece o decrece. Confundir ambas lecturas es el error conceptual más frecuente de esta nota.

> [!tip] 🔗 Qué informa cada derivada
>
> | Derivada | Información | Interpretación |
> |---|---|---|
> | $f'(x)$ | Pendiente | Crecimiento y decrecimiento, extremos |
> | $f''(x)$ | Curvatura | Concavidad e inflexiones |
> | $f'''(x)$ | Cambio de curvatura | Validación de inflexiones difíciles |
>
> **Por qué importa:** el análisis completo combina las dos primeras: $f'$ da la forma general de subidas y bajadas, $f''$ decide cómo se curvan esos tramos.
>
> **Ejemplo:** en $f(x) = x^3 - 6x^2 + 9x + 1$: $f'(x) = 3x^2 - 12x + 9$ aporta los puntos críticos, y $f''(x) = 6(x-2)$ aporta la inflexión en $x = 2$.

---

## 🎯 Puntos de inflexión: algoritmo

> [!tip] 📋 Proceso en cinco pasos
>
> 1. **Calcular** $f''(x)$.
> 2. **Resolver** $f''(x) = 0$.
> 3. **Identificar** los puntos donde $f''(x)$ no existe (pero $f$ sí está definida).
> 4. **Verificar** el cambio de signo con una tabla de signos.
> 5. **Calcular** $f(x)$ en los candidatos confirmados y escribir las coordenadas.
>
> **Por qué importa:** el paso 4 es el filtro: sin él, cualquier $f''(x_0) = 0$ parecería inflexión y los falsos positivos (como $x^4$ en $0$) se cuelan en la gráfica.
>
> **Ejemplo:** para $f(x) = x^4$: $f''(x) = 12x^2$ se anula en $x = 0$, pero el signo es positivo en ambos lados, así que el paso 4 lo descarta: **no** hay inflexión.

> [!example] 📐 Interpretación geométrica en el punto de inflexión
>
> - La **tangente cruza** la curva (no la toca por un solo lado).
> - La **curvatura cambia** de dirección.
> - La **velocidad de cambio** de la pendiente es cero en ese punto.
>
> **Por qué importa:** "la tangente cruza la curva" es la imagen que te deja reconocer un inflexión en una gráfica a simple vista, antes de calcular nada.

---

## 📚 Ejemplos y gráficas

> [!example] 📈 Ejemplo 1: $f(x) = x^3$ (sí hay inflexión)
>
> - $f'(x) = 3x^2$, $f''(x) = 6x$.
> - $f''(x) = 0$ → $x = 0$.
> - Cambio de signo: negativo para $x < 0$, positivo para $x > 0$.
> - **Punto de inflexión: $(0, 0)$.**

> [!example] 📉 Ejemplo 2: $f(x) = x^4$ (falso inflexión)
>
> - $f'(x) = 4x^3$, $f''(x) = 12x^2$.
> - $f''(x) = 0$ → $x = 0$.
> - **No hay cambio de signo** ($12x^2 \geq 0$ siempre).
> - **No es punto de inflexión:** solo un candidato descartado.
>
> **Lección:** $f''(x_0) = 0$ es condición necesaria, nunca suficiente.

> [!example] 📊 Ejemplo 3: análisis combinado de $f(x) = x^3 - 6x^2 + 9x + 1$
>
> **Primera derivada:** $f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3)$, con puntos críticos $x = 1$ y $x = 3$.
>
> **Segunda derivada:** $f''(x) = 6x - 12 = 6(x-2)$, con candidato $x = 2$.
>
> **Tabla de concavidad:**
>
> | Intervalo | $x < 2$ | $x = 2$ | $x > 2$ |
> |---|---|---|---|
> | $f''(x)$ | $-$ | $0$ | $+$ |
> | Concavidad | Hacia abajo | Inflexión | Hacia arriba |
>
> **Resultado:** cóncava hacia abajo en $(-\infty, 2)$, hacia arriba en $(2, +\infty)$, inflexión en $x = 2$ con $f(2) = 8 - 24 + 18 + 1 = 3$, es decir el punto $(2, 3)$.

> [!info] 🖼️ Pasos para construir la gráfica
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Concavidad_y_Puntos_de_Inflexión_03.svg]]
>
> **Se lee así:** es una cadena lineal de rectángulos que va de la función a la gráfica completa, sin rombos ni ramas alternativas. El orden es revelador: primero se calcula la primera derivada, luego la segunda, y solo después se localizan puntos críticos y puntos de inflexión, seguidos de los intervalos de monotonía y de concavidad. Al final se evalúan los puntos especiales y se arma la gráfica completa.
>
> **Por qué importa:** fíjate en que la segunda derivada **no se usa sola**: aquí se combina con la primera para que cada tramo de la gráfica tenga una razón. Esto evita dejar huecos en el bosquejo y asegura que la curvatura quede bien dibujada.
>
> **Ejemplo:** con $f(x) = x^3 - 6x^2 + 9x + 1$ aplicas los pasos en cadena: $f'(x) = 3x^2 - 12x + 9$ para los puntos críticos y $f''(x) = 6(x-2)$ para la inflexión en $x = 2$.

> [!warning] 🎨 Casos especiales en las gráficas
>
> - **Inflexión con tangente horizontal:** $f'(x_0) = 0$ y $f''(x_0) = 0$ con cambio de signo: la tangente es horizontal **y** la curva cambia de concavidad (ejemplo: $x^3$ en $0$).
> - **Inflexión con tangente vertical:** $f'(x_0)$ no existe pero $f''$ cambia de signo; común en funciones con raíces fraccionarias.
> - **Falsos puntos de inflexión:** $f''(x_0) = 0$ sin cambio de signo, como $f(x) = x^4$ en $x = 0$.
>
> **Por qué importa:** estos tres casos son los que se confunden en los ejercicios de bosquejo: uno parece máximo pero es inflexión, otro parece inflexión y no lo es.

> [!tip] 🎓 Mnemotecnias
>
> - **"COCA-COLA":** **CO**ncavidad **CO**n **A**rriba → $f''(x) > 0$ (forma de copa **C**); **CO**ncavidad **L**leva **A**bajo → $f''(x) < 0$ (loma invertida).
> - **Regla de las manos:** mano derecha con los dedos hacia arriba = cóncava arriba; mano izquierda con los dedos hacia abajo = cóncava abajo; el punto donde cambias de mano es el inflexión.
> - **Tabla resumen:** $f'' > 0$ → U (ejemplo $x^2$); $f'' < 0$ → ∩ (ejemplo $-x^2$); $f'' = 0$ → transición posible (ejemplo $x^3$ en $0$).

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Determina la concavidad de $f(x) = x^3 - 6x^2 + 9x + 1$ y su punto de inflexión.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 3x^2 - 12x + 9$ y $f''(x) = 6x - 12 = 6(x-2)$.
> >
> > $f''(x) = 0$ da $x = 2$; $f''$ existe en todo $\mathbb{R}$.
> >
> > Signos: $f'' < 0$ para $x < 2$ y $f'' > 0$ para $x > 2$: hay cambio de confirmación.
> >
> > **Resultado:** cóncava hacia abajo en $(-\infty, 2)$, hacia arriba en $(2, +\infty)$; inflexión en $(2, f(2)) = (2, 3)$.

> [!example] 📋 Planteamiento
>
> ¿Es $x = 0$ un punto de inflexión de $f(x) = x^4$?
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 4x^3$ y $f''(x) = 12x^2$, que vale $0$ en $x = 0$.
> >
> > Pero $12x^2 \geq 0$ para **todos** los $x$: el signo no cambia al pasar por $0$.
> >
> > Como falla la condición suficiente, **no es punto de inflexión**; solo un candidato descartado. La curva es cóncava hacia arriba en ambos lados.

> [!example] 📋 Planteamiento
>
> Encuentra los puntos de inflexión de $f(x) = \frac{x}{x^2+1}$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = \frac{1-x^2}{(x^2+1)^2}$.
> >
> > Segunda derivada (regla del cociente sobre $f'$):
> >
> > $$f''(x) = \frac{-2x(x^2+1)^2 - (1-x^2)\cdot 2(x^2+1)(2x)}{(x^2+1)^4} = \frac{2x(x^2-3)}{(x^2+1)^3}.$$
> >
> > $f''(x) = 0$ da $x = 0$ y $x = \pm\sqrt{3}$ (los tres en el dominio).
> >
> > Signos de $2x(x^2-3)$: cambia en los tres ceros, así que hay inflexión en cada uno.
> >
> > **Resultado:** inflexiones en $(0, 0)$, $(\sqrt{3}, \sqrt{3}/4)$ y $(-\sqrt{3}, -\sqrt{3}/4)$.

> [!example] 📋 Planteamiento
>
> Clasifica la naturaleza del punto crítico $x = 1$ de $f(x) = x^4 - 4x^3 + 6x^2$ usando la segunda derivada.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 4x^3 - 12x^2 + 12x = 4x(x^2 - 3x + 3)$; el discriminante del paréntesis es $9 - 12 < 0$, así que el único punto crítico real es $x = 0$.
> >
> > Revisando: $f'(1) = 4 - 12 + 12 = 4 \neq 0$, así que $x = 1$ **no** es punto crítico de esta función.
> >
> > **Lección:** antes de clasificar con $f''$, verifica con $f'$ que el punto sea realmente crítico; el test de la segunda derivada solo aplica en críticos.

> [!example] 📋 Planteamiento
>
> Analiza concavidad e inflexiones de $f(x) = x^{2/3}$ y dibuja su comportamiento.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = \frac{2}{3}x^{-1/3}$ y $f''(x) = -\frac{2}{9}x^{-4/3} = -\frac{2}{9x^{4/3}}$.
> >
> > $f''$ nunca se anula y **no existe en $x = 0$**; $x^{4/3} > 0$ siempre, así que $f'' < 0$ en todo su dominio salvo en $0$.
> >
> > **Resultado:** cóncava hacia abajo en $(-\infty, 0) \cup (0, +\infty)$; no hay cambio de signo, así que **no hay punto de inflexión**, aunque en $x = 0$ la tangente es vertical (ya visto en la nota de monotonía: ahí hay mínimo local).

> [!example] 📋 Planteamiento
>
> Combina $f'$ y $f''$ para bosquejar $f(x) = x^3 - 3x$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$: críticos en $x = \pm 1$; máximo local en $x = -1$ ($f(-1) = 2$) y mínimo en $x = 1$ ($f(1) = -2$).
> >
> > $f''(x) = 6x$: cóncava abajo para $x < 0$, cóncava arriba para $x > 0$, inflexión en $(0, 0)$.
> >
> > **Bosquejo:** la curva baja desde arriba, gira en $(-1, 2)$, baja pasando por el origen donde cambia de curvatura, gira en $(1, -2)$ y sube. Los tres puntos marcados bastan para dibujarla con la forma correcta.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino concavidad hacia arriba y hacia abajo con su condición en $f''(x)$.
> - [ ] Distingo la condición necesaria ($f''(x_0) = 0$) de la suficiente (cambio de signo) en un punto de inflexión.
> - [ ] Construyo una tabla de signos de $f''(x)$ y clasifico los intervalos de concavidad.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Encuentro todos los puntos de inflexión de una función polinómica o racional aplicando el algoritmo de cinco pasos.
> - [ ] Descarto falsos inflexiones como $x = 0$ en $f(x) = x^4$ verificando el cambio de signo.
> - [ ] Combino la primera y la segunda derivada para bosquejar una función con la curvatura correcta.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Trato los puntos donde $f''$ no existe como candidatos de inflexión y verifico su cambio de signo.
> - [ ] Distingo inflexiones con tangente horizontal, con tangente vertical y falsos inflexiones.
> - [ ] Aplico el test de la segunda derivada a los puntos críticos y sé cuándo no es concluyente.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: concavidad, puntos de inflexión y test de la segunda derivada.
> - R. Larson, *Cálculo* (Cengage), cap. 4: curvatura y análisis gráfico combinado.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 6: propiedades de las derivadas superiores.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — el checklist completo de graficación.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — la primera derivada, que esta nota complementa.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — extremos clasificados con la segunda derivada.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice el criterio de la segunda derivada?::Si $f''(x) > 0$ la función es cóncava hacia arriba (forma de U); si $f''(x) < 0$ es cóncava hacia abajo (forma de ∩).
> - ¿Qué diferencia hay entre condición necesaria y suficiente en una inflexión?::Necesaria: $f''(x_0) = 0$ o no existe. Suficiente: que $f''$ **cambie de signo** al pasar por $x_0$.
> - ¿Por qué $x = 0$ no es inflexión de $f(x) = x^4$?::Porque $f''(x) = 12x^2$ se anula ahí pero es positiva a ambos lados: no hay cambio de signo.
> - ¿Qué mide $f''(x)$ geométricamente?::La tasa de cambio de la pendiente: si es positiva la pendiente aumenta (curva gira hacia arriba), si es negativa disminuye.
> - ¿Qué tres casos especiales puede tener una inflexión?::Tangente horizontal ($f' = 0$), tangente vertical ($f'$ no existe) y falso inflexión ($f'' = 0$ sin cambio de signo).

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — el checklist de graficación donde esta nota es el bloque de concavidad.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — la primera derivada y los extremos.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — la segunda derivada como test de máximo y mínimo.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]] — la teoría de $f^{(n)}$ que aquí usamos con $n = 2$.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — de dónde salen las derivadas que calculamos.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — la segunda derivada como aceleración en problemas físicos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero el algoritmo de cinco pasos con los ejemplos $x^3$ y $x^4$ hasta que el filtro del cambio de signo sea automático.
> - Después combina $f'$ y $f''$ en el ejercicio de bosquejo de $f(x) = x^3 - 3x$: es el tipo que une todas las notas de análisis.
> - Cuando domines la concavidad, aplica la segunda derivada en [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|Problemas de Optimización]] para clasificar extremos sin tablas.
> - En cada ejercicio, escribe siempre **qué condición estás verificando** (necesaria o suficiente) antes de concluir.

---

**Tags:** #MATG1045 #unidad5 #concavidad #puntos-inflexion #segunda-derivada #intervalos-concavidad #falsos-inflexiones #graficacion

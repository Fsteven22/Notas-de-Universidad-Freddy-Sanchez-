---
dg-publish: true
tags: [MATG1045, unidad5, monotonia, puntos-criticos, primera-derivada, extremos-locales, tabla-de-signos, optimizacion, teoremas-valor-medio]
---

# 📊 Monotonía y Puntos Críticos

## 🎯 Introducción

> [!info] 💡 Qué estudia esta nota
>
> La **monotonía** describe si una función es creciente o decreciente en intervalos concretos, y los **puntos críticos** son los valores donde ese comportamiento puede cambiar. Con ambas piezas se deciden máximos y mínimos locales, que es la puerta de entrada a la optimización.
>
> **Por qué importa:**
>
> - Permite determinar máximos y mínimos de funciones.
> - Es el fundamento de la optimización de la Unidad 5.
> - Es la base del análisis completo de funciones.
> - Es la herramienta clave de los problemas aplicados de economía, física e ingeniería.
>
> **Ejemplo:** en $f(x) = x^3 - 3x^2 - 9x + 5$ los puntos críticos $x = -1$ y $x = 3$ son justamente donde la función deja de subir y empieza a bajar (o al revés): ahí viven el máximo y el mínimo.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Monotonía
>
> Una función $f$ es **creciente en un intervalo $I$** si para todo $x_1, x_2 \in I$ con $x_1 < x_2$ se cumple $f(x_1) \leq f(x_2)$; es **estrictamente creciente** cuando la desigualdad es estricta ($f(x_1) < f(x_2)$). Es **decreciente en $I$** si $f(x_1) \geq f(x_2)$ para todo $x_1 < x_2$ en $I$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Monotonía_y_Puntos_Críticos_02.svg]]
>
> **Se lee así:** el diagrama arranca con una función definida en un intervalo y encadena dos preguntas de comparación: si $f(x_1) \leq f(x_2)$ siempre, la función es creciente; si no, prueba $f(x_1) \geq f(x_2)$, y si se cumple es decreciente; si ninguna, no es monótona. Cada veredicto se traduce después a su criterio con derivada: $f' > 0$ para creciente y $f' < 0$ para decreciente.
>
> **Por qué importa:** las dos definiciones se distinguen por el sentido de la desigualdad, no por la derivada: la derivada es el criterio práctico que viene después. Entender esa separación te evita confundir "la función es negativa" con "la función baja".
>
> **Ejemplo:** $f(x) = x^2$ es decreciente en $(-\infty, 0]$ y creciente en $[0, +\infty)$: en el primer intervalo, al subir $x$ la función baja.

> [!note] 📋 Definición — Punto crítico
>
> Un punto $x = c$ es **punto crítico** de $f$ si:
>
> 1. $c$ está en el **dominio** de $f$; y
> 2. se cumple una de estas dos condiciones: $f'(c) = 0$ **o** $f'(c)$ no existe.
>
> Según el comportamiento alrededor de $c$: **máximo local** ($f(c) \geq f(x)$ cerca de $c$), **mínimo local** ($f(c) \leq f(x)$ cerca de $c$), o **punto silla** (ni máximo ni mínimo).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Monotonía_y_Puntos_Críticos_03.svg]]
>
> **Se lee así:** es un árbol de decisiones: primero un rombo exige que $c$ esté en el dominio; después otro comprueba que la derivada sea cero o no exista; si ambas se cumplen, $c$ es punto crítico y un último rombo mira si el signo de $f'$ cambia en $c$. El cambio de $+$ a $-$ da máximo local, de $-$ a $+$ da mínimo, y el mismo signo indica punto de inflexión horizontal sin extremo.
>
> **Por qué importa:** el árbol recuerda los dos filtros que se olvidan: estar en el dominio y que la derivada pueda fallar sin ser cero. Sin ellos, declaras "crítico" a un punto inexistente o te saltas el $|x|$ en el $0$.
>
> **Ejemplo:** en $f(x) = x^{2/3}(x-5)$ el candidato $x = 0$ no tiene $f'(0) = 0$ pero sí $f'(0)$ inexistente: el segundo rombo lo deja pasar y el cambio de signo lo clasifica como máximo local.

---

## 🧮 Criterio de la primera derivada

> [!success] ✅ Teorema de monotonía
>
> Sea $f$ derivable en el intervalo $(a,b)$:
>
> - Si $f'(x) > 0$ para todo $x \in (a,b)$ → $f$ es **estrictamente creciente** en $(a,b)$.
> - Si $f'(x) < 0$ para todo $x \in (a,b)$ → $f$ es **estrictamente decreciente** en $(a,b)$.
> - Si $f'(x) = 0$ para todo $x \in (a,b)$ → $f$ es **constante** en $(a,b)$.
>
> **Interpretación geométrica:** $f' > 0$ significa pendiente positiva (la curva sube); $f' < 0$, pendiente negativa (baja); $f' = 0$, tangente horizontal.
>
> **Por qué importa:** este teorema traduce un problema de comparación infinita (probar $f(x_1) \leq f(x_2)$ para todos los pares) en un problema de signo en intervalos, que se resuelve con una tabla.

> [!example] 🏔️ Test de la primera derivada para extremos
>
> Sea $x = c$ un punto crítico de $f$:
>
> | Comportamiento de $f'$ | Antes de $c$ | En $c$ | Después de $c$ | Conclusión |
> |---|---|---|---|---|
> | **Máximo local** | $f' > 0$ | $f' = 0$ | $f' < 0$ | Sube y luego baja |
> | **Mínimo local** | $f' < 0$ | $f' = 0$ | $f' > 0$ | Baja y luego sube |
> | **No extremo** | $f' > 0$ | $f' = 0$ | $f' > 0$ | Punto de inflexión horizontal |
> | **No extremo** | $f' < 0$ | $f' = 0$ | $f' < 0$ | Punto de inflexión horizontal |
>
> **Por qué importa:** el signo de $f'$ **antes y después** es lo que clasifica; el cero solo identifica al candidato. Es el error clásico de dar por máximo todo punto donde $f' = 0$.
>
> **Ejemplo:** $f(x) = x^3$ tiene $f'(0) = 0$, pero el signo es $+$ en ambos lados: no hay extremo, solo un punto de inflexión horizontal.

---

## 🔄 Metodología de análisis

> [!tip] 📋 Algoritmo en cinco pasos (método DICE)
>
> 1. **D — Derivar:** calcula $f'(x)$.
> 2. **I — Igualar a cero:** resuelve $f'(x) = 0$ e identifica dónde $f'(x)$ no existe; verifica que cada candidato esté en el dominio.
> 3. **C — Crear tabla de signos:** divide el dominio con los puntos críticos y evalúa el signo de $f'(x)$ en cada intervalo (con un punto de prueba por intervalo).
> 4. **E — Evaluar:** $f' > 0$ → creciente; $f' < 0$ → decreciente; clasifica cada crítico por el cambio de signo.
> 5. **A — Anotar:** escribe intervalos de monotonía y extremos con su valor.
>
> **Checklist de verificación:** ¿calculé bien $f'(x)$? · ¿encontré todos los ceros? · ¿busqué donde no existe? · ¿verifiqué el dominio? · ¿completé la tabla? · ¿clasifiqué cada punto?
>
> **Por qué importa:** "Deriva, Iguala, Crea y Evalúa" es la secuencia que sale limpia en un examen; saltarse el paso de dominio o el de derivada inexistente es donde se pierden los puntos.

> [!info] 🖼️ Diagrama de flujo del análisis
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Monotonía_y_Puntos_Críticos_01.svg]]
>
> **Se lee así:** el flujo deriva, busca los ceros de $f'(x)$ y los puntos donde la derivada no existe, y luego divide el dominio en intervalos para tabular el signo. De la conclusión salen tres ramas: derivada positiva, negativa o nula en el punto crítico. Las dos primeras se juntan en la clasificación del punto, que se abre en máximo local o mínimo local según el signo cambie de más a menos o al revés.
>
> **Por qué importa:** fíjate en que el diagrama separa **encontrar** candidatos de **clasificar** el extremo: eso evita declarar un máximo sin revisar el signo antes y después. También recuerda que un punto crítico exige estar en el dominio y que la derivada puede no existir sin ser cero.
>
> **Ejemplo:** para $f(x) = x^3 - 3x^2 - 9x + 5$, los candidatos $x = -1$ y $x = 3$ salen de $f'(x) = 3(x+1)(x-3)$, y el diagrama te dice que el primero es máximo local y el segundo mínimo local.

> [!info] 🖼️ Control visual con la gráfica de $f(x) = x^3 - 3x$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/cal1-analisis-grafica-cubica-x3-3x.png]]
>
> **Se lee así:** se ve la gráfica de $f(x) = x^3 - 3x$ en el plano cartesiano, con la leyenda en la esquina superior izquierda. La curva tiene forma de S: sube, baja y vuelve a subir, y cruza el eje $x$ en $-\sqrt{3}$, en $0$ y en $\sqrt{3}$. Dos puntos están marcados en rojo y rotulados: el máximo en $(-1, 2)$ y el mínimo en $(1, -2)$, que son justamente los puntos críticos que busca el diagrama de flujo anterior.
>
> **Por qué importa:** ver la gráfica te da la respuesta antes de derivar: los dos puntos rojos son exactamente donde $f'(x) = 0$. Esto te sirve como control para saber si tu tabla de signos y tu clasificación quedaron bien.
>
> **Ejemplo:** si tu análisis de $f(x) = x^3 - 3x$ da un máximo local en $(-1, 2)$ y un mínimo en $(1, -2)$, comparas esos puntos con los de la figura y confirmas que el resultado es correcto.

---

## 🎨 Ejemplos resueltos

> [!example] 📈 Ejemplo 1: polinomio cúbico, $f(x) = x^3 - 3x^2 - 9x + 5$
>
> **Derivada:** $f'(x) = 3x^2 - 6x - 9 = 3(x-3)(x+1)$, con ceros $x = -1$ y $x = 3$ (ambos en el dominio).
>
> **Tabla de signos:**
>
> | Intervalo | $x < -1$ | $x = -1$ | $-1 < x < 3$ | $x = 3$ | $x > 3$ |
> |---|---|---|---|---|---|
> | $(x+1)$ | $-$ | $0$ | $+$ | $+$ | $+$ |
> | $(x-3)$ | $-$ | $-$ | $-$ | $0$ | $+$ |
> | $f'(x) = 3(x+1)(x-3)$ | $+$ | $0$ | $-$ | $0$ | $+$ |
> | Monotonía de $f$ | ↗ | MAX | ↘ | MIN | ↗ |
>
> **Resultados:** creciente en $(-\infty, -1) \cup (3, +\infty)$; decreciente en $(-1, 3)$; máximo local en $x = -1$, $f(-1) = 10$; mínimo local en $x = 3$, $f(3) = -22$.

> [!example] 📉 Ejemplo 2: función racional, $f(x) = \frac{x^2 - 4}{x^2 + 1}$
>
> **Derivada (regla del cociente):**
>
> $$f'(x) = \frac{(2x)(x^2+1) - (x^2-4)(2x)}{(x^2+1)^2} = \frac{2x[(x^2+1)-(x^2-4)]}{(x^2+1)^2} = \frac{10x}{(x^2+1)^2}.$$
>
> **Puntos críticos:** el denominador nunca es cero, así que solo $f'(x) = 0$ da $x = 0$.
>
> **Signos:** como $(x^2+1)^2 > 0$ siempre, el signo lo decide $10x$: negativo para $x < 0$, positivo para $x > 0$.
>
> **Resultados:** decreciente en $(-\infty, 0)$, creciente en $(0, +\infty)$; mínimo absoluto en $x = 0$ con $f(0) = -4$.

> [!example] 🌱 Ejemplo 3: función con raíz, $f(x) = x^{2/3}(x - 5)$
>
> **Derivada:** expandiendo, $f(x) = x^{5/3} - 5x^{2/3}$, y
>
> $$f'(x) = \frac{5}{3}x^{2/3} - \frac{10}{3}x^{-1/3} = \frac{5(x-2)}{3x^{1/3}}.$$
>
> **Puntos críticos:** $f'(x) = 0$ da $x = 2$; $f'(x)$ no existe en $x = 0$ (denominador cero), que sí está en el dominio.
>
> **Tabla de signos:**
>
> | Intervalo | $x < 0$ | $x = 0$ | $0 < x < 2$ | $x = 2$ | $x > 2$ |
> |---|---|---|---|---|---|
> | $(x-2)$ | $-$ | $-$ | $-$ | $0$ | $+$ |
> | $x^{1/3}$ | $-$ | $0$ | $+$ | $+$ | $+$ |
> | $f'(x)$ | $+$ | ∄ | $-$ | $0$ | $+$ |
> | Monotonía | ↗ | MAX | ↘ | MIN | ↗ |
>
> **Resultados:** creciente en $(-\infty, 0) \cup (2, +\infty)$; decreciente en $(0, 2)$; máximo local en $x = 0$ con $f(0) = 0$; mínimo local en $x = 2$ con $f(2) = -3 \cdot 2^{2/3}$. Fíjate en que el máximo apareció donde la derivada **no existía**.

---

## ⚠️ Errores y casos especiales

> [!warning] 🚨 Los cinco errores frecuentes
>
> 1. **Olvidar los puntos donde la derivada no existe:** no basta con $f'(x) = 0$; hay que buscar también donde $f'(x)$ no está definida.
> 2. **No verificar el dominio:** un candidato fuera del dominio no es punto crítico.
> 3. **Tabla de signos incompleta:** evalúa $f'(x)$ en **todos** los intervalos que abren los críticos, con un punto de prueba en cada uno.
> 4. **Confundir extremos locales con globales:** un máximo local no es automáticamente el máximo absoluto.
> 5. **Invertir los signos:** $f'(x) > 0$ significa función **creciente**, no decreciente.
>
> **Por qué importa:** los cinco son errores de procedimiento, no de cálculo; se corrigen con el checklist DICE antes de dar el ejercicio por terminado.

> [!note] 🎪 Casos especiales
>
> - **Extremos del dominio:** el criterio de la primera derivada puede no aplicar; analiza los límites laterales.
> - **Derivada que no cambia de signo:** $f'(x) = (x-2)^2$ se anula en $x = 2$ pero mantiene el signo: no hay extremo, solo punto de inflexión horizontal.
> - **No diferenciables:** $f(x) = |x|$ no es derivable en $x = 0$, y sin embargo $x = 0$ es mínimo local; ahí usa la definición directa de extremo.
> - **Infinitos críticos:** $f(x) = x^2\sin(1/x)$ (con $f(0) = 0$) tiene infinitos puntos críticos cerca del origen.
>
> **Por qué importa:** estos casos son los que separan un análisis mecánico de uno riguroso; aparecen en los ejercicios "trampa" de los parciales.

---

## 🔧 Teoremas y conexiones

> [!quote] 🎓 Teoremas de existencia
>
> **Teorema de Rolle:** si $f$ es continua en $[a,b]$, diferenciable en $(a,b)$ y $f(a) = f(b)$, existe $c \in (a,b)$ con $f'(c) = 0$.
>
> **Teorema del valor medio:** si $f$ es continua en $[a,b]$ y diferenciable en $(a,b)$, existe $c \in (a,b)$ tal que
>
> $$f'(c) = \frac{f(b) - f(a)}{b - a}.$$
>
> **Aplicaciones:** garantizan la existencia de puntos críticos en ciertas condiciones, conectan el comportamiento local con el global y son la base teórica del análisis de monotonía.

> [!success] 🔗 Dónde se conecta esta nota
>
> - **Concavidad (segunda derivada):** $f'' > 0$ cóncava arriba, $f'' < 0$ cóncava abajo, inflexiones donde $f'' = 0$.
> - **Límites y continuidad:** comportamiento en los extremos del dominio y efecto de las discontinuidades.
> - **Integrales:** el teorema fundamental del cálculo y las áreas bajo curvas crecientes/decrecientes.
> - **Optimización:** los puntos críticos son los candidatos a extremo en los problemas de máximo y mínimo.

> [!note] 👁️ Lectura gráfica de la monotonía
>
> | Comportamiento de $f(x)$ | Signo de $f'(x)$ | Gráfica de $f'(x)$ |
> |---|---|---|
> | Creciente | $f' > 0$ | Por encima del eje $x$ |
> | Decreciente | $f' < 0$ | Por debajo del eje $x$ |
> | Máximo local | $f' = 0$ | Cruza de $+$ a $-$ |
> | Mínimo local | $f' = 0$ | Cruza de $-$ a $+$ |
> | Punto de inflexión | $f' = 0$ | Toca el eje pero no cruza |
>
> **Por qué importa:** leer la derivada gráficamente te deja verificar de un vistazo un análisis completo: los picos y valles de $f$ son los ceros de $f'$, y la curva de $f'$ subiendo o bajando te habla de la concavidad que verás en la próxima nota.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Encuentra los puntos críticos y los intervalos de monotonía de $f(x) = x^3 - 6x^2 + 9x + 1$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 3x^2 - 12x + 9 = 3(x-1)(x-3)$, con ceros $x = 1$ y $x = 3$, ambos en el dominio.
> >
> > Tabla: $f' > 0$ en $(-\infty, 1)$, $f' < 0$ en $(1, 3)$, $f' > 0$ en $(3, +\infty)$.
> >
> > **Resultado:** creciente en $(-\infty, 1) \cup (3, +\infty)$, decreciente en $(1, 3)$; máximo local en $x = 1$ ($f(1) = 5$) y mínimo local en $x = 3$ ($f(3) = 1$).

> [!example] 📋 Planteamiento
>
> Analiza $f(x) = \frac{x}{x^2+1}$ con el método DICE.
>
> > [!success]- ✅ Solución
> >
> > **D:** regla del cociente: $f'(x) = \frac{(1)(x^2+1) - x(2x)}{(x^2+1)^2} = \frac{1 - x^2}{(x^2+1)^2}$.
> >
> > **I:** $f'(x) = 0$ da $x = \pm 1$; la derivada existe en todo $\mathbb{R}$.
> >
> > **C:** el denominador es siempre positivo, así que el signo lo decide $1 - x^2$: positivo en $(-1, 1)$ y negativo fuera.
> >
> > **E:** creciente en $(-1, 1)$, decreciente en $(-\infty, -1) \cup (1, +\infty)$.
> >
> > **A:** mínimo local en $x = -1$ con $f(-1) = -1/2$; máximo local en $x = 1$ con $f(1) = 1/2$.

> [!example] 📋 Planteamiento
>
> Clasifica $x = 0$ en $f(x) = x^{2/3}$ usando la definición de punto crítico.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = \frac{2}{3}x^{-1/3} = \frac{2}{3x^{1/3}}$: no existe en $x = 0$ (denominador cero), y $0$ está en el dominio, así que **es punto crítico**.
> >
> > Signos de $f'$: negativos para $x < 0$ y positivos para $x > 0$, así que la función baja y sube: mínimo local en $x = 0$ con $f(0) = 0$.
> >
> > **Lección:** un punto crítico puede nacer de una derivada inexistente, no solo de $f' = 0$.

> [!example] 📋 Planteamiento
>
> ¿Por qué $f(x) = x^3$ no tiene extremos aunque $f'(0) = 0$?
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 3x^2 \geq 0$ para todo $x$, y en $x = 0$ vale $0$.
> >
> > El signo de $f'$ es positivo **antes y después** de $0$: no hay cambio, así que por el test de la primera derivada no hay extremo, solo un punto de inflexión horizontal.
> >
> > **Lección:** el cero de la derivada identifica al candidato; lo que clasifica es el cambio de signo.

> [!example] 📋 Planteamiento
>
> Encuentra los extremos de $f(x) = xe^{-x}$ para $x \in \mathbb{R}$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = (1)e^{-x} + x(-e^{-x}) = e^{-x}(1 - x)$.
> >
> > Como $e^{-x} > 0$ siempre, $f'(x) = 0$ solo en $x = 1$, que es el único punto crítico.
> >
> > Signos: $f' > 0$ para $x < 1$ y $f' < 0$ para $x > 1$: creciente y luego decreciente.
> >
> > **Resultado:** máximo local (y absoluto) en $x = 1$ con $f(1) = 1/e \approx 0{,}368$; sin mínimo.

> [!example] 📋 Planteamiento
>
> Aplica el teorema del valor medio a $f(x) = x^2$ en $[1, 4]$ y verifica el punto $c$.
>
> > [!success]- ✅ Solución
> >
> > $f$ es continua en $[1, 4]$ y derivable en $(1, 4)$, así que existe $c$ con $f'(c) = \frac{f(4)-f(1)}{4-1}$.
> >
> > $f'(c) = 2c$ y $\frac{16 - 1}{3} = 5$, así que $2c = 5$ y $c = 2{,}5 \in (1, 4)$.
> >
> > **Interpretación:** en $x = 2{,}5$ la tangente es paralela a la recta que une los extremos del arco: el teorema siempre garantiza esa coincidencia.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo las definiciones de función creciente, decreciente y punto crítico.
> - [ ] Aplico el criterio de la primera derivada para decidir monotonía en un intervalo.
> - [ ] Construyo una tabla de signos de $f'(x)$ completa a partir de los puntos críticos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Clasifico cada punto crítico como máximo local, mínimo local o no extremo con el test de la primera derivada.
> - [ ] Encuentro los puntos críticos que nacen donde la derivada no existe, no solo donde se anula.
> - [ ] Analizo funciones polinómicas, racionales y con raíz de principio a fin con el método DICE.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Distingo extremos locales de absolutos y justifico la diferencia.
> - [ ] Aplico el teorema del valor medio y verifico el punto $c$ que garantiza.
> - [ ] Resuelvo los casos especiales (derivada sin cambio de signo, no diferenciables, extremos del dominio) sin caer en los cinco errores comunes.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: monotonía, puntos críticos y test de la primera derivada.
> - R. Larson, *Cálculo* (Cengage), cap. 4: extremos locales y análisis con la primera derivada.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 6: teoremas de Rolle y del valor medio.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la derivada que aquí se usa como test de signo.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — por qué hay puntos críticos sin derivada.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — el test de la segunda derivada que continúa esta nota.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dos condiciones debe cumplir un punto crítico?::Estar en el dominio de $f$ y cumplir que $f'(c) = 0$ o que $f'(c)$ no exista.
> - ¿Qué dice el criterio de la primera derivada?::Si $f'(x) > 0$ en $(a,b)$ la función es creciente ahí; si $f'(x) < 0$ es decreciente; si $f' = 0$ en todo el intervalo es constante.
> - ¿Cómo se clasifica un punto crítico?::Mirando el signo de $f'$ antes y después: de $+$ a $-$ da máximo local, de $-$ a $+$ da mínimo, y si no cambia no hay extremo.
> - ¿Por qué $f(x) = x^{2/3}$ tiene extremo en $0$?::Porque $f'(0)$ no existe pero $0$ está en el dominio, y el signo de $f'$ cambia de $-$ a $+$: mínimo local.
> - ¿Qué garantiza el teorema del valor medio?::Que en $(a,b)$ exista un $c$ con $f'(c) = (f(b)-f(a))/(b-a)$: la tangente en $c$ es paralela a la recta secante de los extremos.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — de dónde sale $f'(x)$.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — los puntos donde la derivada no existe.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — el checklist completo donde esta nota es el bloque de derivadas.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — la segunda derivada y la curvatura.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — los puntos críticos como candidatos a extremo.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/01 - Tasas de Cambio|01 - Tasas de Cambio]] — la derivada como velocidad, que también se anula en los extremos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica el método DICE con el primer y segundo ejercicio hasta que la tabla de signos salga sola.
> - Después salta a [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|Concavidad y Puntos de Inflexión]] para añadir la segunda derivada al análisis.
> - Cuando domines los extremos locales, ve a [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|Problemas de Optimización]] a aplicarlos a situaciones del mundo real.
> - En cada ejercicio, escribe siempre **qué punto crítico es** y **qué evidencia de signo** justifica su clasificación.

---

**Tags:** #MATG1045 #unidad5 #monotonia #puntos-criticos #primera-derivada #extremos-locales #tabla-de-signos #optimizacion #teoremas-valor-medio

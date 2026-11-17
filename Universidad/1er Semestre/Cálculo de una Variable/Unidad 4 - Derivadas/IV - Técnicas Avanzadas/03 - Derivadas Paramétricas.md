---
dg-publish: true
tags: [MATG1045, unidad4, derivadas-parametricas, ecuaciones-parametricas, regla-cadena, tangentes, curvatura, longitud-arco]
---

# 🎯 Derivadas Paramétricas

## 🎯 Introducción

> [!info] 💡 Qué resuelve la parametrización
>
> Una **curva paramétrica** se describe por $x = f(t)$ y $y = g(t)$: en lugar de tener $y$ como función de $x$, ambas coordenadas dependen de un parámetro $t$. Las **derivadas paramétricas** permiten encontrar la pendiente de esa curva aunque sea imposible despejar $y$ en función de $x$.
>
> **Por qué importa:** el círculo, la cicloide, la hipérbola y las trayectorias de un móvil se describen así. Además, el parámetro da una lectura física: $t$ es el tiempo y $\frac{dx}{dt}$, $\frac{dy}{dt}$ son las componentes de la velocidad.
>
> **Ejemplo:** para $x = t^3 - 3t$, $y = t^2$, el cociente $\frac{2t}{3(t^2-1)}$ da tangente horizontal en $t = 0$ y tangentes verticales en $t = \pm 1$.

> [!warning] ⚠️ Los dos errores que más se repiten
>
> - **NO** dividas sin comprobar $\frac{dx}{dt} \neq 0$: si el denominador se anula, la tangente es **vertical** y hay que analizarla aparte.
> - **NO** inviertas el cociente: $\frac{dy}{dx}$ y $\frac{dx}{dy}$ son recíprocos, no iguales.
>
> **Por qué importa:** ambos errores cambian por completo el resultado, y el primero además oculta información importante de la curva.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Derivada paramétrica
>
> Para una curva $x = f(t)$, $y = g(t)$ con $g'(t)$ y $f'(t)$ existentes, la **derivada paramétrica** es
>
> $$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{g'(t)}{f'(t)},$$
>
> siempre que $f'(t) \neq 0$. Es la pendiente de la recta tangente a la curva en el punto $(x, y)$ que corresponde al parámetro $t$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivadas_Paramétricas_01.svg]]
>
> **Se lee así:** el flujo arranca con la curva paramétrica en un rectángulo, sigue por el cálculo de las dos derivadas respecto al parámetro y llega a un **rombo de decisión** que pregunta si $\frac{dx}{dt}$ es distinto de cero. Si es así, una rama lleva a la caja de la pendiente $\frac{dy}{dx} = \frac{g'(t)}{f'(t)}$ y de ahí a evaluarla en un valor concreto de $t$; si no, la otra lleva a la tangente vertical o al punto singular, que se analizan aparte.
>
> **Por qué importa:** te ordena el trabajo en pasos fijos y te obliga a **verificar la condición $\frac{dx}{dt} \neq 0$** antes de dividir. Esa comprobación evita el error clásico de dividir entre cero y perder las tangentes verticales.
>
> **Ejemplo:** para $x = t^3 - 3t$, $y = t^2$, el cociente $\frac{2t}{3(t^2-1)}$ da tangente horizontal en $t = 0$ y tangentes verticales en $t = \pm 1$.

> [!info] 🔍 Por qué funciona la fórmula
>
> Por la regla de la cadena:
>
> - $\frac{dy}{dx} = \frac{dy}{dt}\cdot\frac{dt}{dx}$.
> - Como $\frac{dt}{dx} = \frac{1}{\frac{dx}{dt}}$.
> - Entonces $\frac{dy}{dx} = \frac{dy}{dt}\cdot\frac{1}{\frac{dx}{dt}} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}$.
>
> **Por qué importa:** la fórmula no es un truco: es la regla de la cadena con el parámetro en el medio. Por eso el cociente y no la resta, y por eso el mismo razonamiento sirve para la segunda derivada.

---

## 📊 Ejemplos fundamentales

> [!example] 🔢 Parábola paramétrica
>
> **Encontrar** $\frac{dy}{dx}$ para $x = t^2$, $y = 2t$.
>
> - $\frac{dx}{dt} = 2t$ y $\frac{dy}{dt} = 2$.
> - $\frac{dy}{dx} = \frac{2}{2t} = \frac{1}{t}$ (para $t \neq 0$).
>
> **Verificación eliminando el parámetro:** $t = \frac{y}{2}$, luego $x = \frac{y^2}{4}$; derivando implícitamente, $1 = \frac{y}{2}\frac{dy}{dx}$, de donde $\frac{dy}{dx} = \frac{2}{y} = \frac{1}{t}$ ✅
>
> **Por qué importa:** eliminar el parámetro y comparar es la mejor forma de **verificar** un resultado paramétrico.

> [!example] 🔢 Círculo paramétrico
>
> **Encontrar** $\frac{dy}{dx}$ para $x = r\cos(t)$, $y = r\sin(t)$.
>
> - $\frac{dx}{dt} = -r\operatorname{sen}(t)$ y $\frac{dy}{dt} = r\cos(t)$.
> - $\frac{dy}{dx} = \frac{r\cos(t)}{-r\operatorname{sen}(t)} = -\cot(t)$.
>
> **Interpretación:** es la pendiente de la tangente al círculo en el punto del ángulo $t$; como el radio es perpendicular a la tangente, la pendiente de la tangente es la recíproca negativa de la pendiente del radio.

> [!example] 🔢 Cicloide
>
> **Encontrar** $\frac{dy}{dx}$ para $x = a(t - \operatorname{sen}t)$, $y = a(1 - \cos t)$.
>
> - $\frac{dx}{dt} = a(1 - \cos t)$ y $\frac{dy}{dt} = a\operatorname{sen}t$.
> - $\frac{dy}{dx} = \frac{\operatorname{sen}t}{1 - \cos t}$.
> - Con identidades de medio ángulo: $\frac{2\operatorname{sen}(t/2)\cos(t/2)}{2\operatorname{sen}^2(t/2)} = \cot(t/2)$.
>
> **Resultado:** $\frac{dy}{dx} = \cot(t/2)$.
>
> **Por qué importa:** las identidades de medio ángulo son la herramienta estándar aquí: simplifican cocientes que en $t$ no se ven.

> [!example] 🔢 Curva exponencial
>
> **Encontrar** $\frac{dy}{dx}$ para $x = e^t$, $y = t^2$.
>
> - $\frac{dx}{dt} = e^t$ y $\frac{dy}{dt} = 2t$.
> - $\frac{dy}{dx} = \frac{2t}{e^t}$.
> - Como $x = e^t$, entonces $t = \ln x$, y queda $\frac{dy}{dx} = \frac{2\ln x}{x}$.
>
> **Por qué importa:** cuando el enunciado pide la derivada "en función de $x$", hay que **deshacer el parámetro** al final.

---

## 🔄 Derivadas de orden superior

> [!info] 🧮 Segunda derivada paramétrica
>
> Para derivar dos veces se usa la misma idea, encadenada:
>
> $$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(\frac{dy}{dx}\right) = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}}.$$
>
> En tres pasos: se calcula $\frac{dy}{dx}$, se deriva **respecto a $t$** con la regla del cociente, y se divide otra vez por $\frac{dx}{dt}$.
>
> > [!info] 🖼️ Recorrido de la segunda derivada
> >
> > ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivadas_Paramétricas_02.svg]]
> >
> > **Se lee así:** el diagrama es un **recorrido de seis rectángulos** que avanza siempre en una sola dirección: se empieza por la primera derivada ya calculada, se deriva respecto al parámetro, aparece un recuadro que recuerda usar la regla del cociente, sigue el desarrollo algebraico de ese cociente, aparece una división extra y se cierra con la segunda derivada ya simplificada.
> >
> > **Por qué importa:** fíjate en que el paso clave es el *cociente*: derivar $\frac{dy}{dx}$ como si fuera una fracción corriente y luego dividir otra vez por $\frac{dx}{dt}$. Eso evita el error típico de derivar respecto a $x$ o de olvidar el segundo cociente, que es donde se va el punto del ejercicio.
> >
> > **Ejemplo:** con $x = r\cos(t)$ y $y = r\operatorname{sen}(t)$, el recorrido da $\frac{dy}{dx} = -\cot(t)$, su derivada respecto a $t$ es $\csc^2(t)$ y, al dividir por $-r\operatorname{sen}(t)$, se obtiene $\frac{d^2y}{dx^2} = -\frac{1}{r\operatorname{sen}^3(t)}$.

> [!example] 🔢 Segunda derivada del círculo
>
> **Encontrar** $\frac{d^2y}{dx^2}$ para $x = r\cos(t)$, $y = r\operatorname{sen}(t)$.
>
> - $\frac{dy}{dx} = -\cot(t)$.
> - $\frac{d}{dt}(-\cot t) = \csc^2(t)$.
> - $\frac{dx}{dt} = -r\operatorname{sen}(t)$.
> - $\frac{d^2y}{dx^2} = \frac{\csc^2(t)}{-r\operatorname{sen}(t)} = -\frac{1}{r\operatorname{sen}^3(t)}$.
>
> **Interpretación:** el signo cambia con el cuadrante, como corresponde a un círculo: la parte superior es cóncava hacia abajo y la inferior, hacia arriba.

> [!info] 📊 Fórmula directa de la segunda derivada
>
> $$\frac{d^2y}{dx^2} = \frac{g''(t)f'(t) - g'(t)f''(t)}{[f'(t)]^3},$$
>
> donde $f'(t) = \frac{dx}{dt}$, $f''(t) = \frac{d^2x}{dt^2}$, $g'(t) = \frac{dy}{dt}$ y $g''(t) = \frac{d^2y}{dt^2}$.
>
> **Por qué importa:** es la regla del cociente aplicada y simplificada de una vez; conviene conocerla para verificar el resultado del procedimiento de tres pasos.

> [!example] 🔢 Segundaderivative directa
>
> **Encontrar** $\frac{d^2y}{dx^2}$ para $x = t^3$, $y = t^2$.
>
> - $f'(t) = 3t^2$, $f''(t) = 6t$, $g'(t) = 2t$, $g''(t) = 2$.
> - $\frac{d^2y}{dx^2} = \frac{2 \cdot 3t^2 - 2t \cdot 6t}{(3t^2)^3} = \frac{6t^2 - 12t^2}{27t^6} = -\frac{2}{9t^4}$.
>
> **Comprobación por el método de tres pasos:** $\frac{dy}{dx} = \frac{2t}{3t^2} = \frac{2}{3t}$; derivando respecto a $t$, $-\frac{2}{3t^2}$; dividiendo por $3t^2$: $-\frac{2}{9t^4}$ ✅

---

## 🎪 Casos especiales y singularidades

> [!info] 🧮 Los tres casos que hay que saber detectar
>
> - **Tangente horizontal:** $\frac{dy}{dx} = 0$, ocurre cuando $\frac{dy}{dt} = 0$ y $\frac{dx}{dt} \neq 0$.
> - **Tangente vertical:** $\frac{dy}{dx} = \pm\infty$, ocurre cuando $\frac{dx}{dt} = 0$ y $\frac{dy}{dt} \neq 0$.
> - **Punto singular:** ambas derivadas son cero a la vez; requiere analizar con derivadas superiores o con L'Hôpital.
>
> **Por qué importa:** el diagrama de decisión de la definición ya separa estos casos: cuando $\frac{dx}{dt} = 0$ no se divide, se interpreta.

> [!example] 🔢 Análisis de singularidades
>
> **Analizar** $x = t^3 - 3t$, $y = t^2$.
>
> - $\frac{dx}{dt} = 3t^2 - 3 = 3(t^2-1)$ y $\frac{dy}{dt} = 2t$.
> - $\frac{dy}{dx} = \frac{2t}{3(t^2-1)}$.
>
> **Tangente horizontal:** $\frac{dy}{dt} = 0 \Rightarrow t = 0$. En $t = 0$: $x = 0$, $y = 0$ y $\frac{dx}{dt} = -3 \neq 0$. Tangente horizontal en $(0, 0)$.
>
> **Tangentes verticales:** $\frac{dx}{dt} = 0 \Rightarrow t = \pm 1$. En $t = 1$: $x = -2$, $y = 1$; en $t = -1$: $x = 2$, $y = 1$. Tangentes verticales en $(-2, 1)$ y $(2, 1)$.

---

## 🔢 Aplicaciones geométricas

> [!info] 🧮 Longitud de arco
>
> $$L = \int_{t_1}^{t_2} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt$$
>
> **Por qué importa:** la pendiente da la *dirección* del movimiento, pero la longitud necesita la *velocidad total*: por eso entra la suma de cuadrados de las dos componentes.

> [!example] 🔢 Longitud de un semicírculo
>
> **Calcular** la longitud con $x = r\cos(t)$, $y = r\operatorname{sen}(t)$, $t \in [0, \pi]$.
>
> - $\frac{dx}{dt} = -r\operatorname{sen}(t)$ y $\frac{dy}{dt} = r\cos(t)$.
> - $\sqrt{r^2\operatorname{sen}^2(t) + r^2\cos^2(t)} = \sqrt{r^2} = r$.
> - $L = \int_0^\pi r\,dt = r\pi$ ✅
>
> **Por qué importa:** el resultado no depende de la parametrización: el resultado es la mitad de la circunferencia, $\pi r$.

> [!info] 🧮 Área bajo una curva paramétrica
>
> $$A = \int_{t_1}^{t_2} y\,\frac{dx}{dt}\,dt$$
>
> **Condición:** la curva no debe intersectarse a sí misma en el intervalo.
>
> **Por qué importa:** el signo de $\frac{dx}{dt}$ indica el sentido en que se recorre la curva; por eso hay que cuidar los límites de integración para obtener un área positiva.

> [!example] 🔢 Área bajo la cicloide
>
> **Calcular** el área bajo $x = t - \operatorname{sen}(t)$, $y = 1 - \cos(t)$, $t \in [0, 2\pi]$.
>
> - $\frac{dx}{dt} = 1 - \cos(t)$.
> - $A = \int_0^{2\pi} (1-\cos t)^2\,dt = \int_0^{2\pi}\left(1 - 2\cos t + \cos^2 t\right)dt$.
> - $= \left[t - 2\operatorname{sen}t + \frac{t}{2} + \frac{\operatorname{sen}(2t)}{4}\right]_0^{2\pi} = 3\pi$.

---

## ⚠️ Errores comunes y estrategias

> [!warning] 🚨 Errores frecuentes
>
> **Conceptuales:**
>
> - Confundir $\frac{dx}{dy}$ con $\frac{dy}{dx}$: son recíprocos, no iguales.
> - Olvidar verificar $\frac{dx}{dt} \neq 0$.
> - No simplificar con identidades, especialmente en los casos trigonométricos.
>
> **De cálculo:**
>
> - Derivar respecto a $x$ en lugar de $t$ en las derivadas superiores.
> - Aplicar mal la regla de la cadena en las composiciones.
> - Signos incorrectos, sobre todo en funciones trigonométricas.
>
> **En derivadas superiores:**
>
> - Usar la fórmula directa sin verificar la regla del cociente.
> - Dejar expresiones sin simplificar cuando hay cancelaciones evidentes.
>
> **Estrategia de éxito:**
>
> 1. **Elimina el parámetro** cuando sea posible y compara resultados.
> 2. **Verifica casos particulares**: evalúa en valores concretos de $t$ y comprueba la geometría.
> 3. **Simplifica** con identidades trigonométricas (especialmente de medio ángulo) y factoriza.
> 4. **Expresa en términos de $x$ o $y$** si el enunciado lo pide.

> [!tip] 🎓 Mnemotecnias y tabla de referencia
>
> **"dy sobre dx es dy/dt sobre dx/dt"**: el cociente de dos derivadas, punto.
>
> **Pasos "CDDD":**
>
> - **C**alcular $\frac{dx}{dt}$ y $\frac{dy}{dt}$.
> - **D**ividir: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$.
> - **D**eterminar los puntos especiales ($\frac{dx}{dt} = 0$ o $\frac{dy}{dt} = 0$).
> - **D**erivadas superiores si hace falta.
>
> **Casos especiales:**
>
> - $\frac{dy}{dt} = 0$, $\frac{dx}{dt} \neq 0$ → tangente horizontal.
> - $\frac{dy}{dt} \neq 0$, $\frac{dx}{dt} = 0$ → tangente vertical.
> - $\frac{dy}{dt} = 0$, $\frac{dx}{dt} = 0$ → punto singular.
>
> **Analogía:** la parametrización es el GPS de la curva: $t$ es el "tiempo" y dice dónde estamos; las derivadas paramétricas dan la dirección del movimiento.

> [!info] 📋 Curvas paramétricas más comunes
>
> | Curva | Ecuaciones paramétricas | $\frac{dy}{dx}$ | Casos especiales |
> |---|---|---|---|
> | **Círculo** | $x = r\cos(t)$, $y = r\operatorname{sen}(t)$ | $-\cot(t)$ | Tangente vertical en $t = 0, \pi$ |
> | **Elipse** | $x = a\cos(t)$, $y = b\operatorname{sen}(t)$ | $-\frac{b}{a}\cot(t)$ | Vértices en $t = 0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}$ |
> | **Parábola** | $x = t^2$, $y = 2at$ | $\frac{a}{t}$ | Tangente vertical en $t = 0$ |
> | **Cicloide** | $x = a(t-\operatorname{sen}t)$, $y = a(1-\cos t)$ | $\cot(t/2)$ | Cúspides en $t = 2\pi k$ |
> | **Hipérbola** | $x = a\sec(t)$, $y = b\tan(t)$ | $\frac{b}{a}\operatorname{sen}(t)$ | Asíntotas verticales |
>
> **Por qué importa:** la tabla da la respuesta directa para las curvas que más aparecen, y de paso indica dónde están los puntos especiales.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{dy}{dx}$ para $x = 3t$, $y = t^2$.
>
> > [!success]- ✅ Solución
> >
> > $\frac{dx}{dt} = 3$ y $\frac{dy}{dt} = 2t$.
> >
> > $$\frac{dy}{dx} = \frac{2t}{3}.$$
> >
> > **Respuesta:** $\frac{dy}{dx} = \frac{2t}{3}$.

> [!example] 📋 Planteamiento
>
> Calcula $\frac{dy}{dx}$ para $x = \cos(2t)$, $y = \operatorname{sen}(2t)$.
>
> > [!success]- ✅ Solución
> >
> > $\frac{dx}{dt} = -2\operatorname{sen}(2t)$ y $\frac{dy}{dt} = 2\cos(2t)$.
> >
> > $$\frac{dy}{dx} = \frac{2\cos(2t)}{-2\operatorname{sen}(2t)} = -\cot(2t).$$
> >
> > **Respuesta:** $-\cot(2t)$, válida donde $\operatorname{sen}(2t) \neq 0$.

> [!example] 📋 Planteamiento
>
> Halla $\frac{dy}{dx}$ para $x = e^t$, $y = e^{2t}$, y exprésala en función de $x$.
>
> > [!success]- ✅ Solución
> >
> > $\frac{dx}{dt} = e^t$ y $\frac{dy}{dt} = 2e^{2t}$.
> >
> > $$\frac{dy}{dx} = \frac{2e^{2t}}{e^t} = 2e^t.$$
> >
> > Como $x = e^t$, queda $\frac{dy}{dx} = 2x$.
> >
> > **Respuesta:** $2x$.

> [!example] 📋 Planteamiento
>
> Para $x = t^3 - 3t$, $y = t^2$, determina las tangentes horizontales y verticales.
>
> > [!success]- ✅ Solución
> >
> > $\frac{dx}{dt} = 3(t^2-1)$ y $\frac{dy}{dt} = 2t$.
> >
> > **Horizontales:** $\frac{dy}{dt} = 0 \Rightarrow t = 0$; como $\frac{dx}{dt} = -3 \neq 0$, la tangente en $(0, 0)$ es horizontal.
> >
> > **Verticales:** $\frac{dx}{dt} = 0 \Rightarrow t = \pm 1$; en $t = 1$ el punto es $(-2, 1)$ y en $t = -1$ es $(2, 1)$, y en ambos $\frac{dy}{dt} \neq 0$.
> >
> > **Respuesta:** tangente horizontal en $(0, 0)$ y tangentes verticales en $(-2, 1)$ y $(2, 1)$.

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d^2y}{dx^2}$ para $x = 2\cos(t)$, $y = 3\operatorname{sen}(t)$.
>
> > [!success]- ✅ Solución
> >
> > $\frac{dx}{dt} = -2\operatorname{sen}(t)$ y $\frac{dy}{dt} = 3\cos(t)$, luego
> >
> > $$\frac{dy}{dx} = \frac{3\cos t}{-2\operatorname{sen}t} = -\frac{3}{2}\cot(t).$$
> >
> > Derivando respecto a $t$: $\frac{d}{dt}\left(-\frac{3}{2}\cot t\right) = \frac{3}{2}\csc^2(t)$.
> >
> > Dividiendo por $\frac{dx}{dt} = -2\operatorname{sen}t$:
> >
> > $$\frac{d^2y}{dx^2} = \frac{\frac{3}{2}\csc^2(t)}{-2\operatorname{sen}t} = -\frac{3}{4\operatorname{sen}^3(t)}.$$
> >
> > **Respuesta:** $-\frac{3}{4\operatorname{sen}^3(t)}$.

> [!example] 📋 Planteamiento
>
> Para $x = \ln(t)$, $y = t^2$, calcula $\frac{dy}{dx}$ y exprésala en función de $x$.
>
> > [!success]- ✅ Solución
> >
> > $\frac{dx}{dt} = \frac{1}{t}$ y $\frac{dy}{dt} = 2t$.
> >
> > $$\frac{dy}{dx} = \frac{2t}{1/t} = 2t^2.$$
> >
> > Como $x = \ln t$, entonces $t = e^x$, y $t^2 = e^{2x}$.
> >
> > **Respuesta:** $\frac{dy}{dx} = 2e^{2x}$.

> [!example] 📋 Planteamiento
>
> Para $x = t^2 - 2t$, $y = t^3 - 3t$, analiza la concavidad de la curva.
>
> > [!success]- ✅ Solución
> >
> > $\frac{dx}{dt} = 2(t-1)$ y $\frac{dy}{dt} = 3(t^2-1) = 3(t-1)(t+1)$.
> >
> > Para $t \neq 1$:
> >
> > $$\frac{dy}{dx} = \frac{3(t-1)(t+1)}{2(t-1)} = \frac{3}{2}(t+1).$$
> >
> > Derivando respecto a $t$: $\frac{3}{2}$; dividiendo por $\frac{dx}{dt} = 2(t-1)$:
> >
> > $$\frac{d^2y}{dx^2} = \frac{3/2}{2(t-1)} = \frac{3}{4(t-1)}.$$
> >
> > **Respuesta:** la segunda derivada es positiva para $t > 1$ y negativa para $t < 1$: hay un cambio de concavidad en $t = 1$, que corresponde al punto $(x, y) = (-1, -2)$, donde la parametrización tiene $\frac{dx}{dt} = 0$ (rama vertical).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo la fórmula de la derivada paramétrica y justifico su origen en la regla de la cadena.
> - [ ] Calculo $\frac{dy}{dx}$ de una curva dada y lo verifico eliminando el parámetro.
> - [ ] Detecto tangentes horizontales y verticales a partir de $\frac{dy}{dt}$ y $\frac{dx}{dt}$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo la segunda derivada paramétrica con el método de tres pasos y con la fórmula directa.
> - [ ] Simplifico resultados con identidades de medio ángulo.
> - [ ] Expreso $\frac{dy}{dx}$ en función de $x$ o de $y$ cuando el enunciado lo pide.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Analizo puntos singulares y puntos de inflexión en curvas parametrizadas.
> - [ ] Aplico las fórmulas paramétricas de longitud de arco y área, cuidando el sentido de recorrido.
> - [ ] Interpreto $t$ como tiempo y relaciono las derivadas paramétricas con la velocidad y la aceleración.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 10: curvas paramétricas y longitud de arco.
> - R. Larson, *Cálculo* (Cengage), cap. 10: ecuaciones paramétricas y tangentes.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 3: pendiente de una curva parametrizada.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la base matemática del cociente.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — el método alternativo para verificar resultados.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — donde la longitud de arco paramétrica se aplica.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la fórmula de la derivada paramétrica?::$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{g'(t)}{f'(t)}$, válida cuando $f'(t) \neq 0$.
> - ¿Por qué esa fórmula?::Es la regla de la cadena: $\frac{dy}{dx} = \frac{dy}{dt}\cdot\frac{dt}{dx}$ y $\frac{dt}{dx} = \frac{1}{dx/dt}$.
> - ¿Cómo se calcula la segunda derivada paramétrica?::Se deriva $\frac{dy}{dx}$ **respecto a $t$** con la regla del cociente y se divide por $\frac{dx}{dt}$; o se usa $\frac{g''f' - g'f''}{[f']^3}$.
> - ¿Cuándo hay tangente vertical?::Cuando $\frac{dx}{dt} = 0$ y $\frac{dy}{dt} \neq 0$: la pendiente es infinita y no se puede dividir.
> - ¿Cómo se verifica un resultado paramétrico?:: Eliminando el parámetro y derivando de forma implícita, y comparando con el cociente obtenido.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — el fundamento del cociente.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — la vía alternativa para verificar.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/02 - Derivadas de Funciones Inversas|02 - Derivadas de Funciones Inversas]] — el otro caso en que no se puede despejar $y$.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]] — la idea de derivar dos veces, aplicada aquí al parámetro.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — la aplicación integral de estas derivadas.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — el mismo cambio de variable, en el mundo de las integrales.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 a 3: el cociente debe salirte sin vacilar.
> - Después salta al 4 (tangentes especiales) y al 5 (segunda derivada), que son los dos que aparecen en parciales.
> - Termina con el 7, donde el punto de inflexión coincide con una rama vertical: ese caso mixto es el que más confunde.
> - Cuando lo domines, conecta con [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|Longitud de Curva]], donde estas derivadas se integran.

---

**Tags:** #MATG1045 #unidad4 #derivadas-parametricas #ecuaciones-parametricas #regla-cadena #tangentes #curvatura #longitud-arco

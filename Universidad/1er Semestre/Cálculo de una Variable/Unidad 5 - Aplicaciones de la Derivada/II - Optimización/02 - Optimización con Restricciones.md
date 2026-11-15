---
dg-publish: true
tags: [MATG1045, unidad5, restricciones, sustitucion, lagrange, multiplicadores, curvas-de-nivel, precio-sombra, modelado]
---

# 🔒 Optimización con Restricciones

## 🎯 Introducción

> [!info] 💡 Cuándo el problema trae amarras
>
> Cuando una función objetivo no puede moverse libremente —hay un presupuesto, un volumen fijo, un material limitado— aparece la **optimización con restricciones**: maximizar o minimizar $f(x, y)$ sujeto a una condición $g(x, y) = 0$. Hay dos caminos: **sustitución** (usar la restricción para eliminar una variable) y **multiplicadores de Lagrange** (resolver sin eliminar nada, con un sistema).
>
> **Por qué importa:** los problemas reales casi nunca son libres: el presupuesto, la geometría y la física imponen restricciones. Saber elegir entre sustitución y Lagrange es la diferencia entre resolver en diez líneas o enredarse una hora.
>
> **Ejemplo:** maximizar el área $xy$ con perímetro $2x + 2y = 20$ se resuelve por sustitución en un par de líneas; maximizar la utilidad $x^{0.4}y^{0.6}$ con presupuesto $2x + 3y = 100$ es más limpio con Lagrange.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Método de sustitución
>
> El **método de sustitución** es la técnica más directa para restricciones de igualdad: se usa la restricción para eliminar una variable y convertir el problema en optimización sin restricciones. Procedimiento en seis pasos:
>
> 1. **Identificar** la función objetivo $f(x, y)$ y la restricción $g(x, y) = 0$.
> 2. **Despejar** una variable de la restricción: $y = h(x)$.
> 3. **Sustituir** en la función objetivo: $f(x, h(x)) = F(x)$.
> 4. **Optimizar** la función de una variable: $F'(x) = 0$.
> 5. **Encontrar** la otra variable volviendo a la restricción.
> 6. **Verificar** que sea máximo o mínimo.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Optimización_con_Restricciones_01.svg]]
>
> **Se lee así:** es una línea recta de rectángulos, sin decisiones ni ramas. Arranca con la función objetivo y la restricción, sigue por despejar una variable y sustituirla para quedarse con una función de una sola variable, deriva e iguala a cero, y termina calculando la variable que faltaba y verificando la naturaleza del extremo.
>
> **Por qué importa:** el diagrama muestra que la restricción no se ignora: se convierte en una fórmula para eliminar una variable. Si te saltas el paso de volver a la restricción para hallar la otra variable, no tienes el punto completo del problema.
>
> **Ejemplo:** en el rectángulo de área máxima con perímetro 20, despejas $y = 10 - x$, sustituyes en $A = xy$ para obtener $A(x) = 10x - x^2$ y el punto crítico $x = 5$.

> [!note] 📋 Definición — Multiplicadores de Lagrange
>
> Para optimizar $f(x, y)$ sujeto a $g(x, y) = 0$, se define la **función de Lagrange**
>
> $$L(x, y, \lambda) = f(x, y) - \lambda\, g(x, y),$$
>
> y se resuelve el sistema
>
> $$\frac{\partial L}{\partial x} = \frac{\partial f}{\partial x} - \lambda \frac{\partial g}{\partial x} = 0, \qquad \frac{\partial L}{\partial y} = \frac{\partial f}{\partial y} - \lambda \frac{\partial g}{\partial y} = 0, \qquad \frac{\partial L}{\partial \lambda} = -g(x, y) = 0.$$
>
> **Condición geométrica equivalente:** en el punto óptimo, $\nabla f = \lambda \nabla grad$… es decir, el gradiente de la función objetivo es **proporcional** al gradiente de la restricción, con $\lambda$ el **multiplicador de Lagrange**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Optimización_con_Restricciones_02.svg]]
>
> **Se lee así:** el diagrama decide por pasos: un rombo pregunta cuántas restricciones hay y otro si la restricción se puede despejar con facilidad. Con una sola restricción despejable se llega a una función de una variable y se resuelve con la derivada igualada a cero; si el despeje es difícil, la rama lleva al sistema con el multiplicador $\lambda$. Con varias restricciones, la ruta termina en un sistema complejo con varios multiplicadores.
>
> **Por qué importa:** elegir el método correcto antes de calcular ahorra horas: despejar puede volverse un desastre algebraico con varias restricciones. La comparación también muestra qué información extra da Lagrange, justamente el valor de $\lambda$.
>
> **Ejemplo:** para la utilidad $U(x, y) = x^{0.4} y^{0.6}$ con presupuesto $2x + 3y = 100$, hay una restricción difícil de despejar, así que toca la rama de Lagrange.

---

## 🔄 Método de sustitución en detalle

> [!warning] ⚖️ Cuándo usar sustitución
>
> **✅ Ideal cuando:**
>
> - La restricción es **fácil de despejar**.
> - Resulta en una función **simple de una variable**.
> - Hay **una sola restricción**.
>
> **❌ Evitar cuando:**
>
> - El despeje es **muy complejo** o genera expresiones irracionales complicadas.
> - Hay **múltiples restricciones** de igualdad.
>
> **Por qué importa:** la sustitución es rápida pero frágil: un despeje mal hecho contamina todo el problema. Si el despeje se complica, cambia de método antes de seguir.

> [!example] 📦 Ejemplo resuelto: área máxima con perímetro fijo
>
> **Enunciado:** hallar las dimensiones del rectángulo de área máxima cuyo perímetro es $20$.
>
> 1. **Variables:** $x$ = largo, $y$ = ancho.
> 2. **Objetivo:** maximizar $A(x, y) = xy$.
> 3. **Restricción:** $2x + 2y = 20$, es decir $x + y = 10$.
> 4. **Despeje:** $y = 10 - x$.
> 5. **Sustitución:** $A(x) = x(10 - x) = 10x - x^2$.
> 6. **Dominio:** $0 < x < 10$ (dimensiones positivas).
> 7. **Derivada:** $A'(x) = 10 - 2x = 0$ → $x = 5$.
> 8. **Otra variable:** $y = 10 - 5 = 5$.
> 9. **Verificación:** $A''(x) = -2 < 0$ → máximo.
>
> **Respuesta:** cuadrado de 5 × 5 unidades (área $25$).

> [!example] 📏 Ejemplo resuelto: punto más cercano a una recta
>
> **Enunciado:** hallar el punto de la recta $x + y = 1$ más cercano al origen.
>
> - **Objetivo:** minimizar $d^2(x, y) = x^2 + y^2$ (cuadrado de la distancia, para evitar la raíz).
> - **Restricción:** $y = 1 - x$.
> - **Sustitución:** $d^2(x) = x^2 + (1-x)^2 = 2x^2 - 2x + 1$.
> - **Derivada:** $(d^2)' = 4x - 2 = 0$ → $x = 1/2$, y $y = 1 - 1/2 = 1/2$.
> - **Verificación:** $(d^2)'' = 4 > 0$ → mínimo.
>
> **Respuesta:** el punto $(1/2, 1/2)$, a distancia $\sqrt{2}/2$ del origen.

---

## ⚖️ Multiplicadores de Lagrange

> [!success] 🧭 Filosofía del método
>
> Lagrange optimiza sin eliminar variables: en el punto óptimo, el gradiente de la función objetivo es **proporcional** al gradiente de la restricción,
>
> $$\nabla f = \lambda \nabla g.$$
>
> **Por qué importa:** es una condición necesaria que funciona igual con una o con diez restricciones, y su interpretación económica es rica: $\lambda$ mide cuánto cambiaría el valor óptimo si relajaras la restricción.

> [!info] 💰 Interpretación del multiplicador $\lambda$
>
> $\lambda$ representa la **tasa de cambio del valor óptimo** respecto a cambios en la restricción:
>
> - **$\lambda > 0$:** relajar la restricción **aumentaría** el valor óptimo.
> - **$\lambda < 0$:** relajarla lo **disminuiría**.
> - **$|\lambda|$:** magnitud del **precio sombra** de la restricción (lo que vale "una unidad más" de recurso).
>
> **Por qué importa:** en economía e ingeniería, $\lambda$ es el resultado más útil del problema: dice cuánto pagarías por una unidad extra de presupuesto o de material.
>
> **Ejemplo:** en el problema de maximizar $xy$ con $x + y = 10$ sale $\lambda = 5$: si el recurso pasara de $10$ a $11$, el valor máximo aumentaría aproximadamente en $5$ unidades.

> [!example] 🧮 Ejemplo introductorio con Lagrange
>
> **Enunciado:** maximizar $f(x, y) = xy$ sujeto a $x + y = 10$.
>
> 1. **Función de Lagrange:** $L(x, y, \lambda) = xy - \lambda(x + y - 10)$.
> 2. **Sistema:**
>
>    $$\frac{\partial L}{\partial x} = y - \lambda = 0 \Rightarrow y = \lambda, \qquad \frac{\partial L}{\partial y} = x - \lambda = 0 \Rightarrow x = \lambda, \qquad x + y = 10.$$
>
> 3. **Resolver:** de las dos primeras, $x = y = \lambda$; sustituyendo en la tercera, $2\lambda = 10$ → $\lambda = 5$.
> 4. **Solución:** $x = 5$, $y = 5$, $\lambda = 5$.
>
> **Interpretación:** si el recurso subiera de $10$ a $11$, el máximo pasaría de $25$ a aproximadamente $30$.

> [!tip] 📊 Comparación: sustitución vs. Lagrange
>
> | Aspecto | Sustitución | Lagrange |
> |---|---|---|
> | Complejidad algebraica | Variable | Constante |
> | Número de ecuaciones | $1$ | $n + m$ |
> | Información adicional | No | Sí ($\lambda$) |
> | Múltiples restricciones | Difícil | Natural |
> | Interpretación económica | Limitada | Rica |
>
> **Por qué importa:** la tabla es tu árbol de decisión: una restricción despejable y simple → sustitución; restricción difícil, varias condiciones o cuando te interesan las sensibilidades → Lagrange.

---

## 🛠 Problemas prácticos

> [!example] 🏗️ Diseño de tanque cilíndrico
>
> **Enunciado:** diseñar un tanque cilíndrico cerrado de volumen $1000$ m³ que minimice la superficie total.
>
> - Variables: $r$ = radio, $h$ = altura; objetivo $S = 2\pi r^2 + 2\pi r h$; restricción $\pi r^2 h = 1000$.
> - **Por sustitución:** $h = \frac{1000}{\pi r^2}$, así que $S(r) = 2\pi r^2 + \frac{2000}{r}$.
> - $S'(r) = 4\pi r - \frac{2000}{r^2} = 0$ → $4\pi r^3 = 2000$ → $r = \sqrt[3]{\frac{500}{\pi}} \approx 5{,}42$ m.
> - $h = \frac{1000}{\pi (5{,}42)^2} \approx 10{,}84$ m, es decir **$h = 2r$**: la altura óptima es igual al diámetro.
>
> **Por Lagrange:** $L = 2\pi r^2 + 2\pi r h - \lambda(\pi r^2 h - 1000)$; de $\frac{\partial L}{\partial h} = 2\pi r - \lambda \pi r^2 = 0$ sale $\lambda = \frac{2}{r}$, y sustituyendo en la de $r$ se llega igual a $h = 2r$.
>
> **Por qué importa:** los dos caminos dan lo mismo; el segundo es más simétrico y te entrega $\lambda$ de regalo.

> [!example] 💼 Optimización de producción (Lagrange)
>
> **Enunciado:** una empresa produce dos bienes con utilidad $U(x, y) = x^{0.4} y^{0.6}$ y presupuesto $2x + 3y = 100$.
>
> $$L = x^{0.4} y^{0.6} - \lambda(2x + 3y - 100),$$
>
> $$\frac{\partial L}{\partial x} = 0.4 x^{-0.6} y^{0.6} - 2\lambda = 0, \qquad \frac{\partial L}{\partial y} = 0.6 x^{0.4} y^{-0.4} - 3\lambda = 0.$$
>
> Despejando $\lambda$ en ambas e igualando: $\frac{0.4 y}{2x} = \frac{0.6 x}{3y}$ → $0{,}2\,y/x = 0{,}2\,x/y$ → $y^2 = x^2$, y siendo positivos, $y = x$.
>
> Sustituyendo en la restricción: $2x + 3x = 100$ → $x = 20$, $y = 20$.
>
> **Interpretación:** el consumidor óptimo gasta lo mismo en ambos bienes (aunque el presupuesto los pese distinto, la utilidad equilibra).

> [!warning] 🔧 Viga de resistencia máxima
>
> **Enunciado:** de un tronco de radio $R$, cortar una viga rectangular de máximo momento de resistencia.
>
> - Objetivo: $M = k\, w h^2$ (maximizar); restricción: $w^2 + h^2 = 4R^2$ (inscrita en el círculo).
> - **Solución:** $h = w\sqrt{2}$, es decir, altura = $\sqrt{2} \times$ ancho.
>
> **Por qué importa:** es el caso en que la restricción geométrica (la sección circular) es incómoda de despejar sin raíces: Lagrange la trata directamente.

> [!example] ✨ Principio de Fermat (reflexión de la luz)
>
> **Enunciado:** un rayo viaja de $A(0, a)$ a $B(d, b)$ reflejándose en el eje $x$; hallar el punto de reflexión que minimiza el tiempo.
>
> - Variable: $x$ = punto de reflexión; $T(x) = \frac{\sqrt{x^2 + a^2} + \sqrt{(d-x)^2 + b^2}}{c}$.
> - $\frac{dT}{dx} = \frac{1}{c}\left[\frac{x}{\sqrt{x^2 + a^2}} - \frac{d-x}{\sqrt{(d-x)^2 + b^2}}\right] = 0$.
> - Cada fracción es el seno de un ángulo, así que la condición es $\operatorname{sen}(\theta_1) = \operatorname{sen}(\theta_2)$.
>
> **Resultado:** ángulo de incidencia = ángulo de reflexión: la luz minimiza el tiempo.

---

## 📐 Interpretación geométrica

> [!tip] 👁️ Curvas de nivel y tangencia
>
> Las **curvas de nivel** de $f(x, y) = c$ son los conjuntos donde la función toma valor constante. **En el punto óptimo, la curva de nivel de la función objetivo es tangente a la curva de restricción.**
>
> **Por qué importa:** esa tangencia es la imagen que explica Lagrange: si las curvas se cortaran en vez de tocarse, podrías moverte a lo largo de la restricción ganando valor; solo en la tangencia no queda margen de mejora.
>
> **Ejemplo:** con objetivo $xy$ y restricción $x + y = 10$, las hipérbolas $xy = c$ se acercan a la recta hasta que en $c = 25$ quedan tangentes: ese es el máximo, en $(5, 5)$.

> [!warning] ⚖️ Condición de tangencia
>
> Dos curvas son tangentes cuando tienen la **misma recta tangente**, lo que ocurre cuando sus **vectores normales son paralelos**:
>
> - Vector normal a $f(x, y) = c$: $\nabla f = (\partial f/\partial x, \partial f/\partial y)$.
> - Vector normal a $g(x, y) = 0$: $\nabla g = (\partial g/\partial x, \partial g/\partial y)$.
> - **Condición:** $\nabla f = \lambda \nabla g$ (vectores paralelos).
>
> **Por qué importa:** ahí está la demostración geométrica del método: proporcionalidad de gradientes = tangencia de curvas de nivel con la restricción.

> [!info] 🖼️ Visualización de los casos
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Optimización_con_Restricciones_03.svg]]
>
> **Se lee así:** el diagrama parte de una entrada con dos ramas: la familia de curvas de nivel del objetivo y la curva única de la restricción. Ambas convergen en el recuadro de buscar tangencia, que desemboca en un rombo con tres salidas: tangencia externa, interna y punto de silla. Cada salida lleva a un recuadro con la consecuencia: no hay intersección, la curva de nivel encierra a la restricción, o hace falta la segunda derivada.
>
> **Por qué importa:** es la intuición detrás de Lagrange: el óptimo es donde la curva de nivel toca a la restricción, y el signo de $\lambda$ dice hacia dónde. Te sirve para entender por qué el método funciona y para interpretar el resultado cuando los números no tienen sentido.
>
> **Ejemplo:** en el ejemplo de $xy$ con $x + y = 10$, las hipérbolas se acercan a la recta hasta que en $c = 25$ quedan tangentes, y ese es el máximo en $(5, 5)$.

> [!example] 🔍 Casos geométricos y signo de $\lambda$
>
> - **Máximo interior:** las curvas de nivel rodean el punto óptimo y la restricción pasa por el mayor valor alcanzable.
> - **Mínimo interior:** el óptimo está en el "centro" de las curvas de nivel.
> - **Óptimo en frontera:** el punto puede estar en los extremos del dominio de la restricción y requiere análisis adicional.
> - **$\lambda > 0$:** $\nabla f$ y $\nabla g$ apuntan en la misma dirección; la función crece en la dirección que relaja la restricción (típico en maximización).
> - **$\lambda < 0$:** apuntan en direcciones opuestas (típico en minimización).
>
> **Intuición del gradiente:** $\nabla f$ apunta hacia el mayor crecimiento de $f$; $\nabla g$ es perpendicular a la curva de restricción. En el óptimo no es posible moverse a lo largo de la restricción para mejorar la función objetivo.
>
> **Restricciones múltiples:** con $g_1(x, y) = 0$ y $g_2(x, y) = 0$, la condición se generaliza a $\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2$: el gradiente de $f$ es combinación lineal de los gradientes de las restricciones, y el óptimo vive en la intersección de sus curvas.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Maximiza el área de un rectángulo con perímetro $20$ usando sustitución.
>
> > [!success]- ✅ Solución
> >
> > Restricción: $x + y = 10$ → $y = 10 - x$.
> >
> > Objetivo: $A(x) = x(10 - x) = 10x - x^2$, con $0 < x < 10$.
> >
> > $A'(x) = 10 - 2x = 0$ → $x = 5$; $A''(x) = -2 < 0$ → máximo.
> >
> > $y = 10 - 5 = 5$. **Respuesta:** cuadrado de 5 × 5, área $25$.

> [!example] 📋 Planteamiento
>
> Halla el punto de la recta $x + y = 1$ más cercano al origen.
>
> > [!success]- ✅ Solución
> >
> > Minimizar $d^2 = x^2 + y^2$ con $y = 1 - x$: $d^2(x) = 2x^2 - 2x + 1$.
> >
> > $(d^2)' = 4x - 2 = 0$ → $x = 1/2$, y $y = 1/2$.
> >
> > $(d^2)'' = 4 > 0$ → mínimo. **Respuesta:** punto $(1/2, 1/2)$, distancia $\sqrt{2}/2$.

> [!example] 📋 Planteamiento
>
> Maximiza $f(x, y) = xy$ sujeto a $x + y = 10$ con multiplicadores de Lagrange e interpreta $\lambda$.
>
> > [!success]- ✅ Solución
> >
> > $L = xy - \lambda(x + y - 10)$; sistema: $y - \lambda = 0$, $x - \lambda = 0$, $x + y = 10$.
> >
> > De las dos primeras, $x = y = \lambda$; en la tercera, $2\lambda = 10$ → $\lambda = 5$.
> >
> > **Respuesta:** $(5, 5)$ con valor $25$; $\lambda = 5$ significa que una unidad extra de recurso elevaría el máximo en unas $5$ unidades (precio sombra).

> [!example] 📋 Planteamiento
>
> Diseña un tanque cilíndrico cerrado de volumen $1000$ m³ que minimice el material.
>
> > [!success]- ✅ Solución
> >
> > $S(r) = 2\pi r^2 + \frac{2000}{r}$ (tras despejar $h = 1000/(\pi r^2)$).
> >
> > $S'(r) = 4\pi r - \frac{2000}{r^2} = 0$ → $r^3 = \frac{500}{\pi}$ → $r \approx 5{,}42$ m.
> >
> > $h = \frac{1000}{\pi r^2} \approx 10{,}84$ m = $2r$.
> >
> > $S''(r) = 4\pi + \frac{4000}{r^3} > 0$ → mínimo. **Respuesta:** $r \approx 5{,}42$ m y $h \approx 10{,}84$ m.

> [!example] 📋 Planteamiento
>
> Una empresa tiene utilidad $U(x, y) = x^{0.4} y^{0.6}$ y presupuesto $2x + 3y = 100$. Halla la mezcla óptima.
>
> > [!success]- ✅ Solución
> >
> > $L = x^{0.4}y^{0.6} - \lambda(2x + 3y - 100)$; derivadas parciales:
> >
> > $0.4x^{-0.6}y^{0.6} = 2\lambda$ y $0.6x^{0.4}y^{-0.4} = 3\lambda$.
> >
> > Despejando $\lambda$ e igualando: $\frac{0.4y}{2x} = \frac{0.6x}{3y}$ → $y^2 = x^2$ → $y = x$ (valores positivos).
> >
> > En la restricción: $2x + 3x = 100$ → $x = 20$, $y = 20$.
> >
> > **Respuesta:** comprar 20 unidades de cada bien (gasto igual en ambos).

> [!example] 📋 Planteamiento
>
> ¿Qué método usarías para cada uno y por qué?
>
> a) Maximizar $A = xy$ con $2x + 2y = 20$.
> b) Maximizar $U = x^{0.4}y^{0.6}$ con $2x + 3y = 100$.
> c) Minimizar $S = 2\pi r^2 + 2\pi rh$ con $\pi r^2 h = 1000$ y además $h \leq 2r$.
>
> > [!success]- ✅ Solución
> >
> > **a) Sustitución:** una restricción lineal, despeje trivial ($y = 10 - x$), función de una variable.
> >
> > **b) Lagrange:** la restricción es lineal y se podría despejar, pero la utilidad con potencias fraccionarias se vuelve incómoda; además $\lambda$ da información económica útil.
> >
> > **c) Lagrange con revisión de frontera:** dos condiciones (igualdad y desigualdad $h \leq 2r$); se resuelve el caso de igualdad y luego se comprueba si el óptimo cae dentro de la desigualdad o en su frontera $h = 2r$.
>
> > **Lección:** la elección del método es parte de la solución; el checklist SUSTLAG (despeje simple → sustitución; despeje largo, muchas restricciones o gradientes fáciles → Lagrange) te guía.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico los seis pasos del método de sustitución a una restricción lineal.
> - [ ] Escribo la función de Lagrange y su sistema de ecuaciones para un problema dado.
> - [ ] Interpreto el multiplicador $\lambda$ como precio sombra de la restricción.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Elijo correctamente entre sustitución y Lagrange según el árbol de decisión de la nota.
> - [ ] Resuelvo problemas de diseño (tanque, viga) con ambas vías y comparo los resultados.
> - [ ] Explico la condición $\nabla f = \lambda \nabla g$ con el argumento de la tangencia de curvas de nivel.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Interpreto el signo y la magnitud de $\lambda$ en un problema económico concreto.
> - [ ] Trato restricciones múltiples con la combinación lineal de gradientes.
> - [ ] Detecto cuándo el óptimo cae en la frontera del dominio de la restricción y lo verifico.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 14: optimización con restricciones y multiplicadores de Lagrange.
> - R. Larson, *Cálculo* (Cengage), cap. 13: método de Lagrange con aplicaciones.
> - T. Apostol, *Calculus, Vol. 2* (Wiley), cap. 12: extremos con restricciones.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — la optimización sin restricciones que aquí se complementa.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — herramientas para verificar la naturaleza de los extremos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — el test de la segunda derivada.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuáles son los seis pasos del método de sustitución?::Identificar objetivo y restricción, despejar una variable, sustituir, derivar e igualar a cero, hallar la otra variable y verificar máximo o mínimo.
> - ¿Qué dice la condición de Lagrange?::Que en el óptimo $\nabla f = \lambda \nabla g$: el gradiente del objetivo es proporcional al de la restricción, es decir, sus curvas de nivel son tangentes.
> - ¿Qué representa el multiplicador $\lambda$?::La tasa de cambio del valor óptimo si se relaja la restricción; su valor absoluto es el precio sombra del recurso.
> - ¿Cuándo conviene Lagrange en vez de sustitución?::Cuando el despeje es largo o incómodo, cuando hay varias restricciones o cuando se quiere interpretar económicamente $\lambda$.
> - ¿Qué relación geométrica tiene el punto óptimo con las curvas de nivel?::La curva de nivel del objetivo es tangente a la curva de la restricción; si se cortaran, habría margen para mejorar moviéndose por la restricción.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — la base de modelado y verificación sin restricciones.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — puntos críticos y extremos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — segunda derivada para clasificar.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — restricciones que cambian con el tiempo.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — cómo la derivada y la integral cierran el círculo del cálculo.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — optimización de áreas con integración.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los dos ejemplos de sustitución hasta que el despeje y el regreso a la restricción sean automáticos.
> - Después salta a los ejemplos con Lagrange: empieza por $xy$ con $x + y = 10$, que es el caso más limpio.
> - Cuando domines los dos métodos, resuelve el ejercicio de decisión (a, b, c): ahí se concentra el criterio completo de la nota.
> - En cada problema, escribe antes de calcular **qué método eliges y por qué**, y termina interpretando **qué significa $\lambda$**.

---

**Tags:** #MATG1045 #unidad5 #restricciones #sustitucion #lagrange #multiplicadores #curvas-de-nivel #precio-sombra #modelado

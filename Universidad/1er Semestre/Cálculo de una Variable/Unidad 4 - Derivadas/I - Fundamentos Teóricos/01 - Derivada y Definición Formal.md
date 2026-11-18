---
dg-publish: true
tags: [MATG1045, unidad4, derivada, definicion-formal, limite-incremental, recta-tangente, velocidad-instantanea, no-derivabilidad, mnemotecnia]
---

# 📈 Derivada y Definición Formal

## 🎯 Introducción

> [!quote] 💬 Cita de Gilbert Strang
>
> _"La derivada es el concepto más importante de todo el cálculo. Es la velocidad instantánea, la pendiente de la tangente, la razón de cambio... es el lenguaje con el que la naturaleza describe el cambio."_

> [!info] 💡 El concepto fundamental
>
> La **derivada** es el límite de la razón de cambio promedio cuando el intervalo se aproxima a cero. Conecta la geometría (pendiente de la recta tangente) con la física (velocidad instantánea) de manera elegante, y es el concepto del que dependen todas las reglas de derivación, el análisis de funciones y la optimización.
>
> **Interpretaciones principales:**
>
> - **Geométrica:** pendiente de la recta tangente a la curva en el punto.
> - **Física:** velocidad instantánea, o razón de cambio de una magnitud respecto a otra.
> - **Algebraica:** límite de los cocientes de diferencias $\frac{f(x+h)-f(x)}{h}$ cuando $h \to 0$.
>
> **Por qué importa:** una sola fórmula, el límite del cociente incremental, describe tanto la pendiente de una curva como la velocidad de un objeto. Quien entiende esa idea no memoriza reglas: las deriva.
>
> **Ejemplo:** en $f(x) = x^2$ la pendiente en $x = 2$ es $4$; si el objeto sigue esa función de posición, a los $2$ segundos viaja a $4$ unidades por segundo.

> [!warning] 🔬 Dónde se usa la derivada
>
> - **En física:** velocidad $v(t) = s'(t)$, aceleración $a(t) = v'(t) = s''(t)$, corriente $I = dQ/dt$.
> - **En geometría:** pendiente de tangentes, razón de cambio de área o volumen, curvatura.
> - **En optimización:** máximos y mínimos vía puntos críticos $f'(x) = 0$ y concavidad con $f''(x)$.
>
> **Por qué importa:** estas tres familias de problemas son las que aparecen en los exámenes de la unidad, y las tres se resuelven con la misma herramienta.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Derivada (por límite)
>
> Sea $f(x)$ una función definida en un intervalo que contiene a $x = a$. La **derivada de $f$ en $x = a$** es
>
> $$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h},$$
>
> **siempre que este límite exista y sea finito**. Formas equivalentes:
>
> $$f'(a) = \lim_{\Delta x \to 0} \frac{f(a + \Delta x) - f(a)}{\Delta x}, \qquad f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}, \qquad f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivada_y_Definición_Formal_02.svg]]
>
> **Se lee así:** es una cadena de rectángulos que baja paso a paso: se parte de una función, se toman dos puntos cercanos, se calcula la pendiente de la secante que los une, se toma el límite cuando el incremento se hace cero y se llega a la pendiente de la tangente. Cada eslabón explica una parte del cociente de la definición.
>
> **Por qué importa:** así ves la fórmula $\frac{f(a+h)-f(a)}{h}$ como una pendiente real y no como un símbolo abstracto. Esta intuición es la que después usas para aproximar con tangentes y para justificar cuándo la derivada existe.
>
> **Ejemplo:** con $f(x) = x^2$ en $x = 2$, las pendientes secantes $5$, $4.1$, $4.01$ y $4.001$ (para $h = 1$, $0.1$, $0.01$, $0.001$) se acercan a $f'(2) = 4$.

> [!note] 📋 Definición — Existencia de la derivada
>
> Para que $f'(a)$ exista hacen falta tres condiciones:
>
> 1. $f$ debe estar **definida** en un entorno de $a$.
> 2. El límite del cociente incremental debe **existir**, es decir, los dos laterales deben coincidir.
> 3. El límite debe ser **finito**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivada_y_Definición_Formal_03.svg]]
>
> **Se lee así:** es un árbol de decisiones: un rombo pregunta si la función es continua en el punto y, si no, cierra ahí; si es continua, un segundo rombo compara los límites laterales de la derivada y un tercero pregunta si el límite es finito. Cada rama termina en una caja con el diagnóstico: no existe por discontinuidad, por esquina o por tangente vertical, o bien la derivada sí existe.
>
> **Por qué importa:** es el filtro que te dice qué revisar primero cuando una derivada no aparece: primero continuidad, luego lados, después finitud. Así evitas afirmar que $f'(a)$ existe sin comprobar que el límite sea finito.
>
> **Ejemplo:** para $f(x) = \sqrt[3]{x}$ en $x = 0$ el diagrama lleva a la última rama fallida: el límite es infinito, así que hay tangente vertical y la derivada no existe.

---

## 🔢 Notaciones de la derivada

> [!info] ✍️ Las cinco formas de escribir una derivada
>
> | Notación | Nombre | Uso principal |
> |---|---|---|
> | $f'(x)$ | Lagrange | Matemáticas puras y funciones generales |
> | $\frac{dy}{dx}$ | Leibniz | Física y aplicaciones; énfasis en variables |
> | $\frac{df}{dx}$ | Leibniz | Funciones específicas |
> | $\dot{y}$ | Newton | Física (derivada respecto al tiempo) |
> | $D_x f$, $Df(x)$ | Operador | Análisis funcional y derivadas parciales |
>
> **Derivadas de orden superior:** segunda $f''(x)$, $\frac{d^2y}{dx^2}$, $\ddot{y}$; $n$-ésima $f^{(n)}(x)$, $\frac{d^ny}{dx^n}$.
>
> **Por qué importa:** en los exámenes conviven las tres notaciones. Reconocer cuál es cuál evita leer una derivada segunda como dos primeras.

> [!warning] 🎯 Qué significa (y qué no) $\frac{dy}{dx}$
>
> - **NO** es una fracción literal: es el límite de $\frac{\Delta y}{\Delta x}$ cuando $\Delta x \to 0$.
> - **SÍ** se comporta como razón de cambio, y por eso la regla de la cadena "se cancela" como si fuera una fracción.
> - **Es flexible** para manipular algebraicamente en ecuaciones diferenciales.
>
> **Por qué importa:** entenderlo como razón de cambio es lo que hace posible la regla de la cadena y la derivación implícita más adelante.
>
> **Ejemplo:** $\frac{dy}{dx} = 3x^2$ se lee "la variable $y$ cambia $3x^2$ veces por cada unidad de $x$".

---

## 🎨 Interpretación geométrica y física

> [!tip] 🎯 De la secante a la tangente
>
> 1. **Recta secante:** une dos puntos $(a, f(a))$ y $(a+h, f(a+h))$.
> 2. **Pendiente secante:** $m_{sec} = \frac{f(a+h) - f(a)}{h}$.
> 3. **Límite:** cuando $h \to 0$, el punto $(a+h, f(a+h))$ se acerca a $(a, f(a))$.
> 4. **Recta tangente:** la secante se convierte en la tangente.
> 5. **Derivada:** $f'(a)$ es la pendiente de la recta tangente.
>
> **Pendientes secantes de $f(x) = x^2$ en $x = 2$:**
>
> | $h$ | $f(2+h)$ | Cociente $\frac{f(2+h)-f(2)}{h}$ | Pendiente |
> |---|---|---|---|
> | $1$ | $9$ | $\frac{9-4}{1}$ | $5$ |
> | $0.1$ | $4.41$ | $\frac{4.41-4}{0.1}$ | $4.1$ |
> | $0.01$ | $4.0401$ | $\frac{4.0401-4}{0.01}$ | $4.01$ |
> | $0.001$ | $4.004001$ | $\frac{4.004001-4}{0.001}$ | $4.001$ |
>
> **Observación:** las pendientes se acercan a $4$, por lo tanto $f'(2) = 4$.
>
> **Por qué importa:** esta tabla es la derivada "a la vista": muestra cómo el cociente incremental converge y por qué la tangente tiene pendiente $4$ y no $5$.

> [!warning] 📐 Ecuación de la recta tangente
>
> Si $f'(a)$ existe, la recta tangente a $y = f(x)$ en el punto $(a, f(a))$ es
>
> $$y - f(a) = f'(a)(x - a), \qquad \text{o bien} \qquad y = f(a) + f'(a)(x - a).$$
>
> **Por qué importa:** es la aplicación geométrica directa de la derivada: sin $f'(a)$ no hay tangente, y con ella cualquier problema de aproximación lineal se convierte en una recta.
>
> **Ejemplo:** para $f(x) = x^2$ en $x = 2$: $y - 4 = 4(x - 2)$, es decir $y = 4x - 4$.

> [!info] 🏃 Velocidad instantánea
>
> Si $s(t)$ es la posición de un objeto en el instante $t$:
>
> - **Velocidad promedio** en $[t, t+h]$: $v_{prom} = \frac{s(t+h) - s(t)}{h}$.
> - **Velocidad instantánea** en $t$: $v(t) = s'(t) = \lim_{h \to 0} \frac{s(t+h) - s(t)}{h}$.
>
> **Ejemplo (caída libre):** con $g = 9.8$ m/s², $v_0 = 10$ m/s y $s_0 = 0$, $s(t) = -4.9t^2 + 10t$. Entonces
>
> $$v(2) = \lim_{h \to 0} \frac{[-4.9(2+h)^2 + 10(2+h)] - [-4.9(4) + 20]}{h} = \lim_{h \to 0} (-9.6 - 4.9h) = -9.6 \text{ m/s}.$$
>
> **Por qué importa:** el signo negativo indica que a los $2$ segundos el objeto desciende a $9.6$ m/s. Es la misma fórmula que la pendiente geométrica, aplicada al tiempo.
>
> **Interpretación física completa:** velocidad $v(t) = x'(t)$, aceleración $a(t) = v'(t) = x''(t)$, corriente eléctrica $I = dQ/dt$.

---

## 🧮 Cálculo de derivadas por la definición

> [!tip] 📋 Metodología en cinco pasos
>
> 1. **Escribir** la definición: $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$.
> 2. **Sustituir** $f(x+h)$ y $f(x)$.
> 3. **Simplificar** la expresión algebraicamente.
> 4. **Factorizar** para cancelar $h$ del denominador.
> 5. **Evaluar** el límite cuando $h \to 0$.
>
> **Por qué importa:** el paso 4 es el corazón del método: sin cancelar el $h$ no hay límite que tomar. Si el $h$ no se cancela, la función no es derivable ahí.
>
> **Ejemplo:** en $f(x) = x^2$ el numerador $2xh + h^2$ se factoriza como $h(2x+h)$ y el $h$ se cancela con el denominador.

> [!example] 📈 Función lineal: $f(x) = 3x + 2$
>
> $$f'(x) = \lim_{h \to 0} \frac{[3(x+h) + 2] - [3x + 2]}{h} = \lim_{h \to 0} \frac{3h}{h} = \lim_{h \to 0} 3 = 3.$$
>
> **Conclusión:** $f'(x) = 3$, la pendiente constante de la recta.

> [!example] 📊 Función cuadrática: $f(x) = x^2$
>
> $$f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = \lim_{h \to 0} (2x + h) = 2x.$$
>
> **Conclusión:** $f'(x) = 2x$; en $x = 2$ la pendiente es $4$, como predice la tabla de la sección geométrica.

> [!example] 🌿 Función con raíz: $f(x) = \sqrt{x}$, $x > 0$
>
> Se racionaliza multiplicando por el conjugado:
>
> $$f'(x) = \lim_{h \to 0} \frac{\sqrt{x+h} - \sqrt{x}}{h} \cdot \frac{\sqrt{x+h} + \sqrt{x}}{\sqrt{x+h} + \sqrt{x}} = \lim_{h \to 0} \frac{1}{\sqrt{x+h} + \sqrt{x}} = \frac{1}{2\sqrt{x}}.$$
>
> **Conclusión:** $f'(x) = \frac{1}{2\sqrt{x}}$. La racionalización es el truco que permite cancelar el $h$.

> [!tip] 🎓 Mnemotecnia "DELTA"
>
> - **D — Definir el límite:** escribe $f'(a) = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h}$ y verifica que $f$ esté definida cerca de $a$.
> - **E — Expandir y sustituir:** calcula $f(a+h)$ y sustituye; simplifica el numerador.
> - **L — Limpiar la expresión:** factoriza y cancela el $h$ del denominador.
> - **T — Tomar el límite:** evalúa $h \to 0$ y comprueba que el resultado sea finito.
> - **A — Asegurar e interpreta:** ¿tiene sentido? ¿qué significa geométrica o físicamente?
>
> **Aplicación a $f(x) = x^3$:** $f(x+h) = x^3 + 3x^2h + 3xh^2 + h^3$, se cancela $h$ y queda $\lim_{h \to 0} (3x^2 + 3xh + h^2) = 3x^2$. Verificación: en $x = 2$ la pendiente es $3(4) = 12$.

> [!success] ✅ Tres formas de verificar tu derivada
>
> 1. **Numérica:** usa $\frac{f(x+h)-f(x)}{h}$ con $h$ muy pequeño y compara con tu resultado.
> 2. **Por integración:** si $F'(x) = f(x)$, entonces $\int f(x)\,dx$ debe devolverte $F(x) + C$.
> 3. **Gráfica:** grafica $f$ y $f'$; donde $f'(x) = 0$, $f$ debe tener extremos.
>
> **Por qué importa:** verificar antes de entregar un ejercicio cuesta segundos y evita el error más común: una regla mal aplicada que ni siquiera produce una curva con el signo correcto.

---

## ⚡ Reglas y tipos de derivación

> [!success] ✅ Reglas algebraicas
>
> **Reglas básicas:**
>
> $$\text{Constante: } (c)' = 0, \qquad \text{Identidad: } (x)' = 1, \qquad \text{Potencia: } (x^n)' = n x^{n-1}, \qquad \text{Múltiplo: } (c f)' = c f'.$$
>
> **Combinaciones:**
>
> $$(f + g)' = f' + g', \qquad (f - g)' = f' - g', \qquad (fg)' = f'g + fg', \qquad \left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}.$$
>
> **Regla de la cadena:**
>
> $$\big(f(g(x))\big)' = f'(g(x)) \cdot g'(x).$$
>
> **Por qué importa:** estas siete reglas sustituyen a la definición en el 99% de los ejercicios; la definición queda para demostrarlas y para los casos raros.
>
> **Ejemplo:** $\left(\frac{1}{x}\right)' = \left(x^{-1}\right)' = -x^{-2} = -\frac{1}{x^2}$, aplicando la potencia con exponente negativo.

> [!info] 🔢 Funciones elementales y sus derivadas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivada_y_Definición_Formal_01.svg]]
>
> **Se lee así:** arriba hay una caja rectangular que se abre en tres ramas paralelas, y cada rama vuelve a partirse en dos cajas rectangulares con la fórmula de la derivada correspondiente. La idea visual es que las funciones especiales se agrupan por familias y que cada familia tiene sus propias derivadas ya resueltas en la hoja.
>
> **Por qué importa:** es una tabla de consulta rápida: cuando aparece $\ln x$ o $\tan x$ ya sabes qué fórmula aplicar sin derivar desde cero. Te evita además el error clásico de olvidar el factor $\ln a$ en la base exponencial.
>
> **Ejemplo:** $\frac{d}{dx}[\log_5 x] = \frac{1}{x \ln 5}$; se toma la rama de logarítmicas y se aplica sin volver a la definición.
>
> **Trigonométricas inversas:**
>
> $$(\arcsin x)' = \frac{1}{\sqrt{1-x^2}}, \qquad (\arccos x)' = -\frac{1}{\sqrt{1-x^2}}, \qquad (\arctan x)' = \frac{1}{1+x^2}.$$

> [!info] 🔄 Los cuatro tipos de derivación
>
> 1. **Explícita:** $y = f(x)$; aplicación directa de las reglas.
> 2. **Implícita:** ecuación $F(x,y) = 0$; se deriva ambos lados respecto a $x$ y se despeja $dy/dx$.
> 3. **Logarítmica:** para $f(x)^{g(x)}$; se aplica $\ln$ a ambos lados y se deriva implícitamente.
> 4. **Paramétrica:** con $x = f(t)$, $y = g(t)$, $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$.
>
> **Por qué importa:** elegir el tipo correcto es la mitad del problema. Reconocer $f(x)^{g(x)}$ de entrada te ahorra diez minutos de álgebra fallida.

> [!tip] 🎓 Mnemotecnia "DERIVAR"
>
> - **D** — **Detectar** el tipo de función.
> - **E** — **Elegir** la regla apropiada.
> - **R** — **Recordar** la fórmula base.
> - **I** — **Identificar** funciones compuestas.
> - **V** — **Verificar** aplicando la regla de la cadena.
> - **A** — **Aplicar** las reglas algebraicas.
> - **R** — **Revisar** y simplificar el resultado.
>
> **Pasos de apoyo:** identifica la estructura (¿suma, producto, composición?), clasifica las funciones, aplica las reglas en orden, simplifica y, si puedes, verifica derivando hacia atrás.

---

## ⚠️ Casos donde la derivada no existe

> [!warning] 🔴 Caso 1: discontinuidad
>
> $$f(x) = \begin{cases} x & \text{si } x < 1 \\ x+1 & \text{si } x \geq 1 \end{cases}$$
>
> En $x = 1$ la función es discontinua, por lo tanto no es derivable. **Regla general:** la continuidad es condición necesaria de la derivabilidad (nunca suficiente).

> [!warning] 🔴 Caso 2: esquina o cúspide
>
> Para $f(x) = |x|$ en $x = 0$:
>
> - Derivada por la izquierda: $\lim_{h \to 0^-} \frac{|h|}{h} = -1$.
> - Derivada por la derecha: $\lim_{h \to 0^+} \frac{|h|}{h} = 1$.
>
> Como $-1 \neq 1$, $f'(0)$ no existe. **La función es continua, pero no derivable.**

> [!warning] 🔴 Caso 3: tangente vertical
>
> Para $f(x) = \sqrt[3]{x}$ en $x = 0$:
>
> $$f'(0) = \lim_{h \to 0} \frac{\sqrt[3]{h}}{h} = \lim_{h \to 0} \frac{1}{h^{2/3}} = +\infty.$$
>
> El límite es infinito, por lo tanto la derivada no existe: hay tangente vertical. **El límite debe ser finito**, por eso la tercera condición de existencia.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = 3x + 2$ usando la definición por límite.
>
> > [!success]- ✅ Solución
> >
> > $$f'(x) = \lim_{h \to 0} \frac{[3(x+h) + 2] - [3x + 2]}{h} = \lim_{h \to 0} \frac{3x + 3h + 2 - 3x - 2}{h} = \lim_{h \to 0} \frac{3h}{h} = 3.$$
> >
> > Respuesta: $f'(x) = 3$, la pendiente constante de la recta.

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = x^2$ usando la definición por límite y calcula la pendiente en $x = 5$.
>
> > [!success]- ✅ Solución
> >
> > $$f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = \lim_{h \to 0} (2x + h) = 2x.$$
> >
> > En $x = 5$: $f'(5) = 10$. Respuesta: $f'(x) = 2x$ y la pendiente en $5$ es $10$.

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = \sqrt{x}$ para $x > 0$ usando la definición y racionalizando.
>
> > [!success]- ✅ Solución
> >
> > $$f'(x) = \lim_{h \to 0} \frac{\sqrt{x+h} - \sqrt{x}}{h} \cdot \frac{\sqrt{x+h} + \sqrt{x}}{\sqrt{x+h} + \sqrt{x}} = \lim_{h \to 0} \frac{(x+h) - x}{h(\sqrt{x+h} + \sqrt{x})} = \lim_{h \to 0} \frac{1}{\sqrt{x+h} + \sqrt{x}}.$$
> >
> > Cancelado el $h$ y tomando el límite: $f'(x) = \frac{1}{2\sqrt{x}}$. En $x = 4$ la pendiente es $1/4$.

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = x^3$ con el método DELTA y verifica el resultado en $x = 2$.
>
> > [!success]- ✅ Solución
> >
> > **D:** $f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$.
> >
> > **E:** $f(x+h) = x^3 + 3x^2h + 3xh^2 + h^3$, así que $f'(x) = \lim_{h \to 0} \frac{3x^2h + 3xh^2 + h^3}{h}$.
> >
> > **L:** factorizando, $= \lim_{h \to 0} \frac{h(3x^2 + 3xh + h^2)}{h} = \lim_{h \to 0} (3x^2 + 3xh + h^2)$.
> >
> > **T:** $= 3x^2$.
> >
> > **A:** $f'(x) = 3x^2$; en $x = 2$ la pendiente es $3(4) = 12$, que coincide con la gráfica de $y = x^3$.

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = x^2 \sin(x)$ con la regla del producto.
>
> > [!success]- ✅ Solución
> >
> > $(fg)' = f'g + fg'$ con $f = x^2$, $f' = 2x$, $g = \sin x$, $g' = \cos x$.
> >
> > $$f'(x) = 2x \sin(x) + x^2 \cos(x).$$
> >
> > **Verificación:** en $x = 0$ da $0$, coherente con que la curva tiene tangente horizontal en el origen.

> [!example] 📋 Planteamiento
>
> Deriva $h(x) = \sin(x^3 + 2x)$ con la regla de la cadena.
>
> > [!success]- ✅ Solución
> >
> > Función externa: $\sin(u)$ con derivada $\cos(u)$. Función interna: $u = x^3 + 2x$ con derivada $3x^2 + 2$.
> >
> > $$h'(x) = \cos(x^3 + 2x) \cdot (3x^2 + 2).$$
> >
> > **Regla general:** $\big(f(g(x))\big)' = f'(g(x)) \cdot g'(x)$; nunca se olvida el factor derivado de la función interna.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo la definición por límite de la derivada y sus tres formas equivalentes.
> - [ ] Distingo las notaciones de Lagrange, Leibniz y Newton y sé cuándo se usa cada una.
> - [ ] Interpreto la derivada como pendiente de tangente y como velocidad instantánea.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo derivadas de funciones lineales, cuadráticas y con raíz usando la definición.
> - [ ] Aplico las reglas algebraicas, la regla del producto, del cociente y de la cadena.
> - [ ] Escribo la ecuación de la recta tangente en un punto dado.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro con los laterales por qué una derivada no existe (esquina, discontinuidad, tangente vertical).
> - [ ] Verifico una derivada por método numérico, por integración o graficamente.
> - [ ] Elijo el tipo de derivación adecuado (explícita, implícita, logarítmica o paramétrica) según la forma de la función.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2: la derivada como límite y sus interpretaciones.
> - R. Larson, *Cálculo* (Cengage), cap. 2: derivadas por definición y reglas básicas.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 5: construcción analítica de la derivada.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — el límite del que nace todo.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — las reglas vistas aquí, con más práctica.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — la relación teórica completa entre ambas propiedades.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cómo se define la derivada de $f$ en $a$?::$f'(a) = \lim_{h \to 0} \frac{f(a+h)-f(a)}{h}$, siempre que el límite exista y sea finito.
> - ¿Qué significa geométricamente $f'(a)$?::La pendiente de la recta tangente a la curva $y = f(x)$ en el punto $(a, f(a))$; la ecuación es $y - f(a) = f'(a)(x-a)$.
> - ¿Qué tres condiciones se necesitan para que exista $f'(a)$?::$f$ definida cerca de $a$, el límite del cociente incremental existente (laterales iguales) y el límite finito.
> - ¿Cuándo una función continua no es derivable?::En esquinas y cúspides, como $|x|$ en $0$: los laterales de la derivada valen $-1$ y $1$ y no coinciden.
> - ¿Cuál es la regla de la cadena?::$\big(f(g(x))\big)' = f'(g(x)) \cdot g'(x)$: derivada de la externa evaluada en la interna, por la derivada de la interna.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — el límite del que nace la derivada.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — continuidad como condición necesaria de derivabilidad.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — la lectura visual del concepto, en detalle.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — la relación teórica entre ambas.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — métodos eficientes a partir de esta definición.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la composición, tratada aparte.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — problemas dinámicos.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/03 - Aproximaciones Lineales y Diferenciales|03 - Aproximaciones Lineales y Diferenciales]] — uso de la tangente para aproximar.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — el proceso inverso de la derivación.
>
> **Panorama de la definición:**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivada_y_Definición_Formal_04.svg]]
>
> **Se lee así:** un cuadro raíz "Definición Derivada" despliega cinco subgrafos de rectángulos: la interpretación geométrica, la física, los métodos de cálculo, la existencia de la derivada y las aplicaciones. Cada subgrafo agrupa las hojas que se apoyan en la definición, como la pendiente tangente, la cancelación de $h$ o la continuidad necesaria.
>
> **Por qué importa:** te sirve como panorama: la definición no es un trámite, es la base de todo lo que viene después, incluidas las derivadas de orden superior y las parciales. También te muestra qué rama conviene repasar antes de un parcial.
>
> **Ejemplo:** siguiendo la rama de métodos, el paso de cancelar $h$ en $\lim_{h \to 0}\frac{f(x+h)-f(x)}{h}$ es lo que permite después demostrar la regla del producto.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica la derivación por definición con los tres ejemplos de esta nota hasta que la cancelación del $h$ sea automática.
> - Después salta a [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|Reglas Fundamentales de Derivación]] para derivar sin volver a la definición.
> - La composición merece su propia nota: ve a [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|Regla de la Cadena]] antes de intentar ejercicios compuestos.
> - En cada problema, escribe primero **qué tipo de función es** y **qué regla vas a usar**; después calcula.

---

**Tags:** #MATG1045 #unidad4 #derivada #definicion-formal #limite-incremental #recta-tangente #velocidad-instantanea #no-derivabilidad #mnemotecnia

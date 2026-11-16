---
dg-publish: true
tags: [MATG1045, unidad6, propiedades-integral, integral-indefinida, integral-definida, constante-integracion, linealidad, teorema-fundamental-calculo, regla-barrow, desigualdades]
---

# 🧮 Propiedades de la Integral

## 🎯 Introducción

> [!info] 💡 Qué es la integración y por qué tiene propiedades
>
> La **integración** es la operación inversa de la derivada: donde la derivada mide la tasa de cambio instantánea, la integral mide la **acumulación**. Esa relación es tan estrecha que casi todo el comportamiento de la integral se deduce de unas pocas propiedades.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_01.svg]]
>
> **Se lee así:** es una cadena corta de tres rectángulos: se parte de la función $f(x)$, una flecha lleva a su derivada $f'(x)$, rotulada como tasa de cambio, y otra flecha lleva a la integral $\int f(x)\,dx$, rotulada como acumulación. Las dos flechas apuntan en sentidos opuestos porque son procesos inversos.
>
> **Por qué importa:** el diagrama fija las dos lecturas del símbolo. Una integral sin límites devuelve una **familia de funciones**; con límites devuelve un **número** (el área acumulada). Tener presente cuál de las dos estás calculando evita la mitad de los errores de esta unidad.
>
> **Ejemplo:** si $f(x) = 2x$, su derivada es $f'(x) = 2$, mientras que su integral indefinida es $\int 2x\,dx = x^2 + C$, la familia de funciones cuya derivada es exactamente $2x$.

> [!warning] ⚠️ Las tres confusiones que más cuestan puntos
>
> 1. **NO** trates la integral indefinida como un número: es una familia de funciones con $+C$.
> 2. **NO** olvides el $+C$ antes de sustituir límites… salvo que vayas a evaluar, donde se cancela.
> 3. **NO** apliques la regla de Barrow sin comprobar que la antiderivativa es correcta: un error ahí se propaga a todo el ejercicio.
>
> **Por qué importa:** los tres son errores de planteamiento, no de cálculo, y por eso se repiten en cada evaluación.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Integral indefinida
>
> Sea $F$ una primitiva de $f$ en un intervalo, es decir $F'(x) = f(x)$. La **integral indefinida** de $f$ es el conjunto de todas sus primitivas:
>
> $$\int f(x)\,dx = F(x) + C, \qquad C \in \mathbb{R}.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_02.svg]]
>
> **Se lee así:** es un flujo vertical de cuatro casillas: se parte de la integral indefinida $\int f(x)\,dx$, se indica que $F(x)$ es una primitiva de $f(x)$ porque $F'(x) = f(x)$, el siguiente recuadro da el resultado $F(x) + C$ y el último fija la notación $\int f(x)\,dx = F(x) + C$. No hay rombos: es un recorrido lineal.
>
> **Por qué importa:** la última casilla es la que recuerda que **el resultado nunca es una función sola sino una familia entera**. Cualquier $C$ cumple la condición, y omitirlo equivale a devolver una respuesta incompleta.
>
> **Ejemplo:** para $f(x) = 3x^2$ se obtiene $\int 3x^2\,dx = x^3 + C$; comprobando, $\frac{d}{dx}(x^3 + C) = 3x^2$ para cualquier $C$.

> [!note] 📋 Definición — Integral definida
>
> La **integral definida** de $f$ en $[a,b]$, con $f$ continua, es el límite de sumas de Riemann
>
> $$\int_a^b f(x)\,dx = \lim_{\|P\|\to 0}\sum_{i=1}^{n} f(x_i^*)\,\Delta x_i.$$
>
> Por el teorema fundamental, si $F$ es una primitiva de $f$ entonces el valor es un **número**: $F(b) - F(a)$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_08.svg]]
>
> **Se lee así:** es una tabla comparativa de dos columnas enfrentadas. La fila superior separa el concepto "integral" en dos ramas: **indefinida** y **definida**. Debajo, tres filas contrastan cada rama: la indefinida no tiene límites y sí incluye la constante $C$, mientras la definida tiene límites $a$ y $b$ y no la incluye; el resultado de la primera es una familia de funciones y el de la segunda, un número real (área acumulada).
>
> **Por qué importa:** es la distinción estructural de toda la unidad. Si confundes las dos columnas, sustituirás límites en una expresión con $C$ o escribirás $+C$ en un número, y ambas respuestas quedan mal aunque el cálculo previo sea correcto.
>
> **Ejemplo:** $\int 2x\,dx = x^2 + C$ (familia), mientras que $\int_1^3 2x\,dx = 9 - 1 = 8$ (número).

> [!note] 📋 Definición — Relación inversa con la derivada
>
> Integrar y derivar son operaciones inversas, en este orden:
>
> $$\frac{d}{dx}\left[\int f(x)\,dx\right] = f(x), \qquad \int \frac{d}{dx}\big[F(x)\big]\,dx = F(x) + C.$$
>
> La consecuencia práctica es el teorema fundamental: $\int_a^b f(x)\,dx = F(b) - F(a)$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_05.svg]]
>
> **Se lee así:** el diagrama se organiza en tres bloques. El superior enuncia que integrar y derivar son operaciones inversas; el intermedio muestra las dos igualdades de la relación (derivada de la integral da $f(x)$, integral de la derivada da $F(x) + C$); el inferior, rotulado "consecuencia práctica", enlaza con el teorema fundamental y su fórmula de evaluación $\int_a^b f(x)\,dx = F(b) - F(a)$.
>
> **Por qué importa:** el bloque inferior es el que convierte la teoría en herramienta: sin esa consecuencia, cada integral exigiría construir sumas de Riemann. Así se reduce todo el cálculo a buscar una antiderivada y evaluarla.
>
> **Ejemplo:** derivando $\int 2x\,dx = x^2 + C$ se recupera $2x$; integrando $\frac{d}{dx}(x^2) = 2x$ se recupera $x^2 + C$.

> [!note] 📋 Definición — Teorema Fundamental del Cálculo y regla de Barrow
>
> El **teorema fundamental** tiene dos partes:
>
> 1. **Primera parte:** si $F(x) = \int_a^x f(t)\,dt$, entonces $F'(x) = f(x)$. La derivada de la integral es la función original.
> 2. **Segunda parte (regla de Barrow):** $\displaystyle\int_a^b f(x)\,dx = F(b) - F(a)$, con $F$ cualquier primitiva de $f$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_14.svg]]
>
> **Se lee así:** un rectángulo central con el nombre del teorema se abre en dos ramas. La rama izquierda, "primera parte", muestra $F(x) = \int_a^x f(t)\,dt$ y concluye $F'(x) = f(x)$ con la leyenda "la derivada de la integral es la función original". La rama derecha, "segunda parte (regla de Barrow)", lleva a la fórmula de evaluación $\int_a^b f(x)\,dx = F(b) - F(a)$.
>
> **Por qué importa:** las dos ramas responden preguntas distintas. La izquierda permite construir nuevas funciones a partir de integrales (tasas de cambio); la derecha permite **calcular** cualquier integral continua en un intervalo cerrado. Es el puente entre derivadas e integrales de toda la materia.
>
> **Ejemplo:** con $F(x) = \int_0^x 3t^2\,dt = x^3$ se cumple $F'(x) = 3x^2$ (primera parte); e $\int_0^2 3x^2\,dx = 8 - 0 = 8$ (segunda parte).

---

## ➕ Propiedades de la integral indefinida

> [!success] ✅ Linealidad
>
> Para constantes $k$, $a$ y $b$:
>
> $$\int k\,f(x)\,dx = k\int f(x)\,dx, \qquad \int \big[f(x) + g(x)\big]\,dx = \int f(x)\,dx + \int g(x)\,dx.$$
>
> Combinadas: $\displaystyle\int \big[a f(x) + b g(x)\big]\,dx = a\int f(x)\,dx + b\int g(x)\,dx$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_03.svg]]
>
> **Se lee así:** un nodo raíz "Linealidad de la integral" se abre en dos ramas de decisión: **constante multiplicativa** y **aditividad**. Cada rama baja a su fórmula ($\int k\cdot f\,dx = k\int f\,dx$ y $\int (f+g)\,dx = \int f\,dx + \int g\,dx$) y ambas se recogen en la casilla final de combinación $\int (af + bg)\,dx = a\int f\,dx + b\int g\,dx$.
>
> **Por qué importa:** la linealidad es lo que permite partir un polinomio en términos de $x^n$ e integrar cada uno por separado. Es la propiedad que más se aplica y la que convierte una integral difícil en varias fáciles.
>
> **Ejemplo:** $\int (4x^3 - 2x + 5)\,dx = 4\cdot\frac{x^4}{4} - 2\cdot\frac{x^2}{2} + 5x + C = x^4 - x^2 + 5x + C$.

> [!warning] ⚠️ Constante de integración
>
> Derivar elimina los términos constantes, por eso integrar debe **devolverlos**. Si $F'(x) = f(x)$, entonces $F(x) + C$ es primitiva para **cualquier** $C$:
>
> $$\frac{d}{dx}(x^2 + 5) = \frac{d}{dx}(x^2 - 3) = 2x \quad \Longrightarrow \quad \int 2x\,dx = x^2 + C.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_04.svg]]
>
> **Se lee así:** el flujo parte de la constante de integración $C$ y pregunta "¿por qué existe?". La respuesta llega en dos casillas: la igualdad $d(x^2+5)/dx = d(x^2-3)/dx = 2x$ y la explicación "la derivación pierde el término constante". De ahí se pasa a la "familia infinita: $x^2 + C$" y se cierra con la notación $\int 2x\,dx = x^2 + C$.
>
> **Por qué importa:** el diagrama muestra el **origen** del $+C$, no solo su existencia. Entender que la derivada no puede distinguir $x^2+5$ de $x^2-3$ explica por qué la integral indefinida nunca puede devolver una función única.
>
> **Ejemplo:** $\int \cos x\,dx = \sin x + C$: comprobando, $\frac{d}{dx}(\sin x + 7) = \cos x$, igual que $\frac{d}{dx}(\sin x - 2)$.

> [!info] 🖼️ La familia infinita de primitivas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_06.svg]]
>
> **Se lee así:** un nodo raíz indica "$F(x)$ es una primitiva de $f(x)$" y de él salen cinco flechas a cinco casillas paralelas: $F(x)+C_1$, $F(x)+C_2$, $F(x)+C_3$, $F(x)+C_4$ y $G(x)+C_5$. Todas apuntan en el mismo nivel porque ninguna es más "principal" que otra.
>
> **Por qué importa:** visualiza que la solución es un **conjunto infinito** de funciones, no una sola. Eso es exactamente lo que grafica un paquete de curvas desplazadas verticalmente: la misma forma, distintas alturas.
>
> **Ejemplo:** para $f(x) = 2x$ la familia es $x^2 + C$: parábolas idénticas desplazadas, todas con la misma pendiente en cada $x$.

> [!tip] 🔧 Problema de valor inicial
>
> Para **fijar** la constante se da una condición $F(x_0) = c$. Procedimiento:
>
> 1. Escribir la familia general $F(x) + C$.
> 2. Sustituir $x = x_0$ e igualar a $c$.
> 3. Despejar el valor de $C$.
> 4. Reescribir la solución única $F(x)$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_07.svg]]
>
> **Se lee así:** el flujo arranca con el enunciado $F'(x) = f(x)$ con $F(x_0) = c$, pasa a la "familia general $F(x)+C$" y entra en un bloque rotulado "aplicar la condición inicial" con tres casillas encadenadas: sustituir $x = x_0$ y $f(x_0) = c$, despejar el valor de $C$, y llegar a la "solución única $F(x)$".
>
> **Por qué importa:** es la respuesta práctica a la duda de por qué la constante existe y cuándo se elimina. Sin la condición hay infinitas soluciones; con ella, exactamente una. Ese es todo el contenido del ejercicio típico de valor inicial.
>
> **Ejemplo:** con $F'(x) = 3x^2$ y $F(1) = 5$: familia $x^3 + C$, sustituyendo $1 + C = 5$ da $C = 4$, solución única $F(x) = x^3 + 4$.

---

## 🔢 Propiedades de la integral definida

> [!success] ✅ Linealidad de la integral definida
>
> Para constantes $c$ y $d$:
>
> $$\int_a^b k\,f(x)\,dx = k\int_a^b f(x)\,dx, \qquad \int_a^b \big[f(x) + g(x)\big]\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx.$$
>
> Combinadas: $\displaystyle\int_a^b \big[c f + d g\big]\,dx = c\int_a^b f\,dx + d\int_a^b g\,dx$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_09.svg]]
>
> **Se lee así:** el espejo del diagrama de linealidad indefinida, pero con límites $a$ y $b$ en cada fórmula. El nodo raíz "linealidad de la integral definida" se abre en **constante multiplicativa** y **aditividad**, cada rama muestra su igualdad con los límites, y ambas se recogen en la combinación general $\int_a^b (cf+dg)\,dx = c\int_a^b f\,dx + d\int_a^b g\,dx$.
>
> **Por qué importa:** confirma que la linealidad **se hereda** de la indefinida a la definida. Por eso se puede partir una integral en varias antes de aplicar la regla de Barrow, que es el paso que más ahorra en los exámenes.
>
> **Ejemplo:** $\int_0^2 (3x^2 + 1)\,dx = \big[x^3\big]_0^2 + \big[x\big]_0^2 = 8 + 2 = 10$.

> [!note] 📋 Definición — Propiedades de los límites de integración
>
> 1. **Orden invertido:** $\displaystyle\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$.
> 2. **Límites iguales:** $\displaystyle\int_a^a f(x)\,dx = 0$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_10.svg]]
>
> **Se lee así:** dos ramas paralelas salen de un nodo común "propiedades de los límites". La rama superior, "orden invertido", conduce a la igualdad $\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$. La rama inferior, "límites iguales", conduce primero a una "interpretación geométrica" y luego a la conclusión $\int_a^a f(x)\,dx = 0$, con la glosa "no hay intervalo que integrar: valor 0".
>
> **Por qué importa:** la segunda propiedad resuelve de un vistazo cualquier integral con los mismos extremos, sin calcular nada. La primera permite reordenar límites siempre que se cambie el signo, y es la que aparece en los problemas de simetría.
>
> **Ejemplo:** $\int_{-1}^{5} f(x)\,dx = -\int_{5}^{-1} f(x)\,dx$; y $\int_{2}^{2} \ln x\,dx = 0$ sin necesidad de saber nada de $\ln x$.

> [!note] 📋 Definición — Aditividad del intervalo
>
> Si $a < c < b$, entonces
>
> $$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_11.svg]]
>
> **Se lee así:** el flujo parte de la "integral definida sobre $[a,b]$" y pasa por un nodo rotulado "aditividad" con la condición "caso $a < c < b$". Debajo, la rama de "interpretación geométrica" conduce a la igualdad $\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$: un recorrido lineal, sin decisiones.
>
> **Por qué importa:** permite **partir** una integral en trozos. Es la propiedad que hace posible integrar funciones por tramos, cambiar de sentido al recorrer un intervalo y calcular áreas donde la función cambia de fórmula.
>
> **Ejemplo:** $\int_0^4 x^2\,dx = \int_0^2 x^2\,dx + \int_2^4 x^2\,dx = \tfrac{8}{3} + \tfrac{56}{3} = \tfrac{64}{3}$, que coincide con $\big[\tfrac{x^3}{3}\big]_0^4$.

---

## 📏 Desigualdades y cotas

> [!note] 📋 Definición — Desigualdades de comparación y cotas
>
> Para $f$ y $g$ continuas en $[a,b]$:
>
> 1. **Comparación:** si $f(x) \le g(x)$, entonces $\int_a^b f(x)\,dx \le \int_a^b g(x)\,dx$.
> 2. **Signo:** si $f(x) \ge 0$, entonces $\int_a^b f(x)\,dx \ge 0$.
> 3. **Cotas:** si $m \le f(x) \le M$, entonces $m(b-a) \le \int_a^b f(x)\,dx \le M(b-a)$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_12.svg]]
>
> **Se lee así:** tres parejas de casillas enfrentadas, cada una con una flecha de hipótesis a consecuencia. Arriba, $f(x) \le g(x)$ conduce a $\int_a^b f\,dx \le \int_a^b g\,dx$; en medio, $f(x) \ge 0$ conduce a $\int_a^b f\,dx \ge 0$; abajo, $m \le f(x) \le M$ conduce a la doble cota $m(b-a) \le \int_a^b f\,dx \le M(b-a)$.
>
> **Por qué importa:** la tercera fila es la herramienta para **acotar sin calcular**: si solo conoces los valores mínimo y máximo de la función, ya puedes encerrar la integral entre dos números. Es la base de los teoremas de comparación de integrales impropias.
>
> **Ejemplo:** como $0 \le \sin x \le 1$ en $[0,\pi]$, entonces $0 \le \int_0^\pi \sin x\,dx \le \pi$, y el valor real $2$ queda dentro de ese intervalo.

---

## 🖼️ Interpretación geométrica

> [!info] 📈 El signo de la función y la integral
>
> - Si $f(x) > 0$ en $[a,b]$: la integral es el **área** bajo la curva.
> - Si $f(x) < 0$: la integral es el área **con signo negativo**.
> - Si $f$ cambia de signo: la integral devuelve el **área neta** (lo que está arriba menos lo que está debajo).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_13.svg]]
>
> **Se lee así:** un nodo superior con la integral $\int_a^b f(x)\,dx$ conduce a un evaluador "signo de $f(x)$ en $[a,b]$" que se abre en tres ramas: $f(x) > 0$, $f(x) < 0$ y "$f(x)$ cambia de signo". Cada rama es un caso de lectura geométrica distinto del mismo número.
>
> **Por qué importa:** explica por qué la integral no es "el área" sin más, sino el área **con signo**. Cuando la función cruza el eje, cancelaciones reales: dos regiones iguales pueden darse cuenta de que su suma es cero.
>
> **Ejemplo:** $\int_{-1}^{1} x\,dx = 0$, porque el área negativa de $[-1,0]$ cancela exactamente a la positiva de $[0,1]$.

---

## 🧮 Cómo se calcula: evaluación por antiderivadas

> [!tip] 🔧 El algoritmo de cinco pasos
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Propiedades_de_la_Integral_15.svg]]
>
> **Se lee así:** una cadena vertical de seis casillas que ordena el cálculo: se parte de la "integral definida $\int_a^b f(x)\,dx$" y siguen cinco pasos numerados —hallar la antiderivativa $F(x)$, evaluar $F(b)$, evaluar $F(a)$, restar $F(b) - F(a)$— hasta la casilla final "resultado numérico". No hay ramas: es un procedimiento fijo.
>
> **Por qué importa:** el paso 4 es el que se olvida: **primero se evalúa cada extremo y luego se resta**. Saltarse ese orden produce el error clásico de restar antes de sustituir, que da signos invertidos.
>
> **Ejemplo:** $\int_1^4 3x^2\,dx$: $F(x) = x^3$, $F(4) = 64$, $F(1) = 1$, y la resta da $63$.

> [!example] 🔢 Aplicación completa: $\int_0^3 (2x + 1)\,dx$
>
> 1. **Antiderivativa:** $\int (2x+1)\,dx = x^2 + x + C$ (aquí $C$ no hace falta).
> 2. **Evaluar en el límite superior:** $F(3) = 9 + 3 = 12$.
> 3. **Evaluar en el límite inferior:** $F(0) = 0 + 0 = 0$.
> 4. **Restar:** $12 - 0 = 12$.
>
> **Por qué importa:** en este caso el límite inferior es cero, así que el paso 3 queda "gratis" y es fácil confundir eso con un error. Evalúa **siempre** los dos extremos aunque uno sea nulo.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los seis errores que más se repiten
>
> 1. **Olvidar el $+C$** en una integral indefinida.
> 2. **Dejar el $+C$** después de sustituir límites (se cancela: $(F(b)+C) - (F(a)+C)$).
> 3. **Invertir los límites** sin cambiar el signo.
> 4. **No partir el intervalo** cuando la función cambia de fórmula o de signo.
> 5. **Leer el resultado como área positiva** cuando la función es negativa.
> 6. **Evaluar antes de restar:** sustituir mal $F(b) - F(a)$ en vez de $F(b) - F(a)$.
>
> **Por qué importa:** los seis son de planteamiento y se detectan con una sola pregunta: *¿qué estoy calculando, una familia o un número?*

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\int (6x^2 - 4x + 3)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > Se aplica la linealidad término a término:
> >
> > $$\int 6x^2\,dx = 6\cdot\frac{x^3}{3} = 2x^3, \qquad \int 4x\,dx = 4\cdot\frac{x^2}{2} = 2x^2, \qquad \int 3\,dx = 3x.$$
> >
> > **Respuesta:** $2x^3 - 2x^2 + 3x + C$.
> >
> > Comprobación: $\frac{d}{dx}(2x^3 - 2x^2 + 3x + C) = 6x^2 - 4x + 3$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve el problema de valor inicial: $F'(x) = 3x^2 - 2x$ con $F(2) = 7$.
>
> > [!success]- ✅ Solución
> >
> > Familia general: $F(x) = x^3 - x^2 + C$.
> >
> > Sustituyendo la condición: $F(2) = 8 - 4 + C = 7$, de donde $4 + C = 7$ y $C = 3$.
> >
> > **Respuesta:** $F(x) = x^3 - x^2 + 3$.
> >
> > Comprobación: $F(2) = 8 - 4 + 3 = 7$ ✓ y $F'(x) = 3x^2 - 2x$ ✓

> [!example] 📋 Planteamiento
>
> Calcula $\int_1^3 (2x + 1)\,dx$ usando la regla de Barrow y verifica con la suma de áreas de la región trapezoidal.
>
> > [!success]- ✅ Solución
> >
> > **Regla de Barrow:** con $F(x) = x^2 + x$,
> >
> > $$F(3) - F(1) = (9 + 3) - (1 + 1) = 12 - 2 = 10.$$
> >
> > **Verificación geométrica:** la región es un trapecio con altura $2$ (de $x=1$ a $x=3$) y paralelas $f(1) = 3$ y $f(3) = 7$:
> >
> > $$A = \frac{3 + 7}{2}\cdot 2 = 10.$$
> >
> > **Respuesta:** $10$; los dos métodos coinciden.

> [!example] 📋 Planteamiento
>
> Sin calcular, justifica el signo de $\int_{-2}^{2} (x^3 - x)\,dx$ y calcula después su valor.
>
> > [!success]- ✅ Solución
> >
> > La función $g(x) = x^3 - x$ es **impar**: $g(-x) = -x^3 + x = -g(x)$. Como el intervalo $[-2,2]$ es simétrico respecto del origen, la integral de una función impar es $0$ (el área negativa cancela a la positiva).
> >
> > **Cálculo directo:** $F(x) = \frac{x^4}{4} - \frac{x^2}{2}$, y
> >
> > $$F(2) - F(-2) = \left(4 - 2\right) - \left(4 - 2\right) = 0.$$
> >
> > **Respuesta:** $0$, confirmado por las dos vías.

> [!example] 📋 Planteamiento
>
> Acota $\int_0^2 e^{-x^2}\,dx$ usando las cotas $m \le f(x) \le M$ en $[0,2]$.
>
> > [!success]- ✅ Solución
> >
> > $f(x) = e^{-x^2}$ es decreciente en $[0,2]$ (su derivada $-2x e^{-x^2}$ es negativa para $x>0$), así que
> >
> > $$M = f(0) = 1, \qquad m = f(2) = e^{-4} \approx 0.0183.$$
> >
> > Aplicando la cota con $b - a = 2$:
> >
> > $$m(b-a) \le \int_0^2 e^{-x^2}\,dx \le M(b-a) \quad \Longrightarrow \quad 0.0366 \le \int_0^2 e^{-x^2}\,dx \le 2.$$
> >
> > **Respuesta:** el valor real es $\approx 0.8821$, que queda dentro del intervalo acotado.

> [!example] 📋 Planteamiento
>
> Parte la integral $\int_{-1}^{3} |x|\,dx$ en el punto donde la función cambia de fórmula y calcula su valor.
>
> > [!success]- ✅ Solución
> >
> > En $x = 0$ la expresión cambia: $|x| = -x$ en $[-1,0]$ y $|x| = x$ en $[0,3]$. Por aditividad del intervalo:
> >
> > $$\int_{-1}^{3} |x|\,dx = \int_{-1}^{0} (-x)\,dx + \int_{0}^{3} x\,dx.$$
> >
> > Primera parte: $\left[-\frac{x^2}{2}\right]_{-1}^{0} = 0 - \left(-\frac{1}{2}\right) = \frac{1}{2}$.
> >
> > Segunda parte: $\left[\frac{x^2}{2}\right]_{0}^{3} = \frac{9}{2} - 0 = \frac{9}{2}$.
> >
> > **Respuesta:** $5$; geométricamente coincide con la suma de los dos triángulos de la figura: el de la izquierda tiene base $1$ y altura $1$ ($\frac{1}{2}$), y el de la derecha base $3$ y altura $3$ ($\frac{9}{2}$).

> [!example] 📋 Planteamiento
>
> Usa la linealidad y los límites especiales para hallar $\int_0^5 (3x^2 + 2)\,dx - 3\int_0^5 x^2\,dx$.
>
> > [!success]- ✅ Solución
> >
> > Por linealidad, $\int_0^5 (3x^2 + 2)\,dx = 3\int_0^5 x^2\,dx + \int_0^5 2\,dx$.
> >
> > Sustituyendo en la expresión original, el término $3\int_0^5 x^2\,dx$ se cancela con el que se resta:
> >
> > $$3\int_0^5 x^2\,dx + \int_0^5 2\,dx - 3\int_0^5 x^2\,dx = \int_0^5 2\,dx.$$
> >
> > Y $\int_0^5 2\,dx = [2x]_0^5 = 10$.
> >
> > **Respuesta:** $10$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo la integral indefinida (familia con $+C$) de la definida (número sin constante).
> - [ ] Aplico la linealidad para partir una integral en varias más simples.
> - [ ] Escribo las propiedades de los límites (inversión y límites iguales) sin calcular.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo problemas de valor inicial fijando la constante con la condición dada.
> - [ ] Parto el intervalo de integración con la aditividad cuando la función cambia de fórmula.
> - [ ] Acoto una integral entre $m(b-a)$ y $M(b-a)$ sin calcular el valor exacto.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Enuncio las dos partes del teorema fundamental y explico qué responde cada una.
> - [ ] Interpreto el signo de una integral a partir del signo de la función y detecto cancelaciones.
> - [ ] Verifico un resultado con un método alternativo (geometría, simetría o propiedades).

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4 y 5: propiedades de la integral y teorema fundamental.
> - R. Larson, *Cálculo* (Cengage), cap. 5: linealidad, cotas y regla de Barrow.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 5: la integral como acumulación.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la definición de la que se deducen estas propiedades.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — las dos partes vistas aquí con detalle.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración|03 - Constante de integración]] — el destino natural de la constante $C$.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué devuelve la integral indefinida?::Una familia de funciones $F(x) + C$, no un número: todas las primitivas de $f$.
> - ¿Qué devuelve la integral definida?::Un número real, la acumulación neta en $[a,b]$; se obtiene con $F(b) - F(a)$ y no lleva $+C$.
> - ¿Cuál es la linealidad de la integral?::$\int (af + bg)\,dx = a\int f\,dx + b\int g\,dx$, válida tanto para la indefinida como para la definida.
> - ¿Qué dice la aditividad del intervalo?::Que se puede partir el intervalo: $\int_a^b f\,dx = \int_a^c f\,dx + \int_c^b f\,dx$ cuando $a < c < b$.
> - ¿Qué permiten las cotas $m \le f \le M$?::Acotar sin calcular: $m(b-a) \le \int_a^b f(x)\,dx \le M(b-a)$.
> - ¿Cómo fijo la constante de integración?::Con un problema de valor inicial: se sustituye la condición $F(x_0) = c$ en la familia $F(x) + C$ y se despeja $C$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — de dónde salen las sumas que dan sentido a la definida.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/03 - Propiedades de la Sumatoria|03 - Propiedades de la Sumatoria]] — la notación sigma que aparece en la definición.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el puente que hace calculable todo esto.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — las primitivas que la integral indefinida devuelve.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración|03 - Constante de integración]] — el $+C$ en profundidad.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — los métodos que aplican estas propiedades en la práctica.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: linealidad y valor inicial deben salirte sin vacilar.
> - Después salta al 3, donde la regla de Barrow se aplica de punta a punta y puedes verificarlo geométricamente.
> - Cuando lo tengas, ataca el 6 (partición del intervalo), que es el que más se parece a los exámenes de la casa.
> - El 5 y el 7 son el nivel de acotación y simplificación: úsalos para comprobar que entiendes las propiedades y no solo el cálculo.
> - Cierra con [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|Teorema Fundamental del Cálculo]], donde estas reglas se demuestran.

---

**Tags:** #MATG1045 #unidad6 #propiedades-integral #integral-indefinida #integral-definida #constante-integracion #linealidad #teorema-fundamental-calculo #regla-barrow #desigualdades

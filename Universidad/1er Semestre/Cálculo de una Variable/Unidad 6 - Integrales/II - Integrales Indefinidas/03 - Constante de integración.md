---
dg-publish: true
tags: [MATG1045, unidad6, constante-integracion, familia-curvas, problemas-valor-inicial, condiciones-iniciales, ecuaciones-diferenciales, aplicaciones-fisica]
---

# 🔑 Constante de Integración

## 🎯 Introducción

> [!info] 💡 Qué es y por qué existe la $C$
>
> La **constante de integración** $C$ es el factor que distingue una antiderivada particular de la familia completa de todas las antiderivadas. Derivar elimina las constantes, por eso integrar debe devolverlas: $\int f(x)\,dx = F(x) + C$.
>
> **Por qué importa:** sin la $C$ solo obtienes una solución particular de infinitas, y en ecuaciones diferenciales eso significa perder soluciones válidas del problema físico.
>
> **Ejemplo:** $\int 2x\,dx = x^2$ está incompleto; $\int 2x\,dx = x^2 + C$ es la respuesta correcta: todas las parábolas cuya derivada es $2x$.

> [!warning] ⚠️ Los tres errores que más se repiten
>
> 1. **NO** omitas la $C$ en una integral indefinida: es la diferencia entre la general y la particular.
> 2. **NO** la conserves después de sustituir límites: $(F(b)+C) - (F(a)+C) = F(b) - F(a)$, se cancela sola.
> 3. **NO** escribas una $C$ por término: al sumar integrales, $C_1 + C_2$ se combina en **una sola** $C$.
>
> **Por qué importa:** los tres son errores de concepto, no de cálculo, y por eso sobreviven a la comprobación derivando.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Constante de integración
>
> La **constante de integración** $C$ es una constante arbitraria que se añade al resultado de una integral indefinida para representar todas las posibles antiderivadas de una función:
>
> $$\int f(x)\,dx = F(x) + C,$$
>
> donde $F(x)$ es una antiderivada particular de $f(x)$. Existe porque si $F'(x) = f(x)$, entonces $\frac{d}{dx}[F(x) + C] = F'(x) + 0 = f(x)$ para cualquier $C$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Constante_de_integración_01.svg]]
>
> **Se lee así:** como una cadena que arranca en una sola caja con la igualdad $\int f(x)\,dx = F(x) + C$, de la que salen dos flechas: una hacia la caja que identifica a $C$ como constante de integración de valores arbitrarios, y otra hacia el recuadro donde se deriva $F(x) + C$. Desde ahí el recorrido sigue hacia abajo y termina en la caja que recuerda que en una integral definida las constantes se cancelan.
>
> **Por qué importa:** el diagrama encadena la definición, la demostración y la consecuencia en un solo recorrido. Te da la razón lógica de la $C$ (al derivarla da cero) y te evita el error de mantenerla en una integral definida, donde $[F(b)+C] - [F(a)+C]$ se simplifica a $F(b) - F(a)$.
>
> **Ejemplo:** en el problema de valor inicial de la nota, $\frac{dy}{dx} = 3x^2 - 2x$ con $y(1) = 5$, el diagrama marca que primero se integra con $C$ y luego la condición inicial la fija.

> [!note] 📋 Condición inicial y solución particular
>
> Para **fijar** el valor de $C$ hace falta información adicional: una condición inicial $y(x_0) = y_0$, una condición de frontera o una lectura física del problema. El procedimiento es:
>
> 1. Integrar para obtener la familia general $F(x) + C$.
> 2. Sustituir la condición conocida.
> 3. Despejar $C$ y reescribir la solución particular.
>
> **Por qué importa:** la condición inicial es lo que convierte una familia infinita en la única función que modela el problema concreto; sin ella, el modelo admite infinitas respuestas.
>
> **Ejemplo:** con $\frac{dy}{dx} = 3x^2 - 2x$ y $y(1) = 5$: $y = x^3 - x^2 + C$, y $5 = 1 - 1 + C$ da $C = 5$, luego $y = x^3 - x^2 + 5$.

---

## 🌐 Interpretación geométrica

> [!info] 🖼️ La familia de curvas paralelas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Constante_de_integración_02.svg]]
>
> **Se lee así:** como un rectángulo inicial con el ejemplo $\int 2x\,dx = x^2 + C$, del que salen cuatro flechas hacia casos particulares: $C = 0$, $C = 2$, $C = -3$ y $C = k$, cada uno con su desplazamiento vertical. Una quinta flecha lleva a la caja que dice que todas las curvas tienen la misma pendiente $2x$ en cualquier punto, y desde ahí una última flecha cierra con que la forma es idéntica y solo se desplazan.
>
> **Por qué importa:** la vista quita la duda de si la $C$ cambia la forma de la curva: no, solo la sube o la baja. Explica por qué la derivada de todas ellas coincide y por qué, con un punto dado, se puede escoger una sola.
>
> **Ejemplo:** con $C = 2$ y $C = -3$ se obtienen las parábolas $y = x^2 + 2$ y $y = x^2 - 3$, que comparten la pendiente $2x$ en cada punto.

> [!example] 📐 Lo que significa cada pieza en el plano
>
> - **Misma forma:** todas las curvas de la familia son congruentes.
> - **Desplazamiento vertical:** $C$ las mueve arriba ($C > 0$), abajo ($C < 0$) o las deja donde están ($C = 0$).
> - **Pendiente común:** en $x = a$ todas tienen pendiente $f(a)$, porque la derivada no "ve" la constante.
>
> **Por qué importa:** es la lectura geométrica que conecta con la Unidad 4: la primitiva recorre el campo de direcciones trazado por $f$, y $C$ elige qué curva de la familia lo sigue.

---

## 🔧 Determinación de la constante

> [!tip] 🔧 Problema de valor inicial en tres pasos
>
> 1. **Integrar:** obtener la familia general $F(x) + C$.
> 2. **Aplicar la condición:** sustituir $x = x_0$ e igualar al valor dado.
> 3. **Despejar:** hallar $C$ y escribir la solución particular.
>
> **Por qué importa:** es el formato exacto del examen; escribirlo en tres pasos con etiqueta evita perder puntos por saltos.
>
> **Ejemplo:** $\frac{dy}{dx} = e^x$ con $y(0) = 3$: familia $y = e^x + C$; $3 = e^0 + C = 1 + C$ da $C = 2$; solución $y = e^x + 2$ (verificando: $y(0) = 3$ ✓ y $y' = e^x$ ✓).

> [!example] 🚗 Interpretación física: aceleración y velocidad
>
> Un objeto tiene $a(t) = 6t$ m/s² y $v(0) = 10$ m/s.
>
> $$v(t) = \int 6t\,dt = 3t^2 + C, \qquad v(0) = 10 \Rightarrow C = 10, \qquad v(t) = 3t^2 + 10.$$
>
> **Por qué importa:** aquí $C$ no es un formalismo: **es la velocidad inicial**. Cada contexto le da un significado concreto.

> [!example] 🎯 Integraciones sucesivas: dos constantes
>
> Si $\frac{d^2y}{dx^2} = 6$:
>
> $$\frac{dy}{dx} = \int 6\,dx = 6x + C_1, \qquad y = \int (6x + C_1)\,dx = 3x^2 + C_1 x + C_2.$$
>
> $C_1$ se fija con la velocidad inicial y $C_2$ con la posición inicial.
>
> **Por qué importa:** una EDO de orden $n$ aporta $n$ constantes, y por eso hacen falta $n$ condiciones para determinarlas todas.

---

## 📊 La $C$ en distintos contextos

> [!info] 📋 Significado y determinación por contexto
>
> | Contexto | Significado de $C$ | Determinación |
> |---|---|---|
> | Ecuaciones diferenciales | familia de soluciones | condición inicial $y(x_0) = y_0$ |
> | Física — posición | posición inicial | $s(0) = s_0$ |
> | Física — velocidad | velocidad inicial | $v(0) = v_0$ |
> | Circuitos — carga | carga inicial | $q(0) = q_0$ |
> | Economía | capital inicial | $K(0) = K_0$ |
> | Biología | población inicial | $P(0) = P_0$ |
>
> **Por qué importa:** la tabla convierte la $C$ de símbolo abstracto a dato con nombre; cuando el enunciado da una condición, ya sabes qué representa.

> [!example] ⚡ Circuitos: carga en un capacitor
>
> Si la corriente es $i(t) = 0.5e^{-t}$ A y $q(0) = 2$ C, con $i = \frac{dq}{dt}$:
>
> $$q(t) = \int 0.5e^{-t}\,dt = -0.5e^{-t} + C, \qquad 2 = -0.5 + C \Rightarrow C = 2.5,$$
>
> luego $q(t) = -0.5e^{-t} + 2.5$.
>
> **Por qué importa:** la carga inicial fija la constante igual que la velocidad en cinemática: mismo procedimiento, distinto nombre.

---

## 🧮 Propiedades algebraicas

> [!success] ✅ Una sola constante por expresión
>
> Al combinar integrales, las constantes particulares se absorben en una:
>
> $$\int f\,dx + \int g\,dx = F(x) + C_1 + G(x) + C_2 = F(x) + G(x) + C, \qquad C = C_1 + C_2.$$
>
> Y con múltiplos: $k\int f\,dx = kF(x) + kC_1 = kF(x) + C$, donde $C = kC_1$.
>
> **Por qué importa:** por eso se escribe **una sola** $C$ al final de una expresión integrada término a término, no una por término.
>
> **Ejemplo:** $3\int x\,dx - 2\int x^2\,dx + 5\int 1\,dx = \frac{3x^2}{2} - \frac{2x^3}{3} + 5x + C$ con $C = 3C_1 - 2C_2 + 5C_3$.

---

## 🧠 Orden y constantes en ecuaciones diferenciales

> [!info] 🖼️ El orden de la EDO decide el número de constantes
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Constante_de_integración_03.svg]]
>
> **Se lee así:** como una caja central sobre la $C$ en ecuaciones diferenciales de la que salen cinco flechas. Tres de ellas llevan a los casos de orden 1, 2 y $n$, con una, dos y $n$ constantes respectivamente; las otras dos van a la lectura de análisis funcional, que identifica el núcleo del operador derivada con las funciones constantes, y al recordatorio de que el valor particular de $C$ se fija con una condición inicial.
>
> **Por qué importa:** el orden de la EDO y el número de constantes son el mismo dato. Conecta lo que estás calculando con la solución de ecuaciones diferenciales y evita tratar la $C$ como un número decorativo en lugar de un parámetro que describe una familia de soluciones.
>
> **Ejemplo:** el doble caso de la nota, $\frac{d^2y}{dx^2} = 6$, da $y = 3x^2 + C_1 x + C_2$, con $C_1$ ligada a la velocidad inicial y $C_2$ a la posición inicial.

> [!note] 📋 Núcleo del operador derivada (lectura avanzada)
>
> En análisis funcional, la constante de integración es el **espacio nulo** del operador derivada:
>
> $$\ker(D) = \{f : Df = 0\} = \{\text{funciones constantes}\}.$$
>
> **Por qué importa:** explica *por qué exactamente* una y solo una dimensión de indeterminación aparece al integrar una vez: el núcleo de $D$ tiene dimensión 1. Integrar dos veces lo duplica, y así sucesivamente.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco malentendidos clásicos
>
> 1. **"La constante es opcional":** no lo es; sin ella la respuesta es incompleta.
> 2. **"Todas las constantes son iguales":** $C_1 + C_2$ se combinan en una sola $C$ nueva.
> 3. **"La constante es siempre positiva":** $C \in \mathbb{R}$, puede ser negativa o cero.
> 4. **"Una vez determinada no cambia":** en un problema es fija, pero cada problema tiene la suya.
> 5. **"Se mantiene en la integral definida":** se cancela en la evaluación.
>
> **Por qué importa:** los cinco son de concepto y se detectan con una pregunta: *¿estoy devolviendo una familia o un número?*

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Escribe la antiderivada general de $f(x) = 6x^2 - 4x + 3$ e intégrala dos veces para ver dónde aparecen las constantes.
>
> > [!success]- ✅ Solución
> > 
> > Primera integración:
> > 
> > $$\int (6x^2 - 4x + 3)\,dx = 2x^3 - 2x^2 + 3x + C_1.$$
> > 
> > Segunda integración (aplicando la fórmula a cada término):
> > 
> > $$\int (2x^3 - 2x^2 + 3x + C_1)\,dx = \frac{x^4}{2} - \frac{2x^3}{3} + \frac{3x^2}{2} + C_1 x + C_2.$$
> > 
> > **Respuesta:** $2x^3 - 2x^2 + 3x + C_1$ y $\frac{x^4}{2} - \frac{2x^3}{3} + \frac{3x^2}{2} + C_1x + C_2$: dos integraciones, dos constantes.

> [!example] 📋 Planteamiento
>
> Resuelve el problema de valor inicial: $\frac{dy}{dx} = 3x^2 - 2x$ con $y(1) = 5$.
>
> > [!success]- ✅ Solución
> > 
> > **Paso 1 (integrar):** $y = \int (3x^2 - 2x)\,dx = x^3 - x^2 + C$.
> > 
> > **Paso 2 (condición):** $y(1) = 1 - 1 + C = C = 5$.
> > 
> > **Paso 3 (solución):** $y = x^3 - x^2 + 5$.
> > 
> > **Respuesta:** $y = x^3 - x^2 + 5$.
> > 
> > Verificación: $y(1) = 1 - 1 + 5 = 5$ ✓ y $y' = 3x^2 - 2x$ ✓

> [!example] 📋 Planteamiento
>
> Un móvil tiene aceleración $a(t) = -9.8$ m/s², con $v(0) = 20$ m/s y $s(0) = 100$ m. Encuentra $v(t)$ y $s(t)$.
>
> > [!success]- ✅ Solución
> > 
> > **Velocidad:** $v(t) = \int (-9.8)\,dt = -9.8t + C_1$; con $v(0) = 20$ se obtiene $C_1 = 20$, luego $v(t) = -9.8t + 20$.
> > 
> > **Posición:** $s(t) = \int (-9.8t + 20)\,dt = -4.9t^2 + 20t + C_2$; con $s(0) = 100$ se obtiene $C_2 = 100$.
> > 
> > **Respuesta:** $v(t) = -9.8t + 20$ m/s y $s(t) = -4.9t^2 + 20t + 100$ m.
> > 
> > Cada condición fija una constante distinta, en el orden en que aparecen.

> [!example] 📋 Planteamiento
>
> Simplifica $3\int x\,dx - 2\int x^2\,dx + 5\int 1\,dx$ en una sola expresión.
>
> > [!success]- ✅ Solución
> > 
> > Integrando por separado:
> > 
> > $$3\left(\frac{x^2}{2} + C_1\right) - 2\left(\frac{x^3}{3} + C_2\right) + 5(x + C_3) = \frac{3x^2}{2} - \frac{2x^3}{3} + 5x + (3C_1 - 2C_2 + 5C_3).$$
> > 
> > **Respuesta:** $\dfrac{3x^2}{2} - \dfrac{2x^3}{3} + 5x + C$ con $C = 3C_1 - 2C_2 + 5C_3$, una sola constante.

> [!example] 📋 Planteamiento
>
> Justifica por qué $\int_1^4 2x\,dx$ no lleva $+C$, aunque su antiderivada sí la tenga.
>
> > [!success]- ✅ Solución
> > 
> > La antiderivada general es $F(x) + C$. Al evaluar en los límites:
> > 
> > $$[F(x) + C]_1^4 = (F(4) + C) - (F(1) + C) = F(4) - F(1),$$
> > 
> > porque $C - C = 0$.
> > 
> > **Respuesta:** $\int_1^4 2x\,dx = 16 - 1 = 15$; la $C$ se cancela sola, así que la integral definida es un número.

> [!example] 📋 Planteamiento
>
> Encuentra la carga $q(t)$ si la corriente es $i(t) = 0.5e^{-t}$ A y $q(0) = 2$ C.
>
> > [!success]- ✅ Solución
> > 
> > Como $i = \frac{dq}{dt}$:
> > 
> > $$q(t) = \int 0.5e^{-t}\,dt = -0.5e^{-t} + C.$$
> > 
> > Condición inicial: $2 = -0.5e^{0} + C = -0.5 + C$, de donde $C = 2.5$.
> > 
> > **Respuesta:** $q(t) = -0.5e^{-t} + 2.5$ coulombs.
> > 
> > Verificación: $q'(t) = 0.5e^{-t} = i(t)$ ✓ y $q(0) = -0.5 + 2.5 = 2$ ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Explico por qué existe la constante de integración (la derivada anula las constantes).
> - [ ] Escribo siempre la familia completa $F(x) + C$ en una integral indefinida.
> - [ ] Interpreto geométricamente la $C$ como desplazamiento vertical de una familia de curvas.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo problemas de valor inicial en tres pasos con la condición dada.
> - [ ] Combino varias integrales en una sola expresión con una única $C$.
> - [ ] Traduzco cada contexto (velocidad, carga, población) a su condición inicial correspondiente.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo integraciones sucesivas distinguiendo $C_1$, $C_2$ y su significado físico.
> - [ ] Relaciono el orden de una EDO con el número de constantes y de condiciones necesarias.
> - [ ] Explico la $C$ como el núcleo del operador derivada en el lenguaje de análisis funcional.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: problemas de valor inicial.
> - R. Larson, *Cálculo* (Cengage), cap. 5: la constante de integración.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 5: familias de curvas.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — la notación que aquí se completa con la $C$.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la segunda parte, donde la $C$ se cancela.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — la tabla a la que siempre se le añade $+C$.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Por qué existe la constante de integración?::Porque derivar anula las constantes: $\frac{d}{dx}(F+C) = f$ para cualquier $C$, así que la integral devuelve una familia entera.
> - ¿Qué representa geométricamente la $C$?::Un desplazamiento vertical: todas las curvas de la familia tienen la misma forma y la misma pendiente en cada punto.
> - ¿Cómo fijo el valor de $C$?::Con una condición inicial: se integra, se sustituye $y(x_0) = y_0$ y se despeja $C$.
> - ¿Se conserva la $C$ en una integral definida?::No: $(F(b)+C) - (F(a)+C) = F(b) - F(a)$, se cancela en la evaluación.
> - ¿Cuántas constantes aporta una EDO de orden $n$?::$n$ constantes ($C_1, \ldots, C_n$), y por eso hacen falta $n$ condiciones iniciales.
> - ¿Cuántas $C$ se escriben al integrar varios términos?::Una sola: las constantes particulares se combinan ($C = C_1 + C_2 + \ldots$).

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — de donde sale la familia $F(x) + C$.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — el problema de valor inicial visto desde las propiedades.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la regla de Barrow, donde la $C$ se cancela.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — la tabla de fórmulas, siempre con $+C$.
> - [[1er Semestre/Física Mecánica/01 - Cinemática/Cinemática Traslacional|Cinemática Traslacional]] — donde las condiciones iniciales fijan constantes con nombre propio (velocidad y posición iniciales).
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — el análogo de las derivadas: allí hace falta un punto, aquí una condición inicial.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 2 y 4: valor inicial y constantes combinadas, los dos casos mínimos.
> - Después salta al 3 y al 6, donde cada condición fija una constante con nombre (velocidad, carga).
> - Cuando lo tengas, ataca el 1 (integraciones sucesivas), que prepara las EDO de segundo orden.
> - Cierra con [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|Teorema Fundamental del Cálculo]], donde verás por qué la $C$ desaparece al evaluar límites.

---

**Tags:** #MATG1045 #unidad6 #constante-integracion #familia-curvas #problemas-valor-inicial #condiciones-iniciales #ecuaciones-diferenciales #aplicaciones-fisica

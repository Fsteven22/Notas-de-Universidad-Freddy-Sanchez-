---
dg-publish: true
tags: [MATG1045, unidad6, identidades-trigonometricas, producto-a-suma, reduccion-potencias, angulo-doble, suma-a-producto, weierstrass, integrales-trigonometricas]
---

# 🌊 Identidades Trigonométricas para Integrales

## 🎯 Introducción

> [!info] 💡 Por qué una identidad desbloquea una integral
>
> Las **identidades trigonométricas** transforman integrales que parecen imposibles en formas integrables estándar: productos en sumas, potencias en múltiples ángulos y racionales en trigonometría en integrales de $t$.
>
> **Por qué importa:** la filosofía es *lo que parece imposible de integrar a menudo solo necesita la identidad correcta*. Reconocer el patrón antes de calcular es lo que separa un ejercicio resuelto de uno atascado.
>
> **Ejemplo:** $\int \sin(3x)\cos(5x)\,dx$ no tiene antiderivada directa, pero la identidad de producto a suma la convierte en dos senos integrables.

> [!warning] ⚠️ Los tres errores que más se repiten
>
> 1. **NO** olvides el factor $\frac{1}{2}$ en producto a suma: es el que más se escapa.
> 2. **NO** dejes signos malos al usar $\sin(-\theta) = -\sin\theta$ tras aplicar la identidad.
> 3. **NO** integres sin simplificar antes: reducir potencias y factorizar primero acorta el cálculo a la mitad.
>
> **Por qué importa:** los tres son errores de mecánica que arruinan un planteamiento correcto; una comprobación derivando los detecta al instante.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Producto a suma
>
> Las identidades de **producto a suma** convierten productos de funciones trigonométricas en sumas:
>
> $$\sin A \cos B = \tfrac{1}{2}[\sin(A+B) + \sin(A-B)], \qquad \cos A \sin B = \tfrac{1}{2}[\sin(A+B) - \sin(A-B)]$$
>
> $$\cos A \cos B = \tfrac{1}{2}[\cos(A+B) + \cos(A-B)], \qquad \sin A \sin B = \tfrac{1}{2}[\cos(A-B) - \cos(A+B)]$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Identidades_Trigonométricas_para_Integrales_01.svg]]
>
> **Se lee así:** el diagrama entra por un rectángulo de producto trigonométrico y llega a un **rombo de decisión** que pregunta por el tipo de producto. De ahí salen tres ramas paralelas, una por cada par de funciones, y cada una lleva a su fórmula correspondiente; las tres vuelven a converger en una caja final de integral de sumas simples.
>
> **Por qué importa:** fíjate en que el rombo te obliga a **clasificar antes de calcular**. Esto te evita intentar integrar el producto directamente y te muestra que las tres salidas desembocan en el mismo tipo de integral, la de sumas simples.
>
> **Ejemplo:** en $\int \cos(4x)\cos(x)\,dx$ caes en la rama cos·cos y se convierte en $\frac{1}{2}[\cos(5x) + \cos(3x)]$ antes de integrar.

> [!note] 📋 Reducción de potencias
>
> Para integrar **potencias de funciones trigonométricas**, se expresan en múltiples ángulos:
>
> $$\sin^2 x = \frac{1 - \cos 2x}{2}, \qquad \cos^2 x = \frac{1 + \cos 2x}{2}, \qquad \tan^2 x = \sec^2 x - 1$$
>
> Y para exponentes impares: $\sin^3 x = \dfrac{3\sin x - \sin 3x}{4}$, $\cos^3 x = \dfrac{3\cos x + \cos 3x}{4}$.
>
> | Potencia | Identidad de reducción | Forma integrable |
> |---|---|---|
> | $\sin^2 x$ | $\frac{1 - \cos 2x}{2}$ | $\frac{1}{2}\left(x - \frac{\sin 2x}{2}\right)$ |
> | $\cos^2 x$ | $\frac{1 + \cos 2x}{2}$ | $\frac{1}{2}\left(x + \frac{\sin 2x}{2}\right)$ |
> | $\sin^4 x$ | $\frac{3 - 4\cos 2x + \cos 4x}{8}$ | términos lineales en $x$ |
>
> **Por qué importa:** sin esta reducción, $\int \sin^2 x\,dx$ no tiene antiderivada elemental en esa forma; con ella se vuelve un coseno de ángulo doble más una constante.
>
> **Ejemplo:** $\int \sin^2(3x)\,dx = \int \frac{1 - \cos(6x)}{2}\,dx = \frac{x}{2} - \frac{\sin(6x)}{12} + C$.

> [!note] 📋 Definición — Suma a producto y ángulo doble
>
> **Suma a producto** (para factorizar):
>
> $$\sin A + \sin B = 2\sin\!\left(\frac{A+B}{2}\right)\cos\!\left(\frac{A-B}{2}\right), \qquad \cos A - \cos B = -2\sin\!\left(\frac{A+B}{2}\right)\sin\!\left(\frac{A-B}{2}\right)$$
>
> **Ángulo doble** (para expandir): $\sin 2x = 2\sin x\cos x$ y $\cos 2x = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Identidades_Trigonométricas_para_Integrales_02.svg]]
>
> **Se lee así:** como una cadena de cinco rectángulos: la suma trigonométrica pasa por un paso de factorización, luego por un producto de factores, después por una sustitución del tipo $u = \ldots$ y termina en una integral estándar. Aparte aparecen dos pares de cajas, sin flechas hacia la cadena principal, que muestran una suma concreta y el producto factorizado equivalente.
>
> **Por qué importa:** aquí la identidad no es un truco suelto: es un paso que abre la puerta a la sustitución y a las integrales estándar. Te da el orden exacto: factorizar, sustituir, integrar.
>
> **Ejemplo:** el diagrama ilustra el paso con $\cos A - \cos B$, que se factoriza como $-2\sin\!\left(\frac{A+B}{2}\right)\sin\!\left(\frac{A-B}{2}\right)$ para poder integrarla por sustitución.

> [!note] 📋 Sustitución de Weierstrass
>
> Para integrales **racionales en seno y coseno** se usa $t = \tan\!\left(\dfrac{x}{2}\right)$, con las conversiones:
>
> $$\sin x = \frac{2t}{1+t^2}, \qquad \cos x = \frac{1-t^2}{1+t^2}, \qquad dx = \frac{2}{1+t^2}\,dt.$$
>
> | Tipo de integral | Sustitución | Resultado |
> |---|---|---|
> | $\int \frac{dx}{a + b\cos x}$ | $t = \tan(x/2)$ | integral racional en $t$ |
> | $\int \frac{dx}{a + b\sin x}$ | $t = \tan(x/2)$ | integral racional en $t$ |
> | $\int R(\sin x, \cos x)\,dx$ | $t = \tan(x/2)$ | función racional en $t$ |
>
> **Por qué importa:** es la red de seguridad universal: toda integral racional en seno y coseno se vuelve racional en $t$, que se resuelve por fracciones parciales.
>
> **Ejemplo:** $\int \frac{dx}{2 + \cos x}$ con la sustitución da $\int \frac{2\,dt}{3 + t^2} = \frac{2}{\sqrt 3}\arctan\!\left(\frac{t}{\sqrt 3}\right) + C$.

---

## 🎲 Cómo elegir la identidad

> [!info] 🖼️ El árbol de decisión
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Identidades_Trigonométricas_para_Integrales_03.svg]]
>
> **Se lee así:** como un árbol de decisión. La integral trigonométrica entra a un rombo que pregunta por el tipo de expresión, y de ahí salen cuatro ramas: producto de funciones, potencias, suma de funciones o expresión racional. Cada rama lleva a su identidad, y de cada identidad sale un rectángulo con el paso final: integrar sumas simples, integrar términos lineales, factorizar y sustituir o resolver una integral racional en $t$.
>
> **Por qué importa:** el diagrama quita el *adivinar y probar*: antes de escribir un solo paso tienes que clasificar la expresión y elegir la identidad. Te evita perder tiempo con trigonométricas que no tienen antiderivada elemental en la forma en que están escritas.
>
> **Ejemplo:** con $t = \tan(x/2)$ resuelves la integral de la nota $\int \frac{dx}{2 + \cos x}$, que al cambiar de variable se transforma en $\int \frac{2\,dt}{3 + t^2}$.

> [!tip] 🔧 La regla de decisión en cuatro pasos
>
> 1. **¿Hay un producto de dos funciones distintas?** → producto a suma.
> 2. **¿Hay una potencia par de seno o coseno?** → reducción de potencias.
> 3. **¿Hay una suma de dos senos o cosenos?** → suma a producto.
> 4. **¿Es racional en seno y coseno?** → Weierstrass $t = \tan(x/2)$.
>
> **Por qué importa:** este orden de preguntas reproduce el árbol de decisión de la figura y te da un procedimiento fijo en vez de intuición.
>
> **Ejemplo:** $\int \sin^3 x \cos^2 x\,dx$ no cae en ninguna de las cuatro (es producto de potencias impares): se reserva un seno para el diferencial y se reduce el resto con $\sin^2 = 1 - \cos^2$.

---

## 🧮 Ejemplos resueltos

> [!example] 🔢 Producto sen·cos: $\int \sin(3x)\cos(5x)\,dx$
>
> $$\sin(3x)\cos(5x) = \tfrac{1}{2}[\sin(8x) + \sin(-2x)] = \tfrac{1}{2}[\sin(8x) - \sin(2x)]$$
>
> $$\int \sin(3x)\cos(5x)\,dx = \tfrac{1}{2}\left[-\frac{\cos(8x)}{8} + \frac{\cos(2x)}{2}\right] + C = -\frac{\cos(8x)}{16} + \frac{\cos(2x)}{4} + C$$
>
> **Por qué importa:** es el caso mínimo del árbol: identificar la rama, aplicar la fórmula y notar el signo de $\sin(-2x)$.

> [!example] 🔢 Potencia par: $\int \sin^2 x\,dx$
>
> $$\int \sin^2 x\,dx = \int \frac{1 - \cos 2x}{2}\,dx = \frac{1}{2}\left[x - \frac{\sin 2x}{2}\right] + C = \frac{x}{2} - \frac{\sin 2x}{4} + C$$
>
> **Por qué importa:** muestra la potencia de la reducción: una potencia se vuelve un término lineal en $x$ y un coseno de ángulo doble.

> [!example] 🔢 Combinada: $\int \sin^2 x \cos^2 x\,dx$
>
> 1. **Patrón:** $\sin^2 x \cos^2 x = (\sin x \cos x)^2$.
> 2. **Ángulo doble:** $\sin x \cos x = \dfrac{\sin 2x}{2}$, luego $(\sin x\cos x)^2 = \dfrac{\sin^2 2x}{4}$.
> 3. **Reducir potencia:** $\sin^2 2x = \dfrac{1 - \cos 4x}{2}$.
> 4. **Integrar:** $\displaystyle\int \sin^2 x\cos^2 x\,dx = \frac{1}{8}\int (1 - \cos 4x)\,dx = \frac{x}{8} - \frac{\sin 4x}{32} + C$.
>
> **Por qué importa:** es el patrón de dos identidades encadenadas: primero expandir, después reducir. Ese encadenamiento es lo que aparece en los exámenes.

> [!example] 🔢 Racional trigonométrica: $\int \frac{dx}{2 + \cos x}$
>
> Con $t = \tan(x/2)$: $\cos x = \frac{1-t^2}{1+t^2}$ y $dx = \frac{2}{1+t^2}\,dt$, luego
>
> $$\int \frac{dx}{2 + \cos x} = \int \frac{2\,dt}{2(1+t^2) + (1-t^2)} = \int \frac{2\,dt}{3 + t^2} = \frac{2}{\sqrt 3}\arctan\!\left(\frac{t}{\sqrt 3}\right) + C = \frac{2}{\sqrt 3}\arctan\!\left(\frac{\tan(x/2)}{\sqrt 3}\right) + C.$$
>
> **Por qué importa:** demuestra la red de seguridad de Weierstrass: una fracción en seno y coseno se resuelve como cualquier racional.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco fallos típicos
>
> 1. **Olvidar el $\frac{1}{2}$** de producto a suma.
> 2. **Signos incorrectos:** $\cos A \cos B = \frac{1}{2}[\cos(A+B) + \cos(A-B)]$ con **más**, no menos; y $\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$ con el orden invertido.
> 3. **No simplificar** antes de integrar (reducir potencias y factorizar primero).
> 4. **Usar Weierstrass a lo bestia:** $t = \tan(x/2)$ siempre funciona, pero deja la integral muy larga; prueba antes la vía directa.
> 5. **Integrar $\tan^2 x$ como si fuera potencia de seno:** se convierte con $\tan^2 x = \sec^2 x - 1$ directamente.
>
> **Por qué importa:** los tres primeros son de memoria y se corrigen con una comprobación derivando; los dos últimos, de estrategia, se corrigen con el árbol de decisión.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\int \cos(4x)\cos(x)\,dx$.
>
> > [!success]- ✅ Solución
> > 
> > Por producto a suma, rama cos·cos:
> > 
> > $$\cos(4x)\cos(x) = \tfrac{1}{2}[\cos(5x) + \cos(3x)]$$
> > 
> > $$\int \cos(4x)\cos(x)\,dx = \tfrac{1}{2}\left[\frac{\sin(5x)}{5} + \frac{\sin(3x)}{3}\right] + C = \frac{\sin(5x)}{10} + \frac{\sin(3x)}{6} + C.$$
> > 
> > **Respuesta:** $\dfrac{\sin(5x)}{10} + \dfrac{\sin(3x)}{6} + C$.

> [!example] 📋 Planteamiento
>
> Calcula $\int \cos^4 x\,dx$.
>
> > [!success]- ✅ Solución
> > 
> > Se reduce dos veces con $\cos^2 x = \frac{1 + \cos 2x}{2}$:
> > 
> > $$\cos^4 x = \left(\frac{1 + \cos 2x}{2}\right)^2 = \frac{1 + 2\cos 2x + \cos^2 2x}{4} = \frac{1 + 2\cos 2x + \frac{1 + \cos 4x}{2}}{4} = \frac{3 + 4\cos 2x + \cos 4x}{8}.$$
> > 
> > Integrando: $\displaystyle\int \cos^4 x\,dx = \frac{3x}{8} + \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + C$.
> > 
> > **Respuesta:** $\dfrac{3x}{8} + \dfrac{\sin 2x}{4} + \dfrac{\sin 4x}{32} + C$.

> [!example] 📋 Planteamiento
>
> Resuelve $\int \sin^3 x \cos^2 x\,dx$.
>
> > [!success]- ✅ Solución
> > 
> > Se reserva un $\sin x$ para el diferencial ($d(-\cos x) = \sin x\,dx$) y el resto se convierte en cosenos con $\sin^2 x = 1 - \cos^2 x$:
> > 
> > $$\int \sin^3 x \cos^2 x\,dx = \int (1 - \cos^2 x)\cos^2 x \cdot \sin x\,dx.$$
> > 
> > Con $u = \cos x$, $du = -\sin x\,dx$:
> > 
> > $$-\int (1 - u^2)u^2\,du = -\left(\frac{u^3}{3} - \frac{u^5}{5}\right) + C = \frac{\cos^5 x}{5} - \frac{\cos^3 x}{3} + C.$$
> > 
> > **Respuesta:** $\dfrac{\cos^5 x}{5} - \dfrac{\cos^3 x}{3} + C$.

> [!example] 📋 Planteamiento
>
> Calcula $\int \frac{dx}{1 + \sin x}$.
>
> > [!success]- ✅ Solución
> > 
> > Con Weierstrass $t = \tan(x/2)$: $\sin x = \frac{2t}{1+t^2}$, $dx = \frac{2\,dt}{1+t^2}$:
> > 
> > $$\int \frac{dx}{1 + \sin x} = \int \frac{2\,dt}{(1+t^2) + 2t} = \int \frac{2\,dt}{(1+t)^2} = -\frac{2}{1+t} + C = -\frac{2}{1 + \tan(x/2)} + C.$$
> > 
> > **Respuesta:** $-\dfrac{2}{1 + \tan(x/2)} + C$.
> > 
> > Alternativa sin Weierstrass: multiplicar y dividir por $1 - \sin x$ y usar $\cos^2 x$ en el denominador.

> [!example] 📋 Planteamiento
>
> Convierte $\sin A + \sin B$ en producto y explica por qué eso desbloquea una integral como $\int [\sin(5x) + \sin(3x)]\,dx$ de otra forma.
>
> > [!success]- ✅ Solución
> > 
> > $$\sin A + \sin B = 2\sin\!\left(\frac{A+B}{2}\right)\cos\!\left(\frac{A-B}{2}\right).$$
> > 
> > Para $A = 5x$, $B = 3x$: $\sin(5x) + \sin(3x) = 2\sin(4x)\cos(x)$.
> > 
> > **Respuesta:** la suma se vuelve un producto; en este caso concreto la suma ya era integrable directamente, pero cuando aparece como **resultado** de otra manipulación (no como integral suelta), el producto abre la vía por partes o por sustitución.
> > 
> > Verificación: derivar $2\sin(4x)\cos(x)$ devuelve $\sin(5x) + \sin(3x)$ ✓

> [!example] 📋 Planteamiento
>
> Deduce $\int \frac{\cos x}{2 + \sin x}\,dx$ y verifica el resultado.
>
> > [!success]- ✅ Solución
> > 
> > El numerador es casi el diferencial del denominario: si $u = 2 + \sin x$, entonces $du = \cos x\,dx$.
> > 
> > $$\int \frac{\cos x}{2 + \sin x}\,dx = \int \frac{du}{u} = \ln|u| + C = \ln|2 + \sin x| + C.$$
> > 
> > **Respuesta:** $\ln|2 + \sin x| + C$.
> > 
> > Verificación: $\frac{d}{dx}\ln(2 + \sin x) = \frac{\cos x}{2 + \sin x}$ ✓ (aquí no hizo falta ninguna identidad: la clasificación del árbol empieza descartando el caso racional).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo de memoria las cuatro identidades de producto a suma con sus signos correctos.
> - [ ] Reduzco potencias pares de seno y coseno a múltiplos de ángulo.
> - [ ] Expando y factorizo con las fórmulas de ángulo doble y mitad.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Clasifico una integral trigonométrica con el árbol de decisión y elijo la identidad sin probar a ciegas.
> - [ ] Encadeno dos identidades (ángulo doble + reducción) para potencias de producto.
> - [ ] Aplico la sustitución de Weierstrass a una racional en seno y coseno.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo $\int \sin^m x \cos^n x\,dx$ con la estrategia de reservar un factor para el diferencial.
> - [ ] Deduzco las identidades de suma a producto a partir de las de producto a suma.
> - [ ] Eligo entre vía directa, Weierstrass y sustitución según el coste de cada camino.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 7: integrales trigonométricas e identidades.
> - R. Larson, *Cálculo* (Cengage), cap. 8: reducción de potencias y Weierstrass.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 6: estrategias de integración.
> - [[Preuniversitario/Matemáticas/Unidad 3 - Funciones y Trigonometría/II - Trigonometría/05 - Identidades trigonométricas|05 - Identidades trigonométricas]] — el fundamento teórico previo.
> - [[Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — la técnica con la que se consumen estas identidades.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — el destino final de las formas a las que aquí se llega.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué hace la identidad de producto a suma?::Convierte un producto de funciones trigonométricas en una suma integrable, con factor $\frac{1}{2}$ y combinaciones de $A+B$ y $A-B$.
> - ¿Cómo se integra $\sin^2 x$?::Con la reducción $\sin^2 x = \frac{1 - \cos 2x}{2}$, que da $\frac{x}{2} - \frac{\sin 2x}{4} + C$.
> - ¿Cuándo se usa la sustitución de Weierstrass?::Cuando la integral es racional en seno y coseno: $t = \tan(x/2)$ la convierte en racional en $t$.
> - ¿Qué hago con $\sin^3 x \cos^2 x$?::Reservo un $\sin x$ para el diferencial y convierto el resto en cosenos con $\sin^2 = 1 - \cos^2$.
> - ¿Qué signo lleva $\cos A \cos B$ en producto a suma?::$+$: $\frac{1}{2}[\cos(A+B) + \cos(A-B)]$; en $\sin A \sin B$ es $-$ con el orden invertido.
> - ¿Qué identidad convierte una suma en producto?::$\sin A + \sin B = 2\sin\!\left(\frac{A+B}{2}\right)\cos\!\left(\frac{A-B}{2}\right)$; sirve para factorizar.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Preuniversitario/Matemáticas/Unidad 3 - Funciones y Trigonometría/II - Trigonometría/05 - Identidades trigonométricas|05 - Identidades trigonométricas]] — de dónde salen todas las fórmulas de esta nota.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — la notación y la regla de potencia que aquí se combinan.
> - [[Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — el mecanismo que consume las identidades.
> - [[Unidad 6 - Integrales/Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — las técnicas completas con estas identidades como repertorio.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — las fórmulas directas que cierran cada caso.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — donde la sustitución trigonométrica reaparece en serio.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: producto a suma y reducción de potencias deben salirte sin mirar la tabla.
> - Después salta al 3 y al 4, donde se encadenan dos identidades y entra Weierstrass.
> - Cuando lo tengas, ataca el 5 y el 6, que son de estrategia: deciden qué camino tomar antes de calcular.
> - Cierra con [[Unidad 6 - Integrales/Técnicas de Integración/03 - Integrales Trigonométricas|Integrales Trigonométricas]], donde este repertorio se aplica a ejercicios completos.

---

**Tags:** #MATG1045 #unidad6 #identidades-trigonometricas #producto-a-suma #reduccion-potencias #angulo-doble #suma-a-producto #weierstrass #integrales-trigonometricas

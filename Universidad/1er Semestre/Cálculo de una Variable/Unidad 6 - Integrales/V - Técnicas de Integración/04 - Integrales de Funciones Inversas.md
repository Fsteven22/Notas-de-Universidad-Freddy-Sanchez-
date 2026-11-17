---
dg-publish: true
tags: [MATG1045, unidad6, integrales-de-funciones-inversas, integrales, funciones-inversas, integracion-por-partes, arcsin, arccos, arctan, arcsec, identidades-trigonometricas]
---

# 🔄 Integrales de Funciones Inversas

## 🎯 Introducción

> [!info] 💡 Qué son y por qué se resuelven siempre igual
>
> Las **integrales de funciones inversas** son aquellas cuyo integrando es una función inversa: $\int \arcsin(x)\,dx$, $\int \arccos(x)\,dx$, $\int \arctan(x)\,dx$, $\int \text{arcsec}(x)\,dx$ y sus compañeras. No hay una tabla infinita que memorizar: **todas** se resuelven con **integración por partes**, tomando la función inversa como $u$ y $dx$ como $dv$, de modo que la derivada de la inversa convierta la integral residual en algo elemental.
>
> **Por qué importa:** es el caso donde la técnica de por partes rinde al máximo: una función que no sabes integrar de golpe (¿cuál es la antiderivada de $\arctan$?) se deriva sin problema y la integral que queda sí es inmediata. Además, es el puente natural a $\int \ln(x)\,dx$ y a las integrales definidas notables.
>
> **Ejemplo:** $\int \arctan(x)\,dx = x\arctan(x) - \frac{1}{2}\ln(1+x^2) + C$: la derivada de $\arctan$ es $\frac{1}{1+x^2}$, y con $w = 1+x^2$ la residual se integra de una sola vez.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — el método general $\int f^{-1}(x)\,dx$ y la tabla de derivadas de las inversas.
> - **Las tres parejas** — arcoseno/arcocoseno, arcotangente/arcocotangente y arcosecante/arcocosecante, con sus ejemplos.
> - **Productos y potencias** — $x\arcsin(x)$ y $\arctan^2(x)$, el caso que no se cierra.
> - **Identidades y tablas** — relaciones entre inversas y los resultados de consulta.
> - **Avanzados y práctica** — composiciones, integrales definidas notables y los nueve ejercicios.
>
> **Por qué importa:** el hilo de toda la nota es uno solo — *la inversa va como $u$* —; lo demás son variantes de ese reparto y los cuidados de dominio que las acompañan.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Método general: integración por partes para $\int f^{-1}(x)\,dx$
>
> Para resolver $\int f^{-1}(x)\,dx$, usar:
>
> - **$u = f^{-1}(x)$** (la función inversa).
> - **$dv = dx$** $\Rightarrow$ **$v = x$**.
> - **$du = (f^{-1})'(x)\,dx$** (usar la derivada de la función inversa).
> - **Resultado:** $x \cdot f^{-1}(x) - \int x \cdot (f^{-1})'(x)\,dx$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_de_Funciones_Inversas_01.svg]]
>
> **Se lee así:** una caja con el patrón general $\int f^{-1}(x)\,dx$ abre el diagrama y se abre en tres cajas hermanas que corresponden a las tres decisiones de la integración por partes: qué se toma como $u$, qué se toma como $dv$ con su $v$ y cuál es el $du$. Las tres convergen en una sola caja donde se enuncia la fórmula del resultado, y de esa caja sale una última advertencia roja con el criterio para elegir las piezas.
>
> **Por qué importa:** te da la receta única para integrar una función inversa, que **siempre** empieza por ponerla como $u$. Y te recuerda la condición de fondo: si la integral que queda no es más simple que la original, hay que cambiar la elección.
>
> **Ejemplo:** para $\int \arctan(x)\,dx$ tomas $u = \arctan(x)$, $v = x$ y resuelves la residual con $w = 1+x^2$, obteniendo $x\arctan(x) - \frac{1}{2}\ln(1+x^2) + C$.

> [!tip] 🧮 Derivadas y dominios de las funciones inversas
>
> | Función inversa | Derivada | Dominio |
> |---|---|---|
> | $\arcsin(x)$ | $\frac{1}{\sqrt{1-x^2}}$ | $[-1, 1]$ |
> | $\arccos(x)$ | $-\frac{1}{\sqrt{1-x^2}}$ | $[-1, 1]$ |
> | $\arctan(x)$ | $\frac{1}{1+x^2}$ | $\mathbb{R}$ |
> | $\text{arccot}(x)$ | $-\frac{1}{1+x^2}$ | $\mathbb{R}$ |
> | $\text{arcsec}(x)$ | $\frac{1}{\|x\|\sqrt{x^2-1}}$ | $\|x\| \geq 1$ |
> | $\text{arccsc}(x)$ | $-\frac{1}{\|x\|\sqrt{x^2-1}}$ | $\|x\| \geq 1$ |
>
> **Por qué importa:** estas seis derivadas son **el motor** de toda la nota: el $du$ de cada por partes sale de aquí. Fíjate en que las tres primeras son positivas y sus parejas negativas, y que el valor absoluto de arcsec/arccsc es el que hace falta para que la derivada cuadre en ambos semiejes.

---

## 📐 Arcoseno y arcocoseno

> [!info] 🧮 Fórmulas básicas de la pareja
>
> - $\frac{d}{dx}[\arcsin(x)] = \frac{1}{\sqrt{1-x^2}}$
> - $\frac{d}{dx}[\arccos(x)] = -\frac{1}{\sqrt{1-x^2}}$
> - **Identidad útil:** $\arcsin(x) + \arccos(x) = \frac{\pi}{2}$
>
> **Por qué importa:** la identidad te ahorra resolver la segunda integral de la pareja: como las dos suman $\pi/2$, sus antiderivadas difieren solo en una constante (y en el signo de la raíz).

> [!example] 🔢 Ejemplo 1 — integral de arcoseno
>
> **Resolver:** $\int \arcsin(x)\,dx$
>
> - **Integración por partes:** $u = \arcsin(x)$, $dv = dx$ → $du = \frac{1}{\sqrt{1-x^2}}\,dx$, $v = x$
> - $\int \arcsin(x)\,dx = x\arcsin(x) - \int \frac{x}{\sqrt{1-x^2}}\,dx$
> - Para la segunda integral: $w = 1-x^2 \Rightarrow dw = -2x\,dx$, luego $\int \frac{x}{\sqrt{1-x^2}}\,dx = -\frac{1}{2}\int w^{-1/2}\,dw = -\sqrt{w} = -\sqrt{1-x^2}$
> - **Resultado:** $\int \arcsin(x)\,dx = x\arcsin(x) + \sqrt{1-x^2} + C$
>
> **Por qué importa:** el signo doble (el $-$ de la fórmula y el $-$ del $dw$) es lo que convierte la resta en suma; verificando, $\frac{d}{dx}\big[x\arcsin(x) + \sqrt{1-x^2}\big] = \arcsin(x) + \frac{x}{\sqrt{1-x^2}} - \frac{x}{\sqrt{1-x^2}} = \arcsin(x)$ ✓

> [!example] 🖼️ El ejemplo 1, paso a paso en un diagrama
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_de_Funciones_Inversas_02.svg]]
>
> **Se lee así:** una cadena vertical de seis rectángulos sin ramas: arranca con el esqueleto de la integral de arcoseno y avanza paso a paso. De la primera caja sale el bloque de integración por partes con el reparto de $u$, $dv$, $du$ y $v$; luego dos cajas encadenadas muestran la integral que sobra y su antiderivada elemental, y al final una caja de resultado y otra de verificación por derivada.
>
> **Por qué importa:** **cada paso queda justificado**, así evitas saltarte la integral residual y reconoces que el truco está en ver que ya es elemental. La verificación por derivada es tu red de seguridad cuando el signo de la raíz no parece cuadrar.
>
> **Ejemplo:** en $\int \arcsin(x)\,dx$ el diagrama desglosa el cálculo hasta llegar a $x\arcsin(x) + \sqrt{1-x^2} + C$.

> [!example] 🔢 Ejemplo 2 — integral de arcocoseno
>
> **Resolver:** $\int \arccos(x)\,dx$
>
> - **Integración por partes:** $u = \arccos(x)$, $dv = dx$ → $du = -\frac{1}{\sqrt{1-x^2}}\,dx$, $v = x$
> - $\int \arccos(x)\,dx = x\arccos(x) + \int \frac{x}{\sqrt{1-x^2}}\,dx$
> - La segunda integral es la misma del ejemplo anterior: $-\sqrt{1-x^2}$
> - **Resultado:** $\int \arccos(x)\,dx = x\arccos(x) - \sqrt{1-x^2} + C$
>
> **Por qué importa:** comparalo con el ejemplo 1: la derivada negativa de $\arccos$ invierte el signo de la raíz en el resultado. Diferencia de un signo, no de un método.

---

## 🧭 Arcotangente y arcosecante

> [!info] 🧮 Fórmulas básicas de arcotangente y arcocotangente
>
> - $\frac{d}{dx}[\arctan(x)] = \frac{1}{1+x^2}$
> - $\frac{d}{dx}[\text{arccot}(x)] = -\frac{1}{1+x^2}$
> - **Identidad útil:** $\arctan(x) + \text{arccot}(x) = \frac{\pi}{2}$
>
> **Por qué importa:** $\frac{1}{1+x^2}$ es la derivada perfecta para por partes: la residual se vuelve $\int \frac{x}{1+x^2}\,dx$, que es logaritmo puro con $w = 1+x^2$.

> [!example] 🔢 Ejemplo 3 — integral de arcotangente
>
> **Resolver:** $\int \arctan(x)\,dx$
>
> - **Integración por partes:** $u = \arctan(x)$, $dv = dx$ → $du = \frac{1}{1+x^2}\,dx$, $v = x$
> - $\int \arctan(x)\,dx = x\arctan(x) - \int \frac{x}{1+x^2}\,dx$
> - Para la segunda integral: $w = 1+x^2 \Rightarrow dw = 2x\,dx$, luego $\int \frac{x}{1+x^2}\,dx = \frac{1}{2}\ln(1+x^2)$
> - **Resultado:** $\int \arctan(x)\,dx = x\arctan(x) - \frac{1}{2}\ln(1+x^2) + C$
>
> **Por qué importa:** sin valor absoluto en el logaritmo porque $1+x^2 > 0$ siempre; este resultado es el que usarás mil veces en integrales definidas y en el método de Weierstrass.

> [!info] 🧮 Fórmulas básicas de arcosecante y arcocosecante
>
> - $\frac{d}{dx}[\text{arcsec}(x)] = \frac{1}{\|x\|\sqrt{x^2-1}}$ para $\|x\| > 1$
> - $\frac{d}{dx}[\text{arccsc}(x)] = -\frac{1}{\|x\|\sqrt{x^2-1}}$ para $\|x\| > 1$
>
> **Por qué importa:** el valor absoluto no es decorativo: con $x > 1$ se puede quitar y la integral residual queda $\int \frac{1}{\sqrt{x^2-1}}\,dx = \ln\|x + \sqrt{x^2-1}\| + C$, una fórmula de la tabla de integrales notables.

> [!example] 🔢 Ejemplo 4 — integral de arcosecante
>
> **Resolver:** $\int \text{arcsec}(x)\,dx$ para $x > 1$
>
> - **Integración por partes:** $u = \text{arcsec}(x)$, $dv = dx$ → $du = \frac{1}{x\sqrt{x^2-1}}\,dx$ (aquí $x > 1$), $v = x$
> - $\int \text{arcsec}(x)\,dx = x\,\text{arcsec}(x) - \int \frac{1}{\sqrt{x^2-1}}\,dx$
> - La segunda integral es estándar: $\int \frac{1}{\sqrt{x^2-1}}\,dx = \ln\|x + \sqrt{x^2-1}\|$
> - **Resultado:** $\int \text{arcsec}(x)\,dx = x\,\text{arcsec}(x) - \ln\|x + \sqrt{x^2-1}\| + C$
>
> **Por qué importa:** el $x$ del $v$ cancela exactamente el $x$ del denominador del $du$; ese cancelamiento es la razón por la que por partes funciona tan bien con las inversas.

---

## 🔢 Productos y potencias

> [!example] 🔢 Ejemplo 5 — producto con variable
>
> **Resolver:** $\int x \arcsin(x)\,dx$
>
> - **Integración por partes:** $u = \arcsin(x)$, $dv = x\,dx$ → $du = \frac{1}{\sqrt{1-x^2}}\,dx$, $v = \frac{x^2}{2}$
> - $\int x \arcsin(x)\,dx = \frac{x^2}{2}\arcsin(x) - \int \frac{x^2}{2\sqrt{1-x^2}}\,dx$
> - Para la segunda integral, usar $x^2 = 1-(1-x^2)$:
> $\int \frac{x^2}{\sqrt{1-x^2}}\,dx = \int \frac{1}{\sqrt{1-x^2}}\,dx - \int \sqrt{1-x^2}\,dx = \arcsin(x) - \frac{1}{2}\big(x\sqrt{1-x^2} + \arcsin(x)\big) = \frac{1}{2}\arcsin(x) - \frac{x\sqrt{1-x^2}}{2}$
> - **Resultado:** $\int x \arcsin(x)\,dx = \frac{x^2}{2}\arcsin(x) - \frac{1}{4}\arcsin(x) + \frac{x\sqrt{1-x^2}}{4} + C$
>
> **Por qué importa:** el truco de escribir $x^2 = 1 - (1-x^2)$ convierte la residual en dos integrales de tabla. Este es el patrón de los productos $x \cdot f^{-1}(x)$: por partes una vez y después solo tablas.

> [!warning] 🔢 Ejemplo 6 — potencia de arcotangente: el caso que no se cierra
>
> **Intentar:** $\int \arctan^2(x)\,dx$
>
> - **Primera por partes** ($u = \arctan^2(x)$, $dv = dx$): $x\arctan^2(x) - 2\int \frac{x\arctan(x)}{1+x^2}\,dx$
> - **En la residual**, con $t = \arctan(x)$ se convierte en $\int t\tan(t)\,dt$, que por partes otra vez se reduce a $-t\ln(\cos t) + \int \ln(\cos t)\,dt$
> - **Aviso:** esa última integral **no tiene primitiva elemental** (se expresa con funciones especiales como el dilogaritmo $\text{Li}_2$), y lo mismo le pasa a la residual original $\int \frac{\ln(1+x^2)}{1+x^2}\,dx$. El procedimiento de por partes es correcto, pero la integral no se cierra con elementos básicos.
> - **En la práctica:** $\int \arctan^2(x)\,dx$ se trabaja como **integral definida** o con métodos numéricos/series; el ejercicio útil es llegar hasta aquí y reconocer el callejón.
>
> **Por qué importa:** es el contraejemplo que enseña que *fácil de plantear* no significa *antiderivada elemental*: junto con $\int e^{-x^2}$ o $\int \frac{\sin x}{x}$, pertenece a la lista de integrales sin forma cerrada. Reconocerlo a tiempo te evita girar en círculo buscando una sustitución que no existe.

---

## 🔄 Identidades y relaciones

> [!info] 🧮 Relaciones complementarias
>
> - $\arcsin(x) + \arccos(x) = \frac{\pi}{2}$
> - $\arctan(x) + \text{arccot}(x) = \frac{\pi}{2}$
> - $\text{arcsec}(x) + \text{arccsc}(x) = \frac{\pi}{2}$ para $x > 0$
>
> **Por qué importa:** resuelves una y la otra sale por resta con $\pi/2$; también te permiten reescribir respuestas equivalentes en forma de arcoseno o de arccoseno sin que la corrección las marque como distintas.

> [!note] 🧮 Identidades trigonométricas para inversas
>
> - $\sin(\arcsin(x)) = x$
> - $\cos(\arcsin(x)) = \sqrt{1-x^2}$
> - $\tan(\arcsin(x)) = \frac{x}{\sqrt{1-x^2}}$
> - $\sin(\arccos(x)) = \sqrt{1-x^2}$
> - $\cos(\arctan(x)) = \frac{1}{\sqrt{1+x^2}}$
> - $\sin(\arctan(x)) = \frac{x}{\sqrt{1+x^2}}$
>
> **Por qué importa:** son la vía para **volver a $x$** cuando una sustitución te deja el resultado en función del ángulo; se construyen con el triángulo de referencia, igual que en las sustituciones trigonométricas.

> [!info] 🧮 Relaciones de conversión
>
> - $\arcsin(x) = \arctan\left(\frac{x}{\sqrt{1-x^2}}\right)$
> - $\arccos(x) = \arctan\left(\frac{\sqrt{1-x^2}}{x}\right)$ para $x > 0$
> - $\text{arcsec}(x) = \arccos\left(\frac{1}{x}\right)$ para $\|x\| \geq 1$
>
> **Por qué importa:** cuando una respuesta sale en $\arctan$ y el enunciado pide $\arcsin$ (o al revés), estas conversiones te ahorran rehacer el ejercicio; la tercera es la definición misma de arcosecante.

---

## 📊 Tablas de consulta

> [!tip] 📋 Resultados fundamentales
>
> | Función | Integral |
> |---|---|
> | $\arcsin(x)$ | $x\arcsin(x) + \sqrt{1-x^2} + C$ |
> | $\arccos(x)$ | $x\arccos(x) - \sqrt{1-x^2} + C$ |
> | $\arctan(x)$ | $x\arctan(x) - \frac{1}{2}\ln(1+x^2) + C$ |
> | $\text{arccot}(x)$ | $x\,\text{arccot}(x) + \frac{1}{2}\ln(1+x^2) + C$ |
> | $\text{arcsec}(x)$ | $x\,\text{arcsec}(x) - \ln\|x + \sqrt{x^2-1}\| + C$ |
> | $\text{arccsc}(x)$ | $x\,\text{arccsc}(x) + \ln\|x + \sqrt{x^2-1}\| + C$ |
>
> **Por qué importa:** son las seis salidas de los ejemplos 1 a 4; si tu respuesta no se parece a ninguna, revisa el signo del $du$ antes de seguir.

> [!tip] 📋 Integrales con productos simples
>
> | Función | Integral |
> |---|---|
> | $x\arcsin(x)$ | $\frac{x^2}{2}\arcsin(x) - \frac{1}{4}\arcsin(x) + \frac{x\sqrt{1-x^2}}{4} + C$ |
> | $x\arctan(x)$ | $\frac{x^2+1}{2}\arctan(x) - \frac{x}{2} + C$ |
> | $\frac{\arcsin(x)}{x}$ | No tiene forma cerrada elemental |
> | $\frac{\arctan(x)}{x}$ | Serie infinita o integral especial (dilogaritmo) |
>
> **Por qué importa:** las dos primeras filas se resuelven con por partes + tablas; las dos últimas te avisan de antemano de los callejones sin salida, para que no pierdas el examen persiguiendo una sustitución que no existe.

---

## ⚠️ Dominios y estrategias

> [!warning] 🚨 Dominios y cuidados en la integración
>
> **Dominios y rangos principales:**
>
> - $\arcsin(x)$, $\arccos(x)$: $x \in [-1, 1]$; rangos $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ y $[0, \pi]$.
> - $\arctan(x)$, $\text{arccot}(x)$: $x \in \mathbb{R}$; rangos $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ y $(0, \pi)$.
> - $\text{arcsec}(x)$, $\text{arccsc}(x)$: $\|x\| \geq 1$.
>
> **Cuidados en la integración:**
>
> - **Verificar el dominio** antes de aplicar fórmulas (el resultado debe vivir donde vivía el integrando).
> - **Considerar el signo** en las derivadas con valor absoluto ($\text{arcsec}$ con $x < -1$).
> - **Simplificar usando identidades** antes de integrar cuando sea posible.
>
> **Por qué importa:** los tres fallos son de **planteamiento** y ninguno avisa con error; el del valor absoluto en arcosecante es el que más se ignora porque en los ejercicios tipo siempre dan $x > 1$.

> [!success] 💡 Estrategias de éxito
>
> **Preparación:**
>
> - Memorizar las derivadas de las seis inversas (la tabla de Definiciones Formales).
> - Conocer las identidades básicas para simplificación.
> - Identificar el patrón antes de aplicar integración por partes.
>
> **Durante la resolución:**
>
> - **Siempre** usar $u =$ función inversa en la integración por partes.
> - Buscar simplificaciones usando identidades trigonométricas.
> - Verificar el dominio de validez de la solución.
>
> **Verificación:**
>
> - Derivar el resultado para comprobar que devuelve el integrando.
> - Verificar continuidad en los puntos críticos del dominio.
> - Comprobar casos límite cuando sea relevante.
>
> **Por qué importa:** la derivada final es el único control que detecta signos invertidos en el $du$; con seis fórmulas de tabla en la cabeza, el 90 % de estos ejercicios se cierra en tres renglones.

---

## 🚀 Casos avanzados

> [!example] 🔢 Ejemplo 7 — composición con argumento $x/a$
>
> **Resolver:** $\int \arcsin\left(\frac{x}{a}\right)\,dx$ donde $a > 0$
>
> - **Sustitución previa:** $u = \frac{x}{a} \Rightarrow x = au$, $dx = a\,du$
> - $\int \arcsin\left(\frac{x}{a}\right)\,dx = a\int \arcsin(u)\,du$
> - Usar el resultado conocido del ejemplo 1: $\int \arcsin(u)\,du = u\arcsin(u) + \sqrt{1-u^2} + C$
> - $= a\left[\frac{x}{a}\arcsin\left(\frac{x}{a}\right) + \sqrt{1-\frac{x^2}{a^2}}\right] + C$
> - **Resultado:** $x\arcsin\left(\frac{x}{a}\right) + \sqrt{a^2-x^2} + C$
>
> **Por qué importa:** la composición no cambia el método: primero se normaliza el argumento a $u$ y después entra la fórmula de la tabla. Nota que $\sqrt{a^2 - x^2}$ aparece solo si el resultado se factoriza con $a$ fuera.

> [!info] 🎯 Integrales definidas notables
>
> - $\int_0^1 \arcsin(x)\,dx = \frac{\pi}{2} - 1 \approx 0{,}5708$
> - $\int_0^1 \arctan(x)\,dx = \frac{\pi}{4} - \frac{\ln 2}{2} \approx 0{,}4388$
> - $\int_{-1}^1 x\arcsin(x)\,dx = \frac{\pi}{4} \approx 0{,}7854$ (**¡cuidado!** el integrando es **par**: impar × impar = par, así que la integral **no** es cero)
>
> **Por qué importa:** la tercera es la trampa clásica: parece de simetría y se resuelve bien aprovechando que es par ($2\int_0^1$), no anulándola. Las tres se obtienen con los resultados de la tabla evaluados en los extremos.

---

## 🗺️ Patrones de reconocimiento

> [!info] 🖼️ Dónde aparecen y cómo practicar
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_de_Funciones_Inversas_03.svg]]
>
> **Se lee así:** el diagrama tiene forma de árbol: una caja central con el patrón $\int f^{-1}(x)\,dx$ (aplicaciones y práctica) abre hacia cuatro destinos. Tres son aplicaciones —geometría con áreas y longitudes, longitudes de arco y probabilidad con distribuciones especiales— y uno es la caja de niveles de práctica, que a su vez se ramifica en tres: básico ($\arcsin(2x)$, $\arctan(3x)$, $x\arccos(x)$), intermedio ($\arcsin^2(x)$, $\arctan(x)/x^2$, $\text{arcsec}(\sqrt{x})$) y avanzado ($\arctan(x)\ln(x)$, combinaciones). Una quinta flecha lleva a un recuadro aparte con el patrón de las potencias.
>
> **Por qué importa:** te sirve para **ubicar un problema dentro de la ruta**: si te piden un área o una longitud de arco con inversa trigonométrica, ya sabes por dónde entrar. Y te avisa que las potencias, como $\arcsin^2(x)$, exigen por partes aplicadas **repetidamente**.
>
> **Ejemplo:** el ejercicio 4 de esta nota, $\int \arcsin^2(x)\,dx$, cae en el nivel intermedio y activa el patrón de por partes repetidas.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Resuelve $\int \arcsin(2x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución previa:** $u = 2x$, $du = 2\,dx$ → $\frac{1}{2}\int \arcsin(u)\,du = \frac{1}{2}\big[u\arcsin(u) + \sqrt{1-u^2}\big] + C$.
> > **Respuesta:** $x\arcsin(2x) + \frac{1}{2}\sqrt{1-4x^2} + C$.
> > **Control:** $\frac{d}{dx}\big[x\arcsin(2x)\big] = \arcsin(2x) + \frac{2x}{\sqrt{1-4x^2}}$ y $\frac{d}{dx}\frac{\sqrt{1-4x^2}}{2} = \frac{-2x}{\sqrt{1-4x^2}}$; sumando, cancelan ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \arctan(3x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Por partes:** $u = \arctan(3x)$, $dv = dx$ → $du = \frac{3}{1+9x^2}\,dx$, $v = x$.
> > $$x\arctan(3x) - \int \frac{3x}{1+9x^2}\,dx = x\arctan(3x) - \frac{1}{6}\ln(1+9x^2) + C$$
> > **Respuesta:** $x\arctan(3x) - \frac{1}{6}\ln(1+9x^2) + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int x\arccos(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Por partes:** $u = \arccos(x)$, $dv = x\,dx$ → $du = -\frac{1}{\sqrt{1-x^2}}\,dx$, $v = \frac{x^2}{2}$.
> > $$\frac{x^2}{2}\arccos(x) + \frac{1}{2}\int \frac{x^2}{\sqrt{1-x^2}}\,dx$$
> > Con $x^2 = 1-(1-x^2)$ la integral vale $\frac{1}{2}\big(\arcsin(x) - x\sqrt{1-x^2}\big)$ y, usando $\arcsin(x) = \frac{\pi}{2} - \arccos(x)$ (la constante se absorbe en $C$):
> > **Respuesta:** $\frac{2x^2-1}{4}\arccos(x) - \frac{x\sqrt{1-x^2}}{4} + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \arcsin^2(x)\,dx$ (por partes repetidas).
>
> > [!success]- ✅ Solución
> >
> > **Primera por partes** ($u = \arcsin^2(x)$, $dv = dx$): $x\arcsin^2(x) - 2\int \frac{x\arcsin(x)}{\sqrt{1-x^2}}\,dx$.
> > **Segunda por partes** en la residual ($u = \arcsin(x)$, $dv = \frac{x}{\sqrt{1-x^2}}\,dx \Rightarrow v = -\sqrt{1-x^2}$):
> > $$\int \frac{x\arcsin(x)}{\sqrt{1-x^2}}\,dx = -\sqrt{1-x^2}\arcsin(x) + \int dx = -\sqrt{1-x^2}\arcsin(x) + x$$
> > **Respuesta:** $\arcsin^2(x)\,x + 2\sqrt{1-x^2}\arcsin(x) - 2x + C$.
> > **Cuidado:** el patrón de potencias de inversas es **por partes tantas veces como potencia** ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{\arctan(x)}{x^2}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Por partes:** $u = \arctan(x)$, $dv = x^{-2}\,dx$ → $du = \frac{1}{1+x^2}\,dx$, $v = -\frac{1}{x}$.
> > $$-\frac{\arctan(x)}{x} + \int \frac{1}{x(1+x^2)}\,dx$$
> > **Fracciones:** $\frac{1}{x(1+x^2)} = \frac{1}{x} - \frac{x}{1+x^2}$, luego la integral es $\ln\|x\| - \frac{1}{2}\ln(1+x^2)$.
> > **Respuesta:** $-\frac{\arctan(x)}{x} + \ln\|x\| - \frac{1}{2}\ln(1+x^2) + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \text{arcsec}(\sqrt{x})\,dx$ para $x > 1$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $t = \sqrt{x}$ → $x = t^2$, $dx = 2t\,dt$: $\int \text{arcsec}(\sqrt{x})\,dx = 2\int t\,\text{arcsec}(t)\,dt$.
> > **Por partes:** $u = \text{arcsec}(t)$, $dv = t\,dt$ → $v = \frac{t^2}{2}$:
> > $$2\left[\frac{t^2}{2}\text{arcsec}(t) - \frac{1}{2}\int \frac{t}{\sqrt{t^2-1}}\,dt\right] = t^2\text{arcsec}(t) - \sqrt{t^2-1} + C$$
> > **Respuesta:** $x\,\text{arcsec}(\sqrt{x}) - \sqrt{x-1} + C$.
> > **Control:** $\frac{d}{dx}\big[x\,\text{arcsec}(\sqrt{x})\big] = \text{arcsec}(\sqrt{x}) + \frac{1}{2\sqrt{x-1}}$ y la raíz aporta $-\frac{1}{2\sqrt{x-1}}$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \arctan(x)\ln(x)\,dx$ (nivel avanzado).
>
> > [!success]- ✅ Solución
> >
> > **Por partes** ($u = \ln(x)$, $dv = \arctan(x)\,dx$, $v = x\arctan(x) - \frac{1}{2}\ln(1+x^2)$):
> > $$x\ln(x)\arctan(x) - \frac{1}{2}\ln(x)\ln(1+x^2) - \int \arctan(x)\,dx + \frac{1}{2}\int \frac{\ln(1+x^2)}{x}\,dx$$
> > Las dos primeras integrales son de tabla; la última **no es elemental** y se expresa con el dilogaritmo: $\frac{1}{2}\int \frac{\ln(1+x^2)}{x}\,dx = -\frac{1}{4}\text{Li}_2(-x^2)$.
> > **Respuesta (referencia):** $x\ln(x)\arctan(x) - \frac{1}{2}\ln(x)\ln(1+x^2) - x\arctan(x) + \frac{1}{2}\ln(1+x^2) - \frac{1}{4}\text{Li}_2(-x^2) + C$.
> > **Lección:** el producto de dos funciones suaves puede esconder una integral sin primitiva elemental; reconocer el dilogaritmo ahorra horas de sustituciones inútiles ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{\arcsin(x)}{\sqrt{1-x^2}}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución directa:** $u = \arcsin(x)$ → $du = \frac{dx}{\sqrt{1-x^2}}$.
> > $$\int \frac{\arcsin(x)}{\sqrt{1-x^2}}\,dx = \int u\,du = \frac{u^2}{2} + C$$
> > **Respuesta:** $\frac{1}{2}\arcsin^2(x) + C$.
> > **Truco:** la derivada de $\arcsin$ ya está escondida en el denominador: aquí **no** hace falta por partes ✓

> [!example] 📋 Planteamiento
>
> Evalúa $\int_0^{\pi/2} x\,\arcsin(\sin(x))\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Dominio de la salida:** $\arcsin$ devuelve valores en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$; para $x \in [0, \pi/2]$ eso incluye al propio $x$, luego $\arcsin(\sin(x)) = x$ en todo el intervalo.
> > $$\int_0^{\pi/2} x \cdot x\,dx = \int_0^{\pi/2} x^2\,dx = \left[\frac{x^3}{3}\right]_0^{\pi/2} = \frac{\pi^3}{24}$$
> > **Respuesta:** $\frac{\pi^3}{24} \approx 1{,}2919$.
> > **Lección:** antes de integrar, simplifica la composición con el **rango** de la función inversa ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico la integración por partes con $u = f^{-1}(x)$ y $dv = dx$ para cualquier función inversa.
> - [ ] Derivo las seis funciones inversas trigonométricas, con su valor absoluto y dominio correctos.
> - [ ] Reproduzco de memoria las integrales de $\arcsin$, $\arccos$ y $\arctan$ verificándolas por derivación.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo productos $x \cdot f^{-1}(x)$ combinando por partes con la identidad $x^2 = 1 - (1-x^2)$ o integración racional.
> - [ ] Uso las identidades complementarias y de conversión para reescribir respuestas equivalentes.
> - [ ] Calculo integrales definidas notables sin caer en la trampa de la simetría mal aplicada.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo composiciones como $\int \arcsin(x/a)\,dx$ normalizando el argumento antes de usar la tabla.
> - [ ] Reconozco cuándo una integral (potencias o productos de inversas) no tiene primitiva elemental y paro a tiempo.
> - [ ] Combino por partes repetidas con sustituciones en potencias de inversas ($\arcsin^2$, $\arctan^3$) y verifico cada resultado derivando.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 7.1: integración por partes aplicada a funciones inversas.
> - G. Strang, *Calculus* (Wellesley-Cambridge): integración por partes e integrales de funciones inversas.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — la técnica fundamental de toda esta nota.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/02 - Identidades Trigonométricas para Integrales|02 - Identidades Trigonométricas para Integrales]] — las identidades con las que se simplifica cada residual.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — base de límites y funciones trigonométricas.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — el complemento natural: allí la inversa no aparece, pero sí sus primas.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — integrales con $\sqrt{a^2 \pm x^2}$ que conectan con estas sustituciones.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es el patrón para $\int f^{-1}(x)\,dx$?::Por partes con $u = f^{-1}(x)$, $dv = dx$ (entonces $v = x$): el resultado es $x f^{-1}(x) - \int x (f^{-1})'(x)\,dx$.
> - ¿Por qué siempre se toma la inversa como $u$?::Porque su derivada es elemental (está en la tabla) y convierte la integral residual en algo integrable; al revés no funciona.
> - ¿Cuánto vale $\int \arcsin(x)\,dx$ y $\int \arctan(x)\,dx$?::$x\arcsin(x) + \sqrt{1-x^2} + C$ y $x\arctan(x) - \frac{1}{2}\ln(1+x^2) + C$.
> - ¿Qué cuidado tienen arcsec y arccsc?::Su derivada lleva valor absoluto: $\frac{1}{\|x\|\sqrt{x^2-1}}$; en los ejercicios con $x > 1$ se quita sin más.
> - ¿Qué truco usa $\int x\arcsin(x)\,dx$?::$x^2 = 1 - (1-x^2)$, que parte la residual en dos integrales de tabla ($\arcsin$ y $\sqrt{1-x^2}$).
> - ¿$\int \arctan^2(x)\,dx$ se cierra?::No: tras dos por partes queda $\int \frac{\ln(1+x^2)}{1+x^2}\,dx$, que no tiene primitiva elemental (aparece el dilogaritmo); se trabaja como definida o numérica.
> - ¿Qué vale $\int_{-1}^1 x\arcsin(x)\,dx$?::$\frac{\pi}{4}$: el integrando es **par** (impar × impar), así que se duplica la integral de $0$ a $1$ en lugar de anularse.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — la técnica que hace posible toda esta nota, con su método de tabla.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/02 - Identidades Trigonométricas para Integrales|02 - Identidades Trigonométricas para Integrales]] — el repertorio de identidades para simplificar las residuales.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — funciones trigonométricas y límites, la base previa.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — complemento natural de técnicas.
> - [[2do Semestre/Cálculo Vectorial/Unidad 5 - Línea e Integrales Dobles/VI – Cambio de Variables en Integrales Dobles/03 – Teorema de cambio de variables|03 – Teorema de cambio de variables]] — para casos con composiciones en integrales dobles.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — sustitución trigonométrica y raíces $\sqrt{a^2 \pm x^2}$.
>
> **Aplicaciones:** cálculo de áreas (especialmente con funciones periódicas), física de oscilaciones y ondas, geometría analítica (longitudes de arco) y probabilidad (distribuciones especiales).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1, 2 y 3: las tres inversas básicas con su sustitución previa, el esqueleto de todo lo demás.
> - Después pasa al 4 y al 5, donde entran las por partes repetidas y la integración racional de la residual.
> - Cierra con el 6 al 9: el arcosecante con raíz, el producto con logaritmo (reconoce el callejón), la sustitución directa y la definida de trampa de simetría.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/V - Técnicas de Integración/05 - Integrales por Fracciones Parciales|Integrales por Fracciones Parciales]] para las residuales racionales largas; como siguiente horizonte, las **funciones especiales** (dilogaritmo) donde terminan estas integrales.

---

**Tags:** #MATG1045 #unidad6 #integrales-de-funciones-inversas #integrales #funciones-inversas #integracion-por-partes #arcsin #arccos #arctan #arcsec #identidades-trigonometricas

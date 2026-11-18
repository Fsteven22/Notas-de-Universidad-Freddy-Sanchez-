---
dg-publish: true
tags: [MATG1045, unidad6, integrales-trigonometricas, integrales, trigonometricas, identidades, sustitucion-weierstrass, tecnicas-integracion, formulas-reduccion, productos-trigonometricos]
---

# 📐 Integrales Trigonométricas

## 🎯 Introducción

> [!info] 💡 Qué son y por qué tienen su propia nota
>
> Las **integrales trigonométricas** son integrales cuyo integrando es una función racional en senos y cosenos con exponentes, productos o argumentos distintos: $\int \sin^m x \cos^n x\,dx$, $\int \tan^m x \sec^n x\,dx$, $\int \sin(3x)\cos(5x)\,dx$, etc. No se resuelven de golpe: se atacan con **identidades trigonométricas, sustituciones y fórmulas de reducción**, eligiendo la estrategia según los exponentes y el patrón del integrando.
>
> **Por qué importa:** esta nota es el taller de herramientas de la parte trigonométrica del cálculo integral. Lo que aprendas aquí se reutiliza en longitud de arco, áreas en coordenadas polares, series de Fourier y en cualquier integral donde aparezca una raíz con $\sin$ o $\cos$.
>
> **Ejemplo:** $\int \sin^3 x \cos^2 x\,dx$ se resuelve con la regla del exponente impar (seno impar → $u = \cos x$) y queda en una potencia pura de $u$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — los cuatro casos de $\sin^m\cos^n$ y los cuatro de $\tan^m\sec^n$, con su árbol de decisión.
> - **Identidades esenciales** — reducción de potencia, potencias superiores y producto ↔ suma.
> - **Casos resueltos y productos** — los nueve ejemplos clásicos, uno por cada patrón.
> - **Weierstrass** — la herramienta pesada $t = \tan(x/2)$ para lo que nada anterior resuelve.
> - **Tablas y reducción** — referencia rápida y recursión $I_n \to I_{n-2}$.
>
> **Por qué importa:** el orden no es aleatorio: primero se mira el patrón (¿potencia? ¿producto? ¿racional?), después se elige la herramienta. Saltarse ese orden es lo que hace que un ejercicio de tres líneas se convierta en una página.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Potencias de seno y coseno: $\int \sin^m(x) \cos^n(x)\,dx$
>
> **Caso 1:** si $m$ es impar → usar $u = \cos(x)$, $du = -\sin(x)\,dx$ (sobra una $\sin(x)$).
> **Caso 2:** si $n$ es impar → usar $u = \sin(x)$, $du = \cos(x)\,dx$ (sobra un $\cos(x)$).
> **Caso 3:** si ambos son pares → identidades de reducción de potencia: $\sin^2(x) = \frac{1-\cos(2x)}{2}$ y $\cos^2(x) = \frac{1+\cos(2x)}{2}$.
> **Caso 4:** si ambos son impares → elegir la sustitución más conveniente (cualquiera de las dos anteriores).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_Trigonométricas_01.svg]]
>
> **Se lee así:** una caja raíz con el patrón general $\int \sin^m(x)\cdot\cos^n(x)\,dx$ abre cuatro ramas en abanico, y cada rama es un rectángulo con la condición de los exponentes y el camino a seguir. No hay rombos ni bifurcaciones posteriores: las cuatro hojas cuelgan al mismo nivel y cubren desde el caso de un solo exponente impar hasta el de los dos impares, que se resuelve eligiendo.
>
> **Por qué importa:** el árbol es de una sola pregunta — mirar si los exponentes son pares o impares. Te ahorra probar sustituciones al aire, que es justo donde más tiempo se pierde en una integral trigonométrica.
>
> **Ejemplo:** con $\int \sin^3(x) \cos^2(x)\,dx$, el exponente impar del seno te manda a la rama 1 con $u = \cos(x)$, y de ahí sale $-\frac{\cos^3(x)}{3} + \frac{\cos^5(x)}{5} + C$.

> [!note] 📋 Definición — Potencias de tangente y secante: $\int \tan^m(x) \sec^n(x)\,dx$
>
> **Caso 1:** si $n$ es par → usar $u = \tan(x)$, $du = \sec^2(x)\,dx$ (se guarda un $\sec^2$ y el resto $\sec^{n-2}$ se escribe con $\tan^2 = \sec^2 - 1$).
> **Caso 2:** si $m$ y $n$ son impares → usar $u = \sec(x)$, $du = \sec(x)\tan(x)\,dx$ (sobra un $\tan(x)$).
> **Caso 3:** si $m$ es par y $n$ impar → reducir con $\tan^2(x) = \sec^2(x) - 1$ repetidamente.
> **Caso 4:** si $m$ es impar y $n$ par → combinar métodos o usar reducción.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_Trigonométricas_02.svg]]
>
> **Se lee así:** el esquema repite la forma de la raíz con cuatro ramas en abanico, pero ahora las condiciones se leen sobre los exponentes de tangente y secante. Dos ramas proponen una sustitución directa con su diferencial (las verdes), la tercera manda reescribir una potencia repetidamente y la última no fija sustitución, sino que indica combinar métodos o reducir (las naranjas).
>
> **Por qué importa:** la estructura es idéntica a la del seno y el coseno, así que aprendes **un solo criterio de lectura** para las dos familias. Esto te sirve para detectar en segundos el caso par-impar, que es el que más se confunde.
>
> **Ejemplo:** con $\int \tan^3(x) \sec^4(x)\,dx$, el exponente par de la secante te lleva a la rama 1 con $u = \tan(x)$, y la integral se vuelve $\int u^3(1+u^2)\,du$.

> [!tip] 🪞 Familia gemela: cotangente y cosecante
>
> Para $\int \cot^m(x) \csc^n(x)\,dx$ se aplica el **mismo árbol** que para tangente y secante, con estas identidades:
>
> - $\cot^2(x) = \csc^2(x) - 1$
> - $d(\cot(x)) = -\csc^2(x)\,dx$
> - $d(\csc(x)) = -\csc(x)\cot(x)\,dx$
>
> **Por qué importa:** no hace falta memorizar un segundo criterio: los signos negativos son la única diferencia, y los controlas derivando cada diferencial antes de sustituir.

---

## 🔺 Identidades esenciales

> [!info] 🧮 Identidades de reducción de potencia
>
> - $\sin^2(x) = \frac{1 - \cos(2x)}{2}$
> - $\cos^2(x) = \frac{1 + \cos(2x)}{2}$
> - $\tan^2(x) = \sec^2(x) - 1$
> - $\cot^2(x) = \csc^2(x) - 1$
> - $\sec^2(x) = 1 + \tan^2(x)$
> - $\csc^2(x) = 1 + \cot^2(x)$
>
> **Por qué importa:** son la vía del **caso ambos pares**: bajan la potencia de 2 en 2 hasta llegar a una potencia 1, que ya es inmediata. Las cuatro últimas son las que convierten tangentes en secantes (o al revés) para que aparezca la derivada que buscas.

> [!info] 🧮 Identidades de potencias superiores
>
> - $\sin^3(x) = \frac{3\sin(x) - \sin(3x)}{4}$
> - $\cos^3(x) = \frac{3\cos(x) + \cos(3x)}{4}$
> - $\sin^4(x) = \frac{3 - 4\cos(2x) + \cos(4x)}{8}$
> - $\cos^4(x) = \frac{3 + 4\cos(2x) + \cos(4x)}{8}$
>
> **Por qué importa:** cuando la integral es **solo** una potencia (sin el otro factor), bajar de golpe a armónicos lineales es más rápido que encadenar reducciones; $\sin^4$ y $\cos^4$ aparecen constantemente en exámenes.

> [!note] 🔄 Producto ↔ suma y suma ↔ producto
>
> **Producto a suma:**
>
> - $\sin(A)\cos(B) = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$
> - $\sin(A)\sin(B) = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$
> - $\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]$
>
> **Suma a producto:**
>
> - $\sin(A) + \sin(B) = 2\sin\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)$
> - $\cos(A) + \cos(B) = 2\cos\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)$
>
> **Por qué importa:** los **argumentos distintos** ($3x$ y $5x$) no admiten sustitución: la única salida es convertir el producto en una suma de senos o cosenos con argumento simple. Y ojo con $\sin(A-B)$: si $A < B$ sale negativo.

---

## 🧮 Casos resueltos: seno y coseno

> [!example] 🔢 Ejemplo 1 — exponente impar en el seno
>
> **Resolver:** $\int \sin^3(x) \cos^2(x)\,dx$
>
> - $m = 3$ (impar) → usar $u = \cos(x)$, $du = -\sin(x)\,dx$
> - $\sin^3(x) = \sin^2(x) \cdot \sin(x) = (1-\cos^2(x))\sin(x)$
> - $\int \sin^3(x) \cos^2(x)\,dx = \int (1-\cos^2(x))\cos^2(x)\sin(x)\,dx$
> - $= \int (1-u^2)u^2(-du) = -\int (u^2 - u^4)\,du = -\left(\frac{u^3}{3} - \frac{u^5}{5}\right) + C$
> - **Respuesta:** $-\frac{\cos^3(x)}{3} + \frac{\cos^5(x)}{5} + C$
>
> **Por qué importa:** el signo negativo del $du$ es lo que convierte $-\int(u^2-u^4)$ en $-\frac{u^3}{3} + \frac{u^5}{5}$; olvidarlo invierte los dos términos.

> [!example] 🔢 Ejemplo 2 — ambos exponentes pares
>
> **Resolver:** $\int \sin^2(x) \cos^2(x)\,dx$
>
> - Usar identidades: $\sin^2(x) = \frac{1-\cos(2x)}{2}$ y $\cos^2(x) = \frac{1+\cos(2x)}{2}$
> - $\sin^2(x)\cos^2(x) = \frac{1-\cos(2x)}{2} \cdot \frac{1+\cos(2x)}{2} = \frac{1-\cos^2(2x)}{4} = \frac{1}{4} - \frac{1+\cos(4x)}{8} = \frac{1}{8} - \frac{\cos(4x)}{8}$
> - $\int \sin^2(x) \cos^2(x)\,dx = \frac{x}{8} - \frac{\sin(4x)}{32} + C$
>
> **Por qué importa:** el truco de multiplicar primero $(1-\cos 2x)(1+\cos 2x)$ ahorra una reducción completa; el resultado solo contiene el armónico $4x$, como era de esperar de dos potencias cuadradas.

> [!example] 🔢 Ejemplo 8 — caso mixto: par × impar
>
> **Análisis:** $\int \sin^4(x) \cos^3(x)\,dx$ con $m = 4$ (par), $n = 3$ (impar) → usar $u = \sin(x)$.
>
> - $u = \sin(x)$, $du = \cos(x)\,dx$
> - $\cos^3(x) = \cos^2(x) \cdot \cos(x) = (1-\sin^2(x))\cos(x)$
> - $\int \sin^4(x)(1-\sin^2(x))\cos(x)\,dx = \int u^4(1-u^2)\,du = \int (u^4 - u^6)\,du$
> - **Respuesta:** $\frac{\sin^5(x)}{5} - \frac{\sin^7(x)}{7} + C$
>
> **Por qué importa:** cuando uno de los exponentes es impar, **siempre** queda un factor suelto para el $du$; aquí el $\cos(x)$ sobrante es el que viaja con la sustitución.

> [!example] 🔢 Ejemplo 9 — pura potencia par con reducción
>
> **Resolver:** $\int \cos^4(x)\,dx$
>
> - $\cos^4(x) = \left(\frac{1+\cos(2x)}{2}\right)^2 = \frac{1 + 2\cos(2x) + \cos^2(2x)}{4}$
> - $\cos^2(2x) = \frac{1+\cos(4x)}{2}$, luego $\cos^4(x) = \frac{3 + 4\cos(2x) + \cos(4x)}{8}$
> - $\int \cos^4(x)\,dx = \frac{3x}{8} + \frac{\sin(2x)}{4} + \frac{\sin(4x)}{32} + C$
>
> **Por qué importa:** dos aplicaciones de reducción seguidas; el coeficiente $\frac{4}{8} = \frac{1}{2}$ multiplica a $\int\cos(2x) = \frac{\sin(2x)}{2}$ y da $\frac{\sin(2x)}{4}$. Es el ejercicio donde más se fallan los factores.

---

## 📐 Casos resueltos: tangente y secante

> [!example] 🔢 Ejemplo 3 — secante con exponente par
>
> **Resolver:** $\int \tan^3(x) \sec^4(x)\,dx$
>
> - $n = 4$ (par) → usar $u = \tan(x)$, $du = \sec^2(x)\,dx$
> - $\sec^4(x) = \sec^2(x) \cdot \sec^2(x) = (1+\tan^2(x))\sec^2(x)$
> - $\int \tan^3(x)(1+\tan^2(x))\sec^2(x)\,dx = \int u^3(1+u^2)\,du = \int (u^3 + u^5)\,du$
> - **Respuesta:** $\frac{\tan^4(x)}{4} + \frac{\tan^6(x)}{6} + C$
>
> **Por qué importa:** con $n$ par **siempre** sobra un $\sec^2$ para el $du$; el resto de secantes se convierte en tangentes con $\sec^2 = 1 + \tan^2$.

> [!example] 🔢 Ejemplo 4 — tangente y secante ambas impares
>
> **Resolver:** $\int \tan^3(x) \sec(x)\,dx$
>
> - $m = 3$ (impar), $n = 1$ (impar) → usar $u = \sec(x)$, $du = \sec(x)\tan(x)\,dx$
> - $\tan^3(x) = \tan^2(x) \cdot \tan(x) = (\sec^2(x)-1)\tan(x)$
> - $\int (\sec^2(x)-1)\sec(x)\tan(x)\,dx = \int (u^2-1)\,du = \frac{u^3}{3} - u + C$
> - **Respuesta:** $\frac{\sec^3(x)}{3} - \sec(x) + C$
>
> **Por qué importa:** el par $\sec(x)\tan(x)$ es exactamente $du$; por eso, con ambas potencias impares, la mitad de la tangente se aparta como diferencial y la otra mitad se reescribe en secantes.

---

## 🎲 Productos de funciones trigonométricas

> [!example] 🔢 Ejemplo 5 — producto seno × coseno
>
> **Resolver:** $\int \sin(3x) \cos(5x)\,dx$
>
> - Usar $\sin(A)\cos(B) = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$
> - $\sin(3x)\cos(5x) = \frac{1}{2}[\sin(8x) + \sin(-2x)] = \frac{1}{2}[\sin(8x) - \sin(2x)]$
> - $\int \frac{1}{2}[\sin(8x) - \sin(2x)]\,dx = \frac{1}{2}\left[-\frac{\cos(8x)}{8} + \frac{\cos(2x)}{2}\right] + C$
> - **Respuesta:** $-\frac{\cos(8x)}{16} + \frac{\cos(2x)}{4} + C$
>
> **Por qué importa:** $\sin(-2x) = -\sin(2x)$ es el signo que decide el ejercicio; el resto es integrar dos senos con argumento lineal.

> [!example] 🔢 Ejemplo 6 — producto seno × seno
>
> **Resolver:** $\int \sin(2x) \sin(4x)\,dx$
>
> - Usar $\sin(A)\sin(B) = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$
> - $\sin(2x)\sin(4x) = \frac{1}{2}[\cos(-2x) - \cos(6x)] = \frac{1}{2}[\cos(2x) - \cos(6x)]$
> - $\int \frac{1}{2}[\cos(2x) - \cos(6x)]\,dx = \frac{1}{2}\left[\frac{\sin(2x)}{2} - \frac{\sin(6x)}{6}\right] + C$
> - **Respuesta:** $\frac{\sin(2x)}{4} - \frac{\sin(6x)}{12} + C$
>
> **Por qué importa:** aquí el orden $A - B$ importa: $\cos(-2x) = \cos(2x)$ lo salva, pero si los argumentos se intercambian mal el signo del primer término cambia.

---

## 🌐 Sustitución de Weierstrass

> [!note] 📋 Definición — Criterios de simetría y sustitución de Weierstrass
>
> Para $\int R(\sin(x), \cos(x))\,dx$ con $R$ racional, elegir la sustitución según cómo responda la función a cambios de signo:
>
> 1. Si $R(-\sin(x), \cos(x)) = -R(\sin(x), \cos(x))$ → usar $u = \cos(x)$.
> 2. Si $R(\sin(x), -\cos(x)) = -R(\sin(x), \cos(x))$ → usar $u = \sin(x)$.
> 3. Si $R(-\sin(x), -\cos(x)) = R(\sin(x), \cos(x))$ → usar $u = \tan(x)$.
> 4. En otros casos → sustitución de Weierstrass: $t = \tan\left(\frac{x}{2}\right)$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_Trigonométricas_03.svg]]
>
> **Se lee así:** el diagrama parte de una caja con el patrón general $\int R(\sin x, \cos x)\,dx$ y de ella salen cuatro ramas paralelas. Tres son criterios de simetría (verdes) que dependen de cómo cambia el signo al sustituir $-\sin$ o $-\cos$, y la cuarta es el caso general que no encaja en ninguno (naranja): la sustitución de Weierstrass $t = \tan(x/2)$, de la que cuelgan tres cajas con las identidades del seno, del coseno y del diferencial.
>
> **Por qué importa:** los tres criterios de simetría son **filtros rápidos**: si la función responde a un cambio de signo, ya tienes la sustitución sin más análisis. Solo cuando ninguno aplica tiene sentido recurrir a Weierstrass, que es la herramienta pesada.
>
> **Ejemplo:** para $\int \frac{1}{2 + \cos(x)}\,dx$ ningún criterio de simetría aplica, así que tomas $t = \tan(x/2)$ y la integral se vuelve racional en $t$.

> [!warning] 🚨 La sustitución de Weierstrass
>
> **Fórmula:** $t = \tan\left(\frac{x}{2}\right)$, con las transformaciones:
>
> - $\sin(x) = \frac{2t}{1+t^2}$
> - $\cos(x) = \frac{1-t^2}{1+t^2}$
> - $\tan(x) = \frac{2t}{1-t^2}$
> - $dx = \frac{2}{1+t^2}\,dt$
>
> **Cuándo usarla:** integrales racionales en funciones trigonométricas que no se resuelven por los criterios de simetría ni por las técnicas de potencias.
>
> **Por qué importa:** convierte **cualquier** racional en $\sin$ y $\cos$ en un racional en $t$, que siempre se resuelve (aunque sea con fracciones parciales). El precio es que la vuelta a $x$ es engorrosa: se recupera con un triángulo o con $t = \tan(x/2)$ directamente.

> [!example] 🔢 Ejemplo 7 — Weierstrass en acción
>
> **Resolver:** $\int \frac{1}{2 + \cos(x)}\,dx$
>
> - Sea $t = \tan\left(\frac{x}{2}\right)$, entonces $\cos(x) = \frac{1-t^2}{1+t^2}$ y $dx = \frac{2}{1+t^2}\,dt$
> - $\int \frac{1}{2 + \frac{1-t^2}{1+t^2}} \cdot \frac{2}{1+t^2}\,dt = \int \frac{2}{2(1+t^2) + 1-t^2}\,dt = \int \frac{2}{3 + t^2}\,dt$
> - $= \frac{2}{\sqrt{3}} \arctan\left(\frac{t}{\sqrt{3}}\right) + C$
> - **Respuesta:** $\frac{2}{\sqrt{3}} \arctan\left(\frac{\tan(x/2)}{\sqrt{3}}\right) + C$
>
> **Por qué importa:** fíjate en que el denominador $2(1+t^2) + (1-t^2) = 3 + t^2$ es **positivo**: la integral cae en el patrón $\int \frac{du}{a^2+u^2} = \frac{1}{a}\arctan\frac{u}{a}$, y el ejercicio se cierra en tres renglones.

---

## 📊 Tablas de referencia

> [!tip] 📋 Integrales fundamentales
>
> | Función | Integral |
> |---|---|
> | $\sin(x)$ | $-\cos(x) + C$ |
> | $\cos(x)$ | $\sin(x) + C$ |
> | $\tan(x)$ | $-\ln\|\cos(x)\| + C$ o $\ln\|\sec(x)\| + C$ |
> | $\cot(x)$ | $\ln\|\sin(x)\| + C$ |
> | $\sec(x)$ | $\ln\|\sec(x) + \tan(x)\| + C$ |
> | $\csc(x)$ | $-\ln\|\csc(x) + \cot(x)\| + C$ |
> | $\sec^2(x)$ | $\tan(x) + C$ |
> | $\csc^2(x)$ | $-\cot(x) + C$ |
> | $\sec(x)\tan(x)$ | $\sec(x) + C$ |
> | $\csc(x)\cot(x)$ | $-\csc(x) + C$ |
>
> **Por qué importa:** son las diez salidas hacia las que tienden todas las integrales de esta nota; si tu resultado no se parece a ninguna, revisa la sustitución antes de seguir.

> [!tip] 📋 Integrales de potencias comunes
>
> | Función | Integral |
> |---|---|
> | $\sin^2(x)$ | $\frac{x}{2} - \frac{\sin(2x)}{4} + C$ |
> | $\cos^2(x)$ | $\frac{x}{2} + \frac{\sin(2x)}{4} + C$ |
> | $\tan^2(x)$ | $\tan(x) - x + C$ |
> | $\sin^3(x)$ | $-\cos(x) + \frac{\cos^3(x)}{3} + C$ |
> | $\cos^3(x)$ | $\sin(x) - \frac{\sin^3(x)}{3} + C$ |
>
> **Por qué importa:** las cinco primeras filas salen en casi todos los ejercicios tipo; tenerlas de memoria te deja el tiempo del examen para el patrón difícil.

---

## 🔢 Fórmulas de reducción

> [!info] 🔄 Recursión $I_n \to I_{n-2}$
>
> **Potencias de seno:**
> $$I_n = \int \sin^n(x)\,dx = -\frac{1}{n}\sin^{n-1}(x)\cos(x) + \frac{n-1}{n}I_{n-2}$$
>
> **Potencias de coseno:**
> $$I_n = \int \cos^n(x)\,dx = \frac{1}{n}\cos^{n-1}(x)\sin(x) + \frac{n-1}{n}I_{n-2}$$
>
> **Potencias de tangente** (para $n \geq 2$):
> $$I_n = \int \tan^n(x)\,dx = \frac{\tan^{n-1}(x)}{n-1} - I_{n-2}$$
>
> **Potencias de secante** (para $n \geq 2$):
> $$I_n = \int \sec^n(x)\,dx = \frac{\sec^{n-2}(x)\tan(x)}{n-1} + \frac{n-2}{n-1}I_{n-2}$$
>
> **Por qué importa:** cada fórmula **baja la potencia de 2 en 2** hasta llegar a $I_0$ o $I_1$, que están en la tabla de fundamentales. Son el respaldo cuando el árbol de decisión no aplica (por ejemplo $\int \tan^5$ o $\int \sec^3$).

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los tres frentes de error
>
> **Errores de identificación:**
>
> - No reconocer el patrón correcto para elegir la sustitución.
> - Confundir cuándo usar cada método (exponente par vs. impar).
> - Aplicar mal las identidades trigonométricas.
>
> **Errores de cálculo:**
>
> - Olvidar el signo negativo en $du = -\sin(x)\,dx$ cuando $u = \cos(x)$.
> - No simplificar correctamente las expresiones con identidades.
> - Cometer errores en las identidades de producto a suma.
> - No verificar el dominio de las funciones involucradas.
>
> **Errores de verificación:**
>
> - No comprobar la respuesta derivando el resultado.
> - Olvidar la constante de integración.
> - No simplificar la respuesta final.
>
> **Por qué importa:** los de identificación se previenen con los árboles de decisión, los de cálculo con la lista de signos y los de verificación con una derivada final: son los tres controles antes de entregar.

> [!success] 💡 Estrategias de éxito
>
> **Antes de empezar:**
>
> - Identifica el tipo de integral y elige el método apropiado.
> - Revisa si hay simplificaciones obvias con identidades básicas.
> - Considera si un cambio de variable simple ($u$-substitution) podría funcionar.
>
> **Durante el proceso:**
>
> - Mantén un registro claro de las sustituciones realizadas.
> - Simplifica en cada paso para evitar expresiones complicadas.
> - Usa identidades trigonométricas para reducir la complejidad.
>
> **Verificación final:**
>
> - Deriva tu respuesta para verificar que obtienes el integrando original.
> - Revisa que el dominio de tu respuesta sea consistente.
> - Simplifica la expresión final tanto como sea posible.
>
> **Por qué importa:** la verificación final por derivación es la única que detecta signos invertidos y potencias mal bajadas; una integral mal resuelta derivada a tiempo se corrige en segundos.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Resuelve $\int \sin^2(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Identidad:** $\sin^2(x) = \frac{1-\cos(2x)}{2}$.
> > $$\int \sin^2(x)\,dx = \int \frac{1-\cos(2x)}{2}\,dx = \frac{x}{2} - \frac{\sin(2x)}{4} + C$$
> > **Respuesta:** $\frac{x}{2} - \frac{\sin(2x)}{4} + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \tan^2(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Identidad:** $\tan^2(x) = \sec^2(x) - 1$.
> > $$\int \tan^2(x)\,dx = \int (\sec^2(x) - 1)\,dx = \tan(x) - x + C$$
> > **Respuesta:** $\tan(x) - x + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \sec^2(x)\tan(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Sustitución:** $u = \tan(x)$, $du = \sec^2(x)\,dx$.
> > $$\int \sec^2(x)\tan(x)\,dx = \int u\,du = \frac{u^2}{2} + C$$
> > **Respuesta:** $\frac{\tan^2(x)}{2} + C$ (equivalente a $\frac{\sec^2(x)}{2} + C$) ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \sin^3(x) \cos^4(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Árbol:** $m = 3$ impar → $u = \cos(x)$, $du = -\sin(x)\,dx$; $\sin^3 = (1-\cos^2)\sin$.
> > $$\int (1-u^2)u^4(-du) = -\int (u^4 - u^6)\,du = -\frac{u^5}{5} + \frac{u^7}{7} + C$$
> > **Respuesta:** $-\frac{\cos^5(x)}{5} + \frac{\cos^7(x)}{7} + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \tan^4(x) \sec^2(x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Árbol:** $n = 2$ par → $u = \tan(x)$, $du = \sec^2(x)\,dx$ (el resto de secantes ya no hay: sobra exactamente uno).
> > $$\int \tan^4(x)\sec^2(x)\,dx = \int u^4\,du = \frac{u^5}{5} + C$$
> > **Respuesta:** $\frac{\tan^5(x)}{5} + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \sin(2x) \cos(3x)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Producto a suma:** $\sin(A)\cos(B) = \frac{1}{2}[\sin(A+B) + \sin(A-B)]$ con $A = 2x$, $B = 3x$:
> > $$\sin(2x)\cos(3x) = \frac{1}{2}[\sin(5x) + \sin(-x)] = \frac{1}{2}[\sin(5x) - \sin(x)]$$
> > $$\int = \frac{1}{2}\left[-\frac{\cos(5x)}{5} + \cos(x)\right] + C = -\frac{\cos(5x)}{10} + \frac{\cos(x)}{2} + C$$
> > **Respuesta:** $-\frac{\cos(5x)}{10} + \frac{\cos(x)}{2} + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{1}{1 + \sin(x)}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Conjugado:** multiplicar por $\frac{1-\sin(x)}{1-\sin(x)}$:
> > $$\int \frac{1-\sin(x)}{1-\sin^2(x)}\,dx = \int \frac{1-\sin(x)}{\cos^2(x)}\,dx = \int (\sec^2(x) - \sec(x)\tan(x))\,dx$$
> > **Respuesta:** $\tan(x) - \sec(x) + C$.
> > **Control:** $\frac{d}{dx}(\tan - \sec) = \sec^2 - \sec\tan = \frac{1-\sin}{\cos^2} = \frac{1}{1+\sin}$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \tan^5(x)\,dx$ con las fórmulas de reducción.
>
> > [!success]- ✅ Solución
> >
> > **Reducción de tangente:** $I_5 = \frac{\tan^4(x)}{4} - I_3$ y $I_3 = \frac{\tan^2(x)}{2} - I_1$, con $I_1 = \int \tan = \ln\|\sec(x)\|$.
> > $$I_5 = \frac{\tan^4(x)}{4} - \frac{\tan^2(x)}{2} + \ln\|\sec(x)\| + C$$
> > **Respuesta:** $\frac{\tan^4(x)}{4} - \frac{\tan^2(x)}{2} + \ln\|\sec(x)\| + C$.
> > **Truco:** el exponente impar de la tangente no admite el árbol directo: la recursión baja de 2 en 2 ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \sqrt{1 + \cos(x)}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Identidad:** $1 + \cos(x) = 2\cos^2\left(\frac{x}{2}\right)$, luego $\sqrt{1+\cos x} = \sqrt{2}\,\|\cos(x/2)\|$.
> > En un intervalo donde $\cos(x/2) \geq 0$:
> > $$\int \sqrt{2}\cos\left(\frac{x}{2}\right)\,dx = \sqrt{2} \cdot 2\sin\left(\frac{x}{2}\right) + C$$
> > **Respuesta:** $2\sqrt{2}\,\sin\left(\frac{x}{2}\right) + C$.
> > **Control:** $\frac{d}{dx}\,2\sqrt{2}\sin(x/2) = \sqrt{2}\cos(x/2) = \sqrt{2\cos^2(x/2)} = \sqrt{1+\cos x}$ ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Elijo la sustitución correcta para $\int \sin^m x \cos^n x\,dx$ y $\int \tan^m x \sec^n x\,dx$ según la paridad de los exponentes.
> - [ ] Aplico las identidades de reducción de potencia para bajar exponentes pares de 2 en 2.
> - [ ] Convierto productos con argumentos distintos en sumas con producto a suma e integro el resultado.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo integrales mixtas (par × impar) separando el factor que viaja con el $du$.
> - [ ] Uso las fórmulas de reducción $I_n \to I_{n-2}$ para potencias altas de seno, coseno, tangente o secante.
> - [ ] Aplico los criterios de simetría para elegir $u = \cos$, $u = \sin$ o $u = \tan$ en racionales de seno y coseno.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo con $t = \tan(x/2)$ una integral racional que ningún criterio anterior cubre y recupero la variable $x$.
> - [ ] Combino identidades, sustitución y por partes en una misma integral trigonométrica.
> - [ ] Verifico cada resultado derivando y comparando con el integrando original antes de darlo por bueno.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 7.2: integrales trigonométricas.
> - G. Strang, *Calculus* (Wellesley-Cambridge): integrales trigonométricas y sustituciones.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/02 - Identidades Trigonométricas para Integrales|02 - Identidades Trigonométricas para Integrales]] — el repertorio completo de identidades que esta nota aplica.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — la técnica base con la que se ejecutan todas las sustituciones de aquí.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — el complemento para productos donde las identidades no alcanzan.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — las integrales inmediatas hacia las que tienden estos resultados.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas|03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas]] — las derivadas que hacen posibles todos los $du$ de la nota.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cómo elijo la sustitución en $\int \sin^m x \cos^n x\,dx$?::Si $m$ es impar → $u = \cos x$; si $n$ es impar → $u = \sin x$; si ambos pares → reducción de potencia; si ambos impares → la que convenga.
> - ¿Y en $\int \tan^m x \sec^n x\,dx$?::Si $n$ es par → $u = \tan x$; si ambos impares → $u = \sec x$; si $m$ par y $n$ impar → reescribir $\tan^2 = \sec^2 - 1$; si $m$ impar y $n$ par → combinar o reducir.
> - ¿Qué hago cuando los exponentes son ambos pares?::Bajar la potencia con $\sin^2 = \frac{1-\cos 2x}{2}$ y $\cos^2 = \frac{1+\cos 2x}{2}$, repitiendo hasta llegar a potencia 1.
> - ¿Cuándo sirve producto a suma?::Cuando los argumentos son distintos ($\sin 3x \cos 5x$): se convierte en una suma de senos o cosenos con argumento lineal.
> - ¿Qué es la sustitución de Weierstrass?::$t = \tan(x/2)$, con $\sin x = \frac{2t}{1+t^2}$, $\cos x = \frac{1-t^2}{1+t^2}$ y $dx = \frac{2\,dt}{1+t^2}$: racionaliza cualquier $R(\sin x, \cos x)$.
> - ¿Qué criterio elige entre $\cos$, $\sin$ y $\tan$ antes de Weierstrass?::La simetría: $R(-\sin,\cos) = -R$ → $u = \cos$; $R(\sin,-\cos) = -R$ → $u = \sin$; $R(-\sin,-\cos) = R$ → $u = \tan$.
> - ¿Qué bajan las fórmulas de reducción?::Bajan la potencia de 2 en 2: $I_n$ se expresa con $I_{n-2}$ hasta llegar a $I_0$ o $I_1$, que están en la tabla.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/02 - Identidades Trigonométricas para Integrales|02 - Identidades Trigonométricas para Integrales]] — las identidades completas de las que esta nota toma sus herramientas.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — sustituciones trigonométricas para raíces ($\sqrt{a^2-x^2}$), la otra cara del mismo cambio de variable.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — para productos sin derivada limpia y para el caso cíclico $\int e^x \sin x\,dx$.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/04 - Integrales de Funciones Inversas|04 - Integrales de Funciones Inversas]] — donde $\arctan$ y $\arcsin$ aparecen como resultado y no como integrando.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — estas mismas integrales evaluadas con límites cuando el intervalo se escapa.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — integrales con $\sqrt{1 + (f')^2}$ que a veces caen en potencias trigonométricas.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] — el terreno donde $\sin$ y $\cos$ se integran con límites definidos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1, 2 y 3: reducción de potencia y la sustitución más simple, el esqueleto de todo lo demás.
> - Después pasa al 4 y al 5, donde entran la paridad mixta y el árbol de tangente/secante.
> - Cierra con el 6 al 9: producto a suma, el conjugado con seno, la reducción de $\tan^5$ y la raíz con media identidad.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/V - Técnicas de Integración/05 - Integrales por Fracciones Parciales|Integrales por Fracciones Parciales]] para cuando Weierstrass produzca un racional largo; como siguiente horizonte, las **series de Fourier**, donde estas integrales se calculan por centenas.

---

**Tags:** #MATG1045 #unidad6 #integrales-trigonometricas #integrales #trigonometricas #identidades #sustitucion-weierstrass #tecnicas-integracion #formulas-reduccion #productos-trigonometricos

---
dg-publish: true
tags: [MATG1045, unidad4, derivadas-trigonometricas-exponenciales-y-logaritmicas, calculo, derivadas, funciones-trigonometricas, regla-cadena, mnemotecnias, metodos-estudio, identidades-trigonometricas, exponenciales, logaritmos]
---

# 📐 Derivadas Trigonométricas, Exponenciales y Logarítmicas

## 🎯 Introducción

> [!info] 💡 Lo que une a estas tres familias
>
> Las derivadas de las funciones trigonométricas, exponenciales y logarítmicas son las que más se usan en física, ingeniería y matemáticas aplicadas, y las tres comparten la misma estructura: una fórmula fija por función, más la regla de la cadena cuando hay composición. Las trigonométricas tienen patrones que se memorizan con ciclos; las exponenciales y logarítmicas son inversas entre sí y sus derivadas reflejan esa relación.
>
> **Por qué importa:** una vez que internalizas estas fórmulas, cualquier función compuesta se resuelve en dos renglones. Y como modelan crecimiento, decaimiento y oscilaciones, aparecen en todos los problemas de aplicación de la derivada.
>
> **Ejemplo:** la posición de un movimiento armónico $x(t) = A\sin(\omega t + \phi)$ se deriva con el par seno-coseno más la cadena, y la velocidad sale $v(t) = A\omega\cos(\omega t + \phi)$.

> [!warning] ⚠️ Lo que debes dominar antes
>
> - La regla de la cadena, porque casi ningún ejercicio de esta nota es una función simple: [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]].
> - La tabla de derivadas básicas, con las reglas algebraicas que acompañan a las fórmulas: [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]].
> - La definición formal de derivada, de donde salen todas estas fórmulas: [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]].
>
> **Por qué importa:** aquí no se demuestra nada nuevo, se **aplica** lo anterior con disciplina. El error típico no es de concepto, sino de olvidar la cadena o el signo.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Derivadas de funciones trigonométricas
>
> Cada función trigonométrica tiene una derivada fija dentro de su dominio: $\frac{d}{dx}[\sin x] = \cos x$, $\frac{d}{dx}[\cos x] = -\sin x$, $\frac{d}{dx}[\tan x] = \sec^2 x$, $\frac{d}{dx}[\cot x] = -\csc^2 x$, $\frac{d}{dx}[\sec x] = \sec x\tan x$ y $\frac{d}{dx}[\csc x] = -\csc x\cot x$. Con composición, cada una se multiplica por la derivada interna $g'(x)$.
>
> | Función | Derivada | Mnemotecnia |
> |---------|----------|-------------|
> | $\sin(x)$ | $\cos(x)$ | "Seno se convierte en coseno" |
> | $\cos(x)$ | $-\sin(x)$ | "Coseno cambia signo y se vuelve seno" |
> | $\tan(x)$ | $\sec^2(x)$ | "Tangente al cuadrado secante" |
> | $\cot(x)$ | $-\csc^2(x)$ | "Cotangente negativa cosecante cuadrada" |
> | $\sec(x)$ | $\sec(x)\tan(x)$ | "Secante se multiplica por tangente" |
> | $\csc(x)$ | $-\csc(x)\cot(x)$ | "Cosecante negativa por cotangente" |
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivadas_Trigonométricas,_Exponenciales_y_Logarítmicas_01.svg]]
>
> **Se lee así:** Se ven tres pares de rectángulos unidos por flechas de doble sentido, de modo que cada par forma un ciclo cerrado de dos pasos. El primer ciclo empareja seno con coseno y hace que uno se convierta en el otro; el segundo empareja tangente con secante y el tercero cotangente con cosecante. Cada ciclo repite sus propias dos fórmulas sin mezclarse con los demás.
>
> **Por qué importa:** Los signos y los cuadrados son donde más se equivocan los estudiantes. Tener el ciclo a la vista te deja recorrer los dos pasos y comprobar que la derivada de tangente trae $\sec^2(x)$ y no $\tan^2(x)$.
>
> **Ejemplo:** Para derivar $\sin^3(x)$ reescribes $[\sin(x)]^3$, aplicas la regla de la potencia y usas el par seno-coseno para obtener $3\sin^2(x)\cos(x)$.

> [!note] 📋 Definición — Derivadas exponenciales y logarítmicas
>
> La exponencial natural es su propia derivada, $\frac{d}{dx}[e^x] = e^x$; cualquier otra base $a$ multiplica por su "ADN" logarítmico, $\frac{d}{dx}[a^x] = a^x\ln a$. El logaritmo natural deriva al recíproco, $\frac{d}{dx}[\ln x] = \frac{1}{x}$, y los demás logaritmos dividen por $\ln a$. Con composición, ambas familias se multiplican por la derivada interna $g'(x)$.
>
> | Función | Derivada | Dominio |
> |---------|----------|---------|
> | $e^x$ | $e^x$ | $\mathbb{R}$ |
> | $a^x$ | $a^x \ln(a)$ | $\mathbb{R}$, $a > 0$, $a \neq 1$ |
> | $\ln(x)$ | $\frac{1}{x}$ | $(0, +\infty)$ |
> | $\log_a(x)$ | $\frac{1}{x \ln(a)}$ | $(0, +\infty)$, $a > 0$, $a \neq 1$ |
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivadas_Trigonométricas,_Exponenciales_y_Logarítmicas_02.svg]]
>
> **Se lee así:** Es un flujo con **dos decisiones en rombo** encadenadas. La primera separa las funciones de base natural o logaritmo natural de las que usan otra base, que necesitan el factor $\ln(a)$; en ambos casos las ramas vuelven a juntarse. La segunda decisión pregunta si hay composición: si la hay, se aplica la regla de la cadena y si no, la fórmula directa, y ambos caminos terminan en la misma caja de resultado final.
>
> **Por qué importa:** Resuelve las dos confusiones más frecuentes: olvidar el $\ln(a)$ en bases distintas de $e$ y saltarse la regla de la cadena. La segunda decisión te hace preguntarte *¿es compuesto o directo?* antes de derivar.
>
> **Ejemplo:** Para derivar $\ln(x^2+5x)$, la primera decisión te manda a la fórmula del logaritmo natural y la segunda te hace aplicar la cadena, dando $\frac{2x+5}{x^2+5x}$.

---

## 🧠 Mnemotecnias: cómo memorizar las trigonométricas

> [!tip] 🎓 El círculo de derivadas
>
> Ordena las funciones en un círculo y gira en sentido horario: cada derivada es la siguiente función del ciclo.
>
> $$\sin(x) \rightarrow \cos(x) \rightarrow -\sin(x) \rightarrow -\cos(x) \rightarrow \sin(x)$$
>
> Cada paso del círculo es una derivada: de seno sale coseno, de coseno sale menos seno, y así vuelta completa.
>
> **Por qué importa:** es la única regla que te da las cuatro funciones pares de una sola mirada, con sus signos incluidos.
>
> **Ejemplo:** la derivada de $\cos(x)$ es el siguiente en el ciclo, $-\sin(x)$; la de $-\sin(x)$ es $-\cos(x)$.

> [!example] 🧠 Mnemotecnia "SOCOTA" (los signos)
>
> - **S**eno $\rightarrow$ **O**k (positivo).
> - **C**oseno $\rightarrow$ **O**puesta (negativo).
> - **T**angente $\rightarrow$ **A**lways positive ($\sec^2$ siempre positivo).
>
> **Para las recíprocas recuerda:** las funciones **co-** (coseno, cotangente, cosecante) introducen el signo negativo: $\cot(x) \rightarrow -\csc^2(x)$ y $\csc(x) \rightarrow -\csc(x)\cot(x)$.
>
> **Por qué importa:** el signo es el error número uno de estas fórmulas; SOCOTA lo decide de memoria antes de que escribas nada.

> [!note] 📝 Parejas bailando y familias
>
> - **Pareja 1:** $\sin$ y $\cos$ se turnan, uno se convierte en el otro.
> - **Pareja 2:** $\tan$ y $\sec$ bailan juntas: $\tan \rightarrow \sec^2$, $\sec \rightarrow \sec\tan$.
> - **Pareja 3:** $\cot$ y $\csc$ bailan juntas y siempre negativas: $\cot \rightarrow -\csc^2$, $\csc \rightarrow -\csc\cot$.
>
> **Técnica del espejo:** $\sin \leftrightarrow \cos$ se reflejan; $\tan$ "ve" su reflejo al cuadrado, $\sec^2$; $\sec$ se mira con tangente, $\sec\tan$.
>
> **Por qué importa:** en lugar de seis fórmulas sueltas memorizas tres parejas, y cada pareja se deriva mirando a la otra.
>
> **Ejemplo:** si te preguntan la derivada de $\cot(x)$, buscas la pareja csc: sale $-\csc^2(x)$, con el signo negativo de las co-funciones.

---

## 🧮 Ejemplos con regla de la cadena (trigonométricas)

> [!example] 🔢 Ejemplo 1: función simple con composición
>
> **Resolver** $\frac{d}{dx}[\sin(3x)]$.
>
> - Función externa: $\sin(u)$ con derivada $\cos(u)$.
> - Función interna: $u = 3x$ con derivada $3$.
> - Resultado: $\frac{d}{dx}[\sin(3x)] = \cos(3x) \cdot 3 = 3\cos(3x)$.

> [!example] 🔢 Ejemplo 2: composición más profunda
>
> **Resolver** $\frac{d}{dx}[\tan(x^2 + 1)]$.
>
> - Función externa: $\tan(u)$ con derivada $\sec^2(u)$.
> - Función interna: $u = x^2 + 1$ con derivada $2x$.
> - Resultado: $\frac{d}{dx}[\tan(x^2 + 1)] = \sec^2(x^2 + 1) \cdot 2x = 2x\sec^2(x^2 + 1)$.

> [!example] 🔢 Ejemplo 3: producto de funciones trigonométricas
>
> **Resolver** $\frac{d}{dx}[\sin(x)\cos(x)]$.
>
> - Regla del producto: $\sin'(x)\cos(x) + \sin(x)\cos'(x) = \cos(x)\cos(x) + \sin(x)(-\sin(x))$.
> - Simplificando: $\cos^2(x) - \sin^2(x) = \cos(2x)$, por la identidad del doble ángulo.
>
> **Por qué importa:** el resultado $\cos(2x)$ confirma la fórmula: a veces la derivada se reconoce con identidades.

> [!example] 🔢 Ejemplo 4: potencia de una trigonométrica
>
> **Resolver** $\frac{d}{dx}[\sin^3(x)]$.
>
> - Reescribir como $[\sin(x)]^3$; externa $u^3$ con derivada $3u^2$; interna $u = \sin(x)$ con derivada $\cos(x)$.
> - Resultado: $3[\sin(x)]^2 \cdot \cos(x) = 3\sin^2(x)\cos(x)$.
>
> **Por qué importa:** $\sin^3(x)$ **no** es $\sin(x^3)$; la reescritura antes de derivar evita confundir los dos enunciados.

---

## 🔍 Patrones, errores y errores comunes (trigonométricas)

> [!info] 🔍 Tres patrones que conviene ver
>
> 1. **Alternancia de signos:** las funciones co- (coseno, cotangente, cosecante) introducen signos negativos: $\cos(x) \rightarrow -\sin(x)$, $\cot(x) \rightarrow -\csc^2(x)$, $\csc(x) \rightarrow -\csc(x)\cot(x)$.
> 2. **Funciones al cuadrado:** las derivadas de $\tan$ y $\cot$ traen cuadrados: $\sec^2(x)$ y $-\csc^2(x)$.
> 3. **Productos en secante y cosecante:** $\sec(x) \rightarrow \sec(x)\tan(x)$ y $\csc(x) \rightarrow -\csc(x)\cot(x)$.
>
> **Por qué importa:** los tres patrones cubren las seis fórmulas. Si recuerdas dónde hay cuadrado, dónde hay producto y dónde hay signo, no necesitas memorizar de memoria ciega.

> [!warning] 🚨 Errores frecuentes y cómo evitarlos
>
> 1. **Olvidar el signo:** incorrecto $\frac{d}{dx}[\cos(x)] = \sin(x)$; correcto $\frac{d}{dx}[\cos(x)] = -\sin(x)$.
> 2. **Confundir el cuadrado:** incorrecto $\frac{d}{dx}[\tan(x)] = \tan^2(x)$; correcto $\frac{d}{dx}[\tan(x)] = \sec^2(x)$.
> 3. **No aplicar la cadena:** incorrecto $\frac{d}{dx}[\sin(3x)] = \cos(3x)$; correcto $\frac{d}{dx}[\sin(3x)] = 3\cos(3x)$.
>
> **Por qué importa:** los tres son de memoria o de prisa, no de concepto. La verificación es rápida: usa el círculo para el signo, mira si hay cuadrado y revisa si la función interna trae su factor.

> [!tip] 💡 Estrategias de verificación
>
> 1. **Método del círculo:** recorre el ciclo mental y comprueba signo y función.
> 2. **Verificación numérica:** prueba un valor específico, por ejemplo $x = 0$ en $\frac{d}{dx}[\cos x] = -\sin x$.
> 3. **Identidades:** usa $\sin^2 + \cos^2 = 1$ para reescribir el resultado.
> 4. **Simetría:** recuerda que el coseno es par y el seno impar.

---

## 📈 Funciones trigonométricas inversas

> [!note] 📋 Tabla de derivadas inversas
>
> | Función | Derivada | Dominio |
> |---------|----------|---------|
> | $\arcsin(x)$ | $\frac{1}{\sqrt{1 - x^2}}$ | $(-1, 1)$ |
> | $\arccos(x)$ | $\frac{-1}{\sqrt{1 - x^2}}$ | $(-1, 1)$ |
> | $\arctan(x)$ | $\frac{1}{1 + x^2}$ | $(-\infty, \infty)$ |
> | $\arccot(x)$ | $\frac{-1}{1 + x^2}$ | $(-\infty, \infty)$ |
> | $\operatorname{arcsec}(x)$ | $\frac{1}{\|x\| \sqrt{x^2 - 1}}$ | $(-\infty, -1) \cup (1, \infty)$ |
> | $\operatorname{arccsc}(x)$ | $\frac{-1}{\|x\| \sqrt{x^2 - 1}}$ | $(-\infty, -1) \cup (1, \infty)$ |
>
> **Por qué importa:** las inversas comparten el patrón de sus pares: las funciones co- traen signo negativo y el dominio es el de la trigonométrica acotada. En $\arctan$ no hay raíz, por eso su denominador es $1 + x^2$.
>
> **Ejemplo:** con $\frac{d}{dx}[\arcsin(x^2)]$ la cadena multiplica por $2x$ y queda $\frac{2x}{\sqrt{1-x^4}}$.

---

## 🌊 Aplicaciones: movimiento armónico y ondas

> [!example] 📊 Movimiento armónico simple
>
> **Posición:** $x(t) = A\sin(\omega t + \phi)$
>
> **Velocidad:** $v(t) = \frac{dx}{dt} = A\omega\cos(\omega t + \phi)$
>
> **Aceleración:** $a(t) = \frac{dv}{dt} = -A\omega^2\sin(\omega t + \phi)$
>
> **Por qué importa:** la aceleración sale proporcional y opuesta a la posición, $a = -\omega^2 x$, que es exactamente la ecuación de un oscilador armónico. Las dos derivadas seguidas son la regla de la cadena dos veces.

> [!example] 📊 Ondas y oscilaciones
>
> **Función de onda:** $y = A\sin(kx - \omega t)$
>
> **Derivada espacial:** $\frac{\partial y}{\partial x} = Ak\cos(kx - \omega t)$
>
> **Derivada temporal:** $\frac{\partial y}{\partial t} = -A\omega\cos(kx - \omega t)$
>
> **Por qué importa:** aquí se derivan respecto a una variable manteniendo fija la otra; el signo negativo de la derivada temporal viene del signo de $-\omega t$ dentro del seno.

---

## 📊 Derivadas exponenciales y logarítmicas

> [!info] 🎯 Las ocho fórmulas básicas
>
> **Exponenciales:**
>
> | Función | Derivada |
> |---------|----------|
> | $e^x$ | $e^x$ |
> | $a^x$ | $a^x \ln(a)$ |
> | $e^{g(x)}$ | $e^{g(x)} \cdot g'(x)$ |
> | $a^{g(x)}$ | $a^{g(x)} \ln(a) \cdot g'(x)$ |
>
> **Logarítmicas:**
>
> | Función | Derivada |
> |---------|----------|
> | $\ln(x)$ | $\frac{1}{x}$ |
> | $\log_a(x)$ | $\frac{1}{x \ln(a)}$ |
> | $\ln(g(x))$ | $\frac{g'(x)}{g(x)}$ |
> | $\log_a(g(x))$ | $\frac{g'(x)}{g(x) \ln(a)}$ |
>
> **Por qué importa:** fíjate en la simetría: la exponencial **multiplica** por $\ln(a)$ y el logaritmo **divide** por $\ln(a)$. Cuando la base es $e$, $\ln e = 1$ y ambas fórmulas se simplifican a las de arriba.

> [!example] 🔢 Ejemplo 1: la función que es su propia derivada
>
> **Resolver** $\frac{d}{dx}[e^x]$.
>
> $\frac{d}{dx}[e^x] = e^x$.
>
> **Característica especial:** $e^x$ es la única función igual a su derivada, lo que la hace el motor de todo modelo de crecimiento proporcional.

> [!example] 🔢 Ejemplo 2: exponencial con base distinta de $e$
>
> **Resolver** $\frac{d}{dx}[2^x]$.
>
> Aplicando la fórmula: $\frac{d}{dx}[2^x] = 2^x \ln(2)$.
>
> **Verificación:** $\ln(2) \approx 0.693 < 1$, así que esta derivada crece más despacio que la de $e^x$, como corresponde a una base menor.

> [!example] 🔢 Ejemplo 3: logaritmos
>
> **Resolver** $\frac{d}{dx}[\ln(x)]$ y $\frac{d}{dx}[\log_{10}(x)]$.
>
> $\frac{d}{dx}[\ln(x)] = \frac{1}{x}$ para $x > 0$; $\frac{d}{dx}[\log_{10}(x)] = \frac{1}{x \ln(10)}$, y como $\ln(10) \approx 2.303$, esta derivada es más pequeña que la del logaritmo natural.

> [!example] 🔢 Ejemplo 4: con regla de la cadena
>
> **Resolver** $\frac{d}{dx}[e^{3x^2 + 1}]$, $\frac{d}{dx}[\ln(x^2 + 5x)]$ y $\frac{d}{dx}[3^{x^2}]$.
>
> - Exponencial compuesta: externa $e^u$ con derivada $e^u$, interna $u = 3x^2+1$ con derivada $6x$; resultado $6x\,e^{3x^2 + 1}$.
> - Logaritmo compuesto: externa $\ln(u)$ con derivada $\frac{1}{u}$, interna $u = x^2+5x$ con derivada $2x+5$; resultado $\frac{2x+5}{x^2+5x}$.
> - Base variable: $3^{x^2} \ln(3) \cdot 2x = 2x\ln(3)\cdot 3^{x^2}$.
>
> **Por qué importa:** en los tres casos la estructura es la misma: fórmula de la familia por la derivada interna. Ese es exactamente el flujo de la figura de la Definición.

---

## ⚠️ Errores comunes y propiedades clave

> [!warning] 🚨 Los cuatro errores clásicos
>
> 1. **Olvidar el $\ln(a)$:** incorrecto $\frac{d}{dx}[2^x] = 2^x$; correcto $\frac{d}{dx}[2^x] = 2^x\ln(2)$.
> 2. **Ignorar el dominio:** $\frac{d}{dx}[\ln(x)] = \frac{1}{x}$ vale para $x > 0$, no para todo $x$.
> 3. **Saltarse la cadena:** incorrecto $\frac{d}{dx}[\ln(x^2)] = \frac{1}{x^2}$; correcto $\frac{d}{dx}[\ln(x^2)] = \frac{1}{x^2} \cdot 2x = \frac{2}{x}$.
> 4. **Confundir $x^n$ con $n^x$:** $\frac{d}{dx}[x^3] = 3x^2$ es potencia; $\frac{d}{dx}[3^x] = 3^x\ln(3)$ es exponencial.
>
> **Por qué importa:** el error 4 arruina ejercicios enteros de examen porque cambia la regla completa. Pregunta siempre: *¿la variable está en la base o en el exponente?*

> [!info] 🔍 Propiedades que explican las fórmulas
>
> **Relación inversa:** si $y = e^x$ entonces $x = \ln(y)$; sus derivadas son $e^x$ y $\frac{1}{x}$, y el producto de derivadas inversas es $e^x \cdot \frac{1}{e^x} = 1$.
>
> **Cambio de base:** $a^x = e^{x\ln(a)}$ y $\log_a(x) = \frac{\ln(x)}{\ln(a)}$, formas que permiten derivar cualquier base con las fórmulas naturales.
>
> **Identidades útiles:** $\frac{d}{dx}[\ln|x|] = \frac{1}{x}$ para $x \neq 0$, y $\frac{d}{dx}[x^n] = nx^{n-1}$ frente a $\frac{d}{dx}[n^x] = n^x\ln(n)$.
>
> **Por qué importa:** no son trucos sueltos: el cambio de base es la razón por la que existe el factor $\ln(a)$, y la relación inversa explica por qué exponencial y logaritmo se derivan tan distinto.

> [!tip] 💡 La técnica del "ADN logarítmico"
>
> Toda base $a \neq e$ necesita su ADN, que es $\ln(a)$:
>
> - **Exponencial:** $a^x \rightarrow a^x\ln(a)$, **multiplica** por su ADN.
> - **Logarítmica:** $\log_a(x) \rightarrow \frac{1}{x\ln(a)}$, **divide** por su ADN.
> - Base $e$: no necesita ADN, es la natural.
>
> **Por qué importa:** una sola imagen para las dos familias y sus signos implícitos. Si la base es $e$, olvídate del factor; si no lo es, el ADN aparece sí o sí.

---

## 🌱 Crecimiento, decaimiento y casos especiales

> [!example] 🧬 Crecimiento exponencial
>
> **Problema:** una población de bacterias crece según $P(t) = 1000e^{0.05t}$. ¿Cuál es la tasa de crecimiento instantánea?
>
> $P'(t) = 1000 \cdot e^{0.05t} \cdot 0.05 = 50e^{0.05t}$.
>
> **Interpretación:** la tasa de crecimiento es proporcional a la población actual, el rasgo definitorio del crecimiento exponencial.

> [!example] 💰 Interés compuesto continuo
>
> **Problema:** una inversión crece según $A(t) = 5000e^{0.06t}$. ¿Cuál es la tasa de crecimiento después de 10 años?
>
> $A'(t) = 5000 \cdot e^{0.06t} \cdot 0.06 = 300e^{0.06t}$; en $t = 10$: $A'(10) = 300e^{0.6} \approx 300(1.822) = 546.6$ dólares por año.
>
> **Por qué importa:** la derivada da la **velocidad** de crecimiento en ese instante, no el saldo; el saldo es $A(10)$ y la tasa es $A'(10)$.

> [!example] 🔢 Derivación implícita con exponenciales y logaritmos
>
> **Resolver:** si $xe^y + \ln(xy) = 5$, encontrar $\frac{dy}{dx}$.
>
> - $\frac{d}{dx}[xe^y] = e^y + xe^y\frac{dy}{dx}$ (producto con cadena).
> - $\frac{d}{dx}[\ln(xy)] = \frac{1}{xy}\left(y + x\frac{dy}{dx}\right) = \frac{1}{x} + \frac{1}{y}\frac{dy}{dx}$ (cadena y simplificación).
> - Ecuación resultante: $e^y + xe^y\frac{dy}{dx} + \frac{1}{x} + \frac{1}{y}\frac{dy}{dx} = 0$.
> - Agrupando: $\frac{dy}{dx}\left(xe^y + \frac{1}{y}\right) = -e^y - \frac{1}{x}$, y finalmente
>
> $$\frac{dy}{dx} = \frac{-e^y - \frac{1}{x}}{xe^y + \frac{1}{y}} = \frac{-y(xe^y + 1)}{x(xye^y + 1)}.$$
>
> **Por qué importa:** es la unión de esta nota con [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]]: la cadena del exponencial y la del logaritmo trabajando dentro de una ecuación.

> [!example] 🔢 Derivación logarítmica y funciones especiales
>
> **Potencia variable:** para $\frac{d}{dx}[x^x]$ se toma $\ln y = x\ln x$, se deriva $\frac{1}{y}\frac{dy}{dx} = \ln x + 1$ y queda $\frac{dy}{dx} = x^x(\ln x + 1)$. El desarrollo completo está en [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]].
>
> **Logaritmo de valor absoluto:** para funciones que pueden ser negativas, $\frac{d}{dx}[\ln|g(x)|] = \frac{g'(x)}{g(x)}$; en particular $\frac{d}{dx}[\ln|x|] = \frac{1}{x}$ para $x \neq 0$.
>
> **Funciones hiperbólicas:** definidas con exponenciales, $\sinh(x) = \frac{e^x - e^{-x}}{2}$ y $\cosh(x) = \frac{e^x + e^{-x}}{2}$, cuyas derivadas se intercambian: $\frac{d}{dx}[\sinh(x)] = \cosh(x)$ y $\frac{d}{dx}[\cosh(x)] = \sinh(x)$, como un gemelo seno-coseno sin signos negativos.

---

## 📋 Tabla de referencia completa

> [!note] 🚀 Guía de consulta rápida con regla de la cadena
>
> **Trigonométricas compuestas:**
>
> | Función compuesta | Derivada |
> |-------------------|----------|
> | $\sin(g(x))$ | $\cos(g(x)) \cdot g'(x)$ |
> | $\cos(g(x))$ | $-\sin(g(x)) \cdot g'(x)$ |
> | $\tan(g(x))$ | $\sec^2(g(x)) \cdot g'(x)$ |
> | $\cot(g(x))$ | $-\csc^2(g(x)) \cdot g'(x)$ |
> | $\sec(g(x))$ | $\sec(g(x))\tan(g(x)) \cdot g'(x)$ |
> | $\csc(g(x))$ | $-\csc(g(x))\cot(g(x)) \cdot g'(x)$ |
>
> **Exponenciales y logarítmicas compuestas:**
>
> | Función compuesta | Derivada |
> |-------------------|----------|
> | $e^{g(x)}$ | $e^{g(x)} \cdot g'(x)$ |
> | $a^{g(x)}$ | $a^{g(x)} \ln(a) \cdot g'(x)$ |
> | $\ln(g(x))$ | $\frac{g'(x)}{g(x)}$ |
> | $\log_a(g(x))$ | $\frac{g'(x)}{g(x) \ln(a)}$ |
>
> **Casos especiales:** $\frac{d}{dx}[x^x] = x^x(\ln x + 1)$, $\frac{d}{dx}[\ln|x|] = \frac{1}{x}$ y $[g(x)]^{h(x)}$ se deriva con la técnica logarítmica.
>
> **Por qué importa:** doce filas que cubren el 90% de los ejercicios de función compuesta. Leer la tabla como "fórmula de la familia por $g'(x)$" la vuelve deducible en vez de memorística.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Cadena trigonométrica básica

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[\sin(3x)]$ y $\frac{d}{dx}[\tan(x^2+1)]$.
>
> > [!success]- ✅ Solución
> >
> > En $\sin(3x)$: externa $\sin(u)$ con derivada $\cos(u)$, interna $u = 3x$ con derivada $3$; entonces $\frac{d}{dx}[\sin(3x)] = 3\cos(3x)$.
> >
> > En $\tan(x^2+1)$: externa $\tan(u)$ con derivada $\sec^2(u)$, interna $u = x^2+1$ con derivada $2x$; entonces $\frac{d}{dx}[\tan(x^2+1)] = 2x\sec^2(x^2+1)$.

### ✏️ Ejercicio 2 — Potencia de una trigonométrica

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[\sin^3(x)]$.
>
> > [!success]- ✅ Solución
> >
> > Reescribir como $[\sin(x)]^3$: la externa $u^3$ deriva a $3u^2$ y la interna $u = \sin(x)$ deriva a $\cos(x)$.
> >
> > Aplicando la cadena: $3[\sin(x)]^2 \cdot \cos(x) = 3\sin^2(x)\cos(x)$.
> >
> > Verificación: es el patrón "potencia por derivada de la base", igual que en $[\sin(x)]^3$.

### ✏️ Ejercicio 3 — Exponencial y logaritmo compuestos

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[e^{3x^2+1}]$ y $\frac{d}{dx}[\ln(x^2+5x)]$.
>
> > [!success]- ✅ Solución
> >
> > Exponencial: externa $e^u$ con derivada $e^u$, interna $u = 3x^2+1$ con derivada $6x$; resultado $\frac{d}{dx}[e^{3x^2+1}] = 6x\,e^{3x^2+1}$.
> >
> > Logaritmo: externa $\ln(u)$ con derivada $\frac{1}{u}$, interna $u = x^2+5x$ con derivada $2x+5$; resultado $\frac{d}{dx}[\ln(x^2+5x)] = \frac{2x+5}{x^2+5x}$.

### ✏️ Ejercicio 4 — Bases distintas de $e$

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[2^x]$ y $\frac{d}{dx}[\log_{10}(x)]$, y explica la aparición de $\ln(a)$ en ambas.
>
> > [!success]- ✅ Solución
> >
> > $\frac{d}{dx}[2^x] = 2^x\ln(2)$ y $\frac{d}{dx}[\log_{10}(x)] = \frac{1}{x\ln(10)}$.
> >
> > El $\ln(a)$ aparece por el cambio de base: $a^x = e^{x\ln a}$ se deriva con la exponencial natural, y $\log_a x = \frac{\ln x}{\ln a}$ deja el $\ln a$ como constante en el denominador.
> >
> > Como la exponencial **multiplica** y el logaritmo **divide**, las dos fórmulas son simétricas.

### ✏️ Ejercicio 5 — Derivadas inversas

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[\arcsin(x^2)]$ y $\frac{d}{dx}[\arctan(\sqrt{x})]$.
>
> > [!success]- ✅ Solución
> >
> > $\arcsin(x^2)$: la derivada de $\arcsin$ es $\frac{1}{\sqrt{1-u^2}}$ con $u = x^2$ y $u' = 2x$; queda $\frac{2x}{\sqrt{1-x^4}}$.
> >
> > $\arctan(\sqrt{x})$: la derivada de $\arctan$ es $\frac{1}{1+u^2}$ con $u = \sqrt{x}$ y $u' = \frac{1}{2\sqrt{x}}$; queda $\frac{1}{2\sqrt{x}(1+x)}$.
> >
> > En ambos casos: fórmula de la inversa evaluada en la interna, por la derivada de la interna.

### ✏️ Ejercicio 6 — Crecimiento exponencial

> [!example] 📋 Planteamiento
>
> Una inversión crece según $A(t) = 5000e^{0.06t}$. Encuentra la tasa de crecimiento en $t = 10$ años e interprétala.
>
> > [!success]- ✅ Solución
> >
> > Derivando: $A'(t) = 5000 \cdot e^{0.06t} \cdot 0.06 = 300e^{0.06t}$ (cadena con la constante del exponente).
> >
> > Evaluando: $A'(10) = 300e^{0.6} \approx 300(1.822) = 546.6$ dólares por año.
> >
> > Interpretación: al décimo año el saldo crece a razón de unos 546.6 dólares anuales; el saldo mismo es $A(10) \approx 9110$ dólares, que es otra cosa.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Derivo las seis funciones trigonométricas con su signo correcto.
> - [ ] Derivo $e^x$, $a^x$, $\ln x$ y $\log_a x$ explicando cuándo aparece $\ln(a)$.
> - [ ] Aplico la regla de la cadena a composiciones de estas familias.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Distingo $\sin^3(x)$ de $\sin(x^3)$ y derivo cada una correctamente.
> - [ ] Derivo funciones inversas como $\arcsin(x^2)$ y $\arctan(\sqrt{x})$.
> - [ ] Resuelvo un problema de crecimiento exponencial interpretando la derivada como tasa.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Combino derivación implícita con exponenciales y logaritmos en una misma ecuación.
> - [ ] Reconozco cuándo un caso $f(x)^{g(x)}$ exige derivación logarítmica.
> - [ ] Derivo funciones hiperbólicas y verifico su relación con las exponenciales.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 3: derivadas de exponenciales, logaritmos y trigonométricas.
> - R. Larson, *Cálculo* (Cengage), cap. 3: funciones trigonométricas inversas y aplicaciones.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la herramienta que acompaña a todas las fórmulas de esta nota.
> - [[Unidad 6 - Integrales/Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — el proceso inverso de estas derivadas.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la derivada de $\cos(x)$?::$-\sin(x)$; el coseno cambia de signo y se vuelve seno, como dice el círculo de derivadas.
> - ¿Cuál es la derivada de $\tan(x)$?::$\sec^2(x)$, sin signo negativo; es el cuadrado de la secante, no $\tan^2(x)$.
> - ¿Qué derivada tiene $a^x$ con $a \neq e$?::$a^x\ln(a)$: multiplica por su "ADN" logarítmico, que es $\ln(a)$.
> - ¿Por qué $\ln(x^2)$ deriva a $\frac{2}{x}$ y no a $\frac{1}{x^2}$?::Por la regla de la cadena: $\frac{1}{x^2}$ por la derivada interna $2x$, que simplifica a $\frac{2}{x}$.
> - ¿Qué función es igual a su propia derivada?::$e^x$; es la única, y por eso modela crecimiento proporcional.
> - ¿Cómo se deriva $\arcsin(x^2)$?::$\frac{2x}{\sqrt{1-x^4}}$: la fórmula de $\arcsin$ evaluada en $x^2$ por la derivada $2x$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — sin ella casi ningún ejercicio de esta nota se resuelve.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] — el resumen donde conviven estas fórmulas con las algebraicas.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — para ecuaciones donde estas funciones aparecen sin despejar.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]] — la técnica para potencias $f(x)^{g(x)}$ que aquí solo se enuncia.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — pendientes de curvas trigonométricas y exponenciales.
> - [[Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — hacia Cálculo Integral: estas fórmulas se usan al revés al integrar.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Empieza por el círculo de derivadas y SOCOTA: dominar los signos de las seis trigonométricas es la base de todo lo demás.
> - Después practica cadenas cortas como $\sin(3x)$ y $e^{3x^2+1}$ hasta que la estructura "fórmula por derivada interna" sea automática.
> - Cuando toques optimización o modelado, vuelve a los ejemplos de crecimiento y movimiento armónico de esta nota.
> - Para el caso $f(x)^{g(x)}$, continúa en [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]]; hacia el integral, en [[Unidad 6 - Integrales/Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]].

---

**Tags:** #MATG1045 #unidad4 #derivadas-trigonometricas-exponenciales-y-logaritmicas #calculo #derivadas #funciones-trigonometricas #regla-cadena #mnemotecnias #identidades-trigonometricas #exponenciales #logaritmos

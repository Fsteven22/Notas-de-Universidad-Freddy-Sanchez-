---
dg-publish: true
tags: [MATG1045, unidad4, reglas-fundamentales-de-derivacion, potencia, regla-producto, regla-cociente, funciones-elementales, mnemotecnia]
---

# ⚙️ Reglas Fundamentales de Derivación

## 🎯 Introducción

> [!info] 💡 Derivar sin volver al límite
>
> Las **reglas fundamentales de derivación** son el conjunto de fórmulas que permite calcular derivadas de forma sistemática, sin rehacer el cociente incremental en cada paso. La definición $f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$ es el origen de todo, pero usarla en cada ejercicio costaría diez minutos por función; estas reglas convierten ese límite en un cálculo de segundos.
>
> **Lo que cubre esta nota:** constantes, múltiplo constante, potencia, suma, diferencia, producto y cociente, más el catálogo de derivadas de las funciones elementales.
>
> **Por qué importa:** el 99% de los ejercicios del curso se resuelven con estas fórmulas. La definición queda para demostrarlas y para los casos raros; aquí aprendes a reconocer cuál toca en cada expresión.
>
> **Ejemplo:** en $f(x) = 3x^4 - 2x^3 + 5x^2 - 7x + 9$ no se toca ningún límite: se deriva término a término y queda $12x^3 - 6x^2 + 10x - 7$.

> [!warning] ⚠️ Lo que ya debías dominar antes de entrar
>
> - La definición de derivada y por qué el $h$ se cancela: [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]].
> - El límite del que nace todo: [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]].
> - Las funciones elementales (potencias, trigonométricas, exponenciales, logarítmicas) y sus dominios.
>
> **Por qué importa:** si la regla de la potencia o la del producto te suenan nuevas, todo el tema se te va a caer encima. Repasa esas dos notas antes de seguir.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Reglas básicas de derivación
>
> Son tres las reglas con las que arranca cualquier cálculo de derivadas:
>
> $$\frac{d}{dx}[c] = 0, \qquad \frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x), \qquad \frac{d}{dx}[x^n] = n x^{n-1}.$$
>
> La primera dice que una constante no cambia, por lo tanto su tasa de cambio es cero; la segunda permite sacar el factor constante antes de derivar; la tercera es la **regla de la potencia**, válida para cualquier número real $n$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Reglas_Fundamentales_de_Derivación_04.svg]]
>
> **Se lee así:** el diagrama arranca en una caja con las tres reglas y se abre en tres ramas paralelas: constante, múltiplo constante y potencia. Cada rama baja a un par de ejemplos concretos y las tres se juntan en una caja final que dice que se aplican término a término en cualquier polinomio.
>
> **Por qué importa:** son las únicas tres que no dependen de ninguna otra regla. Todas las demás se construyen sobre ellas, y aplicarlas por partes es lo que permite derivar un polinomio completo de un solo golpe.
>
> **Ejemplo:** $\frac{d}{dx}[3x^2] = 3 \cdot 2x = 6x$ combina múltiplo constante con potencia, y $\frac{d}{dx}[5] = 0$ es la primera regla en estado puro.

> [!note] 📋 Definición — Reglas de combinación (suma, diferencia, producto y cociente)
>
> Para combinar funciones ya derivadas:
>
> $$(f \pm g)' = f' \pm g', \qquad (fg)' = f'g + fg', \qquad \left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}.$$
>
> La suma y la diferencia derivan término a término; el producto y el cociente **no**: ahí participan las derivadas de las dos funciones, y en el cociente el denominador va al cuadrado. Estas siete fórmulas (las tres básicas más estas) sustituyen a la definición en casi todos los ejercicios.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Reglas_Fundamentales_de_Derivación_01.svg]]
>
> **Se lee así:** es un árbol de decisión. La caja de entrada, "función a derivar", llega a un rombo que pregunta por el tipo de función y sale en cuatro ramas paralelas: simple, suma o diferencia, producto y cociente. Cada rama indica la acción correspondiente (fórmula directa de la tabla, derivar término a término, regla del producto, regla del cociente) y las cuatro terminan en la misma caja de resultado final.
>
> **Por qué importa:** fija el orden de trabajo: **detectar el tipo antes de escribir fórmulas**, y no al revés. El error más caro del curso es aplicar la regla del producto a una suma simple, y este árbol te obliga a preguntarlo antes de empezar.
>
> **Ejemplo:** en $k(x) = \frac{x^2 e^x}{\ln x}$ entras por la rama del cociente y, dentro del numerador, vuelves a la rama del producto para derivar $x^2 e^x$.

---

## 🧮 Reglas en detalle y sus trucos

> [!tip] ➕ Reglas de suma, diferencia y múltiplo constante
>
> $$\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x), \qquad \frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x).$$
>
> **Generalización:** la derivada de una suma finita es la suma de las derivadas:
>
> $$\frac{d}{dx}[f_1(x) + f_2(x) + \cdots + f_n(x)] = f_1'(x) + f_2'(x) + \cdots + f_n'(x).$$
>
> **Por qué importa:** son lineales, es decir, reparten la derivada entre los términos. Por eso un polinomio se deriva de un barrido, de izquierda a derecha, sin más cuenta que multiplicar el exponente.
>
> **Ejemplo:** $\frac{d}{dx}[x^3 + 2x^2 - 5x + 7] = 3x^2 + 4x - 5$; el $7$ desaparece porque su derivada es cero.

> [!tip] ✖️ Regla del producto
>
> $$\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x).$$
>
> **Mnemotecnia:** "*PRIMERO por segundo + primero por SEGUNDO*", es decir, se deriva cada factor por separado y se va sumando.
>
> **Por qué importa:** el producto **no** se deriva multiplicando las derivadas ($(fg)' \neq f'g'$). Cada factor aparece dos veces, una vez derivado y otra vez intacto.
>
> **Ejemplo:** $\frac{d}{dx}[x^2 \cdot \sin x] = 2x \cdot \sin x + x^2 \cdot \cos x$.

> [!tip] ➗ Regla del cociente
>
> $$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}.$$
>
> **Mnemotecnia:** "*ABAJO por arriba MENOS arriba por ABAJO, todo sobre abajo al cuadrado*".
>
> **Por qué importa:** el orden del numerador importa: si cambias los términos de lugar, el signo se va. Y el denominador va **al cuadrado**, no sin exponente.
>
> **Ejemplo:** $\frac{d}{dx}\left[\frac{x^2}{x+1}\right] = \frac{2x(x+1) - x^2 \cdot 1}{(x+1)^2} = \frac{x^2+2x}{(x+1)^2}$.

> [!info] 🧩 Casos especiales y atajos
>
> - **Producto de tres funciones:** $(fgh)' = f'gh + fg'h + fgh'$, o aplica la regla del producto dos veces con $[(fg)h]'$.
> - **Cocientes que se simplifican:** a veces conviene simplificar antes de derivar: $\frac{x^3}{x} = x^2$ y luego $(x^2)' = 2x$.
> - **Potencias con exponente negativo:** $\frac{d}{dx}[x^{-2}] = -2x^{-3} = -\frac{2}{x^3}$: el signo se conserva y el exponente baja igual.
> - **Racicones como potencias:** $\frac{d}{dx}[\sqrt{x}] = \frac{d}{dx}[x^{1/2}] = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$.
>
> **Por qué importa:** simplificar antes de derivar reduce el tamaño de la expresión y con eso baja la probabilidad de error algebraico.
>
> **Ejemplo:** $\left(\frac{1}{x}\right)' = (x^{-1})' = -x^{-2} = -\frac{1}{x^2}$, la potencia con exponente negativo aplicada a la función recíproca.

---

## 📈 Derivadas de funciones elementales

> [!tip] 📊 Algebraicas
>
> | Función $f(x)$ | Derivada $f'(x)$ | Nota |
> |---|---|---|
> | $c$ | $0$ | constante |
> | $x$ | $1$ | identidad |
> | $x^n$ | $n x^{n-1}$ | regla de la potencia |
> | $\sqrt{x}$ | $\frac{1}{2\sqrt{x}}$ | raíz como potencia |
> | $\frac{1}{x}$ | $-\frac{1}{x^2}$ | definida para $x \neq 0$ |

> [!tip] 📊 Exponenciales y logarítmicas
>
> | Función $f(x)$ | Derivada $f'(x)$ | Nota |
> |---|---|---|
> | $e^x$ | $e^x$ | la única igual a su derivada |
> | $a^x$ | $a^x \ln a$ | $a > 0$, $a \neq 1$ |
> | $\ln x$ | $\frac{1}{x}$ | $x > 0$ |
> | $\log_a x$ | $\frac{1}{x \ln a}$ | $a > 0$, $a \neq 1$ |

> [!tip] 📊 Trigonométricas
>
> | Función $f(x)$ | Derivada $f'(x)$ | Nota |
> |---|---|---|
> | $\sin x$ | $\cos x$ | básica |
> | $\cos x$ | $-\sin x$ | **signo negativo** |
> | $\tan x$ | $\sec^2 x$ | equivale a $1/\cos^2 x$ |
> | $\cot x$ | $-\csc^2 x$ | **signo negativo** |
> | $\sec x$ | $\sec x \tan x$ | producto de secante y tangente |
> | $\csc x$ | $-\csc x \cot x$ | **signo negativo** |

> [!tip] 📊 Trigonométricas inversas
>
> | Función $f(x)$ | Derivada $f'(x)$ | Condición |
> |---|---|---|
> | $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ | $\|x\| < 1$ |
> | $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ | $\|x\| < 1$ |
> | $\arctan x$ | $\frac{1}{1+x^2}$ | $x \in \mathbb{R}$ |
> | $\text{arccot } x$ | $-\frac{1}{1+x^2}$ | $x \in \mathbb{R}$ |
> | $\text{arcsec } x$ | $\frac{1}{\|x\|\sqrt{x^2-1}}$ | $\|x\| > 1$ |
> | $\text{arccsc } x$ | $-\frac{1}{\|x\|\sqrt{x^2-1}}$ | $\|x\| > 1$ |

> [!tip] 📊 Hiperbólicas
>
> | Función $f(x)$ | Derivada $f'(x)$ | Nota |
> |---|---|---|
> | $\sinh x$ | $\cosh x$ | |
> | $\cosh x$ | $\sinh x$ | sin signo negativo |
> | $\tanh x$ | $\text{sech}^2 x$ | |
> | $\text{coth } x$ | $-\text{csch}^2 x$ | signo negativo |
> | $\text{sech } x$ | $-\text{sech } x \tanh x$ | signo negativo |
> | $\text{csch } x$ | $-\text{csch } x \coth x$ | signo negativo |
>
> **Por qué importa:** esta tabla es la hoja de consulta rápida del curso. Para la versión resumida y lista para imprimir, consulta [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]].
>
> **Ejemplo:** $\frac{d}{dx}[\log_5 x] = \frac{1}{x \ln 5}$: se toma la rama de logarítmicas y se aplica sin volver a la definición.

---

## 💡 Ejemplos desarrollados

> [!example] 🎯 Ejemplo 1: polinomio completo
>
> **Derivar** $f(x) = 3x^4 - 2x^3 + 5x^2 - 7x + 9$.
>
> Se aplica suma, diferencia y múltiplo constante, derivando término a término:
>
> $$f'(x) = 3(4x^3) - 2(3x^2) + 5(2x) - 7(1) + 0 = 12x^3 - 6x^2 + 10x - 7.$$
>
> **Por qué importa:** el $9$ desaparece y el $7$ se queda sin factor: cada término se toma por separado.

> [!example] 🎯 Ejemplo 2: regla del producto
>
> **Derivar** $g(x) = x^3 \sin x$.
>
> - Factores: $f(x) = x^3$ con $f'(x) = 3x^2$; $g(x) = \sin x$ con $g'(x) = \cos x$.
> - Aplicando $(fg)' = f'g + fg'$:
>
> $$g'(x) = 3x^2 \sin x + x^3 \cos x.$$
>
> **Por qué importa:** el segundo término mantiene $\sin x$ intacto; si hubieras escrito $3x^2 \cos x$ estarías multiplicando las derivadas, que es el error clásico.

> [!example] 🎯 Ejemplo 3: regla del cociente
>
> **Derivar** $h(x) = \frac{2x+1}{x^2+3}$.
>
> - $f(x) = 2x+1$ con $f'(x) = 2$; $g(x) = x^2+3$ con $g'(x) = 2x$.
> - Aplicando la regla del cociente:
>
> $$h'(x) = \frac{2(x^2+3) - (2x+1)(2x)}{(x^2+3)^2} = \frac{2x^2+6-4x^2-2x}{(x^2+3)^2} = \frac{-2x^2-2x+6}{(x^2+3)^2}.$$
>
> **Por qué importa:** el orden del numerador decide el signo de todo el resultado.

> [!example] 🎯 Ejemplo 4: cociente con producto adentro
>
> **Derivar** $k(x) = \frac{x^2 e^x}{\ln x}$.
>
> - Numerador $u(x) = x^2 e^x$: $u'(x) = 2x e^x + x^2 e^x = e^x(2x + x^2)$.
> - Denominador $v(x) = \ln x$: $v'(x) = \frac{1}{x}$.
> - Aplicando la regla del cociente:
>
> $$k'(x) = \frac{e^x(2x+x^2)\ln x - x^2 e^x \cdot \frac{1}{x}}{(\ln x)^2} = \frac{x e^x[(2+x)\ln x - 1]}{(\ln x)^2}.$$
>
> **Por qué importa:** es el patrón de "regla dentro de regla": decides con el árbol exterior (cociente) y luego resuelves el numerador con el árbol interior (producto).

---

## 🧠 Mnemotecnias para no olvidar las fórmulas

> [!tip] 🎓 Las seis frases del curso
>
> - **Reglas básicas "CMP":** **C**onstante = 0, **M**últiplo constante sale afuera, **P**otencia: baja el exponente y resta uno.
> - **Producto "PRIMERO + SEGUNDO":** primero derivado por segundo, más primero por segundo derivado.
> - **Cociente "ABAJO ARRIBA MENOS ARRIBA ABAJO":** $\frac{\text{ABAJO} \cdot \text{ARRIBA}' - \text{ARRIBA} \cdot \text{ABAJO}'}{(\text{ABAJO})^2}$.
> - **Trigonométricas "SICO TANECO":** **SI**n → **CO**s; **CO**s → **-SI**n; **TAN** → **SEC²**; **COT** → **-CSC²**.
> - **Exponenciales "LA E SE QUEDA":** $e^x$ se queda igual; $a^x$ se multiplica por $\ln a$.
> - **Logarítmicas "UNO SOBRE X":** $\ln x \to \frac{1}{x}$; $\log_a x \to \frac{1}{x \ln a}$.
>
> **Por qué importa:** en un parcial no hay tiempo de derivar desde cero; lo que se memoriza es el patrón, y el patrón se recuerda mejor con una frase que con una fórmula suelta.

> [!info] 🎨 Método de estudio visual: el árbol de derivación
>
> 1. Dibuja la función como raíz.
> 2. Identifica qué regla aplicar (ramas principales).
> 3. Descompón en subfunciones (ramas menores).
> 4. Deriva cada parte (hojas).
> 5. Combina según la regla (fruto final).
>
> **Colores sugeridos:** verde para reglas básicas (constante, potencia, suma), azul para producto, rojo para cociente, amarillo para trigonométricas y naranja para exponenciales y logarítmicas.
>
> **Ejemplo:** para $\frac{x^2 e^x}{\ln x}$ la raíz se parte en cociente (rojo), el numerador en producto (azul) y $\ln x$ en logarítmica (naranja).

---

## 🔍 Estrategias de resolución

> [!info] 💡 Algoritmo de derivación en cuatro pasos
>
> 1. **Identificación:** ¿es suma o diferencia? → término a término; ¿producto? → regla del producto; ¿cociente? → regla del cociente; ¿función simple? → tabla de derivadas.
> 2. **Descomposición:** separa la función "exterior" de la "interior", saca las constantes multiplicativas y simplifica la expresión si conviene.
> 3. **Aplicación:** aplica la regla elegida paso a paso, sin saltos, manteniendo ordenados los términos.
> 4. **Simplificación y verificación:** factoriza, combina términos semejantes y comprueba el resultado.
>
> **Por qué importa:** la mitad de los errores no son de cálculo sino de elección: se deriva mal porque se eligió mal la regla. Los pasos 1 y 2 existen para que eso no pase.
>
> **Ejemplo:** en $\frac{x^3}{x}$ el paso 2 (simplificar) ahorra aplicar la regla del cociente entera: $x^3/x = x^2$ y $(x^2)' = 2x$.

> [!success] ✅ Tres formas de verificar tu derivada
>
> 1. **Numérica:** evalúa $\frac{f(x+h)-f(x)}{h}$ con $h$ muy pequeño y compara con tu resultado.
> 2. **Gráfica:** grafica $f$ y $f'$; donde $f$ crece, $f'$ debe ser positiva, y los máximos de $f$ deben caer donde $f' = 0$.
> 3. **Por integración:** si $F'(x) = f(x)$, entonces $\int f(x)\,dx$ devuelve $F(x) + C$.
>
> **Por qué importa:** verificar cuesta segundos y detecta el error más común: una regla mal aplicada que ni siquiera produce una curva con el signo correcto.

---

## ⚠️ Errores comunes y cómo evitarlos

> [!warning] 🚨 Los seis errores que más se repiten
>
> 1. **Producto:** $(fg)' = f'g'$ es **incorrecto**; lo correcto es $(fg)' = f'g + fg'$.
> 2. **Cociente:** invertir el numerador, $\frac{fg' - f'g}{g^2}$, cambia el signo de todo; lo correcto es $\frac{f'g - fg'}{g^2}$.
> 3. **Signo en trigonométricas:** $\frac{d}{dx}[\cos x] = \sin x$ es incorrecto; lo correcto es $-\sin x$ (y lo mismo para $\cot$ y $\csc$).
> 4. **Potencia con exponente negativo:** $\frac{d}{dx}[x^{-2}] = -2x^{-3}$ sí, pero al final conviene escribir $-\frac{2}{x^3}$ para no confundir el signo.
> 5. **Constantes sin factorizar:** deriva más lento y con más errores no sacar las constantes al principio; $\frac{d}{dx}[3x^2+6x] = 3\frac{d}{dx}[x^2] + 6\frac{d}{dx}[x] = 6x+6$.
> 6. **Confundir $\ln x$ con $\log x$:** $\frac{d}{dx}[\ln x] = \frac{1}{x}$, mientras que $\frac{d}{dx}[\log_{10} x] = \frac{1}{x \ln 10}$.
>
> **Por qué importa:** los cinco primeros se corrigen con una sola revisión de signos y de orden; el sexto es una confusión de notación que invalida la respuesta completa.

---

## 🌍 Aplicaciones y contexto

> [!note] 🌐 Dónde se usan estas reglas
>
> - **Cinemática:** con $s(t) = 5t^3 - 2t^2 + t$ la velocidad es $v(t) = s'(t) = 15t^2 - 4t + 1$ y la aceleración $a(t) = v'(t) = 30t - 4$.
> - **Crecimiento poblacional:** $P(t) = P_0 e^{rt}$ tiene $P'(t) = rP(t)$, es decir, la tasa de crecimiento es proporcional a la población.
> - **Economía:** si $C(x) = 1000 + 50x + 0.1x^2$ es el costo total, $C'(x) = 50 + 0.2x$ es el costo marginal, el costo de producir una unidad más.
> - **Ingeniería:** en un capacitor, $i(t) = C \frac{dv}{dt}$; en un inductor, $v(t) = L \frac{di}{dt}$.
> - **Química:** la velocidad de reacción de primer orden es $r = -\frac{d[A]}{dt} = k[A]$.
>
> **Por qué importa:** la misma fórmula de potencia resuelve un polinomio de examen y el modelo de costo de una empresa. Por eso los exámenes de la unidad mezclan casos aplicados.
>
> **Ejemplo:** con $B(x) = R(x) - C(x) = 50x - 0.6x^2 - 1000$ el beneficio marginal es $B'(x) = 50 - 1.2x$, y $B'(x) = 0$ da la producción óptima.

> [!info] 🖼️ Las reglas, en cuatro campos profesionales
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Reglas_Fundamentales_de_Derivación_02.svg]]
>
> **Se lee así:** la raíz es el conjunto de reglas de derivación y de ahí sale un rombo que abre hacia cuatro áreas profesionales: física, economía, ingeniería y ciencias naturales. Cada área se desglosa en tres campos concretos, desde la cinemática y las ondas hasta el análisis marginal, el control de sistemas y la química cinética.
>
> **Por qué importa:** te muestra que las mismas reglas sirven en campos muy distintos y por qué en la carrera te van a pedir casos aplicados y no solo fórmulas sueltas.
>
> **Ejemplo:** en el modelo logístico de biología, $P(t) = \frac{K}{1+ae^{-rt}}$, la tasa $P'(t)$ sale de derivar la exponencial interna con la regla de la cadena.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Polinomio completo

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = 3x^4 - 2x^3 + 5x^2 - 7x + 9$ usando las reglas básicas y verifica el resultado en $x = 1$ por el cociente incremental con $h = 0.001$.
>
> > [!success]- ✅ Solución
> >
> > Se deriva término a término con potencia, múltiplo constante y constante:
> >
> > $$f'(x) = 12x^3 - 6x^2 + 10x - 7.$$
> >
> > Verificación: $f'(1) = 12 - 6 + 10 - 7 = 9$.
> >
> > Con $h = 0.001$: $f(1) = 8$ y $f(1.001) = 3(1.001)^4 - 2(1.001)^3 + 5(1.001)^2 - 7(1.001) + 9 = 8.009006...$, de modo que $\frac{f(1.001)-f(1)}{0.001} \approx 9.006$, que se acerca a $9$.

### ✏️ Ejercicio 2 — Regla del producto

> [!example] 📋 Planteamiento
>
> Deriva $g(x) = x^3 \sin x$ con la regla del producto y determina la pendiente de la tangente en $x = 0$.
>
> > [!success]- ✅ Solución
> >
> > $f(x) = x^3$ con $f'(x) = 3x^2$; $g(x) = \sin x$ con $g'(x) = \cos x$.
> >
> > $$g'(x) = 3x^2 \sin x + x^3 \cos x.$$
> >
> > En $x = 0$: $g'(0) = 0 + 0 = 0$, así que la tangente al origen es horizontal, $y = 0$.

### ✏️ Ejercicio 3 — Regla del cociente

> [!example] 📋 Planteamiento
>
> Deriva $h(x) = \frac{2x+1}{x^2+3}$ y comprueba si puede anularse el numerador de tu resultado.
>
> > [!success]- ✅ Solución
> >
> > $$h'(x) = \frac{2(x^2+3) - (2x+1)(2x)}{(x^2+3)^2} = \frac{-2x^2-2x+6}{(x^2+3)^2}.$$
> >
> > El numerador $-2x^2-2x+6 = 0$ cuando $x^2 + x - 3 = 0$, es decir $x = \frac{-1 \pm \sqrt{13}}{2} \approx 1.30$ o $-2.30$: ahí $h$ tiene tangente horizontal. El denominador nunca se anula, así que la derivada está definida en todo $\mathbb{R}$.

### ✏️ Ejercicio 4 — Cociente con producto adentro

> [!example] 📋 Planteamiento
>
> Deriva $k(x) = \frac{x^2 e^x}{\ln x}$ (dominio $x > 0$ y $x \neq 1$) combinando la regla del cociente con la del producto.
>
> > [!success]- ✅ Solución
> >
> > Numerador $u = x^2 e^x$ con $u' = 2x e^x + x^2 e^x = e^x(2x + x^2)$; denominador $v = \ln x$ con $v' = 1/x$.
> >
> > $$k'(x) = \frac{e^x(2x+x^2)\ln x - x^2 e^x \cdot \frac{1}{x}}{(\ln x)^2} = \frac{x e^x[(2+x)\ln x - 1]}{(\ln x)^2}.$$
> >
> > En $x = 1$ el denominador $\ln x$ se anula, así que la derivada no existe en ese punto: el dominio de $k'$ es $x > 0$ con $x \neq 1$.

### ✏️ Ejercicio 5 — Simplificar antes de derivar

> [!example] 📋 Planteamiento
>
> Deriva $f(x) = \frac{x^4 - x^2}{x^2}$ de dos formas: simplificando primero y aplicando la regla del cociente tal cual. ¿Coinciden?
>
> > [!success]- ✅ Solución
> >
> > **Forma A (simplificando):** para $x \neq 0$, $f(x) = \frac{x^4}{x^2} - \frac{x^2}{x^2} = x^2 - 1$, así que $f'(x) = 2x$.
> >
> > **Forma B (regla del cociente):** con numerador $u = x^4 - x^2$ ($u' = 4x^3 - 2x$) y denominador $v = x^2$ ($v' = 2x$):
> >
> > $$f'(x) = \frac{(4x^3-2x)x^2 - (x^4-x^2)(2x)}{x^4} = \frac{4x^5 - 2x^3 - 2x^5 + 2x^3}{x^4} = \frac{2x^5}{x^4} = 2x.$$
> >
> > **Coinciden:** $f'(x) = 2x$. La forma A es más corta porque cancela términos antes de derivar; la forma B es más larga pero verifica que la regla del cociente funciona aunque la expresión se pueda simplificar.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Derivo un polinomio término a término sin mirar la tabla.
> - [ ] Escribo de memoria las reglas de producto y de cociente con su mnemotecnia.
> - [ ] Distingo cuándo una función pide producto, cuándo cociente y cuándo basta la potencia.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Derivo funciones que combinan dos o más reglas (cociente con producto adentro).
> - [ ] Reproduzco de memoria las derivadas de las seis trigonométricas y sus signos.
> - [ ] Verifico una derivada con el cociente incremental y con la gráfica.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Elijo simplificar antes de derivar cuando la expresión lo permite.
> - [ ] Aplico las reglas a un problema de costo marginal o de velocidad sin perder el contexto.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 3: reglas de derivación.
> - R. Larson, *Cálculo* (Cengage), cap. 3: producto, cociente y potencia.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la definición de la que salen estas reglas.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la regla que completa este conjunto.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] — la tabla resumen para consulta rápida.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice la regla de la potencia y para qué valores de $n$ vale?::$\frac{d}{dx}[x^n] = n x^{n-1}$ para cualquier $n$ real; el exponente baja y se resta uno.
> - ¿Cuál es la regla del producto?::$(fg)' = f'g + fg'$: se deriva cada factor por turnos y se suman los dos términos.
> - ¿Qué orden tiene el numerador de la regla del cociente?::$\frac{f'g - fg'}{g^2}$: primero la derivada del numerador por el denominador, menos numerador por derivada del denominador, todo sobre el denominador al cuadrado.
> - ¿Qué signo tienen las derivadas de $\cos$, $\cot$ y $\csc$?::Negativo: $-\sin x$, $-\csc^2 x$ y $-\csc x \cot x$.
> - ¿Qué dos reglas fallan si no simplificas antes?::Ninguna falla, pero simplificar antes evita errores de signo: en $\frac{x^4-x^2}{x^2}$ conviene reducir a $x^2-1$ antes de derivar.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — de dónde salen todas estas reglas.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la composición, que completa el conjunto.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — cuando la función no viene despejada.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]] — cuando conviene tomar $\ln$ antes de derivar.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — donde estas reglas se usan a fondo.
>
> **El mapa de la herramientería:**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Reglas_Fundamentales_de_Derivación_03.svg]]
>
> **Se lee así:** un cuadro raíz "Reglas de Derivación" despliega cuatro subgrafos de rectángulos: reglas básicas (constante, potencia, múltiplo constante, suma y diferencia), reglas avanzadas (producto, cociente, cadena, implícita), funciones elementales (algebraicas, trigonométricas, exponenciales, logarítmicas, hiperbólicas) y aplicaciones (física, economía, ingeniería, optimización).
>
> **Por qué importa:** te sirve como índice mental del temario: en un parcial solo puedes estar en una de esas ramas, y saber en cuál te dice qué fórmula abrir.
>
> **Ejemplo:** si el ejercicio pide derivar $e^x \ln x$, vas a la rama de reglas avanzadas (producto) y a la de funciones elementales (logarítmica), y combinas $e^x \ln x + e^x \frac{1}{x}$.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica hasta que el árbol de decisión sea automático: identifica el tipo de función antes de escribir cualquier fórmula.
> - Después salta a [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] para las funciones compuestas.
> - Consulta [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] como chuleta rápida antes de un parcial.
> - Cuando aparezcan ecuaciones con $y$ mezclada, ve a [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]].

---

**Tags:** #MATG1045 #unidad4 #reglas-fundamentales-de-derivacion #potencia #regla-producto #regla-cociente #funciones-elementales #mnemotecnia

---
dg-publish: true
tags: [MATG1045, unidad2, propiedades-limite, teoremas-limite, algebra-de-limites, sustitucion-directa, continuidad, emparedado, caracterizacion-sucesional, criterio-cauchy]
---

# ⚖️ Propiedades y Teoremas de los Límites

## 🎯 Introducción

> [!info] 💡 ¿Para qué sirven las propiedades?
>
> Las **propiedades de los límites** (también llamadas **álgebra de límites**) son reglas que permiten calcular límites de expresiones complejas a partir de límites más simples. En vez de demostrar cada límite desde cero con $\varepsilon$-$\delta$, se descompone la expresión, se resuelven las piezas y se recombinan.
>
> **Condición previa:** todas las propiedades exigen que los límites individuales que se usan **existan y sean finitos**. Si alguno no existe, la regla no se puede aplicar.
>
> **Ejemplo:** $\lim_{x \to 2} \frac{x^3 + 2x^2 - 3x + 1}{x^2 - 1}$ se resuelve en tres cuentas: el numerador tiende a $11$, el denominador a $3$ y el cociente da $11/3$.

> [!warning] ⚠️ Lo que NO autorizan las propiedades
>
> - **NO autorizan** dividir cuando el denominador tiende a $0$.
> - **NO autorizan** sustituir en una forma indeterminada como $0/0$ o $\infty/\infty$.
> - **NO autorizan** componer $f(g(x))$ con $f$ discontinua en el límite interno.
>
> Y lo que sí autorizan:
>
> - **SÍ permiten** separar sumas, productos, cocientes, potencias y raíces cuando todos los límites implicados existen.
> - **SÍ permiten** sustituir directamente cuando la función es continua en el punto.
> - **SÍ permiten** extenderse a límites laterales, $\lim_{x \to a^+}$ y $\lim_{x \to a^-}$, sin cambiar de reglas.

> [!tip] 🔢 Estrategia de descomposición en cuatro pasos
>
> 1. **Identificar la estructura:** ¿suma, producto, cociente, potencia o composición?
> 2. **Descomponer:** separar la expresión en piezas más simples.
> 3. **Evaluar cada pieza:** usar sustitución directa cuando la función sea continua.
> 4. **Recombinar:** aplicar la propiedad correspondiente y escribir el resultado.
>
> **Por qué importa:** el orden evita el error clásico de intentar una técnica pesada (factorización, L'Hôpital) en un límite que se resuelve sustituyendo.
>
> **Ejemplo:** $\lim_{x \to 3} (2x^3 - x^2 + 4x - 7) = 50$ se obtiene pieza a pieza: $2(27) - 9 + 12 - 7$.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Álgebra de límites
>
> Sean $\lim_{x \to a} f(x) = L$ y $\lim_{x \to a} g(x) = M$, con $L$ y $M$ números reales (es decir, ambos límites existen y son finitos). Entonces se cumplen:
>
> - **Suma y diferencia:** $\lim_{x \to a} [f(x) \pm g(x)] = L \pm M$
> - **Producto:** $\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$
> - **Cociente:** $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M}$, si $M \neq 0$
> - **Potencia:** $\lim_{x \to a} [f(x)]^n = L^n$, si la potencia está definida
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_01.svg]]
>
> **Se lee así:** el esquema parte de un límite complejo y pasa por un rombo que pregunta por la operación principal. Cada rama aplica su regla: suma o resta lleva a límites separados y al resultado $L \pm M$; producto lleva al producto de límites; división pasa por un rombo sobre el denominador, que si es cero deriva a técnicas especiales; potencia o raíz pasa por un rombo sobre las condiciones de dominio, que si fallan obliga a redefinir el dominio.
>
> **Por qué importa:** el rombo del denominador y el de dominio son los dos filtros de validez del álgebra. Te recuerdan que la regla no se aplica a ciegas: primero verifica que cada pieza exista y que la operación tenga sentido.
>
> **Ejemplo:** para $\lim_{x \to 2} \frac{x^2 - 1}{x + 3}$ el denominador tiende a $5 \neq 0$, así que se aplica el cociente y el resultado es $3/5$.

> [!note] 📋 Definición — Sustitución directa
>
> Si $f$ está **definida** y es **continua** en $x = a$, entonces
>
> $$\lim_{x \to a} f(x) = f(a).$$
>
> Es decir, basta sustituir el valor en la función.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_04.svg]]
>
> **Se lee así:** el diagrama es un atajo de dos rutas: del rectángulo inicial sale un rombo que pregunta si la función es continua en el punto. La rama afirmativa va a la **sustitución directa** y de ahí al resultado $f(a)$; la negativa salta a un rectángulo de otras técnicas, que se desglosa en factorización y en la regla de L'Hôpital.
>
> **Por qué importa:** la continuidad es la llave que decide si trabajas o no. Aplicar el atajo te ahorra factorizar o invocar L'Hôpital en límites que se resuelven en un segundo, como los de cualquier polinomio.
>
> **Ejemplo:** para $\lim_{x \to 2} (3x^3 - 2x^2 + x - 5)$ la función es continua, así que sustituyes y obtienes $13$ sin factorizar.

> [!note] 📋 Definición — Teorema del emparedado (sandwich)
>
> Si existen tres funciones $g$, $f$ y $h$ tales que $g(x) \leq f(x) \leq h(x)$ para toda $x$ cerca de $a$ (sin importar en $a$), y si
>
> $$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L,$$
>
> entonces $\lim_{x \to a} f(x) = L$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_08.svg]]
>
> **Se lee así:** el esquema arranca en la búsqueda de dos funciones que acoten a $f(x)$, sigue con la verificación de la cadena $g(x) \leq f(x) \leq h(x)$ cerca de $a$ y llega a un rombo que pregunta si los límites de $g$ y $h$ coinciden en $L$. Si no coinciden, el teorema no permite concluir; si coinciden, la conclusión es que el límite de $f$ es $L$.
>
> **Por qué importa:** es la herramienta que resuelve límites que no se pueden calcular ni sustituyendo ni factorizando, como $\lim_{x \to 0} x^2 \sin(1/x)$. La rama negativa del rombo recuerda que acotar por un lado solo no basta: hace falta que las dos cotas converjan.
>
> **Ejemplo:** como $-x^2 \leq x^2 \sin(1/x) \leq x^2$ y ambos extremos tienden a $0$, el límite central es $0$.

> [!note] 📋 Definición — Caracterización por sucesiones
>
> $\lim_{x \to a} f(x) = L$ si y solo si, para **toda** sucesión $x_n \to a$ con $x_n \neq a$ para todo $n$, se cumple $f(x_n) \to L$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_09.svg]]
>
> **Se lee así:** el esquema parte de tomar cualquier sucesión $x_n$ que tienda a $a$, pasa por un rombo que exige que cada término sea distinto de $a$, evalúa la sucesión $f(x_n)$ y llega a un segundo rombo: si **todas** las sucesiones producen valores que tienden a $L$, el límite de $f$ es $L$; si una sola sucesión falla, esa sucesión revela que el límite no existe.
>
> **Por qué importa:** convierte un problema de todos los $x$ en un problema de sucesiones, y sobre todo da una **receta para desmentir**: basta una sucesión que dé valores distintos para probar que el límite no es el propuesto.
>
> **Ejemplo:** $\lim_{x \to 0} \sin(1/x)$ no existe porque con $x_n = 1/(n\pi)$ se obtiene $\sin(n\pi) = 0$, mientras que con $y_n = 1/((2n+1)\pi/2)$ se obtiene $\sin = 1$.

> [!note] 📋 Definición — Criterio de Cauchy
>
> $\lim_{x \to a} f(x)$ existe (y es finito) si y solo si: para todo $\varepsilon > 0$ existe $\delta > 0$ tal que, para todo $x, z$ con $0 < |x - a| < \delta$ y $0 < |z - a| < \delta$,
>
> $$|f(x) - f(z)| < \varepsilon.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_10.svg]]
>
> **Se lee así:** el esquema arranca preguntando por la distancia entre valores cercanos, pasa por un rombo que exige la condición $\forall \varepsilon > 0\ \exists \delta > 0$ y por otro que comprueba que si $x$ y $z$ están cerca de $a$, entonces $f(x)$ y $f(z)$ están cerca la una de la otra. Si ambas se cumplen, la función es Cauchy cerca de $a$ y existe un único límite; si alguna falla, la condición de Cauchy falla.
>
> **Por qué importa:** a diferencia de la definición usual, este criterio **no necesita conocer $L$** para verificar la existencia. Por eso sirve para demostrar que un límite existe antes de saber cuál es.
>
> **Ejemplo:** para $f(x) = \sum_{k=1}^{n} 1/k^2$ acotada cerca de $0$, la diferencia $|f(x) - f(z)|$ se controla por la cola de la serie y se hace menor que $\varepsilon$ con un $\delta$ adecuado.

> [!note] 📋 Definición — Unicidad del límite
>
> Si $\lim_{x \to a} f(x)$ existe, es **único**: no pueden convivir dos valores distintos $L_1 \neq L_2$ con la función acercándose a ambos.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_11.svg]]
>
> **Se lee así:** el esquema supone dos límites $L_1$ y $L_2$, toma una tolerancia menor que la mitad de su distancia y obliga a que cerca de $a$ la misma $f(x)$ esté cerca de $L_1$ y a la vez cerca de $L_2$. El rombo pregunta si las dos zonas de tolerancia se contradicen: si se contradicen, la conclusión es que $L_1 = L_2$.
>
> **Por qué importa:** la unicidad garantiza que "buscar el límite" tenga sentido y que métodos distintos (sustitución, emparedado, tablas) no puedan dar respuestas incompatibles.
>
> **Ejemplo:** $\lim_{x \to 1} \frac{x^2-1}{x-1}$ vale $2$, y no puede valer a la vez $0$ o $3$: cualquier banda de $\varepsilon = 1/2$ alrededor de $2$ excluye a los otros dos.

---

## 📐 Teoremas del álgebra de límites

> [!success] ✅ Teorema de suma y diferencia
>
> Si $\lim_{x \to a} f(x) = L$ y $\lim_{x \to a} g(x) = M$, entonces:
>
> $$\lim_{x \to a} [f(x) + g(x)] = L + M, \qquad \lim_{x \to a} [f(x) - g(x)] = L - M.$$
>
> **Reglas derivadas:**
>
> 1. **Constante:** $\lim_{x \to a} c = c$
> 2. **Múltiplo:** $\lim_{x \to a} [c \cdot f(x)] = c \cdot L$
> 3. **Suma finita:** $\lim_{x \to a} [f_1 + \dots + f_n] = L_1 + \dots + L_n$
>
> | Operación | Notación | Resultado | Condición |
> |---|---|---|---|
> | Suma | $\lim [f + g]$ | $L + M$ | Ambos límites existen |
> | Diferencia | $\lim [f - g]$ | $L - M$ | Ambos límites existen |
> | Constante por función | $\lim [c \cdot f]$ | $c \cdot L$ | El límite de $f$ existe |
> | Suma múltiple | $\lim [f_1 + \dots + f_n]$ | $L_1 + \dots + L_n$ | Todos existen |
>
> **Ejemplo:** $\lim_{x \to 2} [(x^2 + 3) + (2x - 1)] = 7 + 3 = 10$, porque $x^2 + 3 \to 7$ y $2x - 1 \to 3$.

> [!success] ✅ Teorema de producto y cociente
>
> Si $\lim_{x \to a} f(x) = L$ y $\lim_{x \to a} g(x) = M$, entonces:
>
> $$\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M, \qquad \lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M} \ \text{si } M \neq 0.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_02.svg]]
>
> **Se lee así:** el diagrama abre con una casilla de producto o cociente y un rombo que exige verificar primero que los límites individuales existen; la rama negativa lleva a una casilla que advierte que el teorema no se aplica. Si existen, otro rombo separa producto y cociente: el producto va directo a multiplicar límites y el cociente pasa por un rombo extra sobre el denominador.
>
> **Por qué importa:** este es el filtro de validez de ambas reglas: primero los límites individuales, después el denominador. Te ahorra escribir una cuenta que no vale y te indica cuándo cambiar a factorización u otra técnica.
>
> **Ejemplo:** para $\lim_{x \to 2} \frac{x^2 - 1}{x + 3}$ los límites individuales existen y el denominador tiende a $5$, así que el resultado es $3/5$.
>
> **Casos del cociente:**
>
> | Situación | $\lim f(x)$ | $\lim g(x)$ | $\lim \frac{f(x)}{g(x)}$ | Acción |
> |---|---|---|---|---|
> | Normal | $L$ | $M \neq 0$ | $L/M$ | Aplicar el teorema |
> | Infinito | $L \neq 0$ | $0$ | $\pm\infty$ | Límite no existe (asíntota) |
> | Indeterminada | $0$ | $0$ | ¿? | Factorizar o racionalizar |
> | Indeterminada | $\infty$ | $\infty$ | ¿? | Ver nota de formas indeterminadas |

> [!success] ✅ Teorema de potencia y raíz
>
> Si $\lim_{x \to a} f(x) = L$ existe, entonces:
>
> $$\lim_{x \to a} [f(x)]^n = L^n \ (n \in \mathbb{Z}), \qquad \lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{L} \ \text{(si la raíz está definida)}.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_07.svg]]
>
> **Se lee así:** el esquema arranca en la evaluación de una potencia o una raíz y pasa por un rombo que pregunta si el límite de $f(x)$ existe y es finito; si no, la rama lleva a no aplicar la regla. Si existe, un segundo rombo comprueba que la potencia esté definida sobre el dominio y solo entonces se sustituye el límite $L$ en la potencia, con resultado $L$ elevado al exponente.
>
> **Por qué importa:** las dos restricciones son las que suelen olvidarse. Exponente negativo exige $L \neq 0$, raíz par exige $L \geq 0$ y exponente racional $p/q$ exige verificar el dominio de la raíz.
>
> **Ejemplo:** $\lim_{x \to 5} \sqrt{2x - 1} = \sqrt{9} = 3$, porque el límite interno es $9 \geq 0$ y la raíz está definida.
>
> | Tipo de potencia | Condición | Ejemplo | Resultado |
> |---|---|---|---|
> | Cuadrado | $L$ cualquiera | $\lim_{x \to 2} (x-1)^2$ | $1$ |
> | Raíz cuadrada | $L \geq 0$ | $\lim_{x \to 4} \sqrt{x-3}$ | $1$ |
> | Raíz cúbica | $L$ cualquiera | $\lim_{x \to -1} \sqrt[3]{x+9}$ | $2$ |
> | Potencia negativa | $L \neq 0$ | $\lim_{x \to 1} (x+1)^{-2}$ | $1/4$ |

> [!note] 🎭 Teorema de composición de funciones
>
> Si $\lim_{x \to a} g(x) = L$ y $f$ es **continua en $L$**, entonces
>
> $$\lim_{x \to a} f(g(x)) = f\!\left(\lim_{x \to a} g(x)\right) = f(L).$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_03.svg]]
>
> **Se lee así:** se ve un recorrido de peldaños: partir del límite de una composición, calcular primero el límite de la función interna y llegar a un rombo que pregunta si ese límite existe. Si existe, un segundo rombo indaga si la función externa es **continua** en ese valor y solo entonces se aplica $f$ en $L$; cada rombo fallido abre una salida que detiene el procedimiento.
>
> **Por qué importa:** el orden importa: primero se resuelve la función interna y solo después se evalúa la externa en ese valor, y solo si la externa es continua. Saltarse esa verificación es la causa más común de resultados falsos en límites compuestos con $\sin$, $e^u$ o $\ln$.
>
> **Ejemplo:** para $\lim_{x \to 2} \ln(x^2 - 3)$ el límite interno es $1$, se verifica que $\ln$ es continua en $1$ y el resultado es $\ln(1) = 0$.
>
> | Función externa $f$ | Condición en $L$ | Ejemplo | Evaluación |
> |---|---|---|---|
> | $\sin(u)$ | Siempre continua | $\lim_{x \to 0} \sin(x^2)$ | $\sin(0) = 0$ |
> | $e^u$ | Siempre continua | $\lim_{x \to 1} e^{2x-2}$ | $e^{0} = 1$ |
> | $\ln(u)$ | $L > 0$ | $\lim_{x \to 2} \ln(x^2)$ | $\ln(4)$ |
> | $\sqrt{u}$ | $L \geq 0$ | $\lim_{x \to 3} \sqrt{x+1}$ | $\sqrt{4} = 2$ |
> | $1/u$ | $L \neq 0$ | $\lim_{x \to 1} \frac{1}{x+2}$ | $1/3$ |

> [!tip] 🎓 Mnemotecnia "SPCP"
>
> - **S**uma: límite de suma = suma de límites.
> - **P**roducto: límite de producto = producto de límites.
> - **C**ociente: límite de cociente = cociente de límites (denominador $\neq 0$).
> - **P**otencia: límite de potencia = potencia del límite.
>
> **Frase:** *"Suma, Producto, Cociente, Potencia — Siempre Preservan Cálculos Precisos"*.
>
> **Regla adicional para composición:** *"Componer funciones: límite interno + continuidad externa"*.

---

## 🚀 Límites directos: sustitución y continuidad

> [!success] ✅ Polinomios y funciones racionales
>
> - **Polinomios:** continuos en todos los reales, así que $\lim_{x \to a} P(x) = P(a)$ siempre.
> - **Racionales:** $f(x) = P(x)/Q(x)$ es continua donde $Q(a) \neq 0$; donde $Q(a) = 0$ hay que analizar.
>
> | Tipo de función | Dominio de continuidad | Ejemplo | $\lim_{x \to 1}$ |
> |---|---|---|---|
> | Polinomial | $\mathbb{R}$ | $x^2 + 3x - 2$ | $1 + 3 - 2 = 2$ |
> | Racional | $\mathbb{R}$ salvo donde el denominador es $0$ | $\frac{x+2}{x-3}$ | $\frac{3}{-2} = -\frac{3}{2}$ |
>
> **Ejemplo:** $\lim_{x \to 3} \frac{x^2 + 2x - 1}{x - 1} = \frac{9 + 6 - 1}{3 - 1} = 7$, porque el denominador vale $2 \neq 0$.

> [!tip] 🌊 Funciones trigonométricas, exponenciales y logarítmicas
>
> | Función | Dominio de continuidad | Puntos de discontinuidad |
> |---|---|---|
> | $\sin(x)$, $\cos(x)$ | $\mathbb{R}$ | Ninguno |
> | $\tan(x)$ | $\mathbb{R} \setminus \{\frac{\pi}{2} + n\pi\}$ | $x = \frac{\pi}{2} + n\pi$ |
> | $\cot(x)$ | $\mathbb{R} \setminus \{n\pi\}$ | $x = n\pi$ |
> | $a^x$ ($a > 0$, $a \neq 1$) | $\mathbb{R}$ | Ninguno |
> | $\log_a(x)$ ($a > 0$, $a \neq 1$) | $(0, +\infty)$ | Ninguno |
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_05.svg]]
>
> **Se lee así:** es un gráfico circular partido en dos porciones, con un título arriba que anuncia el bloque de continuidad trigonométrica. La porción grande, del 60%, corresponde a las funciones continuas salvo en puntos concretos, y la chica, del 40%, a las continuas en todo $\mathbb{R}$; la leyenda de colores aclara a cuál parte corresponde cada rótulo.
>
> **Por qué importa:** la mayor parte de las funciones trigonométricas tiene puntos de corte, así que antes de sustituir tienes que verificar la continuidad en ese punto. Esto te evita responder $\tan(\pi/2)$ cuando lo que te piden es el **límite**.
>
> **Ejemplo:** $\lim_{x \to \pi/3} \tan(x) = \sqrt{3}$ por sustitución directa, porque la tangente es continua en $\pi/3$.

> [!info] 🗺️ Algoritmo de decisión para límites directos
>
> 1. **¿El punto está en el dominio?** Si no, no se sustituye.
> 2. **¿La función es continua en el punto?** Si sí, sustituir: $\lim_{x \to a} f(x) = f(a)$.
> 3. **Si no es continua:** analizar límites laterales y discontinuidad, o aplicar técnicas especiales (factorización, racionalización, emparedado).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Propiedades_y_Teoremas_de_los_Límites_06.svg]]
>
> **Se lee así:** el diagrama es un filtro de dos decisiones sucesivas: primero un rombo que pregunta si el punto de aproximación pertenece al dominio, y luego otro que pregunta si la función es continua ahí. Cada "no" lleva a una salida distinta —técnicas especiales si el punto está fuera del dominio y límites laterales con análisis de discontinuidad si no es continua—; el "sí" doble desemboca en la sustitución directa.
>
> **Por qué importa:** el diagrama ordena las comprobaciones de más básica a más específica: primero que el punto esté en el dominio y luego la continuidad. Así detectas temprano los casos en que no se puede sustituir y evitas perder tiempo con técnicas que no tocan el problema.
>
> **Ejemplo:** para $\lim_{x \to 0} \frac{2x + 1}{x^2 + 4}$ el punto está en el dominio y la función es continua, así que la sustitución directa da $1/4$.

> [!warning] ⚠️ Cuándo NO usar sustitución directa
>
> - La función **no está definida** en el punto.
> - Resulta una **forma indeterminada:** $0/0$, $\infty/\infty$, $0 \cdot \infty$, $\infty - \infty$.
> - Hay **discontinuidad** en el punto de evaluación (salto o asíntota).
>
> **En esos casos:** factorizar, racionalizar, usar el emparedado o pasar a la nota de formas indeterminadas.
>
> **Por qué importa:** sustituir en una indeterminada produce una respuesta falsa con apariencia correcta, que es el error más caro en un examen.
>
> **Ejemplo:** $\lim_{x \to 4} \frac{x^2 - 16}{x - 4}$ da $0/0$ al sustituir; factorizando, $\frac{(x-4)(x+4)}{x-4} = x+4 \to 8$.

---

## ⚠️ Errores y Trampas Frecuentes

> [!warning] 🚨 Errores en el álgebra de límites
>
> - **Dividir sin verificar el denominador:** si $M = 0$ y $L \neq 0$, el límite no existe (infinito); si ambos son $0$, es indeterminado.
> - **Aplicar la regla con límites que no existen:** las propiedades exigen que todos los límites implicados existan y sean finitos.
> - **Raíz de un número negativo:** para raíces pares verifica que el límite interno sea $\geq 0$; para impares no hay restricción.
> - **Exponente negativo con $L = 0$:** la potencia no está definida y la regla no se aplica.
> - **Componer con la externa discontinua:** $\lim f(g(x)) = f(\lim g(x))$ solo si $f$ es continua en el límite interno.
>
> **Por qué importa:** los cinco errores son de condiciones de aplicación, no de cálculo; ninguno se detecta revisando la aritmética, se detecta revisando las hipótesis del teorema.
>
> **Ejemplo:** $\lim_{x \to 0} \frac{\sin x}{x}$ no se resuelve sustituyendo ($0/0$): el límite vale $1$ por un teorema especial, no por el cociente de límites.

> [!warning] 🚫 Trampas en la sustitución directa
>
> - **Sustituir donde no hay dominio:** $\lim_{x \to 0} \frac{1}{x}$ no se resuelve poniendo $x = 0$.
> - **Creer que el límite es el valor de la función:** puede haber hueco o salto; el límite puede existir aunque $f(a)$ no, o ser distinto de $f(a)$.
> - **Olvidar los laterales:** si los laterales no coinciden, el límite no existe aunque cada lado se calcule bien.
> - **Usar la tabla como prueba:** la tabla sugiere, no demuestra; la demostración es la definición o un teorema.
>
> **Por qué importa:** son confusiones de concepto que arrastran el resto del problema. Revisarlas antes de dar por cerrado un ejercicio es más barato que corregirlo después.
>
> **Ejemplo:** en $f(x) = \frac{x^2-1}{x-1}$ con $f(1)$ definida como $0$, el límite en $1$ sigue siendo $2$: el valor fijo no entra en el límite.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 2} [(x^2 + 3) + (2x - 1)]$ aplicando las propiedades de suma.
>
> > [!success]- ✅ Solución
> >
> > Por la propiedad de suma, el límite de la suma es la suma de los límites:
> >
> > $$\lim_{x \to 2} (x^2 + 3) = 4 + 3 = 7, \qquad \lim_{x \to 2} (2x - 1) = 4 - 1 = 3.$$
> >
> > Ambos existen y son finitos, así que se pueden combinar: $7 + 3 = 10$. Respuesta: $\lim_{x \to 2} [(x^2 + 3) + (2x - 1)] = 10$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 3} \frac{2x^3 - x^2 + 4x - 7}{x^2 + 2x - 1}$ usando el teorema del cociente.
>
> > [!success]- ✅ Solución
> >
> > Primero verifica el denominador en $x = 3$: $9 + 6 - 1 = 14 \neq 0$, así que el cociente se puede aplicar.
> >
> > Numerador: $\lim_{x \to 3} (2x^3 - x^2 + 4x - 7) = 2(27) - 9 + 12 - 7 = 50$.
> >
> > Denominador: $\lim_{x \to 3} (x^2 + 2x - 1) = 14$.
> >
> > Resultado: $\frac{50}{14} = \frac{25}{7}$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 5} \sqrt{2x - 1}$ verificando las condiciones de la raíz.
>
> > [!success]- ✅ Solución
> >
> > El límite interno es $\lim_{x \to 5} (2x - 1) = 9$, que existe y es finito.
> >
> > Como la raíz es par, comprueba que $9 \geq 0$: se cumple, y la raíz cuadrada está definida en ese punto.
> >
> > Aplica el teorema de raíz: $\lim_{x \to 5} \sqrt{2x - 1} = \sqrt{9} = 3$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 2} \ln(x^2 - 3)$ usando el teorema de composición.
>
> > [!success]- ✅ Solución
> >
> > Función interna: $g(x) = x^2 - 3$ con $\lim_{x \to 2} g(x) = 1$.
> >
> > Función externa: $f(u) = \ln(u)$. Como $\ln$ es continua en $u = 1 > 0$, se puede aplicar el teorema de composición.
> >
> > Resultado: $\lim_{x \to 2} \ln(x^2 - 3) = \ln(1) = 0$.
> >
> > **Nota:** si el límite interno hubiera dado un valor $\leq 0$, la composición no se podría evaluar así.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to \pi/6} (\sin x \cdot \cos x + 2x)$ combinando las propiedades de suma y producto.
>
> > [!success]- ✅ Solución
> >
> > Por suma: $\lim_{x \to \pi/6} (\sin x \cdot \cos x) + \lim_{x \to \pi/6} (2x)$.
> >
> > Por producto y porque $\sin$ y $\cos$ son continuas: $\sin(\pi/6) \cdot \cos(\pi/6) = \frac{1}{2} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{4}$.
> >
> > Segundo término: $2 \cdot \frac{\pi}{6} = \frac{\pi}{3}$.
> >
> > Resultado: $\frac{\sqrt{3}}{4} + \frac{\pi}{3}$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 4} \frac{x^2 - 16}{x - 4}$ y explica por qué no aplica el teorema del cociente.
>
> > [!success]- ✅ Solución
> >
> > Al sustituir se obtiene $\frac{16 - 16}{4 - 4} = \frac{0}{0}$, una forma indeterminada: el teorema del cociente exige que el denominador tienda a un número distinto de cero, y aquí tiende a $0$.
> >
> > Se factoriza el numerador: $x^2 - 16 = (x-4)(x+4)$. Para $x \neq 4$,
> >
> > $$\frac{x^2 - 16}{x - 4} = x + 4.$$
> >
> > Ahora sí se sustituye: $\lim_{x \to 4} (x + 4) = 8$. Respuesta: $8$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 0} e^{x^2 + 2x}$ y verifica las hipótesis antes de aplicar el teorema.
>
> > [!success]- ✅ Solución
> >
> > Función interna: $g(x) = x^2 + 2x$ con $\lim_{x \to 0} g(x) = 0$.
> >
> > Función externa: $f(u) = e^u$, que es continua en todo $\mathbb R$, en particular en $0$.
> >
> > Se aplica la composición: $\lim_{x \to 0} e^{x^2 + 2x} = e^{0} = 1$.
> >
> > **Nota:** la exponencial no necesita condición adicional sobre el límite interno; con $\ln$ sí haría falta que fuera positivo.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Enuncio las propiedades de suma, producto, cociente y potencia con sus condiciones.
> - [ ] Aplico la sustitución directa a polinomios, racionales y funciones elementales continuas.
> - [ ] Identifico cuándo el cociente o la raíz no se pueden aplicar tal cual.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Descompongo un límite complejo en piezas simples y lo resuelvo con el álgebra de límites.
> - [ ] Verifico las hipótesis de composición: límite interno existente y externa continua.
> - [ ] Distingo una forma indeterminada de un cociente legítimo y elijo la técnica siguiente.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Aplico el teorema del emparedado a límites que no se resuelven sustituyendo.
> - [ ] Uso la caracterización por sucesiones para demostrar que un límite no existe.
> - [ ] Explico por qué el límite es único y qué garantiza esa unicidad en el resto del curso.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2: propiedades de los límites y límite directo.
> - R. Larson, *Cálculo* (Cengage), cap. 1: álgebra de límites y límites directos.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 3: teoremas básicos y teorema del emparedado.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — de dónde salen las reglas que aquí se aplican.
> - [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]] — qué hacer cuando el álgebra no alcanza.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — el concepto que hace válida la sustitución directa.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la condición previa de todo el álgebra de límites?::Que todos los límites individuales que se usen existan y sean finitos; si alguno no existe, la regla no se aplica.
> - ¿Cuándo puedes resolver un límite por sustitución directa?::Cuando la función está definida y es continua en el punto: entonces $\lim_{x \to a} f(x) = f(a)$.
> - ¿Qué hacer si el cociente da $0/0$?::No aplica el teorema del cociente: factorizar o racionalizar; si no se puede, pasar a la nota de formas indeterminadas.
> - ¿Qué dice el teorema del emparedado?::Si $g(x) \leq f(x) \leq h(x)$ cerca de $a$ y $\lim g = \lim h = L$, entonces $\lim f = L$; las dos cotas deben converger al mismo valor.
> - ¿Cómo se desmiente un límite con sucesiones?::Basta encontrar una sucesión $x_n \to a$ con $x_n \neq a$ cuya imagen $f(x_n)$ no tienda al valor propuesto.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la definición $\varepsilon$-$\delta$ que fundamenta todas estas reglas.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — las mismas propiedades aplicadas a $\lim_{x \to a^+}$ y $\lim_{x \to a^-}$.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/02 - Límites Especiales|02 - Límites Especiales]] — límites que no se resuelven con el álgebra directo.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/03 - Límites en Gráficas|03 - Límites en Gráficas]] — lectura visual de las mismas reglas.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — la caracterización por sucesiones llevada a sucesiones de números.
> - [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]] — los casos donde el álgebra de límites se queda corto.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — la sustitución directa como criterio de continuidad.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la derivada como límite de un cociente, con sus condiciones.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los límites directos de la sección de ejercicios hasta que la sustitución sea automática.
> - Después salta a [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|Límites Laterales]] para aprender a tratar los puntos donde la sustitución falla.
> - Cuando te encuentres con $0/0$ o $\infty/\infty$, ve directo a [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|Formas Indeterminadas]].
> - En cada problema, escribe antes de calcular **qué teorema vas a usar y por qué se cumplen sus hipótesis**.

---

**Tags:** #MATG1045 #unidad2 #propiedades-limite #teoremas-limite #algebra-de-limites #sustitucion-directa #continuidad #emparedado #caracterizacion-sucesional #criterio-cauchy

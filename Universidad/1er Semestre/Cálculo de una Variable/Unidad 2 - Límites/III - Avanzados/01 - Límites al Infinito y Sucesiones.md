---
dg-publish: true
tags: [MATG1045, unidad2, limites-al-infinito-y-sucesiones, limites, limites-infinitos, asintotas-verticales, funciones-racionales, calculo, discontinuidades, comportamiento-asintotico, analisis-signos, infinito]
---

# 🎯 Límites Infinitos, Límites al Infinito y Sucesiones

## 🎯 Introducción

> [!tip] 💡 Concepto clave de los límites infinitos
>
> Los **límites infinitos** ocurren cuando una función crece o decrece sin límite cuando la variable independiente se aproxima a un valor específico. A diferencia de los límites al infinito, aquí **x se acerca a un punto finito**, pero **f(x) tiende a infinito**.

> [!tip] 💡 Concepto clave de los límites al infinito
>
> Los límites al infinito nos permiten estudiar el **comportamiento de funciones cuando la variable independiente crece o decrece sin límite**. Son fundamentales para entender el comportamiento asintótico y las tendencias a largo plazo de las funciones.

---

## 📋 Definiciones Formales

> [!info] 📚 Definición de límite infinito
>
> Decimos que $\lim_{x \to a} f(x) = +\infty$ si para todo número $M > 0$ existe $\delta > 0$ tal que $$f(x) > M \text{ siempre que } 0 < |x - a| < \delta$$
>
> Decimos que $\lim_{x \to a} f(x) = -\infty$ si para todo número $M > 0$ existe $\delta > 0$ tal que $$f(x) < -M \text{ siempre que } 0 < |x - a| < \delta$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_08.svg]]
>
> **Se lee así:** El diagrama entra con $x$ acercándose al punto finito $a$ y llega a un rombo que pregunta qué le pasa a $f(x)$. De ahí salen dos ramas: una donde la función crece más que cualquier cota $M$ y otra donde decrece más que cualquier cota. Cada rama lleva a su recuadro de límite infinito, positivo o negativo, y las dos convergen en el recuadro de que la recta $x = a$ es asíntota vertical. Un último recuadro recuerda que escribir ese símbolo no significa que el límite exista.
>
> **Por qué importa:** La $\delta$ del enunciado dice algo muy concreto: por muy grande que sea la cota $M$ que te den, siempre hay un entorno del punto donde la función la supera. Eso es lo que convierte "se va a infinito" en una afirmación verificable.
>
> **Ejemplo:** En $f(x) = 1/x^2$ con $x \to 0$, elige $M = 1000$: basta tomar $\delta = 0.03$ para que $f(x) > 1000$ en todo el entorno, así que el límite es $+\infty$.

> [!warning] 📈 Definición de asíntota vertical
>
> La recta vertical $x = a$ es una **asíntota vertical** de la función $f(x)$ si al menos uno de los siguientes límites es infinito:
>
> - $\lim_{x \to a^+} f(x) = \pm\infty$ (límite lateral derecho),
> - $\lim_{x \to a^-} f(x) = \pm\infty$ (límite lateral izquierdo).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_01.svg]]
>
> **Se lee así:** Entra por la función cerca de $x = a$ y llega a un rombo que pide los **límites laterales**, que se separan en rama derecha e izquierda. Si alguna da infinito, ambas convergen en la **asíntota vertical $x = a$** y de ahí al caso donde la función explota. Si las dos son finitas, se pasa al segundo rombo: si coinciden, el límite existe y la función es continua; si difieren, hay discontinuidad con salto finito.
>
> **Por qué importa:** Distingue los cuatro tipos de asíntota vertical según el comportamiento lateral. Esto te sirve para no afirmar que hay asíntota cuando en realidad el salto es finito.
>
> **Ejemplo:** En $f(x) = (x+1)/(x-2)$ el límite por la izquierda es menos infinito y por la derecha más infinito, así que $x = 2$ es asíntota vertical de tipo IV.

> [!info] 📚 Definición de límite al infinito
>
> Decimos que $\lim_{x \to \infty} f(x) = L$ si para todo $\varepsilon > 0$ existe un número $M > 0$ tal que $$|f(x) - L| < \varepsilon \text{ siempre que } x > M$$
>
> **Tipos de límites al infinito:**
>
> - $\lim_{x \to +\infty} f(x) = L$: límite cuando $x$ tiende a $+\infty$.
> - $\lim_{x \to -\infty} f(x) = L$: límite cuando $x$ tiende a $-\infty$.
> - $\lim_{x \to \infty} f(x) = \infty$: límite infinito.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_03.svg]]
>
> **Se lee así:** Arriba hay un rectángulo con la función y debajo un **rombo de decisión** que pregunta por el límite cuando $x$ tiende a infinito. Del rombo salen tres ramas rotuladas: dos según el tipo de resultado y una tercera para cuando el límite no existe. Las dos primeras bajan a un recuadro de consecuencia (estabilización o crecimiento sin cota) y la tercera a un recuadro con un ejemplo de función.
>
> **Por qué importa:** Fíjate en que el diagrama separa tres resultados que a simple vista se confunden: un valor finito, un crecimiento ilimitado y una oscilación. Esto te evita responder *no existe* cuando en realidad la función se va a infinito, y te obliga a revisar los dos lados antes de concluir.
>
> **Ejemplo:** Con $f(x) = \sin x$ sigues la rama de comportamiento oscilatorio, mientras que con $f(x) = 1/x$ sigues la del límite finito $L = 0$, que da la asíntota horizontal $y = 0$.

> [!tip] 🎯 Definición del límite de una sucesión
>
> Una sucesión $(a_n)$ **converge** al límite $L$ si: $$\forall \varepsilon > 0, \exists N \in \mathbb{N} : n > N \Rightarrow |a_n - L| < \varepsilon$$
>
> **Notación:** $\lim_{n \to \infty} a_n = L$ o $a_n \to L$.
>
> **Interpretación geométrica:** a partir de cierto término $N$, todos los términos de la sucesión están dentro de una "banda" de anchura $2\varepsilon$ alrededor de $L$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_05.svg]]
>
> **Se lee así:** Es una cadena horizontal de rectángulos que representa los **términos de una sucesión** uno tras otro: $a_1$, luego $a_2$, luego $a_3$, un grupo de puntos suspensivos que indica que siguen más términos, y finalmente $a_n$. De ese último rectángulo sale una flecha hacia un rectángulo aparte con el valor $L$, de modo que el diagrama muestra cómo los términos van avanzando hacia el valor buscado.
>
> **Por qué importa:** Fíjate en que $L$ está fuera de la cadena: el límite no es uno de los términos, *es a dónde se acercan*. Esta imagen te ayuda a entender por qué la sucesión se define con una $\varepsilon$ y una $N$.
>
> **Ejemplo:** En la sucesión $a_n = 1/n$ los términos van acercándose al rectángulo $L$ con valor $0$, de modo que $\lim_{n \to \infty} a_n = 0$ y la sucesión es convergente.

> [!warning] 🥪 Definición del teorema del emparedado
>
> Si $(a_n)$, $(b_n)$ y $(c_n)$ son sucesiones tales que:
>
> 1. $a_n \leq b_n \leq c_n$ para todo $n$ suficientemente grande,
> 2. $\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L$,
>
> **entonces** $\lim_{n \to \infty} b_n = L$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_06.svg]]
>
> **Se lee así:** El esquema tiene **tres rectángulos de sucesión** en cadena, unidos por flechas rotuladas con el signo de desigualdad, de modo que el bloque central queda encajonado entre los dos externos. De los tres sale una flecha hacia un mismo rectángulo con el valor $L$, que es el destino común y el único punto de cierre del diagrama.
>
> **Por qué importa:** Fíjate en que las tres sucesiones apuntan al mismo $L$: la garantía no es que la central se acerque, sino que *no tiene dónde esconderse* porque está encajonada entre dos que sí convergen. Esto te da una forma de probar convergencia sin calcular el término general.
>
> **Ejemplo:** Con $a_n = -1/n$, $b_n = \sin(n)/n$ y $c_n = 1/n$, el diagrama muestra que las tres convergen a $0$ y que por eso $\lim_{n \to \infty} \frac{\sin n}{n} = 0$.

---

## 📐 Límites Infinitos en un Punto

> [!warning] ⚠️ Los límites infinitos no existen como números
>
> Cuando escribimos $\lim_{x \to a} f(x) = \infty$, estamos describiendo un **comportamiento específico** de la función, pero técnicamente **el límite no existe** porque infinito no es un número real.
>
> **Notación correcta:**
>
> - $\lim_{x \to a} f(x) = +\infty$ describe un comportamiento concreto.
> - Decir "el límite existe y vale infinito" es incorrecto conceptualmente.

> [!info] 📊 Tabla de comportamientos
>
> |Tipo de límite|Notación|Comportamiento de $f(x)$|Interpretación gráfica|
> |---|---|---|---|
> |Infinito positivo|$\lim_{x \to a} f(x) = +\infty$|Crece sin límite|Asíntota vertical, función sube|
> |Infinito negativo|$\lim_{x \to a} f(x) = -\infty$|Decrece sin límite|Asíntota vertical, función baja|
> |Laterales diferentes|$\lim_{x \to a^+} f(x) = +\infty$ y $\lim_{x \to a^-} f(x) = -\infty$|Comportamientos opuestos|Asíntota vertical con salto|

> [!info] 🎯 Tipos de asíntotas verticales
>
> |Comportamiento|Límites laterales|Ejemplo visual|
> |---|---|---|
> |Tipo I|$\lim_{x \to a^-} f(x) = +\infty$ y $\lim_{x \to a^+} f(x) = +\infty$|Ambos lados suben|
> |Tipo II|$\lim_{x \to a^-} f(x) = -\infty$ y $\lim_{x \to a^+} f(x) = -\infty$|Ambos lados bajan|
> |Tipo III|$\lim_{x \to a^-} f(x) = +\infty$ y $\lim_{x \to a^+} f(x) = -\infty$|Un lado sube, el otro baja|
> |Tipo IV|$\lim_{x \to a^-} f(x) = -\infty$ y $\lim_{x \to a^+} f(x) = +\infty$|Un lado baja, el otro sube|

> [!tip] 🧮 Estrategia para encontrar límites infinitos
>
> **Funciones racionales** $f(x) = \frac{P(x)}{Q(x)}$: si $Q(a) = 0$ pero $P(a) \neq 0$, existe asíntota vertical en $x = a$.
>
> **Proceso de análisis:**
>
> 1. **Factoriza** numerador y denominador.
> 2. **Identifica** los puntos donde el denominador se anula.
> 3. **Evalúa** el signo del numerador en esos puntos.
> 4. **Analiza** el comportamiento lateral del denominador.

> [!warning] 🔍 Método del análisis de signos
>
> Para $f(x) = \frac{P(x)}{Q(x)}$ cerca de $x = a$ donde $Q(a) = 0$:
>
> 1. **Determina** el signo de $P(a)$.
> 2. **Analiza** el signo de $Q(x)$ en los intervalos $(a-\delta, a)$ y $(a, a+\delta)$.
> 3. **Aplica** la regla de signos para cocientes.
>
> |$P(a)$|$Q(x)$ cerca de $a^-$|$Q(x)$ cerca de $a^+$|Límite por izquierda|Límite por derecha|
> |---|---|---|---|---|
> |$+$|$+$|$+$|$+\infty$|$+\infty$|
> |$+$|$+$|$-$|$+\infty$|$-\infty$|
> |$+$|$-$|$+$|$-\infty$|$+\infty$|
> |$+$|$-$|$-$|$-\infty$|$-\infty$|
> |$-$|$+$|$+$|$-\infty$|$-\infty$|
> |$-$|$+$|$-$|$-\infty$|$+\infty$|
> |$-$|$-$|$+$|$+\infty$|$-\infty$|
> |$-$|$-$|$-$|$+\infty$|$+\infty$|
>
> **Por qué importa:** la tabla evita recordar de memoria la regla de signos del cociente: basta leer la fila que corresponde a las dos señales que hayas encontrado.

> [!info] 📝 Ejemplo 1: función racional simple
>
> Encontrar $\lim_{x \to 2} \frac{x+1}{x-2}$.
>
> 1. **Identificar:** $Q(2) = 2-2 = 0$ y $P(2) = 2+1 = 3 > 0$.
> 2. **Analizar signos de $Q(x) = x - 2$:** para $x < 2$ es negativo y para $x > 2$ es positivo.
> 3. **Aplicar la regla de signos:** $\lim_{x \to 2^-} \frac{x+1}{x-2} = -\infty$ y $\lim_{x \to 2^+} \frac{x+1}{x-2} = +\infty$.
> 4. **Conclusión:** $x = 2$ es asíntota vertical tipo IV.

> [!info] 📝 Ejemplo 2: con factorización
>
> Encontrar $\lim_{x \to 3} \frac{x^2-9}{(x-3)^2}$.
>
> 1. **Factorizar:** $\frac{x^2-9}{(x-3)^2} = \frac{(x-3)(x+3)}{(x-3)^2} = \frac{x+3}{x-3}$ para $x \neq 3$.
> 2. **Evaluar:** $\lim_{x \to 3} \frac{x+3}{x-3}$.
> 3. **Analizar:** $P(3) = 6 > 0$ y $Q(x) = x - 3$ cambia de signo en $x = 3$.
> 4. **Resultado:** $\lim_{x \to 3^-} \frac{x+3}{x-3} = -\infty$ y $\lim_{x \to 3^+} \frac{x+3}{x-3} = +\infty$.
>
> **Por qué importa:** el cuadrado en el denominador original hacía pensar que no habría cambio de signo; cancelar primero revela la forma real del problema.

> [!tip] ⚖️ Reglas algebraicas con infinito
>
> |Operación|Resultado|Condición|
> |---|---|---|
> |$\infty + \infty$|$\infty$|Mismo signo|
> |$\infty - \infty$|**Indeterminada**|Requiere análisis especial|
> |$\infty \cdot c$|$+\infty$ si $c > 0$, $-\infty$ si $c < 0$|$c \neq 0$|
> |$\frac{\infty}{\infty}$|**Indeterminada**|Requiere L'Hôpital o factorización|
> |$\frac{c}{\infty}$|$0$|$c$ finito|
> |$\frac{c}{0}$|$\pm\infty$|Depende del signo de $c$ y de la aproximación|

> [!warning] 🚨 Formas indeterminadas relacionadas
>
> Casos que requieren técnicas especiales:
>
> - $\infty - \infty$: factorización o racionalización.
> - $\frac{\infty}{\infty}$: L'Hôpital o comparación de grados.
> - $0 \cdot \infty$: reescribir como cociente.
> - $\frac{0}{0}$ que puede llevar a $\infty$: factorización y simplificación.

> [!info] 🖼️ Selector según el tipo de función
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_02.svg]]
>
> **Se lee así:** El diagrama parte de un límite que podría ser infinito y pasa por un rombo que clasifica el **tipo de función**, con cuatro ramas: la racional, que analiza los ceros del denominador y aplica el método de signos; la exponencial, que evalúa base y exponente; la logarítmica, que verifica el dominio; y la trigonométrica, que identifica discontinuidades y revisa tangente y secante. Las cuatro terminan en el rectángulo de asíntota vertical.
>
> **Por qué importa:** Cada familia de funciones pide un análisis distinto, aunque todas busquen asíntota vertical. Reconocer la categoría evita que apliques el método de signos a una función trigonométrica.
>
> **Ejemplo:** En $f(x) = \ln(x-3)$ revisas el dominio, ves que solo existe para $x > 3$ y concluyes que $x = 3$ es asíntota vertical unilateral.

> [!tip] 🧠 Técnica de estudio "FASE"
>
> - **F**actoriza numerador y denominador.
> - **A**naliza dónde se anula el denominador.
> - **S**ignos: determina el signo en cada lado.
> - **E**valúa el comportamiento lateral.
>
> **Método de estudio activo:** dibuja una tabla con columnas $x$, $P(x)$, $Q(x)$ y $\frac{P(x)}{Q(x)}$, marca los valores críticos, practica cinco ejemplos diarios y visualiza cada función con software gráfico.
>
> **Tarjetas de memorización:** en el anverso, una función con denominador que se anula; en el reverso, la tabla de signos y los límites laterales completos.

---

## 🚀 Límites al Infinito

> [!warning] ⚠️ Cuidado con la notación
>
> - $x \to \infty$ significa que $x$ crece sin límite.
> - $x \to -\infty$ significa que $x$ decrece sin límite.
> - El símbolo $\infty$ **no es un número**: es una notación para expresar comportamiento.

> [!info] 📊 Casos especiales del límite al infinito
>
> |Caso|Notación|Significado|
> |---|---|---|
> |Límite finito|$\lim_{x \to \infty} f(x) = L$|La función se aproxima a un valor $L$|
> |Infinito positivo|$\lim_{x \to \infty} f(x) = +\infty$|La función crece sin límite|
> |Infinito negativo|$\lim_{x \to \infty} f(x) = -\infty$|La función decrece sin límite|
> |No existe|$\lim_{x \to \infty} f(x) = \nexists$|La función oscila o no tiene comportamiento definido|

> [!tip] 📈 Asíntotas horizontales
>
> Una **asíntota horizontal** es una recta horizontal $y = L$ tal que la gráfica de la función se aproxima a esta recta cuando $x \to \pm\infty$.
>
> **Condición:** $y = L$ es asíntota horizontal si $\lim_{x \to +\infty} f(x) = L$ o $\lim_{x \to -\infty} f(x) = L$.

> [!info] 🎯 Interpretación geométrica del comportamiento asintótico
>
> - **Aproximación gradual**: la función se acerca cada vez más a la asíntota.
> - **Nunca se toca**: la función puede acercarse indefinidamente sin tocar la asíntota.
> - **Estabilidad**: para valores grandes de $x$, $f(x) \approx L$.
>
> **Ejemplos visuales:**
>
> - $f(x) = \frac{1}{x}$ tiene asíntota horizontal $y = 0$.
> - $f(x) = e^{-x}$ tiene asíntota horizontal $y = 0$ cuando $x \to +\infty$.
> - $f(x) = \arctan(x)$ tiene asíntotas horizontales $y = \pm\frac{\pi}{2}$.

> [!tip] 🧮 Regla fundamental para funciones racionales
>
> Para una función racional $f(x) = \frac{P(x)}{Q(x)}$ con $$f(x) = \frac{a_n x^n + a_{n-1}x^{n-1} + \cdots + a_0}{b_m x^m + b_{m-1}x^{m-1} + \cdots + b_0}$$
>
> el límite cuando $x \to \infty$ depende de los **grados** de los polinomios:
>
> |Relación de grados|Resultado del límite|Ejemplo|
> |---|---|---|
> |$n < m$ (numerador de menor grado)|$\lim_{x \to \infty} f(x) = 0$|$\frac{x^2}{x^3 + 1} \to 0$|
> |$n = m$ (grados iguales)|$\lim_{x \to \infty} f(x) = \frac{a_n}{b_m}$|$\frac{3x^2 + 1}{2x^2 - 5} \to \frac{3}{2}$|
> |$n > m$ (numerador de mayor grado)|$\lim_{x \to \infty} f(x) = \pm\infty$|$\frac{x^3 + 2}{x^2 - 1} \to \infty$|
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_04.svg]]
>
> **Se lee así:** Parte del cociente de polinomios, se identifican los **grados $n$ y $m$** y un rombo los compara. Si el grado del numerador es menor, el flujo lleva a un rectángulo de límite cero y asíntota horizontal, con la consecuencia de que la función decae a cero. Con grados iguales se obtiene el cociente de coeficientes principales y la función se estabiliza; con grado mayor arriba, el límite es infinito y no hay asíntota horizontal.
>
> **Por qué importa:** Es la regla que resuelve de un vistazo todos los límites al infinito de funciones racionales. Te dice también si la gráfica tendrá o no asíntota horizontal.
>
> **Ejemplo:** Para $\lim_{x \to \infty} \frac{3x^2 - 5x + 2}{2x^2 + x - 1}$ los grados son iguales, así que el límite es $3/2$ y la asíntota horizontal es $y = 3/2$.

> [!warning] 🔍 Método de dividir por la mayor potencia
>
> **Estrategia:**
>
> 1. **Identifica** la mayor potencia de $x$ en el denominador.
> 2. **Divide** numerador y denominador por esa potencia.
> 3. **Evalúa** el límite usando que $\lim_{x \to \infty} \frac{1}{x^k} = 0$ para $k > 0$.
>
> **Ejemplo:** $$\lim_{x \to \infty} \frac{3x^2 - 5x + 2}{2x^2 + x - 1}$$
>
> Dividimos por $x^2$: $$\lim_{x \to \infty} \frac{3 - \frac{5}{x} + \frac{2}{x^2}}{2 + \frac{1}{x} - \frac{1}{x^2}} = \frac{3 - 0 + 0}{2 + 0 - 0} = \frac{3}{2}$$
>
> **Por qué importa:** el método convierte una forma $\frac{\infty}{\infty}$ en un cociente de constantes, sin necesidad de derivar.

> [!info] 🤔 Formas indeterminadas al infinito
>
> |Forma|Ejemplo|Estrategia de resolución|
> |---|---|---|
> |$\frac{\infty}{\infty}$|$\lim_{x \to \infty} \frac{x^2}{x^2 + 1}$|Dividir por la mayor potencia|
> |$\infty - \infty$|$\lim_{x \to \infty} (x^2 - x^2)$|Factorizar o racionalizar|
> |$1^\infty$|$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$|Usar límites exponenciales|

> [!tip] 🧠 Técnica de estudio "GMD"
>
> **G**rado **M**ayor **D**etermina:
>
> - **G**rado mayor arriba (numerador): el límite es infinito.
> - **G**rado mayor abajo (denominador): el límite es cero.
> - **G**rados iguales: el límite es el cociente de los coeficientes principales.
>
> **Método de estudio activo:** practica tres ejemplos diarios de cada tipo, dibuja las gráficas para visualizar el comportamiento y verifica siempre dividiendo por la mayor potencia.

---

## 📊 Límites de Sucesiones

> [!info] 📈 Tipos de comportamiento de una sucesión
>
> |Tipo|Definición|Ejemplo|Comportamiento|
> |---|---|---|---|
> |Convergente|$\lim_{n \to \infty} a_n = L \in \mathbb{R}$|$\frac{1}{n} \to 0$|Se acerca a un valor finito|
> |Divergente a $+\infty$|$\lim_{n \to \infty} a_n = +\infty$|$n^2 \to +\infty$|Crece sin límite|
> |Divergente a $-\infty$|$\lim_{n \to \infty} a_n = -\infty$|$-n \to -\infty$|Decrece sin límite|
> |Oscilante|No tiene límite|$(-1)^n$|Alterna entre valores|
>
> **Mnemotecnia:** *"Converge Cerca, Diverge Distante, Oscila Onda"*.

> [!tip] 🧮 Álgebra de límites de sucesiones
>
> Si $\lim_{n \to \infty} a_n = A$ y $\lim_{n \to \infty} b_n = B$, entonces:
>
> - **Suma:** $\lim_{n \to \infty} (a_n + b_n) = A + B$.
> - **Producto:** $\lim_{n \to \infty} (a_n \cdot b_n) = A \cdot B$.
> - **Cociente:** $\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{A}{B}$, siempre que $B \neq 0$.
> - **Potencia:** $\lim_{n \to \infty} a_n^k = A^k$.
>
> **Formas indeterminadas:** $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \cdot \infty$ y $\infty - \infty$.

> [!info] 🎲 Ejemplos del teorema del emparedado
>
> **Ejemplo 1:** $\lim_{n \to \infty} \frac{\sin n}{n}$.
> Como $-1 \leq \sin n \leq 1$, entonces $-\frac{1}{n} \leq \frac{\sin n}{n} \leq \frac{1}{n}$.
> Dado que $\lim_{n \to \infty} \left(-\frac{1}{n}\right) = \lim_{n \to \infty} \frac{1}{n} = 0$, por el teorema del emparedado $\lim_{n \to \infty} \frac{\sin n}{n} = 0$ ✅.
>
> **Ejemplo 2:** $\lim_{n \to \infty} \frac{1}{n} \cos(n^2)$.
> Como $-1 \leq \cos(n^2) \leq 1$, se tiene $-\frac{1}{n} \leq \frac{\cos(n^2)}{n} \leq \frac{1}{n}$, y el resultado es $0$ ✅.
>
> **Visualización:** la sucesión central está "atrapada" entre dos que convergen al mismo límite.

> [!tip] 🎢 Teorema de convergencia monótona
>
> **Toda sucesión monótona y acotada es convergente.**
>
> **Casos específicos:**
>
> - Creciente y acotada superiormente converge al **supremo**.
> - Decreciente y acotada inferiormente converge al **ínfimo**.
>
> |Tipo|Definición|Convergencia|Ejemplo|
> |---|---|---|---|
> |Monótona creciente|$a_n \leq a_{n+1}$|Converge si acotada superiormente|$a_n = 1 - \frac{1}{n}$|
> |Monótona decreciente|$a_n \geq a_{n+1}$|Converge si acotada inferiormente|$a_n = \frac{1}{n}$|
> |Estrictamente creciente|$a_n < a_{n+1}$|Mismas condiciones|$a_n = n$ (no acotada)|
> |Estrictamente decreciente|$a_n > a_{n+1}$|Mismas condiciones|$a_n = -n$ (no acotada)|

> [!warning] 🔍 Criterios de monotonía
>
> **1. Diferencia de términos consecutivos:**
>
> - Si $a_{n+1} - a_n \geq 0$ la sucesión es creciente.
> - Si $a_{n+1} - a_n \leq 0$ la sucesión es decreciente.
>
> **2. Cociente de términos consecutivos:**
>
> - Si $\frac{a_{n+1}}{a_n} \geq 1$ con $a_n > 0$ es creciente.
> - Si $\frac{a_{n+1}}{a_n} \leq 1$ con $a_n > 0$ es decreciente.
>
> **3. Función asociada:**
>
> - Si $f(x) = a_x$ y $f'(x) \geq 0$ es creciente.
> - Si $f(x) = a_x$ y $f'(x) \leq 0$ es decreciente.

> [!info] 🎯 Ejemplos clásicos de monotonía
>
> **Ejemplo 1: sucesión $a_n = \frac{2n + 1}{n + 3}$.**
> $$a_{n+1} - a_n = \frac{2(n+1) + 1}{(n+1) + 3} - \frac{2n + 1}{n + 3} = \frac{(2n + 3)(n + 3) - (2n + 1)(n + 4)}{(n + 4)(n + 3)} = \frac{5}{(n + 4)(n + 3)} > 0$$
> Es estrictamente creciente. Además $a_n = 2 - \frac{5}{n + 3} < 2$, así que está acotada y converge a $\lim_{n \to \infty} a_n = 2$ ✅.
>
> **Ejemplo 2: sucesión de Fibonacci normalizada.** Con $a_n = \frac{F_{n+1}}{F_n}$, donde $F_n$ es el término $n$-ésimo de Fibonacci, la sucesión converge al **número áureo** $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$.

> [!info] 🖼️ Ruta de decisión para la convergencia
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Límites_al_Infinito_y_Sucesiones_07.svg]]
>
> **Se lee así:** Entra por la sucesión y llega a un rombo que pregunta si es **monótona**; si lo es, un segundo rombo pregunta si está **acotada**, y de las combinaciones sale la convergencia por el teorema monótono o la divergencia. Si no es monótona, se ofrecen dos rutas: el teorema del sandwich o un análisis directo, y la primera vuelve a pasar por un rombo de condiciones antes de confirmar la convergencia.
>
> **Por qué importa:** Te da una ruta de decisión para justificar si una sucesión converge, en vez de adivinar. Sirve especialmente en parciales, donde debes nombrar el teorema que usas.
>
> **Ejemplo:** Para $a_n = (2n+1)/(n+3)$ la diferencia $a_{n+1} - a_n$ es positiva y además $a_n < 2$, así que es monótona y acotada y converge a $2$.

> [!tip] 📚 Estrategia CLIMB para sucesiones
>
> - **C**onvergencia: determina si la sucesión converge.
> - **L**ímite: calcula el valor límite si existe.
> - **I**dentifica: el tipo de sucesión (monótona, oscilante, etc.).
> - **M**étodo: elige la herramienta apropiada (sandwich, monotonía, etc.).
> - **B**ound: verifica las cotas si es necesario.
>
> **Regla mnemotécnica:** *"Monótona Acotada Siempre Converge"*.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 2} \frac{x+1}{x-2}$ por cada lado y clasifica la asíntota vertical.
>
> > [!success]- ✅ Solución
> >
> > El numerador en $x = 2$ vale $3 > 0$ y el denominador cambia de signo: es negativo por la izquierda y positivo por la derecha.
> >
> > Por lo tanto $\lim_{x \to 2^-} \frac{x+1}{x-2} = -\infty$ y $\lim_{x \to 2^+} \frac{x+1}{x-2} = +\infty$.
> >
> > Los dos lados van a infinito con signos opuestos, así que $x = 2$ es una asíntota vertical tipo IV.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 3} \frac{x^2-9}{(x-3)^2}$.
>
> > [!success]- ✅ Solución
> >
> > Sustituir da $\frac{0}{0}$, así que factorizamos: $\frac{(x-3)(x+3)}{(x-3)^2} = \frac{x+3}{x-3}$ para $x \neq 3$.
> >
> > En $x = 3$ el numerador vale $6 > 0$ y el denominador $x - 3$ cambia de signo.
> >
> > Entonces $\lim_{x \to 3^-} \frac{x+3}{x-3} = -\infty$ y $\lim_{x \to 3^+} \frac{x+3}{x-3} = +\infty$; el límite no existe y hay asíntota vertical.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to \infty} \frac{3x^2 - 5x + 2}{2x^2 + x - 1}$ y di si la gráfica tiene asíntota horizontal.
>
> > [!success]- ✅ Solución
> >
> > Los grados del numerador y del denominador son iguales ($n = m = 2$), así que el límite es el cociente de los coeficientes principales: $\frac{3}{2}$.
> >
> > Se verifica dividiendo por $x^2$: $\lim_{x \to \infty} \frac{3 - 5/x + 2/x^2}{2 + 1/x - 1/x^2} = \frac{3}{2}$.
> >
> > Como el límite es finito, la gráfica tiene asíntota horizontal $y = \frac{3}{2}$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to \infty} \frac{x^3 + 2}{x^2 - 1}$ comparando los grados.
>
> > [!success]- ✅ Solución
> >
> > El grado del numerador ($3$) es mayor que el del denominador ($2$), así que el límite es infinito.
> >
> > Dividiendo por $x^2$ queda $\lim_{x \to \infty} \frac{x + 2/x^2}{1 - 1/x^2} = \infty$, porque el numerador crece sin límite y el denominador tiende a $1$.
> >
> > Conclusión: no hay asíntota horizontal y la función crece sin cota.

> [!example] 📋 Planteamiento
>
> Demuestra con el teorema del emparedado que $\lim_{n \to \infty} \frac{\sin n}{n} = 0$.
>
> > [!success]- ✅ Solución
> >
> > Como para todo $n$ se tiene $-1 \leq \sin n \leq 1$, dividiendo entre $n > 0$ obtenemos $-\frac{1}{n} \leq \frac{\sin n}{n} \leq \frac{1}{n}$.
> >
> > Los extremos cumplen $\lim_{n \to \infty} -\frac{1}{n} = 0$ y $\lim_{n \to \infty} \frac{1}{n} = 0$.
> >
> > Como ambas cotas comparten el mismo límite, por el teorema del emparedado $\lim_{n \to \infty} \frac{\sin n}{n} = 0$.

> [!example] 📋 Planteamiento
>
> Decide si $a_n = \frac{2n+1}{n+3}$ converge y, si lo hace, encuentra su límite.
>
> > [!success]- ✅ Solución
> >
> > Calculamos la diferencia: $a_{n+1} - a_n = \frac{5}{(n+4)(n+3)}$, que es siempre positiva, así que la sucesión es creciente.
> >
> > Reescribimos $a_n = 2 - \frac{5}{n+3}$, lo que muestra que $a_n < 2$ para todo $n$: está acotada superiormente.
> >
> > Por el teorema de convergencia monótona, una sucesión creciente y acotada converge. Su límite es $\lim_{n \to \infty} a_n = 2$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Explico la diferencia entre un límite infinito en un punto y un límite al infinito.
> - [ ] Interpreto la $\delta$ del límite infinito y la $\varepsilon$ y la $N$ del límite de una sucesión.
> - [ ] Distingo un límite finito de uno infinito y de uno inexistente en una función racional.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico el análisis de signos para determinar los límites laterales y el tipo de asíntota vertical.
> - [ ] Resuelvo límites al infinito de funciones racionales comparando grados o dividiendo por la mayor potencia.
> - [ ] Verifico la monotonía y la acotación de una sucesión para decidir su convergencia.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro un límite de sucesión con el teorema del emparedado eligiendo cotas adecuadas.
> - [ ] Explico por qué escribir un límite igual a infinito no significa que el límite exista.
> - [ ] Conecto el límite al infinito con la existencia de asíntotas horizontales en la gráfica.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2 y 4: límites al infinito, asíntotas y sucesiones.
> - R. Larson, *Cálculo* (Cengage), cap. 1: límites infinitos y comportamiento asintótico.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 3 y 10: sucesiones, convergencia y teorema del emparedado.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — los $\varepsilon$ y $\delta$ que reaparecen en estas definiciones.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — la herramienta fundamental para el análisis lateral.
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — estudio completo del comportamiento asintótico.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué significa que $\lim_{x \to a} f(x) = +\infty$?::Que por muy grande que sea la cota $M$, siempre hay un entorno de $a$ donde $f(x)$ supera $M$; el límite como número no existe.
> - ¿Cuándo es $x = a$ una asíntota vertical?::Cuando al menos uno de los límites laterales en $a$ es $+\infty$ o $-\infty$.
> - ¿Qué dice la regla de los grados para una racional al infinito?::Si el grado del numerador es menor el límite es $0$; si son iguales es el cociente de coeficientes principales; si es mayor es infinito.
> - ¿Qué condiciones exige el teorema de convergencia monótona?::Que la sucesión sea monótona y que además esté acotada del lado hacia el que crece.
> - ¿Cómo se demuestra que $\sin(n)/n$ tiende a $0$?::Con el emparedado: se acota entre $-1/n$ y $1/n$, dos sucesiones que convergen a $0$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la definición $\varepsilon$-$\delta$ que aquí se adapta al infinito.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — las propiedades operacionales y el emparedado.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — los dos lados que deciden la asíntota vertical.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/02 - Límites Especiales|02 - Límites Especiales]] — exponenciales y logarítmicos en el comportamiento al infinito.
> - [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]] — qué hacer con las formas $\frac{\infty}{\infty}$ y $\infty - \infty$.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — la caracterización por sucesiones de la continuidad.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — donde los límites al infinito se aplican a integrales.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero el análisis de signos hasta que la tabla de cocientes sea automática.
> - Después domina la regla de los grados antes de tocar las formas indeterminadas.
> - Cuando aparezca $\frac{\infty}{\infty}$ o $\infty - \infty$, ve a [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]].
> - En cada problema, escribe antes de calcular **qué teorema vas a usar y por qué se cumplen sus hipótesis**.

---

**Tags:** #MATG1045 #unidad2 #limites-al-infinito-y-sucesiones #limites #limites-infinitos #asintotas-verticales #funciones-racionales #calculo #discontinuidades #comportamiento-asintotico #analisis-signos #infinito #asíntotas #matematicas #comportamiento-asintótico #sucesiones #convergencia #teorema-sandwich #monotonia #analisis-real #acotacion #supremo-infimo

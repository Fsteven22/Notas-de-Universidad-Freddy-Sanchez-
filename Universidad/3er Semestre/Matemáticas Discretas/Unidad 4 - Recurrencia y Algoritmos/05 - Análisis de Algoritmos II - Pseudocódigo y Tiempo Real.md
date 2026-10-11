---
dg-publish: true
---
# ⏱️ Análisis de Algoritmos II — Pseudocódigo y Tiempo Real

## 🎯 Introducción

> [!info] 💡 De qué trata esta nota
> 
> En [[04 - Análisis de Algoritmos I - Fundamentos y Funciones Matemáticas]] obtuvimos $\mathcal{O}$, $\Omega$ y $\Theta$ a partir de una **fórmula $f(n)$ ya dada**. Aquí el punto de partida es distinto: un **algoritmo en seudocódigo** (ver [[03 - Pseudocódigo y Algoritmos]]), y el trabajo consiste en **contar cuántas veces se ejecuta una instrucción clave**, para luego acotar esa cuenta asintóticamente — incluyendo algoritmos recursivos.
> 
> ```mermaid
> graph TD
>     A[Análisis desde Pseudocódigo] --> B[Mejor, peor y caso promedio]
>     A --> C[Contar operaciones en bucles anidados]
>     A --> F[Ramificaciones, cortes y bloques]
>     A --> D[Algoritmos recursivos]
>     A --> E[De Θ a tiempo real]
> ```

---

## 🔵 Tiempos de Ejecución: Mejor, Peor y Promedio Caso

> [!note] 🔵 Definiciones
> 
> Si la entrada de un algoritmo es un [[04 - Cardinalidad y Leyes de Cardinalidad|Cardinalidad]] de $n$ elementos, se dice que el **tamaño de la entrada** es $n$.
> 
> - **Tiempo del mejor caso:** el tiempo _mínimo_ necesario para entradas de tamaño $n$.
> - **Tiempo del peor caso:** el tiempo _máximo_ necesario para entradas de tamaño $n$.
> - **Tiempo del caso promedio:** el tiempo necesario promediado sobre un conjunto finito de entradas, todas de tamaño $n$.

> [!example] 🟢 Ejemplo — búsqueda secuencial
> 
> Encuentra una clave en una [[04 - Sucesiones y Cadenas|sucesión]] ${s_n}$ de $n$ términos:
> 
> ```
> Entrada: clave, n
> Salida: indice (0 si no se encuentra)
> for i = 1 to n{
>     if (clave == si)
>         return i    // búsqueda exitosa
> }
> return 0            // búsqueda no exitosa
> ```
> 
> **Mejor caso:** si $s_1$ es la clave, el condicional se ejecuta $1$ vez → $\Theta(1)$.
> 
> **Peor caso:** si la clave no está, el condicional se ejecuta $n$ veces → $\Theta(n)$.
> 
> **Caso promedio:** si la clave está en la posición $i$, el condicional se ejecuta $i$ veces; si no está, se ejecuta $n$ veces. El promedio es:
> 
> $$f(n) = \frac{(1+2+\cdots+n)+n}{n+1}$$
> 
> Usando $1+2+\cdots+n\leq n^2$ (de la nota anterior):
> 
> $$f(n) \leq \frac{n^2+n}{n+1} = \frac{n(n+1)}{n+1} = n \quad\implies\quad f(n) = \mathcal{O}(n)$$
> 
> Y usando $1+2+\cdots+n \geq \frac{n^2}{4}$:
> 
> $$f(n) \geq \frac{n^2/4+n}{n+1} \geq \frac{n^2/4+n/4}{n+1} = \frac{n}{4} \quad\implies\quad f(n) = \Omega(n)$$
> 
> **Conclusión:** el tiempo del caso promedio es $f(n) = \Theta(n)$.

> [!tip] 💡 De dónde salen $n^2$ y $n^2/4$
> 
> Ambas cotas de $1+2+\cdots+n$ vienen de tratar la suma como un polinomio en $n$ (exactamente el trabajo de la nota anterior), no de una fórmula nueva:
> 
> - La suma exacta es $\frac{n(n+1)}{2}$, que es $\Theta(n^2)$ por el atajo de polinomios ([[01 - Grafos I - Conceptos Básicos y Recorridos|grado]] 2, coeficiente líder $\frac12$).
> - $1+2+\cdots+n\leq n^2$: cada uno de los $n$ términos es a lo sumo $n$, así que la suma completa es a lo sumo $n\cdot n=n^2$ — el mismo truco de "homogeneizar" de la nota anterior, pero aplicado término a término en vez de a una fórmula cerrada.
> - $1+2+\cdots+n\geq n^2/4$: al menos la mitad de los términos (del $\lceil n/2\rceil$ al $n$) valen $\geq n/2$, así que la suma es al menos $\frac{n}{2}\cdot\frac{n}{2}=\frac{n^2}{4}$.
> 
> Una vez que tienes $f(n)$ acotada entre $\frac{n}{4}$ y $n$, la conclusión $\Theta(n)$ es directa — es la misma "receta de sándwich" de siempre, solo que aquí los límites vienen de acotar una suma en vez de despejar un polinomio.

> [!tip] 📌 Observación — de una fórmula de tiempo a Θ
> 
> Si se sabe que un algoritmo toma $60n^2+5n+1$ unidades de tiempo en el peor caso, y ya se demostró (nota anterior) que $60n^2+5n+1=\Theta(n^2)$, entonces el tiempo del peor caso de ese algoritmo es directamente $\Theta(n^2)$ — no hace falta reanalizar la fórmula, solo aplicar el resultado ya probado.

---

## 🟡 Contando Operaciones en Bucles Anidados

> [!example] 🟢 Ejemplo I — bucles anidados simples
> 
> ```
> for i = 1 to n
>     for j = 1 to i
>         x = x + 1
> ```
> 
> Cuando $i=1$, la línea interna se ejecuta $1$ vez; cuando $i=2$, $2$ veces; y así sucesivamente. En total:
> 
> $$f(n) = 1+2+\cdots+n = \Theta(n^2)$$

> [!example] 🟢 Ejemplo II — `while` que divide entre 2, con `for` interno de tamaño $j$
> 
> ```
> j = n
> while (j ≥ 1){
>     for i = 1 to j
>         x = x + 1
>     j = ⌊j/2⌋
> }
> ```
> 
> Sea $t(n)$ el número de veces que se ejecuta `x = x + 1`.
> 
> **Cota inferior:** la primera vez que se entra al `while`, la instrucción ya se ejecuta $n$ veces → $t(n)\geq n,\ \forall n\geq1$, es decir $t(n)=\Omega(n)$.
> 
> **Cota superior:** si $k$ es el número de iteraciones del `while`, el total de ejecuciones es a lo sumo la suma geométrica
> 
> $$n+\frac{n}{2}+\frac{n}{4}+\cdots+\frac{n}{2^{k-1}} = n\left(\frac{1-(1/2)^k}{1-1/2}\right) = 2n\left(1-\frac{1}{2^k}\right) \leq 2n$$
> 
> Entonces $t(n)\leq 2n,\ \forall n\in\mathbb{N}$, es decir $t(n)=\mathcal{O}(n)$.
> 
> **Conclusión:** $t(n) = \Theta(n)$.

> [!example] 🟢 Ejemplo III — mismo `while`, pero el ciclo interno corre de $1$ a $n$ (no a $j$)
> 
> ```
> i = n
> while (i ≥ 1){
>     for j = 1 to n
>         x = x + 1
>     i = ⌊i/2⌋
> }
> ```
> 
> Aquí el ciclo interno siempre corre $n$ veces, así que lo que cambia es **cuántas veces se entra al `while`**. Se demuestra por inducción que si $2^{k-1}\leq n < 2^k$, entonces $t(n) = kn$.
> 
> **Paso base:** para $1\leq n<2$ ($k=1$), se entra una sola vez → $t(n)=n=1\cdot n$. Para $2\leq n<4$ ($k=2$), se entra dos veces → $t(n)=2n$.
> 
> **Paso inductivo:** si $2^{k}\leq n<2^{k+1}$, se entra una vez con $i=n$ (ejecutando la instrucción $n$ veces), luego $i=\lfloor n/2\rfloor$ cae en el rango $2^{k-1}\leq i<2^k$, y por hipótesis inductiva el resto ejecuta $kn$ veces más. En total $t(n)=n+kn=(k+1)n$, que es exactamente la fórmula para el rango $2^k\leq n<2^{k+1}$.
> 
> **De la [[02 - Relaciones|relación]] con $k$ a Θ(n log n):** de $2^{k-1}\leq n<2^k$ se sigue $k-1\leq \log n<k$, y para $n\geq2$ ($\log n\geq1$):
> 
> $$n\log n < nk \leq 2n\log n, \quad \forall n\geq2$$
> 
> **Conclusión:** $t(n) = \Theta(n\log n)$.

> [!tip] 💡 Los dos saltos lógicos del Ejemplo III
> 
> **① Por qué la inducción prueba $t(n)=kn$ y no solo lo sugiere:**
> 
> La hipótesis inductiva no es "sobre $n$" en el sentido usual, sino sobre el **rango** $[2^{k-1},2^k)$ en el que cae $n$: se asume que la fórmula ya vale para todo valor en el rango anterior $[2^{k-1},2^k)$, y se demuestra para el siguiente rango $[2^k,2^{k+1})$. Cada `while` gasta $n$ operaciones (el `for` interno, que siempre corre hasta $n$) y luego reduce la variable de control a $\lfloor n/2\rfloor$, que por construcción cae exactamente en el rango anterior — de ahí que el resto del trabajo, por hipótesis, sea $kn$. Sumando el gasto de esta iteración ($n$) más el resto ($kn$) da $(k+1)n$, que es la fórmula del rango siguiente. Es inducción "por rangos de potencias de 2", una variante común cuando el algoritmo divide entre 2 en cada paso.
> 
> **② Por qué $k=\Theta(\log n)$ y no solo "$k$ está relacionado con $\log n$":**
> 
> De $2^{k-1}\leq n<2^k$ se aplica $\log$ (creciente, preserva las desigualdades) a los tres lados: $k-1\leq\log n<k$. Esto encierra a $k$ entre $\log n$ y $\log n+1$ — una diferencia de **como mucho 1**, sin importar qué tan grande sea $n$ (el mismo tipo de argumento que el lema del piso de la nota anterior). Multiplicando por $n$ y usando $\log n\geq1$ (válido para $n\geq2$) para poder comparar $\log n$ y $\log n+1$ con múltiplos simples de $\log n$: $$n\log n < nk \leq n(\log n+1) \leq n\log n+n\log n = 2n\log n$$ (la última desigualdad usa $n\leq n\log n$ para $n\geq2$). De ahí sale directamente el sándwich $n\log n<t(n)\leq2n\log n$, es decir $\Theta(n\log n)$ — sin necesidad de adivinar la constante, sale sola del álgebra.

> [!example] 🟢 Ejemplo IV — `for` anidado con límite $\lfloor i/2\rfloor$
> 
> ```
> for i = 1 to n
>     for j = 1 to ⌊i/2⌋
>         x = x + 1
> ```
> 
> Estudiando los primeros valores: $t(1)=0$, $t(2)=1$, $t(3)=1+1$, $t(4)=1+1+2,\dots$ Por inducción se obtiene la fórmula cerrada:
> 
> $$t(2k) = k^2, \qquad t(2k+1) = k(k+1), \quad \forall k\in\mathbb{N}$$
> 
> **Cota superior:** si $n=2k+1$ (impar), $t(n)=\left(\frac{n-1}{2}\right)\left(\frac{n+1}{2}\right) \leq \left(\frac{n+1}{2}\right)^2 \leq n^2$; si $n=2k$ (par), $t(n)=\frac{n^2}{4}\leq\frac{(n+1)^2}{4}$. En ambos casos $t(n)\leq n^2,\ \forall n$ → $t(n)=\mathcal{O}(n^2)$.
> 
> **Cota inferior:** de forma análoga, $t(n)\geq\frac{(n-1)^2}{4},\ \forall n$. Para $n\geq2$, $n-1\geq n/2$, así que $t(n)\geq n^2/16$ → $t(n)=\Omega(n^2)$.
> 
> **Conclusión:** $t(n) = \Theta(n^2)$.

> [!tip] 💡 Por qué la cota se separa en par/impar
> 
> La fórmula cerrada de $t(n)$ no es una sola expresión en $n$ — depende de si $n$ es par o impar ($t(2k)=k^2$ vs $t(2k+1)=k(k+1)$), porque el límite del ciclo interno es $\lfloor i/2\rfloor$, que redondea distinto según la paridad de $i$. Por eso la prueba revisa ambos casos por separado en vez de una sola cadena de desigualdades como en los ejemplos anteriores — pero el objetivo es el mismo: en cada caso, acotar la fórmula cerrada (en términos de $k$) por arriba y por abajo con expresiones en $n=2k$ o $n=2k+1$, y verificar que ambas caen en $\Theta(n^2)$.
> 
> El truco algebraico central es reemplazar $k$ por $n$ usando $k\approx n/2$ en ambas direcciones (p. ej. $\left(\frac{n+1}{2}\right)^2\leq n^2$ para la cota superior, y $n-1\geq n/2$ para $n\geq2$ en la cota inferior) — exactamente el mismo tipo de "homogeneizar" de la nota anterior, solo que aplicado a una fórmula cerrada en $k$ en vez de a un polinomio en $n$ directamente.

---

## 🎓 Generalizando: Cuando la Variable Que Se Reduce No Arranca en $n$

> [!info] 💡 El problema que resuelve esta sección
> 
> En los Ejemplos II y III, la variable que se divide entre 2 arrancaba exactamente en $n$. En los talleres es común que arranque en otra expresión que depende de $n$ — como $\lfloor 7\sqrt{n}\rfloor$ o $\lfloor\log(5n)\rfloor$. La buena noticia: **el método es el mismo**, usando el lema del piso ($\lfloor x\rfloor=\Theta(x)$, ver [[04 - Análisis de Algoritmos I - Fundamentos y Funciones Matemáticas]]) para reemplazar la expresión inicial por algo más simple.
> 
> Lo único que hay que identificar es **cuál de los tres patrones** aplica:
> 
> |Patrón|¿Cómo es el ciclo interno?|Resultado|
> |---|---|---|
> |**Patrón A** (como el Ejemplo III)|Corre un rango **fijo**, independiente de la variable que se reduce|$t(n) = (\text{rango fijo})\times\log(\text{valor inicial})$|
> |**Patrón B** (como el Ejemplo II)|Corre **hasta la misma variable** que se está reduciendo|$t(n) = \Theta(\text{valor inicial})$ (suma geométrica)|
> |**Patrón C** (nuevo)|**No hay** ciclo interno — solo una instrucción suelta dentro del `while`|$t(n) = \Theta(\log(\text{valor inicial}))$ (el número de iteraciones del `while`, sin multiplicar por nada)|

> [!example] 🟢 Ejemplo — Patrón A con valor inicial $\lfloor7\sqrt{n}\rfloor$ (Taller III, ejercicio 2)
> 
> ```
> i = ⌊7√n⌋
> while (i ≥ 1){
>     for j = 1 to n
>         x = x + 1
>     i = ⌊i/2⌋
> }
> ```
> 
> El ciclo interno siempre corre $n$ veces (rango fijo, no depende de $i$) → **Patrón A**. Sea $V=\lfloor7\sqrt{n}\rfloor$.
> 
> **Paso 1 — simplificar $V$ con el lema del piso:** de $x-1<\lfloor x\rfloor\leq x$ con $x=7\sqrt{n}$, para $n\geq1$ se tiene $7\sqrt{n}-1\geq6\sqrt{n}$ (pues $\sqrt n\ge 1$), así que
> 
> $$6\sqrt{n} < V \leq 7\sqrt{n} \quad\implies\quad V=\Theta(\sqrt{n})$$
> 
> **Paso 2 — contar iteraciones del `while`:** igual que en el Ejemplo III, si $2^{k-1}\leq V<2^k$ entonces $t(n)=kn$, con $k=\Theta(\log V)$.
> 
> **Paso 3 — traducir $\log V$ a $\log n$:** como $V=\Theta(\sqrt n)$, $\log V = \Theta(\log\sqrt{n}) = \Theta\left(\tfrac{1}{2}\log n\right) = \Theta(\log n)$.
> 
> **Conclusión:** $t(n) = kn = \Theta(n)\cdot\Theta(\log n) = \Theta(n\log n)$.

> [!example] 🟢 Ejemplo — Patrón B con valor inicial $\lfloor\log(5n)\rfloor$ (Taller III, ejercicio 3)
> 
> ```
> k = ⌊log(5n)⌋
> while (k ≥ 1){
>     for i = 1 to k
>         x = x + 1
>     k = ⌊k/2⌋
> }
> ```
> 
> Aquí el ciclo interno corre **hasta $k$**, la misma variable que se reduce → **Patrón B** (igual que el Ejemplo II, pero con $k_0=\lfloor\log(5n)\rfloor$ en vez de $n$).
> 
> **Paso 1 — simplificar $k_0$ con el lema del piso:** con $x=\log(5n)=\log5+\log n$,
> 
> $$\log(5n)-1 < k_0 \leq \log(5n) \quad\implies\quad k_0=\Theta(\log n)$$
> 
> (ya que $\log5$ es una constante, y $\log5+\log n=\Theta(\log n)$).
> 
> **Paso 2 — suma geométrica (Patrón B):** igual que en el Ejemplo II, el total de operaciones es a lo sumo $k_0+\frac{k_0}{2}+\frac{k_0}{4}+\cdots\leq 2k_0$, y al menos $k_0$ (la primera iteración ya aporta $k_0$). Entonces $t(n)=\Theta(k_0)$.
> 
> **Conclusión:** $t(n) = \Theta(k_0) = \Theta(\log n)$.

> [!example] 🟢 Ejemplo — Patrón C con valor inicial $3n^2$ (Lección III, ejercicio 4)
> 
> ```
> i = 3n²
> while (i ≥ 1){
>     x = x + 1
>     i = ⌊i/2⌋
> }
> ```
> 
> Aquí no hay ningún `for` — el cuerpo del `while` es una sola instrucción suelta. Eso significa que **cada vez que se entra al `while`, se ejecuta exactamente una operación**, así que el total de operaciones **es** el número de veces que se entra al `while`, sin ningún ciclo interno que multiplique.
> 
> **Paso 1 — el valor inicial:** $V=3n^2$ (ya es un entero, no hace falta el lema del piso aquí).
> 
> **Paso 2 — contar iteraciones:** igual que en los otros patrones, si $2^{k-1}\leq V<2^k$, se entra al `while` exactamente $k$ veces, con $k=\Theta(\log V)$.
> 
> **Paso 3 — traducir a $\log n$:** como $3n^2$ es una potencia de $n$ (con constante y exponente), $\log(3n^2)=\Theta(\log n)$.
> 
> **Conclusión:** $t(n) = k = \Theta(\log n)$.
> 
> > [!tip]- 💡 Comparación directa: por qué el Patrón C es "más simple" que A y B
> > 
> > En A y B, el `for` interno **multiplica** el trabajo de cada iteración del `while` — por eso A termina con un producto ($\text{rango}\times\log V$) y B con una suma geométrica que colapsa al valor inicial. En C no hay nada que multiplicar: cada iteración del `while` cuesta $\Theta(1)$, así que el total es literalmente "cuántas veces entré al `while`" — ni más ni menos. Es el caso más simple de los tres, y suele aparecer cuando el ejercicio quiere probar que entiendes que $\log$ es, en el fondo, "cuántas veces puedo dividir esto entre 2".

> [!tip] 💡 Receta resumida (actualizada con los tres patrones)
> 
> 1. Identifica el valor inicial $V(n)$ de la variable que se divide entre 2, y simplifícalo con el lema del piso si hace falta (ignora el $\lfloor\cdot\rfloor$, trabaja directo con lo de adentro).
> 2. Mira qué hace el cuerpo del `while`:
>    - ¿Hay un `for` que depende de esa misma variable? → **Patrón B**, $t(n)=\Theta(V(n))$.
>    - ¿Hay un `for` con un rango fijo (no depende de la variable)? → **Patrón A**, $t(n)=(\text{rango})\times\Theta(\log V(n))$.
>    - ¿No hay `for`, solo una instrucción suelta? → **Patrón C**, $t(n)=\Theta(\log V(n))$.
> 3. Si necesitas $\log V(n)$ (patrones A o C), recuerda: si $V(n)$ es $n$ o una potencia/raíz de $n$, $\log V(n)=\Theta(\log n)$; si $V(n)$ ya es del tipo $\log n$, ese paso no aplica — $V(n)$ mismo ya es $\Theta(\log n)$.

---

## 🔀 Ramificaciones, Cortes Anticipados y Bloques Combinados

> [!info] 💡 De qué trata esta sección
> 
> Hasta ahora cada ejemplo tenía una sola estructura (un ciclo, o un `while` que se reduce). Aquí se combinan piezas: `if`/`else` anidados, ciclos que terminan antes de tiempo (`return`), y varios bloques distintos uno tras otro — el tipo de algoritmo "integrador" que junta todo lo anterior en un solo ejercicio.

### `if`/`else` anidados

> [!note] 📋 La regla: solo se ejecuta una rama, nunca ambas
> 
> A diferencia de los bloques secuenciales (que se suman), en una ramificación **nunca se suman las dos ramas** — el algoritmo elige una y ejecuta solo esa. Para el peor caso, te quedas con la rama más cara en cada nivel; para el mejor caso, con la más barata.

> [!example] 🟢 Ejemplo — dos niveles de `if`/`else`
> 
> ```
> if (cond1):
>     if (cond2):
>         for i = 1 to n
>             for j = 1 to n
>                 x = x + 1        // Θ(n²)
>     else:
>         for i = 1 to n
>             x = x + 1            // Θ(n)
> else:
>     x = x + 1                     // Θ(1)
> ```
> 
> El [[04 - Árboles I - Conceptos Básicos y Árboles de Expansión|árbol]] de posibilidades tiene tres hojas: $\Theta(n^2)$, $\Theta(n)$, $\Theta(1)$. **Peor caso:** la hoja más cara → $\mathcal{O}(n^2)$. **Mejor caso:** la hoja más barata → $\Omega(1)$. No hay una única $\Theta$ para "el algoritmo en general" a menos que se especifique de qué caso se habla — igual que con la búsqueda secuencial al inicio de esta nota.

### Cortes anticipados (`return` dentro de ciclos anidados)

> [!example] 🟢 Ejemplo — buscar un par repetido
> 
> ```
> for i = 1 to n:
>     for j = 1 to n:
>         if (a[i] == a[j]):
>             return verdadero
> return falso
> ```
> 
> **Mejor caso:** los dos primeros elementos ya coinciden → una sola comparación → $\Theta(1)$.
> 
> **Peor caso:** nunca hay coincidencia → se recorre el doble ciclo completo → $\Theta(n^2)$ (regla del producto de siempre, sin ningún corte).
> 
> El `return` no cambia **cómo** se analiza el ciclo anidado — sigue siendo la regla del producto para el peor caso. Solo agranda la brecha posible entre mejor y peor caso: cuanto más adentro esté el `return` respecto a los ciclos, más grande esa brecha.

### Varios bloques secuenciales, incluyendo uno recursivo

> [!note] 📋 La regla de la suma, con más de dos piezas
> 
> $$\mathcal{O}(f_1(n)) + \mathcal{O}(f_2(n)) + \cdots + \mathcal{O}(f_k(n)) = \mathcal{O}\big(\max(f_1(n),\ldots,f_k(n))\big)$$
> 
> Si uno de los bloques es una llamada recursiva, primero se obtiene su complejidad con las herramientas de la sección "Algoritmos Recursivos" (desenrollando, o por niveles) — y **después** se suma como cualquier otro bloque.

> [!example] 🟢 Ejemplo integrador — tres bloques distintos en secuencia
> 
> ```
> for i = 1 to n
>     x = x + 1                    // Bloque 1: Θ(n)
> 
> if (n > 10):
>     for i = 1 to n
>         for j = 1 to n
>             x = x + 1             // Bloque 2 (peor caso): Θ(n²)
> else:
>     x = x + 1                     // Bloque 2 (mejor caso): Θ(1)
> 
> for i = 1 to log(n)
>     x = x + 1                    // Bloque 3: Θ(log n)
> ```
> 
> **Peor caso de cada bloque:** $\Theta(n)$, $\mathcal{O}(n^2)$, $\Theta(\log n)$. Sumando y quedándose con el que domina:
> 
> $$\Theta(n) + \mathcal{O}(n^2) + \Theta(\log n) = \mathcal{O}(n^2)$$

### 🪤 Casos trampa: cuando la comparación visual engaña

> [!warning] ⚠️ Regla para no caer
> 
> **Cualquier potencia positiva de $n$ le gana a cualquier potencia de $\log n$**, sin importar qué tan chica sea esa potencia: $\log n = o(n^\varepsilon)$ para todo $\varepsilon>0$ (la notación $o$ minúscula significa "crece estrictamente más despacio que"). La trampa más común es comparar $n\log n$ contra $n^{1{,}5}$ — visualmente parecen similares, pero:
> 
> $$n^{1{,}5} = n\cdot n^{0{,}5} \qquad\text{mientras que}\qquad n\log n = n\cdot\log n$$
> 
> Como $\log n$ pierde contra **cualquier** raíz (por chiquita que sea), $n\log n = o(n^{1{,}5})$ — $n^{1{,}5}$ gana, aunque no sea obvio a simple vista.

> [!example] 🟢 Ejemplo con trampa incluida
> 
> ```
> for i=1 to n: for j=1 to n: x=x+1              // Θ(n²)
> mergesort(arr, n)                                // Θ(n log n)
> for i=1 to n: for j=1 to sqrt(n): x=x+1         // Θ(n^1.5)
> ```
> 
> Tres bloques: $n^2$, $n\log n$, $n^{1{,}5}$. Ordenando de mayor a menor: $n^2 > n^{1{,}5} > n\log n$ (el $n^2$ le gana a cualquier potencia menor, y $n^{1{,}5}$ le gana a $n\log n$ por la regla de arriba). Resultado final, sin caer en la trampa: $\Theta(n^2)$.

---

## 🔴 Algoritmos Recursivos y su Análisis

> [!note] 🔴 Definición
> 
> Una **[[01 - Funciones|función]] recursiva** es una función que se invoca a sí misma. Un **algoritmo recursivo** es aquel que contiene una función recursiva.

> [!example] 🟢 Ejemplo — factorial y su correctitud
> 
> Por definición, $n! = n(n-1)!,\ \forall n\geq1$, con $0!=1$ — es decir, $f(n)=n!$ se puede definir recursivamente:
> 
> ```
> Entrada: un entero n ≥ 0
> Salida: n!
> factorial(n){
>     if (n == 0)
>         return 1
>     return n * factorial(n - 1)
> }
> ```
> 
> **Demostración de correctitud (inducción en $n$):**
> 
> - _Paso base:_ para $n=0$, el algoritmo regresa $1=0!$. ✅
> - _Paso inductivo:_ si $\text{factorial}(n-1)=(n-1)!$ (hipótesis), entonces para $n\neq0$: $\text{factorial}(n)=n\cdot\text{factorial}(n-1)=n\cdot(n-1)!=n!$. ✅
> 
> Por inducción, $\text{factorial}(n)=n!$ para todo $n\geq0$. $\blacksquare$

> [!example] 🟢 Ejemplo — la caminata del robot (conexión con Fibonacci)
> 
> Un robot da pasos de $1$ o $2$ metros. Sea $walk(n)$ el número de formas de caminar $n$ metros. Si el primer paso es de $1$ metro, quedan $walk(n-1)$ formas de completar el resto; si es de $2$ metros, quedan $walk(n-2)$. Por el principio de la suma:
> 
> $$walk(n) = walk(n-1)+walk(n-2), \qquad walk(1)=1,\ walk(2)=2$$
> 
> ```
> Entrada: n
> Salida: walk(n)
> caminatas(n){
>     if (n == 1 ∨ n == 2)
>         return n
>     return caminatas(n - 1) + caminatas(n - 2)
> }
> ```
> 
> Los primeros términos son $1,2,3,5,8,13,\dots$ — la misma recurrencia que la [[01 - Relaciones de Recurrencia|sucesión de Fibonacci]] $f_n=f_{n-1}+f_{n-2}$, solo desfasada: $walk(1)=f_2,\ walk(2)=f_3,\ walk(n)=f_{n+1}$ para todo $n\geq1$ (se prueba por inducción fuerte).

---

## 🎯 Ejercicio Extra — Tiempo de Ejecución de Algoritmos Recursivos

> [!question] 📋 Por qué esta sección
> 
> Los dos ejemplos de arriba (factorial y la caminata del robot) solo demuestran **correctitud**: que el algoritmo calcula lo que dice calcular. No dicen nada sobre **cuánto tarda**. Para eso hace falta plantear una relación de recurrencia distinta — una para el **tiempo** $T(n)$, no para el resultado — y resolverla "desenrollándola" (sustituyendo repetidamente hasta encontrar el patrón). Es el mismo espíritu de las secciones anteriores (contar operaciones, reconocer si el patrón es A o B), aplicado ahora a llamadas recursivas en vez de iteraciones de un `while`. Para la versión formal de resolver recurrencias ([[02 - Recurrencia Homogénea|ecuación característica]], etc.), ver [[01 - Relaciones de Recurrencia]].

> [!tip] 📌 El método: desenrollar la recurrencia
> 
> 1. Plantea $T(n)$ = (trabajo local de esa llamada) + (tiempo de la o las llamadas recursivas).
> 2. Sustituye $T(n-1)$ (o $T(n/2)$, etc.) por su propia definición, y otra vez, y otra vez — hasta ver el patrón en función del número de sustituciones $k$.
> 3. Encuentra el $k$ en el que se llega al caso base, y sustitúyelo de vuelta.
> 4. El resultado es una fórmula cerrada para $T(n)$; conviértela a $\Theta$ con las mismas herramientas de siempre.

> [!success] ✅ (a) Recursión lineal — $\text{factorial}(n)$: $T(n)=T(n-1)+c,\ T(0)=c \implies \Theta(n)$
> 
> Cada llamada hace trabajo constante ($c$: la multiplicación y la comparación) más **una** llamada recursiva sobre $n-1$. Desenrollando: $$T(n) = T(n-1)+c = T(n-2)+2c = T(n-3)+3c = \cdots = T(n-k)+kc$$ Se llega al caso base cuando $n-k=0$, es decir $k=n$: $$T(n) = T(0)+nc = c+nc = (n+1)c$$ → $T(n)=\Theta(n)$: una sola cadena de $n$ llamadas, cada una con trabajo constante, es asintóticamente igual a un solo `for` de $n$ iteraciones (Ejemplo I de esta nota).

> [!success] ✅ (b) Recursión que se divide entre 2 — búsqueda binaria: $T(n)=T(\lfloor n/2\rfloor)+c,\ T(1)=c \implies \Theta(\log n)$
> 
> ```
> buscar(n){
>     if (n <= 1) return c
>     return c + buscar(⌊n/2⌋)
> }
> ```
> 
> Por el lema del piso (nota anterior), $\lfloor n/2\rfloor=\Theta(n/2)$, así que para el análisis asintótico se puede trabajar directamente con $n/2$. Desenrollando: $$T(n) = T(n/2)+c = T(n/4)+2c = T(n/8)+3c = \cdots = T(n/2^k)+kc$$ Se llega al caso base cuando $n/2^k=1$, es decir $k=\log n$: $$T(n) = T(1)+c\log n = c+c\log n$$ → $T(n)=\Theta(\log n)$. Nótese el paralelo exacto con el Patrón B de la sección anterior: "dividir entre 2 y trabajar $\Theta(1)$ en cada nivel" da $\Theta(\log(\text{valor inicial}))$, sea eso una iteración de `while` o una llamada recursiva.

> [!success] ✅ (c) Doble recursión — $\text{caminatas}(n)$: $T(n)=T(n-1)+T(n-2)+c \implies$ exponencial, **no** $\Theta(n)$
> 
> A diferencia de (a) y (b), aquí cada llamada se **ramifica en dos**, así que desenrollar no da una sola cadena — da un árbol que se duplica en cada nivel. No hace falta la fórmula exacta (eso requiere la ecuación característica de [[01 - Relaciones de Recurrencia]]) para ver que es exponencial:
> 
> **Cota superior fácil:** como $T$ es creciente, $T(n-2)\leq T(n-1)$, así que $T(n)\leq2T(n-1)+c$. Desenrollando esta versión (más floja pero más simple): $$T(n) \leq 2T(n-1)+c \leq 4T(n-2)+3c \leq \cdots \leq 2^nT(0)+(2^n-1)c$$ → $T(n)=\mathcal{O}(2^n)$.
> 
> **Cota inferior fácil:** como $T(n-1)\geq T(n-2)$, también $T(n)\geq2T(n-2)+c$ — esto desenrolla de $2$ en $2$ en $n$: $$T(n) \geq 2T(n-2)+c \geq 4T(n-4)+3c \geq \cdots \geq 2^{n/2}T(0)+\cdots$$ → $T(n)=\Omega!\left(2^{n/2}\right) = \Omega!\left((\sqrt2)^n\right)$.
> 
> **Conclusión:** $T(n)$ queda atrapado entre dos exponenciales, $(\sqrt2)^n$ y $2^n$ — genuinamente exponencial, no lineal ni logarítmico (el valor exacto es $\Theta(\varphi^n)$ con $\varphi\approx1{,}618$, la razón áurea, resolviendo la recurrencia formalmente). Esta es la razón concreta detrás de la tabla de "Por qué importa" más abajo: cada llamada extra que se ramifica duplica aproximadamente el trabajo, y eso se vuelve impracticable mucho antes que cualquier $\Theta(n^k)$.

> [!success] ✅ (d) Divide y vencerás con [[05 - Permutaciones y Combinaciones|combinación]] lineal — estilo _merge sort_: $T(n)=2T(n/2)+n,\ T(1)=c \implies \Theta(n\log n)$
> 
> ```
> combinar(n){
>     if (n <= 1) return c
>     return combinar(⌊n/2⌋) + combinar(⌊n/2⌋) + n
> }
> ```
> 
> Aquí también hay dos llamadas recursivas (como en el caso c), pero con una diferencia clave: el trabajo local **no es constante**, es $n$ (por ejemplo, combinar dos mitades ordenadas). Conviene pensar por **niveles del árbol de recursión** en vez de desenrollar término a término:
> 
> |Nivel|Nº de subproblemas|Tamaño de cada uno|Trabajo local por subproblema|Trabajo total del nivel|
> |---|---|---|---|---|
> |$0$|$1$|$n$|$n$|$n$|
> |$1$|$2$|$n/2$|$n/2$|$2\cdot\frac{n}{2}=n$|
> |$2$|$4$|$n/4$|$n/4$|$4\cdot\frac{n}{4}=n$|
> |$i$|$2^i$|$n/2^i$|$n/2^i$|$2^i\cdot\frac{n}{2^i}=n$|
> 
> Cada nivel aporta exactamente $n$ de trabajo (los subproblemas se duplican, pero cada uno hace la mitad de trabajo — se cancela). El árbol tiene $\log n$ niveles, igual que en (b), porque el tamaño se divide entre 2 en cada nivel hasta llegar a $1$. Sumando el trabajo de los $\log n$ niveles: $$T(n) \approx n\cdot\log n \implies T(n)=\Theta(n\log n)$$
> 
> Este es el mismo resultado que el Ejemplo III de esta nota ($t(n)=\Theta(n\log n)$ para el `while` con `for` interno de tamaño fijo) — no es casualidad: "$\log n$ niveles/iteraciones, cada uno con $\Theta(n)$ de trabajo" es el mismo patrón, ya sea con recursión o con un ciclo.
> 
> > [!tip]- 💡 Tabla resumen: las cuatro formas de recursión de esta sección
> > 
> > |Recurrencia|Llamadas por nivel|Trabajo local|Resultado|Ejemplo|
> > |---|---|---|---|---|
> > |$T(n)=T(n-1)+c$|1|$\Theta(1)$|$\Theta(n)$|factorial (a)|
> > |$T(n)=T(n/2)+c$|1|$\Theta(1)$|$\Theta(\log n)$|búsqueda binaria (b)|
> > |$T(n)=2T(n-1)+c$|2 (misma escala)|$\Theta(1)$|exponencial|caminatas/Fibonacci (c)|
> > |$T(n)=2T(n/2)+n$|2 (mitad de tamaño)|$\Theta(n)$|$\Theta(n\log n)$|estilo _merge sort_ (d)|
> > 
> > La diferencia entre (c) y (d) es la que más se presta a confusión: ambas tienen dos llamadas recursivas, pero (c) las hace sobre **casi el mismo tamaño** ($n-1$ y $n-2$), lo cual dispara el número de llamadas exponencialmente; (d) las hace sobre **la mitad del tamaño** ($n/2$), lo cual mantiene el trabajo por nivel constante en $n$ y da solo $\log n$ niveles.

---

## 📊 De la Notación Asintótica al Tiempo Real

> [!note] 📋 Número de operaciones según Θ, para distintos $n$
> 
> |Complejidad|$n=10$|$n=100$|$n=1000$|
> |---|---|---|---|
> |$\Theta(1)$|1|1|1|
> |$\Theta(\log n)$|3,32|6,64|9,97|
> |$\Theta(n)$|10|100|1000|
> |$\Theta(n\log n)$|33,22|664,39|9965,78|
> |$\Theta(n^2)$|100|10 000|1 000 000|
> |$\Theta(n^3)$|1000|1 000 000|1 000 000 000|

> [!tip] 📌 Unidades de tiempo
> 
> |Símbolo|Nombre|Equivalencia|
> |---|---|---|
> |ns|nanosegundo|$10^{-9}$ s|
> |µs|microsegundo|$10^{-6}$ s $=10^3$ ns|
> |ms|milisegundo|$10^{-3}$ s $=10^3$ µs|
> |s|segundo|unidad base SI|
> 
> Suponiendo $1$ operación $=1$ ns, el número de operaciones de la tabla anterior se traduce directamente a tiempo real (por ejemplo, $\Theta(n^2)$ con $n=1000$ toma $10^6$ ns $\approx 1$ ms).

> [!warning] ⚠️ Por qué importa: crecimiento exponencial y factorial
> 
> |$n$|$2^n$ (operaciones)|Tiempo aprox.|
> |---|---|---|
> |20|1 048 576|≈ 1 ms|
> |30|≈ $1{,}07\times10^9$|≈ 1 s|
> |40|≈ $1{,}10\times10^{12}$|≈ 18 min|
> |50|≈ $1{,}13\times10^{15}$|≈ 13 días|
> 
> |$n$|$n!$ (operaciones)|Tiempo aprox.|
> |---|---|---|
> |10|$3{,}63\times10^6$|≈ 3,6 ms|
> |15|≈ $1{,}31\times10^{12}$|≈ 22 min|
> |20|≈ $2{,}43\times10^{18}$|≈ 77 años|
> 
> A partir de $n\approx50$, un algoritmo $\Theta(2^n)$ ya es impracticable; los algoritmos $\Theta(n!)$ se vuelven inviables incluso antes. Esta es la razón práctica detrás de todo el trabajo de las dos notas: **la notación asintótica predice, sin ejecutar nada, si un algoritmo será usable para el tamaño de entrada que te interesa.**

![[ChatGPT Image 18 ago 2026, 20_44_56.png]]

---

## 🔗 Conexiones

> [!note] 📋 Temas relacionados
> 
> - [[04 - Análisis de Algoritmos I - Fundamentos y Funciones Matemáticas]] — primera parte: cómo obtener las cotas a partir de una fórmula $f(n)$ ya dada.
> - [[03 - Pseudocódigo y Algoritmos]] — la sintaxis de los algoritmos analizados aquí.
> - [[01 - Relaciones de Recurrencia]] — la recurrencia de Fibonacci reaparece en el ejemplo de la caminata del robot.

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
> 
> [1] E. Pineda, _Análisis de Algoritmos_, clase MATG1051, ESPOL, jul. 2026.
> 
> [2] E. Pineda, _Taller III P5_, clase MATG1051, ESPOL, 2026 — ejercicios 2 y 3 (patrones de generalización).
> 
> [3] K. H. Rosen, _Discrete Mathematics and Its Applications_, 8th ed. New York, USA: McGraw-Hill, 2019, pp. 185–210.
> 
> [4] R. Johnsonbaugh, _Discrete Mathematics_, 8th ed. Hoboken, NJ, USA: Pearson, 2018, pp. 249–268.

---


## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Analizo algoritmos de búsqueda lineal y binaria.
> - [ ] Analizo algoritmos de ordenamiento (bubble, selection, insertion).
> - [ ] Determino peor caso, mejor caso y caso promedio.

> [!note] Nivel Intermedio
> - [ ] Analizo algoritmos de ordenamiento eficientes (merge sort, quicksort).
> - [ ] Comparo algoritmos de ordenamiento por complejidad.
> - [ ] Identifico el caso promedio y su relación con el peor caso.

> [!note] Nivel Avanzado
> - [ ] Analizo algoritmos de grafos (BFS, DFS) y su complejidad.
> - [ ] Aplico análisis amortizado a estructuras de datos (pilas, colas).
> - [ ] Resuelvo problemas de diseño de algoritmos óptimos.

**Tags:** #analisisdealgoritmos #notacionasintotica #recursion #tiemporeal #MATG1051 #unidad4 #ESPOL

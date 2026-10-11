---
dg-publish: true
---
# 🔀 Permutaciones y Combinaciones

## 🎯 Introducción

> [!info] 💡 ¿Cuándo importa el orden?
> 
> La distinción fundamental en conteo es si el **orden de selección importa** o no:
> 
> ```mermaid
> graph TD
>     A["Selección de r elementos de n disponibles"] --> B{¿Importa el orden?}
>     B -->|Sí| C[PERMUTACIÓN]
>     B -->|No| D[COMBINACIÓN]
>     C --> E["P(n,r) = n! / (n-r)!"]
>     D --> F["C(n,r) = n! / ((n-r)! r!)"]
>     C --> G["Con repetición: n! / (k₁! k₂! … kᵣ!)"]
>     D --> H["Con repetición: C(n+r-1, r)"]
> ```

---

## 🧠 El truco de un segundo para no confundirlas nunca más

> [!important] 🧠 Pregúntate: "si cambio el orden, ¿es un resultado distinto?"
> 
> - **Permutación** → el orden SÍ importa → ejemplo: elegir presidente/secretario/tesorero (ser presidente ≠ ser secretario, aunque sean las mismas 2 personas).
> - **Combinación** → el orden NO importa → ejemplo: elegir un comité de 3 personas sin cargos (da igual el orden en que los nombres).
> 
> **Truco para acordarte de las fórmulas sin memorizarlas:**
> 
> 1. Primero cuenta como si el orden SÍ importara: $P(n,r) = \dfrac{n!}{(n-r)!}$ (esto siempre es más fácil de razonar: $n$ opciones, luego $n-1$, luego $n-2$...).
> 2. Si en realidad el orden NO importaba, te diste cuenta de que **contaste cada grupo varias veces** (una vez por cada forma de ordenarlo). Divide entre $r!$ para quitar esas repeticiones:
> 
> $$C(n,r) = \frac{P(n,r)}{r!} = \frac{n!}{(n-r)!,r!}$$
> 
> Ejemplo con $n=4, r=2$: hay $P(4,2)=12$ formas ordenadas ($ab, ba, ac, ca,\ldots$), pero $ab$ y $ba$ son "el mismo grupo" si el orden no importa. Como cada grupo de 2 se puede ordenar de $2!=2$ maneras, divides $12/2=6$. Por eso $C(4,2)=6$.
> 
> > 💡 Nunca memorices cuál fórmula lleva el $r!$ abajo — razona: "¿estoy repitiendo grupos por el orden? Si sí, divido por las formas de reordenar ese grupo ($r!$)."

## 🔀 Permutaciones de $n$ elementos

> [!note] 📋 Definición — Permutación
> 
> Una **permutación** de $n$ elementos diferentes $x_1, \ldots, x_n$ es un **ordenamiento** de los $n$ elementos.
> 
> > [!abstract] Teorema Existen $n!$ permutaciones de $n$ elementos, donde $n! = n(n-1)(n-2)\cdots 2 \cdot 1$.
> > 
> > **Demostración:** Por el principio de la multiplicación: $n$ opciones para la 1ª posición, $n-1$ para la 2ª, ..., $1$ para la última. $\blacksquare$

> [!example] 📝 Ejemplo 1 — Subcadena fija (DEF juntas en orden)
> 
> **¿Cuántas permutaciones de ABCDEF contienen la subcadena DEF?**
> 
> Tratamos "DEF" como un **bloque único**. Entonces ordenamos 4 unidades: {DEF}, A, B, C.
> 
> $$4! = \mathbf{24}$$

> [!example] 📝 Ejemplo 2 — Subcadena en cualquier orden
> 
> **¿Cuántas permutaciones de ABCDEF contienen D, E, F juntas en cualquier orden?**
> 
> - El bloque {D,E,F} junto con A,B,C da $4!$ ordenamientos del bloque.
> - Dentro del bloque, D, E, F se pueden ordenar de $3! = 6$ maneras.
> 
> $$4! \cdot 3! = 24 \cdot 6 = \mathbf{144}$$

> [!example] 📝 Ejemplo 3 — Mesa circular
> 
> **¿De cuántas maneras se pueden sentar 6 personas alrededor de una mesa circular?**
> 
> En una mesa circular, las **rotaciones del mismo arreglo son equivalentes**. Fijamos una persona en un lugar y ordenamos las 5 restantes:
> 
> $$(6-1)! = 5! = \mathbf{120}$$
> 
> > [!tip]- 💡 ¿Por qué $n-1$?
> > 
> > En una fila hay $n!$ arreglos. En un círculo, cada arreglo tiene $n$ rotaciones que se ven igual (rotar todos una posición no cambia el arreglo). Entonces dividimos: $n!/n = (n-1)!$.

---

## 🔢 Permutaciones $r$ — $r$-arreglos

> [!note] 📋 Definición — Permutación $r$ o $r$-arreglo
> 
> Una **permutación $r$** de $n$ elementos es un **ordenamiento de $r$ elementos** tomados de ${x_1, \ldots, x_n}$. Se denota $P(n, r)$.
> 
> > [!abstract] Teorema Si $r \leq n$: $$P(n, r) = n(n-1)(n-2)\cdots(n-r+1) = \frac{n!}{(n-r)!}$$
> > 
> > **Demostración:** $n$ opciones para la 1ª posición, $n-1$ para la 2ª, ..., $n-r+1$ para la $r$-ésima. $\blacksquare$

> [!tip] 💡 Diferencia con permutación completa
> 
> - Permutación de $n$: ordena **todos** los elementos → $n!$
> - Permutación $r$ de $n$: ordena solo **$r$ de los $n$** → $P(n,r) = \dfrac{n!}{(n-r)!}$

> [!example] 📝 Ejemplo — 2-arreglos de {a,b,c}
> 
> Las permutaciones 2 de ${a,b,c}$ son (el orden importa, $ab \neq ba$):
> 
> $$ab,\ ba,\ ac,\ ca,\ bc,\ cb$$
> 
> $$P(3,2) = \frac{3!}{(3-2)!} = \frac{6}{1} = 6 \checkmark$$

> [!example] 📝 Ejemplo — Cargos directivos
> 
> **¿De cuántas maneras se puede elegir presidente, vicepresidente, secretario y tesorero de un grupo de 9 personas?**
> 
> El orden importa (los cargos son distintos). Es un 4-arreglo de 9: $$P(9, 4) = 9 \cdot 8 \cdot 7 \cdot 6 = \mathbf{3024}$$

> [!example] 📝 Ejemplo — Ingleses y franceses en fila
> 
> **¿De cuántas maneras pueden hacer fila 6 ingleses y 3 franceses si ningún par de franceses puede estar adyacente?**
> 
> **Estrategia:** primero colocar a los ingleses, luego intercalar a los franceses en los huecos.
> 
> |Paso|Descripción|Formas|
> |---|---|---|
> |1|Ordenar los 6 ingleses entre sí|$6! = 720$|
> |2|Hay 7 huecos disponibles (antes, entre y después)|—|
> |3|Elegir 3 huecos para los franceses (orden importa)|$P(7,3) = 7\cdot6\cdot5 = 210$|
> 
> Por el principio de la multiplicación: $$720 \cdot 210 = \mathbf{151{,}200}$$
> 
> > [!tip]- 💡 Visualización de los huecos
> > 
> > Si los ingleses son I₁I₂I₃I₄I₅I₆, los 7 huecos son:
> > 
> > ```
> > _I₁_I₂_I₃_I₄_I₅_I₆_
> > ```
> > 
> > Colocar un francés en cada hueco elegido garantiza que nunca quedan dos franceses juntos.

---

## 🔄 Permutaciones con Repetición (Generalizadas)

> [!note] 📋 Definición — Permutación con repetición
> 
> Dada una [[04 - Sucesiones y Cadenas|sucesión]] de $n$ elementos con $k_1$ objetos del tipo 1, $k_2$ del tipo 2, ..., $k_r$ del tipo $r$ (donde $n = k_1 + k_2 + \cdots + k_r$), el número de **ordenamientos distintos** es:
> 
> $$\frac{n!}{k_1!, k_2!, \cdots, k_r!}$$
> 
> Se divide por los factoriales de las multiplicidades para eliminar los ordenamientos repetidos.

> [!example] 📝 Ejemplo — Letras de MATEMATICA
> 
> **¿Cuántas cadenas distintas se pueden formar con las letras de MATEMATICA?**
> 
> MATEMATICA tiene 10 letras. Contamos las repeticiones:
> 
> |Letra|Apariciones|
> |---|---|
> |M|2|
> |A|3|
> |T|2|
> |E|1|
> |I|1|
> |C|1|
> |**Total**|**10**|
> 
> $$\frac{10!}{2!\cdot 3!\cdot 2!\cdot 1!\cdot 1!\cdot 1!} = \frac{3{,}628{,}800}{2 \cdot 6 \cdot 2} = \mathbf{151{,}200}$$

> [!example] 📝 Ejemplo — Distribución de libros
> 
> **¿De cuántas maneras se pueden dividir 8 libros entre Brenda (4), Samuel (2) y Mariana (2)?**
> 
> Representamos cada distribución como una secuencia de letras: B=Brenda, S=Samuel, M=Mariana. Por ejemplo BBBBSSM M significa que los libros 1,2,3,4 van a Brenda, 5,6 a Samuel, 7,8 a Mariana. Cada ordenamiento de BBBBSSMM da una distribución distinta:
> 
> $$\frac{8!}{4!\cdot 2!\cdot 2!} = \frac{40{,}320}{24 \cdot 2 \cdot 2} = \mathbf{420}$$

---

## 🎯 Combinaciones

> [!note] 📋 Definición — Combinación
> 
> Una **combinación $r$** de ${x_1, \ldots, x_n}$ es una **selección no ordenada** de $r$ elementos (un subconjunto de $r$ elementos). El número de combinaciones $r$ de $n$ elementos se denota:
> 
> $$C(n,r) = \binom{n}{r} = \frac{n!}{(n-r)!, r!}$$
> 
> > [!abstract] Demostración Cada permutación $r$ se construye en dos pasos: elegir la combinación ($\binom{n}{r}$ maneras) y luego ordenarla ($r!$ maneras). Entonces: $$\binom{n}{r} \cdot r! = P(n,r) = \frac{n!}{(n-r)!} \implies \binom{n}{r} = \frac{n!}{(n-r)!,r!} \quad \blacksquare$$

> [!tip] 💡 La diferencia clave
> 
> ||Permutación|Combinación|
> |---|---|---|
> |¿Importa el orden?|✅ Sí|❌ No|
> |${a,b}$ vs ${b,a}$|Son **distintos**|Son lo **mismo**|
> |Fórmula|$\dfrac{n!}{(n-r)!}$|$\dfrac{n!}{(n-r)!,r!}$|
> |Ejemplo con $n=4, r=2$|$4\cdot3=12$|$\dfrac{4\cdot3}{2}=6$|

> [!example] 📝 Ejemplo — Manos de póquer
> 
> **1. ¿Cuántas manos de 5 cartas hay en una baraja de 52?**
> 
> El orden no importa (una mano es un [[01 - Conjuntos, Cardinalidad y Subconjuntos|conjunto]] de cartas): $$\binom{52}{5} = \frac{52!}{47!\cdot 5!} = \mathbf{2{,}598{,}960}$$
> 
> **2. ¿Cuántas manos tienen todas las cartas del mismo palo (color)?**
> 
> - Elegir el palo: $\binom{4}{1} = 4$.
> - Elegir 5 cartas de las 13 de ese palo: $\binom{13}{5} = 1287$.
> 
> $$\binom{4}{1} \cdot \binom{13}{5} = 4 \cdot 1287 = \mathbf{5148}$$
> 
> **3. ¿Cuántas manos tienen un trío y un par (full house)?**
> 
> - Elegir la denominación del trío: 13 maneras.
> - Elegir la denominación del par: 12 maneras (diferente al trío).
> - Elegir 3 palos de 4 para el trío: $\binom{4}{3} = 4$.
> - Elegir 2 palos de 4 para el par: $\binom{4}{2} = 6$.
> 
> $$13 \cdot 12 \cdot \binom{4}{3} \cdot \binom{4}{2} = 13 \cdot 12 \cdot 4 \cdot 6 = \mathbf{3744}$$

> [!example] 📝 Ejemplo — Rutas en tablero $n \times n$
> 
> **¿Cuántas rutas hay de la esquina inferior izquierda a la superior derecha de un tablero $n \times n$, moviéndose solo a la derecha (D) o hacia arriba (A)?**
> 
> Cada ruta es una cadena de $2n$ pasos: exactamente $n$ pasos D y $n$ pasos A. Elegir qué $n$ posiciones serán D (las restantes son A automáticamente):
> 
> $$\binom{2n}{n}$$
> 
> > [!tip]- 💡 Doble interpretación
> > 
> > Este problema también se puede ver como una **permutación con repetición** de $n$ letras D y $n$ letras A: $$\frac{(2n)!}{n!\cdot n!} = \binom{2n}{n} \checkmark$$

---

## 🔁 Combinaciones con Repetición (Generalizadas)

> [!tip] 🧠 Piensa en "estrellas y barras" desde el inicio, no al final
> 
> Esta es la fórmula que más se memoriza sin entender. El truco real es imaginar $r$ objetos idénticos (★) que vas a repartir en $n$ cajas, usando $n-1$ separadores (|) para marcar dónde termina una caja y empieza la otra.
> 
> Ejemplo: repartir 5 pelotas en 3 colores (cajas) es lo mismo que ordenar 5 estrellas y 2 barras: `★★|★|★★` significa "2 en la caja 1, 1 en la caja 2, 2 en la caja 3".
> 
> El total de símbolos es $r + (n-1)$, y solo necesitas elegir en qué posiciones van las barras (o las estrellas, es lo mismo):
> 
> $$\binom{n+r-1}{r}$$
> 
> Si memorizas la imagen de "estrellas y barras" en vez de la fórmula, puedes reconstruirla siempre que la necesites.

> [!note] 📋 Definición — Combinación con repetición
> 
> Las **combinaciones con repetición** de $n$ tipos de elementos tomados de $r$ en $r$ son los grupos de $r$ elementos formados con los $n$ tipos dados, **sin importar el orden y permitiendo repetir** el mismo tipo.
> 
> > [!abstract] Teorema El número de combinaciones con repetición de $n$ tipos tomados de $r$ en $r$ es: $$\binom{n+r-1}{r} = \binom{n+r-1}{n-1}$$

> [!example] 📝 Ejemplo — Combinaciones con rep. de {a,b,c}
> 
> Las combinaciones con repetición de ${a,b,c}$ tomadas de 2 en 2 ($n=3$, $r=2$):
> 
> $$aa,\ ab,\ ac,\ bb,\ bc,\ cc$$
> 
> $$\binom{3+2-1}{2} = \binom{4}{2} = \mathbf{6} \checkmark$$

> [!example] 📝 Ejemplo — Pelotas de colores
> 
> **Hay 4 pilas (roja, azul, verde, blanca) con al menos 9 pelotas cada una.**
> 
> **1. ¿De cuántas maneras se pueden elegir 9 pelotas?** ($n=4$ tipos, $r=9$)
> 
> $$\binom{4+9-1}{9} = \binom{12}{9} = \binom{12}{3} = \mathbf{220}$$
> 
> **2. ¿De cuántas maneras si se requiere al menos una de cada color?**
> 
> Primero asignamos 1 pelota de cada color (obligatorio, consume 4). Quedan $9-4=5$ pelotas por elegir libremente de 4 tipos:
> 
> $$\binom{4+5-1}{5} = \binom{8}{5} = \binom{8}{3} = \mathbf{56}$$

> [!example] 📝 Ejemplo — Soluciones enteras no negativas
> 
> **¿Cuántas soluciones en enteros no negativos tiene $x_1 + x_2 + x_3 = 12$?**
> 
> Equivale a distribuir 12 unidades entre 3 variables (elegir cuántas unidades va a cada variable, con repetición permitida). Con $n=3$ variables y $r=12$:
> 
> $$\binom{12+3-1}{12} = \binom{14}{2} = \mathbf{91}$$
> 
> > [!tip]- 💡 Técnica de barras y estrellas
> > 
> > Imagina 12 estrellas ★ y 2 barras | que separan los grupos. Por ejemplo ★★★|★★★★★|★★★★ representa $x_1=3,\ x_2=5,\ x_3=4$. El número de arreglos de 12 estrellas y 2 barras es $\binom{14}{2} = 91$.

---

## 📊 Tabla Resumen General

||**Sin repetición**|**Con repetición**|
|---|---|---|
|**Selección ordenada** (permutación)|$\dfrac{n!}{(n-r)!}$|$\dfrac{n!}{k_1!\cdots k_r!}$|
|**Selección no ordenada** (combinación)|$\dbinom{n}{r}$|$\dbinom{n+r-1}{r}$|

---

## 📝 Ejercicios Propuestos

> [!question] 📋 Ejercicios
> 
> **1.** ¿Cuántas permutaciones de las letras de CÁLCULO existen?
> 
> **2.** Un grupo de 10 estudiantes debe elegir 3 representantes. ¿De cuántas maneras? ¿Y si uno de los representantes debe ser el jefe?
> 
> **3.** ¿Cuántas cadenas binarias de longitud 8 contienen exactamente cuatro 1s?
> 
> **4.** ¿Cuántas soluciones enteras no negativas tiene $x_1 + x_2 + x_3 + x_4 = 10$?

> [!success] ✅ Respuestas
> 
> **1.** CÁLCULO tiene 7 letras: C×2, Á×1, L×2, U×1, O×1. Total: $\dfrac{7!}{2!\cdot2!} = \dfrac{5040}{4} = \mathbf{1260}$.
> 
> **2.** Sin orden: $\binom{10}{3} = \mathbf{120}$. Con jefe: elegir el jefe (10 maneras) y luego los otros 2 de los 9 restantes $\binom{9}{2}=36$ → $10 \cdot 36 = \mathbf{360}$ (equivalentemente $P(10,3)/2! \cdot ...$, o directamente: primero jefe $10$, luego $\binom{9}{2}$).
> 
> **3.** Elegir qué 4 posiciones (de 8) serán 1s: $\binom{8}{4} = \mathbf{70}$.
> 
> **4.** Con $n=4$ variables y $r=10$: $\binom{10+4-1}{10} = \binom{13}{3} = \mathbf{286}$.

---


## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Calculo permutaciones P(n,r) = n!/(n-r)!
> - [ ] Calculo combinaciones C(n,r) = n!/(r!(n-r)!).
> - [ ] Distinguo cuándo importa el orden (permutación) vs cuándo no (combinación).

> [!note] Nivel Intermedio
> - [ ] Resuelvo problemas de permutaciones con elementos repetidos.
> - [ ] Aplico combinaciones con restricciones (selección sin reemplazo).
> - [ ] Uso identidades de Pascal para simplificar cálculos.

> [!note] Nivel Avanzado
> - [ ] Resuelvo problemas de distribución de objetos en categorías.
> - [ ] Aplico el principio de inclusión-exclusión a permutaciones con restricciones.
> - [ ] Conecto combinaciones con el triángulo de Pascal y el teorema del binomio.


> [!quote] 🔗 Conexiones
> - Previo: [[04 - Principios de Multiplicación y Suma]] — fundamentos
> - Siguiente: [[06 - Teorema del Binomio y Principio del Palomar]]
> - Relacionado: [[04 - Cardinalidad y Leyes de Cardinalidad]]

**Tags:** #matematicas-discretas #conteo #permutaciones #combinaciones #combinatoria #MATG1051
---
dg-publish: true
---
# 🔣 Teorema del Binomio y Principio del Palomar

## 🎯 Introducción

> [!info] 💡 ¿Qué contiene esta nota?
> 
> Esta nota cubre las dos últimas herramientas del capítulo de conteo:
> 
> ```mermaid
> graph TD
>     A[Herramientas de Conteo Avanzadas] --> B[Teorema Binomial]
>     A --> C[Principio del Palomar]
>     B --> D["Expansión de (a+b)ⁿ"]
>     B --> E["Identidades combinatorias"]
>     B --> F["Identidad de Pascal"]
>     C --> G["Versión 1: existencia de colisión"]
>     C --> H["Versión 2: cuántas colisiones mínimo"]
> ```

---

## 🧠 El truco para no memorizar la fórmula del binomio

> [!tip] 🧠 Piensa en "elegir de cuáles factores tomo la b"
> 
> $(a+b)^n$ es literalmente $(a+b)$ multiplicado por sí mismo $n$ veces. Cuando expandes, de **cada** uno de los $n$ paréntesis eliges o el término $a$ o el término $b$. Un término como $a^{n-k}b^k$ aparece una vez por cada forma distinta de **elegir en cuáles $k$ de los $n$ paréntesis tomaste la $b$** — y eso es exactamente $\binom{n}{k}$, ni más ni menos.
> 
> Así que no memorices la fórmula: piensa "tomé $b$ de $k$ paréntesis, ¿de cuántas formas pude elegir esos $k$ paréntesis de entre los $n$?" → esa es la respuesta.
> 
> **Truco extra para el signo:** si $b$ es negativo, cada vez que la tomas un número impar de veces el signo se voltea, por eso los términos alternan $+,-,+,-,\ldots$

## 📐 Coeficientes Binomiales

Los coeficientes $\binom{n}{k}$ ya aparecieron como número de combinaciones. Aquí revelan otra propiedad: son exactamente los coeficientes en la expansión de $(a+b)^n$.

> [!note] 📋 Teorema Binomial
> 
> Sean $a, b \in \mathbb{R}$ y $n \in \mathbb{N} \cup {0}$. Entonces:
> 
> $$\boxed{(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k}$$
> 
> > [!tip]- 💡 ¿Por qué aparecen los $\binom{n}{k}$?
> > 
> > Al expandir $(a+b)^n = (a+b)(a+b)\cdots(a+b)$, cada término $a^{n-k}b^k$ aparece tantas veces como formas hay de elegir **en cuáles** de los $n$ factores tomamos $b$ (y en los restantes tomamos $a$). Esa cantidad es exactamente $\binom{n}{k}$.

> [!example] 📝 Ejemplo — Expansión de $(2x - 5y)^6$
> 
> Aplicamos el teorema con $a = 2x$, $b = -5y$, $n = 6$:
> 
> $$(2x - 5y)^6 = \sum_{k=0}^{6} \binom{6}{k} (2x)^{6-k}(-5y)^k$$
> 
> |$k$|$\binom{6}{k}$|$(2x)^{6-k}$|$(-5y)^k$|Término|
> |---|---|---|---|---|
> |0|1|$64x^6$|$1$|$64x^6$|
> |1|6|$32x^5$|$-5y$|$-960x^5y$|
> |2|15|$16x^4$|$25y^2$|$6000x^4y^2$|
> |3|20|$8x^3$|$-125y^3$|$-20000x^3y^3$|
> |4|15|$4x^2$|$625y^4$|$37500x^2y^4$|
> |5|6|$2x$|$-3125y^5$|$-37500xy^5$|
> |6|1|$1$|$15625y^6$|$15625y^6$|
> 
> $$(2x-5y)^6 = 64x^6 - 960x^5y + 6000x^4y^2 - 20000x^3y^3 + 37500x^2y^4 - 37500xy^5 + 15625y^6$$
> 
> > [!tip]- 💡 Truco para el signo
> > 
> > Como $b = -5y$ es negativo, los términos alternan de signo: $+, -, +, -, \ldots$ (positivo cuando $k$ es par, negativo cuando $k$ es impar).

---

## 🔗 Identidades Combinatorias

> [!note] 📋 Identidad 1 — Suma de todos los coeficientes binomiales
> 
> $$\sum_{k=0}^{n}\binom{n}{k} = 2^n$$
> 
> > [!abstract]- Demostración Aplicamos el teorema binomial con $a = b = 1$: $$2^n = (1+1)^n = \sum_{k=0}^{n}\binom{n}{k} 1^{n-k} 1^k = \sum_{k=0}^{n}\binom{n}{k} \quad \blacksquare$$
> 
> **Interpretación:** La suma de los subconjuntos de tamaño 0, 1, 2, ..., $n$ de un [[04 - Cardinalidad y Leyes de Cardinalidad|Cardinalidad]] de $n$ elementos es igual al total de subconjuntos: $2^n$. Esto es consistente con lo visto en el principio de la multiplicación.

> [!note] 📋 Identidad de Pascal
> 
> Para todo $n \in \mathbb{N}$ y $1 \leq k \leq n$:
> 
> $$\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}$$
> 
> > [!abstract]- Demostración algebraica
> > 
> > $$\binom{n}{k-1} + \binom{n}{k} = \frac{n!}{(n-k+1)!(k-1)!} + \frac{n!}{(n-k)!,k!}$$
> > 
> > Factorizamos $\dfrac{n!}{(n-k)!(k-1)!}$:
> > 
> > $$= \frac{n!}{(n-k)!(k-1)!}\left(\frac{1}{n+1-k} + \frac{1}{k}\right) = \frac{n!}{(n-k)!(k-1)!} \cdot \frac{n+1}{(n+1-k),k}$$
> > 
> > $$= \frac{(n+1)!}{(n+1-k)!,k!} = \binom{n+1}{k} \quad \blacksquare$$
> 
> > [!tip]- 💡 Interpretación combinatoria
> > 
> > Para elegir $k$ elementos de ${x_1,\ldots,x_{n+1}}$, fijamos $x_{n+1}$:
> > 
> > - Si $x_{n+1}$ **está** en la selección → elegimos $k-1$ de los $n$ restantes: $\binom{n}{k-1}$.
> > - Si $x_{n+1}$ **no está** → elegimos $k$ de los $n$ restantes: $\binom{n}{k}$.

---

## 🔺 Triángulo de Pascal

> [!tip] 🧠 Cómo construirlo tú mismo en 10 segundos (sin fórmulas)
> 
> Solo dos reglas:
> 
> 1. **Los bordes siempre son 1** (los extremos de cada fila).
> 2. **Cada número interior = la suma de los dos números que tiene justo encima.**
> 
> ```
>       1       ←  fila n=0
>      1 1      ←  fila n=1: bordes = 1
>     1 2 1     ←  fila n=2: el 2 del medio = 1+1 (los de arriba)
>    1 3 3 1    ←  fila n=3: 3 = 1+2, 3 = 2+1
>   1 4 6 4 1   ←  fila n=4: 6 = 3+3
> ```
> 
> Con esas dos reglas puedes reconstruir cualquier fila sin memorizar nada — y sin calcular un solo factorial.
> La identidad de Pascal ($\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}$) es justamente la versión algebraica de la regla "sumar los dos de arriba". Por eso el triángulo funciona:
> 
> ```
> n=0:               1  
> n=1:             1    1  
> n=2:           1    2    1  
> n=3:         1    3    3    1  
> n=4:       1    4    6    4    1  
> n=5:     1    5   10   10    5    1  
> n=6:   1    6   15   20   15    6    1  
> ```

> [!tip] 💡 Propiedades del triángulo
> 
> - La fila $n$ contiene los coeficientes $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$ — es decir, la fila $n$ te da **directamente** los coeficientes de la expansión de $(a+b)^n$, sin calcular ningún $\binom{n}{k}$ a mano.
> - La suma de la fila $n$ es $2^n$ (por la identidad 1). _Chequeo rápido: fila $n=4$ → $1+4+6+4+1=16=2^4$ ✓_
> - El triángulo es **simétrico**: $\binom{n}{k} = \binom{n}{n-k}$ — se nota a simple vista porque cada fila se lee igual de izquierda a derecha que de derecha a izquierda.
> 
> **Truco de examen:** si te piden un coeficiente binomial pequeño (n ≤ 6 o 7), muchas veces es más rápido dibujar el triángulo hasta esa fila que aplicar la fórmula de factoriales.

---

## 🐦 Principio del Palomar

> [!tip] 🧠 En una frase (y cómo reconocer cuándo usarlo)
> 
> Si tienes más calcetines que cajones, sí o sí algún cajón tendrá 2+ calcetines. Así de simple. La parte difícil del palomar **nunca es la lógica** — es identificar en el problema **quién es la "paloma" (lo que hay muchos) y quién es el "palomar" (las categorías limitadas)**.
> 
> **Truco para resolver cualquier ejercicio de palomar en 3 pasos:**
> 
> 1. Pregúntate: "¿qué estoy contando que hay MUCHOS?" → esas son tus palomas ($n$).
> 2. Pregúntate: "¿en cuántas categorías/casillas se pueden agrupar?" → eso es tus palomares ($m$).
> 3. Si $n > m$, garantizado que algún palomar tiene 2+. Si te piden garantizar $k$ o más, usa $k = \lceil n/m \rceil$ (redondea siempre hacia arriba).
> 
> El paso que más cuesta es el 2 — inventar las categorías correctas. Usualmente conviene pensar "¿qué pares de cosas quiero que colisionen?" y diseñar la categoría a partir de ahí (mira la tabla de estrategia más abajo).

> [!note] 📋 Definición — Primera versión
> 
> Si $n$ palomas vuelan a $k$ palomares y $k < n$, entonces **algún palomar contiene al menos 2 palomas**.

> [!warning] ⚠️ Limitación importante
> 
> El principio **solo garantiza la existencia** del objeto buscado. No dice cómo encontrarlo ni cuántos hay con esa propiedad. Para aplicarlo, debemos decidir qué objetos hacen el papel de **palomas** y qué objetos el papel de **palomares**.

> [!example] 📝 Ejemplo 1 — Nombres duplicados
> 
> **Se sabe que 14 personas tienen nombres de pila de entre {Alicia, María, Luis, Carlos} y apellidos de entre {López, Macías, Moreira}. Demuestre que al menos dos personas tienen el mismo nombre completo.**
> 
> - **Palomas:** 14 personas.
> - **Palomares:** $4 \times 3 = 12$ nombres completos posibles.
> 
> Como $14 > 12$, por el principio del palomar, algún nombre completo es compartido por al menos 2 personas. $\blacksquare$

---

## 🐦🐦 Principio del Palomar — Segunda Versión (Generalizada)

> [!note] 📋 Definición — Segunda versión
> 
> Sea $f: X \to Y$ con $|X| = n$ y $|Y| = m$. Sea $k = \left\lceil \dfrac{n}{m} \right\rceil$. Entonces existen al menos $k$ valores $a_1, \ldots, a_k \in X$ tales que:
> 
> $$f(a_1) = f(a_2) = \cdots = f(a_k)$$
> 
> Es decir, algún valor de $Y$ tiene **al menos $k$ preimágenes** en $X$.

> [!tip] 💡 ¿Por qué $\lceil n/m \rceil$?
> 
> Si ningún palomar tuviera $k$ palomas, cada uno tendría a lo más $k-1$. El total sería a lo sumo $m(k-1) < n$ palomas (por la definición de techo), contradicción. $\blacksquare$

> [!example] 📝 Ejemplo 2 — Tres personas con el mismo nombre
> 
> **26 personas con nombres de pila de entre {Alfredo, Julio, Mario, Kevin} y apellidos de entre {Domínguez, Galarza, Gaibor}. Demuestre que al menos 3 personas tienen el mismo nombre completo.**
> 
> - **Palomas:** 26 personas ($n=26$).
> - **Palomares:** $4 \times 3 = 12$ nombres posibles ($m=12$).
> 
> $$k = \left\lceil \frac{26}{12} \right\rceil = \lceil 2.16\ldots \rceil = 3$$
> 
> Por el principio del palomar generalizado, algún nombre se asigna a al menos **3 personas**. $\blacksquare$

> [!example] 📝 Ejemplo 3 — Jugadores de basketball
> 
> **12 jugadores (numerados 1–12) colocados alrededor del cuadro central. Demuestre que hay 3 jugadores consecutivos cuya suma es al menos 20.**
> 
> Sean $S_1, S_2, \ldots, S_{12}$ las sumas de cada trío de jugadores consecutivos (en forma circular). Observamos que:
> 
> $$S_1 + S_2 + \cdots + S_{12} = 3(1+2+\cdots+12) = 3 \cdot 78 = 234$$
> 
> (cada jugador aparece en exactamente 3 tríos). Si todas las sumas fueran $< 20$, es decir $\leq 19$, el total sería a lo sumo $12 \cdot 19 = 228 < 234$, contradicción. Por tanto, alguna suma es $\geq 20$. $\blacksquare$

---

## 🔍 Estrategia para Aplicar el Palomar

> [!note] 📋 Técnica — Cómo identificar palomas y palomares
> 
> |Elemento|Papel|Pregunta a hacerse|
> |---|---|---|
> |El conjunto más grande|**Palomas**|¿Qué objetos quiero "meter" en categorías?|
> |Las categorías|**Palomares**|¿Cuántas categorías distintas hay?|
> |La conclusión|**Colisión**|¿Cuántos objetos caen en la misma categoría?|
> 
> La **clave** es definir las categorías de forma que la colisión garantizada sea exactamente la propiedad que queremos demostrar.

---

## 📝 Ejercicios Propuestos

> [!question] 📋 Ejercicios del PDF
> 
> **1.** Un inventario de 80 artículos, cada uno marcado como disponible o no disponible. Hay 50 disponibles. Demuestre que existen al menos 2 artículos **no disponibles** que están separados por 3 o por 6 artículos en la lista.
> 
> **2.** 12 jugadores de basketball (numerados 1–12) colocados alrededor del cuadro central. Demuestre que hay 3 jugadores consecutivos cuya suma es al menos 20. _(resuelto arriba)_
> 
> **3.** Demuestre que en un grupo de 10 personas hay al menos dos tales que la diferencia o la suma de sus edades es divisible por 16. (Suponga edades enteras.)

> [!question] 📋 Ejercicios adicionales
> 
> **4.** ¿Cuál es el mínimo de personas que deben estar en una sala para garantizar que al menos 3 nacieron el mismo mes?
> 
> **5.** Demuestre que entre 5 puntos enteros en el plano, siempre hay dos cuyo punto medio también tiene coordenadas enteras.

> [!success] ✅ Respuestas
> 
> **4.** $n=12$ palomares (meses). Queremos $k=3$: $\lceil n/12 \rceil = 3 \Rightarrow n > 24$, entonces se necesitan al menos $\mathbf{25}$ personas.
> 
> **5.** El punto medio de $(x_1,y_1)$ y $(x_2,y_2)$ tiene coordenadas enteras $\iff$ $x_1+x_2$ y $y_1+y_2$ son pares $\iff$ $x_1,x_2$ tienen la misma paridad **y** $y_1,y_2$ tienen la misma paridad. Las paridades posibles de un punto son: (par,par), (par,impar), (impar,par), (impar,impar) → 4 categorías. Con 5 puntos, por el palomar, al menos 2 comparten categoría, y ese par tiene punto medio entero. $\blacksquare$

---


## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Expando (a+b)^n usando el teorema del binomio.
> - [ ] Identifico coeficientes binomiales en el triángulo de Pascal.
> - [ ] Aplico el principio del palomar para probar existencia.

> [!note] Nivel Intermedio
> - [ ] Resuelvo problemas de conteo usando coeficientes binomiales.
> - [ ] Aplico el principio del palomar generalizado a problemas de distribución.
> - [ ] Uso identidades binomiales para simplificar sumatorias.

> [!note] Nivel Avanzado
> - [ ] Resuelvo identidades binomiales usando el método combinatorio.
> - [ ] Aplico el principio del palomar a problemas de complejidad computacional.
> - [ ] Conecto el teorema del binomio con distribuciones de probabilidad.


> [!quote] 🔗 Conexiones
> - Previo: [[05 - Permutaciones y Combinaciones]] — combinaciones
> - Relacionado: 04 - Recurrencia y Algoritmos — relación con recurrencias
> - Aplicación: [[01 - Grafos I - Conceptos Básicos y Recorridos]]

**Tags:** #matematicas-discretas #conteo #teorema-binomial #identidades #pascal #palomar #combinatoria #MATG1051
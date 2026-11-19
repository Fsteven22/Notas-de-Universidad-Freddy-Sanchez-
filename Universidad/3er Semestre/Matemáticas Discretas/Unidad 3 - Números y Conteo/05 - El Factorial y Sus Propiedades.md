---
dg-publish: true
tags: [MATG1051, unidad3, factorial, permutaciones, combinaciones, binomial]
---

# ❗ El Factorial y Sus Propiedades

## 🎯 Introducción

> [!info] 💡 ¿Qué es el factorial y por qué importa?
>
> El **factorial** de un entero no negativo $n$, denotado $n!$, cuenta cuántos ordenamientos de $n$ objetos distintos existen. Es la herramienta fundamental de la combinatoria: todas las fórmulas de permutaciones y combinaciones nacen de ella.
>
> **Por qué importa:** sin el factorial no existen las fórmulas de conteo ordenado ($P(n,r) = \frac{n!}{(n-r)!}$), las permutaciones circulares ($(n-1)!$) ni los coeficientes binomiales. Toda la Unidad 3 se apoya en esta sola noción.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dis-u3-05-04-graph.svg]]
> **Se lee así:** un camino en fila de izquierda a derecha: la primera posición se puede llenar con cualquiera de los $n$ objetos, la segunda con los $n-1$ restantes, … y la última con 1; el principio multiplicativo hace el resto: $n \cdot (n-1) \cdots 2 \cdot 1 = n!$.
> **Por qué importa:** es la demostración "a mano" de por qué $n!$ cuenta órdenes — el factorial no es una definición caprichosa, es el resultado del conteo secuencial.

---

## 📋 Definición Formal

> [!note] 📋 Definición 16 — Factorial
>
> Sea $n \in \mathbb{N}$, con $n \geq 0$. El **factorial** de $n$ se define por:
>
> $$n! = \begin{cases} 1 & \text{si } n = 0 \\ n \cdot (n-1)! & \text{si } n \geq 1 \end{cases}$$
>
> o, en forma explícita, $n! = 1 \cdot 2 \cdot 3 \cdots n$ (producto de los $n$ primeros enteros positivos).
>
> **Se lee así:** $n!$ es el producto de los $n$ primeros enteros positivos, con la convención $0! = 1$ (producto vacío).
>
> **Ejemplo:** $5! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120$; y $0! = 1$ por convención.

> [!note] 📋 Definición 17 — Telescopio de factoriales
>
> Para enteros $0 \leq k \leq n$:
>
> $$\frac{n!}{k!} = (k+1)(k+2) \cdots n$$
>
> Si $n = k$, la fracción vale $1$ (producto vacío).
>
> **Se lee así:** dividir $n!$ entre $k!$ cancela los $k$ factores más pequeños y deja la cadena desde $k+1$ hasta $n$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dis-u3-05-05-graph.svg]]
> **Se lee así:** $n!$ se parte en dos: el bloque de los factores $1 \ldots k$ (que es exactamente $k!$ y se cancela) y la cola $k+1 \ldots n$ (que es lo que sobrevive). El diagrama de la flecha punteada es la cancelación: nada se multiplica, solo se elimina el prefijo común.
>
> **Ejemplo:** $\dfrac{7!}{3!} = 4 \cdot 5 \cdot 6 \cdot 7 = 840$.

> [!note] 📋 Definición 18 — Ceros finales de $n!$ en base 10
>
> El número de ceros con los que termina $n!$ es la cantidad de factores $5$ en su descomposición:
>
> $$z(n) = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \cdots$$
>
> **Se lee así:** cada múltiplo de $5$ aporta un cero al factorial; los múltiplos de $25$ aportan un segundo cero (y los $125$ un tercero).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dis-u3-05-06-graph.svg]]
> **Se lee así:** primero hay que encontrar todos los factores $5$ que aparecen en $n!$: los $\lfloor n/5 \rfloor$ múltiplos de $5$ aportan uno cada uno, los $\lfloor n/25 \rfloor$ múltiplos de $25$ aportan uno adicional (ya tienen dos 5), los $\lfloor n/125 \rfloor$ uno más, y así sucesivamente; la suma de todos los cocientes es $z(n)$.
>
> **Ejemplo:** $50!$ termina en $z(50) = 10 + 2 = 12$ ceros.

---

## 📐 Propiedades y Teoremas

> [!note] 📋 Propiedad 1 — Recurrencia
>
> $n! = n \cdot (n-1)!$ para todo $n \geq 1$.
>
> **Se lee así:** el factorial se construye del anterior multiplicándolo por el índice.
>
> **Ejemplo:** $6! = 720 = 6 \cdot 120 = 6 \cdot 5!$.

> [!note] 📋 Propiedad 2 — Monotonía y crecimiento
>
> $(n+1)! > n!$ para todo $n \geq 0$ (en particular, la sucesión $n!$ es estrictamente creciente y $n! \geq 2^{n-1}$ para $n \geq 1$).
>
> **Se lee así:** cada factorial es mayor que el anterior; el crecimiento es superexponencial (mayor que cualquier geométrica).
>
> **Ejemplo:** $4! = 24 \geq 2^{3} = 8$; $5! = 120 \geq 2^4 = 16$.

> [!note] 📋 Propiedad 3 — Divisibilidad telescópica
>
> Si $0 \leq k \leq n$, entonces $k! \mid n!$ (con cociente $(k+1)(k+2)\cdots n \in \mathbb{Z}$).
>
> **Demostración:** por la Definición 17, $\frac{n!}{k!} = (k+1)(k+2)\cdots n \in \mathbb{N}$.
>
> **Ejemplo:** $3! \mid 7!$ porque $\frac{7!}{3!} = 840 \in \mathbb{Z}$.

> [!note] 📋 Propiedad 4 — El factorial cuenta permutaciones
>
> Existen exactamente $n!$ permutaciones de $n$ objetos distintos. Como consecuencia, las permutaciones circulares son $(n-1)!$.
>
> **Ejemplo:** las $5$ personas de un grupo se sientan en una fila de $120$ formas ($5! = 120$); alrededor de una mesa circular, de $4! = 24$.

> [!note] 📋 Propiedad 5 — Conexión con los coeficientes binomiales
>
> El coeficiente binomial se define $\binom{n}{k} = \frac{n!}{k! \, (n-k)!}$; de ella se derivan $\binom{n}{0} = \binom{n}{n} = 1$ y la simetría $\binom{n}{k} = \binom{n}{n-k}$ (sustituir $k \mapsto n - k$).
>
> **Ejemplo:** $\binom{7}{2} = \frac{7!}{2! \, 5!} = 21$; y $\binom{7}{5} = \binom{7}{2} = 21$.

---

## 🧮 Ejemplos Resueltos

> [!example] 📝 Ejemplo 1 — Simplificación telescópica
>
> Simplifica $\dfrac{10!}{7!}$ y $\dfrac{12!}{10! \, 2!}$.
>
> > [!success]- ✅ Solución
> >
> > $\dfrac{10!}{7!} = 8 \cdot 9 \cdot 10 = 720$.
> >
> > $\dfrac{12!}{10! \, 2!} = \dfrac{12!}{10! \cdot 2} = \dfrac{11 \cdot 12}{2} = 66$.
> >
> > **Lección:** cancelar el prefijo común del factorial es siempre ventajoso: nunca calcules un factorial que no hay que usar.

> [!example] 📝 Ejemplo 2 — Ceros finales
>
> ¿Cuántos ceros finales tiene $200!$?
>
> > [!success]- ✅ Solución
> >
> > $z(200) = \lfloor 200/5 \rfloor + \lfloor 200/25 \rfloor + \lfloor 200/125 \rfloor = 40 + 8 + 1 = 49$.
> >
> > **Lección:** descomponer el recuento en sumas de cocientes evita contar factores a mano.

> [!example] 📝 Ejemplo 3 — Divisibilidad del factorial
>
> Demuestra que $6! \mid 10!$ y calcula el cociente.
>
> > [!success]- ✅ Solución
> >
> > Por la Propiedad 3, $\dfrac{10!}{6!} = 7 \cdot 8 \cdot 9 \cdot 10 = 5040 \in \mathbb{N}$.
> >
> > **Lección:** $\frac{n!}{k!}$ siempre es el número de formas ordenadas de elegir los $n-k$ últimos elementos — 1.440 da divido exacta frecuentemente.

> [!example] 📝 Ejemplo 4 — El factorial y las permutaciones circulares
>
> De cuántas maneras se pueden sentar 6 personas alrededor de una mesa si la persona A y B no pueden estar juntas?
>
> > [!success]- ✅ Solución
> >
> > Congelamos el orden circular: sin restricción hay $(6-1)! = 120$ formas.
> >
> > Con A y B juntos: tratar AB como bloque → $(5-1)! = 24$ formas para los $5$ bloques, por $2$ órdenes internos (AB o BA): $24 \cdot 2 = 48$.
> >
> > Pedidas (no juntas): $120 - 48 = 72$.
> >
> > **Lección:** el mismo truco sirve cuando el factorial cuenta todos los arreglos y luego se excluyen los prohibidos (principio de inclusión-exclusión).

---

## 📝 Ejercicios

> [!example] 📋 Planteamiento
>
> Calcula $0! \cdot 1! \cdot 2! \cdot 3!$ y $(0! + 1! + 2! + 3!)$.
>
> > [!success]- ✅ Solución
> >
> > $0! = 1$, $1! = 1$, $2! = 2$, $3! = 6$.
> >
> > Producto: $1 \cdot 1 \cdot 2 \cdot 6 = 12$.
> >
> > Suma: $1 + 1 + 2 + 6 = 10$.
> >
> > **Lección:** $0! = 1$ no es opcional; sin esa convención nada cuadra.

> [!example] 📋 Planteamiento
>
> Simplifica $\dfrac{2n}{(n+1)} \binom{2n}{n}$.
>
> > [!success]- ✅ Solución
> >
> > $\binom{2n}{n} = \dfrac{(2n)!}{n! \, n!}$. Entonces
> >
> > $$\frac{2n}{(n+1)} \cdot \frac{(2n)!}{n!\,n!} = \frac{(2n+1) \cdot (2n)!}{(n+1) \cdot n!\, n!} = \frac{(2n+1)!}{(n+1)!\, n!} = \binom{2n+1}{n+1}$$
> >
> > **Lección:** la forma cerrada del resultado es el coeficiente binomial; usar telescopios evita expandir factoriales grandes.

> [!example] 📋 Planteamiento
>
> ¿Cuántos ceros finales tiene $75!$?
>
> > [!success]- ✅ Solución
> >
> > $z(75) = \lfloor 75/5 \rfloor + \lfloor 75/25 \rfloor = 15 + 3 = 18$.
> >
> > **Lección:** añadir siempre el último término que no desborda la base.

> [!example] 📋 Planteamiento
>
> Demuestra $\binom{n}{k} = \binom{n}{n-k}$ a partir de la fórmula con factoriales.
>
> > [!success]- ✅ Solución
> >
> > $$\binom{n}{n-k} = \frac{n!}{(n-k)!\, \bigl(n-(n-k)\bigr)!} = \frac{n!}{(n-k)!\, k!} = \binom{n}{k}$$
> >
> > **Lección:** la simetría se ve inmediatamente al intercambiar $k \leftrightarrow n-k$ en el denominador.

---

## ✅ Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino el factorial con la recurrencia $n! = n(n-1)!$ y la convención $0! = 1$.
> - [ ] Simplifico fracciones con factoriales usando el telescopio.
> - [ ] Conozco que $n!$ cuenta las permutaciones de $n$ elementos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Uso la divisibilidad telescópica $k! \mid n!$ para decidir divisibilidad sin calcular.
> - [ ] Calculo los ceros finales de $n!$ con la fórmula $\lfloor n/5 \rfloor + \lfloor n/25 \rfloor + \cdots$.
> - [ ] Relaciono factorial, permutaciones $P(n,r)$ y coeficientes binomiales $\binom{n}{k}$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas que mezclan el factorial con conteo restringido (inclusión-exclusión).
> - [ ] Verifico resultados complejos mediante el factorial como conteo de órdenes.

---

## 📊 Resumen Visual

> [!note] 🗺️ Diagrama — Resumen Visual
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dis-u3-05-03-graph.svg]]
> **Se lee así:** un cuadro raíz "$n!$ — Factorial" despliega cuatro subgrafos: **Definición** (la recurrencia $n! = n(n-1)!$ con $0! = 1$), **Telescopio** (cancelar $\frac{n!}{k!}$ deja la cadena $(k+1)\cdots n$), **Permutaciones** ($n!$ órdenes de $n$ objetos y $(n-1)!$ arreglos circulares) y **Combinatorios** ($\binom{n}{k}$, simetría y ceros finales).
> **Por qué importa:** es la estructura de toda la nota; con ella se reconoce rápidamente qué tipo de cuenta es la que toca.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - Johnsonbaugh, *Discrete Mathematics*, 8.ª ed., cap. 5: permutaciones y combinaciones.
> - [[Unidad 3 - Números y Conteo/06 - Permutaciones y Combinaciones|06 - Permutaciones y Combinaciones]] — el factorial como conteo de órdenes.
> - [[Unidad 3 - Números y Conteo/07 - Teorema del Binomio y Principio del Palomar|07 - Teorema del Binomio y Principio del Palomar]] — $\binom{n}{k}$ y $\binom{n}{k} = \binom{n}{n-k}$.
> - [[Unidad 3 - Números y Conteo/04 - Principios de Multiplicación y Suma|04 - Principios de Multiplicación y Suma]] — el principio multiplicativo detrás de $n!$.
> - [[Unidad 2 - Funciones y Relaciones/04 - Sucesiones y Cadenas|04 - Sucesiones y Cadenas]] — el factorial como producto de sucesión telescópica.
> - [[Unidad 1 - Logica y Conjuntos/III - Razonamiento Inductivo/03 - Inducción Matemática|03 - Inducción Matemática]] — la inducción que prueba $n! = n \cdot (n-1)!$ y $n! \geq 2^{n-1}$.
> - Unidad 0 - Guias y Ejercicios/Lecciones/SOLUCIÓN_LEC_2.pdf — Lección 2 (04/11/2026, paralelo 1): el producto telescópico $\prod_{i=2}^n(1-\frac{1}{i^2}) = \frac{n+1}{2n}$ resuelto con inducción, y la relación $f \,R\, g \iff f(0)=g(0)$ sobre funciones con su clase $[f] = \{g : g(0) = 0\}$.
> 📎 [[../Unidad 0 - Guias y Ejercicios/Lecciones/SOLUCIÓN_LEC_2.pdf|SOLUCIÓN_LEC_2.pdf]]
> - Unidad 0 - Guias y Ejercicios/Lecciones/SOLUCIÓN_LEC_1.pdf — Lección 1 (14/10/2026, paralelo 1), capítulo 1 «Conjunto, lógica, demostraciones y circuitos combinatorios»: proposición con cuantificadores múltiples resuelta con testigo.
> 📎 [[../Unidad 0 - Guias y Ejercicios/Lecciones/SOLUCIÓN_LEC_1.pdf|SOLUCIÓN_LEC_1.pdf]]

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Regla rápida: antes de cada fórmula con factorial, pregúntate si puedes simplificar cancelando prefijos comunes.
> - Después pasa a [[Unidad 3 - Números y Conteo/06 - Permutaciones y Combinaciones|06 - Permutaciones y Combinaciones]] (usos del factorial en conteo).
> - Cierra con [[Unidad 3 - Números y Conteo/07 - Teorema del Binomio y Principio del Palomar|07 - Teorema del Binomio y Principio del Palomar]] ($\binom{n}{k}$ con factoriales).

---

**Tags:** #matematicas-discretas #unidad3 #factorial #conteo #permutaciones #combinatoria #MATG1051

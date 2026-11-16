---
dg-publish: true
tags: [MATG1045, unidad6, propiedades-sumatoria, notacion-sigma, sumas-teorema, linealidad, cambio-indice, sumas-riemann]
---

# 🔄 Propiedades de la Sumatoria

## 🎯 Introducción

> [!info] 💡 Qué resuelve la notación sigma
>
> La **sumatoria** expresa la suma de muchos términos con una sola fórmula: $\sum_{i=a}^{b} f(i) = f(a) + f(a+1) + \cdots + f(b)$. En vez de escribir cientos de sumandos, se describe el patrón una vez y se dice de dónde a dónde va.
>
> **Por qué importa:** es el lenguaje en el que se escribe la suma de Riemann, la definición de serie y la mayoría de los límites de la materia. Dominar sus propiedades convierte cálculos largos en manipulaciones de dos renglones.
>
> **Ejemplo:** $\sum_{i=1}^{4} 3i = 3\sum_{i=1}^{4} i = 3 \cdot 10 = 30$: sacar el $3$ fuera es aplicar linealidad.

> [!warning] ⚠️ Los tres errores que más se repiten
>
> 1. **NO** trates la sumatoria de un producto como producto de sumatorias: $\sum f(i)g(i) \neq \sum f(i) \cdot \sum g(i)$.
> 2. **NO** cambies de índice sin ajustar los límites: si $j = i + k$, los extremos también se desplazan $k$.
> 3. **NO** cuentes términos de memoria: son $b - a + 1$, y ese "más uno" es el que se olvida.
>
> **Por qué importa:** los tres producen resultados numéricos malos con un planteamiento impecable, por eso conviene verificar con un caso pequeño.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Sumatoria y notación sigma
>
> La **sumatoria** de una secuencia $f(i)$ con índice $i$ recorriendo los enteros de $a$ a $b$ es
>
> $$\sum_{i=a}^{b} f(i) = f(a) + f(a+1) + f(a+2) + \cdots + f(b).$$
>
> Sus componentes son: $\Sigma$ (símbolo de sumatoria), $i$ (índice o variable *dummy*), $a$ (límite inferior), $b$ (límite superior) y $f(i)$ (término general).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Propiedades_de_la_Sumatoria_01.svg]]
>
> **Se lee así:** una caja central con la notación sigma se abre en cinco flechas hacia sus piezas: el índice, el límite inferior, el límite superior y el término general, más una quinta hacia un bloque de "casos especiales" que a su vez se divide en tres ramas: límite inferior mayor que el superior, límites iguales, e índice negativo.
>
> **Por qué importa:** el diagrama separa el símbolo de sus piezas y de paso advierte de los tres casos límite. Te evita errores al contar términos y al cambiar el índice sin reajustar los extremos, que es donde se pierden más puntos.
>
> **Ejemplo:** en $\sum_{i=1}^{5} 7$ hay $5 - 1 + 1 = 5$ términos y el resultado es $7 \cdot 5 = 35$; si el inferior fuera mayor que el superior, la suma sería $0$.

> [!note] 📋 Casos especiales de la sumatoria
>
> 1. **Suma vacía:** si $a > b$, entonces $\sum_{i=a}^{b} f(i) = 0$ (no hay términos que sumar).
> 2. **Un solo término:** si $a = b$, entonces $\sum_{i=a}^{b} f(i) = f(a)$.
> 3. **Índice negativo:** está permitido; por ejemplo $\sum_{i=-2}^{3} i = -2 -1 + 0 + 1 + 2 + 3 = 3$.
>
> **Por qué importa:** el caso vacío resuelve de golpe cualquier suma con extremos invertidos, y el recuento $b - a + 1$ es lo que decide si la suma tiene uno, varios o ningún término.

---

## ⚖️ Propiedades fundamentales

> [!success] ✅ Linealidad: constante fuera y suma repartida
>
> Para cualquier constante $c$:
>
> $$\sum_{i=a}^{b} c\,f(i) = c\sum_{i=a}^{b} f(i), \qquad \sum_{i=a}^{b}\big[f(i) + g(i)\big] = \sum_{i=a}^{b} f(i) + \sum_{i=a}^{b} g(i).$$
>
> Restando, $\sum_{i=a}^{b}\big[f(i) - g(i)\big] = \sum_{i=a}^{b} f(i) - \sum_{i=a}^{b} g(i)$.
>
> **Por qué importa:** la linealidad es lo que permite partir un polinomio en monomios y sumar cada uno con su fórmula conocida.
>
> **Ejemplo:** $\sum_{i=1}^{4} (2i + 5) = 2\sum_{i=1}^{4} i + \sum_{i=1}^{4} 5 = 2 \cdot 10 + 5 \cdot 4 = 40$.

> [!success] ✅ Suma de una constante
>
> Una constante sumada $b - a + 1$ veces vale:
>
> $$\sum_{i=a}^{b} c = c\,(b - a + 1).$$
>
> **Por qué importa:** recuerda que la sumatoria **cuenta términos**, y ese recuento $b-a+1$ es el que aparece multiplicando a la constante.
>
> **Ejemplo:** $\sum_{i=1}^{5} 7 = 7 \cdot (5 - 1 + 1) = 7 \cdot 5 = 35$; y $\sum_{i=0}^{n} 1 = n + 1$.

> [!success] ✅ Separación del intervalo
>
> Para $a \le b < c$:
>
> $$\sum_{i=a}^{c} f(i) = \sum_{i=a}^{b} f(i) + \sum_{i=b+1}^{c} f(i).$$
>
> **Por qué importa:** es el análogo de la aditividad de la integral: permite partir una suma larga en trozos, cambiar de sentido de recorrido o tratar por separado dos tramos con fórmulas distintas.
>
> **Ejemplo:** $\sum_{i=1}^{5} i = \sum_{i=1}^{2} i + \sum_{i=3}^{5} i = 3 + 12 = 15$ ✓

---

## 🧮 Manipulaciones avanzadas

> [!example] 🔢 Cambio de índice
>
> Si se sustituye $j = i + k$ (con $k$ constante), entonces $i = j - k$ y los límites se desplazan igual:
>
> $$\sum_{i=a}^{b} f(i) = \sum_{j=a+k}^{b+k} f(j-k).$$
>
> **Ejemplo:** con $k = 1$, $\sum_{i=1}^{3} i^2 = \sum_{j=2}^{4} (j-1)^2 = 1^2 + 2^2 + 3^2 = 14$.
>
> **Por qué importa:** el cambio de índice sirve para alinear dos sumatorias que empiezan en distinto punto, y es el paso clave del método telescópico.

> [!example] 🔢 Inversión del orden
>
> $$\sum_{i=a}^{b} f(i) = \sum_{i=a}^{b} f(a + b - i).$$
>
> La suma no cambia si se recorre "al revés": el primer término pasa a ser el último y viceversa.
>
> **Por qué importa:** es la herramienta clásica para demostrar identidades que parecen imposibles; basta sumar la expresión original con su versión invertida.

> [!example] 🔢 Sumatorias dobles
>
> $$\sum_{i=1}^{n} \sum_{j=1}^{m} f(i,j) = \sum_{j=1}^{m} \sum_{i=1}^{n} f(i,j).$$
>
> **Por qué importa:** el orden de sumación se puede cambiar; en casos como $\sum\sum (i+j)$ eso convierte un producto en una suma manejable, siempre que el conjunto de índices sea un rectángulo.

> [!warning] ⚠️ Lo que NO se puede hacer
>
> - $\displaystyle\sum_{i=1}^{n} f(i)\,g(i) \neq \sum_{i=1}^{n} f(i) \cdot \sum_{i=1}^{n} g(i)$: el producto no se reparte.
> - $\displaystyle\frac{\sum f(i)}{\sum g(i)} \neq \sum \frac{f(i)}{g(i)}$: lo mismo con los cocientes.
> - $\displaystyle\sum_{i=1}^{n} c \neq c$ sino $c \cdot n$: la constante no se "anula" al sumar.
>
> **Por qué importa:** son las tres operaciones que la sumatoria **no** respeta; confundirlas con la linealidad arruina ejercicios de límites y series.

---

## 📚 Fórmulas básicas para memorizar

> [!info] 📋 Las cinco fórmulas que más se usan
>
> | Fórmula | Expresión | Resultado |
> |---|---|---|
> | Suma de enteros | $\sum_{i=1}^{n} i$ | $\dfrac{n(n+1)}{2}$ |
> | Suma de cuadrados | $\sum_{i=1}^{n} i^2$ | $\dfrac{n(n+1)(2n+1)}{6}$ |
> | Suma de cubos | $\sum_{i=1}^{n} i^3$ | $\left[\dfrac{n(n+1)}{2}\right]^2$ |
> | Suma geométrica | $\sum_{i=0}^{n} r^{\,i}$ | $\dfrac{1 - r^{\,n+1}}{1-r}$, con $r \neq 1$ |
> | Suma de constantes | $\sum_{i=1}^{n} c$ | $c \cdot n$ |
>
> **Por qué importa:** conviene tenerlas a mano, pero conviene aún más **verificarlas con $n$ pequeño**: para $n = 4$, $\sum i = 10 = \frac{4 \cdot 5}{2}$ ✓ y $\sum i^2 = 30 = \frac{4 \cdot 5 \cdot 9}{6}$ ✓.

---

## 🎯 Aplicaciones en cálculo

> [!info] 🖼️ De la sumatoria a la integral
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Propiedades_de_la_Sumatoria_02.svg]]
>
> **Se lee así:** es una **cadena recta de rectángulos** sin bifurcaciones: se parte de la aplicación en la suma de Riemann, se particiona el intervalo, se calculan el ancho y el punto de evaluación, se obtiene el aporte de cada tramo, se suman todos los aportes y, al pasar al límite, se llega a la integral.
>
> **Por qué importa:** la integral definida aparece como **el límite de un proceso de aproximación**, no como un misterio. Así entiendes por qué el método numérico y el método por antiderivadas llegan al mismo resultado.
>
> **Ejemplo:** para aproximar $\int_0^1 x^2\,dx$ con $n = 2$, el diagrama da $\Delta x = 0.5$ y $x_i = 0.5, 1$, y la suma $0.5(0.25 + 1) = 0.625$ se acerca al valor exacto $\frac{1}{3}$.

> [!example] 🎯 Los tres terrenos de uso
>
> - **Sumas de Riemann:** $\displaystyle\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x_i$.
> - **Series:** la sumatoria con $b \to \infty$ define una serie; de ahí salen convergencia y divergencia.
> - **Límites:** expresar un límite como sumatoria (o al revés) es la técnica estándar de la Unidad 2.
>
> **Por qué importa:** las mismas propiedades sirven en los tres casos; reconocer cuál de ellas aplica es lo que acelera el ejercicio.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco fallos típicos
>
> 1. **Contar mal los términos:** son $b - a + 1$, no $b - a$.
> 2. **Cambiar de índice sin mover los límites:** si $j = i + k$, arriba y abajo se suman $k$.
> 3. **Repartir el producto:** $\sum f g \neq \sum f \cdot \sum g$.
> 4. **Olvidar los signos alternados:** en $\sum (-1)^i f(i)$ el primer término decide la paridad de toda la suma.
> 5. **No verificar con un caso pequeño:** casi ningún error de índices sobrevive a una comprobación con $n = 2$.
>
> **Por qué importa:** los cinco son errores de manipulación que se corrigen con un hábito: *cuenta los términos y comprueba con $n$ pequeño antes de continuar*.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\sum_{i=1}^{6} (4i + 2)$ usando las propiedades de linealidad.
>
> > [!success]- ✅ Solución
> >
> > Se separa la suma y se saca la constante:
> >
> > $$\sum_{i=1}^{6} (4i + 2) = 4\sum_{i=1}^{6} i + \sum_{i=1}^{6} 2 = 4\cdot\frac{6 \cdot 7}{2} + 2 \cdot 6 = 84 + 12 = 96.$$
> >
> > **Respuesta:** $96$.
> >
> > Verificación directa: $6 + 10 + 14 + 18 + 22 + 26 = 96$ ✓

> [!example] 📋 Planteamiento
>
> Aplica la fórmula de suma de cuadrados para hallar $\sum_{i=1}^{10} i^2$.
>
> > [!success]- ✅ Solución
> >
> > Con $n = 10$:
> >
> > $$\sum_{i=1}^{10} i^2 = \frac{10 \cdot 11 \cdot 21}{6} = \frac{2310}{6} = 385.$$
> >
> > **Respuesta:** $385$.
> >
> > Comprobación con los primeros términos: $1 + 4 + 9 + 16 + 25 = 55$ y la fórmula con $n = 5$ da $\frac{5 \cdot 6 \cdot 11}{6} = 55$ ✓

> [!example] 📋 Planteamiento
>
> Reescribe $\sum_{i=3}^{7} i^2$ como una sumatoria con índice $j$ que empiece en $j = 1$.
>
> > [!success]- ✅ Solución
> >
> > Se toma $j = i - 2$, es decir $i = j + 2$. Los límites se desplazan lo mismo: $i = 3 \to j = 1$ e $i = 7 \to j = 5$.
> >
> > $$\sum_{i=3}^{7} i^2 = \sum_{j=1}^{5} (j+2)^2.$$
> >
> > **Respuesta:** $\sum_{j=1}^{5} (j+2)^2$, y efectivamente $3^2 + 4^2 + 5^2 + 6^2 + 7^2 = 135 = 9 + 16 + 25 + 36 + 49$ ✓

> [!example] 📋 Planteamiento
>
> Parte $\sum_{i=1}^{9} i$ en dos sumatorias que empiecen en $i = 1$ y $i = 6$, y comprueba el resultado.
>
> > [!success]- ✅ Solución
> >
> > Por separación del intervalo:
> >
> > $$\sum_{i=1}^{9} i = \sum_{i=1}^{5} i + \sum_{i=6}^{9} i = \frac{5 \cdot 6}{2} + (6 + 7 + 8 + 9) = 15 + 30 = 45.$$
> >
> > **Respuesta:** $45$, y la fórmula completa confirma: $\frac{9 \cdot 10}{2} = 45$ ✓

> [!example] 📋 Planteamiento
>
> Calcula la suma geométrica $\sum_{i=0}^{5} 2^{\,i}$.
>
> > [!success]- ✅ Solución
> >
> > Con $r = 2$ y $n = 5$:
> >
> > $$\sum_{i=0}^{5} 2^{\,i} = \frac{1 - 2^{6}}{1 - 2} = \frac{1 - 64}{-1} = 63.$$
> >
> > **Respuesta:** $63$.
> >
> > Verificación directa: $1 + 2 + 4 + 8 + 16 + 32 = 63$ ✓

> [!example] 📋 Planteamiento
>
> Argumenta por qué $\sum_{i=1}^{n} \sum_{j=1}^{n} (i + j)$ se simplifica cambiando el orden de sumación.
>
> > [!success]- ✅ Solución
> >
> > Se reparte la suma interior: $\sum_{j=1}^{n}(i+j) = i \cdot n + \sum_{j=1}^{n} j = in + \frac{n(n+1)}{2}$.
> >
> > Sumando ahora respecto de $i$:
> >
> > $$\sum_{i=1}^{n} \left(in + \frac{n(n+1)}{2}\right) = n\cdot\frac{n(n+1)}{2} + n\cdot\frac{n(n+1)}{2} = n^2(n+1).$$
> >
> > **Respuesta:** $n^2(n+1)$; con $n = 2$ la suma directa da $2 + 3 + 3 + 4 = 12 = 4 \cdot 3$ ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico los cinco componentes de la notación sigma y cuento sus términos con $b - a + 1$.
> - [ ] Aplico la linealidad para sacar constantes y separar sumas.
> - [ ] Resuelvo los casos especiales: suma vacía, un solo término e índice negativo.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Uso las fórmulas de $\sum i$, $\sum i^2$ e $\sum i^3$ y las verifico con un valor pequeño.
> - [ ] Cambio de índice ajustando correctamente los límites de la sumatoria.
> - [ ] Parto una sumatoria en dos intervalos consecutivos y compruebo el resultado.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Explico por qué el producto no se reparte en una sumatoria y doy un contraejemplo.
> - [ ] Escribo una suma de Riemann como sumatoria y tomo su límite para obtener una integral.
> - [ ] Resuelvo identidades usando la inversión del orden o el método telescópico.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 5: sumas de Riemann y notación sigma.
> - R. Larson, *Cálculo* (Cengage), cap. 5: propiedades de la sumatoria.
> - K. Knopp, *Theory and Application of Infinite Series* (Dover): manipulaciones de series.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — el destino final de estas sumas.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — donde la sumatoria se encuentra con el límite.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — lo que hace calculable el límite de la suma.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuántos términos tiene $\sum_{i=a}^{b} f(i)$?::$b - a + 1$: ese "más uno" es el que se olvida al contar.
> - ¿Qué dice la linealidad de la sumatoria?::Las constantes salen ($\sum c f(i) = c \sum f(i)$) y las sumas se reparten ($\sum [f+g] = \sum f + \sum g$).
> - ¿Cuál es la suma de los primeros $n$ enteros?::$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$; la de sus cuadrados, $\frac{n(n+1)(2n+1)}{6}$.
> - ¿Qué pasa si el límite inferior es mayor que el superior?::La sumatoria vale $0$ por convención: es la **suma vacía**.
> - ¿Cómo se cambia de índice con $j = i + k$?::Se reemplaza $i = j - k$ en el término general **y** se desplazan los límites $k$ unidades.
> - ¿Se reparte el producto en una sumatoria?::No: $\sum f(i)g(i) \neq \sum f(i) \cdot \sum g(i)$; solo se reparte la suma y la multiplicación por constantes.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la sumatoria de rectángulos cuyo límite da la integral.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — las propiedades análogas en el mundo integral.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el teorema que convierte esa suma en un cálculo práctico.
> - [[Unidad 6 - Integrales/V - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] — métodos numéricos construidos sobre estas sumas.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — el límite de sucesiones que aquí se suma.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — donde la suma se convierte en resultado numérico.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: linealidad y fórmula de cuadrados deben salirte sin vacilar.
> - Después salta al 3 y al 4, donde los índices y los límites son la dificultad real.
> - Cuando lo tengas, ataca el 5 (geométrica) y el 6 (doble sumatoria), que son los que aparecen en series.
> - Cierra con [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|Integral de Riemann]]: ahí verás estas mismas sumas convertirse en el área bajo una curva.

---

**Tags:** #MATG1045 #unidad6 #propiedades-sumatoria #notacion-sigma #sumas-teorema #linealidad #cambio-indice #sumas-riemann

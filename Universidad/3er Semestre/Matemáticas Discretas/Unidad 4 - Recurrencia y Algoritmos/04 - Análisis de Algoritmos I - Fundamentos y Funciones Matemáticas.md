---
dg-publish: true
---
# 📈 Análisis de Algoritmos I — Fundamentos y Funciones Matemáticas

> [!info] 💡 De qué trata esta nota
> 
> Aquí el punto de partida es una **fórmula $f(n)$ ya dada explícitamente** (como $f(n) = 2n^2-5n+3$) y el trabajo es puramente algebraico: identificar el término dominante y, si se pide demostrar, exhibir $c_1$, $c_2$ y $n_0$. Es la **primera de dos partes**; la segunda, [[05 - Análisis de Algoritmos II - Pseudocódigo y Tiempo Real]], cubre cómo obtener las cotas contando operaciones en pseudocódigo.

## 🔵 Definiciones Formales

> [!note] 📋 Definiciones (como las plantea la clase)
> 
> Sea $f(n)$ el número de operaciones de un algoritmo. La definición que usa el profesor Pineda usa **valor absoluto** y la frase "excepto una cantidad finita de valores de $n$" (equivalente a "$\forall n \geq n_0$"):
> 
> - **Cota superior $\mathcal{O}$:** $f(n) = \mathcal{O}(g(n))$ si existe una constante $C_1>0$ tal que $|f(n)| \leq C_1|g(n)|$, para todo $n \in \mathbb{N}$, excepto una cantidad finita de valores de $n$.
>     
> - **Cota inferior $\Omega$:** $f(n) = \Omega(g(n))$ si existe una constante $C_2>0$ tal que $|f(n)| \geq C_2|g(n)|$, para todo $n \in \mathbb{N}$, excepto una cantidad finita de valores de $n$.
>     
> - **Cota estrecha $\Theta$:** $f(n) = \Theta(g(n))$ si $f(n) = \mathcal{O}(g(n))$ **y** $f(n) = \Omega(g(n))$.
>     
> 
> > [!tip] 📌 Intuición rápida
> > 
> > - $\mathcal{O}$ → cota máxima ("a lo sumo crece así")
> > - $\Omega$ → cota mínima ("al menos crece así")
> > - $\Theta$ → crecimiento exacto ("crece exactamente así")

## 🟢 El Atajo de Polinomios (el más común)

> [!note] 📋 Regla rápida
> 
> Si $p(n) = a_k n^k + a_{k-1}n^{k-1} + \cdots + a_0$ con $a_k \neq 0$, entonces $p(n) = \Theta(n^k)$: el [[01 - Grafos I - Conceptos Básicos y Recorridos|grado]] del polinomio determina directamente la cota estrecha. Para una **[[01 - Funciones|función]] racional** $\dfrac{p(n)}{q(n)}$, se comparan los grados de numerador y denominador: $\Theta!\left(n^{\deg p - \deg q}\right)$.
> 
> Este atajo basta para responder rápido, pero cuando el ejercicio pide **"estudiar" o "demostrar"** la función, hay que exhibir $c_1$, $c_2$ y $n_0$ explícitos (ver técnica abajo).

> [!success] ✅ Los coeficientes líderes negativos NO son un problema
> 
> **Teorema.** Cualquier polinomio en $n$ de grado $k$ es $\Theta(n^k)$, **aun cuando algunos de sus coeficientes sean negativos** (incluido el líder).
> 
> La razón es que la definición formal usa **valor absoluto**: $|f(n)| \leq C_1|g(n)|$. Aunque $f(n)=-4n^3+n^2-5n$ se vuelve negativa para $n$ grande, $|f(n)|$ se comporta como $4n^3$, así que $f(n)=\Theta(n^3)$ sin ninguna salvedad.

## 🎓 Cuándo Piden Demostrar de Verdad ($c_1$, $c_2$, $n_0$ explícitos)

> [!example] 🟢 Ejemplo completo — Estudiar $f(n) = 2n^2 - 5n + 3,\ \forall n \in \mathbb{N}$
> 
> **Objetivo:** demostrar que $f(n) = \Theta(n^2)$, exhibiendo $c_1$, $c_2$ y $n_0$.
> 
> **Paso 1 — Cota superior ($\mathcal{O}$):**
> 
> Para $n \geq 1$, se cumple $3 \leq 3n^2$, entonces:
> 
> $$f(n) = 2n^2 - 5n + 3 \leq 2n^2 + 3 \leq 2n^2 + 3n^2 = 5n^2$$
> 
> Es decir, $f(n) \leq 5n^2$ para todo $n \geq 1$ → $f(n) = \mathcal{O}(n^2)$ con $c_1 = 5$, $n_0 = 1$.
> 
> **Paso 2 — Cota inferior ($\Omega$):**
> 
> Buscamos $c_2$ tal que $f(n) \geq c_2 n^2$. Probamos con $c_2 = 1$:
> 
> $$2n^2 - 5n + 3 \geq n^2 \iff n^2 - 5n + 3 \geq 0$$
> 
> Resolviendo $n^2-5n+3=0$, las raíces son $n = \dfrac{5\pm\sqrt{13}}{2} \approx 0{,}70$ y $4{,}30$. La parábola es positiva fuera de ese intervalo, así que para todo entero $n \geq 5$ se cumple $n^2-5n+3\geq 0$.
> 
> Por lo tanto, $f(n) \geq n^2$ para todo $n \geq 5$ → $f(n) = \Omega(n^2)$ con $c_2 = 1$, $n_0 = 5$.
> 
> **Paso 3 — Conclusión:**
> 
> Como ambas cotas valen simultáneamente a partir de $n_0 = 5$:
> 
> $$n^2 \leq f(n) \leq 5n^2 \quad \text{para todo } n \geq 5 \quad\implies\quad f(n) = \Theta(n^2) \quad \blacksquare$$
> 
> > [!tip]- 💡 Truco para elegir $c_1$ rápido
> > 
> > En la cota superior, basta con **sobreestimar** cada término negativo o de menor grado por un múltiplo del término dominante (aquí, $3 \leq 3n^2$ para $n\geq1$). No hace falta encontrar la constante más ajustada — cualquier $c_1$ que funcione es válida.

---

## ✏️ Ejercicios de Clase — Notación Θ de Polinomios

> [!question] 📋 Encuentra la notación Θ para cada función (clase del 16/07, Ebner Pineda)
> 
> **1.** $f(n) = -4n^3 + n^2 - 5n,\ \forall n \in \mathbb{N}$
> 
> **2.** $f(n) = -\dfrac{5}{3}n^2 + 7n + 8,\ \forall n \in \mathbb{N}$
> 
> **3.** $f(n) = \dfrac{3}{4}n^3 - 4n^2 - 7n,\ \forall n \in \mathbb{N}$
> 
> **4.** $f(n) = \dfrac{5n^3 + 3\log n}{2 + 7n}$

> [!tip] 📌 El método real: primero $\mathcal{O}$, luego $\Omega$, y si coinciden → $\Theta$
> 
> El atajo del grado dominante te da la respuesta rápido, pero **demostrarla** — que es como se resuelven estos ejercicios en realidad — exige el mismo procedimiento de tres pasos cada vez: (1) exhibir una cota superior $c_1g(n)$, (2) exhibir una cota inferior $c_2g(n)$, (3) si ambas usan la misma $g(n)$, concluir $\Theta(g(n))$.

> [!success] ✅ 1. $f(n)=-4n^3+n^2-5n \implies \Theta(n^3)$
> 
> El coeficiente líder es negativo, así que trabajamos con $|f(n)|$.
> 
> Factorizando, $f(n)=-n(4n^2-n+5)$; como $4n^2-n+5>0$ siempre (discriminante negativo) y $n>0$, se tiene $f(n)<0,\ \forall n\geq1$ → $|f(n)|=4n^3-n^2+5n$.
> 
> **Cota superior:** quitando el término negativo $-n^2$ (solo puede agrandar) y usando $n\leq n^3$ (para $n\geq1$):
> 
> $$|f(n)| \leq 4n^3+5n \leq 4n^3+5n^3 = 9n^3, \quad\forall n\geq1$$
> 
> → $f(n)=\mathcal{O}(n^3)$ con $c_1=9$, $n_0=1$.
> 
> **Cota inferior:** quitando el término positivo $5n$ (solo puede achicar) y usando $n^2\leq n^3$:
> 
> $$|f(n)| \geq 4n^3-n^2 \geq 4n^3-n^3 = 3n^3, \quad\forall n\geq1$$
> 
> → $f(n)=\Omega(n^3)$ con $c_2=3$, $n_0=1$.
> 
> **Conclusión:** $3n^3\leq|f(n)|\leq9n^3,\ \forall n\geq1 \implies f(n)=\Theta(n^3)$. $\blacksquare$

> [!tip] 💡 Los "trucos" detrás del ejercicio 1, paso a paso
> 
> Demostrar formalmente la complejidad de un algoritmo consiste en acotar la función entre dos extremos: una cota superior (el peor escenario, $\mathcal{O}$) y una cota inferior (el mejor escenario, $\Omega$). Así se llega a cada constante del ejercicio anterior.
> 
> **① ¿Por qué $9n^3$ en la cota superior?**
> 
> El objetivo es encontrar una función de un solo término que sea siempre $\geq |f(n)| = 4n^3-n^2+5n$ para $n\geq1$, agrandando la expresión con dos trucos válidos:
> 
> - _Eliminar lo que resta:_ quitar un término negativo solo puede agrandar el resultado. $$4n^3-n^2+5n \leq 4n^3+5n$$
> - _Homogeneizar potencias:_ como $n\leq n^3$ para $n\geq1$ (p. ej. $n=2\Rightarrow2\leq8$), se reemplaza la potencia menor por la mayor, lo que agranda de nuevo: $$4n^3+5n \leq 4n^3+5n^3$$
> - _Resultado:_ con ambos términos ya en $n^3$, se suman directamente: $$4n^3+5n^3 = 9n^3$$
> 
> El $9$ es entonces $c_1$: la constante que surge de este proceso de "agrandar con seguridad", y demuestra que $|f(n)|$ nunca supera a $9n^3$.
> 
> **② ¿Por qué $3n^3$ en la cota inferior?**
> 
> Aquí el objetivo es opuesto: encontrar una función de un solo término que sea siempre $\leq|f(n)|$, "achicando" la expresión:
> 
> - _Eliminar lo que suma:_ quitar un término positivo solo puede achicar el resultado. $$4n^3-n^2+5n \geq 4n^3-n^2$$
> - _Restar una cantidad mayor:_ como $n^2\leq n^3$ para $n\geq1$, restar la potencia mayor en vez de la menor achica todavía más. $$4n^3-n^2 \geq 4n^3-n^3$$
> - _Resultado:_ $$4n^3-n^3 = 3n^3$$
> 
> Esto da $c_2=3$ y demuestra que $|f(n)|$ nunca cae por debajo de $3n^3$.
> 
> **③ Por qué eso implica $\Theta(n^3)$**
> 
> Juntando ambas cotas se obtiene la desigualdad sándwich $3n^3\leq|f(n)|\leq9n^3,\ \forall n\geq1$. Como la función queda atrapada entre dos funciones de orden cúbico, su velocidad de crecimiento es exactamente $\Theta(n^3)$ — ni más rápida que $9n^3$ ni más lenta que $3n^3$.
> 
> Este mismo patrón de "agrandar quitando restas / homogeneizando potencias hacia arriba" y "achicar quitando sumas / homogeneizando potencias hacia abajo" es el que se reutiliza en los ejercicios 2, 3 y 4.

> [!success] ✅ 2. $f(n)=-\frac{5}{3}n^2+7n+8 \implies \Theta(n^2)$
> 
> **Cota superior:** por la desigualdad del triángulo,
> 
> $|f(n)|\leq\frac{5}{3}n^2+7n+8$. Para $n\geq1$: $7n\leq7n^2$ y $8\leq8n^2$, entonces:
> 
> $$|f(n)| \leq \frac{5}{3}n^2+7n^2+8n^2 = \frac{50}{3}n^2, \quad\forall n\geq1$$
> 
> → $f(n)=\mathcal{O}(n^2)$ con $c_1=\frac{50}{3}$, $n_0=1$.
> 
> **Cota inferior:** para $n$ suficientemente grande, $-\frac{5}{3}n^2$ domina y $f(n)<0$, así que $|f(n)|=\frac{5}{3}n^2-7n-8$. Con $c_2=1$:
> 
> $$\frac{5}{3}n^2-7n-8\geq n^2 \iff \frac{2}{3}n^2-7n-8\geq0$$
> 
> Resolviendo $2n^2-21n-24=0$, la raíz positiva es $n\approx11{,}54$, así que para todo entero $n\geq12$ se cumple la desigualdad → $f(n)=\Omega(n^2)$ con $c_2=1$, $n_0=12$.
> 
> **Conclusión:** $n^2\leq|f(n)|\leq\frac{50}{3}n^2,\ \forall n\geq12 \implies f(n)=\Theta(n^2)$. $\blacksquare$

> [!tip] 💡 Los "trucos" detrás del ejercicio 2, paso a paso
> 
> **① ¿Por qué $\frac{50}{3}n^2$ en la cota superior?**
> 
> Aquí no se puede usar el truco de "quitar el término que resta", porque el término que resta es justo el líder ($-\frac{5}{3}n^2$) — quitarlo eliminaría la potencia dominante. En su lugar se usa la **desigualdad del triángulo** ($|a-b+c|\leq|a|+|b|+|c|$), que agranda de un solo golpe pasando cada término a su valor absoluto: $$|f(n)| \leq \tfrac{5}{3}n^2+7n+8$$ Luego se homogeneiza cada término suelto multiplicándolo hacia $n^2$ (válido para $n\geq1$: $7n\leq7n^2$, $8\leq8n^2$): $$\tfrac{5}{3}n^2+7n^2+8n^2 = \tfrac{50}{3}n^2$$ $c_1=\frac{50}{3}$ es simplemente la suma de los tres coeficientes ya homogeneizados — no es la constante más ajustada posible, pero es válida.
> 
> **② ¿Por qué $n^2$ (con $n_0=12$) en la cota inferior?**
> 
> Como el coeficiente líder es negativo, $f(n)$ termina siendo negativo para $n$ grande — hay que confirmarlo antes de trabajar con $|f(n)|=\frac{5}{3}n^2-7n-8$. A diferencia del ejercicio 1 (donde $n^2\leq n^3$ da una cota inferior _inmediata_), aquí restar $7n+8$ de $\frac{5}{3}n^2$ no deja una potencia limpia: hay que **resolver una desigualdad cuadrática** ($\frac{2}{3}n^2-7n-8\geq0$) para encontrar a partir de qué $n_0$ el sobrante ($\frac{5}{3}n^2-n^2=\frac{2}{3}n^2$) alcanza a cubrir los términos que se restaron. Por eso $n_0=12$ es más grande que en el ejercicio 1: la "distancia" entre $\frac{5}{3}n^2$ y $n^2$ es más chica, así que se necesita un $n$ mayor para que la potencia cuadrática gane.
> 
> **③ Conclusión:** $n^2\leq|f(n)|\leq\frac{50}{3}n^2$ para $n\geq12$ atrapa a $f(n)$ entre dos funciones de orden $n^2$ → $\Theta(n^2)$.

> [!success] ✅ 3. $f(n)=\frac{3}{4}n^3-4n^2-7n \implies \Theta(n^3)$
> 
> **Cota superior:** para $n\geq1$: $4n^2+7n\leq11n^2\leq11n^3$, entonces:
> 
> $$f(n) \leq \frac{3}{4}n^3+11n^3 < 12n^3, \quad\forall n\geq1$$
> 
> → $f(n)=\mathcal{O}(n^3)$ con $c_1=12$, $n_0=1$.
> 
> **Cota inferior:** para $n$ suficientemente grande (se verifica con $n_0=20$):
> 
> $$\frac{3}{4}n^3-4n^2-7n \geq \frac{1}{2}n^3$$
> 
> → $f(n)=\Omega(n^3)$ con $c_2=\frac12$, $n_0=20$.
> 
> **Conclusión:** $\frac12n^3\leq f(n)\leq12n^3,\ \forall n\geq20 \implies f(n)=\Theta(n^3)$. $\blacksquare$

> [!tip] 💡 Los "trucos" detrás del ejercicio 3, paso a paso
> 
> **① ¿Por qué $12n^3$ en la cota superior?**
> 
> Aquí no se necesita valor absoluto: como el término dominante $\frac{3}{4}n^3$ es positivo, basta con acotar $f(n)$ directamente (sin las barras $|\cdot|$), porque $-4n^2-7n \leq 4n^2+7n$ sin importar el signo. Se homogeneiza sumando los términos restantes hacia $n^3$ (para $n\geq1$: $4n^2+7n\leq4n^2+7n^2=11n^2\leq11n^3$): $$f(n) \leq \tfrac{3}{4}n^3+11n^3 < 12n^3$$ El $12$ sale de redondear $\frac{3}{4}+11=11{,}75$ hacia arriba para tener una constante entera y cómoda — no hace falta que sea exacta, solo válida.
> 
> **② ¿Por qué $\frac12n^3$ (con $n_0=20$) en la cota inferior?**
> 
> A diferencia de los ejercicios anteriores, aquí **no** se elimina un término entero (como se hizo con $-n^2$ o $+5n$ en el ejercicio 1); en vez de eso se le "presta" una fracción del término dominante a los términos que restan. La idea es demostrar que $4n^2+7n$ nunca consume más de un cuarto de $n^3$: $$\tfrac{3}{4}n^3-4n^2-7n \geq \tfrac{1}{2}n^3 \iff \tfrac{1}{4}n^3 \geq 4n^2+7n$$ Para $n$ chico esto falla ($4n^2+7n$ crece más rápido al inicio), pero como $n^3$ termina dominando a $n^2$ y $n$, existe un punto de quiebre — aquí, $n_0=20$ — a partir del cual la desigualdad se cumple siempre. Elegir $c_2=\frac12$ (en vez de un valor más ajustado) simplemente hace más fácil verificar el $n_0$.
> 
> **③ Conclusión:** $\frac12n^3\leq f(n)\leq12n^3$ para $n\geq20$ → $\Theta(n^3)$.

> [!success] ✅ 4. $f(n)=\dfrac{5n^3+3\log n}{2+7n} \implies \Theta(n^2)$
> 
> Para funciones racionales, la dirección de la desigualdad se invierte entre numerador y denominador: agrandar el numerador exige achicar el denominador, y viceversa.
> 
> **Cota superior:** agrandamos el numerador y achicamos el denominador. Usando $\log n\leq n-1\leq n\leq n^3$ (para $n\geq1$):
> 
> $$5n^3+3\log n \leq 5n^3+3n^3 = 8n^3$$
> 
> Y $2+7n\geq7n$ (se quita la constante positiva). Entonces:
> 
> $$f(n) \leq \frac{8n^3}{7n} = \frac{8}{7}n^2, \quad\forall n\geq1$$
> 
> → $f(n)=\mathcal{O}(n^2)$ con $c_1=\frac{8}{7}$, $n_0=1$.
> 
> **Cota inferior:** achicamos el numerador y agrandamos el denominador. Como $\log n\geq0$ para $n\geq1$:
> 
> $$5n^3+3\log n \geq 5n^3$$
> 
> Y $2+7n\leq2n+7n=9n$ (usando $2\leq2n$). Entonces:
> 
> $$f(n) \geq \frac{5n^3}{9n} = \frac{5}{9}n^2, \quad\forall n\geq1$$
> 
> → $f(n)=\Omega(n^2)$ con $c_2=\frac{5}{9}$, $n_0=1$.
> 
> **Conclusión:** $\frac{5}{9}n^2\leq f(n)\leq\frac{8}{7}n^2,\ \forall n\geq1 \implies f(n)=\Theta(n^2)$. $\blacksquare$

> [!tip] 💡 Los "trucos" detrás del ejercicio 4, paso a paso
> 
> Este caso es distinto a los tres anteriores porque $f(n)$ es una **fracción** $\dfrac{p(n)}{q(n)}$, no un polinomio. En una fracción, agrandar y achicar se comportan al revés en numerador y denominador: una fracción crece si el numerador crece **o** si el denominador se achica, y viceversa.
> 
> **① ¿Por qué $\frac{8}{7}n^2$ en la cota superior?**
> 
> Para que la fracción sea lo más grande posible, se **agranda el numerador** y se **achica el denominador** al mismo tiempo:
> 
> - Numerador: $\log n \leq n$ (para $n\geq1$, el logaritmo siempre crece más lento que $n$), y luego $n\leq n^3$, así que $3\log n\leq3n^3$: $$5n^3+3\log n \leq 5n^3+3n^3 = 8n^3$$
> - Denominador: se **quita** la constante positiva $+2$ (quitar algo que suma solo puede achicar): $$2+7n \geq 7n$$
> - Al dividir un numerador más grande entre un denominador más chico, la fracción completa queda sobreestimada: $$f(n) \leq \frac{8n^3}{7n} = \frac{8}{7}n^2$$
> 
> **② ¿Por qué $\frac{5}{9}n^2$ en la cota inferior?**
> 
> Para que la fracción sea lo más pequeña posible, se hace exactamente lo contrario: se **achica el numerador** y se **agranda el denominador**:
> 
> - Numerador: como $\log n\geq0$ para $n\geq1$, quitarlo del todo solo puede achicar: $$5n^3+3\log n \geq 5n^3$$
> - Denominador: se **agranda** reemplazando la constante $2$ por $2n$ (válido porque $2\leq2n$ para $n\geq1$), y se suma al término existente: $$2+7n \leq 2n+7n = 9n$$
> - Numerador más chico entre denominador más grande da una fracción subestimada: $$f(n) \geq \frac{5n^3}{9n} = \frac{5}{9}n^2$$
> 
> **③ Conclusión:** el patrón clave para recordar en funciones racionales es que **agrandar la fracción = agrandar arriba + achicar abajo**, y **achicar la fracción = achicar arriba + agrandar abajo** — lo contrario de la intuición con polinomios sueltos. Como ambas cotas coinciden en $n^2$ (porque el grado 3 del numerador menos el grado 1 del denominador da $3-1=2$, tal como predice el atajo de la sección "El Atajo de Polinomios"), se confirma $f(n)=\Theta(n^2)$.

---

## 🎓 Herramienta: El Piso ($\lfloor\cdot\rfloor$) No Cambia el Orden de Crecimiento

> [!info] 💡 Por qué esto va aquí
> 
> Esta herramienta aparece **textualmente** como sugerencia en los talleres (ej. Taller III: _"Sugerencia: $x-1<\lfloor x\rfloor\leq x,\ \forall x\in\mathbb{R}$"_), y es la pieza que permite tratar valores iniciales como $\lfloor 7\sqrt{n}\rfloor$ o $\lfloor\log(5n)\rfloor$ igual que su versión sin piso. Se usa constantemente en los ejercicios de conteo de operaciones de [[05 - Análisis de Algoritmos II - Pseudocódigo y Tiempo Real]].

> [!tip] 📌 Lema
> 
> $$x - 1 < \lfloor x \rfloor \leq x, \quad \forall x \in \mathbb{R}$$
> 
> Es decir, $\lfloor x\rfloor$ nunca supera a $x$, y nunca es menor que $x-1$ — la diferencia siempre es menor que $1$, sin importar qué tan grande sea $x$. Por eso, **para efectos de $\mathcal{O}, \Omega, \Theta$, puedes tratar $\lfloor x\rfloor$ como si fuera $x$**: $\lfloor x\rfloor = \Theta(x)$ siempre que $x$ crezca (el mismo argumento aplica al techo $\lceil x\rceil$, con $x\leq\lceil x\rceil<x+1$).

> [!example] 🟢 Por qué esa diferencia de "menos de 1" nunca importa para $\Theta$
> 
> ¿Cambia el resultado si en vez de $\sqrt{n}$ tu algoritmo usa $\lfloor\sqrt{n}\rfloor$? No. Con $x=\sqrt{n}$: $\sqrt{n}-1 < \lfloor\sqrt{n}\rfloor \leq \sqrt{n}$. La cota superior da $\lfloor\sqrt{n}\rfloor=\mathcal{O}(\sqrt{n})$ de inmediato. Para la cota inferior, con $n\geq4$ se cumple $\sqrt{n}-1\geq\frac{1}{2}\sqrt{n}$ (verifica con $n=4$: $2-1=1\geq1$ ✅), entonces $\lfloor\sqrt{n}\rfloor=\Omega(\sqrt{n})$.
> 
> Conclusión: $\lfloor\sqrt{n}\rfloor=\Theta(\sqrt{n})$ — igual que sin el piso. El mismo argumento funciona para **cualquier** función creciente: $\lfloor 7\sqrt{n}\rfloor=\Theta(\sqrt{n})$, $\lfloor\log(5n)\rfloor=\Theta(\log n)$, etc.

---

## 🎯 Ejercicio Extra — Cuatro Casos que No Aparecieron Arriba

> [!question] 📋 Por qué este ejercicio
> 
> Los ejercicios 1–4 cubren polinomios (con y sin coeficiente líder negativo) y una función racional donde el numerador domina. Pero hay otras situaciones típicas que **no** aparecieron todavía y que sí pueden salir en un parcial o taller:
> 
> - **(a)** Un coeficiente enorme en un término de **menor** grado — ¿de verdad no importa?
> - **(b)** Una función con **piso** ($\lfloor\cdot\rfloor$) donde hay que usar el lema explícitamente dentro de la demostración (no solo citarlo).
> - **(c)** Una función acotada por algo que **no es una potencia pura de $n$** (aparece $\log n$ multiplicando).
> - **(d)** Una función racional donde el denominador tiene **mayor grado** que el numerador — la función _decrece_, no crece.
> 
> Cada parte usa $c_1$, $c_2$, $n_0$ explícitos, igual que los ejercicios anteriores.

> [!success] ✅ (a) $f(n) = 2n^4 - 100n^3 + 50,\ \forall n\geq1 \implies \Theta(n^4)$
> 
> **La trampa:** el $-100n^3$ tiene un coeficiente mucho más grande que el $2$ de $2n^4$. La intuición ingenua diría que "domina", pero el **grado** manda, no el coeficiente — el atajo de polinomios lo garantiza. Lo que sí cambia es **cuánto tarda** ($n_0$) en verse esa dominancia.
> 
> **Cota superior:** por la desigualdad del triángulo, $|f(n)|\leq2n^4+100n^3+50$. Homogeneizando hacia $n^4$ (para $n\geq1$: $n^3\leq n^4$, $1\leq n^4$): $$|f(n)| \leq 2n^4+100n^4+50n^4 = 152n^4$$ → $\mathcal{O}(n^4)$ con $c_1=152$, $n_0=1$.
> 
> **Cota inferior:** quitando $+50$ (achica): $f(n)\geq2n^4-100n^3$. Factorizando, $2n^4-100n^3=n^4(2-\frac{100}{n})$. Con $c_2=1$, necesitamos $2-\frac{100}{n}\geq1 \iff n\geq100$. $$f(n) \geq n^4, \quad\forall n\geq100$$ → $\Omega(n^4)$ con $c_2=1$, $n_0=100$.
> 
> **Conclusión:** $n^4\leq|f(n)|\leq152n^4,\ \forall n\geq100 \implies f(n)=\Theta(n^4)$. $\blacksquare$
> 
> El $n_0=100$ (mucho más grande que el $n_0=1$ del ejercicio 1) es precisamente el "precio" de tener un coeficiente tan grande en el término de menor grado: el $n^4$ necesita crecer más para superarlo, pero **tarde o temprano lo hace**, y eso es todo lo que $\Theta$ exige.

> [!success] ✅ (b) $f(n) = 5\lfloor\sqrt{n}\rfloor - 3,\ \forall n\geq1 \implies \Theta(\sqrt{n})$
> 
> Esta es la aplicación directa del lema $\sqrt{n}-1<\lfloor\sqrt{n}\rfloor\leq\sqrt{n}$ dentro de una prueba completa, en vez de solo invocarlo.
> 
> **Cota superior:** usando $\lfloor\sqrt{n}\rfloor\leq\sqrt{n}$ y quitando el $-3$ (achica, así que ayuda a la cota superior): $$f(n) = 5\lfloor\sqrt{n}\rfloor-3 \leq 5\sqrt{n}-3 \leq 5\sqrt{n}, \quad\forall n\geq1$$ → $\mathcal{O}(\sqrt{n})$ con $c_1=5$, $n_0=1$.
> 
> **Cota inferior:** usando la mitad estricta del lema, $\lfloor\sqrt{n}\rfloor>\sqrt{n}-1$: $$f(n) > 5(\sqrt{n}-1)-3 = 5\sqrt{n}-8$$ Con $c_2=1$: $5\sqrt{n}-8\geq\sqrt{n} \iff 4\sqrt{n}\geq8 \iff \sqrt{n}\geq2 \iff n\geq4$. $$f(n) > 5\sqrt{n}-8 \geq \sqrt{n}, \quad\forall n\geq4$$ → $\Omega(\sqrt{n})$ con $c_2=1$, $n_0=4$.
> 
> **Conclusión:** $\sqrt{n}\leq f(n)\leq5\sqrt{n},\ \forall n\geq4 \implies f(n)=\Theta(\sqrt{n})$. $\blacksquare$
> 
> La diferencia clave con los ejercicios 1–4: aquí el $-1$ del lema del piso se propaga como una constante extra ($-8$ en vez de $-3$) dentro de la cota inferior, pero como es solo una constante (no cambia con $n$), termina absorbida por el mismo tipo de argumento de siempre — solo hay que cargarla con cuidado en el álgebra.

> [!success] ✅ (c) $f(n) = n^2\log n + 3n,\ \forall n\geq2 \implies \Theta(n^2\log n)$
> 
> **La novedad:** la función de comparación $g(n)=n^2\log n$ **no es una potencia pura de $n$** — es un polinomio multiplicado por un logaritmo. Esto es muy común en análisis de algoritmos (ordenamientos basados en comparación, heapify, etc.), y se cubrirá con más detalle en la Nota II. Aquí basta con saber tratar $\log n$ como "otra variable" que crece, sin necesidad de acotarla por una potencia de $n$.
> 
> **Cota superior:** para $n\geq2$ (con $\log$ en base 2, $\log n\geq1$), y usando $n\leq n^2$: $$3n \leq 3n^2 \leq 3n^2\log n$$ $$f(n) = n^2\log n+3n \leq n^2\log n+3n^2\log n = 4n^2\log n, \quad\forall n\geq2$$ → $\mathcal{O}(n^2\log n)$ con $c_1=4$, $n_0=2$.
> 
> **Cota inferior:** quitando $+3n$ (positivo, achica): $$f(n) \geq n^2\log n, \quad\forall n\geq2$$ → $\Omega(n^2\log n)$ con $c_2=1$, $n_0=2$.
> 
> **Conclusión:** $n^2\log n \leq f(n) \leq 4n^2\log n,\ \forall n\geq2 \implies f(n)=\Theta(n^2\log n)$. $\blacksquare$
> 
> Se empieza en $n_0=2$ (no $n=1$) solo porque en $n=1$ se tendría $\log 1=0$, un caso degenerado donde "$\log n$ crece" todavía no aplica — pero la definición formal permite ignorar una cantidad finita de valores de $n$, así que esto no rompe nada.

> [!success] ✅ (d) $f(n) = \dfrac{4n+7}{n^2-1},\ \forall n\geq2 \implies \Theta!\left(\dfrac{1}{n}\right)$
> 
> **La novedad:** en el ejercicio 4, el numerador tenía **mayor** grado que el denominador ($n^3$ vs $n$) y la función crecía. Aquí es al revés — el denominador ($n^2$) tiene mayor grado que el numerador ($n$) — así que $f(n)$ **decrece** a medida que $n$ crece. El atajo de la sección de funciones racionales lo predice: $\Theta(n^{\deg p-\deg q})=\Theta(n^{1-2})=\Theta(n^{-1})=\Theta(1/n)$.
> 
> **Cota superior** (agrandar numerador, achicar denominador): numerador, usando $7\leq7n$: $$4n+7 \leq 4n+7n=11n$$ Denominador, buscando una cota inferior simple: para $n\geq2$, $n^2-1\geq\frac{n^2}{2}$ (en $n=2$: $3\geq2$ ✅, y la brecha solo crece). Dividir entre un denominador más chico agranda la fracción: $$f(n) \leq \frac{11n}{n^2/2} = \frac{22}{n}, \quad\forall n\geq2$$ → $\mathcal{O}(1/n)$ con $c_1=22$, $n_0=2$.
> 
> **Cota inferior** (achicar numerador, agrandar denominador): numerador, quitando $+7$: $$4n+7 \geq 4n$$ Denominador, quitando el $-1$ (agranda, ya que elimina una resta): $n^2-1\leq n^2$. Dividir entre un denominador más grande achica la fracción: $$f(n) \geq \frac{4n}{n^2} = \frac{4}{n}, \quad\forall n\geq2$$ → $\Omega(1/n)$ con $c_2=4$, $n_0=2$.
> 
> **Conclusión:** $\dfrac{4}{n}\leq f(n)\leq\dfrac{22}{n},\ \forall n\geq2 \implies f(n)=\Theta(1/n)$. $\blacksquare$
> 
> Nótese que "$c_1$ agranda / $c_2$ achica" sigue siendo la misma lógica de siempre — lo único distinto es que, al ser $f(n)$ decreciente, "más grande" para el numerador y "más chico" para el denominador todavía producen una cota superior, exactamente como en el ejercicio 4.

![[ChatGPT Image 18 ago 2026, 20_42_23.png]]

---

## ➡️ Continúa en la Nota II

> [!success] 📋 Siguiente paso
> 
> El siguiente paso es aprender a obtener $\mathcal{O}$, $\Omega$ y $\Theta$ **a partir de pseudocódigo** (contando operaciones en ciclos, recursión, mejor/peor/promedio caso) — eso está en [[05 - Análisis de Algoritmos II - Pseudocódigo y Tiempo Real]].

## 🔗 Conexiones

> [!note] 📋 Temas relacionados
> 
> - [[05 - Análisis de Algoritmos II - Pseudocódigo y Tiempo Real]] — segunda parte de esta nota.
> - [[03 - Pseudocódigo y Algoritmos]] — la sintaxis de los algoritmos que se analizan en la Nota II.

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
> 
> [1] E. Pineda, _Análisis de Algoritmos_, clase MATG1051, ESPOL, jul. 2026.
> 
> [2] K. H. Rosen, _Discrete Mathematics and Its Applications_, 8th ed. New York, USA: McGraw-Hill, 2019, pp. 185–210.
> 
> [3] R. Johnsonbaugh, _Discrete Mathematics_, 8th ed. Hoboken, NJ, USA: Pearson, 2018, pp. 249–268.

---


## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Defino notación O, Ω y Θ para complejidad temporal.
> - [ ] Clasifico algoritmos en O(1), O(log n), O(n), O(n log n), O(n²).
> - [ ] Cuento operaciones básicas para determinar la complejidad.

> [!note] Nivel Intermedio
> - [ ] Aplico reglas de la O grande (suma, producto, composición).
> - [ ] Comparo funciones usando límites (regla de L'Hôpital para complejidad).
> - [ ] Analizo la complejidad de algoritmos con ciclos anidados.

> [!note] Nivel Avanzado
> - [ ] Determino la complejidad exacta de algoritmos recursivos usando recurrencias.
> - [ ] Aplico teorema maestro para análisis de divide y vencerás.
> - [ ] Analizo complejidad espacial junto con la temporal.

**Tags:** #analisisdealgoritmos #notacionasintotica #bigO #complejidad #MATG1051 #unidad4 #ESPOL

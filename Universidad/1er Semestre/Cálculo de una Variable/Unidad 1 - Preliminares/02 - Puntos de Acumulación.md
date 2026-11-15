---
dg-publish: true
tags: [MATG1045, unidad1, puntos-de-acumulacion, topologia, clausura, conjuntos-cerrados, sucesiones]
---

# 📍 Puntos de Acumulación

## 🎯 Introducción

> [!info] 💡 ¿Qué idea geométrica sostiene esta nota?
>
> Un punto de acumulación no es, simplemente, un punto “cercano” a un conjunto. Es un punto al que el conjunto se acerca **arbitrariamente**, por pequeño que sea el radio que se elija. Esa diferencia entre “hay uno cerca” y “hay otros puntos a cualquier distancia” es la que separa un punto aislado de uno de acumulación.
>
> En la Unidad 2, esta idea se reutiliza para definir límites: el valor que se busca debe ser approached por puntos del dominio, sin depender del valor de la función en el punto. Por eso conviene fijar ahora la terminología exacta: acumulación, adherencia, interior, frontera y clausura.
>
> **Ejemplo:** $0$ no pertenece a $\{1/n:n\in\mathbb N\}$, pero cada bola alrededor de $0$ contiene términos de la sucesión. Por tanto, $0$ es punto de acumulación y el conjunto no es cerrado.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Punto de acumulación
>
> Sean $(X,d)$ un espacio métrico, $A\subseteq X$ y $x_0\in X$. El punto $x_0$ es un **punto de acumulación** de $A$ si para todo $r>0$,
> $$B(x_0,r)\cap(A\setminus\{x_0\})\ne\varnothing.$$
>
> Equivalentemente, $B(x_0,r)\cap A$ contiene infinitos puntos de $A$ distintos de $x_0$. No se exige que $x_0\in A$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Puntos_de_Acumulación_01.svg]]
>
> **Se lee así:** desde el punto de acumulación salen una rama de definición y otra de aplicaciones. La rama de definición abre en cercanía, infinitud y tipos de punto; la condición geométrica central es que todo entorno de $x_0$ contiene otros puntos de $A$. La rama de aplicaciones lleva a la clausura y a los límites.
>
> **Por qué importa:** el diagrama impide confundir “cercano” con “arbitrariamente cercano”. Excluir $x_0$ de la comprobación es lo que impide que cualquier punto se acumule a sí mismo.
>
> **Ejemplo:** $0$ es punto de acumulación de $(0,1)$ y de $\{1/n:n\in\mathbb N\}$, aunque ninguno de esos conjuntos contenga a $0$.

> [!note] 📋 Definición — Caracterizaciones equivalentes
>
> Para $(X,d)$, $A\subseteq X$ y $x_0\in X$, las siguientes condiciones son equivalentes:
>
> 1. $\forall r>0$, $B(x_0,r)\cap(A\setminus\{x_0\})\ne\varnothing$.
> 2. Existe $(x_n)\subseteq A\setminus\{x_0\}$ con $x_n\to x_0$.
> 3. Para todo $r>0$, $(B(x_0,r)\cap A)\setminus\{x_0\}$ es infinito.
> 4. Para todo $\varepsilon>0$, existe $x\in A\setminus\{x_0\}$ con $d(x,x_0)<\varepsilon$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Puntos_de_Acumulación_02.svg]]
>
> **Se lee así:** el diagrama parte de un punto frente a un conjunto y decide primero si toda bola contiene otros puntos de $A$. La rama de acumulación contrasta con las decisiones de aislamiento, frontera e interior; no presenta “cercano” como una noción única, sino como cuatro relaciones distintas.
>
> **Por qué importa:** la caracterización por sucesión convierte un problema topológico en una construcción explícita. En un examen, exhibir $x_n=1/n$ suele demostrar mejor la acumulación que repetir la definición.
>
> **Ejemplo:** para probar que $0$ acumula $\{1/n:n\in\mathbb N\}$, basta tomar $x_n=1/n$.

> [!note] 📋 Definición — Punto aislado
>
> Un punto $x_0\in A$ es **aislado** en $A$ si no es punto de acumulación de $A$. Equivalentemente, existe $r>0$ tal que
> $$B(x_0,r)\cap A=\{x_0\}.$$
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Puntos_de_Acumulación_02.svg]]
>
> **Se lee así:** cuando la respuesta a la pregunta principal es no, una segunda decisión busca una bola que contenga únicamente a $x_0$. Esa rama roja representa el aislamiento.
>
> **Por qué importa:** aislamiento es la negación operativa de acumulación. Un conjunto finito no puede tener acumulación porque sus puntos se pueden separar.
>
> **Ejemplo:** todos los naturales son aislados en $\mathbb N$ y en $\mathbb Z$.

> [!note] 📋 Definición — Punto interior
>
> Un punto $x_0\in A$ es **interior** de $A$ si existe $r>0$ tal que
> $$B(x_0,r)\subseteq A.$$
>
> Todo punto interior es de acumulación, pero no todo punto de acumulación es interior.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Puntos_de_Acumulación_02.svg]]
>
> **Se lee así:** una tercera salida del diagrama pregunta por una bola completamente contenida en $A$. La diferencia está en el “completamente”: interior exige que toda la bola pertenezca al conjunto.
>
> **Por qué importa:** acumulación solo exige intersección con $A$ y su complemento; interior exige que la bola entera esté en $A$.
>
> **Ejemplo:** $0.5$ es interior de $(0,1)$ porque $B(0.5,0.2)=(0.3,0.7)\subset(0,1)$.

> [!note] 📋 Definición — Punto frontera
>
> Un punto $x_0\in X$ es **frontera** de $A$ si para todo $r>0$,
> $$B(x_0,r)\cap A\ne\varnothing\quad\text{y}\quad B(x_0,r)\cap(X\setminus A)\ne\varnothing.$$
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Puntos_de_Acumulación_02.svg]]
>
> **Se lee así:** la rama de frontera exige dos intersecciones simultáneas: la bola debe tocar $A$ y también su complemento. No importa que $x_0$ pertenezca o no a $A$.
>
> **Por qué importa:** una frontera es el lugar de contacto entre dos regiones. Si $A$ es denso, todo punto puede ser frontera aunque solo uno de los conjuntos sea denso.
>
> **Ejemplo:** $0$ y $1$ son frontera de $(0,1)$; todo real es frontera de $\mathbb Q$.

> [!note] 📋 Definición — Clausura y conjunto cerrado
>
> La **clausura** de $A$ es
> $$\overline A=A\cup A'.$$
> Es el conjunto cerrado más pequeño que contiene a $A$. Un conjunto $A$ es **cerrado** si y solo si contiene todos sus puntos de acumulación:
> $$A\text{ cerrado}\iff A'\subseteq A\iff A=\overline A.$$
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Puntos_de_Acumulación_03.svg]]
>
> **Se lee así:** $A$ y su conjunto derivado $A'$ se unen para formar $\overline A$. La decisión inferior comprueba si todos los puntos de $A'$ están en $A$; de esa respuesta dependen el carácter cerrado y el criterio secuencial.
>
> **Por qué importa:** la clausura agrega a $A$ exactamente los límites que le faltan. Es la herramienta para activar la definición formal de límite.
>
> **Ejemplo:** $\overline{(0,1)}=[0,1]$, $\overline{\{1/n:n\in\mathbb N\}}=\{1/n:n\in\mathbb N\}\cup\{0\}$ y $\overline{\mathbb Q}=\mathbb R$.

> [!note] 📋 Definición — Densidad y conjunto perfecto
>
> $A$ es **denso** en $X$ si $\overline A=X$. Un conjunto $A$ es **perfecto** si es cerrado y $A'=A$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Puntos_de_Acumulación_03.svg]]
>
> **Se lee así:** la clausura se compara con el espacio completo $X$ para decidir si $A$ es denso; además, el conjunto derivado debe coincidir con $A$ para que sea perfecto.
>
> **Por qué importa:** estos dos conceptos separan “muchos puntos de acumulación” de “todos sus puntos son de acumulación”.
>
> **Ejemplo:** $\mathbb Q$ es denso pero no perfecto; $[0,1]$ y el conjunto de Cantor son perfectos.

---

## 🔍 Ejemplos y Caracterización

> [!example] 📏 En la recta real
>
> - $A=(0,1)$: $A'=[0,1]$. Todo punto interior es de acumulación y los extremos también, aunque no pertenezcan a $A$.
> - $A=[0,1]$: $A'=[0,1]$. Incluir los extremos no cambia el conjunto derivado.
> - $A=\mathbb N$: $A'=\varnothing$. Por ejemplo, $B(n,0.5)$ contiene solo $n$.
> - $A=\{1,1/2,1/3,\ldots\}$: $A'=\{0\}$. Cada bola de $0$ contiene términos $1/n$ para $n$ suficientemente grande; cada $1/n$ puede aislarse.
>
> **Por qué importa:** estos cuatro casos cubren intervalo con extremos, intervalo cerrado, conjunto aislado y convergencia a un punto.

> [!example] 🗺️ En el plano
>
> - Disco abierto $B((0,0),1)$: su conjunto derivado es el disco cerrado $\{(x,y):x^2+y^2\le1\}$.
> - Cuadrícula $\mathbb Z^2$: $A'=\varnothing$; una bola de radio $0.5$ contiene solo el punto elegido.
> - Cuadrícula racional $\mathbb Q^2$: $A'=\mathbb R^2$, porque todo punto del plano tiene racionales arbitrariamente cerca.
>
> **Por qué importa:** densidad y aislamiento se ven de inmediato en el plano: la cuadrícula racional llena el plano sin tener puntos “vacíos”, mientras $\mathbb Z^2$ separa cada punto.

> [!example] 🎲 En un espacio discreto
>
> Para cualquier $A\subseteq X$ con métrica discreta, $A'=\varnothing$. La bola $B(x,0.5)$ contiene únicamente a $x$, de modo que ningún punto acumula a otros puntos de $A$.
>
> **Por qué importa:** demuestra que la topología, y no solo el conjunto de puntos, determina la acumulación.

> [!example] 📈 Convergencia y acumulación
>
> Si $(x_n)\subseteq A$ converge a $x_0$ y infinitos términos son distintos de $x_0$, entonces $x_0\in A'$. Para $x_n=1/n$ en $\{1/n:n\in\mathbb N\}$, se cumple $0\in A'$. En cambio, la sucesión constante $x_n=5$ en $\{5\}$ no da acumulación: $5$ es aislado.
>
> **Por qué importa:** la sucesión constante es el contraejemplo que separa “hay convergencia” de “hay puntos de acumulación”.

> [!example] 🌟 Casos notables en $\mathbb R$
>
> - Cantor: cerrado, sin puntos interiores y perfecto; todos sus puntos son de acumulación.
> - $\{1/n:n\in\mathbb N\}\cup\{0\}$: único punto de acumulación $0$; cerrado.
> - $\{1+1/n:n\in\mathbb N\}$: único punto de acumulación $1$, que no pertenece al conjunto; no cerrado.
> - $\mathbb R\setminus\mathbb Q$: conjunto derivado igual a $\mathbb R$; denso y no cerrado.

> [!example] 🌍 Casos notables en $\mathbb R^2$
>
> - Circunferencia $S^1$: derivada igual a $S^1$; cerrada y sin interior.
> - $\mathbb Q^2$: derivada igual a $\mathbb R^2$; denso y no cerrado.
> - Corona $1<x^2+y^2<4$: derivada $1\le x^2+y^2\le4$; no cerrada.

> [!note] 📊 Tabla comparativa de tipos de punto
>
> | Tipo | ¿Debe estar en $A$? | Condición | Ejemplo |
> |---|---|---|---|
> | Acumulación | No necesariamente | Toda bola contiene puntos de $A\setminus\{x_0\}$ | $0$ para $(0,1)$ |
> | Aislado | Sí | Existe bola que solo contiene a $x_0$ | $5$ para $\{5\}\cup[10,20]$ |
> | Interior | Sí | Existe bola totalmente contenida en $A$ | $0.5$ para $(0,1)$ |
> | Frontera | No necesariamente | Toda bola toca $A$ y $X\setminus A$ | $0$ para $(0,1)$ |
> | Exterior | No | Existe bola disjunta de $A$ | $10$ para $(0,1)$ |
>
> **Relaciones:** todo punto interior es de acumulación; los puntos aislados no son de acumulación; los puntos frontera pueden o no ser de acumulación.

> [!example] 🤯 Situaciones contra intuitivas
>
> - $[0,1]$: todos los puntos son de acumulación, por lo que $A'=A$.
> - $(0,1)$: los extremos son de acumulación aunque no estén en el conjunto.
> - $\mathbb Q$: $A'=\mathbb R$, incluidos todos los irracionales.
> - $\mathbb Z$: es infinito, pero $A'=\varnothing$ y por tanto es cerrado.
> - $\{0\}\cup\{1/n:n\in\mathbb N\}$: solo $0$ es de acumulación; cada $1/n$ es aislado.
>
> **Por qué importa:** infinito no implica tener puntos de acumulación; la geometría y la topología del conjunto sí.

---

## ⚙️ Propiedades, Operaciones y Teoremas

> [!note] ⚙️ Propiedades fundamentales
>
> 1. Si $A\subseteq B$, entonces $A'\subseteq B'$.
> 2. $(A\cup B)'=A'\cup B'$.
> 3. $(A\cap B)'\subseteq A'\cap B'$; la inclusión puede ser estricta.
> 4. Si $A$ es finito, $A'=\varnothing$.
> 5. $(\overline A)'=A'$.
>
> **Ejemplo de la tercera propiedad:** para $A=[0,1]$ y $B=[1,2]$, $(A\cap B)'=\varnothing$, pero $A'\cap B'=\{1\}$.

> [!note] 🔄 Puntos de acumulación del complemento
>
> En general no hay una igualdad simple entre $A'$ y $(X\setminus A)'$. Para $A=(0,1)$, $A'=[0,1]$ y $(X\setminus A)'=\mathbb R$. Para $A=\mathbb Q$, tanto $A'$ como $(X\setminus A)'$ son $\mathbb R$.
>
> **Por qué importa:** “un conjunto es cerrado” no equivale a “su complemento no tiene puntos de acumulación”.

> [!success] 🌟 Bolzano–Weierstrass
>
> Todo conjunto infinito y acotado en $\mathbb R^n$ tiene al menos un punto de acumulación. Equivalentemente, toda sucesión acotada en $\mathbb R^n$ posee una subsucesión convergente.
>
> **Ejemplo:** $\{1/n:n\in\mathbb N\}$ es infinito, acotado y tiene el punto de acumulación $0$.

> [!success] 💎 Compacidad y criterio secuencial
>
> En espacios métricos, $K$ es compacto si y solo si todo subconjunto infinito de $K$ tiene un punto de acumulación en $K$. Además, $A$ es cerrado si y solo si toda sucesión de elementos de $A$ que converge tiene su límite en $A$.
>
> **Ejemplo:** $(0,1)$ no es compacto porque $\{1/n:n\ge2\}$ acumula en $0\notin(0,1)$; $[0,1]$ sí lo es.

> [!tip] 🧠 Estrategias para identificar acumulación
>
> 1. **Construir una sucesión** en $A\setminus\{x_0\}$ que converja a $x_0$.
> 2. **Verificar con bolas:** para todo radio arbitrario, exhibir otro punto de $A$.
> 3. **Negarlo:** para demostrar que $x_0$ no acumula, encontrar una bola sin puntos de $A$ distintos de $x_0$.
> 4. **Usar propiedades:** finito o discreto implica $A'=\varnothing$; un intervalo en $\mathbb R$ se analiza por sus extremos; un conjunto denso tiene una derivada grande.
>
> **Aplicaciones:** clustering y detección de outliers (DBSCAN), distribuciones de materia en física, k-NN y consultas por rango en computación.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Determina los puntos de acumulación de:
>
> - $A=\{1,2,3,4,5\}$;
> - $B=(0,1]$;
> - $C=\{0\}\cup(1,2)$.
>
> > [!success]- ✅ Solución
> >
> > $A'=\varnothing$, porque $A$ es finito. $B'=[0,1]$. Para $C$, se tiene $C'=\{1,2\}$: $0$ es aislado y los puntos de $(1,2)$ son de acumulación, igual que el extremo $1$.

> [!example] 📋 Planteamiento
>
> Demuestra que $0$ es el único punto de acumulación de $\{1/n:n\in\mathbb N\}$ y que todo punto de $(0,1)$ acumula $\mathbb Q\cap(0,1)$.
>
> > [!success]- ✅ Solución
> >
> > Para $0$, la sucesión $x_n=1/n$ está en el conjunto, nunca vale $0$ y converge a $0$. Si $x\ne0$, se elige una bola suficientemente pequeña separada del conjunto o contienen solo un número finito de sus términos. Para la segunda afirmación, la densidad de $\mathbb Q$ garantiza un racional distinto del punto central dentro de cualquier radio.

> [!example] 📋 Planteamiento
>
> Responde: ¿puede un punto aislado ser de acumulación? Si $A\subseteq\mathbb R$ cumple $A'=\mathbb R$, ¿$A$ debe ser infinito? ¿Debe ser numerable?
>
> > [!success]- ✅ Solución
> >
> > No: el aislamiento significa exactamente que existe una bola sin otros puntos de $A$. Sí, $A$ debe ser infinito porque los conjuntos finitos tienen derivada vacía. No debe ser numerable: $\mathbb Q$ es numerable y $\mathbb Q'=\mathbb R$.

> [!example] 📋 Planteamiento
>
> Determina $A'$ para:
>
> - $A=\{n+1/n:n\in\mathbb N\}$;
> - $B=\{r+1/n:r\in\mathbb Q,n\in\mathbb N\}$;
> - $C=\{(-1)^n/n:n\in\mathbb N\}$.
>
> > [!success]- ✅ Solución
> >
> > $A'=\varnothing$, porque los términos se separan y escapan al infinito. $B'=\mathbb R$, por la densidad de $\mathbb Q$ y porque cada racional es límite de $r+1/n$. $C'=\{0\}$, pues la sucesión alterna de signo pero converge a $0$.

> [!example] 📋 Planteamiento
>
> Demuestra que un conjunto finito no tiene puntos de acumulación y da un conjunto con exactamente dos puntos de acumulación.
>
> > [!success]- ✅ Solución
> >
> > Para $A=\{a_1,\ldots,a_n\}$, cada punto se puede aislar con una bola menor que la mitad de su distancia al resto; fuera de $A$ también puede construirse una bola separada. Un ejemplo con exactamente dos puntos de acumulación es
> > $$\{1/n:n\in\mathbb N\}\cup\{2+1/n:n\in\mathbb N\},$$
> > cuyo conjunto derivado es $\{0,2\}$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino punto de acumulación, aislado, interior y frontera.
> - [ ] Distingo acumulación de pertenencia a un conjunto.
> - [ ] Calculo conjuntos derivados de intervalos y conjuntos finitos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Uso sucesiones para demostrar acumulación.
> - [ ] Explico la relación entre $A'$, $\overline A$ y el carácter cerrado.
> - [ ] Distingo un conjunto infinito sin puntos de acumulación de uno denso.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> - W. Rudin, *Principles of Mathematical Analysis*, cap. 2, topología de $\mathbb R^n$.
> - J. Munkres, *Topology*, Parte I, conjuntos cerrables y puntos de acumulación.
> - T. M. Apostol, *Análisis Matemático*,capítulos de topología y secuencias.
> - Material de cátedra de MATG1045.

> [!note] 📗 Exámenes relacionados
>
> - EXA-2022-1S-CÁLCULO DE UNA VARIABLE-1-1Par.pdf, p. 1: preguntas sobre representación de conjuntos y puntos de acumulación. Se usa como enlace de estudio, sin incrustar el PDF.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Definición de punto de acumulación?::Toda bola alrededor de $x_0$ contiene un punto de $A$ distinto de $x_0$.
> - ¿Puede un punto de acumulación no estar en $A$?::Sí; por ejemplo $0$ para $\{1/n\}$.
> - ¿Caracterización por sucesión?::$x_0$ acumula $A$ si existe $(x_n)\subset A\setminus\{x_0\}$ con $x_n\to x_0$.
> - ¿Punto aislado?::Existe una bola alrededor de $x_0$ cuyo único punto de $A$ es $x_0$.
> - ¿Punto interior?::Existe una bola alrededor de $x_0$ completamente contenida en $A$.
> - ¿Clausura?::$\overline A=A\cup A'$.
> - ¿Conjunto cerrado?::$A'\subseteq A$, equivalentemente $A=\overline A$.
> - ¿Finito implica?::Un conjunto finito no tiene puntos de acumulación.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Métricas y Espacios Métricos]] — define las bolas usadas en esta nota.
> - [[../Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|Concepto y Definición Formal del Límite]] — usa la acumulación como noción de cercanía.
> - [[../Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|Continuidad y Límites]] — la continuidad se apoya en límites y clausuras.
> - [[../Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|Límites al Infinito y Sucesiones]] — conecta sucesión, convergencia y conjunto derivado.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Continúa con [[../Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|Concepto y Definición Formal del Límite]].
> - Revisa las caracterizaciones por sucesión antes de estudiar límites laterales.
> - Resuelve primero los tres ejercicios sobre $\mathbb R$ y después aplica el mismo criterio a $\mathbb R^2$.
> - Usa el mapa de la Unidad 2 para separar acumulación, adherencia y límite funcional.

---

**Tags:** #MATG1045 #unidad1 #puntos-de-acumulacion #topologia #clausura #conjuntos-cerrados #sucesiones #convergencia

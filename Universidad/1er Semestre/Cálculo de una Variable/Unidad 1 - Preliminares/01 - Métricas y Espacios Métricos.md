---
dg-publish: true
tags: [MATG1045, unidad1, metricas, espacios-metricos, topologia, analisis-real]
---

# 📏 Métricas y Espacios Métricos

## 🎯 Introducción

> [!info] 💡 ¿Por qué formalizar la distancia?
>
> La geometría euclidiana dice que una distancia es un número, pero el cálculo necesita algo más general: una manera de decidir **qué tan cerca** están dos objetos. Esa decisión aparece al hablar de límite, continuidad, convergencia y compactitud.
>
> Una métrica no es “la distancia verdadera”; es una distancia coherente sobre un conjunto. En $\mathbb R$ lo natural es $|x-y|$, mientras que en una ciudad cuadriculada puede ser más útil la distancia del taxi. Cambiar la métrica cambia qué significa “cercano”, aunque la topología pueda seguir siendo la misma.
>
> **Objetivo de la nota:** reconocer cuándo una función es una métrica, comparar métricas clásicas, entender cómo las bolas producen topología y anticipar el lenguaje que se reutiliza en límites.
>
> **Ejemplo:** para dos estudiantes de la ESPOL, la distancia social no es euclidiana: puede contar conexiones en una red. Si se formaliza como métrica discreta, cualquier par distinto queda a distancia $1$.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Métrica
>
> Sea $X$ un conjunto no vacío. Una función $d:X\times X\to[0,\infty)$ es una **métrica** si para todo $x,y,z\in X$ cumple:
>
> 1. **No negatividad:** $d(x,y)\ge 0$.
> 2. **Identidad:** $d(x,y)=0\iff x=y$.
> 3. **Simetría:** $d(x,y)=d(y,x)$.
> 4. **Desigualdad triangular:** $d(x,z)\le d(x,y)+d(y,z)$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métricas_y_Espacios_Métricos_02.svg]]
>
> **Se lee así:** una función candidata entra a una decisión de cuatro salidas. Las cuatro flechas verdes enumeran los axiomas: no negatividad, identidad, simetría y desigualdad triangular. La rama roja obliga a localizar el axioma fallido antes de usar la función.
>
> **Por qué importa:** el diagrama convierte “es una distancia” en una tarea verificable. Evita el error más común: aceptar una fórmula porque se parece a una distancia sin comprobar la desigualdad triangular.
>
> **Ejemplo:** para $d(x,y)=(x-y)^2$ en $\mathbb R$, la no negatividad y la identidad se cumplen, pero $d(0,2)=4>2=d(0,1)+d(1,2)$; por tanto no es métrica.

> [!note] 📋 Definición — Espacio métrico
>
> Un **espacio métrico** es un par ordenado $(X,d)$ donde $X$ es un conjunto no vacío y $d$ es una métrica sobre $X$. El conjunto $X$ aporta los puntos y la función $d$ aporta la forma de medir cercanía.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métricas_y_Espacios_Métricos_01.svg]]
>
> **Se lee así:** la caja superior representa el par $(X,d)$. A la izquierda se separan sus dos componentes: conjunto de puntos y función de distancia. A la derecha, las bolas abierta y cerrada forman un segundo eje y desembocan en ejemplos sobre la recta y el plano.
>
> **Por qué importa:** separar $X$ de $d$ revela que la misma colección de puntos puede tener varias estructuras metricas distintas. Es el punto de partida de la topología metrizable.
>
> **Ejemplo:** $\mathbb R^2$ admite la distancia euclidiana, la del taxi y la del máximo; por eso “el plano” no basta para determinar cómo se mide la cercanía.

> [!note] 📋 Definición — Bolas y esfera
>
> En $(X,d)$, para $x_0\in X$ y $r>0$:
>
> - **Bola abierta:** $B(x_0,r)=\{x\in X:d(x,x_0)<r\}$.
> - **Bola cerrada:** $\overline B(x_0,r)=\{x\in X:d(x,x_0)\le r\}$.
> - **Esfera:** $S(x_0,r)=\{x\in X:d(x,x_0)=r\}$.
>
> Además, $\overline B(x_0,r)=B(x_0,r)\cup S(x_0,r)$. En general la bola cerrada no tiene por qué ser igual a la clausura de la bola abierta; sí coincide en $\mathbb R^n$ con la métrica euclidiana.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métricas_y_Espacios_Métricos_03.svg]]
>
> **Se lee así:** un mismo centro y radio alimentan tres caminos. La bola abierta usa la desigualdad estricta, la cerrada incluye la igualdad y la esfera conserva únicamente la frontera. Las flechas finales muestran sus formas en la recta.
>
> **Por qué importa:** las bolas son la moneda local de la topología métrica: un conjunto abierto debe contener una bola alrededor de cada punto, y un límite se formula controlando radios.
>
> **Ejemplo:** en $\mathbb R$ con $d_E$, $B(0,1)=(-1,1)$, $\overline B(0,1)=[-1,1]$ y $S(0,1)=\{-1,1\}$.

> [!note] 📋 Definición — Métricas equivalentes
>
> Dos métricas $d_1,d_2$ sobre $X$ son **equivalentes** si inducen la misma topología. En un espacio métrico finito o en las situaciones usuales de $\mathbb R^n$, esto equivale a la existencia de constantes $C_1,C_2>0$ tales que
> $$C_1d_1(x,y)\le d_2(x,y)\le C_2d_1(x,y).$$
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Métricas_y_Espacios_Métricos_02.svg]]
>
> **Se lee así:** las métricas candidatas desembocan en la misma comprobación de cuatro axiomas y, si ambas son válidas, pueden compararse mediante cotas constantes sin que cambie la estructura de cercanía.
>
> **Por qué importa:** equivalentes no significa idénticas: sus valores numéricos y la forma de sus bolas pueden diferir. Lo que se conserva son abiertos, cerrados, convergencia y continuidad.
>
> **Ejemplo:** en $\mathbb R^2$, $d_\infty(x,y)\le d_2(x,y)\le d_1(x,y)$, de modo que las tres métricas son equivalentes aunque sus bolas sean círculo, rombo y cuadrado.

---

## 📐 Métricas Clásicas y Bolas

> [!note] 📋 Familias de métricas en $\mathbb R^n$
>
> Para $x=(x_1,\ldots,x_n)$ y $y=(y_1,\ldots,y_n)$:
>
> | Nombre | Fórmula | Lectura geométrica |
> |---|---|---|
> | Euclidiana $d_2$ | $\sqrt{\sum_{i=1}^n(x_i-y_i)^2}$ | Distancia en línea recta |
> | Taxi o Manhattan $d_1$ | $\sum_{i=1}^n|x_i-y_i|$ | Recorrido por ejes |
> | Máximo o Chebyshev $d_\infty$ | $\max_i|x_i-y_i|$ | Peor coordenada |
> | Discreta $d_D$ | $0$ si $x=y$; $1$ si $x\ne y$ | Solo importa igualdad o diferencia |
>
> **Por qué importa:** la misma pregunta admite respuestas coherentes distintas. Elegir una métrica es elegir qué diferencias son relevantes.
>
> **Ejemplo:** para navegar por una ciudad con calles en cuadrícula, $d_1$ suele ser más útil que $d_2$.

> [!example] 🧪 Verificación de los cuatro axiomas
>
> Para $d(x,y)=|x-y|$ en $\mathbb R$:
>
> - No negatividad: $|x-y|\ge0$.
> - Identidad: $|x-y|=0\iff x=y$.
> - Simetría: $|x-y|=|-(y-x)|=|y-x|$.
> - Triangular: $|x-z|\le|x-y|+|y-z|$.
>
> Por las cuatro verificaciones, $d$ es una métrica.

> [!example] 🔢 Euclidiana: cálculos numéricos
>
> - En $\mathbb R$: $d_2(3,7)=4$, $d_2(-2,5)=7$, $d_2(\pi,\pi)=0$.
> - En $\mathbb R^2$, para $A=(1,2)$ y $B=(4,6)$:
> $$d_2(A,B)=\sqrt{3^2+4^2}=5.$$
> - En $\mathbb R^3$, para $P=(1,0,0)$ y $Q=(0,1,1)$:
> $$d_2(P,Q)=\sqrt{1+1+1}=\sqrt3\approx1.732.$$
>
> **Por qué importa:** fijar los mismos puntos en espacios distintos muestra cómo la fórmula euclidiana conserva el teorema de Pitágoras.

> [!example] 🚕 Taxi: aplicación urbana
>
> Para $A=(1,2)$ y $B=(4,6)$:
> $$d_1(A,B)=|4-1|+|6-2|=7.$$
> En $\mathbb R^3$, para $P=(1,0,2)$ y $Q=(3,1,5)$:
> $$d_1(P,Q)=2+1+3=6.$$
> La distancia del taxi siempre es mayor o igual que la euclidiana.
>
> **Aplicaciones:** navegación urbana, procesamiento de imágenes, aprendizaje automático con distancia $L1$ y optimización robusta.

> [!example] 📦 Máximo: peor coordenada
>
> Para $A=(1,2)$ y $B=(4,6)$:
> $$d_\infty(A,B)=\max\{3,4\}=4.$$
> En $\mathbb R^2$, las bolas $d_\infty$ son cuadrados; la métrica destaca la coordenada con mayor separación.
>
> **Por qué importa:** cuando todos los errores se acumulan en el peor caso, el máximo es la elección natural.

> [!example] 🎲 Métrica discreta
>
> En $X=\{a,b,c\}$, $d_D(a,a)=0$ y $d_D(a,b)=d_D(b,c)=d_D(a,c)=1$. Los cuatro axiomas se cumplen: si $x=z$ la desigualdad triangular es inmediata; si $x\ne z$, la suma de dos pasos es al menos $1$.
>
> En $\mathbb R$ con esta métrica, $d_D(2,3)=d_D(0,1000000)=1$. Todos los puntos distintos son equidistantes y todo subconjunto es abierto y cerrado.

> [!example] 🔢 Métrica del supremo en funciones
>
> Sea $C([a,b])$ el espacio de funciones continuas en $[a,b]$. La métrica del supremo es
> $$d_\infty(f,g)=\sup_{x\in[a,b]}|f(x)-g(x)|=\max_{x\in[a,b]}|f(x)-g(x)|.$$
> El máximo existe porque $f-g$ es continua en un intervalo compacto.
>
> **Otras métricas:** $d_1(f,g)=\int_a^b|f-g|\,dx$ y $d_2(f,g)=\sqrt{\int_a^b|f-g|^2\,dx}$.
>
> **Por qué importa:** esta métrica mide la separación vertical máxima entre curvas y produce convergencia uniforme.

> [!example] 🎯 Formas de las bolas unitarias en $\mathbb R^2$
>
> Con centro $(0,0)$ y radio $1$:
>
> | Métrica | Bola abierta | Forma |
> |---|---|---|
> | $d_2$ | $x^2+y^2<1$ | Disco circular |
> | $d_1$ | $|x|+|y|<1$ | Rombo |
> | $d_\infty$ | $\max\{|x|,|y|\}<1$ | Cuadrado |
>
> En la métrica discreta, $B(x_0,1)=\{x_0\}$ porque los demás puntos están exactamente a distancia $1$, mientras que $\overline B(x_0,1)=X$.

> [!example] 🏙️ Bolas de la recta y el plano
>
> - En $\mathbb R$: $B(0,1)=(-1,1)$, $\overline B(0,1)=[-1,1]$, $S(0,1)=\{-1,1\}$.
> - En $\mathbb R^2$ euclidiano: $B((0,0),1)$ es el disco abierto y $\overline B((0,0),1)$ el disco cerrado.
> - En $\mathbb R^2$ con $d_1$: $B_1((0,0),1)$ es el rombo de vértices $(1,0),(0,1),(-1,0),(0,-1)$.
> - En un espacio discreto: $B(x_0,1)=\{x_0\}$ y $B(x_0,2)=X$.

---

## 🔄 Propiedades, Ejemplos y Aplicaciones

> [!note] ⚙️ Álgebra de espacios métricos
>
> - Si $A\subseteq B$, entonces $A'\subseteq B'$.
> - Todo conjunto finito tiene $A'=\varnothing$.
> - $(\overline A)'=A'$.
> - Una métrica induce una topología; no toda topología proviene de una métrica.
> - Una isometría preserva exactamente las distancias y, por tanto, bolas, diámetros, límites y continuidad.
>
> **Por qué importa:** estas reglas separan propiedades que dependen solo de la métrica de otras que dependen de la topología.

> [!tip] ✅ Completitud y Cauchy
>
> Una sucesión $(x_n)$ es de **Cauchy** si
> $$\forall\varepsilon>0,\ \exists N:\ m,n\ge N\implies d(x_m,x_n)<\varepsilon.$$
> Un espacio $(X,d)$ es **completo** si toda sucesión de Cauchy converge a un punto de $X$.
>
> **Ejemplos:** $\mathbb R$ con la métrica euclidiana es completo; $\mathbb Q$ no lo es; $C([a,b])$ con $d_\infty$ es completo; todo espacio métrico compacto es completo. La completación $\widehat X$ extiende la métrica y contiene a $X$ como subespacio denso; por ejemplo, $\widehat{\mathbb Q}=\mathbb R$.

> [!tip] 📐 Isometrías
>
> Una función $f:X\to Y$ es una **isometría** si
> $$d_Y(f(x_1),f(x_2))=d_X(x_1,x_2).$$
> Entonces $f$ es inyectiva y continua; si es sobreyectiva, $X$ e $Y$ son isométricos. Rotaciones, traslaciones y reflexiones en $\mathbb R^n$ son isometrías, y también lo es $f(x)=x+1$ en $(\mathbb R,|\cdot|)$.

> [!warning] ⚠️ Errores frecuentes
>
> | Afirmación incorrecta | Corrección | Contraejemplo o razón |
> |---|---|---|
> | “Toda distancia es métrica” | Hay que comprobar los cuatro axiomas | $(x-y)^2$ viola la desigualdad triangular |
> | “La euclidiana es la única natural” | La métrica depende del contexto | Taxi, Hamming, grafos o Wasserstein según el problema |
> | “$d(x,y)=0$ siempre implica $x=y$” | Eso distingue métrica de pseudométrica | $|x_1-x_2|$ en $\mathbb R^2$ ignora la segunda coordenada |
> | “Bola cerrada = clausura de la bola abierta” | Solo es cierto en ciertos espacios | En $\mathbb R^n$ euclidiano sí; en espacios generales puede fallar |
> | “Todas las métricas inducen la misma topología” |Solo las equivalentes lo hacen | $d_1,d_2,d_\infty$ son equivalentes, pero la discreta no |
>
> **Mnemotecnia para estudiar:** visualiza primero en $\mathbb R$ y $\mathbb R^2$, verifica siempre los cuatro axiomas, calcula distancias concretas y conecta la métrica con la topología.

> [!success] 🌐 Aplicaciones en distintas áreas
>
> | Área | Métricas o ideas útiles | Aplicación |
> |---|---|---|
> | Análisis de datos | Euclidiana, Manhattan, Hamming, Mahalanobis, coseno, Wasserstein | Agrupamiento, clasificación y outliers |
> | Procesamiento de imágenes | $L1$, $L2$, Hausdorff, Earth Mover, SSIM | Diferencias entre imágenes y formas |
> | Bioinformática | Hamming, Levenshtein, filogenética, edición | Comparar ADN y proteínas |
> | Teoría de grafos | Distancia por camino más corto | Redes de transporte y centrality |
> | Física e ingeniería | Minkowski, métricas curvas, Fubini–Study | Espacio-tiempo, relatividad y señales |
> | Economía y finanzas | Distancias entre activos y medidas de riesgo | Portafolios y series temporales |
>
> **Ejemplo:** en clustering, $k$-means usa chiefly distancia euclidiana, mientras DBSCAN se apoya en vecinos dentro de un radio y guarda la estructura de densidad.

> [!note] 📖 Glosario esencial
>
> | Español | Inglés | Español | Inglés |
> |---|---|---|---|
> | Métrica | Metric | Bola abierta | Open ball |
> | Distancia | Distance | Bola cerrada | Closed ball |
> | Espacio métrico | Metric space | Esfera | Sphere |
> | Axiomas | Axioms | Radio | Radius |
> | Desigualdad triangular | Triangle inequality | Diámetro | Diameter |
> | No negatividad | Non-negativity | Acotado | Bounded |
> | Identidad | Identity of indiscernibles | Isometría | Isometry |
> | Simetría | Symmetry | Completo | Complete |
> | Euclidiana | Euclidean metric | Compacto | Compact |
> | Taxi o Manhattan | Taxi/Manhattan metric | Conexo | Connected |
> | Máximo o Chebyshev | Maximum metric | Separable | Separable |
> | Discreta | Discrete metric | Convergente | Convergent |
> | Del supremo | Supremum metric | Cauchy | Cauchy sequence |
> | Pseudométrica | Pseudometric | Punto de acumulación | Accumulation point |
> | Semimétrica | Semimetric | Punto adherente | Adherent point |
> | Ultramétrica | Ultrametric | Abierto | Open set |
> | Cerrado | Closed set | Clausura | Closure |
> | Interior | Interior | Frontera | Boundary |
> | Denso | Dense | Vecindad | Neighborhood |
>
> **Por qué importa:** el glosario evita traducir “closure” como “cerradura” y “accumulation point” como “punto límite”, reservando este último para el límite de una función.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Determina si las funciones son métricas:
>
> 1. $d(x,y)=|x-y|^2$ en $\mathbb R$.
> 2. $d(x,y)=\min\{|x-y|,1\}$ en $\mathbb R$.
> 3. $d(x,y)=|x^2-y^2|$ en $\mathbb R$.
> 4. $d((x_1,y_1),(x_2,y_2))=|x_1-x_2|+2|y_1-y_2|$ en $\mathbb R^2$.
>
> > [!success]- ✅ Solución
> >
> > 1. **No.** $d(0,2)=4>2=d(0,1)+d(1,2)$.
> > 2. **Sí.** Los valores son no negativos, nulos solo si $x=y$ y simétricos. Si $d(x,y)<1$, la desigualdad usual da $d(x,z)\le|x-z|\le|x-y|+|y-z|$; si $d(x,y)=1$, el lado derecho es al menos $1=d(x,z)$.
> > 3. **No.** $d(1,-1)=0$, aunque $1\ne-1$.
> > 4. **Sí.** Es una suma ponderada de métricas y la desigualdad triangular se obtiene sumando las de cada coordenada.

> [!example] 📋 Planteamiento
>
> Para $A=(2,1)$ y $B=(5,5)$, calcula $d_2(A,B)$, $d_1(A,B)$ y $d_\infty(A,B)$. Después describe las bolas unitarias en $\mathbb R^2$ para las tres métricas.
>
> > [!success]- ✅ Solución
> >
> > $$d_2(A,B)=\sqrt{3^2+4^2}=5,\quad d_1(A,B)=3+4=7,\quad d_\infty(A,B)=\max\{3,4\}=4.$$
> > Las bolas son, respectivamente, disco abierto, rombo y cuadrado. Se cumple $4\le5\le7$.

> [!example] 📋 Planteamiento
>
> En $X=\{a,b,c,d\}$ con métrica discreta, calcula $B(a,0.5)$, $B(a,1)$ y $\overline B(a,1)$. ¿Tiene $\{a\}$ puntos de acumulación?
>
> > [!success]- ✅ Solución
> >
> > $B(a,0.5)=B(a,1)=\{a\}$, porque los demás puntos están a distancia $1$; $\overline B(a,1)=X$. El conjunto $\{a\}$ no tiene puntos de acumulación: en la métrica discreta todo punto está aislado.

> [!example] 📋 Planteamiento
>
> En $(\mathbb R,d_E)$, determina $B(3,2)$, $\overline B(3,2)$ y explica la diferencia. En $(\mathbb R^2,d_E)$, decide si $(3,4)$ pertenece a $B((0,0),5)$ y a $\overline B((0,0),5)$.
>
> > [!success]- ✅ Solución
> >
> > $B(3,2)=(1,5)$ y $\overline B(3,2)=[1,5]$; la cerrada agrega los extremos $1$ y $5$. Como $d_E((0,0),(3,4))=5$, el punto no pertenece a la bola abierta, pero sí a la cerrada.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino métrica y espacio métrico sin mirar.
> - [ ] Compruebo los cuatro axiomas en una fórmula sencilla.
> - [ ] Distingo bola abierta, bola cerrada y esfera.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Comparo $d_1$, $d_2$ y $d_\infty$ mediante cálculos y formas de bolas.
> - [ ] Explico por qué métricas equivalentes conservan la topología.
> - [ ] Reconozco cuándo una discontinuidad o PSEUDOmétrica invalidan un argumento.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> - W. Rudin, *Principles of Mathematical Analysis*, cap. 2, topología básica.
> - J. Munkres, *Topology*, Parte I, espacios métricos.
> - T. M. Apostol, *Análisis Matemático*,capítulos de números reales y topología.
> - Material de cátedra de MATG1045 y apuntes de la ESPOL sobre espacios métricos.

> [!note] 📗 Exámenes relacionados
>
> - EXA-2022-1S-CÁLCULO DE UNA VARIABLE-1-1Par.pdf, p. 1: ejercicios de conjuntos y puntos de acumulación que conectan esta nota con [[../Unidad 1 - Preliminares/02 - Puntos de Acumulación|02 - Puntos de Acumulación]]. El PDF se cita como enlace de estudio, no se embebe.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué cuatro axiomas define una métrica?::No negatividad, identidad, simetría y desigualdad triangular.
> - ¿Qué distingue un espacio métrico?::El par $(X,d)$: conjunto no vacío y métrica sobre él.
> - ¿Bola abierta?::$B(x_0,r)=\{x:d(x,x_0)<r\}$.
> - ¿Por qué $(x-y)^2$ no es métrica en $\mathbb R$?::Viola la desigualdad triangular: $4>1+1$ para $0,1,2$.
> - ¿Qué métricas de $\mathbb R^2$ son equivalentes?::$d_1,d_2,d_\infty$; inducen la misma topología.
> - ¿Qué distingue una pseudométrica?::Puede tener $d(x,y)=0$ con $x\ne y$.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Puntos de Acumulación]] — usa bolas para caracterizar cercanía topológica.
> - [[../Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|Concepto y Definición Formal del Límite]] — traduce la cercanía métrica en la definición de límite.
> - [[../Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|Continuidad y Límites]] — la continuidad se expresa con métricas.
> - [[../Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|Derivabilidad y Continuidad]] — conecta métrica, continuidad y derivabilidad.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Siguiente: [[02 - Puntos de Acumulación]].
> - Repaso de límites: [[../Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|Concepto y Definición Formal del Límite]].
> - Aplicación de continuidad: [[../Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|Continuidad y Límites]].
> - Diagnóstico: resuelve en orden los ejercicios de esta nota antes de pasar a la Unidad 2.

---

**Tags:** #MATG1045 #unidad1 #metricas #espacios-metricos #topologia #analisis-real #distancia #bolas #convergencia

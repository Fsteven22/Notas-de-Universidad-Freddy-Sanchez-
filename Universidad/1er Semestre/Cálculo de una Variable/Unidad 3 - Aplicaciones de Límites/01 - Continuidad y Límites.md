---
dg-publish: true
tags: [MATG1045, unidad3, continuidad, limites, discontinuidades, valor-intermedio, continuidad-uniforme]
---

# 🔗 Continuidad y Límites

## 🎯 Introducción

> [!info] 💡 ¿Qué significa “no romper” una función?
>
> Una función es continua en un punto cuando el valor que toma al llegar coincide con el valor que tiene allí. La idea parece simple, pero la definición operacional exige controlar dos escalas: qué error toleramos en la imagen y qué distancia en el dominio garantiza ese error.
>
> La continuidad conecta tres temas: permite clasificar roturas de una gráfica, sostiene el teorema del valor intermedio y distingue una continuidad local de una garantía global. Es la base de la bisección, de la existencia de raíces y de muchas demostraciones de existencia.
>
> **Ejemplo:** $f(x)=\sin x/x$, con $f(0)=0$, tiene una discontinuidad evitable en $0$ porque el límite es $1$. Cambiar $f(0)$ por $1$ repara la función.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Continuidad en un punto
>
> Sea $f:D\to\mathbb R$ y $a\in D$. La función $f$ es **continua en $a$** si para todo $\varepsilon>0$ existe $\delta>0$ tal que
> $$x\in D,\quad |x-a|<\delta\implies |f(x)-f(a)|<\varepsilon.$$
>
> Son equivalentes:
>
> 1. $\displaystyle\lim_{x\to a}f(x)=f(a)$.
> 2. $\displaystyle\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=f(a)$.
> 3. Para toda sucesión $(x_n)\subseteq D$ con $x_n\to a$, se tiene $f(x_n)\to f(a)$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Continuidad_y_Límites_04.svg]]
>
> **Se lee así:** el diagrama recorre la definición epsilon-delta: se elige una tolerancia $\varepsilon$, se responde con un radio $\delta$ y se comprueba la desigualdad de imágenes. La rama final equipara esa condición con la igualdad entre límite y valor.
>
> **Por qué importa:** el control simultáneo de $x$ y $f(x)$ explica por qué “el límite coincide con el valor” es una definición y no solo una slogan.
>
> **Ejemplo:** $f(x)=x^2$ es continua en todo real porque $|x^2-a^2|=|x-a||x+a|$ puede controlarse eligiendo $\delta$ en función de $\varepsilon$ y de $a$.

> [!note] 📋 Definición — Continuidad uniforme
>
> Una función $f:A\to\mathbb R$ es **uniformemente continua** en $A$ si para todo $\varepsilon>0$ existe $\delta>0$ tal que, para todos $x,y\in A$,
> $$|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.$$
>
> En la continuidad puntual, $\delta$ puede depender del punto; en la uniforme, el mismo $\delta$ sirve para todos los puntos del dominio.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Continuidad_y_Límites_05.svg]]
>
> **Se lee así:** dos ramas contrastan la pregunta local, donde $\delta$ depende del punto, con la global, donde un único radio sirve en todo $A$. Las dos cajas inferiores ofrecen criterios suficientes: Heine-Cantor y derivada acotada.
>
> **Por qué importa:** separa “no hay saltos” de “la Sensitivity no se dispara cerca de ningún borde”. Esa diferencia explica por qué $1/x$ falla en $(0,1]$.
>
> **Ejemplo:** $\sin x$ es uniformemente continua en $\mathbb R$ porque $|f(x)-f(y)|\le|x-y|$.

> [!note] 📋 Definición — Discontinuidad
>
> Una función $f:D\to\mathbb R$ es **discontinua en $a\in D$** cuando no es continua en ese punto.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Continuidad_y_Límites_01.svg]]
>
> **Se lee así:** desde “discontinuidad en $a$” se decide primero si es evitable. Las no evitables se separan en salto finito, salto infinito y oscilación; cada rama termina en la comparación de límites laterales que la identifica.
>
> **Por qué importa:** clasificar exige responder primero si el límite existe, y solo después si coincide o no con $f(a)$. Ese orden evita llamar “evitable” a un salto.
>
> **Ejemplo:** $f(x)=\sin(1/x)$ para $x\ne0$ es esencial en $0$ porque no tiene límite.

---

## 📊 Álgebra, Discontinuidades y Algoritmo

> [!info] 📊 Álgebra de funciones continuuas
>
> Si $f$ y $g$ son continuas en $a$, también lo son:
>
> | Operación | Fórmula | Condición |
> |---|---|---|
> | Suma | $(f+g)(x)=f(x)+g(x)$ | Siempre |
> | Producto | $(fg)(x)=f(x)g(x)$ | Siempre |
> | Cociente | $(f/g)(x)=f(x)/g(x)$ | $g(a)\ne0$ |
> | Composición | $(f\circ g)(x)=f(g(x))$ | $g$ continua en $a$ y $f$ continua en $g(a)$ |
> | Valor absoluto | $|f(x)|$ | Siempre |
>
> **Mnemotecnia:** **S**uma **P**roducto **C**ociente **C**omposición **A**bsoluto = **SPCCA**.

> [!note] 📋 Taxonomía de discontinuidades
>
> | Tipo | Condición | Comportamiento | Ejemplo |
> |---|---|---|---|
> | Evitable o removible | El límite existe y es distinto de $f(a)$ | Se repara redefiniendo $f(a)$ | $\sin x/x$ con $f(0)=0$ |
> | Salto finito | Límites laterales finitos y distintos | La gráfica salta | $x+1$ para $x<0$; $x+2$ para $x\ge0$ |
> | Salto infinito | Un límite lateral es infinito | Rama vertical | $1/x$ en $0$ |
> | Esencial u oscilante | El límite no existe por oscilación | La curva no tiene dirección de llegada | $\sin(1/x)$ en $0$ |
>
> **Ejemplo de salto:** para $f(x)=x+1$ si $x<0$ y $f(x)=x+2$ si $x\ge0$, los límites laterales son $1$ y $2$; el salto mide $2-1=1$.
>
> **Ejemplo infinito:** para $f(x)=1/x$, $\lim_{x\to0^-}f(x)=-\infty$ y $\lim_{x\to0^+}f(x)=+\infty$.

> [!tip] 🔍 Algoritmo para analizar $a$
>
> 1. **Dominio:** ¿Está $a$ en el dominio?
> 2. **Límites:** calcular $\lim_{x\to a^-}f(x)$ y $\lim_{x\to a^+}f(x)$.
> 3. **Comparar:** ¿son iguales?
> 4. **Evaluar:** calcular $f(a)$.
> 5. **Decidir:** clasificar según la tabla.
>
> **Mnemotecnia:** **D**ominio **L**ímites **C**omparar **E**valuar **D**ecidir = **DLCED**.

> [!tip] 🎯 Método TRACE
>
> - **T**ipo: identificar la función y sus posibles discontinuidades.
> - **R**ango: determinar el intervalo de estudio.
> - **A**nálisis: examinar límites y valores.
> - **C**lasificar: distinguir continuidad puntual y uniforme.
> - **E**jemplos: construir contraejemplos cuando el criterio no basta.
>
> **Mnemotecnias:** discontinuidades **E**vitable, **S**alto, **I**nfinita, **E**sencial = **ESIE**; valor intermedio **C**ontinua, **I**ntermedia, **V**alor, **A**lcanza = **CIVA**.

---

## 🌉 Teorema del Valor Intermedio

> [!success] 🌉 Teorema del Valor Intermedio
>
> Si $f$ es continua en $[a,b]$ y $k$ está entre $f(a)$ y $f(b)$, entonces existe $c\in(a,b)$ tal que $f(c)=k$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Continuidad_y_Límites_02.svg]]
>
> **Se lee así:** dos cadenas horizontales coordinan el dominio y la imagen. La superior pasa de $f(a)$ por $k$ hasta $f(b)$; la inferior pasa de $a$ por $c$ hasta $b$. Las flechas cruzadas emparejan cada valor con el punto donde se alcanza.
>
> **Por qué importa:** sin continuidad, una curva puede saltarse un valor intermedio. El diagrama muestra exactamente qué dato falta al salir del eje vertical: el punto $c$ del eje horizontal.
>
> **Ejemplo:** $f(x)=x^3+x-1$ es continua y $f(0)=-1$, $f(1)=1$; por TVI tiene una raíz en $(0,1)$.

> [!note] ✅ Condiciones y aplicaciones del TVI
>
> **Condiciones:**
>
> 1. $f$ continua en $[a,b]$.
> 2. $k\in[\min\{f(a),f(b)\},\max\{f(a),f(b)\}]$.
>
> **Existencia de raíces:** si $f$ es continua y $f(a)f(b)<0$, entonces $f(c)=0$ para algún $c\in(a,b)$.
>
> **Ecuaciones trigonométricas:** $g(x)=\cos x-x$ es continua en $[0,\pi/2]$ y cambia de signo, por lo que $\cos x=x$ tiene solución.
>
> **Problema de renta:** si el salario varía continuamente de $1000$ a $5000$, existe alguien que gana exactamente $3000$.

> [!warning] ⚡ Heine-Cantor y Derivada acotada
>
> Toda función continua en un conjunto compacto es uniformemente continua. En particular, si $f$ es continua en $[a,b]$, es uniformemente continua allí.
>
> **Contraejemplo:** $f(x)=1/x$ es continua en cada punto de $(0,1)$ y $(0,1]$, pero no uniformemente continua, porque se dispara al acercarse a $0$.
>
> **Criterio de la derivada:** si $f$ es derivable en $(a,b)$ y $f'$ está acotada, el teorema del valor medio da
> $$|f(x)-f(y)|=|f'(c)|\,|x-y|\le M|x-y|,$$
> y por tanto $f$ es uniformemente continua.
>
> | Función | Intervalo | ¿Uniformemente continua? | Razón |
> |---|---|---|---|
> | $x^2$ | $\mathbb R$ | No | $f'(x)=2x$ no acotada |
> | $x^2$ | $[0,10]$ | Sí | Compacto y continua |
> | $\sin x$ | $\mathbb R$ | Sí | Lipschitz con constante $1$ |
> | $1/x$ | $(0,1]$ | No | Crece sin control cerca de $0$ |
> | $\sqrt x$ | $[0,\infty)$ | Sí | $|f'(x)|\le1$ para $x>0$ |

> [!info] 🖼️ Árbol de decisiones para continuidad
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Continuidad_y_Límites_03.svg]]
>
> **Se lee así:** el árbol pregunta primero si la función es continua. Si no, conduce a la clasificación de sus discontinuidades; si sí, pregunta por un dominio compacto y luego por la derivada acotada, terminando en uniformemente continua, en la definición epsilon-delta o en la conclusión de continuidad solo puntual.
>
> **Por qué importa:** ordena el análisis en dos niveles, local y global, y evita confundir “continua” con “uniformemente continua”.
>
> **Ejemplo:** para $f(x)=1/x$ en $(0,1]$, la función es continua pero $f'(x)=-1/x^2$ no está acotada; el diagrama conduce a la rama de continuidad solo puntual.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Analiza la continuidad de
> $$f(x)=\begin{cases}\frac{\sin x}{x},&x\ne0,\\0,&x=0.\end{cases}$$
> Clasifica la discontinuidad en $0$ y propón una reparación.
>
> > [!success]- ✅ Solución
> >
> > Como $\lim_{x\to0}\sin x/x=1$ y $f(0)=0$, el límite bilateral existe pero no coincide con el valor. La discontinuidad en $0$ es evitable. Se repara definiendo $f(0)=1$.

> [!example] 📋 Planteamiento
>
> Para
> $$f(x)=\begin{cases}x+1,&x<0,\\x+2,&x\ge0,\end{cases}$$
> calcula los límites laterales, clasifica la discontinuidad y encuentra el tamaño del salto.
>
> > [!success]- ✅ Solución
> >
> > $\lim_{x\to0^-}f(x)=1$ y $\lim_{x\to0^+}f(x)=2$. Los límites laterales son finitos y distintos, por lo que hay discontinuidad de salto finito. El salto es $|2-1|=1$.

> [!example] 📋 Planteamiento
>
> Demuestra que $x^3+x-1$ tiene una raíz en $(0,1)$ y que $\cos x=x$ tiene una solución en $(0,\pi/2)$. En ambos casos, identifica la continuidad y el cambio de signo.
>
> > [!success]- ✅ Solución
> >
> > Ambos polinomios son continuos. Para el primero, $f(0)=-1<0$ y $f(1)=1>0$; TVI da una raíz. Para el segundo, $g(x)=\cos x-x$ es continua y $g(0)=1>0$, mientras $g(\pi/2)=-\pi/2<0$; TVI da una solución.

> [!example] 📋 Planteamiento
>
> Determina si $f(x)=1/x$ es uniformemente continua en $(0,1]$. Justifica con el teorema del valor medio o con un contraejemplo explícito.
>
> > [!success]- ✅ Solución
> >
> > No lo es. En $(0,1]$, $f'(x)=-1/x^2$ no está acotada, de modo que el criterio de derivada acotada no se cumple. Además, para $\varepsilon=1$ se pueden elegir $x_n=1/(2n)$ y $y_n=1/(3n)$: $|x_n-y_n|\to0$, pero $|f(x_n)-f(y_n)|=n\to\infty$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico continuidad con la definición epsilon-delta.
> - [ ] Relaciono continuidad con límites bilaterales y laterales.
> - [ ] Clasifico una discontinuidad usando el algoritmo DLCED.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico TVI para probar existencia de raíces.
> - [ ] Distingo continuidad puntual y uniforme.
> - [ ] Uso Heine-Cantor y el criterio de derivada acotada para justificar uniformidad.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> - J. Stewart, *Cálculo*, temas de continuidad y teorema del valor intermedio.
> - G. B. Thomas, *Cálculo*, secciones de continuidad y límites.
> - Material de cátedra de MATG1045.
> - EXA-2023-0S-CÁLCULO DE UNA VARIABLE-1-1Par.pdf, p. 2: práctica de límites y continuidad; se cita como enlace de estudio, sin incrustar el PDF.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Definición epsilon-delta de continuidad?::Para cada ε existe δ tal que $|x-a|<δ$ implica $|f(x)-f(a)|<ε$.
> - ¿Equivalencia clave?::$\lim_{x\to a}f(x)=f(a)$.
> - ¿Cociente no definido?::Se discontinuidad evitable si el límite existe, y removable si se puede redefinir para continuarla.
> - ¿Tipos de discontinuidad?::Evitable, salto finito, salto infinito y esencial u oscilante.
> - ¿TVI?::Una función continua en $[a,b]$ toma todos los valores entre $f(a)$ y $f(b)$.
> - ¿Continuidad uniforme?::Un mismo δ para todos los pares $x,y$ del dominio.
> - ¿Heine-Cantor?::Toda función continua en un compacto es uniformemente continua.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[../Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|Concepto y Definición Formal del Límite]] — base de la continuidad.
> - [[../Unidad 1 - Preliminares/02 - Puntos de Acumulación|Puntos de Acumulación]] —fundamento topológico de la cercanía.
> - [[../Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|Derivabilidad y Continuidad]] — relación entre continuidad y derivabilidad.
> - [[02 - Asíntotas y Comportamiento de Funciones]] — usa límites para describir ramas infinitas.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Revisa [[../Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|Concepto y Definición Formal del Límite]] antes de usar TVI.
> - Continúa con [[02 - Asíntotas y Comportamiento de Funciones]].
> - Practica primero límites laterales y después clasificación de discontinuidades.
> - Para la Derivada, conecta continuidad con [[../Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|Derivabilidad y Continuidad]].

---

**Tags:** #MATG1045 #unidad3 #continuidad #limites #discontinuidades #valor-intermedio #continuidad-uniforme

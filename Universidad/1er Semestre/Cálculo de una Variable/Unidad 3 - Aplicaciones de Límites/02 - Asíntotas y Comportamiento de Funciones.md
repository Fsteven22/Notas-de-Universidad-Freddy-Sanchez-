---
dg-publish: true
tags: [MATG1045, unidad3, asintotas, comportamiento-de-funciones, limites, graficas, funciones-racionales]
---

# 📐 Asíntotas y Comportamiento de Funciones

## 🎯 Introducción

> [!info] 💡 ¿Qué información da una asíntota?
>
> Una asíntota describe el comportamiento de una curva en una dirección importante: al acercarse a un punto problemático o al alejarse hacia el infinito. No es solo una recta auxiliar para el dibujo; es la traducción gráfica de un límite.
>
> El análisis se organiza en tres familias. Una vertical $x=a$ corresponde a un límite infinito al acercarse a $a$. Una horizontal $y=L$ corresponde a un límite finito al llegar a $\pm\infty$. Una oblicua $y=mx+b$ corresponde a una recta a la que la función se aproxima con error tendente a cero.
>
> **Ejemplo:** $f(x)=1/(x-2)$ tiene asíntota vertical $x=2$ y asíntota horizontal $y=0$. La primera describe cada rama; la segunda, su comportamiento final.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Asíntota
>
> Una **asíntota** de $f$ es una recta a la que la gráfica de $f$ se aproxima indefinidamente sin intersectarla salvo, como máximo, en un número finito de puntos. En esta materia se estudian las asíntotas vertical, horizontal y oblicua.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Asíntotas_y_Comportamiento_de_Funciones_02.svg]]
>
> **Se lee así:** una caja central de asíntota abre en tres ramas: vertical, horizontal y oblicua. Cada rama incluye la dirección de análisis y el límite o diferencia que la define; las dos últimas rejoinan en la idea de comportamiento final.
>
> **Por qué importa:** el diagrama impide mezclar las direcciones: una vertical se detecta al acercarse a un punto, mientras las otras se detectan al alejarse.
>
> **Ejemplo:** la curva $y=\log x$ se aproxima al eje $x=0$ sin tocarlo; esa recta es su asíntota vertical.

> [!note] 📋 Definición — Asíntota horizontal
>
> La recta $y=L$ es una **asíntota horizontal** de $f$ si
> $$\lim_{x\to+\infty}f(x)=L\quad\text{o}\quad\lim_{x\to-\infty}f(x)=L.$$
> Puede haber una asíntota en cada dirección y sus valores pueden ser distintos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Asíntotas_y_Comportamiento_de_Funciones_03.svg]]
>
> **Se lee así:** primero se analizan las dos direcciones hacia el infinito. Una decisión exige un límite finito; la rama verde conduce a la asíntota horizontal, mientras los límites infinitos o inexistentes la descartan. Las cajas finales resumen el criterio para racionales.
>
> **Por qué importa:** una asíntota horizontal no afirma que la función esté limitada en todo su dominio, solo en una dirección hacia el infinito.
>
> **Ejemplo:** si $f(x)=(3x^2+2x-1)/(x^2-4)$, los grados son iguales y la asíntota es $y=3$.

> [!note] 📋 Definición — Asíntota vertical
>
> La recta $x=a$ es una **asíntota vertical** de $f$ si
> $$\lim_{x\to a^-}f(x)=\pm\infty\quad\text{o}\quad\lim_{x\to a^+}f(x)=\pm\infty.$$
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Asíntotas_y_Comportamiento_de_Funciones_04.svg]]
>
> **Se lee así:** se parten de los candidatos donde la función no está definida y se decide con límites laterales infinitos. La rama verde distingue vertical simple, vertical con salto y vertical unilateral; una discontinuidad evitable se descarta.
>
> **Por qué importa:** el candidato no basta: $x=2$ puede ser un hueco reparable o una vertical. Solo el crecimiento infinito confirma la asíntota.
>
> **Ejemplo:** $f(x)=1/(x-2)$ satisface $\lim_{x\to2^-}f(x)=-\infty$ y $\lim_{x\to2^+}f(x)=+\infty$.

> [!note] 📋 Definición — Asíntota oblicua
>
> La recta $y=mx+b$ es una **asíntota oblicua** de $f$ si
> $$\lim_{x\to\pm\infty}\bigl(f(x)-(mx+b)\bigr)=0.$$
> La pendiente y el intercepto se calculan por
> $$m=\lim_{x\to\pm\infty}\frac{f(x)}x,\qquad b=\lim_{x\to\pm\infty}\bigl(f(x)-mx\bigr),$$
> siempre que ambos límites existan y sean finitos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Asíntotas_y_Comportamiento_de_Funciones_05.svg]]
>
> **Se lee así:** la búsqueda empieza con una recta candidata. Se calcula la pendiente como crecimiento relativo, se verifica que sea finita y luego se calcula el intercepto; solo si ambos controles pasan se declara la asíntota.
>
> **Por qué importa:** el error debe ser la distancia vertical entre curva y recta, no solo la razón $f(x)/x$. Calcular únicamente $m$ no basta.
>
> **Ejemplo:** para $f(x)=(x^2+x+1)/(x+1)$, $m=1$ y $b=0$; por tanto la asíntota es $y=x$.

> [!note] 📋 Definición — Asíntota vertical, horizontal y oblicua
>
> Una asíntota vertical $x=a$ exige crecimiento infinito al acercarse a $a$; una horizontal $y=L$ exige un límite finito al alejarse; una oblicua $y=mx+b$ exige que la diferencia vertical con la recta tienda a cero al alejarse.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Asíntotas_y_Comportamiento_de_Funciones_02.svg]]
>
> **Se lee así:** las tres definiciones parallelas parten de $x\to a$ o $x\to\pm\infty$ y terminan, respectivamente, en una recta vertical, horizontal o inclinada.
>
> **Por qué importa:** memorizar una sola fórmula sin la dirección lleva a Buscar asíntotas donde no las hay.
>
> **Ejemplo:** $f(x)=x+2/x$ tiene $y=x$ como asíntota oblicua; no puede tener horizontal en la misma dirección.

---

## 🔎 Técnicas para Encontrar Asíntotas

> [!info] 📊 Asíntotas horizontales
>
> | Comportamiento | $\lim_{x\to+\infty}f$ | $\lim_{x\to-\infty}f$ | Asíntotas |
> |---|---|---|---|
> | Estable | $L$ | $L$ | Una: $y=L$ |
> | Bifurcado | $L_1$ | $L_2$ | Dos: $y=L_1$, $y=L_2$ |
> | Parcial | $L$ | $\pm\infty$ | Una: $y=L$ |
> | Explosivo | $\pm\infty$ | $\pm\infty$ | Ninguna |
>
> **Por qué importa:** una función puede tener dos asíntotas horizontales, una por dirección. Buscar solo en $+\infty$ deja casos incompletos.

> [!warning] 🔍 Criterios por tipo de función
>
> **Funciones racionales** $f=P/Q$:
>
> - Si $\deg P<\deg Q$, hay asíntota horizontal $y=0$.
> - Si $\deg P=\deg Q$, hay $y=a_n/b_n$, cociente de coeficientes principales.
> - Si $\deg P>\deg Q$, no hay asíntota horizontal.
>
> **Exponenciales:**
>
> - $\lim_{x\to+\infty}e^x=+\infty$ y $\lim_{x\to-\infty}e^x=0$.
> - $\lim_{x\to+\infty}e^{-x}=0$ y $\lim_{x\to-\infty}e^{-x}=+\infty$.
>
> **Trigonométricas y relacionadas:**
>
> - $\lim_{x\to\pm\infty}\sin x/x=0$.
> - $\sin x$ y $\cos x$ no tienen asíntotas horizontales porque oscilan.
>
> **Mnemotecnia:** **H**orizontal, **V**ertical, **O**blicua = **HVO**.

> [!warning] ↕️ Algoritmo para asíntotas verticales
>
> 1. Identificar valores donde $f$ no está definida.
> 2. Verificar que no sean discontinuidades evitables.
> 3. Calcular ambos límites laterales.
> 4. Clasificar el comportamiento.
> 5. Confirmar visualmente la gráfica.
>
> | Límites laterales | Tipo | Comportamiento |
> |---|---|---|
> | $+\infty,+\infty$ | Vertical simple | Ambos lados suben |
> | $-\infty,-\infty$ | Vertical simple | Ambos lados bajan |
> | $+\infty,-\infty$ | Vertical con salto | Un lado sube y otro baja |
> | $-\infty,+\infty$ | Vertical con salto | Un lado baja y otro sube |
>
> **Fuentes comunes:** denominadores que se anulan, logaritmos de expresiones que tienden a $0^+$, tangentes en múltiplos impares de $\pi/2$ y raíces con exponentes negativos.

> [!warning] ↗️ Algoritmo para asíntotas oblicuas
>
> 1. Verificar que no exista asíntota horizontal en esa dirección.
> 2. Calcular $m=\lim f(x)/x$.
> 3. Si $m$ es finito, calcular $b=\lim(f(x)-mx)$.
> 4. Si $b$ es finito, declarar $y=mx+b$.
> 5. Repetir en la dirección opuesta si corresponde.
>
> **Casos especiales:**
>
> - Si $m=0$, el resultado es una asíntota horizontal $y=b$.
> - Si $m=\pm\infty$ o $b=\pm\infty$, no hay asíntota oblicua.
> - Hay como máximo una asíntota oblicua por dirección.
>
> **Mnemotecnia de búsqueda:** **P**rimero **H**orizontales, **L**uego **V**erticales, **F**inalmente **O**blicuas = **PHLFO**.

> [!example] 🎯 Ejemplos horizontales
>
> 1. $f(x)=\frac{3x^2+2x-1}{x^2-4}$: grados iguales; $y=3$.
> 2. $f(x)=\frac{2x-1}{x^2+1}$: grado del numerador menor; $y=0$.
> 3. $f(x)=2+\frac3x$: ambos límites son $2$; $y=2$.
> 4. $f(x)=xe^{-x}$: $xe^{-x}\to0$ en ambas direcciones; $y=0$.
>
> **Por qué importa:** el mismo resultado puede obtenerse por cociente de grados o por estructura de la expresión.

> [!example] 🎪 Ejemplos verticales
>
> 1. $f(x)=1/(x-2)$: límites $-\infty$ y $+\infty$; asíntota vertical con salto en $x=2$.
> 2. $f(x)=x^2/(x-1)^2$: ambos límites $+\infty$; vertical simple en $x=1$.
> 3. $f(x)=\ln(x-3)$: el límite derecho es $-\infty$ y el dominio exige $x>3$; vertical unilateral en $x=3$.
> 4. $f(x)=\frac{x^2-4}{x-2}=x+2$ para $x\ne2$: hueco evitable; **no** hay asíntota vertical en $2$.
>
> **Por qué importa:** el último caso evita el error de_llamar asíntota a cualquier raíz del denominador.

> [!example] 🔬 Ejemplos oblicuas
>
> Para $f(x)=\frac{x^2+x+1}{x+1}$:
> $$m=\lim_{x\to+\infty}\frac{x^2+x+1}{x(x+1)}=1,$$
> $$b=\lim_{x\to+\infty}\left(\frac{x^2+x+1}{x+1}-x\right)=\lim_{x\to+\infty}\frac1{x+1}=0.$$
> Así, $y=x$ es asíntota oblicua.
>
> Para $f(x)=x+\frac2x$:
> $$m=\lim_{x\to\pm\infty}\left(1+\frac2{x^2}\right)=1,\qquad b=\lim_{x\to\pm\infty}\frac2x=0.$$
> También $y=x$ es asíntota oblicua.

---

## 📈 Análisis y Graficación

> [!tip] 📊 Método GRAPH
>
> - **G**ráfica preliminar: esbozar el comportamiento general.
> - **R**estricciones: identificar dominio y puntos problemáticos.
> - **A**síntotas: encontrar vertical, horizontal y oblicua.
> - **P**untos clave: interceptos, extremos e inflexiones.
> - **H**erramientas: usar derivadas para el análisis completo.
>
> **Por qué importa:** el orden evita dibujar una rama sin conocer la asíntota que la limita o identificar una asíntota antes de revisar el dominio.
>
> **Ejemplo:** para $1/(x-2)$, primero se detecta $x=2$ como candidata; los límites infinito y finito confirman la vertical $x=2$ y la horizontal $y=0$.

> [!info] 🖼️ Guía completa de graficación
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Asíntotas_y_Comportamiento_de_Funciones_01.svg]]
>
> **Se lee así:** desde la función se recorre dominio y recorrido, asíntotas, interceptos y comportamiento global. De este último salen cuatro ramas: vertical, horizontal, oblicua y funciones sin asíntota; la vertical añade la definición por límite infinito y el ejemplo $1/(x-2)$.
>
> **Por qué importa:** ofrece una checklist reutilizable para graficar sin saltar pasos ni confundir asíntota con una tendencia aproximada.
>
> **Ejemplo:** al graficar $1/(x-2)$, el diagrama conduce a $x=2$, divide la gráfica en dos ramas y luego exige describir el comportamiento final con $y=0$.

> [!note] 📖 Tipos de límites infinitos
>
> - “Sube, sube”: ambos lados tienden a $+\infty$.
> - “Baja, baja”: ambos lados tienden a $-\infty$.
> - “Sube, baja”: el lado izquierdo sube y el derecho baja.
> - “Baja, sube”: el lado izquierdo baja y el derecho sube.
>
> **Mnemotecnia:** **SSBB-SB-BS**.
>
> **Por qué importa:**（左）right describe una vertical simple y el resto una vertical con salto.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Determina las asíntotas verticales, horizontales y oblicuas de
> $$f(x)=\frac{x^2+3x-2}{x-4}.$$
> Justifica cada una.
>
> > [!success]- ✅ Solución
> >
> > En $x=4$, el numerador vale $16+12-2=26\ne0$, por lo que
> > $$\lim_{x\to4^-}f(x)=-\infty,\qquad \lim_{x\to4^+}f(x)=+\infty.$$
> > Hay asíntota vertical $x=4$. Como $\deg P=2>1=\deg Q$, no hay horizontal. Al dividir,
> > $$f(x)=x+7+\frac{26}{x-4},$$
> > y el término residual tiende a cero en ambas direcciones; la asíntota oblicua es $y=x+7$.

> [!example] 📋 Planteamiento
>
> Analiza $f(x)=\frac{2x-1}{x^2+1}$ y $g(x)=2+\frac3x$ por asíntotas horizontales.
>
> > [!success]- ✅ Solución
> >
> > En $f$, $\deg P=1<2=\deg Q$, por tanto $\lim_{x\to\pm\infty}f(x)=0$ y $y=0$ es horizontal. En $g$, $\lim_{x\to\pm\infty}(2+3/x)=2$, de modo que $y=2$ es horizontal. Ninguna de las dos tiene asíntota vertical: sus denominadores no se anulan en $\mathbb R$.

> [!example] 📋 Planteamiento
>
> Explica por qué $h(x)=\frac{x^2-4}{x-2}$ no tiene asíntota vertical en $x=2$, aunque $x=2$ sea raíz del denominador.
>
> > [!success]- ✅ Solución
> >
> > Para $x\ne2$, $h(x)=x+2$. El límite bilateral en $2$ es $4$, finito, por lo que la discontinuidad es evitable y no hay crecimiento infinito. La raíz del denominador es solo un candidato; deben calcularse los límites laterales.

> [!example] 📋 Planteamiento
>
> Calcula la asíntota oblicua de $f(x)=\frac{x^3+1}{x^2-1}$ en $x\to+\infty$.
>
> > [!success]- ✅ Solución
> >
> > Se factoriza $x^3+1=(x+1)(x^2-x+1)$ y $x^2-1=(x-1)(x+1)$, de modo que $f(x)=\frac{x^2-x+1}{x-1}$ para $x\ne\pm1$. Entonces
> > $$m=\lim_{x\to+\infty}\frac{f(x)}x=1,$$
> > $$b=\lim_{x\to+\infty}(f(x)-x)=\lim_{x\to+\infty}\frac{-2x+1}{x-1}=-2.$$
> > La asíntota es $y=x-2$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo asíntota vertical, horizontal y oblicua por su dirección de análisis.
> - [ ] Aplico el criterio de grados a funciones racionales.
> - [ ] Identifico una vertical mediante límites laterales.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo $m$ y $b$ para una asíntota oblicua.
> - [ ] Distingo una discontinuidad evitable de una vertical.
> - [ ] Construyo una gráfica usando el método GRAPH.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> - J. Stewart, *Cálculo*, comportamiento de funciones y asíntotas.
> - G. B. Thomas, *Cálculo*, asíntotas y análisis de funciones racionales.
> - Material de cátedra de MATG1045.
> - EXA-2023-0S-CÁLCULO DE UNA VARIABLE-1-2Par.pdf, p. 2: práctica de análisis de funciones; enlace de estudio, sin incrustación.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Asíntota vertical?::$x=a$ con al menos un límite lateral infinito al acercarse a $a$.
> - ¿Asíntota horizontal?::$y=L$ con límite $L$ finito en $x\to+\infty$ o $x\to-\infty$.
> - ¿Asíntota oblicua?::$y=mx+b$ con $f(x)-(mx+b)\to0$ al infinito.
> - ¿Cómo se calculan $m$ y $b$?::$m=\lim f(x)/x$ y $b=\lim(f(x)-mx)$, si son finitos.
> - ¿Racional con grado P menor que Q?::Asíntota horizontal $y=0$.
> - ¿Racional con grados iguales?::Asíntota horizontal $y=a_n/b_n$.
> - ¿Una raíz del denominador garantiza vertical?::No; se deben verificar límites laterales infinitos.
> - ¿Mnemotecnia HVO?::Horizontal, vertical, oblicua.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Continuidad y Límites]] — clasifica las discontinuidades y las verticales.
> - [[../Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|Límites al Infinito y Sucesiones]] — base de horizontales y oblicuas.
> - [[../Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|Límites Laterales]] — base de verticales.
> - [[../Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|Análisis Completo de Funciones]] — completa el estudio con derivadas.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Revisa límites laterales antes de buscar verticales.
> - Continúa con [[../Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|Análisis Completo de Funciones]].
> - Usa [[../Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|Límites al Infinito y Sucesiones]] para justificar cada dirección.
> - Dibuja primero las asíntotas y luego usa la tabla de límites infinitos para separar ramas.

---

**Tags:** #MATG1045 #unidad3 #asintotas #comportamiento-de-funciones #limites #graficas #funciones-racionales

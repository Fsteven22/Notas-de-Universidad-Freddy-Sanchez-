---
dg-publish: true
tags: [MATG1045, unidad4, derivabilidad, continuidad, teorema-implicacion, contraejemplos, derivadas-laterales, clasificacion-puntos, mnemotecnia]
---

# 🔗 Derivabilidad y Continuidad

## 🎯 Introducción

> [!info] 💡 La relación fundamental
>
> La relación entre derivabilidad y continuidad es uno de los conceptos más importantes del análisis matemático. Aunque están íntimamente conectadas, **no son equivalentes**: toda función derivable es continua, pero no toda función continua es derivable.
>
> **Por qué importa:** esa flecha de un solo sentido gobierna todo el curso: antes de analizar una función con derivadas hay que saber que la continuidad es el paso previo obligado, y que ver que "se ve continua" no basta para afirmar que se puede derivar.
>
> **Ejemplo:** $f(x) = |x|$ es continua en $0$ pero no derivable ahí; en cambio $f(x) = x^2$ cumple las dos.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Continuidad en un punto
>
> Una función $f(x)$ es **continua en $x = a$** si se cumplen tres condiciones:
>
> 1. **$f(a)$ existe:** la función está definida en $a$.
> 2. **$\lim_{x \to a} f(x)$ existe.**
> 3. **$\lim_{x \to a} f(x) = f(a)$:** el límite coincide con el valor de la función.
>
> Equivalentemente, basta la tercera condición con las dos primeras implícitas: $\lim_{x \to a} f(x) = f(a)$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivabilidad_y_Continuidad_04.svg]]
>
> **Se lee así:** el esquema es un filtro de tres decisiones encadenadas: primero pregunta si $f(a)$ está definida, después si existe el límite cuando $x$ tiende a $a$ y por último si ese límite es igual a $f(a)$. Cada "no" lleva a su diagnóstico (sin definición, límite inexistente, discontinuidad evitable o de salto) y el "sí" triple termina en la casilla de **continua en $a$**.
>
> **Por qué importa:** el orden de los rombos es el mismo orden en que debes comprobar la continuidad en un ejercicio. Saltarse el primer rombo (¿está definida?) es el error más frecuente cuando la función se define por partes.
>
> **Ejemplo:** para $f(x) = \frac{x^2-1}{x-1}$ en $x = 1$ el primer rombo falla: $f(1)$ no existe, así que la función no es continua ahí, aunque el límite sí exista.

> [!note] 📋 Definición — Derivabilidad en un punto
>
> Una función $f(x)$ es **derivable (diferenciable) en $x = a$** si existe y es finito el límite
>
> $$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}.$$
>
> **Derivadas laterales:** $f'_+(a) = \lim_{h \to 0^+} \frac{f(a+h)-f(a)}{h}$ y $f'_-(a) = \lim_{h \to 0^-} \frac{f(a+h)-f(a)}{h}$. Se tiene
>
> $$f'(a) \text{ existe} \iff f'_+(a) = f'_-(a) = \text{valor finito}.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivabilidad_y_Continuidad_05.svg]]
>
> **Se lee así:** el esquema arranca en la derivabilidad y forma el cociente incremental; un rombo pregunta si su límite existe y es finito. Si no existe, la rama baja a calcular las derivadas laterales y otro rombo exige que sean iguales y finitas; si el primer límite existe, la ruta va directo. Ambas rutas terminan en la casilla de **derivada existente**, de la que sale la conclusión de que la función es continua en el punto.
>
> **Por qué importa:** el diagrama muestra que las derivadas laterales son el plan B cuando el límite "a la vista" falla, y que el veredicto final siempre arrastra la continuidad. Es el criterio que aplicas en los ejercicios con funciones por partes.
>
> **Ejemplo:** en $f(x) = |x|$ en $0$, el primer rombo falla (los laterales dan $1$ y $-1$), la rama de laterales también y la conclusión es: no derivable.

---

## 🧠 Teorema: derivabilidad implica continuidad

> [!warning] 📋 Teorema fundamental
>
> Si $f$ es derivable en $x = a$, entonces $f$ es continua en $x = a$:
>
> $$f'(a) \text{ existe} \Rightarrow f \text{ es continua en } a.$$
>
> **En sentido contrario no vale:** hay funciones continuas que no son derivables.
>
> **Por qué importa:** este teorema te ahorra trabajo en dos direcciones: si sabes que una función es derivable, ya tienes la continuidad gratis; y si encuentras una discontinuidad, puedes descartar de entrada que sea derivable ahí.

> [!tip] 🔬 Demostración
>
> **Queremos probar:** $\lim_{x \to a} f(x) = f(a)$, dado que $f'(a)$ existe.
>
> $$\lim_{h \to 0} [f(a+h) - f(a)] = \lim_{h \to 0} \left[\frac{f(a+h) - f(a)}{h} \cdot h\right] = f'(a) \cdot 0 = 0.$$
>
> Por lo tanto $\lim_{h \to 0} f(a+h) = f(a)$, y cambiando a la variable $x = a + h$ queda $\lim_{x \to a} f(x) = f(a)$: la función es continua en $a$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivabilidad_y_Continuidad_01.svg]]
>
> **Se lee así:** es una cadena de rectángulos que va de arriba abajo: parte de que la función es derivable, pasa por el cociente de la definición, multiplica por el incremento, llega a la igualdad de límites y termina en la conclusión de que la función es continua en ese punto. Cada caja es un paso algebraico encadenado.
>
> **Por qué importa:** fíjate en que no es un recíproco: derivable **implica** continua, pero continua no implica derivable. Tener esta demostración en un diagrama te da el argumento limpio que necesitas en el examen.
>
> **Ejemplo:** como contraejemplo del recíproco, $f(x) = |x|$ en $x = 0$ es continua, pero sus derivadas laterales valen $-1$ y $1$, así que no es derivable.

> [!warning] 🔴 El recíproco NO es cierto: $f(x) = |x|$
>
> **Continuidad en $x = 0$:** $f(0) = 0$; $\lim_{x \to 0} |x| = 0$; y $0 = f(0)$. Continua ✔
>
> **Derivabilidad en $x = 0$:**
>
> $$f'(0) = \lim_{h \to 0} \frac{|h|}{h}.$$
>
> - Por la derecha: $\lim_{h \to 0^+} \frac{h}{h} = 1$.
> - Por la izquierda: $\lim_{h \to 0^-} \frac{-h}{h} = -1$.
>
> Como $1 \neq -1$, el límite no existe.
>
> **Conclusión:** $f(x) = |x|$ es continua pero **no** derivable en $x = 0$.
>
> **Interpretación geométrica:** la continuidad significa que la gráfica no tiene saltos ni huecos; la no derivabilidad significa que hay un **pico o esquina** donde no se puede trazar una tangente única.
>
> **Por qué importa:** este es el contraejemplo que hay que citar cada vez que alguien afirme que "continua equivale a derivable".

---

## 🔍 Clasificación de puntos y ejemplos

> [!tip] 🎯 Los cuatro tipos de punto
>
> | Tipo | Continua | Derivable | Ejemplo | Descripción |
> |---|---|---|---|---|
> | **A** | Sí | Sí | $f(x) = x^2$ en $x = 1$ | Función suave |
> | **B** | Sí | No | $f(x) = |x|$ en $x = 0$ | Esquina o pico |
> | **C** | No | No | Discontinuidad de salto | Salto finito |
> | **D** | No | No | $f(x) = \frac{1}{x}$ en $x = 0$ | Discontinuidad infinita |
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivabilidad_y_Continuidad_02.svg]]
>
> **Se lee así:** es un diagrama de clasificación con dos decisiones encadenadas: primero un rombo pregunta si el punto es continuo y, si no, se cierra como caso no derivable; si lo es, un segundo rombo pregunta si es derivable y separa el punto entre función suave o esquina o cúspide. Cada salida lleva rotulada su categoría.
>
> **Por qué importa:** te da una manera ordenada de etiquetar cada punto crítico de una gráfica: primero continuidad, después derivabilidad. Con eso evitas decir que una función con pico es derivable solo porque se ve continua.
>
> **Ejemplo:** para $f(x) = |x - 2|$ en $x = 2$ el diagrama marca tipo B: continua porque $\lim_{x \to 2}|x-2| = 0 = f(2)$, pero con esquina y derivadas laterales distintas.

> [!example] 📈 Tipo A: función suave, $f(x) = x^3 - 2x + 1$ en $x = 1$
>
> **Continuidad:** $\lim_{x \to 1} (x^3 - 2x + 1) = 1 - 2 + 1 = 0 = f(1)$ ✔
>
> **Derivabilidad por la definición:**
>
> $$f'(1) = \lim_{h \to 0} \frac{(1+h)^3 - 2(1+h) + 1 - 0}{h} = \lim_{h \to 0} \frac{h + 3h^2 + h^3}{h} = \lim_{h \to 0} (1 + 3h + h^2) = 1.$$
>
> **Conclusión:** continua y derivable en $x = 1$, con $f'(1) = 1$ (tipo A).

> [!example] 🔺 Tipo B: esquina, $f(x) = |x - 2|$ en $x = 2$
>
> **Continuidad:** $\lim_{x \to 2} |x - 2| = 0 = f(2)$ ✔
>
> **Derivabilidad:** $f'(2) = \lim_{h \to 0} \frac{|h|}{h}$; por la derecha vale $1$ y por la izquierda $-1$.
>
> **Conclusión:** continua pero no derivable en $x = 2$ (tipo B).

> [!example] 📊 Tipo C: discontinuidad de salto
>
> $$f(x) = \begin{cases} x+1 & \text{si } x < 0 \\ x-1 & \text{si } x \geq 0 \end{cases} \quad \text{en } x = 0.$$
>
> **Continuidad:** $f(0) = -1$; $\lim_{x \to 0^-} f = 1$; $\lim_{x \to 0^+} f = -1$. Los laterales no coinciden, así que no es continua.
>
> **Derivabilidad:** si no es continua, tampoco es derivable (contraposición del teorema fundamental).
>
> **Conclusión:** ni continua ni derivable en $x = 0$ (tipo C).

> [!example] 🌿 Tangente vertical: $f(x) = \sqrt[3]{x}$ en $x = 0$
>
> **Continuidad:** $\lim_{x \to 0} \sqrt[3]{x} = 0 = f(0)$ ✔
>
> **Derivabilidad:** $f'(0) = \lim_{h \to 0} \frac{\sqrt[3]{h}}{h} = \lim_{h \to 0} \frac{1}{h^{2/3}} = +\infty$.
>
> **Conclusión:** continua pero no derivable: la derivada es infinita porque hay tangente vertical. Recuerda que la derivada debe ser **finita**.

> [!info] 🔬 Ejemplo con derivadas laterales: función por partes
>
> $$f(x) = \begin{cases} x^2 & \text{si } x \leq 1 \\ 2x - 1 & \text{si } x > 1 \end{cases} \quad \text{en } x = 1.$$
>
> **Continuidad:** $f(1) = 1$; $\lim_{x \to 1^-} f = 1$; $\lim_{x \to 1^+} f = 2(1) - 1 = 1$. Es continua.
>
> **Derivadas laterales:**
>
> - $f'_-(1) = \lim_{h \to 0^-} \frac{(1+h)^2 - 1}{h} = \lim_{h \to 0^-} (2 + h) = 2$.
> - $f'_+(1) = \lim_{h \to 0^+} \frac{2(1+h) - 1 - 1}{h} = \lim_{h \to 0^+} 2 = 2$.
>
> **Conclusión:** como $f'_-(1) = f'_+(1) = 2$ y es finito, $f$ es derivable en $x = 1$ con $f'(1) = 2$.
>
> **Por qué importa:** este es el caso en el que la definición a la vista no basta: en los puntos donde cambia la expresión hay que calcular las derivadas laterales y compararlas.

---

## 🔧 Condiciones suficientes para derivabilidad

> [!success] ✅ Criterios prácticos
>
> 1. **Funciones elementales:** polinomios, exponenciales, logaritmos y trigonométricas son derivables en todo su dominio.
> 2. **Composición:** si $f$ y $g$ son derivables, entonces $f \circ g$ es derivable (regla de la cadena).
> 3. **Operaciones:** si $f$ y $g$ son derivables, también lo son $f \pm g$, $f \cdot g$ y $\frac{f}{g}$ (con $g \neq 0$).
> 4. **Definidas por partes:** verificar continuidad **y** igualdad de derivadas laterales en cada punto de unión.
>
> **Por qué importa:** los cuatro criterios te dicen qué comprobar y qué puedes dar por supuesto. Con las elementales no pierdas tiempo: su derivabilidad es un teorema, no un ejercicio.
>
> **Ejemplo:** $\frac{\sin x}{1 + x^2}$ es derivable en todo $\mathbb{R}$ por cociente de derivables con denominador nunca cero.

---

## ⚠️ Errores conceptuales comunes

> [!warning] 🚨 Los cuatro malentendidos típicos
>
> 1. **Invertir la implicación:** incorrecto "continua ⟹ derivable"; correcto "derivable ⟹ continua".
> 2. **Asumir derivabilidad sin verificar:** $f(x) = x^{2/3}$ parece suave pero no es derivable en $x = 0$ (tangente vertical).
> 3. **Ignorar los puntos de frontera:** donde cambia la definición de una función por partes hay que verificar derivadas laterales.
> 4. **Confundir la suavidad visual con la derivabilidad:** la apariencia gráfica no prueba nada; la verificación es analítica.
>
> **Por qué importa:** los cuatro son errores de razonamiento que invalidan la conclusión aunque la cuenta esté bien hecha.

> [!tip] 🎓 Mnemotecnia "VERIFICA"
>
> - **V — Verificar continuidad primero:** si no es continua, no puede ser derivable.
> - **E — Examinar la función cerca del punto:** ¿hay esquinas, picos o definición por partes?
> - **R — Revisar la definición por partes:** calcular límites laterales y el valor en el punto de unión.
> - **I — Investigar derivadas laterales:** calcular $f'_+(a)$ y $f'_-(a)$ y comprobar que son iguales y finitas.
> - **F — Formular la conclusión:** decidir si es continua, derivable o ambas, y el tipo de punto (A, B, C o D).
> - **I — Interpretar geométricamente:** ¿qué significa para la gráfica? ¿Hay tangente única?
> - **C — Comprobar con casos conocidos:** contrastar con funciones elementales.
> - **A — Anotar casos especiales:** acumular tu lista de patrones de no derivabilidad.
>
> **Aplicación a $f(x) = x|x|$ en $x = 0$:** la función es continua ($\lim = 0 = f(0)$); no hay esquina visible pero sí cambio de expresión; las derivadas laterales dan $f'_+(0) = \lim_{h \to 0^+} h = 0$ y $f'_-(0) = \lim_{h \to 0^-} (-h) = 0$; al ser iguales, es derivable con $f'(0) = 0$ y tangente horizontal en el origen. Multiplicar $|x|$ por $x$ elimina la esquina.

---

## 🌟 Aplicaciones y consecuencias

> [!info] 🌐 Consecuencias teóricas
>
> 1. **Teoremas de valor medio:** exigen derivabilidad en el intervalo.
> 2. **Optimización:** los extremos ocurren donde $f'(x) = 0$ **o donde $f'(x)$ no existe**.
> 3. **Aproximaciones lineales:** solo son posibles en puntos derivables.
> 4. **Ecuaciones diferenciales:** requieren funciones derivables.
>
> **Usos prácticos:** identificar puntos críticos en el análisis de funciones, verificar si un modelo físico es "suave", decidir dónde buscar extremos y saber dónde aplicar métodos lineales.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Derivabilidad_y_Continuidad_03.svg]]
>
> **Se lee así:** es un esquema de recuadros redondeados con un bloque central del que salen cinco ramas: el teorema principal con su demostración y la advertencia de que no hay recíproco, la clasificación de puntos, los ejemplos clave, los métodos de verificación y las aplicaciones. Cada rama se abre en hojas concretas.
>
> **Por qué importa:** reúne en una sola vista la teoría, los casos y los usos, así sabes qué revisar antes de responder. Te sirve tanto para un ejercicio de análisis de funciones como para justificar por qué una aproximación lineal es válida en un punto.
>
> **Ejemplo:** para justificar la aproximación lineal de $f(x) = \sqrt{x}$ en $x = 4$, tomas la hoja de aplicaciones: la aproximación solo es válida donde la función es derivable.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Demuestra que $f(x) = x^3 - 2x + 1$ es continua y derivable en $x = 1$, y calcula $f'(1)$.
>
> > [!success]- ✅ Solución
> >
> > Continuidad: $\lim_{x \to 1} (x^3 - 2x + 1) = 1 - 2 + 1 = 0 = f(1)$.
> >
> > Derivabilidad: $f'(1) = \lim_{h \to 0} \frac{(1+h)^3 - 2(1+h) + 1}{h} = \lim_{h \to 0} \frac{h + 3h^2 + h^3}{h} = 1$.
> >
> > El límite existe y es finito, así que $f$ es derivable en $1$ con $f'(1) = 1$; por el teorema fundamental, la continuidad ya estaba garantizada.

> [!example] 📋 Planteamiento
>
> Prueba que $f(x) = |x - 2|$ es continua pero no derivable en $x = 2$.
>
> > [!success]- ✅ Solución
> >
> > Continuidad: $f(2) = 0$ y $\lim_{x \to 2} |x - 2| = 0$, así que $\lim_{x \to 2} f(x) = f(2)$.
> >
> > Derivabilidad: $f'(2) = \lim_{h \to 0} \frac{|h|}{h}$; por la derecha vale $1$ y por la izquierda $-1$.
> >
> > Como los laterales difieren, el límite no existe: es continua pero no derivable (tipo B, esquina).

> [!example] 📋 Planteamiento
>
> Clasifica el punto $x = 0$ de $f(x) = \begin{cases} x+1 & \text{si } x < 0 \\ x-1 & \text{si } x \geq 0 \end{cases}$ y justifica por qué no es derivable.
>
> > [!success]- ✅ Solución
> >
> > $f(0) = -1$; $\lim_{x \to 0^-} f(x) = 1$ y $\lim_{x \to 0^+} f(x) = -1$. Los laterales no coinciden, así que no es continua.
> >
> > Por contraposición del teorema (derivable ⟹ continua), al no ser continua tampoco es derivable: es un punto de tipo C.

> [!example] 📋 Planteamiento
>
> Determina si $f(x) = \sqrt[3]{x}$ es derivable en $x = 0$.
>
> > [!success]- ✅ Solución
> >
> > Continuidad: $\lim_{x \to 0} \sqrt[3]{x} = 0 = f(0)$ ✔
> >
> > Derivada: $f'(0) = \lim_{h \to 0} \frac{\sqrt[3]{h}}{h} = \lim_{h \to 0} \frac{1}{h^{2/3}} = +\infty$.
> >
> > El límite no es finito, así que no es derivable: hay tangente vertical. Es continua (tipo B con derivada infinita).

> [!example] 📋 Planteamiento
>
> Estudia la derivabilidad de $f(x) = \begin{cases} x^2 & \text{si } x \leq 1 \\ 2x - 1 & \text{si } x > 1 \end{cases}$ en $x = 1$ usando derivadas laterales.
>
> > [!success]- ✅ Solución
> >
> > Continuidad: $f(1) = 1$, $\lim_{x \to 1^-} f = 1$ y $\lim_{x \to 1^+} f = 1$: es continua.
> >
> > Laterales: $f'_-(1) = \lim_{h \to 0^-} \frac{(1+h)^2 - 1}{h} = 2$ y $f'_+(1) = \lim_{h \to 0^+} \frac{2(1+h) - 2}{h} = 2$.
> >
> > Al ser iguales y finitas, $f'(1) = 2$: es derivable en el punto de unión.

> [!example] 📋 Planteamiento
>
> Aplica el método VERIFICA a $f(x) = x|x|$ en $x = 0$ y concluye si es derivable.
>
> > [!success]- ✅ Solución
> >
> > **V:** $f(x) = \begin{cases} x^2 & x \geq 0 \\ -x^2 & x < 0 \end{cases}$ y $\lim_{x \to 0} f = 0 = f(0)$: continua.
> >
> > **E/R:** parece suave, pero hay cambio de expresión en $0$: verificar.
> >
> > **I:** $f'_+(0) = \lim_{h \to 0^+} \frac{h^2}{h} = 0$ y $f'_-(0) = \lim_{h \to 0^-} \frac{-h^2}{h} = 0$.
> >
> > **F/I:** iguales y finitas, derivable con $f'(0) = 0$: tangente horizontal en el origen.
> >
> > **C/A:** multiplicar $|x|$ por $x$ elimina la esquina; contrasta con $|x|$, que sí la tiene.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo las tres condiciones de continuidad y la definición de derivabilidad en un punto.
> - [ ] Enuncio el teorema "derivable implica continua" y distingo su recíproco falso.
> - [ ] Clasifico un punto como tipo A, B, C o D según continuidad y derivabilidad.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Demuestro con el cociente incremental que una función es derivable en un punto dado.
> - [ ] Calculo derivadas laterales en los puntos de una función por partes y decido derivabilidad.
> - [ ] Presento $|x|$ como contraejemplo del recíproco con todos los pasos verificados.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro el teorema de derivabilidad implícita a continuidad y explico por qué la flecha no se invierte.
> - [ ] Aplico el método VERIFICA de principio a fin en una función poco habitual.
> - [ ] Identifico en un problema de optimización tanto los puntos donde $f' = 0$ como los donde $f'$ no existe.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2: continuidad y derivabilidad.
> - R. Larson, *Cálculo* (Cengage), cap. 2: la derivada como condición de continuidad.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 5: relaciones entre continuidad y diferenciabilidad.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la definición de derivada que da sentido al teorema.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — esquinas y tangentes en la gráfica.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — el concepto de continuidad en profundidad.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la relación correcta entre derivabilidad y continuidad?::Derivable implica continua; el recíproco es falso: $|x|$ es continua en $0$ pero no derivable.
> - ¿Qué tres condiciones definan la continuidad en $a$?::$f(a)$ existe, $\lim_{x \to a} f(x)$ existe y $\lim_{x \to a} f(x) = f(a)$.
> - ¿Cuándo existe $f'(a)$ en una función por partes?::Cuando las derivadas laterales $f'_+(a)$ y $f'_-(a)$ existen, son finitas e iguales.
> - ¿Qué tipos de punto no son derivables?::El tipo B (esquina o pico, continua), el C (salto) y el D (discontinuidad infinita); solo el tipo A es suave.
> - ¿Por qué la tangente vertical implica no derivabilidad?::Porque la derivada debe ser finita: si el límite del cociente es infinito, la derivada no existe.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — el concepto de continuidad del que partimos.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la definición formal de derivada.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — esquinas, tangentes y su lectura visual.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — el álgebra de derivadas que evita volver a la definición.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — derivabilidad de las composiciones.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — clasificación de puntos en el análisis completo.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — dónde buscar extremos: $f' = 0$ o $f'$ inexistente.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — tasas relacionadas con funciones derivables.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los cuatro ejemplos clasificados (tipos A, B, C y tangente vertical) hasta que el veredicto salga solo.
> - Después aplica las derivadas laterales a funciones por partes: es el formato de examen más común de esta nota.
> - Con los criterios de la sección "Condiciones suficientes" puedes saltar a [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|Reglas Fundamentales de Derivación]] sin miedo a justificar cada paso.
> - Recuerda siempre: en optimización, los candidatos a extremo son los puntos con $f'(x) = 0$ **y** los puntos donde $f'$ no existe.

---

**Tags:** #MATG1045 #unidad4 #derivabilidad #continuidad #teorema-implicacion #contraejemplos #derivadas-laterales #clasificacion-puntos #mnemotecnia

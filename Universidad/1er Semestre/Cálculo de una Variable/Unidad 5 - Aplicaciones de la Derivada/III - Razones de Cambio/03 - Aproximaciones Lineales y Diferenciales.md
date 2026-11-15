---
dg-publish: true
tags: [MATG1045, unidad5, aproximaciones-lineales, diferenciales, linealizacion, propagacion-errores, mediciones, derivada]
---

# 📏 Aproximaciones Lineales y Diferenciales

## 🎯 Introducción

> [!info] 💡 Qué permite esta nota
>
> Las **aproximaciones lineales** permiten *estimar* valores de funciones complicadas usando la **recta tangente** como aproximación local. En vez de calcular $f(3.1)$ con una fórmula incómoda, te apoyas en la recta que ya conoces en $x = 3$ y lees el valor casi exacto.
>
> **Por qué importa:** es la base de la **propagación de errores** en el laboratorio y del cálculo mental rápido: cuando el cambio es pequeño, la derivada basta para predecirlo.
>
> **Ejemplo:** para $f(x) = x^2$ en $x = 3$, el diferencial da $dy = 6 \cdot 0.1 = 0.6$, mientras que el valor real es $\Delta y = 9.61 - 9 = 0.61$: un error de apenas $0.01$.

> [!warning] ⚠️ Las dos advertencias que debes respetar
>
> 1. **La aproximación es local:** solo es precisa para valores **cercanos** al punto de tangencia. Lejos de $a$, el error se dispara.
> 2. **El error es de segundo orden:** la diferencia entre $\Delta y$ y $dy$ es proporcional a $dx^2$. Al duplicar $dx$, el error se cuadruplica; por eso el método falla lejos del punto.
>
> **Por qué importa:** entender esto evita el error clásico de usar la aproximación en un punto lejano y presentar un número falsamente preciso.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Diferencial de una función
>
> Para una función $f(x)$ derivable en $x = a$, el **diferencial** se define como
>
> $$dy = f'(a)\,dx,$$
>
> donde $dx$ es el incremento (pequeño) en la variable independiente, $dy$ es el **cambio aproximado** en la dependiente y $f'(a)$ es la pendiente de la tangente en ese punto.
>
> Sobre la recta tangente, el cambio $dy$ es **exacto**; sobre la curva, el cambio real $\Delta y = f(a+dx) - f(a)$ difiere en una cantidad de segundo orden.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Aproximaciones_Lineales_y_Diferenciales_03.svg]]
>
> **Se lee así:** el diagrama parte del punto de tangencia $(a, f(a))$ y toma $dx$ como un incremento pequeño en $x$; de ahí sale la fórmula $dy = f'(a)dx$, que representa el cambio aproximado en $y$. La rama final contrasta los dos mundos: sobre la recta tangente el cambio es exacto, mientras que sobre la curva el cambio real es $\Delta y = f(a+dx) - f(a)$, y la diferencia entre ambos es proporcional a $dx^2$.
>
> **Por qué importa:** el diagrama justifica por qué la aproximación funciona: la curva y su tangente se separan muy despacio, a velocidad de $dx^2$. Esa es la razón matemática de que $dy$ sea una buena aproximación de $\Delta y$ cuando $dx$ es pequeño.
>
> **Ejemplo:** para $f(x) = x^2$ en $a = 3$: $f'(3) = 6$, así que $dy = 6 \cdot 0.1 = 0.6$; el valor real es $\Delta y = 9.61 - 9 = 0.61$ y la diferencia es $0.01 = dx^2$, exactamente lo que predice el diagrama.

> [!note] 📋 Definición — Aproximación lineal
>
> Para aproximar $f(a + h)$ con $h$ pequeño se usa la ecuación de la **recta tangente** en $(a, f(a))$:
>
> $$f(a + h) \approx f(a) + f'(a)\cdot h.$$
>
> La diferencia $f(a+h) - \big[f(a) + f'(a)h\big]$ se llama **error de la aproximación** y tiende a cero cuando $h \to 0$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Aproximaciones_Lineales_y_Diferenciales_01.svg]]
>
> **Se lee así:** es una cadena corta de cuatro rectángulos con flechas hacia abajo: se parte de la función original, se marca el punto donde se va a trabajar, se traza la recta que toca la curva en ese punto y se llega a la casilla de aproximación local. Cada flecha es un paso, no una decisión.
>
> **Por qué importa:** la aproximación no se aplica a la función completa sino a un entorno del punto de tangencia; por eso el diagrama pasa siempre por la recta antes de llegar al resultado. Te evita usar $f(a+h) \approx f(a) + f'(a)h$ lejos de $a$, donde el error se dispara.
>
> **Ejemplo:** para $f(x) = x^2$ en $a = 3$ con $h = 0.1$, el recorrido da $f(3.1) \approx 9 + 6 \cdot 0.1 = 9.6$, frente al valor exacto $9.61$.

---

## 🧮 Cómo se aplica en la práctica

> [!tip] 🔧 Procedimiento en cuatro pasos
>
> 1. **Identifica** el punto de referencia $a$ (el valor cercano al que quieres llegar).
> 2. **Calcula** $f(a)$ y $f'(a)$.
> 3. **Determina** el incremento $h$ (pequeño).
> 4. **Sustituye:** $f(a+h) \approx f(a) + f'(a)h$, y compara con el valor exacto si puedes, para cuantificar el error.
>
> **Por qué importa:** el error más común no esalgebraico sino de **punto de referencia**: usar $a$ lejos del valor buscado arruina la aproximación aunque la fórmula esté bien.

> [!example] 🌟 Ejemplo numérico: $f(x) = x^2$ en $x = 3$
>
> - $f'(x) = 2x$, entonces $f'(3) = 6$.
> - Diferencial: $dy = 6\,dx$.
> - Con $dx = 0.1$: $dy = 0.6$.
> - **Verificación:** valor real $f(3.1) = 9.61$ y $f(3) = 9$, luego $\Delta y = 0.61$.
> - Aproximación: $dy = 0.6$ — diferencia de solo $0.01$.
>
> **Por qué importa:** el ejemplo muestra las dos magnitudes lado a lado: $dy$ (aproximado) y $\Delta y$ (exacto). Esa diferencia es el **error de linealización**.

> [!warning] ⚠️ Limitaciones de la aproximación
>
> - Solo es precisa para valores **cercanos** al punto de tangencia.
> - El error crece conforme nos alejamos de $a$ (es proporcional a $dx^2$).
> - En funciones muy curvadas la aproximación puede ser pobre aunque $dx$ sea pequeño.
> - Si $f'(a) = 0$, la aproximación es de segundo orden y el primer término no aporta información.
>
> **Por qué importa:** saber *cuándo no applies* la linealización es tan importante como saber aplicarla.

> [!tip] 🎓 Mnemotecnia "DALE"
>
> - **D**iferencial: $dy = f'(x)\,dx$.
> - **A**proximación: $f(a+h) \approx f(a) + f'(a)h$.
> - **L**ineal: usamos la recta tangente.
> - **E**rror: $\Delta f \approx |f'(x)|\,\Delta x$.
>
> **Por qué importa:** "DALE" recorre el flujo mental completo: del diferencial a la aproximación, de la aproximación a la linealización y de ahí al error. Es la secuencia que se repite en cualquier problema de esta nota.

---

## 📊 Propagación de errores

> [!info] 🔬 Cómo se propaga la incertidumbre
>
> Cuando medimos una magnitud física siempre hay **incertidumbre**. Si $x$ tiene un error $\Delta x$, el error en el valor calculado de $f(x)$ es aproximadamente
>
> $$\Delta f \approx |f'(x)| \cdot \Delta x.$$
>
> El valor absoluto es indispensable: los errores se acumulan en la dirección de la magnitud, no en la del signo de la derivada.
>
> > [!note] 📋 Fórmulas de propagación más usadas
> >
> > | Función | $f(x)$ | Error propagado $\Delta f$ |
> > |---|---|---|
> > | Potencia | $x^n$ | $\lvert n x^{n-1}\rvert \Delta x$ |
> > | Exponencial | $e^x$ | $e^x \Delta x$ |
> > | Logaritmo | $\ln x$ | $\frac{\Delta x}{\lvert x\rvert}$ |
> > | Seno | $\sin x$ | $\lvert\cos x\rvert \Delta x$ |
> > | Coseno | $\cos x$ | $\lvert\sin x\rvert \Delta x$ |
> >
> > **Por qué importa:** la tabla convierte el procedimiento general en fórmulas listos para usar: basta derivar y sustituir en la fila correspondiente.
>
> > **Ejemplo:** para $V = \frac{4}{3}\pi r^3$, $\Delta V \approx |4\pi r^2| \Delta r = 4\pi r^2 \Delta r$.

> [!info] 🖼️ De la medida al resultado con margen
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Aproximaciones_Lineales_y_Diferenciales_02.svg]]
>
> **Se lee así:** es una cadena de cuatro rectángulos que sigue el recorrido de una medición real: la primera casilla es la medida con su incertidumbre, la segunda indica aplicar el diferencial, la tercera pide derivar la magnitud que se quiere propagar y la cuarta cierra con el resultado numérico acompañado de su margen de error.
>
> **Por qué importa:** la incertidumbre de la medida entra una sola vez, al principio, y el error final sale amplificado por la derivada. Esto te sirve para los informes de laboratorio: da una cota realista del volumen y evita presentar un número sin margen.
>
> **Ejemplo:** con $r = 5.0 \pm 0.1$ cm en una esfera, la cadena da $V'(r) = 4\pi r^2$, luego $\Delta V \approx 4\pi(25)(0.1) = 10\pi$ y termina en $V = 523.6 \pm 31.4\ \text{cm}^3$.

---

## 🔬 Aplicaciones en mediciones

> [!example] 🧪 Volumen de una esfera
>
> **Enunciado:** una esfera tiene radio $r = 5.0 \pm 0.1$ cm. ¿Cuál es el error en el volumen?
>
> - $V(r) = \frac{4}{3}\pi r^3$.
> - $V'(r) = 4\pi r^2$.
> - $\Delta V \approx V'(5)\cdot\Delta r = 4\pi(25)(0.1) = 10\pi \approx 31.4\ \text{cm}^3$.
>
> **Respuesta:** $V = 523.6 \pm 31.4\ \text{cm}^3$.
>
> **Por qué importa:** fíjate en que el error relativo es mayor que el de la medida: $\frac{31.4}{523.6} \approx 6\%$, tres veces el $2\%$ de la incertidumbre en el radio. El error **se amplifica** con la potencia.

> [!example] 📏 Cifras significativas
>
> **Enunciado:** mide un círculo con radio $r = 10.0 \pm 0.1$ cm y calcula el área.
>
> - $A = \pi r^2$, $A'(r) = 2\pi r$.
> - $\Delta A \approx 2\pi(10)(0.1) = 2\pi \approx 6.3\ \text{cm}^2$.
> - Área: $\pi(10)^2 = 314.2\ \text{cm}^2$.
>
> **Respuesta:** $A = 314.2 \pm 6.3\ \text{cm}^2$, es decir, $314 \pm 6\ \text{cm}^2$ respetando las cifras significativas.
>
> **Por qué importa:** el margen de error **acorta** la cifra final: no tiene sentido reportar $314.159 \pm 6.3\ \text{cm}^2$.

> [!example] ⚗️ Estimación de una raíz
>
> **Enunciado:** estima $\sqrt{4.1}$ con la aproximación lineal.
>
> - Punto de referencia: $a = 4$, con $f(x) = \sqrt{x}$, $f(4) = 2$.
> - $f'(x) = \frac{1}{2\sqrt{x}}$, luego $f'(4) = \frac{1}{4}$.
> - Con $h = 0.1$: $\sqrt{4.1} \approx 2 + \frac{1}{4}(0.1) = 2.025$.
>
> **Respuesta:** $\sqrt{4.1} \approx 2.025$ (valor exacto: $2.024845\ldots$).
>
> **Por qué importa:** sin calculadora, este tipo de estimación es la forma de "sentir" un valor: el error es de apenas $0.0002$.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Usa la aproximación lineal para estimar $f(2.1)$ si $f(x) = x^3$.
>
> > [!success]- ✅ Solución
> >
> > Punto de referencia $a = 2$: $f(2) = 8$ y $f'(x) = 3x^2$, luego $f'(2) = 12$.
> >
> > Con $h = 0.1$:
> >
> > $$f(2.1) \approx 8 + 12 \cdot 0.1 = 9.2.$$
> >
> > Valor exacto: $2.1^3 = 9.261$. **Respuesta:** la aproximación da $9.2$ con un error de $0.061$.

> [!example] 📋 Planteamiento
>
> Calcula el diferencial de $f(x) = x^2 + 3x$ en $x = 1$ para $dx = 0.02$.
>
> > [!success]- ✅ Solución
> >
> > $f'(x) = 2x + 3$, así que $f'(1) = 5$.
> >
> > $$dy = f'(1)\,dx = 5 \cdot 0.02 = 0.1.$$
> >
> > **Respuesta:** $dy = 0.1$; el valor exacto es $f(1.02) = 1.0404 + 3.06 = 4.1004$, luego $\Delta y = 4.1004 - 4 = 0.1004$, con error $0.0004$.

> [!example] 📋 Planteamiento
>
> Una esfera tiene radio $r = 3.00 \pm 0.05$ cm. Propaga el error al volumen.
>
> > [!success]- ✅ Solución
> >
> > $V = \frac{4}{3}\pi r^3$, $V'(r) = 4\pi r^2$.
> >
> > $$\Delta V \approx 4\pi(3)^2 \cdot 0.05 = 36\pi \cdot 0.05 = 1.8\pi \approx 5.65\ \text{cm}^3.$$
> >
> > **Respuesta:** $V = 113.1 \pm 5.7\ \text{cm}^3$; el error relativo ($\approx 5\%$) triplica el de la medida ($1{,}67\%$).

> [!example] 📋 Planteamiento
>
> Estima $\sqrt{9.6}$ usando la aproximación lineal.
>
> > [!success]- ✅ Solución
> >
> > $a = 9$, $f(x) = \sqrt{x}$: $f(9) = 3$ y $f'(9) = \frac{1}{2 \cdot 3} = \frac{1}{6}$.
> >
> > Con $h = 0.6$:
> >
> > $$\sqrt{9.6} \approx 3 + \frac{1}{6}(0.6) = 3.1.$$
> >
> > Valor exacto: $3.098386\ldots$. **Respuesta:** la aproximación da $3.1$ con error $\approx 0.0016$.

> [!example] 📋 Planteamiento
>
> Estima el valor de $\tan(0.52)$ con la aproximación lineal en $a = 0.5$ rad.
>
> > [!success]- ✅ Solución
> >
> > $f(x) = \tan x$, $a = 0.5$: $f(0.5) \approx 0.546302$ y $f'(x) = \sec^2 x = 1 + \tan^2 x$, luego $f'(0.5) = 1 + 0.298446 \approx 1.298446$.
> >
> > Con $h = 0.02$:
> >
> > $$\tan(0.52) \approx 0.546302 + 1.298446 \cdot 0.02 \approx 0.572271.$$
> >
> > **Respuesta:** $\tan(0.52) \approx 0.5723$ (valor exacto $\approx 0.572561$).

> [!example] 📋 Planteamiento
>
> Un terreno rectangular mide $20.0 \pm 0.1$ m de largo y $10.0 \pm 0.1$ m de ancho. ¿Cuál es el error en su área?
>
> > [!success]- ✅ Solución
> >
> > $A = L \cdot W$, con $L$ el largo y $W$ el ancho: $\frac{\partial A}{\partial L} = W = 10.0$ y $\frac{\partial A}{\partial W} = L = 20.0$.
> >
> > $$\Delta A \approx \left|\frac{\partial A}{\partial L}\right|\Delta L + \left|\frac{\partial A}{\partial W}\right|\Delta W = 10(0.1) + 20(0.1) = 3.0\ \text{m}^2.$$
> >
> > **Respuesta:** el área es $200.0 \pm 3.0\ \text{m}^2$; los errores de las dos dimensiones se **suman**, no se cancelan.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo el diferencial $dy = f'(a)\,dx$ e interpreto cada símbolo.
> - [ ] Aplico $f(a+h) \approx f(a) + f'(a)h$ para estimar un valor cercano.
> - [ ] Identifico el punto de referencia $a$ y el incremento $h$ en un problema dado.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Cuantifico el error de la linealización comparando el valor exacto con el aproximado.
> - [ ] Propago incertidumbres con $\Delta f \approx |f'(x)|\Delta x$ y justifico el valor absoluto.
> - [ ] Calculo el error de un volumen, un área o un perímetro a partir de las incertidumbres de las medidas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Explico por qué el error de la aproximación es de segundo orden y qué implica al alejarme de $a$.
> - [ ] Propago errores en problemas con dos variables medidas, sumando las contribuciones parciales.
> - [ ] Evalúo cuándo la linealización deja de ser útil y propongo una alternativa (series de Taylor o cálculo directo).

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 3 y 4: aproximaciones lineales y diferenciales.
> - R. Larson, *Cálculo* (Cengage), cap. 3: linealización y propagación de errores.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 3: el diferencial como cambio infinitesimal.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la derivada que define el diferencial.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — la recta tangente que da nombre a la aproximación.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/01 - Tasas de Cambio|01 - Tasas de Cambio]] — la tasa instantánea que aquí se convierte en cambio estimado.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es el diferencial de $f$ en $a$?::$dy = f'(a)\,dx$: el cambio aproximado en $y$ que produce el incremento $dx$ siguiendo la recta tangente en $(a, f(a))$.
> - ¿Cuál es la fórmula de la aproximación lineal?::$f(a+h) \approx f(a) + f'(a)\,h$, la ecuación de la recta tangente en el punto de referencia.
> - ¿Cómo se propaga un error?::$\Delta f \approx |f'(x)|\,\Delta x$: el error se amplifica por el valor absoluto de la derivada.
> - ¿Por qué la aproximación lineal funciona?::Porque la curva se separa de su tangente a velocidad de $dx^2$: el error es de segundo orden y desaparece cuando $dx \to 0$.
> - ¿Qué pasa si uso la aproximación lejos del punto de referencia?::El error crece como $dx^2$ y la estimación deja de ser confiable: hay que elegir un $a$ cercano al valor buscado.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — de dónde sale $f'(a)$ que multiplica a $dx$.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/02 - Interpretación Geométrica de la Derivada|02 - Interpretación Geométrica de la Derivada]] — la geometría de la tangente que sostiene la linealización.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/01 - Tasas de Cambio|01 - Tasas de Cambio]] — la tasa instantánea como cambio por unidad.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — predecir cómo cambian varias magnitudes a la vez.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — el volumen que aquí se estima con incertidumbres.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el proceso inverso: acumular en vez de estimar localmente.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2 (aproximación y diferencial) hasta que el paso "elegir $a$ y $h$" sea automático.
> - Después salta a los ejercicios 3 y 6, donde entra la propagación de errores: ahí está la aplicación de laboratorio.
> - Cuando domines ambos, resuelve el ejercicio 5 (ángulo) para ver la aproximación con trigonometría.
> - En cada ejercicio, compara siempre tu valor aproximado con el exacto y anota el error: así se ve por qué funciona el método.

---

**Tags:** #MATG1045 #unidad5 #aproximaciones-lineales #diferenciales #linealizacion #propagacion-errores #mediciones #derivada

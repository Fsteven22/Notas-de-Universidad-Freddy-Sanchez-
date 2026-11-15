---
dg-publish: true
tags: [MATG1045, unidad2, limites-laterales, calculo, limites, discontinuidades, funciones-por-partes, izquierda-derecha, existencia-limites, continuidad, matematicas, analisis]
---

# ↔ Límites por la Izquierda y Derecha

## 🎯 Introducción

> [!tip] 🎯 Concepto Central
>
> Los **límites laterales** nos permiten analizar el comportamiento de una función acercándonos a un punto desde **una sola dirección**. Son como examinar una intersección desde cada calle por separado antes de decidir si es seguro cruzar.

---

## 📋 Definiciones Formales

> [!info] 👈 Definición de límite por la izquierda
>
> Se dice que $\lim_{x \to a^-} f(x) = L_1$ cuando, al acercar $x$ a $a$ **solo con valores menores que $a$**, los valores de $f(x)$ se acercan a $L_1$. En otras palabras: $x < a$ y $x \to a$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Límites_Laterales_03.svg]]
>
> **Se lee así:** El diagrama arranca en el rectángulo del punto $x = a$ y baja por una cadena de tres rectángulos: primero recoge los valores menores que $a$, después describe cómo $x$ se acerca por la izquierda y después cómo $f(x)$ se estabiliza. Entra a un rombo que pregunta si esos valores se estabilizan; la rama "Sí" termina en el recuadro del límite izquierdo que vale $L_1$ y en el recuadro de la notación, y la rama "No" cierra en un recuadro rojo donde el límite izquierdo no existe.
>
> **Por qué importa:** El rombo obliga a comprobar la estabilización antes de afirmar que el límite existe. Muchos problemas se resuelven bien por un lado y se cierran mal porque se dio por sentado que la curva se acerca a un valor fijo.
>
> **Ejemplo:** En $f(x) = \sqrt{x}$ con $x \to 4^-$ sigues la rama "Sí" y obtienes $L_1 = 2$, porque la raíz se acerca a $2$ por valores menores de $4$.

> [!info] 👉 Definición de límite por la derecha
>
> Se dice que $\lim_{x \to a^+} f(x) = L_2$ cuando, al acercar $x$ a $a$ **solo con valores mayores que $a$**, los valores de $f(x)$ se acercan a $L_2$. En otras palabras: $x > a$ y $x \to a$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Límites_Laterales_04.svg]]
>
> **Se lee así:** Es el espejo del diagrama anterior: desde el rectángulo del punto $x = a$ se recogen ahora los valores **mayores** que $a$, luego cómo $x$ se acerca por la derecha y luego cómo $f(x)$ se estabiliza. El rombo vuelve a preguntar si los valores se estabilizan, y de ahí salen el recuadro del límite derecho $L_2$ con su notación o el recuadro rojo de no existencia.
>
> **Por qué importa:** Este es el segundo test que hay que pasar. Como el diagrama es simétrico al del lado izquierdo, te recuerda que el procedimiento es idéntico y que lo único que cambia es el sentido de aproximación.
>
> **Ejemplo:** En $f(x) = \sqrt{x}$ con $x \to 4^+$ obtienes $L_2 = 2$; como $L_1 = L_2$, el límite completo vale $2$.

> [!warning] ⚖️ Definición de la existencia del límite
>
> El límite $\lim_{x \to a} f(x)$ existe **si y solo si**:
>
> 1. **Ambos límites laterales existen**, y
> 2. **son iguales**: $\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)$.
>
> Cuando esto ocurre: $$\lim_{x \to a} f(x) = \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Límites_Laterales_01.svg]]
>
> **Se lee así:** Se ve un punto central $x = a$ del que se separan dos ramas: una de aproximación por la izquierda y otra por la derecha, cada una con su propio rectángulo de límite lateral, $L_1$ y $L_2$. Las dos vuelven a juntarse en un rombo que compara si $L_1$ y $L_2$ coinciden, y de ahí salen las dos respuestas posibles: el límite existe con valor común o **no existe**.
>
> **Por qué importa:** Este es el teorema fundamental de los límites laterales: el límite existe si y solo si los dos lados coinciden. Tenerlo en la cabeza te impide concluir existencia mirando un solo lado, que es el error más repetido en los exámenes.
>
> **Ejemplo:** Para la función por partes $k(x)$ definida más abajo, en $x = 1$ el límite izquierdo es $1$ y el derecho es $3$, así que el límite no existe aunque la función sí esté definida en ese punto.

---

## 🧮 Técnicas de Cálculo

> [!example] 🔢 Método de aproximación numérica
>
> Para calcular $\lim_{x \to a^-} f(x)$ se tabulan valores que se acercan a $a$ desde cada lado. La idea es observar hacia dónde se encamina la columna de $f(x)$, no calcular un valor exacto a mano.
>
> **Tabla desde la izquierda:**
>
> |$x$ (valores < a)|$f(x)$|
> |---|---|
> |$a - 0.1$|$f(a-0.1)$|
> |$a - 0.01$|$f(a-0.01)$|
> |$a - 0.001$|$f(a-0.001)$|
>
> **Tabla desde la derecha:**
>
> |$x$ (valores > a)|$f(x)$|
> |---|---|
> |$a + 0.1$|$f(a+0.1)$|
> |$a + 0.01$|$f(a+0.01)$|
> |$a + 0.001$|$f(a+0.001)$|
>
> **Por qué importa:** La tabla sugiere la tendencia, pero no la demuestra: sirve para decidir qué hipótesis verificar con álgebra después.

---

## 🎭 Casos Fundamentales

### Caso 1: Límites laterales iguales ✅

> [!example] 🌊 Función continua
>
> **Ejemplo:** $f(x) = x^2$ en $x = 2$.
>
> - $\lim_{x \to 2^-} x^2 = 4$
> - $\lim_{x \to 2^+} x^2 = 4$
> - Como son iguales: $\lim_{x \to 2} x^2 = 4$ ✨
>
> **Verificación numérica:**
>
> |Desde la izquierda|$f(x) = x^2$|Desde la derecha|$f(x) = x^2$|
> |---|---|---|---|
> |$x = 1.9$|$3.61$|$x = 2.1$|$4.41$|
> |$x = 1.99$|$3.9601$|$x = 2.01$|$4.0401$|
> |$x = 1.999$|$3.996001$|$x = 2.001$|$4.004001$|
>
> **Resultado:** ambos lados se acercan a $4$, así que el límite existe y vale $4$.

### Caso 2: Discontinuidad removible 🕳️

> [!example] ⚪ Función con hueco
>
> **Ejemplo:** $g(x) = \frac{x^2 - 4}{x - 2}$ en $x = 2$.
>
> **Análisis algebraico:** $g(x) = \frac{x^2 - 4}{x - 2} = \frac{(x-2)(x+2)}{x - 2} = x + 2$ (para $x \neq 2$).
>
> - $\lim_{x \to 2^-} g(x) = \lim_{x \to 2^-} (x + 2) = 4$
> - $\lim_{x \to 2^+} g(x) = \lim_{x \to 2^+} (x + 2) = 4$
> - **Resultado:** $\lim_{x \to 2} g(x) = 4$ ✅
>
> **Nota:** aunque $g(2)$ no existe, el límite sí existe: la discontinuidad es removible.

### Caso 3: Discontinuidad de salto 📈📉

> [!warning] ❌ Límites laterales diferentes
>
> **Ejemplo de salto real:** $k(x) = \begin{cases} x & \text{si } x < 1 \\ x + 2 & \text{si } x \geq 1 \end{cases}$
>
> **En $x = 1$:**
>
> - $\lim_{x \to 1^-} k(x) = 1$
> - $\lim_{x \to 1^+} k(x) = 3$
> - Como $1 \neq 3$: $\lim_{x \to 1} k(x)$ **no existe** ❌
>
> **Contraejemplo útil:** la función escalón $h(x) = \begin{cases} x + 1 & \text{si } x < 3 \\ 2x - 2 & \text{si } x \geq 3 \end{cases}$ sí tiene límite en $x = 3$, porque ambos lados dan $4$. Que haya dos fórmulas distintas no garantiza que haya salto: hay que calcular.
>
> **Por qué importa:** el caso de salto es el único donde la discontinuidad se detecta comparando números; los otros dos se resuelven estudiando el dominio y la factorización.

### Caso 4: Límites infinitos ♾️

> [!warning] ♾️ Asíntotas verticales
>
> **Ejemplo:** $f(x) = \frac{1}{x - 2}$ en $x = 2$.
>
> **Análisis por signos:**
>
> - Para $x < 2$: $(x - 2) < 0$, entonces $f(x) < 0$
> - Para $x > 2$: $(x - 2) > 0$, entonces $f(x) > 0$
>
> - $\lim_{x \to 2^-} \frac{1}{x - 2} = -\infty$
> - $\lim_{x \to 2^+} \frac{1}{x - 2} = +\infty$
> - **Resultado:** $\lim_{x \to 2} \frac{1}{x - 2}$ **no existe**, aunque cada límite lateral sí esté definido como infinito.
>
> **Por qué importa:** aquí el problema no es de cálculo sino de lectura: los dos lados van a infinitos opuestos, así que la recta $x = 2$ es una asíntota vertical con comportamiento contrario en cada lado.

---

## 📊 Análisis Visual en Gráficas

> [!info] 👀 Identificación gráfica de límites laterales
>
> |Tipo visual|Límite izquierdo|Límite derecho|Límite total|
> |---|---|---|---|
> |🌊 Curva continua|✅ Existe|✅ Existe|✅ Existe|
> |🕳️ Hueco|✅ Existe|✅ Existe|✅ Existe|
> |📈📉 Salto|✅ Existe|✅ Existe|❌ No existe|
> |♾️ Asíntota vertical|♾️ Infinito|♾️ Infinito|Depende del caso|
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Límites_Laterales_02.svg]]
>
> **Se lee así:** El diagrama parte de una gráfica y la recorre en dos direcciones: siguiendo la curva desde la izquierda y desde la derecha, con un rectángulo en cada ruta que pregunta a qué altura apunta la curva. Esas dos alturas llegan a un rombo de comparación sobre si son la misma, y el veredicto final es que el límite existe o no existe.
>
> **Por qué importa:** Leer la altura de la curva es la forma más rápida de decidir en un examen, y el diagrama te entrena en mirar los dos lados antes de afirmar. Con una gráfica te ahorras toda la tabla de valores cuando lo que importa es solo la tendencia.
>
> **Ejemplo:** En la gráfica de $f(x) = 1/(x - 2)$, siguiendo la curva desde cada lado se llega a alturas opuestas, y por eso el límite en $x = 2$ no existe aunque ambos límites laterales sean infinitos.

---

## 🧩 Funciones Definidas por Partes

> [!example] 🎯 Estrategia para funciones por partes
>
> **Para evaluar límites laterales en $x = a$:**
>
> 1. **Identifica** qué fórmula usar para $x < a$ (límite izquierdo).
> 2. **Identifica** qué fórmula usar para $x > a$ (límite derecho).
> 3. **Calcula** cada límite lateral por separado.
> 4. **Compara** los resultados.
>
> **Por qué importa:** el orden importa: primero se elige la fórmula y después se sustituye. Elegir mal la rama es el error más caro de este tipo de ejercicios.

> [!example] 🔍 Ejemplo detallado
>
> $$f(x) = \begin{cases} x^2 & \text{si } x < 0 \\ 2 & \text{si } x = 0 \\ x + 1 & \text{si } x > 0 \end{cases}$$
>
> **Análisis en $x = 0$:**
>
> - **Límite izquierdo:** $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} x^2 = 0$
> - **Límite derecho:** $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (x + 1) = 1$
> - **Comparación:** $0 \neq 1$
> - **Conclusión:** $\lim_{x \to 0} f(x)$ no existe
>
> **Nota:** aunque $f(0) = 2$, esto no afecta la existencia del límite: el valor fijo no entra en el cálculo.

---

## ⚖️ Propiedades de Límites Laterales

> [!info] 📜 Teoremas importantes
>
> Si $\lim_{x \to a^-} f(x) = L_1$ y $\lim_{x \to a^+} f(x) = L_2$, las operaciones se comportan igual que en cualquier límite:
>
> - **Suma:** $\lim_{x \to a^{\pm}} [f(x) + g(x)] = \lim_{x \to a^{\pm}} f(x) + \lim_{x \to a^{\pm}} g(x)$
> - **Producto:** $\lim_{x \to a^{\pm}} [f(x) \cdot g(x)] = \lim_{x \to a^{\pm}} f(x) \cdot \lim_{x \to a^{\pm}} g(x)$
> - **Cociente:** $\lim_{x \to a^{\pm}} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a^{\pm}} f(x)}{\lim_{x \to a^{\pm}} g(x)}$, siempre que el denominador no sea cero.
>
> **Por qué importa:** todas las reglas exigen que los límites implicados existan y sean finitos. Aplicarlas cuando un lado no existe produce respuestas inventadas.

---

## 🌍 Aplicaciones Prácticas

> [!example] 🚗 Aplicación: velocidad instantánea
>
> Un auto se mueve según $s(t) = \begin{cases} 2t^2 & \text{si } 0 \leq t < 3 \\ 18 + 3(t-3) & \text{si } t \geq 3 \end{cases}$.
>
> **¿Cuál es la velocidad en $t = 3$?** La velocidad es $v(t) = s'(t)$:
>
> - **Antes de $t = 3$:** $v(t) = \frac{d}{dt}(2t^2) = 4t$, entonces $\lim_{t \to 3^-} v(t) = 4(3) = 12$ m/s.
> - **Después de $t = 3$:** $v(t) = \frac{d}{dt}[18 + 3(t-3)] = 3$, entonces $\lim_{t \to 3^+} v(t) = 3$ m/s.
>
> **Conclusión:** como $12 \neq 3$, hay un cambio abrupto de velocidad en $t = 3$.
>
> **Por qué importa:** es el mismo criterio de los límites laterales aplicado a la física: si los dos lados no coinciden, la magnitud física tiene un salto en ese instante.

---

## ⚠️ Errores Comunes

> [!warning] 🚨 Trampas frecuentes
>
> **Error 1: usar la función equivocada en los límites laterales.** En funciones por partes es fácil sustituir con la fórmula del lado contrario. **Solución:** verificar cuidadosamente qué expresión corresponde a cada lado antes de calcular.
>
> **Error 2: confundir límites laterales con el valor de la función.** $f(a)$ no determina los límites laterales: estos dependen del comportamiento **cerca de** $a$, no **en** $a$. **Solución:** estudiar el entorno del punto, no el punto.
>
> **Error 3: concluir existencia sin verificar ambos lados.** Calcular un solo límite lateral no basta. **Solución:** siempre verificar los dos lados antes de concluir, y compararlos explícitamente.
>
> **Por qué importa:** los tres errores son de planteamiento, no de aritmética; ninguno se detecta revisando cuentas, se detecta revisando el orden del procedimiento.

---

## 🧠 Mnemotecnia "LATERAL"

> [!tip] 🎓 Para recordar el proceso
>
> - **L**ocaliza el punto de interés $x = a$.
> - **A**naliza desde ambos lados por separado.
> - **T**abula valores acercándose desde cada lado.
> - **E**valúa hacia dónde tiende cada límite lateral.
> - **R**evisa si los límites laterales son iguales.
> - **A**firma la existencia del límite solo si coinciden.
> - **L**ee el resultado: existe o no existe.
>
> **Por qué importa:** la mnemotecnia ordena exactamente el algoritmo del teorema de existencia, así que sirve de checklist antes de dar un ejercicio por cerrado.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Para $f(x) = \begin{cases} x^2 & \text{si } x < 0 \\ 2 & \text{si } x = 0 \\ x + 1 & \text{si } x > 0 \end{cases}$, calcula $\lim_{x \to 0^-} f(x)$, $\lim_{x \to 0^+} f(x)$ y decide si existe $\lim_{x \to 0} f(x)$.
>
> > [!success]- ✅ Solución
> >
> > Para $x < 0$ rige $f(x) = x^2$, así que $\lim_{x \to 0^-} f(x) = 0^2 = 0$.
> >
> > Para $x > 0$ rige $f(x) = x + 1$, así que $\lim_{x \to 0^+} f(x) = 0 + 1 = 1$.
> >
> > Como $0 \neq 1$, por el teorema de existencia el límite no existe. El valor $f(0) = 2$ no interviene en la decisión.

> [!example] 📋 Planteamiento
>
> Sea $g(x) = \frac{x^2 - 4}{x - 2}$. Calcula $\lim_{x \to 2} g(x)$ y explica por qué la función no está definida en ese punto.
>
> > [!success]- ✅ Solución
> >
> > Sustituir da $\frac{4 - 4}{2 - 2} = \frac{0}{0}$, así que hay que simplificar: $g(x) = \frac{(x-2)(x+2)}{x-2} = x + 2$ para $x \neq 2$.
> >
> > Entonces $\lim_{x \to 2^-} g(x) = 4$ y $\lim_{x \to 2^+} g(x) = 4$. Al coincidir, $\lim_{x \to 2} g(x) = 4$.
> >
> > El denominador se anula en $x = 2$ y ahí no se puede dividir, por eso $g(2)$ no existe: es un hueco, una discontinuidad removible.

> [!example] 📋 Planteamiento
>
> Para $k(x) = \begin{cases} x & \text{si } x < 1 \\ x + 2 & \text{si } x \geq 1 \end{cases}$, calcula los límites laterales en $x = 1$ y clasifica la discontinuidad.
>
> > [!success]- ✅ Solución
> >
> > Por la izquierda rige $f(x) = x$, así que $\lim_{x \to 1^-} k(x) = 1$.
> >
> > Por la derecha rige $f(x) = x + 2$, así que $\lim_{x \to 1^+} k(x) = 3$.
> >
> > Como $1 \neq 3$, el límite no existe y la discontinuidad es de **salto**, con salto de magnitud $3 - 1 = 2$.

> [!example] 📋 Planteamiento
>
> Calcula $\lim_{x \to 2} \frac{1}{x - 2}$ por la izquierda y por la derecha, y di qué representa geométricamente.
>
> > [!success]- ✅ Solución
> >
> > Para $x < 2$ el denominador es negativo, así que $\lim_{x \to 2^-} \frac{1}{x - 2} = -\infty$.
> >
> > Para $x > 2$ el denominador es positivo, así que $\lim_{x \to 2^+} \frac{1}{x - 2} = +\infty$.
> >
> > Los dos laterales van a infinito, por lo que el límite no existe. Geométricamente, la recta $x = 2$ es una asíntota vertical porque la función crece sin cota al acercarse a ella.

> [!example] 📋 Planteamiento
>
> Un auto se mueve según $s(t) = \begin{cases} 2t^2 & \text{si } 0 \leq t < 3 \\ 18 + 3(t-3) & \text{si } t \geq 3 \end{cases}$. Usa límites laterales para decidir si la velocidad en $t = 3$ es un solo valor.
>
> > [!success]- ✅ Solución
> >
> > La velocidad es la derivada de la posición: para $t < 3$ tenemos $v(t) = 4t$, y para $t \geq 3$ tenemos $v(t) = 3$.
> >
> > Por la izquierda, $\lim_{t \to 3^-} v(t) = 4 \cdot 3 = 12$ m/s. Por la derecha, $\lim_{t \to 3^+} v(t) = 3$ m/s.
> >
> > Como $12 \neq 3$, la velocidad no tiene un valor único en $t = 3$: el movimiento presenta un salto de velocidad en ese instante.

> [!example] 📋 Planteamiento
>
> Lee de la gráfica los límites laterales en $x = 2$ de la función por partes $g(x) = \begin{cases} x + 1 & \text{si } x < 2 \\ 3 & \text{si } x = 2 \\ 2x - 1 & \text{si } x > 2 \end{cases}$ y concluye sobre la continuidad.
>
> > [!success]- ✅ Solución
> >
> > Por la izquierda la curva sigue $y = x + 1$, que se acerca a $3$; por la derecha sigue $y = 2x - 1$, que también se acerca a $3$.
> >
> > Los dos lados coinciden en $3$, así que $\lim_{x \to 2} g(x) = 3$.
> >
> > Además $g(2) = 3$, por lo que el límite coincide con el valor de la función y la función es continua en ese punto.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Explico con mis palabras qué significa $\lim_{x \to a^-} f(x) = L$ y qué significa $\lim_{x \to a^+} f(x) = L$.
> - [ ] Escribo la notación correcta del límite lateral izquierdo y del derecho sin confundir los signos.
> - [ ] Identifico en una gráfica hacia dónde apunta la curva por cada lado de un punto.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico el teorema de existencia y decido si un límite existe comparando sus dos laterales.
> - [ ] Resuelvo límites laterales de funciones definidas por partes eligiendo la fórmula correcta en cada lado.
> - [ ] Distinguo una discontinuidad removible de una de salto a partir de los valores laterales.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Determino cuándo un límite lateral es infinito y relaciono ese resultado con una asíntota vertical.
> - [ ] Explico por qué el valor de la función en el punto no decide la existencia del límite.
> - [ ] Aplico límites laterales a un problema de velocidad o de tasa de cambio y interpreto el resultado.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2: límites laterales y existencia del límite.
> - R. Larson, *Cálculo* (Cengage), cap. 1: límite por la izquierda y por la derecha.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 3: límites laterales y discontinuidades.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — de dónde sale la definición formal que aquí se aplica a cada lado.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — las reglas algebraicas que se usan lado por lado.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — el concepto que hace que coincidan límite y valor de la función.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué significa la notación $\lim_{x \to a^-} f(x) = L$?::Que al acercar $x$ a $a$ solo por valores menores que $a$, los valores de $f(x)$ se acercan a $L$.
> - ¿Cuál es la condición para que exista $\lim_{x \to a} f(x)$?::Que existan ambos límites laterales y que sean iguales: $\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)$.
> - En una función por partes, ¿qué fórmula se usa para el límite izquierdo?::La que rige para $x < a$; para el límite derecho se usa la de $x > a$.
> - Si $\lim_{x \to 1^-} k(x) = 1$ y $\lim_{x \to 1^+} k(x) = 3$, ¿qué pasa con el límite?::No existe, porque los dos laterales no coinciden: la discontinuidad es de salto.
> - ¿Qué relación hay entre un límite lateral infinito y la gráfica?::Si un lateral tiende a más o menos infinito, la recta $x = a$ es una asíntota vertical.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la definición $\varepsilon$-$\delta$ que da sentido a "acercarse por un lado".
> - [[Unidad 2 - Límites/II - Técnicas Básicas/02 - Límites Especiales|02 - Límites Especiales]] — límites que no se resuelven por sustitución directa.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/03 - Límites en Gráficas|03 - Límites en Gráficas]] — la lectura visual de los mismos dos lados.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — qué hacer cuando el límite lateral es infinito.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|03 - Derivabilidad y Continuidad]] — la derivada lateral nace de limitar por un solo lado.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — la continuidad es exactamente la igualdad entre límite y valor.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero funciones por partes hasta que elegir la fórmula de cada lado sea automático.
> - Después pasa a [[Unidad 2 - Límites/II - Técnicas Básicas/03 - Límites en Gráficas|03 - Límites en Gráficas]] para leer esos mismos dos lados directamente en una curva.
> - Cuando aparezca un 0/0 tras calcular los laterales, ve a [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]].
> - En cada ejercicio, escribe antes de calcular **qué fórmula corresponde a cada lado y por qué**.

---

**Tags:** #MATG1045 #unidad2 #limites-laterales #calculo #limites #discontinuidades #funciones-por-partes #izquierda-derecha #existencia-limites #continuidad #matematicas #analisis

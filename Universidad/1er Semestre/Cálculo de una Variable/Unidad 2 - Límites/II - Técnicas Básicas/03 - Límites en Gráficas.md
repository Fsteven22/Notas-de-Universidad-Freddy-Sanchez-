---
dg-publish: true
tags: [MATG1045, unidad2, limites-en-graficas, calculo, limites, graficas, interpretacion-visual, continuidad, discontinuidades, asitotas, lectura-grafica, analisis-visual]
---

# 📈 Límites en Gráficas

## 🎯 Introducción

> [!tip] 🎯 Concepto Central
>
> **Leer límites en gráficas** es como ser un detective visual: observamos hacia dónde "apunta" la función cuando nos acercamos a un punto, sin importar qué pase exactamente en ese punto. La gráfica nos cuenta la historia completa del comportamiento de la función.

---

## 📋 Definiciones Formales

> [!info] 🔍 Definición de límite leído en una gráfica
>
> Para encontrar $\lim_{x \to a} f(x)$ en una gráfica se sigue siempre el mismo procedimiento:
>
> 1. **Localiza** el punto $x = a$ en el eje horizontal.
> 2. **Acércate** al punto desde ambos lados.
> 3. **Observa** hacia dónde "apuntan" los valores de $f(x)$.
> 4. **Determina** si ambos lados convergen al mismo valor.
>
> El punto dibujado no decide nada: lo que decide es la tendencia de la curva al acercarse.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límites_en_Gráficas_01.svg]]
>
> **Se lee así:** El diagrama arranca con una **gráfica de f(x)** y pasa a un rectángulo que pide localizar $x = a$. Desde ahí se bifurca en dos ramas paralelas, una por la izquierda y otra por la derecha, que vuelven a unirse en un rombo que pregunta si ambos lados coinciden. Si la respuesta es sí, un rectángulo cierra con que el límite existe y vale $L$; si es no, otro rectángulo avisa que el límite no existe.
>
> **Por qué importa:** Es el procedimiento mental que debes seguir frente a cualquier gráfica. Te evita el error más común: mirar solo un lado o confundir el punto dibujado con el valor del límite.
>
> **Ejemplo:** En $f(x) = \frac{x^2-1}{x-1}$ la curva apunta a $y = 2$ por los dos lados, aunque hay un hueco en $x = 1$, así que el límite existe y vale $2$.

> [!warning] 🎭 Definición de los casos visuales de discontinuidad
>
> Toda gráfica cercana a un punto cae en uno de cuatro casos, y cada caso da una respuesta distinta al límite:
>
> 1. **Curva continua con punto sólido:** el límite existe y vale $f(a)$.
> 2. **Hueco (círculo vacío):** el límite existe pero no coincide con el valor de la función.
> 3. **Salto:** la curva cambia de nivel y los límites laterales difieren, así que el límite no existe.
> 4. **Asíntota vertical:** la función crece sin cota y el límite es infinito.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límites_en_Gráficas_03.svg]]
>
> **Se lee así:** El diagrama parte de la gráfica de $f(x)$ cerca de $x = a$ y llega a un rombo que pregunta qué ve la curva en el punto. De ahí salen cuatro ramas rotuladas: curva sin interrupciones y punto sólido, círculo vacío, salto de nivel y línea vertical punteada. Las dos primeras convergen en el recuadro de que el límite sí existe, y las dos últimas en el recuadro de que no existe.
>
> **Por qué importa:** Este clasificador evita que confundas un hueco con un salto, que es el error más frecuente: el hueco conserva el límite y el salto lo destruye. Identificar el símbolo visual antes de calcular te ahorra la mitad del análisis.
>
> **Ejemplo:** En $g(x) = \frac{x^2-4}{x-2}$ ves un círculo vacío en $x = 2$ y tomas la rama del hueco: el límite existe y vale $4$.

---

## 👀 Cómo Leer Límites Visualmente

> [!info] 🔍 Técnica de lectura en cuatro movimientos
>
> El procedimiento de la definición se ejecuta así frente a cualquier gráfica:
>
> 1. **Marca** el punto $x = a$ en el eje horizontal y levanta la vista hacia la curva.
> 2. **Sigue** la curva desde la izquierda anotando a qué altura tiende.
> 3. **Repite** el mismo recorrido desde la derecha.
> 4. **Compara** las dos alturas: si coinciden, ese es el límite; si no, no existe.
>
> **Por qué importa:** descomponer la lectura en dos recorridos separados impide que el ojo se salte un lado, que es justo donde aparecen los errores.

---

## 🎭 Casos Visuales Fundamentales

### Caso 1: Función Continua 🌊

> [!example] ✅ Límite existe y coincide con el valor de la función
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límites_en_Gráficas_02.svg]]
>
> **Se lee así:** Es un recorrido lineal de tres rectángulos: primero la **curva suave** de la función, luego el punto concreto sobre el eje en $x = a$ y, al final, el resultado de que el límite coincide con el valor de la función. No hay decisiones ni ramas, solo la secuencia de una gráfica sin interrupciones con un punto sólido, donde el límite existe y vale $f(a)$.
>
> **Por qué importa:** Este es el caso base de todo lo demás: si la curva es continua, la lectura del límite es inmediata. Reconocerlo rápido te ahorra análisis algebraico innecesarios en ejercicios de gráfica.
>
> **Ejemplo:** En la función por partes $g(x) = x+1$ si $x < 2$ y $2x-1$ si $x > 2$, ambas ramas llegan a $3$, así que $\lim_{x \to 2} g(x) = 3 = g(2)$.
>
> **Características visuales:**
>
> - La curva es "suave" y sin interrupciones.
> - Hay un punto sólido en $(a, f(a))$.
> - La función se acerca naturalmente al punto.
>
> **Resultado:** $\lim_{x \to a} f(x) = f(a)$ ✨

### Caso 2: Discontinuidad Removible (Hueco) 🕳️

> [!example] ✅ Límite existe pero difiere del valor de la función
>
> **Características visuales:**
>
> - Círculo vacío (hueco) en el punto $(a, f(a))$.
> - Posible punto sólido en otra altura.
> - La curva "apunta" hacia donde debería estar el punto.
>
> |Situación|Descripción visual|Límite|
> |---|---|---|
> |Solo hueco|Círculo vacío en $(a, L)$|$\lim_{x \to a} f(x) = L$|
> |Hueco + punto|Hueco en $(a, L)$, punto en $(a, M)$|$\lim_{x \to a} f(x) = L$|
>
> **Por qué importa:** la altura del punto sólido no cuenta para el límite; lo que cuenta es hacia dónde apunta la curva que rodea al hueco.

### Caso 3: Discontinuidad de Salto 📈📉

> [!warning] ❌ Límite no existe: salto finito
>
> **Características visuales:**
>
> - La función "salta" de un nivel a otro.
> - Límite por la izquierda distinto del límite por la derecha.
> - Puede haber combinación de puntos sólidos y huecos.
>
> **Ejemplo típico:** función escalón.
>
> - Desde la izquierda se acerca a un valor $L_1$.
> - Desde la derecha se acerca a un valor $L_2 \neq L_1$.
> - Como $L_1 \neq L_2$, el límite no existe.
>
> **Por qué importa:** aquí no basta con mirar la curva: hay que nombrar los dos valores y compararlos, porque el salto es una diferencia numérica concreta.

### Caso 4: Discontinuidad Infinita (Asíntota Vertical) ♾️

> [!warning] ♾️ Límite infinito y asíntota vertical
>
> **Características visuales:**
>
> - Línea vertical punteada (asíntota).
> - La función crece o decrece sin límite.
> - Los valores de $f(x)$ van hacia $+\infty$ o $-\infty$.
>
> **Casos posibles:**
>
> - $\lim_{x \to a^-} f(x) = +\infty$ y $\lim_{x \to a^+} f(x) = +\infty$ dan $\lim_{x \to a} f(x) = +\infty$.
> - $\lim_{x \to a^-} f(x) = -\infty$ y $\lim_{x \to a^+} f(x) = -\infty$ dan $\lim_{x \to a} f(x) = -\infty$.
> - Límites laterales con signos opuestos: el límite no existe.
>
> **Por qué importa:** distinguir "infinito" de "no existe" cambia la conclusión y, con ella, la clasificación de la discontinuidad.

---

## 🔬 Análisis Detallado por Tipos

> [!info] 📊 Tabla de identificación visual
>
> |Tipo de gráfica|Símbolo visual|Límite|Continuidad|
> |---|---|---|---|
> |Curva suave|Punto sólido|✅ Existe $= f(a)$|✅ Continua|
> |Con hueco|Círculo vacío|✅ Existe $\neq f(a)$|❌ Discontinua|
> |Hueco + punto|Vacío + sólido|✅ Existe $\neq f(a)$|❌ Discontinua|
> |Salto|Sólido + vacío|❌ No existe|❌ Discontinua|
> |Asíntota vertical|Línea punteada|♾️ Infinito|❌ Discontinua|
>
> **Por qué importa:** esta tabla es la que conviene tener delante cuando se resuelven varios ejercicios seguidos: convierte la lectura de la gráfica en una decisión de una sola entrada.

---

## 🎯 Estrategias de Lectura Visual

> [!tip] 🔍 Método "MIRA"
>
> - **M**arca el punto $x = a$ en el eje horizontal.
> - **I**magina líneas verticales acercándose al punto.
> - **R**astra hacia dónde apuntan los valores de $f(x)$.
> - **A**naliza si ambos lados convergen al mismo valor.
>
> **Por qué importa:** las cuatro letras ordenan la misma secuencia de la definición, de modo que el método no depende de la gráfica sino de la costumbre.

> [!example] 🖱️ Técnica del "dedo seguidor"
>
> 1. **Coloca tu dedo** en un punto alejado de $x = a$.
> 2. **Deslízalo** lentamente siguiendo la curva hacia $x = a$.
> 3. **Observa** hacia dónde se dirige tu dedo en el eje $y$.
> 4. **Repite** desde el otro lado.
> 5. **Compara** ambas direcciones.
>
> **Por qué importa:** es la versión física del procedimiento: el dedo obliga a recorrer la curva entera en vez de saltar al resultado.

---

## 🎪 Casos Especiales Visuales

> [!warning] 🌀 Comportamiento oscilatorio
>
> **¿Cuándo no existe el límite por oscilación?**
>
> - La función "vibra" infinitamente cerca del punto.
> - No se estabiliza en un valor específico.
> - Ejemplo clásico: $f(x) = \sin\left(\frac{1}{x}\right)$ cerca de $x = 0$.
>
> **Identificación visual:**
>
> - Ondas que se vuelven más frecuentes cerca del punto.
> - No hay una "dirección clara" hacia donde apunta.
>
> **Por qué importa:** el oscilatorio es el único caso donde la curva ni siquiera se acerca a un valor por ninguno de los dos lados, así que el límite no existe aunque no haya ni salto ni asíntota.

> [!info] ♾️ Comportamiento asintótico horizontal
>
> Para $\lim_{x \to \infty} f(x)$ o $\lim_{x \to -\infty} f(x)$ se busca:
>
> - líneas horizontales punteadas (asíntotas horizontales),
> - el comportamiento de la función cuando $x$ va muy a la derecha,
> - el comportamiento de la función cuando $x$ va muy a la izquierda.
>
> **Casos:**
>
> - Se acerca a una línea horizontal: el límite es el valor de esa línea.
> - Crece sin límite: el límite es $+\infty$.
> - Decrece sin límite: el límite es $-\infty$.
>
> **Por qué importa:** la misma lectura se aplica al infinito, solo que el punto de referencia deja de estar en el eje y se corre hasta el extremo.

---

## 📚 Ejemplos Prácticos de Lectura

> [!example] 🔍 Ejemplo 1: función racional
>
> Para $f(x) = \frac{x^2 - 1}{x - 1}$:
>
> - Hay un hueco en $x = 1$.
> - La función parece una recta $y = x + 1$ excepto en $x = 1$.
> - Al acercarse a $x = 1$, apunta hacia $y = 2$.
>
> **Conclusión:** $\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = 2$ ✨

> [!example] 🔍 Ejemplo 2: función definida por partes
>
> $$g(x) = \begin{cases} x + 1 & \text{si } x < 2 \\ 3 & \text{si } x = 2 \\ 2x - 1 & \text{si } x > 2 \end{cases}$$
>
> **Análisis visual en $x = 2$:**
>
> - Desde la izquierda sigue $y = x + 1$ y se acerca a $3$.
> - Desde la derecha sigue $y = 2x - 1$ y también se acerca a $3$.
> - Hay un punto sólido en $(2, 3)$.
>
> **Conclusión:** $\lim_{x \to 2} g(x) = 3 = g(2)$, así que la función es continua ✅.

---

## ⚠️ Errores Visuales Comunes

> [!warning] 🚨 Trampas en la lectura gráfica
>
> **Error 1: confundir el valor de la función con el límite.**
> Mirar solo el punto sólido no basta. **Solución:** observar hacia dónde apunta la curva, no solo los puntos.
>
> **Error 2: no verificar ambos lados.**
> Solo mirar desde un lado del punto deja la mitad del problema sin resolver. **Solución:** siempre verificar los límites laterales.
>
> **Error 3: confundir escalas.**
> Leer mal los valores de los ejes cambia la respuesta numérica. **Solución:** prestar atención a las escalas y unidades antes de concluir.
>
> **Por qué importa:** los tres fallos ocurren antes de calcular nada, así que ninguna revisión de aritmética los detecta.

---

## 🛠️ Herramientas Tecnológicas

> [!tip] 🧰 Recursos para práctica visual
>
> **Software recomendado:**
>
> - **Desmos Graphing Calculator**: gráficas interactivas.
> - **GeoGebra**: visualización dinámica.
> - **Wolfram Alpha**: gráficas y análisis.
> - **Mathematica/Maple**: análisis avanzado.
>
> **Ventajas:**
>
> - Zoom para ver detalles.
> - Manipulación de parámetros.
> - Medición precisa de valores.
>
> **Por qué importa:** una gráfica mal escalada induce a leer mal el límite; con la herramienta adecuada puedes comprobar la tendencia que estás afirmando.

---

## 🧠 Mnemotecnia "VISUAL"

> [!tip] 🎓 Para leer límites en gráficas
>
> - **V**e hacia el punto de interés en $x = a$.
> - **I**dentifica el tipo de comportamiento (continuo, salto, hueco, etc.).
> - **S**igue la curva desde ambos lados.
> - **U**bica hacia dónde apuntan los valores de $f(x)$.
> - **A**naliza si los límites laterales coinciden.
> - **L**ee el valor final del límite (si existe).
>
> **Por qué importa:** la palabra completa es la secuencia de trabajo: nada en ella dice "mira el punto", porque el punto nunca es la respuesta.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Para $f(x) = \frac{x^2 - 1}{x - 1}$, describe qué se ve en la gráfica cerca de $x = 1$ y calcula el límite.
>
> > [!success]- ✅ Solución
> >
> > Al factorizar, $f(x) = \frac{(x-1)(x+1)}{x-1} = x + 1$ para $x \neq 1$, así que la gráfica es la recta $y = x + 1$ con un círculo vacío en $(1, 2)$.
> >
> > Siguiendo la curva desde ambos lados, los valores se acercan a $2$ por la izquierda y por la derecha.
> >
> > Como los dos lados coinciden, $\lim_{x \to 1} f(x) = 2$, aunque $f(1)$ no esté definida.

> [!example] 📋 Planteamiento
>
> Lee en la gráfica el límite de $g(x) = \begin{cases} x + 1 & \text{si } x < 2 \\ 3 & \text{si } x = 2 \\ 2x - 1 & \text{si } x > 2 \end{cases}$ en $x = 2$ y clasifica la continuidad.
>
> > [!success]- ✅ Solución
> >
> > Por la izquierda la rama $y = x + 1$ se acerca a $3$; por la derecha la rama $y = 2x - 1$ también se acerca a $3$.
> >
> > Los dos lados coinciden, así que $\lim_{x \to 2} g(x) = 3$.
> >
> > Además el punto $(2, 3)$ está sólido y $g(2) = 3$, por lo que el límite coincide con el valor y la función es continua en ese punto.

> [!example] 📋 Planteamiento
>
> Una gráfica muestra una curva con un círculo vacío en $(2, 4)$ y un punto sólido en $(2, 1)$. ¿Qué vale $\lim_{x \to 2} f(x)$ y qué discontinuidad hay?
>
> > [!success]- ✅ Solución
> >
> > El círculo vacío indica que la curva apunta a la altura $4$ por los dos lados, así que $\lim_{x \to 2} f(x) = 4$.
> >
> > El punto sólido solo fija el valor de la función: $f(2) = 1$, distinto del límite.
> >
> > Es una discontinuidad **removible**: el límite existe pero no coincide con el valor.

> [!example] 📋 Planteamiento
>
> En una gráfica, la curva llega a $x = 1$ con altura $2$ por la izquierda y altura $5$ por la derecha, con un punto sólido en $(1, 5)$. ¿Existe el límite?
>
> > [!success]- ✅ Solución
> >
> > El límite izquierdo vale $2$ y el derecho vale $5$.
> >
> > Como $2 \neq 5$, el límite no existe: es una discontinuidad **de salto**.
> >
> > El punto sólido en $(1, 5)$ solo dice que $f(1) = 5$; no hace que el límite aparezca.

> [!example] 📋 Planteamiento
>
> La gráfica de $f(x) = \frac{1}{x - 2}$ muestra una línea vertical punteada en $x = 2$. Describe lo que ocurre por cada lado y concluye.
>
> > [!success]- ✅ Solución
> >
> > Siguiendo la curva por la izquierda, los valores se disparan hacia $-\infty$; por la derecha se disparan hacia $+\infty$.
> >
> > Por lo tanto $\lim_{x \to 2^-} f(x) = -\infty$ y $\lim_{x \to 2^+} f(x) = +\infty$.
> >
> > El límite no existe y $x = 2$ es una asíntota vertical, porque los dos lados no solo difieren sino que van en signos opuestos.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Localizo $x = a$ en una gráfica y sigo la curva por cada lado para decir hacia dónde apunta.
> - [ ] Distingo en una gráfica un punto sólido de un círculo vacío y explico qué significa cada uno.
> - [ ] Escribo el límite que sugiere una gráfica simple y lo comparo con el valor de la función.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Clasifico una discontinuidad visual como removible, de salto o infinita.
> - [ ] Aplico el método MIRA y la técnica del dedo seguidor para no saltarme ningún lado.
> - [ ] Leo en una gráfica una asíntota vertical y una horizontal y las relaciono con su límite.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Detecto la falta de límite por oscilación en funciones como $\sin(1/x)$.
> - [ ] Resuelvo en una sola lectura los ejemplos de función racional y de función por partes.
> - [ ] Explico por qué la escala mal leída cambia el resultado y cómo verificarla antes de concluir.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2: límites y sus interpretaciones gráficas.
> - R. Larson, *Cálculo* (Cengage), cap. 1: lectura de gráficas y discontinuidades.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 3: límite y tipos de discontinuidad.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la definición formal que la gráfica interpreta.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — el cálculo de los dos lados que aquí se lee.
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — el comportamiento asintótico completo.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué se mira en una gráfica para calcular $\lim_{x \to a} f(x)$?::La tendencia de la curva al acercarse a $x = a$ por la izquierda y por la derecha, no el punto dibujado.
> - ¿Qué indica un círculo vacío en la gráfica?::Que hay una discontinuidad removible: el límite existe, pero no coincide con el valor de la función o este ni siquiera está definido.
> - ¿Cuándo es de salto una discontinuidad visual?::Cuando la curva cambia de nivel y los límites laterales tienen valores distintos; entonces el límite no existe.
> - ¿Qué distingue a la discontinuidad infinita de la de salto?::En la infinita la función se va a más o menos infinito contra una asíntota vertical; en la de salto se queda en valores finitos distintos.
> - ¿Cómo se detecta la falta de límite por oscilación?::Viendo que la curva vibra sin estabilizarse cerca del punto, como $\sin(1/x)$ en $x = 0$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite|01 - Concepto y Definición Formal del Límite]] — la base conceptual que la gráfica traduce.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — los límites laterales que se leen en cada rama.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/02 - Límites Especiales|02 - Límites Especiales]] — los casos donde la sustitución directa falla.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — qué significa que la función se vaya a infinito.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — la continuidad como coincidencia entre límite y valor.
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — asíntotas verticales y horizontales vistas con más detalle.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica con gráficas sencillas hasta que identificar el caso visual sea inmediato.
> - Después combina la lectura gráfica con [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] para verificar los dos lados algebraicamente.
> - Cuando la gráfica muestre una asíntota, pasa a [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]].
> - En cada ejercicio, escribe antes de responder **qué símbolo visual estás leyendo y qué te permite concluir**.

---

**Tags:** #MATG1045 #unidad2 #limites-en-graficas #calculo #limites #graficas #interpretacion-visual #continuidad #discontinuidades #asitotas #lectura-grafica #analisis-visual #matematicas #funciones

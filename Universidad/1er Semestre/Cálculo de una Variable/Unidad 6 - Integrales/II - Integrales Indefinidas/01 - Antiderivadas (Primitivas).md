---
dg-publish: true
tags: [MATG1045, unidad6, antiderivadas, primitivas, integral-indefinida, derivacion-inversa, problemas-valor-inicial, familia-curvas, verificacion]
---

# 🔄 Antiderivadas (Primitivas)

## 🎯 Introducción

> [!info] 💡 Qué es una antiderivada
>
> Una **antiderivada** (o primitiva) de una función $f(x)$ es cualquier función $F(x)$ cuya derivada sea $f(x)$. Es el proceso inverso de la derivación y la base de la **integración indefinida**.
>
> **Por qué importa:** con ella se reconstruyen funciones a partir de sus tasas de cambio: de la aceleración a la velocidad, de la velocidad a la posición, de una razón de crecimiento a la población. Es además la entrada obligatoria a las ecuaciones diferenciales.
>
> **Ejemplo:** si $f(x) = 2x$, entonces $F(x) = x^2$, $F(x) = x^2 + 5$ y $F(x) = x^2 - 3$ son todas antiderivadas: derivarlas devuelve $2x$.

> [!info] 🗺️ El mapa de la nota
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Antiderivadas_(Primitivas)_01.svg]]
>
> **Se lee así:** un mapa con el tema central "Antiderivadas" en el centro y cuatro ramas hacia los bloques de la nota: **Fundamentos** (definición, existencia y unicidad, notación, verificación), **Técnicas** (fórmulas básicas, propiedades lineales, casos especiales), **Aplicaciones** (problemas de valor inicial, modelado físico, reconstrucción de funciones) y **Conexiones** (derivadas, integrales definidas, ecuaciones diferenciales).
>
> **Por qué importa:** sirve de índice visual: si recuerdas las cuatro ramas, recuerdas el orden completo de la nota y dónde buscar cada herramienta.
>
> **Ejemplo:** un ejercicio de valor inicial cae en la rama *Aplicaciones*, y su comprobación derivando vuelve a la rama *Fundamentos*.

> [!warning] ⚠️ Los tres errores que más se repiten
>
> 1. **NO** olvides el $+C$: la respuesta es siempre una familia completa.
> 2. **NO** apliques la regla de potencia a $n = -1$: $\int x^{-1}\,dx = \ln|x| + C$, no una división entre cero.
> 3. **NO** escribas una constante por término: es **una sola** $C$ para toda la expresión.
>
> **Por qué importa:** los tres son errores de formato que invalidan un cálculo correcto, y por eso el parcial los penaliza sin piedad.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Antiderivada y notación
>
> Si $F'(x) = f(x)$ para todo $x$ de un intervalo $I$, entonces:
>
> - $F(x)$ es una **antiderivada** (primitiva) de $f(x)$ en $I$;
> - la **integral indefinida** se denota $\int f(x)\,dx = F(x) + C$;
> - $C$ es la **constante de integración** y el conjunto de todas las antiderivadas forma una **familia de funciones**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Antiderivadas_(Primitivas)_02.svg]]
>
> **Se lee así:** un ciclo de ida y vuelta entre dos rectángulos: de $f$ sale una flecha de **antiderivación** hacia $F + C$, y de $F + C$ sale una flecha de **derivación** que vuelve a $f$. Una tercera caja, "familia de funciones", apunta hacia $F + C$, indicando que a un integrando le corresponde toda una familia.
>
> **Por qué importa:** el diagrama fija el orden mental correcto: integrar construye y derivar **verifica**. También recuerda que la respuesta nunca es una función suelta, sino una familia completa con su $+C$.
>
> **Ejemplo:** en $\int 2x\,dx = x^2 + C$ sigues la flecha de antiderivación; al derivar $x^2 + C$ vuelves a $2x$ por la flecha de derivación.

> [!note] 📋 Notación de la integral
>
> Cada símbolo tiene un significado fijo:
>
> - $\int$: símbolo de integral (del latín *summa*).
> - $f(x)$: **integrando**, la función de la que se busca la primitiva.
> - $dx$: **diferencial** de $x$, que indica la variable de integración.
> - $C$: constante de integración, obligatoria en las indefinidas.
>
> **Por qué importa:** la variable es $dx$, no la $x$ del límite superior en una integral definida. Distinguir ambos símbolos evita el error de integrar respecto de la variable equivocada.

---

## 🏗️ Existencia y unicidad

> [!success] ✅ Teorema de existencia
>
> Si $f(x)$ es **continua** en un intervalo $I$, entonces $f(x)$ tiene al menos una antiderivada en $I$.
>
> **Por qué importa:** la continuidad es la condición que garantiza que el proceso inverso existe. Sin ella puede no haber antiderivada en algunos intervalos, como ocurre con las funciones con saltos.

> [!success] ✅ Teorema de unicidad
>
> Si $F$ y $G$ son dos antiderivadas de $f$ en un intervalo $I$, entonces
>
> $$G(x) = F(x) + C$$
>
> para alguna constante $C$.
>
> **Por qué importa:** es la razón de que $+C$ sea **obligatorio y suficiente**: todas las antiderivadas difieren únicamente por una constante, y una condición inicial basta para fijarla.
>
> **Ejemplo:** $x^2$ y $x^2 + 100$ son primitivas de $2x$; no hay una tercera opción que no sea de esa forma.

---

## 🧮 Fórmulas básicas

> [!info] 📋 La tabla de integrales notables
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/cal1-integrales-tabla-20-notables.jpg]]
>
> **Se lee así:** un catálogo de veinte entradas donde cada línea muestra un integrando y, a continuación, su antiderivada cerrada con $C$. Las fórmulas van por familias: potencias elementales, logaritmos y exponenciales, trigonométricas directas, inversas trigonométricas e hiperbólicas.
>
> **Por qué importa:** tenerla a la mano evita improvisar la antiderivada de un seno o de un $1/x$. Además recuerda dos detalles que se olvidan: toda indefinida termina en $+C$ y el valor absoluto del logaritmo no es opcional.
>
> **Ejemplo:** para $\int (2\operatorname{sen} x - 3\cos x + 4\sec^2 x)\,dx$ la tabla da de inmediato las tres antiderivadas que hay que combinar.

> [!tip] 🔧 La regla de potencia, con su excepción
>
> Para $n \neq -1$:
>
> $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C.$$
>
> El caso $n = -1$ es distinto: $\displaystyle\int x^{-1}\,dx = \int \frac{1}{x}\,dx = \ln|x| + C$.
>
> **Por qué importa:** la excepción es la trampa clásica del examen: dividir entre $n+1 = 0$ no existe, y la respuesta correcta involucra el logaritmo.

---

## ⚖️ Propiedades de las antiderivadas

> [!success] ✅ Linealidad
>
> 1. **Suma:** $\displaystyle\int \big[f(x) + g(x)\big]\,dx = \int f(x)\,dx + \int g(x)\,dx$
> 2. **Constante:** $\displaystyle\int k\,f(x)\,dx = k\int f(x)\,dx$
> 3. **Diferencia:** $\displaystyle\int \big[f(x) - g(x)\big]\,dx = \int f(x)\,dx - \int g(x)\,dx$
>
> **Por qué importa:** la linealidad es lo que permite partir un polinomio en términos e integrar cada uno por separado con la fórmula de potencias.

> [!warning] ⚠️ Lo que NO se reparte
>
> - $\displaystyle\int f(x)\,g(x)\,dx \neq \int f(x)\,dx \cdot \int g(x)\,dx$
> - $\displaystyle\int \frac{f(x)}{g(x)}\,dx \neq \frac{\int f(x)\,dx}{\int g(x)\,dx}$
> - Y la constante es **una sola** para toda la expresión, no una por término.
>
> **Por qué importa:** confundir la linealidad con el producto es el error conceptual más grave de esta sección; para productos existen técnicas propias (partes, cambio de variable) que se ven en la nota de Técnicas de Integración.

---

## ✅ Verificación por derivación

> [!example] 🔍 El método de verificación
>
> Para comprobar que $F(x)$ es antiderivada de $f(x)$:
>
> 1. Calcula $F'(x)$.
> 2. Verifica que $F'(x) = f(x)$.
> 3. Si coincide, la antiderivada general es $F(x) + C$.
>
> **Problema:** verificar que $F(x) = \frac{x^4}{4} - 2x^3 + 5x^2 - 7x$ es primitiva de $f(x) = x^3 - 6x^2 + 10x - 7$.
>
> $$F'(x) = \frac{4x^3}{4} - 6x^2 + 10x - 7 = x^3 - 6x^2 + 10x - 7 = f(x)\ \checkmark$$
>
> **Por qué importa:** derivar toma diez segundos y descarta de inmediato un error de signo o de potencia. Es el control de calidad obligatorio antes de entregar.

---

## 💡 Ejemplos desarrollados

> [!example] 🔢 Polinomio: $\int (4x^3 - 6x^2 + 2x - 8)\,dx$
>
> Se aplica la linealidad y luego la regla de potencia:
>
> $$= 4\cdot\frac{x^4}{4} - 6\cdot\frac{x^3}{3} + 2\cdot\frac{x^2}{2} - 8x + C = x^4 - 2x^3 + x^2 - 8x + C.$$
>
> **Por qué importa:** es el esquema de cualquier polinomio: *separa, saca constantes, baja exponente y suma uno*.

> [!example] 🔢 Con radicales: $\int \left(3\sqrt{x} - \dfrac{4}{\sqrt{x}} + 2\sqrt[3]{x^2}\right)dx$
>
> Primero se reescribe con exponentes: $\int (3x^{1/2} - 4x^{-1/2} + 2x^{2/3})\,dx$. Después:
>
> $$= 3\cdot\frac{x^{3/2}}{3/2} - 4\cdot\frac{x^{1/2}}{1/2} + 2\cdot\frac{x^{5/3}}{5/3} + C = 2x^{3/2} - 8x^{1/2} + \frac{6x^{5/3}}{5} + C.$$
>
> **Por qué importa:** reescribir con exponentes fraccionarios y negativos es el paso que hace posible aplicar una sola fórmula a expresiones que parecen distintas.

> [!example] 🔢 Racional: $\int \dfrac{2x^4 - 3x^2 + 5}{x^3}\,dx$
>
> Se separa la fracción: $\int \left(2x - 3x^{-1} + 5x^{-3}\right)dx$ y se integra término a término:
>
> $$= 2\cdot\frac{x^2}{2} - 3\ln|x| + 5\cdot\frac{x^{-2}}{-2} + C = x^2 - 3\ln|x| - \frac{5}{2x^2} + C.$$
>
> **Por qué importa:** el término $x^{-1}$ obliga a usar el logaritmo: es la única potencia que no sigue la regla general, y en una fracción aparece mucho más de lo que parece.

> [!example] 🔢 Trigonométricas: $\int (2\operatorname{sen} x - 3\cos x + 4\sec^2 x)\,dx$
>
> Directo de la tabla:
>
> $$= 2(-\cos x) - 3(\operatorname{sen} x) + 4\tan x + C = -2\cos x - 3\operatorname{sen} x + 4\tan x + C.$$
>
> **Por qué importa:** el signo del seno es el que se olvida: $\int \operatorname{sen} x\,dx = -\cos x + C$, y verificar derivando lo confirma al instante.

---

## 🧩 Problemas de valor inicial

> [!tip] 🔧 Método en tres pasos
>
> Un **problema de valor inicial (PVI)** busca una función $F$ con $F'(x) = f(x)$ y $F(x_0) = y_0$:
>
> 1. Encontrar la antiderivada general $F(x) = \int f(x)\,dx$.
> 2. Usar la condición inicial para determinar $C$.
> 3. Escribir la solución particular.
>
> **Por qué importa:** el PVI es el puente entre la familia infinita y la función única que modela el problema físico concreto.

> [!example] 🔢 Ejemplo completo con verificación
>
> **Problema:** hallar $F(x)$ tal que $F'(x) = 3x^2 - 4x + 1$ y $F(2) = 10$.
>
> - **Paso 1:** $F(x) = \int (3x^2 - 4x + 1)\,dx = x^3 - 2x^2 + x + C$.
> - **Paso 2:** $F(2) = 8 - 8 + 2 + C = 10 \Rightarrow 2 + C = 10 \Rightarrow C = 8$.
> - **Paso 3:** $F(x) = x^3 - 2x^2 + x + 8$.
>
> **Verificación:** $F'(x) = 3x^2 - 4x + 1$ ✓ y $F(2) = 8 - 8 + 2 + 8 = 10$ ✓
>
> **Por qué importa:** las dos comprobaciones son distintas: una confirma la derivada, la otra la condición inicial. Hacer ambas descarta cualquier error de $C$.

---

## 🎭 Interpretación geométrica

> [!info] 🖼️ La familia de curvas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Antiderivadas_(Primitivas)_03.svg]]
>
> **Se lee así:** dos caminos que desembocan en la familia de antiderivadas. Por un lado, la función $f$ atraviesa un rombo de decisión (el campo de direcciones) y sale hacia la familia $F + C$, desde la que se abren tres ramas: curva de referencia con $C = 0$, curvas superiores con $C > 0$ y curvas inferiores con $C < 0$. Por otro lado, una cadena va de la condición inicial a fijar el valor de $C$ y termina eligiendo una única curva.
>
> **Por qué importa:** el esquema muestra que **todas** las antiderivadas tienen la misma forma y solo cambian de altura, y que la condición inicial es lo que selecciona una sola curva de la familia.
>
> **Ejemplo:** para $f(x) = 2x$ la familia es $x^2 + C$: parábolas idénticas desplazadas verticalmente, todas con pendiente $2$ en $x = 1$.

> [!example] 📐 Lo que significa cada símbolo en el plano
>
> - **Familia de curvas:** las antiderivadas difieren por traslaciones verticales.
> - **Constante $C$:** el desplazamiento vertical entre curvas vecinas.
> - **Pendiente común:** en $x = a$, todas tienen pendiente $f(a)$.
> - **Campo de pendientes:** $f(x)$ dibuja las direcciones que las antiderivadas siguen.
>
> **Por qué importa:** es la lectura geométrica que conecta con la Unidad 4: la primitiva es la curva que *recorre* el campo de direcciones trazado por $f$.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\int (5x^4 - 3x^2 + 7)\,dx$.
>
> > [!success]- ✅ Solución
> >
> > Linealidad y regla de potencia:
> >
> > $$5\cdot\frac{x^5}{5} - 3\cdot\frac{x^3}{3} + 7x + C = x^5 - x^3 + 7x + C.$$
> >
> > **Respuesta:** $x^5 - x^3 + 7x + C$.
> >
> > Verificación: $\frac{d}{dx}(x^5 - x^3 + 7x + C) = 5x^4 - 3x^2 + 7$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \dfrac{1}{x^3}\,dx$ y $\int \dfrac{1}{x}\,dx$ comparando los dos resultados.
>
> > [!success]- ✅ Solución
> >
> > El primero es una potencia con $n = -3$:
> >
> > $$\int x^{-3}\,dx = \frac{x^{-2}}{-2} + C = -\frac{1}{2x^2} + C.$$
> >
> > El segundo es el caso $n = -1$, que **no** sigue la regla:
> >
> > $$\int \frac{1}{x}\,dx = \ln|x| + C.$$
> >
> > **Respuesta:** $-\dfrac{1}{2x^2} + C$ y $\ln|x| + C$. La comparación muestra por qué $n = -1$ es la excepción.

> [!example] 📋 Planteamiento
>
> Encuentra la antiderivada de $f(x) = 3x^2 - 4x + 1$ que cumple $F(2) = 10$.
>
> > [!success]- ✅ Solución
> >
> > Familia general: $F(x) = x^3 - 2x^2 + x + C$.
> >
> > Condición inicial: $F(2) = 8 - 8 + 2 + C = 2 + C = 10$, luego $C = 8$.
> >
> > **Respuesta:** $F(x) = x^3 - 2x^2 + x + 8$.
> >
> > Comprobación: $F'(x) = 3x^2 - 4x + 1$ ✓ y $F(2) = 10$ ✓

> [!example] 📋 Planteamiento
>
> Un objeto tiene aceleración $a(t) = 6t$ m/s² y velocidad inicial $v(0) = 4$ m/s. Encuentra $v(t)$ y luego $s(t)$ con $s(0) = 0$.
>
> > [!success]- ✅ Solución
> >
> > Velocidad: $v(t) = \int 6t\,dt = 3t^2 + C_1$. Con $v(0) = 4$ se obtiene $C_1 = 4$, luego $v(t) = 3t^2 + 4$.
> >
> > Posición: $s(t) = \int (3t^2 + 4)\,dt = t^3 + 4t + C_2$. Con $s(0) = 0$ resulta $C_2 = 0$.
> >
> > **Respuesta:** $v(t) = 3t^2 + 4$ m/s y $s(t) = t^3 + 4t$ m.
> >
> > Verificación: $v(t) = s'(t) = 3t^2 + 4$ ✓

> [!example] 📋 Planteamiento
>
> Verifica que $F(x) = \frac{x^4}{4} - 2x^3 + 5x^2 - 7x$ es primitiva de $f(x) = x^3 - 6x^2 + 10x - 7$.
>
> > [!success]- ✅ Solución
> >
> > Se deriva término a término:
> >
> > $$F'(x) = \frac{4x^3}{4} - 6x^2 + 10x - 7 = x^3 - 6x^2 + 10x - 7.$$
> >
> > El resultado coincide con $f(x)$.
> >
> > **Respuesta:** $F$ es primitiva de $f$, y la antiderivada general es $F(x) + C$.

> [!example] 📋 Planteamiento
>
> Integra $\int \dfrac{x^3 + 2x - 1}{x^2}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > Se separa la fracción: $\frac{x^3}{x^2} + \frac{2x}{x^2} - \frac{1}{x^2} = x + 2x^{-1} - x^{-2}$.
> >
> > Integrando término a término:
> >
> > $$\frac{x^2}{2} + 2\ln|x| + \frac{1}{x} + C.$$ (recordar que $\int -x^{-2}\,dx = -\frac{x^{-1}}{-1} = \frac{1}{x}$)
> >
> > **Respuesta:** $\dfrac{x^2}{2} + 2\ln|x| + \dfrac{1}{x} + C$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino antiderivada e integral indefinida y distingo la familia de funciones de una solución particular.
> - [ ] Aplico la regla de potencia a potencias positivas, fraccionarias y negativas.
> - [ ] Escribo la tabla de integrales notables sin consultar.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Integro polinomios, racionales simples y trigonométricas usando linealidad.
> - [ ] Resuelvo problemas de valor inicial fijando la constante con la condición dada.
> - [ ] Verifico cualquier resultado derivándolo antes de darlo por bueno.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Enuncio los teoremas de existencia y unicidad y explico por qué la continuidad es la condición.
> - [ ] Interpreto geométricamente una familia de curvas y el papel del campo de pendientes.
> - [ ] Traduzco un problema físico (aceleración a posición) en dos integrales con condiciones iniciales.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: antiderivadas y problemas de valor inicial.
> - R. Larson, *Cálculo* (Cengage), cap. 5: la notación de integral indefinida.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 5: antiderivadas como familias de curvas.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] — las reglas que aquí se invierten.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración|03 - Constante de integración]] — el $+C$ en profundidad.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el puente que hace útil todo esto.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es una antiderivada de $f$?::Cualquier función $F$ con $F'(x) = f(x)$ en un intervalo; el conjunto completo es $\int f(x)\,dx = F(x) + C$.
> - ¿Cuál es la regla de potencia?::$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$ para $n \neq -1$; si $n = -1$ la respuesta es $\ln|x| + C$.
> - ¿Qué garantiza el teorema de existencia?::Que si $f$ es continua en $I$, entonces $f$ tiene al menos una antiderivada en $I$.
> - ¿Qué dice el teorema de unicidad?::Que dos antiderivadas de la misma función difieren por una constante: $G(x) = F(x) + C$.
> - ¿Cómo se resuelve un problema de valor inicial?::Se integra, se sustituye la condición $F(x_0) = y_0$ para despejar $C$ y se escribe la solución particular.
> - ¿Se puede repartir el producto en una integral indefinida?::No: $\int f g\,dx \neq \int f\,dx \cdot \int g\,dx$; solo se reparte la suma y la multiplicación por constantes.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] — las reglas que se invierten para integrar.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración|03 - Constante de integración]] — por qué existe la $C$ y cuándo se fija.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — la tabla completa de fórmulas directas.
> - [[Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — para integrales que no salen de una sola.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la Parte II que usa estas antiderivadas.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la aplicación geométrica de la integral definida.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: la regla de potencia y sus excepciones deben salirte sin pensar.
> - Después salta al 3 y al 4, donde el problema de valor inicial y la aplicación física son el paso siguiente.
> - Cuando domines ambos, usa el 6 para ver cómo una fracción se vuelve integrable al separarla.
> - Cierra con [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|Integrales Notables]], donde la tabla completa amplía lo visto aquí.

---

**Tags:** #MATG1045 #unidad6 #antiderivadas #primitivas #integral-indefinida #derivacion-inversa #problemas-valor-inicial #familia-curvas #verificacion

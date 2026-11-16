---
dg-publish: true
tags: [MATG1045, unidad6, teorema-fundamental-calculo, regla-barrow, funciones-integrales, valor-medio, limites-variables, aplicaciones-fisica]
---

# ⚡ Teorema Fundamental del Cálculo

## 🎯 Introducción

> [!info] 💡 El puente entre derivadas e integrales
>
> El **teorema fundamental del cálculo (TFC)** demuestra que derivar y antiderivar son operaciones inversas. Con él, calcular un área deja de exigir sumas de rectángulos y pasa a ser buscar una antiderivada y evaluarla en dos puntos.
>
> **Por qué importa:** unifica los dos grandes problemas de la historia del cálculo: las tangentes (derivadas) y las cuadraturas (áreas). Sin este teorema, la integral sería una herramienta de aproximación; con él, es una herramienta de cálculo exacto.
>
> **Ejemplo:** para calcular $\int_0^3 2x\,dx$ ya no hace falta particionar el intervalo: basta con $F(x) = x^2$ y evaluar $9 - 0 = 9$.

> [!warning] ⚠️ La confusión que separa las dos partes
>
> - **Parte I:** da la derivada de una integral con límite variable: $\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$. Responde *qué derivada tiene el área acumulada*.
> - **Parte II (regla de Barrow):** permite evaluar la integral: $\int_a^b f(x)\,dx = F(b) - F(a)$. Responde *cuánto vale el área*.
>
> **Por qué importa:** usar la parte equivocada es el error más caro de la unidad. Si el ejercicio pide **derivar**, aplica la Parte I; si pide **calcular una integral**, aplica la Parte II.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Primera parte del teorema fundamental
>
> Si $f$ es continua en $[a,b]$, la función **área acumulada**
>
> $$F(x) = \int_a^x f(t)\,dt$$
>
> es diferenciable en $(a,b)$ y su derivada es la función original:
>
> $$F'(x) = f(x).$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Teorema_Fundamental_del_Cálculo_01.svg]]
>
> **Se lee así:** una cadena de rectángulos que avanza hacia abajo: se enuncia el TFC Parte I ($\frac{d}{dx}$ de $\int_{a}^{x} f(t)\,dt = f(x)$), se marca la condición "$f$ continua en $[a,b]$", se define $F(x) = \int_a^x f(t)\,dt$, se concluye que $F$ es diferenciable en $(a,b)$ y que $F'(x) = f(x)$, y dos cajas finales lo interpretran: $F(x)$ es el área acumulada desde $a$ hasta $x$, y la tasa de cambio del área es la altura de $f$ en $x$.
>
> **Por qué importa:** la última casilla es la lectura física de la idea: *la velocidad con que crece el área es exactamente la altura de la curva*. Es la demostración intuitiva de que integrar y derivar se cancelan.
>
> **Ejemplo:** con $F(x) = \int_0^x 3t^2\,dt = x^3$, la derivada $F'(x) = 3x^2$ devuelve la función original, como predice el diagrama.

> [!note] 📋 Definición — Segunda parte del teorema (regla de Barrow)
>
> Si $f$ es continua en $[a,b]$ y $F$ es **cualquier** primitiva de $f$, entonces
>
> $$\int_a^b f(x)\,dx = F(b) - F(a) = \big[F(x)\big]_a^b.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Teorema_Fundamental_del_Cálculo_02.svg]]
>
> **Se lee así:** una cadena de seis casillas numeradas: se enuncia la Parte II ($\int_{a}^{b} f(x)\,dx = F(b) - F(a)$), se fija la condición ($f$ continua, $F' = f$), siguen los tres pasos —hallar una antiderivada $F(x)$, evaluar $F$ en los límites, calcular $F(b) - F(a)$—, se escribe la notación compacta $[F(x)]_a^b$, y una caja final recuerda verificar derivando, porque $F'(x)$ debe dar $f(x)$.
>
> **Por qué importa:** el diagrama convierte el teorema en un **algoritmo fijo de tres pasos**. Fíjate en la última casilla: la verificación derivando es parte del procedimiento, no un extra.
>
> **Ejemplo:** $\int_1^4 2x\,dx$: antiderivada $F(x) = x^2$, evaluación $16 - 1 = 15$, verificación $F'(x) = 2x$ ✓.

---

## 🧮 Cómo se aplica la Parte II

> [!example] 🔢 Aplicación directa: $\int_1^4 2x\,dx$
>
> 1. **Antiderivada:** $F(x) = x^2$ (comprobando: $F'(x) = 2x$ ✓).
> 2. **Evaluar:** $F(4) = 16$ y $F(1) = 1$.
> 3. **Restar:** $16 - 1 = 15$.
>
> **Por qué importa:** es el caso mínimo del algoritmo de tres pasos; si este no sale automático, los siguientes tampoco.

> [!example] 🔢 Función trigonométrica: $\int_0^{\pi/2} \cos x\,dx$
>
> 1. **Antiderivada:** $F(x) = \operatorname{sen}(x)$ (comprobando: $F'(x) = \cos x$ ✓).
> 2. **Evaluar:** $F(\pi/2) = 1$ y $F(0) = 0$.
> 3. **Restar:** $1 - 0 = 1$.
>
> **Por qué importa:** confirma que la regla de Barrow funciona igual con trigonometría: el límite superior se sustituye y se resta el inferior. Geométricamente, el área bajo el cuarto de coseno vale exactamente $1$.

> [!example] 🔢 Con la Parte I: derivar $\frac{d}{dx}\left[\int_2^x t^3\,dt\right]$
>
> Aquí **no** se calcula la integral: se aplica la Parte I directamente. La variable del límite superior es $x$, así que la derivada es la función integrada evaluada en $x$:
>
> $$\frac{d}{dx}\left[\int_2^x t^3\,dt\right] = x^3.$$
>
> **Verificación calculando la integral:** $\int_2^x t^3\,dt = \frac{x^4}{4} - \frac{16}{4}$, y derivando se recupera $x^3$ ✓.
>
> **Por qué importa:** muestra la diferencia con el caso anterior: si la $x$ solo aparece en el límite, el teorema resuelve la derivada sin integrar nada.

---

## 🔄 Límites variables en la Parte I

> [!tip] 🔧 Caso general con dos límites funcionales
>
> Cuando ambos límites dependen de $x$, se aplica la regla de la cadena a la Parte I:
>
> $$\frac{d}{dx}\left[\int_{g(x)}^{h(x)} f(t)\,dt\right] = f\big(h(x)\big)\cdot h'(x) - f\big(g(x)\big)\cdot g'(x).$$
>
> **Por qué importa:** la fórmula tiene la estructura *arriba con su derivada, menos abajo con su derivada*. Decirla en voz alta evita el error de signo en el límite inferior.
>
> **Ejemplo:** $\frac{d}{dx}\left[\int_{x^2}^{x^3} \operatorname{sen}(t)\,dt\right] = \operatorname{sen}(x^3)\cdot 3x^2 - \operatorname{sen}(x^2)\cdot 2x$, usando $h(x) = x^3$ y $g(x) = x^2$.

> [!example] 🔢 Doble comprobación del caso general
>
> Con $F$ primitiva de $f$, la integral vale $F(h(x)) - F(g(x))$, y derivando por la regla de la cadena se obtiene exactamente la fórmula anterior: $F'(h(x))h'(x) - F'(g(x))g'(x) = f(h(x))h'(x) - f(g(x))g'(x)$.
>
> **Por qué importa:** esa línea de tres pasos es la demostración completa. Si un día olvidas la fórmula, puedes reconstruirla derivando $F(h(x)) - F(g(x))$.

---

## 📐 Propiedades y corolarios

> [!info] 🖼️ Propiedades de la función acumulada
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Teorema_Fundamental_del_Cálculo_03.svg]]
>
> **Se lee así:** una caja central con $F(x) = \int_a^x f(t)\,dt$ se abre en cuatro ramas paralelas. Tres enumeran propiedades de $F$: que es continua en $[a,b]$, que es diferenciable con $F'(x) = f(x)$, y que cumple la condición inicial $F(a) = 0$. La cuarta conduce a un corolario más ancho: el **valor medio para integrales**, $\int_a^b f(x)\,dx = f(c)(b-a)$.
>
> **Por qué importa:** el diagrama reúne en un solo lugar las propiedades de la función acumulada y el corolario más usado. Te evita confundir el **valor medio para integrales** con el **teorema del valor medio** de las derivadas, que son dos afirmaciones distintas.
>
> **Ejemplo:** para $\int_0^{\pi} \operatorname{sen}(x)\,dx = 2$, el corolario garantiza que existe $c \in [0,\pi]$ con $\operatorname{sen}(c)\cdot\pi = 2$, es decir $c = \arcsin(2/\pi) \approx 0.69$.

> [!success] ✅ Los dos corolarios por escrito
>
> 1. **Valor medio para integrales:** si $f$ es continua en $[a,b]$, existe $c \in [a,b]$ tal que
>
> $$\int_a^b f(x)\,dx = f(c)\,(b-a).$$
>
> 2. **Caracterización de antiderivadas:** si $F'(x) = G'(x) = f(x)$ en un intervalo, entonces $F(x) = G(x) + C$ para alguna constante $C$.
>
> **Por qué importa:** el corolario 1 dice que el área tiene un valor que **alguna altura representa**; el corolario 2 justifica que escribir $+C$ es la única decisión libre al integrar.

> [!tip] 🔧 Funciones definidas por integrales
>
> Las funciones $F(x) = \int_a^x f(t)\,dt$ con $f$ continua cumplen:
>
> 1. **Continuidad:** $F$ es continua en $[a,b]$.
> 2. **Diferenciabilidad:** $F'(x) = f(x)$.
> 3. **Condición inicial:** $F(a) = 0$ (la integral de un intervalo vacío es cero).
>
> **Por qué importa:** estas tres condiciones son lo mínimo que se pide en ejercicios de "estudia la función $F(x) = \int_0^x \ldots$": sin ellas no puedes decidir crecimiento ni concavidad de $F$.

---

## 🌐 Aplicaciones

> [!example] 🏔️ Cálculo de áreas
>
> El área entre $f$ y el eje $x$ en $[a,b]$ es
>
> $$\text{Área} = \int_a^b \big|f(x)\big|\,dx.$$
>
> **Por qué importa:** el valor absoluto es necesario cuando la función cruza el eje: sin él obtienes el área neta (con cancelaciones), no el área total.

> [!example] 🚀 Cinemática
>
> - Velocidad: $v(t) = \dfrac{ds}{dt}$, luego $s(t) = \displaystyle\int v(t)\,dt$.
> - Aceleración: $a(t) = \dfrac{dv}{dt}$, luego $v(t) = \displaystyle\int a(t)\,dt$.
> - Desplazamiento: $\displaystyle\int_{t_1}^{t_2} v(t)\,dt = s(t_2) - s(t_1)$.
>
> **Por qué importa:** es la misma relación del TFC leída en física: derivar pasa de posición a velocidad a aceleración, integrar hace el viaje de vuelta.

> [!example] ⚡ Trabajo con fuerza variable
>
> Si la fuerza varía según $F(x)$, el trabajo desde $x = a$ hasta $x = b$ es
>
> $$W = \int_a^b F(x)\,dx.$$
>
> **Por qué importa:** es la aplicación directa de la regla de Barrow a un problema físico: fuerza constante es el caso particular, y con fuerza variable hace falta integrar.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco errores que más se repiten
>
> 1. **Confundir las dos partes:** la Parte I deriva una integral, la Parte II evalúa una integral.
> 2. **Olvidar la variable de integración:** en $\int_a^x f(t)\,dt$ la variable es $t$, no $x$; la $x$ solo aparece en el límite.
> 3. **Mal manejo de límites variables:** aplicar mal la regla de la cadena o invertir el signo del límite inferior.
> 4. **Antiderivada incorrecta:** verificar siempre que $F'(x) = f(x)$ antes de sustituir.
> 5. **Signo en la evaluación:** es $F(b) - F(a)$, no $F(a) - F(b)$.
>
> **Por qué importa:** los cinco son de planteamiento. La comprobación más rápida es derivar el resultado: si no recupera la función integrada, el error está en la antiderivada.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\int_0^2 (3x^2 + 4)\,dx$ con la regla de Barrow.
>
> > [!success]- ✅ Solución
> >
> > Antiderivada: $F(x) = x^3 + 4x$; verificación: $F'(x) = 3x^2 + 4$ ✓
> >
> > Evaluación: $F(2) = 8 + 8 = 16$ y $F(0) = 0$.
> >
> > Resta: $16 - 0 = 16$.
> >
> > **Respuesta:** $16$.

> [!example] 📋 Planteamiento
>
> Deriva $G(x) = \displaystyle\int_1^x \sqrt{t^2 + 1}\,dt$ sin calcular la integral.
>
> > [!success]- ✅ Solución
> >
> > Se aplica la **Parte I** del teorema: la variable $x$ aparece solo en el límite superior, y el integrando es continuo.
> >
> > $$G'(x) = \sqrt{x^2 + 1}.$$
> >
> > **Respuesta:** $G'(x) = \sqrt{x^2+1}$; además $G(1) = 0$ por la condición inicial.

> [!example] 📋 Planteamiento
>
> Halla $\frac{d}{dx}\displaystyle\int_{2x}^{x^3} \operatorname{sen}(t)\,dt$.
>
> > [!success]- ✅ Solución
> >
> > Con $h(x) = x^3$, $h'(x) = 3x^2$, $g(x) = 2x$, $g'(x) = 2$ y $f(t) = \operatorname{sen}(t)$:
> >
> > $$\frac{d}{dx}\int_{2x}^{x^3} \operatorname{sen}(t)\,dt = \operatorname{sen}(x^3)\cdot 3x^2 - \operatorname{sen}(2x)\cdot 2.$$
> >
> > **Respuesta:** $3x^2\operatorname{sen}(x^3) - 2\operatorname{sen}(2x)$.
> >
> > El signo negativo del segundo término es el que recuerda el límite inferior.

> [!example] 📋 Planteamiento
>
> Usa el teorema del valor medio para integrales en $\int_0^4 x\,dx$ y determina $c$.
>
> > [!success]- ✅ Solución
> >
> > La integral vale $\big[\tfrac{x^2}{2}\big]_0^4 = 8$.
> >
> > Por el corolario, existe $c \in [0,4]$ con $f(c)(4 - 0) = 8$, donde $f(x) = x$:
> >
> > $$4c = 8 \quad \Longrightarrow \quad c = 2.$$
> >
> > **Respuesta:** $c = 2$, el punto medio del intervalo (como predice el teorema para funciones lineales).

> [!example] 📋 Planteamiento
>
> Un móvil tiene velocidad $v(t) = 3t^2 - 2t$ m/s. Calcula el desplazamiento entre $t = 0$ y $t = 3$ s.
>
> > [!success]- ✅ Solución
> >
> > El desplazamiento es la integral de la velocidad:
> >
> > $$\int_0^3 (3t^2 - 2t)\,dt = \big[t^3 - t^2\big]_0^3 = (27 - 9) - 0 = 18 \text{ m}.$$
> >
> > **Respuesta:** $18$ m.
> >
> > Verificación: la posición es $s(t) = t^3 - t^2$, con $s(3) - s(0) = 18$ ✓

> [!example] 📋 Planteamiento
>
> Comprueba que $F(x) = \frac{x^4}{4} + C$ es primitiva de $x^3$ y calcula $\int_{-1}^{2} x^3\,dx$.
>
> > [!success]- ✅ Solución
> >
> > Derivando: $F'(x) = \frac{4x^3}{4} = x^3$ ✓, así que $F$ es primitiva para cualquier $C$.
> >
> > Evaluación: $F(2) = \frac{16}{4} = 4$ y $F(-1) = \frac{1}{4}$.
> >
> > Resta: $4 - \frac{1}{4} = \frac{15}{4}$.
> >
> > **Respuesta:** $\frac{15}{4}$. Fíjate en que la $C$ se cancela sola: $(F(b)+C) - (F(a)+C) = F(b) - F(a)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Enuncio las dos partes del teorema fundamental y distingo para qué sirve cada una.
> - [ ] Evalúo una integral definida en tres pasos: antiderivada, evaluación y resta.
> - [ ] Distingo la variable de integración de la variable del límite superior.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Derivo funciones con límite superior variable usando la Parte I.
> - [ ] Aplico la fórmula general con ambos límites funcionales y sus derivadas.
> - [ ] Estudio una función definida por integral verificando continuidad, derivada y condición inicial.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Aplico el corolario del valor medio para integrales y localizo el $c$ correspondiente.
> - [ ] Explico la demostración de la Parte I con la noción de área acumulada.
> - [ ] Resuelvo problemas de física (desplazamiento, trabajo) traduciéndolos a integrales y evaluándolos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: el teorema fundamental y sus aplicaciones.
> - R. Larson, *Cálculo* (Cengage), cap. 5: regla de Barrow y corolarios.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 5: área acumulada y derivada.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la definición de límite de sumas que este teorema evita calcular.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — las propiedades algebraicas previas.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — las técnicas para hallar la antiderivada.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice la Parte I del TFC?::Si $F(x) = \int_a^x f(t)\,dt$ con $f$ continua, entonces $F'(x) = f(x)$: la derivada del área acumulada es la función.
> - ¿Qué dice la Parte II (regla de Barrow)?::$\int_a^b f(x)\,dx = F(b) - F(a)$ con $F$ cualquier primitiva de $f$ continua.
> - ¿Cómo derivo una integral con límites que dependen de $x$?::$f(h(x))h'(x) - f(g(x))g'(x)$: arriba con su derivada menos abajo con su derivada.
> - ¿Cuál es la condición inicial de $F(x) = \int_a^x f(t)\,dt$?::$F(a) = 0$: la integral sobre un intervalo sin longitud es cero.
> - ¿Qué establece el valor medio para integrales?::Existe $c \in [a,b]$ con $\int_a^b f(x)\,dx = f(c)(b-a)$ si $f$ es continua.
> - ¿Cómo verifico que una antiderivada es correcta?::Derivándola: $F'(x)$ debe devolver exactamente $f(x)$ antes de sustituir límites.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — el límite de sumas que el TFC reemplaza en la práctica.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — linealidad y aditividad que se usan al evaluar.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — el paso previo obligatorio: hallar $F$.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — cambio de variable y partes para encontrar $F$.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la aplicación geométrica principal.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/01 - Tasas de Cambio|01 - Tasas de Cambio]] — la lectura de $f$ como tasa que integra el TFC.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 6: los dos son regla de Barrow a secas y deben salirte sin dudar.
> - Después salta al 2 y al 3, donde entra la Parte I y los límites variables, que es lo que más se pregunta en parciales.
> - Cuando domines ambos, ataca el 4 (valor medio) y el 5 (física), que son la aplicación conceptual.
> - Cierra con [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|Métodos de Integración Definida]], donde se aprende a hallar la antiderivada que este teorema necesita.

---

**Tags:** #MATG1045 #unidad6 #teorema-fundamental-calculo #regla-barrow #funciones-integrales #valor-medio #limites-variables #aplicaciones-fisica

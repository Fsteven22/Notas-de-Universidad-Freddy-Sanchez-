---
dg-publish: true
tags: [MATG1045, unidad6, integral-de-riemann, matematicas/calculo/integralesb, teoria/riemann, definiciones/fundamentales, limites/infinitos, geometria/areas, analisis/real]
---

# 🎯 Integral de Riemann

> [!info] 💡 **Concepto Central**
>
> La Integral de Riemann es la definición formal del área bajo una curva, construida a partir del límite de sumas de aproximaciones rectangulares cuando el número de subdivisiones tiende al infinito.

## 📏 Partición de un Intervalo

> [!tip] 🔧 **Definición de Partición**
>
> Una **partición** $P$ del intervalo $[a,b]$ es un conjunto finito de puntos:
>
> $$P = \{x_0, x_1, x_2, \ldots, x_n\}$$
>
> donde $a = x_0 < x_1 < x_2 < \cdots < x_n = b$

### 🎯 Tipos de Particiones

#### 📐 Partición Regular
> [!info] 💡 Partición regular
>
> Todos los subintervalos tienen la misma longitud:
> $$\Delta x = \frac{b-a}{n} \quad \text{y} \quad x_i = a + i \cdot \Delta x$$

#### 📊 Partición Irregular  
> [!info] 💡 Partición irregular
>
> Los subintervalos pueden tener diferentes longitudes:
> $$\Delta x_i = x_i - x_{i-1} \quad \text{(puede variar para cada } i\text{)}$$

### 🔄 Refinamiento de Particiones
> [!info] 📈 **Refinamiento**
>
> Una partición $P'$ es un **refinamiento** de $P$ si $P \subseteq P'$ (contiene todos los puntos de $P$ y posiblemente más).

> [!info] 🖼️ Refinamiento de Particiones
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_01.svg]]
>
> **Se lee así:** así: como una cadena de cuatro rectángulos que avanza hacia la derecha. Una partición inicial da paso a la acción de agregar puntos de corte, y ese paso produce una partición refinada que, a su vez, desemboca en una mejor aproximación del área. No hay rombos ni ramas: es una secuencia lineal de pasos.
>
> **Por qué importa:** Fíjate en que este esquema fija qué significa *refinamiento*: no se cambian los puntos antiguos, se añaden más. Te evita el error de creer que al hacer una partición más fina se redefine la anterior, y te prepara para entender por qué el límite de la integral se toma con $\|P\| \to 0$.
>
> **Ejemplo:** En la nota, la partición regular $P = \{0, 0.5, 1, 1.5, 2\}$ de $f(x) = x^2$ en $[0,2]$ se refina con $n = 8$, donde $\|P\| = 0.25$ y la suma por la derecha mejora de $3.75$ a $3.21$.

## 📊 Norma de una Partición

> [!warning] 🎯 **Definición Crucial**
>
> La **norma** (o **malla**) de una partición $P$ se define como:
>
> $$\|P\| = \max_{1 \leq i \leq n} \Delta x_i = \max_{1 \leq i \leq n} (x_i - x_{i-1})$$
>
> Es decir, la longitud del subintervalo más largo.

### ⚡ Importancia de la Norma

> [!info] 🔍 **¿Por qué es importante?**
>
> - **Control de precisión**: A menor norma, mejor aproximación
> - **Condición de límite**: Para que exista la integral, necesitamos $\|P\| \to 0$
> - **Independencia de $n$**: No basta con $n \to \infty$, debe cumplirse $\|P\| \to 0$

> [!info] 🖼️ Importancia de la Norma
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_02.svg]]
>
> **Se lee así:** así: como dos ramas paralelas que comparan una norma grande con una norma pequeña. La rama de la norma grande conduce a subintervalos anchos y termina en una aproximación burda, mientras la rama de la norma pequeña pasa por subintervalos finos, luego por una aproximación precisa, y continúa hasta el límite $\|P\| \to 0$ y la integral exacta.
>
> **Por qué importa:** Fíjate en que el diagrama separa dos caminos que a primera vista parecen el mismo: *muchos subintervalos* no es lo mismo que *subintervalos finos*. Te evita el error de pensar que basta con $n \to \infty$, porque lo que controla la precisión es que $\|P\| \to 0$.
>
> **Ejemplo:** Un error típico es aproximar $\int_0^2 x^2 dx$ con $n = 1000$ subintervalos desiguales: la suma sigue lejos de $\frac{8}{3}$ si el subintervalo más largo no se encoge.

## 🧮 Notación Sigma y Suma de Riemann

### 📐 Definición de Suma de Riemann

> [!tip] 🎯 **Notación Sigma Completa**
>
> Dada una función $f(x)$ en $[a,b]$ y una partición $P$, la **Suma de Riemann** es:
>
> $$S(f,P) = \sum_{i=1}^{n} f(x_i^*) \Delta x_i$$
>
> donde:
> - $\sum_{i=1}^{n}$ indica sumar desde $i=1$ hasta $i=n$
> - $f(x_i^*)$ es el valor de la función en un punto $x_i^* \in [x_{i-1}, x_i]$
> - $\Delta x_i = x_i - x_{i-1}$ es el ancho del $i$-ésimo subintervalo

### 🎨 Variantes de la Suma según el Punto de Muestra

#### 📍 Suma por la Izquierda
> [!note] 📝 Variantes de la Suma según el Punto de Muestra
>
> $$L_n = \sum_{i=1}^{n} f(x_{i-1}) \Delta x_i$$
> [!note] 📍 Punto de muestra — suma por la izquierda
>
> Punto de muestra: $x_i^* = x_{i-1}$

#### 📍 Suma por la Derecha
> [!note] 📝 Variantes de la Suma según el Punto de Muestra
>
> $$R_n = \sum_{i=1}^{n} f(x_i) \Delta x_i$$
> [!note] 📍 Punto de muestra — suma por la derecha
>
> Punto de muestra: $x_i^* = x_i$

#### 📍 Suma del Punto Medio
> [!note] 📝 Variantes de la Suma según el Punto de Muestra
>
> $$M_n = \sum_{i=1}^{n} f\left(\frac{x_{i-1} + x_i}{2}\right) \Delta x_i$$
> [!note] 📍 Punto de muestra — suma del punto medio
>
> Punto de muestra: $x_i^* = \frac{x_{i-1} + x_i}{2}$

### 🔢 Caso Especial: Partición Regular

> [!info] 🧮 Caso especial: partición regular
>
> Para partición regular con $\Delta x = \frac{b-a}{n}$:

> [!info] ⚡ **Fórmulas Simplificadas**
>
> - **Izquierda**: $L_n = \frac{b-a}{n} \sum_{i=0}^{n-1} f\left(a + i \cdot \frac{b-a}{n}\right)$
> - **Derecha**: $R_n = \frac{b-a}{n} \sum_{i=1}^{n} f\left(a + i \cdot \frac{b-a}{n}\right)$
> - **Punto Medio**: $M_n = \frac{b-a}{n} \sum_{i=1}^{n} f\left(a + \left(i-\frac{1}{2}\right) \cdot \frac{b-a}{n}\right)$

## 🎯 Definición Formal de la Integral de Riemann

> [!warning] 🏆 **Definición Fundamental**
>
> Una función $f$ es **Riemann integrable** en $[a,b]$ si existe un número $I$ tal que para cualquier $\varepsilon > 0$, existe $\delta > 0$ donde:
>
> $$\text{Si } \|P\| < \delta \text{, entonces } \left|\sum_{i=1}^{n} f(x_i^*) \Delta x_i - I\right| < \varepsilon$$
>
> En este caso, escribimos:
> $$\int_a^b f(x) dx = I = \lim_{\|P\| \to 0} \sum_{i=1}^{n} f(x_i^*) \Delta x_i$$

### 🔍 Interpretación del Límite

> [!info] 🖼️ Interpretación del Límite
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_03.svg]]
>
> **Se lee así:** así: como un diagrama con un rombo de decisión en el centro. Una partición de norma pequeña alimenta el cálculo de la suma de Riemann, y el rombo pregunta si la norma ya tiende a cero: si la respuesta es sí, las sumas convergen al valor $I$ y ese número queda identificado como la integral de Riemann; si es no, la flecha devuelve el proceso a refinar la partición y volver a empezar.
>
> **Por qué importa:** Fíjate en que el rombo convierte la definición en un **ciclo de refinamiento**: la integral no se obtiene en un solo intento, sino en la familia de sumas que se estabiliza al hacer $\|P\| \to 0$. Te evita tratar la suma de Riemann como un resultado único y definitivo.
>
> **Ejemplo:** En la nota, con $f(x) = x^2$ en $[0,2]$ se pasa de $R_4 = 3.75$ a $R_8 = 3.21$, $R_{16} = 2.94$ y $R_{32} = 2.80$, acercándose siempre a $\frac{8}{3}$.

## 🧪 Ejemplo Detallado

> [!tip] 🔬 **Ejemplo: $f(x) = x^2$ en $[0,2]$**
>
> **Paso 1: Partición regular con $n=4$**
> $$\Delta x = \frac{2-0}{4} = 0.5$$
> $$P = \{0, 0.5, 1, 1.5, 2\}$$
> $$\|P\| = 0.5$$
>
> **Paso 2: Suma por la derecha**
> $$R_4 = \sum_{i=1}^{4} f(x_i) \Delta x_i = \sum_{i=1}^{4} f(i \cdot 0.5) \cdot 0.5$$
> $$= 0.5[f(0.5) + f(1) + f(1.5) + f(2)]$$
> $$= 0.5[(0.5)^2 + 1^2 + (1.5)^2 + 2^2]$$
> $$= 0.5[0.25 + 1 + 2.25 + 4] = 0.5 \times 7.5 = 3.75$$
>
> **Paso 3: Comparación con valor exacto**
> $$\int_0^2 x^2 dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} \approx 2.667$$
>
> **Error**: $|3.75 - 2.667| = 1.083$
>
> ### 📈 Mejorando la Aproximación
>
> | $n$ | $\|P\|$ | $R_n$ | Error |
> |-----|---------|-------|-------|
> | 4   | 0.5     | 3.75  | 1.083 |
> | 8   | 0.25    | 3.21  | 0.543 |
> | 16  | 0.125   | 2.94  | 0.273 |
> | 32  | 0.0625  | 2.80  | 0.133 |
>
> >[!info] 📊 **Observación**: Conforme $\|P\| \to 0$, la suma converge a $\frac{8}{3}$

## ⚡ Condiciones de Integrabilidad

> [!warning] 🔍 **Teoremas Fundamentales**
>
> ### 🎯 Teorema 1: Funciones Continuas
> Si $f$ es continua en $[a,b]$, entonces $f$ es Riemann integrable en $[a,b]$.
>
> ### 🎯 Teorema 2: Funciones Monótonas  
> Si $f$ es monótona en $[a,b]$, entonces $f$ es Riemann integrable en $[a,b]$.
>
> ### 🎯 Teorema 3: Discontinuidades Finitas
> Si $f$ es acotada en $[a,b]$ y tiene un número finito de discontinuidades, entonces $f$ es Riemann integrable en $[a,b]$.
>
> [!info] 🖼️ Condiciones de Integrabilidad
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_04.svg]]
>
> **Se lee así:** así: como una escalera de decisiones. Partiendo de una función definida en un intervalo cerrado, el primer rombo pregunta si es continua; si lo es, se llega al rectángulo de integrabilidad, y si no, la flecha baja a un segundo rombo sobre la monotonía. Desde ahí se pasa a un tercer rombo que combina acotación y número finito de discontinuidades, y la última salida advierte que la función puede no ser integrable.
>
> **Por qué importa:** Fíjate en que el diagrama te da una **estrategia de verificación** antes de calcular: primero continuidad, luego monotonía, y por último acotación con discontinuidades finitas. Te evita Attempting积分 una función que no cumple ninguna condición y perder tiempo en sumas que no convergen.
>
> **Ejemplo:** La función $f(x) = x$ en $[0,1]$ es continua, así que el primer rombo ya responde sí y queda garantizada la integral $\int_0^1 x dx = \frac{1}{2}$.

## 🛠️ Propiedades Fundamentales

> [!info] 📋 **Propiedades Algebraicas**
>
> ### 🔢 Linealidad
> $$\int_a^b [c_1f(x) + c_2g(x)] dx = c_1\int_a^b f(x) dx + c_2\int_a^b g(x) dx$$
>
> ### 🔄 Aditividad en el Dominio
> Si $a < c < b$:
> $$\int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx$$
>
> ### 📊 Comparación
> Si $f(x) \leq g(x)$ en $[a,b]$:
> $$\int_a^b f(x) dx \leq \int_a^b g(x) dx$$
>
## ⚠️ Errores Comunes y Conceptos Clave

> [!warning] 🚨 **Errores Frecuentes**
>
> 1. **Confundir $n \to \infty$ con $\|P\| \to 0$**: No es lo mismo
> 2. **Olvidar el $\Delta x_i$**: Siempre multiplicar por el ancho
> 3. **Índices incorrectos**: En suma izquierda usar $f(x_{i-1})$
> 4. **Ignorar discontinuidades**: Verificar integrabilidad primero
> 5. **Signos**: Si $f(x) < 0$, la integral es negativa

## 🌐 Interpretación Geométrica

> [!tip] 🏔️ **Significado Visual**
>
> - **Área positiva**: Cuando $f(x) \geq 0$, la integral representa el área bajo la curva
> - **Área con signo**: Cuando $f(x)$ cambia de signo, se obtiene el área neta
> - **Aproximación**: Los rectángulos aproximan cada vez mejor la región curva

> [!info] 🖼️ Interpretación Geométrica
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integral_de_Riemann_05.svg]]
>
> **Se lee así:** así: como un proceso de construcción con una bifurcación. Desde la función se divide el intervalo en subintervalos y se crean rectángulos; de cada rectángulo salen dos rutas, la altura y la base, que vuelven a juntarse en el área de un rectángulo. Después las áreas se suman, se toma el límite cuando la norma tiende a cero y se llega al área exacta.
>
> **Por qué importa:** Fíjate en que el esquema muestra el **puente entre la fórmula y el dibujo**: la integral es una suma de áreas que se hace cada vez más fina. Te sirve para entender por qué, si $f$ cambia de signo, obtienes un área neta y no un área positiva.
>
> **Ejemplo:** Para $f(x) = x - 1$ en $[0,2]$, los rectángulos sobre $[0,1]$ restan y los de $[1,2]$ suman, y el área neta da $\int_0^2 (x-1) dx = 0$.

---

>[!quote] ## 📚 Referencias y Conexiones
>
> ### 🔗 Notas Relacionadas
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo.md|04 - Teorema Fundamental del Cálculo.md]] - Conexión integral-derivada
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva.md|01 - Área bajo la Curva.md]] - Interpretación geométrica
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral.md|02 - Propiedades de la Integral.md]] - Operaciones con integrales
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida.md|01 - Métodos de Integración Definida.md]] - Técnicas de cálculo
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias.md|01 - Integrales Impropias.md]] - Extensión del concepto
>
> ### 📖 Para Profundizar
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración.md|03 - Constante de integración.md]] - Desarrollo histórico del concepto
> - Integral de Lebesgue - Generalización moderna
> - Métodos Numéricos de Integración - Aplicaciones computacionales
>

## 📚 Referencias

> [!quote] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo.md]]
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva.md]]
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral.md]]
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida.md]]
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias.md]]
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración.md]]

**Tags:** #MATG1045 #unidad6 #integral-de-riemann #matematicas/calculo/integralesb #teoria/riemann #definiciones/fundamentales #limites/infinitos #geometria/areas #analisis/real

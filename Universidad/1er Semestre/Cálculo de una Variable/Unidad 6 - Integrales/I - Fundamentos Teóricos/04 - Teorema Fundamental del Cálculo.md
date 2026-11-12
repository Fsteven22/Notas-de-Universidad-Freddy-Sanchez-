---
dg-publish: true
tags: [MATG1045, unidad6, teorema-fundamental-del-calculo, fundamental/conexiones, derivadas/integrales, aplicaciones/fisica, historia/matematicas, evaluacion/integrales]
---

# ⚡ Teorema Fundamental del Cálculo

> [!info] 💡 **El Puente Conceptual**
>
> El Teorema Fundamental del Cálculo establece la conexión profunda entre derivación e integración, demostrando que son operaciones inversas y proporcionando una herramienta poderosa para evaluar integrales definidas.

## 🎯 Primera Parte del Teorema Fundamental

> [!tip] 🏆 **Teorema Fundamental del Cálculo - Parte I**
>
> Si $f$ es continua en $[a,b]$ y definimos:
>
> $$F(x) = \int_a^x f(t) dt$$
>
> entonces $F$ es diferenciable en $(a,b)$ y:
>
> $$F'(x) = f(x)$$
>
> Es decir: $\frac{d}{dx}\left[\int_a^x f(t) dt\right] = f(x)$

### 🔍 Interpretación Geométrica

> [!info] 📊 **Significado Visual**
>
> - $F(x)$ representa el **área acumulada** desde $a$ hasta $x$
> - $F'(x) = f(x)$ significa que la **tasa de cambio** del área acumulada es igual al **valor de la función** en ese punto
> - La "altura" de la función determina qué tan rápido crece el área

> [!info] 🖼️ Interpretación Geométrica
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Teorema_Fundamental_del_Cálculo_01.svg]]
>
> **Se lee así:** así: como una cadena que arranca con la condición de continuidad y desemboca en dos lecturas finales. Tras enunciar la primera parte del teorema, el diagrama define $F(x)$, recuerda que esa función es diferenciable y de ahí sale la igualdad clave $F'(x) = f(x)$, que luego se traduce en la lectura del área acumulada y en la idea de que su tasa de cambio es la altura de la función.
>
> **Por qué importa:** Fíjate en que el diagrama te da la demostración esquemática en tres movimientos, así entiendes por qué la hipótesis de continuidad es indispensable. Te evita el error de derivar una integral con límites variables sin aplicar la regla de la cadena.
>
> **Ejemplo:** Para derivar $\frac{d}{dx}\left[\int_2^x t^3 dt\right]$ la primera parte da directamente $x^3$, y el esquema te recuerda que la variable de integración es $t$, no $x$.

### 🧮 Demostración (Esquema)

> [!warning] 🔬 **Idea de la Demostración**
>
> **Paso 1**: Usar definición de derivada
> $$F'(x) = \lim_{h \to 0} \frac{F(x+h) - F(x)}{h}$$
>
> **Paso 2**: Expresar con integrales
> $$F'(x) = \lim_{h \to 0} \frac{\int_a^{x+h} f(t)dt - \int_a^x f(t)dt}{h}$$
>
> **Paso 3**: Usar aditividad de la integral
> $$F'(x) = \lim_{h \to 0} \frac{\int_x^{x+h} f(t)dt}{h}$$
>
> **Paso 4**: Aplicar Teorema del Valor Medio para integrales
> $$F'(x) = \lim_{h \to 0} \frac{f(c) \cdot h}{h} = \lim_{h \to 0} f(c) = f(x)$$

## 🎯 Segunda Parte del Teorema Fundamental

> [!tip] 🏆 **Teorema Fundamental del Cálculo - Parte II**
>
> Si $f$ es continua en $[a,b]$ y $F$ es cualquier antiderivada de $f$ (es decir, $F'(x) = f(x)$), entonces:
>
> $$\int_a^b f(x) dx = F(b) - F(a)$$
>
> **Notación**: $\int_a^b f(x) dx = [F(x)]_a^b = F(b) - F(a)$

### 🔧 Metodología de Evaluación

> [!info] 📋 **Proceso de Evaluación**
>
> **Paso 1**: Encontrar una antiderivada $F(x)$ de $f(x)$
>
> **Paso 2**: Evaluar $F$ en los límites de integración
>
> **Paso 3**: Calcular $F(b) - F(a)$

> [!info] 🖼️ Metodología de Evaluación
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Teorema_Fundamental_del_Cálculo_02.svg]]
>
> **Se lee así:** así: como un recorrido de seis pasos encadenados. Desde la hipótesis de continuidad se enuncia la segunda parte, y luego el diagrama desglosa el método en tres pasos numerados, cierra con la notación entre corchetes y termina en una caja de verificación que propone derivar el resultado para comprobarlo.
>
> **Por qué importa:** Fíjate en que la última caja es un **control de calidad**: derivar la antiderivada para verificar. Te evita el error de invertir la resta, escribir $F(a) - F(b)$ y obtener un número con el signo cambiado sin darte cuenta.
>
> **Ejemplo:** Para $\int_1^4 2x dx$ se toma $F(x) = x^2$ y se obtiene $F(4) - F(1) = 16 - 1 = 15$, que coincide con el área del trapecio de la nota.

## 🧪 Ejemplos Detallados

### 🔬 Ejemplo 1: Aplicación Directa

> [!tip] 📈 **Evaluar**: $\int_1^4 2x dx$
>
> **Paso 1**: Encontrar antiderivada
> $F(x) = x^2$ (ya que $\frac{d}{dx}[x^2] = 2x$)
>
> **Paso 2**: Aplicar el teorema
> $$\int_1^4 2x dx = [x^2]_1^4 = 4^2 - 1^2 = 16 - 1 = 15$$
>
> **Verificación**: El área del trapecio de altura $2$ a $8$ y base $3$ es $\frac{(2+8) \cdot 3}{2} = 15$ ✓

### 🔬 Ejemplo 2: Con Funciones Trigonométricas

> [!tip] 📐 **Evaluar**: $\int_0^{\pi/2} \cos(x) dx$
>
> **Paso 1**: Antiderivada de $\cos(x)$ es $\sin(x)$
>
> **Paso 2**: Aplicar el teorema
> $$\int_0^{\pi/2} \cos(x) dx = [\sin(x)]_0^{\pi/2} = \sin(\pi/2) - \sin(0) = 1 - 0 = 1$$

### 🔬 Ejemplo 3: Primera Parte del Teorema

> [!tip] 🧮 **Derivar**: $\frac{d}{dx}\left[\int_2^x t^3 dt\right]$
>
> **Aplicando la Primera Parte directamente**:
> $$\frac{d}{dx}\left[\int_2^x t^3 dt\right] = x^3$$
>
> **Verificación por Segunda Parte**:
> $\int_2^x t^3 dt = \left[\frac{t^4}{4}\right]_2^x = \frac{x^4}{4} - \frac{16}{4} = \frac{x^4 - 16}{4}$
>
> $\frac{d}{dx}\left[\frac{x^4 - 16}{4}\right] = \frac{4x^3}{4} = x^3$ ✓

## 🌐 Casos Especiales y Variaciones

### 🔄 Límites Variables

> [!warning] 🎯 **Caso General**: $\frac{d}{dx}\left[\int_{g(x)}^{h(x)} f(t) dt\right]$
>
> **Regla de la Cadena aplicada**:
> $$\frac{d}{dx}\left[\int_{g(x)}^{h(x)} f(t) dt\right] = f(h(x)) \cdot h'(x) - f(g(x)) \cdot g'(x)$$

#### 📊 Ejemplos de Límites Variables

> [!info] 🔬 **Ejemplo**: $\frac{d}{dx}\left[\int_{x^2}^{x^3} \sin(t) dt\right]$
>
> Aplicando la fórmula:
> - $h(x) = x^3$, $h'(x) = 3x^2$
> - $g(x) = x^2$, $g'(x) = 2x$
> - $f(t) = \sin(t)$
>
> $$\frac{d}{dx}\left[\int_{x^2}^{x^3} \sin(t) dt\right] = \sin(x^3) \cdot 3x^2 - \sin(x^2) \cdot 2x$$

### 🔀 Funciones Definidas por Integrales

> [!tip] 📈 **Funciones Integrales**
>
> Las funciones de la forma $F(x) = \int_a^x f(t) dt$ tienen propiedades especiales:
>
> 1. **Continuidad**: Si $f$ es continua, entonces $F$ es continua
> 2. **Diferenciabilidad**: $F'(x) = f(x)$
> 3. **Condición inicial**: $F(a) = 0$

## 🛠️ Propiedades y Corolarios

### 📋 Propiedades Fundamentales

> [!info] 🔧 **Propiedades Derivadas**
>
> #### 🎯 Corolario 1: Valor Medio para Integrales
> Si $f$ es continua en $[a,b]$, existe $c \in [a,b]$ tal que:
> $$\int_a^b f(x) dx = f(c)(b-a)$$
>
> #### 🎯 Corolario 2: Caracterización de Antiderivadas
> Si $F'(x) = G'(x) = f(x)$ en un intervalo, entonces $F(x) = G(x) + C$ para alguna constante $C$.
>
> [!info] 🖼️ Propiedades Fundamentales
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Teorema_Fundamental_del_Cálculo_03.svg]]
>
> **Se lee así:** así: como una caja central de la que salen cuatro ramas paralelas. Tres ramas enumeran propiedades de la función acumulada: que es continua, que es diferenciable con derivada igual a $f$, y que vale cero en el extremo inicial. La cuarta y la quinta caja, más anchas, contienen los dos corolarios del teorema.
>
> **Por qué importa:** Fíjate en que el diagrama reúne en un solo lugar las **propiedades de la función acumulada** y los dos corolarios más usados del TFC. Te evita confundir el valor medio para integrales con el teorema del valor medio y aplicarlos donde no toca.
>
> **Ejemplo:** Para $\int_0^\pi \sin(x) dx$, el corolario 1 garantiza que existe $c$ con $\int_0^\pi \sin(x) dx = \sin(c) \pi$, y el corolario 2 explica por qué $G(x) = F(x) + C$.

## 🎨 Aplicaciones Importantes

### 🏔️ Cálculo de Áreas

> [!tip] 📊 **Área bajo curvas**
>
> El área entre $f(x)$ y el eje $x$ desde $x = a$ hasta $x = b$:
> $$\text{Área} = \int_a^b |f(x)| dx$$

### ⚡ Física y Movimiento

> [!info] 🚀 **Cinemática**
>
> - **Velocidad**: $v(t) = \frac{ds}{dt}$ ⟹ $s(t) = \int v(t) dt$
> - **Aceleración**: $a(t) = \frac{dv}{dt}$ ⟹ $v(t) = \int a(t) dt$
>
> **Desplazamiento total**: $\int_{t_1}^{t_2} v(t) dt = s(t_2) - s(t_1)$

### 🔋 Trabajo y Energía

> [!tip] ⚡ **Trabajo con fuerza variable**
>
> Si la fuerza varía según $F(x)$, el trabajo desde $x = a$ hasta $x = b$:
> $$W = \int_a^b F(x) dx$$

## ⚠️ Errores Comunes y Precauciones

> [!warning] 🚨 **Errores Frecuentes**
>
> 1. **Confundir las dos partes**: La Parte I da la derivada de una integral, la Parte II evalúa integrales
>
> 2. **Olvidar la variable de integración**: En $\int_a^x f(t) dt$, la variable es $t$, no $x$
>
> 3. **Límites variables mal manejados**: Aplicar incorrectamente la regla de la cadena
>
> 4. **Antiderivadas incorrectas**: Verificar siempre que $F'(x) = f(x)$
>
> 5. **Signos en la evaluación**: Recordar que es $F(b) - F(a)$, no $F(a) - F(b)$

### 🔍 Verificaciones Útiles

> [!info] ✅ **Cómo verificar resultados**
>
> - **Derivar el resultado**: Si evaluaste $\int_a^b f(x)dx$, verifica derivando
> - **Casos especiales**: Probar con funciones simples conocidas
> - **Continuidad**: El resultado debe ser continuo respecto a los límites

## 🌟 Importancia Histórica y Conceptual

> [!tip] 📜 **Contexto Histórico**
>
> - **Newton y Leibniz** (siglo XVII): Desarrollaron independientemente el cálculo
> - **Conexión fundamental**: Unificó dos problemas aparentemente distintos:
>   - **Problema de tangentes** (derivadas)
>   - **Problema de cuadraturas** (áreas/integrales)

### 🧠 Impacto Conceptual

> [!info] 🖼️ Impacto Conceptual
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Teorema_Fundamental_del_Cálculo_04.svg]]
>
> **Se lee así:** así: como un árbol histórico. Del nodo de importancia se abren dos ramas, el problema de las tangentes y el problema de las cuadraturas, y ambas confluyen en la caja de unificación. De esa unificación salen dos salidas finales: la comprobación del resultado derivando y el requisito de que el resultado varíe continuamente con los límites.
>
> **Por qué importa:** Fíjate en que el diagrama cuenta **por qué** el TFC importó: unificó dos problemas que antes se trataban por separado. Te da la motivación histórica y también el control de calidad de derivar tu resultado para verificarlo.
>
> **Ejemplo:** El caso de la nota donde $\int_2^x t^3 dt = \frac{x^4 - 16}{4}$ se usa para mostrar que, derivando, se recupera la función original.

---

>[!quote] ## 📚 Referencias y Conexiones
>
> ### 🔗 Notas Relacionadas
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann.md|01 - Integral de Riemann.md]] - Definición formal de la integral definida
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral.md|02 - Propiedades de la Integral.md]] - Herramientas para manipular integrales
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida.md|01 - Métodos de Integración Definida.md]] - Técnicas para encontrar antiderivadas
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva.md|01 - Área bajo la Curva.md]] - Aplicación geométrica principal
> - Ecuaciones Diferenciales - Aplicación del teorema para resolver EDOs
>
> ### 📖 Para Profundizar
> - Teorema del Valor Medio - Base teórica de la demostración
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo.md#Funciones Definidas por Integrales|Funciones Definidas por Integrales]] - Estudio detallado de funciones integrales
> - Historia del Cálculo - Desarrollo histórico del teorema
> - [[Cálculo de una Variable.md|Cálculo de una Variable.md]] - Generalización avanzada
>
> ### 🎯 Aplicaciones Especializadas
> - Trabajo y Energía con Integrales - Aplicaciones en física
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución.md|01 - Volúmenes de Sólidos de Revolución.md]] - Aplicaciones geométricas
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas.md#Longitud de Arco|Longitud de Arco]] - Más aplicaciones geométricas
>

## 📚 Referencias

> [!quote] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann.md]]
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral.md]]
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida.md]]
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva.md]]
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo.md#Funciones Definidas por Integrales]]
> - [[Cálculo de una Variable.md]]
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución.md]]
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas.md#Longitud de Arco]]

**Tags:** #MATG1045 #unidad6 #teorema-fundamental-del-calculo #fundamental/conexiones #derivadas/integrales #aplicaciones/fisica #historia/matematicas #evaluacion/integrales

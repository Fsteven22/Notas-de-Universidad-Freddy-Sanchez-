---
dg-publish: true
tags: [MATG1045, unidad5, aproximaciones-lineales-y-diferenciales, calculo, aproximaciones, diferenciales, errores, mediciones, derivadas, matematicas, fisica-experimental, analisis-numerico]
---

# 📏 Aproximaciones Lineales y Diferenciales

> [!tip] 🎯 Concepto Central
>
> Las aproximaciones lineales nos permiten **estimar valores** de funciones complicadas usando la **recta tangente** como aproximación local. Es como usar una "lupa matemática" para ver de cerca el comportamiento de una función.

## 🔄 Diferencial de una Función

> [!info] 📐 Definición del Diferencial Para una función $f(x)$ derivable en $x = a$, el **diferencial** se define como:
>
> $$dy = f'(x)dx$$
>
> Donde:
>
> - $dy$ = cambio aproximado en $y$
> - $f'(x)$ = derivada de la función
> - $dx$ = cambio pequeño en $x$
>

> [!example] 🌟 Ejemplo Práctico Para $f(x) = x^2$ en $x = 3$:
>
> - $f'(x) = 2x$, entonces $f'(3) = 6$
> - El diferencial: $dy = 6dx$
> - Si $dx = 0.1$, entonces $dy = 0.6$
>
> **Verificación:**
>
> - Valor real: $f(3.1) = 9.61$, $f(3) = 9$ → $\Delta y = 0.61$
> - Aproximación: $dy = 0.6$ ✨ ¡Muy cercano!

## 🔍 Aproximaciones Locales

> [!tip] 🎯 Fórmula de Aproximación Lineal Para aproximar $f(a + h)$ donde $h$ es pequeño:
>
> $$f(a + h) \approx f(a) + f'(a) \cdot h$$
>
> Esta es la **ecuación de la recta tangente** en el punto $(a, f(a))$.

> [!info] 🖼️ Aproximaciones Locales
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Aproximaciones_Lineales_y_Diferenciales_01.svg]]
>
> **Se lee así:** El diagrama es una **cadena corta de cuatro rectángulos** con flechas que van hacia abajo: se parte de la función original, se marca el punto donde se va a trabajar, se traza la recta que toca la curva en ese punto y se llega a la casilla de aproximación local. Cada flecha significa un paso, no una decisión.
>
> **Por qué importa:** Fíjate en que la aproximación no se aplica a la función completa sino a un entorno del punto de tangencia: por eso el diagrama pasa siempre por la recta antes de llegar al resultado. Esto te evita usar $f(a+h) \approx f(a) + f'(a)h$ lejos de $a$, donde el error se dispara.
>
> **Ejemplo:** Para $f(x) = x^2$ en $a = 3$ con $dx = 0.1$, el recorrido da $dy = 6 \cdot 0.1 = 0.6$, frente al valor real $\Delta y = 0.61$, que muestra lo buena que es la aproximación en ese punto.

> [!warning] ⚠️ Limitaciones de la Aproximación
>
> - Solo es **precisa para valores cercanos** al punto de tangencia
> - El error aumenta conforme nos alejamos del punto $a$
> - Para funciones muy curvadas, la aproximación puede ser pobre

## 📊 Propagación de Errores

> [!info] 🔬 Análisis de Errores Cuando medimos magnitudes físicas, siempre hay **incertidumbre**. Si $x$ tiene un error $\Delta x$, entonces el error en $f(x)$ es aproximadamente:
>
> $$\Delta f \approx |f'(x)| \cdot \Delta x$$

### Tabla de Propagación de Errores Comunes

> [!note] 📋 Fórmulas de Propagación
>
> |Función|$f(x)$|Error Propagado $\Delta f$|
> |---|---|---|
> |Potencia|$x^n$|$\|n x^{n-1}\| \Delta x$|
> |Exponencial|$e^x$|$e^x \Delta x$|
> |Logaritmo|$\ln x$|$\frac{\Delta x}{\|x\|}$|
> |Seno|$\sin x$|$\|\cos x\| \Delta x$|
> |Coseno|$\cos x$|$\|\sin x\| \Delta x$|

## 🔬 Aplicaciones en Mediciones

> [!example] 🧪 Ejemplo: Volumen de una Esfera Una esfera tiene radio $r = 5.0 \pm 0.1$ cm. ¿Cuál es el error en el volumen?
>
> **Solución:**
>
> - $V(r) = \frac{4}{3}\pi r^3$
> - $V'(r) = 4\pi r^2$
> - $\Delta V \approx V'(5) \cdot \Delta r = 4\pi(25)(0.1) = 10\pi \approx 31.4 \text{ cm}^3$
>
> Por tanto: $V = 523.6 \pm 31.4 \text{ cm}^3$ 📐

> [!info] 🖼️ Aplicaciones en Mediciones
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Aproximaciones_Lineales_y_Diferenciales_02.svg]]
>
> **Se lee así:** Es una **cadena de cuatro rectángulos** que sigue el recorrido de una medición real: la primera casilla es la medida con su incertidumbre, la segunda indica aplicar el diferencial, la tercera pide derivar la magnitud que se quiere propagar y la cuarta cierra con el resultado numérico acompañado de su margen de error.
>
> **Por qué importa:** Fíjate en que la incertidumbre de la medida entra una sola vez, al principio, y el error final sale amplificado por la derivada. Esto te sirve para los informes de laboratorio: te da una cota realista del volumen y evita que presentes un número sin margen.
>
> **Ejemplo:** Con $r = 5.0 \pm 0.1$ cm en una esfera, la cadena da $V'(r) = 4\pi r^2$, luego $\Delta V \approx 4\pi(25)(0.1) = 10\pi$ y termina en $V = 523.6 \pm 31.4\ \text{cm}^3$.

> [!tip] 🎓 Técnica de Estudio: Mnemotecnia "DALE" Para recordar el proceso de aproximaciones lineales:
>
> - **D**iferencial: $dy = f'(x)dx$
> - **A**proximación: $f(a+h) \approx f(a) + f'(a)h$
> - **L**ineal: Usamos la recta tangente
> - **E**rror: $\Delta f \approx |f'(x)|\Delta x$

## 📚 Referencias

> [!quote] 🔗 Notas Relacionadas
>
> - Derivadas y sus Aplicaciones - Fundamentos necesarios
> - Recta Tangente - Base geométrica de las aproximaciones
> - Análisis de Errores Experimentales - Aplicaciones prácticas
> - Funciones y Continuidad - Conceptos previos importantes

## 💡 Notas Recomendadas

> [!note] 📖 Para Profundizar
>
> - [[04 – Diferenciabilidad#Diferencial Total|Diferencial Total]] - Extensión a funciones de varias variables
> - Series de Taylor - Aproximaciones de orden superior
> - Métodos Numéricos - Implementación computacional
> - Física Experimental - Aplicaciones en laboratorio
> - Estadística de Errores - Análisis más avanzado de incertidumbre

---

**Tags:** #MATG1045 #unidad5 #aproximaciones-lineales-y-diferenciales #calculo #aproximaciones #diferenciales #errores #mediciones #derivadas #matematicas #fisica-experimental #analisis-numerico

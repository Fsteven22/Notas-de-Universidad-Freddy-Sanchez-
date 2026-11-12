---
dg-publish: true
tags: [MATG1045, unidad6, integrales-por-fracciones-parciales, matemáticas, cálculo, integración, fracciones-parciales, funciones-racionales, métodos-integración, álgebra, análisis-matemático, universidad]
---

# 🧮 Integrales por Fracciones Parciales

## 📖 Introducción

> [!info] 💡 Concepto Clave La **integración por fracciones parciales** es una técnica fundamental para resolver integrales de funciones racionales. Consiste en descomponer una fracción compleja en suma de fracciones más simples que podemos integrar fácilmente.
>

> [!tip] 📌 ¿Cuándo usar este método?
>
> - Cuando tenemos una función racional $\frac{P(x)}{Q(x)}$
> - El denominador $Q(x)$ es factorizable
> - Métodos como sustitución o integración por partes no son viables

---

## 🔤 Variables y Notación

> [!note] 📝 Elementos principales
>
> - **$P(x)$**: Polinomio del numerador
> - **$Q(x)$**: Polinomio del denominador
> - **$\frac{P(x)}{Q(x)}$**: Función racional a integrar
> - **$A, B, C, ...$**: Constantes a determinar en la descomposición
>

> [!warning] ⚠️ Tipos de factores en el denominador
>
> - 🔹 **Lineales distintos**: $(ax + b)$
> - ♻️ **Lineales repetidos**: $(ax + b)^n$
> - 🧩 **Cuadráticos irreducibles**: $ax^2 + bx + c$ donde $\Delta < 0$
> - 🔁 **Cuadráticos repetidos**: $(ax^2 + bx + c)^n$

---

## 🛠️ Procedimiento Paso a Paso

> [!tip] 🔎 **Paso 1: Verificación del grado**
>
> **Si** $\text{grado}(P(x)) \geq \text{grado}(Q(x))$: $$\frac{P(x)}{Q(x)} = \text{Cociente}(x) + \frac{\text{Resto}(x)}{Q(x)}$$
>
> **Si** $\text{grado}(P(x)) < \text{grado}(Q(x))$: ✅ Continuar al paso 2
>

> [!tip] 🧱 **Paso 2: Factorización del denominador**
>
> Descomponer $Q(x)$ completamente:
>
> - Encontrar raíces reales → factores lineales
> - Identificar factores cuadráticos irreducibles
> - Determinar multiplicidades
>

> [!tip] 🧮 **Paso 3: Establecer la descomposición**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_por_Fracciones_Parciales_01.svg]]
>
> **Se lee así:** Es una cadena horizontal de rectángulos unidos por flechas rectas, sin rombos ni bifurcaciones: cada caja es un paso y el orden de las flechas impone el orden de trabajo. La cadena arranca en el objetivo general y termina en una caja de cierre que manda comprobar el resultado derivando.
>
> **Por qué importa:** Fíjate en que el diagrama es una lista de control y no una encrucijada: el error típico es saltarse la verificación de grados o la factorización completa. Te sirve como orden de trabajo para no inventarte la descomposición antes de tener el denominador factorizado.
>
> **Ejemplo:** Con $\int \frac{x+5}{x^2+x-2} dx$ de la nota, la cadena te lleva de la verificación de grados a factorizar $(x+2)(x-1)$, declarar las constantes $A$ y $B$, integrar cada parte y cerrar derivando para comprobar.

> [!tip] 🧩 **Paso 4: Resolver para las constantes**
>
> **Método 1 - Sustitución de raíces:**
>
> - Multiplica ambos lados por $Q(x)$
> - Sustituye valores convenientes de $x$ (especialmente raíces)
>
> **Método 2 - Igualación de coeficientes:**
>
> - Expande el lado derecho
> - Iguala coeficientes de potencias semejantes
>

> [!tip] 🧘‍♂️ **Paso 5: Integración**
>
> Integra cada fracción parcial usando fórmulas básicas:
>
> - $\int \frac{1}{u} du = \ln|u| + C$
> - $\int \frac{1}{u^n} du = \frac{-1}{(n-1)u^{n-1}} + C$ (para $n > 1$)
> - $\int \frac{1}{u^2 + a^2} du = \frac{1}{a}\arctan\left(\frac{u}{a}\right) + C$

---

## 📊 Fundamento Teórico

> [!info] 🎓 Base matemática El **Teorema de Descomposición en Fracciones Parciales** establece que toda función racional propia puede expresarse de manera única como suma de fracciones parciales. Este resultado se basa en:
>
> - La factorización única de polinomios sobre $\mathbb{R}[x]$
> - Propiedades algebraicas de los cuerpos
> - Teorema fundamental del álgebra

> [!info] 🖼️ Fundamento Teórico
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_por_Fracciones_Parciales_02.svg]]
>
> **Se lee así:** El diagrama separa dos planos: arriba, una caja central sobre antiderivadas estándar se abre en tres ramas, según el factor que aparezca en el denominador, y cada rama termina en su fórmula; abajo, otra rama lleva a la base teórica, que se abre en tres pilares algebraicos. Todo son rectángulos, sin decisiones, y las flechas van en un solo sentido, de la causa a la consecuencia.
>
> **Por qué importa:** Esta es la tabla que necesitas cuando ya descompusiste la fracción: **cada tipo de factor pide una antiderivada distinta**, y confundirlas es el error típico. Entender los tres pilares te da la garantía de que la descomposición que encontraste es única y no arbitraria.
>
> **Ejemplo:** En $\int \frac{x+5}{x^2 + x - 2} dx$ de la nota, los factores $x+2$ y $x-1$ caen en la rama de lineal simple y cada uno aporta su logaritmo.

---

## 🔗 Conexiones Interdisciplinarias

> [!note] 🧩 **Álgebra y Análisis**
>
> - **Factorización de polinomios**: Base fundamental del método
> - **Sistemas de ecuaciones lineales**: Para resolver constantes
> - **Integración básica**: Aplicación de fórmulas elementales
>

> [!note] 🔬 **Aplicaciones en Ingeniería**
>
> - **Transformada de Laplace**: Inversión de transformadas racionales
> - **Análisis de circuitos**: Funciones de transferencia
> - **Teoría de control**: Análisis de estabilidad

---

## 💡 Ejemplo Detallado

> [!example] 🧪 **Problema**: Calcular $\int \frac{x+5}{x^2 + x - 2} dx$
>

> [!tip] 📝 **Solución paso a paso**
>
> **1. Verificar grado:** ✅ Numerador grado 1 < Denominador grado 2
>
> **2. Factorizar:** $x^2 + x - 2 = (x + 2)(x - 1)$
>
> **3. Descomposición:** $$\frac{x+5}{(x+2)(x-1)} = \frac{A}{x+2} + \frac{B}{x-1}$$
>
> **4. Resolver constantes:** $$x + 5 = A(x - 1) + B(x + 2)$$
>
> - Para $x = 1$: $6 = 3B \Rightarrow B = 2$
> - Para $x = -2$: $3 = -3A \Rightarrow A = -1$
>
> **5. Integrar:** $$\int \left(\frac{-1}{x+2} + \frac{2}{x-1}\right) dx = -\ln|x+2| + 2\ln|x-1| + C$$
>
> **Forma compacta:** $\ln\left|\frac{(x-1)^2}{x+2}\right| + C$
>

> [!success] ✅ **Verificación**
>
> Podemos verificar derivando el resultado para obtener la función original.

---

## 📈 Visualización Gráfica

> [!info] 🖼️ Visualización Gráfica
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_por_Fracciones_Parciales_03.svg]]
>
> **Se lee así:** Es un árbol de recuadros que baja por pasos: del integrando inicial a la descomposición propuesta, luego a la igualdad de la que salen dos cajas hermanas, una por cada valor de $x$ donde se evalúa. Esas dos cajas vuelven a unirse en la integral ya descompuesta, que desciende en línea recta por la antiderivada, su forma compacta y un recuadro final de comprobación por derivación.
>
> **Por qué importa:** Fíjate en que los dos caminos de constantes se resuelven por separado y luego convergen, de modo que la respuesta queda determinada por completo. Esto te sirve como plantilla para cualquier racional con dos factores lineales: descomponer, evaluar en las raíces, integrar y verificar.
>
> **Ejemplo:** Con la integral de la nota, la caja de la raíz $x = 1$ da $B = 2$ y la de $x = -2$ da $A = -1$, y de ahí sale $-\ln|x+2| + 2\ln|x-1| + C$, que se puede compactar en un solo logaritmo.

> [!info] 📊 **Interpretación gráfica**
>
> - La función original tiene asíntotas verticales en $x = -2$ y $x = 1$
> - Cada fracción parcial contribuye con un comportamiento específico
> - La suma reproduce exactamente la función original

---

## 🎯 Estrategias y Consejos

> [!tip] 💡 **Consejos prácticos**
>
> - **Siempre verifica** que el grado del numerador sea menor
> - **Factoriza completamente** antes de establecer fracciones parciales
> - **Usa valores estratégicos** de $x$ para simplificar cálculos
> - **Verifica tu resultado** derivando la integral obtenida
>

> [!warning] ⚠️ **Errores comunes**
>
> - Olvidar casos de factores repetidos
> - Confundir la forma de fracciones con cuadráticos irreducibles
> - Errores aritméticos al resolver el sistema de ecuaciones
> - No verificar la factorización del denominador

---

## 📚 Referencias

> [!quote] **Notas relacionadas**
>
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida.md|01 - Métodos de Integración Definida.md]] - Método alternativo para ciertas funciones racionales

> [!quote] ❝ Referencias
>
> - Integración por Sustitución - Método alternativo para ciertas funciones racionales
> - [[Unidad 6 - Integrales/Técnicas de Integración/02 - Integración por Partes.md|02 - Integración por Partes.md]] - Complementa cuando hay productos
> - Factorización de Polinomios - Fundamento algebraico
> - [[Unidad 6 - Integrales/Técnicas de Integración/03 - Integrales Trigonométricas.md|03 - Integrales Trigonométricas.md]] - Casos especiales de sustitución

---

## 🔍 Notas Recomendadas

> [!note] 📖 **Para profundizar**
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo.md|04 - Teorema Fundamental del Cálculo.md]]
> - [[05 - Sistemas de ecuaciones lineales]]
> - Transformada de Laplace
> - Funciones Racionales y sus Propiedades
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida.md|01 - Métodos de Integración Definida.md]]

---

**Tags:** #MATG1045 #unidad6 #integrales-por-fracciones-parciales #matemáticas #cálculo #integración #fracciones-parciales #funciones-racionales #métodos-integración #álgebra #análisis-matemático #universidad #ingeniería

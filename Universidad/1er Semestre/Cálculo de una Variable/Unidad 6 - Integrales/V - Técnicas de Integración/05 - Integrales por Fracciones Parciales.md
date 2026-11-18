---
dg-publish: true
tags: [MATG1045, unidad6, integrales-por-fracciones-parciales, integrales, funciones-racionales, fracciones-parciales, integracion, algebra, metodos-integracion]
---

# 🧮 Integrales por Fracciones Parciales

## 🎯 Introducción

> [!info] 💡 Qué son y por qué son el final de la integración racional
>
> La **integración por fracciones parciales** es la técnica para integrar funciones racionales $\frac{P(x)}{Q(x)}$ cuando el denominador es factorizable y las técnicas previas (sustitución, por partes) no aplican. La idea es **descomponer** la fracción compleja en una suma de fracciones más simples —una por cada factor del denominador— que sí se integran con fórmulas de tabla.
>
> **Por qué importa:** es la última gran técnica de la integración indefinida. Todo lo que no resuelven el cambio de variable, las identidades trigonométricas ni por partes, lo resuelve esta: integrales racionales con polinomios de cualquier grado en el denominador, integrales que aparecen en transformadas de Laplace y en cualquier sistema de ecuaciones diferenciales.
>
> **Ejemplo:** $\int \frac{x+5}{x^2+x-2}\,dx$ no admite sustitución útil, pero el denominador se factoriza como $(x+2)(x-1)$, y con eso la integral se parte en dos logaritmos.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — el teorema de descomposición, el procedimiento en 5 pasos y la tabla de antiderivadas por tipo de factor.
> - **Procedimiento paso a paso** — los cinco pasos con sus dos métodos para resolver las constantes.
> - **Tipos de factores** — la referencia de formas: lineales, cuadráticos, simples y repetidos.
> - **Ejemplos resueltos** — el caso base con raíces, el factor repetido y el cuadrático irreducible.
> - **Ejercicios** — nueve plantillas, una por cada variante posible.
>
> **Por qué importa:** el método es siempre la misma secuencia (grados → factorizar → descomponer → constantes → integrar); lo único que cambia entre ejercicios es la forma que le das al denominador. Por eso la nota empieza con esa secuencia y termina con la plantilla de práctica.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Método de fracciones parciales (procedimiento en 5 pasos)
>
> Dada una racional propia $\frac{P(x)}{Q(x)}$ (con $\text{grado}(P) < \text{grado}(Q)$), el método consta de cinco pasos:
>
> 1. **Verificar grados:** si $\text{grado}(P) \geq \text{grado}(Q)$, dividir antes: $\frac{P}{Q} = \text{Cociente}(x) + \frac{\text{Resto}(x)}{Q(x)}$.
> 2. **Factorizar $Q(x)$** completamente en factores lineales (reales) y cuadráticos irreducibles, con sus multiplicidades.
> 3. **Descomponer** en fracciones parciales con una constante o un par lineal por cada factor.
> 4. **Resolver las constantes** por sustitución de raíces o por igualación de coeficientes.
> 5. **Integrar** cada fracción parcial por separado y **verificar derivando** la respuesta.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_por_Fracciones_Parciales_01.svg]]
>
> **Se lee así:** una cadena de rectángulos encadenados de arriba abajo, sin rombos ni bifurcaciones: cada caja es un paso y el orden de las flechas impone el orden de trabajo. La cadena arranca en el objetivo general $\int P(x)/Q(x)\,dx$, pasa por los cinco pasos numerados (grados, factorizar, descomponer, constantes, integrar) y termina en una caja de cierre roja que manda comprobar el resultado derivando.
>
> **Por qué importa:** el diagrama es una **lista de control**, no una encrucijada: el error típico es saltarse la verificación de grados o factorizar a medias. Úsalo como orden de trabajo para no inventarte la descomposición antes de tener el denominador completamente factorizado.
>
> **Ejemplo:** con $\int \frac{x+5}{x^2+x-2}\,dx$, la cadena te lleva de comprobar que $1 < 2$ a factorizar $(x+2)(x-1)$, declarar $A$ y $B$, integrar cada parte y cerrar derivando.

> [!note] 📋 Definición — Formas de la descomposición y antiderivadas según el factor
>
> El **Teorema de Descomposición en Fracciones Parciales** establece que toda función racional **propia** puede expresarse de manera **única** como suma de fracciones parciales. Cada tipo de factor del denominador exige una forma y una antiderivada distintas:
>
> - **Lineal simple** $(ax+b)$ → $\frac{A}{ax+b}$ → logaritmo: $\int \frac{du}{u} = \ln|u| + C$
> - **Lineal repetido** $(ax+b)^n$ → $\frac{A_1}{ax+b} + \dots + \frac{A_n}{(ax+b)^n}$ → potencia: $\int u^{-n}\,du = \frac{-1}{(n-1)u^{n-1}} + C$ ($n > 1$)
> - **Cuadrático irreducible** $ax^2+bx+c$ con $\Delta < 0$ → $\frac{Bx+C}{ax^2+bx+c}$ → arctangente: $\int \frac{du}{u^2+a^2} = \frac{1}{a}\arctan\frac{u}{a} + C$
> - **Cuadrático repetido** $(ax^2+bx+c)^n$ → suma de fracciones con numeradores lineales, de grado $n$ en el denominador.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_por_Fracciones_Parciales_02.svg]]
>
> **Se lee así:** el diagrama separa dos planos desde una caja raíz con las antiderivadas estándar según el factor. Arriba, tres ramas verdes —una por cada tipo de factor simple— terminan en su fórmula integral (logaritmo, potencia y arctangente). Abajo, una cuarta rama lleva a la **base teórica**, que se abre en tres pilares azules: factorización única sobre $\mathbb{R}[x]$, teorema fundamental del álgebra y descomposición única.
>
> **Por qué importa:** es la tabla que necesitas **ya descompuesta** la fracción: cada tipo de factor pide una antiderivada distinta, y confundirlas es el error típico. Los tres pilares, en cambio, te garantizan que la descomposición que encontraste es única y no arbitraria: si cuadra, es la correcta.
>
> **Ejemplo:** en $\int \frac{x+5}{x^2+x-2}\,dx$, los factores $x+2$ y $x-1$ caen en la rama de lineal simple y cada uno aporta su logaritmo.

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🔎 Paso 1 — Verificación del grado
>
> **Si** $\text{grado}(P(x)) \geq \text{grado}(Q(x))$ (racional **impropia**): dividir primero.
> $$\frac{P(x)}{Q(x)} = \text{Cociente}(x) + \frac{\text{Resto}(x)}{Q(x)}$$
> El cociente se integra como polinomio y el resto, de menor grado, sí entra en fracciones parciales.
>
> **Si** $\text{grado}(P(x)) < \text{grado}(Q(x))$ (racional **propia**): continuar al paso 2.
>
> **Por qué importa:** sin este paso, la descomposición del paso 3 simplemente **no existe** en la forma estándar; es el filtro que determina si el método aplica directo o requiere una división previa.

> [!tip] 🧱 Paso 2 — Factorización del denominador
>
> Descomponer $Q(x)$ **completamente**:
>
> - Raíces reales $\Rightarrow$ factores lineales $(x - r)$.
> - Factores sin raíz real $\Rightarrow$ cuadráticos irreducibles $ax^2+bx+c$ con $\Delta < 0$.
> - Registrar la **multiplicidad** de cada factor: un factor repetido $k$ veces aporta $k$ fracciones.
>
> **Por qué importa:** una factorización incompleta produce una descomposición incompleta y, con ella, un sistema de ecuaciones sin solución. No pases al paso 3 hasta que $Q(x)$ esté escrito como producto de factores de grado 1 y 2.

> [!tip] 🧮 Paso 3 — Establecer la descomposición
>
> Escribir una fracción parcial por cada factor, con la forma que le corresponde (ver **Definición — Formas de la descomposición**):
>
> - $(x-r)$ simple → $\frac{A}{x-r}$
> - $(x-r)^k$ repetido → $\frac{A_1}{x-r} + \frac{A_2}{(x-r)^2} + \dots + \frac{A_k}{(x-r)^k}$
> - $ax^2+bx+c$ irreducible → $\frac{Bx+C}{ax^2+bx+c}$
> - $(ax^2+bx+c)^m$ repetido → $\frac{B_1x+C_1}{ax^2+bx+c} + \dots + \frac{B_mx+C_m}{(ax^2+bx+c)^m}$
>
> Después multiplicar por $Q(x)$ para obtener una **identidad polinomial**: la igualdad vale para **todo** $x$.
>
> **Por qué importa:** el numerador de una fracción parcial cuadrática siempre es **lineal** ($Bx + C$), no una constante: olvidar la $x$ deja el sistema incompleto y pierdes la mitad de las soluciones.

> [!tip] 🔢 Paso 4 — Resolver para las constantes
>
> **Método 1 — Sustitución de raíces:**
>
> - Partir de la identidad ya multiplicada por $Q(x)$.
> - Sustituir las raíces del denominador: cada una anula todos los términos que llevan ese factor y deja una ecuación con **una sola** constante.
>
> **Método 2 — Igualación de coeficientes:**
>
> - Expandir el lado derecho de la identidad.
> - Igualar los coeficientes de cada potencia de $x$ (mayor a menor) y resolver el sistema.
>
> **Por qué importa:** con $k$ factores hacen falta $k$ ecuaciones; el método 1 las da en un renglón por raíz, y el método 2 las da todas al comparar potencias. Si tras sustituir las raíces quedan constantes sin determinar, combina ambos métodos (usa las raíces y una potencia más).

> [!tip] 🧘 Paso 5 — Integración
>
> Integrar cada fracción parcial con las fórmulas básicas:
>
> - $\int \frac{1}{u}\,du = \ln|u| + C$
> - $\int \frac{1}{u^n}\,du = \frac{-1}{(n-1)u^{n-1}} + C$ (para $n > 1$)
> - $\int \frac{1}{u^2+a^2}\,du = \frac{1}{a}\arctan\left(\frac{u}{a}\right) + C$
> - Numerador lineal sobre cuadrático: partir $\frac{Bx+C}{ax^2+bx+c} = \frac{B}{2a}\cdot\frac{2ax+b}{ax^2+bx+c} + \text{(constante sobre el cuadrático)}$, que da logaritmo + arctangente.
>
> **Por qué importa:** la última línea es la única variante con trampa: si el numerador **no** es la derivada del denominador, no sale logaritmo puro; hay que separar en dos fracciones antes de integrar.

---

## 📐 Tipos de Factores: Referencia Rápida

> [!tip] 📋 Tabla maestra de descomposición
>
> | Factor en $Q(x)$ | Forma de la descomposición | Antiderivada resultante |
> |---|---|---|
> | $(ax+b)$ | $\dfrac{A}{ax+b}$ | $\dfrac{1}{a}\ln\|ax+b\|$ |
> | $(ax+b)^n$ | $\dfrac{A_1}{ax+b} + \dots + \dfrac{A_n}{(ax+b)^n}$ | logaritmo + potencias de $(ax+b)^{-k}$ |
> | $ax^2+bx+c$, $\Delta<0$ | $\dfrac{Bx+C}{ax^2+bx+c}$ | logaritmo y/o $\dfrac{1}{\sqrt{\Delta}}\arctan$ completando cuadrado |
> | $(ax^2+bx+c)^n$ | $\dfrac{B_1x+C_1}{ax^2+bx+c} + \dots + \dfrac{B_nx+C_n}{(ax^2+bx+c)^n}$ | arctangente + reducción |
>
> **Por qué importa:** es la consulta de tres segundos antes de empezar cualquier ejercicio: identifica el factor, copia la forma y ya sabes cuántas constantes debes determinar (una por fracción).

> [!warning] 🚨 Errores comunes
>
> - Olvidar el paso de grados (racional impropia sin dividir).
> - No factorizar completamente el denominador o pasar por alto multiplicidades.
> - Escribir solo constante $A$ donde toca numerador lineal $Bx + C$.
> - Usar una sola raíz y dar el sistema por cerrado cuando quedan constantes libres.
> - Errores aritméticos al resolver el sistema de ecuaciones.
> - No verificar la respuesta derivando.
>
> **Por qué importa:** los cuatro primeros son fallos de **planteamiento** y ninguno avisa con error: la integral "se ve bien" pero no cuadra al derivar. Por eso el paso 5 termina siempre con la verificación.

> [!success] 💡 Consejos prácticos
>
> - **Verifica siempre** que el grado del numerador sea menor (o divide primero).
> - **Factoriza completamente** antes de establecer fracciones parciales.
> - **Usa raíces** para determinar constantes: son la vía más corta cuando el denominador tiene raíces claras.
> - **Compacta** la respuesta en un solo logaritmo cuando los signos lo permiten: $\ln|a| + 2\ln|b| = \ln\left|\frac{b^2}{a}\right|$.
> - **Verifica tu resultado** derivando: la derivada debe devolver exactamente $P(x)/Q(x)$.
>
> **Por qué importa:** la compactación no es cosmética: deja la respuesta en la forma en que aparece en las tablas y en los resultados de control, y hace visible si un signo salió invertido.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Dos factores lineales simples (sustitución de raíces)
>
> **Resolver:** $\int \frac{x+5}{x^2+x-2}\,dx$
>
> 1. **Grado:** numerador 1 < denominador 2 → propia ✓
> 2. **Factorizar:** $x^2+x-2 = (x+2)(x-1)$
> 3. **Descomponer:** $\frac{x+5}{(x+2)(x-1)} = \frac{A}{x+2} + \frac{B}{x-1}$
> 4. **Constantes:** multiplicando por el denominador, $x+5 = A(x-1) + B(x+2)$:
>    - $x = 1$: $6 = 3B \Rightarrow B = 2$
>    - $x = -2$: $3 = -3A \Rightarrow A = -1$
> 5. **Integrar:** $\int \left(\frac{-1}{x+2} + \frac{2}{x-1}\right)dx = -\ln|x+2| + 2\ln|x-1| + C$
>
> **Forma compacta:** $\ln\left|\frac{(x-1)^2}{x+2}\right| + C$
>
> **Control:** $\frac{d}{dx}\ln\left|\frac{(x-1)^2}{x+2}\right| = \frac{2}{x-1} - \frac{1}{x+2} = \frac{2(x+2)-(x-1)}{(x-1)(x+2)} = \frac{x+5}{x^2+x-2}$ ✓
>
> **Por qué importa:** este es el patrón base: **dos raíces, dos constantes, dos logaritmos**. Sustituir las raíces directamente en la identidad multiplicada es el método más rápido cuando el denominador ya está factorizado.

> [!example] 🖼️ El ejemplo 1, paso a paso en un diagrama
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Integrales_por_Fracciones_Parciales_03.svg]]
>
> **Se lee así:** un árbol que baja por pasos: del integrando inicial a la descomposición propuesta, luego a la identidad $x+5 = A(x-1)+B(x+2)$, de la que salen **dos cajas hermanas** —una por cada valor de $x$ donde se evalúa—. Esas dos cajas vuelven a unirse en la integral ya descompuesta, que desciende en línea recta por la antiderivada, su forma compacta y un recuadro final de comprobación por derivación.
>
> **Por qué importa:** los dos caminos de constantes se resuelven por separado y **convergen**: la respuesta queda determinada por completo con una evaluación por raíz. Te sirve de plantilla para cualquier racional con dos factores lineales: descomponer, evaluar en las raíces, integrar, verificar.
>
> **Ejemplo:** la caja $x=1$ da $B=2$ y la $x=-2$ da $A=-1$, y de ahí sale $-\ln|x+2| + 2\ln|x-1| + C$.

> [!example] 🔢 Ejemplo 2 — Factor lineal repetido (igualación de coeficientes)
>
> **Resolver:** $\int \frac{1}{x^2(x+1)}\,dx$
>
> 1. **Grado:** $0 < 3$ → propia ✓
> 2. **Factorizar:** $x^2(x+1)$ — el factor $x$ está **repetido** (multiplicidad 2).
> 3. **Descomponer:** $\frac{1}{x^2(x+1)} = \frac{A}{x} + \frac{B}{x^2} + \frac{C}{x+1}$
> 4. **Constantes (coeficientes):** $1 = Ax(x+1) + B(x+1) + Cx^2 = (A+C)x^2 + (A+B)x + B$:
>    - $x^0$: $B = 1$
>    - $x^1$: $A+B = 0 \Rightarrow A = -1$
>    - $x^2$: $A+C = 0 \Rightarrow C = 1$
> 5. **Integrar:** $\int \left(-\frac{1}{x} + \frac{1}{x^2} + \frac{1}{x+1}\right)dx = -\ln|x| - \frac{1}{x} + \ln|x+1| + C$
>
> **Forma compacta:** $\ln\left|\frac{x+1}{x}\right| - \frac{1}{x} + C$
>
> **Por qué importa:** un factor repetido $k$ veces genera $k$ fracciones con **el mismo** factor en denominador (potencias $1, \dots, k$). Aquí no hay raíces múltiples que sustituir cómodamente, por eso el método de coeficientes es el indicado.

> [!example] 🔢 Ejemplo 3 — Cuadrático irreducible (completar cuadrado)
>
> **Resolver:** $\int \frac{x-1}{x^2+x+1}\,dx$
>
> 1. **Grado:** $1 < 2$ → propia ✓
> 2. **Factorizar:** $\Delta = 1^2 - 4 = -3 < 0$ → **irreducible**, se queda como está.
> 3. **Descomponer:** ya es irreducible; el numerador lineal se escribe como combinación de la derivada del denominador:
> $x - 1 = \frac{1}{2}(2x+1) - \frac{3}{2}$
> 4. **Integrar:** $\frac{1}{2}\int \frac{2x+1}{x^2+x+1}\,dx - \frac{3}{2}\int \frac{dx}{x^2+x+1}$
>    - Primera: $\frac{1}{2}\ln(x^2+x+1)$
>    - Segunda: $x^2+x+1 = \left(x+\frac{1}{2}\right)^2 + \frac{3}{4}$ → $\frac{3}{2}\cdot\frac{2}{\sqrt{3}}\arctan\frac{2x+1}{\sqrt{3}} = \sqrt{3}\arctan\frac{2x+1}{\sqrt{3}}$
> 5. **Respuesta:** $\frac{1}{2}\ln(x^2+x+1) - \sqrt{3}\arctan\left(\frac{2x+1}{\sqrt{3}}\right) + C$
>
> **Por qué importa:** es el patrón de todo cuadrático irreducible: **logaritmo + arctangente**. El truco de separar el numerador en "derivada del denominador + constante" es lo que convierte la fracción en dos integrales de tabla, y completar el cuadrado es lo que deja la segunda en el patrón $\int \frac{du}{u^2+a^2}$.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{x^3+1}{x^2-1}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Grado:** $3 \geq 2$ → impropia, dividir: $x^3+1 = x(x^2-1) + (x+1)$, luego $\frac{x^3+1}{x^2-1} = x + \frac{x+1}{(x-1)(x+1)} = x + \frac{1}{x-1}$ (cancelando $x+1$, $x \neq -1$).
> > $$\int x\,dx + \int \frac{dx}{x-1} = \frac{x^2}{2} + \ln|x-1| + C$$
> > **Control:** $x + \frac{1}{x-1} = \frac{x(x-1)+1}{x-1} = \frac{x^2-x+1}{x-1}$, y $(x^2-x+1)(x+1) = x^3+1$ ✓
> > **Lección:** la división polinomial a veces simplifica el resto hasta cancelar factores ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{2x+3}{x^2+1}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Denominador:** $\Delta = -4 < 0$ → irreducible; el numerador contiene $2x$, la derivada del denominador.
> > $$\int \frac{2x}{x^2+1}\,dx + \int \frac{3}{x^2+1}\,dx = \ln(x^2+1) + 3\arctan(x) + C$$
> > **Respuesta:** $\ln(x^2+1) + 3\arctan(x) + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{1}{x^2+4x+8}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Denominador:** $\Delta = 16-32 = -16 < 0$ → irreducible; **no se factoriza**, completar cuadrado: $x^2+4x+8 = (x+2)^2+4$.
> > $$\int \frac{dx}{(x+2)^2+2^2} = \frac{1}{2}\arctan\left(\frac{x+2}{2}\right) + C$$
> > **Respuesta:** $\frac{1}{2}\arctan\left(\frac{x+2}{2}\right) + C$.
> > **Lección:** cuando el denominador no tiene raíces, no hay descomposición: solo completar cuadrado y arctangente ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{1}{(x^2+1)^2}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Cuadrático irreducible repetido** ($n = 2$): usar la sustitución trigonométrica $x = \tan\theta$, $dx = \sec^2\theta\,d\theta$, $1+x^2 = \sec^2\theta$:
> > $$\int \frac{\sec^2\theta}{\sec^4\theta}\,d\theta = \int \cos^2\theta\,d\theta = \frac{\theta + \sin\theta\cos\theta}{2} + C$$
> > Con $\theta = \arctan(x)$, $\sin\theta\cos\theta = \frac{x}{1+x^2}$ (triángulo con catetos $x$ y $1$):
> > **Respuesta:** $\frac{1}{2}\arctan(x) + \frac{x}{2(x^2+1)} + C$.
> > **Control:** $\frac{d}{dx}\left[\frac{\arctan x + x/(1+x^2)}{2}\right] = \frac{1}{2}\left[\frac{1}{1+x^2} + \frac{1-x^2}{(1+x^2)^2}\right] = \frac{1}{(1+x^2)^2}$ ✓
> > **Lección:** la repetición de un cuadrático se resuelve con trigonometría o reducción, nunca con una sola fracción ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{1}{(x-1)(x^2+1)}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Mezcla** de lineal simple e irreducible: $\frac{1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx+C}{x^2+1}$.
> > Identidad: $1 = A(x^2+1) + (Bx+C)(x-1)$:
> > - $x = 1$: $1 = 2A \Rightarrow A = \frac{1}{2}$
> > - Coef. de $x^2$: $0 = A + B \Rightarrow B = -\frac{1}{2}$
> > - Término independiente: $1 = A - C \Rightarrow C = -\frac{1}{2}$
>
> > $$\frac{1}{2}\int \frac{dx}{x-1} - \frac{1}{2}\int \frac{x+1}{x^2+1}\,dx = \frac{1}{2}\ln|x-1| - \frac{1}{4}\ln(x^2+1) - \frac{1}{2}\arctan(x) + C$$
> > **Respuesta:** $\frac{1}{2}\ln|x-1| - \frac{1}{4}\ln(x^2+1) - \frac{1}{2}\arctan(x) + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{x^2}{x^2+1}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Grados iguales:** antes de todo, dividir (o reescribir): $\frac{x^2}{x^2+1} = \frac{(x^2+1)-1}{x^2+1} = 1 - \frac{1}{x^2+1}$.
> > $$\int 1\,dx - \int \frac{dx}{x^2+1} = x - \arctan(x) + C$$
> > **Respuesta:** $x - \arctan(x) + C$.
> > **Lección:** si los grados son iguales, la racional es impropia: el paso 1 es obligatorio ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{1}{x^2-4}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Factorizar:** $x^2-4 = (x-2)(x+2)$ → $\frac{1}{(x-2)(x+2)} = \frac{A}{x-2} + \frac{B}{x+2}$.
> > Identidad: $1 = A(x+2) + B(x-2)$:
> > - $x = 2$: $1 = 4A \Rightarrow A = \frac{1}{4}$
> > - $x = -2$: $1 = -4B \Rightarrow B = -\frac{1}{4}$
>
> > $$\frac{1}{4}\int \frac{dx}{x-2} - \frac{1}{4}\int \frac{dx}{x+2} = \frac{1}{4}\ln\left|\frac{x-2}{x+2}\right| + C$$
> > **Respuesta:** $\frac{1}{4}\ln\left|\frac{x-2}{x+2}\right| + C$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{3x+1}{(x+1)^2}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Lineal repetido:** $\frac{3x+1}{(x+1)^2} = \frac{A}{x+1} + \frac{B}{(x+1)^2}$.
> > Identidad: $3x+1 = A(x+1) + B$:
> > - Coef. de $x$: $A = 3$
> > - Independiente: $A + B = 1 \Rightarrow B = -2$
>
> > $$\int \frac{3}{x+1}\,dx - \int \frac{2}{(x+1)^2}\,dx = 3\ln|x+1| + \frac{2}{x+1} + C$$
> > **Control:** $\frac{d}{dx}\left[3\ln|x+1| + \frac{2}{x+1}\right] = \frac{3}{x+1} - \frac{2}{(x+1)^2} = \frac{3(x+1)-2}{(x+1)^2} = \frac{3x+1}{(x+1)^2}$ ✓
> > **Lección:** la potencia $k$ en el denominador aporta potencias $1$ a $k$ arriba, y la antiderivada de $(x+1)^{-2}$ es $-\frac{1}{x+1}$: por eso el signo del segundo término es **positivo** ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{1}{x(x^2+1)}\,dx$.
>
> > [!success]- ✅ Solución
> >
> > **Mezcla:** $\frac{1}{x(x^2+1)} = \frac{A}{x} + \frac{Bx+C}{x^2+1}$ → $1 = A(x^2+1) + (Bx+C)x$:
> > - $x = 0$: $A = 1$
> > - Coef. $x^2$: $A + B = 0 \Rightarrow B = -1$; coef. $x$: $C = 0$
>
> > $$\int \left(\frac{1}{x} - \frac{x}{x^2+1}\right)dx = \ln|x| - \frac{1}{2}\ln(x^2+1) + C$$
> > **Forma compacta:** $\ln\frac{|x|}{\sqrt{x^2+1}} + C$.
> > **Lección:** cuando la $x$ del denominador es una potencia par, la fracción resultante suele cancelar el término lineal del numerador ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico el grado del racional y aplico división polinomial cuando $\text{grado}(P) \geq \text{grado}(Q)$.
> - [ ] Factorizo el denominador completo identificando factores lineales, cuadráticos irreducibles y sus multiplicidades.
> - [ ] Escribo la forma de descomposición correcta para cada tipo de factor, con numerador lineal donde corresponde.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Determino las constantes por sustitución de raíces y por igualación de coeficientes, eligiendo el método según el caso.
> - [ ] Integro cada fracción parcial con logaritmo, potencia o arctangente según el factor del denominador.
> - [ ] Separo numeradores lineales sobre cuadráticos en parte logarítmica y parte arctangente completando cuadrado.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Combino división polinomial y fracciones parciales en racionales impropias con cancelaciones posteriores.
> - [ ] Resuelvo factores repetidos, lineales y cuadráticos, sin olvidar ningún término de la descomposición.
> - [ ] Verifico cada resultado derivando y recuperando exactamente el integrando original, y compacto la respuesta en un solo logaritmo.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 7.4: integración de funciones racionales por fracciones parciales.
> - G. Strang, *Calculus* (Wellesley-Cambridge): fracciones parciales y funciones racionales.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — el concepto de antiderivada que esta técnica aplica fracción por fracción.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — las tres fórmulas (logaritmo, potencia, arctangente) hacia las que tiende todo.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — la misma racional evaluada con límites cuando el intervalo está acotado.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el teorema que justifica la verificación por derivación.
> - [[Preuniversitario/Matemáticas/Unidad 4 - Matrices y Sistemas/I - Matrices y Sistemas de Ecuaciones/05 - Sistemas de ecuaciones lineales|05 - Sistemas de ecuaciones lineales]] — el álgebra del paso 4: sistemas lineales para determinar las constantes.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuándo aplica el método de fracciones parciales?::Cuando $\frac{P}{Q}$ es una racional propia ($\text{grado}(P) < \text{grado}(Q)$) y el denominador $Q$ es factorizable en $\mathbb{R}[x]$.
> - ¿Qué hago si el grado del numerador es mayor o igual?::División polinomial: $\frac{P}{Q} = \text{Cociente} + \frac{\text{Resto}}{Q}$; el resto, de menor grado, entra en fracciones parciales.
> - ¿Qué forma le doy a un lineal repetido $(ax+b)^n$?::$\frac{A_1}{ax+b} + \frac{A_2}{(ax+b)^2} + \dots + \frac{A_n}{(ax+b)^n}$: una fracción por cada potencia, de 1 a $n$.
> - ¿Y a un cuadrático irreducible $ax^2+bx+c$ con $\Delta<0$?::$\frac{Bx+C}{ax^2+bx+c}$: numerador **lineal**, no constante; con repetición, se suman fracciones análogas con potencias en el denominador.
> - ¿Cómo resuelvo las constantes?::Dos métodos: sustitución de raíces (tras multiplicar por $Q$, cada raíz anula los demás términos) o igualación de coeficientes de potencias semejantes.
> - ¿Qué antiderivada tiene cada tipo de factor?::Lineal simple → logaritmo; potencia de lineal → $\frac{-1}{(n-1)u^{n-1}}$; cuadrático irreducible → $\frac{1}{a}\arctan\frac{u}{a}$ tras completar cuadrado.
> - ¿Por qué el numerador de la fracción cuadrática es $Bx+C$?::Porque el numerador debe tener grado **menor** que el denominador: grado 1 < grado 2; y eso da dos constantes que igualar.
> - ¿Cómo empieza siempre la verificación?::Derivando la respuesta: debe devolver exactamente $\frac{P(x)}{Q(x)}$; si no, revisa la factorización o el sistema de constantes.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — el concepto que esta técnica ejecuta fracción por fracción.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/04 - Integrales Notables (Fórmulas Directas)|04 - Integrales Notables (Fórmulas Directas)]] — las tres fórmulas de salida: logaritmo, potencia y arctangente.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — la técnica previa: si el denominador no se factoriza con facilidad, un cambio de variable puede resolverlo antes.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/02 - Integración por Partes|02 - Integración por Partes]] — complemento para productos $\frac{P(x)}{Q(x)}\cdot f(x)$ donde la racional queda como $u$.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/03 - Integrales Trigonométricas|03 - Integrales Trigonométricas]] — tras la sustitución de Weierstrass, una $R(\sin x, \cos x)$ se vuelve racional y esta nota es la que la termina.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/04 - Integrales de Funciones Inversas|04 - Integrales de Funciones Inversas]] — donde la residual de por partes a veces produce una racional larga.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — estas mismas racionales integradas con límites cuando el intervalo se escapa.
>
> **Conexiones interdisciplinarias:** la descomposición es el motor de la **transformada de Laplace inversa** (ingeniería de control), del **análisis de circuitos** (funciones de transferencia) y de la **teoría de control** (estabilidad); en álgebra, conecta con sistemas de ecuaciones lineales, y en análisis, con la factorización única de polinomios.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 6 y 3: grados iguales y denominador sin raíces, los dos atajos que evitan la descomposición completa.
> - Después pasa al 7, 8 y 2: lineal simple por parejas, factor repetido y cuadrático irreducible puro, los tres tipos canónicos.
> - Cierra con 1, 4, 5 y 9: la impropia con cancelación, la repetición cuadrática con trigonometría y las mezclas con numerador lineal.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/VI - Otras Técnicas/01 - Integración Numérica|01 - Integración Numérica]] para integrales que no admiten forma cerrada; como siguiente horizonte, las **transformadas de Laplace**, donde fracciones parciales se aplican a cada ejercicio.

---

**Tags:** #MATG1045 #unidad6 #integrales-por-fracciones-parciales #integrales #funciones-racionales #fracciones-parciales #integracion #algebra #metodos-integracion

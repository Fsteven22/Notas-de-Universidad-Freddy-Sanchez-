---
dg-publish: true
tags: [MATG1045, unidad4, derivacion-logaritmica, calculo, derivadas, funciones-exponenciales, regla-cadena, productos-complejos, exponentes-variables]
---

# 🔄 Derivación Logarítmica

## 🎯 Introducción

> [!info] 💡 La idea en una frase
>
> La **derivación logarítmica** es una técnica que usa las propiedades del logaritmo natural para convertir productos en sumas, cocientes en restas y potencias en coeficientes, de modo que funciones muy complicadas se derivan como si fueran sumas de términos simples.
>
> **Por qué importa:** hay funciones donde la regla del producto obliga a escribir n términos larguísimos, y otras donde ninguna regla directa sirve porque la base y el exponente dependen de $x$ a la vez. Con un solo $\ln$ a ambos lados, los dos problemas desaparecen.
>
> **Ejemplo:** para $y = x^2(x+1)^3\sqrt{x-2}$ basta tomar $\ln y = 2\ln x + 3\ln(x+1) + \frac{1}{2}\ln(x-2)$ y derivar esa suma.

> [!warning] ⚠️ Lo que debes dominar antes
>
> - La regla de la cadena, porque al derivar $\ln|y|$ respecto a $x$ aparece un factor $\frac{1}{y}\frac{dy}{dx}$: [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]].
> - La derivación implícita, porque el paso central de la técnica es derivar implícitamente ambos lados: [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]].
> - Las propiedades de los logaritmos ($\ln AB = \ln A + \ln B$, $\ln A^n = n\ln A$), que son las que hacen el trabajo sucio.
>
> **Por qué importa:** la técnica no tiene trucos ocultos: toma $\ln$, expande, deriva implícitamente y despeja. Si dominas esas tres piezas, el resto es álgebra.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Derivación logarítmica
>
> La **derivación logarítmica** consiste en tomar el logaritmo natural a ambos lados de la ecuación $y = f(x)$, descomponer el lado derecho con las propiedades del $\ln$, derivar implícitamente respecto a $x$ y despejar $\frac{dy}{dx}$ multiplicando por la función original $y$.
>
> $$\frac{d}{dx}[\ln|y|] = \frac{1}{y} \cdot \frac{dy}{dx} \quad \Longrightarrow \quad \frac{dy}{dx} = y \cdot \frac{d}{dx}[\ln|y|].$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Derivación_Logarítmica_01.svg]]
>
> **Se lee así:** Es una cadena recta de rectángulos, sin decisiones: cada caja es un paso y la flecha apunta al siguiente. La secuencia va de la función complicada a la aplicación del logaritmo, pasa por las propiedades del $\ln$ que convierten productos en sumas y potencias en coeficientes, sigue con la derivación implícita de ambos lados y termina despejando $\frac{dy}{dx}$ y volviendo a sustituir $y = f(x)$.
>
> **Por qué importa:** Muestra el esqueleto de la técnica: el logaritmo no es un truco, es una forma de **convertir multiplicaciones en sumas**. Si te saltas la caja de propiedades, pierdes justo la ventaja que hace el método rápido.
>
> **Ejemplo:** Para derivar $y = x^2(x+1)^3\sqrt{x-2}$ de la nota, tomas $\ln|y|$, lo separas en $2\ln x + 3\ln(x+1) + \frac{1}{2}\ln(x-2)$ y derivas esa suma.

> [!note] 📋 Definición — Potencia de base y exponente variables
>
> Cuando la función tiene la forma $y = f(x)^{g(x)}$, es decir, tanto la base como el exponente dependen de $x$, ninguna regla directa aplica: la de potencias exige exponente constante y la exponencial exige base constante. El logaritmo resuelve el problema porque $\ln(f(x)^{g(x)}) = g(x)\ln f(x)$, que ya es un producto derivable.
>
> $$\ln y = g(x)\ln f(x) \quad \Longrightarrow \quad \frac{dy}{dx} = f(x)^{g(x)}\left[g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}\right].$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Derivación_Logarítmica_02.svg]]
>
> **Se lee así:** Es una cadena de seis rectángulos sin ramas: se parte de la potencia con base y exponente variables, se aplica el logaritmo y se llega a la igualdad clave, donde el exponente multiplica al logaritmo de la base. De ahí se deriva con la regla del producto, se despeja $\frac{dy}{dx}$ y la respuesta final aparece multiplicada por la potencia original.
>
> **Por qué importa:** Aquí ninguna regla directa sirve: la de potencias no admite exponente variable y la exponencial no admite base variable. **El logaritmo es la única salida**, y el diagrama te fija el orden en que van los pasos.
>
> **Ejemplo:** Con $y = x^x$ el diagrama se reduce a $\ln y = x\ln x$, de donde $\frac{1}{y}\frac{dy}{dx} = \ln x + 1$ y $\frac{dy}{dx} = x^x(\ln x + 1)$.

---

## 📊 Casos de aplicación

### 🧮 Técnica $\ln$ para productos complejos

> [!info] 🧮 Del producto largo al término elegante
>
> **Problema:** derivar $y = f_1(x) \cdot f_2(x) \cdot f_3(x) \cdots f_n(x)$.
>
> **Solución tradicional** (regla del producto): sale un término por factor, $\frac{dy}{dx} = f_1'f_2f_3\cdots f_n + f_1f_2'f_3\cdots f_n + \cdots$, con $n$ sumandos larguísimos.
>
> **Solución con $\ln$:**
>
> | Paso | Expresión |
> |------|-----------|
> | Tomar $\ln$ | $\ln|y| = \ln|f_1(x)| + \ln|f_2(x)| + \cdots + \ln|f_n(x)|$ |
> | Derivar implícitamente | $\frac{1}{y}\frac{dy}{dx} = \frac{f_1'}{f_1} + \frac{f_2'}{f_2} + \cdots + \frac{f_n'}{f_n}$ |
> | Despejar | $\frac{dy}{dx} = y\left[\frac{f_1'}{f_1} + \frac{f_2'}{f_2} + \cdots + \frac{f_n'}{f_n}\right]$ |
>
> **Por qué importa:** un solo término elegante contra $n$ términos complicados. El coste del método es solo escribir el $\ln$ una vez.
>
> **Ejemplo:** en $y = x^2(x+1)^3$ queda $\ln y = 2\ln x + 3\ln(x+1)$ y $\frac{1}{y}\frac{dy}{dx} = \frac{2}{x} + \frac{3}{x+1}$.

> [!example] 🔢 Ejemplo 1: producto de múltiples funciones
>
> **Encontrar** $\frac{d}{dx}\left[x^2(x+1)^3\sqrt{x-2}\right]$ para $x > 2$.
>
> 1. Sea $y = x^2(x+1)^3\sqrt{x-2}$; entonces $\ln y = 2\ln x + 3\ln(x+1) + \frac{1}{2}\ln(x-2)$.
> 2. Derivando implícitamente: $\frac{1}{y}\frac{dy}{dx} = \frac{2}{x} + \frac{3}{x+1} + \frac{1}{2(x-2)}$.
> 3. Multiplicando por $y$:
>
> $$\frac{dy}{dx} = x^2(x+1)^3\sqrt{x-2}\left[\frac{2}{x} + \frac{3}{x+1} + \frac{1}{2(x-2)}\right].$$

> [!example] 🔢 Ejemplo 2: cociente complejo
>
> **Encontrar** $\frac{d}{dx}\left[\frac{x^3(x+1)^2}{\sqrt{x-1}(2x+3)^4}\right]$ para $x > 1$.
>
> 1. Sea $y = \frac{x^3(x+1)^2}{\sqrt{x-1}(2x+3)^4}$; entonces $\ln y = 3\ln x + 2\ln(x+1) - \frac{1}{2}\ln(x-1) - 4\ln(2x+3)$.
> 2. Derivando: $\frac{1}{y}\frac{dy}{dx} = \frac{3}{x} + \frac{2}{x+1} - \frac{1}{2(x-1)} - \frac{8}{2x+3}$ (el último término trae un $2$ por la cadena).
> 3. Resultado: $\frac{dy}{dx} = y \cdot \left[\frac{3}{x} + \frac{2}{x+1} - \frac{1}{2(x-1)} - \frac{8}{2x+3}\right]$.
>
> **Por qué importa:** los signos $+$ y $-$ salen solos de la posición del factor en el cociente; esa es la ventaja sobre la regla del cociente.

### 🔢 Funciones de la forma $f(x)^{g(x)}$

> [!info] 🧮 El caso sin regla directa
>
> **El problema único:** cuando la base y el exponente dependen de $x$ a la vez:
>
> - La regla de potencias $\frac{d}{dx}[x^n] = nx^{n-1}$ **no aplica** (el exponente es variable).
> - La regla exponencial $\frac{d}{dx}[a^x] = a^x\ln a$ **no aplica** (la base es variable).
>
> **La salida logarítmica**, para $y = f(x)^{g(x)}$:
>
> 1. $\ln y = g(x) \ln f(x)$
> 2. $\frac{1}{y}\frac{dy}{dx} = g'(x)\ln f(x) + g(x) \cdot \frac{f'(x)}{f(x)}$ (regla del producto)
> 3. $\frac{dy}{dx} = f(x)^{g(x)} \left[g'(x)\ln f(x) + g(x) \cdot \frac{f'(x)}{f(x)}\right]$
>
> **Patrón de memoria:** *"g prima por ln de f, más g por f prima sobre f"*.
>
> **Por qué importa:** es el único caso donde la derivación logarítmica no es un atajo, sino la **única** vía. Reconocerlo a tiempo evita media página de intentos fallidos.
>
> **Ejemplo:** en $y = (x^2+1)^{\sin x}$ queda $\ln y = \sin x \cdot \ln(x^2+1)$ y, por producto, $\frac{1}{y}\frac{dy}{dx} = \cos x\ln(x^2+1) + \frac{2x\sin x}{x^2+1}$.

> [!example] 🔢 Ejemplo 3: $x^x$
>
> **Encontrar** $\frac{d}{dx}[x^x]$ para $x > 0$.
>
> 1. Sea $y = x^x$; entonces $\ln y = x \ln x$.
> 2. Derivando con la regla del producto: $\frac{1}{y}\frac{dy}{dx} = \ln x + x \cdot \frac{1}{x} = \ln x + 1$.
> 3. Resultado: $\frac{dy}{dx} = x^x(\ln x + 1)$.

> [!example] 🔢 Ejemplo 4: base y exponente variables
>
> **Encontrar** $\frac{d}{dx}[(x^2+1)^{\sin x}]$.
>
> 1. Sea $y = (x^2+1)^{\sin x}$; entonces $\ln y = \sin x \cdot \ln(x^2+1)$.
> 2. Derivando: $\frac{1}{y}\frac{dy}{dx} = \cos x \cdot \ln(x^2+1) + \sin x \cdot \frac{2x}{x^2+1}$.
> 3. Resultado:
>
> $$\frac{dy}{dx} = (x^2+1)^{\sin x}\left[\cos x \cdot \ln(x^2+1) + \frac{2x\sin x}{x^2+1}\right].$$

> [!example] 🔢 Ejemplo 5: múltiples raíces
>
> **Encontrar** $\frac{d}{dx}\left[\frac{\sqrt[3]{x^2+1}\sqrt{x-1}}{\sqrt[4]{x+3}}\right]$ para $x > 1$.
>
> 1. Sea $y = \frac{(x^2+1)^{1/3}(x-1)^{1/2}}{(x+3)^{1/4}}$; entonces $\ln y = \frac{1}{3}\ln(x^2+1) + \frac{1}{2}\ln(x-1) - \frac{1}{4}\ln(x+3)$.
> 2. Derivando: $\frac{1}{y}\frac{dy}{dx} = \frac{2x}{3(x^2+1)} + \frac{1}{2(x-1)} - \frac{1}{4(x+3)}$.
> 3. Resultado: $\frac{dy}{dx} = y \cdot \left[\frac{2x}{3(x^2+1)} + \frac{1}{2(x-1)} - \frac{1}{4(x+3)}\right]$.
>
> **Por qué importa:** convierte un problema de cálculo pesado en simple aritmética algebraica: sin $\ln$ serían tres reglas de la potencia y dos del cociente encadenadas.

### 🎓 Mnemotecnia "LDP-S"

> [!tip] 🎓 Los cuatro pasos del método
>
> - **L**ogaritmo natural a ambos lados.
> - **D**escomponer usando las propiedades del $\ln$.
> - **P**roducto o cociente $\rightarrow$ suma o resta.
> - **S**ustituir $y = f(x)$ al final.
>
> **Propiedades que hacen el trabajo:**
>
> $$\ln(AB) = \ln A + \ln B, \qquad \ln(A/B) = \ln A - \ln B, \qquad \ln(A^n) = n\ln A.$$
>
> **Por qué importa:** el paso D es el que ahorra todo el tiempo; si lo saltas, el método no gana nada sobre la regla del producto.
>
> **Ejemplo:** con $y = \sqrt{x}\sqrt[3]{x+1}$, el paso D da $\ln y = \frac{1}{2}\ln x + \frac{1}{3}\ln(x+1)$ y la derivada es $y\left[\frac{1}{2x} + \frac{1}{3(x+1)}\right]$.

---

## ✅ ¿Cuándo usar la técnica?

> [!note] 📈 Criterios de decisión
>
> **✅ SÍ usar derivación logarítmica cuando:**
>
> - **Productos de 3+ funciones:** $x^2(x+1)^3\sqrt{x-2}(x+5)^4$
> - **Cocientes complejos:** $\frac{x^3(x+1)^2\sqrt{x-5}}{(x-1)^4(x+3)^2}$
> - **Exponentes variables:** $x^x$, $(x^2+1)^{\sin x}$, $(\ln x)^{\cos x}$
> - **Raíces múltiples:** $\sqrt{x}\sqrt[3]{x+1}\sqrt[4]{x-2}$
>
> **❌ NO usar (los métodos directos son mejores):**
>
> - Productos simples de 2 funciones: $x^2 \sin x$
> - Funciones con exponente constante: $x^3$, $(\sin x)^2$
> - Funciones exponenciales simples: $e^x$, $2^x$
>
> **Por qué importa:** el criterio se decide **antes** de derivar. Los dos extremos cuestan tiempo: encadenar la regla del producto sobre seis factores, o tomar $\ln$ de un producto de dos donde el método directo es más rápido.

> [!note] 🖼️ Árbol de decisión: qué método toca
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Derivación_Logarítmica_03.svg]]
>
> **Se lee así:** Es un **árbol de decisión**: de una caja de entrada se llega a un rombo que pregunta cuántos factores multiplican o dividen. Con uno o dos, la rama baja a los métodos directos, producto o cociente; con tres o más, pasa a una caja que pregunta por los exponentes variables y desde ahí las ramas van a la derivación logarítmica obligatoria, la muy recomendada o la comparación entre métodos, según aparezcan o no raíces y potencias fraccionarias.
>
> **Por qué importa:** Te da el criterio antes de derivar y evita los dos extremos: encadenar la regla del producto sobre seis factores o aplicar logaritmos a un producto de dos, donde el método directo es más rápido.
>
> **Ejemplo:** Para $y = \sqrt{x}\sqrt[3]{x+1}\sqrt[4]{x+2}\sqrt[5]{x+3}$ la nota muestra que hay cuatro raíces, así que entras por la rama logarítmica y terminas sumando cuatro términos con $1/2$, $1/3$, $1/4$ y $1/5$.

> [!example] 🔢 Comparación directa: $\frac{d}{dx}[x(x+1)(x+2)(x+3)]$
>
> **Método 1 — expandir primero:** $x(x+1)(x+2)(x+3) = x^4 + 6x^3 + 11x^2 + 6x$, y derivar da $4x^3 + 18x^2 + 22x + 6$. Tiempo medio, requiere la expansión.
>
> **Método 2 — regla del producto directa:** $(x+1)(x+2)(x+3) + x(x+2)(x+3) + x(x+1)(x+3) + x(x+1)(x+2)$. Tiempo largo: cuatro términos complicados.
>
> **Método 3 — derivación logarítmica:**
>
> $$\ln y = \ln x + \ln(x+1) + \ln(x+2) + \ln(x+3), \qquad \frac{1}{y}\frac{dy}{dx} = \frac{1}{x} + \frac{1}{x+1} + \frac{1}{x+2} + \frac{1}{x+3}.$$
>
> **Por qué importa:** el método 3 es el más rápido y el más sistemático: el patrón es siempre el mismo, sin multiplicar binomios ni repetir la regla del producto cuatro veces.

> [!example] 🔢 Antes y después del $\ln$
>
> **Caso 1:** $y = \sqrt{x}\sqrt[3]{x+1}\sqrt[4]{x+2}\sqrt[5]{x+3}$. Sin logaritmos: regla del producto aplicada tres veces, cada término con múltiples raíces. Con logaritmos: $\ln y = \frac{1}{2}\ln x + \frac{1}{3}\ln(x+1) + \frac{1}{4}\ln(x+2) + \frac{1}{5}\ln(x+3)$. De pesadilla a trivial.
>
> **Caso 2:** $y = x^{\sin x}$. Sin logaritmos: imposible con las reglas básicas. Con logaritmos: $\ln y = \sin x \cdot \ln x$ y se deriva con la regla del producto. De imposible a rutinario.

---

## ⚠️ Errores comunes y cuidados

> [!warning] 🚨 Dominio, signos y formas indeterminadas
>
> - **Verifica que $f(x) > 0$** en el intervalo de trabajo; si puede ser negativa, escribe $\ln|f(x)|$ y el resultado sigue siendo válido.
> - **Cuidado con las discontinuidades:** donde $f(x) = 0$ el logaritmo no existe y la función puede cambiar de signo.
> - **Formas indeterminadas:** $0^0$, $\infty^0$ y $1^\infty$ no se derivan a ciegas; se resuelven con logaritmos y límites: [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]].
>
> **Por qué importa:** la técnica asume que el logaritmo está definido. Saltarse el análisis de dominio es la forma más rápida de aprobar un paso y equivocar el resultado completo.

> [!tip] 💡 Lista de verificación "PCEF"
>
> - **P**roducto de muchas funciones $\rightarrow$ ✅ usa $\ln$.
> - **C**ociente complejo $\rightarrow$ ✅ usa $\ln$.
> - **E**xponente variable $f(x)^{g(x)}$ $\rightarrow$ ✅ usa $\ln$ (obligatorio).
> - **F**unción simple $\rightarrow$ ❌ los métodos directos son mejores.
>
> **Por qué importa:** son cuatro letras para no confundir el momento de usar la técnica. El error clásico es aplicarla por inercia a un producto de dos factores.
>
> **Ejemplo:** $y = x^3$ cae en la F: $\frac{d}{dx}[x^3] = 3x^2$ directamente, sin tomar ningún logaritmo.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Producto de tres factores

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}\left[x^2(x+1)^3\sqrt{x-2}\right]$ para $x > 2$.
>
> > [!success]- ✅ Solución
> >
> > Sea $y = x^2(x+1)^3\sqrt{x-2}$. Aplicando $\ln$: $\ln y = 2\ln x + 3\ln(x+1) + \frac{1}{2}\ln(x-2)$.
> >
> > Derivando implícitamente: $\frac{1}{y}\frac{dy}{dx} = \frac{2}{x} + \frac{3}{x+1} + \frac{1}{2(x-2)}$.
> >
> > Multiplicando por $y$: $\frac{dy}{dx} = x^2(x+1)^3\sqrt{x-2}\left[\frac{2}{x} + \frac{3}{x+1} + \frac{1}{2(x-2)}\right]$.

### ✏️ Ejercicio 2 — Cociente con raíces

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}\left[\frac{x^3(x+1)^2}{\sqrt{x-1}(2x+3)^4}\right]$ para $x > 1$.
>
> > [!success]- ✅ Solución
> >
> > Sea $y = \frac{x^3(x+1)^2}{\sqrt{x-1}(2x+3)^4}$. Con $\ln$: $\ln y = 3\ln x + 2\ln(x+1) - \frac{1}{2}\ln(x-1) - 4\ln(2x+3)$.
> >
> > Derivando: $\frac{1}{y}\frac{dy}{dx} = \frac{3}{x} + \frac{2}{x+1} - \frac{1}{2(x-1)} - \frac{8}{2x+3}$ (el $\ln(2x+3)$ trae $4 \cdot \frac{2}{2x+3}$ por la cadena).
> >
> > Multiplicando por $y$: $\frac{dy}{dx} = y\left[\frac{3}{x} + \frac{2}{x+1} - \frac{1}{2(x-1)} - \frac{8}{2x+3}\right]$.

### ✏️ Ejercicio 3 — La potencia clásica $x^x$

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[x^x]$ para $x > 0$.
>
> > [!success]- ✅ Solución
> >
> > Sea $y = x^x$. Aplicando $\ln$: $\ln y = x \ln x$.
> >
> > Derivando con la regla del producto: $\frac{1}{y}\frac{dy}{dx} = 1 \cdot \ln x + x \cdot \frac{1}{x} = \ln x + 1$.
> >
> > Multiplicando por $y$: $\frac{dy}{dx} = x^x(\ln x + 1)$.

### ✏️ Ejercicio 4 — Base y exponente variables

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[(x^2+1)^{\sin x}]$.
>
> > [!success]- ✅ Solución
> >
> > Sea $y = (x^2+1)^{\sin x}$. Aplicando $\ln$: $\ln y = \sin x \cdot \ln(x^2+1)$.
> >
> > Derivando con la regla del producto: $\frac{1}{y}\frac{dy}{dx} = \cos x \cdot \ln(x^2+1) + \sin x \cdot \frac{2x}{x^2+1}$.
> >
> > Multiplicando por $y$: $\frac{dy}{dx} = (x^2+1)^{\sin x}\left[\cos x \cdot \ln(x^2+1) + \frac{2x\sin x}{x^2+1}\right]$.

### ✏️ Ejercicio 5 — Raíces combinadas

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}\left[\frac{\sqrt[3]{x^2+1}\sqrt{x-1}}{\sqrt[4]{x+3}}\right]$ para $x > 1$.
>
> > [!success]- ✅ Solución
> >
> > Sea $y = \frac{(x^2+1)^{1/3}(x-1)^{1/2}}{(x+3)^{1/4}}$. Aplicando $\ln$: $\ln y = \frac{1}{3}\ln(x^2+1) + \frac{1}{2}\ln(x-1) - \frac{1}{4}\ln(x+3)$.
> >
> > Derivando: $\frac{1}{y}\frac{dy}{dx} = \frac{1}{3} \cdot \frac{2x}{x^2+1} + \frac{1}{2(x-1)} - \frac{1}{4(x+3)}$.
> >
> > Multiplicando por $y$: $\frac{dy}{dx} = y\left[\frac{2x}{3(x^2+1)} + \frac{1}{2(x-1)} - \frac{1}{4(x+3)}\right]$.

### ✏️ Ejercicio 6 — Comparar con la regla del producto

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[x(x+1)(x+2)(x+3)]$ por dos métodos: regla del producto y derivación logarítmica. ¿Cuál es más corto?
>
> > [!success]- ✅ Solución
> >
> > **Logarítmico:** $\ln y = \ln x + \ln(x+1) + \ln(x+2) + \ln(x+3)$, luego $\frac{1}{y}\frac{dy}{dx} = \frac{1}{x} + \frac{1}{x+1} + \frac{1}{x+2} + \frac{1}{x+3}$ y $\frac{dy}{dx} = y\left[\frac{1}{x} + \frac{1}{x+1} + \frac{1}{x+2} + \frac{1}{x+3}\right]$.
> >
> > **Producto:** $(x+1)(x+2)(x+3) + x(x+2)(x+3) + x(x+1)(x+3) + x(x+1)(x+2)$, cuatro términos que hay que simplificar.
> >
> > Expandiendo el logarítmico: $\frac{dy}{dx} = 4x^3 + 18x^2 + 22x + 6$, idéntico al que sale de expandir primero. El logarítmico es más corto.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Reconozco cuándo conviene la derivación logarítmica y cuándo no.
> - [ ] Aplico los cuatro pasos LDP-S a un producto de tres o más factores.
> - [ ] Uso las propiedades del $\ln$ para descomponer productos, cocientes y raíces.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Derivo funciones de la forma $f(x)^{g(x)}$ como $x^x$ o $(x^2+1)^{\sin x}$.
> - [ ] Resuelvo cocientes complejos respetando el signo de cada factor.
> - [ ] Verifico el resultado sustituyendo un punto o comparando con otro método.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Decido entre método directo, regla del producto y logarítmico antes de empezar.
> - [ ] Combino derivación logarítmica con límites para resolver formas indeterminadas.
> - [ ] Analizo el dominio de $f(x)$ antes de tomar el logaritmo.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 3: derivación logarítmica.
> - R. Larson, *Cálculo* (Cengage), cap. 3: derivadas de productos y potencias variables.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — el paso "derivar implícitamente" viene de ahí.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — las propiedades que usas al descomponer el $\ln$.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es el orden de los pasos de la derivación logarítmica?::LDP-S: logaritmo a ambos lados, descomponer con las propiedades del $\ln$, derivar implícitamente y sustituir $y = f(x)$ al final.
> - ¿Qué propiedad convierte un producto en suma?::$\ln(AB) = \ln A + \ln B$; también $\ln(A/B) = \ln A - \ln B$ y $\ln(A^n) = n\ln A$.
> - ¿Cuál es la derivada de $x^x$?::$x^x(\ln x + 1)$, tomando $\ln y = x\ln x$ y derivando con la regla del producto.
> - ¿Por qué no sirve la regla de potencias en $f(x)^{g(x)}$?::Porque exige exponente constante; si el exponente depende de $x$, la única vía es la derivación logarítmica.
> - ¿Cómo se deriva un producto de cuatro factores con $\ln$?::Se suman cuatro logaritmos, la derivada es $y$ por la suma de $\frac{f_i'}{f_i}$, y el resultado se escribe otra vez con $y = f(x)$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — hace aparecer el $\frac{dy}{dx}$ al derivar el $\ln$.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — el motor implícito que sostiene toda la técnica.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] — la regla del producto que este método evita.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas|03 - Derivadas Trigonométricas, Exponenciales y Logarítmicas]] — las derivadas elementales que aparecen al expandir.
> - [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]] — donde la derivación logarítmica se combina con límites.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero con productos de tres factores: consolidas las propiedades del $\ln$ sin la carga algebraica de los cocientes.
> - Después salta a $f(x)^{g(x)}$ con casos cortos como $x^x$ y $2^{\sin x}$.
> - Cuando el enunciado traiga $1^\infty$ o $0^0$, combina la técnica con [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]].
> - Para decidir entre métodos, repasa [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]] y aplica el árbol de decisión de esta nota.

---

**Tags:** #MATG1045 #unidad4 #derivacion-logaritmica #calculo #derivadas #funciones-exponenciales #regla-cadena #productos-complejos #exponentes-variables

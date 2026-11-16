---
dg-publish: true
tags: [MATG1045, unidad6, integrales-notables, formulas-directas, regla-potencia, integrales-trigonometricas, integrales-inversas, integrales-hiperbolicas]
---

# 🧮 Integrales Notables (Fórmulas Directas)

## 🎯 Introducción

> [!info] 💡 Qué son las integrales notables
>
> Las **integrales notables** (o **integrales inmediatas**) se resuelven aplicando directamente las fórmulas básicas de integración, sin técnicas como sustitución, partes o fracciones parciales. Se basan en el teorema fundamental: si $F'(x) = f(x)$, entonces $\int f(x)\,dx = F(x) + C$, y en el principio de linealidad $\int [af + bg]\,dx = a\int f\,dx + b\int g\,dx$.
>
> **Por qué importa:** son el repertorio que hay que tener automatizado. Cada técnica avanzada termina reduciendo el problema a una de estas fórmulas; si no las dominas, cada ejercicio exige volver a deducir lo básico.
>
> **Ejemplo:** $\int (3x^2 - 5\operatorname{sen} x + 2e^x)\,dx$ se resuelve con tres filas de la tabla: $x^3 + 5\cos x + 2e^x + C$.

> [!warning] ⚠️ Los tres errores que más se repiten
>
> 1. **NO** olvides el valor absoluto en $\ln|x|$: sin él la fórmula es inválida para $x < 0$.
> 2. **NO** apliques la regla de potencia con $n = -1$: ese caso es $\ln|x| + C$.
> 3. **NO** te saltes la verificación derivando: una fila mal recordada produce un error que se propaga a todo el ejercicio.
>
> **Por qué importa:** los tres son errores de memoria y de dominio; una derivada de control los detecta en segundos.

---

## 📋 Definiciones Formales

> [!note] 📋 Regla de la potencia y su excepción
>
> Para cualquier $n \neq -1$:
>
> $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C.$$
>
> El caso $n = -1$ es distinto: $\displaystyle\int \frac{1}{x}\,dx = \ln|x| + C$, válida para $x \neq 0$ (y en intervalos donde $x>0$ se escribe $\ln x + C$; donde $x<0$, $\ln(-x) + C$).
>
> **Por qué importa:** es la fórmula más usada de toda la tabla, y su excepción es la trampa clásica del examen: dividir entre $n+1 = 0$ no existe.
>
> **Ejemplo:** $\int x^3\,dx = \frac{x^4}{4} + C$; $\int \sqrt{x}\,dx = \int x^{1/2}\,dx = \frac{2x^{3/2}}{3} + C$; $\int \frac{1}{x^2}\,dx = -\frac{1}{x} + C$.

> [!note] 📋 Definición — Las veinte fórmulas directas
>
> El catálogo completo está en la tabla de la casa, agrupado por familias: algebraicas, exponenciales, trigonométricas, inversas e hiperbólicas.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/cal1-integrales-tabla-20-notables.jpg]]
>
> **Se lee así:** una tabla vertical de veinte filas numeradas: el símbolo integral abre cada fila, el integrando va al centro y la antiderivada termina a la derecha con su constante de integración. Las filas se agrupan por familias, primero las algebraicas, luego las exponenciales, las trigonométricas, las inversas y al final las hiperbólicas. No hay flechas ni decisiones, es un **catálogo** para consultar en orden.
>
> **Por qué importa:** tenerlas numeradas y juntas ahorra buscar cada fórmula en la nota mientras resuelves. Funciona como **lista de control**: si reconoces la forma del integrando, la fila te dice qué fórmula aplicar y con qué restricciones de dominio.
>
> **Ejemplo:** con $\int \frac{4}{x^2+9}\,dx$ buscas la fila de la integral arctangente y aplicas $\frac{1}{a}\arctan(x/a) + C$ con $a = 3$, y sale $\frac{4}{3}\arctan(x/3) + C$.

---

## 🗺️ Las familias de integrales directas

> [!info] 🖼️ Cómo se organiza el catálogo
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Integrales_Notables_(Fórmulas_Directas)_01.svg]]
>
> **Se lee así:** un árbol de decisión que arranca en la integral inmediata y pregunta por la **forma del integrando**. Se abren seis ramas: potencia $x^n$ (que a su vez bifurca en $n \neq -1$ y el caso logarítmico), recíproco $1/x$, exponencial, trigonométrica (tres subramas: par directo, producto y cociente), racional con radical (arcseno o arctangente). Todas las ramas convergen en tres casillas finales encadenadas: aplicar linealidad, añadir la constante $C$ y verificar derivando.
>
> **Por qué importa:** el diagrama convierte la tabla en un **procedimiento**: primero clasificas la forma, luego aplicas la fila, luego combinas con linealidad y cierras con la verificación. Las tres casillas finales son obligatorias en cualquier ejercicio.
>
> **Ejemplo:** $\int \frac{3}{\sqrt{1 - x^2}}\,dx$ cae en la rama de radical → arcoseno, y da $3\arcsin x + C$.

> [!tip] 🔧 Los cuatro pasos de resolución
>
> 1. **Identificar:** reconocer la forma (algebraica, trigonométrica, exponencial…).
> 2. **Preparar:** extraer constantes y reescribir en forma estándar ($\sqrt{x} = x^{1/2}$, $\frac{3}{x^3} = 3x^{-3}$).
> 3. **Aplicar:** usar la fila correspondiente de la tabla, con su $+C$.
> 4. **Verificar:** derivar el resultado y comprobar restricciones de dominio.
>
> **Por qué importa:** el paso 2 es el que más ahorra tiempo: casi ningún integrando llega en forma estándar.
>
> **Ejemplo:** $\int \frac{4}{x^2 + 9}\,dx$ requiere reescribirse como $4\int \frac{1}{x^2 + 3^2}\,dx$ antes de poder usar la fila de arctangente con $a = 3$.

---

## 🔢 Integrales algebraicas y exponenciales

> [!success] ✅ Las cinco primeras
>
> 1. $\displaystyle\int dx = x + C$
> 2. $\displaystyle\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$, $n \neq -1$
> 3. $\displaystyle\int \frac{1}{x}\,dx = \ln|x| + C$
> 4. $\displaystyle\int e^x\,dx = e^x + C$
> 5. $\displaystyle\int a^x\,dx = \frac{a^x}{\ln a} + C$, con $a > 0$ y $a \neq 1$ (casos: $\int 2^x\,dx = \frac{2^x}{\ln 2} + C$, $\int 10^x\,dx = \frac{10^x}{\ln 10} + C$)
>
> **Por qué importa:** la 4 es la única función igual a su propia derivada, y la 5 solo se distingue de ella por el factor $\ln a$ en el denominador.
>
> **Ejemplo:** la demostración de la 5 es directa: $a^x = e^{x\ln a}$, y derivando $\frac{e^{x\ln a}}{\ln a}$ se recupera $a^x$ ✓

---

## 📐 Integrales trigonométricas

> [!success] ✅ Las doce trigonométricas
>
> **Par directo:**
>
> 6. $\displaystyle\int \operatorname{sen} x\,dx = -\cos x + C$ (¡con signo menos!)
> 7. $\displaystyle\int \cos x\,dx = \operatorname{sen} x + C$
> 8. $\displaystyle\int \sec^2 x\,dx = \tan x + C$
> 9. $\displaystyle\int \csc^2 x\,dx = -\cot x + C$
>
> **Producto:**
>
> 10. $\displaystyle\int \sec x \tan x\,dx = \sec x + C$
> 11. $\displaystyle\int \csc x \cot x\,dx = -\csc x + C$
>
> **Cociente (dan logaritmos):**
>
> 12. $\displaystyle\int \tan x\,dx = -\ln|\cos x| + C = \ln|\sec x| + C$
> 13. $\displaystyle\int \cot x\,dx = \ln|\operatorname{sen} x| + C$
> 14. $\displaystyle\int \sec x\,dx = \ln|\sec x + \tan x| + C$
> 15. $\displaystyle\int \csc x\,dx = \ln|\csc x - \cot x| + C$
>
> **Por qué importa:** las de cociente son las que menos se recuerdan porque no siguen el patrón de las demás: tangente, cotangente, secante y cosecante se integran con logaritmos.
>
> **Ejemplo:** $\int \tan x\,dx$ se hace con $u = \cos x$: $\int \frac{-\sin x}{\cos x}\,dx = -\ln|\cos x| + C$.

---

## 🔄 Integrales inversas e hiperbólicas

> [!success] ✅ Las tres inversas
>
> 16. $\displaystyle\int \frac{1}{\sqrt{a^2 - x^2}}\,dx = \arcsin\!\left(\frac{x}{a}\right) + C$, requiere $|x| < a$
> 17. $\displaystyle\int \frac{1}{a^2 + x^2}\,dx = \frac{1}{a}\arctan\!\left(\frac{x}{a}\right) + C$
> 18. $\displaystyle\int \frac{1}{x\sqrt{x^2 - a^2}}\,dx = \frac{1}{a}\arcsin\!\left(\frac{|x|}{a}\right) + C$, requiere $|x| > a$
>
> **Por qué importa:** la restricción de dominio no es decorativa: el denominador tiene que ser real y distinto de cero, y por eso cada fórmula exige su intervalo.
>
> **Ejemplo:** $\int \frac{1}{9 + x^2}\,dx$ con $a = 3$ da $\frac{1}{3}\arctan\!\left(\frac{x}{3}\right) + C$.

> [!success] ✅ Las dos hiperbólicas
>
> 19. $\displaystyle\int \operatorname{senh} x\,dx = \cosh x + C$
> 20. $\displaystyle\int \cosh x\,dx = \operatorname{senh} x + C$
>
> A diferencia de las trigonométricas, aquí **no hay signo menos**: la derivada de $\cosh$ es $\operatorname{senh}$ y viceversa, sin rotación de signo.
>
> **Por qué importa:** es la diferencia que confunde a quien memoriza las trigonométricas y las transfiere sin más.
>
> **Ejemplo:** $\int \cosh x\,dx = \operatorname{senh} x + C$, verificando: $\frac{d}{dx}\operatorname{senh} x = \cosh x$ ✓

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los seis fallos típicos
>
> 1. **Signo del seno:** $\int \operatorname{sen} x\,dx = -\cos x + C$.
> 2. **Valor absoluto ausente** en $\ln|x|$ y en las antiderivadas logarítmicas.
> 3. **Dominios sin comprobar:** $\arcsin(x/a)$ exige $|x| < a$; la forma con $\sqrt{x^2 - a^2}$ exige $|x| > a$.
> 4. **Una $C$ por término:** al sumar integrales, $C_1 + C_2$ se combina en una sola $C$.
> 5. **Olvidar el $\frac{1}{\ln a}$** en $\int a^x\,dx$.
> 6. **No reescribir el integrando:** potencias negativas y fraccionarias, radicales y constantes deben normalizarse antes de aplicar la fila.
>
> **Por qué importa:** los seis son de planteamiento y se detectan con la verificación por derivación, que debería ser el paso final automático de cualquier ejercicio.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $\int (3x^2 - 5\operatorname{sen} x + 2e^x)\,dx$.
>
> > [!success]- ✅ Solución
> > 
> > Por linealidad, tres filas de la tabla:
> > 
> > $$3\int x^2\,dx - 5\int \operatorname{sen} x\,dx + 2\int e^x\,dx = 3\cdot\frac{x^3}{3} - 5(-\cos x) + 2e^x + C$$
> > 
> > **Respuesta:** $x^3 + 5\cos x + 2e^x + C$.
> > 
> > Verificación: $\frac{d}{dx}(x^3 + 5\cos x + 2e^x) = 3x^2 - 5\operatorname{sen} x + 2e^x$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \frac{4}{x^2 + 9}\,dx$.
>
> > [!success]- ✅ Solución
> > 
> > Se saca la constante y se lleva a forma estándar:
> > 
> > $$4\int \frac{1}{x^2 + 3^2}\,dx.$$
> > 
> > Con la fila de arctangente ($a = 3$): $\frac{1}{a}\arctan(x/a) + C$.
> > 
> > **Respuesta:** $\dfrac{4}{3}\arctan\!\left(\dfrac{x}{3}\right) + C$.
> > 
> > Verificación: $\frac{d}{dx}\left[\frac{4}{3}\arctan\frac{x}{3}\right] = \frac{4}{3}\cdot\frac{1}{1 + (x/3)^2}\cdot\frac{1}{3} = \frac{4}{9 + x^2}$ ✓

> [!example] 📋 Planteamiento
>
> Integra $\int \left(2\sqrt{x} - \dfrac{3}{x^3}\right)dx$.
>
> > [!success]- ✅ Solución
> > 
> > Primero forma estándar: $2x^{1/2} - 3x^{-3}$.
> > 
> > $$2\cdot\frac{x^{3/2}}{3/2} - 3\cdot\frac{x^{-2}}{-2} + C = \frac{4}{3}x^{3/2} + \frac{3}{2x^2} + C.$$
> > 
> > **Respuesta:** $\dfrac{4}{3}x\sqrt{x} + \dfrac{3}{2x^2} + C$.
> > 
> > Verificación: $\frac{d}{dx}\left[\frac{4}{3}x^{3/2}\right] = 2x^{1/2}$ y $\frac{d}{dx}\left[\frac{3}{2}x^{-2}\right] = -3x^{-3}$ ✓

> [!example] 📋 Planteamiento
>
> Calcula $\int \frac{dx}{\sqrt{4 - x^2}}$ y justifica el dominio de la fórmula usada.
>
> > [!success]- ✅ Solución
> > 
> > Con $a = 2$ en la fila de arcseno: $\int \frac{1}{\sqrt{a^2 - x^2}}\,dx = \arcsin(x/a) + C$.
> > 
> > **Respuesta:** $\arcsin\!\left(\dfrac{x}{2}\right) + C$, válida para $|x| < 2$ (ahí el radicando es positivo y el denominador no se anula).
> > 
> > Verificación: $\frac{d}{dx}\arcsin(x/2) = \frac{1}{\sqrt{1 - (x/2)^2}}\cdot\frac{1}{2} = \frac{1}{\sqrt{4 - x^2}}$ ✓

> [!example] 📋 Planteamiento
>
> Resuelve $\int \tan x\,dx$ y $\int \sec x\,dx$ mostrando el paso de logaritmo.
>
> > [!success]- ✅ Solución
> > 
> > **Tangente:** $\int \frac{\operatorname{sen} x}{\cos x}\,dx$ con $u = \cos x$, $du = -\operatorname{sen} x\,dx$:
> > 
> > $$-\int \frac{du}{u} = -\ln|u| + C = -\ln|\cos x| + C = \ln|\sec x| + C.$$
> > 
> > **Secante:** multiplicando y dividiendo por $\sec x + \tan x$:
> > 
> > $$\int \sec x\,dx = \int \frac{\sec^2 x + \sec x\tan x}{\sec x + \tan x}\,dx = \ln|\sec x + \tan x| + C.$$
> > 
> > **Respuesta:** $-\ln|\cos x| + C$ y $\ln|\sec x + \tan x| + C$.

> [!example] 📋 Planteamiento
>
> Integra $\displaystyle\int \left(\frac{1}{x} + 3^x - \csc^2 x + \frac{1}{\sqrt{x}}\right)dx$ y verifica.
>
> > [!success]- ✅ Solución
> > 
> > Cuatro filas distintas:
> > 
> > $$\ln|x| + \frac{3^x}{\ln 3} + \cot x + 2\sqrt{x} + C.$$
> > 
> > **Respuesta:** $\ln|x| + \dfrac{3^x}{\ln 3} + \cot x + 2\sqrt{x} + C$.
> > 
> > Verificación: $\frac{1}{x} + 3^x - \csc^2 x + x^{-1/2}$ ✓ (el signo de $\cot$ y el de $\csc^2$ son los que más se olvidan).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo de memoria las fórmulas algebraicas y exponenciales con sus restricciones ($n \neq -1$, $a > 0$, $a \neq 1$).
> - [ ] Distingo $\int \operatorname{sen} x\,dx = -\cos x + C$ de $\int \cos x\,dx = \operatorname{sen} x + C$ sin dudar.
> - [ ] Siempre incluyo el valor absoluto en los logaritmos y la constante $C$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Reescribo el integrando en forma estándar (potencias negativas, fraccionarias, radicales) antes de aplicar la tabla.
> - [ ] Aplico la linealidad para partir una integral combinada en varias fórmulas directas.
> - [ ] Elijo la fila correcta clasificando la forma: potencia, recíproco, exponencial, trigonométrica o racional con radical.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo las integrales de tangente, cotangente, secante y cosecante mostrando el paso de logaritmo.
> - [ ] Justifico el intervalo de validez de cada fórmula inversa a partir del dominio.
> - [ ] Verifico cualquier resultado derivando y corrijo el error que encuentre.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4.1: fórmulas de integración.
> - R. Larson, *Cálculo* (Cengage), cap. 5.1: tabla de integrales.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 5: inmediatas.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — la regla de potencia y la notación.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración|03 - Constante de integración]] — la $C$ que siempre se añade.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la Parte II que convierte estas antiderivadas en números.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la regla de la potencia?::$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$ para $n \neq -1$; si $n = -1$ la respuesta es $\ln|x| + C$.
> - ¿Cómo se integra el seno?::$\int \operatorname{sen} x\,dx = -\cos x + C$: con signo menos, al revés que el coseno.
> - ¿Qué da la integral de $a^x$?::$\frac{a^x}{\ln a} + C$, con $a > 0$ y $a \neq 1$; solo para $a = e$ no aparece el logaritmo.
> - ¿Cuáles dan logaritmos entre las trigonométricas?::Tangente, cotangente, secante y cosecante: $\int \tan x\,dx = -\ln|\cos x| + C$ es la más usada.
> - ¿Cuándo se usa la fila de arcseno?::En $\frac{1}{\sqrt{a^2 - x^2}}$ con $|x| < a$; la de arctangente va en $\frac{1}{a^2 + x^2}$ sin restricción.
> - ¿Qué tres pasos cierran cualquier integral directa?::Aplicar la fila con su $+C$, combinar por linealidad y verificar derivando el resultado.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/01 - Antiderivadas (Primitivas)|01 - Antiderivadas (Primitivas)]] — de donde salen estas fórmulas como casos particulares.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración|03 - Constante de integración]] — la $C$ obligatoria en todas las respuestas.
> - [[Unidad 6 - Integrales/II - Integrales Indefinidas/02 - Identidades Trigonométricas para Integrales|02 - Identidades Trigonométricas para Integrales]] — cuando el integrando no llega en forma estándar, la identidad lo prepara.
> - [[Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales|01 - Cambio de Variable en Integrales]] — lo que toca cuando la tabla no alcanza.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/03 - Tabla de Derivadas Básicas|03 - Tabla de Derivadas Básicas]] — la tabla inversa de la que estas fórmulas salen.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — el teorema que hace útil todo el catálogo.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 3: linealidad y forma estándar, los dos pasos previos a cualquier fila.
> - Después salta al 2 y al 4, donde entran las fórmulas inversas con sus dominios.
> - Cuando lo tengas, ataca el 5, que muestra el paso de logaritmo de las cuatro trigonométricas difíciles.
> - Cierra con [[Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales|Cambio de Variable en Integrales]], para cuando el integrando no coincida con ninguna fila.

---

**Tags:** #MATG1045 #unidad6 #integrales-notables #formulas-directas #regla-potencia #integrales-trigonometricas #integrales-inversas #integrales-hiperbolicas

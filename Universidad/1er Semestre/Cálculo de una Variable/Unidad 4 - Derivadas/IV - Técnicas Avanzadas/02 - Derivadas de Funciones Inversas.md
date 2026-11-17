---
dg-publish: true
tags: [MATG1045, unidad4, funciones-inversas, arctan, arcsen, logaritmo, derivacion-implicita, regla-cadena, identidades-trigonometricas]
---

# 🔄 Derivadas de Funciones Inversas

## 🎯 Introducción

> [!info] 💡 Qué resuelve esta técnica
>
> Las **derivadas de funciones inversas** permiten hallar la derivada de $f^{-1}$ **conociendo la derivada de $f$**. Con eso se derivan $\arcsin$, $\arctan$, $\ln$ y cualquier otra inversa, sin memorizar cada caso por separado.
>
> **Por qué importa:** el método es uno solo y se deduce de la derivación implícita. Además explica la geometría: las gráficas de $f$ y $f^{-1}$ son simétricas respecto de $y = x$, y sus pendientes son **recíprocas**.
>
> **Ejemplo:** para derivar $y = \arctan(x)$ se escribe $x = \tan(y)$, se deriva de forma implícita y se despeja: $\frac{dy}{dx} = \frac{1}{1+x^2}$.

> [!warning] ⚠️ El error que cuesta puntos
>
> - **NO** escribas $(f^{-1})'(x) = \frac{1}{f'(x)}$: lo correcto es $(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$. La composición con la inversa no se puede quitar.
> - **NO** olvides el **valor absoluto** en $\operatorname{arcsec}$ y $\operatorname{arccsc}$.
> - **NO** ignores el **rango** de cada inversa: es lo que fija el signo de la raíz cuadrada.
>
> **Por qué importa:** los tres son errores de planteamiento; corregirlos antes de calcular evita rehacer la solución entera.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Derivada de la función inversa
>
> Si $f$ es **biyectiva** (por tanto tiene función inversa $f^{-1}$) y $f'$ no se anula en el punto, entonces:
>
> $$\frac{d}{dx}\big[f^{-1}(x)\big] = \frac{1}{f'\big(f^{-1}(x)\big)}.$$
>
> **Forma equivalente:** si $y = f^{-1}(x)$, entonces $x = f(y)$; derivando implícitamente, $1 = f'(y)\frac{dy}{dx}$, de donde $\frac{dy}{dx} = \frac{1}{f'(y)}$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Derivadas_de_Funciones_Inversas_01.svg]]
>
> **Se lee así:** es una cadena vertical de rectángulos, sin rombos: cada paso depende del anterior. Se parte de tener una función invertible y su derivada, se pasa por el objetivo de hallar la derivada de la inversa, se usa la equivalencia que intercambia $x$ e $y$, se deriva esa relación de forma implícita, se despeja el cociente y se termina sustituyendo para dejar todo en función de $x$.
>
> **Por qué importa:** te da la ruta para derivar $\arcsin$, $\arctan$ o $\ln$ sin memorizar cada caso: inviertes la función, derivas y despejas. Además evita el error de escribir $\frac{1}{f'(x)}$, que **no es lo mismo**.
>
> **Ejemplo:** para $y = \arctan(x)$ usas $x = \tan(y)$, obtienes $\frac{dy}{dx} = \frac{1}{\sec^2(y)}$ y, con $1 + \tan^2(y) = \sec^2(y)$, llegas a $\frac{1}{1+x^2}$.

> [!info] 🔍 Justificación geométrica
>
> Si $(a, b)$ está en la gráfica de $f$, entonces $(b, a)$ está en la gráfica de $f^{-1}$, porque las dos gráficas son simétricas respecto de $y = x$.
>
> - La pendiente de $f$ en $(a, b)$ es $f'(a)$.
> - La pendiente de $f^{-1}$ en $(b, a)$ es $(f^{-1})'(b)$.
> - Al reflejar, los segmentos de la recta tangente intercambian su papel horizontal y vertical, de modo que las pendientes son **recíprocas**: $(f^{-1})'(b) = \frac{1}{f'(a)}$.
>
> **Por qué importa:** la geometría explica el recíproco sin álgebra: una recta de pendiente $m$ se refleja en $y = x$ y pasa a tener pendiente $1/m$.

---

## 🧮 Derivadas de las inversas fundamentales

> [!example] 🔢 El logaritmo natural y el logaritmo en base $a$
>
> **Para $\ln x$:** sea $y = \ln x$, entonces $x = e^y$; como $\frac{d}{dx}e^y = e^y\frac{dy}{dx}$,
>
> $$1 = e^y\frac{dy}{dx} \quad \Rightarrow \quad \frac{dy}{dx} = \frac{1}{e^y} = \frac{1}{x}.$$
>
> **Para $\log_a x$ (con $a > 0$, $a \neq 1$):** sea $y = \log_a x$, entonces $x = a^y$; como $\frac{d}{dx}a^y = a^y\ln(a)\frac{dy}{dx}$,
>
> $$1 = a^y\ln(a)\frac{dy}{dx} \quad \Rightarrow \quad \frac{dy}{dx} = \frac{1}{a^y\ln(a)} = \frac{1}{x\ln(a)}.$$
>
> **Por qué importa:** el $\ln(a)$ aparece porque derivar $a^y$ trae un factor $\ln(a)$ que la cadena de la inversa debe "devolver".

> [!example] 🔢 La arcotangente
>
> **Encontrar** $\frac{d}{dx}[\arctan(x)]$.
>
> - Sea $y = \arctan(x)$, entonces $x = \tan(y)$ con $y \in (-\frac{\pi}{2}, \frac{\pi}{2})$.
> - $\frac{dy}{dx} = \frac{1}{\sec^2(y)}$.
> - Con $1 + \tan^2(y) = \sec^2(y)$ y $\tan(y) = x$: $\sec^2(y) = 1 + x^2$.
>
> **Resultado:** $\frac{d}{dx}[\arctan(x)] = \frac{1}{1+x^2}$.

> [!example] 🔢 El arcoseno
>
> **Encontrar** $\frac{d}{dx}[\arcsin(x)]$.
>
> - Sea $y = \arcsin(x)$, entonces $x = \operatorname{sen}(y)$ con $y \in [-\frac{\pi}{2}, \frac{\pi}{2}]$.
> - $\frac{dy}{dx} = \frac{1}{\cos(y)}$.
> - Como $\cos^2(y) = 1 - \operatorname{sen}^2(y) = 1 - x^2$ y en ese rango $\cos(y) \ge 0$, entonces $\cos(y) = \sqrt{1-x^2}$.
>
> **Resultado:** $\frac{d}{dx}[\arcsin(x)] = \frac{1}{\sqrt{1-x^2}}$.
>
> **Por qué importa:** fíjate en que el **rango** de la inversa decide el signo de la raíz: sin ese dato, $\cos(y) = \pm\sqrt{1-x^2}$ y la derivada quedaría ambigua.

> [!info] 📋 Tabla de inversas trigonométricas
>
> | Función | Derivada | Dominio | Observaciones |
> |---|---|---|---|
> | $\arcsin(x)$ | $\frac{1}{\sqrt{1-x^2}}$ | $(-1, 1)$ | Indefinida en $x = \pm 1$ |
> | $\arccos(x)$ | $-\frac{1}{\sqrt{1-x^2}}$ | $(-1, 1)$ | El signo es negativo |
> | $\arctan(x)$ | $\frac{1}{1+x^2}$ | $\mathbb{R}$ | Definida para todo real |
> | $\operatorname{arccot}(x)$ | $-\frac{1}{1+x^2}$ | $\mathbb{R}$ | El signo es negativo |
> | $\operatorname{arcsec}(x)$ | $\frac{1}{\lvert x\rvert\sqrt{x^2-1}}$ | $(-\infty,-1) \cup (1,\infty)$ | El valor absoluto es indispensable |
> | $\operatorname{arccsc}(x)$ | $-\frac{1}{\lvert x\rvert\sqrt{x^2-1}}$ | $(-\infty,-1) \cup (1,\infty)$ | Valor absoluto y signo negativo |
>
> **Por qué importa:** los signos no son caprichos: $\arcsin$ y $\arctan$ son crecientes (derivada positiva) y $\arccos$ y $\operatorname{arccot}$ son decrecientes (derivada negativa). Lo que hay que memorizar es el **carácter** de cada función, no la fórmula suelta.

---

## 🔧 Método general

> [!info] 🖼️ Proceso sistemático
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Derivadas_de_Funciones_Inversas_02.svg]]
>
> **Se lee así:** es una **cadena de siete rectángulos**, sin rombos, donde cada paso depende del anterior: se parte de la inversa, se escriben las variables, se invierte la relación, se deriva de forma implícita, se despeja la derivada, se reescribe todo en función de $x$ y se cierra con la simplificación final.
>
> **Por qué importa:** el orden importa: primero se invierte y se deriva, y solo al final se simplifica. Seguir esta ruta da el mismo resultado que memorizar $\arcsin$ o $\operatorname{arcsec}$ por separado, y evita el error de escribir $\frac{1}{f'(x)}$ en vez de $\frac{1}{f'(f^{-1}(x))}$.
>
> **Ejemplo:** para $y = \operatorname{arcsec}(x)$ recorres la cadena: escribes $x = \sec(y)$, derivas, despejas $\frac{dy}{dx} = \frac{1}{\sec(y)\tan(y)}$ y, con $1 + \tan^2(y) = \sec^2(y)$, llegas a $\frac{1}{\lvert x\rvert\sqrt{x^2-1}}$.

> [!example] 🔢 Caso con valor absoluto: $\operatorname{arcsec}(x)$
>
> - Sea $y = \operatorname{arcsec}(x)$, entonces $x = \sec(y)$ con $y \in [0, \pi]$, $y \neq \frac{\pi}{2}$.
> - $\frac{dy}{dx} = \frac{1}{\sec(y)\tan(y)}$.
> - De $\sec(y) = x$ y $\tan^2(y) = \sec^2(y) - 1 = x^2 - 1$ se obtiene $\tan(y) = \pm\sqrt{x^2-1}$.
> - **Determinar el signo:** en $[0, \frac{\pi}{2})$ ambos $\sec$ y $\tan$ son positivos; en $(\frac{\pi}{2}, \pi]$ ambos son negativos. En los dos casos el **producto** es positivo: $\sec(y)\tan(y) = \lvert x\rvert\sqrt{x^2-1}$.
>
> **Resultado:** $\frac{d}{dx}[\operatorname{arcsec}(x)] = \frac{1}{\lvert x\rvert\sqrt{x^2-1}}$.
>
> **Por qué importa:** el valor absoluto aparece porque el producto de dos factores que cambian de signo a la vez **no** cambia de signo; se escribe $\lvert x\rvert$ y no $x$.

> [!example] 🔢 Función inversa definida por el usuario
>
> **Encontrar** $\frac{d}{dx}[f^{-1}(x)]$ si $f(x) = x^3 + 2x + 1$.
>
> - $f'(x) = 3x^2 + 2$.
> - Sea $y = f^{-1}(x)$; entonces $f(y) = x$ y $\frac{dy}{dx} = \frac{1}{f'(y)} = \frac{1}{3y^2 + 2}$.
> - Sustituyendo $y = f^{-1}(x)$: $\frac{d}{dx}[f^{-1}(x)] = \frac{1}{3[f^{-1}(x)]^2 + 2}$.
>
> **Nota:** no se puede simplificar más sin conocer la forma explícita de $f^{-1}(x)$ (y aquí ni se puede despejar cómodamente). **Eso es normal:** la fórmula deja la respuesta en términos de la inversa.
>
> **Por qué importa:** cuando el enunciado pide $(f^{-1})'(a)$ en un punto concreto, basta con buscar $b$ tal que $f(b) = a$ y aplicar $\frac{1}{f'(b)}$.

---

## 🔄 Aplicaciones

> [!example] 🔢 Composiciones con regla de la cadena
>
> - $\frac{d}{dx}[\arcsin(2x)] = \frac{1}{\sqrt{1-(2x)^2}}\cdot 2 = \frac{2}{\sqrt{1-4x^2}}$, con dominio $x \in (-\frac{1}{2}, \frac{1}{2})$.
> - $\frac{d}{dx}[\ln(\operatorname{sen} x)] = \frac{1}{\operatorname{sen}x}\cos x = \cot(x)$, con dominio $\operatorname{sen}x > 0$.
>
> **Por qué importa:** la cadena no cambia nada del método: se deriva la función "de fuera" (que es una inversa) y se multiplica por la derivada de "adentro".

> [!example] 🔢 Derivación implícita con inversas
>
> **Encontrar** $\frac{dy}{dx}$ si $\arctan(xy) + \ln(x^2 + y^2) = \frac{\pi}{4}$.
>
> - Derivando ambos lados: $\frac{1}{1+(xy)^2}\left(y + x\frac{dy}{dx}\right) + \frac{1}{x^2+y^2}\left(2x + 2y\frac{dy}{dx}\right) = 0$.
> - Agrupando los términos con $\frac{dy}{dx}$:
>
> $$\left(\frac{x}{1+x^2y^2} + \frac{2y}{x^2+y^2}\right)\frac{dy}{dx} = -\left(\frac{y}{1+x^2y^2} + \frac{2x}{x^2+y^2}\right).$$
>
> - Despejando:
>
> $$\frac{dy}{dx} = -\frac{\dfrac{y}{1+x^2y^2} + \dfrac{2x}{x^2+y^2}}{\dfrac{x}{1+x^2y^2} + \dfrac{2y}{x^2+y^2}}.$$
>
> **Por qué importa:** cuando la inversa aparece dentro de una igualdad, la regla de la cadena se aplica **por dentro**: la derivada de $\arctan(xy)$ incluye el factor $y + x\frac{dy}{dx}$, que es justamente la clave para despejar.

---

## ⚠️ Errores comunes y estrategias

> [!warning] 🚨 Errores frecuentes
>
> **Conceptuales:**
>
> - Confundir función e inversa: $(f^{-1})'(x) \neq \frac{1}{f'(x)}$.
> - Olvidar los dominios: las inversas trigonométricas los tienen restringidos.
> - Signos incorrectos, sobre todo en $\arccos$ y $\operatorname{arccot}$.
>
> **De cálculo:**
>
> - No usar el valor absoluto en $\operatorname{arcsec}$ y $\operatorname{arccsc}$.
> - Aplicar mal las identidades: $\cos^2(y) + \operatorname{sen}^2(y) = 1$.
> - Usar rangos incorrectos: cada inversa tiene su rango, y de él depende el signo de la raíz.
>
> **Estrategia de éxito:**
>
> 1. Identificar la función directa $f(x)$.
> 2. Calcular $f'(x)$.
> 3. Aplicar $(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$.
> 4. Simplificar con identidades y comprobar el dominio.

> [!tip] 🎓 Mnemotecnias y plantilla mental
>
> **Signos (arcsen y arcsec positivos; arccos y arccot negativos):**
>
> - **A**rcsen: $+\frac{1}{\sqrt{1-x^2}}$ ✅
> - **S**ec: $+\frac{1}{\lvert x\rvert\sqrt{x^2-1}}$ ✅
> - **A**rccos: $-\frac{1}{\sqrt{1-x^2}}$ ❌
> - **C**sc: $-\frac{1}{\lvert x\rvert\sqrt{x^2-1}}$ ❌
> - **T**an: $+\frac{1}{1+x^2}$ ✅
> - **C**ot: $-\frac{1}{1+x^2}$ ❌
>
> **Fórmula maestra:** *"uno sobre f prima de f inversa"*.
>
> **Identidades clave:**
>
> - $\operatorname{sen}^2 y + \cos^2 y = 1$ → $\cos y = \sqrt{1 - \operatorname{sen}^2 y}$.
> - $1 + \tan^2 y = \sec^2 y$ → $\sec y = \sqrt{1 + \tan^2 y}$.
> - $\sec^2 y - 1 = \tan^2 y$ → $\tan y = \sqrt{\sec^2 y - 1}$.
>
> **Plantilla mental:**
>
> 1. ¿Es una inversa estándar? → usa la tabla.
> 2. Si no → aplica el teorema general.
> 3. Verifica el dominio y simplifica.
>
> **Analogía del espejo:** si $f$ y $f^{-1}$ son funciones espejo, sus pendientes también lo son: una es la recíproca de la otra.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{d}{dx}[\arcsin(3x)]$.
>
> > [!success]- ✅ Solución
> >
> > Por la regla de la cadena, con $u = 3x$:
> >
> > $$\frac{d}{dx}[\arcsin(3x)] = \frac{1}{\sqrt{1-(3x)^2}}\cdot 3 = \frac{3}{\sqrt{1-9x^2}}.$$
> >
> > **Respuesta:** $\frac{3}{\sqrt{1-9x^2}}$, definida en $-\frac{1}{3} < x < \frac{1}{3}$.

> [!example] 📋 Planteamiento
>
> Calcula $\frac{d}{dx}[\ln(x^2 + 1)]$.
>
> > [!success]- ✅ Solución
> >
> > Por la regla de la cadena, con $u = x^2 + 1$:
> >
> > $$\frac{d}{dx}[\ln(x^2+1)] = \frac{1}{x^2+1}\cdot 2x = \frac{2x}{x^2+1}.$$
> >
> > **Respuesta:** $\frac{2x}{x^2+1}$.

> [!example] 📋 Planteamiento
>
> Deriva $\frac{d}{dx}[\arctan(\sqrt{x})]$.
>
> > [!success]- ✅ Solución
> >
> > Doble cadena: $u = \sqrt{x}$, con $u' = \frac{1}{2\sqrt{x}}$:
> >
> > $$\frac{d}{dx}[\arctan(\sqrt{x})] = \frac{1}{1+(\sqrt{x})^2}\cdot \frac{1}{2\sqrt{x}} = \frac{1}{2\sqrt{x}\,(1+x)}.$$
> >
> > **Respuesta:** $\frac{1}{2\sqrt{x}(1+x)}$, para $x > 0$.

> [!example] 📋 Planteamiento
>
> Deriva $\frac{d}{dx}[\operatorname{arcsec}(e^x)]$.
>
> > [!success]- ✅ Solución
> >
> > Con $u = e^x$ y $u' = e^x$:
> >
> > $$\frac{d}{dx}[\operatorname{arcsec}(e^x)] = \frac{e^x}{\lvert e^x\rvert\sqrt{e^{2x}-1}}.$$
> >
> > Como $e^x > 0$ siempre, $\lvert e^x\rvert = e^x$, y queda $\frac{1}{\sqrt{e^{2x}-1}}$.
> >
> > **Respuesta:** $\frac{1}{\sqrt{e^{2x}-1}}$, definida para $x > 0$.

> [!example] 📋 Planteamiento
>
> Calcula $\frac{d}{dx}[\ln(\arcsin(x))]$.
>
> > [!success]- ✅ Solución
> >
> > Cadena con $u = \arcsin(x)$ y $u' = \frac{1}{\sqrt{1-x^2}}$:
> >
> > $$\frac{d}{dx}[\ln(\arcsin x)] = \frac{1}{\arcsin(x)}\cdot \frac{1}{\sqrt{1-x^2}}.$$
> >
> > **Respuesta:** $\frac{1}{\arcsin(x)\sqrt{1-x^2}}$, con dominio $0 < x < 1$ (además de $\arcsin x > 0$).

> [!example] 📋 Planteamiento
>
> Deriva $\frac{d}{dx}\big[(\arccos x)^2\big]$.
>
> > [!success]- ✅ Solución
> >
> > Cadena con $u = \arccos x$ y $u' = -\frac{1}{\sqrt{1-x^2}}$:
> >
> > $$\frac{d}{dx}\big[(\arccos x)^2\big] = 2\arccos(x)\cdot\left(-\frac{1}{\sqrt{1-x^2}}\right) = -\frac{2\arccos(x)}{\sqrt{1-x^2}}.$$
> >
> > **Respuesta:** $-\frac{2\arccos(x)}{\sqrt{1-x^2}}$, con $-1 < x < 1$.

> [!example] 📋 Planteamiento
>
> Si $f(x) = x^5 + 3x^3 + x$, encuentra $(f^{-1})'(5)$.
>
> > [!success]- ✅ Solución
> >
> > Primero se busca el punto: $f(1) = 1 + 3 + 1 = 5$, luego $f^{-1}(5) = 1$.
> >
> > Ahora $f'(x) = 5x^4 + 9x^2 + 1$, de modo que $f'(1) = 5 + 9 + 1 = 15$.
> >
> > Por la fórmula: $(f^{-1})'(5) = \frac{1}{f'(f^{-1}(5))} = \frac{1}{15}$.
> >
> > **Respuesta:** $\frac{1}{15}$.

> [!example] 📋 Planteamiento
>
> Verifica que $\frac{d}{dx}[\arcsin(x) + \arccos(x)]$ es constante.
>
> > [!success]- ✅ Solución
> >
> > $$\frac{d}{dx}[\arcsin x + \arccos x] = \frac{1}{\sqrt{1-x^2}} - \frac{1}{\sqrt{1-x^2}} = 0.$$
> >
> > Una derivada nula en todo el intervalo significa que la función es constante.
> >
> > **Respuesta:** la suma es constante e igual a $\frac{\pi}{2}$; de ahí la identidad $\arcsin x + \arccos x = \frac{\pi}{2}$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Enuncio la fórmula $(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$ con sus condiciones.
> - [ ] Derivo $\ln x$, $\log_a x$, $\arctan x$ y $\arcsin x$ con el método de derivación implícita.
> - [ ] Distingo la inversa de una función de la función recíproca $\frac{1}{f(x)}$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Derivo $\operatorname{arcsec}$ y $\operatorname{arccsc}$ justificando el valor absoluto.
> - [ ] Aplico la regla de la cadena con funciones inversas y controlo el dominio.
> - [ ] Resuelvo ejercicios de derivación implícita donde la inversa aparece anidada.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Calculo $(f^{-1})'(a)$ sin despejar la inversa, localizando antes el punto $b$ con $f(b) = a$.
> - [ ] Interpreto geométricamente la relación de pendientes recíprocas entre $f$ y $f^{-1}$.
> - [ ] Verifico los signos de la tabla de inversas a partir del carácter creciente o decreciente de cada función.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 3: derivadas de funciones inversas.
> - R. Larson, *Cálculo* (Cengage), cap. 3: regla de la cadena con inversas.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 3: la inversa como operación dual.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — la técnica que hace posible el método.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — necesaria para las composiciones con inversas.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]] — derivadas de orden superior de las inversas.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la fórmula de la derivada de la función inversa?::$(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$, con $f$ biyectiva y $f'$ no nula.
> - ¿Cómo se deriva $\arcsin x$ con el método?::Se escribe $x = \operatorname{sen} y$, se deriva de forma implícita: $1 = \cos y \frac{dy}{dx}$, y con $\cos y = \sqrt{1-x^2}$ (rango de $\arcsin$) queda $\frac{dy}{dx} = \frac{1}{\sqrt{1-x^2}}$.
> - ¿Por qué $\operatorname{arcsec}$ lleva valor absoluto?::Porque $\sec y$ y $\tan y$ cambian de signo a la vez, así que su producto es siempre positivo y se escribe $\lvert x\rvert\sqrt{x^2-1}$.
> - ¿Cómo se calcula $(f^{-1})'(5)$ si $f(x) = x^5+3x^3+x$?::Se busca $b$ con $f(b) = 5$: aquí $b = 1$; luego $(f^{-1})'(5) = \frac{1}{f'(1)} = \frac{1}{15}$.
> - ¿Por qué $\arcsin x + \arccos x$ es constante?::Porque sus derivadas se cancelan: $\frac{1}{\sqrt{1-x^2}} - \frac{1}{\sqrt{1-x^2}} = 0$; el valor es $\frac{\pi}{2}$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — el fundamento del método.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]] — usa la derivada de $\ln x$ que aquí se obtiene.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — para las composiciones con inversas.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]] — el caso general de derivar varias veces.
> - [[Unidad 6 - Integrales/V - Técnicas de Integración/04 - Integrales de Funciones Inversas|04 - Integrales de Funciones Inversas]] — el proceso inverso en el mundo de las integrales.
> - [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|02 - Formas Indeterminadas]] — para verificar el comportamiento límite de las inversas.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 a 3: reconocer la estructura (inversa + cadena) debe salirte al instante.
> - Después salta al 4 y al 5, donde el valor absoluto y los dominios son la dificultad real.
> - Termina con el 7 y el 8: el primero es el tipo "punto concreto" que más aparece, y el 8 muestra para qué sirven las inversas (identidades).
> - Cuando lo tengas dominado, continúa con [[Unidad 6 - Integrales/V - Técnicas de Integración/04 - Integrales de Funciones Inversas|Integrales de Funciones Inversas]], donde se usa el mismo razonamiento al revés.

---

**Tags:** #MATG1045 #unidad4 #funciones-inversas #arctan #arcsen #logaritmo #derivacion-implicita #regla-cadena #identidades-trigonometricas

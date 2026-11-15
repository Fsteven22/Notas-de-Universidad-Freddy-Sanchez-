---
dg-publish: true
tags: [MATG1045, unidad4, derivacion-implicita, curvas-implicitas, rectas-tangentes, razones-relacionadas, segunda-derivada]
---

# 🔄 Derivación Implícita

## 🎯 Introducción

> [!info] 💡 Cuando $y$ no está despejada
>
> La **derivación implícita** es la técnica que permite calcular $\frac{dy}{dx}$ cuando la relación entre $x$ y $y$ viene dada por una ecuación $F(x,y) = 0$ en lugar de una fórmula $y = f(x)$. En vez de despejar (a veces imposible o muy engorroso), se deriva **ambos lados** de la ecuación respecto a $x$ y se despeja después.
>
> **La idea clave:** si $y$ es función de $x$, entonces $\frac{d}{dx}[y] = \frac{dy}{dx}$. Cada vez que aparece una $y$ derivada, sale un factor $\frac{dy}{dx}$ que después se junta y se despeja.
>
> **Por qué importa:** es la puerta a las curvas que no son funciones (círculos, elipses), a los problemas de razones de cambio relacionadas y a las ecuaciones diferenciales.
>
> **Ejemplo:** en $x^2 + y^2 = 25$ nunca necesitas escribir $y = \pm\sqrt{25-x^2}$: derivando a mano queda $2x + 2y\frac{dy}{dx} = 0$ y entonces $\frac{dy}{dx} = -\frac{x}{y}$.

> [!warning] ⚠️ Lo que debes dominar antes
>
> - La regla de la cadena, porque es la que hace aparecer el $\frac{dy}{dx}$: [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]].
> - La regla del producto, porque los términos $xy$ la necesitan: [[Unidad 4 - Derivadas/II - Reglas de Derivación/01 - Reglas Fundamentales de Derivación|01 - Reglas Fundamentales de Derivación]].
> - La derivada y su interpretación geométrica: [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]].
>
> **Por qué importa:** esta técnica no trae fórmulas nuevas: es la cadena aplicada con disciplina. Si se te olvida un $\frac{dy}{dx}$, el despeje final no cierra.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Función explícita y función implícita
>
> Una relación es **explícita** cuando la variable dependiente está despejada, $y = f(x)$; es **implícita** cuando la relación se da como una ecuación $F(x,y) = 0$ sin despejar. La derivación implícita calcula la pendiente de una relación implícita **sin resolver por $y$**.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivación_Implícita_02.svg]]
>
> **Se lee así:** el diagrama arranca en una caja con la ecuación de $x$ e $y$ y llega a un rombo que pregunta si $y$ está despejada. Por la rama "sí" se obtiene la función explícita $y = f(x)$ y se deriva directamente con las reglas; por la rama "no" se obtiene $F(x,y) = 0$ y se derivan ambos lados respecto a $x$ para despejar $\frac{dy}{dx}$. Las dos ramas terminan en la misma caja: la derivada $\frac{dy}{dx}$.
>
> **Por qué importa:** te muestra que los dos caminos **llegan al mismo sitio**, y que el implícito no es un método alternativo sino el mismo cálculo con un paso menos de álgebra. Evita el error de despejar $y$ en una ecuación donde eso significa usar la raíz cuadrada con dos ramas.
>
> **Ejemplo:** en $x^2 + y^2 = 25$ despejar obliga a $y = \pm\sqrt{25-x^2}$ (dos ramas); derivando implícitamente queda una sola expresión $\frac{dy}{dx} = -\frac{x}{y}$ que sirve para ambas ramas.

> [!note] 📋 Definición — Derivación implícita (el método)
>
> La **derivación implícita** consiste en: derivar ambos lados de la ecuación respecto a $x$, aplicar la regla de la cadena a cada término que contenga $y$ (dejando un factor $\frac{dy}{dx}$), agrupar todos los términos con $\frac{dy}{dx}$ en un lado, factorizar y despejar.
>
> $$F(x,y) = 0 \ \xrightarrow{\ \frac{d}{dx}\ } \ \text{ecuación con } \frac{dy}{dx} \ \xrightarrow{\ \text{despejar}\ } \ \frac{dy}{dx} = -\frac{F_x}{F_y}.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Derivación_Implícita_01.svg]]
>
> **Se lee así:** el diagrama arranca con la ecuación implícita $F(x,y) = 0$ y baja hasta un rombo central que pregunta por el tipo de término. De él salen cuatro ramas rotuladas: solo $x$ (se deriva normalmente), solo $y$ (se aplica la cadena y aparece $\frac{dy}{dx}$), producto $xy$ (cadena más producto) y composición (cadena completa). Las cuatro vuelven a juntarse en tres rectángulos encadenados: agrupar los términos con $\frac{dy}{dx}$, factorizar y despejar.
>
> **Por qué importa:** es el mapa que evita el error más caro de la técnica, olvidar el $\frac{dy}{dx}$ en los términos con $y$. Con él decides qué regla toca en cada parte de la ecuación y llegas al despeje sin saltos.
>
> **Ejemplo:** en la elipse $\frac{x^2}{16} + \frac{y^2}{9} = 1$ derivas ambos lados, aplicas la cadena al bloque con $y$ y despejas $\frac{dy}{dx} = -\frac{9x}{16y}$.

---

## 🧮 El método, paso a paso

> [!tip] 🎓 Mnemotecnia "DERIVA TODO, MULTIPLICA Y"
>
> 1. **D**eriva ambos lados de la ecuación respecto a $x$.
> 2. **E**n cada término con $y$, recuerda que sale un $\frac{dy}{dx}$.
> 3. **R**ecuerda la regla clave: $\frac{d}{dx}[y] = \frac{dy}{dx}$.
> 4. **I**dentifica **todos** los términos que llevan $\frac{dy}{dx}$.
> 5. **V**e agrupando esos términos a un lado de la ecuación.
> 6. **A**grupa en el otro lado los términos sin $\frac{dy}{dx}$.
> 7. **D**espeja $\frac{dy}{dx}$ factorizando.
>
> **Por qué importa:** el paso 5 es el que hace falta practicar: hasta ahí el error es de regla, después es de álgebra.
>
> **Ejemplo:** en $2x + 2y\frac{dy}{dx} = 0$ el paso 5 da $2y\frac{dy}{dx} = -2x$ y el paso 7 da $\frac{dy}{dx} = -\frac{x}{y}$.

> [!example] 🧠 La "cadena invisible"
>
> Imagina que cada $y$ trae una cadena conectada a $x$: al derivar, la cadena tira y aparece $\frac{dy}{dx}$.
>
> - $\frac{d}{dx}[y^2] = 2y \cdot \frac{dy}{dx}$
> - $\frac{d}{dx}[\sin y] = \cos y \cdot \frac{dy}{dx}$
> - $\frac{d}{dx}[e^y] = e^y \cdot \frac{dy}{dx}$
> - $\frac{d}{dx}[\ln y] = \frac{1}{y} \cdot \frac{dy}{dx}$
>
> **Por qué importa:** no importa la función, siempre se deriva como si la interna fuera $y(x)$. Ese factor extra es **la** regla de la derivación implícita.
>
> **Ejemplo:** $\frac{d}{dx}[\cos y] = -\sin y \cdot \frac{dy}{dx}$: el signo negativo viene de la derivada del coseno, el $\frac{dy}{dx}$ de la cadena.

> [!note] 📝 Técnica "BUSCA Y MARCA"
>
> 1. **BUSCA** términos con solo $x$: se derivan normal.
> 2. **BUSCA** términos con solo $y$: se derivan con $\frac{dy}{dx}$.
> 3. **BUSCA** productos $xy$: regla del producto **más** cadena.
> 4. **MARCA** todos los $\frac{dy}{dx}$ para agruparlos después.
>
> **Por qué importa:** marcar antes de agrupar evita perder un factor en el despeje, que es el segundo error más común después de olvidar la cadena.

---

## 🔵 Ejemplos básicos

> [!example] 🔢 Ejemplo 1: círculo
>
> **Resolver** $x^2 + y^2 = 25$ para encontrar $\frac{dy}{dx}$.
>
> 1. Derivar ambos lados: $\frac{d}{dx}[x^2] + \frac{d}{dx}[y^2] = \frac{d}{dx}[25]$.
> 2. Aplicar cadena al segundo término: $2x + 2y\frac{dy}{dx} = 0$.
> 3. Despejar: $2y\frac{dy}{dx} = -2x$ y $\frac{dy}{dx} = -\frac{x}{y}$.
>
> **Interpretación:** en el punto $(3,4)$ la pendiente es $-\frac{3}{4}$; en $(5,0)$ es infinita, es decir tangente vertical, justo lo que muestra el círculo.

> [!example] 🔢 Ejemplo 2: elipse
>
> **Resolver** $\frac{x^2}{16} + \frac{y^2}{9} = 1$ para encontrar $\frac{dy}{dx}$.
>
> 1. Derivar: $\frac{2x}{16} + \frac{2y}{9}\frac{dy}{dx} = 0$, es decir $\frac{x}{8} + \frac{2y}{9}\frac{dy}{dx} = 0$.
> 2. Despejar: $\frac{2y}{9}\frac{dy}{dx} = -\frac{x}{8}$ y $\frac{dy}{dx} = -\frac{9x}{16y}$.
>
> **Fórmula general:** para $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ siempre sale $\frac{dy}{dx} = -\frac{b^2 x}{a^2 y}$.
>
> **Por qué importa:** el patrón $-\frac{b^2x}{a^2y}$ se reutiliza en optimización con restricciones elípticas.

> [!example] 🔢 Ejemplo 3: productos
>
> **Resolver** $x^2 y + x y^2 = 6$ para encontrar $\frac{dy}{dx}$.
>
> - Para $x^2y$: $\frac{d}{dx}[x^2 y] = 2xy + x^2\frac{dy}{dx}$ (producto más cadena).
> - Para $xy^2$: $\frac{d}{dx}[x y^2] = y^2 + x \cdot 2y\frac{dy}{dx} = y^2 + 2xy\frac{dy}{dx}$.
> - Juntando: $2xy + x^2\frac{dy}{dx} + y^2 + 2xy\frac{dy}{dx} = 0$.
> - Agrupando y despejando: $(x^2 + 2xy)\frac{dy}{dx} = -2xy - y^2$, luego
>
> $$\frac{dy}{dx} = \frac{-2xy - y^2}{x^2 + 2xy} = \frac{-y(2x+y)}{x(x+2y)}.$$

> [!example] 🔢 Ejemplo 4: trigonométricas implícitas
>
> **Resolver** $\sin(xy) + \cos(y) = x$ para encontrar $\frac{dy}{dx}$.
>
> - $\frac{d}{dx}[\sin(xy)] = \cos(xy) \cdot \left(y + x\frac{dy}{dx}\right)$ (cadena con producto adentro).
> - $\frac{d}{dx}[\cos(y)] = -\sin(y) \cdot \frac{dy}{dx}$; la derecha deriva a $1$.
> - Expandiendo: $y\cos(xy) + x\cos(xy)\frac{dy}{dx} - \sin(y)\frac{dy}{dx} = 1$.
> - Despejando: $(x\cos(xy) - \sin(y))\frac{dy}{dx} = 1 - y\cos(xy)$, luego
>
> $$\frac{dy}{dx} = \frac{1 - y\cos(xy)}{x\cos(xy) - \sin(y)}.$$

> [!example] 🔢 Ejemplo 5: exponenciales y logaritmos implícitos
>
> **Resolver** $e^{xy} + \ln(x+y) = 2$ para encontrar $\frac{dy}{dx}$.
>
> - $\frac{d}{dx}[e^{xy}] = e^{xy}\left(y + x\frac{dy}{dx}\right)$; $\frac{d}{dx}[\ln(x+y)] = \frac{1 + \frac{dy}{dx}}{x+y}$; la constante deriva a $0$.
> - Expandiendo: $y e^{xy} + x e^{xy}\frac{dy}{dx} + \frac{1}{x+y} + \frac{1}{x+y}\frac{dy}{dx} = 0$.
> - Agrupando: $\left(x e^{xy} + \frac{1}{x+y}\right)\frac{dy}{dx} = -y e^{xy} - \frac{1}{x+y}$, luego
>
> $$\frac{dy}{dx} = \frac{-y e^{xy} - \frac{1}{x+y}}{x e^{xy} + \frac{1}{x+y}}.$$

---

## 📈 Derivadas de orden superior

> [!warning] 🚨 Segunda derivada implícita: el paso que se olvida
>
> Para encontrar $\frac{d^2y}{dx^2}$:
>
> 1. Encuentra $\frac{dy}{dx}$ por derivación implícita.
> 2. Deriva esa expresión respecto a $x$, **volviendo a aplicar la implícita** donde aparezca $y$.
> 3. Sustituye la expresión conocida de $\frac{dy}{dx}$ y simplifica.
>
> **Por qué importa:** en el paso 2 la variable $y$ sigue siendo función de $x$, así que cada $y$ vuelve a traer su factor $\frac{dy}{dx}$. Saltárselo deja la respuesta en términos mixtos.
>
> **Ejemplo:** del círculo $x^2+y^2=25$ con $\frac{dy}{dx} = -\frac{x}{y}$ se obtiene $\frac{d^2y}{dx^2} = -\frac{25}{y^3}$.

> [!example] 🔢 Segunda derivada del círculo
>
> $$\frac{d^2y}{dx^2} = \frac{d}{dx}\left[-\frac{x}{y}\right] = -\frac{y \cdot 1 - x \cdot \frac{dy}{dx}}{y^2}.$$
>
> Sustituyendo $\frac{dy}{dx} = -\frac{x}{y}$:
>
> $$\frac{d^2y}{dx^2} = -\frac{y + \frac{x^2}{y}}{y^2} = -\frac{y^2 + x^2}{y^3} = -\frac{25}{y^3}.$$
>
> **Interpretación:** el signo de $\frac{d^2y}{dx^2}$ es el signo de $-y^3$: la rama superior del círculo ($y > 0$) es cóncava hacia abajo y la inferior ($y < 0$) hacia arriba, como se ve en la gráfica.

> [!example] 🔢 Segunda derivada de la elipse y de una parábola paramétrica
>
> **Elipse:** con $\frac{dy}{dx} = -\frac{9x}{16y}$,
>
> $$\frac{d^2y}{dx^2} = -\frac{9}{16} \cdot \frac{y - x \cdot \frac{dy}{dx}}{y^2} = -\frac{9(16y^2 + 9x^2)}{16^2 y^3}.$$
>
> **Parábola paramétrica** $x = t^2$, $y = 2t$ con $\frac{dy}{dx} = \frac{1}{t}$:
>
> $$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left[\frac{1}{t}\right]}{\frac{dx}{dt}} = \frac{-\frac{1}{t^2}}{2t} = -\frac{1}{2t^3}.$$
>
> **Para curvas paramétricas:** $\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left[\frac{dy}{dx}\right]}{\frac{dx}{dt}}$. Cuando $t > 0$ la derivada segunda es negativa (cóncava hacia abajo) y cuando $t < 0$ es positiva.

> [!info] 📊 Qué dice la segunda derivada
>
> - $\frac{d^2y}{dx^2} > 0$: la curva es cóncava hacia arriba.
> - $\frac{d^2y}{dx^2} < 0$: la curva es cóncava hacia abajo.
> - $\frac{d^2y}{dx^2} = 0$ y cambio de signo: posible punto de inflexión.
>
> **Por qué importa:** es el mismo criterio de [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]], aplicado a curvas que no vienen despejadas.

---

## 📐 Curvas paramétricas: las dos fórmulas

> [!note] 📋 Curvas paramétricas: planteamiento completo
>
> Una curva paramétrica viene dada por $x = f(t)$ y $y = g(t)$, con $t$ el parámetro (usualmente el tiempo). Las fórmulas fundamentales son:
>
> $$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{g'(t)}{f'(t)} \quad (\text{siempre que } f'(t) \neq 0), \qquad \frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left[\frac{dy}{dx}\right]}{\frac{dx}{dt}}.$$
>
> **Lectura geométrica:** tangente horizontal cuando $\frac{dy}{dt} = 0$ y $\frac{dx}{dt} \neq 0$; tangente vertical cuando $\frac{dx}{dt} = 0$ y $\frac{dy}{dt} \neq 0$; punto singular cuando ambas se anulan a la vez. La velocidad del punto es $v = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}$.
>
> **Por qué importa:** la derivada implícita y la paramétrica atacan el mismo problema (no tienes $y$ despejada) por caminos distintos: una deriva la ecuación, la otra divide dos derivadas respecto al parámetro. La nota dedicada las desarrolla: [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas|03 - Derivadas Paramétricas]].
>
> **Ejemplo:** en $x = 5\cos t$, $y = 5\sin t$ se obtiene $\frac{dy}{dx} = \frac{5\cos t}{-5\sin t} = -\cot t$, igual que $-\frac{x}{y}$ por derivación implícita.

> [!example] 🔢 Tres curvas paramétricas resueltas
>
> **Círculo** $x = 5\cos t$, $y = 5\sin t$: $\frac{dx}{dt} = -5\sin t$, $\frac{dy}{dt} = 5\cos t$, luego $\frac{dy}{dx} = -\cot t$. Verificación: eliminando el parámetro, $x^2+y^2=25$ y $\frac{dy}{dx} = -\frac{x}{y} = -\cot t$.
>
> **Parábola** $x = t^2$, $y = 2t$: $\frac{dy}{dx} = \frac{2}{2t} = \frac{1}{t}$ y $\frac{d^2y}{dx^2} = -\frac{1}{2t^3}$.
>
> **Cicloide** $x = r(t - \sin t)$, $y = r(1 - \cos t)$: $\frac{dy}{dx} = \frac{r\sin t}{r(1-\cos t)}$, y con identidades $\frac{\sin t}{1-\cos t} = \frac{2\sin(t/2)\cos(t/2)}{2\sin^2(t/2)} = \cot\left(\frac{t}{2}\right)$.

---

## ⚠️ Errores comunes y cómo evitarlos

> [!warning] 🚨 Los cuatro errores clásicos
>
> 1. **Olvidar $\frac{dy}{dx}$ en términos con $y$:** $\frac{d}{dx}[y^2] = 2y$ es incorrecto; lo correcto es $2y\frac{dy}{dx}$.
> 2. **No aplicar la regla del producto:** $\frac{d}{dx}[xy] = y\frac{dy}{dx}$ es incorrecto; lo correcto es $y + x\frac{dy}{dx}$.
> 3. **Despejar mal:** hay que agrupar **todos** los términos con $\frac{dy}{dx}$ antes de factorizar; si falta uno, el resultado no cierra.
> 4. **Dar por sentado que $\frac{dy}{dx}$ existe:** hay puntos donde la tangente es vertical y la derivada no existe.
>
> **Por qué importa:** los tres primeros son de proceso y se corrigen siguiendo el orden del método; el cuarto es de lectura geométrica y se comprueba evaluando el denominador del despeje.

> [!tip] 💡 Cinco estrategias anti-error
>
> 1. **Marca cada $y$** antes de derivar: donde haya $y$, saldrá un $\frac{dy}{dx}$.
> 2. **Usa paréntesis** en productos como $(x)(y)$ para no perder la regla del producto.
> 3. **Deriva paso a paso:** no hagas varios pasos mentales a la vez.
> 4. **Agrupa antes que factorizar:** primero todo lo que lleva $\frac{dy}{dx}$, después factoriza.
> 5. **Sustituye un punto conocido** de la curva para verificar que la pendiente tiene sentido.
>
> **Ejemplo:** en el círculo, sustituye $(3,4)$ en $\frac{dy}{dx} = -\frac{x}{y}$ y comprueba que la pendiente $-\frac{3}{4}$ apunta hacia abajo a la derecha, como se dibuja.

---

## 🌊 Aplicaciones geométricas y razones de cambio

> [!example] 🔢 Tangente a una curva implícita
>
> **Problema:** encuentra la ecuación de la tangente a $x^2 + y^2 = 25$ en el punto $(3,4)$.
>
> 1. El punto está en la curva: $3^2 + 4^2 = 9 + 16 = 25$.
> 2. La pendiente: $\frac{dy}{dx} = -\frac{x}{y}$, evaluada en $(3,4)$ da $-\frac{3}{4}$.
> 3. Ecuación: $y - 4 = -\frac{3}{4}(x - 3)$, es decir $y = -\frac{3}{4}x + \frac{25}{4}$.
>
> **Por qué importa:** es la misma fórmula de recta tangente de la nota de derivación, solo que la pendiente sale de un despeje implícito.

> [!info] 🔄 Razones de cambio relacionadas
>
> El método general para problemas donde varias cantidades cambian a la vez:
>
> 1. Establecer la relación entre las variables.
> 2. Derivar implícitamente respecto al **tiempo** $t$.
> 3. Sustituir los valores conocidos.
> 4. Resolver para la razón de cambio deseada.
>
> **Por qué importa:** al derivar respecto a $t$, cada $y(t)$ trae su $\frac{dy}{dt}$: es la misma cadena de antes, con la variable independiente distinta.

> [!example] 🔢 El globo que se infla
>
> **Problema:** un globo esférico se infla a $50$ cm³/min. ¿A qué velocidad aumenta el radio cuando $r = 10$ cm?
>
> 1. Relación: $V = \frac{4}{3}\pi r^3$.
> 2. Derivar respecto a $t$: $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$.
> 3. Sustituir: $50 = 4\pi (10)^2 \frac{dr}{dt} = 400\pi \frac{dr}{dt}$.
> 4. Resolver: $\frac{dr}{dt} = \frac{50}{400\pi} = \frac{1}{8\pi}$ cm/min.
>
> **Interpretación:** aunque el volumen crece a razón constante, el radio crece cada vez más despacio porque el mismo volumen se reparte en una esfera más grande.

---

## 📋 Tabla de patrones comunes

> [!note] 🚀 Derivadas implícitas que salen una y otra vez
>
> | Expresión | Derivada respecto a $x$ |
> |-----------|-------------------------|
> | $y^n$ | $n y^{n-1} \frac{dy}{dx}$ |
> | $xy$ | $y + x\frac{dy}{dx}$ |
> | $x^2 y$ | $2xy + x^2\frac{dy}{dx}$ |
> | $\sin(y)$ | $\cos(y) \frac{dy}{dx}$ |
> | $e^y$ | $e^y \frac{dy}{dx}$ |
> | $\ln(y)$ | $\frac{1}{y} \frac{dy}{dx}$ |
> | $\sin(xy)$ | $\cos(xy)\left(y + x\frac{dy}{dx}\right)$ |
> | $e^{xy}$ | $e^{xy}\left(y + x\frac{dy}{dx}\right)$ |
>
> **Por qué importa:** son ocho patrones que cubren la mayoría de los ejercicios de examen. Memorizarlos convierte la derivación implícita en un trámite de despeje.
>
> **Ejemplo:** si la ecuación trae $\ln(x^2+y^2)$, la derivada es $\frac{2x + 2y\frac{dy}{dx}}{x^2+y^2}$, combinando la tabla con la regla del cociente de la cadena.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Círculo y su tangente

> [!example] 📋 Planteamiento
>
> Sea $x^2 + y^2 = 25$. Encuentra $\frac{dy}{dx}$ y la ecuación de la recta tangente en el punto $(3,4)$.
>
> > [!success]- ✅ Solución
> >
> > Derivando: $2x + 2y\frac{dy}{dx} = 0$, luego $\frac{dy}{dx} = -\frac{x}{y}$.
> >
> > En $(3,4)$: pendiente $m = -\frac{3}{4}$.
> >
> > Tangente: $y - 4 = -\frac{3}{4}(x - 3)$, es decir $y = -\frac{3}{4}x + \frac{25}{4}$.

### ✏️ Ejercicio 2 — Elipse

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{dy}{dx}$ para $\frac{x^2}{9} + \frac{y^2}{4} = 1$ y determina dónde la tangente es horizontal.
>
> > [!success]- ✅ Solución
> >
> > Derivando: $\frac{2x}{9} + \frac{2y}{4}\frac{dy}{dx} = 0$, es decir $\frac{x}{9} + \frac{y}{2}\frac{dy}{dx} = 0$.
> >
> > Despejando: $\frac{dy}{dx} = -\frac{2x}{9y}$ (la fórmula general $-\frac{b^2x}{a^2y}$ con $a^2 = 9$, $b^2 = 4$).
> >
> > La tangente es horizontal cuando el numerador se anula y el denominador no: $x = 0$, es decir en los vértices $(0, 2)$ y $(0, -2)$.

### ✏️ Ejercicio 3 — Producto implícito

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{dy}{dx}$ para $x^2y + xy^2 = 12$ en el punto $(2,2)$.
>
> > [!success]- ✅ Solución
> >
> > Derivando con producto y cadena: $2xy + x^2\frac{dy}{dx} + y^2 + 2xy\frac{dy}{dx} = 0$.
> >
> > Agrupando: $(x^2 + 2xy)\frac{dy}{dx} = -2xy - y^2$, luego $\frac{dy}{dx} = \frac{-2xy - y^2}{x^2 + 2xy}$.
> >
> > En $(2,2)$: numerador $= -8 - 4 = -12$; denominador $= 4 + 8 = 12$; luego $\frac{dy}{dx} = -1$.
> >
> > El punto sí cumple la ecuación: $2^2 \cdot 2 + 2 \cdot 2^2 = 8 + 4 = 12$.

### ✏️ Ejercicio 4 — Trigonométrica implícita

> [!example] 📋 Planteamiento
>
> Encuentra $\frac{dy}{dx}$ si $\sin(xy) + \cos(y) = x$.
>
> > [!success]- ✅ Solución
> >
> > $\frac{d}{dx}[\sin(xy)] = \cos(xy)\left(y + x\frac{dy}{dx}\right)$; $\frac{d}{dx}[\cos(y)] = -\sin(y)\frac{dy}{dx}$; la derecha deriva a $1$.
> >
> > Expandiendo: $y\cos(xy) + x\cos(xy)\frac{dy}{dx} - \sin(y)\frac{dy}{dx} = 1$.
> >
> > Agrupando: $(x\cos(xy) - \sin(y))\frac{dy}{dx} = 1 - y\cos(xy)$, luego
> >
> > $$\frac{dy}{dx} = \frac{1 - y\cos(xy)}{x\cos(xy) - \sin(y)}.$$

### ✏️ Ejercicio 5 — Razón de cambio relacionada

> [!example] 📋 Planteamiento
>
> Un globo esférico se infla a $50$ cm³/min. ¿A qué velocidad crece el radio cuando $r = 10$ cm?
>
> > [!success]- ✅ Solución
> >
> > Relación: $V = \frac{4}{3}\pi r^3$.
> >
> > Derivando respecto al tiempo: $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$.
> >
> > Sustituyendo: $50 = 4\pi (100) \frac{dr}{dt} = 400\pi \frac{dr}{dt}$.
> >
> > Resultado: $\frac{dr}{dt} = \frac{50}{400\pi} = \frac{1}{8\pi} \approx 0.04$ cm/min.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo una relación explícita de una implícita en un enunciado.
> - [ ] Derivo ambos lados de una ecuación aplicando la cadena a cada término con $y$.
> - [ ] Despejo $\frac{dy}{dx}$ sin perder términos en el camino.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo círculos, elipses y productos implícitos y verifico con un punto.
> - [ ] Escribo la ecuación de la tangente a una curva implícita.
> - [ ] Calculo una segunda derivada implícita sustituyendo la primera.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo un problema de razones de cambio relacionadas derivando respecto al tiempo.
> - [ ] Combino derivación implícita y paramétrica y comparo los dos caminos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 3: derivación implícita y razones relacionadas.
> - R. Larson, *Cálculo* (Cengage), cap. 3: derivadas implícitas y de orden superior.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la regla que hace posible esta técnica.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — la misma técnica con la variable independiente $t$.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es el paso que define a la derivación implícita?::Derivar ambos lados de la ecuación respecto a $x$ aplicando la cadena a cada término con $y$, y después despejar $\frac{dy}{dx}$.
> - ¿Cómo se deriva $y^2$ respecto a x?::$\frac{d}{dx}[y^2] = 2y \frac{dy}{dx}$: la derivada externa por la derivada interna $y(x)$.
> - ¿Cuál es la derivada implícita de $xy$?$::$y + x\frac{dy}{dx}$, por la regla del producto con la cadena.
> - ¿Cómo sale la tangente a un círculo?::Derivando $x^2+y^2=r^2$ sale $\frac{dy}{dx} = -\frac{x}{y}$; se evalúa en el punto y se usa $y - y_0 = m(x-x_0)$.
> - ¿Qué cuidado tiene la segunda derivada implícita?::Al derivar $\frac{dy}{dx}$ vuelven a aparecer factores $\frac{dy}{dx}$ que hay que sustituir con la expresión ya encontrada.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — la herramienta que sostiene toda la técnica.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/02 - Derivación Logarítmica|02 - Derivación Logarítmica]] — otra técnica que deriva implícitamente, pero tomando $\ln$ primero.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas|03 - Derivadas Paramétricas]] — el otro camino cuando la curva viene parametrizada.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|01 - Derivadas de Orden Superior]] — el mismo criterio de concavidad aplicado aquí.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — la técnica en problemas de tiempo real.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero con círculos y elipses: son las que más rápido consolidan el despeje.
> - Después salta a ecuaciones con productos $xy$ para dominar la regla del producto dentro de la implícita.
> - Cuando el enunciado traiga un tiempo $t$, ve a [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]].
> - Para curvas parametrizadas, usa [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas|03 - Derivadas Paramétricas]].

---

**Tags:** #MATG1045 #unidad4 #derivacion-implicita #curvas-implicitas #rectas-tangentes #razones-relacionadas #segunda-derivada

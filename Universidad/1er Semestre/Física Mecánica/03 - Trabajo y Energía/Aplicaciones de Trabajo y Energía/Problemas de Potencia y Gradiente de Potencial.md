---
dg-publish: true
tags: [FISG1001, unidad3, fisica-mecanica, trabajo-energia, potencia, gradiente-de-potencial]
---

# ⚡ Problemas de Potencia y Gradiente de Potencial

> [!quote] 🧭 De la energía al ritmo, y del ritmo a la fuerza
>
> El trabajo y la energía dicen *cuánto*; la potencia dice *a qué ritmo*; el gradiente de
> potencial devuelve la energía al terreno de las fuerzas. Los tres puntos de vista describen
> el mismo fenómeno.

---

## 📋 Conceptos Fundamentales

> [!info] 🎯 Potencia
>
> La **potencia** es la rapidez con que se realiza trabajo o se transfiere energía. No dice
> cuánta energía hay, sino **cuánta por unidad de tiempo**.
>
> **Potencia media:**
>
> $$P_{med} = \frac{W}{\Delta t} = \frac{\Delta E}{\Delta t}$$
>
> **Potencia instantánea:**
>
> $$P = \frac{dW}{dt} = \frac{dE}{dt}$$
>
> **Unidades:** watt (W) = J/s. Otras: 1 hp ≈ 746 W, 1 kW = 10³ W.

> [!info] 🎯 Potencia a partir de la fuerza
>
> Si una fuerza $\vec{F}$ actúa sobre un cuerpo que se mueve con velocidad $\vec{v}$, el trabajo
> diferencial es $dW = \vec{F}\cdot d\vec{r}$, y dividiendo por $dt$:
>
> $$P = \vec{F}\cdot\vec{v} = F\,v\cos\theta$$
>
> donde $\theta$ es el ángulo entre la fuerza y la velocidad.
>
> **Casos particulares:**
>
> - Si $\vec{F} \parallel \vec{v}$: $P = Fv$ (máxima).
> - Si $\vec{F} \perp \vec{v}$: $P = 0$ (una fuerza centrípeta **no** realiza trabajo ni
>   transmite potencia).
> - Si $\vec{F}$ se opone al movimiento: $P < 0$ (la potencia se *extrae* del sistema).

> [!info] 🎯 Potencia en rotación
>
> El análogo rotacional de $P = Fv$ es:
>
> $$P = \tau\,\omega$$
>
> con $\tau$ el torque y $\omega$ la velocidad angular. Ejemplo típico: la potencia que entrega
> el motor de un taladro o de una rueda que gira.

## 🔻 Gradiente de Potencial

> [!note] 📐 De la energía a la fuerza
>
> Para una **fuerza conservativa**, la energía potencial $U$ contiene toda la información de la
> fuerza. La fuerza es el **negativo del gradiente** de $U$:
>
> $$\vec{F} = -\nabla U = -\left(\frac{\partial U}{\partial x}\hat{i} + \frac{\partial U}{\partial y}\hat{j} + \frac{\partial U}{\partial z}\hat{k}\right)$$
>
> En una dimensión se reduce a:
>
> $$F_x = -\frac{dU}{dx}$$
>
> **El signo menos tiene sentido físico:** la fuerza siempre apunta hacia donde la energía
> potencial **disminuye** (los cuerpos "caen" hacia el mínimo de potencial).

> [!tip] 🔢 Gradientes que ya conoces
>
> | Sistema | Energía potencial | Fuerza (gradiente) |
> |---|---|---|
> | Gravitatorio (cerca de la Tierra) | $U = mgh$ | $F = -mg$ (hacia abajo) |
> | Elástico (resorte) | $U = \tfrac{1}{2}kx^2$ | $F = -kx$ (restauradora) |
> | Gravitatorio (Newton) | $U = -\dfrac{GMm}{r}$ | $F = -\dfrac{GMm}{r^2}$ (atractiva) |
>
> En los tres casos, derivar la energía potencial devuelve la fuerza conocida con su signo
> correcto.

> [!warning] ⚠️ Gradiente ≠ fuerza generalizada
>
> La relación $\vec{F} = -\nabla U$ **solo** es válida para fuerzas conservativas. Con
> rozamiento, con una fuerza aplicada externa o con fuerzas dependientes del tiempo no existe
> una $U$ de la que derivar: hay que usar el teorema del trabajo y la energía,
> $W_{neto} = \Delta K$.

---

## 🧮 Problemas Resueltos

> [!example] 🧮 Problema 1 — Potencia de un motor que eleva una carga
>
> Un motor sube un bloque de $m = 200\ \text{kg}$ a velocidad **constante** de
> $v = 3\ \text{m/s}$. ¿Qué potencia entrega?
>
> > [!success]- ✅ Solución
> >
> > A velocidad constante la fuerza neta es cero, así que el motor ejerce una fuerza igual al
> > peso:
> >
> > $$F = mg = 200 \times 9{,}8 = 1960\ \text{N}$$
> >
> > $$P = Fv = 1960 \times 3 = 5880\ \text{W} \approx \mathbf{5{,}9\ \text{kW}}$$
> >
> > **Interpretación:** es el ritmo mínimo para subir la carga; cualquier aceleración añadiría
> > potencia extra ($P = (mg + ma)v$).

> [!example] 🧮 Problema 2 — Potencia instantánea con fuerza variable
>
> Una partícula se mueve en el eje $x$ con $v = 2\ \text{m/s}$ constante bajo una fuerza
> $F(x) = 6x^2\ \text{N}$. ¿Cuál es la potencia instantánea en $x = 3\ \text{m}$?
>
> > [!success]- ✅ Solución
> >
> > Con fuerza y velocidad en la misma dirección:
> >
> > $$P = F(x)\,v = 6(3)^2 \times 2 = 6 \times 9 \times 2 = \mathbf{108\ \text{W}}$$
> >
> > **Interpretación:** aunque la velocidad sea constante, la potencia **crece** porque la fuerza
> > crece con la posición. La potencia no es una propiedad del móvil, sino de la interacción en
> > cada instante.

> [!example] 🧮 Problema 3 — Fuerza a partir de la energía potencial
>
> La energía potencial de una partícula es $U(x) = 3x^3 - 2x$ (en joules, con $x$ en metros).
> Halla la fuerza en $x = 1\ \text{m}$.
>
> > [!success]- ✅ Solución
> >
> > Derivando y aplicando $F = -dU/dx$:
> >
> > $$F(x) = -\frac{d}{dx}\left(3x^3 - 2x\right) = -(9x^2 - 2) = 2 - 9x^2$$
> >
> > En $x = 1$: $F = 2 - 9 = \mathbf{-7\ \text{N}}$ (apunta hacia $-x$).
> >
> > **Interpretación:** el signo negativo indica que la fuerza empuja al cuerpo de vuelta hacia
> > el mínimo de $U$, que está en $x>0$ pequeño.

> [!example] 🧮 Problema 4 — Gradiente en dos dimensiones
>
> Una partícula se mueve en el plano con $U(x,y) = 2x^2y$. Determina el vector fuerza en
> $(x,y) = (2, 3)$.
>
> > [!success]- ✅ Solución
> >
> > Calculamos las derivadas parciales:
> >
> > $$\frac{\partial U}{\partial x} = 4xy, \qquad \frac{\partial U}{\partial y} = 2x^2$$
> >
> > $$\vec{F} = -(4xy\,\hat{i} + 2x^2\,\hat{j})$$
> >
> > En $(2,3)$: $\vec{F} = -(24\,\hat{i} + 8\,\hat{j})\ \text{N} = \mathbf{(-24,\,-8)\ \text{N}}$.
> >
> > **Interpretación:** la fuerza apunta en la dirección en la que $U$ baja más rápido, con la
> > magnitud del gradiente en ese punto.

> [!example] 🧮 Problema 5 — Potencia rotacional
>
> Un motor aplica un torque de $\tau = 50\ \text{N·m}$ a un eje que gira a
> $\omega = 10\ \text{rad/s}$. ¿Qué potencia desarrolla?
>
> > [!success]- ✅ Solución
> >
> > $$P = \tau\,\omega = 50 \times 10 = \mathbf{500\ \text{W}}$$
> >
> > **Interpretación:** la misma potencia se puede lograr con mucho torque y poca velocidad
> > angular (como una llave de fuerza) o con poco torque y mucha velocidad (como un taladro
> > rápido).

---

## 🔗 Conexiones con la Unidad

> [!tip] 🧩 Cómo encaja con el resto del tema
>
> - **Trabajo y Energía** — define $W$ y $K$; la potencia es su derivada temporal.
> - **Principio de energía** — $W_{neto} = \Delta K$; dividiendo por $\Delta t$ se obtiene la
>   potencia media.
> - **Conservación de la energía** — si hay fuerzas conservativas, $U$ existe y
>   $\vec{F} = -\nabla U$.
> - **Diagramas de Energía** — el gradiente explica por qué la partícula "rueda" hacia los
>   mínimos de $U$.
> - **Fuerzas no conservativas** — el rozamiento no tiene potencial; su efecto se mide con
>   $W_{nc} = \Delta E$.

## 📊 Resumen de Fórmulas

> [!success] ✅ Lo esencial
>
> | Concepto | Fórmula | Notas |
> |---|---|---|
> | Potencia media | $P_{med} = W/\Delta t$ | Ritmo promedio |
> | Potencia instantánea | $P = dW/dt$ | Ritmo en un instante |
> | Potencia mecánica | $P = \vec{F}\cdot\vec{v}$ | Producto escalar |
> | Potencia rotacional | $P = \tau\,\omega$ | Análogo angular |
> | Fuerza conservativa | $\vec{F} = -\nabla U$ | Gradiente de potencial |
> | Caso 1D | $F_x = -dU/dx$ | Derivada simple |
> | Teorema trabajo-energía | $W_{neto} = \Delta K$ | Válido siempre |

---

**Tags:** #FISG1001 #fisica-mecanica #unidad3 #trabajo-energia #potencia #gradiente-de-potencial

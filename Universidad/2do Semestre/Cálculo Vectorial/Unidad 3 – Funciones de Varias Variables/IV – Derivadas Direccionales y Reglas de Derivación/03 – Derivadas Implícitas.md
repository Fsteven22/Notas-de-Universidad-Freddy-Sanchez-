# 📘 Derivadas Implícitas

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Derivadas Implícitas?
> 
> Las derivadas implícitas permiten calcular derivadas de relaciones donde no podemos (o no queremos) despejar explícitamente una variable en términos de otras.
> 
> **Motivación:**
> 
> - Muchas relaciones matemáticas son implícitas: $x^2 + y^2 = 1$
> - Despejar puede ser imposible: $x^5 + y^5 = x + y$
> - O simplemente inconveniente: ecuaciones complejas
> - Solución: **derivar implícitamente** sin despejar
> 
> **Pregunta fundamental:**
> 
> Si tenemos $F(x, y) = 0$, ¿cómo calculamos $\frac{dy}{dx}$ sin despejar $y$?
> 
> **Aplicaciones prácticas:**
> 
> - **Geometría:** Tangentes a curvas implícitas (círculos, elipses, lemniscatas)
> - **Física:** Ecuaciones de estado, conservación de energía
> - **Economía:** Curvas de indiferencia, isocuantas de producción
> - **Química:** Ecuaciones de gases reales (Van der Waals)
> - **Termodinámica:** Relaciones entre variables de estado
> - **Optimización:** Restricciones implícitas, multiplicadores de Lagrange

---

## 📐 Derivación Implícita - Caso Básico

### 📋 Definición y Método

> [!example]- 🟢 Definición: Derivada Implícita
> 
> **Situación:** Dada una ecuación $F(x, y) = 0$ que define implícitamente $y$ como función de $x$ (i.e., $y = y(x)$).
> 
> **Método:** Derivar ambos lados respecto a $x$, tratando $y$ como función de $x$.
> 
> ---
> 
> **Fórmula fundamental:**
> 
> Si $F(x, y) = 0$ y $F_y \neq 0$, entonces:
> 
> $$\boxed{\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{\partial F/\partial x}{\partial F/\partial y}}$$
> 
> ---
> 
> **Derivación usando regla de la cadena:**
> 
> Derivando $F(x, y(x)) = 0$ respecto a $x$:
> 
> $$\frac{d}{dx}[F(x, y(x))] = 0$$
> 
> Por regla de la cadena:
> 
> $$\frac{\partial F}{\partial x} \cdot 1 + \frac{\partial F}{\partial y} \cdot \frac{dy}{dx} = 0$$
> 
> Despejando:
> 
> $$\frac{dy}{dx} = -\frac{F_x}{F_y}$$
> 
> ---
> 
> **Condición necesaria:**
> 
> $F_y \neq 0$ en el punto de interés (Teorema de la Función Implícita)
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - $F_x = 0$: curva tiene tangente vertical ($\frac{dy}{dx} = 0$)
> - $F_y = 0$: curva tiene tangente horizontal (o punto singular)
> - $\nabla F = (F_x, F_y)$ es perpendicular a la curva de nivel

### 🎨 Visualización Geométrica

> [!note]- 🖼️ Interpretación Gráfica
> 
> ### Curva Implícita
> 
> Para $F(x, y) = 0$, la curva es el conjunto de nivel:
> 
> ```
>         y
>         |
>         |    F(x,y) = 0
>         |     ___
>         |   /     \
>         |  |   •P  |
>         |   \ ___ /
>         |
>         +------------- x
> ```
> 
> ---
> 
> ### Vector Gradiente y Tangente
> 
> En un punto $P = (x_0, y_0)$ sobre la curva:
> 
> ```
>       ∇F ↑
>           |
>           |
>     ------•P------ ← tangente (pendiente dy/dx)
>          / \
>         /   \ curva
> ```
> 
> - $\nabla F = (F_x, F_y)$ es perpendicular a la curva
> - El vector tangente es $(1, \frac{dy}{dx})$
> - $\nabla F \cdot (1, \frac{dy}{dx}) = 0$ implica $F_x + F_y\frac{dy}{dx} = 0$
> 
> ---
> 
> ### Ejemplo Visual: Círculo
> 
> $F(x, y) = x^2 + y^2 - 1 = 0$
> 
> ```
>         y
>         |
>       1 •
>         |  \
>         |   \ ∇F
>         |    •P
>         |   /
>         | /  curva
>         +----------- x
>                   1
> ```
> 
> El gradiente apunta radialmente hacia afuera, perpendicular al círculo.

---

## 📊 Casos y Ejemplos Básicos

### Ejemplo 1: Círculo

> [!example]- 📝 Ejemplo 1: Derivada del Círculo
> 
> **Ecuación:** $x^2 + y^2 = 25$
> 
> **Calcular:** $\frac{dy}{dx}$
> 
> ---
> 
> **Método 1: Derivación implícita directa**
> 
> Derivando ambos lados respecto a $x$:
> 
> $$\frac{d}{dx}(x^2 + y^2) = \frac{d}{dx}(25)$$
> 
> $$2x + 2y\frac{dy}{dx} = 0$$
> 
> $$\boxed{\frac{dy}{dx} = -\frac{x}{y}}$$
> 
> ---
> 
> **Método 2: Fórmula $-F_x/F_y$**
> 
> $F(x, y) = x^2 + y^2 - 25$
> 
> $$F_x = 2x, \quad F_y = 2y$$
> 
> $$\frac{dy}{dx} = -\frac{2x}{2y} = -\frac{x}{y}$$ ✓
> 
> ---
> 
> **Verificación en punto específico:**
> 
> En $(3, 4)$: $\frac{dy}{dx} = -\frac{3}{4}$
> 
> Pendiente de la recta tangente: $y - 4 = -\frac{3}{4}(x - 3)$
> 
> ---
> 
> **Observaciones:**
> 
> - En $(5, 0)$: $\frac{dy}{dx}$ no está definida (tangente vertical)
> - En $(0, 5)$: $\frac{dy}{dx} = 0$ (tangente horizontal)
> - Signo negativo: semicírculo superior tiene pendiente negativa a la derecha

### Ejemplo 2: Elipse

> [!example]- 📝 Ejemplo 2: Derivada de la Elipse
> 
> **Ecuación:** $\frac{x^2}{9} + \frac{y^2}{4} = 1$
> 
> ---
> 
> **Derivando implícitamente:**
> 
> $$\frac{2x}{9} + \frac{2y}{4}\frac{dy}{dx} = 0$$
> 
> $$\frac{dy}{dx} = -\frac{2x/9}{2y/4} = -\frac{4x}{9y}$$
> 
> $$\boxed{\frac{dy}{dx} = -\frac{4x}{9y}}$$
> 
> ---
> 
> **En el punto $(0, 2)$:**
> 
> $$\frac{dy}{dx} = 0$$ (tangente horizontal en vértice)
> 
> **En el punto $(3, 0)$:**
> 
> No definida (tangente vertical en vértice)
> 
> ---
> 
> **Ecuación de tangente en $(3\cos\theta, 2\sin\theta)$:**
> 
> $$\frac{dy}{dx} = -\frac{4 \cdot 3\cos\theta}{9 \cdot 2\sin\theta} = -\frac{2\cos\theta}{3\sin\theta}$$

### Ejemplo 3: Ecuación de Tercer Grado

> [!example]- 📝 Ejemplo 3: Folium de Descartes
> 
> **Ecuación:** $x^3 + y^3 = 3xy$ (Folium de Descartes)
> 
> Esta curva tiene un lazo y es imposible despejar $y$ explícitamente.
> 
> ---
> 
> **Derivando implícitamente:**
> 
> $$3x^2 + 3y^2\frac{dy}{dx} = 3y + 3x\frac{dy}{dx}$$
> 
> Agrupando términos con $\frac{dy}{dx}$:
> 
> $$3y^2\frac{dy}{dx} - 3x\frac{dy}{dx} = 3y - 3x^2$$
> 
> $$\frac{dy}{dx}(3y^2 - 3x) = 3y - 3x^2$$
> 
> $$\boxed{\frac{dy}{dx} = \frac{y - x^2}{y^2 - x}}$$
> 
> ---
> 
> **Método alternativo con $-F_x/F_y$:**
> 
> $F(x, y) = x^3 + y^3 - 3xy$
> 
> $$F_x = 3x^2 - 3y$$ $$F_y = 3y^2 - 3x$$
> 
> $$\frac{dy}{dx} = -\frac{3x^2 - 3y}{3y^2 - 3x} = \frac{y - x^2}{y^2 - x}$$ ✓
> 
> ---
> 
> **Puntos singulares:**
> 
> Donde $F_x = F_y = 0$:
> 
> $$3x^2 - 3y = 0 \implies y = x^2$$ $$3y^2 - 3x = 0 \implies x = y^2$$
> 
> Sustituyendo: $x = (x^2)^2 = x^4$, entonces $x(x^3 - 1) = 0$
> 
> Puntos: $(0, 0)$ y $(1, 1)$
> 
> En $(0, 0)$: origen (punto doble con tangente $y = x$) En $(1, 1)$: punto en la curva donde la pendiente no está bien definida

### Ejemplo 4: Segunda Derivada

> [!example]- 📝 Ejemplo 4: Segunda Derivada Implícita
> 
> **Ecuación:** $x^2 + y^2 = 1$
> 
> **Ya sabemos:** $\frac{dy}{dx} = -\frac{x}{y}$
> 
> **Calcular:** $\frac{d^2y}{dx^2}$
> 
> ---
> 
> **Derivando $\frac{dy}{dx}$ respecto a $x$:**
> 
> $$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(-\frac{x}{y}\right)$$
> 
> Usando regla del cociente:
> 
> $$= -\frac{y \cdot 1 - x \cdot \frac{dy}{dx}}{y^2}$$
> 
> $$= -\frac{y - x\left(-\frac{x}{y}\right)}{y^2}$$
> 
> $$= -\frac{y + \frac{x^2}{y}}{y^2}$$
> 
> $$= -\frac{y^2 + x^2}{y^3}$$
> 
> Como $x^2 + y^2 = 1$:
> 
> $$\boxed{\frac{d^2y}{dx^2} = -\frac{1}{y^3}}$$
> 
> ---
> 
> **Interpretación:**
> 
> - Para $y > 0$ (semicírculo superior): $\frac{d^2y}{dx^2} < 0$ (cóncavo hacia abajo) ✓
> - Para $y < 0$ (semicírculo inferior): $\frac{d^2y}{dx^2} > 0$ (cóncavo hacia arriba) ✓

---

## 🔬 Derivadas Implícitas en Varias Variables

### 📐 Caso General: Dos Variables Independientes

> [!example]- 🔵 Caso: $F(x, y, z) = 0$ define $z = z(x, y)$
> 
> **Situación:** La ecuación $F(x, y, z) = 0$ define implícitamente $z$ como función de $x$ e $y$.
> 
> **Teorema de la Función Implícita:** Si $F_z \neq 0$, podemos calcular:
> 
> $$\boxed{\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}}$$
> 
> ---
> 
> **Derivación:**
> 
> Pensando en $z = z(x, y)$ y derivando $F(x, y, z(x, y)) = 0$ parcialmente:
> 
> **Respecto a $x$:** $$\frac{\partial F}{\partial x} + \frac{\partial F}{\partial z}\frac{\partial z}{\partial x} = 0$$
> 
> $$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}$$
> 
> **Respecto a $y$:** $$\frac{\partial F}{\partial y} + \frac{\partial F}{\partial z}\frac{\partial z}{\partial y} = 0$$
> 
> $$\frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> $F(x, y, z) = 0$ define una **superficie** en $\mathbb{R}^3$
> 
> - $\frac{\partial z}{\partial x}$: pendiente de la superficie en dirección $x$
> - $\frac{\partial z}{\partial y}$: pendiente de la superficie en dirección $y$
> - $\nabla F = (F_x, F_y, F_z)$ es normal a la superficie
> 
> ---
> 
> **Vector normal a la superficie:**
> 
> El plano tangente tiene vector normal:
> 
> $$\vec{n} = \nabla F = (F_x, F_y, F_z)$$
> 
> O equivalentemente: $(F_x, F_y, -1)$ si normalizamos con $F_z$

### Ejemplo 5: Esfera

> [!example]- 📝 Ejemplo 5: Derivadas Parciales de una Esfera
> 
> **Ecuación:** $x^2 + y^2 + z^2 = 9$ (esfera de radio 3)
> 
> **Calcular:** $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$
> 
> ---
> 
> **Solución:**
> 
> $F(x, y, z) = x^2 + y^2 + z^2 - 9$
> 
> $$F_x = 2x, \quad F_y = 2y, \quad F_z = 2z$$
> 
> $$\frac{\partial z}{\partial x} = -\frac{2x}{2z} = -\frac{x}{z}$$
> 
> $$\frac{\partial z}{\partial y} = -\frac{2y}{2z} = -\frac{y}{z}$$
> 
> $$\boxed{\frac{\partial z}{\partial x} = -\frac{x}{z}, \quad \frac{\partial z}{\partial y} = -\frac{y}{z}}$$
> 
> ---
> 
> **En el punto $(2, 1, 2)$:**
> 
> Verificamos: $4 + 1 + 4 = 9$ ✓
> 
> $$\frac{\partial z}{\partial x}\Bigg|_{(2,1,2)} = -\frac{2}{2} = -1$$
> 
> $$\frac{\partial z}{\partial y}\Bigg|_{(2,1,2)} = -\frac{1}{2}$$
> 
> ---
> 
> **Plano tangente en $(2, 1, 2)$:**
> 
> Vector normal: $\nabla F = (4, 2, 4)$ o simplificado $(2, 1, 2)$
> 
> Ecuación: $$2(x - 2) + 1(y - 1) + 2(z - 2) = 0$$ $$2x + y + 2z = 9$$

### Ejemplo 6: Paraboloide

> [!example]- 📝 Ejemplo 6: Paraboloide Elíptico
> 
> **Ecuación:** $z = x^2 + 2y^2$ o $F(x, y, z) = x^2 + 2y^2 - z = 0$
> 
> ---
> 
> **Método 1: Implícita**
> 
> $$F_x = 2x, \quad F_y = 4y, \quad F_z = -1$$
> 
> $$\frac{\partial z}{\partial x} = -\frac{2x}{-1} = 2x$$
> 
> $$\frac{\partial z}{\partial y} = -\frac{4y}{-1} = 4y$$
> 
> ---
> 
> **Método 2: Directa (ya está despejada)**
> 
> $$z = x^2 + 2y^2$$
> 
> $$\frac{\partial z}{\partial x} = 2x, \quad \frac{\partial z}{\partial y} = 4y$$ ✓
> 
> ---
> 
> **Observación:**
> 
> Cuando $z$ ya está despejada, el método implícito da el mismo resultado (y es más trabajo). Pero cuando no podemos despejar, ¡el método implícito es indispensable!

### Ejemplo 7: Ecuación de Estado

> [!example]- 🔥 Ejemplo 7: Gas de Van der Waals
> 
> **Ecuación de estado:**
> 
> $$\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT$$
> 
> donde $a$, $b$, $R$, $n$ son constantes.
> 
> ---
> 
> **Pregunta:** ¿Cómo calcular $\frac{\partial P}{\partial V}\Big|_T$ y $\frac{\partial P}{\partial T}\Big|_V$?
> 
> ---
> 
> **Solución:**
> 
> Reescribiendo como $F(P, V, T) = 0$:
> 
> $$F = \left(P + \frac{an^2}{V^2}\right)(V - nb) - nRT$$
> 
> ---
> 
> **Derivadas parciales de $F$:**
> 
> $$F_P = V - nb$$
> 
> $$F_V = (V - nb)\left(-\frac{2an^2}{V^3}\right) + \left(P + \frac{an^2}{V^2}\right)$$
> 
> $$F_T = -nR$$
> 
> ---
> 
> **Aplicando fórmulas:**
> 
> $$\frac{\partial P}{\partial V}\Bigg|_T = -\frac{F_V}{F_P}$$
> 
> $$\frac{\partial P}{\partial T}\Bigg|_V = -\frac{F_T}{F_P} = -\frac{-nR}{V - nb} = \frac{nR}{V - nb}$$
> 
> Esta última reproduce la forma del gas ideal cuando $a, b \to 0$.

---

## 🔄 Derivadas Implícitas y Regla de la Cadena

### 📊 Relaciones Termodinámicas

> [!note]- 🌡️ Relaciones de Maxwell
> 
> **Contexto:** En termodinámica, variables como $P$, $V$, $T$, $S$ (entropía) están relacionadas.
> 
> **Relación fundamental:** Si tres variables están relacionadas por $F(x, y, z) = 0$, entonces:
> 
> $$\boxed{\frac{\partial x}{\partial y}\Bigg|_z \cdot \frac{\partial y}{\partial z}\Bigg|_x \cdot \frac{\partial z}{\partial x}\Bigg|_y = -1}$$
> 
> ---
> 
> **Demostración:**
> 
> De $F(x, y, z) = 0$:
> 
> $$\frac{\partial x}{\partial y}\Bigg|_z = -\frac{F_y}{F_x}$$
> 
> $$\frac{\partial y}{\partial z}\Bigg|_x = -\frac{F_z}{F_y}$$
> 
> $$\frac{\partial z}{\partial x}\Bigg|_y = -\frac{F_x}{F_z}$$
> 
> Producto:
> 
> $$\left(-\frac{F_y}{F_x}\right) \cdot \left(-\frac{F_z}{F_y}\right) \cdot \left(-\frac{F_x}{F_z}\right) = -1$$ ✓
> 
> ---
> 
> **Aplicación:** Gas ideal $PV = nRT$
> 
> $$\frac{\partial P}{\partial V}\Bigg|_T = -\frac{P}{V}$$
> 
> $$\frac{\partial V}{\partial T}\Bigg|_P = \frac{V}{T}$$
> 
> $$\frac{\partial T}{\partial P}\Bigg|_V = \frac{T}{P}$$
> 
> Producto: $-\frac{P}{V} \cdot \frac{V}{T} \cdot \frac{T}{P} = -1$ ✓

### 🔗 Reciprocidad de Derivadas

> [!note]- 🔄 Teorema de Reciprocidad
> 
> **Teorema:** Si $F(x, y) = 0$ define $y = y(x)$ o $x = x(y)$, entonces:
> 
> $$\boxed{\frac{dx}{dy} = \frac{1}{\frac{dy}{dx}}}$$
> 
> (siempre que ambas derivadas existan y sean no nulas)
> 
> ---
> 
> **Demostración:**
> 
> $$\frac{dy}{dx} = -\frac{F_x}{F_y}$$
> 
> $$\frac{dx}{dy} = -\frac{F_y}{F_x}$$
> 
> Claramente son recíprocos. ✓
> 
> ---
> 
> **Extensión a varias variables:**
> 
> Si $F(x, y, z) = 0$ permite despejar cualquier variable:
> 
> $$\frac{\partial z}{\partial x}\Bigg|_y \cdot \frac{\partial x}{\partial z}\Bigg|_y = -1$$
> 
> (mantener $y$ constante en ambas)

---

## 🌟 Derivadas Implícitas de Orden Superior

### 📐 Segunda Derivada Implícita

> [!example]- 📝 Ejemplo 8: Segunda Derivada en General
> 
> **Dada:** $F(x, y) = 0$ con $\frac{dy}{dx} = -\frac{F_x}{F_y}$
> 
> **Calcular:** $\frac{d^2y}{dx^2}$
> 
> ---
> 
> **Solución:**
> 
> $$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(-\frac{F_x}{F_y}\right)$$
> 
> Usando regla del cociente y cadena:
> 
> $$= -\frac{F_y \cdot \frac{d(F_x)}{dx} - F_x \cdot \frac{d(F_y)}{dx}}{F_y^2}$$
> 
> ---
> 
> **Calculando las derivadas:**
> 
> $$\frac{d(F_x)}{dx} = F_{xx} + F_{xy}\frac{dy}{dx}$$
> 
> $$\frac{d(F_y)}{dx} = F_{yx} + F_{yy}\frac{dy}{dx}$$
> 
> ---
> 
> **Sustituyendo $\frac{dy}{dx} = -\frac{F_x}{F_y}$:**
> 
> $$\frac{d^2y}{dx^2} = -\frac{F_y(F_{xx} - F_{xy}F_x/F_y) - F_x(F_{yx} - F_{yy}F_x/F_y)}{F_y^2}$$
> 
> Simplificando (y usando $F_{xy} = F_{yx}$):
> 
> $$\boxed{\frac{d^2y}{dx^2} = -\frac{F_{xx}F_y^2 - 2F_{xy}F_xF_y + F_{yy}F_x^2}{F_y^3}}$$
> 
> ---
> 
> **Forma alternativa:**
> 
> $$\frac{d^2y}{dx^2} = -\frac{1}{F_y^3}\det\begin{pmatrix} F_{xx} & F_{xy} & F_x \ F_{yx} & F_{yy} & F_y \ F_x & F_y & 0 \end{pmatrix}$$

### Ejemplo 9: Segunda Derivada de una Elipse

> [!example]- 📝 Ejemplo 9: Curvatura de Elipse
> 
> **Ecuación:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
> 
> **Primera derivada:** Ya calculada anteriormente
> 
> $$\frac{dy}{dx} = -\frac{b^2x}{a^2y}$$
> 
> ---
> 
> **Segunda derivada:**
> 
> $$\frac{d^2y}{dx^2} = \frac{d}{dx}\left(-\frac{b^2x}{a^2y}\right)$$
> 
> $$= -\frac{b^2}{a^2} \cdot \frac{y - x\frac{dy}{dx}}{y^2}$$
> 
> $$= -\frac{b^2}{a^2} \cdot \frac{y - x\left(-\frac{b^2x}{a^2y}\right)}{y^2}$$
> 
> $$= -\frac{b^2}{a^2} \cdot \frac{y + \frac{b^2x^2}{a^2y}}{y^2}$$
> 
> $$= -\frac{b^2}{a^2} \cdot \frac{a^2y^2 + b^2x^2}{a^2y^3}$$
> 
> Usando la ecuación de la elipse: $b^2x^2 = a^2b^2 - a^2y^2$
> 
> $$= -\frac{b^2}{a^2} \cdot \frac{a^2b^2}{a^2y^3}$$
> 
> $$\boxed{\frac{d^2y}{dx^2} = -\frac{b^4}{a^2y^3}}$$
> 
> ---
> 
> **Curvatura:**
> 
> $$\kappa = \frac{|y''|}{(1 + (y')^2)^{3/2}} = \frac{b^4/a^2y^3}{(1 + b^4x^2/a^4y^2)^{3/2}}$$
> 
> En los vértices $(0, \pm b)$: $\kappa = \frac{b^4}{a^2b^3} = \frac{b}{a^2}$
> 
> En los vértices $(\pm a, 0)$: $\kappa = \frac{a}{b^2}$

---

## 🎯 Aplicaciones Avanzadas

### 🔍 Aplicación 1: Optimización con Restricciones

> [!example]- 📐 Ejemplo 10: Extremos Condicionados
> 
> **Problema:** Maximizar $f(x, y) = xy$ sujeto a $x^2 + y^2 = 1$
> 
> ---
> 
> **Método 1: Sustitución con derivada implícita**
> 
> De la restricción: $y = \pm\sqrt{1 - x^2}$
> 
> Para el caso positivo: $g(x) = x\sqrt{1 - x^2}$
> 
> $g'(x) = \sqrt{1 - x^2} + x \cdot \frac{-x}{\sqrt{1 - x^2}}$ $= \sqrt{1 - x^2} - \frac{x^2}{\sqrt{1 - x^2}}$ $= \frac{1 - 2x^2}{\sqrt{1 - x^2}}$
> 
> Igualando a cero: $1 - 2x^2 = 0$, entonces $x = \pm\frac{1}{\sqrt{2}}$
> 
> Puntos críticos: $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$, etc.
> 
> Valor máximo: $f = \frac{1}{2}$
> 
> ---
> 
> **Método 2: Multiplicadores de Lagrange** (más elegante)
> 
> Sistema: $\nabla f = \lambda \nabla g$ $(y, x) = \lambda(2x, 2y)$
> 
> Con $x^2 + y^2 = 1$
> 
> Da los mismos puntos críticos.

### 🌊 Aplicación 2: Ecuaciones Diferenciales Implícitas

> [!example]- 🔬 Ejemplo 11: Familia de Curvas
> 
> **Ecuación diferencial:** $x\frac{dy}{dx} + y = x^2$
> 
> **Solución implícita:** $x^2 - xy = C$
> 
> ---
> 
> **Verificación por derivación implícita:**
> 
> De $F(x, y) = x^2 - xy - C = 0$:
> 
> $\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{2x - y}{-x} = \frac{2x - y}{x}$
> 
> Sustituyendo en la ED: $x \cdot \frac{2x - y}{x} + y = 2x - y + y = 2x$ ❌
> 
> (Error en la solución propuesta)
> 
> ---
> 
> **Corrección:**
> 
> La ecuación $x\frac{dy}{dx} + y = x^2$ es lineal.
> 
> Factor integrante: $\mu = e^{\int 1/x dx} = x$
> 
> Multiplicando: $x^2\frac{dy}{dx} + xy = x^3$
> 
> $\frac{d}{dx}(x^2y) = x^3$
> 
> $x^2y = \frac{x^4}{4} + C$
> 
> Solución implícita correcta: $4x^2y - x^4 = C$

### 💰 Aplicación 3: Economía - Curvas de Indiferencia

> [!example]- 📊 Ejemplo 12: Utilidad Marginal
> 
> **Función de utilidad:** $U(x, y) = x^{0.5}y^{0.5}$ (Cobb-Douglas)
> 
> **Curva de indiferencia:** $U(x, y) = k$ (utilidad constante)
> 
> ---
> 
> **Tasa Marginal de Sustitución (TMS):**
> 
> $TMS = -\frac{dy}{dx}\Bigg|_{U=k}$
> 
> Es la cantidad de $y$ que el consumidor está dispuesto a intercambiar por una unidad de $x$ manteniendo utilidad constante.
> 
> ---
> 
> **Cálculo:**
> 
> $F(x, y) = x^{0.5}y^{0.5} - k$
> 
> $F_x = 0.5x^{-0.5}y^{0.5}$ $F_y = 0.5x^{0.5}y^{-0.5}$
> 
> $\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{0.5x^{-0.5}y^{0.5}}{0.5x^{0.5}y^{-0.5}} = -\frac{y}{x}$
> 
> $\boxed{TMS = \frac{y}{x}}$
> 
> ---
> 
> **Interpretación:**
> 
> - Si $y/x = 2$, el consumidor intercambia 2 unidades de $y$ por 1 de $x$
> - Cuando $x$ aumenta, $TMS$ disminuye (saciedad)
> 
> ---
> 
> **Fórmula general:**
> 
> Para cualquier función de utilidad:
> 
> $TMS = \frac{U_x}{U_y}$

### 🌡️ Aplicación 4: Termodinámica Avanzada

> [!example]- ⚗️ Ejemplo 13: Relaciones de Maxwell
> 
> **Energía libre de Helmholtz:** $F = U - TS$
> 
> Diferencial exacto: $dF = -SdT - PdV$
> 
> ---
> 
> **Relación de Maxwell:**
> 
> Como $dF$ es diferencial exacta:
> 
> $\frac{\partial^2 F}{\partial T \partial V} = \frac{\partial^2 F}{\partial V \partial T}$
> 
> Por lo tanto:
> 
> $\frac{\partial}{\partial V}\left(-S\right) = \frac{\partial}{\partial T}(-P)$
> 
> $\boxed{\frac{\partial S}{\partial V}\Bigg|_T = \frac{\partial P}{\partial T}\Bigg|_V}$
> 
> ---
> 
> **Aplicación práctica:**
> 
> Para gas ideal: $P = \frac{nRT}{V}$
> 
> $\frac{\partial P}{\partial T}\Bigg|_V = \frac{nR}{V}$
> 
> Por lo tanto: $\frac{\partial S}{\partial V}\Bigg|_T = \frac{nR}{V}$
> 
> Integrando: $S = nR\ln V + f(T)$
> 
> (parte de la ecuación de Sackur-Tetrode)

---

## 🧩 Sistemas de Ecuaciones Implícitas

### 📐 Caso: Múltiples Ecuaciones

> [!note]- 🔢 Sistema de Ecuaciones Implícitas
> 
> **Sistema:** $\begin{cases} F(x, y, u, v) = 0 \ G(x, y, u, v) = 0 \end{cases}$
> 
> Define implícitamente $u = u(x, y)$ y $v = v(x, y)$
> 
> ---
> 
> **Teorema de la Función Implícita (Caso General):**
> 
> Si el jacobiano:
> 
> $J = \det\begin{pmatrix} F_u & F_v \ G_u & G_v \end{pmatrix} \neq 0$
> 
> entonces podemos calcular derivadas usando:
> 
> $\begin{pmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{pmatrix} = -\begin{pmatrix} F_u & F_v \ G_u & G_v \end{pmatrix}^{-1} \begin{pmatrix} F_x & F_y \ G_x & G_y \end{pmatrix}$
> 
> ---
> 
> **Fórmula explícita (usando regla de Cramer):**
> 
> $\frac{\partial u}{\partial x} = -\frac{1}{J}\det\begin{pmatrix} F_x & F_v \ G_x & G_v \end{pmatrix} = -\frac{F_xG_v - F_vG_x}{J}$
> 
> $\frac{\partial v}{\partial x} = -\frac{1}{J}\det\begin{pmatrix} F_u & F_x \ G_u & G_x \end{pmatrix} = -\frac{F_uG_x - F_xG_u}{J}$
> 
> Y similarmente para $\frac{\partial u}{\partial y}$ y $\frac{\partial v}{\partial y}$.

### Ejemplo 14: Sistema 2×2

> [!example]- 📝 Ejemplo 14: Transformación de Coordenadas
> 
> **Sistema:** $\begin{cases} x = r\cos\theta \ y = r\sin\theta \end{cases}$
> 
> **Pregunta:** Calcular $\frac{\partial r}{\partial x}$, $\frac{\partial r}{\partial y}$, $\frac{\partial \theta}{\partial x}$, $\frac{\partial \theta}{\partial y}$
> 
> ---
> 
> **Método 1: Despejar explícitamente**
> 
> $r = \sqrt{x^2 + y^2}$ $\theta = \arctan(y/x)$
> 
> $\frac{\partial r}{\partial x} = \frac{x}{\sqrt{x^2 + y^2}} = \frac{x}{r} = \cos\theta$
> 
> $\frac{\partial r}{\partial y} = \frac{y}{r} = \sin\theta$
> 
> $\frac{\partial \theta}{\partial x} = \frac{-y/x^2}{1 + y^2/x^2} = \frac{-y}{x^2 + y^2} = -\frac{\sin\theta}{r}$
> 
> $\frac{\partial \theta}{\partial y} = \frac{1/x}{1 + y^2/x^2} = \frac{x}{x^2 + y^2} = \frac{\cos\theta}{r}$
> 
> ---
> 
> **Método 2: Sistema implícito**
> 
> $F(x, y, r, \theta) = x - r\cos\theta = 0$ $G(x, y, r, \theta) = y - r\sin\theta = 0$
> 
> Derivadas parciales: $F_x = 1, \quad F_y = 0, \quad F_r = -\cos\theta, \quad F_\theta = r\sin\theta$ $G_x = 0, \quad G_y = 1, \quad G_r = -\sin\theta, \quad G_\theta = -r\cos\theta$
> 
> Jacobiano: $J = \det\begin{pmatrix} -\cos\theta & r\sin\theta \ -\sin\theta & -r\cos\theta \end{pmatrix} = r\cos^2\theta + r\sin^2\theta = r$
> 
> Aplicando fórmula: $\frac{\partial r}{\partial x} = -\frac{1}{r}\det\begin{pmatrix} 1 & r\sin\theta \ 0 & -r\cos\theta \end{pmatrix} = \frac{r\cos\theta}{r} = \cos\theta$ ✓
> 
> (Las demás se calculan similarmente)

### Ejemplo 15: Cambio de Variables en EDPs

> [!example]- 🌊 Ejemplo 15: Ecuación de Onda
> 
> **Ecuación de onda:** $u_{tt} = c^2u_{xx}$
> 
> **Cambio de variables:** $\xi = x - ct$, $\eta = x + ct$
> 
> ---
> 
> **Relaciones implícitas:** $\begin{cases} \xi = x - ct \ \eta = x + ct \end{cases}$
> 
> Inversas: $x = \frac{\xi + \eta}{2}, \quad t = \frac{\eta - \xi}{2c}$
> 
> ---
> 
> **Derivadas usando regla de la cadena:**
> 
> $\frac{\partial}{\partial x} = \frac{\partial}{\partial \xi}\frac{\partial \xi}{\partial x} + \frac{\partial}{\partial \eta}\frac{\partial \eta}{\partial x} = \frac{\partial}{\partial \xi} + \frac{\partial}{\partial \eta}$
> 
> $\frac{\partial}{\partial t} = \frac{\partial}{\partial \xi}\frac{\partial \xi}{\partial t} + \frac{\partial}{\partial \eta}\frac{\partial \eta}{\partial t} = -c\frac{\partial}{\partial \xi} + c\frac{\partial}{\partial \eta}$
> 
> ---
> 
> **Segundas derivadas:**
> 
> $\frac{\partial^2}{\partial x^2} = \left(\frac{\partial}{\partial \xi} + \frac{\partial}{\partial \eta}\right)^2 = \frac{\partial^2}{\partial \xi^2} + 2\frac{\partial^2}{\partial \xi \partial \eta} + \frac{\partial^2}{\partial \eta^2}$
> 
> $\frac{\partial^2}{\partial t^2} = c^2\left(\frac{\partial}{\partial \eta} - \frac{\partial}{\partial \xi}\right)^2 = c^2\left(\frac{\partial^2}{\partial \eta^2} - 2\frac{\partial^2}{\partial \xi \partial \eta} + \frac{\partial^2}{\partial \xi^2}\right)$
> 
> ---
> 
> **Sustituyendo en ecuación de onda:**
> 
> $c^2\left(\frac{\partial^2 u}{\partial \eta^2} - 2\frac{\partial^2 u}{\partial \xi \partial \eta} + \frac{\partial^2 u}{\partial \xi^2}\right) = c^2\left(\frac{\partial^2 u}{\partial \xi^2} + 2\frac{\partial^2 u}{\partial \xi \partial \eta} + \frac{\partial^2 u}{\partial \eta^2}\right)$
> 
> Simplificando: $-2\frac{\partial^2 u}{\partial \xi \partial \eta} = 2\frac{\partial^2 u}{\partial \xi \partial \eta}$
> 
> $\boxed{\frac{\partial^2 u}{\partial \xi \partial \eta} = 0}$
> 
> ---
> 
> **Solución:**
> 
> Integrando dos veces: $u(\xi, \eta) = f(\xi) + g(\eta)$
> 
> En variables originales: $u(x, t) = f(x - ct) + g(x + ct)$
> 
> (Solución de d'Alembert: ondas viajando en ambas direcciones)

---

## 💡 Propiedades y Teoremas

### 📐 Teorema de la Función Implícita (Formal)

> [!note]- 🎓 Enunciado Completo
> 
> **Teorema:** Sea $F: \mathbb{R}^{n+m} \to \mathbb{R}^m$ una función de clase $C^1$ y sea $(\vec{a}, \vec{b}) \in \mathbb{R}^n \times \mathbb{R}^m$ tal que:
> 
> 1. $F(\vec{a}, \vec{b}) = \vec{0}$
> 2. La matriz jacobiana $\frac{\partial F}{\partial \vec{y}}(\vec{a}, \vec{b})$ es invertible
> 
> Entonces existen entornos $U$ de $\vec{a}$ y $V$ de $\vec{b}$, y una función única $\vec{g}: U \to V$ de clase $C^1$ tal que:
> 
> - $\vec{g}(\vec{a}) = \vec{b}$
> - $F(\vec{x}, \vec{g}(\vec{x})) = \vec{0}$ para todo $\vec{x} \in U$
> - La derivada de $\vec{g}$ está dada por:
> 
> $J_{\vec{g}}(\vec{x}) = -\left[\frac{\partial F}{\partial \vec{y}}\right]^{-1} \cdot \frac{\partial F}{\partial \vec{x}}$
> 
> ---
> 
> **Interpretación:**
> 
> - Condición 1: El punto está en la superficie
> - Condición 2: La superficie no es "singular" (el jacobiano es no nulo)
> - Conclusión: Localmente podemos "despejar" $\vec{y}$ en términos de $\vec{x}$
> 
> ---
> 
> **Caso 2D familiar:**
> 
> $F(x, y) = 0$, si $F_y \neq 0$ entonces:
> 
> $\frac{dy}{dx} = -\frac{F_x}{F_y}$

### 📐 Condiciones de Regularidad

> [!note]- ✅ Cuándo Aplica el Teorema
> 
> **Puntos regulares vs singulares:**
> 
> Un punto $(x_0, y_0)$ sobre $F(x, y) = 0$ es:
> 
> - **Regular** si $\nabla F(x_0, y_0) \neq \vec{0}$
> - **Singular** si $\nabla F(x_0, y_0) = \vec{0}$
> 
> ---
> 
> **En puntos regulares:**
> 
> - Podemos despejar una variable (la que tenga derivada parcial no nula)
> - Existe tangente bien definida
> - La curva es "suave" localmente
> 
> ---
> 
> **En puntos singulares:**
> 
> - El teorema no aplica
> - Puede haber: cúspides, puntos dobles, cruces
> - Tangente no está bien definida
> 
> ---
> 
> **Ejemplo:** Folium de Descartes $x^3 + y^3 = 3xy$
> 
> $\nabla F = (3x^2 - 3y, 3y^2 - 3x)$
> 
> Puntos singulares donde ambas componentes son cero:
> 
> - $(0, 0)$: punto doble (auto-intersección)
> - $(1, 1)$: punto en la curva donde derivada no está definida

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Derivadas Implícitas
> 
> ✅ **Idea central:**
> 
> - No necesitamos despejar explícitamente
> - Derivamos la ecuación completa respecto a la variable independiente
> - Tratamos las variables dependientes como funciones
> 
> ✅ **Fórmula fundamental (una variable):** $\frac{dy}{dx} = -\frac{F_x}{F_y}$
> 
> ✅ **Fórmula fundamental (varias variables):** $\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$
> 
> ✅ **Condición necesaria:**
> 
> - La derivada parcial respecto a la variable dependiente debe ser no nula
> - Equivalente a: $\nabla F \neq \vec{0}$ (punto regular)
> 
> ---
> 
> ### Estrategia para Aplicar
> 
> **Pasos sistemáticos:**
> 
> 1. ✅ **Identificar:** ¿Cuál es la variable dependiente?
> 2. ✅ **Verificar:** ¿El jacobiano es no nulo?
> 3. ✅ **Calcular derivadas parciales:** De $F$ respecto a todas las variables
> 4. ✅ **Aplicar fórmula:** $-F_x/F_y$ o matriz jacobiana para sistemas
> 5. ✅ **Simplificar:** Usar la ecuación original si es necesario
> 
> ---
> 
> ### Aplicaciones Importantes
> 
> La derivación implícita es fundamental para:
> 
> - **Geometría:** Tangentes a curvas y superficies implícitas
> - **Optimización:** Multiplicadores de Lagrange
> - **Termodinámica:** Relaciones entre variables de estado
> - **Economía:** Tasas marginales de sustitución
> - **EDPs:** Cambios de variables para simplificar
> 
> ---
> 
> ### Errores Frecuentes
> 
> ❌ **Olvidar la regla de la cadena:** Al derivar términos con $y$ ❌ **Confundir $\frac{\partial}{\partial x}$ con $\frac{d}{dx}$:** En contextos mixtos ❌ **No verificar $F_y \neq 0$:** Antes de usar la fórmula ❌ **Dividir por cero:** En puntos singulares
> 
> ---
> 
> ### Conexión con Otros Conceptos
> 
> Las derivadas implícitas conectan:
> 
> - Regla de la cadena (es su aplicación directa)
> - Teorema de la función implícita (justificación teórica)
> - Gradiente (es perpendicular a curvas de nivel)
> - Multiplicadores de Lagrange (optimización con restricciones)
> - Ecuaciones diferenciales (familias de curvas)

---

## 🎯 Casos Especiales y Trampas

### ⚠️ Trampa 1: Puntos Singulares

> [!warning]- 🚨 Cuidado con $\nabla F = \vec{0}$
> 
> **Problema:** En puntos donde $F_x = F_y = 0$, la fórmula no aplica.
> 
> ---
> 
> **Ejemplo:** Custoide $x^3 - y^2 = 0$
> 
> $F(x, y) = x^3 - y^2$ $F_x = 3x^2, \quad F_y = -2y$
> 
> En el origen $(0, 0)$:
> 
> - $F_x = 0$, $F_y = 0$
> - $\frac{dy}{dx}$ no está definida por la fórmula
> 
> **Análisis geométrico:**
> 
> - La curva tiene una cúspide en el origen
> - No hay tangente única
> 
> ---
> 
> **Solución alternativa:**
> 
> Despejar: $y = \pm x^{3/2}$
> 
> Para $x > 0$: dos ramas con derivadas:
> 
> - Superior: $\frac{dy}{dx} = \frac{3}{2}x^{1/2}$
> - Inferior: $\frac{dy}{dx} = -\frac{3}{2}x^{1/2}$
> 
> Ambas tienden a $\infty$ cuando $x \to 0^+$ (tangente vertical)

### ⚠️ Trampa 2: Múltiples Ramas

> [!warning]- 🌿 Funciones Multivaluadas
> 
> **Problema:** Una ecuación puede definir múltiples funciones.
> 
> ---
> 
> **Ejemplo:** $x^2 + y^2 = 1$
> 
> Define dos funciones:
> 
> - $y = +\sqrt{1 - x^2}$ (semicírculo superior)
> - $y = -\sqrt{1 - x^2}$ (semicírculo inferior)
> 
> La derivada implícita $\frac{dy}{dx} = -\frac{x}{y}$ es válida para ambas, pero da valores diferentes:
> 
> - En $(0.6, 0.8)$: $\frac{dy}{dx} = -0.75$
> - En $(0.6, -0.8)$: $\frac{dy}{dx} = 0.75$
> 
> ---
> 
> **Moraleja:**
> 
> El teorema de la función implícita garantiza existencia **local**, no global. Debemos especificar qué rama estamos considerando.

### ⚠️ Trampa 3: Dependencia Circular

> [!warning]- 🔄 Variables Interdependientes
> 
> **Cuidado al aplicar fórmulas cuando las variables están relacionadas de forma compleja.**
> 
> ---
> 
> **Ejemplo problemático:**
> 
> Si $F(x, y, z) = 0$ y $G(x, y, z) = 0$ definen $y = y(x)$ y $z = z(x)$ simultáneamente, no podemos aplicar la fórmula simple $\frac{dy}{dx} = -F_x/F_y$ sin considerar que $z$ también depende de $x$.
> 
> **Correcto:** Usar el sistema completo: $\begin{pmatrix} F_y & F_z \ G_y & G_z \end{pmatrix} \begin{pmatrix} dy/dx \ dz/dx \end{pmatrix} = -\begin{pmatrix} F_x \ G_x \end{pmatrix}$

---

## 📚 Tabla de Referencia Rápida

> [!note]- 📋 Fórmulas Clave
> 
> |Situación|Fórmula|
> |---|---|
> |**Una variable implícita**|$\frac{dy}{dx} = -\frac{F_x}{F_y}$|
> |**Dos variables implícitas**|$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}$|
> |**Sistema 2×2**|$\begin{pmatrix} \frac{\partial u}{\partial x} \ \frac{\partial v}{\partial x} \end{pmatrix} = -\begin{pmatrix} F_u & F_v \ G_u & G_v \end{pmatrix}^{-1} \begin{pmatrix} F_x \ G_x \end{pmatrix}$|
> |**Segunda derivada**|$\frac{d^2y}{dx^2} = -\frac{F_{xx}F_y^2 - 2F_{xy}F_xF_y + F_{yy}F_x^2}{F_y^3}$|
> |**Relación termodinámica**|$\frac{\partial x}{\partial y}\Big|
> |**Recíproco**|$\frac{dx}{dy} = \frac{1}{dy/dx}$ (si ambas existen)|
> 
> ### Condiciones Necesarias
> 
> - ✅ $F$ debe ser $C^1$ (derivadas continuas)
> - ✅ $F(\vec{a}) = 0$ (punto en la superficie)
> - ✅ Jacobiano no nulo: $\det\left(\frac{\partial F}{\partial \text{vars. dependientes}}\right) \neq 0$

---

## 🔗 Relaciones con Otros Temas

> [!quote]- 🌐 Conexiones Matemáticas
> 
> ### Prerequisitos:
> 
> - **Derivadas parciales** - Base fundamental
> - **Regla de la cadena** - Herramienta principal
> - **Matriz Jacobiana** - Para sistemas
> - **Diferenciabilidad** - Hipótesis del teorema
> - **Gradiente** - Interpretación geométrica
> 
> ### Este tema es prerequisito para:
> 
> - **Multiplicadores de Lagrange** - Optimización con restricciones
> - **Ecuaciones diferenciales implícitas** - Familias de curvas
> - **Geometría diferencial** - Superficies implícitas
> - **Termodinámica** - Relaciones entre variables
> - **Cambio de variables en integrales** - Transformaciones
> - **Teoría de curvas** - Tangentes y normales
> 
> ### Temas relacionados:
> 
> - **Curvas de nivel** - Interpretación geométrica
> - **Teorema de la función inversa** - Caso especial
> - **Ecuaciones de estado** - Física y química
> - **Curvas de indiferencia** - Economía
> - **Parametrizaciones** - Representaciones alternativas
> 
> ### Diagrama de flujo:
> 
> ```
> Derivadas parciales
>          ↓
>    Regla de cadena
>          ↓
>   Derivadas implícitas
>          ↓
>     ┌────┴────┐
>     ↓         ↓
> Optimización  Geometría
> con restric.  diferencial
> ```
> 
> ### Siguiente tema recomendado:
> 
> **Multiplicadores de Lagrange** - Aplicación directa de derivadas implícitas en optimización

---

## 📖 Ejemplos de Práctica

### Problema 1: Lemniscata

> [!example]- 🎯 Ejercicio: Lemniscata de Bernoulli
> 
> **Ecuación:** $(x^2 + y^2)^2 = 2a^2(x^2 - y^2)$
> 
> **Tareas:** a) Calcular $\frac{dy}{dx}$ b) Encontrar puntos con tangente horizontal c) Encontrar puntos con tangente vertical
> 
> ---
> 
> **Solución a):**
> 
> $F(x, y) = (x^2 + y^2)^2 - 2a^2(x^2 - y^2)$
> 
> $F_x = 2(x^2 + y^2) \cdot 2x - 2a^2 \cdot 2x$ $= 4x(x^2 + y^2) - 4a^2x$ $= 4x(x^2 + y^2 - a^2)$
> 
> $F_y = 2(x^2 + y^2) \cdot 2y - 2a^2 \cdot (-2y)$ $= 4y(x^2 + y^2) + 4a^2y$ $= 4y(x^2 + y^2 + a^2)$
> 
> $\boxed{\frac{dy}{dx} = -\frac{x(x^2 + y^2 - a^2)}{y(x^2 + y^2 + a^2)}}$
> 
> ---
> 
> **Solución b):** Tangente horizontal cuando $F_x = 0$
> 
> $4x(x^2 + y^2 - a^2) = 0$
> 
> Casos:
> 
> - $x = 0$: De la ecuación original, $y^4 = -2a^2y^2$, entonces $y = 0$
>     
>     Punto $(0, 0)$ (origen, punto doble)
>     
> - $x^2 + y^2 = a^2$: Sustituyendo en ecuación original: $a^4 = 2a^2(x^2 - y^2)$ $a^2 = 2(x^2 - y^2)$
>     
>     Con $x^2 + y^2 = a^2$: $x^2 = \frac{3a^2}{4}, \quad y^2 = \frac{a^2}{4}$
>     
>     Puntos: $\left(\pm\frac{a\sqrt{3}}{2}, \pm\frac{a}{2}\right)$ (4 puntos)
>     
> 
> ---
> 
> **Solución c):** Tangente vertical cuando $F_y = 0$
> 
> $4y(x^2 + y^2 + a^2) = 0$
> 
> Como $x^2 + y^2 + a^2 > 0$ siempre, necesitamos $y = 0$
> 
> De la ecuación: $x^4 = 2a^2x^2$, entonces $x^2(x^2 - 2a^2) = 0$
> 
> Puntos: $(0, 0)$ y $(\pm a\sqrt{2}, 0)$

### Problema 2: Optimización Implícita

> [!example]- 🎯 Ejercicio: Optimización con Restricción
> 
> **Problema:** Encontrar el rectángulo de área máxima inscrito en la elipse:
> 
> $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
> 
> con lados paralelos a los ejes.
> 
> ---
> 
> **Solución:**
> 
> Por simetría, buscamos punto $(x, y)$ en primer cuadrante.
> 
> Área del rectángulo: $A = (2x)(2y) = 4xy$
> 
> **Método: Usar derivada implícita**
> 
> De la elipse: $\frac{dy}{dx} = -\frac{b^2x}{a^2y}$
> 
> Para maximizar $A(x)$ donde $y = y(x)$ está en la elipse:
> 
> $\frac{dA}{dx} = 4\left(y + x\frac{dy}{dx}\right) = 4\left(y - x\frac{b^2x}{a^2y}\right)$
> 
> $= 4\left(y - \frac{b^2x^2}{a^2y}\right) = \frac{4}{a^2y}\left(a^2y^2 - b^2x^2\right)$
> 
> Igualando a cero: $a^2y^2 = b^2x^2$
> 
> Con la restricción $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
> 
> $\frac{x^2}{a^2} + \frac{x^2}{a^2} = 1$ $x = \frac{a}{\sqrt{2}}, \quad y = \frac{b}{\sqrt{2}}$
> 
> $\boxed{A_{\max} = 4 \cdot \frac{a}{\sqrt{2}} \cdot \frac{b}{\sqrt{2}} = 2ab}$

### Problema 3: Termodinámica

> [!example]- 🎯 Ejercicio: Ciclo Termodinámico
> 
> **Ecuación de Van der Waals:**
> 
> $\left(P + \frac{a}{V^2}\right)(V - b) = RT$
> 
> **Calcular:** Las tres derivadas parciales cíclicas y verificar su producto.
> 
> ---
> 
> **Solución:**
> 
> $F(P, V, T) = \left(P + \frac{a}{V^2}\right)(V - b) - RT = 0$
> 
> **Derivadas parciales de $F$:**
> 
> $F_P = V - b$
> 
> $F_V = \left(P + \frac{a}{V^2}\right) + (V - b)\left(-\frac{2a}{V^3}\right)$ $= P + \frac{a}{V^2} - \frac{2a(V-b)}{V^3}$ $= P + \frac{aV - 2a(V-b)}{V^3} = P - \frac{a(V - 2b)}{V^3}$
> 
> $F_T = -R$
> 
> ---
> 
> **Derivadas cíclicas:**
> 
> $\frac{\partial P}{\partial V}\Bigg|_T = -\frac{F_V}{F_P} = -\frac{P - \frac{a(V-2b)}{V^3}}{V - b}$
> 
> $\frac{\partial V}{\partial T}\Bigg|_P = -\frac{F_T}{F_V} = \frac{R}{P - \frac{a(V-2b)}{V^3}}$
> 
> $\frac{\partial T}{\partial P}\Bigg|_V = -\frac{F_P}{F_T} = \frac{V - b}{R}$
> 
> ---
> 
> **Verificación del producto:**
> 
> $\frac{\partial P}{\partial V}\Bigg|_T \cdot \frac{\partial V}{\partial T}\Bigg|_P \cdot \frac{\partial T}{\partial P}\Bigg|_V$
> 
> $= -\frac{P - \frac{a(V-2b)}{V^3}}{V - b} \cdot \frac{R}{P - \frac{a(V-2b)}{V^3}} \cdot \frac{V - b}{R}$
> 
> $= -1$ ✓

---

## 🧪 Aplicaciones Especializadas

### 🎨 Aplicación 1: Curvas Algebraicas

> [!example]- 🌸 Ejemplo 16: Rosa de Cuatro Pétalos
> 
> **Ecuación en polares:** $r = \sin(2\theta)$
> 
> **Conversión a cartesianas:**
> 
> $r^2 = r\sin(2\theta) = 2r\sin\theta\cos\theta$ $x^2 + y^2 = 2 \cdot \frac{y}{\sqrt{x^2+y^2}} \cdot \frac{x}{\sqrt{x^2+y^2}} \cdot (x^2 + y^2)$ $(x^2 + y^2)^2 = 2xy(x^2 + y^2)$ $(x^2 + y^2)^{3/2} = 2xy$
> 
> O mejor: $(x^2 + y^2)^3 = 4x^2y^2(x^2 + y^2)$
> 
> Simplificando: $(x^2 + y^2)^2 = 4x^2y^2$
> 
> ---
> 
> **Derivada implícita:**
> 
> $2(x^2 + y^2) \cdot 2(x + y\frac{dy}{dx}) = 8xy\frac{dy}{dx} + 8x^2y$
> 
> Reorganizando y resolviendo para $\frac{dy}{dx}$...
> 
> (Cálculo extenso, mejor usar polares directamente)

### 🔬 Aplicación 2: Ecuaciones Diferenciales

> [!example]- 📐 Ejemplo 17: Solución Implícita de ED
> 
> **Ecuación diferencial:** $y' = \frac{x - y}{x + y}$
> 
> **Solución implícita:** $x^2 + 2xy - y^2 = C$
> 
> ---
> 
> **Verificación:**
> 
> De $F(x, y) = x^2 + 2xy - y^2 - C = 0$:
> 
> $F_x = 2x + 2y$ $F_y = 2x - 2y$
> 
> $\frac{dy}{dx} = -\frac{F_x}{F_y} = -\frac{2x + 2y}{2x - 2y} = -\frac{x + y}{x - y} = \frac{x - y}{-(x - y)} \cdot \frac{-1}{1}$
> 
> Espera, revisemos: $\frac{dy}{dx} = -\frac{2x + 2y}{2x - 2y} = -\frac{x + y}{x - y} = \frac{-(x+y)}{x-y}$
> 
> Para que sea $\frac{x-y}{x+y}$, debería ser: $\frac{dy}{dx} = -\frac{2x + 2y}{2x - 2y}$
> 
> Hmm, hay un error. Revisemos la solución propuesta...
> 
> **Corrección:** La solución correcta es $x^2 - 2xy - y^2 = C$
> 
> Entonces: $F_x = 2x - 2y, \quad F_y = -2x - 2y$ $\frac{dy}{dx} = -\frac{2x - 2y}{-2x - 2y} = \frac{x - y}{x + y}$ ✓

### 💡 Aplicación 3: Cambio de Variables en Integral

> [!example]- 🔄 Ejemplo 18: Jacobiano Implícito
> 
> **Transformación implícita:** $\begin{cases} u = x^2 - y^2 \ v = 2xy \end{cases}$
> 
> **Calcular:** El jacobiano $\frac{\partial(u,v)}{\partial(x,y)}$
> 
> ---
> 
> **Solución directa:**
> 
> $J = \det\begin{pmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{pmatrix} = \det\begin{pmatrix} 2x & -2y \ 2y & 2x \end{pmatrix}$
> 
> $= 4x^2 + 4y^2 = 4(x^2 + y^2) = 4r^2$
> 
> ---
> 
> **Inversa (usando implícitas):**
> 
> Para encontrar $\frac{\partial(x,y)}{\partial(u,v)}$:
> 
> Sistema: $F(x, y, u, v) = x^2 - y^2 - u = 0$ $G(x, y, u, v) = 2xy - v = 0$
> 
> $\frac{\partial(x,y)}{\partial(u,v)} = \left[\frac{\partial(u,v)}{\partial(x,y)}\right]^{-1}$
> 
> Como el jacobiano directo es $4r^2$:
> 
> $\frac{\partial(x,y)}{\partial(u,v)} = \frac{1}{4r^2} = \frac{1}{4(x^2 + y^2)}$
> 
> ---
> 
> **Observación:** Esta es la transformación $(x, y) \mapsto (x^2 - y^2, 2xy)$ que aparece en $z^2$ para $z = x + iy$ (números complejos).

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **Las derivadas implícitas evitan el álgebra tedioso**
>     - No necesitamos despejar explícitamente
>     - Aplicamos regla de la cadena directamente
>     - Obtenemos resultados más elegantes
> 2. **La fórmula $-F_x/F_y$ es fundamental**
>     - Proviene de derivar $F(x, y(x)) = 0$
>     - Generaliza a varias variables y sistemas
>     - Requiere verificar que el denominador no sea cero
> 3. **El gradiente $\nabla F$ contiene toda la información**
>     - Es perpendicular a las curvas/superficies de nivel
>     - Su anulación indica puntos singulares
>     - Determina cuando podemos "despejar" variables
> 4. **Aplicaciones en todos los campos**
>     - Geometría: tangentes a curvas implícitas
>     - Física: ecuaciones de estado, conservación
>     - Economía: tasas marginales
>     - Optimización: restricciones no lineales
> 5. **Conexión con teoremas profundos**
>     - Teorema de la función implícita (existencia)
>     - Multiplicadores de Lagrange (optimización)
>     - Cambio de variables (integrales)
> 
> ---
> 
> ### Jerarquía de Conceptos
> 
> ```
> Derivadas parciales
>          ↓
>    Regla de cadena
>          ↓
>   Derivadas implícitas
>          ↓
>     ┌────┴────┬────────┐
>     ↓         ↓        ↓
>  Geometría  Física  Optimización
>  (tangentes) (estado) (Lagrange)
> ```
> 
> ---
> 
> ### Estrategia General
> 
> **Para problemas con derivadas implícitas:**
> 
> 6. ✅ **Identificar la ecuación:** $F(\text{variables}) = 0$
> 7. ✅ **Determinar dependencias:** ¿Qué es función de qué?
> 8. ✅ **Calcular derivadas parciales:** De $F$ respecto a todas las variables
> 9. ✅ **Verificar regularidad:** ¿El jacobiano es no nulo?
> 10. ✅ **Aplicar fórmula apropiada:** Simple o matricial según el caso
> 11. ✅ **Simplificar si es posible:** Usar la ecuación original
> 12. ✅ **Interpretar el resultado:** Geométrica o físicamente
> 
> ---
> 
> ### Errores Comunes a Evitar
> 
> ❌ **Olvidar derivar términos con la variable dependiente** ❌ **No aplicar regla de la cadena correctamente** ❌ **Confundir $d/dx$ con $\partial/\partial x$** ❌ **No verificar puntos singulares ($\nabla F = 0$)** ❌ **Dividir por cero en denominadores** ❌ **No especificar qué variable es constante** ❌ **Ignorar múltiples ramas de la función**
> 
> ---
> 
> ### Reflexión Final
> 
> Las derivadas implícitas son un ejemplo perfecto de cómo:
> 
> - **La teoría profunda** (Teorema de la función implícita)
> - **Una técnica práctica** (fórmula $-F_x/F_y$)
> - **Aplicaciones diversas** (física, economía, geometría)
> 
> se unen para formar una herramienta poderosa y versátil.
> 
> **Mensaje clave:**
> 
> No siempre necesitamos "resolver" explícitamente una ecuación para trabajar con ella. Las derivadas implícitas nos permiten extraer información (tasas de cambio, tangentes, extremos) directamente de la ecuación, sin el álgebra complicado de despejar.
> 
> Este concepto es fundamental en:
> 
> - **Matemática pura:** Geometría diferencial, topología
> - **Matemática aplicada:** EDPs, optimización, análisis numérico
> - **Ciencias:** Termodinámica, química, economía
> - **Ingeniería:** Control, diseño, análisis de sistemas
> 
> Dominar las derivadas implícitas es dominar una de las técnicas más útiles del cálculo multivariable.

---

## 📊 Resumen Visual

> [!note]- 🗺️ Mapa Mental
> 
> ```
> DERIVADAS IMPLÍCITAS
> │
> ├─ CONCEPTO BÁSICO
> │  ├─ Ecuación: F(x,y) = 0
> │  ├─ No despejamos y explícitamente
> │  └─ Derivamos con regla de cadena
> │
> ├─ FÓRMULA FUNDAMENTAL
> │  ├─ Una variable: dy/dx = -Fₓ/Fᵧ
> │  ├─ Dos variables: ∂z/∂x = -Fₓ/Fᵤ, ∂z/∂y = -Fᵧ/Fᵤ
> │  └─ Sistemas: Usar matrices jacobianas
> │
> ├─ CONDICIONES
> │  ├─ F debe ser C¹ (continua con derivadas continuas)
> │  ├─ Punto regular: ∇F ≠ 0
> │  └─ Denominador no nulo
> │
> ├─ GEOMETRÍA
> │  ├─ ∇F ⊥ curva de nivel
> │  ├─ Tangente: pendiente = dy/dx
> │  └─ Puntos singulares: ∇F = 0
> │
> ├─ APLICACIONES
> │  ├─ Geometría: tangentes, curvaturas
> │  ├─ Física: ecuaciones de estado
> │  ├─ Economía: TMS, elasticidades
> │  ├─ Optimización: multiplicadores de Lagrange
> │  └─ EDPs: cambios de variables
> │
> └─ CASOS ESPECIALES
>    ├─ Segunda derivada implícita
>    ├─ Sistemas de ecuaciones
>    ├─ Relaciones cíclicas (termodinámica)
>    └─ Curvas algebraicas complejas
> ```

---

## 📚 Problemas Propuestos

> [!note]- 💪 Ejercicios para Practicar
> 
> ### Nivel Básico
> 
> 1. Calcular $\frac{dy}{dx}$ para:
>     - a) $x^3 + y^3 = 6xy$
>     - b) $e^{xy} + x^2 = y$
>     - c) $\sin(x + y) = x\cos y$
> 2. Para $x^2 + 4y^2 = 4$, encontrar los puntos donde:
>     - a) Tangente es horizontal
>     - b) Tangente es vertical
>     - c) Pendiente es $-1$
> 3. Verificar que $x^2 - xy + y^2 = 3$ satisface: $x\frac{dy}{dx} = y - 2x$ (Primero calcular $\frac{dy}{dx}$ implícitamente)
> 
> ---
> 
> ### Nivel Intermedio
> 
> 4. Para la astroide $x^{2/3} + y^{2/3} = a^{2/3}$:
>     - a) Calcular $\frac{dy}{dx}$
>     - b) Calcular $\frac{d^2y}{dx^2}$
>     - c) Ecuación de la tangente en $(a\cos^3 t, a\sin^3 t)$
> 5. Si $F(x, y, z) = x^2 + y^2 + z^2 - 3xyz = 0$:
>     - a) Calcular $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$
>     - b) Verificar que $x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y} = 2z - 3xy$
> 6. Para el sistema: $\begin{cases} x = u^2 - v^2 \ y = 2uv \end{cases}$ Calcular $\frac{\partial u}{\partial x}$, $\frac{\partial u}{\partial y}$, $\frac{\partial v}{\partial x}$, $\frac{\partial v}{\partial y}$
> 
> ---
> 
> ### Nivel Avanzado
> 
> 7. **Termodinámica:** Para gas ideal $PV = nRT$, demostrar: $\frac{\partial P}{\partial T}\Bigg|_V \cdot \frac{\partial T}{\partial V}\Bigg|_P \cdot \frac{\partial V}{\partial P}\Bigg|_T = -1$
>     
> 8. **Optimización:** Usar derivadas implícitas para encontrar el punto más cercano en $x^2 + xy + y^2 = 3$ al origen.
>     
> 9. **Curvas algebraicas:** Para la curva de Cassini $(x^2+y^2)^2 - 2a^2(x^2-y^2) = a^4 - b^4$:
>     
>     - a) Encontrar ecuación de tangente en punto general
>     - b) Determinar puntos singulares (si existen)
> 10. **EDPs:** Mostrar que el cambio de variables $\xi = x - ct$, $\eta = x + ct$ transforma la ecuación de onda $u_{tt} = c^2u_{xx}$ en $u_{\xi\eta} = 0$
>     

---

**Tags:** #calculo-multivariable #derivadas-implicitas #teorema-funcion-implicita #regla-cadena #curvas-nivel #geometria-diferencial #termodinamica #optimizacion #multiplicadores-lagrange #ecuaciones-estado #tangentes #jacobiana
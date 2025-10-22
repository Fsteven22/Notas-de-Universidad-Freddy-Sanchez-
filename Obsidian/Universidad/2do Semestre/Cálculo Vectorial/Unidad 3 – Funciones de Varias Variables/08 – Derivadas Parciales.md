# 📘 08 – Derivadas Parciales

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Derivadas Parciales?
> 
> Las derivadas parciales extienden el concepto de derivada a funciones de varias variables, permitiéndonos analizar **cómo cambia la función** cuando variamos **una variable a la vez**.
> 
> **Motivación:**
> 
> - En $f(x)$: la derivada $f'(x)$ mide la tasa de cambio
> - En $f(x,y)$: necesitamos medir cambios en **múltiples direcciones**
> - Solución: derivadas parciales $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$
> 
> **Aplicaciones prácticas:**
> 
> - **Física:** Velocidad en diferentes direcciones, gradientes de temperatura
> - **Economía:** Utilidad marginal, productividad marginal
> - **Ingeniería:** Tasas de cambio en sistemas multivariables
> - **Optimización:** Encontrar máximos y mínimos de funciones
> 
> **Diferencia clave:**
> 
> - En una variable: una sola derivada
> - En dos variables: **dos derivadas parciales** (una por cada variable)
> - En tres variables: **tres derivadas parciales**

---

## 📐 Definición de Derivada Parcial

### 🔍 Definición Formal

> [!example]- 🟢 Definición: Derivada Parcial con respecto a $x$
> 
> **Definición:** La **derivada parcial** de $f(x,y)$ con respecto a $x$ en el punto $(x_0, y_0)$ es:
> 
> $$\frac{\partial f}{\partial x}(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}$$
> 
> **siempre que este límite exista.**
> 
> ---
> 
> **Interpretación:**
> 
> - Mantenemos $y$ **fija** en $y_0$
> - Variamos solo $x$
> - Medimos la tasa de cambio de $f$ en la dirección del eje $x$
> 
> ---
> 
> **Notaciones equivalentes:** $$\frac{\partial f}{\partial x} = f_x = \partial_x f = D_x f = D_1 f$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - Es la **pendiente** de la curva que resulta de intersectar la superficie $z = f(x,y)$ con el plano $y = y_0$
> - Representa la "inclinación" de la superficie en la dirección $x$

> [!example]- 🟡 Definición: Derivada Parcial con respecto a $y$
> 
> **Definición:** La **derivada parcial** de $f(x,y)$ con respecto a $y$ en el punto $(x_0, y_0)$ es:
> 
> $$\frac{\partial f}{\partial y}(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h}$$
> 
> ---
> 
> **Interpretación:**
> 
> - Mantenemos $x$ **fija** en $x_0$
> - Variamos solo $y$
> - Medimos la tasa de cambio de $f$ en la dirección del eje $y$
> 
> ---
> 
> **Notaciones equivalentes:** $$\frac{\partial f}{\partial y} = f_y = \partial_y f = D_y f = D_2 f$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - Es la **pendiente** de la curva que resulta de intersectar la superficie $z = f(x,y)$ con el plano $x = x_0$
> - Representa la "inclinación" de la superficie en la dirección $y$

### 🎯 Interpretación Geométrica

> [!note]- 📊 Visualización de Derivadas Parciales
> 
> Para una superficie $z = f(x,y)$:
> 
> ```
>         z
>         |
>         |    Superficie z = f(x,y)
>         |      /|\
>         |     / | \
>         |    /  |  \
>         |   /   |   \
>         |  /    |    \
>         | /     •(x₀,y₀,f(x₀,y₀))
>         |/      |     
>         +-------+------- y
>        /        y₀
>       /
>      x    x₀
> ```
> 
> ---
> 
> ### $\frac{\partial f}{\partial x}$ en $(x_0, y_0)$
> 
> **Corte con plano $y = y_0$:**
> 
> ```
>         z
>         |
>         |      /
>         |     /  ← Pendiente = ∂f/∂x
>         |    /
>         |   •
>         |  /
>         | /
>         +--------- x
>            x₀
> ```
> 
> - Mantenemos $y = y_0$ constante
> - Observamos la curva resultante
> - $\frac{\partial f}{\partial x}$ es la pendiente de esta curva
> 
> ---
> 
> ### $\frac{\partial f}{\partial y}$ en $(x_0, y_0)$
> 
> **Corte con plano $x = x_0$:**
> 
> ```
>         z
>         |
>         |    \
>         |     \  ← Pendiente = ∂f/∂y
>         |      \
>         |       •
>         |        \
>         |         \
>         +---------- y
>               y₀
> ```
> 
> - Mantenemos $x = x_0$ constante
> - Observamos la curva resultante
> - $\frac{\partial f}{\partial y}$ es la pendiente de esta curva

---

## 🛠️ Cálculo de Derivadas Parciales

### 📍 Regla Práctica

> [!tip]- ✅ Método para Calcular Derivadas Parciales
> 
> ### Para calcular $\frac{\partial f}{\partial x}$:
> 
> 1. Tratar a $y$ como una **constante**
> 2. Derivar con respecto a $x$ usando las reglas usuales de derivación
> 3. El resultado es $\frac{\partial f}{\partial x}$
> 
> ### Para calcular $\frac{\partial f}{\partial y}$:
> 
> 4. Tratar a $x$ como una **constante**
> 5. Derivar con respecto a $y$ usando las reglas usuales
> 6. El resultado es $\frac{\partial f}{\partial y}$
> 
> ---
> 
> **Reglas de derivación (se aplican igual):**
> 
> - Regla de la potencia: $\frac{\partial}{\partial x}(x^n) = nx^{n-1}$
> - Regla del producto
> - Regla del cociente
> - Regla de la cadena
> - Derivadas de funciones trigonométricas, exponenciales, logarítmicas, etc.

---

## 📚 Ejemplos Básicos

### Ejemplo 1: Polinomio Simple

> [!example]- 📝 Ejemplo 1: Función Polinomial
> 
> **Función:** $$f(x,y) = x^2 + 3xy + y^2$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial x}$:**
> 
> Tratamos $y$ como constante:
> 
> - $\frac{\partial}{\partial x}(x^2) = 2x$
> - $\frac{\partial}{\partial x}(3xy) = 3y$ (porque $y$ es constante)
> - $\frac{\partial}{\partial x}(y^2) = 0$ (constante respecto a $x$)
> 
> $$\boxed{\frac{\partial f}{\partial x} = 2x + 3y}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial y}$:**
> 
> Tratamos $x$ como constante:
> 
> - $\frac{\partial}{\partial y}(x^2) = 0$ (constante respecto a $y$)
> - $\frac{\partial}{\partial y}(3xy) = 3x$ (porque $x$ es constante)
> - $\frac{\partial}{\partial y}(y^2) = 2y$
> 
> $$\boxed{\frac{\partial f}{\partial y} = 3x + 2y}$$
> 
> ---
> 
> **Evaluar en $(1, 2)$:** $$\frac{\partial f}{\partial x}(1,2) = 2(1) + 3(2) = 8$$ $$\frac{\partial f}{\partial y}(1,2) = 3(1) + 2(2) = 7$$
> 
> **Interpretación:**
> 
> - En $(1,2)$, si aumentamos $x$ en 1 unidad (manteniendo $y=2$), $f$ aumenta aproximadamente 8 unidades
> - Si aumentamos $y$ en 1 unidad (manteniendo $x=1$), $f$ aumenta aproximadamente 7 unidades

### Ejemplo 2: Función Exponencial

> [!example]- 📝 Ejemplo 2: Con Exponencial
> 
> **Función:** $$f(x,y) = e^{x^2 + y^2}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial x}$:**
> 
> Usamos la regla de la cadena: $$\frac{\partial f}{\partial x} = e^{x^2 + y^2} \cdot \frac{\partial}{\partial x}(x^2 + y^2)$$
> 
> $$= e^{x^2 + y^2} \cdot 2x$$
> 
> $$\boxed{\frac{\partial f}{\partial x} = 2xe^{x^2 + y^2}}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial y}$:**
> 
> $$\frac{\partial f}{\partial y} = e^{x^2 + y^2} \cdot \frac{\partial}{\partial y}(x^2 + y^2)$$
> 
> $$= e^{x^2 + y^2} \cdot 2y$$
> 
> $$\boxed{\frac{\partial f}{\partial y} = 2ye^{x^2 + y^2}}$$

### Ejemplo 3: Función Racional

> [!example]- 📝 Ejemplo 3: Cociente de Funciones
> 
> **Función:** $$f(x,y) = \frac{xy}{x^2 + y^2}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial x}$:**
> 
> Usamos la regla del cociente: $$\frac{\partial f}{\partial x} = \frac{(x^2 + y^2) \cdot \frac{\partial}{\partial x}(xy) - xy \cdot \frac{\partial}{\partial x}(x^2 + y^2)}{(x^2 + y^2)^2}$$
> 
> $$= \frac{(x^2 + y^2) \cdot y - xy \cdot 2x}{(x^2 + y^2)^2}$$
> 
> $$= \frac{x^2y + y^3 - 2x^2y}{(x^2 + y^2)^2}$$
> 
> $$= \frac{y^3 - x^2y}{(x^2 + y^2)^2}$$
> 
> $$\boxed{\frac{\partial f}{\partial x} = \frac{y(y^2 - x^2)}{(x^2 + y^2)^2}}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial y}$:**
> 
> Por simetría (o calculando directamente):
> 
> $$\frac{\partial f}{\partial y} = \frac{(x^2 + y^2) \cdot x - xy \cdot 2y}{(x^2 + y^2)^2}$$
> 
> $$= \frac{x^3 + xy^2 - 2xy^2}{(x^2 + y^2)^2}$$
> 
> $$\boxed{\frac{\partial f}{\partial y} = \frac{x(x^2 - y^2)}{(x^2 + y^2)^2}}$$

### Ejemplo 4: Función Trigonométrica

> [!example]- 📝 Ejemplo 4: Con Seno y Coseno
> 
> **Función:** $$f(x,y) = \sin(x)\cos(y)$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial x}$:**
> 
> Tratamos $\cos(y)$ como constante: $$\frac{\partial f}{\partial x} = \cos(x) \cdot \cos(y)$$
> 
> $$\boxed{\frac{\partial f}{\partial x} = \cos(x)\cos(y)}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial y}$:**
> 
> Tratamos $\sin(x)$ como constante: $$\frac{\partial f}{\partial y} = \sin(x) \cdot (-\sin(y))$$
> 
> $$\boxed{\frac{\partial f}{\partial y} = -\sin(x)\sin(y)}$$

### Ejemplo 5: Función Logarítmica

> [!example]- 📝 Ejemplo 5: Con Logaritmo
> 
> **Función:** $$f(x,y) = \ln(x^2 + y^2)$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial x}$:**
> 
> Usamos la regla de la cadena: $$\frac{\partial f}{\partial x} = \frac{1}{x^2 + y^2} \cdot \frac{\partial}{\partial x}(x^2 + y^2)$$
> 
> $$= \frac{1}{x^2 + y^2} \cdot 2x$$
> 
> $$\boxed{\frac{\partial f}{\partial x} = \frac{2x}{x^2 + y^2}}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial y}$:**
> 
> $$\frac{\partial f}{\partial y} = \frac{1}{x^2 + y^2} \cdot 2y$$
> 
> $$\boxed{\frac{\partial f}{\partial y} = \frac{2y}{x^2 + y^2}}$$

### Ejemplo 6: Función Compuesta

> [!example]- 📝 Ejemplo 6: Composición Compleja
> 
> **Función:** $$f(x,y) = e^{xy}\sin(x + y)$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial x}$:**
> 
> Usamos la regla del producto: $$\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(e^{xy}) \cdot \sin(x+y) + e^{xy} \cdot \frac{\partial}{\partial x}(\sin(x+y))$$
> 
> $$= ye^{xy}\sin(x+y) + e^{xy}\cos(x+y)$$
> 
> $$\boxed{\frac{\partial f}{\partial x} = e^{xy}[y\sin(x+y) + \cos(x+y)]}$$
> 
> ---
> 
> **Calcular $\frac{\partial f}{\partial y}$:**
> 
> $$\frac{\partial f}{\partial y} = xe^{xy}\sin(x+y) + e^{xy}\cos(x+y)$$
> 
> $$\boxed{\frac{\partial f}{\partial y} = e^{xy}[x\sin(x+y) + \cos(x+y)]}$$

---

## 🔬 Derivadas Parciales de Orden Superior

### 📐 Definición

> [!note]- 🟣 Derivadas Parciales de Segundo Orden
> 
> Para una función $f(x,y)$, podemos calcular derivadas de las derivadas:
> 
> ### Derivadas Parciales Puras (Segunda derivada con respecto a la misma variable)
> 
> **Derivada de $f_x$ con respecto a $x$:** $$\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) = f_{xx}$$
> 
> **Derivada de $f_y$ con respecto a $y$:** $$\frac{\partial^2 f}{\partial y^2} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right) = f_{yy}$$
> 
> ---
> 
> ### Derivadas Parciales Mixtas (Segunda derivada con respecto a variables diferentes)
> 
> **Derivada de $f_x$ con respecto a $y$:** $$\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = f_{xy}$$
> 
> **Derivada de $f_y$ con respecto a $x$:** $$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) = f_{yx}$$
> 
> ---
> 
> **Notación:**
> 
> - $f_{xx}$ = segunda derivada parcial pura con respecto a $x$
> - $f_{yy}$ = segunda derivada parcial pura con respecto a $y$
> - $f_{xy}$ = derivada mixta: primero con respecto a $x$, luego con respecto a $y$
> - $f_{yx}$ = derivada mixta: primero con respecto a $y$, luego con respecto a $x$
> 
> **Nota sobre el orden:** En la notación $\frac{\partial^2 f}{\partial y \partial x}$, se lee de **derecha a izquierda**: primero derivamos con respecto a $x$, luego con respecto a $y$.

### Ejemplo 7: Derivadas de Orden Superior

> [!example]- 📝 Ejemplo 7: Todas las Derivadas de Segundo Orden
> 
> **Función:** $$f(x,y) = x^3y^2 + x^2y$$
> 
> ---
> 
> **Paso 1: Derivadas de primer orden**
> 
> $$f_x = 3x^2y^2 + 2xy$$ $$f_y = 2x^3y + x^2$$
> 
> ---
> 
> **Paso 2: Derivadas de segundo orden puras**
> 
> $$f_{xx} = \frac{\partial}{\partial x}(3x^2y^2 + 2xy) = 6xy^2 + 2y$$
> 
> $$f_{yy} = \frac{\partial}{\partial y}(2x^3y + x^2) = 2x^3$$
> 
> ---
> 
> **Paso 3: Derivadas mixtas**
> 
> $$f_{xy} = \frac{\partial}{\partial y}(3x^2y^2 + 2xy) = 6x^2y + 2x$$
> 
> $$f_{yx} = \frac{\partial}{\partial x}(2x^3y + x^2) = 6x^2y + 2x$$
> 
> ---
> 
> **Observación importante:** $$\boxed{f_{xy} = f_{yx} = 6x^2y + 2x}$$
> 
> Las derivadas mixtas son **iguales**. Esto no es casualidad (ver Teorema de Schwarz).

---

## 🌟 Teorema de Schwarz (Clairaut)

> [!note]- 🎯 Teorema: Igualdad de Derivadas Mixtas
> 
> **Enunciado:** Si $f$ está definida en un disco abierto que contiene al punto $(a,b)$, y si las derivadas parciales $f_{xy}$ y $f_{yx}$ son **continuas** en ese disco, entonces:
> 
> $$f_{xy}(a,b) = f_{yx}(a,b)$$
> 
> ---
> 
> **Consecuencia práctica:** Para la mayoría de funciones "bien comportadas" (polinomios, exponenciales, trigonométricas, etc.), las derivadas mixtas son iguales, por lo que:
> 
> $$\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$$
> 
> ---
> 
> **Importancia:**
> 
> - Simplifica cálculos (solo necesitamos calcular una derivada mixta)
> - Es fundamental en teoría de ecuaciones diferenciales parciales
> - Base para definir el concepto de "función suave" o $C^2$
> 
> ---
> 
> **Advertencia:** Este teorema requiere **continuidad** de las derivadas mixtas. Existen funciones patológicas donde $f_{xy} \neq f_{yx}$, pero son raras en la práctica.

### Ejemplo 8: Verificación del Teorema de Schwarz

> [!example]- 📝 Ejemplo 8: Comprobar $f_{xy} = f_{yx}$
> 
> **Función:** $$f(x,y) = e^{x^2y}$$
> 
> ---
> 
> **Derivadas de primer orden:**
> 
> $$f_x = e^{x^2y} \cdot 2xy = 2xye^{x^2y}$$
> 
> $$f_y = e^{x^2y} \cdot x^2 = x^2e^{x^2y}$$
> 
> ---
> 
> **Calcular $f_{xy}$:**
> 
> $$f_{xy} = \frac{\partial}{\partial y}(2xye^{x^2y})$$
> 
> Usamos la regla del producto: $$= 2x \cdot e^{x^2y} + 2xy \cdot e^{x^2y} \cdot x^2$$
> 
> $$= 2xe^{x^2y} + 2x^3ye^{x^2y}$$
> 
> $$= 2xe^{x^2y}(1 + x^2y)$$
> 
> ---
> 
> **Calcular $f_{yx}$:**
> 
> $$f_{yx} = \frac{\partial}{\partial x}(x^2e^{x^2y})$$
> 
> $$= 2xe^{x^2y} + x^2 \cdot e^{x^2y} \cdot 2xy$$
> 
> $$= 2xe^{x^2y} + 2x^3ye^{x^2y}$$
> 
> $$= 2xe^{x^2y}(1 + x^2y)$$
> 
> ---
> 
> **Conclusión:** $$\boxed{f_{xy} = f_{yx} = 2xe^{x^2y}(1 + x^2y)}$$ ✓

---

## 📊 Derivadas Parciales en Tres Variables

> [!note]- 🎲 Extensión a $\mathbb{R}^3$
> 
> Para una función $f(x,y,z)$, tenemos **tres derivadas parciales de primer orden:**
> 
> ### Derivadas de Primer Orden
> 
> $$\frac{\partial f}{\partial x} = f_x = \lim_{h \to 0} \frac{f(x+h,y,z) - f(x,y,z)}{h}$$
> 
> $$\frac{\partial f}{\partial y} = f_y = \lim_{h \to 0} \frac{f(x,y+h,z) - f(x,y,z)}{h}$$
> 
> $$\frac{\partial f}{\partial z} = f_z = \lim_{h \to 0} \frac{f(x,y,z+h) - f(x,y,z)}{h}$$
> 
> ---
> 
> ### Derivadas de Segundo Orden
> 
> **Hay 9 derivadas de segundo orden posibles:**
> 
> **Puras:**
> 
> - $f_{xx}$, $f_{yy}$, $f_{zz}$
> 
> **Mixtas:**
> 
> - $f_{xy}$, $f_{xz}$, $f_{yx}$, $f_{yz}$, $f_{zx}$, $f_{zy}$
> 
> **Por el Teorema de Schwarz:**
> 
> - $f_{xy} = f_{yx}$
> - $f_{xz} = f_{zx}$
> - $f_{yz} = f_{zy}$
> 
> Por lo tanto, solo hay **6 derivadas de segundo orden distintas**.

### Ejemplo 9: Función de Tres Variables

> [!example]- 📝 Ejemplo 9: Derivadas en $\mathbb{R}^3$
> 
> **Función:** $$f(x,y,z) = x^2yz + xy^2z + xyz^2$$
> 
> ---
> 
> **Derivadas de primer orden:**
> 
> $$f_x = 2xyz + y^2z + yz^2$$
> 
> $$f_y = x^2z + 2xyz + xz^2$$
> 
> $$f_z = x^2y + xy^2 + 2xyz$$
> 
> ---
> 
> **Algunas derivadas de segundo orden:**
> 
> $$f_{xx} = 2yz$$
> 
> $$f_{xy} = 2xz + 2yz + z^2$$
> 
> $$f_{xyz} = \frac{\partial}{\partial z}(f_{xy}) = 2x + 2y + 2z$$
> 
> **Nota:** $f_{xyz}$ es una derivada de **tercer orden** (derivamos tres veces).

---

## 💡 Interpretaciones y Aplicaciones

### 🌡️ Aplicación 1: Temperatura

> [!example]- 🔥 Ejemplo: Distribución de Temperatura
> 
> **Situación:** La temperatura en una placa metálica está dada por: $$T(x,y) = 100 - x^2 - 2y^2$$
> 
> donde $T$ está en °C y $x, y$ en centímetros.
> 
> ---
> 
> **Derivadas parciales:**
> 
> $$\frac{\partial T}{\partial x} = -2x$$
> 
> $$\frac{\partial T}{\partial y} = -4y$$
> 
> ---
> 
> **Interpretación en el punto $(3, 2)$:**
> 
> $$\frac{\partial T}{\partial x}(3,2) = -2(3) = -6 \text{ °C/cm}$$
> 
> $$\frac{\partial T}{\partial y}(3,2) = -4(2) = -8 \text{ °C/cm}$$
> 
> **Significado:**
> 
> - Si nos movemos en dirección $x$ positiva desde $(3,2)$, la temperatura **disminuye** a razón de 6°C por centímetro
> - Si nos movemos en dirección $y$ positiva, la temperatura **disminuye** a razón de 8°C por centímetro
> - La temperatura disminuye más rápido en la dirección $y$

### 💰 Aplicación 2: Economía - Utilidad Marginal

> [!example]- 📈 Ejemplo: Función de Utilidad
> 
> **Situación:** La utilidad de un consumidor que compra $x$ unidades del bien A e $y$ unidades del bien B es: $$U(x,y) = xy + 2x + 3y$$
> 
> ---
> 
> **Utilidades marginales:**
> 
> $$\frac{\partial U}{\partial x} = y + 2$$
> 
> $$\frac{\partial U}{\partial y} = x + 3$$
> 
> ---
> 
> **Interpretación:**
> 
> - $\frac{\partial U}{\partial x}$ = **utilidad marginal** del bien A
> - Mide cuánto aumenta la utilidad al consumir una unidad más de A (manteniendo B constante)
> 
> **En el punto $(10, 5)$:** $$\frac{\partial U}{\partial x}(10,5) = 5 + 2 = 7$$ $$\frac{\partial U}{\partial y}(10,5) 
= 10 + 3 = 13$$
> **Interpretación económica:**
> 
> - Al consumir 10 unidades de A y 5 de B, una unidad adicional de A aumenta la utilidad en 7
> - Una unidad adicional de B aumenta la utilidad en 13
> - El bien B proporciona mayor utilidad marginal en este punto
> - El consumidor debería preferir más unidades de B que de A

### 🏗️ Aplicación 3: Ingeniería - Producción

> [!example]- 🏭 Ejemplo: Función de Producción Cobb-Douglas
> 
> **Situación:** La producción de una fábrica está dada por: $$P(K,L) = 10K^{0.4}L^{0.6}$$
> 
> donde $K$ = capital invertido, $L$ = horas de trabajo
> 
> ---
> 
> **Productividades marginales:**
> 
> $$\frac{\partial P}{\partial K} = 10 \cdot 0.4 \cdot K^{-0.6}L^{0.6} = 4K^{-0.6}L^{0.6}$$
> 
> $$\frac{\partial P}{\partial L} = 10 \cdot 0.6 \cdot K^{0.4}L^{-0.4} = 6K^{0.4}L^{-0.4}$$
> 
> ---
> 
> **Con $K = 100$ y $L = 100$:**
> 
> $$\frac{\partial P}{\partial K}(100,100) = 4 \cdot 100^{-0.6} \cdot 100^{0.6} = 4$$
> 
> $$\frac{\partial P}{\partial L}(100,100) = 6 \cdot 100^{0.4} \cdot 100^{-0.4} = 6$$
> 
> **Interpretación:**
> 
> - Aumentar el capital en 1 unidad aumenta la producción en aproximadamente 4 unidades
> - Aumentar el trabajo en 1 hora aumenta la producción en aproximadamente 6 unidades
> - El trabajo es más productivo que el capital en este punto

### 🌊 Aplicación 4: Física - Onda

> [!example]- 🌀 Ejemplo: Ecuación de Onda
> 
> **Situación:** Una onda en una cuerda está descrita por: $$u(x,t) = A\sin(kx - \omega t)$$
> 
> donde $x$ = posición, $t$ = tiempo
> 
> ---
> 
> **Derivadas:**
> 
> $$\frac{\partial u}{\partial x} = Ak\cos(kx - \omega t)$$
> 
> $$\frac{\partial u}{\partial t} = -A\omega\cos(kx - \omega t)$$
> 
> $$\frac{\partial^2 u}{\partial x^2} = -Ak^2\sin(kx - \omega t)$$
> 
> $$\frac{\partial^2 u}{\partial t^2} = -A\omega^2\sin(kx - \omega t)$$
> 
> ---
> 
> **Ecuación de onda:**
> 
> Si $\omega = vk$ (donde $v$ es la velocidad de propagación), entonces:
> 
> $$\frac{\partial^2 u}{\partial t^2} = v^2 \frac{\partial^2 u}{\partial x^2}$$
> 
> Esta es la famosa **ecuación de onda 1D**.

---

## 🔍 Relación entre Derivadas Parciales y Continuidad

> [!warning]- ⚠️ Advertencias Importantes
> 
> ### 1. Existencia de Derivadas Parciales NO implica Continuidad
> 
> **Contraejemplo:** $$f(x,y) = \begin{cases} \frac{xy}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> **En el origen:**
> 
> $$f_x(0,0) = \lim_{h \to 0} \frac{f(h,0) - f(0,0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$$
> 
> $$f_y(0,0) = \lim_{h \to 0} \frac{f(0,h) - f(0,0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0$$
> 
> **Pero:** $f$ NO es continua en $(0,0)$ (el límite no existe, depende del camino).
> 
> **Conclusión:** Las derivadas parciales existen, pero la función **NO es continua**.
> 
> ---
> 
> ### 2. Continuidad NO implica Existencia de Derivadas Parciales
> 
> **Contraejemplo:** $$f(x,y) = \sqrt{x^2 + y^2}$$
> 
> - $f$ es continua en $(0,0)$
> - Pero las derivadas parciales **NO existen** en $(0,0)$
> 
> **Verificación:** $$f_x(0,0) = \lim_{h \to 0} \frac{\sqrt{h^2 + 0} - 0}{h} = \lim_{h \to 0} \frac{|h|}{h}$$
> 
> Este límite no existe (es $+1$ por la derecha y $-1$ por la izquierda).
> 
> ---
> 
> ### 3. Derivadas Parciales Continuas SÍ implican Continuidad
> 
> **Teorema:** Si $f_x$ y $f_y$ existen y son **continuas** en un entorno de $(x_0, y_0)$, entonces $f$ es continua en $(x_0, y_0)$.
> 
> Este resultado es fundamental y lleva al concepto de **diferenciabilidad** (próximo tema).

---

## 📐 Derivadas Parciales de Orden Superior (General)

> [!note]- 🔢 Notación y Generalización
> 
> ### Derivadas de Orden $n$
> 
> Para $f(x,y)$, podemos tener derivadas de cualquier orden:
> 
> **Tercer orden:**
> 
> - $f_{xxx}$, $f_{xxy}$, $f_{xyx}$, $f_{yxx}$
> - $f_{xyy}$, $f_{yxy}$, $f_{yyx}$, $f_{yyy}$
> 
> Con el Teorema de Schwarz, muchas son iguales:
> 
> - $f_{xxy} = f_{xyx} = f_{yxx}$
> - $f_{xyy} = f_{yxy} = f_{yyx}$
> 
> ---
> 
> ### Notación compacta
> 
> **Multiíndices:** Para $f(x,y)$, podemos escribir: $$\frac{\partial^{m+n} f}{\partial x^m \partial y^n}$$
> 
> **Ejemplo:** $$\frac{\partial^3 f}{\partial x^2 \partial y} = f_{xxy}$$
> 
> ---
> 
> ### Clase $C^k$
> 
> Decimos que $f$ es de **clase $C^k$** si todas sus derivadas parciales hasta orden $k$ existen y son continuas.
> 
> - $C^0$ = continuas
> - $C^1$ = derivadas de primer orden continuas
> - $C^2$ = derivadas hasta segundo orden continuas
> - $C^\infty$ = infinitamente diferenciable

---

## 🎯 Ejemplos Avanzados

### Ejemplo 10: Función Implícita

> [!example]- 📝 Ejemplo 10: Derivada Implícita
> 
> **Situación:** Dada la ecuación implícita: $$x^2 + y^2 + z^2 = 1$$
> 
> donde $z = f(x,y)$, encontrar $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$.
> 
> ---
> 
> **Método: Derivación implícita**
> 
> Derivamos toda la ecuación con respecto a $x$ (tratando $y$ como constante y $z$ como función de $x$):
> 
> $$2x + 0 + 2z\frac{\partial z}{\partial x} = 0$$
> 
> $$\boxed{\frac{\partial z}{\partial x} = -\frac{x}{z}}$$
> 
> ---
> 
> Derivamos con respecto a $y$:
> 
> $$0 + 2y + 2z\frac{\partial z}{\partial y} = 0$$
> 
> $$\boxed{\frac{\partial z}{\partial y} = -\frac{y}{z}}$$
> 
> ---
> 
> **Interpretación geométrica:** La ecuación $x^2 + y^2 + z^2 = 1$ representa una esfera. Las derivadas parciales nos dan las pendientes de la superficie en las direcciones $x$ e $y$.

### Ejemplo 11: Laplaciano

> [!example]- 📝 Ejemplo 11: Operador Laplaciano
> 
> **Definición:** El **Laplaciano** de $f$ es: $$\nabla^2 f = \Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$
> 
> (En tres variables: $\nabla^2 f = f_{xx} + f_{yy} + f_{zz}$)
> 
> ---
> 
> **Calcular el Laplaciano de:** $$f(x,y) = e^x\cos(y)$$
> 
> **Derivadas de primer orden:** $$f_x = e^x\cos(y)$$ $$f_y = -e^x\sin(y)$$
> 
> **Derivadas de segundo orden:** $$f_{xx} = e^x\cos(y)$$ $$f_{yy} = -e^x\cos(y)$$
> 
> **Laplaciano:** $$\nabla^2 f = e^x\cos(y) + (-e^x\cos(y)) = 0$$
> 
> **Conclusión:** $f$ es una **función armónica** (su Laplaciano es cero).
> 
> ---
> 
> **Importancia:**
> 
> - Las funciones armónicas son soluciones de la ecuación de Laplace: $\nabla^2 f = 0$
> - Aparecen en física (electromagnetismo, mecánica de fluidos, transferencia de calor)

### Ejemplo 12: Verificar EDP

> [!example]- 📝 Ejemplo 12: Verificar Ecuación Diferencial Parcial
> 
> **Problema:** Verificar que $u(x,t) = \sin(x)\cos(ct)$ satisface la ecuación de onda: $$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$
> 
> ---
> 
> **Derivadas con respecto a $x$:** $$\frac{\partial u}{\partial x} = \cos(x)\cos(ct)$$
> 
> $$\frac{\partial^2 u}{\partial x^2} = -\sin(x)\cos(ct)$$
> 
> ---
> 
> **Derivadas con respecto a $t$:** $$\frac{\partial u}{\partial t} = -c\sin(x)\sin(ct)$$
> 
> $$\frac{\partial^2 u}{\partial t^2} = -c^2\sin(x)\cos(ct)$$
> 
> ---
> 
> **Verificación:** $$c^2 \frac{\partial^2 u}{\partial x^2} = c^2 \cdot (-\sin(x)\cos(ct)) = -c^2\sin(x)\cos(ct)$$
> 
> $$\frac{\partial^2 u}{\partial t^2} = -c^2\sin(x)\cos(ct)$$
> 
> $$\boxed{\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}}$$ ✓
> 
> La función satisface la ecuación de onda.

---

## 📊 Tabla Resumen: Reglas de Derivación

> [!note]- 📋 Reglas Útiles para Derivadas Parciales
> 
> |Regla|Fórmula|
> |---|---|
> |**Constante**|$\frac{\partial}{\partial x}(c) = 0$|
> |**Potencia**|$\frac{\partial}{\partial x}(x^n) = nx^{n-1}$|
> |**Suma**|$\frac{\partial}{\partial x}(f + g) = \frac{\partial f}{\partial x} + \frac{\partial g}{\partial x}$|
> |**Producto**|$\frac{\partial}{\partial x}(fg) = \frac{\partial f}{\partial x}g + f\frac{\partial g}{\partial x}$|
> |**Cociente**|$\frac{\partial}{\partial x}\left(\frac{f}{g}\right) = \frac{\frac{\partial f}{\partial x}g - f\frac{\partial g}{\partial x}}{g^2}$|
> |**Cadena**|$\frac{\partial}{\partial x}(f(g)) = f'(g)\frac{\partial g}{\partial x}$|
> |**Exponencial**|$\frac{\partial}{\partial x}(e^{f}) = e^{f}\frac{\partial f}{\partial x}$|
> |**Logaritmo**|$\frac{\partial}{\partial x}(\ln f) = \frac{1}{f}\frac{\partial f}{\partial x}$|
> |**Seno**|$\frac{\partial}{\partial x}(\sin f) = \cos f \cdot \frac{\partial f}{\partial x}$|
> |**Coseno**|$\frac{\partial}{\partial x}(\cos f) = -\sin f \cdot \frac{\partial f}{\partial x}$|

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular las derivadas parciales de primer orden:**
> 
> a) $f(x,y) = x^3 + 2x^2y + 3y^2$
> 
> b) $f(x,y) = xy^2 + x^2y$
> 
> c) $f(x,y) = e^{x+y}$
> 
> d) $f(x,y) = \sin(xy)$
> 
> e) $f(x,y) = x\ln(y)$
> 
> f) $f(x,y) = \frac{x}{y}$
> 
> ---
> 
> **2. Evaluar las derivadas en el punto indicado:**
> 
> a) $f(x,y) = x^2 + y^2$ en $(1,2)$
> 
> b) $f(x,y) = xe^y$ en $(2,0)$
> 
> c) $f(x,y) = \cos(x + y)$ en $(\pi/4, \pi/4)$
> 
> ---
> 
> **3. Calcular todas las derivadas de segundo orden:**
> 
> a) $f(x,y) = x^2y + xy^2$
> 
> b) $f(x,y) = e^{xy}$
> 
> c) $f(x,y) = \sin(x)\cos(y)$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Verificar el Teorema de Schwarz:**
> 
> a) $f(x,y) = x^3y^2 - 2xy^3$
> 
> b) $f(x,y) = e^{x^2+y^2}$
> 
> c) $f(x,y) = \ln(x^2 + y^2)$
> 
> ---
> 
> **5. Derivadas de funciones de tres variables:**
> 
> a) $f(x,y,z) = x^2 + y^2 + z^2$
> 
> b) $f(x,y,z) = xyz$
> 
> c) $f(x,y,z) = e^{xyz}$
> 
> ---
> 
> **6. Calcular el Laplaciano:**
> 
> a) $f(x,y) = x^2 + y^2$
> 
> b) $f(x,y) = \ln(x^2 + y^2)$
> 
> c) $f(x,y) = e^x\sin(y)$
> 
> ---
> 
> **7. Derivación implícita:**
> 
> a) Para $x^2 + y^2 + z^2 = 4$, encontrar $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$
> 
> b) Para $xyz = 1$, encontrar $\frac{\partial z}{\partial x}$ y $\frac{\partial z}{\partial y}$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **8. Verificar ecuaciones diferenciales parciales:**
> 
> a) Verificar que $u(x,t) = e^{-t}\sin(x)$ satisface la ecuación del calor: $\frac{\partial u}{\partial t} = \frac{\partial^2 u}{\partial x^2}$
> 
> b) Verificar que $u(x,y) = x^3 - 3xy^2$ satisface la ecuación de Laplace: $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$
> 
> ---
> 
> **9. Aplicaciones:**
> 
> a) La temperatura en una placa es $T(x,y) = 100 - x^2 - 2y^2$. ¿En qué dirección (x o y) disminuye más rápido la temperatura en el punto $(2,1)$?
> 
> b) La utilidad es $U(x,y) = 20x^{0.5}y^{0.5}$. Calcular las utilidades marginales cuando $x = 100$ e $y = 100$.
> 
> ---
> 
> **10. Derivadas de orden superior:**
> 
> a) Para $f(x,y) = e^{xy}$, calcular $f_{xxx}$, $f_{xyy}$, $f_{xyz}$ (¿qué es esto último?)
> 
> b) Para $f(x,y) = \sin(x + y)$, calcular todas las derivadas hasta tercer orden
> 
> ---
> 
> **11. Problemas teóricos:**
> 
> a) Demostrar que si $f(x,y) = g(x) + h(y)$, entonces $f_{xy} = 0$
> 
> b) Si $f(x,y) = x^2y + xy^2$, demostrar que $xf_x + yf_y = 3f$ (Teorema de Euler para funciones homogéneas)

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = x^3 + 2x^2y + 3y^2$
> 
> $$f_x = 3x^2 + 4xy$$ $$f_y = 2x^2 + 6y$$
> 
> ---
> 
> **1b)** $f(x,y) = xy^2 + x^2y$
> 
> $$f_x = y^2 + 2xy$$ $$f_y = 2xy + x^2$$
> 
> ---
> 
> **1c)** $f(x,y) = e^{x+y}$
> 
> $$f_x = e^{x+y}$$ $$f_y = e^{x+y}$$
> 
> ---
> 
> **1d)** $f(x,y) = \sin(xy)$
> 
> $$f_x = y\cos(xy)$$ $$f_y = x\cos(xy)$$
> 
> ---
> 
> **2a)** $f(x,y) = x^2 + y^2$ en $(1,2)$
> 
> $$f_x = 2x \implies f_x(1,2) = 2$$ $$f_y = 2y \implies f_y(1,2) = 4$$
> 
> ---
> 
> **3a)** $f(x,y) = x^2y + xy^2$
> 
> $$f_x = 2xy + y^2$$ $$f_y = x^2 + 2xy$$
> 
> $$f_{xx} = 2y$$ $$f_{yy} = 2x$$ $$f_{xy} = 2x + 2y = f_{yx}$$ ✓

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $f(x,y) = x^3y^2 - 2xy^3$
> 
> $$f_x = 3x^2y^2 - 2y^3$$ $$f_y = 2x^3y - 6xy^2$$
> 
> $$f_{xy} = 6x^2y - 6y^2$$ $$f_{yx} = 6x^2y - 6y^2$$
> 
> $$\boxed{f_{xy} = f_{yx}}$$ ✓
> 
> ---
> 
> **5a)** $f(x,y,z) = x^2 + y^2 + z^2$
> 
> $$f_x = 2x, \quad f_y = 2y, \quad f_z = 2z$$
> 
> ---
> 
> **6a)** $f(x,y) = x^2 + y^2$
> 
> $$f_{xx} = 2, \quad f_{yy} = 2$$
> 
> $$\nabla^2 f = 2 + 2 = 4$$
> 
> ---
> 
> **7a)** $x^2 + y^2 + z^2 = 4$
> 
> Derivando implícitamente con respecto a $x$: $$2x + 0 + 2z\frac{\partial z}{\partial x} = 0$$
> 
> $$\boxed{\frac{\partial z}{\partial x} = -\frac{x}{z}}$$
> 
> Análogamente: $$\boxed{\frac{\partial z}{\partial y} = -\frac{y}{z}}$$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **8a)** $u(x,t) = e^{-t}\sin(x)$
> 
> $$\frac{\partial u}{\partial t} = -e^{-t}\sin(x)$$
> 
> $$\frac{\partial u}{\partial x} = e^{-t}\cos(x)$$ $$\frac{\partial^2 u}{\partial x^2} = -e^{-t}\sin(x)$$
> 
> Comparando: $$\frac{\partial u}{\partial t} = -e^{-t}\sin(x) = \frac{\partial^2 u}{\partial x^2}$$ ✓
> 
> ---
> 
> **9a)** $T(x,y) = 100 - x^2 - 2y^2$ en $(2,1)$
> 
> $$\frac{\partial T}{\partial x} = -2x \implies \frac{\partial T}{\partial x}(2,1) = -4$$
> 
> $$\frac{\partial T}{\partial y} = -4y \implies \frac{\partial T}{\partial y}(2,1) = -4$$
> 
> **Respuesta:** La temperatura disminuye a la misma tasa en ambas direcciones.
> 
> ---
> 
> **11a)** Si $f(x,y) = g(x) + h(y)$:
> 
> $$f_x = g'(x) + 0 = g'(x)$$ $$f_{xy} = \frac{\partial}{\partial y}(g'(x)) = 0$$
> 
> Porque $g'(x)$ no depende de $y$. ✓

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Derivadas Parciales
> 
> ✅ **Definición básica:**
> 
> - $\frac{\partial f}{\partial x}$ mide la tasa de cambio de $f$ cuando solo varía $x$
> - Se calcula tratando las demás variables como constantes
> 
> ✅ **Interpretación geométrica:**
> 
> - $\frac{\partial f}{\partial x}$ es la pendiente en la dirección $x$
> - Equivale a cortar la superficie con un plano paralelo al plano $xz$
> 
> ✅ **Notación:**
> 
> - $\frac{\partial f}{\partial x} = f_x = \partial_x f = D_x f$
> - Todas son equivalentes
> 
> ---
> 
> ### Sobre Derivadas de Orden Superior
> 
> ✅ **Teorema de Schwarz:**
> 
> - Si las derivadas mixtas son continuas: $f_{xy} = f_{yx}$
> - Válido para la mayoría de funciones "bien comportadas"
> 
> ✅ **Laplaciano:**
> 
> - $\nabla^2 f = f_{xx} + f_{yy}$ (en 2D)
> - $\nabla^2 f = f_{xx} + f_{yy} + f_{zz}$ (en 3D)
> - Fundamental en física y ecuaciones diferenciales
> 
> ---
> 
> ### Advertencias Importantes
> 
> ⚠️ **Existencia de derivadas parciales ≠ Continuidad** ⚠️ **Continuidad ≠ Existencia de derivadas parciales** ⚠️ **Derivadas parciales continuas → Continuidad de $f$**
> 
> ---
> 
> ### Aplicaciones
> 
> 📍 **Física:** Gradientes, ecuaciones de onda, calor, Laplace 📍 **Economía:** Utilidades marginales, productividades marginales 📍 **Ingeniería:** Tasas de cambio en sistemas multivariables 📍 **Optimización:** Condiciones necesarias para extremos

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema es prerequisito para:**
> 
> - [[09 - Diferenciabilidad]] - Derivadas parciales continuas → diferenciabilidad
> - [[10 - Regla de la Cadena]] - Composición de funciones diferenciables
> - [[11 - Gradiente]] - Vector formado por derivadas parciales
> - [[12 - Derivadas Direccionales]] - Generalización de derivadas parciales
> - [[15 - Optimización]] - Condiciones de primer y segundo orden
> - [[16 - Multiplicadores de Lagrange]] - Optimización con restricciones
> 
> **Conceptos relacionados:**
> 
> - **Límites** - Base de la definición de derivada
> - **Continuidad** - Relación sutil con derivabilidad
> - **Diferenciabilidad** - Concepto más fuerte que derivadas parciales
> - **Ecuaciones Diferenciales Parciales** - Usan extensivamente derivadas parciales
> 
> **Siguiente tema recomendado:** [[09 - Diferenciabilidad y Plano Tangente]]

---

## 📝 Notas Finales

> [!note]- 🎯 Reflexiones sobre Derivadas Parciales
> 
> ### Importancia Conceptual
> 
> Las derivadas parciales son la **primera generalización** del concepto de derivada a múltiples variables:
> 
> - En 1D: una derivada mide **la** tasa de cambio
> - En 2D+: derivadas parciales miden tasas de cambio en **direcciones coordenadas**
> - Son la base para conceptos más generales (gradiente, derivada direccional)
> 
> ---
> 
> ### Limitaciones
> 
> Las derivadas parciales por sí solas **no capturan toda la información** sobre el cambio de una función:
> 
> - Solo miden cambios en direcciones paralelas a los ejes
> - No garantizan comportamiento suave (continuidad)
> - No proporcionan una aproximación lineal completa
> 
> Por eso necesitamos el concepto de **diferenciabilidad** (próximo tema).
> 
> ---
> 
> ### Visualización  
> **Pensar en derivadas parciales como:**
> 
> - "Rebanadas" de la superficie
> - Pendientes en direcciones específicas
> - Tasas de cambio instantáneas cuando una variable se mueve
> 
> **Analogía:** Si caminas sobre una montaña (superficie):
> 
> - $\frac{\partial f}{\partial x}$ = qué tan empinado es si caminas hacia el Este
> - $\frac{\partial f}{\partial y}$ = qué tan empinado es si caminas hacia el Norte
> - Pero podrías caminar en cualquier dirección → necesitamos derivadas direccionales
> 
> ---
> 
> ### Para Profundizar
> 
> **Conceptos avanzados:**
> 
> - Derivadas de Fréchet y Gâteaux (análisis funcional)
> - Derivadas débiles (teoría de distribuciones)
> - Derivadas covariantes (geometría diferencial)
> - Cálculo de variaciones
> 
> **Aplicaciones avanzadas:**
> 
> - Ecuaciones en derivadas parciales (EDP)
> - Física matemática (mecánica cuántica, relatividad)
> - Aprendizaje automático (descenso de gradiente)
> - Optimización numérica

---

## 🧮 Fórmulas de Referencia Rápida

> [!note]- 📋 Tabla de Referencia: Derivadas Parciales Comunes
> 
> |Función $f(x,y)$|$\frac{\partial f}{\partial x}$|$\frac{\partial f}{\partial y}$|
> |---|---|---|
> |$x^n$|$nx^{n-1}$|$0$|
> |$y^n$|$0$|$ny^{n-1}$|
> |$xy$|$y$|$x$|
> |$x^2 + y^2$|$2x$|$2y$|
> |$xy^2$|$y^2$|$2xy$|
> |$e^x$|$e^x$|$0$|
> |$e^y$|$0$|$e^y$|
> |$e^{xy}$|$ye^{xy}$|$xe^{xy}$|
> |$\sin(x)$|$\cos(x)$|$0$|
> |$\sin(y)$|$0$|$\cos(y)$|
> |$\sin(xy)$|$y\cos(xy)$|$x\cos(xy)$|
> |$\ln(x)$|$\frac{1}{x}$|$0$|
> |$\ln(x^2+y^2)$|$\frac{2x}{x^2+y^2}$|$\frac{2y}{x^2+y^2}$|
> |$\frac{x}{y}$|$\frac{1}{y}$|$-\frac{x}{y^2}$|
> |$\sqrt{x^2+y^2}$|$\frac{x}{\sqrt{x^2+y^2}}$|$\frac{y}{\sqrt{x^2+y^2}}$|

---

## 💡 Trucos y Técnicas Útiles

> [!tip]- 🎯 Estrategias para Derivadas Parciales
> 
> ### Truco 1: Identificar qué es constante
> 
> Antes de derivar, **subraya mentalmente** qué variables son constantes:
> 
> Para $\frac{\partial}{\partial x}$: subraya todas las $y$, $z$, etc.
> 
> **Ejemplo:** $f(x,y) = x^2\underline{y} + 3\underline{y^2}$
> 
> Al derivar con respecto a $x$:
> 
> - $x^2\underline{y}$ se comporta como $(constante) \cdot x^2$
> - $3\underline{y^2}$ es solo una constante
> 
> ---
> 
> ### Truco 2: Usar simetría
> 
> Si $f(x,y)$ es simétrica en $x$ e $y$, entonces puedes obtener $\frac{\partial f}{\partial y}$ intercambiando $x \leftrightarrow y$ en $\frac{\partial f}{\partial x}$.
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2$
> 
> - $f_x = 2x$
> - Por simetría: $f_y = 2y$
> 
> ---
> 
> ### Truco 3: Verificar dimensiones
> 
> Las derivadas parciales cambian las **dimensiones/unidades**:
> 
> Si $f$ tiene unidades [U] y $x$ tiene unidades [X]: $$\left[\frac{\partial f}{\partial x}\right] = \frac{[U]}{[X]}$$
> 
> **Ejemplo:** Si $T(x,y)$ es temperatura en °C y $x, y$ en metros: $$\left[\frac{\partial T}{\partial x}\right] = \frac{\text{°C}}{\text{m}}$$
> 
> ---
> 
> ### Truco 4: Patrón de exponenciales
> 
> Para $f(x,y) = e^{g(x,y)}$: $$\frac{\partial f}{\partial x} = e^{g(x,y)} \cdot \frac{\partial g}{\partial x} = f \cdot g_x$$
> 
> **Útil recordar:** La derivada de una exponencial es "ella misma por la derivada del exponente"
> 
> ---
> 
> ### Truco 5: Logaritmos
> 
> Para funciones complicadas con productos/cocientes, a veces ayuda tomar logaritmo primero:
> 
> $$f(x,y) = \frac{x^a y^b}{z^c} \implies \ln f = a\ln x + b\ln y - c\ln z$$
> 
> Luego derivar y despejar.

---

## 🔬 Casos Especiales y Patológicos

> [!warning]- ⚠️ Funciones Problemáticas
> 
> ### Caso 1: Derivadas parciales existen pero $f$ no es continua
> 
> **Ejemplo clásico:** $$f(x,y) = \begin{cases} \frac{xy}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$$
> 
> - $f_x(0,0) = 0$ y $f_y(0,0) = 0$ (existen)
> - Pero $\lim_{(x,y) \to (0,0)} f(x,y)$ no existe
> - Por lo tanto, $f$ **no es continua** en el origen
> 
> ---
> 
> ### Caso 2: $f$ continua pero derivadas no existen
> 
> **Ejemplo:** $$f(x,y) = \sqrt{x^2 + y^2}$$
> 
> - $f$ es continua en todo $\mathbb{R}^2$
> - En $(0,0)$: $f_x$ y $f_y$ **no existen** (no son diferenciables)
> 
> ---
> 
> ### Caso 3: Derivadas parciales existen pero no son continuas
> 
> **Ejemplo:** $$f(x,y) = \begin{cases} (x^2+y^2)\sin\left(\frac{1}{\sqrt{x^2+y^2}}\right) & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$$
> 
> - Todas las derivadas parciales existen
> - Pero oscilan violentamente cerca del origen
> - No son continuas en $(0,0)$
> 
> ---
> 
> ### Caso 4: Derivadas mixtas no conmutan
> 
> **Ejemplo (raro pero existe):** $$f(x,y) = \begin{cases} \frac{xy(x^2-y^2)}{x^2+y^2} & (x,y) \neq (0,0) \ 0 & (x,y) = (0,0) \end{cases}$$
> 
> En el origen:
> 
> - $f_{xy}(0,0) = 1$
> - $f_{yx}(0,0) = -1$
> 
> **Razón:** Las derivadas mixtas no son continuas, por lo que el Teorema de Schwarz no aplica.

---

## 📐 Notación Alternativa: Operadores Diferenciales

> [!note]- 🔢 Notación de Operadores
> 
> ### Operador Nabla (∇)
> 
> El **gradiente** de $f$ se denota: $$\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$
> 
> (Tema del próximo capítulo)
> 
> ---
> 
> ### Operador Laplaciano (∇² o Δ)
> 
> $$\nabla^2 f = \Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$
> 
> En 3D: $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$
> 
> ---
> 
> ### Operador D'Alembertian (□)
> 
> En física (relatividad especial): $$\Box f = \frac{1}{c^2}\frac{\partial^2 f}{\partial t^2} - \nabla^2 f$$
> 
> ---
> 
> ### Notación de Índices
> 
> En física y geometría diferencial:
> 
> - $\partial_i f = \frac{\partial f}{\partial x^i}$ (derivada parcial con respecto a la i-ésima coordenada)
> - $\partial_i \partial_j f = f_{ij}$ (derivada de segundo orden)
> 
> **Ejemplo:** En 3D con coordenadas $(x^1, x^2, x^3) = (x, y, z)$:
> 
> - $\partial_1 f = \frac{\partial f}{\partial x}$
> - $\partial_2 f = \frac{\partial f}{\partial y}$
> - $\partial_3 f = \frac{\partial f}{\partial z}$

---

## 🎨 Visualización de Derivadas Parciales

> [!note]- 🖼️ Interpretación Gráfica Detallada
> 
> ### Superficie y Cortes
> 
> Para $z = f(x,y) = x^2 + y^2$ (paraboloide):
> 
> ```
>         z
>         |
>       8 |        •
>         |       /|\
>       6 |      / | \
>         |     /  |  \
>       4 |    /   |   \
>         |   /    |    \
>       2 |  /     |     \
>         | /      |      \
>       0 +--------+-------- y
>        /         2
>       /
>      x    2
> ```
> 
> ---
> 
> ### Corte y = 2 (derivada con respecto a x)
> 
> ```
>         z
>         |
>       8 |      /
>         |     /
>       6 |    /  ← Pendiente en x=2: f_x(2,2) = 4
>         |   /
>       4 |  •
>         | /
>       2 |/
>         +--------- x
>               2
> ```
> 
> La curva es $z = x^2 + 4$, y su pendiente en $x=2$ es $f_x(2,2) = 2(2) = 4$.
> 
> ---
> 
> ### Corte x = 2 (derivada con respecto a y)
> 
> ```
>         z
>         |
>       8 |      /
>         |     /
>       6 |    /  ← Pendiente en y=2: f_y(2,2) = 4
>         |   /
>       4 |  •
>         | /
>       2 |/
>         +--------- y
>               2
> ```
> 
> La curva es $z = 4 + y^2$, y su pendiente en $y=2$ es $f_y(2,2) = 2(2) = 4$.
> 
> ---
> 
> ### Plano Tangente (adelanto)
> 
> Las dos derivadas parciales determinan el **plano tangente** a la superficie en el punto.
> 
> Ecuación del plano tangente en $(x_0, y_0)$: $$z - f(x_0,y_0) = f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)$$

---

## 🔄 Derivadas Parciales en Coordenadas Polares

> [!note]- 🌀 Cambio de Coordenadas
> 
> ### Transformación
> 
> Coordenadas polares: $$x = r\cos\theta, \quad y = r\sin\theta$$
> 
> Si $f(x,y)$ se expresa en polares como $g(r,\theta)$, entonces:
> 
> ---
> 
> ### Relación entre derivadas
> 
> **Del teorema de la cadena (tema futuro):**
> 
> $$\frac{\partial f}{\partial x} = \frac{\partial g}{\partial r}\frac{\partial r}{\partial x} + \frac{\partial g}{\partial \theta}\frac{\partial \theta}{\partial x}$$
> 
> $$\frac{\partial f}{\partial y} = \frac{\partial g}{\partial r}\frac{\partial r}{\partial y} + \frac{\partial g}{\partial \theta}\frac{\partial \theta}{\partial y}$$
> 
> **Donde:**
> 
> - $\frac{\partial r}{\partial x} = \cos\theta$
> - $\frac{\partial r}{\partial y} = \sin\theta$
> - $\frac{\partial \theta}{\partial x} = -\frac{\sin\theta}{r}$
> - $\frac{\partial \theta}{\partial y} = \frac{\cos\theta}{r}$
> 
> ---
> 
> ### Laplaciano en polares
> 
> $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = \frac{\partial^2 g}{\partial r^2} + \frac{1}{r}\frac{\partial g}{\partial r} + \frac{1}{r^2}\frac{\partial^2 g}{\partial \theta^2}$$
> 
> Esta es una fórmula importante en física (problemas con simetría circular).

---

## 📚 Ecuaciones Diferenciales Parciales Importantes

> [!note]- 🎓 EDPs Clásicas
> 
> ### 1. Ecuación de Laplace (estacionaria)
> 
> $$\nabla^2 u = 0$$
> 
> $$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$
> 
> **Aplicaciones:**
> 
> - Potencial electrostático
> - Flujo de fluidos incompresibles
> - Temperatura en estado estacionario
> 
> **Soluciones:** Funciones armónicas
> 
> ---
> 
> ### 2. Ecuación del Calor (parabólica)
> 
> $$\frac{\partial u}{\partial t} = k\nabla^2 u$$
> 
> En 1D: $$\frac{\partial u}{\partial t} = k\frac{\partial^2 u}{\partial x^2}$$
> 
> **Aplicaciones:**
> 
> - Conducción de calor
> - Difusión de partículas
> 
> **Solución típica:** $u(x,t) = e^{-kt}\sin(x)$
> 
> ---
> 
> ### 3. Ecuación de Onda (hiperbólica)
> 
> $$\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u$$
> 
> En 1D: $$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$
> 
> **Aplicaciones:**
> 
> - Ondas en cuerdas
> - Ondas sonoras
> - Ondas electromagnéticas
> 
> **Solución típica:** $u(x,t) = \sin(kx - \omega t)$
> 
> ---
> 
> ### 4. Ecuación de Poisson
> 
> $$\nabla^2 u = f$$
> 
> **Aplicaciones:**
> 
> - Potencial gravitatorio
> - Potencial eléctrico con cargas
> 
> **Caso especial:** Cuando $f = 0$, es la ecuación de Laplace.

---

## 🎯 Resumen Visual: Árbol de Conceptos

> [!note]- 🌳 Mapa Conceptual
> 
> ```
> DERIVADAS PARCIALES
> │
> ├─ DEFINICIÓN
> │  ├─ Límite cuando h→0
> │  ├─ Mantener otras variables constantes
> │  └─ Notación: ∂f/∂x, f_x, D_x f
> │
> ├─ CÁLCULO
> │  ├─ Tratar otras variables como constantes
> │  ├─ Usar reglas de derivación usuales
> │  └─ Regla de la cadena
> │
> ├─ INTERPRETACIÓN
> │  ├─ Geométrica: pendiente de curva de corte
> │  ├─ Física: tasa de cambio instantánea
> │  └─ Aplicada: marginal/sensibilidad
> │
> ├─ ORDEN SUPERIOR
> │  ├─ Derivadas puras: f_xx, f_yy
> │  ├─ Derivadas mixtas: f_xy, f_yx
> │  └─ Teorema de Schwarz: f_xy = f_yx
> │
> ├─ OPERADORES
> │  ├─ Laplaciano: ∇²f
> │  ├─ Gradiente: ∇f (próximo tema)
> │  └─ D'Alembertian: □
> │
> └─ APLICACIONES
>    ├─ Ecuaciones diferenciales parciales
>    ├─ Optimización (condiciones necesarias)
>    ├─ Física (leyes de conservación)
>    └─ Economía (análisis marginal)
> ```

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **Derivadas parciales = derivadas con respecto a una variable manteniendo las demás fijas**
>     
> 2. **Existen múltiples derivadas parciales** (una por cada variable independiente)
>     
> 3. **Son la base para conceptos más avanzados:**
>     
>     - Gradiente
>     - Derivadas direccionales
>     - Diferenciabilidad
>     - Optimización
> 4. **El Teorema de Schwarz es tu amigo** (derivadas mixtas conmutan bajo condiciones razonables)
>     
> 5. **No confundir:**
>     
>     - Derivadas parciales ≠ Diferenciabilidad
>     - Derivadas parciales ≠ Continuidad
> 
> ---
> 
> ### Próximos Pasos
> 
> Con derivadas parciales dominadas, estás listo para:
> 
> - **Diferenciabilidad:** Aproximación lineal completa
> - **Gradiente:** Vector de derivadas parciales
> - **Derivadas direccionales:** Generalización a cualquier dirección
> - **Plano tangente:** Mejor aproximación lineal a la superficie
> - **Optimización:** Encontrar máximos y mínimos
> 
> ---
> 
> ### Práctica Recomendada
> 
> - Calcular derivadas de muchas funciones diferentes
> - Visualizar geométricamente cuando sea posible
> - Verificar el Teorema de Schwarz en ejemplos
> - Resolver problemas aplicados (física, economía)
> - Practicar derivadas de orden superior

---

**Tags:** #calculo-multivariable #derivadas-parciales #funciones-varias-variables #teorema-schwarz #laplaciano #ecuaciones-diferenciales-parciales #gradiente #optimizacion #fisica-matematica
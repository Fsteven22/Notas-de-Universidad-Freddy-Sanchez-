# 📘 Definición y Clasificación de Funciones de Varias Variables

## 🎯 Introducción

> [!info]- 💡 Del Cálculo de Una Variable al Cálculo Multivariable Hasta ahora hemos trabajado con funciones de **una variable**: $f(x) = x^2$, donde tenemos una entrada y una salida.
> 
> Ahora extendemos estos conceptos a funciones de **varias variables**: $f(x,y) = x^2 + y^2$, donde tenemos múltiples entradas.
> 
> **¿Por qué es importante?**
> 
> - 🌡️ La temperatura depende de posición (x, y, z) y tiempo (t)
> - 💰 El costo de producción depende de mano de obra y capital
> - 🎮 La posición de un objeto en un juego depende de x, y, z
> - 📊 Los datos reales casi siempre dependen de múltiples factores

---

## 📐 Función Escalar

### 🔍 Definición

> [!example]- 🟢 Función Escalar: $f: \mathbb{R}^n \to \mathbb{R}$
> 
> **Definición formal:** Una **función escalar de $n$ variables** es una regla que asigna a cada punto $(x_1, x_2, ..., x_n)$ en $\mathbb{R}^n$ exactamente **un número real** $w$.
> 
> $$f: \mathbb{R}^n \to \mathbb{R}$$
> 
> **Notación según número de variables:**
> 
> |Variables|Notación|Se lee como|
> |---|---|---|
> |2 variables|$z = f(x,y)$|"z es función de x e y"|
> |3 variables|$w = f(x,y,z)$|"w es función de x, y y z"|
> |n variables|$w = f(x_1, x_2, ..., x_n)$|"w es función de x-sub-1 hasta x-sub-n"|
> 
> **Componentes:**
> 
> - **Variables independientes:** $x, y, z, ...$ (entrada)
> - **Variable dependiente:** $z, w$ (salida)
> - **Regla de correspondencia:** la fórmula o expresión

### 📚 Ejemplos Fundamentales

> [!example]- 📝 Ejemplo 1: Función de Dos Variables
> 
> **Función:** $f(x,y) = x^2 + y^2$
> 
> **Análisis:**
> 
> - **Entrada:** Un punto $(x,y)$ del plano $\mathbb{R}^2$
> - **Salida:** Un número real (la suma de los cuadrados)
> - **Dominio:** $\mathbb{R}^2$ (todos los puntos del plano)
> - **Rango:** $[0, +\infty)$ (solo valores no negativos)
> 
> **Evaluaciones:**
> 
> - $f(1, 2) = 1^2 + 2^2 = 1 + 4 = 5$
> - $f(0, 0) = 0^2 + 0^2 = 0$
> - $f(-3, 4) = (-3)^2 + 4^2 = 9 + 16 = 25$
> - $f(a, b) = a^2 + b^2$
> 
> **Interpretación geométrica:** Esta función representa la **distancia al cuadrado** desde el punto $(x,y)$ al origen $(0,0)$.

> [!example]- 📝 Ejemplo 2: Temperatura en una Placa
> 
> **Función:** $T(x,y) = 100 - x^2 - 2y^2$
> 
> **Contexto:** Imagina una placa metálica donde:
> 
> - $(x,y)$ representa la posición en la placa
> - $T(x,y)$ es la temperatura en grados Celsius en ese punto
> 
> **Análisis:**
> 
> - En el origen: $T(0,0) = 100°C$ (punto más caliente)
> - Alejándonos del origen, la temperatura disminuye
> - $T(1,1) = 100 - 1 - 2 = 97°C$
> - $T(2,2) = 100 - 4 - 8 = 88°C$
> 
> **Observación:** La temperatura disminuye más rápido en la dirección $y$ que en $x$ (coeficiente 2 vs 1).

> [!example]- 📝 Ejemplo 3: Función de Tres Variables
> 
> **Función:** $f(x,y,z) = x^2 + y^2 + z^2$
> 
> **Análisis:**
> 
> - **Entrada:** Un punto $(x,y,z)$ del espacio $\mathbb{R}^3$
> - **Salida:** Un número real
> - **Interpretación:** Distancia al cuadrado desde $(x,y,z)$ hasta el origen
> 
> **Evaluaciones:**
> 
> - $f(1,2,2) = 1 + 4 + 4 = 9$
> - $f(0,0,0) = 0$
> - $f(1,1,1) = 3$
> 
> **Aplicación física:** Si $f$ representa el potencial gravitatorio, entonces puntos equidistantes del origen tienen el mismo potencial (superficies equipotenciales esféricas).

> [!example]- 📝 Ejemplo 4: Índice de Masa Corporal (IMC)
> 
> **Función:** $\text{IMC}(m, h) = \frac{m}{h^2}$
> 
> Donde:
> 
> - $m$ = masa en kilogramos
> - $h$ = altura en metros
> 
> **Evaluaciones:**
> 
> - Persona de 70 kg y 1.75 m: $\text{IMC}(70, 1.75) = \frac{70}{1.75^2} = \frac{70}{3.0625} \approx 22.86$
> - Persona de 80 kg y 1.80 m: $\text{IMC}(80, 1.80) = \frac{80}{3.24} \approx 24.69$
> 
> **Interpretación:**
> 
> - IMC < 18.5: Bajo peso
> - 18.5 ≤ IMC < 25: Normal
> - IMC ≥ 25: Sobrepeso

> [!example]- 📝 Ejemplo 5: Volumen de un Cilindro
> 
> **Función:** $V(r, h) = \pi r^2 h$
> 
> Donde:
> 
> - $r$ = radio de la base
> - $h$ = altura del cilindro
> 
> **Evaluaciones:**
> 
> - $V(2, 5) = \pi(2)^2(5) = 20\pi \approx 62.83$ unidades cúbicas
> - $V(3, 10) = \pi(3)^2(10) = 90\pi \approx 282.74$ unidades cúbicas
> 
> **Observación:** El volumen depende de **dos variables independientes**: si duplicamos el radio, el volumen se cuadruplica; si duplicamos la altura, el volumen se duplica.

### 🎨 Ejemplos con Restricciones de Dominio

> [!warning]- ⚠️ Funciones con Dominio Restringido
> 
> **Ejemplo 6: Raíz cuadrada** $$f(x,y) = \sqrt{9 - x^2 - y^2}$$
> 
> **Restricción:** El radicando debe ser no negativo $$9 - x^2 - y^2 \geq 0$$ $$x^2 + y^2 \leq 9$$
> 
> **Dominio:** Disco cerrado de radio 3 centrado en el origen $$\text{Dom}(f) = {(x,y) \in \mathbb{R}^2 : x^2 + y^2 \leq 9}$$
> 
> **Interpretación geométrica:** La función está definida solo dentro y sobre el círculo de radio 3.
> 
> ---
> 
> **Ejemplo 7: Logaritmo** $$g(x,y) = \ln(xy)$$
> 
> **Restricción:** El argumento del logaritmo debe ser positivo $$xy > 0$$
> 
> **Dominio:** $$\text{Dom}(g) = {(x,y) : xy > 0} = {(x,y) : \text{ambos + o ambos -}}$$
> 
> Primer y tercer cuadrante (sin los ejes).
> 
> ---
> 
> **Ejemplo 8: División** $$h(x,y) = \frac{x^2 + y^2}{x - y}$$
> 
> **Restricción:** El denominador no puede ser cero $$x - y \neq 0$$ $$x \neq y$$
> 
> **Dominio:** Todo $\mathbb{R}^2$ excepto la recta $y = x$ $$\text{Dom}(h) = {(x,y) \in \mathbb{R}^2 : x \neq y}$$

---

## 🎯 Función Vectorial

### 🔍 Definición

> [!example]- 🔵 Función Vectorial: $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$
> 
> **Definición formal:** Una **función vectorial** asigna a cada punto en $\mathbb{R}^n$ un **vector** en $\mathbb{R}^m$.
> 
> $$\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$$
> 
> **Notación:** $$\vec{F}(x_1, ..., x_n) = \langle f_1(x_1, ..., x_n), f_2(x_1, ..., x_n), ..., f_m(x_1, ..., x_n) \rangle$$
> 
> O también: $$\vec{F}(x,y) = f_1(x,y)\vec{i} + f_2(x,y)\vec{j}$$ $$\vec{F}(x,y,z) = f_1(x,y,z)\vec{i} + f_2(x,y,z)\vec{j} + f_3(x,y,z)\vec{k}$$
> 
> **Componentes:** Cada función vectorial se compone de $m$ **funciones escalares** llamadas **funciones componente**:
> 
> - $f_1, f_2, ..., f_m$ son funciones escalares
> - Cada $f_i: \mathbb{R}^n \to \mathbb{R}$

### 📚 Ejemplos de Funciones Vectoriales

> [!example]- 📝 Ejemplo 1: Campo Vectorial en el Plano ($\mathbb{R}^2 \to \mathbb{R}^2$)
> 
> **Función:** $\vec{F}(x,y) = \langle -y, x \rangle$
> 
> O equivalentemente: $$\vec{F}(x,y) = -y\vec{i} + x\vec{j}$$
> 
> **Análisis:**
> 
> - **Entrada:** Punto $(x,y)$ en el plano
> - **Salida:** Vector $\langle -y, x \rangle$ en ese punto
> 
> **Evaluaciones:**
> 
> - $\vec{F}(1,0) = \langle 0, 1 \rangle$ → vector hacia arriba
> - $\vec{F}(0,1) = \langle -1, 0 \rangle$ → vector hacia la izquierda
> - $\vec{F}(1,1) = \langle -1, 1 \rangle$ → vector diagonal
> - $\vec{F}(2,3) = \langle -3, 2 \rangle$
> 
> **Interpretación física:** Este campo vectorial representa una **rotación antihoraria** alrededor del origen. Imagina un fluido girando.

> [!example]- 📝 Ejemplo 2: Curva Parametrizada ($\mathbb{R} \to \mathbb{R}^2$)
> 
> **Función:** $\vec{r}(t) = \langle \cos(t), \sin(t) \rangle$
> 
> **Análisis:**
> 
> - **Entrada:** Parámetro $t \in \mathbb{R}$ (escalar)
> - **Salida:** Punto $(x,y)$ en el plano (vector)
> 
> **Evaluaciones:**
> 
> - $\vec{r}(0) = \langle 1, 0 \rangle$ → punto $(1,0)$
> - $\vec{r}(\pi/2) = \langle 0, 1 \rangle$ → punto $(0,1)$
> - $\vec{r}(\pi) = \langle -1, 0 \rangle$ → punto $(-1,0)$
> - $\vec{r}(2\pi) = \langle 1, 0 \rangle$ → vuelve al inicio
> 
> **Interpretación geométrica:** La función traza el **círculo unitario** en sentido antihorario conforme $t$ aumenta.
> 
> **Verificación:** $$x^2 + y^2 = \cos^2(t) + \sin^2(t) = 1$$

> [!example]- 📝 Ejemplo 3: Hélice en el Espacio ($\mathbb{R} \to \mathbb{R}^3$)
> 
> **Función:** $\vec{r}(t) = \langle \cos(t), \sin(t), t \rangle$
> 
> **Análisis:**
> 
> - **Entrada:** Parámetro $t$
> - **Salida:** Punto $(x,y,z)$ en el espacio
> 
> **Evaluaciones:**
> 
> - $\vec{r}(0) = \langle 1, 0, 0 \rangle$
> - $\vec{r}(\pi) = \langle -1, 0, \pi \rangle$
> - $\vec{r}(2\pi) = \langle 1, 0, 2\pi \rangle$
> 
> **Interpretación:**
> 
> - En el plano $xy$: traza un círculo (como Ejemplo 2)
> - En $z$: aumenta linealmente con $t$
> - **Resultado:** Una espiral ascendente (hélice)
> 
> **Aplicación:** Modelo del resorte, escalera de caracol, ADN.

> [!example]- 📝 Ejemplo 4: Campo Gravitatorio ($\mathbb{R}^3 \to \mathbb{R}^3$)
> 
> **Función:** $$\vec{F}(x,y,z) = -\frac{GM}{(x^2+y^2+z^2)^{3/2}}\langle x, y, z \rangle$$
> 
> Donde:
> 
> - $G$ = constante gravitacional
> - $M$ = masa del objeto central
> 
> **Análisis:**
> 
> - **Entrada:** Posición $(x,y,z)$ en el espacio
> - **Salida:** Vector fuerza gravitatoria en ese punto
> 
> **Características:**
> 
> - El vector siempre apunta **hacia el origen** (signo negativo)
> - La magnitud disminuye con el cuadrado de la distancia
> - Es proporcional a la masa $M$
> 
> **Interpretación física:** Describe el campo gravitatorio creado por un objeto masivo en el origen.

> [!example]- 📝 Ejemplo 5: Campo de Velocidades ($\mathbb{R}^2 \to \mathbb{R}^2$)
> 
> **Función:** $\vec{v}(x,y) = \langle 2y, -x \rangle$
> 
> **Interpretación:** Velocidad de un fluido en cada punto $(x,y)$.
> 
> **Evaluaciones:**
> 
> - En $(1,0)$: $\vec{v}(1,0) = \langle 0, -1 \rangle$ → fluye hacia abajo
> - En $(0,1)$: $\vec{v}(0,1) = \langle 2, 0 \rangle$ → fluye a la derecha
> - En $(2,3)$: $\vec{v}(2,3) = \langle 6, -2 \rangle$
> 
> **Aplicación:** Modelar corrientes de agua, viento, campos eléctricos.

> [!example]- 📝 Ejemplo 6: Transformación Lineal ($\mathbb{R}^2 \to \mathbb{R}^2$)
> 
> **Función:** $\vec{T}(x,y) = \langle 2x + y, x - 3y \rangle$
> 
> **Análisis:**
> 
> - Transforma vectores del plano en otros vectores del plano
> - Es una transformación lineal (se puede representar como matriz)
> 
> **Evaluaciones:**
> 
> - $\vec{T}(1,0) = \langle 2, 1 \rangle$
> - $\vec{T}(0,1) = \langle 1, -3 \rangle$
> - $\vec{T}(2,3) = \langle 7, -7 \rangle$
> 
> **Forma matricial:** $$\vec{T}\begin{pmatrix} x \ y \end{pmatrix} = \begin{pmatrix} 2 & 1 \ 1 & -3 \end{pmatrix}\begin{pmatrix} x \ y \end{pmatrix}$$

---

## 📊 Clasificación General

> [!note]- 🗂️ Tabla de Clasificación
> 
> |Tipo|Entrada → Salida|Notación|Ejemplo|
> |---|---|---|---|
> |**Escalar de 2 var**|$\mathbb{R}^2 \to \mathbb{R}$|$z = f(x,y)$|$f(x,y) = x^2 + y^2$|
> |**Escalar de 3 var**|$\mathbb{R}^3 \to \mathbb{R}$|$w = f(x,y,z)$|$f(x,y,z) = xyz$|
> |**Escalar de n var**|$\mathbb{R}^n \to \mathbb{R}$|$w = f(\vec{x})$|$f(\vec{x}) = \|\vec{x}\|$|
> |**Curva en plano**|$\mathbb{R} \to \mathbb{R}^2$|$\vec{r}(t)$|$\langle \cos t, \sin t \rangle$|
> |**Curva en espacio**|$\mathbb{R} \to \mathbb{R}^3$|$\vec{r}(t)$|$\langle t, t^2, t^3 \rangle$|
> |**Campo vectorial 2D**|$\mathbb{R}^2 \to \mathbb{R}^2$|$\vec{F}(x,y)$|$\langle -y, x \rangle$|
> |**Campo vectorial 3D**|$\mathbb{R}^3 \to \mathbb{R}^3$|$\vec{F}(x,y,z)$|$\langle x, y, z \rangle$|
> |**Superficie param.**|$\mathbb{R}^2 \to \mathbb{R}^3$|$\vec{r}(u,v)$|$\langle u\cos v, u\sin v, u^2 \rangle$|

---

## ⚖️ Comparación: Escalar vs Vectorial

> [!tip]- 🔄 Diferencias Clave
> 
> ### Función Escalar
> 
> **Características:**
> 
> - ✅ La salida es **un número**
> - ✅ Se representa como superficie o curvas de nivel
> - ✅ Tiene una sola derivada parcial por variable
> - ✅ El gradiente es un vector
> 
> **Ejemplos típicos:**
> 
> - Temperatura: $T(x,y,z)$
> - Presión: $P(x,y,z)$
> - Densidad: $\rho(x,y,z)$
> - Energía potencial: $U(x,y,z)$
> 
> **Visualización:** Mapa de contorno, superficie en 3D
> 
> ---
> 
> ### Función Vectorial
> 
> **Características:**
> 
> - ✅ La salida es **un vector** (múltiples componentes)
> - ✅ Se representa como campo de vectores
> - ✅ Cada componente es una función escalar
> - ✅ Tiene divergencia y rotacional
> 
> **Ejemplos típicos:**
> 
> - Velocidad de fluido: $\vec{v}(x,y,z)$
> - Campo eléctrico: $\vec{E}(x,y,z)$
> - Campo magnético: $\vec{B}(x,y,z)$
> - Fuerza: $\vec{F}(x,y,z)$
> 
> **Visualización:** Flechas en cada punto del espacio

---

## 🎓 Propiedades Importantes

> [!success]- ⭐ Relaciones entre Escalares y Vectoriales
> 
> **1. Descomposición de función vectorial:** Toda función vectorial es un conjunto de funciones escalares: $$\vec{F}(x,y) = \langle f_1(x,y), f_2(x,y) \rangle$$ donde $f_1$ y $f_2$ son escalares.
> 
> **2. Gradiente convierte escalar en vectorial:** $$f: \mathbb{R}^n \to \mathbb{R} \quad \Rightarrow \quad \nabla f: \mathbb{R}^n \to \mathbb{R}^n$$
> 
> **3. Divergencia convierte vectorial en escalar:** $$\vec{F}: \mathbb{R}^3 \to \mathbb{R}^3 \quad \Rightarrow \quad \nabla \cdot \vec{F}: \mathbb{R}^3 \to \mathbb{R}$$
> 
> **4. Rotacional mantiene vectorial:** $$\vec{F}: \mathbb{R}^3 \to \mathbb{R}^3 \quad \Rightarrow \quad \nabla \times \vec{F}: \mathbb{R}^3 \to \mathbb{R}^3$$

---

## 📝 Ejercicios Propuestos

> [!example]- 💪 Práctica
> 
> **Básicos:**
> 
> 1. Evaluar $f(x,y) = x^3y + xy^2$ en $(2,1)$ y $(-1,3)$
> 2. Determinar si $g(x,y,z) = xyz$ es escalar o vectorial
> 3. Evaluar $\vec{r}(t) = \langle t^2, 2t, 1 \rangle$ en $t=1$ y $t=-2$
> 
> **Intermedios:** 4. Encontrar el dominio de $f(x,y) = \frac{1}{\sqrt{4-x^2-y^2}}$ 5. Graficar el campo vectorial $\vec{F}(x,y) = \langle x, y \rangle$ 6. Describir la curva $\vec{r}(t) = \langle 3\cos t, 3\sin t, 4t \rangle$
> 
> **Avanzados:** 7. Clasificar las siguientes funciones y determinar $n$ y $m$:
> 
> - $f(x,y,z,w) = x^2 + y^2 + z^2 + w^2$
> - $\vec{G}(s,t) = \langle s+t, s-t, st \rangle$
> 
> 8. Proponer una función escalar que modele la temperatura en una habitación
> 9. Proponer una función vectorial que modele el viento en una ciudad

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones
> 
> **Este tema es base para:**
> 
> - [[02 - Dominio y Rango]] - Determinar dónde están definidas
> - [[03 - Gráfico de Funciones]] - Visualizar funciones escalares
> - [[04 - Curvas de Nivel]] - Representar funciones de 2 variables
> - [[08 - Derivadas Parciales]] - Calcular tasas de cambio
> - [[11 - Gradiente]] - Vector de derivadas parciales
> 
> **Prerequisitos:**
> 
> - Funciones de una variable
> - Vectores en $\mathbb{R}^n$
> - Álgebra vectorial básica

---

**Tags:** #calculo-multivariable #funciones-varias-variables #funcion-escalar #funcion-vectorial #campos-vectoriales #parametrizacion #dominio #clasificacion
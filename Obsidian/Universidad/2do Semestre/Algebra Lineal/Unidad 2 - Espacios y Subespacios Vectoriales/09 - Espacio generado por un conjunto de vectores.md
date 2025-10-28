# 📘 Espacio Generado por un Conjunto de Vectores

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante el Espacio Generado?
> 
> Cuando tenemos un conjunto de vectores, surge una pregunta natural: **¿qué tan "grande" es el espacio que estos vectores pueden crear mediante combinaciones lineales?**
> 
> **Motivación:**
> 
> - Los vectores individuales son como "bloques de construcción"
> - Las combinaciones lineales son las "construcciones" que podemos hacer
> - El espacio generado es el **conjunto de todas las construcciones posibles**
> - Es uno de los conceptos más fundamentales del álgebra lineal
> 
> **Analogía:**
> 
> - **Vectores base:** Como los colores primarios (rojo, azul, amarillo)
> - **Combinaciones lineales:** Mezclar colores en diferentes proporciones
> - **Espacio generado:** Todos los colores que puedes crear con esas mezclas
> 
> **Preguntas fundamentales:**
> 
> - ¿Qué vectores puedo "alcanzar" con un conjunto dado?
> - ¿Cuántos vectores necesito para generar todo un espacio?
> - ¿Hay vectores "redundantes" en mi conjunto?
> 
> **Aplicaciones prácticas:**
> 
> - **Computación gráfica:** Representar cualquier imagen como combinación de imágenes base
> - **Procesamiento de señales:** Descomponer señales en componentes básicas
> - **Machine Learning:** Espacios de características
> - **Física:** Describir estados cuánticos
> - **Economía:** Modelos de equilibrio general

---

## 📝 Definición de Espacio Generado

### 🔑 Definición Formal

> [!example]- 🟢 Definición: Espacio Generado (Span)
> 
> **Definición:** Sea $V$ un espacio vectorial y sea $S = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ un conjunto de vectores en $V$. El **espacio generado** por $S$, denotado $\text{span}(S)$ o $\langle S \rangle$, es el conjunto de todas las **combinaciones lineales** de los vectores en $S$:
> 
> $$\text{span}(S) = \text{span}(\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n) = \left{ c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n : c_i \in \mathbb{R} \right}$$
> 
> En otras palabras:
> 
> $$\text{span}(S) = \left{ \sum_{i=1}^n c_i\vec{v}_i : c_i \in \mathbb{R} \right}$$
> 
> ---
> 
> **Notaciones alternativas:**
> 
> - $\text{span}(S)$
> - $\text{span}{\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$
> - $\langle \vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n \rangle$
> - $\text{Lin}(S)$ (en algunos textos)
> - $[S]$ (menos común)
> 
> ---
> 
> **Interpretación:**
> 
> - $\text{span}(S)$ es el "espacio más pequeño" que contiene todos los vectores de $S$
> - Es el conjunto de todos los vectores que puedes "alcanzar" usando $S$
> - Incluye **todas las combinaciones lineales posibles**
> 
> ---
> 
> **Observaciones importantes:**
> 
> 1. Los coeficientes $c_i$ pueden ser cualquier número real
> 2. Se permiten coeficientes cero (lo que "apaga" ese vector)
> 3. Se permiten coeficientes negativos (lo que "invierte" ese vector)
> 4. El conjunto $S$ mismo está contenido en $\text{span}(S)$ (tomando $c_i = 1$ y los demás cero)

### 🎯 Casos Especiales

> [!note]- 📋 Casos Importantes
> 
> ### 1. Conjunto Vacío
> 
> $$\text{span}(\emptyset) = {\vec{0}}$$
> 
> El espacio generado por el conjunto vacío es solo el vector cero.
> 
> ---
> 
> ### 2. Un Solo Vector
> 
> $$\text{span}(\vec{v}) = {c\vec{v} : c \in \mathbb{R}}$$
> 
> **Interpretación geométrica:**
> 
> - Si $\vec{v} \neq \vec{0}$: Es la **recta** que pasa por el origen en la dirección de $\vec{v}$
> - Si $\vec{v} = \vec{0}$: Es solo ${\vec{0}}$
> 
> **Ejemplo en $\mathbb{R}^3$:**
> 
> $$\text{span}\left(\begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}\right) = \left{ \begin{bmatrix} c \ 2c \ 3c \end{bmatrix} : c \in \mathbb{R} \right}$$
> 
> Es la recta que pasa por el origen con dirección $(1, 2, 3)$.
> 
> ---
> 
> ### 3. Dos Vectores
> 
> $$\text{span}(\vec{v}_1, \vec{v}_2) = {c_1\vec{v}_1 + c_2\vec{v}_2 : c_1, c_2 \in \mathbb{R}}$$
> 
> **Casos geométricos en $\mathbb{R}^3$:**
> 
> - Si $\vec{v}_2 = k\vec{v}_1$ (paralelos): Es una **recta**
> - Si $\vec{v}_1$ y $\vec{v}_2$ no son paralelos: Es el **plano** que contiene a ambos vectores y pasa por el origen
> 
> ---
> 
> ### 4. Vector Cero Incluido
> 
> $$\text{span}(\vec{v}_1, \vec{v}_2, \vec{0}) = \text{span}(\vec{v}_1, \vec{v}_2)$$
> 
> El vector cero **no agrega nada** al espacio generado (es redundante).

---

## 🎨 Interpretación Geométrica

### Visualización en $\mathbb{R}^2$

> [!note]- 📊 En el Plano
> 
> ### Un Vector en $\mathbb{R}^2$
> 
> $$\vec{v} = \begin{bmatrix} 2 \ 1 \end{bmatrix}$$
> 
> ```
>       y
>       |
>     3 |
>       |      • (4,2) = 2v
>     2 |    •
>       |  • (2,1) = v
>     1 | •
>       |• (0,0)
>     0 +-------------- x
>       0   2   4
>       |•
>    -1 | • (-2,-1) = -v
> 
>     span(v) = recta a través del origen
> ```
> 
> **Descripción:**
> 
> - Todos los múltiplos escalares de $\vec{v}$
> - Forma una **recta** que pasa por el origen
> - Ecuación: $y = \frac{1}{2}x$
> 
> ---
> 
> ### Dos Vectores No Paralelos en $\mathbb{R}^2$
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \end{bmatrix}$$
> 
> ```
>       y
>       |
>     3 | •   •   •   •
>       |
>     2 | •   •   •   •
>       |     v₂ = (0,1)
>     1 | •   •   •   •
>       |
>     0 +-------------- x
>       0   1   2   3
>           v₁ = (1,0)
> 
>     span(v₁, v₂) = todo R²
> ```
> 
> **Descripción:**
> 
> - Cualquier vector $(x, y)$ puede escribirse como $x\vec{v}_1 + y\vec{v}_2$
> - $\text{span}(\vec{v}_1, \vec{v}_2) = \mathbb{R}^2$ (todo el plano)
> 
> ---
> 
> ### Dos Vectores Paralelos en $\mathbb{R}^2$
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 2 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 2 \ 4 \end{bmatrix}$$
> 
> ```
>       y
>       |
>     4 |    • (2,4) = v₂
>       |  •
>     2 | • (1,2) = v₁
>       |•
>     0 +-------------- x
>       0   1   2
> 
>     span(v₁, v₂) = recta (misma que span(v₁))
> ```
> 
> **Descripción:**
> 
> - $\vec{v}_2 = 2\vec{v}_1$ (son paralelos)
> - $\text{span}(\vec{v}_1, \vec{v}_2) = \text{span}(\vec{v}_1)$ (solo una recta)
> - $\vec{v}_2$ es **redundante**

### Visualización en $\mathbb{R}^3$

> [!note]- 📊 En el Espacio
> 
> ### Un Vector en $\mathbb{R}^3$
> 
> $$\vec{v} = \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}$$
> 
> ```
>         z
>         |
>         |  • (1,1,1)
>         | /
>         |/_____ y
>        /|
>       / |
>      /  
>     x
> 
>     span(v) = recta diagonal
> ```
> 
> **Descripción:**
> 
> - Recta que pasa por el origen con dirección $(1, 1, 1)$
> - Todos los puntos de la forma $(t, t, t)$ donde $t \in \mathbb{R}$
> 
> ---
> 
> ### Dos Vectores No Paralelos en $\mathbb{R}^3$
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}$$
> 
> ```
>         z
>         |
>         |
>         |
>         +----------- y
>        /|  ← Plano xy
>       / |
>      /  |
>     x
> 
>     span(v₁, v₂) = plano xy
> ```
> 
> **Descripción:**
> 
> - Plano que contiene ambos vectores y pasa por el origen
> - Ecuación del plano: $z = 0$ (el plano $xy$)
> - Todos los puntos de la forma $(s, t, 0)$ donde $s, t \in \mathbb{R}$
> 
> ---
> 
> ### Tres Vectores No Coplanares en $\mathbb{R}^3$
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \quad \vec{v}_3 = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> ```
>         z
>         | v₃
>         |
>         |
>         +----------- y
>        /|      v₂
>       / |
>      /  |
>     x   
>     v₁
> 
>     span(v₁, v₂, v₃) = todo R³
> ```
> 
> **Descripción:**
> 
> - Generan todo $\mathbb{R}^3$
> - Cualquier vector $(x, y, z)$ puede escribirse como $x\vec{v}_1 + y\vec{v}_2 + z\vec{v}_3$

---

## 🧮 Propiedades del Espacio Generado

> [!note]- ⭐ Propiedades Fundamentales
> 
> ### Propiedad 1: Es un Subespacio
> 
> **Teorema:** Para cualquier conjunto $S$ de vectores, $\text{span}(S)$ es un **subespacio vectorial**.
> 
> **Demostración:**
> 
> Debemos verificar las tres propiedades de subespacio:
> 
> 1. **Vector cero:** $\vec{0} \in \text{span}(S)$
>     - Tomando todos los coeficientes $c_i = 0$: $\vec{0} = 0\vec{v}_1 + 0\vec{v}_2 + \cdots + 0\vec{v}_n$ ✓
> 2. **Cerrado bajo suma:** Si $\vec{u}, \vec{w} \in \text{span}(S)$, entonces $\vec{u} + \vec{w} \in \text{span}(S)$
>     - $\vec{u} = \sum a_i\vec{v}_i$ y $\vec{w} = \sum b_i\vec{v}_i$
>     - $\vec{u} + \vec{w} = \sum (a_i + b_i)\vec{v}_i \in \text{span}(S)$ ✓
> 3. **Cerrado bajo multiplicación escalar:** Si $\vec{u} \in \text{span}(S)$ y $c \in \mathbb{R}$, entonces $c\vec{u} \in \text{span}(S)$
>     - $\vec{u} = \sum a_i\vec{v}_i$
>     - $c\vec{u} = \sum (ca_i)\vec{v}_i \in \text{span}(S)$ ✓
> 
> ---
> 
> ### Propiedad 2: Subespacio Más Pequeño
> 
> **Teorema:** $\text{span}(S)$ es el **subespacio más pequeño** que contiene a $S$.
> 
> Es decir, si $W$ es un subespacio que contiene a todos los vectores de $S$, entonces:
> 
> $$\text{span}(S) \subseteq W$$
> 
> **Intuición:** No puedes hacer un espacio más pequeño que contenga a $S$ y sea cerrado bajo combinaciones lineales.
> 
> ---
> 
> ### Propiedad 3: Contiene al Conjunto Original
> 
> $$S \subseteq \text{span}(S)$$
> 
> **Razón:** Cada $\vec{v}_i \in S$ está en $\text{span}(S)$ tomando $c_i = 1$ y $c_j = 0$ para $j \neq i$.
> 
> ---
> 
> ### Propiedad 4: Monotonía
> 
> Si $S_1 \subseteq S_2$, entonces:
> 
> $$\text{span}(S_1) \subseteq \text{span}(S_2)$$
> 
> **Interpretación:** Más vectores generadores → espacio más grande (o igual).
> 
> ---
> 
> ### Propiedad 5: Idempotencia
> 
> $$\text{span}(\text{span}(S)) = \text{span}(S)$$
> 
> **Interpretación:** Generar combinaciones de combinaciones no crea nada nuevo.
> 
> ---
> 
> ### Propiedad 6: Vectores Redundantes
> 
> Si $\vec{v} \in \text{span}(S)$, entonces:
> 
> $$\text{span}(S \cup {\vec{v}}) = \text{span}(S)$$
> 
> **Interpretación:** Agregar un vector que ya está en el span no cambia el espacio generado.

---

## 📚 Ejemplos Básicos

### Ejemplo 1: Un Vector en $\mathbb{R}^2$

> [!example]- 📝 Ejemplo 1: Span de Un Vector
> 
> **Conjunto:** $$S = \left{ \begin{bmatrix} 2 \ 3 \end{bmatrix} \right}$$
> 
> **Calcular:** $\text{span}(S)$
> 
> ---
> 
> **Solución:**
> 
> $$\text{span}(S) = \left{ c \begin{bmatrix} 2 \ 3 \end{bmatrix} : c \in \mathbb{R} \right} = \left{ \begin{bmatrix} 2c \ 3c \end{bmatrix} : c \in \mathbb{R} \right}$$
> 
> **Forma paramétrica:**
> 
> $$\begin{cases} x = 2c \ y = 3c \end{cases}$$
> 
> Eliminando el parámetro: $\frac{x}{2} = \frac{y}{3}$, es decir:
> 
> $$y = \frac{3}{2}x$$
> 
> **Interpretación geométrica:**
> 
> - Es la **recta** que pasa por el origen con pendiente $\frac{3}{2}$
> - Dirección: $(2, 3)$
> 
> $$\boxed{\text{span}(S) = \left{ (x, y) : y = \frac{3}{2}x \right}}$$

### Ejemplo 2: Dos Vectores en $\mathbb{R}^3$

> [!example]- 📝 Ejemplo 2: Span de Dos Vectores
> 
> **Conjunto:** $$S = \left{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} \right}$$
> 
> **Calcular:** $\text{span}(S)$ y su interpretación geométrica
> 
> ---
> 
> **Solución:**
> 
> $$\text{span}(S) = \left{ c_1 \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + c_2 \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} : c_1, c_2 \in \mathbb{R} \right}$$
> 
> $$= \left{ \begin{bmatrix} c_1 \ c_2 \ c_1 + c_2 \end{bmatrix} : c_1, c_2 \in \mathbb{R} \right}$$
> 
> **Forma paramétrica:**
> 
> $$\begin{cases} x = c_1 \ y = c_2 \ z = c_1 + c_2 \end{cases}$$
> 
> De las dos primeras: $c_1 = x$, $c_2 = y$
> 
> Sustituyendo en la tercera: $z = x + y$
> 
> **Ecuación del plano:**
> 
> $$x + y - z = 0$$
> 
> o equivalentemente:
> 
> $$z = x + y$$
> 
> **Interpretación geométrica:**
> 
> - Es un **plano** que pasa por el origen
> - Normal al plano: $\vec{n} = (1, 1, -1)$ (coeficientes de la ecuación)
> - Contiene a los vectores $(1, 0, 1)$ y $(0, 1, 1)$
> 
> $$\boxed{\text{span}(S) = {(x, y, z) : z = x + y}}$$

### Ejemplo 3: Vectores Paralelos

> [!example]- 📝 Ejemplo 3: Vectores Linealmente Dependientes
> 
> **Conjunto:** $$S = \left{ \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 4 \ 6 \end{bmatrix}, \begin{bmatrix} -1 \ -2 \ -3 \end{bmatrix} \right}$$
> 
> **Calcular:** $\text{span}(S)$
> 
> ---
> 
> **Observación:**
> 
> $$\vec{v}_2 = 2\vec{v}_1, \quad \vec{v}_3 = -\vec{v}_1$$
> 
> Todos los vectores son **múltiplos escalares** de $\vec{v}_1$.
> 
> ---
> 
> **Solución:**
> 
> Como $\vec{v}_2$ y $\vec{v}_3$ están en $\text{span}(\vec{v}_1)$:
> 
> $$\text{span}(S) = \text{span}(\vec{v}_1) = \left{ c \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix} : c \in \mathbb{R} \right}$$
> 
> **Interpretación:**
> 
> - A pesar de tener 3 vectores, solo generan una **recta**
> - Los vectores $\vec{v}_2$ y $\vec{v}_3$ son **redundantes**
> - Todos apuntan en la misma dirección (o la opuesta)
> 
> $$\boxed{\text{span}(S) = \left{ \begin{bmatrix} c \ 2c \ 3c \end{bmatrix} : c \in \mathbb{R} \right}}$$

### Ejemplo 4: Vectores Canónicos

> [!example]- 📝 Ejemplo 4: Base Canónica de $\mathbb{R}^3$
> 
> **Conjunto:** $$S = \left{ \vec{e}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \vec{e}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \vec{e}_3 = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} \right}$$
> 
> **Calcular:** $\text{span}(S)$
> 
> ---
> 
> **Solución:**
> 
> $$\text{span}(S) = \left{ c_1 \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + c_2 \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} + c_3 \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} : c_1, c_2, c_3 \in \mathbb{R} \right}$$
> 
> $$= \left{ \begin{bmatrix} c_1 \ c_2 \ c_3 \end{bmatrix} : c_1, c_2, c_3 \in \mathbb{R} \right}$$
> 
> **Conclusión:**
> 
> Cualquier vector $(x, y, z)$ puede escribirse como:
> 
> $$\begin{bmatrix} x \ y \ z \end{bmatrix} = x\vec{e}_1 + y\vec{e}_2 + z\vec{e}_3$$
> 
> Por tanto:
> 
> $$\boxed{\text{span}(S) = \mathbb{R}^3}$$
> 
> Los vectores canónicos **generan todo** $\mathbb{R}^3$.

---

## 🔍 Verificar si un Vector está en el Span

> [!note]- 🎯 Método: Resolver Sistema de Ecuaciones
> 
> **Pregunta:** ¿Está $\vec{w}$ en $\text{span}(\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n)$?
> 
> **Método:** Intentar expresar $\vec{w}$ como combinación lineal:
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n$$
> 
> Esto es un **sistema de ecuaciones lineales** en las incógnitas $c_1, c_2, \ldots, c_n$.
> 
> **Resultado:**
> 
> - ✅ Si el sistema tiene solución: $\vec{w} \in \text{span}(S)$
> - ❌ Si el sistema es inconsistente: $\vec{w} \notin \text{span}(S)$
> 
> ---
> 
> **Procedimiento:**
> 
> 1. Plantear la ecuación matricial: $[\ \vec{v}_1 \ | \ \vec{v}_2 \ | \ \cdots \ | \ \vec{v}_n \ ] \begin{bmatrix} c_1 \ c_2 \ \vdots \ c_n \end{bmatrix} = \vec{w}$
>     
> 2. Formar la matriz aumentada: $[\ \vec{v}_1 \ | \ \vec{v}_2 \ | \ \cdots \ | \ \vec{v}_n \ | \ \vec{w} \ ]$
>     
> 3. Reducir a forma escalonada
>     
> 4. Analizar consistencia
>     

### Ejemplo 5: Verificar Pertenencia

> [!example]- 📝 Ejemplo 5: ¿Está el vector en el span?
> 
> **Dado:** $$S = \left\{ 
\begin{bmatrix} 1 & 2 & 1 \end{bmatrix}, 
\begin{bmatrix} 2 & 1 & 3 \end{bmatrix} 
\right\}, \quad 
\vec{w} = \begin{bmatrix} 3 & 4 & 5 \end{bmatrix}$$
> 
> **Pregunta:** ¿Está $\vec{w} \in \text{span}(S)$?
> 
> ---
> 
> **Solución:**
> 
> Queremos saber si existen $c_1, c_2$ tales que:
> 
> $$c_1 \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix} + c_2 \begin{bmatrix} 2 \ 1 \ 3 \end{bmatrix} = \begin{bmatrix} 3 \ 4 \ 5 \end{bmatrix}$$
> 
> **Sistema de ecuaciones:**
> 
> $$\begin{cases} c_1 + 2c_2 = 3 \ 2c_1 + c_2 = 4 \ c_1 + 3c_2 = 5 \end{cases}$$
> 
> **Matriz aumentada:**
> 
> $$\left[\begin{array}{cc|c} 1 & 2 & 3 \ 2 & 1 & 4 \ 1 & 3 & 5 \end{array}\right]$$
> 
> **Reducción por filas:**
> 
> $R_2 - 2R_1$:
> 
> $$\left[\begin{array}{cc|c} 1 & 2 & 3 \ 0 & -3 & -2 \ 1 & 3 & 5 \end{array}\right]$$
> 
> $R_3 - R_1$:
> 
> $$\left[\begin{array}{cc|c} 1 & 2 & 3 \ 0 & -3 & -2 \ 0 & 1 & 2 \end{array}\right]$$
> 
> $R_2 + 3R_3$:
> 
> $$\left[\begin{array}{cc|c} 1 & 2 & 3 \ 0 & 0 & 4 \ 0 & 1 & 2 \end{array}\right]$$
> 
> **Análisis:**
> 
> La segunda fila dice: $0 = 4$, lo cual es una **contradicción**.
> 
> El sistema es **inconsistente**.
> 
> $$\boxed{\vec{w} \notin \text{span}(S)}$$
> 
> **Interpretación geométrica:**
> 
> - $\text{span}(S)$ es un plano en $\mathbb{R}^3$
> - $\vec{w}$ no está en ese plano
> - Los dos vectores de $S$ no son suficientes para "alcanzar" a $\vec{w}$

### Ejemplo 6: Vector que SÍ está en el Span

> [!example]- 📝 Ejemplo 6: Pertenencia Exitosa
> 
> **Dado:** $$S = \left{ \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} \right}, \quad \vec{w} = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix}$$
> 
> **Pregunta:** ¿Está $\vec{w} \in \text{span}(S)$?
> 
> ---
> 
> **Plantear:**
> 
> $$c_1 \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} + c_2 \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + c_3 \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix}$$
> 
> **Sistema:**
> 
> $$\begin{cases} c_1 + c_2 = 2 \ c_1 + c_3 = 3 \ c_2 + c_3 = 4 \end{cases}$$
> 
> **Matriz aumentada:**
> 
> $$\left[\begin{array}{ccc|c} 1 & 1 & 0 & 2 \ 1 & 0 & 1 & 3 \ 0 & 1 & 1 & 4 \end{array}\right]$$
> 
> **Reducción:**
> 
> $R_2 - R_1$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 1 & 0 & 2 \ 0 & -1 & 1 & 1 \ 0 & 1 & 1 & 4 \end{array}\right]$$
> 
> $R_3 + R_2$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 1 & 0 & 2 \ 0 & -1 & 1 & 1 \ 0 & 0 & 2 & 5 \end{array}\right]$$
> 
> **Resolver hacia atrás:**
> 
> De $R_3$: $2c_3 = 5$ → $c_3 = \frac{5}{2}$
> 
> De $R_2$: $-c_2 + c_3 = 1$ → $c_2 = \frac{5}{2} - 1 = \frac{3}{2}$
> 
> De $R_1$: $c_1 + c_2 = 2$ → $c_1 = 2 - \frac{3}{2} = \frac{1}{2}$
> 
> **Verificación:**
> 
> $$\frac{1}{2}\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} + \frac{3}{2}\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + \frac{5}{2}\begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} = \begin{bmatrix} \frac{1}{2} + \frac{3}{2} \ \frac{1}{2} + \frac{5}{2} \ \frac{3}{2} + \frac{5}{2} \end{bmatrix} = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix}$$ ✓
> 
> $$\boxed{\vec{w} \in \text{span}(S)}$$
> 
> La combinación lineal es:
> 
> $$\vec{w} = \frac{1}{2}\vec{v}_1 + \frac{3}{2}\vec{v}_2 + \frac{5}{2}\vec{v}_3$$

---

## 🎓 Relación con Independencia Lineal

> [!note]- 🔗 Conexión Importante
> 
> ### Vectores Redundantes
> 
> Un vector $\vec{v}_k$ en $S = {\vec{v}_1, \ldots, \vec{v}_n}$ es **redundante** si:
> 
> $$\vec{v}_k \in \text{span}(\vec{v}_1, \ldots, \vec{v}_{k-1}, \vec{v}_{k+1}, \ldots, \vec{v}_n)$$
> 
> Es decir, puede escribirse como combinación de los otros.
> 
> En este caso:
> 
> $$\text{span}(S) = \text{span}(S \setminus {\vec{v}_k})$$
> 
> ---
> 
> ### Independencia Lineal (Adelanto)
> 
> Un conjunto $S$ es **linealmente independiente** si ningún vector es redundante.
> 
> Equivalentemente: La única forma de obtener $\vec{0}$ como combinación lineal es con todos los coeficientes cero.
> 
> **Relación con span:**
> 
> - Si $S$ es **linealmente dependiente**: Tiene vectores redundantes, se puede reducir sin cambiar el span
> - Si $S$ es **linealmente independiente**: No tiene vectores redundantes, todos son necesarios
> 
> ---
> 
> ### Base (Adelanto)
> 
> Un conjunto $B$ es una **base** de un espacio $V$ si:
> 
> 1. $\text{span}(B) = V$ (genera todo el espacio)
> 2. $B$ es linealmente independiente (sin redundancia)
> 
> **Ejemplo:** Los vectores canónicos ${\vec{e}_1, \vec{e}_2, \vec{e}_3}$ forman una base de $\mathbb{R}^3$.

---

## 📐 Espacio Generado y Subespacios

> [!note]- 🎯 Teorema Fundamental
> 
> **Teorema:** Todo subespacio $W$ de un espacio vectorial $V$ puede expresarse como el span de algún conjunto de vectores.
> 
> Es decir, para todo subespacio $W$, existe un conjunto $S$ tal que:
> 
> $$W = \text{span}(S)$$
> 
> ---
> 
> **Consecuencia:** Estudiar subespacios es equivalente a estudiar conjuntos generadores.
> 
> ---
> 
> ### Caracterización de Subespacios en $\mathbb{R}^n$
> 
> En $\mathbb{R}^n$, los subespacios son exactamente los espacios generados:
> 
> |Dimensión|Forma Geométrica|Ejemplo en $\mathbb{R}^3$|
> |---|---|---|
> |0|Solo ${\vec{0}}$|El origen|
> |1|Recta por el origen|$\text{span}(\vec{v})$|
> |2|Plano por el origen|$\text{span}(\vec{v}_1, \vec{v}_2)$|
> |3|Todo el espacio|$\text{span}(\vec{e}_1, \vec{e}_2, \vec{e}_3)$|

---

## 🔢 Ejemplos con Espacios de Matrices y Polinomios

### Ejemplo 7: Espacio de Matrices

> [!example]- 📝 Ejemplo 7: Matrices 2×2
> 
> **Conjunto de matrices:**
> 
> $$S = \left{ \begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix} \right}$$
> 
> **Calcular:** $\text{span}(S)$
> 
> ---
> 
> **Solución:**
> 
> Una combinación lineal general es:
> 
> $$c_1 \begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix} + c_2 \begin{bmatrix} 0 & 1 \ 0 & 0 \end{bmatrix} + c_3 \begin{bmatrix} 0 & 0 \ 1 & 0 \end{bmatrix} + c_4 \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}$$
> 
> $$= \begin{bmatrix} c_1 & c_2 \ c_3 & c_4 \end{bmatrix}$$
> 
> **Conclusión:**
> 
> Cualquier matriz $2 \times 2$ puede escribirse como combinación lineal de las matrices en $S$.
> 
> $$\boxed{\text{span}(S) = M_{2 \times 2}(\mathbb{R})}$$
> 
> (el espacio de todas las matrices $2 \times 2$)
> 
> ---
> 
> **Interpretación:** Las matrices en $S$ son las "matrices canónicas" que forman una base del espacio de matrices $2 \times 2$.

### Ejemplo 8: Polinomios

> [!example]- 📝 Ejemplo 8: Espacio de Polinomios
> 
> **Conjunto:** $$S = {1, x, x^2}$$ en el espacio $P_2$ (polinomios de grado ≤ 2)
> 
> **Calcular:** $\text{span}(S)$
> 
> ---
> 
> **Solución:**
> 
> Una combinación lineal general es:
> 
> $$c_1 \cdot 1 + c_2 \cdot x + c_3 \cdot x^2 = c_1 + c_2x + c_3x^2$$
> 
> Esto representa **cualquier** polinomio de grado ≤ 2.
> 
> $$\boxed{\text{span}(S) = P_2}$$
> 
> ---
> 
> **Ejemplo específico:**
> 
> El polinomio $p(x) = 3 - 2x + 5x^2$ está en $\text{span}(S)$:
> 
> $$p(x) = 3 \cdot 1 + (-2) \cdot x + 5 \cdot x^2$$
> 
> ---
> 
> **Subespacio más pequeño:**
> 
> Si solo usamos $S' = {1, x}$:
> 
> $$\text{span}(S') = P_1$$
> 
> (solo polinomios lineales: $a + bx$)

### Ejemplo 9: Matrices Simétricas

> [!example]- 📝 Ejemplo 9: Subespacios Especiales
> 
> **Pregunta:** ¿Cuál es un conjunto generador para el espacio de matrices simétricas $2 \times 2$?
> 
> Una matriz simétrica tiene la forma:
> 
> $$\begin{bmatrix} a & b \ b & c \end{bmatrix}$$
> 
> ---
> 
> **Solución:**
> 
> Podemos escribir cualquier matriz simétrica como:
> 
> $$\begin{bmatrix} a & b \ b & c \end{bmatrix} = a \begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix} + b \begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix} + c \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}$$
> 
> **Conjunto generador:**
> 
> $$S = \left{ \begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix} \right}$$
> 
> $$\boxed{\text{span}(S) = \text{Sim}_{2 \times 2}}$$
> 
> (el espacio de matrices simétricas $2 \times 2$)
> 
> ---
> 
> **Observación:** Este espacio tiene 3 "dimensiones" (necesitamos 3 matrices para generarlo), mientras que el espacio completo $M_{2 \times 2}$ tiene 4 dimensiones.

---

## 🧮 Algoritmo: Encontrar Conjunto Generador Minimal

> [!note]- 🔧 Procedimiento para Reducir Redundancia
> 
> **Objetivo:** Dado un conjunto $S$ de vectores, encontrar un subconjunto $S' \subseteq S$ tal que:
> 
> 1. $\text{span}(S') = \text{span}(S)$
> 2. $S'$ no tiene vectores redundantes (es linealmente independiente)
> 
> ---
> 
> ### Método de Eliminación
> 
> **Algoritmo:**
> 
> 1. **Formar matriz:** Colocar los vectores como columnas en una matriz $A$
>     
> 2. **Reducir a forma escalonada:** Usar eliminación gaussiana para obtener la forma escalonada reducida
>     
> 3. **Identificar columnas pivote:** Las columnas con pivotes corresponden a vectores linealmente independientes
>     
> 4. **Seleccionar vectores:** El conjunto generador minimal es el conjunto de vectores originales correspondientes a las columnas pivote
>     
> 
> ---
> 
> ### Ejemplo del Algoritmo
> 
> **Dado:**
> 
> $$S = \left{ \vec{v}_1 = \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 2 \ 4 \ 2 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}, \vec{v}_4 = \begin{bmatrix} 3 \ 5 \ 4 \end{bmatrix} \right}$$
> 
> **Paso 1:** Formar matriz
> 
> $$A = \begin{bmatrix} 1 & 2 & 1 & 3 \ 2 & 4 & 1 & 5 \ 1 & 2 & 2 & 4 \end{bmatrix}$$
> 
> **Paso 2:** Reducir
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 2 & 0 & 2 \ 0 & 0 & 1 & 1 \ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Paso 3:** Columnas pivote: 1 y 3
> 
> **Paso 4:** Conjunto generador minimal:
> 
> $$S' = {\vec{v}_1, \vec{v}_3}$$
> 
> **Verificación:**
> 
> - $\vec{v}_2 = 2\vec{v}_1$ (redundante)
> - $\vec{v}_4 = 2\vec{v}_1 + \vec{v}_3$ (combinación de los otros)
> 
> $$\boxed{\text{span}(S) = \text{span}(S') = \text{span}(\vec{v}_1, \vec{v}_3)}$$

---

## 🎯 Aplicaciones Prácticas

### Aplicación 1: Sistemas de Ecuaciones Lineales

> [!example]- 🔧 Espacio de Soluciones
> 
> **Sistema homogéneo:** $A\vec{x} = \vec{0}$
> 
> El conjunto de todas las soluciones es un subespacio llamado **núcleo** o **espacio nulo** de $A$:
> 
> $$\text{Nul}(A) = {\vec{x} : A\vec{x} = \vec{0}}$$
> 
> ---
> 
> **Ejemplo:**
> 
> Sistema: $$\begin{cases} x + 2y - z = 0 \ 2x + 4y - 2z = 0 \end{cases}$$
> 
> **Resolver:**
> 
> Matriz aumentada:
> 
> $$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \ 2 & 4 & -2 & 0 \end{array}\right] \sim \left[\begin{array}{ccc|c} 1 & 2 & -1 & 0 \ 0 & 0 & 0 & 0 \end{array}\right]$$
> 
> **Solución general:**
> 
> $$x + 2y - z = 0 \implies x = -2y + z$$
> 
> Variables libres: $y, z$
> 
> $$\vec{x} = \begin{bmatrix} -2y + z \ y \ z \end{bmatrix} = y\begin{bmatrix} -2 \ 1 \ 0 \end{bmatrix} + z\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$$
> 
> **Espacio de soluciones:**
> 
> $$\text{Nul}(A) = \text{span}\left{ \begin{bmatrix} -2 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} \right}$$
> 
> Es un **plano** que pasa por el origen en $\mathbb{R}^3$.

### Aplicación 2: Espacio Columna de una Matriz

> [!example]- 📊 Column Space
> 
> **Definición:** El **espacio columna** de una matriz $A$ es el span de sus columnas:
> 
> $$\text{Col}(A) = \text{span}{\vec{a}_1, \vec{a}_2, \ldots, \vec{a}_n}$$
> 
> donde $\vec{a}_i$ son las columnas de $A$.
> 
> ---
> 
> **Interpretación:** $\text{Col}(A)$ es el conjunto de todos los vectores $\vec{b}$ tales que el sistema $A\vec{x} = \vec{b}$ tiene solución.
> 
> ---
> 
> **Ejemplo:**
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 \ 2 & 4 & 6 \ 1 & 1 & 2 \end{bmatrix}$$
> 
> Las columnas son:
> 
> $$\vec{a}_1 = \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \quad \vec{a}_2 = \begin{bmatrix} 2 \ 4 \ 2 \end{bmatrix}, \quad \vec{a}_3 = \begin{bmatrix} 3 \ 6 \ 3 \end{bmatrix}$$
> 
> **Observación:** $\vec{a}_2 = 2\vec{a}_1$ y $\vec{a}_3 = 3\vec{a}_1$
> 
> Por tanto:
> 
> $$\text{Col}(A) = \text{span}(\vec{a}_1) = \text{span}\left{ \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix} \right}$$
> 
> Es una **recta** en $\mathbb{R}^3$.

### Aplicación 3: Procesamiento de Señales

> [!example]- 🎵 Descomposición de Señales
> 
> **Problema:** Representar una señal compleja como combinación de señales básicas.
> 
> **Conjunto de señales base:**
> 
> $$S = {\sin(t), \sin(2t), \sin(3t), \ldots}$$
> 
> **Señal general:**
> 
> Cualquier señal periódica puede aproximarse como:
> 
> $$f(t) = c_1\sin(t) + c_2\sin(2t) + c_3\sin(3t) + \cdots$$
> 
> Esto es la **Serie de Fourier** (en su forma simplificada).
> 
> ---
> 
> **Interpretación:**
> 
> - Las funciones $\sin(nt)$ son como "vectores base"
> - Los coeficientes $c_i$ determinan cuánto de cada frecuencia hay
> - El espacio generado contiene todas las señales que podemos representar

### Aplicación 4: Computer Graphics

> [!example]- 🎮 Transformaciones Lineales
> 
> **Problema:** Representar imágenes como combinaciones de imágenes base.
> 
> **Ejemplo simplificado:**
> 
> Una imagen en escala de grises $8 \times 8$ píxeles puede verse como un vector en $\mathbb{R}^{64}$.
> 
> **Conjunto de imágenes base:**
> 
> $$S = {\text{Imagen}_1, \text{Imagen}_2, \ldots, \text{Imagen}_{64}}$$
> 
> Podemos elegir bases especiales (como **DCT - Discrete Cosine Transform**) que son eficientes para compresión.
> 
> **Cualquier imagen:**
> 
> $$\text{Imagen} = c_1 \cdot \text{Base}_1 + c_2 \cdot \text{Base}_2 + \cdots + c_{64} \cdot \text{Base}_{64}$$
> 
> **Aplicación:** Compresión JPEG usa este principio, guardando solo los coeficientes más importantes.

---

## 📊 Tabla Resumen de Propiedades

> [!note]- 📋 Propiedades del Span
> 
> |Propiedad|Enunciado|Intuición|
> |---|---|---|
> |**Subespacio**|$\text{span}(S)$ es un subespacio|Cerrado bajo combinaciones lineales|
> |**Contiene a S**|$S \subseteq \text{span}(S)$|Los generadores están incluidos|
> |**Minimal**|Si $W \supseteq S$ es subespacio, entonces $\text{span}(S) \subseteq W$|Es el subespacio más pequeño que contiene a $S$|
> |**Monotonía**|$S_1 \subseteq S_2 \implies \text{span}(S_1) \subseteq \text{span}(S_2)$|Más vectores → espacio más grande (o igual)|
> |**Idempotencia**|$\text{span}(\text{span}(S)) = \text{span}(S)$|Generar dos veces no cambia nada|
> |**Redundancia**|Si $\vec{v} \in \text{span}(S)$, entonces $\text{span}(S \cup {\vec{v}}) = \text{span}(S)$|Vectores en el span son redundantes|
> |**Vector cero**|$\vec{0} \in \text{span}(S)$ siempre|Tomando todos los coeficientes = 0|
> |**Intersección**|$\text{span}(S_1) \cap \text{span}(S_2)$ es un subespacio|Intersección de subespacios es subespacio|

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular el span:**
> 
> a) $\text{span}\left{ \begin{bmatrix} 1 \ 2 \end{bmatrix} \right}$ en $\mathbb{R}^2$
> 
> b) $\text{span}\left{ \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} \right}$ en $\mathbb{R}^3$
> 
> c) $\text{span}{1, x}$ en $P_2$
> 
> d) $\text{span}\left{ \begin{bmatrix} 1 & 0 \ 0 & 1 \end{bmatrix} \right}$ en $M_{2 \times 2}$
> 
> ---
> 
> **2. Verificar pertenencia:**
> 
> ¿Está el vector $\vec{w}$ en $\text{span}(S)$?
> 
> a) $S = \left{ \begin{bmatrix} 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 4 \end{bmatrix} \right}$, $\vec{w} = \begin{bmatrix} 5 \ 8 \end{bmatrix}$
> 
> b) $S = \left{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} \right}$, $\vec{w} = \begin{bmatrix} 2 \ 3 \ 5 \end{bmatrix}$
> 
> c) $S = {1, x, x^2}$ en $P_2$, $p(x) = 2 - 3x + x^2$
> 
> ---
> 
> **3. Interpretación geométrica:**
> 
> Describir geométricamente cada span en $\mathbb{R}^3$:
> 
> a) $\text{span}\left{ \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} \right}$
> 
> b) $\text{span}\left{ \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} \right}$
> 
> c) $\text{span}\left{ \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 4 \ 6 \end{bmatrix} \right}$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Redundancia:**
> 
> Para cada conjunto, identificar vectores redundantes y encontrar un subconjunto minimal que genere el mismo espacio:
> 
> a) $S = \left{ \begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 2 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix} \right}$
> 
> b) $S = \left{ \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix} \right}$
> 
> c) $S = {1, x, 1+x, x^2}$ en $P_2$
> 
> ---
> 
> **5. Ecuaciones de subespacios:**
> 
> Para cada span, encontrar ecuación(es) que describan el subespacio:
> 
> a) $\text{span}\left{ \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix} \right}$ en $\mathbb{R}^3$
> 
> b) $\text{span}\left{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} \right}$ en $\mathbb{R}^3$
> 
> ---
> 
> **6. Operaciones con spans:**
> 
> Sean $S_1 = \left{ \begin{bmatrix} 1 \ 0 \end{bmatrix} \right}$ y $S_2 = \left{ \begin{bmatrix} 0 \ Tienes razón, veo que el formato LaTeX para matrices no se está renderizando correctamente. Déjame continuar con el formato correcto:

---

## 🎓 Ejercicios Propuestos (continuación)

> [!example]- 💪 Práctica Nivel Intermedio (continuación)
> 
> **4. Redundancia:**
> 
> Para cada conjunto, identificar vectores redundantes y encontrar un subconjunto minimal que genere el mismo espacio:
> 
> a) $S = \left{ \begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 2 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix} \right}$
> 
> b) $S = \left{ \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix} \right}$
> 
> c) $S = {1, x, 1+x, x^2}$ en $P_2$
> 
> ---
> 
> **5. Ecuaciones de subespacios:**
> 
> Para cada span, encontrar ecuación(es) que describan el subespacio:
> 
> a) $\text{span}\left{ \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix} \right}$ en $\mathbb{R}^3$
> 
> b) $\text{span}\left{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} \right}$ en $\mathbb{R}^3$
> 
> ---
> 
> **6. Operaciones con spans:**
> 
> Sean $S_1 = \left{ \begin{bmatrix} 1 \ 0 \end{bmatrix} \right}$ y $S_2 = \left{ \begin{bmatrix} 0 \ 1 \end{bmatrix} \right}$
> 
> a) Calcular $\text{span}(S_1) \cap \text{span}(S_2)$
> 
> b) ¿Es $\text{span}(S_1 \cup S_2) = \text{span}(S_1) + \text{span}(S_2)$?
> 
> c) Describir geométricamente $\text{span}(S_1 \cup S_2)$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Espacio columna:**
> 
> Para cada matriz, encontrar un conjunto generador minimal de $\text{Col}(A)$:
> 
> a) $A = \begin{bmatrix} 1 & 2 & 3 \ 2 & 4 & 6 \ 3 & 6 & 9 \end{bmatrix}$
> 
> b) $A = \begin{bmatrix} 1 & 0 & 2 \ 0 & 1 & 3 \ 1 & 1 & 5 \end{bmatrix}$
> 
> c) $A = \begin{bmatrix} 1 & 2 & 1 & 4 \ 2 & 1 & 3 & 5 \ 1 & -1 & 2 & 1 \end{bmatrix}$
> 
> ---
> 
> **8. Demostrar propiedades:**
> 
> a) Demostrar que $\text{span}(\text{span}(S)) = \text{span}(S)$
> 
> b) Demostrar que si $\vec{v} \in \text{span}(S)$, entonces $\text{span}(S \cup {\vec{v}}) = \text{span}(S)$
> 
> c) Demostrar que $\text{span}(S_1 \cup S_2) = \text{span}(S_1) + \text{span}(S_2)$
> 
> ---
> 
> **9. Matrices especiales:**
> 
> a) Encontrar un conjunto generador para el espacio de matrices antisimétricas $2 \times 2$ (donde $A^T = -A$)
> 
> b) Encontrar un conjunto generador para el espacio de matrices diagonales $3 \times 3$
> 
> c) ¿Cuál es $\dim(\text{span}(S))$ para cada caso?
> 
> ---
> 
> **10. Aplicación a sistemas:**
> 
> Para el sistema $A\vec{x} = \vec{0}$ donde:
> 
> $$A = \begin{bmatrix} 1 & 2 & -1 & 3 \ 2 & 4 & 1 & 0 \ 1 & 2 & 4 & -9 \end{bmatrix}$$
> 
> a) Encontrar el espacio nulo $\text{Nul}(A)$ como span de vectores
> 
> b) Verificar que $\text{Nul}(A)$ es un subespacio
> 
> c) ¿Cuántos vectores necesitas para generar $\text{Nul}(A)$?

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $\text{span}\left{ \begin{bmatrix} 1 \ 2 \end{bmatrix} \right}$
> 
> Todos los vectores de la forma $c\begin{bmatrix} 1 \ 2 \end{bmatrix} = \begin{bmatrix} c \ 2c \end{bmatrix}$
> 
> **Geometría:** Recta $y = 2x$
> 
> $$\boxed{\text{span} = {(x,y) : y = 2x}}$$
> 
> ---
> 
> **1b)** $\text{span}\left{ \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} \right}$
> 
> $$c_1\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} = \begin{bmatrix} c_1 \ c_2 \ 0 \end{bmatrix}$$
> 
> **Geometría:** Plano $xy$ (donde $z=0$)
> 
> $$\boxed{\text{span} = {(x,y,z) : z = 0}}$$
> 
> ---
> 
> **2a)** ¿Está $\begin{bmatrix} 5 \ 8 \end{bmatrix}$ en $\text{span}\left{ \begin{bmatrix} 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 4 \end{bmatrix} \right}$?
> 
> Resolver: $c_1\begin{bmatrix} 1 \ 2 \end{bmatrix} + c_2\begin{bmatrix} 3 \ 4 \end{bmatrix} = \begin{bmatrix} 5 \ 8 \end{bmatrix}$
> 
> Sistema: $$\begin{cases} c_1 + 3c_2 = 5 \ 2c_1 + 4c_2 = 8 \end{cases}$$
> 
> De la primera: $c_1 = 5 - 3c_2$
> 
> Sustituyendo: $2(5-3c_2) + 4c_2 = 8$
> 
> $10 - 6c_2 + 4c_2 = 8$
> 
> $-2c_2 = -2 \implies c_2 = 1$
> 
> $c_1 = 5 - 3 = 2$
> 
> **Verificación:** $2\begin{bmatrix} 1 \ 2 \end{bmatrix} + 1\begin{bmatrix} 3 \ 4 \end{bmatrix} = \begin{bmatrix} 5 \ 8 \end{bmatrix}$ ✓
> 
> $$\boxed{\text{Sí, está en el span}}$$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $S = \left{ \begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 2 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix} \right}$
> 
> **Análisis:**
> 
> - $\begin{bmatrix} 2 \ 0 \end{bmatrix} = 2\begin{bmatrix} 1 \ 0 \end{bmatrix}$ (redundante)
> 
> **Conjunto minimal:**
> 
> $$S' = \left{ \begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix} \right}$$
> 
> $$\boxed{\text{span}(S) = \text{span}(S') = \mathbb{R}^2}$$
> 
> ---
> 
> **5b)** Ecuación del plano generado por $\left{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} \right}$
> 
> Un vector general es:
> 
> $$\vec{v} = c_1\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} = \begin{bmatrix} c_1 \ c_2 \ c_1+c_2 \end{bmatrix}$$
> 
> Si $(x,y,z)$ está en el span: $x=c_1$, $y=c_2$, $z=c_1+c_2$
> 
> Eliminando parámetros: $z = x + y$
> 
> **Ecuación del plano:**
> 
> $$\boxed{x + y - z = 0}$$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **7a)** $A = \begin{bmatrix} 1 & 2 & 3 \ 2 & 4 & 6 \ 3 & 6 & 9 \end{bmatrix}$
> 
> **Observación:** Todas las columnas son múltiplos de la primera:
> 
> - Columna 2 = $2 \times$ Columna 1
> - Columna 3 = $3 \times$ Columna 1
> 
> **Conjunto generador minimal:**
> 
> $$\boxed{\text{Col}(A) = \text{span}\left{ \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix} \right}}$$
> 
> Es una recta en $\mathbb{R}^3$.
> 
> ---
> 
> **8a)** Demostrar: $\text{span}(\text{span}(S)) = \text{span}(S)$
> 
> **Demostración:**
> 
> ($\subseteq$) Sea $\vec{w} \in \text{span}(\text{span}(S))$
> 
> Entonces $\vec{w}$ es combinación lineal de vectores en $\text{span}(S)$
> 
> Cada vector en $\text{span}(S)$ es combinación lineal de vectores en $S$
> 
> Por tanto $\vec{w}$ es combinación de combinaciones, que sigue siendo combinación lineal de $S$
> 
> Luego $\vec{w} \in \text{span}(S)$
> 
> ($\supseteq$) Como $\text{span}(S) \subseteq \text{span}(\text{span}(S))$ por definición
> 
> $$\boxed{\text{span}(\text{span}(S)) = \text{span}(S)}$$ ✓
> 
> ---
> 
> **9a)** Matrices antisimétricas $2 \times 2$: $A^T = -A$
> 
> Forma general: $\begin{bmatrix} 0 & a \ -a & 0 \end{bmatrix}$
> 
> Esto es: $a\begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix}$
> 
> **Conjunto generador:**
> 
> $$\boxed{S = \left{ \begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix} \right}}$$
> 
> Dimensión = 1

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Espacio Generado
> 
> ✅ **Definición:**
> 
> - $\text{span}(S)$ = todas las combinaciones lineales de vectores en $S$
> - $\text{span}(\vec{v}_1, \ldots, \vec{v}_n) = {c_1\vec{v}_1 + \cdots + c_n\vec{v}_n : c_i \in \mathbb{R}}$
> 
> ✅ **Es un subespacio:**
> 
> - Contiene $\vec{0}$
> - Cerrado bajo suma y multiplicación escalar
> - Es el subespacio más pequeño que contiene a $S$
> 
> ✅ **Interpretación geométrica:**
> 
> - 1 vector no nulo → recta
> - 2 vectores no paralelos en $\mathbb{R}^3$ → plano
> - 3 vectores no coplanares en $\mathbb{R}^3$ → todo $\mathbb{R}^3$
> 
> ---
> 
> ### Verificación Práctica
> 
> ✅ **Para verificar si $\vec{w} \in \text{span}(S)$:**
> 
> 1. Plantear: $\vec{w} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$
> 2. Obtener sistema de ecuaciones
> 3. Resolver (matriz aumentada)
> 4. Si tiene solución → SÍ está; si no → NO está
> 
> ✅ **Para encontrar conjunto minimal:**
> 
> 1. Formar matriz con vectores como columnas
> 2. Reducir a forma escalonada
> 3. Tomar vectores originales correspondientes a columnas pivote
> 
> ---
> 
> ### Propiedades Importantes
> 
> ✅ **Redundancia:**
> 
> - Vector cero siempre es redundante
> - Si $\vec{v} \in \text{span}(S)$, agregar $\vec{v}$ no cambia el span
> - Vectores paralelos son redundantes entre sí
> 
> ✅ **Operaciones:**
> 
> - $\text{span}(S_1 \cup S_2)$ contiene a ambos spans
> - $\text{span}(S_1) \cap \text{span}(S_2)$ es subespacio
> - $\text{span}(\text{span}(S)) = \text{span}(S)$ (idempotencia)

---

## 🔗 Relaciones Importantes

> [!quote]- 🌐 Conexiones con Otros Temas
> 
> ### Prerequisitos:
> 
> - **[[05 - Subespacios Vectoriales]]** - El span es un subespacio
> - **[[06 - Combinaciones Lineales]]** - Definición fundamental del span
> - **[[07 - Sistemas de Ecuaciones Lineales]]** - Para verificar pertenencia
> - **[[08 - Matrices y Operaciones]]** - Método de reducción por filas
> 
> ### Este tema es prerequisito para:
> 
> - **[[10 - Independencia Lineal]]** - Conjuntos sin redundancia
> - **[[11 - Base y Dimensión]]** - Conjuntos generadores minimales
> - **[[12 - Espacio Columna y Rango]]** - Span de columnas de una matriz
> - **[[13 - Espacio Nulo]]** - Soluciones como span
> - **[[14 - Coordenadas y Cambio de Base]]** - Representación única
> - **[[15 - Transformaciones Lineales]]** - Imagen como span
> 
> ### Conceptos relacionados:
> 
> - **Subespacio** - Todo span es un subespacio
> - **Independencia Lineal** - Ausencia de redundancia en generadores
> - **Base** - Conjunto generador minimal e independiente
> - **Dimensión** - Número mínimo de vectores necesarios
> - **Espacio Columna** - $\text{Col}(A) = \text{span}$ de columnas de $A$
> - **Espacio Nulo** - Soluciones de $A\vec{x} = \vec{0}$ como span
> 
> ### Diagrama de Flujo:
> 
> ```
> Combinaciones Lineales
>          ↓
>    Espacio Generado (span)
>          ↓
>    Es un Subespacio
>          ↓
>    Independencia Lineal
>          ↓
>    Base y Dimensión
> ```
> 
> ### Siguiente tema recomendado:
> 
> **[[10 - Independencia Lineal]]** - Para entender cuándo un conjunto generador no tiene redundancia

---

## 📊 Mapa Conceptual

> [!note]- 🌳 Árbol de Conceptos
> 
> ```
> ESPACIO GENERADO (SPAN)
> │
> ├─ DEFINICIÓN
> │  ├─ Todas las combinaciones lineales
> │  ├─ span(v₁, ..., vₙ) = {c₁v₁ + ... + cₙvₙ}
> │  └─ Notaciones: span(S), ⟨S⟩, Lin(S)
> │
> ├─ PROPIEDADES ALGEBRAICAS
> │  ├─ Es un subespacio
> │  ├─ Contiene a S
> │  ├─ Subespacio más pequeño que contiene a S
> │  ├─ Monotonía: S₁ ⊆ S₂ ⇒ span(S₁) ⊆ span(S₂)
> │  └─ Idempotencia: span(span(S)) = span(S)
> │
> ├─ INTERPRETACIÓN GEOMÉTRICA
> │  ├─ En ℝ²
> │  │  ├─ 1 vector → recta
> │  │  └─ 2 vectores no paralelos → plano completo
> │  └─ En ℝ³
> │     ├─ 1 vector → recta
> │     ├─ 2 vectores no paralelos → plano
> │     └─ 3 vectores no coplanares → todo ℝ³
> │
> ├─ MÉTODOS DE CÁLCULO
> │  ├─ Verificar pertenencia
> │  │  └─ Resolver sistema de ecuaciones
> │  ├─ Encontrar ecuaciones del subespacio
> │  │  └─ Eliminar parámetros
> │  └─ Reducir redundancia
> │     └─ Forma escalonada reducida
> │
> ├─ CASOS ESPECIALES
> │  ├─ span(∅) = {0}
> │  ├─ span({0}) = {0}
> │  ├─ span(vectores paralelos) = span(uno de ellos)
> │  └─ span(base canónica) = ℝⁿ
> │
> └─ APLICACIONES
>    ├─ Espacio columna de matrices
>    ├─ Espacio nulo (soluciones homogéneas)
>    ├─ Subespacios de matrices especiales
>    ├─ Espacios de polinomios
>    └─ Procesamiento de señales
> ```

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **El span es el concepto constructor del álgebra lineal**
>     - Define subespacios mediante vectores generadores
>     - Permite "construir" espacios a partir de bloques básicos
>     - Es la base para entender dimensión y bases
> 2. **Todo subespacio puede expresarse como span**
>     - Cualquier subespacio es el span de algún conjunto
>     - Esto unifica la teoría de subespacios
> 3. **Método práctico para trabajar con subespacios**
>     - Más fácil trabajar con generadores que con ecuaciones
>     - Permite cálculos concretos (combinaciones lineales)
>     - Conexión directa con sistemas de ecuaciones
> 4. **La geometría ayuda a la intuición**
>     - En ℝ² y ℝ³: rectas, planos, espacios
>     - Visualización crucial para entender
>     - Generaliza a dimensiones superiores
> 5. **Redundancia es un tema central**
>     - No todos los generadores son necesarios
>     - Lleva naturalmente a independencia lineal
>     - Base = conjunto generador minimal
> 
> ---
> 
> ### Próximos Pasos
> 
> Con el espacio generado dominado, estás listo para:
> 
> - **Independencia Lineal:** Cuándo un conjunto no tiene redundancia
> - **Base y Dimensión:** Conjuntos generadores optimales
> - **Rango de una Matriz:** Dimensión del espacio columna
> - **Núcleo de una Matriz:** Espacio de soluciones
> - **Transformaciones Lineales:** Imagen y kernel
> 
> ---
> 
> ### Estrategia de Estudio
> 
> **Para dominar este tema:**
> 
> 1. ✅ Practicar cálculo de spans en ℝ² y ℝ³
> 2. ✅ Visualizar geométricamente los resultados
> 3. ✅ Resolver sistemas para verificar pertenencia
> 4. ✅ Identificar vectores redundantes
> 5. ✅ Conectar con subespacios vistos antes
> 6. ✅ Aplicar a espacios abstractos (matrices, polinomios)
> 
> ---
> 
> ### Reflexión Final
> 
> El concepto de span es uno de los más fundamentales en álgebra lineal:
> 
> - Conecta vectores individuales con subespacios completos
> - Proporciona una forma constructiva de definir subespacios
> - Es la base para todos los conceptos posteriores (independencia, base, dimensión)
> 
> **Mensaje clave:** Dominar el span es dominar la forma en que "construimos" espacios vectoriales a partir de bloques básicos. Todo lo demás en álgebra lineal se construye sobre esta idea.

---

**Tags:** #algebra-lineal #espacio-generado #span #subespacios #combinaciones-lineales #vectores #independencia-lineal #base-dimension #espacio-columna #geometria-vectorial
# 📘 Subespacios Vectoriales

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes los Subespacios Vectoriales?
> 
> Los subespacios vectoriales son **subconjuntos especiales** de espacios vectoriales que heredan la estructura de espacio vectorial. Son fundamentales para entender la estructura interna de los espacios vectoriales.
> 
> **Motivación:**
> 
> - En $\mathbb{R}^3$: planos y rectas por el origen son subespacios
> - Permiten **descomponer** problemas complejos en partes más simples
> - Son la base para conceptos como **rango**, **núcleo** y **dimensión**
> 
> **Aplicaciones prácticas:**
> 
> - **Física:** Espacios de estados, simetrías de sistemas físicos
> - **Computación:** Compresión de datos, reducción de dimensionalidad
> - **Ecuaciones Diferenciales:** Espacios de soluciones
> - **Aprendizaje Automático:** Espacios de características, PCA
> 
> **Idea clave:**
> 
> - Un subespacio es un "espacio vectorial dentro de otro espacio vectorial"
> - Si dos vectores están en un subespacio, su suma y múltiplos también lo están
> - Los subespacios siempre contienen el vector cero

---

## 📐 Definición de Subespacio Vectorial

### 📋 Definición Formal

> [!example]- 🟢 Definición: Subespacio Vectorial
> 
> **Definición:** Sea $V$ un espacio vectorial sobre un campo $\mathbb{F}$ (usualmente $\mathbb{R}$ o $\mathbb{C}$). Un subconjunto $W \subseteq V$ es un **subespacio vectorial** de $V$ si satisface:
> 
> 1. **Contiene el vector cero:** $\vec{0} \in W$
> 2. **Cerrado bajo la suma:** Si $\vec{u}, \vec{v} \in W$, entonces $\vec{u} + \vec{v} \in W$
> 3. **Cerrado bajo multiplicación por escalar:** Si $\vec{v} \in W$ y $c \in \mathbb{F}$, entonces $c\vec{v} \in W$
> 
> ---
> 
> **Notación:**
> 
> - $W \leq V$ significa "$W$ es subespacio de $V$"
> - $W < V$ significa "$W$ es subespacio propio de $V$" (es decir, $W \neq V$)
> 
> ---
> 
> **Interpretación:**
> 
> Un subespacio es un subconjunto que "se comporta como un espacio vectorial" usando las mismas operaciones de $V$.
> 
> ---
> 
> **Consecuencia importante:**
> 
> Si $W$ es subespacio de $V$, entonces $W$ es **automáticamente** un espacio vectorial con las operaciones heredadas de $V$.

> [!tip]- ✅ Criterio del Subespacio (Versión Compacta)
> 
> **Teorema:** Un subconjunto no vacío $W \subseteq V$ es un subespacio si y solo si:
> 
> $$\text{Para todo } \vec{u}, \vec{v} \in W \text{ y todo } c \in \mathbb{F}: \quad c\vec{u} + \vec{v} \in W$$
> 
> Esta es una **condición única** que combina las tres anteriores.
> 
> ---
> 
> **Ventaja:** Solo necesitas verificar UNA propiedad en lugar de tres.
> 
> **Nota:** Esta versión automáticamente garantiza que $\vec{0} \in W$ (tomando $c = 0$).

### 🎯 Interpretación Geométrica

> [!note]- 📊 Visualización en $\mathbb{R}^2$ y $\mathbb{R}^3$
> 
> ### Subespacios de $\mathbb{R}^2$
> 
> ```
>       y
>       |
>       |  / â† Recta por el origen (subespacio 1D)
>       | /
>       |/
>   ----+---- x
>      /|
>     / |
>        â†' Otra recta por el origen
> ```
> 
> **Subespacios de $\mathbb{R}^2$:**
> 
> 1. ${\vec{0}}$ - el vector cero (dimensión 0)
> 2. Cualquier recta que pase por el origen (dimensión 1)
> 3. Todo $\mathbb{R}^2$ (dimensión 2)
> 
> **NO son subespacios:**
> 
> - Rectas que NO pasan por el origen
> - Curvas
> - Regiones acotadas
> 
> ---
> 
> ### Subespacios de $\mathbb{R}^3$
> 
> ```
>         z
>         |
>         |    Plano por origen
>         |   /
>         |  /
>         | /
>         |/
>   ------+------ y
>        /|
>       / |
>      /  |
>     x   Recta por origen
> ```
> 
> **Subespacios de $\mathbb{R}^3$:**
> 
> 1. ${\vec{0}}$ (dimensión 0)
> 2. Cualquier recta por el origen (dimensión 1)
> 3. Cualquier plano por el origen (dimensión 2)
> 4. Todo $\mathbb{R}^3$ (dimensión 3)
> 
> **Regla de oro:** En $\mathbb{R}^n$, los subespacios geométricos SIEMPRE pasan por el origen.

---

## 📚 Ejemplos Básicos

### Ejemplo 1: Subespacios de $\mathbb{R}^2$

> [!example]- 📍 Ejemplo 1: Rectas por el Origen
> 
> **a) La recta $y = 2x$**
> 
> $$W = {(x, 2x) : x \in \mathbb{R}} = {(x, y) : y = 2x}$$
> 
> **Verificación:**
> 
> 1. **Vector cero:** $(0,0)$ satisface $y = 2x$ ✓
>     
> 2. **Cerrado bajo suma:**
>     
>     - Sean $\vec{u} = (x_1, 2x_1)$ y $\vec{v} = (x_2, 2x_2)$
>     - $\vec{u} + \vec{v} = (x_1 + x_2, 2x_1 + 2x_2) = (x_1 + x_2, 2(x_1 + x_2))$
>     - La segunda coordenada es el doble de la primera ✓
> 3. **Cerrado bajo multiplicación:**
>     
>     - Sea $c \in \mathbb{R}$ y $\vec{v} = (x, 2x)$
>     - $c\vec{v} = (cx, 2cx) = (cx, 2(cx))$
>     - La segunda coordenada es el doble de la primera ✓
> 
> $$\boxed{W \text{ es un subespacio de } \mathbb{R}^2}$$
> 
> ---
> 
> **b) La recta $y = 2x + 1$ (NO es subespacio)**
> 
> $$W = {(x, y) : y = 2x + 1}$$
> 
> **Verificación:**
> 
> 4. **Vector cero:** $(0,0)$ no satisface $y = 2x + 1$ ya que $0 \neq 1$ ✗
> 
> $$\boxed{\text{NO es subespacio (no pasa por el origen)}}$$
> 
> ---
> 
> **Conclusión general:** En $\mathbb{R}^2$, una recta $y = mx + b$ es subespacio ⟺ $b = 0$.

### Ejemplo 2: Subespacios de $\mathbb{R}^3$

> [!example]- 📍 Ejemplo 2: Planos y Rectas en $\mathbb{R}^3$
> 
> **a) El plano $xy$ (donde $z = 0$)**
> 
> $$W = {(x, y, 0) : x, y \in \mathbb{R}}$$
> 
> **Verificación:**
> 
> 1. $\vec{0} = (0,0,0) \in W$ ✓
>     
> 2. Si $(x_1, y_1, 0), (x_2, y_2, 0) \in W$: $$\text{suma} = (x_1+x_2, y_1+y_2, 0+0) = (x_1+x_2, y_1+y_2, 0) \in W$$ ✓
>     
> 3. Si $(x, y, 0) \in W$ y $c \in \mathbb{R}$: $$c(x,y,0) = (cx, cy, 0) \in W$$ ✓
>     
> 
> $$\boxed{W \text{ es subespacio}}$$
> 
> **Análogamente:** Los planos $xz$ y $yz$ también son subespacios.
> 
> ---
> 
> **b) El plano $x + y + z = 0$**
> 
> $$W = {(x, y, z) : x + y + z = 0}$$
> 
> **Verificación:**
> 
> 4. $(0,0,0)$ satisface $0+0+0=0$ ✓
>     
> 5. Si $x_1+y_1+z_1=0$ y $x_2+y_2+z_2=0$: $$(x_1+x_2) + (y_1+y_2) + (z_1+z_2) = (x_1+y_1+z_1) + (x_2+y_2+z_2) = 0+0 = 0$$ ✓
>     
> 6. Si $x+y+z=0$ y $c \in \mathbb{R}$: $$cx + cy + cz = c(x+y+z) = c \cdot 0 = 0$$ ✓
>     
> 
> $$\boxed{W \text{ es subespacio}}$$
> 
> ---
> 
> **c) El plano $x + y + z = 1$ (NO es subespacio)**
> 
> $(0,0,0)$ no satisface $0+0+0=1$ ✗
> 
> $$\boxed{\text{NO es subespacio}}$$
> 
> ---
> 
> **Regla general:** El plano $ax + by + cz = d$ es subespacio ⟺ $d = 0$.

### Ejemplo 3: Subespacios Triviales

> [!example]- 📍 Ejemplo 3: Subespacios en Todo Espacio Vectorial
> 
> Para **cualquier** espacio vectorial $V$:
> 
> ### 1. El subespacio cero
> 
> $$W = {\vec{0}}$$
> 
> **Verificación trivial:**
> 
> - Contiene $\vec{0}$ ✓
> - $\vec{0} + \vec{0} = \vec{0} \in W$ ✓
> - $c\vec{0} = \vec{0} \in W$ ✓
> 
> ---
> 
> ### 2. El espacio total
> 
> $$W = V$$
> 
> **Verificación trivial:** $V$ satisface todas las propiedades por definición.
> 
> ---
> 
> **Definición:**
> 
> - ${\vec{0}}$ se llama el **subespacio trivial** o **subespacio cero**
> - $V$ se llama el **subespacio impropio**
> - Cualquier otro subespacio es un **subespacio propio no trivial**
> 
> ---
> 
> **Teorema:** Todo espacio vectorial $V$ tiene al menos **dos subespacios**: ${\vec{0}}$ y $V$.

### Ejemplo 4: Matrices

> [!example]- 📍 Ejemplo 4: Subespacios de Matrices
> 
> Sea $M_{2×2}(\mathbb{R})$ el espacio de matrices $2 \times 2$ con entradas reales.
> 
> **a) Matrices simétricas**
> 
> $$W = \left{\begin{pmatrix} a & b \ b & c \end{pmatrix} : a, b, c \in \mathbb{R}\right}$$
> 
> **Verificación:**
> 
> 1. La matriz cero es simétrica ✓
>     
> 2. Suma de matrices simétricas: $$\begin{pmatrix} a_1 & b_1 \ b_1 & c_1 \end{pmatrix} + \begin{pmatrix} a_2 & b_2 \ b_2 & c_2 \end{pmatrix} = \begin{pmatrix} a_1+a_2 & b_1+b_2 \ b_1+b_2 & c_1+c_2 \end{pmatrix}$$ es simétrica ✓
>     
> 3. Múltiplo escalar de simétrica es simétrica ✓
>     
> 
> $$\boxed{W \text{ es subespacio}}$$
> 
> ---
> 
> **b) Matrices diagonales**
> 
> $$W = \left{\begin{pmatrix} a & 0 \ 0 & b \end{pmatrix} : a, b \in \mathbb{R}\right}$$
> 
> **Verificación:** Similar al caso anterior.
> 
> $$\boxed{W \text{ es subespacio}}$$
> 
> ---
> 
> **c) Matrices con determinante 1 (NO es subespacio)**
> 
> $$W = {A \in M_{2×2}(\mathbb{R}) : \det(A) = 1}$$
> 
> **Contraejemplo:**
> 
> - $I = \begin{pmatrix} 1 & 0 \ 0 & 1 \end{pmatrix}$ tiene $\det(I) = 1$ ✓
> - Pero $2I = \begin{pmatrix} 2 & 0 \ 0 & 2 \end{pmatrix}$ tiene $\det(2I) = 4 \neq 1$ ✗
> 
> $$\boxed{\text{NO es subespacio (no cerrado bajo multiplicación escalar)}}$$

### Ejemplo 5: Polinomios

> [!example]- 📍 Ejemplo 5: Subespacios de Polinomios
> 
> Sea $P_n$ el espacio de polinomios de grado ≤ $n$.
> 
> **a) Polinomios pares**
> 
> $$W = {p(x) \in P_n : p(-x) = p(x)}$$
> 
> Ejemplo: $p(x) = x^4 + 3x^2 + 5$
> 
> **Verificación:**
> 
> 1. El polinomio cero es par ✓
>     
> 2. Si $p(-x) = p(x)$ y $q(-x) = q(x)$: $$(p+q)(-x) = p(-x) + q(-x) = p(x) + q(x) = (p+q)(x)$$ ✓
>     
> 3. Si $p(-x) = p(x)$ y $c \in \mathbb{R}$: $$(cp)(-x) = cp(-x) = cp(x) = (cp)(x)$$ ✓
>     
> 
> $$\boxed{W \text{ es subespacio}}$$
> 
> ---
> 
> **b) Polinomios con coeficiente constante cero**
> 
> $$W = {p(x) = a_1x + a_2x^2 + \cdots + a_nx^n : a_i \in \mathbb{R}}$$
> 
> Es decir, $p(0) = 0$.
> 
> **Verificación:** Ejercicio (es subespacio) ✓
> 
> ---
> 
> **c) Polinomios con $p(1) = 2$ (NO es subespacio)**
> 
> $$W = {p(x) \in P_n : p(1) = 2}$$
> 
> El polinomio cero satisface $p(1) = 0 \neq 2$ ✗
> 
> $$\boxed{\text{NO es subespacio}}$$

---

## 🔬 Propiedades Fundamentales

### 🎯 Teoremas Básicos

> [!note]- 🟡 Propiedades de Subespacios
> 
> ### Teorema 1: Intersección de Subespacios
> 
> **Enunciado:** Si $W_1$ y $W_2$ son subespacios de $V$, entonces:
> 
> $$W_1 \cap W_2 \text{ es subespacio de } V$$
> 
> **Demostración:**
> 
> 1. $\vec{0} \in W_1$ y $\vec{0} \in W_2$ ⟹ $\vec{0} \in W_1 \cap W_2$ ✓
>     
> 2. Si $\vec{u}, \vec{v} \in W_1 \cap W_2$:
>     
>     - $\vec{u}, \vec{v} \in W_1$ ⟹ $\vec{u}+\vec{v} \in W_1$
>     - $\vec{u}, \vec{v} \in W_2$ ⟹ $\vec{u}+\vec{v} \in W_2$
>     - Por lo tanto, $\vec{u}+\vec{v} \in W_1 \cap W_2$ ✓
> 3. Similar para multiplicación escalar ✓
>     
> 
> ---
> 
> **Generalización:** La intersección de **cualquier cantidad** de subespacios es un subespacio:
> 
> $$\bigcap_{i \in I} W_i \text{ es subespacio}$$
> 
> ---
> 
> ### ⚠️ Advertencia: La unión NO es subespacio
> 
> **Contraejemplo en $\mathbb{R}^2$:**
> 
> - $W_1 = {(x, 0) : x \in \mathbb{R}}$ (eje $x$)
> - $W_2 = {(0, y) : y \in \mathbb{R}}$ (eje $y$)
> 
> Ambos son subespacios, pero:
> 
> - $(1, 0) \in W_1 \subseteq W_1 \cup W_2$
> - $(0, 1) \in W_2 \subseteq W_1 \cup W_2$
> - $(1, 1) = (1, 0) + (0, 1) \notin W_1 \cup W_2$ ✗
> 
> $$\boxed{W_1 \cup W_2 \text{ NO es subespacio en general}}$$

> [!note]- 🟡 Teorema 2: Caracterización por Combinaciones Lineales
> 
> **Teorema:** $W$ es subespacio de $V$ si y solo si $W$ contiene todas las combinaciones lineales de sus elementos.
> 
> **Formalmente:** $W \leq V$ ⟺ Para todo $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k \in W$ y $c_1, c_2, \ldots, c_k \in \mathbb{F}$:
> 
> $$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k \in W$$
> 
> ---
> 
> **Interpretación:** Un subespacio es "cerrado bajo combinaciones lineales finitas".

---

## 🌟 Generación de Subespacios

### 📋 Definición de Span

> [!example]- 🟢 Definición: Espacio Generado (Span)
> 
> **Definición:** Sean $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k$ vectores en $V$. El **espacio generado** por estos vectores es:
> 
> $$\text{span}{\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k} = {c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k : c_i \in \mathbb{F}}$$
> 
> Es decir, el conjunto de **todas las combinaciones lineales** de $\vec{v}_1, \ldots, \vec{v}_k$.
> 
> ---
> 
> **Notación alternativa:**
> 
> - $\text{span}{\vec{v}_1, \ldots, \vec{v}_k}$
> - $\langle \vec{v}_1, \ldots, \vec{v}_k \rangle$
> - $[\vec{v}_1, \ldots, \vec{v}_k]$
> 
> ---
> 
> **Propiedades:**
> 
> 1. $\text{span}{\vec{v}_1, \ldots, \vec{v}_k}$ es **siempre un subespacio**
> 2. Es el **subespacio más pequeño** que contiene a $\vec{v}_1, \ldots, \vec{v}_k$
> 3. Si $W = \text{span}{\vec{v}_1, \ldots, \vec{v}_k}$, decimos que ${\vec{v}_1, \ldots, \vec{v}_k}$ **genera** o **engendra** a $W$

> [!tip]- ✅ Teorema: El Span es un Subespacio
> 
> **Teorema:** Para cualquier conjunto de vectores ${\vec{v}_1, \ldots, \vec{v}_k} \subseteq V$:
> 
> $$W = \text{span}{\vec{v}_1, \ldots, \vec{v}_k} \text{ es un subespacio de } V$$
> 
> **Demostración:**
> 
> 4. **Vector cero:** $\vec{0} = 0\vec{v}_1 + \cdots + 0\vec{v}_k \in W$ ✓
>     
> 5. **Suma:** Si $\vec{u} = \sum a_i\vec{v}_i$ y $\vec{w} = \sum b_i\vec{v}_i$: $$\vec{u} + \vec{w} = \sum (a_i + b_i)\vec{v}_i \in W$$ ✓
>     
> 6. **Multiplicación:** Si $\vec{u} = \sum a_i\vec{v}_i$ y $c \in \mathbb{F}$: $$c\vec{u} = \sum (ca_i)\vec{v}_i \in W$$ ✓
>     

### Ejemplos de Span

> [!example]- 📍 Ejemplo 6: Span en $\mathbb{R}^2$
> 
> **a) Span de un vector no nulo**
> 
> $$W = \text{span}\left{\begin{pmatrix} 1 \ 2 \end{pmatrix}\right} = \left{c\begin{pmatrix} 1 \ 2 \end{pmatrix} : c \in \mathbb{R}\right}$$
> 
> **Interpretación geométrica:** La recta $y = 2x$ (pasa por el origen)
> 
> ```
>       y
>       |
>     4 |    â€¢
>       |   /
>     2 |  â€¢
>       | /
>     0 +------ x
>       0  1  2
> ```
> 
> ---
> 
> **b) Span de dos vectores no colineales**
> 
> $$W = \text{span}\left{\begin{pmatrix} 1 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \end{pmatrix}\right}$$
> 
> $$= \left{c_1\begin{pmatrix} 1 \ 0 \end{pmatrix} + c_2\begin{pmatrix} 0 \ 1 \end{pmatrix} : c_1, c_2 \in \mathbb{R}\right}$$
> 
> $$= \left{\begin{pmatrix} c_1 \ c_2 \end{pmatrix} : c_1, c_2 \in \mathbb{R}\right} = \mathbb{R}^2$$
> 
> **Interpretación:** Estos dos vectores generan **todo** $\mathbb{R}^2$
> 
> ---
> 
> **c) Span de vectores colineales**
> 
> $$W = \text{span}\left{\begin{pmatrix} 1 \ 2 \end{pmatrix}, \begin{pmatrix} 2 \ 4 \end{pmatrix}\right}$$
> 
> Nota que $\begin{pmatrix} 2 \ 4 \end{pmatrix} = 2\begin{pmatrix} 1 \ 2 \end{pmatrix}$
> 
> Por lo tanto:
> 
> $$W = \text{span}\left{\begin{pmatrix} 1 \ 2 \end{pmatrix}\right}$$
> 
> **Interpretación:** Agregar vectores dependientes no "expande" el span.

> [!example]- 📍 Ejemplo 7: Span en $\mathbb{R}^3$
> 
> **a) Span de un vector (recta)**
> 
> $$W = \text{span}\left{\begin{pmatrix} 1 \ 1 \ 1 \end{pmatrix}\right}$$
> 
> Es la recta $x = y = z$ (diagonal principal del cubo unitario)
> 
> ---
> 
> **b) Span de dos vectores (plano)**
> 
> $$W = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}\right}$$
> 
> $$= \left{\begin{pmatrix} a \ b \ 0 \end{pmatrix} : a, b \in \mathbb{R}\right}$$
> 
> Es el **plano $xy$** (donde $z = 0$)
> 
> ---
> 
> **c) Span de tres vectores linealmente independientes**
> 
> $$W = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix}\right} = \mathbb{R}^3$$
> 
> ---
> 
> **Patrón en $\mathbb{R}^3$:**
> 
> - 1 vector independiente → recta (dimensión 1)
> - 2 vectores independientes → plano (dimensión 2)
> - 3 vectores independientes → todo $\mathbb{R}^3$ (dimensión 3)

> [!example]- 📍 Ejemplo 8: Span en Polinomios
> 
> Sea $P_2$ el espacio de polinomios de grado ≤ 2.
> 
> **a) Polinomios sin término constante**
> 
> $$W = \text{span}{x, x^2}$$
> 
> $$= {ax + bx^2 : a, b \in \mathbb{R}}$$
> 
> Estos son todos los polinomios con $p(0) = 0$.
> 
> ---
> 
> **b) Todo $P_2$**
> 
> $$P_2 = \text{span}{1, x, x^2}$$
> 
> Cualquier polinomio $p(x) = a_0 + a_1x + a_2x^2$ es combinación lineal de ${1, x, x^2}$.

---

## 🔧 Suma de Subespacios

### 📋 Definición

> [!example]- 🟢 Definición: Suma de Subespacios
> 
> **Definición:** Sean $W_1$ y $W_2$ subespacios de $V$. La **suma** de $W_1$ y $W_2$ es:
> 
> $$W_1 + W_2 = {\vec{w}_1 + \vec{w}_2 : \vec{w}_1 \in W_1, \vec{w}_2 \in W_2}$$
> 
> ---
> 
> **Teorema:** $W_1 + W_2$ es un subespacio de $V$.
> 
> **Demostración:** Ejercicio (similar a probar que span es subespacio).
> 
> ---
> 
> **Propiedades:**
> 
> 1. $W_1 + W_2 = \text{span}(W_1 \cup W_2)$
> 2. $W_1 + W_2$ es el **subespacio más pequeño** que contiene a $W_1$ y $W_2$ 3. $W_1 \subseteq W_1 + W_2$ y $W_2 \subseteq W_1 + W_2$ 4. $W_1 \cap W_2 \subseteq W_1 + W_2$
> 
> ---
> 
> **Generalización:** Para múltiples subespacios:
> 
> $$W_1 + W_2 + \cdots + W_k = {\vec{w}_1 + \vec{w}_2 + \cdots + \vec{w}_k : \vec{w}_i \in W_i}$$

### Ejemplos de Suma de Subespacios

> [!example]- 📍 Ejemplo 9: Suma en $\mathbb{R}^3$
> 
> **a) Suma de dos rectas**
> 
> $$W_1 = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}\right} \quad \text{(eje } x\text{)}$$
> 
> $$W_2 = \text{span}\left{\begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}\right} \quad \text{(eje } y\text{)}$$
> 
> $$W_1 + W_2 = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}\right}$$
> 
> $$= \left{\begin{pmatrix} a \ b \ 0 \end{pmatrix} : a, b \in \mathbb{R}\right} = \text{plano } xy$$
> 
> **Observación:** La suma de dos rectas (no colineales) genera un plano.
> 
> ---
> 
> **b) Suma de plano y recta**
> 
> $$W_1 = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}\right} \quad \text{(plano } xy\text{)}$$
> 
> $$W_2 = \text{span}\left{\begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix}\right} \quad \text{(eje } z\text{)}$$
> 
> $$W_1 + W_2 = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix}\right} = \mathbb{R}^3$$

### Suma Directa

> [!example]- 🟣 Definición: Suma Directa
> 
> **Definición:** Sean $W_1$ y $W_2$ subespacios de $V$. Decimos que $V$ es la **suma directa** de $W_1$ y $W_2$ si:
> 
> 1. $V = W_1 + W_2$ (todo vector de $V$ se escribe como suma)
> 2. $W_1 \cap W_2 = {\vec{0}}$ (la intersección es trivial)
> 
> **Notación:** $V = W_1 \oplus W_2$
> 
> ---
> 
> **Caracterización equivalente:** $V = W_1 \oplus W_2$ si y solo si **todo** $\vec{v} \in V$ se escribe **de manera única** como:
> 
> $$\vec{v} = \vec{w}_1 + \vec{w}_2, \quad \vec{w}_1 \in W_1, \vec{w}_2 \in W_2$$
> 
> ---
> 
> **Interpretación geométrica:** Los subespacios son "complementarios" y no se "traslapan" (excepto en el origen).

> [!example]- 📍 Ejemplo 10: Suma Directa
> 
> **a) En $\mathbb{R}^2$**
> 
> $$W_1 = \text{span}\left{\begin{pmatrix} 1 \ 0 \end{pmatrix}\right}, \quad W_2 = \text{span}\left{\begin{pmatrix} 0 \ 1 \end{pmatrix}\right}$$
> 
> - $W_1 + W_2 = \mathbb{R}^2$ ✓
> - $W_1 \cap W_2 = {\vec{0}}$ ✓
> 
> $$\boxed{\mathbb{R}^2 = W_1 \oplus W_2}$$
> 
> Cualquier vector $\begin{pmatrix} a \ b \end{pmatrix} = a\begin{pmatrix} 1 \ 0 \end{pmatrix} + b\begin{pmatrix} 0 \ 1 \end{pmatrix}$ (representación única)
> 
> ---
> 
> **b) En $\mathbb{R}^3$**
> 
> $$W_1 = \text{plano } xy = \left{\begin{pmatrix} x \ y \ 0 \end{pmatrix}\right}$$
> 
> $$W_2 = \text{eje } z = \left{\begin{pmatrix} 0 \ 0 \ z \end{pmatrix}\right}$$
> 
> - $W_1 + W_2 = \mathbb{R}^3$ ✓
> - $W_1 \cap W_2 = {\vec{0}}$ ✓
> 
> $$\boxed{\mathbb{R}^3 = W_1 \oplus W_2}$$
> 
> ---
> 
> **c) NO suma directa**
> 
> $$W_1 = \text{span}\left{\begin{pmatrix} 1 \ 1 \end{pmatrix}\right}, \quad W_2 = \text{span}\left{\begin{pmatrix} 2 \ 2 \end{pmatrix}\right}$$
> 
> - $W_1 = W_2$ (son la misma recta)
> - $W_1 \cap W_2 = W_1 \neq {\vec{0}}$ ✗
> 
> $$\boxed{\text{NO es suma directa}}$$

---

## 🎯 Criterios para Verificar Subespacios

### 🛠️ Guía Práctica

> [!tip]- ✅ Checklist para Verificar Subespacios
> 
> ### Método 1: Definición Directa (3 condiciones)
> 
> Para verificar si $W \subseteq V$ es subespacio:
> 
> 1. ✓ **Verificar que $\vec{0} \in W$**
>     - A menudo es la forma más rápida de descartar
>     - Si $\vec{0} \notin W$, entonces NO es subespacio
> 2. ✓ **Verificar cerradura bajo suma**
>     - Tomar $\vec{u}, \vec{v} \in W$ arbitrarios
>     - Mostrar que $\vec{u} + \vec{v} \in W$
> 3. ✓ **Verificar cerradura bajo multiplicación escalar**
>     - Tomar $\vec{v} \in W$ arbitrario y $c \in \mathbb{F}$ arbitrario
>     - Mostrar que $c\vec{v} \in W$
> 
> ---
> 
> ### Método 2: Criterio Compacto (1 condición)
> 
> Verificar que para todo $\vec{u}, \vec{v} \in W$ y $c \in \mathbb{F}$:
> 
> $$c\vec{u} + \vec{v} \in W$$
> 
> **Ventaja:** Una sola verificación
> 
> **Nota:** Automáticamente implica $\vec{0} \in W$ (tomar $c = 0$)
> 
> ---
> 
> ### Método 3: Por Span
> 
> Si puedes escribir $W = \text{span}{\vec{v}_1, \ldots, \vec{v}_k}$, entonces $W$ es subespacio automáticamente.
> 
> ---
> 
> ### Método 4: Como Núcleo o Imagen
> 
> Si $W$ es el núcleo o imagen de una transformación lineal, entonces es subespacio (tema futuro).

> [!warning]- ⚠️ Trampas Comunes
> 
> ### ❌ Errores Frecuentes
> 
> **1. Olvidar verificar el vector cero**
> 
> Ejemplo malo: $W = {(x, y) : x + y = 1}$
> 
> - Parece un plano, pero $(0,0) \notin W$ ✗
> 
> ---
> 
> **2. Confundir "subconjunto" con "subespacio"**
> 
> Todo subespacio es subconjunto, pero NO todo subconjunto es subespacio.
> 
> Ejemplo: ${(x, y) : x \geq 0, y \geq 0}$ (primer cuadrante)
> 
> - Es subconjunto de $\mathbb{R}^2$
> - NO es subespacio (no cerrado bajo multiplicación por negativos)
> 
> ---
> 
> **3. Asumir que la unión es subespacio**
> 
> $W_1 \cup W_2$ generalmente NO es subespacio.
> 
> ---
> 
> **4. Verificar solo con ejemplos específicos**
> 
> Debes demostrar para vectores **arbitrarios**, no solo casos particulares.
> 
> ❌ Mal: "Tomando $\vec{u} = (1,0)$ y $\vec{v} = (0,1)$..."
> 
> ✓ Bien: "Sean $\vec{u}, \vec{v} \in W$ arbitrarios..."
> 
> ---
> 
> **5. Condiciones necesarias vs suficientes**
> 
> - Contener $\vec{0}$ es **necesario** pero NO suficiente
> - Las tres condiciones juntas son **necesarias Y suficientes**

---

## 📊 Tabla de Subespacios Comunes

> [!note]- 📋 Referencia Rápida: Subespacios Clásicos
> 
> |Espacio|Subespacio|Descripción|Dimensión|
> |---|---|---|---|
> |$\mathbb{R}^2$|${\vec{0}}$|Solo el origen|0|
> |$\mathbb{R}^2$|Recta por origen|${t\vec{v} : t \in \mathbb{R}}$|1|
> |$\mathbb{R}^2$|$\mathbb{R}^2$|Todo el plano|2|
> |$\mathbb{R}^3$|${\vec{0}}$|Solo el origen|0|
> |$\mathbb{R}^3$|Recta por origen|$\text{span}{\vec{v}}$|1|
> |$\mathbb{R}^3$|Plano por origen|$\text{span}{\vec{v}_1, \vec{v}_2}$|2|
> |$\mathbb{R}^3$|$\mathbb{R}^3$|Todo el espacio|3|
> |$M_{n×n}$|Matrices simétricas|$A^T = A$|$\frac{n(n+1)}{2}$|
> |$M_{n×n}$|Matrices antisimétricas|$A^T = -A$|$\frac{n(n-1)}{2}$|
> |$M_{n×n}$|Matrices diagonales|Ceros fuera diagonal|$n$|
> |$M_{n×n}$|Matrices triangulares sup.|Ceros debajo diagonal|$\frac{n(n+1)}{2}$|
> |$P_n$|Polinomios pares|$p(-x) = p(x)$|$\lceil \frac{n+1}{2} \rceil$|
> |$P_n$|Polinomios impares|$p(-x) = -p(x)$|$\lfloor \frac{n+1}{2} \rfloor$|
> |$\mathbb{R}^n$|Hiperplano|$\vec{a} \cdot \vec{x} = 0$|$n-1$|
> |$C[a,b]$|Funciones con $f(a)=0$|Condición inicial|$\infty$|

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Verificar si son subespacios de $\mathbb{R}^2$:**
> 
> a) $W = {(x, 2x) : x \in \mathbb{R}}$
> 
> b) $W = {(x, y) : x + y = 0}$
> 
> c) $W = {(x, y) : x + y = 1}$
> 
> d) $W = {(x, y) : xy = 0}$ (ejes coordenados)
> 
> e) $W = {(x, y) : x \geq 0, y \geq 0}$ (primer cuadrante)
> 
> f) $W = {(x, 0) : x \in \mathbb{R}}$ (eje $x$)
> 
> ---
> 
> **2. Verificar si son subespacios de $\mathbb{R}^3$:**
> 
> a) $W = {(x, y, z) : x + y + z = 0}$
> 
> b) $W = {(x, y, z) : x = y = z}$
> 
> c) $W = {(x, y, z) : z = 1}$
> 
> d) $W = {(x, y, z) : x^2 + y^2 + z^2 = 0}$
> 
> e) $W = {(x, y, 0) : x, y \in \mathbb{R}}$
> 
> ---
> 
> **3. Encontrar el span:**
> 
> a) $\text{span}\left{\begin{pmatrix} 1 \ 2 \end{pmatrix}\right}$
> 
> b) $\text{span}\left{\begin{pmatrix} 1 \ 0 \ 1 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 1 \end{pmatrix}\right}$
> 
> c) $\text{span}{1, x, x^2}$ en $P_3$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Verificar subespacios de matrices:**
> 
> a) Matrices $2×2$ con traza cero: $W = \left{\begin{pmatrix} a & b \ c & d \end{pmatrix} : a + d = 0\right}$
> 
> b) Matrices $2×2$ con determinante 0
> 
> c) Matrices $2×2$ que conmutan con $\begin{pmatrix} 1 & 0 \ 0 & 2 \end{pmatrix}$
> 
> ---
> 
> **5. Intersección y suma:**
> 
> a) $W_1 = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}\right}$, $W_2 = \text{span}\left{\begin{pmatrix} 1 \ 1 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix}\right}$
> 
> Encontrar $W_1 \cap W_2$ y $W_1 + W_2$
> 
> b) ¿Es $\mathbb{R}^3 = W_1 \oplus W_2$?
> 
> ---
> 
> **6. En $P_3$ (polinomios grado ≤ 3):**
> 
> a) $W_1 = {p(x) : p(0) = 0}$
> 
> b) $W_2 = {p(x) : p(1) = 0}$
> 
> Verificar que son subespacios y encontrar $W_1 \cap W_2$
> 
> ---
> 
> **7. Demostrar:**
> 
> a) Si $W_1 \subseteq W_2$, entonces $W_1 \cap W_2 = W_1$ y $W_1 + W_2 = W_2$
> 
> b) $(W_1 + W_2) + W_3 = W_1 + (W_2 + W_3)$ (asociatividad)

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **8. Problemas teóricos:**
> 
> a) Demostrar que si $W$ es subespacio de dimensión finita, entonces cualquier conjunto que genera $W$ contiene al menos $\dim(W)$ vectores
> 
> b) Demostrar que la intersección de todos los subespacios que contienen a un conjunto $S$ es $\text{span}(S)$
> 
> c) Si $V = W_1 \oplus W_2$, demostrar que $\dim(V) = \dim(W_1) + \dim(W_2)$
> 
> ---
> 
> **9. Complementos ortogonales:**
> 
> En $\mathbb{R}^3$, dado $W = \text{span}\left{\begin{pmatrix} 1 \ 1 \ 0 \end{pmatrix}\right}$, encontrar $W^\perp = {\vec{v} : \vec{v} \cdot \vec{w} = 0 \text{ para todo } \vec{w} \in W}$
> 
> Verificar que $\mathbb{R}^3 = W \oplus W^\perp$
> 
> ---
> 
> **10. Subespacios de funciones:**
> 
> En $C(\mathbb{R})$ (funciones continuas):
> 
> a) $W = {f : f(-x) = f(x)}$ (funciones pares)
> 
> b) $W = {f : f(-x) = -f(x)}$ (funciones impares)
> 
> Demostrar que $C(\mathbb{R}) = W_{\text{par}} + W_{\text{impar}}$ (no necesariamente directa)
> 
> ---
> 
> **11. Problema de dimensión:**
> 
> Demostrar la **fórmula de Grassmann**:
> 
> $$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $W = {(x, 2x) : x \in \mathbb{R}}$
> 
> 1. $(0,0) \in W$ ✓
> 2. $(x_1, 2x_1) + (x_2, 2x_2) = (x_1+x_2, 2(x_1+x_2)) \in W$ ✓
> 3. $c(x, 2x) = (cx, 2cx) \in W$ ✓
> 
> $$\boxed{\text{SÍ es subespacio}}$$
> 
> ---
> 
> **1c)** $W = {(x, y) : x + y = 1}$
> 
> $(0,0)$ no satisface $0 + 0 = 1$ ✗
> 
> $$\boxed{\text{NO es subespacio}}$$
> 
> ---
> 
> **1d)** $W = {(x, y) : xy = 0}$ (ejes coordenados)
> 
> - $(1, 0) \in W$ ✓
> - $(0, 1) \in W$ ✓
> - $(1, 0) + (0, 1) = (1, 1)$ pero $1 \cdot 1 = 1 \neq 0$ ✗
> 
> $$\boxed{\text{NO es subespacio (no cerrado bajo suma)}}$$
> 
> ---
> 
> **2a)** $W = {(x, y, z) : x + y + z = 0}$
> 
> 1. $0 + 0 + 0 = 0$ ✓
> 2. Si $x_1+y_1+z_1=0$ y $x_2+y_2+z_2=0$: $(x_1+x_2) + (y_1+y_2) + (z_1+z_2) = 0$ ✓
> 3. Si $x+y+z=0$: $cx + cy + cz = c(x+y+z) = 0$ ✓
> 
> $$\boxed{\text{SÍ es subespacio}}$$
> 
> ---
> 
> **2d)** $W = {(x, y, z) : x^2 + y^2 + z^2 = 0}$
> 
> Solo $(0,0,0)$ satisface esta ecuación (en $\mathbb{R}^3$)
> 
> $$\boxed{W = {\vec{0}} \text{ (subespacio trivial)}}$$
> 
> ---
> 
> **3a)** $\text{span}\left{\begin{pmatrix} 1 \ 2 \end{pmatrix}\right} = \left{\begin{pmatrix} t \ 2t \end{pmatrix} : t \in \mathbb{R}\right}$
> 
> **Interpretación:** La recta $y = 2x$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** Matrices con traza cero
> 
> $W = \left{\begin{pmatrix} a & b \ c & -a \end{pmatrix} : a, b, c \in \mathbb{R}\right}$
> 
> 4. La matriz cero tiene traza 0 ✓
> 5. $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B) = 0 + 0 = 0$ ✓
> 6. $\text{tr}(cA) = c \cdot \text{tr}(A) = c \cdot 0 = 0$ ✓
> 
> $$\boxed{\text{SÍ es subespacio}}$$
> 
> ---
> 
> **4b)** Matrices con determinante 0
> 
> Contraejemplo:
> 
> - $A = \begin{pmatrix} 1 & 0 \ 0 & 0 \end{pmatrix}$ tiene $\det(A) = 0$ ✓
> - $B = \begin{pmatrix} 0 & 0 \ 0 & 1 \end{pmatrix}$ tiene $\det(B) = 0$ ✓
> - $A + B = I$ tiene $\det(I) = 1 \neq 0$ ✗
> 
> $$\boxed{\text{NO es subespacio}}$$
> 
> ---
> 
> **5a)**
> 
> $W_1 = \text{plano } xy$, $W_2 = \text{plano generado por } (1,1,0) \text{ y } (0,0,1)$
> 
> **Intersección:** Vectores en ambos planos deben tener $z = 0$ y estar en $W_2$
> 
> $$W_1 \cap W_2 = \text{span}\left{\begin{pmatrix} 1 \ 1 \ 0 \end{pmatrix}\right}$$
> 
> **Suma:**
> 
> $$W_1 + W_2 = \text{span}\left{\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix}\right} = \mathbb{R}^3$$
> 
> ---
> 
> **6)** $W_1 = {p(x) : p(0) = 0}$
> 
> - Si $p(0) = 0$ y $q(0) = 0$, entonces $(p+q)(0) = 0$ ✓
> - $(cp)(0) = c \cdot p(0) = c \cdot 0 = 0$ ✓
> 
> $$\boxed{W_1 \text{ es subespacio}}$$
> 
> $W_1 = \text{span}{x, x^2, x^3}$
> 
> **Intersección:** $W_1 \cap W_2 = {p(x) : p(0) = 0 \text{ y } p(1) = 0}$
> 
> Ejemplo: $p(x) = x(x-1) = x^2 - x$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **9)** Complemento ortogonal
> 
> $W = \text{span}\left{\begin{pmatrix} 1 \ 1 \ 0 \end{pmatrix}\right}$
> 
> $W^\perp = \left{\begin{pmatrix} x \ y \ z \end{pmatrix} : x + y = 0\right}$
> 
> $$W^\perp = \text{span}\left{\begin{pmatrix} 1 \ -1 \ 0 \end{pmatrix}, \begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix}\right}$$
> 
> **Verificación:** $\dim(W) + \dim(W^\perp) = 1 + 2 = 3 = \dim(\mathbb{R}^3)$ ✓
> 
> ---
> 
> **11)** Fórmula de Grassmann (Sketch)
> 
> **Idea:** Considera la función:
> 
> $$f: W_1 \times W_2 \to W_1 + W_2, \quad f(\vec{w}_1, \vec{w}_2) = \vec{w}_1 + \vec{w}_2$$
> 
> - $f$ es sobreyectiva
> - El núcleo de $f$ está relacionado con $W_1 \cap W_2$
> - Por el teorema de dimensión: $\dim(\text{dom}) = \dim(\text{img}) + \dim(\ker)$
> 
> **Resultado:**
> 
> $$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Subespacios
> 
> ✅ **Definición básica:**
> 
> - Un subespacio es un subconjunto que es también un espacio vectorial
> - Debe contener $\vec{0}$, ser cerrado bajo suma y multiplicación escalar
> 
> ✅ **Interpretación geométrica:**
> 
> - En $\mathbb{R}^n$: siempre pasan por el origen
> - Pueden ser puntos, rectas, planos, hiperplanos...
> 
> ✅ **Span:**
> 
> - $\text{span}{\vec{v}_1, \ldots, \vec{v}_k}$ es siempre un subespacio
> - Es el subespacio más pequeño que contiene a los vectores
> 
> ---
> 
> ### Sobre Operaciones
> 
> ✅ **Intersección:**
> 
> - $W_1 \cap W_2$ siempre es subespacio
> - Se puede intersectar cualquier cantidad de subespacios
> 
> ✅ **Unión:**
> 
> - $W_1 \cup W_2$ generalmente NO es subespacio
> 
> ✅ **Suma:**
> 
> - $W_1 + W_2$ siempre es subespacio
> - Es el subespacio más pequeño que contiene a $W_1$ y $W_2$
> 
> ✅ **Suma directa:**
> 
> - $V = W_1 \oplus W_2$ significa descomposición única
> - Requiere $W_1 \cap W_2 = {\vec{0}}$
> 
> ---
> 
> ### Advertencias Importantes
> 
> ⚠️ **NO son subespacios:**
> 
> - Conjuntos que no contienen $\vec{0}$
> - Conjuntos acotados (esferas, bolas, cubos...)
> - Unión de subespacios (en general)
> - Conjuntos definidos por desigualdades estrictas
> 
> ⚠️ **Confusiones comunes:**
> 
> - Subconjunto ≠ Subespacio
> - Pasar por el origen ≠ Ser subespacio (necesario pero no suficiente)
> - Contener vectores ≠ Ser cerrado bajo combinaciones lineales

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema es prerequisito para:**
> 
> - [[08 - Independencia Lineal]] - Vectores que no son combinación lineal de otros
> - [[09 - Bases y Dimensión]] - Conjuntos generadores linealmente independientes
> - [[10 - Transformaciones Lineales]] - Núcleo e imagen son subespacios
> - [[11 - Espacios con Producto Interno]] - Subespacios ortogonales
> - [[12 - Diagonalización]] - Espacios propios son subespacios
> - [[13 - Teorema Espectral]] - Descomposición en subespacios ortogonales
> 
> **Conceptos relacionados:**
> 
> - **Espacios Vectoriales** - Estructura general que contiene subespacios
> - **Combinaciones Lineales** - Generan subespacios (span)
> - **Sistemas de Ecuaciones** - Conjunto solución puede ser subespacio
> - **Dimensión** - Mide el "tamaño" del subespacio
> - **Rango y Nulidad** - Dimensiones de subespacios especiales
> 
> **Siguiente tema recomendado:** [[08 - Independencia Lineal y Bases]]

---

## 📝 Notas Finales

> [!note]- 🎯 Reflexiones sobre Subespacios Vectoriales
> 
> ### Importancia Conceptual
> 
> Los subespacios son fundamentales porque:
> 
> - **Simplifican problemas:** Descomponer espacios grandes en partes manejables
> - **Revelan estructura:** Muestran la "arquitectura interna" de espacios vectoriales
> - **Conectan álgebra y geometría:** Une intuición geométrica con manipulación algebraica
> - **Base de la teoría:** Casi todos los conceptos avanzados involucran subespacios
> 
> ---
> 
> ### Perspectiva Geométrica
> 
> **En $\mathbb{R}^2$ y $\mathbb{R}^3$:**
> 
> - Los subespacios son "espacios planos" que pasan por el origen
> - Rectas, planos, hiperplanos...
> - La condición "pasar por el origen" es esencial
> 
> **Intuición:** Si puedes "escalar" y "sumar" vectores sin salir del conjunto, es subespacio.
> 
> ---
> 
> ### Perspectiva Algebraica
> 
> **Los subespacios capturan:**
> 
> - Soluciones de sistemas homogéneos: $A\vec{x} = \vec{0}$
> - Espacios de funciones con propiedades especiales
> - Estructuras invariantes bajo transformaciones
> 
> **Regla de oro:** Un subespacio es "cerrado" bajo las operaciones del espacio vectorial.
> 
> ---
> 
> ### Patrones Comunes
> 
> **Subespacios típicos:**
> 
> 1. **Por ecuaciones:** ${\vec{x} : A\vec{x} = \vec{0}}$
>     - Intersección de hiperplanos por el origen
>     - Siempre es subespacio
> 2. **Por generadores:** $\text{span}{\vec{v}_1, \ldots, \vec{v}_k}$
>     - Combinaciones lineales de vectores dados
>     - Siempre es subespacio
> 3. **Por propiedades:** ${f : f \text{ satisface propiedad } P}$
>     - Verificar caso por caso si es subespacio
> 
> ---
> 
> ### Para Profundizar
> 
> **Conceptos avanzados relacionados:**
> 
> - **Retículos de subespacios:** Estructura ordenada de todos los subespacios
> - **Grassmannianas:** Espacios de todos los subespacios de dimensión $k$
> - **Álgebra multilineal:** Productos tensoriales de subespacios
> - **Teoría de representaciones:** Subespacios invariantes
> - **Geometría algebraica:** Variedades lineales
> 
> **Aplicaciones avanzadas:**
> 
> - **Mecánica cuántica:** Espacios de estados, observables
> - **Teoría de códigos:** Códigos lineales como subespacios
> - **Análisis funcional:** Subespacios de dimensión infinita
> - **Teoría de control:** Espacios controlables/observables
> - **Compresión:** PCA encuentra subespacios de menor dimensión

---

## 🧮 Fórmulas de Referencia Rápida

> [!note]- 📋 Tabla de Referencia: Propiedades de Subespacios
> 
> ### Definición
> 
> |Propiedad|Fórmula/Condición|
> |---|---|
> |Vector cero|$\vec{0} \in W$|
> |Cerradura suma|$\vec{u}, \vec{v} \in W \Rightarrow \vec{u}+\vec{v} \in W$|
> |Cerradura escalar|$\vec{v} \in W, c \in \mathbb{F} \Rightarrow c\vec{v} \in W$|
> |Criterio compacto|$c\vec{u} + \vec{v} \in W$ para todo $\vec{u}, \vec{v} \in W$, $c \in \mathbb{F}$|
> 
> ---
> 
> ### Operaciones
> 
> |Operación|Resultado|Es subespacio|
> |---|---|---|
> |Intersección|$W_1 \cap W_2$|✅ Siempre|
> |Unión|$W_1 \cup W_2$|❌ En general no|
> |Suma|$W_1 + W_2$|✅ Siempre|
> |Suma directa|$W_1 \oplus W_2$|✅ Si $W_1 \cap W_2 = {\vec{0}}$|
> 
> ---
> 
> ### Dimensión (adelanto)
> 
> |Fórmula|Nombre|
> |---|---|
> |$\dim({\vec{0}}) = 0$|Subespacio trivial|
> |$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$|Fórmula de Grassmann|
> |$V = W_1 \oplus W_2 \Rightarrow \dim(V) = \dim(W_1) + \dim(W_2)$|Suma directa|
> |$\dim(W) \leq \dim(V)$ si $W \leq V$|Monotonía|
> 
> ---
> 
> ### Subespacios en $\mathbb{R}^n$
> 
> |Dimensión|Nombre|Ejemplos en $\mathbb{R}^3$|
> |---|---|---|
> |0|Punto|${\vec{0}}$|
> |1|Recta|$\text{span}{\vec{v}}$|
> |2|Plano|$\text{span}{\vec{v}_1, \vec{v}_2}$|
> |$n-1$|Hiperplano|${\vec{x} : \vec{a} \cdot \vec{x} = 0}$|
> |$n$|Espacio completo|$\mathbb{R}^n$|

---

## 💡 Trucos y Técnicas Útiles

> [!tip]- 🎯 Estrategias para Trabajar con Subespacios
> 
> ### Truco 1: Verificación del Vector Cero Primero
> 
> **Siempre verifica primero si $\vec{0} \in W$**
> 
> - Es la verificación más rápida
> - Si falla, ya sabes que NO es subespacio
> - Ahorra tiempo en problemas de examen
> 
> **Ejemplos rápidos:**
> 
> - ${(x,y) : x+y = 1}$ → $(0,0)$ no satisface → ✗ NO es subespacio
> - ${(x,y) : x+y = 0}$ → $(0,0)$ satisface → ✓ Continúa verificando
> 
> ---
> 
> ### Truco 2: Usar Span para Caracterizar
> 
> Si puedes escribir $W$ como span de vectores, **automáticamente** es subespacio.
> 
> **Ejemplo:** En lugar de verificar las 3 condiciones para: $$W = {(x, 2x, 3x) : x \in \mathbb{R}}$$
> 
> Reconoce que: $$W = \text{span}\left{\begin{pmatrix} 1 \ 2 \ 3 \end{pmatrix}\right}$$
> 
> Por lo tanto es subespacio ✓
> 
> ---
> 
> ### Truco 3: Contraejemplos para Descartar
> 
> Para demostrar que algo NO es subespacio, **basta un contraejemplo**.
> 
> **Estrategia:** Busca vectores "simples" y verifica si la suma o múltiplos están en $W$.
> 
> **Ejemplo:** $W = {(x,y) : xy = 0}$
> 
> - $(1,0) \in W$ ✓
> - $(0,1) \in W$ ✓
> - $(1,0) + (0,1) = (1,1)$ pero $1 \cdot 1 \neq 0$ ✗
> 
> ---
> 
> ### Truco 4: Ecuaciones Homogéneas
> 
> **Regla general:** Si $W$ está definido por ecuaciones **lineales homogéneas**, es subespacio.
> 
> **Homogénea:** Sin término constante (igualdad a cero)
> 
> ✅ $ax + by + cz = 0$ → Subespacio ❌ $ax + by + cz = d$ (con $d \neq 0$) → NO es subespacio
> 
> **Razón:** Las ecuaciones homogéneas preservan el cero y son cerradas bajo combinaciones lineales.
> 
> ---
> 
> ### Truco 5: Visualización en Dimensiones Bajas
> 
> Para desarrollar intuición, **visualiza en $\mathbb{R}^2$ o $\mathbb{R}^3$**:
> 
> - ¿Pasa por el origen? Si no, NO es subespacio
> - ¿Es "plano" (lineal)? Si es curvo, NO es subespacio
> - ¿Si escalas/sumas vectores, sigues dentro? Debe ser cerrado
> 
> ---
> 
> ### Truco 6: Propiedades de Funciones
> 
> Para subespacios de funciones, verifica si la propiedad es **lineal**:
> 
> ✅ "Funciones con $f(0) = 0$" → Lineal → Subespacio ✅ "Funciones pares" → Lineal → Subespacio ❌ "Funciones con $f(0) = 1$" → No lineal → NO es subespacio ❌ "Funciones positivas" → No lineal → NO es subespacio
> 
> **Test rápido:** Si $f$ y $g$ tienen la propiedad, ¿la tiene $cf + g$?

---

## 🎨 Visualización Avanzada

> [!note]- 🖼️ Galería de Subespacios
> 
> ### En $\mathbb{R}^2$
> 
> ```
> Subespacio trivial {0}:
> 
>       y
>       |
>       |
>       |
>   ----â€¢---- x
>       |
>       |
> 
> Solo el origen
> ```
> 
> ```
> Recta por el origen:
> 
>       y
>       |  /
>       | /  â† W = span{v}
>       |/
>   ----â€¢---- x
>      /|
>     / |
> 
> Dimensión 1
> ```
> 
> ```
> Todo R²:
> 
>       y
>     â€¢ | â€¢
>    â€¢  |  â€¢
>   ----+---- x
>    â€¢  |  â€¢
>     â€¢ | â€¢
> 
> W = R² completo
> Dimensión 2
> ```
> 
> ---
> 
> ### Suma de Subespacios en $\mathbb{R}^3$
> 
> ```
> W₁ + W₂ (recta + recta = plano):
> 
>         z
>         |
>         |  Plano W₁+W₂
>         | /â•±
>         |/â•±
>   ------+------ y
>        /|
>       / |W₁
>      /  |
>     x   W₂
> 
> Si W₁ y W₂ no son colineales
> ```
> 
> ```
> Intersección de planos (recta):
> 
>         z
>         |
>      P₁ |\ /P₂
>         | X  â† P₁ ∩ P₂ = recta
>         |/ \
>   ------+------ y
>        /|
>       / |
>      x
> 
> Dos planos se intersectan en una recta
> ```
> 
> ---
> 
> ### Suma Directa Visual
> 
> ```
> R³ = W₁ ⊕ W₂:
> 
>         z (W₂)
>         |
>         |
>         |
>         |
>   ------â€¢------ y
>        / â•²â•² (W₁ = plano xy)
>       /   â•²â•²
>      x     â•²â•²
> 
> W₁ ∩ W₂ = {0}
> W₁ + W₂ = R³
> ```

---

## 🔬 Casos Especiales y Patológicos

> [!warning]- ⚠️ Ejemplos Sutiles y Tramposos
> 
> ### Caso 1: Producto de Coordenadas
> 
> $$W = {(x, y) \in \mathbb{R}^2 : xy = 0}$$
> 
> **Descripción:** Unión de los ejes coordenados
> 
> **Análisis:**
> 
> - $(1, 0) \in W$ (eje $x$)
> - $(0, 1) \in W$ (eje $y$)
> - Pero $(1,0) + (0,1) = (1,1)$ y $1 \cdot 1 = 1 \neq 0$
> 
> $$\boxed{\text{NO es subespacio}}$$
> 
> **Lección:** Unión de subespacios NO es subespacio (en general)
> 
> ---
> 
> ### Caso 2: Norma Constante
> 
> $$W = {(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1}$$
> 
> **Descripción:** Círculo unitario
> 
> **Análisis:**
> 
> - $(1, 0) \in W$ ✓
> - $2(1, 0) = (2, 0)$ pero $4 + 0 = 4 \neq 1$ ✗
> 
> $$\boxed{\text{NO es subespacio (no cerrado bajo multiplicación)}}$$
> 
> **Lección:** Conjuntos curvos o acotados no son subespacios
> 
> ---
> 
> ### Caso 3: Matrices Invertibles
> 
> $$W = {A \in M_{n×n} : \det(A) \neq 0}$$
> 
> **Análisis:**
> 
> - La matriz cero NO es invertible
> - $\vec{0} \notin W$ ✗
> 
> $$\boxed{\text{NO es subespacio}}$$
> 
> Además, suma de matrices invertibles no siempre es invertible.
> 
> ---
> 
> ### Caso 4: Polinomios con Raíz Específica (no en origen)
> 
> $$W = {p(x) \in P_n : p(1) = 0}$$
> 
> **Análisis:**
> 
> 1. El polinomio cero satisface $p(1) = 0$ ✓
> 2. Si $p(1) = 0$ y $q(1) = 0$: $(p+q)(1) = p(1) + q(1) = 0$ ✓
> 3. Si $p(1) = 0$: $(cp)(1) = c \cdot p(1) = 0$ ✓
> 
> $$\boxed{\text{SÍ es subespacio}}$$
> 
> **Lección:** Condiciones sobre valores de funciones pueden dar subespacios si son "lineales"
> 
> ---
> 
> ### Caso 5: Rango Fijo
> 
> $$W = {A \in M_{n×n} : \text{rango}(A) = k}$$
> 
> **Para $k > 0$:**
> 
> - La matriz cero tiene rango 0, no $k$
> - $\vec{0} \notin W$ ✗
> 
> **Para $k = 0$:**
> 
> - Solo la matriz cero tiene rango 0
> - $W = {\vec{0}}$ ✓ (subespacio trivial)
> 
> $$\boxed{\text{Subespacio solo si } k = 0}$$
> 
> ---
> 
> ### Caso 6: Funciones Acotadas
> 
> $$W = {f : \mathbb{R} \to \mathbb{R} : |f(x)| \leq 1 \text{ para todo } x}$$
> 
> **Análisis:**
> 
> - $f(x) = 1$ satisface $|f(x)| = 1 \leq 1$ ✓
> - $2f(x) = 2$ pero $|2| = 2 > 1$ ✗
> 
> $$\boxed{\text{NO es subespacio}}$$

---

## 🎓 Problemas Tipo Examen

> [!example]- 📝 Problemas Conceptuales
> 
> **Problema 1:** Verdadero o Falso (justificar)
> 
> a) Todo subconjunto de un espacio vectorial que contiene el vector cero es un subespacio.
> 
> b) La intersección de dos subespacios es siempre un subespacio.
> 
> c) La unión de dos subespacios es siempre un subespacio.
> 
> d) Si $W_1 \subseteq W_2$ son subespacios, entonces $\dim(W_1) \leq \dim(W_2)$.
> 
> e) El span de cualquier conjunto de vectores contiene el vector cero.
> 
> f) Si $W$ no contiene el vector cero, entonces $W$ no es un subespacio.
> 
> g) Todo subespacio de $\mathbb{R}^3$ es un punto, recta, plano, o todo $\mathbb{R}^3$.
> 
> h) Si $\dim(W_1) = \dim(W_2)$, entonces $W_1 = W_2$.
> 
> ---
> 
> **Problema 2:** Elección Múltiple
> 
> ¿Cuál de los siguientes NO es un subespacio de $\mathbb{R}^3$?
> 
> A) ${(x, y, z) : x + y + z = 0}$
> 
> B) ${(x, y, z) : x = 2y}$
> 
> C) ${(x, y, z) : xyz = 0}$
> 
> D) ${(x, 0, z) : x, z \in \mathbb{R}}$
> 
> ---
> 
> **Problema 3:** Demostración
> 
> Demuestra que si $W_1$ y $W_2$ son subespacios de $V$ con $W_1 \cup W_2$ también subespacio, entonces $W_1 \subseteq W_2$ o $W_2 \subseteq W_1$.
> 
> **Hint:** Usa contradicción. Supón que existen $\vec{w}_1 \in W_1 \setminus W_2$ y $\vec{w}_2 \in W_2 \setminus W_1$.

> [!example]- 📝 Problemas de Cálculo
> 
> **Problema 4:** Encontrar intersección y suma
> 
> Dados los subespacios de $\mathbb{R}^4$:
> 
> $$W_1 = \left{\begin{pmatrix} x \ y \ 0 \ 0 \end{pmatrix} : x, y \in \mathbb{R}\right}$$
> 
> $$W_2 = \left{\begin{pmatrix} x \ x \ z \ 0 \end{pmatrix} : x, z \in \mathbb{R}\right}$$
> 
> Encuentra: a) $W_1 \cap W_2$ b) $W_1 + W_2$ c) ¿Es $W_1 + W_2$ suma directa?
> 
> ---
> 
> **Problema 5:** Complemento
> 
> Sea $W = \text{span}\left{\begin{pmatrix} 1 \ 1 \ 1 \end{pmatrix}\right}$ en $\mathbb{R}^3$.
> 
> a) Encuentra un subespacio $U$ tal que $\mathbb{R}^3 = W \oplus U$
> 
> b) ¿Es $U$ único? Si no, encuentra otro.
> 
> ---
> 
> **Problema 6:** Verificación algebraica
> 
> Sea $W = {A \in M_{3×3} : A^T = A \text{ y } \text{tr}(A) = 0}$
> 
> a) Demuestra que $W$ es un subespacio de $M_{3×3}$
> 
> b) Encuentra una base para $W$ y su dimensión

---

## ✨ Aplicaciones Prácticas

> [!note]- 🌍 Aplicaciones Reales de Subespacios
> 
> ### 1. Compresión de Datos (PCA)
> 
> **Problema:** Datos de alta dimensión (muchas variables)
> 
> **Solución:** Encontrar subespacio de menor dimensión que "capture" la mayor variación
> 
> **Ejemplo:** Imágenes de 1000×1000 píxeles ($10^6$ dimensiones) pueden estar "casi" en un subespacio de 100 dimensiones
> 
> ---
> 
> ### 2. Sistemas de Ecuaciones
> 
> **Ecuación homogénea:** $A\vec{x} = \vec{0}$
> 
> El conjunto solución es un subespacio (el núcleo de $A$)
> 
> **Aplicación:** Encontrar "grados de libertad" en un sistema
> 
> ---
> 
> ### 3. Mecánica Cuántica
> 
> **Estados cuánticos:** Vectores en espacios de Hilbert
> 
> **Observables:** Subespacios asociados a valores propios
> 
> **Medición:** Proyección sobre subespacios
> 
> ---
> 
> ### 4. Teoría de Códigos
> 
> **Códigos lineales:** Subespacios de $\mathbb{F}_2^n$ (vectores binarios)
> 
> **Corrección de errores:** Distancia entre subespacios
> 
> **Ejemplo:** Código de Hamming usa subespacios de dimensión 4 en $\mathbb{F}_2^7$
> 
> ---
> 
> ### 5. Procesamiento de Señales
> 
> **Señales:** Funciones en espacios de dimensión infinita
> 
> **Filtros:** Proyección sobre subespacios de frecuencias
> 
> **Fourier:** Descomposición en subespacios de diferentes frecuencias
> 
> ---
> 
> ### 6. Aprendizaje Automático
> 
> **Espacios de características:** Datos viven en subespacios
> 
> **Clasificación:** Separar datos encontrando subespacios
> 
> **Reducción de dimensionalidad:** t-SNE, UMAP encuentran subespacios de menor dimensión

---

## 🎯 Resumen Ejecutivo

> [!note]- 📌 Lo Más Importante en Una Página
> 
> ### Definición Core
> 
> $W \leq V$ si:
> 
> 1. $\vec{0} \in W$
> 2. $\vec{u} + \vec{v} \in W$ para todo $\vec{u}, \vec{v} \in W$
> 3. $c\vec{v} \in W$ para todo $\vec{v} \in W$, $c \in \mathbb{F}$
> 
> **O equivalentemente:** $c\vec{u} + \vec{v} \in W$ para todo $\vec{u}, \vec{v} \in W$, $c \in \mathbb{F}$
> 
> ---
> 
> ### Ejemplos Prototípicos
> 
> |Espacio|Subespacios|Dimensión|
> |---|---|---|
> |$\mathbb{R}^2$|${\vec{0}}$, rectas por origen, $\mathbb{R}^2$|0, 1, 2|
> |$\mathbb{R}^3$|${\vec{0}}$, rectas, planos, $\mathbb{R}^3$|0, 1, 2, 3|
> |$M_{n×n}$|Simétricas, antisimétricas, diagonales...|varía|
> |$P_n$|Pares, impares, con $p(a)=0$...|varía|
> 
> ---
> 
> ### Operaciones
> 
> - **Intersección:** $W_1 \cap W_2$ siempre es subespacio ✓
> - **Unión:** $W_1 \cup W_2$ generalmente NO es subespacio ✗
> - **Suma:** $W_1 + W_2$ siempre es subespacio ✓
> - **Span:** $\text{span}{S}$ siempre es subespacio ✓
> 
> ---
> 
> ### Criterios Rápidos
> 
> **ES subespacio si:**
> 
> - Definido por ecuaciones lineales homogéneas
> - Es el span de algunos vectores
> - Es núcleo o imagen de transformación lineal
> 
> **NO es subespacio si:**
> 
> - No contiene $\vec{0}$
> - Definido por desigualdades o ecuaciones no lineales
> - Es acotado (excepto ${\vec{0}}$)
> 
> ---
> 
> ### Fórmulas Clave
> 
> $$\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)$$
> 
> $$V = W_1 \oplus W_2 \iff W_1 + W_2 = V \text{ y } W_1 \cap W_2 = {\vec{0}}$$

---

**Fin del documento 07 – Subespacios Vectoriales**

---

**Tags:** #algebra-lineal #subespacios-vectoriales #espacios-vectoriales #span #suma-directa #interseccion #generadores #algebra-abstracta #geometria-lineal
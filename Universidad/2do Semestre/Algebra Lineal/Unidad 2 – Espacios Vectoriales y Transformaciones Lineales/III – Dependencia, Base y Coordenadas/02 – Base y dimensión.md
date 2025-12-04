# 📘 Base y Dimensión

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Bases y la Dimensión?
> 
> Hemos visto que algunos vectores son redundantes (dependencia lineal) y que otros son esenciales (independencia lineal). Ahora surge una pregunta fundamental: **¿Cuál es el conjunto "perfecto" de vectores para representar un espacio?**
> 
> **Motivación:**
> 
> - Queremos el conjunto **mínimo** que genera todo el espacio
> - Pero también queremos que sea **máximo** en independencia
> - Este conjunto ideal se llama **base**
> - El número de elementos en la base se llama **dimensión**
> 
> **Analogías:**
> 
> - **Sistema de coordenadas:** Los ejes X, Y, Z forman una base para el espacio 3D
> - **Receta fundamental:** Ingredientes básicos que permiten hacer cualquier plato
> - **ADN:** Información mínima necesaria para reconstruir todo el organismo
> - **Colores primarios:** RGB o CMYK como bases para generar todos los colores
> - **Alfabeto:** Letras básicas que generan todas las palabras posibles
> 
> **Preguntas fundamentales:**
> 
> - ¿Cuántos vectores necesito para generar un espacio?
> - ¿Cuál es el conjunto óptimo de vectores generadores?
> - ¿Todos los conjuntos generadores mínimos tienen el mismo tamaño?
> - ¿Cómo medir el "tamaño" de un espacio vectorial?
> 
> **Aplicaciones prácticas:**
> 
> - **Sistemas de coordenadas:** Definir sistemas de referencia
> - **Compresión de datos:** Representación óptima
> - **Machine Learning:** Reducción de dimensionalidad (PCA)
> - **Gráficos computacionales:** Sistemas de coordenadas personalizados
> - **Análisis de datos:** Identificar dimensiones importantes
> - **Física:** Bases ortonormales en mecánica cuántica

---

## 📐 Definición de Base

### 🔑 Definición Formal

> [!example]- 🟢 Definición: Base de un Espacio Vectorial
> 
> **Definición:** Un conjunto de vectores $\mathcal{B} = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ es una **base** de un espacio vectorial $V$ si cumple **ambas** condiciones:
> 
> 1. **Genera el espacio:** $\text{span}(\mathcal{B}) = V$
> 2. **Es linealmente independiente:** Los vectores de $\mathcal{B}$ son linealmente independientes
> 
> $$\mathcal{B} \text{ es base de } V \iff \begin{cases} \text{span}(\mathcal{B}) = V \ \mathcal{B} \text{ es linealmente independiente} \end{cases}$$
> 
> ---
> 
> **En otras palabras:**
> 
> - Una base es un conjunto generador **mínimo**
> - Una base es un conjunto independiente **máximo**
> - Cada vector del espacio se expresa de **manera única** como combinación lineal de la base
> - La base es el "alfabeto" del espacio vectorial
> 
> ---
> 
> **Interpretación crucial:**
> 
> - **Generador mínimo:** Si quitas cualquier vector, ya no genera todo $V$
> - **Independiente máximo:** Si agregas cualquier vector de $V$, se vuelve dependiente
> - **Representación óptima:** Ni sobran ni faltan vectores
> 
> ---
> 
> **Observaciones importantes:**
> 
> 1. Todo espacio vectorial (excepto ${\vec{0}}$) tiene al menos una base
> 2. Un mismo espacio puede tener **muchas bases diferentes**
> 3. **Todas las bases del mismo espacio tienen el mismo número de vectores**
> 4. Este número común se llama **dimensión** del espacio

### 🎨 Caracterizaciones Equivalentes de Base

> [!note]- 🔄 Definiciones Equivalentes
> 
> Las siguientes afirmaciones son **equivalentes** para un conjunto $\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_n}$ en un espacio vectorial $V$:
> 
> ### (1) Definición Estándar
> 
> $\mathcal{B}$ genera $V$ y es linealmente independiente
> 
> ---
> 
> ### (2) Conjunto Generador Mínimo
> 
> $\mathcal{B}$ genera $V$, pero si se elimina cualquier vector, deja de generar $V$
> 
> $$\text{span}(\mathcal{B}) = V \quad \text{y} \quad \text{span}(\mathcal{B} \setminus {\vec{v}_i}) \neq V \quad \forall i$$
> 
> ---
> 
> ### (3) Conjunto Independiente Maximal
> 
> $\mathcal{B}$ es linealmente independiente, pero agregar cualquier vector de $V$ lo hace dependiente
> 
> $$\mathcal{B} \text{ independiente} \quad \text{y} \quad \mathcal{B} \cup {\vec{w}} \text{ dependiente} \quad \forall \vec{w} \in V \setminus \mathcal{B}$$
> 
> ---
> 
> ### (4) Representación Única
> 
> Todo vector de $V$ se puede expresar de **manera única** como combinación lineal de vectores en $\mathcal{B}$
> 
> $$\forall \vec{v} \in V, \exists! \text{ escalares } c_1, \ldots, c_n : \vec{v} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$$
> 
> ---
> 
> ### (5) Propiedad de Extensión-Reducción
> 
> - Todo conjunto linealmente independiente en $V$ puede **extenderse** a una base
> - Todo conjunto que genera $V$ puede **reducirse** a una base
> 
> **Interpretación:** La base es el "punto de equilibrio" entre generar e independencia.

---

## 🌟 Ejemplos Fundamentales de Bases

### Base Canónica de ℝⁿ

> [!example]- 📍 La Base Estándar
> 
> **Definición:** La **base canónica** (o estándar) de $\mathbb{R}^n$ es:
> 
> $$\mathcal{E} = {\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n}$$
> 
> donde:
> 
> $$\vec{e}_1 = \begin{bmatrix} 1 \ 0 \ 0 \ \vdots \ 0 \end{bmatrix}, \quad \vec{e}_2 = \begin{bmatrix} 0 \ 1 \ 0 \ \vdots \ 0 \end{bmatrix}, \quad \ldots, \quad \vec{e}_n = \begin{bmatrix} 0 \ 0 \ 0 \ \vdots \ 1 \end{bmatrix}$$
> 
> ---
> 
> ### Para ℝ²
> 
> $$\mathcal{E}_2 = \left\{ \vec{e}_1 = \begin{bmatrix} 1 \ 0 \end{bmatrix}, \vec{e}_2 = \begin{bmatrix} 0 \ 1 \end{bmatrix} \right\}$$
> 
> **Visualización:**
> 
> ```
>       y
>       |
>     1 |  e₂
>       |  ↑
>       |  
>     0 +-----→--- x
>       0  1  e₁
> 
>     Base canónica de ℝ²
> ```
> 
> **Verificación de que es base:**
> 
> 1. **Genera ℝ²:** Cualquier vector $\begin{bmatrix} x \ y \end{bmatrix} = x\vec{e}_1 + y\vec{e}_2$ ✓
>     
> 2. **Independiente:** $c_1\vec{e}_1 + c_2\vec{e}_2 = \vec{0} \Rightarrow c_1 = c_2 = 0$ ✓
>     
> 
> ---
> 
> ### Para ℝ³
> 
> $$\mathcal{E}_3 = \left\{ \vec{e}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \vec{e}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \vec{e}_3 = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} \right\}$$
> 
> **Visualización:**
> 
> ```
>         z
>         | e₃
>         ↑
>         |
>         +-------→--- y
>        /|      e₂
>       // |
>      ↓  |
>     x   
>     e₁
> 
>     Base canónica de ℝ³
> ```
> 
> **Propiedades especiales:**
> 
> - Los vectores son **ortogonales** entre sí
> - Cada vector tiene **longitud 1** (ortonormales)
> - Corresponden a los ejes coordenados
> - Forman un **sistema de coordenadas cartesianas**

### Otras Bases de ℝⁿ

> [!example]- 🔄 Bases Alternativas
> 
> **Ejemplo 1: Base alternativa de ℝ²**
> 
> $$\mathcal{B} = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 1 \ -1 \end{bmatrix} \right\}$$
> 
> **Verificación:**
> 
> **1. Independencia:** Por determinante
> 
> $$\det\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} = -1 - 1 = -2 \neq 0$$ ✓
> 
> **2. Genera ℝ²:** Como tiene 2 vectores independientes en ℝ², genera todo el espacio ✓
> 
> **Visualización:**
> 
> ```
>       y
>       |
>     2 |  v₁
>       | ↗
>     1 |
>       |    
>     0 +------------- x
>       |     ↘ v₂
>    -1 |
> 
>     Base rotada 45°
> ```
> 
> **Representación de vectores:**
> 
> Para expresar $\begin{bmatrix} 3 \ 1 \end{bmatrix}$ en esta base:
> 
> $$\begin{bmatrix} 3 \ 1 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \ -1 \end{bmatrix}$$
> 
> Resolviendo: $c_1 = 2, c_2 = 1$
> 
> $$\begin{bmatrix} 3 \ 1 \end{bmatrix} = 2\begin{bmatrix} 1 \ 1 \end{bmatrix} + 1\begin{bmatrix} 1 \ -1 \end{bmatrix}$$
> 
> ---
> 
> **Ejemplo 2: Base de ℝ³**
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} \right\}$$
> 
> **Verificación por determinante:**
> 
> $$\det\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{bmatrix} = 1(0-1) - 0 + 1(0-1) = -2 \neq 0$$ ✓
> 
> Como el determinante es no nulo, los vectores son independientes. Como son 3 vectores independientes en ℝ³, forman una base.

### Base de Polinomios

> [!example]- 📈 Base Canónica de Pₙ
> 
> **Base estándar de polinomios de grado ≤ n:**
> 
> $$\mathcal{B} = {1, x, x^2, x^3, \ldots, x^n}$$
> 
> ---
> 
> ### Para P₂ (polinomios de grado ≤ 2)
> 
> $$\mathcal{B} = {1, x, x^2}$$
> 
> **Verificación:**
> 
> **1. Genera P₂:** Todo polinomio $p(x) = a_0 + a_1x + a_2x^2$ es combinación lineal:
> 
> $$p(x) = a_0 \cdot 1 + a_1 \cdot x + a_2 \cdot x^2$$ ✓
> 
> **2. Independiente:** Si $c_0 \cdot 1 + c_1 \cdot x + c_2 \cdot x^2 = 0$ (polinomio cero)
> 
> Entonces todos los coeficientes deben ser cero: $c_0 = c_1 = c_2 = 0$ ✓
> 
> ---
> 
> ### Bases alternativas de P₂
> 
> **Base de Lagrange (puntos x = 0, 1, 2):**
> 
> $$\mathcal{B} = {L_0(x), L_1(x), L_2(x)}$$
> 
> donde:
> 
> - $L_0(x) = \frac{(x-1)(x-2)}{(0-1)(0-2)} = \frac{(x-1)(x-2)}{2}$
> - $L_1(x) = \frac{x(x-2)}{(1-0)(1-2)} = -x(x-2)$
> - $L_2(x) = \frac{x(x-1)}{(2-0)(2-1)} = \frac{x(x-1)}{2}$
> 
> **Propiedad especial:** $L_i(j) = \delta_{ij}$ (1 si $i=j$, 0 si no)
> 
> ---
> 
> **Base de potencias desplazadas:**
> 
> $$\mathcal{B} = {1, (x-1), (x-1)^2}$$
> 
> Esta base es útil para aproximaciones cerca de $x = 1$.

### Base de Matrices

> [!example]- 📊 Base Canónica de M₂ₓ₂
> 
> **Base estándar de matrices 2×2:**
> 
> $$\mathcal{B} = \left\{ E_{11} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, E_{12} = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, E_{21} = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}, E_{22} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \right\}$$
> 
> **Verificación:**
> 
> **1. Genera M₂ₓ₂:** Toda matriz se puede escribir como:
> 
> $$\begin{bmatrix} a & b \\ c & d \end{bmatrix} = a \cdot E_{11} + b \cdot E_{12} + c \cdot E_{21} + d \cdot E_{22}$$ ✓
> 
> **2. Independiente:** Si
> 
> $$c_1 E_{11} + c_2 E_{12} + c_3 E_{21} + c_4 E_{22} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$
> 
> entonces:
> 
> $$\begin{bmatrix} c_1 & c_2 \\ c_3 & c_4 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$
> 
> Por tanto: $c_1 = c_2 = c_3 = c_4 = 0$ ✓
> 
> ---
> 
> **Base alternativa (matrices simétricas 2×2):**
> 
> Las matrices simétricas tienen la forma $\begin{bmatrix} a & b \\ b & c \end{bmatrix}$
> 
> Una base es:
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \right\}$$
> 
> **Nota:** El espacio de matrices simétricas 2×2 tiene dimensión 3 (no 4).

---

## 📏 Definición de Dimensión

### 🔑 Concepto de Dimensión

> [!example]- 🟢 Definición: Dimensión de un Espacio Vectorial
> 
> **Definición:** La **dimensión** de un espacio vectorial $V$, denotada $\dim(V)$, es el **número de vectores en cualquier base** de $V$.
> 
> $$\dim(V) = |\mathcal{B}| \text{ donde } \mathcal{B} \text{ es cualquier base de } V$$
> 
> ---
> 
> **Teorema Fundamental:**
> 
> **Todas las bases de un mismo espacio vectorial tienen el mismo número de elementos.**
> 
> Este teorema garantiza que la dimensión está bien definida: no depende de qué base elijas.
> 
> ---
> 
> **Casos especiales:**
> 
> - $\dim({\vec{0}}) = 0$ (el espacio trivial tiene dimensión 0)
> - Si $V$ no puede generarse por un conjunto finito, decimos que $V$ tiene **dimensión infinita**
> 
> ---
> 
> **Interpretación:**
> 
> - La dimensión mide el "tamaño" del espacio vectorial
> - Es el número de "grados de libertad"
> - Es el número mínimo de coordenadas necesarias
> - Es el número de "direcciones independientes"
> 
> ---
> 
> **Observaciones importantes:**
> 
> 1. La dimensión es un **invariante** del espacio (no cambia con la base)
> 2. Espacios de diferente dimensión nunca pueden ser isomorfos
> 3. La dimensión determina completamente la estructura de espacios vectoriales de dimensión finita

### 📊 Dimensiones de Espacios Comunes

> [!note]- 📐 Tabla de Dimensiones
> 
> |Espacio Vectorial|Base|Dimensión|
> |---|---|---|
> |${\vec{0}}$|$\emptyset$|0|
> |$\mathbb{R}^n$|${\vec{e}_1, \ldots, \vec{e}_n}$|$n$|
> |$\mathbb{R}^2$|$\left\{\begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix}\right\}$|2|
> |$\mathbb{R}^3$|$\left\{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\}$|3|
> |$P_n$ (polinomios grado ≤ n)|${1, x, x^2, \ldots, x^n}$|$n + 1$|
> |$P_2$|${1, x, x^2}$|3|
> |$M_{m \times n}$ (matrices)|${E_{ij}}$|$m \cdot n$|
> |$M_{2 \times 2}$|${E_{11}, E_{12}, E_{21}, E_{22}}$|4|
> |$M_{3 \times 3}$|${E_{ij} : 1 \leq i,j \leq 3}$|9|
> |Matrices simétricas $n \times n$|-|$\frac{n(n+1)}{2}$|
> |Matrices antisimétricas $n \times n$|-|$\frac{n(n-1)}{2}$|
> |Matrices diagonales $n \times n$|-|$n$|
> |Matrices triangulares sup. $n \times n$|-|$\frac{n(n+1)}{2}$|
> 
> ---
> 
> **Ejemplos detallados:**
> 
> ### ℝ²
> 
> $$\dim(\mathbb{R}^2) = 2$$
> 
> Necesitas 2 vectores independientes para generar el plano.
> 
> ### P₃
> 
> $$\dim(P_3) = 4$$
> 
> Base: ${1, x, x^2, x^3}$ - necesitas 4 monomios.
> 
> ### M₂ₓ₃
> 
> $$\dim(M_{2 \times 3}) = 2 \times 3 = 6$$
> 
> Una matriz $2 \times 3$ tiene 6 entradas independientes.
> 
> ### Matrices simétricas 3×3
> 
> $$\dim(\text{Sim}_3) = \frac{3(3+1)}{2} = 6$$
> 
> Forma: $\begin{bmatrix} a & b & c \\ b & d & e \\ c & e & f \end{bmatrix}$ - 6 parámetros independientes.

---

## 🎯 Teoremas Fundamentales sobre Bases y Dimensión

### Teorema: Existencia y Unicidad de la Dimensión

> [!note]- ⭐ Teorema Principal
> 
> **Teorema de la Dimensión:**
> 
> Sea $V$ un espacio vectorial de dimensión finita. Entonces:
> 
> 1. **Existencia:** $V$ tiene al menos una base
> 2. **Invarianza:** Todas las bases de $V$ tienen el **mismo número** de elementos
> 3. **Este número se llama dimensión:** $\dim(V)$
> 
> ---
> 
> **Demostración (sketch):**
> 
> **Parte 1 (Existencia):**
> 
> - Si $V = {\vec{0}}$, entonces $\emptyset$ es base y $\dim(V) = 0$
> - Si $V \neq {\vec{0}}$, toma $\vec{v}_1 \neq \vec{0}$
> - Si $\text{span}(\vec{v}_1) = V$, terminamos
> - Si no, existe $\vec{v}_2 \notin \text{span}(\vec{v}_1)$
> - Continúa hasta obtener un conjunto maximal independiente
> - Este conjunto es una base ✓
> 
> **Parte 2 (Invarianza):**
> 
> - Supón $\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_n}$ y $\mathcal{C} = {\vec{w}_1, \ldots, \vec{w}_m}$ son bases
> - Como $\mathcal{B}$ es independiente y $\mathcal{C}$ genera, se puede demostrar que $n \leq m$
> - Por simetría, $m \leq n$
> - Por tanto, $n = m$ ✓

### Teorema: Caracterizaciones de Bases

> [!note]- 🔄 Criterios para Identificar Bases
> 
> **Teorema:** Sea $V$ un espacio vectorial con $\dim(V) = n$, y sea $S = {\vec{v}_1, \ldots, \vec{v}_k}$ un conjunto de vectores en $V$.
> 
> Las siguientes afirmaciones son **equivalentes**:
> 
> ### (1) S es una base de V
> 
> ---
> 
> ### (2) S es independiente y |S| = n
> 
> $$S \text{ linealmente independiente} \quad \text{y} \quad |S| = \dim(V)$$
> 
> **Conclusión:** Un conjunto independiente con el número correcto de vectores es automáticamente una base.
> 
> ---
> 
> ### (3) S genera V y |S| = n
> 
> $$\text{span}(S) = V \quad \text{y} \quad |S| = \dim(V)$$
> 
> **Conclusión:** Un conjunto generador con el número correcto de vectores es automáticamente una base.
> 
> ---
> 
> **Consecuencias prácticas:**
> 
> **Para verificar que S es base de ℝⁿ:**
> 
> - **Opción 1:** Mostrar que $S$ tiene $n$ vectores independientes
> - **Opción 2:** Mostrar que $S$ tiene $n$ vectores que generan $\mathbb{R}^n$
> - **Opción 3:** Verificar ambas propiedades (método completo)
> 
> **Ejemplo en ℝ³:**
> 
> Si tienes 3 vectores independientes en ℝ³, automáticamente generan todo ℝ³ (son base).
> 
> Si tienes 3 vectores que generan ℝ³, automáticamente son independientes (son base).

### Teorema: Extensión y Reducción

> [!note]- 🔧 Construcción de Bases
> 
> **Teorema de Extensión:**
> 
> Sea $V$ un espacio vectorial con $\dim(V) = n$. Si $S = {\vec{v}_1, \ldots, \vec{v}_k}$ es un conjunto **linealmente independiente** con $k < n$, entonces $S$ puede **extenderse** a una base de $V$.
> 
> $$S \subseteq \mathcal{B} \text{ donde } \mathcal{B} \text{ es base de } V$$
> 
> **En otras palabras:** Siempre puedes agregar vectores hasta completar una base.
> 
> ---
> 
> **Teorema de Reducción:**
> 
> Si $S = {\vec{v}_1, \ldots, \vec{v}_m}$ **genera** $V$ con $m > n = \dim(V)$, entonces podemos **eliminar** vectores de $S$ para obtener una base de $V$.
> 
> $$\mathcal{B} \subseteq S \text{ donde } \mathcal{B} \text{ es base de } V$$
> 
> **En otras palabras:** Siempre puedes quitar vectores redundantes para obtener una base.
> 
> ---
> 
> **Procedimiento de extensión:**
> 
> 1. Partir con conjunto independiente $S = {\vec{v}_1, \ldots, \vec{v}_k}$
> 2. Si $\text{span}(S) = V$, terminamos (ya es base)
> 3. Si no, existe $\vec{w} \in V \setminus \text{span}(S)$
> 4. Agregar $\vec{w}$ a $S$: ahora $S \cup {\vec{w}}$ es independiente
> 5. Repetir hasta tener $n$ vectores
> 
> ---
> 
> **Procedimiento de reducción:**
> 
> 6. Partir con conjunto generador $S = {\vec{v}_1, \ldots, \vec{v}_m}$
> 7. Formar matriz con vectores como columnas
> 8. Reducir a forma escalonada
> 9. Seleccionar vectores correspondientes a columnas pivote
> 10. Estos forman una base

### Teorema: Desigualdades Fundamentales

> [!note]- 📊 Relaciones entre Tamaño y Dimensión
> 
> **Teorema:** Sea $V$ un espacio vectorial con $\dim(V) = n$.
> 
> ### (1) Conjunto Independiente
> 
> Si $S$ es linealmente independiente, entonces:
> 
> $$|S| \leq n$$
> 
> **Interpretación:** No puedes tener más de $n$ vectores independientes en un espacio de dimensión $n$.
> **Corolario:** Si $|S| > n$, entonces $S$ es automáticamente dependiente.
> 
> ---
> 
> ### (2) Conjunto Generador
> 
> Si $\text{span}(S) = V$, entonces:
> 
> $$|S| \geq n$$
> 
> **Interpretación:** Necesitas al menos $n$ vectores para generar un espacio de dimensión $n$.
> 
> **Corolario:** Si $|S| < n$, entonces $S$ no puede generar todo $V$.
> 
> ---
> 
> ### (3) Base = Igualdad
> 
> $S$ es base de $V$ si y solo si:
> 
> $$S \text{ es independiente y } |S| = n$$
> 
> o equivalentemente:
> 
> $$S \text{ genera } V \text{ y } |S| = n$$
> 
> ---
> 
> **Tabla resumen:**
> 
> |Propiedad|Tamaño|Conclusión|
> |---|---|---|
> |Independiente|$\|S\| < n$|Puede extenderse a base|
> |Independiente|$\|S\| = n$|**Es base**|
> |Independiente|$\|S\| > n$|**Imposible**|
> |Generador|$\|S\| < n$|**Imposible**|
> |Generador|$\|S\| = n$|**Es base**|
> |Generador|$\|S\| > n$|Puede reducirse a base|

---

## 🔍 Métodos para Encontrar Bases

### Método 1: A partir de Conjunto Generador

> [!note]- 🎯 Reducir Generadores a Base
> 
> **Objetivo:** Dado un conjunto generador $S$, encontrar una base contenida en $S$.
> 
> ---
> 
> **Algoritmo (Método de Columnas Pivote):**
> 
> **Paso 1:** Formar matriz $A$ con los vectores como **columnas**
> 
> $$A = [\ \vec{v}_1 \ | \ \vec{v}_2 \ | \ \cdots \ | \ \vec{v}_k \ ]$$
> 
> **Paso 2:** Reducir $A$ a forma escalonada reducida (RREF)
> 
> **Paso 3:** Identificar las **columnas pivote** en RREF
> 
> **Paso 4:** Tomar los vectores **originales** correspondientes a las columnas pivote
> 
> **Estos vectores forman una base** del espacio generado por $S$.
> 
> ---
> 
> **Ejemplo:** Encontrar base de $\text{span}(S)$ donde:
> 
> $$S = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 2 \ 4 \ 6 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}, \vec{v}_4 = \begin{bmatrix} 3 \ 5 \ 8 \end{bmatrix} \right\}$$
> 
> **Paso 1:** Formar matriz
> 
> $$A = \begin{bmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 1 & 5 \\ 3 & 6 & 2 & 8 \end{bmatrix}$$
> 
> **Paso 2:** Reducir a RREF
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 2 & 0 & 2 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Paso 3:** Columnas pivote: **1 y 3**
> 
> **Paso 4:** Base de $\text{span}(S)$:
> 
> $$\mathcal{B} = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix} \right\}$$
> 
> **Verificación:**
> 
> - $\vec{v}_2 = 2\vec{v}_1$ (redundante)
> - $\vec{v}_4 = 2\vec{v}_1 + \vec{v}_3$ (combinación de la base)
> 
> $$\boxed{\dim(\text{span}(S)) = 2}$$

### Método 2: Extender Conjunto Independiente

> [!note]- 🔧 Completar a Base
> 
> **Objetivo:** Dado un conjunto independiente $S$ en $\mathbb{R}^n$, extenderlo a una base de $\mathbb{R}^n$.
> 
> ---
> 
> **Algoritmo:**
> 
> **Paso 1:** Partir con $S = {\vec{v}_1, \ldots, \vec{v}_k}$ linealmente independiente
> 
> **Paso 2:** Agregar vectores de la base canónica: ${\vec{v}_1, \ldots, \vec{v}_k, \vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n}$
> 
> **Paso 3:** Aplicar el método de reducción (columnas pivote) a este conjunto ampliado
> 
> **Paso 4:** Los vectores correspondientes a columnas pivote forman una base que **contiene** $S$
> 
> ---
> 
> **Ejemplo:** Extender a base de ℝ³
> 
> $$S = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} \right\}$$
> 
> **Paso 1:** $S$ es independiente (un vector no nulo)
> 
> **Paso 2:** Agregar base canónica
> 
> $$T = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} \right\}$$
> 
> **Paso 3:** Formar matriz y reducir
> 
> $$A = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{bmatrix}$$
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$
> 
> **Paso 4:** Columnas pivote: 1, 2, 3
> 
> **Base extendida:**
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} \right\}$$
> 
> ✓ Contiene $\vec{v}_1$ original
> 
> ✓ Tiene 3 vectores independientes en ℝ³ → es base

### Método 3: Base de Subespacio Definido por Ecuaciones

> [!note]- 📐 Subespacios Implícitos
> 
> **Objetivo:** Encontrar una base para el subespacio $W$ definido por ecuaciones lineales.
> 
> ---
> 
> **Procedimiento:**
> 
> **Paso 1:** Escribir el sistema de ecuaciones en forma matricial
> 
> **Paso 2:** Resolver el sistema homogéneo (encontrar espacio nulo)
> 
> **Paso 3:** Expresar la solución en forma paramétrica
> 
> **Paso 4:** Los vectores que multiplican a los parámetros forman una base
> 
> ---
> 
> **Ejemplo:** Encontrar base de $W$ definido por:
> 
> $$W = \left\{ \begin{bmatrix} x \ y \ z \end{bmatrix} \in \mathbb{R}^3 : x + 2y + z = 0 \right\}$$
> 
> **Paso 1:** Sistema homogéneo
> 
> $$x + 2y + z = 0$$
> 
> **Paso 2:** Resolver
> 
> $$x = -2y - z$$
> 
> **Paso 3:** Forma paramétrica (con $y = s$, $z = t$)
> 
> $$\begin{bmatrix} x \ y \ z \end{bmatrix} = \begin{bmatrix} -2y - z \ y \ z \end{bmatrix} = \begin{bmatrix} -2s - t \ s \ t \end{bmatrix} = s\begin{bmatrix} -2 \ 1 \ 0 \end{bmatrix} + t\begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix}$$
> 
> **Paso 4:** Base de $W$
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} -2 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix} \right\}$$
> 
> $$\boxed{\dim(W) = 2}$$
> 
> **Interpretación geométrica:** $W$ es un plano que pasa por el origen en ℝ³.
> 
> ---
> 
> **Ejemplo 2:** Subespacio con dos ecuaciones
> 
> $$W = \left\{ \begin{bmatrix} x \ y \ z \ w \end{bmatrix} \in \mathbb{R}^4 : \begin{cases} x + y + z + w = 0 \ x - y + 2z = 0 \end{cases} \right\}$$
> 
> **Matriz aumentada:**
> 
> $$\left[\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 0 \\ 1 & -1 & 2 & 0 & 0 \end{array}\right]$$
> 
> **Reducir:**
> 
> $$\left[\begin{array}{cccc|c} 1 & 0 & \frac{3}{2} & \frac{1}{2} & 0 \ 0 & 1 & -\frac{1}{2} & \frac{1}{2} & 0 \end{array}\right]$$
> 
> **Variables libres:** $z = s$, $w = t$
> 
> **Solución:**
> 
> $$\begin{bmatrix} x \ y \ z \ w \end{bmatrix} = s\begin{bmatrix} -3/2 \ 1/2 \ 1 \ 0 \end{bmatrix} + t\begin{bmatrix} -1/2 \ -1/2 \ 0 \ 1 \end{bmatrix}$$
> 
> **Base:**
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} -3 \ 1 \ 2 \ 0 \end{bmatrix}, \begin{bmatrix} -1 \ -1 \ 0 \ 2 \end{bmatrix} \right\}$$
> 
> (Multiplicados por 2 para eliminar fracciones)
> 
> $$\boxed{\dim(W) = 2}$$

### Método 4: Base de Espacio Columna

> [!note]- 📊 Base de Col(A)
> 
> **Objetivo:** Encontrar una base para el espacio columna de una matriz $A$.
> 
> ---
> 
> **Método de Columnas Pivote:**
> 
> **Paso 1:** Reducir $A$ a forma escalonada (REF o RREF)
> 
> **Paso 2:** Identificar posiciones de pivotes
> 
> **Paso 3:** Las columnas de $A$ **original** en posiciones pivote forman una base de $\text{Col}(A)$
> 
> **⚠️ IMPORTANTE:** Tomar columnas de $A$ original, no de RREF
> 
> ---
> 
> **Ejemplo:**
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 7 & 10 \\ 3 & 6 & 10 & 13 \end{bmatrix}$$
> 
> **Paso 1:** Reducir
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 2 & 0 & -1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Paso 2:** Pivotes en columnas 1 y 3
> 
> **Paso 3:** Base de $\text{Col}(A)$ (de $A$ original):
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 3 \ 7 \ 10 \end{bmatrix} \right\}$$
> 
> $$\boxed{\dim(\text{Col}(A)) = 2 = \text{rango}(A)}$$
> 
> **Observación clave:** $\dim(\text{Col}(A)) = \text{rango}(A) = $ número de pivotes

---

## 📚 Ejemplos Detallados

### Ejemplo 1: Verificar que un Conjunto es Base

> [!example]- 📝 Verificación Completa
> 
> **Dado:** ¿Es $\mathcal{B}$ una base de ℝ³?
> 
> $$\mathcal{B} = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix} \right\}$$
> 
> ---
> 
> **Solución:**
> 
> **Método 1: Verificar independencia (determinante)**
> 
> $$A = \begin{bmatrix} 1 & 1 & 2 \\ 1 & 2 & 3 \\ 1 & 3 & 4 \end{bmatrix}$$
> 
> $$\det(A) = 1 \cdot \det\begin{bmatrix} 2 & 3 \\ 3 & 4 \end{bmatrix} - 1 \cdot \det\begin{bmatrix} 1 & 3 \\ 1 & 4 \end{bmatrix} + 2 \cdot \det\begin{bmatrix} 1 & 2 \\ 1 & 3 \end{bmatrix}$$
> 
> $$= 1(8-9) - 1(4-3) + 2(3-2) = -1 - 1 + 2 = 0$$
> 
> **Conclusión:** $\det(A) = 0$ → Los vectores son **dependientes**
> 
> $$\boxed{\text{NO es base}}$$
> 
> ---
> 
> **Verificación adicional:** Encontrar relación de dependencia
> 
> Plantear: $c_1\vec{v}_1 + c_2\vec{v}_2 + c_3\vec{v}_3 = \vec{0}$
> 
> Sistema: $$\begin{cases} c_1 + c_2 + 2c_3 = 0 \\ c_1 + 2c_2 + 3c_3 = 0 \\ c_1 + 3c_2 + 4c_3 = 0 \end{cases}$$
> 
> Resolviendo: $(c_1, c_2, c_3) = t(1, -2, 1)$ para cualquier $t \neq 0$
> 
> **Relación:** $\vec{v}_1 - 2\vec{v}_2 + \vec{v}_3 = \vec{0}$
> 
> **Interpretación:** $\vec{v}_3 = 2\vec{v}_2 - \vec{v}_1$ (redundante)

### Ejemplo 2: Encontrar Dimensión de Subespacio Generado

> [!example]- 📏 Calcular Dimensión
> 
> **Dado:** Encontrar $\dim(\text{span}(S))$ donde:
> 
> $$S = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 1 \ 2 \ 1 \end{bmatrix} \right\}$$
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Formar matriz con vectores como columnas
> 
> $$A = \begin{bmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \end{bmatrix}$$
> 
> **Paso 2:** Reducir a forma escalonada
> 
> $R_3 - R_1$:
> 
> $$\begin{bmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 \end{bmatrix}$$
> 
> $R_4 - R_2$:
> 
> $$\begin{bmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Paso 3:** Contar pivotes: **2 pivotes** (columnas 1 y 2)
> 
> $$\boxed{\dim(\text{span}(S)) = 2}$$
> 
> **Base de span(S):**
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix} \right\}$$
> 
> **Relaciones:**
> 
> - $\vec{v}_3 = \vec{v}_1 + \vec{v}_2$
> - $\vec{v}_4 = 2\vec{v}_1 + \vec{v}_2$

### Ejemplo 3: Base de Polinomios con Restricciones

> [!example]- 📈 Subespacio de P₃
> 
> **Dado:** Encontrar una base para el subespacio $W$ de $P_3$ donde:
> 
> $$W = {p(x) \in P_3 : p(1) = 0}$$
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Caracterizar el subespacio
> 
> Sea $p(x) = a_0 + a_1x + a_2x^2 + a_3x^3$
> 
> Condición: $p(1) = 0$
> 
> $$a_0 + a_1 + a_2 + a_3 = 0$$
> 
> **Paso 2:** Resolver para $a_0$
> 
> $$a_0 = -a_1 - a_2 - a_3$$
> 
> **Paso 3:** Expresar $p(x)$
> 
> $$p(x) = (-a_1 - a_2 - a_3) + a_1x + a_2x^2 + a_3x^3$$
> 
> $$= a_1(-1 + x) + a_2(-1 + x^2) + a_3(-1 + x^3)$$
> 
> **Paso 4:** Base de $W$
> 
> $$\mathcal{B} = {-1 + x, \ -1 + x^2, \ -1 + x^3}$$
> 
> o equivalentemente:
> 
> $$\mathcal{B} = {x - 1, \ x^2 - 1, \ x^3 - 1}$$
> 
> $$\boxed{\dim(W) = 3}$$
> 
> **Verificación:**
> 
> - $(x-1)|_{x=1} = 0$ ✓
> - $(x^2-1)|_{x=1} = 0$ ✓
> - $(x^3-1)|_{x=1} = 0$ ✓
> - Son linealmente independientes ✓

### Ejemplo 4: Base de Matrices Simétricas

> [!example]- 📊 Subespacio de M₃ₓ₃
> 
> **Dado:** Encontrar una base y la dimensión del espacio de matrices simétricas $3 \times 3$.
> 
> $$\text{Sim}_3 = \left\{ A \in M_{3 \times 3} : A^T = A \right\}$$
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Forma general de matriz simétrica
> 
> $$A = \begin{bmatrix} a & b & c \\ b & d & e \\ c & e & f \end{bmatrix}$$
> 
> **Observación:** 6 parámetros independientes: $a, b, c, d, e, f$
> 
> **Paso 2:** Expresar como combinación lineal
> 
> $$A = a\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} + b\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} + c\begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix}$$
> 
> $$+ d\begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix} + e\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} + f\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
> 
> **Paso 3:** Base de $\text{Sim}_3$
> 
> $$\mathcal{B} = \left\{ E_{11}, E_{12}+E_{21}, E_{13}+E_{31}, E_{22}, E_{23}+E_{32}, E_{33} \right\}$$
> 
> Explícitamente:
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \right\}$$
> 
> $$\boxed{\dim(\text{Sim}_3) = 6 = \frac{3(3+1)}{2}}$$
> 
> **Fórmula general:** $\dim(\text{Sim}_n) = \frac{n(n+1)}{2}$

### Ejemplo 5: Extender a Base de ℝ⁴

> [!example]- 🔧 Extensión de Conjunto Independiente
> 
> **Dado:** Extender a una base de ℝ⁴:
> 
> $$S = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 0 \ 1 \ 1 \ 1 \end{bmatrix} \right\}$$
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Verificar que $S$ es independiente
> 
> Los vectores claramente no son proporcionales → independientes ✓
> 
> **Paso 2:** Agregar vectores canónicos
> 
> $$T = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 0 \ 1 \end{bmatrix} \right\}$$
> 
> **Paso 3:** Formar matriz y reducir
> 
> $$A = \begin{bmatrix} 1 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 & 0 & 1 \end{bmatrix}$$
> 
> Reduciendo:
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 0 & 0 & 0 & -1 & 0 \\ 0 & 1 & 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & -1 \end{bmatrix}$$
> 
> **Paso 4:** Pivotes en columnas 1, 2, 3, 4
> 
> **Base extendida:**
> 
> $$\mathcal{B} = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \
0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 0 \end{bmatrix} \right\}$$
> ✓ Contiene los dos vectores originales
> 
> ✓ Tiene 4 vectores independientes en ℝ⁴
> 
> $$\boxed{\text{Base de } \mathbb{R}^4}$$

---

## 🧮 Propiedades Importantes de Bases y Dimensión

### Propiedades Fundamentales

> [!note]- ⭐ Propiedades Esenciales
> 
> ### Propiedad 1: Invariancia de la Dimensión
> 
> **Teorema:** Si $\mathcal{B}_1$ y $\mathcal{B}_2$ son bases de $V$, entonces:
> 
> $$|\mathcal{B}_1| = |\mathcal{B}_2|$$
> 
> **Interpretación:** La dimensión no depende de la base elegida.
> 
> ---
> 
> ### Propiedad 2: Dimensión de Subespacios
> 
> **Teorema:** Si $W$ es un subespacio de $V$, entonces:
> 
> $$\dim(W) \leq \dim(V)$$
> 
> **Igualdad** si y solo si $W = V$.
> 
> **Corolario:** Un subespacio propio tiene dimensión estrictamente menor.
> 
> ---
> 
> ### Propiedad 3: Unicidad de Representación
> 
> **Teorema:** Si $\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_n}$ es base de $V$, entonces **todo** vector $\vec{w} \in V$ se puede escribir de **manera única** como:
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n$$
> 
> Los escalares $c_1, \ldots, c_n$ se llaman **coordenadas** de $\vec{w}$ respecto a $\mathcal{B}$.
> 
> **Notación:** $[\vec{w}]_{\mathcal{B}} = \begin{bmatrix} c_1 \ c_2 \ \vdots \ c_n \end{bmatrix}$
> 
> ---
> 
> ### Propiedad 4: Dimensión del Espacio Nulo
> 
> **Teorema (Adelanto del Teorema del Rango):** Para una matriz $A$ de $m \times n$:
> 
> $$\dim(\text{Nul}(A)) + \dim(\text{Col}(A)) = n$$
> 
> o equivalentemente:
> 
> $$\text{nulidad}(A) + \text{rango}(A) = n$$
> 
> **Interpretación:** Las dimensiones del espacio nulo y columna suman el número de columnas.
> 
> ---
> 
> ### Propiedad 5: Dimensión de ℝⁿ
> 
> $$\dim(\mathbb{R}^n) = n$$
> 
> **Consecuencias:**
> 
> - Cualquier conjunto de $n$ vectores independientes en ℝⁿ es base
> - Cualquier conjunto de $n$ vectores que genera ℝⁿ es base
> - No puede haber más de $n$ vectores independientes en ℝⁿ

### Teorema del Rango (Adelanto)

> [!note]- 📊 Relación Fundamental
> 
> **Teorema del Rango (Rank-Nullity Theorem):**
> 
> Sea $A$ una matriz $m \times n$. Entonces:
> 
> $$\text{rango}(A) + \text{nulidad}(A) = n$$
> 
> donde:
> 
> - $\text{rango}(A) = \dim(\text{Col}(A))$ = número de columnas pivote
> - $\text{nulidad}(A) = \dim(\text{Nul}(A))$ = número de variables libres
> 
> ---
> 
> **Interpretación:**
> 
> Para una matriz $n \times n$:
> 
> $$\begin{array}{|c|c|c|} \hline \text{Rango} & \text{Nulidad} & \text{Interpretación} \\ \hline n & 0 & \text{Invertible, det} \neq 0 \\ < n & > 0 & \text{Singular, det} = 0 \\ \hline \end{array}$$
> 
> ---
> 
> **Ejemplo:**
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 7 & 10 \\ 3 & 6 & 10 & 13 \end{bmatrix}$$
> 
> Vimos anteriormente que $\text{rango}(A) = 2$
> 
> Por el teorema del rango:
> 
> $$\text{nulidad}(A) = 4 - 2 = 2$$
> 
> Esto significa que el espacio nulo tiene dimensión 2 (hay 2 variables libres).

### Relaciones entre Subespacios

> [!note]- 🔗 Dimensiones de Suma e Intersección
> 
> **Teorema de la Dimensión (Suma e Intersección):**
> 
> Si $U$ y $W$ son subespacios de $V$, entonces:
> 
> $$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$$
> 
> donde $U + W = {\vec{u} + \vec{w} : \vec{u} \in U, \vec{w} \in W}$
> 
> ---
> 
> **Analogía:** Como el principio de inclusión-exclusión en teoría de conjuntos:
> 
> $$|A \cup B| = |A| + |B| - |A \cap B|$$
> 
> ---
> 
> **Casos especiales:**
> 
> ### Suma Directa
> 
> Si $U \cap W = {\vec{0}}$, entonces:
> 
> $$\dim(U \oplus W) = \dim(U) + \dim(W)$$
> 
> Notación: $U \oplus W$ (suma directa)
> 
> **Ejemplo:** En ℝ³, si $U$ es el plano $xy$ y $W$ es el eje $z$:
> 
> - $\dim(U) = 2$
> - $\dim(W) = 1$
> - $U \cap W = {\vec{0}}$
> - $\dim(U \oplus W) = 2 + 1 = 3 = \dim(\mathbb{R}^3)$
> 
> ---
> 
> **Ejemplo numérico:**
> 
> En ℝ³, sean:
> 
> $$U = \text{span}\left\{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}\right\} \quad (\text{plano } xy)$$
> 
> $$W = \text{span}\left\{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}\right\} \quad (\text{recta en plano } xy)$$
> 
> Entonces:
> 
> - $\dim(U) = 2$
> - $\dim(W) = 1$
> - $U \cap W = W$ (la recta está contenida en el plano)
> - $\dim(U \cap W) = 1$
> 
> Por el teorema:
> 
> $$\dim(U + W) = 2 + 1 - 1 = 2$$
> 
> Es decir, $U + W = U$ (el plano)

---

## 🎨 Coordenadas Respecto a una Base

### Definición de Coordenadas

> [!example]- 📍 Vector de Coordenadas
> 
> **Definición:** Sea $\mathcal{B} = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ una base de $V$, y sea $\vec{w} \in V$.
> 
> Los **escalares únicos** $c_1, c_2, \ldots, c_n$ tales que:
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n$$
> 
> se llaman **coordenadas** de $\vec{w}$ respecto a la base $\mathcal{B}$.
> 
> **Notación:**
> 
> $$[\vec{w}]_{\mathcal{B}} = \begin{bmatrix} c_1 \ c_2 \ \vdots \ c_n \end{bmatrix}$$
> 
> ---
> 
> **Observaciones:**
> 
> 1. Las coordenadas son **únicas** (garantizado por independencia)
> 2. $[\vec{w}]_{\mathcal{B}}$ es un vector en ℝⁿ
> 3. Las coordenadas dependen de la base elegida
> 4. Para la base canónica: $[\vec{w}]_{\mathcal{E}} = \vec{w}$

### Ejemplo de Coordenadas

> [!example]- 📐 Cálculo de Coordenadas
> 
> **Dado:** En ℝ², sea la base:
> 
> $$\mathcal{B} = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 1 \ -1 \end{bmatrix} \right\}$$
> 
> Encontrar las coordenadas de $\vec{w} = \begin{bmatrix} 3 \ 1 \end{bmatrix}$ respecto a $\mathcal{B}$.
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Plantear la ecuación
> 
> $$\begin{bmatrix} 3 \ 1 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \ -1 \end{bmatrix}$$
> 
> **Paso 2:** Sistema de ecuaciones
> 
> $$\begin{cases} c_1 + c_2 = 3 \ c_1 - c_2 = 1 \end{cases}$$
> 
> **Paso 3:** Resolver
> 
> Sumando las ecuaciones: $2c_1 = 4 \Rightarrow c_1 = 2$
> 
> De la primera: $c_2 = 3 - 2 = 1$
> 
> **Paso 4:** Coordenadas
> 
> $$[\vec{w}]_{\mathcal{B}} = \begin{bmatrix} 2 \ 1 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$2\begin{bmatrix} 1 \ 1 \end{bmatrix} + 1\begin{bmatrix} 1 \ -1 \end{bmatrix} = \begin{bmatrix} 2+1 \ 2-1 \end{bmatrix} = \begin{bmatrix} 3 \ 1 \end{bmatrix}$$ ✓
> 
> ---
> 
> **Método matricial:**
> 
> Formar matriz con base como columnas:
> 
> $$P_{\mathcal{B}} = \begin{bmatrix} 1 & 1 \ 1 & -1 \end{bmatrix}$$
> 
> Resolver: $P_{\mathcal{B}}[\vec{w}]_{\mathcal{B}} = \vec{w}$
> 
> $$[\vec{w}]_{\mathcal{B}} = P_{\mathcal{B}}^{-1}\vec{w}$$

---

## 🎯 Algoritmos y Procedimientos

### Procedimiento Completo: Verificar si es Base

> [!note]- ✅ Checklist de Verificación
> 
> **Para verificar si $\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_k}$ es base de $V$ con $\dim(V) = n$:**
> 
> ---
> 
> ### Método 1: Verificación Completa (Ambas Propiedades)
> 
> **Paso 1:** Verificar independencia
> 
> - Plantear $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{0}$
> - Mostrar que solo $c_1 = \cdots = c_k = 0$ es solución
> 
> **Paso 2:** Verificar que genera $V$
> 
> - Mostrar que todo vector de $V$ es combinación lineal de $\mathcal{B}$
> 
> Si ambos se cumplen → **ES BASE** ✓
> 
> ---
> 
> ### Método 2: Contar + Una Propiedad (Más Eficiente)
> 
> **Opción A:** Si $k = n$ (tamaño correcto)
> 
> - Verificar **solo independencia**
> - Si es independiente → automáticamente genera $V$ → **ES BASE**
> 
> **Opción B:** Si $k = n$ (tamaño correcto)
> 
> - Verificar **solo que genera**
> - Si genera $V$ → automáticamente es independiente → **ES BASE**
> 
> **Opción C:** Si $k \neq n$
> 
> - **NO ES BASE** (tamaño incorrecto)
> 
> ---
> 
> ### Método 3: Determinante (Solo ℝⁿ, k = n)
> 
> **Para vectores en ℝⁿ:**
> 
> **Paso 1:** Formar matriz $A = [\ \vec{v}_1 \ | \ \cdots \ | \ \vec{v}_n \ ]$
> 
> **Paso 2:** Calcular $\det(A)$
> 
> **Paso 3:**
> 
> - Si $\det(A) \neq 0$ → **ES BASE**
> - Si $\det(A) = 0$ → **NO ES BASE**

### Procedimiento: Encontrar Base de Subespacio

> [!note]- 🔍 Guía Completa
> 
> **Dado:** Subespacio $W$ de $V$
> 
> **Objetivo:** Encontrar una base de $W$ y calcular $\dim(W)$
> 
> ---
> 
> ### Caso 1: W Definido por Generadores
> 
> **Dado:** $W = \text{span}(S)$ donde $S = {\vec{v}_1, \ldots, \vec{v}_k}$
> 
> **Procedimiento:**
> 
> 1. Formar matriz $A = [\ \vec{v}_1 \ | \ \cdots \ | \ \vec{v}_k \ ]$
> 2. Reducir a RREF
> 3. Columnas pivote de $A$ **original** forman base de $W$
> 4. $\dim(W) = $ número de pivotes
> 
> ---
> 
> ### Caso 2: W Definido por Ecuaciones
> 
> **Dado:** $W = {\vec{x} \in \mathbb{R}^n : A\vec{x} = \vec{0}}$ (espacio nulo)
> 
> **Procedimiento:**
> 
> 1. Resolver el sistema homogéneo $A\vec{x} = \vec{0}$
> 2. Expresar solución en forma paramétrica
> 3. Vectores que multiplican parámetros forman base
> 4. $\dim(W) = $ número de parámetros libres
> 
> ---
> 
> ### Caso 3: W es Espacio Columna
> 
> **Dado:** $W = \text{Col}(A)$
> 
> **Procedimiento:**
> 
> 1. Reducir $A$ a forma escalonada
> 2. Identificar columnas pivote
> 3. Columnas correspondientes de $A$ **original** forman base
> 4. $\dim(W) = \text{rango}(A)$
> 
> ---
> 
> ### Caso 4: W es Espacio Fila
> 
> **Dado:** $W = \text{Fila}(A)$
> 
> **Procedimiento:**
> 
> 1. Reducir $A$ a RREF
> 2. Filas **no nulas** de RREF forman base de $W$
> 3. $\dim(W) = \text{rango}(A) = $ número de filas no nulas

---

## 💡 Aplicaciones de Bases y Dimensión

### Aplicación 1: Sistemas de Coordenadas Personalizados

> [!example]- 🎯 Coordenadas en Diferentes Bases
> 
> **Problema:** En gráficos computacionales, a veces necesitamos sistemas de coordenadas no estándar.
> 
> **Ejemplo:** Base rotada 45° en ℝ²
> 
> $$\mathcal{B} = \left\{ \vec{v}_1 = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \ 1 \end{bmatrix}, \vec{v}_2 = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \ -1 \end{bmatrix} \right\}$$
> 
> **Ventaja:** Simplifica cálculos en direcciones específicas.
> 
> **Conversión:** Un punto $(x, y)$ en coordenadas estándar se expresa en la nueva base como:
> 
> $$[\vec{p}]_{\mathcal{B}} = \begin{bmatrix} \frac{x+y}{\sqrt{2}} \ \frac{x-y}{\sqrt{2}} \end{bmatrix}$$

### Aplicación 2: Compresión de Datos (PCA)

> [!example]- 📊 Reducción de Dimensionalidad
> 
> **Análisis de Componentes Principales (PCA):**
> 
> **Idea:** Encontrar una base donde:
> 
> - Los primeros vectores capturan la mayor varianza
> - Se pueden descartar últimos vectores (menor información)
> - Reducción de dimensión con mínima pérdida de información
> 
> **Proceso:**
> 
> 1. Datos originales en ℝⁿ
> 2. Encontrar base "óptima" (componentes principales)
> 3. Proyectar a subespacio de dimensión $k < n$
> 4. Retener $\frac{\text{varianza capturada}}{\text{varianza total}} \approx 95%$
> 
> **Ejemplo:** Imágenes de 1000×1000 píxeles (dimensión 1,000,000)
> 
> - Encontrar base donde 100 dimensiones capturan 95% de información
> - Reducción: $1{,}000{,}000 \to 100$ → compresión de $10{,}000:1$

### Aplicación 3: Bases Ortonormales en Física

> [!example]- ⚛️ Mecánica Cuántica
> 
> **Estados cuánticos:**
> 
> En mecánica cuántica, los estados se representan en espacios vectoriales complejos de dimensión infinita (espacios de Hilbert).
> 
> **Base de estados:**
> 
> Para un sistema de 2 niveles (qubit):
> 
> $$\mathcal{B} = {|0\rangle, |1\rangle}$$
> 
> donde $|0\rangle = \begin{bmatrix} 1 \ 0 \end{bmatrix}$ y $|1\rangle = \begin{bmatrix} 0 \ 1 \end{bmatrix}$
> 
> **Estado general:**
> 
> $$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$
> 
> donde $|\alpha|^2 + |\beta|^2 = 1$
> 
> **Las coordenadas** $[\alpha, \beta]$ determinan completamente el estado cuántico.

### Aplicación 4: Espacios de Soluciones

> [!example]- 🔧 Ingeniería y Física
> 
> **Ecuaciones diferenciales:**
> 
> El conjunto de soluciones de una ecuación diferencial lineal homogénea forma un espacio vectorial.
> 
> **Ejemplo:** $y'' - y = 0$
> 
> **Solución general:** $y(x) = c_1e^x + c_2e^{-x}$
> 
> **Base del espacio de soluciones:**
> 
> $$\mathcal{B} = {e^x, e^{-x}}$$
> 
> $$\boxed{\dim(\text{Espacio de soluciones}) = 2}$$
> 
> **Interpretación:** Necesitas 2 condiciones iniciales para determinar única solución.

---

## 📚 Ejercicios Propuestos

### Ejercicios Nivel Básico

> [!example]- 💪 Práctica Fundamental
> 
> **1. Verificar si es base de ℝ²:**
> 
> a) $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 4 \end{bmatrix}\right\}$
> 
> b) $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 2 \end{bmatrix}\right\}$
> 
> c) $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \end{bmatrix}\right\}$
> 
> ---
> 
> **2. Determinar dimensión:**
> 
> a) $W = \text{span}\left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 0 \ 2 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right\}$
> 
> b) $W = \left\{\begin{bmatrix} x \ y \ z \end{bmatrix} : x + y + z = 0\right\}$
> 
> c) Matrices diagonales $2 \times 2$
> 
> ---
> 
> **3. Encontrar coordenadas:**
> 
> En ℝ², sea $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ -1 \end{bmatrix}\right\}$
> 
> Encontrar $[\vec{v}]_{\mathcal{B}}$ para:
> 
> a) $\vec{v} = \begin{bmatrix} 5 \ 3 \end{bmatrix}$
> 
> b) $\vec{v} = \begin{bmatrix} 2 \ 0 \end{bmatrix}$
> 
> c) $\vec{v} = \begin{bmatrix} 0 \ 4 \end{bmatrix}$

### Ejercicios Nivel Intermedio

> [!example]- 💪 Desafío Moderado
> 
> **4. Bases de subespacios:**
> 
> a) Encontrar base y dimensión de:
> 
> $$W = \text{span}\left\{\begin{bmatrix} 1 \ 2 \ 3 \ 4 \end{bmatrix}, \begin{bmatrix} 2 \ 3 \ 4 \ 5 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 2 \ 3 \end{bmatrix}\right\}$$
> 
> b) Encontrar base del espacio nulo de:
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 7 & 10 \\ 0 & 0 & 1 & 2 \end{bmatrix}$$
> 
> c) Encontrar base del espacio columna de $A$ (mismo $A$)
> 
> ---
> 
> **5. Extender a base:**
> 
> Extender a base de ℝ³:
> 
> a) $S = \left\{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}\right\}$
> 
> b) $S = \left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right\}$
> 
> ---
> 
> **6. Polinomios:**
> 
> a) Encontrar base de ${p(x) \in P_3 : p(0) = 0}$
> 
> b) Encontrar base de ${p(x) \in P_3 : p(1) = p(-1)}$
> 
> c) ¿Cuál es la dimensión de ${p(x) \in P_n : p'(0) = 0}$?

### Ejercicios Nivel Avanzado

> [!example]- 💪 Desafío Avanzado
> 
> **7. Matrices especiales:**
> 
> Encontrar base y dimensión de:
> 
> a) Matrices antisimétricas $3 \times 3$ (donde $A^T = -A$)
> 
> b) Matrices que conmutan con $\begin{bmatrix} 1 & 1 \ 0 & 1 \end{bmatrix}$
> 
> c) Matrices $2 \times 2$ con traza cero
> 
> ---
> 
> **8. Suma e intersección:**
> 
> En ℝ³, sean:
> 
> $$U = \text{span}\left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right\}$$
> 
> $$W = \text{span}\left\{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}\right\}$$
> 
> a) Encontrar base de $U + W$
> 
> b) Encontrar base de $U \cap W$
> 
> c) Verificar: $\dim(U+W) = \dim(U) + \dim(W) - \dim(U \cap W)$
> 
> ---
> 
> **9. Cambio de base:**
> 
> En ℝ², sean las bases:
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 4 \end{bmatrix}\right\}, \quad \mathcal{C} = \left\{\begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix}\right\}$$
> 
> a) Si $[\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 2 \ 3 \end{bmatrix}$, encontrar $[\vec{v}]_{\mathcal{C}}$
> 
> b) Encontrar matriz de cambio de base $P_{\mathcal{C} \leftarrow \mathcal{B}}$
> 
> ---
> 
> **10. Demostrar:**
> 
> a) Si $\dim(V) = n$ y $S$ tiene $n$ vectores independientes, entonces $S$ es base
> 
> b) Si $W_1$ y $W_2$ son subespacios con $W_1 \cap W_2 = {\vec{0}}$ y $\dim(W_1) + \dim(W_2) = \dim(V)$, entonces $V = W_1 \oplus W_2$
> 
> c) Todo espacio vectorial de dimensión finita tiene una base

---

## ✅ Soluciones Selectas

### Soluciones Ejercicios Básicos

> [!success]- 🔑 Respuestas Nivel 1
> 
> **1a)** $\mathcal{B} = \left\{ \begin{bmatrix} 1 \\ 2 \end{bmatrix},\; \begin{bmatrix} 3 \\ 4 \end{bmatrix} \right\}$
> **Solución por determinante:**
> 
> $$\det\begin{bmatrix} 1 & 3 \ 2 & 4 \end{bmatrix} = (1)(4) - (3)(2) = 4 - 6 = -2 \neq 0$$
> 
> Como el determinante es no nulo y tenemos 2 vectores en ℝ²:
> 
> $$\boxed{\text{SÍ ES BASE}}$$
> 
> ---
> 
> **1b)** $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 2 \end{bmatrix}\right\}$
> 
> **Solución por inspección:**
> 
> $$\begin{bmatrix} 2 \ 2 \end{bmatrix} = 2\begin{bmatrix} 1 \ 1 \end{bmatrix}$$
> 
> Los vectores son **proporcionales** (dependientes).
> 
> $$\boxed{\text{NO ES BASE}}$$
> 
> ---
> 
> **1c)** $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \end{bmatrix}\right\}$
> 
> **Solución:**
> 
> Tenemos **3 vectores en ℝ²**.
> 
> Como $3 > 2 = \dim(\mathbb{R}^2)$, el conjunto tiene más vectores que la dimensión del espacio.
> 
> Por tanto, automáticamente son **dependientes**.
> 
> $$\boxed{\text{NO ES BASE}}$$
> 
> **Relación:** $\begin{bmatrix} 1 \ 1 \end{bmatrix} = \begin{bmatrix} 1 \ 0 \end{bmatrix} + \begin{bmatrix} 0 \ 1 \end{bmatrix}$
> 
> ---
> 
> **2a)** $W = \text{span}\left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 0 \ 2 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right\}$
> 
> **Observación:** $\begin{bmatrix} 2 \ 0 \ 2 \end{bmatrix} = 2\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$ (redundante)
> 
> **Base reducida:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right\}$$
> 
> Estos dos vectores son independientes (no proporcionales).
> 
> $$\boxed{\dim(W) = 2}$$
> 
> ---
> 
> **2b)** $W = \left\{\begin{bmatrix} x \ y \ z \end{bmatrix} : x + y + z = 0\right\}$
> 
> **Resolver:** $x = -y - z$
> 
> **Forma paramétrica:** Con $y = s$, $z = t$:
> 
> $$\begin{bmatrix} x \ y \ z \end{bmatrix} = \begin{bmatrix} -s-t \ s \ t \end{bmatrix} = s\begin{bmatrix} -1 \ 1 \ 0 \end{bmatrix} + t\begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix}$$
> 
> **Base:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} -1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(W) = 2}$$
> 
> ---
> 
> **2c)** Matrices diagonales $2 \times 2$
> 
> **Forma general:**
> 
> $$\begin{bmatrix} a & 0 \ 0 & b \end{bmatrix} = a\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix} + b\begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}$$
> 
> **Base:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(\text{Diag}_{2 \times 2}) = 2}$$
> 
> ---
> 
> **3a)** $\vec{v} = \begin{bmatrix} 5 \ 3 \end{bmatrix}$, base $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ -1 \end{bmatrix}\right\}$
> 
> **Plantear:** $\begin{bmatrix} 5 \ 3 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \ -1 \end{bmatrix}$
> 
> **Sistema:** $$\begin{cases} c_1 + c_2 = 5 \ c_1 - c_2 = 3 \end{cases}$$
> 
> **Resolver:**
> 
> - Sumando: $2c_1 = 8 \Rightarrow c_1 = 4$
> - De la primera: $c_2 = 1$
> 
> $$\boxed{[\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 4 \ 1 \end{bmatrix}}$$
> 
> ---
> 
> **3b)** $\vec{v} = \begin{bmatrix} 2 \ 0 \end{bmatrix}$
> 
> **Sistema:** $$\begin{cases} c_1 + c_2 = 2 \ c_1 - c_2 = 0 \end{cases}$$
> 
> **Resolver:**
> 
> - De la segunda: $c_1 = c_2$
> - En la primera: $2c_1 = 2 \Rightarrow c_1 = 1$
> - Entonces $c_2 = 1$
> 
> $$\boxed{[\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 1 \ 1 \end{bmatrix}}$$
> 
> ---
> 
> **3c)** $\vec{v} = \begin{bmatrix} 0 \ 4 \end{bmatrix}$
> 
> **Sistema:** $$\begin{cases} c_1 + c_2 = 0 \ c_1 - c_2 = 4 \end{cases}$$
> 
> **Resolver:**
> 
> - Sumando: $2c_1 = 4 \Rightarrow c_1 = 2$
> - De la primera: $c_2 = -2$
> 
> $$\boxed{[\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 2 \ -2 \end{bmatrix}}$$

### Soluciones Ejercicios Intermedios

> [!success]- 🔑 Respuestas Nivel 2
> 
> **4a)** Base de $W = \text{span}\left\{\begin{bmatrix} 1 \ 2 \ 3 \ 4 \end{bmatrix}, \begin{bmatrix} 2 \ 3 \ 4 \ 5 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 2 \ 3 \end{bmatrix}\right\}$
> 
> **Formar matriz:**
> 
> $$A = \begin{bmatrix} 1 & 2 & 0 \\ 2 & 3 & 1 \\ 3 & 4 & 2 \\ 4 & 5 & 3 \end{bmatrix}$$
> 
> **Reducir (por filas):**
> 
> $R_2 - 2R_1$, $R_3 - 3R_1$, $R_4 - 4R_1$:
> 
> $$\begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & -2 & 2 \\ 0 & -3 & 3 \end{bmatrix}$$
> 
> $R_3 - 2R_2$, $R_4 - 3R_2$:
> 
> $$\begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$
> 
> **Pivotes en columnas 1 y 2**
> 
> **Base de W:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 2 \ 3 \ 4 \end{bmatrix}, \begin{bmatrix} 2 \ 3 \ 4 \ 5 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(W) = 2}$$
> 
> **Relación:** $\begin{bmatrix} 0 \ 1 \ 2 \ 3 \end{bmatrix} = -\begin{bmatrix} 1 \ 2 \ 3 \ 4 \end{bmatrix} + \begin{bmatrix} 2 \ 3 \ 4 \ 5 \end{bmatrix}$
> 
> ---
> 
> **4b)** Base del espacio nulo de $A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 7 & 10 \\ 0 & 0 & 1 & 2 \end{bmatrix}$
> 
> **Resolver:** $A\vec{x} = \vec{0}$
> 
> **Matriz aumentada:**
> 
> $$\left[\begin{array}{cccc|c} 1 & 2 & 3 & 4 & 0 \\ 2 & 4 & 7 & 10 & 0 \\ 0 & 0 & 1 & 2 & 0 \end{array}\right]$$
> 
> **Reducir:**
> 
> $$\left[\begin{array}{cccc|c} 1 & 2 & 0 & -2 & 0 \\ 0 & 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
> 
> **Variables libres:** $x_2 = s$, $x_4 = t$
> 
> **De las ecuaciones:**
> 
> - $x_3 = -2t$
> - $x_1 = -2s + 2t$
> 
> **Solución:**
> 
> $$\vec{x} = \begin{bmatrix} -2s+2t \ s \ -2t \ t \end{bmatrix} = s\begin{bmatrix} -2 \ 1 \ 0 \ 0 \end{bmatrix} + t\begin{bmatrix} 2 \ 0 \ -2 \ 1 \end{bmatrix}$$
> 
> **Base de Nul(A):**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} -2 \ 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 2 \ 0 \ -2 \ 1 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(\text{Nul}(A)) = 2}$$
> 
> **Verificar Teorema del Rango:**
> 
> - $\text{rango}(A) = 2$ (2 pivotes)
> - $\text{nulidad}(A) = 2$
> - $2 + 2 = 4$ = número de columnas ✓
> 
> ---
> 
> **4c)** Base del espacio columna del mismo $A$
> 
> **De la RREF anterior, pivotes en columnas 1 y 3**
> 
> **Base de Col(A):** (columnas de $A$ **original**)
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 2 \ 0 \end{bmatrix}, \begin{bmatrix} 3 \ 7 \ 1 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(\text{Col}(A)) = 2}$$
> 
> ---
> 
> **5a)** Extender $S = \left\{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}\right\}$ a base de ℝ³
> 
> **Agregar base canónica:**
> 
> $$T = \left\{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\}$$
> 
> **Matriz:**
> 
> $$A = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
> 
> **Reducir:**
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$
> 
> **Pivotes en columnas 1, 2, 3**
> 
> **Base extendida:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}\right\}$$
> 
> o más simple:
> 
> $$\boxed{\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\}}$$
> 
> ---
> 
> **6a)** Base de ${p(x) \in P_3 : p(0) = 0}$
> 
> **Condición:** $p(0) = a_0 = 0$
> 
> **Forma general:** $p(x) = a_1x + a_2x^2 + a_3x^3$
> 
> **Base:**
> 
> $$\boxed{\mathcal{B} = {x, x^2, x^3}}$$
> 
> $$\dim = 3$$
> 
> ---
> 
> **6b)** Base de ${p(x) \in P_3 : p(1) = p(-1)}$
> 
> **Condición:**
> 
> $$p(1) = a_0 + a_1 + a_2 + a_3$$ $$p(-1) = a_0 - a_1 + a_2 - a_3$$
> 
> **Igualdad:** $a_1 + a_3 = -a_1 + a_3 \Rightarrow 2a_1 = 0 \Rightarrow a_1 = 0$
> 
> Pero también: $a_0 + a_2 = a_0 + a_2$ (siempre cierto)
> 
> **Corrección:** $p(1) - p(-1) = 2a_1 + 2a_3 = 0 \Rightarrow a_1 + a_3 = 0 \Rightarrow a_3 = -a_1$
> 
> **Forma:** $p(x) = a_0 + a_1x + a_2x^2 - a_1x^3 = a_0 \cdot 1 + a_1(x - x^3) + a_2 \cdot x^2$
> 
> **Base:**
> 
> $$\boxed{\mathcal{B} = {1, x - x^3, x^2}}$$
> 
> $$\dim = 3$$
> 
> ---
> 
> **6c)** Dimensión de ${p(x) \in P_n : p'(0) = 0}$
> 
> **Derivada:** $p'(x) = a_1 + 2a_2x + 3a_3x^2 + \cdots + na_nx^{n-1}$
> 
> **Condición:** $p'(0) = a_1 = 0$
> 
> **Forma:** $p(x) = a_0 + a_2x^2 + a_3x^3 + \cdots + a_nx^n$
> 
> **Parámetros libres:** $a_0, a_2, a_3, \ldots, a_n$ → $n$ parámetros
> 
> $$\boxed{\dim = n}$$

### Soluciones Ejercicios Avanzados

> [!success]- 🔑 Respuestas Nivel 3
> 
> **7a)** Matrices antisimétricas $3 \times 3$ (donde $A^T = -A$)
> 
> **Forma general:**
> 
> $$A = \begin{bmatrix} 0 & a & b \ -a & 0 & c \ -b & -c & 0 \end{bmatrix}$$
> 
> **Observación:** Diagonal debe ser cero, y $a_{ij} = -a_{ji}$
> 
> **Parámetros independientes:** $a, b, c$
> 
> **Base:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ -1 & 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(\text{Antisim}_3) = 3 = \frac{3(3-1)}{2}}$$
> 
> **Fórmula general:** $\dim(\text{Antisim}_n) = \frac{n(n-1)}{2}$
> 
> ---
> 
> **7c)** Matrices $2 \times 2$ con traza cero
> 
> **Condición:** $\text{tr}(A) = a + d = 0 \Rightarrow d = -a$
> 
> **Forma general:**
> 
> $$A = \begin{bmatrix} a & b \ c & -a \end{bmatrix}$$
> 
> **Parámetros:** $a, b, c$
> 
> **Base:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim = 3}$$
> 
> ---
> 
> **8.** Suma e intersección de subespacios
> 
> $$U = \text{span}\left\{\vec{u}_1 = \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \vec{u}_2 = \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right\}$$
> 
> $$W = \text{span}\left\{\vec{w}_1 = \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \vec{w}_2 = \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}\right\}$$
> 
> **a) Base de $U + W$:**
> 
> Formar matriz con todos los vectores:
> 
> $$A = \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 1 & 1 & 0 & 2 \end{bmatrix}$$
> 
> Reducir:
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{bmatrix}$$
> 
> Pivotes en columnas 1, 2, 3
> 
> **Base de $U + W$:**
> 
> $$\mathcal{B}_{U+W} = \left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(U + W) = 3 = \mathbb{R}^3}$$
> 
> **b) Base de $U \cap W$:**
> 
> Un vector está en $U \cap W$ si:
> 
> $$\vec{v} = s\vec{u}_1 + t\vec{u}_2 = r\vec{w}_1 + q\vec{w}_2$$
> 
> Sistema:
> 
> $$s\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + t\begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} = r\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} + q\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}$$
> 
> $$\begin{cases} s = r + q \\ t = r + q \\ s + t = 2q \end{cases}$$
> 
> De las dos primeras: $s = t$
> 
> De la tercera: $2s = 2q \Rightarrow s = q$
> 
> De la primera: $s = r + s \Rightarrow r = 0$
> 
> **Solución:** $r = 0$, $q = s$, $t = s$
> 
> $$\vec{v} = s(\vec{u}_1 + \vec{u}_2) = s\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}$$
> 
> **Base de $U \cap W$:**
> 
> $$\mathcal{B}_{U \cap W} = \left\{\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}\right\}$$
> 
> $$\boxed{\dim(U \cap W) = 1}$$
> 
> **c) Verificación:**
> 
> $$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$$ $$3 = 2 + 2 - 1$$ ✓

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Bases
> 
> ✅ **Definición dual:**
> 
> - Base = conjunto generador mínimo
> - Base = conjunto independiente maximal
> - Base = conjunto que permite representación única
> 
> ✅ **Propiedades fundamentales:**
> 
> - Todo espacio (≠ {0}) tiene al menos una base
> - Todas las bases del mismo espacio tienen igual tamaño
> - Ese tamaño se llama dimensión
> 
> ✅ **Bases en ℝⁿ:**
> 
> - Base canónica: ${\vec{e}_1, \ldots, \vec{e}_n}$
> - $n$ vectores independientes → base
> - $n$ vectores que generan → base
> - Determinante ≠ 0 → base
> 
> ---
> 
> ### Sobre Dimensión
> 
> ✅ **Significado:**
> 
> - Número de "grados de libertad"
> - Número mínimo de coordenadas
> - "Tamaño" del espacio vectorial
> 
> ✅ **Propiedades:**
> 
> - $\dim(W) \leq \dim(V)$ si $W \subseteq V$
> - $\dim(W) = \dim(V) \Rightarrow W = V$
> - Invariante: no depende de la base
> 
> ✅ **Fórmulas útiles:**
> 
> - $\dim(\mathbb{R}^n) = n$
> - $\dim(P_n) = n + 1$
> - $\dim(M_{m \times n}) = m \cdot n$
> - $\dim(\text{Sim}_n) = \frac{n(n+1)}{2}$
> - $\text{rango}(A) + \text{nulidad}(A) = n$ (columnas)
> 
> ---
> 
> ### Procedimientos Clave
> 
> ✅ **Encontrar base de span:**
> 
> 1. Formar matriz con vectores como columnas
> 2. Reducir a RREF
> 3. Columnas pivote de matriz original = base
> 
> ✅ **Encontrar base de espacio nulo:**
> 
> 4. Resolver $A\vec{x} = \vec{0}$
> 5. Expresar en forma paramétrica
> 6. Vectores de parámetros = base
> 
> ✅ **Extender a base:**
> 
> 7. Partir con conjunto independiente
> 8. Agregar vectores canónicos
> 9. Aplicar método de columnas pivote
> 
> ---
> 
> ### Teoremas Importantes
> 
> ✅ **Caracterización de bases:**
> 
> - En $\dim(V) = n$: independiente con $n$ vectores → base
> - En $\dim(V) = n$: generador con $n$ vectores → base
> 
> ✅ **Teorema del rango:**
> 
> - $\dim(\text{Col}(A)) + \dim(\text{Nul}(A)) = n$
> 
> ✅ **Dimensión de suma:**
> 
> - $\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$

---

## 📊 Tabla Resumen Comparativa

> [!note]- 📋 Guía Rápida
> 
> |Concepto|Definición|Propiedades|Dimensión|
> |---|---|---|---|
> |**ℝⁿ**|Vectores con $n$ componentes|Espacio vectorial estándar|$n$|
> |**Base canónica de ℝⁿ**|${\vec{e}_1, \ldots, \vec{e}_n}$|Ortogonal, ortonormal|$n$ vectores |
> | **Pₙ** | Polinomios grado ≤ n | Todas operaciones definidas | $n+1$ | | **Base canónica de Pₙ** | ${1, x, x^2, \ldots, x^n}$ | Monomios | $n+1$ vectores | | **M_{m×n}** | Matrices m×n | Suma y multiplicación escalar | $m \cdot n$ | | **Sim_n** | Matrices simétricas n×n | $A^T = A$ | $\frac{n(n+1)}{2}$ | | **Antisim_n** | Matrices antisimétricas n×n | $A^T = -A$ | $\frac{n(n-1)}{2}$ | | **Diag_n** | Matrices diagonales n×n | $a_{ij} = 0$ si $i \neq j$ | $n$ | | **Col(A)** | Espacio columna de A | Combinaciones de columnas | rango(A) | | **Nul(A)** | Espacio nulo de A | Soluciones de $A\vec{x} = \vec{0}$ | nulidad(A) | | **Fila(A)** | Espacio fila de A | Combinaciones de filas | rango(A) |
> 
> ---
> 
> ### Relaciones Importantes
> 
> |Relación|Fórmula|Nombre|
> |---|---|---|
> |Suma de dimensiones|$\text{rango}(A) + \text{nulidad}(A) = n$|Teorema del Rango|
> |Subespacio propio|$\dim(W) < \dim(V)$ si $W \subset V$|Desigualdad estricta|
> |Suma de subespacios|$\dim(U+W) = \dim(U) + \dim(W) - \dim(U \cap W)$|Fórmula de dimensión|
> |Suma directa|$\dim(U \oplus W) = \dim(U) + \dim(W)$|Si $U \cap W = {\vec{0}}$|
> |Complemento|$\dim(V) = \dim(W) + \dim(W^{\perp})$|Descomposición ortogonal|

---

## 🔗 Relaciones con Otros Temas

> [!quote]- 🌐 Conexiones Conceptuales
> 
> ### Prerequisitos:
> 
> - **[[06 - Combinaciones Lineales]]** - Construcción de vectores
> - **[[07 - Sistemas de Ecuaciones Lineales]]** - Resolución de sistemas
> - **[[08 - Matrices y Operaciones]]** - Representación matricial
> - **[[09 - Espacio Generado (Span)]]** - Conjuntos generadores
> - **[[01 – Dependencia e independencia lineal]]** - Conjuntos independientes
> 
> ### Este tema es prerequisito para:
> 
> - **[[12 - Espacio Columna y Rango]]** - Aplicación directa de bases
> - **[[13 - Espacio Nulo y Nulidad]]** - Bases de espacios nulos
> - **[[14 - Coordenadas y Cambio de Base]]** - Representación en bases
> - **[[15 - Teorema del Rango]]** - Relación dimensional
> - **[[16 - Transformaciones Lineales]]** - Dimensión de imagen y núcleo
> - **[[17 - Valores y Vectores Propios]]** - Bases especiales
> - **[[18 - Diagonalización]]** - Bases de vectores propios
> - **[[19 - Espacios con Producto Interno]]** - Bases ortonormales
> 
> ### Conceptos relacionados:
> 
> - **Coordenadas** - Representación única en base
> - **Cambio de base** - Transformación entre bases
> - **Rango** - Dimensión del espacio columna
> - **Nulidad** - Dimensión del espacio nulo
> - **Ortogonalización** - Construcción de bases ortogonales
> 
> ### Diagrama de Flujo:
> 
> ```
> Independencia Lineal
>          ↓
>    Espacio Generado
>          ↓
>    BASE Y DIMENSIÓN
>          ↓
>    ┌─────┴─────┐
>    ↓           ↓
> Coordenadas  Teorema del Rango
>    ↓           ↓
> Cambio Base  Transformaciones
> ```
> 
> ### Siguiente tema recomendado:
> 
> **[[12 - Espacio Columna y Rango]]** - Aplicación de bases a matrices y sistemas lineales

---

## 🎓 Guía de Estudio

> [!tip]- 📖 Estrategia de Aprendizaje
> 
> ### Nivel 1: Comprensión Básica
> 
> **Objetivos:**
> 
> - [ ] Definir qué es una base
> - [ ] Entender la dimensión como invariante
> - [ ] Reconocer la base canónica de ℝⁿ
> - [ ] Calcular dimensiones de espacios comunes
> 
> **Actividades:**
> 
> 1. Memorizar definiciones formales
> 2. Practicar verificación de bases en ℝ² y ℝ³
> 3. Calcular dimensiones de espacios estándar
> 4. Visualizar bases geométricamente
> 
> **Tiempo estimado:** 2-3 horas
> 
> ---
> 
> ### Nivel 2: Aplicación de Procedimientos
> 
> **Objetivos:**
> 
> - [ ] Encontrar bases de espacios generados
> - [ ] Encontrar bases de espacios nulos
> - [ ] Extender conjuntos independientes a bases
> - [ ] Reducir conjuntos generadores a bases
> - [ ] Calcular coordenadas en bases no estándar
> 
> **Actividades:**
> 
> 1. Dominar método de columnas pivote
> 2. Practicar resolución paramétrica
> 3. Realizar 10+ ejercicios de cada tipo
> 4. Verificar respuestas por múltiples métodos
> 
> **Tiempo estimado:** 4-6 horas
> 
> ---
> 
> ### Nivel 3: Conceptos Avanzados
> 
> **Objetivos:**
> 
> - [ ] Trabajar con bases de espacios abstractos
> - [ ] Aplicar teorema del rango
> - [ ] Calcular suma e intersección de subespacios
> - [ ] Demostrar propiedades de dimensión
> - [ ] Resolver problemas con parámetros
> 
> **Actividades:**
> 
> 1. Estudiar demostraciones de teoremas
> 2. Resolver problemas de matrices especiales
> 3. Aplicar fórmula de dimensión de suma
> 4. Conectar con transformaciones lineales
> 
> **Tiempo estimado:** 5-8 horas
> 
> ---
> 
> ### Nivel 4: Maestría y Aplicaciones
> 
> **Objetivos:**
> 
> - [ ] Reconocer patrones instantáneamente
> - [ ] Elegir método óptimo para cada problema
> - [ ] Conectar con aplicaciones reales
> - [ ] Resolver problemas de competencia
> 
> **Actividades:**
> 
> 1. Problemas mixtos y de síntesis
> 2. Casos de aplicación (PCA, gráficos)
> 3. Optimización de cálculos
> 4. Problemas de olimpiadas matemáticas
> 
> **Tiempo estimado:** 8-12 horas

---

## 🎯 Errores Comunes y Cómo Evitarlos

> [!warning]- ⚠️ Trampas Frecuentes
> 
> ### Error 1: Confundir tamaño con dimensión
> 
> **❌ Incorrecto:** "Este conjunto tiene 5 vectores, entonces la dimensión es 5"
> 
> **✅ Correcto:** La dimensión es el número de vectores en una **base**, no en cualquier conjunto generador. Puede haber redundancia.
> 
> **Ejemplo:** $$S = \left\{\begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 2 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 3 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \end{bmatrix}\right\}$$
> 
> Aunque $|S| = 5$, la dimensión de $\text{span}(S)$ es 2 (es ℝ²).
> 
> ---
> 
> ### Error 2: Usar columnas de RREF en lugar de originales
> 
> **❌ Incorrecto:** Tomar columnas pivote de la matriz reducida como base
> 
> **✅ Correcto:** Las columnas pivote indican **posiciones**, pero debes tomar las columnas **originales**
> 
> **Razón:** La reducción cambia el espacio columna, pero preserva relaciones de dependencia.
> 
> ---
> 
> ### Error 3: Olvidar verificar independencia
> 
> **❌ Incorrecto:** "Este conjunto genera V y tiene n vectores, pero ¿es base?"
> 
> **✅ Correcto:** Si genera V y tiene $n = \dim(V)$ vectores, entonces **automáticamente** es independiente (por teorema).
> 
> No necesitas verificar ambas propiedades si el tamaño es correcto.
> 
> ---
> 
> ### Error 4: Confundir base con espacio
> 
> **❌ Incorrecto:** "La base es igual al espacio vectorial"
> 
> **✅ Correcto:**
> 
> - La **base** es un conjunto de vectores
> - El **espacio** es el span de la base
> - $\mathcal{B} \neq V$, pero $\text{span}(\mathcal{B}) = V$
> 
> ---
> 
> ### Error 5: Dimensión del espacio nulo
> 
> **❌ Incorrecto:** "Número de ecuaciones = dimensión del espacio nulo"
> 
> **✅ Correcto:** Dimensión del espacio nulo = **número de variables libres**, no número de ecuaciones
> 
> **Fórmula correcta:** $$\dim(\text{Nul}(A)) = n - \text{rango}(A)$$
> 
> donde $n$ = número de columnas
> 
> ---
> 
> ### Error 6: Coordenadas en base incorrecta
> 
> **❌ Incorrecto:** Usar coordenadas estándar cuando se pide coordenadas en base específica
> 
> **✅ Correcto:** Siempre verificar **respecto a qué base** estás expresando el vector
> 
> **Notación:** $[\vec{v}]_{\mathcal{B}}$ indica coordenadas respecto a base $\mathcal{B}$

---

## 🧩 Problemas Desafío

> [!example]- 🏆 Para Pensar Profundamente
> 
> ### Problema 1: Dimensión de intersección
> 
> En ℝ⁴, sean $U$ y $W$ subespacios con $\dim(U) = \dim(W) = 3$.
> 
> **Pregunta:** ¿Cuáles son los valores posibles de $\dim(U \cap W)$?
> 
>Pista: Usa la fórmula de dimensión: $\dim(U+W) = \dim(U) + \dim(W) - \dim(U \cap W)$
> 
> Recuerda que $\dim(U+W) \leq 4$ (están en ℝ⁴)
> 
> Solución:
> 
> De la fórmula: $$\dim(U \cap W) = \dim(U) + \dim(W) - \dim(U+W) = 3 + 3 - \dim(U+W) = 6 - \dim(U+W)$$
> 
> Como $\dim(U+W) \leq 4$: $$\dim(U \cap W) \geq 6 - 4 = 2$$
> 
> También, $\dim(U \cap W) \leq \min(\dim(U), \dim(W)) = 3$
> 
> **Respuesta:** $\dim(U \cap W) \in {2, 3}$
> 
> 
> 
> ---
> 
> ### Problema 2: Base especial
> 
> Encontrar una base de ℝ³ tal que cada vector de la base sea ortogonal a $\vec{v} = \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}$ excepto uno.
> 
> Pista Comienza encontrando dos vectores ortogonales a $\vec{v}$, luego completa con $\vec{v}$ mismo. 
> 
> ---
> 
> ### Problema 3: Dimensión paramétrica
> 
> Sea $W_k$ el subespacio de ℝ⁴ definido por:
> 
> $$W_k = \left\{\begin{bmatrix} x \ y \ z \ w \end{bmatrix} : x + y + kz = 0, \ 2x - y + w = 0\right\}$$
> 
> **Pregunta:** ¿Para qué valores de $k$ se tiene $\dim(W_k) = 2$?
> 
> Solución
> 
> Formar matriz de coeficientes: $$A = \begin{bmatrix} 1 & 1 & k & 0 \ 2 & -1 & 0 & 1 \end{bmatrix}$$
> 
> Para que $\dim(W_k) = 2$, necesitamos: $$\text{rango}(A) = 4 - 2 = 2$$
> 
> Es decir, las dos filas deben ser independientes.
> 
> Las filas son siempre independientes (no proporcionales) para cualquier $k$.
> 
> **Respuesta:** Para **todo** $k \in \mathbb{R}$, $\dim(W_k) = 2$
> 
> </details>
> 
> ---
> 
> ### Problema 4: Bases y determinantes
> 
> Si $\mathcal{B} = {\vec{v}_1, \vec{v}_2, \vec{v}_3}$ es base de ℝ³ y $\det[\vec{v}_1 \ \vec{v}_2 \ \vec{v}_3] = 5$, ¿cuál es el determinante de la matriz formada por ${\vec{v}_1 + \vec{v}_2, \ \vec{v}_2, \ \vec{v}_3}$?
> 
> Pista: Usa propiedades de determinantes: sumar una fila/columna a otra no cambia el determinante. Solución
> 
> $$\det[\vec{v}_1 + \vec{v}_2 \ \vec{v}_2 \ \vec{v}_3] = \det[\vec{v}_1 \ \vec{v}_2 \ \vec{v}_3] + \det[\vec{v}_2 \ \vec{v}_2 \ \vec{v}_3]$$
> 
> El segundo determinante es 0 (columnas repetidas).
> 
> **Respuesta:** $\det = 5$
> 
> </details>
> 
> ---
> 
> ### Problema 5: Dimensión infinita
> 
> Considera el espacio $C[0,1]$ de todas las funciones continuas en $[0,1]$.
> 
> **Preguntas:** a) ¿Es ${1, x, x^2, x^3, \ldots}$ una base de $C[0,1]$?
> 
> b) ¿Cuál es $\dim(C[0,1])$?
> 
> Respuestas:
> 
> a) **No**. Este conjunto genera solo los polinomios, que son un subconjunto propio de $C[0,1]$. Por ejemplo, $e^x$ no es polinomio.
> 
> b) $\dim(C[0,1]) = \infty$ (dimensión infinita). No hay conjunto finito que genere todas las funciones continuas.
> 
> </details>

---

## 📖 Resumen Ejecutivo

> [!summary]- 📋 Lo Esencial en 5 Minutos
> 
> ### Definiciones Centrales
> 
> **Base:** Conjunto linealmente independiente que genera el espacio
> 
> - Es generador **mínimo**
> - Es independiente **maximal**
> - Permite representación **única**
> 
> **Dimensión:** Número de vectores en cualquier base
> 
> - Invariante (no depende de la base elegida)
> - Mide el "tamaño" del espacio
> - $\dim(\mathbb{R}^n) = n$, $\dim(P_n) = n+1$, $\dim(M_{m \times n}) = mn$
> 
> ---
> 
> ### Teoremas Clave
> 
> 1. **Todas las bases tienen igual tamaño** (dimensión bien definida)
>     
> 2. **En $\dim(V) = n$:**
>     
>     - $n$ vectores independientes → base
>     - $n$ vectores generadores → base
> 3. **Teorema del Rango:** $$\text{rango}(A) + \text{nulidad}(A) = n$$
>     
> 4. **Dimensión de suma:** $$\dim(U+W) = \dim(U) + \dim(W) - \dim(U \cap W)$$
>     
> 
> ---
> 
> ### Métodos Fundamentales
> 
> **Encontrar base de span(S):**
> 
> 1. Matriz con vectores como columnas
> 2. RREF
> 3. Columnas pivote de original
> 
> **Encontrar base de Nul(A):**
> 
> 4. Resolver $A\vec{x} = \vec{0}$
> 5. Forma paramétrica
> 6. Vectores de parámetros
> 
> **Verificar si es base:**
> 
> - Método rápido: Tamaño correcto + una propiedad
> - Método completo: Independencia Y generación
> 
> ---
> 
> ### Aplicaciones
> 
> - **Sistemas de coordenadas:** Bases personalizadas
> - **Compresión de datos:** PCA, reducción dimensional
> - **Física cuántica:** Estados en bases ortonormales
> - **Ecuaciones diferenciales:** Dimensión del espacio de soluciones
> - **Gráficos computacionales:** Transformaciones de coordenadas

---

## ✨ Reflexión Final

> [!quote]- 💭 La Importancia de Bases y Dimensión
> 
> ### Por qué es fundamental
> 
> El concepto de **base** y **dimensión** es el corazón del álgebra lineal moderna:
> 
> **Base = Lenguaje óptimo**
> 
> - Es el "alfabeto" mínimo para describir todo el espacio
> - Cada vector tiene una "escritura" única (coordenadas)
> - Optimiza representación y cálculo
> 
> **Dimensión = Medida del espacio**
> 
> - Cuantifica la complejidad del espacio
> - Invariante fundamental (como el "ADN" del espacio)
> - Determina completamente espacios de dimensión finita
> 
> ---
> 
> ### Conexión con el mundo real
> 
> **En ciencia de datos:**
> 
> - Reducción dimensional (PCA): encontrar base óptima
> - Cada "característica" es una dimensión
> - Eliminar dimensiones redundantes = mejorar eficiencia
> 
> **En física:**
> 
> - Grados de libertad = dimensión del espacio de estados
> - Bases ortonormales = sistemas de medición
> - Cambio de base = transformación de referencia
> 
> **En ingeniería:**
> 
> - Señales = vectores en espacio infinito-dimensional
> - Base de Fourier = descomposición en frecuencias
> - Compresión = representación en base eficiente
> 
> ---
> 
> ### El camino hacia adelante
> 
> Con bases y dimensión dominadas, ahora puedes:
> 
> ✅ **Entender coordenadas** - Representación en diferentes bases
> 
> ✅ **Analizar transformaciones** - Cómo cambian dimensiones
> 
> ✅ **Aplicar el teorema del rango** - Relaciones fundamentales
> 
> ✅ **Trabajar con productos internos** - Bases ortogonales
> 
> ✅ **Diagonalizar matrices** - Bases de vectores propios
> 
> ---
> 
> ### Mensaje clave
> 
> **Las bases son los "ladrillos" y la dimensión es el "plano":**
> 
> - Una base te dice **cómo construir** el espacio
> - La dimensión te dice **qué tan grande** es el espacio
> - Juntos, caracterizan completamente espacios vectoriales
> 
> Dominar estos conceptos es dominar la esencia del álgebra lineal. Cada tema posterior construye sobre esta fundación sólida.

---

## 🔄 Próximos Pasos

> [!tip]- 🎯 Plan de Acción
> 
> ### Para consolidar este tema:
> 
> 1. **Practicar 20+ problemas** de cada tipo
> 2. **Visualizar geométricamente** en ℝ² y ℝ³
> 3. **Conectar con temas previos** (independencia, span)
> 4. **Anticipar aplicaciones** (transformaciones, coordenadas)
> 
> ### Tema siguiente recomendado:
> 
> **[[12 - Espacio Columna y Rango]]**
> 
> - Aplicación directa de bases
> - Profundización del teorema del rango
> - Conexión con sistemas lineales
> 
> ### Temas alternativos:
> 
> **Si quieres profundizar primero:**
> 
> - **[[14 - Coordenadas y Cambio de Base]]** - Representación en bases
> - **[[13 - Espacio Nulo y Nulidad]]** - Bases de espacios nulos
> 
> **Si quieres ver aplicaciones:**
> 
> - **[[19 - Espacios con Producto Interno]]** - Bases ortonormales
> - **Reducción dimensional (PCA)** - Aplicación práctica

---

**Tags:** #algebra-lineal #base #dimension #espacio-vectorial #coordenadas #teorema-rango #independencia-lineal #generadores #subespacios #dimension-finita
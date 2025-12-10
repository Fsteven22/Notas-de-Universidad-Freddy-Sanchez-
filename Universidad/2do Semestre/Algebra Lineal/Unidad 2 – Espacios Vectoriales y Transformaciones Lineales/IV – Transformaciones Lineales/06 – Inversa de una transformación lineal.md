# 🔄 Inversa de una Transformación Lineal

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva
> **La inversa de una transformación lineal es una transformación que "deshace" el efecto de la original, regresando cada vector a su posición inicial. Es el proceso de "reversa" algebraico que permite recuperar la entrada original a partir de la salida. Solo existe cuando la transformación es biyectiva (isomorfismo), garantizando que cada salida tiene exactamente una entrada asociada.**
>
> **Características clave:**
> - **Reversibilidad perfecta:** Aplicar T y luego T⁻¹ regresa al vector original
> - **Biyectividad necesaria:** Solo isomorfismos tienen inversa
> - **Linealidad preservada:** La inversa también es transformación lineal
> - **Unicidad:** Si existe, la inversa es única
> - **Composición identidad:** T⁻¹ ∘ T = Id y T ∘ T⁻¹ = Id
> - **Simetría:** (T⁻¹)⁻¹ = T

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto
> **Raíces en funciones inversas (1600-1800):**
> - **Descartes (1637):** Geometría analítica
>   - Funciones y sus inversas geométricas
>   - Reflexión sobre y = x
> - **Leibniz (1684):** Cálculo diferencial
>   - Inversa de la derivación (integración)
>   - Notación de funciones inversas
> - **Euler (1748):** Introductio in analysin infinitorum
>   - Funciones trigonométricas inversas
>   - Función logarítmica como inversa de exponencial
>   - Notación sistemática
>
> **Matrices inversas (1800-1850):**
> - **Gauss (1809):** Teoría de mínimos cuadrados
>   - Sistemas de ecuaciones lineales
>   - Método de eliminación
>   - Concepto implícito de matriz inversa
> - **Cauchy (1829):** "Mémoire sur les fonctions"
>   - Primera definición de determinante
>   - Relación con invertibilidad
>   - det(A) ≠ 0 ⟺ A invertible
> - **Cayley (1858):** "Memoir on the Theory of Matrices"
>   - **Primeras matrices inversas explícitas** ⭐
>   - Álgebra matricial formal
>   - A⁻¹A = AA⁻¹ = I
>   - Publicación revolucionaria
>
> **Teoría de grupos (1830-1870):**
> - **Galois (1830-1832):** Teoría de grupos
>   - Elementos inversos en grupos
>   - Grupo simétrico y permutaciones inversas
>   - Trabajo póstumo publicado en 1846
> - **Cayley (1854):** Grupos abstractos
>   - Todo elemento de grupo tiene inverso
>   - Grupo lineal general GL(n)
>   - Matrices invertibles forman grupo
>
> **Transformaciones lineales (1850-1900):**
> - **Sylvester (1850s):** Teoría de matrices
>   - Término "matriz" (del latín "matriz" = útero)
>   - Rango y nulidad
>   - Criterios de invertibilidad
> - **Grassmann (1862):** Ausdehnungslehre (2ª ed.)
>   - Transformaciones lineales abstractas
>   - Operadores inversos
>   - Adelantado conceptualmente
> - **Frobenius (1878):** Teoría de matrices
>   - Forma canónica
>   - Factorización
>   - Propiedades de inversas
>
> **Formalización moderna (1900-1930):**
> - **Wedderburn (1907):** "On Hypercomplex Numbers"
>   - Álgebras de división
>   - Teoría de anillos
>   - Elementos invertibles
> - **Emmy Noether (1920s):** Álgebra abstracta
>   - Inversas en anillos y cuerpos
>   - Unidades en teoría de anillos
>   - Marco general para invertibilidad
> - **van der Waerden (1930):** "Moderne Algebra"
>   - **Tratamiento sistemático de inversas** ⭐⭐
>   - Unificación de teorías
>   - Libro de texto influyente
>
> **Análisis funcional (1920-1950):**
> - **Banach (1932):** Théorie des opérations linéaires
>   - **Teorema de la aplicación abierta** ⭐⭐⭐
>   - Operadores inversos acotados
>   - Espacios de Banach
> - **von Neumann (1930s):** Espacios de Hilbert
>   - Operadores autoadjuntos
>   - Inversa de Moore-Penrose (pseudoinversa)
>   - Análisis espectral
> - **Gelfand (1941):** Teoría de álgebras de Banach
>   - Espectro e invertibilidad
>   - Teoría de perturbaciones
>
> **Métodos numéricos (1950-presente):**
> - **Wilkinson (1960s):** Análisis numérico
>   - Estabilidad de algoritmos de inversión
>   - Condicionamiento de matrices
>   - "Algebraic Eigenvalue Problem" (1965)
> - **Golub & Van Loan (1983):** "Matrix Computations"
>   - Algoritmos modernos de inversión
>   - Descomposiciones (LU, QR, SVD)
>   - Pseudoinversa computacional
> - **Aplicaciones modernas:**
>   - Criptografía (RSA usa inversas modulares)
>   - Computer graphics (transformaciones inversas)
>   - Control systems (retroalimentación inversa)
>   - Machine learning (backpropagation como inversa)
>   - Redes neuronales (capas invertibles, flow models)
>
> **Desarrollos recientes:**
> - **Invertible Neural Networks (2018-presente):**
>   - Normalizing flows
>   - Transformaciones invertibles aprendibles
>   - Generative models
> - **Teoría de categorías:**
>   - Isomorfismos como morfismos invertibles
>   - Equivalencias de categorías
>
> **Nota histórica:** El concepto de inversa ha sido fundamental en matemáticas desde tiempos antiguos (división como inversa de multiplicación), pero su formalización para transformaciones lineales y matrices tomó hasta el siglo XIX. Cayley's 1858 memoir marca el nacimiento del álgebra lineal moderna.

## 📊 Definiciones Formales

> [!important]- Transformación Lineal Inversa
> **DEFINICIÓN (Inversa de una Transformación):**
>
> Sea $T: V \to W$ una transformación lineal. La **inversa** de $T$ (si existe) es una transformación lineal $T^{-1}: W \to V$ que satisface:
>
> $$\boxed{\begin{aligned}
> T^{-1} \circ T &= \text{Id}_V \\
> T \circ T^{-1} &= \text{Id}_W
> \end{aligned}}$$
>
> Equivalentemente, para todo $\vec{v} \in V$ y todo $\vec{w} \in W$:
>
> $$\boxed{T^{-1}(\vec{w}) = \vec{v} \iff T(\vec{v}) = \vec{w}}$$
>
> **NOTACIÓN:**
> - $T^{-1}$ se lee "T inversa"
> - El exponente -1 **NO** significa $\frac{1}{T}$, sino la operación inversa
>
> **CONDICIÓN DE EXISTENCIA:**
>
> $$\boxed{T^{-1} \text{ existe} \iff T \text{ es biyectiva (isomorfismo)}}$$

> [!important]- Transformación Invertible
> **DEFINICIÓN (Transformación Invertible):**
>
> Una transformación lineal $T: V \to W$ es **invertible** si existe su inversa $T^{-1}: W \to V$.
>
> $$\boxed{T \text{ invertible} \iff \exists T^{-1} \text{ tal que } T^{-1} \circ T = \text{Id}_V \text{ y } T \circ T^{-1} = \text{Id}_W}$$
>
> **CARACTERIZACIONES EQUIVALENTES:**
>
> Las siguientes condiciones son **equivalentes**:
> 1. $T$ es invertible
> 2. $T$ es biyectiva (inyectiva y sobreyectiva)
> 3. $T$ es un isomorfismo
> 4. $\text{Ker}(T) = \{\vec{0}\}$ y $\text{Im}(T) = W$
> 5. $\text{nullity}(T) = 0$ y $\text{rank}(T) = \dim(W)$
> 6. $T$ transforma bases en bases
> 7. Si $T$ está representada por matriz $A$ (cuadrada), entonces $\det(A) \neq 0$

> [!important]- Propiedades Fundamentales de la Inversa
> **TEOREMA (Propiedades de T⁻¹):**
>
> Si $T: V \to W$ es invertible, entonces:
>
> **1. UNICIDAD:**
> $$\boxed{\text{La inversa es única}}$$
> Si $S$ y $R$ satisfacen las propiedades de inversa, entonces $S = R = T^{-1}$
>
> **2. LINEALIDAD:**
> $$\boxed{T^{-1} \text{ es transformación lineal}}$$
> Para $\vec{w}_1, \vec{w}_2 \in W$ y $c \in \mathbb{F}$:
> - $T^{-1}(\vec{w}_1 + \vec{w}_2) = T^{-1}(\vec{w}_1) + T^{-1}(\vec{w}_2)$
> - $T^{-1}(c\vec{w}) = cT^{-1}(\vec{w})$
>
> **3. INVERTIBILIDAD DE LA INVERSA:**
> $$\boxed{T^{-1} \text{ es invertible y } (T^{-1})^{-1} = T}$$
>
> **4. COMPOSICIÓN IDENTIDAD:**
> $$\boxed{\begin{aligned}
> (T^{-1} \circ T)(\vec{v}) &= \vec{v} \quad \forall \vec{v} \in V \\
> (T \circ T^{-1})(\vec{w}) &= \vec{w} \quad \forall \vec{w} \in W
> \end{aligned}}$$
>
> **5. PRESERVACIÓN DE NÚCLEO E IMAGEN:**
> $$\boxed{\begin{aligned}
> \text{Ker}(T^{-1}) &= \{\vec{0}\} \\
> \text{Im}(T^{-1}) &= V
> \end{aligned}}$$

## 🎯 Teoremas Fundamentales

> [!success]- Teorema de Existencia y Unicidad
> **TEOREMA 1: Existencia y unicidad de la inversa** ⭐⭐⭐
>
> Sea $T: V \to W$ transformación lineal.
>
> $$\boxed{T \text{ tiene inversa} \iff T \text{ es biyectiva}}$$
>
> Además, si existe, la inversa es **única**.
>
> **DEMOSTRACIÓN:**
>
> **($\Rightarrow$) Si T tiene inversa, entonces T es biyectiva:**
>
> Suponer que existe $T^{-1}: W \to V$ tal que:
> - $T^{-1} \circ T = \text{Id}_V$
> - $T \circ T^{-1} = \text{Id}_W$
>
> **Inyectividad:**
>
> Si $T(\vec{v}) = \vec{0}$, entonces:
> $$\vec{v} = \text{Id}_V(\vec{v}) = (T^{-1} \circ T)(\vec{v}) = T^{-1}(T(\vec{v})) = T^{-1}(\vec{0}) = \vec{0}$$
>
> Por tanto $\text{Ker}(T) = \{\vec{0}\}$ ⇒ $T$ inyectiva ✓
>
> **Sobreyectividad:**
>
> Para cualquier $\vec{w} \in W$, sea $\vec{v} = T^{-1}(\vec{w}) \in V$.
>
> Entonces:
> $$T(\vec{v}) = T(T^{-1}(\vec{w})) = (T \circ T^{-1})(\vec{w}) = \text{Id}_W(\vec{w}) = \vec{w}$$
>
> Por tanto $\text{Im}(T) = W$ ⇒ $T$ sobreyectiva ✓
>
> **($\Leftarrow$) Si T es biyectiva, entonces existe T⁻¹:**
>
> Como $T$ es biyectiva, para cada $\vec{w} \in W$ existe **único** $\vec{v} \in V$ tal que $T(\vec{v}) = \vec{w}$.
>
> **Definir:** $T^{-1}: W \to V$ por:
> $$T^{-1}(\vec{w}) = \text{el único } \vec{v} \text{ tal que } T(\vec{v}) = \vec{w}$$
>
> **Verificar que T⁻¹ es lineal:**
>
> Sean $\vec{w}_1, \vec{w}_2 \in W$ y $c \in \mathbb{F}$.
>
> Sean $\vec{v}_1 = T^{-1}(\vec{w}_1)$ y $\vec{v}_2 = T^{-1}(\vec{w}_2)$.
>
> Por definición: $T(\vec{v}_1) = \vec{w}_1$ y $T(\vec{v}_2) = \vec{w}_2$
>
> **Aditividad:**
> $$T(\vec{v}_1 + \vec{v}_2) = T(\vec{v}_1) + T(\vec{v}_2) = \vec{w}_1 + \vec{w}_2$$
>
> Por definición de $T^{-1}$:
> $$T^{-1}(\vec{w}_1 + \vec{w}_2) = \vec{v}_1 + \vec{v}_2 = T^{-1}(\vec{w}_1) + T^{-1}(\vec{w}_2)$$ ✓
>
> **Homogeneidad:**
> $$T(c\vec{v}_1) = cT(\vec{v}_1) = c\vec{w}_1$$
>
> Por definición de $T^{-1}$:
> $$T^{-1}(c\vec{w}_1) = c\vec{v}_1 = cT^{-1}(\vec{w}_1)$$ ✓
>
> **Verificar composiciones:**
>
> Para $\vec{v} \in V$:
> $$(T^{-1} \circ T)(\vec{v}) = T^{-1}(T(\vec{v})) = \vec{v}$$
> por definición de $T^{-1}$ ✓
>
> Para $\vec{w} \in W$:
> $$(T \circ T^{-1})(\vec{w}) = T(T^{-1}(\vec{w})) = \vec{w}$$
> por definición de $T^{-1}$ ✓
>
> **Unicidad:**
>
> Si $S: W \to V$ también satisface las propiedades de inversa:
> $$S = S \circ \text{Id}_W = S \circ (T \circ T^{-1}) = (S \circ T) \circ T^{-1} = \text{Id}_V \circ T^{-1} = T^{-1}$$ ✓
>
> **Q.E.D.**

> [!success]- Teorema de Composición de Inversas
> **TEOREMA 2: Inversa de una composición** ⭐
>
> Sean $T: U \to V$ y $S: V \to W$ transformaciones lineales invertibles.
>
> Entonces $S \circ T: U \to W$ es invertible y:
>
> $$\boxed{(S \circ T)^{-1} = T^{-1} \circ S^{-1}}$$
>
> **INTERPRETACIÓN:** "La inversa de una composición es la composición de las inversas en orden inverso"
>
> **DEMOSTRACIÓN:**
>
> Necesitamos verificar:
> 1. $(T^{-1} \circ S^{-1}) \circ (S \circ T) = \text{Id}_U$
> 2. $(S \circ T) \circ (T^{-1} \circ S^{-1}) = \text{Id}_W$
>
> **Verificación 1:**
> $$\begin{aligned}
> (T^{-1} \circ S^{-1}) \circ (S \circ T) &= T^{-1} \circ (S^{-1} \circ S) \circ T \\
> &= T^{-1} \circ \text{Id}_V \circ T \\
> &= T^{-1} \circ T \\
> &= \text{Id}_U
> \end{aligned}$$ ✓
>
> **Verificación 2:**
> $$\begin{aligned}
> (S \circ T) \circ (T^{-1} \circ S^{-1}) &= S \circ (T \circ T^{-1}) \circ S^{-1} \\
> &= S \circ \text{Id}_V \circ S^{-1} \\
> &= S \circ S^{-1} \\
> &= \text{Id}_W
> \end{aligned}$$ ✓
>
> **Q.E.D.**
>
> ---
>
> **COROLARIO (Cadena de composiciones):**
>
> Para transformaciones invertibles $T_1, T_2, \ldots, T_n$:
>
> $$\boxed{(T_n \circ \cdots \circ T_2 \circ T_1)^{-1} = T_1^{-1} \circ T_2^{-1} \circ \cdots \circ T_n^{-1}}$$

> [!success]- Teorema de Representación Matricial
> **TEOREMA 3: Matriz de la inversa** ⭐⭐
>
> Sea $T: V \to W$ transformación lineal invertible, con matrices asociadas $[T]_{\mathcal{B}_V}^{\mathcal{B}_W}$ y $[T^{-1}]_{\mathcal{B}_W}^{\mathcal{B}_V}$ respecto a bases $\mathcal{B}_V$ de $V$ y $\mathcal{B}_W$ de $W$.
>
> Entonces:
>
> $$\boxed{[T^{-1}]_{\mathcal{B}_W}^{\mathcal{B}_V} = \left([T]_{\mathcal{B}_V}^{\mathcal{B}_W}\right)^{-1}}$$
>
> **INTERPRETACIÓN:** "La matriz de la transformación inversa es la matriz inversa de la transformación"
>
> **DEMOSTRACIÓN:**
>
> Sea $A = [T]_{\mathcal{B}_V}^{\mathcal{B}_W}$ y $B = [T^{-1}]_{\mathcal{B}_W}^{\mathcal{B}_V}$
>
> Por propiedades de composición:
> $$[T^{-1} \circ T]_{\mathcal{B}_V}^{\mathcal{B}_V} = [\text{Id}_V]_{\mathcal{B}_V}^{\mathcal{B}_V} = I_n$$
>
> donde $n = \dim(V)$.
>
> Por teorema de matrices de composición:
> $$[T^{-1} \circ T]_{\mathcal{B}_V}^{\mathcal{B}_V} = [T^{-1}]_{\mathcal{B}_W}^{\mathcal{B}_V} \cdot [T]_{\mathcal{B}_V}^{\mathcal{B}_W} = BA$$
>
> Por tanto: $BA = I_n$
>
> Similarmente: $AB = I_m$ donde $m = \dim(W)$
>
> Como $T$ es isomorfismo: $\dim(V) = \dim(W)$, entonces $n = m$
>
> Por tanto $B = A^{-1}$ ✓
>
> **Q.E.D.**
>
> ---
>
> **COROLARIO (Criterio de invertibilidad por determinante):**
>
> Para matrices cuadradas:
>
> $$\boxed{T \text{ invertible} \iff \det([T]) \neq 0}$$

> [!success]- Teorema del Grupo Lineal General
> **TEOREMA 4: GL(V) como grupo** ⭐
>
> El conjunto de todas las transformaciones lineales invertibles de $V$ en sí mismo forma un **grupo** bajo composición:
>
> $$\boxed{\text{GL}(V) = \{T: V \to V \mid T \text{ invertible}\}}$$
>
> llamado **grupo lineal general** de $V$.
>
> **PROPIEDADES DEL GRUPO:**
>
> 1. **Cerrado bajo composición:**
>    $$S, T \in \text{GL}(V) \implies S \circ T \in \text{GL}(V)$$
>
> 2. **Asociatividad:**
>    $$(R \circ S) \circ T = R \circ (S \circ T)$$
>
> 3. **Elemento identidad:**
>    $$\text{Id}_V \in \text{GL}(V)$$
>    $$T \circ \text{Id}_V = \text{Id}_V \circ T = T$$
>
> 4. **Inversos:**
>    $$T \in \text{GL}(V) \implies T^{-1} \in \text{GL}(V)$$
>    $$T \circ T^{-1} = T^{-1} \circ T = \text{Id}_V$$
>
> **DEMOSTRACIÓN:**
>
> **(1) Cerrado:** Si $S$ y $T$ son invertibles, entonces $S \circ T$ es biyectiva (composición de biyecciones), por tanto invertible ✓
>
> **(2) Asociatividad:** Propiedad general de composición de funciones ✓
>
> **(3) Identidad:** $\text{Id}_V$ es claramente biyectiva, por tanto invertible ✓
>
> **(4) Inversos:** Por Teorema 1, si $T$ invertible entonces $T^{-1}$ existe y también es invertible ✓
>
> **Q.E.D.**
>
> ---
>
> **NOTA:** Para $V = \mathbb{R}^n$ o $V = \mathbb{C}^n$, este grupo se denota:
> $$\text{GL}(n, \mathbb{R}) \quad \text{o} \quad \text{GL}(n, \mathbb{C})$$
> y consiste en todas las matrices $n \times n$ invertibles.

## 💎 Ejemplos Resueltos Detallados

> [!example]- Cálculo de Inversas Directamente
> **EJEMPLO 1: Inversa en ℝ²**
>
> Sea $T: \mathbb{R}^2 \to \mathbb{R}^2$ definida por:
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 2x + y \\ x + 3y \end{bmatrix}$$
>
> Determinar si $T$ es invertible y, si lo es, encontrar $T^{-1}$.
>
> **SOLUCIÓN:**
>
> **Método 1: Verificación directa**
>
> **Paso 1: Encontrar la matriz de T**
>
> $$A = [T] = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$$
>
> **Paso 2: Verificar invertibilidad**
>
> $$\det(A) = (2)(3) - (1)(1) = 6 - 1 = 5 \neq 0$$
>
> Como $\det(A) \neq 0$: $$\boxed{T \text{ es invertible}} \text{ ✓}$$
>
> **Paso 3: Calcular A⁻¹**
>
> Fórmula para matriz $2 \times 2$:
> $$A^{-1} = \frac{1}{\det(A)}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
>
> donde $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$
>
> $$A^{-1} = \frac{1}{5}\begin{bmatrix} 3 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 3/5 & -1/5 \\ -1/5 & 2/5 \end{bmatrix}$$
>
> **Paso 4: Expresar T⁻¹**
>
> $$\boxed{T^{-1}\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} \frac{3x - y}{5} \\ \frac{-x + 2y}{5} \end{bmatrix}}$$
>
> **Método 2: Resolver sistema**
>
> Si $T^{-1}\begin{pmatrix}\begin{bmatrix} u \\ v \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \\ y \end{bmatrix}$, entonces:
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} u \\ v \end{bmatrix}$$
>
> Es decir:
> $$\begin{cases}
> 2x + y = u \\
> x + 3y = v
> \end{cases}$$
>
> Resolver para $x, y$ en términos de $u, v$:
>
> De la primera: $y = u - 2x$
>
> Sustituir en la segunda:
> $$x + 3(u - 2x) = v$$
> $$x + 3u - 6x = v$$
> $$-5x = v - 3u$$
> $$x = \frac{3u - v}{5}$$
>
> Por tanto:
> $$y = u - 2x = u - 2\left(\frac{3u - v}{5}\right) = \frac{5u - 6u + 2v}{5} = \frac{-u + 2v}{5}$$
>
> Resultado idéntico ✓
>
> **Verificación:**
>
> $$(T \circ T^{-1})\begin{pmatrix}\begin{bmatrix} u \\ v \end{bmatrix}\end{pmatrix} = T\begin{pmatrix}\begin{bmatrix} \frac{3u - v}{5} \\ \frac{-u + 2v}{5} \end{bmatrix}\end{pmatrix}$$
>
> $$= \begin{bmatrix} 2\cdot\frac{3u - v}{5} + \frac{-u + 2v}{5} \\ \frac{3u - v}{5} + 3\cdot\frac{-u + 2v}{5} \end{bmatrix} = \begin{bmatrix} \frac{6u - 2v - u + 2v}{5} \\ \frac{3u - v - 3u + 6v}{5} \end{bmatrix}$$
>
> $$= \begin{bmatrix} \frac{5u}{5} \\ \frac{5v}{5} \end{bmatrix} = \begin{bmatrix} u \\ v \end{bmatrix}$$ ✓
>
> ---
>
> **EJEMPLO 2: Transformación en espacio de polinomios**
>
> Sea $T: \mathcal{P}_2 \to \mathcal{P}_2$ definida por:
> $$T(a_0 + a_1x + a_2x^2) = (a_0 + a_1) + (a_1 + a_2)x + a_2x^2$$
>
> Determinar si $T$ es invertible y encontrar $T^{-1}$ si existe.
>
> **SOLUCIÓN:**
>
> **Paso 1: Encontrar matriz respecto a base estándar**
>
> Base estándar: $\mathcal{B} = \{1, x, x^2\}$
>
> $$T(1) = 1 = 1 \cdot 1 + 0 \cdot x + 0 \cdot x^2 \implies [T(1)]_{\mathcal{B}} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$$
>
> $$T(x) = 1 + x = 1 \cdot 1 + 1 \cdot x + 0 \cdot x^2 \implies [T(x)]_{\mathcal{B}} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$$
<
> $$T(x^2) = x + x^2 = 0 \cdot 1 + 1 \cdot x + 1 \cdot x^2 \implies [T(x^2)]_{\mathcal{B}} = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$$
>
> Matriz de $T$:
> $$A = [T]_{\mathcal{B}} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$$
>
> **Paso 2: Verificar invertibilidad**
>
> Matriz triangular superior, por tanto:
> $$\det(A) = (1)(1)(1) = 1 \neq 0$$
>
> $$\boxed{T \text{ es invertible}} \text{ ✓}$$
>
> **Paso 3: Calcular A⁻¹**
>
> Por eliminación gaussiana o fórmula directa:
>
> $$A^{-1} = \begin{bmatrix} 1 & -1 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$
>
> **Verificación rápida:**
> $$AA^{-1} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$ ✓
>
> **Paso 4: Expresar T⁻¹**
>
> Si $p(x) = b_0 + b_1x + b_2x^2$, entonces:
>
> $$[T^{-1}(p)]_{\mathcal{B}} = A^{-1}[p]_{\mathcal{B}} = \begin{bmatrix} 1 & -1 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} b_0 \\ b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} b_0 - b_1 + b_2 \\ b_1 - b_2 \\ b_2 \end{bmatrix}$$
>
> Por tanto:
>
> $$\boxed{T^{-1}(b_0 + b_1x + b_2x^2) = (b_0 - b_1 + b_2) + (b_1 - b_2)x + b_2x^2}$$
>
> **Verificación:**
>
> Sea $p(x) = 2 + 3x + 5x^2$
>
> $$T^{-1}(p) = (2 - 3 + 5) + (3 - 5)x + 5x^2 = 4 - 2x + 5x^2$$
>
> Aplicar $T$:
> $$T(4 - 2x + 5x^2) = (4 + (-2)) + ((-2) + 5)x + 5x^2 = 2 + 3x + 5x^2 = p(x)$$ ✓
>
> ---
>
> **EJEMPLO 3: Transformación no invertible**
>
> Sea $T: \mathbb{R}^3 \to \mathbb{R}^3$ definida por:
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y \\ 2x + 2y \\ z \end{bmatrix}$$
>
> ¿Es $T$ invertible?
>
> **SOLUCIÓN:**
>
> **Matriz de T:**
> $$A = \begin{bmatrix} 1 & 1 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
>
> **Calcular determinante:**
>
> Expandir por tercera columna:
> $$\det(A) = 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix} = 1 \cdot (2 - 2) = 0$$
>
> Como $\det(A) = 0$:
>
> $$\boxed{T \text{ NO es invertible}} \text{ ✗}$$
>
> **Verificación por núcleo:**
>
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
>
> $$\begin{cases}
> x + y = 0 \\
> 2x + 2y = 0 \\
> z = 0
> \end{cases}$$
>
> Solución: $y = -x$, $z = 0$
>
> $$\text{Ker}(T) = \left\{\begin{bmatrix} t \\ -t \\ 0 \end{bmatrix} : t \in \mathbb{R}\right\} = \text{span}\left\{\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}\right\}$$
>
> $$\text{nullity}(T) = 1 \neq 0$$
>
> Por tanto $T$ no es inyectiva ⇒ no invertible ✓

> [!example]- Inversas de Composiciones
> **EJEMPLO 4: Composición de rotaciones**
>
> Sean $R_{\theta}: \mathbb{R}^2 \to \mathbb{R}^2$ y $R_{\phi}: \mathbb{R}^2 \to \mathbb{R}^2$ rotaciones con matrices:
>
> $$[R_{\theta}] = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}, \quad [R_{\phi}] = \begin{bmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{bmatrix}$$
>
> Encontrar $(R_{\phi} \circ R_{\theta})^{-1}$.
>
> **SOLUCIÓN:**
>
> **Método 1: Usando teorema de composición**
>
> Por Teorema 2:
> $$\boxed{(R_{\phi} \circ R_{\theta})^{-1} = R_{\theta}^{-1} \circ R_{\phi}^{-1}}$$
>
> **Encontrar inversas individuales:**
>
> Una rotación por ángulo $\alpha$ tiene inversa la rotación por $-\alpha$:
>
> $$R_{\theta}^{-1} = R_{-\theta}, \quad R_{\phi}^{-1} = R_{-\phi}$$
>
> Por tanto:
> $$(R_{\phi} \circ R_{\theta})^{-1} = R_{-\theta} \circ R_{-\phi} = R_{-\theta - \phi} = R_{-(\theta + \phi)}$$
>
> **Matriz:**
> $$\boxed{[(R_{\phi} \circ R_{\theta})^{-1}] = \begin{bmatrix} \cos(-(\theta+\phi)) & -\sin(-(\theta+\phi)) \\ \sin(-(\theta+\phi)) & \cos(-(\theta+\phi)) \end{bmatrix}}$$
>
> $$= \begin{bmatrix} \cos(\theta+\phi) & \sin(\theta+\phi) \\ -\sin(\theta+\phi) & \cos(\theta+\phi) \end{bmatrix}$$
>
> **Método 2: Cálculo directo**
>
> $$[R_{\phi} \circ R_{\theta}] = [R_{\phi}][R_{\theta}]$$
>
> $$= \begin{bmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{bmatrix}\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
>
> $$= \begin{bmatrix} \cos\phi\cos\theta - \sin\phi\sin\theta & -\cos\phi\sin\theta - \sin\phi\cos\theta \\ \sin\phi\cos\theta + \cos\phi\sin\theta & -\sin\phi\sin\theta + \cos\phi\cos\theta \end{bmatrix}$$
>
> $$= \begin{bmatrix} \cos(\phi+\theta) & -\sin(\phi+\theta) \\ \sin(\phi+\theta) & \cos(\phi+\theta) \end{bmatrix}$$
>
> Inversa (transpuesta para matrices de rotación):
> $$= \begin{bmatrix} \cos(\phi+\theta) & \sin(\phi+\theta) \\ -\sin(\phi+\theta) & \cos(\phi+\theta) \end{bmatrix}$$
>
> Resultado idéntico ✓
>
> ---
>
> **EJEMPLO 5: Inversa de producto de transformaciones**
>
> Sean $S: \mathbb{R}^2 \to \mathbb{R}^2$ reflexión sobre el eje $x$ y $T: \mathbb{R}^2 \to \mathbb{R}^2$ escalamiento por factor 2.
>
> $$[S] = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}, \quad [T] = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$$
>
> Encontrar $(T \circ S)^{-1}$ y verificar.
>
> **SOLUCIÓN:**
>
> **Paso 1: Encontrar inversas individuales**
>
> $$S^{-1} = S \quad \text{(reflexión es su propia inversa)}$$
> $$[S^{-1}] = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
>
> $$[T^{-1}] = \begin{bmatrix} 1/2 & 0 \\ 0 & 1/2 \end{bmatrix}$$
>
> **Paso 2: Aplicar teorema**
>
> $$(T \circ S)^{-1} = S^{-1} \circ T^{-1}$$
>
> $$[(T \circ S)^{-1}] = [S^{-1}][T^{-1}] = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\begin{bmatrix} 1/2 & 0 \\ 0 & 1/2 \end{bmatrix}$$
>
> $$\boxed{[(T \circ S)^{-1}] = \begin{bmatrix} 1/2 & 0 \\ 0 & -1/2 \end{bmatrix}}$$
>
> **Verificación:**
>
> $$[T \circ S] = [T][S] = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}$$
>
> $$[T \circ S] \cdot [(T \circ S)^{-1}] = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}\begin{bmatrix} 1/2 & 0 \\ 0 & -1/2 \end{bmatrix}$$
>
> $$= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$ ✓

> [!example]- Aplicaciones Prácticas
> **EJEMPLO 6: Cambio de coordenadas**
>
> En $\mathbb{R}^2$, considerar dos bases:
> - Base estándar: $\mathcal{E} = \{\vec{e}_1, \vec{e}_2\}$ donde $\vec{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, $\vec{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$
> - Base alternativa: $\mathcal{B} = \{\vec{b}_1, \vec{b}_2\}$ donde $\vec{b}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$, $\vec{b}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$
>
> Encontrar la transformación que convierte coordenadas de $\mathcal{B}$ a $\mathcal{E}$ y su inversa.
>
> **SOLUCIÓN:**
>
> **Paso 1: Matriz de cambio de base**
>
> La matriz $P$ cuyas columnas son los vectores de $\mathcal{B}$ expresados en $\mathcal{E}$:
>
> $$P = [\vec{b}_1 \mid \vec{b}_2] = \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$$
>
> Esta matriz convierte de coordenadas $\mathcal{B}$ a coordenadas $\mathcal{E}$:
> $$[\vec{v}]_{\mathcal{E}} = P[\vec{v}]_{\mathcal{B}}$$
>
> **Paso 2: Calcular P⁻¹**
>
> $$\det(P) = (1)(-1) - (1)(1) = -1 - 1 = -2 \neq 0$$
>
> $$P^{-1} = \frac{1}{-2}\begin{bmatrix} -1 & -1 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{bmatrix}$$
>
> Esta matriz convierte de coordenadas $\mathcal{E}$ a coordenadas $\mathcal{B}$:
> $$\boxed{[\vec{v}]_{\mathcal{B}} = P^{-1}[\vec{v}]_{\mathcal{E}}}$$
>
> **Ejemplo numérico:**
>
> Sea $\vec{v} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$ en base estándar.
>
> Sus coordenadas en base $\mathcal{B}$:
> $$[\vec{v}]_{\mathcal{B}} = P^{-1}\begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 1/2 & 1/2 \\ 1/2 & -1/2 \end{bmatrix}\begin{bmatrix} 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$
>
> **Verificación:**
> $$2\vec{b}_1 + 1\vec{b}_2 = 2\begin{bmatrix} 1 \\ 1 \end{bmatrix} + \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} = \vec{v}$$ ✓
>
> ---
>
> **EJEMPLO 7: Codificación y decodificación**
>
> En criptografía simple, se usa matriz de codificación $C: \mathbb{R}^2 \to \mathbb{R}^2$:
>
> $$[C] = \begin{bmatrix} 3 & 2 \\ 5 & 4 \end{bmatrix}$$
>
> Codificar el mensaje $\vec{m} = \begin{bmatrix} 7 \\ 11 \end{bmatrix}$ y luego decodificarlo.
>
> **SOLUCIÓN:**
>
> **Codificación:**
> $$\vec{c} = C(\vec{m}) = \begin{bmatrix} 3 & 2 \\ 5 & 4 \end{bmatrix}\begin{bmatrix} 7 \\ 11 \end{bmatrix} = \begin{bmatrix} 21 + 22 \\ 35 + 44 \end{bmatrix} = \begin{bmatrix} 43 \\ 79 \end{bmatrix}$$
>
> **Decodificación (necesitamos C⁻¹):**
>
> $$\det(C) = (3)(4) - (2)(5) = 12 - 10 = 2 \neq 0$$
>
> $$[C^{-1}] = \frac{1}{2}\begin{bmatrix} 4 & -2 \\ -5 & 3 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ -5/2 & 3/2 \end{bmatrix}$$
>
> Aplicar $C^{-1}$ al mensaje codificado:
> $$\vec{m} = C^{-1}(\vec{c}) = \begin{bmatrix} 2 & -1 \\ -5/2 & 3/2 \end{bmatrix}\begin{bmatrix} 43 \\ 79 \end{bmatrix}$$
>
> $$= \begin{bmatrix} 86 - 79 \\ -215/2 + 237/2 \end{bmatrix} = \begin{bmatrix} 7 \\ 11 \end{bmatrix}$$ ✓
>
> Mensaje original recuperado correctamente.

## 🎭 Métodos de Cálculo

> [!tip]- Técnicas para Encontrar Inversas
> **MÉTODO 1: Inversión de matrices (casos pequeños)**
>
> Para matrices $2 \times 2$:
> $$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies A^{-1} = \frac{1}{ad - bc}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$
>
> **Requisito:** $\det(A) = ad - bc \neq 0$
>
> ---
>
> **MÉTODO 2: Eliminación Gaussiana (Gauss-Jordan)**
>
> Para matriz $n \times n$:
>
> 1. Formar matriz aumentada $[A \mid I]$
> 2. Aplicar operaciones elementales de fila
> 3. Reducir a $[I \mid A^{-1}]$
>
> **Ejemplo:** Invertir $A = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 2 & 0 & 1 \end{bmatrix}$
>
> $$\left[\begin{array}{ccc|ccc} 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 3 & 0 & 1 & 0 \\ 2 & 0 & 1 & 0 & 0 & 1 \end{array}\right]$$
>
> Después de operaciones:
> $$\left[\begin{array}{ccc|ccc} 1 & 0 & 0 & -1/10 & 1/5 & -3/5 \\ 0 & 1 & 0 & -3/5 & -1/10 & 3/10 \\ 0 & 0 & 1 & 1/5 & -2/5 & -1/10 \end{array}\right]$$
>
> $$\boxed{A^{-1} = \begin{bmatrix} -1/10 & 1/5 & -3/5 \\ -3/5 & -1/10 & 3/10 \\ 1/5 & -2/5 & -1/10 \end{bmatrix}}$$
>
> ---
>
> **MÉTODO 3: Matriz adjunta (cofactores)**
>
> Para cualquier matriz $n \times n$ invertible:
>
> $$A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$$
>
> donde $\text{adj}(A)$ es la **matriz adjunta** (transpuesta de la matriz de cofactores).
>
> **Pasos:**
> 4. Calcular $\det(A)$ (verificar $\neq 0$)
> 5. Calcular matriz de cofactores $C_{ij} = (-1)^{i+j}M_{ij}$
> 6. Transponer: $\text{adj}(A) = (C_{ij})^T$
> 7. Dividir: $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$
>
> **Útil para:** Cálculos simbólicos, matrices pequeñas
>
> ---
>
> **MÉTODO 4: Descomposición LU**
>
> Si $A = LU$ (factorización LU):
>
> Para resolver $A\vec{x} = \vec{b}$:
> 8. Resolver $L\vec{y} = \vec{b}$ (sustitución hacia adelante)
> 9. Resolver $U\vec{x} = \vec{y}$ (sustitución hacia atrás)
>
> Para múltiples vectores $\vec{b}$, esto es eficiente.
>
> ---
>
> **MÉTODO 5: Resolución de sistemas**
>
> Si $T(\vec{v}) = \vec{w}$, resolver para $\vec{v}$ en términos de $\vec{w}$:
>
> $$T^{-1}(\vec{w}) = \vec{v}$$
>
> **Útil para:** Transformaciones con fórmulas explícitas

## 📐 Propiedades Algebraicas Adicionales

> [!note]- Álgebra de Transformaciones Inversas
> **PROPIEDAD 1: Involución**
> $$\boxed{(T^{-1})^{-1} = T}$$
>
> La inversa de la inversa es la transformación original.
>
> ---
>
> **PROPIEDAD 2: Identidad como su propia inversa**
> $$\boxed{\text{Id}_V^{-1} = \text{Id}_V}$$
>
> ---
>
> **PROPIEDAD 3: Inversa de un múltiplo escalar**
>
> Si $c \neq 0$ y $T$ invertible:
> $$\boxed{(cT)^{-1} = \frac{1}{c}T^{-1}}$$
>
> **Demostración:**
> $$(cT) \circ \left(\frac{1}{c}T^{-1}\right) = c \cdot \frac{1}{c}(T \circ T^{-1}) = \text{Id}$$ ✓
>
> ---
>
> **PROPIEDAD 4: Inversa de potencias**
>
> Si $T$ invertible y $n \in \mathbb{Z}^+$:
> $$\boxed{(T^n)^{-1} = (T^{-1})^n}$$
>
> **Notación:** Se escribe $T^{-n} = (T^{-1})^n$
>
> ---
>
> **PROPIEDAD 5: Conmutatividad con la inversa**
>
> Si $T$ y $S$ conmutan y ambas son invertibles:
> $$TS = ST \implies T^{-1}S^{-1} = S^{-1}T^{-1}$$
>
> **Demostración:**
> $$T^{-1}S^{-1} = (ST)^{-1} = (TS)^{-1} = S^{-1}T^{-1}$$ ✓
>
> ---
>
> **PROPIEDAD 6: Preservación de determinantes**
>
> Si $A$ es matriz de $T$ invertible:
> $$\boxed{\det(A^{-1}) = \frac{1}{\det(A)}}$$
>
> **Demostración:**
> $$\det(A)\det(A^{-1}) = \det(AA^{-1}) = \det(I) = 1$$ ✓
>
> ---
>
> **PROPIEDAD 7: Traza de la inversa**
>
> En general: $\text{tr}(A^{-1}) \neq \frac{1}{\text{tr}(A)}$
>
> **Contraejemplo:**
> $$A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}, \quad A^{-1} = \begin{bmatrix} 1/2 & 0 \\ 0 & 1/3 \end{bmatrix}$$
>
> $$\text{tr}(A) = 5, \quad \text{tr}(A^{-1}) = \frac{5}{6} \neq \frac{1}{5}$$

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes
> **1. "T⁻¹ significa 1/T"**
>
> ❌ **FALSO**
>
> El exponente -1 **NO** significa división o recíproco.
>
> Es **notación** para la transformación inversa que satisface:
> $$T^{-1} \circ T = \text{Id}$$
>
> No existe "1 dividido entre una transformación".
>
> ---
>
> **2. "Toda transformación lineal tiene inversa"**
>
> ❌ **FALSO**
>
> Solo las **biyectivas** (isomorfismos) tienen inversa.
>
> **Contraejemplo:** Proyección $P: \mathbb{R}^3 \to \mathbb{R}^2$
> - Lineal ✓
> - No inyectiva (dimensiones diferentes)
> - No tiene inversa ✗
>
> ---
>
> **3. "Si det(A) ≠ 0, entonces A⁻¹ = 1/det(A)"**
>
> ❌ **FALSO** (confusión grave)
>
> ✅ **CORRECTO:** 
> $$A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$$
>
> El determinante es solo un **factor escalar**, no la inversa completa.
>
> ---
>
> **4. "(S ∘ T)⁻¹ = S⁻¹ ∘ T⁻¹"**
>
> ❌ **FALSO** (orden incorrecto)
>
> ✅ **CORRECTO:**
> $$\boxed{(S \circ T)^{-1} = T^{-1} \circ S^{-1}}$$
>
> El orden se **invierte**.
>
> **Analogía:** Ponerse calcetines y luego zapatos:
> - Para deshacer: quitar zapatos primero, luego calcetines
>
> ---
>
> **5. "Si T tiene inversa, entonces [T⁻¹] = [T]⁻¹ en cualquier base"**
>
> ⚠️ **CUIDADO CON LA NOTACIÓN**
>
> ✅ **CORRECTO:** Para bases fijas $\mathcal{B}_V$ y $\mathcal{B}_W$:
> $$[T^{-1}]_{\mathcal{B}_W}^{\mathcal{B}_V} = \left([T]_{\mathcal{B}_V}^{\mathcal{B}_W}\right)^{-1}$$
>
> Pero las bases deben ser las mismas (en orden inverso).
>
> ---
>
> **6. "T invertible implica que T² = I"**
>
> ❌ **FALSO**
>
> Ser invertible no significa ser **involutiva** (su propia inversa).
>
> **Contraejemplo:** Rotación por $90°$
> - Invertible ✓
> - $R_{90}^2 = R_{180} \neq I$ ✗
> - $R_{90}^{-1} = R_{-90} = R_{270} \neq R_{90}$
>
> Solo algunas transformaciones invertibles son involutivas (como reflexiones).
>
> ---
>
> **7. "Calcular A⁻¹ multiplicando A por I"**
>
> ❌ **NO FUNCIONA**
>
> $$A \cdot I = A \neq A^{-1}$$
>
> ✅ **MÉTODO CORRECTO:** Gauss-Jordan $[A \mid I] \to [I \mid A^{-1}]$
>
> ---
>
> **8. "Si T no es sobreyectiva, entonces T⁻¹ existe parcialmente"**
>
> ❌ **FALSO** (concepto confuso)
>
> Si $T$ no es biyectiva, $T^{-1}$ **no existe** como transformación lineal.
>
> ⚠️ **NOTA:** Existe el concepto de **pseudoinversa** (Moore-Penrose) para casos no invertibles, pero es diferente y más avanzado.
>
> ---
>
> **9. "A⁻¹ se puede calcular siempre dividiendo"**
>
> ❌ **FALSO**
>
> No existe "división de matrices" en el sentido usual.
>
> ✅ **CORRECTO:** Resolver $AX = I$ para encontrar $X = A^{-1}$
>
> O usar métodos: Gauss-Jordan, adjunta, descomposición LU, etc.
>
> ---
>
> **10. "tr(A⁻¹) = 1/tr(A)"**
>
> ❌ **FALSO** (propiedad que NO se cumple)
>
> La traza no se comporta así con inversas.
>
> **Contraejemplo ya visto:** $A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$

## 🔍 Casos Especiales Importantes

> [!note]- Transformaciones con Propiedades Especiales
> **CASO 1: Transformaciones Ortogonales**
>
> Una transformación $T: \mathbb{R}^n \to \mathbb{R}^n$ es **ortogonal** si preserva el producto interno:
> $$\langle T(\vec{u}), T(\vec{v}) \rangle = \langle \vec{u}, \vec{v} \rangle$$
>
> **Propiedad de inversa:**
> $$\boxed{T \text{ ortogonal} \implies T^{-1} = T^*}$$
>
> donde $T^*$ es la **transpuesta** (o adjunta).
>
> En términos matriciales: $A^{-1} = A^T$
>
> **Ejemplos:** Rotaciones, reflexiones
>
> ---
>
> **CASO 2: Transformaciones Involutivas**
>
> Una transformación es **involutiva** si:
> $$\boxed{T^2 = \text{Id} \implies T^{-1} = T}$$
>
> Es decir, es su propia inversa.
>
> **Ejemplos:**
> - Reflexiones sobre ejes o planos
> - Negación: $T(\vec{v}) = -\vec{v}$ (con $T^2 = \text{Id}$)
> - Conjugación compleja: $T(z) = \bar{z}$
>
> **Caracterización matricial:** $A^2 = I$
>
> ---
>
> **CASO 3: Transformaciones Unitarias (espacios complejos)**
>
> Para $T: \mathbb{C}^n \to \mathbb{C}^n$ unitaria:
> $$\boxed{T^{-1} = T^*}$$
>
> donde $T^*$ es la **adjunta hermítica** (transpuesta conjugada).
>
> En matrices: $A^{-1} = A^* = \overline{A^T}$
>
> ---
>
> **CASO 4: Transformaciones Diagonales**
>
> Si $D = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$ con todos $\lambda_i \neq 0$:
>
> $$\boxed{D^{-1} = \text{diag}(1/\lambda_1, 1/\lambda_2, \ldots, 1/\lambda_n)}$$
>
> **Muy fácil de invertir:** Solo invertir elementos diagonales.
>
> ---
>
> **CASO 5: Transformaciones Triangulares**
>
> Matrices triangulares (superior o inferior) con elementos diagonales no nulos son invertibles.
>
> Su inversa también es triangular del mismo tipo.
>
> **Ejemplo:**
> $$A = \begin{bmatrix} 2 & 3 & 1 \\ 0 & 1 & 4 \\ 0 & 0 & 5 \end{bmatrix} \implies A^{-1} = \begin{bmatrix} 1/2 & -3/2 & 11/10 \\ 0 & 1 & -4/5 \\ 0 & 0 & 1/5 \end{bmatrix}$$
>
> (Triangular superior ⇒ inversa triangular superior)
>
> ---
>
> **CASO 6: Permutaciones**
>
> Una matriz de permutación $P$ siempre es invertible y:
> $$\boxed{P^{-1} = P^T}$$
>
> **Ejemplo:**
> $$P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix} \implies P^{-1} = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix} = P^T$$

## 🎯 Aplicaciones Importantes

> [!tip]- Aplicaciones en Diversas Áreas
> **APLICACIÓN 1: Sistemas de ecuaciones lineales**
>
> Si $A$ es invertible, el sistema $A\vec{x} = \vec{b}$ tiene **solución única**:
> $$\boxed{\vec{x} = A^{-1}\vec{b}}$$
>
> **Ventaja computacional:** Si se resuelven muchos sistemas con la misma $A$ pero diferentes $\vec{b}$, calcular $A^{-1}$ una vez es eficiente.
>
> ---
>
> **APLICACIÓN 2: Gráficos por computadora (transformaciones inversas)**
>
> - **Transformación directa:** Rotar, escalar, trasladar objetos
> - **Transformación inversa:** Determinar posición original
>
> **Ejemplo:** Ray tracing requiere transformaciones inversas para:
> - Convertir coordenadas de pantalla a coordenadas de mundo
> - Intersección de rayos con objetos transformados
>
> ---
>
> **APLICACIÓN 3: Criptografía (cifrado Hill)**
>
> **Cifrado:** $\vec{c} = K\vec{m}$ (donde $K$ es matriz clave)
> **Descifrado:** $\vec{m} = K^{-1}\vec{c}$
>
> Requiere que $K$ sea invertible (típicamente $\det(K) \neq 0 \pmod{26}$)
>
> ---
>
> **APLICACIÓN 4: Cambio de coordenadas en física**
>
> **Ejemplo:** Cambio entre sistemas de referencia
>
> - Sistema 1 → Sistema 2: $\vec{v}_2 = P\vec{v}_1$
> - Sistema 2 → Sistema 1: $\vec{v}_1 = P^{-1}\vec{v}_2$
>
> En mecánica cuántica: transformaciones unitarias (inversas = adjuntas)
>
> ---
>
> **APLICACIÓN 5: Análisis de redes (teoría de grafos)**
>
> La **matriz de adyacencia** de un grafo, si es invertible, permite:
> - Calcular número de caminos entre nodos
> - Análisis de conectividad
> - PageRank de Google (usa inversas aproximadas)
>
> ---
>
> **APLICACIÓN 6: Control de sistemas (retroalimentación)**
>
> En teoría de control, el **controlador inverso** cancela la dinámica del sistema:
>
> $$\text{Sistema: } y = Gu \quad \implies \quad \text{Control: } u = G^{-1}y_{\text{deseado}}$$
>
> Requiere que el sistema $G$ sea invertible (estabilidad).
>
> ---
>
> **APLICACIÓN 7: Machine Learning (normalización inversa)**
>
> **Normalización:** $\vec{x}_{\text{norm}} = S\vec{x} + \vec{b}$
> **Desnormalización:** $\vec{x} = S^{-1}(\vec{x}_{\text{norm}} - \vec{b})$
>
> Común en:
> - Preprocesamiento de datos
> - Normalizing flows (modelos generativos)
> - Redes neuronales invertibles (i-RevNet, Glow)
>
> ---
>
> **APLICACIÓN 8: Resolución de ecuaciones diferenciales**
>
> Método de matriz exponencial para EDOs lineales:
> $$\frac{d\vec{x}}{dt} = A\vec{x} \implies \vec{x}(t) = e^{At}\vec{x}_0$$
>
> Si $A$ invertible: $e^{At}$ siempre invertible con $(e^{At})^{-1} = e^{-At}$
>
> ---
>
> **APLICACIÓN 9: Procesamiento de señales (filtros inversos)**
>
> **Filtro:** $y = H \ast x$ (convolución)
> **Deconvolución:** $x = H^{-1} \ast y$
>
> Usado en:
> - Restauración de imágenes borrosas
> - Ecualización de audio
> - Corrección de distorsión

## 📊 Tabla de Referencia Rápida

> [!note]- Guía de Consulta
> **CONDICIONES DE INVERTIBILIDAD:**
>
> | Condición | Equivalencia |
> |-----------|--------------|
> | $T$ invertible | $\exists T^{-1}: T^{-1} \circ T = \text{Id}_V$, $T \circ T^{-1} = \text{Id}_W$ |
> | | $T$ es biyectiva |
> | | $T$ es isomorfismo |
> | | $\text{Ker}(T) = \{\vec{0}\}$ y $\text{Im}(T) = W$ |
> | | $\dim(V) = \dim(W)$ y $T$ inyectiva (o sobreyectiva) |
> | | $\det([T]) \neq 0$ (si matrices cuadradas) |
>
> **PROPIEDADES DE INVERSAS:**
>
> | Propiedad | Fórmula |
> |-----------|---------|
> | Unicidad | Si existe, $T^{-1}$ es única |
> | Linealidad | $T^{-1}$ es transformación lineal |
> | Involución | $(T^{-1})^{-1} = T$ |
> | Identidad | $\text{Id}_V^{-1} = \text{Id}_V$ |
> | Composición | $(S \circ T)^{-1} = T^{-1} \circ S^{-1}$ |
> | Múltiplo escalar | $(cT)^{-1} = \frac{1}{c}T^{-1}$ (si $c \neq 0$) |
> | Potencias | $(T^n)^{-1} = (T^{-1})^n$ |
> | Matriz | $[T^{-1}]_{\mathcal{B}_W}^{\mathcal{B}_V} = ([T]_{\mathcal{B}_V}^{\mathcal{B}_W})^{-1}$ |
>
> **INVERSAS ESPECIALES:**
>
> | Tipo | Propiedad de Inversa |
> |------|---------------------|
> | Ortogonal | $T^{-1} = T^*$ (transpuesta) |
> | Unitaria | $T^{-1} = T^*$ (adjunta hermítica) |
> | Involutiva | $T^{-1} = T$ (propia inversa) |
> | Diagonal | Invertir elementos diagonales |
> | Permutación | $P^{-1} = P^T$ |
>
> **MÉTODOS DE CÁLCULO:**
>
> | Método | Mejor para |
> |--------|-----------|
> | Fórmula $2 \times 2$ | Matrices pequeñas |
> | Gauss-Jordan | Matrices numéricas generales |
> | Adjunta/cofactores | Matrices simbólicas pequeñas |
> | Descomposición LU | Múltiples sistemas |
> | Resolución directa | Transformaciones con fórmulas explícitas |

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales
> **Fundamentos previos:**
> - [[01 - Transformaciones lineales]] - Definición básica
> - [[02 - Núcleo e Imagen]] - Caracterización de inyectividad
> - [[03 - Inyectividad y sobreyectividad]] - Biyectividad
> - [[04 - Biyectividad e isomorfismo]] - Equivalencia con isomorfismo
>
> **Temas directamente relacionados:**
> - [[06 - Matriz de una transformación]] - Representación matricial
> - [[07 - Composición de transformaciones]] - $(S \circ T)^{-1} = T^{-1} \circ S^{-1}$
> - [[08 - Matriz inversa]] - Inversión de matrices
> - [[09 - Cambio de base]] - Matrices de cambio son invertibles
> - [[10 - Determinantes]] - Criterio $\det \neq 0$
>
> **Aplicaciones posteriores:**
> - [[15 - Valores propios]] - Matriz $A - \lambda I$ invertible ⟺ $\lambda$ no es valor propio
> - [[16 - Diagonalización]] - $P^{-1}AP = D$
> - [[20 - Forma de Jordan]] - Similitud vía invertibles
> - [[25 - Descomposición SVD]] - Pseudoinversa
> - [[30 - Teorema espectral]] - Transformaciones unitarias
>
> **Temas avanzados:**
> - [[35 - Operadores adjuntos]] - Relación con inversas
> - [[40 - Grupos de Lie]] - GL(n) como grupo de Lie
> - [[45 - Análisis funcional]] - Operadores inversibles acotados
> - [[50 - Teorema del mapeo abierto]] - Inversa acotada de operador acotado

## 🧮 Ejercicios Resueltos Adicionales

> [!example]- Problemas de Práctica
> **EJERCICIO 1: Verificación de inversa**
>
> Verificar que $T: \mathbb{R}^3 \to \mathbb{R}^3$ y $S: \mathbb{R}^3 \to \mathbb{R}^3$ son inversas una de otra:
>
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y \\ y + z \\ z + x \end{bmatrix}, \quad S\begin{pmatrix}\begin{bmatrix} a \\ b \\ c \end{bmatrix}\end{pmatrix} = \begin{bmatrix} (a - b + c)/2 \\ (a + b - c)/2 \\ (-a + b + c)/2 \end{bmatrix}$$
>
> **SOLUCIÓN:**
>
> Necesitamos verificar: $S \circ T = \text{Id}$ y $T \circ S = \text{Id}$
>
> **Verificar S ∘ T:**
>
> $$(S \circ T)\begin{pmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix}\end{pmatrix} = S\begin{pmatrix}\begin{bmatrix} x + y \\ y + z \\ z + x \end{bmatrix}\end{pmatrix}$$
>
> $$= \begin{bmatrix} \frac{(x+y) - (y+z) + (z+x)}{2} \\ \frac{(x+y) + (y+z) - (z+x)}{2} \\ \frac{-(x+y) + (y+z) + (z+x)}{2} \end{bmatrix}$$
>
> $$= \begin{bmatrix} \frac{2x}{2} \\ \frac{2y}{2} \\ \frac{2z}{2} \end{bmatrix} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$$ ✓
>
> **Verificar T ∘ S:**
>
> $$(T \circ S)\begin{pmatrix}\begin{bmatrix} a \\ b \\ c \end{bmatrix}\end{pmatrix} = T\begin{pmatrix}\begin{bmatrix} (a-b+c)/2 \\ (a+b-c)/2 \\ (-a+b+c)/2 \end{bmatrix}\end{pmatrix}$$
>
> $$= \begin{bmatrix} \frac{a-b+c}{2} + \frac{a+b-c}{2} \\ \frac{a+b-c}{2} + \frac{-a+b+c}{2} \\ \frac{-a+b+c}{2} + \frac{a-b+c}{2} \end{bmatrix}$$
>
> $$= \begin{bmatrix} \frac{2a}{2} \\ \frac{2b}{2} \\ \frac{2c}{2} \end{bmatrix} = \begin{bmatrix} a \\ b \\ c \end{bmatrix}$$ ✓
>
> $$\boxed{S = T^{-1} \text{ y } T = S^{-1}}$$
>
> ---
>
> **EJERCICIO 2: Inversa de transformación de derivación restringida**
>
> Sea $D: \mathcal{P}_3 \to \mathcal{P}_2$ la derivada, y sea $I: \mathcal{P}_2 \to \mathcal{P}_3$ definida por:
> $$I(p(x)) = \int_0^x p(t)\,dt$$
>
> ¿Son $D$ e $I$ inversas una de otra?
>
> **SOLUCIÓN:**
>
> **Verificar I ∘ D:**
>
> Para $p(x) = a_0 + a_1x + a_2x^2 + a_3x^3 \in \mathcal{P}_3$:
>
> $$D(p) = a_1 + 2a_2x + 3a_3x^2$$
>
> $$I(D(p)) = \int_0^x (a_1 + 2a_2t + 3a_3t^2)\,dt = a_1x + a_2x^2 + a_3x^3$$
>
> **NO es igual a $p(x)$** porque falta el término constante $a_0$.
>
> $$(I \circ D)(p) = p(x) - a_0 \neq p(x) \quad \text{si } a_0 \neq 0$$
>
> **Verificar D ∘ I:**
>
> Para $q(x) = b_0 + b_1x + b_2x^2 \in \mathcal{P}_2$:
>
> $$I(q) = \int_0^x (b_0 + b_1t + b_2t^2)\,dt = b_0x + \frac{b_1x^2}{2} + \frac{b_2x^3}{3}$$
>
> $$D(I(q)) = b_0 + b_1x + b_2x^2 = q(x)$$ ✓
>
> **CONCLUSIÓN:**
> $$\boxed{\begin{aligned}
> &D \circ I = \text{Id}_{\mathcal{P}_2} \quad \text{✓} \\
> &I \circ D \neq \text{Id}_{\mathcal{P}_3} \quad \text{✗}
> \end{aligned}}$$
>
> $I$ es **inversa por la derecha** de $D$, pero no son inversas bilaterales.
>
> Esto ocurre porque $D: \mathcal{P}_3 \to \mathcal{P}_2$ no es biyectiva (no inyectiva).
>
> ---
>
> **EJERCICIO 3: Inversa de transformación por bloques**
>
> Encontrar la inversa de:
> $$A = \begin{bmatrix} I_2 & B \\ 0 & I_2 \end{bmatrix}$$
>
> donde $I_2$ es la identidad $2 \times 2$ y $B = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$
>
> **SOLUCIÓN:**
>
> Para matrices por bloques de la forma $\begin{bmatrix} I & B \\ 0 & I \end{bmatrix}$:
>
> $$\boxed{A^{-1} = \begin{bmatrix} I & -B \\ 0 & I \end{bmatrix}}$$
>
> Por tanto:
> $$A^{-1} = \begin{bmatrix} 1 & 0 & -1 & -2 \\ 0 & 1 & -3 & -4 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$
>
> **Verificación:**
> $$AA^{-1} = \begin{bmatrix} I_2 & B \\ 0 & I_2 \end{bmatrix}\begin{bmatrix} I_2 & -B \\ 0 & I_2 \end{bmatrix}$$
>
> $$= \begin{bmatrix} I_2 \cdot I_2 + B \cdot 0 & I_2 \cdot (-B) + B \cdot I_2 \\ 0 \cdot I_2 + I_2 \cdot 0 & 0 \cdot (-B) + I_2 \cdot I_2 \end{bmatrix}$$
>
> $$= \begin{bmatrix} I_2 & -B + B \\ 0 & I_2 \end{bmatrix} = \begin{bmatrix} I_2 & 0 \\ 0 & I_2 \end{bmatrix} = I_4$$ ✓

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales para Recordar
> **DEFINICIÓN CENTRAL:**
> $$\boxed{T^{-1} \text{ existe} \iff T \text{ es biyectiva (isomorfismo)}}$$
>
> Cuando existe:
> $$T^{-1} \circ T = \text{Id}_V \quad \text{y} \quad T \circ T^{-1} = \text{Id}_W$$
>
> **TEOREMA DE EXISTENCIA Y UNICIDAD:** ⭐⭐⭐
> - $T$ tiene inversa ⟺ $T$ es biyectiva
> - Si existe, la inversa es **única**
> - $T^{-1}$ es automáticamente transformación lineal
>
> **PROPIEDAD FUNDAMENTAL DE COMPOSICIÓN:**
> $$\boxed{(S \circ T)^{-1} = T^{-1} \circ S^{-1}}$$
>
> El orden se **invierte**.
>
> **REPRESENTACIÓN MATRICIAL:**
> $$\boxed{[T^{-1}]_{\mathcal{B}_W}^{\mathcal{B}_V} = \left([T]_{\mathcal{B}_V}^{\mathcal{B}_W}\right)^{-1}}$$
>
> La matriz de la inversa es la inversa de la matriz.
>
> **CRITERIO PRÁCTICO (matrices cuadradas):**
> $$\boxed{T \text{ invertible} \iff \det([T]) \neq 0}$$
>
> **PROPIEDADES ESENCIALES:**
> - Involución: $(T^{-1})^{-1} = T$
> - Linealidad: $T^{-1}(\vec{w}_1 + \vec{w}_2) = T^{-1}(\vec{w}_1) + T^{-1}(\vec{w}_2)$
> - Unicidad: Solo hay una inversa
> - Grupo: GL(V) = conjunto de todas las invertibles
>
> **CASOS ESPECIALES IMPORTANTES:**
> - Ortogonal: $T^{-1} = T^T$
> - Involutiva: $T^{-1} = T$
> - Diagonal: Invertir elementos diagonales
> - Permutación: $P^{-1} = P^T$
>
> **MÉTODOS DE CÁLCULO:**
> 1. Matriz $2 \times 2$: Fórmula directa
> 2. Gauss-Jordan: $[A \mid I] \to [I \mid A^{-1}]$
> 3. Adjunta: $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$
> 4. Resolución: Resolver $T(\vec{v}) = \vec{w}$ para $\vec{v}$
>
> **APLICACIONES CLAVE:**
> - Solución de sistemas: $\vec{x} = A^{-1}\vec{b}$
> - Gráficos por computadora: Transformaciones inversas
> - Criptografía: Descifrado
> - Control de sistemas: Controladores inversos
> - Machine Learning: Normalizing flows
>
> **VERIFICACIÓN PRÁCTICA:**
>
> Para verificar que $S = T^{-1}$:
> 1. Calcular $S \circ T$ y verificar que da identidad
> 2. Calcular $T \circ S$ y verificar que da identidad
> 3. Ambas deben cumplirse
>
> **CONCLUSIÓN FILOSÓFICA:**
>
> _"La inversa es el 'deshacer' algebraico perfecto: aplicar T y luego T⁻¹ regresa exactamente al punto de partida. Solo existe cuando la transformación es biyectiva, garantizando que cada salida tiene exactamente una entrada. Es la esencia de la reversibilidad matemática."_

---

**Tags:** #algebra-lineal #transformacion-inversa #invertibilidad #isomorfismo #biyectividad #matriz-inversa #grupo-lineal #composicion #reversibilidad #gl-n
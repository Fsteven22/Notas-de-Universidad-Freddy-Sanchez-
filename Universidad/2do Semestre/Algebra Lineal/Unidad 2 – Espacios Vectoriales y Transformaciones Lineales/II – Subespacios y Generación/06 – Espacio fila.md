# 📐 Espacio Fila

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva
> **El espacio fila de una matriz es el subespacio vectorial generado por sus filas. Representa todos los vectores que pueden obtenerse como combinaciones lineales de las filas de la matriz. Este concepto es el dual del espacio columna y comparte con él la misma dimensión (el rango), aunque viven en espacios diferentes.**
> 
> **Características clave:**
> - **Generación:** Formado por todas las combinaciones lineales de filas
> - **Dualidad:** Complemento natural del espacio columna
> - **Dimensión:** Igual al rango de la matriz (mismo que Col(A))
> - **Espacio ambiente:** Subespacio de ℝⁿ (para matriz m×n)
> - **Preservación:** Las operaciones elementales por filas NO cambian este espacio

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto
> **Orígenes duales (1850-1880):**
> - **Sylvester (1850):** Concepto de rango
>   - Introducción del término "rank"
>   - Observación inicial de dualidad
> - **Frobenius (1879):** Teorema fundamental
>   - Demostró que rango por filas = rango por columnas
>   - Resultado sorprendente y no trivial
> - **Cayley (1858):** Teoría de matrices
>   - Operaciones con filas y columnas
>   - Sistematización algebraica
> 
> **Desarrollo de la dualidad (1900-1940):**
> - **Grassmann:** Teoría de extensión
>   - Espacios duales geométricos
>   - Interpretación abstracta
> - **Wedderburn (1907):** Álgebra de matrices
>   - Relaciones entre Row(A) y Col(Aᵀ)
>   - Teoría de transpuestas
> - **Von Neumann (1930s):** Espacios de Hilbert
>   - Dualidad en espacios infinito-dimensionales
>   - Teoría de operadores adjuntos
> 
> **Era computacional (1950-presente):**
> - **Algoritmos numéricos:**
>   - Factorización LU
>   - Descomposición QR
>   - SVD y espacios fundamentales
> - **Aplicaciones modernas:**
>   - Compresión de datos
>   - Análisis de componentes principales
>   - Teoría de la información
>   - Machine learning (espacios de características)

## 📊 Definición Formal

> [!important]- Espacio Fila
> **Definición:**
> 
> Sea $A$ una matriz $m \times n$:
> 
> $$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$
> 
> Las filas de $A$ son vectores en $\mathbb{R}^n$:
> 
> $$\vec{r}_1 = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \end{bmatrix}$$
> 
> $$\vec{r}_2 = \begin{bmatrix} a_{21} & a_{22} & \cdots & a_{2n} \end{bmatrix}$$
> 
> $$\vdots$$
> 
> $$\vec{r}_m = \begin{bmatrix} a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$
> 
> **ESPACIO FILA:**
> 
> $$\text{Row}(A) = \text{span}\{\vec{r}_1, \vec{r}_2, \ldots, \vec{r}_m\}$$
> 
> $$= \{\beta_1\vec{r}_1 + \beta_2\vec{r}_2 + \cdots + \beta_m\vec{r}_m : \beta_i \in \mathbb{R}\}$$
> 
> Es el conjunto de todas las combinaciones lineales de las filas de $A$.
> 
> **Notación:**
> - $\text{Row}(A)$: espacio fila de $A$
> - $\mathcal{R}(A^T)$: espacio columna de $A^T$
> - $\text{Col}(A^T)$: notación equivalente
> 
> **Relación clave:**
> 
> $$\text{Row}(A) = \text{Col}(A^T)$$
> 
> El espacio fila de $A$ es el espacio columna de su transpuesta.
> 
> **Espacio ambiente:**
> 
> Si $A$ es $m \times n$:
> - $\text{Row}(A) \subseteq \mathbb{R}^n$ (vectores fila)
> - $\text{Col}(A) \subseteq \mathbb{R}^m$ (vectores columna)
> 
> ¡Viven en espacios diferentes!

## 🎯 Propiedades Fundamentales

> [!success]- Características del Espacio Fila
> **Teorema: Row(A) es un subespacio**
> 
> **DEMOSTRACIÓN:**
> 
> (S1) Vector cero:
> 
> $$\vec{0} = 0\vec{r}_1 + 0\vec{r}_2 + \cdots + 0\vec{r}_m$$
> $$\therefore \vec{0} \in \text{Row}(A) \quad \checkmark$$
> 
> (S2) Cerradura bajo suma:
> 
> Sean $\vec{u}, \vec{v} \in \text{Row}(A)$:
> $$\vec{u} = \alpha_1\vec{r}_1 + \cdots + \alpha_m\vec{r}_m$$
> $$\vec{v} = \beta_1\vec{r}_1 + \cdots + \beta_m\vec{r}_m$$
> 
> $$\vec{u} + \vec{v} = (\alpha_1+\beta_1)\vec{r}_1 + \cdots + (\alpha_m+\beta_m)\vec{r}_m \in \text{Row}(A) \quad \checkmark$$
> 
> (S3) Cerradura bajo multiplicación escalar:
> 
> Sea $\vec{u} \in \text{Row}(A)$, $c \in \mathbb{R}$:
> $$c\vec{u} = c(\alpha_1\vec{r}_1 + \cdots + \alpha_m\vec{r}_m) = (c\alpha_1)\vec{r}_1 + \cdots + (c\alpha_m)\vec{r}_m \in \text{Row}(A) \quad \checkmark$$
> 
> $$\therefore \text{Row}(A) \text{ es subespacio de } \mathbb{R}^n$$
> 
> **Propiedades dimensionales:**
> 
> **P1)** $\text{Row}(A) \subseteq \mathbb{R}^n$ donde $A$ es $m \times n$
> 
> (Las filas "viven" en $\mathbb{R}^n$)
> 
> **P2)** $\dim(\text{Row}(A)) = \text{rank}(A) = r$
> 
> Mismo rango que espacio columna
> 
> **P3)** $\dim(\text{Row}(A)) \leq \min\{m, n\}$
> - No puede exceder número de filas $(m)$
> - No puede exceder número de columnas $(n)$
> 
> **P4)** Si $A$ es $m \times n$:
> $$\text{rank}(A) = m \iff \text{filas son LI}$$
> $$\text{rank}(A) < m \iff \text{filas son LD}$$
> 
> **P5)** $\text{rank}(A) = n \iff \text{Row}(A) = \mathbb{R}^n$
> 
> (Las filas generan todo el espacio)
> 
> **Teorema fundamental de dualidad:**
> 
> $$\boxed{\dim(\text{Row}(A)) = \dim(\text{Col}(A)) = \text{rank}(A)}$$
> 
> **INTERPRETACIÓN:**
> 
> Aunque $\text{Row}(A)$ y $\text{Col}(A)$ son subespacios de espacios diferentes ($\mathbb{R}^n$ vs $\mathbb{R}^m$), tienen la **misma dimensión**.
> 
> Este es un resultado profundo y sorprendente.
> 
> **DEMOSTRACIÓN (idea):**
> 
> Por definición: $\text{Row}(A) = \text{Col}(A^T)$
> 
> Por teorema de transposición: $\text{rank}(A) = \text{rank}(A^T)$
> 
> Por tanto:
> $$\dim(\text{Row}(A)) = \dim(\text{Col}(A^T)) = \text{rank}(A^T) = \text{rank}(A) = \dim(\text{Col}(A))$$

## 🔥 Propiedad Clave: Preservación por Operaciones de Fila

> [!warning]- Diferencia Crítica con Espacio Columna
> **Teorema: Las operaciones elementales por filas PRESERVAN el espacio fila**
> 
> Si $B$ se obtiene de $A$ mediante operaciones elementales por filas:
> 
> $$\boxed{\text{Row}(A) = \text{Row}(B)}$$
> 
> **CONTRASTE:**
> - ✅ Row(A) = Row(RREF(A)) — SÍ se preserva
> - ❌ Col(A) ≠ Col(RREF(A)) — NO se preserva (en general)
> 
> **DEMOSTRACIÓN:**
> 
> Operaciones elementales por filas:
> 
> **Tipo 1:** Intercambiar filas $i$ y $j$
> 
> $$\text{span}\{\vec{r}_1, \ldots, \vec{r}_i, \ldots, \vec{r}_j, \ldots, \vec{r}_m\} = \text{span}\{\vec{r}_1, \ldots, \vec{r}_j, \ldots, \vec{r}_i, \ldots, \vec{r}_m\}$$
> 
> El orden no afecta el span $\checkmark$
> 
> **Tipo 2:** Multiplicar fila $i$ por escalar $c \neq 0$
> 
> Nueva fila: $\vec{r}_i' = c\vec{r}_i$
> 
> Cualquier CL de las nuevas filas:
> $$\beta_1\vec{r}_1 + \cdots + \beta_i(c\vec{r}_i) + \cdots + \beta_m\vec{r}_m = \beta_1\vec{r}_1 + \cdots + (c\beta_i)\vec{r}_i + \cdots + \beta_m\vec{r}_m$$
> 
> Está en $\text{Row}(A)$ original $\checkmark$
> 
> Y viceversa: $\vec{r}_i = \frac{1}{c}\vec{r}_i'$, así que span original ⊆ span nuevo $\checkmark$
> 
> **Tipo 3:** Sumar múltiplo de fila $j$ a fila $i$
> 
> Nueva fila: $\vec{r}_i' = \vec{r}_i + c\vec{r}_j$
> 
> $$\vec{r}_i' = 1\cdot\vec{r}_i + c\cdot\vec{r}_j + 0\cdot\vec{r}_k \quad (k \neq i,j)$$
> 
> Por tanto $\vec{r}_i' \in \text{span}\{\vec{r}_1, \ldots, \vec{r}_m\}$ $\checkmark$
> 
> Y despejando: $\vec{r}_i = \vec{r}_i' - c\vec{r}_j$, así que $\vec{r}_i \in$ span nuevo $\checkmark$
> 
> $$\therefore \text{Row}(A) = \text{Row}(B) \text{ para cualquier } B \text{ obtenida por ERO}$$
> 
> **CONSECUENCIA IMPORTANTE:**
> 
> Para encontrar base de $\text{Row}(A)$, podemos usar las filas NO NULAS de la forma escalonada reducida (RREF).
> 
> ¡No necesitamos regresar a la matriz original!

## 🔍 Cálculo del Espacio Fila

> [!tip]- Método de Reducción por Filas
> **Algoritmo para encontrar base de Row(A):**
> 
> **PROCEDIMIENTO:**
> 
> 1. Reducir $A$ a forma escalonada reducida (RREF)
> 
> 2. Las filas NO NULAS de la RREF forman una base de $\text{Row}(A)$
> 
> **IMPORTANTE:**
> 
> ✅ Usar filas de la forma REDUCIDA (no de la original)
> 
> Esto es OPUESTO al caso del espacio columna.
> 
> **RAZÓN:**
> 
> Las operaciones elementales por filas SÍ preservan el espacio fila, así que las filas de la RREF generan el mismo espacio que las filas originales.
> 
> **Ejemplo detallado:**
> 
> Encontrar base de $\text{Row}(A)$ donde:
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 5 & 6 \\ 3 & 6 & 8 & 9 \end{bmatrix}$$
> 
> **PASO 1: Reducir a RREF**
> 
> $$A \rightarrow \begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 0 & -1 & -2 \\ 0 & 0 & -1 & -3 \end{bmatrix} \quad (F_2 - 2F_1, \, F_3 - 3F_1)$$
> 
> $$\rightarrow \begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 0 & -1 & -2 \\ 0 & 0 & 0 & -1 \end{bmatrix} \quad (F_3 - F_2)$$
> 
> $$\rightarrow \begin{bmatrix} 1 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \quad \text{(RREF completa)}$$
> 
> **PASO 2: Identificar filas no nulas**
> 
> Todas las filas son no nulas:
> 
> $$\vec{r}_1' = \begin{bmatrix} 1 & 2 & 0 & 0 \end{bmatrix}$$
> $$\vec{r}_2' = \begin{bmatrix} 0 & 0 & 1 & 0 \end{bmatrix}$$
> $$\vec{r}_3' = \begin{bmatrix} 0 & 0 & 0 & 1 \end{bmatrix}$$
> 
> **PASO 3: Base de Row(A)**
> 
> $$\text{Base de Row}(A): \left\{\begin{bmatrix} 1 \\ 2 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}\right\}$$
> 
> (Escribimos como vectores columna para claridad)
> 
> $$\dim(\text{Row}(A)) = 3 = \text{rank}(A)$$
> 
> **VERIFICACIÓN:**
> 
> Cada fila original es CL de la base:
> 
> Fila 1 original: $[1, 2, 3, 4]$
> $$= 1\cdot[1,2,0,0] + 3\cdot[0,0,1,0] + 4\cdot[0,0,0,1] \quad \checkmark$$
> 
> **Método alternativo usando Aᵀ:**
> 
> Como $\text{Row}(A) = \text{Col}(A^T)$:
> 
> 1. Calcular $A^T$
> 2. Encontrar base de $\text{Col}(A^T)$ usando método de columnas pivote
> 3. Esta es una base de $\text{Row}(A)$

## 📈 Relación Fila-Columna

> [!important]- Teorema Fundamental del Rango
> **Igualdad de dimensiones:**
> 
> Para cualquier matriz $A$:
> 
> $$\boxed{\text{rank}_{\text{fila}}(A) = \text{rank}_{\text{columna}}(A)}$$
> 
> O equivalentemente:
> 
> $$\boxed{\dim(\text{Row}(A)) = \dim(\text{Col}(A))}$$
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> 
> ```mermaid
> graph TB
>     A[Matriz A: m×n]
>     B[Row A ⊆ ℝⁿ]
>     C[Col A ⊆ ℝᵐ]
>     
>     A --> B
>     A --> C
>     
>     B --> D[dim = r]
>     C --> E[dim = r]
>     
>     D -.mismo rango.- E
>     
>     style B fill:#c8e6c9
>     style C fill:#bbdefb
>     style D fill:#fff9c4
>     style E fill:#fff9c4
> ```
> 
> **Espacios diferentes, misma dimensión:**
> 
> - $\text{Row}(A)$ vive en $\mathbb{R}^n$ (espacio de las filas)
> - $\text{Col}(A)$ vive en $\mathbb{R}^m$ (espacio de las columnas)
> - Ambos tienen dimensión $r = \text{rank}(A)$
> 
> **EJEMPLO ILUSTRATIVO:**
> 
> Matriz $3 \times 5$:
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\ 2 & 4 & 5 & 6 & 7 \\ 3 & 6 & 8 & 9 & 10 \end{bmatrix}$$
> 
> Supongamos $\text{rank}(A) = 2$:
> 
> - $\text{Row}(A)$: plano en $\mathbb{R}^5$, $\dim = 2$
> - $\text{Col}(A)$: plano en $\mathbb{R}^3$, $\dim = 2$
> 
> ¡Dos planos en espacios completamente diferentes, pero ambos bidimensionales!
> 
> **DEMOSTRACIÓN (esquema):**
> 
> 1. Reducir $A$ a forma escalonada $R$
> 2. Número de filas no nulas en $R$ = rango por filas
> 3. Número de columnas pivote en $R$ = rango por columnas
> 4. Estos números son iguales (mismo número de pivotes)
> 5. Las operaciones por filas:
>    - NO cambian Row(A)
>    - NO cambian relaciones de dependencia en Col(A)
> 6. Por tanto: $\dim(\text{Row}(A)) = \dim(\text{Col}(A))$

## 🎨 Interpretación Geométrica

> [!note]- Visualización del Espacio Fila
> **Comparación visual Row vs Col:**
> 
> ```mermaid
> graph LR
>     subgraph "Matriz 3×4"
>         A[A]
>     end
>     
>     subgraph "Espacio Fila"
>         B[Row A ⊆ ℝ⁴]
>         B1[dim ≤ 3]
>         B --> B1
>     end
>     
>     subgraph "Espacio Columna"
>         C[Col A ⊆ ℝ³]
>         C1[dim ≤ 3]
>         C --> C1
>     end
>     
>     A --> B
>     A --> C
>     
>     B1 -.misma dim.- C1
>     
>     style B fill:#c8e6c9
>     style C fill:#bbdefb
>     style B1 fill:#fff9c4
>     style C1 fill:#fff9c4
> ```
> 
> **CASO 1: Matriz 2×3 con filas LI**
> 
> $$A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}$$
> 
> $$\text{Row}(A) = \text{span}\left\{\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}\right\} \subseteq \mathbb{R}^3$$
> 
> Visualización: plano en $\mathbb{R}^3$ que pasa por el origen
> 
> **Ecuación del plano:**
> 
> Un vector $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ está en $\text{Row}(A)$ si:
> 
> $$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \alpha\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} + \beta\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$$
> 
> Eliminando parámetros: $x - z + y - z = 0$ → $x + y = 2z$
> 
> **CASO 2: Filas paralelas (LD)**
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{bmatrix}$$
> 
> Todas las filas son múltiplos de $[1, 2, 3]$
> 
> $$\text{Row}(A) = \text{span}\left\{\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\right\} = \text{recta en } \mathbb{R}^3$$
> 
> Ecuación paramétrica: 
> $$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = t\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad t \in \mathbb{R}$$
> 
> **CASO 3: Comparación Row vs Col**
> 
> $$A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$
> 
> **Espacio fila:**
> $$\text{Row}(A) = \text{span}\left\{\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}\right\} = \text{plano } xy \text{ en } \mathbb{R}^3$$
> 
> **Espacio columna:**
> $$\text{Col}(A) = \text{span}\left\{\begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \end{bmatrix}\right\} = \mathbb{R}^2 \text{ completo}$$
> 
> Ambos tienen $\dim = 2$, pero viven en espacios diferentes.

## 🔗 Los Cuatro Subespacios Fundamentales

> [!success]- Teorema de los Cuatro Subespacios
> **Para matriz $A$ de $m \times n$ con rango $r$:**
> 
> ```mermaid
> graph TB
>     subgraph "Dominio: ℝⁿ"
>         A[Row A<br/>Espacio Fila<br/>dim = r]
>         B[Nul A<br/>Espacio Nulo<br/>dim = n-r]
>     end
>     
>     subgraph "Codominio: ℝᵐ"
>         C[Col A<br/>Espacio Columna<br/>dim = r]
>         D[Nul Aᵀ<br/>Nulo Izquierdo<br/>dim = m-r]
>     end
>     
>     A -->|transformación| C
>     B -->|aniquilado| E[0]
>     
>     A -.ortogonal.- B
>     C -.ortogonal.- D
>     
>     A -.misma dim.- C
>     
>     style A fill:#c8e6c9
>     style B fill:#ffccbc
>     style C fill:#bbdefb
>     style D fill:#ffccbc
> ```
> 
> **TABLA COMPARATIVA:**
> 
> | Subespacio | Notación | Espacio ambiente | Dimensión | Definición |
> |------------|----------|------------------|-----------|------------|
> | **Espacio Fila** | Row(A) | $\mathbb{R}^n$ | $r$ | span de filas |
> | **Espacio Nulo** | Nul(A) | $\mathbb{R}^n$ | $n-r$ | soluciones de $A\vec{x}=\vec{0}$ |
> | **Espacio Columna** | Col(A) | $\mathbb{R}^m$ | $r$ | span de columnas |
> | **Nulo Izquierdo** | Nul(A^T) | $\mathbb{R}^m$ | $m-r$ | soluciones de $A^T\vec{y}=\vec{0}$ |
> 
> **Relaciones de ortogonalidad:**
> 
> **Teorema de Ortogonalidad:**
> 
> $$\text{Row}(A) \perp \text{Nul}(A)$$
> 
> $$\text{Col}(A) \perp \text{Nul}(A^T)$$
> 
> **DEMOSTRACIÓN (Row ⊥ Nul):**
> 
> Sea $\vec{r}$ una fila de $A$ y $\vec{x} \in \text{Nul}(A)$, es decir, $A\vec{x} = \vec{0}$.
> 
> El producto $A\vec{x}$ en la componente $i$ es:
> $$(A\vec{x})_i = \vec{r}_i \cdot \vec{x} = 0$$
> 
> Por tanto, toda fila de $A$ es ortogonal a todo vector en $\text{Nul}(A)$.
> 
> Como $\text{Row}(A) = \text{span}\{\text{filas}\}$, se tiene:
> $$\text{Row}(A) \perp \text{Nul}(A) \quad \checkmark$$
> 
> **Descomposición ortogonal:**
> 
> $$\mathbb{R}^n = \text{Row}(A) \oplus \text{Nul}(A)$$
> 
> Todo vector $\vec{v} \in \mathbb{R}^n$ se descompone únicamente:
> $$\vec{v} = \vec{v}_{\text{row}} + \vec{v}_{\text{nul}}$$
> 
> donde $\vec{v}_{\text{row}} \in \text{Row}(A)$ y $\vec{v}_{\text{nul}} \in \text{Nul}(A)$
> 
> Similarmente:
> $$\mathbb{R}^m = \text{Col}(A) \oplus \text{Nul}(A^T)$$
> 
> **Teorema de la dimensión (versión completa):**
> 
> En $\mathbb{R}^n$:
> $$\dim(\text{Row}(A)) + \dim(\text{Nul}(A)) = n$$
> $$r + (n-r) = n \quad \checkmark$$
> 
> En $\mathbb{R}^m$:
> $$\dim(\text{Col}(A)) + \dim(\text{Nul}(A^T)) = m$$
> $$r + (m-r) = m \quad \checkmark$$

## 💡 Ejemplos Resueltos

> [!example]- Problemas Detallados
> **Problema 1: Encontrar base de Row(A)**
> 
> Sea 
> $$A = \begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 3 & 1 \\ 3 & 6 & 4 & 1 \\ 5 & 10 & 8 & 3\end{bmatrix}$$
>
> 
> Encontrar base de $\text{Row}(A)$ y su dimensión.
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Reducir a RREF**
> 
> $$\begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 3 & 1 \\ 3 & 6 & 4 & 1 \\ 5 & 10 & 8 & 3 \end{bmatrix}$$
> 
> $$F_2 - 2F_1, \, F_3 - 3F_1, \, F_4 - 5F_1 \rightarrow$$
> 
> $$\begin{bmatrix} 1 & 2 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 3 & 3 \end{bmatrix}$$
> 
> $$F_3 - F_2, \, F_4 - 3F_2 \rightarrow$$
> 
> $$\begin{bmatrix} 1 & 2 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> $$F_1 - F_2 \rightarrow \begin{bmatrix} 1 & 2 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} = \text{RREF}$$
> 
> **PASO 2: Identificar filas no nulas**
> 
> Filas no nulas de RREF:
> - Fila 1: $[1, 2, 0, -1]$
> - Fila 2: $[0, 0, 1, 1]$
> 
> **PASO 3: Base de Row(A)**
> 
> $$\text{Base de Row}(A): \left\{\begin{bmatrix} 1 \\ 2 \\ 0 \\ -1 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \\ 1 \end{bmatrix}\right\}$$
> 
> **RESPUESTA:**
> - Base: $\{[1,2,0,-1], [0,0,1,1]\}$
> - $\dim(\text{Row}(A)) = 2$
> - $\text{rank}(A) = 2$
> - $\text{Row}(A)$ es un plano en $\mathbb{R}^4$
> 
> **VERIFICACIÓN:**
> 
> Cada fila original debe ser CL de la base:
> 
> Fila 1: $[1,2,1,0] = 1 \cdot [1,2,0,-1] + 1 \cdot [0,0,1,1]$ ✓
> 
> Fila 2: $[2,4,3,1] = 2 \cdot [1,2,0,-1] + 3 \cdot [0,0,1,1]$ ✓
> 
> ---
> 
> **Problema 2: Comparar Row(A) y Col(A)**
> 
> Para 
> $$A = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 6 & 10 \end{bmatrix}$$
> 
> Encontrar bases de $\text{Row}(A)$ y $\text{Col}(A)$.
> 
> **SOLUCIÓN:**
> 
> **PARTE A: Espacio Fila**
> 
> Reducir a RREF:
> 
> $$\begin{bmatrix} 1 & 3 & 5 \\ 2 & 6 & 10 \end{bmatrix} \xrightarrow{F_2 - 2F_1} \begin{bmatrix} 1 & 3 & 5 \\ 0 & 0 & 0 \end{bmatrix}$$
> 
> Fila no nula: $[1, 3, 5]$
> 
> $$\text{Base de Row}(A): \left\{\begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix}\right\}$$
> 
> $\dim(\text{Row}(A)) = 1$ — recta en $\mathbb{R}^3$
> 
> **PARTE B: Espacio Columna**
> 
> De la RREF, columna pivote: posición 1
> 
> Tomar columna 1 de $A$ original:
> 
> $$\text{Base de Col}(A): \left\{\begin{bmatrix} 1 \\ 2 \end{bmatrix}\right\}$$
> 
> $\dim(\text{Col}(A)) = 1$ — recta en $\mathbb{R}^2$
> 
> **COMPARACIÓN:**
> 
> - $\text{Row}(A) \subseteq \mathbb{R}^3$, $\dim = 1$ (recta)
> - $\text{Col}(A) \subseteq \mathbb{R}^2$, $\dim = 1$ (recta)
> - Ambos tienen dimensión 1 ($\text{rank}(A) = 1$)
> - Viven en espacios diferentes
> - Son "rectas" en dimensiones diferentes
> 
> ---
> 
> **Problema 3: Verificar ortogonalidad Row ⊥ Nul**
> 
> Para 
> $$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$$
> 
> Verificar que $\text{Row}(A) \perp \text{Nul}(A)$.
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Encontrar Nul(A)**
> 
> Resolver $A\vec{x} = \vec{0}$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 2 & 3 & 0 \\ 4 & 5 & 6 & 0 \end{array}\right] \rightarrow \left[\begin{array}{ccc|c} 1 & 2 & 3 & 0 \\ 0 & -3 & -6 & 0 \end{array}\right]$$
> 
> $$\rightarrow \left[\begin{array}{ccc|c} 1 & 0 & -1 & 0 \\ 0 & 1 & 2 & 0 \end{array}\right]$$
> 
> Variables: $x_1, x_2$ básicas; $x_3$ libre
> 
> Solución: 
> $$x_3 = t, \quad x_2 = -2t, \quad x_1 = t$$
> 
> $$\vec{x} = t\begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$$
> 
> $$\text{Base de Nul}(A): \left\{\begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}\right\}$$
> 
> **PASO 2: Verificar ortogonalidad**
> 
> Filas de $A$:
> $$\vec{r}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad \vec{r}_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$$
> 
> Vector en Nul(A):
> $$\vec{n} = \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$$
> 
> Productos punto:
> $$\vec{r}_1 \cdot \vec{n} = 1(1) + 2(-2) + 3(1) = 1 - 4 + 3 = 0 \quad \checkmark$$
> 
> $$\vec{r}_2 \cdot \vec{n} = 4(1) + 5(-2) + 6(1) = 4 - 10 + 6 = 0 \quad \checkmark$$
> 
> Por tanto: $\text{Row}(A) \perp \text{Nul}(A)$ ✓
> 
> **INTERPRETACIÓN:**
> 
> En $\mathbb{R}^3$:
> - $\text{Row}(A)$ es un plano (dim = 2)
> - $\text{Nul}(A)$ es una recta (dim = 1)
> - Son ortogonales y complementarios: $2 + 1 = 3$ ✓
> 
> ---
> 
> **Problema 4: Ecuación del espacio Row(A)**
> 
> Para 
> $$A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \end{bmatrix}$$
> 
> Encontrar ecuación(es) que definen $\text{Row}(A)$ en $\mathbb{R}^3$.
> 
> **SOLUCIÓN:**
> 
> **MÉTODO 1: Vía RREF**
> 
> $$\begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 3 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
> 
> Base de Row(A): $\{[1,2,0], [0,0,1]\}$
> 
> Un vector $[x, y, z]$ está en Row(A) si:
> $$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \alpha\begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} + \beta\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$
> 
> Esto da: $x = \alpha$, $y = 2\alpha$, $z = \beta$
> 
> Eliminando parámetros: $y = 2x$
> 
> **ECUACIÓN DE Row(A):**
> $$\boxed{y - 2x = 0}$$
> 
> Es un plano en $\mathbb{R}^3$ que pasa por el origen.
> 
> **MÉTODO 2: Vía Nul(Aᵀ)**
> 
> $\text{Row}(A)$ es el complemento ortogonal de $\text{Nul}(A^T)$.
> 
> $$A^T = \begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 1 & 3 \end{bmatrix}$$
> 
> Resolver $A^T\vec{y} = \vec{0}$:
> 
> $$\begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$
> 
> Primera ecuación: $y_1 + 2y_2 = 0$
> 
> Base de Nul(Aᵀ): $\{[-2, 1, 0]^T\}$ después de verificar tercera fila
> 
> Vector normal a Row(A): $\vec{n} = [-2, 1, 0]$
> 
> Ecuación del plano: $-2x + y + 0z = 0$
> 
> $$\boxed{y = 2x}$$ ✓ (mismo resultado)

## ⚡ Propiedades Adicionales

> [!important]- Teoremas sobre Espacio Fila
> **Propiedades de preservación:**
> 
> **P1)** Si $B = PA$ donde $P$ es invertible:
> $$\text{Row}(B) = \text{Row}(A)$$
> 
> Multiplicar por invertible a la izquierda preserva espacio fila
> 
> **P2)** Si $B = AQ$ donde $Q$ es invertible:
> $$\text{Row}(B) \neq \text{Row}(A)$$ en general
> 
> Pero: $\dim(\text{Row}(B)) = \dim(\text{Row}(A))$
> 
> **Relación con transpuesta:**
> 
> **T1)** $\text{Row}(A) = \text{Col}(A^T)$
> 
> Definición fundamental
> 
> **T2)** $\text{Row}(A^T) = \text{Col}(A)$
> 
> Simetría de transposición
> 
> **T3)** $\dim(\text{Row}(A)) = \dim(\text{Row}(A^T))$
> 
> Ambos iguales al rango
> 
> **Relación con productos:**
> 
> **PR1)** $\text{Row}(AB) \subseteq \text{Row}(B)$
> 
> **DEMOSTRACIÓN:**
> 
> Las filas de $AB$ son combinaciones lineales de las filas de $B$.
> 
> Si $\vec{r}_i$ es la fila $i$ de $A$:
> $$(AB)_{\text{fila } i} = \sum_{j=1}^m a_{ij} \cdot (\text{fila } j \text{ de } B)$$
> 
> Por tanto toda fila de $AB$ está en $\text{span}\{\text{filas de } B\} = \text{Row}(B)$ ✓
> 
> **PR2)** Si $A$ tiene filas LI (rango fila completo):
> $$\text{Row}(AB) = \text{Row}(B)$$
> 
> **Descomposición de rango:**
> 
> Toda matriz $A$ de rango $r$ se puede escribir:
> $$A = CR$$
> 
> donde:
> - $C$ es $m \times r$ con $\text{rank}(C) = r$ (base de Col(A))
> - $R$ es $r \times n$ con $\text{rank}(R) = r$ (base de Row(A))
> 
> Esta es la **descomposición de rango**.

## 🎯 Aplicaciones del Espacio Fila

> [!note]- Usos Prácticos
> **1. Sistemas de ecuaciones:**
> 
> **Interpretación dual:**
> 
> Sistema $A\vec{x} = \vec{b}$ puede verse como:
> - **Vista columna:** $\vec{b}$ como CL de columnas
> - **Vista fila:** Cada ecuación es $\vec{r}_i \cdot \vec{x} = b_i$
> 
> La solución $\vec{x}$ debe ser ortogonal a toda fila de la parte homogénea.
> 
> **2. Teoría de códigos:**
> 
> En códigos lineales:
> - **Matriz generadora $G$:** Las filas de $G$ generan el código
> - **Espacio del código:** $\mathcal{C} = \text{Row}(G)$
> - **Dimensión del código:** $k = \dim(\text{Row}(G))$
> 
> **3. Análisis de datos:**
> 
> Matriz de datos $X$ ($n \times p$):
> - Filas = observaciones
> - Columnas = variables
> 
> $\text{Row}(X)$: espacio generado por las observaciones
> - Describe variabilidad en datos
> - Base para PCA
> 
> **4. Reducción de dimensionalidad:**
> 
> Si $\text{rank}(A) = r < \min\{m,n\}$:
> - $\text{Row}(A)$ tiene dimensión $r$ en $\mathbb{R}^n$
> - Datos proyectados viven en subespacio $r$-dimensional
> - Compresión sin pérdida de información
> 
> **5. Ortogonalización:**
> 
> Proceso de Gram-Schmidt en filas:
> - Genera base ortonormal de Row(A)
> - Útil para factorización QR
> - Aplicación en mínimos cuadrados
> 
> **6. Complementos ortogonales:**
> 
> **Proyección ortogonal:**
> 
> Todo vector $\vec{v} \in \mathbb{R}^n$ se descompone:
> $$\vec{v} = \text{proj}_{\text{Row}(A)}\vec{v} + \text{proj}_{\text{Nul}(A)}\vec{v}$$
> 
> Esto es fundamental en:
> - Mínimos cuadrados
> - Filtrado de señales
> - Procesamiento de imágenes

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes
> **1. "Row(A) usa filas de la matriz original"**
> 
> ❌ **INCOMPLETO**
> 
> Puedes usar:
> - ✅ Filas NO NULAS de RREF (método estándar)
> - ✅ Filas originales que son LI
> - ✅ Cualquier base del mismo subespacio
> 
> **DIFERENCIA CLAVE:**
> - Col(A): columnas de A ORIGINAL
> - Row(A): filas de A REDUCIDA (o equivalente)
> 
> ---
> 
> **2. "Row(A) y Col(A) son el mismo espacio"**
> 
> ❌ **FALSO**
> 
> SON DIFERENTES:
> - Viven en espacios diferentes ($\mathbb{R}^n$ vs $\mathbb{R}^m$)
> - Generalmente no se pueden comparar
> 
> SOLO comparten:
> - La misma dimensión (el rango)
> 
> **Ejemplo:**
> $$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$$
> 
> - $\text{Row}(A) = \mathbb{R}^2$ (todo el plano)
> - $\text{Col}(A) = $ plano $xy$ en $\mathbb{R}^3$
> 
> Claramente diferentes, aunque $\dim = 2$ para ambos.
> 
> ---
> 
> **3. "Si Row(A) = Row(B), entonces A = B"**
> 
> ❌ **FALSO**
> 
> **Contraejemplo:**
> 
> $$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$
> 
> $$\text{Row}(A) = \text{Row}(B) = \mathbb{R}^2$$
> 
> Pero $A \neq B$
> 
> CORRECTO: Mismo espacio fila implica relación por ERO.
> 
> ---
> 
> **4. "Operaciones por columnas preservan Row(A)"**
> 
> ❌ **FALSO**
> 
> - Operaciones por FILAS → preservan Row(A) ✅
> - Operaciones por COLUMNAS → preservan Col(A) ✅
> 
> No cruzar las operaciones.
> 
> ---
> 
> **5. "dim(Row(A)) ≤ m siempre"**
> 
> ⚠️ **CUIDADO**
> 
> Si $A$ es $m \times n$:
> $$\dim(\text{Row}(A)) \leq \min\{m, n\}$$
> 
> No solo $m$, también está limitado por $n$ (el espacio ambiente).
> 
> **Ejemplo:**
> $$A = \begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \end{bmatrix}$$
> 
> $m = 2$, $n = 5$
> 
> $\dim(\text{Row}(A)) = 2 \leq \min\{2, 5\} = 2$ ✓
> 
> ---
> 
> **6. "Row(A) ⊥ Col(A)"**
> 
> ❌ **FALSO** en general
> 
> No tiene sentido hablar de ortogonalidad entre subespacios de espacios diferentes.
> 
> CORRECTO:
> - $\text{Row}(A) \perp \text{Nul}(A)$ (ambos en $\mathbb{R}^n$) ✅
> - $\text{Col}(A) \perp \text{Nul}(A^T)$ (ambos en $\mathbb{R}^m$) ✅
> 
> ---
> 
> **7. "Todas las filas están en Row(A)"**
> 
> ✅ **VERDADERO**
> 
> Cada fila $\vec{r}_i$ cumple:
> $$\vec{r}_i = 0\vec{r}_1 + \cdots + 1\vec{r}_i + \cdots + 0\vec{r}_m$$
> 
> Pero esto NO significa que todas sean necesarias para una base (pueden ser LD).

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales
> **Fundamentos previos:**
> - [[01 - Vectores en espacios vectoriales]] - Subespacios
> - [[05 - Combinaciones lineales]] - Span
> - [[06 - Independencia lineal]] - Bases
> - [[05 – Espacio columna]] - Concepto dual
> 
> **Temas relacionados:**
> - [[18 - Espacio nulo]] - Complemento ortogonal
> - [[19 - Rango y nulidad]] - Teorema dimensional
> - [[20 - Transformaciones lineales]] - Dualidad
> - [[22 - Ortogonalidad]] - Proyecciones
> 
> **Aplicaciones posteriores:**
> - [[25 - Mínimos cuadrados]] - Descomposición ortogonal
> - [[26 - Descomposición QR]] - Ortogonalización
> - [[27 - SVD]] - Cuatro subespacios
> - [[28 - Espacios fundamentales]] - Teoría completa

## 📚 Recursos Adicionales

> [!note]- Herramientas y Referencias
> **Software de álgebra lineal:**
> 
> - **MATLAB**
>   ```matlab
>   A = [1 2 3; 4 5 6; 7 8 9];
>   R = rref(A);
>   row_space_basis = R(any(R,2),:); % filas no nulas
>   rank_A = rank(A);
>   ```
> 
> - **Python (NumPy/SciPy)**
>   ```python
>   import numpy as np
>   from scipy.linalg import orth
>   
>   A = np.array([[1,2,3],[4,5,6],[7,8,9]])
>   # Base ortonormal de Row(A)
>   row_basis = orth(A.T).T
>   rank_A = np.linalg.matrix_rank(A)
>   ```
> 
> - **Wolfram Alpha**
>   - "row space {{1,2,3},{4,5,6},{7,8,9}}"
>   - "reduced row echelon form {{1,2,3},{4,5,6}}"
> 
> **Visualizadores:**
> - **GeoGebra 3D** - Planos y rectas en ℝ³
> - **3Blue1Brown** - "The Four Fundamental Subspaces"
> - **MIT OCW** - Videos de Gilbert Strang

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas
> **Nivel introductorio:**
> - **Lay, D. C.** (2016). _Álgebra Lineal y sus Aplicaciones_ (5ª ed.). Pearson.
>   - Cap. 4.6: Rango
>   - Sección sobre espacios fila y columna
> 
> - **Poole, D.** (2011). _Álgebra Lineal: Una Introducción Moderna_ (3ª ed.). Cengage.
>   - Cap. 3: Espacios vectoriales
>   - Excelentes visualizaciones
> 
> **Nivel intermedio:**
> - **Strang, G.** (2016). _Introduction to Linear Algebra_ (5th ed.). Wellesley-Cambridge.
>   - **CAP. 3: THE FOUR FUNDAMENTAL SUBSPACES** ⭐
>   - Perspectiva única y profunda
>   - Videos disponibles (MIT OCW)
> 
> - **Anton, H., & Rorres, C.** (2014). _Elementary Linear Algebra_ (11th ed.). Wiley.
>   - Cap. 5: Espacios vectoriales generales
>   - Muchos ejemplos trabajados
> 
> **Nivel avanzado:**
> - **Axler, S.** (2015). _Linear Algebra Done Right_ (3rd ed.). Springer.
>   - Cap. 3: Linear Maps
>   - Tratamiento abstracto y elegante
> 
> - **Horn, R. A., & Johnson, C. R.** (2013). _Matrix Analysis_ (2nd ed.). Cambridge.
>   - Cap. 0: Review and Miscellany
>   - Perspectiva avanzada de espacios fundamentales

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales
> 
> **DEFINICIÓN ESENCIAL:**
> 
> $$\text{Row}(A) = \text{span}\{\vec{r}_1, \vec{r}_2, \ldots, \vec{r}_m\} = \text{Col}(A^T)$$
> 
> **TEOREMA FUNDAMENTAL:**
> 
> $$\boxed{\dim(\text{Row}(A)) = \dim(\text{Col}(A)) = \text{rank}(A)}$$
> 
> **ALGORITMO DE CÁLCULO:**
> 1. Reducir $A$ a RREF
> 2. Las filas NO NULAS de RREF forman base de Row(A)
> 
> **DIFERENCIA CRÍTICA:**
> - **Col(A):** columnas de A ORIGINAL con posiciones pivote
> - **Row(A):** filas NO NULAS de A REDUCIDA
> 
> **PROPIEDAD CLAVE:**
> 
> $$\text{Operaciones por filas PRESERVAN Row}(A)$$
> 
> **ORTOGONALIDAD:**
> 
> $$\text{Row}(A) \perp \text{Nul}(A) \quad \text{en } \mathbb{R}^n$$
> 
> $$\mathbb{R}^n = \text{Row}(A) \oplus \text{Nul}(A)$$
> 
> **RELACIONES DIMENSIONALES:**
> 
> $$\dim(\text{Row}(A)) + \dim(\text{Nul}(A)) = n$$
> 
> donde $A$ es $m \times n$

---

**Tags:** #algebra-lineal #espacio-fila #rango #matriz #subespacios #dualidad #transformaciones-lineales #cuatro-subespacios #ortogonalidad #row-space
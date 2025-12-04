# 📐 Espacio Columna

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva
> **El espacio columna de una matriz es el subespacio vectorial generado por sus columnas. Representa todos los vectores que pueden obtenerse como combinaciones lineales de las columnas de la matriz. Este concepto es fundamental para entender qué sistemas lineales tienen solución y cuál es el rango de una transformación lineal.**
> 
> **Características clave:**
> - **Generación:** Formado por todas las combinaciones lineales de columnas
> - **Subespacio:** Es un subespacio del espacio ambiente
> - **Dimensión:** El rango de la matriz
> - **Interpretación:** Imagen de la transformación lineal asociada
> - **Aplicación:** Determina existencia de soluciones

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto
> **Orígenes (1850-1900):**
> - **Cayley (1858):** Teoría de matrices
>   - Primera formulación sistemática
>   - Operaciones matriciales
> - **Sylvester (1850):** Concepto de rango
>   - Introducción del término "rank"
>   - Relación con determinantes
> - **Frobenius (1879):** Teoría de rango
>   - Rango por filas vs columnas
>   - Teorema de igualdad
> 
> **Desarrollo geométrico (1900-1950):**
> - **Grassmann:** Espacios lineales
>   - Interpretación geométrica
>   - Subespacios generados
> - **Schmidt (1907):** Ortogonalización
>   - Bases ortonormales
>   - Proyecciones
> - **Von Neumann (1930s):** Teoría de operadores
>   - Imagen y núcleo
>   - Espacios duales
> 
> **Era moderna (1950-presente):**
> - **Computación numérica:**
>   - Algoritmos de rango
>   - Descomposición SVD
> - **Aplicaciones:**
>   - Análisis de datos
>   - Procesamiento de señales
>   - Machine learning

## 📊 Definición Formal

> [!important]- Espacio Columna
> **Definición:**
> 
> Sea $A$ una matriz $m \times n$:
> 
> $$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$
> 
> Las columnas de $A$ son vectores en $\mathbb{R}^m$:
> 
> $$\vec{c}_1 = \begin{bmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{m1} \end{bmatrix}, \quad \vec{c}_2 = \begin{bmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{m2} \end{bmatrix}, \quad \ldots, \quad \vec{c}_n = \begin{bmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{mn} \end{bmatrix}$$
> 
> **ESPACIO COLUMNA:**
> 
> $$\text{Col}(A) = \text{span}\{\vec{c}_1, \vec{c}_2, \ldots, \vec{c}_n\}$$
> 
> $$= \{\alpha_1\vec{c}_1 + \alpha_2\vec{c}_2 + \cdots + \alpha_n\vec{c}_n : \alpha_i \in \mathbb{R}\}$$
> 
> $$= \{A\vec{x} : \vec{x} \in \mathbb{R}^n\}$$
> 
> Es el conjunto de todas las combinaciones lineales de las columnas de $A$.
> 
> **Notación:**
> - $\text{Col}(A)$: espacio columna de $A$
> - $\text{Im}(A)$: imagen de $A$ (mismo concepto)
> - $\mathcal{R}(A)$: rango-espacio de $A$
> - $C(A)$: notación alternativa
> 
> Relación con transformación lineal: Si $T(\vec{x}) = A\vec{x}$, entonces $\text{Col}(A) = \text{Im}(T)$

## 🎯 Propiedades Fundamentales

> [!success]- Características del Espacio Columna
> **Teorema: Col(A) es un subespacio**
> 
> **DEMOSTRACIÓN:**
> 
> (S1) Vector cero:
> $$\vec{0} = A\vec{0} = 0\vec{c}_1 + 0\vec{c}_2 + \cdots + 0\vec{c}_n$$
> $$\therefore \vec{0} \in \text{Col}(A) \quad \checkmark$$
> 
> (S2) Cerradura bajo suma:
> 
> Sean $\vec{u}, \vec{v} \in \text{Col}(A)$, entonces $\exists \vec{x}, \vec{y}$ tales que:
> $$\vec{u} = A\vec{x}, \quad \vec{v} = A\vec{y}$$
> 
> $$\vec{u} + \vec{v} = A\vec{x} + A\vec{y} = A(\vec{x} + \vec{y}) \in \text{Col}(A) \quad \checkmark$$
> 
> (S3) Cerradura bajo multiplicación escalar:
> 
> Sea $\vec{u} \in \text{Col}(A)$, $\alpha \in \mathbb{R}$, entonces $\exists \vec{x}$ tal que:
> $$\vec{u} = A\vec{x}$$
> 
> $$\alpha\vec{u} = \alpha(A\vec{x}) = A(\alpha\vec{x}) \in \text{Col}(A) \quad \checkmark$$
> 
> $$\therefore \text{Col}(A) \text{ es subespacio de } \mathbb{R}^m$$
> 
> **Propiedades dimensionales:**
> 
> **P1)** $\text{Col}(A) \subseteq \mathbb{R}^m$ donde $A$ es $m \times n$
> 
> (Las columnas "viven" en $\mathbb{R}^m$)
> 
> **P2)** $\dim(\text{Col}(A)) = \text{rank}(A) = r$ donde $r$ es el número de columnas pivote
> 
> **P3)** $\dim(\text{Col}(A)) \leq \min\{m, n\}$
> - No puede exceder número de filas $(m)$
> - No puede exceder número de columnas $(n)$
> 
> **P4)** Si $A$ es $m \times n$:
> $$\text{rank}(A) = n \iff \text{columnas son LI}$$
> $$\text{rank}(A) < n \iff \text{columnas son LD}$$
> 
> **P5)** $\text{rank}(A) = m \iff \text{Col}(A) = \mathbb{R}^m$
> 
> (Las columnas generan todo el espacio)
> 
> **Relación con sistemas lineales:**
> 
> $$\text{Sistema } A\vec{x} = \vec{b} \text{ tiene solución} \iff \vec{b} \in \text{Col}(A)$$
> 
> **DEMOSTRACIÓN:**
> 
> $(\Rightarrow)$ Si $\exists \vec{x}$ tal que $A\vec{x} = \vec{b}$, entonces $\vec{b} = A\vec{x} \in \text{Col}(A)$ por definición
> 
> $(\Leftarrow)$ Si $\vec{b} \in \text{Col}(A)$, entonces $\exists \vec{x}$ tal que $\vec{b} = A\vec{x}$, por tanto $\vec{x}$ es solución del sistema
> 
> **INTERPRETACIÓN:**
> 
> El espacio columna es el conjunto de todos los vectores $\vec{b}$ para los cuales $A\vec{x} = \vec{b}$ tiene solución.

## 🔍 Cálculo del Espacio Columna

> [!tip]- Método de Reducción por Filas
> **Algoritmo para encontrar base de Col(A):**
> 
> **PROCEDIMIENTO:**
> 
> 1. Reducir $A$ a forma escalonada reducida (RREF)
> 
> 2. Identificar columnas pivote en la forma reducida
> 
> 3. Las columnas correspondientes en la matriz ORIGINAL $A$ forman una base de $\text{Col}(A)$
> 
> **IMPORTANTE:**
> 
> ⚠️ Usar columnas de $A$ original, NO de la forma reducida
> 
> La reducción solo identifica CUÁLES columnas usar, pero la base se forma con las columnas originales.
> 
> **RAZÓN:**
> 
> Las operaciones elementales por filas NO preservan el espacio columna (cambian las relaciones lineales entre columnas), pero SÍ preservan las relaciones de dependencia lineal.
> 
> **Ejemplo detallado:**
> 
> Encontrar base de $\text{Col}(A)$ donde:
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 5 & 6 \\ 3 & 6 & 8 & 9 \end{bmatrix}$$
> 
> **PASO 1: Reducir a forma escalonada**
> 
> $$A \rightarrow \begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 0 & -1 & -2 \\ 0 & 0 & -1 & -3 \end{bmatrix} \quad (F_2 - 2F_1, \, F_3 - 3F_1)$$
> 
> $$\rightarrow \begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 0 & -1 & -2 \\ 0 & 0 & 0 & -1 \end{bmatrix} \quad (F_3 - F_2)$$
> 
> $$\rightarrow \begin{bmatrix} 1 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \quad \text{(RREF completa)}$$
> 
> **PASO 2: Identificar pivotes**
> 
> Columnas pivote: 1, 3, 4 (posiciones con los 1's principales)
> 
> **PASO 3: Base de Col(A)**
> 
> Tomar columnas 1, 3, 4 de $A$ ORIGINAL:
> 
> $$\vec{c}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \quad \vec{c}_3 = \begin{bmatrix} 3 \\ 5 \\ 8 \end{bmatrix}, \quad \vec{c}_4 = \begin{bmatrix} 4 \\ 6 \\ 9 \end{bmatrix}$$
> 
> $$\text{Base: } \left\{\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \begin{bmatrix} 3 \\ 5 \\ 8 \end{bmatrix}, \begin{bmatrix} 4 \\ 6 \\ 9 \end{bmatrix}\right\}$$
> 
> $$\dim(\text{Col}(A)) = 3$$
> 
> **VERIFICACIÓN:**
> 
> Columna 2 es combinación de columna 1:
> $$\vec{c}_2 = 2\vec{c}_1$$
> 
> $$\begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} = 2\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \quad \checkmark$$

## 📈 Relación con el Rango

> [!important]- Rango y Dimensión
> **Teorema del rango:**
> 
> Para matriz $A$ de $m \times n$:
> 
> $$\text{rank}(A) = \dim(\text{Col}(A))$$
> 
> El rango es la dimensión del espacio columna.
> 
> **INTERPRETACIÓN:**
> - $\text{rank}(A)$ = número de columnas linealmente independientes
> - $\text{rank}(A)$ = número de columnas pivote
> - $\text{rank}(A)$ = número de vectores en base de $\text{Col}(A)$
> 
> **Rango por filas vs rango por columnas:**
> 
> **TEOREMA FUNDAMENTAL:**
> 
> $$\text{rank}_{\text{filas}}(A) = \text{rank}_{\text{columnas}}(A)$$
> 
> Es decir:
> $$\dim(\text{Row}(A)) = \dim(\text{Col}(A))$$
> 
> Este resultado NO es obvio geométricamente:
> - $\text{Row}(A) \subseteq \mathbb{R}^n$ (vectores fila)
> - $\text{Col}(A) \subseteq \mathbb{R}^m$ (vectores columna)
> 
> Son subespacios de espacios DIFERENTES, pero tienen la MISMA dimensión.
> 
> **DEMOSTRACIÓN (idea):**
> 
> Las operaciones elementales por filas:
> - NO cambian el espacio fila
> - NO cambian las relaciones de dependencia entre columnas
> - Preservan el número de pivotes
> 
> Por tanto, preservan ambos rangos.

## 🎨 Interpretación Geométrica

> [!note]- Visualización del Espacio Columna
> **En $\mathbb{R}^3$:**
> 
> ```mermaid
> graph TD
>     A[Matriz A: 3×2] --> B[Col A es subespacio de ℝ³]
>     B --> C{Rango de A}
>     C -->|rank = 2| D[Plano por el origen]
>     C -->|rank = 1| E[Recta por el origen]
>     C -->|rank = 0| F[Solo el origen]
>     
>     D --> G[2 columnas LI]
>     E --> H[Columnas paralelas]
>     F --> I[Matriz cero]
>     
>     style B fill:#e1f5ff
>     style D fill:#c8e6c9
>     style E fill:#fff9c4
>     style F fill:#ffccbc
> ```
> 
> **Casos visuales:**
> 
> **CASO 1: Matriz $3 \times 2$ con columnas LI**
> 
> $$A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$$
> 
> $$\text{Col}(A) = \text{plano } xy \text{ en } \mathbb{R}^3$$
> 
> Generado por $\vec{c}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ y $\vec{c}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$
> 
> Visualización: plano horizontal a altura $z = 0$
> 
> **CASO 2: Columnas paralelas**
> 
> $$A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 6 \end{bmatrix}$$
> 
> $\vec{c}_2 = 2\vec{c}_1$, por tanto columnas LD
> 
> $$\text{Col}(A) = \text{span}\left\{\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\right\} = \text{recta por origen}$$
> 
> Visualización: recta con dirección $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$
> 
> **CASO 3: Tres columnas en $\mathbb{R}^3$**
> 
> $$A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$$
> 
> $\text{Col}(A) = \text{plano } xy$ (tercera columna $= \vec{c}_1 + \vec{c}_2$)
> 
> Aunque hay 3 columnas, solo 2 son LI

## 🔗 Relación con Otros Subespacios

> [!success]- Cuatro Subespacios Fundamentales
> **Para matriz $A$ de $m \times n$:**
> 
> **CUATRO SUBESPACIOS:**
> 
> **1. ESPACIO COLUMNA:** $\text{Col}(A) \subseteq \mathbb{R}^m$
> - Combinaciones lineales de columnas
> - $\dim = \text{rank}(A) = r$
> - Imagen de $T(\vec{x}) = A\vec{x}$
> 
> **2. ESPACIO NULO:** $\text{Nul}(A) \subseteq \mathbb{R}^n$
> - Soluciones de $A\vec{x} = \vec{0}$
> - $\dim = n - r$ (nulidad)
> - Núcleo de $T(\vec{x}) = A\vec{x}$
> 
> **3. ESPACIO FILA:** $\text{Row}(A) \subseteq \mathbb{R}^n$
> - Combinaciones lineales de filas
> - $\text{Row}(A) = \text{Col}(A^T)$
> - $\dim = \text{rank}(A) = r$
> 
> **4. ESPACIO NULO IZQUIERDO:** $\text{Nul}(A^T) \subseteq \mathbb{R}^m$
> - Soluciones de $A^T\vec{y} = \vec{0}$
> - $\dim = m - r$
> 
> **Relaciones de ortogonalidad:**
> 
> ```mermaid
> graph TB
>     subgraph "ℝⁿ (dominio)"
>         A[Row A<br/>dim = r]
>         B[Nul A<br/>dim = n-r]
>     end
>     
>     subgraph "ℝᵐ (codominio)"
>         C[Col A<br/>dim = r]
>         D[Nul Aᵀ<br/>dim = m-r]
>     end
>     
>     A -.ortogonal.- B
>     C -.ortogonal.- D
>     
>     A -->|A mapea| C
>     B -->|A aniquila| E[0⃗]
>     
>     style A fill:#c8e6c9
>     style B fill:#ffccbc
>     style C fill:#c8e6c9
>     style D fill:#ffccbc
> ```
> 
> **Teorema de la dimensión:**
> 
> **TEOREMA DEL RANGO-NULIDAD:**
> 
> Para $A$ de $m \times n$:
> $$\text{rank}(A) + \text{nullity}(A) = n$$
> 
> Es decir:
> $$\dim(\text{Col}(A)) + \dim(\text{Nul}(A)) = n$$
> 
> **INTERPRETACIÓN:**
> - $n$ = dimensión del dominio
> - $\text{rank}(A)$ = dimensión de la imagen
> - $\text{nullity}(A)$ = dimensión del núcleo
> 
> "La dimensión se conserva al aplicar $T$"
> 
> **EJEMPLO:**
> 
> Si $A$ es $5 \times 7$ con $\text{rank}(A) = 3$:
> - $\text{Col}(A) \subseteq \mathbb{R}^5$, $\dim(\text{Col}(A)) = 3$
> - $\text{Nul}(A) \subseteq \mathbb{R}^7$, $\dim(\text{Nul}(A)) = 7 - 3 = 4$

## 💡 Ejemplos Resueltos

> [!example]- Problemas Detallados
> **Problema 1: Encontrar base y dimensión**
> 
> Sea 
> $$A = \begin{bmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 3 & 7 \\ 3 & 6 & 4 & 10 \end{bmatrix}$$
> 
> Encontrar base de $\text{Col}(A)$ y su dimensión.
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Reducir a forma escalonada**
> 
> $$\begin{bmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 3 & 7 \\ 3 & 6 & 4 & 10 \end{bmatrix}$$
> 
> $$F_2 - 2F_1 \rightarrow \begin{bmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 1 \\ 3 & 6 & 4 & 10 \end{bmatrix}$$
> 
> $$F_3 - 3F_1 \rightarrow \begin{bmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix}$$
> 
> $$F_3 - F_2 \rightarrow \begin{bmatrix} 1 & 2 & 1 & 3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> $$\text{RREF:} \quad \begin{bmatrix} 1 & 2 & 0 & 2 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **PASO 2: Identificar pivotes**
> 
> Columnas pivote: 1 y 3
> 
> **PASO 3: Base de Col(A)**
> 
> Tomar columnas 1 y 3 de $A$ ORIGINAL:
> 
> $$\text{Base: } \left\{\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix}\right\}$$
> 
> **RESPUESTA:**
> - Base de $\text{Col}(A)$: $\left\{\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix}\right\}$
> - $\dim(\text{Col}(A)) = 2$
> - $\text{Col}(A)$ es un plano en $\mathbb{R}^3$
> 
> **VERIFICACIÓN:**
> 
> $$\vec{c}_2 = 2\vec{c}_1: \quad \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} = 2\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \quad \checkmark$$
> 
> $$\vec{c}_4 = 2\vec{c}_1 + \vec{c}_3: \quad \begin{bmatrix} 3 \\ 7 \\ 10 \end{bmatrix} = 2\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} \quad \checkmark$$
> 
> ---
> 
> **Problema 2: Determinar si $\vec{b} \in \text{Col}(A)$**
> 
> Sea 
> $$A = \begin{bmatrix} 1 & 3 & 4 \\ 2 & 7 & 9 \\ 1 & 4 & 5 \end{bmatrix}, \quad \vec{b} = \begin{bmatrix} 2 \\ 5 \\ 3 \end{bmatrix}$$
> 
> Determinar si $\vec{b}$ está en $\text{Col}(A)$.
> 
> **SOLUCIÓN:**
> 
> **MÉTODO 1: Sistema aumentado**
> 
> Resolver $A\vec{x} = \vec{b}$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 3 & 4 & 2 \\ 2 & 7 & 9 & 5 \\ 1 & 4 & 5 & 3 \end{array}\right]$$
> 
> $$F_2 - 2F_1 \rightarrow \left[\begin{array}{ccc|c} 1 & 3 & 4 & 2 \\ 0 & 1 & 1 & 1 \\ 1 & 4 & 5 & 3 \end{array}\right]$$
> 
> $$F_3 - F_1 \rightarrow \left[\begin{array}{ccc|c} 1 & 3 & 4 & 2 \\ 0 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \end{array}\right]$$
> 
> $$F_3 - F_2 \rightarrow \left[\begin{array}{ccc|c} 1 & 3 & 4 & 2 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]$$
> 
> Sistema consistente $\checkmark$
> 
> Por tanto: $\vec{b} \in \text{Col}(A)$
> 
> **Solución:** 
> - $x_3 = t$ (libre)
> - $x_2 = 1 - t$
> - $x_1 = 2 - 3(1-t) - 4t = -1 - t$
> 
> **Verificación con $t = 0$:**
> 
> $$\vec{x} = \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}$$
> 
> $$A\vec{x} = -1\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 3 \\ 7 \\ 4 \end{bmatrix} + 0\begin{bmatrix} 4 \\ 9 \\ 5 \end{bmatrix}$$
> 
> $$= \begin{bmatrix} -1 \\ -2 \\ -1 \end{bmatrix} + \begin{bmatrix} 3 \\ 7 \\ 4 \end{bmatrix} = \begin{bmatrix} 2 \\ 5 \\ 3 \end{bmatrix} = \vec{b} \quad \checkmark$$
> 
> ---
> 
> **Problema 3: Ecuación vectorial**
> 
> Expresar $\vec{b} = \begin{bmatrix} 5 \\ 11 \\ 8 \end{bmatrix}$ como combinación lineal de las columnas de:
> 
> $$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 2 & 3 \end{bmatrix}$$
> 
> **SOLUCIÓN:**
> 
> Queremos: $x_1\vec{c}_1 + x_2\vec{c}_2 = \vec{b}$
> 
> Esto es: $A\vec{x} = \vec{b}$
> 
> $$\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & 4 & 11 \\ 2 & 3 & 8 \end{array}\right]$$
> 
> $$F_2 - 3F_1 \rightarrow \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -2 & -4 \\ 2 & 3 & 8 \end{array}\right]$$
> 
> $$F_3 - 2F_1 \rightarrow \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -2 & -4 \\ 0 & -1 & -2 \end{array}\right]$$
> 
> $$F_2/(-2) \rightarrow \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & 2 \\ 0 & -1 & -2 \end{array}\right]$$
> 
> $$F_3 + F_2 \rightarrow \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{array}\right]$$
> 
> $$F_1 - 2F_2 \rightarrow \left[\begin{array}{cc|c} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{array}\right]$$
> 
> Solución: $x_1 = 1$, $x_2 = 2$
> 
> **RESPUESTA:**
> 
> $$\vec{b} = 1 \cdot \vec{c}_1 + 2 \cdot \vec{c}_2$$
> 
> $$\begin{bmatrix} 5 \\ 11 \\ 8 \end{bmatrix} = 1\begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix} + 2\begin{bmatrix} 2 \\ 4 \\ 3 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$\begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix} + 2\begin{bmatrix} 2 \\ 4 \\ 3 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix} + \begin{bmatrix} 4 \\ 8 \\ 6 \end{bmatrix} = \begin{bmatrix} 5 \\ 11 \\ 8 \end{bmatrix} \quad \checkmark$$
> 
> ---
> 
> **Problema 4: Espacio columna de producto**
> 
> Si $A$ es $m \times n$ y $B$ es $n \times p$, demostrar que:
> $$\text{Col}(AB) \subseteq \text{Col}(A)$$
> 
> **DEMOSTRACIÓN:**
> 
> Sea $\vec{y} \in \text{Col}(AB)$, entonces:
> $$\vec{y} = (AB)\vec{x} \text{ para algún } \vec{x} \in \mathbb{R}^p$$
> 
> Usando asociatividad:
> $$\vec{y} = A(B\vec{x})$$
> 
> Sea $\vec{z} = B\vec{x} \in \mathbb{R}^n$, entonces:
> $$\vec{y} = A\vec{z}$$
> 
> Por tanto: $\vec{y} \in \text{Col}(A)$
> 
> Esto demuestra: $\text{Col}(AB) \subseteq \text{Col}(A) \quad \checkmark$
> 
> **INTERPRETACIÓN:**
> 
> Multiplicar por $B$ (por la derecha) no puede AUMENTAR el espacio columna, solo puede mantenerlo o reducirlo.
> 
> **EJEMPLO:**
> 
> Si $A$ es $3 \times 4$ con $\text{rank}(A) = 3$ (columnas generan $\mathbb{R}^3$) y $B$ es $4 \times 2$, entonces:
> 
> $$\text{rank}(AB) \leq \text{rank}(A) = 3$$
> $$\text{rank}(AB) \leq \text{rank}(B) \leq 2$$
> 
> Por tanto: $\text{rank}(AB) \leq 2$

## ⚡ Propiedades del Rango

> [!important]- Teoremas sobre el Rango
> **Propiedades básicas:**
> 
> Para matrices $A$ y $B$ apropiadas:
> 
> **R1)** $\text{rank}(A) = \text{rank}(A^T)$
> 
> Rango por filas = rango por columnas
> 
> **R2)** $\text{rank}(A + B) \leq \text{rank}(A) + \text{rank}(B)$
> 
> Desigualdad triangular
> 
> **R3)** $\text{rank}(AB) \leq \min\{\text{rank}(A), \text{rank}(B)\}$
> 
> El producto no aumenta rango
> 
> **R4)** Si $A$ es invertible ($n \times n$):
> $$\text{rank}(AB) = \text{rank}(B)$$
> $$\text{rank}(BA) = \text{rank}(B)$$
> 
> Multiplicar por invertible preserva rango
> 
> **R5)** $\text{rank}(A^TA) = \text{rank}(A) = \text{rank}(AA^T)$
> 
> Para cualquier $A$
> 
> **R6)** Si $A$ es $m \times n$:
> $$\text{rank}(A) = m \iff \text{filas son LI}$$
> $$\text{rank}(A) = n \iff \text{columnas son LI}$$
> 
> **Teorema de Sylvester:**
> 
> Para $A$ ($m \times n$) y $B$ ($n \times p$):
> 
> $$\text{rank}(A) + \text{rank}(B) - n \leq \text{rank}(AB) \leq \min\{\text{rank}(A), \text{rank}(B)\}$$
> 
> **INTERPRETACIÓN:**
> - Cota superior: el producto no aumenta rango
> - Cota inferior: pérdida máxima de rango
> 
> **CASO ESPECIAL:**
> 
> Si $\text{rank}(A) = n$ (columnas LI):
> $$\text{rank}(AB) = \text{rank}(B)$$

## 🎯 Aplicaciones del Espacio Columna

> [!note]- Usos Prácticos
> **Consistencia de sistemas:**
> 
> **CRITERIO DE CONSISTENCIA:**
> 
> $$\text{Sistema } A\vec{x} = \vec{b} \text{ tiene solución} \iff \vec{b} \in \text{Col}(A)$$
> 
> **MÉTODO PRÁCTICO:**
> 
> 1. Formar matriz aumentada $[A|\vec{b}]$
> 2. Reducir a forma escalonada
> 3. Si no hay fila $[0 \, 0 \, \cdots \, 0 \, | \, c]$ con $c \neq 0$, entonces $\vec{b} \in \text{Col}(A)$
> 
> **EJEMPLO:**
> 
> $$\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 2 & 4 & 7 \end{array}\right] \rightarrow \left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 1 \end{array}\right] \leftarrow \text{Inconsistente}$$
> 
> $\vec{b} \notin \text{Col}(A)$, sistema sin solución
> 
> **Análisis de transformaciones:**
> 
> Para $T: \mathbb{R}^n \to \mathbb{R}^m$ definida por $T(\vec{x}) = A\vec{x}$:
> 
> - $\text{Col}(A) = \text{Im}(T)$ (imagen de $T$)
> - $\dim(\text{Col}(A)) = \dim(\text{Im}(T)) = \text{rank}(T)$
> - $T$ es sobreyectiva $\iff \text{Col}(A) = \mathbb{R}^m \iff \text{rank}(A) = m$
> 
> **Aproximación de mínimos cuadrados:**
> 
> Problema: $A\vec{x} = \vec{b}$ sin solución exacta
> 
> Solución de mínimos cuadrados: Encontrar $\vec{x}$ que minimiza $\|\vec{A\vec{x}} - \vec{b}\|$
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> - Proyectar $\vec{b}$ sobre $\text{Col}(A)$
> - La proyección $\hat{\vec{b}}$ está en $\text{Col}(A)$
> - $\vec{x}$ es solución de $A\vec{x} = \hat{\vec{b}}$
> - Error mínimo: $\|\vec{b} - \hat{\vec{b}}\|$
> 
> $$\vec{b} - \hat{\vec{b}} \perp \text{Col}(A)$$

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes
> **1. "Usar columnas de la forma reducida"**
> 
> ✗ **FALSO**
> 
> La base de $\text{Col}(A)$ se forma con columnas de $A$ ORIGINAL, no de la forma reducida.
> 
> **RAZÓN:**
> 
> Las operaciones por filas cambian el espacio columna.
> 
> **CORRECTO:**
> 1. Reducir para identificar pivotes
> 2. Tomar columnas correspondientes de $A$ original
> 
> ---
> 
> **2. "Col(A) = Col(RREF(A))"**
> 
> ✗ **FALSO** en general
> 
> **Ejemplo:**
> 
> $$A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \quad \text{RREF} = \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$$
> 
> $$\text{Col}(A) = \text{span}\left\{\begin{bmatrix} 1 \\ 2 \end{bmatrix}\right\} \neq \text{Col(RREF)} = \text{span}\left\{\begin{bmatrix} 1 \\ 0 \end{bmatrix}\right\}$$
> 
> Las operaciones por filas NO preservan $\text{Col}(A)$
> 
> ---
> 
> **3. "rank(A + B) = rank(A) + rank(B)"**
> 
> ✗ **FALSO**
> 
> Solo es desigualdad: $\text{rank}(A+B) \leq \text{rank}(A) + \text{rank}(B)$
> 
> **Contraejemplo:**
> 
> $$A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 0 & 0 \\ -1 & 0 \end{bmatrix}$$
> 
> $$\text{rank}(A) = 1, \quad \text{rank}(B) = 1$$
> 
> $$A + B = \begin{bmatrix} 1 & 0 \\ -1 & 0 \end{bmatrix} \implies \text{rank}(A+B) = 1$$
> 
> $$1 \neq 1 + 1 = 2$$
> 
> ---
> 
> **4. "Todas las columnas están en Col(A)"**
> 
> ✓ **VERDADERO**
> 
> Cada columna $\vec{c}_j$ está en $\text{Col}(A)$ porque:
> $$\vec{c}_j = 0\vec{c}_1 + \cdots + 1\vec{c}_j + \cdots + 0\vec{c}_n$$
> 
> Pero esto NO significa que todas sean necesarias para formar una base (pueden ser LD).
> 
> ---
> 
> **5. "Col(A) depende del orden de columnas"**
> 
> ✗ **FALSO**
> 
> El espacio generado es el mismo independientemente del orden de las columnas.
> 
> Solo cambia cuál base específica elegimos, pero el subespacio es el mismo.
> 
> $$\text{span}\{\vec{c}_1, \vec{c}_2, \vec{c}_3\} = \text{span}\{\vec{c}_3, \vec{c}_1, \vec{c}_2\}$$
> 
> ---
> 
> **6. "Si b⃗ ∉ Col(A), entonces Ax⃗ = b⃗ tiene infinitas soluciones"**
> 
> ✗ **FALSO**
> 
> Si $\vec{b} \notin \text{Col}(A)$, entonces $A\vec{x} = \vec{b}$ NO tiene solución (ninguna, no infinitas).
> 
> **CORRECTO:**
> - $\vec{b} \in \text{Col}(A)$ → sistema consistente (puede tener 1 o infinitas soluciones)
> - $\vec{b} \notin \text{Col}(A)$ → sistema inconsistente (sin solución)
> 
> ---
> 
> **7. "Col(A) siempre tiene dimensión n"**
> 
> ✗ **FALSO**
> 
> Si $A$ es $m \times n$:
> $$\dim(\text{Col}(A)) = \text{rank}(A) \leq \min\{m, n\}$$
> 
> Puede ser menor que $n$ si las columnas son LD.
> 
> **Ejemplo:**
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$$
> 
> $n = 3$ pero $\dim(\text{Col}(A)) = 1$

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales
> **Fundamentos previos:**
> - [[01 - Vectores en espacios vectoriales]] - Espacios y subespacios
> - [[05 - Combinaciones lineales]] - Generación de vectores
> - [[06 - Independencia lineal]] - Bases
> - [[08 - Sistemas de ecuaciones lineales]] - Consistencia
> 
> **Temas relacionados:**
> - [[06 – Espacio fila]] - Dual del espacio columna
> - [[18 - Espacio nulo]] - Kernel de transformación
> - [[19 - Rango y nulidad]] - Teorema fundamental
> - [[20 - Transformaciones lineales]] - Imagen
> 
> **Aplicaciones posteriores:**
> - [[25 - Mínimos cuadrados]] - Proyecciones
> - [[26 - Descomposición QR]] - Ortogonalización
> - [[27 - Valores singulares]] - SVD
> - [[28 - Espacios fundamentales]] - Teoría completa

## 📚 Recursos Adicionales

> [!note]- Herramientas y Referencias
> **Software de álgebra lineal:**
> 
> - **MATLAB**
>   - Funciones: `orth()`, `rank()`, `rref()`
>   - Visualización de espacios vectoriales
> - **Python (NumPy)**
>   ```python
>   import numpy as np
>   A = np.array([[1,2,3],[2,4,5],[3,6,8]])
>   rank = np.linalg.matrix_rank(A)
>   ```
> - **Wolfram Alpha**
>   - "column space {{1,2},{3,4},{5,6}}"
>   - "rank of matrix {{1,2,3},{2,4,5}}"
> 
> **Visualizadores:**
> - **GeoGebra 3D** - Visualizar subespacios en $\mathbb{R}^3$
> - **3Blue1Brown** - Videos sobre espacios fundamentales

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas
> **Nivel introductorio:**
> - **Lay, D. C.** (2016). _Álgebra Lineal y sus Aplicaciones_ (5ª ed.). Pearson.
>   - Cap. 4: Espacios vectoriales
>   - Sección 4.6: Rango
> - **Kolman, B., & Hill, D.** (2006). _Álgebra Lineal_ (8ª ed.). Pearson.
>   - Cap. 5: Espacios fundamentales
> 
> **Nivel intermedio:**
> - **Strang, G.** (2016). _Introduction to Linear Algebra_ (5th ed.). Wellesley-Cambridge.
>   - Cap. 3: Los cuatro subespacios fundamentales
>   - Perspectiva geométrica excepcional
> - **Anton, H., & Rorres, C.** (2014). _Álgebra Lineal Elemental_ (11ª ed.). Wiley.
>   - Cap. 5: Espacios vectoriales generales
> 
> **Nivel avanzado:**
> - **Axler, S.** (2015). _Linear Algebra Done Right_ (3rd ed.). Springer.
>   - Cap. 3: Transformaciones lineales
>   - Tratamiento abstracto del rango

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales
> 
> **DEFINICIONES ESENCIALES:**
> 
> $$\text{Col}(A) = \text{span}\{\vec{c}_1, \vec{c}_2, \ldots, \vec{c}_n\} = \{A\vec{x} : \vec{x} \in \mathbb{R}^n\}$$
> 
> $$\dim(\text{Col}(A)) = \text{rank}(A)$$
> 
> **TEOREMA FUNDAMENTAL:**
> 
> $$A\vec{x} = \vec{b} \text{ tiene solución} \iff \vec{b} \in \text{Col}(A)$$
> 
> **ALGORITMO DE CÁLCULO:**
> 1. Reducir $A$ a RREF
> 2. Identificar columnas pivote
> 3. Tomar columnas correspondientes de $A$ ORIGINAL
> 
> **RELACIONES CLAVE:**
> 
> $$\text{rank}(A) + \text{nullity}(A) = n$$
> 
> $$\text{Col}(A) \subseteq \mathbb{R}^m \text{ donde } A \text{ es } m \times n$$

---

**Tags:** #algebra-lineal #espacio-columna #rango #matriz #sistemas-lineales #transformaciones-lineales #subespacios #imagen #consistencia #combinaciones-lineales
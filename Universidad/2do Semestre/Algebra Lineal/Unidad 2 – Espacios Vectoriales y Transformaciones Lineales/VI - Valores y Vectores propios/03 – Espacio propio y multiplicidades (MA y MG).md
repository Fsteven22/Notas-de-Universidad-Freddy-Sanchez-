# 🎯 Espacios Propios (Eigenspaces)

## 🎯 Introducción

> [!info]- 💡 ¿Qué es un Espacio Propio?
> 
> Un **espacio propio** (o eigenespacio) asociado a un valor propio λ de una matriz A es el conjunto de todos los vectores que son transformados por A en múltiplos de sí mismos (con factor λ), junto con el vector cero.
> 
> **Analogía práctica:** Imagina una transformación lineal como estirar o comprimir el espacio. Los espacios propios son las direcciones especiales que solo se estiran o comprimen, pero no cambian de dirección.
> 
> **¿Por qué son importantes?**
> 
> |Aspecto|Descripción|Ejemplo de Uso|
> |---|---|---|
> |**Diagonalización**|Simplificar matrices|Calcular potencias A^n|
> |**Sistemas dinámicos**|Estudiar evolución a largo plazo|Modelos de población|
> |**Vibraciones**|Análisis de frecuencias naturales|Ingeniería estructural|
> |**Gráficos**|Análisis de componentes principales|Reducción de dimensionalidad|
> |**Mecánica cuántica**|Estados estacionarios|Niveles de energía|

```mermaid
graph TB
    A[Matriz A] --> B[Valores propios λ]
    B --> C[Vector propio v]
    C --> D[Espacio propio E_λ]
    D --> E[Subespacios invariantes]
    
    F[Aplicaciones] --> G[Diagonalización]
    F --> H[Sistemas dinámicos]
    F --> I[PCA]
    
    style A fill:#e1f5ff
    style D fill:#e1ffe1
    style F fill:#fff4e1
```

---
## 🏗️ Definición de Espacio Propio

### 📊 Concepto Formal

> [!success]- 🎨 Espacio Propio E_λ
> 
> Sea A una matriz n×n y λ un valor propio de A. El **espacio propio** asociado a λ, denotado E_λ, es:
> 
> $$E_\lambda = {\vec{v} \in \mathbb{R}^n : A\vec{v} = \lambda\vec{v}} = \text{Nul}(A - \lambda I)$$
> 
> **En palabras:** E_λ es el conjunto de todos los vectores propios asociados a λ, más el vector cero.
> 
> **Componentes:**
> 
> |Elemento|Significado|
> |---|---|
> |**E_λ**|Espacio propio de λ|
> |**Nul(A - λI)**|Núcleo o espacio nulo de (A - λI)|
> |**{v : Av = λv}**|Todos los vectores que cumplen la ecuación|
> |**Incluye 0**|El vector cero siempre está en E_λ|
> 
> **Propiedades fundamentales:**
> 
> 1. **Es un subespacio:** E_λ es un subespacio vectorial de ℝⁿ
> 2. **Contiene al menos un vector no nulo:** Si λ es valor propio, E_λ ≠ {0}
> 3. **Dimensión ≥ 1:** dim(E_λ) ≥ 1 para cada valor propio λ
> 4. **Cerrado bajo combinaciones lineales:** Si v₁, v₂ ∈ E_λ, entonces c₁v₁ + c₂v₂ ∈ E_λ
> 
> **Verificación de subespacio:**
> 
> ```mermaid
> graph TD
>     A["E_λ = Nul(A - λI)"] --> B[¿Contiene 0?]
>     B -->|Sí: A0 = λ0| C[✓]
>     
>     A --> D[¿Cerrado bajo suma?]
>     D -->|v₁,v₂ ∈ E_λ| E["A(v₁+v₂) = λ(v₁+v₂)?"]
>     E -->|Sí| F[✓]
>     
>     A --> G[¿Cerrado bajo mult. escalar?]
>     G -->|v ∈ E_λ, c ∈ ℝ| H["A(cv) = λ(cv)?"]
>     H -->|Sí| I[✓]
>     
>     C --> J[E_λ es subespacio]
>     F --> J
>     I --> J
>     
>     style A fill:#e1f5ff
>     style J fill:#e1ffe1
> ```

### 🔧 Cálculo de Espacios Propios

> [!example]- 🎯 Procedimiento Paso a Paso
> 
> **Para encontrar E_λ:**
> 
> 1. Calcular valores propios de A
> 2. Para cada λ, resolver el sistema homogéneo (A - λI)v = 0
> 3. Encontrar el espacio solución (base del núcleo)
> 4. El espacio propio E_λ = span{vectores base}
> 
> **Ejemplo completo:**
> 
> Encontrar todos los espacios propios de $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$
> 
> ```
> Paso 1: Valores propios (ya calculados)
> λ₁ = 4, λ₂ = 2
> 
> Paso 2: Espacio propio para λ₁ = 4
> 
> (A - 4I)v = 0
> ([3-4   1  ][v₁]) = [0]
>  [1     3-4][v₂]    [0]
> 
> ([-1  1][v₁]) = [0]
>  [1  -1][v₂]    [0]
> 
> Sistema: -v₁ + v₂ = 0  →  v₂ = v₁
> 
> Solución general: v = [v₁] = v₁[1]
>                       [v₁]     [1]
> 
> Base de E₄: {[1, 1]ᵀ}
> 
> E₄ = span{[1, 1]ᵀ} = {t[1, 1]ᵀ : t ∈ ℝ}
> dim(E₄) = 1
> 
> Paso 3: Espacio propio para λ₂ = 2
> 
> (A - 2I)v = 0
> ([3-2   1  ][v₁]) = [0]
>  [1     3-2][v₂]    [0]
> 
> ([1  1][v₁]) = [0]
>  [1  1][v₂]    [0]
> 
> Sistema: v₁ + v₂ = 0  →  v₂ = -v₁
> 
> Solución general: v = [ v₁] = v₁[ 1]
>                       [-v₁]     [-1]
> 
> Base de E₂: {[1, -1]ᵀ}
> 
> E₂ = span{[1, -1]ᵀ} = {t[1, -1]ᵀ : t ∈ ℝ}
> dim(E₂) = 1
> 
> Respuesta:
> E₄ = span{[1, 1]ᵀ}
> E₂ = span{[1, -1]ᵀ}
> ```
> 
> **Interpretación geométrica (2D):**
> 
> ```mermaid
> graph LR
>     A[Plano ℝ²] --> B[E₄: recta y = x]
>     A --> C[E₂: recta y = -x]
>     
>     B --> D[Vectores se estiran 4×]
>     C --> E[Vectores se estiran 2×]
>     
>     style A fill:#e1f5ff
>     style B fill:#e1ffe1
>     style C fill:#fff4e1
> ```

---
## 🎓 Propiedades de los Espacios Propios

### 📋 Propiedades Fundamentales

> [!tip]- 🔧 Teoremas Importantes
> 
> **Propiedad 1: Independencia lineal**
> 
> Vectores propios correspondientes a valores propios **distintos** son linealmente independientes.
> 
> ```
> Si Av₁ = λ₁v₁ y Av₂ = λ₂v₂ con λ₁ ≠ λ₂
> Entonces {v₁, v₂} es LI
> ```
> 
> **Propiedad 2: Suma directa**
> 
> Si λ₁, λ₂, ..., λₖ son valores propios distintos:
> 
> $$E_{\lambda_1} \oplus E_{\lambda_2} \oplus \cdots \oplus E_{\lambda_k} \subseteq \mathbb{R}^n$$
> 
> Los espacios propios para diferentes valores propios son "independientes".
> 
> **Propiedad 3: Bases y diagonalización**
> 
> A es diagonalizable si y solo si:
> 
> $$\dim(E_{\lambda_1}) + \dim(E_{\lambda_2}) + \cdots + \dim(E_{\lambda_k}) = n$$
> 
> Es decir: la suma de las dimensiones de todos los espacios propios = n
> 
> **Propiedad 4: Invariancia**
> 
> Los espacios propios son **invariantes** bajo A:
> 
> Si v ∈ E_λ, entonces Av ∈ E_λ
> 
> **Tabla resumen:**
> 
> |Propiedad|Condición|Consecuencia|
> |---|---|---|
> |**Independencia**|λᵢ ≠ λⱼ|vᵢ y vⱼ son LI|
> |**Suma directa**|Valores propios distintos|E_λᵢ ∩ E_λⱼ = {0}|
> |**Diagonalización**|Σ dim(E_λᵢ) = n|A es diagonalizable|
> |**Invariancia**|v ∈ E_λ|Av ∈ E_λ|

---

## 🎯 Aplicaciones

### 🔄 Diagonalización de Matrices

> [!success]- 🎨 Proceso de Diagonalización
> 
> Una matriz A es **diagonalizable** si existe una matriz invertible P tal que:
> 
> $$A = PDP^{-1}$$
> 
> donde D es diagonal.
> 
> **Construcción de P y D:**
> 
> - **Columnas de P:** vectores propios de A
> - **Diagonal de D:** valores propios correspondientes
> 
> ```mermaid
> flowchart TD
>     A[Matriz A] --> B[Calcular valores propios]
>     B --> C[Calcular espacios propios]
>     C --> D{Σ dim(E_λᵢ) = n?}
>     D -->|Sí| E[A es diagonalizable]
>     D -->|No| F[A NO es diagonalizable]
>     
>     E --> G[Formar P con vectores propios]
>     E --> H[Formar D con valores propios]
>     G --> I[A = PDP⁻¹]
>     H --> I
>     
>     style A fill:#e1f5ff
>     style E fill:#e1ffe1
>     style F fill:#ffe1e1
>     style I fill:#fff4e1
> ```
> 
> **Ejemplo completo:**
> 
> Diagonalizar $A = \begin{bmatrix} 3 & 1 \ 1 & 3 \end{bmatrix}$
> 
> ```
> Paso 1: Valores propios (ya calculados)
> λ₁ = 4, λ₂ = 2
> 
> Paso 2: Vectores propios (ya calculados)
> v₁ = [1, 1]ᵀ para λ₁ = 4
> v₂ = [1, -1]ᵀ para λ₂ = 2
> 
> Paso 3: Verificar diagonalizabilidad
> dim(E₄) + dim(E₂) = 1 + 1 = 2 = n ✓
> 
> Paso 4: Formar matrices
> P = [v₁ | v₂] = [1   1]
>                 [1  -1]
> 
> D = [λ₁  0 ] = [4  0]
>     [0   λ₂]   [0  2]
> 
> Paso 5: Calcular P⁻¹
> P⁻¹ = 1/det(P) · [adjunta de P]
>     = 1/(-2) · [-1  -1]
>                [-1   1]
>     = [1/2   1/2]
>       [1/2  -1/2]
> 
> Paso 6: Verificar
> PDP⁻¹ = [1   1][4  0][1/2   1/2]
>         [1  -1][0  2][1/2  -1/2]
>       
>       = [1   1][2    2]
>         [1  -1][1   -1]
>       
>       = [3  1]  = A ✓
>         [1  3]
> ```

### 📊 Potencias de Matrices

> [!example]- 🚀 Cálculo Eficiente de A^n
> 
> Si A = PDP⁻¹, entonces:
> 
> $$A^n = PD^nP^{-1}$$
> 
> y calcular D^n es trivial (elevar elementos diagonales):
> 
> $$D^n = \begin{bmatrix} \lambda_1^n & 0 & \cdots \ 0 & \lambda_2^n & \cdots \ \vdots & \vdots & \ddots \end{bmatrix}$$
> 
> **Ejemplo:**
> 
> Calcular A¹⁰⁰ para $A = \begin{bmatrix} 3 & 1 \ 1 & 3 \end{bmatrix}$
> 
> ```
> Paso 1: Usar diagonalización conocida
> A = PDP⁻¹ donde:
> P = [1   1]    D = [4  0]    P⁻¹ = [1/2   1/2]
>     [1  -1]        [0  2]          [1/2  -1/2]
> 
> Paso 2: Calcular D¹⁰⁰
> D¹⁰⁰ = [4¹⁰⁰    0  ]
>        [0     2¹⁰⁰]
> 
> Paso 3: Calcular A¹⁰⁰
> A¹⁰⁰ = PD¹⁰⁰P⁻¹
>      = [1   1][4¹⁰⁰    0  ][1/2   1/2]
>        [1  -1][0     2¹⁰⁰][1/2  -1/2]
>      
>      = [1   1][4¹⁰⁰/2    4¹⁰⁰/2 ]
>        [1  -1][2¹⁰⁰/2   -2¹⁰⁰/2]
>      
>      = [(4¹⁰⁰ + 2¹⁰⁰)/2    (4¹⁰⁰ - 2¹⁰⁰)/2]
>        [(4¹⁰⁰ - 2¹⁰⁰)/2    (4¹⁰⁰ + 2¹⁰⁰)/2]
> 
> Sin diagonalización esto sería prácticamente imposible!
> ```

---

## 📊 Resumen Visual

> [!note]- 📐 Mapa Conceptual
> 
> ```mermaid
> mindmap
>   root((Espacios<br/>Propios))
>     Valores propios λ
>       Ecuación característica
>       det(A - λI) = 0
>       Raíces del polinomio
>     Vectores propios v
>       Av = λv
>       v ≠ 0
>       Dirección invariante
>     Espacio propio E_λ
>       Subespacio
>       E_λ = Nul(A - λI)
>       dim(E_λ) ≥ 1
>     Multiplicidades
>       Algebraica MA
>       Geométrica MG  
>       1 ≤ MG ≤ MA
>     Aplicaciones
>       Diagonalización
>       Potencias de matrices
>       Sistemas dinámicos
> ```
> 
> **Tabla de fórmulas clave:**
> 
> |Concepto|Fórmula|Interpretación|
> |---|---|---|
> |**Ecuación característica**|det(A - λI) = 0|Encontrar λ|
> |**Espacio propio**|E_λ = {v : Av = λv}|Conjunto de vectores|
> |**Dimensión**|dim(E_λ) = MG(λ)|Multiplicidad geométrica|
> |**Diagonalización**|A = PDP⁻¹|P = vectores propios|
> |**Potencias**|A^n = PD^nP⁻¹|Cálculo eficiente|

---

## 🎓 Ejemplos Completos

> [!example]- 📝 Problema 1: Matriz 3×3
> 
> **Enunciado:** Encontrar todos los espacios propios y verificar si es diagonalizable:
> 
> $$A = \begin{bmatrix} 2 & 0 & 0 \ 1 & 2 & -1 \ 1 & 0 & 1 \end{bmatrix}$$
> 
> ```
> Solución:
> 
> Paso 1: Calcular polinomio característico
> det(A - λI) = det([2-λ   0     0  ])
>                  [1     2-λ   -1  ]
>                  [1     0     1-λ ]
> 
> Expandiendo por primera fila:
> = (2-λ) · det([2-λ   -1 ])
>              [0     1-λ]
> = (2-λ)[(2-λ)(1-λ) - 0]
> = (2-λ)(2-λ)(1-λ)
> = (2-λ)²(1-λ)
> 
> Paso 2: Valores propios
> λ₁ = 2 con MA(2) = 2
> λ₂ = 1 con MA(1) = 1
> 
> Paso 3: Espacio propio E₂
> (A - 2I)v = 0
> ([0   0    0][v₁])   ([0])
> [1 0 -1][v₂] = [0] [1 0 -1][v₃] [0]
> 
> Sistema: v₁ - v₃ = 0 → v₁ = v₃ v₂ libre
> 
> Solución: v = [v₃] = v₂[0] + v₃[1] [v₂] [1] [0] [v₃] [0] [1]
> 
> E₂ = span{[0,1,0]ᵀ, [1,0,1]ᵀ} MG(2) = 2 ✓ (MG = MA)
> 
> Paso 4: Espacio propio E₁ (A - I)v = 0 ([1 0 0][v₁]) ([0]) [1 1 -1][v₂] = [0] [1 0 0][v₃] [0]
> 
> Sistema: v₁ = 0 v₁ + v₂ - v₃ = 0 → v₂ = v₃
> 
> Solución: v = [0 ] = v₃[0] [v₃] [1] [v₃] [1]
> 
> E₁ = span{[0,1,1]ᵀ} MG(1) = 1 ✓ (MG = MA)
> 
> Paso 5: Verificar diagonalizabilidad dim(E₂) + dim(E₁) = 2 + 1 = 3 ✓
> 
> A es diagonalizable con: P = [0 1 0] D = [2 0 0] [1 0 1] [0 2 0] [0 1 1] [0 0 1]
> 
> Respuesta: E₂ = span{[0,1,0]ᵀ, [1,0,1]ᵀ} E₁ = span{[0,1,1]ᵀ} A es diagonalizable
> ```

---

**Tags:** #algebra-lineal #espacios-propios #valores-propios #vectores-propios #diagonalizacion #multiplicidad #subespacios #eigenspaces

# 🔢 Multiplicidad Algebraica y Geométrica

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Multiplicidades?
> 
> Las **multiplicidades** son conceptos fundamentales que describen "cuántas veces" aparece un valor propio, pero desde dos perspectivas diferentes:
> 
> - **Algebraica:** desde el polinomio característico
> - **Geométrica:** desde el espacio de vectores propios
> 
> **Analogía práctica:** Imagina una orquesta donde el director (valor propio) puede tener:
> 
> - **Multiplicidad algebraica:** cuántas sillas están asignadas para ese director
> - **Multiplicidad geométrica:** cuántos músicos independientes realmente ocupan esas sillas
> 
> **¿Por qué son importantes?**
> 
> |Aspecto|Descripción|Ejemplo de Uso|
> |---|---|---|
> |**Diagonalización**|Determinar si A es diagonalizable|Condición: MG = MA para todos los λ|
> |**Estructura**|Entender la forma de la matriz|Bloques de Jordan|
> |**Sistemas dinámicos**|Comportamiento a largo plazo|Estabilidad de soluciones|
> |**Dimensión**|Contar vectores propios independientes|Bases de espacios propios|

```mermaid
graph TB
    A[Valor propio λ] --> B[Multiplicidad Algebraica MA]
    A --> C[Multiplicidad Geométrica MG]
    
    B --> D[Del polinomio característico]
    C --> E[Del espacio propio E_λ]
    
    D --> F[Raíces repetidas]
    E --> G[Vectores LI]
    
    H[Relación] --> I[1 ≤ MG ≤ MA]
    I --> J{MG = MA?}
    J -->|Para todos λ| K[Diagonalizable]
    J -->|Existe λ con MG < MA| L[NO diagonalizable]
    
    style A fill:#e1f5ff
    style K fill:#e1ffe1
    style L fill:#ffe1e1
```

---

## 📐 Multiplicidad Algebraica (MA)

### 🎨 Definición Formal

> [!note]- 📘 Concepto de Multiplicidad Algebraica
> 
> Sea λ un valor propio de la matriz A (n×n). La **multiplicidad algebraica** de λ, denotada MA(λ) o alg(λ), es la **multiplicidad de λ como raíz del polinomio característico**.
> 
> $$\text{MA}(\lambda) = \text{exponente de } (\lambda - \lambda_i) \text{ en } p_A(\lambda)$$
> 
> **Polinomio característico factorizado:**
> 
> $$p_A(\lambda) = \det(A - \lambda I) = (\lambda - \lambda_1)^{m_1}(\lambda - \lambda_2)^{m_2} \cdots (\lambda - \lambda_k)^{m_k}$$
> 
> donde:
> 
> - λ₁, λ₂, ..., λₖ son los valores propios **distintos**
> - m₁, m₂, ..., mₖ son sus multiplicidades algebraicas
> 
> **Componentes:**
> 
> |Símbolo|Significado|Restricción|
> |---|---|---|
> |**MA(λ)**|Multiplicidad algebraica|≥ 1|
> |**p_A(λ)**|Polinomio característico|Grado n|
> |**mᵢ**|Exponente de (λ - λᵢ)|1 ≤ mᵢ ≤ n|
> |**Σmᵢ**|Suma de multiplicidades|= n|
> 
> **Propiedades fundamentales:**
> 
> ```mermaid
> graph LR
>     A[Matriz A n×n] --> B[Polinomio p_A de grado n]
>     B --> C[n raíces contadas con multiplicidad]
>     C --> D["Σ MA(λᵢ) = n"]
>     
>     E[Cada valor propio] --> F["MA(λ) ≥ 1"]
>     
>     style A fill:#e1f5ff
>     style D fill:#e1ffe1
> ```
> 
> **Tabla de propiedades:**
> 
> |Propiedad|Descripción|Fórmula|
> |---|---|---|
> |**Suma total**|Suma de todas las MA|Σ MA(λᵢ) = n|
> |**Mínimo**|Cada valor propio cuenta al menos una vez|MA(λ) ≥ 1|
> |**Máximo**|No puede exceder n|MA(λ) ≤ n|
> |**Valores distintos**|Si todos λᵢ distintos|MA(λᵢ) = 1 para todo i|

### 📝 Ejemplos de Cálculo

> [!example]- 🎯 Ejemplos Detallados
> 
> **Ejemplo 1: MA simple (todos distintos)**
> 
> $$A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3 \end{bmatrix}$$
> 
> ```
> Paso 1: Polinomio característico
> p_A(λ) = det(A - λI) = det([1-λ  0    0  ])
>                           [0    2-λ  0  ]
>                           [0    0    3-λ]
> = (1-λ)(2-λ)(3-λ)
> 
> Paso 2: Factorización
> p_A(λ) = (λ-1)¹(λ-2)¹(λ-3)¹
> 
> Paso 3: Multiplicidades algebraicas
> λ₁ = 1: MA(1) = 1
> λ₂ = 2: MA(2) = 1
> λ₃ = 3: MA(3) = 1
> 
> Verificar: Σ MA = 1 + 1 + 1 = 3 = n ✓
> ```
> 
> **Ejemplo 2: MA repetidas**
> 
> $$A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 5 \end{bmatrix}$$
> 
> ```
> Paso 1: Polinomio característico (matriz triangular)
> p_A(λ) = (2-λ)(2-λ)(5-λ)
>        = (2-λ)²(5-λ)
>        = (λ-2)²(λ-5)
> 
> Paso 2: Multiplicidades algebraicas
> λ₁ = 2: MA(2) = 2  ← valor propio repetido
> λ₂ = 5: MA(5) = 1
> 
> Verificar: Σ MA = 2 + 1 = 3 = n ✓
> ```
> 
> **Ejemplo 3: MA máxima**
> 
> $$A = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{bmatrix}$$
> 
> ```
> Paso 1: Polinomio característico (triangular)
> p_A(λ) = (3-λ)³
>        = (λ-3)³
> 
> Paso 2: Multiplicidad algebraica
> λ = 3: MA(3) = 3  ← único valor propio con MA máxima
> 
> Verificar: Σ MA = 3 = n ✓
> ```

---

## 🏗️ Multiplicidad Geométrica (MG)

### 📊 Definición Formal

> [!success]- 🎨 Concepto de Multiplicidad Geométrica
> 
> Sea λ un valor propio de la matriz A (n×n). La **multiplicidad geométrica** de λ, denotada MG(λ) o geo(λ), es la **dimensión del espacio propio** E_λ.
> 
> $$\text{MG}(\lambda) = \dim(E_\lambda) = \dim(\text{Nul}(A - \lambda I))$$
> 
> **En otras palabras:**
> 
> MG(λ) = número máximo de vectores propios **linealmente independientes** asociados a λ
> 
> **Componentes:**
> 
> |Concepto|Fórmula|Interpretación|
> |---|---|---|
> |**E_λ**|{v : Av = λv}|Espacio propio|
> |**Nul(A-λI)**|{v : (A-λI)v = 0}|Núcleo o espacio nulo|
> |**dim(E_λ)**|Número de vectores en base de E_λ|MG(λ)|
> |**Base de E_λ**|{v₁, v₂, ..., vₘ} donde m = MG(λ)|Vectores LI|
> 
> **Proceso de cálculo:**
> 
> ```mermaid
> flowchart TD
>     A[Valor propio λ] --> B[Formar A - λI]
>     B --> C[Resolver A - λI v = 0]
>     C --> D[Encontrar espacio solución]
>     D --> E[Determinar base del espacio]
>     E --> F[Contar vectores en la base]
>     F --> G[MG = # vectores en base]
>     
>     style A fill:#e1f5ff
>     style G fill:#e1ffe1
> ```
> 
> **Relación con el rango:**
> 
> $$\text{MG}(\lambda) = \dim(\text{Nul}(A - \lambda I)) = n - \text{rango}(A - \lambda I)$$
> 
> Por el teorema de la dimensión: $$n = \text{rango}(A - \lambda I) + \text{nulidad}(A - \lambda I)$$

### 📝 Ejemplos de Cálculo

> [!example]- 🎯 Cálculo de MG
> 
> **Ejemplo 1: MG = 1 (caso simple)**
> 
> Para $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ con λ = 3
> 
> ```
> Paso 1: Formar A - λI
> A - 3I = [2-3   1  ] = [-1  1]
>          [1    2-3]   [1  -1]
> 
> Paso 2: Resolver (A - 3I)v = 0
> [-1  1][v₁] = [0]
> [1  -1][v₂]   [0]
> 
> Sistema: -v₁ + v₂ = 0  →  v₂ = v₁
> 
> Paso 3: Solución general
> v = [v₁] = v₁[1]  = t[1]
>     [v₁]     [1]     [1]
> 
> Paso 4: Base de E₃
> Base = {[1, 1]ᵀ}
> 
> Paso 5: Multiplicidad geométrica
> MG(3) = dim(E₃) = 1
> 
> Solo hay UN vector propio LI para λ = 3
> ```
> 
> **Ejemplo 2: MG = 2 (dos vectores LI)**
> 
> Para $A = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 5 \end{bmatrix}$ con λ = 2
> 
> ```
> Paso 1: Formar A - λI
> A - 2I = [0  0  0]
>          [0  0  0]
>          [0  0  3]
> 
> Paso 2: Resolver (A - 2I)v = 0
> [0  0  0][v₁]   [0]
> [0  0  0][v₂] = [0]
> [0  0  3][v₃]   [0]
> 
> Sistema: 3v₃ = 0  →  v₃ = 0
>          v₁, v₂ libres
> 
> Paso 3: Solución general
> v = [v₁]   [1]     [0]
>     [v₂] = v₁[0] + v₂[1]
>     [0 ]   [0]     [0]
> 
> Paso 4: Base de E₂
> Base = {[1,0,0]ᵀ, [0,1,0]ᵀ}
> 
> Paso 5: Multiplicidad geométrica
> MG(2) = dim(E₂) = 2
> 
> Hay DOS vectores propios LI para λ = 2
> ```
> 
> **Ejemplo 3: MG < MA (deficiente)**
> 
> Para $A = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{bmatrix}$ con λ = 2
> 
> ```
> Sabemos: MA(2) = 3 (del polinomio (λ-2)³)
> 
> Paso 1: Formar A - 2I
> A - 2I = [0  1  0]
>          [0  0  0]
>          [0  0  0]
> 
> Paso 2: Resolver (A - 2I)v = 0
> [0  1  0][v₁]   [0]
> [0  0  0][v₂] = [0]
> [0  0  0][v₃]   [0]
> 
> Sistema: v₂ = 0
>          v₁, v₃ libres
> 
> Paso 3: Solución general
> v = [v₁]   [1]     [0]
>     [0 ] = v₁[0] + v₃[0]
>     [v₃]   [0]     [1]
> 
> Paso 4: Base de E₂
> Base = {[1,0,0]ᵀ, [0,0,1]ᵀ}
> 
> Paso 5: Multiplicidad geométrica
> MG(2) = 2
> 
> ¡MG(2) = 2 < 3 = MA(2)!
> Hay solo DOS vectores propios LI, pero MA dice que "debería" haber 3
> ```

---

## ⚖️ Relación entre MA y MG

### 🎯 Teorema Fundamental

> [!success]- 📐 Desigualdad Fundamental
> 
> **Teorema:** Para cualquier valor propio λ de una matriz A:
> 
> $$1 \leq \text{MG}(\lambda) \leq \text{MA}(\lambda)$$
> 
> **Componentes de la desigualdad:**
> 
> |Parte|Significado|
> |---|---|
> |**1 ≤ MG**|Siempre hay al menos un vector propio|
> |**MG ≤ MA**|No puede haber más vectores LI que raíces|
> 
> **Interpretación:**
> 
> ```mermaid
> graph LR
>     A[MG = 1] --> B[Mínimo: un vector propio]
>     C[MG < MA] --> D[Deficiente: matriz NO diagonalizable]
>     E[MG = MA] --> F[Ideal: suficientes vectores propios]
>     G[MG > MA] --> H[IMPOSIBLE]
>     
>     style B fill:#e1f5ff
>     style D fill:#ffe1e1
>     style F fill:#e1ffe1
>     style H fill:#ff0000
> ```
> 
> **Casos posibles:**
> 
> |Relación|Descripción|Consecuencia|
> |---|---|---|
> |**MG = MA**|Caso ideal|Contribuye a diagonalización|
> |**MG < MA**|Deficiencia|Impide diagonalización|
> |**MG > MA**|Imposible|No puede ocurrir|

### 🔍 Condición de Diagonalización

> [!tip]- 🎨 Criterio de Diagonalización
> 
> **Teorema de Diagonalización:**
> 
> Una matriz A (n×n) es **diagonalizable** si y solo si:
> 
> $$\text{MG}(\lambda_i) = \text{MA}(\lambda_i) \quad \text{para todo valor propio } \lambda_i$$
> 
> **Equivalentemente:**
> 
> $$\sum_{i=1}^{k} \text{MG}(\lambda_i) = n$$
> 
> donde k es el número de valores propios distintos.
> 
> **Análisis de casos:**
> 
> ```mermaid
> flowchart TD
>     A[Matriz A n×n] --> B[Calcular todos los valores propios]
>     B --> C[Para cada λᵢ]
>     C --> D[Calcular MA λᵢ]
>     C --> E[Calcular MG λᵢ]
>     
>     D --> F{¿MG = MA?}
>     E --> F
>     
>     F -->|Para todos λᵢ| G[A es DIAGONALIZABLE]
>     F -->|Existe λᵢ con MG < MA| H[A NO es diagonalizable]
>     
>     G --> I[Existe base de vectores propios]
>     H --> J[Insuficientes vectores propios]
>     
>     style A fill:#e1f5ff
>     style G fill:#e1ffe1
>     style H fill:#ffe1e1
> ```
> 
> **Checklist de verificación:**
> 
> - [ ] Encontrar todos los valores propios distintos
> - [ ] Para cada λ, calcular MA del polinomio
> - [ ] Para cada λ, calcular MG del espacio propio
> - [ ] Comparar: ¿MG = MA para todos los λ?
> - [ ] Si todos cumplen: diagonalizable ✓
> - [ ] Si alguno no cumple: NO diagonalizable ✗

---

## 📊 Ejemplos Completos

### 🎓 Análisis Detallado de Matrices

> [!example]- 📝 Ejemplo 1: Matriz Diagonalizable
> 
> **Enunciado:** Analizar multiplicidades y diagonalización de:
> 
> $$A = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{bmatrix}$$
> 
> ```
> PASO 1: MULTIPLICIDADES ALGEBRAICAS
> 
> Polinomio característico (matriz triangular):
> p_A(λ) = (1-λ)(1-λ)(3-λ)
>        = (1-λ)²(3-λ)
>        = (λ-1)²(λ-3)
> 
> Valores propios:
> λ₁ = 1: MA(1) = 2
> λ₂ = 3: MA(3) = 1
> 
> Verificar: 2 + 1 = 3 = n ✓
> 
> PASO 2: MULTIPLICIDAD GEOMÉTRICA PARA λ = 1
> 
> A - I = [0  2  0]
>         [0  0  0]
>         [0  0  2]
> 
> Resolver (A - I)v = 0:
> 2v₂ = 0  →  v₂ = 0
> 2v₃ = 0  →  v₃ = 0
> v₁ libre
> 
> Espacio solución:
> v = [v₁]   [1]
>     [0 ] = v₁[0]
>     [0 ]   [0]
> 
> Base de E₁: {[1,0,0]ᵀ}
> MG(1) = 1
> 
> ¡Problema! MG(1) = 1 < 2 = MA(1)
> 
> PASO 3: MULTIPLICIDAD GEOMÉTRICA PARA λ = 3
> 
> A - 3I = [-2  2  0]
>          [0  -2  0]
>          [0   0  0]
> 
> Resolver (A - 3I)v = 0:
> -2v₁ + 2v₂ = 0  →  v₁ = v₂
> -2v₂ = 0  →  v₂ = 0, luego v₁ = 0
> v₃ libre
> 
> Espacio solución:
> v = [0 ]   [0]
>     [0 ] = v₃[0]
>     [v₃]   [1]
> 
> Base de E₃: {[0,0,1]ᵀ}
> MG(3) = 1 = MA(3) ✓
> 
> PASO 4: CONCLUSIÓN
> 
> Resumen de multiplicidades:
> λ = 1: MA = 2, MG = 1  ✗ (MG < MA)
> λ = 3: MA = 1, MG = 1  ✓ (MG = MA)
> 
> Total de vectores propios LI: 1 + 1 = 2 < 3
> 
> A NO ES DIAGONALIZABLE
> Razón: Deficiencia en λ = 1
> ```

> [!example]- 📝 Ejemplo 2: Matriz Diagonalizable
> 
> **Enunciado:** Analizar multiplicidades y diagonalización de:
> 
> $$A = \begin{bmatrix} 4 & 0 & 0 \\ 1 & 4 & 0 \\ 0 & 0 & 5 \end{bmatrix}$$
> 
> ```
> PASO 1: MULTIPLICIDADES ALGEBRAICAS
> 
> Polinomio característico:
> p_A(λ) = (4-λ)²(5-λ)
>        = (λ-4)²(λ-5)
> 
> Valores propios:
> λ₁ = 4: MA(4) = 2
> λ₂ = 5: MA(5) = 1
> 
> PASO 2: MULTIPLICIDAD GEOMÉTRICA PARA λ = 4
> 
> A - 4I = [0  0  0]
>          [1  0  0]
>          [0  0  1]
> 
> Resolver (A - 4I)v = 0:
> v₁ = 0
> v₃ = 0
> v₂ libre
> 
> Espacio solución:
> v = [0 ]   [0]
>     [v₂] = v₂[1]
>     [0 ]   [0]
> 
> Base de E₄: {[0,1,0]ᵀ}
> MG(4) = 1
> 
> ¡Problema! MG(4) = 1 < 2 = MA(4)
> 
> PASO 3: MULTIPLICIDAD GEOMÉTRICA PARA λ = 5
> 
> A - 5I = [-1  0  0]
>          [1  -1  0]
>          [0   0  0]
> 
> Resolver (A - 5I)v = 0:
> -v₁ = 0  →  v₁ = 0
> v₁ - v₂ = 0  →  v₂ = 0
> v₃ libre
> 
> Base de E₅: {[0,0,1]ᵀ}
> MG(5) = 1 = MA(5) ✓
> 
> PASO 4: CONCLUSIÓN
> 
> Resumen:
> λ = 4: MA = 2, MG = 1  ✗
> λ = 5: MA = 1, MG = 1  ✓
> 
> A NO ES DIAGONALIZABLE
> Solo hay 2 vectores propios LI, necesitamos 3
> ```

> [!example]- 📝 Ejemplo 3: Matriz SÍ Diagonalizable
> 
> **Enunciado:** Analizar multiplicidades de:
> 
> $$A = \begin{bmatrix} 2 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 5 \end{bmatrix}$$
> 
> ```
> PASO 1: MULTIPLICIDADES ALGEBRAICAS
> 
> Matriz diagonal por bloques:
> p_A(λ) = (2-λ)³(5-λ)
> 
> λ₁ = 2: MA(2) = 3
> λ₂ = 5: MA(5) = 1
> 
> PASO 2: MULTIPLICIDAD GEOMÉTRICA PARA λ = 2
> 
> A - 2I = [0  0  0  0]
>          [0  0  0  0]
>          [0  0  0  0]
>          [0  0  0  3]
> 
> Resolver (A - 2I)v = 0:
> 3v₄ = 0  →  v₄ = 0
> v₁, v₂, v₃ libres
> 
> Espacio solución:
> v = [v₁]     [1]     [0]     [0]
>     [v₂] = v₁[0] + v₂[1] + v₃[0]
>     [v₃]     [0]     [0]     [1]
>     [0 ]     [0]     [0]     [0]
> 
> Base de E₂: {[1,0,0,0]ᵀ, [0,1,0,0]ᵀ, [0,0,1,0]ᵀ}
> MG(2) = 3 = MA(2) ✓
> 
> PASO 3: MULTIPLICIDAD GEOMÉTRICA PARA λ = 5
> 
> A - 5I = [-3  0  0  0]
>          [0  -3  0  0]
>          [0   0 -3  0]
>          [0   0  0  0]
> 
> Resolver (A - 5I)v = 0:
> -3v₁ = 0  →  v₁ = 0
> -3v₂ = 0  →  v₂ = 0
> -3v₃ = 0  →  v₃ = 0
> v₄ libre
> 
> Base de E₅: {[0,0,0,1]ᵀ}
> MG(5) = 1 = MA(5) ✓
> 
> PASO 4: CONCLUSIÓN
> 
> Resumen:
> λ = 2: MA = 3, MG = 3  ✓
> λ = 5: MA = 1, MG = 1  ✓
> 
> Total: 3 + 1 = 4 vectores propios LI
> 
> A ES DIAGONALIZABLE ✓
> 
> Matriz de diagonalización:
> P = [[1,0,0,0]ᵀ | [0,1,0,0]ᵀ | [0,0,1,0]ᵀ | [0,0,0,1]ᵀ]
> 
> D = [2  0  0  0]
>     [0  2  0  0]
>     [0  0  2  0]
>     [0  0  0  5]
> ```

---

## 📋 Tabla Resumen y Comparación

> [!note]- 📊 Cuadro Comparativo Completo
> 
> |Aspecto|Multiplicidad Algebraica (MA)|Multiplicidad Geométrica (MG)|
> |---|---|---|
> |**Definición**|Exponente en p_A(λ)|dim(E_λ)|
> |**Cálculo**|Del polinomio característico|Del espacio nulo|
> |**Fórmula**|Raíz repetida m veces|# vectores en base de E_λ|
> |**Rango**|1 ≤ MA ≤ n|1 ≤ MG ≤ MA|
> |**Información**|"Cuántas veces aparece λ"|"Cuántos vectores propios LI"|
> |**Siempre es...**|≥ MG|≤ MA|
> |**Para diagonalización**|No suficiente por sí sola|Debe igualar MA|
> 
> **Casos especiales:**
> 
> |Situación|MA|MG|¿Diagonalizable?|Ejemplo|
> |---|---|---|---|---|
> |Valores propios distintos|Todas = 1|Todas = 1|✓ Sí|Matriz diagonal|
> |λ con MA = n|n|Varía|Dep||. de MG | A = kI tiene MG = n |
> | Deficiente | > MG | < MA | ✗ No | Matrices de Jordan | | Ideal | = MG | = MA | ✓ Sí | Matrices simétricas |

---

## 🎯 Estrategia de Análisis

> [!tip]- 🗺️ Guía Paso a Paso
> ```mermaid
> flowchart TD
>     A[Matriz A]
>     A --> B[Calcular polinomio característico]
>     B --> C["Factorizar p_A(λ)"]
>     C --> D[Identificar valores propios]
>     D --> E[Determinar MA de cada λ]
> 
>     E --> F[Para cada valor propio λᵢ]
>     F --> G[Formar A − λᵢI]
>     G --> H["Resolver (A − λᵢI)v = 0"]
>     H --> I[Encontrar base de E_λᵢ]
>     I --> J["Calcular MG(λᵢ)"]
> 
>     J --> K{"¿MG(λᵢ) = MA(λᵢ)?"}
>     K -->|Sí, todos| L[DIAGONALIZABLE]
>     K -->|No| M[NO diagonalizable]
> 
>     L --> N[Formar matriz P]
>     L --> O[Formar matriz D]
> 
> ```

**Tags:** #algebra-lineal #multiplicidad #algebraica #geometrica #diagonalizacion #valores-propios #espacios-propios #vectores-propios
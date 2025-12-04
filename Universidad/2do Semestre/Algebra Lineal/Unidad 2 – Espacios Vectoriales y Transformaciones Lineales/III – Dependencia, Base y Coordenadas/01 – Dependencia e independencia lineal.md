# 📘 Dependencia e Independencia Lineal

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante la Independencia Lineal?
> 
> Cuando trabajamos con un conjunto de vectores, surge una pregunta fundamental: **¿Hay vectores redundantes en nuestro conjunto?**
> 
> **Motivación:**
> 
> - Algunos vectores pueden "fabricarse" a partir de otros
> - Esto significa que son **redundantes** (no aportan información nueva)
> - Queremos identificar conjuntos sin redundancia
> - Esto optimiza representaciones y cálculos
> 
> **Analogía:**
> 
> - **Receta de cocina:** Si ya tienes harina, azúcar y huevos, agregar "mezcla de harina y azúcar" es redundante
> - **Direcciones:** Si puedes llegar a cualquier lugar con Norte y Este, agregar "Noreste" no te da nuevas posibilidades
> - **Datos:** Variables que pueden calcularse a partir de otras no añaden información
> 
> **Preguntas fundamentales:**
> 
> - ¿Todos los vectores en mi conjunto son necesarios?
> - ¿Puedo expresar un vector como combinación de los otros?
> - ¿Cuál es el conjunto mínimo que genera el mismo espacio?
> 
> **Aplicaciones prácticas:**
> 
> - **Compresión de datos:** Eliminar redundancia
> - **Machine Learning:** Selección de características independientes
> - **Sistemas de ecuaciones:** Detectar ecuaciones redundantes
> - **Gráficos computacionales:** Bases eficientes para transformaciones
> - **Análisis numérico:** Evitar problemas de inestabilidad

---

## 📝 Definición de Dependencia Lineal

### 🔑 Definición Formal

> [!example]- 🟢 Definición: Dependencia Lineal
> 
> **Definición:** Un conjunto de vectores $S = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ en un espacio vectorial $V$ es **linealmente dependiente** si existen escalares $c_1, c_2, \ldots, c_n$, **no todos cero**, tales que:
> 
> $$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n = \vec{0}$$
> 
> ---
> 
> **En otras palabras:**
> 
> - Puedes obtener el vector cero como combinación lineal
> - Al menos uno de los coeficientes es diferente de cero
> - Esto significa que al menos un vector es combinación de los otros
> 
> ---
> 
> **Interpretación crucial:**
> 
> Si $c_k \neq 0$, entonces podemos despejar:
> 
> $$\vec{v}_k = -\frac{c_1}{c_k}\vec{v}_1 - \cdots - \frac{c_{k-1}}{c_k}\vec{v}_{k-1} - \frac{c_{k+1}}{c_k}\vec{v}_{k+1} - \cdots - \frac{c_n}{c_k}\vec{v}_n$$
> 
> Es decir, **al menos un vector se puede escribir como combinación de los otros**.
> 
> ---
> 
> **Observaciones importantes:**
> 
> 1. La combinación **trivial** $0\vec{v}_1 + 0\vec{v}_2 + \cdots + 0\vec{v}_n = \vec{0}$ siempre existe
> 2. Dependencia significa que existe una combinación **no trivial** que da cero
> 3. Si un conjunto es dependiente, al menos un vector es redundante

### 🔍 Casos Especiales de Dependencia

> [!note]- 📋 Casos Importantes
> 
> ### 1. Conjunto con el Vector Cero
> 
> **Teorema:** Si $\vec{0} \in S$, entonces $S$ es **linealmente dependiente**.
> 
> **Demostración:**
> 
> Si $S = {\vec{0}, \vec{v}_2, \ldots, \vec{v}_n}$, entonces:
> 
> $$1 \cdot \vec{0} + 0\vec{v}_2 + \cdots + 0\vec{v}_n = \vec{0}$$
> 
> Esta es una combinación no trivial (coeficiente 1 ≠ 0) que da cero. ✓
> 
> **Conclusión:** El vector cero siempre hace que un conjunto sea dependiente.
> 
> ---
> 
> ### 2. Vectores Paralelos (Proporcionales)
> 
> **Teorema:** Si dos vectores son paralelos (uno es múltiplo escalar del otro), el conjunto es linealmente dependiente.
> 
> **Ejemplo:** Si $\vec{v}_2 = k\vec{v}_1$, entonces:
> 
> $$k\vec{v}_1 - \vec{v}_2 = \vec{0}$$
> 
> o equivalentemente: $-k\vec{v}_1 + 1\vec{v}_2 = \vec{0}$
> 
> **Casos geométricos en $\mathbb{R}^2$ y $\mathbb{R}^3$:**
> 
> - Dos vectores en la misma dirección (o dirección opuesta)
> - Tres vectores en el mismo plano (coplanares) en $\mathbb{R}^3$
> 
> ---
> 
> ### 3. Más Vectores que Dimensión
> 
> **Teorema Fundamental:** En $\mathbb{R}^n$, cualquier conjunto de **más de $n$ vectores** es linealmente dependiente.
> 
> **Ejemplos:**
> 
> - En $\mathbb{R}^2$: Cualquier conjunto de 3 o más vectores es dependiente
> - En $\mathbb{R}^3$: Cualquier conjunto de 4 o más vectores es dependiente
> - En general: $n+1$ vectores en $\mathbb{R}^n$ siempre son dependientes
> 
> **Intuición:** No puedes tener más "direcciones independientes" que la dimensión del espacio.
> 
> ---
> 
> ### 4. Un Solo Vector
> 
> **Teorema:** El conjunto ${\vec{v}}$ con un solo vector es:
> 
> - **Dependiente** si y solo si $\vec{v} = \vec{0}$
> - **Independiente** si y solo si $\vec{v} \neq \vec{0}$
> 
> **Razón:** La única combinación $c\vec{v} = \vec{0}$ con $\vec{v} \neq \vec{0}$ requiere $c = 0$.

---

## 📘 Definición de Independencia Lineal

### 🔑 Definición Formal

> [!example]- 🟢 Definición: Independencia Lineal
> 
> **Definición:** Un conjunto de vectores $S = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ es **linealmente independiente** si la **única** forma de obtener el vector cero como combinación lineal es usando **todos los coeficientes iguales a cero**:
> 
> $$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n = \vec{0} \implies c_1 = c_2 = \cdots = c_n = 0$$
> 
> ---
> 
> **En otras palabras:**
> 
> - Solo la combinación **trivial** produce el vector cero
> - No hay forma no trivial de obtener cero
> - Ningún vector puede expresarse como combinación de los otros
> - **No hay redundancia** en el conjunto
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - Cada vector aporta una "dirección nueva"
> - Ningún vector está en el span de los otros
> - Son vectores que apuntan en direcciones "verdaderamente diferentes"
> 
> ---
> 
> **Relación con dependencia:**
> 
> Un conjunto es linealmente independiente si y solo si **NO** es linealmente dependiente.
> 
> $$\text{Independiente} \iff \neg\text{Dependiente}$$

### 🎯 Caracterizaciones Equivalentes

> [!note]- 🔄 Formas Equivalentes de Independencia
> 
> Las siguientes afirmaciones son **equivalentes** para $S = {\vec{v}_1, \ldots, \vec{v}_n}$:
> 
> ### (1) Definición Estándar
> 
> $$c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = \vec{0} \implies c_1 = \cdots = c_n = 0$$
> 
> ---
> 
> ### (2) Ningún Vector en el Span de los Otros
> 
> $$\vec{v}_i \notin \text{span}(\vec{v}_1, \ldots, \vec{v}_{i-1}, \vec{v}_{i+1}, \ldots, \vec{v}_n)$$
> 
> para todo $i = 1, 2, \ldots, n$
> 
> ---
> 
> ### (3) Representación Única
> 
> Cada vector en $\text{span}(S)$ se puede escribir de **manera única** como combinación lineal de vectores en $S$.
> 
> Si $\vec{w} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = d_1\vec{v}_1 + \cdots + d_n\vec{v}_n$
> 
> entonces $c_i = d_i$ para todo $i$.
> 
> ---
> 
> ### (4) Sistema Homogéneo con Única Solución
> 
> El sistema $[\ \vec{v}_1 \ | \ \vec{v}_2 \ | \ \cdots \ | \ \vec{v}_n \ ]\vec{c} = \vec{0}$ tiene solo la solución trivial $\vec{c} = \vec{0}$.
> 
> ---
> 
> ### (5) Eliminar Cualquier Vector Reduce el Span
> 
> $$\text{span}(S \setminus {\vec{v}_i}) \neq \text{span}(S)$$
> 
> para todo vector $\vec{v}_i \in S$
> 
> **Interpretación:** Todos los vectores son **esenciales** para generar el espacio.

---

## 🎨 Interpretación Geométrica

### Visualización en $\mathbb{R}^2$

> [!note]- 📊 En el Plano
> 
> ### Dos Vectores Independientes
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \end{bmatrix}$$
> 
> ```
>       y
>       |
>     2 |
>       |  v₂
>     1 |  ↑
>       |  
>     0 +------→---- x
>       0  1  v₁  2
> 
>     Independientes: direcciones diferentes
> ```
> 
> **Características:**
> 
> - No son paralelos
> - No están en la misma recta
> - Generan todo $\mathbb{R}^2$
> - Ninguno es múltiplo del otro
> 
> ---
> 
> ### Dos Vectores Dependientes
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 2 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 2 \ 4 \end{bmatrix}$$
> 
> ```
>       y
>       |
>     4 |    • v₂
>       |   /
>     2 |  • v₁
>       | /
>     0 +-------------- x
>       0   1   2
> 
>     Dependientes: misma dirección
>     v₂ = 2v₁
> ```
> 
> **Características:**
> 
> - Son paralelos ($\vec{v}_2 = 2\vec{v}_1$)
> - Están en la misma recta
> - Solo generan una recta (no todo $\mathbb{R}^2$)
> - Uno es múltiplo del otro
> 
> ---
> 
> ### Tres Vectores en $\mathbb{R}^2$
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \end{bmatrix}, \quad \vec{v}_3 = \begin{bmatrix} 1 \ 1 \end{bmatrix}$$
> 
> ```
>       y
>       |
>     2 |
>       |  v₂
>     1 |  ↑  • v₃
>       |    ↗
>     0 +------→---- x
>       0  1  v₁  2
> 
>     Dependientes: v₃ = v₁ + v₂
>     (3 vectores en R² siempre son dependientes)
> ```
> 
> **Observación:** $\vec{v}_3 = \vec{v}_1 + \vec{v}_2$, entonces:
> 
> $$1\vec{v}_1 + 1\vec{v}_2 - 1\vec{v}_3 = \vec{0}$$
> 
> Combinación no trivial que da cero → **Dependientes**

### Visualización en $\mathbb{R}^3$

> [!note]- 📊 En el Espacio
> 
> ### Dos Vectores Independientes en $\mathbb{R}^3$
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}$$
> 
> ```
>         z
>         |
>         |
>         |
>         +----------- y
>        /|    v₂ →
>       // |
>      //  |
>     x   
>     ↓ v₁
> 
>     Independientes: generan el plano xy
> ```
> 
> **Características:**
> 
> - No son paralelos
> - Generan un **plano** en $\mathbb{R}^3$
> - Ninguno está en el span del otro
> 
> ---
> 
> ### Tres Vectores Independientes en $\mathbb{R}^3$
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \quad \vec{v}_3 = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> ```
>         z
>         | v₃
>         ↑
>         |
>         +-------→--- y
>        /|      v₂
>       // |
>      ↓  |
>     x   
>     v₁
> 
>     Independientes: generan todo R³
> ```
> 
> **Características:**
> 
> - Tres direcciones completamente diferentes
> - No son coplanares (no están en el mismo plano)
> - Generan **todo** $\mathbb{R}^3$
> - Son los vectores canónicos
> 
> ---
> 
> ### Tres Vectores Dependientes (Coplanares)
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \quad \vec{v}_3 = \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}$$
> 
> ```
>         z
>         |
>         |
>         |
>         +----------- y
>        /|  Todos en
>       // |  el plano xy
>      //  |  v₃ = v₁ + v₂
>     x
> 
>     Dependientes: coplanares
> ```
> 
> **Observación:** $\vec{v}_3 = \vec{v}_1 + \vec{v}_2$
> 
> Entonces: $1\vec{v}_1 + 1\vec{v}_2 - 1\vec{v}_3 = \vec{0}$
> 
> Todos están en el mismo plano → **Dependientes**

---

## 🔍 Métodos para Determinar Independencia

### Método 1: Sistema de Ecuaciones Homogéneo

> [!note]- 🎯 Procedimiento Estándar
> 
> **Objetivo:** Determinar si ${\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ es linealmente independiente.
> 
> ---
> 
> **Procedimiento:**
> 
> **Paso 1:** Plantear el sistema homogéneo
> 
> $$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n = \vec{0}$$
> 
> **Paso 2:** Escribir como sistema matricial
> 
> $$[\ \vec{v}_1 \ | \ \vec{v}_2 \ | \ \cdots \ | \ \vec{v}_n \ ] \begin{bmatrix} c_1 \ c_2 \ \vdots \ c_n \end{bmatrix} = \vec{0}$$
> 
> **Paso 3:** Reducir la matriz a forma escalonada (REF o RREF)
> 
> **Paso 4:** Analizar las soluciones:
> 
> - ✅ **Solo solución trivial** ($c_1 = c_2 = \cdots = c_n = 0$) → **Independiente**
> - ❌ **Tiene soluciones no triviales** → **Dependiente**
> 
> ---
> 
> **Criterios de decisión:**
> 
> ### Para Independencia:
> 
> - Cada columna debe tener un **pivote**
> - No hay variables libres
> - El sistema tiene rango completo: $\text{rango} = n$
> 
> ### Para Dependencia:
> 
> - Al menos una columna sin pivote
> - Hay variables libres
> - El sistema tiene rango incompleto: $\text{rango} < n$

### Método 2: Determinante (Solo Matrices Cuadradas)

> [!note]- 🔢 Método del Determinante
> 
> **Aplicable cuando:** Los vectores forman una **matriz cuadrada** (igual número de vectores que componentes).
> 
> ---
> 
> **Teorema:** Sea $A = [\ \vec{v}_1 \ | \ \vec{v}_2 \ | \ \cdots \ | \ \vec{v}_n \ ]$ una matriz $n \times n$.
> 
> $${\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n} \text{ es independiente} \iff \det(A) \neq 0$$
> 
> ---
> 
> **Equivalentemente:**
> 
> - **$\det(A) \neq 0$** → Los vectores son **linealmente independientes**
> - **$\det(A) = 0$** → Los vectores son **linealmente dependientes**
> 
> ---
> 
> **Ejemplo:**
> 
> $$\vec{v}_1 = \begin{bmatrix} 1 \ 2 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 3 \ 4 \end{bmatrix}$$
> 
> $$A = \begin{bmatrix} 1 & 3 \ 2 & 4 \end{bmatrix}$$
> 
> $$\det(A) = (1)(4) - (3)(2) = 4 - 6 = -2 \neq 0$$
> 
> $$\boxed{\text{Linealmente independientes}}$$
> 
> ---
> 
> **Limitación:** Solo funciona cuando el número de vectores = dimensión del espacio.

### Método 3: Inspección (Casos Simples)

> [!note]- 👁️ Detección Visual
> 
> **Casos obvios de DEPENDENCIA:**
> 
> 1. **Vector cero incluido:** Si $\vec{0} \in S$ → Dependiente
>     
> 2. **Vectores proporcionales:** Si $\vec{v}_i = k\vec{v}_j$ → Dependiente
>     
> 3. **Más vectores que dimensión:** En $\mathbb{R}^n$, si $|S| > n$ → Dependiente
>     
> 4. **Uno es combinación obvia:** Si ves que $\vec{v}_3 = \vec{v}_1 + \vec{v}_2$ → Dependiente
>     
> 
> ---
> 
> **Casos obvios de INDEPENDENCIA:**
> 
> 1. **Vectores canónicos:** ${\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n}$ → Independiente
>     
> 2. **Un vector no nulo:** ${\vec{v}}$ con $\vec{v} \neq \vec{0}$ → Independiente
>     
> 3. **Dos vectores no paralelos en $\mathbb{R}^2$** → Independiente
>     
> 4. **Tres vectores no coplanares en $\mathbb{R}^3$** → Independiente
>     

---

## 📚 Ejemplos Detallados

### Ejemplo 1: Verificar Independencia en $\mathbb{R}^3$

> [!example]- 📝 Ejemplo 1: Tres Vectores en $\mathbb{R}^3$
> 
> **Dado:** $$S = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 4 \ 5 \ 6 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 7 \ 8 \ 9 \end{bmatrix} \right\}$$
> 
> **Pregunta:** ¿Es $S$ linealmente independiente?
> 
> ---
> 
> **Solución por Sistema de Ecuaciones:**
> 
> **Paso 1:** Plantear
> 
> $$c_1\begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix} + c_2\begin{bmatrix} 4 \ 5 \ 6 \end{bmatrix} + c_3\begin{bmatrix} 7 \ 8 \ 9 \end{bmatrix} = \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$$
> 
> **Paso 2:** Sistema de ecuaciones
> 
> $$\begin{cases} c_1 + 4c_2 + 7c_3 = 0 \ 2c_1 + 5c_2 + 8c_3 = 0 \ 3c_1 + 6c_2 + 9c_3 = 0 \end{cases}$$
> 
> **Paso 3:** Matriz aumentada
> 
> $$\left[\begin{array}{ccc|c} 1 & 4 & 7 & 0 \ 2 & 5 & 8 & 0 \ 3 & 6 & 9 & 0 \end{array}\right]$$
> 
> **Paso 4:** Reducción por filas
> 
> $R_2 - 2R_1$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 4 & 7 & 0 \ 0 & -3 & -6 & 0 \ 3 & 6 & 9 & 0 \end{array}\right]$$
> 
> $R_3 - 3R_1$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 4 & 7 & 0 \ 0 & -3 & -6 & 0 \ 0 & -6 & -12 & 0 \end{array}\right]$$
> 
> $R_3 - 2R_2$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 4 & 7 & 0 \ 0 & -3 & -6 & 0 \ 0 & 0 & 0 & 0 \end{array}\right]$$
> 
> **Paso 5:** Análisis
> 
> - Solo hay **2 pivotes** (columnas 1 y 2)
> - $c_3$ es **variable libre**
> - Hay **infinitas soluciones** (no solo la trivial)
> 
> **De $R_2$:** $-3c_2 - 6c_3 = 0 \Rightarrow c_2 = -2c_3$
> 
> **De $R_1$:** $c_1 + 4(-2c_3) + 7c_3 = 0 \Rightarrow c_1 = c_3$
> 
> **Solución general:**
> 
> $$\begin{bmatrix} c_1 \ c_2 \ c_3 \end{bmatrix} = c_3\begin{bmatrix} 1 \ -2 \ 1 \end{bmatrix}, \quad c_3 \in \mathbb{R}$$
> 
> **Ejemplo de solución no trivial:** $c_3 = 1$:
> 
> $$1\vec{v}_1 - 2\vec{v}_2 + 1\vec{v}_3 = \vec{0}$$
> 
> **Verificación:**
> 
> $$\begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix} - 2\begin{bmatrix} 4 \ 5 \ 6 \end{bmatrix} + \begin{bmatrix} 7 \ 8 \ 9 \end{bmatrix} = \begin{bmatrix} 1-8+7 \ 2-10+8 \ 3-12+9 \end{bmatrix} = \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$$ ✓
> 
> $$\boxed{\text{LINEALMENTE DEPENDIENTES}}$$
> 
> **Interpretación:** $\vec{v}_3 = 2\vec{v}_2 - \vec{v}_1$ (redundante)

### Ejemplo 2: Vectores Canónicos

> [!example]- 📝 Ejemplo 2: Base Canónica de $\mathbb{R}^3$
> 
> **Dado:** $$S = \left\{ \vec{e}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \vec{e}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \vec{e}_3 = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} \right\}$$
> 
> **Pregunta:** ¿Es $S$ linealmente independiente?
> 
> ---
> 
> **Solución:**
> 
> **Método 1: Sistema de ecuaciones**
> 
> $$c_1\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} + c_3\begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} = \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$$
> 
> $$\begin{bmatrix} c_1 \ c_2 \ c_3 \end{bmatrix} = \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$$
> 
> Solo $c_1 = c_2 = c_3 = 0$ satisface esto.
> 
> ---
> 
> **Método 2: Determinante**
> 
> $$A = \begin{bmatrix} 1 & 0 & 0 \ 0 & 1 & 0 \ 0 & 0 & 1 \end{bmatrix}$$
> 
> $$\det(A) = 1 \neq 0$$
> 
> ---
> 
> **Método 3: Forma escalonada**
> 
> La matriz ya está en forma escalonada reducida:
> $$\begin{bmatrix} 1 & 0 & 0 \ 0 & 1 & 0 \ 0 & 0 & 1 \end{bmatrix}$$
> - Todas las columnas tienen pivote
> - No hay variables libres
> - Rango = 3 (completo)
> 
> $$\boxed{\text{LINEALMENTE INDEPENDIENTES}}$$
> 
> **Conclusión:** Los vectores canónicos siempre son linealmente independientes en $\mathbb{R}^n$.

### Ejemplo 3: Dependencia con Vector Cero

> [!example]- 📝 Ejemplo 3: Conjunto con Vector Cero
> 
> **Dado:** $$S = \left\{ \begin{bmatrix} 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 4 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \end{bmatrix} \right\}$$
> 
> **Pregunta:** ¿Es $S$ linealmente independiente?
> 
> ---
> 
> **Solución:**
> 
> **Por inspección:** Como $\vec{0} \in S$, sabemos inmediatamente que es **dependiente**.
> 
> **Demostración explícita:**
> 
> $$0\begin{bmatrix} 1 \ 2 \end{bmatrix} + 0\begin{bmatrix} 3 \ 4 \end{bmatrix} + 1\begin{bmatrix} 0 \ 0 \end{bmatrix} = \begin{bmatrix} 0 \ 0 \end{bmatrix}$$
> 
> Esta es una combinación **no trivial** (coeficiente $c_3 = 1 \neq 0$) que da el vector cero.
> 
> $$\boxed{\text{LINEALMENTE DEPENDIENTES}}$$
> 
> **Lección:** El vector cero **siempre** hace que un conjunto sea dependiente.

### Ejemplo 4: Vectores en $\mathbb{R}^2$

> [!example]- 📝 Ejemplo 4: Dos Vectores no Paralelos
> 
> **Dado:** $$S = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 2 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 3 \ 5 \end{bmatrix} \right\}$$
> 
> **Pregunta:** ¿Es $S$ linealmente independiente?
> 
> ---
> 
> **Solución por Determinante:**
> 
> $$A = \begin{bmatrix} 1 & 3 \ 2 & 5 \end{bmatrix}$$
> 
> $$\det(A) = (1)(5) - (3)(2) = 5 - 6 = -1 \neq 0$$
> 
> $$\boxed{\text{LINEALMENTE INDEPENDIENTES}}$$
> 
> ---
> 
> **Verificación geométrica:**
> 
> - ¿Es $\vec{v}_2$ múltiplo de $\vec{v}_1$?
> - Si $\vec{v}_2 = k\vec{v}_1$, entonces $\begin{bmatrix} 3 \ 5 \end{bmatrix} = k\begin{bmatrix} 1 \ 2 \end{bmatrix}$
> - Esto requiere: $3 = k$ y $5 = 2k$
> - De la primera: $k = 3$
> - De la segunda: $k = 2.5$
> - Contradicción → No son paralelos → **Independientes** ✓

### Ejemplo 5: Polinomios

> [!example]- 📝 Ejemplo 5: Polinomios en $P_2$
> 
> **Dado:** $$S = {1, x, x^2}$$ en el espacio $P_2$ (polinomios de grado ≤ 2)
> 
> **Pregunta:** ¿Es $S$ linealmente independiente?
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Plantear
> 
> $$c_1 \cdot 1 + c_2 \cdot x + c_3 \cdot x^2 = 0$$
> 
> (donde $0$ es el polinomio cero: $0 + 0x + 0x^2$)
> 
> **Paso 2:** Escribir explícitamente
> 
> $$c_1 + c_2x + c_3x^2 = 0 + 0x + 0x^2$$
> 
> **Paso 3:** Igualar coeficientes
> 
> Para que dos polinomios sean iguales, **todos** sus coeficientes deben ser iguales:
> 
> $$\begin{cases} c_1 = 0 & \text{(coeficiente de } x^0\text{)} \ c_2 = 0 & \text{(coeficiente de } x^1\text{)} \ c_3 = 0 & \text{(coeficiente de } x^2\text{)} \end{cases}$$
> 
> **Paso 4:** Conclusión
> 
> La única solución es $c_1 = c_2 = c_3 = 0$ (solución trivial).
> 
> $$\boxed{\text{LINEALMENTE INDEPENDIENTES}}$$
> 
> **Observación:** Los monomios ${1, x, x^2, \ldots, x^n}$ siempre son linealmente independientes.

### Ejemplo 6: Matrices

> [!example]- 📝 Ejemplo 6: Matrices 2×2
> 
> **Dado:** $$S = \left\{ A_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, A_2 = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, A_3 = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}, A_4 = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \right\}$$
> 
> **Pregunta:** ¿Es $S$ linealmente independiente en $M_{2 \times 2}$?
> 
> ---
> 
> **Solución:**
> 
> **Paso 1:** Plantear
> 
> $$c_1A_1 + c_2A_2 + c_3A_3 + c_4A_4 = O$$
> 
> donde $O$ es la matriz cero $2 \times 2$.
> 
> **Paso 2:** Expandir
> 
> $$c_1\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + c_2\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} + c_3\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix} + c_4\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$
> 
> $$\begin{bmatrix} c_1 & c_2 \\ c_3 & c_4 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$
> 
> **Paso 3:** Igualar entradas
> 
> $$c_1 = 0, \quad c_2 = 0, \quad c_3 = 0, \quad c_4 = 0$$
> 
> $$\boxed{\text{LINEALMENTE INDEPENDIENTES}}$$
> 
> **Conclusión:** Las matrices canónicas $2 \times 2$ son linealmente independientes.

### Ejemplo 7: Caso con Más Vectores que Dimensión

> [!example]- 📝 Ejemplo 7: Cuatro Vectores en $\mathbb{R}^3$
> 
> **Dado:** $$S = \left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} \right\}$$
> 
> **Pregunta:** ¿Es $S$ linealmente independiente?
> 
> ---
> 
> **Solución:**
> 
> **Por teorema:** Tenemos **4 vectores** en $\mathbb{R}^3$.
> 
> Como $4 > 3$, el conjunto **debe ser** linealmente dependiente.
> 
> $$\boxed{\text{LINEALMENTE DEPENDIENTES}}$$
> 
> ---
> 
> **Demostración explícita:**
> 
> Observamos que:
> 
> $$\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} + \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> Por tanto:
> 
> $$1\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + 1\begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} + 1\begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix} - 1\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} = \vec{0}$$
> 
> Combinación no trivial → **Dependientes** ✓
> 
> **Lección:** En $\mathbb{R}^n$, cualquier conjunto con más de $n$ vectores es automáticamente dependiente.

---

## 🧮 Propiedades de Independencia/Dependencia

> [!note]- ⭐ Propiedades Fundamentales
> 
> ### Propiedad 1: Subconjunto de Conjunto Independiente
> 
> **Teorema:** Si $S$ es linealmente independiente, entonces cualquier **subconjunto** de $S$ también es linealmente independiente.
> 
> $$S \text{ independiente} \implies T \subseteq S \implies T \text{ independiente}$$
> 
> **Contrarecíproco:** Si $T$ es dependiente, entonces cualquier conjunto que contenga a $T$ es dependiente.
> 
> ---
> 
> ### Propiedad 2: Extensión de Conjunto Dependiente
> 
> **Teorema:** Si $S$ es linealmente dependiente, entonces cualquier **superconjunto** de $S$ también es linealmente dependiente.
> 
> $$S \text{ dependiente} \implies S \subseteq T \implies T \text{ dependiente}$$
> 
> **Intuición:** Agregar vectores a un conjunto dependiente no elimina la dependencia.
> 
> ---
> 
> ### Propiedad 3: Agregar Vector al Span
> 
> **Teorema:** Sea $S = {\vec{v}_1, \ldots, \vec{v}_n}$ linealmente independiente y sea $\vec{w} \notin \text{span}(S)$.
> 
> Entonces $S \cup {\vec{w}}$ es **linealmente independiente**.
> 
> **Contrapositivo:** Si $S \cup {\vec{w}}$ es dependiente, entonces $\vec{w} \in \text{span}(S)$.
> 
> ---
> 
> ### Propiedad 4: Caracterización de Dependencia
> 
> **Teorema:** $S = {\vec{v}_1, \ldots, \vec{v}_n}$ es linealmente dependiente si y solo si **al menos un vector** puede escribirse como combinación lineal de los otros.
> 
> $$S \text{ dependiente} \iff \exists i : \vec{v}_i \in \text{span}(\vec{v}_1, \ldots, \vec{v}_{i-1}, \vec{v}_{i+1}, \ldots, \vec{v}_n)$$
> 
> ---
> 
> ### Propiedad 5: Dimensión Máxima
> 
> **Teorema:** En $\mathbb{R}^n$:
> 
> - Un conjunto de **más de $n$ vectores** siempre es dependiente
> - Un conjunto de **$n$ vectores independientes** genera todo $\mathbb{R}^n$
> - Un conjunto de **menos de $n$ vectores** no puede generar todo $\mathbb{R}^n$
> 
> ---
> 
> ### Propiedad 6: Unicidad de Representación
> 
> **Teorema:** Si $S$ es linealmente independiente, entonces cada vector en $\text{span}(S)$ tiene una **representación única** como combinación lineal de vectores en $S$.
> 
> **Demostración:** Si $\vec{w} = \sum a_i\vec{v}_i = \sum b_i\vec{v}_i$, entonces:
> 
> $$\sum (a_i - b_i)\vec{v}_i = \vec{0}$$
> 
> Por independencia: $a_i - b_i = 0$ para todo $i$, es decir, $a_i = b_i$.

---

## 🔄 Relación con Bases y Dimensión

> [!note]- 🔗 Conexión con Conceptos Futuros
> 
> ### Adelanto: Base
> 
> Un conjunto $B$ es una **base** de un espacio vectorial $V$ si:
> 
> 1. $B$ es **linealmente independiente**
> 2. $\text{span}(B) = V$ (genera todo el espacio)
> 
> **Interpretación:**
> 
> - Los vectores de la base son los "bloques constructores" del espacio
> - Son el conjunto generador **mínimo** (sin redundancia)
> - Son el conjunto independiente **máximo**
> 
> ---
> 
> ### Adelanto: Dimensión
> 
> La **dimensión** de un espacio vectorial $V$ es el número de vectores en cualquier base de $V$.
> 
> **Relación con independencia:**
> 
> - En $\mathbb{R}^n$: $\dim(\mathbb{R}^n) = n$
> - Cualquier conjunto de $n$ vectores independientes en $\mathbb{R}^n$ es una base
> - No puede haber más de $n$ vectores independientes en $\mathbb{R}^n$
> 
> ---
> 
> ### Teoremas Importantes (Adelanto)
> 
> **Teorema 1:** Si $\dim(V) = n$, entonces:
> 
> - Cualquier conjunto de más de $n$ vectores es dependiente
> - Cualquier conjunto de $n$ vectores independientes es una base
> 
> **Teorema 2:** Si $S$ tiene $n$ vectores en $\mathbb{R}^n$:
> 
> $$S \text{ independiente} \iff S \text{ genera } \mathbb{R}^n \iff S \text{ es base}$$

---

## 🎯 Algoritmo: Extraer Conjunto Independiente Maximal

> [!note]- 🔧 Procedimiento para Eliminar Dependencia
> 
> **Objetivo:** Dado un conjunto $S$ de vectores, encontrar un subconjunto $S' \subseteq S$ que sea linealmente independiente y que $\text{span}(S') = \text{span}(S)$.
> 
> ---
> 
> ### Método de las Columnas Pivote
> 
> **Algoritmo:**
> 
> **Paso 1:** Formar matriz $A$ con los vectores como columnas
> 
> $$A = [\ \vec{v}_1 \ | \ \vec{v}_2 \ | \ \cdots \ | \ \vec{v}_n \ ]$$
> 
> **Paso 2:** Reducir a forma escalonada reducida (RREF)
> 
> **Paso 3:** Identificar columnas pivote
> 
> **Paso 4:** Los vectores **originales** correspondientes a las columnas pivote forman un conjunto independiente maximal
> 
> ---
> 
> ### Ejemplo del Algoritmo
> 
> **Dado:**
> 
> $$S = \left\{ \vec{v}_1 = \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 2 \ 4 \ 6 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}, \vec{v}_4 = \begin{bmatrix} 3 \ 5 \ 8 \end{bmatrix} \right\}$$
> 
> **Paso 1:** Formar matriz
> 
> $$A = \begin{bmatrix} 1 & 2 & 1 & 3 \ 2 & 4 & 1 & 5 \ 3 & 6 & 2 & 8 \end{bmatrix}$$
> 
> **Paso 2:** Reducir
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 2 & 0 & 2 \ 0 & 0 & 1 & 1 \ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Paso 3:** Columnas pivote: **1 y 3**
> 
> **Paso 4:** Conjunto independiente maximal:
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

## 📊 Tabla Resumen de Criterios

> [!note]- 📋 Guía Rápida de Independencia/Dependencia
> 
> |Situación|Independiente|Dependiente|
> |---|---|---|
> |**Vector cero incluido**|❌ Nunca|✅ Siempre|
> |**Un vector no nulo**|✅ Siempre|❌ Nunca|
> |**Dos vectores paralelos**|❌ Nunca|✅ Siempre|
> |**Dos vectores no paralelos**|✅ Siempre|❌ Nunca|
> |**Más vectores que dimensión**|❌ Nunca|✅ Siempre|
> |**Vectores canónicos**|✅ Siempre|❌ Nunca|
> |**Determinante ≠ 0** (cuadrada)|✅ Sí|❌ No|
> |**Determinante = 0** (cuadrada)|❌ No|✅ Sí|
> |**Todas columnas con pivote**|✅ Sí|❌ No|
> |**Alguna columna sin pivote**|❌ No|✅ Sí|
> |**Solo solución trivial**|✅ Sí|❌ No|
> |**Tiene soluciones no triviales**|❌ No|✅ Sí|

---

## 💡 Estrategias de Resolución

> [!tip]- 🎯 Cómo Abordar Problemas
> 
> ### Para Determinar Independencia:
> 
> **1. Inspección rápida (si aplica):**
> 
> - ¿Hay vector cero? → Dependiente
> - ¿Hay vectores paralelos? → Dependiente
> - ¿Más vectores que dimensión? → Dependiente
> - ¿Vectores canónicos? → Independiente
> 
> **2. Si es matriz cuadrada:**
> 
> - Calcular determinante
> - $\det \neq 0$ → Independiente
> - $\det = 0$ → Dependiente
> 
> **3. Método general:**
> 
> - Plantear $c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = \vec{0}$
> - Formar matriz aumentada
> - Reducir a forma escalonada
> - Analizar pivotes y variables libres
> 
> ---
> 
> ### Para Encontrar Relación de Dependencia:
> 
> **Si el conjunto es dependiente:**
> 
> 1. Resolver el sistema homogéneo
> 2. Encontrar solución no trivial
> 3. Expresar un vector como combinación de los otros
> 
> **Ejemplo:** Si la solución es $c_1 = 2, c_2 = -1, c_3 = 1$:
> 
> $$2\vec{v}_1 - \vec{v}_2 + \vec{v}_3 = \vec{0}$$
> 
> Entonces: $\vec{v}_3 = \vec{v}_2 - 2\vec{v}_1$

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Determinar independencia por inspección:**
> 
> a) $S = \left\{ \begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix} \right\}$
> 
> b) $S = \left\{ \begin{bmatrix} 2 \ 4 \end{bmatrix}, \begin{bmatrix} 1 \ 2 \end{bmatrix} \right\}$
> 
> c) $S = \left\{ \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix} \right\}$
> 
> d) $S = \left\{ \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} \right\}$
> 
> ---
> 
> **2. Verificar usando determinante:**
> 
> a) $S = \left\{ \begin{bmatrix} 1 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 5 \end{bmatrix} \right\}$
> 
> b) $S = \left\{ \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 1 \ 3 \end{bmatrix}, \begin{bmatrix} 1 \ -1 \ 2 \end{bmatrix} \right\}$
> 
> c) $S = \left\{ \begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 3 \ 0 \end{bmatrix} \right\}$
> 
> ---
> 
> **3. Polinomios:**
> 
> Determinar si los siguientes conjuntos son linealmente independientes en $P_2$:
> 
> a) ${1, x+1, x^2}$
> 
> b) ${1, 1+x, 1+x+x^2}$
> 
> c) ${x, x^2, x^3}$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Resolver sistema homogéneo:**
> 
> Determinar si los siguientes conjuntos son linealmente independientes:
> 
> a) $S = \left\{ \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix} \right\}$
> 
> b) $S = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} \right\}$
> 
> c) $S = \left\{ \begin{bmatrix} 1 \ 2 \ 3 \ 4 \end{bmatrix}, \begin{bmatrix} 2 \ 1 \ 4 \ 3 \end{bmatrix}, \begin{bmatrix} 3 \ 3 \ 7 \ 7 \end{bmatrix} \right\}$
> 
> ---
> 
> **5. Encontrar relaciones de dependencia:**
> 
> Para los conjuntos dependientes del ejercicio 4, encontrar:
> 
> a) Una combinación lineal no trivial que da cero
> 
> b) Expresar uno de los vectores como combinación de los otros
> 
> ---
> 
> **6. Matrices:**
> 
> Determinar si las siguientes matrices son linealmente independientes en $M_{2 \times 2}$:
> 
> a) $\left\{ \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \right\}$
> 
> b) $\left\{ \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}, \begin{bmatrix} 9 & 10 \\ 11 & 12 \end{bmatrix} \right\}$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Conjunto independiente maximal:**
> 
> Para cada conjunto, encontrar un subconjunto linealmente independiente maximal:
> 
> a) $S = \left\{ \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 4 \ 2 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 5 \ 4 \end{bmatrix} \right\}$
> 
> b) $S = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 1 \ 2 \ 1 \end{bmatrix} \right\}$
> 
> ---
> 
> **8. Demostrar propiedades:**
> 
> a) Demostrar: Si $S$ es linealmente independiente y $\vec{w} \notin \text{span}(S)$, entonces $S \cup {\vec{w}}$ es linealmente independiente.
> 
> b) Demostrar: Si $S$ es linealmente dependiente, entonces al menos un vector en $S$ puede escribirse como combinación lineal de los otros.
> 
> c) Demostrar: En $\mathbb{R}^n$, cualquier conjunto de más de $n$ vectores es linealmente dependiente.
> 
> ---
> 
> **9. Parámetros:**
> 
> Para qué valores de $k$ el siguiente conjunto es linealmente independiente:
> 
> a) $S = \left\{ \begin{bmatrix} 1 \ 2 \ k \end{bmatrix}, \begin{bmatrix} 2 \ k \ 3 \end{bmatrix}, \begin{bmatrix} k \ 3 \ 1 \end{bmatrix} \right\}$
> b) $S = \left\{ \begin{bmatrix} 1 \ k \end{bmatrix}, \begin{bmatrix} k \ 4 \end{bmatrix} \right\}$
> c) $S = \left\{ \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ k \ 1 \end{bmatrix}, \begin{bmatrix} k \ 1 \ k \end{bmatrix} \right\}$
> 
> ---
> 
> **10. Funciones:**
> 
> Determinar si los siguientes conjuntos de funciones son linealmente independientes:
> 
> a) ${e^x, e^{2x}, e^{3x}}$ en el espacio de funciones continuas
> 
> b) ${\sin(x), \cos(x), \sin(2x)}$
> 
> c) ${1, \sin^2(x), \cos^2(x)}$
> 
> **Sugerencia:** Para funciones, usar el Wronskiano o evaluar en puntos específicos.

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $S = \left\{ \begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix} \right\}$
> 
> **Solución:** Vectores canónicos → **Linealmente independientes**
> 
> **Verificación:** $c_1\begin{bmatrix} 1 \ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \end{bmatrix} = \begin{bmatrix} 0 \ 0 \end{bmatrix}$
> 
> Implica $c_1 = 0$ y $c_2 = 0$ (solo solución trivial) ✓
> 
> $$\boxed{\text{INDEPENDIENTES}}$$
> 
> ---
> 
> **1b)** $S = \left\{ \begin{bmatrix} 2 \ 4 \end{bmatrix}, \begin{bmatrix} 1 \ 2 \end{bmatrix} \right\}$
> 
> **Solución:** $\begin{bmatrix} 2 \ 4 \end{bmatrix} = 2\begin{bmatrix} 1 \ 2 \end{bmatrix}$ (paralelos)
> 
> **Combinación no trivial:** $2\begin{bmatrix} 1 \ 2 \end{bmatrix} - 1\begin{bmatrix} 2 \ 4 \end{bmatrix} = \vec{0}$
> 
> $$\boxed{\text{DEPENDIENTES}}$$
> 
> ---
> 
> **1c)** $S = \left\{ \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix} \right\}$
> 
> **Solución:** Contiene el vector cero → **Automáticamente dependiente**
> 
> **Combinación no trivial:** $0\begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix} + 1\begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix} = \vec{0}$
> 
> $$\boxed{\text{DEPENDIENTES}}$$
> 
> ---
> 
> **1d)** $S = \left\{ \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} \right\}$
> 
> **Solución:** 4 vectores en $\mathbb{R}^3$ → **Más vectores que dimensión** → Dependiente
> 
> **Relación:** $\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix} + \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$
> 
> $$\boxed{\text{DEPENDIENTES}}$$
> 
> ---
> 
> **2a)** $S = \left\{ \begin{bmatrix} 1 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 5 \end{bmatrix} \right\}$
> 
> **Solución por determinante:**
> 
> $$\det\begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix} = (1)(5) - (2)(3) = 5 - 6 = -1 \neq 0$$
> 
> $$\boxed{\text{INDEPENDIENTES}}$$
> 
> ---
> 
> **3a)** ${1, x+1, x^2}$ en $P_2$
> 
> **Plantear:** $c_1(1) + c_2(x+1) + c_3(x^2) = 0$
> 
> $$c_1 + c_2 + c_2x + c_3x^2 = 0$$
> 
> **Igualar coeficientes:**
> 
> $$\begin{cases} c_1 + c_2 = 0 & \text{(constante)} \ c_2 = 0 & \text{(coeficiente de } x\text{)} \ c_3 = 0 & \text{(coeficiente de } x^2\text{)} \end{cases}$$
> 
> De la segunda: $c_2 = 0$
> 
> De la primera: $c_1 = 0$
> 
> De la tercera: $c_3 = 0$
> 
> Solo solución trivial → $$\boxed{\text{INDEPENDIENTES}}$$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $S = \left\{ \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}, \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix} \right\}$
> 
> **Matriz aumentada:**
> 
> $$\left[\begin{array}{ccc|c} 1 & 1 & 2 & 0 \\ 1 & 2 & 3 & 0 \\ 1 & 3 & 4 & 0 \end{array}\right]$$
> 
> **Reducción:**
> 
> $R_2 - R_1$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 1 & 2 & 0 \\ 0 & 1 & 1 & 0 \\ 1 & 3 & 4 & 0 \end{array}\right]$$
> 
> $R_3 - R_1$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 1 & 2 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 2 & 2 & 0 \end{array}\right]$$
> 
> $R_3 - 2R_2$:
> 
> $$\left[\begin{array}{ccc|c} 1 & 1 & 2 & 0 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right]$$
> 
> **Análisis:**
> 
> - Solo 2 pivotes (columnas 1 y 2)
> - $c_3$ es variable libre
> - Hay soluciones no triviales
> 
> $$\boxed{\text{DEPENDIENTES}}$$
> 
> **De $R_2$:** $c_2 + c_3 = 0 \Rightarrow c_2 = -c_3$
> 
> **De $R_1$:** $c_1 + c_2 + 2c_3 = 0 \Rightarrow c_1 = -c_2 - 2c_3 = c_3 - 2c_3 = -c_3$
> 
> **Tomando $c_3 = 1$:** $(c_1, c_2, c_3) = (-1, -1, 1)$
> 
> **Relación de dependencia:**
> 
> $$-\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} - \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix} + \begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix} = \vec{0}$$
> 
> **Despejando $\vec{v}_3$:**
> 
> $$\begin{bmatrix} 2 \ 3 \ 4 \end{bmatrix} = \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} + \begin{bmatrix} 1 \ 2 \ 3 \end{bmatrix}$$
> 
> ---
> 
> **4b)** $S = \left\{ \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} \right\}$
> 
> **Por determinante:**
> 
> $$\det\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{bmatrix}$$
> 
> Expandiendo por la primera fila:
> 
> $$= 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} - 0 + 1 \cdot \det\begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$$
> 
> $$= 1(0-1) + 1(0-1) = -1 - 1 = -2 \neq 0$$
> 
> $$\boxed{\text{INDEPENDIENTES}}$$
> 
> ---
> 
> **6a)** Matrices: $\left\{ \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \right\}$
> 
> **Plantear:**
> 
> $$c_1\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + c_2\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} + c_3\begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$
> 
> $$\begin{bmatrix} c_1 + c_3 & c_2 + c_3 \\ c_2 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \ 0 & 0 \end{bmatrix}$$
> 
> **Ecuaciones:**
> 
> $$\begin{cases} c_1 + c_3 = 0 \ c_2 + c_3 = 0 \ c_2 = 0 \ 0 = 0 \end{cases}$$
> 
> De la tercera: $c_2 = 0$
> 
> De la segunda: $c_3 = 0$
> 
> De la primera: $c_1 = 0$
> 
> Solo solución trivial → $$\boxed{\text{INDEPENDIENTES}}$$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **7a)** $S = \left\{ \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 4 \ 2 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 5 \ 4 \end{bmatrix} \right\}$
> 
> **Formar matriz:**
> 
> $$A = \begin{bmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 1 & 5 \\ 1 & 2 & 2 & 4 \end{bmatrix}$$
> 
> **Reducir a RREF:**
> 
> $$\text{RREF}(A) = \begin{bmatrix} 1 & 2 & 0 & 2 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Columnas pivote:** 1 y 3
> 
> **Conjunto independiente maximal:**
> 
> $$S' = \left\{ \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix} \right\}$$
> 
> **Observaciones:**
> 
> - $\vec{v}_2 = 2\vec{v}_1$ (dependiente de $\vec{v}_1$)
> - $\vec{v}_4 = 2\vec{v}_1 + \vec{v}_3$ (dependiente de $\vec{v}_1$ y $\vec{v}_3$)
> 
> $$\boxed{S' = {\vec{v}_1, \vec{v}_3}}$$
> 
> ---
> 
> **9a)** Para qué valores de $k$ es independiente:
> 
> $$S = \left\{ \begin{bmatrix} 1 \ 2 \ k \end{bmatrix}, \begin{bmatrix} 2 \ k \ 3 \end{bmatrix}, \begin{bmatrix} k \ 3 \ 1 \end{bmatrix} \right\}$$
> 
> **Calcular determinante:**
> 
> $$\det\begin{bmatrix} 1 & 2 & k \\ 2 & k & 3 \\ k & 3 & 1 \end{bmatrix}$$
> 
> Expandiendo por la primera fila:
> 
> $$= 1 \cdot \det\begin{bmatrix} k & 3 \\ 3 & 1 \end{bmatrix} - 2 \cdot \det\begin{bmatrix} 2 & 3 \\ k & 1 \end{bmatrix} + k \cdot \det\begin{bmatrix} 2 & k \\ k & 3 \end{bmatrix}$$
> 
> $$= 1(k - 9) - 2(2 - 3k) + k(6 - k^2)$$
> 
> $$= k - 9 - 4 + 6k + 6k - k^3$$
> 
> $$= -k^3 + 13k - 13$$
> 
> **Para independencia:** $-k^3 + 13k - 13 \neq 0$
> 
> Factorizando: $-(k-1)(k^2+k-13) = 0$
> 
> Raíces: $k = 1$ o $k = \frac{-1 \pm \sqrt{1+52}}{2} = \frac{-1 \pm \sqrt{53}}{2}$
> 
> $$\boxed{k \neq 1, \quad k \neq \frac{-1 + \sqrt{53}}{2}, \quad k \neq \frac{-1 - \sqrt{53}}{2}}$$
> 
> ---
> 
> **9b)** $S = \left\{ \begin{bmatrix} 1 \ k \end{bmatrix}, \begin{bmatrix} k \ 4 \end{bmatrix} \right\}$
> 
> **Determinante:**
> 
> $$\det\begin{bmatrix} 1 & k \ k & 4 \end{bmatrix} = 4 - k^2$$
> 
> **Para independencia:** $4 - k^2 \neq 0$
> 
> $$k^2 \neq 4$$
> 
> $$\boxed{k \neq 2 \text{ y } k \neq -2}$$
> 
> ---
> 
> **10c)** ${1, \sin^2(x), \cos^2(x)}$
> 
> **Análisis:** Sabemos que $\sin^2(x) + \cos^2(x) = 1$ (identidad fundamental)
> 
> Por tanto:
> 
> $$1 \cdot 1 - 1 \cdot \sin^2(x) - 1 \cdot \cos^2(x) = 0$$
> 
> Esta es una combinación no trivial que da la función cero.
> 
> $$\boxed{\text{DEPENDIENTES}}$$

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Independencia Lineal
> 
> ✅ **Definición de Dependencia:**
> 
> - Existe combinación **no trivial** que da cero
> - $c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = \vec{0}$ con algún $c_i \neq 0$
> - Al menos un vector es combinación de los otros
> 
> ✅ **Definición de Independencia:**
> 
> - Solo la combinación **trivial** da cero
> - $c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = \vec{0} \Rightarrow$ todos los $c_i = 0$
> - Ningún vector es combinación de los otros
> - **Sin redundancia**
> 
> ✅ **Casos automáticos de DEPENDENCIA:**
> 
> - Contiene vector cero
> - Vectores paralelos (proporcionales)
> - Más vectores que dimensión del espacio
> - Uno es combinación obvia de otros
> 
> ---
> 
> ### Métodos de Verificación
> 
> ✅ **Sistema homogéneo:**
> 
> 1. Plantear $c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = \vec{0}$
> 2. Formar matriz aumentada
> 3. Reducir a forma escalonada
> 4. Analizar: todas columnas con pivote → Independiente
> 
> ✅ **Determinante (matrices cuadradas):**
> 
> - $\det(A) \neq 0$ → Independiente
> - $\det(A) = 0$ → Dependiente
> 
> ✅ **Inspección:**
> 
> - Detectar casos obvios rápidamente
> - Verificar proporcionalidad
> - Contar vectores vs dimensión
> 
> ---
> 
> ### Aplicaciones Importantes
> 
> ✅ **Bases y dimensión:**
> 
> - Base = conjunto independiente que genera el espacio
> - Dimensión = tamaño de cualquier base
> 
> ✅ **Optimización:**
> 
> - Eliminar redundancia
> - Encontrar representación mínima
> - Comprimir información
> 
> ✅ **Unicidad:**
> 
> - Independencia garantiza representación única
> - Importante para coordenadas y cambio de base

---

## 📊 Diagrama Conceptual

> [!note]- 🌳 Árbol de Conceptos
> 
> ```
> INDEPENDENCIA LINEAL
> │
> ├─ DEPENDENCIA LINEAL
> │  ├─ Definición: ∃ combinación no trivial = 0
> │  ├─ Interpretación: al menos un vector redundante
> │  ├─ Casos automáticos
> │  │  ├─ Vector cero incluido
> │  │  ├─ Vectores paralelos
> │  │  └─ Más vectores que dimensión
> │  └─ Relación de dependencia
> │     └─ Expresar un vector en términos de otros
> │
> ├─ INDEPENDENCIA LINEAL
> │  ├─ Definición: solo combinación trivial = 0
> │  ├─ Interpretación: sin redundancia
> │  ├─ Caracterizaciones equivalentes
> │  │  ├─ Ningún vector en span de otros
> │  │  ├─ Representación única
> │  │  └─ Sistema homogéneo con única solución
> │  └─ Ejemplos estándar
> │     ├─ Vectores canónicos
> │     ├─ Monomios {1, x, x², ...}
> │     └─ Matrices canónicas
> │
> ├─ MÉTODOS DE VERIFICACIÓN
> │  ├─ Sistema de ecuaciones homogéneo
> │  │  ├─ Formar matriz
> │  │  ├─ Reducir a forma escalonada
> │  │  └─ Analizar pivotes y variables libres
> │  ├─ Determinante (solo matrices cuadradas)
> │  │  ├─ det ≠ 0 → Independiente
> │  │  └─ det = 0 → Dependiente
> │  └─ Inspección visual
> │     ├─ Detectar casos obvios
> │     └─ Verificar proporcionalidad
> │
> ├─ PROPIEDADES
> │  ├─ Subconjunto de independiente es independiente
> │  ├─ Superconjunto de dependiente es dependiente
> │  ├─ Agregar vector fuera del span preserva independencia
> │  └─ Dimensión máxima en ℝⁿ es n
> │
> ├─ ALGORITMOS
> │  ├─ Extraer conjunto independiente maximal
> │  │  └─ Método de columnas pivote
> │  └─ Encontrar relación de dependencia
> │     └─ Resolver sistema homogéneo
> │
> └─ APLICACIONES
>    ├─ Bases y dimensión
>    ├─ Compresión de datos
>    ├─ Selección de características (ML)
>    ├─ Sistemas de ecuaciones
>    └─ Coordenadas y representación única
> ```

---

## 🔗 Relaciones Importantes

> [!quote]- 🌐 Conexiones con Otros Temas
> 
> ### Prerequisitos:
> 
> - **[[06 - Combinaciones Lineales]]** - Base de la definición
> - **[[07 - Sistemas de Ecuaciones Lineales]]** - Método de verificación
> - **[[08 - Matrices y Operaciones]]** - Representación matricial
> - **[[09 - Espacio Generado]]** - Contexto de span
> 
> ### Este tema es prerequisito para:
> 
> - **[[02 – Base y dimensión]]** - Conjuntos independientes que generan
> - **[[12 - Espacio Columna y Rango]]** - Independencia de columnas
> - **[[13 - Espacio Nulo]]** - Soluciones y dependencia
> - **[[14 - Coordenadas y Cambio de Base]]** - Representación única
> - **[[15 - Transformaciones Lineales]]** - Núcleo e inyectividad
> 
> ### Conceptos relacionados:
> 
> - **Base** - Conjunto independiente que genera
> - **Dimensión** - Tamaño del conjunto independiente maximal
> - **Rango** - Número de columnas independientes
> - **Nulidad** - Dimensión del espacio nulo
> - **Determinante** - Criterio para independencia (matrices cuadradas)
> 
> ### Diagrama de Flujo:
> 
> ```
> Combinaciones Lineales
>          ↓
>    Espacio Generado
>          ↓
>    Dependencia/Independencia
>          ↓
>    Base y Dimensión
>          ↓
>    Coordenadas
> ```
> 
> ### Siguiente tema recomendado:
> 
> **[[02 – Base y dimensión]]** - Para entender los conjuntos óptimos que generan espacios

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **Independencia = Sin Redundancia**
>     - El concepto más importante del álgebra lineal
>     - Diferencia entre información útil y redundante
>     - Base para construir representaciones óptimas
> 2. **Dos caras de la misma moneda:**
>     - Dependencia: existe combinación no trivial → cero
>     - Independencia: solo combinación trivial → cero
>     - Son conceptos complementarios
> 3. **Métodos prácticos disponibles:**
>     - Sistema homogéneo (siempre funciona)
>     - Determinante (matrices cuadradas)
>     - Inspección (casos simples)
> 4. **Importancia geométrica:**
>     - Vectores independientes → direcciones diferentes
>     - Maximiza el "espacio cubierto"
>     - Fundamento para coordenadas
> 5. **Aplicaciones universales:**
>     - Bases de espacios vectoriales
>     - Compresión de datos
>     - Análisis de sistemas
>     - Machine learning
> 
> ---
> 
> ### Próximos Pasos
> 
> Con independencia lineal dominada, estás listo para:
> 
> - **Base y Dimensión:** Conjuntos independientes óptimos
> - **Teorema de la Dimensión:** Relaciones fundamentales
> - **Coordenadas:** Representación única en una base
> - **Rango y Nulidad:** Aplicación a matrices
> - **Transformaciones Lineales:** Kernel e imagen
> 
> ---
> 
> ### Estrategia de Estudio
> 
> **Para dominar este tema:**
> 
> 1. ✅ Practicar detección de casos obvios
> 2. ✅ Dominar el método de reducción de filas
> 3. ✅ Visualizar geométricamente en $\mathbb{R}^2$ y $\mathbb{R}^3$
> 4. ✅ Conectar con el concepto de span
> 5. ✅ Entender la interpretación de "redundancia"
> 6. ✅ Aplicar a espacios abstractos (matrices, polinomios)
> 
> ---
> 
> ### Reflexión Final
> 
> La independencia lineal es el concepto que separa los vectores "esenciales" de los "redundantes":
> 
> - Es la base para definir dimensión
> - Garantiza unicidad de representación
> - Optimiza almacenamiento y computación
> - Es fundamental en toda aplicación del álgebra lineal
> 
> **Mensaje clave:** Entender independencia lineal es entender cuándo un conjunto de vectores contiene "información nueva" versus "información repetida". Este es el corazón del álgebra lineal moderna.

---

**Tags:** #algebra-lineal #independencia-lineal #dependencia-lineal #vectores #base-dimension #sistemas-lineales #determinante #espacios-vectoriales #redundancia #representacion-unica
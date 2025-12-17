# 📐 Proceso de Gram-Schmidt

## 🎯 Introducción al Proceso de Gram-Schmidt

> [!info]- 💡 ¿Qué es el Proceso de Gram-Schmidt?
> 
> El **proceso de Gram-Schmidt** es un algoritmo que transforma un conjunto de vectores linealmente independientes en un conjunto de vectores **ortogonales** (o **ortonormales**). Es una de las herramientas más importantes en álgebra lineal aplicada.
> 
> **Analogía intuitiva:**
> 
> Imagina que tienes varios palos de diferentes longitudes y direcciones que están inclinados unos respecto a otros. El proceso de Gram-Schmidt es como reorganizar esos palos de manera que:
> 
> - **Todos sean perpendiculares entre sí** (ortogonales)
> - **Mantengan el mismo "espacio" que cubrían antes** (generan el mismo subespacio)
> - **Opcionalmente, todos tengan longitud 1** (ortonormales)
> 
> **Del problema a la solución:**
> 
> ```mermaid
> graph LR
>     A[Vectores linealmente<br/>independientes<br/>v₁, v₂, ..., vₙ] --> B[Proceso de<br/>Gram-Schmidt]
>     B --> C[Vectores ortogonales<br/>u₁, u₂, ..., uₙ]
>     C --> D[Normalización<br/>opcional]
>     D --> E[Base ortonormal<br/>e₁, e₂, ..., eₙ]
>     
>     style A fill:#ffe1e1
>     style C fill:#fff4e1
>     style E fill:#e1ffe1
> ```

---

## 🎬 Motivación y Problema

> [!question]- 🤔 ¿Por Qué Necesitamos Este Proceso?
> 
> ### El Problema
> 
> Dada una base arbitraria de un espacio vectorial, los vectores suelen estar "inclinados" entre sí, lo que dificulta:
> 
> - **Cálculos de proyecciones**
> - **Descomposición de vectores**
> - **Resolución de sistemas**
> - **Análisis de señales**
> 
> ### La Solución
> 
> Una **base ortogonal** (mejor aún, ortonormal) simplifica enormemente estos cálculos porque:
> 
> |Ventaja|Con Base Arbitraria|Con Base Ortonormal|
> |---|---|---|
> |**Proyección sobre un vector**|Requiere resolver sistemas|Fórmula directa: $\text{proy}_{\mathbf{u}} \mathbf{v} = \langle \mathbf{v}, \mathbf{u} \rangle \mathbf{u}$|
> |**Coordenadas de un vector**|Sistema de ecuaciones|$\mathbf{v} = \sum_i \langle \mathbf{v}, \mathbf{e}_i \rangle \mathbf{e}_i$|
> |**Ortogonalidad**|Cálculo complejo|Verificar $\langle \mathbf{u}, \mathbf{v} \rangle = 0$|
> |**Distancias**|Requiere matrices|Teorema de Pitágoras generalizado|
> 
> ### Ejemplo Visual
> 
> ```mermaid
> graph TD
>     A[Base arbitraria] --> B[Difícil trabajar con ella]
>     B --> C[Aplicar Gram-Schmidt]
>     C --> D[Base ortogonal/ortonormal]
>     D --> E[Cálculos simplificados]
>     
>     A --> F[Vectores inclinados<br/>entre sí]
>     D --> G[Vectores perpendiculares<br/>longitud 1]
>     
>     style A fill:#ffe1e1
>     style D fill:#e1ffe1
>     style E fill:#e1f5ff
> ```

---

## 📋 El Algoritmo: Versión Ortogonal

> [!note]- 🔷 Proceso de Gram-Schmidt (Ortogonalización)
> 
> **Input:** Vectores linealmente independientes $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$
> 
> **Output:** Vectores ortogonales $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n$
> 
> ### Algoritmo Paso a Paso
> 
> $$\begin{align}
> \mathbf{u}_1 &= \mathbf{v}_1 \\[10pt]
> \mathbf{u}_2 &= \mathbf{v}_2 - \frac{\langle \mathbf{v}_2, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1 \\[10pt]
> \mathbf{u}_3 &= \mathbf{v}_3 - \frac{\langle \mathbf{v}_3, \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1, \mathbf{u}_1 \rangle} \mathbf{u}_1 - \frac{\langle \mathbf{v}_3, \mathbf{u}_2 \rangle}{\langle \mathbf{u}_2, \mathbf{u}_2 \rangle} \mathbf{u}_2 \\[10pt]
> &\vdots \\[10pt]
> \mathbf{u}_k &= \mathbf{v}_k - \sum_{j=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_j \rangle}{\langle \mathbf{u}_j, \mathbf{u}_j \rangle} \mathbf{u}_j
> \end{align}$$
> 
> ### Interpretación Geométrica
> 
> Cada nuevo vector $\mathbf{u}_k$ se obtiene:
> 
> 1. **Tomamos** $\mathbf{v}_k$
> 2. **Restamos** todas sus proyecciones sobre los vectores ortogonales anteriores $\mathbf{u}_1, \ldots, \mathbf{u}_{k-1}$
> 3. **El resultado** es perpendicular a todos los anteriores
> 
> ```mermaid
> graph TD
>     A["Vector original vₖ"] --> B["Proyectar sobre u₁, u₂, ..., uₖ₋₁"]
>     B --> C["Restar todas las proyecciones"]
>     C --> D["Resultado: uₖ perpendicular<br/>a todos los anteriores"]
>     
>     style A fill:#e1f5ff
>     style D fill:#e1ffe1
> ```
> 
> ### Notación de Proyección
> 
> Definiendo la **proyección ortogonal** de $\mathbf{v}$ sobre $\mathbf{u}$:
> 
> $$\text{proy}_{\mathbf{u}} \mathbf{v} = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}$$
> 
> El algoritmo se puede escribir más compactamente:
> 
> $$\mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proy}_{\mathbf{u}_j} \mathbf{v}_k$$

---

## 🌟 El Algoritmo: Versión Ortonormal

> [!success]- ⭐ Proceso de Gram-Schmidt (Ortonormalización)
> 
> Para obtener vectores **ortonormales** (ortogonales Y de norma 1), simplemente normalizamos cada vector ortogonal:
> 
> ### Algoritmo Completo
> 
> **Paso 1: Ortogonalización** (como antes)
> 
> $$\mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_j \rangle}{\langle \mathbf{u}_j, \mathbf{u}_j \rangle} \mathbf{u}_j$$
> 
> **Paso 2: Normalización**
> 
> $$\mathbf{e}_k = \frac{\mathbf{u}_k}{\|\mathbf{u}_k\|}$$
> 
> donde $\|\mathbf{u}_k\| = \sqrt{\langle \mathbf{u}_k, \mathbf{u}_k \rangle}$ es la norma de $\mathbf{u}_k$.
> 
> ### Algoritmo Alternativo (Normalización Inmediata)
> 
> Podemos normalizar inmediatamente después de cada ortogonalización:
> 
> $$\begin{align}
> \mathbf{e}_1 &= \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|} \\[10pt]
> \mathbf{u}_k &= \mathbf{v}_k - \sum_{j=1}^{k-1} \langle \mathbf{v}_k, \mathbf{e}_j \rangle \mathbf{e}_j \\[10pt]
> \mathbf{e}_k &= \frac{\mathbf{u}_k}{\|\mathbf{u}_k\|}
> \end{align}$$
> 
> **Ventaja:** Las proyecciones son más simples: $\text{proy}_{\mathbf{e}_j} \mathbf{v}_k = \langle \mathbf{v}_k, \mathbf{e}_j \rangle \mathbf{e}_j$
> 
> ### Propiedades del Resultado
> 
> Los vectores $\mathbf{e}_1, \ldots, \mathbf{e}_n$ satisfacen:
> 
> |Propiedad|Condición Matemática|
> |---|---|
> |**Ortonormalidad**|$\langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij} = \begin{cases} 1 & \text{si } i = j \\ 0 & \text{si } i \neq j \end{cases}$|
> |**Generan el mismo espacio**|$\text{span}\{\mathbf{e}_1, \ldots, \mathbf{e}_k\} = \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ para todo $k$|
> |**Son base**|Si los $\mathbf{v}_i$ eran linealmente independientes|

---

## 🎨 Ejemplo Detallado en $\mathbb{R}^3$

> [!example]- 📊 Ejemplo Paso a Paso
> 
> ### Problema
> 
> Ortonormalizar los vectores:
> 
> $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \quad \mathbf{v}_3 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$
> 
> usando el producto interno estándar de $\mathbb{R}^3$.
> 
> ---
> 
> ### Paso 1: Primer Vector
> 
> $$\mathbf{u}_1 = \mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$$
> 
> **Calculamos la norma:**
> 
> $$\|\mathbf{u}_1\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}$$
> 
> **Normalizamos:**
> 
> $$\mathbf{e}_1 = \frac{\mathbf{u}_1}{\|\mathbf{u}_1\|} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix}$$
> 
> ---
> 
> ### Paso 2: Segundo Vector
> 
> **Calculamos la proyección de $\mathbf{v}_2$ sobre $\mathbf{e}_1$:**
> 
> $$\langle \mathbf{v}_2, \mathbf{e}_1 \rangle = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}}$$
> 
> **Restamos la proyección:**
> 
> $$\begin{align}
> \mathbf{u}_2 &= \mathbf{v}_2 - \langle \mathbf{v}_2, \mathbf{e}_1 \rangle \mathbf{e}_1 \\[8pt]
> &= \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} - \frac{1}{\sqrt{2}} \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix} \\[8pt]
> &= \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} - \begin{pmatrix} 1/2 \\ 1/2 \\ 0 \end{pmatrix} \\[8pt]
> &= \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix}
> \end{align}$$
> 
> **Verificamos ortogonalidad:**
> 
> $$\langle \mathbf{u}_2, \mathbf{e}_1 \rangle = \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix} = \frac{1/2 - 1/2}{\sqrt{2}} = 0 \quad ✅$$
> 
> **Calculamos la norma:**
> 
> $$\|\mathbf{u}_2\| = \sqrt{(1/2)^2 + (-1/2)^2 + 1^2} = \sqrt{1/4 + 1/4 + 1} = \sqrt{3/2} = \frac{\sqrt{6}}{2}$$
> 
> **Normalizamos:**
> 
> $$\mathbf{e}_2 = \frac{\mathbf{u}_2}{\|\mathbf{u}_2\|} = \frac{2}{\sqrt{6}} \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix} = \begin{pmatrix} 1/\sqrt{6} \\ -1/\sqrt{6} \\ 2/\sqrt{6} \end{pmatrix}$$
> 
> ---
> 
> ### Paso 3: Tercer Vector
> 
> **Calculamos las proyecciones:**
> 
> $$\langle \mathbf{v}_3, \mathbf{e}_1 \rangle = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix} = \frac{1}{\sqrt{2}}$$
> 
> $$\langle \mathbf{v}_3, \mathbf{e}_2 \rangle = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 1/\sqrt{6} \\ -1/\sqrt{6} \\ 2/\sqrt{6} \end{pmatrix} = \frac{-1 + 2}{\sqrt{6}} = \frac{1}{\sqrt{6}}$$
> 
> **Restamos las proyecciones:**
> 
> $$\begin{align}
> \mathbf{u}_3 &= \mathbf{v}_3 - \langle \mathbf{v}_3, \mathbf{e}_1 \rangle \mathbf{e}_1 - \langle \mathbf{v}_3, \mathbf{e}_2 \rangle \mathbf{e}_2 \\[8pt]
> &= \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - \frac{1}{\sqrt{2}} \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix} - \frac{1}{\sqrt{6}} \begin{pmatrix} 1/\sqrt{6} \\ -1/\sqrt{6} \\ 2/\sqrt{6} \end{pmatrix} \\[8pt]
> &= \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} - \begin{pmatrix} 1/2 \\ 1/2 \\ 0 \end{pmatrix} - \begin{pmatrix} 1/6 \\ -1/6 \\ 2/6 \end{pmatrix} \\[8pt]
> &= \begin{pmatrix} -2/3 \\ 2/3 \\ 2/3 \end{pmatrix}
> \end{align}$$
> 
> **Verificamos ortogonalidad:**
> 
> $$\langle \mathbf{u}_3, \mathbf{e}_1 \rangle = 0 \quad ✅, \quad \langle \mathbf{u}_3, \mathbf{e}_2 \rangle = 0 \quad ✅$$
> 
> **Calculamos la norma:**
> 
> $$\|\mathbf{u}_3\| = \sqrt{4/9 + 4/9 + 4/9} = \sqrt{12/9} = \frac{2\sqrt{3}}{3}$$
> 
> **Normalizamos:**
> 
> $$\mathbf{e}_3 = \frac{3}{2\sqrt{3}} \begin{pmatrix} -2/3 \\ 2/3 \\ 2/3 \end{pmatrix} = \frac{1}{\sqrt{3}} \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1/\sqrt{3} \\ 1/\sqrt{3} \\ 1/\sqrt{3} \end{pmatrix}$$
> 
> ---
> 
> ### Resultado Final
> 
> **Base ortonormal:**
> 
> $$\boxed{\mathbf{e}_1 = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{pmatrix}, \quad \mathbf{e}_2 = \begin{pmatrix} 1/\sqrt{6} \\ -1/\sqrt{6} \\ 2/\sqrt{6} \end{pmatrix}, \quad \mathbf{e}_3 = \begin{pmatrix} -1/\sqrt{3} \\ 1/\sqrt{3} \\ 1/\sqrt{3} \end{pmatrix}}$$
> 
> **Verificación final:**
> 
> |Par de vectores|Producto interno|Resultado|
> |---|---|---|
> |$\langle \mathbf{e}_1, \mathbf{e}_1 \rangle$|$1/2 + 1/2 + 0$|$1$ ✅|
> |$\langle \mathbf{e}_2, \mathbf{e}_2 \rangle$|$1/6 + 1/6 + 4/6$|$1$ ✅|
> |$\langle \mathbf{e}_3, \mathbf{e}_3 \rangle$|$1/3 + 1/3 + 1/3$|$1$ ✅|
> |$\langle \mathbf{e}_1, \mathbf{e}_2 \rangle$|-|$0$ ✅|
> |$\langle \mathbf{e}_1, \mathbf{e}_3 \rangle$|-|$0$ ✅|
> |$\langle \mathbf{e}_2, \mathbf{e}_3 \rangle$|-|$0$ ✅|

---

## 🎭 Ejemplo en $\mathbb{R}^2$ (Visualización)

> [!example]- 🎨 Visualización Geométrica
> 
> ### Problema Simple
> 
> Ortonormalizar:
> 
> $$\mathbf{v}_1 = \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
> 
> ---
> 
> ### Solución
> 
> **Paso 1:**
> 
> $$\mathbf{u}_1 = \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \quad \|\mathbf{u}_1\| = \sqrt{10}$$
> 
> $$\mathbf{e}_1 = \begin{pmatrix} 3/\sqrt{10} \\ 1/\sqrt{10} \end{pmatrix}$$
> 
> **Paso 2:**
> 
> $$\langle \mathbf{v}_2, \mathbf{e}_1 \rangle = \frac{3 + 2}{\sqrt{10}} = \frac{5}{\sqrt{10}}$$
> 
> $$\mathbf{u}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix} - \frac{5}{\sqrt{10}} \begin{pmatrix} 3/\sqrt{10} \\ 1/\sqrt{10} \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} - \begin{pmatrix} 3/2 \\ 1/2 \end{pmatrix} = \begin{pmatrix} -1/2 \\ 3/2 \end{pmatrix}$$
> 
> $$\|\mathbf{u}_2\| = \sqrt{1/4 + 9/4} = \sqrt{10}/2$$
> 
> $$\mathbf{e}_2 = \begin{pmatrix} -1/\sqrt{10} \\ 3/\sqrt{10} \end{pmatrix}$$
> 
> ---
> 
> ### Interpretación Visual
> 
> ```mermaid
> graph TD
>     A["Vectores originales v₁ y v₂<br/>(no perpendiculares)"] --> B["Mantener v₁ como u₁"]
>     B --> C["Proyectar v₂ sobre u₁"]
>     C --> D["Restar proyección de v₂"]
>     D --> E["Resultado: u₂ perpendicular a u₁"]
>     E --> F["Normalizar ambos"]
>     F --> G["Base ortonormal e₁, e₂"]
>     
>     style A fill:#ffe1e1
>     style E fill:#fff4e1
>     style G fill:#e1ffe1
> ```
> 
> **Verificación:**
> 
> $$\langle \mathbf{e}_1, \mathbf{e}_2 \rangle = \frac{3(-1) + 1(3)}{10} = 0 \quad ✅$$

---

## 📚 Ejemplo con Funciones

> [!example]- 📈 Gram-Schmidt en $C[0,1]$
> 
> ### Problema
> 
> Ortonormalizar los polinomios $1, x, x^2$ en $C[0,1]$ con el producto interno:
> 
> $$\langle f, g \rangle = \int_0^1 f(x)g(x) \, dx$$
> 
> ---
> 
> ### Paso 1: Primer Polinomio
> 
> $$u_1(x) = 1$$
> 
> $$\|u_1\|^2 = \int_0^1 1 \, dx = 1 \quad \Rightarrow \quad \|u_1\| = 1$$
> 
> $$e_1(x) = 1$$
> 
> ---
> 
> ### Paso 2: Segundo Polinomio
> 
> $$\langle x, e_1 \rangle = \int_0^1 x \cdot 1 \, dx = \left[\frac{x^2}{2}\right]_0^1 = \frac{1}{2}$$
> 
> $$u_2(x) = x - \frac{1}{2} \cdot 1 = x - \frac{1}{2}$$
> 
> $$\|u_2\|^2 = \int_0^1 \left(x - \frac{1}{2}\right)^2 dx = \int_0^1 \left(x^2 - x + \frac{1}{4}\right) dx$$
> 
> $$= \left[\frac{x^3}{3} - \frac{x^2}{2} + \frac{x}{4}\right]_0^1 = \frac{1}{3} - \frac{1}{2} + \frac{1}{4} = \frac{1}{12}$$
> 
> $$\|u_2\| = \frac{1}{2\sqrt{3}} \quad \Rightarrow \quad e_2(x) = 2\sqrt{3}\left(x - \frac{1}{2}\right) = \sqrt{3}(2x - 1)$$
> 
> ---
> 
> ### Paso 3: Tercer Polinomio
> 
> $$\langle x^2, e_1 \rangle = \int_0^1 x^2 \, dx = \frac{1}{3}$$
> 
> $$\langle x^2, e_2 \rangle = \sqrt{3} \int_0^1 x^2(2x - 1) \, dx = \sqrt{3} \int_0^1 (2x^3 - x^2) \, dx$$
> 
> $$= \sqrt{3} \left[\frac{x^4}{2} - \frac{x^3}{3}\right]_0^1 = \sqrt{3}\left(\frac{1}{2} - \frac{1}{3}\right) = \frac{\sqrt{3}}{6}$$
> 
> $$u_3(x) = x^2 - \frac{1}{3} \cdot 1 - \frac{\sqrt{3}}{6} \cdot \sqrt{3}(2x-1)$$
> 
> $$= x^2 - \frac{1}{3} - \frac{1}{2}(2x-1) = x^2 - x + \frac{1}{6}$$
> 
> Normalizando (cálculo omitido):
> 
> $$e_3(x) = \sqrt{5}(6x^2 - 6x + 1)$$
> 
> ---
> 
> ### Resultado
> 
> **Polinomios ortonormales:**
> 
> $$\boxed{\begin{align}
> e_1(x) &= 1 \\
> e_2(x) &= \sqrt{3}(2x - 1) \\
> e_3(x) &= \sqrt{5}(6x^2 - 6x + 1)
> \end{align}}$$
> 
> Estos son los primeros tres **polinomios de Legendre desplazados** al intervalo $[0,1]$.

---

## 🔍 Propiedades y Teoremas

> [!success]- ⚡ Propiedades Importantes
> 
> ### Teorema 1: Preservación del Subespacio
> 
> Para cada $k = 1, 2, \ldots, n$:
> 
> $$\text{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_k\} = \text{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$$
> 
> **Significado:** Los vectores ortogonales generan los mismos subespacios que los originales.
> 
> ---
> 
> ### Teorema 2: Existencia y Unicidad
> 
> **Existencia:** Si $\mathbf{v}_1, \ldots, \mathbf{v}_n$ son linealmente independientes, el proceso de Gram-Schmidt siempre produce vectores ortogonales $\mathbf{u}_1, \ldots, \mathbf{u}_n$.
> 
> **Unicidad (parcial):** Los vectores ortonormales son únicos salvo cambios de signo (multiplicación por $-1$).
> 
> ---
> 
> ### Teorema 3: Ortogonalidad Garantizada
> 
> Los vectores $\mathbf{u}_1, \ldots, \mathbf{u}_n$ producidos satisfacen:
<
> $$\langle \mathbf{u}_i, \mathbf{u}_j \rangle = 0 \quad \text{para todo } i \neq j$$
<
**Demostración (por inducción):**
<
> ```
> Base: u₁ es ortogonal a sí mismo trivialmente.
> 
> Hipótesis: u₁, ..., uₖ₋₁ son mutuamente ortogonales.
> 
> Paso inductivo: Mostrar que uₖ es ortogonal a todos los anteriores.
> 
> Para cualquier j < k:
> ⟨uₖ, uⱼ⟩ = ⟨vₖ - Σᵢ₌₁ᵏ⁻¹ projᵤᵢ(vₖ), uⱼ⟩
>          = ⟨vₖ, uⱼ⟩ - ⟨projᵤⱼ(vₖ), uⱼ⟩
>          = ⟨vₖ, uⱼ⟩ - ⟨vₖ, uⱼ⟩/⟨uⱼ, uⱼ⟩ · ⟨uⱼ, uⱼ⟩
>          = ⟨vₖ, uⱼ⟩ - ⟨vₖ, uⱼ⟩
>          = 0 ✅
> ```
<
> ### Teorema 4: Dependencia Lineal
> 
> Si en algún paso $\mathbf{u}_k = \mathbf{0}$, entonces los vectores originales $\mathbf{v}_1, \ldots, \mathbf{v}_n$ eran **linealmente dependientes**.
> 
> **Interpretación:** El proceso falla si y solo si los vectores de entrada no son linealmente independientes.
<
> ### Tabla Resumen de Propiedades
> 
> | Propiedad         | Descripción                                                      | Implicación                  |
| ----------------- | ---------------------------------------------------------------- | ---------------------------- |
| **Preservación**  | Mismo subespacio en cada paso                                    | No perdemos información      |
| **Ortogonalidad** | $\langle \mathbf{u}_i, \mathbf{u}_j \rangle = 0$ para $i \neq j$ | Vectores perpendiculares     |
| **Normalización** | $\|\mathbf{e}_i\| = 1$                                           | Base ortonormal              |
| **Optimalidad**   | Minimiza distancia en cada paso                                  | Mejor aproximación ortogonal |

---

## 🎯 Gram-Schmidt Modificado

> [!tip]- 🔄 Versión Numéricamente Estable
> 
> ### El Problema de Estabilidad
> 
> El proceso clásico de Gram-Schmidt puede ser **numéricamente inestable** cuando los vectores están casi linealmente dependientes o cuando trabajamos con aritmética de punto flotante.
> 
> **Problema:** Los errores de redondeo se acumulan, y los vectores resultantes pueden no ser verdaderamente ortogonales.
> 
> ### Gram-Schmidt Modificado (MGS)
> 
> En lugar de calcular todas las proyecciones de $\mathbf{v}_k$ de una vez, las calculamos **secuencialmente** y actualizamos el vector después de cada proyección.
> 
> **Algoritmo:**
> 
> ```
> Para k = 1 hasta n:
>     uₖ = vₖ
>     Para j = 1 hasta k-1:
>         uₖ = uₖ - proyₑⱼ(uₖ)  // Nota: proyectamos uₖ actual, no vₖ
>     eₖ = uₖ / ‖uₖ‖
> ```
> 
> ### Comparación
> 
> |Aspecto|Clásico (CGS)|Modificado (MGS)|
> |---|---|---|
> |**Fórmula**|$\mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proy}_{\mathbf{e}_j} \mathbf{v}_k$|Proyecciones secuenciales de $\mathbf{u}_k$|
> |**Estabilidad**|Menos estable|Más estable|
> |**Complejidad**|$O(n^2m)$|$O(n^2m)$|
> |**Ortogonalidad**|Puede degradarse|Mejor preservada|
> |**Uso práctico**|Teórico, ejemplos pequeños|Implementaciones numéricas|
> 
> ### Ejemplo Numérico de la Diferencia
> 
> ```
> Con vectores casi colineales:
> v₁ = (1, 1, 1)
> v₂ = (1, 1.0001, 1)
> v₃ = (1, 1, 1.0001)
> 
> CGS: Ortogonalidad puede degradarse a ~10⁻⁸
> MGS: Ortogonalidad mantenida a ~10⁻¹⁵
> ```
> 
> **Recomendación:** En implementaciones computacionales, usar **siempre MGS**.

---

## 🔬 Variante: QR Factorización

> [!info]- 🏗️ Conexión con Factorización QR
> 
> El proceso de Gram-Schmidt está íntimamente relacionado con la **factorización QR** de matrices.
> 
> ### Representación Matricial
> 
> Si colocamos los vectores originales como columnas de una matriz $A$:
> 
> $$A = \begin{bmatrix} | & | & & | \\ \mathbf{v}_1 & \mathbf{v}_2 & \cdots & \mathbf{v}_n \\ | & | & & | \end{bmatrix}$$
> 
> Y los vectores ortonormales como columnas de $Q$:
> 
> $$Q = \begin{bmatrix} | & | & & | \\ \mathbf{e}_1 & \mathbf{e}_2 & \cdots & \mathbf{e}_n \\ | & | & & | \end{bmatrix}$$
> 
> Entonces el proceso de Gram-Schmidt produce:
> 
> $$A = QR$$
> 
> donde $R$ es una matriz **triangular superior**.
> 
> ### Construcción de R
> 
> Los elementos de $R$ vienen de las proyecciones:
> 
> $$R_{ij} = \begin{cases}
> \langle \mathbf{v}_j, \mathbf{e}_i \rangle & \text{si } i \leq j \\
> 0 & \text{si } i > j
> \end{cases}$$
> 
> $$R_{jj} = \|\mathbf{u}_j\|$$
> 
> ### Ejemplo
> 
> Para los vectores del ejemplo en $\mathbb{R}^2$:
> 
> $$A = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$$
> 
> $$Q = \begin{bmatrix} 3/\sqrt{10} & -1/\sqrt{10} \\ 1/\sqrt{10} & 3/\sqrt{10} \end{bmatrix}$$
> 
> $$R = \begin{bmatrix} \sqrt{10} & 5/\sqrt{10} \\ 0 & \sqrt{10}/2 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$QR = \begin{bmatrix} 3/\sqrt{10} & -1/\sqrt{10} \\ 1/\sqrt{10} & 3/\sqrt{10} \end{bmatrix} \begin{bmatrix} \sqrt{10} & 5/\sqrt{10} \\ 0 & \sqrt{10}/2 \end{bmatrix} = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix} = A \quad ✅$$
> 
> ### Aplicaciones de QR
> 
> ```mermaid
> graph TD
>     A[Factorización QR] --> B[Resolver sistemas<br/>lineales]
>     A --> C[Encontrar<br/>eigenvalores]
>     A --> D[Mínimos<br/>cuadrados]
>     A --> E[Ortogonalizar<br/>bases]
>     
>     style A fill:#e1ffe1
>     style B fill:#e1f5ff
>     style C fill:#e1f5ff
>     style D fill:#e1f5ff
>     style E fill:#e1f5ff
> ```

---

## 🎨 Visualización del Proceso

> [!tip]- 🗺️ Interpretación Geométrica Paso a Paso
> 
> ### Visualización en 2D
> 
> ```mermaid
> graph TD
>     A["Paso 1: Tomar v₁<br/>u₁ = v₁"] --> B["Paso 2: Proyectar v₂<br/>sobre u₁"]
>     B --> C["Restar proyección<br/>u₂ = v₂ - proj"]
>     C --> D["Resultado: u₂ ⊥ u₁"]
>     
>     style A fill:#e1f5ff
>     style C fill:#fff4e1
>     style D fill:#e1ffe1
> ```
> 
> ### Analogía Visual
> 
> Imagina que tienes dos palos inclinados:
> 
> **Antes de Gram-Schmidt:**
> ```
>     v₂ ↗
>        /
>       /
>      /
>   v₁ →
> ```
> 
> **Después de Gram-Schmidt:**
> ```
>   u₂ ↑
>      |
>      |
>      └─── u₁ →
> ```
> 
> ### En 3D
> 
> Para tres vectores, el proceso:
> 
> 1. **Mantiene** $\mathbf{v}_1$ como $\mathbf{u}_1$
> 2. **Proyecta** $\mathbf{v}_2$ sobre $\mathbf{u}_1$ y resta → $\mathbf{u}_2$ perpendicular a $\mathbf{u}_1$
> 3. **Proyecta** $\mathbf{v}_3$ sobre el plano formado por $\mathbf{u}_1$ y $\mathbf{u}_2$, resta → $\mathbf{u}_3$ perpendicular a ambos
> 
> **Resultado:** Sistema de ejes ortogonales (como x, y, z)

---

## 🔍 Aplicaciones Prácticas

> [!quote]- 🌍 Usos en el Mundo Real
> 
> ### 1. Procesamiento de Señales
> 
> **Problema:** Descomponer una señal en componentes ortogonales.
> 
> **Aplicación de Gram-Schmidt:**
> - Crear filtros ortogonales
> - Análisis de Fourier discreto
> - Codificación de señales
> 
> ```mermaid
> graph LR
>     A[Señal original] --> B[Gram-Schmidt]
>     B --> C[Componentes<br/>ortogonales]
>     C --> D[Análisis/filtrado<br/>independiente]
>     
>     style C fill:#e1ffe1
> ```
> 
> ### 2. Regresión por Mínimos Cuadrados
> 
> **Problema:** Ajustar un modelo lineal $y = \beta_1 x_1 + \cdots + \beta_n x_n$.
> 
> **Ventaja con Gram-Schmidt:**
> - Ortogonalizar las variables predictoras $x_1, \ldots, x_n$
> - Los coeficientes $\beta_i$ se calculan independientemente
> - Evita problemas de multicolinealidad
> 
> **Fórmula simplificada:**
> 
> $$\beta_i = \frac{\langle y, e_i \rangle}{\langle e_i, e_i \rangle}$$
> 
> donde $e_i$ son las variables ortogonalizadas.
> 
> ### 3. Métodos Numéricos
> 
> |Método|Uso de Gram-Schmidt|Beneficio|
> |---|---|---|
> |**Algoritmo QR**|Iterativo para eigenvalores|Convergencia a eigenvalores|
> |**GMRES**|Resolver sistemas grandes|Construir base de Krylov ortogonal|
> |**Arnoldi**|Aproximar eigenvalores|Reducción ortogonal|
> 
> ### 4. Computación Gráfica
> 
> **Problema:** Construir sistemas de coordenadas locales en superficies.
> 
> **Aplicación:**
> - Dado un vector normal $\mathbf{n}$ a una superficie
> - Usar Gram-Schmidt para construir dos vectores tangentes ortogonales
> - Resultado: sistema de coordenadas local (n, t₁, t₂)
> 
> ### 5. Machine Learning
> 
> **Decorrelación de características:**
> ```
> Entrada: Features correlacionadas x₁, x₂, ..., xₙ
> ↓
> Gram-Schmidt
> ↓
> Salida: Features ortogonales e₁, e₂, ..., eₙ
> ↓
> Beneficio: Reduce redundancia, mejora aprendizaje
> ```
> 
> ### 6. Polinomios Ortogonales
> 
> **Construir familias de polinomios ortogonales:**
> 
> |Intervalo|Peso|Familia resultante|
> |---|---|---|
> |$[-1, 1]$|$w(x) = 1$|Polinomios de Legendre|
> |$[-1, 1]$|$w(x) = \frac{1}{\sqrt{1-x^2}}$|Polinomios de Chebyshev|
> |$[0, \infty)$|$w(x) = e^{-x}$|Polinomios de Laguerre|
> |$(-\infty, \infty)$|$w(x) = e^{-x^2}$|Polinomios de Hermite|
> 
> **Uso:** Aproximación de funciones, análisis numérico, física cuántica.

---

## ⚠️ Consideraciones Importantes

> [!warning]- 🚨 Problemas y Limitaciones
> 
> ### 1. Dependencia Lineal
> 
> **Problema:** Si los vectores de entrada son linealmente dependientes, el algoritmo falla.
> 
> **Síntoma:** En algún paso, $\mathbf{u}_k = \mathbf{0}$ (o muy cercano a cero).
> 
> **Solución:**
> - Verificar independencia lineal antes de aplicar
> - Omitir vectores que produzcan $\mathbf{u}_k \approx \mathbf{0}$
> - Usar descomposición SVD como alternativa
> 
> ### 2. Inestabilidad Numérica
> 
> **Problema:** Con aritmética de punto flotante, la ortogonalidad se degrada.
> 
> **Causas:**
> - Vectores casi colineales
> - Acumulación de errores de redondeo
> - Pérdida de precisión en restas
> 
> **Soluciones:**
> - Usar **Gram-Schmidt Modificado** (MGS)
> - Reortogonalización: aplicar el proceso dos veces
> - Usar alternativas como Householder o Givens
> 
> ```mermaid
> graph TD
>     A[Detectar problema] --> B{Tipo de problema}
>     B -->|Dependencia lineal| C[Eliminar vectores<br/>redundantes]
>     B -->|Inestabilidad numérica| D[Usar MGS o<br/>reortogonalizar]
>     B -->|Vectores casi colineales| E[Considerar SVD<br/>o QR pivoteado]
>     
>     style A fill:#ffe1e1
>     style C fill:#fff4e1
>     style D fill:#fff4e1
>     style E fill:#fff4e1
> ```
> 
> ### 3. Orden de los Vectores
> 
> **Observación:** El orden de los vectores de entrada **afecta el resultado**.
> 
> **Ejemplo:**
> ```
> Entrada: v₁, v₂, v₃
> Salida: e₁ ∥ v₁, e₂ ⊥ e₁, e₃ ⊥ e₁, e₂
> 
> vs.
> 
> Entrada: v₃, v₂, v₁
> Salida: e₁' ∥ v₃, e₂' ⊥ e₁', e₃' ⊥ e₁', e₂'
> (diferentes bases ortogonales!)
> ```
> 
> **Implicación:** El primer vector determina la "dirección principal".
> 
> ### 4. Complejidad Computacional
> 
> **Para $n$ vectores en $\mathbb{R}^m$:**
> 
> |Operación|Cantidad|
> |---|---|
> |Productos internos|$O(n^2)$|
> |Operaciones por producto|$O(m)$|
> |**Total**|$O(n^2 m)$|
> 
> **Comparación:**
> - **QR con Householder:** $O(nm^2)$ (mejor para $m < n$)
> - **QR con Givens:** $O(nm^2)$ (matrices sparse)

---

## 🧩 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> ### Nivel Básico
> 
> **1.** Aplica el proceso de Gram-Schmidt para ortonormalizar:
> 
> $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
> 
> en $\mathbb{R}^2$ con el producto interno estándar.
> 
> **2.** Verifica que los vectores resultantes del ejercicio anterior son ortonormales.
> 
> **3.** Ortogonaliza (sin normalizar) los vectores:
> 
> $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$$
> 
> ### Nivel Intermedio
> 
> **4.** Aplica Gram-Schmidt a los vectores:
> 
> $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \quad \mathbf{v}_3 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}$$
> 
> **5.** Ortonormaliza los polinomios $1, x, x^2$ en $[-1, 1]$ con:
> 
> $$\langle f, g \rangle = \int_{-1}^1 f(x)g(x) \, dx$$
> 
> (Estos son los primeros tres polinomios de Legendre)
> 
> **6.** Encuentra la factorización QR de:
> 
> $$A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}$$
> 
> ### Nivel Avanzado
> 
> **7.** Demuestra que si $\mathbf{v}_1, \ldots, \mathbf{v}_n$ son linealmente independientes, entonces el proceso de Gram-Schmidt produce vectores no nulos.
> 
> **8.** Sea $W = \text{span}\{\mathbf{v}_1, \mathbf{v}_2\}$ en $\mathbb{R}^3$. Usa Gram-Schmidt para:
> - Encontrar una base ortonormal de $W$
> - Encontrar un vector unitario ortogonal a $W$
> 
> Datos:
> $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}$$
> 
> **9.** **Proyecto:** Implementa el proceso de Gram-Schmidt Modificado en tu lenguaje de programación favorito y compara la estabilidad numérica con el algoritmo clásico usando vectores casi colineales.

---

## 🔬 Comparación con Otros Métodos

> [!info]- ⚖️ Gram-Schmidt vs. Otras Técnicas de Ortogonalización
> 
> ### Tabla Comparativa
> 
> |Método|Complejidad|Estabilidad|Uso Principal|
> |---|---|---|---|
> |**Gram-Schmidt Clásico**|$O(n^2m)$|⭐⭐|Teoría, ejemplos pequeños|
> |**Gram-Schmidt Modificado**|$O(n^2m)$|⭐⭐⭐|Implementaciones prácticas|
> |**Householder QR**|$O(nm^2)$|⭐⭐⭐⭐⭐|Matrices densas, alta precisión|
> |**Givens QR**|$O(nm^2)$|⭐⭐⭐⭐|Matrices sparse, paralelizable|
> |**SVD**|$O(nm^2)$|⭐⭐⭐⭐⭐|Matrices casi singulares, análisis|
> 
> ### Cuándo Usar Cada Método
> 
> ```mermaid
> graph TD
>     A{¿Qué tipo de<br/>problema?} --> B{¿Tamaño?}
>     B -->|Pequeño n| C[Gram-Schmidt<br/>Clásico]
>     B -->|Mediano/Grande| D{¿Estabilidad<br/>crítica?}
>     D -->|Sí| E[Householder QR]
>     D -->|No| F[Gram-Schmidt<br/>Modificado]
>     
>     A --> G{¿Matriz sparse?}
>     G -->|Sí| H[Givens QR]
>     
>     A --> I{¿Matriz casi<br/>singular?}
>     I -->|Sí| J[SVD]
>     
>     style C fill:#e1f5ff
>     style E fill:#e1ffe1
>     style F fill:#fff4e1
>     style H fill:#e1ffe1
>     style J fill:#e1ffe1
> ```
> 
> ### Ventajas de Gram-Schmidt
> 
> - **Intuitivo:** Fácil de entender geométricamente
> - **Constructivo:** Produce la base paso a paso
> - **Flexible:** Fácil de adaptar a productos internos no estándar
> - **Directo:** No requiere matrices auxiliares
> 
> ### Desventajas de Gram-Schmidt
> 
> - **Estabilidad:** Puede perder ortogonalidad en aritmética flotante
> - **Eficiencia:** No es el más rápido para matrices grandes
> - **Sensibilidad:** Al orden de los vectores de entrada

---

## 📖 Resumen del Capítulo

> [!abstract]- 📝 Puntos Clave
> 
> ### Conceptos Fundamentales
> 
> |Concepto|Descripción|Notación|
> |---|---|---|
> |**Gram-Schmidt**|Algoritmo de ortogonalización|$\mathbf{v}_i \to \mathbf{u}_i \to \mathbf{e}_i$|
> |**Proyección**|Componente de un vector sobre otro|$\text{proy}_{\mathbf{u}} \mathbf{v} = \frac{\langle \mathbf{v}, \mathbf{u} \rangle}{\langle \mathbf{u}, \mathbf{u} \rangle} \mathbf{u}$|
> |**Ortogonalización**|Producir vectores perpendiculares|$\langle \mathbf{u}_i, \mathbf{u}_j \rangle = 0$|
> |**Ortonormalización**|Perpendiculares y unitarios|$\langle \mathbf{e}_i, \mathbf{e}_j \rangle = \delta_{ij}$|
> 
> ### Fórmulas Esenciales
> 
> $$\begin{align}
> \text{Ortogonalización:} & \quad \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \frac{\langle \mathbf{v}_k, \mathbf{u}_j \rangle}{\langle \mathbf{u}_j, \mathbf{u}_j \rangle} \mathbf{u}_j \\[10pt]
> \text{Normalización:} & \quad \mathbf{e}_k = \frac{\mathbf{u}_k}{\|\mathbf{u}_k\|} \\[10pt]
> \text{Con base ortonormal:} & \quad \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \langle \mathbf{v}_k, \mathbf{e}_j \rangle \mathbf{e}_j
> \end{align}$$
> 
> ### Propiedades Importantes
> 
> - Preserva el subespacio generado en cada paso
> - Produce base ortogonal si la entrada es linealmente independiente
> - El orden de los vectores afecta el resultado
> - Relacionado con factorización QR
> 
> ### Algoritmo en Pseudocódigo
> 
> ```
> Entrada: v₁, v₂, ..., vₙ (linealmente independientes)
> Salida: e₁, e₂, ..., eₙ (ortonormales)
> 
> Para k = 1 hasta n:
>     uₖ = vₖ
>     Para j = 1 hasta k-1:
>         uₖ = uₖ - ⟨vₖ, eⱼ⟩ eⱼ
>     eₖ = uₖ / ‖uₖ‖
> ```
> 
> ### Aplicaciones Clave
> 
> - Regresión por mínimos cuadrados
> - Factorización QR
> - Construcción de bases ortogonales
> - Métodos iterativos (GMRES, Arnoldi)
> - Polinomios ortogonales
> 
> ### Próximo Tema
> 
> En el siguiente capítulo estudiaremos las **proyecciones ortogonales** y el **teorema de la mejor aproximación**, que utilizan directamente las bases ortogonales construidas por Gram-Schmidt.

---

**Tags:** #algebra-lineal #gram-schmidt #ortogonalizacion #base-ortonormal #factorizacion-qr #proyecciones #metodos-numericos
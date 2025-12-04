# 🔷 Suma de Subespacios

## 🎯 Introducción

> [!info]- 💡 ¿Por qué Suma de Subespacios?
> 
> **Problema:** Dados dos subespacios $U$ y $W$, ¿cómo combinarlos en uno más grande?
> 
> **Solución:** La suma $U + W$ contiene todas las combinaciones posibles.
> 
> **Motivación:**
> 
> - **Descomposición:** Partir espacio en componentes más simples
> - **Proyecciones:** Separar vectores en partes ortogonales
> - **Ecuaciones diferenciales:** Solución = homogénea + particular
> - **Física:** Estado total = suma de estados independientes
> - **Análisis de datos:** Descomponer señales en componentes
> 
> **Analogías:**
> 
> - **Mezcla de colores:** Combinar paletas de pintura
> - **Unión de conjuntos:** Pero respetando estructura vectorial
> - **Fusión de equipos:** Todos los recursos disponibles juntos
> - **Superposición cuántica:** Estados combinados linealmente
> - **Combinación musical:** Mezclar diferentes instrumentos
> 
> **Aplicaciones prácticas:**
> 
> - **Machine Learning:** Descomposición de features
> - **Procesamiento de señales:** Filtrado y separación
> - **Gráficos 3D:** Composición de transformaciones
> - **Análisis numérico:** Métodos de descomposición

---

## 📐 Definición Formal

### Suma de Subespacios

> [!note]- 📋 Definición Principal
> 
> Sean $U$ y $W$ subespacios de $V$.
> 
> La **suma** de $U$ y $W$ es:
> 
> $$U + W = {\vec{u} + \vec{w} \mid \vec{u} \in U, \vec{w} \in W}$$
> 
> **En palabras:** Todos los vectores que se pueden escribir como suma de un vector de $U$ y un vector de $W$.
> 
> **Propiedades fundamentales:**
> 
> - $U + W$ es subespacio de $V$
> - $U \subseteq U + W$ y $W \subseteq U + W$
> - $U + W$ es el subespacio más pequeño que contiene a $U$ y $W$
> - $U + W = \text{span}(U \cup W)$
> 
> ---
> 
> **Notaciones alternativas:**
> 
> - $\text{span}(U \cup W)$ - generado por la unión
> - $U \oplus W$ - suma directa (caso especial)
> - $\langle U, W \rangle$ - subespacio generado

> [!warning]- ⚠️ Diferencia con Unión
> 
> **CUIDADO:** $U + W \neq U \cup W$ en general
> 
> **Ejemplo:**
> 
> En $\mathbb{R}^2$: $$U = \text{eje } x, \quad W = \text{eje } y$$
> 
> - $U \cup W$ = solo los ejes (no es subespacio)
> - $U + W = \mathbb{R}^2$ (todo el plano)
> 
> **Regla:** La unión NO es subespacio (no cerrada bajo suma)

> [!example]- 📝 Ejemplos Básicos
> 
> **1. Rectas en $\mathbb{R}^2$:**
> 
> $$U = \text{span}\left{\begin{bmatrix} 1 \ 0 \end{bmatrix}\right}, \quad W = \text{span}\left{\begin{bmatrix} 0 \ 1 \end{bmatrix}\right}$$
> 
> Cualquier vector $\begin{bmatrix} x \ y \end{bmatrix} = x\begin{bmatrix} 1 \ 0 \end{bmatrix} + y\begin{bmatrix} 0 \ 1 \end{bmatrix}$
> 
> $$U + W = \mathbb{R}^2$$ (todo el plano)
> 
> ---
> 
> **2. Rectas en $\mathbb{R}^3$:**
> 
> $$U = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}\right}, \quad W = \text{span}\left{\begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}\right}$$
> 
> $$U + W = \left{\begin{bmatrix} x \ y \ 0 \end{bmatrix} \mid x,y \in \mathbb{R}\right}$$ = plano $xy$
> 
> ---
> 
> **3. Planos en $\mathbb{R}^3$:**
> 
> $$U = \text{plano } xy, \quad W = \text{plano } xz$$
> 
> $$U + W = \mathbb{R}^3$$ (todo el espacio)
> 
> ---
> 
> **4. Mismo subespacio:**
> 
> $$U + U = U$$
> 
> (la suma de un subespacio consigo mismo es él mismo)

### Suma Directa

> [!note]- ⭐ Caso Especial Importante
> 
> La suma $U + W$ es **directa** si $U \cap W = {\vec{0}}$
> 
> **Notación:** $U \oplus W$ (suma directa)
> 
> **Caracterización:** Todo vector de $U + W$ se escribe de forma única:
> 
> $$\vec{v} = \vec{u} + \vec{w}, \quad \vec{u} \in U, \vec{w} \in W$$
> 
> **Fórmula de dimensión:**
> 
> $$\dim(U \oplus W) = \dim(U) + \dim(W)$$
> 
> ---
> 
> **Equivalencias (todas son lo mismo):**
> 
> Las siguientes afirmaciones son equivalentes:
> 
> 1. $U + W = U \oplus W$ (es suma directa)
> 2. $U \cap W = {\vec{0}}$ (intersección trivial)
> 3. Representación única: si $\vec{u}_1 + \vec{w}_1 = \vec{u}_2 + \vec{w}_2$ entonces $\vec{u}_1 = \vec{u}_2$ y $\vec{w}_1 = \vec{w}_2$
> 4. $\dim(U + W) = \dim(U) + \dim(W)$ (dimensiones se suman)
> 5. Si ${\vec{u}_1, \ldots, \vec{u}_k}$ es base de $U$ y ${\vec{w}_1, \ldots, \vec{w}_m}$ es base de $W$, entonces ${\vec{u}_1, \ldots, \vec{u}_k, \vec{w}_1, \ldots, \vec{w}_m}$ es base de $U \oplus W$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - Suma directa: los subespacios son "independientes"
> - No directa: hay "solapamiento" entre subespacios

> [!tip]- 🛠️ Cómo Verificar Suma Directa
> 
> **Método 1:** Verificar $U \cap W = {\vec{0}}$
> 
> 1. Tomar $\vec{v} \in U \cap W$
> 2. Expresar $\vec{v}$ usando bases de $U$ y $W$
> 3. Resolver el sistema resultante
> 4. Si solo solución es $\vec{v} = \vec{0}$, entonces es suma directa
> 
> **Método 2:** Verificar dimensiones
> 
> 1. Calcular $\dim(U)$ y $\dim(W)$
> 2. Calcular $\dim(U + W)$
> 3. Si $\dim(U + W) = \dim(U) + \dim(W)$, es suma directa
> 
> **Método 3:** Verificar independencia de bases
> 
> 4. Tomar bases de $U$ y $W$
> 5. Juntar todos los vectores
> 6. Si el conjunto es linealmente independiente, es suma directa

---

## 🔍 Propiedades Fundamentales

### Teorema de la Dimensión

> [!note]- 📊 Fórmula Principal (Grassmann)
> 
> Para subespacios $U, W$ de $V$:
> 
> $$\boxed{\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)}$$
> 
> **Nombre:** Fórmula de Grassmann o Identidad de dimensión
> 
> **Analogía:** Principio de inclusión-exclusión para conjuntos
> 
> $$|A \cup B| = |A| + |B| - |A \cap B|$$
> 
> **Demostración (idea):**
> 
> 1. Tomar base ${\vec{v}_1, \ldots, \vec{v}_k}$ de $U \cap W$
> 2. Extender a base de $U$: ${\vec{v}_1, \ldots, \vec{v}_k, \vec{u}_1, \ldots, \vec{u}_r}$
> 3. Extender a base de $W$: ${\vec{v}_1, \ldots, \vec{v}_k, \vec{w}_1, \ldots, \vec{w}_s}$
> 4. Probar que ${\vec{v}_1, \ldots, \vec{v}_k, \vec{u}_1, \ldots, \vec{u}_r, \vec{w}_1, \ldots, \vec{w}_s}$ es base de $U + W$
> 5. Contar: $(k + r + s) = (k + r) + (k + s) - k$
> 
> ---
> 
> **Casos especiales:**
> 
> |Situación|Fórmula|Ejemplo|
> |---|---|---|
> |**Suma directa**|$\dim(U + W) = \dim(U) + \dim(W)$|Rectas perpendiculares|
> |**$U \subseteq W$**|$\dim(U + W) = \dim(W)$|Recta en plano|
> |**$U = W$**|$\dim(U + W) = \dim(U)$|Mismo subespacio|
> |**Máxima intersección**|$\dim(U \cap W) = \min(\dim U, \dim W)$|Un subespacio contiene al otro|

> [!example]- 📝 Ejemplo de Cálculo Detallado
> 
> En $\mathbb{R}^4$:
> 
> $$U = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix}\right}$$
> 
> $$W = \text{span}\left{\begin{bmatrix} 1 \ 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \ 1 \end{bmatrix}\right}$$
> 
> **Paso 1:** Dimensiones básicas
> 
> - $\dim(U) = 2$ (dos vectores L.I.)
> - $\dim(W) = 2$ (dos vectores L.I.)
> 
> **Paso 2:** Encontrar $U \cap W$
> 
> $\vec{v} \in U \cap W$ si: $$\vec{v} = c_1\begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix} = d_1\begin{bmatrix} 1 \ 1 \ 0 \ 0 \end{bmatrix} + d_2\begin{bmatrix} 0 \ 0 \ 1 \ 1 \end{bmatrix}$$
> 
> Sistema de ecuaciones: $$\begin{cases} c_1 = d_1 \ c_2 = d_1 \ c_1 = d_2 \ c_2 = d_2 \end{cases}$$
> 
> De las primeras dos: $c_1 = c_2 = d_1$
> 
> De las últimas dos: $c_1 = c_2 = d_2$
> 
> Por tanto: $c_1 = c_2$, y podemos tomar $c_1 = c_2 = t$:
> 
> $$U \cap W = \text{span}\left{\begin{bmatrix} 1 \ 1 \ 1 \ 1 \end{bmatrix}\right}$$
> 
> **Paso 3:** $\dim(U \cap W) = 1$
> 
> **Paso 4:** Aplicar fórmula de Grassmann
> 
> $$\dim(U + W) = 2 + 2 - 1 = 3$$
> 
> **Verificación:** Base de $U + W$
> 
> $$\left{\begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \ 0 \end{bmatrix}\right}$$
> 
> Efectivamente tiene 3 vectores L.I. ✓

### Propiedades Algebraicas

> [!note]- 🎨 Operaciones con Sumas
> 
> **1. Conmutatividad:** $$U + W = W + U$$
> 
> _Demostración:_
> 
> - $\vec{v} \in U + W \Rightarrow \vec{v} = \vec{u} + \vec{w} = \vec{w} + \vec{u} \in W + U$
> 
> ---
> 
> **2. Asociatividad:** $$(U + V) + W = U + (V + W)$$
> 
> Podemos escribir sin paréntesis: $U + V + W$
> 
> ---
> 
> **3. Elemento neutro:** $$U + {\vec{0}} = U$$
> 
> El subespacio cero no agrega nada.
> 
> ---
> 
> **4. Idempotencia:** $$U + U = U$$
> 
> Un subespacio sumado consigo mismo es él mismo.
> 
> ---
> 
> **5. Monotonía:** $$U \subseteq V \Rightarrow U + W \subseteq V + W$$
> 
> Si un subespacio contiene a otro, sus sumas mantienen la contención.
> 
> ---
> 
> **6. Absorción:** $$U \subseteq W \Rightarrow U + W = W$$
> 
> Si $U$ está contenido en $W$, la suma es simplemente $W$.
> 
> ---
> 
> **7. Distributiva parcial (intersección):** $$U \cap (V + W) \supseteq (U \cap V) + (U \cap W)$$
> 
> (⚠️ Igualdad no siempre se cumple, solo contención)
> 
> **Contraejemplo:** En $\mathbb{R}^2$, con $U = W = $ eje $x$, $V = $ eje $y$:
> 
> - $U \cap (V + W) = U \cap \mathbb{R}^2 = U$
> - $(U \cap V) + (U \cap W) = {\vec{0}} + U = U$
> 
> En este caso sí hay igualdad, pero no siempre.
> 
> ---
> 
> **8. Modularidad:**
> 
> Si $U \subseteq W$, entonces: $$U + (V \cap W) = (U + V) \cap W$$
> 
> (Propiedad de Dedekind)

### Suma de Múltiples Subespacios

> [!note]- 🔢 Generalización
> 
> **Definición:** Para subespacios $U_1, U_2, \ldots, U_k$:
> 
> $$U_1 + U_2 + \cdots + U_k = \left{\sum_{i=1}^k \vec{u}_i \mid \vec{u}_i \in U_i\right}$$
> 
> **Suma directa múltiple:** $U_1 \oplus U_2 \oplus \cdots \oplus U_k$
> 
> Es directa si cada $\vec{v}$ se escribe únicamente como suma.
> 
> **Condición equivalente:** $$U_i \cap (U_1 + \cdots + U_{i-1} + U_{i+1} + \cdots + U_k) = {\vec{0}}$$
> 
> para todo $i$.
> 
> **Fórmula dimensional:** $$\dim(U_1 \oplus \cdots \oplus U_k) = \sum_{i=1}^k \dim(U_i)$$
> 
> ---
> 
> **Ejemplo:** Descomposición de $\mathbb{R}^n$
> 
> $$\mathbb{R}^n = \text{span}{\vec{e}_1} \oplus \text{span}{\vec{e}_2} \oplus \cdots \oplus \text{span}{\vec{e}_n}$$

---

## 💡 Ejemplos Detallados

### Ejemplo 1: Suma en $\mathbb{R}^3$

> [!example]- 📐 Recta + Plano
> 
> **Subespacio $U$ (recta):** $$U = \text{span}\left{\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}\right}$$
> 
> **Subespacio $W$ (plano $xy$):** $$W = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}\right} = \left{\begin{bmatrix} x \ y \ 0 \end{bmatrix} \mid x,y \in \mathbb{R}\right}$$
> 
> **Paso 1: Encontrar intersección**
> 
> $$\vec{v} \in U \cap W \Leftrightarrow \vec{v} = c\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} = \begin{bmatrix} a \ b \ 0 \end{bmatrix}$$
> 
> De la tercera componente: $c = 0$
> 
> Por tanto: $U \cap W = {\vec{0}}$
> 
> **Paso 2: Calcular dimensión de la suma**
> 
> $$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W) = 1 + 2 - 0 = 3$$
> 
> **Conclusión:** $U \oplus W = \mathbb{R}^3$ (suma directa)
> 
> **Interpretación:** La recta no está en el plano, por eso generan todo el espacio.
> 
> **Base de $U \oplus W$:** $$\left{\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}\right}$$
> 
> **Representación única:** Todo vector $\begin{bmatrix} x \ y \ z \end{bmatrix}$ se escribe como:
> 
> $$\begin{bmatrix} x \ y \ z \end{bmatrix} = z\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} + (x-z)\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + (y-z)\begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}$$

### Ejemplo 2: Suma No Directa

> [!example]- 📐 Planos con Intersección
> 
> **Plano $U$:** $x + y + z = 0$
> 
> Forma paramétrica: $$\begin{bmatrix} x \ y \ z \end{bmatrix} = y\begin{bmatrix} -1 \ 1 \ 0 \end{bmatrix} + z\begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix}$$
> 
> $$U = \text{span}\left{\begin{bmatrix} -1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix}\right}$$
> 
> **Plano $W$:** $x - y + z = 0$
> 
> Forma paramétrica: $$\begin{bmatrix} x \ y \ z \end{bmatrix} = y\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} + z\begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix}$$
> 
> $$W = \text{span}\left{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} -1 \ 0 \ 1 \end{bmatrix}\right}$$
> 
> **Paso 1: Encontrar intersección**
> 
> Sistema: $$\begin{cases} x + y + z = 0 \ x - y + z = 0 \end{cases}$$
> 
> Sumando: $2x + 2z = 0 \Rightarrow z = -x$
> 
> Restando: $2y = 0 \Rightarrow y = 0$
> 
> $$U \cap W = \text{span}\left{\begin{bmatrix} 1 \ 0 \ -1 \end{bmatrix}\right}$$
> 
> $\dim(U \cap W) = 1$ (recta)
> 
> **Paso 2: Dimensión de la suma**
> 
> $$\dim(U + W) = 2 + 2 - 1 = 3 = \dim(\mathbb{R}^3)$$
> 
> Por lo tanto: $U + W = \mathbb{R}^3$
> 
> **Paso 3: ¿Es suma directa?**
> 
> NO, porque $U \cap W \neq {\vec{0}}$
> 
> **Representación NO única:** El vector $\begin{bmatrix} 1 \ 0 \ -1 \end{bmatrix}$ está en $U$ y en $W$:
> 
> - Como elemento de $U$: $\begin{bmatrix} 1 \ 0 \ -1 \end{bmatrix} + \vec{0}$
> - Otra forma: $\vec{0} + \begin{bmatrix} 1 \ 0 \ -1 \end{bmatrix}$
> 
> Ambas representaciones dan el mismo vector.

### Ejemplo 3: Matrices $2 \times 2$

> [!example]- 📐 Subespacios de Matrices
> 
> **Espacio:** $M_{2 \times 2}$ (matrices $2 \times 2$)
> 
> **Subespacio $U$:** Matrices simétricas $$U = \left{\begin{bmatrix} a & b \ b & c \end{bmatrix} \mid a,b,c \in \mathbb{R}\right}$$
> 
> Base de $U$: $$\left{\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}\right}$$
> 
> $\dim(U) = 3$
> 
> **Subespacio $W$:** Matrices antisimétricas $$W = \left{\begin{bmatrix} 0 & b \ -b & 0 \end{bmatrix} \mid b \in \mathbb{R}\right}$$
> 
> Base de $W$: $$\left{\begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix}\right}$$
> 
> $\dim(W) = 1$
> 
> **Intersección:** Una matriz es simétrica Y antisimétrica si:
> 
> $$A = A^T \text{ y } A = -A^T$$
> 
> Esto implica $A = -A$, entonces $2A = 0$, por tanto $A = 0$
> 
> $$U \cap W = \left{\begin{bmatrix} 0 & 0 \ 0 & 0 \end{bmatrix}\right}$$
> 
> **Suma directa:** $$\dim(U \oplus W) = 3 + 1 = 4 = \dim(M_{2 \times 2})$$
> 
> Por tanto: $M_{2 \times 2} = U \oplus W$
> 
> **Descomposición:** Toda matriz $A$ se escribe únicamente como:
> 
> $$A = \underbrace{\frac{A + A^T}{2}}_{\text{parte simétrica}} + \underbrace{\frac{A - A^T}{2}}_{\text{parte antisimétrica}}$$
> 
> **Ejemplo numérico:** $$\begin{bmatrix} 1 & 3 \ 2 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 2.5 \ 2.5 & 4 \end{bmatrix} + \begin{bmatrix} 0 & 0.5 \ -0.5 & 0 \end{bmatrix}$$

### Ejemplo 4: Polinomios

> [!example]- 📐 Subespacios de $\mathbb{P}_3$
> 
> **Espacio:** $\mathbb{P}_3$ = polinomios de grado ≤ 3
> 
> **Subespacio $U$:** Polinomios pares $$U = {p(x) \mid p(-x) = p(x)} = {a_0 + a_2x^2 \mid a_0, a_2 \in \mathbb{R}}$$
> 
> Base: ${1, x^2}$, $\dim(U) = 2$
> 
> **Subespacio $W$:** Polinomios impares $$W = {p(x) \mid p(-x) = -p(x)} = {a_1x + a_3x^3 \mid a_1, a_3 \in \mathbb{R}}$$
> 
> Base: ${x, x^3}$, $\dim(W) = 2$
> 
> **Intersección:** $p(x)$ par e impar
> 
> $$p(x) = p(-x) = -p(x) \Rightarrow 2p(x) = 0 \Rightarrow p(x) = 0$$
> 
> $$U \cap W = {0}$$
> 
> **Suma directa:** $$\dim(U \oplus W) = 2 + 2 = 4 = \dim(\mathbb{P}_3)$$
> 
> $$\mathbb{P}_3 = U \oplus W$$
> 
> **Descomposición:** Todo polinomio $p(x) = a_0 + a_1x + a_2x^2 + a_3x^3$:
> 
> $$p(x) = \underbrace{(a_0 + a_2x^2)}_{\text{parte par}} + \underbrace{(a_1x + a_3x^3)}_{\text{parte impar}}$$

---

## 🔧 Métodos de Cálculo

### Método 1: Encontrar Base de $U + W$

> [!tip]- 🛠️ Algoritmo Sistemático
> 
> **Objetivo:** Encontrar base de $U + W$
> 
> **Procedimiento:**
> 
> 1. **Tomar bases:**
>     - Base de $U$: ${\vec{u}_1, \ldots, \vec{u}_k}$
>     - Base de $W$: ${\vec{w}_1, \ldots, \vec{w}_m}$
> 2. **Juntar todos los vectores:** $$S = {\vec{u}_1, \ldots, \vec{u}_k, \vec{w}_1, \ldots, \vec{w}_m}$$
>     
> 3. **Extraer subconjunto L.I.:**
>     
>     - Formar matriz con vectores como columnas
>     - Reducir a forma escalonada
>     - Columnas con pivotes forman base de $U + W$
> 4. **Dimensión:** $$\dim(U + W) = \text{número de pivotes}$$
>     
> 
> ---
> 
> **Ejemplo:** En $\mathbb{R}^3$
> 
> $$U = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right}$$
> 
> $$W = \text{span}\left{\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 2 \ 1 \ 1 \end{bmatrix}\right}$$
> 
> **Paso 1:** Matriz con todos los vectores
> 
> $$M = \begin{bmatrix} 1 & 0 & 1 & 2 \ 0 & 1 & 1 & 1 \ 1 & 1 & 0 & 1 \end{bmatrix}$$
> 
> **Paso 2:** Forma escalonada
> 
> $$\begin{bmatrix} 1 & 0 & 1 & 2 \ 0 & 1 & 1 & 1 \ 0 & 0 & -2 & -2 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 0 & 1 \ 0 & 1 & 0 & 0 \ 0 & 0 & 1 & 1 \end{bmatrix}$$
> 
> **Paso 3:** Tres pivotes en columnas 1, 2, 3
> 
> Base de $U + W$: $$\left{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}\right}$$
> 
> $$\dim(U + W) = 3 = \mathbb{R}^3$$

### Método 2: Encontrar $U \cap W$

> [!tip]- 🛠️ Intersección de Subespacios
> 
> **Método general:**
> 
> 1. **Expresar condiciones:**
>     
>     - $\vec{v} \in U$: combinación lineal de base de $U$
>     - $\vec{v} \in W$: combinación lineal de base de $W$
> 2. **Igualar:** $$c_1\vec{u}_1 + \cdots + c_k\vec{u}_k = d_1\vec{w}_1 + \cdots + d_m\vec{w}_m$$
>     
> 3. **Sistema homogéneo:** Reorganizar como $A\vec{x} = \vec{0}$
>     
> 4. **Resolver:** Espacio nulo da las combinaciones que están en ambos
>     
> 5. **Base de $U \cap W$:** Usar soluciones para construir vectores de la intersección
>     
> 
> ---
> 
> **Ejemplo:** Continúa del anterior
> 
> $$U = \text{span}\left{\vec{u}_1 = \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \vec{u}_2 = \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}\right}$$
> 
> $$W = \text{span}\left{\vec{w}_1 = \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \vec{w}_2 = \begin{bmatrix} 2 \ 1 \ 1 \end{bmatrix}\right}$$
> 
> **Paso 1:** $\vec{v} \in U \cap W$ si:
> 
> $$c_1\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} = d_1\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} + d_2\begin{bmatrix} 2 \ 1 \ 1 \end{bmatrix}$$
> 
> **Paso 2:** Sistema
> 
> $$\begin{cases} c_1 = d_1 + 2d_2 \ c_2 = d_1 + d_2 \ c_1 + c_2 = d_2 \end{cases}$$
> 
> **Paso 3:** Reorganizar: $c_1 - d_1 - 2d_2 = 0$, etc.
> 
> Matriz aumentada: $$\begin{bmatrix} 1 & 0 & -1 & -2 & 0 \ 0 & 1 & -1 & -1 & 0 \ 1 & 1 & 0 & -1 & 0 \end{bmatrix}$$
> 
> **Paso 4:** Resolver (forma escalonada)
> 
> Solución: $c_1 = -t$, $c_2 = -t$, $d_1 = t$, $d_2 = 0$ (tomando $t$ como parámetro)
> 
> **Paso 5:** Vector en intersección
> 
> $$\vec{v} = -t\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + (-t)\begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} = t\begin{bmatrix} -1 \ -1 \ -2 \end{bmatrix}$$
> 
> $$U \cap W = \text{span}\left{\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}\right}$$
> 
> $$\dim(U \cap W) = 1$$
> 
> **Verificación de Grassmann:** $$\dim(U + W) = 2 + 2 - 1 = 3$$ ✓

### Método 3: Verificar Suma Directa

> [!tip]- 🛠️ Tres Formas de Verificar
> 
> **Forma 1: Intersección**
> 
> Verificar $U \cap W = {\vec{0}}$
> 
> ```
> 1. Encontrar U ∩ W (método anterior)
> 2. Si solo contiene el vector cero → suma directa
> 3. Si contiene otros vectores → NO directa
> ```
> 
> ---
> 
> **Forma 2: Dimensión**
> 
> Verificar $\dim(U + W) = \dim(U) + \dim(W)$
> 
> ```
> 4. Calcular dim(U) y dim(W)
> 5. Calcular dim(U + W) (encontrando base)
> 6. Comparar: si suman directamente → directa
> ```
> 
> ---
> 
> **Forma 3: Independencia lineal**
> 
> Juntar bases y verificar L.I.
> 
> ```
> 7. Base de U: {u₁, ..., uₖ}
> 8. Base de W: {w₁, ..., wₘ}
> 9. Verificar si {u₁, ..., uₖ, w₁, ..., wₘ} es L.I.
> 10. Si sí → suma directa
> ```
> 
> ---
> 
> **Ejemplo comparativo:**
> 
> En $\mathbb{R}^3$: $$U = \text{eje } x, \quad W = \text{plano } yz$$
> 
> **Forma 1:** $$U \cap W = {\vec{0}}$$ ✓ Directa
> 
> **Forma 2:** $$\dim(U + W) = 1 + 2 = 3 = \dim(U) + \dim(W)$$ ✓ Directa
> 
> **Forma 3:** Bases: $\left{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}\right}$ y $\left{\begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right}$
> 
> Conjunto $\left{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right}$ es L.I. ✓ Directa

---

## 🎯 Aplicaciones

### Aplicación 1: Descomposición de Soluciones

> [!example]- 🔬 Ecuaciones Diferenciales
> 
> **Ecuación:** $\frac{d^2y}{dx^2} + y = \sin(x)$
> 
> **Teorema fundamental:** La solución general es:
> 
> $$y(x) = y_h(x) + y_p(x)$$
> 
> donde:
> 
> - $y_h$ = solución homogénea ($\frac{d^2y}{dx^2} + y = 0$)
> - $y_p$ = solución particular
> 
> **Como suma de subespacios:**
> 
> Sea $S$ el espacio de todas las soluciones de la ecuación completa.
> 
> $$S = U + W$$
> 
> donde:
> 
> - $U$ = espacio de soluciones homogéneas
> - $W$ = ${y_p}$ (un vector particular)
> 
> **Propiedades:**
> 
> - $\dim(U) = 2$ (dos constantes arbitrarias)
> - Soluciones: $y_h = c_1\cos(x) + c_2\sin(x)$
> - Una particular: $y_p = -\frac{1}{2}x\cos(x)$
> 
> **Forma general:** $$y = c_1\cos(x) + c_2\sin(x) - \frac{1}{2}x\cos(x)$$
> 
> **NO es suma directa** porque estamos sumando un subespacio con un vector (traslación), no dos subespacios.

### Aplicación 2: Proyecciones Ortogonales

> [!example]- 📊 Descomposición en Componentes
> 
> **Teorema de descomposición ortogonal:**
> 
> Si $U$ es subespacio de $\mathbb{R}^n$ con producto interno, entonces:
> 
> $$\mathbb{R}^n = U \oplus U^\perp$$
> 
> donde $U^\perp = {\vec{v} \mid \vec{v} \cdot \vec{u} = 0 \text{ para todo } \vec{u} \in U}$
> 
> **Descomposición de vectores:**
> 
> Todo $\vec{v} \in \mathbb{R}^n$ se escribe únicamente como:
> 
> $$\vec{v} = \text{proj}_U(\vec{v}) + \text{proj}_{U^\perp}(\vec{v})$$
> 
> ---
> 
> **Ejemplo:** En $\mathbb{R}^3$
> 
> $$U = \text{plano } xy = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}\right}$$
> 
> $$U^\perp = \text{eje } z = \text{span}\left{\begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right}$$
> 
> Vector $\vec{v} = \begin{bmatrix} 3 \ 4 \ 5 \end{bmatrix}$:
> 
> $$\text{proj}_U(\vec{v}) = \begin{bmatrix} 3 \ 4 \ 0 \end{bmatrix}, \quad \text{proj}_{U^\perp}(\vec{v}) = \begin{bmatrix} 0 \ 0 \ 5 \end{bmatrix}$$
> 
> $$\begin{bmatrix} 3 \ 4 \ 5 \end{bmatrix} = \begin{bmatrix} 3 \ 4 \ 0 \end{bmatrix} + \begin{bmatrix} 0 \ 0 \ 5 \end{bmatrix}$$
> 
> ---
> 
> **Aplicación en Machine Learning:**
> 
> - **Regresión lineal:** Proyectar datos en espacio de columnas
> - **PCA:** Proyectar en subespacios principales
> - **Filtrado de ruido:** Separar señal (en $U$) de ruido (en $U^\perp$)

### Aplicación 3: Descomposición de Matrices

> [!example]- 🔢 Teoría de Matrices
> 
> **Descomposición en partes simétricas:**
> 
> Toda matriz $A \in M_{n \times n}$ se escribe como:
> 
> $$A = \underbrace{\frac{A + A^T}{2}}_{\text{parte simétrica } S} + \underbrace{\frac{A - A^T}{2}}_{\text{parte antisimétrica } K}$$
> 
> **Como suma directa:**
> 
> $$M_{n \times n} = \text{Sym}_n \oplus \text{Skew}_n$$
> 
> donde:
> 
> - $\text{Sym}_n$ = matrices simétricas
> - $\text{Skew}_n$ = matrices antisimétricas
> 
> **Dimensiones:**
> 
> - $\dim(\text{Sym}_n) = \frac{n(n+1)}{2}$
> - $\dim(\text{Skew}_n) = \frac{n(n-1)}{2}$
> - $\dim(M_{n \times n}) = n^2$
> 
> **Verificación:** $$\frac{n(n+1)}{2} + \frac{n(n-1)}{2} = \frac{n^2 + n + n^2 - n}{2} = n^2$$ ✓
> 
> ---
> 
> **Ejemplo:** $n = 3$
> 
> $$A = \begin{bmatrix} 1 & 2 & 3 \ 4 & 5 & 6 \ 7 & 8 & 9 \end{bmatrix}$$
> 
> $$S = \frac{1}{2}\begin{bmatrix} 2 & 6 & 10 \ 6 & 10 & 14 \ 10 & 14 & 18 \end{bmatrix} = \begin{bmatrix} 1 & 3 & 5 \ 3 & 5 & 7 \ 5 & 7 & 9 \end{bmatrix}$$
> 
> $$K = \frac{1}{2}\begin{bmatrix} 0 & -2 & -4 \ 2 & 0 & -2 \ 4 & 2 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -1 & -2 \ 1 & 0 & -1 \ 2 & 1 & 0 \end{bmatrix}$$
> 
> Verificar: $S + K = A$ ✓

### Aplicación 4: Teoría de Códigos

> [!example]- 💻 Códigos Correctores de Errores
> 
> **Contexto:** Códigos lineales para corrección de errores
> 
> **Espacio:** $\mathbb{F}_2^n$ (vectores binarios de longitud $n$)
> 
> **Código lineal $C$:** Subespacio de $\mathbb{F}_2^n$
> 
> **Código dual:** $C^\perp = {\vec{v} \mid \vec{v} \cdot \vec{c} = 0 \text{ para todo } \vec{c} \in C}$
> 
> **Propiedad dimensional:**
> 
> $$\dim(C) + \dim(C^\perp) = n$$
> 
> Si además $C \cap C^\perp = {\vec{0}}$:
> 
> $$\mathbb{F}_2^n = C \oplus C^\perp$$
> 
> ---
> 
> **Ejemplo: Código de Hamming (7,4)**
> 
> - $n = 7$ bits totales
> - $\dim(C) = 4$ bits de información
> - $\dim(C^\perp) = 3$ bits de paridad
> 
> **Descomposición:** Mensaje recibido $\vec{r} \in \mathbb{F}_2^7$:
> 
> $$\vec{r} = \vec{c} + \vec{e}$$
> 
> donde:
> 
> - $\vec{c} \in C$ (palabra código válida)
> - $\vec{e}$ (vector de error)
> 
> **Síndrome:** $\vec{s} = \text{proj}_{C^\perp}(\vec{r})$ indica el error

### Aplicación 5: Física Cuántica

> [!example]- ⚛️ Espacios de Estados
> 
> **Espacio de Hilbert:** $\mathcal{H}$ (espacio de estados cuánticos)
> 
> **Sistema compuesto:** Dos partículas con espacios $\mathcal{H}_1$ y $\mathcal{H}_2$
> 
> **Espacio total:** $\mathcal{H} = \mathcal{H}_1 \otimes \mathcal{H}_2$ (producto tensorial)
> 
> **Estados separables:** Se escriben como $|\psi\rangle = |\psi_1\rangle \otimes |\psi_2\rangle$
> 
> **Descomposición de observables:**
> 
> Todo observable $A$ se descompone:
> 
> $$A = A_{\text{diag}} + A_{\text{off-diag}}$$
> 
> donde espacios propios forman suma directa:
> 
> $$\mathcal{H} = \bigoplus_{i=1}^n E_{\lambda_i}$$
> 
> ($E_{\lambda_i}$ = espacio propio con eigenvalor $\lambda_i$)
> 
> ---
> 
> **Principio de superposición:**
> 
> Si $|\psi_1\rangle \in U$ y $|\psi_2\rangle \in W$ son estados posibles:
> 
> $$|\psi\rangle = \alpha|\psi_1\rangle + \beta|\psi_2\rangle \in U + W$$
> 
> es también un estado posible (superposición cuántica)

---

## 🎨 Visualización Geométrica

> [!note]- 📊 Interpretación Visual
> 
> ### Suma en $\mathbb{R}^2$
> 
> ```
> Recta U + Recta W:
> 
>      W ↗              Si paralelas:
>       /               U + W = U (o W)
>      /                
>     /_____ U →        Si NO paralelas:
>                       U + W = ℝ²
> ```
> 
> ### Suma en $\mathbb{R}^3$
> 
> ```
> Recta + Plano:
> 
>         ↑ L (recta)
>         |
>    _____|_____  P (plano)
>   /     |    /
>  /______|___/
> 
> Si L ⊄ P:  L + P = ℝ³
> Si L ⊂ P:  L + P = P
> ```
> 
> ### Suma Directa
> 
> ```
> U ⊕ W (suma directa):
> 
>      W
>      ↑
>      |
>      |
>  ────┼──── U
>      |
>      |
>    U ∩ W = {0}
> 
> Todo vector v se descompone:
> v = u + w (único)
> ```
> 
> ### Suma NO Directa
> 
> ```
> Planos que se intersectan:
> 
>      \  U  /
>       \   /
>        \ / ← U ∩ W (recta)
>         X
>        / \
>       /   \
>      /  W  \
> 
> U + W = ℝ³
> pero U ∩ W ≠ {0}
> ```

---

## 📋 Tabla de Resumen Completa

> [!summary]- 🔍 Referencia Rápida Extendida
> 
> ### Definiciones Fundamentales
> 
> |Concepto|Definición|Notación|
> |---|---|---|
> |**Suma**|${\vec{u} + \vec{w} \mid \vec{u} \in U, \vec{w} \in W}$|$U + W$|
> |**Suma directa**|Suma con $U \cap W = {\vec{0}}$|$U \oplus W$|
> |**Intersección**|${\vec{v} \mid \vec{v} \in U \text{ y } \vec{v} \in W}$|$U \cap W$|
> |**Complemento**|$W$ tal que $V = U \oplus W$|$W = U^c$|
> 
> ---
> 
> ### Fórmulas de Dimensión
> 
> |Situación|Fórmula|Condición|
> |---|---|---|
> |**General (Grassmann)**|$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$|Siempre|
> |**Suma directa**|$\dim(U \oplus W) = \dim(U) + \dim(W)$|$U \cap W = {\vec{0}}$|
> |**Contención**|$\dim(U + W) = \dim(W)$|$U \subseteq W$|
> |**Iguales**|$\dim(U + W) = \dim(U)$|$U = W$|
> |**Complemento**|$\dim(U) + \dim(W) = \dim(V)$|$V = U \oplus W$|
> 
> ---
> 
> ### Condiciones para Suma Directa
> 
> |Condición|Significado|Uso|
> |---|---|---|
> |$U \cap W = {\vec{0}}$|Intersección trivial|Definición|
> |$\dim(U + W) = \dim(U) + \dim(W)$|Dimensiones suman|Verificación rápida|
> |Representación única|Cada $\vec{v} = \vec{u} + \vec{w}$ única|Aplicaciones|
> |Bases L.I.|Unión de bases es L.I.|Construcción|
> 
> ---
> 
> ### Propiedades Algebraicas
> 
> |Propiedad|Enunciado|Válida|
> |---|---|---|
> |**Conmutativa**|$U + W = W + U$|✓ Sí|
> |**Asociativa**|$(U + V) + W = U + (V + W)$|✓ Sí|
> |**Identidad**|$U + {\vec{0}} = U$|✓ Sí|
> |**Idempotente**|$U + U = U$|✓ Sí|
> |**Distributiva**|$U \cap (V + W) = (U \cap V) + (U \cap W)$|✗ No siempre|
> |**Monotonía**|$U \subseteq V \Rightarrow U + W \subseteq V + W$|✓ Sí|
> |**Absorción**|$U \subseteq W \Rightarrow U + W = W$|✓ Sí|
> 
> ---
> 
> ### Casos Especiales en $\mathbb{R}^n$
> 
> |Subespacios|Intersección|Suma|Directa|
> |---|---|---|---|
> |Dos rectas distintas (no paralelas) en $\mathbb{R}^2$|${\vec{0}}$|$\mathbb{R}^2$|Sí|
> |Dos rectas paralelas en $\mathbb{R}^2$|Una recta|Una recta|No|
> |Recta y plano (recta no en plano) en $\mathbb{R}^3$|${\vec{0}}$|$\mathbb{R}^3$|Sí|
> |Recta y plano (recta en plano) en $\mathbb{R}^3$|Recta|Plano|No|
> |Dos planos distintos en $\mathbb{R}^3$|Recta o ${\vec{0}}$|$\mathbb{R}^3$|Depende|
> |Subespacio y complemento ortogonal|${\vec{0}}$|$\mathbb{R}^n$|Sí|
> 
> ---
> 
> ### Métodos de Cálculo
> 
> |Objetivo|Método|Complejidad|
> |---|---|---|
> |**Base de $U + W$**|Juntar bases, eliminar dependencias|$O(n^3)$|
> |**$\dim(U + W)$**|Contar pivotes|$O(n^3)$|
> |**$U \cap W$**|Resolver sistema homogéneo|$O(n^3)$|
> |**Verificar suma directa**|Método 1, 2 o 3|$O(n^3)$|
> |**Encontrar complemento**|Extender base|$O(n^3)$|

---

## 💪 Ejercicios Adicionales

### Nivel Básico (Continuación)

> [!example]- 🎯 Más Práctica Fundamental
> 
> **6.** En $\mathbb{R}^3$, sean: $$U = {(x,y,z) \mid x + y = 0}$$ $$W = {(x,y,z) \mid y + z = 0}$$
> 
> a) Encontrar bases de $U$ y $W$ b) Calcular $\dim(U)$ y $\dim(W)$ c) Encontrar $U \cap W$ d) Calcular $\dim(U + W)$ e) ¿Es suma directa?
> 
> ---
> 
> **7.** Demostrar que si $U \subseteq W$, entonces $U + W = W$
> 
> ---
> 
> **8.** En $\mathbb{P}_2$, sean: $$U = {p(x) \mid p(0) = 0}$$ $$W = {p(x) \mid p(1) = 0}$$
> 
> a) Encontrar bases de $U$ y $W$ b) Determinar si $\mathbb{P}_2 = U + W$ c) ¿Es suma directa?
> 
> ---
> 
> **9.** Verificar que $U + W$ es subespacio probando que es cerrado bajo suma y multiplicación escalar.
> 
> ---
> 
> **10.** Si $\dim(U) = 3$, $\dim(W) = 4$ y $U + W = \mathbb{R}^5$, ¿cuál es $\dim(U \cap W)$?

### Nivel Intermedio (Continuación)

> [!example]- 🎯 Desafío Moderado Extendido
> 
> **11.** En $M_{2 \times 2}$, sean: $$U = \left{\begin{bmatrix} a & b \ c & d \end{bmatrix} \mid a + d = 0\right}$$ $$W = \left{\begin{bmatrix} a & b \ c & d \end{bmatrix} \mid b = c\right}$$
> 
> a) Demostrar que $U$ y $W$ son subespacios 
> b) Encontrar $\dim(U)$ y $\dim(W)$ 
> c) Calcular $U \cap W$ 
> d) Calcular $\dim(U + W)$
> e) ¿Es $M_{2 \times 2} = U + W$?
> 
> ---
> 
> **12.** Demostrar que si $V = U \oplus W$, entonces para todo $\vec{v} \in V$ existe una única descomposición $\vec{v} = \vec{u} + \vec{w}$ con $\vec{u} \in U$, $\vec{w} \in W$.
> 
> ---
> 
> **13.** En $\mathbb{R}^4$, encontrar un complemento $W$ para: $$U = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix}\right}$$
> 
> tal que $\mathbb{R}^4 = U \oplus W$
> 
> ---
> 
> **14.** Demostrar: Si $U_1 \subseteq U_2$ y $W_1 \subseteq W_2$, entonces $U_1 + W_1 \subseteq U_2 + W_2$
> 
> ---
> 
> **15.** Sean $U, V, W$ subespacios con $U \subseteq W$. Demostrar: $$U + (V \cap W) = (U + V) \cap W$$
> 
> (Ley modular de Dedekind)

### Nivel Avanzado

> [!example]- 🎯 Desafío Avanzado
> 
> **16.** Demostrar que si $\dim(V) = n$ y $U$ es subespacio con $\dim(U) = k$, entonces existe un complemento $W$ tal que $V = U \oplus W$ con $\dim(W) = n - k$.
> 
> ---
> 
> **17.** **Teorema de las dimensiones generalizado:**
> 
> Para tres subespacios $U, V, W$, demostrar:
> 
> $$\dim(U + V + W) = \dim(U) + \dim(V) + \dim(W)$$ $$- \dim(U \cap V) - \dim(V \cap W) - \dim(U \cap W)$$ $$+ \dim(U \cap V \cap W)$$
> 
> ---
> 
> **18.** Sea $T: V \to V$ una transformación lineal. Demostrar:
> 
> $$V = \ker(T) \oplus \text{Im}(T) \Leftrightarrow T^2 = T$$
> 
> (Proyecciones)
> 
> ---
> 
> **19.** En $\mathbb{C}^n$ con producto interno, demostrar:
> 
> a) $(U + W)^\perp = U^\perp \cap W^\perp$ b) $(U \cap W)^\perp = U^\perp + W^\perp$
> 
> ---
> 
> **20.** **Descomposición de Jordan:**
> 
> Demostrar que si $T: V \to V$ es nilpotente y $U = \ker(T)$, $W = \text{Im}(T)$, entonces:
> 
> $$\dim(U) + \dim(W) \geq \dim(V)$$
> 
> con igualdad si y solo si $U \cap W = {\vec{0}}$

---

## ✅ Soluciones Selectas

### Soluciones Básicas

> [!success]- 🔑 Respuestas Nivel Básico
> 
> **6.**
> 
> a) **Base de $U$:**
> 
> $x + y = 0 \Rightarrow y = -x$
> 
> $$\begin{bmatrix} x \ y \ z \end{bmatrix} = \begin{bmatrix} x \ -x \ z \end{bmatrix} = x\begin{bmatrix} 1 \ -1 \ 0 \end{bmatrix} + z\begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> Base: $\left{\begin{bmatrix} 1 \ -1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right}$
> 
> **Base de $W$:**
> 
> $y + z = 0 \Rightarrow z = -y$
> 
> $$\begin{bmatrix} x \ y \ z \end{bmatrix} = \begin{bmatrix} x \ y \ -y \end{bmatrix} = x\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + y\begin{bmatrix} 0 \ 1 \ -1 \end{bmatrix}$$
> 
> Base: $\left{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ -1 \end{bmatrix}\right}$
> 
> b) $\dim(U) = 2$, $\dim(W) = 2$
> 
> c) **Intersección:** $x + y = 0$ y $y + z = 0$
> 
> De la primera: $y = -x$
> 
> De la segunda: $z = -y = x$
> 
> $$U \cap W = \text{span}\left{\begin{bmatrix} 1 \ -1 \ 1 \end{bmatrix}\right}$$
> 
> $\dim(U \cap W) = 1$
> 
> d) Por Grassmann: $$\dim(U + W) = 2 + 2 - 1 = 3$$
> 
> e) **NO es suma directa** porque $U \cap W \neq {\vec{0}}$
> 
> Pero sí es $U + W = \mathbb{R}^3$
> 
> ---
> 
> **7.** **Demostración:**
> 
> Queremos probar: $U + W = W$
> 
> **($\subseteq$)** Sea $\vec{v} \in U + W$, entonces $\vec{v} = \vec{u} + \vec{w}$ con $\vec{u} \in U$, $\vec{w} \in W$.
> 
> Como $U \subseteq W$, tenemos $\vec{u} \in W$.
> 
> Entonces $\vec{v} = \vec{u} + \vec{w} \in W$ (suma de vectores de $W$)
> 
> **($\supseteq$)** Sea $\vec{w} \in W$.
> 
> Entonces $\vec{w} = \vec{0} + \vec{w}$ con $\vec{0} \in U$ (todo subespacio contiene $\vec{0}$)
> 
> Por tanto $\vec{w} \in U + W$
> 
> Conclusión: $U + W = W$ ✓
> 
> ---
> 
> **8.**
> 
> a) **Base de $U$:** $p(0) = 0$
> 
> Si $p(x) = a_0 + a_1x + a_2x^2$, entonces $p(0) = a_0 = 0$
> 
> $$U = {a_1x + a_2x^2} = \text{span}{x, x^2}$$
> 
> Base: ${x, x^2}$, $\dim(U) = 2$
> 
> **Base de $W$:** $p(1) = 0$
> 
> $p(1) = a_0 + a_1 + a_2 = 0 \Rightarrow a_0 = -a_1 - a_2$
> 
> $$p(x) = (-a_1 - a_2) + a_1x + a_2x^2 = a_1(x - 1) + a_2(x^2 - 1)$$
> 
> Base: ${x - 1, x^2 - 1}$, $\dim(W) = 2$
> 
> b) **Intersección:** $p(0) = 0$ y $p(1) = 0$
> 
> $p(x) = a_1x + a_2x^2$ con $a_1 + a_2 = 0$
> 
> Entonces $a_2 = -a_1$:
> 
> $$p(x) = a_1x - a_1x^2 = a_1(x - x^2)$$
> 
> $$U \cap W = \text{span}{x - x^2}$$
> 
> $\dim(U \cap W) = 1$
> 
> **Dimensión de la suma:** $$\dim(U + W) = 2 + 2 - 1 = 3 = \dim(\mathbb{P}_2)$$
> 
> Por tanto: $\boxed{\mathbb{P}_2 = U + W}$ ✓
> 
> c) **NO es suma directa** porque $U \cap W \neq {\vec{0}}$
> 
> ---
> 
> **10.** Usar Grassmann:
> 
> $$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$$
> 
> Como $U + W = \mathbb{R}^5$:
> 
> $$5 = 3 + 4 - \dim(U \cap W)$$
> 
> $$\boxed{\dim(U \cap W) = 2}$$

### Soluciones Intermedias

> [!success]- 🔑 Respuestas Nivel Intermedio
> 
> **11.**
> 
> a) **$U$ es subespacio:**
> 
> - $\vec{0}$ (matriz cero): $0 + 0 = 0$ ✓
> - Cerrado bajo suma: Si $a_1 + d_1 = 0$ y $a_2 + d_2 = 0$, entonces $(a_1 + a_2) + (d_1 + d_2) = 0$ ✓
> - Cerrado bajo escalares: Si $a + d = 0$, entonces $ca + cd = c(a + d) = 0$ ✓
> 
> **$W$ es subespacio:** (Similar)
> 
> b) **Dimensión de $U$:**
> 
> Condición: $d = -a$
> 
> $$\begin{bmatrix} a & b \ c & -a \end{bmatrix} = a\begin{bmatrix} 1 & 0 \ 0 & -1 \end{bmatrix} + b\begin{bmatrix} 0 & 1 \ 0 & 0 \end{bmatrix} + c\begin{bmatrix} 0 & 0 \ 1 & 0 \end{bmatrix}$$
> 
> Base: $\left{\begin{bmatrix} 1 & 0 \ 0 & -1 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 1 & 0 \end{bmatrix}\right}$
> 
> $$\boxed{\dim(U) = 3}$$
> 
> **Dimensión de $W$:**
> 
> Condición: $c = b$
> 
> $$\begin{bmatrix} a & b \ b & d \end{bmatrix} = a\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix} + b\begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix} + d\begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}$$
> 
> $$\boxed{\dim(W) = 3}$$
> 
> c) **Intersección:** $a + d = 0$ y $b = c$
> 
> $$\begin{bmatrix} a & b \ b & -a \end{bmatrix} = a\begin{bmatrix} 1 & 0 \ 0 & -1 \end{bmatrix} + b\begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix}$$
> 
> Base de $U \cap W$: $\left{\begin{bmatrix} 1 & 0 \ 0 & -1 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix}\right}$
> 
> $$\boxed{\dim(U \cap W) = 2}$$
> 
> d) Por Grassmann: $$\dim(U + W) = 3 + 3 - 2 = 4$$
> 
> e) Como $\dim(M_{2 \times 2}) = 4$ y $\dim(U + W) = 4$:
> 
> $$\boxed{M_{2 \times 2} = U + W}$$ ✓
> 
> ---
> 
> **12.** **Demostración:**
> 
> **Existencia:** Ya garantizada por definición de suma.
> 
> **Unicidad:** Supongamos dos descomposiciones:
> 
> $$\vec{v} = \vec{u}_1 + \vec{w}_1 = \vec{u}_2 + \vec{w}_2$$
> 
> con $\vec{u}_1, \vec{u}_2 \in U$ y $\vec{w}_1, \vec{w}_2 \in W$.
> 
> Entonces: $$\vec{u}_1 - \vec{u}_2 = \vec{w}_2 - \vec{w}_1$$
> 
> El lado izquierdo está en $U$, el derecho en $W$.
> 
> Por tanto: $\vec{u}_1 - \vec{u}_2 \in U \cap W$
> 
> Como $U \cap W = {\vec{0}}$ (suma directa):
> 
> $$\vec{u}_1 - \vec{u}_2 = \vec{0} \Rightarrow \vec{u}_1 = \vec{u}_2$$
> 
> $$\vec{w}_2 - \vec{w}_1 = \vec{0} \Rightarrow \vec{w}_1 = \vec{w}_2$$
> 
> Por tanto la descomposición es única ✓
> 
> ---
> 
> **13.** **Solución:**
> 
> Necesitamos $W$ con $\dim(W) = 2$ tal que $U \cap W = {\vec{0}}$
> 
> **Opción 1:** $$W = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \ 0 \end{bmatrix}\right}$$
> 
> **Verificar:** Vector en $U \cap W$:
> 
> $$c_1\begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \ 0 \ 1 \end{bmatrix} = d_1\begin{bmatrix} 1 \ 0 \ 0 \ 0 \end{bmatrix} + d_2\begin{bmatrix} 0 \ 0 \ 1 \ 0 \end{bmatrix}$$
> 
> Sistema: $$\begin{cases} c_1 = d_1 \ c_2 = 0 \ c_1 = d_2 \ c_2 = 0 \end{cases}$$
> 
> De ecuaciones 1 y 3: $d_1 = c_1 = d_2$
> 
> De la matriz original: $c_1 = d_2$ (fila 3), pero $c_1 = 0$ (de segunda ecuación necesitaría...)
> 
> Realmente: $c_1 = d_1$, $c_1 = d_2$ implica $d_1 = d_2$, pero mirando fila 2: $c_2 = 0$.
> 
> Sistema implica $c_1 = c_2 = d_1 = d_2 = 0$
> 
> $$\boxed{W = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \ 0 \end{bmatrix}\right}}$$
> 
> **Opción 2 (más simple):** $$\boxed{W = \text{span}\left{\begin{bmatrix} 1 \ 0 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \ 0 \end{bmatrix}\right}}$$
> 
> (tomar los primeros dos vectores canónicos)

### Soluciones Avanzadas

> [!success]- 🔑 Respuestas Nivel Avanzado
> 
> **16.** **Demostración:**
> 
> **Paso 1:** Sea ${\vec{u}_1, \ldots, \vec{u}_k}$ base de $U$.
> 
> **Paso 2:** Por teorema de extensión de base, podemos extender a base de $V$:
> 
> $${\vec{u}_1, \ldots, \vec{u}_k, \vec{w}_1, \ldots, \vec{w}_{n-k}}$$
> 
> **Paso 3:** Definir: $$W = \text{span}{\vec{w}_1, \ldots, \vec{w}_{n-k}}$$
> 
> Claramente $\dim(W) = n - k$
> 
> **Paso 4:** Verificar $U \cap W = {\vec{0}}$:
> 
> Si $\vec{v} \in U \cap W$, entonces:
> 
> $$\vec{v} = c_1\vec{u}_1 + \cdots + c_k\vec{u}_k = d_1\vec{w}_1 + \cdots + d_{n-k}\vec{w}_{n-k}$$
> 
> $$c_1\vec{u}_1 + \cdots + c_k\vec{u}_k - d_1\vec{w}_1 - \cdots - d_{n-k}\vec{w}_{n-k} = \vec{0}$$
> 
> Como ${\vec{u}_1, \ldots, \vec{u}_k, \vec{w}_1, \ldots, \vec{w}_{n-k}}$ es L.I.:
> 
> $$c_1 = \cdots = c_k = d_1 = \cdots = d_{n-k} = 0$$
> 
> Por tanto $\vec{v} = \vec{0}$
> 
> **Paso 5:** Verificar $V = U + W$:
> 
> Todo $\vec{v} \in V$ se escribe en la base:
> 
> $$\vec{v} = c_1\vec{u}_1 + \cdots + c_k\vec{u}_k + d_1\vec{w}_1 + \cdots + d_{n-k}\vec{w}_{n-k}$$
> 
> $$= \underbrace{(c_1\vec{u}_1 + \cdots + c_k\vec{u}_k)}_{\in U} + \underbrace{(d_1\vec{w}_1 + \cdots + d_{n-k}\vec{w}_{n-k})}_{\in W}$$
> 
> Por tanto $V = U \oplus W$ ✓
> 
> ---
> 
> **18.** **Demostración:**
> 
> **($\Rightarrow$)** Supongamos $V = \ker(T) \oplus \text{Im}(T)$
> 
> Sea $\vec{v} \in V$, entonces $\vec{v} = \vec{u} + T(\vec{w})$ con $\vec{u} \in \ker(T)$, $T(\vec{w}) \in \text{Im}(T)$
> 
> Aplicar $T$: $$T(\vec{v}) = T(\vec{u}) + T(T(\vec{w})) = \vec{0} + T^2(\vec{w})$$
> 
> Pero $T(\vec{v}) \in \text{Im}(T)$, y por suma directa, $T(\vec{v}) = T(T(\vec{w}))$
> 
> Necesitamos probar $T^2 = T$... (complejo, requiere más desarrollo)
> 
> **($\Leftarrow$)** Supongamos $T^2 = T$
> 
> - Todo $\vec{v} = \vec{v} - T(\vec{v}) + T(\vec{v})$
> - $T(\vec{v} - T(\vec{v})) = T(\vec{v}) - T^2(\vec{v}) = T(\vec{v}) - T(\vec{v}) = \vec{0}$
> - Entonces $\vec{v} - T(\vec{v}) \in \ker(T)$
> - Y claramente $T(\vec{v}) \in \text{Im}(T)$
> 
> Por tanto $V = \ker(T) + \text{Im}(T)$
> 
> Para suma directa: si $\vec{u} \in \ker(T) \cap \text{Im}(T)$:
> 
> - $T(\vec{u}) = \vec{0}$ (en kernel)
> - $\vec{u} = T(\vec{w})$ para algún $\vec{w}$ (en imagen)
> - Entonces $\vec{0} = T(\vec{u}) = T(T(\vec{w})) = T^2(\vec{w}) = T(\vec{w}) = \vec{u}$
> 
> Por tanto $\ker(T) \cap \text{Im}(T) = {\vec{0}}$ ✓
> 
> ---
> 
> **19.** **Demostración:**
> 
> a) **($(U + W)^\perp = U^\perp \cap W^\perp$)**
> 
> **($\subseteq$)** Sea $\vec{v} \in (U + W)^\perp$
> 
> Para todo $\vec{u} \in U$: $\vec{u} = \vec{u} + \vec{0} \in U + W$
> 
> Entonces $\langle \vec{v}, \vec{u} \rangle = 0$, por tanto $\vec{v} \in U^\perp$
> 
> Similarmente $\vec{v} \in W^\perp$
> 
> Por tanto $\vec{v} \in U^\perp \cap W^\perp$
> 
> **($\supseteq$)** Sea $\vec{v} \in U^\perp \cap W^\perp$
> 
> Para todo $\vec{z} \in U + W$: $\vec{z} = \vec{u} + \vec{w}$ con $\vec{u} \in U$, $\vec{w} \in W$
> 
> $$\langle \vec{v}, \vec{z} \rangle = \langle \vec{v}, \vec{u} + \vec{w} \rangle = \langle \vec{v}, \vec{u} \rangle + \langle \vec{v}, \vec{w} \rangle = 0 + 0 = 0$$
> 
> Por tanto $\vec{v} \in (U + W)^\perp$ ✓
> 
> b) Similar, usando que $(U^\perp)^\perp = U$ en espacios de dimensión finita.

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales Completos
> 
> ### Sobre la Suma de Subespacios
> 
> ✅ **Definición:**
> 
> - $U + W = {\vec{u} + \vec{w} \mid \vec{u} \in U, \vec{w} \in W}$
> - Todas las combinaciones posibles de sumas
> - Es el subespacio más pequeño que contiene a $U$ y $W$
> 
> ✅ **Suma directa:**
> 
> - $U \oplus W$ cuando $U \cap W = {\vec{0}}$
> - Cada vector tiene representación única
> - Dimensiones se suman: $\dim(U \oplus W) = \dim(U) + \dim(W)$
> 
> ✅ **Fórmula de Grassmann:**
> 
> - $\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$
> - Generaliza principio de inclusión-exclusión
> - SIEMPRE válida
> 
> ---
> 
> ### Criterios para Suma Directa
> 
> ✅ **Cinco condiciones equivalentes:**
> 
> 1. $U \cap W = {\vec{0}}$
> 2. $\dim(U + W) = \dim(U) + \dim(W)$
> 3. Representación única de cada vector
> 4. Unión de bases es linealmente independiente
> 5. Si $\vec{u} + \vec{w} = \vec{0}$ entonces $\vec{u} = \vec{w} = \vec{0}$
> 
> ---
> 
> ### Propiedades Algebraicas
> 
> ✅ **Sí cumple:**
> 
> - Conmutativa, asociativa, idempotente
> - Monotonía, absorción
> - Elemento neutro ${\vec{0}}$
> 
> ✅ **NO cumple:**
> 
> - Distributiva (solo contención)
> - No hay inversos
> 
> ---
> 
> ### Aplicaciones Principales
> 
> ✅ **Descomposición ortogonal:** $\mathbb{R}^n = U \oplus U^\perp$
> 
> ✅ **Ecuaciones diferenciales:** Solución = homogénea + particular
> 
> ✅ **Matrices:** Simétrica + antisimétrica
> 
> ✅ **Proyecciones:** Todo vector = componente en $U$ + componente en $W$

---

## 🔗 Notas Relacionadas Ampliadas

> [!quote]- 🌐 Conexiones Conceptuales
> 
> ### Prerequisitos:
> 
> - **[[04 - Subespacios Vectoriales]]** - Qué es un subespacio
> - **[[08 - Bases]]** - Bases de subespacios
> - **[[09 - Dimensión]]** - Concepto de dimensión
> - **[[07 - Independencia Lineal]]** - Para verificar sumas directas
> 
> ### Este tema es prerequisito para:
> 
> - **[[16 - Complemento Ortogonal]]** - Caso especial de suma directa
> - **[[17 - Proyecciones]]** - Descomposición usando suma directa
> - **[[18 - Descomposición Espectral]]** - Suma de espacios propios
> - **[[22 - Teorema del Rango-Nulidad]]** - $V = \ker(T) \oplus \text{Im}(T)$ (indirectamente)
> 
> ### Temas relacionados:
> 
> - **Producto directo de espacios** - Construcción categórica
> - **Suma de Whitney** - Generalización
> - **Haces vectoriales** - En geometría diferencial
> - **Descomposición de módulos** - Álgebra abstracta
> 
> ### Aplicaciones conectadas:
> 
> - **Análisis funcional:** Descomposición de espacios de Hilbert
> - **Mecánica cuántica:** Superposición de estados
> - **Teoría de códigos:** Código y dual
> - **Análisis numérico:** Métodos de descomposición de dominios
> 
> ### Diagrama de flujo:
> 
> ```
>     Subespacios U y W
>           ↓
>      Formar U + W
>           ↓
>     ¿U ∩ W = {0}?
>      ↙         ↘
>    SÍ          NO
>     ↓           ↓
>  U ⊕ W      U + W
>  (directa)  (no directa)
>     ↓           ↓
>  dim = Σ    dim < Σ
> ```

---

## 📊 Tabla Comparativa Final

> [!summary]- 🔍 Suma vs Intersección vs Unión
> 
> |Aspecto|$U + W$|$U \cap W$|$U \cup W$|
> |---|---|---|---|
> |**Definición**|${\vec{u} + \vec{w}}$|${\vec{v} \mid \vec{v} \in U \land \vec{v} \in W}$|${\vec{v} \mid \vec{v} \in U \lor \vec{v} \in W}$|
> |**¿Es subespacio?** | ✓ Siempre | ✓ Siempre | ✗ Generalmente NO |
> | **Dimensión** | $\dim U + \dim W - \dim(U \cap W)$ | $\leq \min(\dim U, \dim W)$ | No aplica | | **Contención** | $U \subseteq U + W$ | $U \cap W \subseteq U$ | $U \subseteq U \cup W$ | | **Operación** | "Sumar" vectores | "Común" a ambos | "Juntar" ambos | | **Tamaño relativo** | Más grande que $U$ y $W$ | Más pequeño que $U$ y $W$ | Igual que $U + W$ | | **Ejemplo en $\mathbb{R}^2$** | Dos rectas → plano | Dos rectas → punto | Dos rectas → NO subespacio |

---

## 🎨 Visualización Geométrica Extendida

> [!note]- 📊 Más Interpretaciones Visuales
> 
> ### Suma Directa en $\mathbb{R}^3$
> 
> ```
> Ejemplo: Eje X ⊕ Plano YZ
> 
>         z
>         ↑
>         |  
>    _____|_____ (plano yz)
>   /     |    /
>  /      |   /
> /       |  /
> ————————•————————→ x (recta)
>         |
>         |
>         ↓ y
> 
> Cualquier punto (a,b,c):
> (a,b,c) = (a,0,0) + (0,b,c)
>           ↑         ↑
>         en X      en YZ
> ÚNICA descomposición
> ```
> 
> ### Suma NO Directa
> 
> ```
> Ejemplo: Dos planos que se cortan
> 
>      Plano 1
>        \    Plano 2
>         \  /
>          \/  ← Intersección (recta)
>          /\
>         /  \
> 
> Punto en la intersección:
> Múltiples formas de escribirlo
> como suma de vectores de ambos planos
> ```
> 
> ### Dimensiones
> 
> ```
> En ℝ³:
> 
> Recta + Recta (no paralelas):
> 1 + 1 - 0 = 2 (plano)
> 
> Recta + Plano (recta no en plano):
> 1 + 2 - 0 = 3 (todo ℝ³)
> 
> Plano + Plano (distintos):
> 2 + 2 - 1 = 3 (todo ℝ³)
> (intersección = recta)
> ```
> 
> ### Complementos Ortogonales
> 
> ```
> Subespacio y su complemento:
> 
>       U⊥ (perpendicular)
>        ↑
>        |
>        |
> ———————•——————→ U
>        |
>        |
> 
> ℝⁿ = U ⊕ U⊥
> 
> Proyecciones:
> v = proj_U(v) + proj_{U⊥}(v)
>     ↓             ↓
>   en U         en U⊥
> ```

---

## 🔬 Teoría Profunda (Opcional)

> [!note]- 🎓 Perspectiva Avanzada
> 
> ### Retículo de Subespacios
> 
> El conjunto de todos los subespacios de $V$ con las operaciones $+$ (suma) y $\cap$ (intersección) forma un **retículo modular**.
> 
> **Propiedades del retículo:**
> 
> 1. **Elemento mínimo:** ${\vec{0}}$
> 2. **Elemento máximo:** $V$
> 3. **Supremo:** $U \lor W = U + W$
> 4. **Ínfimo:** $U \land W = U \cap W$
> 
> **Ley modular:** Si $U \subseteq W$: $$U + (V \cap W) = (U + V) \cap W$$
> 
> ---
> 
> ### Teoría de Categorías
> 
> En la categoría de espacios vectoriales:
> 
> - **Suma directa** es el coproducto categórico
> - **Producto directo** es el producto categórico
> - En espacios de dimensión finita: coinciden
> 
> **Diagrama conmutativo:**
> 
> ```
>      U
>       ↘ i_U
>         ⊕
>   W → U⊕W
>    i_W ↗
> ```
> 
> Propiedad universal: Para todo espacio $Z$ con morfismos $f_U: U \to Z$ y $f_W: W \to Z$, existe único morfismo $f: U \oplus W \to Z$ tal que $f \circ i_U = f_U$ y $f \circ i_W = f_W$.
> 
> ---
> 
> ### Álgebra de Grassmann
> 
> La fórmula de dimensión se relaciona con el álgebra exterior:
> 
> $$\dim(\Lambda^k(U + W)) = \sum_{i=0}^k \binom{dim U}{i}\binom{dim W}{k-i}$$
> 
> Para $k=1$, recuperamos la fórmula de Grassmann.
> 
> ---
> 
> ### Suma de Infinitos Subespacios
> 
> Para espacios de dimensión infinita:
> 
> **Suma directa (algebraica):** $$\bigoplus_{i \in I} U_i = \left{\sum_{i \in I} \vec{u}_i \mid \vec{u}_i \in U_i, \text{ casi todos cero}\right}$$
> 
> **Suma directa (topológica):** $$\overline{\bigoplus_{i \in I} U_i} = \text{clausura de la suma algebraica}$$
> 
> **Ejemplo:** $\ell^2 = \bigoplus_{n=1}^\infty \mathbb{R}$ (topológicamente)

---

## ⚠️ Errores Comunes Adicionales

> [!warning]- 🚫 Más Trampas Frecuentes
> 
> ### Error 1: Confundir $U + W$ con $U \cup W$
> 
> **INCORRECTO:**
> 
> ```
> U + W = todos los vectores que están en U o en W
> ```
> 
> **CORRECTO:**
> 
> ```
> U + W = {u + w | u ∈ U, w ∈ W}
> (vectores que son SUMAS, no uniones)
> ```
> 
> **Ejemplo:** En $\mathbb{R}^2$, ejes $x$ e $y$:
> 
> - $U \cup W$ = solo los ejes (NO es subespacio)
> - $U + W = \mathbb{R}^2$ (todo el plano)
> 
> ---
> 
> ### Error 2: Asumir que toda suma es directa
> 
> **INCORRECTO:**
> 
> ```
> Si U y W son distintos → U ⊕ W
> ```
> 
> **CORRECTO:**
> 
> ```
> Necesita verificar U ∩ W = {0}
> ```
> 
> **Contraejemplo:** $$U = \text{span}{(1,1)}, \quad W = \text{span}{(2,2)}$$
> 
> Son distintos pero $W = 2U$, entonces $U \cap W = U \neq {\vec{0}}$
> 
> ---
> 
> ### Error 3: Dimensiones que no cuadran
> 
> **INCORRECTO:**
> 
> ```
> dim(U + W) = dim(U) + dim(W) siempre
> ```
> 
> **CORRECTO:**
> 
> ```
> Solo si es suma DIRECTA
> En general: dim(U + W) ≤ dim(U) + dim(W)
> ```
> 
> ---
> 
> ### Error 4: Olvidar verificar que es subespacio
> 
> Algunos estudiantes asumen que cualquier conjunto de sumas es subespacio.
> 
> **Siempre verificar:**
> 
> - Contiene $\vec{0}$
> - Cerrado bajo suma
> - Cerrado bajo multiplicación escalar
> 
> (Para suma de subespacios, automáticamente se cumple)
> 
> ---
> 
> ### Error 5: Base incorrecta de $U + W$
> 
> **INCORRECTO:**
> 
> ```
> Base de U + W = base de U ∪ base de W
> ```
> 
> **CORRECTO:**
> 
> ```
> Juntar bases, luego EXTRAER subconjunto L.I.
> (pueden haber vectores redundantes)
> ```
> 
> ---
> 
> ### Error 6: Confundir complemento con complemento ortogonal
> 
> **Complemento:** Cualquier $W$ tal que $V = U \oplus W$ (NO único)
> 
> **Complemento ortogonal:** $U^\perp$ (ÚNICO, requiere producto interno)
> 
> Todo complemento ortogonal es complemento, pero no viceversa.

---

## 🎯 Estrategias de Resolución

> [!tip]- 🛠️ Guía de Resolución de Problemas
> 
> ### Para encontrar $U + W$:
> 
> **Paso 1:** Identificar bases de $U$ y $W$
> 
> **Paso 2:** Juntar todos los vectores de ambas bases
> 
> **Paso 3:** Encontrar subconjunto L.I. máximo
> 
> - Método: forma escalonada de matriz con vectores como columnas
> - Los vectores correspondientes a columnas pivote forman base
> 
> **Paso 4:** Calcular dimensión
> 
> ---
> 
> ### Para encontrar $U \cap W$:
> 
> **Método 1 (Sistemas):**
> 
> 1. $\vec{v} \in U$: $\vec{v} = c_1\vec{u}_1 + \cdots + c_k\vec{u}_k$
> 2. $\vec{v} \in W$: $\vec{v} = d_1\vec{w}_1 + \cdots + d_m\vec{w}_m$
> 3. Igualar: $c_1\vec{u}_1 + \cdots + c_k\vec{u}_k = d_1\vec{w}_1 + \cdots + d_m\vec{w}_m$
> 4. Resolver sistema homogéneo
> 5. Soluciones dan vectores de intersección
> 
> **Método 2 (Ecuaciones):**
> 
> Si $U$ y $W$ están dados por ecuaciones:
> 
> 6. $U \cap W$ = vectores que satisfacen TODAS las ecuaciones
> 7. Combinar sistemas de ecuaciones
> 8. Resolver sistema resultante
> 
> ---
> 
> ### Para verificar suma directa:
> 
> **Opción A:** Calcular intersección
> 
> - Si $U \cap W = {\vec{0}}$ → directa
> 
> **Opción B:** Usar dimensiones
> 
> - Calcular $\dim(U)$, $\dim(W)$, $\dim(U + W)$
> - Si $\dim(U + W) = \dim(U) + \dim(W)$ → directa
> 
> **Opción C:** Verificar L.I. de bases unidas
> 
> - Juntar bases de $U$ y $W$
> - Si el conjunto es L.I. → directa
> 
> ---
> 
> ### Checklist de verificación:
> 
> |✓|Verificación|Método|
> |---|---|---|
> |☐|$U$ y $W$ son subespacios|Definición o dado|
> |☐|Bases correctas|Verificar L.I. y span|
> |☐|$\dim(U + W)$ calculada|Forma escalonada|
> |☐|$\dim(U \cap W)$ calculada|Sistema o ecuaciones|
> |☐|Grassmann verificado|$\dim U + \dim W - \dim(U \cap W)$|
> |☐|Suma directa (si aplica)|Alguna de las 3 opciones|

---

## 📚 Resumen Ejecutivo

> [!summary]- 🎯 Lo Esencial del Capítulo
> 
> ### Idea Central
> 
> **La suma de subespacios $U + W$ combina ambos subespacios mediante todas las sumas posibles $\vec{u} + \vec{w}$. Es el subespacio más pequeño que contiene a ambos.**
> 
> ---
> 
> ### Definiciones Clave
> 
> |Concepto|Fórmula|Cuándo|
> |---|---|---|
> |**Suma**|$U + W = {\vec{u} + \vec{w}}$|Siempre|
> |**Suma directa**|$U \oplus W$|Si $U \cap W = {\vec{0}}$|
> |**Dimensión**|$\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$|Grassmann|
> 
> ---
> 
> ### Fórmula Más Importante
> 
> $$\boxed{\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)}$$
> 
> **Casos especiales:**
> 
> - Suma directa: $\dim(U \oplus W) = \dim(U) + \dim(W)$
> - Contención: Si $U \subseteq W$, entonces $U + W = W$
> 
> ---
> 
> ### Métodos de Cálculo
> 
> |Objetivo|Procedimiento|Complejidad|
> |---|---|---|
> |**Base de $U + W$**|Juntar bases → eliminar dependencias|$O(n^3)$|
> |**$\dim(U + W)$**|Contar vectores L.I.|$O(n^3)$|
> |**$U \cap W$**|Resolver $c_i\vec{u}_i = d_j\vec{w}_j$|$O(n^3)$|
> |**Suma directa?**|Verificar $U \cap W = {\vec{0}}$|$O(n^3)$|
> 
> ---
> 
> ### Aplicaciones Principales
> 
> 1. **Descomposición ortogonal:** $\mathbb{R}^n = U \oplus U^\perp$
> 2. **Proyecciones:** $\vec{v} = \text{proj}_U(\vec{v}) + \text{proj}_{U^\perp}(\vec{v})$
> 3. **Ecuaciones diferenciales:** Sol. general = homogénea + particular
> 4. **Matrices:** Toda matriz = simétrica + antisimétrica
> 5. **Teoría de códigos:** Espacio = código $\oplus$ dual
> 
> ---
> 
> ### Próximo Paso
> 
> **Complemento Ortogonal:** Caso especial de suma directa donde los subespacios son perpendiculares, con propiedades geométricas importantes.

---

## 🏷️ Tags

#algebra-lineal #suma-de-subespacios #suma-directa #interseccion #formula-de-grassmann #dimension #complemento #descomposicion #proyecciones #subespacios #espacios-vectoriales #base #independencia-lineal #span #ortogonalidad #complemento-ortogonal #ecuaciones-diferenciales #matrices #teoria-de-codigos #reticulo-modular #algebra-abstracta #metodos-numericos #aplicaciones #verificacion #calculo-dimensional #geometria-vectorial #visualizacion

---

## 📖 Referencias y Lecturas Adicionales

> [!quote]- 📚 Para Profundizar
> 
> ### Textos Clásicos:
> 
> - **Linear Algebra Done Right** - Sheldon Axler
>     - Capítulo 1: Espacios vectoriales
>     - Enfoque en suma directa y complementos
> - **Linear Algebra** - Hoffman & Kunze
>     - Capítulo 2: Vector spaces
>     - Tratamiento abstracto y riguroso
> - **Introduction to Linear Algebra** - Gilbert Strang
>     - Capítulo 3: Vector spaces and subspaces
>     - Perspectiva geométrica
> 
> ### Artículos y notas:
> 
> - **Grassmann's Law** en Wikipedia
> - **Modular Lattice** - teoría de orden
> - **Direct Sum** en nLab (categorías)

---


# 📘 Combinación Lineal

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Combinaciones Lineales?
> 
> Las combinaciones lineales son el **concepto central** del álgebra lineal. Permiten construir nuevos vectores a partir de vectores dados mediante suma y multiplicación escalar.
> 
> **Motivación:**
> 
> - Cualquier vector en un espacio puede expresarse como combinación de vectores base
> - Sistemas de ecuaciones lineales preguntan: "¿es $\vec{b}$ combinación lineal de las columnas de $A$?"
> - La independencia lineal se define en términos de combinaciones lineales
> 
> **Aplicaciones prácticas:**
> 
> - **Física:** Descomposición de fuerzas y velocidades
> - **Gráficos por computadora:** Interpolación, mezcla de colores
> - **Procesamiento de señales:** Superposición de ondas
> - **Economía:** Combinación de recursos, portafolios de inversión
> 
> **Idea clave:**
> 
> - Una combinación lineal es "sumar vectores con pesos"
> - Los coeficientes (escalares) determinan "cuánto" de cada vector
> - Todo el álgebra lineal se construye sobre este concepto simple pero poderoso

---

## 📐 Definición de Combinación Lineal

### 📋 Definición Formal

> [!example]- 🟢 Definición: Combinación Lineal
> 
> **Definición:** Sean $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k$ vectores en un espacio vectorial $V$ sobre un campo $\mathbb{F}$. Un vector $\vec{w} \in V$ es una **combinación lineal** de $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k$ si existen escalares $c_1, c_2, \ldots, c_k \in \mathbb{F}$ tales que:
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k$$
> 
> O en notación compacta:
> 
> $$\vec{w} = \sum_{i=1}^{k} c_i\vec{v}_i$$
> 
> ---
> 
> **Terminología:**
> 
> - Los escalares $c_1, c_2, \ldots, c_k$ se llaman **coeficientes** de la combinación lineal
> - Los vectores $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k$ son los **vectores base** de la combinación
> - Si $c_i = 0$ para todo $i$, se llama **combinación lineal trivial**
> 
> ---
> 
> **Notación alternativa:**
> 
> - "El vector $\vec{w}$ se expresa como combinación lineal de ${\vec{v}_1, \ldots, \vec{v}_k}$"
> - "El vector $\vec{w}$ está en el span de ${\vec{v}_1, \ldots, \vec{v}_k}$"
> - "$\vec{w} \in \text{span}{\vec{v}_1, \ldots, \vec{v}_k}$"

> [!note]- 🎯 Interpretación Geométrica
> 
> ### En $\mathbb{R}^2$
> 
> Una combinación lineal $c_1\vec{v}_1 + c_2\vec{v}_2$ representa:
> 
> ```
>       y
>       |
>       |    â€¢ w = c₁v₁ + c₂v₂
>       |   /|
>       |  / |
>       | /  | câ‚‚vâ‚‚
>       |/   |
>   ----â€¢----+---- x
>      /  câ‚vâ‚
>     /vâ‚
> ```
> 
> - **Paso 1:** Escalar $\vec{v}_1$ por $c_1$ → vector $c_1\vec{v}_1$
> - **Paso 2:** Escalar $\vec{v}_2$ por $c_2$ → vector $c_2\vec{v}_2$
> - **Paso 3:** Sumar ambos vectores → resultado $\vec{w}$
> 
> ---
> 
> ### Interpretación Física
> 
> **Como "receta" o "mezcla":**
> 
> - $c_1 = 2, c_2 = 3$: "toma 2 unidades de $\vec{v}_1$ y 3 de $\vec{v}_2$"
> - Los coeficientes son "pesos" o "proporciones"
> - El resultado es una "mezcla ponderada"
> 
> **Como desplazamiento:**
> 
> - Empiezas en el origen
> - Te mueves $c_1$ veces en la dirección $\vec{v}_1$
> - Luego te mueves $c_2$ veces en la dirección $\vec{v}_2$
> - Llegas a $\vec{w}$

---

## 📚 Ejemplos Básicos

### Ejemplo 1: Combinaciones Lineales en $\mathbb{R}^2$

> [!example]- 📍 Ejemplo 1: Vectores en el Plano
> 
> **Dados los vectores:**
> 
> $$\vec{v}_1 = \begin{pmatrix} 1 \ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \ 1 \end{pmatrix}$$
> 
> ---
> 
> **a) Expresar $\vec{w} = \begin{pmatrix} 3 \ 5 \end{pmatrix}$ como combinación lineal**
> 
> Buscamos $c_1, c_2$ tales que:
> 
> $$c_1\begin{pmatrix} 1 \ 0 \end{pmatrix} + c_2\begin{pmatrix} 0 \ 1 \end{pmatrix} = \begin{pmatrix} 3 \ 5 \end{pmatrix}$$
> 
> $$\begin{pmatrix} c_1 \ c_2 \end{pmatrix} = \begin{pmatrix} 3 \ 5 \end{pmatrix}$$
> 
> **Solución:** $c_1 = 3, c_2 = 5$
> 
> $$\boxed{\vec{w} = 3\vec{v}_1 + 5\vec{v}_2}$$
> 
> ---
> 
> **b) ¿Todo vector en $\mathbb{R}^2$ es combinación lineal de $\vec{v}_1, \vec{v}_2$?**
> 
> Sí, porque cualquier $\begin{pmatrix} a \ b \end{pmatrix} = a\begin{pmatrix} 1 \ 0 \end{pmatrix} + b\begin{pmatrix} 0 \ 1 \end{pmatrix}$
> 
> Por lo tanto: $\text{span}{\vec{v}_1, \vec{v}_2} = \mathbb{R}^2$
> 
> ---
> 
> **c) Diferentes combinaciones**
> 
> |Coeficientes|Combinación lineal|Resultado|
> |---|---|---|
> |$c_1=2, c_2=0$|$2\vec{v}_1 + 0\vec{v}_2$|$\begin{pmatrix} 2 \ 0 \end{pmatrix}$|
> |$c_1=0, c_2=3$|$0\vec{v}_1 + 3\vec{v}_2$|$\begin{pmatrix} 0 \ 3 \end{pmatrix}$|
> |$c_1=1, c_2=1$|$\vec{v}_1 + \vec{v}_2$|$\begin{pmatrix} 1 \ 1 \end{pmatrix}$|
> |$c_1=-1, c_2=2$|$-\vec{v}_1 + 2\vec{v}_2$|$\begin{pmatrix} -1 \ 2 \end{pmatrix}$|

### Ejemplo 2: Vectores Colineales

> [!example]- 📍 Ejemplo 2: Vectores en la Misma Dirección
> 
> **Dados:**
> 
> $$\vec{v}_1 = \begin{pmatrix} 1 \ 2 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 2 \ 4 \end{pmatrix}$$
> 
> **Observación:** $\vec{v}_2 = 2\vec{v}_1$ (son colineales)
> 
> ---
> 
> **a) Expresar $\vec{w} = \begin{pmatrix} 5 \ 10 \end{pmatrix}$ como combinación lineal**
> 
> **Método 1:** Usar solo $\vec{v}_1$: $$\vec{w} = 5\vec{v}_1 = 5\begin{pmatrix} 1 \ 2 \end{pmatrix} = \begin{pmatrix} 5 \ 10 \end{pmatrix}$$ ✓
> 
> **Método 2:** Usar solo $\vec{v}_2$: $$\vec{w} = \frac{5}{2}\vec{v}_2 = 2.5\begin{pmatrix} 2 \ 4 \end{pmatrix} = \begin{pmatrix} 5 \ 10 \end{pmatrix}$$ ✓
> 
> **Método 3:** Usar ambos: $$\vec{w} = 3\vec{v}_1 + 1\vec{v}_2 = 3\begin{pmatrix} 1 \ 2 \end{pmatrix} + \begin{pmatrix} 2 \ 4 \end{pmatrix} = \begin{pmatrix} 5 \ 10 \end{pmatrix}$$ ✓
> 
> **Conclusión:** La representación **NO es única** cuando los vectores son dependientes.
> 
> ---
> 
> **b) ¿Se puede expresar $\vec{u} = \begin{pmatrix} 1 \ 0 \end{pmatrix}$?**
> 
> Necesitamos: $$c_1\begin{pmatrix} 1 \ 2 \end{pmatrix} + c_2\begin{pmatrix} 2 \ 4 \end{pmatrix} = \begin{pmatrix} 1 \ 0 \end{pmatrix}$$
> 
> Sistema: $$\begin{cases} c_1 + 2c_2 = 1 \ 2c_1 + 4c_2 = 0 \end{cases}$$
> 
> De la segunda ecuación: $c_1 + 2c_2 = 0$
> 
> Pero la primera dice: $c_1 + 2c_2 = 1$
> 
> **Contradicción** ✗
> 
> $$\boxed{\text{NO se puede expresar como combinación lineal}}$$
> 
> **Razón:** $\text{span}{\vec{v}_1, \vec{v}_2}$ es solo una recta (la recta $y = 2x$)

### Ejemplo 3: Combinaciones Lineales en $\mathbb{R}^3$

> [!example]- 📍 Ejemplo 3: Vectores en el Espacio
> 
> **Dados:**
> 
> $$\vec{v}_1 = \begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 1 \ 1 \ 0 \end{pmatrix}$$
> 
> ---
> 
> **a) ¿Es $\vec{w} = \begin{pmatrix} 2 \ 3 \ 0 \end{pmatrix}$ combinación lineal?**
> 
> Buscamos $c_1, c_2, c_3$:
> 
> $$c_1\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix} + c_2\begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix} + c_3\begin{pmatrix} 1 \ 1 \ 0 \end{pmatrix} = \begin{pmatrix} 2 \ 3 \ 0 \end{pmatrix}$$
> 
> Sistema: $$\begin{cases} c_1 + c_3 = 2 \ c_2 + c_3 = 3 \ 0 = 0 \end{cases}$$
> 
> **Solución (infinitas):**
> 
> - $c_3 = t$ (parámetro libre)
> - $c_1 = 2 - t$
> - $c_2 = 3 - t$
> 
> **Ejemplo con $t = 0$:** $\vec{w} = 2\vec{v}_1 + 3\vec{v}_2$
> 
> **Ejemplo con $t = 1$:** $\vec{w} = 1\vec{v}_1 + 2\vec{v}_2 + 1\vec{v}_3$
> 
> $$\boxed{\text{SÍ, pero de infinitas formas (vectores dependientes)}}$$
> 
> ---
> 
> **b) ¿Es $\vec{u} = \begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix}$ combinación lineal?**
> 
> Sistema: $$\begin{cases} c_1 + c_3 = 0 \ c_2 + c_3 = 0 \ 0 = 1 \end{cases}$$
> 
> **Contradicción** en la tercera ecuación ✗
> 
> $$\boxed{\text{NO es combinación lineal}}$$
> 
> **Razón:** Los tres vectores están en el plano $xy$ (tienen $z = 0$), así que solo generan ese plano.

### Ejemplo 4: Polinomios

> [!example]- 📍 Ejemplo 4: Combinaciones de Polinomios
> 
> **En el espacio $P_2$ de polinomios de grado ≤ 2:**
> 
> $$p_1(x) = 1, \quad p_2(x) = x, \quad p_3(x) = x^2$$
> 
> ---
> 
> **a) Expresar $q(x) = 3 + 2x - 5x^2$ como combinación lineal**
> 
> $$q(x) = c_1 \cdot 1 + c_2 \cdot x + c_3 \cdot x^2$$
> 
> Comparando coeficientes: $$3 + 2x - 5x^2 = c_1 + c_2x + c_3x^2$$
> 
> **Solución:** $c_1 = 3, c_2 = 2, c_3 = -5$
> 
> $$\boxed{q(x) = 3p_1(x) + 2p_2(x) - 5p_3(x)}$$
> 
> ---
> 
> **b) ¿Todo polinomio en $P_2$ es combinación lineal?**
> 
> Sí, cualquier $p(x) = a_0 + a_1x + a_2x^2$ se escribe como:
> 
> $$p(x) = a_0 \cdot 1 + a_1 \cdot x + a_2 \cdot x^2$$
> 
> Por lo tanto: $\text{span}{1, x, x^2} = P_2$
> 
> **Conclusión:** ${1, x, x^2}$ genera todo $P_2$

### Ejemplo 5: Matrices

> [!example]- 📍 Ejemplo 5: Combinaciones de Matrices
> 
> **En $M_{2×2}(\mathbb{R})$, dados:**
> 
> $$A_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad A_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$
> 
> $$A_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad A_4 = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$
> 
> ---
> 
> **a) Expresar $B = \begin{pmatrix} 2 & 3 \ -1 & 5 \end{pmatrix}$ como combinación lineal**
> 
> $$c_1A_1 + c_2A_2 + c_3A_3 + c_4A_4 = B$$
> 
> $$c_1\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + c_2\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + c_3\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} + c_4\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ -1 & 5 \end{pmatrix}$$
> 
> $$\begin{pmatrix} c_1 & c_2 \\ c_3 & c_4 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ -1 & 5 \end{pmatrix}$$
> 
> **Solución:** $c_1 = 2, c_2 = 3, c_3 = -1, c_4 = 5$
> 
> $$\boxed{B = 2A_1 + 3A_2 - A_3 + 5A_4}$$
> 
> ---
> 
> **b) Observación**
> 
> ${A_1, A_2, A_3, A_4}$ genera todo $M_{2×2}(\mathbb{R})$ porque:
> 
> $$\begin{pmatrix} a & b \\ c & d \end{pmatrix} = aA_1 + bA_2 + cA_3 + dA_4$$
> 
> Estas matrices son la "base estándar" de $M_{2×2}$.

---

## 🔧 Propiedades de Combinaciones Lineales

### 🎯 Propiedades Fundamentales

> [!note]- 🟡 Teorema: Propiedades Básicas
> 
> Sean $\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k$ vectores en un espacio vectorial $V$.
> 
> ### Propiedad 1: El vector cero
> 
> El vector cero **siempre** es combinación lineal:
> 
> $$\vec{0} = 0\vec{v}_1 + 0\vec{v}_2 + \cdots + 0\vec{v}_k$$
> 
> **Nota:** Esta es la **combinación lineal trivial**.
> 
> ---
> 
> ### Propiedad 2: Cada vector es combinación de sí mismo
> 
> $$\vec{v}_i = 0\vec{v}_1 + \cdots + 1\vec{v}_i + \cdots + 0\vec{v}_k$$
> 
> ---
> 
> ### Propiedad 3: Cerradura bajo operaciones
> 
> Si $\vec{u}$ y $\vec{w}$ son combinaciones lineales de ${\vec{v}_1, \ldots, \vec{v}_k}$, entonces:
> 
> - **Suma:** $\vec{u} + \vec{w}$ también es combinación lineal
> - **Múltiplo escalar:** $c\vec{u}$ también es combinación lineal
> 
> **Demostración:**
> 
> Si $\vec{u} = \sum a_i\vec{v}_i$ y $\vec{w} = \sum b_i\vec{v}_i$, entonces:
> 
> $$\vec{u} + \vec{w} = \sum (a_i + b_i)\vec{v}_i$$
> 
> $$c\vec{u} = \sum (ca_i)\vec{v}_i$$
> 
> ---
> 
> ### Propiedad 4: Transitividad
> 
> Si cada $\vec{v}_i$ es combinación lineal de ${\vec{w}_1, \ldots, \vec{w}_m}$, entonces cualquier combinación lineal de ${\vec{v}_1, \ldots, \vec{v}_k}$ también es combinación lineal de ${\vec{w}_1, \ldots, \vec{w}_m}$.
> 
> **En símbolos:** $\text{span}{\vec{v}_1, \ldots, \vec{v}_k} \subseteq \text{span}{\vec{w}_1, \ldots, \vec{w}_m}$

> [!note]- 🟡 Teorema: Equivalencia con Span
> 
> **Teorema:** Un vector $\vec{w}$ es combinación lineal de ${\vec{v}_1, \ldots, \vec{v}_k}$ si y solo si:
> 
> $$\vec{w} \in \text{span}{\vec{v}_1, \ldots, \vec{v}_k}$$
> 
> **Esto establece la equivalencia:**
> 
> $$\text{"$\vec{w}$ es combinación lineal"} \iff \text{"$\vec{w}$ está en el span"}$$
> 
> ---
> 
> **Consecuencia práctica:**
> 
> Los términos "combinación lineal" y "estar en el span" son **intercambiables**:
> 
> - Pregunta: "¿Es $\vec{w}$ combinación lineal de $\vec{v}_1, \vec{v}_2$?"
> - Equivalente: "¿Está $\vec{w}$ en $\text{span}{\vec{v}_1, \vec{v}_2}$?"

---

## 🛠️ Métodos para Determinar Combinaciones Lineales

### 📋 Método General: Sistema de Ecuaciones

> [!tip]- ✅ Algoritmo: ¿Es $\vec{w}$ combinación lineal?
> 
> **Problema:** Dados $\vec{v}_1, \ldots, \vec{v}_k$ y $\vec{w}$, determinar si $\vec{w}$ es combinación lineal.
> 
> **Método:**
> 
> ### Paso 1: Plantear la ecuación
> 
> $$c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k = \vec{w}$$
> 
> ### Paso 2: Escribir como sistema
> 
> Si los vectores están en $\mathbb{R}^n$, esto da un sistema de $n$ ecuaciones con $k$ incógnitas.
> 
> ### Paso 3: Resolver el sistema
> 
> - **Si tiene solución:** $\vec{w}$ ES combinación lineal
>     - Los valores de $c_i$ son los coeficientes
> - **Si no tiene solución:** $\vec{w}$ NO es combinación lineal
> 
> ### Paso 4: Interpretar
> 
> - **Solución única:** Los vectores son linealmente independientes
> - **Infinitas soluciones:** Los vectores son linealmente dependientes
> - **Sin solución:** $\vec{w}$ no está en el span
> 
> ---
> 
> **Forma matricial:**
> 
> El sistema $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{w}$ se escribe como:
> 
> $$\begin{pmatrix} | & | & & | \ \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_k \ | & | & & | \end{pmatrix} \begin{pmatrix} c_1 \ c_2 \ \vdots \ c_k \end{pmatrix} = \vec{w}$$
> 
> O simplemente: $A\vec{c} = \vec{w}$ donde $A$ tiene columnas $\vec{v}_1, \ldots, \vec{v}_k$

### Ejemplos Detallados

> [!example]- 📍 Ejemplo 6: Método Sistemático en $\mathbb{R}^3$
> 
> **Pregunta:** ¿Es $\vec{w} = \begin{pmatrix} 5 \ 7 \ 3 \end{pmatrix}$ combinación lineal de:
> 
> $$\vec{v}_1 = \begin{pmatrix} 1 \ 2 \ 1 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 2 \ 1 \ 0 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} 1 \ 1 \ 1 \end{pmatrix}$$
> 
> ---
> 
> **Paso 1: Plantear ecuación**
> 
> $$c_1\begin{pmatrix} 1 \ 2 \ 1 \end{pmatrix} + c_2\begin{pmatrix} 2 \ 1 \ 0 \end{pmatrix} + c_3\begin{pmatrix} 1 \ 1 \ 1 \end{pmatrix} = \begin{pmatrix} 5 \ 7 \ 3 \end{pmatrix}$$
> 
> ---
> 
> **Paso 2: Sistema de ecuaciones**
> 
> $$\begin{cases} c_1 + 2c_2 + c_3 = 5 \ 2c_1 + c_2 + c_3 = 7 \ c_1 + 0c_2 + c_3 = 3 \end{cases}$$
> 
> ---
> 
> **Paso 3: Resolver (método de eliminación)**
> 
> Matriz aumentada:
> 
> $$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 5 \ 2 & 1 & 1 & 7 \ 1 & 0 & 1 & 3 \end{array}\right)$$
> 
> $R_2 - 2R_1$:
> 
> $$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 5 \ 0 & -3 & -1 & -3 \ 1 & 0 & 1 & 3 \end{array}\right)$$
> 
> $R_3 - R_1$:
> 
> $$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 5 \ 0 & -3 & -1 & -3 \ 0 & -2 & 0 & -2 \end{array}\right)$$
> 
> $R_3: -2 \to c_2 = 1$
> 
> Sustituyendo hacia atrás: $c_1 = 2, c_2 = 1, c_3 = 1$
> 
> ---
> 
> **Paso 4: Verificación**
> 
> $$2\begin{pmatrix} 1 \ 2 \ 1 \end{pmatrix} + 1\begin{pmatrix} 2 \ 1 \ 0 \end{pmatrix} + 1\begin{pmatrix} 1 \ 1 \ 1 \end{pmatrix} = \begin{pmatrix} 2+2+1 \ 4+1+1 \ 2+0+1 \end{pmatrix} = \begin{pmatrix} 5 \ 7 \ 3 \end{pmatrix}$$ ✓
> 
> $$\boxed{\vec{w} = 2\vec{v}_1 + \vec{v}_2 + \vec{v}_3}$$

> [!example]- 📍 Ejemplo 7: Caso sin Solución
> 
> **Pregunta:** ¿Es $\vec{w} = \begin{pmatrix} 1 \ 2 \ 3 \end{pmatrix}$ combinación lineal de:
> 
> $$\vec{v}_1 = \begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}$$
> 
> ---
**Paso 1: Plantear ecuación**
> $$c_1\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix} + c_2\begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix} = \begin{pmatrix} 1 \ 2 \ 3 \end{pmatrix}$$
> 
> ---
> 
> **Paso 2: Sistema de ecuaciones**
> 
> $$\begin{cases} c_1 = 1 \ c_2 = 2 \ 0 = 3 \end{cases}$$
> 
> ---
> 
> **Paso 3: Análisis**
> 
> La tercera ecuación es **contradictoria**: $0 = 3$ ✗
> 
> $$\boxed{\text{NO tiene solución → NO es combinación lineal}}$$
> 
> ---
> 
> **Interpretación geométrica:**
> 
> $\vec{v}_1$ y $\vec{v}_2$ solo generan el plano $xy$ (donde $z = 0$).
> 
> El vector $\vec{w}$ tiene $z = 3 \neq 0$, por lo que no está en ese plano.

> [!example]- 📍 Ejemplo 8: Infinitas Soluciones
> 
> **Pregunta:** ¿Es $\vec{w} = \begin{pmatrix} 3 \ 6 \end{pmatrix}$ combinación lineal de:
> 
> $$\vec{v}_1 = \begin{pmatrix} 1 \ 2 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 2 \ 4 \end{pmatrix}, \quad \vec{v}_3 = \begin{pmatrix} -1 \ -2 \end{pmatrix}$$
> 
> ---
> 
> **Observación:** Los tres vectores son colineales ($\vec{v}_2 = 2\vec{v}_1$, $\vec{v}_3 = -\vec{v}_1$)
> 
> ---
> 
> **Paso 1: Sistema**
> 
> $$\begin{cases} c_1 + 2c_2 - c_3 = 3 \ 2c_1 + 4c_2 - 2c_3 = 6 \end{cases}$$
> 
> ---
> 
> **Paso 2: Análisis**
> 
> La segunda ecuación es $2 \times$ la primera → **redundante**
> 
> Una ecuación, tres incógnitas → **infinitas soluciones**
> 
> ---
> 
> **Paso 3: Solución general**
> 
> De $c_1 + 2c_2 - c_3 = 3$, expresando $c_1$:
> 
> $$c_1 = 3 - 2c_2 + c_3$$
> 
> Con $c_2 = s$ y $c_3 = t$ (parámetros libres):
> 
> $$\boxed{c_1 = 3 - 2s + t, \quad c_2 = s, \quad c_3 = t}$$
> 
> ---
> 
> **Ejemplos específicos:**
> 
> |$s$|$t$|$c_1$|$c_2$|$c_3$|Combinación|
> |---|---|---|---|---|---|
> |0|0|3|0|0|$3\vec{v}_1$|
> |1|0|1|1|0|$\vec{v}_1 + \vec{v}_2$|
> |0|1|4|0|1|$4\vec{v}_1 + \vec{v}_3$|
> |1|1|2|1|1|$2\vec{v}_1 + \vec{v}_2 + \vec{v}_3$|
> 
> **Conclusión:** SÍ es combinación lineal, de **infinitas formas** (vectores dependientes).

---

## 🎯 Relación con Sistemas de Ecuaciones Lineales

### 📊 Interpretación Matricial

> [!note]- 🟣 Conexión: Combinaciones Lineales ↔ Sistemas Lineales
> 
> ### Teorema Fundamental
> 
> La pregunta "¿Es $\vec{b}$ combinación lineal de las columnas de $A$?" es equivalente a:
> 
> $$\text{"¿Tiene solución el sistema } A\vec{x} = \vec{b}\text{?"}$$
> 
> ---
> 
> ### Explicación Detallada
> 
> Sea $A = \begin{pmatrix} | & | & & | \ \vec{a}_1 & \vec{a}_2 & \cdots & \vec{a}_n \ | & | & & | \end{pmatrix}$
> 
> Entonces:
> 
> $$A\vec{x} = A\begin{pmatrix} x_1 \ x_2 \ \vdots \ x_n \end{pmatrix} = x_1\vec{a}_1 + x_2\vec{a}_2 + \cdots + x_n\vec{a}_n$$
> 
> Por lo tanto:
> 
> $$A\vec{x} = \vec{b} \iff \vec{b} = x_1\vec{a}_1 + x_2\vec{a}_2 + \cdots + x_n\vec{a}_n$$
> 
> ---
> 
> ### Consecuencias Importantes
> 
> 1. **Consistencia del sistema:** $A\vec{x} = \vec{b}$ es consistente ⟺ $\vec{b} \in \text{span}{\text{columnas de } A}$
>     
> 2. **Espacio columna:** $\text{Col}(A) = \text{span}{\vec{a}_1, \ldots, \vec{a}_n}$
>     
> 3. **Rango:** $\text{rango}(A) = \dim(\text{Col}(A))$ = dimensión del espacio generado por las columnas
>     

> [!example]- 📍 Ejemplo 9: Interpretación Matricial
> 
> **Sistema:** $A\vec{x} = \vec{b}$ donde
> 
> $$A = \begin{pmatrix} 1 & 2 & 1 \ 0 & 1 & -1 \ 2 & 3 & 0 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 5 \ 1 \ 8 \end{pmatrix}$$
> 
> ---
> 
> **Pregunta equivalente:** ¿Es $\vec{b}$ combinación lineal de las columnas de $A$?
> 
> $$\vec{b} = x_1\begin{pmatrix} 1 \ 0 \ 2 \end{pmatrix} + x_2\begin{pmatrix} 2 \ 1 \ 3 \end{pmatrix} + x_3\begin{pmatrix} 1 \ -1 \ 0 \end{pmatrix}$$
> 
> ---
> 
> **Solución del sistema:**
> 
> Matriz aumentada:
> 
> $$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 5 \ 0 & 1 & -1 & 1 \ 2 & 3 & 0 & 8 \end{array}\right)$$
> 
> Reduciendo (eliminación gaussiana):
> 
> $$\left(\begin{array}{ccc|c} 1 & 0 & 0 & 1 \ 0 & 1 & 0 & 2 \ 0 & 0 & 1 & 1 \end{array}\right)$$
> 
> **Solución:** $x_1 = 1, x_2 = 2, x_3 = 1$
> 
> ---
> 
> **Verificación:**
> 
> $$1\begin{pmatrix} 1 \ 0 \ 2 \end{pmatrix} + 2\begin{pmatrix} 2 \ 1 \ 3 \end{pmatrix} + 1\begin{pmatrix} 1 \ -1 \ 0 \end{pmatrix} = \begin{pmatrix} 1+4+1 \ 0+2-1 \ 2+6+0 \end{pmatrix} = \begin{pmatrix} 5 \ 1 \ 8 \end{pmatrix}$$ ✓
> 
> $$\boxed{\text{SÍ es combinación lineal}}$$

---

## 🌟 Aplicaciones de Combinaciones Lineales

### 🎨 Aplicación 1: Interpolación

> [!example]- 🖼️ Ejemplo: Interpolación de Colores
> 
> **Problema:** En gráficos por computadora, queremos mezclar colores.
> 
> **Modelo RGB:** Cada color es un vector en $\mathbb{R}^3$:
> 
> $$\text{Rojo} = \begin{pmatrix} 255 \ 0 \ 0 \end{pmatrix}, \quad \text{Verde} = \begin{pmatrix} 0 \ 255 \ 0 \end{pmatrix}, \quad \text{Azul} = \begin{pmatrix} 0 \ 0 \ 255 \end{pmatrix}$$
> 
> ---
> 
> **Mezcla:** Cualquier color es combinación lineal:
> 
> $$\text{Color} = c_R \cdot \text{Rojo} + c_G \cdot \text{Verde} + c_B \cdot \text{Azul}$$
> 
> donde $0 \leq c_R, c_G, c_B \leq 1$
> 
> ---
> 
> **Ejemplos:**
> 
> - **Amarillo:** $\begin{pmatrix} 255 \ 255 \ 0 \end{pmatrix} = 1 \cdot \text{Rojo} + 1 \cdot \text{Verde}$
>     
> - **Morado:** $\begin{pmatrix} 128 \ 0 \ 128 \end{pmatrix} = 0.5 \cdot \text{Rojo} + 0.5 \cdot \text{Azul}$
>     
> - **Gris:** $\begin{pmatrix} 128 \ 128 \ 128 \end{pmatrix} = 0.5 \cdot (\text{Rojo} + \text{Verde} + \text{Azul})$
>     

### ⚡ Aplicación 2: Fuerzas en Física

> [!example]- 🔧 Ejemplo: Descomposición de Fuerzas
> 
> **Problema:** Una fuerza $\vec{F}$ actúa sobre un objeto en un plano inclinado.
> 
> ```
>         â†' F (fuerza aplicada)
>        /|
>       / |
>      /  |
>     /   |
>    /θ   | Fâ‚™ (componente normal)
>   /_____|
>   Fₜ (componente tangencial)
> ```
> 
> ---
> 
> **Descomposición:** Expresar $\vec{F}$ como combinación lineal de:
> 
> - $\vec{n}$: vector normal al plano
> - $\vec{t}$: vector tangente al plano
> 
> $$\vec{F} = F_n \vec{n} + F_t \vec{t}$$
> 
> donde:
> 
> - $F_n = |\vec{F}| \cos\theta$ (componente normal)
> - $F_t = |\vec{F}| \sin\theta$ (componente tangencial)
> 
> ---
> 
> **Aplicación:** Esta descomposición permite calcular:
> 
> - Fricción (depende de $F_n$)
> - Aceleración del objeto (depende de $F_t$)

### 📊 Aplicación 3: Economía - Portafolios

> [!example]- 💰 Ejemplo: Inversión en Portafolios
> 
> **Problema:** Un inversionista tiene tres activos disponibles.
> 
> **Retornos históricos (vectores de rendimientos en 3 períodos):**
> 
> $$\vec{a}_1 = \begin{pmatrix} 0.05 \ 0.10 \ 0.08 \end{pmatrix}, \quad \vec{a}_2 = \begin{pmatrix} 0.03 \ 0.04 \ 0.06 \end{pmatrix}, \quad \vec{a}_3 = \begin{pmatrix} 0.15 \ 0.12 \ 0.20 \end{pmatrix}$$
> 
> ---
> 
> **Portafolio:** Combinación lineal con pesos $w_1, w_2, w_3$:
> 
> $$\vec{p} = w_1\vec{a}_1 + w_2\vec{a}_2 + w_3\vec{a}_3$$
> 
> donde $w_1 + w_2 + w_3 = 1$ (todo el capital) y $w_i \geq 0$
> 
> ---
> 
> **Ejemplo:** Si invertimos 50% en $a_1$, 30% en $a_2$, 20% en $a_3$:
> 
> $$\vec{p} = 0.5\begin{pmatrix} 0.05 \ 0.10 \ 0.08 \end{pmatrix} + 0.3\begin{pmatrix} 0.03 \ 0.04 \ 0.06 \end{pmatrix} + 0.2\begin{pmatrix} 0.15 \ 0.12 \ 0.20 \end{pmatrix}$$
> 
> $$= \begin{pmatrix} 0.025 + 0.009 + 0.030 \ 0.050 + 0.012 + 0.024 \ 0.040 + 0.018 + 0.040 \end{pmatrix} = \begin{pmatrix} 0.064 \ 0.086 \ 0.098 \end{pmatrix}$$
> 
> 

### 🎵 Aplicación 4: Procesamiento de Señales

> [!example]- 🎶 Ejemplo: Síntesis de Audio
> 
> **Problema:** Crear un tono musical complejo.
> 
> **Ondas base (armónicos):**
> 
> $$f_1(t) = \sin(2\pi \cdot 440t) \quad \text{(La fundamental, 440 Hz)}$$ $$f_2(t) = \sin(2\pi \cdot 880t) \quad \text{(Primera armónica)}$$ $$f_3(t) = \sin(2\pi \cdot 1320t) \quad \text{(Segunda armónica)}$$
> 
> ---
> 
> **Señal compuesta:** Combinación lineal
> 
> $$s(t) = a_1 f_1(t) + a_2 f_2(t) + a_3 f_3(t)$$
> 
> donde $a_i$ determinan la **amplitud** de cada armónico
> 
> ---
> 
> **Ejemplos:**
> 
> - **Tono puro:** $s(t) = f_1(t)$ (solo fundamental)
> - **Tono rico:** $s(t) = f_1(t) + 0.5f_2(t) + 0.3f_3(t)$ (con armónicos)
> 
> **Aplicación:** Esto es la base de la síntesis de audio digital.

### 🧬 Aplicación 5: Genética - Expresión de Genes

> [!example]- 🔬 Ejemplo: Perfiles de Expresión Génica
> 
> **Problema:** Analizar la expresión de genes en diferentes condiciones.
> 
> **Datos:** Cada muestra es un vector de niveles de expresión:
> 
> $$\vec{s}_1 = \begin{pmatrix} 2.3 \ 1.5 \ 0.8 \ 3.2 \end{pmatrix}, \quad \vec{s}_2 = \begin{pmatrix} 1.1 \ 2.9 \ 1.2 \ 0.5 \end{pmatrix}$$
> 
> (expresión de 4 genes en 2 muestras)
> 
> ---
> 
> **Modelo:** Expresar una nueva muestra como combinación:
> 
> $$\vec{s}_{\text{nueva}} = c_1\vec{s}_1 + c_2\vec{s}_2$$
> 
> Si los coeficientes son significativos, sugiere que la nueva muestra es una "mezcla" de los estados representados por $\vec{s}_1$ y $\vec{s}_2$.
> 
> ---
> 
> **Aplicación:** Clasificación de tejidos, identificación de subtipos de cáncer.

---

## 🔬 Casos Especiales y Teoremas

### 📊 Combinaciones Afines

> [!note]- 🟡 Definición: Combinación Afín
> 
> **Definición:** Una **combinación afín** es una combinación lineal donde los coeficientes suman 1:
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k$$
> 
> con $c_1 + c_2 + \cdots + c_k = 1$
> 
> ---
> 
> **Diferencia con combinación lineal:**
> 
> - **Lineal:** Cualquier coeficiente (suma no restringida)
> - **Afín:** Suma de coeficientes = 1
> 
> ---
> 
> **Interpretación geométrica:**
> 
> - Combinaciones afines de 2 vectores → **segmento** que los une
> - Combinaciones afines de 3 vectores → **triángulo** con esos vértices
> - Combinaciones afines generan **conjuntos convexos**
> 
> ---
> 
> **Ejemplo en $\mathbb{R}^2$:**
> 
> $$\vec{w} = t\vec{v}_1 + (1-t)\vec{v}_2, \quad 0 \leq t \leq 1$$
> 
> - $t = 0$: $\vec{w} = \vec{v}_2$
> - $t = 1$: $\vec{w} = \vec{v}_1$
> - $t = 0.5$: $\vec{w} = \frac{\vec{v}_1 + \vec{v}_2}{2}$ (punto medio)

### 🎯 Combinaciones Convexas

> [!note]- 🟡 Definición: Combinación Convexa
> 
> **Definición:** Una **combinación convexa** es una combinación afín con coeficientes no negativos:
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k$$
> 
> con $c_i \geq 0$ y $\sum c_i = 1$
> 
> ---
> 
> **Propiedades:**
> 
> - Generan la **envoltura convexa** (convex hull) de los vectores
> - Geométricamente: el "interior" del polígono/politopo con vértices en $\vec{v}_i$
> 
> ---
> 
> **Ejemplo:** En $\mathbb{R}^2$ con tres vectores:
> 
> ```
>       vâ‚‚
>        â€¢
>       /â– \
>      / â– â–  \
>     /  â– â– â–  \
>    â€¢â€"â€"â€"â€"â€"â€¢
>   vâ‚       v₃
> ```
> 
> Todas las combinaciones convexas llenan el triángulo sombreado.

### 📐 Teorema: Caracterización de Subespacios

> [!note]- 🟣 Teorema: Cerradura bajo Combinaciones Lineales
> 
> **Teorema:** Un subconjunto $W$ de un espacio vectorial $V$ es un subespacio si y solo si es **cerrado bajo combinaciones lineales**.
> 
> **Formalmente:** $W \leq V$ ⟺ Para todo $\vec{v}_1, \ldots, \vec{v}_k \in W$ y $c_1, \ldots, c_k \in \mathbb{F}$:
> 
> $$c_1\vec{v}_1 + \cdots + c_k\vec{v}_k \in W$$
> 
> ---
> 
> **Demostración:** (⟹)
> 
> Si $W$ es subespacio:
> 
> 1. Es cerrado bajo suma → $\vec{v}_1 + \vec{v}_2 \in W$
> 2. Es cerrado bajo multiplicación → $c\vec{v} \in W$
> 3. Por inducción → cualquier combinación lineal está en $W$
> 
> ---
> 
> **Consecuencia práctica:**
> 
> Para verificar que $W$ es subespacio, **basta** verificar que es cerrado bajo combinaciones lineales (en lugar de las 3 condiciones separadas).

---

## 🛠️ Técnicas de Cálculo Avanzadas

### 📊 Método de la Matriz Inversa

> [!tip]- ✅ Técnica: Usando Inversa (cuando existe)
> 
> **Situación:** Queremos expresar $\vec{w}$ como combinación de vectores **linealmente independientes** $\vec{v}_1, \ldots, \vec{v}_n$ en $\mathbb{R}^n$.
> 
> **Ventaja:** Si los vectores forman una base, la representación es única.
> 
> ---
> 
> **Método:**
> 
> ### Paso 1: Formar matriz
> 
> $$A = \begin{pmatrix} | & | & & | \ \vec{v}_1 & \vec{v}_2 & \cdots & \vec{v}_n \ | & | & & | \end{pmatrix}$$
> 
> ### Paso 2: Resolver
> 
> $$\vec{c} = A^{-1}\vec{w}$$
> 
> ### Paso 3: Los coeficientes son las entradas de $\vec{c}$
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n$$
> 
> ---
> 
> **Nota:** Este método solo funciona si $A$ es invertible (vectores linealmente independientes).

> [!example]- 📍 Ejemplo 10: Usando Inversa
> 
> **Expresar $\vec{w} = \begin{pmatrix} 7 \ 11 \end{pmatrix}$ como combinación de:**
> 
> $$\vec{v}_1 = \begin{pmatrix} 1 \ 2 \end{pmatrix}, \quad \vec{v}_2 = \begin{pmatrix} 3 \ 4 \end{pmatrix}$$
> 
> ---
> 
> **Paso 1: Matriz**
> 
> $$A = \begin{pmatrix} 1 & 3 \ 2 & 4 \end{pmatrix}$$
> 
> ---
> 
> **Paso 2: Calcular inversa**
> 
> $$\det(A) = 1 \cdot 4 - 3 \cdot 2 = -2$$
> 
> $$A^{-1} = \frac{1}{-2}\begin{pmatrix} 4 & -3 \ -2 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1.5 \ 1 & -0.5 \end{pmatrix}$$
> 
> ---
> 
> **Paso 3: Calcular coeficientes**
> 
> $$\vec{c} = A^{-1}\vec{w} = \begin{pmatrix} -2 & 1.5 \ 1 & -0.5 \end{pmatrix}\begin{pmatrix} 7 \ 11 \end{pmatrix} = \begin{pmatrix} -14 + 16.5 \ 7 - 5.5 \end{pmatrix} = \begin{pmatrix} 2.5 \ 1.5 \end{pmatrix}$$
> 
> ---
> 
> **Respuesta:**
> 
> $$\boxed{\vec{w} = 2.5\vec{v}_1 + 1.5\vec{v}_2}$$
> 
> **Verificación:**
> 
> $$2.5\begin{pmatrix} 1 \ 2 \end{pmatrix} + 1.5\begin{pmatrix} 3 \ 4 \end{pmatrix} = \begin{pmatrix} 2.5 + 4.5 \ 5 + 6 \end{pmatrix} = \begin{pmatrix} 7 \ 11 \end{pmatrix}$$ ✓

### 🔄 Cambio de Base

> [!note]- 🟣 Concepto: Cambio de Base
> 
> **Idea:** El mismo vector puede tener diferentes representaciones en diferentes bases.
> 
> **Configuración:**
> 
> - Base estándar $\mathcal{E} = {\vec{e}_1, \ldots, \vec{e}_n}$
> - Base alternativa $\mathcal{B} = {\vec{b}_1, \ldots, \vec{b}_n}$
> 
> ---
> 
> **Vector en base estándar:**
> 
> $$\vec{v} = v_1\vec{e}_1 + \cdots + v_n\vec{e}_n$$
> 
> Coordenadas: $[\vec{v}]_\mathcal{E} = \begin{pmatrix} v_1 \ \vdots \ v_n \end{pmatrix}$
> 
> ---
> 
> **Mismo vector en base $\mathcal{B}$:**
> 
> $$\vec{v} = c_1\vec{b}_1 + \cdots + c_n\vec{b}_n$$
> 
> Coordenadas: $[\vec{v}]_\mathcal{B} = \begin{pmatrix} c_1 \ \vdots \ c_n \end{pmatrix}$
> 
> ---
> 
> **Matriz de cambio de base:** $P_{\mathcal{B}}$ tal que:
> 
> $$[\vec{v}]_\mathcal{E} = P_{\mathcal{B}} [\vec{v}]_\mathcal{B}$$
> 
> donde $P_{\mathcal{B}}$ tiene como columnas los vectores de $\mathcal{B}$ expresados en $\mathcal{E}$.
> 
> ---
> 
> **Para convertir:** $[\vec{v}]_\mathcal{B} = P_{\mathcal{B}}^{-1} [\vec{v}]_\mathcal{E}$

---

## 📋 Tabla de Referencia Rápida

> [!note]- 📊 Resumen de Conceptos Clave
> 
> |Concepto|Definición|Condición|Ejemplo|
> |---|---|---|---|
> |**Combinación lineal**|$\sum c_i\vec{v}_i$|Cualquier $c_i$|$2\vec{v}_1 - 3\vec{v}_2$|
> |**Combinación trivial**|$\sum c_i\vec{v}_i$|Todos $c_i = 0$|$0\vec{v}_1 + 0\vec{v}_2$|
> |**Combinación afín**|$\sum c_i\vec{v}_i$|$\sum c_i = 1$|$0.6\vec{v}_1 + 0.4\vec{v}_2$|
> |**Combinación convexa**|$\sum c_i\vec{v}_i$|$c_i \geq 0, \sum c_i = 1$|$0.3\vec{v}_1 + 0.7\vec{v}_2$|
> |**Span**|${\sum c_i\vec{v}_i : c_i \in \mathbb{F}}$|Todas las combinaciones|$\text{span}{\vec{v}_1, \vec{v}_2}$|
> 
> ---

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Determinar si es combinación lineal:**
> 
> a) ¿Es $\begin{pmatrix} 5 \ 7 \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 2 \end{pmatrix}$ y $\begin{pmatrix} 2 \ 3 \end{pmatrix}$?
> 
> b) ¿Es $\begin{pmatrix} 1 \ 2 \ 3 \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}$ y $\begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}$?
> 
> c) ¿Es $\begin{pmatrix} 4 \ 8 \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 2 \end{pmatrix}$ y $\begin{pmatrix} 2 \ 4 \end{pmatrix}$?
> 
> ---
> 
> **2. Encontrar coeficientes:**
> 
> a) Expresar $\begin{pmatrix} 6 \ 9 \end{pmatrix}$ como $c_1\begin{pmatrix} 2 \ 3 \end{pmatrix} + c_2\begin{pmatrix} 0 \ 1 \end{pmatrix}$
> 
> b) Expresar $3 + 2x - x^2$ como combinación de $1, x, x^2$
> 
> c) Expresar $\begin{pmatrix} 1 & 2 \ 3 & 4 \end{pmatrix}$ como combinación de $\begin{pmatrix} 1 & 0 \ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \ 0 & 1 \end{pmatrix}$
> 
> ---
> 
> **3. Verificar afirmaciones:**
> 
> a) ¿Todo vector en $\mathbb{R}^2$ es combinación de $\begin{pmatrix} 1 \ 0 \end{pmatrix}$ y $\begin{pmatrix} 0 \ 1 \end{pmatrix}$?
> 
> b) ¿Todo vector en $\mathbb{R}^3$ es combinación de $\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}$ y $\begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}$?
> 
> c) ¿El vector cero es siempre combinación lineal de cualquier conjunto de vectores?

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Sistemas con parámetros:**
> 
> a) ¿Para qué valores de $k$ es $\begin{pmatrix} k \ 2k \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 2 \end{pmatrix}$ y $\begin{pmatrix} 2 \ 3 \end{pmatrix}$?
> 
> b) ¿Para qué valor de $a$ es $\begin{pmatrix} 1 \ 2 \ a \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 1 \ 1 \end{pmatrix}$ y $\begin{pmatrix} 1 \ 0 \ -1 \end{pmatrix}$?
> 
> ---
> 
> **5. Múltiples representaciones:**
> 
> a) Dados $\vec{v}_1 = \begin{pmatrix} 1 \ 1 \end{pmatrix}, \vec{v}_2 = \begin{pmatrix} 1 \ 2 \end{pmatrix}, \vec{v}_3 = \begin{pmatrix} 2 \ 3 \end{pmatrix}$, encuentra DOS formas diferentes de expresar $\begin{pmatrix} 4 \ 5 \end{pmatrix}$ como combinación lineal.
> 
> b) ¿Por qué existen múltiples representaciones?
> 
> ---
> 
> **6. Interpretación geométrica:**
> 
> a) Si $\vec{v}_1$ y $\vec{v}_2$ son vectores no colineales en $\mathbb{R}^2$, describe geométricamente $\text{span}{\vec{v}_1, \vec{v}_2}$
> 
> b) Si $\vec{v}_1$ y $\vec{v}_2$ son colineales, describe $\text{span}{\vec{v}_1, \vec{v}_2}$
> 
> c) Describe $\text{span}{\vec{v}}$ para un vector no nulo $\vec{v}$ en $\mathbb{R}^3$
> 
> ---
> 
> **7. Polinomios:**
> 
> a) ¿Es $p(x) = x^2 + 2x + 1$ combinación de $q(x) = x^2 + 1$ y $r(x) = x$?
> 
> b) ¿Qué polinomios en $P_3$ se pueden expresar como combinación de $x$ y $x^3$?
> 
> ---
> 
> **8. Matrices:**
> 
> a) ¿Es $\begin{pmatrix} 1 & 2 \ 2 & 4 \end{pmatrix}$ combinación de matrices simétricas $\begin{pmatrix} 1 & 0 \ 0 & 0 \end{pmatrix}$ y $\begin{pmatrix} 0 & 1 \ 1 & 0 \end{pmatrix}$?
> 
> b) Encuentra todas las matrices $2 \times 2$ que son combinación de $\begin{pmatrix} 1 & 0 \ 0 & -1 \end{pmatrix}$ y $\begin{pmatrix} 0 & 1 \ 1 & 0 \end{pmatrix}$

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **9. Problemas teóricos:**
> 
> a) Demuestra que si $\vec{w}$ es combinación de ${\vec{v}_1, \ldots, \vec{v}_k}$ y cada $\vec{v}_i$ es combinación de ${\vec{u}_1, \ldots, \vec{u}_m}$, entonces $\vec{w}$ es combinación de ${\vec{u}_1, \ldots, \vec{u}_m}$
> 
> b) Demuestra que $\text{span}{\vec{v}_1, \ldots, \vec{v}_k}$ es el subespacio más pequeño que contiene a $\vec{v}_1, \ldots, \vec{v}_k$
> 
> c) Si $W_1 = \text{span}{S_1}$ y $W_2 = \text{span}{S_2}$, demuestra que $W_1 + W_2 = \text{span}(S_1 \cup S_2)$
> 
> ---
> 
> **10. Aplicaciones:**
> 
> a) **Física:** Una fuerza $\vec{F} = \begin{pmatrix} 10 \ 5 \ 3 \end{pmatrix}$ N actúa sobre un objeto. Expresa $\vec{F}$ como combinación de fuerzas unitarias en direcciones $x$, $y$, $z$.
> 
> b) **Economía:** Tres productos tienen vectores de costo $\vec{c}_1 = \begin{pmatrix} 10 \ 5 \ 2 \end{pmatrix}$, $\vec{c}_2 = \begin{pmatrix} 8 \ 6 \ 3 \end{pmatrix}$, $\vec{c}_3 = \begin{pmatrix} 12 \ 4 \ 1 \end{pmatrix}$ (materiales, labor, transporte). Si el presupuesto es $\begin{pmatrix} 100 \ 50 \ 20 \end{pmatrix}$, ¿qué combinación de productos se puede comprar?
> 
> ---
> 
> **11. Combinaciones especiales:**
> 
> a) Encuentra todas las combinaciones **convexas** de $\begin{pmatrix} 0 \ 0 \end{pmatrix}$ y $\begin{pmatrix} 1 \ 1 \end{pmatrix}$. Describe geométricamente.
> 
> b) ¿Qué forma geométrica generan las combinaciones convexas de tres vectores $\vec{v}_1, \vec{v}_2, \vec{v}_3$ en $\mathbb{R}^2$?
> 
> ---
> 
> **12. Cambio de base:**
> 
> a) Dado $\vec{v} = \begin{pmatrix} 3 \ 4 \end{pmatrix}$ en base estándar, encuentra sus coordenadas en la base $\mathcal{B} = \left{\begin{pmatrix} 1 \ 1 \end{pmatrix}, \begin{pmatrix} 1 \ -1 \end{pmatrix}\right}$
> 
> b) Si $[\vec{v}]_\mathcal{B} = \begin{pmatrix} 2 \ 3 \end{pmatrix}$ en la base del inciso anterior, encuentra $[\vec{v}]_\mathcal{E}$ (coordenadas estándar)
> 
> ---
> 
> **13. Problema de optimización:**
> 
> Encuentra la combinación convexa de $\vec{v}_1 = \begin{pmatrix} 1 \ 0 \end{pmatrix}$ y $\vec{v}_2 = \begin{pmatrix} 0 \ 1 \end{pmatrix}$ que está más cerca de $\vec{w} = \begin{pmatrix} 0.6 \ 0.7 \end{pmatrix}$.

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** ¿Es $\begin{pmatrix} 5 \ 7 \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 2 \end{pmatrix}$ y $\begin{pmatrix} 2 \ 3 \end{pmatrix}$?
> 
> Sistema: $$\begin{cases} c_1 + 2c_2 = 5 \ 2c_1 + 3c_2 = 7 \end{cases}$$
> 
> Solución: $c_1 = -1, c_2 = 3$
> 
> $$\boxed{\text{SÍ: } \begin{pmatrix} 5 \ 7 \end{pmatrix} = -\begin{pmatrix} 1 \ 2 \end{pmatrix} + 3\begin{pmatrix} 2 \ 3 \end{pmatrix}}$$
> 
> ---
> 
> **1b)** ¿Es $\begin{pmatrix} 1 \ 2 \ 3 \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 0 \ 0 \end{pmatrix}$ y $\begin{pmatrix} 0 \ 1 \ 0 \end{pmatrix}$?
> 
> Sistema: $$\begin{cases} c_1 = 1 \ c_2 = 2 \ 0 = 3 \end{cases}$$
> 
> Contradicción en la tercera ecuación ✗
> 
> $$\boxed{\text{NO es combinación lineal}}$$
> 
> ---
> 
> **2a)** Expresar $\begin{pmatrix} 6 \ 9 \end{pmatrix}$
> 
> $$c_1\begin{pmatrix} 2 \ 3 \end{pmatrix} + c_2\begin{pmatrix} 0 \ 1 \end{pmatrix} = \begin{pmatrix} 6 \ 9 \end{pmatrix}$$
> 
> Sistema: $$\begin{cases} 2c_1 = 6 \ 3c_1 + c_2 = 9 \end{cases}$$
> 
> De la primera: $c_1 = 3$
> 
> Sustituyendo: $c_2 = 9 - 9 = 0$
> 
> $$\boxed{\begin{pmatrix} 6 \ 9 \end{pmatrix} = 3\begin{pmatrix} 2 \ 3 \end{pmatrix} + 0\begin{pmatrix} 0 \ 1 \end{pmatrix}}$$
> 
> ---
> 
> **3a)** ¿Todo vector en $\mathbb{R}^2$ es combinación de $\begin{pmatrix} 1 \ 0 \end{pmatrix}$ y $\begin{pmatrix} 0 \ 1 \end{pmatrix}$?
> 
> Sí, porque cualquier $\begin{pmatrix} a \ b \end{pmatrix} = a\begin{pmatrix} 1 \ 0 \end{pmatrix} + b\begin{pmatrix} 0 \ 1 \end{pmatrix}$
> 
> $$\boxed{\text{SÍ, estos vectores generan todo } \mathbb{R}^2}$$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** ¿Para qué $k$ es $\begin{pmatrix} k \ 2k \end{pmatrix}$ combinación de $\begin{pmatrix} 1 \ 2 \end{pmatrix}$ y $\begin{pmatrix} 2 \ 3 \end{pmatrix}$?
> 
> Sistema: $$\begin{cases} c_1 + 2c_2 = k \ 2c_1 + 3c_2 = 2k \end{cases}$$
> 
> De la segunda: $2c_1 + 3c_2 = 2k$
> 
> Multiplicando la primera por 2: $2c_1 + 4c_2 = 2k$
> 
> Restando: $c_2 = 0$, entonces $c_1 = k$
> 
> $$\boxed{\text{Para TODO } k \in \mathbb{R}: \begin{pmatrix} k \ 2k \end{pmatrix} = k\begin{pmatrix} 1 \ 2 \end{pmatrix}}$$
> 
> **Nota:** El vector $\begin{pmatrix} k \ 2k \end{pmatrix}$ es siempre colineal con $\begin{pmatrix} 1 \ 2 \end{pmatrix}$.
> 
> ---
> 
> **6a)** Geometría del span
> 
> Si $\vec{v}_1$ y $\vec{v}_2$ no son colineales en $\mathbb{R}^2$:
> 
> $$\boxed{\text{span}{\vec{v}_1, \vec{v}_2} = \mathbb{R}^2 \text{ (todo el plano)}}$$
> 
> ---
> 
> **6b)** Si son colineales ($\vec{v}_2 = k\vec{v}_1$):
> 
> $$\boxed{\text{span}{\vec{v}_1, \vec{v}_2} = \text{span}{\vec{v}_1} \text{ (una recta)}}$$
> 
> ---
> 
> **7a)** Polinomios
> 
> ¿Es $p(x) = x^2 + 2x + 1$ combinación de $q(x) = x^2 + 1$ y $r(x) = x$?
> 
> $$c_1(x^2 + 1) + c_2 x = x^2 + 2x + 1$$
> 
> $$c_1x^2 + c_2x + c_1 = x^2 + 2x + 1$$
> 
> Comparando coeficientes:
> 
> - $x^2$: $c_1 = 1$
> - $x$: $c_2 = 2$
> - Constante: $c_1 = 1$ ✓
> 
> $$\boxed{\text{SÍ: } p(x) = 1 \cdot q(x) + 2 \cdot r(x)}$$

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **9a)** Demostración de transitividad
> 
> **Dado:**
> 
> - $\vec{w} = \sum a_i\vec{v}_i$
> - Cada $\vec{v}_i = \sum b_{ij}\vec{u}_j$
> 
> **Demostrar:** $\vec{w}$ es combinación de ${\vec{u}_1, \ldots, \vec{u}_m}$
> 
> **Demostración:**
> 
> $$\vec{w} = \sum_i a_i\vec{v}_i = \sum_i a_i\left(\sum_j b_{ij}\vec{u}_j\right)$$
> 
> $$= \sum_i \sum_j a_ib_{ij}\vec{u}_j = \sum_j \left(\sum_i a_ib_{ij}\right)\vec{u}_j$$
> 
> Con $c_j = \sum_i a_ib_{ij}$:
> 
> $$\vec{w} = \sum_j c_j\vec{u}_j$$ ✓
> 
> ---
> 
> **11a)** Combinaciones convexas
> 
> $$\vec{w} = t\begin{pmatrix} 0 \ 0 \end{pmatrix} + (1-t)\begin{pmatrix} 1 \ 1 \end{pmatrix} = (1-t)\begin{pmatrix} 1 \ 1 \end{pmatrix}$$
> 
> con $0 \leq t \leq 1$
> 
> **Resultado:** Todos los puntos del segmento de $(0,0)$ a $(1,1)$
> 
> $$\boxed{\left{\begin{pmatrix} s \ s \end{pmatrix} : 0 \leq s \leq 1\right}}$$
> 
> ```
>     y
>     |
>   1 â€¢ (1,1)
>     |/
>     â€¢ (0,0)
>     +---- x
>     0   1
> 
> Segmento desde origen hasta (1,1)
> ```
> 
> ---
> 
> **12a)** Cambio de base
> 
> **Dado:** $\vec{v} = \begin{pmatrix} 3 \ 4 \end{pmatrix}$ en base estándar
> 
> **Base:** $\mathcal{B} = \left{\begin{pmatrix} 1 \ 1 \end{pmatrix}, \begin{pmatrix} 1 \ -1 \end{pmatrix}\right}$
> 
> Buscamos $c_1, c_2$ tales que:
> 
> $$c_1\begin{pmatrix} 1 \ 1 \end{pmatrix} + c_2\begin{pmatrix} 1 \ -1 \end{pmatrix} = \begin{pmatrix} 3 \ 4 \end{pmatrix}$$
> 
> Sistema: $$\begin{cases} c_1 + c_2 = 3 \ c_1 - c_2 = 4 \end{cases}$$
> 
> Sumando: $2c_1 = 7 \Rightarrow c_1 = 3.5$
> 
> Restando: $2c_2 = -1 \Rightarrow c_2 = -0.5$
> 
> $$\boxed{[\vec{v}]_\mathcal{B} = \begin{pmatrix} 3.5 \ -0.5 \end{pmatrix}}$$

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Combinaciones Lineales
> 
> ✅ **Definición fundamental:**
> 
> - $\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k$
> - Los $c_i$ son escalares (coeficientes)
> - Es la operación más básica del álgebra lineal
> 
> ✅ **Equivalencia con span:**
> 
> - $\vec{w}$ es combinación lineal ⟺ $\vec{w} \in \text{span}{\vec{v}_1, \ldots, \vec{v}_k}$
> - Son dos formas de decir lo mismo
> 
> ✅ **Conexión con sistemas:**
> 
> - Pregunta: "¿Es $\vec{w}$ combinación lineal?"
> - Método: Resolver sistema $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{w}$
> - Tiene solución ⟺ Es combinación lineal
> 
> ---
> 
> ### Sobre Unicidad
> 
> ✅ **Representación única:**
> 
> - Si vectores son **linealmente independientes** → representación única
> - Si vectores son **linealmente dependientes** → infinitas representaciones (o ninguna)
> 
> ✅ **Vector cero:**
> 
> - Siempre es combinación lineal: $\vec{0} = 0\vec{v}_1 + \cdots + 0\vec{v}_k$
> - Esta es la combinación trivial
> 
> ---
> 
> ### Casos Especiales
> 
> ✅ **Combinación afín:**
> 
> - Coeficientes suman 1: $\sum c_i = 1$
> - Genera segmentos, triángulos, etc.
> 
> ✅ **Combinación convexa:**
> 
> - Coeficientes ≥ 0 y suman 1
> - Genera envolturas convexas
> 
> ---
> 
> ### Aplicaciones
> 
> 📊 **Sistemas de ecuaciones:** $A\vec{x} = \vec{b}$ pregunta si $\vec{b}$ es combinación de columnas
> 
> 🎨 **Gráficos:** Mezcla de colores, interpolación
> 
> ⚡ **Física:** Descomposición de fuerzas, superposición
> 
> 💰 **Economía:** Portafolios, combinación de recursos

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema es prerequisito para:**
> 
> - [[09 - Independencia Lineal]] - Cuando la única combinación que da $\vec{0}$ es la trivial
> - [[10 - Bases y Dimensión]] - Conjuntos que generan mediante combinaciones lineales
> - [[11 - Transformaciones Lineales]] - Preservan combinaciones lineales
> - [[12 - Espacios Columna y Nulo]] - Definidos por combinaciones de columnas
> - [[13 - Rango y Nulidad]] - Dimensiones de espacios generados
> - [[14 - Sistemas de Ecuaciones]] - Interpretación como combinaciones
> 
> **Conceptos relacionados:**
> 
> - **Span** - Conjunto de todas las combinaciones lineales
> - **Subespacios** - Cerrados bajo combinaciones lineales
> - **Dependencia Lineal** - Cuando un vector es combinación de otros
> - **Bases** - Generan todo el espacio mediante combinaciones lineales
> - **Coordenadas** - Coeficientes de combinación lineal en una base
> 
> **Siguiente tema recomendado:** [[09 - Independencia Lineal y Dependencia]]

---

## 📝 Notas Finales

> [!note]- 🎯 Reflexiones sobre Combinaciones Lineales
> 
> ### Importancia Conceptual
> 
> Las combinaciones lineales son el **corazón del álgebra lineal**:
> 
> - **Más fundamental que matrices:** Las matrices son solo herramientas para trabajar con combinaciones lineales
> - **Unifica conceptos:** Span, independencia, bases, dimensión... todo se define en términos de combinaciones lineales
> - **Interpretación dual:** Algebraica (suma ponderada) y geométrica (construcción de vectores)
> 
> ---
> 
> ### Perspectiva Práctica
> 
> **Pregunta central del álgebra lineal:**
> 
> > "¿Puedo construir este vector usando estos otros vectores?"
> 
> Esta pregunta aparece en:
> 
> - Resolver sistemas de ecuaciones
> - Determinar si vectores son independientes
> - Encontrar bases
> - Calcular dimensiones
> - Analizar transformaciones
> 
> ---
> 
> ### Intuición Geométrica
> 
> **Pensar en combinaciones lineales como:**
> 
> - **Receta:** "mezcla" de ingredientes (vectores) con cantidades (coeficientes)
> - **Navegación:** partir del origen, moverse múltiplos de cada vector
> - **Construcción:** ensamblar un vector target usando bloques (vectores base)
> 
> **En $\mathbb{R}^2$ y $\mathbb{R}^3$:**
> 
> - 1 vector → recta
> - 2 vectores independientes → plano (en $\mathbb{R}^3$) o plano completo (en $\mathbb{R}^2$)
> - 3 vectores independientes → todo $\mathbb{R}^3$
> 
> ---
> 
> ### Conexión con Otras Áreas
> 
> **Combinaciones lineales aparecen en:**
> 
> - **Análisis de Fourier:** Funciones como combinaciones de senos/cosenos
> - **Mecánica Cuántica:** Estados como combinaciones de estados base
> - **Estadística:** Regresión lineal como combinación de variables
> - **Redes Neuronales:** Capas lineales son combinaciones ponderadas
> - **Optimización:** Regiones factibles como combinaciones convexas
> 
> ---
> 
> ### Para Profundizar
> 
> **Generalizaciones:**
> 
> - **Combinaciones infinitas:** Series de Fourier, espacios de Hilbert
> - **Combinaciones no lineales:** Variedades, espacios no lineales
> - **Álgebra multilineal:** Tensores, productos exterior
> - **Geometría algebraica:** Variedades afines
> 
> **Estructuras relacionadas:**
> 
> - **Módulos:** Generalización sobre anillos
> - **Espacios afines:** Sin origen privilegiado
> - **Espacios convexos:** Solo combinaciones convexas
> - **Conos:** Solo coeficientes no negativos

---

## 🧮 Fórmulas y Algoritmos de Referencia

> [!note]- 📋 Algoritmo General: Determinar Combinación Lineal
> 
> **Input:** Vectores $\vec{v}_1, \ldots, \vec{v}_k$ y vector objetivo $\vec{w}$
> 
> **Output:** Coeficientes $c_1, \ldots, c_k$ o "no es combinación lineal"
> 
> ---
> 
> ### Algoritmo:
> 
> ```
> 1. Plantear ecuación: c₁v₁ + c₂v₂ + ⋯ + cₖvₖ = w
> 
> 2. Formar matriz aumentada: [v₁ v₂ ⋯ vₖ | w]
> 
> 3. Aplicar eliminación gaussiana
> 
> 4. Analizar forma escalonada reducida:
>    
>    SI última columna tiene pivote:
>        RETORNAR "No es combinación lineal"
>    
>    SI NO:
>        RETORNAR coeficientes de la solución
> 
> 1. SI hay variables libres:
> ```
>    RETORNAR "Infinitas representaciones (parámetros: ...)"
> ```
> 
> SI NO: RETORNAR "Representación única: c₁, c₂, ..., cₖ"
> 
> ```
> 
> ---
> 
> ### Complejidad:
> ```
> - **Tiempo:** $O(n^2k)$ donde $n$ = dimensión, $k$ = número de vectores
> - **Espacio:** $O(nk)$ para almacenar la matriz
> ```

---

## 💡 Trucos y Técnicas Adicionales

> [!tip]- 🎯 Estrategias Avanzadas
> 
> ### Truco 1: Reconocer Patrones Visuales
> 
> **En $\mathbb{R}^2$:**
> 
> - Si $\vec{w}$ está "alineado" con $\vec{v}_1$ → solo necesitas $\vec{v}_1$
> - Si $\vec{w}$ está en el plano generado → es combinación
> - Si $\vec{w}$ "sale" del plano → no es combinación
> 
> ```
>       y
>       |
>       | w₂ (fuera del plano)
>       |/
>       â€¢ w₁ (en el plano)
>      /|
>     / |
>    /  +---- x
>   Plano generado
> ```
> 
> ---
> 
> ### Truco 2: Usar Determinantes (solo para cuadradas)
> 
> Si tienes $n$ vectores en $\mathbb{R}^n$:
> 
> - Si $\det(A) \neq 0$ → los vectores generan todo $\mathbb{R}^n$
> - Si $\det(A) = 0$ → no generan todo el espacio
> 
> **Limitación:** Solo funciona para matrices cuadradas.
> 
> ---
> 
> ### Truco 3: Interpretación por Bloques
> 
> Para sistemas grandes, divide en bloques:
> 
> $$\vec{w} = \begin{pmatrix} \vec{w}_1 \ \vec{w}_2 \end{pmatrix}, \quad \vec{v}_i = \begin{pmatrix} \vec{v}_{i,1} \ \vec{v}_{i,2} \end{pmatrix}$$
> 
> Entonces:
> 
> $$c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{w}$$
> 
> se descompone en:
> 
> $$\begin{cases} c_1\vec{v}_{1,1} + \cdots + c_k\vec{v}_{k,1} = \vec{w}_1 \ c_1\vec{v}_{1,2} + \cdots + c_k\vec{v}_{k,2} = \vec{w}_2 \end{cases}$$
> 
> ---
> 
> ### Truco 4: Verificación Rápida con Producto Punto
> 
> Si conoces un vector $\vec{n}$ perpendicular a todos los $\vec{v}_i$:
> 
> $$\vec{n} \perp \vec{v}_i \text{ para todo } i$$
> 
> Entonces $\vec{w}$ es combinación lineal **solo si** $\vec{n} \perp \vec{w}$
> 
> **Razón:** $\vec{n} \cdot (c_1\vec{v}_1 + \cdots + c_k\vec{v}_k) = 0$
> 
> ---
> 
> ### Truco 5: Casos con Simetría
> 
> Si los vectores tienen simetría especial, explótala:
> 
> **Ejemplo:** Vectores $\vec{v}_1 = \begin{pmatrix} 1 \ 1 \end{pmatrix}, \vec{v}_2 = \begin{pmatrix} 1 \ -1 \end{pmatrix}$
> 
> Son ortogonales → cualquier vector se descompone fácilmente:
> 
> $$\vec{w} = \begin{pmatrix} a \ b \end{pmatrix} = \frac{a+b}{2}\begin{pmatrix} 1 \ 1 \end{pmatrix} + \frac{a-b}{2}\begin{pmatrix} 1 \ -1 \end{pmatrix}$$

---

## 🎨 Visualizaciones Interactivas (Conceptual)

> [!note]- 🖼️ Galería de Combinaciones Lineales
> 
> ### En $\mathbb{R}^2$: Dos Vectores Independientes
> 
> ```
>       y
>       |
>       |  â€¢ w = 2v₁ + 1.5v₂
>       | /|\
>       |/ | \1.5vâ‚‚
>       â€¢  |  \
>      /|  |   \
>     / |  +----â€¢ vâ‚‚
>    /  | /    /
>   /   |/    /
>  â€¢----â€¢----+---- x
>  vâ‚    2vâ‚
> 
> Construcción paso a paso:
> 1. Escala v₁ por 2
> 2. Escala v₂ por 1.5
> 3. Suma vectorialmente
> ```
> 
> ---
> 
> ### En $\mathbb{R}^2$: Vectores Colineales
> 
> ```
>       y
>       |
>       |  / vâ‚‚ = 2vâ‚
>       | /
>       |/
>       â€¢ vâ‚
>      /|
>     / |
>    /  +---- x
> 
> Todas las combinaciones están
> en la misma recta
> ```
> 
> ---
> 
> ### En $\mathbb{R}^3$: Tres Vectores Coplanares
> 
> ```
>         z
>         |
>         |  Plano generado
>         | /â•±â•±â•±
>         |/â•±â•±â•±
>   ------â€¢â•±â•±â•± y
>        /|â•±â•±
>       / |
>      x
> 
> Las combinaciones llenan un plano,
> no todo R³
> ```
> 
> ---
> 
> ### Combinaciones Convexas en $\mathbb{R}^2$
> 
> ```
>       vâ‚‚
>        â€¢
>       /â– â– \
>      / â– â– â–  \
>     /  â– â– â–  \
>    /   â– â– â–   \
>   â€¢â€"â€"â€"â–²â€"â€"â€"â€¢
>  vâ‚    w    v₃
> 
> Triángulo relleno = todas las
> combinaciones convexas de v₁, v₂, v₃
> ```

---

## 🔍 Problemas Conceptuales Profundos

> [!example]- 🧠 Preguntas para Reflexionar
> 
> **1. Paradoja dimensional:**
> 
> En $\mathbb{R}^3$, necesitas 3 vectores independientes para generar todo el espacio. Pero ¿por qué no 2 o 4?
> 
> **Respuesta:** La dimensión es una propiedad intrínseca del espacio. Es el número **mínimo** de vectores independientes necesarios.
> 
> ---
> 
> **2. ¿Puede un conjunto infinito generar un espacio finito-dimensional?**
> 
> Sí. Ejemplo: ${e_1, e_2, e_1+e_2, 2e_1, 3e_2, \ldots}$ genera $\mathbb{R}^2$ (dimensión 2).
> 
> **Lección:** Tamaño del conjunto ≠ dimensión del span.
> 
> ---
> 
> **3. ¿Todo vector es combinación lineal de sí mismo?**
> 
> Sí, trivialmente: $\vec{v} = 1 \cdot \vec{v}$
> 
> Por lo tanto: $\vec{v} \in \text{span}{\vec{v}}$ siempre.
> 
> ---
> 
> **4. Si $\vec{w}$ es combinación de ${\vec{v}_1, \vec{v}_2}$ y ${\vec{v}_1, \vec{v}_2}$ son combinaciones de ${\vec{u}_1, \vec{u}_2, \vec{u}_3}$, ¿$\vec{w}$ es combinación de ${\vec{u}_1, \vec{u}_2, \vec{u}_3}$?**
> 
> Sí, por la propiedad de transitividad (ver Ejercicio 9a).
> 
> **Consecuencia:** $\text{span}(S_1) \subseteq \text{span}(S_2)$ si cada vector de $S_1$ es combinación de vectores de $S_2$.
> 
> ---
> 
> **5. ¿Puede un vector ser "su propia combinación lineal" de manera no trivial?**
> 
> Sí, si el conjunto es linealmente dependiente:
> 
> Ejemplo: $\vec{v}_3 = \vec{v}_1 + \vec{v}_2$
> 
> Entonces: $\vec{v}_3 = 1\vec{v}_1 + 1\vec{v}_2 + 0\vec{v}_3$ ✓
> 
> También: $\vec{v}_3 = 0\vec{v}_1 + 0\vec{v}_2 + 1\vec{v}_3$ ✓
> 
> Múltiples representaciones.

---

## 📊 Tabla Comparativa: Tipos de Combinaciones

> [!note]- 📋 Comparación Completa
> 
> |Tipo|Restricción en $c_i$|Conjunto Generado|Geometría|Aplicación|
> |---|---|---|---|---|
> |**Lineal**|Ninguna|Subespacio|Plano/línea por origen|Álgebra lineal general|
> |**Afín**|$\sum c_i = 1$|Subespacio afín|Plano/línea (cualquier)|Geometría afín, interpolación|
> |**Convexa**|$c_i \geq 0, \sum c_i = 1$|Envoltura convexa|Polígono/politopo|Optimización, economía|
> |**Cónica**|$c_i \geq 0$|Cono|Región angular|Programación lineal|
> 
> ---
> 
> ### Relaciones de Inclusión
> 
> ```
> Convexas ⊆ Afines ⊆ Lineales
>     ∪
>  Cónicas
> ```
> 
> - Toda combinación convexa es afín
> - Toda combinación afín es lineal
> - Combinaciones cónicas y convexas se solapan parcialmente

---

## 🎯 Resumen Ejecutivo Final

> [!note]- 📌 Todo en Una Página
> 
> ### Definición Core
> 
> $$\vec{w} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_k\vec{v}_k$$
> 
> donde $c_i \in \mathbb{F}$ (escalares), $\vec{v}_i \in V$ (vectores)
> 
> ---
> 
> ### Equivalencias Clave
> 
> Las siguientes afirmaciones son **equivalentes**:
> 
> 1. $\vec{w}$ es combinación lineal de ${\vec{v}_1, \ldots, \vec{v}_k}$
> 2. $\vec{w} \in \text{span}{\vec{v}_1, \ldots, \vec{v}_k}$
> 3. El sistema $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{w}$ tiene solución
> 4. El sistema $A\vec{c} = \vec{w}$ es consistente (donde $A$ tiene columnas $\vec{v}_i$)
> 5. $\vec{w} \in \text{Col}(A)$ (espacio columna de $A$)
> 
> ---
> 
> ### Método de Solución
> 
> **Pregunta:** ¿Es $\vec{w}$ combinación de $\vec{v}_1, \ldots, \vec{v}_k$?
> 
> **Respuesta:**
> 
> 6. Plantea $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{w}$
> 7. Forma matriz aumentada $[A | \vec{w}]$
> 8. Reduce a forma escalonada
> 9. Verifica consistencia
> 
> ---
> 
> ### Casos Posibles
> 
> |Caso|Resultado|Interpretación|
> |---|---|---|
> |Solución única|Es combinación (única)|Vectores independientes|
> |Infinitas soluciones|Es combinación (múltiple)|Vectores dependientes|
> |Sin solución|NO es combinación|$\vec{w}$ fuera del span|
> 
> ---
> 
> ### Propiedades Fundamentales
> 
> ✅ $\vec{0}$ siempre es combinación (trivial)
> 
> ✅ Cada $\vec{v}_i$ es combinación de sí mismo
> 
> ✅ Suma/múltiplos de combinaciones son combinaciones
> 
> ✅ Transitividad: si A es comb. de B, y B es comb. de C → A es comb. de C
> 
> ---
> 
> ### Geometría
> 
> - **1 vector:** Recta por origen
> - **2 vectores independientes:** Plano por origen
> - **3 vectores independientes en $\mathbb{R}^3$:** Todo el espacio
> - **$k$ vectores en $\mathbb{R}^n$ con $k < n$:** Subespacio de dimensión ≤ $k$
> 
> ---
> 
> ### Aplicaciones Principales
> 
> 🔹 **Resolver sistemas de ecuaciones lineales**
> 
> 🔹 **Determinar si vectores generan un espacio**
> 
> 🔹 **Cambio de coordenadas entre bases**
> 
> 🔹 **Interpolación y aproximación**
> 
> 🔹 **Descomposición de señales/fuerzas**

---

## 🎓 Conexión con Temas Futuros

> [!quote]- 🔮 Vista Previa de Conceptos Avanzados
> 
> ### Independencia Lineal (Próximo Tema)
> 
> **Pregunta clave:** ¿Cuándo la única combinación lineal que da $\vec{0}$ es la trivial?
> 
> $$c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{0} \implies c_1 = \cdots = c_k = 0$$
> 
> **Conexión:** Independencia ⟺ Representación única como combinación lineal
> 
> ---
> 
> ### Bases
> 
> **Definición:** Conjunto que:
> 
> 1. Genera todo el espacio (mediante combinaciones lineales)
> 2. Es linealmente independiente
> 
> **Consecuencia:** Todo vector tiene representación **única** como combinación de vectores base.
> 
> ---
> 
> ### Transformaciones Lineales
> 
> **Propiedad fundamental:** $T$ es lineal si preserva combinaciones:
> 
> $$T(c_1\vec{v}_1 + c_2\vec{v}_2) = c_1T(\vec{v}_1) + c_2T(\vec{v}_2)$$
> 
> **Consecuencia:** Para conocer $T$ completamente, basta conocerla en una base.
> 
> ---
> 
> ### Espacios de Funciones
> 
> **Series de Fourier:** Cualquier función (bajo condiciones) es combinación lineal infinita de senos/cosenos:
> 
> $$f(x) = a_0 + \sum_{n=1}^{\infty} [a_n\cos(nx) + b_n\sin(nx)]$$
> 
> **Polinomios de Taylor:** Combinación lineal de potencias:
> 
> $$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$
> 
> ---
> 
> ### Descomposición de Matrices
> 
> **Diagonalización:** Expresar matriz como combinación de proyecciones:
> 
> $$A = \lambda_1 P_1 + \lambda_2 P_2 + \cdots + \lambda_k P_k$$
> 
> **SVD:** Descomposición en valores singulares
> 
> $$A = \sigma_1\vec{u}_1\vec{v}_1^T + \sigma_2\vec{u}_2\vec{v}_2^T + \cdots$$

---

## ✨ Reflexión Final

> [!quote]- 🌟 El Poder de la Linealidad
> 
> ### Por qué las Combinaciones Lineales son Tan Poderosas
> 
> **1. Simplicidad:**
> 
> - Solo dos operaciones: suma y multiplicación escalar
> - Fáciles de computar y entender
> 
> **2. Universalidad:**
> 
> - Aparecen en todas las áreas de matemáticas y ciencias
> - Modelo básico para sistemas complejos
> 
> **3. Composicionalidad:**
> 
> - Puedes construir objetos complejos de simples
> - Descomponer problemas difíciles en partes manejables
> 
> **4. Aproximación:**
> 
> - Muchos fenómenos no lineales son "casi lineales" localmente
> - Base para cálculo diferencial, análisis numérico
> 
> ---
> 
> ### La Esencia del Álgebra Lineal
> 
> > "El álgebra lineal es el estudio de qué se puede construir mediante combinaciones lineales, y cómo."
> 
> **Todo se reduce a esta pregunta:**
> 
> _"¿Puedo alcanzar este vector usando combinaciones de estos otros vectores?"_
> 
> - Si SÍ → el vector está en el span
> - Si NO → necesito más vectores, o dimensión mayor
> - Si SÍ de forma única → los vectores son independientes
> - Si SÍ de múltiples formas → hay redundancia (dependencia)
> 
> ---
> 
> ### Para el Estudiante
> 
> **Dominar combinaciones lineales es dominar álgebra lineal.**
> 
> - Practica visualizar geométricamente
> - Conecta con sistemas de ecuaciones
> - Reconoce el patrón en diferentes contextos
> - Aprecia su simplicidad y poder
> 
> Todo lo que sigue en álgebra lineal es elaboración de esta idea central.

---

**Fin del documento 08 – Combinación Lineal**

---

**Tags:** #algebra-lineal #combinacion-lineal #span #espacios-vectoriales #sistemas-lineales #independencia-lineal #generadores #algebra-abstracta #geometria-vectorial #bases
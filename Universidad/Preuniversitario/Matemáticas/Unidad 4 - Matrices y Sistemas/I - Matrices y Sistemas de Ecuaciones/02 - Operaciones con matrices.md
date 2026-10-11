---
dg-publish: true
---

# ➕ Operaciones con Matrices

## 🎯 Introducción

> [!info] 💡 ¿Cómo se opera con matrices?
>
> La **suma** es elemento a elemento (mismo orden) y el **producto** es fila por columna ($[AB]_{ij}=\sum_kA_{ik}B_{kj}$, exige columnas de $A$ = filas de $B$). La **transpuesta** intercambia filas y columnas. El producto **no conmuta** en general.
>
> ```mermaid
> graph LR
>     A["A m x n<br/>B n x p"] --> B["AB<br/>m x p"]
>     B --> C{"Conmuta?"}
>     C -->|Casi nunca| D["AB distinto BA"]
>     style B fill:#e1ffe1
>     style D fill:#ffe1e1
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Suma y producto por escalar
>
> Si $A,B$ son $m\times n$ y $c\in\mathbb{R}$:
>
> $$[A+B]_{ij}=A_{ij}+B_{ij}, \qquad (cA)_{ij}=cA_{ij}$$
>
> La matriz cero $O$ es el neutro ($A+O=A$) y $-A$ es la opuesta ($A+(-A)=O$).

> [!note] 📋 Definición — Producto de matrices
>
> Si $A$ es $m\times n$ y $B$ es $n\times p$:
>
> $$[AB]_{ij}=\sum_{k=1}^{n}A_{ik}B_{kj}$$
>
> El elemento $(i,j)$ es el producto punto de la fila $i$ de $A$ con la columna $j$ de $B$. Sin $n$ común, $AB$ **no existe**.

> [!note] 📋 Definición — Transpuesta
>
> $(A^T)_{ij}=A_{ji}$ (filas pasan a columnas). Propiedades: $(A^T)^T=A$, $(A+B)^T=A^T+B^T$, $(AB)^T=B^TA^T$ (orden invertido).

> [!example] 🟢 Ejemplo — Producto $2\times2$
>
> $$A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\quad B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$
>
> $$AB=\begin{pmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot0\\3\cdot0+4\cdot1&3\cdot1+4\cdot0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}$$
>
> Al revés: $BA=\begin{pmatrix}3&4\\1&2\end{pmatrix}\neq AB$.

---

## 🛠️ Método para Multiplicar

> [!note] 📋 Procedimiento general
>
> 1. Verificar compatibilidad: columnas de $A$ = filas de $B$ (si no, detenerse).
> 2. El resultado es $m\times p$.
> 3. Para cada $(i,j)$: multiplicar fila $i$ de $A$ por columna $j$ de $B$ elemento a elemento y sumar.
> 4. Verificar dimensiones del resultado.
>
> **Principio clave:** cada elemento de $AB$ combina **toda** una fila con **toda** una columna — por eso el orden importa y $AB\neq BA$ en general.

> [!tip] 💡 Cómo pensarlo sin memorizar la fórmula
>
> Imagina que la fila $i$ de $A$ es una lista de "pesos" y la columna $j$ de $B$ es una lista de "valores": el elemento $(i,j)$ de $AB$ es el total ponderado (cada peso por su valor, sumados). Por eso $AB$ responde "¿cuánto aporta cada fila a cada columna?" — y al intercambiar ($BA$), las preguntas cambian, así que el resultado casi nunca coincide.

---

## 📋 Tabla Comparativa: Suma vs. Producto

> [!note] 📋 Propiedades lado a lado
>
> | Propiedad | Suma $+$ | Producto $\times$ |
> |---|---|---|
> | **Requisito** | Mismo orden $m\times n$ | $n$ común ($m\times n$ por $n\times p$) |
> | **Conmutativa** | Sí: $A+B=B+A$ | No: $AB\neq BA$ en general |
> | **Asociativa** | Sí | Sí: $(AB)C=A(BC)$ |
> | **Neutro** | $O$ (cero) | $I$ (identidad, solo cuadradas) |
> | **Distributiva** | — | $A(B+C)=AB+AC$ |
> | **Cancelación** | Sí: $A+B=A+C\therefore B=C$ | No sin inversa |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Multiplicar sin $n$ común:** $A_{2\times3}B_{2\times2}$ no existe — verificar dimensiones primero.
> - **Transponer mal el producto:** $(AB)^T=B^TA^T$, no $A^TB^T$ (el orden se invierte).
> - **Cancelar sin inversa:** $AB=AC\not\therefore B=C$ (a diferencia de números, las matrices no siempre tienen inverso).
> - **Asumir $AB=BA$:** solo vale en casos especiales (diagonales, potencias de la misma matriz).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Suma $A+B$ con $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$.
> 2. Calcula $2A$ y $-A$ con la $A$ anterior.
> 3. ¿Existe $AB$ si $A$ es $2\times3$ y $B$ es $3\times2$? ¿De qué orden es?

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\begin{pmatrix}6&8\\10&12\end{pmatrix}$ (elemento a elemento).
>
> **2.** $\begin{pmatrix}2&4\\6&8\end{pmatrix}$; opuesta $\begin{pmatrix}-1&-2\\-3&-4\end{pmatrix}$.
>
> **3.** Sí: $n=3$ común; resultado $2\times2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Calcula $AB$ con $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, y verifica que $BA\neq AB$.
> 5. Halla $A^2$ si $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$.
> 6. Calcula $3A-2B$ con las matrices del Nivel 1.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $AB=\begin{pmatrix}2&1\\4&3\end{pmatrix}$; $BA=\begin{pmatrix}3&4\\1&2\end{pmatrix}$.
>
> **5.** $A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}$.
>
> **6.** $\begin{pmatrix}3-10&6-12\\9-14&12-16\end{pmatrix}=\begin{pmatrix}-7&-6\\-5&-4\end{pmatrix}$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $(AB)C=A(BC)$ usando la definición por índices ($\sum_{k,l}$).
> 8. Prueba $\text{tr}(AB)=\text{tr}(BA)$ para cuadradas ($\sum_{i,k}A_{ik}B_{ki}$).
> 9. Sea $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$: calcula $N^2$ y explica por qué se llama nilpotente.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $[(AB)C]_{ij}=\sum_l\sum_kA_{ik}B_{kl}C_{lj}=[A(BC)]_{ij}$ (las sumas finitas conmutan).
>
> **8.** $\text{tr}(AB)=\sum_i\sum_kA_{ik}B_{ki}=\sum_k\sum_iB_{ki}A_{ik}=\text{tr}(BA)$.
>
> **9.** $N^2=O$ (la fila 2 es cero y anula el producto): **nilpotente** de índice 2.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Sumo matrices del mismo orden y multiplico por escalar elemento a elemento.
> - [ ] Verifico la condición de $n$ común antes de multiplicar dos matrices.
> - [ ] Calculo productos $2\times2$ con la regla fila por columna.
> - [ ] Transpongo matrices e identifico el resultado correcto.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Verifico con ejemplos que $AB\neq BA$ en general.
> - [ ] Calculo potencias $A^n$ de matrices $2\times2$ concretas.
> - [ ] Aplico $(AB)^T=B^TA^T$ con el orden correcto.
> - [ ] Combino operaciones ($3A-2B$, $A(B+C)$) respetando dimensiones.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro asociatividad del producto con índices y sumas dobles.
> - [ ] Pruebo $\text{tr}(AB)=\text{tr}(BA)$ y explico su uso.
> - [ ] Reconozco matrices nilpotentes y calculo sus potencias.
> - [ ] Analizo potencias de rotaciones ($R^4=I$) y su significado geométrico.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] S. Lipschutz, *Álgebra Lineal (Schaum)*, 4ta ed., McGraw-Hill — cap. 2 (operaciones).
>
> [2] K. Rosen, *Discrete Mathematics and Its Applications*, 8th ed., McGraw-Hill, 2019 — §2.6 (matrices).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Definición y clases de matrices]] — la identidad $I$ y la cero $O$ son los neutros usados aquí.
> - [[04 - Determinantes]] — $\det(AB)=\det(A)\det(B)$ conecta producto con determinante.
> - [[06 - Matriz Inversa]] — $AA^{-1}=I$ usa el producto definido en esta nota.
> - [[03 - Matrices relevantes]] — diagonales y triangulares simplifican estos cálculos.

---

**Tags:** #matrices #operaciones-matrices #producto-matricial #algebra-lineal #unidad4

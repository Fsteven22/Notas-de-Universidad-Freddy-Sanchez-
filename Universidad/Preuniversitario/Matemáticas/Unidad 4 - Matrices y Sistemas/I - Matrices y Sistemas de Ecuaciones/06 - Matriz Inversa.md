---
dg-publish: true
---

# 🔄 Matriz Inversa

## 🎯 Introducción

> [!info] 💡 ¿Qué es $A^{-1}$?
>
> La matriz que satisface $AA^{-1}=A^{-1}A=I$. Existe si y solo si $A$ es cuadrada con $\det(A)\neq0$, y resuelve $Ax=b$ como $x=A^{-1}b$.
>
> ```mermaid
> graph LR
>     A["A<br/>n x n"] --> B{"det distinto 0?"}
>     B -->|Sí| C["Existe inversa<br/>AA-1=I"]
>     B -->|No| D["Singular<br/>sin inversa"]
>     style C fill:#e1ffe1
>     style D fill:#ffe1e1
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Inversa y condición de existencia
>
> $B$ es **inversa** de $A$ si $AB=BA=I$; si existe es única y se denota $A^{-1}$. Para $A$ cuadrada: $A^{-1}$ existe $\iff\det(A)\neq0$.
>
> **Fórmula $2\times2$:** $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ (intercambia diagonal, cambia signo del resto, divide por el determinante).
>
> **General:** $A^{-1}=\frac{1}{\det(A)}\text{adj}(A)$ con $\text{adj}(A)=C^T$ (transpuesta de cofactores), o **Gauss-Jordan**: $[A|I]\to[I|A^{-1}]$ por operaciones de fila.

> [!tip] 💡 Cómo hallarla sin perderse
>
> En $2\times2$, memoriza el patrón "cambia la diagonal, cambia el signo de los otros dos, divide todo por $ad-bc$". En tamaño mayor, Gauss-Jordan es más seguro que la adjunta: opera filas hasta ver $I$ a la izquierda y lee la inversa a la derecha — si aparece una fila de ceros, $\det=0$ y no hay inversa.

> [!example] 🟢 Ejemplo — Inversa $2\times2$ verificada
>
> $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\quad\det=2\cdot1-1\cdot1=1$$
>
> $$A^{-1}=\frac{1}{1}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$
>
> Verificación: $AA^{-1}=\begin{pmatrix}2-1&-2+2\\1-1&-1+2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ ✓

---

## 📋 Tabla Comparativa: Propiedades

> [!note] 📋 Qué vale y cuándo usarlo
>
> | Propiedad | Fórmula | Uso típico |
> |---|---|---|
> | **Producto** | $(AB)^{-1}=B^{-1}A^{-1}$ (orden inverso) | Invertir composiciones |
> | **Doble inversa** | $(A^{-1})^{-1}=A$ | Volver atrás |
> | **Transpuesta** | $(A^T)^{-1}=(A^{-1})^T$ | Conmutan ambas operaciones |
> | **Determinante** | $\det(A^{-1})=1/\det(A)$ | Si $\det=0$, no buscar inversa |
> | **Escalar** | $(kA)^{-1}=A^{-1}/k$ ($k\neq0$) | Sacar constantes |
> | **Casos rápidos** | $\text{diag}^{-1}$ invierte entradas; $Q^{-1}=Q^T$ si ortogonal | Diagonales y rotaciones |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Invertir sin verificar $\det\neq0$:** si $\det=0$ no hay inversa que hallar.
> - **Sumar inversas:** $(A+B)^{-1}\neq A^{-1}+B^{-1}$ — la inversa no distribuye sobre la suma.
> - **No invertir el orden:** $(AB)^{-1}=B^{-1}A^{-1}$, no $A^{-1}B^{-1}$ (como al deshacer pasos en orden inverso: primero se deshace lo último).
> - **Calcular $A^{-1}$ elemento a elemento:** $1/a_{ij}$ no es la inversa — la inversa mezcla toda la matriz.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Halla la inversa de $\begin{pmatrix}2&1\\1&1\end{pmatrix}$ y verifica $AA^{-1}=I$.
> 2. ¿Es invertible $\begin{pmatrix}1&2\\2&4\end{pmatrix}$? Justifica con $\det$.
> 3. Halla la inversa de $\text{diag}(2,3,4)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$ (ver ejemplo).
>
> **2.** No: $\det=4-4=0$.
>
> **3.** $\text{diag}(1/2,1/3,1/4)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Halla $A^{-1}$ con $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ por adjunta y verifica.
> 5. Halla $\begin{pmatrix}2&1\\4&3\end{pmatrix}^{-1}$ por Gauss-Jordan.
> 6. Calcula $(AB)^{-1}$ con $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, $B=\begin{pmatrix}3&0\\1&2\end{pmatrix}$ de dos formas.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\det=-2$; $A^{-1}=\frac{1}{-2}\begin{pmatrix}4&-2\\-3&1\end{pmatrix}=\begin{pmatrix}-2&1\\3/2&-1/2\end{pmatrix}$.
>
> **5.** $\det=2$; $[A|I]\to\dots\to\begin{pmatrix}3/2&-1/2\\-2&1\end{pmatrix}$.
>
> **6.** Directo: $AB=\begin{pmatrix}5&4\\1&2\end{pmatrix}$, $(AB)^{-1}=\frac{1}{6}\begin{pmatrix}2&-4\\-1&5\end{pmatrix}$; vía $B^{-1}A^{-1}$ (mismo resultado).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $(AB)^{-1}=B^{-1}A^{-1}$ usando solo $AA^{-1}=I$.
> 8. Prueba $(A^{-1})^{-1}=A$ y $(A^T)^{-1}=(A^{-1})^T$.
> 9. Sea $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$: explica por qué no tiene inversa de dos formas ($\det$ y $Nx=0$ con $x\neq0$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AA^{-1}=I$ (y al revés); por unicidad es la inversa.
>
> **8.** $A^{-1}A=I$ dice que $A$ es la inversa de $A^{-1}$; $(A^T)(A^{-1})^T=(AA^{-1})^T=I^T=I$.
>
> **9.** $\det=0$; además $N\binom{0}{1}=\binom{0}{0}$ con vector no nulo (no inyectiva).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico la fórmula $2\times2$ (cambia diagonal, cambia signo, divide por $\det$).
> - [ ] Verifico $AA^{-1}=I$ después de hallar una candidata.
> - [ ] Decido invertibilidad con $\det$ antes de operar.
> - [ ] Invierto diagonales entrada por entrada.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Invierto $2\times2$ y $3\times3$ por Gauss-Jordan.
> - [ ] Aplico $(AB)^{-1}=B^{-1}A^{-1}$ con el orden correcto.
> - [ ] Resuelvo $Ax=b$ como $x=A^{-1}b$ cuando aplica.
> - [ ] Distingo inversa de función ($A^{-1}$) de inversa elemento a elemento.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro $(AB)^{-1}$, $(A^{-1})^{-1}$ y $(A^T)^{-1}$ desde los axiomas.
> - [ ] Explico no invertibilidad por $\det=0$ y por no inyectividad.
> - [ ] Relaciono inversa con unicidad de solución en sistemas.
> - [ ] Conecto ortogonalidad ($Q^{-1}=Q^T$) con rotaciones.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] S. Lipschutz, *Álgebra Lineal (Schaum)*, 4ta ed., McGraw-Hill — cap. 2 (inversa).
>
> [2] K. Rosen, *Discrete Mathematics and Its Applications*, 8th ed., McGraw-Hill, 2019 — §2.6 (matrices).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Determinantes]] — $\det\neq0$ como condición de existencia.
> - [[05 - Sistemas de ecuaciones lineales]] — $x=A^{-1}b$ como método.
> - [[02 - Operaciones con matrices]] — producto y transpuesta usados en las pruebas.
> - [[03 - Matrices relevantes]] — diagonales y ortogonales, casos rápidos.

---

**Tags:** #matrices #matriz-inversa #algebra-lineal #unidad4

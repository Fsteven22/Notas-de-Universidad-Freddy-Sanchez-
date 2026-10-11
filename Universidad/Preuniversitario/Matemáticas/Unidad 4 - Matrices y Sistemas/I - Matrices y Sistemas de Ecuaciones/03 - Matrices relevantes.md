---
dg-publish: true
---

# ⭐ Matrices Relevantes

## 🎯 Introducción

> [!info] 💡 ¿Qué matrices vale la pena conocer por nombre?
>
> La **inversa** ($AA^{-1}=I$), las **geométricas** (rotación, reflexión, proyección), las **de modelo** (permutación, Markov) y **Vandermonde** (interpolación). Cada una resuelve un problema típico que reaparece en [[06 - Matriz Inversa]] y [[05 - Sistemas de ecuaciones lineales]].
>
> ```mermaid
> graph LR
>     A["Matriz<br/>especial"] --> B["Qué hace?"]
>     B -->|Invierte| C["Inversa<br/>AA-1=I"]
>     B -->|Transforma| D["Rot/Ref/Proy"]
>     B -->|Modela| E["Markov/Perm"]
>     style C fill:#e1ffe1
>     style E fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Inversa de una matriz cuadrada
>
> $B$ es **inversa** de $A$ (cuadrada) si $AB=BA=I$. Si existe, es única y se denota $A^{-1}$. Existe si y solo si $\det(A)\neq0$ (ver [[04 - Determinantes]]).
>
> $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\quad\therefore\quad A^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$
>
> Verificación: $AA^{-1}=\begin{pmatrix}2\cdot1+1\cdot(-1)&2\cdot(-1)+1\cdot2\\1\cdot1+1\cdot(-1)&1\cdot(-1)+1\cdot2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$.

> [!tip] 💡 Cómo pensarla sin memorizar
>
> La inversa "deshace" lo que $A$ hace: si $A$ lleva $x$ a $b=Ax$, entonces $A^{-1}$ lleva $b$ de vuelta a $x$. Por eso $A^{-1}$ **no** es $1/A$ elemento a elemento — es la operación completa al revés, y por eso exige que $A$ sea cuadrada con $\det\neq0$.

> [!note] 📋 Definición — Matrices geométricas
>
> - **Rotación** $\theta$: $\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ (a $90°$: $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$).
> - **Reflexión** en $x$: $\text{diag}(1,-1)$; **proyección** sobre $x$: $\text{diag}(1,0)$.
>
> Todas son ortogonales o idempotentes: $R^T=R^{-1}$, $P^2=P$.

> [!tip] 💡 Cómo visualizarlas
>
> Aplica la matriz a los vectores base $(1,0)$ y $(0,1)$: sus imágenes son las **columnas** de la matriz, y dibujarlas revela la transformación (rotar, reflejar o aplanar). Si las columnas se ven "aplastadas" sobre una línea, es una proyección.

> [!note] 📋 Definición — Matrices de modelo
>
> - **Permutación:** una $1$ por fila y columna (reordena coordenadas).
> - **Markov:** entradas $\ge0$ con columnas que suman $1$ (probabilidades de transición).
> - **Vandermonde:** $(x_i^{j})$ para interpolar por $n$ puntos.
>
> > [!example] 🟢 Ejemplo — Rota $(1,0)$ por $90°$
> >
> > $$\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}0\\1\end{pmatrix}$$
> >
> > El $(1,0)$ termina en $(0,1)$: giro antihorario de $90°$, como se espera.

---

## 📋 Tabla Comparativa

> [!note] 📋 Qué la distingue y cuándo usarla
>
> | Matriz | Se reconoce por | Sirve para |
> |---|---|---|
> | **Inversa** $A^{-1}$ | $AA^{-1}=I$ | Deshacer $A$, resolver $Ax=b$ |
> | **Rotación** | columnas ortonormales, $\det=1$ | Girar vectores |
> | **Reflexión** | $M^2=I$, $\det=-1$ | Espejar en un eje |
> | **Proyección** | $P^2=P$ | Aplastar sobre un subespacio |
> | **Permutación** | una $1$ por fila/columna | Reordenar coordenadas |
> | **Markov** | columnas suman $1$ | Evolucionar probabilidades |
> | **Vandermonde** | potencias $x_i^j$ | Interpolar polinomios |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Calcular $A^{-1}$ como $1/A$ elemento a elemento:** la inversa invierte la **operación completa**, no cada número — se halla con Gauss-Jordan o la fórmula de [[06 - Matriz Inversa]].
> - **Creer que rotación y reflexión son lo mismo:** rotar preserva orientación ($\det=1$); reflejar la invierte ($\det=-1$).
> - **Pedir inversa de una no cuadrada:** sin determinante no hay inversa (aunque existan pseudoinversas, fuera de este curso).
> - **Olvidar verificar $BA=I$ además de $AB=I$:** en dimensión finita basta una, pero al proponer candidata conviene comprobar ambas direcciones.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Halla la inversa de $\begin{pmatrix}2&1\\1&1\end{pmatrix}$ y verifica $AA^{-1}=I$.
> 2. Rota $(1,0)$ por $90°$ y refleja $(2,3)$ en el eje $x$.
> 3. Proyecta $(2,3)$ sobre el eje $x$ y explica por qué $P^2=P$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$; el producto da $I$.
>
> **2.** $(0,1)$; $(2,-3)$.
>
> **3.** $(2,0)$; proyectar dos veces no cambia nada.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Calcula $R_{90}^2$ y $R_{90}^4$ e interpreta geométricamente.
> 5. Verifica que $\begin{pmatrix}0.7&0.4\\0.3&0.6\end{pmatrix}$ es Markov (columnas suman $1$).
> 6. Halla el determinante de Vandermonde con $x=1,2,3$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $R_{90}^2=-I$ (giro $180°$), $R_{90}^4=I$ (vuelta completa).
>
> **5.** $0.7+0.3=1$, $0.4+0.6=1$.
>
> **6.** $(3-2)(3-1)(2-1)=2$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $R(\theta)R(\phi)=R(\theta+\phi)$ usando suma de ángulos.
> 8. Prueba que si $Q$ es ortogonal entonces $\det(Q)=\pm1$.
> 9. Halla el vector estacionario de $\begin{pmatrix}0.7&0.4\\0.3&0.6\end{pmatrix}$ resolviendo $\pi P=\pi$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** El producto da $\cos(\theta+\phi)$ y $\sin(\theta+\phi)$ en las posiciones correctas.
>
> **8.** $\det(Q^TQ)=(\det Q)^2=\det(I)=1$.
>
> **9.** $\pi=(4/7,3/7)$: el $57\%$ termina en el estado 1 a largo plazo.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo inversas $2\times2$ y verifico $AA^{-1}=I$.
> - [ ] Aplico rotaciones, reflexiones y proyecciones a vectores concretos.
> - [ ] Reconozco matrices de permutación y de Markov por su forma.
> - [ ] Distingo cuándo una matriz es candidata a tener inversa.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Compongo rotaciones y calculo sus potencias con significado geométrico.
> - [ ] Hallo vectores estacionarios de matrices de Markov $2\times2$.
> - [ ] Uso Vandermonde para interpolar por puntos dados.
> - [ ] Verifico idempotencia ($P^2=P$) y sus consecuencias.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Pruebo $R(\theta)R(\phi)=R(\theta+\phi)$ y $\det(Q)=\pm1$ para ortogonales.
> - [ ] Descompongo rotaciones en producto de reflexiones.
> - [ ] Relaciono ortogonalidad con preservación de longitudes y ángulos.
> - [ ] Conecto Vandermonde con unicidad del polinomio interpolante.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] S. Lipschutz, *Álgebra Lineal (Schaum)*, 4ta ed., McGraw-Hill — cap. 3 (matrices especiales).
>
> [2] K. Rosen, *Discrete Mathematics and Its Applications*, 8th ed., McGraw-Hill, 2019 — §2.6 (matrices).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Operaciones con matrices]] — el producto y la transpuesta usados para verificar $AA^{-1}=I$.
> - [[06 - Matriz Inversa]] — método general de Gauss-Jordan para hallar $A^{-1}$.
> - [[04 - Determinantes]] — $\det\neq0$ como condición de existencia de la inversa.
> - [[05 - Sistemas de ecuaciones lineales]] — $x=A^{-1}b$ resuelve sistemas cuadrados.

---

**Tags:** #matrices #matrices-especiales #inversa #algebra-lineal #unidad4

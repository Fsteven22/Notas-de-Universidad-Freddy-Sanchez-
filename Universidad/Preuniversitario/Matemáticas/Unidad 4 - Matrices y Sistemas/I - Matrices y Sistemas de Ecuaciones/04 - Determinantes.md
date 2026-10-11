---
dg-publish: true
---

# 🎯 Determinantes

## 🎯 Introducción

> [!info] 💡 ¿Qué es un determinante?
>
> El **determinante** $\det(A)$ es un escalar asociado a cada matriz **cuadrada**: mide cuánto escala volúmenes la transformación, y decide **invertibilidad** ($\det\neq0\iff A^{-1}$ existe). Es la herramienta de [[06 - Matriz Inversa]] y de la regla de Cramer en [[05 - Sistemas de ecuaciones lineales]].
>
> ```mermaid
> graph LR
>     A["Matriz<br/>cuadrada A"] --> B["det(A)<br/>escalar"]
>     B --> C{"det = 0?"}
>     C -->|Sí| D["Singular<br/>sin inversa"]
>     C -->|No| E["Regular<br/>existe A-1"]
>     style A fill:#fff4e1
>     style C fill:#e1ffe1
>     style E fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Determinante $2\times2$ y $3\times3$
>
> Para $2\times2$: $\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc$ (diagonal principal menos diagonal secundaria).
>
> Para $3\times3$: regla de **Sarrus** (repite las dos primeras columnas y suma diagonales $\searrow$ menos $\nearrow$) o desarrollo por cofactores en cualquier fila/columna.
>
> Para $n\times n$: desarrollo recursivo por cofactores, o reducción de **Gauss** a triangular (el determinante es el producto de la diagonal, cambiando de signo por cada intercambio de filas).

> [!tip] 💡 Cómo calcularlo sin equivocarse
>
> En $2\times2$, dibuja mentalmente las dos diagonales: multiplica la que baja ($\searrow$) y réstale la que sube ($\nearrow$). En $3\times3$ con Sarrus, escribe las columnas $1,2$ otra vez a la derecha y suma las tres diagonales que bajan menos las tres que suben — si un término te da un signo raro, revisa justo esas diagonales.

> [!example] 🟢 Ejemplo — $2\times2$ y $3\times3$
>
> $$\begin{vmatrix}2&3\\1&4\end{vmatrix}=2\cdot4-3\cdot1=5$$
>
> $$\begin{vmatrix}2&1&-1\\3&0&2\\1&-2&1\end{vmatrix}=2(0\cdot1-2\cdot(-2))-1(3\cdot1-2\cdot1)+(-1)(3\cdot(-2)-0\cdot1)=8-1+6=13$$

---

## 📋 Tabla Comparativa: Propiedades

> [!note] 📋 Qué hace cada propiedad y cuándo usarla
>
> | Propiedad | Fórmula | Uso típico |
> |---|---|---|
> | **Producto** | $\det(AB)=\det(A)\det(B)$ | $\det=0$ si algún factor es singular |
> | **Transpuesta** | $\det(A^T)=\det(A)$ | Desarrollar por la fila/columna con más ceros |
> | **Inversa** | $\det(A^{-1})=1/\det(A)$ | Si $\det=0$, no buscar inversa |
> | **Escalar** | $\det(kA)=k^n\det(A)$ ($n\times n$) | El $k$ sale una vez **por fila** |
> | **Fila nula o proporcional** | $\det=0$ | Detectar singularidad al instante |
> | **Triangular** | producto de la diagonal | Objetivo de Gauss |

> [!tip] 💡 Cómo usar las propiedades para ahorrar cálculo
>
> Antes de desarrollar, mira la matriz: ¿fila de ceros? ¿dos filas proporcionales? ¿triangular? Cualquiera de esas respuestas da el determinante **sin operar**. Solo desarrolla (Sarrus/cofactores) cuando la matriz no tiene atajos visibles.

---

## 📐 Geometría y Aplicaciones

> [!note] 📋 Definición — Significado geométrico
>
> $|\det(A)|$ es el área (2D) o volumen (3D) del paralelepípedo formado por las columnas de $A$. El signo indica si la transformación preserva orientación ($+$) o la invierte ($-$).
>
> **Aplicaciones:** Cramer ($x_i=\det(A_i)/\det(A)$ para sistemas cuadrados); eigenvalores ($\det(A-\lambda I)=0$).

> [!example] 🟢 Ejemplo — Cramer $2\times2$
>
> Sistema $2x+3y=8$, $x+4y=11$: $\det=2\cdot4-3\cdot1=5$.
>
> $$x=\frac{\begin{vmatrix}8&3\\11&4\end{vmatrix}}{5}=\frac{32-33}{5}=-\frac{1}{5},\qquad y=\frac{\begin{vmatrix}2&8\\1&11\end{vmatrix}}{5}=\frac{22-8}{5}=\frac{14}{5}$$

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Distribuir sobre la suma:** $\det(A+B)\neq\det(A)+\det(B)$ — el determinante no es lineal en la suma.
> - **Sacar el escalar una sola vez:** $\det(kA)=k^n\det(A)$, no $k\det(A)$ (el $k$ multiplica cada una de las $n$ filas).
> - **Creer que $\det=0$ implica $A=O$:** $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ tiene $\det=0$ sin ser cero (filas proporcionales).
> - **Olvidar el signo en cofactores:** el signo $(-1)^{i+j}$ alterna como tablero de ajedrez — verifica la casilla antes de desarrollar.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Calcula $\begin{vmatrix}2&3\\1&4\end{vmatrix}$ y $\begin{vmatrix}5&-2\\3&1\end{vmatrix}$.
> 2. Calcula $\det(I_3)$, $\det(O_{2})$ y $\det(kI_3)$.
> 3. Calcula el determinante de $\begin{pmatrix}2&3\\0&4\end{pmatrix}$ sin desarrollar.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $8-3=5$; $5+6=11$.
>
> **2.** $1$, $0$, $k^3$ (el $k$ sale 3 veces).
>
> **3.** $2\cdot4=8$ (triangular: producto diagonal).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Verifica $\det(AB)=\det(A)\det(B)$ con $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.
> 5. Halla $a$ para que $\det\begin{pmatrix}2&a\\4&6\end{pmatrix}=0$.
> 6. Resuelve $2x+3y=8$, $x+4y=11$ con Cramer.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\det(A)=-2$, $\det(B)=-1$, producto $2$; $AB=\begin{pmatrix}2&1\\4&3\end{pmatrix}$ con $\det=6-4=2$. ✓
>
> **5.** $12-4a=0\therefore a=3$ (filas proporcionales).
>
> **6.** $\det=5$, $x=-1/5$, $y=14/5$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba que $\det\begin{pmatrix}A&B\\O&D\end{pmatrix}=\det(A)\det(D)$ para bloques cuadrados.
> 8. Halla los eigenvalores de $\begin{pmatrix}2&1\\1&2\end{pmatrix}$ con $\det(A-\lambda I)=0$.
> 9. Prueba $\det(A^{-1})=1/\det(A)$ partiendo de $AA^{-1}=I$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Desarrolla por la primera columna repetidamente: solo sobreviven los productos de diagonales de $A$ y $D$.
>
> **8.** $(2-\lambda)^2-1=0\therefore\lambda^2-4\lambda+3=0\therefore\lambda=1,3$.
>
> **9.** $1=\det(I)=\det(AA^{-1})=\det(A)\det(A^{-1})$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo determinantes $2\times2$ con diagonales sin equivocarme en el signo.
> - [ ] Aplico Sarrus en $3\times3$ repitiendo las dos primeras columnas.
> - [ ] Reconozco casos inmediatos: identidad, cero, triangular y filas proporcionales.
> - [ ] Distingo cuándo un determinante es cero sin desarrollar.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Desarrollo por cofactores eligiendo la fila/columna con más ceros.
> - [ ] Reduzco por Gauss a triangular contando intercambios de fila.
> - [ ] Resuelvo sistemas $2\times2$ con la regla de Cramer.
> - [ ] Uso $\det(AB)$ y $\det(kA)$ con el exponente correcto.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Pruebo propiedades con bloques e índices.
> - [ ] Hallo eigenvalores $2\times2$ con el polinomio característico.
> - [ ] Relaciono determinante nulo con dependencia lineal de filas/columnas.
> - [ ] Decido si una matriz es invertible antes de intentar invertirla.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] S. Lipschutz, *Álgebra Lineal (Schaum)*, 4ta ed., McGraw-Hill — cap. 4 (determinantes).
>
> [2] K. Rosen, *Discrete Mathematics and Its Applications*, 8th ed., McGraw-Hill, 2019 — §2.6 (matrices).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Matrices relevantes]] — triangulares y diagonales, donde el determinante es inmediato.
> - [[06 - Matriz Inversa]] — $\det\neq0$ como condición y $A^{-1}=\text{adj}(A)/\det(A)$.
> - [[05 - Sistemas de ecuaciones lineales]] — Cramer y criterio de solución única.
> - [[02 - Operaciones con matrices]] — $\det(AB)$ conecta producto con determinante.

---

**Tags:** #matrices #determinantes #algebra-lineal #unidad4

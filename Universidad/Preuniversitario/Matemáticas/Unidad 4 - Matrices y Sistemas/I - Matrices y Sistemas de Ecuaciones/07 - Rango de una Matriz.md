---
dg-publish: true
---

# 📏 Rango de una Matriz

## 🎯 Introducción

> [!info] 💡 ¿Qué es el rango?
>
> El **rango** $r(A)$ es el número máximo de filas (o columnas) linealmente independientes de $A$. Cuenta las ecuaciones "útiles" de un sistema: con él, Rouché-Frobenius decide si $Ax=b$ tiene solución única, infinitas o ninguna.
>
> ```mermaid
> graph LR
>     A["Matriz A"] --> B["Filas/cols<br/>indep"]
>     B --> C["r(A)"]
>     C --> D{"r = n?"}
>     D -->|Sí| E["Invertible"]
>     D -->|No| F["Singular"]
>     style C fill:#e1ffe1
>     style F fill:#ffe1e1
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Rango y cómo calcularlo
>
> $r(A)$ = máximo $k$ tal que existe un menor $k\times k$ no nulo = número de filas no nulas tras Gauss = dimensión del espacio fila = dimensión del espacio columna.
>
> **Métodos:**
> 1. **Gauss:** triangular por filas; $r$ = filas no nulas.
> 2. **Menores:** mayor $k$ con algún $\det_{k\times k}\neq0$.
>
> Propiedades: $r(A)=r(A^T)$; $r(AB)\le\min(r(A),r(B))$; $r(A)=n\iff A^{-1}$ existe ($n\times n$).

> [!tip] 💡 Cómo hallarlo sin perderse
>
> Triangulariza por Gauss y cuenta las filas que no se anulan por completo — ese conteo **es** el rango. Si una fila se vuelve $(0,\dots,0)$, era combinación de las anteriores: ignórala y sigue. Para matrices pequeñas ($2\times2$, $3\times3$), mirar si hay filas proporcionales suele bastar.

> [!example] 🟢 Ejemplo — Rango por Gauss
>
> $$A=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}$$
>
> La fila 2 es $2\times$ la fila 1, así que se anula al restar: quedan $\begin{pmatrix}1&2&3\\0&0&0\\1&0&1\end{pmatrix}$, y la fila 3 es independiente. Filas no nulas: $2$ $\therefore r(A)=2$.

---

## 📋 Tabla Comparativa: Rango e Invertibilidad

> [!note] 📋 Qué dice el rango en cada caso
>
> | Situación | Rango | Consecuencia |
> |---|---|---|
> | $A$ $n\times n$ con $r=n$ | Completo | Invertible ($\det\neq0$) |
> | $A$ $n\times n$ con $r<n$ | Deficiente | Singular ($\det=0$) |
> | $Ax=b$ con $r(A)=r(A\|b)=n$ | — | Solución única |
> | $Ax=b$ con $r(A)=r(A\|b)<n$ | — | Infinitas ($n-r$ parámetros) |
> | $Ax=b$ con $r(A)\neq r(A\|b)$ | — | Incompatible ($\emptyset$) |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Contar filas no nulas antes de triangularizar:** filas proporcionales parecen independientes hasta que Gauss las anula — triangulariza primero.
> - **Creer que $r(A)=r(A^T)$ es casualidad:** vale siempre (espacios fila y columna tienen igual dimensión), no solo en ejemplos.
> - **Asumir $r(AB)=\min(r(A),r(B))$:** es solo una cota superior; el producto puede perder rango (ej. $A\neq O$ con $A^2=O$ tiene $r(A^2)=0$).
> - **Confundir rango con determinante:** el rango existe para cualquier tamaño; el determinante solo para cuadradas.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Halla $r(A)$ con $A=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}$ por Gauss.
> 2. Halla $r(I_3)$, $r(O_{2})$ y $r\begin{pmatrix}1&1\\1&1\end{pmatrix}$.
> 3. Clasifica con Rouché: $A=\begin{pmatrix}1&2\\2&4\end{pmatrix}$, $b=(3,5)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $r=2$ (fila 2 = $2\times$ fila 1, se anula).
>
> **2.** $3$, $0$, $1$ (filas proporcionales).
>
> **3.** $r(A)=1\neq2=r(A|b)$ → incompatible.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Si $r(A)=2$ y $r(B)=3$ con $n=4$ común, acota $r(AB)$ con Sylvester.
> 5. Prueba que $r(A)=r(A^T)$ usando Gauss por filas y por columnas.
> 6. $A$ $3\times4$ con $r(A)=2$: ¿cuántos parámetros libres tiene $Ax=0$?

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $2+3-4=1\le r(AB)\le\min(2,3)=2$.
>
> **5.** Triangularizar por filas o columnas da el mismo conteo de pivotes no nulos.
>
> **6.** $4-2=2$ parámetros.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $r(AB)\ge r(A)+r(B)-n$ (Sylvester) usando nulidades.
> 8. Prueba $r(A)=r(A^TA)$ para $A$ real ($A^TAx=0\iff Ax=0$).
> 9. Si $A$ es $n\times n$ con $r(A)=n-1$, prueba que $\dim\ker(A)=1$ y que $\text{adj}(A)\neq O$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $n-r(AB)\le(n-r(A))+(n-r(B))$ contando dimensiones de núcleos.
>
> **8.** $x^TA^TAx=\|Ax\|^2=0\iff Ax=0$: mismo núcleo, mismo rango.
>
> **9.** $\dim\ker=n-r=1$; algún menor $(n-1)\times(n-1)$ es no nulo $\therefore$ adjunta no nula.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Triangularizo por Gauss y cuento filas no nulas para hallar el rango.
> - [ ] Detecto filas proporcionales como dependencia inmediata.
> - [ ] Clasifico $Ax=b$ con Rouché-Frobenius en los tres casos.
> - [ ] Relaciono $r=n$ con invertibilidad en cuadradas.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico Sylvester para acotar $r(AB)$.
> - [ ] Pruebo $r(A)=r(A^T)$ por pivotes.
> - [ ] Hallo parámetros libres como $n-r$ en homogéneos.
> - [ ] Uso el rango para decidir si $\det=0$ sin calcularlo.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro Sylvester y $r(A)=r(A^TA)$ con núcleos.
> - [ ] Relaciono rango, nulidad y adjunta en el caso $r=n-1$.
> - [ ] Explico por qué el producto puede perder rango con nilpotentes.
> - [ ] Conecto rango con dependencia lineal de filas/columnas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] S. Lipschutz, *Álgebra Lineal (Schaum)*, 4ta ed., McGraw-Hill — cap. 1 (rango).
>
> [2] K. Rosen, *Discrete Mathematics and Its Applications*, 8th ed., McGraw-Hill, 2019 — §2.4 (matrices).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[05 - Sistemas de ecuaciones lineales]] — Rouché-Frobenius usa $r(A)$ y $r(A|b)$.
> - [[06 - Matriz Inversa]] — $r=n\iff A^{-1}$ existe.
> - [[04 - Determinantes]] — $\det\neq0\iff r=n$ en cuadradas.
> - [[01 - Definición y clases de matrices]] — filas y columnas como vectores.

---

**Tags:** #matrices #rango #algebra-lineal #unidad4

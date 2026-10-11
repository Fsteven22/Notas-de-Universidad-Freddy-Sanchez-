---
dg-publish: true
---

# 📊 Sistemas de Ecuaciones Lineales

## 🎯 Introducción

> [!info] 💡 ¿Qué es un sistema lineal?
>
> $Ax=b$ con $A$ matriz $m\times n$ busca $x$ que cumpla **todas** las ecuaciones a la vez. El teorema de **Rouché-Frobenius** (comparar rangos de $A$ y de la ampliada $A|b$) decide si hay solución única, infinitas o ninguna.
>
> ```mermaid
> graph LR
>     A["A x = b"] --> B{"Rango A<br/>vs A|b"}
>     B -->|Iguales = n| C["Única<br/>x=A-1b"]
>     B -->|Iguales menor n| D["Infinitas<br/>parámetros"]
>     B -->|Distintos| E["Incompatible<br/>vacío"]
>     style C fill:#e1ffe1
>     style E fill:#ffe1e1
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Sistema y teorema de Rouché-Frobenius
>
> $A_{m\times n}x=b$ con $A\in\mathbb{R}^{m\times n}$, $x\in\mathbb{R}^n$, $b\in\mathbb{R}^m$. Sea $r(A)$ el rango y $A|b$ la matriz ampliada:
>
> - **Compatible determinado:** $r(A)=r(A|b)=n$ → solución única.
> - **Compatible indeterminado:** $r(A)=r(A|b)<n$ → infinitas ($n-r$ parámetros libres).
> - **Incompatible:** $r(A)\neq r(A|b)$ → ninguna ($\emptyset$).

> [!tip] 💡 Cómo leer el teorema sin memorizarlo
>
> Piensa en ecuaciones "útiles" (independientes) frente a incógnitas: si las útiles igualan a las incógnitas, una solución; si sobran incógnitas, infinitas (las libres parametrizan); si aparece $0=1$, ninguna. El rango cuenta exactamente esas ecuaciones útiles.

---

## 🛠️ Métodos de Resolución

> [!note] 📋 Procedimiento general — Gauss y alternativas
>
> 1. Escribir la matriz ampliada $A|b$.
> 2. **Gauss:** triangular superior con operaciones de fila (intercambiar si el pivote es $0$), luego sustitución regresiva.
> 3. **Gauss-Jordan:** continuar hasta forma $\begin{pmatrix}I&B\end{pmatrix}$ (solución directa).
> 4. **Alternativas** (solo cuadradas con $\det\neq0$): Cramer $x_i=\det(A_i)/\det(A)$ o $x=A^{-1}b$.
>
> **Principio clave:** las operaciones de fila no cambian el conjunto solución — solo lo reescriben en forma más simple.

> [!example] 🟢 Ejemplo — Gauss $3\times3$
>
> $$\begin{cases}2x+y-z=8\\-3x-y+2z=-11\\-2x+y+2z=-3\end{cases}$$
>
> 1. Suma la 1ª a la 2ª: $-x+z=-3$; suma la 1ª a la 3ª: $2y+z=5$.
> 2. De la primera: $x=z+3$; de la segunda: $y=(5-z)/2$.
> 3. Sustituye en la 1ª: $2(z+3)+(5-z)/2-z=8\therefore z=-1$, luego $x=2$, $y=3$.
> 4. Verificación en la 2ª: $-6-3-2=-11$ ✓. **Solución:** $(2,3,-1)$.

---

## 📋 Tabla Comparativa: Métodos

> [!note] 📋 Cuándo usar cada uno
>
> | Método | Cuándo conviene | Requisito |
> |---|---|---|
> | **Gauss** | General, cualquier tamaño | Ninguno (intercambia filas si pivote $0$) |
> | **Gauss-Jordan** | Quieres la solución sin sustituir | Más operaciones, mismo requisito |
> | **Cramer** | $2\times2$, $3\times3$ a mano | Cuadrada con $\det\neq0$ |
> | **Inversa** | Mismo $A$, varios $b$ | Cuadrada con $\det\neq0$ |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Dividir por un pivote $0$ sin intercambiar filas:** busca otra fila con entrada no nula o el sistema cambia.
> - **Asumir solución única con $r(A)=r(A|b)<n$:** hay **infinitas** — parametriza las variables libres en función de parámetros.
> - **Olvidar verificar:** sustituye la solución en las ecuaciones originales (detecta errores de cálculo como el del ejemplo).
> - **Usar Cramer o inversa sin comprobar $\det\neq0$:** si $\det=0$, esos métodos no aplican.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Resuelve $\begin{cases}x+y=3\\2x-y=0\end{cases}$ por sustitución y por Gauss.
> 2. Clasifica con Rouché: $x+y=2$, $2x+2y=5$.
> 3. Halla $r(A)$ y $r(A|b)$ para $A=\begin{pmatrix}1&2\\2&4\end{pmatrix}$, $b=(3,5)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $x=1,y=2$ (suma: $3x=3$).
>
> **2.** Incompatible: $r(A)=1\neq2=r(A|b)$ (la segunda es $0=1$).
>
> **3.** $r(A)=1$, $r(A|b)=2$ → incompatible.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Resuelve $\begin{cases}x+y+z=6\\2x-y+z=3\\x-y+2z=4\end{cases}$ por Gauss y verifica.
> 5. Parametriza: $x+y+z=1$, $2x+2y+2z=2$ (¿cuántos parámetros?).
> 6. Halla $k$ para que $\begin{cases}x+y=2\\2x+ky=4\end{cases}$ tenga infinitas soluciones.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Resta/suma: $y=1$... resolviendo: $x=1,y=2,z=3$; verifica $1+2+3=6$ ✓.
>
> **5.** Una ecuación útil, $3$ incógnitas → $2$ parámetros: $(1-s-t,s,t)$.
>
> **6.** $k=2$ (ecuaciones proporcionales: $r=1<2$).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Discute según $k$: $x+y+z=1$, $x+ky+z=2$, $x+2y+z=3$ (¿única, infinitas o ninguna?).
> 8. Explica por qué $Ax=b$ con $A$ no cuadrada $3\times2$ no puede tener solución única para todo $b$.
> 9. Plantea mínimos cuadrados para $Ax=b$ incompatible: ecuación normal $A^TAx=A^Tb$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Resta la 1ª de la 2ª: $(k-1)y=1$. Si $k\neq1$: única. Si $k=1$: $0=1$ → incompatible.
>
> **8.** $r(A)\le2<3=n$ como máximo... con $3$ incógnitas y $2$ ecuaciones $n=3>r$ como máximo $2$: nunca $r=n=3$.
>
> **9.** Minimiza $\|Ax-b\|^2$ derivando: $A^TAx=A^Tb$ (cuadrada y resoluble si columnas independientes).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Resuelvo sistemas $2\times2$ por sustitución y por Gauss.
> - [ ] Calculo rangos $2\times2$ y clasifico con Rouché-Frobenius.
> - [ ] Distingo los tres casos: única, infinitas, ninguna.
> - [ ] Verifico soluciones sustituyendo en las ecuaciones originales.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico Gauss y Gauss-Jordan en $3\times3$ sin perderme en las cuentas.
> - [ ] Parametrizo soluciones infinitas con el número correcto de parámetros.
> - [ ] Hallo valores críticos de $k$ que cambian la clasificación.
> - [ ] Uso Cramer e inversa solo cuando $\det\neq0$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Discuto sistemas con parámetros según $k$ de forma completa.
> - [ ] Explico límites de unicidad en sistemas no cuadrados.
> - [ ] Planteo mínimos cuadrados para sistemas incompatibles.
> - [ ] Relaciono rango, determinante y geometría (planos que se cortan).

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] S. Lipschutz, *Álgebra Lineal (Schaum)*, 4ta ed., McGraw-Hill — cap. 2–3 (sistemas y rango).
>
> [2] K. Rosen, *Discrete Mathematics and Its Applications*, 8th ed., McGraw-Hill, 2019 — §2.4 (matrices).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Determinantes]] — Cramer y criterio $\det\neq0$ para solución única.
> - [[06 - Matriz Inversa]] — $x=A^{-1}b$ como método alternativo.
> - [[07 - Rango de una Matriz]] — cálculo del rango usado en Rouché-Frobenius.
> - [[01 - Definición y clases de matrices]] — la matriz $A$ y la ampliada $A|b$.

---

**Tags:** #sistemas-lineales #gauss #rouche-frobenius #algebra-lineal #unidad4

# 🔁 Inducción Matemática

## 🎯 Introducción

> [!info]- 💡 ¿Para qué sirve la inducción matemática?
> 
> La **inducción matemática** es una técnica de demostración que permite probar que una proposición $S(n)$ es verdadera para **todos los números naturales** (o para todo entero mayor o igual a un valor inicial $n_0$).
> 
> Es especialmente útil cuando queremos demostrar fórmulas de sumas, desigualdades, propiedades de divisibilidad, o cualquier propiedad que dependa de $n \in \mathbb{N}$.

---

## 📐 Principio de Inducción Matemática (Simple)

> [!note]- 📖 Principio de Inducción Matemática
> 
> Suponga que se tiene una función proposicional $S(n)$, cuyo dominio de discurso es $\mathbb{N}$. Suponga que:
> 
> 1. $S(1)$ es verdadera, **y**
> 2. Para cada $n \in \mathbb{N}$, si $S(n)$ es verdadera entonces $S(n+1)$ es verdadera.
> 
> Entonces $S(n)$ es verdadera **para cada $n \in \mathbb{N}$**.
> 
> > La condición (1) se llama **paso base** y la condición (2) se llama **paso inductivo**. La suposición de que $S(n)$ es verdadera en el paso inductivo se llama **hipótesis inductiva**.

---

## 🔧 Estructura de una Demostración por Inducción

> [!tip]- ⚙️ Pasos a seguir
> 
> ```
> 1. PASO BASE:   Verificar que S(1) es verdadera.
> 
> 2. PASO INDUCTIVO:
>    - Hipótesis inductiva: Suponer que S(n) es verdadera para algún n ∈ ℕ.
>    - Meta: Demostrar que S(n+1) es verdadera.
>    - Usar la hipótesis inductiva para llegar a S(n+1).
> 
> 3. CONCLUSIÓN: Por el principio de inducción, S(n) es verdadera ∀n ∈ ℕ.
> ```

---

## 📝 Ejemplos (Inducción Simple)

> [!example]- 📝 Ejemplo 1 — Suma de los primeros $n$ impares
> 
> **Teorema:** $1 + 3 + 5 + \cdots + (2n-1) = n^2$, para todo $n \in \mathbb{N}$.
> 
> **Demostración:**
> 
> Sea $t_n = 1 + 3 + \cdots + (2n-1)$ y $S(n) : t_n = n^2$.
> 
> **Paso base:** $S(1) : t_1 = 1 = 1^2$ ✅
> 
> **Paso inductivo:** Supongamos que $S(n)$ es verdadera para algún $n \in \mathbb{N}$, es decir, $t_n = n^2$. Probemos que $S(n+1)$ es verdadera:
> 
> $$t_{n+1} = 1 + 3 + \cdots + (2n-1) + (2(n+1)-1)$$
> 
> $$= t_n + 2(n+1) - 1$$
> 
> $$= n^2 + 2(n+1) - 1 \quad \text{(por hipótesis inductiva)}$$
> 
> $$= n^2 + 2n + 1$$
> 
> $$= (n+1)^2$$
> 
> Así, $S(n+1)$ es verdadera. Por el principio de inducción, $S(n)$ es verdadera para todo $n \in \mathbb{N}$. $\blacksquare$

---

## 📐 Principio Fuerte de Inducción Matemática

> [!note]- 📖 Principio Fuerte de Inducción
> 
> Sea $n_0 \in \mathbb{Z}$ y $S(n)$ una función proposicional con dominio de discurso el conjunto de enteros mayores o iguales que $n_0$. Suponga que:
> 
> 1. $S(n_0)$ es verdadera, **y**
> 2. Para todo $n > n_0$, si $S(k)$ es verdadera para **todos** los $k$ satisfaciendo $n_0 \leq k < n$, entonces $S(n)$ es verdadera.
> 
> Entonces $S(n)$ es verdadera **para todo entero $n \geq n_0$**.
> 
> > ⚠️ Las dos formas de inducción matemática son **lógicamente equivalentes**.
> 
> **¿Cuándo usar la forma fuerte?**
> Se usa cuando para demostrar $S(n)$ necesitamos información de **varios predecesores** de $n$, no solo del anterior $S(n-1)$.

---

## 🔧 Estructura de la Inducción Fuerte

> [!tip]- ⚙️ Pasos a seguir
> 
> ```
> 1. PASO BASE:   Verificar S(n₀).
> 
> 2. PASO INDUCTIVO:
>    - Hipótesis inductiva (fuerte): Suponer que S(k) es verdadera
>      para todo k con n₀ ≤ k < n (no solo para n-1).
>    - Meta: Demostrar que S(n) es verdadera.
>    - Usar la hipótesis para cualquier predecesor que se necesite.
> 
> 3. CONCLUSIÓN: Por el principio fuerte de inducción, S(n) es verdadera ∀n ≥ n₀.
> ```

---

## 🧮 Definición Auxiliar — Función Piso

> [!note]- 📖 Definición — Función Piso $\lfloor x \rfloor$
> 
> Dado $x \in \mathbb{R}$, llamaremos **Piso** de $x$, denotado $\lfloor x \rfloor$, al **mayor entero que es menor o igual a $x$**.
> 
> **Ejemplos:**
> 
> | Expresión | Valor |
> |:---:|:---:|
> | $\lfloor 4/3 \rfloor$ | $1$ |
> | $\lfloor 0.999 \rfloor$ | $0$ |
> | $\lfloor -2 \rfloor$ | $-2$ |
> | $\lfloor 4 \rfloor$ | $4$ |

---

## 📝 Ejemplos (Inducción Fuerte)

> [!example]- 📝 Ejemplo 2 — Lista recursiva con función piso
> 
> Sea $C_n$ una lista de números definida por:
> $$C_1 = 0 \qquad \text{y} \qquad C_n = C_{\lfloor n/2 \rfloor} + n, \quad \forall n > 1$$
> 
> **Teorema:** $C_n < 4n$, $\forall n \geq 1$.
> 
> **Demostración:**
> 
> **Paso base:** $C_1 = 0 < 4 \cdot 1$ ✅
> 
> Verificamos algunos términos adicionales:
> 
> | $n$ | $C_n$ | $4n$ | ¿$C_n < 4n$? |
> |:---:|:---:|:---:|:---:|
> | 1 | 0 | 4 | ✅ |
> | 2 | $C_1 + 2 = 2$ | 8 | ✅ |
> | 3 | $C_1 + 3 = 3$ | 12 | ✅ |
> | 4 | $C_2 + 4 = 6$ | 16 | ✅ |
> | 5 | $C_2 + 5 = 7$ | 20 | ✅ |
> 
> **Paso inductivo (inducción fuerte):**
> 
> Dado $n > 1$, supongamos que $C_k < 4k$ para todo $1 \leq k < n$ *(hipótesis inductiva fuerte)*.
> 
> Sabemos que $1 \leq \lfloor n/2 \rfloor \leq n/2 < n$ ya que $n > 1$.
> 
> Tomando $k = \lfloor n/2 \rfloor$ tenemos que $1 \leq k < n$, por lo que por la hipótesis inductiva:
> 
> $$C_{\lfloor n/2 \rfloor} = C_k < 4k = 4\lfloor n/2 \rfloor$$
> 
> Entonces:
> 
> $$C_n = C_{\lfloor n/2 \rfloor} + n < 4\lfloor n/2 \rfloor + n \leq 4\cdot\frac{n}{2} + n = 2n + n = 3n < 4n$$
> 
> Concluimos que $C_n < 4n$, $\forall n \geq 1$, por el **principio fuerte de inducción matemática**. $\blacksquare$

---

## 📊 Comparación: Inducción Simple vs. Fuerte

> [!success]- 🗂️ ¿Cuándo usar cada una?
> 
> | Aspecto | Inducción Simple | Inducción Fuerte |
> |---|---|---|
> | **Hipótesis** | $S(n)$ es verdadera | $S(k)$ es verdadera para todo $k < n$ |
> | **Uso** | Basta con el paso anterior | Se necesitan varios predecesores |
> | **Ejemplos típicos** | Fórmulas de sumas, potencias | Recursiones, secuencias tipo $C_{\lfloor n/2 \rfloor}$ |
> | **Equivalencia** | Ambas son lógicamente equivalentes | ✅ |
> ![[file_00000000f17c71fba96939a05e098492.png]]

---

## 🏋️ Ejercicios Propuestos

> [!question]- 📋 Ejercicios de la clase
> 
> **Inducción simple:**
> 
> **1.** Demuestre que $8 \cdot 7^n - 3 \cdot 2^n$ es divisible por 5, $\forall n \in \mathbb{N}$.
> 
> **2.** Demuestre que si $a \in \mathbb{R}$ y $r \neq 1$, entonces:
> $$a + ar + ar^2 + \cdots + ar^n = a\,\frac{1 - r^{n+1}}{1 - r}, \quad \forall n \geq 0 \quad \text{(Suma geométrica)}$$
> 
> **3.** Use la suma geométrica para demostrar que si $0 < r < 1$ entonces:
> $$r^0 + r + r^2 + \cdots + r^n < \frac{1}{1-r}, \quad \forall n \geq 0$$
> 
> **4.** Usando el ejercicio anterior, demuestre que si $0 < r < 1$ entonces:
> $$1 \cdot r + 2 \cdot r^2 + \cdots + n \cdot r^n < \frac{r}{(1-r)^2}, \quad \forall n \in \mathbb{N}$$
> 
> ---
> 
> **Inducción fuerte:**
> 
> **5.** Demuestre que cualquier grupo con al menos 6 estudiantes se puede dividir en subgrupos de 3 o 4 estudiantes.
> 
> **6.** Sea $C_n$ definida por $C_1 = 0$ y $C_n = 4C_{\lfloor n/2 \rfloor} + n$, $\forall n > 1$. Demuestre que $C_n \leq 4(n-1)^2$, $\forall n \geq 1$.
> 
> **7.** Sea $C_n$ definida por $C_1 = 1$, $C_2 = 5$, $C_3 = 7$ y $C_n = 4C_{n-1} - C_{n-2} - 6C_{n-3}$, $\forall n \geq 4$. Encuentre una fórmula para $C_n$ y demuéstrela por inducción.

---

## 📊 Resumen Visual

```mermaid
graph TD
    A[Proposición S n<br/>para todo n ∈ ℕ] --> B{¿Qué forma de inducción?}

    B --> C[Inducción Simple<br/>Hipótesis: S n verdadera]
    B --> D[Inducción Fuerte<br/>Hipótesis: S k verdadera ∀ k menor que n]

    C --> E[Paso base: S 1 verdadera]
    C --> F[Paso inductivo: S n → S n+1]

    D --> G[Paso base: S n₀ verdadera]
    D --> H[Paso inductivo: S k para k menor que n → S n]

    E --> I[✅ S n verdadera para todo n]
    F --> I
    G --> I
    H --> I

    style A fill:#1e3a5f,color:#fff
    style B fill:#4a2d6a,color:#fff
    style I fill:#2d6a4f,color:#fff
```

---

**Tags:** #matematicas-discretas #induccion-matematica #induccion-fuerte #demostraciones #recursion #MATG1051

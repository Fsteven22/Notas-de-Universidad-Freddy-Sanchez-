# 🔢 Sucesiones y Cadenas

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las sucesiones y cadenas?
> 
> Las **sucesiones** son un caso especial de función: asignan a cada entero en un rango dado un elemento de algún conjunto. Las **cadenas** son sucesiones finitas de elementos, con la diferencia de que el orden importa y las repeticiones se permiten.
> 
> ```mermaid
> graph TD
>     A[Función f : X → Y] --> B[Sucesión s : A → X]
>     B --> C[A es conjunto de enteros consecutivos]
>     B --> D[Finita si A es finito]
>     B --> E[Infinita si A es infinito]
>     D --> F[Cadena sobre X]
>     style A fill:#e1f5ff
>     style B fill:#1e3a5f,color:#fff
>     style F fill:#f5e1ff
> ```

---

## 📋 Sucesiones

> [!note]- 📋 Definición 5 — Sucesión
> 
> Sea $X$ un conjunto. Una **sucesión en** $X$ es cualquier función $s : A \to X$, donde $A$ es un conjunto de **enteros consecutivos**.
> 
> - Al elemento $s(n)$ lo denotaremos $s_n$ y lo llamaremos el **$n$-ésimo término** de la sucesión.
> - A $n$ se le llama **índice** de la sucesión.
> - Si $s : A \to X$ es una sucesión, la denotaremos por ${s_n}$ o ${s_n}_{n \in A}$.

> [!note]- 📋 Definición 6 — Sucesión finita e infinita
> 
> - Una sucesión es **finita** si su dominio es finito.
> - Una sucesión es **infinita** si su dominio es infinito.
> 
> Si $s$ es una sucesión infinita con índice inicial $k$:
> 
> $${s_n}_{n=k}^{\infty}$$
> 
> Una sucesión finita $x$ indexada desde $i$ hasta $j$:
> 
> $${x_n}_{n=i}^{j}$$
> 
> > [!tip]- 💡 Ejemplo de notación
> > 
> > Una sucesión $t$ cuyo dominio es ${-1, 0, 1, 2, 3}$ se denota ${t_n}_{n=-1}^{3}$.

---

## 🧮 Ejemplos de Sucesiones

> [!example]- 📝 Ejemplo 17 — Sucesiones básicas
> 
> **Sucesión $s$:** $2, 4, 6, \ldots$ con primer índice $1$:
> 
> $$s_1 = 2,\quad s_2 = 4,\quad \ldots,\quad s_n = 2n$$
> 
> **Sucesión $t$:** $a, a, b, a, a$ con primer índice $1$:
> 
> $$t_1 = a,\quad t_2 = a,\quad t_3 = b,\quad t_4 = a,\quad t_5 = a$$

> [!example]- 📝 Ejemplo 18 — Sucesión finita
> 
> Sea $x$ la sucesión dada por $x_n = \dfrac{1}{2^n}$, para $-1 \leq n \leq 4$.
> 
> Los elementos de $x$ son:
> 
> $$x_{-1} = 2,\quad x_0 = 1,\quad x_1 = \tfrac{1}{2},\quad x_2 = \tfrac{1}{4},\quad x_3 = \tfrac{1}{8},\quad x_4 = \tfrac{1}{16}$$

---

## ∑ Suma y Producto de Sucesiones

> [!note]- ∑ Definición 9 — Notación de suma y producto
> 
> Sea ${a_i}_{i=m}^{n}$ una sucesión. Se definen:
> 
> **Suma:**
> 
> $$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + \cdots + a_n$$
> 
> **Producto:**
> 
> $$\prod_{i=m}^{n} a_i = a_m \cdot a_{m+1} \cdots a_n$$
> 
> A $m$ se le llama **límite inferior** y a $n$ **límite superior**.
> 
> En general, si $S$ es un conjunto finito de enteros y $a$ es una sucesión:
> 
> $$\sum_{i \in S} a_i \quad \text{denota la suma de } {a_i : i \in S}$$
> 
> $$\prod_{i \in S} a_i \quad \text{denota el producto de } {a_i : i \in S}$$

> [!example]- 📝 Ejemplo 21
> 
> Sea $a$ la sucesión definida por $a_n = 2n$, $n \geq 1$:
> 
> $$\sum_{i=1}^{3} a_i = a_1 + a_2 + a_3 = 2 + 4 + 6 = 12$$
> 
> $$\prod_{i=1}^{3} a_i = a_1 \cdot a_2 \cdot a_3 = 2 \cdot 4 \cdot 6 = 48$$

> [!example]- 📝 Ejemplo 22 — Suma geométrica
> 
> La suma geométrica $a + ar + ar^2 + \cdots + ar^n$ se escribe:
> 
> $$\sum_{i=0}^{n} ar^i$$

---

## 🔤 Cadenas

> [!note]- 📋 Definición 10 — Cadena
> 
> Sea $X$ un conjunto. Una **cadena sobre** $X$ es una **sucesión finita** de elementos en $X$.
> 
> **Notación y convenciones:**
> 
> - Si $s_1 = b,\ s_2 = a,\ s_3 = a,\ s_4 = c$, la cadena se denota $baac$.
> - El **orden importa**: la cadena $baac$ es diferente a $abac$.
> - Las **repeticiones** se expresan con superíndices: $bbaaac = b^2a^3c$.
> - La **cadena nula** (sin elementos) se denota $\lambda$.
> - $X^*$ denota el conjunto de **todas** las cadenas sobre $X$.
> - $X^+$ denota el conjunto de las cadenas **no nulas** sobre $X$.

> [!note]- 📋 Longitud y Concatenación
> 
> Sea $\alpha$ una cadena sobre $X$:
> 
> - La **longitud** de $\alpha$, denotada $|\alpha|$, es el número de elementos en $\alpha$.
>     
> - Si $\alpha$ y $\beta$ son cadenas, la cadena $\alpha\beta$ (primero $\alpha$, luego $\beta$) se llama **concatenación** de $\alpha$ y $\beta$.
>     
> - Una cadena $\beta$ es **subcadena** de $\alpha$ si existen cadenas $\gamma$ y $\delta$ tal que $\alpha = \gamma\beta\delta$.
>     
> 
> > [!tip]- 💡 Propiedades de la longitud
> > 
> > - $|\lambda| = 0$
> > - $|\alpha\beta| = |\alpha| + |\beta|$

---

## 🧮 Ejemplos de Cadenas

> [!example]- 📝 Ejemplo 23 — Cadena sobre un conjunto
> 
> Sea $X = {a, b, c}$. Si hacemos $s_1 = b,\ s_2 = a,\ s_3 = a,\ s_4 = c$, obtenemos la cadena $baac$.
> 
> **Ejemplos adicionales:**
> 
> - $baac \neq abac$ (el orden importa)
> - $bbaaac = b^2a^3c$ (notación con superíndices)
> - $|baac| = 4$
> - $|b^2a^3c| = 6$
> - Concatenación: si $\alpha = ab$ y $\beta = ca$, entonces $\alpha\beta = abca$ con $|\alpha\beta| = 4$
> - $ca$ es subcadena de $bca$ (con $\gamma = b$ y $\delta = \lambda$)

---

## 📊 Resumen Visual

```mermaid
graph TD
    A[Sucesiones y Cadenas] --> B[Sucesión s : A → X]
    A --> C[Cadena sobre X]
    B --> D[Finita: dominio finito]
    B --> E[Infinita: dominio infinito]
    B --> F["Suma: Σ aᵢ"]
    B --> G["Producto: Π aᵢ"]
    C --> H[Sucesión finita de elementos]
    C --> I["Longitud |α|"]
    C --> J[Concatenación αβ]
    C --> K["Cadena nula λ"]

    style A fill:#1e3a5f,color:#fff
    style B fill:#e1f5ff
    style C fill:#f5e1ff
    style F fill:#e1ffe1
    style G fill:#e1ffe1
```

---

## 📝 Ejercicios Propuestos

> [!question]- 📋 Ejercicios
> 
> **1.** Sea $a_n = 3n - 1$, $1 \leq n \leq 5$. Calcula $\displaystyle\sum_{i=1}^{5} a_i$ y $\displaystyle\prod_{i=1}^{4} a_i$.
> 
> **2.** Sea $X = {0, 1}$ (alfabeto binario). Escribe todas las cadenas de longitud 2 en $X$. ¿Cuántas hay de longitud $n$?
> 
> **3.** Sea $\alpha = a^2b$ y $\beta = ba^3$. Calcula $\alpha\beta$, $\beta\alpha$, $|\alpha\beta|$ y verifica que $\alpha\beta \neq \beta\alpha$.
> 
> **4.** Indica si $ab$ es subcadena de $cab$, $aab$, $ba$.

> [!success]- ✅ Respuestas
> 
> **1.** $a_1=2,\ a_2=5,\ a_3=8,\ a_4=11,\ a_5=14$. $\sum = 2+5+8+11+14 = 40$. $\prod = 2 \cdot 5 \cdot 8 \cdot 11 = 880$.
> 
> **2.** Cadenas de longitud 2: ${00, 01, 10, 11}$ — hay $4 = 2^2$ cadenas. En general, hay $2^n$ cadenas de longitud $n$.
> 
> **3.** $\alpha\beta = a^2b \cdot ba^3 = a^2b^2a^3$, longitud $|\alpha\beta| = 2+2+3 = 7$. $\beta\alpha = ba^3 \cdot a^2b = ba^5b$, longitud $7$. $a^2b^2a^3 \neq ba^5b$, por lo tanto $\alpha\beta \neq \beta\alpha$. ✅
> 
> **4.**
> 
> - $cab$: ✅ $ab$ es subcadena ($\gamma = c$, $\delta = \lambda$).
> - $aab$: ✅ $ab$ es subcadena ($\gamma = a$, $\delta = \lambda$).
> - $ba$: ❌ $ab$ no es subcadena de $ba$.

---

**Tags:** #matematicas-discretas #conjuntos #sucesiones #cadenas #notacion-suma #MATG1051
---
dg-publish: true
---

# 🧾 Demostraciones

## 🎯 Introducción

> [!info] 💡 ¿Qué es una demostración matemática?
> 
> Una **demostración** es un argumento lógico riguroso que establece la verdad de una proposición a partir de **axiomas**, **definiciones** y **resultados previamente probados**.
> 
> A diferencia de las demostraciones algebraicas (que manipulan equivalencias lógicas paso a paso), aquí se trabaja con proposiciones matemáticas del mundo real: propiedades de enteros, desigualdades, existencia de objetos, etc.
>
> ```mermaid
> graph TD
>     A["¿Qué quieres probar?"] --> B{"¿Forma del enunciado?"}
>     B -->|"Si P entonces Q"| C["Directa: supone P, llega a Q"]
>     B -->|"No Q → No P"| D["Contrapositiva / Contradicción"]
>     B -->|"Existe x tal que..."| E["Constructiva: exhibe el x"]
>     B -->|"Para todo n..."| F["Inducción"]
>     style A fill:#e1f5ff
> ```
>
> **En esta nota:** vocabulario (axioma, teorema, lema, corolario), estructura de teorema, métodos directo/indirecto/contradicción/constructivo y cómo elegir método según la forma del enunciado.
>

---

## 📚 Vocabulario Matemático Fundamental

> [!note] 📖 Definición 5 — Términos esenciales
> 
> | Término | Definición |
> |---|---|
> | **Axioma** | Resultado que se supone **verdadero sin necesidad de demostrarlo**. Es el punto de partida de toda la teoría. |
> | **Teorema** | Proposición que se ha **probado que es verdadera** a partir de axiomas y resultados previos. |
> | **Lema** | Teorema auxiliar que **por sí mismo no es interesante**, pero resulta útil para probar otro teorema más importante. |
> | **Corolario** | Teorema que es **consecuencia inmediata** de otro teorema ya demostrado. |
> | **Demostración / Prueba** | Argumento lógico que **establece la veracidad** de un teorema. |

---


> [!note] 📐 Mapa — Vocabulario de demostración
>
> ```mermaid
> graph TD
>     A["Axioma<br/>se asume"] --> T["Teorema<br/>se prueba"]
>     T --> L["Lema<br/>auxiliar"]
>     T --> C["Corolario<br/>consecuencia"]
>     style A fill:#fff4e1
>     style T fill:#e1ffe1
> ```
>
> **Se lee así:** todo nace de axiomas; el teorema es la meta, el lema el andamio, el corolario el regalo.

## 📐 Estructura General de un Teorema

> [!note] 📋 Forma estándar
> 
> La mayoría de los teoremas tienen la siguiente forma:
> 
> > [!example] 🟢 Ejemplo
> >
> > "Para todo $x_1, x_2, \ldots, x_n$, **si** $p(x_1, \ldots, x_n)$ **entonces** $q(x_1, \ldots, x_n)$."
> 
> Esta es una proposición **cuantificada universalmente**, y es verdadera si:
> 
> $$p(x_1,\ldots,x_n) \to q(x_1,\ldots,x_n) \quad \text{es verdadera para todo } x_1,\ldots,x_n \text{ en el dominio}$$
> 
> **Clave:** Para demostrarla, solo necesitamos considerar el caso en que $p$ es **verdadera**, pues cuando $p$ es **falsa**, el condicional es **verdadero por omisión**.

---

## 🔢 Definición de Paridad

> [!note] 📖 Definición 6 — Números Pares e Impares
> 
> Sea $n$ un número entero:
> 
> - $n$ es **par** si existe un entero $k$ tal que $n = 2k$.
> - $n$ es **impar** si existe un entero $k$ tal que $n = 2k + 1$.
> 
> > [!example] 🟢 Ejemplo
> >
> > Todo número entero es par **o** impar, y nunca ambos a la vez.
> 
> Esta definición es la base de muchos ejemplos de demostración.

---

## 🎯 Técnica 1 — Prueba Directa

> [!tip] ⚙️ ¿En qué consiste?
> 
> Se **supone que $p$ es verdadera** y, mediante razonamiento lógico usando axiomas, definiciones y teoremas previos, se **concluye que $q$ es verdadera**.
> 
> ```
> Hipótesis p  →  razonamiento  →  Conclusión q
> ```

> [!example] 📝 Ejemplo 12 — Suma de impar y par es impar
> 
> **Teorema:** Para cualesquiera enteros $m$ y $n$, si $m$ es impar y $n$ es par, entonces $m + n$ es impar.
> 
> **Demostración directa:**
> 
> Sean $m, n \in \mathbb{Z}$ arbitrarios. Supongamos que $m$ es impar y $n$ es par.
> 
> Por definición:
> - $\exists\, k_1 \in \mathbb{Z}$ tal que $m = 2k_1 + 1$
> - $\exists\, k_2 \in \mathbb{Z}$ tal que $n = 2k_2$
> 
> Entonces:
> $$m + n = (2k_1 + 1) + 2k_2 = 2k_1 + 2k_2 + 1 = 2(k_1 + k_2) + 1$$
> 
> Haciendo $k = k_1 + k_2 \in \mathbb{Z}$, se tiene $m + n = 2k + 1$, es decir, $m + n$ es **impar**. $\blacksquare$

> [!example] 📝 Ejemplo 15 — El cuadrado de un impar es impar
> 
> **Teorema:** Para todo entero $m$, si $m$ es impar entonces $m^2$ es impar.
> 
> **Demostración directa:**
> 
> Si $m$ es impar, existe $k \in \mathbb{Z}$ tal que $m = 2k + 1$. Entonces:
> 
> $$m^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
> 
> Haciendo $n = 2k^2 + 2k \in \mathbb{Z}$, se tiene $m^2 = 2n + 1$, es decir, $m^2$ es **impar**. $\blacksquare$

---

## 🔁 Técnica 2 — Prueba por Contradicción

> [!tip] ⚙️ ¿En qué consiste?
> 
> También llamada **prueba indirecta**. Para demostrar $p \to q$:
> 
> 1. Se supone que $p \to q$ es **falsa**, es decir, que $p \wedge \neg q$ es verdadera.
> 2. Se razona hasta llegar a una **contradicción** de la forma $r \wedge \neg r$.
> 3. La contradicción muestra que la suposición era imposible, por tanto $p \to q$ es **verdadera**.
> 
> ```
> Suponer: p ∧ ¬q  →  razonamiento  →  r ∧ ¬r  (contradicción)
>                                        ↓
>                              p → q es verdadera ✅
> ```

> [!example] 📝 Ejemplo 13 — Prueba por contradicción
> 
> **Teorema:** Para todos $x, y \in \mathbb{R}$, si $x + y \geq 2$ entonces $x \geq 1$ o $y \geq 1$.
> 
> **Demostración por contradicción:**
> 
> Sean $x, y \in \mathbb{R}$ arbitrarios. Supongamos que:
> - $p$: $x + y \geq 2$ es **verdadera**, y
> - $q$: $x \geq 1$ o $y \geq 1$ es **falsa**.
> 
> Como $q$ es falsa, por las Leyes de De Morgan:
> $$\neg(x \geq 1 \vee y \geq 1) \equiv x < 1 \wedge y < 1$$
> 
> Entonces $x < 1$ y $y < 1$, lo que implica:
> $$x + y < 1 + 1 = 2$$
> 
> Pero habíamos supuesto $x + y \geq 2$. Tenemos:
> $$(x + y \geq 2) \wedge (x + y < 2) \quad \longrightarrow \quad \text{contradicción!}$$
> 
> Por lo tanto la proposición es **verdadera**. $\blacksquare$

---

## 🔂 Técnica 3 — Prueba por Contrarrecíproco

> [!tip] ⚙️ ¿En qué consiste?
> 
> Es un caso especial de la prueba por contradicción, basado en la equivalencia:
> 
> $$p \to q \equiv \neg q \to \neg p$$
> 
> En lugar de demostrar $p \to q$, se demuestra su contrarrecíproco $\neg q \to \neg p$:
> 
> 1. Se supone que $q$ es **falsa** ($\neg q$ verdadera).
> 2. Se deduce que $p$ es **falsa** ($\neg p$ verdadera).
> 
> ```
> Suponer: ¬q  →  razonamiento  →  ¬p
>                                    ↓
>                         p → q es verdadera ✅
> ```

> [!example] 📝 Ejemplo 14 — Prueba por contrarrecíproco
> 
> **Teorema:** Para todo entero $m$, si $m^2$ es impar entonces $m$ es impar.
> 
> **Demostración por contrarrecíproco:**
> 
> Debemos demostrar: si $m$ **no** es impar (es par), entonces $m^2$ **no** es impar (es par).
> 
> Supongamos que $m$ es **par**. Entonces $\exists\, k \in \mathbb{Z}$ tal que $m = 2k$.
> 
> $$m^2 = (2k)^2 = 4k^2 = 2(2k^2)$$
> 
> Haciendo $n = 2k^2 \in \mathbb{Z}$, se tiene $m^2 = 2n$, es decir, $m^2$ es **par**.
> 
> Hemos demostrado $\neg q \to \neg p$, equivalente a $p \to q$. $\blacksquare$

> [!success] ⭐ Corolario — Equivalencia del cuadrado
> 
> Combinando los Ejemplos 14 y 15 (usando contrarrecíproco):
> 
> > [!example] 🟢 Ejemplo
> >
> > **Para todo entero $m$: $m^2$ es impar $\Leftrightarrow$ $m$ es impar.**
> 
> Y aplicando la ley del contrarrecíproco:
> 
> > [!example] 🟢 Ejemplo
> >
> > **Para todo entero $m$: $m^2$ es par $\Leftrightarrow$ $m$ es par.**

---

## 📚 Técnica 4 — Prueba por Casos

> [!tip] ⚙️ ¿En qué consiste?
> 
> Se emplea cuando la hipótesis se divide en **casos exhaustivos y excluyentes** de manera natural. Si $p \equiv p_1 \vee p_2 \vee \cdots \vee p_n$, entonces:
> 
> $$p \to q \equiv (p_1 \to q) \wedge (p_2 \to q) \wedge \cdots \wedge (p_n \to q)$$
> 
> Se demuestra **cada caso por separado** y se concluye que $p \to q$ es verdadera.
> 
> ```
> Caso 1: p₁ → q  ✅
> Caso 2: p₂ → q  ✅
>     ...
> Caso n: pₙ → q  ✅
>          ↓
>    p → q verdadera ✅
> ```

> [!example] 📝 Ejemplo 16a — $|x| = |-x|$
> 
> **Teorema:** $\forall x \in \mathbb{R} : |x| = |-x|$
> 
> **Demostración por casos:**
> 
> **Caso 1:** $x \geq 0$.
> Entonces $|x| = x$ y $|-x| = -(-x) = x$. Por lo tanto $|x| = |-x|$. ✅
> 
> **Caso 2:** $x < 0$.
> Entonces $|x| = -x$ y como $-x > 0$, se tiene $|-x| = -x$. Por lo tanto $|x| = |-x|$. ✅
> 
> En ambos casos se cumple. $\blacksquare$

> [!example] 📝 Ejemplo 16b — $x \leq |x|$
> 
> **Teorema:** $\forall x \in \mathbb{R} : x \leq |x|$
> 
> **Demostración por casos:**
> 
> **Caso 1:** $x \geq 0$.
> Entonces $|x| = x$, por lo tanto $x = |x|$, es decir $x \leq |x|$. ✅
> 
> **Caso 2:** $x < 0$.
> Entonces $|x| = -x > 0 > x$, por lo tanto $x < |x|$. ✅
> 
> En ambos casos $x \leq |x|$. $\blacksquare$

> [!example] 📝 Ejemplo 16c — Desigualdad Triangular $|x+y| \leq |x| + |y|$
> 
> **Teorema:** $\forall x, y \in \mathbb{R} : |x + y| \leq |x| + |y|$
> 
> **Demostración por casos** (según los signos de $x$ y $y$):
> 
> **Caso 1:** $x \geq 0$ y $y \geq 0$.
> $x + y \geq 0$, entonces $|x+y| = x+y = |x|+|y|$. ✅
> 
> **Caso 2:** $x < 0$ y $y < 0$.
> $x + y < 0$, entonces $|x+y| = -(x+y) = (-x)+(-y) = |x|+|y|$. ✅
> 
> **Caso 3:** $x \geq 0$ y $y < 0$ (el caso $x < 0$, $y \geq 0$ es simétrico).
> Si $x + y \geq 0$: $|x+y| = x+y \leq x + |y| = |x|+|y|$. ✅
> Si $x + y < 0$: $|x+y| = -(x+y) \leq -y = |y| \leq |x|+|y|$. ✅
> 
> En todos los casos $|x+y| \leq |x|+|y|$. $\blacksquare$

> [!example] 📝 Ejemplo 16d — Fórmulas del máximo y mínimo
> 
> **Teoremas:**
> 
> $$\forall x, y \in \mathbb{R} : \max\{x, y\} = \frac{x + y + |x - y|}{2}$$
> 
> $$\forall x, y \in \mathbb{R} : \min\{x, y\} = \frac{x + y - |x - y|}{2}$$
> 
> **Demostración del máximo por casos:**
> 
> **Caso 1:** $x \geq y$ → $x - y \geq 0$, entonces $|x-y| = x-y$.
> $$\frac{x+y+(x-y)}{2} = \frac{2x}{2} = x = \max\{x,y\}$$ ✅
> 
> **Caso 2:** $x < y$ → $x - y < 0$, entonces $|x-y| = -(x-y) = y-x$.
> $$\frac{x+y+(y-x)}{2} = \frac{2y}{2} = y = \max\{x,y\}$$ ✅
> 
> 
> 
> 
> 
**Demostración del mínimo por casos:**
> 
**Caso 1:** $x \geq y \Rightarrow x - y \geq 0$, entonces $|x - y| = x - y$.
> 
$$\frac{x + y - (x - y)}{2} = \frac{2y}{2} = y = \min\{x, y\} \checkmark$$
> 
**Caso 2:** $x < y \Rightarrow x - y < 0$, entonces $|x - y| = -(x-y) = y - x$.
> 
$$\frac{x + y - (y - x)}{2} = \frac{2x}{2} = x = \min\{x, y\} \checkmark$$
> 
> 
> 
> 
La lógica es simétrica a la del máximo: en cada caso, al restar $|x-y|$ en lugar de sumarlo, "cancela" el mayor y deja el menor.

---

## 📊 Comparación de Técnicas

> [!success] 🗂️ ¿Cuándo usar cada técnica?
> 
> | Técnica | ¿Cuándo usarla? | Estructura |
> |---|---|---|
> | **Prueba Directa** | La conclusión fluye naturalmente de la hipótesis | $p \Rightarrow \cdots \Rightarrow q$ |
> | **Por Contradicción** | Difícil trabajar directo; útil con "no existe" | Suponer $p \wedge \neg q$, llegar a $r \wedge \neg r$ |
> | **Por Contrarrecíproco** | Más fácil probar $\neg q \to \neg p$ que $p \to q$ | Suponer $\neg q$, demostrar $\neg p$ |
> | **Por Casos** | La hipótesis tiene subcasos naturales (par/impar, positivo/negativo...) | Demostrar $p_i \to q$ para cada $i$ |

---

## 🔗 Base Lógica de cada Técnica

> [!note] 📋 Fundamento en el [[01 - Algebra de Proposiciones|álgebra de proposiciones]]
> 
> Cada técnica se apoya en una equivalencia lógica ya demostrada:
> 
> | Técnica | Equivalencia que la justifica |
> |---|---|
> | Prueba directa | El condicional es vacuamente V cuando $p$ es F |
> | Por contradicción | $(p \to q) \equiv \neg(p \wedge \neg q)$ |
> | Por contrarrecíproco | $(p \to q) \equiv (\neg q \to \neg p)$ |
> | Por casos | $(p_1 \vee p_2) \to q \equiv (p_1 \to q) \wedge (p_2 \to q)$ |
> | Uso de De Morgan | $\neg(p \vee q) \equiv \neg p \wedge \neg q$ |

---

## 📝 Ejercicios Propuestos (Guía 1)

> [!example] ✏️ Ejercicio 1 — Prueba directa con divisibilidad (Guía 1, ej. 18)
>
> Demuestra por prueba directa: si $2 \mid n^2-1$, entonces $4 \mid n^2-1$.
>
> > [!success]- ✅ Solución guiada
> >
> > Si $2 \mid n^2-1$, entonces $n^2-1$ es par, luego $n^2$ es impar y por tanto $n$ es impar: $n = 2k+1$ para algún $k \in \mathbb{Z}$. Entonces $n^2-1 = (2k+1)^2-1 = 4k^2+4k = 4k(k+1)$, múltiplo de $4$. ∎ Directa pura: suponer el antecedente y construir el consecuente.

> [!example] ✏️ Ejercicio 2 — Elige la técnica (de la clase)
>
> Para cada enunciado, di qué técnica usarías y por qué:
>
> - (a) "Si $n^2$ es par, $n$ es par"
> - (b) "$\sqrt{2}$ es irracional"
> - (c) "Todo entero $n \geq 8$ se escribe como $3a+5b$"
> - (d) "$|x\cdot y| = |x|\cdot|y|$ para $x, y \in \mathbb{R}$"
>
> > [!success]- ✅ Solución guiada
> >
> > - (a) **Contrarrecíproco**: "si $n$ es impar, $n^2$ es impar" sale directo ($n = 2k+1$).
> > - (b) **Contradicción**: supone $\sqrt{2} = p/q$ irreducible y llega a $p$ y $q$ pares.
> > - (c) **Casos** (módulo 3: $n = 3k$, $3k+1$, $3k+2$ desde base $8, 9, 10$).
> > - (d) **Casos** por signos de $x$ e $y$.
> >
> > Regla: la forma del enunciado manda la técnica.

---

## ⚠️ Errores Comunes y Principios

> [!danger] ❌ Error 1: Contradicción sin negar la conclusión (viola **$(p \to q) \equiv \neg(p \wedge \neg q)$**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** suponer $p$ y derivar cualquier absurdo sin haber supuesto $\neg q$.
> - ✅ Así sí: supone $p \wedge \neg q$ completo y deriva la contradicción desde ahí.

> [!danger] ❌ Error 2: Contrarrecíproco sin negar (viola **$p \to q \equiv \neg q \to \neg p$**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** "probar" $q \to p$ creyendo que es el contrarrecíproco.
> - ✅ Así sí: niega **ambos** lados y voltea: parte de $\neg q$ y llega a $\neg p$.

> [!danger] ❌ Error 3: Casos que no cubren todo (viola **exhaustividad**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** probar par/impar pero olvidar el $0$, o cubrir $n > 0$ sin el $n = 0$.
> - ✅ Así sí: verifica que la unión de tus casos es todo el dominio antes de concluir.

---

## 📊 Resumen Visual

```mermaid
graph TD
    A[Teorema a demostrar p → q] --> B{¿Qué estrategia?}

    B --> C[Prueba Directa Suponer p, concluir q]
    B --> D[Por Contradicción Suponer p ∧ ¬q, llegar a r ∧ ¬r]
    B --> E[Por Contrarrecíproco Suponer ¬q, concluir ¬p]
    B --> F[Por Casos p₁∨p₂∨...∨pₙ → demostrar cada caso]

    C --> G[✅ Demostración completa]
    D --> G
    E --> G
    F --> G

```

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - Vocabulario: axioma (se asume), teorema (se prueba), lema (auxiliar), corolario (consecuencia inmediata).
> - 4 técnicas: directa (supón P, llega a Q), contradicción (supón $\neg$Q, absurdo), contrapositiva ($\neg Q \to \neg P$), casos (parte el dominio).
> - Elige por la forma: "existe" → constructiva; "para todo n" → inducción; "si...entonces" → directa o contrapositiva.

---

## 🏋️ Lección 1 (2026) — Conjuntos por comprensión

> [!example] ✏️ $A \subseteq B \cap C$ cazando elementos
>
> $A = \{n : n-4$ múltiplo de $12\}$, $B = \{n : $ múltiplo de $4\}$, $C = \{n : n+2$ múltiplo de $3\}$. Toma $x \in A$: $x-4 = 12k$, o sea $x = 12k+4 = 4(3k+1)$ → $x \in B$ ✅. Además $x+2 = 12k+6 = 3(4k+2)$ → $x \in C$ ✅. Como $x$ era arbitrario, $A \subseteq B \cap C$. ∎
>
> > [!success]- ✅ Qué mirar
> >
> > Prueba **directa** con elemento arbitrario + factorizar el número pedido ($4$ para B, $3$ para C) + cerradura de $\mathbb{Z}$ para nombrar el testigo ($m = 3k+1$).

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
>
> - [ ] Elijo la técnica (directa, contradicción, contrarrecíproco, casos) según el enunciado.
> - [ ] Ejecuto par/impar con prueba directa sin mirar.
> - [ ] Verifico que mis casos cubren todo el dominio.

> [!note] 🎯 Nivel Intermedio
>
> - [ ] Cito la equivalencia lógica que justifica cada técnica.
> - [ ] Reescribo una prueba por contradicción como contrarrecíproca y viceversa.

---

## 🔁 Repaso SR (flashcards)

#flashcards/discretas-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Axioma vs teorema vs lema vs corolario?::Asumido / probado / auxiliar / consecuencia inmediata.
> - ¿4 técnicas y cuándo?::Directa (P→Q), contradicción (¬Q→absurdo), contrapositiva, casos.
> - ¿"Existe x" se prueba cómo?::Constructiva: exhibiendo el x.
- ¿Lección 2026 conjuntos?::$A \subseteq B \cap C$ con $x = 12k+4$: factoriza $4$ (B) y $3$ de $x+2$ (C).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Matemáticas Discretas]]
> - Anterior: [[02 - Cuantificadores]] · Inducción: [[03 - Inducción Matemática]]
> - Reglas: [[01 - Reglas de Inferencia]]

---

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Rosen, *Discrete Mathematics and Its Applications* — cap. 1 (métodos de demostración).
> - Material de clase MATG1051: las 4 técnicas y paridad.

---

**Tags:** #matematicas-discretas #algebra-proposicional #demostraciones #prueba-directa #contradiccion #contrarreciproco #prueba-por-casos #axiomas #teoremas #MATG1051

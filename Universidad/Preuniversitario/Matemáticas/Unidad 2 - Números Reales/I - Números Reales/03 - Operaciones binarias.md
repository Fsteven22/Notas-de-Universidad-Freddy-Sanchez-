---
dg-publish: true
---

# ⚙️ Operaciones Binarias

## 🎯 Introducción

> [!info] 💡 ¿Qué es una operación binaria?
>
> $*:S\times S\to S$ (cerrada por definición): conmutativa, asociativa, neutro e inverso deciden la estructura (monoide, grupo, campo). $\mathbb{Z}_5$ es campo; $\mathbb{Z}_6$ no.
>
> ```mermaid
> graph LR
>     A["Cerrada<br/>SxS a S"] --> B["Asoc+neutro<br/>monoide"]
>     B --> C["Inverso<br/>grupo"]
>     C --> D["Conmuta<br/>abeliano"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[03-cayley.png]]

> [!tip] 💡 Visual — Tabla de Cayley
>
> La tabla muestra neutro (fila que repite) e inversos (dónde aparece $e$): en $\mathbb{Z}_5$ todo no-cero tiene inverso; en $\mathbb{Z}_6$ solo $1,5$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Propiedades y estructuras
>
> **Binaria:** $*:S\times S\to S$. **Propiedades:** cerradura, conmutativa ($a*b=b*a$), asociativa, neutro $e$, inverso $a^{-1}$.
>
> **Estructuras:** monoide (asoc+neutro), grupo (+inverso), abeliano (+conmuta), anillo, campo.

> [!tip] 💡 Cómo clasificar estructuras sin perderse
>
> Verifica en orden: cerrada → asociativa → neutro → inverso → conmutativa; el primer fallo dice la estructura. En $\mathbb{Z}_n$ los invertibles son los coprimos ($\text{MCD}=1$): $\mathbb{Z}_5$ campo, $\mathbb{Z}_6$ solo $1,5$ invertibles.

> [!example] 🟢 Ejemplo — $a\oplus b=2a+3b$ y $a*b=a+b+1$
>
> $1\oplus2=8\neq7=2\oplus1\therefore$ no conmutativa. $a*e=a+e+1=a\therefore e=-1$ (verifica $(-1)*a=a$ ✓).

---

## 📋 Tabla Comparativa: Estructuras

> [!note] 📋 Qué axiomas pide cada una
>
> | Estructura | Asoc. | Neutro | Inverso | Conm. |
> |---|---|---|---|---|
> | Monoide | ✓ | ✓ | — | — |
> | Grupo | ✓ | ✓ | ✓ | — |
> | Abeliano | ✓ | ✓ | ✓ | ✓ |
> | $(\mathbb{Z}_{12},+)$ | ✓ | $0$ | $n-a$ | ✓ |
> | $(\mathbb{Z}_5^*,\cdot)$ | ✓ | $1$ | $2^{-1}=3$ | ✓ |
>
> **Composición/matrices:** asociativas, no conmutativas ($2x+3\neq2x+6$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$-$ en $\mathbb{N}$ binaria:** $5-7\notin\mathbb{N}\therefore$ no cerrada.
> - **$\sqrt{\ }$ no cerrada en $\mathbb{R}^+$:** sí lo es ($\sqrt{x}>0$); falla en $\mathbb{R}$ ($-1$).
> - **Neutro a ojo:** despeja $a*e=a$ y verifica ambos lados.
> - **Conmutativa $\implies$ neutro:** $a*b=a$ es asociativa y conmutativa sin neutro.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. ¿Cerradas? $-$ en $\mathbb{N}$, $\div$ en $\mathbb{Z}$, $\cup$ en $\mathcal{P}(A)$, $\sqrt{\ }$ en $\mathbb{R}^+$.
> 2. ¿Conmutativa $a\oplus b=2a+3b$?
> 3. Neutro de $a*b=a+b+1$ en $\mathbb{Z}$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** No; no; sí; sí ($\sqrt{x}>0$).
>
> **2.** No ($8\neq7$).
>
> **3.** $e=-1$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $(a+b)/2$ en $\mathbb{Q}$: ¿asociativa?
> 5. Idempotentes de $a*b=a+b-ab$.
> 6. $f=2x$, $g=x+3$: $g\circ f$ vs $f\circ g$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** No ($3.5\neq3$).
>
> **5.** $a=0,1$ ($a(a-1)=0$).
>
> **6.** $2x+3$ vs $2x+6$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $(\mathbb{Z}_n,+_n)$ grupo abeliano.
> 8. Cerrada+asociativa+neutro pero no conmutativa en $\{0,1,2\}$.
> 9. ¿Cuántas operaciones binarias en $n$ elementos?

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Cerrada, asociativa, $e=0$, inverso $n-a$.
>
> **8.** $e=0$; $1\cdot2=1$, $2\cdot1=2$ (verifica asociatividad caso por caso).
>
> **9.** $n^{n^2}$ ($n^2$ pares, $n$ valores cada uno).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Decido cerradura con contraejemplos.
> - [ ] Pruebo conmutatividad con un par.
> - [ ] Despejo neutros e inversos.
> - [ ] Leo tablas de Cayley.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Refuto asociatividad con tríos.
> - [ ] Hallo idempotentes resolviendo.
> - [ ] Clasifico $\mathbb{Z}_n$ aditivos.
> - [ ] Comparo composiciones.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro grupos $\mathbb{Z}_n$.
> - [ ] Construyo tablas no conmutativas.
> - [ ] Refuto con $a*b=a$.
> - [ ] Cuento $n^{n^2}$ operaciones.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. Grimaldi, *Matemática Discreta*, Pearson — cap. de estructuras.
>
> [2] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §9.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Propiedades de las Operaciones]] — axiomas en conjuntos.
> - [[04 - Operaciones entre números reales]] — $+,\times$ en $\mathbb{R}$.
> - [[02 - Operaciones con matrices]] — producto no conmutativo.
> - [[09 - Operaciones con funciones de variable real]] — composición.

---

**Tags:** #números-reales #operaciones #grupos #unidad2

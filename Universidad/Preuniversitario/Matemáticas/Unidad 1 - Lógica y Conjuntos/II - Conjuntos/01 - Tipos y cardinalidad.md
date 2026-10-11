---
dg-publish: true
---

# 🗂️ Tipos y Cardinalidad

## 🎯 Introducción

> [!info] 💡 ¿Qué tipos de conjuntos hay?
>
> Vacío, unitario, finito, infinito numerable ($\mathbb{N},\mathbb{Z},\mathbb{Q}$) y continuo ($\mathbb{R}$): la cardinalidad $|A|$ cuenta elementos y $|\mathcal{P}(A)|=2^{|A|}$ cuenta subconjuntos. Cantor separa numerable de no numerable.
>
> ```mermaid
> graph LR
>     A["Vacío<br/>unitario"] --> B["Finito<br/>|A|=n"]
>     B --> C["Numerable<br/>aleph0"]
>     C --> D["Continuo<br/>R"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Tipos y cardinales
>
> **Tipos:** $\emptyset$ ($|\emptyset|=0$), unitario, finito ($|A|=n$), infinito. **Extensionalidad:** $\{1,1,2\}=\{1,2\}$.
>
> **Potencia:** $|\mathcal{P}(A)|=2^{|A|}$; $\mathcal{P}(\emptyset)=\{\emptyset\}$. **Equinumeroso:** biyección entre ellos; **Cantor:** $|\mathcal{P}(A)|>|A|$.

> [!tip] 💡 Cómo contar y comparar infinitos
>
> No listes infinitos: busca la biyección ($\mathbb{N}\to$ pares con $n\mapsto2n$; $\mathbb{N}\to\mathbb{Z}$ intercalando $0,1,-1,2,-2,\dots$). $\emptyset\subseteq A$ siempre (vacuamente: ningún elemento falla). Para $|\mathcal{P}|>|\cdot|$ usa la diagonal $D=\{x:x\notin f(x)\}$.

> [!example] 🟢 Ejemplo — Biyección $\mathbb{N}\to\mathbb{Z}$
>
> $0\mapsto0$, $2n\mapsto n$, $2n-1\mapsto-n$ ($n\ge1$): $0,1,-1,2,-2,\dots$ cubre todo $\mathbb{Z}$ sin repetir ✓.

---

## 📋 Tabla Comparativa: Conjuntos

> [!note] 📋 Qué cardinal tiene cada uno
>
> | Conjunto | Tipo | Cardinal |
> |---|---|---|
> | $\emptyset$ | Vacío | $0$ |
> | $\{\emptyset\}$ | Unitario | $1$ |
> | $\{x\in\mathbb{N}:x<100\}$ | Finito | $100$ |
> | $\{x\in\mathbb{R}:x^2=-1\}$ | Vacío | $0$ |
> | Primos | Infinito numerable | $\aleph_0$ |
> | $\mathbb{Q}$ | Numerable (pares $(p,q)$) | $\aleph_0$ |
> | $\mathbb{R}$ | Continuo (diagonal) | $\mathfrak{c}$ |
>
> **Operaciones:** $|A\cup B|=5$ ($\{1,2,3\},\{3,4,5\}$); $|A\times B|=|A||B|$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\mathcal{P}(\emptyset)=\emptyset$:** es $\{\emptyset\}$ ($|\cdot|=1$).
> - **$\{1,1,2\}$ con 3 elementos:** repetidos no cuentan ($|{\cdot}|=2$).
> - **Intercalar $\mathbb{Z}$ con $-0$:** usa $2n-1\mapsto-n$ (no $2n+1$).
> - **Infinito $\therefore$ mismo tamaño:** $\mathbb{R}>\mathbb{Q}$ (diagonal).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $|A|,|B|,|C|,|D|$ con $A=\{1..5\}$, $B=\{x\in\mathbb{Z}:-2\le x\le2\}$, $C=\emptyset$, $D=\{\emptyset\}$.
> 2. $\mathcal{P}(\{1,2\})$ y $|\mathcal{P}(\{1,2,3,4\})|$.
> 3. ¿$\{1,1,2\}=\{1,2\}$? ¿$|\{a,a,b\}|$?

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $5,5,0,1$.
>
> **2.** $4$ subconjuntos; $16$.
>
> **3.** Sí; $2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $|A\cup B|$ ($\{1,2,3\},\{3,4,5\}$) y $|A\times B|$ ($5,3$).
> 5. $A^c$ con $U=\{1..5\}$, $A=\{1,2\}$.
> 6. Enumera $\mathbb{Z}$ biyectivamente.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $5$; $15$.
>
> **5.** $\{3,4,5\}$.
>
> **6.** $0,1,-1,2,-2,\dots$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. ¿Por qué $\emptyset\subseteq A$ siempre?
> 8. Infinito equinumeroso con subconjunto propio.
> 9. Cantor en $\{1,2\}$: $|\mathcal{P}|>|\cdot|$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Vacuamente (ningún $x$ falla).
>
> **8.** Pares $\subsetneq\mathbb{N}$ con $n\mapsto2n$.
>
> **9.** $D=\{x:x\notin f(x)\}$ fuera de la imagen.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo cardinales finitos y vacíos.
> - [ ] Listo $\mathcal{P}$ de 1–2 elementos.
> - [ ] Aplico extensionalidad.
> - [ ] Clasifico finito/vacío/infinito.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Opero $|A\cup B|$, $|A\times B|$.
> - [ ] Hallo complementos.
> - [ ] Hallo $|A-B|$ con intersección.
> - [ ] Enumero $\mathbb{Z}$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Construyo biyecciones $\mathbb{N}\to\mathbb{Z}$.
> - [ ] Pruebo $\mathbb{Q}$ numerable.
> - [ ] Aplico la diagonal de Cantor.
> - [ ] Distingo $\aleph_0$ de $\mathfrak{c}$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §2.1.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Conjuntos Numéricos]] — $\mathbb{N},\mathbb{Z},\mathbb{Q}$ concretos.
> - [[03 - Operaciones entre Conjuntos]] — siguiente: $\cup,\cap$.
> - [[10 - Funciones en Conjuntos]] — biyecciones a fondo.
> - [[07 - Pares ordenados y producto cartesiano]] — $|A\times B|$.

---

**Tags:** #conjuntos #cardinalidad #cantor #unidad1

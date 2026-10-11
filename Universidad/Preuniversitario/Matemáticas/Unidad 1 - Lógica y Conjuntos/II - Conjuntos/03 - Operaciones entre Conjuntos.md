---
dg-publish: true
---

# ➕ Operaciones entre Conjuntos

## 🎯 Introducción

> [!info] 💡 ¿Cómo se opera con conjuntos?
>
> $\cup$ (o), $\cap$ (y), $-$ (quitar), $^c$ (complemento), $\triangle$ (o-exclusivo): cada una tiene su prueba de pertenencia ($x\in A\cup B\iff x\in A\lor x\in B$) y De Morgan las conecta.
>
> ```mermaid
> graph LR
>     A["x en A<br/>x en B"] --> B["Union<br/>inter"]
>     B --> C["Dif<br/>compl"]
>     C --> D["De Morgan<br/>conecta"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Las cinco operaciones
>
> **$\cup$:** $x\in A\lor x\in B$. **$\cap$:** $x\in A\land x\in B$. **$-$:** $x\in A\land x\notin B$ (no conmuta).
>
> **$^c$:** respecto a $U$ (depende de $U$). **$\triangle$:** $(A-B)\cup(B-A)=(A\cup B)-(A\cap B)$.

> [!tip] 💡 Cómo operar sin equivocarse
>
> Traduce a $\lor$/$\land$ antes de manipular: $A-(B\cup C)$ es $x\in A\land\lnot(x\in B\lor x\in C)$, y De Morgan hace el resto ($(A-B)\cap(A-C)$). El complemento siempre menciona $U$ — con $U$ distinto, $A^c$ distinto.

> [!example] 🟢 Ejemplo — $A=\{1,2,3\},B=\{3,4,5\}$
>
> $\cup=\{1..5\}$, $\cap=\{3\}$, $A-B=\{1,2\}$, $B-A=\{4,5\}$, $\triangle=\{1,2,4,5\}$ (verifica $|\cup|=5=3+3-1$ ✓).

---

## 📋 Tabla Comparativa: Operaciones

> [!note] 📋 Qué significa cada una
>
> | Operación | Pertenencia | Ejemplo $[0,2],[1,3]$ |
> |---|---|---|
> | $\cup$ | $\lor$ | $[0,3]$ |
> | $\cap$ | $\land$ | $[1,2]$ |
> | $-$ | $\land\lnot$ | $[0,3]-[1,2]=[0,1)\cup(2,3]$ |
> | $^c$ | $\lnot$ en $U$ | Cambia con $U$ |
> | $\triangle$ | $\oplus$ | Elementos no compartidos |
>
> **Absorción:** $A\cup(A\cap B)=A$; $(A\cap B)\cup(A\cap B^c)=A$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$-$ conmutativa:** $A-B\neq B-A$ ($\{a\}$ vs $\{c\}$).
> - **$A^c$ sin $U$:** el complemento depende del universal.
> - **$A-B=\emptyset\therefore A=\emptyset$:** solo dice $A\subseteq B$.
> - **$\triangle$ como $\cup$:** quita la intersección.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $A=\{1,2,3\},B=\{3,4,5\}$: $\cup,\cap,-,\triangle$.
> 2. $[0,2]\cup[1,3]$, $\cap$, $[0,3]-[1,2]$.
> 3. $A-B$ vs $B-A$ ($\{a,b\},\{b,c\}$).

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\{1..5\}$; $\{3\}$; $\{1,2\}$; $\{1,2,4,5\}$.
>
> **2.** $[0,3]$; $[1,2]$; $[0,1)\cup(2,3]$.
>
> **3.** $\{a\}$; $\{c\}$ (no conmutan).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Simplifica $A\cup(A\cap B)$ y $(A\cup B)^c$.
> 5. Prueba $A-(B\cup C)=(A-B)\cap(A-C)$.
> 6. $A^c$ con $U=\{1..6\}$ vs $U=\{1..10\}$ ($A=\{1,2,3\}$).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $A$; $A^c\cap B^c$.
>
> **5.** De Morgan en la pertenencia.
>
> **6.** $\{4,5,6\}$ vs $\{4..10\}$ (depende de $U$).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $A\triangle B=(A\cup B)-(A\cap B)$.
> 8. $A-B=\emptyset\iff$ ¿qué?
> 9. Inclusión-exclusión con tres conjuntos.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Doble inclusión ($\oplus$ vs $\cup$-sin-$\cap$).
>
> **8.** $A\subseteq B$ (no $A=\emptyset$).
>
> **9.** Suma 3, resta pares, suma triple.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo $\cup,\cap,-,\triangle$ finitos.
> - [ ] Hallo complementos con $U$.
> - [ ] Opero intervalos.
> - [ ] Detecto no conmutatividad.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Simplifico con absorción.
> - [ ] Aplico De Morgan a conjuntos.
> - [ ] Pruebo igualdades por pertenencia.
> - [ ] Verifico distributivas con ejemplos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro por doble inclusión.
> - [ ] Caracterizo $A-B=\emptyset$.
> - [ ] Pruebo $(A-B)-C=A-(B\cup C)$.
> - [ ] Aplico inclusión-exclusión.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §2.2.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Tipos y cardinalidad]] — base: conjuntos.
> - [[04 - Propiedades de las Operaciones]] — siguiente: leyes.
> - [[05 - Propiedades de los operadores lógicos]] — De Morgan lógico.
> - [[09 - Relaciones]] — $\subseteq$ como orden.

---

**Tags:** #conjuntos #operaciones #demorgan #unidad1

---
dg-publish: true
---

# 📜 Propiedades de Operaciones

## 🎯 Introducción

> [!info] 💡 ¿Qué leyes rigen $\cup,\cap,-,^c$?
>
> Conmutativa, asociativa, distributiva, absorción, De Morgan y dualidad: simplifican expresiones sin elementos. Probar es doble inclusión o pertenencia traducida a $\lor$/$\land$.
>
> ```mermaid
> graph LR
>     A["Expresión<br/>larga"] --> B["Patrón<br/>abs/DM"]
>     B --> C["Simplifica<br/>ley"]
>     C --> D["Dual<br/>intercambia"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Leyes y prueba
>
> **Básicas:** conmutativa/asociativa ($\cup,\cap$; $-$ no), neutro ($\cup:\emptyset$, $\cap:U$), idempotencia, dominancia.
>
> **Fuertes:** distributiva, absorción ($A\cup(A\cap B)=A$), De Morgan, $(A^c)^c=A$, $A-B=A\cap B^c$. **Dual:** intercambia $\cup/\cap$, $\emptyset/U$. **Prueba:** doble inclusión.

> [!tip] 💡 Cómo simplificar sin perderse
>
> Convierte $-$ a $\cap^c$ primero ($A-B=A\cap B^c$) — todo se vuelve $\cup$/$\cap$ y aplican De Morgan y distributiva. Factoriza el conjunto común: $A^c\cap B^c\cup(A^c\cap B)\equiv A^c\cap(B^c\cup B)\equiv A^c$. El dual sale gratis intercambiando.

> [!example] 🟢 Ejemplo — $A\cup(A^c\cap B)$
>
> Distribuye: $(A\cup A^c)\cap(A\cup B)=U\cap(A\cup B)=A\cup B$ (no colapsa a $A$: $B$ aporta fuera de $A$ ✓).

---

## 📋 Tabla Comparativa: Leyes

> [!note] 📋 Qué ley usar y cuándo
>
> | Patrón | Ley | Resultado |
> |---|---|---|
> | $A\cup\emptyset$, $A\cap U$ | Neutro | $A$ |
> | $A\cup U$, $A\cap\emptyset$ | Dominancia | $U$, $\emptyset$ |
> | $(A\cap B)\cup(A\cap B^c)$ | Factoriza | $A$ |
> | $(A\cup B)^c$ | De Morgan | $A^c\cap B^c$ |
> | $A\cup(A^c\cap B)$ | Distribuye | $A\cup B$ |
>
> **No asociativa:** $(A-B)-C\neq A-(B-C)$ ($\{1\}$ vs $\{1,3\}$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$-$ conmutativa/asociativa:** ni una ni otra (contraejemplo $\{1\}$ vs $\{1,3\}$).
> - **$A\cup(A^c\cap B)=A$:** es $A\cup B$.
> - **De Morgan a medias:** $(A\cup B)^c=A^c\cap B^c$ (parte el $\cup$).
> - **Dual sin intercambiar $U$:** dual cambia $\cup/\cap$ **y** $\emptyset/U$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Verifica $A\cup\emptyset=A$, $A\cap A=A$.
> 2. ¿Conmuta $-$? Contraejemplo.
> 3. Dual de $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Neutro e idempotencia.
>
> **2.** $\{1\}\neq\{3\}$.
>
> **3.** $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Simplifica $(A\cap B)\cup(A\cap B^c)$.
> 5. Prueba $A-B=A\cap B^c$.
> 6. Dual de De Morgan: escribe y verifica.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $A$.
>
> **5.** Doble inclusión ($\land\lnot$).
>
> **6.** $(A\cap B)^c=A^c\cup B^c$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $A-(B\cup C)=(A-B)\cap(A-C)$ con De Morgan.
> 8. Numérico: $(A-B)-C\neq A-(B-C)$.
> 9. Prueba $A\cap(B-C)=(A\cap B)-C$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $A\cap B^c\cap C^c$ ambos lados.
>
> **8.** $\{1\}$ vs $\{1,3\}$.
>
> **9.** $x\in A\land x\in B\land x\notin C$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico neutro e idempotencia.
> - [ ] Refuto conmutatividad de $-$.
> - [ ] Identifico neutros y absorbentes.
> - [ ] Escribo duales.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Factorizo con distributiva.
> - [ ] Pruebo $A-B=A\cap B^c$.
> - [ ] Simplifico con De Morgan.
> - [ ] Verifico duales.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Encadeno 3+ leyes.
> - [ ] Refuto asociatividad numéricamente.
> - [ ] Distingo $A\cup B$ de $A$.
> - [ ] Demuestro por doble inclusión.

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
> - [[03 - Operaciones entre Conjuntos]] — base: operaciones.
> - [[05 - Propiedades de los operadores lógicos]] — dual lógico.
> - [[03 - Operaciones binarias]] — asociatividad abstracta.
> - [[09 - Relaciones]] — $\subseteq$ y orden.

---

**Tags:** #conjuntos #leyes #dualidad #unidad1

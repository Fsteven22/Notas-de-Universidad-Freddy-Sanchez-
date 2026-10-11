---
dg-publish: true
---

# 🔍 Cuantificadores

## 🎯 Introducción

> [!info] 💡 ¿Qué son $\forall$ y $\exists$?
>
> $\forall x\,P(x)$ (todos) se refuta con un contraejemplo; $\exists x\,P(x)$ (alguno) se prueba con un testigo. Negar intercambia ($\lnot\forall=\exists\lnot$) y el orden importa ($\forall x\exists y\neq\exists y\forall x$).
>
> ```mermaid
> graph LR
>     A["Para todo<br/>contraej"] --> B["Existe<br/>testigo"]
>     B --> C["Niega<br/>intercambia"]
>     C --> D["Orden<br/>importa"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Universal, existencial y negación
>
> **$\forall x\,P(x)$:** V si todo $x$ cumple (un contraejemplo la tumba). **$\exists x\,P(x)$:** V si algún $x$ cumple (testigo).
>
> **De Morgan:** $\lnot\forall xP\equiv\exists x\lnot P$; $\lnot\exists xP\equiv\forall x\lnot P$. **Vacío:** $\forall$ en $\emptyset$ es V; $\exists$ es F.

> [!tip] 💡 Cómo probar, refutar y negar
>
> $\forall$ se refuta con un caso ($\exists x\in\mathbb{Z}\;x^2=2$ es F: ningún entero); $\exists$ se prueba exhibiendo ($x=2$ primo par). Al negar, cambia cada cuantificador y niega el predicado: $\lnot\forall x\exists y(x<y)\equiv\exists x\forall y(x\ge y)$.

> [!example] 🟢 Ejemplo — Orden distinto, valor distinto
>
> $\forall x\exists y\,(x+y=0)$ es V ($y=-x$); $\exists y\forall x\,(x+y=0)$ es F (ningún $y$ sirve para todo $x$).

---

## 📋 Tabla Comparativa: Cuantificadores

> [!note] 📋 Qué pide cada uno
>
> | Forma | Se prueba con | Se refuta con |
> |---|---|---|
> | $\forall x\,P(x)$ | Argumento general | Un contraejemplo |
> | $\exists x\,P(x)$ | Un testigo | Agotar el dominio |
> | $\forall x\exists y$ | $y$ según $x$ | $x$ sin $y$ |
> | $\exists y\forall x$ | Un $y$ universal | Cada $y$ falla en algún $x$ |
>
> **Distribución:** $\forall$ distribuye $\land$ pero no $\lor$ ($P$ par, $Q$ impar en $\{1,2\}$ refuta).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Negar sin intercambiar:** $\lnot\forall xP$ es $\exists x\lnot P$, no $\forall x\lnot P$.
> - **$\forall x\exists y=\exists y\forall x$:** el orden cambia el valor.
> - **$\forall$ en vacío como F:** es V (vacuamente); $\exists$ es F.
> - **Libre vs ligada:** en $\forall x\,(x<y)$, $y$ queda libre (no es proposición).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. V/F: $\exists x\in\mathbb{Z}\;x^2=2$; $\forall x\,(x+0=x)$.
> 2. Niega $\forall x\,P(x)$.
> 3. $D=\{2,4,6\}$: $\forall x$ par; $\exists x>5$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** F; V.
>
> **2.** $\exists x\,\lnot P(x)$.
>
> **3.** V; V (testigo $6$).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. "Existe $x$ primo y par" con testigo.
> 5. Niega $\forall x\exists y\,(x<y)$.
> 6. $D=\emptyset$: $\forall x\,(x^2<0)$ y $\exists x\,(x^2<0)$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\exists x(\text{Primo}\land\text{Par})$; $x=2$.
>
> **5.** $\exists x\forall y\,(x\ge y)$.
>
> **6.** V (vacua); F.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $\forall x\exists y\,(x+y=0)$ vs $\exists y\forall x\,(x+y=0)$ en $\mathbb{Z}$.
> 8. ¿$\forall x(P\lor Q)\equiv\forall xP\lor\forall xQ$?
> 9. Niega $\forall x\exists y\forall z\,((P\land Q)\to R)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** V; F.
>
> **8.** No ($P$ par, $Q$ impar en $\{1,2\}$).
>
> **9.** $\exists x\forall y\exists z\,(P\land Q\land\lnot R)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Simbolizo "todo" y "existe".
> - [ ] Decido V/F en dominios finitos.
> - [ ] Niego $\forall$/$\exists$ simples.
> - [ ] Hallo testigos y contraejemplos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Detecto libres y ligadas.
> - [ ] Niego anidados $\forall\exists$.
> - [ ] Evalúo en $\emptyset$.
> - [ ] Traduzco "ningún" de dos formas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Formalizo inyectividad.
> - [ ] Distingo órdenes $\forall\exists$/$\exists\forall$.
> - [ ] Refuto distribuciones con $\{1,2\}$.
> - [ ] Niego triples anidados.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §1.4.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 2.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[05 - Predicados de una variable]] — $P(x)$ como base.
> - [[05 - Predicados de una variable]] — siguiente: $P(x,y)$.
> - [[01 - Proposiciones]] — $V/F$ de enunciados.
> - [[06 - Razonamientos con predicados y cuantificadores]] — reglas $\forall$/$\exists$.

---

**Tags:** #lógica #cuantificadores #forall #unidad1

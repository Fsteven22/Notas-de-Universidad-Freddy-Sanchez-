---
dg-publish: true
---

# 📜 Leyes Lógicas

## 🎯 Introducción

> [!info] 💡 ¿Qué leyes rigen los conectivos?
>
> Identidad, dominación, De Morgan, distributiva, absorción y condicional ($p\to q\equiv\lnot p\lor q$): simplifican fórmulas sin tablas. El método CLAVE (Conoce, Localiza, Aplica, Verifica, Expande) ordena el trabajo.
>
> ```mermaid
> graph LR
>     A["Fórmula<br/>larga"] --> B["Localiza<br/>patrón"]
>     B --> C["Aplica<br/>ley"]
>     C --> D["Verifica<br/>tabla"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Leyes por grupo
>
> **Básicas:** $p\land V\equiv p$, $p\lor F\equiv p$ (neutro); $p\land F\equiv F$, $p\lor V\equiv V$ (dominación); $p\land\lnot p\equiv F$.
>
> **De Morgan:** $\lnot(p\land q)\equiv\lnot p\lor\lnot q$. **Condicional:** $p\to q\equiv\lnot p\lor q$; contrapositiva $\lnot q\to\lnot p$. **Distributiva/absorción:** $p\land(q\lor r)\equiv(p\land q)\lor(p\land r)$; $p\lor(p\land q)\equiv p$.

> [!tip] 💡 Cómo simplificar sin perderse
>
> Busca primero De Morgan (niega paréntesis partiendo el $\land$/$\lor$) y condicionales (pásalos a $\lor$). Luego factoriza el literal común como en álgebra: $(p\land q)\lor(p\land\lnot q)\equiv p\land(q\lor\lnot q)\equiv p$. Verifica con una valuación rápida.

> [!example] 🟢 Ejemplo — $(p\to q)\land(p\to\lnot q)\equiv\lnot p$
>
> $(\lnot p\lor q)\land(\lnot p\lor\lnot q)\equiv\lnot p\lor(q\land\lnot q)\equiv\lnot p\lor F\equiv\lnot p$ ✓.

---

## 📋 Tabla Comparativa: Leyes

> [!note] 📋 Qué ley aplicar y cuándo
>
> | Patrón | Ley | Resultado |
> |---|---|---|
> | $\lnot(p\land q)$ | De Morgan | $\lnot p\lor\lnot q$ |
> | $p\to q$ | Condicional | $\lnot p\lor q$ |
> | $(p\land q)\lor(p\land\lnot q)$ | Factoriza | $p$ |
> | $(p\lor q)\land(\lnot p\lor q)$ | Distributiva | $q$ |
> | $[(p\lor q)\land\lnot p]\lor q$ | Absorción | $q$ |
>
> **Vacía:** antecedente F $\therefore$ condicional V ("si $5$ es par..." es V).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **De Morgan sin partir:** $\lnot(p\land q)\neq\lnot p\land\lnot q$.
> - **$p\to q\equiv p\land q$:** es $\lnot p\lor q$.
> - **Contrapositiva como $q\to p$:** es $\lnot q\to\lnot p$.
> - **Absorción inventada:** $p\lor(\lnot p\land q)\equiv p\lor q$ (distribuye primero).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. De Morgan a $\lnot(p\land q)$ y $\lnot(p\lor q)$.
> 2. Contrapositiva de $p\to q$.
> 3. $p\leftrightarrow q$ como dos condicionales.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\lnot p\lor\lnot q$; $\lnot p\land\lnot q$.
>
> **2.** $\lnot q\to\lnot p$.
>
> **3.** $(p\to q)\land(q\to p)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Simplifica $(p\land q)\lor(p\land\lnot q)$.
> 5. Aplica distributiva a $p\land(q\lor r)$.
> 6. ¿Por qué "si $5$ es par, $2+2=5$" es V?

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $p$ (factoriza).
>
> **5.** $(p\land q)\lor(p\land r)$.
>
> **6.** Antecedente F (verdad vacía).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $(p\to q)\land(p\to\lnot q)$ por leyes.
> 8. $\lnot(p\lor q)\lor(p\land q)$ y su patrón.
> 9. Exportación $(p\land q)\to r\equiv p\to(q\to r)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\lnot p$.
>
> **8.** $p\leftrightarrow q$.
>
> **9.** Tabla 8 filas (columnas iguales).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico De Morgan a $\land$/$\lor$.
> - [ ] Escribo contrapositivas.
> - [ ] Uso neutro y dominación.
> - [ ] Traduzco negaciones del lenguaje.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Factorizo literales comunes.
> - [ ] Convierto $\to$ a $\lor$.
> - [ ] Distribuyo en ambas direcciones.
> - [ ] Explico verdad vacía.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Encadeno 3+ leyes.
> - [ ] Reconozco $p\leftrightarrow q$ escondido.
> - [ ] Pruebo exportación.
> - [ ] Clasifico resultados.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §1.3.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 2.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Clases de Proposiciones]] — base: equivalencias.
> - [[03 - Clases de Proposiciones]] — clasifica resultados.
> - [[06 - Razonamientos]] — siguiente: inferencia.
> - [[04 - Propiedades de las Operaciones]] — dualidad en conjuntos.

---

**Tags:** #lógica #leyes #demorgan #unidad1

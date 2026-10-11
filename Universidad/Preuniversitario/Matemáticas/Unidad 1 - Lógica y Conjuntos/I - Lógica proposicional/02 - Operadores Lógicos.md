---
dg-publish: true
---

# 🔗 Operadores Lógicos

## 🎯 Introducción

> [!info] 💡 ¿Qué son los operadores lógicos?
>
> Funciones de verdad que combinan proposiciones: $\lnot$ (NOT), $\land$ (AND), $\lor$ (OR), $\to$ (THEN), $\leftrightarrow$ (IFF). El conector principal (menor precedencia) manda en la fórmula.
>
> ```mermaid
> graph LR
>     A["p,q<br/>simples"] --> B["Conector<br/>5 ops"]
>     B --> C["Compuesta<br/>V/F"]
>     C --> D["Principal<br/>manda"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Los cinco y precedencia
>
> **$\lnot p$:** invierte (unario, mayor precedencia). **$p\land q$:** V solo si ambas V. **$p\lor q$:** F solo si ambas F.
>
> **$p\to q$:** F solo si $p$ V y $q$ F ($\equiv\lnot p\lor q$). **$p\leftrightarrow q$:** V si iguales. **Precedencia:** $\lnot>\land>\lor>\to>\leftrightarrow$.

> [!tip] 💡 Cómo hallar el conector principal
>
> Lee de afuera hacia adentro respetando precedencia y paréntesis: en $\lnot(p\land q)$ el $\lnot$ externo manda; en $\lnot p\lor\lnot q$ el $\lor$ (el $\lnot$ ata primero a cada $p$). Traduce "solo si" como condición necesaria ($p\to q$) y "no es cierto que... o..." como $\lnot(p\lor q)$.

> [!example] 🟢 Ejemplo — Principal en cinco fórmulas
>
> $\lnot(p\land q)\to\lnot$; $(p\lor q)\land r\to\land$; $p\to(q\leftrightarrow r)\to\to$; $\lnot p\lor\lnot q\to\lor$; $(p\to q)\leftrightarrow(\lnot q\to\lnot p)\to\leftrightarrow$.

---

## 📋 Tabla Comparativa: Conectores

> [!note] 📋 Cuándo es V cada uno
>
> | Conector | V cuando | F cuando |
> |---|---|---|
> | $\lnot p$ | $p$ F | $p$ V |
> | $p\land q$ | Ambas V | Alguna F |
> | $p\lor q$ | Alguna V | Ambas F |
> | $p\to q$ | Salvo V$\to$F | $p$ V, $q$ F |
> | $p\leftrightarrow q$ | Iguales | Distintas |
>
> **Lenguaje:** "pero/admás" $=\land$; "si... entonces" $=\to$; "sii/equivale" $=\leftrightarrow$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$p\to q$ como $p\land q$:** el condicional es V con antecedente F.
> - **"O" excluyente siempre:** $\lor$ es inclusivo (ambas V $\to$ V).
> - **"Solo si" al revés:** "aprobarás solo si estudias" es $p\to q$.
> - **Principal en $\lnot p\lor\lnot q$:** es $\lor$, no $\lnot$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Principal en $\lnot(p\land q)$, $(p\lor q)\land r$, $p\to(q\leftrightarrow r)$.
> 2. Principal en $\lnot p\lor\lnot q$ y $(p\to q)\leftrightarrow(\lnot q\to\lnot p)$.
> 3. Traduce "si estudias y practicas, entonces aprobarás".

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\lnot$; $\land$; $\to$.
>
> **2.** $\lor$; $\leftrightarrow$.
>
> **3.** $(p\land q)\to r$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. "No es cierto que llueva o haga sol".
> 5. "Aprobarás sii estudias o tienes suerte".
> 6. "Aprobarás solo si estudias".

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\lnot(p\lor q)$.
>
> **5.** $p\leftrightarrow(q\lor r)$.
>
> **6.** $p\to q$ (necesaria).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Traduce "si no llueve iremos al parque, pero si llueve y hace frío nos quedaremos".
> 8. ¿Es $(p\to q)\lor(q\to p)$ tautología?
> 9. Formaliza "si $n$ par $\therefore n^2$ par" y nombra la regla.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(\lnot p\to q)\land((p\land r)\to s)$.
>
> **8.** Sí (uno de los dos siempre es V).
>
> **9.** Modus ponens.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico conectores principales.
> - [ ] Recito tablas de los cinco.
> - [ ] Traduzco condicionales simples.
> - [ ] Aplico precedencia.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Traduzco negaciones de disyunciones.
> - [ ] Distingo necesaria de suficiente.
> - [ ] Formalizo bicondicionales.
> - [ ] Uso equivalencias ($q\to p$).

> [!note] 📋 Nivel Avanzado
>
> - [ ] Traduzco párrafos compuestos.
> - [ ] Decido tautologías con tablas.
> - [ ] Simplifico $(p\land q)\to p$.
> - [ ] Reconozco reglas de inferencia.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §1.1.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 2.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Proposiciones]] — base: qué es P.
> - [[03 - Clases de Proposiciones]] — siguiente: tautologías.
> - [[03 - Clases de Proposiciones]] — FBF y valuaciones.
> - [[06 - Razonamientos]] — modus ponens y reglas.

---

**Tags:** #lógica #operadores #conectores #unidad1

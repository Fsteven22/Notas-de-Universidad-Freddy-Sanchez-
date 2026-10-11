---
dg-publish: true
---

# ⚖️ Razonamientos

## 🎯 Introducción

> [!info] 💡 ¿Qué es un razonamiento válido?
>
> Premisas $\therefore$ conclusión donde la conclusión sigue necesariamente (premisas V $\implies$ conclusión V): modus ponens/tollens, silogismos y dilemas son válidos; afirmar el consecuente no. Válido + premisas V $=$ sólido.
>
> ```mermaid
> graph LR
>     A["Premisas<br/>lista"] --> B["Regla<br/>MP/MT/SH"]
>     B --> C["Conclusión<br/>necesaria"]
>     C --> D["Sólido<br/>+V premisas"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Validez, reglas y falacias
>
> **Válido:** $(P_1\land\cdots\land P_n)\to C$ tautología. **Sólido:** válido + premisas verdaderas.
>
> **Reglas:** MP ($p\to q,p\therefore q$), MT ($p\to q,\lnot q\therefore\lnot p$), SH (encadena $\to$), SD ($p\lor q,\lnot p\therefore q$). **Falacias:** afirmar consecuente, negar antecedente.

> [!tip] 💡 Cómo decidir validez en segundos
>
> Formaliza con letras y busca el patrón: $\to$ + antecedente $\to$ MP; $\to$ + $\lnot$ consecuente $\to$ MT; cadena de $\to$ $\to$ SH. Si ves consecuente afirmado o antecedente negado, es falacia directa — no necesitas tabla.

> [!example] 🟢 Ejemplo — Cadena de lluvia
>
> $p\to q,q\to r,r\to s,p\therefore s$ por SH dos veces (verifica cada eslabón: si uno falla, la cadena se rompe ahí).

---

## 📋 Tabla Comparativa: Reglas vs Falacias

> [!note] 📋 Qué patrón es válido y cuál no
>
> | Patrón | Estado | Nombre |
> |---|---|---|
> | $p\to q,p\therefore q$ | Válido | Modus ponens |
> | $p\to q,\lnot q\therefore\lnot p$ | Válido | Modus tollens |
> | $p\lor q,\lnot p\therefore q$ | Válido | Silogismo disyuntivo |
> | Dilema $(p\to q)\land(r\to s)\land(p\lor r)$ | Válido | Dilema constructivo |
> | $p\to q,q\therefore p$ | Falacia | Afirmar consecuente |
> | $p\to q,\lnot p\therefore\lnot q$ | Falacia | Negar antecedente |
>
> **Informales:** *ad ignorantiam* (OVNIs), *ad hominem*, falsa causa — fallan en contenido, no en forma.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Válido = premisas V:** la validez es forma; la solidez añade verdad ("el sol es oro" es válido, no sólido).
> - **Tests pasan $\therefore$ sin bugs:** afirmar consecuente (MT bien usado solo descarta lo detectable).
> - **MT como $q\to p$:** es $\lnot q\therefore\lnot p$ (niega, no afirma).
> - **Ex falso ignorado:** premisas contradictorias validan cualquier conclusión.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Validez de $p\to q,p\therefore q$; $p\to q,q\therefore p$; $p\lor q,\lnot p\therefore q$.
> 2. Regla en "si llueve se cancela; llueve $\therefore$ se cancela".
> 3. ¿Válidas? $p\land q\therefore p$; $p\therefore p\lor q$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Válido (MP); falacia; válido (SD).
>
> **2.** Modus ponens.
>
> **3.** Sí (simplificación y adición).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Falacia: "nadie probó que OVNIs no existen $\therefore$ existen".
> 5. Verifica MT con tabla.
> 6. Formaliza la cadena de lluvia (4 eslabones).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** *Ad ignorantiam*.
>
> **5.** Tabla siempre V.
>
> **6.** SH dos veces.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Dilema $(p\to q)\land(r\to s)\land(p\lor r)\therefore q\lor s$.
> 8. Construye válido no sólido (marca la premisa falsa).
> 9. Tests pasan: falacia y reformulación con MT.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Válido (dilema constructivo).
>
> **8.** "Todo lo que brilla es oro..." (premisa 1 falsa).
>
> **9.** Afirmar consecuente; MT solo descarta lo detectable.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Separo premisas y conclusión.
> - [ ] Reconozco MP, MT, SD.
> - [ ] Detecto consecuente/antecedente falaz.
> - [ ] Aplico simplificación y adición.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Nombro falacias informales.
> - [ ] Verifico MT con tabla.
> - [ ] Encadeno SH.
> - [ ] Instancio universales + MP.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Pruebo dilemas constructivos.
> - [ ] Construyo válido no sólido.
> - [ ] Ilustro *ex falso*.
> - [ ] Reformulo argumentos con MT.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §1.6.
>
> [2] I. Copi, *Introducción a la Lógica* — cap. de inferencia.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[05 - Propiedades de los operadores lógicos]] — base: leyes.
> - [[07 - Demostraciones]] — siguiente: métodos de prueba.
> - [[06 - Razonamientos con predicados y cuantificadores]] — reglas con $\forall,\exists$.
> - [[03 - Clases de Proposiciones]] — validez como tautología.

---

**Tags:** #lógica #razonamientos #falacias #unidad1

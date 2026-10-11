---
dg-publish: true
---

# 💬 Proposiciones

## 🎯 Introducción

> [!info] 💡 ¿Qué es una proposición?
>
> Enunciado con valor de verdad único (V o F): "Guayaquil está en Ecuador" sí; "¿cómo estás?", órdenes y paradojas no. El método VADO (Verificable, Aseverativo, Definido, Objetivo) decide en segundos.
>
> ```mermaid
> graph LR
>     A["Enunciado<br/>cualquiera"] --> B["VADO<br/>4 filtros"]
>     B --> C["P<br/>V o F"]
>     C --> D["NP<br/>pregunta/etc"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Proposición y VADO
>
> **Proposición:** enunciado declarativo con exactamente un valor de verdad ($V(p)\in\{V,F\}$).
>
> **VADO:** Verificable (se puede decidir), Aseverativo (afirma/niega), Definido (sentido único), Objetivo (no depende del gusto).

> [!tip] 💡 Cómo clasificar sin dudar
>
> Busca el verbo primero: pregunta, orden o exclamación $\to$ NP directo. Si afirma algo, pasa VADO — "la pizza está deliciosa" falla en Objetivo (NP), "mañana lloverá" pasa (P, verificable después). Las autorreferencias ("esta proposición es falsa") fallan en Definido.

> [!example] 🟢 Ejemplo — Cinco clasificaciones
>
> $5+3=8$ P (V); "¿cómo estás?" NP (pregunta); "cierra la ventana" NP (orden); $x+5=12$ NP (variable libre); $\exists n$ primo $>100$ P (existencial V).

---

## 📋 Tabla Comparativa: P vs NP

> [!note] 📋 Qué cae en cada lado
>
> | Enunciado | P/NP | Por qué |
> |---|---|---|
> | $5+3=8$ | P | Matemática objetiva |
> | Guayaquil está en Ecuador | P | Hecho verificable |
> | ¿Cómo estás? | NP | Pregunta |
> | ¡Qué calor! | NP | Exclamación |
> | Cierra la ventana | NP | Orden |
> | $x+5=12$ | NP | Variable libre |
> | La pizza está deliciosa | NP | Subjetiva |
> | Esta proposición es falsa | NP | Paradoja |
> | $p\to q$ | P | Forma condicional |
>
> **Predictivas:** "mañana lloverá" es P (verificable después, aunque hoy no se sepa).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Preguntas como P:** sin afirmación no hay valor de verdad.
> - **Subjetivas como P:** el gusto no es objetivo.
> - **$x+5=12$ como P:** con $x$ libre no tiene valor fijo (es predicado).
> - **Paradojas como P:** no admiten valor único.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $5+3=8$.
> 2. "¿Cómo estás?"
> 3. "Cierra la ventana".

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** P (matemática objetiva).
>
> **2.** NP (pregunta).
>
> **3.** NP (orden).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $x+5=12$.
> 5. "La pizza está deliciosa".
> 6. "Mañana lloverá".

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** NP (variable libre).
>
> **5.** NP (subjetiva).
>
> **6.** P (verificable después).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. "Esta proposición es falsa".
> 8. $\emptyset$ no tiene elementos.
> 9. $\forall\varepsilon>0\,\exists\delta>0:\ldots$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** NP (paradoja).
>
> **8.** P (matemática formal).
>
> **9.** P (matemática formal).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo P de NP en 5 casos.
> - [ ] Reconozco preguntas/órdenes/exclamaciones.
> - [ ] Identifico hechos verificables.
> - [ ] Aplico VADO básico.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Detecto variables libres.
> - [ ] Descarto subjetivas.
> - [ ] Acepto predictivas verificables.
> - [ ] Clasifico cuantificadas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Detecto paradojas autorreferentes.
> - [ ] Clasifico formas ($p\to q$).
> - [ ] Evalúo enunciados probabilísticos.
> - [ ] Formalizo con cuantificadores.

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
> - [[02 - Operadores Lógicos]] — siguiente: conectivos.
> - [[03 - Clases de Proposiciones]] — simples/compuestas.
> - [[05 - Predicados de una variable]] — $x+5=12$ como predicado.
> - [[02 - Cuantificadores]] — $\forall,\exists$ formales.

---

**Tags:** #lógica #proposiciones #vado #unidad1

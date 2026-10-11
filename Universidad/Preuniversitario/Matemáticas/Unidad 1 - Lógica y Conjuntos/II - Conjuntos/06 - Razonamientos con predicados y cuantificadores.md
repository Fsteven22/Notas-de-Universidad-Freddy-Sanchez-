---
dg-publish: true
---

# ⚖️ Razonamientos con Predicados

## 🎯 Introducción

> [!info] 💡 ¿Cómo se razona con $\forall$ y $\exists$?
>
> Cuatro reglas: IU ($\forall\to$ caso), GU (caso arbitrario $\to\forall$), IE ($\exists\to$ testigo nuevo), GE (caso $\to\exists$). El testigo de IE nunca es arbitrario — GU sobre él es inválida.
>
> ```mermaid
> graph LR
>     A["Para todo<br/>IU baja"] --> B["Testigo<br/>IE nuevo"]
>     B --> C["Arbitrario<br/>GU sube"]
>     C --> D["Existe<br/>GE cierra"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Las cuatro reglas
>
> **IU:** $\forall xP\therefore P(a)$ (cualquier $a$). **GU:** $P(a)$, $a$ arbitrario $\therefore\forall xP$.
>
> **IE:** $\exists xP\therefore P(c)$, $c$ nuevo. **GE:** $P(a)\therefore\exists xP$. **Estrategia:** IE primero, IU después, MP en medio, GE/GU al final.

> [!tip] 💡 Cómo armar derivaciones sin errores
>
> Elimina $\exists$ antes de instanciar $\forall$ (el testigo $c$ debe ser fresco). Jamás generalices un testigo de IE: "$2$ es par $\therefore\forall x$ par" falla porque $2$ no es arbitrario. Con testigo común ($\exists$ par y $\exists$ primo) verifica explícito ($x=2$ sirve a ambos).

> [!example] 🟢 Ejemplo — $\forall x(P\to Q),\exists xP\therefore\exists xQ$
>
> $P(c)$ (IE); $P(c)\to Q(c)$ (IU); $Q(c)$ (MP); $\exists xQ$ (GE) ✓.

---

## 📋 Tabla Comparativa: Reglas

> [!note] 📋 Qué regla usar y cuándo
>
> | Paso | Regla | Condición |
> |---|---|---|
> | $\forall\to$ caso | IU | Cualquier $a$ |
> | Caso arbitrario $\to\forall$ | GU | $a$ sin supuestos |
> | $\exists\to$ caso | IE | $c$ nuevo |
> | Caso $\to\exists$ | GE | Siempre vale |
>
> **Orden:** $\forall x\exists y\,(y>x)$ V en $\mathbb{N}$; $\exists y\forall x\,(y>x)$ F (sin máximo).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **GU sobre testigo IE:** $a$ es fijo desconocido, no arbitrario.
> - **IE dos veces con mismo $c$:** cada $\exists$ pide testigo nuevo.
> - **IU después de IE con $c$:** instancia con el testigo, no con otro.
> - **Testigos distintos como uno:** par (4) y primo (3) no dan par-primo sin verificar ($2$ sí).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. IU en $\forall x\,(x+0=x)$ con $x=5$.
> 2. ¿Vale "$2$ par $\therefore\forall x$ par"?
> 3. GE: "$10$ par $\therefore\exists x$ par".

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $5+0=5$.
>
> **2.** No ($2$ no arbitrario).
>
> **3.** Sí, directa.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $\forall x(P\to Q),\exists xP\therefore\exists xQ$ (4 líneas).
> 5. Error: $\exists xP\therefore P(a)$; $P(a)\to Q(a)\therefore\forall x(P\to Q)$.
> 6. $\forall x(P\to Q),\lnot Q(c)\therefore\lnot P(c)$ (reglas).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** IE, IU, MP, GE.
>
> **5.** $a$ de IE: GU inválida.
>
> **6.** IU + MT.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Barbara: $\forall x(M\to P),\forall x(S\to M)\therefore\forall x(S\to P)$.
> 8. $\exists y\forall xP\to\forall x\exists yP$ sí; al revés no.
> 9. $\exists$ par + $\exists$ primo: ¿testigo común?

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** IU, IU, SH, GU.
>
> **8.** $y=x+1$ vs sin máximo.
>
> **9.** No en general; aquí $x=2$ (verificado).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico IU a casos.
> - [ ] Detecto GU inválidas.
> - [ ] Aplico GE directa.
> - [ ] Nombro testigos con condiciones.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Derivo en 4–6 líneas numeradas.
> - [ ] Niego $\forall\exists$ anidados.
> - [ ] Detecto testigos no arbitrarios.
> - [ ] Combino IU + MT.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Derivo por casos con arbitrario.
> - [ ] Distingo órdenes $\forall\exists$.
> - [ ] Verifico testigos comunes.
> - [ ] Pruebo Barbara con IU/GU.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §1.6.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 2.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Cuantificadores]] — base: $\forall,\exists$.
> - [[06 - Razonamientos]] — reglas proposicionales.
> - [[05 - Predicados de una variable]] — $P(x)$ y $V_P$.
> - [[07 - Demostraciones]] — Barbara como silogismo.

---

**Tags:** #lógica #inferencia #cuantificadores #unidad1

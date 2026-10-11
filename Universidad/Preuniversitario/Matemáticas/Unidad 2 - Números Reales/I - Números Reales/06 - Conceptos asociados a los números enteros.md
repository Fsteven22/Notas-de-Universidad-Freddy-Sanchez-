---
dg-publish: true
---

# 🔢 Enteros: Divisibilidad y Primos

## 🎯 Introducción

> [!info] 💡 ¿Qué rige a los enteros?
>
> Divisibilidad ($a\mid b$), primos (factorización única), MCD/mcm (Euclides) y congruencias ($a\equiv b\bmod n$): con resto $r\ge0$ la división es única y $\mathbb{Z}_p$ es campo si $p$ es primo.
>
> ```mermaid
> graph LR
>     A["a|b<br/>divide"] --> B["Primos<br/>factoriza"]
>     B --> C["MCD<br/>Euclides"]
>     C --> D["Mod n<br/>congruencia"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[06-criba.png]]

> [!tip] 💡 Visual — Criba de Eratóstenes
>
> Tacha múltiplos de $2,3,5,\ldots$: sobreviven $2,3,5,7,11,13,17,19,23,29$ hasta $30$ — y $360=2^3\cdot3^2\cdot5$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — División, primos y congruencias
>
> **División:** $a=bq+r$, $0\le r<|b|$ ($b\neq0$; el resto nunca negativo). **Primo:** solo divisores $1,p$. **Fundamental:** factorización única.
>
> **MCD/mcm:** Euclides (restos sucesivos); $\text{MCD}\cdot\text{mcm}=ab$. **Congruencia:** $a\equiv b\bmod n\iff n\mid(a-b)$.

> [!tip] 💡 Cómo dividir con negativos sin fallar
>
> El resto es $r\ge0$ siempre: $-17\div5$ da $q=-4,r=3$ (no $r=-2$); $17\div-5$ da $q=-3,r=2$. Verifica multiplicando: $bq+r$ debe dar $a$ exacto — si no, el cociente está mal.

> [!example] 🟢 Ejemplo — $\text{MCD}(48,18)$ y $7x\equiv1\bmod5$
>
> $48=18(2)+12$, $18=12(1)+6\therefore\text{MCD}=6$; Bézout $48(-1)+18(3)=6$ ✓. $7\equiv2\therefore2x\equiv1\therefore x\equiv3$ (verifica $21\equiv1$ ✓).

---

## 📋 Tabla Comparativa: Herramientas

> [!note] 📋 Qué usar para cada pregunta
>
> | Pregunta | Herramienta | Ejemplo |
> |---|---|---|
> | ¿Divide? | $a\mid b\iff$ resto $0$ | $3\mid12$ sí; $0\mid5$ no |
> | Factores primos | Criba + división | $360=2^3\cdot3^2\cdot5$ |
> | Común mayor/menor | Euclides | $\text{MCD}(48,18)=6$, $\text{mcm}(12,18)=36$ |
> | Resto de potencias | Fermat/Euler | $2^{100}\equiv1\bmod101$ |
> | Sistema de restos | Chino | $x\equiv2(3),3(5)\therefore x\equiv8(15)$ |
>
> **Bases:** $13_{10}=1101_2$; $255_{10}=FF_{16}$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Resto negativo:** $r\ge0$ siempre ($17\div-5\to q=-3,r=2$).
> - **$0\mid5$:** el divisor nunca es $0$ ($5\mid0$ sí vale).
> - **$1$ primo:** no (solo $2,3,5,\ldots$).
> - **Inverso sin $\text{MCD}=1$:** en $\mathbb{Z}_6$ solo $1,5$ invierten.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. ¿$a\mid b$? $3\mid12$, $4\mid10$, $5\mid0$, $0\mid5$.
> 2. Primos hasta $30$; factoriza $360$.
> 3. Cociente y resto: $17\div5$, $-17\div5$, $17\div-5$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Sí; no; sí; no.
>
> **2.** $2,3,5,7,11,13,17,19,23,29$; $2^3\cdot3^2\cdot5$.
>
> **3.** $3$ r$2$; $-4$ r$3$; $-3$ r$2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Euclides: $\text{MCD}(48,18)$, $\text{MCD}(1071,462)$.
> 5. Resuelve $7x\equiv1\bmod5$ y $3x\equiv2\bmod7$.
> 6. $255_{10}$ a hex y $FF_{16}$ a decimal.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $6$; $21$.
>
> **5.** $x\equiv3$; $x\equiv3$.
>
> **6.** $FF_{16}$; $255$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Bézout: $x,y$ con $48x+18y=6$.
> 8. Prueba infinitud de primos.
> 9. Resto chino: $x\equiv2(3)$, $x\equiv3(5)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $x=-1,y=3$.
>
> **8.** $N=p_1\cdots p_k+1$ trae primo nuevo.
>
> **9.** $x\equiv8\bmod15$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Decido $a\mid b$ con resto cero.
> - [ ] Cribo primos y factorizo.
> - [ ] Divido con $r\ge0$ (negativos incluidos).
> - [ ] Reduzco $\bmod n$ y convierto bases.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico Euclides a dos pares.
> - [ ] Resuelvo $ax\equiv b$ lineales.
> - [ ] Verifico $\text{MCD}\cdot\text{mcm}=ab$.
> - [ ] Pruebo paridad con divisibilidad.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Hallo coeficientes de Bézout.
> - [ ] Demuestro infinitud de primos.
> - [ ] Aplico Fermat a potencias gigantes.
> - [ ] Resuelvo sistemas con resto chino.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. Grimaldi, *Matemática Discreta*, Pearson — cap. de enteros.
>
> [2] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §4.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Operaciones binarias]] — $\mathbb{Z}_n$ como estructura.
> - [[01 - Tipos y cardinalidad]] — infinitud de primos.
> - [[13 - Técnicas de conteo]] — conteo con MCD.
> - [[12 - Inducción matemática]] — prueba infinitud de primos.

---

**Tags:** #números-reales #enteros #primos #unidad2

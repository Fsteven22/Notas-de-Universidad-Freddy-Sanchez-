---
dg-publish: true
---

# 🏷️ Clases y Estructuras

## 🎯 Introducción

> [!info] 💡 ¿Cómo se clasifican y construyen las compuestas?
>
> Por su tabla: **tautología** (todo V), **contradicción** (todo F), **contingencia** (mezcla) — pero solo las fórmulas bien formadas (FBF) admiten tabla. Equivalencia ($\equiv$) y consecuencia ($\vDash$) comparan columnas, y FND/FNC son sus formas canónicas.
>
> ```mermaid
> graph LR
>     A["FBF<br/>sintaxis"] --> B["Tabla<br/>2n filas"]
>     B --> C["Clase<br/>V/F/mezcla"]
>     C --> D["Equiv<br/>FND/FNC"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — FBF, clases y comparación
>
> **FBF:** variable es FBF; si $A,B$ lo son, $\lnot A,(A\land B),(A\lor B),(A\to B),(A\leftrightarrow B)$ también (todo operador binario exige dos operandos: $p\land\land q$ no es FBF).
>
> **Clases:** tautología (todo V, ej. $p\lor\lnot p$), contradicción (todo F), contingencia (mezcla, ej. $p\land q$ con 1V 3F).
>
> **$\equiv$** columnas idénticas (misma función de verdad); **$\vDash$** cuando $A\to B$ es tautología (más fuerte: $p\lor q\not\vDash p$ porque $p=F,q=V$ refuta). **FND** disyunción de $\land$ (lista filas V); **FNC** conjunción de $\lor$ (filas F).

> [!tip] 💡 Cómo clasificar y convertir sin errores
>
> Arma las $2^n$ filas evaluando de adentro afuera; busca el contraejemplo antes de llenar todo (una F tumba tautología). A FND traduce cada fila V a su conjunción; $(p\to q)\land r$ pasa por $(\lnot p\lor q)\land r$ y distribuye a $(\lnot p\land r)\lor(q\land r)$. Ojo: $(p\lor q)\land\lnot q$ da F,V,F,F (equivale a $p\land\lnot q$, el $\lnot q$ mata la primera fila).

> [!example] 🟢 Ejemplo — $(p\to q)\land(\lnot p\to q)\to q$ es tautología
>
> Si $q$ es V, el consecuente salva; si $q$ es F, ambas condicionales exigen $p$ y $\lnot p$ (antecedente imposible) $\therefore$ todo V.

---

## 📋 Tabla Comparativa: Clases y Formas

> [!note] 📋 Qué patrón da cada clase y forma
>
> | Fórmula | Clase/forma (por qué) |
> |---|---|
> | $p\lor\lnot p$ | Tautología (tercero excluido: una siempre V) |
> | $p\land\lnot p$ | Contradicción (nada es y no es) |
> | $p\land q$ | Contingencia (1V 3F) |
> | $(p\to q)\land(q\to p)$ | Contingencia ($\equiv p\leftrightarrow q$: solo coinciden) |
> | $(p\to q)\lor(q\to p)$ | Tautología (una de las dos siempre V) |
> | $(p\land q)\lor(\lnot p\land\lnot q)$ | FND de $p\leftrightarrow q$ (filas V listadas) |
> | $(\lnot p\lor q)\land(p\lor\lnot q)$ | FNC de $p\leftrightarrow q$ (filas F negadas) |
>
> **Conteo:** $2^{2^n}$ funciones ($n=2\to16$, una sola tautología: la constante V).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Contingencia como contradicción:** $p\land q$ tiene una V (no es "siempre F").
> - **$\vDash$ simétrico:** $p\lor q\not\vDash p$ ($p=F,q=V$ refuta: la premisa no garantiza cada parte).
> - **FND con filas F:** FND usa las V; FNC las F (invertidas).
> - **$(p\lor q)\land\lnot q$ en $(V,V)$:** da F (el $\lnot q$ mata la fila).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $p\land\lnot p$, $p\lor\lnot p$, $p\land q$.
> 2. ¿FBF? $p\land\land q$, $(p\to)$, $pq\lor r$.
> 3. Tabla de $(p\lor q)\land\lnot q$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Contradicción; tautología; contingencia.
>
> **2.** No las tres (sintaxis rota).
>
> **3.** F,V,F,F ($\equiv p\land\lnot q$).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $(p\to q)\land(\lnot p\to q)\to q$.
> 5. ¿Vale $p\land q\vDash p\lor r$? ¿Y $p\lor q\vDash p$?
> 6. $(p\leftrightarrow q)$ a FND y FNC.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Tautología.
>
> **5.** Sí ($p$ ya V basta); no ($p=F,q=V$ refuta).
>
> **6.** $(p\land q)\lor(\lnot p\land\lnot q)$; $(\lnot p\lor q)\land(p\lor\lnot q)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $((p\to q)\land(q\to r))\to(p\to r)$.
> 8. FND impar-de-tres (solo 1 o 3 V).
> 9. $p\land\lnot q$ ¿satisfacible? ¿implica a $p$?

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Tautología (silogismo hipotético: encadena).
>
> **8.** 4 términos (uno por fila V).
>
> **9.** Sí (1V de 4); sí ($(p\land\lnot q)\to p$ tautología).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Clasifico con tablas $2^n$.
> - [ ] Decido FBF por sintaxis.
> - [ ] Reconozco $p\lor\lnot p$ y $p\land\lnot p$.
> - [ ] Cuento V/F en contingencias.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Decido tautologías compuestas.
> - [ ] Pruebo equivalencias por columnas.
> - [ ] Decido $\vDash$ con contraejemplos.
> - [ ] Convierto a FND/FNC.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Encadeno silogismos hipotéticos.
> - [ ] Construyo FND desde filas V.
> - [ ] Cuento $2^{2^n}$ funciones.
> - [ ] Identifico equivalencias escondidas.

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
> - [[02 - Operadores Lógicos]] — base: conectivos.
> - [[05 - Propiedades de los operadores lógicos]] — siguiente: leyes.
> - [[06 - Razonamientos]] — $\vDash$ como validez.
> - [[13 - Técnicas de conteo]] — conteo $2^{2^n}$.

---

**Tags:** #lógica #tautología #fbf #unidad1

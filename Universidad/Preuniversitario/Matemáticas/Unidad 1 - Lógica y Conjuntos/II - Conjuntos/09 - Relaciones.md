---
dg-publish: true
---

# 🔗 Relaciones

## 🎯 Introducción

> [!info] 💡 ¿Qué es una relación?
>
> $R\subseteq A\times A$ con propiedades (reflexiva, simétrica, transitiva): equivalencia (R+S+T) parte en clases; orden parcial (R+A+T) dibuja Hasse. La matriz y el dígrafo la muestran.
>
> ```mermaid
> graph LR
>     A["R subset<br/>AxA"] --> B["R+S+T<br/>equiv"]
>     B --> C["R+A+T<br/>orden"]
>     C --> D["Clases<br/>Hasse"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Propiedades y tipos
>
> **Propiedades:** reflexiva ($(a,a)$), simétrica ($(a,b)\to(b,a)$), antisimétrica, transitiva ($(a,b),(b,c)\to(a,c)$).
>
> **Equivalencia:** R+S+T (clases disjuntas que parten $A$). **Orden parcial:** R+A+T (Hasse sin flechas redundantes). **Clausuras:** $r,s,t$ agregan lo mínimo.

> [!tip] 💡 Cómo clasificar relaciones sin olvidar pares
>
> Revisa en orden R, S, T buscando el contraejemplo: $(2,2)$ ausente tumba reflexiva; $(1,2),(2,1)$ sin $(2,2)$ tumba transitiva. Para clausura transitiva agrega los "atajos" ($(1,2),(2,3)\to(1,3)$). Igualdad es R+S+A+T a la vez.

> [!example] 🟢 Ejemplo — $R=\{(1,1),(1,2),(2,1)\}$ en $\{1,2\}$
>
> No reflexiva (falta $(2,2)$); simétrica sí; no transitiva (falta $(2,2)$ de $(2,1),(1,2)$).

---

## 📋 Tabla Comparativa: Relaciones

> [!note] 📋 Qué propiedades tiene cada una
>
> | Relación | R | S | T | Tipo |
> |---|---|---|---|---|
> | $=$ (igualdad) | ✓ | ✓ | ✓ | Equivalencia + orden |
> | $<$ en $\{1,2,3\}$ | ✗ | ✗ | ✓ | Orden estricto |
> | $\le$ | ✓ | ✗ | ✓ | Orden parcial |
> | $\equiv_3$ en $\mathbb{Z}$ | ✓ | ✓ | ✓ | $3$ clases $[0],[1],[2]$ |
> | $a\mid b$ en $\{1,2,4,8\}$ | ✓ | ✗ | ✓ | Cadena $1$-$2$-$4$-$8$ |
>
> **Composición:** $R=\{(1,2)\},S=\{(2,3)\}\therefore S\circ R=\{(1,3)\}$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Simétrica $\therefore$ reflexiva:** no ($R=\{(1,2),(2,1)\}$ sin diagonal).
> - **Antisimétrica = asimétrica:** $=$ es ambas; $<$ solo asimétrica.
> - **$t(R)$ sin atajos:** $(1,2),(2,3)$ exige $(1,3)$.
> - **Clases solapadas:** equivalencia parte (disjuntas, cubren).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $R=\{(1,1),(1,2),(2,1)\}$: R, S, T.
> 2. $R=\{(1,2),(2,3)\}$: ¿transitiva? $t(R)$.
> 3. $<$ en $\{1,2,3\}$: enumera y verifica.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** No; sí; no (falta $(2,2)$).
>
> **2.** No; $t(R)$ agrega $(1,3)$.
>
> **3.** $\{(1,2),(1,3),(2,3)\}$; irreflexiva + transitiva.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Clases de $\equiv_3$ y $\mathbb{Z}/\equiv_3$.
> 5. $a\mid b$ en $\{1,2,4,8\}$: ¿parcial? Maximales.
> 6. $R^{-1}$ y $S\circ R$ ($R=\{(1,2)\},S=\{(2,3)\}$).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $[0],[1],[2]$.
>
> **5.** Sí; maximal $8$, minimal $1$.
>
> **6.** $\{(2,1)\}$; $\{(1,3)\}$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Equivalencia $\leftrightarrow$ partición ($\{\{1,2\},\{3,4\}\}$).
> 8. Clausuras $r,s,t$ de $\{(1,2),(2,3)\}$.
> 9. $t(R)$ por potencias hasta $R^n$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Clases = bloques.
>
> **8.** $r$ agrega diagonal; $s$ invierte; $t$ atajos.
>
> **9.** $t(R)=R\cup R^2$ ($n=3$).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico R, S, T con contraejemplos.
> - [ ] Hallo clausuras mínimas.
> - [ ] Represento con matriz/dígrafo.
> - [ ] Enumero $<$ finitos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo clases y cocientes.
> - [ ] Dibujo Hasse (cadenas y diamantes).
> - [ ] Identifico maximales/minimales.
> - [ ] Compongo e invierto.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Pruebo equivalencia-partición.
> - [ ] Calculo las tres clausuras.
> - [ ] Caracterizo $R\circ R^{-1}\subseteq R$.
> - [ ] Itero potencias hasta $R^n$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §9.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 5.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[07 - Pares ordenados y producto cartesiano]] — base: $R\subseteq\times$.
> - [[10 - Funciones en Conjuntos]] — siguiente: funciones.
> - [[05 - Predicados de una variable]] — $P(x,y)$ como relación.
> - [[05 - Relación de orden]] — orden en $\mathbb{R}$.

---

**Tags:** #conjuntos #relaciones #equivalencia #unidad1

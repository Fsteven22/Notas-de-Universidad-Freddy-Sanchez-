---
dg-publish: true
---

# ⚖️ Relación de Orden

## 🎯 Introducción

> [!info] 💡 ¿Qué es el orden en $\mathbb{R}$?
>
> $a<b\iff b-a$ positivo: compatible con $+$ (se preserva) pero $\times-1$ invierte. Cotas, $\sup$/$\inf$ e intervalos describen conjuntos; $\mathbb{Q}$ es denso pero $\mathbb{R}$ es completo.
>
> ```mermaid
> graph LR
>     A["a menor b<br/>resta +"] --> B["Suma<br/>preserva"]
>     B --> C["Por -1<br/>invierte"]
>     C --> D["Sup/inf<br/>cotas"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[05-sup.png]]

> [!tip] 💡 Visual — Supremo e ínfimo
>
> En $(0,1)$ no hay máx/mín pero $\sup=1$, $\inf=0$: el supremo es la menor cota superior aunque no pertenezca al conjunto.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Axiomas, intervalos y cotas
>
> **Orden:** reflexiva, antisimétrica, transitiva; total en $\mathbb{R}$ ($a<b\iff b-a\in\mathbb{R}^+$).
>
> **Reglas:** $a<b\therefore a+c<b+c$; $a<b,c<0\therefore ac>bc$ (invierte). **Cotas:** $\sup$ (menor superior), $\inf$ (mayor inferior).

> [!tip] 💡 Cómo resolver inecuaciones sin fallar el intervalo
>
> Despeja normal pero al dividir por negativo **invierte** ($-3x\ge9\therefore x\le-3$) — marca ese paso. Negar invierte cada símbolo ($x<5\to x\ge5$); en dobles ($5\le2x-1<11$) opera las tres partes a la vez.

> [!example] 🟢 Ejemplo — $5\le2x-1<11$ paso a paso
>
> Suma $1$: $6\le2x<12$; divide $2$: $3\le x<6\therefore[3,6)$ (verifica $x=3\to5$ ✓, $x=6\to11$ excluido ✓).

---

## 📋 Tabla Comparativa: Conjuntos y Cotas

> [!note] 📋 Qué tiene cada conjunto
>
> | Conjunto | máx/mín | $\sup$/$\inf$ | Bien ordenado |
> |---|---|---|---|
> | $\{1,2,3,6\}$ | $6/1$ | $6/1$ | Sí (finito) |
> | $(0,1)$ | Ninguno | $1/0$ | No |
> | $\mathbb{N}$ | mín $0$ | $\inf0$, sin $\sup$ | Sí |
> | $\mathbb{Q}$ | — | Denso (entre $a<b$ hay $q$) | No |
>
> **Densidad:** $n(b-a)>1$, $m=\min\{k:k/n>a\}\therefore a<m/n<b$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$-a<-b$ desde $a<b$:** invierte ($-a>-b$).
> - **$a<b\therefore a^2<b^2$:** $-3<2$ pero $9>4$.
> - **Negar $2<x<7$ como $2\ge x\ge7$:** es $x\le2\lor x\ge7$.
> - **$\sup=\max$ siempre:** en $(0,1)$ el sup no pertenece.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. V/F: $a<b\to a+5<b+5$; $a<b\to-a<-b$; $a<b\to a^2<b^2$.
> 2. Resuelve: $2x+3<7$, $-3x\ge9$, $5\le2x-1<11$.
> 3. Nega: $x<5$, $2<x<7$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** V; F (invierte); F ($-3<2$).
>
> **2.** $(-\infty,2)$; $(-\infty,-3]$; $[3,6)$.
>
> **3.** $x\ge5$; $x\le2\lor x\ge7$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $B=(0,1)$: máx/mín, $\sup$/$\inf$, ¿bien ordenado?
> 5. Prueba $0<a<b\therefore1/b<1/a$.
> 6. Racional entre $\sqrt2,\sqrt3$ y entre $\pi,e$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Sin máx/mín; $\sup1$, $\inf0$; no.
>
> **5.** Divide por $ab>0$ (preserva) e invierte roles.
>
> **6.** $1.5$; $3$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Arquímedes: $\forall\varepsilon>0\;\exists n\;1/n<\varepsilon$.
> 8. $\sup(A)$ único si existe.
> 9. Orden lexicográfico en $\mathbb{N}\times\mathbb{N}$: ¿total? ¿bien?

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $n>1/\varepsilon$ por Arquímedes.
>
> **8.** $s_1\le s_2\le s_1\therefore s_1=s_2$.
>
> **9.** Sí total, sí bien; $(1,5)<(2,1)<(2,3)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico V/F de suma e inversión.
> - [ ] Resuelvo lineales invirtiendo con $-$.
> - [ ] Niego desigualdades simples y dobles.
> - [ ] Comparo en la recta.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Pruebo reflexiva/antisimétrica/transitiva.
> - [ ] Hallo $\sup$/$\inf$ sin máx/mín.
> - [ ] Demuestro $1/b<1/a$.
> - [ ] Intercalo racionales (densidad).

> [!note] 📋 Nivel Avanzado
>
> - [ ] Pruebo Arquímedes y densidad de $\mathbb{Q}$.
> - [ ] Demuestro unicidad del $\sup$.
> - [ ] Clasifico órdenes lexicográficos.
> - [ ] Construyo parciales no totales.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. Grimaldi, *Matemática Discreta*, Pearson — cap. de relaciones.
>
> [2] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §9.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Conjuntos Numéricos]] — $\mathbb{R}$ como base.
> - [[11 - Inecuaciones]] — inecuaciones a fondo.
> - [[13 - Técnicas de conteo]] — bien orden y conteo.
> - [[09 - Relaciones]] — orden como relación.

---

**Tags:** #números-reales #orden #supremo #unidad2

---
dg-publish: true
---

# 🔢 Números y Decimales

## 🎯 Introducción

> [!info] 💡 ¿Qué son los reales y cómo se escriben?
>
> $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$ con $\mathbb{I}=\mathbb{R}-\mathbb{Q}$ — y el decimal delata cada uno: finito o periódico $\iff$ racional (el denominador manda: solo $2^m5^n$ da finito), no periódico $\iff$ irracional.
>
> ```mermaid
> graph LR
>     A["N Z Q<br/>cadena"] --> B["R<br/>Q union I"]
>     B --> C["Decimal<br/>delata"]
>     C --> D["Fracción<br/>10k resta"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[01-conjuntos-numericos.png]]

> [!tip] 💡 Visual — Jerarquía y decimales
>
> Rectángulos $N\subset Z\subset Q\subset R$; $0.333\ldots=1/3$ vive en $Q$ (periódico) mientras $0.101001\ldots$ cae en $I$ (sin período) — el decimal decide la capa.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Conjuntos y expansiones
>
> **$\mathbb{N},\mathbb{Z}$:** contar y deudas (cerrados en $+,\times$; $\mathbb{Z}$ además en $-$). **$\mathbb{Q}=\{p/q\}$:** resuelve $2x=3$; denso y numerable.
>
> **$\mathbb{R}=\mathbb{Q}\cup\mathbb{I}$:** completo (sin huecos: $\{x:x^2<2\}$ necesita $\sqrt2$). **Decimal:** finito $\iff$ denominador $2^m5^n$ (porque completa a potencia de $10$); periódico puro/mixto según otros primos; $0.\bar9=1$ ($10x-x=9$).

> [!tip] 💡 Cómo clasificar y convertir sin dudar
>
> Mira el decimal primero (periódico $\to Q$, no $\to I$), pero evalúa raíces ($\sqrt9=3$ es natural). A fracción: corre el período con $10^k$ y resta ($0.1\bar6$: $100x-10x=15\therefore x=1/6$). A decimal: factoriza el denominador simplificado antes de predecir ($30=2\cdot3\cdot5$ avisa mixto).

> [!example] 🟢 Ejemplo — $17/30$ y $0.3737\ldots$
>
> $30=2\cdot3\cdot5\therefore$ mixto $0.5\bar6$ ✓. $x=0.3737\ldots\therefore99x=37\therefore37/99$ (divide y verifica ✓).

---

## 📋 Tabla Comparativa: Conjuntos y Decimales

> [!note] 📋 Qué propiedad y expansión corresponde
>
> | Conjunto | Clave (por qué) | Decimal |
> |---|---|---|
> | $\mathbb{N}$ | Contar (Peano) | Enteros $\ge0$ |
> | $\mathbb{Z}$ | Resta cerrada (deudas) | Enteros con signo |
> | $\mathbb{Q}$ | $p/q$ (denso: promedios) | Finito/periódico |
> | $\mathbb{I}$ | No periódicos | $\sqrt2,\pi,0.101\ldots$ |
> | $\mathbb{R}$ | Completo (cierra huecos) | Todos |
>
> | Fracción | Denominador | Sale |
> |---|---|---|
> | $3/8$ | $2^3$ | $0.375$ finito |
> | $5/6$ | $2\cdot3$ | $0.8\bar3$ mixto |
> | $2/7$ | $7$ | $0.\overline{285714}$ puro |
>
> **Cerraduras:** $\mathbb{N}$ no resta; $\mathbb{Z}$ no divide; $\mathbb{Q}$ todo salvo $\div0$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\sqrt9$ irracional:** es $3$ (el valor manda, no el símbolo).
> - **$0.999\ldots<1$:** es $=1$ ($10x-x=9$ lo prueba).
> - **$22/7=\pi$:** $3.142857\neq3.141592$ (aproxima, no iguala).
> - **Denominador sin simplificar:** reduce antes ($6/15=2/5$ finito, no periódico).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Sistema mínimo de $7,-3,2/5,\sqrt9,\sqrt7,\pi,0.333\ldots$.
> 2. A fracción: $0.\bar6$, $2.\bar4$, $0.1\bar6$.
> 3. A decimal: $3/8$, $5/6$, $2/7$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\mathbb{N}$: $7,\sqrt9$; $\mathbb{Z}$: $-3$; $\mathbb{Q}$: $2/5,0.333\ldots$; $\mathbb{I}$: $\sqrt7,\pi$.
>
> **2.** $2/3$; $22/9$; $1/6$.
>
> **3.** $0.375$; $0.8\bar3$; $0.\overline{285714}$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $17/30$: tipo, decimal y períodos.
> 5. Racional entre $\sqrt2,\sqrt3$; irracional entre $1,2$.
> 6. $r\in\mathbb{Q},x\in\mathbb{I}\therefore r+x\in\mathbb{I}$ (prueba).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Mixto; $0.5\bar6$; período $1$.
>
> **5.** $1.5$; $\sqrt2$.
>
> **6.** Si fuese $q\in\mathbb{Q}\therefore x=q-r\in\mathbb{Q}$ (contradicción).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Densidad de $\mathbb{I}$ con $q\sqrt2$.
> 8. $\mathbb{A}$ numerable $\therefore\mathbb{T}$ no.
> 9. Períodos de $1/13$ y $1/17$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $q$ racional entre $a/\sqrt2,b/\sqrt2$; $q\sqrt2$ irracional medio.
>
> **8.** Polinomios racionales numerables.
>
> **9.** $6$ y $16$ (orden de $10\bmod p$).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Clasifico por decimal y valor.
> - [ ] Convierto periódico a fracción.
> - [ ] Predigo finito/mixto/puro.
> - [ ] Pruebo $0.\bar9=1$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Verifico fracciones dividiendo.
> - [ ] Intercalo racionales/irracionales.
> - [ ] Sumo racional + irracional.
> - [ ] Demuestro criterio $2^m5^n$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro densidad de $\mathbb{I}$.
> - [ ] Distingo $\aleph_0$ de continuo.
> - [ ] Calculo períodos modulares.
> - [ ] Explico $0.1+0.2$ en máquina.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 1.
>
> [2] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §1.2.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Tipos y cardinalidad]] — $\mathbb{N},\mathbb{Z},\mathbb{Q}$ como conjuntos.
> - [[05 - Relación de orden]] — siguiente: orden.
> - [[13 - Técnicas de conteo]] — numerabilidad de $\mathbb{Q}$.
> - [[15 - Sucesiones]] — decimales como límites.

---

**Tags:** #números-reales #conjuntos #decimales #unidad2

---
dg-publish: true
---

# ➗ Funciones Racionales

## 🎯 Introducción

> [!info] 💡 ¿Qué es una función racional?
>
> $P(x)/Q(x)$: ceros de $P$, verticales en ceros de $Q$, horizontal/oblicua por grados, huecos donde se cancela — y el signo sale de la tabla de críticos.
>
> ```mermaid
> graph LR
>     A["P/Q<br/>ceros"] --> B["Verticales<br/>Q=0"]
>     B --> C["Horiz<br/>grados"]
>     C --> D["Signo<br/>tabla"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Asíntotas, huecos y signo
>
> **Dominio:** $\mathbb{R}\setminus\{\text{ceros de }Q\}$. **Vertical:** $x=a$ si $Q(a)=0$ (sin cancelar). **Hueco:** ○ si el factor cancela.
>
> **Horizontal:** $\deg P<\deg Q\to y=0$; iguales $\to$ cociente líderes; $P$ mayor en $1\to$ oblicua. **Signo:** tabla con ceros y verticales.

> [!tip] 💡 Cómo bosquejar racionales sin errores
>
> Factoriza todo primero y cancela — lo cancelado es hueco ○, lo que queda en el denominador es vertical. La horizontal sale de comparar grados (no dividas). Para inecuaciones lleva todo a un lado y lee la tabla: los extremos con $=$ se incluyen **solo** si son ceros, nunca si son verticales.

> [!example] 🟢 Ejemplo — $(2x+1)/(x-1)\le0$
>
> Críticos $-1/2$ (cero) y $1$ (vertical): signos $+,-,+$; negativo en $(-1/2,1)$ e incluye el cero $\therefore[-1/2,1)$ (el $1$ nunca se incluye ✓).

---

## 📋 Tabla Comparativa: Asíntotas

> [!note] 📋 Qué asíntota sale según grados
>
> | Grados | Horizontal/oblicua | Ejemplo |
> |---|---|---|
> | $\deg P<\deg Q$ | $y=0$ | $1/x$ |
> | Iguales | Cociente líderes | $(2x+1)/(x-1)$: $y=2$ |
> | $P$ mayor en $1$ | Oblicua (divide) | $(x^2+1)/x$: $y=x$ |
> | Cancela factor | Hueco ○ | $(x^2-1)/(x-1)$: ○ en $(1,2)$ |
>
> **Parciales:** $(2x+1)/(x^2-1)=A/(x-1)+B/(x+1)$ con $A=3/2,B=1/2$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$[-1/2,1)$ con extremos cruzados:** el cero se incluye, la vertical jamás.
> - **Hueco como vertical:** si cancela, es ○ (no asíntota).
> - **Horizontal dividiendo siempre:** compara grados primero.
> - **Corte con $y=1$ asumido:** si $y=1$ es asíntota, no hay corte.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $\text{Dom}$ de $1/(x-3)$, $(x+1)/(x^2-4)$.
> 2. Ceros y verticales de $(x-1)/(x+2)$.
> 3. Horizontal de $1/x$, $(2x+1)/(x-1)$, $(x^2+1)/x$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\mathbb{R}\setminus\{3\}$; $\mathbb{R}\setminus\{\pm2\}$.
>
> **2.** Cero $1$; vertical $-2$.
>
> **3.** $y=0$; $y=2$; oblicua $y=x$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $(2x+1)/(x-1)\le0$ con tabla.
> 5. Intersección de $(x-1)/(x+2)$ con $y=1$.
> 6. $1/(x-1)>2$ llevando a un lado.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $[-1/2,1)$.
>
> **5.** Ninguna ($y=1$ asíntota).
>
> **6.** $(1,3/2)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Bosqueja $(x^2-4)/(x^2-9)$ (signo $+$).
> 8. $(x^2+1)/(x^2-1)$: paridad y asíntotas.
> 9. $\lim_{x\to\pm\infty}(3x^2+1)/(2x^2-x)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $+$ en $(-\infty,-3)\cup[-2,2]\cup(3,\infty)$.
>
> **8.** Par; $x=\pm1$; $y=1$.
>
> **9.** $3/2$ (cociente líderes).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo dominios excluyendo ceros de $Q$.
> - [ ] Distingo ceros, verticales y huecos.
> - [ ] Leo horizontales por grados.
> - [ ] Evalúo signos por tramos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Bosquejo con 4 pasos (cero, vertical, horizontal, signo).
> - [ ] Resuelvo inecuaciones con tabla.
> - [ ] Hallo oblicuas dividiendo.
> - [ ] Detecto cortes imposibles.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Bosquejo con 4+ críticos.
> - [ ] Demuestro $y=0$ dividiendo por $x^m$.
> - [ ] Descompongo en parciales.
> - [ ] Calculo límites al infinito.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 3 (racionales).
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. de funciones.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[11 - Funciones polinomiales]] — $P$ y $Q$ como base.
> - [[11 - Inecuaciones]] — tablas de signos.
> - [[02 - Representación gráfica]] — huecos y oblicuas.
> - [[10 - Función inversa de una función biyectiva]] — inversa racional.

---

**Tags:** #funciones #racionales #asintotas #unidad3

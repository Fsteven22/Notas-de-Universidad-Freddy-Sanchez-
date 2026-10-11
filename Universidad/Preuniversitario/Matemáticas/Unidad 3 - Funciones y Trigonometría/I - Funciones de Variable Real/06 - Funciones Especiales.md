---
dg-publish: true
---

# ⭐ Funciones Especiales

## 🎯 Introducción

> [!info] 💡 ¿Qué funciones especiales hay?
>
> $|x|$, piso $\lfloor x\rfloor$, techo $\lceil x\rceil$, signo, parte fraccionaria, Heaviside $H$ y sigmoide $\sigma$: modelan distancias, escalones y conmutaciones — con saltos donde hay que dibujar ○/●.
>
> ```mermaid
> graph LR
>     A["|x|<br/>distancia"] --> B["Piso<br/>escalones"]
>     B --> C["H<br/>conmuta"]
>     C --> D["Sigma<br/>suaviza"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Las seis especiales
>
> **$|x|$:** $-x$ si $x<0$, $x$ si $x\ge0$. **Piso:** mayor entero $\le x$. **Techo:** menor entero $\ge x$. **Signo:** $-1,0,1$.
>
> **Fraccionaria:** $\{x\}=x-\lfloor x\rfloor$. **Heaviside:** $0$ si $t<0$, $1$ si $t\ge0$. **Sigmoide:** $1/(1+e^{-x})$.

> [!tip] 💡 Cómo no enredarse con pisos negativos
>
> El piso siempre baja: $\lfloor-1.2\rfloor=-2$ (no $-1$). Verifica con $\{x\}+\lfloor x\rfloor=x$: $-1.2=-2+0.8$ ✓. Para $|ax-b|$, el cero $x=b/a$ parte los tramos — escríbelo primero.

> [!example] 🟢 Ejemplo — $|2x-4|$ por tramos
>
> Cero en $x=2$: $4-2x$ si $x<2$, $2x-4$ si $x\ge2$. Vértice $(2,0)$; continua en $2$ pero no derivable (laterales $\mp2$).

---

## 📋 Tabla Comparativa: Especiales

> [!note] 📋 Qué hace cada una y dónde salta
>
> | Función | Valor tipo | Salto en |
> |---|---|---|
> | $\|x\|$ | Distancia a $0$ | Ninguno (pico en $0$) |
> | $\lfloor x\rfloor$ | Escalones | Cada entero |
> | $\lceil x\rceil$ | Escalones arriba | Cada entero |
> | $\text{sgn}(x)$ | $-1,0,1$ | $x=0$ |
> | $H(t)$ | $0/1$ (conmuta) | $t=0$ |
> | $\sigma(x)$ | $(0,1)$ suave | Ninguno |
>
> **Identidad:** $\lfloor x\rfloor+\{x\}=x$; **integral:** $\int_0^3\lfloor x\rfloor dx=0+1+2=3$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\lfloor-1.2\rfloor=-1$:** es $-2$ (piso baja siempre).
> - **$|x|$ derivable en $0$:** no (laterales $\pm1$).
> - **$\lim_{x\to0}\text{sgn}(x)$:** no existe ($-1\neq1$).
> - **$H(t-3)$ activa en $t>3$:** incluye $t=3$ ($H(0)=1$).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $|{-7}|$, $\lfloor3.2\rfloor$, $\lceil-2.3\rceil$, $\text{sgn}(-5)$, $\{4.6\}$.
> 2. Grafica $|x-1|$ (vértice).
> 3. $\lfloor-1.2\rfloor$ vs $-\lfloor1.2\rfloor$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $7,3,-2,-1,0.6$.
>
> **2.** Vértice $(1,0)$.
>
> **3.** $-2\neq-1$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Continuidad en $0$ de $|x|$, $\lfloor x\rfloor$, $\text{sgn}(x)$.
> 5. $H(t-3)$: ¿cuándo se activa?
> 6. $\sigma(0)$, $\lim_{x\to\infty}\sigma(x)$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Solo $|x|$.
>
> **5.** $t\ge3$.
>
> **6.** $1/2$, $1$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $\lfloor x+n\rfloor=\lfloor x\rfloor+n$ ($n\in\mathbb{Z}$).
> 8. Derivada de $|x|$ ($x\neq0$).
> 9. Aproxima $H$ con $\sigma(kx)$, $k\to\infty$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $x+n$ desplaza la parte entera.
>
> **8.** $\text{sgn}(x)$ ($1$ si $x>0$, $-1$ si $x<0$).
>
> **9.** Pendiente en $0$ crece sin cota.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Evalúo $|x|$, piso, techo, signo.
> - [ ] Grafico $|x-h|$ con vértice.
> - [ ] Distingo piso negativo del opuesto.
> - [ ] Uso $\{x\}+\lfloor x\rfloor=x$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Decido continuidad en saltos.
> - [ ] Escribo $|ax-b|$ por tramos.
> - [ ] Activo Heaviside con retardo.
> - [ ] Evalúo límites de $\sigma$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro traslaciones enteras del piso.
> - [ ] Derivo $|x|$ fuera del origen.
> - [ ] Integro escalones por tramos.
> - [ ] Aproximo $H$ con $\sigma$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 2 (especiales).
>
> [2] K. Rosen, *Matemática Discreta*, McGraw-Hill — §2.3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Funciones definidas por tramos]] — tramos base.
> - [[09 - Valor Absoluto]] — ecuaciones con $|x|$.
> - [[13 - Funciones exponenciales]] — base de $\sigma$.
> - [[02 - Representación gráfica]] — ○/● y saltos.

---

**Tags:** #funciones #especiales #piso #heaviside #unidad3

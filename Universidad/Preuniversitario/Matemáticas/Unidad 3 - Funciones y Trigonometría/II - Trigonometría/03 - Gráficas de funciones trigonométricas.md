---
dg-publish: true
---

# 🌊 Gráficas Trigonométricas

## 🎯 Introducción

> [!info] 💡 ¿Cómo se grafican $\sin,\cos,\tan$?
>
> $y=A\sin(Bx-C)+D$: $A$ amplitud, $T=2\pi/B$ período, $C/B$ fase, $D$ eje. $\tan$ repite cada $\pi$ con asíntotas donde $\cos=0$.
>
> ```mermaid
> graph LR
>     A["A<br/>amplitud"] --> B["T=2pi/B<br/>período"]
>     B --> C["Fase<br/>C/B"]
>     C --> D["Eje<br/>D"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U3-onda.png]]

> [!tip] 💡 Visual — $y=2\sin(3x-\pi)+1$
>
> Amplitud $2$, período $2\pi/3$, fase $\pi/3$, eje $y=1$ (rango $[-1,3]$): cada parámetro se lee directo de la fórmula.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Parámetros y base
>
> **Base:** $\sin,\cos$ con $A=1$, $T=2\pi$; $\tan$ con $T=\pi$, asíntotas $x=\pi/2+k\pi$.
>
> **Transformada:** $A$ (altura), $B$ ($T=2\pi/B$), $C$ (fase $C/B$), $D$ (desplaza eje). **Suma:** $\sin x+\cos x=\sqrt2\sin(x+\pi/4)$.

> [!tip] 💡 Cómo leer $A,B,C,D$ sin confundir
>
> Factoriza $B$ primero: $3x-\pi=3(x-\pi/3)\therefore$ fase $\pi/3$ a la derecha (el signo engaña si no factorizas). La amplitud es $|A|$ y el eje es $D$ — el rango sale solo: $[D-A,D+A]$.

> [!example] 🟢 Ejemplo — $y=2\sin(3x-\pi)+1$
>
> $A=2$, $T=2\pi/3$, fase $\pi/3$, rango $[-1,3]$ (verifica $x=\pi/3\to1$, máximo $3$ en $x=\pi/2$ ✓).

---

## 📋 Tabla Comparativa: Base y Transformadas

> [!note] 📋 Qué cambia cada parámetro
>
> | Función | $A,T$ | Fase/eje |
> |---|---|---|
> | $\sin x$, $\cos x$ | $1,2\pi$ | Eje $0$ |
> | $2\sin x$ | $2,2\pi$ | Eje $0$ |
> | $\cos2x$ | $1,\pi$ | Desfase $0$ |
> | $\cos(x-\pi/2)$ | $1,2\pi$ | $=\sin x$ |
> | $\tan2x$ | $-, \pi/2$ | Asíntotas $\pi/4+k\pi/2$ |
>
> **Combinada:** $\sin2x+\cos3x$ con $T=2\pi$ (mcm de $\pi,2\pi/3$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Fase $=-\pi$:** factoriza $B$: $3x-\pi=3(x-\pi/3)$ (fase $+\pi/3$).
> - **$T=2\pi$ siempre:** es $2\pi/B$ ($\cos2x\to\pi$).
> - **$\tan$ con $T=2\pi$:** es $\pi$ (asíntotas cada $\pi$).
> - **Rango sin $D$:** $[D-A,D+A]$, no $[-A,A]$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Amplitud y período de $\sin x$, $\cos x$, $2\sin x$.
> 2. Ceros de $\sin x$ en $[0,2\pi]$.
> 3. Par/impar de $\sin,\cos,\tan$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $1,2\pi$; $1,2\pi$; $2,2\pi$.
>
> **2.** $0,\pi,2\pi$.
>
> **3.** Impar, par, impar.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $y=2\sin(3x-\pi)+1$: parámetros y rango.
> 5. $y=\tan(2x)$: período y asíntotas.
> 6. Modela $d=3\sin(2t)$: amplitud y período.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $2,2\pi/3,\pi/3,[-1,3]$.
>
> **5.** $T=\pi/2$; $x=\pi/4+k\pi/2$.
>
> **6.** $3,\pi$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $y=\sin x+\cos x$ como seno único.
> 8. Grafica $y=x\sin x$ (envolventes).
> 9. Marea $h=2+1.5\sin(\pi t/6)$: extremos y período.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\sqrt2\sin(x+\pi/4)$.
>
> **8.** Oscila entre $y=\pm x$.
>
> **9.** $3.5$ en $t=3$, $0.5$ en $t=9$; $T=12$ h.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico $A,T$ de $\sin,\cos$.
> - [ ] Hallo ceros en $[0,2\pi]$.
> - [ ] Ubico asíntotas de $\tan$.
> - [ ] Clasifico paridad.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Leo $A,B,C,D$ factorizando.
> - [ ] Hallo fases y rangos.
> - [ ] Grafico $\tan$ transformada.
> - [ ] Modelo oscilaciones simples.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Sumo senos en uno solo.
> - [ ] Grafico con envolventes.
> - [ ] Hallo períodos de sumas (mcm).
> - [ ] Modelo mareas con fase.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 5 (gráficas trig).
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. de trigonometría.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Funciones trigonométricas elementales]] — base: valores y signos.
> - [[02 - Representación gráfica]] — transformaciones generales.
> - [[04 - Funciones trigonométricas inversas]] — siguiente: $\arcsin$.
> - [[05 - Identidades trigonométricas]] — suma a seno único.

---

**Tags:** #trigonometria #graficas #amplitud #unidad3

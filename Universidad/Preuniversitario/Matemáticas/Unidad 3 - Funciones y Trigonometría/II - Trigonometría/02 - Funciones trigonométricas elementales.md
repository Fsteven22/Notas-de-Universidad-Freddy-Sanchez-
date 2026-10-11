---
dg-publish: true
---

# 📐 Funciones Trigonométricas Elementales

## 🎯 Introducción

> [!info] 💡 ¿Qué son $\sin,\cos,\tan$?
>
> Razones en el triángulo ($op/hip$, $ady/hip$, $op/ady$) extendidas al círculo unitario: el cuadrante da el signo, el ángulo de referencia da el valor, y $\sin^2+\cos^2=1$ las ata.
>
> ```mermaid
> graph LR
>     A["Triángulo<br/>op/hip"] --> B["Círculo<br/>unitario"]
>     B --> C["Signo<br/>cuadrante"]
>     C --> D["Valor<br/>referencia"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U3-trig.png]]

---

## 📋 Definición Formal

> [!note] 📋 Definición — Razones, signos y fundamental
>
> **Razones:** $\sin=op/hip$, $\cos=ady/hip$, $\tan=\sin/\cos$; $\sec,\csc,\cot$ recíprocas.
>
> **Signos (I→IV):** $\sin:+ + - -$; $\cos:+ - - +$; $\tan:+ - + -$. **Fundamental:** $\sin^2\theta+\cos^2\theta=1$.

> [!tip] 💡 Cómo hallar valores sin calculadora
>
> Reduce al ángulo de referencia (distancia al eje $x$) y pega el signo del cuadrante: $210°\to30°$ en III $\therefore\sin=-1/2$. Con una razón y el cuadrante, la fundamental da las demás ($\sin=3/5$ en II $\therefore\cos=-4/5$).

> [!example] 🟢 Ejemplo — Triángulo $3$-$4$-$5$
>
> Agudo opuesto al $3$: $\sin=3/5$, $\cos=4/5$, $\tan=3/4$ (verifica $9/25+16/25=1$ ✓).

---

## 📋 Tabla Comparativa: Valores Exactos

> [!note] 📋 Qué valor tiene cada ángulo notable
>
> | $\theta$ | $\sin$ | $\cos$ | $\tan$ |
> |---|---|---|---|
> | $30°$ ($\pi/6$) | $1/2$ | $\sqrt3/2$ | $\sqrt3/3$ |
> | $45°$ ($\pi/4$) | $\sqrt2/2$ | $\sqrt2/2$ | $1$ |
> | $60°$ ($\pi/3$) | $\sqrt3/2$ | $1/2$ | $\sqrt3$ |
> | $0°$ | $0$ | $1$ | $0$ |
> | $90°$ | $1$ | $0$ | — ($\cot=0$) |
>
> **Derivadas:** $\tan^2+1=\sec^2$ (divide fundamental por $\cos^2$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Signo del cuadrante olvidado:** $\tan135°=-1$, no $1$.
> - **$\sin30°=\sqrt3/2$:** es $1/2$ (el $\sqrt3/2$ es $\cos30°$).
> - **$\text{Dom}(\tan)=\mathbb{R}$:** excluye $\pi/2+k\pi$.
> - **$\sin^2+\cos^2=1$ solo en agudos:** vale para todo $\theta$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $3$-$4$-$5$: $\sin,\cos,\tan$ del agudo opuesto al $3$.
> 2. Signo de $\sin210°$, $\cos300°$, $\tan135°$.
> 3. $\tan45°$, $\sec0°$, $\cot90°$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $3/5,4/5,3/4$.
>
> **2.** $-$, $+$, $-$.
>
> **3.** $1,1,0$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Si $\sin=3/5$ en II: $\cos,\tan$.
> 5. Referencia de $210°,300°,135°$ y valores del $\sin$.
> 6. $\text{Dom}(\tan)$ y asíntotas.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $-4/5,-3/4$.
>
> **5.** $30°,60°,45°$; $-1/2,-\sqrt3/2,\sqrt2/2$.
>
> **6.** $x\neq\pi/2+k\pi$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Si $\tan=2$ (cuadrante I): $\sin,\cos$.
> 8. Simplifica $(\sin\theta+\cos\theta)^2$.
> 9. $\theta$ con $\sin\theta=1/2$ en $[0,2\pi)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $2/\sqrt5,1/\sqrt5$.
>
> **8.** $1+\sin2\theta$.
>
> **9.** $\pi/6,5\pi/6$ (I y II).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo razones en triángulos.
> - [ ] Asigno signos por cuadrante.
> - [ ] Memorizo valores de $30°,45°,60°$.
> - [ ] Verifico la fundamental.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo razones desde una dada.
> - [ ] Reduzco a ángulos de referencia.
> - [ ] Deduzco $\tan^2+1=\sec^2$.
> - [ ] Determino dominios con asíntotas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro la fundamental en el círculo.
> - [ ] Resuelvo $\tan$ dado con dos signos.
> - [ ] Simplifico con ángulo doble.
> - [ ] Hallo todos los $\theta$ de un valor.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 5 (trigonometría).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de trigonometría.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Ángulos y sus medidas]] — base: radianes y referencia.
> - [[05 - Identidades trigonométricas]] — identidades a fondo.
> - [[03 - Gráficas de funciones trigonométricas]] — siguiente: ondas.
> - [[02 - Coordenadas polares]] — $x=r\cos\theta$.

---

**Tags:** #trigonometria #seno #coseno #unidad3

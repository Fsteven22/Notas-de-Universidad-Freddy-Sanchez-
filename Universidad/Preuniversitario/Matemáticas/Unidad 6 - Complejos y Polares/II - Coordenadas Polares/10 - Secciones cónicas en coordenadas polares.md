---
dg-publish: true
---

# 🪐 Cónicas en Polares

## 🎯 Introducción

> [!info] 💡 ¿Qué forma tienen las cónicas en polares?
>
> $r=\ell/(1+e\cos\theta)$ con el foco en el polo: $e$ decide (elipse, parábola, hipérbola), $\ell$ escala. Perihelio $r_p=\ell/(1+e)$, afelio $r_a=\ell/(1-e)$ — Kepler en una línea.
>
> ```mermaid
> graph LR
>     A["r=l/(1+e cos)<br/>foco en polo"] --> B["e menor 1<br/>elipse"]
>     B --> C["e=1<br/>parábola"]
>     C --> D["e mayor 1<br/>hipérbola"]
>     style A fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-conicaspolar.png]]

> [!tip] 💡 Visual — Misma $\ell$, distinto $e$
>
> Con $e=0.5$ la curva se cierra (elipse), con $e=1$ escapa por un lado (parábola) y con $e=1.5$ abre dos ramas (hipérbola) — todo lo decide el denominador $1+e\cos\theta$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Ecuación focal y elementos
>
> **Ecuación:** $r=\ell/(1+e\cos\theta)$ (directriz $x=d$, $\ell=ed$). **Clasificación:** $0\le e<1$ elipse; $e=1$ parábola; $e>1$ hipérbola.
>
> **Elementos:** $a=\ell/|1-e^2|$, $c=ae$, $r_p=\ell/(1+e)$, $r_a=\ell/(1-e)$; Kepler $T^2=a^3$ (años, UA).

> [!tip] 💡 Cómo identificar cónicas polares sin dudar
>
> Normaliza dividiendo por el término independiente hasta forma $1+e\cos\theta$: el coeficiente de $\cos$ es $e$ y el numerador es $\ell$. El perihelio está en $\theta=0$ con $+\cos$ (denominador máximo) — si la ecuación trae $-\cos$, el perihelio se muda a $\theta=\pi$.

> [!example] 🟢 Ejemplo — $r=12/(3+4\cos\theta)$
>
> Divide entre $3$: $r=4/(1+(4/3)\cos\theta)\therefore\ell=4$, $e=4/3>1$ (hipérbola). $a=4/(16/9-1)=36/7$, $c=48/7$; vértice en $\theta=0$: $r=12/7$; directriz $x=\ell/e=3$ (derecha del foco).

---

## 📋 Tabla Comparativa: Cónicas por $e$

> [!note] 📋 Qué curva sale según $e$
>
> | $e$ | Cónica | $r_p$, $r_a$ | Ejemplo orbital |
> |---|---|---|---|
> | $0$ | Círculo | $r=\ell$ | Órbita circular |
> | $0.4$ | Elipse | $1.071$, $2.5$ (con $\ell=1.5$) | Planeta $a=1.786$ UA |
> | $1$ | Parábola | $r_{\min}=\ell/2$ | Cometa de escape |
> | $4/3$ | Hipérbola | Solo $r_p=12/7$ | Sonda gravitacional |
>
> **Hohmann Tierra→Marte:** $a_t=1.26$ UA, $\Delta v=5.60$ km/s, $224$ días.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$e$ sin normalizar:** en $r=12/(3+4\cos\theta)$, $e=4/3$ (divide entre $3$ primero).
> - **Perihelio en $\theta$ equivocado:** con $+\cos$ es $\theta=0$; con $-\cos$ es $\theta=\pi$.
> - **Directriz del lado contrario:** $+\cos$ usa $x=+d$ (derecha); verifica con el vértice.
> - **Parábola con afelio:** $e=1$ no tiene afelio (escapa al infinito, no regresa).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Identifica $r=12/(3+4\cos\theta)$ ($\ell$, $e$, tipo).
> 2. $r=8/(1+\cos\theta)$ a cartesianas (vértice, foco, directriz).
> 3. Perihelio y afelio de $r=1.5/(1-0.4\cos\theta)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\ell=4$, $e=4/3$ (hipérbola).
>
> **2.** $y^2=-16(x-4)$; $V(4,0)$, $F(0,0)$, $x=8$.
>
> **3.** $r_p=1.071$ ($\theta=\pi$), $r_a=2.5$ ($\theta=0$).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $a,b,T$ del planeta $r=1.5/(1-0.4\cos\theta)$.
> 5. Ecuación orbital con perihelio $2$ UA y afelio $4$ UA.
> 6. Cometa $r=0.8/(1+\cos\theta)$: perihelio y ¿regresa?

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $a=1.786$, $b=1.636$ UA; $T=2.39$ años.
>
> **5.** $a=3$, $e=1/3$, $\ell=8/3$; $r=8/(3+\cos\theta)$.
>
> **6.** $0.4$ UA en $\theta=0$; $e=1\therefore$ no regresa.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Deduce $r=\ell/(1+e\cos\theta)$ desde $PF=e\cdot d(P,\text{directriz})$.
> 8. Hohmann Tierra→Marte: $\Delta v$ y tiempo (verifica $5.60$ km/s, $224$ d).
> 9. $v$ en el perihelio del cometa ($59.3$ km/s con $v=\sqrt{2GM/r}$... verifica).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $r=e(d-r\cos\theta)\therefore r=ed/(1+e\cos\theta)$.
>
> **8.** $v_1=29.78$, $v_p=32.73$, $v_a=21.48$, $v_2=24.13$; $\Delta v_1=2.95$, $\Delta v_2=2.65$.
>
> **9.** $r=5.984\times10^7$ km; $v=\sqrt{2.654\times10^{11}/5.984\times10^7}\approx66.6$ km/s.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Normalizo hasta $1+e\cos\theta$ y leo $\ell,e$.
> - [ ] Clasifico por $e$ y hallo vértices.
> - [ ] Convierto a cartesianas multiplicando por $r$.
> - [ ] Hallo perihelio y afelio.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico Kepler $T^2=a^3$.
> - [ ] Construyo órbitas desde perihelio/afelio.
> - [ ] Distingo escape ($e\ge1$) de retorno.
> - [ ] Verifico directrices con el vértice.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Deduzco la ecuación focal.
> - [ ] Calculo transferencias de Hohmann.
> - [ ] Verifico velocidades orbitales.
> - [ ] Relaciono $e$ con energía orbital.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Cálculo con Geometría Analítica* — cap. de cónicas.
>
> [2] H. Curtis, *Orbital Mechanics for Engineering Students* — Hohmann.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Elipse]] — elipse cartesiana base.
> - [[02 - Coordenadas polares]] — conversión general.
> - [[09 - Espirales en coordenadas polares]] — curvas no cerradas.
> - [[04 - Rectas en coordenadas polares]] — la directriz como recta.

---

**Tags:** #polares #conicas #kepler #orbitas #unidad6

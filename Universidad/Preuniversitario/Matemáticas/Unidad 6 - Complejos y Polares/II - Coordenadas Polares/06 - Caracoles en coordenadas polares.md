---
dg-publish: true
---

# 🌸 Familias Polares

## 🎯 Introducción

> [!info] 💡 ¿Qué familias viven en polares?
>
> **Caracoles** $r=a+b\cos\theta$ ($\lambda=a/b$ decide bucle, cardioide, hoyuelo), **rosas** $r=a\cos n\theta$ ($n$ impar $\to n$ pétalos, par $\to2n$), **lemniscatas** $r^2=a^2\cos2\theta$ (dos bucles $\infty$): la forma de la ecuación predice el dibujo.
>
> ```mermaid
> graph LR
>     A["a+b cos<br/>caracol"] --> B["a cos nt<br/>rosa"]
>     B --> C["r2=a2cos2<br/>lemniscata"]
>     C --> D["Simetría<br/>media tabla"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-galeria.png]]

> [!tip] 💡 Visual — Galería base
>
> Cardioide, rosa 4 pétalos, lemniscata y caracol con bucle: cuatro ecuaciones, cuatro siluetas — lee la forma antes de tabular.

![[U6-caracol.png]]

> [!tip] 💡 Visual — Tres caracoles
>
> $\lambda<1$ bucle, $\lambda=1$ cardioide, $1<\lambda<2$ hoyuelo: la razón $a/b$ esculpe.

![[U6-rosas.png]]

> [!tip] 💡 Visual — 3, 4 y 8 pétalos
>
> $r=4\cos3\theta$, $r=3\cos2\theta$, $r=2\sin4\theta$: la paridad de $n$ cuenta ($n$ par duplica porque $r(\theta+\pi)=-r(\theta)$ recorre los otros sin repetir).

![[U6-lemniscata.png]]

> [!tip] 💡 Visual — Lemniscata y $r=1$
>
> $r^2=4\cos2\theta$ solo existe donde $\cos2\theta\ge0$ (dos intervalos $\therefore$ dos bucles); el círculo la corta en $\pm\pi/6$ para áreas entre curvas.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Las tres familias
>
> **Caracol:** $r=a+b\cos\theta$ (o $\sin$); $\lambda=a/b$: bucle si $<1$ ($r=0$ tiene solución porque $a<b$), cardioide si $=1$ (cúspide: un solo toque al polo), hoyuelo si $1<\lambda<2$, convexo si $\ge2$.
>
> **Rosa:** $r=a\cos n\theta$; longitud $a$ (máximo $|r|$ sin derivar). **Lemniscata:** $r^2=a^2\cos2\theta$ (Bernoulli: $PF_1\cdot PF_2=c^2$, prima-producto de la elipse-suma); extensión $a$, área total $a^2$ ($a^2/2$ por lóbulo, por simetría $\times4$ del cuarto).

> [!tip] 💡 Cómo graficar cada familia
>
> Lee la familia antes de tabular (ya sabes la silueta). Tabula medio período con simetría y marca ceros y máximos — ellos mandan. En lemniscatas respeta el dominio (fuera no hay curva, $r$ sería imaginario); en rosas cuenta máximos de $|\cdot|$, no ceros.

> [!example] 🟢 Ejemplo — $r=2+3\cos\theta$ y $r=5\cos3\theta$
>
> $\lambda=2/3\therefore$ bucle ($r=0$ en $\cos\theta=-2/3$); $r_{\max}=5$, $r_{\min}=-1$. Rosa: 3 pétalos, extremos en $\theta=0,2\pi/3,4\pi/3$ ($(5,0),(-2.5,\pm4.33)$).

---

## 📋 Tabla Comparativa: Familias

> [!note] 📋 Qué ecuación da qué y por qué
>
> | Forma | Tipo (por qué) | Dato |
> |---|---|---|
> | $r=a+b\cos\theta$, $\lambda<1$ | Bucle ($r$ se vuelve negativo) | $r=2+3\cos\theta$ |
> | $\lambda=1$ | Cardioide (un toque al polo) | $A=3\pi a^2/2$ ($6\pi$ si $a=2$) |
> | $\lambda\ge2$ | Convexo (casi óvalo) | $r>0$ siempre |
> | $r=a\cos n\theta$, $n$ impar | $n$ pétalos (repite a $2\pi$) | $r=4\cos3\theta$ ($A=4\pi$) |
> | $n$ par | $2n$ pétalos (mitad opuesta nueva) | $r=2\sin4\theta$ ($8$) |
> | $r^2=a^2\cos2\theta$ | 2 bucles (dominio partido) | $A=a^2$ total |
>
> **Bucle interior:** $r=1+2\cos\theta$ en $[2\pi/3,4\pi/3]$ con $A=\pi-3\sqrt3/2$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\lambda$ invertido ($b/a$):** es $a/b$ ($2+3\cos\theta\to2/3$ bucle).
> - **$2n$ pétalos siempre:** solo $n$ par; impar da $n$.
> - **Lemniscata en todo $\theta$:** $r$ imaginario fuera del dominio.
> - **Área total $=a^2/2$:** eso es un lóbulo; el total es $a^2$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Clasifica $r=2+3\cos\theta$ (extremos y origen).
> 2. Pétalos de $3\cos5\theta$, $2\sin4\theta$.
> 3. Dominio de $r^2=9\cos2\theta$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Bucle; $5$ en $0$, $-1$ en $\pi$; origen $\theta\approx2.30,3.98$.
>
> **2.** $5$; $8$ (longitudes $3,2$).
>
> **3.** $[-\pi/4,\pi/4]\cup[3\pi/4,5\pi/4]$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Área del bucle de $r=1+2\cos\theta$.
> 5. Área de $r=4\cos3\theta$ (total y pétalo).
> 6. Extremos cartesianos de $r=5\cos3\theta$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\pi-3\sqrt3/2$.
>
> **5.** $4\pi$; $4\pi/3$.
>
> **6.** $(5,0),(-2.5,\pm4.33)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $A=3\pi a^2/2$ en $r=a+a\cos\theta$.
> 8. Prueba $n$ par $\to2n$ pétalos.
> 9. Área de $r^2=2\cos2\theta$ fuera de $r=1$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\frac12a^2(2\pi+\pi)$ (promedio de $\cos^2$).
>
> **8.** $r(\theta+\pi)=-r(\theta)$ recorre otros $n$.
>
> **9.** $(\sqrt3-\pi/3)/2$ por lóbulo.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Clasifico caracoles por $\lambda$.
> - [ ] Cuento pétalos por paridad.
> - [ ] Determino dominios de lemniscatas.
> - [ ] Hallo extremos y orígenes.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Integro bucles en su intervalo.
> - [ ] Calculo áreas por pétalo.
> - [ ] Hallo extremos cartesianos.
> - [ ] Verifico simetrías.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro áreas con simetría.
> - [ ] Pruebo conteo de pétalos.
> - [ ] Planteo áreas entre curvas.
> - [ ] Relaciono producto-focos (Bernoulli).

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Cálculo con Geometría Analítica* — cap. de polares.
>
> [2] J. Bernoulli, *Acta Eruditorum* (1694) — lemniscata.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Graficación en coordenadas polares]] — técnicas y media tabla.
> - [[02 - Coordenadas polares]] — áreas con $\frac12\int r^2$.
> - [[09 - Espirales en coordenadas polares]] — siguiente: no cerradas.
> - [[04 - Rectas en coordenadas polares]] — rectas y círculos.

---

**Tags:** #polares #caracol #rosas #lemniscata #unidad6

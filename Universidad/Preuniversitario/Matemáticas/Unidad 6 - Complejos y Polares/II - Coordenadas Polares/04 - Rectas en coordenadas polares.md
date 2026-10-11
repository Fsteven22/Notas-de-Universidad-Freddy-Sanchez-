---
dg-publish: true
---

# 📏 Rectas y Círculos en Polares

## 🎯 Introducción

> [!info] 💡 ¿Cómo son rectas y círculos en polares?
>
> Recta: $r\cos(\theta-\alpha)=d$ (normal $(d,\alpha)$; multiplica el denominador y cae $Ax+By=C$). Círculo por el polo: $r=2a\cos\theta$ (centro $(a,0)$) o $r=2a\sin\theta$ (el coeficiente ya es el diámetro).
>
> ```mermaid
> graph LR
>     A["Normal<br/>(d,a)"] --> B["Recta<br/>r cos=d"]
>     B --> C["Círculo<br/>r=2a cos"]
>     C --> D["Centro<br/>radio=a"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-rectapolar.png]]

> [!tip] 💡 Visual — $x+y=4$
>
> Normal $(2\sqrt2,\pi/4)$ con punto cercano $(2,2)$: la forma normal lo dice sin despejar. Los círculos $r=2a\cos\theta$ son la misma idea (diámetro sobre el eje).

![[U6-circpolar.png]]

> [!tip] 💡 Visual — Círculos por el polo
>
> $r=2,4,6\cos\theta$ (centros $(1,0),(2,0),(3,0)$) y $r=6\sin\theta$ punteada: todos tangentes al polo porque $r=0$ pertenece a cada uno.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Normal y círculos
>
> **Recta:** $r\cos(\theta-\alpha)=d$ (normaliza $(A,B)$ a unitario: el lado derecho es $d$). **Casos:** $\theta=\theta_0$ es rayo (no recta completa); $r\sin\theta=b$ horizontal; $r\cos\theta=a$ vertical.
>
> **Círculo:** $r=2a\cos\theta$ centro $(a,0)$; $r=2a\sin\theta$ centro $(0,a)$; $r=c$ centrado. **General:** $r^2-2r(h\cos\theta+k\sin\theta)+h^2+k^2-R^2=0$ (multiplica por $r$ y completa cuadrados como en cartesianas).

> [!tip] 💡 Cómo identificar sin convertir todo
>
> $r$ dividiendo constante entre senos/cosenos $\to$ multiplica y aparecen $x,y$ solos. En $r=2a\cos\theta$ el coeficiente es el diámetro (centro $(a,0)$, radio $a$). Ojo al dividir entre $r$: el polo $r=0$ también pertenece — no lo pierdas.

> [!example] 🟢 Ejemplo — $r=4/(\cos\theta+\sin\theta)$ y $r=8\cos\theta$
>
> $x+y=4$ (normal $r\cos(\theta-\pi/4)=2\sqrt2$). $8=2a\therefore$ centro $(4,0)$, $R=4$ (verifica $x^2+y^2=8x$ ✓).

---

## 📋 Tabla Comparativa: Rectas y Círculos

> [!note] 📋 Qué ecuación da qué curva y por qué
>
> | Ecuación | Curva (por qué) |
> |---|---|
> | $\theta=\pi/4$ | Rayo $y=x$ (polo fijo, una dirección) |
> | $r\sin\theta=2$ | $y=2$ (el $r$ se cancela al multiplicar) |
> | $r\cos(\theta-\pi/4)=2\sqrt2$ | $x+y=4$ (normal a $45°$) |
> | $r=2a\cos\theta$ | Centro $(a,0)$, $R=a$ (diámetro sobre $x$) |
> | $r=2a\sin\theta$ | Centro $(0,a)$, $R=a$ (diámetro sobre $y$) |
>
> **Distancia punto-recta:** $|r_0\cos(\theta_0-\alpha)-d|$ (proyección menos $d$, en valor absoluto). **Rangos:** $\cos$ en $[-\pi/2,\pi/2]$; $\sin$ en $[0,\pi]$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\theta=\theta_0$ como recta:** es rayo (una dirección desde el polo).
> - **$a$ como radio en $r=2a\cos\theta$:** el radio es $a$ (mitad del coeficiente).
> - **Normal sin normalizar:** $d$ exige coeficientes unitarios.
> - **$r=0$ perdido al dividir:** el polo pertenece a estos círculos.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Identifica $r=4/(\cos\theta+\sin\theta)$.
> 2. Centro y radio de $r=8\cos\theta$.
> 3. Cruces de $r=4\sin\theta$ con el eje polar.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $x+y=4$; normal $r\cos(\theta-\pi/4)=2\sqrt2$.
>
> **2.** $(4,0)$, $R=4$.
>
> **3.** Solo el origen (tangente).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Distancia de $(5,\pi/6)$ a $3r\cos\theta+4r\sin\theta=10$.
> 5. $r=10\cos\theta$ a cartesianas.
> 6. Intersección $r\cos\theta=3$ con $r\sin\theta=2$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $3\sqrt3/2$ (ambos métodos coinciden).
>
> **5.** $(x-5)^2+y^2=25$.
>
> **6.** $(3,2)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Deduce $r\cos(\theta-\alpha)=d$ del producto punto.
> 8. $r=2a\cos\theta$ con $r=2a\sin\theta$: cortes (polo + $(a,a)$).
> 9. Punto de $x+y=4$ más cercano al polo.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(x,y)\cdot(\cos\alpha,\sin\alpha)=d$ y $\cos(A-B)$.
>
> **8.** $\theta=\pi/4$ más el polo ($r=0$ en ambas).
>
> **9.** $(2,2)$ (denominador máximo en $\pi/4$).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Reconozco $\theta=c$, $r\sin\theta=b$, $r\cos\theta=a$.
> - [ ] Leo centro y radio del coeficiente.
> - [ ] Multiplico por el denominador para convertir.
> - [ ] Hallo cruces con los ejes.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Escribo formas normales $(d,\alpha)$.
> - [ ] Calculo distancias por dos métodos.
> - [ ] Completo cuadrados para verificar.
> - [ ] Determino rangos de $\theta$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro la forma normal.
> - [ ] Resuelvo intersecciones (+ polo).
> - [ ] Optimizo $r(\theta)$.
> - [ ] Manejo centros arbitrarios.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Cálculo con Geometría Analítica* — cap. de polares.
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de coordenadas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Puntos y rectas]] — rectas cartesianas base.
> - [[02 - Circunferencia]] — círculos cartesianos.
> - [[01 - Plano polar]] — ubicar puntos.
> - [[10 - Secciones cónicas en coordenadas polares]] — cónicas $r=ed/(1+e\cos\theta)$.

---

**Tags:** #polares #rectas #circulos #unidad6

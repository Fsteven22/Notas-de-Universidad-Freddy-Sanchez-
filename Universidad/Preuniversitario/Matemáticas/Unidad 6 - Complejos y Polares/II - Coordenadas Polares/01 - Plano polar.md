---
dg-publish: true
---

# 🧭 Plano Polar

## 🎯 Introducción

> [!info] 💡 ¿Qué es el plano polar?
>
> Puntos $P(r,\theta)$: $r$ distancia al polo, $\theta$ ángulo desde el eje polar. Conversión $x=r\cos\theta$, $y=r\sin\theta$; $r$ negativo invierte la dirección ($\theta+\pi$).
>
> ```mermaid
> graph LR
>     A["Polo O<br/>eje polar"] --> B["Punto<br/>(r,theta)"]
>     B --> C["Cartesiano<br/>x=rcos y=rsen"]
>     C --> D["Distancia<br/>ley cosenos"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-polar.png]]

> [!tip] 💡 Visual — Cuatro puntos
>
> $P(3,\pi/4)$ va $45°$ antihorario; $R(-4,\pi/6)$ invierte a $7\pi/6$ (tercer cuadrante); $T(5,-\pi/3)$ gira horario — todos caen donde la figura los muestra.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Coordenadas y conversión
>
> **Punto:** $(r,\theta)$ con $r\in\mathbb{R}$, $\theta$ en radianes. **Conversión:** $x=r\cos\theta$, $y=r\sin\theta$; $r^2=x^2+y^2$, $\tan\theta=y/x$ (con cuadrante).
>
> **No unicidad:** $(r,\theta)=(r,\theta+2k\pi)=(-r,\theta+\pi)$; $(0,\theta)=O$ para todo $\theta$.

> [!tip] 💡 Cómo ubicar puntos sin equivocarse
>
> Primero gira el ángulo (negativo = horario), luego avanza $|r|$ — si $r<0$, suma $\pi$ al ángulo y avanza. Para pasar a cartesianas verifica el cuadrante con los signos de $x,y$ antes de aceptar un $\arctan$.

> [!example] 🟢 Ejemplo — $R(-4,\pi/6)$ y conversión
>
> $r<0\therefore R=(4,\pi/6+\pi)=(4,7\pi/6)$ (tercer cuadrante). Cartesianas: $x=4\cos(7\pi/6)=-2\sqrt3$, $y=-2$ (verifica $r^2=12+4=16$ ✓).

---

## 📋 Tabla Comparativa: Representaciones

> [!note] 📋 Cuándo usar cada representación
>
> | Representación | Punto | Uso |
> |---|---|---|
> | **Positiva** | $(3,\pi/4)$ | Directa, $r>0$ |
> | **Negativa** | $(-4,\pi/6)=(4,7\pi/6)$ | $r<0$ invierte |
> | **Ángulo $>2\pi$** | $(2,5\pi/3)=(2,-\pi/3)$ | Reduce módulo $2\pi$ |
> | **Polo** | $(0,\theta)=O$ | $\theta$ irrelevante |
>
> **Distancia polar:** $d^2=r_1^2+r_2^2-2r_1r_2\cos(\theta_2-\theta_1)$ (ley de cosenos).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$r<0$ sin invertir:** $(-4,\pi/6)$ no está a $30°$ sino en el tercer cuadrante.
> - **$\theta=\arctan(y/x)$ sin cuadrante:** $(-1,-1)$ da $\pi/4$ pero es $5\pi/4$.
> - **Unicidad asumida:** el mismo punto tiene infinitas ternas $(r,\theta+2k\pi)$.
> - **Grados y radianes mezclados:** $5\pi/3\neq5/3°$; convierte antes de operar.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Ubica $(3,\pi/4)$, $(2,5\pi/3)$, $(-4,\pi/6)$, $(0,\pi/2)$.
> 2. Representaciones de $(5,-\pi/3)$ con $r>0$ y ángulo positivo.
> 3. Cartesianas de $(4,7\pi/6)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** I cuadrante; IV; III (invierte); polo.
>
> **2.** $(5,5\pi/3)$; también $(-5,2\pi/3)$.
>
> **3.** $(-2\sqrt3,-2)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Polares de $(-1,-1)$ (todas las formas).
> 5. Distancia entre $(3,\pi/4)$ y $(2,5\pi/3)$.
> 6. Describe $r=3$ y $\theta=\pi/4$ como curvas.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(\sqrt2,5\pi/4)$; $+2k\pi$; $(-\sqrt2,\pi/4)$.
>
> **5.** $\Delta\theta=17\pi/12$, $\cos=-0.2588$; $d^2=13+3.106$; $d\approx4.01$.
>
> **6.** Círculo radio $3$; rayo a $45°$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $(r,\theta)=(-r,\theta+\pi)$ geométricamente.
> 8. Región $1\le r\le2$, $0\le\theta\le\pi/2$: área ($\pi\cdot3/4$... halla).
> 9. Simetría: criterios $r(\theta)=r(-\theta)$ (eje polar), $r(\pi-\theta)$ (eje $\pi/2$), $r(\theta+\pi)$ (polo).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Media vuelta + distancia $|r|$ llegan al mismo punto.
>
> **8.** $(1/2)(4-1)(\pi/2)=3\pi/4$.
>
> **9.** Sustituye y compara ecuaciones (suficientes, no necesarias).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Ubico puntos con $r$ positivo, negativo y cero.
> - [ ] Reduzco ángulos módulo $2\pi$.
> - [ ] Convierto polar-cartesiano en ambos sentidos.
> - [ ] Reconozco representaciones del mismo punto.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Ajusto cuadrantes en $\arctan$.
> - [ ] Aplico ley de cosenos para distancias.
> - [ ] Describo $r=c$, $\theta=c$ como curvas.
> - [ ] Trabajo regiones con desigualdades.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro equivalencias de representación.
> - [ ] Calculo áreas de sectores anulares.
> - [ ] Aplico criterios de simetría.
> - [ ] Verifico conversiones con $r^2=x^2+y^2$.

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
> - [[02 - Coordenadas polares]] — conversiones a fondo.
> - [[03 - Graficación en coordenadas polares]] — trazado de curvas.
> - [[01 - Definición y representación geométrica]] — Argand vs polar.
> - [[01 - Ángulos y sus medidas]] — radianes y sentido de giro.

---

**Tags:** #polares #plano-polar #conversion #unidad6

---
dg-publish: true
---

# 🌀 Espirales Polares

## 🎯 Introducción

> [!info] 💡 ¿Qué espirales hay en polares?
>
> **Arquímedes** $r=a\theta$ (brazos equidistantes), **logarítmica** $r=ae^{b\theta}$ (ángulo radio-tangente constante, autosimilar), **hiperbólica** $r=a/\theta$ (asíntota), **Fermat** $r^2=a^2\theta$.
>
> ```mermaid
> graph LR
>     A["r=a t<br/>Arquímedes"] --> B["r=ae bt<br/>logarítmica"]
>     B --> C["r=a/t<br/>hiperbólica"]
>     C --> D["r2=a2 t<br/>Fermat"]
>     style A fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-espirales.png]]

> [!tip] 💡 Visual — Tres espirales
>
> Arquímedes crece parejo (mismo espacio entre vueltas), la logarítmica se abre cada vez más (misma forma a toda escala) y la hiperbólica se pega a una asíntota sin tocarla.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Ecuaciones y propiedades
>
> **Arquímedes:** $r=a\theta$ (separación $2\pi a$ entre vueltas). **Logarítmica:** $r=ae^{b\theta}$ con $\tan\phi=1/b$ (ángulo constante) y autosimilaridad $r(\theta+2\pi)=r(\theta)e^{2\pi b}$.
>
> **Hiperbólica:** $r=a/\theta$ (asíntota $y=a$). **Fermat:** $r^2=a^2\theta$ (dos brazos opuestos).

> [!tip] 💡 Cómo distinguirlas de un vistazo
>
> Vueltas paralelas equidistantes → Arquímedes. Cada vuelta proporcionalmente igual (conchas, galaxias) → logarítmica: verifica $\tan\phi=r/(dr/d\theta)$ constante. Se aplana hacia una recta → hiperbólica. Dos brazos simétricos desde el polo → Fermat.

> [!example] 🟢 Ejemplo — $r=2\theta$ con $r=4$ y $r=e^{\theta/2}$
>
> $2\theta=4\therefore\theta=2$ (primera); infinitas en $\theta=2+2\pi n$ (una por vuelta). $r=e^{\theta/2}$: vuelta completa escala $e^{\pi}\approx23.14$ (misma forma, autosimilar ✓).

---

## 📋 Tabla Comparativa: Espirales

> [!note] 📋 Qué ecuación da qué espiral
>
> | Espiral | Ecuación | Clave | Ejemplo |
> |---|---|---|---|
> | **Arquímedes** | $r=a\theta$ | Brazos a $2\pi a$ | $r=2\theta$ |
> | **Logarítmica** | $r=ae^{b\theta}$ | $\phi$ constante | $r=2e^{\theta/\sqrt3}$ ($\phi=60°$) |
> | **Hiperbólica** | $r=a/\theta$ | Asíntota | $r=2/\theta$ |
> | **Fermat** | $r^2=a^2\theta$ | Dos brazos | $r=\theta^{1/2}$ |
>
> **Área entre $r=\theta$ y $r=2\theta$** ($[0,2\pi]$): $\frac12\int_0^{2\pi}3\theta^2=4\pi^3$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Una sola intersección espiral-círculo:** hay una por vuelta ($\theta=2+2\pi n$).
> - **$\phi$ variable en logarítmica:** $\tan\phi=1/b$ es constante en toda la curva.
> - **Hiperbólica hasta $\theta=0$:** $r\to\infty$ (asíntota, no polo).
> - **Fermat de un brazo:** $r^2$ da $\pm r$ (dos brazos opuestos).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Cortes de $r=2\theta$ con $r=4$ (tres primeros).
> 2. Primer punto en cartesianas ($\theta=2$).
> 3. Clasifica $r=3\theta$, $r=e^{\theta}$, $r=5/\theta$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\theta=2$, $2+2\pi$, $2+4\pi$.
>
> **2.** $(4\cos2,4\sin2)\approx(-1.66,3.64)$.
>
> **3.** Arquímedes; logarítmica; hiperbólica.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Área entre $r=\theta$ y $r=2\theta$ en $[0,2\pi]$.
> 5. Factor de escala por vuelta de $r=e^{\theta/2}$.
> 6. $\phi$ de $r=2e^{\theta/\sqrt3}$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $4\pi^3\approx123.37$.
>
> **5.** $e^{\pi}\approx23.14$.
>
> **6.** $\tan\phi=\sqrt3\therefore\phi=60°$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba autosimilaridad: rotar $\alpha$ + escalar $e^{\alpha b}$ deja $r=ae^{b\theta}$ igual.
> 8. Longitud de $r=2/\theta$ en $[1,\infty)$ (¿converge?... plantea).
> 9. Separación entre vueltas de $r=a\theta$ ($2\pi a$... demuestra).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $ae^{b(\theta+\alpha)}=e^{b\alpha}\cdot ae^{b\theta}$ ∎.
>
> **8.** $s=\int_1^\infty\sqrt{4/\theta^2+4/\theta^4}$ diverge (cola $\sim2/\theta$).
>
> **9.** $r(\theta+2\pi)-r(\theta)=2\pi a$ constante.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico las cuatro espirales por su ecuación.
> - [ ] Hallo cortes con círculos (todas las vueltas).
> - [ ] Convierto puntos a cartesianas.
> - [ ] Reconozco brazos y asíntotas.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo áreas entre espirales.
> - [ ] Hallo factores de escala por vuelta.
> - [ ] Verifico ángulos $\phi$ constantes.
> - [ ] Trabajo intervalos $[0,2\pi]$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro autosimilaridad.
> - [ ] Analizo convergencia de longitudes.
> - [ ] Deduzco separación entre vueltas.
> - [ ] Conecto con crecimiento natural (logarítmica).

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Cálculo con Geometría Analítica* — cap. de polares.
>
> [2] D'Arcy Thompson, *Sobre el crecimiento y la forma* — espirales naturales.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Graficación en coordenadas polares]] — técnicas de trazado.
> - [[02 - Coordenadas polares]] — áreas con $\frac12\int r^2$.
> - [[13 - Funciones exponenciales]] — $e^{b\theta}$ base.
> - [[10 - Secciones cónicas en coordenadas polares]] — siguiente: cónicas $r=ed/(1+e\cos\theta)$.

---

**Tags:** #polares #espirales #logaritmica #arquimedes #unidad6

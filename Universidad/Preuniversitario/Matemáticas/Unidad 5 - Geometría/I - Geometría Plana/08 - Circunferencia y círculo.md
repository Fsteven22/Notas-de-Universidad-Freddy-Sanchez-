---
dg-publish: true
---

# ⭕ Circunferencia y Círculo

## 🎯 Introducción

> [!info] 💡 ¿Qué es una circunferencia?
>
> El conjunto $\{P:d(P,O)=r\}$ (curva) y el **círculo** su interior: $(x-h)^2+(y-k)^2=r^2$. Con arco $s=r\theta$, sector $r^2\theta/2$ y tangentes $PT^2=d^2-r^2$ se mide todo lo circular.
>
> ```mermaid
> graph LR
>     A["Centro<br/>O y radio r"] --> B["Ecuación<br/>(x-h)2+(y-k)2=r2"]
>     B --> C["Arco y sector<br/>s=rθ"]
>     C --> D["Tangentes<br/>PT2=d2-r2"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-tangente.png]]

> [!tip] 💡 Visual — tangente desde $P(10,0)$
>
> Círculo $r=5$: el triángulo $OPT$ es recto en $T$, así que $PT=\sqrt{100-25}=5\sqrt3$ por Pitágoras.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Ecuación, elementos y posiciones
>
> **Canónica:** $(x-h)^2+(y-k)^2=r^2$ (centro $(h,k)$); **general:** $x^2+y^2+Dx+Ey+F=0$ con centro $(-D/2,-E/2)$ y $r=\sqrt{D^2/4+E^2/4-F}$.
>
> **Elementos:** radio, diámetro $=2r$, cuerda, arco, sector, tangente ($\perp$ al radio en el contacto), secante.
>
> **Posiciones recta-círculo:** $d>r$ exterior (0 cortes), $d=r$ tangente (1), $d<r$ secante (2); sustituye $y=mx+b$ y mira el discriminante.

> [!tip] 💡 Cómo pasar de general a canónica sin perderse
>
> Agrupa $x$ con $x$ e $y$ con $y$, completa cuadrados sumando lo mismo a ambos lados: $x^2+6x\to(x+3)^2-9$. El centro sale con signos cambiados $(-D/2,-E/2)$ y el radio es la raíz del número final — si sale negativo, no hay círculo real.

> [!example] 🟢 Ejemplo — Centro y radio de $x^2+y^2+6x-8y+9=0$
>
> $(x^2+6x+9)+(y^2-8y+16)=-9+9+16\therefore(x+3)^2+(y-4)^2=16$. Centro $(-3,4)$, $r=4$.

---

## 📋 Tabla Comparativa: Medidas Circulares

> [!note] 📋 Qué fórmula usar y cuándo
>
> | Medida | Fórmula | Uso |
> |---|---|---|
> | **Longitud** | $C=2\pi r$ | Perímetro completo |
> | **Arco** ($\theta$ rad) | $s=r\theta$ | Fracción de vuelta |
> | **Área círculo** | $\pi r^2$ | Interior completo |
> | **Área sector** | $r^2\theta/2$ | Fracción de área |
> | **Tangente** desde $d$ | $PT=\sqrt{d^2-r^2}$ | Pitágoras $OPT$ recto en $T$ |
> | **Intersección** recta | sustituye y discriminante | $0,1,2$ cortes |
>
> **Ángulos:** central $=\theta$; inscrito $=\theta/2$ (mismo arco); en semicírculo $=90°$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Radio con signo cambiado:** en $(x+3)^2$ el centro es $h=-3$, no $+3$.
> - **Arco con grados sin convertir:** $s=r\theta$ exige $\theta$ en **radianes** ($120°=2\pi/3$).
> - **Tangente sin Pitágoras:** $PT\neq d-r$; es $\sqrt{d^2-r^2}$ (triángulo recto).
> - **Circunferencia vs círculo:** curva ($2\pi r$) vs interior ($\pi r^2$).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Ecuación centro $(2,-3)$, $r=5$ (canónica y general).
> 2. Arco $r=6$, $\theta=120°$.
> 3. Sector $r=8$, $45°$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(x-2)^2+(y+3)^2=25$; $x^2+y^2-4x+6y-12=0$.
>
> **2.** $s=6\cdot2\pi/3=4\pi$.
>
> **3.** $A=\frac12\cdot64\cdot\pi/4=8\pi$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Centro y radio de $x^2+y^2+6x-8y+9=0$.
> 5. Tangente desde $(10,0)$ a $x^2+y^2=25$.
> 6. Intersección $x^2+y^2=13$ con $y=2x+1$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(-3,4)$, $r=4$.
>
> **5.** $\sqrt{100-25}=5\sqrt3$.
>
> **6.** $5x^2+4x-12=0\therefore x=1.2,-2$; puntos $(1.2,3.4),(-2,-3)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba que el inscrito en semicírculo es $90°$ (isósceles con centro).
> 8. Potencia de $(10,0)$ respecto a $x^2+y^2=25$ ($100-25=75=PT^2$).
> 9. Círculo por $(0,0),(4,0),(0,2)$ (sistema: $D=-4,E=-2$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Dos isósceles con $O$; suma $2\alpha+2\beta=180°$.
>
> **8.** $75$ (positiva: exterior).
>
> **9.** $x^2+y^2-4x-2y=0$; centro $(2,1)$, $r=\sqrt5$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo canónica desde centro y radio.
> - [ ] Calculo arcos y sectores convirtiendo a radianes.
> - [ ] Distingo circunferencia (curva) de círculo (interior).
> - [ ] Identifico centro y radio a simple vista.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Completo cuadrados para hallar centro y radio.
> - [ ] Hallo tangentes con $PT^2=d^2-r^2$.
> - [ ] Resuelvo intersecciones recta-círculo con discriminante.
> - [ ] Aplico inscrito $=$ mitad del central.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro inscrito en semicírculo y potencia de un punto.
> - [ ] Hallo círculos por tres puntos con sistemas.
> - [ ] Relaciono posición relativa con discriminante.
> - [ ] Verifico cuadriláteros cíclicos con arcos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de circunferencia.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 2 (cónicas).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Figuras geométricas en el plano]] — círculo como figura base.
> - [[03 - Ángulos]] — central, inscrito y cuadriláteros cíclicos.
> - [[02 - Circunferencia]] — siguiente: forma analítica completa.
> - [[10 - Funciones en Conjuntos]] — $x^2+y^2=1$ no es función.

---

**Tags:** #circunferencia #circulo #tangente #geometria #unidad5

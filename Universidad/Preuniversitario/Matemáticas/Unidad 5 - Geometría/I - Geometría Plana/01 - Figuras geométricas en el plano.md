---
dg-publish: true
---

# 📐 Figuras Geométricas en el Plano

## 🎯 Introducción

> [!info] 💡 ¿Qué es una figura plana?
>
> Un conjunto de puntos del plano $\mathbb{R}^2$ con forma definida: **rectas** (1D), **polígonos** (cadenas cerradas de segmentos) y **curvas** (círculos, cónicas). Cada una se describe por vértices o ecuación, y se mide con perímetro y área.
>
> ```mermaid
> graph LR
>     A["Puntos<br/>(x,y)"] --> B["Rectas<br/>Ax+By=C"]
>     B --> C["Polígonos<br/>vértices"]
>     C --> D["Curvas<br/>círculo/cónicas"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-figuras.png]]

> [!tip] 💡 Visual — tres familias
>
> Triángulo (3 vértices), cuadrado (lados iguales) y círculo (centro + radio $r$). Toda figura plana se reduce a puntos, segmentos o curvas.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Plano, distancia y figuras base
>
> El plano es $\mathbb{R}^2$ con distancia $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$. **Recta** por dos puntos: $Ax+By+C=0$; **círculo** centro $(h,k)$ radio $r$: $(x-h)^2+(y-k)^2=r^2$; **polígono**: cadena cerrada de $n$ segmentos (vértices $V_1,\dots,V_n$).
>
> **Lugar geométrico:** conjunto definido por una condición (ej. mediatriz = equidistantes de dos puntos).

> [!tip] 💡 Cómo leer una figura sin perderse
>
> Primero ubica sus **puntos clave** (vértices, centro, intersecciones); luego sus **lados o curvas** (segmentos, arcos); al final aplica la fórmula de medida. Casi todo problema de figuras se resuelve en ese orden: puntos → lados → área/perímetro.

> [!example] 🟢 Ejemplo — Recta por $A=(2,3)$, $B=(5,-1)$
>
> Pendiente $m=(-1-3)/(5-2)=-4/3$; punto-pendiente: $y-3=(-4/3)(x-2)\therefore4x+3y-17=0$. Verificación en $B$: $20-3-17=0$ ✓

---

## 📋 Tabla Comparativa: Áreas y Perímetros

> [!note] 📋 Qué mide cada fórmula y cuándo usarla
>
> | Figura | Área | Perímetro | Uso típico |
> |---|---|---|---|
> | **Triángulo** | $bh/2$; Herón $\sqrt{s(s-a)(s-b)(s-c)}$ | $a+b+c$ | Base general |
> | **Cuadrado/Rectángulo** | $l^2$ / $bh$ | $4l$ / $2(b+h)$ | Lados conocidos |
> | **Paralelogramo** | $b\cdot h$ ($h$ altura, no lado) | $2(a+b)$ | Altura dada |
> | **Trapecio** | $(B+b)h/2$ | suma lados | Dos bases paralelas |
> | **Círculo** | $\pi r^2$ | $2\pi r$ | Radio conocido |
> | **Sector** ($\theta$ rad) | $r^2\theta/2$ | $r\theta+2r$ | Ángulo central |
> | **Elipse** | $\pi ab$ | aproximado | Semiejes |
> | **Polígono** $(x_i,y_i)$ | $\frac12\|\sum(x_iy_{i+1}-x_{i+1}y_i)\|$ | suma lados | Vértices (shoelace) |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Usar el lado inclinado como altura:** en paralelogramo y trapecio la altura es **perpendicular** a la base, no el lado oblicuo.
> - **Confundir radio con diámetro:** $A=\pi r^2$ usa $r$; si dan $d$, primero $r=d/2$.
> - **Olvidar unidades cuadradas** en áreas (y lineales en perímetros).
> - **Herón con $s$ mal calculado:** $s=(a+b+c)/2$ es el **semi**perímetro, no el perímetro.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Halla la ecuación de la recta por $(2,3)$ y $(5,-1)$.
> 2. Área y perímetro de un rectángulo $3\times4$.
> 3. Área de un círculo $r=2$ y longitud de su circunferencia.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $m=-4/3$; $4x+3y-17=0$.
>
> **2.** $A=12$, $P=14$.
>
> **3.** $A=4\pi$, $C=4\pi$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Halla el círculo por $(0,0),(4,0),(0,2)$ (centro y radio).
> 5. Área del triángulo $(1,2),(4,6),(7,3)$ con determinante.
> 6. Distancia de $(2,3)$ a $3x-4y+1=0$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $x^2+y^2-4x-2y=0$; centro $(2,1)$, $r=\sqrt5$.
>
> **5.** $\frac12|1(6-3)+4(3-2)+7(2-6)|=21/2$.
>
> **6.** $|6-12+1|/5=1$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba la fórmula de Herón desde $A=bh/2$ con $h^2=a^2-(\frac{a^2+c^2-b^2}{2a})^2$.
> 8. Área entre $y=x^2$ y $y=2x+3$ (cortes $-1,3$; integra).
> 9. Lugares: halla la mediatriz de $(0,0),(4,2)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Desarrolla $h$ por Pitágoras y factoriza $(s-a)(s-b)(s-c)s$.
>
> **8.** $\int_{-1}^3(2x+3-x^2)dx=[x^2+3x-x^3/3]_{-1}^3=32/3$.
>
> **9.** Equidistancia: $x^2+y^2=(x-4)^2+(y-2)^2\therefore8x+4y=20\therefore2x+y=5$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo ecuaciones de rectas por dos puntos.
> - [ ] Calculo áreas y perímetros de figuras básicas.
> - [ ] Distingo radio de diámetro en círculos.
> - [ ] Ubico puntos y leo coordenadas sin errores.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo círculos por tres puntos (centro y radio).
> - [ ] Aplico determinante y Herón en triángulos.
> - [ ] Calculo distancias punto-recta.
> - [ ] Uso sectores y arcos con radianes.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro Herón y áreas entre curvas.
> - [ ] Hallo lugares geométricos (mediatriz) algebraicamente.
> - [ ] Aplico shoelace en polígonos generales.
> - [ ] Relaciono figuras con sus ecuaciones analíticas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 1–2 (plano y figuras).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de áreas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Clases de rectas en el plano]] — posiciones relativas de rectas.
> - [[07 - Perímetro y área de un polígono]] — fórmulas y shoelace.
> - [[08 - Circunferencia y círculo]] — círculo y sus elementos.
> - [[01 - Puntos y rectas]] — geometría analítica del plano.

---

**Tags:** #geometria-plana #figuras #areas #unidad5

---
dg-publish: true
---

# 📏 Perímetro y Área de un Polígono

## 🎯 Introducción

> [!info] 💡 ¿Cómo se miden los polígonos?
>
> El **perímetro** suma lados ($P=\sum L_i$) y el **área** cuenta superficie: fórmulas directas en regulares ($P=na$, $A=P\cdot ap/2$), **shoelace** con vértices y **Pick** en retículas ($A=I+B/2-1$).
>
> ```mermaid
> graph LR
>     A["Polígono"] --> B{"Datos?"}
>     B -->|Regular| C["P=na<br/>A=P·ap/2"]
>     B -->|Vértices| D["Shoelace"]
>     B -->|Retícula| E["Pick"]
>     style C fill:#e1ffe1
>     style E fill:#e1f5ff
> ```

![[U5-pick.png]]

> [!tip] 💡 Visual — shoelace en acción
>
> Cuadrilátero $(1,1),(4,2),(5,5),(2,4)$: la fórmula da $A=8$ sin descomponer en triángulos.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Perímetro, área y apotema
>
> **Perímetro:** $P=L_1+\dots+L_n$ (suma de lados; en regular $P=na$).
>
> **Área:** medida de superficie. **Apotema** $ap$: distancia del centro al punto medio de un lado (solo regulares); $A=\frac12P\cdot ap$.
>
> **Shoelace** (vértices ordenados): $A=\frac12|\sum(x_iy_{i+1}-x_{i+1}y_i)|$ (cíclico). **Pick** (retícula): $A=I+B/2-1$ con $I$ interiores y $B$ en borde.

> [!tip] 💡 Cómo elegir el método sin dudar
>
> ¿Es regular con lado/apotema? Usa $P=na$, $A=P\cdot ap/2$. ¿Tienes vértices? Shoelace (ordénalos en sentido horario o antihorario, sin saltar). ¿Está sobre cuadrícula con vértices enteros? Pick contando puntos. ¿Ninguno? Descompón en triángulos/rectángulos conocidos.

> [!example] 🟢 Ejemplo — Trapecio $(0,0),(6,0),(5,4),(1,4)$ por dos vías
>
> Shoelace: $A=\frac12|0+24+20-4|=\frac12|40|=20$. Verificación (trapecio): bases $6,4$, altura $4$: $A=((6+4)/2)\cdot4=20$ ✓

---

## 📋 Tabla Comparativa: Regulares

> [!note] 📋 Qué fórmula usar y cuándo
>
> | Polígono | Perímetro | Área | Clave |
> |---|---|---|---|
> | **Triángulo** | $a+b+c$ | $bh/2$, Herón, $\frac12ab\sin\gamma$ | Según datos |
> | **Cuadrado** $a$ | $4a$ | $a^2$ | Lado directo |
> | **Hexágono** $a$ | $6a$ | $3a^2\sqrt3/2$ | $6$ equiláteros |
> | **Regular $n$** | $na$ | $\frac12P\cdot ap$, $ap=a/(2\tan(\pi/n))$ | Apotema primero |
> | **Cualquiera** $(x_i,y_i)$ | suma distancias | Shoelace | Orden cíclico |
> | **Retícula** | — | $I+B/2-1$ (Pick) | Contar puntos |
>
> **Hexágono inscrito** ($R$): lado $=R$; $A=3R^2\sqrt3/2$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Shoelace con vértices desordenados:** deben ir en orden cíclico (horario o antihorario); saltar cruza la suma y da cualquier cosa.
> - **Olvidar cerrar el ciclo:** el último término usa $(x_1,y_1)$ de nuevo.
> - **Apotema = radio:** $ap$ va al **punto medio del lado**, $R$ al **vértice** ($ap=R\cos(\pi/n)$).
> - **Pick fuera de retícula:** exige vértices enteros; si no, no aplica.
> - **Perímetro con diagonales:** $P$ suma **lados**, nunca diagonales.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Perímetro del pentágono $(0,0),(4,0),(5,3),(2,5),(-1,3)$.
> 2. Área del hexágono regular $R=6$ (lado y $A=54\sqrt3$).
> 3. Pick con $I=12,B=8$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $4+\sqrt{10}+\sqrt{13}+\sqrt{13}+\sqrt{10}\approx17.54$.
>
> **2.** Lado $=6$; $P=36$; $A=54\sqrt3\approx93.53$.
>
> **3.** $12+4-1=15$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Shoelace del trapecio $(0,0),(6,0),(5,4),(1,4)$ y verificación.
> 5. Decágono $a=5$: $P$, apotema y área.
> 6. Área $(1,1),(4,2),(5,5),(2,4)$ con shoelace.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $20$ (ver ejemplo).
>
> **5.** $P=50$; $ap=5/(2\tan18°)\approx7.69$; $A\approx192.25$.
>
> **6.** $\frac12|-2+16+10-8|=8$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba Pick en un rectángulo $m\times n$ y extiéndelo por aditividad.
> 8. Área máxima con perímetro fijo: el regular gana (isoperimétrica discreta).
> 9. $A$ del polígono $(0,0),(3,1),(5,4),(2,6),(-1,3)$ con shoelace.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $I=(m-1)(n-1)$, $B=2m+2n$: $A=mn$ ✓; todo polígono reticular se parte en triángulos base.
>
> **8.** A igual $P$, más lados $\to$ más área; límite: círculo.
>
> **9.** $\sum x_iy_{i+1}=0+12+30+6+0=48$; $\sum y_ix_{i+1}=0+5+8-6+0=7$; $A=|48-7|/2=20.5$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Sumo lados para $P$ y uso $P=na$ en regulares.
> - [ ] Aplico Pick contando $I$ y $B$.
> - [ ] Calculo áreas de hexágonos con $R$.
> - [ ] Distingo lado, apotema y radio.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico shoelace con vértices ordenados y cíclicos.
> - [ ] Hallo apotemas con $\tan(\pi/n)$.
> - [ ] Verifico áreas por dos vías (fórmula + descomposición).
> - [ ] Uso diagonales solo donde corresponde.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro Pick por aditividad desde rectángulos.
> - [ ] Pruebo optimalidad del regular a perímetro fijo.
> - [ ] Manejo polígonos de $n$ grande con shoelace.
> - [ ] Relaciono $ap=R\cos(\pi/n)$ geométricamente.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de áreas.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 1 (polígonos).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Poligonales y polígonos]] — diagonales y triangulación.
> - [[01 - Figuras geométricas en el plano]] — fórmulas base por figura.
> - [[06 - Cuadriláteros]] — trapecios y Brahmagupta.
> - [[04 - Determinantes]] — shoelace como determinante.

---

**Tags:** #perimetro #area #poligonos #shoelace #geometria #unidad5

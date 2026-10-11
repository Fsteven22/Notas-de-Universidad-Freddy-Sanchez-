---
dg-publish: true
---

# 📐 Triángulos

## 🎯 Introducción

> [!info] 💡 ¿Qué hace especial al triángulo?
>
> Tres lados determinan forma rígida (a diferencia de cuadriláteros) y todo polígono se triangula. Sus leyes —Pitágoras, senos, cosenos— resuelven lados y ángulos, y sus puntos notables (baricentro, incentro, circuncentro) concentran la geometría del triángulo.
>
> ```mermaid
> graph LR
>     A["3 lados<br/>rígido"] --> B["Leyes<br/>Pit/sen/cos"]
>     B --> C["Resolver<br/>lados y ángulos"]
>     C --> D["Notables<br/>G/I/O"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-triangulo.png]]

> [!tip] 💡 Visual — elementos básicos
>
> Vértices $A,B,C$, lados $a,b,c$ opuestos y altura $h$ punteada: con ellos se enuncian Pitágoras, área $bh/2$ y los puntos notables.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Elementos, existencia y clasificación
>
> **Elementos:** vértices $A,B,C$; lados $a=BC,b=CA,c=AB$; ángulos $\alpha+\beta+\gamma=180°$; altura $h$ (perpendicular a la base); mediana (al punto medio); bisectriz (divide el ángulo); mediatriz (perpendicular en punto medio).
>
> **Existencia (desigualdad triangular):** $a<b+c$, $b<a+c$, $c<a+b$ — cada lado menor que la suma de los otros dos.
>
> **Clasificación:** por lados (equilátero/isósceles/escaleno); por ángulos (acutángulo/rectángulo/obtusángulo).

> [!tip] 💡 Cómo clasificar sin dudar
>
> Primero mira los **ángulos** ($>90°$ → obtusángulo; $=90°$ → rectángulo; si no, acutángulo) y luego los **lados** (¿cuántos iguales?). Para existencia, verifica solo la suma de los **dos menores** contra el mayor — si esa pasa, las otras dos pasan solas.

> [!example] 🟢 Ejemplo — ¿Existe $(2,3,6)$? ¿Y $(3,4,5)$?
>
> $2+3=5<6$ ∴ $(2,3,6)$ imposible. $3+4>5$, $3+5>4$, $4+5>3$ ∴ $(3,4,5)$ existe (rectángulo: $9+16=25$).

---

## 📋 Tabla Comparativa: Leyes Métricas

> [!note] 📋 Qué dice cada ley y cuándo usarla
>
> | Ley | Fórmula | Uso |
> |---|---|---|
> | **Pitágoras** | $a^2+b^2=c^2$ ($\gamma=90°$) | Rectángulos; recíproca clasifica ($>$ acutángulo, $<$ obtusángulo) |
> | **Senos** | $a/\sin\alpha=b/\sin\beta=c/\sin\gamma=2R$ | AAS, ASA; radio circunscrito |
> | **Cosenos** | $a^2=b^2+c^2-2bc\cos\alpha$ | LLL, LAL; ángulo desde lados |
> | **Área** | $bh/2$; Herón; $\frac12ab\sin\gamma$ | Según datos |
> | **Bisectriz** | $BD/DC=c/b$ | Divide proporcional |
> | **Mediana** | $m_a^2=(2b^2+2c^2-a^2)/4$ | Apolonio |
>
> **Ternas primitivas:** $(3,4,5),(5,12,13),(8,15,17)$ — generadas por $m^2-n^2,2mn,m^2+n^2$.

> [!example] 🟢 Ejemplo — LLL con $a=7,b=8,c=9$
>
> $\cos\alpha=(64+81-49)/(2\cdot8\cdot9)=96/144=2/3\therefore\alpha\approx48.2°$. Verifica tipo: $49+64>81$ y análogos ∴ acutángulo.

---

## 📐 Puntos Notables

> [!note] 📋 Definición — Baricentro, incentro, circuncentro, ortocentro
>
> - **Baricentro** $G$: intersección de medianas (centro de masa); divide cada mediana $2$:$1$.
> - **Incentro** $I$: intersección de bisectrices; centro del círculo inscrito (radio $r=A/s$).
> - **Circuncentro** $O$: intersección de mediatrices; centro del circunscrito ($R=abc/4A$).
> - **Ortocentro** $H$: intersección de alturas; en rectángulo es el vértice recto.
> - **Recta de Euler:** $O,G,H$ colineales con $OG:GH=1$:$2$.
>
> **Cómo se usa:** $G$ promedia vértices $((x_1+x_2+x_3)/3)$; $I$ equidista de los lados; $O$ equidista de vértices.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Pitágoras sin ángulo recto:** $a^2+b^2=c^2$ exige $\gamma=90°$ — fuera de ahí usa cosenos.
> - **Ley de senos ambigua (SSA):** $\sin\theta=a$ da dos ángulos ($\theta$ y $180°-\theta$) — verifica cuál encaja.
> - **Altura = lado oblicuo:** la altura es perpendicular a la base, no el lado inclinado.
> - **Incentro = baricentro:** coinciden solo en el equilátero; en general son puntos distintos.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. ¿Existe $(2,3,6)$? ¿Y $(3,4,5)$? Clasifica el segundo.
> 2. Hipotenusa con catetos $6,8$; cateto con hipotenusa $13$ y cateto $5$.
> 3. Área de base $10$ altura $6$ y con Herón de $(5,5,6)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** No ($2+3<6$); sí, rectángulo ($9+16=25$).
>
> **2.** $10$; $12$ ($169-25=144$).
>
> **3.** $30$; $s=8$, $A=\sqrt{8\cdot3\cdot3\cdot2}=12$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Resuelve con senos: $A=30°$, $B=60°$, $a=5$ (halla $b,c$).
> 5. Con cosenos: $b=8,c=9$ incluidos $60°$... halla $a$ con $a^2=64+81-2\cdot8\cdot9\cos60°$.
> 6. Baricentro de $(0,0),(6,0),(0,9)$ e incentro del $(3,4,5)$ rectángulo.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $C=90°$; $b=5\sin60°/\sin30°=5\sqrt3$; $c=5/\sin30°=10$.
>
> **5.** $a^2=145-72=73\therefore a=\sqrt{73}$.
>
> **6.** $G=(2,3)$; $r=(3+4-5)/2=1$, $I=(1,1)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba la ley de cosenos trazando la altura ($c^2=a^2+b^2-2ab\cos\gamma$... plantea con $h$).
> 8. Prueba Euler $OI^2=R(R-2r)$ para el $(3,4,5)$ ($R=2.5,r=1$: $6.25-5=1.25=OI^2$).
> 9. Mediana $m_a$ con $b=5,c=6,a=7$ y verifica Apolonio.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $h=b\sin\gamma$, proyección $b\cos\gamma$; Pitágoras en el triángulo restante.
>
> **8.** $OI=\sqrt{1.25}\approx1.12$.
>
> **9.** $m_a^2=(50+72-49)/4=73/4$; Apolonio $25+36=2(73/4+49/4)=61$ ✓.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico existencia con desigualdad triangular.
> - [ ] Aplico Pitágoras y área $bh/2$.
> - [ ] Clasifico por lados y ángulos.
> - [ ] Hallo hipotenusa y catetos directos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo AAS/ASA con senos y LLL/LAL con cosenos.
> - [ ] Uso Herón y $\frac12ab\sin\gamma$ según datos.
> - [ ] Hallo baricentro, incentro y circuncentro básicos.
> - [ ] Manejo la ambigüedad SSA con los dos ángulos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro cosenos, Euler $OI$ y Apolonio.
> - [ ] Trabajo bisectriz ($BD/DC$) y mediana ($m_a$).
> - [ ] Genero ternas pitagóricas con $m,n$.
> - [ ] Relaciono $R=abc/4A$ y $r=A/s$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de triángulos.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 2 (leyes y puntos notables).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Poligonales y polígonos]] — triangulación y suma $(n-2)180°$.
> - [[03 - Ángulos]] — suma $180°$ y clasificación por ángulos.
> - [[02 - Funciones trigonométricas elementales]] — $\sin,\cos$ usados en las leyes.
> - [[07 - Perímetro y área de un polígono]] — Herón y áreas.

---

**Tags:** #triangulos #pitagoras #ley-senos #geometria #unidad5

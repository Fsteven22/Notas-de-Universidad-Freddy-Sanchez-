---
dg-publish: true
---

# 📐 Poligonales y Polígonos

## 🎯 Introducción

> [!info] 💡 ¿Qué es un polígono?
>
> Una cadena cerrada de $n$ segmentos (lados) con $n$ vértices. Se clasifica por lados (triángulo, cuadrilátero...), por regularidad y por convexidad; sus leyes (suma $(n-2)180°$, diagonales $n(n-3)/2$) se prueban triangulando desde un vértice.
>
> ```mermaid
> graph LR
>     A["n segmentos<br/>cerrados"] --> B["Polígono<br/>n vértices"]
>     B --> C["Triangula<br/>n-2 triángulos"]
>     C --> D["Leyes<br/>ángulos/diagonales"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-poligono.png]]

> [!tip] 💡 Visual — triangulación
>
> Desde $V_0$ salen $n-3$ diagonales que parten el hexágono en $n-2=4$ triángulos: por eso la suma interior es $4\cdot180°=720°$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Poligonal, polígono y elementos
>
> **Poligonal:** cadena de segmentos $V_1V_2,\dots,V_{n-1}V_n$; **cerrada** si $V_n=V_1$. **Polígono:** poligonal cerrada simple (sin autointersecciones) con $n\ge3$.
>
> **Elementos:** vértices $V_i$, lados, ángulos interiores $\alpha_i$, diagonales (unen no adyacentes), perímetro $P=\sum L_i$. **Convexo** si todo segmento entre dos puntos queda dentro; **regular** si lados y ángulos iguales.

> [!tip] 💡 Cómo no confundir los conteos
>
> Tres números distintos con tres orígenes: $n-3$ diagonales **desde un vértice** (excluye a sí mismo y a sus 2 vecinos), $n(n-3)/2$ diagonales **totales** (cada una se contó 2 veces, una por extremo) y $n-2$ **triángulos** en la triangulación. Si un resultado no es entero o contradice estos, revisa cuál de los tres pedían.

> [!example] 🟢 Ejemplo — Pentágono: $5$ diagonales y $540°$
>
> Desde cada vértice salen $5-3=2$; total $5\cdot2/2=5$ diagonales. Triangulación en $3$ triángulos: suma $3\cdot180°=540°=(5-2)180°$ ✓

---

## 📋 Tabla Comparativa: Fórmulas por $n$

> [!note] 📋 Qué vale cada cantidad y cuándo usarla
>
> | Cantidad | Fórmula | Uso |
> |---|---|---|
> | **Suma interiores** | $(n-2)180°$ | Triángulos $180°$, cuadriláteros $360°$ |
> | **Suma exteriores** | $360°$ (convexo, siempre) | Verificación |
> | **Interior regular** | $180°-360°/n$ | $n=9,\alpha=140°\therefore$ eneágono |
> | **Diagonales totales** | $n(n-3)/2$ | Decágono: $35$ |
> | **Área (coordenadas)** | $\frac12\|\sum(x_iy_{i+1}-x_{i+1}y_i)\|$ | Vértices (shoelace) |
> | **Perímetro regular** | $n\cdot a$ | Lado $a$ repetido |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Contar $n(n-3)$ diagonales sin dividir por 2:** cada diagonal une 2 vértices y se cuenta dos veces.
> - **Usar $(n-2)180°$ en no convexos sin cuidado:** la fórmula vale para simples (con prueba por orejas); verifica convexidad primero.
> - **Confundir interior con exterior:** $\alpha_{int}+\alpha_{ext}=180°$ por vértice; la suma de exteriores es $360°$ total, no por vértice.
> - **Llamar regular a todo polígono de lados iguales:** el rombo tiene lados iguales pero ángulos distintos — regular exige **ambos**.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Suma interior de pentágono y octágono.
> 2. Diagonales de hexágono y decágono.
> 3. Interior regular de nonágono ($140°$): verifica con $180-360/n$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $540°$; $1080°$.
>
> **2.** $9$; $35$.
>
> **3.** $180-40=140°$ ✓ ($n=9$).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Polígono regular con interior $140°$: lados y diagonales.
> 5. Área con shoelace: $(0,0),(4,0),(4,3)$.
> 6. Prueba $S_{ext}=360°$ girando una vuelta completa.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $n=9$; $D=27$.
>
> **5.** $\frac12|0+12+0-0-0-0|=6$.
>
> **6.** Al recorrer el perímetro giras $360°$ en total.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $(n-2)180°$ por triangulación desde un vértice.
> 8. Prueba $n(n-3)/2$ contando por vértice y corrigiendo doble conteo.
> 9. Teselación: ¿qué regulares cubren el plano sin huecos? (triángulo, cuadrado, hexágono: $360°/ \alpha_{int}$ entero).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $n-2$ triángulos disjuntos cubren el polígono; cada uno suma $180°$.
>
> **8.** $n$ vértices $\times(n-3)$ diagonales $/2$ (cada una con 2 extremos).
>
> **9.** $360/60=6$, $360/90=4$, $360/120=3$; pentágono ($108°$) no divide a $360$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Clasifico polígonos por lados y regularidad.
> - [ ] Calculo sumas $(n-2)180°$ y diagonales $n(n-3)/2$.
> - [ ] Distingo convexo de no convexo y regular de equilátero.
> - [ ] Hallo interiores regulares con $180-360/n$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Uso shoelace con vértices ordenados.
> - [ ] Pruebo $S_{ext}=360°$ y la aplico.
> - [ ] Hallo $n$ desde el ángulo interior regular.
> - [ ] Triangulo polígonos desde un vértice.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro suma y diagonales por conteo.
> - [ ] Decido teselaciones con divisibilidad de $360°$.
> - [ ] Relaciono orejas con triangulación general.
> - [ ] Verifico convexidad antes de aplicar fórmulas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de polígonos.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 1 (poligonales).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Ángulos]] — suma $(n-2)180°$ y exteriores $360°$.
> - [[05 - Triángulos]] — caso $n=3$ con Pitágoras y Herón.
> - [[06 - Cuadriláteros]] — caso $n=4$ y sus tipos.
> - [[07 - Perímetro y área de un polígono]] — shoelace y áreas.

---

**Tags:** #poligonos #diagonales #triangulacion #geometria #unidad5

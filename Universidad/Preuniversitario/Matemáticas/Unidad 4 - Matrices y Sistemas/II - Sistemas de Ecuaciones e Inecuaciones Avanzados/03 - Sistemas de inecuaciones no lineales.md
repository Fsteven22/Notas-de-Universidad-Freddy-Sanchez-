---
dg-publish: true
---

# 📐 Sistemas de Inecuaciones No Lineales

## 🎯 Introducción

> [!info] 💡 ¿Qué cambia respecto al caso lineal?
>
> Las fronteras son **curvas** (círculos, parábolas, hipérbolas) en vez de rectas: la solución sigue siendo la intersección de regiones, pero los "vértices" son cortes curva-curva y la región puede ser no conexa (varias piezas). El método es el mismo: frontera + punto de prueba + intersección.
>
> ```mermaid
> graph LR
>     A["Curvas<br/>frontera"] --> B["Lado<br/>punto prueba"]
>     B --> C["Intersección<br/>región curva"]
>     C --> D["Cortes<br/>curva-curva"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U4-nolineal.png]]

> [!tip] 💡 Visual — cuarto de disco
>
> $x^2+y^2\le16$ con $x,y\ge0$: la frontera curva es el arco y los "vértices" son $(4,0)$, $(0,4)$ y $(0,0)$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Sistema, frontera curva y región
>
> Cada inecuación $f(x,y)\le c$ (o $\ge,<,>$) tiene **frontera** $f(x,y)=c$ (curva) y dos lados; el punto de prueba elige. La solución es la intersección de las regiones. Puede ser: vacía, acotada, infinita, **no conexa** (varias piezas separadas) o de medida cero (solo la curva).
>
> **Casos por cónica:** $x^2+y^2\le r^2$ (disco), $2\le\sqrt{x^2+y^2}\le4$ (anillo), $y\le4-x^2$ (bajo parábola), $x^2-y^2\ge4$ (fuera de hipérbola, dos piezas).

> [!tip] 💡 Cómo no perderse con curvas
>
> Dibuja primero **todas** las fronteras como igualdades (círculo, parábola, rectas) y marca sus cortes; recién después sombrea cada desigualdad por separado con punto de prueba. Si una frontera es complicada ($e^x$, hipérbola), ubica 2-3 puntos guía antes de trazarla.

> [!example] 🟢 Ejemplo — Anillo $4\le x^2+y^2\le16$
>
> 1. Fronteras: círculos $r=2$ y $r=4$ (concéntricos).
> 2. Punto $(3,0)$: $9$ cumple $4\le9\le16$ ✓ → la zona entre ambos.
> 3. Región: corona acotada, conexa, área $\pi(16-4)=12\pi$.

---

## 📋 Tabla Comparativa: Regiones No Lineales

> [!note] 📋 Qué forma toma cada combinación
>
> | Sistema | Región | Clave |
> |---|---|---|
> | Disco + cuadrante | Cuarto de disco | Cortes con ejes |
> | Parábolas opuestas | Lente entre curvas | Resolver $4-x^2=x^2-4$ |
> | Hipérbola + disco | Dos piezas (una por rama) | No conexa |
> | Círculo + recta | Segmento circular | Intersección recta-círculo |
> | Racional/exponencial | Según asíntotas | Dominio primero |
>
> **Mixto típico:** $x^2+y^2\le25$, $3x+4y\le20$, $x,y\ge0$: el círculo corta a la recta en $(0,5)$ y $(4.8,1.4)$; vértices $(0,0),(0,5),(4.8,1.4),(5,0)$ más el arco.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Tratar curvas como rectas:** la intersección recta-círculo da $0,1,2$ puntos (no siempre 1) — resuelve la cuadrática completa.
> - **Olvidar piezas:** con hipérbolas o $|x|$, la región puede tener varias componentes; verifica cada rama.
> - **Ignorar el dominio:** $1/(x^2+y^2)\le1$ equivale a $x^2+y^2\ge1$ **más** $(0,0)$ excluido.
> - **Asumir convexidad:** la intersección de discos es convexa, pero con hipérbolas o anillos deja de serlo — el óptimo puede no estar en "vértices".

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Describe $x^2+y^2\le16$ con $x,y\ge0$ (fronteras y vértices).
> 2. Describe $y\le4-x^2$ con $y\ge x^2-4$: halla los cortes.
> 3. ¿Es $(3,0)$ solución de $x^2+y^2\le16$, $x\ge0$?

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Arco $r=4$ más ejes; vértices $(4,0),(0,4),(0,0)$.
>
> **2.** $4-x^2=x^2-4\therefore x=\pm2$; puntos $(2,0),(-2,0)$.
>
> **3.** $9\le16$ ✓ y $3\ge0$ ✓ → sí.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Halla el área del anillo $4\le x^2+y^2\le16$.
> 5. Cuarto de elipse $x^2/9+y^2/4\le1$, $x,y\ge0$: vértices y área.
> 6. Intersección de $x^2+y^2=25$ con $3x+4y=20$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\pi(16-4)=12\pi$.
>
> **5.** $(0,0),(3,0),(0,2)$ más arco; área $3\pi/2$.
>
> **6.** $(0,5)$ y $(4.8,1.4)$ (sustituye $y=(20-3x)/4$).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Analiza $x^2-y^2\ge4$, $x^2+y^2\le16$, $x\ge0$: ¿conexa? Describe piezas.
> 8. Estudia $1/(x^2+y^2)\le1$, $xy\le1$, $x,y>0$ (dominio y cortes).
> 9. Maximiza $x+y$ sobre $x^2+y^2\le1$ (el óptimo está en $(\sqrt2/2,\sqrt2/2)$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** No conexa: rama derecha de la hipérbola dentro del disco (más su reflejo si $x\ge0$ incluye el eje).
>
> **8.** Fuera del disco unitario ($(0,0)$ excluido) bajo $xy=1$; $x^2+1/x^2=1$ sin solución real → no se cortan.
>
> **9.** Rectas $x+y=k$ tangentes al disco: $k_{\max}=\sqrt2$ en $(\sqrt2/2,\sqrt2/2)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Dibujo fronteras curvas (círculos, parábolas) y elijo el lado con punto de prueba.
> - [ ] Hallo cortes curva-curva resolviendo el sistema de igualdades.
> - [ ] Describo regiones con desigualdades encadenadas ($2\le r\le4$).
> - [ ] Distingo región vacía, acotada e infinita en casos curvos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo áreas de anillos y cuartos de elipse.
> - [ ] Resuelvo sistemas mixtos recta-círculo con sustitución.
> - [ ] Detecto no-conexidad en hipérbolas y valores absolutos.
> - [ ] Manejo dominios excluidos en racionales.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Analizo piezas de regiones no conexas una por una.
> - [ ] Optimizo sobre discos con tangencia (isocuantas curvas).
> - [ ] Estudio intersecciones sin solución real (discriminante).
> - [ ] Relaciono convexidad con validez del método de vértices.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precalculus: Mathematics for Calculus*, 7th ed., Cengage, 2015 — §9–10 (cónicas y sistemas).
>
> [2] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de sistemas no lineales.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Sistemas de inecuaciones lineales]] — mismo método (frontera + prueba + intersección) con rectas.
> - [[01 - Sistemas de ecuaciones no lineales]] — cortes como soluciones de igualdades.
> - [[08 - Circunferencia y círculo]] — fronteras circulares y sus ecuaciones.
> - [[11 - Inecuaciones]] — inecuaciones de una variable como caso previo.

---

**Tags:** #sistemas-inecuaciones #no-lineales #conicas #algebra #unidad4

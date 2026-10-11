---
dg-publish: true
---

# 📐 Sistemas de Inecuaciones Lineales

## 🎯 Introducción

> [!info] 💡 ¿Qué es un sistema de inecuaciones lineales?
>
> Un conjunto de desigualdades $ax+by\le c$ que deben cumplirse **a la vez**. Cada una define un **semiplano**; la solución es su **intersección**: la región factible (acotada, infinita, un punto o vacía). Sus vértices son la clave de la optimización lineal.
>
> ```mermaid
> graph LR
>     A["Inecuaciones<br/>ax+by<=c"] --> B["Semiplanos<br/>frontera + lado"]
>     B --> C["Intersección<br/>región factible"]
>     C --> D["Vértices<br/>óptimo"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U4-factible.png]]

> [!tip] 💡 Visual — región factible
>
> $x+y\le6$, $2x+y\le10$, $x,y\ge0$: el polígono verde con vértices $(0,0),(0,6),(4,2),(5,0)$ es la intersección de los cuatro semiplanos.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Inecuación, semiplano y región factible
>
> $ax+by\le c$ (o $\ge,<,>$) divide el plano por su **frontera** $ax+by=c$: un lado cumple, el otro no. Frontera **sólida** si $\le$/$\ge$ (incluida), **punteada** si $<$/$>$ (excluida).
>
> La **región factible** $RF=\{(x,y):\text{cumple todas}\}$ es la intersección de los semiplanos. Puede ser: vacía (incompatible), acotada (polígono), no acotada (infinita), un punto o una recta. Los **vértices** son intersecciones de fronteras que pertenecen a $RF$.

> [!tip] 💡 Cómo hallar el lado correcto sin dudar
>
> Convierte en ecuación, traza la recta con dos puntos (los interceptos son lo más rápido) y prueba $(0,0)$: si cumple, sombrea su lado; si no, el opuesto. Si $(0,0)$ está sobre la frontera, prueba $(1,0)$ en su lugar.

> [!example] 🟢 Ejemplo — Región del sistema
>
> $$\begin{cases}x+y\le6\\2x+y\le10\\x\ge0,\;y\ge0\end{cases}$$
>
> Frontera 1: $(0,6),(6,0)$; $(0,0)$ cumple $\therefore$ debajo. Frontera 2: $(0,10),(5,0)$; $(0,0)$ cumple $\therefore$ debajo. Vértices: $(0,0)$; $(0,6)$ ($x=0$ con $L_1$); $(4,2)$ ($L_1\cap L_2$: $x=4,y=2$); $(5,0)$ ($L_2$ con $y=0$). Cuadrilátero acotado.

---

## 🛠️ Método Gráfico y Algebraico

> [!note] 📋 Procedimiento general
>
> 1. Trazar cada frontera (sólida o punteada según inclusión).
> 2. Elegir el lado con punto de prueba.
> 3. Intersecar: la región común es la factible.
> 4. Hallar vértices: resolver pares de fronteras $2\times2$ y **verificar** en todas las demás inecuaciones.
> 5. Clasificar: acotada, infinita, punto o vacía.
>
> **Algebraico (Fourier):** para verificar un punto, sustitúyelo en **todas**; para hallar vértices, resuelve cada par de fronteras y descarta los que fallen alguna.

> [!tip] 💡 Cómo no perder vértices ni inventarlos
>
> Enumera **todas** las intersecciones de pares de fronteras y verifica cada una en el sistema completo: la intersección de $L_1,L_2$ puede caer fuera por culpa de $L_3$ (ej. $(6,0)$ en $x+y\le6,2x+y\le10$... verifica: $6\le6$ ✓ pero $12\le10$ ✗ → no es vértice).

---

## 📐 Optimización Lineal

> [!note] 📋 Definición — Función objetivo y teorema fundamental
>
> Maximizar/minimizar $Z=ax+by$ sujeto al sistema. **Teorema:** si $RF$ es acotada y no vacía, el óptimo **existe y está en un vértice** (si se alcanza en dos, vale en toda la arista).
>
> **Método:** halla $RF$ y sus vértices, evalúa $Z$ en cada uno, elige el mayor/menor. En región no acotada puede no haber máximo ($Z\to\infty$).

> [!example] 🟢 Ejemplo — Producción óptima
>
> Maximizar $Z=3x+2y$ con $x+y\le6$, $2x+y\le10$, $x,y\ge0$.
>
> Vértices: $(0,0)\to0$; $(0,6)\to12$; $(4,2)\to16$; $(5,0)\to15$. **Máximo:** $Z=16$ en $(4,2)$.

---

## 📋 Tabla Comparativa: Tipos de Región

> [!note] 📋 Qué forma toma y cuándo
>
> | Región | Cómo se ve | Ejemplo |
> |---|---|---|
> | **Acotada** | Polígono cerrado | $x+y\le6$, $x,y\ge0$ + cota |
> | **No acotada** | Infinita en alguna dirección | $x+y\ge3$, $x,y\ge0$ |
> | **Vacía** | Nada | $x+y\le2$ con $x+y\ge5$ |
> | **Punto** | Un solo punto | $x\le3,x\ge3,y\le2,y\ge2$ → $(3,2)$ |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Sombrear el lado contrario:** siempre verifica con punto de prueba, nunca "a ojo".
> - **Línea sólida con $<$/$>$:** la frontera excluida va punteada y sus puntos no pertenecen.
> - **Aceptar intersecciones sin verificar:** todo cruce de fronteras es solo *candidato* a vértice.
> - **Confundir intersección con unión:** $RF$ exige cumplir **todas** (∩), no alguna.
> - **Olvidar $x,y\ge0$ en aplicados:** cantidades físicas no son negativas.
> - **Asumir región acotada:** con solo $\ge$ suele ser infinita.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Traza $x+2y=8$ con interceptos e indica el lado de $x+2y\le8$ con $(0,0)$.
> 2. Verifica si $(1,2)$ cumple $2x+y\le7$, $x-3y\le-4$, $x,y\ge0$.
> 3. Clasifica: $x+y\le2$ con $x+y\ge5$; $x+y\ge3$ con $x,y\ge0$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(0,4),(8,0)$; $(0,0)$ cumple → debajo.
>
> **2.** $4\le7$ ✓, $-5\le-4$ ✓ → sí es solución.
>
> **3.** Vacía (contradicción); no acotada (noreste infinito).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Halla vértices de $x+y\le5$, $x-y\le1$, $x,y\ge0$ (verifica cada cruce).
> 5. Maximiza $Z=3x+2y$ con $2x+y\le8$, $x+2y\le8$, $x,y\ge0$.
> 6. Resuelve $x+y<4$, $x>1$, $y>0$: ¿pertenecen los vértices?

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(0,0),(0,5),(3,2),(1,0)$; $(5,0)$ falla $x-y\le1$ y $(0,-1)$ falla $y\ge0$.
>
> **5.** Vértices $(0,0),(0,4),(8/3,8/3),(4,0)$; $Z$: $0,8,40/3,12$ → máximo $40/3$ en $(8/3,8/3)$.
>
> **6.** Región abierta; $(1,0),(1,3),(4,0)$ no pertenecen (fronteras excluidas).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Minimiza $C=x+2y$ con $x+2y\ge10$, $2x+y\ge10$, $x,y\ge0$ (no acotada con mínimo).
> 8. Explica con isocuantas por qué el óptimo acotado siempre está en un vértice.
> 9. Transporte: minimiza $C=2x+3y+4(40-x)+(30-y)$ con $x+y\le50$, $x+y\ge10$, $0\le x\le40$, $0\le y\le30$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Vértices factibles $(0,10),(10/3,10/3)$... evalúa: $C(0,10)=20$, $C(10/3,10/3)=10$ → mínimo $10$ en $(10/3,10/3)$.
>
> **8.** $Z=k$ son rectas paralelas; al mover $k$ el último contacto con el polígono es un vértice (o arista completa si paralela).
>
> **9.** $C=-2x+2y+190$; vértices $(0,10)$:$210$, $(0,30)$:$250$, $(20,30)$:$210$, $(40,10)$:$130$, $(40,0)$:$110$, $(10,0)$:$170$ → mínimo $110$ en $(40,0)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Trazo fronteras con interceptos, sólida o punteada según inclusión.
> - [ ] Elijo el semiplano correcto con punto de prueba.
> - [ ] Verifico si un punto dado cumple todo el sistema.
> - [ ] Distingo región vacía, acotada y no acotada.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo vértices resolviendo pares de fronteras y verificándolos.
> - [ ] Clasifico regiones y descarto cruces que fallan restricciones.
> - [ ] Optimizo evaluando $Z$ en cada vértice factible.
> - [ ] Manejo desigualdades estrictas y pertenencia de vértices.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Optimizo en regiones no acotadas decidiendo si hay máximo/mínimo.
> - [ ] Explico el teorema del vértice con isocuantas.
> - [ ] Modelo producción, dieta y transporte con restricciones.
> - [ ] Detecto aristas con infinitas soluciones óptimas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] W. L. Winston, *Operations Research: Applications and Algorithms*, 4ta ed., Cengage — cap. 3 (programación lineal gráfica).
>
> [2] J. Stewart, *Precalculus: Mathematics for Calculus*, 7th ed., Cengage, 2015 — §9 (sistemas y desigualdades).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[11 - Inecuaciones]] — inecuaciones de una variable como caso previo.
> - [[05 - Sistemas de ecuaciones lineales]] — fronteras como ecuaciones; vértices como soluciones $2\times2$.
> - [[01 - Puntos y rectas]] — trazado de fronteras en el plano.
> - [[03 - Sistemas de inecuaciones no lineales]] — siguiente: regiones curvas.

---

**Tags:** #sistemas-inecuaciones #programacion-lineal #region-factible #algebra #unidad4

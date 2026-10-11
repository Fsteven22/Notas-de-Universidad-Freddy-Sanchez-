---
dg-publish: true
---

# 📏 Clases de Rectas en el Plano

## 🎯 Introducción

> [!info] 💡 ¿Cómo se relacionan dos rectas?
>
> Dos rectas son **paralelas** ($m_1=m_2$, nunca se cortan), **perpendiculares** ($m_1m_2=-1$, ángulo $90°$), **secantes** (un corte) o **coincidentes** (la misma). Con las pendientes y los coeficientes $A_1/A_2=B_1/B_2$ se decide sin graficar.
>
> ```mermaid
> graph LR
>     A["L1, L2"] --> B{"m1 = m2?"}
>     B -->|No| C["Secantes<br/>un corte"]
>     B -->|Sí| D{"b1 = b2?"}
>     D -->|Sí| E["Coincidentes"]
>     D -->|No| F["Paralelas"]
>     style C fill:#e1ffe1
>     style F fill:#e1f5ff
> ```

![[U5-rectas.png]]

> [!tip] 💡 Visual — tres relaciones
>
> Paralelas ($m=2$ ambas), perpendiculares ($2\cdot(-1/2)=-1$) y secantes con corte marcado en $(1,3)$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Recta y sus formas
>
> Recta por $P_1,P_2$: $m=(y_2-y_1)/(x_2-x_1)$. **Formas:** punto-pendiente $y-y_1=m(x-x_1)$; explícita $y=mx+b$; general $Ax+By+C=0$; simétrica $x/a+y/b=1$ ($a,b$ interceptos).
>
> **Posición:** horizontal $y=b$ ($m=0$); vertical $x=a$ ($m$ indefinida); creciente $m>0$; decreciente $m<0$.

> [!tip] 💡 Cómo elegir la forma sin dudar
>
> ¿Tienes dos puntos? Calcula $m$ y usa punto-pendiente. ¿Tienes $m$ y un punto? Directo a punto-pendiente. ¿Necesitas comparar dos rectas? Pasa todo a forma general y compara $A_1/A_2=B_1/B_2$ — una sola cuenta decide paralelas, secantes o coincidentes.

> [!example] 🟢 Ejemplo — Recta por $(3,1)$ con $m=2$
>
> $y-1=2(x-3)\therefore y=2x-5$. Verificación en $(3,1)$: $1=6-5$ ✓

---

## 📋 Tabla Comparativa: Posiciones Relativas

> [!note] 📋 Qué condición cumple cada caso y cómo se usa
>
> | Relación | Condición ($y=mx+b$) | Condición ($Ax+By+C=0$) | Uso |
> |---|---|---|---|
> | **Paralelas** | $m_1=m_2$, $b_1\neq b_2$ | $A_1/A_2=B_1/B_2\neq C_1/C_2$ | Nunca se cortan |
> | **Perpendiculares** | $m_1m_2=-1$ | $A_1A_2+B_1B_2=0$ | Ángulo $90°$ |
> | **Secantes** | $m_1\neq m_2$ | $A_1/A_2\neq B_1/B_2$ | Corte único $x=(b_2-b_1)/(m_1-m_2)$ |
> | **Coincidentes** | $m_1=m_2$, $b_1=b_2$ | proporciones iguales | Infinitos puntos comunes |
>
> **Ángulo:** $\tan\theta=|m_2-m_1|/(1+m_1m_2)$ (agudo); **distancia** punto-recta $d=|Ax_0+By_0+C|/\sqrt{A^2+B^2}$; **haz** por $(x_0,y_0)$: $y-y_0=m(x-x_0)$ con $m$ parámetro.

> [!example] 🟢 Ejemplo — $y=2x+3$ vs $y=2x-1$ (paralelas, distancia $4/\sqrt5$)
>
> 1. $m_1=m_2=2$, $b$ distintos $\therefore$ paralelas.
> 2. Distancia: $|{-1}-3|/\sqrt{1+4}=4/\sqrt5$ (fórmula punto-recta con $(0,-1)$ sobre la 2ª).
> 3. Contrasta $y=\frac34x+2$ vs $y=-\frac43x-1$: $m_1m_2=-1$ $\therefore$ perpendiculares. $\blacksquare$

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Decir "paralelas" con $m_1=m_2$ sin mirar $b$:** si también $b_1=b_2$ son **coincidentes**, no paralelas.
> - **Perpendicular con horizontal/vertical:** $m_1m_2=-1$ no aplica ($m$ indefinida); horizontal $\perp$ vertical por definición.
> - **Olvidar el valor absoluto** en distancia y ángulo (dan magnitudes, siempre $\ge0$).
> - **Usar $y=mx+b$ con recta vertical:** $x=a$ no tiene $m$ — pasa a forma general.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Clasifica: $y=2x+1$ vs $y=2x-3$; $y=x$ vs $y=-x+2$; $y=3$ vs $x=1$.
> 2. Halla $m$ de la recta por $(1,2),(4,8)$.
> 3. Escribe $2x+3y=6$ en forma simétrica ($x/3+y/2=1$).

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Paralelas; perpendiculares ($1\cdot(-1)=-1$); perpendiculares (horizontal/vertical).
>
> **2.** $m=2$.
>
> **3.** Interceptos $(3,0),(0,2)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Paralela a $y=3x-1$ por $(2,2)$ y perpendicular por el mismo punto.
> 5. Intersección de $y=2x+1$ con $y=-x+4$.
> 6. Ángulo agudo entre $y=x$ e $y=\sqrt3\,x$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $y=3x-4$; $y=-x/3+8/3$.
>
> **5.** $(1,3)$.
>
> **6.** $\tan\theta=(\sqrt3-1)/(1+\sqrt3)=2-\sqrt3\therefore\theta=15°$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Distancia entre $y=2x+1$ e $y=2x+5$ ($4/\sqrt5$).
> 8. Haz por $(1,1)$: ¿qué $m$ da perpendicular a $y=2x$? Escribe la recta.
> 9. Prueba que $A_1/A_2=B_1/B_2\neq C_1/C_2\iff$ paralelas (sin solución el sistema).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Toma $(0,1)$: $|2\cdot0-1+5|/\sqrt5=4/\sqrt5$.
>
> **8.** $m=-1/2$; $y-1=-(x-1)/2$.
>
> **9.** Proporcionales en $A,B$ con $C$ distinto $\therefore 0=C_1-(A_1/A_2)C_2\neq0$: sistema $0\neq0$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo $m$ por dos puntos y escribo punto-pendiente.
> - [ ] Clasifico pares de rectas con $m_1,m_2$ y $b$.
> - [ ] Distingo horizontal/vertical y sus pendientes.
> - [ ] Paso entre formas punto-pendiente, explícita y general.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo paralelas y perpendiculares por un punto dado.
> - [ ] Calculo intersecciones resolviendo el sistema $2\times2$.
> - [ ] Hallo ángulos con $\tan\theta$ y distancias punto-recta.
> - [ ] Uso la forma simétrica con interceptos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Calculo distancias entre paralelas y haces por un punto.
> - [ ] Pruebo condiciones $A_1/A_2$ con sistemas.
> - [ ] Relaciono perpendicularidad con producto punto de direcciones.
> - [ ] Decido coincidencia vs paralelismo con $C_1/C_2$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 1 (la recta).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de rectas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Figuras geométricas en el plano]] — rectas como figuras base.
> - [[05 - Función lineal]] — $y=mx+b$ como función.
> - [[01 - Puntos y rectas]] — recta en forma vectorial y paramétrica.
> - [[05 - Sistemas de ecuaciones lineales]] — intersección como sistema $2\times2$.

---

**Tags:** #rectas #pendiente #paralelas #geometria #unidad5

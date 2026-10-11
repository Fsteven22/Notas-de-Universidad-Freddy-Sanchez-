---
dg-publish: true
---

# 📍 Puntos y Rectas

## 🎯 Introducción

> [!info] 💡 ¿Qué estudia la geometría analítica plana?
>
> Puntos $(x,y)$ con distancia $d=\sqrt{\Delta x^2+\Delta y^2}$ y **rectas** en sus formas (punto-pendiente, general, simétrica): con pendiente $m$, posiciones relativas y distancias se decide todo sin dibujar.
>
> ```mermaid
> graph LR
>     A["Puntos<br/>(x,y)"] --> B["Recta<br/>Ax+By=C"]
>     B --> C["Pendiente<br/>m=dy/dx"]
>     C --> D["Posición<br/>paralela/perp"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Punto, distancia y recta
>
> **Punto:** $(x,y)$; **distancia:** $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$; **punto medio:** promedio por coordenadas.
>
> **Recta:** $m=(y_2-y_1)/(x_2-x_1)$; punto-pendiente $y-y_1=m(x-x_1)$; general $Ax+By+C=0$; simétrica $x/a+y/b=1$.
>
> **Distancias:** punto-recta $d=|Ax_0+By_0+C|/\sqrt{A^2+B^2}$; **ángulo:** $\tan\theta=|m_2-m_1|/(1+m_1m_2)$.

> [!tip] 💡 Cómo hallar una recta sin dudar
>
> Con dos puntos: calcula $m$ y usa punto-pendiente con **cualquiera** de los dos (el resultado es el mismo). Con $m$ y un punto: directo. Para comparar dos rectas, pasa ambas a forma general y mira $A_1/A_2=B_1/B_2$ — decide paralelas, secantes o coincidentes de una vez.

> [!example] 🟢 Ejemplo — Recta por $A(2,3),B(5,-1)$ e intersección
>
> $m=(-1-3)/(5-2)=-4/3$; $y-3=(-4/3)(x-2)\therefore4x+3y-17=0$ (verifica en $B$: $20-3-17=0$ ✓). Alternativa determinante $\begin{vmatrix}x&y&1\\2&3&1\\5&-1&1\end{vmatrix}=0$ da lo mismo.
>
> Intersección $2x-y+3=0$ con $x+3y-5=0$: $x=5-3y\therefore2(5-3y)-y=-3\therefore y=13/7,x=-4/7$ (verifica en $L_1$ ✓).

---

## 📋 Tabla Comparativa: Formas y Posiciones

> [!note] 📋 Qué forma usar y cómo decidir posición
>
> | Forma | Ecuación | Cuándo usarla |
> |---|---|---|
> | **Punto-pendiente** | $y-y_1=m(x-x_1)$ | Tienes $m$ y un punto |
> | **Explícita** | $y=mx+b$ | Lees $m$ y corte $b$ directo |
> | **General** | $Ax+By+C=0$ | Comparar dos rectas, distancias |
> | **Simétrica** | $x/a+y/b=1$ | Interceptos $a,b$ conocidos |
> | **Paramétrica** | $(x,y)=P+t\vec{v}$ | Movimiento y dirección |
>
> | Relación | Condición | Ejemplo |
> |---|---|---|
> | **Paralelas** | $m_1=m_2$, $b$ distintos | $y=2x+1$, $y=2x-3$ |
> | **Perpendiculares** | $m_1m_2=-1$ (o $A_1A_2+B_1B_2=0$) | $y=\frac34x+2$, $y=-\frac43x-1$ |
> | **Secantes** | $m_1\neq m_2$ | Corte resolviendo $2\times2$ |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$m$ con $x$ e $y$ cruzados:** $m=(y_2-y_1)/(x_2-x_1)$ — el cambio en $y$ va **arriba**.
> - **Vertical en forma $y=mx+b$:** $x=a$ no tiene $m$; usa forma general.
> - **Distancia sin valor absoluto:** $d\ge0$ siempre; el numerador lleva $|\cdot|$.
> - **Perpendicular olvidando recíproco:** $m_\perp=-1/m$ (cambia signo **e** invierte).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Recta por $(2,3),(5,-1)$ (punto-pendiente y general).
> 2. Distancia $(0,0)$ a $(3,4)$ y punto medio.
> 3. $m$ de la recta por $(1,1),(4,7)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $m=-4/3$; $4x+3y-17=0$.
>
> **2.** $d=5$; $(3/2,2)$.
>
> **3.** $m=2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Intersección $2x-y+3=0$ con $x+3y-5=0$.
> 5. Perpendicular a $3x+4y-12=0$ por $(2,-1)$.
> 6. Distancia $(4,-2)$ a $5x-12y+13=0$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(-4/7,13/7)$ (verificado).
>
> **5.** $m=4/3$; $4x-3y-11=0$ (verifica $A_1A_2+B_1B_2=0$).
>
> **6.** $|20+24+13|/13=57/13$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Rectas por $(1,2)$ con distancia $2$ al origen.
> 8. Haz por $(0,1)$: ¿qué $m$ da distancia $1$ al punto $(2,0)$?
> 9. Prueba que $A_1/A_2=B_1/B_2\neq C_1/C_2\iff$ paralelas (sistema sin solución).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $y-2=m(x-1)$: $|2-m|/\sqrt{m^2+1}=2\therefore m=0$ o $m=-4/3$; rectas $y=2$ y $4x+3y=10$.
>
> **8.** $y-1=mx$: $|2m+1|/\sqrt{m^2+1}=1\therefore m=0$ o $m=-4/3$; rectas $y=1$ y $4x+3y=3$.
>
> **9.** Proporcionales en $A,B$ con $C$ distinto $\therefore0\neq0$ imposible.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo $m$ y escribo punto-pendiente con cualquier punto.
> - [ ] Calculo distancias y puntos medios.
> - [ ] Paso entre las cuatro formas de recta.
> - [ ] Clasifico pares de rectas por $m$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo intersecciones resolviendo $2\times2$.
> - [ ] Trazo perpendiculares con $m_\perp=-1/m$.
> - [ ] Calculo distancias punto-recta con valor absoluto.
> - [ ] Uso forma simétrica con interceptos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo haces con condiciones de distancia.
> - [ ] Pruebo condiciones $A_1/A_2$ con sistemas.
> - [ ] Manejo verticales fuera de $y=mx+b$.
> - [ ] Verifico todo sustituyendo.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 1 (puntos y rectas).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de la recta.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Clases de rectas en el plano]] — posiciones relativas sintéticas.
> - [[05 - Función lineal]] — $y=mx+b$ como función.
> - [[02 - Circunferencia]] — siguiente: distancia al centro.
> - [[05 - Sistemas de ecuaciones lineales]] — intersección como sistema.

---

**Tags:** #puntos-rectas #pendiente #distancia #geometria #unidad5

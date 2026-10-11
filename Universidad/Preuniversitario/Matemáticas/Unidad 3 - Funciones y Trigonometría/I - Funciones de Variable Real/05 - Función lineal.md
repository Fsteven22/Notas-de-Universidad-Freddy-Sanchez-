---
dg-publish: true
---

# 📈 Función Lineal

## 🎯 Introducción

> [!info] 💡 ¿Qué es la función lineal?
>
> $f(x)=mx+b$: $m$ pendiente (subida por paso), $b$ corte en $y$. Paralelas comparten $m$, perpendiculares usan $-1/m$ — y todo sistema $2\times2$ es una intersección de rectas.
>
> ```mermaid
> graph LR
>     A["m<br/>pendiente"] --> B["y=mx+b<br/>recta"]
>     B --> C["Paralela<br/>m igual"]
>     C --> D["Perp<br/>-1/m"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Pendiente, formas y distancia
>
> **Pendiente:** $m=(y_2-y_1)/(x_2-x_1)$. **Formas:** $y=mx+b$, $y-y_1=m(x-x_1)$, $Ax+By+C=0$.
>
> **Paralelas:** $m_1=m_2$. **Perpendiculares:** $m_1m_2=-1$. **Distancia:** $|Ax_0+By_0+C|/\sqrt{A^2+B^2}$.

> [!tip] 💡 Cómo no fallar con rectas
>
> Calcula $m$ primero y escribe punto-pendiente con cualquier punto dado — el resultado es el mismo. Para perpendiculares invierte **y** cambia el signo ($3\to-1/3$); el error clásico es solo invertir. La distancia punto-recta siempre lleva valor absoluto.

> [!example] 🟢 Ejemplo — Paralela y perpendicular por el origen
>
> Paralela a $y=2x+1$: $y=2x$. Perpendicular: $y=-x/2$ (verifica $2\cdot(-1/2)=-1$ ✓). Distancia $(0,0)$ a $3x+4y-10=0$: $10/5=2$.

---

## 📋 Tabla Comparativa: Posiciones

> [!note] 📋 Qué condición usar y cuándo
>
> | Relación | Condición | Ejemplo |
> |---|---|---|
> | **Paralelas** | $m_1=m_2$ | $y=2x+1$, $y=2x+5$ ($d=4/\sqrt5$) |
> | **Perpendiculares** | $m_1m_2=-1$ | $y=3x$, $y=-x/3+4/3$ |
> | **Secantes** | $m_1\neq m_2$ | $y=2x+1$, $y=-x+4$ en $(1,3)$ |
> | **Idénticas** | $m,b$ iguales | Infinitos cortes |
>
> **Aplicación:** $C=20x+500$: $34$ unidades cuestan $1180$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Perpendicular $1/m$:** es $-1/m$ (signo e inverso).
> - **$m$ con $x,y$ cruzados:** $(y_2-y_1)/(x_2-x_1)$, $y$ arriba.
> - **Cero de $3x-6$:** $x=2$ (despeja, no adivines el signo).
> - **Regresión $b=4/3$:** con $(0,1),(1,3),(2,4)$ sale $b=7/6$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $m$ de $(1,3),(3,7)$ y $(-1,2),(2,-4)$.
> 2. Recta por $(0,1)$ con $m=2$; por $(2,5)$ con $m=-1$.
> 3. Ceros de $3x-6$ y $-2x+4$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $2$; $-2$.
>
> **2.** $y=2x+1$; $y=-x+7$.
>
> **3.** $x=2$; $x=2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. ¿Colineales $(1,1),(2,3),(3,5)$? Ecuación.
> 5. Intersección $y=2x+1$ con $y=-x+4$.
> 6. Interpola $f(2)=4,f(5)=10$ en $x=3$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Sí ($m=2$); $y=2x-1$.
>
> **5.** $(1,3)$.
>
> **6.** $6$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Regresión de $(0,1),(1,3),(2,4)$.
> 8. Distancia entre $y=2x+1$ e $y=2x+5$.
> 9. Prueba $m_1m_2=-1$ con vectores dirección.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $m=1.5$, $b=7/6$ (verifica $\Sigma y=3b+m\Sigma x$).
>
> **8.** $4/\sqrt5$.
>
> **9.** $(1,m_1)\cdot(1,m_2)=1+m_1m_2=0$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo $m$ entre dos puntos.
> - [ ] Escribo punto-pendiente y explícita.
> - [ ] Hallo ceros e interceptos.
> - [ ] Trazo paralelas y perpendiculares.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Detecto colinealidad.
> - [ ] Resuelvo intersecciones $2\times2$.
> - [ ] Calculo distancias punto-recta.
> - [ ] Interpolo valores lineales.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Ajusto regresiones con fórmulas.
> - [ ] Hallo distancias entre paralelas.
> - [ ] Demuestro $m_1m_2=-1$.
> - [ ] Modelo MRU y costos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 1 (rectas).
>
> [2] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de funciones.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Puntos y rectas]] — rectas en geometría analítica.
> - [[05 - Sistemas de ecuaciones lineales]] — intersección como sistema.
> - [[07 - Función cuadrática]] — siguiente: parábolas.
> - [[10 - Ecuaciones]] — ecuación lineal $ax+b=0$.

---

**Tags:** #funciones #lineal #pendiente #unidad3

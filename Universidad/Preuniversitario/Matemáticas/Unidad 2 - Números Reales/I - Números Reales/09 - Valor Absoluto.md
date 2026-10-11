---
dg-publish: true
---

# 📏 Valor Absoluto

## 🎯 Introducción

> [!info] 💡 ¿Qué es el valor absoluto?
>
> $|x|=\max(x,-x)$: distancia al origen. $|x-a|<r$ es el intervalo $(a-r,a+r)$; $|x-a|=|x-b|$ da el punto medio. Triangular: $|a+b|\le|a|+|b|$.
>
> ```mermaid
> graph LR
>     A["|x|<br/>distancia"] --> B["Ecuación<br/>=a: dos"]
>     B --> C["Desigual<br/>intervalo"]
>     C --> D["Triangular<br/>suma"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[09-abs.png]]

> [!tip] 💡 Visual — V y distancias
>
> $|x|$ es la V con vértice $(0,0)$; $|{-3}|=3$ marca la distancia. $|x-1|=|x+3|$ da $x=-1$ (punto medio entre $1$ y $-3$).

---

## 📋 Definición Formal

> [!note] 📋 Definición — Valor, distancia y triangular
>
> **Valor:** $|x|=x$ si $x\ge0$, $-x$ si $x<0$; $\sqrt{x^2}=|x|$. **Distancia:** $d(a,b)=|a-b|$.
>
> **Ecuación:** $|f|=a\to f=\pm a$ ($a\ge0$). **Desigualdad:** $|f|<a\to-a<f<a$; $|f|>a\to f>a\lor f<-a$. **Triangular:** $|a+b|\le|a|+|b|$.

> [!tip] 💡 Cómo resolver con $|x|$ sin perder casos
>
> Parte por los ceros de cada barra y resuelve en cada tramo — $|x-1|+|x+2|\le5$ tiene 3 tramos ($x<-2$, medio, $x\ge1$) y la unión da $[-3,2]$. Para $|f|>a$ escribe las dos ramas ($\lor$); para $|f|<a$ el intervalo doble.

> [!example] 🟢 Ejemplo — $|x-1|+|x+2|\le5$ por casos
>
> $x<-2$: $-2x-1\le5\therefore x\ge-3$ (tramo $[-3,-2)$). Medio: $3\le5$ siempre. $x\ge1$: $2x+1\le5\therefore x\le2$. Unión $[-3,2]$ ✓.

---

## 📋 Tabla Comparativa: Casos

> [!note] 📋 Qué forma sale según el signo
>
> | Ecuación | Solución | Ejemplo |
> |---|---|---|
> | $\|x\|=5$ | $\pm5$ | Dos puntos |
> | $\|x-2\|=3$ | $-1,5$ | Desplaza centro |
> | $\|x-3\|<4$ | $(-1,7)$ | Intervalo abierto |
> | $\|2x+1\|\ge5$ | $(-\infty,-3]\cup[2,\infty)$ | Dos rayos |
> | $\|x-1\|=\|x+3\|$ | $x=-1$ | Punto medio |
>
> **Anidado:** $\big\||x|-2\big\|<1\therefore1<|x|<3\therefore(-3,-1)\cup(1,3)$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\sqrt{(-5)^2}=-5$:** es $5$ ($\sqrt{x^2}=|x|$).
> - **$|x-3|<4\to(-1,7]$ con $=$:** abierto en ambos (estricto).
> - **Un solo tramo en sumas:** $|x-2|+|x+1|<6$ da $(-5/2,7/2)$ (3 tramos).
> - **$\|x\|$ como $x$:** $\sqrt{x^2}=|x|$, no $x$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $|-7|$, $|3-8|$, $\sqrt{(-5)^2}$, $-|-4|$.
> 2. $|x|=5$, $|x-2|=3$, $|2x+1|=7$.
> 3. $|x-3|<4$, $|2x+1|\ge5$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $7$; $5$; $5$; $-4$.
>
> **2.** $\pm5$; $-1,5$; $3,-4$.
>
> **3.** $(-1,7)$; $(-\infty,-3]\cup[2,\infty)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $|3x-6|>9$ y $\big\||x|-2\big\|<1$.
> 5. $|x^2-4|<5$ (con $x^2\ge0$).
> 6. $x$ con $|x-1|=|x+3|$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(-\infty,-1)\cup(5,\infty)$; $(-3,-1)\cup(1,3)$.
>
> **5.** $(-3,3)$.
>
> **6.** $x=-1$ (punto medio).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $|x-2|+|x+1|<6$.
> 8. $|x+3|-|x-1|>2$.
> 9. Prueba $|a-b|\ge\big\||a|-|b|\big|$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(-5/2,7/2)$ (3 tramos verificados).
>
> **8.** $(0,\infty)$ (casos: $x>0$ aporta).
>
> **9.** $|a|=|(a-b)+b|\le|a-b|+|b|$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Evalúo $|x|$ y $\sqrt{x^2}$ con signo.
> - [ ] Resuelvo $|f|=a$ con $\pm$.
> - [ ] Escribo intervalos desde desigualdades.
> - [ ] Grafico la V con vértice.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo anidados de adentro afuera.
> - [ ] Parto en casos por ceros.
> - [ ] Demuestro la triangular por casos.
> - [ ] Hallo puntos medios equidistantes.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo sumas/restas de barras.
> - [ ] Demuestro la triangular inversa.
> - [ ] Maximizo sumas en intervalos.
> - [ ] Induzco a $n$ sumandos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Álgebra y Trigonometría* — cap. 1.
>
> [2] A. Baldor, *Aritmética*, Patria — cap. de valor absoluto.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[06 - Funciones Especiales]] — $|x|$ como función.
> - [[11 - Inecuaciones]] — inecuaciones con barras.
> - [[01 - Definición, dominio y rango]] — $\sqrt{x^2}=|x|$.
> - [[05 - Relación de orden]] — desigualdades base.

---

**Tags:** #números-reales #valor-absoluto #desigualdades #unidad2

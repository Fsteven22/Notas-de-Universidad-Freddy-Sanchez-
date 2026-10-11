---
dg-publish: true
---

# ⚖️ Inecuaciones

## 🎯 Introducción

> [!info] 💡 ¿Qué es una inecuación?
>
> Desigualdad con incógnita ($<,\le,>,\ge$): se despeja como ecuación pero $\times\div$ negativo **invierte**, y racionales/radicales/módulos piden tabla de críticos o casos. La solución es un intervalo o unión.
>
> ```mermaid
> graph LR
>     A["Despeja<br/>invierte -"] --> B["Críticos<br/>ceros+vert"]
>     B --> C["Tabla<br/>signos"]
>     C --> D["Intervalo<br/>unión"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Propiedades y métodos
>
> **Propiedades:** $a<b\therefore a+c<b+c$; $a<b,c<0\therefore ac>bc$ (invierte); recíprocos en positivos invierten.
>
> **Métodos:** lineales (despeja+invierte); cuadráticas/polinómicas (raíces+tabla); racionales (críticos con verticales); $|f|<a\to-a<f<a$; radicales (dominio+eleva+verifica).

> [!tip] 💡 Cómo resolver sin fallar los extremos
>
> Lleva todo a un lado y factoriza antes de la tabla — los críticos son ceros **y** verticales. Los extremos con $=$ se incluyen solo si son ceros (nunca verticales): $x/(x-3)\le2$ da $(-\infty,3)\cup[6,\infty)$, con el $3$ fuera siempre.

> [!example] 🟢 Ejemplo — $x^2-5x+6<0$ y $(x^2-4)/(x+1)\ge0$
>
> Raíces $2,3$, abre arriba $\therefore(2,3)$. Racional: críticos $-2,-1,2$; signos $-,+,-,+$; $\ge0$ con $-1$ fuera $\therefore\{-2\}\cup[2,\infty)$.

---

## 📋 Tabla Comparativa: Tipos

> [!note] 📋 Qué método usa cada tipo
>
> | Tipo | Método | Ejemplo |
> |---|---|---|
> | Lineal | Despeja + invierte $-$ | $-2x+5\ge9\therefore x\le-2$ |
> | Cuadrática | Raíces + parábola | $x^2-5x+6<0\therefore(2,3)$ |
> | Racional | Tabla con verticales | $(x-1)/(x+2)>0\therefore(-\infty,-2)\cup(1,\infty)$ |
> | $\|f\|$ | Intervalo o ramas | $\|2x+1\|\ge5\therefore(-\infty,-3]\cup[2,\infty)$ |
> | Radical | Dominio + eleva | $\sqrt{x-2}<3\therefore[2,11)$ |
> | Exp/log | Monotonía (base $<1$ invierte) | $\log_2(x-1)<3\therefore(1,9)$ |
>
> **Sistemas:** intersecta ($\begin{cases}2x-1<5\\x+3\ge1\end{cases}\therefore[-2,3)$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Multiplicar en cruz con $x$:** lleva a un lado y tabla (el signo de $x$ importa).
> - **Vertical incluida:** $x=3$ en $x/(x-3)\le2$ jamás entra.
> - **Elevar sin dominio:** $\sqrt{x+1}>x-1$ da $[-1,3)$, no $(-1,\infty)$.
> - **$|x-2|+|x+1|<6\to(-3,5)$:** es $(-5/2,7/2)$ (3 tramos).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $3x-7<11$, $-2x+5\ge9$, $(x-2)/3>1$.
> 2. $x^2-5x+6<0$, $x^2-9\le0$, $-x^2+6x-5>0$.
> 3. $|x-3|<4$, $|2x+1|\ge5$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(-\infty,6)$; $(-\infty,-2]$; $(5,\infty)$.
>
> **2.** $(2,3)$; $[-3,3]$; $(1,5)$.
>
> **3.** $(-1,7)$; $(-\infty,-3]\cup[2,\infty)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $(x-1)/(x+2)>0$, $x/(x-3)\le2$, $1/x<1/(x-1)$.
> 5. $\sqrt{x-2}<3$, $\sqrt{x+1}>x-1$, $\sqrt{2x-1}\le\sqrt{x+3}$.
> 6. Sistemas: $2x-1<5$ con $x+3\ge1$; $|x|<3$ con $x^2-2x-3\ge0$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(-\infty,-2)\cup(1,\infty)$; $(-\infty,3)\cup[6,\infty)$; $(-\infty,0)\cup(1,\infty)$.
>
> **5.** $[2,11)$; $[-1,3)$; $[1/2,4]$.
>
> **6.** $[-2,3)$; $(-3,-1]$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $|x-2|+|x+1|<6$; $|x+3|-|x-1|>2$.
> 8. $(x-1)(x+2)(x-3)\ge0$; $x^3-4x^2+4x>0$.
> 9. $h(t)=100t-5t^2>480$; $(x^2-1)/(x^2+1)>1/2$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(-5/2,7/2)$; $(0,\infty)$.
>
> **8.** $[-2,1]\cup[3,\infty)$; $(0,2)\cup(2,\infty)$.
>
> **9.** $(8,12)$; $(-\infty,-\sqrt3)\cup(\sqrt3,\infty)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Despejo invirtiendo con negativos.
> - [ ] Resuelvo cuadráticas con parábola.
> - [ ] Aplico $|f|<a$ y $|f|>a$.
> - [ ] Escribo soluciones como intervalos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Armo tablas con verticales.
> - [ ] Resuelvo radicales con dominio.
> - [ ] Intersecto sistemas.
> - [ ] Verifico extremos sustituyendo.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo sumas de módulos por casos.
> - [ ] Hallo tablas cúbicas completas.
> - [ ] Modelo ganancias y proyectiles.
> - [ ] Detecto extrañas al elevar.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de inecuaciones.
>
> [2] J. Stewart, *Precálculo*, 7ma ed. — cap. 1.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[10 - Ecuaciones]] — base: despejes.
> - [[09 - Valor Absoluto]] — $|f|$ a fondo.
> - [[05 - Relación de orden]] — orden y supremo.
> - [[12 - Funciones racionales]] — tablas racionales.

---

**Tags:** #números-reales #inecuaciones #intervalos #unidad2

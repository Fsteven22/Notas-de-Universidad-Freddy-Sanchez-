---
dg-publish: true
---

# 📉 Función Cuadrática

## 🎯 Introducción

> [!info] 💡 ¿Qué es la función cuadrática?
>
> $f(x)=ax^2+bx+c$: parábola con vértice $(-b/2a,f(-b/2a))$, apertura según $a$ y raíces según $\Delta=b^2-4ac$. Optimizar es leer el vértice.
>
> ```mermaid
> graph LR
>     A["a,b,c<br/>coeficientes"] --> B["Vértice<br/>-b/2a"]
>     B --> C["Raíces<br/>Delta"]
>     C --> D["Óptimo<br/>vértice"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Formas, vértice y discriminante
>
> **Formas:** $ax^2+bx+c$, $a(x-h)^2+k$, $a(x-x_1)(x-x_2)$. **Vértice:** $h=-b/2a$, $k=f(h)$.
>
> **Discriminante:** $\Delta>0$ dos raíces; $=0$ doble; $<0$ ninguna real. **Vieta:** suma $-b/a$, producto $c/a$.

> [!tip] 💡 Cómo resolver cuadráticas sin enredarse
>
> Completa cuadrados para el vértice, usa $\Delta$ antes de la fórmula para saber cuántas raíces esperar, y verifica con Vieta (la suma y el producto delatan errores de signo). En optimización con restricción (perímetro, suma fija), despeja una variable y el vértice da el máximo.

> [!example] 🟢 Ejemplo — Rectángulo de perímetro 40
>
> $2x+2y=40\therefore y=20-x$; $A=x(20-x)$ con vértice $x=10\therefore$ cuadrado $10\times10$, $A=100$.

---

## 📋 Tabla Comparativa: Discriminante

> [!note] 📋 Qué dice $\Delta$ y cuándo
>
> | $\Delta$ | Raíces | Ejemplo |
> |---|---|---|
> | $>0$ | Dos reales distintas | $x^2-5x+6$: $2,3$ |
> | $=0$ | Una doble | $x^2+kx+9$: $k=\pm6$ |
> | $<0$ | Ninguna real | $x^2+1$: sin cortes |
>
> **Signo:** $ax^2+bx+c\ge k\iff a>0$ y $\Delta\le0$ (completando: $a(x+b/2a)^2+\ldots$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Vértice $-b/2a$ con signo:** en $x^2-4x+3$, $h=+2$ (doble negativo).
> - **$\Delta$ mal calculado:** $b^2-4ac$ con todos los signos.
> - **Máx/mín cruzados:** $a>0$ mínimo, $a<0$ máximo.
> - **Inecuación $\le0$ fuera de raíces:** es **entre** raíces ($[-1,4]$ en $x^2-3x-4$).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Vértice y apertura de $x^2-2x$, $-x^2+4$, $2x^2+1$.
> 2. Raíces de $x^2-5x+6$, $x^2-4$, $x^2+1$.
> 3. Máx/mín de $x^2-4x+3$ y $-x^2+2$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(1,-1)$↑; $(0,4)$↓; $(0,1)$↑.
>
> **2.** $2,3$; $\pm2$; ninguna real.
>
> **3.** Mín $-1$ en $x=2$; máx $2$ en $x=0$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $2x^2+5x+2=0$ con fórmula y Vieta.
> 5. $h(t)=-5t^2+20t$: altura máxima y tiempo.
> 6. Intersección $y=x^2$ con $y=2x+3$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $x=-1/2,-2$ (suma $-5/2$, producto $1$).
>
> **5.** $20$ m en $t=2$ s.
>
> **6.** $(-1,1),(3,9)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Trayectoria $y=-x^2+6x$: alcance y altura.
> 8. Dos números suman 10, producto máximo.
> 9. $ax^2+bx+c$ por $(0,1),(1,0),(2,3)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Alcance $6$, máx $9$ en $x=3$.
>
> **8.** $5,5$ (vértice de $x(10-x)$).
>
> **9.** $a=2,b=-3,c=1$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo vértices con $-b/2a$.
> - [ ] Decido apertura por el signo de $a$.
> - [ ] Resuelvo con fórmula y $\Delta$.
> - [ ] Completo cuadrados.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Verifico con Vieta.
> - [ ] Optimizo áreas y alturas.
> - [ ] Hallo intersecciones parábola-recta.
> - [ ] Decido máx/mín por $a$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Pruebo condiciones de signo con $\Delta$.
> - [ ] Ajusto parábolas por tres puntos.
> - [ ] Resuelvo inecuaciones con la parábola.
> - [ ] Modelo trayectorias.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 3 (polinomios).
>
> [2] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de cuadráticas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Parábola]] — parábola como cónica.
> - [[10 - Ecuaciones]] — ecuación cuadrática.
> - [[11 - Inecuaciones]] — inecuaciones con parábola.
> - [[11 - Funciones polinomiales]] — grado 2 como caso.

---

**Tags:** #funciones #cuadratica #vertice #unidad3

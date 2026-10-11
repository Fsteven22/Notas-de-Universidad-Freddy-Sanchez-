---
dg-publish: true
---

# 📈 Parábola

## 🎯 Introducción

> [!info] 💡 ¿Qué es una parábola?
>
> El conjunto $\{P:d(P,F)=d(P,\ell)\}$ (equidista del foco $F$ y la directriz $\ell$): $(x-h)^2=4p(y-k)$ si abre vertical, con vértice $V$, parámetro $p$ y lado recto $4p$.
>
> ```mermaid
> graph LR
>     A["Foco F<br/>directriz l"] --> B["Equidista<br/>d(P,F)=d(P,l)"]
>     B --> C["Vértice<br/>punto medio"]
>     C --> D["Ecuación<br/>4p"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-parabola.png]]

> [!tip] 💡 Visual — $x^2=12y$
>
> Foco $(0,3)$, directriz $y=-3$, vértice $(0,0)$, $p=3$: verifica $(6,3)$ con $d=6$ a ambos.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Elementos y canónicas
>
> **Elementos:** vértice $V$ (punto medio $F$-directriz), foco $F$ a distancia $p$, directriz $\ell$ perpendicular al eje, lado recto $4p$.
>
> **Vertical:** $(x-h)^2=4p(y-k)$ (abre arriba si $p>0$). **Horizontal:** $(y-k)^2=4p(x-h)$ (derecha si $p>0$).

> [!tip] 💡 Cómo hallarla sin perderse
>
> Marca $V$ y $F$: el vector $V\to F$ da el **eje** y su longitud es $p$; la directriz es perpendicular por el punto opuesto a distancia $p$. El signo de $p$ (foco arriba/derecha = $+$) decide la ecuación — dibuja primero, escribe después.

> [!example] 🟢 Ejemplo — Foco $(0,3)$, directriz $y=-3$
>
> Eje vertical; $V=(0,0)$ (punto medio); $p=3$; abre arriba $\therefore x^2=12y$. Verificación $(6,3)$: $d(F)=6$, $d(\ell)=|3+3|=6$ ✓

---

## 📋 Tabla Comparativa: Orientaciones

> [!note] 📋 Qué ecuación corresponde y cuándo
>
> | Abre hacia | Ecuación | Foco | Directriz |
> |---|---|---|---|
> | **Arriba** | $(x-h)^2=4p(y-k)$, $p>0$ | $(h,k+p)$ | $y=k-p$ |
> | **Abajo** | $(x-h)^2=4p(y-k)$, $p<0$ | $(h,k+p)$ | $y=k-p$ |
> | **Derecha** | $(y-k)^2=4p(x-h)$, $p>0$ | $(h+p,k)$ | $x=h-p$ |
> | **Izquierda** | $(y-k)^2=4p(x-h)$, $p<0$ | $(h+p,k)$ | $x=h-p$ |
>
> **General:** $y^2+6y-4x+5=0\therefore(y+3)^2=4(x+1)$: $V(-1,-3)$, $p=1$, $F(0,-3)$, $x=-2$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$p$ con signo cambiado:** $p$ lleva el signo de la dirección (foco arriba $=+$); verifica con un punto.
> - **Directriz del lado del foco:** va **opuesta** ($x=h-p$ si el foco es $h+p$).
> - **Completar cuadrados sin balancear:** lo sumado a la izquierda se suma a la derecha.
> - **Lado recto $=p$:** es $4p$ (cuerda focal completa).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $V(2,3)$, $F(5,3)$: ecuación y directriz.
> 2. $y^2+6y-4x+5=0$: $V,F$, directriz, $p$.
> 3. Lado recto de $x^2=12y$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $p=3$; $(y-3)^2=12(x-2)$; $x=-1$.
>
> **2.** $V(-1,-3)$, $p=1$, $F(0,-3)$, $x=-2$.
>
> **3.** $4p=12$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Parábola vertical por $(0,0),(2,1),(4,4)$ ($y=x^2/4$... halla $a,b,c$).
> 5. Tangente a $x^2=12y$ en $(6,3)$ ($y=x-3$... verifica $m=x/6$).
> 6. Reflector: rayos paralelos al eje pasan por el foco (antena).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $c=0$, $4a+2b=1$, $16a+4b=4\therefore a=1/4,b=0$.
>
> **5.** Deriva $2x=12y'\therefore m=1$; $y-3=x-6$.
>
> **6.** Propiedad focal: todo rayo axial refleja al foco.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $x^2=4py$ desde $d(P,F)=d(P,\ell)$.
> 8. Intersección $x^2=12y$ con $y=x+2$ (discriminante).
> 9. Lugar: puntos cuya distancia a $(0,2)$ es el doble que a $y=-1$ (elipse... verifica: $x^2+(y-2)^2=4(y+1)^2$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\sqrt{x^2+(y-p)^2}=|y+p|\therefore x^2=4py$.
>
> **8.** $x^2=12x+24\therefore x=6\pm4\sqrt3$ (dos cortes).
>
> **9.** $x^2-3y^2-12y=0\therefore$ hipérbola (no parábola: razón $\neq1$).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico $V,F$, directriz y $p$ con signos.
> - [ ] Escribo canónicas verticales y horizontales.
> - [ ] Calculo lados rectos $4p$.
> - [ ] Distingo orientación por posición del foco.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Completo cuadrados para hallar elementos.
> - [ ] Hallo tangentes derivando implícitamente.
> - [ ] Ajusto parábolas por tres puntos.
> - [ ] Verifico puntos con equidistancia.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro $x^2=4py$ desde la definición.
> - [ ] Resuelvo intersecciones con discriminante.
> - [ ] Clasifico lugares por razón de distancias.
> - [ ] Explico la propiedad focal del reflector.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 3 (parábola).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de cónicas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[07 - Función cuadrática]] — $y=ax^2+bx+c$ como parábola vertical.
> - [[02 - Circunferencia]] — completar cuadrados igual que aquí.
> - [[04 - Elipse]] — siguiente cónica: dos focos.
> - [[01 - Puntos y rectas]] — directriz como recta.

---

**Tags:** #parabola #foco #conicas #geometria #unidad5

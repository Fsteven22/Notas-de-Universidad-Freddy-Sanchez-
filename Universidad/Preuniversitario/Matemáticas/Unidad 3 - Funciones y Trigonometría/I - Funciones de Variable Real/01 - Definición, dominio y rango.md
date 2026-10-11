---
dg-publish: true
---

# 📐 Definición, Dominio y Rango

## 🎯 Introducción

> [!info] 💡 ¿Qué es una función real?
>
> $f:D\to\mathbb{R}$ ($D\subseteq\mathbb{R}$) asigna a cada $x$ un único $y=f(x)$: el **dominio** son las entradas válidas, el **rango** las salidas alcanzadas, y la prueba vertical decide si una gráfica es función.
>
> ```mermaid
> graph LR
>     A["Dominio<br/>D"] --> B["f<br/>regla"]
>     B --> C["Rango<br/>Im(f)"]
>     C --> D["Gráfica<br/>(x,f(x))"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U3-01-dominio.png]]

> [!tip] 💡 Visual — Dominio restringido
>
> $f(x)=1/x$ no existe en $x=0$ ($\text{Dom}=\mathbb{R}\setminus\{0\}$); $g(x)=\sqrt{x}$ exige $x\ge0$. Las asíntotas y cortes marcan lo prohibido.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Función, dominio y rango
>
> **Función:** $f:D\to B$ con totalidad ($\forall x\in D\;\exists y$) y unicidad (un solo $y$ por $x$). $f(a)$ imagen; $f^{-1}(\{b\})$ preimagen.
>
> **Dominio:** $\text{Dom}(f)=\{x:f(x)\text{ definida}\}$. **Rango:** $\text{Ran}(f)=\{f(x):x\in\text{Dom}\}$.

> [!tip] 💡 Cómo hallar dominios sin olvidar casos
>
> Revisa en orden: denominador $\neq0$, raíz par $\ge0$, logaritmo $>0$ — lo que quede es $\mathbb{R}$. Para el rango, el vértice manda en cuadráticas y los signos en racionales; si cancelas factores, el dominio **no** se agranda.

> [!example] 🟢 Ejemplo — $f(x)=\sqrt{x^2-4}$
>
> $x^2\ge4\therefore\text{Dom}=(-\infty,-2]\cup[2,\infty)$; $\text{Ran}=[0,\infty)$ (la raíz nunca es negativa). Verifica $x=\pm2\to0$ ✓

---

## 📋 Tabla Comparativa: Reglas de Dominio

> [!note] 📋 Qué condición aplica y cuándo
>
> | Expresión | Condición | Ejemplo |
> |---|---|---|
> | **Denominador** | $\neq0$ | $1/(x-2)$: $\mathbb{R}\setminus\{2\}$ |
> | **Raíz par** | $\ge0$ | $\sqrt{x-1}$: $[1,\infty)$ |
> | **Logaritmo** | $>0$ | $\ln(2x+1)$: $(-1/2,\infty)$ |
> | **Polinomio** | Ninguna ($\mathbb{R}$) | $x^2+1$: $\mathbb{R}$ |
> | **Composición** $g\circ f$ | $x\in\text{Dom}(f)$, $f(x)\in\text{Dom}(g)$ | $\sqrt{x^2}$: $\mathbb{R}$ |
>
> **Prueba vertical:** cada recta $x=a$ corta la gráfica a lo más una vez ($x^2+y^2=1$ falla en $x=0$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$f$ vs $f(x)$:** la regla vs el valor en un punto.
> - **Cancelar sin dominio:** $(x^2-4)/(x-2)=x+2$ solo si $x\neq2$.
> - **$g\circ f=f\circ g$:** el orden importa (dominios distintos).
> - **Rango de $\sqrt{x^2}$:** dominio $\mathbb{R}$ pero rango $[0,\infty)$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $\text{Dom}$ de $1/(x-3)$, $\sqrt{2x+4}$, $x^2+1$.
> 2. $\text{Ran}$ de $x^2$ y $1/x$.
> 3. ¿Función? $y=2x+1$, $x^2+y^2=4$, $y=\pm\sqrt{x}$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\mathbb{R}\setminus\{3\}$; $[-2,\infty)$; $\mathbb{R}$.
>
> **2.** $[0,\infty)$; $\mathbb{R}\setminus\{0\}$.
>
> **3.** Sí; no; no.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $\text{Ran}$ de $x^2-4x+3$ (vértice).
> 5. $\text{Dom}(g\circ f)$ con $f(x)=x^2$, $g(x)=\sqrt{x}$.
> 6. Por tramos $x^2$ si $x<0$, $2x+1$ si $x\ge0$: $\text{Dom},\text{Ran}$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $[-1,\infty)$ (vértice $(2,-1)$).
>
> **5.** $x^2\ge0$ siempre $\therefore\mathbb{R}$.
>
> **6.** $\mathbb{R}$; $[0,\infty)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $\text{Dom}$ de $\sqrt{(x-1)/(x+2)}$ (tabla de signos).
> 8. $f(x)=1/(1+1/x)$: simplifica y dominio.
> 9. Halla $a$ con $\text{Ran}(x^2+ax+1)=[0,\infty)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(-\infty,-2)\cup[1,\infty)$.
>
> **8.** $x/(x+1)$; $x\neq0,-1$.
>
> **9.** $\Delta=0\therefore a=\pm2$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo $\text{Dom}$ con reglas ($\neq0$, $\ge0$, $>0$).
> - [ ] Distingo función de relación con prueba vertical.
> - [ ] Evalúo $f(a)$ y hallo preimágenes.
> - [ ] Reconozco notación $f:D\to C$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo $\text{Ran}$ con vértice y signos.
> - [ ] Compongo con dominio restringido.
> - [ ] Resuelvo funciones por tramos.
> - [ ] Verifico ceros de logaritmos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Hallo dominios con tabla de signos.
> - [ ] Pruebo $\text{Dom}(f+g)=\text{Dom}(f)\cap\text{Dom}(g)$.
> - [ ] Parametrizo rangos con $\Delta$.
> - [ ] Despejo relaciones implícitas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 2 (funciones).
>
> [2] K. Rosen, *Matemática Discreta*, McGraw-Hill — §2.3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[10 - Funciones en Conjuntos]] — $f:A\to B$ general.
> - [[02 - Representación gráfica]] — siguiente: gráfica.
> - [[04 - Tipos de funciones]] — clasificación.
> - [[03 - Funciones definidas por tramos]] — tramos a fondo.

---

**Tags:** #funciones #dominio #rango #unidad3

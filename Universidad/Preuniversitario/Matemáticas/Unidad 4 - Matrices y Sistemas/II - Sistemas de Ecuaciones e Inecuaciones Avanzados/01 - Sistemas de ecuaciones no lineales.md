---
dg-publish: true
---

# 📐 Sistemas de Ecuaciones No Lineales

## 🎯 Introducción

> [!info] 💡 ¿Qué cambia respecto a lo lineal?
>
> Con potencias, raíces o exponenciales ($x^2$, $\sqrt{x}$, $e^x$) no hay un método único como Gauss: se combinan **sustitución** (reducir a una incógnita), **lectura gráfica** (intersección de curvas) y **métodos numéricos** (Newton). Los sistemas **simétricos** sí tienen técnica propia ($s=x+y$, $p=xy$).
>
> ```mermaid
> graph LR
>     A["Ecs no lineales"] --> B["Sustitución"]
>     A --> C["Gráfico"]
>     A --> D["Numérico<br/>Newton"]
>     style C fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Sistema no lineal y sus métodos
>
> Un sistema es **no lineal** si alguna ecuación no es de la forma $a_1x_1+\dots+a_nx_n=b$. Métodos:
>
> - **Sustitución:** despeja una variable y sustituye (reduce a una incógnita).
> - **Gráfico:** las soluciones son intersecciones de curvas (da número y ubicación aproximada).
> - **Newton-Raphson:** $x_{n+1}=x_n-\dfrac{f(x_n)}{f'(x_n)}$ converge rápido si $x_0$ está cerca de la raíz.

> [!tip] 💡 Cómo elegir el método sin dudar
>
> Si una ecuación es lineal, despeja de ahí y sustituye (siempre funciona). Si ambas son curvas conocidas (recta-círculo, parábola-recta), dibuja mentalmente las intersecciones para saber **cuántas** soluciones buscar antes de operar. Reserva Newton para ecuaciones que no se despejan ($e^x=x+2$).

> [!example] 🟢 Ejemplo — Sustitución $\begin{cases}x^2+y=3\\x+y=1\end{cases}$
>
> 1. De la 2ª: $y=1-x$.
> 2. Sustituye: $x^2+(1-x)=3\therefore x^2-x-2=0\therefore(x-2)(x+1)=0$.
> 3. $x=2\therefore y=-1$; $x=-1\therefore y=2$. **Soluciones:** $(2,-1),(-1,2)$ (verifica en ambas).

---

## 📋 Tabla Comparativa: Métodos de Resolución

> [!note] 📋 Qué método usar y cuándo
>
> | Método | Cuándo | Clave |
> |---|---|---|
> | **Sustitución** | Una ecuación despejable | Despeja y sustituye |
> | **Simétricos** $s,p$ | Invariante ante $x\leftrightarrow y$ | $x,y$ raíces de $t^2-st+p=0$ |
> | **Igualación** | Misma variable despejable en ambas | Iguala expresiones |
> | **Gráfico** | Cónicas y rectas | Cortes $0,1,2$ |

> [!note] 📋 Definición — Cambio $s=x+y$, $p=xy$
>
> Un sistema es **simétrico** si no cambia al permutar $x\leftrightarrow y$. Con $s=x+y$, $p=xy$: $x^2+y^2=s^2-2p$, $x^3+y^3=s^3-3ps$. Luego $x,y$ son raíces de $t^2-st+p=0$.
>
> **Polinómicas simétricas en 3 variables:** $x+y+z$, $xy+yz+zx$, $xyz$ como base.

> [!tip] 💡 Cómo reconocerlos al instante
>
> Si intercambias $x$ por $y$ en todo el sistema y queda **idéntico**, es simétrico: pasa directo a $s,p$ sin intentar sustitución a ciegas (que suele enredarse).

> [!example] 🟢 Ejemplo — $x+y=5$, $x^2+y^2=13$
>
> 1. $(x+y)^2=x^2+2xy+y^2\therefore25=13+2xy\therefore xy=6$.
> 2. $x,y$ son raíces de $t^2-5t+6=0$: $t=2,3$.
> 3. **Soluciones:** $(2,3),(3,2)$ (el par simétrico siempre acompaña). $\blacksquare$

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Dividir por una variable sin discutir si vale $0$:** se pierden soluciones (ej. dividir por $x$ elimina $x=0$).
> - **Elevar al cuadrado sin verificar:** aparecen soluciones extrañas ($\sqrt{x}=-1$ no da $x=1$ como solución válida).
> - **Olvidar el par simétrico:** en sistemas simétricos, si $(a,b)$ es solución con $a\neq b$, $(b,a)$ también lo es.
> - **Aceptar raíces de Newton sin comprobar:** el método puede converger a una raíz distinta o divergir si $x_0$ está lejos.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Resuelve $\begin{cases}x+y=5\\x^2+y^2=13\end{cases}$ con $s,p$.
> 2. Resuelve $\begin{cases}x+y=5\\xy=6\end{cases}$ pasando a $t^2-5t+6=0$.
> 3. Resuelve $x^2+y^2=25$, $x+y=7$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $xy=6$; $(2,3),(3,2)$.
>
> **2.** $t=2,3$; $(2,3),(3,2)$.
>
> **3.** $xy=12$; $(3,4),(4,3)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Resuelve $\begin{cases}x^2+xy+y^2=7\\x+y=1\end{cases}$ sustituyendo $y=1-x$.
> 5. Resuelve $\begin{cases}x^3+y^3=9\\x+y=3\end{cases}$ con $x^3+y^3=s^3-3ps$.
> 6. Itera Newton para $\sqrt[3]{5}$ desde $x_0=2$ (3 iteraciones).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $x^2+x(1-x)+(1-x)^2=7\therefore x^2-x-2=0$: $(2,-1),(-1,2)$.
>
> **5.** $27-9p=9\therefore p=2$; $t^2-3t+2=0$: $(1,2),(2,1)$.
>
> **6.** $f=x^3-5$: $x_1\approx1.71$, $x_2\approx1.71$, $x_3\approx1.71$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Resuelve $\begin{cases}x^2+y^2+z^2=14\\x+y+z=6\\xy+yz+zx=11\end{cases}$ pasando a cúbica $t^3-6t^2+11t-6=0$.
> 8. Factoriza $x^3+y^3+z^3-3xyz$ y explica su uso en sistemas simétricos.
> 9. Resuelve $e^x=x+2$ por intersección gráfica y refina una raíz con Newton.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Raíces $1,2,3$: las $6$ permutaciones son solución.
>
> **8.** $(x+y+z)(x^2+y^2+z^2-xy-yz-zx)$; si $x+y+z=0$, entonces $x^3+y^3+z^3=3xyz$.
>
> **9.** $f=e^x-x-2$; $x_0=1$: $x_1\approx1.84$ (la otra raíz $x\approx-1.1$ se halla desde $x_0=-1$).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Resuelvo sistemas simétricos $2\times2$ con $s=x+y$, $p=xy$.
> - [ ] Aplico sustitución reduciendo a una incógnita y verifico.
> - [ ] Predigo el número de soluciones con lectura gráfica.
> - [ ] Distingo sistemas lineales de no lineales al leerlos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Uso $x^3+y^3=s^3-3ps$ en sistemas cúbicos simétricos.
> - [ ] Aplico Newton en una variable con $x_0$ razonable.
> - [ ] Verifico soluciones extrañas al elevar al cuadrado.
> - [ ] No divido por variables sin discutir el cero.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo sistemas simétricos de 3 variables pasando a cúbica.
> - [ ] Factorizo $x^3+y^3+z^3-3xyz$ y la aplico.
> - [ ] Combino gráfica y Newton en ecuaciones trascendentes.
> - [ ] Explico cuándo Newton converge y cuándo diverge.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precalculus: Mathematics for Calculus*, 7th ed., Cengage, 2015 — §10.5 (sistemas no lineales).
>
> [2] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de sistemas (simétricos y numéricos).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[05 - Sistemas de ecuaciones lineales]] — Gauss y Rouché como contraste: aquí no hay método único.
> - [[06 - Conceptos asociados a los números enteros]] — ecuaciones diofantinas (soluciones enteras).
> - [[07 - Expresiones algebraicas]] — factorización usada en $s,p$ y Ruffini.
> - [[13 - Funciones exponenciales]] — $e^x$ en ecuaciones trascendentes.

---

**Tags:** #sistemas-no-lineales #simetricos #newton #algebra #unidad4

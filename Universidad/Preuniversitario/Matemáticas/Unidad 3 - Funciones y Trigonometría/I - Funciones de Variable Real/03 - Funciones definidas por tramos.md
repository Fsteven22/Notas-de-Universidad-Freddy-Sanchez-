---
dg-publish: true
---

# 🧩 Funciones por Tramos

## 🎯 Introducción

> [!info] 💡 ¿Qué es una función por tramos?
>
> Reglas distintas según el intervalo ($|x|$, $\text{sgn}$, tarifas): se evalúa eligiendo el tramo del punto, y en las fronteras se decide continuidad comparando límites laterales con el valor.
>
> ```mermaid
> graph LR
>     A["Punto x<br/>¿qué tramo?"] --> B["Evalúa<br/>regla local"]
>     B --> C["Frontera<br/>límites lat"]
>     C --> D["Continua<br/>si coinciden"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Tramos, continuidad y notación
>
> **Por tramos:** $f(x)=f_i(x)$ si $x\in I_i$, con $I_i$ partición del dominio. **Continuidad en frontera $c$:** $\lim^-=\lim^+=f(c)$.
>
> **Notación:** ○ abierto (excluye), ● cerrado (incluye); $|x|=-x$ si $x<0$, $x$ si $x\ge0$.

> [!tip] 💡 Cómo evaluar y graficar sin errores
>
> Antes de calcular, pregunta en qué intervalo cae $x$ — el error típico es usar la regla vecina. En fronteras dibuja ○ donde el tramo no incluye y ● donde sí; la continuidad se verifica con los tres valores (izquierda, derecha, punto), no a ojo.

> [!example] 🟢 Ejemplo — $f(x)=x^2$ si $x<0$, $2x+1$ si $x\ge0$
>
> $f(-2)=4$, $f(0)=1$, $f(3)=7$. En $x=0$: $\lim^-=0\neq1=f(0)\therefore$ discontinua (salto). $\text{Ran}=[0,\infty)$.

---

## 📋 Tabla Comparativa: Funciones Típicas

> [!note] 📋 Qué tramos usa cada una
>
> | Función | Tramos | Frontera |
> |---|---|---|
> | $\|x\|$ | $-x$ / $x$ | Continua en $0$, no derivable |
> | $\text{sgn}(x)$ | $-1,0,1$ | Salto en $0$ |
> | $\lfloor x\rfloor$ | $[n,n+1)\to n$ | Saltos en enteros |
> | $\|x-2\|$ | $2-x$ / $x-2$ | Vértice en $(2,0)$ |
> | Tarifa | Fijo + excedente | Continua por diseño |
>
> **Composición:** $\|x^2-1\|$: ceros $\pm1$ dan 3 tramos.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Regla vecina:** evalúa siempre con el tramo que contiene a $x$.
> - **○/● cruzados:** el abierto excluye, el cerrado incluye.
> - **Continua a ojo:** compara límites laterales con $f(c)$.
> - **$\lfloor-1.2\rfloor=-1$:** es $-2$ (hacia abajo, no hacia cero).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $f(-2),f(0),f(3)$ del ejemplo.
> 2. $|x|$ por tramos; $|{-5}|,|3|$.
> 3. Grafica $\text{sgn}(x)$ con ○/●.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $4,1,7$.
>
> **2.** $-x$ si $x<0$, $x$ si $x\ge0$; $5,3$.
>
> **3.** $-1,0,1$ con salto en $0$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Continuidad en $x=0$ del ejemplo.
> 5. Escribe $|x-2|$ por tramos.
> 6. ¿Continua en $0$? $f=1/x$ si $x\neq0$, $0$ si $x=0$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** No ($\lim^-=0\neq1$).
>
> **5.** $2-x$ si $x<2$, $x-2$ si $x\ge2$.
>
> **6.** No (límite no existe).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Halla $a$ con $x^2$ si $x<1$, $ax+1$ si $x\ge1$ continua.
> 8. $\text{Ran}$ de $|x^2-4|$.
> 9. Derivabilidad de $|x|$ en $0$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $1=a+1\therefore a=0$.
>
> **8.** $[0,\infty)$.
>
> **9.** No (laterales $\pm1$).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Evalúo eligiendo el tramo correcto.
> - [ ] Escribo $|x|$ y $\text{sgn}$ por tramos.
> - [ ] Dibujo ○/● en fronteras.
> - [ ] Calculo pisos positivos y negativos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Verifico continuidad con límites laterales.
> - [ ] Hallo rangos uniendo tramos.
> - [ ] Traslado valores absolutos.
> - [ ] Sumo funciones tramo a tramo.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Ajusto parámetros para continuidad.
> - [ ] Compongo con ceros múltiples.
> - [ ] Decido derivabilidad en fronteras.
> - [ ] Modelo tarifas por tramos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 2 (tramos).
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. de funciones.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Definición, dominio y rango]] — base: dominio y rango.
> - [[06 - Funciones Especiales]] — $|x|$, $\text{sgn}$, piso.
> - [[02 - Representación gráfica]] — ○/● y saltos.
> - [[09 - Valor Absoluto]] — ecuaciones con $|x|$.

---

**Tags:** #funciones #tramos #continuidad #unidad3

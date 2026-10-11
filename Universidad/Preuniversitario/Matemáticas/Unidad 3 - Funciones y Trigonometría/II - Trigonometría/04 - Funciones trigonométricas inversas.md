---
dg-publish: true
---

# 🔙 Trigonométricas Inversas

## 🎯 Introducción

> [!info] 💡 ¿Qué son $\arcsin,\arccos,\arctan$?
>
> Las inversas con dominio restringido ($\arcsin:[-1,1]\to[-\pi/2,\pi/2]$): devuelven **el** ángulo principal. $\arcsin(\sin\theta)=\theta$ solo si $\theta$ ya está en el rango.
>
> ```mermaid
> graph LR
>     A["Restringe<br/>dominio"] --> B["Invierte<br/>arcsin"]
>     B --> C["Rango<br/>principal"]
>     C --> D["Reduce<br/>al rango"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Rangos y relaciones
>
> **$\arcsin$:** $[-1,1]\to[-\pi/2,\pi/2]$. **$\arccos$:** $[-1,1]\to[0,\pi]$. **$\arctan$:** $\mathbb{R}\to(-\pi/2,\pi/2)$.
>
> **Claves:** $\arcsin x+\arccos x=\pi/2$; $\sin(\arccos(3/5))=4/5$ (triángulo $3$-$4$-$5$).

> [!tip] 💡 Cómo evaluar inversas sin equivocarse
>
> Primero pregunta si el argumento está en el rango principal — si no ($\sin(5\pi/6)$), reduce al ángulo coterminal dentro del rango ($5\pi/6\to\pi/6$). Para composiciones como $\sin(\arccos x)$, dibuja el triángulo con el dato y lee el otro cateto.

> [!example] 🟢 Ejemplo — $\arcsin(\sin(5\pi/6))$
>
> $5\pi/6\notin[-\pi/2,\pi/2]$; $\sin(5\pi/6)=1/2\therefore$ respuesta $\pi/6$ (verifica $\sin(\pi/6)=1/2$ ✓).

---

## 📋 Tabla Comparativa: Las Tres Inversas

> [!note] 📋 Qué dominio y rango tiene cada una
>
> | Función | Dominio | Rango | Ejemplo |
> |---|---|---|---|
> | $\arcsin$ | $[-1,1]$ | $[-\pi/2,\pi/2]$ | $\arcsin(1/2)=\pi/6$ |
> | $\arccos$ | $[-1,1]$ | $[0,\pi]$ | $\arccos(-1/2)=2\pi/3$ |
> | $\arctan$ | $\mathbb{R}$ | $(-\pi/2,\pi/2)$ | $\arctan(1)=\pi/4$ |
>
> **Suma:** $\arctan1+\arctan2+\arctan3=\pi/4+3\pi/4=\pi$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\arcsin(\sin\theta)=\theta$ siempre:** solo en el rango principal.
> - **$\arcsin$ con $|x|>1$:** fuera del dominio (no existe real).
> - **Rangos cruzados:** $\arcsin$ llega a $\pm\pi/2$; $\arccos$ a $0,\pi$.
> - **$\arctan$ acotada:** nunca llega a $\pm\pi/2$ (asíntotas).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $\arcsin(1/2)$, $\arccos(0)$, $\arctan(1)$.
> 2. $\arcsin(-1/2)$, $\arccos(-1/2)$.
> 3. $\arcsin(1)+\arccos(1)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\pi/6,\pi/2,\pi/4$.
>
> **2.** $-\pi/6,2\pi/3$.
>
> **3.** $\pi/2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $\arcsin(\sin(5\pi/6))$.
> 5. $\sin(\arccos(3/5))$.
> 6. Prueba $\arcsin x+\arccos x=\pi/2$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\pi/6$ (reduce al rango).
>
> **5.** $4/5$ (triángulo $3$-$4$-$5$).
>
> **6.** Complementarios a $\pi/2$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Resuelve $\arcsin x=\arccos x$.
> 8. $\sin(2\arcsin(1/2))$.
> 9. Prueba $\arctan x+\arctan(1/x)=\pi/2$ ($x>0$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $x=\sqrt2/2$ (ángulo $\pi/4$).
>
> **8.** $\sin(\pi/3)=\sqrt3/2$.
>
> **9.** Complementarios ($x,1/x$ recíprocos).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Evalúo $\arcsin,\arccos,\arctan$ notables.
> - [ ] Recito dominios y rangos.
> - [ ] Simplifico $f(f^{-1}(x))=x$.
> - [ ] Sumo complementarios a $\pi/2$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Reduzco al rango principal.
> - [ ] Resuelvo $\sin(\arccos x)$ con triángulos.
> - [ ] Pruebo $\arcsin+\arccos=\pi/2$.
> - [ ] Sumo $\arctan$ con tangente.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Convierto $\arcsin$ a $\arctan$ con triángulo.
> - [ ] Derivo $(\arcsin x)'=1/\sqrt{1-x^2}$.
> - [ ] Resuelvo ecuaciones $\arcsin=\arccos$.
> - [ ] Demuestro sumas recíprocas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 5 (inversas trig).
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. de trigonometría.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[10 - Función inversa de una función biyectiva]] — inversas generales.
> - [[02 - Funciones trigonométricas elementales]] — base: valores.
> - [[06 - Ecuaciones e inecuaciones trigonométricas]] — siguiente: ecuaciones.
> - [[04 - Tipos de funciones]] — biyectividad para invertir.

---

**Tags:** #trigonometria #inversas #arcsin #unidad3

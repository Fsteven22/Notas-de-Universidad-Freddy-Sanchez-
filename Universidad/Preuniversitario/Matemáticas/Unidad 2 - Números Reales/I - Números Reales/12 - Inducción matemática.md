---
dg-publish: true
---

# 🪜 Inducción Matemática

## 🎯 Introducción

> [!info] 💡 ¿Qué es la inducción?
>
> Domino infinito: base $P(1)$ + paso $P(k)\to P(k+1)$ tumba todo $\mathbb{N}$. Sirve para sumas ($n(n+1)/2$), divisibilidad ($4^n-1$ por $3$) y desigualdades ($2^n<n!$ desde $n=4$).
>
> ```mermaid
> graph LR
>     A["Base<br/>P(1)"] --> B["Hipótesis<br/>P(k)"]
>     B --> C["Paso<br/>P(k+1)"]
>     C --> D["Todo N<br/>cae"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Principio y fuerte
>
> **Simple:** $P(1)$ cierto y $P(k)\implies P(k+1)\therefore\forall n\,P(n)$. **Fuerte:** usa $P(1),\dots,P(k)$ (primos, Fibonacci).
>
> **Esquema:** base numérica + álgebra del paso (factoriza $(k+1)$, suma el término nuevo).

> [!tip] 💡 Cómo armar el paso sin trabarse
>
> Escribe $P(k+1)$ primero (la meta) y transforma la hipótesis hasta llegar ahí: en sumas suma el término $(k+1)$ a ambos lados; en divisibilidad reescribe $4^{k+1}-1=4(4^k-1)+3$; en desigualdades acota ($2<k+1$ si $k\ge4$).

> [!example] 🟢 Ejemplo — $1^2+\cdots+n^2=n(n+1)(2n+1)/6$
>
> Base $1=1$ ✓. Paso: suma $(k+1)^2$ a la hipótesis y factoriza $(k+1)$: queda $(k+1)(k+2)(2k+3)/6=P(k+1)$ ✓.

---

## 📋 Tabla Comparativa: Tipos de Prueba

> [!note] 📋 Qué inducción usar y cuándo
>
> | Proposición | Tipo | Paso clave |
> |---|---|---|
> | Suma cerrada | Simple | Suma el término $(k+1)$ |
> | Divisibilidad | Simple | Reescribe ($4(4^k-1)+3$) |
> | Desigualdad | Simple ($n\ge n_0$) | Acota ($2<k+1$) |
> | Producto de primos | Fuerte | $k+1$ primo o $ab$ |
> | Fibonacci $F_n<2^n$ | Fuerte | Usa $F_k,F_{k-1}$ |
>
> **Recurrencia:** Hanói $H_{n+1}=2H_n+1\therefore H_n=2^n-1$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Sin base:** el paso solo encadena, no arranca (caballos del mismo color falla en $k=1$).
> - **Base en $n=1$ con $n\ge4$:** $2^n<n!$ arranca en $16<24$.
> - **Paso sin usar hipótesis:** debe aparecer $P(k)$ en la cuenta.
> - **Simple donde pide fuerte:** primos necesitan todos los anteriores.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $1+\cdots+n=n(n+1)/2$ (base + paso).
> 2. $4^n-1$ divisible por $3$.
> 3. $2^n<n!$ base en $n=4$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Base $1$; suma $(k+1)$ y factoriza.
>
> **2.** Base $3$; $4(4^k-1)+3$.
>
> **3.** $16<24$ ✓.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Completa el paso de $\sum i^2$.
> 5. $2^n<n!$ paso ($n\ge4$).
> 6. $n^3-n$ divisible por $3$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(k+1)(k+2)(2k+3)/6$.
>
> **5.** $2^{k+1}<2k!<(k+1)!$ ($2<k+1$).
>
> **6.** $k^3-k+3k(k+1)$ (múltiplo de $3$).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Bernoulli $(1+x)^n\ge1+nx$ ($x>-1$).
> 8. Hanói: $2^n-1$ movimientos mínimos.
> 9. Falla "caballos mismo color" en $k=1$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(1+kx)(1+x)\ge1+(k+1)x$ (pues $kx^2\ge0$).
>
> **8.** Base $1$; $2(2^k-1)+1$.
>
> **9.** Conjuntos de $1$ no se solapan.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico bases numéricas.
> - [ ] Planteo hipótesis $P(k)$.
> - [ ] Sumo el término nuevo.
> - [ ] Pruebo divisibilidad simple.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Completo pasos algebraicos.
> - [ ] Acoto en desigualdades.
> - [ ] Reescribo $a^{k+1}-1$ con hipótesis.
> - [ ] Sumo cubos con fórmula.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Elijo fuerte cuando pide.
> - [ ] Demuestro Bernoulli.
> - [ ] Analizo recurrencias (Hanói).
> - [ ] Detecto inducciones falsas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §5.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. de inducción.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[07 - Demostraciones]] — métodos de prueba.
> - [[15 - Sucesiones]] — recurrencias como Hanói.
> - [[13 - Técnicas de conteo]] — Bernoulli como caso.
> - [[11 - Funciones polinomiales]] — fórmulas de sumas.

---

**Tags:** #números-reales #inducción #demostración #unidad2

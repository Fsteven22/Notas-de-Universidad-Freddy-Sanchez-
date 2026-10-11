---
dg-publish: true
---

# 🔄 Función Inversa

## 🎯 Introducción

> [!info] 💡 ¿Qué es la función inversa?
>
> Si $f$ es biyectiva, $f^{-1}$ deshace: $f^{-1}(f(x))=x$. Se halla despejando $x$ ($y=3x-2\therefore x=(y+2)/3$) y su gráfica es el reflejo en $y=x$.
>
> ```mermaid
> graph LR
>     A["x<br/>entrada"] --> B["f<br/>biyectiva"]
>     B --> C["y<br/>salida"]
>     C --> D["f-1<br/>deshace"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Biyectividad e inversa
>
> **Biyectiva:** inyectiva + sobreyectiva (horizontal corta exactamente 1 vez). **Inversa:** $f^{-1}(f(x))=x$, $f(f^{-1}(y))=y$.
>
> **Método:** escribe $y=f(x)$, despeja $x$, intercambia. **Dominios:** $\text{Dom}(f^{-1})=\text{Ran}(f)$ y viceversa.

> [!tip] 💡 Cómo hallar inversas sin perderse
>
> Despeja con calma paso a paso y verifica componiendo — si no da $x$, el despeje falló. Si no es biyectiva, restringe el dominio por el vértice o monotonía antes de invertir ($x^2$ necesita $[0,\infty)$).

> [!example] 🟢 Ejemplo — $f(x)=(2x+1)/(x-1)$
>
> $y(x-1)=2x+1\therefore x(y-2)=y+1\therefore x=(y+1)/(y-2)$. $f^{-1}(x)=(x+1)/(x-2)$ (verifica $f(f^{-1}(0))=f(-1/2)=0$ ✓).

---

## 📋 Tabla Comparativa: Inversas Típicas

> [!note] 📋 Qué inversa tiene cada función
>
> | $f$ | $f^{-1}$ | Condición |
> |---|---|---|
> | $3x-2$ | $(x+2)/3$ | Biyectiva |
> | $x^3$ | $\sqrt[3]{x}$ | Biyectiva |
> | $x^2$ | $\sqrt{x}$ | Restringe $[0,\infty)$ |
> | $\sqrt{x-1}$ | $x^2+1$ ($x\ge0$) | $\text{Dom}(f^{-1})=[1,\infty)$ |
> | $e^x$ | $\ln x$ | Intercambia dominios |
> | $(ax+b)/(cx+d)$ | $(-dx+b)/(cx-a)$ | $ad-bc\neq0$ |
>
> **Composición:** $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$ (orden invertido).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Invertir $x^2$ en $\mathbb{R}$:** no es inyectiva; restringe primero.
> - **$f^{-1}=1/f$:** la inversa deshace, no divide.
> - **Dominios sin intercambiar:** $\text{Dom}(f^{-1})=\text{Ran}(f)$.
> - **$(g\circ f)^{-1}=g^{-1}\circ f^{-1}$:** el orden se **invierte**.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $f(x)=3x-2$: $f^{-1}$ y verificación.
> 2. ¿Biyectiva? $2x+1$, $x^2$ ($\mathbb{R}$), $x^3$.
> 3. Grafica $x+1$ y su inversa.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(x+2)/3$; $f(f^{-1}(x))=x$.
>
> **2.** Sí; no; sí.
>
> **3.** Simétricas en $y=x$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $f=(2x+1)/(x-1)$: inversa completa.
> 5. Restringe $x^2-4x+3$ para invertir.
> 6. $f=\sqrt{x-1}$: $f^{-1}$ y dominios.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(x+1)/(x-2)$.
>
> **5.** $[2,\infty)$ o $(-\infty,2]$ (vértice $x=2$).
>
> **6.** $x^2+1$ ($x\ge0$); $\text{Dom}(f^{-1})=[1,\infty)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $x^3+2x+1$ biyectiva sin fórmula cerrada.
> 8. $(ax+b)/(cx+d)$: inversa y condición.
> 9. $f(x)=1-x$ iterada ($f^{-1}=f$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $f'=3x^2+2>0$ (monótona).
>
> **8.** $(-dx+b)/(cx-a)$; $ad-bc\neq0$.
>
> **9.** Involución: $1-(1-x)=x$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Despejo $x$ para hallar $f^{-1}$.
> - [ ] Verifico componiendo ($=x$).
> - [ ] Decido biyectividad con horizontal.
> - [ ] Reflejo gráficas en $y=x$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Invierto racionales despejando.
> - [ ] Restringo por vértice/monotonía.
> - [ ] Intercambio dominios y rangos.
> - [ ] Invierto composiciones en orden.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Pruebo biyectividad con derivada.
> - [ ] Invierto Möbius con determinante.
> - [ ] Demuestro $(f^{-1})^{-1}=f$.
> - [ ] Detecto involuciones.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 2 (inversas).
>
> [2] K. Rosen, *Matemática Discreta*, McGraw-Hill — §2.3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Tipos de funciones]] — biyectividad base.
> - [[09 - Operaciones con funciones de variable real]] — $(f\circ g)^{-1}$.
> - [[04 - Funciones trigonométricas inversas]] — $\arcsin$ restringido.
> - [[13 - Funciones exponenciales]] — inversa de $e^x$.

---

**Tags:** #funciones #inversa #biyectiva #unidad3

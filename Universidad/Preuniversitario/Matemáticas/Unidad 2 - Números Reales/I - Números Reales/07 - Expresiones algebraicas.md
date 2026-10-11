---
dg-publish: true
---

# 🧩 Expresiones Algebraicas

## 🎯 Introducción

> [!info] 💡 ¿Qué es una expresión algebraica?
>
> Letras + números + operaciones: monomios se suman por semejanza, notables se expanden de memoria ($(x+3)^2=x^2+6x+9$) y factorizar es el camino inverso — siempre con el dominio anotado al cancelar.
>
> ```mermaid
> graph LR
>     A["Monomios<br/>semejantes"] --> B["Notables<br/>expande"]
>     B --> C["Factoriza<br/>invierte"]
>     C --> D["Simplifica<br/>dominio"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Términos, notables y factorización
>
> **Término:** $ax^n$; **semejantes:** mismo literal y exponente ($3x^2+5x^2=8x^2$).
>
> **Notables:** $(a\pm b)^2=a^2\pm2ab+b^2$, $(a+b)(a-b)=a^2-b^2$, $(a\pm b)^3$, suma/diferencia de cubos.
>
> **Factorizar:** factor común, trinomio, diferencia de cuadrados/cubos, Ruffini.

> [!tip] 💡 Cómo factorizar en orden
>
> Saca factor común primero (el error es empezar por el trinomio con factor dentro). Luego prueba notables: ¿dos cuadrados restando? ¿trinomio cuadrado perfecto ($x^2\pm6x+9$)? Si nada calza, Ruffini con divisores del independiente.

> [!example] 🟢 Ejemplo — $\frac{x^2-x-6}{x^2-4}$ simplificada
>
> $(x-3)(x+2)/(x-2)(x+2)=(x-3)/(x-2)$ con $x\neq\pm2$ (el $-2$ cancelado sigue prohibido ✓).

---

## 📋 Tabla Comparativa: Notables

> [!note] 📋 Qué patrón usar y cuándo
>
> | Patrón | Expansión | Ejemplo |
> |---|---|---|
> | $(a+b)^2$ | $a^2+2ab+b^2$ | $(x+3)^2=x^2+6x+9$ |
> | $(a-b)^2$ | $a^2-2ab+b^2$ | $(2a-5)^2=4a^2-20a+25$ |
> | $(a+b)(a-b)$ | $a^2-b^2$ | $x^2-25=(x+5)(x-5)$ |
> | $a^3-b^3$ | $(a-b)(a^2+ab+b^2)$ | $x^3-8=(x-2)(\ldots)$ |
> | $a^3+b^3$ | $(a+b)(a^2-ab+b^2)$ | Verifica multiplicando |
>
> **Cuarta:** $(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4$ (Pascal $1$-$4$-$6$-$4$-$1$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$(x+3)^2=x^2+9$:** falta $6x$.
> - **Cancelar sin dominio:** $(x^2-4)/(x-2)=x+2$ solo si $x\neq2$.
> - **Factor común olvidado:** $6x^2+9x=3x(2x+3)$ antes del trinomio.
> - **$x^2+kx+9$ perfecto con $k=6$:** también $k=-6$ ($(x-3)^2$).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Suma: $3x^2+5x^2$, $7xy-2xy+4$.
> 2. Expande: $(x+3)^2$, $(2a-5)^2$, $(x+4)(x-4)$.
> 3. Factoriza: $6x^2+9x$, $x^2+5x+6$, $x^2-25$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $8x^2$; $5xy+4$.
>
> **2.** $x^2+6x+9$; $4a^2-20a+25$; $x^2-16$.
>
> **3.** $3x(2x+3)$; $(x+2)(x+3)$; $(x+5)(x-5)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Factoriza $2x^2+7x+3$ y $x^3-8$.
> 5. Simplifica $(x^2-x-6)/(x^2-4)$ con dominio.
> 6. Ruffini: $x^3-2x^2-x+2$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(2x+1)(x+3)$; $(x-2)(x^2+2x+4)$.
>
> **5.** $(x-3)/(x-2)$; $x\neq\pm2$.
>
> **6.** $(x-1)(x-2)(x+1)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $(a+b)^4$ por binomio.
> 8. Factoriza $x^4-5x^2+4$.
> 9. Halla $k$ con $x^2+kx+9$ cuadrado perfecto.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $a^4+4a^3b+6a^2b^2+4ab^3+b^4$.
>
> **8.** $(x-1)(x+1)(x-2)(x+2)$.
>
> **9.** $k=\pm6$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Sumo semejantes sin mezclar.
> - [ ] Expando tres notables de memoria.
> - [ ] Factorizo comunes y trinomios.
> - [ ] Evalúo polinomios en puntos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Factorizo cubos y bicuadráticas.
> - [ ] Simplifico con dominio anotado.
> - [ ] Aplico Ruffini completo.
> - [ ] Pruebo identidades expandiendo.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Expando $(a+b)^4$ con Pascal.
> - [ ] Demuestro suma de cubos.
> - [ ] Hallo $k$ de cuadrados perfectos.
> - [ ] Verifico multiplicando factores.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de notables.
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. 1.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[11 - Funciones polinomiales]] — polinomios como funciones.
> - [[13 - Técnicas de conteo]] — $(a+b)^n$ general.
> - [[12 - Funciones racionales]] — simplificar $P/Q$.
> - [[10 - Ecuaciones]] — factorizar para resolver.

---

**Tags:** #números-reales #álgebra #notables #unidad2

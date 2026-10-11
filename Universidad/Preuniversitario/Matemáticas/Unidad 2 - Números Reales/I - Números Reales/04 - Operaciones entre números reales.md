---
dg-publish: true
---

# 🧮 Operaciones entre Reales

## 🎯 Introducción

> [!info] 💡 ¿Cómo se opera con reales?
>
> Suma/resta por signos, producto/cociente por fracciones, PEMDAS para el orden, y potencias/radicales con sus leyes: extraer factores ($\sqrt{75}=5\sqrt3$) y racionalizar dejan todo exacto.
>
> ```mermaid
> graph LR
>     A["+ -<br/>signos"] --> B["x /<br/>fracciones"]
>     B --> C["PEMDAS<br/>orden"]
>     C --> D["Pot/rad<br/>leyes"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U2-operaciones.png]]

> [!tip] 💡 Visual — Operaciones y signos
>
> La recta muestra dónde cae cada resultado: $5+3\times2-4=7$ (no $12$), y $(-3)(-4)=+12$ confirma la regla de signos.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Las cuatro, orden y leyes
>
> **Suma/resta:** signos iguales suman, distintos restan. **Producto/cociente:** $(a/b)(c/d)=ac/bd$; $(a/b)/(c/d)=ad/bc$.
>
> **PEMDAS:** paréntesis, exponentes, $\times\div$, $+,-$. **Leyes:** $a^ma^n=a^{m+n}$, $\sqrt{ab}=\sqrt a\sqrt b$, $(a+b)^2=a^2+2ab+b^2$.

> [!tip] 💡 Cómo operar sin errores de orden
>
> Marca las multiplicaciones y potencias antes de sumar — el $90\%$ de errores es sumar antes de multiplicar. En fracciones compuestas trabaja de adentro hacia afuera, y en radicales extrae cuadrados perfectos primero ($\sqrt{75}=5\sqrt3$ directo).

> [!example] 🟢 Ejemplo — $(2/5)/(3/7)$ y $2\sqrt{12}+3\sqrt{27}$
>
> $(2\cdot7)/(5\cdot3)=14/15$. $2(2\sqrt3)+3(3\sqrt3)=4\sqrt3+9\sqrt3=13\sqrt3$.

---

## 📋 Tabla Comparativa: Leyes

> [!note] 📋 Qué ley usar y cuándo
>
> | Situación | Ley | Ejemplo |
> |---|---|---|
> | Potencias misma base | Suma exponentes | $2^5\cdot2^3=256$ |
> | Potencia de potencia | Multiplica | $(3^2)^3=729$ |
> | Raíz de producto | Separa | $\sqrt2\cdot\sqrt8=4$ |
> | Conjugado | $(a-b)(a+b)$ | $2/(3-\sqrt2)=2(3+\sqrt2)/7$ |
> | Cuadrado de suma | $(a+b)^2$ | $(x+3)^2=x^2+6x+9$ |
>
> **Iterada:** $1/(1+1/(1+1/(1+x)))=(2+x)/(3+2x)$ (de adentro afuera).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$5+3\times2=16$:** es $11$ ($\times$ primero).
> - **$(a+b)^2=a^2+b^2$:** falta $2ab$.
> - **$6/\sqrt3=6\sqrt3/3$ sin simplificar:** es $2\sqrt3$.
> - **Signos en resta:** $7-(-3)=10$ (doble negativo suma).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $5+3\times2-4$, $(5+3)(2-4)$, $12\div3+4\times2$.
> 2. $2/3+1/4$, $3/5-1/3$, $(2/5)/(3/7)$.
> 3. $(-5)+(-3)$, $(-7)-(-4)$, $(-3)(-4)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $7$; $-16$; $12$.
>
> **2.** $11/12$; $4/15$; $14/15$.
>
> **3.** $-8$; $-3$; $12$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $\sqrt{75}$, $2\sqrt{12}+3\sqrt{27}$, $\sqrt2\cdot\sqrt8$.
> 5. Racionaliza $1/\sqrt7$, $2/(3-\sqrt2)$.
> 6. $(x+3)^2$, $(2a-5)^2$, $(x+4)(x-4)$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $5\sqrt3$; $13\sqrt3$; $4$.
>
> **5.** $\sqrt7/7$; $2(3+\sqrt2)/7$.
>
> **6.** $x^2+6x+9$; $4a^2-20a+25$; $x^2-16$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $[((2^3\cdot2^{-1})^2)/2^4]^3$.
> 8. Lado del cuadrado de área $50$.
> 9. Simplifica $1/(1+1/(1+1/(1+x)))$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $1$ ($2^{4-4}$ al cubo).
>
> **8.** $5\sqrt2$.
>
> **9.** $(2+x)/(3+2x)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico PEMDAS sin fallar.
> - [ ] Sumo y multiplico fracciones.
> - [ ] Manejo signos en las cuatro.
> - [ ] Resto con doble negativo.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Extraigo factores de radicales.
> - [ ] Racionalizo con conjugados.
> - [ ] Expando productos notables.
> - [ ] Opero potencias con leyes.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Simplifico fracciones iteradas.
> - [ ] Expando $(a+b)^3$ completo.
> - [ ] Pruebo distributivas con cocientes.
> - [ ] Verifico con factorización.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Aritmética*, Patria — cap. de operaciones.
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. 1.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Operaciones binarias]] — estructura abstracta.
> - [[07 - Expresiones algebraicas]] — notables a fondo.
> - [[09 - Valor Absoluto]] — signos y distancias.
> - [[10 - Ecuaciones]] — despejes con operaciones.

---

**Tags:** #números-reales #operaciones #pemdas #unidad2

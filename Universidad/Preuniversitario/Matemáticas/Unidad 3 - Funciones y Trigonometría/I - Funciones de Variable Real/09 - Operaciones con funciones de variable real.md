---
dg-publish: true
---

# ➕ Operaciones con Funciones

## 🎯 Introducción

> [!info] 💡 ¿Cómo se combinan funciones?
>
> Punto a punto ($f+g$, $fg$, $f/g$ con dominio intersección) y por **composición** $(g\circ f)(x)=g(f(x))$ (de adentro hacia afuera): el orden importa y el dominio se restringe dos veces.
>
> ```mermaid
> graph LR
>     A["f,g<br/>punto a punto"] --> B["Compón<br/>g(f(x))"]
>     B --> C["Dominio<br/>doble filtro"]
>     C --> D["Inversa<br/>deshace"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Aritmética y composición
>
> **Aritmética:** $(f\pm g)(x)$, $(fg)(x)$, $(f/g)(x)$ con $\text{Dom}=\text{Dom}(f)\cap\text{Dom}(g)$ ($g\neq0$ en cociente).
>
> **Composición:** $(g\circ f)(x)=g(f(x))$ con $\text{Dom}=\{x\in\text{Dom}(f):f(x)\in\text{Dom}(g)\}$. **Inversa:** $(f\circ g)(x)=x\iff g=f^{-1}$.

> [!tip] 💡 Cómo componer sin equivocarse
>
> Trabaja de adentro hacia afuera escribiendo cada capa: $f(1)=1$, luego $g(1)=3$ — no intentes hacerlo mental de un paso. El dominio filtra dos veces (entrada de $f$ y salida hacia $g$); en cocientes filtra una tercera ($g\neq0$).

> [!example] 🟢 Ejemplo — $f=x^2$, $g=2x+1$
>
> $(f+g)(2)=4+5=9$; $(fg)(1)=3$; $(g\circ f)(1)=g(1)=3$ pero $(f\circ g)(1)=f(3)=9$ (el orden cambia todo ✓).

---

## 📋 Tabla Comparativa: Operaciones

> [!note] 📋 Qué dominio resulta y cuándo
>
> | Operación | Regla | Dominio |
> |---|---|---|
> | $f+g$, $fg$ | Punto a punto | Intersección |
> | $f/g$ | Punto a punto | Intersección menos ceros de $g$ |
> | $g\circ f$ | Adentro hacia afuera | Doble filtro |
> | $f^{-1}$ | Deshace $f$ | Rango de $f$ |
>
> **Iterada:** $f(x)=2x+1\therefore f^n(x)=2^nx+2^n-1$ (por inducción).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$g\circ f=f\circ g$:** $3\neq9$ en el ejemplo — el orden manda.
> - **Dominio simple en compuesta:** $\sqrt{x^2-4}$ exige $|x|\ge2$ (filtro de $g$).
> - **$(f+g)^2=f^2+g^2$:** falta $2fg$.
> - **Ceros del denominador olvidados:** $f/g$ excluye $g=0$ siempre.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $f=x^2$, $g=2x+1$: $(f+g)(2)$, $(fg)(1)$, $(f/g)(0)$.
> 2. $(g\circ f)(1)$ y $(f\circ g)(1)$.
> 3. Descompón $\sqrt{x^2+1}$ en $g\circ f$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $9$; $3$; $0$.
>
> **2.** $3$; $9$ (orden distinto).
>
> **3.** $f=x^2+1$, $g=\sqrt{\cdot}$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $\text{Dom}$ de $\sqrt{\cdot}\circ(x^2-4)$.
> 5. $f=1/x$, $g=x+1$: $f\circ g$, $g\circ f$ y dominios.
> 6. $h=|x^2-1|$ como $g\circ f$ (dos formas).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $|x|\ge2$.
>
> **5.** $1/(x+1)$ ($x\neq-1$); $1/x+1$ ($x\neq0$).
>
> **6.** $|\cdot|\circ(x^2-1)$; $|\cdot-1|\circ x^2$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $(f\circ g)^{-1}=g^{-1}\circ f^{-1}$.
> 8. $\text{Dom}(\ln\circ(x^2-1))$.
> 9. Prueba $g\circ f$ inyectiva si $f,g$ lo son.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Aplica a $y$ y usa unicidad (orden invertido).
>
> **8.** $|x|>1$.
>
> **9.** $g(f(a_1))=g(f(a_2))\therefore a_1=a_2$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Opero $+,-,\times,\div$ punto a punto.
> - [ ] Compongo de adentro hacia afuera.
> - [ ] Hallo dominios de cocientes.
> - [ ] Descompongo en $g\circ f$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Filtro dominios dos veces.
> - [ ] Comparo $f\circ g$ vs $g\circ f$.
> - [ ] Invierto composiciones biyectivas.
> - [ ] Distingo $(f+g)^2$ de $f^2+g^2$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Itero composiciones ($f^n$).
> - [ ] Demuestro inyectividad compuesta.
> - [ ] Descompongo trascendentes ($\sin(x^2)$).
> - [ ] Caracterizo inversas por identidad.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 2 (composición).
>
> [2] K. Rosen, *Matemática Discreta*, McGraw-Hill — §2.3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Definición, dominio y rango]] — base: dominios.
> - [[10 - Función inversa de una función biyectiva]] — inversas a fondo.
> - [[04 - Tipos de funciones]] — inyectiva para invertir.
> - [[11 - Inecuaciones]] — dominios con desigualdades.

---

**Tags:** #funciones #composicion #operaciones #unidad3

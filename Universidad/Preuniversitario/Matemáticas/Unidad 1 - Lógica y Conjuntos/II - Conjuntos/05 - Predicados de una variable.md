---
dg-publish: true
---

# 📌 Predicados

## 🎯 Introducción

> [!info] 💡 ¿Qué es un predicado?
>
> Plantilla con huecos ($P(x)$, $P(x,y)$) que al sustituir da proposición. Su conjunto de verdad traduce conectivos a operaciones, y cuantificar ($\forall x\exists y$) cierra los huecos — con el orden de $\forall$/$\exists$ cambiando el valor.
>
> ```mermaid
> graph LR
>     A["P(x,y)<br/>plantilla"] --> B["Verdad<br/>V_P"]
>     B --> C["Cuantifica<br/>todo/alguno"]
>     C --> D["Orden<br/>importa"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Predicado, verdad y cuantificación
>
> **Predicado:** $P(x)$ o $P(x,y)$ en un dominio (sin valor hasta sustituir, porque el hueco deja el valor abierto).
>
> **Verdad:** $V_P=\{x:P(x)\text{ V}\}$ (o pares en $P(x,y)$); por eso los conectivos se vuelven operaciones: $V_{P\land Q}=V_P\cap V_Q$ (pide ambas, como $\cap$ pide ambos).
>
> **Cuantificar** cierra todos los huecos y produce proposición; **mixtos** dependen del orden ($\forall x\exists y$ deja elegir $y$ según $x$; $\exists y\forall x$ exige un $y$ único para todos).

> [!tip] 💡 Cómo trabajar con $V_P$ y mixtos
>
> Convierte todo a conjuntos primero: $P\to Q$ falla solo donde $P$ vale y $Q$ no, de ahí $V_{P\to Q}=V_P^c\cup V_Q$. En mixtos lee de afuera adentro preguntando "¿puede depender?": $x+y=0$ con $\forall x\exists y$ sí ($y=-x$); con $\exists y\forall x$ no (ningún $y$ sirve a todo $x$).

> [!example] 🟢 Ejemplo — $V_P=\{1,3\}$, $V_Q=\{2,3\}$ en $U=\{1,2,3\}$
>
> $V_{P\lor Q}=\{1,2,3\}$ (unión: basta que una valga). $V_{P\to Q}$: $x=1\to F$ (V$\to$F), $x=2,3\to V\therefore\{2,3\}$.

> [!example] 🟢 Ejemplo — "$x\le y$" en $U=\{1,2\}$
>
> $\forall x\exists y$: V ($1\to1$, $2\to2$). $\exists y\forall x$: F (ningún $y$ es $\ge$ ambos) — el orden decide.

---

## 📋 Tabla Comparativa: Conectivo, Cuantificador y Orden

> [!note] 📋 Qué operación y valor corresponde
>
> | Conectivo | Operación (por qué) | Ejemplo |
> |---|---|---|
> | $\lnot P$ | Complemento (niega la pertenencia) | $V_P=\{2,4\}\to\{1,3\}$ |
> | $P\land Q$ | Intersección (exige ambas) | $\{0,2,4\}\cap\{0..5\}$ |
> | $P\to Q$ | $V_P^c\cup V_Q$ (solo falla V$\to$F) | $\{2,3\}$ arriba |
> | $\forall$/$\exists$ | $V_P=U$ / $V_P\neq\emptyset$ | Testigo vs contraejemplo |
>
> | Orden mixto | Valor en $\{1,2\}$ (por qué) | Regla |
> |---|---|---|
> | $\forall x\exists y\,(x\le y)$ | V ($y$ depende de $x$) | $\exists\forall\to\forall\exists$ vale |
> | $\exists y\forall x\,(x\le y)$ | F (sin $y$ universal) | Al revés no ($y>x$ refuta) |
>
> **Negar** intercambia cada cuantificador ($\lnot\forall x\exists y\equiv\exists x\forall y\lnot$) porque negar "todos" es "alguno no".

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$V_{P\to Q}=V_P-V_Q$:** es $V_P^c\cup V_Q$ (falla solo V$\to$F).
> - **$\forall$ con un testigo:** un ejemplo prueba $\exists$, no $\forall$ (para $\forall$ hay que argumentar general).
> - **Órdenes iguales:** $\forall x\exists y\neq\exists y\forall x$ (dependencia vs unicidad).
> - **Ejemplos fuera del dominio:** en $\{2,4,6\}$ el F es $(6,4)$, no $(2,3)$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $U=\{1..5\}$, $P$ par: $\forall xP$, $\exists xP$, $\exists x(P\land x>3)$.
> 2. "$x+y=10$" en $\mathbb{N}$: $P(3,7)$, $P(2,5)$.
> 3. "$x\mid y$" en $\{2,4,6\}$: dos V y un F.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** F ($1$ impar); V ($2$); V ($4$).
>
> **2.** V; F.
>
> **3.** $(2,4)$, $(2,6)$ V; $(6,4)$ F.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $P(x)$:"$x>2$" en $\{1,2,3\}$: $V_P$, $\forall$, $\exists$.
> 5. Niega $\forall x\exists y\,(x<y)$.
> 6. Formaliza "cada estudiante tiene un tutor".

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\{3\}$; F; V.
>
> **5.** $\exists x\forall y\,(x\ge y)$.
>
> **6.** $\forall x(Est\to\exists y(Tut\land Tutoriza))$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. "Exactamente un padre biológico" formalizado.
> 8. $y=x^2$: ¿$\forall x\exists y$? ¿$\exists y\forall x$?
> 9. Prueba $V_{P\leftrightarrow Q}=(V_P\cap V_Q)\cup(V_P^c\cap V_Q^c)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\forall x\exists y(Padre\land\forall z(Padre\to z=y))$.
>
> **8.** V ($y$ depende); F (sin $y$ único).
>
> **9.** Casos $x\in V_P$ sí/no (coinciden $\iff$ mismo lado).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Evalúo $P(a)$ y $P(a,b)$ sustituyendo.
> - [ ] Hallo $V_P$ y $V_R$ en finitos.
> - [ ] Decido $\forall$/$\exists$ con testigo/contraejemplo.
> - [ ] Uso pares dentro del dominio.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Opero $V_P,V_Q$ con $\cap,\cup,^c$.
> - [ ] Calculo $V_{P\to Q}$ por el fallo V$\to$F.
> - [ ] Niego mixtos intercambiando.
> - [ ] Formalizo "cada... tiene un...".

> [!note] 📋 Nivel Avanzado
>
> - [ ] Formalizo unicidad ("exactamente uno").
> - [ ] Pruebo $\exists\forall\to\forall\exists$ y refuto el recíproco.
> - [ ] Defino inyectividad con $\forall x_1,x_2$.
> - [ ] Pruebo igualdades de $V$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §1.4.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 2.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Cuantificadores]] — base: $\forall,\exists$.
> - [[07 - Pares ordenados y producto cartesiano]] — $V_P\subseteq\times$.
> - [[09 - Relaciones]] — siguiente: relaciones.
> - [[10 - Funciones en Conjuntos]] — inyectividad formal.

---

**Tags:** #lógica #predicados #cuantificadores #unidad1

---
dg-publish: true
---

# 📦 Pares y Producto Cartesiano

## 🎯 Introducción

> [!info] 💡 ¿Qué es $A\times B$?
>
> Todos los pares $(a,b)$ con $a\in A$, $b\in B$: el orden importa ($(2,3)\neq(3,2)$), $|A\times B|=|A||B|$, y un factor vacío anula todo. Relaciones y funciones son subconjuntos de productos.
>
> ```mermaid
> graph LR
>     A["A x B<br/>pares"] --> B["Orden<br/>importa"]
>     B --> C["Cuenta<br/>|A||B|"]
>     C --> D["Relación<br/>subconjunto"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Par, producto y legge
>
> **Par:** $(a,b)=(c,d)\iff a=c\land b=d$. **Producto:** $A\times B=\{(a,b):a\in A,b\in B\}$.
>
> **Leyes:** $|A\times B|=|A||B|$; $A\times(B\cup C)=(A\times B)\cup(A\times C)$; $(A\times B)\cap(C\times D)=(A\cap C)\times(B\cap D)$.

> [!tip] 💡 Cómo operar con productos sin errores
>
> Despeja por coordenadas ($(2x,1)=(4,y+1)\therefore x=2,y=0$) — nunca cruces. Para igualdades distribuye la pertenencia: $A\times B=A\times C$ con $A\neq\emptyset$ da $B=C$ fijando $a$. Y recuerda: $A\times B=B\times A$ solo si $A=B$ o hay vacío.

> [!example] 🟢 Ejemplo — $R=\{(a,b):a<b\}$ en $\{1,2,3\}\times\{2,3,4\}$
>
> $R=\{(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)\}$; no es función ($1$ tiene 3 imágenes: falla unicidad).

---

## 📋 Tabla Comparativa: Productos

> [!note] 📋 Qué vale cada producto
>
> | Producto | Elementos | Cuenta |
> |---|---|---|
> | $\{1,2,3\}\times\{a,b\}$ | $6$ pares | $3\cdot2$ |
> | $\{1,2\}\times\{1,2\}$ | Diagonal $(1,1),(2,2)$ | $4$ |
> | $\emptyset\times\{1,2\}$ | $\emptyset$ | $0$ (anula) |
> | $A\times B=\emptyset$ | Alguno vacío | $\lor$, no $\land$ |
>
> **Relaciones:** $2^{|A||B|}$ posibles ($2\times3\to64$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$(2,3)=(3,2)$:** el orden importa (salvo iguales).
> - **$A\times B=\emptyset\therefore$ ambos vacíos:** basta uno.
> - **$A\times B=B\times A$ siempre:** solo si $A=B$ o hay vacío.
> - **Relación = función:** falta totalidad + unicidad.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $A=\{1,2,3\},B=\{a,b\}$: $A\times B$ y $|{\cdot}|$.
> 2. Despeja $(x,5)=(3,y)$ y $(2x,1)=(4,y+1)$.
> 3. $A=\emptyset,B=\{1,2\}$: $A\times B$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $6$ pares; $|{\cdot}|=6$.
>
> **2.** $x=3,y=5$; $x=2,y=0$.
>
> **3.** $\emptyset$ (anula).

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Prueba $A\times(B\cup C)=(A\times B)\cup(A\times C)$.
> 5. $R$ ($a<b$) arriba: ¿función?
> 6. Relaciones $A\to B$ con $|A|=2,|B|=3$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Pertenencia con $\lor$.
>
> **5.** No (unicidad falla).
>
> **6.** $2^6=64$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $A\times B=A\times C$, $A\neq\emptyset\therefore B=C$.
> 8. $A\times B=B\times A\iff$ ¿cuándo?
> 9. $(A\times B)\cap(C\times D)$ por doble inclusión.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Fija $a\in A$ y compara.
>
> **8.** $A=B$ o hay vacío.
>
> **9.** $(A\cap C)\times(B\cap D)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Listo $A\times B$ finitos.
> - [ ] Despejo por coordenadas.
> - [ ] Detecto orden relevante.
> - [ ] Anulo con factor vacío.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Distribuyo $\times$ sobre $\cup$.
> - [ ] Decido si relaciones son funciones.
> - [ ] Cuento $2^{|A||B|}$ relaciones.
> - [ ] Dibujo grillas cartesianas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Cancelo productos con $A\neq\emptyset$.
> - [ ] Caracterizo conmutatividad.
> - [ ] Pruebo intersecciones de productos.
> - [ ] Biyecto $\mathbb{N}\times\mathbb{N}$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §2.1.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Tipos y cardinalidad]] — base: $|A\times B|$.
> - [[09 - Relaciones]] — siguiente: relaciones.
> - [[10 - Funciones en Conjuntos]] — funciones como productos.
> - [[05 - Predicados de una variable]] — $P(x,y)$ como relación.

---

**Tags:** #conjuntos #cartesiano #relaciones #unidad1

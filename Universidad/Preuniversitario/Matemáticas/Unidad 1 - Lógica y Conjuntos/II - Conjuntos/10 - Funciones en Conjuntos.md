---
dg-publish: true
---

# 🔄 Funciones en Conjuntos

## 🎯 Introducción

> [!info] 💡 ¿Qué es $f:A\to B$?
>
> Relación total (todo $a$ tiene imagen) y única (una sola): inyectiva (distintos $\to$ distintos), sobreyectiva ($\text{Ran}=B$), biyectiva (ambas, con inversa). $|B|^{|A|}$ funciones; palomar limita inyecciones.
>
> ```mermaid
> graph LR
>     A["Total<br/>única"] --> B["Iny<br/>1-1"]
>     B --> C["Sobre<br/>Ran=B"]
>     C --> D["Biy<br/>inversa"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Función y tipos
>
> **Función:** $\forall a\in A\;\exists!b\in B:(a,b)\in f$. **Inyectiva:** $f(a_1)=f(a_2)\to a_1=a_2$. **Sobreyectiva:** $\forall b\;\exists a$.
>
> **Biyectiva:** ambas ($\iff$ inversa). **Conteo:** $|B|^{|A|}$ funciones; inyecciones $P(|B|,|A|)$ si $|A|\le|B|$.

> [!tip] 💡 Cómo clasificar sin equivocarse
>
> Totalidad primero (¿todo $a$ tiene imagen?), unicidad después (¿alguna colisión?). Para composición calcula de adentro afuera: $g\circ f$ con $f=2x,g=x+1$ es $2x+1$ (no $2x+2$: ese es $f\circ g$). Palomar decide existencias ($3\to2$ no inyecta).

> [!example] 🟢 Ejemplo — $f=\{(1,a),(2,b),(3,a)\}$
>
> Función (total+única); no inyectiva ($1,3\to a$); sobreyectiva ($a,b$ alcanzados).

---

## 📋 Tabla Comparativa: Tipos

> [!note] 📋 Qué cumple cada función
>
> | Función | Iny | Sobre | Cuenta |
> |---|---|---|---|
> | $\{1,2\}\to\{a,b,c\}$ | Sí | No | $3^2=9$ totales |
> | $x^2:\mathbb{R}\to\mathbb{R}$ | No | No | — |
> | $x^2:\mathbb{R}\to[0,\infty)$ | No | Sí | — |
> | $3x-2:\mathbb{R}\to\mathbb{R}$ | Sí | Sí | Biyectiva |
> | $\{1,2,3\}\to\{a,b\}$ | No (palomar) | $6$ sobre | $2^3=8$ totales |
>
> **Composición:** $g\circ f=2x+1$; $f\circ g=2x+2$ (no conmutan).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$g\circ f=f\circ g$:** $2x+1\neq2x+2$ (orden manda).
> - **Relación = función:** exige total + única.
> - **Inyecta $3\to2$:** palomar lo prohíbe ($0$ inyecciones).
> - **$f^{-1}=1/f$:** la inversa deshace, no divide.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $f=\{(1,a),(2,b),(3,a)\}$: ¿función? ¿inyectiva? ¿sobreyectiva?
> 2. $x^2$ en $\mathbb{R}\to\mathbb{R}$ vs $\mathbb{R}\to[0,\infty)$.
> 3. $g(a)=g(b)=1$: ¿función? ¿inyectiva?

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Sí; no; sí.
>
> **2.** Ninguna; solo sobre.
>
> **3.** Sí; no.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $f=2x$, $g=x+1$: $g\circ f$ y $f\circ g$.
> 5. Inversa de $2x+1$ con verificación.
> 6. $\{1,2,3\}\to\{a,b\}$: ¿inyectiva? ¿sobreyectivas?

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $2x+1$; $2x+2$ (no conmutan).
>
> **5.** $(y-1)/2$; $f(f^{-1})=y$.
>
> **6.** No (palomar); $6$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $3x-2$ biyectiva $\mathbb{R}\to\mathbb{R}$.
> 8. $g\circ f$ inyectiva si $f,g$ lo son.
> 9. $|\mathbb{N}\times\mathbb{N}|=|\mathbb{N}|$ (Cantor).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Iny: $3x_1\neq3x_2$; sobre: $y\mapsto(y+2)/3$.
>
> **8.** $g(f(a_1))=g(f(a_2))\to a_1=a_2$.
>
> **9.** $f(m,n)=(m+n)(m+n+1)/2+n$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico total + única.
> - [ ] Distingo iny/sobre con colisiones.
> - [ ] Cuento $|B|^{|A|}$ funciones.
> - [ ] Evalúo pares ordenados.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Compongo en orden correcto.
> - [ ] Hallo inversas y verifico.
> - [ ] Aplico palomar.
> - [ ] Pruebo biyectividad lineal.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Cuento sobreyecciones.
> - [ ] Biyecto $\mathbb{N}\to\mathbb{Z}$.
> - [ ] Demuestro inyectividad compuesta.
> - [ ] Emparejo $\mathbb{N}\times\mathbb{N}$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §2.3.
>
> [2] R. Grimaldi, *Matemática Discreta*, Pearson — cap. 3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[09 - Relaciones]] — base: $f\subseteq\times$.
> - [[10 - Función inversa de una función biyectiva]] — inversas reales.
> - [[01 - Tipos y cardinalidad]] — biyecciones y Cantor.
> - [[04 - Tipos de funciones]] — iny/sobre en $\mathbb{R}$.

---

**Tags:** #conjuntos #funciones #biyectiva #unidad1

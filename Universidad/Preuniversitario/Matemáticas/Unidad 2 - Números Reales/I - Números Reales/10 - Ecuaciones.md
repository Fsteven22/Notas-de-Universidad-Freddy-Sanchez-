---
dg-publish: true
---

# 🟰 Ecuaciones

## 🎯 Introducción

> [!info] 💡 ¿Qué es resolver una ecuación?
>
> Hallar $x$ con igualdad verdadera: lineales despejando, cuadráticas con $\Delta$, $|f|=a$ con $\pm$, radicales elevando (y verificando), sistemas por sustitución. Elevar crea extrañas — verifica siempre.
>
> ```mermaid
> graph LR
>     A["Lineal<br/>despeja"] --> B["Cuadrática<br/>Delta"]
>     B --> C["|f|, raiz<br/>casos/eleva"]
>     C --> D["Verifica<br/>extrañas"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[10-parabola.png]]

> [!tip] 💡 Visual — Raíces como cortes
>
> $x^2-5x+6=0$ corta en $2,3$; $x^2-6x+9$ toca en $3$ (doble); $x^2+1$ no corta (sin reales) — $\Delta$ lo predice.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Tipos y métodos
>
> **Lineal:** $ax+b=0\therefore x=-b/a$ ($a\neq0$; si $a=0$ discute). **Cuadrática:** $\Delta>0$ dos, $=0$ doble, $<0$ ninguna real.
>
> **$|f|=a$:** $f=\pm a$ ($a\ge0$; $a<0\to\emptyset$). **Radical:** aísla, eleva, exige radicando $\ge0$ y verifica.

> [!tip] 💡 Cómo resolver sin crear falsas
>
> Despeja en orden inverso a PEMDAS (sumas primero, multiplicaciones después). Con radicales aísla **una** raíz antes de elevar; con $|x|$ parte por ceros. Al final sustituye todo: $\sqrt{x+5}=x-1$ da $x=4$ y $x=-1$, pero $-1$ falla ($\sqrt3\neq-2$) y se descarta.

> [!example] 🟢 Ejemplo — $\sqrt{x+2}+\sqrt{x-1}=3$
>
> Aísla: $\sqrt{x+2}=3-\sqrt{x-1}$; eleva: $x+2=8+x-6\sqrt{x-1}\therefore\sqrt{x-1}=1\therefore x=2$ (verifica $\sqrt4+\sqrt1=3$ ✓).

---

## 📋 Tabla Comparativa: Ecuaciones

> [!note] 📋 Qué método usar y cuándo
>
> | Tipo | Método | Ejemplo |
> |---|---|---|
> | Lineal | Despeja | $3x-7=5\therefore x=4$ |
> | Cuadrática | $\Delta$ + fórmula | $x^2-5x+6$: $2,3$ |
> | $\|f\|=a$ | $f=\pm a$ | $\|x-3\|=5$: $8,-2$ |
> | Radical | Aísla + eleva + verifica | $\sqrt{x-1}=3\therefore x=10$ |
> | Sistema $2\times2$ | Sustituye | $x+y=5,x-y=1\therefore(3,2)$ |
>
> **Paramétrica:** $mx=4$: $m\neq0\to4/m$; $m=0\to\emptyset$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$|x|=-2$ con solución:** $\emptyset$ (módulo $\ge0$).
> - **Extrañas aceptadas:** $\sqrt{x+5}=x-1$ descarta $x=-1$.
> - **$(x+1)(x-2)=0\to$ divide:** cada factor da raíz ($-1,2$).
> - **$mx=4$ sin discutir $m$:** $m=0$ deja $\emptyset$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $3x-7=5$, $-2x+5=11$, $(2x-1)/3=(x+2)/2$.
> 2. $x^2-5x+6=0$, $x^2-9=0$, $x^2+4x+3=0$.
> 3. $|x-3|=5$, $|x|=-2$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $4$; $-3$; $8$.
>
> **2.** $2,3$; $\pm3$; $-1,-3$.
>
> **3.** $8,-2$; $\emptyset$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $-x^2+4x-3=0$ y $x^2-6x+9=0$.
> 5. $\sqrt{x+5}=x-1$ (verifica).
> 6. $x^2+y^2=25$, $x+y=7$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $1,3$; $3$ doble.
>
> **5.** $x=4$ ($-1$ extraña).
>
> **6.** $(3,4),(4,3)$ (raíces de $t^2-7t+12$).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $mx=4$ discute $m$.
> 8. $x^4-5x^2+4=0$ (bicudrática).
> 9. $1/x+1/y=5/6$, $1/x-1/y=1/6$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $x=4/m$; $\emptyset$ si $m=0$.
>
> **8.** $x=\pm1,\pm2$.
>
> **9.** $u=1/2,v=1/3\therefore x=2,y=3$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Despejo lineales en orden inverso.
> - [ ] Resuelvo cuadráticas con $\Delta$.
> - [ ] Aplico $f=\pm a$ en módulos.
> - [ ] Elevo radicales simples.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo $|x|$ por casos.
> - [ ] Descarto extrañas verificando.
> - [ ] Sustituyo en sistemas no lineales.
> - [ ] Uso Vieta para verificar.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Discuto parámetros ($m=0$).
> - [ ] Reduzco bicuadráticas con $y=x^2$.
> - [ ] Elevo dos veces con radicales dobles.
> - [ ] Sustituyo $u=1/x$ en sistemas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de ecuaciones.
>
> [2] J. Stewart, *Precálculo*, 7ma ed. — cap. 1.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[07 - Función cuadrática]] — vértice y raíces.
> - [[09 - Valor Absoluto]] — $|f|=a$ a fondo.
> - [[05 - Sistemas de ecuaciones lineales]] — sistemas $2\times2$.
> - [[11 - Inecuaciones]] — siguiente: desigualdades.

---

**Tags:** #números-reales #ecuaciones #sistemas #unidad2

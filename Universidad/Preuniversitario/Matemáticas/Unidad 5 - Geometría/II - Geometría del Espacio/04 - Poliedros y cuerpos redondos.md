---
dg-publish: true
---

# ⚖️ Poliedros y Cuerpos Redondos

## 🎯 Introducción

> [!info] 💡 ¿En qué se diferencian?
>
> Los **poliedros** tienen caras planas y cumplen Euler $V-A+C=2$; los **cuerpos redondos** (cilindro, cono, esfera, toro) tienen superficies curvas y salen de revolución. Compararlos decide qué fórmula usar y explica por qué la esfera minimiza superficie a volumen dado.
>
> ```mermaid
> graph LR
>     A["Sólido"] --> B{"Caras<br/>planas?"}
>     B -->|Sí| C["Poliedro<br/>Euler"]
>     B -->|No| D["Redondo<br/>revolución"]
>     C --> E["Prisma/Pirámide<br/>Regular"]
>     D --> E
>     style C fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Dos familias y sus leyes
>
> **Poliedros:** caras planas; convexos cumplen $V-A+C=2$. Prisma: $V=2n,A=3n,C=n+2$, $V_{ol}=A_bh$; pirámide: $V=n+1,A=2n,C=n+1$, $V_{ol}=A_bh/3$. Regulares: 5 platónicos.
>
> **Redondos:** cilindro $\pi r^2h$; cono $\pi r^2h/3$; esfera $4\pi r^3/3$; toro $2\pi^2Rr^2$.
>
> **Puente:** el cilindro es el "prisma circular" ($A_b=\pi r^2$) y el cono la "pirámide circular" (mismo $/3$).

> [!tip] 💡 Cómo elegir la fórmula sin dudar
>
> Pregunta primero: ¿caras planas o curvas? Si planas, ¿prisma (2 bases) o pirámide (ápice)? Si curvas, ¿qué generatriz rotó (rectángulo/triángulo/semicírculo)? Esa sola pregunta reduce docenas de fórmulas a 2-3 candidatas.

> [!example] 🟢 Ejemplo — Prisma hexagonal vs cilindro $r=2,h=5$
>
> Prisma hexagonal $a=2,h=5$: $A_b=6\sqrt3$, $V=30\sqrt3$. Cilindro: $V=20\pi$. Misma estructura ($A_bh$), distinta base — por eso el cilindro es "prisma límite" al crecer $n$.

---

## 📋 Tabla Comparativa: Poliedros vs Redondos

> [!note] 📋 Qué tienen en común y qué los separa
>
> | Aspecto | Poliedros | Redondos |
> |---|---|---|
> | **Caras** | Planas (polígonos) | Curvas (revolución) |
> | **Ley global** | Euler $V-A+C=2$ | Generatriz + eje |
> | **Volumen tipo** | $A_bh$ / $A_bh/3$ | $\pi\int f^2$ |
> | **Teselan espacio** | Cubos, prismas sí | Esferas no (74% Kepler) |
> | **Óptimo $V/A$** | Cubo $a/6$ | Esfera $r/3$ (mínima superficie) |
> | **Resistencia** | Aristas concentran | Esfera distribuye (submarinos) |
>
> **Eficiencia:** a volumen fijo, la esfera minimiza superficie (burbujas, gotas, células); entre poliedros gana el más "redondo" (icosaedro entre platónicos).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Euler en toro:** $V-A+C=2$ exige convexo simple; el toro da $0$ (agujero).
> - **Pirámide sin $/3$:** $V=A_bh/3$ siempre, aunque la base sea rara.
> - **Cilindro como "prisma" sin ajustar:** la analogía $A_bh$ vale, pero $A_b=\pi r^2$ (no $l^2$).
> - **Esfera tesela:** no — deja $26\%$ de huecos (Kepler $74\%$); solo cubos y prismas teselan.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Euler en prisma pentagonal y pirámide hexagonal.
> 2. Cilindro $r=2,h=5$ y cono misma base/altura: $V$ de cada uno.
> 3. Esfera $r=3$: $V$ y $A$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $10-15+7=2$; $7-12+7=2$ ✓.
>
> **2.** $20\pi$; $20\pi/3$ (un tercio).
>
> **3.** $36\pi$; $36\pi$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Prisma hexagonal $a=2,h=5$ vs cilindro $r=2,h=5$ (compara $V$).
> 5. $V/A$ de esfera $r$ vs cubo $a=2r$ (esfera doble).
> 6. Toro $R=4,r=1$: $V$ y $A$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $30\sqrt3\approx51.96$ vs $20\pi\approx62.83$.
>
> **5.** Esfera $r/3$; cubo $a=2r$: $8r^3/24r^2=r/3$. (A igual $V$, la esfera gana: compara $V=1$ en ambos.)
>
> **6.** $V=8\pi^2$; $A=16\pi^2$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba que 5 platónicos son los únicos (defecto $<360°$).
> 8. Kepler $74\%$: estima con celda cúbica $2r$ y esfera inscrita ($\pi/6\approx52\%$ simple; $74\%$ FCC).
> 9. ¿Teselan tetraedros solos? (No: ángulo diedro $\approx70.5°$ no divide $360°$; sí con octaedros.)

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $k$ caras de $n$ lados por vértice: $k(n-2)180/n<360$ da 5 casos.
>
> **8.** Simple $\pi/6$; FCC $\pi\sqrt2/6\approx74\%$.
>
> **9.** $360/70.53$ no entero; tetra+octa sí (Fedorov).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo poliedro de redondo y aplico Euler.
> - [ ] Calculo $V$ de prismas, pirámides, cilindro, cono y esfera.
> - [ ] Relaciono cilindro-prisma y cono-pirámide por $A_bh$.
> - [ ] Identifico los 5 platónicos por $V,A,C$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Comparo $V/A$ entre esfera y cubo.
> - [ ] Uso toro y sus dos radios correctamente.
> - [ ] Decido teselación (cubos sí, esferas no).
> - [ ] Verifico todo con Euler.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro unicidad de platónicos por defecto angular.
> - [ ] Estimo Kepler simple vs FCC.
> - [ ] Explico mínima superficie de la esfera.
> - [ ] Relaciono dualidades con $V\leftrightarrow C$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de sólidos.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 3 (poliedros y revolución).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Poliedros]] — Euler y platónicos en detalle.
> - [[02 - Poliedros]] — cilindro, cono, esfera, toro.
> - [[04 - Poligonales y polígonos]] — caras como polígonos.
> - [[01 - Sistema tridimensional]] — coordenadas de vértices.

---

**Tags:** #poliedros #cuerpos-redondos #comparacion #geometria #unidad5

---
dg-publish: true
---

# 🔷 Cuadriláteros

## 🎯 Introducción

> [!info] 💡 ¿Qué es un cuadrilátero?
>
> Un polígono de $4$ lados con $\alpha+\beta+\gamma+\delta=360°$. Se clasifica por pares paralelos (trapecio, paralelogramo, trapezoide) y de ahí a rombo, rectángulo y cuadrado — cada nivel añade propiedades a diagonales y áreas.
>
> ```mermaid
> graph LR
>     A["Cuadrilátero<br/>4 lados"] --> B{"Pares<br/>paralelos?"}
>     B -->|Uno| C["Trapecio"]
>     B -->|Dos| D["Paralelogramo<br/>rombo/rect/cuad"]
>     B -->|Cero| E["Trapezoide"]
>     style D fill:#e1ffe1
>     style E fill:#e1f5ff
> ```

![[U5-varignon.png]]

> [!tip] 💡 Visual — Varignon
>
> Los puntos medios de **cualquier** cuadrilátero forman un paralelogramo (punteado): sus lados son paralelos a las diagonales originales.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Elementos y jerarquía
>
> **Elementos:** vértices $A,B,C,D$; lados $a,b,c,d$; ángulos $\alpha+\beta+\gamma+\delta=360°$ (una diagonal lo parte en dos triángulos); diagonales $p=AC,q=BD$.
>
> **Jerarquía:** trapecio (1 par paralelo) → paralelogramo (2 pares: lados y ángulos opuestos iguales, diagonales se bisecan) → rombo ($4$ lados iguales, diagonales $\perp$) / rectángulo ($4$ rectos, diagonales iguales) → cuadrado (ambos).
>
> **Especiales:** cíclico (vértices en círculo $\iff$ opuestos suplementarios); tangencial (lados tangentes $\iff a+c=b+d$, Pitot).

> [!tip] 💡 Cómo clasificar sin dudar
>
> Cuenta pares paralelos: $0$ → trapezoide, $1$ → trapecio, $2$ → paralelogramo. Dentro del paralelogramo pregunta: ¿lados iguales? (rombo), ¿ángulos rectos? (rectángulo), ¿ambos? (cuadrado). Esa cascada nunca falla.

> [!example] 🟢 Ejemplo — Clasifica con lados $5,5,5,5$ y un ángulo $60°$
>
> $4$ lados iguales $\therefore$ rombo (o cuadrado); ángulo $60°\neq90°$ $\therefore$ no cuadrado. Es rombo con ángulos $60°,120°,60°,120°$.

---

## 📋 Tabla Comparativa: Áreas y Teoremas

> [!note] 📋 Qué fórmula usar y cuándo
>
> | Figura | Área | Clave |
> |---|---|---|
> | **Paralelogramo** | $bh$; $ab\sin\alpha$ | Base por altura perpendicular |
> | **Rombo** | $pq/2$; $a^2\sin\alpha$ | Diagonales $\perp$; $p^2+q^2=4a^2$ |
> | **Rectángulo** | $ab$ | Diagonales iguales $\sqrt{a^2+b^2}$ |
> | **Cuadrado** | $a^2=d^2/2$ | $d=a\sqrt2$; $R=a\sqrt2/2$, $r=a/2$ |
> | **Trapecio** | $(B+b)h/2$ | Promedio de bases |
> | **Cíclico** | Brahmagupta $\sqrt{(s-a)(s-b)(s-c)(s-d)}$ | Opuestos suplementarios; Ptolomeo $AC\cdot BD=AB\cdot CD+BC\cdot AD$ |
> | **Tangencial** | $rs$ | $a+c=b+d$ (Pitot) |
>
> **Varignon:** puntos medios forman paralelogramo de área mitad y perímetro = suma de diagonales.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$4$ lados iguales $\therefore$ cuadrado:** es **rombo**; cuadrado exige además $4$ rectos.
> - **Diagonales perpendiculares en todo paralelogramo:** solo rombo y cuadrado (rectángulo las tiene **iguales**, no perpendiculares).
> - **Trapecio con 2 pares paralelos:** eso es paralelogramo; trapecio tiene exactamente **un** par.
> - **Área con el lado oblicuo:** la altura es **perpendicular** a la base, no el lado inclinado.
> - **Perímetro vs área del cuadrado:** $P=4a$, $A=a^2$ — no mezclarlos.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Clasifica: lados $5,5,5,5$ con ángulo $60°$; ángulos $90°,90°,90°,90°$ con lados $3,4,3,4$.
> 2. Área de paralelogramo $a=8,b=5,\alpha=60°$.
> 3. Rombo lado $10$, diagonal $16$: otra diagonal y área.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Rombo; rectángulo (no cuadrado).
>
> **2.** $40\cdot\sqrt3/2=20\sqrt3$.
>
> **3.** $q^2=400-256=144\therefore q=12$; $A=16\cdot12/2=96$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Trapecio bases $12,8$, altura $5$: área.
> 5. Verifica cíclico con $\alpha=75°,\beta=110°,\gamma=105°,\delta=70°$.
> 6. Cuadrado en $(0,0),(4,0),(4,4),(0,4)$: verifica lados, diagonales y área.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(20/2)\cdot5=50$.
>
> **5.** Suma $360°$; opuestos $180°$ ✓ $\therefore$ cíclico.
>
> **6.** Lados $4$; diagonales $4\sqrt2$ iguales; $A=16$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba Varignon: puntos medios forman paralelogramo (teorema del segmento medio).
> 8. Brahmagupta con $a=2,b=3,c=4,d=5$ cíclico ($s=7$, $A=\sqrt{120}$).
> 9. Ptolomeo en rectángulo $3\times4$ ($5\cdot5=9+16$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Cada lado une puntos medios: paralelo a la diagonal e igual a su mitad → paralelogramo.
>
> **8.** $\sqrt{5\cdot4\cdot3\cdot2}=\sqrt{120}$.
>
> **9.** Diagonales $5,5$; $3\cdot3+4\cdot4=25=5\cdot5$ ✓.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Clasifico por pares paralelos con la cascada (trapecio/paralelogramo/trapezoide).
> - [ ] Distingo rombo/rectángulo/cuadrado por lados y ángulos.
> - [ ] Calculo áreas de paralelogramo, trapecio y rombo.
> - [ ] Verifico sumas de $360°$ en cualquier cuadrilátero.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico diagonales ($pq/2$, Pitágoras $p^2+q^2=4a^2$).
> - [ ] Verifico cíclicos (opuestos $180°$) y tangenciales ($a+c=b+d$).
> - [ ] Uso coordenadas para verificar cuadrados.
> - [ ] Calculo áreas con $ab\sin\alpha$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro Varignon y Ptolomeo en casos concretos.
> - [ ] Aplico Brahmagupta y Bretschneider según el caso.
> - [ ] Relaciono $R,r$ del cuadrado con $a$ y $d$.
> - [ ] Analizo cometas y rectángulos áureos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de cuadriláteros.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 1 (paralelogramos).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Poligonales y polígonos]] — $n=4$ como caso general.
> - [[05 - Triángulos]] — Varignon usa segmento medio del triángulo.
> - [[08 - Circunferencia y círculo]] — cíclicos y Ptolomeo.
> - [[07 - Perímetro y área de un polígono]] — shoelace en cuadriláteros.

---

**Tags:** #cuadrilateros #paralelogramo #rombo #geometria #unidad5

---
dg-publish: true
---

# ♾️ Hipérbola

## 🎯 Introducción

> [!info] 💡 ¿Qué es una hipérbola?
>
> El conjunto $\{P:|PF_1-PF_2|=2a\}$ (diferencia constante): $x^2/a^2-y^2/b^2=1$ con $c^2=a^2+b^2$, asíntotas $y=\pm(b/a)x$ y $e=c/a>1$.
>
> ```mermaid
> graph LR
>     A["Focos F1 F2<br/>diferencia 2a"] --> B["Eje transverso<br/>2a"]
>     B --> C["Asíntotas<br/>y=+-b/a x"]
>     C --> D["Excentricidad<br/>e mayor 1"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-hiperbola.png]]

> [!tip] 💡 Visual — $x^2/4-y^2/4=1$
>
> Dos ramas con asíntotas $y=\pm x$: lejos del centro las ramas se pegan a las asíntotas sin tocarlas nunca.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Elementos y canónicas
>
> **Elementos:** centro $C$, focos a distancia $c$, vértices a $a$, relación $c^2=a^2+b^2$ (¡suma, al revés de la elipse!), asíntotas por el centro con pendiente $\pm b/a$, $e=c/a>1$.
>
> **Horizontal:** $(x-h)^2/a^2-(y-k)^2/b^2=1$. **Vertical:** $(y-k)^2/a^2-(x-h)^2/b^2=1$ ($a$ siempre con el término **positivo**).

> [!tip] 💡 Cómo no confundirla con la elipse
>
> El signo **menos** entre cuadrados dice hipérbola al instante. El término positivo lleva $a^2$ y dice el eje (transverso). Las asíntotas salen igualando a cero: de $x^2/a^2-y^2/b^2=0$ lees $y=\pm(b/a)x$ directo.

> [!example] 🟢 Ejemplo — $4x^2-9y^2-16x+18y-29=0$
>
> $4(x-2)^2-9(y-1)^2=36\therefore(x-2)^2/9-(y-1)^2/4=1$. Centro $(2,1)$, horizontal, $a=3,b=2,c=\sqrt{13}$, asíntotas $y-1=\pm(2/3)(x-2)$.

---

## 📋 Tabla Comparativa: Las Cuatro Cónicas

> [!note] 📋 Cómo clasificar con discriminante $B^2-4AC$
>
> | Cónica | Signos $x^2,y^2$ | $B^2-4AC$ | Ejemplo |
> |---|---|---|---|
> | **Círculo** | iguales, mismo signo | $<0$ (caso $e=0$) | $x^2+y^2=25$ |
> | **Elipse** | distintos coef., mismo signo | $<0$ | $x^2/25+y^2/9=1$ |
> | **Parábola** | solo un cuadrado | $=0$ | $x^2=12y$ |
> | **Hipérbola** | signos opuestos | $>0$ | $x^2/9-y^2/16=1$ |
>
> **Equilátera:** $a=b$ (asíntotas perpendiculares); si está girada $45°$, su ecuación es $xy=k$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$c^2=a^2-b^2$ como elipse:** en hipérbola es $c^2=a^2+b^2$ ($c>a$ siempre).
> - **$a$ en el término negativo:** $a^2$ va con el término **positivo**.
> - **Asíntotas con $a/b$ invertido:** horizontal usa $b/a$; verifica con un vértice.
> - **Una sola rama dibujada:** son **dos** ramas simétricas respecto al centro.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Focos $(\pm5,0)$, vértices $(\pm3,0)$: ecuación.
> 2. Asíntotas de $x^2/9-y^2/16=1$.
> 3. $e$ de $y^2/9-x^2/27=1$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $c=5,a=3,b=4$; $x^2/9-y^2/16=1$.
>
> **2.** $y=\pm(4/3)x$.
>
> **3.** $c=6,a=3$; $e=2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Centro $(2,-1)$, $V(2,3)$, $F(2,4)$: ecuación.
> 5. Asíntotas $y=\pm2x$ por $(2,\sqrt3)$: ecuación.
> 6. Elementos de $4x^2-9y^2-16x+18y-29=0$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Vertical, $a=4,c=5,b=3$; $(y+1)^2/16-(x-2)^2/9=1$.
>
> **5.** $b=2a$; $4/a^2-3/4a^2=1\therefore a^2=13/4$; $4x^2-y^2=13$.
>
> **6.** $(2,1)$; $a=3,b=2,c=\sqrt{13}$; $V(-1,1),(5,1)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Focos $(0,\pm6)$, $e=2$: ecuación y asíntotas.
> 8. Prueba que $y=\pm(b/a)x$ son asíntotas (límite $x\to\infty$).
> 9. Clasifica $xy=1$ por rotación $45°$ (equilátera).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $c=6,a=3,b^2=27$; $y^2/9-x^2/27=1$; $y=\pm(\sqrt3/3)x$.
>
> **8.** $y=\pm(b/a)\sqrt{x^2-a^2}\to\pm(b/a)x$.
>
> **9.** $u^2-v^2=2$: hipérbola equilátera girada.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico $a,b,c$ con $c^2=a^2+b^2$.
> - [ ] Escribo canónicas desde focos y vértices.
> - [ ] Trazo asíntotas $y=\pm(b/a)x$.
> - [ ] Distingo hipérbola por el signo menos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Completo cuadrados y leo elementos.
> - [ ] Hallo ecuaciones desde asíntotas + punto.
> - [ ] Uso $e$ para hallar $a$ desde $c$.
> - [ ] Dibujo ambas ramas simétricas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro asíntotas con límites.
> - [ ] Clasifico cónicas con discriminante.
> - [ ] Reconozco la equilátera $xy=k$.
> - [ ] Relaciono $e>1$ con apertura de ramas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 5 (hipérbola).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de cónicas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[04 - Elipse]] — suma constante ($c^2=a^2-b^2$).
> - [[03 - Parábola]] — $e=1$, caso límite.
> - [[08 - Circunferencia y círculo]] — arco y tangentes sintéticas.
> - [[01 - Sistemas de ecuaciones no lineales]] — intersecciones cónicas.

---

**Tags:** #hiperbola #asintotas #conicas #geometria #unidad5

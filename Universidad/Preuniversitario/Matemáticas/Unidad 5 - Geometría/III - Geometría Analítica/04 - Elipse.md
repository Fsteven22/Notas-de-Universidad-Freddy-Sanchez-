---
dg-publish: true
---

# 🫒 Elipse

## 🎯 Introducción

> [!info] 💡 ¿Qué es una elipse?
>
> El conjunto $\{P:PF_1+PF_2=2a\}$ (suma constante a los focos): $x^2/a^2+y^2/b^2=1$ con $c^2=a^2-b^2$ y excentricidad $e=c/a$. El círculo es su caso $e=0$.
>
> ```mermaid
> graph LR
>     A["Focos F1 F2<br/>suma 2a"] --> B["Eje mayor<br/>2a"]
>     B --> C["Eje menor<br/>2b"]
>     C --> D["Excentricidad<br/>e=c/a"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-elipse.png]]

> [!tip] 💡 Visual — $x^2/9+y^2/4=1$
>
> $a=3,b=2,c=\sqrt5$: los focos $(\pm\sqrt5,0)$ están dentro, cerca del centro — $e\approx0.75$ moderadamente achatada.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Elementos y canónicas
>
> **Elementos:** centro $C$, focos $F_{1,2}$ a distancia $c$, vértices mayores a $a$, menores a $b$, relación $a^2=b^2+c^2$, excentricidad $e=c/a\in[0,1)$.
>
> **Horizontal:** $(x-h)^2/a^2+(y-k)^2/b^2=1$ ($a>b$). **Vertical:** $(x-h)^2/b^2+(y-k)^2/a^2=1$.

> [!tip] 💡 Cómo leer una elipse sin confundir ejes
>
> Divide entre el término independiente hasta forma $...=1$; el denominador **mayor** es $a^2$ y su variable dice el eje. Calcula $c=\sqrt{a^2-b^2}$ solo al final — y recuerda $e$ cerca de $0$ es casi círculo, cerca de $1$ es aguja.

> [!example] 🟢 Ejemplo — $4x^2+9y^2-8x+36y+4=0$
>
> $4(x-1)^2+9(y+2)^2=36\therefore(x-1)^2/9+(y+2)^2/4=1$. Centro $(1,-2)$, horizontal, $a=3,b=2,c=\sqrt5$, $e=\sqrt5/3$.

---

## 📋 Tabla Comparativa: Elipse vs Círculo vs Hipérbola

> [!note] 📋 Cuándo es cada cónica
>
> | Cónica | Ecuación tipo | Relación | Excentricidad |
> |---|---|---|---|
> | **Círculo** | $x^2+y^2=r^2$ | $a=b$ | $e=0$ |
> | **Elipse** | $x^2/a^2+y^2/b^2=1$ | $a^2=b^2+c^2$ | $0<e<1$ |
> | **Parábola** | $x^2=4py$ | un foco | $e=1$ |
> | **Hipérbola** | $x^2/a^2-y^2/b^2=1$ | $c^2=a^2+b^2$ | $e>1$ |
>
> **Test rápido:** dos cuadrados positivos sumando $=1$ → elipse; restando $=1$ → hipérbola.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$a$ siempre en $x$:** $a$ es el denominador mayor, esté donde esté.
> - **$c^2=a^2+b^2$ como hipérbola:** en elipse es $c^2=a^2-b^2$ ($c<a$ siempre).
> - **No dividir hasta $=1$:** sin normalizar, los denominadores no son $a^2,b^2$.
> - **Focos en el eje menor:** van sobre el eje **mayor** a distancia $c$ del centro.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Focos $(\pm3,0)$, vértices $(\pm5,0)$: ecuación y $e$.
> 2. Centro $(2,-1)$, $a=5$ vertical, $b=3$: ecuación y focos.
> 3. Excentricidad de $x^2/9+y^2/4=1$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $c=3,a=5,b=4$; $x^2/25+y^2/16=1$; $e=0.6$.
>
> **2.** $(x-2)^2/9+(y+1)^2/25=1$; $F(2,-5),(2,3)$.
>
> **3.** $e=\sqrt5/3\approx0.745$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $4x^2+9y^2-8x+36y+4=0$: centro, focos, vértices, $e$.
> 5. Focos $(\pm4,0)$, suma $=10$: ecuación.
> 6. Lado recto de $x^2/25+y^2/16=1$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(1,-2)$; $F(1\pm\sqrt5,-2)$; $V(-2,-2),(4,-2)$; $e=\sqrt5/3$.
>
> **5.** $2a=10\therefore a=5,c=4,b=3$; $x^2/25+y^2/9=1$.
>
> **6.** $2b^2/a=32/5=6.4$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $PF_1+PF_2=2a\implies x^2/a^2+y^2/b^2=1$.
> 8. Tangente a $x^2/25+y^2/16=1$ en $(5\cos\theta,4\sin\theta)$.
> 9. Órbita: $a=1.5\text{ UA}$, $e=0.017$: distancia $c$ y perihelio/afelio.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\sqrt{(x+c)^2+y^2}+\sqrt{(x-c)^2+y^2}=2a$, aísla y eleva dos veces.
>
> **8.** $xx_0/25+yy_0/16=1\therefore x\cos\theta/5+y\sin\theta/4=1$ (forma $T$ como el círculo).
>
> **9.** $c=0.0255$ UA; perihelio $1.4745$, afelio $1.5255$ UA.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico $a,b,c$ y el eje por el denominador mayor.
> - [ ] Calculo excentricidades $e=c/a$.
> - [ ] Escribo canónicas desde focos y vértices.
> - [ ] Distingo elipse de círculo e hipérbola.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Completo cuadrados y normalizo a $=1$.
> - [ ] Hallo focos y vértices trasladados.
> - [ ] Construyo elipses desde la suma $2a$.
> - [ ] Calculo lados rectos $2b^2/a$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro la canónica desde la definición.
> - [ ] Hallo tangentes en puntos paramétricos.
> - [ ] Aplico $e$ a órbitas reales.
> - [ ] Verifico focos dentro del eje mayor.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 4 (elipse).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de cónicas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Parábola]] — una sola distancia constante ($e=1$).
> - [[05 - Hipérbola]] — diferencia constante ($e>1$).
> - [[02 - Circunferencia]] — caso límite $e=0$.
> - [[15 - Sucesiones]] — Kepler: órbitas elípticas.

---

**Tags:** #elipse #focos #conicas #geometria #unidad5

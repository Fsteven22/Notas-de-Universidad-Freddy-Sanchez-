---
dg-publish: true
---

# 🔄 Coordenadas Polares: Conversión

## 🎯 Introducción

> [!info] 💡 ¿Qué son las coordenadas polares?
>
> $(r,\theta)$ con $x=r\cos\theta$, $y=r\sin\theta$: multiplicar por $r$ convierte $r=a\sin\theta$ en círculos, y $A=\frac12\int r^2d\theta$ da áreas como $6\pi$ para $r=2+2\cos\theta$.
>
> ```mermaid
> graph LR
>     A["(x,y)<br/>cartesiano"] --> B["(r,theta)<br/>polar"]
>     B --> C["Curvas<br/>r=f(theta)"]
>     C --> D["Área<br/>1/2 int r2"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-cardioide.png]]

> [!tip] 💡 Visual — Cardioide y $r=1$
>
> $r=2+2\cos\theta$ (área $6\pi$) corta al círculo $r=1$ en $(0,\pm1)$: igualar $1+\cos\theta=1$ da $\theta=\pi/2,3\pi/2$ directo.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Conversión y fórmulas
>
> **Conversión:** $x=r\cos\theta$, $y=r\sin\theta$; $r=\sqrt{x^2+y^2}$, $\theta=\arctan(y/x)$ con cuadrante.
>
> **Área:** $A=\frac12\int_\alpha^\beta r^2d\theta$. **Distancia:** ley de cosenos. **Tangente:** $dy/dx=(dr/d\theta\sin\theta+r\cos\theta)/(dr/d\theta\cos\theta-r\sin\theta)$.

> [!tip] 💡 Cómo convertir ecuaciones sin atascarse
>
> Multiplica por $r$ cuando veas $\sin\theta,\cos\theta$ sueltos ($r\sin\theta=y$); sustituye $r^2=x^2+y^2$ cuando veas $r^2$. Para identificar curvas, completa cuadrados en cartesianas — $r=4\sin\theta$ es el círculo $x^2+(y-2)^2=4$ disfrazado.

> [!example] 🟢 Ejemplo — $r=4\sin\theta$ y área de $r=2+2\cos\theta$
>
> $r^2=4r\sin\theta\therefore x^2+y^2=4y\therefore x^2+(y-2)^2=4$: círculo centro $(0,2)$, $r=2$. Área cardioide: $\frac12\int_0^{2\pi}(2+2\cos\theta)^2d\theta=\frac12[6\theta+8\sin\theta+\sin2\theta]_0^{2\pi}=6\pi$.

---

## 📋 Tabla Comparativa: Curvas Polares Comunes

> [!note] 📋 Qué ecuación da qué curva
>
> | Ecuación | Curva | Datos |
> |---|---|---|
> | $r=a$ | Círculo centrado | Radio $a$ |
> | $r=a\sin\theta$, $r=a\cos\theta$ | Círculo por el polo | Diámetro $a$ |
> | $r=a+b\cos\theta$ ($a=b$) | Cardioide | Área $6\pi a^2/...$ ($6\pi$ si $a=2$) |
> | $r=a+b\cos\theta$ ($a>b$) | Caracol sin lazo | Sin autointersección |
> | $r=a\cos(n\theta)$ | Rosa $2n$ o $n$ pétalos | $n$ par: $2n$; impar: $n$ |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Intersecciones solo igualando:** el polo puede ser corte aunque $\theta$ difiera — verifícalo aparte.
> - **$\theta$ sin cuadrante:** $(\sqrt3,1)\to(2,\pi/6)$ ✓ pero $(-1,-1)$ es $5\pi/4$, no $\pi/4$.
> - **Límites de área incompletos:** la cardioide completa exige $0$ a $2\pi$.
> - **$r$ negativo ignorado en gráficas:** $r<0$ dibuja en la dirección opuesta.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $(\sqrt3,1)$ a polares (con verificación).
> 2. Identifica $r=4\sin\theta$.
> 3. Puntos de $(1,\pi/2)$ y $(1,3\pi/2)$ en cartesianas.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(2,\pi/6)$ ($2\cos\pi/6=\sqrt3$ ✓).
>
> **2.** Círculo $(0,2)$, $r=2$.
>
> **3.** $(0,1)$, $(0,-1)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Área de $r=2+2\cos\theta$.
> 5. Intersección $r=1+\cos\theta$ con $r=1$ (+ polo).
> 6. Convierte $x^2+(y-2)^2=4$ a polar.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $6\pi$.
>
> **5.** $(1,\pi/2),(1,3\pi/2)$; el polo solo está en la cardioide.
>
> **6.** $r=4\sin\theta$ (divide entre $r$).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Tangente horizontal a $r=1+\cos\theta$ en $\theta=\pi/3$ (usa $dy/dx$).
> 8. Longitud de arco: plantea $\int\sqrt{r^2+(dr/d\theta)^2}$ para $r=2+2\cos\theta$.
> 9. Escribe $z=1+i$ en las tres formas y verifica De Moivre con $(1+i)^2=2i$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $dr/d\theta=-\sqrt3/2$, $r=3/2$; $dy/d\theta=-3/4+3/4=0$, $dx/d\theta=-\sqrt3$; horizontal.
>
> **8.** $L=\int_0^{2\pi}\sqrt{8+8\cos\theta}\,d\theta=16$.
>
> **9.** $\sqrt2\angle45°=\sqrt2e^{i\pi/4}$; $(\sqrt2)^2\angle90°=2i$ ✓.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Convierto puntos con cuadrante correcto.
> - [ ] Identifico círculos $r=a\sin\theta$.
> - [ ] Hallo intersecciones igualando + polo.
> - [ ] Verifico conversiones sustituyendo.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo áreas con $\frac12\int r^2$.
> - [ ] Convierto ecuaciones en ambos sentidos.
> - [ ] Resuelvo intersecciones completas.
> - [ ] Reconozco cardioides y caracoles.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Hallo tangentes con $dy/dx$ polar.
> - [ ] Planteo longitudes de arco.
> - [ ] Conecto polar con complejos (Euler).
> - [ ] Verifico De Moivre numéricamente.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Cálculo con Geometría Analítica* — cap. de polares.
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de coordenadas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Plano polar]] — ubicar puntos y representaciones.
> - [[03 - Graficación en coordenadas polares]] — trazado sistemático.
> - [[02 - Operaciones]] — De Moivre y forma polar.
> - [[04 - Rectas en coordenadas polares]] — rectas y círculos.

---

**Tags:** #polares #conversion #cardioide #unidad6

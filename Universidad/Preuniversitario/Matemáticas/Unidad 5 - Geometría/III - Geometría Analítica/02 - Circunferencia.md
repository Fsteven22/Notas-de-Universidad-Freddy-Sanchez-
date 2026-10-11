---
dg-publish: true
---

# ⭕ Circunferencia

## 🎯 Introducción

> [!info] 💡 ¿Qué es una circunferencia analíticamente?
>
> El conjunto $\{(x,y):(x-h)^2+(y-k)^2=r^2\}$ — puntos a distancia $r$ del centro $(h,k)$. Completando cuadrados se lee centro y radio desde la forma general, y con $T_xx+T_yy=r^2$ se traza la tangente en un punto.
>
> ```mermaid
> graph LR
>     A["Centro<br/>(h,k) + r"] --> B["Canónica<br/>(x-h)2+.."]
>     B --> C["General<br/>completar"]
>     C --> D["Tangente<br/>Txx+Tyy=r2"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Canónica, general y elementos
>
> **Canónica:** $(x-h)^2+(y-k)^2=r^2$. **General:** $x^2+y^2+Dx+Ey+F=0$ con centro $(-D/2,-E/2)$ y $r^2=h^2+k^2-F$ (exige $D^2+E^2-4F>0$).
>
> **Elementos:** centro, radio, diámetro, cuerda, tangente ($\perp$ al radio), secante.

> [!tip] 💡 Cómo pasar de general a canónica sin perderse
>
> Agrupa $x$ con $x$ e $y$ con $y$ y completa cuadrados sumando a ambos lados; el centro sale con signos cambiados. Antes de terminar verifica $D^2+E^2-4F>0$ — si no, no hay círculo real (punto o vacío).

> [!example] 🟢 Ejemplo — Centro y radio de $x^2+y^2+8x-6y+9=0$
>
> $(x^2+8x+16)+(y^2-6y+9)=-9+16+9\therefore(x+4)^2+(y-3)^2=16$. Centro $(-4,3)$, $r=4$ (verifica $64+36-36=64>0$ ✓).

---

## 📋 Tabla Comparativa: Posiciones

> [!note] 📋 Qué criterio usar en cada caso
>
> | Situación | Criterio | Ejemplo |
> |---|---|---|
> | **Punto vs círculo** | $d<C\,r$: dentro; $=r$: sobre; $>r$: fuera | $(3,4)$ sobre $x^2+y^2=25$ |
> | **Recta vs círculo** | $d<r$: secante (2); $=r$: tangente (1); $>r$: exterior (0) | Sustituye y discriminante |
> | **Círculo vs círculo** | $d<R+r$ y $d>\|R-r\|$: 2 cortes; $=$: tangentes; si no: separados/incluido | Compara $d$ con suma y resta |
> | **Tangente en $P$** | $T_xx+T_yy=r^2$ (centrada) | $(3,4)$: $3x+4y=25$ |
>
> **Potencia:** $Pot(P)=d^2-r^2$ ($>0$ exterior, $=0$ sobre, $<0$ interior).

![[U5-tangente.png]]

---

## 🛠️ Método: Tres Puntos y Tangentes

> [!note] 📋 Procedimiento general
>
> 1. **Por tres puntos:** sustituye en $x^2+y^2+Dx+Ey+F=0$, resuelve el $3\times3$ para $D,E,F$.
> 2. **Tangente en $P$:** verifica $P$ sobre el círculo; usa $T_xx+T_yy=r^2$ (o $m_\perp=-1/m_{radio}$).
> 3. **Tangentes desde exterior:** $PT^2=d^2-r^2$ da la longitud; los puntos de contacto salen del sistema.
>
> **Principio clave:** cada condición geométrica (pasa por, tangente a) es una ecuación algebraica — tres condiciones determinan $D,E,F$.

> [!example] 🟢 Ejemplo — Círculo por $(1,1),(5,1),(3,5)$
>
> Sistema: $D+E+F=-2$, $5D+E+F=-26$, $3D+5E+F=-34$. Resta: $4D=-24\therefore D=-6$; $2D+4E=-32\therefore E=-5$; $F=9$. Ecuación $x^2+y^2-6x-5y+9=0$; centro $(3,2.5)$, $r=2.5$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Centro con signos sin cambiar:** en $(x+4)^2$ el centro es $h=-4$.
> - **Radio sin verificar existencia:** si $D^2+E^2-4F\le0$ no hay círculo real.
> - **Tangente sin verificar $P$:** $T_xx+T_yy=r^2$ exige $P$ sobre el círculo.
> - **$r^2$ negativo aceptado:** $r^2=h^2+k^2-F$ debe ser $>0$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Canónica a general: $(x-3)^2+(y+2)^2=16$.
> 2. Posición de $(3,4)$ y $(0,0)$ respecto a $x^2+y^2=25$.
> 3. Tangente a $x^2+y^2=25$ en $(3,4)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $x^2+y^2-6x+4y-3=0$.
>
> **2.** Sobre ($9+16=25$); dentro ($0<25$).
>
> **3.** $3x+4y=25$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Centro y radio de $x^2+y^2+8x-6y+9=0$ (dos métodos).
> 5. Círculo por $(1,1),(5,1),(3,5)$.
> 6. Intersección $x^2+y^2=13$ con $y=2x+1$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(-4,3)$, $r=4$.
>
> **5.** $D=-6,E=-5,F=9$; centro $(3,2.5)$, $r=2.5$.
>
> **6.** $5x^2+4x-12=0\therefore x=1.2,-2$; puntos $(1.2,3.4),(-2,-3)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Tangentes desde $(10,0)$ a $x^2+y^2=25$ (longitud y puntos).
> 8. Prueba que el inscrito en semicírculo es recto con vectores (producto punto $0$).
> 9. Potencia de $(7,0)$ respecto a $x^2+y^2=25$ y su significado.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $PT=\sqrt{75}=5\sqrt3$; contactos resolviendo $(x-0)^2...$ sistema con $x^2+y^2=25$.
>
> **8.** $(P-A)\cdot(P-B)=0$ con $AB$ diámetro.
>
> **9.** $49-25=24>0$ (exterior; $\sqrt{24}$ tangente).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Paso de canónica a general y viceversa.
> - [ ] Decido posición de puntos con $d$ vs $r$.
> - [ ] Trazo tangentes en puntos del círculo.
> - [ ] Identifico centro y radio a simple vista.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Completo cuadrados y verifico existencia.
> - [ ] Hallo círculos por tres puntos.
> - [ ] Resuelvo intersecciones con discriminante.
> - [ ] Aplico potencia de un punto.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Hallo tangentes desde puntos exteriores.
> - [ ] Demuestro inscrito en semicírculo.
> - [ ] Relaciono discriminante con posiciones.
> - [ ] Verifico ciclicidad con potencia.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 2 (circunferencia).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. del círculo.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[08 - Circunferencia y círculo]] — arco, sector y tangentes sintéticas.
> - [[01 - Puntos y rectas]] — distancias y rectas usadas aquí.
> - [[03 - Parábola]] — siguiente cónica: vértice y foco.
> - [[09 - Polígonos y circunferencia]] — Ptolomeo y ciclicidad.

---

**Tags:** #circunferencia #circulo #tangente #geometria #unidad5

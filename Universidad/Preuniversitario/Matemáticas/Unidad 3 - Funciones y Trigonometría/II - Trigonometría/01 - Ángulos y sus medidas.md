---
dg-publish: true
---

# 📐 Ángulos y sus Medidas

## 🎯 Introducción

> [!info] 💡 ¿Cómo se miden los ángulos?
>
> Grados ($360°$ la vuelta) y radianes ($2\pi$ la vuelta, $\pi$ rad $=180°$): con $s=r\theta$ y $A=r^2\theta/2$ el radián vuelve arco y sector multiplicaciones directas.
>
> ```mermaid
> graph LR
>     A["Grados<br/>360"] --> B["Radianes<br/>2pi"]
>     B --> C["Arco<br/>s=rt"]
>     C --> D["Sector<br/>r2t/2"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Sistemas, arco y sector
>
> **Conversión:** $\text{rad}=\text{grad}\times\pi/180$. **Coterminales:** $\theta+360°k$ (mismo lado terminal).
>
> **Arco:** $s=r\theta$ ($\theta$ en radianes). **Sector:** $A=r^2\theta/2$. **Segmento:** $(r^2/2)(\theta-\sin\theta)$.

> [!tip] 💡 Cómo convertir y verificar sin errores
>
> Memoriza el puente $\pi=180°$ y multiplica por $\pi/180$ o $180/\pi$ según la dirección — verifica con un caso conocido ($90°\to\pi/2$). Para relojes, la horaria avanza $0.5°$ por minuto: a las 2:20 marca $70°$ y el minutero $120°\therefore50°$ entre ellas.

> [!example] 🟢 Ejemplo — Sector y segmento ($r=3$, $\theta=\pi/3$)
>
> $A=9(\pi/3)/2=3\pi/2$. Segmento con $r=2$, $\theta=\pi/2$: $(4/2)(\pi/2-1)=\pi-2$.

---

## 📋 Tabla Comparativa: Ángulos Notables

> [!note] 📋 Qué conversión memorizar
>
> | Grados | Radianes | Tipo |
> |---|---|---|
> | $30°$ | $\pi/6$ | Agudo |
> | $45°$ | $\pi/4$ | Agudo |
> | $90°$ | $\pi/2$ | Recto |
> | $180°$ | $\pi$ | Llano |
> | $225°$ | $5\pi/4$ | $+180°+45°$ |
> | $270°$ | $3\pi/2$ | Reflexivo ($>180°$) |
>
> **Coterminales:** $30°\to390°$; $-45°\to315°$; $150°$ y $-210°$ difieren $360°$ ✓.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$s=r\theta$ con grados:** $\theta$ debe estar en radianes.
> - **$270°$ obtuso:** obtuso es $<180°$; $270°$ es reflexivo.
> - **Coterminal restando mal:** $-45°+360°=315°$ (suma, no resta).
> - **Horaria fija en la hora:** avanza $0.5°$/min (2:20 $\to70°$).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. A radianes: $30°,45°,60°,90°,180°$.
> 2. A grados: $\pi/6,\pi/4,\pi/3,\pi/2,3\pi/4$.
> 3. Arco con $r=2$, $\theta=\pi/4$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\pi/6,\pi/4,\pi/3,\pi/2,\pi$.
>
> **2.** $30°,45°,60°,90°,135°$.
>
> **3.** $s=\pi/2$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $225°$ a rad y su coterminal negativo.
> 5. Sector $r=3$, $\theta=\pi/3$.
> 6. Arco $s=4$, $r=2$: $\theta$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $5\pi/4$; $-135°$.
>
> **5.** $3\pi/2$.
>
> **6.** $2$ rad.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Reloj: ángulo exacto a las 2:20.
> 8. Segmento $r=2$, $\theta=\pi/2$.
> 9. $\omega=2\pi$ rad/s a rpm.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $120°-70°=50°$.
>
> **8.** $\pi-2$.
>
> **9.** $60$ rpm.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Convierto grados-radianes ambos sentidos.
> - [ ] Clasifico agudo/recto/obtuso/llano/reflexivo.
> - [ ] Hallo coterminales $\pm360°$.
> - [ ] Calculo arcos $s=r\theta$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo áreas de sectores.
> - [ ] Comparo coterminalidad por diferencia.
> - [ ] Despejo $\theta$ desde $s$.
> - [ ] Resuelvo relojes básicos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro $s=r\theta$ por proporción.
> - [ ] Calculo segmentos circulares.
> - [ ] Convierto $\omega$ a rpm.
> - [ ] Resuelvo relojes exactos.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 5 (trigonometría).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de ángulos.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[03 - Ángulos]] — ángulos en geometría plana.
> - [[02 - Funciones trigonométricas elementales]] — siguiente: $\sin,\cos$.
> - [[01 - Plano polar]] — $\theta$ como coordenada.
> - [[08 - Circunferencia y círculo]] — arco y sector sintéticos.

---

**Tags:** #trigonometria #angulos #radianes #unidad3

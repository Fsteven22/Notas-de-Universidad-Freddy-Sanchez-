---
dg-publish: true
---

# 🌙 Figuras Circulares

## 🎯 Introducción

> [!info] 💡 ¿Qué figuras nacen del círculo?
>
> **Sector** (cuña con ángulo $\theta$), **segmento** (sector menos triángulo), **corona** (anillo entre dos radios) y **lúnula** (entre dos arcos) — todas se miden sumando o restando áreas de círculo, triángulo y sector.
>
> ```mermaid
> graph LR
>     A["Círculo<br/>πr2"] --> B["Sector<br/>r2θ/2"]
>     B --> C["Segmento<br/>sector-triángulo"]
>     A --> D["Corona<br/>π(R2-r2)"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-circulares.png]]

> [!tip] 💡 Visual — sector, corona, segmento
>
> Sector ($r^2\theta/2$), corona ($\pi(R^2-r^2)$) y segmento (sector menos el triángulo central).

---

## 📋 Definición Formal

> [!note] 📋 Definición — Sector, segmento, corona y lúnula
>
> - **Sector** ($\theta$ rad): $A=r^2\theta/2$, arco $s=r\theta$.
> - **Segmento** circular: sector menos triángulo isósceles: $A=\frac12r^2(\theta-\sin\theta)$.
> - **Corona** ($r<R$): $A=\pi(R^2-r^2)=\pi(R+r)(R-r)$; ancho $w=R-r$.
> - **Lúnula:** entre dos arcos; Hipócrates: algunas equivalen a figuras rectilíneas.
> - **Trapecio circular:** porción de corona entre dos radios: $A=(R^2-r^2)\theta/2$.

> [!tip] 💡 Cómo no confundirlas
>
> Pregunta qué bordes tiene: ¿dos radios + arco? Sector. ¿cuerda + arco? Segmento (resta el triángulo). ¿dos círculos? Corona (resta áreas). ¿dos arcos de círculos distintos? Lúnula (resta segmentos).

> [!example] 🟢 Ejemplo — Segmento con $r=2$, $\theta=60°=\pi/3$
>
> Sector: $\frac12\cdot4\cdot\pi/3=2\pi/3$. Triángulo: $\frac12\cdot4\cdot\sin60°=\sqrt3$. Segmento: $2\pi/3-\sqrt3\approx0.36$.

---

## 📋 Tabla Comparativa

> [!note] 📋 Qué fórmula usar y cuándo
>
> | Figura | Área | Clave |
> |---|---|---|
> | **Sector** | $r^2\theta/2$ ($\theta$ rad) | Fracción $\theta/2\pi$ del círculo |
> | **Segmento** | $\frac12r^2(\theta-\sin\theta)$ | Sector menos triángulo |
> | **Corona** | $\pi(R^2-r^2)$ | Resta de círculos |
> | **Lúnula** | diferencia de segmentos | Caso Hipócrates = triángulo |
> | **Trapecio circular** | $(R^2-r^2)\theta/2$ | Corona parcial |
>
> **Teorema de la corona:** si una cuerda del exterior es tangente al interior, $A=\pi(c/2)^2$ con $c$ la cuerda — depende solo de $c$, no de $R,r$ (Pitágoras: $c^2/4=R^2-r^2$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\theta$ en grados en $r^2\theta/2$:** exige **radianes** ($60°=\pi/3$).
> - **Segmento = sector:** falta restar el triángulo isósceles central.
> - **Corona con diámetros:** $R,r$ son **radios**; si dan $D$, divide entre 2 primero.
> - **Lúnula cualquiera cuadrable:** solo 5 tipos (Hipócrates y familia); en general no.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Sector $r=8$, $45°$.
> 2. Corona $R=5,r=3$.
> 3. Arco $r=6$, $120°$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $A=\frac12\cdot64\cdot\pi/4=8\pi$.
>
> **2.** $\pi(25-9)=16\pi$.
>
> **3.** $s=6\cdot2\pi/3=4\pi$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Segmento $r=2$, $\theta=60°$.
> 5. Corona con cuerda tangente $c=8$.
> 6. Trapecio circular $R=4,r=2,\theta=\pi/2$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $2\pi/3-\sqrt3$.
>
> **5.** $A=\pi\cdot16=16\pi$ (solo depende de $c$).
>
> **6.** $(16-4)(\pi/2)/2=3\pi$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba el teorema de la corona con Pitágoras ($c^2/4=R^2-r^2$).
> 8. Lúnula de Hipócrates: área = triángulo (con $r$ y catetos).
> 9. Segmento con $\theta=120°$, $r=3$ y verifica contra sector menos triángulo.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Mitad de cuerda, radio interior y $c/2$: triángulo recto.
>
> **8.** Arcos se cancelan dejando el triángulo isósceles.
>
> **9.** $\frac12\cdot9\cdot(2\pi/3-\sqrt3/2)=3\pi-9\sqrt3/4...$ calcula: $\frac92(2\pi/3-\sin120°)=\frac92(2\pi/3-\sqrt3/2)=3\pi-9\sqrt3/4$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo sectores y arcos convirtiendo a radianes.
> - [ ] Hallo coronas restando círculos.
> - [ ] Distingo sector, segmento y corona por sus bordes.
> - [ ] Uso $s=r\theta$ correctamente.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resto el triángulo para hallar segmentos.
> - [ ] Aplico el teorema de la cuerda tangente.
> - [ ] Calculo trapecios circulares parciales.
> - [ ] Verifico resultados por dos vías.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro el teorema de la corona con Pitágoras.
> - [ ] Explico la cuadratura de Hipócrates.
> - [ ] Manejo lúnulas como diferencia de segmentos.
> - [ ] Relaciono estas áreas con integrales (coronas diferenciales).

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de áreas circulares.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 2 (sectores).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[08 - Circunferencia y círculo]] — arco, sector y tangentes.
> - [[01 - Ángulos y sus medidas]] — radianes para $\theta$.
> - [[07 - Perímetro y área de un polígono]] — áreas por descomposición.
> - [[09 - Polígonos y circunferencia]] — Ptolomeo y áreas mixtas.

---

**Tags:** #figuras-circulares #sector #corona #geometria #unidad5

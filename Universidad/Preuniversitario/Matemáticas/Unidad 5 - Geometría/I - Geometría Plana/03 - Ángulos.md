---
dg-publish: true
---

# 📐 Ángulos

## 🎯 Introducción

> [!info] 💡 ¿Qué es un ángulo?
>
> La región entre dos semirrectas con vértice común, medida en **grados** ($360°$ la vuelta) o **radianes** ($2\pi$ la vuelta, $180°=\pi$). Se clasifica por magnitud (agudo/recto/obtuso), por posición (adyacentes/opuestos) y cumple leyes en triángulos, polígonos y circunferencias.
>
> ```mermaid
> graph LR
>     A["Dos rayos<br/>vértice común"] --> B["Medida<br/>grados/rad"]
>     B --> C["Clasifica<br/>magnitud/posición"]
>     C --> D["Leyes<br/>triángulo/polígono"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-angulos.png]]

> [!tip] 💡 Visual — paralelas y transversal
>
> Entre $L_1\parallel L_2$ los alternos internos ($a,b$) son iguales; los colaterales suman $180°$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Ángulo, medida y clasificación por magnitud
>
> Ángulo $(r_1,r_2)$ con vértice $O$: $0°\le\alpha\le360°$. **Sistemas:** sexagesimal ($1°=60'=3600''$), radianes ($\text{rad}=\text{grad}\cdot\pi/180$), gon ($400$ la vuelta, topografía).
>
> **Magnitud:** nulo $0°$, agudo $<90°$, recto $90°$, obtuso $90°$-$180°$, llano $180°$, reflejo $>180°$. **Parejas:** complementarios ($90°$), suplementarios ($180°$), conjugados ($360°$).

> [!tip] 💡 Cómo convertir sin equivocarse
>
> Multiplica por el factor unitario: grados a radianes por $\pi/180$, radianes a grados por $180/\pi$. Para $D=d+m/60+s/3600$: divide minutos por $60$ y segundos por $3600$ antes de sumar — el error típico es sumar $32'$ como $0.32°$.

> [!example] 🟢 Ejemplo — $127°32'45''$ a decimal y radianes
>
> $D=127+32/60+45/3600=127.5458°$; rad $=127.5458\cdot\pi/180\approx2.2266$.

---

## 📋 Tabla Comparativa: Posiciones y Leyes

> [!note] 📋 Qué vale en cada caso y cuándo usarlo
>
> | Situación | Regla | Uso |
> |---|---|---|
> | **Opuestos por vértice** | iguales ($\alpha=\beta$) | Dos rectas que se cortan |
> | **Adyacentes** | suplementarios si forman llano | Ángulos juntos |
> | **Correspondientes** (paralelas) | iguales | Hallar $x$ igualando |
> | **Alternos** (paralelas) | iguales | Interior o exterior opuesto |
> | **Colaterales** (paralelas) | suman $180°$ | Mismo lado |
> | **Triángulo** | $\alpha+\beta+\gamma=180°$ | Interior; exterior = suma no adyacentes |
> | **Polígono $n$** | interiores $(n-2)180°$, exteriores $360°$ | Regular: $\alpha_{int}=180-360/n$ |
> | **Inscrito** | mitad del central mismo arco | Semicírculo $\therefore90°$ |
> | **Inclinación** | $m=\tan\alpha$ | $\alpha=\arctan m$ por cuadrante |

> [!example] 🟢 Ejemplo — Paralelas con $3x+20°$ y $5x-40°$ correspondientes
>
> Iguales: $3x+20=5x-40\therefore x=30$; ángulos $110°$ y $110°$ ✓ (los otros cuatro son $70°$, suplementarios).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Opuestos por el vértice suplementarios:** son **iguales**; suplementarios son los adyacentes.
> - **$\pi=360°$:** $\pi=180°$, $2\pi=360°$ — verifica el factor.
> - **Complementarios suman $180°$:** complementarios $90°$, suplementarios $180°$.
> - **Ángulo entre rectas $>90°$:** la fórmula con $|\cdot|$ da el **agudo** ($0°<\theta\le90°$).
> - **Cuadrilátero suma $180°$:** es $(4-2)180°=360°$; $180°$ es solo triángulos.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Convierte $60°$ a radianes y $3\pi/4$ a grados.
> 2. Complemento de $35°$ y suplemento de $110°$.
> 3. Clasifica $45°,95°,180°,270°$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\pi/3$; $135°$.
>
> **2.** $55°$; $70°$.
>
> **3.** Agudo, obtuso, llano, reflejo.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Paralelas cortadas: correspondiente $3x+20°$ e igual a $5x-40°$; halla $x$.
> 5. Ángulo agudo entre $y=2x+1$, $y=-x+3$ ($\tan\theta=3$).
> 6. Polígono regular con interior $140°$: lados y diagonales.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $x=30$; ángulos $110°$.
>
> **5.** $\theta=\arctan3\approx71.57°$.
>
> **6.** $(n-2)180=140n\therefore n=9$; $D=9\cdot6/2=27$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba que opuestos por el vértice son iguales (adyacencias suplementarias).
> 8. Inscrito en semicírculo $=90°$ (isósceles con centro + suma $180°$).
> 9. Ángulo polar de $(-1,1)$: cuadrante II $\therefore3\pi/4$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\alpha+\gamma=180=\beta+\gamma\therefore\alpha=\beta$.
>
> **8.** Dos triángulos isósceles con el centro; suma da $2\alpha+2\beta=180°$.
>
> **9.** $\arctan(-1)=-\pi/4+\pi=3\pi/4$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Convierto grados, radianes y decimal con $D=d+m/60+s/3600$.
> - [ ] Clasifico por magnitud y hallo complementos/suplementos.
> - [ ] Identifico opuestos por el vértice como iguales.
> - [ ] Distingo agudo/recto/obtuso/llano/reflejo al verlos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico correspondientes/alternos/colaterales en paralelas.
> - [ ] Uso suma $180°$ en triángulos y $(n-2)180°$ en polígonos.
> - [ ] Hallo ángulos entre rectas con $\tan\theta$.
> - [ ] Calculo inscritos como mitad del central.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro opuestos iguales e inscrito en semicírculo.
> - [ ] Hallo lados/diagonales desde el ángulo interior regular.
> - [ ] Determino ángulos polares por cuadrante ($\text{atan2}$).
> - [ ] Verifico cuadriláteros cíclicos con opuestos suplementarios.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de ángulos.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 1 (medida angular).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Figuras geométricas en el plano]] — figuras donde viven los ángulos.
> - [[02 - Clases de rectas en el plano]] — ángulo entre rectas y pendientes.
> - [[05 - Triángulos]] — suma $180°$ y clasificación por ángulos.
> - [[08 - Circunferencia y círculo]] — central, inscrito y cuadriláteros cíclicos.

---

**Tags:** #angulos #medicion-angular #geometria #unidad5

---
dg-publish: true
---

# 🧊 Sistema Tridimensional

## 🎯 Introducción

> [!info] 💡 ¿Qué añade la tercera dimensión?
>
> Puntos $(x,y,z)$ con distancia $d=\sqrt{\Delta x^2+\Delta y^2+\Delta z^2}$, 8 octantes por signos y vectores en $\mathbb{R}^3$ con producto escalar — la extensión directa del plano hacia poliedros y superficies.
>
> ```mermaid
> graph LR
>     A["Punto<br/>(x,y,z)"] --> B["Distancia<br/>3D"]
>     B --> C["Vectores<br/>R3"]
>     C --> D["Planos y<br/>superficies"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-3d.png]]

> [!tip] 💡 Visual — distancia en 3D
>
> $A(1,2,3)$ a $B(4,-1,5)$: $d=\sqrt{9+9+4}=\sqrt{22}$ (Pitágoras aplicado dos veces).

---

## 📋 Definición Formal

> [!note] 📋 Definición — Coordenadas, distancia y vectores
>
> **Punto:** $(x,y,z)$; **octantes** por signos (I: $+,+,+$; VI: $-,+,-$ para $(-2,3,-4)$).
>
> **Distancia:** $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$. **Punto medio:** promedio por coordenadas. **División** $r$:$s$: $P=(sA+rB)/(r+s)$.
>
> **Vectores:** $\vec{v}=(v_1,v_2,v_3)$, $|\vec{v}|=\sqrt{\sum v_i^2}$; **escalar:** $\vec{u}\cdot\vec{v}=\sum u_iv_i=|u||v|\cos\theta$; **unitario:** $\hat{u}=\vec{v}/|\vec{v}|$.

> [!tip] 💡 Cómo no perderse en 3D
>
> Todo es el caso 2D con una coordenada más: distancia añade $(\Delta z)^2$, punto medio promedia tres, y el escalar suma tres productos. Si una fórmula 3D te confunde, escríbela primero en 2D y agrega $z$.

> [!example] 🟢 Ejemplo — Distancia, medio y escalar
>
> $A(1,2,3),B(4,-1,5)$: $d=\sqrt{9+9+4}=\sqrt{22}$. Medio de $(2,-3,5),(6,1,-1)$: $(4,-1,2)$ ✓ (verifica $\sqrt{17}$ a cada extremo). $\vec{u}=(2,-1,3),\vec{v}=(1,4,-2)$: $\vec{u}\cdot\vec{v}=2-4-6=-8$.

---

## 📋 Tabla Comparativa: 2D vs 3D

> [!note] 📋 Qué cambia al agregar $z$
>
> | Concepto | 2D | 3D |
> |---|---|---|
> | **Distancia** | $\sqrt{\Delta x^2+\Delta y^2}$ | $+\Delta z^2$ dentro |
> | **Punto medio** | promedia $x,y$ | promedia $x,y,z$ |
> | **Regiones** | 4 cuadrantes | 8 octantes |
> | **Vectores** | $(v_1,v_2)$ | $(v_1,v_2,v_3)$ |
> | **Escalar** | $u_1v_1+u_2v_2$ | $+u_3v_3$ |
> | **Planos** | rectas $Ax+By=C$ | planos $Ax+By+Cz=D$ |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Olvidar $(\Delta z)^2** en distancia (da menor valor).
> - **Signos en octantes:** $(-,+,-)$ es VI, no II — revisa las tres coordenadas.
> - **División $r$:$s$ al revés:** $P=(sA+rB)/(r+s)$ (cruzado: $s$ pondera $A$).
> - **Ángulo con escalar sin normalizar:** $\cos\theta=\vec{u}\cdot\vec{v}/(|u||v|)$, no solo el producto.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Distancia $(1,2,3)$ a $(4,-1,5)$.
> 2. Punto medio de $(2,-3,5)$ y $(6,1,-1)$.
> 3. Octante de $(-2,3,-4)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\sqrt{22}$.
>
> **2.** $(4,-1,2)$.
>
> **3.** $(-,+,-)$: VI.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Divide $AB$ en razón $2$:$3$ con $A(1,2,3),B(6,12,8)$.
> 5. $|\vec{v}|$ y unitario de $(3,-4,12)$.
> 6. Ángulo entre $(2,-1,3)$ y $(1,4,-2)$ ($\cos\theta=-8/\sqrt{14\cdot21}$).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(3,6,5)$ (verifica $2\sqrt6/3\sqrt6$).
>
> **5.** $13$; $(3/13,-4/13,12/13)$.
>
> **6.** Obtuso ($\cos<0$).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba desigualdad triangular en $\mathbb{R}^3$ con Cauchy-Schwarz.
> 8. Halla el plano por $(1,0,0),(0,1,0),(0,0,1)$ ($x+y+z=1$).
> 9. Volumen del paralelepípedo con aristas $(1,0,0),(0,2,0),(0,0,3)$ ($6$ por triple producto).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $|u+v|^2\le(|u|+|v|)^2$ expandiendo con escalar.
>
> **8.** Interceptos unitarios $\therefore x+y+z=1$.
>
> **9.** $|\det|=6$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo distancias y puntos medios en 3D.
> - [ ] Ubico octantes por signos.
> - [ ] Hallo magnitudes y unitarios.
> - [ ] Distingo 2D de 3D al agregar $z$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Divido segmentos en razón dada.
> - [ ] Hallo ángulos con producto escalar.
> - [ ] Verifico resultados por simetría.
> - [ ] Uso vectores para distancias.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro triangular con Cauchy-Schwarz.
> - [ ] Hallo planos por interceptos.
> - [ ] Calculo volúmenes con triple producto.
> - [ ] Relaciono escalar con proyecciones.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Geometría Analítica* — cap. 3 (espacio 3D).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de sólidos.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Figuras geométricas en el plano]] — distancia 2D como base.
> - [[02 - Poliedros]] — siguiente: sólidos con vértices 3D.
> - [[03 - Operaciones binarias]] — $\mathbb{R}^3$ como espacio vectorial.
> - [[01 - Puntos y rectas]] — rectas y planos analíticos.

---

**Tags:** #tridimensional #vectores #distancia-3d #geometria #unidad5

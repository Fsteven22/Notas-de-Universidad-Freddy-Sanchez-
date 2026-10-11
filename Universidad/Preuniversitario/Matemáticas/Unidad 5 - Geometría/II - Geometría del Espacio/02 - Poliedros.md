---
dg-publish: true
---

# 🧊 Poliedros y Sólidos

## 🎯 Introducción

> [!info] 💡 ¿Qué sólidos importan?
>
> Poliedros (caras planas: Euler $V-A+C=2$, 5 regulares, prismas y pirámides) y redondos (cilindro, cono, esfera: girar un perfil los genera, y Pappus da volúmenes girando áreas).
>
> ```mermaid
> graph LR
>     A["Caras<br/>planas"] --> B["Euler<br/>V-A+C=2"]
>     B --> C["Prisma<br/>pirámide"]
>     C --> D["Gira<br/>redondos"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-solidos.png]]

> [!tip] 💡 Visual — Familia de sólidos
>
> Prisma ($2B+Ph$), pirámide ($B+Ph/2$... $V=Bh/3$), cilindro ($2\pi r^2+2\pi rh$), cono ($\pi r^2+\pi rg$) y esfera ($4\pi r^2$): la figura los ordena por caras planas vs curvas.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Poliedros y redondos
>
> **Poliedro:** caras poligonales; **Euler** $V-A+C=2$ (vale porque toda red polédrica conexa colapsa a ese invariante). **Regulares:** 5 (tetra, cubo, octa, dodeca, icosa: solo 5 porque en cada vértice caben 3–5 triángulos, 3 cuadrados o 3 pentágonos).
>
> **Prisma:** $V=BH$ (cavalieri: secciones iguales $\therefore$ volumen igual); **pirámide/cono:** $V=BH/3$ (tres pirámides llenan el prisma). **Cilindro:** $V=\pi r^2h$; **esfera:** $V=4\pi r^3/3$, $A=4\pi r^2$. **Pappus:** $V=A\cdot d$ (área por distancia del centroide: explica el $4\pi r^3/3$ girando el semicírculo).

> [!tip] 💡 Cómo no confundir fórmulas
>
> Todo lo "recto" (prisma, cilindro) es base $\times$ altura; todo lo "puntiagudo" (pirámide, cono) es eso entre $3$ — si tu cono no lleva $/3$, está mal. La esfera sale de Pappus o de $4/3$: verifica con $r=1$ ($V=4\pi/3\approx4.19$).

> [!example] 🟢 Ejemplo — Pirámide cuadrada $l=6,h=9$ y esfera $r=3$
>
> $B=36\therefore V=36\cdot9/3=108$. Esfera: $V=4\pi(27)/3=36\pi$, $A=36\pi$ (coinciden solo porque $r=3$: $4\pi r^2=4\pi r^3/3\iff r=3$).

---

## 📋 Tabla Comparativa: Sólidos

> [!note] 📋 Qué fórmula usa cada uno y por qué
>
> | Sólido | Volumen (por qué) | Área |
> |---|---|---|
> | Prisma | $BH$ (Cavalieri) | $2B+Ph$ |
> | Pirámide | $BH/3$ (3 llenan prisma) | $B+Ph/2$ |
> | Cilindro | $\pi r^2h$ (prisma circular) | $2\pi r^2+2\pi rh$ |
> | Cono | $\pi r^2h/3$ (pirámide circular) | $\pi r^2+\pi rg$ |
> | Esfera | $4\pi r^3/3$ (Pappus) | $4\pi r^2$ |
>
> **Euler verifica:** cubo $8-12+6=2$; pirámide cuadrada $5-8+5=2$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Pirámide sin $/3$:** siempre divide (cabe 3 veces en el prisma).
> - **$g=h$ en el cono:** generatriz $g=\sqrt{r^2+h^2}$ (hipotenusa, no altura).
> - **Esfera $V=4\pi r^2$:** eso es el área; el volumen lleva $r^3/3$.
> - **Euler en redondos:** $V-A+C$ es para poliedros (caras planas).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Euler en cubo y pirámide cuadrada.
> 2. Prisma $B=20,H=7$: $V$.
> 3. Esfera $r=2$: $V$ y $A$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $8-12+6=2$; $5-8+5=2$.
>
> **2.** $140$.
>
> **3.** $32\pi/3$; $16\pi$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Pirámide $l=6,h=9$: $V$.
> 5. Cono $r=3,h=4$: $g$, $A$, $V$.
> 6. ¿Por qué solo 5 regulares?

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $108$.
>
> **5.** $g=5$; $A=24\pi$; $V=12\pi$.
>
> **6.** Suma de ángulos en vértice $<360°$ (3–5 triángulos, 3 cuadrados, 3 pentágonos).

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Esfera por Pappus (semicírculo girando).
> 8. Tronco de cono: $V$ restando conos.
> 9. $r$ con $A=V$ numéricamente en la esfera.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $A=\pi r^2/2$, $d=2\pi(4r/3\pi)$; $V=4\pi r^3/3$.
>
> **8.** $V_{grande}-V_{chico}$ (semejanza para $h$).
>
> **9.** $r=3$ (único positivo).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico Euler en 2 poliedros.
> - [ ] Calculo $V$ de prismas y esferas.
> - [ ] Distingo $g$ de $h$ en conos.
> - [ ] Nombro los 5 regulares.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo pirámides con $/3$.
> - [ ] Hallo $g,A,V$ de conos.
> - [ ] Justifico los 5 regulares.
> - [ ] Uso Cavalieri para prismas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Deduzco la esfera con Pappus.
> - [ ] Resto troncos por semejanza.
> - [ ] Resuelvo $A=V$ en esferas.
> - [ ] Verifico Euler en cualquiera.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de sólidos.
>
> [2] R. D. Swokowski, *Cálculo* — cap. de volúmenes.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Sistema tridimensional]] — base: coordenadas 3D.
> - [[04 - Poliedros y cuerpos redondos]] — siguiente: mixtos y aplicaciones.
> - [[07 - Perímetro y área de un polígono]] — bases poligonales.
> - [[10 - Figuras circulares]] — círculos que generan.

---

**Tags:** #geometria #poliedros #solidos #unidad5

---
dg-publish: true
---

# 🎨 Graficación Polar

## 🎯 Introducción

> [!info] 💡 ¿Cómo se grafica en polares?
>
> Identifica el tipo por la forma ($a\pm b\sin\theta$ cardioide, $a\sin n\theta$ rosa, $r^2=a^2\cos2\theta$ lemniscata), usa simetría para media tabla, marca ceros y máximos, y recuerda que $r<0$ dibuja opuesto.
>
> ```mermaid
> graph LR
>     A["Forma<br/>r=f(theta)"] --> B["Simetría<br/>media tabla"]
>     B --> C["Ceros y max<br/>puntos clave"]
>     C --> D["Une<br/>r neg opuesto"]
>     style A fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-galeria.png]]

> [!tip] 💡 Visual — Galería
>
> Cardioide $r=2-2\sin\theta$ (cúspide en $\pi/2$), rosa $r=3\sin2\theta$ (4 pétalos), lemniscata $r^2=9\cos2\theta$ (dos bucles), caracol $r=1+3\cos\theta$ (bucle interior) — las cuatro familias de un vistazo.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Familias y simetrías
>
> **Familias:** $r=a\pm b\cos\theta$ (cardioide si $a=b$, caracol si no); $r=a\cos n\theta$ (rosa: $2n$ pétalos si $n$ par, $n$ si impar); $r^2=a^2\cos2\theta$ (lemniscata, dos bucles).
>
> **Simetrías:** $r(-\theta)=r(\theta)$ eje polar; $r(\pi-\theta)$ eje $\pi/2$; $r(\theta+\pi)$ polo.

> [!tip] 💡 Cómo graficar rápido y bien
>
> Lee la familia antes de tabular — ya sabes la forma esperada. Tabula solo medio período usando simetría y marca primero ceros ($r=0$) y máximos ($|r|$ mayor): esos puntos mandan en el dibujo. Si aparece $r<0$, no lo borres: es el bucle interior o el pétalo opuesto.

> [!example] 🟢 Ejemplo — $r=2-2\sin\theta$ paso a paso
>
> Cardioide ($a=b=2$) hacia abajo; simétrica en $\pi/2$. Puntos: $\theta=0\to2$, $\pi/2\to0$ (origen), $\pi\to2$, $3\pi/2\to4$ (máximo). Une con forma de corazón.

---

## 📋 Tabla Comparativa: Familias

> [!note] 📋 Qué esperar de cada forma
>
> | Forma | Tipo | Pistas |
> |---|---|---|
> | $r=a\pm b\cos\theta$, $a=b$ | Cardioide | Cúspide en el polo |
> | $r=a\pm b\cos\theta$, $a<b$ | Caracol con bucle | $r=0$ tiene solución |
> | $r=a\pm b\cos\theta$, $a>b$ | Caracol sin bucle | $r>0$ siempre |
> | $r=a\cos n\theta$ | Rosa | $n$ par: $2n$; impar: $n$ pétalos |
> | $r^2=a^2\cos2\theta$ | Lemniscata | Solo donde $\cos2\theta\ge0$ |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$r<0$ descartado:** en $r=1+3\cos\theta$, $r=-2$ en $\pi$ es el bucle interior (punto $(2,0)$).
> - **Pétalos de más/menos:** $n$ par da $2n$; cuenta máximos de $|\sin n\theta|$, no ceros.
> - **Lemniscata en todo $\theta$:** solo existe donde $\cos2\theta\ge0$ (dos intervalos).
> - **Simetría sin verificar:** sustituye $r(-\theta)$ antes de asumir medio trabajo.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Grafica $r=2-2\sin\theta$ (tipo, simetría, 4 puntos).
> 2. Pétalos de $r=3\sin2\theta$ (ángulos y longitud).
> 3. Dominio de $r^2=9\cos2\theta$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Cardioide abajo; puntos $2,0,2,4$.
>
> **2.** $4$ pétalos en $\pi/4,3\pi/4,5\pi/4,7\pi/4$; longitud $3$.
>
> **3.** $[-\pi/4,\pi/4]\cup[3\pi/4,5\pi/4]$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Grafica $r=1+3\cos\theta$ (bucle: $\cos\theta=-1/3$).
> 5. Máxima extensión de la lemniscata $r^2=9\cos2\theta$.
> 6. Simetrías de $r=3\sin2\theta$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Bucle interior en $[1.911,4.372]$; máximo $4$ en $0$.
>
> **5.** $r=3$ en $\theta=0,\pi$.
>
> **6.** Eje $\pi/2$ y polo.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $n$ par $\to2n$ pétalos en $r=a\cos n\theta$.
> 8. Área de un pétalo de $r=3\sin2\theta$ ($\frac12\int_0^{\pi/2}9\sin^22\theta=9\pi/8$... verifica).
> 9. Transforma $r=2-2\sin\theta$ rotando $\pi/2$ (qué ecuación da).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $r(\theta+\pi)=-r(\theta)$ recorre los otros $n$ sin repetir.
>
> **8.** $9\pi/8$ por pétalo; total $9\pi/2$.
>
> **9.** $r=2-2\cos\theta$ (cardioide a la izquierda).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico familias por la forma.
> - [ ] Tabulo puntos clave (ceros y máximos).
> - [ ] Aplico simetrías para media tabla.
> - [ ] Interpreto $r<0$ correctamente.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Grafico caracoles con bucle interior.
> - [ ] Hallo dominios de lemniscatas.
> - [ ] Cuento pétalos según paridad de $n$.
> - [ ] Verifico simetrías sustituyendo.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro conteo de pétalos.
> - [ ] Calculo áreas por pétalo.
> - [ ] Transformo curvas por rotación.
> - [ ] Predigo la forma antes de tabular.

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
> - [[02 - Coordenadas polares]] — conversión y áreas.
> - [[06 - Caracoles en coordenadas polares]] — familias a fondo.
> - [[06 - Caracoles en coordenadas polares]] — caracoles a fondo.


---

**Tags:** #polares #graficacion #cardioide #rosa #unidad6

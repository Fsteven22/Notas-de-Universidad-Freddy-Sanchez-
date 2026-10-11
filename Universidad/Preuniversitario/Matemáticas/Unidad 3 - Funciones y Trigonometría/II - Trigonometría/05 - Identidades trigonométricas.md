---
dg-publish: true
---

# 🧮 Identidades Trigonométricas

## 🎯 Introducción

> [!info] 💡 ¿Qué son las identidades trigonométricas?
>
> Igualdades que valen para todo $\theta$: pitagóricas ($\sin^2+\cos^2=1$), suma ($\sin(A+B)$), doble ($\sin2\theta=2\sin\theta\cos\theta$) y mitad. Demostrar es reducir un lado al otro.
>
> ```mermaid
> graph LR
>     A["Pitagórica<br/>base"] --> B["Suma<br/>A+B"]
>     B --> C["Doble<br/>2t"]
>     C --> D["Mitad<br/>t/2"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Las cuatro familias
>
> **Pitagóricas:** $\sin^2+\cos^2=1$, $\tan^2+1=\sec^2$. **Suma:** $\sin(A\pm B)$, $\cos(A\pm B)$, $\tan(A+B)=(\tan A+\tan B)/(1-\tan A\tan B)$.
>
> **Doble:** $\sin2\theta=2\sin\theta\cos\theta$, $\cos2\theta=\cos^2-\sin^2$. **Mitad:** $\sin^2(\theta/2)=(1-\cos\theta)/2$.

> [!tip] 💡 Cómo demostrar identidades sin perderse
>
> Trabaja un solo lado (el más complicado) hacia el otro: factoriza, pasa a $\sin/\cos$ o busca pitagóricas escondidas. Para valores exactos parte el ángulo en notables ($75°=45°+30°$); para dobles con un dato, halla primero el compañero ($\sin=3/5\therefore\cos=4/5$).

> [!example] 🟢 Ejemplo — $\sin75°$ y $\sin2\theta$ con $\sin=3/5$
>
> $\sin(45+30)=\sin45\cos30+\cos45\sin30=(\sqrt6+\sqrt2)/4$. $\sin2\theta=2(3/5)(4/5)=24/25$, $\cos2\theta=7/25$.

---

## 📋 Tabla Comparativa: Identidades

> [!note] 📋 Qué fórmula usar y cuándo
>
> | Familia | Fórmula | Uso |
> |---|---|---|
> | Pitagórica | $\sin^2+\cos^2=1$ | Halla el compañero |
> | Suma | $\sin(A+B)$ | Parte en notables |
> | Doble | $\sin2\theta=2\sin\theta\cos\theta$ | Duplica datos |
> | Mitad | $\cos^215°=(2+\sqrt3)/4$ | Ángulos mitad |
> | Producto | $\sin A\cos B=[\sin(A+B)+\sin(A-B)]/2$ | Suma/resta fórmulas |
>
> **Cociente útil:** $\sin2x/(1+\cos2x)=\tan x$ (usa $2\sin x\cos x/2\cos^2x$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$\sin(A+B)=\sin A+\sin B$:** falso (usa la fórmula completa).
> - **Signo de $\cos(A-B)$:** es $\cos A\cos B+\sin A\sin B$ ($+$).
> - **$\cos2\theta$ con una forma:** tiene tres ($\cos^2-\sin^2$, $1-2\sin^2$, $2\cos^2-1$).
> - **Mitad sin $\pm$:** $\sin(\theta/2)=\pm\sqrt{(1-\cos\theta)/2}$ (cuadrante manda).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Verifica $\sin^230°+\cos^230°=1$.
> 2. $\sin75°$ con $45+30$.
> 3. $\sin15°$ con $45-30$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $1/4+3/4=1$.
>
> **2.** $(\sqrt6+\sqrt2)/4$.
>
> **3.** $(\sqrt6-\sqrt2)/4$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Simplifica $(\sin\theta+\cos\theta)^2$.
> 5. $\cos^215°$ con mitad.
> 6. Si $\sin\theta=3/5$: $\sin2\theta,\cos2\theta$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $1+\sin2\theta$.
>
> **5.** $(2+\sqrt3)/4$.
>
> **6.** $24/25,7/25$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $\sin3\theta=3\sin\theta-4\sin^3\theta$.
> 8. Simplifica $\sin2x/(1+\cos2x)$.
> 9. Halla $\tan(\pi/8)$ con mitad.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\sin(2\theta+\theta)$ expandido.
>
> **8.** $\tan x$.
>
> **9.** $\sqrt2-1$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Verifico la pitagórica con valores.
> - [ ] Parto ángulos en notables.
> - [ ] Aplico doble con datos.
> - [ ] Uso $\tan^2+1=\sec^2$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Simplifico cuadrados de sumas.
> - [ ] Deduzco $\tan(A+B)$.
> - [ ] Aplico mitad a $15°$.
> - [ ] Verifico formas $\sin^2$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro suma con Euler.
> - [ ] Expando $\sin3\theta$.
> - [ ] Convierto productos en sumas.
> - [ ] Hallo $\tan(\pi/8)$ exacto.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 5 (identidades).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de trigonometría.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Funciones trigonométricas elementales]] — base: valores y fundamental.
> - [[02 - Operaciones]] — De Moivre y Euler.
> - [[03 - Gráficas de funciones trigonométricas]] — suma a seno único.
> - [[06 - Ecuaciones e inecuaciones trigonométricas]] — siguiente: ecuaciones.

---

**Tags:** #trigonometria #identidades #doble #unidad3

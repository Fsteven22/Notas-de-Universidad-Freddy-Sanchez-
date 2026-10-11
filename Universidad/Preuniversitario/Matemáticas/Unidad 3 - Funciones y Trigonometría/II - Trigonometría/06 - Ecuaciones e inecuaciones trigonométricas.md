---
dg-publish: true
---

# ⚖️ Ecuaciones e Inecuaciones Trigonométricas

## 🎯 Introducción

> [!info] 💡 ¿Cómo se resuelven ecuaciones trigonométricas?
>
> Referencia + cuadrantes dan las soluciones base, $+2k\pi$ las generaliza; factorizar o usar identidades reduce las demás a básicas. Al elevar al cuadrado verifica extrañas.
>
> ```mermaid
> graph LR
>     A["Referencia<br/>cuadrantes"] --> B["Base<br/>[0,2pi)"]
>     B --> C["General<br/>+2kpi"]
>     C --> D["Verifica<br/>extrañas"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Solución base, general e inecuación
>
> **Base:** soluciones en $[0,2\pi)$ (una o dos por valor). **General:** $+2k\pi$ ($+k\pi$ en $\tan$).
>
> **Métodos:** factoriza ($\sin2x=\cos x\therefore\cos x(2\sin x-1)=0$), sustituye ($y=\sin x$), eleva y verifica. **Inecuación:** arco solución $+$ período.

> [!tip] 💡 Cómo no perder soluciones ni crear falsas
>
> Dibuja el círculo y marca todos los cortes antes de escribir — $\sin x=1/2$ tiene dos ($\pi/6,5\pi/6$), no uno. Si elevas al cuadrado ($\sin x+\cos x=1$), sustituye cada candidata: $x=\pi$ da $-1\neq1$ y se descarta.

> [!example] 🟢 Ejemplo — $2\sin^2x-\sin x-1=0$
>
> $(2\sin x+1)(\sin x-1)=0\therefore\sin x=1$ ($x=\pi/2+2k\pi$) o $\sin x=-1/2$ ($7\pi/6,11\pi/6+2k\pi$).

---

## 📋 Tabla Comparativa: Ecuaciones Base

> [!note] 📋 Qué soluciones salen en $[0,2\pi)$
>
> | Ecuación | Soluciones | General |
> |---|---|---|
> | $\sin x=1/2$ | $\pi/6,5\pi/6$ | $+2k\pi$ |
> | $\sin x=-1/2$ | $7\pi/6,11\pi/6$ | $+2k\pi$ |
> | $\cos x=0$ | $\pi/2,3\pi/2$ | $+k\pi$ |
> | $\tan x=1$ | $\pi/4,5\pi/4$ | $+k\pi$ |
> | $\cos x=1$ | $0$ | $2k\pi$ |
>
> **Inecuación:** $\sin x>1/2\therefore(\pi/6+2k\pi,5\pi/6+2k\pi)$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Una sola solución:** $\sin$ y $\cos$ dan dos por valor (salvo extremos).
> - **$+2k\pi$ en $\tan$:** es $+k\pi$ (período $\pi$).
> - **Extrañas sin verificar:** elevar crea falsas ($x=\pi$ en $\sin+\cos=1$).
> - **$\sin3x=\sin x\to x=k\pi/2$:** $\pi/2$ falla; son $x=k\pi$ o $\pi/4+k\pi/2$.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $\sin x=1/2$ en $[0,2\pi)$.
> 2. $\cos x=0$ en $[0,2\pi)$.
> 3. $\tan x=1$ en $[0,2\pi)$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $\pi/6,5\pi/6$.
>
> **2.** $\pi/2,3\pi/2$.
>
> **3.** $\pi/4,5\pi/4$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $2\sin^2x-\sin x-1=0$ general.
> 5. $\sin x>1/2$ general.
> 6. $\sin2x=\cos x$ (factoriza).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\pi/2+2k\pi$; $7\pi/6,11\pi/6+2k\pi$.
>
> **5.** $(\pi/6+2k\pi,5\pi/6+2k\pi)$.
>
> **6.** $\cos x=0$ o $\sin x=1/2$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $\sin x+\cos x=1$ (verifica extrañas).
> 8. $\cos x\le-1/2$ general.
> 9. $\sin3x=\sin x$ completo.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $2k\pi,\pi/2+2k\pi$ ($\pi$ se descarta).
>
> **8.** $[2\pi/3+2k\pi,4\pi/3+2k\pi]$.
>
> **9.** $x=k\pi$ o $x=\pi/4+k\pi/2$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo soluciones base con referencia.
> - [ ] Generalizo con $+2k\pi$ ($+k\pi$ en $\tan$).
> - [ ] Resuelvo $\sin,\cos,\tan$ básicas.
> - [ ] Verifico sustituyendo.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Factorizo con ángulo doble.
> - [ ] Resuelvo cuadráticas en $\sin x$.
> - [ ] Hallo arcos de inecuaciones.
> - [ ] Sustituyo $2x$ como bloque.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Descarto extrañas al elevar.
> - [ ] Resuelvo $\sin3x=\sin x$ completo.
> - [ ] Acoto rangos con desigualdades.
> - [ ] Demuestro cotas con derivadas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 5 (ecuaciones trig).
>
> [2] A. Baldor, *Geometría*, 2da ed., Patria — cap. de trigonometría.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[02 - Funciones trigonométricas elementales]] — base: valores.
> - [[05 - Identidades trigonométricas]] — factoriza con doble.
> - [[13 - Funciones exponenciales]] — inecuaciones análogas.
> - [[04 - Funciones trigonométricas inversas]] — ángulo principal.

---

**Tags:** #trigonometria #ecuaciones #inecuaciones #unidad3

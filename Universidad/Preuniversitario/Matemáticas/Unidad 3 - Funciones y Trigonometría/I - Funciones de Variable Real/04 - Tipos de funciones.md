---
dg-publish: true
---

# 🏷️ Tipos de Funciones

## 🎯 Introducción

> [!info] 💡 ¿Cómo se clasifican las funciones?
>
> Por **fórmula** (algebraicas vs trascendentes) y por **comportamiento** (inyectiva, sobreyectiva, par/impar, periódica, monótona): la prueba horizontal decide inyectividad y $f(-x)$ la paridad.
>
> ```mermaid
> graph LR
>     A["Fórmula<br/>alg o trasc"] --> B["Inyectiva<br/>horiz"]
>     B --> C["Par/impar<br/>f(-x)"]
>     C --> D["Periódica<br/>monótona"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Familias y propiedades
>
> **Algebraicas:** polinómicas, racionales, radicales. **Trascendentes:** exponencial, logaritmo, trigonométricas.
>
> **Inyectiva:** $f(a)=f(b)\implies a=b$. **Sobreyectiva:** $\text{Ran}=C$. **Par:** $f(-x)=f(x)$; **impar:** $f(-x)=-f(x)$. **Periódica:** $f(x+T)=f(x)$.

> [!tip] 💡 Cómo clasificar sin dudar
>
> Primero mira la fórmula (¿hay $x$ en exponente? trascendente). Luego prueba horizontal para inyectividad — si alguna recta $y=b$ corta dos veces, no es inyectiva. La paridad sale de $f(-x)$: si vuelve lo mismo es par, si cambia todo de signo es impar; $x\sin x$ da $(-x)(-\sin x)=x\sin x\therefore$ **par**.

> [!example] 🟢 Ejemplo — $f(x)=x/(x^2+1)$
>
> $f(-x)=-f(x)\therefore$ impar; $|f|\le1/2$ (máximo en $x=\pm1$); $f(2)=f(1/2)=2/5\therefore$ no inyectiva.

---

## 📋 Tabla Comparativa: Propiedades Típicas

> [!note] 📋 Qué propiedad tiene cada función
>
> | Función | Inyectiva | Par/impar | Período |
> |---|---|---|---|
> | $2x+1$ | Sí (biyectiva) | Ninguna | No |
> | $x^2$ ($\mathbb{R}$) | No | Par | No |
> | $x^3$ | Sí (biyectiva) | Impar | No |
> | $e^x$ | Sí (no sobre en $\mathbb{R}$) | Ninguna | No |
> | $\sin x$ | No | Impar | $2\pi$ |
> | $x\sin x$ | No | **Par** | No |
>
> **Crecimiento:** $2^x$ supera a $x^2$ desde $x=5$ ($32>25$) y diverge.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$x\sin x$ impar:** $(-x)\sin(-x)=x\sin x\therefore$ par.
> - **Periódica inyectiva:** si repite valores, no es inyectiva (salvo constante en un punto).
> - **$x^2$ inyectiva:** solo restringida ($[2,\infty)$ con vértice en $2$ sí).
> - **Constante periódica:** todo $T$ sirve, pero no es inyectiva.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Clasifica: $3x^2+1$, $1/(x+1)$, $\sqrt{x}$, $2^x$, $\ln x$, $\sin x$.
> 2. Inyectiva/sobreyectiva: $2x+1$, $x^2$, $e^x$ ($\mathbb{R}\to\mathbb{R}$).
> 3. Período de $\sin x$, $\cos2x$, constante.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** Pol, rac, radical, exp, log, trig.
>
> **2.** Biyectiva; ninguna; inyectiva no sobre.
>
> **3.** $2\pi$, $\pi$, todo $T$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Prueba $x^3$ biyectiva y halla inversa.
> 5. $x^2-4x+3$ en $[2,\infty)$: ¿inyectiva?
> 6. Clasifica $x/(x^2+1)$ completa.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Estricta creciente $\therefore\sqrt[3]{x}$.
>
> **5.** Sí (vértice $x=2$, crece).
>
> **6.** Impar, $|f|\le1/2$, no inyectiva.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Continua inyectiva en intervalo $\therefore$ estrictamente monótona (prueba).
> 8. $f$ par y periódica no constante: ¿inyectiva?
> 9. Dirichlet: ¿inyectiva? ($D(0)=D(1)=1$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Por valor intermedio (si sube y baja, repite).
>
> **8.** No (periódica repite).
>
> **9.** No.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Clasifico por fórmula (6 familias).
> - [ ] Decido inyectividad con prueba horizontal.
> - [ ] Hallo paridad con $f(-x)$.
> - [ ] Identifico períodos básicos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Pruebo biyectividad y hallo inversas.
> - [ ] Restringo dominios para inyectividad.
> - [ ] Comparo crecimientos exp vs pol.
> - [ ] Clasifico racionales completas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro monotonía desde inyectividad.
> - [ ] Refuto inyectividad con contraejemplos.
> - [ ] Analizo paridad de productos.
> - [ ] Parametrizo biyectividad ($ax^3$, $a\neq0$).

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 2 (funciones).
>
> [2] K. Rosen, *Matemática Discreta*, McGraw-Hill — §2.3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[10 - Funciones en Conjuntos]] — inyectiva/sobreyectiva general.
> - [[10 - Función inversa de una función biyectiva]] — inversas a fondo.
> - [[05 - Función lineal]] — ejemplo biyectivo.
> - [[02 - Funciones trigonométricas elementales]] — periódicas.

---

**Tags:** #funciones #tipos #inyectiva #paridad #unidad3

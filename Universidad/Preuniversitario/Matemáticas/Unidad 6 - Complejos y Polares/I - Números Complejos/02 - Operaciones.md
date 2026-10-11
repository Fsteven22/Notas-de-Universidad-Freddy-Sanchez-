---
dg-publish: true
---

# ⚙️ Operaciones con Complejos

## 🎯 Introducción

> [!info] 💡 ¿Cómo se opera con complejos?
>
> Binómica para sumar/restar por componentes; **polar** para multiplicar (módulos $\times$, ángulos $+$) con De Moivre $z^n=r^n(\cos n\theta+i\sin n\theta)$; Euler $re^{i\theta}$ para dividir y raíces $n$-ésimas.
>
> ```mermaid
> graph LR
>     A["Binómica<br/>a+bi"] --> B["Polar<br/>r ang t"]
>     B --> C["De Moivre<br/>r n ang nt"]
>     C --> D["Euler<br/>r e it"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-demoivre.png]]

> [!tip] 💡 Visual — Potencias $(1+i)^k$
>
> Cada potencia gira $45°$ y escala $\sqrt2$: multiplicar es **rotar + dilatar** — por eso De Moivre convierte potencias en multiplicar el ángulo.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Las cuatro operaciones y De Moivre
>
> **Suma/resta:** $(a+bi)\pm(c+di)=(a\pm c)+(b\pm d)i$. **Producto:** distribuye con $i^2=-1$. **Cociente:** multiplica por el conjugado.
>
> **Polar:** $r_1r_2\angle(\theta_1+\theta_2)$; **De Moivre:** $z^n=r^n(\cos n\theta+i\sin n\theta)$; **Euler:** $re^{i\theta}$.

> [!tip] 💡 Cómo elegir la forma antes de calcular
>
> Sumas, restas y fracciones con binomios chicos → binómica con conjugado. Potencias grandes, productos encadenados o raíces → pasa a polar primero (el ángulo manda). Si el exponente es múltiplo de $4$ en $i$, reduce módulo $4$ antes de cualquier otra cosa.

> [!example] 🟢 Ejemplo — $(1-\sqrt3\,i)^{10}$ con De Moivre
>
> $r=2$, $\theta=-\pi/3$; $z^{10}=2^{10}(\cos(-10\pi/3)+i\sin(-10\pi/3))=1024(\cos(2\pi/3)+i\sin(2\pi/3))=-512+512\sqrt3\,i$.

---

## 📋 Tabla Comparativa: Formas para Operar

> [!note] 📋 Qué forma conviene según la operación
>
> | Operación | Mejor forma | Regla |
> |---|---|---|
> | **Sumar/restar** | Binómica | Componente a componente |
> | **Multiplicar** | Polar | Módulos $\times$, ángulos $+$ |
> | **Dividir** | Polar o conjugado | Módulos $\div$, ángulos $-$ |
> | **Potencia** | De Moivre | $r^n$, ángulo $\times n$ |
> | **Raíz $n$-ésima** | Euler | $n$ raíces separadas $2\pi/n$ |
>
> **Fracción mixta:** $[(2+3i)(1-i)]/[(3+i)(2-i)]=(5+i)/(7-i)=17/25+(6/25)i$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Ángulos multiplicados al sumar:** en binómica se suman componentes, no ángulos.
> - **De Moivre sin normalizar $\theta$:** reduce el ángulo final módulo $2\pi$ (p. ej. $-10\pi/3\to2\pi/3$).
> - **Raíces únicas:** $z^{1/n}$ tiene **$n$** valores distintos.
> - **$(1+i)^4$ expandiendo:** usa $(1+i)^2=2i\therefore(2i)^2=-4$ (más rápido y seguro).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Simplifica $[(2+3i)(1-i)]/[(3+i)(2-i)]$.
> 2. $(1+i)(1+i^2)(1+i^4)(1+i^8)$.
> 3. $1/(1+1/(1+1/(1+i)))$ de adentro hacia afuera.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(5+i)/(7-i)=17/25+(6/25)i$.
>
> **2.** $(1+i)(0)(2)(2)=0$.
>
> **3.** $8/13-(1/13)i$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $(1-\sqrt3\,i)^{10}$ con De Moivre.
> 5. Resuelve $z^2+(1-i)z-6-3i=0$ (discriminante $24+10i=(5+i)^2$).
> 6. Cociente $(3+2i)/(1-4i)$ en polar (módulos y ángulo).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $-512+512\sqrt3\,i$.
>
> **5.** $z_1=2+i$, $z_2=-3$ (verifica sustituyendo).
>
> **6.** $r=\sqrt{13/17}=\sqrt{221}/17$, $\theta=\arctan(2/3)+\arctan(4)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Halla las $3$ raíces cúbicas de $8$ y dibújalas (triángulo equilátero).
> 8. Prueba $|z_1z_2|=|z_1||z_2|$ con $z\bar z=|z|^2$.
> 9. Suma geométrica: interpreta $(2+3i)+(−1+2i)$ como paralelogramo.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $2$, $2\angle120°$, $2\angle240°$.
>
> **8.** $|z_1z_2|^2=z_1z_2\bar z_1\bar z_2=|z_1|^2|z_2|^2$.
>
> **9.** $1+5i$ (punta del paralelogramo).

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Multiplico y divido en binómica con conjugado.
> - [ ] Simplifico fracciones mixtas paso a paso.
> - [ ] Reduzco potencias de $i$ módulo $4$.
> - [ ] Opero de adentro hacia afuera en fracciones iteradas.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico De Moivre a potencias grandes.
> - [ ] Resuelvo cuadráticas complejas con discriminante.
> - [ ] Paso a polar para multiplicar y dividir.
> - [ ] Verifico soluciones sustituyendo.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Hallo raíces $n$-ésimas completas ($n$ valores).
> - [ ] Demuestro $|z_1z_2|=|z_1||z_2|$.
> - [ ] Interpreto productos como rotación + escala.
> - [ ] Uso Euler para simplificar cocientes.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. D. Swokowski, *Álgebra y Trigonometría* — cap. de complejos.
>
> [2] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de imaginarios.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Definición y representación geométrica]] — base binómica y Argand.
> - [[02 - Coordenadas polares]] — $r,\theta$ como sistema.
> - [[10 - Ecuaciones]] — cuadráticas con discriminante negativo.
> - [[06 - Ecuaciones e inecuaciones trigonométricas]] — ángulos de De Moivre.

---

**Tags:** #complejos #demoivre #euler #operaciones #unidad6

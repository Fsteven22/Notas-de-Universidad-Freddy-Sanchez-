---
dg-publish: true
---

# ℂ Números Complejos: Definición

## 🎯 Introducción

> [!info] 💡 ¿Qué es un número complejo?
>
> $z=a+bi$ con $i^2=-1$: punto $(a,b)$ del plano complejo (Argand). Suma/resta son vectoriales, el producto usa $i^2=-1$ y el conjugado $\bar z=a-bi$ da el módulo $|z|=\sqrt{a^2+b^2}$.
>
> ```mermaid
> graph LR
>     A["z=a+bi<br/>punto (a,b)"] --> B["Conjugado<br/>a-bi"]
>     B --> C["Módulo<br/>raiz(a2+b2)"]
>     C --> D["Polar<br/>r(cos+isen)"]
>     style A fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U6-argand.png]]

> [!tip] 💡 Visual — $z=3+2i$
>
> Vector $(3,2)$ con $r=\sqrt{13}$; su conjugado $(3,-2)$ es el reflejo en el eje real — la suma $z+\bar z=6$ cae sobre el eje real.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Complejo, conjugado y módulo
>
> **Complejo:** $z=a+bi$, $a=\text{Re}(z)$, $b=\text{Im}(z)$, $i^2=-1$. **Igualdad:** parte real e imaginaria iguales.
>
> **Conjugado:** $\bar z=a-bi$. **Módulo:** $|z|=\sqrt{a^2+b^2}$. **Propiedades:** $z\bar z=|z|^2$, $z+\bar z=2a$, $z-\bar z=2bi$.

> [!tip] 💡 Cómo operar sin enredarse con $i$
>
> Suma y resta por componentes como vectores; en el producto distribuye y sustituye **solo al final** $i^2=-1$. Para dividir, multiplica arriba y abajo por el conjugado del denominador — el denominador se vuelve real ($|z|^2$) y todo se simplifica.

> [!example] 🟢 Ejemplo — $z_1=3+2i$, $z_2=1-4i$
>
> Suma $4-2i$; resta $2+6i$; producto $3-12i+2i-8i^2=11-10i$. Cociente: $[(3+2i)(1+4i)]/17=(-5+14i)/17$ (verifica $1^2+4^2=17$ ✓).

---

## 📋 Tabla Comparativa: Formas de $z$

> [!note] 📋 Qué forma usar y cuándo
>
> | Forma | Expresión | Ideal para |
> |---|---|---|
> | **Binómica** | $a+bi$ | Sumar, restar |
> | **Polar** | $r(\cos\theta+i\sin\theta)$ | Multiplicar, potencias |
> | **Exponencial** | $re^{i\theta}$ | Euler, raíces |
> | **Vector** | $(a,b)$ en Argand | Suma geométrica |
>
> **Potencias de $i$:** $i^{23}=i^3=-i$ (divide el exponente entre $4$ y quédate con el resto).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$i^2=+1$:** es $-1$; el error contamina todo el producto.
> - **Dividir sin conjugado:** siempre multiplica por el conjugado del denominador.
> - **$\theta=\arctan(b/a)$ a ciegas:** ajusta el cuadrante (II: $\pi-\alpha$, III: $\pi+\alpha$).
> - **$|z|=a+b$:** el módulo es $\sqrt{a^2+b^2}$, no la suma.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $z_1=3+2i$, $z_2=1-4i$: suma, resta, producto, cociente.
> 2. Simplifica $i^{23}$, $i^{-10}$, $(1+i)^4$.
> 3. $z=3-4i$: $\bar z$, $|z|$, $z\bar z$, $z+\bar z$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $4-2i$; $2+6i$; $11-10i$; $(-5+14i)/17$.
>
> **2.** $-i$; $-1$; $-4$ (vía $(2i)^2$).
>
> **3.** $3+4i$; $5$; $25$; $6$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Polar de $1+i$, $-\sqrt3+i$, $-2i$.
> 5. Representa $2+3i$, $-1+2i$, $3-i$ y su suma (paralelogramo).
> 6. Resuelve $x^2+4=0$ en $\mathbb{C}$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $\sqrt2\angle45°$; $2\angle150°$; $2\angle(-90°)$.
>
> **5.** Suma $1+5i$ (punta del paralelogramo).
>
> **6.** $x=\pm2i$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $z\bar z=|z|^2$ y deduce la fórmula del inverso $z^{-1}=\bar z/|z|^2$.
> 8. Halla $\sqrt{i}$ resolviendo $(a+bi)^2=i$.
> 9. Describe $|z-1|=2$ geométricamente (círculo centro $(1,0)$, $r=2$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $(a+bi)(a-bi)=a^2+b^2$; $z\cdot(\bar z/|z|^2)=1$.
>
> **8.** $a^2-b^2=0$, $2ab=1\therefore\pm(1+i)/\sqrt2$.
>
> **9.** Círculo: puntos a distancia $2$ de $(1,0)$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Opero suma, resta y producto con $i^2=-1$.
> - [ ] Divido usando el conjugado.
> - [ ] Calculo $\bar z$ y $|z|$ de memoria.
> - [ ] Simplifico potencias de $i$ con módulo $4$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Convierto binómica a polar con cuadrante.
> - [ ] Represento sumas como paralelogramos.
> - [ ] Resuelvo cuadráticas con discriminante negativo.
> - [ ] Verifico $z\bar z=|z|^2$.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Deduzco el inverso desde el conjugado.
> - [ ] Hallo raíces cuadradas de complejos.
> - [ ] Interpreto $|z-a|=r$ como círculos.
> - [ ] Conecto polar con trigonometría.

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
> - [[02 - Operaciones]] — producto, cociente y potencias a fondo.
> - [[10 - Ecuaciones]] — cuadráticas con discriminante negativo.
> - [[02 - Coordenadas polares]] — $r,\theta$ como coordenadas.
> - [[05 - Identidades trigonométricas]] — forma polar y De Moivre.

---

**Tags:** #complejos #argand #conjugado #unidad6

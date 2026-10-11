---
dg-publish: true
---

# 📊 Representación y Graficación

## 🎯 Introducción

> [!info] 💡 ¿Cómo se dibuja cualquier función?
>
> Puntos $(x,f(x))$ con esqueleto (interceptos, simetría, asíntotas) + checklist de 6 pasos + transformaciones $f(x-h)+k$: el esqueleto dice dónde, las transformaciones mueven el dibujo hecho.
>
> ```mermaid
> graph LR
>     A["Puntos<br/>(x,f(x))"] --> B["Esqueleto<br/>inter/sim/as"]
>     B --> C["Checklist<br/>6 pasos"]
>     C --> D["Transforma<br/>h,k"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Gráfica, checklist y transformaciones
>
> **Gráfica:** $G(f)=\{(x,f(x))\}$. **Interceptos:** $f(0)$ y $f(x)=0$. **Simetría:** par $f(-x)=f(x)$ (ahorra media tabla); impar origen.
>
> **Checklist:** dominio, interceptos, par/impar, asíntotas, monotonía/extremos, concavidad. **Transformaciones:** $f(x-h)$ derecha $h$ (signo contrario porque $x-h=0\iff x=h$); $+k$ arriba; $-f$ refleja $x$; $|f|$ dobla lo negativo; factor cancelado deja hueco ○.

> [!tip] 💡 Cómo bosquejar en orden
>
> Esqueleto primero (interceptos + asíntotas), simetría después (media tabla gratis), transformaciones al final sobre la base — no sobre la fórmula. Los dobleces ($|f|$) y huecos (○ en $(1,2)$ para $(x^2-1)/(x-1)$) se aplican a la gráfica terminada.

> [!example] 🟢 Ejemplo — $y=|x^2-4|$ y $(x-1)^2-4$
>
> Base $x^2-4$ (vértice $(0,-4)$, ceros $\pm2$); dobla lo negativo: W con $(0,4),(\pm2,0)$. $(x-1)^2-4$ es $x^2$ derecha $1$, abajo $4$ (vértice $(1,-4)$, ceros $-1,3$).

---

## 📋 Tabla Comparativa: Transformaciones

> [!note] 📋 Qué hace cada operación y por qué
>
> | Operación | Efecto (por qué) | Ejemplo |
> |---|---|---|
> | $f(x-h)$ | Derecha $h$ (cero en $x=h$) | $(x-2)^2$ |
> | $f(x)+k$ | Arriba $k$ (suma directa) | $\|x-2\|+1$ (V en $(2,1)$) |
> | $-f(x)$ | Refleja en $x$ (cambia signo $y$) | $-x^2$ abre abajo |
> | $af(x)$, $a>1$ | Estira (multiplica alturas) | $2x^2$ angosta |
> | $\|f(x)\|$ | Dobla lo bajo el eje | $\|x^2-4\|$ en W |
> | Cancela factor | Hueco ○ (punto ausente) | ○ en $(1,2)$ |
>
> **Oblicuas:** $(x^2-1)/x$ tiene $x=0$ y $y=x$ (divide: cociente $x$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$f(x+2)$ a la derecha:** a la izquierda (cero en $x=-2$).
> - **$\|f\|$ doblando lo positivo:** solo sube lo bajo el eje.
> - **Hueco ignorado:** $(x^2-1)/(x-1)$ es $y=x+1$ sin $(1,2)$.
> - **$(t^2,t)$ como $y(x)$:** $x$ repite con $\pm y$ (no función).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Interceptos de $2x+1$, $x^2-4$, $1/x$.
> 2. Par/impar: $x^2$, $x^3$, $x^2+x$, $|x|$.
> 3. $(x+2)^2-3$ desde $x^2$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $(0,1),(-1/2,0)$; $(0,-4),(\pm2,0)$; ninguno en $y$.
>
> **2.** Par, impar, ninguna, par.
>
> **3.** Izquierda $2$, abajo $3$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Asíntotas de $1/(x-2)$ y $(2x+1)/(x-1)$.
> 5. $2|x-1|+3$ desde $|x|$.
> 6. Hueco de $(x^2-1)/(x-1)$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $x=2,y=0$; $x=1,y=2$.
>
> **5.** Derecha $1$, estira $2$, sube $3$.
>
> **6.** $y=x+1$ con ○ en $(1,2)$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Bosqueja $(x^2-1)/x$ completo.
> 8. Concavidad de $x^3-3x$ e inflexión.
> 9. $e^{-x^2}$: paridad, máximo, asíntota.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Ceros $\pm1$; $x=0$; $y=x$; impar.
>
> **8.** $f''=6x$; $(0,0)$.
>
> **9.** Par; $(0,1)$; $y=0$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Hallo interceptos con ambos ejes.
> - [ ] Clasifico par/impar con $f(-x)$.
> - [ ] Aplico traslaciones con signo.
> - [ ] Leo $h,k$ directos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Hallo asíntotas verticales/horizontales.
> - [ ] Combino traslación + estiramiento.
> - [ ] Doblo negativos con $|f|$.
> - [ ] Marco huecos removibles.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Detecto oblicuas dividiendo.
> - [ ] Analizo concavidad con $f''$.
> - [ ] Decido paramétricas como funciones.
> - [ ] Bosquejo campanas exponenciales.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 2 (gráficas).
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. de funciones.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Definición, dominio y rango]] — base: dominio y vertical.
> - [[12 - Funciones racionales]] — siguiente: asíntotas y huecos.
> - [[04 - Tipos de funciones]] — inyectiva y horizontal.
> - [[07 - Función cuadrática]] — vértice y ceros.

---

**Tags:** #funciones #graficacion #transformaciones #unidad3

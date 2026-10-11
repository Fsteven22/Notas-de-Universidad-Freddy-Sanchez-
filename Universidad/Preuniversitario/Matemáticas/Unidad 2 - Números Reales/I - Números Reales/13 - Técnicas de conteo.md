---
dg-publish: true
---

# 🔢 Conteo y Binomio

## 🎯 Introducción

> [!info] 💡 ¿Cómo se cuenta y expande?
>
> $P(n,k)$ si importa el orden, $C(n,k)$ si no — y esos mismos $\binom{n}{k}$ son los coeficientes de $(a+b)^n$ (Pascal). Contar subconjuntos por tamaño suma $2^n$; expandir $(a+b)^n$ los usa como pesos.
>
> ```mermaid
> graph LR
>     A["Orden<br/>P o C"] --> B["Pascal<br/>binom"]
>     B --> C["Expande<br/>(a+b)n"]
>     C --> D["Suma filas<br/>2n"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[13-pascal.png]]

> [!tip] 💡 Visual — Pascal manda en ambos
>
> $\binom{5}{2}=4+6=10$ cuenta comités y a la vez es el coeficiente de $a^3b^2$ en $(a+b)^5$ — la misma tabla responde dos preguntas porque elegir posiciones de $b$ entre $5$ factores es un comité.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Conteo y teorema
>
> **$P(n,k)=n!/(n-k)!$** (orden: placas); **$C(n,k)=n!/k!(n-k)!$** (sin orden: comités). **Suma/resta:** disjuntos suman; con solape restan intersección.
>
> **Binomio:** $(a+b)^n=\sum_k\binom{n}{k}a^{n-k}b^k$ con $T_{k+1}=\binom{n}{k}a^{n-k}b^k$ (cuenta desde $k=0$: el tercer término usa $k=2$). **Corolarios:** fila suma $2^n$; alternada $0$.

> [!tip] 💡 Cómo elegir fórmula y término sin dudar
>
> Permutar dos elegidos ¿cambia algo? Placas sí ($P$), comités no ($C$). En $(x+1/x)^6$ el exponente es $6-2k$: iguala al buscado ($6-2k=2\therefore k=2\therefore\binom{6}{2}=15$). Con restricción posicional parte por el dígito fijo (pares: último $0$ da $504$, último $2,4,6,8$ da $1792$).

> [!example] 🟢 Ejemplo — $x^3$ en $(2x-1)^5$ y pares de 4 dígitos
>
> $T_4=\binom{5}{3}(2x)^3(-1)^2=80x^3$ (potencias $3+2=5$ ✓). Pares sin repetir: $504+1792=2296$.

---

## 📋 Tabla Comparativa: Conteo y Binomio

> [!note] 📋 Qué fórmula usar y por qué
>
> | Situación | Fórmula (por qué) | Resultado |
> |---|---|---|
> | Etapas | Producto (independientes) | Menú $72$ |
> | Orden importa | $P$ (permutar cambia) | Placas $26\cdot25\cdots$ |
> | Orden no | $C$ (permutar igual) | $C(6,3)=20$ |
> | "O" con solape | Resta intersección | $50+33-16=67$ |
> | Expandir | $\binom{n}{k}$ (elige posiciones) | $80x^3$ arriba |
> | Letras repetidas | Divide repeticiones | MATEMATICA $=151200$ |
>
> **Aproxima:** $(1.01)^{10}\approx1+0.1+0.0045=1.1045$ (3 términos bastan cerca de $0$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$P$ donde va $C$:** comités no ordenan (divide por $k!$).
> - **$T_3$ con $k=3$:** cuenta desde $0$ ($k=2$).
> - **MATEMATICA sin dividir $T$:** $10!/(3!2!2!)$ ($T\times2$ también repite).
> - **"O" sumando directo:** resta la intersección si se solapan.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $P(5,2)$, $C(5,2)$, $5!$.
> 2. Placas 3 letras + 3 dígitos sin repetir.
> 3. Expande $(x+1)^3$ y $(x-2)^2$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $20$; $10$; $120$.
>
> **2.** $26\cdot25\cdot24\cdot10\cdot9\cdot8$.
>
> **3.** $x^3+3x^2+3x+1$; $x^2-4x+4$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. 4 dígitos pares sin repetir.
> 5. Múltiplos de 2 o 3 hasta 100.
> 6. $x^2$ en $(x+1/x)^6$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $2296$.
>
> **5.** $67$.
>
> **6.** $\binom{6}{2}=15$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $\sum_k\binom{n}{k}=2^n$ por doble conteo.
> 8. MATEMATICA con repetidas.
> 9. $P(X=2)$ con $n=5,p=1/3$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** Por tamaño vs por inclusión.
>
> **8.** $151200$.
>
> **9.** $80/243$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo $P$ de $C$ por el orden.
> - [ ] Expando $(a+b)^n$ con Pascal.
> - [ ] Hallo $T_{k+1}$ contando desde $0$.
> - [ ] Multiplico etapas.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Parto por dígitos restringidos.
> - [ ] Resto intersecciones en "o".
> - [ ] Aíslo coeficientes de $x^m$.
> - [ ] Aproximo $(1+x)^n$ parcial.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro por doble conteo.
> - [ ] Divido por repeticiones.
> - [ ] Modelo binomiales $P(X=k)$.
> - [ ] Derivo $\sum k\binom{n}{k}=n2^{n-1}$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. Grimaldi, *Matemática Discreta*, Pearson — cap. de conteo.
>
> [2] K. Rosen, *Discrete Mathematics*, McGraw-Hill — §6.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[07 - Expresiones algebraicas]] — $(a+b)^4$ por binomio.
> - [[12 - Inducción matemática]] — prueba sumas binomiales.
> - [[01 - Tipos y cardinalidad]] — conteo infinito.
> - [[15 - Sucesiones]] — serie binomial.

---

**Tags:** #números-reales #conteo #binomio #unidad2

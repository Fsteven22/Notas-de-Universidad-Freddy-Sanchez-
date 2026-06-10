# 📝 Guía de Problemas 1 — Ejercicios Resueltos

> [!info]- 📌 Sobre esta guía
> 
> Ejercicios resueltos de la **Guía de Problemas 1** — Matemáticas Discretas (MATG1051). Autores de la guía: Cristhian Hernández, Ebner Pineda, Liliana Pérez, Jennifer Avilés.
> 
> |Sección|Tema|Ejercicios|
> |---|---|---|
> |1.1|Proposiciones, tablas de verdad y circuitos|1–6|
> |1.2|Condicionales y equivalencia lógica|7–12|
> |1.3|Demostraciones e inducción matemática|15–22|
> |1.4|Conjuntos, operaciones y demostraciones|23–28|

---

![[GUÍA 1 DE PROBLEMAS MD (1).pdf]]

## 🔌 1.1 — Proposiciones, Tablas de Verdad y Circuitos

> [!example]- 📝 Ejercicio 1 — Simplificación de circuito (3 entradas)
> 
> **Enunciado:** El circuito tiene entradas $p, q, r$ y salida $s$. Analizando la figura: NOT en $p$, NOT en $q$, NOT en $r$; luego tres AND: $(p \land q)$, $(\neg p \land r)$, $(\neg q \land r)$; y finalmente un OR de las tres salidas.
> 
> **Paso 1 — Expresión booleana del circuito original:**
> 
> $$s = (p \land q) \lor (\neg p \land r) \lor (\neg q \land r)$$
> 
> **Paso 2 — Simplificar:**
> 
> Agrupamos el factor común $r$ en los dos últimos términos:
> 
> $$s = (p \land q) \lor [r \land (\neg p \lor \neg q)]$$
> 
> Aplicamos De Morgan en el paréntesis: $\neg p \lor \neg q = \neg(p \land q)$:
> 
> $$s = (p \land q) \lor [r \land \neg(p \land q)]$$
> 
> Aplicamos absorción $A \lor (\neg A \land B) \equiv A \lor B$, con $A = (p \land q)$ y $B = r$:
> 
> $$\boxed{s = (p \land q) \lor r}$$
> 
> **Paso 3 — Circuito equivalente con 2 puertas:**
> 
> 1. **AND** entre $p$ y $q$ → produce $p \land q$.
> 2. **OR** entre el resultado anterior y $r$ → salida $s$.

> [!example]- 📝 Ejercicio 2 — Expresión booleana del circuito
> 
> **Enunciado:** Circuito con entradas $P, Q$ y compuertas AND, NOT, OR.
> 
> **Paso 1 — Leer el circuito (tres ramas hacia un OR final):**
> 
> - Rama 1: $P \land Q$ (AND directo)
> - Rama 2: NOT en $P$, luego AND con $Q$ → $\neg P \land Q$
> - Rama 3: NOT en $P$ y NOT en $Q$, luego AND → $\neg P \land \neg Q$
> 
> $$S = (P \land Q) \lor (\neg P \land Q) \lor (\neg P \land \neg Q)$$
> 
> **Paso 2 — Simplificar:**
> 
> Agrupamos factor común $\neg P$ en los dos últimos términos:
> 
> $$S = (P \land Q) \lor [\neg P \land (Q \lor \neg Q)]$$
> 
> Como $Q \lor \neg Q = 1$:
> 
> $$S = (P \land Q) \lor \neg P$$
> 
> Aplicamos absorción $\neg P \lor (P \land Q) \equiv \neg P \lor Q$:
> 
> $$\boxed{S = \neg P \lor Q}$$
> 
> **Paso 3 — Circuito equivalente con 2 puertas:**
> 
> 1. **NOT** en $P$ → $\neg P$.
> 2. **OR** entre $\neg P$ y $Q$ → salida $S$.

> [!example]- 📝 Ejercicio 3 — Expresión booleana y tabla de verdad
> 
> **Enunciado:** Circuito con entradas $x_1, x_2, x_3$.
> 
> **Paso 1 — Leer el circuito:**
> 
> - AND entre $x_1$ y $x_2$ → $x_1 \land x_2$
> - AND entre $x_1$ y $x_3$ → $x_1 \land x_3$, luego NOT → $\neg(x_1 \land x_3)$
> - OR de ambos → $(x_1 \land x_2) \lor \neg(x_1 \land x_3)$
> - NOT en $x_3$ → $\neg x_3$
> - AND final → $((x_1 \land x_2) \lor \neg(x_1 \land x_3)) \land \neg x_3$
> 
> **Paso 2 — Simplificar:**
> 
> Distribuimos el AND con $\neg x_3$:
> 
> $$= ((x_1 \land x_2) \land \neg x_3) \lor (\neg(x_1 \land x_3) \land \neg x_3)$$
> 
> Aplicamos De Morgan en el segundo término: $\neg(x_1 \land x_3) = \neg x_1 \lor \neg x_3$:
> 
> $$= (x_1 \land x_2 \land \neg x_3) \lor ((\neg x_1 \lor \neg x_3) \land \neg x_3)$$
> 
> Distribuimos $\neg x_3$ en el segundo término:
> 
> $$= (x_1 \land x_2 \land \neg x_3) \lor (\neg x_1 \land \neg x_3) \lor (\neg x_3 \land \neg x_3)$$
> 
> Idempotencia en el último término $(\neg x_3 \land \neg x_3 = \neg x_3)$:
> 
> $$= (x_1 \land x_2 \land \neg x_3) \lor (\neg x_1 \land \neg x_3) \lor \neg x_3$$
> 
> Factorizamos $\neg x_3$ en todos los términos (distributiva):
> 
> $$= \neg x_3 \land [1 \lor \neg x_1 \lor (x_1 \land x_2)] \quad \text{(distributiva)}$$
> 
> Como $1 \lor (\text{cualquier cosa}) = 1$ (dominación):
> 
> $$= \neg x_3 \land 1$$
> 
> Por identidad ($A \land 1 = A$):
> 
> Por tanto la expresión se reduce a:
> 
> $$\boxed{S = \neg x_3}$$
> 
> **Tabla de verdad:**
> 
> |$x_1$|$x_2$|$x_3$|$S = \neg x_3$|
> |---|---|---|---|
> |0|0|0|**1**|
> |0|0|1|0|
> |0|1|0|**1**|
> |0|1|1|0|
> |1|0|0|**1**|
> |1|0|1|0|
> |1|1|0|**1**|
> |1|1|1|0|
> 
> La salida es 1 únicamente cuando $x_3 = 0$, independientemente de $x_1$ y $x_2$.

> [!example]- 📝 Ejercicio 4 — Tabla de verdad, clasificación y simplificación
> 
> **Enunciado:** $[(p \to q) \land (\neg r \lor p)] \to (q \lor r)$
> 
> **(a) Tabla de verdad:**
> 
> Usando $p \to q \equiv \neg p \lor q$:
> 
> |$p$|$q$|$r$|$p \to q$|$\neg r \lor p$|$(p\to q)\land(\neg r\lor p)$|$q \lor r$|$s$|
> |---|---|---|---|---|---|---|---|
> |V|V|V|V|V|V|V|**V**|
> |V|V|F|V|V|V|V|**V**|
> |V|F|V|F|V|F|V|**V**|
> |V|F|F|F|V|F|F|**V**|
> |F|V|V|V|V|V|V|**V**|
> |F|V|F|V|F|F|V|**V**|
> |F|F|V|V|V|V|V|**V**|
> |F|F|F|V|F|F|F|**V**|
> 
> **(b) Clasificación:**
> 
> Todas las filas dan **Verdadero** → la proposición es una **tautología**. ✅
> 
> **(c) Simplificación algebraica:**
> 
> $$[(p \to q) \land (\neg r \lor p)] \to (q \lor r)$$ $$\equiv \neg[(p \to q) \land (\neg r \lor p)] \lor (q \lor r) \quad \text{(equiv. condicional)}$$ $$\equiv \neg[(\neg p \lor q) \land (\neg r \lor p)] \lor q \lor r \quad \text{(equiv. condicional)}$$
> 
> Si el antecedente es verdadero, entonces $(\neg p \lor q)$ y $(\neg r \lor p)$ son ambos verdaderos. Dos casos:
> 
> - Si $p = V$: de $\neg p \lor q$ obtenemos $q = V$, luego $q \lor r = V$.
> - Si $p = F$: de $\neg r \lor p = \neg r \lor F = \neg r$, necesitamos $r = F$. Pero entonces $q \lor r = q \lor F = q$. Y de $\neg p \lor q = T \lor q = T$, $q$ puede ser cualquier cosa — no fuerza que el antecedente sea verdadero a menos que lo sea.
> 
> En todos los casos el consecuente es verdadero o el antecedente es falso, por lo tanto es **tautología**. $\blacksquare$
> 
> **(d) Verificación:** La tabla confirma que $s = V$ en todas las filas. ✅

> [!example]- 📝 Ejercicio 5 — Valor lógico con valores asignados
> 
> **Enunciado:** $p = V$, $q = V$, $r = F$, $s = F$. Evaluar:
> 
> $$(\neg p \to q) \land (\neg r \lor s) \to (\neg s \to p) \land (p \land \neg s)$$
> 
> **Paso 1 — Calcular cada parte:**
> 
> |Subexpresión|Sustitución|Valor|
> |---|---|---|
> |$\neg p$|$\neg V$|$F$|
> |$\neg r$|$\neg F$|$V$|
> |$\neg s$|$\neg F$|$V$|
> |$\neg p \to q$|$F \to V$|$V$|
> |$\neg r \lor s$|$V \lor F$|$V$|
> |$\neg s \to p$|$V \to V$|$V$|
> |$p \land \neg s$|$V \land V$|$V$|
> 
> **Paso 2 — Combinar:**
> 
> - Antecedente: $(\neg p \to q) \land (\neg r \lor s) = V \land V = V$
> - Consecuente: $(\neg s \to p) \land (p \land \neg s) = V \land V = V$
> 
> $$V \to V = \boxed{V}$$
> 
> El valor lógico de la proposición es **Verdadero**.

> [!example]- 📝 Ejercicio 6 — Sistema de seguridad (bóveda)
> 
> **Enunciado:** Entradas $A$ (gerente), $B$ (subgerente), $C$ (supervisor). Reglas:
> 
> - $A = 1$ → acceso concedido, excepto si $A=B=C=1$ (coacción, bloqueo).
> - $A = 0$ → acceso solo si $B = 1$ y $C = 1$.
> 
> **(a) Tabla de verdad:**
> 
> |$A$|$B$|$C$|$Y$|Motivo|
> |---|---|---|---|---|
> |0|0|0|0|Ninguno autoriza|
> |0|0|1|0|Solo C|
> |0|1|0|0|Solo B|
> |0|1|1|1|B y C sin A|
> |1|0|0|1|Gerente presente|
> |1|0|1|1|Gerente presente|
> |1|1|0|1|Gerente presente|
> |1|1|1|0|Coacción — bloqueado|
> 
> **(b) Expresión lógica simplificada:**
> 
> Las filas con $Y = 1$ son: $(0,1,1)$, $(1,0,0)$, $(1,0,1)$, $(1,1,0)$.
> 
> Suma de minitérminos:
> 
> $$Y = (\neg A \land B \land C) \lor (A \land \neg B \land \neg C) \lor (A \land \neg B \land C) \lor (A \land B \land \neg C)$$
> 
> Agrupando las tres últimas (todas tienen $A = 1$ y no son $B=C=1$):
> 
> $$= (\neg A \land B \land C) \lor (A \land \neg(B \land C))$$ $$= (\neg A \land B \land C) \lor (A \land (\neg B \lor \neg C))$$
> 
> Factorizando con De Morgan:
> 
> $$\boxed{Y = (A \lor (B \land C)) \land \neg(A \land B \land C)}$$
> 
> Es decir: "acceso si el gerente está O si están B y C juntos, pero no los tres a la vez."
> 
> **(c) Circuito:**
> 
> ```
> B ─┐
>    AND ─────────────────────────────────┐
> C ─┘                                    OR ──┐
>                                         │    │
> A ──────────────────────────────────────┘    AND ── Y
>                                              │
> A ─┐                                         │
> B ─┤ AND ─┐                                  │
> C ─┘      NOT ──────────────────────────────┘
> ```
> 
> Puertas: AND (B,C) → OR con A → AND con NOT(A∧B∧C).

---

## 🔁 1.2 — Proposiciones Condicionales y Equivalencia Lógica

> [!example]- 📝 Ejercicio 7 — Recíproca, inversa y contrarrecíproca
> 
> **Variables:** $p$: "Obtengo el 10% de descuento en el impuesto predial." $q$: "Cancelo el impuesto predial en enero."
> 
> **Traducción:** "Obtengo el 10% de descuento, **dado que** cancelo en enero" → el "dado que" indica que $q$ es la condición:
> 
> $$q \to p$$
> 
> |Nombre|Formal|En lenguaje común|
> |---|---|---|
> |**Original**|$q \to p$|Si cancelo en enero, obtengo el 10% de descuento.|
> |**Recíproca**|$p \to q$|Si obtengo el 10% de descuento, entonces cancelé en enero.|
> |**Inversa**|$\neg q \to \neg p$|Si no cancelo en enero, no obtengo el 10% de descuento.|
> |**Contrarrecíproca**|$\neg p \to \neg q$|Si no obtengo el 10% de descuento, entonces no cancelé en enero.|
> 
> > [!tip] La original y la contrarrecíproca son **lógicamente equivalentes**. La recíproca y la inversa también son equivalentes entre sí.

> [!example]- 📝 Ejercicio 8 — Validez del razonamiento (lanchas)
> 
> **Proposiciones:**
> 
> - $p$: llueve. $q$: hay niebla. $r$: se realiza la carrera de lanchas. $s$: continúan las exhibiciones. $t$: se entrega el trofeo.
> 
> **Premisas formalizadas:**
> 
> 1. $(\neg p \lor \neg q) \to (r \land s)$
> 2. $r \to t$
> 3. $\neg t$
> 
> **Conclusión:** $p$
> 
> **Demostración:**
> 
> |Paso|Expresión|Justificación|
> |---|---|---|
> |1|$r \to t$|Premisa 2|
> |2|$\neg t$|Premisa 3|
> |3|$\neg r$|Modus Tollens (1, 2)|
> |4|$(\neg p \lor \neg q) \to (r \land s)$|Premisa 1|
> |5|$\neg(r \land s)$|De $\neg r$ (3)|
> |6|$\neg(\neg p \lor \neg q)$|Modus Tollens (4, 5)|
> |7|$p \land q$|De Morgan (6)|
> |8|$p$|Simplificación (7)|
> 
> El razonamiento es **válido**. $\blacksquare$

> [!example]- 📝 Ejercicio 9 — Validez del razonamiento (submarinistas)
> 
> **Proposiciones:**
> 
> - $a$: el mar está agitado. $t$: hay tormenta. $v$: la visibilidad es buena. $b$: bajaremos a 50m. $e$: somos submarinistas experimentados. $p$: los tiburones nos preocupan.
> 
> **Premisas:**
> 
> 1. $(\neg a \land \neg t) \to v$
> 2. $v \to b$
> 3. $e \to \neg p$
> 4. $e$
> 5. $\neg b \lor p$
> 
> **Conclusión:** $a \lor t$
> 
> **Demostración:**
> 
> |Paso|Expresión|Justificación|
> |---|---|---|
> |1|$e$|Premisa 4|
> |2|$e \to \neg p$|Premisa 3|
> |3|$\neg p$|Modus Ponens (1, 2)|
> |4|$\neg b \lor p$|Premisa 5|
> |5|$\neg b$|Resolución (3, 4): de $\neg p$ y $\neg b \lor p$ → $\neg b$|
> |6|$v \to b$|Premisa 2|
> |7|$\neg v$|Modus Tollens (5, 6)|
> |8|$(\neg a \land \neg t) \to v$|Premisa 1|
> |9|$\neg(\neg a \land \neg t)$|Modus Tollens (7, 8)|
> |10|$a \lor t$|De Morgan (9)|
> 
> El razonamiento es **válido**. $\blacksquare$

> [!example]- 📝 Ejercicio 10 — Validez del razonamiento (Juan y la procrastinación)
> 
> **Proposiciones:**
> 
> - $d$: acostumbra aplazar trabajos. $r$: es procrastinador. $v$: puede revisar sus trabajos. $b$: tiene buena nota. $j$: Juan.
> 
> **Premisas formalizadas:**
> 
> 1. $\forall x: d(x) \to r(x)$ — Quien aplaza es procrastinador.
> 2. $\forall x: r(x) \to \neg v(x)$ — Los procrastinadores no pueden revisar.
> 3. $\forall x: b(x) \to v(x)$ — Buena nota requiere revisar (contrarrecíproca: $\neg v(x) \to \neg b(x)$).
> 4. $d(j)$ — Juan aplaza.
> 
> **Conclusión:** $\neg b(j)$
> 
> **Demostración:**
> 
> |Paso|Expresión|Justificación|
> |---|---|---|
> |1|$d(j)$|Premisa 4|
> |2|$d(j) \to r(j)$|Premisa 1 (instancia Juan)|
> |3|$r(j)$|Modus Ponens (1, 2)|
> |4|$r(j) \to \neg v(j)$|Premisa 2 (instancia Juan)|
> |5|$\neg v(j)$|Modus Ponens (3, 4)|
> |6|$b(j) \to v(j)$|Premisa 3 (instancia Juan)|
> |7|$\neg b(j)$|Modus Tollens (5, 6)|
> 
> El razonamiento es **válido**. $\blacksquare$

> [!example]- 📝 Ejercicio 11 — Argumento con 5 premisas
> 
> **Premisas:**
> 
> 1. $\neg s \to \neg p$
> 2. $u$
> 3. $t \to \neg u$
> 4. $\neg p \to \neg(\neg q \land \neg r)$
> 5. $s \to t$
> 
> **Conclusión:** $\neg q \to r$
> 
> **Demostración:**
> 
> |Paso|Expresión|Justificación|
> |---|---|---|
> |1|$u$|Premisa 2|
> |2|$t \to \neg u$|Premisa 3|
> |3|$\neg t$|Modus Tollens (1, 2): $u$ y $t \to \neg u$ → $\neg t$|
> |4|$s \to t$|Premisa 5|
> |5|$\neg s$|Modus Tollens (3, 4)|
> |6|$\neg s \to \neg p$|Premisa 1|
> |7|$\neg p$|Modus Ponens (5, 6)|
> |8|$\neg p \to \neg(\neg q \land \neg r)$|Premisa 4|
> |9|$\neg(\neg q \land \neg r)$|Modus Ponens (7, 8)|
> |10|$q \lor r$|De Morgan (9)|
> |11|$\neg q \to r$|Equivalencia disyunción-condicional (10)|
> 
> El argumento es **válido**. $\blacksquare$

> [!example]- 📝 Ejercicio 12 — Argumento con 3 premisas
> 
> **Premisas:**
> 
> 6. $p \land q \to r$
> 7. $(p \to r) \to s$
> 8. $t \lor \neg q$
> 
> **Conclusión:** $q \to s \land t$
> 
> **Análisis — ¿Es válido?**
> 
> Supongamos $q = V$ e intentamos probar $s \land t$.
> 
> De premisa 3: $t \lor \neg q = t \lor F = t$, así que $t = V$. ✅
> 
> Ahora intentamos probar $s$. De premisa 2 necesitamos $p \to r$.
> 
> - Si $p = V$: de premisa 1, $p \land q = V \land V = V \to r$, así que $r = V$. Entonces $p \to r = V \to V = V$, y por premisa 2, $s = V$. ✅
> - Si $p = F$: $p \to r = F \to r = V$ siempre. Entonces por premisa 2, $s = V$. ✅
> 
> En ambos casos $s = V$ y $t = V$, por lo tanto $s \land t = V$.
> 
> El argumento es **válido**. $\blacksquare$

---

## 🔢 1.3 — Demostraciones e Inducción Matemática

> [!example]- 📝 Ejercicio 13 — Cuantificadores en $\mathbb{R} \times \mathbb{R}$
> 
> **Dominio:** $\mathbb{R} \times \mathbb{R}$
> 
> **(a) $\forall x \forall y\ (x^2 < y+1)$** — ❌ **Falso.** Contraejemplo: $x = 2, y = 0$: $4 < 1$. ✗
> 
> **(b) $\forall x \exists y\ (x^2 < y+1)$** — ✅ **Verdadero.** Para cualquier $x$, tomamos $y = x^2$: entonces $x^2 < x^2 + 1$. ✓
> 
> **(c) $\exists x \forall y\ (x^2 < y+1)$** — ❌ **Falso.** Para cualquier $x$ fijo, si tomamos $y = -x^2 - 1$, entonces $y+1 = -x^2 \leq 0 \leq x^2$. ✗
> 
> **(d) $\exists x \exists y\ (x^2 < y+1)$** — ✅ **Verdadero.** $x = 0, y = 0$: $0 < 1$. ✓
> 
> **(e) $\exists y \forall x\ (x^2 < y+1)$** — ❌ **Falso.** Para cualquier $y$ fijo, $x^2$ es no acotada. ✗
> 
> **(f) $\forall y \exists x\ (x^2 < y+1)$** — ❌ **Falso.** Para $y = -2$, necesitamos $x^2 < -1$, lo cual es imposible en $\mathbb{R}$ ya que $x^2 \geq 0$ siempre. ✗
> 
> **(g) $\forall x \forall y\ (x^2 + y^2 = 9)$** — ❌ **Falso.** $x=0, y=0$: $0 \neq 9$. ✗
> 
> **(h) $\forall x \exists y\ (x^2 + y^2 = 9)$** — ❌ **Falso.** Para $|x| > 3$ (por ejemplo $x = 4$), necesitaríamos $y^2 = 9 - 16 = -7$, sin solución real. ✗
> 
> **(i) $\exists x \forall y\ (x^2 + y^2 = 9)$** — ❌ **Falso.** Fijando $x$, $y^2 = 9-x^2$ es constante, no puede valer para todo $y$. ✗
> 
> **(j) $\exists x \exists y\ (x^2 + y^2 = 9)$** — ✅ **Verdadero.** $x=3, y=0$. ✓
> 
> **(k) $\forall x \forall y\ (x^2 + y^2 \geq 0)$** — ✅ **Verdadero.** Suma de cuadrados siempre es no negativa. ✓
> 
> **(l) $\forall x \exists y\ (x^2 + y^2 \geq 0)$** — ✅ **Verdadero.** Se sigue de (k). ✓
> 
> **(m) $\exists x \forall y\ (x^2 + y^2 \geq 0)$** — ✅ **Verdadero.** $x=0$: $y^2 \geq 0$ siempre. ✓
> 
> **(n) $\exists x \exists y\ (x^2 + y^2 \geq 0)$** — ✅ **Verdadero.** $x=0, y=0$: $0 \geq 0$. ✓
> 
> **(ñ) $\forall x \forall y\ ((x < y) \to (x^2 < y^2))$** — ❌ **Falso.** Contraejemplo: $x = -3, y = 1$: $-3 < 1$ pero $9 \not< 1$. ✗
> 
> **(o) $\forall x \exists y\ ((x < y) \to (x^2 < y^2))$** — ✅ **Verdadero.** Para cualquier $x$, tomamos $y = |x| + 1 > 0$ con $y > x$: entonces $y^2 > x^2$ si $y > |x|$. ✓
> 
> **(p) $\exists x \forall y\ ((x < y) \to (x^2 < y^2))$** — ✅ **Verdadero.** $x = 0$: si $0 < y$ entonces $y^2 > 0 = x^2$. ✓
> 
> **(q) $\exists x \exists y\ ((x < y) \to (x^2 < y^2))$** — ✅ **Verdadero.** $x=1, y=2$: $1 < 2$ y $1 < 4$. ✓

> [!example]- 📝 Ejercicio 14 — Valor lógico de proposiciones cuantificadas
> 
> **(a) $\exists x \in \mathbb{R} : 7 - 4x < 5 - 4x^2$**
> 
> $7 - 4x < 5 - 4x^2 \iff 4x^2 - 4x + 2 < 0 \iff 2(2x^2 - 2x + 1) < 0$
> 
> El discriminante de $2x^2 - 2x + 1$ es $4 - 8 = -4 < 0$ y coeficiente líder positivo, por lo que siempre es positivo. Entonces $2(2x^2-2x+1) > 0$ para todo $x$.
> 
> **Falso.** ❌
> 
> **(b) $\exists x > 0, \forall y \in \mathbb{R} : \dfrac{5y^2 - 2}{1 + 7y^2} < 9x$**
> 
> Analizamos $f(y) = \dfrac{5y^2-2}{1+7y^2}$. Cuando $y \to \infty$: $f(y) \to \dfrac{5}{7}$. El máximo de $f$ es $\dfrac{5}{7}$ (límite). También $f(0) = -2$.
> 
> Entonces $f(y) < \dfrac{5}{7}$ para todo $y$. Tomando $x = \dfrac{1}{9}$: $9x = 1 > \dfrac{5}{7}$. ✓
> 
> **Verdadero.** ✅
> 
> **(c) $\exists x \in \mathbb{R} : 2x^2 - 5x + 3 \leq 1 - x$**
> 
> $2x^2 - 5x + 3 \leq 1 - x \iff 2x^2 - 4x + 2 \leq 0 \iff 2(x-1)^2 \leq 0$
> 
> Como $(x-1)^2 \geq 0$ siempre, la única solución es $x = 1$.
> 
> **Verdadero** (con $x=1$). ✅
> 
> **(d) $\forall x > 0, \exists y \in \mathbb{R} : 4y^2 - 3xy + 1 < 0$**
> 
> Tratamos como cuadrática en $y$: $4y^2 - 3xy + 1$. Para que tenga raíces reales y tome valores negativos, el discriminante debe ser positivo:
> 
> $\Delta = 9x^2 - 16 > 0 \iff x > \dfrac{4}{3}$
> 
> Para $0 < x \leq \dfrac{4}{3}$, el discriminante es $\leq 0$ y la cuadrática es siempre $\geq 0$, sin solución negativa.
> 
> **Falso.** ❌

> [!example]- 📝 Ejercicio 15 — Inducción: $3^n \geq 2n+1$
> 
> **Demostrar:** $\forall n \in \mathbb{N}: 3^n \geq 2n+1$
> 
> **Base:** $n=1$: $3^1 = 3 \geq 2(1)+1 = 3$. ✓
> 
> **Hipótesis inductiva (HI):** Suponer que $3^k \geq 2k+1$ para algún $k \geq 1$.
> 
> **Paso inductivo:** Demostrar que $3^{k+1} \geq 2(k+1)+1 = 2k+3$.
> 
> $$3^{k+1} = 3 \cdot 3^k \geq 3(2k+1) \quad \text{(por HI)}$$ $$= 6k+3 \geq 2k+3 \quad \text{(pues } 6k \geq 2k \text{ para } k \geq 1\text{)}$$
> 
> Por lo tanto $3^{k+1} \geq 2k+3 = 2(k+1)+1$. $\blacksquare$

> [!example]- 📝 Ejercicio 16 — Inducción: suma de cuadrados
> 
> **Demostrar:** $1^2 + 2^2 + \cdots + n^2 = \dfrac{n(n+1)(2n+1)}{6}$, $\forall n \geq 1$
> 
> **Base:** $n=1$: $1 = \dfrac{1 \cdot 2 \cdot 3}{6} = 1$. ✓
> 
> **HI:** $\displaystyle\sum_{i=1}^{k} i^2 = \dfrac{k(k+1)(2k+1)}{6}$
> 
> **Paso inductivo:**
> 
> $$\sum_{i=1}^{k+1} i^2 = \sum_{i=1}^{k} i^2 + (k+1)^2 = \frac{k(k+1)(2k+1)}{6} + (k+1)^2$$
> 
> $$= (k+1)\left[\frac{k(2k+1)}{6} + (k+1)\right] = (k+1) \cdot \frac{k(2k+1) + 6(k+1)}{6}$$
> 
> $$= (k+1) \cdot \frac{2k^2 + 7k + 6}{6} = (k+1) \cdot \frac{(k+2)(2k+3)}{6}$$
> 
> $$= \frac{(k+1)(k+2)(2(k+1)+1)}{6} \quad \blacksquare$$

> [!example]- 📝 Ejercicio 17 — Inducción: suma alternada de cuadrados
> 
> **Demostrar:** $-1^2 + 2^2 - 3^2 + \cdots + (-1)^n n^2 = \dfrac{(-1)^n n(n+1)}{2}$, $\forall n \geq 1$
> 
> **Base:** $n=1$: $(-1)^1 \cdot 1 = -1 = \dfrac{(-1)^1 \cdot 1 \cdot 2}{2} = -1$. ✓
> 
> **HI:** $\displaystyle\sum_{i=1}^{k}(-1)^i i^2 = \frac{(-1)^k k(k+1)}{2}$
> 
> **Paso inductivo:**
> 
> $$\sum_{i=1}^{k+1}(-1)^i i^2 = \frac{(-1)^k k(k+1)}{2} + (-1)^{k+1}(k+1)^2$$
> 
> $$= (-1)^{k+1}(k+1)\left[-\frac{k}{2} + (k+1)\right] = (-1)^{k+1}(k+1) \cdot \frac{-k + 2(k+1)}{2}$$
> 
> $$= (-1)^{k+1}(k+1) \cdot \frac{k+2}{2} = \frac{(-1)^{k+1}(k+1)(k+2)}{2} \quad \blacksquare$$

> [!example]- 📝 Ejercicio 18 — Directo: si 2 | $n^2-1$ entonces 4 | $n^2-1$
> 
> **Demostrar:** Si $2 \mid n^2-1$, entonces $4 \mid n^2-1$.
> 
> Si $2 \mid n^2-1$, entonces $n^2-1$ es par, es decir $n^2$ es impar, lo que implica que $n$ es impar.
> 
> Si $n$ es impar, existe $k \in \mathbb{Z}$ tal que $n = 2k+1$. Entonces:
> 
> $$n^2 - 1 = (2k+1)^2 - 1 = 4k^2 + 4k + 1 - 1 = 4k^2 + 4k = 4k(k+1)$$
> 
> Como $k(k+1)$ es producto de dos enteros consecutivos, es entero. Por tanto $4 \mid 4k(k+1) = n^2-1$. $\blacksquare$

> [!example]- 📝 Ejercicio 19 — Inducción: divisibilidad por 57
> 
> **Demostrar:** $7^{n+1} + 8^{2n-1}$ es divisible por 57, $\forall n \in \mathbb{N}$.
> 
> Nota: $57 = 3 \times 19$ y $8^2 = 64$.
> 
> **Base:** $n=1$: $7^2 + 8^1 = 49 + 8 = 57 = 57 \cdot 1$. ✓
> 
> **HI:** $57 \mid 7^{k+1} + 8^{2k-1}$, es decir $7^{k+1} + 8^{2k-1} = 57m$ para algún $m \in \mathbb{Z}$.
> 
> **Paso inductivo:** Demostrar que $57 \mid 7^{k+2} + 8^{2k+1}$.
> 
> $$7^{k+2} + 8^{2k+1} = 7 \cdot 7^{k+1} + 64 \cdot 8^{2k-1}$$ $$= 7 \cdot 7^{k+1} + (7 + 57) \cdot 8^{2k-1}$$ $$= 7(7^{k+1} + 8^{2k-1}) + 57 \cdot 8^{2k-1}$$ $$= 7 \cdot 57m + 57 \cdot 8^{2k-1}$$ $$= 57(7m + 8^{2k-1})$$
> 
> Por tanto $57 \mid 7^{k+2} + 8^{2k+1}$. $\blacksquare$

> [!example]- 📝 Ejercicio 20 — Inducción: desigualdad con raíces
> 
> **Demostrar:** $\displaystyle1 + \frac{1}{\sqrt{2}} + \cdots + \frac{1}{\sqrt{n}} > 2(\sqrt{n+1}-1)$, $\forall n \in \mathbb{N}$
> 
> **Base:** $n=1$: $1 > 2(\sqrt{2}-1) = 2\sqrt{2}-2 \approx 0.828$. ✓
> 
> **HI:** $\displaystyle S_k = \sum_{i=1}^{k}\frac{1}{\sqrt{i}} > 2(\sqrt{k+1}-1)$
> 
> **Paso inductivo:**
> 
> $$S_{k+1} = S_k + \frac{1}{\sqrt{k+1}} > 2(\sqrt{k+1}-1) + \frac{1}{\sqrt{k+1}}$$
> 
> Necesitamos mostrar que $2(\sqrt{k+1}-1) + \dfrac{1}{\sqrt{k+1}} \geq 2(\sqrt{k+2}-1)$.
> 
> Esto equivale a: $\dfrac{1}{\sqrt{k+1}} \geq 2(\sqrt{k+2} - \sqrt{k+1})$.
> 
> Racionalizando el lado derecho:
> 
> $$2(\sqrt{k+2}-\sqrt{k+1}) = \frac{2}{\sqrt{k+2}+\sqrt{k+1}} \leq \frac{2}{2\sqrt{k+1}} = \frac{1}{\sqrt{k+1}}$$
> 
> Por tanto $S_{k+1} > 2(\sqrt{k+2}-1)$. $\blacksquare$

> [!example]- 📝 Ejercicio 21 — Inducción: $1^2 + 2^2 + \cdots + n^2 \leq n^3$
> 
> **Demostrar:** $\displaystyle\sum_{i=1}^{n} i^2 \leq n^3$, $\forall n \in \mathbb{N}$
> 
> **Base:** $n=1$: $1 \leq 1$. ✓
> 
> **HI:** $\displaystyle\sum_{i=1}^{k} i^2 \leq k^3$
> 
> **Paso inductivo:**
> 
> $$\sum_{i=1}^{k+1} i^2 = \sum_{i=1}^{k} i^2 + (k+1)^2 \leq k^3 + (k+1)^2$$
> 
> Necesitamos: $k^3 + (k+1)^2 \leq (k+1)^3$.
> 
> $$(k+1)^3 - (k+1)^2 = (k+1)^2 \cdot k \geq k^3 \iff k(k+1)^2 \geq k^3$$ $$\iff (k+1)^2 \geq k^2 \iff k^2+2k+1 \geq k^2$$
> 
> Lo cual es verdadero para todo $k \geq 1$. $\blacksquare$

> [!example]- 📝 Ejercicio 22 — Inducción: diagonales de polígono convexo
> 
> **Demostrar:** Un polígono convexo de $n$ lados tiene $\dfrac{n(n-3)}{2}$ diagonales.
> 
> **Base:** $n=3$ (triángulo): $\dfrac{3(0)}{2} = 0$ diagonales. ✓ (un triángulo no tiene diagonales).
> 
> **HI:** Un polígono convexo de $k$ lados tiene $\dfrac{k(k-3)}{2}$ diagonales.
> 
> **Paso inductivo:** Al agregar un vértice nuevo para pasar a $k+1$ lados:
> 
> El nuevo vértice $V_{k+1}$ puede conectarse con los $k+1-3 = k-2$ vértices que no son sus vecinos inmediatos (sus dos vecinos forman los nuevos lados). Además, el lado que conectaba los dos vecinos del nuevo vértice desaparece como lado (se convierte en diagonal interna — no, en realidad pasa a ser interior). Revisando correctamente:
> 
> Al pasar de $k$ a $k+1$ vértices, el nuevo vértice añade $(k+1)-3 = k-2$ diagonales nuevas (hacia todos excepto sus 2 vecinos y él mismo).
> 
> $$D(k+1) = D(k) + (k-2) = \frac{k(k-3)}{2} + (k-2) = \frac{k^2-3k+2k-4}{2} = \frac{k^2-k-4}{2}$$
> 
> Y el valor esperado es:
> 
> $$\frac{(k+1)(k+1-3)}{2} = \frac{(k+1)(k-2)}{2} = \frac{k^2-k-2}{2}$$
> 
> Hay una diferencia de 1 en el numerador. Esto indica que al agregar el vértice, el segmento que unía sus dos vecinos (que era un **lado** del polígono de $k$ vértices) ahora se convierte en una **diagonal** del polígono de $k+1$ vértices, añadiendo 1 diagonal más:
> 
> $$D(k+1) = D(k) + (k-2) + 1 = \frac{k(k-3)}{2} + k - 1 = \frac{k^2-3k+2k-2}{2} = \frac{k^2-k-2}{2} = \frac{(k+1)(k-2)}{2} \quad \blacksquare$$

---

## 🧮 1.4 — Conjuntos, Operaciones y Demostraciones

> [!example]- 📝 Ejercicio 23 — Si $A \subseteq B$, entonces $A \cap B = A$
> 
> **Demostrar:** Si $A \subseteq B$, entonces $A \cap B = A$.
> 
> **Demostración (doble contención):**
> 
> **(⊆)** Sea $x \in A \cap B$. Entonces $x \in A$ y $x \in B$. En particular $x \in A$. Así $A \cap B \subseteq A$.
> 
> **(⊇)** Sea $x \in A$. Como $A \subseteq B$, entonces $x \in B$. Luego $x \in A$ y $x \in B$, es decir $x \in A \cap B$. Así $A \subseteq A \cap B$.
> 
> Por doble contención: $A \cap B = A$. $\blacksquare$

> [!example]- 📝 Ejercicio 24 — Condiciones entre conjuntos
> 
> **(a) $A \cap B = A$:**
> 
> Por el Ejercicio 23, esto equivale a $A \subseteq B$.
> 
> **(b) $\overline{A} \cap U = \emptyset$:**
> 
> $\overline{A} \cap U = \overline{A}$ (ley de identidad). Entonces $\overline{A} = \emptyset$, lo que implica $A = U$.
> 
> La condición es que $A = U$ (el conjunto universal).
> 
> **(c) $A \cup B = A$:**
> 
> $A \cup B = A$ significa que todo elemento de $B$ ya está en $A$, es decir $B \subseteq A$.

> [!example]- 📝 Ejercicio 25 — $A \times (B \cap C) = (A \times B) \cap (A \times C)$
> 
> **Demostración:**
> 
> Sea $(x, y)$ un par ordenado arbitrario.
> 
> $$(x, y) \in A \times (B \cap C)$$ $$\iff x \in A \land y \in (B \cap C) \quad \text{(def. producto cartesiano)}$$ $$\iff x \in A \land (y \in B \land y \in C) \quad \text{(def. intersección)}$$ $$\iff (x \in A \land y \in B) \land (x \in A \land y \in C) \quad \text{(idem., conm., asoc.)}$$ $$\iff (x, y) \in A \times B \land (x, y) \in A \times C \quad \text{(def. producto cartesiano)}$$ $$\iff (x, y) \in (A \times B) \cap (A \times C) \quad \text{(def. intersección)}$$
> 
> Como $(x,y)$ es arbitrario: $A \times (B \cap C) = (A \times B) \cap (A \times C)$. $\blacksquare$

> [!example]- 📝 Ejercicio 26 — Simplificación con álgebra de conjuntos
> 
> **Simplificar:** $((C \cup \overline{A}) - \overline{B-A}) \cap C$
> 
> Primero, $B - A = B \cap \overline{A}$, entonces $\overline{B-A} = \overline{B \cap \overline{A}} = \overline{B} \cup A$ (De Morgan).
> 
> Luego, $X - Y = X \cap \overline{Y}$:
> 
> $$(C \cup \overline{A}) - \overline{B-A} = (C \cup \overline{A}) \cap \overline{(\overline{B} \cup A)}$$ $$= (C \cup \overline{A}) \cap (B \cap \overline{A}) \quad \text{(De Morgan)}$$
> 
> Distribuyendo:
> 
> $$= (C \cap B \cap \overline{A}) \cup (\overline{A} \cap B \cap \overline{A})$$ $$= (C \cap B \cap \overline{A}) \cup (B \cap \overline{A}) \quad \text{(idempotencia)}$$ $$= B \cap \overline{A} \quad \text{(absorción: } (C\cap B\cap\overline{A}) \cup (B\cap\overline{A}) = B\cap\overline{A}\text{)}$$
> 
> Finalmente intersectamos con $C$:
> 
> $$(B \cap \overline{A}) \cap C = B \cap C \cap \overline{A}$$
> 
> $$\boxed{((C \cup \overline{A}) - \overline{B-A}) \cap C = B \cap C \cap \overline{A}}$$

> [!example]- 📝 Ejercicio 27 — Si $A \subseteq B$, entonces $A \cup C \subseteq B \cup C$
> 
> **Demostración:**
> 
> Sea $x \in A \cup C$ arbitrario. Entonces $x \in A$ o $x \in C$.
> 
> - **Caso 1:** $x \in A$. Como $A \subseteq B$, entonces $x \in B$. Por tanto $x \in B \cup C$. ✓
> - **Caso 2:** $x \in C$. Entonces directamente $x \in B \cup C$. ✓
> 
> En ambos casos $x \in B \cup C$, por tanto $A \cup C \subseteq B \cup C$. $\blacksquare$

> [!example]- 📝 Ejercicio 28 — Tres demostraciones con álgebra de conjuntos
> 
> **(a) $A - (A - (A \cap B)) = A \cap B$**
> 
> Recordar: $X - Y = X \cap \overline{Y}$.
> 
> $$A - (A \cap B) = A \cap \overline{(A \cap B)} = A \cap (\overline{A} \cup \overline{B}) \quad \text{(De Morgan)}$$ $$= (A \cap \overline{A}) \cup (A \cap \overline{B}) = \emptyset \cup (A \cap \overline{B}) = A \cap \overline{B} = A - B$$
> 
> Entonces:
> 
> $$A - (A-(A\cap B)) = A - (A-B) = A \cap \overline{(A \cap \overline{B})}$$ $$= A \cap (\overline{A} \cup B) \quad \text{(De Morgan)}$$ $$= (A \cap \overline{A}) \cup (A \cap B) = \emptyset \cup (A \cap B) = A \cap B \quad \blacksquare$$
> 
> **(b) $(B \cup (C - \overline{A})) \cap (C \cap A) = A \cap C$**
> 
> Primero: $C - \overline{A} = C \cap \overline{(\overline{A})} = C \cap A$.
> 
> $$B \cup (C \cap A) \quad \text{(sustituyendo)}$$
> 
> Entonces:
> 
> $$(B \cup (C \cap A)) \cap (C \cap A)$$ $$= C \cap A \quad \text{(absorción: } (X \cup Y) \cap Y = Y\text{, con } Y = C\cap A\text{)}$$ $$= A \cap C \quad \blacksquare$$
> 
> **(c) $(A-B) \cap \overline{(C \cap \overline{A})} = A - B$**
> 
> Primero simplificamos $\overline{(C \cap \overline{A})}$:
> 
> $$\overline{C \cap \overline{A}} = \overline{C} \cup A \quad \text{(De Morgan)}$$
> 
> Entonces:
> 
> $$(A - B) \cap (\overline{C} \cup A)$$ $$= (A \cap \overline{B}) \cap (\overline{C} \cup A)$$ $$= (A \cap \overline{B} \cap \overline{C}) \cup (A \cap \overline{B} \cap A)$$ $$= (A \cap \overline{B} \cap \overline{C}) \cup (A \cap \overline{B}) \quad \text{(idempotencia)}$$ $$= A \cap \overline{B} \quad \text{(absorción)}$$ $$= A - B \quad \blacksquare$$

---

**Tags:** #matematicas-discretas #guia-problemas #logica #conjuntos #induccion #demostraciones #MATG1051
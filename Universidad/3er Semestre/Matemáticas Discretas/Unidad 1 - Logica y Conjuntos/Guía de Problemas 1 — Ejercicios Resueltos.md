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
> Aplicamos absorción directamente: en la expresión $(x_1 \land x_2 \land \neg x_3) \lor (\neg x_1 \land \neg x_3) \lor \neg x_3$, el término $\neg x_3$ absorbe a los dos anteriores (ambos lo contienen como factor), usando $A \lor (B \land A) \equiv A$:
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
> |F|V|V|V|F|F|V|**V**|
> |F|V|F|V|V|V|V|**V**|
> |F|F|V|V|F|F|V|**V**|
> |F|F|F|V|V|V|F|**F**|
> 
> **(b) Clasificación:**
> 
> La fila $(F,F,F)$ da Falso → la proposición es una **contingencia**. ✅
> 
> **(c) Simplificación algebraica:**
> 
> $$[(p \to q) \land (\neg r \lor p)] \to (q \lor r)$$
> 
> **Paso 1:** Aplicamos la equivalencia del condicional ($A \to B \equiv \neg A \lor B$) al operador principal y al interno:
> 
> $$\equiv \neg[(\neg p \lor q) \land (\neg r \lor p)] \lor (q \lor r)$$
> 
> **Paso 2:** Aplicamos De Morgan en el corchete:
> 
> $$\equiv [\neg(\neg p \lor q) \lor \neg(\neg r \lor p)] \lor (q \lor r)$$
> 
> **Paso 3:** Aplicamos De Morgan y doble negación dentro de cada paréntesis:
> 
> $$\equiv [(p \land \neg q) \lor (r \land \neg p)] \lor (q \lor r)$$
> 
> **Paso 4:** Asociatividad (todos los términos unidos por $\lor$):
> 
> $$\equiv (p \land \neg q) \lor (r \land \neg p) \lor q \lor r$$
> 
> **Paso 5:** Reagrupamos estratégicamente (ley conmutativa):
> 
> $$\equiv (p \land \neg q) \lor q \lor (r \land \neg p) \lor r$$
> 
> **Paso 6:** Aplicamos absorción en cada par:
> 
> - $(p \land \neg q) \lor q \equiv p \lor q$ (absorción)
> - $(r \land \neg p) \lor r \equiv r$ (absorción)
> 
> $$\equiv (p \lor q) \lor r$$
> 
> **Paso 7:** Asociatividad:
> 
> $$\equiv p \lor q \lor r$$
> 
> **(b) Clasificación:**
> 
> La fórmula es equivalente a $p \lor q \lor r$, que es Falsa cuando $p=F, q=F, r=F$ y Verdadera en los demás casos → **contingencia**. $\blacksquare$

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
> **Paso 1 — Agrupar los tres minitérminos con $A=1$:**
> 
> Los tres últimos comparten $A=1$ y en todos ellos $B \land C$ es falso (nunca son $B=C=1$ simultáneamente):
> 
> $$(A \land \neg B \land \neg C) \lor (A \land \neg B \land C) \lor (A \land B \land \neg C)$$
> 
> Factorizamos $A$:
> 
> $$= A \land [(\neg B \land \neg C) \lor (\neg B \land C) \lor (B \land \neg C)]$$
> 
> Agrupamos los dos primeros dentro del corchete (factor común $\neg B$):
> 
> $$= A \land [(\neg B \land (\neg C \lor C)) \lor (B \land \neg C)]$$
> 
> Como $\neg C \lor C = V$ (tercio excluido):
> 
> $$= A \land [\neg B \lor (B \land \neg C)]$$
> 
> Aplicamos absorción $\neg B \lor (B \land \neg C) \equiv \neg B \lor \neg C$ (por resolución: $\neg B \lor B = V$, y $\neg B \lor \neg C$ cubre todos los casos menos $B=C=1$):
> 
> $$= A \land (\neg B \lor \neg C)$$
> 
> Aplicamos De Morgan: $\neg B \lor \neg C \equiv \neg(B \land C)$:
> 
> $$= A \land \neg(B \land C)$$
> 
> **Paso 2 — Unir con el primer minitérmino $(\neg A \land B \land C)$:**
> 
> $$Y = (\neg A \land B \land C) \lor (A \land \neg(B \land C))$$
> 
> **Paso 3 — Reescribir aplicando distributiva:**
> 
> Partimos de $(\neg A \land B \land C) \lor (A \land \neg(B \land C))$. Llamamos $X = B \land C$ para simplificar la notación:
> 
> $$= (\neg A \land X) \lor (A \land \neg X)$$
> 
> Aplicamos distributiva sumando $A$ al primer término y $X$ al segundo:
> 
> $$= [(\neg A \land X) \lor A] \land [(\neg A \land X) \lor \neg X]$$
> 
> Simplificamos cada factor:
> 
> - $(\neg A \land X) \lor A \equiv A \lor X$ (absorción: $A \lor (\neg A \land X) \equiv A \lor X$)
> - $(\neg A \land X) \lor \neg X \equiv \neg A \lor \neg X \equiv \neg(A \land X)$ (absorción análoga)
> 
> Por tanto:
> 
> $$= (A \lor X) \land \neg(A \land X)$$
> 
> Restituyendo $X = B \land C$:
> 
> $$\boxed{Y = (A \lor (B \land C)) \land \neg(A \land B \land C)}$$
> 
> **Verificación rápida con la tabla:**
> 
> |Fila|$A \lor (B \land C)$|$\neg(A \land B \land C)$|$Y$|Tabla|
> |---|---|---|---|---|
> |$(0,1,1)$|$0 \lor 1 = 1$|$\neg 0 = 1$|**1**|1 ✅|
> |$(1,1,1)$|$1 \lor 1 = 1$|$\neg 1 = 0$|**0**|0 ✅|
> |$(1,0,0)$|$1 \lor 0 = 1$|$\neg 0 = 1$|**1**|1 ✅|
> |$(0,0,0)$|$0 \lor 0 = 0$|$\neg 0 = 1$|**0**|0 ✅|
> 
> $$\boxed{Y = (A \lor (B \land C)) \land \neg(A \land B \land C)}$$
> 
> Es decir: "acceso si el gerente está presente O si están B y C juntos, pero bloqueado si están los tres (coacción)."
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
> |2|$d(j) \to r(j)$|Instanciación Universal (IU) en Premisa 1|
> |3|$r(j)$|Modus Ponens (1, 2)|
> |4|$r(j) \to \neg v(j)$|Instanciación Universal (IU) en Premisa 2|
> |5|$\neg v(j)$|Modus Ponens (3, 4)|
> |6|$b(j) \to v(j)$|Instanciación Universal (IU) en Premisa 3|
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
> **Conclusión:** $q \to (s \land t)$
> 
> **Demostración Formal (Reducción al Absurdo):**
> 
> Suponemos que la conclusión es **falsa**, es decir:
> 
> $$\neg[q \to (s \land t)] \equiv q \land \neg(s \land t) \equiv q \land (\neg s \lor \neg t)$$
> 
> Trabajamos con esta hipótesis y las premisas para derivar una contradicción.
> 
> |Paso|Expresión|Justificación|
> |---|---|---|
> |1|$p \land q \to r$|Premisa 1|
> |2|$(p \to r) \to s$|Premisa 2|
> |3|$t \lor \neg q$|Premisa 3|
> |4|$q \land (\neg s \lor \neg t)$|Hipótesis de absurdo: negación de la conclusión|
> |5|$q$|Simplificación (4)|
> |6|$\neg s \lor \neg t$|Simplificación (4)|
> |7|$t$|Silogismo Disyuntivo (3, 5): de $t \lor \neg q$ y $q$ se obtiene $t$|
> |8|$\neg s$|Silogismo Disyuntivo (6, 7): de $\neg s \lor \neg t$ y $t$ se obtiene $\neg s$|
> |9|$\neg s \to \neg(p \to r)$|Contrarrecíproca de la Premisa 2|
> |10|$\neg(p \to r)$|Modus Ponens (8, 9)|
> |11|$p \land \neg r$|Equivalencia $\neg(p \to r) \equiv p \land \neg r$ aplicada a (10)|
> |12|$p$|Simplificación (11)|
> |13|$\neg r$|Simplificación (11)|
> |14|$p \land q$|Conjunción (12, 5)|
> |15|$r$|Modus Ponens (1, 14)|
> |16|$r \land \neg r$|Conjunción (15, 13) — **⊥ Contradicción**|
> 
> La hipótesis de absurdo lleva a $r \land \neg r$, que es una contradicción. Por tanto la conclusión $q \to (s \land t)$ es verdadera. $\blacksquare$
> 
> El argumento es **válido**.

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
> 
> 
> **(a) $\exists x \in \mathbb{R} : 7 - 4x < 5 - 4x^2$**
> 
> **Resultado: Falso ❌**
> 
> Reescribimos la desigualdad pasando todo al mismo lado:
> 
> $$7 - 4x < 5 - 4x^2 \iff 4x^2 - 4x + 2 < 0 \iff 2(2x^2 - 2x + 1) < 0$$
> 
> Analizamos el signo de $2x^2 - 2x + 1$. Su discriminante es:
> 
> $$\Delta = (-2)^2 - 4(2)(1) = 4 - 8 = -4 < 0$$
> 
> Como $\Delta < 0$ y el coeficiente líder es positivo, la cuadrática **no tiene raíces reales y es siempre positiva**. Por tanto $2(2x^2-2x+1) > 0$ para todo $x \in \mathbb{R}$, y la desigualdad nunca se cumple. $\blacksquare$
> 
> ---
> 
> **(b) $\exists x > 0,\ \forall y \in \mathbb{R} :\ \dfrac{5y^2 - 2}{1 + 7y^2} < 9x$**
> 
> **Resultado: Verdadero ✅**
> 
> Analizamos el comportamiento de $f(y) = \dfrac{5y^2-2}{1+7y^2}$ para acotar su valor máximo:
> 
> $$\lim_{y \to \infty} f(y) = \frac{5}{7}$$
> 
> Esta es una asíntota horizontal que $f$ nunca alcanza, luego $f(y) < \dfrac{5}{7}$ para todo $y \in \mathbb{R}$.
> 
> Elegimos $x = \dfrac{1}{9} > 0$, con lo que $9x = 1$. Entonces:
> 
> $$f(y) < \frac{5}{7} < 1 = 9x \quad \forall y \in \mathbb{R}$$
> 
> Existe el valor $x = \dfrac{1}{9}$ que satisface la condición. $\blacksquare$
> 
> ---
> 
> **(c) $\exists x \in \mathbb{R} : 2x^2 - 5x + 3 \leq 1 - x$**
> 
> **Resultado: Verdadero ✅**
> 
> Pasamos todo al mismo lado y simplificamos:
> 
> $$2x^2 - 5x + 3 \leq 1 - x \iff 2x^2 - 4x + 2 \leq 0 \iff 2(x-1)^2 \leq 0$$
> 
> Como $(x-1)^2 \geq 0$ siempre, la única forma de que $2(x-1)^2 \leq 0$ se cumpla es con igualdad: $x = 1$.
> 
> Verificación: $2(1)^2 - 5(1) + 3 = 0 \leq 0 = 1 - 1$. ✓
> 
> Existe $x = 1$ que satisface la condición. $\blacksquare$
> 
> ---
> 
> **(d) $\forall x > 0,\ \exists y \in \mathbb{R} : 4y^2 - 3xy + 1 < 0$**
> 
> **Resultado: Falso ❌**
> 
> Para que exista algún $y$ tal que $4y^2 - 3xy + 1 < 0$, la cuadrática en $y$ debe tomar valores negativos, lo que requiere que tenga raíces reales distintas, es decir $\Delta > 0$:
> 
> $$\Delta = (-3x)^2 - 4(4)(1) = 9x^2 - 16 > 0 \iff x > \frac{4}{3}$$
> 
> Para $0 < x \leq \dfrac{4}{3}$, se tiene $\Delta \leq 0$, por lo que la cuadrática es **siempre $\geq 0$** y nunca toma valores negativos.
> 
> Como el cuantificador exige que esto valga para **todo** $x > 0$, y falla para $x = 1 \in \left(0, \frac{4}{3}\right]$, la proposición es falsa. $\blacksquare$

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
> **Demostrar:** Un polígono convexo de $n$ lados tiene $\dfrac{n(n-3)}{2}$ diagonales, $\forall n \geq 3$.
> 
> **Base:** $n=3$ (triángulo): $\dfrac{3(3-3)}{2} = 0$ diagonales. ✓ (un triángulo no tiene diagonales).
> 
> **HI:** Un polígono convexo de $k$ lados tiene $D(k) = \dfrac{k(k-3)}{2}$ diagonales.
> 
> **Paso inductivo:** Construimos el polígono de $k+1$ lados insertando un vértice nuevo $V_{k+1}$ sobre uno de los lados del polígono de $k$ lados — digamos sobre el lado $\overline{AB}$. Esto reemplaza ese lado por dos lados nuevos $\overline{AV_{k+1}}$ y $\overline{V_{k+1}B}$.
> 
> Contamos las diagonales nuevas que aparecen:
> 
> 1. **El segmento $\overline{AB}$** dejó de ser un lado y pasa a ser diagonal: $+1$
> 2. **El vértice $V_{k+1}$** puede conectarse mediante diagonales con todos los vértices excepto él mismo y sus 2 vecinos ($A$ y $B$): son $k+1-1-2 = k-2$ diagonales nuevas.
> 
> Total de diagonales nuevas: $(k-2)+1 = k-1$.
> 
> $$D(k+1) = D(k) + (k-1) = \frac{k(k-3)}{2} + (k-1) = \frac{k^2-3k+2k-2}{2} = \frac{k^2-k-2}{2} = \frac{(k+1)(k-2)}{2}$$
> 
> Como $\dfrac{(k+1)(k-2)}{2} = \dfrac{(k+1)((k+1)-3)}{2}$, que es exactamente la fórmula para $n = k+1$. $\blacksquare$
> 
> ![[Pasted image 20260613145551.png]]
> 
> ![[Pasted image 20260613145600.png]]
> 
> ![[Pasted image 20260613145618.png]]
> 
>
> >[!note] 📌 Nota — Lo que muestran las imágenes
> > Las imágenes ilustran el paso inductivo: al insertar el vértice $V_{k+1}$ sobre el lado $\overline{AB}$, ocurren dos cosas simultáneamente:
> >
> > 1. $\overline{AB}$ **deja de ser un lado** del polígono y se convierte en **diagonal** — de ahí el $+1$ en el conteo.
> > 2. $V_{k+1}$ traza **$k-2$ diagonales nuevas** hacia todos los vértices que no son sus vecinos inmediatos.
> >
> > Esos dos aportes juntos ($k-2+1 = k-1$) son los que hacen que la fórmula cierre exactamente al pasar de $k$ a $k+1$.

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
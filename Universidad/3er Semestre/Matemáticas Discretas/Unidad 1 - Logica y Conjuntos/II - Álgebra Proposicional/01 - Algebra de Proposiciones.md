# 🧮 Álgebra de Proposiciones

## 🎯 Introducción

> [!info]- 💡 ¿De qué trata el Álgebra de Proposiciones?
> 
> El **álgebra de proposiciones** nos permite **demostrar equivalencias lógicas sin tablas de verdad**, manipulando expresiones paso a paso como en el álgebra ordinaria, justificando cada paso con una ley.
> 
> Ya conocemos las leyes (de las notas de Lógica Proposicional). Ahora las usamos como **herramientas de demostración**.
> 
> > **Notación:** Los símbolos $\equiv$ y $\Leftrightarrow$ se usan indistintamente para indicar equivalencia lógica.

---

## 📋 Leyes de Referencia Rápida

> [!success]- 🗂️ Tabla de leyes (para consultar al demostrar)
> 
> | Ley | Para $\vee$ | Para $\wedge$ |
> |---|---|---|
> | **Asociativa** | $(p \vee q) \vee r \Leftrightarrow p \vee (q \vee r)$ | $(p \wedge q) \wedge r \Leftrightarrow p \wedge (q \wedge r)$ |
> | **Conmutativa** | $p \vee q \Leftrightarrow q \vee p$ | $p \wedge q \Leftrightarrow q \wedge p$ |
> | **Distributiva** | $p \vee (q \wedge r) \Leftrightarrow (p \vee q) \wedge (p \vee r)$ | $p \wedge (q \vee r) \Leftrightarrow (p \wedge q) \vee (p \wedge r)$ |
> | **Identidad** | $p \vee F \Leftrightarrow p$ | $p \wedge V \Leftrightarrow p$ |
> | **Acotación** | $p \vee V \Leftrightarrow V$ | $p \wedge F \Leftrightarrow F$ |
> | **Complemento** | $p \vee \neg p \Leftrightarrow V$ | $p \wedge \neg p \Leftrightarrow F$ |
> | **Idempotencia** | $p \vee p \Leftrightarrow p$ | $p \wedge p \Leftrightarrow p$ |
> | **Involución** | $\neg(\neg p) \Leftrightarrow p$ | — |
> | **De Morgan** | $\neg(p \vee q) \Leftrightarrow \neg p \wedge \neg q$ | $\neg(p \wedge q) \Leftrightarrow \neg p \vee \neg q$ |
> | **Absorción** | $p \vee (p \wedge q) \Leftrightarrow p$ | $p \wedge (p \vee q) \Leftrightarrow p$ |
> | **Condicional** | $p \to q \Leftrightarrow \neg p \vee q$ | — |
> | **Contrarrecíproco** | $p \to q \Leftrightarrow \neg q \to \neg p$ | — |

---

## ✍️ ¿Cómo estructurar una demostración algebraica?

> [!tip]- ⚙️ Formato estándar
> 
> Cada paso tiene la forma:
> 
> $$\text{expresión anterior} \equiv \text{expresión nueva} \qquad \text{(ley usada)}$$
> 
> Se parte de un lado de la equivalencia y se transforma hasta llegar al otro lado.
> 
> **Reglas:**
> - Nunca se modifica ambos lados al mismo tiempo.
> - Cada paso debe justificarse con exactamente una ley.
> - Se finaliza con $\blacksquare$ (símbolo de demostración completa).

---

## 📝 Ejercicios Resueltos

### Ejercicio 1

> [!example]- 📝 Demostrar: $\neg p \wedge (q \vee p) \equiv \neg p \wedge q$
> 
> $$\neg p \wedge (q \vee p)$$
> $$\equiv (\neg p \wedge q) \vee (\neg p \wedge p) \qquad \text{(ley distributiva)}$$
> $$\equiv (\neg p \wedge q) \vee (p \wedge \neg p) \qquad \text{(ley conmutativa)}$$
> $$\equiv (\neg p \wedge q) \vee F \qquad \text{(ley de complemento)}$$
> $$\equiv \neg p \wedge q \qquad \text{(ley de identidad)} \quad \blacksquare$$

---

### Ejercicio 2

> [!example]- 📝 Demostrar la Ley de Absorción: $p \vee (p \wedge q) \Leftrightarrow p$
> 
> $$p \vee (p \wedge q)$$
> $$\equiv (p \wedge V) \vee (p \wedge q) \qquad \text{(ley de identidad)}$$
> $$\equiv p \wedge (V \vee q) \qquad \text{(ley distributiva)}$$
> $$\equiv p \wedge (q \vee V) \qquad \text{(ley conmutativa)}$$
> $$\equiv p \wedge V \qquad \text{(ley de acotación)}$$
> $$\equiv p \qquad \text{(ley de identidad)} \quad \blacksquare$$

---

### Ejercicio 3

> [!example]- 📝 Demostrar: $p \wedge \neg q \Leftrightarrow p \wedge \neg(q \vee \neg p)$
> 
> Partimos del lado derecho y llegamos al izquierdo:
> 
> $$p \wedge \neg(q \vee \neg p)$$
> $$\Leftrightarrow p \wedge (\neg q \wedge \neg(\neg p)) \qquad \text{(ley de De Morgan)}$$
> $$\Leftrightarrow p \wedge (\neg q \wedge p) \qquad \text{(ley de involución)}$$
> $$\Leftrightarrow p \wedge (p \wedge \neg q) \qquad \text{(ley conmutativa)}$$
> $$\Leftrightarrow (p \wedge p) \wedge \neg q \qquad \text{(ley asociativa)}$$
> $$\Leftrightarrow p \wedge \neg q \qquad \text{(ley de idempotencia)} \quad \blacksquare$$

---

### Ejercicio 4

> [!example]- 📝 Demostrar: $((¬p \vee q) \vee r) \wedge ((¬p \vee q) \vee ¬r) \Leftrightarrow p \to q$
> 
> Sea $s = \neg p \vee q$ para simplificar la notación:
> 
> $$(s \vee r) \wedge (s \vee \neg r)$$
> $$\Leftrightarrow s \vee (r \wedge \neg r) \qquad \text{(ley distributiva)}$$
> $$\Leftrightarrow s \vee F \qquad \text{(ley de complemento)}$$
> $$\Leftrightarrow s \qquad \text{(ley de identidad)}$$
> $$\Leftrightarrow \neg p \vee q \qquad \text{(sustituyendo } s\text{)}$$
> $$\Leftrightarrow p \to q \qquad \text{(ley del condicional)} \quad \blacksquare$$

---

### Ejercicio 5

> [!example]- 📝 Demostrar la Ley del Contrarrecíproco: $p \to q \equiv \neg q \to \neg p$
> 
> Partimos del lado derecho:
> 
> $$\neg q \to \neg p$$
> $$\equiv \neg(\neg q) \vee \neg p \qquad \text{(ley del condicional)}$$
> $$\equiv q \vee \neg p \qquad \text{(ley de involución)}$$
> $$\equiv \neg p \vee q \qquad \text{(ley conmutativa)}$$
> $$\equiv p \to q \qquad \text{(ley del condicional)} \quad \blacksquare$$

---

## ⚠️ Observaciones Importantes

> [!warning]- ⚠️ El condicional NO es asociativo
> 
> A diferencia de $\vee$ y $\wedge$, el condicional **no es asociativo**:
> 
> $$p \to (q \to r) \not\equiv (p \to q) \to r$$
> 
> **Contraejemplo:** Sean $VL(p) = VL(q) = VL(r) = 0$ (todos falsos):
> 
> | Expresión | Evaluación | Resultado |
> |---|---|---|
> | $q \to r$ | $F \to F$ | $V$ |
> | $p \to (q \to r)$ | $F \to V$ | $V$ |
> | $p \to q$ | $F \to F$ | $V$ |
> | $(p \to q) \to r$ | $V \to F$ | **F** |
> 
> Como $V \neq F$, las expresiones **no son equivalentes**. ❌

> [!note]- 📋 La equivalencia lógica es una relación de equivalencia
> 
> La relación $P \equiv Q$ sobre el conjunto de todas las formas proposicionales cumple:
> 
> | Propiedad | Significado |
> |---|---|
> | **Reflexiva** | $P \equiv P$ |
> | **Simétrica** | Si $P \equiv Q$ entonces $Q \equiv P$ |
> | **Transitiva** | Si $P \equiv Q$ y $Q \equiv R$ entonces $P \equiv R$ |
> 
> Esto permite encadenar demostraciones en múltiples pasos con total validez.

---

## 🎲 Aplicación — El Problema de los Baúles

> [!example]- 🏴‍☠️ El Rey y el Tesoro
> 
> Como recompensa por salvar a su hija, el Rey te ofrece elegir uno de tres baúles. Solo uno contiene el tesoro; los otros dos están vacíos. Las inscripciones son:
> 
> - **Baúl 1:** "Este baúl está vacío."
> - **Baúl 2:** "Este baúl está vacío."
> - **Baúl 3:** "El tesoro está en el baúl 2."
> 
> La Reina, que **nunca miente**, dice que **exactamente una inscripción es verdadera**.
> 
> **Análisis por casos:**
> 
> | Caso | Inscripción 1 | Inscripción 2 | Inscripción 3 | ¿Exactamente una V? |
> |---|:-:|:-:|:-:|:-:|
> | Tesoro en baúl 1 | F (hay tesoro) | V (está vacío) | F (no está en 2) | ✅ Una sola V |
> | Tesoro en baúl 2 | V (está vacío) | F (hay tesoro) | V (está en 2) | ❌ Dos verdaderas |
> | Tesoro en baúl 3 | V (está vacío) | V (está vacío) | F (no está en 2) | ❌ Dos verdaderas |
> 
> **Conclusión:** El tesoro está en el **baúl 1**. $\blacksquare$

---

## 📊 Resumen Visual

```mermaid
graph LR
    A[Expresión inicial] -->|"Ley 1"| B[Paso 1]
    B -->|"Ley 2"| C[Paso 2]
    C -->|"Ley 3"| D[...]
    D -->|"Ley n"| E[Expresión final ✅]

    style A fill:#1e3a5f,color:#fff
    style E fill:#2d6a4f,color:#fff
```

---

**Tags:** #matematicas-discretas #algebra-proposicional #demostraciones-algebraicas #equivalencias-logicas #MATG1051

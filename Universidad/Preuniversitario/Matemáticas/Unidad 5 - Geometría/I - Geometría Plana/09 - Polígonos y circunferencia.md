---
dg-publish: true
---

# ⭕ Polígonos y Circunferencia

## 🎯 Introducción

> [!info] 💡 ¿Cómo se relacionan polígonos y círculos?
>
> Un polígono es **inscrito** (vértices sobre el círculo) o **circunscrito** (lados tangentes). Los inscritos cumplen Ptolomeo y Brahmagupta; los circunscritos, Pitot — y los regulares son **bicéntricos** (ambos a la vez).
>
> ```mermaid
> graph LR
>     A["Polígono<br/>+ círculo"] --> B{"Vértices<br/>o lados?"}
>     B -->|Vértices en O| C["Inscrito<br/>Ptolomeo"]
>     B -->|Lados tangentes| D["Circunscrito<br/>Pitot"]
>     style C fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U5-ciclico.png]]

> [!tip] 💡 Visual — cuadrilátero cíclico
>
> Los 4 vértices sobre el círculo: opuestos suman $180°$ (criterio de ciclicidad) y vale Ptolomeo $AC\cdot BD=AB\cdot CD+BC\cdot AD$.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Inscrito, circunscrito y bicéntrico
>
> **Inscrito (cíclico):** vértices sobre el círculo $\iff$ opuestos suplementarios ($\alpha+\gamma=\beta+\delta=180°$).
>
> **Circunscrito (tangencial):** lados tangentes $\iff a+c=b+d$ (Pitot: tangentes desde un vértice iguales).
>
> **Bicéntrico:** ambas a la vez. Todos los regulares lo son; en cuadriláteros solo casos como el cuadrado.

> [!tip] 💡 Cómo decidir sin dudar
>
> ¿Vértices sobre un círculo? Prueba opuestos $=180°$ (cíclico). ¿Lados tangentes a un círculo? Prueba $a+c=b+d$ (tangencial). Si un cuadrilátero cumple **ambas**, es bicéntrico y su área es $\sqrt{abcd}$.

> [!example] 🟢 Ejemplo — Rombo $5,5,5,5$: ¿cíclico? ¿tangencial?
>
> Opuestos: rombo general no tiene opuestos $180°$ (salvo cuadrado) $\therefore$ no cíclico. Lados: $5+5=5+5$ ✓ $\therefore$ **sí** tangencial (todo rombo lo es).

---

## 📋 Tabla Comparativa: Teoremas

> [!note] 📋 Qué dice cada teorema y cuándo usarlo
>
> | Teorema | Fórmula | Uso |
> |---|---|---|
> | **Ptolomeo** (cíclico) | $AC\cdot BD=AB\cdot CD+BC\cdot AD$ | Diagonales desde lados |
> | **Pitot** (tangencial) | $a+c=b+d$ | Decide si admite incírculo |
> | **Brahmagupta** (cíclico) | $A=\sqrt{(s-a)(s-b)(s-c)(s-d)}$ | Área (Herón con un lado $\to0$) |
> | **Inscrito** | mitad del central | Ángulos en el círculo |
> | **Euler** $OI$ | $OI^2=R(R-2r)$ | Distancia entre centros |
> | **Aproximación $\pi$** | $n$-gono inscrito/circunscrito | Arquímedes: $3.14$ con $96$ lados |

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Todo rombo es cíclico:** solo el cuadrado (rombo con $90°$); el rombo general no tiene opuestos suplementarios.
> - **Ptolomeo en no cíclico:** vale $\le$ (desigualdad), igualdad solo si cíclico.
> - **Brahmagupta sin ciclicidad:** exige vértices concíclicos; si no, usa Bretschneider.
> - **Bicéntrico cualquiera:** en cuadriláteros es rarísimo (cuadrado y deltoides especiales); no todo rombo/rectángulo.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. ¿Cíclico? Opuestos $75°,105°$ y $110°,70°$.
> 2. ¿Tangencial? Lados $2,3,4,3$ ($2+4$ vs $3+3$).
> 3. Brahmagupta con $2,3,4,5$ cíclico ($s=7$).

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $75+105=180$, $110+70=180$ ✓ sí.
>
> **2.** $6=6$ ✓ sí.
>
> **3.** $\sqrt{5\cdot4\cdot3\cdot2}=\sqrt{120}$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Ptolomeo en rectángulo $3\times4$ ($5\cdot5=9+16$).
> 5. Rombo: ¿cíclico? ¿tangencial? Justifica ambas.
> 6. Euler $OI$ en $(3,4,5)$ ($R=2.5,r=1$).

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** Diagonales $5,5$; $9+16=25$ ✓.
>
> **5.** Tangencial sí ($a+c=b+d$); cíclico solo si cuadrado.
>
> **6.** $OI^2=2.5(2.5-2)=1.25$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba Ptolomeo construyendo $E$ en $BD$ con $\angle BAE=\angle CAD$ (semejanza).
> 8. Arquímedes: $\pi$ con $96$-gono (perímetros inscrito/circunscrito).
> 9. Fuss bicéntrico: verifica cuadrado $a$ ($R=a\sqrt2/2$, $r=a/2$).

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $\triangle ABE\sim\triangle ACD$ y $\triangle ADE\sim\triangle ACB$; suma da $AC\cdot BD$.
>
> **8.** $P_{in}<2\pi<P_{out}$ con $n=96$: $3.1408<\pi<3.1429$.
>
> **9.** $(R+r)^2$ vs... con círculos concéntricos el cuadrado cumple ambas definiciones.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Decido cíclico (opuestos $180°$) y tangencial ($a+c=b+d$).
> - [ ] Aplico Brahmagupta en cíclicos dados.
> - [ ] Reconozco rombo tangencial no cíclico.
> - [ ] Uso inscrito $=$ mitad del central.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Verifico Ptolomeo en rectángulos y cuadrados.
> - [ ] Hallo $OI$ con Euler en triángulos rectángulos.
> - [ ] Distingo bicéntrico de solo-cíclico/solo-tangencial.
> - [ ] Aproximo $\pi$ con polígonos inscritos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro Ptolomeo por semejanza con punto auxiliar.
> - [ ] Pruebo Arquímedes con $n$-gonos y límites.
> - [ ] Verifico Fuss en el cuadrado.
> - [ ] Relaciono Herón–Brahmagupta–Bretschneider como familia.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] A. Baldor, *Geometría*, 2da ed., Patria — cap. de polígonos y círculo.
>
> [2] R. D. Swokowski, *Geometría Analítica* — cap. 2 (cónicas y teoremas).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[06 - Cuadriláteros]] — cíclicos ($180°$) y tangenciales ($a+c$).
> - [[08 - Circunferencia y círculo]] — inscrito y potencia.
> - [[10 - Funciones en Conjuntos]] — biyecciones en Poncelet.
> - [[02 - Circunferencia]] — forma analítica del círculo.

---

**Tags:** #poligonos-circulo #ptolomeo #brahmagupta #geometria #unidad5

---
dg-publish: true
---

# 🧪 Simulacro — Lección Lunes 18 (U1 + U2-01–03)

> [!info] 💡 Cómo usar este simulacro
>
> - Tapa las soluciones (`✅` plegadas) y responde en voz alta o en papel, como en la lección.
> - U1 (ej. 1–4) ya salió en el Control02: van rápido, son calentamiento.
> - U2-01–03 (ej. 5–10) es lo nuevo probable: arquitectura, componentes y UML clases.
> - Meta: 8/10 sin mirar. Lo que falles → tarjeta SR de su nota.

## U1 — Calentamiento SOLID

> [!example] ✏️ Ejercicio 1 — Las 5 de Main.java
>
> En [[Main.java]] hay una violación por principio. Nómbralas en orden S-O-L-I-S-P… digo, S-O-L-I-D.
>
> > [!success]- ✅ Solución
> >
> > - **S:** `Employee` calcula bono + genera PDF + manda email (3 razones para cambiar).
> > - **O:** `BonusReport.describe()` con cadena `instanceof` (cada tipo nuevo lo modifica).
> > - **L:** `TemporaryEmployee` lanza `UnsupportedOperationException` (no sustituye al padre).
> > - **I:** `EmployeeTasks` obliga `manage()` a quien no gerencia.
> > - **D:** `ServicePerson` hace `new MySql()` adentro (depende de lo concreto).

> [!example] ✏️ Ejercicio 2 — SRP y los 3 actores
>
> ¿Por qué `Employee` con `calculatePay()`, `reportHours()` y `save()` viola SRP aunque "hace cosas de empleados"?
>
> > [!success]- ✅ Solución
> >
> > Porque responde a 3 actores (CFO, COO, CTO): un cambio pedido por uno puede romper a los otros (duplicación accidental + merges). SRP = un módulo, un actor.

> [!example] ✏️ Ejercicio 3 — OCP del reporte
>
> El resumen financiero sale en web y ahora debe salir en impresora B/N. ¿Qué permite OCP y qué protege?
>
> > [!success]- ✅ Solución
> >
> > Agregar el formato sin modificar una línea vieja; SRP separa cálculo de presentación y el **Interactor** (alto nivel) queda protegido de BD, Controlador y Vistas.

> [!example] ✏️ Ejercicio 4 — Square no es Rectangle
>
> `r.setW(5); r.setH(2); assert(area == 10)` falla si `r` es un `Square`. ¿Qué principio viola y cuál es la regla?
>
> > [!success]- ✅ Solución
> >
> > LSP: el subtipo debe aguantar todo lo que el cliente hace con el padre. Regla: si necesitas `if` por tipo en el cliente, no son sustituibles.

## U2-01 — Arquitectura y estilos

> [!example] ✏️ Ejercicio 5 — Los dos niveles
>
> ¿Cuáles son los dos niveles del diseño y qué prohíbe la regla del docente?
>
> > [!success]- ✅ Solución
> >
> > Arquitectural (qué piezas y cómo se hablan) y detallado (qué clases e interfaces exactas). Regla: no se codifica lo que no pasó por ambos.

> [!example] ✏️ Ejercicio 6 — Microservicios para 3 endpoints
>
> Sistema de 3 endpoints para 10 usuarios. ¿Qué estilo eliges y por qué no microservicios?
>
> > [!success]- ✅ Solución
> >
> > Monolito modular en capas (equipo chico, proyecto semestral). Microservicios = más YAML que código: overkill sin equipos independientes.

## U2-02 — Componentes e interfaces

> [!example] ✏️ Ejercicio 7 — La interfaz de 25 métodos
>
> `ISistema` con 25 métodos de reportes, pagos y envíos. ¿El diagnóstico y la cura?
>
> > [!success]- ✅ Solución
> >
> > God Interface: todo cambio la rompe. Dividir por rol (`IReportes`, `IPagos`, `IEnvíos`). Regla: si un cliente usa menos del 50%, está obesa.

> [!example] ✏️ Ejercicio 8 — Fachada que calcula
>
> `TiendaFacade.comprar()` suma totales, valida y persiste. ¿Qué está mal y cuál es la regla?
>
> > [!success]- ✅ Solución
> >
> > La fachada implementa en vez de orquestar (viola SRP + delegación). Regla: orquesta, no implementa — si crece, esconde un diseño pendiente.

## U2-03 — UML clases

> [!example] ✏️ Ejercicio 9 — `Curso extends Lista`
>
> ¿Por qué `class Curso extends Lista` está mal aunque "reusa el método"?
>
> > [!success]- ✅ Solución
> >
> > Un Curso NO ES una Lista (es-un falso, sin sustitución real). Heredar por pereza contamina el subtipo. Cura: asociación o composición; hereda solo con es-un + LSP.

> [!example] ✏️ Ejercicio 10 — El extremo mudo
>
> `Estudiante — * Curso` (un solo lado con multiplicidad). ¿Qué falta y cómo queda?
>
> > [!success]- ✅ Solución
> >
> > Falta el otro extremo: la cardinalidad queda adivinada. Completo: `Estudiante 1..* — * Curso` (ambos extremos siempre; si no sabes el número, `*` + anota el supuesto).

---

## ✅ Checklist pre-lección

> [!note] 🎯 Nivel listo
>
> - [ ] Digo las 5 violaciones de Main.java sin mirar.
> - [ ] Elijo estilo por contexto (equipos, datos, flujo), no por moda.
> - [ ] Detecto God Interface, fachada obesa y es-un falso en código ajeno.
> - [ ] Hice este simulacro: _____/10.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - U1: [[04 - Principios SOLID]]
> - U2: [[01 - Diseño arquitectónico y estilos]] · [[02 - Diseño por componentes e interfaces]] · [[03 - UML clases, objetos y relaciones]]

**Tags:** #CCPG1042 #simulacro #leccion #solid #uml #diseno-software

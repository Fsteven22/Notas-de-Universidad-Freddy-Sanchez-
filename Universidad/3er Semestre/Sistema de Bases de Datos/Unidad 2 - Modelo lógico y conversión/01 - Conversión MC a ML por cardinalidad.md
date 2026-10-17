---
dg-publish: true
tags: [TICG1018, unidad2, modelo-logico, conversion, ml]
---

# 🔄 Conversión del Modelo Conceptual al Modelo Lógico

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Convertir?
>
> El modelo conceptual (ER) dice **qué existe**; el modelo lógico dice **cómo se guarda en tablas**. Convertir es traducir cada entidad, relación y restricción a tablas + claves sin perder información. Es el corazón de la Lección 1.
>
> **Dónde estamos en el diseño (3 pasos):**
>
> 1. **Análisis de requerimientos** → qué necesita el usuario.
> 2. **Diseño conceptual** → se identifican datos y restricciones (ER).
> 3. **Diseño lógico y físico** → se crean tablas, relaciones, restricciones; luego procedimientos y triggers.
>
> **Analogía del mundo real:** el ER es el plano arquitectónico; el ML es la lista de materiales con medidas exactas. El plano sin lista no se construye.
>
> | Concepto | Modelo Conceptual | Modelo Lógico |
> |---|---|---|
> | **Entidad** | Rectángulo Chen | Tabla |
> | **Atributo** | Óvalo | Columna |
> | **Instancia** | — | Fila (tupla) |
> | **Relación** | Rombo | FK o tabla intermedia |
> | **Regla de oro** | Qué existe | Cómo se guarda |

![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-01-graph.svg]]

---

## 📋 Definiciones Formales

> [!info] ℹ️ Cómo leer esta sección
> Una definición por bloque con su figura. Cada figura anticipa la regla donde se usa.

### 1️⃣ Tabla, columna, fila — el vocabulario lógico

> [!note] 📋 Definición — Tabla, columna, fila, campo
>
> Tabla = relación; columna = atributo con dominio; fila = tupla; campo = intersección fila-columna.
> Equivalencia: tabla/fila/columna = archivo/registro/campo = relación/tupla/atributo.
>
> | Tabla EMPLEADO | idEmpleado (PK) | nombre |
> |---|---|---|
> | Fila 1 (tupla) | 101 | Ana |
> | Fila 2 (tupla) | 102 | Luis |
>
> **Ejemplo:** la columna `nombre` tiene dominio texto; el campo (102, nombre) vale `Luis`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-02-graph.svg]]
>
> **Se lee así:** la tabla contiene filas y columnas; donde se cruzan hay un campo con exactamente un valor.

### 2️⃣ Claves — PK, candidatas y compuestas

> [!note] 📋 Definición — Claves
>
> Una o más columnas que identifican filas. **Única** = una fila; **compuesta** = 2+ atributos; **primaria (PK)** = única por tabla (representa la tabla en relaciones, organiza almacenamiento, genera índices); **candidatas** = únicas adicionales no elegidas.
>
> **Ejemplo:** en REGISTRO ninguna columna sola identifica (un profesor dicta varias materias); `idProf + matricula + idMateria` sí → PK compuesta de 3.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-03-er.svg]]
>
> **Se lee así:** `PK` identifica, `FK` referencia, `UK` es candidata no elegida (`nombre` único pero no PK), `PK, FK` es compuesta que además referencia.

### 3️⃣ Integridad de entidad y referencial — lo que nunca se rompe

> [!note] 📋 Definición — Integridad
>
> - **De entidad:** la PK nunca es nula ni se repite.
> - **Referencial:** toda FK apunta a una PK que existe (la FK no necesita ser única donde está, pero sí donde apunta).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-04-flow.svg]]
>
> **Ejemplo:** matricular el carnet 999 inexistente se rechaza; la BD protege sola lo que en archivos había que programar.

### 4️⃣ Padre e hijo — quién recibe la FK

> [!note] 📋 Definición — Padre / Hijo (en 1:M)
>
> El lado `1` es **padre**; el lado `M` es **hijo** y recibe la FK.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-05-er.svg]]
>
> **Ejemplo:** rotula el `1` primero y la dirección sale sola (ver Regla 3).

### 5️⃣ Fusión de tablas — el ML mínimo

> [!note] 📋 Definición — Fusión
>
> El ML debe tener el **mínimo de tablas posible**: las de un solo atributo se eliminan y las 1:1 total-total se fusionan.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-06-graph.svg]]
>
> **Ejemplo:** EQUIPO–PRESIDENTE (1,1)-(1,1) → una sola tabla con `cedula_presi` dentro (ver Regla 4, caso C).

### 6️⃣ Modelo lógico — el refinamiento

> [!note] 📋 Definición — Modelo lógico
>
> Refinamiento del conceptual donde se reducen/aumentan entidades y solo quedan las que serán tablas; después **se normaliza**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-07-graph.svg]]
>
> **Ejemplo:** el rombo *toma* (conceptual) se vuelve tabla MATRÍCULA (lógico); luego 1FN verifica que no tenga grupos repetitivos.

---

## 🛠️ Método: Convertir Paso a Paso

> [!success] 🏆 Protocolo de conversión (úsalo en la Lección 1)
>
> 1. **Entidades → tablas directas:** cada entidad es una tabla; sus atributos, columnas; su PK se mantiene.
> 2. **M:N → tabla intermedia:** con las PK de ambos lados (PK,FK) + atributos propios de la relación.
> 3. **1:M → FK al hijo:** copia la PK del padre (lado 1) como FK en el hijo (lado M); los atributos de la relación viajan al hijo.
> 4. **1:1 → según participación** (ver tabla de 3 casos abajo).
> 5. **Especiales:** supertipo/subtipo, dependencia, recursiva (ver sección).
> 6. **Normaliza** el esquema resultante (mínimo [[02 - Primera forma normal y diccionario de datos|1FN]]).

### 🔍 Regla 1 — Entidades → tablas directas

> [!note] 📋 Cada entidad, una tabla
>
> Cada entidad del modelo conceptual se transforma directamente en una tabla: los atributos pasan a ser columnas y la clave primaria se mantiene.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-08-er.svg]]
>
> **Se lee así:** la entidad CLIENTE con 4 atributos produce una tabla de 4 columnas donde `idCliente` identifica cada fila.

---

### 🔍 Regla 2 — M:N → tabla intermedia siempre

> [!example] 🧪 Rentar (CLIENTE–PROPIEDAD)
>
> La relación se convierte en tabla con las claves primarias de **ambas** entidades (cada una PK y FK a la vez), más los atributos propios de la relación.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-09-er.svg]]
>
> **Se lee así:** `RENTAR` no existía como entidad, nace de la relación; sus dos claves apuntan a cada lado y las fechas viven con ella.
>
> **Mismo patrón — Venta:** `DETALLE(idProd PK, FK, codigo PK, FK, cantidad)` entre PRODUCTO y VENTA; los `=` del diagrama de clase confirman qué columna referencia a qué PK.

---

### 🔍 Regla 3 — 1:M → la FK vive en el hijo

> [!example] 🧪 Trabaja (EMPLEADO–DEPARTAMENTO)
>
> El lado `1` es el **padre** y el lado `M` es el **hijo**: se copia la PK del padre como FK en la tabla del hijo. Si la relación tiene atributos propios, también bajan al hijo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-10-er.svg]]
>
> **Se lee así:** un departamento tiene muchos empleados; cada empleado guarda `idDepartamento` diciendo a cuál pertenece. `fechaTrabaja` (atributo del rombo) baja con él.
>
> **Mismo patrón — Registra:** `RESERVACION(idReservacion PK, fechaLlegada, horaLlegada, diasPermanencia, FK idUsuario)` recibe además `fechaReservacion, horaReservacion` de la relación; `USUARIO` no recibe nada.

---

### 🔍 Regla 4 — 1:1 → tres casos por participación

> [!note] 📋 Memoriza cada caso con su ejemplo
>
> **Caso A — (0,1) vs (1,1): propaga del (1,1) al (0,1).** Ejemplo CLIENTE–PREFERENCIA (`establece`):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-11-er.svg]]
>
> **Se lee así:** no todo cliente fija preferencia (0,1), pero toda preferencia es de un cliente (1,1); la PK viaja al lado opcional.
>
> **Caso B — participación parcial: decide PADRE e HIJO.** Ejemplo PERSONA–LICENCIA (`posee`): no toda persona tiene licencia (parcial), pero toda licencia es de una persona. La persona es padre, la licencia hija:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-12-er.svg]]
>
> **Se lee así:** la PK del padre (`cedula`) se copia al hijo como FK. `PERSONA` no recibe nada. Sin persona no hay licencia (pero sí hay personas sin licencia).
>
> **Caso C — (1,1) vs (1,1): unifica en una sola tabla.** Ejemplo EQUIPO–PRESIDENTE (`tiene`):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-13-er.svg]]
>
> **Se lee así:** una sola tabla con la PK de cualquiera de las dos; los datos del presidente viven como columnas (`cedula_presi, nombre_presi...`).

---

### 🔍 Regla 5 — Ternaria → una tabla con las 3 claves

> [!example] 🧪 Registro (PROFESOR–MATERIA–ESTUDIANTE)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-14-er.svg]]
>
> **Se lee así:** `REGISTRO` combina las 3 PK como clave compuesta (las 3 son FK a la vez) y cuelga `calificacion, hora` de la combinación completa.

---

### 🔍 Regla 6 — Supertipo–subtipo → el caso manda: (a) 3 tablas, (b) 1 tabla, (c) mixto, (d) ancha

> [!note] 📋 Las 4 conversiones del deck BD02 (una por combinación)
>
> **(a) {obligatorio, sobrelapado} → 3 tablas** (cada tipo la suya, banderas en el padre):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-15-er.svg]]
>
> **(b) {obligatorio, disjunto} → 1 sola tabla** con discriminador (nadie es dos cosas: no hacen falta hijos):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-16-er.svg]]
>
> **(c) {opcional, disjunto} → supertabla + hijos solo si aplican** (`Tipo` admite nulo; el hijo lleva la PK como (PK,FK) cuando existe).
>
> **(d) {opcional, sobrelapado} → 1 tabla ancha** (banderas + todos los atributos propios juntos; sin tablas hijas).
>
> **Se lee así:** (a) separa porque hay solape real; (b) colapsa porque el discriminador basta; (c) respeta lo opcional con nulos; (d) todo junto porque nada obliga a partir. La regla vieja *"una tabla por tipo"* solo valía para (a).
>
> **Cómo detectar la jerarquía (caso empleados):** caza 2 frases — *"hay personal que no encaja"* = parcial; *"nadie desempeña dos perfiles"* = exclusiva. Si el enunciado calla, **pregunta al cliente**: no se adivina.
>
> **Regla de oro:** las relaciones salen de los **subtipos**, no del supertipo — *atiende* cuelga de VENDEDOR (un desarrollador no atiende clientes). Colgarla de EMPLEADO afirma que cualquiera puede tener clientes: error de modelado.
>
> > [!quote] 📖 C. Zavaleta, *MER: guía completa*, caso empleados con generalización (2026)

---

### 🔍 Regla 7 — Dependencia → la débil hereda la PK fuerte

> [!example] 🧪 Edificio–Departamento
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-17-er.svg]]
>
> **Se lee así:** el departamento débil no se identifica solo (`hab_num` se repite entre edificios); su PK es compuesta: la del fuerte heredada + su número.

---

### 🔍 Regla 8 — Recursiva → FK a sí misma o intermedia doble

> [!example] 🧪 Supervisión y grupos de empleados
>
> **Recursiva 1:M** (un jefe supervisa empleados):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-18-er.svg]]
>
> **Se lee así:** `idSupervisor` es FK que apunta a `idEmpleado` de la **misma** tabla (`idEmpleado = idSupervisor`).
>
> **Roles obligatorios (caso banco):** en reflexivas etiqueta cada rama (*principal* / *dependiente*) o el diagrama es ilegible. *Depende* (SUCURSAL–SUCURSAL): principal (0,n) vs dependiente (0,1) — hay oficinas que no dependen de ninguna.
>
> > [!quote] 📖 C. Zavaleta, *MER: guía completa*, caso entidad bancaria (2026)
>
> **Recursiva M:N** (grupos donde ambos roles son empleados): tabla intermedia con doble FK → `EMPLEADO_GRUPOS(idEmpSupervisor PK, FK, idEmpSupervisado PK, FK)`.

---

## 🔁 Conversión inversa — del ML al MC (viceversa)

> [!note] 📋 Definición — Leer tablas y reconstruir el ER
>
> Dadas las tablas con sus PK/FK, recupera el conceptual: cada tabla es una entidad, cada FK es una relación y cada tabla intermedia es un rombo. Es la lectura inversa del protocolo MC→ML: si sabes convertir hacia adelante, sabes leer hacia atrás buscando las huellas que dejó cada regla.
>
> | Huella en las tablas | Origen en el ER |
> |---|---|
> | Tabla con PK compuesta de 2 (PK,FK) + atributos propios | M:N con intermedia (Regla 2) |
> | Tabla con PK compuesta de 3 (PK,FK) | Ternaria (Regla 5) |
> | FK simple en una tabla | 1:M: la tabla con la FK es el hijo (Regla 3) |
> | PK que es a la vez FK a otra tabla | Supertipo→subtipo o 1:1 fusionable (Regla 6 / caso C) |
> | FK que apunta a la misma tabla | Recursiva 1:M (Regla 8) |
> | Tabla intermedia con doble FK a la misma tabla | Recursiva M:N (Regla 8) |
> | Tabla de (FK + un valor) con PK compuesta | Multivaluado (U2-02 §6) |
> | PK heredada del fuerte + número local | Entidad débil (Regla 7) |
>
> **Protocolo inverso (en orden):**
>
> 1. Marca todas las PK y FK de cada tabla.
> 2. Las tablas cuya PK es compuesta solo de FK → intermedias: dibuja el rombo con sus participantes.
> 3. Las FK simples → flechas 1:M hacia el padre (la tabla referenciada).
> 4. Las PK compartidas → supertipo (padre) y subtipos (hijos); si no hay atributos propios, era una 1:1 fusionable.
> 5. Reconstruye cardinalidades preguntando el negocio en ambas direcciones (U1-02 §frases): las tablas no guardan (x,y), tú las deduces.

### ✏️ Ejercicio inverso 1 — MATRÍCULA

> [!example] 🧪 Planteamiento
> - Tablas: `ESTUDIANTE(carnet PK, nombre)`, `MATERIA(cod PK, nombre)`, `MATRICULA(carnet PK/FK, cod PK/FK, nota)`. Reconstruye el ER.
>
> > [!success]- Solución
> > - MATRICULA tiene PK compuesta de 2 FK + atributo propio (nota) → intermedia de M:N.
> > - ER: ESTUDIANTE —*toma*— MATERIA (M:N, atributo nota en el rombo); carnet y cod subrayados como PK.

### ✏️ Ejercicio inverso 2 — El supervisor fantasma

> [!example] 🧪 Planteamiento
> - Tablas: `EMPLEADO(id PK, nombre, idSup FK→EMPLEADO)`, `VENDEDOR(id PK/FK→EMPLEADO, numVentas)`, `VENTA(id PK, fecha, idEmp FK→EMPLEADO)`. Reconstruye el ER.
>
> > [!success]- Solución
> > - idSup a la misma tabla → recursiva *supervisa* 1:M con roles (supervisor/supervisado).
> > - VENDEDOR con PK compartida + atributo propio → subtipo de EMPLEADO (supertipo, caso a).
> > - VENTA con FK simple → EMPLEADO 1:M *realiza* (cuelga del supertipo: cualquiera vende, como el caso subsidio de la Guía 1).

---

## 🎨 Ejemplo Trabajado Completo

> [!example] 💡 De ER a tablas: trabaja (EMPLEADO–DEPARTAMENTO)
>
> **ER de partida:** `EMPLEADO(idEmpleado, nombre, dirección, teléfono)` —(trabaja, fechaTrabaja)→ `DEPARTAMENTO(idDepartamento, nombre)`, cardinalidad M:1.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-19-graph.svg]]
>
> **Conversión:**
>
> 1. Entidades → tablas (PK se mantienen).
> 2. Relación 1:M → FK al hijo + atributo `fechaTrabaja` al hijo.
>
> **Tablas resultantes:**
>
> | Tabla | Columnas (PK/FK marcadas) |
> |---|---|
> | **EMPLEADO** | idEmpleado PK int, nombre char(30), dirección char(50), teléfono int, **FK** idDepartamento int, fechaTrabaja date |
> | **DEPARTAMENTO** | idDepartamento PK int, nombre char(30) |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-20-er.svg]]
>
> **Se lee así:** el Chen de arriba convertido: el rombo desaparece, nace la FK en el hijo y `fechaTrabaja` baja con ella. Compara ambos dibujos línea por línea.
>
> **Verificación:** ¿puedo despedir un departamento con empleados? No — la FK lo impide (integridad referencial). ¿Dos empleados con mismo id? No — PK única.

---

## 🗺️ Diagrama de Decisión: ¿Cómo Convierto Esta Relación?

![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-21-flow.svg]]

---

## ⚠️ Errores Comunes y Principios Lógicos

> [!warning] ⚠️ Cómo leer esta sección
> Cada error trae su diagrama: primero lo **malo** (❌) y luego lo **correcto** (✅). Si tu conversión se parece al primero, ya sabes qué regla aplicar.

### ❌ Error 1: FK al revés en 1:M

> [!danger] ❌ Viola: dirección padre→hijo
>
> Poner la FK en el padre (lado 1) es absurdo: un departamento tendría que apuntar a **uno** de sus 50 empleados.
>
> ❌ Así NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-22-er.svg]]
>
> ✅ Así SÍ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-23-er.svg]]
>
> **Regla que lo evita:** en 1:M el hijo (M) recibe; el padre (1) no apunta a nadie.

---

### ❌ Error 2: M:N sin tabla intermedia

> [!danger] ❌ Viola: primera forma normal (grupos repetitivos)
>
> Aplanar la relación en columnas numeradas crea un grupo repetitivo: ¿y si una venta lleva 4 productos?
>
> ❌ Así NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-24-er.svg]]
>
> ✅ Así SÍ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-25-er.svg]]
>
> **Regla que lo evita:** toda M:N produce tabla intermedia con las PK de ambos lados.

---

### ❌ Error 3: 1:1 total-total en dos tablas

> [!danger] ❌ Viola: fusión mínima de tablas
>
> Si cada equipo tiene exactamente un presidente y viceversa, dos tablas solo generan un JOIN obligatorio en cada consulta.
>
> ❌ Así NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-26-er.svg]]
>
> ✅ Así SÍ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-27-er.svg]]
>
> **Regla que lo evita:** caso C (1,1)-(1,1) se unifica en una sola tabla.

---

### ❌ Error 4: Atributos de la relación olvidados

> [!danger] ❌ Viola: preservación de información
>
> Convertir `Registra` bajando solo la FK pero perdiendo `fechaReservacion, horaReservacion` destruye datos del conceptual.
>
> ❌ Así NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-28-er.svg]]
>
> ✅ Así SÍ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-29-er.svg]]
>
> **Regla que lo evita:** todo atributo del rombo viaja a la tabla que absorbe la relación.

---

### ❌ Error 5: Subtipo sin PK heredada

> [!danger] ❌ Viola: identidad del supertipo
>
> Darle al subtipo una PK propia rompe el vínculo: ya no se sabe qué empleado es ese vendedor.
>
> ❌ Así NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-30-er.svg]]
>
> ✅ Así SÍ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-31-er.svg]]
>
> **Regla que lo evita:** cada subtipo lleva la PK del supertipo como (PK,FK) — en los casos (a) y (c); en (b) y (d) no hay tablas hijas que hereden.

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist de conversión
>
> **1. Marca padre e hijo antes de escribir** — en 1:M no hay ambigüedad si rotulas el `1`.
>
> **2. Dibuja los `=` de referencia** — como en el diagrama de clase: cada FK anota a qué PK apunta.
>
> **3. Cuenta tablas al final** — ¿alguna tiene un solo atributo? Elimínala. ¿Alguna 1:1 total-total? Fusiónala.
>
> **4. Lee la relación en voz alta** — "un empleado trabaja en un departamento" te dice dónde va la FK.
>
> **5. Normaliza después** — la conversión produce el esquema; [[02 - Primera forma normal y diccionario de datos|1FN]] lo valida.

---

## 📝 Ejercicios Propuestos

> [!info] ℹ️ Cómo trabajarlos
> Cada ejercicio trae su **planteamiento visual** (lo que te dan) y la **solución guiada** (cómo se llega). Tapa la solución, resuelve, compara.

### ✏️ Ejercicio 1 — Ternaria con atributos

> [!example] 📋 Planteamiento
>
> Convierte esta relación ternaria: `ESTUDIANTE(Matrícula PK, nombre, apellido)` —registra(calificación, hora)→ `MATERIA(idMateria PK, nombre, descripción)`, con `PROFESOR(idProf PK, ...)` como tercer participante.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-32-er.svg]]
>
> > [!success]- ✅ Solución guiada
> >
> > 1. Las 3 entidades dan 3 tablas con sus PK intactas.
> > 2. La ternaria produce `REGISTRO` con las 3 PK como (PK,FK) cada una.
> > 3. `calificacion, hora` cuelgan de la combinación completa.
> >
> > | Tabla | Claves |
> > |---|---|
> > | ESTUDIANTE | Matricula PK, nombre, apellido |
> > | MATERIA | idMateria PK, nombre, descripción |
> > | PROFESOR | idProf PK, ... |
> > | REGISTRO | idProf PK,FK + Matricula PK,FK + idMateria PK,FK + calificacion + hora |

---

### ✏️ Ejercicio 2 — Supertipo con pregunta trampa

> [!example] 📋 Planteamiento
>
> `PRODUCT` supertipo con subtipos `CD` y `BOOK`. ¿Es obligatorio que toda instancia de PRODUCT esté asociada a un CD? ¿Puede un BOOK no aparecer en PRODUCT? Dibuja la implementación según tu respuesta.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-33-er.svg]]
>
> > [!success]- ✅ Solución guiada
> >
> > 1. La respuesta depende de la restricción: si es {obligatorio, disjunto}, todo PRODUCT es CD o BOOK y ningún BOOK vive fuera de PRODUCT.
> > 2. Si es {opcional,...}, sí puede haber PRODUCT sin subtipo.
> > 3. Implementación: `CD(idProd PK,FK, ...)` y `BOOK(idProd PK,FK, ...)`; discriminante `tipo` si es disjunto.
> >
> > **Trampa del ejercicio:** sin la restricción {obligatorio/opcional, disjunto/sobrelapado} no hay respuesta única — en la lección, exige el dato antes de convertir.

---

### ✏️ Ejercicio 3 — Taller pata de gallo

> [!example] 📋 Planteamiento
>
> Convierte a lógico el diagrama del taller en notación pata de gallo (ejercicio de clase).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-34-flow.svg]]
>
> > [!success]- ✅ Solución guiada
> >
> > 1. Traduce cada pata a cardinalidad con el diagrama de decisión de esta nota.
> > 2. Aplica el protocolo en orden: entidades → M:N → 1:M → 1:1 → especiales.
> > 3. Verifica con el checklist de Mejores Prácticas antes de entregar.

---

### ✏️ Ejercicio 4 — 1:1 con participación mixta

> [!example] 📋 Planteamiento
>
> `CLIENTE(cédula PK, nombre, dirección, teléfono)` + `PREFERENCIA(id_pref PK, tipoPref, maxRent)`, relación `establece` con (0,1) del lado cliente y (1,1) del lado preferencia. ¿Qué caso 1:1 es y dónde va la FK?
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-01-35-er.svg]]
>
> > [!success]- ✅ Solución guiada
> >
> > 1. Participaciones (0,1) vs (1,1) → **caso A**.
> > 2. La PK del lado (1,1) se propaga a la tabla del lado (0,1).
> > 3. Resultado: `PREFERENCIA(id_pref PK, tipoPref, maxRent, FK cedula)`; `CLIENTE` no recibe nada.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u2
- ¿3 pasos del diseño de BD?::Requerimientos → conceptual (ER) → lógico/físico (tablas + triggers).
- ¿Equivalencias tabla/fila/columna?::Archivo/registro/campo = relación/tupla/atributo.
- ¿M:N al lógico?::Tabla intermedia con las PK de ambos lados como (PK,FK) + atributos de la relación.
- ¿1:M dónde va la FK?::En el hijo (lado M); el padre (lado 1) no recibe nada.
- ¿1:1 caso A, B y C?::A: (0,1)-(1,1) propaga PK del 1,1 al 0,1. B: parcial, PK del padre al hijo. C: (1,1)-(1,1) unifica en una tabla.
- ¿Supertipo-subtipo al lógico?::(a) 3 tablas con banderas; (b) 1 tabla con discriminante tipo; (c) supertabla + hijos opcionales; (d) 1 tabla ancha.
- ¿Débil y recursiva?::Débil: PK del fuerte como (PK,FK). Recursiva 1:M: FK a sí misma; M:N: intermedia con doble FK.
- ¿Fusión de tablas en 1 línea?::Mínimo de tablas: elimina las de 1 atributo y fusiona 1:1 total-total.
- ¿Cómo detecto jerarquía parcial/exclusiva?::"No encaja en ninguno" = parcial; "nadie dos perfiles" = exclusiva; si calla, pregunto.
- ¿Reflexiva bien dibujada?::Etiqueto roles (principal/dependiente) en cada rama.
- ¿Intermedia con 2 FK en la PK qué fue?::M:N con atributos propios (el rombo): la leo como relación, no como entidad.
- ¿PK compartida como (PK,FK) qué fue?::Subtipo del supertipo referenciado (o 1:1 total-total si no aporta nada).
- ¿FK a sí misma qué fue?::Recursiva 1:M con roles; doble FK a la misma tabla: recursiva M:N.

> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)
## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Protocolo de conversión MC→ML por cardinalidad
> ✅ Los 3 casos 1:1 + especiales (supertipo, débil, recursiva)
> ✅ Fusión mínima de tablas
>
> **Siguiente:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **1FN y diccionario** | 5 condiciones + documento por tabla | Valida tu conversión (Lección 1) |

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Siguiente: [[02 - Primera forma normal y diccionario de datos]]
> - Base: [[01 - Dato, información y modelos de datos]] · [[02 - Entidades, atributos, claves y relaciones]] · [[03 - Modelo relacional, ERM y casos Tiny College]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Diapositivas BD 02 MC_a_ML (Irene Cheung): diseño en 3 pasos, conversión por cardinalidad, supertipo-subtipo, dependencia, recursiva, 1FN, diccionario.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 4 (claves) y cap. 6 (normalización).

---

**Tags:** #TICG1018 #unidad2 #ml #conversion #bd

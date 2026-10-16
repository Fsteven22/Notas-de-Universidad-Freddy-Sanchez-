---
dg-publish: true
tags: [TICG1018, unidad0, guia, taller1, bd]
---

# 📝 Guía de Problemas 1 — MC, ML y Normalización (Taller 1)

> [!info] ℹ️ Qué es esta guía
> Recopilación de los ejercicios reales de talleres, lecciones y exámenes (2022–2026) que cubren lo del **Taller 1**: modelo conceptual en Chen, conversión a modelo lógico pata de gallo, supertipos, dependencias y normalización hasta 3FN. Los enunciados salen de los PDFs de la Unidad 0; las soluciones y claves son propias.
> - Bloque A: casos de modelado (enunciado + clave + esqueleto del diagrama).
> - Bloque B: dependencias y normalización (resueltos paso a paso, con diagrama).
> - Bloque C: banco de conceptos V/F.
> - Método completo en: [[02 - Entidades, atributos, claves y relaciones]], [[01 - Conversión MC a ML por cardinalidad]], [[02 - Primera forma normal y diccionario de datos]], [[03 - Segunda y tercera forma normal]].

## 🅰️ Bloque A — Modelo conceptual (casos reales)

> [!tip] 📌 Cómo trabajar cada caso
> Lee el enunciado, dibuja el Chen en papel o ERDPlus (rectángulo = entidad, rombo = relación, óvalo = atributo, subrayado = PK), abre la clave, compara. La clave trae lo que el corrector verifica (entidades, identificadores, cardinalidades, la trampa) más el esqueleto del diagrama esperado.

### ✏️ Ejercicio 1 — Lavandería (Taller 1, 2026)

> [!example] 🧪 Planteamiento (fuente: `2026_1PAO_Taller_1_TICG1018.pdf`)
> - Empresa de limpieza en seco; se registran CLIENTES (identificación, nombres, apellidos, teléfono, correo, dirección) con **historial de solicitudes y preferencias**.
> - PRENDAS (descripción, color, material, marca, observaciones, tratamientos especiales por manchas o tejidos delicados).
> - EMPLEADOS (identificación, nombres, apellidos, cargo, fecha de contratación, teléfono, correo) que participan en etapas: recepción, clasificación, limpieza, planchado, entrega.
> - SOLICITUDES (fecha de recepción, fecha estimada de entrega, estado: recibido / en proceso / listo / entregado) con **varias prendas y varios servicios**.
> - SERVICIOS (código, tipo, observación, tiempo estimado, costo).
> - PAGOS (comprobante, fecha, valor, método, estado).
> - 📌 Se pide: conceptual en Chen + lógico en pata de gallo con toda la simbología.
>
> > [!quote]- 📄 Enunciado original
> >
> > 1. Crear el diseño conceptual en notación de CHEN y el diseño lógico en notación pata de gallo considerando toda la simbología vista en clase:
> >
> > Una empresa dedicada a la limpieza de ropa en seco desea implementar un sistema de información para administrar sus operaciones diarias. El sistema debe registrar la información de los clientes, incluyendo datos como número de identificación, nombres, apellidos, teléfono, correo electrónico y dirección. Los clientes pueden realizar múltiples solicitudes de servicio a lo largo del tiempo, por lo que es importante mantener un historial detallado de sus pedidos y preferencias.
> >
> > La empresa recibe diferentes tipos de prendas para su procesamiento, tales como trajes, vestidos, camisas, pantalones y abrigos. De cada prenda se requiere almacenar información como descripción, color, material, marca y observaciones especiales proporcionadas por el cliente. Además, algunas prendas pueden requerir tratamientos específicos debido a la presencia de manchas delicadas, tejidos especiales o instrucciones particulares de cuidado.
> >
> > El proceso de limpieza es realizado por empleados especializados que participan en distintas etapas del servicio, como recepción, clasificación, limpieza, planchado y entrega. De cada empleado se registra información como número de identificación, nombres, apellidos, cargo, fecha de contratación, teléfono y correo electrónico. La empresa necesita conocer qué empleados participaron en cada solicitud para fines de control de calidad y seguimiento de las operaciones.
> >
> > Cada solicitud puede incluir varias prendas y diferentes servicios, tales como limpieza en seco, eliminación de manchas, planchado especial, desinfección o tratamiento de telas delicadas. Para cada servicio se almacena un código único, tipo de servicio, observación, tiempo estimado de ejecución y costo. Asimismo, el sistema debe registrar de cada solicitud la fecha de recepción de las prendas, la fecha estimada de entrega y el estado actual del trabajo, que puede ser recibido, en proceso, listo para entrega o entregado.
> >
> > Finalmente, la empresa necesita gestionar los pagos realizados por los clientes. Para cada transacción se registra un número de comprobante, fecha, valor cancelado, método de pago y estado de la transacción. La gerencia también desea generar reportes sobre los servicios más solicitados, los ingresos obtenidos en determinados períodos y la productividad de los empleados, con el fin de mejorar la calidad del servicio y optimizar la toma de decisiones.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej01-lavanderia.svg]]
>
> > [!success]- Clave de modelado
> > - Entidades: CLIENTE, SOLICITUD, PRENDA, SERVICIO, EMPLEADO, PAGO.
> > - Teléfono del cliente: **multivaluado**. Observaciones de la prenda *en esa solicitud*: atributo de la intermedia, no de PRENDA.
> > - M:N con intermedia y atributos propios:
> >   - SOLICITUD–PRENDA → DETALLE (observaciones de esa prenda en esa solicitud).
> >   - SOLICITUD–SERVICIO → DETALLE (costo y tiempo de ese servicio en esa solicitud).
> >   - SOLICITUD–EMPLEADO → PARTICIPACIÓN (etapa en la que participó).
> > - 1:M: CLIENTE–SOLICITUD (FK cliente en solicitud); SOLICITUD–PAGO (FK solicitud en pago).
> > - Trampa: el historial **no** es entidad (sale de CLIENTE 1:M SOLICITUD con fechas); estado = valor con dominio, no entidad.

### ✏️ Ejercicio 2 — TaxiGo! (Lección 1, 2024)

> [!example] 🧪 Planteamiento (fuente: `Leccion 1 - PAO I 2024.pdf`)
> - USUARIO se registra (nombres, apellidos, fecha de nacimiento, móvil) con usuario y contraseña.
> - Registra el lugar de recojo: calle principal, número, calle secundaria, ciudad.
> - CONDUCTOR (nombres, apellidos, cuenta bancaria, cédula, género, licencia, dirección, teléfono, código único en la compañía).
> - CARRO (placa, gasolina, modelo, color, alquilado sí/no; si es alquilado, datos del PROPIETARIO: nombres, apellidos, dirección, teléfono).
> - CARRERA (origen y destino en texto + latitud/longitud, precio estimado).
> - Al aceptar: se guardan los **primeros 4 dígitos** de la tarjeta + fecha de pago.
> - Se registran cancelaciones y viajes exitosos (estadísticas de uso).
> - 📌 Se pide: modelo conceptual.
>
> > [!quote]- 📄 Enunciado original
> >
> > Lección de Base de datos. Modelo Conceptual. Por favor desarrollar el modelo conceptual del siguiente ejercicio.
> >
> > Se requiere implementar un sistema para la reserva de taxis online llamada TaxiGo!. Un usuario se descarga la aplicación y se registra o inicia sesión. Luego, el usuario registra el lugar donde el taxi deberá recogerlo esto es: calle principal, número de la casa, calle secundaria y ciudad. La aplicación verifica que existan carros disponibles e internamente notifica el pedido a los taxistas más cercanos y el que acepte primero la carrera se le asignará al usuario. Posteriormente, al usuario le aparecerá los datos del taxi y del conductor, así como el tiempo estimado que le tomará al taxi recogerlo y el valor de la carrera. Finalmente, si el usuario acepta la carrera se procederá a cargar el valor a pagar a su tarjeta de crédito, de lo contrario se cancela la carrera.
> >
> > A la empresa le interesa registrar los datos del cliente (usuario) como los nombres, apellidos, fecha de nacimiento y teléfono móvil. Una vez registrado el cliente se le asigna un usuario y contraseña para la aplicación. Cuando el usuario acepta cualquier carrera en el sistema guarda los primeros 4 números de la tarjeta de crédito y la fecha de pago. Se deberá también mantener un registro de los conductores de los taxis: nombres, apellidos, cuenta bancaria, cédula, género, tipo de licencia, dirección y teléfono. Además, conocer datos del carro como la placa, tipo de gasolina, modelo, color y si su carro es alquilado o no. Si es alquilado se deberá conocer los datos del propietario (nombres, apellidos, dirección y teléfono). Una vez registrado se les asigna a los conductores un código único dentro de la compañía.
> >
> > Los datos de la carrera deben incluir, dirección de origen y destino en texto y también expresados en longitud y latitud, y su precio estimado. A la empresa también le interesa generar estadísticas de uso de la aplicación, por ello es importante registrar también las cancelaciones y viajes que culminaron con éxito.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej02-taxigo.svg]]
>
> > [!success]- Clave de modelado
> > - Lugar de recojo: atributo **compuesto** (principal, número, secundaria, ciudad), no entidad. Coordenadas: compuesto (lat, long).
> > - CONDUCTOR–CARRO: 1:1 (un carro activo) o 1:M con intermedia con fechas si se exige historial — decide y justifica.
> > - PROPIETARIO solo existe si el carro es alquilado: entidad opcional del lado 1 (0:1).
> > - Tarjeta: solo 4 dígitos + fecha (atributo simple de la carrera aceptada); nunca el número completo.
> > - Cancelación vs éxito: **estado** de CARRERA (aceptada / cancelada / culminada); las estadísticas salen por consulta.

### ✏️ Ejercicio 3 — Revista AZM (Taller 1, 2024 / 1E 2022)

> [!example] 🧪 Planteamiento (fuente: `2024_1PAO_Taller_1_TICG1018.pdf`)
> - Autores envían ARTÍCULOS (título, categoría, resumen, cuerpo, tags, ID único, estado informado por email).
> - Revisores asignados por área: **3 por artículo**; autores y coautores de *otros* artículos pueden ser revisores de artículos ajenos.
> - Si se rechaza: se devuelve con criterios y hay **reenvío** (2da revisión con 2 revisores nuevos; si falla, rechazo final).
> - Aprobación exige que **todos** los revisores aprueben.
> - Aprobado → revisores de planta verifican gramática, citado, referencias y formato → publicación.
>
> > [!quote]- 📄 Enunciado original
> >
> > La revista AZM desea digitalizar el proceso de recepción, aprobación y publicación de las investigaciones en su revista, se lo ha contratado a usted para realizar este trabajo:
> >
> > Los autores envían sus artículos a la revista revisando su cumplimiento de los requisitos que demanda la revista, entre ellos están: el tipo de archivo, que no haya sido publicado anteriormente en otra revista, que esté bien citado con fuentes verídicas, etc. El archivo se adjunta a un formulario que solicita el título, la categoría (hardware, software, ux, etc), resumen, cuerpo y tags (etiquetas) del artículo. El estado del artículo se lo informa por email y se lo puede consultar indicando el ID del artículo que es un identificador único asignado al artículo.
> >
> > La revista se encarga de asignar revisores al artículo de acuerdo al área de relacionada. Los autores y coautores del artículo y de otros artículos también son considerados como revisores de otros artículos que no sea el suyo. Se asignan 3 revisores por artículo.
> >
> > Si en la revisión se lo rechaza, se lo devuelve al autor indicando los criterios por el cual no cumplió y dando una última opción a ser reenviado considerando los puntos de la primera revisión. En la segunda evaluación se asignan 2 nuevos revisores. Si aún el artículo no es aprobado en esta segunda revisión, se lo rechaza y el autor es notificado vía email. Para que un artículo sea aprobado todos los revisores deben aprobar su publicación.
> >
> > Una vez que el articulo es aprobado la revista asigna revisores de AZM para verificar gramática, citado, referencias y formato. Una vez aprobado por todos los revisores de la revista, el artículo es publicado.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej03-azm.svg]]
>
> > [!success]- Clave de modelado
> > - AUTOR y REVISOR son **roles** de PERSONA: un autor es revisor de otros artículos, nunca del suyo (restricción; anótala como regla de negocio).
> > - ARTÍCULO–REVISOR es M:N con intermedia EVALUACIÓN (veredicto, criterios, ronda 1/2).
> > - "3 revisores ronda 1, 2 nuevos ronda 2, unanimidad": vive en la app, no en el ER.
> > - Reenvío: el mismo ARTÍCULO con versión/ronda (atributo), no artículo nuevo.
> > - Estado: valor (enviado / observado / aprobado / publicado).

### ✏️ Ejercicio 4 — Subsidio de combustibles (1E, 2024)

> [!example] 🧪 Planteamiento (fuente: `2024-1PAO-1E-SBD.docx`, Sección 2)
> - VEHÍCULO (placa, chasis, tipo, última matriculación, edad, cilindraje, gama: baja/media/alta).
> - SUBSIDIO configurable: porcentaje según edad + cilindraje + gama; **cambia en cualquier momento**.
> - VENTA (tipo de gasolina, cantidad, valor oficial, % de subsidio, total pagado, vendedor, comprador).
> - GASOLINERA (empresa, dirección); CIUDAD compuesta (país, provincia, ciudad, calle principal, secundaria + **referencias**: varias).
> - EMPLEADO vendedor (cédula, nombres, apellidos) con **supervisor que también es empleado y también vende**.
> - Comprador: da sus datos o factura al propietario; **el vehículo cambia de propietario, pero la venta conserva el histórico**.
> - 📌 Se pide: entidades, atributos, relaciones e identificadores.
>
> > [!quote]- 📄 Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > Se le ha asignado crear un sistema para poder registrar y controlar el subsidio focalizado de los combustibles, para esto se ha definido los parámetros para otorgar dichos subsidios son la edad de los vehículos, el cilindraje y la gama (baja, media, alta).
> >
> > Las gasolineras deben integrarse a un sistema único de información vehicular donde se encuentra la información antes mencionada y adicional los datos de la placa, chasis, tipo (suv, van, todo terreno, etc.), fecha de última matriculación.
> >
> > Los subsidios serán otorgados en porcentaje respecto al precio oficial del galón de combustible, ejemplo un carro de gama baja, con 3 años de comprado y 1.5 c.c. de cilindraje tiene un porcentaje de 30% del subsidio, pero, el mismo carro con 15 años de antigüedad tendría 5% del subsidio. Es decir, los subsidios son configurables basándose en los 3 parámetros antes indicados y pueden cambiar en cualquier momento.
> >
> > En cada venta de combustible se debe registrar cual es el tipo de gasolina (super, extra, eco, etc.) la cantidad, el valor oficial, el porcentaje del subsidio, el valor total pagado, el vendedor y el comprador.
> >
> > De la gasolinera se requiere conocer el nombre de la empresa, la dirección. La ciudad está compuesta por país, provincia, ciudad, calle principal, calle secundaria, referencias (pueden ser muchas referencias).
> >
> > Del empleado vendedor se requiere conocer la cédula, nombres, apellidos, y su supervisor que también es un empleado. Se debe contemplar que el supervisor puede vender también gasolina por lo cual la venta debería quedar registrado a nombre de dicho supervisor.
> >
> > Cuando se realiza la venta el comprador puede decidir dar sus datos o pedir que le facturen a nombre del propietario del vehículo, de ambos, los datos a almacenar son cédula, nombre, apellidos, correo electrónico. Recuerde que un vehículo puede cambiar de propietario, pero la venta debería mantener el histórico del propietario que se le vendió el combustible.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej04-subsidio.svg]]
>
> > [!success]- Clave de modelado
> > - EMPLEADO *supervisa* EMPLEADO: **recursiva** 1:M con roles (supervisor / supervisado); la VENTA cuelga de EMPLEADO sin distinguir (ambos venden).
> > - Histórico de propietarios: VEHÍCULO–PROPIETARIO es M:N con intermedia TENENCIA (fecha desde / hasta); la VENTA referencia al propietario **de ese momento**.
> > - CIUDAD: entidad con ubicación compuesta + multivaluado referencias.
> > - SUBSIDIO: entidad de configuración con vigencia (desde / hasta) porque cambia en el tiempo; la VENTA copia el % aplicado (foto del momento).

### ✏️ Ejercicio 5 — Concursos del ministerio (1E, 2025)

> [!example] 🧪 Planteamiento (fuente: `2025-1PAO-1E-SBD.docx`, Sección 1)
> - ESTUDIANTE (cédula, nombres, apellidos, fecha de nacimiento, escuela); ESCUELA (nombre, dirección, teléfono, email).
> - CONCURSO (nombre, descripción, fecha del evento, inicio/cierre de inscripción, costo, premios).
> - PREMIOS por puesto (puesto + descripción; N premios libres, ej. 1er lugar: $200 en cines).
> - INSCRIPCIÓN registra fecha y valor pagado (descuento por registro temprano).
> - COMITÉ de PROFESORES (nombres, apellidos, teléfono, email, perfil profesional).
> - CRITERIOS por concurso (nombre, descripción, puntaje máximo).
> - Cada miembro califica a cada participante en cada criterio; resultados archivados.
> - 📌 Se pide: modelo conceptual.
>
> > [!quote]- 📄 Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > Se requiere crear una aplicación para el ministerio de educación que permita llevar el control de los concursos en los que participan los estudiantes de las escuelas de acuerdo con las siguientes especificaciones:
> >
> > De cada estudiante se tendrá la siguiente información: cédula, nombres, apellidos, fecha de nacimiento y la escuela a la que pertenece. De cada escuela se tendrá la siguiente información: nombre, dirección, teléfono, email.
> >
> > De cada concurso se almacenará la siguiente información: nombre, descripción, fecha y hora del evento, fecha de inicio de inscripción, fecha de cierre de inscripción, costo de inscripción y premios. Los premios deben especificar a qué puesto corresponde y la descripción del premio. Por ejemplo: Primer lugar: $200 en cines; Segundo lugar: $100 en compras de alimentos; Tercer lugar: $50 en viajes. (Se pueden crear tantos premios como se desee)
> >
> > Una vez que un concurso está creado, puede recibir inscripciones. Al inscribirse un estudiante, se deberá registrar también la fecha de inscripción y el valor de inscripción pagado, ya que podrían existir descuentos por un registro temprano.
> >
> > Cada concurso es evaluado por un comité conformado por varios profesores. El comité es presentado ante el público por lo que se registrará en el sistema la información de cada profesor miembro del comité como nombres, apellidos, teléfono, email y una breve descripción de su perfil profesional.
> >
> > En cada concurso el comité evaluará los criterios de calificación definidos para cada concurso. El criterio incluye el nombre, descripción y el puntaje máximo a obtener. Por ejemplo, un concurso de programación puede tener criterios de eficacia, eficiencia, calidad, etc. Para cada estudiante participante, los miembros del comité registrarán la calificación que obtuvieron en cada criterio. Los estudiantes con los mejores puntajes serán los ganadores de los premios. Los resultados deben quedar registrados para consultas posteriores.
> >
> > (El examen incluye una figura con el modelo.)
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej05-concursos.svg]]
>
> > [!success]- Clave de modelado
> > - INSCRIPCIÓN: intermedia ESTUDIANTE–CONCURSO con atributos (fecha, valor pagado).
> > - PREMIO: **débil** de CONCURSO (puesto + descripción; no existe sin su concurso).
> > - CALIFICACIÓN: ternaria PROFESOR–ESTUDIANTE–CRITERIO (puntaje) — verifica que necesite a los tres (sí: el puntaje es *de un profesor a un estudiante en un criterio*).
> > - Trampa: el comité es agrupación, no entidad (PROFESOR–CONCURSO M:N "integra comité"); el ganador sale por consulta.

### ✏️ Ejercicio 6 — Reforestación NAREN (1E, 2023)

> [!example] 🧪 Planteamiento (fuente: `2023-1PAO-1E-SBD.docx`, Sección 2)
> - EVENTOS (nombre, inicio/fin) con organizadores y voluntarios.
> - ÁREAS con varios PUNTOS de encuentro (coordenadas) y fotos del antes/después.
> - ASISTENTES —organizadores y voluntarios— (cédula, nombre, apellido, nacimiento, dirección, foto).
> - RECOMENDACIONES por evento (botas, agua, abrigo…).
> - ÁRBOLES por área (tipos: guayacán, roble, pino…; cantidad asignada).
> - Asistencia al inicio y al fin del día; GRUPOS con líder y ayudante (**voluntarios, no organizadores**).
> - Registro de árboles no sembrados por área.
> - 📌 Se pide: modelo conceptual.
>
> > [!quote]- 📄 Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios:
> >
> > La empresa Nacional de Recursos Naturales (NAREN) solicita desarrollar un sistema para administrar la reforestación de áreas verdes como bosques, selvas, etc.
> >
> > El sistema debe permitir organizar eventos de reforestación los cuales incluyen a los organizadores y voluntarios. Estos eventos deben contar con la fecha y hora de inicio y de fin, y un nombre. Por cada evento, se debe organizar distintas áreas de reforestación y para cada área pueden existir varios puntos de encuentro. Se debe registrar las coordenadas de los puntos de encuentro, el nombre de las áreas a reforestar y las fotos del antes y el después de cada área.
> >
> > Se requiere almacenar de los asistentes (organizadores y voluntarios) su cédula, nombre, apellido, fecha de nacimiento, dirección domiciliaria y una foto.
> >
> > Para cada evento se publican recomendaciones a los asistentes, por ejemplo: deben vestir botas, traer una cantidad determinada de agua, deben usar abrigo, etc. Se asigna para cada área una cantidad determinada de árboles a sembrar, de los cuales se debe almacenar los tipos de árboles, ejemplo guayacán, roble, pino, etc.
> >
> > Al inicio del día los organizadores toman asistencia de los voluntarios, los dividen en grupos y se le asigna una cantidad determinada de árboles que deben sembrar en un punto de coordenadas de referencia, cada grupo tiene un líder y un ayudante que responden por cada grupo. Tanto líderes como ayudantes son voluntarios, no organizadores.
> >
> > Al final del día, los organizadores deben tomar nuevamente lista a los voluntarios y registrar por cada área si existieron árboles que no fueron sembrados y que cantidad.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej06-naren.svg]]
>
> > [!success]- Clave de modelado
> > - ASISTENTE supertipo con subtipos ORGANIZADOR y VOLUNTARIO (líder/ayudante salen de VOLUNTARIO: **roles**, no subtipos nuevos).
> > - PUNTO débil de ÁREA (coordenadas + orden dentro del área); FOTO: multivaluado del área (antes/después como valores o débil con tipo).
> > - ASISTENCIA: intermedia VOLUNTARIO–EVENTO (jornada inicio/fin, presente sí/no).
> > - GRUPO: junta líder + ayudante + miembros + punto asignado + árboles asignados/sembrados.

### ✏️ Ejercicio 7 — Pho-grah.local (1E, 2023-2)

> [!example] 🧪 Planteamiento (fuente: `2023-2PAO-1E-SBD.docx`, Sección 2)
> - Usuarios (email, nombre, contraseña, edad, género, lugares de interés) suben MEDIOS a LUGARES (edificios, paisajes…).
> - LUGAR con **jerarquía libre** (Ecuador : Guayas : Guayaquil : Malecón : Torre Morisca).
> - MEDIOS en dos grupos: **estáticos** y **dinámicos** (audio/video); cada medio con id, URL, texto corto y **hashtags**; repositorio de medios.
> - Se gestiona qué usuario subió qué medio a qué lugar.
> - 📌 Se pide: entidades, atributos, relaciones e identificadores.
>
> > [!quote]- 📄 Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > La compañía Pho-grah.local (PL) requiere de una aplicación similar a Instagram (IG), por lo que requiere una base de datos relacional que cumpla con los siguientes requisitos de datos:
> >
> > PL describe que el objetivo principal de la aplicación es permitir a los usuarios que puedan subir fotos, archivos de audio, archivos de video, que correspondan a lugares definidos por los usuarios, tales como edificios, paisajes, lugares arquitectónicos, etc.
> >
> > La aplicación debe permitir a múltiples usuarios darse de alta con un perfil de usuario que incluya, correo electrónico, nombre, contraseña, como mínimo, edad, género y lugares de interés.
> >
> > La aplicación debe permitir al usuario crear el concepto de Lugar. Los lugares pueden ser representados de manera jerárquica, por ejemplo: Ecuador: Guayas: Guayaquil: Malecón León Febres Cordero: Torre Morisca. La profundidad de la jerarquía es libre.
> >
> > Considere a las fotos y archivos digitales como medios digitales divididos en dos grupos: medios estáticos y medios dinámicos (audio y video). Estos medios estarán almacenados en un repositorio en donde cada medio está representado por un id, una URL de acceso. A cada medio le corresponde un texto corto y un conjunto de hashtags. La aplicación debe permitir gestionar los medios que los usuarios suban a los lugares.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej07-phograh.svg]]
>
> > [!success]- Clave de modelado
> > - LUGAR *contiene* LUGAR: **recursiva** 1:M de profundidad libre (FK padre).
> > - Hashtags: **multivaluado** de MEDIO (pide tabla propia en el lógico).
> > - MEDIO supertipo con subtipos ESTÁTICO y DINÁMICO (¿aportan algo propio? duración el dinámico, dimensiones el estático; si no, basta atributo tipo — justifica).
> > - SUBIDA: ternaria USUARIO–MEDIO–LUGAR (fecha): el mismo medio puede subirlo varios usuarios a varios lugares (sí necesita a los tres).

### ✏️ Ejercicio 8 — Expresos escolares (1E, 2024-2)

> [!example] 🧪 Planteamiento (fuente: `2024-2PAO-1E-SBD.docx`, Sección 1)
> - Colegios contratan rutas; PADRES registran hogar (coordenadas) y representados (valida el colegio).
> - BUSETAS, CHOFERES (licencia + expiración), AYUDANTES; asignación semanal chofer + buseta + ayudante + ruta (**cambios a media semana** por enfermedad).
> - App envía posición periódica; padres ven distancia, placa, foto y nombre del conductor y ayudante.
> - CHECK de subida/bajada del estudiante (fecha/hora + novedad).
> - Suspensión por falta de pago (la parada desaparece para el chofer).
> - Usuarios con **más de un rol** (chofer con representado en otro colegio).
> - PARADA (lat/long, dirección, referencias, orden); COLEGIO (nombre, logo).
> - 📌 Se pide: entidades, atributos, relaciones e identificadores.
>
> > [!quote]- 📄 Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > Crear el modelo conceptual de un sistema para administrar los recorridos de una empresa de expresos escolares. Para cumplir esto el sistema debe considerar las siguientes reglas de negocio.
> >
> > La empresa tiene contratos de servicios de expreso con diferentes colegios en varias partes del país, los mismos que le detallan las rutas que deben cubrir y los estudiantes que deben recoger en cada ruta.
> >
> > Al inicio del año lectivo los padres de familia se registran en el sistema y marcan las coordenadas de su hogar en la app móvil, adicional ingresan los datos de su o sus representados y posterior son validados por el colegio.
> >
> > La empresa cuenta con varias busetas, conductores y ayudantes; al iniciar la semana cada chofer es asignado a una buseta con un ayudante, los cuales se encargan de hacer el recorrido que tiene asignada la buseta. Se puede dar casos fortuitos ej. Un chofer se puede enfermar a media semana, entonces el cambio se lo realiza cuando sea necesario.
> >
> > El dispositivo móvil del conductor cuenta con una app que va enviando las coordenadas de la posición actual cada cierto tiempo del vehículo, de esta forma los padres de familia saben a qué distancia se encuentra el expreso de su lugar de recogida junto a otros datos como son: la placa de la buseta, foto y nombre del conductor y ayudante.
> >
> > Al recoger al estudiante se debe colocar un check de ingreso en una lista, de esta forma se establece que el estudiante subió al expreso desde su hogar y lo mismo sucede cuando lo retorna, se debe marcar otro check indicando que el estudiante efectivamente subió al expreso para retornar a su hogar.
> >
> > El sistema debe permitir suspender el servicio a un estudiante en caso de que no haya pagado el valor mensual, de ser así, la ruta no mostraría al chofer la parada de dicho estudiante.
> >
> > De los colegios se interesa conocer el nombre y un logo para customizar el entorno de la aplicación. De los padres de familia interesa conocer la cédula, nombres, apellidos. De los estudiantes se interesa conocer matricula, nombres apellidos, curso y estado (activo o inactivo). De los choferes interesa conocer cédula, nombres, apellidos, archivo de licencia y fecha de expiración. De los ayudantes interesa conocer la cédula, nombres y apellidos.
> >
> > Se puede dar la situación en que los usuarios tengan más de un rol, ejemplo un chofer hace la ruta para un colegio, pero podría tener a un representado en otro colegio.
> >
> > Cada ubicación de recogida/llegada consta de latitud, longitud, dirección, referencias y orden. El sistema ordena cada ubicación con un algoritmo interno para calcular la ruta más efectiva.
> >
> > La asistencia debe almacenar el día de recogida/retorno, la fecha y hora en que el estudiante sube al expreso y alguna novedad.
> >
> > (El examen incluye dos figuras.)
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej08-expreso.svg]]
>
> > [!success]- Clave de modelado
> > - Roles múltiples: PERSONA supertipo con roles PADRE / CHOFER / AYUDANTE / ESTUDIANTE (**sobrelapado**: un chofer puede ser padre).
> > - ASIGNACIÓN semanal: intermedia CHOFER–BUSETA–AYUDANTE–RUTA con vigencia (desde / hasta); el cambio a media semana = cerrar fila y abrir otra.
> > - ASISTENCIA/check: intermedia ESTUDIANTE–RUTA–fecha (subida sí/no, bajada sí/no, hora, novedad).
> > - Suspensión por pago: **estado** del ESTUDIANTE (activo / suspendido); la parada se filtra por consulta.
> > - Posición periódica: débil de BUSETA (timestamp + coordenadas); no mezclar con PARADA (puntos fijos).

### ✏️ Ejercicio 9 — Crédito hipotecario (3E, 2023-2)

> [!example] 🧪 Planteamiento (fuente: `2023-2PAO-3E-SBD.docx`, Sección 1)
> - PRESTATARIO (cédula, nombre, dirección, teléfono, ingresos, historial) y PRESTAMISTA del banco.
> - CONTRATO (tasa, plazo, monto, pagos mensuales, fechas); PROPIEDAD en garantía (dirección, tasación por TASADOR: ubicación, tamaño, estado).
> - HISTORIAL: deudas (descripción, fecha contraída / límite / pagada) + tipos de crédito (tarjeta, estatal…, deuda actual, límite).
> - Pagos mensuales alimentan el historial; incumplimiento → relación legal (ejecución hipotecaria).
> - 📌 Se pide: conceptual con entidades, atributos, relaciones y tipos.
>
> > [!quote]- 📄 Enunciado original
> >
> > Elabore el modelo conceptual incluyendo entidades, atributos, relaciones y sus tipos para el siguiente planteamiento:
> >
> > Se lo ha contratado para implementar un sistema que procese Créditos Hipotecarios del Banco del PACIPICO. Para ello deberá diseñar un modelo de base de datos que permita guardar los datos necesarios para solicitar y/o aprobar el otorgamiento del crédito.
> >
> > Para llevar a cabo un préstamo hipotecario, se debe considerar la participación del prestatario (que es la persona que solicita el préstamo hipotecario) y del prestamista que es el representante del Banco del PATIPICO que recepta la documentación del prestatario.
> >
> > El prestatario para solicitar un crédito Hipotecario debe indicar los siguientes datos cédula, nombre, dirección, teléfono, ingresos mensuales e historial crediticio. El prestamista revisa la información y decide formalizar o no el contrato hipotecario. En el contrato se establecen los términos y condiciones como la tasa de interés, el plazo y monto del préstamo, montos de los pagos mensuales y su fecha de plazo. Además, el prestatario proporciona información sobre la propiedad que se utilizará como garantía para el préstamo, lo que incluye información como dirección de la propiedad y el valor de tasación. Este valor se determina mediante una evaluación realizada por un tasador profesional del banco, que examina diversos aspectos de la propiedad como la ubicación, tamaño, características y estado de la propiedad (buen estado, requiere reparaciones, etc.). Un valor de tasación adecuado asegura al prestamista que la propiedad ofrecida como garantía tiene un valor suficiente para respaldar el monto del préstamo.
> >
> > El historial crediticio del prestatario es otro aspecto fundamental que influye en la aprobación del préstamo y las condiciones asociadas al mismo. Este historial incluye información sobre el comportamiento financiero pasado del prestatario, como el manejo de deudas, que incluyen una descripción, fecha que se lo contrajo, fecha límite de pago y fecha que se lo pagó. También un historial de crédito que incluyan que tipo de crédito accedió (ej. Tarjeta de crédito, créditos estatales, etc.) cantidad actual de la deuda y límite máximo de crédito disponible. Un historial crediticio sólido aumenta la confianza del prestamista en la capacidad del prestatario para cumplir con las obligaciones del préstamo.
> >
> > Durante la vigencia del préstamo hipotecario, se establece una relación continua entre el prestamista y el prestatario según se realizan los pagos mensuales. Estos pagos se registran como parte del historial crediticio del prestatario, lo que puede afectar las relaciones futuras con otras entidades financieras. Además, en caso de incumplimiento de pago, se activa una relación legal que puede llevar a medidas como la ejecución hipotecaria de la propiedad.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej09-hipotecario.svg]]
>
> > [!success]- Clave de modelado
> > - PRESTATARIO y PRESTAMISTA: roles de PERSONA (el prestamista es empleado del banco).
> > - PROPIEDAD–TASACIÓN 1:M con tasador y fecha (la tasación cambia: **historízala, no la sobrescribas**).
> > - DEUDA: débil de PRESTATARIO. CONTRATO: intermedia PRESTATARIO–PRESTAMISTA–PROPIEDAD (tasa, plazo, monto).
> > - Incumplimiento/ejecución: **estado** del CONTRATO (vigente / en mora / en ejecución), no entidad nueva.

### ✏️ Ejercicio 10 — Comunidad EcoLife (3E, 2024-2)

> [!example] 🧪 Planteamiento (fuente: `2024-2PAO-3E-SBD.docx`, Sección 1)
> - MIEMBRO (ID, nombre, apellido, email único, registro, ubicación, puntos; **redes + cuentas**: multivaluados) en **hasta 4 MARCAS** (ID, nombre, descripción, email).
> - PUBLICACIONES (ID, título, contenido, fecha, red, cuenta, tipo: artículo / pregunta / respuesta / comentario) en un TEMA (ID, nombre único, descripción).
> - EVENTOS (ID, nombre, fecha/hora, ubicación, capacidad); RECOMPENSAS (ID, tipo, descripción, puntos requeridos).
> - Reglas: miembro crea N publicaciones (cada una de un miembro y un tema); miembro asiste a N eventos; miembros reclaman recompensas; marcas crean publicaciones y organizan eventos.
> - 📌 Se pide: conceptual en Chen + lógico pata de gallo normalizado.
>
> > [!quote]- 📄 Enunciado original
> >
> > Elabore el modelo conceptual incluyendo entidades, atributos, relaciones y sus tipos en notación de CHEN para el siguiente planteamiento:
> >
> > La empresa "EcoLife", una marca de productos sostenibles para el hogar, busca fortalecer la lealtad de sus clientes y obtener información valiosa para el desarrollo de nuevos productos a través de la creación y gestión de una comunidad de marca en línea.
> >
> > En la estructura de comunidad gestionada por EcoLife, cada individuo que se une se convierte en un miembro, identificado de manera única por su ID_Miembro. Guardamos su nombre, apellido, correo electrónico (que debe ser único), la fecha de registro y su ubicación. Además, cada miembro acumula puntos según su participación y/o publicación en las redes, por lo que es importante guardar las redes sociales que el miembro está registrado y los nombres de las cuentas. Es importante destacar que EcoLife gestiona un grupo de marcas, y un mismo miembro puede formar parte de hasta cuatro de estas marcas dentro del ecosistema EcoLife.
> >
> > Dentro de cada comunidad de marca, se generan Publicaciones, identificadas por un ID_Publicación, incluyendo título, contenido, fecha de publicación, red social en el cual se publicó y nombre de la cuenta, y el tipo de publicación (artículo, pregunta, respuesta o comentario). Cada publicación se clasifica dentro de un Tema específico, con su propio ID_Tema, nombre único y descripción.
> >
> > EcoLife organiza Eventos para los miembros de sus marcas, cada uno con un ID_Evento, nombre, fecha y hora, ubicación, descripción y Capacidad máxima de asistentes. Para incentivar la participación, EcoLife ofrece Recompensas, identificadas por un ID_Recompensa, tipo (descuento, producto gratis, etc.), descripción y Puntos Requeridos.
> >
> > Toda esta estructura es gestionada por EcoLife y sus marcas afiliadas, identificadas por un ID_Marca, nombre, descripción y correo electrónico. Un Miembro puede crear múltiples Publicaciones dentro de la comunidad de la marca a la que pertenece, y cada publicación está asociada a un solo miembro. Cada Publicación pertenece a un Tema, categorizando el contenido. Un Miembro puede asistir a múltiples Eventos organizados por EcoLife o la marca de la que forma parte, y cada evento puede tener múltiples miembros asistentes. Los Miembros pueden reclamar Recompensas con sus puntos. La Marca EcoLife y sus submarcas crean Publicaciones y organizan Eventos, siendo responsables de la actividad comunitaria. Esta estructura promueve la participación y la lealtad, considerando la posibilidad de que un miembro participe en varias comunidades de marca dentro de EcoLife.
> >
> > (El examen incluye una figura. La Sección 2 pide además el modelo lógico con notación pata de gallo completamente normalizado.)
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej10-ecolife.svg]]
>
> > [!success]- Clave de modelado
> > - MIEMBRO–MARCA M:N con **tope 4** (restricción de app, anótala). Redes + cuentas: multivaluado doble (red, cuenta) → tabla propia.
> > - PUBLICACIÓN–TEMA N:1; PUBLICACIÓN–MIEMBRO N:1 (autor); PUBLICACIÓN–MARCA N:1 (emisora).
> > - Tipo de publicación: valor; si un comentario responde a otra publicación: **recursiva** 1:M.
> > - ASISTENCIA (miembro–evento) y CANJE (miembro–recompensa con fecha y puntos usados): intermedias con atributos.
> > - Capacidad del evento: restricción, no entidad.

## 🅱️ Bloque B — Dependencias y normalización (resueltos)

### ✏️ Ejercicio 11 — Caso `cod_estud` (Taller 1, 2026)

> [!example] 🧪 Planteamiento (fuente: `2026_1PAO_Taller_1_TICG1018.pdf`, punto 2)
> - Figura del examen (diagrama de dependencias; la tabla universal sin normalizar):
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej11-diagrama-dependencias.svg]]
> - 📌 Se pide:
>   - 1) Clave primaria.
>   - 2) Dependencias parciales.
>   - 3) Dependencias transitivas.
>   - 4) Normalizar hasta 3FN + diagrama lógico.
>
> > [!quote]- 📄 Enunciado original
> >
> > 2. Se tiene el siguiente diagrama de dependencias:
> >
> > cod_estud, cod_curso, nombre_estud, correo_estud, nomb_curso, horas_curso, cod_instructor, nomb_instructor, nota_final
> >
> > 1. Identifique la clave primaria.
> > 2. Identifique las dependencias parciales.
> > 3. Identifique las dependencias transitivas.
> > 4. Normalice la relación hasta Tercera Forma Normal (3FN) y obtenga el diagrama lógico.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej11-dep-flow.svg]]
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej11-modelo-3fn.svg]]
>
> > [!success]- Solución guiada
> > - 1) La nota depende del **par** (estudiante, curso): PK = `(cod_estud, cod_curso)`.
> >   - `cod_estud` → nombre, correo.
> >   - `cod_curso` → nomb_curso, horas, cod_instructor.
> >   - instructor → nomb_instructor.
> > - 2) Parciales (parte de la PK):
> >   - `cod_estud` → nombre_estud, correo_estud.
> >   - `cod_curso` → nomb_curso, horas_curso, cod_instructor.
> > - 3) Transitiva: `cod_curso` → `cod_instructor` → `nomb_instructor`.
> > - 4) Esquema 3FN:
> >   - ESTUDIANTE(cod_estud PK, nombre, correo).
> >   - INSTRUCTOR(cod_instructor PK, nombre).
> >   - CURSO(cod_curso PK, nombre, horas, cod_instructor FK).
> >   - MATRÍCULA(cod_estud PK/FK, cod_curso PK/FK, nota_final).
> > - Verifica: toda FK referencia una PK; la intermedia lleva la PK compuesta; sin transitivas restantes.

### ✏️ Ejercicio 12 — Ventas digitales (1E, 2025, con solución oficial)

> [!example] 🧪 Planteamiento (fuente: `2025-1PAO-1E-SBD.docx`, Sección 3)
> - Tabla de Excel a normalizar (PK: Vendedor ID + Producto ID + Fecha Venta):
>
> | Vendedor ID | Producto ID | Fecha Venta | Cantidad | Vendedor Nombre | Producto Nombre | Precio Unitario | Servidor ID | Servidor Región |
> |---|---|---|---|---|---|---|---|---|
> | 501 | A101 | 01/03/24 | 3 | Torres | Antivirus Pro | 25.00 | 78 | América Norte |
> | 501 | A102 | 02/03/24 | 1 | Torres | Firewall Plus | 40.00 | 78 | América Norte |
> | 502 | A101 | 02/03/24 | 2 | López | Antivirus Pro | 25.00 | 79 | Europa Oeste |
> | 503 | A103 | 02/03/24 | 1 | García | Cloud Vault | 60.00 | 80 | Asia Central |
> | 501 | A101 | 05/03/24 | 4 | Torres | Antivirus Pro | 25.00 | 78 | América Norte |
> - DF dadas:
>   - (las 3) → Cantidad, Vendedor Nombre, Nombre Producto, Servidor ID, Servidor Región.
>   - Vendedor ID → Vendedor Nombre, Servidor ID, Servidor Región.
> - 📌 Se pide: DF adicionales y esquema en cada FN.
>
> > [!quote]- 📄 Enunciado original
> >
> > Una empresa registra sus ventas digitales en la siguiente tabla de Excel. Realice el proceso de normalización del esquema relacional de la tabla hasta la 3era Forma Normal. Suponga que la clave primaria es (Vendedor ID, Producto ID, Fecha Venta).
> >
> > Suponga también las siguientes dependencias funcionales:
> >
> > (Vendedor ID, Producto ID, Fecha Venta) → Cantidad, Vendedor Nombre, Nombre Producto, Servidor ID, Servidor Región
> >
> > Vendedor ID → Vendedor Nombre, Servidor ID, Servidor Región
> >
> > Identifique las dependencias funcionales adicionales y sus tipos para justificar el esquema relacional obtenido en cada etapa del proceso.
> >
> > (La tabla de datos va arriba. El documento del examen trae además la solución oficial con rúbrica, que es la usada en la clave.)
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej12-modelo-3fn.svg]]
>
> > [!success]- Solución (la del examen)
> > - DF adicionales:
> >   - (las 3) → Precio Unitario.
> >   - Producto ID → Producto Nombre, Precio Unitario.
> > - Diagrama de dependencias (léelo antes de partir):
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej12-dependencias.svg]]
> > - 1FN: cumplida (sin listas ni multivaluados).
> > - 2FN (fuera parciales):
> >   - PRODUCTO(Producto ID PK, Nombre, Precio).
> >   - VENDEDOR(Vendedor ID PK, Nombre, Servidor ID, Región).
> >   - VENTA(Vendedor ID PK/FK, Producto ID PK/FK, Fecha, Cantidad).
> > - 3FN (fuera la transitiva Vendedor → Servidor → Región):
> >   - SERVIDOR(Servidor ID PK, Región).
> >   - VENDEDOR(Vendedor ID PK, Nombre, Servidor ID FK).
> > - Moraleja de corrector: declara cada DF con su tipo (total / parcial / transitiva) antes de partir; eso solo ya da puntos.

### ✏️ Ejercicio 13 — Recetas de farmacia (1E, 2024)

> [!example] 🧪 Planteamiento (fuente: `2024-1PAO-1E-SBD.docx`, Sección 4)
> - Tabla a normalizar (fíjate en las columnas con listas):
>
> | ID_Receta | Nombre_Producto | Ingredientes | Cantidad_Ingredientes | Precio_Unitario | Etapa_Produccion |
> |---|---|---|---|---|---|
> | 1 | Comprimidos de Paracetamol | Paracetamol (polvo), Almidón de maíz, Estearato de magnesio | 500 mg, 1 g, 10 mg | 0.10 | Mezclado, Granulación, Compresión, Recubrimiento |
> | 2 | Jarabe de Jengibre | Extracto de Jengibre, Agua purificada, Sacarosa, Ácido cítrico | 200 mg, 50 ml, 10 g, 0.5 g | 0.80 | Mezclado, Filtrado, Envasado |
> | 3 | Ungüento de Caléndula | Extracto de Caléndula, Vaselina, Lanolina | 5 g, 20 g, 10 g | 1.50 | Mezclado, Envasado |
> | 4 | Cápsulas de Vitamina C | Ácido ascórbico (polvo), Celulosa microcristalina, Estearato de magnesio | 500 mg, 200 mg, 10 mg | 0.20 | Mezclado, Llenado de cápsulas |
> | 5 | Suspensión antibiótica | Amoxicilina (polvo), Sacarosa, Saborizante a fresa, Agua purificada | 250 mg, 5 g, 1 ml, 50 ml | 1.20 | Mezclado, Homogenización, Envasado |
> - 📌 Se pide: normalizar a 3FN justificando cada FN + diagrama lógico.
>
> > [!quote]- 📄 Enunciado original
> >
> > Normalizar el siguiente esquema relacional hasta la 3era Forma Normal. Justificar porque cumple/no cumple con la Forma Normal y obtener el diagrama lógico normalizado.
> >
> > (La tabla de recetas va arriba.)
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej13-modelo.svg]]
>
> > [!success]- Solución guiada
> > - 1FN: Ingredientes, Cantidades y Etapas son **listas paralelas** (multivaluados) → filas atómicas:
> >   - PRODUCTO(ID_Receta PK, Nombre, Precio).
> >   - DETALLE(ID_Receta PK/FK, Ingrediente PK, Cantidad, Etapa).
> > - 2FN: ¿algo depende de **parte** de la PK?
> >   - Nombre y Precio dependen de ID_Receta (parte) → ya separados en PRODUCTO.
> >   - En el detalle: Cantidad depende de (Receta + Ingrediente); Etapa, de (Receta + Etapa) → si la PK del detalle es triple, hay parciales: parte en DETALLE_INGREDIENTE y DETALLE_ETAPA.
> > - 3FN: sin no-primos que dependan de no-primos (verifica: el precio depende de la PK — sano).
> > - Justificación que pide el examen: nombra la anomalía que elimina cada paso (inserción: no puedes crear un ingrediente sin receta; borrado: borrar la receta borra el catálogo).

### ✏️ Ejercicio 14 — Artefactos MABE/Xiaomi (1E, 2022)

> [!example] 🧪 Planteamiento (fuente: `2022-2PAO-1E-SBD.docx`, Sección 4)
> - Tabla de artefactos (el examen la trae traspuesta; aquí ya girada con las listas a la vista):
>
> | numero | linea | modelo | litros | precio_venta | codigo_linea | marca | tipo | distribuidor | importador |
> |---|---|---|---|---|---|---|---|---|---|
> | 023 | blanca | RMA255FYEU | 250 | 509.86 | 001 | MABE | refrigerador | Mabetec, Mayepsa, ElectroGam, Mabe s.a. | Imaco, Importadora Frailes, Multiclimec, Imp. Lorences |
> | 022 | marron | P1L55M6 | NULL | 598.98 | 002 | Xiaomi | televisor | Xiaomi Store, GadgetMi, Telnet, MundoCellOnline | Noboa Distribuidora, Importadora JMV |
> | 019 | blanca | LMDE3124PBAB0 | 13 | 289.99 | 001 | MABE | lavadora | Mabetec, Mayepsa, ElectroGam, Mabe s.a. | Imaco, Importadora Frailes, Multiclimec, Imp. Lorences |
> - 📌 Se pide: normalizar a 3FN explicando anomalías por FN.
>
> > [!quote]- 📄 Enunciado original
> >
> > Aplicar las normalizaciones (hasta la 3era Forma Normal) para evitar posibles anomalías y redundancia en los datos. Explique cada una de las anomalías encontradas en las diferentes formas normales.
> >
> > (Tabla DATOS DE ARTEFACTOS arriba, girada a orientación normal.)
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej14-modelo.svg]]
>
> > [!success]- Solución guiada
> > - 1FN: distribuidor e importador son listas → tablas propias:
> >   - ARTEFACTO_DISTRIBUIDOR(numero PK/FK, distribuidor PK).
> >   - ARTEFACTO_IMPORTADOR(numero PK/FK, importador PK).
> > - 2FN: PK simple (numero) ⇒ **2FN automática**; verifica que no haya PK compuesta escondida.
> > - 3FN: transitiva numero → codigo_linea → (línea, marca):
> >   - LINEA(codigo_linea PK, línea, marca).
> >   - ARTEFACTO(numero PK, modelo, litros, precio, tipo, codigo_linea FK).
> > - Ojo: litros vacío en una fila = NULL permitido (no rompe 1FN); tipo depende del modelo — solo haz tabla TIPO si el examen lo exige.

### ✏️ Ejercicio 15 — Dependencias abstractas K-A-B-C-D-E-F (1E, 2023)

> [!example] 🧪 Planteamiento (fuente: `2023-1PAO-1E-SBD.docx`, Sección 4)
> - DF conocidas:
>   - K → A, B.
>   - C → D, E, F.
>   - D → F.
> - La columna C trae listas (C1, C2…) en la tabla.
> - 📌 Se pide: normalizar a 3FN explicando anomalías. Es el drill más rápido del bloque: úsalo para calentar.
>
> > [!quote]- 📄 Enunciado original
> >
> > Aplicar las normalizaciones (hasta la 3era Forma Normal) para evitar posibles anomalías y redundancia en los datos. Explique cada una de las anomalías encontradas en las diferentes formas normales.
> >
> > Considerar que:
> >
> > - K determina a A, B
> > - C determina a D, E, F
> > - D determina a F
> >
> > (La tabla de datos con las listas de C va en el PDF.)
> **📊 Complementos de la solución** — función + diagrama; dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej15-dep-flow.svg]]
>
> > [!success]- Solución guiada
> > - Diagrama de dependencias:
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej15-dependencias.svg]]
> > - 1FN: C trae listas → separa con PK (K, C).
> > - 2FN (fuera parciales sobre (K, C)):
> >   - K_TABLA(K PK, A, B).
> >   - C_TABLA(C PK, D, E, F).
> >   - PUENTE(K PK/FK, C PK/FK).
> > - 3FN (transitiva C → D → F):
> >   - D_TABLA(D PK, F).
> >   - C_TABLA(C PK, D FK, E).
> > - Verifica las claves corriendo la función de arriba en tu cuaderno de Python (los dos `print` confirman la PK y las tablas).

### ✏️ Ejercicio 16 — STORE_ITEM y MORE_STUFF (Lección 2, 2024)

> [!example] 🧪 Planteamiento (fuente: `Leccion 2 - PAO I 2024.pdf` — texto completo, sin figura)
> - `STORE_ITEM(SKU, PromotionID, Vendor, Style, Price)` con DF:
>   - (SKU, PromotionID) → todos.
>   - SKU → Vendor, Style.
> - `MORE_STUFF(D, O, N, T, C, R, Y)` con DF:
>   - (D, O) → todos.
>   - (C, R) → Y.
>   - D → N.
> - 📌 Se pide: ¿en qué FN está cada una? Normaliza.
>
> > [!quote]- 📄 Enunciado original
> >
> > Transformar a modelo lógico el siguiente modelo conceptual. (CLIENTE—HORARIO: figura en el PDF.)
> >
> > En que forma normal se encuentra la siguiente relacion. Normalise si es necesario.
> >
> > Tabla: STORE_ITEM (SKU, PromotionID, Vendor, Style, Price). Dependencias: (SKU, PromotionID) → Vendor, Style, Price; SKU → Vendor, Style.
> >
> > Tabla: MORE_STUFF (D, O, N, T, C, R, Y). Dependencias: (D, O) → N, T, C, R, Y; (C, R) → Y; D → N.
> **📊 Diagrama de la solución** — dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej16-dep-flow.svg]]
>
> > [!success]- Solución guiada
> > - Diagrama de dependencias STORE_ITEM:
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej16-store-item.svg]]
> > - STORE_ITEM: parcial SKU → Vendor, Style ⇒ está en **1FN**.
> >   - 2FN: ITEM(SKU PK, Vendor, Style); PROMO(SKU PK/FK, PromotionID PK/FK, Price) — el precio depende del par (precio *en esa promoción*), así que queda en la intermedia.
> > - Diagrama de dependencias MORE_STUFF:
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas draw.io/ej16-more-stuff.svg]]
> > - MORE_STUFF: parcial D → N ⇒ **1FN**.
> >   - 2FN: D_TABLA(D PK, N) + resto (D, O, T, C, R, Y).
> >   - Transitiva (C, R) → Y con (C, R) no-primo ⇒ **3FN**: CR_TABLA(C PK, R PK, Y) + resto (D, O, T, C, R con FK).
> > - Patrón de examen: determinante doble → sospecha parcial; DF entre no-primos → transitiva.

## 🅲️ Bloque C — Banco de conceptos (V/F y completar)

> [!question] ❓ Ronda 1 — de exámenes reales (responde, luego abre)
> - De modelado:
>   - Una relación de una entidad consigo misma se llama… (1E 2024).
>   - Un atributo calculable desde otros atributos es válido (1E 2022).
>   - Una entidad fuerte no depende de otra para existir (1E 2022).
> - De integridad y claves:
>   - Ningún componente de una FK puede tener valores ausentes en la PK referenciada (1E 2022/2024).
>   - Las PK pueden aceptar nulos (1E 2024).
> - De normalización:
>   - "Todos los no-clave dependen de la clave completa y no de una parte" es regla de… (1E 2024).
>   - La 1FN no permite multivaluados, compuestos ni combinaciones (1E 2023).
>   - Las FN buscan minimizar redundancia y anomalías de inserción/actualización/borrado (1E 2023).
>
> > [!success]- Respuestas
> > - De modelado: **recursiva** (o réflexiva); **verdadero** (derivado, óvalo punteado); **verdadero**.
> > - De integridad: **verdadero** (integridad referencial); **falso** (entidad: PK nunca NULL).
> > - De normalización: **2FN**; **verdadero**; **verdadero**.

## ✅ Checklist pre-taller (rúbrica 1E 2025)

> [!tip] 📌 Con qué te califican (25 pts el lógico)
> Entidades completas (6) + atributos con tipos (6) + PK/FK y binarias (6) + especiales ternarias/recursivas/multivaluadas (7). Antes de entregar verifica: ¿conté tablas al final? ¿toda FK apunta a una PK? ¿las M:N tienen intermedia? ¿la 1:1 total-total se fusionó? (protocolo en [[01 - Conversión MC a ML por cardinalidad]]).

## 🔁 Repaso SR (flashcards)

#flashcards/bd-guia1
- ¿Recursiva vs ternaria?::1 entidad en 2 roles (FK a sí misma) vs 3 entidades que se necesitan a la vez (intermedia triple).
- ¿Histórico propietario (subsidio) cómo?::M:N con vigencia desde/hasta; la venta referencia al propietario de ese momento.
- ¿Multivaluado al lógico?::Tabla propia con (PK original como FK + valor) en PK compuesta.
- ¿Supervisor que vende (subsidio)?::Recursiva 1:M; la venta cuelga de EMPLEADO sin distinguir.
- ¿PK de (cod_estud, cod_curso) por qué?::La nota depende del par; ni del uno ni del otro solos.
- ¿2FN automática cuándo?::PK de un solo atributo (no hay parte de la cual depender).
- ¿Transitiva típica?::No-primo → no-primo (instructor → nombre; servidor → región; línea → marca).
- ¿Reenvío AZM es artículo nuevo?::No: mismo artículo, versión/ronda como atributo.
- ¿Lugar jerárquico (Pho-grah) cómo?::Recursiva 1:M (FK padre), profundidad libre.
- ¿Asignación semanal con cambios (expreso)?::Intermedia con vigencia; cambio = cerrar fila + abrir otra.
- ¿Precio en PROMO (Ej. 16) por qué en la intermedia?::Depende del par (SKU, PromotionID): es total, no parcial.
- ¿Clausura para qué?::Verificar que la PK candidata determine todo el universo antes de partir.

## 🧭 Seguir con

> [!info] 🧭 Seguir con
>
> - Método: [[02 - Entidades, atributos, claves y relaciones]] · [[03 - Modelo relacional, ERM y casos Tiny College]] · [[01 - Conversión MC a ML por cardinalidad]] · [[02 - Primera forma normal y diccionario de datos]] · [[03 - Segunda y tercera forma normal]]
> - Índices: [[00 - Leeme Unidad 0|Unidad 0]] · [[00 - Índice Unidad 1]] · [[00 - Índice Unidad 2]]

## 📚 Referencias

> [!quote] 📚 Referencias
>
> - `2026_1PAO_Taller_1_TICG1018.pdf` — Taller 1 (lavandería + `cod_estud`).
> - `2024_1PAO_Taller_1_TICG1018.pdf` — Taller 1 2024 (revista AZM; escaneado, enunciado extraído por OCR).
> - `Leccion 1 - PAO I 2024.pdf` — TaxiGo! (escaneado, enunciado por OCR).
> - `Leccion 2 - PAO I 2024.pdf` — conversión + STORE_ITEM/MORE_STUFF (escaneado, enunciado por OCR).
> - `2024-1PAO-1E-SBD.docx` — 1E 2024 (subsidio, receta, conceptos, rúbrica por secciones).
> - `2025-1PAO-1E-SBD.docx` — 1E 2025 (concursos, ventas con solución oficial, rúbrica del lógico, NesflisDB).
> - `2022-2PAO-1E-SBD.docx` — 1E 2022 (AZM, artefactos, conceptos V/F).
> - `2023-1PAO-1E-SBD.docx` — 1E 2023 (NAREN, K-A-B-C-D-E-F).
> - `2023-2PAO-1E-SBD.docx` — 1E 2023-2 (Pho-grah + conteo de tablas).
> - `2024-2PAO-1E-SBD.docx` — 1E 2024-2 (expreso escolar).
> - `2023-2PAO-3E-SBD.docx` / `2024-2PAO-3E-SBD.docx` — 3E (hipotecario, EcoLife).
> - `Taller 2 PAO-2026-1  SOL.pdf` — hotel 1FN–3FN con solución (desarrollado en [[03 - Segunda y tercera forma normal]]).

---

**Tags:** #TICG1018 #unidad0 #guia #taller1 #bd

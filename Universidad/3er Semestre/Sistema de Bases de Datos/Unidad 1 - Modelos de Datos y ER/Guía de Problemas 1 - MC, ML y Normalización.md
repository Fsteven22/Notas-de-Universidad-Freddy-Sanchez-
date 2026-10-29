---
dg-publish: true
tags: [TICG1018, unidad0, guia, taller1, bd]
---

# ðŸ“ GuÃ­a de Problemas 1 â€” MC, ML y NormalizaciÃ³n (Taller 1)

> [!info] â„¹ï¸ QuÃ© es esta guÃ­a
> RecopilaciÃ³n de los ejercicios reales de talleres, lecciones y exÃ¡menes (2022â€“2026) que cubren lo del **Taller 1**: modelo conceptual en Chen, conversiÃ³n a modelo lÃ³gico pata de gallo, supertipos, dependencias y normalizaciÃ³n hasta 3FN. Los enunciados salen de los PDFs de la Unidad 0; las soluciones y claves son propias.
> - Bloque A: casos de modelado (enunciado + clave + esqueleto del diagrama).
> - Bloque B: dependencias y normalizaciÃ³n (resueltos paso a paso, con diagrama).
> - Bloque C: banco de conceptos V/F.
> - MÃ©todo completo en: [[02 - Entidades, atributos, claves y relaciones]], [[01 - ConversiÃ³n MC a ML por cardinalidad]], [[02 - Primera forma normal y diccionario de datos]], [[03 - Segunda y tercera forma normal]].

## ðŸ…°ï¸ Bloque A â€” Modelo conceptual (casos reales)

> [!tip] ðŸ“Œ CÃ³mo trabajar cada caso
> Lee el enunciado, dibuja el Chen en papel o ERDPlus (rectÃ¡ngulo = entidad, rombo = relaciÃ³n, Ã³valo = atributo, subrayado = PK), abre la clave, compara. La clave trae lo que el corrector verifica (entidades, identificadores, cardinalidades, la trampa) mÃ¡s el esqueleto del diagrama esperado.

### âœï¸ Ejercicio 1 â€” LavanderÃ­a (Taller 1, 2026)

> [!example] ðŸ§ª Planteamiento (fuente: `2026_1PAO_Taller_1_TICG1018.pdf`)
> - Empresa de limpieza en seco; se registran CLIENTES (identificaciÃ³n, nombres, apellidos, telÃ©fono, correo, direcciÃ³n) con **historial de solicitudes y preferencias**.
> - PRENDAS (descripciÃ³n, color, material, marca, observaciones, tratamientos especiales por manchas o tejidos delicados).
> - EMPLEADOS (identificaciÃ³n, nombres, apellidos, cargo, fecha de contrataciÃ³n, telÃ©fono, correo) que participan en etapas: recepciÃ³n, clasificaciÃ³n, limpieza, planchado, entrega.
> - SOLICITUDES (fecha de recepciÃ³n, fecha estimada de entrega, estado: recibido / en proceso / listo / entregado) con **varias prendas y varios servicios**.
> - SERVICIOS (cÃ³digo, tipo, observaciÃ³n, tiempo estimado, costo).
> - PAGOS (comprobante, fecha, valor, mÃ©todo, estado).
> - ðŸ“Œ Se pide: conceptual en Chen + lÃ³gico en pata de gallo con toda la simbologÃ­a.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > 1. Crear el diseÃ±o conceptual en notaciÃ³n de CHEN y el diseÃ±o lÃ³gico en notaciÃ³n pata de gallo considerando toda la simbologÃ­a vista en clase:
> >
> > Una empresa dedicada a la limpieza de ropa en seco desea implementar un sistema de informaciÃ³n para administrar sus operaciones diarias. El sistema debe registrar la informaciÃ³n de los clientes, incluyendo datos como nÃºmero de identificaciÃ³n, nombres, apellidos, telÃ©fono, correo electrÃ³nico y direcciÃ³n. Los clientes pueden realizar mÃºltiples solicitudes de servicio a lo largo del tiempo, por lo que es importante mantener un historial detallado de sus pedidos y preferencias.
> >
> > La empresa recibe diferentes tipos de prendas para su procesamiento, tales como trajes, vestidos, camisas, pantalones y abrigos. De cada prenda se requiere almacenar informaciÃ³n como descripciÃ³n, color, material, marca y observaciones especiales proporcionadas por el cliente. AdemÃ¡s, algunas prendas pueden requerir tratamientos especÃ­ficos debido a la presencia de manchas delicadas, tejidos especiales o instrucciones particulares de cuidado.
> >
> > El proceso de limpieza es realizado por empleados especializados que participan en distintas etapas del servicio, como recepciÃ³n, clasificaciÃ³n, limpieza, planchado y entrega. De cada empleado se registra informaciÃ³n como nÃºmero de identificaciÃ³n, nombres, apellidos, cargo, fecha de contrataciÃ³n, telÃ©fono y correo electrÃ³nico. La empresa necesita conocer quÃ© empleados participaron en cada solicitud para fines de control de calidad y seguimiento de las operaciones.
> >
> > Cada solicitud puede incluir varias prendas y diferentes servicios, tales como limpieza en seco, eliminaciÃ³n de manchas, planchado especial, desinfecciÃ³n o tratamiento de telas delicadas. Para cada servicio se almacena un cÃ³digo Ãºnico, tipo de servicio, observaciÃ³n, tiempo estimado de ejecuciÃ³n y costo. Asimismo, el sistema debe registrar de cada solicitud la fecha de recepciÃ³n de las prendas, la fecha estimada de entrega y el estado actual del trabajo, que puede ser recibido, en proceso, listo para entrega o entregado.
> >
> > Finalmente, la empresa necesita gestionar los pagos realizados por los clientes. Para cada transacciÃ³n se registra un nÃºmero de comprobante, fecha, valor cancelado, mÃ©todo de pago y estado de la transacciÃ³n. La gerencia tambiÃ©n desea generar reportes sobre los servicios mÃ¡s solicitados, los ingresos obtenidos en determinados perÃ­odos y la productividad de los empleados, con el fin de mejorar la calidad del servicio y optimizar la toma de decisiones.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej01-lavanderia.svg]]
>
> > [!success]- Clave de modelado
> > - Entidades: CLIENTE, SOLICITUD, PRENDA, SERVICIO, EMPLEADO, PAGO.
> > - TelÃ©fono del cliente: **multivaluado**. Observaciones de la prenda *en esa solicitud*: atributo de la intermedia, no de PRENDA.
> > - M:N con intermedia y atributos propios:
> >   - SOLICITUDâ€“PRENDA â†’ DETALLE (observaciones de esa prenda en esa solicitud).
> >   - SOLICITUDâ€“SERVICIO â†’ DETALLE (costo y tiempo de ese servicio en esa solicitud).
> >   - SOLICITUDâ€“EMPLEADO â†’ PARTICIPACIÃ“N (etapa en la que participÃ³).
> > - 1:M: CLIENTEâ€“SOLICITUD (FK cliente en solicitud); SOLICITUDâ€“PAGO (FK solicitud en pago).
> > - Trampa: el historial **no** es entidad (sale de CLIENTE 1:M SOLICITUD con fechas); estado = valor con dominio, no entidad.

### âœï¸ Ejercicio 2 â€” TaxiGo! (LecciÃ³n 1, 2024)

> [!example] ðŸ§ª Planteamiento (fuente: `Leccion 1 - PAO I 2024.pdf`)
> - USUARIO se registra (nombres, apellidos, fecha de nacimiento, mÃ³vil) con usuario y contraseÃ±a.
> - Registra el lugar de recojo: calle principal, nÃºmero, calle secundaria, ciudad.
> - CONDUCTOR (nombres, apellidos, cuenta bancaria, cÃ©dula, gÃ©nero, licencia, direcciÃ³n, telÃ©fono, cÃ³digo Ãºnico en la compaÃ±Ã­a).
> - CARRO (placa, gasolina, modelo, color, alquilado sÃ­/no; si es alquilado, datos del PROPIETARIO: nombres, apellidos, direcciÃ³n, telÃ©fono).
> - CARRERA (origen y destino en texto + latitud/longitud, precio estimado).
> - Al aceptar: se guardan los **primeros 4 dÃ­gitos** de la tarjeta + fecha de pago.
> - Se registran cancelaciones y viajes exitosos (estadÃ­sticas de uso).
> - ðŸ“Œ Se pide: modelo conceptual.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > LecciÃ³n de Base de datos. Modelo Conceptual. Por favor desarrollar el modelo conceptual del siguiente ejercicio.
> >
> > Se requiere implementar un sistema para la reserva de taxis online llamada TaxiGo!. Un usuario se descarga la aplicaciÃ³n y se registra o inicia sesiÃ³n. Luego, el usuario registra el lugar donde el taxi deberÃ¡ recogerlo esto es: calle principal, nÃºmero de la casa, calle secundaria y ciudad. La aplicaciÃ³n verifica que existan carros disponibles e internamente notifica el pedido a los taxistas mÃ¡s cercanos y el que acepte primero la carrera se le asignarÃ¡ al usuario. Posteriormente, al usuario le aparecerÃ¡ los datos del taxi y del conductor, asÃ­ como el tiempo estimado que le tomarÃ¡ al taxi recogerlo y el valor de la carrera. Finalmente, si el usuario acepta la carrera se procederÃ¡ a cargar el valor a pagar a su tarjeta de crÃ©dito, de lo contrario se cancela la carrera.
> >
> > A la empresa le interesa registrar los datos del cliente (usuario) como los nombres, apellidos, fecha de nacimiento y telÃ©fono mÃ³vil. Una vez registrado el cliente se le asigna un usuario y contraseÃ±a para la aplicaciÃ³n. Cuando el usuario acepta cualquier carrera en el sistema guarda los primeros 4 nÃºmeros de la tarjeta de crÃ©dito y la fecha de pago. Se deberÃ¡ tambiÃ©n mantener un registro de los conductores de los taxis: nombres, apellidos, cuenta bancaria, cÃ©dula, gÃ©nero, tipo de licencia, direcciÃ³n y telÃ©fono. AdemÃ¡s, conocer datos del carro como la placa, tipo de gasolina, modelo, color y si su carro es alquilado o no. Si es alquilado se deberÃ¡ conocer los datos del propietario (nombres, apellidos, direcciÃ³n y telÃ©fono). Una vez registrado se les asigna a los conductores un cÃ³digo Ãºnico dentro de la compaÃ±Ã­a.
> >
> > Los datos de la carrera deben incluir, direcciÃ³n de origen y destino en texto y tambiÃ©n expresados en longitud y latitud, y su precio estimado. A la empresa tambiÃ©n le interesa generar estadÃ­sticas de uso de la aplicaciÃ³n, por ello es importante registrar tambiÃ©n las cancelaciones y viajes que culminaron con Ã©xito.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej02-taxigo.svg]]
>
> > [!success]- Clave de modelado
> > - Lugar de recojo: atributo **compuesto** (principal, nÃºmero, secundaria, ciudad), no entidad. Coordenadas: compuesto (lat, long).
> > - CONDUCTORâ€“CARRO: 1:1 (un carro activo) o 1:M con intermedia con fechas si se exige historial â€” decide y justifica.
> > - PROPIETARIO solo existe si el carro es alquilado: entidad opcional del lado 1 (0:1).
> > - Tarjeta: solo 4 dÃ­gitos + fecha (atributo simple de la carrera aceptada); nunca el nÃºmero completo.
> > - CancelaciÃ³n vs Ã©xito: **estado** de CARRERA (aceptada / cancelada / culminada); las estadÃ­sticas salen por consulta.

### âœï¸ Ejercicio 3 â€” Revista AZM (Taller 1, 2024 / 1E 2022)

> [!example] ðŸ§ª Planteamiento (fuente: `2024_1PAO_Taller_1_TICG1018.pdf`)
> - Autores envÃ­an ARTÃCULOS (tÃ­tulo, categorÃ­a, resumen, cuerpo, tags, ID Ãºnico, estado informado por email).
> - Revisores asignados por Ã¡rea: **3 por artÃ­culo**; autores y coautores de *otros* artÃ­culos pueden ser revisores de artÃ­culos ajenos.
> - Si se rechaza: se devuelve con criterios y hay **reenvÃ­o** (2da revisiÃ³n con 2 revisores nuevos; si falla, rechazo final).
> - AprobaciÃ³n exige que **todos** los revisores aprueben.
> - Aprobado â†’ revisores de planta verifican gramÃ¡tica, citado, referencias y formato â†’ publicaciÃ³n.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > La revista AZM desea digitalizar el proceso de recepciÃ³n, aprobaciÃ³n y publicaciÃ³n de las investigaciones en su revista, se lo ha contratado a usted para realizar este trabajo:
> >
> > Los autores envÃ­an sus artÃ­culos a la revista revisando su cumplimiento de los requisitos que demanda la revista, entre ellos estÃ¡n: el tipo de archivo, que no haya sido publicado anteriormente en otra revista, que estÃ© bien citado con fuentes verÃ­dicas, etc. El archivo se adjunta a un formulario que solicita el tÃ­tulo, la categorÃ­a (hardware, software, ux, etc), resumen, cuerpo y tags (etiquetas) del artÃ­culo. El estado del artÃ­culo se lo informa por email y se lo puede consultar indicando el ID del artÃ­culo que es un identificador Ãºnico asignado al artÃ­culo.
> >
> > La revista se encarga de asignar revisores al artÃ­culo de acuerdo al Ã¡rea de relacionada. Los autores y coautores del artÃ­culo y de otros artÃ­culos tambiÃ©n son considerados como revisores de otros artÃ­culos que no sea el suyo. Se asignan 3 revisores por artÃ­culo.
> >
> > Si en la revisiÃ³n se lo rechaza, se lo devuelve al autor indicando los criterios por el cual no cumpliÃ³ y dando una Ãºltima opciÃ³n a ser reenviado considerando los puntos de la primera revisiÃ³n. En la segunda evaluaciÃ³n se asignan 2 nuevos revisores. Si aÃºn el artÃ­culo no es aprobado en esta segunda revisiÃ³n, se lo rechaza y el autor es notificado vÃ­a email. Para que un artÃ­culo sea aprobado todos los revisores deben aprobar su publicaciÃ³n.
> >
> > Una vez que el articulo es aprobado la revista asigna revisores de AZM para verificar gramÃ¡tica, citado, referencias y formato. Una vez aprobado por todos los revisores de la revista, el artÃ­culo es publicado.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej03-azm.svg]]
>
> > [!success]- Clave de modelado
> > - AUTOR y REVISOR son **roles** de PERSONA: un autor es revisor de otros artÃ­culos, nunca del suyo (restricciÃ³n; anÃ³tala como regla de negocio).
> > - ARTÃCULOâ€“REVISOR es M:N con intermedia EVALUACIÃ“N (veredicto, criterios, ronda 1/2).
> > - "3 revisores ronda 1, 2 nuevos ronda 2, unanimidad": vive en la app, no en el ER.
> > - ReenvÃ­o: el mismo ARTÃCULO con versiÃ³n/ronda (atributo), no artÃ­culo nuevo.
> > - Estado: valor (enviado / observado / aprobado / publicado).

### âœï¸ Ejercicio 4 â€” Subsidio de combustibles (1E, 2024)

> [!example] ðŸ§ª Planteamiento (fuente: `2024-1PAO-1E-SBD.docx`, SecciÃ³n 2)
> - VEHÃCULO (placa, chasis, tipo, Ãºltima matriculaciÃ³n, edad, cilindraje, gama: baja/media/alta).
> - SUBSIDIO configurable: porcentaje segÃºn edad + cilindraje + gama; **cambia en cualquier momento**.
> - VENTA (tipo de gasolina, cantidad, valor oficial, % de subsidio, total pagado, vendedor, comprador).
> - GASOLINERA (empresa, direcciÃ³n); CIUDAD compuesta (paÃ­s, provincia, ciudad, calle principal, secundaria + **referencias**: varias).
> - EMPLEADO vendedor (cÃ©dula, nombres, apellidos) con **supervisor que tambiÃ©n es empleado y tambiÃ©n vende**.
> - Comprador: da sus datos o factura al propietario; **el vehÃ­culo cambia de propietario, pero la venta conserva el histÃ³rico**.
> - ðŸ“Œ Se pide: entidades, atributos, relaciones e identificadores.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > Se le ha asignado crear un sistema para poder registrar y controlar el subsidio focalizado de los combustibles, para esto se ha definido los parÃ¡metros para otorgar dichos subsidios son la edad de los vehÃ­culos, el cilindraje y la gama (baja, media, alta).
> >
> > Las gasolineras deben integrarse a un sistema Ãºnico de informaciÃ³n vehicular donde se encuentra la informaciÃ³n antes mencionada y adicional los datos de la placa, chasis, tipo (suv, van, todo terreno, etc.), fecha de Ãºltima matriculaciÃ³n.
> >
> > Los subsidios serÃ¡n otorgados en porcentaje respecto al precio oficial del galÃ³n de combustible, ejemplo un carro de gama baja, con 3 aÃ±os de comprado y 1.5 c.c. de cilindraje tiene un porcentaje de 30% del subsidio, pero, el mismo carro con 15 aÃ±os de antigÃ¼edad tendrÃ­a 5% del subsidio. Es decir, los subsidios son configurables basÃ¡ndose en los 3 parÃ¡metros antes indicados y pueden cambiar en cualquier momento.
> >
> > En cada venta de combustible se debe registrar cual es el tipo de gasolina (super, extra, eco, etc.) la cantidad, el valor oficial, el porcentaje del subsidio, el valor total pagado, el vendedor y el comprador.
> >
> > De la gasolinera se requiere conocer el nombre de la empresa, la direcciÃ³n. La ciudad estÃ¡ compuesta por paÃ­s, provincia, ciudad, calle principal, calle secundaria, referencias (pueden ser muchas referencias).
> >
> > Del empleado vendedor se requiere conocer la cÃ©dula, nombres, apellidos, y su supervisor que tambiÃ©n es un empleado. Se debe contemplar que el supervisor puede vender tambiÃ©n gasolina por lo cual la venta deberÃ­a quedar registrado a nombre de dicho supervisor.
> >
> > Cuando se realiza la venta el comprador puede decidir dar sus datos o pedir que le facturen a nombre del propietario del vehÃ­culo, de ambos, los datos a almacenar son cÃ©dula, nombre, apellidos, correo electrÃ³nico. Recuerde que un vehÃ­culo puede cambiar de propietario, pero la venta deberÃ­a mantener el histÃ³rico del propietario que se le vendiÃ³ el combustible.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej04-subsidio.svg]]
>
> > [!success]- Clave de modelado
> > - EMPLEADO *supervisa* EMPLEADO: **recursiva** 1:M con roles (supervisor / supervisado); la VENTA cuelga de EMPLEADO sin distinguir (ambos venden).
> > - HistÃ³rico de propietarios: VEHÃCULOâ€“PROPIETARIO es M:N con intermedia TENENCIA (fecha desde / hasta); la VENTA referencia al propietario **de ese momento**.
> > - CIUDAD: entidad con ubicaciÃ³n compuesta + multivaluado referencias.
> > - SUBSIDIO: entidad de configuraciÃ³n con vigencia (desde / hasta) porque cambia en el tiempo; la VENTA copia el % aplicado (foto del momento).

### âœï¸ Ejercicio 5 â€” Concursos del ministerio (1E, 2025)

> [!example] ðŸ§ª Planteamiento (fuente: `2025-1PAO-1E-SBD.docx`, SecciÃ³n 1)
> - ESTUDIANTE (cÃ©dula, nombres, apellidos, fecha de nacimiento, escuela); ESCUELA (nombre, direcciÃ³n, telÃ©fono, email).
> - CONCURSO (nombre, descripciÃ³n, fecha del evento, inicio/cierre de inscripciÃ³n, costo, premios).
> - PREMIOS por puesto (puesto + descripciÃ³n; N premios libres, ej. 1er lugar: $200 en cines).
> - INSCRIPCIÃ“N registra fecha y valor pagado (descuento por registro temprano).
> - COMITÃ‰ de PROFESORES (nombres, apellidos, telÃ©fono, email, perfil profesional).
> - CRITERIOS por concurso (nombre, descripciÃ³n, puntaje mÃ¡ximo).
> - Cada miembro califica a cada participante en cada criterio; resultados archivados.
> - ðŸ“Œ Se pide: modelo conceptual.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > Se requiere crear una aplicaciÃ³n para el ministerio de educaciÃ³n que permita llevar el control de los concursos en los que participan los estudiantes de las escuelas de acuerdo con las siguientes especificaciones:
> >
> > De cada estudiante se tendrÃ¡ la siguiente informaciÃ³n: cÃ©dula, nombres, apellidos, fecha de nacimiento y la escuela a la que pertenece. De cada escuela se tendrÃ¡ la siguiente informaciÃ³n: nombre, direcciÃ³n, telÃ©fono, email.
> >
> > De cada concurso se almacenarÃ¡ la siguiente informaciÃ³n: nombre, descripciÃ³n, fecha y hora del evento, fecha de inicio de inscripciÃ³n, fecha de cierre de inscripciÃ³n, costo de inscripciÃ³n y premios. Los premios deben especificar a quÃ© puesto corresponde y la descripciÃ³n del premio. Por ejemplo: Primer lugar: $200 en cines; Segundo lugar: $100 en compras de alimentos; Tercer lugar: $50 en viajes. (Se pueden crear tantos premios como se desee)
> >
> > Una vez que un concurso estÃ¡ creado, puede recibir inscripciones. Al inscribirse un estudiante, se deberÃ¡ registrar tambiÃ©n la fecha de inscripciÃ³n y el valor de inscripciÃ³n pagado, ya que podrÃ­an existir descuentos por un registro temprano.
> >
> > Cada concurso es evaluado por un comitÃ© conformado por varios profesores. El comitÃ© es presentado ante el pÃºblico por lo que se registrarÃ¡ en el sistema la informaciÃ³n de cada profesor miembro del comitÃ© como nombres, apellidos, telÃ©fono, email y una breve descripciÃ³n de su perfil profesional.
> >
> > En cada concurso el comitÃ© evaluarÃ¡ los criterios de calificaciÃ³n definidos para cada concurso. El criterio incluye el nombre, descripciÃ³n y el puntaje mÃ¡ximo a obtener. Por ejemplo, un concurso de programaciÃ³n puede tener criterios de eficacia, eficiencia, calidad, etc. Para cada estudiante participante, los miembros del comitÃ© registrarÃ¡n la calificaciÃ³n que obtuvieron en cada criterio. Los estudiantes con los mejores puntajes serÃ¡n los ganadores de los premios. Los resultados deben quedar registrados para consultas posteriores.
> >
> > (El examen incluye una figura con el modelo.)
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej05-concursos.svg]]
>
> > [!success]- Clave de modelado
> > - INSCRIPCIÃ“N: intermedia ESTUDIANTEâ€“CONCURSO con atributos (fecha, valor pagado).
> > - PREMIO: **dÃ©bil** de CONCURSO (puesto + descripciÃ³n; no existe sin su concurso).
> > - CALIFICACIÃ“N: ternaria PROFESORâ€“ESTUDIANTEâ€“CRITERIO (puntaje) â€” verifica que necesite a los tres (sÃ­: el puntaje es *de un profesor a un estudiante en un criterio*).
> > - Trampa: el comitÃ© es agrupaciÃ³n, no entidad (PROFESORâ€“CONCURSO M:N "integra comitÃ©"); el ganador sale por consulta.

### âœï¸ Ejercicio 6 â€” ReforestaciÃ³n NAREN (1E, 2023)

> [!example] ðŸ§ª Planteamiento (fuente: `2023-1PAO-1E-SBD.docx`, SecciÃ³n 2)
> - EVENTOS (nombre, inicio/fin) con organizadores y voluntarios.
> - ÃREAS con varios PUNTOS de encuentro (coordenadas) y fotos del antes/despuÃ©s.
> - ASISTENTES â€”organizadores y voluntariosâ€” (cÃ©dula, nombre, apellido, nacimiento, direcciÃ³n, foto).
> - RECOMENDACIONES por evento (botas, agua, abrigoâ€¦).
> - ÃRBOLES por Ã¡rea (tipos: guayacÃ¡n, roble, pinoâ€¦; cantidad asignada).
> - Asistencia al inicio y al fin del dÃ­a; GRUPOS con lÃ­der y ayudante (**voluntarios, no organizadores**).
> - Registro de Ã¡rboles no sembrados por Ã¡rea.
> - ðŸ“Œ Se pide: modelo conceptual.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios:
> >
> > La empresa Nacional de Recursos Naturales (NAREN) solicita desarrollar un sistema para administrar la reforestaciÃ³n de Ã¡reas verdes como bosques, selvas, etc.
> >
> > El sistema debe permitir organizar eventos de reforestaciÃ³n los cuales incluyen a los organizadores y voluntarios. Estos eventos deben contar con la fecha y hora de inicio y de fin, y un nombre. Por cada evento, se debe organizar distintas Ã¡reas de reforestaciÃ³n y para cada Ã¡rea pueden existir varios puntos de encuentro. Se debe registrar las coordenadas de los puntos de encuentro, el nombre de las Ã¡reas a reforestar y las fotos del antes y el despuÃ©s de cada Ã¡rea.
> >
> > Se requiere almacenar de los asistentes (organizadores y voluntarios) su cÃ©dula, nombre, apellido, fecha de nacimiento, direcciÃ³n domiciliaria y una foto.
> >
> > Para cada evento se publican recomendaciones a los asistentes, por ejemplo: deben vestir botas, traer una cantidad determinada de agua, deben usar abrigo, etc. Se asigna para cada Ã¡rea una cantidad determinada de Ã¡rboles a sembrar, de los cuales se debe almacenar los tipos de Ã¡rboles, ejemplo guayacÃ¡n, roble, pino, etc.
> >
> > Al inicio del dÃ­a los organizadores toman asistencia de los voluntarios, los dividen en grupos y se le asigna una cantidad determinada de Ã¡rboles que deben sembrar en un punto de coordenadas de referencia, cada grupo tiene un lÃ­der y un ayudante que responden por cada grupo. Tanto lÃ­deres como ayudantes son voluntarios, no organizadores.
> >
> > Al final del dÃ­a, los organizadores deben tomar nuevamente lista a los voluntarios y registrar por cada Ã¡rea si existieron Ã¡rboles que no fueron sembrados y que cantidad.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej06-naren.svg]]
>
> > [!success]- Clave de modelado
> > - ASISTENTE supertipo con subtipos ORGANIZADOR y VOLUNTARIO (lÃ­der/ayudante salen de VOLUNTARIO: **roles**, no subtipos nuevos).
> > - PUNTO dÃ©bil de ÃREA (coordenadas + orden dentro del Ã¡rea); FOTO: multivaluado del Ã¡rea (antes/despuÃ©s como valores o dÃ©bil con tipo).
> > - ASISTENCIA: intermedia VOLUNTARIOâ€“EVENTO (jornada inicio/fin, presente sÃ­/no).
> > - GRUPO: junta lÃ­der + ayudante + miembros + punto asignado + Ã¡rboles asignados/sembrados.

### âœï¸ Ejercicio 7 â€” Pho-grah.local (1E, 2023-2)

> [!example] ðŸ§ª Planteamiento (fuente: `2023-2PAO-1E-SBD.docx`, SecciÃ³n 2)
> - Usuarios (email, nombre, contraseÃ±a, edad, gÃ©nero, lugares de interÃ©s) suben MEDIOS a LUGARES (edificios, paisajesâ€¦).
> - LUGAR con **jerarquÃ­a libre** (Ecuador : Guayas : Guayaquil : MalecÃ³n : Torre Morisca).
> - MEDIOS en dos grupos: **estÃ¡ticos** y **dinÃ¡micos** (audio/video); cada medio con id, URL, texto corto y **hashtags**; repositorio de medios.
> - Se gestiona quÃ© usuario subiÃ³ quÃ© medio a quÃ© lugar.
> - ðŸ“Œ Se pide: entidades, atributos, relaciones e identificadores.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > La compaÃ±Ã­a Pho-grah.local (PL) requiere de una aplicaciÃ³n similar a Instagram (IG), por lo que requiere una base de datos relacional que cumpla con los siguientes requisitos de datos:
> >
> > PL describe que el objetivo principal de la aplicaciÃ³n es permitir a los usuarios que puedan subir fotos, archivos de audio, archivos de video, que correspondan a lugares definidos por los usuarios, tales como edificios, paisajes, lugares arquitectÃ³nicos, etc.
> >
> > La aplicaciÃ³n debe permitir a mÃºltiples usuarios darse de alta con un perfil de usuario que incluya, correo electrÃ³nico, nombre, contraseÃ±a, como mÃ­nimo, edad, gÃ©nero y lugares de interÃ©s.
> >
> > La aplicaciÃ³n debe permitir al usuario crear el concepto de Lugar. Los lugares pueden ser representados de manera jerÃ¡rquica, por ejemplo: Ecuador: Guayas: Guayaquil: MalecÃ³n LeÃ³n Febres Cordero: Torre Morisca. La profundidad de la jerarquÃ­a es libre.
> >
> > Considere a las fotos y archivos digitales como medios digitales divididos en dos grupos: medios estÃ¡ticos y medios dinÃ¡micos (audio y video). Estos medios estarÃ¡n almacenados en un repositorio en donde cada medio estÃ¡ representado por un id, una URL de acceso. A cada medio le corresponde un texto corto y un conjunto de hashtags. La aplicaciÃ³n debe permitir gestionar los medios que los usuarios suban a los lugares.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej07-phograh.svg]]
>
> > [!success]- Clave de modelado
> > - LUGAR *contiene* LUGAR: **recursiva** 1:M de profundidad libre (FK padre).
> > - Hashtags: **multivaluado** de MEDIO (pide tabla propia en el lÃ³gico).
> > - MEDIO supertipo con subtipos ESTÃTICO y DINÃMICO (Â¿aportan algo propio? duraciÃ³n el dinÃ¡mico, dimensiones el estÃ¡tico; si no, basta atributo tipo â€” justifica).
> > - SUBIDA: ternaria USUARIOâ€“MEDIOâ€“LUGAR (fecha): el mismo medio puede subirlo varios usuarios a varios lugares (sÃ­ necesita a los tres).

### âœï¸ Ejercicio 8 â€” Expresos escolares (1E, 2024-2)

> [!example] ðŸ§ª Planteamiento (fuente: `2024-2PAO-1E-SBD.docx`, SecciÃ³n 1)
> - Colegios contratan rutas; PADRES registran hogar (coordenadas) y representados (valida el colegio).
> - BUSETAS, CHOFERES (licencia + expiraciÃ³n), AYUDANTES; asignaciÃ³n semanal chofer + buseta + ayudante + ruta (**cambios a media semana** por enfermedad).
> - App envÃ­a posiciÃ³n periÃ³dica; padres ven distancia, placa, foto y nombre del conductor y ayudante.
> - CHECK de subida/bajada del estudiante (fecha/hora + novedad).
> - SuspensiÃ³n por falta de pago (la parada desaparece para el chofer).
> - Usuarios con **mÃ¡s de un rol** (chofer con representado en otro colegio).
> - PARADA (lat/long, direcciÃ³n, referencias, orden); COLEGIO (nombre, logo).
> - ðŸ“Œ Se pide: entidades, atributos, relaciones e identificadores.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Desarrolle el modelo conceptual del siguiente modelo de negocios. Indicar atributos, entidades, relaciones e identificadores:
> >
> > Crear el modelo conceptual de un sistema para administrar los recorridos de una empresa de expresos escolares. Para cumplir esto el sistema debe considerar las siguientes reglas de negocio.
> >
> > La empresa tiene contratos de servicios de expreso con diferentes colegios en varias partes del paÃ­s, los mismos que le detallan las rutas que deben cubrir y los estudiantes que deben recoger en cada ruta.
> >
> > Al inicio del aÃ±o lectivo los padres de familia se registran en el sistema y marcan las coordenadas de su hogar en la app mÃ³vil, adicional ingresan los datos de su o sus representados y posterior son validados por el colegio.
> >
> > La empresa cuenta con varias busetas, conductores y ayudantes; al iniciar la semana cada chofer es asignado a una buseta con un ayudante, los cuales se encargan de hacer el recorrido que tiene asignada la buseta. Se puede dar casos fortuitos ej. Un chofer se puede enfermar a media semana, entonces el cambio se lo realiza cuando sea necesario.
> >
> > El dispositivo mÃ³vil del conductor cuenta con una app que va enviando las coordenadas de la posiciÃ³n actual cada cierto tiempo del vehÃ­culo, de esta forma los padres de familia saben a quÃ© distancia se encuentra el expreso de su lugar de recogida junto a otros datos como son: la placa de la buseta, foto y nombre del conductor y ayudante.
> >
> > Al recoger al estudiante se debe colocar un check de ingreso en una lista, de esta forma se establece que el estudiante subiÃ³ al expreso desde su hogar y lo mismo sucede cuando lo retorna, se debe marcar otro check indicando que el estudiante efectivamente subiÃ³ al expreso para retornar a su hogar.
> >
> > El sistema debe permitir suspender el servicio a un estudiante en caso de que no haya pagado el valor mensual, de ser asÃ­, la ruta no mostrarÃ­a al chofer la parada de dicho estudiante.
> >
> > De los colegios se interesa conocer el nombre y un logo para customizar el entorno de la aplicaciÃ³n. De los padres de familia interesa conocer la cÃ©dula, nombres, apellidos. De los estudiantes se interesa conocer matricula, nombres apellidos, curso y estado (activo o inactivo). De los choferes interesa conocer cÃ©dula, nombres, apellidos, archivo de licencia y fecha de expiraciÃ³n. De los ayudantes interesa conocer la cÃ©dula, nombres y apellidos.
> >
> > Se puede dar la situaciÃ³n en que los usuarios tengan mÃ¡s de un rol, ejemplo un chofer hace la ruta para un colegio, pero podrÃ­a tener a un representado en otro colegio.
> >
> > Cada ubicaciÃ³n de recogida/llegada consta de latitud, longitud, direcciÃ³n, referencias y orden. El sistema ordena cada ubicaciÃ³n con un algoritmo interno para calcular la ruta mÃ¡s efectiva.
> >
> > La asistencia debe almacenar el dÃ­a de recogida/retorno, la fecha y hora en que el estudiante sube al expreso y alguna novedad.
> >
> > (El examen incluye dos figuras.)
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej08-expreso.svg]]
>
> > [!success]- Clave de modelado
> > - Roles mÃºltiples: PERSONA supertipo con roles PADRE / CHOFER / AYUDANTE / ESTUDIANTE (**sobrelapado**: un chofer puede ser padre).
> > - ASIGNACIÃ“N semanal: intermedia CHOFERâ€“BUSETAâ€“AYUDANTEâ€“RUTA con vigencia (desde / hasta); el cambio a media semana = cerrar fila y abrir otra.
> > - ASISTENCIA/check: intermedia ESTUDIANTEâ€“RUTAâ€“fecha (subida sÃ­/no, bajada sÃ­/no, hora, novedad).
> > - SuspensiÃ³n por pago: **estado** del ESTUDIANTE (activo / suspendido); la parada se filtra por consulta.
> > - PosiciÃ³n periÃ³dica: dÃ©bil de BUSETA (timestamp + coordenadas); no mezclar con PARADA (puntos fijos).

### âœï¸ Ejercicio 9 â€” CrÃ©dito hipotecario (3E, 2023-2)

> [!example] ðŸ§ª Planteamiento (fuente: `2023-2PAO-3E-SBD.docx`, SecciÃ³n 1)
> - PRESTATARIO (cÃ©dula, nombre, direcciÃ³n, telÃ©fono, ingresos, historial) y PRESTAMISTA del banco.
> - CONTRATO (tasa, plazo, monto, pagos mensuales, fechas); PROPIEDAD en garantÃ­a (direcciÃ³n, tasaciÃ³n por TASADOR: ubicaciÃ³n, tamaÃ±o, estado).
> - HISTORIAL: deudas (descripciÃ³n, fecha contraÃ­da / lÃ­mite / pagada) + tipos de crÃ©dito (tarjeta, estatalâ€¦, deuda actual, lÃ­mite).
> - Pagos mensuales alimentan el historial; incumplimiento â†’ relaciÃ³n legal (ejecuciÃ³n hipotecaria).
> - ðŸ“Œ Se pide: conceptual con entidades, atributos, relaciones y tipos.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Elabore el modelo conceptual incluyendo entidades, atributos, relaciones y sus tipos para el siguiente planteamiento:
> >
> > Se lo ha contratado para implementar un sistema que procese CrÃ©ditos Hipotecarios del Banco del PACIPICO. Para ello deberÃ¡ diseÃ±ar un modelo de base de datos que permita guardar los datos necesarios para solicitar y/o aprobar el otorgamiento del crÃ©dito.
> >
> > Para llevar a cabo un prÃ©stamo hipotecario, se debe considerar la participaciÃ³n del prestatario (que es la persona que solicita el prÃ©stamo hipotecario) y del prestamista que es el representante del Banco del PATIPICO que recepta la documentaciÃ³n del prestatario.
> >
> > El prestatario para solicitar un crÃ©dito Hipotecario debe indicar los siguientes datos cÃ©dula, nombre, direcciÃ³n, telÃ©fono, ingresos mensuales e historial crediticio. El prestamista revisa la informaciÃ³n y decide formalizar o no el contrato hipotecario. En el contrato se establecen los tÃ©rminos y condiciones como la tasa de interÃ©s, el plazo y monto del prÃ©stamo, montos de los pagos mensuales y su fecha de plazo. AdemÃ¡s, el prestatario proporciona informaciÃ³n sobre la propiedad que se utilizarÃ¡ como garantÃ­a para el prÃ©stamo, lo que incluye informaciÃ³n como direcciÃ³n de la propiedad y el valor de tasaciÃ³n. Este valor se determina mediante una evaluaciÃ³n realizada por un tasador profesional del banco, que examina diversos aspectos de la propiedad como la ubicaciÃ³n, tamaÃ±o, caracterÃ­sticas y estado de la propiedad (buen estado, requiere reparaciones, etc.). Un valor de tasaciÃ³n adecuado asegura al prestamista que la propiedad ofrecida como garantÃ­a tiene un valor suficiente para respaldar el monto del prÃ©stamo.
> >
> > El historial crediticio del prestatario es otro aspecto fundamental que influye en la aprobaciÃ³n del prÃ©stamo y las condiciones asociadas al mismo. Este historial incluye informaciÃ³n sobre el comportamiento financiero pasado del prestatario, como el manejo de deudas, que incluyen una descripciÃ³n, fecha que se lo contrajo, fecha lÃ­mite de pago y fecha que se lo pagÃ³. TambiÃ©n un historial de crÃ©dito que incluyan que tipo de crÃ©dito accediÃ³ (ej. Tarjeta de crÃ©dito, crÃ©ditos estatales, etc.) cantidad actual de la deuda y lÃ­mite mÃ¡ximo de crÃ©dito disponible. Un historial crediticio sÃ³lido aumenta la confianza del prestamista en la capacidad del prestatario para cumplir con las obligaciones del prÃ©stamo.
> >
> > Durante la vigencia del prÃ©stamo hipotecario, se establece una relaciÃ³n continua entre el prestamista y el prestatario segÃºn se realizan los pagos mensuales. Estos pagos se registran como parte del historial crediticio del prestatario, lo que puede afectar las relaciones futuras con otras entidades financieras. AdemÃ¡s, en caso de incumplimiento de pago, se activa una relaciÃ³n legal que puede llevar a medidas como la ejecuciÃ³n hipotecaria de la propiedad.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej09-hipotecario.svg]]
>
> > [!success]- Clave de modelado
> > - PRESTATARIO y PRESTAMISTA: roles de PERSONA (el prestamista es empleado del banco).
> > - PROPIEDADâ€“TASACIÃ“N 1:M con tasador y fecha (la tasaciÃ³n cambia: **historÃ­zala, no la sobrescribas**).
> > - DEUDA: dÃ©bil de PRESTATARIO. CONTRATO: intermedia PRESTATARIOâ€“PRESTAMISTAâ€“PROPIEDAD (tasa, plazo, monto).
> > - Incumplimiento/ejecuciÃ³n: **estado** del CONTRATO (vigente / en mora / en ejecuciÃ³n), no entidad nueva.

### âœï¸ Ejercicio 10 â€” Comunidad EcoLife (3E, 2024-2)

> [!example] ðŸ§ª Planteamiento (fuente: `2024-2PAO-3E-SBD.docx`, SecciÃ³n 1)
> - MIEMBRO (ID, nombre, apellido, email Ãºnico, registro, ubicaciÃ³n, puntos; **redes + cuentas**: multivaluados) en **hasta 4 MARCAS** (ID, nombre, descripciÃ³n, email).
> - PUBLICACIONES (ID, tÃ­tulo, contenido, fecha, red, cuenta, tipo: artÃ­culo / pregunta / respuesta / comentario) en un TEMA (ID, nombre Ãºnico, descripciÃ³n).
> - EVENTOS (ID, nombre, fecha/hora, ubicaciÃ³n, capacidad); RECOMPENSAS (ID, tipo, descripciÃ³n, puntos requeridos).
> - Reglas: miembro crea N publicaciones (cada una de un miembro y un tema); miembro asiste a N eventos; miembros reclaman recompensas; marcas crean publicaciones y organizan eventos.
> - ðŸ“Œ Se pide: conceptual en Chen + lÃ³gico pata de gallo normalizado.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Elabore el modelo conceptual incluyendo entidades, atributos, relaciones y sus tipos en notaciÃ³n de CHEN para el siguiente planteamiento:
> >
> > La empresa "EcoLife", una marca de productos sostenibles para el hogar, busca fortalecer la lealtad de sus clientes y obtener informaciÃ³n valiosa para el desarrollo de nuevos productos a travÃ©s de la creaciÃ³n y gestiÃ³n de una comunidad de marca en lÃ­nea.
> >
> > En la estructura de comunidad gestionada por EcoLife, cada individuo que se une se convierte en un miembro, identificado de manera Ãºnica por su ID_Miembro. Guardamos su nombre, apellido, correo electrÃ³nico (que debe ser Ãºnico), la fecha de registro y su ubicaciÃ³n. AdemÃ¡s, cada miembro acumula puntos segÃºn su participaciÃ³n y/o publicaciÃ³n en las redes, por lo que es importante guardar las redes sociales que el miembro estÃ¡ registrado y los nombres de las cuentas. Es importante destacar que EcoLife gestiona un grupo de marcas, y un mismo miembro puede formar parte de hasta cuatro de estas marcas dentro del ecosistema EcoLife.
> >
> > Dentro de cada comunidad de marca, se generan Publicaciones, identificadas por un ID_PublicaciÃ³n, incluyendo tÃ­tulo, contenido, fecha de publicaciÃ³n, red social en el cual se publicÃ³ y nombre de la cuenta, y el tipo de publicaciÃ³n (artÃ­culo, pregunta, respuesta o comentario). Cada publicaciÃ³n se clasifica dentro de un Tema especÃ­fico, con su propio ID_Tema, nombre Ãºnico y descripciÃ³n.
> >
> > EcoLife organiza Eventos para los miembros de sus marcas, cada uno con un ID_Evento, nombre, fecha y hora, ubicaciÃ³n, descripciÃ³n y Capacidad mÃ¡xima de asistentes. Para incentivar la participaciÃ³n, EcoLife ofrece Recompensas, identificadas por un ID_Recompensa, tipo (descuento, producto gratis, etc.), descripciÃ³n y Puntos Requeridos.
> >
> > Toda esta estructura es gestionada por EcoLife y sus marcas afiliadas, identificadas por un ID_Marca, nombre, descripciÃ³n y correo electrÃ³nico. Un Miembro puede crear mÃºltiples Publicaciones dentro de la comunidad de la marca a la que pertenece, y cada publicaciÃ³n estÃ¡ asociada a un solo miembro. Cada PublicaciÃ³n pertenece a un Tema, categorizando el contenido. Un Miembro puede asistir a mÃºltiples Eventos organizados por EcoLife o la marca de la que forma parte, y cada evento puede tener mÃºltiples miembros asistentes. Los Miembros pueden reclamar Recompensas con sus puntos. La Marca EcoLife y sus submarcas crean Publicaciones y organizan Eventos, siendo responsables de la actividad comunitaria. Esta estructura promueve la participaciÃ³n y la lealtad, considerando la posibilidad de que un miembro participe en varias comunidades de marca dentro de EcoLife.
> >
> > (El examen incluye una figura. La SecciÃ³n 2 pide ademÃ¡s el modelo lÃ³gico con notaciÃ³n pata de gallo completamente normalizado.)
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej10-ecolife.svg]]
>
> > [!success]- Clave de modelado
> > - MIEMBROâ€“MARCA M:N con **tope 4** (restricciÃ³n de app, anÃ³tala). Redes + cuentas: multivaluado doble (red, cuenta) â†’ tabla propia.
> > - PUBLICACIÃ“Nâ€“TEMA N:1; PUBLICACIÃ“Nâ€“MIEMBRO N:1 (autor); PUBLICACIÃ“Nâ€“MARCA N:1 (emisora).
> > - Tipo de publicaciÃ³n: valor; si un comentario responde a otra publicaciÃ³n: **recursiva** 1:M.
> > - ASISTENCIA (miembroâ€“evento) y CANJE (miembroâ€“recompensa con fecha y puntos usados): intermedias con atributos.
> > - Capacidad del evento: restricciÃ³n, no entidad.

## ðŸ…±ï¸ Bloque B â€” Dependencias y normalizaciÃ³n (resueltos)

### âœï¸ Ejercicio 11 â€” Caso `cod_estud` (Taller 1, 2026)

> [!example] ðŸ§ª Planteamiento (fuente: `2026_1PAO_Taller_1_TICG1018.pdf`, punto 2)
> - Figura del examen (diagrama de dependencias; la tabla universal sin normalizar):
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej11-diagrama-dependencias.svg]]
> - ðŸ“Œ Se pide:
>   - 1) Clave primaria.
>   - 2) Dependencias parciales.
>   - 3) Dependencias transitivas.
>   - 4) Normalizar hasta 3FN + diagrama lÃ³gico.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > 2. Se tiene el siguiente diagrama de dependencias:
> >
> > cod_estud, cod_curso, nombre_estud, correo_estud, nomb_curso, horas_curso, cod_instructor, nomb_instructor, nota_final
> >
> > 1. Identifique la clave primaria.
> > 2. Identifique las dependencias parciales.
> > 3. Identifique las dependencias transitivas.
> > 4. Normalice la relaciÃ³n hasta Tercera Forma Normal (3FN) y obtenga el diagrama lÃ³gico.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej11-dep-flow.svg]]
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej11-modelo-3fn.svg]]
>
> > [!success]- SoluciÃ³n guiada
> > - 1) La nota depende del **par** (estudiante, curso): PK = `(cod_estud, cod_curso)`.
> >   - `cod_estud` â†’ nombre, correo.
> >   - `cod_curso` â†’ nomb_curso, horas, cod_instructor.
> >   - instructor â†’ nomb_instructor.
> > - 2) Parciales (parte de la PK):
> >   - `cod_estud` â†’ nombre_estud, correo_estud.
> >   - `cod_curso` â†’ nomb_curso, horas_curso, cod_instructor.
> > - 3) Transitiva: `cod_curso` â†’ `cod_instructor` â†’ `nomb_instructor`.
> > - 4) Esquema 3FN:
> >   - ESTUDIANTE(cod_estud PK, nombre, correo).
> >   - INSTRUCTOR(cod_instructor PK, nombre).
> >   - CURSO(cod_curso PK, nombre, horas, cod_instructor FK).
> >   - MATRÃCULA(cod_estud PK/FK, cod_curso PK/FK, nota_final).
> > - Verifica: toda FK referencia una PK; la intermedia lleva la PK compuesta; sin transitivas restantes.

### âœï¸ Ejercicio 12 â€” Ventas digitales (1E, 2025, con soluciÃ³n oficial)

> [!example] ðŸ§ª Planteamiento (fuente: `2025-1PAO-1E-SBD.docx`, SecciÃ³n 3)
> - Tabla de Excel a normalizar (PK: Vendedor ID + Producto ID + Fecha Venta):
>
> | Vendedor ID | Producto ID | Fecha Venta | Cantidad | Vendedor Nombre | Producto Nombre | Precio Unitario | Servidor ID | Servidor RegiÃ³n |
> |---|---|---|---|---|---|---|---|---|
> | 501 | A101 | 01/03/24 | 3 | Torres | Antivirus Pro | 25.00 | 78 | AmÃ©rica Norte |
> | 501 | A102 | 02/03/24 | 1 | Torres | Firewall Plus | 40.00 | 78 | AmÃ©rica Norte |
> | 502 | A101 | 02/03/24 | 2 | LÃ³pez | Antivirus Pro | 25.00 | 79 | Europa Oeste |
> | 503 | A103 | 02/03/24 | 1 | GarcÃ­a | Cloud Vault | 60.00 | 80 | Asia Central |
> | 501 | A101 | 05/03/24 | 4 | Torres | Antivirus Pro | 25.00 | 78 | AmÃ©rica Norte |
> - DF dadas:
>   - (las 3) â†’ Cantidad, Vendedor Nombre, Nombre Producto, Servidor ID, Servidor RegiÃ³n.
>   - Vendedor ID â†’ Vendedor Nombre, Servidor ID, Servidor RegiÃ³n.
> - ðŸ“Œ Se pide: DF adicionales y esquema en cada FN.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Una empresa registra sus ventas digitales en la siguiente tabla de Excel. Realice el proceso de normalizaciÃ³n del esquema relacional de la tabla hasta la 3era Forma Normal. Suponga que la clave primaria es (Vendedor ID, Producto ID, Fecha Venta).
> >
> > Suponga tambiÃ©n las siguientes dependencias funcionales:
> >
> > (Vendedor ID, Producto ID, Fecha Venta) â†’ Cantidad, Vendedor Nombre, Nombre Producto, Servidor ID, Servidor RegiÃ³n
> >
> > Vendedor ID â†’ Vendedor Nombre, Servidor ID, Servidor RegiÃ³n
> >
> > Identifique las dependencias funcionales adicionales y sus tipos para justificar el esquema relacional obtenido en cada etapa del proceso.
> >
> > (La tabla de datos va arriba. El documento del examen trae ademÃ¡s la soluciÃ³n oficial con rÃºbrica, que es la usada en la clave.)
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej12-modelo-3fn.svg]]
>
> > [!success]- SoluciÃ³n (la del examen)
> > - DF adicionales:
> >   - (las 3) â†’ Precio Unitario.
> >   - Producto ID â†’ Producto Nombre, Precio Unitario.
> > - Diagrama de dependencias (lÃ©elo antes de partir):
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej12-dependencias.svg]]
> > - 1FN: cumplida (sin listas ni multivaluados).
> > - 2FN (fuera parciales):
> >   - PRODUCTO(Producto ID PK, Nombre, Precio).
> >   - VENDEDOR(Vendedor ID PK, Nombre, Servidor ID, RegiÃ³n).
> >   - VENTA(Vendedor ID PK/FK, Producto ID PK/FK, Fecha, Cantidad).
> > - 3FN (fuera la transitiva Vendedor â†’ Servidor â†’ RegiÃ³n):
> >   - SERVIDOR(Servidor ID PK, RegiÃ³n).
> >   - VENDEDOR(Vendedor ID PK, Nombre, Servidor ID FK).
> > - Moraleja de corrector: declara cada DF con su tipo (total / parcial / transitiva) antes de partir; eso solo ya da puntos.

### âœï¸ Ejercicio 13 â€” Recetas de farmacia (1E, 2024)

> [!example] ðŸ§ª Planteamiento (fuente: `2024-1PAO-1E-SBD.docx`, SecciÃ³n 4)
> - Tabla a normalizar (fÃ­jate en las columnas con listas):
>
> | ID_Receta | Nombre_Producto | Ingredientes | Cantidad_Ingredientes | Precio_Unitario | Etapa_Produccion |
> |---|---|---|---|---|---|
> | 1 | Comprimidos de Paracetamol | Paracetamol (polvo), AlmidÃ³n de maÃ­z, Estearato de magnesio | 500 mg, 1 g, 10 mg | 0.10 | Mezclado, GranulaciÃ³n, CompresiÃ³n, Recubrimiento |
> | 2 | Jarabe de Jengibre | Extracto de Jengibre, Agua purificada, Sacarosa, Ãcido cÃ­trico | 200 mg, 50 ml, 10 g, 0.5 g | 0.80 | Mezclado, Filtrado, Envasado |
> | 3 | UngÃ¼ento de CalÃ©ndula | Extracto de CalÃ©ndula, Vaselina, Lanolina | 5 g, 20 g, 10 g | 1.50 | Mezclado, Envasado |
> | 4 | CÃ¡psulas de Vitamina C | Ãcido ascÃ³rbico (polvo), Celulosa microcristalina, Estearato de magnesio | 500 mg, 200 mg, 10 mg | 0.20 | Mezclado, Llenado de cÃ¡psulas |
> | 5 | SuspensiÃ³n antibiÃ³tica | Amoxicilina (polvo), Sacarosa, Saborizante a fresa, Agua purificada | 250 mg, 5 g, 1 ml, 50 ml | 1.20 | Mezclado, HomogenizaciÃ³n, Envasado |
> - ðŸ“Œ Se pide: normalizar a 3FN justificando cada FN + diagrama lÃ³gico.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Normalizar el siguiente esquema relacional hasta la 3era Forma Normal. Justificar porque cumple/no cumple con la Forma Normal y obtener el diagrama lÃ³gico normalizado.
> >
> > (La tabla de recetas va arriba.)
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej13-modelo.svg]]
>
> > [!success]- SoluciÃ³n guiada
> > - 1FN: Ingredientes, Cantidades y Etapas son **listas paralelas** (multivaluados) â†’ filas atÃ³micas:
> >   - PRODUCTO(ID_Receta PK, Nombre, Precio).
> >   - DETALLE(ID_Receta PK/FK, Ingrediente PK, Cantidad, Etapa).
> > - 2FN: Â¿algo depende de **parte** de la PK?
> >   - Nombre y Precio dependen de ID_Receta (parte) â†’ ya separados en PRODUCTO.
> >   - En el detalle: Cantidad depende de (Receta + Ingrediente); Etapa, de (Receta + Etapa) â†’ si la PK del detalle es triple, hay parciales: parte en DETALLE_INGREDIENTE y DETALLE_ETAPA.
> > - 3FN: sin no-primos que dependan de no-primos (verifica: el precio depende de la PK â€” sano).
> > - JustificaciÃ³n que pide el examen: nombra la anomalÃ­a que elimina cada paso (inserciÃ³n: no puedes crear un ingrediente sin receta; borrado: borrar la receta borra el catÃ¡logo).

### âœï¸ Ejercicio 14 â€” Artefactos MABE/Xiaomi (1E, 2022)

> [!example] ðŸ§ª Planteamiento (fuente: `2022-2PAO-1E-SBD.docx`, SecciÃ³n 4)
> - Tabla de artefactos (el examen la trae traspuesta; aquÃ­ ya girada con las listas a la vista):
>
> | numero | linea | modelo | litros | precio_venta | codigo_linea | marca | tipo | distribuidor | importador |
> |---|---|---|---|---|---|---|---|---|---|
> | 023 | blanca | RMA255FYEU | 250 | 509.86 | 001 | MABE | refrigerador | Mabetec, Mayepsa, ElectroGam, Mabe s.a. | Imaco, Importadora Frailes, Multiclimec, Imp. Lorences |
> | 022 | marron | P1L55M6 | NULL | 598.98 | 002 | Xiaomi | televisor | Xiaomi Store, GadgetMi, Telnet, MundoCellOnline | Noboa Distribuidora, Importadora JMV |
> | 019 | blanca | LMDE3124PBAB0 | 13 | 289.99 | 001 | MABE | lavadora | Mabetec, Mayepsa, ElectroGam, Mabe s.a. | Imaco, Importadora Frailes, Multiclimec, Imp. Lorences |
> - ðŸ“Œ Se pide: normalizar a 3FN explicando anomalÃ­as por FN.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Aplicar las normalizaciones (hasta la 3era Forma Normal) para evitar posibles anomalÃ­as y redundancia en los datos. Explique cada una de las anomalÃ­as encontradas en las diferentes formas normales.
> >
> > (Tabla DATOS DE ARTEFACTOS arriba, girada a orientaciÃ³n normal.)
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej14-modelo.svg]]
>
> > [!success]- SoluciÃ³n guiada
> > - 1FN: distribuidor e importador son listas â†’ tablas propias:
> >   - ARTEFACTO_DISTRIBUIDOR(numero PK/FK, distribuidor PK).
> >   - ARTEFACTO_IMPORTADOR(numero PK/FK, importador PK).
> > - 2FN: PK simple (numero) â‡’ **2FN automÃ¡tica**; verifica que no haya PK compuesta escondida.
> > - 3FN: transitiva numero â†’ codigo_linea â†’ (lÃ­nea, marca):
> >   - LINEA(codigo_linea PK, lÃ­nea, marca).
> >   - ARTEFACTO(numero PK, modelo, litros, precio, tipo, codigo_linea FK).
> > - Ojo: litros vacÃ­o en una fila = NULL permitido (no rompe 1FN); tipo depende del modelo â€” solo haz tabla TIPO si el examen lo exige.

### âœï¸ Ejercicio 15 â€” Dependencias abstractas K-A-B-C-D-E-F (1E, 2023)

> [!example] ðŸ§ª Planteamiento (fuente: `2023-1PAO-1E-SBD.docx`, SecciÃ³n 4)
> - DF conocidas:
>   - K â†’ A, B.
>   - C â†’ D, E, F.
>   - D â†’ F.
> - La columna C trae listas (C1, C2â€¦) en la tabla.
> - ðŸ“Œ Se pide: normalizar a 3FN explicando anomalÃ­as. Es el drill mÃ¡s rÃ¡pido del bloque: Ãºsalo para calentar.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Aplicar las normalizaciones (hasta la 3era Forma Normal) para evitar posibles anomalÃ­as y redundancia en los datos. Explique cada una de las anomalÃ­as encontradas en las diferentes formas normales.
> >
> > Considerar que:
> >
> > - K determina a A, B
> > - C determina a D, E, F
> > - D determina a F
> >
> > (La tabla de datos con las listas de C va en el PDF.)
> **ðŸ“Š Complementos de la soluciÃ³n** â€” funciÃ³n + diagrama; dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej15-dep-flow.svg]]
>
> > [!success]- SoluciÃ³n guiada
> > - Diagrama de dependencias:
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej15-dependencias.svg]]
> > - 1FN: C trae listas â†’ separa con PK (K, C).
> > - 2FN (fuera parciales sobre (K, C)):
> >   - K_TABLA(K PK, A, B).
> >   - C_TABLA(C PK, D, E, F).
> >   - PUENTE(K PK/FK, C PK/FK).
> > - 3FN (transitiva C â†’ D â†’ F):
> >   - D_TABLA(D PK, F).
> >   - C_TABLA(C PK, D FK, E).
> > - Verifica las claves corriendo la funciÃ³n de arriba en tu cuaderno de Python (los dos `print` confirman la PK y las tablas).

### âœï¸ Ejercicio 16 â€” STORE_ITEM y MORE_STUFF (LecciÃ³n 2, 2024)

> [!example] ðŸ§ª Planteamiento (fuente: `Leccion 2 - PAO I 2024.pdf` â€” texto completo, sin figura)
> - `STORE_ITEM(SKU, PromotionID, Vendor, Style, Price)` con DF:
>   - (SKU, PromotionID) â†’ todos.
>   - SKU â†’ Vendor, Style.
> - `MORE_STUFF(D, O, N, T, C, R, Y)` con DF:
>   - (D, O) â†’ todos.
>   - (C, R) â†’ Y.
>   - D â†’ N.
> - ðŸ“Œ Se pide: Â¿en quÃ© FN estÃ¡ cada una? Normaliza.
>
> > [!quote]- ðŸ“„ Enunciado original
> >
> > Transformar a modelo lÃ³gico el siguiente modelo conceptual. (CLIENTEâ€”HORARIO: figura en el PDF.)
> >
> > En que forma normal se encuentra la siguiente relacion. Normalise si es necesario.
> >
> > Tabla: STORE_ITEM (SKU, PromotionID, Vendor, Style, Price). Dependencias: (SKU, PromotionID) â†’ Vendor, Style, Price; SKU â†’ Vendor, Style.
> >
> > Tabla: MORE_STUFF (D, O, N, T, C, R, Y). Dependencias: (D, O) â†’ N, T, C, R, Y; (C, R) â†’ Y; D â†’ N.
> **ðŸ“Š Diagrama de la soluciÃ³n** â€” dibuja el tuyo primero y compara al abrir la clave.
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej16-dep-flow.svg]]
>
> > [!success]- SoluciÃ³n guiada
> > - Diagrama de dependencias STORE_ITEM:
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej16-store-item.svg]]
> > - STORE_ITEM: parcial SKU â†’ Vendor, Style â‡’ estÃ¡ en **1FN**.
> >   - 2FN: ITEM(SKU PK, Vendor, Style); PROMO(SKU PK/FK, PromotionID PK/FK, Price) â€” el precio depende del par (precio *en esa promociÃ³n*), asÃ­ que queda en la intermedia.
> > - Diagrama de dependencias MORE_STUFF:
> > ![[Unidad 0 - Guias y Ejercicios/Diagramas/ej16-more-stuff.svg]]
> > - MORE_STUFF: parcial D â†’ N â‡’ **1FN**.
> >   - 2FN: D_TABLA(D PK, N) + resto (D, O, T, C, R, Y).
> >   - Transitiva (C, R) â†’ Y con (C, R) no-primo â‡’ **3FN**: CR_TABLA(C PK, R PK, Y) + resto (D, O, T, C, R con FK).
> > - PatrÃ³n de examen: determinante doble â†’ sospecha parcial; DF entre no-primos â†’ transitiva.

## ðŸ…²ï¸ Bloque C â€” Banco de conceptos (V/F y completar)

> [!question] â“ Ronda 1 â€” de exÃ¡menes reales (responde, luego abre)
> - De modelado:
>   - Una relaciÃ³n de una entidad consigo misma se llamaâ€¦ (1E 2024).
>   - Un atributo calculable desde otros atributos es vÃ¡lido (1E 2022).
>   - Una entidad fuerte no depende de otra para existir (1E 2022).
> - De integridad y claves:
>   - NingÃºn componente de una FK puede tener valores ausentes en la PK referenciada (1E 2022/2024).
>   - Las PK pueden aceptar nulos (1E 2024).
> - De normalizaciÃ³n:
>   - "Todos los no-clave dependen de la clave completa y no de una parte" es regla deâ€¦ (1E 2024).
>   - La 1FN no permite multivaluados, compuestos ni combinaciones (1E 2023).
>   - Las FN buscan minimizar redundancia y anomalÃ­as de inserciÃ³n/actualizaciÃ³n/borrado (1E 2023).
>
> > [!success]- Respuestas
> > - De modelado: **recursiva** (o rÃ©flexiva); **verdadero** (derivado, Ã³valo punteado); **verdadero**.
> > - De integridad: **verdadero** (integridad referencial); **falso** (entidad: PK nunca NULL).
> > - De normalizaciÃ³n: **2FN**; **verdadero**; **verdadero**.

## âœ… Checklist pre-taller (rÃºbrica 1E 2025)

> [!tip] ðŸ“Œ Con quÃ© te califican (25 pts el lÃ³gico)
> Entidades completas (6) + atributos con tipos (6) + PK/FK y binarias (6) + especiales ternarias/recursivas/multivaluadas (7). Antes de entregar verifica: Â¿contÃ© tablas al final? Â¿toda FK apunta a una PK? Â¿las M:N tienen intermedia? Â¿la 1:1 total-total se fusionÃ³? (protocolo en [[01 - ConversiÃ³n MC a ML por cardinalidad]]).

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-guia1
- Â¿Recursiva vs ternaria?::1 entidad en 2 roles (FK a sÃ­ misma) vs 3 entidades que se necesitan a la vez (intermedia triple).
- Â¿HistÃ³rico propietario (subsidio) cÃ³mo?::M:N con vigencia desde/hasta; la venta referencia al propietario de ese momento.
- Â¿Multivaluado al lÃ³gico?::Tabla propia con (PK original como FK + valor) en PK compuesta.
- Â¿Supervisor que vende (subsidio)?::Recursiva 1:M; la venta cuelga de EMPLEADO sin distinguir.
- Â¿PK de (cod_estud, cod_curso) por quÃ©?::La nota depende del par; ni del uno ni del otro solos.
- Â¿2FN automÃ¡tica cuÃ¡ndo?::PK de un solo atributo (no hay parte de la cual depender).
- Â¿Transitiva tÃ­pica?::No-primo â†’ no-primo (instructor â†’ nombre; servidor â†’ regiÃ³n; lÃ­nea â†’ marca).
- Â¿ReenvÃ­o AZM es artÃ­culo nuevo?::No: mismo artÃ­culo, versiÃ³n/ronda como atributo.
- Â¿Lugar jerÃ¡rquico (Pho-grah) cÃ³mo?::Recursiva 1:M (FK padre), profundidad libre.
- Â¿AsignaciÃ³n semanal con cambios (expreso)?::Intermedia con vigencia; cambio = cerrar fila + abrir otra.
- Â¿Precio en PROMO (Ej. 16) por quÃ© en la intermedia?::Depende del par (SKU, PromotionID): es total, no parcial.
- Â¿Clausura para quÃ©?::Verificar que la PK candidata determine todo el universo antes de partir.

## ðŸ§­ Seguir con

> [!info] ðŸ§­ Seguir con
>
> - MÃ©todo: [[02 - Entidades, atributos, claves y relaciones]] Â· [[03 - Modelo relacional, ERM y casos Tiny College]] Â· [[01 - ConversiÃ³n MC a ML por cardinalidad]] Â· [[02 - Primera forma normal y diccionario de datos]] Â· [[03 - Segunda y tercera forma normal]]
> - Ãndices: [[Universidad/3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0|Unidad 0]] Â· [[00 - Ãndice Unidad 1]] Â· [[Universidad/3er Semestre/Sistema de Bases de Datos/Unidad 2 - Modelo lÃ³gico y conversiÃ³n/00 - Ãndice Unidad 2]]

## ðŸ“š Referencias

> [!quote] ðŸ“š Referencias
>
> - `2026_1PAO_Taller_1_TICG1018.pdf` â€” Taller 1 (lavanderÃ­a + `cod_estud`).
> - `2024_1PAO_Taller_1_TICG1018.pdf` â€” Taller 1 2024 (revista AZM; escaneado, enunciado extraÃ­do por OCR).
> - `Leccion 1 - PAO I 2024.pdf` â€” TaxiGo! (escaneado, enunciado por OCR).
> - `Leccion 2 - PAO I 2024.pdf` â€” conversiÃ³n + STORE_ITEM/MORE_STUFF (escaneado, enunciado por OCR).
> - `2024-1PAO-1E-SBD.docx` â€” 1E 2024 (subsidio, receta, conceptos, rÃºbrica por secciones).
> - `2025-1PAO-1E-SBD.docx` â€” 1E 2025 (concursos, ventas con soluciÃ³n oficial, rÃºbrica del lÃ³gico, NesflisDB).
> - `2022-2PAO-1E-SBD.docx` â€” 1E 2022 (AZM, artefactos, conceptos V/F).
> - `2023-1PAO-1E-SBD.docx` â€” 1E 2023 (NAREN, K-A-B-C-D-E-F).
> - `2023-2PAO-1E-SBD.docx` â€” 1E 2023-2 (Pho-grah + conteo de tablas).
> - `2024-2PAO-1E-SBD.docx` â€” 1E 2024-2 (expreso escolar).
> - `2023-2PAO-3E-SBD.docx` / `2024-2PAO-3E-SBD.docx` â€” 3E (hipotecario, EcoLife).
> - `Taller 2 PAO-2026-1  SOL.pdf` â€” hotel 1FNâ€“3FN con soluciÃ³n (desarrollado en [[03 - Segunda y tercera forma normal]]).

---

**Tags:** #TICG1018 #unidad0 #guia #taller1 #bd


---
dg-publish: true
tags: [CCPG1004, cysoc, unidad1, redes-internet]
---

# 🌐 Redes e Internet

## 🎯 Introducción

> [!info] 💡 ¿Cómo se conectaron las computadoras entre sí?
>
> Durante décadas, las computadoras trabajaron de forma aislada. La necesidad de compartir información y recursos impulsó el desarrollo de las redes, que eventualmente evolucionaron hasta formar la Internet que conocemos hoy.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/05_-_Redes_e_Internet_01.svg]]
>
> **Se lee así:** la evolución de las redes: computadoras aisladas (los 50), redes locales LAN (60-70), ARPANET (red militar de conmutación de paquetes), Internet (TCP/IP como estándar), World Wide Web (publicación sobre Internet).
> **Por qué importa:** Internet no es la WWW: la Web es una aplicación sobre Internet (la capa de aplicación del stack TCP/IP); confundirlas impide entender por qué tu correo y tu navegador usan el mismo cable.
> **Ejemplo:** al hacer clic en un enlace, tu navegador abre HTTP sobre TCP/IP: la web viaja por Internet, no es Internet.

---

## 🔬 ARPANET — El origen de todo (1967)

> [!note] 🔬 La primera red de computadoras
>
> **ARPANET** fue una red patrocinada por el gobierno de los Estados Unidos, creada originalmente con fines militares durante la **Guerra Fría**. Fue desarrollada por la agencia **RAND** y comenzó a operar a finales de los años sesenta.
>
> En sus inicios consistía en apenas **2 nodos**, concentrados principalmente en las áreas de **Los Ángeles y Boston**.
>
> | Dato | Detalle |
> |---|---|
> | **Año de inicio** | 1967 |
> | **Creador** | RAND Corporation / Gobierno de EE.UU. |
> | **Propósito original** | Comunicación militar resistente a ataques |
> | **Nodos iniciales** | 2 (Los Ángeles y Boston) |
> | **Relevancia** | Primera red de computadoras de la historia |
>
> ### Expansión de ARPANET
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/05_-_Redes_e_Internet_02.svg]]
>
> **Se lee así:** la cronología de ARPANET: 1967 (RAND la crea con presupuesto militar), 1970 (expande a universidades), 1972 (idea de protocolos comunes), 1983 (ARPANET se divide, nace MILNET exclusivo militar), 1979 (DEC+Intel+Xerox estandarizan Ethernet), 1985 (Ethernet en PCs), 1989 (Novell masifica las LAN), 1990 (TCP/IP estándar de Internet), 1991 (Tim Berners-Lee crea la WWW).
> **Por qué importa:** la Internet nació como proyecto militar distribuido; su arquitectura tolerante a fallos es lo que hoy permite que una caída en una ruta no detenga tu conexión.
> **Ejemplo:** cuando un paquete sale de tu casa viaja por varias rutas distintas decididas por cada enrutador; eso es herencia directa de la arquitectura ARPANET.

---

## 🔌 Ethernet — La red local (1973)

> [!note] 🔌 Conectando computadoras en un mismo espacio
>
> En **1980**, el modelo de una gran máquina con muchos usuarios dio paso a una **red de máquinas más pequeñas conectadas** para compartir recursos como impresoras, software y datos.
>
> El **Ethernet**, inventado por **Robert Metcalfe y David Boggs en 1973**, fue el estándar que hizo esto posible. Era un cable coaxial que conectaba máquinas usando un conjunto de protocolos que permitían la comunicación entre ellas.
>
> | Dato | Detalle |
> |---|---|
> | **Año** | 1973 |
> | **Inventores** | Robert Metcalfe y David Boggs |
> | **Tecnología** | Cable coaxial + protocolos de comunicación |
> | **Estandarización** | 1979 — DEC, Intel y Xerox lo adoptan como estándar |
> | **Masificación** | 1985 — chip Intel avanzado lo hace práctico para PCs |
>
> > 💡 En **1979**, DEC (*Digital Equipment Corporation*), Intel y Xerox se unieron para establecer Ethernet como estándar de facto para redes locales.

---

## 🏢 Redes LAN y Netware (1989)

> [!note] 🏢 Redes de área local
>
> Las estaciones de trabajo o computadoras personales conectadas en red se conocieron como **LAN** (*Local Area Network* — Red de Área Local).
>
> En **1989**, **Netware de Novell** conectó PCs a un servidor de archivos central con gran capacidad de almacenamiento, permitiendo una medida de control central sobre los recursos compartidos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/05_-_Redes_e_Internet_03.svg]]
>
> | Término | Definición |
> |---|---|
> | **LAN** | Red de área local — computadoras en un mismo edificio o campus |
> | **WAN** | Red de área amplia — conecta redes LAN entre ciudades o países |
> | **Servidor** | Máquina con gran capacidad que provee recursos a la red |
> | **Estación de trabajo** | PC conectada a la red que consume recursos del servidor |

---

## 🌍 Internet y TCP/IP

> [!important] 🌍 La red de redes
>
> **Internet** no es una sola red, sino una **red de muchas redes diferentes** alrededor del mundo que se comunican usando un protocolo común: **TCP/IP** (*Transmission Control Protocol / Internet Protocol*).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/05_-_Redes_e_Internet_04.svg]]
>
> ### Componentes clave
>
> | Componente | Función |
> |---|---|
> | **TCP/IP** | Protocolo común que permite la comunicación entre redes distintas |
> | **Router (enrutador)** | Conecta diferentes redes entre sí (LAN-LAN, LAN-WAN, WAN-WAN) |
> | **Switch (conmutador)** | Conecta varios dispositivos dentro de una misma red |
> | **Conmutación de paquetes** | Los datos se dividen en paquetes que viajan por rutas distintas |
>
> > 💡 La **conmutación de paquetes** fue clave para la robustez de Internet: si una ruta falla, los paquetes simplemente toman otra ruta para llegar a su destino.

---

## 🕸️ World Wide Web — WWW (1991)

> [!important] 🕸️ Internet se vuelve accesible para todos
>
> En **1991**, **Tim Berners-Lee** creó la **World Wide Web**, un sistema de documentos interconectados mediante **hipervínculos** accesibles a través de Internet usando un navegador.
>
> La WWW no es lo mismo que Internet — es un **servicio que corre sobre Internet**, al igual que el correo electrónico o las videollamadas.
>
> | Dato | Detalle |
> |---|---|
> | **Año** | 1991 |
> | **Creador** | Tim Berners-Lee (CERN, Suiza) |
> | **Tecnologías base** | HTML, HTTP, URL |
> | **Relevancia** | Democratizó el acceso a la información global |
>
> | Concepto | Significado |
> |---|---|
> | **HTML** | Lenguaje de marcado para crear páginas web |
> | **HTTP** | Protocolo de transferencia de hipertexto |
> | **URL** | Dirección única de cada recurso en la web |
> | **Navegador** | Programa que interpreta HTML y muestra páginas web |
>
> > ⚠️ **Internet ≠ WWW** — Internet es la infraestructura de red; la WWW es uno de los servicios que usa esa infraestructura.

---

## 📅 Línea de Tiempo General

> [!summary] 📅 De ARPANET a la WWW
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/05_-_Redes_e_Internet_05.svg]]
>
> **Se lee así:** historia completa de las redes trimestre a trimestre: 1967 ARPANET, 1972 protocolos, 1973 Ethernet (Metcalfe y Boggs en Xerox PARC), 1979 estandarización DEC+Intel+Xerox, 1983 MILNET y DIX, 1989 Novell domina LAN, 1990 TCP/IP, 1991 WWW.
> **Por qué importa:** internet es la suma de redes privadas (Ethernet/LAN) unificadas por el mismo protocolo TCP/IP; no fue un diseño central sino la interconexión de miles de sistemas.
> **Ejemplo:** tu red doméstica funciona con Ethernet (o WiFi) sobre IP gracias al trabajo previo de Metcalfe; por eso tu casa habla con un servidor en el otro lado del planeta.

---

## 📊 Comparación de tipos de red

> [!summary] 📊 LAN vs WAN vs Internet
>
> | Característica | LAN | WAN | Internet |
> |---|---|---|---|
> | **Alcance** | Edificio o campus | Ciudades o países | Global |
> | **Velocidad** | Alta | Media-baja | Variable |
> | **Propietario** | Empresa u organización | Proveedor de servicios | Nadie / Todos |
> | **Protocolo típico** | Ethernet | MPLS, Frame Relay | TCP/IP |
> | **Ejemplo** | Red de una oficina | Red bancaria nacional | La Internet global |

---

## 📚 Referencias

> [!info] 📚 Referencias
>
> - Dale, Nell & Lewis, John. *Computer Science Illuminated* (6th ed.). Jones & Bartlett Learning.
> - Quinn, Michael J. *Ethics for the Information Age* (7th ed.). Pearson.
> - Syllabus oficial de Computación y Sociedad (CCPG1004), ESPOL, coordinadora Otilia M. Alejandro Molina.
**Tags:** #redes #internet #ARPANET #ethernet #LAN #WAN #TCPIP #WWW #bernerlee #unidad1 #EYAG1037
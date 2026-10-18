---
dg-publish: true
---

# 🌐 Redes e Internet

## 🎯 Introducción

> [!info] 💡 ¿Cómo se conectaron las computadoras entre sí?
>
> Durante décadas, las computadoras trabajaron de forma aislada. La necesidad de compartir información y recursos impulsó el desarrollo de las redes, que eventualmente evolucionaron hasta formar la Internet que conocemos hoy.
>
> ![[Diagramas/05_-_Redes_e_Internet_01.svg]]

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
> ![[Diagramas/05_-_Redes_e_Internet_02.svg]]

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
> ![[Diagramas/05_-_Redes_e_Internet_03.svg]]
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
> ![[Diagramas/05_-_Redes_e_Internet_04.svg]]
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
> ![[Diagramas/05_-_Redes_e_Internet_05.svg]]

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

**Tags:** #redes #internet #ARPANET #ethernet #LAN #WAN #TCPIP #WWW #bernerlee #unidad1 #EYAG1037
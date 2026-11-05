drop database if exists CRM;
create database CRM;
use CRM;

-- Crear la tabla para los productos
CREATE TABLE Producto (
    ProductoID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Descripcion TEXT,
    Precio DECIMAL(10, 2)
);

-- Crear la tabla para los contactos
CREATE TABLE Contacto (
    ContactoID INT PRIMARY KEY,
    ClienteID INT,
    Nombre VARCHAR(100),
    Cargo VARCHAR(50),
    Telefono VARCHAR(20),
    Email VARCHAR(100)
);

CREATE TABLE Cliente (
    ClienteID INT PRIMARY KEY,
    NombreEmpresa VARCHAR(100),
    Direccion VARCHAR(255),
    Telefono VARCHAR(20),
    Email VARCHAR(100)
);

-- Crear la tabla para las oportunidades de venta
CREATE TABLE Oportunidad (
    OportunidadID INT PRIMARY KEY,
    ClienteID INT,
    ContactoID INT,
    NombreOportunidad VARCHAR(100),
    Estado VARCHAR(50),
    Monto DECIMAL(10, 2),
    FechaCreacion DATE,
    EstadoVenta VARCHAR(50),
    FechaCierre DATE,
    MontoCierre DECIMAL(10, 2),
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ClienteID),
    FOREIGN KEY (ContactoID) REFERENCES Contacto(ContactoID)
);

-- Crear la tabla para los productos asociados a una oportunidad
CREATE TABLE ProductoOportunidad (
    ProductoOportunidadID INT PRIMARY KEY,
    OportunidadID INT,
    ProductoID INT,
    Cantidad INT,
    FOREIGN KEY (OportunidadID) REFERENCES Oportunidad(OportunidadID),
    FOREIGN KEY (ProductoID) REFERENCES Producto(ProductoID)
);

-- Crear la tabla para las ventas
CREATE TABLE Venta (
    VentaID INT PRIMARY KEY,
    OportunidadID INT,
    MontoVenta DECIMAL(10, 2),
    FechaVenta DATE,
    FOREIGN KEY (OportunidadID) REFERENCES Oportunidad(OportunidadID)
);

-- Crear la tabla para los usuarios del CRM
CREATE TABLE Usuario (
    UsuarioID INT PRIMARY KEY,
    NombreUsuario VARCHAR(50),
    Contrasena VARCHAR(100),
    NombreCompleto VARCHAR(100),
    Rol VARCHAR(50)
);

-- Crear la tabla para las actividades
CREATE TABLE Actividad (
    ActividadID INT PRIMARY KEY,
    UsuarioID INT,
    Tipo VARCHAR(50),
    Descripcion TEXT,
    FechaInicio DATETIME,
    FechaFin DATETIME,
    OportunidadID INT,
    FOREIGN KEY (OportunidadID) REFERENCES Oportunidad(OportunidadID),
	FOREIGN KEY (UsuarioID) REFERENCES Usuario(UsuarioID)
    
);





-- Datos para Producto
INSERT INTO Producto (ProductoID, Nombre, Descripcion, Precio) VALUES
(1, 'CRM Básico', 'Sistema CRM básico para pequeñas empresas', 29.99),
(2, 'CRM Profesional', 'CRM con funciones avanzadas', 59.99),
(3, 'CRM Enterprise', 'CRM completo para grandes empresas', 99.99),
(4, 'Módulo Marketing', 'Extensión para marketing digital', 19.99),
(5, 'Módulo Ventas', 'Gestión de ventas avanzada', 24.99),
(6, 'Módulo Soporte', 'Gestión de tickets y soporte técnico', 34.99),
(7, 'Módulo Analítica', 'Reportes y análisis de datos', 44.99);


-- Datos para Cliente
INSERT INTO Cliente (ClienteID, NombreEmpresa, Direccion, Telefono, Email) VALUES
(1, 'Alfa S.A.', 'Calle B#10-1', '0996850627', 'contacto@alfas.a..com'),
(2, 'Beta Corp.', 'Calle C#20-2', '0993782338', 'contacto@betacorp..com'),
(3, 'Gamma Ltda.', 'Calle D#30-3', '0993407886', 'contacto@gammaltda..com'),
(4, 'Delta Inc.', 'Calle E#40-4', '0998975756', 'contacto@deltainc..com'),
(5, 'Épsilon Tech', 'Calle F#50-5', '0992983329', 'contacto@épsilontech.com'),
(6, 'Zeta Group', 'Calle G#60-6', '0995020211', 'contacto@zetagroup.com'),
(7, 'Eta Solutions', 'Calle H#70-7', '0999001076', 'contacto@etasolutions.com'),
(8, 'Theta Business', 'Calle I#80-8', '0997884915', 'contacto@thetabusiness.com'),
(9, 'Iota Systems', 'Calle J#90-9', '0997908556', 'contacto@iotasystems.com'),
(10, 'Kappa Dynamics', 'Calle K#100-10', '0999760514', 'contacto@kappadynamics.com'),
(11, 'Lambda Consulting', 'Calle L#110-11', '0999232906', 'contacto@lambdaconsulting.com'),
(12, 'Mu Enterprises', 'Calle M#120-12', '0991241794', 'contacto@muenterprises.com'),
(13, 'Nu Software', 'Calle N#130-13', '0993405821', 'contacto@nusoftware.com'),
(14, 'Xi Co.', 'Calle O#140-14', '0998044283', 'contacto@xico..com'),
(15, 'Omicron Tools', 'Calle P#150-15', '0994556142', 'contacto@omicrontools.com'),
(16, 'Pi Digital', 'Calle Q#160-16', '0993472747', 'contacto@pidigital.com'),
(17, 'Rho Net', 'Calle R#170-17', '0999476370', 'contacto@rhonet.com'),
(18, 'Sigma Cloud', 'Calle S#180-18', '0992391736', 'contacto@sigmacloud.com'),
(19, 'Tau Ltd.', 'Calle T#190-19', '0999153501', 'contacto@taultd..com'),
(20, 'Upsilon Devs', 'Calle U#200-20', '0995686846', 'contacto@upsilondevs.com');


-- Datos para Contacto
INSERT INTO Contacto (ContactoID, ClienteID, Nombre, Cargo, Telefono, Email) VALUES
(1, 11, 'Persona1 Apellido1', 'Director de Marketing', '0982853589', 'persona1@lambdaconsulting.com'),
(2, 3, 'Persona2 Apellido2', 'Gerente General', '0989227505', 'persona2@gammaltda..com'),
(3, 15, 'Persona3 Apellido3', 'Director de Marketing', '0987934687', 'persona3@omicrontools.com'),
(4, 16, 'Persona4 Apellido4', 'Director de Marketing', '0989754571', 'persona4@pidigital.com'),
(5, 10, 'Persona5 Apellido5', 'Gerente de Compras', '0986766180', 'persona5@kappadynamics.com'),
(6, 15, 'Persona6 Apellido6', 'Jefe de Tecnología', '0987722828', 'persona6@omicrontools.com'),
(7, 16, 'Persona7 Apellido7', 'Jefe de Tecnología', '0983381192', 'persona7@pidigital.com'),
(8, 20, 'Persona8 Apellido8', 'Gerente de Compras', '0981652744', 'persona8@upsilondevs.com'),
(9, 9, 'Persona9 Apellido9', 'Gerente General', '0989792065', 'persona9@iotasystems.com'),
(10, 13, 'Persona10 Apellido10', 'Gerente de Compras', '0987426884', 'persona10@nusoftware.com'),
(11, 5, 'Persona11 Apellido11', 'Jefe de Tecnología', '0983965025', 'persona11@épsilontech.com'),
(12, 18, 'Persona12 Apellido12', 'Director de Marketing', '0988709919', 'persona12@sigmacloud.com'),
(13, 12, 'Persona13 Apellido13', 'Gerente General', '0982187686', 'persona13@muenterprises.com'),
(14, 17, 'Persona14 Apellido14', 'Gerente de Compras', '0988883760', 'persona14@rhonet.com'),
(15, 7, 'Persona15 Apellido15', 'Gerente General', '0985421197', 'persona15@etasolutions.com'),
(16, 18, 'Persona16 Apellido16', 'Asistente Comercial', '0985313336', 'persona16@sigmacloud.com'),
(17, 16, 'Persona17 Apellido17', 'Asistente Comercial', '0982079233', 'persona17@pidigital.com'),
(18, 11, 'Persona18 Apellido18', 'Jefe de Tecnología', '0982627443', 'persona18@lambdaconsulting.com'),
(19, 4, 'Persona19 Apellido19', 'Director de Marketing', '0989299172', 'persona19@deltainc..com'),
(20, 13, 'Persona20 Apellido20', 'Director de Marketing', '0983873151', 'persona20@nusoftware.com');


-- Datos para Oportunidad
INSERT INTO Oportunidad (OportunidadID, ClienteID, ContactoID, NombreOportunidad, Estado, Monto, FechaCreacion, EstadoVenta, FechaCierre, MontoCierre) VALUES
(1, 11, 1, 'Venta Módulo Analítica', 'Cerrada', 29.99, '2025-06-16', 'En proceso', '2025-06-26', 29.99),
(2, 3, 2, 'Venta CRM Profesional', 'Cerrada', 59.99, '2025-07-01', 'En proceso', '2025-07-15', 59.99),
(3, 15, 3, 'Venta CRM Profesional', 'Abierta', 19.99, '2025-06-15', 'Perdida', NULL, NULL),
(4, 16, 4, 'Venta CRM Básico', 'Cerrada', 19.99, '2025-06-10', 'En proceso', '2025-06-19', 19.99),
(5, 10, 5, 'Venta CRM Enterprise', 'Abierta', 44.99, '2025-06-30', 'Ganada', NULL, NULL),
(6, 15, 6, 'Venta Módulo Analítica', 'Cerrada', 24.99, '2025-06-23', 'En proceso', '2025-07-08', 24.99),
(7, 16, 7, 'Venta Módulo Analítica', 'Cerrada', 59.99, '2025-06-23', 'Ganada', '2025-07-06', 59.99),
(8, 20, 8, 'Venta Módulo Soporte', 'Cerrada', 19.99, '2025-06-11', 'En proceso', '2025-06-20', 19.99),
(9, 9, 9, 'Venta Módulo Analítica', 'Abierta', 19.99, '2025-06-05', 'En proceso', NULL, NULL),
(10, 13, 10, 'Venta Módulo Ventas', 'Abierta', 59.99, '2025-06-21', 'Ganada', NULL, NULL),
(11, 5, 11, 'Venta CRM Profesional', 'Abierta', 34.99, '2025-06-12', 'Perdida', NULL, NULL),
(12, 18, 12, 'Venta Módulo Marketing', 'Abierta', 44.99, '2025-06-15', 'Perdida', NULL, NULL),
(13, 12, 13, 'Venta Módulo Soporte', 'Abierta', 99.99, '2025-06-17', 'Perdida', NULL, NULL),
(14, 17, 14, 'Venta Módulo Marketing', 'Cerrada', 29.99, '2025-06-21', 'En proceso', '2025-06-29', 29.99),
(15, 7, 15, 'Venta Módulo Soporte', 'Cerrada', 59.99, '2025-06-11', 'Perdida', '2025-06-21', 59.99),
(16, 18, 16, 'Venta Módulo Marketing', 'Abierta', 44.99, '2025-06-25', 'En proceso', NULL, NULL),
(17, 16, 17, 'Venta CRM Profesional', 'Abierta', 99.99, '2025-06-08', 'En proceso', NULL, NULL),
(18, 11, 18, 'Venta Módulo Marketing', 'Cerrada', 29.99, '2025-06-29', 'Ganada', '2025-07-09', 29.99),
(19, 4, 19, 'Venta Módulo Analítica', 'Cerrada', 34.99, '2025-06-08', 'En proceso', '2025-06-14', 34.99),
(20, 13, 20, 'Venta Módulo Marketing', 'Abierta', 44.99, '2025-06-22', 'En proceso', NULL, NULL);

INSERT INTO Venta (VentaID, OportunidadID, FechaVenta, MontoVenta) VALUES
(1, 1,  '2025-07-02',  199.98),
(2, 2,  '2025-07-04',  59.99),
(3, 3,  '2025-07-05',  74.97),
(4, 4,  '2025-07-06',  119.96),
(5, 5,  '2025-07-07',  39.98),
(6, 6,  '2025-07-07',  34.99),
(7, 7,  '2025-07-08',  89.98),
(8, 8,  '2025-07-08',  29.99),
(9, 9,  '2025-07-09',  59.99),
(10, 10,  '2025-07-10',  199.98),
(11, 11,  '2025-07-11',  59.97),
(12, 12,  '2025-07-11',  49.98),
(13, 13,  '2025-07-12',  34.99),
(14, 14,  '2025-07-13',  89.98),
(15, 15,  '2025-07-13',  99.99),
(16, 16,  '2025-07-14',  119.98),
(17, 17,  '2025-07-14',  149.95),
(18, 18,  '2025-07-15',  69.98),
(19, 19,  '2025-07-15',  44.99),
(20, 20,  '2025-07-16',  74.97);
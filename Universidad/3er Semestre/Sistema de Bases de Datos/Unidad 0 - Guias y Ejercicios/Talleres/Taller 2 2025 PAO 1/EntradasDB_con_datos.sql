DROP DATABASE IF EXISTS sistema_tickets;
CREATE DATABASE IF NOT EXISTS sistema_tickets;
USE sistema_tickets;

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de ubicaciones (lugares donde se realizan eventos)
CREATE TABLE ubicaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    direccion TEXT NOT NULL,
    capacidad INT NOT NULL
);

-- Tabla de categorías de eventos
CREATE TABLE categorias_evento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

-- Tabla de eventos
CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATETIME NOT NULL,
    fecha_fin DATETIME NOT NULL,
    id_ubicacion INT,
    id_categoria INT,
    precio_base DECIMAL(10,2) NOT NULL,
    estado ENUM('programado', 'cancelado') DEFAULT 'programado',
    FOREIGN KEY (id_ubicacion) REFERENCES ubicaciones(id) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categorias_evento(id) ON DELETE SET NULL
);

-- Tabla de asientos por evento
CREATE TABLE asientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_evento INT,
    fila VARCHAR(10),
    numero INT,
    precio DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_evento) REFERENCES eventos(id) ON DELETE CASCADE
);

-- Tabla de pagos
CREATE TABLE pagos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    metodo_pago ENUM('Tarjeta', 'Efectivo', 'PayPal', 'Cheque' ,'Transferencia', 'Otro') NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    monto_reembolsado DECIMAL(10,2) DEFAULT 0,
    estado ENUM('pendiente', 'completado', 'fallido', 'reembolsado') DEFAULT 'pendiente',
    fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla de entradas
CREATE TABLE entradas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_evento INT,
    id_pago INT,
    id_asiento INT,
    estado ENUM('válido', 'usado', 'cancelado') DEFAULT 'válido',
    fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (id_evento) REFERENCES eventos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_pago) REFERENCES pagos(id) ON DELETE SET NULL,
    FOREIGN KEY (id_asiento) REFERENCES asientos(id) ON DELETE SET NULL
);

-- Tabla de códigos QR para validación de entradas electrónicas
CREATE TABLE codigos_qr (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_entrada INT UNIQUE,
    codigo VARCHAR(255) UNIQUE NOT NULL, -- Puede ser un hash o UUID
    fecha_generado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_entrada) REFERENCES entradas(id) ON DELETE CASCADE
);

-- Tabla de devoluciones por cancelación de eventos o entradas
CREATE TABLE devoluciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_entrada INT,
    id_pago INT,
    monto DECIMAL(10,2) NOT NULL,
    motivo TEXT NOT NULL,
    estado ENUM('pendiente', 'procesado', 'rechazado') DEFAULT 'pendiente',
    fecha_solicitud TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_entrada) REFERENCES entradas(id) ON DELETE CASCADE,
    FOREIGN KEY (id_pago) REFERENCES pagos(id) ON DELETE CASCADE
);

-- Datos de ejemplo para usuarios
INSERT INTO usuarios (nombre, email, telefono) VALUES ('Juan Pérez', 'juan@example.com', '0987654321');
INSERT INTO usuarios (nombre, email, telefono) VALUES ('María García', 'maria@example.com', '0991234567');
INSERT INTO usuarios (nombre, email, telefono) VALUES ('Carlos López', 'carlos@example.com', '0971112233');

-- Datos de ejemplo para ubicaciones
INSERT INTO ubicaciones (nombre, direccion, capacidad) VALUES ('Teatro Nacional', 'Av. Central 123', 500);
INSERT INTO ubicaciones (nombre, direccion, capacidad) VALUES ('Estadio Olímpico', 'Calle Fútbol 456', 20000);

-- Datos de ejemplo para categorías de eventos
INSERT INTO categorias_evento (nombre) VALUES ('Concierto');
INSERT INTO categorias_evento (nombre) VALUES ('Teatro');
INSERT INTO categorias_evento (nombre) VALUES ('Conferencia');

-- Datos de ejemplo para eventos
INSERT INTO eventos (nombre, descripcion, fecha_inicio, fecha_fin, id_ubicacion, id_categoria, precio_base)
        VALUES ('Rock Fest', 'Festival de rock con bandas internacionales', '2025-06-28 14:14:59', 
        '2025-06-28 17:14:59', 1, 1, 50.0);
INSERT INTO eventos (nombre, descripcion, fecha_inicio, fecha_fin, id_ubicacion, id_categoria, precio_base)
        VALUES ('Obra Clásica', 'Representación teatral de una obra clásica', '2025-06-30 14:14:59', 
        '2025-06-30 17:14:59', 1, 2, 25.0);
INSERT INTO eventos (nombre, descripcion, fecha_inicio, fecha_fin, id_ubicacion, id_categoria, precio_base)
        VALUES ('Tech Summit', 'Conferencia de tecnología y startups', '2025-07-02 14:14:59', 
        '2025-07-02 17:14:59', 2, 3, 75.0);

-- Datos de ejemplo para asientos
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (1, 'A', 1, 57.29);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (1, 'A', 2, 57.93);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (1, 'A', 3, 54.64);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (1, 'B', 1, 58.51);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (1, 'B', 2, 55.9);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (1, 'B', 3, 58.37);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (2, 'A', 1, 34.58);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (2, 'A', 2, 25.43);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (2, 'A', 3, 25.58);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (2, 'B', 1, 32.15);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (2, 'B', 2, 25.21);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (2, 'B', 3, 34.29);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (3, 'A', 1, 77.89);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (3, 'A', 2, 83.16);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (3, 'A', 3, 82.42);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (3, 'B', 1, 82.28);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (3, 'B', 2, 82.59);
INSERT INTO asientos (id_evento, fila, numero, precio) VALUES (3, 'B', 3, 77.21);

-- Datos de ejemplo para pagos
INSERT INTO pagos (id_usuario, metodo_pago, monto, estado)
        VALUES (1, 'Efectivo', 92.36, 'fallido');
INSERT INTO pagos (id_usuario, metodo_pago, monto, estado)
        VALUES (2, 'Tarjeta', 33.74, 'completado');
INSERT INTO pagos (id_usuario, metodo_pago, monto, estado)
        VALUES (3, 'PayPal', 74.55, 'fallido');
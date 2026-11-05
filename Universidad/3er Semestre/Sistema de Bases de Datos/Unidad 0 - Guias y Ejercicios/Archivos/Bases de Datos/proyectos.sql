drop database if exists proyectos;
create database if not exists proyectos;
use proyectos;

-- 1. Tabla de usuarios (supertipo)
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    tipo ENUM('responsable', 'stakeholder') NOT NULL
);

-- 2. Subtipo: responsables
CREATE TABLE responsables (
    id_usuario INT PRIMARY KEY,
    cargo VARCHAR(100),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- 3. Subtipo: stakeholders
CREATE TABLE stakeholders (
    id_usuario INT PRIMARY KEY,
    organizacion VARCHAR(100),
    tipo_interes ENUM('interno', 'externo'),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- 4. Tabla de proyectos
CREATE TABLE proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    id_responsable INT,
    FOREIGN KEY (id_responsable) REFERENCES responsables(id_usuario)
);

-- 5. Áreas del proyecto
CREATE TABLE areas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- 6. Partidas presupuestarias recursivas
CREATE TABLE partidas_presupuestarias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    monto DECIMAL(12, 2) NOT NULL,
    id_proyecto INT NOT NULL,
    id_area INT NOT NULL,
    id_padre INT DEFAULT NULL,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_area) REFERENCES areas(id),
    FOREIGN KEY (id_padre) REFERENCES partidas_presupuestarias(id)
);

-- 7. Actividades del proyecto
CREATE TABLE actividades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    porcentaje_avance DECIMAL(5,2) DEFAULT 0.0,
    id_proyecto INT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id) ON DELETE CASCADE
);

-- 8. Relación de stakeholders y proyectos
CREATE TABLE proyecto_stakeholders (
    id_proyecto INT,
    id_stakeholder INT,
    rol VARCHAR(100),
    PRIMARY KEY (id_proyecto, id_stakeholder),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_stakeholder) REFERENCES stakeholders(id_usuario) ON DELETE CASCADE
);

-- Usuarios (1 responsable y 2 stakeholders)
INSERT INTO usuarios (nombre, correo, tipo) VALUES
('Juan Pérez', 'juan@ejemplo.com', 'responsable'),
('Ana Torres', 'ana@ong.org', 'stakeholder'),
('Carlos Vega', 'carlos@empresa.com', 'stakeholder');

-- Subtipos
INSERT INTO responsables (id_usuario, cargo) VALUES (1, 'Gerente de Proyecto');
INSERT INTO stakeholders (id_usuario, organizacion, tipo_interes)
VALUES
(2, 'ONG Ambiental', 'externo'),
(3, 'Empresa Consultora XYZ', 'interno');

-- Proyecto
INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin, id_responsable)
VALUES ('Planta de reciclaje urbana', 'Proyecto piloto para reciclaje en Quito', '2025-07-01', '2025-12-31', 1);

-- Áreas
INSERT INTO areas (nombre, descripcion) VALUES
('Infraestructura', 'Construcción y equipamiento'),
('Gestión', 'Dirección, supervisión y administración');

-- Partidas presupuestarias (recursivas)
INSERT INTO partidas_presupuestarias (nombre, monto, id_proyecto, id_area, id_padre)
VALUES
('Obras Civiles', 100000.00, 1, 1, NULL),   -- Nivel 1
('Cimentación', 30000.00, 1, 1, 1),        -- Nivel 2
('Estructura', 70000.00, 1, 1, 1),         -- Nivel 2
('Administración del Proyecto', 20000.00, 1, 2, NULL),
('Supervisión', 10000.00, 1, 2, 4);         -- Subpartida de administración

-- Actividades del proyecto
INSERT INTO actividades (nombre, descripcion, fecha_inicio, fecha_fin, porcentaje_avance, id_proyecto)
VALUES
('Estudios preliminares', 'Levantamiento topográfico y permisos', '2025-07-01', '2025-07-15', 100.00, 1),
('Construcción de cimentación', 'Excavación y armado de bases', '2025-07-16', '2025-08-10', 50.00, 1),
('Montaje de estructura metálica', 'Armado de la nave principal', '2025-08-11', '2025-09-15', 0.00, 1);

-- Relación de stakeholders con proyecto
INSERT INTO proyecto_stakeholders (id_proyecto, id_stakeholder, rol) VALUES
(1, 2, 'Financista'),
(1, 3, 'Consultor Técnico');
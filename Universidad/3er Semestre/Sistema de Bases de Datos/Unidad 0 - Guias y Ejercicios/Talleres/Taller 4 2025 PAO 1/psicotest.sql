-- ===========================================
-- Script MySQL: Sistema de Test Psicológicos
-- ===========================================

-- Crear base de datos
DROP DATABASE IF EXISTS psicotest;
CREATE DATABASE psicotest;
USE psicotest;

-- ===========================================
-- TABLAS (DDL)
-- ===========================================

-- Tabla: Paciente
CREATE TABLE Paciente (
    id_paciente INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    genero ENUM('M','F','Otro') NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: Patologia
CREATE TABLE Patologia (
    id_patologia INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla: Test
CREATE TABLE Test (
    id_test INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_patologia INT,
    FOREIGN KEY (id_patologia) REFERENCES Patologia(id_patologia)
);

-- Tabla: PreguntasTest
CREATE TABLE PreguntasTest (
    id_pregunta INT AUTO_INCREMENT PRIMARY KEY,
    id_test INT NOT NULL,
    texto_pregunta TEXT NOT NULL,
    tipo ENUM('opcion_multiple','verdadero_falso','escala') NOT NULL,
    FOREIGN KEY (id_test) REFERENCES Test(id_test) ON DELETE CASCADE
);

-- Tabla: PosiblesRespuesta
CREATE TABLE PosiblesRespuesta (
    id_respuesta INT AUTO_INCREMENT PRIMARY KEY,
    id_pregunta INT NOT NULL,
    texto_respuesta VARCHAR(255) NOT NULL,
    valor INT NOT NULL,
    FOREIGN KEY (id_pregunta) REFERENCES PreguntasTest(id_pregunta) ON DELETE CASCADE
);

-- Tabla: Resultados
CREATE TABLE Resultados (
    id_resultado INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT NOT NULL,
    id_test INT NOT NULL,
    fecha_realizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    puntaje_total INT,
    interpretacion TEXT,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_test) REFERENCES Test(id_test)
);

-- Tabla: RespuestasPaciente
CREATE TABLE RespuestasPaciente (
    id_respuesta_paciente INT AUTO_INCREMENT PRIMARY KEY,
    id_resultado INT NOT NULL,
    id_pregunta INT NOT NULL,
    id_respuesta INT NOT NULL,
    FOREIGN KEY (id_resultado) REFERENCES Resultados(id_resultado) ON DELETE CASCADE,
    FOREIGN KEY (id_pregunta) REFERENCES PreguntasTest(id_pregunta),
    FOREIGN KEY (id_respuesta) REFERENCES PosiblesRespuesta(id_respuesta)
);

-- ===========================================
-- DATOS (DML)
-- ===========================================

-- 5 Pacientes
INSERT INTO Paciente (nombres, apellidos, fecha_nacimiento, genero, email, telefono)
VALUES 
('Carlos', 'Pérez', '1990-05-12', 'M', 'carlos@example.com', '099111222'),
('Ana', 'Lopez', '1985-09-21', 'F', 'ana@example.com', '099333444'),
('Jorge', 'Mendoza', '2000-01-10', 'M', 'jorge@example.com', '098555666'),
('Lucía', 'Castro', '1995-03-25', 'F', 'lucia@example.com', '097777888'),
('Pedro', 'Suarez', '1978-11-02', 'M', 'pedro@example.com', '096999000');
-- Nota: Pedro no tendrá ningún test asociado

-- 5 Patologías
INSERT INTO Patologia (nombre, descripcion)
VALUES
('Ansiedad', 'Trastorno relacionado con niveles altos de ansiedad'),
('Depresión', 'Trastorno del estado de ánimo caracterizado por tristeza persistente'),
('Estrés', 'Respuesta física y emocional a demandas externas'),
('Déficit de atención', 'Trastorno neuropsicológico con dificultades de concentración'),
('Insomnio', 'Trastorno del sueño caracterizado por dificultad para dormir');

-- 5 Tests
INSERT INTO Test (nombre, descripcion, id_patologia)
VALUES
('Test de Ansiedad Generalizada', 'Cuestionario para medir niveles de ansiedad', 1),
('Inventario de Depresión', 'Cuestionario para evaluar síntomas depresivos', 2),
('Escala de Estrés Percebido', 'Cuestionario para evaluar el nivel de estrés', 3),
('Test de Atención', 'Evaluación de problemas de concentración', 4),
('Test de Sueño', 'Cuestionario para evaluar patrones de sueño', 5);

-- 5 Preguntas
INSERT INTO PreguntasTest (id_test, texto_pregunta, tipo)
VALUES
(1, 'Me siento nervioso o tenso con frecuencia.', 'opcion_multiple'),
(1, 'Tengo dificultad para controlar mis preocupaciones.', 'opcion_multiple'),
(2, 'He perdido interés en actividades que solía disfrutar.', 'opcion_multiple'),
(3, 'En el último mes, ¿con qué frecuencia se ha sentido estresado?', 'opcion_multiple'),
(5, '¿Tiene dificultades para conciliar el sueño?', 'verdadero_falso');

-- 5 Posibles Respuestas
INSERT INTO PosiblesRespuesta (id_pregunta, texto_respuesta, valor)
VALUES
(1, 'Nunca', 0),
(1, 'A veces', 1),
(1, 'Frecuentemente', 2),
(2, 'Casi nunca', 0),
(2, 'Casi siempre', 2);

-- 5 Resultados
INSERT INTO Resultados (id_paciente, id_test, puntaje_total, interpretacion)
VALUES
(1, 1, 5, 'Ansiedad leve'),
(1, 2, 12, 'Depresión moderada'),
(2, 1, 8, 'Ansiedad moderada'),
(3, 3, 6, 'Estrés alto'),
(4, 5, 2, 'Insomnio leve');
-- Nota: Paciente 5 (Pedro) queda sin ningún test

-- 5 RespuestasPaciente
INSERT INTO RespuestasPaciente (id_resultado, id_pregunta, id_respuesta)
VALUES
(1, 1, 2), -- Carlos contestó "A veces"
(1, 2, 5), -- Carlos contestó "Casi siempre"
(2, 3, 1), -- Carlos en Depresión: respuesta "Nunca"
(3, 1, 3), -- Ana contestó "Frecuentemente"
(4, 4, 2); -- Jorge contestó "A veces"
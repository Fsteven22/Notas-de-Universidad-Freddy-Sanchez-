-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-06-2016 a las 16:00:39
-- Versión del servidor: 10.1.9-MariaDB
-- Versión de PHP: 5.6.15

drop database if exists supermercado;
create database supermercado;
use supermercado;


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `supermercado`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `ventas_cajero` (IN `mes` VARCHAR(50))  begin
	SELECT count(*) AS cantidad, nombre
	FROM venta, cajero 
	WHERE venta.id_cajero = cajero.id_cajero
	      AND fecha LIKE "2016-01-10"
	      GROUP BY nombre;
end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ventas_mes` (IN `mes` VARCHAR(50))  begin
	SELECT count(*) FROM venta, sucursal
	WHERE venta.id_sucursal = sucursal.id_sucursal
		  AND sucursal.id_sucursal = 1
		  AND fecha LIKE CONCAT('%',mes,'%');
end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ventas_producto` (IN `mes` VARCHAR(50))  begin
	SELECT count(*) AS cantidad, fecha
	FROM venta, sucursal, producto
	WHERE venta.id_sucursal = sucursal.id_sucursal AND
	      sucursal.id_sucursal = producto.id_sucursal AND
	      producto.nombre LIKE "Galletas"
	      GROUP BY fecha;
end$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caja`
--

CREATE TABLE `caja` (
  `id_caja` int(11) NOT NULL,
  `tipo_caja` varchar(50) NOT NULL,
  `id_cajero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `caja`
--

INSERT INTO `caja` (`id_caja`, `tipo_caja`, `id_cajero`) VALUES
(1, 'Normal', 1),
(2, 'Rápida', 2),
(3, 'Normal', 3),
(4, 'Rápida', 4),
(5, 'Normal', 5),
(6, 'Rápida', 6),
(7, 'Normal', 7),
(8, 'Rápida', 8),
(9, 'Normal', 9),
(10, 'Rápida', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cajero`
--

CREATE TABLE `cajero` (
  `id_cajero` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `genero` char(1) NOT NULL,
  `edad` int(3) NOT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `pass` varchar(50) DEFAULT NULL,
  `permiso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cajero`
--

INSERT INTO `cajero` (`id_cajero`, `nombre`, `genero`, `edad`, `correo`, `pass`, `permiso`) VALUES
(1, 'Erika Rubio', 'F', 27, 'Erika@correo.com', '123', 1),
(2, 'Francisco García', 'M', 20, 'Francisco@correo.com', 'abc', 2),
(3, 'Mauricio Saavedra', 'M', 21, 'Mauricio@correo.com', 'xyz', 3),
(4, 'Nadia Delgado', 'F', 25, 'Nadia@correo.com', '135', 4),
(5, 'Dulce Sandoval', 'F', 21, 'Dulce@correo.com', 'jkl', 4),
(6, 'Sergio Mercado', 'M', 30, 'Sergio@correo.com', '123', 4),
(7, 'Viridiana Soto', 'F', 42, 'Viridiana@correo.com', 'abc', 4),
(8, 'Víctor Domínguez', 'M', 24, 'siemprechiva@correo.com', 'xyz', 4),
(9, 'Gabriel Campoy', 'M', 23, 'campsayit@correo.com', 'juansolo', 4),
(10, 'Karolina Herrera', 'F', 20, 'Karolina@correo.com', 'elcamino', 4),
(14, 'María Rosas', 'F', 31, 'Maria@correo.com', 'rosas', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `delegacion`
--

CREATE TABLE `delegacion` (
  `id_delegacion` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `id_estado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `delegacion`
--

INSERT INTO `delegacion` (`id_delegacion`, `nombre`, `id_estado`) VALUES
(1, 'Coyoacán', 1),
(2, 'Cuajimalpa', 1),
(3, 'Álvaro Obregón', 1),
(4, 'Benito Juarez', 1),
(5, 'Iztacalco', 1),
(6, 'Iztapalapa', 1),
(7, 'Xochimilco', 1),
(8, 'Tlalpan', 1),
(9, 'Cuauhtémoc', 1),
(10, 'Venustiano Carranza', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `descuento`
--

CREATE TABLE `descuento` (
  `id_descuento` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_limite` date NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `descuento`
--

INSERT INTO `descuento` (`id_descuento`, `nombre`, `fecha_inicio`, `fecha_limite`, `descripcion`) VALUES
(1, 'Rebaja Galletas', '2016-01-10', '2016-02-10', 'Rebaja del 10%'),
(2, 'Rebaja Papas Fritas', '2016-01-10', '2016-02-10', 'Rebaja del 5%'),
(3, 'Rebaja Lavadora', '2016-03-10', '2016-06-10', 'Rebaja del 5%'),
(4, 'Rebaja Estufa', '2016-01-10', '2016-06-10', 'Rebaja del 7%'),
(5, 'Rebaja Audífonos', '2016-02-10', '2016-04-10', 'Rebaja del 15%'),
(6, 'Rebaja Videojuego', '2016-02-10', '2016-04-10', 'Rebaja del 20%'),
(7, 'Rebaja Escoba', '2016-01-10', '2016-03-10', 'Rebaja del 10%'),
(8, 'Rebaja Cloro', '2016-01-10', '2016-03-10', 'Rebaja del 10%'),
(9, 'Rebaja Sofá', '2016-03-10', '2016-03-20', 'Rebaja del 25%'),
(10, 'Rebaja Mesa', '2016-03-05', '2016-03-30', 'Rebaja del 35%');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleventa`
--

CREATE TABLE `detalleventa` (
  `id_venta` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `id_descuento` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `detalleventa`
--

INSERT INTO `detalleventa` (`id_venta`, `id_producto`, `id_descuento`, `cantidad`, `precio`) VALUES
(1, 1, 1, 7, 100),
(2, 1, 1, 4, 100),
(3, 2, 2, 2, 100),
(4, 2, 2, 5, 100),
(5, 3, 3, 2, 100),
(6, 3, 3, 8, 100),
(7, 4, 4, 3, 100),
(8, 4, 4, 5, 100),
(9, 5, 5, 9, 100),
(10, 5, 5, 1, 100),
(11, 5, 5, 5, 100),
(12, 6, 6, 2, 100),
(13, 6, 6, 1, 100),
(14, 6, 6, 2, 100),
(15, 7, 7, 1, 100),
(16, 7, 7, 5, 100),
(17, 7, 7, 2, 100),
(18, 7, 7, 8, 100),
(19, 8, 8, 3, 100),
(20, 8, 8, 1, 100),
(21, 8, 8, 2, 100),
(22, 8, 8, 7, 100),
(23, 9, 9, 3, 100),
(24, 9, 9, 2, 100),
(25, 9, 9, 1, 100),
(26, 9, 9, 2, 100),
(27, 9, 9, 4, 100),
(28, 10, 10, 5, 100),
(29, 10, 10, 6, 100),
(30, 10, 10, 2, 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id_estado` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`id_estado`, `nombre`) VALUES
(1, 'Ciudad de México'),
(2, 'Veracruz'),
(3, 'Jalisco'),
(4, 'Durango'),
(5, 'Chihuaha'),
(6, 'Oaxaca'),
(7, 'Yucatán'),
(8, 'Campeche'),
(9, 'Nuevo León'),
(10, 'Colima');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `linea` varchar(50) NOT NULL,
  `id_sucursal` int(11) DEFAULT NULL,
  `precio` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `nombre`, `linea`, `id_sucursal`, `precio`) VALUES
(1, 'Galletas', 'Alimentos', 1, 10.5),
(2, 'Papas Fritas', 'Alimentos', 1, 8.5),
(3, 'Lavadora', 'Electrodomésticos', 1, 8499),
(4, 'Estufa', 'Electrodomésticos', 1, 7499),
(5, 'Audífonos', 'Electrónica', 1, 299),
(6, 'Videojuego', 'Electrónica', 1, 799),
(7, 'Escoba', 'Limpieza', 1, 80),
(8, 'Cloro', 'Limpieza', 1, 43.6),
(9, 'Sofá', 'Muebles', 1, 1299),
(10, 'Mesa', 'Muebles', 1, 1150),
(11, 'Chamarra', 'Ropa', 10, 199.5),
(12, 'Camisa', 'Ropa', 10, 80);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sucursal`
--

CREATE TABLE `sucursal` (
  `id_sucursal` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(300) NOT NULL,
  `id_delegacion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sucursal`
--

INSERT INTO `sucursal` (`id_sucursal`, `nombre`, `direccion`, `id_delegacion`) VALUES
(1, 'Sucursal Coyoacán', 'Av. Coyoacán 2000 Xoco 03330 Ciudad de México', 1),
(2, 'Sucursal Cuajimalpa', 'Av Vasco de Quiroga 4871 Cuajimalpa de Morelos Santa Fe Cuajimalpa 05348 Ciudad de México', 2),
(3, 'Sucursal Álvaro Obregón', 'Av. Insurgentes Sur No. 263 Álvaro Obregón Col. Roma 06700 Ciudad de México', 3),
(4, 'Sucursal Benito Juarez', 'Avenida Municipio Libre entre Callejón Ixcateopan y Prolongación Xochicalco.\nColonia Santa Cruz Atoyac.', 4),
(5, 'Sucursal Iztacalco', 'Av. Francisco del Paso y Troncoso 1134 Iztacalco INFONAVIT Iztacalco 89000 Ciudad de México', 5),
(6, 'Sucursal Iztapalapa', 'Calle 6 Granjas San Antonio Iztapalapa 09070 Ciudad de México', 6),
(7, 'Sucursal Xochimilco', 'Primer Callejón Xochimilco Rosales San Lorenzo Ciudad de México', 7),
(8, 'Sucursal Tlalpan', 'Calz. de Tlalpan 906 Tlalpan Nativitas 03500 Ciudad de México', 8),
(9, 'Sucursal Cuauhtémoc', 'Av. Hidalgo 45 Centro Histórico Guerrero 06300 Ciudad de México', 9),
(10, 'Sucursal Venustiano Carranza', 'Av Capitan Carlos León S/N Peñón de los Baños Venustiano Carranza 15620 Ciudad de México', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipopago`
--

CREATE TABLE `tipopago` (
  `id_pago` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipopago`
--

INSERT INTO `tipopago` (`id_pago`, `nombre`) VALUES
(1, 'Efectivo'),
(2, 'Débito'),
(3, 'Crédito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipopago_venta`
--

CREATE TABLE `tipopago_venta` (
  `id_pago` int(11) NOT NULL,
  `id_venta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipopago_venta`
--

INSERT INTO `tipopago_venta` (`id_pago`, `id_venta`) VALUES
(1, 1),
(1, 2),
(1, 7),
(1, 8),
(1, 13),
(1, 14),
(1, 19),
(1, 22),
(1, 25),
(1, 28),
(2, 3),
(2, 4),
(2, 9),
(2, 10),
(2, 15),
(2, 16),
(2, 20),
(2, 23),
(2, 26),
(2, 29),
(3, 5),
(3, 6),
(3, 11),
(3, 12),
(3, 17),
(3, 18),
(3, 21),
(3, 24),
(3, 27),
(3, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id_venta` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `id_sucursal` int(11) DEFAULT NULL,
  `id_cajero` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`id_venta`, `fecha`, `id_sucursal`, `id_cajero`) VALUES
(1, '2016-01-10', 1, 1),
(2, '2016-02-10', 1, 1),
(3, '2016-02-10', 1, 1),
(4, '2016-03-10', 1, 1),
(5, '2016-02-10', 1, 2),
(6, '2016-02-10', 1, 2),
(7, '2016-02-10', 1, 2),
(8, '2016-02-10', 1, 2),
(9, '2016-01-10', 1, 3),
(10, '2016-01-10', 1, 3),
(11, '2016-01-10', 1, 3),
(12, '2016-04-10', 1, 3),
(13, '2016-01-10', 1, 4),
(14, '2016-02-10', 1, 4),
(15, '2016-03-10', 1, 4),
(16, '2016-01-10', 1, 5),
(17, '2016-01-10', 1, 5),
(18, '2016-01-10', 1, 5),
(19, '2016-01-10', 1, 6),
(20, '2016-02-10', 1, 6),
(21, '2016-01-10', 1, 6),
(22, '2016-03-10', 1, 7),
(23, '2016-04-10', 1, 7),
(24, '2016-04-10', 1, 8),
(25, '2016-05-10', 1, 8),
(26, '2016-05-10', 1, 9),
(27, '2016-05-10', 1, 9),
(28, '2016-03-10', 1, 10),
(29, '2016-04-10', 1, 10),
(30, '2016-03-10', 1, 10);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `caja`
--
ALTER TABLE `caja`
  ADD PRIMARY KEY (`id_caja`),
  ADD KEY `id_cajero` (`id_cajero`);

--
-- Indices de la tabla `cajero`
--
ALTER TABLE `cajero`
  ADD PRIMARY KEY (`id_cajero`);

--
-- Indices de la tabla `delegacion`
--
ALTER TABLE `delegacion`
  ADD PRIMARY KEY (`id_delegacion`),
  ADD KEY `id_estado` (`id_estado`);

--
-- Indices de la tabla `descuento`
--
ALTER TABLE `descuento`
  ADD PRIMARY KEY (`id_descuento`);

--
-- Indices de la tabla `detalleventa`
--
ALTER TABLE `detalleventa`
  ADD PRIMARY KEY (`id_venta`,`id_producto`),
  ADD KEY `id_producto` (`id_producto`),
  ADD KEY `id_descuento` (`id_descuento`);

--
-- Indices de la tabla `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `id_sucursal` (`id_sucursal`);

--
-- Indices de la tabla `sucursal`
--
ALTER TABLE `sucursal`
  ADD PRIMARY KEY (`id_sucursal`),
  ADD KEY `id_delegacion` (`id_delegacion`);

--
-- Indices de la tabla `tipopago`
--
ALTER TABLE `tipopago`
  ADD PRIMARY KEY (`id_pago`);

--
-- Indices de la tabla `tipopago_venta`
--
ALTER TABLE `tipopago_venta`
  ADD PRIMARY KEY (`id_pago`,`id_venta`),
  ADD KEY `id_venta` (`id_venta`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id_venta`),
  ADD KEY `id_sucursal` (`id_sucursal`),
  ADD KEY `id_cajero` (`id_cajero`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cajero`
--
ALTER TABLE `cajero`
  MODIFY `id_cajero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT de la tabla `sucursal`
--
ALTER TABLE `sucursal`
  MODIFY `id_sucursal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `caja`
--
ALTER TABLE `caja`
  ADD CONSTRAINT `caja_ibfk_1` FOREIGN KEY (`id_cajero`) REFERENCES `cajero` (`id_cajero`);

--
-- Filtros para la tabla `delegacion`
--
ALTER TABLE `delegacion`
  ADD CONSTRAINT `delegacion_ibfk_1` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`);

--
-- Filtros para la tabla `detalleventa`
--
ALTER TABLE `detalleventa`
  ADD CONSTRAINT `detalleventa_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`),
  ADD CONSTRAINT `detalleventa_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  ADD CONSTRAINT `detalleventa_ibfk_3` FOREIGN KEY (`id_descuento`) REFERENCES `descuento` (`id_descuento`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`id_sucursal`) REFERENCES `sucursal` (`id_sucursal`);

--
-- Filtros para la tabla `sucursal`
--
ALTER TABLE `sucursal`
  ADD CONSTRAINT `sucursal_ibfk_1` FOREIGN KEY (`id_delegacion`) REFERENCES `delegacion` (`id_delegacion`);

--
-- Filtros para la tabla `tipopago_venta`
--
ALTER TABLE `tipopago_venta`
  ADD CONSTRAINT `tipopago_venta_ibfk_1` FOREIGN KEY (`id_pago`) REFERENCES `tipopago` (`id_pago`),
  ADD CONSTRAINT `tipopago_venta_ibfk_2` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`);

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`id_sucursal`) REFERENCES `sucursal` (`id_sucursal`),
  ADD CONSTRAINT `venta_ibfk_2` FOREIGN KEY (`id_cajero`) REFERENCES `cajero` (`id_cajero`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
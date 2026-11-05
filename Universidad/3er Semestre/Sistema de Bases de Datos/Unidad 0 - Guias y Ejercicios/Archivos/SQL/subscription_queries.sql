-- ========================================
-- CONSULTAS SQL - SISTEMA DE SUSCRIPCIONES
-- ========================================

-- a) Calcular el ingreso total generado por plan
-- Mostrar el nombre del plan, el total generado en dólares y el número de suscripciones activas del mismo

SELECT 
    p.nombre AS nombre_plan,
    SUM(pg.monto) AS total_generado_dolares,
    COUNT(DISTINCT s.id_suscripcion) AS suscripciones_activas
FROM planes p
INNER JOIN suscripcion s ON p.id_plan = s.id_plan
INNER JOIN pagos pg ON s.id_suscripcion = pg.id_suscripcion
WHERE s.situacion = 'activa'  -- Solo suscripciones activas
GROUP BY p.id_plan, p.nombre
ORDER BY total_generado_dolares DESC;

-- b) Identificar usuarios con múltiples suscripciones activas
-- Mostrar nombre, apellido y número de suscripciones activas

SELECT 
    u.nombre,
    u.apellido,
    COUNT(s.id_suscripcion) AS numero_suscripciones_activas
FROM usuario u
INNER JOIN suscripcion s ON u.id_usuario = s.id_usuario
WHERE s.situacion = 'activa'
GROUP BY u.id_usuario, u.nombre, u.apellido
HAVING COUNT(s.id_suscripcion) > 1
ORDER BY numero_suscripciones_activas DESC;

-- c) Mostrar el plan más popular (con más suscripciones activas)

SELECT 
    p.nombre AS plan_mas_popular,
    COUNT(s.id_suscripcion) AS total_suscripciones_activas
FROM planes p
INNER JOIN suscripcion s ON p.id_plan = s.id_plan
WHERE s.situacion = 'activa'
GROUP BY p.id_plan, p.nombre
ORDER BY total_suscripciones_activas DESC
LIMIT 1;

-- d) Listar usuarios que nunca han realizado un pago

SELECT 
    u.id_usuario,
    u.nombre,
    u.apellido,
    u.fecha_registro
FROM usuario u
LEFT JOIN suscripcion s ON u.id_usuario = s.id_usuario
LEFT JOIN pagos pg ON s.id_suscripcion = pg.id_suscripcion
WHERE pg.id_pago IS NULL
ORDER BY u.fecha_registro DESC;

-- e) Calcular el ingreso promedio por usuario activo

SELECT 
    ROUND(AVG(ingreso_por_usuario), 2) AS ingreso_promedio_por_usuario
FROM (
    SELECT 
        u.id_usuario,
        SUM(pg.monto) AS ingreso_por_usuario
    FROM usuario u
    INNER JOIN suscripcion s ON u.id_usuario = s.id_usuario
    INNER JOIN pagos pg ON s.id_suscripcion = pg.id_suscripcion
    WHERE s.situacion = 'activa'
    GROUP BY u.id_usuario
) AS ingresos_usuarios;

-- f) Mostrar promociones activas y cuántas suscripciones las están usando

SELECT 
    pr.nombre_promocion,
    pr.descuento,
    pr.fecha_inicio,
    pr.fecha_fin,
    COUNT(s.id_suscripcion) AS suscripciones_con_promocion
FROM promociones pr
LEFT JOIN suscripcion s ON pr.id_promocion = s.id_promocion 
    AND s.situacion = 'activa'
WHERE pr.fecha_fin >= CURDATE()  -- Promociones vigentes
GROUP BY pr.id_promocion, pr.nombre_promocion, pr.descuento, pr.fecha_inicio, pr.fecha_fin
ORDER BY suscripciones_con_promocion DESC;

-- g) Listar pagos pendientes con información del usuario y plan

SELECT 
    u.nombre,
    u.apellido,
    p.nombre AS nombre_plan,
    pg.monto,
    pg.fecha_pago,
    pg.metodo_pago,
    s.fecha_inicio AS inicio_suscripcion
FROM pagos pg
INNER JOIN suscripcion s ON pg.id_suscripcion = s.id_suscripcion
INNER JOIN usuario u ON s.id_usuario = u.id_usuario
INNER JOIN planes p ON s.id_plan = p.id_plan
WHERE pg.estado = 'pendiente'
ORDER BY pg.fecha_pago ASC;

-- h) Encontrar usuarios cuyas suscripciones vencen en los próximos 30 días

SELECT 
    u.nombre,
    u.apellido,
    p.nombre AS nombre_plan,
    s.fecha_fin,
    DATEDIFF(s.fecha_fin, CURDATE()) AS dias_hasta_vencimiento
FROM usuario u
INNER JOIN suscripcion s ON u.id_usuario = s.id_usuario
INNER JOIN planes p ON s.id_plan = p.id_plan
WHERE s.situacion = 'activa'
    AND s.fecha_fin BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY)
ORDER BY s.fecha_fin ASC;

-- i) Resumen financiero por mes del año actual

SELECT 
    YEAR(pg.fecha_pago) AS año,
    MONTH(pg.fecha_pago) AS mes,
    MONTHNAME(pg.fecha_pago) AS nombre_mes,
    COUNT(pg.id_pago) AS total_pagos,
    SUM(pg.monto) AS ingreso_total,
    ROUND(AVG(pg.monto), 2) AS pago_promedio
FROM pagos pg
WHERE YEAR(pg.fecha_pago) = YEAR(CURDATE())
    AND pg.estado = 'completado'
GROUP BY YEAR(pg.fecha_pago), MONTH(pg.fecha_pago), MONTHNAME(pg.fecha_pago)
ORDER BY año DESC, mes DESC;

-- j) Top 5 usuarios que más han gastado

SELECT 
    u.nombre,
    u.apellido,
    COUNT(pg.id_pago) AS total_pagos,
    SUM(pg.monto) AS total_gastado,
    ROUND(AVG(pg.monto), 2) AS pago_promedio
FROM usuario u
INNER JOIN suscripcion s ON u.id_usuario = s.id_usuario
INNER JOIN pagos pg ON s.id_suscripcion = pg.id_suscripcion
WHERE pg.estado = 'completado'
GROUP BY u.id_usuario, u.nombre, u.apellido
ORDER BY total_gastado DESC
LIMIT 5;
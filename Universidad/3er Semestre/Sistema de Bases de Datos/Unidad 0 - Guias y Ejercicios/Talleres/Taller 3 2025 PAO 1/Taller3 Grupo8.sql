use supermercado;

-- Normalizacion de la tabla producto
create table if not exists linea(
	id_linea int primary key auto_increment,
    id_producto int,
    linea varchar(50),
    constraint fk_producto foreign key (id_producto) references producto(id_producto)  
);

insert into linea(id_producto,linea) values 
(1, "Alimentos"),
(2, "Alimentos"),
(3, "Electrodomésticos"),
(4, "Electrodomésticos"),
(5, "Electrónica"),
(6, "Electrónica"),
(7, "Limpieza"),
(8, "Limpieza"),
(9, "Muebles"),
(10, "Mesa"),
(11, "Chamarra"),
(12, "Camisa");

alter table producto drop column linea;

-- Insercion de datos para nueva sucursal
insert into venta values
(31,now(),2,2),
(32,now(),2,2);

insert into detalleventa values
(31,1,9,5,76),
(32,2,9,10,100);

-- Promedio de ventas por sucursal (no considerar descuentos): Presentar nombre de sucursal y promedio
select s.nombre, avg(d.precio * d.cantidad) as promedio
from sucursal s
inner join venta v using (id_sucursal)
inner join detalleventa d using (id_venta)
group by s.id_sucursal;

-- Presentar el producto que más se vende en cada sucursal, usar el campo
-- cantidad de la tabla detalleventa.
create view vProductoMasVendido as
select s.nombre as nombre_sucursal, p.nombre as nombre_producto, sum(dv.cantidad) as CantidadVendida
from sucursal s
inner join venta v on s.id_sucursal = v.id_sucursal
inner join detalleventa dv on v.id_venta = dv.id_venta
inner join producto p on dv.id_producto = p.id_producto
group by s.id_sucursal, s.nombre, p.id_producto, p.nombre
having sum(dv.cantidad) = (select max(sub.total) from (
            select p2.id_producto,sum(dv2.cantidad) as total
            from venta v2
			inner join detalleventa dv2 on v2.id_venta = dv2.id_venta
			inner join producto p2 on dv2.id_producto = p2.id_producto
            where v2.id_sucursal = s.id_sucursal
            group by p2.id_producto
        ) as sub
    );

drop view vProductoMasVendido;

select * from vProductoMasVendido;

-- Crear un procedimiento sPCrearVenta, este procedimiento recibe los parámetros
-- necesarios para crear una venta
delimiter $$
create procedure sPCrearVenta (
    in p_id_producto int,
    in p_id_pago int,
    in p_id_cajero int,
    in p_id_sucursal int,
    in p_cantidad int
)
begin
    declare nuevo_id int;
    declare precio_producto double;
    declare exit handler for sqlexception
    begin
        rollback;
    end;
    start transaction;
    select ifnull(MAX(venta), 0) + 1 into nuevo_id from venta;
    
    insert into venta (venta, fecha, id_sucursal, id_cajero)
    values (nuevo_id, CURDATE(), p_id_sucursal, p_id_cajero);
    
    select precio into precio_producto
    from producto
    where id_producto = p_id_producto;
    insert into detalleventa (id_venta, id_producto, id_descuento, cantidad, precio)
    values (nuevo_id, p_id_producto, 0, p_cantidad, precio_producto);
    
    insert into tipopago_venta (id_pago, id_venta)
    values (p_id_pago, nuevo_id);
    commit;
END $$
 
call sPCrearVenta(2,2,4,3,6);

drop procedure sPCrearVenta;

-- Crear un disparador tgrEncriptarPass para que automáticamente encripte el campo
-- pass en la tabla cajero.
delimiter %%
create trigger tgrEncriptarPass before insert on cajero
for each row
begin
set new.pass = MD5(new.pass);
end;
%%

-- Actualizacion de datos
SET SQL_SAFE_UPDATES = 0;
update cajero
set pass= MD5(pass);

-- Prueba del trigger
insert into cajero values
(15,"Felix Lucas","M",19,"feliluca@espol.edu.ec","abc",2);

select * from cajero;
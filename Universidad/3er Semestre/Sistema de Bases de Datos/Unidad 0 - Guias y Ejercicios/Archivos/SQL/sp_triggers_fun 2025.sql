-- create view nombre [columnas]
-- as .... select 


-- create view peliculas_disponibles as 
-- select inventory_id, title, replacement_cost, store_id
-- from inventory i 
-- inner join film using (film_id)
-- where inventory_id not in ( -- no estan rentadas
-- 	select inventory_id
-- 	from rental
-- 	where return_date is null -- estan rentadas
-- )

-- # in, out, inout
use sakila;
-- drop procedure if exists spVerPagos;
-- delimiter $
-- create procedure spVerPagos(in clienteId int, out resultado decimal(10,2))
-- begin
-- 	select * from payment where customer_id = clienteId;
--     -- set resultado = 10;
--     select sum(amount) into resultado from payment where customer_id = clienteId;
-- end;
-- $
-- delimiter ;

-- drop procedure spVerPagos;


-- call spVerPagos(5, @total);
-- select @total;

-- drop procedure if exists spTopClientes;
-- delimiter %%
-- create procedure spTopClientes(in limite smallint)
-- begin
-- 	drop table if exists tmpTotalClientes;
--     create table tmpTotalClientes as 
--     select customer_id, first_name, last_name, a.address, 
-- 		avg(amount) as promedio
-- 	from customer c inner join payment p using (customer_id)
--     inner join address a using (address_id)
-- 	group by customer_id;

-- 	select * 
-- 	from tmpTotalClientes promedio_cliente
-- 	inner join rental r using (customer_id) 
-- 	where promedio_cliente.promedio > (
-- 		select avg(promedio) promedio_global
-- 		from tmpTotalClientes promedios
-- 	)
--     order by promedio desc
--     limit limite;
--     
--     drop table if exists tmpTotalClientes;
--     
-- end;
-- %%
-- delimiter ;

-- call spTopClientes(3);

-- set @@max_sp_recursion_depth=10;


-- use proyectos;
-- drop procedure if exists spPartidaRaiz;
-- delimiter %%
-- create procedure spPartidaRaiz(in idPartida int)
-- begin
-- 	select id_padre into @idPadre from partidas_presupuestarias
--     where id = idPartida;
--     
--     # id = null
--     if @idPadre is null then
-- 		select * from partidas_presupuestarias where id = idPartida;
-- 	else
-- 		select * from partidas_presupuestarias where id = idPartida;
-- 		call spPartidaRaiz(@idPadre);
--     end if;
-- end;
-- %%
-- delimiter ;

-- call spPartidaRaiz(3);


-- 09:55:59	call spPartidaRaiz(3)	
-- Error Code: 1456. 
-- Recursive limit 0 (as set by the max_sp_recursion_depth variable) 
-- was exceeded for routine spPartidaRaiz	0.0019 sec


# Triggers
# tabla - areas
# evento - insert
# time - before

-- create trigger nombre <time> <event> on <tabla>
-- for each row
-- delimiter %%
-- create trigger tgrMayuscula before insert on areas
-- for each row
-- begin
-- 	set new.nombre = upper(new.nombre);
-- end;
-- %%
-- delimiter ;



-- insert into areas values (4, "prueba", "con disparador");

-- delimiter %%
-- create trigger tgrMayuscula2 after insert on areas
-- for each row
-- begin
-- 	update areas set nombre=upper(nombre)
--     where id = new.id;
-- end;
-- %%
-- delimiter ;

-- insert into areas values (5, "prueba", "con disparador");

-- 10:17:18	insert into areas values (5, "prueba", "con disparador")	Error Code: 1442. 
-- Can't update table 'areas' in stored function/trigger 
-- because it is already used by statement which 
-- invoked this stored function/trigger.	0.0034 sec





use sakila;

-- create table tblResumenVentas 
-- as select customer_id, first_name, last_name, sum(amount) as total
-- from customer as c 
-- inner join payment as p using (customer_id)
-- group by customer_id



-- tabla - payment
-- evento - insert
-- time - after

-- drop trigger tgrResumenVentas;
-- delimiter %%
-- create trigger tgrResumenVentas after insert on payment
-- for each row
-- begin
-- 	
--     set @cliente_existe = (select count(*) from tblResumenVentas where customer_id = new.customer_id);
--     
-- 	# cuando el cliente existe
--     if @cliente_existe > 0 then
-- 		update tblResumenVentas set total = total + new.amount
-- 		where customer_id = new.customer_id;
-- 	else  # el cliente no existe
-- 		select first_name, last_name into @nombre, @apellido 
--         from customer where customer_id = new.customer_id;
--     
-- 		insert into tblResumenVentas
--         values (new.customer_id,@nombre , @apellido , new.amount);
-- 	end if;
-- end;
-- %%
-- delimiter ;


INSERT INTO `sakila`.`customer`
(`store_id`,`first_name`,`last_name`,`email`,`address_id`,`create_date`,`id_persona`)
VALUES (1,"FRANK", "MALO", "fmalo@espol.edu.ec", 5, now(), null);


INSERT INTO `sakila`.`payment`
(`customer_id`,`staff_id`,`rental_id`,`amount`,`payment_date`)
VALUES(600,1,1,12,now());


SET GLOBAL log_bin_trust_function_creators = 1;

-- delimiter %%
-- create function fCalculaIva(valor decimal(10,2)) returns decimal(10,2)
-- begin
-- 	set @total = valor * 0.15;
--     return @total;
-- end;
-- %%
-- delimiter ;


select *, fCalculaIva(amount) as iva
from payment;










create database if not exists ImportTrack;
use ImportTrack;

-- DDL
-- Creacion de tablas

create table if not exists Cliente(
	ID_Cliente int primary key auto_increment not null,
    Direccion varchar(50) not null,
    Correo varchar(50),
    Tipo Enum("Natural","Juridica") not null
);

create table if not exists Persona_Natural(
	ID int primary key not null,
	Nombre varchar(50) not null,
    constraint fk_persona_natural foreign key (ID) references Cliente(ID_Cliente)
);

create table if not exists Persona_Juridica(
	ID int primary key not null,
    Nombre_Comercial varchar(50) not null,
    Razon_Social varchar(50) not null,
    constraint fk_persona_juridica foreign key (ID) references Cliente(ID_Cliente)
);

create table if not exists Telefono(
	ID_Telefono int primary key auto_increment not null,
    ID_Cliente int not null,
    Numero varchar(20) not null,
    constraint fk_cliente_telefono foreign key (ID_Cliente) references Cliente(ID_Cliente) 
);

create table if not exists Pedido(
	ID_Pedido int primary key auto_increment not null,
    Estado_Pedido Enum("Pendiente","En proceso","Enviado","Entregado","Anulado","Devuelto") not null,
    ID_Cliente int not null,
    Total_Paquetes int not null constraint check(Total_Paquetes>0),
    Valor_Total double not null constraint check(Valor_Total>0),
    Valor_Pagado double not null constraint check(Valor_Pagado>=0),
    Fecha datetime not null default now(),
    constraint fk_cliente_pedido foreign key (ID_Cliente) references Cliente(ID_Cliente)
);

create table if not exists Promocion(
	ID_Promocion int primary key auto_increment not null,
    Fecha_Inicio Datetime not null default now(),
    Fecha_Fin Datetime not null,
    Porcentaje_Descuento double not null constraint check (Porcentaje_Descuento>0),
    Estado Enum("Activo","Inactivo") not null,
    Tipo Enum("Promocion_Costo","Promocion_Cantidad","Promocion_Producto","Promocion_Peso") not null,
    constraint check (Fecha_Fin > Fecha_Inicio)
);

create table if not exists Promocion_Costo(
	ID_Promocion int primary key not null,
    Costo_Minimo double not null constraint check (Costo_Minimo>0),
    constraint fk_promocion_costo foreign key (ID_Promocion) references Promocion(ID_Promocion)
);

create table if not exists Promocion_Cantidad(
	ID_Promocion int primary key not null,
    Cantidad_Minima int not null constraint check (Cantidad_Minima>0),
    constraint fk_promocion_cantidad foreign key (ID_Promocion) references Promocion(ID_Promocion)
);

create table if not exists Promocion_Producto(
	ID_Promocion int primary key not null,
    ID_Producto int not null constraint check (ID_Producto>0),
    constraint fk_promocion_producto foreign key (ID_Promocion) references Promocion(ID_Promocion)
);

create table if not exists Promocion_Peso(
	ID_Promocion int primary key not null,
    Peso_Minimo double not null constraint check (Peso_Minimo>0),
    constraint fk_promocion_peso foreign key (ID_Promocion) references Promocion(ID_Promocion)
);

create table if not exists Tracking(
	ID_Tracking int not null auto_increment,
    Fecha_Cambio Datetime not null default now(),
    Estado Enum("Pendiente","En proceso","Enviado","Entregado","Anulado","Devuelto") not null,
    ID_Pedido int not null,
    constraint pk_pedido primary key (ID_Tracking,ID_Pedido),
    constraint fk_pedido foreign key (ID_Pedido) references Pedido(ID_Pedido)
);

create table if not exists Pago(
	ID_Pago int primary key auto_increment not null,
    Monto_Total double not null constraint check (Monto_Total>0),
    Estado_Pago Enum("Pendiente","Completado","Rechazado") not null,
    Fecha_Pago Datetime not null default now(),
    Metodo_Pago Enum("Credito","Debito","Paypal","Efectivo") not null,
    ID_Pedido int not null,
    constraint fk_pedido_pago foreign key (ID_Pedido) references Pedido(ID_Pedido)
);

create table if not exists Codigo_Tracking(
	ID int primary key auto_increment not null,
    ID_Pedido int not null,
    Codigo int not null,
    constraint fk_pedido_codigot foreign key (ID_Pedido) references Pedido(ID_Pedido)
);

create table if not exists Paquete(
	ID_Paquete int primary key auto_increment not null,
    Tienda_Origen varchar(50) not null,
    ID_Promocion int,
    Valor_Con_Descuento double not null,
    Valor_Total double not null constraint check (Valor_Total>0),
    ID_Pedido int not null,
    constraint fk_pedido_paquete foreign key (ID_Pedido) references Pedido(ID_Pedido),
    constraint fk_promocion foreign key (ID_Promocion) references Promocion(ID_Promocion)
);

create table if not exists Producto(
	ID_Producto int primary key auto_increment not null,
    Nombre varchar(20) not null,
    Peso double not null constraint check (Peso>0)
);

create table if not exists Detalle_Paquete(
	Cantidad int not null constraint check (Cantidad>0),
    Precio_Unitario double not null constraint check (Precio_Unitario>0),
    ID_Producto int not null,
    ID_Paquete int not null,
    constraint pk_detalle_paquete primary key (ID_Producto,ID_Paquete),
    constraint fk_detalle_producto foreign key (ID_Producto) references Producto(ID_Producto),
    constraint fk_detalle_paquete foreign key (ID_Paquete) references Paquete(ID_Paquete)
);

-- DML
-- Inserción de datos de prueba

insert into Cliente 
values (1, 'Calle 10 y Av. Colón', 'luis.mejia@correo.com', 'Natural'),
(2, 'Av. Amazonas N32-45', 'jayleen.asencio@correo.com', 'Natural'),
(3, 'Calle Olmedo y 9 de Octubre', 'l.aguilar@correo.com', 'Natural'),
(4, 'Av. La Prensa S12-34', 'jostin.mora@correo.com', 'Natural'),
(5, 'Calle Eloy Alfaro 123', 'gustavo.moscoso@correo.com', 'Natural'),
(6, 'Av. América y Naciones Unidas', 'contacto@mcdonalds.ec', 'Juridica'),
(7, 'Av. de los Shyris N123-45', 'info@pepsi.ec', 'Juridica'),
(8, 'Vía a Daule Km 10', 'ventas@proceramica.ec', 'Juridica'),
(9, 'Av. Principal y Los Álamos', 'bazar@queso.ec', 'Juridica'),
(10, 'Calle Central #505', 'contacto@plinpin.ec', 'Juridica');

insert into Persona_Natural(ID,Nombre) 
values (1,"Luis Mejia"),
(2,"Jayleen Asencio"),
(3,"Luis Aguilar"),
(4,"Jostin Mora"),
(5,"Gustavo Moscoso");

insert into Persona_Juridica(ID,Nombre_Comercial,Razon_Social)
values (6,"McDonald's","Arcos Dorados, S.A."),
(7,"Pepsi","PepsiCo, Inc."),
(8,"Procerámica","Grupo Fernández, S.A."),
(9,"Bazar del Queso","Chascomús, S.A."),
(10,"Juguetes Plinpín","Carlos Fernández, E.I.R.L.");

insert into Telefono 
values (1, 1, "0991234567"),
(2, 2, "0987654321"),
(3, 3, "0976543210"),
(4, 4, "0961112233"),
(5, 5, "0955558888"),
(6, 6, "0937483847"),
(7, 7, "0949373948"),
(8, 8, "0948573948"),
(9, 9, "0949583746"),
(10, 10, "0937463847");

insert into Pedido(Estado_Pedido,ID_Cliente,Total_Paquetes,Valor_Total,Fecha,Valor_Pagado) 
values ("En proceso",1,2,200,now(),200),
("Entregado",2,1,40,"2025-06-30",40),
("Enviado",4,3,300,"2025-07-29",300),
("Pendiente",6,1,20,now(),0),
("Entregado",8,3,250,"2025-05-15",250);

-- Promociones Activas
insert into Promocion(Fecha_Fin, Porcentaje_Descuento, Estado, Tipo) 
values ("2025-08-31",10,"Activo","Promocion_Costo"),
("2025-08-31",15,"Activo","Promocion_Cantidad"),
("2025-08-31",5,"Activo","Promocion_Producto"),
("2025-08-31",20,"Activo","Promocion_Peso"),
("2025-10-09",3,"Activo","Promocion_Costo"),
("2025-10-08",10,"Activo","Promocion_Cantidad"),
("2025-10-07",10,"Activo","Promocion_Producto"),
("2025-09-20",10,"Activo","Promocion_Peso"),
("2025-12-25",8,"Activo","Promocion_Costo"),
("2025-10-05",5,"Activo","Promocion_Cantidad");

-- Promociones Inactivas
insert into Promocion(Fecha_Inicio,Fecha_Fin, Porcentaje_Descuento, Estado, Tipo) 
values ("2025-01-10","2025-01-20",6,"Inactivo","Promocion_Producto"),
("2025-02-10","2025-02-20",20,"Inactivo","Promocion_Peso"),
("2025-03-10","2025-03-20",7,"Inactivo","Promocion_Costo"),
("2025-04-10","2025-04-20",50,"Inactivo","Promocion_Cantidad"),
("2025-05-10","2025-05-20",3,"Inactivo","Promocion_Producto"),
("2025-06-10","2025-06-20",30,"Inactivo","Promocion_Peso"),
("2025-07-10","2025-07-20",25,"Inactivo","Promocion_Costo"),
("2025-01-01","2025-01-05",20,"Inactivo","Promocion_Cantidad"),
("2025-02-01","2025-02-05",10,"Inactivo","Promocion_Producto"),
("2025-03-01","2025-03-05",3,"Inactivo","Promocion_Peso");

insert into Promocion_Costo 
values (1,100),
(5, 200),
(9, 300),
(13, 40),
(17, 30);

insert into Promocion_Cantidad 
values (2,5),
(6, 20),
(10, 3),
(14, 8),
(18, 20);

insert into Promocion_Producto
values (3,1),
(7, 2),
(11, 3),
(15, 3),
(19, 2);

insert into Promocion_Peso
values (4,100),
(8, 200),
(12, 50),
(16, 200),
(20, 20);

insert into Tracking
values (1,"2025-08-03 14:08:20","Pendiente",1),
(2,"2025-08-03 14:30:00","En proceso",1),
(3,"2025-06-30 15:00:00","Pendiente",2),
(4,"2025-07-01 15:00:00","En proceso",2),
(5,"2025-07-04 15:00:00","Enviado",2),
(6,"2025-07-20 15:00:00","Entregado",2),
(7,"2025-07-29 15:00:00","Pendiente",3),
(8,"2025-07-30 15:00:00","En proceso",3),
(9,"2025-08-01 15:00:00","Enviado",3),
(10,"2025-08-03 14:30:00","Pendiente",4),
(11,"2025-05-15 15:00:00","Pendiente",5),
(12,"2025-05-17 15:00:00","En proceso",5),
(13,"2025-05-20 15:00:00","Enviado",5),
(14,"2025-05-25 15:00:00","Entregado",5);

insert into Pago(Monto_Total,Estado_Pago,Fecha_Pago,Metodo_Pago,ID_Pedido)
values (200,"Completado","2025-08-03 14:08:20","Credito",1),
(40,"Completado","2025-06-30 15:00:00","Credito",2),
(300,"Completado","2025-07-29 15:00:00","Credito",3),
(20,"Rechazado","2025-08-03 14:08:20","Debito",4),
(250,"Completado","2025-05-15 15:00:00","Efectivo",5);

insert into Codigo_Tracking(ID,ID_Pedido,Codigo)
values (1, 1, 574638),
(2, 2, 945744),
(3, 3, 948374),
(4, 4, 847645),
(5, 5, 938485);

insert into Producto(ID_Producto,Nombre, Peso)
values (1,"Laptop", 2.5),
(2,"Mouse", 0.2),
(3,"Camiseta algodón", 0.3),
(4,"Silla ergonómica", 8.0),
(5,"Zapatos deportivas", 1.2),
(6,"PlayStation 5", 3.0),
(7,"Llaveros Minecraft", 2.0),
(8,"Cafetera eléctrica", 3.5),
(9,"Calculadora", 0.2),
(10,"Peluche de Mono", 0.3);

insert into Paquete(Tienda_Origen, ID_Promocion, Valor_Con_Descuento, Valor_Total, ID_Pedido)
values ("Amazon",1,135,150,1),
("Amazon",null,65,65,1),
("Ebay",null,40,40,2),
("Amazon",5,194,200,3),
("Amazon",null,53,53,3),
("Amazon",null,53,53,3),
("Temu",15,20,20.6,4),
("Amazon",2,170,200,5),
("Amazon",null,40,40,5),
("Amazon",null,40,40,5);

insert into Detalle_Paquete 
values
(1, 150, 8, 1),
(1, 65, 5, 2),
(1, 40, 5, 3),
(1, 200, 1, 4),
(1, 53, 10, 5),
(1, 53, 3, 6),
(1, 20.6, 3, 7),
(5, 40, 5, 8),
(1, 40, 10, 9),
(1, 40, 7, 10);

-- Consultas significativas definidas en el primer entregable

-- ¿Qué pedidos están pendientes de entrega?
select * 
from Pedido
where Estado_Pedido<>"Entregado"; 

-- ¿Cuáles son los productos que más se han solicitado en el último mes?
select p.Nombre, sum(Cantidad) as total
from Producto p
inner join Detalle_Paquete dp using(ID_Producto)
inner join Paquete pa using(ID_Paquete)
inner join Pedido pe using (ID_Pedido)
where pe.Fecha >= date_sub(curdate(), interval 1 month)
group by p.ID_Producto, p.Nombre
order by total desc;

-- ¿Cuántos pedidos están actualmente en tránsito?
select count(*) as Pedidos_Transito 
from Pedido 
where Estado_Pedido="Enviado";

-- ¿Qué pedidos fueron entregados esta semana?
select *
from Pedido p 
inner join (select * 
from Tracking 
where Estado="Entregado") as pe_entregado 
using(ID_Pedido)
where pe_entregado.Fecha_Cambio between date_sub(curdate(), interval 1 week) and curdate();

-- ¿Cuáles clientes tienen pagos pendientes?
select c.ID_Cliente
from Cliente c
inner join Pedido pe using(ID_Cliente)
inner join Pago pa using(ID_Pedido)
where pa.Estado_Pago = "Pendiente";

-- ¿Qué promociones están activas actualmente?
select *
from Promocion 
where Estado = "Activo";

-- Vista de los productos que mas se han solicitado en el ultimo mes
create view ProductosSolicitados as
select p.Nombre, sum(Cantidad) as total
from Producto p
inner join Detalle_Paquete dp using(ID_Producto)
inner join Paquete pa using(ID_Paquete)
inner join Pedido pe using (ID_Pedido)
where pe.Fecha >= date_sub(curdate(), interval 1 month)
group by p.ID_Producto, p.Nombre
order by total desc; 

-- Procedimiento Almacenado para aplicar una promocion a un paquete
DELIMITER %%
create procedure spAplicarPromocion(in Paquete_ID int, 
in Promocion_ID int)
	BEGIN
		declare cantidad int;
        declare peso_min double;
        declare peso_paquete double;
        declare producto int;
        declare precio double;
        declare descuento double;
        declare tipo_promocion varchar(50);
        declare valor double;
        
		declare exit handler for sqlexception
			begin
				rollback;
				select 'Error inesperado' as Mensaje;
				signal sqlstate '45000'
				set message_text = 'Error inesperado';
			end;
	
        if not exists(select 1  from Paquete where ID_Paquete = Paquete_ID) then
			select 'No existe ese paquete' as Mensaje;
			signal sqlstate '45001'
			set message_text = 'No existe ese paquete.';
        end if;
        
        if not exists(select 1  from Promocion where ID_Promocion = Promocion_ID) then
			select 'No existe esa promocion' as Mensaje;
			signal sqlstate '45002'
			set message_text = 'No existe esa promocion.';
        end if;
        
        if (select Estado from promocion where ID_Promocion=Promocion_ID)="Inactivo" then
			select 'La promocion esta inactiva' as Mensaje;
			signal sqlstate '45003'
            set message_text = 'La promocion esta inactiva';
		end if;
        
		
        start transaction;
        select Valor_Total into valor from Paquete where ID_Paquete = Paquete_ID;
        set descuento = (select Porcentaje_Descuento from promocion where ID_Promocion = Promocion_ID);
        set tipo_promocion= (select Tipo from promocion where ID_Promocion = Promocion_ID);
        if tipo_promocion="Promocion_Costo" then
			set precio = (select Costo_Minimo from promocion p inner join promocion_costo using(ID_Promocion) where ID_Promocion = Promocion_ID);
            if valor>=precio then
					update Paquete set Valor_Con_Descuento = (valor) - (valor * descuento / 100) where ID_Paquete = Paquete_ID;
                    select "Promocion de costo aplicada" as Mensaje;
			else
					select"No aplica para promocion de costo" as Mensaje;
			end if;
        elseif tipo_promocion="Promocion_Cantidad" then
			set cantidad = (select Cantidad_Minima from promocion p inner join promocion_cantidad using(ID_Promocion) where ID_Promocion = Promocion_ID);
            if (select sum(cantidad) from Detalle_Paquete inner join Paquete using (ID_Paquete) where ID_Paquete=Paquete_ID) >= cantidad then
					update Paquete set Valor_Con_Descuento = (valor) - (valor * descuento / 100) where ID_Paquete = Paquete_ID;
					select 'Promocion de cantidad aplicada' as Mensaje;
			else
					select 'No aplica para promocion de cantidad' as Mensaje;
			end if;
        elseif tipo_promocion="Promocion_Producto" then
			set producto = (select ID_Producto from promocion p inner join promocion_producto using(ID_Promocion) where ID_Promocion=Promocion_ID);
            if exists(select 1 from Detalle_Paquete dp where dp.ID_Paquete = Paquete_ID and dp.ID_Producto = producto) then
					update Paquete set Valor_Con_Descuento = (valor) - (valor * descuento / 100) where ID_Paquete = Paquete_ID;
                    select 'Promocion de producto aplicada' as Mensaje;
			else
					select 'No aplica para promocion de producto' as Mensaje;
			end if;
        elseif tipo_promocion="Promocion_Peso" then
			set peso_paquete = (select sum(cantidad*peso) from Detalle_Paquete inner join Producto using(ID_Producto) where ID_Paquete=Paquete_ID);
            set peso_min= (select peso_minimo from promocion p inner join promocion_peso using(ID_Promocion) where ID_Promocion = Promocion_ID);
            if peso_paquete >= peso_min then
					update Paquete set Valor_Con_Descuento = (valor) - (valor * descuento / 100) where ID_Paquete = Paquete_ID;
                    select 'Promocion de peso aplicada' as Mensaje;
			else
					select 'No aplica para promocion de peso' as Mensaje;
			end if;
		end if;
        commit;
	END;
%%

-- Trigger que agrega datos a la tabla de tracking cada vez que se actualiza el estado
-- de un pedido
DELIMITER %%
create trigger tgrTracking after update on Pedido for each row
	BEGIN
		insert into Tracking(Fecha_Cambio,Estado,ID_Pedido)
        values(now(),new.Estado_Pedido,new.ID_Pedido);
    END;
%%

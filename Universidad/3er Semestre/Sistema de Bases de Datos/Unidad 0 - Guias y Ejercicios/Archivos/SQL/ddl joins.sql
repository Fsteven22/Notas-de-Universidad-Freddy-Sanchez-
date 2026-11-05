 /*
 use practica1;

 create table if not exists bus(
	placa varchar(8) not null primary key comment "Placa del bus",
	alias varchar(10) default "Sin alias" comment "Alias del bus",
    modelo varchar(50) default "Modelo no especificado" comment "Modelo del bus",
    capacidad int not null comment "Capacidad del bus",
    combustible varchar(30) default "Combustible no especificado" comment "Tipo de combustible del bus"
);


create table if not exists asiento(
	idAsiento int not null primary key comment "Id del asiento",
	numero int not null comment "Numero del asiento",
    letra varchar(2) comment "Letra del asiento",
	estado boolean not null comment "Estado del asiento",
    bus_fk varchar(8) not null comment "Placa del bus",
    constraint fk_bus foreign key (bus_fk) references  bus (placa)
);

create table if not exists pasajero(
	cedula varchar(10) not null primary key comment "Cedula del pasajero",
    edad int comment "Edad del pasajero",
    nombres varchar(50) not null comment "Nombres del pasajero",
    apellidos varchar(50) not null comment "Apellidos del pasajero"
);

create table if not exists ticket(
	numero int not null primary key comment "Numero del ticket",
    fecha_emision date comment "Fecha cuando se emitio el ticket",
    fk_asiento int not null comment "id del asiento",
    fk_pasajero varchar(10) not null comment "cedula del pasajero asignado",
    constraint asiento_fk foreign key (fk_asiento) references asiento (idAsiento),
    constraint pasajero_fk foreign key (fk_pasajero) references pasajero (cedula) 
);

create table if not exists conductor(
	cedula varchar(10) not null primary key comment "Cedula del conductor"
);

create table if not exists conductor_bus(
	fk_conductor varchar(10) not null comment "Cedula del conductor",
    fk_bus varchar(8) not null comment "Placa del bus",
    constraint conductor_fk foreign key (fk_conductor) references conductor (cedula),
    constraint bus_fk foreign key (fk_bus) references bus (placa),
    constraint clavep primary key (fk_conductor,fk_bus)
);
*/

select c.first_name,c.last_name, f.title 
from customer c inner join  rental r using (customer_id) 
inner join inventory i using (inventory_id) 
inner join film f using (film_id)  
where r.return_date is null;

select c.first_name,c.last_name, f.title
from customer c
inner join (rental r, inventory i, film f)
on (c.customer_id=r.customer_id and r.inventory_id = i.inventory_id and i.fiml_id = f.film_id);

select * from rental;

select c.first_name, c.last_name, count(distinct i.film_id) as total 
from customer c 
inner join (rental r, inventory i) 
on (c.customer_id=r.customer_id and r.inventory_id = i.inventory_id)
group by r.customer_id 
order by total desc;    

select c.first_name, c.last_name, sum(p.amount) as total 
from customer c 
inner join payment p using (customer_id) 
group by customer_id
having sum(p.amount) > 100 
order by total desc;

select title, rental_date 
from film f
inner join inventory i using(film_id)
left join rental r using (inventory_id)
where  month(rental_date) = 5 and year (rental_date) = 2005;  


select * from partidas_presupuestarias;
select p.nombre, p2.nombre from  partidas_presupuestarias p inner join partidas_presupuestarias p2 on p2.id_padre = p.id;
select * from partidas_presupuestarias padre left join partidas_presupuestarias hijo on hijo.id_padre=padre.id where hijo.id is null;
select p.nombre, count(h.id) as hijos from partidas_presupuestarias p left join partidas_presupuestarias h on h.id_padre=p.id group by p.id;
select p.nombre, po.nombre, count(h.id) as hijos from partidas_presupuestarias p left join partidas_presupuestarias h on h.id_padre=p.id inner join proyectos po on po.id=p.id_proyecto group by p.id ;

-- Clientes que no concretaron una venta
use crm;
select distinct c.NombreEmpresa
from cliente c 
inner join  oportunidad o using (ClienteID)
inner join (select count(distinct OportunidadID) as contar from oportunidad 
group by OportunidadID) as totales using (OportunidadID)  
left join venta v using (OportunidadID)
where contar<>(select count(distinct OportunidadID) as contar 
from oportunidad left join venta v using (OportunidadID) where OportunidadID is null);

select NombreEmpresa, count(VentaId)
from cliente c
inner join Oportunidad o using (ClienteID)
left join Venta using (OportunidadID)
group by ClienteID;

select * from venta;

-- limit - Tamaño de la pagina
-- offset - Indice donde inicia la paginacion, por defecto es 0

select * from Oportunidad 
order by MontoCierre desc
limit 3;

use sakila;
create table if not exists TPersona(
	id int auto_increment primary key,
    nombre varchar(45),
    apellido varchar(45)
);

insert into TPersona (nombre,apellido) 
select distinct * from (
select first_name, last_name
from actor
union 
select first_name, last_name
from customer
union
select first_name, last_name
from staff
) t1;

alter table actor add column id_persona int null;
alter table actor add constraint fk_actor_persona foreign key(id_persona) references TPersona(id);

update actor a
inner join TPersona p on (p.nombre=actor.first_name and p.apellido = a.last_name)
set id_persona=p.id;

alter table actor add column id_customer int null;
alter table actor add constraint fk_actor_customer foreign key(id_customer) references TPersona(id);

update actor a
inner join TPersona p on (p.nombre=actor.first_name and p.apellido = a.last_name)
set id_persona=p.id;


-- create view nombre (Opcionalmente Columnas) 
-- as ... select

select distinct title
from inventory i 
inner join film using (film_id)
where inventory_id not in(select inventory_id
from rental where return_date is null);

create view peliculas_disponibles as
select distinct title
from inventory i 
inner join film using (film_id)
where inventory_id not in(select inventory_id
from rental where return_date is null);

select * from peliculas_disponibles;
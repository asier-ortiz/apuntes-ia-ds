DROP DATABASE IF EXISTS mysqlapp;
CREATE SCHEMA mysqlapp DEFAULT CHARACTER SET utf8;
create table mysqlapp.SMARTPHONE
(
	id int auto_increment,
	manufacturer varchar(200) null,
	model varchar(100) null,
	ram int null,
	constraint SMARTPHONE_pk primary key (id)
);
create table mysqlapp.USER
(
	id int auto_increment,
	first_name varchar(50) not null,
	last_name varchar(50) null,
	age int null,
	id_smartphone int null,
	constraint USER_pk primary key (id),
	constraint USER_SMARTPHONE_id_fk
    foreign key (id_smartphone) references SMARTPHONE (id) on delete set null
);

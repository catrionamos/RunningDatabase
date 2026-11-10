create table if not exists programs(
program_id varchar(10) not null primary key,
program_name varchar(100) not null,
target_level varchar(30),
duration_weeks int,
description varchar(255)
);

create table if not exists users(
userid varchar(50) not null primary key,
password varchar(200) not null,
email varchar(120),
fitness_level varchar(30),
running_goal varchar(100),
program_id varchar(10),
foreign key (program_id) references programs(program_id)
);

create table if not exists products(
product_id varchar(10) not null primary key,
product_name varchar(100) not null,
category varchar(50),
price float,
stock_quantity int
);

create table if not exists runs(
run_id serial primary key,
userid varchar(50) not null,
run_date date,
distance_km float,
duration_minutes int,
notes varchar(255),
foreign key (userid) references users(userid)
);

create table if not exists orders(
order_id varchar(10) not null primary key,
userid varchar(50) not null,
product_id varchar(10) not null,
quantity int,
order_date date,
foreign key (userid) references users(userid),
foreign key (product_id) references products(product_id)
);

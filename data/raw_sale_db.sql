--Script para criar a tabela de origem (ex: tabela de vendas)
--Script to create  the origin table (e.g., sales table)

create table if not exists Customers (
    customer_id int primary key,
    customer_name varchar(100),
    customer_city varchar(100),
    customer_state varchar(50),
    registration_date date
);

create table if not exists Products (
    product_id int primary key,
    product_name varchar(100),
    category varchar(50),
    subcategory varchar(50),
    price decimal(10,2)
);

create table if not exists Sales (
    sale_id int primary key,
    request_id int,
    customer_id int references Customers(customer_id),
    product_id int references Products(product_id),
    quantity int,
    sale_date date
);
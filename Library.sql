create database library;
use library;
create table address(
address_id int auto_increment primary key,
branch_name varchar(30),
street_number int,
street_name varchar(30),
town varchar(30),
city varchar(30),
postcode varchar(10));

use library;
create table branch(
branch_id int auto_increment primary key,
branch_number int not null,
branch_phone varchar(70) not null,
branch_address varchar(100) not null,
branch_annual_budget decimal not null);

select * from branch;

use library;
create table users(
user_id int primary key auto_increment,
library_card int not null,
user_name varchar(30) not null,
user_age int not null check (user_age >=16),
fine_date date,
fine_date2 date,
fine_cost decimal,
fine_cost2 decimal,
fine_outstanding varchar(3) not null,
blocked varchar(3) not null);

select * from users;

use library;
create table books(
book_id int primary key auto_increment,
dewy_decimal_number decimal,
isbn varchar(13) not null,
book_title varchar(80) not null,
author varchar(30) not null,
author2 varchar(30),
genre varchar(30) not null,
year_published int not null,
branch_id int not null,
foreign key (branch_id) references branch(branch_id),
copy_number int not null,
on_loan varchar(3) not null);

select * from books;

use library;
create table staff(
staff_id int primary key auto_increment,
employee_number int not null,
staff_name varchar(30) not null,
phone int,
email varchar(30),
branch_id int not null,
foreign key (branch_id) references branch(branch_id),
job_role varchar(30) not null,
salary decimal,
national_insurance varchar(9) not null);

select * from staff;

use library;
create table reservations(
reservation_id int primary key auto_increment,
user_id int not null,
foreign key (user_id) references users(user_id),
book_id int not null,
foreign key (book_id) references books(book_id),
reservation_date date);

select * from reservations;

use library;
create table loans(
loan_id int primary key auto_increment,
user_id int not null,
foreign key (user_id) references users(user_id),
branch_id int not null,
foreign key (branch_id) references branch(branch_id),
book_id int not null,
foreign key (book_id) references books(book_id),
date_loaned date,
date_returned date);

select * from loans;

use library;
create table author(
author_id int primary key auto_increment,
first_name varchar(20),
last_name varchar(20));

use library;
create table book_author(
book_author_id int primary key auto_increment,
book_id int not null,
foreign key (book_id) references books(book_id),
author_id int not null,
foreign key (author_id) references author(author_id));

insert into staff(staff_id, employee_number, staff_name, phone, email, branch_id, job_role, salary, national_insurance)
 values (1, 567, 'Jason', 0786948756, 'js@hotmail.com', 1, 'librarian', 20000, 'ah34567');

insert into address
values (3, 'London', 34, 'Grey Street', 'Kensington', 'London', 'L2 7HG');

select * from address;

insert into author
values (1, 'JK', 'Rowling'),
	   (2, 'Anne', 'Fine'),
       (3, 'James', 'Herbert');

select * from author;

insert into branch
values(1, 23, 078541254, 'Leeds', 20000),
	  (2, 123, 075212442, 'Newcastle', 150000),
      (3, 78, 0457812557, 'London', 250000);

select * from branch;

insert into users
values(1, 547854, 'John Smith', 45, '2022-01-12', '2005-05-10', 5.00, 4.00, 'yes', 'yes');

select * from users;

insert into users
values(2, 544854, 'Mary White', 28, '2022-01-10', '2018-08-02', 8.00, 4.50, 'yes', 'yes'),
	  (3, 687854, 'Sarah Little', 18, '2022-01-15', '2017-01-17', 5.50, 2.00, 'yes', 'yes');


    

    

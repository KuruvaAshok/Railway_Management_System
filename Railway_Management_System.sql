create database railway;
use railway;
show tables;

-- Table-1 Passenger details
create table psgr_det(
pid int, 
pname varchar(20),
age int,
mbl int,
gender varchar(10),
primary key(pid)
);

-- Table-2  Train Details
create table train_det(
train_no int,
train_name varchar(50),
source varchar(20),
destination varchar(20),
primary key(train_no)
);

-- Table-3 Routes Details
create table routes(
train_no int,
stop1 varchar(20),
stop2 varchar(20),
stop3 varchar(20),
stop4 varchar(20),
FOREIGN KEY(train_no) REFERENCES train_det(train_no)
);


-- Table-4  Train_Capacity Details
create table train_capacity(
train_no int,
ac_1 int,
ac_2 int,
ac_3 int,
sleeper int,
gen int,
FOREIGN KEY(train_no) REFERENCES train_det(train_no)
);

-- Table-5 Transactions
create table transactions(
tid int,
fare int,
pid int,
payment_mode varchar(20),
primary key(tid),
FOREIGN KEY(pid) REFERENCES psgr_det(pid)
);

-- Table-6 Booking_Tickets
create table book_tic(
book_id int primary key,
tid int,
train_no int,
pid int,
class varchar(20),
seatno int,
source varchar(20),
destination varchar(20),
foreign key(tid) REFERENCES transactions(tid),
FOREIGN KEY(pid) REFERENCES psgr_det(pid),
FOREIGN KEY(train_no) REFERENCES train_det(train_no)
);

show tables;

select * from train_capacity;
select * from psgr_det;
select * from train_det;
select * from routes;
select * from transactions;
select * from book_tic;

-- Chcking thwe null values in Class(ac_1)
-- select train_det.train_no from train_det left join train_capacity on
-- train_det.train_no=train_capacity.train_no where ac_1 is null;
--          -- OR --
-- select train_no from train_det where train_no not in(select train_no from train_capacity);


-- DELETE FROM psgr_det WHERE pid = 4; 
-- DELETE FROM transactions WHERE tid = 2;


-- Inserting values into tables
-- insert into train_det values (14756, 'Venkatadri Exp','Kacheguda','Tirupati');
-- insert into routes values (14756,'jadcherla','kurnool','kadiri','renigunta');


-- Booking ticket from source to dr=estination
-- select routes.train_no,source,stop1,stop2,stop3,stop4,destination from routes inner join train_det 
-- on  routes.train_no = train_det.train_no  where source='jadcherla' or stop1='jadcherla' or stop2='jadcherla' or stop3='jadcherla' or stop4='jadcherla';

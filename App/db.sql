#####all Numbers and Names Are Fake :)####

# create database DB_Project1;
create table employee(
    emp_id int primary key ,
    emp_name varchar(20),
    emp_last varchar(20),
    emp_sex varchar(1),
    emp_call varchar(11),
    emp_birth_day date,
    branch_id int,
    salary int
);
create table branch(
    branch_id int primary key ,
    branch_name varchar(20),
    branch_call varchar(11),
    branch_address varchar(30),
    branch_password int,
    mng_id int ,
    foreign key (mng_id) references employee(emp_id) on delete set null
);
create table client(
    client_id int primary key ,
    client_name varchar(20),
    client_last varchar(20),
    client_call varchar(11),
    client_address varchar(30)

);
create table raw_material(
    rm_id int primary key ,
    rm_name varchar(20),
    rm_type varchar(20)
);

create table product(
    product_id int primary key ,
    product_name varchar(20),
    product_amount int
);
alter table product change product_amount Product_price int;

create table sell(
    sell_id int primary key,
    branch_id int,
    client_id int,
    product_id int,
    sell_amount int,
    sell_price int,
    date_ date,
    time_ time,
    foreign key (branch_id) references branch(branch_id) on delete set null ,
    foreign key (client_id) references client(client_id) on delete set null ,
    foreign key (product_id) references product(product_id) on delete set null
);
create table buy(
    buy_id int primary key, #change
    branch_id int,
    client_id int,
    rm_id int,
    buy_amount int,
    buy_price int,
    buy_date date,
    buy_time time,
    foreign key (branch_id) references branch(branch_id) on delete set null ,
    foreign key (client_id) references client(client_id) on delete set null ,
    foreign key (rm_id) references raw_material(rm_id) on delete set null
);

create table rm_for_branch(
    rm_id int ,
    branch_id int,
    amount int,
    primary key (rm_id,branch_id),
    foreign key (rm_id) references raw_material(rm_id) on delete cascade ,
    foreign key (branch_id) references branch(branch_id) on delete cascade

);

create table pr_for_branch(
    pr_id int,
    branch_id int,
    amount int,
    primary key (pr_id,branch_id),
    foreign key (pr_id) references product(product_id) on delete cascade ,
    foreign key (branch_id) references branch(branch_id) on delete cascade
);

#update Employee Foreign Key
alter table employee add
foreign key (branch_id) references branch(branch_id)
on delete set null ;

insert into employee values (100,'soroush','alizadeh','m','09303339934','1372-11-17',NULL,4500);
insert into branch values (200,'NaabGol','54203423','RahimAbad',12345,100);

update branch set mng_id=100 where branch_name='NaabGol';
update employee set branch_id=200 where emp_id=100;

insert into employee values (101,'Hasan','Karimi','m','09112843429','1370-02-20',200,4000);
insert into branch values (201,'Kaj','54284354','Rudsar',1234,NULL);
insert into branch values (202,'Bahar','34627345','Rasht',1234,NULL);
insert into employee values (102,'Sina','Alizadeh','m','09111943458','1371-10-22',202,6400);

update branch set mng_id=102 where branch_name='Bahar';


insert into employee values (103,'Fatemeh','Ghorbani','f','09386729934','1375-01-21',202,4200);
insert into employee values (104,'Alireza','Mohammadi','m','09903455343','1369-08-09',201,5200);

update branch set mng_id=104 where branch_name='Kaj';


insert into product values (300,'Fandogh Shoor',370);
insert into product values (301,'Fandogh Tarak Khorde',120);
insert into product values (302,'Kare Fandogh',95);
insert into product values (303,'Maghz Fandogh',400);
insert into product values (304,'Avishan',150);
insert into product values (305,'Gol GavZaban',220);
insert into product values (306,'Chaei Kuhi',100);

insert into raw_material values(400,'Fandogh','Daraje1');
insert into raw_material values(401,'Fandogh','Daraje2');
insert into raw_material values(402,'Gol GavZaban','Daraje1');
insert into raw_material values(403,'Gol GavZaban','Daraje2');
insert into raw_material values(404,'Avishan','Daraje1');
insert into raw_material values(405,'Avishan','Daraje2');
insert into raw_material values(406,'Chaei Kuhi','Daraje1');
insert into raw_material values(407,'Chaei Kuhi','Daraje2');

select* from branch;
#Available Row Material in branch 200
insert into rm_for_branch values (400,200,9000);
insert into rm_for_branch values (401,200,4500);
insert into rm_for_branch values (402,200,300);
insert into rm_for_branch values (404,200,500);
insert into rm_for_branch values (407,200,340);
#Available Row Material in branch 201
insert into rm_for_branch values (400,201,7599);
insert into rm_for_branch values (401,201,5330);
insert into rm_for_branch values (402,201,231);
insert into rm_for_branch values (403,201,654);
insert into rm_for_branch values (405,201,245);
#Available Row Material in branch 202
insert into rm_for_branch values (400,202,8490);
insert into rm_for_branch values (401,202,4955);
insert into rm_for_branch values (402,202,320);
insert into rm_for_branch values (404,202,490);
insert into rm_for_branch values (407,202,330);

#Available Product in Branch 200
insert into pr_for_branch values (300,200,200);
insert into pr_for_branch values (301,200,100);
insert into pr_for_branch values (302,200,100);
insert into pr_for_branch values (304,200,100);
insert into pr_for_branch values (305,200,100);
#Available Product in Branch 201
insert into pr_for_branch values (300,201,200);
insert into pr_for_branch values (301,201,400);
insert into pr_for_branch values (302,201,130);
insert into pr_for_branch values (304,201,150);
insert into pr_for_branch values (305,201,134);
#Available Product in Branch 202
insert into pr_for_branch values (300,202,644);
insert into pr_for_branch values (301,202,466);
insert into pr_for_branch values (302,202,178);
insert into pr_for_branch values (304,202,146);
insert into pr_for_branch values (305,202,145);


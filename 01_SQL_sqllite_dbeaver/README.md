# SQL
* **SQLlite**
    * create file **newfile.db**
* **dbeaver** community version
    * Database
        * select **sqllite**
* DDL
    * create
    * update
    * delete
    * insert

# Now start wrtie query
```
CREATE TABLE students(
sid INT,
name VARCHAR(255),
fname VARCHAR(255),
course VARCHAR(255)
);
```


## Insert
### insert single value with columns names
```
INSERT INTO students(sid, course, name,fname)
VALUES (1,'AI','Hamza','Ali')

```

### insert single value without columns names but all columns sequance should be same

```
INSERT INTO students 
VALUES (2,'Asif','Abid','Blockchain')

```

### insert multiple value without columns names but all columns sequance should be same

```
INSERT INTO students 
VALUES 
(3,'Asif Khan','Abid','CNC'),
(4,'Abid','Ali','AI'),
(5,'Yaseer','Ahmed','Blockchain'),
(6,'Asif Ahmed khan','Abid','AI')
```
# DML
# SQL SELECT Statement

```
SELECT course,sid,name
FROM students
```

## AS or nickname
```
select sid+10 as student_id
from students 


select sid+10 student_id
from students 
```


```
SELECT 
   cs.CustomerID, cs.CustomerName,cs.City ,od.orderid 
FROM
  Customers cs, orders od
where 
   cs.customerid = od.customerid
order by 
  cs.customerid



```

# all query

```
CREATE TABLE students(
sid INT,
name VARCHAR(255),
fname VARCHAR(255),
course VARCHAR(255)
)

INSERT INTO students(sid, course, name,fname)
VALUES (1,'AI','Hamza','Ali')


INSERT INTO students 
VALUES (2,'Asif','Abid','Blockchain')

INSERT INTO students 
VALUES 
(3,'Asif Khan','Abid','CNC'),
(4,'Abid','Ali','AI'),
(5,'Yaseer','Ahmed','Blockchain'),
(6,'Asif Ahmed khan','Abid','AI')


// DML

SELECT course,sid,name
FROM students


SELECT course,sid,name
FROM students


select sid+10 as student_id
from students 


select sid+10 student_id
from students 



select name || ' ' || fname as message
from students


select 'Hello Dear, ' || name || ' S/O or D/O ' || fname || ' Welcome in NED Data Visualization Class'  as Message
from students

create table customers(
CustomerID INT,
CustomerName VARCHAR(255),
ContactName VARCHAR(255),
Address VARCHAR(255),
City VARCHAR(255),
PostalCode VARCHAR(255),
Country VARCHAR(255)
)



select DISTINCT country from customers


select * from customers


select * from customers
WHERE 
	Country = 'USA'
	
	
	
select * from customers
WHERE 
	Country = 'USA' or 
	Country = 'UK' or 
	Country = 'Canada'
	
select * from customers
WHERE 
	Country IN ('USA', 'UK', 'Canada')	
	
	
select count(*) from customers 	


select country, count(*) as no_of_cus from customers
GROUP BY country


select * from customers
ORDER BY country



select * from customers
ORDER BY country DESC
	


select country, count(*) as no_cus from customers 
GROUP BY country
ORDER BY no_cus DESC


ALTER TABLE students 
alter column sid int primary key

delete  from students 
where tid = 1

update students 
set tid=1


create table teachers(
tid int,
name varchar(255),
primary key (tid)
)

insert into teachers 
values (1,'Qasim')




```
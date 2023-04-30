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

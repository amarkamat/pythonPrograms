1. Create a table (student) with 3 columns (rollno, name, course).
postgres=# create table student(rollno int,name text,course text,PRIMARY KEY (rollno));
postgres=# create table student(rollno int PRIMARY KEY,name text,course text);

2. Insert records for 4 students.
postgres=# insert into student(rollno,name,course) values(101,'Jack','Maths');
postgres=# insert into student(rollno,name,course) values(102,'Mark','Science');
postgres=# insert into student(rollno,name,course) values(103,'Sam','Geo');
postgres=# insert into student(rollno,name,course) values(104,'Rup','SST');
insert into student values(101,'Jack','Maths'),(102,'Mark','Science'),(103,'Sam','Geo'),(104,'Rup','SST');

3. Write a Select query to fetch all the students.
postgres=# select * from student;
 rollno | name | course  
--------+------+---------
    101 | Jack | Maths
    102 | Mark | Science
    103 | Sam  | Geo
    104 | Rup  | SST
(4 rows)

4. Update the student name of rollno 3 with ‘Mohan’
postgres=# update student set name='Mohan' where rollno=103;
UPDATE 1
postgres=# select * from student;
 rollno | name  | course  
--------+-------+---------
    101 | Jack  | Maths
    102 | Mark  | Science
    104 | Rup   | SST
    103 | Mohan | Geo
(4 rows)

5. Delete any student from table with their rollno.
postgres=# delete from student where rollno=103;
DELETE 1
postgres=# select * from student;
 rollno | name | course  
--------+------+---------
    101 | Jack | Maths
    102 | Mark | Science
    104 | Rup  | SST
(3 rows)

6. Delete all the data from student table.
postgres=# delete from student;
DELETE 3
postgres=# select * from student;
 rollno | name | course 
--------+------+--------
(0 rows)

7. Drop the student table.
postgres=# drop table student;
postgres=# select * from student;
ERROR:  relation "student" does not exist
LINE 1: select * from student;

8. Create Courses table (cid, cname) where cid is a primary key and Student table
(rollno, name, cid) where rollno is a primary key and cid is a foreign key.
postgres=#create table courses(cid int PRIMARY KEY,cname text);
postgres=#create table student(rollno int,name text,cid int,PRIMARY KEY (rollno),FOREIGN KEY (cid) REFERENCES courses(cid));

9. Insert data in both the tables.
postgres=# insert into courses values(1,'python'),(2,'java'),(3,'c++'),(4,'C');
INSERT 0 4
postgres=# select * from courses;
 cid | cname  
-----+--------
   1 | python
   2 | java
   3 | c++
   4 | C
(4 rows)

postgres=# insert into student values(101,'veera',4),(102,'deep',2),(103,'amar',1),(104,'sri',3),(105,'minal',1);
INSERT 0 5
postgres=# select * from student;
 rollno | name  | cid 
--------+-------+-----
    101 | veera |   4
    102 | deep  |   2
    103 | amar  |   1
    104 | sri   |   3
    105 | minal |   1
(5 rows)

10. Select all the students who are doing a specific course, eg. Python.
postgres=# select name from student where cid=(select cid from courses where cname='python');
 name  
-------
 amar
 minal
(2 rows)


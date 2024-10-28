## Student Management System Project 

### Login into SQL Server
```bash
mysql -u root -p
```

### Create a database
```sql
Create database StudentManagement
```

### use Database
```sql
use StudentManagement
```

### Table Creation
- Student

```sql
Create Table Students ( 
    -> student_id INT Auto_increment Primary Key,
    -> first_name VARCHAR(100),
    -> last_name VARCHAR(100),
    -> dob DATE Not NULL,
    -> gender ENUM('Male','Female'),
    -> email VARCHAR(100),
    -> phone_number VARCHAR(15),
    -> enrollment_date DATE);
```


- Courses
```sql
Create Table Courses (
    -> course_id INT Auto_increment Primary Key,
    -> course_name varchar(50),
    -> instructor_name varchar(50),
    -> credits INT);
```

- Enrollments

```sql
Create Table Enrollments(
    -> enrollment_id INT Auto_increment Primary Key,
    -> student_id INT,
    -> course_id INT,
    -> enrollment_date DATE,
    -> grade DECIMAL(3,2),
    -> FOREIGN KEY (student_id) REFERENCES Students(student_id),
    -> FOREIGN KEY (course_id) REFERENCES Courses(course_id));
```

### Show Tables

```sql
show tables;
```

### INSERT Some Sample Data

- Insert data into Students Table
```sql
INSERT INTO Students(first_name, last_name, dob, gender, email, phone_number, enrollment_date) VALUES
('Aditi','Garg','2001-07-24','Female','aditi.ms@gmail.com','9205665703','2023-10-23'),
('Jane','Smith','1999-10-12','FEMALE','jane.smith@gmail.com','9999999999','2024-01-15');
```


- Insert data into Courses Table
```sql
INSERT INTO Courses(course_name, instructor_name, credits) values ('Database Systems','Apoorv',4), ('Operating Systems','Rachit',2), ('Computer Networks','Aditi',3);
```

- Insert data into Enrollments Table
```sql
INSERT INTO enrollments(student_id, course_id, enrollment_date, grade) Values (1,2,'2024-10-25',3.7),  (2,1,'2024-02-02',3.9), (2,3,'2024-02-27',3.5);
```

### Select Queries

- Get all Student Records
```sql
Select * from Students;
```
<img width="1341" alt="Screenshot 2024-10-23 at 8 18 35 AM" src="https://github.com/user-attachments/assets/f28d6a50-0caf-46b7-a0f1-b5a36ea94951">



- Get Student Records where last_name is Garg
```sql
Select * from Students where last_name='Garg';
```
<img width="1372" alt="Screenshot 2024-10-23 at 8 23 26 AM" src="https://github.com/user-attachments/assets/c01fe095-e790-4d2c-985d-54d5b2223a68">

- Fint Students who enrolled after January 01. 2024 
```sql
Select * from Students where enrollment_date > '2024-01-01';
```
<img width="1387" alt="Screenshot 2024-10-23 at 8 27 08 AM" src="https://github.com/user-attachments/assets/d7ff7e7f-c1fe-4432-8dc9-25059cc23bda">

- Count the number of records in Student table

```sql
Select Count(*) from Students;
```
<img width="473" alt="Screenshot 2024-10-23 at 8 28 11 AM" src="https://github.com/user-attachments/assets/45d2bac5-3d75-46df-a413-5d94cfb5a79f">

- Find Distinct Last name in Students table
```sql
Select Distinct(last_name) from Students;
```   
<img width="588" alt="Screenshot 2024-10-23 at 8 29 58 AM" src="https://github.com/user-attachments/assets/9fb41426-3f99-42cc-8b72-2a8c3b889d5f">

- 'ORDER BY' Clause ( Ascending Order)

Defautl Behavior - Ascending Order
```sql
Select * from Students order by column_name;
```
OR
```sql
Select * from Students order by column_name asc;
``` 
<img width="1408" alt="Screenshot 2024-10-28 at 7 37 05 AM" src="https://github.com/user-attachments/assets/5634cfec-52ae-4cea-8939-9fa44f4407e6">
<img width="1350" alt="Screenshot 2024-10-28 at 7 38 50 AM" src="https://github.com/user-attachments/assets/30bdcb80-2607-4c06-8aad-ad2c2c231c24">

- 'ORDER BY' Clause (Descending Order)
```sql
Select * from Students order by column_name desc;
```   
<img width="1364" alt="Screenshot 2024-10-28 at 7 40 03 AM" src="https://github.com/user-attachments/assets/1a372500-7c28-407c-beda-34036e999f8c">

- 'Group By' Clause
```sql
Select * from Students group by gender;
```
<img width="1440" alt="Screenshot 2024-10-28 at 8 02 57 AM" src="https://github.com/user-attachments/assets/e150bcf3-b336-4a6a-a1ce-8a8580e517f8">
  
```sql
Select 1 from Students group by gender;
```
<img width="712" alt="Screenshot 2024-10-28 at 8 02 48 AM" src="https://github.com/user-attachments/assets/0e746042-0ebc-49ff-a22e-cf19d7502f99">

```sql
Select Count(*), gender from Students group by gender;
```
<img width="732" alt="Screenshot 2024-10-28 at 8 00 55 AM" src="https://github.com/user-attachments/assets/fe4a3846-0f87-4039-bde1-da041db3cdaa">

- 'Group by' + 'having' clause
```sql
Select Min(dob) as 'dob_count',gender from Students group by gender having dob_count > '2000-01-01';
```
<img width="1440" alt="Screenshot 2024-10-28 at 8 47 18 AM" src="https://github.com/user-attachments/assets/faca326a-07a3-47e0-9aad-102a8f5503f9">

<img width="1440" alt="Screenshot 2024-10-28 at 8 47 01 AM" src="https://github.com/user-attachments/assets/5f44cfb7-2319-49b5-86f0-4d84f46222ea">

- 'Between' Operator
```sql
Select course_name, credits from courses where credits between 1 and 3;
```
<img width="975" alt="Screenshot 2024-10-28 at 8 48 04 AM" src="https://github.com/user-attachments/assets/8e9f7c36-7e29-4ba3-94c0-6a6b013301b3">




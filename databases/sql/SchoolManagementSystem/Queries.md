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

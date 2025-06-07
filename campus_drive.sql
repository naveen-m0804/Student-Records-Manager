CREATE DATABASE campus_drive;
USE campus_drive;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    year INT
);

select * from students;

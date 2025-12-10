CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade >= 1 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

INSERT INTO students (full_name, birth_year) 
VALUES 
('Alice Johnson', 2005), ('Brian Smith', 2004), ('Carla Reyes', 2006), ('Daniel Kim', 2005), ('Eva Thompson', 2003),
('Felix Nguyen', 2007), ('Grace Patel', 2005), ('Henry Lopez', 2004), ('Isabella Martinez', 2006)

INSERT INTO grades 
VALUES 
(1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85), (2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
(3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89), (4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
(5, 'English', 90), (5, 'History', 85), (5, 'Math', 88), (6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
(7, 'Art', 84), (7, 'Science' 87), (7, 'Math', 60), (8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80), 
(9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92)

select grade from grades 
join students on student_id = students.id
where full_name = 'Alice Johnson'

select round(AVG(grade), 2) as 'Average grade', full_name from grades 
join students on student_id = students.id
group by full_name

select birth_year, full_name from students
where birth_year > 2004

select round(AVG(grade), 2) as 'Average grade', subject from grades 
group by subject

select round(AVG(grade), 2) as 'Average grade', full_name from grades 
join students on student_id = students.id
group by full_name
order by round(AVG(grade), 2)
limit 3

select grade, full_name from grades 
join students on student_id = students.id
where grade < 80

select distinct full_name from grades 
join students on student_id = students.id
where grade < 80
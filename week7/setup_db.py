import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.executescript("""
    DROP TABLE IF EXISTS students;
    DROP TABLE IF EXISTS courses;
    DROP TABLE IF EXISTS enrollments;

    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT,
        gpa REAL
    );

    CREATE TABLE courses (
        id INTEGER PRIMARY KEY,
        title TEXT,
        department TEXT,
        credits INTEGER
    );

    CREATE TABLE enrollments (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );

    INSERT INTO students VALUES
        (1, 'Alice', 22, 'Orlando', 3.8),
        (2, 'Bob', 24, 'Tampa', 3.1),
        (3, 'Carol', 21, 'Orlando', 3.9),
        (4, 'David', 23, 'Miami', 2.7),
        (5, 'Eva', 22, 'Tampa', 3.5),
        (6, 'Frank', 25, 'Orlando', NULL);

    INSERT INTO courses VALUES
        (1, 'Introduction to QA', 'Computer Science', 3),
        (2, 'Database Systems', 'Computer Science', 4),
        (3, 'Agile Methods', 'Business', 3),
        (4, 'Test Automation', 'Computer Science', 4),
        (5, 'UX Design', 'Design', 2);

    INSERT INTO enrollments VALUES
        (1, 1, 1, 'A'),
        (2, 1, 2, 'B'),
        (3, 2, 1, 'C'),
        (4, 2, 3, 'B'),
        (5, 3, 1, 'A'),
        (6, 3, 4, 'A'),
        (7, 4, 2, 'D'),
        (8, 5, 3, 'B'),
        (9, 5, 4, 'A'),
        (10, 6, 5, 'B');
""")



conn.commit()
conn.close()
print("Database created successfully.")
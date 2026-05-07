import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# First let's insert some dirty data to work with
# Insert dirty data
cursor.execute("INSERT INTO enrollments VALUES (11, 1, 1, 'B')")
cursor.execute("INSERT INTO students VALUES (7, 'Grace', 20, NULL, 3.2)")
cursor.execute("INSERT INTO enrollments VALUES (12, 7, 99, 'A')")
conn.commit()

# 1. Find duplicate enrollments (same student in same course more than once)
print("--- Duplicate Enrollments ---")
cursor.execute("""
    SELECT student_id, course_id, COUNT(*) as count
    FROM enrollments
    GROUP BY student_id, course_id
    HAVING COUNT(*) > 1
""")
print(cursor.fetchall())

# 2. Find students with missing required fields
print("\n--- Students with Missing City ---")
cursor.execute("""
    SELECT name, city
    FROM students
    WHERE city IS NULL
""")
print(cursor.fetchall())

# 3. Orphaned records - enrollments pointing to non-existent courses
print("\n--- Enrollments with Invalid Course ID ---")
cursor.execute("""
    SELECT enrollments.id, enrollments.student_id, enrollments.course_id
    FROM enrollments
    LEFT JOIN courses ON enrollments.course_id = courses.id
    WHERE courses.id IS NULL
""")
print(cursor.fetchall())

# 4. Find students enrolled in more courses than allowed (limit: 2)
print("\n--- Students Exceeding Enrollment Limit ---")
cursor.execute("""
    SELECT students.name, COUNT(*) as total_enrollments
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    GROUP BY students.name
    HAVING COUNT(*) > 2
""")
print(cursor.fetchall())

# 5. Data consistency check - every enrollment should have a valid grade
valid_grades = ('A', 'B', 'C', 'D', 'F')
print("\n--- Enrollments with Invalid Grades ---")
cursor.execute("""
    SELECT id, student_id, grade
    FROM enrollments
    WHERE grade NOT IN ('A', 'B', 'C', 'D', 'F')
    OR grade IS NULL
""")
print(cursor.fetchall())

# 6. Summary health check - counts across all tables
print("\n--- Database Health Summary ---")
cursor.execute("SELECT COUNT(*) FROM students")
print(f"Total students: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM students WHERE gpa IS NULL")
print(f"Students missing GPA: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM students WHERE city IS NULL")
print(f"Students missing city: {cursor.fetchone()[0]}")

cursor.execute("""
    SELECT COUNT(*) FROM enrollments
    LEFT JOIN courses ON enrollments.course_id = courses.id
    WHERE courses.id IS NULL
""")
print(f"Enrollments with invalid course: {cursor.fetchone()[0]}")

cursor.execute("""
    SELECT COUNT(*) FROM (
        SELECT student_id, course_id
        FROM enrollments
        GROUP BY student_id, course_id
        HAVING COUNT(*) > 1
    )
""")
print(f"Duplicate enrollments: {cursor.fetchone()[0]}")

conn.close()
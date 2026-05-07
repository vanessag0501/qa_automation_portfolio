import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 1. Subquery - students with above average GPA
print("--- Students with Above Average GPA ---")
cursor.execute("""
    SELECT name, gpa
    FROM students
    WHERE gpa > (SELECT AVG(gpa) FROM students)
""")
print(cursor.fetchall())

# 2. Subquery - students enrolled in 'Test Automation'
print("\n--- Students enrolled in Test Automation ---")
cursor.execute("""
    SELECT name
    FROM students
    WHERE id IN (
        SELECT student_id FROM enrollments
        WHERE course_id = (
            SELECT id FROM courses WHERE title = 'Test Automation'
        )
    )
""")
print(cursor.fetchall())

# 3. Subquery - courses with more than average enrollments
print("\n--- Courses with More Than Average Enrollments ---")
cursor.execute("""
    SELECT title
    FROM courses
    WHERE id IN (
        SELECT course_id
        FROM enrollments
        GROUP BY course_id
        HAVING COUNT(*) > (
            SELECT AVG(course_count)
            FROM (
                SELECT COUNT(*) as course_count
                FROM enrollments
                GROUP BY course_id
            )
        )
    )
""")
print(cursor.fetchall())

# 4. NULL handling - students missing a GPA
print("\n--- Students Missing GPA ---")
cursor.execute("""
    SELECT name
    FROM students
    WHERE gpa IS NULL
""")
print(cursor.fetchall())

# 5. NULL handling - replace NULL gpa with 0.0 for display
print("\n--- All Students GPA (NULL shown as 0.0) ---")
cursor.execute("""
    SELECT name, COALESCE(gpa, 0.0) as gpa
    FROM students
""")
print(cursor.fetchall())

# 6. NULL handling - students where gpa is not null, ordered
print("\n--- Students with Valid GPA only ---")
cursor.execute("""
    SELECT name, gpa
    FROM students
    WHERE gpa IS NOT NULL
    ORDER BY gpa DESC
""")
print(cursor.fetchall())

# 7. Subquery - students who got a better grade than average in any course
print("\n--- Students who earned an A in a CS course ---")
cursor.execute("""
    SELECT DISTINCT students.name
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    INNER JOIN courses ON enrollments.course_id = courses.id
    WHERE enrollments.grade = 'A'
    AND courses.department = 'Computer Science'
""")
print(cursor.fetchall())

#8. Find students whose GPA is above the average GPA of students in Tampa
print("\n--- Students with GPA above average GPA of Tampa students ---")
cursor.execute("""
    SELECT name, gpa
    FROM students
    WHERE gpa > (
        SELECT AVG(gpa)
        FROM students
        WHERE city = 'Tampa'
    )
""")
print(cursor.fetchall())

#9. Find students who are NOT enrolled in 'Introduction to QA' (hint: use NOT IN with a subquery)
print("\n--- Students NOT enrolled in Introduction to QA ---")
cursor.execute("""
    SELECT name
    FROM students
    WHERE id NOT IN (
        SELECT student_id
        FROM enrollments
        WHERE course_id = (
            SELECT id
            FROM courses
            WHERE title = 'Introduction to QA'
        )
    )
""")
print(cursor.fetchall())

#10. Show all students with their GPA, but replace NUILL with the text 'Not Recorded' using COALESCE
print("\n--- All Students with GPA (NULL as 'Not Recorded') ---")
cursor.execute("""
               Select name, COALESCE(gpa, 'Not Recorded') as gpa
               From students
               """)
print(cursor.fetchall())
conn.close()
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 1. INNER JOIN - students with their enrolled courses
print("--- Students and Their Courses ---")
cursor.execute("""
    SELECT students.name, courses.title
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    INNER JOIN courses ON enrollments.course_id = courses.id
""")
print(cursor.fetchall())

# 2. INNER JOIN with grade
print("\n--- Students, Courses and Grades ---")
cursor.execute("""
    SELECT students.name, courses.title, enrollments.grade
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    INNER JOIN courses ON enrollments.course_id = courses.id
    ORDER BY students.name
""")
print(cursor.fetchall())

# 3. COUNT courses per student by name
print("\n--- Number of Courses per Student ---")
cursor.execute("""
    SELECT students.name, COUNT(*) as total_courses
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    GROUP BY students.name
    ORDER BY total_courses DESC
""")
print(cursor.fetchall())

# 4. LEFT JOIN - all students even if not enrolled
print("\n--- All Students and Their Courses (including unenrolled) ---")
cursor.execute("""
    SELECT students.name, courses.title
    FROM students
    LEFT JOIN enrollments ON students.id = enrollments.student_id
    LEFT JOIN courses ON enrollments.course_id = courses.id
""")
print(cursor.fetchall())

# 5. Find students with a grade of A and what course they got it in
print("\n--- Students who earned an A ---")
cursor.execute("""
    SELECT students.name, courses.title, enrollments.grade
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    INNER JOIN courses ON enrollments.course_id = courses.id
    WHERE enrollments.grade = 'A'
""")
print(cursor.fetchall())

# 6. Average GPA of students enrolled in each course
print("\n--- Average Student GPA per Course ---")
cursor.execute("""
    SELECT courses.title, ROUND(AVG(students.gpa), 2) as avg_gpa
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    INNER JOIN courses ON enrollments.course_id = courses.id
    GROUP BY courses.title
    ORDER BY avg_gpa DESC
""")
print(cursor.fetchall())

#7. Get each student's name and the total credits they're 
# enrolled in (you'll need to join all three tables and SUM the credits)
print("\n--- Total Credits per Student ---")
cursor.execute("""
    SELECT students.name, SUM(courses.credits) as total_credits
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    INNER JOIN courses ON enrollments.course_id = courses.id
    GROUP BY students.name
    ORDER BY total_credits DESC
""")
print(cursor.fetchall())

#8.Find all students who received a grade of 'D' — show their name, course, 
# and city
print("\n--- Students who received a D ---")
cursor.execute("""
    SELECT students.name, courses.title, students.city
    FROM enrollments
    INNER JOIN students ON enrollments.student_id = students.id
    INNER JOIN courses ON enrollments.course_id = courses.id
    WHERE enrollments.grade = 'D'
""")
print(cursor.fetchall())

#9.Find any courses that have no enrollments (hint: LEFT JOIN from courses to
#  enrollments, then look for NULLs)
print("\n--- Courses with No Enrollments ---")
cursor.execute("""
    SELECT courses.title
    FROM courses
    LEFT JOIN enrollments ON courses.id = enrollments.course_id
    WHERE enrollments.id IS NULL
""")
print(cursor.fetchall())

conn.close()
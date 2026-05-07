import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 1. Count all students
print("--- Total Students ---")
cursor.execute("SELECT COUNT(*) FROM students")
print(cursor.fetchone())

# 2. Count students with a GPA (excludes NULLs automatically)
print("\n--- Students with GPA on record ---")
cursor.execute("SELECT COUNT(gpa) FROM students")
print(cursor.fetchone())

# 3. Average GPA (excludes NULLs automatically)
print("\n--- Average GPA ---")
cursor.execute("SELECT AVG(gpa) FROM students")
print(cursor.fetchone())

# 4. Highest and lowest GPA
print("\n--- Highest and Lowest GPA ---")
cursor.execute("SELECT MAX(gpa), MIN(gpa) FROM students")
print(cursor.fetchone())

# 5. Count students per city
print("\n--- Students per City ---")
cursor.execute("SELECT city, COUNT(*) FROM students GROUP BY city")
print(cursor.fetchall())

# 6. Average GPA per city
print("\n--- Average GPA per City ---")
cursor.execute("SELECT city, ROUND(AVG(gpa), 2) FROM students GROUP BY city")
print(cursor.fetchall())

# 7. Cities with more than 1 student
print("\n--- Cities with more than 1 student ---")
cursor.execute("""
    SELECT city, COUNT(*) as student_count
    FROM students
    GROUP BY city
    HAVING COUNT(*) > 1
""")
print(cursor.fetchall())

# 8. Number of enrollments per student
print("\n--- Enrollments per Student ---")
cursor.execute("""
    SELECT student_id, COUNT(*) as total_courses
    FROM enrollments
    GROUP BY student_id
""")
print(cursor.fetchall())

#9. Count how many enrollments have a grade of A
print("\n--- Enrollments with grade A ---")
cursor.execute("""
    SELECT COUNT(*) FROM enrollments WHERE grade = 'A'
""")
print(cursor.fetchone())

#10. Total credits available across all courses using SUM
print("\n--- Total Credits Available ---")
cursor.execute("""
    SELECT SUM(credits) FROM courses
 """)
print(cursor.fetchone())

#11. Average GPA per city for students with GPA above 3.0
print("\n--- Average GPA per City for students with GPA > 3.0 ---")
cursor.execute("""
    SELECT city, ROUND(AVG(gpa), 3) FROM students GROUP BY city HAVING AVG(gpa) > 3.0
""")
print(cursor.fetchall())
conn.close()
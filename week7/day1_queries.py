import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 1. Get all students
print("--- All Students ---")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# 2. Get only name and city
print("\n--- Name and City ---")
cursor.execute("SELECT name, city FROM students")
print(cursor.fetchall())

# 3. Students from Orlando only
print("\n--- Orlando Students ---")
cursor.execute("SELECT name, city FROM students WHERE city = 'Orlando'")
print(cursor.fetchall())

# 4. Students with GPA above 3.5
print("\n--- High GPA Students ---")
cursor.execute("SELECT name, gpa FROM students WHERE gpa > 3.5")
print(cursor.fetchall())

# 5. Students ordered by GPA descending
print("\n--- Students by GPA (highest first) ---")
cursor.execute("SELECT name, gpa FROM students ORDER BY gpa DESC")
print(cursor.fetchall())

# 6. Top 3 students by GPA
print("\n--- Top 3 Students ---")
cursor.execute("SELECT name, gpa FROM students ORDER BY gpa DESC LIMIT 3")
print(cursor.fetchall())

# 7. Students from Orlando OR Tampa
print("\n--- Orlando or Tampa ---")
cursor.execute("SELECT name, city FROM students WHERE city IN ('Orlando', 'Tampa')")
print(cursor.fetchall())

#8. get the name and age of all students young than 23
print("\n--- Students younger than 23 ---")
cursor.execute("SELECT name, age FROM students WHERE age < 23")
print(cursor.fetchall())

#9. Get all students from Miami
print("\n--- Students from Miami ---")
cursor.execute("SELECT name, city FROM students WHERE city = 'Miami'")
print(cursor.fetchall())

#Get name and gpa of the bottom 2 students by gpa - exclude NULLS
print("\n--- Bottom 2 Students by GPA ---")
cursor.execute("SELECT name, gpa FROM students WHERE gpa IS NOT NULL ORDER BY gpa ASC LIMIT 2")
print(cursor.fetchall())




conn.close()
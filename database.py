# import sqlite3


# def create_table():
#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER,
#         course TEXT
#     )
#     """)

#     conn.commit()
#     conn.close()


# def add_student(student_id, name, age, course):
#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     try:
#         cursor.execute("""
#         INSERT INTO students (id, name, age, course)
#         VALUES (?, ?, ?, ?)
#         """, (student_id, name, age, course))

#         conn.commit()
#         print("Student added successfully!")

#     except sqlite3.IntegrityError:
#         print("Student ID already exists.")

#     conn.close()


# def view_students():
#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM students")

#     students = cursor.fetchall()

#     if students:
#         print("\n" + "=" * 60)
#         print("                     ALL STUDENTS")
#         print("=" * 60)

#         print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Course':<20}")
#         print("-" * 60)

#         for student in students:
#             print(
#                 f"{student[0]:<10}"
#                 f"{student[1]:<20}"
#                 f"{student[2]:<10}"
#                 f"{student[3]:<20}"
#                 )

#         print("=" * 60)

#     else:
#         print("\nNo students found.")

#     conn.close()


# def search_student_by_id(student_id):
#     print("\n" + "=" * 60)
#     print("             SEARCH STUDENT")
#     print("=" * 60)

#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT * FROM students
#     WHERE id = ?
#     """, (student_id,))

#     student = cursor.fetchone()

#     if student:
#         print("\nSTUDENT FOUND!")
#         print("-" * 60)
#         print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Course':<20}")
#         print("-" * 60)

#         print(
#             f"{student[0]:<10}"
#             f"{student[1]:<20}"
#             f"{student[2]:<10}"
#             f"{student[3]:<20}"
#         )

#         print("=" * 60)

#     else:
#         print("\nStudent not found.")
#         print("=" * 60)

#     conn.close()


# def search_student_by_name(name):
#     print("\n" + "=" * 60)
#     print("             SEARCH STUDENTS")
#     print("=" * 60)

#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT * FROM students
#     WHERE name LIKE ?
#     """, (f"%{name}%",))

#     students = cursor.fetchall()

#     if students:
#         print(f"\nStudents matching '{name}':")
#         print("-" * 60)

#         print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Course':<20}")
#         print("-" * 60)

#         for student in students:
#             print(
#                 f"{student[0]:<10}"
#                 f"{student[1]:<20}"
#                 f"{student[2]:<10}"
#                 f"{student[3]:<20}"
#             )

#         print("=" * 60)

#     else:
#         print("\nNo students found.")

#     conn.close()
    


# def update_student(student_id, new_name, new_age,        new_course):
#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     UPDATE students
#     SET name = ?, age = ?, course = ?
#     WHERE id = ?
#     """, (new_name, new_age, new_course, student_id))

#     if cursor.rowcount >0:
#         print("Student updated successfully!")
#     else:
#         print("Student not found.")

#     conn.commit()
#     conn.close()



# def delete_student(student_id):
#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute(""" 
#     DELETE FROM students
#     WHERE id = ?
#     """, (student_id,))

#     if cursor.rowcount >0:
#         print("Student deleted successfully!")
#     else:
#         print("Student not found.")

#     conn.commit()
#     conn.close()


# def student_exists(student_id):
#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT id FROM students
#     WHERE id = ?
#     """, (student_id,))

#     student = cursor.fetchone()

#     conn.close()

#     return student is not None
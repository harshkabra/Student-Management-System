# # from fastapi import FastAPI, HTTPException, status
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import sqlite3


# app = FastAPI()

# #iska meaning dekh lena
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )


# class Student(BaseModel):
#     id: int
#     name: str
#     age: int
#     course: str




# @app.get("/")
# def home():
#     return {
#         "message": "Student Management System API is running"
#     }




# @app.get("/students")
# def get_students():

#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM students")

#     students = cursor.fetchall()

#     conn.close()

#     return students



# @app.get("/students/{student_id}")
# def get_student(student_id: int):

#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     SELECT * FROM students
#     WHERE id = ?
#     """, (student_id,))

#     student = cursor.fetchone()

#     conn.close()

#     if student:
#         return {
#             "id": student[0],
#             "name": student[1],
#             "age": student[2],
#             "course": student[3]
#         }

#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Student not found"
#     )



# @app.post("/students", status_code=status.HTTP_201_CREATED)
# def add_student(student: Student):

#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     try:

#         cursor.execute("""
#         INSERT INTO students (id, name, age, course)
#         VALUES (?, ?, ?, ?)
#         """, (
#             student.id,
#             student.name,
#             student.age,
#             student.course
#         ))

#         conn.commit()

#         return {
#             "message": "Student added successfully",
#             "student": student
#         }

#     except sqlite3.IntegrityError:

#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="Student ID already exists"
#         )

#     finally:
#         conn.close()



# @app.put("/students/{student_id}")
# def update_student(student_id: int, student: Student):

#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     UPDATE students
#     SET name = ?, age = ?, course = ?
#     WHERE id = ?
#     """, (
#         student.name,
#         student.age,
#         student.course,
#         student_id
#     ))

#     if cursor.rowcount == 0:

#         conn.close()

#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Student not found"
#         )

#     conn.commit()
#     conn.close()

#     return {
#         "message": "Student updated successfully",
#         "student": {
#             "id": student_id,
#             "name": student.name,
#             "age": student.age,
#             "course": student.course
#         }
#     }



# @app.delete("/students/{student_id}")
# def delete_student(student_id: int):

#     conn = sqlite3.connect("student.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     DELETE FROM students
#     WHERE id = ?
#     """, (student_id,))

#     if cursor.rowcount == 0:

#         conn.close()

#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Student not found"
#         )

#     conn.commit()
#     conn.close()

#     return {
#         "message": "Student deleted successfully"
#     }


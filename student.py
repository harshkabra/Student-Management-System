# students = []


# def get_student_id():
#     while True:
#         try:
#             student_id = int(input("Enter student ID: "))

#             if student_id <= 0:
#                 print("ID must be greater than 0. ")
#                 continue

#             return student_id

#         except ValueError:
#             print("Please eneter a valid number.")


# def get_student_name():
#     while True:
#         name = input("Enter student name: ").strip()

#         if name == "":
#             print("Student name cannot be empty.")
#         else:
#             return name


# def get_student_age():
#     while True:
#         try:
#             age = int(input("Enter Age: "))

#             if age <= 0:
#                 print("Age must be greater than 0.")
#                 continue

#             return age 

#         except ValueError:
#             print("Please enter a valid age")


# def get_student_course():
#     while True:
#         course = input("Enter Course: ").strip()

#         if course == "":
#             print("Course cannot be empty.")
#         else:
#             return course

# #Add Student
# def add_student():
#     print("\n--- Add Student ---")

#     student_id = get_student_id()

#     # check duplicate ID

#     for student in students:
#         if student.student_id == student_id:
#             print("Student ID already exists!")
#             return

#     name = get_student_name()
#     age = get_student_age()
#     course = get_student_course()

#     student = Student(student_id, name, age, course)

#     students.append(student)

#     print("Student added successfully")

 
# #View students
# def view_students():
#     print("\n--- All Students ---")

#     if len(students) == 0:
#         print("No students found.")
#         return

#     for student in students:
#         student.display()
#         print("-----------------------")


# #Search student
# def search_students():
#     print("\n--- Search Student ---")

#     student_id = get_student_id()

#     for student in students:
#         if student.student_id == student_id:
#             print("\nStudent Found")
#             student.display()
#             return

#     print("Student not found.")


# # Update Student
# def update_student():
#     print("\n--- Update Student ---")

#     student_id = get_student_id()

#     for student in students:
#         if student.student_id == student_id:

#             print("\nCurrent Details:")
#             student.display()

#             new_name = input(
#                 "Enter new name (press Enter to keep old name): "
#             ).strip()

#             if new_name != "":
#                 student.update_name(new_name)

#             new_age = input(
#                 "Enter new age (press Enter to keep old age): "
#             ).strip()

#             if new_age != "":
#                 try:
#                     new_age = int(new_age)

#                     if new_age > 0:
#                         student.set_age(new_age)
#                     else:
#                         print("Age must be greater than 0.")

#                 except ValueError:
#                     print("Invalid age.")

#             new_course = input(
#                 "Enter new course (press Enter to keep old course): "
#             ).strip()

#             if new_course != "":
#                 student.update_course(new_course)

#             print("Student updated successfully")
#             return

#     print("Student not found.")


# #Delete student
# def delete_student():
#     print("\n--- Delete Student ---")

#     student_id = get_student_id()

#     for student in students:

#         if student.student_id == student_id:

#             student.display()

#             confirm = input(
#                 "Are you sure you want to delete this student? (y/n):"
#             ).strip().lower()

#             if confirm == "y":
#                 student.remove(student)
#                 print("Student deleted successfully")
#             else:
#                 print("Student deletion cancelled.")

#             return

#     print("Student not found.")

# from database import (
#     create_table,
#     add_student,
#     view_students,
#     search_student_by_id,
#     search_student_by_name,
#     update_student,
#     delete_student,
#     student_exists
# )

# def get_student_details(is_update=False):

#     if is_update:
#         name  = input("Enter new name: ")
#     else:
#         name = input("Enter student name: ")

#     if not name.strip():
#         print("Name cannot be empty.")
#         return None

#     try:
#         if is_update:
#             age = int(input("Enter new age: "))
#         else:
#             age = int(input("Enter student age: "))

#         if age <= 0:
#             print("Age must be greater than 0.")
#             return None

#     except ValueError:
#         print("Please enter a valid age.")
#         return None

#     if is_update:
#         course = input("Enter new course: ")
#     else:
#         course = input("Enter student course:")

#     if not course.strip():
#         print("Course cannot be empty.")
#         return None

#     return name, age, course


# def main():

#     create_table()

#     while True:

#         print("\n===================================")
#         print("     Student Management System     ")
#         print("===================================")

#         print("1. Add student")
#         print("2. View All Students")
#         print("3. Search Student")
#         print("4. Update Student")
#         print("5. Delete Student")
#         print("6. Exit")

#         choice = input("\nEnter your choice: ") 

#         if choice == "1":

#             try:
#                 student_id = int(input("Enter student ID: "))

#                 if student_exists(student_id):
#                     print("Student ID already exists.")
#                     continue

#                 student_details = get_student_details()

#                 if student_details is None:
#                     continue

#                 name, age, course = student_details

#                 add_student(student_id, name, age, course)

#             except ValueError:
#                 print("Please enter a valid number for ID and age")

#         elif choice == "2":

#             view_students()

#         elif choice == "3":

#             print("\n1. Search by ID")
#             print("2. Search by Name")

#             search_choice = input("Enter your choice: ")

#             if search_choice == "1":

#                 try:
#                     student_id = int(input("Enter student ID: "))
#                     search_student_by_id(student_id)

#                 except ValueError:
#                     print("Please enter a valid student ID. ")

#             elif search_choice == "2":

#                 name = input("Enter student name:")

#                 if not name.strip():
#                     print("Name cannot be empty.")
#                     continue

#                 search_student_by_name(name)

#             else:
#                 print("Invalid search option.")

#         elif choice == "4":

#             try:
#                 student_id = int(input("Enter student ID: "))

#                 if not student_exists(student_id):
#                     print("Student not found.")
#                     continue

#                 student_details = get_student_details(is_update=True)

#                 if student_details is None:
#                     continue

#                 new_name, new_age, new_course = student_details

#                 update_student(student_id, new_name, new_age, new_course)

#             except ValueError:
#                 print("Please enter a valid number for ID and age. ")
            

#         elif choice == "5":

#             try:
#                 student_id = int(input("Enter student ID: "))

#                 if not student_exists(student_id):
#                     print("Student not found.")
#                     continue

#                 confirm = input("Are you sure you want to delete this student? (y/n):")

#                 if confirm.lower() == "y":
#                     delete_student(student_id)
#                 elif confirm.lower() == "n":
#                     print("Delete cancelled.")
#                 else:
#                     print("Please enter y or n.")

#             except ValueError:
#                 print("Please enter a valid student ID. ")


#         elif choice == "6":
#             print("\nThank you!")
#             break
            
#         else:
#             print("Invalid option! please choose between 1 and 6.")

# if __name__ == "__main__":
#     main()

class Student:

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.__age = age
        self.course = course

    # Display student
    def display(self):
        print("ID", self.student_id)
        print("Name", self.name)
        print("Age", self.get_age())
        print("Course", self.course)

    # Getter
    def get_age(self):
        return self.__age

    # Setter
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
            print("Age updated successfully")
        else:
            print("Invalid age")

    # Update name
    def update_name(self, new_name):
        if new_name != "":
            self.name = new_name
            print("Name updated successfully")
        else:
            print("Name cannot be empty")

    # Update course
    def update_course(self, new_course):
        if new_course != "":
            self.course = new_course
            print("Course cannot be empty")
from app.database.queries import (
    student_exists,
    add_student,
    get_all_students,
    search_student_by_id,
    search_student_by_name,
    update_student,
    delete_student
)


def create_student(student_id, name, age, course):
    if student_exists(student_id):
        return False

    add_student(student_id, name, age, course)
    return True


def get_students():
    return get_all_students()


def get_student(student_id):
    return search_student_by_id(student_id)


def search_students_by_name(name):
    return search_student_by_name(name)


def update_student_details(student_id, name, age, course):
    return update_student(
        student_id,
        name,
        age,
        course
    )


def remove_student(student_id):
    return delete_student(student_id)
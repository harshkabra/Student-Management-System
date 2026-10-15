from .connection import get_connection


def student_exists(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    return student is not None


def add_student(student_id, name, age, course):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students (id, name, age, course)
        VALUES (?, ?, ?, ?)
        """,
        (student_id, name, age, course)
    )

    conn.commit()
    conn.close()


def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, age, course FROM students"
    )

    students = cursor.fetchall()

    conn.close()

    return students


def search_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, age, course
        FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    return student


def search_student_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, name, age, course
        FROM students
        WHERE name LIKE ?
        """,
        (f"%{name}%",)
    )

    students = cursor.fetchall()

    conn.close()

    return students


def update_student(student_id, name, age, course):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name = ?, age = ?, course = ?
        WHERE id = ?
        """,
        (name, age, course, student_id)
    )

    conn.commit()

    rows_updated = cursor.rowcount

    conn.close()

    return rows_updated


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    rows_deleted = cursor.rowcount

    conn.close()

    return rows_deleted
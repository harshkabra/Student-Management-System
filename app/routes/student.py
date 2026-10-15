from fastapi import APIRouter, HTTPException, status

from app.schemas.student import StudentCreate, StudentResponse
from app.services.student_services import (
    create_student,
    get_students,
    get_student,
    search_students_by_name,
    update_student_details,
    remove_student
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Get all students
@router.get("/", response_model=list[StudentResponse])
def get_all_students():
    students = get_students()

    return [
        {
            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3]
        }
        for student in students
    ]


# Get student by ID
@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int):

    student = get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "id": student[0],
        "name": student[1],
        "age": student[2],
        "course": student[3]
    }


# Add student
@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def add_new_student(student: StudentCreate):

    created = create_student(
        student.id,
        student.name,
        student.age,
        student.course
    )

    if not created:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student ID already exists"
        )

    return student


# Search student by name
@router.get("/search/name/{name}")
def search_by_name(name: str):

    students = search_students_by_name(name)

    return [
        {
            "id": student[0],
            "name": student[1],
            "age": student[2],
            "course": student[3]
        }
        for student in students
    ]


# Update student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate):

    existing_student = get_student(student_id)

    if existing_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    update_student_details(
        student_id,
        student.name,
        student.age,
        student.course
    )

    return {
        "id": student_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }


# Delete student
@router.delete("/{student_id}")
def delete_student(student_id: int):

    existing_student = get_student(student_id)

    if existing_student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    remove_student(student_id)

    return {
        "message": "Student deleted successfully"
    }
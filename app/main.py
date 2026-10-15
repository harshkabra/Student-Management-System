from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import create_table
from app.routes.student import router as student_router

app = FastAPI(
    title="Student Management System API"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database table
create_table()


# Include student routes
app.include_router(student_router)


@app.get("/")
def root():
    return {
        "message": "Student Management System API is running"
    }
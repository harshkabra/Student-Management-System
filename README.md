# Student Management System

A full-stack Student Management System built using **Python, OOP, SQLite, FastAPI, HTML, CSS, and JavaScript**.

## Project Description

This project started as a basic Python command-line Student Management System and was gradually developed into a complete full-stack application.

The system allows users to manage student information such as:

* Student ID
* Student Name
* Age
* Course

The project was created to practice Python programming, Object-Oriented Programming, database management, API development, and frontend development.

## Features

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Student ID validation
7. Duplicate Student ID handling
8. Database persistence
9. Frontend form for adding students
10. Frontend table for displaying students
11. Edit and update students from the frontend
12. Delete students from the frontend
13. Search students from the frontend
14. API error and status handling

## Technologies Used

* **Python** – Backend programming
* **Object-Oriented Programming (OOP)** – Student class and methods
* **SQLite** – Database storage
* **FastAPI** – REST API development
* **Pydantic** – API request data validation
* **HTML** – Frontend structure
* **CSS** – Frontend styling and UI design
* **JavaScript** – Frontend logic and API communication

## Project Structure

```text
Student_Managment_System/
│
├── main.py
├── student.py
├── database.py
├── api.py
├── student.db
│
├── index.html
├── style.css
├── script.js
│
└── README.md
```

## Backend

The backend was developed using Python and FastAPI.

The API provides endpoints for:

* Getting the API status
* Getting all students
* Getting a student by ID
* Adding a student
* Updating a student
* Deleting a student

The API communicates with the SQLite database to store and manage student records.

## Database

SQLite is used as the database for the project.

The `students` table contains:

* `id` – Student ID
* `name` – Student Name
* `age` – Student Age
* `course` – Student Course

The Student ID is used as the primary key to prevent duplicate student records.

## Frontend

The frontend is built using:

* HTML
* CSS
* JavaScript

The frontend communicates with the FastAPI backend using HTTP requests.

Users can:

* Add students
* View students
* Search students
* Edit students
* Delete students

## Python Concepts Used

* Variables
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* User Input
* Type Casting
* Exception Handling (`try-except`)
* String Methods
* Return Statements
* Modules and Imports
* Classes and Objects
* Encapsulation
* Private Variables
* Getters and Setters
* CRUD Operations
* SQLite Database Connectivity

## API Concepts Used

* REST API
* HTTP methods
* GET
* POST
* PUT
* DELETE
* JSON data
* Pydantic models
* HTTP status codes
* Error handling
* API request and response handling

## Testing Completed

The project was tested end-to-end.

The following operations were successfully tested:

* Add Student
* View Students
* Database persistence after page refresh
* Edit/Update Student
* Delete Student
* Search Student
* Invalid numeric Student ID handling
* Duplicate Student ID handling
* API testing
* Database testing
* Frontend/UI testing
* Complete system testing

## How to Run

### 1. Open the project folder

Open the terminal and move into the project directory:

```bash
cd /home/gwl/Documents/Student_Managment_System/
```

### 2. Start the FastAPI server

Run:

```bash
uvicorn api:app --reload
```

The API will normally start at:

```text
http://127.0.0.1:8000
```

### 3. Open the frontend

Open `index.html` in your browser.

Make sure the FastAPI server is running while using the frontend, because the JavaScript frontend communicates with the API.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/students` | Get all students |
| GET | `/students/{student_id}` | Get a student by ID |
| POST | `/students` | Add a student |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Project Purpose

The main purpose of this project is to understand how different technologies work together in a real-world application.

The project helped me practice:

**Python → OOP → SQLite → FastAPI → HTML/CSS → JavaScript → API Integration → Testing**

It also demonstrates how a simple command-line Python project can be developed step by step into a complete full-stack Student Management System.

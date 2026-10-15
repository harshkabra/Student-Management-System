import sqlite3

DATABASE_NAME = "student.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
    """)

    conn.commit()
    conn.close()
import sqlite3
from contextlib import contextmanager

DB_PATH = "specimen_data.db"

@contextmanager
def db_connection():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    with db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS specimens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                microscope_size REAL NOT NULL,
                magnification REAL NOT NULL,
                real_size REAL NOT NULL
            )
        """)

def save_specimen(username: str, microscope_size: float, magnification: float, real_size: float):
    with db_connection() as conn:
        conn.execute("""
            INSERT INTO specimens (username, microscope_size, magnification, real_size)
            VALUES (?, ?, ?, ?)
        """, (username, microscope_size, magnification, real_size))

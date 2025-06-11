from flask import Flask, render_template, request
# from core import calculate_real_size
# from db.database import save_specimen, init_db

def calculate_real_size(microscope_size, magnification):
    if magnification <= 0:
        raise ValueError("Magnification must be greater than 0")
    return microscope_size / magnification
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


app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    context = {"result": None, "error": None}

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        size_input = request.form.get("size", "")
        magnification_input = request.form.get("magnification", "")

        try:
            size = float(size_input)
            magnification = float(magnification_input)
            real_size = calculate_real_size(size, magnification)
            save_specimen(username, size, magnification, real_size)
            context["result"] = f"{real_size:.2f}"
        except Exception as e:
            context["error"] = str(e)

    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True)

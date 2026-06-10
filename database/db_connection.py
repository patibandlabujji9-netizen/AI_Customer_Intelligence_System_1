# database/db_connection.py

import sqlite3
from pathlib import Path

# Database file path
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "sales_forecasting.db"


def get_connection():
    """
    Create and return SQLite database connection.
    """

    conn = sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )

    conn.row_factory = sqlite3.Row

    return conn


def test_connection():
    """
    Test database connection.
    """

    try:
        conn = get_connection()
        conn.close()
        return True

    except Exception as e:
        print(f"Database Error: {e}")
        return False


if __name__ == "__main__":

    if test_connection():
        print("Database Connected Successfully")
    else:
        print("Database Connection Failed")
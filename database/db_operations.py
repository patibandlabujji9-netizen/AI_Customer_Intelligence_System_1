import sqlite3

DB_PATH = "database/customer_analytics.db"

def insert_customer(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers (id, age, income, score, gender, subscribed, churn)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


def fetch_all():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    conn.close()
    return rows
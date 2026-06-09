import sqlite3

conn = sqlite3.connect("database/customer_analytics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    age INTEGER,
    income REAL,
    score INTEGER,
    gender TEXT,
    subscribed INTEGER,
    churn INTEGER
)
""")

conn.commit()
conn.close()

print("Database created successfully")
"""
db_utils.py
------------
Handles database operations such as connection management,
table creation, and data insertion.
"""

import sqlite3
from utils.logger import Logger


class Database:
    """Manages SQLite database connections and operations."""

    def __init__(self, db_name="data_pipeline.db"):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def create_table(self):
        """Creates a simple sales data table if not exists."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT,
                product TEXT,
                revenue REAL,
                quantity INTEGER,
                date TEXT
            )
        """)
        self.conn.commit()
        Logger.log("Database table 'sales' ready.")

    def insert_data(self, data):
        """Inserts a list of tuples into the sales table."""
        self.cursor.executemany(
            "INSERT INTO sales (region, product, revenue, quantity, date) VALUES (?, ?, ?, ?, ?)", data
        )
        self.conn.commit()
        Logger.log(f"Inserted {len(data)} rows into the database.")

    def query(self, query_str):
        """Executes a SELECT query and returns DataFrame-like list of tuples."""
        self.cursor.execute(query_str)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        Logger.log("Database connection closed.")


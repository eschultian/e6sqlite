import sqlite3


def create_database():
    with sqlite3.connect('data/cafe.sqlite') as s3:
        s3.execute("""CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT, 
            cost_1b REAL
        )
        """)


import sqlite3
connection = sqlite3.connect("mysql_database.db")

cursor = connection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS employees(
    id INTERGER(16),
    name VARCHER(32),
    department VARCHER(32),
    phone VARCHER(32),
    email VARCHER(32)
    );
"""
cursor.execute(sql)

connection.commit()
connection.close()
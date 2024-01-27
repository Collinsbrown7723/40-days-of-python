import sqlite3

connection = sqlite3.connect("mysql_database.db")
cursor = connection.cursor()
id = input("Enter id:")
sql = """
    UPDATE employees SET name = "Rick c137" where id =?
"""
cursor.execute(sql,(id,))
connection.commit()
connection.close()
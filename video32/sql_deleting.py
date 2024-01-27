import sqlite3

connection = sqlite3.connect("mysql_database.db")
cursor = connection.cursor()
# id = input("Enter id:")

# sql = " DELETE FROM employees where id = ?"
sql = "DELETE FROM employees WHERE department = 'EET'"
cursor.execute(sql)

connection.commit()
connection.close()
import sqlite3

connection = sqlite3.connect("mysql_database.db")
cursor = connection.cursor()
# id = input("Enter id:")

# sql = " SELECT * FROM employees where id > ?"

# cursor.execute(sql,(id,))
record = (10,"dada","farming","23333323","eadsa@gmail.com")

sql = "INSERT INTO employees VALUES(?,?,?,?,?)"
cursor.execute(sql,record)
connection.commit()
connection.close()

# for row in cursor.fetchall():
#     print(row)
import sqlite3

connection = sqlite3.connect("mysql_database.db")

cursor = connection.cursor()

# sql = """
#     INSERT INTO employees(id,name,department,phone,email) VALUES(1,"collins","IT","+2335454044","example@gmail.com");
#     INSERT INTO employees VALUES(2,"shalom","EEE","+2334443","example2@gmail.com");
#     INSERT INTO employees VALUES(3,"ethil","EET","+23343343443","example3@gmail.com");
# """
sql = """

"""
cursor.executescript(sql)

connection.commit()
connection.close()
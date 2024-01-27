import sqlite3

connection = sqlite3.connect("mysql_database.db")
cursor = connection.cursor()

sql = """
SELECT * from employees
"""

cursor.execute(sql)

for row in cursor.fetchall():
    print(row)
    
sql = """
SELECT name, phone from employees
"""

cursor.execute(sql)   

for row in cursor:#.fetchall() this will still work because the cursor object is iterable
    print(row)
    

sql = """
SELECT * from employees where name like 'c%' order by id desc
"""

cursor.execute(sql)   

for row in cursor:#.fetchall() this will still work because the cursor object is iterable
    print(row)
sql = """
SELECT * from employees where id = 2
"""

cursor.execute(sql)   

# for row in cursor:#.fetchall() this will still work because the cursor object is iterable
#     print(row)
row = cursor.fetchone()
print(row)
connection.close()
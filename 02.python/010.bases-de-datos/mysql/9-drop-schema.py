"""
Borrar una base de datos existente
"""
import mysql.connector as con

database = con.connect(
    host="127.0.0.1",
    port="3300",
    user="root",
    password="admin"
)
cursor = database.cursor()

sql = """
DROP DATABASE IF EXISTS python_mysql;
"""
cursor.execute(sql)

sql = """
SHOW DATABASES;
"""
cursor.execute(sql)
print(cursor.fetchall())

cursor.close()
database.close()

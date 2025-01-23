"""
Borrar una tabla existente en la base de datos
"""
import mysql.connector as con

database = con.connect(
    host="127.0.0.1",
    port="3300",
    user="root",
    password="admin",
    database="python_mysql"
)
cursor = database.cursor()

sql = """
DROP TABLE IF EXISTS product;
"""
cursor.execute(sql)

sql = """
SHOW TABLES;
"""
cursor.execute(sql)
print(cursor.fetchall())

cursor.close()
database.close()

"""
Crear nueva base de datos
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
CREATE SCHEMA python_mysql 
DEFAULT CHARACTER SET utf8 ;
"""
cursor.execute(sql)


cursor.close()
database.close()

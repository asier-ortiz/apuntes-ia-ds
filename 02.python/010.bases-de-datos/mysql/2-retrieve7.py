"""
Paginación:
Recuperar los 20 primeros elementos
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
SELECT * FROM actor limit 20;
"""

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
database.close()

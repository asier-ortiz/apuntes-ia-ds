"""
Recuperar utilizando paginación: recupera los 20 elementos desde el 21 al 40

LIMIT 20  --- 1 al 20 --- Página 1
LIMIT 20, 20 -- 21 al 40 -- Página 2
LIMIT 40, 20 -- del 41 al 60 -- Página 3
LIMIT 60, 20 -- del 61 al 80 -- Página 4


"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

# El primero parámetro limit especifica el comienzo
# El segundo parámetro limit especifica el número de elementos
sql = """
SELECT * FROM actor LIMIT 20, 20;
"""

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("=================")

sql = """
SELECT * FROM actor limit 40, 20;
"""

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
database.close()

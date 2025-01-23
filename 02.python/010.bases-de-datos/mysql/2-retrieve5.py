"""
Recuperar usando parámetros en la consulta
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
SELECT * FROM actor
WHERE first_name = %s OR last_name = %s;
"""
params = ("GRACE", "BERRY")

cursor.execute(sql, params)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
database.close()

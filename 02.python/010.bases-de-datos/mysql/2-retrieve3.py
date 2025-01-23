"""
Recuperar proyecciones: recuperamos solo algunas columnas
"""
import mysql.connector as con
import datetime

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

# cursor.execute("SELECT film_id, title, release_year FROM film;")
cursor.execute("SELECT language_id, name, last_update FROM language;")

rows = cursor.fetchall()

for row in rows:
    print(row)

# 6 - Cerrar los recursos
cursor.close()
database.close()

"""
Recuperar con filtro
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

# sql = """
# SELECT * FROM actor
# WHERE first_name = 'ALAN'
# """
sql = """
SELECT * FROM film_text
WHERE description like '%Scientist%';
"""
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
database.close()

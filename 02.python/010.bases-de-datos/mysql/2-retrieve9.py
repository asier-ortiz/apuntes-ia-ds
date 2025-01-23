"""
Recuperar datos desde múltiples tablas: customer y address
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
SELECT customer_id, first_name, address, postal_code 
FROM customer c 
JOIN address a on c.address_id = a.address_id;
"""

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
database.close()

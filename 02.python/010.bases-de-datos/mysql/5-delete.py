"""
Borra datos
Borra una fila existente en la tabla customer.
Borra un cliente en base de datos
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
 DELETE FROM customer 
 WHERE customer_id = %s; 
"""
params = (601,)
cursor.execute(sql, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

"""
Borra datos
Borra múltiples filas existentes en la tabla customer.
Borra múltiples clientes en base de datos
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
DELETE FROM customer 
WHERE first_name = %s and last_name = %s; 
"""
params = ("usuario", "desactivado")
cursor.execute(sql, params)  # NOTA: no se puede borrar cuando hay dependencias

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

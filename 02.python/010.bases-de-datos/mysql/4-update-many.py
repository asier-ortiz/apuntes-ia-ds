"""
Actualiza datos
Actualiza varias filas existentes en la tabla customer.
Actualiza múltiples clientes en base de datos
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
UPDATE customer
SET first_name = %s, last_name = %s
WHERE active = %s;
"""
params = ("usuario", "desactivado", 0)
cursor.execute(sql, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

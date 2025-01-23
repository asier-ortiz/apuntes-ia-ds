"""
Insertar datos
Inserta una nueva fila en la tabla customer.
Crea un nuevo cliente en base de datos
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
INSERT INTO customer (store_id, first_name, last_name, email, address_id, active)
VALUES (%s, %s, %s, %s, %s, %s);
"""
params = (1, "JUANCITO", "RIGATUSO", "JUANCITO@sakila.org", 605, 1)
cursor.execute(sql, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

"""
Insertar datos
Inserta múltiples nuevas filas en la tabla customer.
Crea varios clientes en base de datos
"""
import mysql.connector as con

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
INSERT INTO customer (store_id, first_name, last_name, email, address_id, active)
VALUES (%s, %s, %s, %s, %s, %s);
"""
customers = [
    (1, "CUSTOMER 1", "LASTNAME1", "customer1@sakila.org", 605, 1),
    (1, "CUSTOMER 2", "LASTNAME2", "customer2@sakila.org", 605, 1),
    (1, "CUSTOMER 3", "LASTNAME3", "customer3@sakila.org", 605, 1),
    (1, "CUSTOMER 4", "LASTNAME4", "customer4@sakila.org", 605, 1),
]
cursor.executemany(sql, customers)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

"""
 CRUD - Opción 2: insertar un nuevo staff
"""
import mysql.connector as con
from models import Staff
from sql import *

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

# 1 - Leer datos de la entrada
print("Introduce los datos del nuevo staff")
first_name = input("Introduce first_name:")
last_name = input("Introduce last_name:")
address_id = input("Introduce address_id:")
email = input("Introduce email:")
store_id = input("Introduce store_id:")
active = bool(input("Introduce active:"))
username = input("Introduce username:")
password = input("Introduce password:")

# 2 - Construir objeto
staff = Staff(None, first_name, last_name, address_id, None, email, store_id, active, username, password, None)


# 3 - Insertar datos en DB
# (first_name, last_name, address_id, email, store_id, active, username, password)
params = (staff.first_name, staff.last_name, staff.address_id, staff.email, staff.store_id, staff.active,
          staff.username, staff.password)
cursor.execute(sql_insert, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

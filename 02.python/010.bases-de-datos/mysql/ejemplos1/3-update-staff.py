"""
 CRUD - Opción 3: actualizar un staff existente
"""
import mysql.connector as con
from models import Staff
from sql import *

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

result = None
staff_id = None
while result is None:
    # 1 - Leer datos de la entrada
    print("Introduce el id del staff que quieres editar:")
    staff_id = int(input("Introduce un id:"))

    # Comprobar si existe staff en base de datos:
    param_id = (staff_id,)
    cursor.execute(sql_exists, param_id)
    result = cursor.fetchone()

    if result is None:
        print("El staff seleccionado no existe. Por favor, inténtelo de nuevo.")

print("fin")

# Introduce los datos actualizados
first_name = input("Introduce first_name:")
last_name = input("Introduce last_name:")
address_id = input("Introduce address_id:")
email = input("Introduce email:")
store_id = input("Introduce store_id:")
active = bool(input("Introduce active:"))
username = input("Introduce username:")
password = input("Introduce password:")

# 2 - Construir objeto
staff = Staff(staff_id, first_name, last_name, address_id, None, email, store_id, active, username, password, None)


# 3 - Actualizar datos en DB
# SET first_name = %s, last_name = %s, address_id = %s, email = %s, store_id = %s, active = %s,
# username = %s, password = %s
# WHERE staff_id = %s;
params = (staff.first_name, staff.last_name, staff.address_id, staff.email, staff.store_id, staff.active,
          staff.username, staff.password, staff.staff_id)
cursor.execute(sql_update, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()

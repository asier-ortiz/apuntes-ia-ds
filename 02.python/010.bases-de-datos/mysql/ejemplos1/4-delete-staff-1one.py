
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


param_id = (staff_id,)
cursor.execute(sql_delete_one, param_id)
database.commit()

cursor.close()
database.close()

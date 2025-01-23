"""
 CRUD - Opción 1: recuperar un único staff por id
"""
import mysql.connector as con
from models import Staff
from sql import *

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()


staff_id = int(input("Introduce el id de staff que desea recuperar:"))
params = (staff_id,)

cursor.execute(sql_retrieve_one, params)
row = cursor.fetchone()

if row is not None:
    staff = Staff(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
    print("Resultado:")
    print(staff)
else:
    print("No se ha encontrado el staff solicitado.")

cursor.close()
database.close()

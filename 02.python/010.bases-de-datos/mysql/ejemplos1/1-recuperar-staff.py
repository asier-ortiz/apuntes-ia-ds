"""
 CRUD - Opción 1: recuperar todos los staff
"""
import mysql.connector as con
from models import Staff
from sql import *

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

cursor.execute(sql_retrieve_all)

rows = cursor.fetchall()

staffs = []
for row in rows:
    staff = Staff(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
    staffs.append(staff)

print("Listado de resultados:")
print(staffs)

cursor.close()
database.close()

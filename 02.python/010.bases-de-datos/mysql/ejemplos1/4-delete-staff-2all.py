
import mysql.connector as con
from models import Staff
from sql import *

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

cursor.execute(sql_delete_all)  # Hay foreign keys por tanto no se puede borrar así, primero hay que borrar/modificar los pagos
database.commit()

cursor.close()
database.close()

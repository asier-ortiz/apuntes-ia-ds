# 1 - Importar driver
import mysql.connector as con

# 2 - Crear conexión a base de datos específica: sakila
# Si no se especifica sql aquí hay que especificarlo en la sentencia
# ESTO PERMITE TRABAJAR CON MÁS DE UNA BASE DE DATOS A LA VEZ
database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin")

# 3 - Obtener el objeto cursor
cursor = database.cursor()

# 4 - Ejecutar sentencia SQL
cursor.execute("SELECT * FROM sakila.customer;")

# 5 - Procesar resultar de la ejecución de la sentencia SQL
customers = cursor.fetchall()
print(type(customers))
for customer in customers:
    print(customer)

cursor.execute("SELECT * FROM librarydb.book;")

# 5 - Procesar resultar de la ejecución de la sentencia SQL
films = cursor.fetchall()
for film in films:
    print(film)

# 6 - Cerrar los recursos
cursor.close()
database.close()
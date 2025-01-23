
# 1 - Importar driver
import mysql.connector as con

# 2 - Crear conexión a base de datos
database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin")

# 3 - Obtener el objeto cursor
cursor = database.cursor()

# 4 - Ejecutar sentencia SQL
cursor.execute("SHOW DATABASES;")

# 5 - Procesar resultar de la ejecución de la sentencia SQL
for database_name in cursor:
    print(database_name)

# 6 - Cerrar los recursos
cursor.close()
database.close()
# 1 - Importar driver
import mysql.connector as con

# 2 - Crear conexión a base de datos específica: sakila
database = con.connect(
    host="127.0.0.1",
    port="3300",
    user="root",
    password="admin",
    database="sakila"
)

# 3 - Obtener el objeto cursor
cursor = database.cursor()

# 4 - Ejecutar sentencia SQL
sql = "SELECT * FROM customer;"
cursor.execute(sql)

# 5 - Procesar resultar de la ejecución de la sentencia SQL
rows = cursor.fetchall()
print(type(rows))
print(type(rows[0]))

for row in rows:
    print(row[2] + " " + row[3])


# 6 - Cerrar los recursos
cursor.close()
database.close()
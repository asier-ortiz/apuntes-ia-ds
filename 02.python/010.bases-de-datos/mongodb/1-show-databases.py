# Importar driver
import pymongo

# Crear string para la conexión
# con = "mongodb://localhost:27017/"
con = "mongodb://root:password@localhost:27017/"

# Crear cliente mongo:
client = pymongo.MongoClient(con)

print(client.list_database_names())

client.close()

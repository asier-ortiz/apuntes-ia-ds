"""
Recuperar determinados campos (proyecciones) todos los documentos de una colección
"""
import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# 1 parámetro = filtro
# 2 parámetro = campos a incluir/excluir

# Ejemplo inclusión:
documents = collection.find({}, {
    "publishedDate": 1
})

for doc in documents:
    print(doc)

client.close()

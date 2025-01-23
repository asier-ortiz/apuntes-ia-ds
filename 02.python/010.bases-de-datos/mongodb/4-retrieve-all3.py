"""
Recuperar determinados campos (proyecciones) todos los documentos de una colección
"""
import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# 1 parámetro = filtro
# 2 parámetro = campos a incluir/excluir

# Ejemplo exclusión:
documents = collection.find({}, {
    "title": 0,
    "isbn": 0,
})
# ⛔ NO SE PUEDE INCLUIR/EXCLUIR A LA VEZ

for doc in documents:
    print(doc)

client.close()

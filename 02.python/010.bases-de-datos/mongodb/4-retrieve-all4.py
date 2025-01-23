"""
Recuperar determinados campos (proyecciones) todos los documentos de una colección
"""
import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# 1 parámetro = filtro
documents = collection.find({
    "pageCount": 402
})

for doc in documents:
    print(doc)

client.close()

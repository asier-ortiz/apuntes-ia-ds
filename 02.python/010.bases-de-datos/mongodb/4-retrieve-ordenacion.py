"""
Recuperar resultados paginados
limit()
skip()
"""
import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# Si no se pasa nada es ascendente
# Si se pasa -1 es descendente
# documents = collection.find({}, {"title": 1}).sort("title")  # ascendente
documents = collection.find({}, {"title": 1})\
    .sort("title", -1)

for doc in documents:
    print(doc)

client.close()

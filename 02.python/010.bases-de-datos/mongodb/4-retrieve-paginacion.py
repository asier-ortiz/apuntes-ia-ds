"""
Recuperar resultados paginados
limit()
skip()
"""
import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# limit - limita el número de resultados a recuperar
# skip - permite saltar los primeros X resultados
documents = collection.find().limit(10).skip(10)

for doc in documents:
    print(doc)

client.close()

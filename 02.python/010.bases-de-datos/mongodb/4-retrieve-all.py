"""
Recuperar todos los documentos de una colección
"""

import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

documents = collection.find()
print(documents)
print(type(documents))

for doc in documents:
    print(doc)

client.close()

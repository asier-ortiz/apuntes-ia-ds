"""
Recuperar un documento por su id normal
"""
import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# Por id normal:
documents = collection.find(
    {
        "_id": {
            "$eq": 1
        }
    },
    {
        "title": 1,
        "pageCount": 1
    },
)

for doc in documents:
    print(doc)

client.close()

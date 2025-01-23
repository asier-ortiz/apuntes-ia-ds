"""
Recuperar un documento por su objectid
"""
import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# Por objectid:
query = {
    "_id": ObjectId("53c2ae8528d75d572c06adb7")  # Filtra por ObjectId
}
projection = {
    "title": 1,
    "pageCount": 1
}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)

client.close()

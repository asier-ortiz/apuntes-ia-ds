"""
Borrar un documento existente en la colección
"""
import datetime
import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection

query = {
    "_id": ObjectId("609a567d1df8d0f60c0ea37d")
}
deleted_books = collection.delete_one(query).deleted_count

print("Se ha eliminado ", deleted_books, "libro/s")

client.close()

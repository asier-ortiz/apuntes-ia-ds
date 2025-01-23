"""
Actualizar un documento existente en la colección
"""
import datetime
import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection

# Recibe un nuevo libro como diccionario, se autogenera el id
modified_books = collection.update_one({
    "_id": ObjectId("609a567d1df8d0f60c0ea37c")  # Elegir un id que exista, si no modifica ningún documento
}, {
    "$set": {
        "status": "DESCATALOGADO",
    }
}).modified_count

print("Se ha modificado ", modified_books, "libro/s")  # ObjectId autogenerado por MongoDB

client.close()

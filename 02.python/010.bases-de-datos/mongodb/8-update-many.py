"""
Actualizar varios documentos existentes en la colección
"""
import datetime
import pymongo

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection

# Recibe un nuevo libro como diccionario, se autogenera el id
query = {
    "publishedDate": {
        "$lt": datetime.datetime(2000, 1, 1)
    }
}
update = {
    "$set": {
        "status": "DESCATALOGADO",
    }
}

modified_books = collection.update_many(query, update).modified_count

print("Se ha modificado ", modified_books, "libro/s")

client.close()

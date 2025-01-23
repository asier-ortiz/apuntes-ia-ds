"""
Insertar un nuevo documento en la colección
"""
import pymongo, datetime

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection

# Recibe un nuevo libro como diccionario, se autogenera el id
book_id = collection.insert_one({
    "isbn": "q432234324",
    "title": "dssfdsfas fsa df",
    "pageCount": 456,
    "status": "AGOTADO",
    "authors": ["Rubén", "Paulho", "Eckhart"],
    "categories": [],
    "longDescription": "dsafafd",
    "publishedDate": datetime.datetime(2021, 5, 11),
    "shortDescription": "sdfasfdsf",
    "thumbnailUrl": ""
}).inserted_id

print("Se ha insertado un nuevo libro con el id: ", book_id)  # ObjectId autogenerado por MongoDB

client.close()

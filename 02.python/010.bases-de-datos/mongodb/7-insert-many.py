"""
Insertar múltiples nuevos documentos en la colección
"""
import pymongo, datetime

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection

# Recibe un nuevo libro como diccionario, se autogenera el id
book1 = {
    "isbn": "q432234324",
    "title": "Book 1 - Ejemplo inserción múltiple",
    "pageCount": 456,
    "status": "AGOTADO",
    "authors": ["Rubén", "Paulho", "Eckhart"],
    "categories": [],
    "longDescription": "dsafafd",
    "publishedDate": datetime.datetime(2021, 5, 11),
    "shortDescription": "sdfasfdsf",
    "thumbnailUrl": ""
}
book2 = {
    "isbn": "q432234324",
    "title": "Book 2 - Ejemplo inserción múltiple",
    "pageCount": 456,
    "status": "AGOTADO",
    "authors": ["Rubén", "Paulho", "Eckhart"],
    "categories": [],
    "longDescription": "dsafafd",
    "publishedDate": datetime.datetime(2021, 5, 11),
    "shortDescription": "sdfasfdsf",
    "thumbnailUrl": ""
}
books = [book1, book2]  # Lista de diccionarios
book_ids = collection.insert_many(books).inserted_ids

print("Se han insertado múltiples libros con los ids: ", book_ids)  # ObjectId autogenerado por MongoDB

client.close()

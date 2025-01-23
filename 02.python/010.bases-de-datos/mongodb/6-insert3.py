"""
Insertar un nuevo documento en la colección
"""
import pymongo
from ejemplos.data import new_book

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection

book_id = collection.insert_one(new_book).inserted_id
print(book_id)

client.close()

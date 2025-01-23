"""
Recuperar todos los libros
"""
import pymongo
from bson import ObjectId

from models import Book
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

doc = collection.find_one({"_id": ObjectId("53c2ae8528d75d572c06adb3")})
print(doc)
print(type(doc))
if doc is not None:
    book = Book(
            doc["_id"] if "_id" in doc else None,
            doc["isbn"] if "isbn" in doc else None,
            doc["title"] if "title" in doc else None,
            doc["pageCount"] if "pageCount" in doc else None,
            doc["status"] if "status" in doc else None,
            doc["authors"] if "authors" in doc else None,
            doc["categories"] if "categories" in doc else None,
            doc["longDescription"] if "longDescription" in doc else None,
            doc["publishedDate"] if "publishedDate" in doc else None,
            doc["shortDescription"] if "shortDescription" in doc else None,
            doc["thumbnailUrl"] if "thumbnailUrl" in doc else None
        )
    print(book)

client.close()

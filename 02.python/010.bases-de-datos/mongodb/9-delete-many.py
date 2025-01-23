"""
Borrar todos los documentos de una colección
"""
import datetime
import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection
collection.drop()

client.close()

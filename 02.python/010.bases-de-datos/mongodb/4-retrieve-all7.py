"""
Recuperar determinados campos (proyecciones) todos los documentos de una colección
"""
import pymongo
import datetime
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

# 1 parámetro = filtro
# 2 parámetro proyección
query = {
    "publishedDate": {
        "$gt": datetime.datetime(1995, 1, 1, 0, 0),
        "$lt": datetime.datetime(1997, 1, 1, 0, 0)
    }
}
projection = {
        "isbn": 1,
        "publishedDate": 1
}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)

client.close()

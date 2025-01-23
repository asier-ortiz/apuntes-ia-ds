import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

library = client["library"]  # database
books = library["books"]  # collection

result = books.estimated_document_count()  # obtener número de documentos en la colección
print(result, "documentos en la base de datos library")

client.close()

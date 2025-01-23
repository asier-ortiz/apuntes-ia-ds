import pymongo
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")

database = client["library"]  # database
collection = database["books"]  # collection

result = collection.find_one()
print(result)
print(type(result))

client.close()

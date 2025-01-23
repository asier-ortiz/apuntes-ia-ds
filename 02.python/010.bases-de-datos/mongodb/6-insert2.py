"""
Insertar un nuevo documento en la colección
"""
import pymongo, datetime

client = pymongo.MongoClient("mongodb://root:password@localhost:27017/")
database = client["library"]  # database
collection = database["books"]  # collection

# Por id normal:
class Book:
    def __init__(self, _id, isbn, title, page_count, status, authors, categories, long_description,
                 published_date, short_description, thumbnail_url):
        self._id = _id
        self.isbn = isbn
        self.title = title
        self.page_count = page_count
        self.status = status
        self.authors = authors
        self.categories = categories
        self.long_description = long_description
        self.published_date = published_date
        self.short_description = short_description
        self.thumbnail_url = thumbnail_url

    def __str__(self):
        return self.title if self.title else str(self._id)

    def __repr__(self):
        return self.__str__()


book = Book(
    _id=None,
    isbn="12345GDFB",
    title="La escalera de la conciencia",
    page_count=490,
    status="PUBLISH",
    authors=[],
    categories=[],
    long_description="Lorem ipsum dolor",
    published_date=datetime.datetime(2021, 5, 11, 11, 11),
    short_description="Lorem ipsum dolor",
    thumbnail_url="https://www.google.com")

print(book)

new_book = {
    "isbn": book.isbn,
    "title": book.title,
    "pageCount": book.page_count,
    "status": book.status,
    "authors": book.authors,
    "categories": book.categories,
    "longDescription": book.long_description,
    "publishedDate": book.published_date,
    "shortDescription": book.short_description,
    "thumbnailUrl": book.thumbnail_url
}

book_id = collection.insert_one(new_book).inserted_id
print(book_id)

client.close()

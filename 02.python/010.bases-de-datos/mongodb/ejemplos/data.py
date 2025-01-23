
from .models import Book
import datetime

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
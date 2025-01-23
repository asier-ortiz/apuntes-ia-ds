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

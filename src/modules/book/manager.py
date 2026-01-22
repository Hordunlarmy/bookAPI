import uuid
from src.store import books
from src.modules.book.schema import BookCreate, BookRead


class BookManager:
    def create_book(self, book_data: BookCreate) -> BookRead:
        new_id = str(uuid.uuid4())
        new_book = BookRead(id=new_id, **book_data.dict())
        books[new_id] = new_book.dict()
        return new_book

    def get_books(self):
        return list(books.values())

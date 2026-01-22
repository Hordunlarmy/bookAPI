from fastapi import APIRouter
from .manager import BookManager
from .schema import BookCreate, BookRead
from typing import List

book_router = APIRouter()

@book_router.get("", response_model=List[BookRead], tags=["Books"])
async def get_books():
    """Retrieve a list of all books."""
    manager = BookManager()
    return manager.get_books()

@book_router.post("", response_model=BookRead, tags=["Books"])
async def create_book(book: BookCreate):
    """Create a new book."""
    manager = BookManager()
    return manager.create_book(book)

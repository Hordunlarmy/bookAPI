from fastapi import APIRouter
from typing import List

from .manager import AuthManager
from .schema import UserCreate, UserRead
from src.modules.library.manager import LibraryManager
from src.modules.book.schema import BookRead

auth_router = APIRouter()

@auth_router.post("", response_model=UserRead, tags=["Users"])
async def create_user(user: UserCreate):
    """Register a new user."""
    manager = AuthManager()
    return manager.create_user(user)

@auth_router.get("/{user_id}/borrowed", response_model=List[BookRead], tags=["Users"])
async def get_user_borrowed_books(user_id: str):
    """List all books borrowed by a user."""
    manager = LibraryManager()
    return manager.get_borrowed_books(user_id)

from fastapi import APIRouter
from .manager import LibraryManager
from .schema import BorrowRequest, BorrowResponse

library_router = APIRouter()

@library_router.post("/borrow", response_model=BorrowResponse, tags=["Library"])
async def borrow_book(request: BorrowRequest):
    manager = LibraryManager()
    return manager.borrow_book(request)

@library_router.post("/return", response_model=BorrowResponse, tags=["Library"])
async def return_book(request: BorrowRequest):
    manager = LibraryManager()
    return manager.return_book(request)

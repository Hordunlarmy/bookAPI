from src.store import books, users, borrows
from src.modules.library.schema import BorrowRequest
from fastapi import HTTPException

class LibraryManager:
    def borrow_book(self, borrow_data: BorrowRequest):
        user_id = borrow_data.userId
        book_id = borrow_data.bookId

        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found")
        
        if book_id not in books:
            raise HTTPException(status_code=404, detail="Book not found")

        is_borrowed = any(b['bookId'] == book_id for b in borrows)
        if is_borrowed:
            raise HTTPException(status_code=400, detail="Book is already borrowed")

        borrows.append(borrow_data.dict())
        return {"message": "Book borrowed successfully"}

    def get_borrowed_books(self, user_id: str):
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_borrows = [b for b in borrows if b['userId'] == user_id]
        borrowed_books = [books[b['bookId']] for b in user_borrows if b['bookId'] in books]
        return borrowed_books

    def return_book(self, return_data: BorrowRequest):
        user_id = return_data.userId
        book_id = return_data.bookId

        record = next((b for b in borrows if b['userId'] == user_id and b['bookId'] == book_id), None)

        if not record:
            raise HTTPException(status_code=404, detail="Borrow record not found")

        borrows.remove(record)
        return {"message": "Book returned successfully"}

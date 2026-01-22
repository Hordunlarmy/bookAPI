from pydantic import BaseModel


class BorrowRequest(BaseModel):
    userId: str
    bookId: str


class BorrowResponse(BaseModel):
    message: str

from fastapi import FastAPI

from src.modules.auth.router import auth_router
from src.modules.book.router import book_router
from src.modules.library.router import library_router

app = FastAPI(title="Library API", version="1.0.0")

app.include_router(auth_router, prefix="/users")
app.include_router(book_router, prefix="/books")
app.include_router(library_router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

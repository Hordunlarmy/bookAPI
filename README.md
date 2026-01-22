# Simple Library API

A simple REST API for a library system built with Python and FastAPI.

## Features

-   **Books**: Add and list books.
-   **Users**: Register users and view borrowed books.
-   **Library**: Borrow and return books.

## Getting Started

### Prerequisites

-   Python 3.8+
-   And other dependencies listed in `pyproject.toml`

### Installation

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

### Running the App

Run the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Books
-   `POST /books`: Add a new book.
-   `GET /books`: List all books.

### Users
-   `POST /users`: Register a new user.
-   `GET /users/{user_id}/borrowed`: List books borrowed by a specific user.

### Library
-   `POST /borrow`: Borrow a book.
-   `POST /return`: Return a borrowed book.

## Documentation

Interactive API documentation is available at:
-   Swagger UI: `http://127.0.0.1:8000/docs`
-   ReDoc: `http://127.0.0.1:8000/redoc`

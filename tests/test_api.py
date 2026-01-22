from fastapi.testclient import TestClient
from main import app
from src.store import users, books, borrows

client = TestClient(app)

def setup_function():
    users.clear()
    books.clear()
    borrows.clear()

def test_add_book():
    response = client.post("/books", json={"title": "The Hobbit", "author": "J.R.R. Tolkien"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"
    assert "id" in data
    assert isinstance(data["id"], str)

def test_register_user():
    response = client.post("/users", json={"name": "Alice"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert "id" in data
    assert isinstance(data["id"], str)

def test_register_user_duplicate():
    client.post("/users", json={"name": "Duplicate User"})
    response = client.post("/users", json={"name": "Duplicate User"})
    assert response.status_code == 400
    assert response.json() == {"detail": "User with this name already exists"}

def test_borrow_book_success():
    user = client.post("/users", json={"name": "Alice"}).json()
    book = client.post("/books", json={"title": "The Hobbit", "author": "Tolkien"}).json()
    
    response = client.post("/borrow", json={"userId": user["id"], "bookId": book["id"]})
    assert response.status_code == 200
    assert response.json() == {"message": "Book borrowed successfully"}

def test_borrow_book_already_borrowed():
    user1 = client.post("/users", json={"name": "Alice"}).json()
    user2 = client.post("/users", json={"name": "Bob"}).json()
    book = client.post("/books", json={"title": "The Hobbit", "author": "Tolkien"}).json()
    
    client.post("/borrow", json={"userId": user1["id"], "bookId": book["id"]})
    
    response = client.post("/borrow", json={"userId": user2["id"], "bookId": book["id"]})
    assert response.status_code == 400
    assert response.json() == {"detail": "Book is already borrowed"}

def test_list_borrowed_books():
    user = client.post("/users", json={"name": "Alice"}).json()
    book1 = client.post("/books", json={"title": "Book 1", "author": "Auth 1"}).json()
    book2 = client.post("/books", json={"title": "Book 2", "author": "Auth 2"}).json()
    
    client.post("/borrow", json={"userId": user["id"], "bookId": book1["id"]})
    
    response = client.get(f"/users/{user['id']}/borrowed")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Book 1"

def test_return_book():
    user = client.post("/users", json={"name": "Alice"}).json()
    book = client.post("/books", json={"title": "Book 1", "author": "Auth 1"}).json()
    client.post("/borrow", json={"userId": user["id"], "bookId": book["id"]})
    
    response = client.post("/return", json={"userId": user["id"], "bookId": book["id"]})
    assert response.status_code == 200
    assert response.json() == {"message": "Book returned successfully"}
    
    response = client.get(f"/users/{user['id']}/borrowed")
    assert response.json() == []

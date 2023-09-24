from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(
        min_length=3,
    )
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


books = [
    Book(1, "Title 1", "Author 1", "Description 1", 5),
    Book(2, "Title 2", "Author 2", "Description 2", 5),
    Book(3, "Title 3", "Author 3", "Description 3", 2),
    Book(4, "Title 4", "Author 4", "Description 4", 1),
]


@app.get("/books")
def fetch_books():
    return books


@app.post("/books/create_one")
def create_book(new_book=Body()):
    books.append(new_book)


@app.get("/books/{book_id}")
def find_book_based_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return "No book"


@app.put("/books/update_book")
def update_book(updated_book: BookRequest):
    for book in books:
        if book.id == updated_book.id:
            books.remove(book)
            books.append(updated_book)
            break

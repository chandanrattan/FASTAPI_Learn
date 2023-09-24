from fastapi import FastAPI

app = FastAPI()

books = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "Maths"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
]


@app.get("/books/{dynamic_param}")
def read_all_books(dynamic_param: str):
    for book in books:
        if book.get("title").casefold() == dynamic_param.casefold():
            return book
        else:
            return "Book not found"


@app.get("/books")
def read_all_books():
    return books

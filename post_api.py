from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "Maths"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
]


@app.post("/books/create_one")
def create_book(new_book=Body()):
    books.append(new_book)


@app.get("/books")
def fetch_books():
    return books


@app.post("/books/update_Book")
def update_book(update_book=Body()):
    counter = 0
    for book in books:
        if book.get("title").casefold() == update_book.get("title").casefold():
            book[counter] = update_book
            return books[counter]
        print(books[counter])
        counter += 1


@app.patch("/books/patch_book")
def update_book(update_book=Body()):
    counter = 0
    for book in books:
        if book.get("title").casefold() == update_book.get("title").casefold():
            book[counter] = update_book
            return books[counter]
        # print(books[counter])
        counter += 1

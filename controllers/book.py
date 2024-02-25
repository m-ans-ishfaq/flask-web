from flask import Blueprint, render_template, request
from models.book import Book
from db.session import session

book_bp = Blueprint('book', __name__)

@book_bp.get('/books')
def get_books():
    books = ['Book1', 'Book2', 'Book3']
    return render_template('books.html', books=books)

@book_bp.post('/book')
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    print(title, author)
    data_is_valid = Book.validate_book_data({ "title": title, "author": author })
    new_book = Book(title=title, author=author)
    if data_is_valid:
        session.add(new_book)
        session.commit()
        return "CREATED", 201
    else:
        return "INVALID", 401
from flask import render_template, redirect, request
from book_app import app
from book_app.models.book import Book
from book_app.models.author import Author


@app.route('/books')
def books():
    return render_template('bookss.html', all_books=Book.get_all())


@app.route('/create/book', methods=['POST'])
def create_book():
    data = {
        "title": request.form['title'],
        "num_of_page": request.form['num_of_page']
    }
    Book.save(data)
    return redirect('/books')


@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    return render_template('show_book.html', book=Book.get_by_id(data), unfavorited_authors=Author.unfavorited_authors(data))


@app.route('/join/author', methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")

from flask import redirect, render_template, request
from book_app.models.book import Book
from book_app.models.author import Author
from book_app import app


@app.route('/')
def index():
    return redirect('/authors')


@app.route('/authors')
def authors():
    return render_template('author.html', all_authors=Author.get_all())


@app.route('/create/author', methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    Author.save(data)
    return redirect('/authors')


@app.route('/author/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_author.html', author=Author.get_by_id(data), unfavorited_books=Book.unfavorited_books(data))

from book_app.config.mysqlconnection import connectToMySQL
from book_app.models import author
from book_app import db


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_page = data['num_of_page']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        self.authors_who_favorited = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        result = connectToMySQL(db).query_db(query)

        books = []

        for b in result:
            books.append(cls(b))
        return books

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors_who_favorited.append(author.Author(data))
        return book

    @classmethod
    def unfavorited_books(cls, data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books').query_db(query, data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books

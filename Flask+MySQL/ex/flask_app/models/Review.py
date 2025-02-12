from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.User import User
from flask_app import db

class Review:
    def __init__(self , data):
        self.id = data['id']
        self.title = data['title']
        self.rating = data['rating']
        self.date_watched = data['date_watched']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user = None

    @classmethod
    def get_by_id(cls , data):
        query = """
            SELECT * FROM reviews JOIN users ON reviews.user_id = users.id WHERE reviews.id = %(id)s;
        """
        result = connectToMySQL(db).query_db(query , data)
        if not result:
            return None

        review = cls(result[0])
        user_data = {
            'id': result[0]['users.id'],
            'username': result[0]['username'],
            'email': result[0]['email'],
            'password': result[0]['password'],
            'created_at': result[0]['users.created_at'],
            'updated_at': result[0]['users.updated_at'],
        }
        review.user = User(user_data)
        return review
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM reviews JOIN users ON reviews.user_id = users.id
        """
        result = connectToMySQL(db).query_db(query)
        reviews = []
        if result:
            for row in result:
                review = cls(row)
                user_data = {
                    'id': row['users.id'],
                    'username': row['username'],
                    'email': row['email'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                }
                review.user = User(user_data)
                reviews.append(review)
        return reviews
    
    @classmethod
    def create(cls , data):
        query = "INSERT INTO reviews (title, rating , date_watched ,content , user_id) VALUES(%(title)s, %(rating)s , %(date_watched)s , %(content)s, %(user_id)s);"
        return connectToMySQL(db).query_db(query ,data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE reviews SET title = %(title)s, rating= %(rating)s, date_watched=%(date_watched)s, content=%(content)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM reviews WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query , data)
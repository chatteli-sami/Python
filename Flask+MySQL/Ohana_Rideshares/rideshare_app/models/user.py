from rideshare_app.config.mysqlconnection import connectToMySQL
from rideshare_app import db
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL(db).query_db(query,data)
        return result
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query, user)
        if len(result) >= 1:
            flash("email already taken", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash('invalid email !!', "register")
        if len(user['first_name']) < 3:
            flash("first name must be at least 3 characters", "register")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("last name must be at least 3 characters", "register")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("first name must be at least 3 characters", "register")
            is_valid = False
        if len(user['password']) < 8:
            flash("password must be at least 3 characters", "register")
            is_valid = False
        if user['password'] != user['confirm']:
            flash('password dont mutch')
            is_valid = False
        return is_valid
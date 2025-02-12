from recipes_app.config.mysqlconnection import connectToMySQL
from recipes_app import db
from flask import flash
from flask_bcrypt import Bcrypt
from recipes_app import app
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.create_at = data["create_at"]
        self.update_at = data["update_at"]
    
    @classmethod
    def save(cls , data):
        ep = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = ep
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = (%(email)s);"
        result = connectToMySQL(db).query_db(query, data)
        if result:
            return cls(result[0])
        return None
    
    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['first_name']) < 3:
            is_valid = False
            flash('first name should at be least 3 charactere', 'validate')
        if len(data['last_name']) < 3:
            is_valid = False
            flash('last name should at be least 3 charactere', 'validate')
        if user_in_db:
            is_valid = False
            flash('email already taken', 'validate')
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('email should be good format', 'validate')
        if len(data['password']) < 8:
            is_valid = False
            flash('password sould be at least 8 charactere', 'validate')
        if data['password'] != data['confirm']:
            is_valid = False
            flash('password dont match', 'validate')
        
        return is_valid

    
    @staticmethod
    def login_validate(data):
        is_valide = True
        user_in_db = User.get_by_email(data)
        if not user_in_db:
            is_valide = False
            flash('no user with this email exists', 'login')
        elif not bcrypt.check_password_hash( user_in_db.password, data['password']):
            is_valide = False
            flash('incorrect password', 'login')
        return is_valide
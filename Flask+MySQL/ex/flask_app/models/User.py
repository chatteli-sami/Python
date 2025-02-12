from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app import db
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)

class User:
    def __init__(self , data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Register a new user
    @classmethod
    def register(cls , data):
        ep = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = ep
        query = "INSERT INTO users (username , email , password) VALUES(%(username)s , %(email)s , %(password)s);"
        return connectToMySQL(db).query_db(query , data)
    # Get a user by email
    @classmethod
    def get_by_email(cls , data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query , data)
        if result:
            return cls(result[0])
        return None

    # Validate the data for registering
    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        # Conditions    
        if len(data['username']) < 6:
            is_valid = False
            flash("Username should be at least 6 characters long" , "register")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Email should be good format." , "register")
        if user_in_db:
            is_Valid = False
            flash("Email already exists." , "register")
        if len(data['password']) < 8:
            is_valid = False
            flash("Password should at least be 8 characters long" , "register")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Passwords must match." , "register")

        return is_valid

    # Validate the data for login in.
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        # Conditions
        if not user_in_db:
            is_valid = False
            flash("No user with this email exists." , "login")
        elif not bcrypt.check_password_hash(user_in_db.password , data['password']):
            is_valid = False
            flash("Incorrect password." , "login")
        return is_valid
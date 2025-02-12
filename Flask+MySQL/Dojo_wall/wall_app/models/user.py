from wall_app.config.mysqlconnection import connectToMySQL
from wall_app import db
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updatesd_at = data["updatesd_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(db).query_db(query)
        users = []
        for u in result:
            users.append(cls(u))
        return users

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        rslt = connectToMySQL(db).query_db(query, data)
        return rslt
    
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query)
        if len(result)>=1:
            flash("email already taken ", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user('email')):
            is_valid = False
            flash("invalid email !!!!!!!!!!!")
        if len(user['first_name']) < 3:
            is_valid = False
            flash("first name must be at least 3 charactere", "register")
        if len(user['last_name']) < 3:
            is_valid = False
            flash("last name must be at least 3 charactere", "register")
        if len(user['password']) < 8:
            is_valid = False
            flash("password must be at least 8 charactere", "register")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("passwordd don't match", "register")
        return is_valid
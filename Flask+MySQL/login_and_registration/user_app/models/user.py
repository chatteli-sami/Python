from user_app.config.mysqlconnection import connectToMySQL
from flask import flash
from user_app import db
import re

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
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(passsword)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @staticmethod
    def is_valid_users(users):
        is_valid = True
        if len(users["first_name"]) < 3:
            is_valid = False
            flash("first name is required")
        if len(users["last_name"]) < 3:
            is_valid = False
            flash("last name is required")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query, users)
        if len(result) >= 1:
            flash("mail is already taken", "registration")
            is_valid = False
        if len(users["email"]) > 0 and not EMAIL_REGEX.match(users['email']):
            flash("invalid email format.", "registration")
            is_valid = False
        if len(users["password"]) < 8:
            flash("password must be lease 8 characters")
            is_valid = False
        return is_valid

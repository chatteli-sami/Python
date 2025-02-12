from user_app.config.mysqlconnection import connectToMySQL
from user_app import db
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @staticmethod
    def is_valid_users(cls, user):
        is_valid = True

        if len(user["first_name"]) <= 0:
            is_valid = False
            flash("first_name is required .")
        if len(user["last_name"]) <= 0:
            is_valid = False
            flash("last_name is required .")

        if len(user["email"]) <= 0:
            is_valid = False
            flash("email is required")

        if len(user["email"]) > 0 and not EMAIL_REGEX.match(user["email"]):
            flash("invaild email format")
            is_valid = False

        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(db).query_db(query)
        users = []
        for u in result:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL(db).query_db(query, data)

from flask_app.config.mysqlconnection import connectToMySQL


class User:

    DB = "user_card"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL("user_card").query_db(query)
        users = []
        for u in result:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL("user_card").query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL("user_card").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s update_at=NOW(), id=%(id)s"
        return connectToMySQL("user_card").query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELET FROM user WHERE id=%(id)s"
        return connectToMySQL("user_card").query_db(query, data)

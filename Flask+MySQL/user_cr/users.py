from mysqlconnection import connectToMySQL


class Users:
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
        result = connectToMySQL('userss').query_db(query)
        users = []
        for u in result:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('users').query_db(query, data)
        return result

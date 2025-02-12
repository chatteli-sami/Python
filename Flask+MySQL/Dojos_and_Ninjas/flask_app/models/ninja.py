from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db


class Ninjas:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one_by_id(cls, id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {
            "id": id
        }
        result = connectToMySQL(db).query_db(query, data)
        ninja = cls(result[0])
        return ninja

    @classmethod
    def delete_by_id(cls, id):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        data = {
            "id": id
        }
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s;"
        return connectToMySQL(db).query_db(query, data)

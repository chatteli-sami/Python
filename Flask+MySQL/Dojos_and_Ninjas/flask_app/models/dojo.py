from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninjas
from flask_app import db


class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(db).query_db(query)
        dojos = []
        for d in result:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def get_all_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return result

        print(result)
        Dojo = cls(result[0])

        for row in result:
            n = {
                "id": row["ninjas.id"],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created-at'],
                "update_at": row['ninjas.update-at']
            }
            Dojo.ninjas.append(Ninjas(n))
            return Dojo

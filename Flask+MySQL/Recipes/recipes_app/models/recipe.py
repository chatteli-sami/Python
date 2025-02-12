from recipes_app.config.mysqlconnection import connectToMySQL
from recipes_app import db
from recipes_app.models.user import User


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.introduction = data['introduction']
        self.date_mado = data['date_mado']
        self.under_30 = data['under_30']
        self.user = None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        if not result:
            return None
        recipe = cls(result[0])
        user_data = {
            'id': result[0]['users.id'],
            'first_name': result[0]['first_name'],
            'last_name': result[0]['last_name'],
            'email': result[0]['email'],
            'password': result[0]['password'],
            'created_at': result[0]['created_at'],
            'updated_at': result[0]['updated_at']
        }
        recipe.user = User(user_data)
        return recipe
    
    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        result = connectToMySQL(db).query_db(query, data)
        recipes = []
        if result:
            for row in result:
                recipe = cls(row)
                user_data = {
                    'id': row[0]['users.id'],
                    'first_name': row[0]['first_name'],
                    'last_name': row[0]['last_name'],
                    'email': row[0]['email'],
                    'password': row[0]['password'],
                    'created_at': row[0]['users.created_at'],
                    'updated_at': row[0]['users.updated_at']
                }
                recipe.user = User(user_data)
                recipes.append(recipe)
        return recipes

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, introduction, date_mado) VALUES (%(name)s, %(description)s, %(introduction)s, %(data_mado)s);"
        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description= %(description)s, introduction=%(introduction)s, date_mado=%(date_mado)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query , data)

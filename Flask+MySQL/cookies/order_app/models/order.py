from order_app.config.mysqlconnection import connectToMySQL
from flask import flash
from order_app import db


class Order:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.number = data['number']
        self.created_at = data['created_at']
        self.update__at = data['update__at']

    @classmethod
    def is_valid_order(cls, order):
        is_valid = True

        if len(order['name']) <= 0:
            is_valid = False
            flash("name is required")
        if len(order['cookie_type']) <= 0:
            is_valid = False
            flash('type is required')
        if int(order['number']) <= 0:
            is_valid = False
            flash("please entre a valid number")

        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        result = connectToMySQL(db).query_db(query)

        orders = []
        for o in result:
            orders.append(cls(o))
        return orders

    @classmethod
    def get_by_id(cls, order_id):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        data = {
            "id": order_id
        }
        result = connectToMySQL(db).query_db(query, data)
        if result:
            iOrder = result[0]
            return iOrder
        return False

    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (name, cookie_type, number) VALUES (%(name)s, %(cookie_type)s, %(number)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE orders SET name = %(name)s, cookie_type = %(cookie_type)s, number = %(number)s WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return result

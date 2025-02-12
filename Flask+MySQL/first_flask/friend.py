from mysqlconnection import connectToMySQL


class Friend:
    db = "first_flask"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occcupation']
        self.created_at = data['created_at']
        self.update_at = data['upsate_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends"

        result = connectToMySQL('first_flask').query_db(query)

        friends = []

        for friend in result:
            friends.append(cls(friend))
        return friends

    @classmethod
    def save(cls, data):
        query = """INSERT INTO friens (first_name, last_name, occupation, created_at, update_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s);"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

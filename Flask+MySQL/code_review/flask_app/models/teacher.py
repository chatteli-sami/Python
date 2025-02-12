from flask_app.config.mysqlconnection import connectToMySQL


class Teacher:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM teacher;"
        result = connectToMySQL("school").query_db(query)

        teacher = []

        for t in result:
            teacher.append(cls(t))
        return teacher

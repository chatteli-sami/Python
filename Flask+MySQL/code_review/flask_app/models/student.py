from flask_app.config.mysqlconnection import connectToMySQL


class Student:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        self.teacher_id = data['teacher_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM students;"
        result = connectToMySQL("school").query_db(query)

        students = []

        for s in result:
            students.append(cls(s))
        return students

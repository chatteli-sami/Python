from wall_app.config.mysqlconnection import connectToMySQL
from flask import flash
from wall_app import db
from wall_app.models.user import User

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']
    
    @classmethod
    def save(cls, data):
        if not cls.validate_post(data):
            print("in save if not valid...")
            return False
        print("Data passed into create METHOD: ", data)

        query = "INSERT into posts (content, user_id) values (%(content)s, %(user_id)s);"
        result = connectToMySQL(db).query_db(query, data)

        return result

    @classmethod
    def delete(cls, post_id):
        query = "DELETE from posts WHERE id = %(id)s;"
        connectToMySQL(db).query_db(query, {"id": post_id})
        return post_id

    @classmethod
    def validate_post(cls, data):
        is_valid = False
        if len(data["content"]) == 0:
            flash("Post content must not be blank.")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = """SELECT * from posts
                JOIN users on posts.user_id = users.id;"""
        results = connectToMySQL(db).query_db(query)
        print("Raw data for all posts: ", results)
        all_posts = []
        for row in results:
            posting_user = User({
                "id": row["user_id"],
                "email": row["email"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
                "password": row["password"]
            })
            new_post = Post({
                "id": row["id"],
                "content": row["content"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "user": posting_user
            })
            all_posts.append(new_post)

        return all_posts
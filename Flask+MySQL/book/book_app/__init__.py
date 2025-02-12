from flask import Flask

db = "books"
app = Flask(__name__)
app.secret_key = "shhhh !"

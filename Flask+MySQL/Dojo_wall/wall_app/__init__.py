from flask import Flask


db = "dojo_wall"
app = Flask(__name__)
app.secret_key = 'shhhhh!'
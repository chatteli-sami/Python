from flask import Flask

app = Flask(__name__)
app.secret_key = "shhhhhh"
db = "user_app"

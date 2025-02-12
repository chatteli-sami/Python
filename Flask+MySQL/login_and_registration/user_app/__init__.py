from flask import Flask

db = "login_and_registration"

app = Flask(__name__)

app.secret_key = "shhhh !"

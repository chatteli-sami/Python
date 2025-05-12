from flask_app import app
from flask_app.models.User import User

from flask import render_template , request , redirect , session


@app.route('/')
def index():
    if 'userEmail' in session:
        return redirect('/dashboard')

    return render_template("index.html")

@app.route('/register' , methods=['POST'])
def register():
    data = request.form
    if User.validate_register(data):
        User.register(data)
    return redirect("/")

@app.route('/login' , methods=['POST'])
def login():
    data = request.form
    if User.validate_login(data):
        session['userEmail'] = data['email']
        return redirect("/dashboard")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
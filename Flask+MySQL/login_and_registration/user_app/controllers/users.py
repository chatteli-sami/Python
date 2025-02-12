from flask import render_template, request, redirect, session, flash
from user_app import app
from user_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def regiter():
    if not User.is_valid_users(request.form):
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(request.form)
    session['user_id'] = id
    return redirect('/dashboared')


@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash('invalid email')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("invalid password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboared')


@app.route('/dashboared')
def dashboared():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template("dashboared.html", user=User.get_by_id(data))


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

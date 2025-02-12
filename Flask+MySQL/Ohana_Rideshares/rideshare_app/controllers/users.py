from flask import flash, render_template, session, request, redirect
from rideshare_app.models.user import User
from flask_bcrypt import Bcrypt
from rideshare_app import app

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not User.register(request.form):
        return redirect('/')
    data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password' : bcrypt.generate_password_hash(request.form['password'])
    }
    user = User.save(data)
    session['user_id'] = user
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash('invalid email', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('invalid password', 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboared')

@app.route('/dashboared')
def dashboared():
    return 'hello '
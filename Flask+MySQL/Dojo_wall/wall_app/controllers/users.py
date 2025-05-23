from flask import flash, render_template, redirect, request, session
from wall_app import app
from wall_app.models.post import Post
from wall_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/wall')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/wall')

@app.route('/wall')
def wall():

    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    
    all_posts = Post.get_all()

    return render_template("wall.html", user=User.get_by_id(data), posts=all_posts)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
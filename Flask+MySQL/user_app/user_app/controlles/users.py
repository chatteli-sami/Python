from flask import render_template, redirect, request, flash, session
from user_app.models.user import User
from user_app import app


@app.route('/')
def index():
    friends = User.get_all()
    print(friends)
    return render_template('user.html', all_friends=friends)


@app.route('/user/new')
def new():
    return render_template('create.html')


@app.route('/create', methods=['POST'])
def create():
    users_info = request.form
    if User.is_valid_users(users_info):
        User.save(users_info)
        print("GO PASS")
        return redirect('/')

    print("IS FAIL")
    return redirect('/user/new')

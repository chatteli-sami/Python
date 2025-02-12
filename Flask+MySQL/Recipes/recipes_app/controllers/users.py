from flask import redirect, render_template, request, session
from recipes_app import app
from recipes_app.models.user import User

@app.route('/')
def index():
    if 'userEmail' in session:
        return redirect('/recipes')
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.form
    if User.validate_register(data):
        User.save(data)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    if User.login_validate(data):
        session['userEmail'] = data['email']
        return redirect('/recipes')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

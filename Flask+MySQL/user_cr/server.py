from flask import Flask, render_template, request, redirect

from users import Users

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template('read_all.html', users=Users.get_all())


@app.route('/user/new')
def new():
    return render_template('create.html')


@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)

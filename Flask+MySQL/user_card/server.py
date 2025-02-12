from flask import Flask, render_template, redirect, request
from users import User

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('users')


@app.route('/users')
def users():
    return render_template('users.html', users=User.get_all())


@app.route('/users/new')
def new():
    return render_template('create.html')


@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/users/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template('edit_users.html', users=User.get_one(data))


@app.route('/users/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template('show.html', users=User.get_one(data))


@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')


@app.route('/users/destroy/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    User.destroy(data)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True)

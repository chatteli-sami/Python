from flask import Flask, render_template, request, redirect

from friend import Friend

app = Flask(__name__)


@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html")


@app.route('/created_friend')
def created_friend():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    Friend.save(data)
    return redirect('/')


@app.route('/friends/create', methods=['POST'])
def create():
    Friend.save(request.form)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

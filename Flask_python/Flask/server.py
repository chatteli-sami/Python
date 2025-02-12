from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/dojo')
def dojo():
    return 'Dojo'


@app.route('/say/<name>')
def say(name):
    print(name)
    return 'hi, ' + name


@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    if isinstance(word, str):
        return f"{word} " * num
    else:
        return "Invalid input!"


@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404


if __name__ == "__main__":
    app.run(debug=True)

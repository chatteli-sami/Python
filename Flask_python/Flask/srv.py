from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def fileHtml():
    return render_template('index.html', phrase='Hello', times=5)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<color>')
def play(x=3, color="blue"):
    return render_template('play.html', x=x, color=color)


if __name__ == '__main__':
    app.run(debug=True)

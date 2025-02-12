from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('index.html', attempts=session['attempts'])


@app.route('/guess', methods=['POST'])
def guess():
    session['attempts'] += 1
    guess = int(request.form['guess'])
    random_number = session['random_number']

    if guess < random_number:
        feedback = 'too low !'
    elif guess > random_number:
        feedback = 'too hight!'
    else:
        feedback = 'correct'

    if session['attempts'] >= 15 and guess != random_number:
        feedback = 'You lose! the correct number was ' + str(random_number)
        return redirect('/reset')

    return render_template('index.html', feedback=feedback, attempts=session['attempts'])


@app.route('/reset')
def reset():
    session.pop('random_number', None)
    session.pop('attempts', None)
    return redirect('/')


@app.route('/leaderboard', methods=['POST', 'GET'])
def leaderboard():
    if request.methods == ['POST']:
        name = request.form['name']
        attempts = session['attempts']
        with open("leaderboard.txt", "a") as file:
            file.write(f"{name} - {attempts}\n")
        return redirect('/leaderboard')

    leaders = []
    try:
        with open("leaderboard.txt", "r") as file:
            leaders = file.readline()
    except FileNotFoundError:
        pass

    return render_template('leaderboard.html', leaders=leaders)


if __name__ == '__main__':
    app.run(debug=True)

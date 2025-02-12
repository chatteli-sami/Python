from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    session['visits'] = session.get('visits', 0) + 1
    session['counter'] = session.get('counter', 0)
    return render_template('index.html', visits=session['visits'], counter=session['counter'])


@app.route('/increment')
def increment():
    session['counter'] = session.get('counter', 0) + 1
    return redirect('/')


@app.route('/increment_by_2')
def increment_by_2():
    session['counter'] = session.get('counter', 0) + 2
    return redirect('/')


@app.route('/reset_counter')
def reset_counter():
    session['counter'] = 0
    return redirect('/')


@app.route('/set_increment', methods=['POST'])
def set_increment():
    increment_value = int(request.form.get('increment_value', 1))
    session['counter'] = session.get('counter', 0) + increment_value
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

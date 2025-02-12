from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.burger import Burger


@app.route('/burgers')
def burgers():
    return render_template("burgers.html", burgers=Burger.get_all())


@app.route('/burgers/create', methods=['POST'])
def create():
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.save(data)
    return redirect('/burgers')

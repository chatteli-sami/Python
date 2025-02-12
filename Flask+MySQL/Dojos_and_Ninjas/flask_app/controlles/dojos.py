from flask import render_template, redirect, request
from flask_app.models.dojo import Dojos
from flask_app import app


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    dojos = Dojos.get_all()
    return render_template('create_dojo.html', all_dojos=dojos)


@app.route('/dojos/create', methods=['POST'])
def create():
    Dojos.save(request.form)
    return redirect('/dojos')


@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template("dojo.html", dojo=Dojos.get_all_with_ninjas(data))

from flask import render_template, redirect, request
from flask_app.models import ninja, dojo
from flask_app import app


@app.route('/ninjas')
def ninjas():
    return render_template("ninja.html", dojos=dojo.Dojos.get_all())


@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    ninja.Ninjas.save(request.form)
    return redirect('/')


@app.route('/ninjas/edite/<ninja_id>')
def edit(ninja_id):
    print("in edit for ninja id : ", ninja_id)
    n = ninja.Ninjas.get_one_by_id(id)
    return render_template("edit_ninja.html", ninja=n)


@app.route('/ninjas/delete/<ninja_id>/<dojo_id>')
def delete(ninja_id):
    print("deleting ninja id : ", ninja_id)
    ninja.Ninjas.delete_by_id(id)
    return redirect(f'/dojos/{dojo.id}')


@app.route('/ninjas/update', methods=['POST'])
def update():
    print(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')

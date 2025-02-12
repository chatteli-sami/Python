from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.burger import Burger


@app.route('/')
def index():
    return redirect('/burgers')


@app.route('/burgers')
def all_burgers():
    return render_template('burger.html', burgers=Burger.get_all())


@app.route('/create', methods=['POST'])
def create_burger():

    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Burger.validate_burger(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
      # else no errors:
    Burger.save(request.form)
    return redirect("/burgers")

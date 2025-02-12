from flask import redirect, render_template, request, session
from recipes_app import app
from recipes_app.models.recipe import Recipe
from recipes_app.models.user import User

@app.route('/recipes')
def recipes():
    if not 'userEmail' in session:
        return redirect('/')
    user_id = User.get_by_email({'email': session['userEmail']}).id
    rcp = Recipe.get_all()
    return render_template('recipe.html', log_user = user_id, rcp=rcp)

@app.route('/recipes/new')
def add_new_recipe():
    if not 'userEmail' in session:
        return redirect('/')
    
    user_id = User.get_by_email({'email': session['userEmail']}).id

    return render_template("add_recipe.html" , user_id = user_id)

@app.route('/recipes/new' , methods=['POST'])
def create_recipe():
    if not 'userEmail' in session:
        return redirect('/')
    
    data = request.form
    Recipe.create(data)
    return redirect('/recipes')

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if not 'userEmail' in session:
        return redirect('/')
    
    recipe_to_edit = Recipe.get_by_id({'id': id})
    return render_template("edit_recipe.html" , recipe = recipe_to_edit)
    

@app.route('/recipes/update' , methods=['POST'])
def update_recipe():
    if not 'userEmail' in session:
        return redirect('/')

    data = request.form
    Recipe.update(data)
    return redirect('/recipes')

@app.route('/reviews/<int:id>')
def show_recipe(id):
    if not 'userEmail' in session:
        return redirect('/')
    
    review = Recipe.get_by_id({'id': id})
    return render_template("show_recipe.html" , review = review)

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if not 'userEmail' in session:
        return redirect('/')
    
    Recipe.delete({'id': id})
    return redirect('/recipes')
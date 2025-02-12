from flask_app import app
from flask import render_template , request , redirect , session

from flask_app.models.User import User
from flask_app.models.Review import Review

@app.route('/dashboard')
def dashboard():
    if not 'userEmail' in session:
        return redirect('/')
    userEmail = session['userEmail']
    user = User.get_by_email({'email': userEmail})

    reviews = Review.get_all()
    return render_template("dashboard.html" , logged_user = user , reviews = reviews)

@app.route('/reviews/new')
def add_new_review():
    if not 'userEmail' in session:
        return redirect('/')
    
    user_id = User.get_by_email({'email': session['userEmail']}).id

    return render_template("add_review.html" , user_id = user_id)

@app.route('/reviews/new' , methods=['POST'])
def create_review():
    if not 'userEmail' in session:
        return redirect('/')
    
    data = request.form
    Review.create(data)
    return redirect('/dashboard')

@app.route('/reviews/<int:id>/edit')
def edit_review(id):
    if not 'userEmail' in session:
        return redirect('/')
    
    review_to_edit = Review.get_by_id({'id': id})
    # date_watched = "12/2/2024 00:00:00"
    review_to_edit.date_watched = str(review_to_edit.date_watched).split(' ')[0]
    return render_template("edit_review.html" , review = review_to_edit)
    

@app.route('/reviews/update' , methods=['POST'])
def update_review():
    if not 'userEmail' in session:
        return redirect('/')

    data = request.form
    Review.update(data)
    return redirect('/dashboard')

@app.route('/reviews/<int:id>')
def show_review(id):
    if not 'userEmail' in session:
        return redirect('/')
    
    review = Review.get_by_id({'id': id})
    return render_template("show_review.html" , review = review)

@app.route('/reviews/<int:id>/delete')
def delete_review(id):
    if not 'userEmail' in session:
        return redirect('/')
    
    Review.delete({'id': id})
    return redirect('/dashboard')
from flask import render_template, redirect, request
from order_app.models.order import Order
from order_app import app


@app.route('/')
def index():
    return redirect('/cookies')


@app.route('/cookies')
def cookies():
    orders = Order.get_all()
    return render_template('cookie.html', all_orders=orders)


@app.route('/cookies/new')
def new_order():
    return render_template('new_order.html')


@app.route('/create', methods=["POST"])
def create():
    data = {
        'name': request.form['name'],
        'cookie_type': request.form['cookie_type'],
        'number': request.form['number']
    }
    if not Order.is_valid_order(data):
        return redirect('/cookies/new')

    Order.save(data)
    return redirect('/cookies')


@app.route('/cookies/edit/<int:cookie_id>')
def edit(cookie_id):
    order = Order.get_by_id(cookie_id)
    return render_template('edit_order.html', one_order=order)


@app.route('/edit/<int:cookie_id>', methods=["POST"])
def update(cookie_id):
    data = request.form
    if not Order.is_valid_order(data):
        return redirect(f'/cookies/edit/{cookie_id}')
    Order.update(data)
    return redirect('/')

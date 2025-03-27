from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pos.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.Boolean, default=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_role'] = user.role
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_role', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        availability = 'availability' in request.form
        new_item = MenuItem(name=name, price=price, category=category, availability=availability)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('menu'))
    menu_items = MenuItem.query.all()
    return render_template('menu.html', menu_items=menu_items)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        table_number = request.form['table_number']
        order = Order(table_number=table_number, total=0)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('order'))
    orders = Order.query.all()
    return render_template('order.html', orders=orders)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        order_id = request.form['order_id']
        payment_method = request.form['payment_method']
        order = Order.query.get(order_id)
        if order:
            order.total = sum(item.menu_item.price * item.quantity for item in order.items)
            db.session.commit()
            return redirect(url_for('receipt', order_id=order_id))
    orders = Order.query.all()
    return render_template('payment.html', orders=orders)

@app.route('/receipt/<int:order_id>')
def receipt(order_id):
    order = Order.query.get(order_id)
    return render_template('receipt.html', order=order)

@app.route('/table', methods=['GET', 'POST'])
def table():
    if request.method == 'POST':
        table_number = request.form['table_number']
        order_id = request.form['order_id']
        order = Order.query.get(order_id)
        if order:
            order.table_number = table_number
            db.session.commit()
        return redirect(url_for('table'))
    orders = Order.query.all()
    return render_template('table.html', orders=orders)

@app.route('/reports')
def reports():
    orders = Order.query.all()
    total_revenue = sum(order.total for order in orders)
    return render_template('reports.html', orders=orders, total_revenue=total_revenue)

if __name__ == '__main__':
    app.run(debug=True)

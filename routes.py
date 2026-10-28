from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.forms import LoginForm, RegistrationForm, LogRunForm
from app.models import User, Run, Product

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/shop')
def shop():
    sample_products = [
        {'name': 'Pro Trail Running Shoes', 'category': 'Footwear', 'price': 129.99},
        {'name': 'GPS Fitness Watch', 'category': 'Electronics', 'price': 199.99},
        {'name': 'Hydration Running Vest', 'category': 'Accessories', 'price': 49.99}
    ]
    return render_template('shop.html', title='Shop', products=sample_products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or user.password_hash != form.password.data:
            flash('Invalid email or password')
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('index'))
        
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
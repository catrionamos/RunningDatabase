from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    fitness_level = db.Column(db.String(50), nullable=True)
    running_goal = db.Column(db.String(100), nullable=True)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=True)
    
    # Relationships
    runs = db.relationship('Run', backref='runner', lazy=True)
    orders = db.relationship('Order', backref='customer', lazy=True)

class Program(db.Model):
    __tablename__ = 'programs'
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(100), nullable=False)
    target_level = db.Column(db.String(50), nullable=True)
    duration_weeks = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    
    users = db.relationship('User', backref='enrolled_program', lazy=True)

class Run(db.Model):
    __tablename__ = 'runs'
    id = db.Column(db.Integer, primary_key=True)
    distance_km = db.Column(db.Float, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    date_logged = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    
    orders = db.relationship('Order', backref='product_item', lazy=True)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    date_ordered = db.Column(db.DateTime, default=datetime.utcnow)
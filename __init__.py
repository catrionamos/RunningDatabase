from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Application Configuration
app.config['SECRET_KEY'] = 'running-devops-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:postgres_password@localhost:5432/running_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User Loader Callback for Flask-Login
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import Routes
from app import routes
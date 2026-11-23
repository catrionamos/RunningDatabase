from flask import Flask
from config import Config

#create the app and load the settings from config.py
app = Flask(__name__)
app.config.from_object(Config)

#import routes at the bottom to avoid circular imports
from app import routes

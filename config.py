#import os to read environment variables
import os

#settings for the flask app, the secret key is needed for forms and sessions
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "R7KD52MRB"

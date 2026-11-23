import os

#the secret key is needed for forms and sessions
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "R7KD52MRB"

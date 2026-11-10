from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class LogRunForm(FlaskForm):
    run_date = DateField('Date of Run', validators=[DataRequired()])
    distance_km = FloatField('Distance (km)', validators=[DataRequired(), NumberRange(min=0.1, max=200)])
    duration_minutes = IntegerField('Duration (minutes)', validators=[DataRequired(), NumberRange(min=1, max=1500)])
    notes = StringField('Notes')
    submit = SubmitField('Log Run')

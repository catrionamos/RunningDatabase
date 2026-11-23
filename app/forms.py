#import FlaskForm class from flask_wtf package
from flask_wtf import FlaskForm
#import the field types used in our forms
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FloatField, IntegerField, DateField
#import validators to check the data entered
from wtforms.validators import DataRequired, NumberRange

#form for the login page
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#form to filter running programs by fitness level
class ProgramSearchForm(FlaskForm):
    level = SelectField('Fitness Level', choices=[('All', 'All'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('All Levels', 'All Levels')])
    submit = SubmitField('Find Programs')

#form to log a new run, distance and time must be within a sensible range
class LogRunForm(FlaskForm):
    run_date = DateField('Date of Run', validators=[DataRequired()])
    distance_km = FloatField('Distance (km)', validators=[DataRequired(), NumberRange(min=0.1, max=200)])
    duration_minutes = IntegerField('Duration (minutes)', validators=[DataRequired(), NumberRange(min=1, max=1500)])
    notes = StringField('Notes')
    submit = SubmitField('Log Run')

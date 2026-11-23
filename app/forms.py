#import FlaskForm class from flask_wtf package
from flask_wtf import FlaskForm
#import the field types used in our forms
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
#import validators to check the data entered
from wtforms.validators import DataRequired

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

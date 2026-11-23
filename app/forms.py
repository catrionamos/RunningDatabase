#import FlaskForm class from flask_wtf package
from flask_wtf import FlaskForm
#import the field types used in our forms
from wtforms import SelectField, SubmitField

#form to filter running programs by fitness level
class ProgramSearchForm(FlaskForm):
    level = SelectField('Fitness Level', choices=[('All', 'All'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('All Levels', 'All Levels')])
    submit = SubmitField('Find Programs')

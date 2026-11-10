from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class ProgramSearchForm(FlaskForm):
    level = SelectField('Fitness Level', choices=[('All', 'All'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('All Levels', 'All Levels')])
    submit = SubmitField('Find Programs')

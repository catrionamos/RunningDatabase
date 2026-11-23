#import render_template, redirect, session and flash functions from flask
from flask import render_template, redirect, session, flash
#import app variable from app package
from app import app
#import the form classes from our forms.py file
from app.forms import ProgramSearchForm
#import psycopg2 to connect to database
import psycopg2

#create an association for the URL /
@app.route('/')

#create an association for the URL /index
@app.route('/index')

#create the index page to display intro text
def index():
    return render_template('index.html', title='Running Database')

#create an association for the URL /about
@app.route('/about')

#create the about page to display information about the web service
def about():
    return render_template('about.html', title='About Us')

#create an association for the URL /programs
@app.route('/programs', methods = ['GET', 'POST'])

#Feature 1 - create the programs page to find a running program by fitness level
def programs():
    #create an instance of a ProgramSearchForm obj and store in a variable called form
    form = ProgramSearchForm()

    #connect to the database and create a cursor obj
    conn = db_connect()
    cur = conn.cursor()

    #if the user picked a level, sql code to retrieve only the programs for that level
    if form.validate_on_submit() and form.level.data != 'All':
        sql = "select program_name, target_level, duration_weeks, description from programs where target_level ='"+form.level.data+"' order by duration_weeks;"
    #otherwise sql code to retrieve every program
    else:
        sql = "select program_name, target_level, duration_weeks, description from programs order by target_level, duration_weeks;"

    #run the sql in our db
    cur.execute(sql)

    #retrieve the results
    program_list = cur.fetchall()

    #close db elements
    cur.close()
    conn.close()

    return render_template('programs.html', title='Find a Program', form = form, programs = program_list)

#create the database connection
def db_connect():
    return psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

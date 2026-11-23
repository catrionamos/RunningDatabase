#import render_template, redirect, session and flash functions from flask
from flask import render_template, redirect, session, flash
#import app variable from app package
from app import app
#import the form classes from our forms.py file
from app.forms import LoginForm, ProgramSearchForm
#import psycopg2 to connect to database
import psycopg2
#import encryption to hash passwords and compare during user login
from werkzeug.security import check_password_hash

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

#create an association for the URL /shop
@app.route('/shop')

#Feature 2 - create the shop page to display running gear from the products table
def shop():
    #connect to the database and create a cursor obj
    conn = db_connect()
    cur = conn.cursor()

    #sql code to retrieve all the products
    sql = "select product_name, category, price, stock_quantity from products order by category, product_name;"

    #run the sql in our db
    cur.execute(sql)

    #retrieve the results
    product_list = cur.fetchall()

    #close db elements
    cur.close()
    conn.close()

    return render_template('shop.html', title='Shop', products = product_list)

#create an association for the URL /login
@app.route('/login', methods = ['GET', 'POST'])

#Feature 3 - create the login page to display web form for user
def login():
    #create an instance of a LoginForm obj and store in a variable called form
    form = LoginForm()

    #receive valid data from the login.html
    if form.validate_on_submit():

        #create variables to hold user data provided in login.html, apostrophes are escaped so the sql does not break
        username = form.username.data.replace("'", "''")
        password = form.password.data

        #connect to the database and create a cursor obj
        conn = db_connect()
        cur = conn.cursor()

        #sql code to retrieve password for provided username
        sql = "select password from users where userid ='"+username+"';"

        #run the sql in our db
        cur.execute(sql)

        #retrieve the results
        user_data = cur.fetchone()

        #close db elements
        cur.close()
        conn.close()

        #check if user_data is valid and if so check password provided is correct
        if user_data and check_password_hash(user_data[0], password):
            #create a session with the username
            session['user_id'] = username
            flash("Logged in successfully!")
            return redirect('/index')
        else:
            flash("Invalid username or password.")

    return render_template('login.html', title="Sign In", form = form)

#create an association for the URL /logout
@app.route('/logout')

#create the logout page to clear the user session
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect('/index')

#create the database connection
def db_connect():
    return psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

#import render_template, redirect, session and flash functions from flask
from flask import render_template, redirect, session, flash
#import app variable from app package
from app import app
#import the form classes from our forms.py file
from app.forms import LoginForm, ProgramSearchForm, LogRunForm
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
            return redirect('/log_run')
        else:
            flash("Invalid username or password.")

    return render_template('login.html', title="Sign In", form = form)

#create an association for the URL /log_run
@app.route('/log_run', methods = ['GET', 'POST'])

#Feature 4 - create the log a run page so a logged in user can save a run and see their runs
def log_run():
    #check the user has a session, if not send them to the login page
    if 'user_id' not in session:
        flash("Please log in to log a run.")
        return redirect('/login')

    #create an instance of a LogRunForm obj and store in a variable called form
    form = LogRunForm()

    #create a variable to hold the username from the session
    username = session['user_id']

    #connect to the database and create a cursor obj
    conn = db_connect()
    cur = conn.cursor()

    #receive valid data from the log_run.html
    if form.validate_on_submit():
        #sql code to insert the new run into the runs table
        sql = "insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('"+username+"','"+str(form.run_date.data)+"',"+str(form.distance_km.data)+","+str(form.duration_minutes.data)+",'"+form.notes.data.replace("'", "''")+"');"

        #run the sql in our db and commit the changes
        cur.execute(sql)
        conn.commit()

        #close db elements
        cur.close()
        conn.close()

        flash("Run saved!")
        return redirect('/log_run')

    #sql code to retrieve all the runs for the logged in user, newest first
    sql = "select run_date, distance_km, duration_minutes, notes from runs where userid ='"+username+"' order by run_date desc;"

    #run the sql in our db
    cur.execute(sql)

    #retrieve the results
    run_list = cur.fetchall()

    #close db elements
    cur.close()
    conn.close()

    return render_template('log_run.html', title='Log a Run', form = form, runs = run_list)

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

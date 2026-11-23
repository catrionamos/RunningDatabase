#import render_template, redirect, session and flash functions from flask
from flask import render_template, redirect, session, flash
#import app variable from app package
from app import app
#import the form classes from our forms.py file
from app.forms import LoginForm, ProgramSearchForm, LogRunForm
#import psycopg2 to connect to database
import psycopg2
#import encryption to compare hashed passwords during user login
from werkzeug.security import check_password_hash
#import os for connecting to db through Docker
import os

#home page of the web service
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Running Database')

#about us page of the web service
@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

#Feature 1 - find a running program by fitness level
@app.route('/programs', methods = ['GET', 'POST'])
def programs():
    form = ProgramSearchForm()
    conn = db_connect()
    cur = conn.cursor()
    #only show the programs for the level picked, otherwise show them all
    if form.validate_on_submit() and form.level.data != 'All':
        sql = "select program_name, target_level, duration_weeks, description from programs where target_level ='"+form.level.data+"' order by duration_weeks;"
    else:
        sql = "select program_name, target_level, duration_weeks, description from programs order by target_level, duration_weeks;"
    cur.execute(sql)
    program_list = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('programs.html', title='Find a Program', form = form, programs = program_list)

#Feature 2 - shop page showing running gear from the products table
@app.route('/shop')
def shop():
    conn = db_connect()
    cur = conn.cursor()
    sql = "select product_name, category, price, stock_quantity from products order by category, product_name;"
    cur.execute(sql)
    product_list = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('shop.html', title='Shop', products = product_list)

#Feature 3 - login page that checks the hashed password in the users table
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #escape any apostrophes so the sql statement does not break
        username = form.username.data.replace("'", "''")
        password = form.password.data
        conn = db_connect()
        cur = conn.cursor()
        sql = "select password from users where userid ='"+username+"';"
        cur.execute(sql)
        user_data = cur.fetchone()
        cur.close()
        conn.close()
        #compare the password entered with the hashed password stored in the database
        if user_data and check_password_hash(user_data[0], password):
            #store the user in the session so they stay logged in
            session['user_id'] = username
            flash("Logged in successfully!")
            return redirect('/log_run')
        else:
            flash("Invalid username or password.")
    return render_template('login.html', title="Sign In", form = form)

#Feature 4 - log a run and see a list of your previous runs
@app.route('/log_run', methods = ['GET', 'POST'])
def log_run():
    #only logged in users can log a run
    if 'user_id' not in session:
        flash("Please log in to log a run.")
        return redirect('/login')
    form = LogRunForm()
    username = session['user_id']
    conn = db_connect()
    cur = conn.cursor()
    #insert the new run into the runs table
    if form.validate_on_submit():
        sql = "insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('"+username+"','"+str(form.run_date.data)+"',"+str(form.distance_km.data)+","+str(form.duration_minutes.data)+",'"+form.notes.data.replace("'", "''")+"');"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        flash("Run saved!")
        return redirect('/log_run')
    #get all the runs for the logged in user, newest first
    sql = "select run_date, distance_km, duration_minutes, notes from runs where userid ='"+username+"' order by run_date desc;"
    cur.execute(sql)
    run_list = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('log_run.html', title='Log a Run', form = form, runs = run_list)

#logout clears the session and returns to the home page
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect('/index')

#create the database connection
def db_connect():
    #use the database url from docker-compose when running in Docker
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        return psycopg2.connect(database_url)
    #otherwise connect to the local database
    return psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

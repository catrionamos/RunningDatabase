from flask import render_template, redirect, session, flash
from app import app
from app.forms import LoginForm, LogRunForm
import psycopg2
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Running Database')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        conn = db_connect()
        cur = conn.cursor()
        sql = "select password from users where userid ='"+username+"';"
        cur.execute(sql)
        user_data = cur.fetchone()
        cur.close()
        conn.close()
        if user_data and check_password_hash(user_data[0], password):
            session['user_id'] = username
            flash("Logged in successfully!")
            return redirect('/log_run')
        else:
            flash("Invalid username or password.")
    return render_template('login.html', title="Sign In", form = form)

@app.route('/log_run', methods = ['GET', 'POST'])
def log_run():
    if 'user_id' not in session:
        flash("Please log in to log a run.")
        return redirect('/login')
    form = LogRunForm()
    username = session['user_id']
    conn = db_connect()
    cur = conn.cursor()
    if form.validate_on_submit():
        sql = "insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('"+username+"','"+str(form.run_date.data)+"',"+str(form.distance_km.data)+","+str(form.duration_minutes.data)+",'"+form.notes.data+"');"
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        flash("Run saved!")
        return redirect('/log_run')
    sql = "select run_date, distance_km, duration_minutes, notes from runs where userid ='"+username+"' order by run_date desc;"
    cur.execute(sql)
    run_list = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('log_run.html', title='Log a Run', form = form, runs = run_list)

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect('/index')

def db_connect():
    return psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

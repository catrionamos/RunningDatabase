from flask import render_template
from app import app
from app.forms import ProgramSearchForm
import psycopg2

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Running Database')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/programs', methods = ['GET', 'POST'])
def programs():
    form = ProgramSearchForm()
    conn = db_connect()
    cur = conn.cursor()
    if form.validate_on_submit() and form.level.data != 'All':
        sql = "select program_name, target_level, duration_weeks, description from programs where target_level ='"+form.level.data+"' order by duration_weeks;"
    else:
        sql = "select program_name, target_level, duration_weeks, description from programs order by target_level, duration_weeks;"
    cur.execute(sql)
    program_list = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('programs.html', title='Find a Program', form = form, programs = program_list)

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

def db_connect():
    return psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

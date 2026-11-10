import psycopg2
import csv
from werkzeug.security import generate_password_hash

conn = psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

cur = conn.cursor()

path = './data/'

csv_file_programs = path+'programs.csv'
with open(csv_file_programs, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        sql = "insert into programs(program_id, program_name, target_level, duration_weeks, description) values('"+row[0]+"','"+row[1]+"','"+row[2]+"',"+row[3]+",'"+row[4]+"');"
        cur.execute(sql)
    csvfile.close()

csv_file_users = path+'userDetails.csv'
with open(csv_file_users, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        sql = "insert into users(userid, password, email, fitness_level, running_goal, program_id) values('"+row[0]+"','"+generate_password_hash(row[1])+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"');"
        cur.execute(sql)
    csvfile.close()

csv_file_products = path+'products.csv'
with open(csv_file_products, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        sql = "insert into products(product_id, product_name, category, price, stock_quantity) values('"+row[0]+"','"+row[1]+"','"+row[2]+"',"+row[3]+","+row[4]+");"
        cur.execute(sql)
    csvfile.close()

csv_file_runs = path+'runs.csv'
with open(csv_file_runs, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        sql = "insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('"+row[0]+"','"+row[1]+"',"+row[2]+","+row[3]+",'"+row[4]+"');"
        cur.execute(sql)
    csvfile.close()

csv_file_orders = path+'orders.csv'
with open(csv_file_orders, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        sql = "insert into orders(order_id, userid, product_id, quantity, order_date) values('"+row[0]+"','"+row[1]+"','"+row[2]+"',"+row[3]+",'"+row[4]+"');"
        cur.execute(sql)
    csvfile.close()

print("Database populated with programs, users, products, runs and orders.")

conn.commit()

cur.close()

conn.close()

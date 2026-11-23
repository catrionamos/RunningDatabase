#import packages to allow to open a csv file and a connection to postgreSQL database
import psycopg2
import csv
#import security to encrypt password before inserting in to table.
from werkzeug.security import generate_password_hash

#connect to the database
conn = psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

#create a cursor/pointer
cur = conn.cursor()

#store the path of the csv files in a variable
path = './data/'

csv_file_programs = path+'programs.csv'
#open data file and read in data row by row to insert into table programs
with open(csv_file_programs, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        #create the sql code to insert the values into the table programs
        sql = "insert into programs(program_id, program_name, target_level, duration_weeks, description) values('"+row[0]+"','"+row[1]+"','"+row[2]+"',"+row[3]+",'"+row[4]+"');"

        #execute the sql code
        cur.execute(sql)

    #close the csv file
    csvfile.close()

csv_file_users = path+'userDetails.csv'
#open data file and read in data row by row to insert into table users
with open(csv_file_users, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        #create the sql code to insert the values into the table users, the password is hashed first
        sql = "insert into users(userid, password, email, fitness_level, running_goal, program_id) values('"+row[0]+"','"+generate_password_hash(row[1])+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"');"

        #execute the sql code
        cur.execute(sql)

    #close the csv file
    csvfile.close()

csv_file_products = path+'products.csv'
#open data file and read in data row by row to insert into table products
with open(csv_file_products, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        #create the sql code to insert the values into the table products
        sql = "insert into products(product_id, product_name, category, price, stock_quantity) values('"+row[0]+"','"+row[1]+"','"+row[2]+"',"+row[3]+","+row[4]+");"

        #execute the sql code
        cur.execute(sql)

    #close the csv file
    csvfile.close()

csv_file_runs = path+'runs.csv'
#open data file and read in data row by row to insert into table runs
with open(csv_file_runs, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        #create the sql code to insert the values into the table runs
        sql = "insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('"+row[0]+"','"+row[1]+"',"+row[2]+","+row[3]+",'"+row[4]+"');"

        #execute the sql code
        cur.execute(sql)

    #close the csv file
    csvfile.close()

csv_file_orders = path+'orders.csv'
#open data file and read in data row by row to insert into table orders
with open(csv_file_orders, newline='') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        #create the sql code to insert the values into the table orders
        sql = "insert into orders(order_id, userid, product_id, quantity, order_date) values('"+row[0]+"','"+row[1]+"','"+row[2]+"',"+row[3]+",'"+row[4]+"');"

        #execute the sql code
        cur.execute(sql)

    #close the csv file
    csvfile.close()

print("Database populated with programs, users, products, runs and orders.")

#commit the sql code to the database
conn.commit()
#close the cursor object in the database
cur.close()
#close the database connection.
conn.close()

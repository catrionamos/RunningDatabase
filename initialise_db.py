#import psycopg2 to connect to postgresql
import psycopg2

#connect to the default postgres database first so we can create running_db
conn = psycopg2.connect(database="postgres", user="postgres", password="Phoebe2004", host="localhost", port="5432")

#create database cannot run inside a transaction so autocommit is turned on
conn.autocommit = True

#create a cursor/pointer
cur = conn.cursor()

#sql code to check if running_db already exists, and create it if it does not
cur.execute("select 1 from pg_database where datname='running_db';")
if cur.fetchone() is None:
    cur.execute("create database running_db;")
    print("Database running_db created.")
else:
    print("Database running_db already exists.")

#close the cursor object and the database connection
cur.close()
conn.close()

#connect to the new running_db database
conn = psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")

#create a cursor/pointer
cur = conn.cursor()

#sql code to drop the old tables so the script can be run again
cur.execute("drop table if exists orders, runs, products, users, programs cascade;")

#open schema.sql, read in the sql code and execute it to create the tables
sql_file = open('schema.sql', 'r')
cur.execute(sql_file.read())

#close the sql file
sql_file.close()
print("Tables programs, users, products, runs and orders created.")

#commit the sql code to the database
conn.commit()
#close the cursor object in the database
cur.close()
#close the database connection.
conn.close()

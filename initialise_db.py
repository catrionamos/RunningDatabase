#import psycopg2 to connect to postgresql
import psycopg2

#connect to the default postgres database first so we can create running_db
conn = psycopg2.connect(database="postgres", user="postgres", password="Phoebe2004", host="localhost", port="5432")

#create database cannot run inside a transaction so autocommit is turned on
conn.autocommit = True

cur = conn.cursor()

#only create running_db if it does not already exist
cur.execute("select 1 from pg_database where datname='running_db';")
if cur.fetchone() is None:
    cur.execute("create database running_db;")
    print("Database running_db created.")
else:
    print("Database running_db already exists.")

cur.close()
conn.close()

#connect to the new running_db database
conn = psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")
cur = conn.cursor()

#drop the old tables so the script can be run again
cur.execute("drop table if exists orders, runs, products, users, programs cascade;")

#read the sql code in schema.sql and run it to create the tables
sql_file = open('schema.sql', 'r')
cur.execute(sql_file.read())
sql_file.close()
print("Tables programs, users, products, runs and orders created.")

#save the changes
conn.commit()

cur.close()

conn.close()

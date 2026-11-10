import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="Phoebe2004", host="localhost", port="5432")

conn.autocommit = True

cur = conn.cursor()

cur.execute("select 1 from pg_database where datname='running_db';")
if cur.fetchone() is None:
    cur.execute("create database running_db;")
    print("Database running_db created.")
else:
    print("Database running_db already exists.")

cur.close()
conn.close()

conn = psycopg2.connect(database="running_db", user="postgres", password="Phoebe2004", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("drop table if exists orders, runs, products, users, programs cascade;")

sql_file = open('schema.sql', 'r')
cur.execute(sql_file.read())
sql_file.close()
print("Tables programs, users, products, runs and orders created.")

conn.commit()

cur.close()

conn.close()

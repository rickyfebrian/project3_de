import psycopg2
import csv

#connect db
conn = psycopg2.connect("host=localhost dbname=project3_de user=userproject3 password=digitalskola")
cur = conn.cursor()

# create table
cur.execute(
    """
    create table if not exists users_using_copy(
    id serial PRIMARY KEY,
    email text,
    name text,
    phone text,
    postal_code text)
    """
)

with open('/home/oce/digitalskola/project/project3/users_w_postal_code.csv', 'r') as f :
    next(f)
    cur.copy_from(f, 'users_using_copy', sep=',', columns=('email','name','phone','postal_code'))

conn.commit()
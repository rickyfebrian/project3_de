import psycopg2
import csv

#connect db
conn = psycopg2.connect("host=localhost dbname=project3_de user=userproject3 password=digitalskola")
cur = conn.cursor()

# create table
cur.execute(
    """
    create table if not exists latihan_users(
    id serial PRIMARY KEY,
    email text,
    name text,
    phone text,
    postal_code text)
    """
)

with open('/home/oce/digitalskola/project/project3/users_w_postal_code.csv') as f :
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        cur.execute('INSERT INTO latihan_users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING', row)

conn.commit()
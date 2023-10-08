import pandas as pd
from sqlalchemy import create_engine
import psycopg2

df = pd.read_csv('/home/oce/digitalskola/project/project3/users_w_postal_code.csv', sep=',')

engine = create_engine('postgresql://userproject3:digitalskola@127.0.0.1:5432/project3_de')
df.to_sql("from_file_table", engine)
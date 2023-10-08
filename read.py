import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql://userproject3:digitalskola@127.0.0.1:5432/project3_de')

df_read = pd.read_sql("select * from from_file_table", engine)

print(df_read)
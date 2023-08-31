import sqlite3
import pandas as pd
path1 = 'data.csv'

df = pd.read_csv(path1)

df.columns = df.columns.str.strip()

connection = sqlite3.connect('Housing')

df.to_sql('data', connection, if_exists='replace')
connection.close()
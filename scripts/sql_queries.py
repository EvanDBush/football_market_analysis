import sqlite3
import pandas as pd

query = 'SELECT * FROM games LIMIT 10'

def query_db(query):

    with sqlite3.connect('./football.db') as football_db:
        df = pd.read_sql(query, football_db)
    print(df)
import sqlite3
import pandas as pd

test_query = 'SELECT * FROM games LIMIT 10'

# Joined table queries
club_value_query = """
SELECT 
    clubs.club_id, 
    clubs.name,
    SUM(player_valuations.market_value_in_eur) AS club_market_value
FROM
    player_valuations
JOIN
    clubs ON player_valuations.current_club_id = clubs.club_id
GROUP BY
    clubs.name
ORDER BY 
    club_market_value DESC
LIMIT 
    10;
"""
player_recent_date_query = """

SELECT 
    player_id,
    MAX(date) AS most_recent_date
FROM 
    player_valuations
GROUP BY
    player_id
"""


def query_db(query):

    with sqlite3.connect('./football.db') as football_db:
        df = pd.read_sql(query, football_db)
    return df 
    

query_db(club_value_query)
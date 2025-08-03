import sqlite3
import pandas as pd

# Connection to database
connection = sqlite3.connect('./football.db')

# Read .csv into pandas dataframe
appearances_df = pd.read_csv('./data/raw/appearances.csv')

# Write dataframe to football database
appearances_df.to_sql('appearances', connection, if_exists='replace')

club_games_df = pd.read_csv('./data/raw/club_games.csv')
club_games_df.to_sql('club_games', connection, if_exists='replace')

clubs_df = pd.read_csv('./data/raw/clubs.csv')
clubs_df.to_sql('clubs', connection, if_exists='replace')

competitions_df = pd.read_csv('./data/raw/competitions.csv')
competitions_df.to_sql('competitions', connection, if_exists='replace')

game_events_df = pd.read_csv('./data/raw/game_events.csv')
game_events_df.to_sql('game_events',connection, if_exists='replace')

game_lineups_df= pd.read_csv('./data/raw/game_lineups.csv')
game_lineups_df.to_sql('game_lineups', connection, if_exists='replace')

games_df = pd.read_csv('./data/raw/games.csv')
games_df.to_sql('games', connection, if_exists='replace')

player_valuations_df = pd.read_csv('./data/raw/player_valuations.csv')
player_valuations_df.to_sql('player_valuations', connection, if_exists='replace')

players_df = pd.read_csv('./data/raw/players.csv')
players_df.to_sql('players', connection, if_exists='replace')

transfers_df = pd.read_csv('./data/raw/transfers.csv')
transfers_df.to_sql('transfers', connection, if_exists='replace')
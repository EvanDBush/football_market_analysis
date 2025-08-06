import pandas as pd

# Appearances Table
appearances_df = pd.read_csv('./data/raw/appearances.csv')

# Convert date column to datetime
appearances_df['date'] = pd.to_datetime(appearances_df['date'])
# 2. drop 6 null values.
appearances_df = appearances_df.dropna()
appearances_df.to_csv('./data/clean/appearances.csv', index=False)

# Club Games Table
club_games_df = pd.read_csv('../data/raw/club_games.csv')
# remove rows with missing ids
# fill missing position values
# fill missing managers names
# drop remaining nulls 

# Clubs Table

# Competitions Table

# Game Events Table

# Game Line-ups Table

# Games Table

# Player Valuations Table

# Players Table

# Transfers Table
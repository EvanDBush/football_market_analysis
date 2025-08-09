import pandas as pd

# EDA Functions

# Cleaning Functions
def clean_player_valuations(df):
    """This function takes in the player_valuations dataframe, 
    applies cleaning logic and writes to .csv file."""
    # change date dtype to datetime
    df['date'] = pd.to_datetime(df['date'])
    print('Changed date column dtype to datetime')
    df.to_csv('./data/clean/player_valuations.csv', index=False)
    print('Cleaned player valuations table written to csv')

def clean_clubs(df):
    """This function takes in the clubs dataframe, 
    applies cleaning logic and writes to .csv file."""

    # calculate club market value
    
    # use player valuations and current club id
    # replace missing average age with domestic league average age.
    # drop url and filename columns
    # calculate missing foreigners percentage from squad size and foreigners number.
    df.to_csv('./data/clean/clubs.csv')
    print('Cleaned clubs table written to csv')
    
# SQL Query Functions
# Plotting Functions
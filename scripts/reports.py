import pandas as pd

table_list = ['appearances', 'club_games', 'clubs', 'competitions', 'game_events',
              'game_lineups', 'games', 'player_valuations', 'players', 'transfers']

def create_dataframe(table_name, folder):
    filename = table_name + '.csv'
    filepath = f'./data/{folder}/{filename}'
    df = pd.read_csv(filepath)
    return df

def eda_report(table_name, folder):
    df = create_dataframe(table_name, folder)
    print(f'The {table_name} table has {df.shape[0]} rows and {df.shape[1]} columns.')
    print(f'The column names and data types are: \n{df.dtypes} ')

def get_all_eda_reports(table_list, folder):
    for table in table_list:
        eda_report(table, folder )

get_all_eda_reports(table_list, 'raw')
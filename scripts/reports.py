import pandas as pd

table_list = ['appearances', 'club_games', 'clubs', 'competitions', 'game_events',
              'game_lineups', 'games', 'player_valuations', 'players', 'transfers']

def create_dataframe(table_name, folder):
    filename = table_name + '.csv'
    filepath = f'./data/{folder}/{filename}'
    df = pd.read_csv(filepath)
    return df

def eda_info_describe(table_name, folder):
    df= create_dataframe(table_name, folder)
    column_info = df.info()
    print(column_info)


def eda_summary(table_name, folder):
    df = create_dataframe(table_name, folder)
    
    total_null_values = df.isnull().sum().sum() 
    total_duplicates = df.duplicated().sum()

    print(
        f'''
    The {table_name} table has {df.shape[0]} rows and {df.shape[1]} columns.
    
    The column names are: \n{'\n'.join(df.columns)}
    
    There are {total_null_values} null values. 
    
    There are {total_duplicates} duplicates.
        ''')

def numeric_columns_report(table_name, folder):
    df = create_dataframe(table_name, folder)
    df = df.add_prefix(table_name + '.')
    descriptive_df = df.describe().round(2).T
    print(descriptive_df)
    return descriptive_df
    
    
def get_all_eda_reports(table_list, folder):
    for table in table_list:
        eda_summary(table, folder )

def get_all_numeric_reports(table_list, folder):
    total_report_df = pd.DataFrame()

    for table in table_list:
        df = numeric_columns_report(table, folder)
        total_report_df= pd.concat([total_report_df, df])
    
    print(total_report_df)

#eda_summary('club_games', 'raw')
#numeric_columns_report('club_games', 'raw')
#get_all_eda_reports(table_list, 'raw')
# numeric_columns_report('players', 'raw')
# numeric_columns_report('clubs', 'raw')
# numeric_columns_report('player_valuations', 'raw')
#get_all_numeric_reports(table_list, 'raw')
#eda_info_describe('games', 'raw')
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
    print(
        f'''
    The {table_name} table has {df.shape[0]} rows and {df.shape[1]} columns.
    
    There are {df.isnull().sum().sum()} null values. 
    
    There are {df.duplicated().sum()} duplicates.
    
    The column names are: \n{', '.join(df.columns)} 
        ''')
def numeric_columns_report(table_name, folder):
    df = create_dataframe(table_name, folder)
    df = df.add_prefix(table_name + '.')
    descriptive_df = df.describe().round(2).T
    return descriptive_df
    
    


def get_all_eda_reports(table_list, folder):
    for table in table_list:
        eda_report(table, folder )

def get_all_numeric_reports(table_list, folder):
    total_report_df = pd.DataFrame()

    for table in table_list:
        df = numeric_columns_report(table, folder)
        total_report_df= pd.concat([total_report_df, df])
    
    print(total_report_df)

#eda_report('appearances', 'raw')
#get_all_eda_reports(table_list, 'raw')
#numeric_columns_report('players', 'raw')
get_all_numeric_reports(table_list, 'raw')
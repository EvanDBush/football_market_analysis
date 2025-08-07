import pandas as pd

#__Appearances Table_____________________________________

#read csv to dataframe
appearances_df = pd.read_csv('./data/raw/appearances.csv')
# Convert date column to datetime
appearances_df['date'] = pd.to_datetime(appearances_df['date'])
# drop 6 null values.
appearances_df = appearances_df.dropna()
# write dataframe to clean csv
appearances_df.to_csv('./data/clean/appearances.csv', index=False)
print('Cleaned appearances table written to csv')

#__Club Games Table__________________________________

#read csv to dataframe
club_games_df = pd.read_csv('./data/raw/club_games.csv')
# drop records with no club and opponent id
club_games_df = club_games_df.dropna(subset=['club_id'])
# fill position columns with 0 to preserve positions available and mark for easy exclusion.
club_games_df['own_position'].fillna(0)
club_games_df['opponent_position'] = club_games_df['opponent_position'].fillna(0)
# fill own goal and opponent goal columns with 0 for 24 missing games
club_games_df['own_goals'] = club_games_df['own_goals'].fillna(0)
club_games_df['opponent_goals'] = club_games_df['opponent_goals'].fillna(0)
# fill missing managers name columns with 'unavailable' to preserve names recorded and mark for exclusion.
club_games_df['own_manager_name'] = club_games_df['own_manager_name'].fillna('unavailable')
club_games_df['opponent_manager_name'] = club_games_df['opponent_manager_name'].fillna('unavailable')
# write dataframe to clean csv
club_games_df.to_csv('./data/clean/club_games.csv', index=False)
print('Cleaned club games table written to csv')

#__Clubs Table____________________________________

#read csv to dataframe
clubs_df = pd.read_csv('./data/raw/clubs.csv')
# calculate club market value
# use player valuations and current club id
# replace missing average age with domestic league average age.
# drop url and filename columns
# calculate missing foreigners percentage from squad size and foreigners number.
clubs_df.to_csv('./data/clean/clubs.csv')
print('Cleaned clubs table written to csv')

# Competitions Table

#read csv to dataframe
competitions_df = pd.read_csv('./data/raw/competitions.csv')
# fill null values in country_name and domestic_league_code with "none" 
competitions_df['country_name'] = competitions_df['country_name'].fillna('unavailable')
competitions_df['domestic_league_code'] = competitions_df['domestic_league_code'].fillna('unavailable')
# write dataframe to clean csv
competitions_df.to_csv('./data/clean/competitions.csv', index=False)
print('Cleaned competitions table written to csv')

#__Game Events Table______________________________

#read csv to dataframe
game_events_df = pd.read_csv('./data/raw/game_events.csv')
#convert date to datetime dtype
game_events_df['date'] = pd.to_datetime(game_events_df['date'])
# fill missing description with "none"
game_events_df['description'] = game_events_df['description'].fillna('unavailable')
# fill missing player_in_id with 0
game_events_df['player_in_id'] = game_events_df['player_in_id'].fillna(0)
# fill player assist id with 0
game_events_df['player_assist_id'] = game_events_df['player_assist_id'].fillna(0)
# write dataframe to clean csv
game_events_df.to_csv('./data/clean/game_events.csv', index=False)
print('Cleaned game events table written to csv')


#__Game Line-ups Table___________________________________

# read csv to dataframe
game_lineups_df = pd.read_csv('./data/raw/game_lineups.csv')
# handle 3 nulls in position column
game_lineups_df['position'] = game_lineups_df['position'].fillna('unavailable')
# convert date column dtype to datetime
game_lineups_df['date'] = pd.to_datetime(game_lineups_df['date'])
# write to clean csv
game_lineups_df.to_csv('./data/clean/game_lineups.csv', index=False)
print('Cleaned game lineups table written to csv')

#__Games Table_________________________________________

# read csv to dataframe
games_df = pd.read_csv('./data/raw/games.csv')
#drop  9 games with missing home and away ids
games_df = games_df.dropna(subset=['home_club_id'])
# fill home_club and away_club position with 0
games_df['home_club_position'] = games_df['home_club_position'].fillna(0)
games_df['away_club_position'] = games_df['away_club_position'].fillna(0)
# fill home_club name and away_club name nulls with club id information

# replace home and away club manager nulls with "unavailable"
games_df['home_club_manager_name'] = games_df['home_club_manager_name'].fillna('unavailable')
# replace attendance nulls with home club attendance avg

# replace formation nulls with 0
games_df['home_club_formation'] = games_df['home_club_formation'].fillna(0)
games_df['away_club_formation'] = games_df['away_club_formation'].fillna(0)
# replace aggregate nulls with 0
games_df['aggregate'] = games_df['aggregate'].fillna(0)
# write dataframe to clean csv
games_df.to_csv('./data/clean/games.csv', index=False)
print('Cleaned games table written to csv')

#__Player Valuations Table__________________________

#read csv to dataframe
player_valuations_df = pd.read_csv('./data/raw/player_valuations.csv')
# change date dtype to datetime
player_valuations_df['date'] = pd.to_datetime(player_valuations_df['date'])
# This table has no nulls or duplicates
# write dataframe to clean csv
player_valuations_df.to_csv('./data/clean/player_valuations.csv', index=False)
print('Cleaned player valuations table written to csv')



#__Players Table_____________________________________

# read csv to dataframe
players_df = pd.read_csv('./data/raw/players.csv')
# handle 2062 missing first name
first_part_of_name = players_df['name'].str.split(' ').str[0]
players_df['first_name'] = players_df['first_name'].fillna(first_part_of_name)
# fill null in date_of_birth with '1900-01-01'
players_df['date_of_birth'] = players_df['date_of_birth'].fillna('1900-01-01 00:00:00')
# change date_of_birth to datetime
players_df['date_of_birth'] = pd.to_datetime(players_df['date_of_birth'])
# fill null in country_of_birth with "unavailable"
players_df['country_of_birth'] = players_df['country_of_birth'].fillna('unavailable')
# fill null in city_of_birth with "unavailable"
players_df['city_of_birth'] = players_df['city_of_birth'].fillna('unavailable')
# fill null in country_of_citizenship with "unavailable"
players_df['country_of_citizenship'] = players_df['country_of_citizenship'].fillna('unavailable') 
# fill null in sub-position with "none"
players_df['sub_position'] = players_df['sub_position'].fillna('unavailable')
# fill null in foot with "unavailable"
players_df['foot'] = players_df['foot'].fillna('unavailable')
# fill null in height with average height
average_height = players_df['height_in_cm'].mean()
players_df['height_in_cm'] = players_df['height_in_cm'].fillna(average_height)
# fill null in contract_expiration_date with '1901-01-01'
players_df['contract_expiration_date'] = players_df['contract_expiration_date'].fillna('1901-01-01 00:00:00')
# fill null in agent_name with 'unavailable'
players_df['agent_name'] = players_df['agent_name'].fillna('unavailable')
# fill null in market_value_in_eur with 0
players_df['market_value_in_eur'] = players_df['market_value_in_eur'].fillna(0)
# fill null in highest_market_value in eur with 0
players_df['highest_market_value_in_eur'] = players_df['highest_market_value_in_eur'].fillna(0)
# write dataframe to clean csv
players_df.to_csv('./data/clean/players.csv', index=False)
print('Cleaned players table written to csv')

#__Transfers Table________________________________

# read csv to dataframe
transfers_df = pd.read_csv('./data/raw/transfers.csv')
# convert transfer_date to datetime
transfers_df['transfer_date'] = pd.to_datetime(transfers_df['transfer_date'])
# fill null in transfer_fee with 0
transfers_df['transfer_fee'] = transfers_df['transfer_fee'].fillna(0)
# fill null in market_value_in_eur with 0
transfers_df['market_value_in_eur'] = transfers_df['market_value_in_eur'].fillna(0)
# write dataframe to clean csv
transfers_df.to_csv('./data/clean/transfers.csv', index=False)
print('Cleaned players table written to csv')
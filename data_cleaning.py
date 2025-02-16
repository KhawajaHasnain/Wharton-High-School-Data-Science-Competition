import pandas as pd

games_data_df = pd.read_excel('Data\games_2022.xlsx', sheet_name='games_2022')

games_data_cleaned = games_data_df.copy()

games_data_cleaned.fillna({
    'FGA_2': 0, 'FGM_2': 0, 'FGA_3': 0, 'FGM_3': 0, 'FTA': 0, 'FTM': 0, 'AST': 0,
    'attendance': 0, 'rest_days': 0, 'tz_dif_H_E': 0, 'prev_game_dist': 0, 'travel_dist': 0
}, inplace=True)

games_data_cleaned.dropna(subset=['game_id', 'team'], inplace=True)

games_data_cleaned.drop_duplicates(subset=['game_id', 'team'], inplace=True)

games_data_cleaned['game_date'] = pd.to_datetime(games_data_cleaned['game_date'], errors='coerce')

numeric_columns = ['FGA_2', 'FGM_2', 'FGA_3', 'FGM_3', 'FTA', 'FTM', 'AST', 'attendance', 'rest_days', 
                   'tz_dif_H_E', 'prev_game_dist', 'travel_dist']
games_data_cleaned[numeric_columns] = games_data_cleaned[numeric_columns].apply(pd.to_numeric, errors='coerce')

games_data_cleaned.to_excel('Data\cleaned_games_data.xlsx', index=False)

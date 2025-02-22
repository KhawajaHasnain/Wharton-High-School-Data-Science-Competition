import pandas as pd

games_data_cleaned = pd.read_excel('Data\games_2022.xlsx', sheet_name='games_2022')

games_data_cleaned['won_game'] = games_data_cleaned['team_score'] > games_data_cleaned['opponent_score']

team_summary = games_data_cleaned.groupby('team').agg(
    games_played=('game_id', 'count'),
    games_won=('won_game', 'sum'),
    total_FGA_2=('FGA_2', 'sum'),
    total_FGM_2=('FGM_2', 'sum'),
    total_FGA_3=('FGA_3', 'sum'),
    total_FGM_3=('FGM_3', 'sum'),
    total_FTA=('FTA', 'sum'),
    total_FTM=('FTM', 'sum'),
    total_AST=('AST', 'sum'),
    total_BLK=('BLK', 'sum'),
    total_STL=('STL', 'sum'),
    total_TOV=('TOV', 'sum'),
    total_TOV_team=('TOV_team', 'sum'),
    total_DREB=('DREB', 'sum'),
    total_OREB=('OREB', 'sum'),
    total_F_tech=('F_tech', 'sum'),
    total_F_personal=('F_personal', 'sum'),
    total_rest_days=('rest_days', 'sum'),
    total_travel_distance=('travel_dist', 'sum')
).reset_index()

team_summary.to_excel('Data\team_summary_games_data.xlsx', index=False)

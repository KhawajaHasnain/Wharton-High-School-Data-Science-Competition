import pandas as pd

data = pd.read_excel('Data\team_summary_games_data.xlsx')

data['adjusted_FGM_3'] = data['total_FGM_3'] * 1.5
data['adjusted_FGA_3'] = data['total_FGA_3'] * 1.5

data['total_FGM'] = data['total_FGM_2'] + data['adjusted_FGM_3']
data['total_FGA'] = data['total_FGA_2'] + data['adjusted_FGA_3']

data['FG_success_percentage'] = (data['total_FGM'] / data['total_FGA']) * 100

data_sorted = data.sort_values(by='FG_success_percentage', ascending=False).reset_index(drop=True)

num_teams = len(data_sorted)
data_sorted['position'] = data_sorted.index + 1
data_sorted['points'] = num_teams + 1 - data_sorted['position']

data_sorted['points'] = data_sorted.groupby('FG_success_percentage')['points'].transform('max')

leaderboard = data_sorted[['team', 'FG_success_percentage', 'position', 'points']]
leaderboard.to_excel('Data\Leaderboards\field_goal_succes_percentage_leaderboard.xlsx', index=False)

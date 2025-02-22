import pandas as pd

file_path = 'Data\team_summary_games_data.xlsx'
data = pd.read_excel(file_path)
data['win_percentage'] = (data['games_won'] / data['games_played']) * 100
sorted_data = data.sort_values(by='win_percentage', ascending=False).reset_index(drop=True)
total_teams = len(sorted_data)
sorted_data['position'] = sorted_data.index + 1
sorted_data['points'] = total_teams - sorted_data['position'] + 1
sorted_data['points'] = sorted_data.groupby('win_percentage')['points'].transform('max')
leaderboard = sorted_data[['team', 'games_played', 'games_won', 'win_percentage', 'position', 'points']]
leaderboard.to_excel('Data\Leaderboards\win_percentage_leaderboard.xlsx', index=False)
print('Leaderboard created and saved!')

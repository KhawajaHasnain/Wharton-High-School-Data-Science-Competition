import pandas as pd

file_path = 'Data\team_summary_games_data.xlsx'
data = pd.read_excel(file_path)

data['avg_attacking_moves_per_game'] = (data['total_AST'] + data['total_OREB']) / data['games_played']

leaderboard = data[['team', 'avg_attacking_moves_per_game']].sort_values(by='avg_attacking_moves_per_game', ascending=False)

leaderboard['rank'] = leaderboard['avg_attacking_moves_per_game'].rank(method='min', ascending=False)

total_teams = len(leaderboard)
leaderboard['points'] = leaderboard['rank'].apply(lambda x: total_teams - int(x) + 1)

leaderboard = leaderboard.sort_values(by='rank')

output_file_path = 'Data\Leaderboards\average_total_attacking_moves_per_game_leaderboard.xlsx'
leaderboard.to_excel(output_file_path, index=False)

import pandas as pd

file_path = 'Data\team_summary_games_data.xlsx'
df = pd.read_excel(file_path)

df['total_points'] = (df['total_FGM_2'] * 2) + (df['total_FGM_3'] * 3)
df['avg_points_per_game'] = df['total_points'] / df['games_played']

leaderboard = df[['team', 'avg_points_per_game']].sort_values(by='avg_points_per_game', ascending=False).reset_index(drop=True)
num_teams = len(leaderboard)
leaderboard['rank'] = leaderboard.index + 1
leaderboard['points'] = num_teams - leaderboard['rank'] + 1
leaderboard['points'] = leaderboard.groupby('avg_points_per_game')['points'].transform('max')

output_file_path = 'Data\Leaderboards\avg_points_per_game_leaderboard.xlsx'
leaderboard.to_excel(output_file_path, index=False)
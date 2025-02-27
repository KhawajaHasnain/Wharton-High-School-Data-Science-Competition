import pandas as pd

file_path = 'Data\team_summary_games_data.xlsx'
df = pd.read_excel(file_path)

df['avg_turnovers_per_game'] = (df['total_TOV'] + df['total_TOV_team']) / df['games_played']

leaderboard = df[['team', 'avg_turnovers_per_game']].sort_values(by='avg_turnovers_per_game', ascending=False).reset_index(drop=True)

leaderboard['position'] = leaderboard.index + 1

leaderboard['points'] = leaderboard.groupby('avg_turnovers_per_game')['position'].transform('min')

output_file_path = 'Data\Leaderboards\average_total_number_of_turnovers_per_game_leaderboard.xlsx'
leaderboard.to_excel(output_file_path, index=False)

print(f'Leaderboard saved to {output_file_path}')

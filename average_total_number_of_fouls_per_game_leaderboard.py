import pandas as pd

file_path = 'Data\team_summary_games_data.xlsx'  
data = pd.read_excel(file_path)

data['avg_fouls_per_game'] = (data['total_F_tech'] + data['total_F_personal']) / data['games_played']

leaderboard = data[['team', 'avg_fouls_per_game']].sort_values(by='avg_fouls_per_game', ascending=False).reset_index(drop=True)

leaderboard['position'] = leaderboard.index + 1
leaderboard['points'] = leaderboard.groupby('avg_fouls_per_game')['position'].transform('min')

output_file_path = 'Data\Leaderboards\average_total_number_of_fouls_per_game_leaderboard.xlsx'
leaderboard.to_excel(output_file_path, index=False)
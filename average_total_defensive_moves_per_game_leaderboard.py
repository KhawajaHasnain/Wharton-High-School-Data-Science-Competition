import pandas as pd

file_path = 'Data\team_summary_games_data.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

df['Avg_Defensive_Moves_Per_Game'] = (df['total_BLK'] + df['total_STL'] + df['total_DREB']) / df['games_played']
df_sorted = df.sort_values(by='Avg_Defensive_Moves_Per_Game', ascending=False).reset_index(drop=True)
df_sorted['Position'] = df_sorted.index + 1
num_teams = len(df_sorted)
df_sorted['Points'] = df_sorted.groupby('Avg_Defensive_Moves_Per_Game')['Position'].transform('min').apply(lambda pos: num_teams - pos + 1)

output_file_path = 'Data\Leaderboards\average_total_defensive_moves_per_game_leaderboard.xlsx'
df_sorted[['team', 'Avg_Defensive_Moves_Per_Game', 'Position', 'Points']].to_excel(output_file_path, index=False)

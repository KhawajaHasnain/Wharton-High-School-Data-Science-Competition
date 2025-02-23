import pandas as pd

file_path = 'Data\team_summary_games_data.xlsx'
df = pd.read_excel(file_path)

df['FT_Success_Percentage'] = (df['total_FTM'] / df['total_FTA']) * 100

df_sorted = df.sort_values(by='FT_Success_Percentage', ascending=False).reset_index(drop=True)

df_sorted['Position'] = df_sorted.index + 1
df_sorted['Points'] = df_sorted['Position'].apply(lambda x: len(df_sorted) - x + 1)

df_sorted['Points'] = df_sorted.groupby('FT_Success_Percentage')['Points'].transform('max')

output_file_path = 'Data\Leaderboards\free_throw_success_percentage_leaderboard.xlsx'
df_sorted[['team', 'FT_Success_Percentage', 'Position', 'Points']].to_excel(output_file_path, index=False)
import pandas as pd

file_path = 'Wharton-High-School-Data-Science-Competition\Data\final_leaderboard.xlsx'  
data = pd.read_excel(file_path)

data['regional_rank'] = data.groupby('region')['Total Points'].rank(ascending=False, method='first')

north_teams = data[data['region'] == 'North'].nsmallest(16, 'regional_rank')[['team', 'regional_rank']]
south_teams = data[data['region'] == 'South'].nsmallest(16, 'regional_rank')[['team', 'regional_rank']]
west_teams = data[data['region'] == 'West'].nsmallest(16, 'regional_rank')[['team', 'regional_rank']]

north_teams.to_excel('Wharton-High-School-Data-Science-Competition\Data\north_top_16_teams.xlsx', index=False)
south_teams.to_excel('Wharton-High-School-Data-Science-Competition\Data\south_top_16_teams.xlsx', index=False)
west_teams.to_excel('Wharton-High-School-Data-Science-Competition\Data\west_top_16_teams.xlsx', index=False)
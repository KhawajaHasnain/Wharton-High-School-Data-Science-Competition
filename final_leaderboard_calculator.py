import pandas as pd

leaderboards = {}
files = {
    'Winning Percentage': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\win_percentage_leaderboard.xlsx', 20),
    'Average Points Per Game': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\avg_points_per_game_leaderboard.xlsx', 15),
    'Field Goal Success Percentage': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\field_goal_success_percentage_leaderboard.xlsx', 12),
    'Free Throw Success Percentage': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\free_throw_success_percentage_leaderboard.xlsx', 8),
    'Average Total Attacking Moves': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\average_total_attacking_moves_per_game_leaderboard.xlsx', 12),
    'Average Number of Defensive Moves': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\average_total_defensive_moves_per_game_leaderboard.xlsx', 12),
    'Average Number of Turnovers': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\average_total_number_of_turnovers_per_game_leaderboard.xlsx', 8),
    'Average Number of Fouls': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\average_total_number_of_fouls_per_game_leaderboard.xlsx', 5),
    'Average Largest Lead as a Ratio of Final Lead': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\average_of_largest_lead_as_a_ratio_final_lead_leaderboard.xlsx', 4),
    'Average Amount of Rest': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\average_amount_of_rest_leaderboard.xlsx', 2),
    'Average Confidence': ('Wharton-High-School-Data-Science-Competition\Data\Leaderboards\average_confidence_leaderboard.xlsx', 2)
}

for key, (file, weight) in files.items():
    df = pd.read_excel(file)
    points_column = "Points" if "Points" in df.columns else "points"
    df["Weighted Points"] = df[points_column] * (weight / 100)
    leaderboards[key] = df

final_leaderboard = leaderboards["Winning Percentage"][['team', 'Weighted Points']].copy()

for key in list(leaderboards.keys())[1:]:
    final_leaderboard = final_leaderboard.merge(leaderboards[key][['team', 'Weighted Points']], on='team', how='outer', suffixes=('', f'_{key}'))

final_leaderboard['Total Points'] = final_leaderboard.filter(like='Weighted Points').sum(axis=1)

final_leaderboard['Rank'] = final_leaderboard['Total Points'].rank(method='dense', ascending=False).astype(int)

final_leaderboard = final_leaderboard[['Rank', 'team', 'Total Points']].sort_values(by='Total Points', ascending=False).reset_index(drop=True)

final_leaderboard.to_excel('Wharton-High-School-Data-Science-Competition\Data\final_leaderboard.xlsx', index=False)

import pandas as pd

cleaned_games_file = "Data\cleaned_games_data.xlsx"

columns_needed = ['game_id', 'team', 'team_score', 'opponent_team_score', 'largest_lead']
games_data = pd.read_excel(cleaned_games_file, usecols=columns_needed)

games_data = games_data.rename(columns={"opponent_team_score": "opponent_score"})

games_data["lead"] = games_data["team_score"] - games_data["opponent_score"]

games_data["lead"] = games_data["lead"].replace(0, pd.NA)

games_data["largest_lead_ratio"] = games_data["largest_lead"] / games_data["lead"]

games_data = games_data.dropna(subset=["largest_lead_ratio"])

grouped_data = games_data.groupby("team")["largest_lead_ratio"].mean().reset_index()

grouped_data = grouped_data.rename(columns={"largest_lead_ratio": "avg_largest_lead_ratio"})

grouped_data = grouped_data.sort_values(by="avg_largest_lead_ratio", ascending=False).reset_index(drop=True)

grouped_data["rank"] = grouped_data["avg_largest_lead_ratio"].rank(method="min", ascending=False).astype(int)

num_teams = len(grouped_data)
grouped_data["points"] = (num_teams + 1 - grouped_data["rank"]).astype(int)

output_file = "Data\Leaderboards\average_of_largest_lead_as_a_ratio_final_lead_leaderboard.xlsx"
grouped_data.to_excel(output_file, index=False)
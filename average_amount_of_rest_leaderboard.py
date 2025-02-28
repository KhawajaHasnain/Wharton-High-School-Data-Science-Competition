import pandas as pd

team_summary_path = "Data\team_summary_games_data.xlsx"
cleaned_games_path = "Data\cleaned_games_data.xlsx"

team_summary_df = pd.read_excel(team_summary_path)
cleaned_games_df = pd.read_excel(cleaned_games_path)

cleaned_games_df["travel_time_days"] = cleaned_games_df["travel_dist"] / (100.5 * 24)
cleaned_games_df["adjusted_rest_days"] = cleaned_games_df["rest_days"] - cleaned_games_df["travel_time_days"]

average_rest_per_team = cleaned_games_df.groupby("team")["adjusted_rest_days"].mean().reset_index()
average_rest_per_team.columns = ["team", "average_rest_days"]

average_rest_per_team = average_rest_per_team.sort_values(by="average_rest_days", ascending=False).reset_index(drop=True)

average_rest_per_team["position"] = range(1, len(average_rest_per_team) + 1)

points_mapping = {}
unique_positions = average_rest_per_team["average_rest_days"].rank(method="dense", ascending=False)
max_points = len(unique_positions)

for rank, group in average_rest_per_team.groupby("average_rest_days"):
    points = max_points - (group["position"].min() - 1)
    points_mapping[rank] = points

average_rest_per_team["points"] = average_rest_per_team["average_rest_days"].map(points_mapping)

output_path = "Data\Leaderboards\average_amount_of_rest_leaderboard.xlsx"
average_rest_per_team.to_excel(output_path, index=False)

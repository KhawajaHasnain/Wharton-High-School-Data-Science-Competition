import pandas as pd

team_summary_df = pd.read_excel("Data\team_summary_games_data.xlsx")
cleaned_games_df = pd.read_excel("Data\cleaned_games_data.xlsx")

cleaned_games_df["confidence"] = cleaned_games_df["attendance"] * cleaned_games_df["home_away_NS"]

team_confidence = cleaned_games_df.groupby("team")["confidence"].mean().reset_index()
team_confidence.columns = ["team", "average_confidence"]

team_confidence = team_confidence.sort_values(by="average_confidence", ascending=False).reset_index(drop=True)
team_confidence["rank"] = range(1, len(team_confidence) + 1)

max_rank = len(team_confidence)
team_confidence["points"] = team_confidence["average_confidence"].rank(method="dense", ascending=False).astype(int)
team_confidence["points"] = max_rank + 1 - team_confidence["points"]

team_confidence.to_excel("Data\Leaderboards\average_confidence_leaderboard.xlsx", index=False)
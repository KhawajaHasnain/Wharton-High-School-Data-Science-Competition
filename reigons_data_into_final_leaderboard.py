import pandas as pd

leaderboard_df = pd.read_excel('Wharton-High-School-Data-Science-Competition\Data\final_leaderboard.xlsx')
region_groups_df = pd.read_excel('Wharton-High-School-Data-Science-Competition\Data\team_reigon_groups.xlsx')

merged_df = leaderboard_df.merge(region_groups_df, on='team', how='left')

merged_df['region'].fillna('East', inplace=True)

merged_df.to_excel('final_leaderboard_with_region.xlsx', index=False)

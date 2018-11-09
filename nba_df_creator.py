# coding: utf-8

import pandas as pd
import numpy as np

# read in csvs with results from last 3 seasons
nba17 = pd.read_csv('nba_h_a_17-18.csv', index_col='Team', usecols = ["Team", "Home Win %", "Home Margin of Victory (Average)", 
                                                                     "Away Win %", "Away Margin of Victory (Average)"])
nba16 = pd.read_csv('nba_h_a_16-17.csv', index_col='Team', usecols = ["Team", "Home Win %", "Home Margin of Victory (Average)", 
                                                                     "Away Win %", "Away Margin of Victory (Average)"])
nba15 = pd.read_csv('nba_h_a_15-16.csv', index_col='Team', usecols = ["Team", "Home Win %", "Home Margin of Victory (Average)", 
                                                                     "Away Win %", "Away Margin of Victory (Average)"])
# create combined df
nba_c = (np.array(nba17) + np.array(nba16) + np.array(nba15)) / 3
nba_df = pd.DataFrame(nba_c, nba17.index, nba17.columns)

# add columns to df that calculate (home - away) winning % and margin of victory
wp_diff = [x[0] - x[2] for x in nba_c]
mov_diff = [x[1] - x[3] for x in nba_c]
nba_df.insert(nba_df.shape[1], "Winning Percentage Difference", wp_diff)
nba_df.insert(nba_df.shape[1], "Margin of Victory Difference", mov_diff)

# get column maxes
# nba_df.idxmax()

# dfs sorted by calculated columns
nba_wp_sorted = nba_df.sort_values("Winning Percentage Difference", 0, False)
nba_mov_sorted = nba_df.sort_values("Margin of Victory Difference", 0, False)

# pairwise correlation between columns
nba_df_corr = nba_df.corr()

# write out csv
# nba_wp_sorted.to_csv('nba_wp_sorted.csv', columns=["Winning Percentage Difference", "Margin of Victory Difference"])
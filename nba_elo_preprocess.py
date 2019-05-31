# This script defines a pre-processing function.
# assumes import pandas as pd

# Pre-process given [df: pandas.DataFrame] for analysis
# Prints info and returns processed dataframe
def nba_elo_preprocess(df):

	df_nba_elo_copy = df.copy()

	# date -> datetime format
	# season -> string/ID (obj)
	# score1/2 -> int
	df_nba_elo_copy['date'] = df_nba_elo_copy['date'].astype('datetime64')
	df_nba_elo_copy['season'] = df_nba_elo_copy['season'].astype('str')
	df_nba_elo_copy['score1'] = df_nba_elo_copy['score1'].astype('Int32')
	df_nba_elo_copy['score2'] = df_nba_elo_copy['score2'].astype('Int32')

	# partial results - can drop since the season is not yet complete
	df_nba_elo_copy.drop(
	    index = df_nba_elo_copy.index[df_nba_elo_copy['elo1_post'].isnull()],
	    inplace = True
	)

	#CREATING DF FOR LOOKING AT TEAM PERFORMANCE / INDIV ELOS

	# melt teams into a single column
	df_nba_elo_copy = df_nba_elo_copy.melt(
	    id_vars = ['date', 'season', 'playoff', 'elo1_pre', 'elo1_post', 'elo2_pre', 'elo2_post'],
	    value_vars = ['team1', 'team2'], var_name = 'team_num', value_name = 'team'
	).sort_values('date').reset_index(drop=True)


	#craft single pre- and post-game/date elo
	df_nba_elo_copy.rename(
	    columns = {'elo1_pre': 'elo_pre', 'elo1_post': 'elo_post'},
	    inplace = True
	)

	#reassign values for "team 2"
	team2_idx = df_nba_elo_copy[df_nba_elo_copy['team_num'] == 'team2'].index
	df_nba_elo_copy.loc[team2_idx, 'elo_pre'] = df_nba_elo_copy.loc[team2_idx, 'elo2_pre']
	df_nba_elo_copy.loc[team2_idx, 'elo_post'] = df_nba_elo_copy.loc[team2_idx, 'elo2_post']

	df_nba_elo_copy = df_nba_elo_copy.drop(
	    columns = ['elo2_pre', 'elo2_post', 'team_num']
	)

	print('nba_elo_preprocess() output:')
	df_nba_elo_copy.info()
	
	return df_nba_elo_copy
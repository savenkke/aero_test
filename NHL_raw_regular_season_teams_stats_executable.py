def _parse():
	import requests
	
	headers = {
		'accept': 'application/json',
	}
	base_url = 'https://statsapi.web.nhl.com/api/v1/teams/'
	team_url = 'https://statsapi.web.nhl.com/api/v1/teams/{team_id}/stats'
	
	base_response = requests.get(base_url, params=params, headers=headers).json()
	team_ids = [team['id'] for team in base_response['teams']]
	
	team_response = requests.get(team_url.format(team_id=20), params=params, headers=headers).json()
	
	regularSeasonStats = {}
	for team_id in team_ids:
		team_response = requests.get(team_url.format(team_id=team_id), params=params, headers=headers).json()
		teamRegularSeasonStats = {"team_id": team_id}
		teamRegularSeasonStats["myFavouriteTeam"] = team_id==21
		# Большое страшное чудо-юдо, чтобы не съесть то, чего не ждём
		for type_block in team_response['stats']:
			if type_block["type"]["displayName"] == 'statsSingleSeason':
				teamRegularSeasonStats["team_name"] = type_block["splits"][0]["team"]["name"]
				teamRegularSeasonStats["gamesPlayed"] = type_block["splits"][0]["stat"].get("gamesPlayed")
				teamRegularSeasonStats["wins"] = type_block["splits"][0]["stat"].get("wins")
				teamRegularSeasonStats["losses"] = type_block["splits"][0]["stat"].get("losses")
				teamRegularSeasonStats["ot"] = type_block["splits"][0]["stat"].get("ot")
				teamRegularSeasonStats["pts"] = type_block["splits"][0]["stat"].get("pts")
				teamRegularSeasonStats["ptPctg"] = type_block["splits"][0]["stat"].get("ptPctg")
				teamRegularSeasonStats["goalsPerGame"] = type_block["splits"][0]["stat"].get("goalsPerGame")
				teamRegularSeasonStats["goalsAgainstPerGame"] = type_block["splits"][0]["stat"].get("goalsAgainstPerGame")
				teamRegularSeasonStats["evGGARatio"] = type_block["splits"][0]["stat"].get("evGGARatio")
				teamRegularSeasonStats["powerPlayPercentage"] = type_block["splits"][0]["stat"].get("powerPlayPercentage")
				teamRegularSeasonStats["powerPlayGoals"] = type_block["splits"][0]["stat"].get("powerPlayGoals")
				teamRegularSeasonStats["powerPlayGoalsAgainst"] = type_block["splits"][0]["stat"].get("powerPlayGoalsAgainst")
				teamRegularSeasonStats["powerPlayOpportunities"] = type_block["splits"][0]["stat"].get("powerPlayOpportunities")
				teamRegularSeasonStats["penaltyKillPercentage"] = type_block["splits"][0]["stat"].get("penaltyKillPercentage")
				teamRegularSeasonStats["shotsPerGame"] = type_block["splits"][0]["stat"].get("shotsPerGame")
				teamRegularSeasonStats["shotsAllowed"] = type_block["splits"][0]["stat"].get("shotsAllowed")
				teamRegularSeasonStats["winScoreFirst"] = type_block["splits"][0]["stat"].get("winScoreFirst")
				teamRegularSeasonStats["winOppScoreFirst"] = type_block["splits"][0]["stat"].get("winOppScoreFirst")
				teamRegularSeasonStats["winLeadFirstPer"] = type_block["splits"][0]["stat"].get("winLeadFirstPer")
				teamRegularSeasonStats["winLeadSecondPer"] = type_block["splits"][0]["stat"].get("winLeadSecondPer")
				teamRegularSeasonStats["winOutshootOpp"] = type_block["splits"][0]["stat"].get("winOutshootOpp")
				teamRegularSeasonStats["winOutshotByOpp"] = type_block["splits"][0]["stat"].get("winOutshotByOpp")
				teamRegularSeasonStats["faceOffsTaken"] = type_block["splits"][0]["stat"].get("faceOffsTaken")
				teamRegularSeasonStats["faceOffsWon"] = type_block["splits"][0]["stat"].get("faceOffsWon")
				teamRegularSeasonStats["faceOffsLost"] = type_block["splits"][0]["stat"].get("faceOffsLost")
				teamRegularSeasonStats["faceOffWinPercentage"] = type_block["splits"][0]["stat"].get("faceOffWinPercentage")
				teamRegularSeasonStats["shootingPctg"] = type_block["splits"][0]["stat"].get("shootingPctg")
				teamRegularSeasonStats["savePctg"] = type_block["splits"][0]["stat"].get("savePctg")
			if type_block["type"]["displayName"] == 'regularSeasonStatRankings' and not type_block["type"].get("game_type"):
				teamRegularSeasonStats["winsRanking"] = type_block["splits"][0]["stat"].get("wins")
				teamRegularSeasonStats["lossesRanking"] = type_block["splits"][0]["stat"].get("losses")
				teamRegularSeasonStats["otRanking"] = type_block["splits"][0]["stat"].get("ot")
				teamRegularSeasonStats["ptsRanking"] = type_block["splits"][0]["stat"].get("pts")
				teamRegularSeasonStats["ptPctgRanking"] = type_block["splits"][0]["stat"].get("ptPctg")
				teamRegularSeasonStats["goalsPerGameRanking"] = type_block["splits"][0]["stat"].get("goalsPerGame")
				teamRegularSeasonStats["goalsAgainstPerGameRanking"] = type_block["splits"][0]["stat"].get("goalsAgainstPerGame")
				teamRegularSeasonStats["evGGARatioRanking"] = type_block["splits"][0]["stat"].get("evGGARatio")
				teamRegularSeasonStats["powerPlayPercentageRanking"] = type_block["splits"][0]["stat"].get("powerPlayPercentage")
				teamRegularSeasonStats["powerPlayGoalsRanking"] = type_block["splits"][0]["stat"].get("powerPlayGoals")
				teamRegularSeasonStats["powerPlayGoalsAgainstRanking"] = type_block["splits"][0]["stat"].get("powerPlayGoalsAgainst")
				teamRegularSeasonStats["powerPlayOpportunitiesRanking"] = type_block["splits"][0]["stat"].get("powerPlayOpportunities")
				teamRegularSeasonStats["penaltyKillOpportunitiesRanking"] = type_block["splits"][0]["stat"].get("penaltyKillOpportunities")
				teamRegularSeasonStats["penaltyKillPercentageRanking"] = type_block["splits"][0]["stat"].get("penaltyKillPercentage")
				teamRegularSeasonStats["shotsPerGameRanking"] = type_block["splits"][0]["stat"].get("shotsPerGame")
				teamRegularSeasonStats["shotsAllowedRanking"] = type_block["splits"][0]["stat"].get("shotsAllowed")
				teamRegularSeasonStats["winScoreFirstRanking"] = type_block["splits"][0]["stat"].get("winScoreFirst")
				teamRegularSeasonStats["winOppScoreFirstRanking"] = type_block["splits"][0]["stat"].get("winOppScoreFirst")
				teamRegularSeasonStats["winLeadFirstPerRanking"] = type_block["splits"][0]["stat"].get("winLeadFirstPer")
				teamRegularSeasonStats["winLeadSecondPerRanking"] = type_block["splits"][0]["stat"].get("winLeadSecondPer")
				teamRegularSeasonStats["winOutshootOppRanking"] = type_block["splits"][0]["stat"].get("winOutshootOpp")
				teamRegularSeasonStats["winOutshotByOppRanking"] = type_block["splits"][0]["stat"].get("winOutshotByOpp")
				teamRegularSeasonStats["faceOffsTakenRanking"] = type_block["splits"][0]["stat"].get("faceOffsTaken")
				teamRegularSeasonStats["faceOffsWonRanking"] = type_block["splits"][0]["stat"].get("faceOffsWon")
				teamRegularSeasonStats["faceOffsLostRanking"] = type_block["splits"][0]["stat"].get("faceOffsLost")
				teamRegularSeasonStats["faceOffWinPercentageRanking"] = type_block["splits"][0]["stat"].get("faceOffWinPercentage")
				teamRegularSeasonStats["savePctRankRanking"] = type_block["splits"][0]["stat"].get("savePctRank")
				teamRegularSeasonStats["shootingPctRankRanking"] = type_block["splits"][0]["stat"].get("shootingPctRank")
		regularSeasonStats[team_id] = teamRegularSeasonStats
		print("got team {0}: '{1}'".format(team_id, teamRegularSeasonStats["team_name"]))
	return regularSeasonStats
	

def NHL_raw_regular_season_teams_stats_func(pg_conn_info)
	from contextlib import closing
	import json
	import psycopg2

	creds = json.loads(pg_conn_info)
	conn_info = {
		'host':     creds['host'],
		'port':     creds['port'],
		'user':     creds['login'],
		'password': creds['password'],
		'database': creds['schema']
	}
	
	data_for_insert = _parse()
	
	with closing(psycopg2.connect(**conn_info)) as conn:
		conn.autocommit = True
		with closing(conn.cursor()) as cur:
			data_for_insert_mogrified = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row).decode('utf-8') for row in data_for_insert)
			cur.execute("""
				INSERT INTO table_schema.table_name (key, value)
				VALUES %s
			""", data_for_insert_mogrified)
	
	return
	
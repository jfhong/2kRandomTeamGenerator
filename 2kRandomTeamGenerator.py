import random

teams = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
				"Chicago Bulls", "Cleveland Cavliers", "Dallas Mavericks", "Denver Nuggets",
				"Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
				"Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat",
				"Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
				"Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns",
				"Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Utah Jazz",
				"Toronto Raptors", "Washington Wizards"]

# how many teams you can choose from the list 'teams'
num_to_choose_from = 1

# randomizing teams and only choosing one from 'teams'
ran_team = random.sample(teams, num_to_choose_from)

# prints team that ure playing with
print(ran_team)
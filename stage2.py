from __future__ import print_function
import json
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint

configuration = tbaapiv3client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-TBA-Auth-Key'] = 'tJI4gHO50o8npMvOWjCGMdL3m8lGCiKT17fhaEupp04EQCB4kdRxy6WqR91qN4ng'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-TBA-Auth-Key'] = 'Bearer'

# Defining host is optional and default to https://www.thebluealliance.com/api/v3
configuration.host = "https://www.thebluealliance.com/api/v3"
# Create an instance of the API class
api_instance = tbaapiv3client.TBAApi(tbaapiv3client.ApiClient(configuration))
api_team = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))
api_event = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
if_modified_since = 'if_modified_since_example' # str | Value of the `Last-Modified` header in the most recently cached response by the client. (optional)

teamkey = 'frc1502'
eventkey = '2020isde1'

#	Create csv for event that includes team, opr, dpr, ccwm, qualfier_rank
#	


#	Create csv file to test the match
#	
#	Match number	- qualifying match number
#	Team
#	RobotPos: 
#		RedRobot1		- teamkey if score line, else 0
#		RedRobot2		- 
#		RedRobot3		-
#		BlueRobot1
#		BlueRobot2
#		BlueRobot3
#	RedAllianceScore
# 	BlueAllianceScore
#	end_game_robot
#	hab_docking_ranking_point
#	complete_rocket_ranking_point


#matchfile = open("matchfile.csv", "w")
teamfile = open("teamfile.csv", "a")

count=0

matches = api_event.get_event_matches(eventkey)
team_hang = {}

# Team hangs format:
# {
#	'frc1502': 3, # <-- number of hangs
#	'frc33': 2
# }
def add_team_hang(team_number):
	if team_number in team_hangs:
		team_hang[team_number] += 1
	else:
		team_hang[team_number] = 1

for match in matches:
	if (hasattr(match.score_breakdown, "red")):
		if (hasattr(match.score_breakdown["red"], "stage2Activated")):
			if (match.score_breakdown["red"].stage2Activated):
				print("Match:" + str(match.match_number) + " had red make stage 2.")
		if (hasattr(match.score_breakdown["blue"], "stage2Activated")):
			if (match.score_breakdown["blue"].stage2Activated):
				print("Match:" + str(match.match_number) + " had blue make stage 2.")
	else:
		print( "Match:" + str(match.match_number) + " had no alliances make stage 2.")
		
#	pprint(match.score_breakdown["red"]["controlPanelPoints"])
#		print(match.match_number)
#	if match.score_breakdown["blue"]["control_panel_points"] > 0:
#		print(match.match_number)
		
#	for i,team_key in enumerate(match.alliances.blue.team_keys, 0):
#		print(match.alliances.blue.team_keys[i])
#		if match['score_breakdown']['blue']['endgameRobot' + (i + 1)] == 'Hang':
#			add_team_hang(blue_team)
#	for (red_team, i) in enumerate(match['alliances']['red']['team_keys']):
#		if match['score_breakdown']['blue']['endgameRobot' + (i + 1)] == 'HabLevel3':
#			add_team_hang(red_team)

#pprint(team_hang)

'''
try:
    
	api_event_response_opr = api_event.get_event_op_rs(eventkey, if_modified_since=if_modified_since)
	OPR = api_event_response_opr.oprs
	pprint( OPR )
	
	for teams in OPR:
		teamfile.write( teams + ", " + str(OPR[teams]) + "\n")
		count=count+1
	
	print( str(count) + " lines added.")

except ApiException as e:
    print("Exception when calling TBAApi->get_status: %s\n" % e)
'''
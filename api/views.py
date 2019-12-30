from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Matches, Deliveries, Player, Location, Team
from collections import Counter

# Create your views here.
# TopFourTeamWins
# TossesWon
# MaxPlayerOfMatch
# MaxMatchesTeam
# MaxWinLocation
# PerBatDecision
# MaxWinLosePerLocation
# MaxWinTeamRuns

# to get top 4 teams in terms of win
class TopFourTeamWins(APIView):
	def get(self, request):
		year = request.GET.get('year', '')
		year_match_filter = Matches.objects.filter(season=year)
		matches_won_team = [data.winner.team_name for data in year_match_filter]
		matches_won_team_counter = Counter(matches_won_team)
		top_four_team = matches_won_team_counter.most_common()[0:4]
		response_dict = {}
		response_dict["season"] = year
		response_dict["top_four_teams"] = dict(top_four_team)
		return Response(response_dict)

# to get team that won most number of tosses
class TossesWon(APIView):
	def get(self, request):
		year = request.GET.get('year', '')
		year_match_filter = Matches.objects.filter(season=year)
		toss_won_teams = [data.toss_winner.team_name for data in year_match_filter]
		toss_won_teams_counter = Counter(toss_won_teams)
		# using list since we are going to take first element alone
		top_team_list = []
		top_team_list.append(toss_won_teams_counter.most_common()[0])
		response_dict = {}
		response_dict["season"] = year
		response_dict["team_won_tosses"] = dict(top_team_list)
		return Response(response_dict)

# to get player that won maximum player of the match
class MaxPlayerOfMatch(APIView):
	def get(self, request):
		year = request.GET.get('year', '')
		year_match_filter = Matches.objects.filter(season=year)
		player_won = [data.player_of_match.player_name for data in year_match_filter]
		player_won_counter = Counter(player_won)
		# using list since we are going to take first element alone
		top_player_list= []
		top_player_list.append(player_won_counter.most_common()[0])
		response_dict = {}
		response_dict["season"] = year
		response_dict["player_won_max_match"] = dict(top_player_list)
		return Response(response_dict)

# to get team that won max matches
class MaxMatchesTeam(APIView):
	def get(self, request):
		year = request.GET.get('year', '')
		year_match_filter = Matches.objects.filter(season=year)
		matches_won_team = [data.winner.team_name for data in year_match_filter]
		matches_won_team_counter = Counter(matches_won_team)
		top_team_list = [matches_won_team_counter.most_common()[0]]
		response_dict = {}
		response_dict["season"] = year
		response_dict["top_team"] = dict(top_team_list)
		return Response(response_dict)

# to get location that has most number of wins
class MaxWinLocation(APIView):
	def get(self, request):
		year = request.GET.get('year', '')
		year_match_filter = Matches.objects.filter(season=year)
		matches_won_team = [data.winner.team_name for data in year_match_filter]
		matches_won_team_counter = Counter(matches_won_team)
		# getting first record on top team
		team = matches_won_team_counter.most_common()[0][0]
		top_team = Matches.objects.filter(winner__team_name=team)
		top_team_venue = [data.venue.venue_name for data in top_team]

		top_team_venue_counter = Counter(top_team_venue)
		top_team_venue_list = [top_team_venue_counter.most_common()[0]]
		response_dict = {}
		response_dict["season"] = year
		response_dict["top_team_venue"] = dict(top_team_venue_list)
		return Response(response_dict)

# to get percentage of bat decision
class PerBatDecision(APIView):
	def get(self, request):
		year = request.GET.get('year', '')
		bat_decision_count = Matches.objects.filter(season=year, toss_decision="bat").count()
		total_match_count = Matches.objects.filter(season=year).count()
		bat_decision_percentage = round((bat_decision_count/total_match_count)*100)
		response_dict = {}
		response_dict["bat_decision_percentage"] = bat_decision_percentage
		return Response(response_dict)

# to get location hosted most number of matches and win and loss %
class MaxWinLosePerLocation(APIView):
	def get(self, request):
		year = request.GET.get('year', '')
		year_match_filter = Matches.objects.filter(season=year)
		most_match_location = [data.venue.venue_name for data in year_match_filter] 
		most_match_counter = Counter(most_match_location)
		top_location = most_match_counter.most_common()[0][0] 
		# to get team that won max match

		year_match_filter_count = Matches.objects.filter(season=year).count()
		matches_won_team = [data.winner.team_name for data in year_match_filter]
		matches_won_team_counter = Counter(matches_won_team)
		top_team = matches_won_team_counter.most_common()[0][0]

		# to get total matches on particular location
		total_matches_location_count = Matches.objects.filter(season=year, venue__venue_name=top_location).count()
		win_count_on_location = Matches.objects.filter(season=year, winner__team_name=top_team, venue__venue_name=top_location).count()
		loss_count = abs(total_matches_location_count - win_count_on_location)
		
		win_percentage = round((win_count_on_location/total_matches_location_count) * 100)	
		loss_percentage = round((loss_count/total_matches_location_count) * 100)

		response_dict = {}
		response_dict["season"] = year
		response_dict["max_match_location"] = top_location
		response_dict["win_percentage"] = win_percentage
		response_dict["loss_percentage"] = loss_percentage

		return Response(response_dict)

# to get the team with highest margin for runs for the season
class MaxWinTeamRuns(APIView):
	def get(self, request):
		year = request.GET.get('year', '')		
		year_match_filter = Matches.objects.filter(season=year)
		highest_run_margin = max([data.win_by_runs for data in year_match_filter])
		# getting team with highes run margin
		team = Matches.objects.filter(season=year, win_by_runs=highest_run_margin)

		if len(team) == 1:
			team_name = team[0].winner.team_name
		else:
			team_name = [data.winner.team_name for data in team]	

		response_dict = {}
		response_dict["season"] = year
		response_dict["max_win_team_by_run"] = team_name

		return Response(response_dict)	

# bonus apis
# to get team that win by highest number of wicket
class MaxWinTeamWickets(APIView):
	def get(self, request):
		year = request.GET.get('year', '')		
		year_match_filter = Matches.objects.filter(season=year)

		highest_wickets = max([data.win_by_wickets for data in year_match_filter])
		# getting team with highest wickets
		team = Matches.objects.filter(season=year, win_by_wickets=highest_wickets)
		
		if len(team) == 1:
			team_name = team[0].winner.team_name
		else:
			team_name = [data.winner.team_name for data in team]	

		response_dict = {}
		response_dict["season"] = year
		response_dict["max_win_team_by_wicket"] = team_name

		return Response(response_dict)

# to get how many times a team won match and toss
class TeamWonTossAndMatch(APIView):
	def get(self, request):
		year = request.GET.get('year', '')	
		team_name = request.GET.get('team_name', '')	
		year_match_filter = Matches.objects.filter(season=year)

		toss_won_count = Matches.objects.filter(season=year, toss_winner__team_name=team_name).count()
		match_won_count = Matches.objects.filter(season=year, winner__team_name=team_name).count()	

		response_dict = {}
		response_dict["season"] = year
		response_dict["team"] = team_name
		response_dict["toss_won_count"] = toss_won_count
		response_dict["match_won_count"] = match_won_count

		return Response(response_dict)
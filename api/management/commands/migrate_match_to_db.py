from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from api.models import Team, Player, Location, Matches
import csv
import datetime

path = settings.CSV_PATH + '/' + settings.MATCH_CSV_NAME

class Command(BaseCommand):
	help = 'Migrate match to db'

	def handle(self, *args, **kwargs):
		with open(path) as f: 
			reader = csv.reader(f) 
			next(reader) 
			for row in reader:
				season = row[1]
				city = row[2]
				y,m,d = tuple(row[3].split('-'))
				y = int(y)
				m = int(m)
				d = int(d)
				date = datetime.date(y,m,d)
				try:
					team1 = Team.objects.get(team_name=row[4])
				except Team.DoesNotExist:	
					team1 = Team.objects.create(team_name=row[4])
				try:	
					team2 = Team.objects.get(team_name=row[5])
				except Team.DoesNotExist:
					team2 = Team.objects.create(team_name=row[5])
				try:		
					toss_winner = Team.objects.get(team_name=row[6])
				except Team.DoesNotExist:
					toss_winner = Team.objects.create(team_name=row[6])
				toss_decision = row[7]
				result = row[8]
				dl_applied = row[9]
				try:
					winner = Team.objects.get(team_name=row[10])
				except Team.DoesNotExist:
					winner = Team.objects.create(team_name=row[10])
				win_by_runs = row[11]
				win_by_wickets = row[12]
				try:
					player_of_match = Player.objects.get(player_name=row[13])
				except Player.DoesNotExist:
					player_of_match = Player.objects.create(player_name=row[13])
				try:
					venue = Location.objects.get(venue_name=row[14])
				except Location.DoesNotExist:
					venue = Location.objects.create(venue_name=row[14])	
				umpire1 = row[15]
				umpire2 = row[16]
				umpire3 = row[17]

				match = Matches.objects.create(
				  	season = season,
				  	city = city,
				  	date = date,
				  	team1 = team1,
				  	team2 = team2,
				  	toss_winner = toss_winner,
				  	toss_decision = toss_decision,
				  	result = result,
				  	dl_applied = dl_applied,
				  	winner = winner,
				  	win_by_runs = win_by_runs,
				  	win_by_wickets = win_by_wickets,
				  	player_of_match = player_of_match,
				  	venue = venue,
				  	umpire1 = umpire1,
				  	umpire2 = umpire2,
				  	umpire3 = umpire3
				  	)

		print ("All records created")       
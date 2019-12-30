from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from api.models import Team, Player, Location, Matches, Deliveries
import csv
import datetime

path = settings.CSV_PATH + '/' + settings.DELIVERY_CSV_NAME

class Command(BaseCommand):
	help = 'Migrate deliveries to db'

	def handle(self, *args, **kwargs):
		with open(path) as f:
			reader = csv.reader(f)
			next(reader)
			for row in reader:
				match_id = Matches.objects.get(pk=int(row[0]))
				inning = row[1]
				try:
					batting_team = Team.objects.get(team_name=row[2])
				except Team.DoesNotExist:
					batting_team = Team.objects.create(team_name=row[2])
				try:
					bowling_team = Team.objects.get(team_name=row[3])
				except Team.DoesNotExist:
					bowling_team = Team.objects.create(team_name=row[3])
				over = row[4]
				ball = row[5]
				try:
					batsman = Player.objects.get(player_name=row[6])
				except Player.DoesNotExist:
					batsman = Player.objects.create(player_name=row[6])	
				try:
					non_striker = Player.objects.get(player_name=row[7])
				except Player.DoesNotExist:	
					non_striker = Player.objects.create(player_name=row[7])
				try:
					bowler = Player.objects.get(player_name=row[8])
				except Player.DoesNotExist:
					bowler = Player.objects.create(player_name=row[8])
				is_super_over = row[9]
				wide_runs = row[10]
				bye_runs = row[11]
				legbye_runs = row[12]
				noball_runs = row[13]
				penalty_runs = row[14]
				batsman_runs = row[15]
				extra_runs = row[16]
				total_runs = row[17]
				if len(row[18]) > 1:
					try:
						player_dismissed = Player.objects.get(player_name=row[18])
					except Player.DoesNotExist:
						player_dismissed = Player.objects.create(player_name=row[18])	
				else:
					player_dismissed = None	
				if len(row[19]) > 1:	
					dismissal_kind = row[19]
				else:
					dismissal_kind = None
				if len(row[20]) > 1:	
					try:	
						fielder = Player.objects.get(player_name=row[20])
					except Player.DoesNotExist:
						fielder = Player.objects.create(player_name=row[20])
				else:
					fielder = None
				deliveries = Deliveries.objects.create(
					match_id = match_id,
					inning = inning,
					batting_team = batting_team,
					bowling_team = bowling_team,
					over = over,
					ball = ball,
					batsman = batsman,
					non_striker = non_striker,
					bowler = bowler,
					is_super_over = is_super_over,
					wide_runs = wide_runs,
					bye_runs = bye_runs,
					legbye_runs = legbye_runs,
					noball_runs = noball_runs,
					penalty_runs = penalty_runs,
					batsman_runs = batsman_runs,
					extra_runs = extra_runs,
					total_runs = total_runs,
					player_dismissed = player_dismissed,
					dismissal_kind = dismissal_kind,
					fielder = fielder
					)


								

		
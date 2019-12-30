from django.db import models

# for the team
class Team(models.Model):
	team_name = models.CharField(max_length=200)

#for the player
class Player(models.Model):
	player_name = models.CharField(max_length=200)

#for the locations
class Location(models.Model):
	venue_name = models.CharField(max_length=200)   

class Matches(models.Model):
	season = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	date = models.DateField()
	team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="team1")
	team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="team2")
	toss_winner = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="tosswinner")
	toss_decision = models.CharField(max_length=200)
	result = models.CharField(max_length=200)
	dl_applied = models.IntegerField()
	winner = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="winner")
	win_by_runs = models.IntegerField()
	win_by_wickets = models.IntegerField()
	player_of_match = models.ForeignKey('Player', on_delete=models.CASCADE, related_name= "playerofmatch")
	venue = models.ForeignKey('Location', on_delete=models.CASCADE, related_name="venue")
	umpire1 = models.CharField(max_length=200)
	umpire2 = models.CharField(max_length=200)
	umpire3 = models.CharField(max_length=200)


class Deliveries(models.Model):
	match_id = models.ForeignKey('Matches', on_delete=models.CASCADE)
	inning = models.IntegerField()
	batting_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="battingteam")
	bowling_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="bowlingteam")
	over = models.IntegerField()
	ball = models.IntegerField()
	batsman = models.ForeignKey('Player', on_delete=models.CASCADE, related_name= "batsman")
	non_striker = models.ForeignKey('Player', on_delete=models.CASCADE, related_name= "nonstriker")
	bowler = models.ForeignKey('Player', on_delete=models.CASCADE)
	is_super_over = models.IntegerField()
	wide_runs = models.IntegerField()
	bye_runs = models.IntegerField()
	legbye_runs = models.IntegerField()
	noball_runs = models.IntegerField()
	penalty_runs = models.IntegerField()
	batsman_runs = models.IntegerField()
	extra_runs = models.IntegerField()
	total_runs = models.IntegerField()
	player_dismissed = models.ForeignKey('Player', on_delete=models.CASCADE, blank=True, null=True,related_name="playerdismissed")
	dismissal_kind = models.CharField(max_length=200, blank=True, null=True)
	fielder = models.ForeignKey('Player', on_delete=models.CASCADE, blank=True, null=True, related_name="fielder")
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from api.models import Team
import csv

path = settings.CSV_PATH + '/' + settings.MATCH_CSV_NAME

class Command(BaseCommand):
    help = 'Migrate team to db'

    def handle(self, *args, **kwargs):
    	with open(path) as f: 
    		reader = csv.reader(f) 
    		next(reader) 
		    for row in reader: 
		        try: 
		            team = Team.objects.get(team_name=row[4]) 
		        except Team.DoesNotExist: 
		            team = Team.objects.create(team_name=row[4]) 



from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from api.models import Player
import csv

path = settings.CSV_PATH + '/' + settings.MATCH_CSV_NAME

class Command(BaseCommand):
    help = 'Migrate player to db'

    def handle(self, *args, **kwargs):
    	with open(path) as f: 
    		reader = csv.reader(f) 
    		next(reader) 
		    for row in reader: 
		        try: 
		            player = Player.objects.get(player_name=row[13]) 
		        except Player.DoesNotExist: 
		            player = Player.objects.create(player_name=row[13]) 



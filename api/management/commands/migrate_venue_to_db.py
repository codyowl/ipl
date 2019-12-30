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
					location = Location.objects.get(venue_name=row[14]) 
				except Location.DoesNotExist: 
					location = Location.objects.create(venue_name=row[14])   



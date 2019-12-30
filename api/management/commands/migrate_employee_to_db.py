from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from api.models import Player
import csv

csv_path = settings.CSV_PATH + '/' + settings.MATCH_CSV_NAME


class Command(BaseCommand):
    help = 'Migrate employee to db'

    def handle(self, *args, **kwargs):
    	pass
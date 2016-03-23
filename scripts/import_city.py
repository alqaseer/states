#!/usr/bin/env python
import csv
import os
import sys
sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from main.models import State, City

import django
django.setup()
City.objects.all().delete()

dir_path = os.path.dirname(os.path.abspath(__file__))

city_csv = os.path.join(dir_path, 'zip_codes_states.csv')

csv_file = open(city_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	mystate, created = State.objects.get_or_create(abbreviation=row['state'])

	new_city, created = City.objects.get_or_create(name=row['city'])

	new_city.zip_code = row['zip_code']
	new_city.latitude = row['latitude']
	new_city.longitude = row['longitude']
	new_city.name = row['city']
	
	new_city.state = mystate
	new_city.county = row['county']
	new_city.save()
	
	print new_city

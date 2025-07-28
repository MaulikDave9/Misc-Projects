#!/usr/bin/env python3

import csv

#input file path 
file_path = '../Data/2018-11-24-events.csv'

# dictionary to hold event counts, key = sessionId, artist and value = event_count
events = {}

with open(file_path, mode = 'r', newline='') as file:
	csv_reader = csv.DictReader(file)
	
	header = next(csv_reader)
	#print(f"Header: {header}")

	for row in csv_reader:
		session_id = row['sessionId']
		artist     = row['artist']
		
		#skip blank artists for this one!
		if artist == '':
			continue
		#print(f"Row: {row}")	
		
		key = (session_id, artist)
		events[key] = events.get(key, 0) + 1
		
		
	#print(events)
	
	#Find and keep only entries with at least 2 events
	events_filtered = {key: value for key, value in events.items() if value >= 2}
	
	print(events_filtered)
		


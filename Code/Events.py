#!/usr/bin/env python3

import pandas as pd

#input file path 
file_path = '../Data/2018-11-24-events.csv'

#Read and store the data in data frame
df = pd.read_csv(file_path)

#Print the column values to test!
#print(df['sessionId'].tolist())

# Find the unique events - assuming 'page' refers to event for this music streaming user activity
#unique_events = df['page'].unique()
#print(unique_events)
#['NextSong' 'Home' 'Help' 'Login' 'Logout' 'About' 'Settings' 'Downgrade']

#Concern: Many rows have no value for artists, ignoring that for now!

#Goal: Produce list of every sessionId features two or more events for the same artist
#Usig groupby sessionId and Artist to find that list and filter by at least 2 events 

grouped   = df.groupby(['sessionId', 'artist'])['page'].count().reset_index(name='n_events')
grouped_f = grouped[grouped['n_events'] >= 2 ]

# test for specific sessionId
print(grouped_f[grouped_f['sessionId'] == 849])

print(grouped_f[['sessionId', 'artist', 'n_events']])

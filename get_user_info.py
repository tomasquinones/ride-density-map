#!
## Outputs three json files for any given USER_ID on ridewithgps.com
## user_info, trips, gears
## These three files are then used by the graphing code.

import json, requests, sys
import api_credentials as cd

# Ride with GPS Info
BASE_URL = 'https://ridewithgps.com'

print(f'Contacting {BASE_URL}...')

# First: Get the user info based on USER_ID
get_user_info = requests.get(f'{BASE_URL}/users/current.json?auth_token={cd.AUTH_TOKEN}&apikey={cd.API_KEY}&version=2')

user_info = get_user_info.json()


with open('user_info.json', 'w') as user_file:
    json.dump(user_info, user_file)
print(f'Downloaded user info from {cd.USER_ID}')

totalRides = user_info['user']['trips_included_in_totals_count']



# Gets full list of trips
print(f'Getting full list of trips for {cd.USER_ID}')
count = 1
offset = 0
triplist = []

while offset < totalRides: 
    get_trips = requests.get(f'{BASE_URL}/users/{cd.USER_ID}/trips.json?auth_token={cd.AUTH_TOKEN}&apikey={cd.API_KEY}&version=2')
    user_trips = get_trips.json()
    for t in user_trips['results']:
        print(t['id'])
        triplist.append(t['id'])
    offset += 20



with open('user_trips.json', 'w') as trips_file:
    json.dump(user_trips, trips_file)

print(f'Downloaded {len(triplist)} trips from {cd.USER_ID}')



# Gets full list of user's gear.
get_gears = requests.get(f'{BASE_URL}/users/{cd.USER_ID}/gears.json?auth_token={cd.AUTH_TOKEN}&apikey={cd.API_KEY}&version=2')
user_gears = get_gears.json()

with open('user_gears.json', 'w') as gears_file:
    json.dump(user_gears, gears_file)

print(f'Downloaded gear info from {cd.USER_ID}')




print('All downloads complete')


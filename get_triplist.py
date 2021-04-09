import json, requests, sys, os, re
import api_credentials as cd

# Ride with GPS Info
BASE_URL = 'https://ridewithgps.com'


# Get the info from ridewithgps
print(f'Contacting {BASE_URL}...')

get_user_info = requests.get(f'{BASE_URL}/users/current.json?auth_token={cd.AUTH_TOKEN}&apikey={cd.API_KEY}&version=2')
user_info = get_user_info.json()

with open('user_info.json', 'w') as user_file:
    json.dump(user_info, user_file)


totalRides = user_info['user']['trips_included_in_totals_count']


# Gets full list of trips
print(f'Getting list of trips for {cd.USER_ID}')

count = 1
offset=0
triplist = []

while offset < totalRides:
    get_trips = requests.get(f'{BASE_URL}/users/{cd.USER_ID}/trips.json?auth_token={cd.AUTH_TOKEN}&apikey={cd.API_KEY}&version=2&offset={offset}&limit=20')
    trips = get_trips.json()
    for t in trips['results']:
        print(t['id'])
        triplist.append(t['id'])
    offset += 20

downloaded = os.listdir('trips')
print(downloaded)
# TODO use os.makedirs() to make the trips folder


for trip in triplist:
    print(f'Downloading {count} of {totalRides}')
    get_trip = requests.get(f'{BASE_URL}/trips/{trip}.json?auth_token={cd.AUTH_TOKEN}&apikey={cd.API_KEY}&version=2')
    trip_json = get_trip.json()

    with open('trips/' + str(trip) + '.json', 'w') as trips_file:
        json.dump(trip_json, trips_file)
    count += 1

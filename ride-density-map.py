import json, os
import plotly.express as px

px.set_mapbox_access_token(open(".mapbox_token").read())


howManyTrips = 0
tripLats = []
tripLongs = []
tripElevations = []
tripData = []
totalpoints = 0
tripList = []

# read contents of /trips folder, place all trip numbers into a list.
for item in os.listdir('trips'):
    if not item.startswith('.'):
        tripList.append(item)
print(tripList)


# iterate through trip list to open, get all the trackpoints,
for trip in tripList:
    print(f'Opening {trip}')

    with open('trips/'+ trip, "r") as read_file: data = json.load(read_file)
    for t in data['trip']['track_points'][::6]:  # Currently getting every sixth track point.
        try:
            if 'y' in t and 'x' in t and 'e' in t:
                tripLat = t['y']
                tripLon = t['x']
                tripEle = 250  #t['e']
            else:
                continue
        except TypeError:
            print('point has bad data')
        else:
            tripLats.append(tripLat)
            tripLongs.append(tripLon)
            tripElevations.append(tripEle)
            totalpoints +=1
    print(f'Processed {trip}')
    read_file.close()

print(f'Processed {len(tripLats)} Bike Rides')
print('Lats Points Total' , len(tripLats))
print('Longs Points Total', len(tripLongs))
print('Elevations Points Total', len(tripElevations))

# TODO: Average the first lat/longs to get a 'centered' center for the map view?
#firstLat = data['first_lat']
#firstLon = data['first_lng']

# Defining the dataframe source to be used by the map.
df = {
    'lats': tripLats,
    'longs': tripLongs,
    'elevations': tripElevations
    }


# Defining the heatmap style and parameters
# Documentation: https://plotly.com/python/reference/#densitymapbox

fig = px.density_mapbox(df,
                        lat='lats',
                        lon='longs',
                        z='elevations',
                        radius=2,
                        center=dict(
                                    lat=45.5567,
                                    lon=-122.6050),
                        zoom=12,
                        mapbox_style='carto-darkmatter', # mapbox_style="stamen-terrain", # mapbox_style="stamen-terrain",
                        color_continuous_scale=px.colors.sequential.Plotly3,
                        title=f'{len(tripList)} Rides with {len(tripLats)} Data Points '

                        )

# Show it!
fig.show()

'''
fig = px.scatter_mapbox(df,
                        lat='lats',
                        lon='longs',
                        # z='elevations',
                        # radius=2,
                        center=dict(
                                    lat=45.5567,
                                    lon=-122.6050),
                        zoom=12,
                        mapbox_style='carto-darkmatter', # mapbox_style="stamen-terrain", # mapbox_style="stamen-terrain",
                        color_continuous_scale=px.colors.sequential.Plotly3,
                        opacity=0.5,
                        title=f'{len(tripList)} Rides with {len(tripLats)} Data Points '

                        )

# Show it!
fig.show()
'''
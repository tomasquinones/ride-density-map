# ride-density-map
Using Python and Plotly Express to show all my ride data from ridewithgps.com
Uses https://plotly.com/python/mapbox-density-heatmaps/

Requirements:
+ Python 3.5
+ Plotly Express -- *pip install ploty*
+ Requests module -- *pip install requests*

Running it!
1. Edit 'api_credentials.py' with your API Key, user, password, whatever
2. You'll need your own Mapbox Token and put it into .mapbox_token file to use the dark map style. 
3. Run `python3 get user_info.py` -- Creates some JSON files with your trip list and more. 
4. Run `python3 get_triplist.py` -- This downloads all your trip data, this could take a while. 
5. Run `python3 ride-density-map.py` -- This will process all your JSON files in the 'trips' folder then open in your default browser. This could take a minute depending on how much data you have and your computer. 


Notes:
+ You will need your own API key from Ride with GPS. 

+ Currently the map auto-centers on Portland.

+ Every fifth data point is placed on the map, otherwise performance takes a huge hit or crashes the browser. 


Plans:
+ Downloading data into a SQLite database rather than having hundreds or even thousands of JSON files to be process.
+ Using Pandas for the managing the data to be rendered. Supposedly this will give another performance boost. 
+ Selector for map type
+ Selector for color scheme
+ Selector for date range

![](https://s3.amazonaws.com/rwgps/screenshots/2021040721-55-10.png)

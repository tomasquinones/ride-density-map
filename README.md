# ride-density-map
Using Python and Plotly Express to show all my ride data from ridewithgps.com

Requirements:
+ Python 3.5
+ Plotly Express
++ pip install ploty

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

import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyDvBkR_3IQDGHxd-iBNP-obx9ncD8PMdaM')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

places = googlemaps.places

location = (37.419793, -121.900285)
radius = 2000

restaurants = places.places(gmaps, "restaurant", location=location, radius=radius, open_now=True)

import pprint
pprint.pprint(restaurants)
#print(directions_result)


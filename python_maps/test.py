import googlemaps
from datetime import datetime
import pprint
from gmplot import gmplot



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

restaurants = places.places(gmaps, "restaurant", location=location, radius=radius, open_now=True)['results']

#pprint.pprint(restaurants)
#dict_keys(['html_attributions', 'results', 'status', 'next_page_token'])
#dict_keys(['id', 'opening_hours', 'name', 'types', 'reference', 'photos', 'place_id', 'price_level', 'geometry', 'rating', 'formatted_address', 'plus_code', 'icon'])
#'geometry': {'location': {'lat': 37.4340294, 'lng': -121.8932378},
#'name': 'IHOP',
#              'opening_hours': {'open_now': True},

info_list = [[restaurant['geometry']['location'], restaurant['name']] for restaurant in restaurants if restaurant['opening_hours']['open_now']]
pprint.pprint(info_list)

#for restaurant in restaurants:
#    print(restaurant['geometry'])

#print(directions_result)

map_draw = gmplot.GoogleMapPlotter(location[0], location[1], 13)
for info in info_list:
    map_draw.marker(info[0]['lat'], info[0]['lng'], 'cornflowerblue')

# Draw
map_draw.draw("my_map.html")

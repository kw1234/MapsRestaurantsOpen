from flask import Flask, render_template, request
import googlemaps
from datetime import datetime
import pprint
from gmplot import gmplot
import constants

app = Flask(__name__)
gmaps = googlemaps.Client(key='AIzaSyDvBkR_3IQDGHxd-iBNP-obx9ncD8PMdaM')
places = googlemaps.places
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#print(geocode_result)

@app.route('/')
def load_map():
    return render_template('my_map.html')

@app.route('/latlon/<subpath>', methods = ['GET', 'POST'])
def lat_lon(subpath):
    if request.method == 'POST':
        lat = float(str(subpath).split("^")[0])
        lon = float(str(subpath).split("^")[1])

        constants.PREV_LAT = lat
        constants.PREV_LON = lon

        draw_map((lat, lon))
        #load_map()
        return subpath
    return "la_lon get"

@app.route('/address/<subpath>', methods = ['GET', 'POST'])
def address(subpath):
    if request.method == 'POST':
        print("address")
        geocode_result = gmaps.geocode(subpath)
        lat = float(geocode_result[0]['geometry']['location']['lat'])
        lon = float(geocode_result[0]['geometry']['location']['lng'])

        constants.PREV_LAT = lat
        constants.PREV_LON = lon

        draw_map((lat, lon))
        return subpath
    return "address get"

@app.route('/latlon/radius/<value>', methods = ['GET', 'POST'])
def radius(value):
    if request.method == 'POST':
        print("radius")
        print(constants.PREV_LAT)
        print(constants.PREV_LON)
        print(value)
        draw_map((constants.PREV_LAT, constants.PREV_LON), float(value))
        return value
    return "radius get"

def draw_map(location, radius=2000):
    restaurants = places.places(gmaps, "restaurant", location=location, radius=radius, open_now=True)['results']
    gusa = places.places(gmaps, "restaurant", location=location, radius=radius, open_now=True)
    print(gusa['next_page_token'])
   
    print(len(restaurants))
    info_list = []
    for restaurant in restaurants:
        location = restaurant['geometry']['location']
        name = restaurant['name']
        if restaurant['opening_hours']['open_now']:
            info_list.append({"name": name, "location": location})

    map_draw = gmplot.GoogleMapPlotter(location['lat'], location['lng'], 13)
    for info in info_list:
        map_draw.marker(info['location']['lat'], info['location']['lng'], 'cornflowerblue')
        
    map_draw.draw("templates/my_map.html")
    map_draw.draw("my_map.html")


if __name__ == '__main__':
    app.run(debug = True)

from flask import Flask, render_template, request
import googlemaps
from datetime import datetime
import pprint
from gmplot import gmplot

app = Flask(__name__)
gmaps = googlemaps.Client(key='AIzaSyDvBkR_3IQDGHxd-iBNP-obx9ncD8PMdaM')
places = googlemaps.places

@app.route('/')
def student():
    return render_template('my_map.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form['location_long_lat']
        print(result)
        draw_map(result)
        return render_template('my_map.html')
    print("aaa")
    return "get"

def draw_map(location):
    print("aaaa")
    radius = 2000
    restaurants = places.places(gmaps, "restaurant", location=location, radius=radius, open_now=True)['results']
    info_list = [[restaurant['geometry']['location'], restaurant['name']] for restaurant in restaurants if restaurant['opening_hours']['open_now']]
    map_draw = gmplot.GoogleMapPlotter(location[0], location[1], 13)
    for info in info_list:
        map_draw.marker(info[0]['lat'], info[0]['lng'], 'cornflowerblue')
        
    map_draw.draw("templates/my_map.html")


if __name__ == '__main__':
    app.run(debug = True)

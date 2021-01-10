import folium
import pandas

import df1

data= df1.maxD

lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
hnum=list(data["ELEV"])

def color_producer(hsnumber):
    if hsnumber < 1000:
        return 'green'
    elif 1000 <= hsnumber < 1500:
        return 'yellow'
    elif 1500 <= hsnumber < 3000:
        return 'blue'
    elif 3000<= hsnumber < 4000:
        return 'pink'
    elif 4000 <= hsnumber < 6500:
        return 'orange'
    else:
        return 'red'


map=folium.Map(location=[43.59503160541172, -116.32247210307258],zoom_start=25)

fg=folium.FeatureGroup(name="my map")


for lt,ln,nm,hn in zip(lat,lon,name,hnum):

    fg.add_child(folium.Marker(location=[lt,ln], popup=hn,icon = folium.Icon(color = color_producer(hn))))


fg.add_child(folium.GeoJson(data=(open('allZones.json','r',encoding='utf-8-sig').read())))

map.add_child(fg)

map.save("map4.html")
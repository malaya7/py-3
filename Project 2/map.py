import folium, pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

def makeColor(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >= 1000 and elevation < 3000:
        return 'orange'
    else:
        return "red"


map = folium.Map(location=[33.6649159,-117.8503908],zoom_start=6, tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")

for x, y, z in zip(lat,lon, elv):
    fgv.add_child(folium.CircleMarker(location=[x,y], popup=str(z) + "Meters", radius=6, color=makeColor(z),fill_opacity=0.7,fill=True))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")

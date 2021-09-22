import pandas as pd
import folium

data= pd.read_csv('Volcanoes_USA.txt')

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data['ELEV'])
name=list(data['NAME'])

def color_producer (elevation) :
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red '

map=folium.Map(location=[38.58,-99.09],zoom_start=6, tiles='OpenStreetMap')

fgv=folium.FeatureGroup(name="VOLCANOES")


for lt,ln,el,n in zip(lat,lon,elev,name):
    fgv.add_child(folium.CircleMarker(location= [lt, ln], radius=6, popup=n+' '+str(el)+' m', fill_color=color_producer(el),
                                     color='grey',fill=True, fill_opacity=0.7))

fgp=folium.FeatureGroup(name="POPULATION")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                            else 'orange' if 1000000<=x['properties']['POP2005']<20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map1.html')

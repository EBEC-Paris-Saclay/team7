import requests
import geopy
import json
from geopy.geocoders import Nominatim

geocoder=Nominatim(user_agent='http')

def allnodesrue(adresse): 
    location = geocoder.geocode(adresse,addressdetails=True) #donne les coordonnées de l'adresse
    id=location.raw["osm_id"]
    coordinates=[]
    response = requests.get("http://overpass-api.de/api/interpreter?data=[out:json];way("+str(id)+");(._;%3E;);out;")
    nodesrue=response.json()
    for i in nodesrue["elements"]:
        if i["type"]=="node":
            coordinates.append((i["lat"],i["lon"]))
    return coordinates


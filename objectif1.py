import requests
import geopy
import json
from geopy.geocoders import Nominatim

geocoder=Nominatim(user_agent='http')

from  ClassificationNoeuds import  classnoeud
from allnodesrue import allnodesrue
from ebec import troncon



adresse = "Rue Kleber Courbevoie"
L=allnodesrue(adresse)
L=classnoeud(L)

lat,lng=48.89394122,2.247959188
indice=0
req0="http://api.geonames.org/findNearestIntersectionOSMJSON?formatted=true"
req=req0+"&lat="+str(lat)+"&lng="+str(lng)+"&username=yirhboula&style=full"
response = requests.get(req)
rue1,rue2=response.json()['intersection']['street2'],response.json()['intersection']['street1']
lat0=response.json()['intersection']['lat']
for i in range(len(L)) :
    if L[i][0]>lat:
        indice=i
        break
        
if float(lat0)<=float(lat):
    L1=L[:indice]
else:
    L1=L[indice:]
for node in L1:
    req0="http://api.geonames.org/findNearestIntersectionOSMJSON?formatted=true"
    lat1,lng1=node[0],node[1]
    req=req0+"&lat="+str(lat1)+"&lng="+str(lng1)+"&username=yirhboula&style=full"
    response = requests.get(req)
    street1,street2=response.json()['intersection']['street2'],response.json()['intersection']['street1']
    if (street1,street2)!=(rue1,rue2):
        print(rue1,rue2,street1,street2)
        break



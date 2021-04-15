import requests
import geopy
import json
from geopy.geocoders import Nominatim

geocoder=Nominatim(user_agent='http')

from  ClassificationNoeuds import  classnoeud
from allnodesrue import allnodesrue
from ebec import troncon



adresse = "Place Victor Hugo Courbevoie"
L=allnodesrue(adresse)
L=classnoeud(L)
troncon(L,(48.89227652, 2.253773690))




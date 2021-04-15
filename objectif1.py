import requests
import geopy
import json
from geopy.geocoders import Nominatim

geocoder=Nominatim(user_agent='http')

from  ClassificationNoeuds import  classnoeud
from allnodesrue import allnodesrue
from ebec import troncon
from nomdelarue import nom,adresse_complete


coord=48.89394122, 2.247959188
L=allnodesrue(adresse_complete(nom(coord)))
L=classnoeud(L)
troncon(L,(48.89394122, 2.247959188 ))




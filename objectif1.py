import requests
import geopy
import json
from geopy.geocoders import Nominatim

geocoder=Nominatim(user_agent='http')

from  ClassificationNoeuds import  classnoeud
from allnodesrue import allnodesrue

adresse = "5 rue Joliot-Curie Gif-sur-Yvette France"
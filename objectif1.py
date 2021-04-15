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
adresse='Avenue Gambetta Courbevoie'
L=allnodesrue(adresse)
#L=allnodesrue(adresse_comlpete(nom(coord)) cette ligne permet de generer directement l'adresse complete et par conséquent de ne pas avoir a la taper nous même.
L=classnoeud(L)
troncon(L,(coord))




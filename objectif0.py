
import geopy
from geopy.geocoders import Nominatim
def nom(coord): 
  adr=geocoder.reverse(coord)
  informations=adr.raw['address']
  adresse=[]
  for element in ['house_number','road','town','city']:
      try:
        adresse.append(informations[element])
      except:
        pass  
  return adresse


geocoder=Nominatim(user_agent='http')
adresse = "109 avenue du général leclerc 75014"  
location = geocoder.geocode(adresse,addressdetails=True) #donne les coordonnées de l'adresse
coord=[location.latitude,location.longitude]


print(nom(coord))
print(coord)
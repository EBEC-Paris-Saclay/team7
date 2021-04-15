
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



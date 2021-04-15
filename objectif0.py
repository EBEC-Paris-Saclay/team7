
import geopy
from geopy.geocoders import Nominatim
def nom(coord): 
  adr=geocoder.reverse(coord)
  total_info=adr.raw['address']
  necessary_info=[]
  for i in ['house_number','road','town','city']:
      try:
        necessary_info.append(total_info[i])
      except:
        pass  
  return necessary_info



import geopy
from geopy.geocoders import Nominatim
geocoders=Nominatim(user_agent='http')
def nom(coord): 
  adr=geocoders.reverse(coord)
  total_info=adr.raw['address']
  necessary_info=[]
  for i in ['house_number','road','town','city']:
      try:
        necessary_info.append(total_info[i])
      except:
        pass  
  return necessary_info

coord=(48.89525193,2.247122897)


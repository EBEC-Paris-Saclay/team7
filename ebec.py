import requests
lat,lng=48.89525193, 2.247122897
req0="http://api.geonames.org/findNearestIntersectionOSMJSON?formatted=true"
req=req0+"&lat="+str(lat)+"&lng="+str(lng)+"&username=yirhboula&style=full"
response = requests.get(req)
print(response)

import json

rue1,rue2=response.json()['intersection']['street2'],response.json()['intersection']['street1']

street=[]

for node in street:
    lat,lng=node.lat, node.lon

    req0="http://api.geonames.org/findNearestIntersectionOSMJSON?formatted=true"
    req=req0+"&lat="+str(lat)+"&lng="+str(lng)+"&username=yirhboula&style=full"
    response = requests.get(req)

    street1,street2=response.json()['intersection']['street2'],response.json()['intersection']['street1']
    if (street1,street2)!=(rue1,rue2):
        break

print((street1,street2,rue1,rue2))


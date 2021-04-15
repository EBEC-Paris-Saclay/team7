import requests
lat,lng=48.89525193, 2.247122897
coord=lat,lng
def troncon(L,coord):
    lat,lng=coord
    indice=0
    req0="http://api.geonames.org/findNearestIntersectionOSMJSON?formatted=true"
    req=req0+"&lat="+str(lat)+"&lng="+str(lng)+"&username=yirhboula&style=full"
    response = requests.get(req)
    rue1,rue2=response.json()['intersection']['street2'],response.json()['intersection']['street1']
    lat0=response.json()['intersection']['lat']
    for i in range(len(L)) :
        while L[i][0]>lat and i<len(L):
            i=+1
    indice=i
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



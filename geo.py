from pymongo import MongoClient
import json
import requests


key="dm9aZW5HanRPQ1E3Y0xZSmNrNmRBUHFlQzM4M2toR3g6V3dCSTBsV2pUbTIxdnpoWA=="
Autho="Basic dm9aZW5HanRPQ1E3Y0xZSmNrNmRBUHFlQzM4M2toR3g6V3dCSTBsV2pUbTIxdnpoWA=="
Content="application/x-www-form-urlencoded"

def cordinates(startadds):
    client = MongoClient('mongodb://bidhuri:jaisiaram1@ds113445.mlab.com:13445/pbcall')
    db = client.get_default_database()

    op=db.delivery.find({})
    lg=list([])
    headers = {'content-type': 'json'}
    for q in op:
        r = requests.post('https://api.pitneybowes.com/oauth/token',headers={"Authorization":Autho,"Content-Type":Content},data={"grant_type":"client_credentials"})
        r=r.json()
        access=r['access_token']
    
        add=str(q['address'])
        country=str(q['country'])
        parameters = {"country":country,"mainAddress":add}
        access="Bearer "+ access
        response = requests.get(url='https://api.pitneybowes.com/location-intelligence/geocode-service/v1/transient/premium/geocode',params=parameters ,headers={"Authorization":access,"Content-Type":"application/json"})
        res=response.json()
        temp = res['formattedStreetAddress']
        temp1 = res['formattedLocationAddress']
        endp = temp +", "+temp1
        #st,st1 = str(start[0]),str(start[1])
        r = requests.post('https://api.pitneybowes.com/oauth/token',headers={"Authorization":Autho,"Content-Type":Content},data={"grant_type":"client_credentials"})
        r=r.json()
        access=r['access_token']
        access="Bearer "+ access
        
        parameters={'startPoint':start,'endPoint':endp,'db':"driving"}
        res1=requests.get(url='https://api.pitneybowes.com/location-intelligence/georoute/v1/route/byaddress',params=parameters,headers={"Authorization":access,"Content-Type":"application/json"})
        print(res1.json())
        if res1['distance']<7000 or res1['time']<25 :
           lg.append(q['Phone']) 
    return lg
    


if __name__=="__main__":
    cordinates()
    
    
    
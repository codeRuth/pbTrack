from pymongo  import MongoClient
import json
import requests
from requests.auth import HTTPDigestAuth
key="voZenGjtOCQ7cLYJck6dAPqeC383khGx"
secret="WwBI0lWjTm21vzhX"

def cordinates():
    client = MongoClient('mongodb://bidhuri:jaisiaram1@ds113445.mlab.com:13445/pbcall')
    db = client.get_default_database()
    r = requests.get('https://api.pitneybowes.com/oauth')
    r.auth = (key, secret)
    
    
    op=db.delivery.find({})
    lg=[]
    headers = {'content-type': 'json'}
    for q in op:
        
        add=q['address']
        country=q['country']
        #print (add+country)
        parameters = {"country": country, "mainAddress": add}
        
        response = requests.request('POST',url='https://api.pitneybowes.com/location-intelligence/geocode-service/v1/transient/premium/geocode',data=parameters,auth=(key,secret))
        print (response)
        #res1=url_route
        
        #if res1['distance']<7000 or res1['time']<25 :
         #  lg.append(q['Phone']) 
    #return lg
    


if __name__=="__main__":
    cordinates()
    
    
    
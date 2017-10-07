from pymongo  import MongoClient
import json

url='https://api.pitneybowes.com/location-intelligence/geocode-service/v1/transient/premium/geocode'

def cordinates(del_add):
    client = MongoClient('mongodb://bidhuri:jaisiaram1@ds113445.mlab.com:13445/pbcall')
    db = client.get_default_database()
    
    op=db.delivery.find({})
    for q in op:
        
        add=q['address']
        country=q['country']
        #print (add+country)
        res=url
        res1=url_route
        lg=[]
        if res1['distance']<7000 or res1['time']<25 :
           lg.append(q['Phone']) 
        return lg
    


if __name__=="__main__":
    cordinates()
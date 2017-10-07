from pymongo import MongoClient
import json
import make_call
import datetime

# def input_val(y ,n ,t ):
#   yes = y
#  no = n
# time = t

# DATA = [
#    {
#        'cust_id': '',
#        'name': '',
#        'address': '',
#        'ord_id': '',
#        'del_time':'',
#        'social':'',
#    } ,
#    {
#        'cust_id': '',
#        'name': '',
#        'address': '',
#        'ord_id': '',
#        'del-time':'',
#        'social':'',
#    } ,
#    {
#        'cust_id': '',
#        'name': '',
#        'address': '',
#        'ord_id': '',
#        'del_time':'',
#        'social':'',
#    }
# ]

# client = MongoClient('mongodb://bidhuri:jaisiaram1@ds113445.mlab.com:13445/pbcall')
# db = client.get_database()


def update(args):
    # del=db.delivery
    # print (db.collection_names())
    # db.delivery.createIndex( { "cust_id":  }, { unique: true } )
    # db.delivery.insert_many(DATA)

    client = MongoClient('mongodb://bidhuri:jaisiaram1@ds113445.mlab.com:13445/pbcall')
    db = client.get_database()

    inp = json.loads(args)
    # print (inp)
    yes = inp['yes']
    no = inp['no']
    del_time = inp['del_time']
    pno = inp['pno']
    # print (pno)
    if yes == 'True':
        pass
    elif no == 'True' and yes == 'False':
        # delv = db['delivery']
        query = {'Phone': pno}
        # f=db.delivery.find({"name":"Aravind S"})
        # for doc in f:
        #    print(doc)
        db.delivery.update(query, {'$set': {'del_time': del_time}})
    client.close()


def get_users():
    client = MongoClient('mongodb://bidhuri:jaisiaram1@ds113445.mlab.com:13445/pbcall')
    db = client.get_database()

    _ = list()
    for doc in db.delivery.find({}, {"_id": 0, "name": 1, "phone": 1}):
        _.append(doc)
    return _

if __name__ == '__main__':
    for x in get_users():
        print type(str(x['phone']))
    get_users()
    #print get_users()[0]['phone']

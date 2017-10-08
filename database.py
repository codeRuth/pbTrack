from pymongo import MongoClient
import json
import config


def update(args):
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()

    inp = json.loads(args)

    yes = inp['yes']
    no = inp['no']
    del_time = inp['del_time']
    pno = inp['pno']
    if yes == 'True':
        pass
    elif no == 'True' and yes == 'False':
        query = {'Phone': pno}
        db.delivery.update(query, {'$set': {'del_time': del_time}})
    client.close()


def get_users():
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()

    _ = list()
    for doc in db.delivery.find({}, {"_id": 0, "name": 1, "phone": 1}):
        _.append(doc)
    return _


def get_data():
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()

    _ = list()
    for doc in db.delivery.find({}, {"_id": 0}):
        _.append(doc)
    return _

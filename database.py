from pymongo import MongoClient
import json
import config


def update(args):
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()

    inp = json.loads(args)
    yes, no, del_time, pno = inp['yes'], inp['no'], inp['del_time'], inp['pno']

    if yes == 'true':
        pass
    elif no == 'true' and yes == 'false':
        query = {'phone': pno}
        db.delivery.update(query, {'$set': {'del_time': del_time, 'availability': 'no'}})
    client.close()


def get_users():
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()

    _ = list()
    for doc in db.delivery.find({}, {"_id": 0, "name": 1, "phone": 1}):
        _.append(doc)
    client.close()
    return _


def get_data():
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()

    _ = list()
    for doc in db.delivery.find({}, {"_id": 0}):
        _.append(doc)
    client.close()
    return _

from pymongo import MongoClient
import json, base64
import config
import requests


def coordinates(start):
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()

    access = generate_access_token()
    customer_db = db.delivery.find({})

    delivery = list([])

    for _ in customer_db:
        add = str(_['address'])
        country = str(_['country'])
        parameters = {"country": country, "mainAddress": add}
        response = requests.get(
            url=config.GEOCODE_API_URL,
            params=parameters, headers={"Authorization": "Bearer " + access, "Content-Type": "application/json"})
        res = response.json()

        end = res['candidates'][0]['formattedStreetAddress'] + ", " + res['candidates'][0]['formattedLocationAddress']

        parameters = {'startAddress': start, 'endAddress': end, 'country': country, 'db': "driving"}
        distance_time = requests.get(url=config.ROUTE_API_URL,
                                     params=parameters,
                                     headers={"Authorization": "Bearer " + access, "Content-Type": "application/json"})
        distance_time = distance_time.json()

        if distance_time['distance'] < 7000 or distance_time['time'] < 15:
            delivery.append(_['phone'])
    return delivery


def generate_access_token():
    _ = requests.post(config.TOKEN_URL,
                      headers={"Authorization": "Basic " + base64.b64encode(config.PB_KEY + ':' + config.PB_SECRET),
                               "Content-Type" : 'application/x-www-form-urlencoded'},
                      data={"grant_type": "client_credentials"})
    return json.loads(_.content)['access_token']


if __name__ == "__main__":
    # start="A-312, SVR Flora Apartments ,Kudlu Road , Somasundarapalya, Bengaluru, Karnataka"
    print generate_access_token()
    print coordinates("A-312, SVR Flora Apartments ,Kudlu Road , Somasundarapalya, Bengaluru, Karnataka")

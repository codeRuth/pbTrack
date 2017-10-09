from pymongo import MongoClient
import googlemaps
import config

gmaps = googlemaps.Client(key=config.GOOGLE_MAPS_API)


def coordinates(start=None):
    client = MongoClient(config.MONGO_URL)
    db = client.get_database()
    customer_db = db.delivery.find({})

    delivery = list([])

    for _ in customer_db:
        add = str(_['address'])

        geocode_result = gmaps.geocode(add)
        res = gmaps.distance_matrix(
            str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(
                geocode_result[0]['geometry']['location']['lng']),
            '12.9817406,77.5447453',
            mode='driving', units='metric')

        distance = res['rows'][0]['elements'][0]['duration']['value']
        time = res['rows'][0]['elements'][0]['distance']['value']

        if distance < 3000 or time < 1000:
            delivery.append(str(_['phone']))
    return delivery


if __name__ == "__main__":
    print coordinates()

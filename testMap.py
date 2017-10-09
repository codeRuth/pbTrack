import googlemaps
from datetime import datetime
import config

gmaps = googlemaps.Client(key=config.GOOGLE_MAPS_API)

# Geocoding an address
geocode_result = gmaps.geocode('A-312, SVR Flora Apartments ,Kudlu Road , Somasundarapalya, Bengaluru, Karnataka')

print geocode_result[0]['geometry']['location']['lat']

print geocode_result[0]['geometry']['location']['lng']

res = gmaps.distance_matrix(
    str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng']),
    '12.9817406,77.5447453',
    mode='driving', units='metric')

print res['rows'][0]['elements'][0]['duration']['value']
print res['rows'][0]['elements'][0]['distance']['value']

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

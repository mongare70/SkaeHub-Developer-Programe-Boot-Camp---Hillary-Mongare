from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocater = Nominatim(user_agent="http")

# latitude and longitude (Nairobi)
latitude = -1.3031689499999999
longitude = 36.826061224105075

# implement reverse function 
location = geolocater.reverse("{},{}".format(latitude, longitude))

# get city, state, and country of location
address = location.raw['address']
city = address.get('city', '')
state = address.get('city', '')
country = address.get('country', '')

print('The city is: {}'.format(city))
print('The state is: {}'.format(state))
print('The country is: {}'.format(country))




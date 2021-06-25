from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocater = Nominatim(user_agent="http")

# state input
state = input("Enter State Name: ")

# get location of state
location = geolocater.geocode(state)

# get latitude and longitude of state
latitude = location.latitude
longitude = location.longitude

# implement reverse function 
location = geolocater.reverse("{},{}".format(latitude, longitude))

# get city, state, and country of location
address = location.raw['address']
country = address.get('country', '')

# country output
print('{} is in {} country.'.format(state, country))

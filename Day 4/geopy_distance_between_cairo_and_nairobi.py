from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Initialize Nominatim API
geolocater = Nominatim(user_agent="http")

# Get Nairobi
str_nairobi = 'Nairobi'
nairobi = geolocater.geocode(str_nairobi)

# Get Cairo
str_cairo = 'Cairo'
cairo = geolocater.geocode(str_cairo)


# loading the latitude-longitude data for Nairobi and Cairo
nairobi = (nairobi.latitude, nairobi.longitude)
cairo = (cairo.latitude, cairo.longitude)

# Print distance between Cairo and Nairobi in km using geodesic
print(geodesic(cairo, nairobi).km)

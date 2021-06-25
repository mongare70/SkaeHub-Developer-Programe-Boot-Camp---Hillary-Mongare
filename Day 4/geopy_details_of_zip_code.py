from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocater = Nominatim(user_agent="http")

# Zip code
zip_code = input("Enter any Zip Code: ")

# Get location
location = geolocater.geocode(zip_code)

# Output location details 
print(location.address)
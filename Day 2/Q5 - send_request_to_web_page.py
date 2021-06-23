#import requests module
import requests

#request with timeout
try:
    res = requests.get('http://httpbin.org/delay/2', timeout=1)

except requests.Timeout as err:
    print(err)
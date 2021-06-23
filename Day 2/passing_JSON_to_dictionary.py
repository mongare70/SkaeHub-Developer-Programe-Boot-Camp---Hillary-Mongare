import urllib.request, json

#function to get JSON from webpage
def readJSON(url):
    with urllib.request.urlopen(url) as url:
        #json.loads() returns a dict object
        data = json.loads(url.read().decode())
        return data

url = "https://catfact.ninja/fact"

x = readJSON(url)

print(x)

print(type(x))
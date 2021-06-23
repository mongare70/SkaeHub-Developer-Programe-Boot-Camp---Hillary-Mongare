#import requests module
import requests

res = requests.get('https://skaehub.com')

print("\n==============================================================================")

#Print response text
print("Response text: ")
print(res.text)

print("\n==============================================================================")

#Print response content
print("Content: ")
print(res.content)

print("\n==============================================================================")

#Print raw socket response
print("Raw response:")
print(res.raw)
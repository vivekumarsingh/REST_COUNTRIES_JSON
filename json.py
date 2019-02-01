import requests
import json
r = requests.get("https://restcountries.eu/rest/v2/region/europe")
print(r.text)
for a in r.json():
    r = a['regionalBlocs']   #("this is array")
for b in r:
    print(b['name'])
  

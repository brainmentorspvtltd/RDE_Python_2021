import urllib.request as url
import json

response = url.urlopen("https://data.covid19india.org/states_daily.json")
data = json.load(response)
states = data['states_daily']
print(states[1200])

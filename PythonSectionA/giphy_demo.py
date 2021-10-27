import urllib.request as url
import json

imgName = input("Search Here... ")
imgName = imgName.replace(" ", "+")

path = f"http://api.giphy.com/v1/gifs/search?q={imgName}&api_key=bc56161131654faeb550630b83e0c977&limit=20"
response = url.urlopen(path)
data = json.load(response)
data = data['data']
for i in range(20):
    img_url = data[i]['images']['original']['url']
    url.urlretrieve(img_url, f'images/img_{i}.gif')
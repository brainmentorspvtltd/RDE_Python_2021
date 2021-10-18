import urllib.request as url
import json

path = "http://api.giphy.com/v1/gifs/search?q=virat+kohli&api_key=bc56161131654faeb550630b83e0c977&limit=10"
response = url.urlopen(path)
data = json.load(response)
data = data['data']
for i in range(len(data)):
    images = data[i]['images']
    img_path = images['original']['url']
    url.urlretrieve(img_path, f'images/img_{i}.gif')
    print("Downloaded...",i)

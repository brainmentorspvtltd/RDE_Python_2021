import json
import urllib.request as url

to_search = input("Search here : ")
to_search = to_search.replace(" ", "+")

path = f"http://api.giphy.com/v1/gifs/search?q={to_search}&api_key=bc56161131654faeb550630b83e0c977&limit=20"
response = url.urlopen(path)
data = json.load(response)
data = data['data']

for i in range(20):
    img_url = data[i]['images']['downsized_large']['url']
    url.urlretrieve(img_url, 'images/img_{}.gif'.format(i))
    print(i,"downloaded...")
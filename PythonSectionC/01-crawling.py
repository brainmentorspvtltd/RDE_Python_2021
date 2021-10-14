import urllib.request as url
import bs4

path="https://www.flipkart.com/search?q=samsung+galaxy+f12"

response = url.urlopen(path)
html = bs4.BeautifulSoup(response)
title = html.find('div', class_='_4rR01T')
print(title.text)

price = html.find('div', class_='_30jeq3 _1_WHN1')
print(price.text)

rating = html.find('div', class_='_3LWZlK')
print(rating.text)


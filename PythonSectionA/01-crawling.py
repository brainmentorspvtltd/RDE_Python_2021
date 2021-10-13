import bs4
import urllib.request as url
path = "https://www.flipkart.com/search?q=tv"

response = url.urlopen(path)
html = bs4.BeautifulSoup(response, 'lxml')
title = html.find('div', class_='_4rR01T')
print(title.text)

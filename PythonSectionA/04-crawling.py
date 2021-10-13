import bs4
import urllib.request as url
path = "https://www.jansatta.com/khel"

response = url.urlopen(path)
html = bs4.BeautifulSoup(response, 'lxml')
title = html.find_all('div', class_='entry-title')
for i in range(len(title)):
    print(title[i].text)

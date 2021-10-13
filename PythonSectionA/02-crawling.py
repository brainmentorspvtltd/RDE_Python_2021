import bs4
import urllib.request as url
path = "https://www.flipkart.com/search?q=iphone+12"

response = url.urlopen(path)
html = bs4.BeautifulSoup(response, 'lxml')
title = html.find_all('div', class_='_4rR01T')
price = html.find_all('div', class_='_30jeq3 _1_WHN1')
for i in range(len(title)):
    print(title[i].text)
    print(price[i].text)

import bs4
import urllib.request as url

path="https://www.flipkart.com/search?q=tv"
response=url.urlopen(path)
HTML=bs4.BeautifulSoup(response, 'lxml')
title=HTML.find('div',class_='_4rR01T')
price=HTML.find('div',class_='_30jeq3 _1_WHN1')
print(title.text)
print(price.text)

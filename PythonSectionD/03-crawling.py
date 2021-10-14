import urllib.request as url
import bs4

path = "https://www.jansatta.com/"

response = url.urlopen(path)
html = bs4.BeautifulSoup(response)
titles = html.find_all('h3', class_='entry-title')
for i in range(len(titles)):
    print(titles[i].text)

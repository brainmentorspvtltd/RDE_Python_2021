import urllib.request as url
import bs4

for i in range(1,5):
    print(f"Page {i}")
    path=f"https://www.flipkart.com/search?q=iphone+12&page={i}"

    response = url.urlopen(path)
    html = bs4.BeautifulSoup(response)
    titles = html.find_all('div', class_='_4rR01T')
    priceList = html.find_all('div', class_='_30jeq3 _1_WHN1')
    ratingList = html.find_all('div', class_='_3LWZlK')

    for j in range(len(titles)):
        print("Title ::",titles[j].text)
        print("Price ::",priceList[j].text)
        print("Rating ::",ratingList[j].text)
        print(f"{j} ::","*"*40)





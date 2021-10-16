import bs4
import urllib.request as url
product = input("Enter Product name : ")
product = product.replace(' ', '+')
k = 0
for j in range (1,5):
    path=f"https://www.flipkart.com/search?q={product}&page={j}"
    response=url.urlopen(path)
    HTML=bs4.BeautifulSoup(response, 'lxml')
    titlelist=HTML.find_all('div',class_='_4rR01T')
    pricelist=HTML.find_all('div',class_='_30jeq3 _1_WHN1')
    imgList = HTML.find_all('img', class_='_396cs4 _3exPp9')
    for i in range (len(titlelist)):
        print(titlelist[i].text)
        print(pricelist[i].text)
        k += 1
        url.urlretrieve(imgList[i]['src'], f'images/img_{k}.png')


import bs4
import urllib.request as url
path = "https://www.imdb.com/title/tt2631186/?ref_=nv_sr_srsg_0"

response = url.urlopen(path)
html = bs4.BeautifulSoup(response, 'lxml')
title = html.find('h1', class_='TitleHeader__TitleText-sc-1wu6n3d-0')
print(title.text)
rating = html.find('span', class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV')
print(rating.text)
summary = html.find('span', class_='GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA')
print(summary.text)


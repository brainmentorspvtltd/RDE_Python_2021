Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> import urllib.request as url
>>> path = "https://data.covid19india.org/states_daily.json"
>>> url.urlopen(path)
<http.client.HTTPResponse object at 0x0000013D59A1F2E0>
>>> response = url.urlopen(path)
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['states_daily'])
>>> states = data['states']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    states = data['states']
KeyError: 'states'
>>> states = data['states_daily']
>>> type(states)
<class 'list'>
>>> len(states)
1563
>>> len(states) / 3
521.0
>>> states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
>>> states[1000]
{'an': '0', 'ap': '121', 'ar': '0', 'as': '17', 'br': '60', 'ch': '26', 'ct': '312', 'date': '10-Feb-21', 'dateymd': '2021-02-10', 'dd': '0', 'dl': '131', 'dn': '0', 'ga': '64', 'gj': '495', 'hp': '49', 'hr': '107', 'jh': '42', 'jk': '32', 'ka': '322', 'kl': '5745', 'la': '3', 'ld': '25', 'mh': '2421', 'ml': '4', 'mn': '39', 'mp': '175', 'mz': '3', 'nl': '3', 'or': '81', 'pb': '180', 'py': '32', 'rj': '89', 'sk': '3', 'status': 'Recovered', 'tg': '163', 'tn': '493', 'tr': '0', 'tt': '11796', 'un': '0', 'up': '166', 'ut': '110', 'wb': '283'}
>>> path = "http://api.giphy.com/v1/gifs/search?q=tom+and+jerry&api_key=bc56161131654faeb550630b83e0c977&limit=20"
>>> response = url.urlopen(path)
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['data', 'pagination', 'meta'])
>>> data = data['data']
>>> type(data)
<class 'list'>
>>> len(data)
20
>>> data[0]
{'type': 'gif', 'id': '6BZaFXBVPBtok', 'url': 'https://giphy.com/gifs/bad-6BZaFXBVPBtok', 'slug': 'bad-6BZaFXBVPBtok', 'bitly_gif_url': 'http://gph.is/145nxxG', 'bitly_url': 'http://gph.is/145nxxG', 'embed_url': 'https://giphy.com/embed/6BZaFXBVPBtok', 'username': '', 'source': 'http://www.reactiongifs.com/spanking/?utm_source=rss&utm_medium=rss&utm_campaign=spanking', 'title': 'Tom And Jerry Reaction GIF', 'rating': 'pg', 'content_url': '', 'source_tld': 'www.reactiongifs.com', 'source_post_url': 'http://www.reactiongifs.com/spanking/?utm_source=rss&utm_medium=rss&utm_campaign=spanking', 'is_sticker': 0, 'import_datetime': '2013-07-24 16:40:05', 'trending_datetime': '2017-08-30 01:30:01', 'images': {'original': {'height': '364', 'width': '500', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif', 'mp4_size': '78495', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.mp4', 'webp_size': '111810', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.webp', 'frames': '5', 'hash': '36d97e49c12da10a279d75133e99bee9'}, 'downsized': {'height': '364', 'width': '500', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif'}, 'downsized_large': {'height': '364', 'width': '500', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif'}, 'downsized_medium': {'height': '364', 'width': '500', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif'}, 'downsized_small': {'height': '364', 'width': '500', 'mp4_size': '97733', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy-downsized-small.mp4'}, 'downsized_still': {'height': '364', 'width': '500', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy_s.gif'}, 'fixed_height': {'height': '200', 'width': '275', 'size': '83961', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200.gif', 'mp4_size': '28533', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200.mp4', 'webp_size': '39468', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200.webp'}, 'fixed_height_downsampled': {'height': '200', 'width': '275', 'size': '83961', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200_d.gif', 'webp_size': '55148', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200_d.webp'}, 'fixed_height_small': {'height': '100', 'width': '138', 'size': '29605', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100.gif', 'mp4_size': '10315', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100.mp4', 'webp_size': '14836', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100.webp'}, 'fixed_height_small_still': {'height': '100', 'width': '138', 'size': '6776', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100_s.gif'}, 'fixed_height_still': {'height': '200', 'width': '275', 'size': '17792', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200_s.gif'}, 'fixed_width': {'height': '146', 'width': '200', 'size': '69437', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200w.gif', 'mp4_size': '18074', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200w.mp4', 'webp_size': '25390', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200w.webp'}, 'fixed_width_downsampled': {'height': '146', 'width': '200', 'size': '69437', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200w_d.gif', 'webp_size': '33312', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200w_d.webp'}, 'fixed_width_small': {'height': '73', 'width': '100', 'size': '18023', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100w.gif', 'mp4_size': '6930', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100w.mp4', 'webp_size': '9216', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100w.webp'}, 'fixed_width_small_still': {'height': '73', 'width': '100', 'size': '4431', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/100w_s.gif'}, 'fixed_width_still': {'height': '146', 'width': '200', 'size': '13984', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/200w_s.gif'}, 'looping': {'mp4_size': '2722405', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy-loop.mp4'}, 'original_still': {'height': '364', 'width': '500', 'size': '89235', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy_s.gif'}, 'original_mp4': {'height': '348', 'width': '480', 'mp4_size': '78495', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.mp4'}, 'preview': {'height': '258', 'width': '354', 'mp4_size': '26923', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy-preview.mp4'}, 'preview_gif': {'height': '111', 'width': '152', 'size': '49882', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy-preview.gif'}, 'preview_webp': {'height': '232', 'width': '318', 'size': '39286', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy-preview.webp'}, '480w_still': {'height': '349', 'width': '480', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/480w_s.jpg'}}, 'analytics_response_payload': 'e=Z2lmX2lkPTZCWmFGWEJWUEJ0b2smZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD00ZDkwZDIwN3NtMHh2aHQ0dzR2YWY0YzJsN3FkcXJlMzFjNXRtbDQ2eDYxdm5xMTEmY3Q9Zw', 'analytics': {'onload': {'url': 'https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX2lkPTZCWmFGWEJWUEJ0b2smZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD00ZDkwZDIwN3NtMHh2aHQ0dzR2YWY0YzJsN3FkcXJlMzFjNXRtbDQ2eDYxdm5xMTEmY3Q9Zw&action_type=SEEN'}, 'onclick': {'url': 'https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX2lkPTZCWmFGWEJWUEJ0b2smZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD00ZDkwZDIwN3NtMHh2aHQ0dzR2YWY0YzJsN3FkcXJlMzFjNXRtbDQ2eDYxdm5xMTEmY3Q9Zw&action_type=CLICK'}, 'onsent': {'url': 'https://giphy-analytics.giphy.com/v2/pingback_simple?analytics_response_payload=e%3DZ2lmX2lkPTZCWmFGWEJWUEJ0b2smZXZlbnRfdHlwZT1HSUZfU0VBUkNIJmNpZD00ZDkwZDIwN3NtMHh2aHQ0dzR2YWY0YzJsN3FkcXJlMzFjNXRtbDQ2eDYxdm5xMTEmY3Q9Zw&action_type=SENT'}}}
>>> data[0]['downsized_large']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data[0]['downsized_large']
KeyError: 'downsized_large'
>>> data[0].keys()
dict_keys(['type', 'id', 'url', 'slug', 'bitly_gif_url', 'bitly_url', 'embed_url', 'username', 'source', 'title', 'rating', 'content_url', 'source_tld', 'source_post_url', 'is_sticker', 'import_datetime', 'trending_datetime', 'images', 'analytics_response_payload', 'analytics'])
>>> data[0]['images']['downsized_large']
{'height': '364', 'width': '500', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif'}
>>> data[0]['images']['downsized_large']['url']
'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif'
>>> 
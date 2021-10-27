Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request as url
>>> path = "https://data.covid19india.org/states_daily.json"
>>> url.urlopen(path)
<http.client.HTTPResponse object at 0x0000024BB2278D90>
>>> response = url.urlopen(path)
>>> import json
>>> data = json.load(response)
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['states_daily'])
>>> states = data["states"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    states = data["states"]
KeyError: 'states'
>>> states = data["states_daily"]
>>> len(states)
1563
>>> len(states) / 3
521.0
>>> states[100]
{'an': '1', 'ap': '0', 'ar': '0', 'as': '3', 'br': '8', 'ch': '0', 'ct': '6', 'date': '16-Apr-20', 'dateymd': '2020-04-16', 'dd': '0', 'dl': '11', 'dn': '0', 'ga': '0', 'gj': '9', 'hp': '3', 'hr': '8', 'jh': '0', 'jk': '2', 'ka': '2', 'kl': '27', 'la': '2', 'ld': '0', 'mh': '5', 'ml': '0', 'mn': '0', 'mp': '6', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '2', 'py': '0', 'rj': '17', 'sk': '0', 'status': 'Recovered', 'tg': '68', 'tn': '62', 'tr': '0', 'tt': '258', 'un': '0', 'up': '11', 'ut': '0', 'wb': '5'}
>>> states[300]
{'an': '0', 'ap': '443', 'ar': '9', 'as': '267', 'br': '228', 'ch': '5', 'ct': '47', 'date': '22-Jun-20', 'dateymd': '2020-06-22', 'dd': '0', 'dl': '2909', 'dn': '15', 'ga': '46', 'gj': '563', 'hp': '54', 'hr': '390', 'jh': '42', 'jk': '132', 'ka': '249', 'kl': '138', 'la': '10', 'ld': '0', 'mh': '3721', 'ml': '2', 'mn': '57', 'mp': '175', 'mz': '1', 'nl': '69', 'or': '143', 'pb': '161', 'py': '17', 'rj': '302', 'sk': '0', 'status': 'Confirmed', 'tg': '872', 'tn': '2710', 'tr': '16', 'tt': '13560', 'un': '-1295', 'up': '591', 'ut': '58', 'wb': '413'}
>>> states[1300]
{'an': '16', 'ap': '20811', 'ar': '206', 'as': '4987', 'br': '10151', 'ch': '790', 'ct': '9867', 'date': '21-May-21', 'dateymd': '2021-05-21', 'dd': '0', 'dl': '7288', 'dn': '95', 'ga': '3075', 'gj': '8783', 'hp': '4535', 'hr': '13486', 'jh': '4117', 'jk': '4466', 'ka': '52581', 'kl': '41032', 'la': '110', 'ld': '177', 'mh': '44493', 'ml': '419', 'mn': '1247', 'mp': '9405', 'mz': '114', 'nl': '225', 'or': '10881', 'pb': '8652', 'py': '2017', 'rj': '18264', 'sk': '261', 'status': 'Recovered', 'tg': '4801', 'tn': '24478', 'tr': '379', 'tt': '357625', 'un': '0', 'up': '17668', 'ut': '8731', 'wb': '19017'}
>>> states[1301]
{'an': '2', 'ap': '104', 'ar': '3', 'as': '81', 'br': '98', 'ch': '14', 'ct': '96', 'date': '21-May-21', 'dateymd': '2021-05-21', 'dd': '0', 'dl': '252', 'dn': '0', 'ga': '30', 'gj': '65', 'hp': '57', 'hr': '112', 'jh': '46', 'jk': '43', 'ka': '353', 'kl': '142', 'la': '1', 'ld': '2', 'mh': '1263', 'ml': '25', 'mn': '15', 'mp': '79', 'mz': '0', 'nl': '13', 'or': '27', 'pb': '172', 'py': '26', 'rj': '129', 'sk': '3', 'status': 'Deceased', 'tg': '25', 'tn': '467', 'tr': '2', 'tt': '4194', 'un': '0', 'up': '172', 'ut': '116', 'wb': '159'}
>>> states[1201]
{'an': '54', 'ap': '2343', 'ar': '3', 'as': '159', 'br': '3460', 'ch': '411', 'ct': '14556', 'date': '18-Apr-21', 'dateymd': '2021-04-18', 'dd': '0', 'dl': '20159', 'dn': '50', 'ga': '531', 'gj': '3981', 'hp': '532', 'hr': '3489', 'jh': '1551', 'jk': '963', 'ka': '4603', 'kl': '4565', 'la': '84', 'ld': '4', 'mh': '45654', 'ml': '41', 'mn': '7', 'mp': '7495', 'mz': '26', 'nl': '8', 'or': '1309', 'pb': '3141', 'py': '282', 'rj': '3084', 'sk': '5', 'status': 'Recovered', 'tg': '1555', 'tn': '5925', 'tr': '7', 'tt': '143839', 'un': '0', 'up': '9041', 'ut': '708', 'wb': '4053'}
>>> states[1201]['tt']
'143839'
>>> states[1202]['tt']
'1620'
>>> states[1202]
{'an': '0', 'ap': '22', 'ar': '0', 'as': '6', 'br': '27', 'ch': '3', 'ct': '170', 'date': '18-Apr-21', 'dateymd': '2021-04-18', 'dd': '0', 'dl': '161', 'dn': '0', 'ga': '11', 'gj': '110', 'hp': '10', 'hr': '29', 'jh': '50', 'jk': '6', 'ka': '81', 'kl': '25', 'la': '0', 'ld': '0', 'mh': '503', 'ml': '1', 'mn': '0', 'mp': '66', 'mz': '0', 'nl': '0', 'or': '2', 'pb': '68', 'py': '3', 'rj': '42', 'sk': '0', 'status': 'Deceased', 'tg': '15', 'tn': '42', 'tr': '0', 'tt': '1620', 'un': '0', 'up': '127', 'ut': '12', 'wb': '28'}
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
>>> data[0]['images']

>>> data[0]['images'].keys()
dict_keys(['original', 'downsized', 'downsized_large', 'downsized_medium', 'downsized_small', 'downsized_still', 'fixed_height', 'fixed_height_downsampled', 'fixed_height_small', 'fixed_height_small_still', 'fixed_height_still', 'fixed_width', 'fixed_width_downsampled', 'fixed_width_small', 'fixed_width_small_still', 'fixed_width_still', 'looping', 'original_still', 'original_mp4', 'preview', 'preview_gif', 'preview_webp', '480w_still'])
>>> data[0]['images']['original']
{'height': '364', 'width': '500', 'size': '329468', 'url': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif', 'mp4_size': '78495', 'mp4': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.mp4', 'webp_size': '111810', 'webp': 'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.webp', 'frames': '5', 'hash': '36d97e49c12da10a279d75133e99bee9'}
>>> data[0]['images']['original']['url']
'https://media2.giphy.com/media/6BZaFXBVPBtok/giphy.gif'
>>> 
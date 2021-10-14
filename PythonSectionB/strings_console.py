Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world, this is Python Programming.."
>>> type(text)
<class 'str'>
>>> len(text)
41
>>> text[0]
'h'
>>> text[12]
' '
>>> text[40]
'.'
>>> text[25]
'o'
>>> text[-1]
'.'
>>> text
'hello world, this is Python Programming..'
>>> text[-2]
'.'
>>> text[-3]
'g'
>>> text[0:4]
'hell'
>>> text[10:40]
'd, this is Python Programming.'
>>> text[:]
'hello world, this is Python Programming..'
>>> text[20:]
' Python Programming..'
>>> text[:20]
'hello world, this is'
>>> text[10:0]
''
>>> text[0:20]
'hello world, this is'
>>> text[0:20:2]
'hlowrd hsi'
>>> text[10:0:-1]
'dlrow olle'
>>> text[10::-1]
'dlrow olleh'
>>> text[::-1]
'..gnimmargorP nohtyP si siht ,dlrow olleh'
>>> text
'hello world, this is Python Programming..'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'..gnimmar'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world, this is python programming..'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING..'
>>> text.capitalize()
'Hello world, this is python programming..'
>>> text.title()
'Hello World, This Is Python Programming..'
>>> text.swapcase()
'HELLO WORLD, THIS IS pYTHON pROGRAMMING..'
>>> text.count('o')
4
>>> text.count('i')
3
>>> text.count('p')
0
>>> text.count('P')
2
>>> text.count('is')
2
>>> text.find('d')
10
>>> text.find('o')
4
>>> text.find('o',0)
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',26)
30
>>> text.find('o',31)
-1
>>> text.index('o')
4
>>> text.index('o',5)
7
>>> text.index('o',31)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    text.index('o',31)
ValueError: substring not found
>>> text.replace('h','i')
'iello world, tiis is Pytion Programming..'
>>> text
'hello world, this is Python Programming..'
>>> text[0] = 'i'
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    text[0] = 'i'
TypeError: 'str' object does not support item assignment
>>> del text[0]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
>>> text.isalnum()
False
>>> text.isalpha()
False
>>> text.islower()
False
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING..'
>>> text.isupper()
False
>>> text.split()
['hello', 'world,', 'this', 'is', 'Python', 'Programming..']
>>> text.split(',')
['hello world', ' this is Python Programming..']
>>> text = "     hello    "
>>> text.strip()
'hello'
>>> text.lstrip()
'hello    '
>>> text.rstrip()
'     hello'
>>> text.strip()
'hello'
>>> text.rfind('o')
9
>>> text
'     hello    '
>>> 
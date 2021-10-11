Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello World, this is Python Programming"
>>> len(text)
39
>>> text[0]
'H'
>>> text[32]
'r'
>>> text[0] = 'I'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    text[0] = 'I'
TypeError: 'str' object does not support item assignment
>>> del text[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
>>> text
'Hello World, this is Python Programming'
>>> text[-1]
'g'
>>> text[-10]
'r'
>>> text[0:4]
'Hell'
>>> text[0:100]
'Hello World, this is Python Programming'
>>> text[0:]
'Hello World, this is Python Programming'
>>> text[:10]
'Hello Worl'
>>> text[:]
'Hello World, this is Python Programming'
>>> text[10:20]
'd, this is'
>>> text[10:30]
'd, this is Python Pr'
>>> text[10:0]
''
>>> text[0:10:2]
'HloWr'
>>> text[0:10:1]
'Hello Worl'
>>> text[0:20:2]
'HloWrd hsi'
>>> text[0:40:2]
'HloWrd hsi yhnPormig'
>>> text[10:0:1]
''
>>> text[10:0:-1]
'dlroW olle'
>>> text[10::-1]
'dlroW olleH'
>>> text[::-1]
'gnimmargorP nohtyP si siht ,dlroW olleH'
>>> text
'Hello World, this is Python Programming'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.swapcase()
'hELLO wORLD, THIS IS pYTHON pROGRAMMING'
>>> text.count('x')
0
>>> text.count('y')
1
>>> text.count('a')
1
>>> text.count('p')
0
>>> text
'Hello World, this is Python Programming'
>>> text.count('[')
0
>>> text.count('P')
2
>>> text.count('o')
4
>>> text.count('i')
3
>>> text.index('i')
15
>>> text.index('i',0)
15
>>> text.index('o',0)
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> text.index('o',31)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    text.index('o',31)
ValueError: substring not found
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',26)
30
>>> text.find('o',31)
-1
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text = "      hello      "
>>> text.strip()
'hello'
>>> text.lstrip()
'hello      '
>>> text.rstrip()
'      hello'
>>> 